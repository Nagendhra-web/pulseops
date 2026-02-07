from typing import List
from fastapi.concurrency import run_in_threadpool

from app.core.config import settings
from app.db.duckdb import get_connection, table_exists
from app.db import queries
from app.schemas import MetricPoint, MetricSeries


def _resolve_table(conn, preferred: str) -> str:
    if table_exists(conn, preferred):
        return preferred
    return "raw_events"


def _fetch_series_sql(metric: str) -> str:
    if metric == "dau":
        return queries.DAU_QUERY
    if metric == "revenue":
        return queries.REVENUE_QUERY
    if metric == "churn":
        return queries.CHURN_QUERY
    raise ValueError(f"Unsupported metric: {metric}")


def _fetch_model_sql(metric: str) -> str:
    if metric == "dau":
        return queries.DAU_MODEL_QUERY
    if metric == "revenue":
        return queries.REVENUE_MODEL_QUERY
    if metric == "churn":
        return queries.CHURN_MODEL_QUERY
    raise ValueError(f"Unsupported metric: {metric}")


def _read_series(metric: str) -> MetricSeries:
    conn = get_connection()
    model_table = None
    if metric == "dau" and table_exists(conn, "daily_active_users"):
        model_table = "daily_active_users"
    if metric == "revenue" and table_exists(conn, "revenue_metrics"):
        model_table = "revenue_metrics"
    if metric == "churn" and table_exists(conn, "churn_metrics"):
        model_table = "churn_metrics"

    if model_table:
        sql = _fetch_model_sql(metric).format(
            lookback_days=settings.anomaly_lookback_days
        )
    else:
        preferred = "fact_events"
        table = _resolve_table(conn, preferred)
        sql = _fetch_series_sql(metric).format(
            table=table, lookback_days=settings.anomaly_lookback_days
        )
    df = conn.execute(sql).df()
    conn.close()

    if df.empty:
        return MetricSeries(name=metric, points=[])

    if "value" not in df.columns:
        df = df.rename(columns={df.columns[1]: "value"})
    points = [MetricPoint(date=row["date"], value=float(row["value"])) for _, row in df.iterrows()]
    return MetricSeries(name=metric, points=points)


async def get_metric_series(metric: str) -> MetricSeries:
    return await run_in_threadpool(_read_series, metric)


async def get_metric_series_batch(metrics: List[str]) -> List[MetricSeries]:
    results = []
    for metric in metrics:
        results.append(await get_metric_series(metric))
    return results
