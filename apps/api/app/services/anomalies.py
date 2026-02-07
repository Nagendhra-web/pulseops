from typing import List, Dict
import pandas as pd
from fastapi.concurrency import run_in_threadpool

from app.core.config import settings
from app.db.duckdb import get_connection, table_exists
from app.db import queries
from app.schemas import AnomalyDetail, AnomalyResponse
from app.services.metrics import _read_series
from ml.anomaly_engine.engine import detect_anomalies
from ml.anomaly_engine.explainers import build_explanation
from app.services.llm import llm_client


def _top_dimensions(conn, table: str, event_date) -> Dict[str, list]:
    dimensions = ["country", "plan", "event_type"]
    results = {}
    for dimension in dimensions:
        sql = queries.EVENTS_BY_DIMENSION_QUERY.format(table=table, dimension=dimension)
        rows = conn.execute(sql, [event_date]).fetchall()
        results[dimension] = [{"value": row[0], "count": int(row[1])} for row in rows]
    return results


def _analyze() -> AnomalyResponse:
    conn = get_connection()
    table = "fact_events" if table_exists(conn, "fact_events") else "raw_events"
    anomalies: List[AnomalyDetail] = []

    for metric in ["dau", "revenue", "churn"]:
        series = _read_series(metric)
        if not series.points:
            continue
        df = pd.DataFrame(
            [{"date": p.date, "value": p.value} for p in series.points]
        )
        detected = detect_anomalies(df, value_col="value", min_points=settings.anomaly_min_points)
        for item in detected:
            top_dimensions = _top_dimensions(conn, table, item["date"])
            base_explanation = build_explanation(
                metric, item["value"], item["score"], top_dimensions
            )
            explanation = llm_client.explain(
                base_explanation,
                {
                    "metric": metric,
                    "date": item["date"],
                    "value": item["value"],
                    "top_dimensions": top_dimensions,
                },
            )
            anomalies.append(
                AnomalyDetail(
                    date=item["date"],
                    metric=metric,
                    value=float(item["value"]),
                    score=float(item["score"]),
                    explanation=explanation,
                    top_dimensions=top_dimensions,
                )
            )
    conn.close()
    return AnomalyResponse(
        anomalies=anomalies,
        total_anomalies=len(anomalies),
        lookback_days=settings.anomaly_lookback_days,
    )


async def get_anomalies() -> AnomalyResponse:
    return await run_in_threadpool(_analyze)
