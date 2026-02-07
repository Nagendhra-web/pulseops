from typing import List, Dict
import pandas as pd
from sklearn.ensemble import IsolationForest
from statsmodels.tsa.seasonal import STL


def detect_anomalies(
    df: pd.DataFrame,
    value_col: str = "value",
    min_points: int = 14,
) -> List[Dict]:
    if df.empty or len(df) < min_points:
        return []

    df = df.sort_values("date").copy()
    series = df[value_col].astype(float).fillna(0.0).values

    period = max(2, min(7, len(series) // 2))
    stl = STL(series, period=period, robust=True).fit()
    resid = stl.resid

    model = IsolationForest(
        n_estimators=200,
        contamination="auto",
        random_state=42,
    )
    model.fit(resid.reshape(-1, 1))
    preds = model.predict(resid.reshape(-1, 1))
    scores = -model.score_samples(resid.reshape(-1, 1))

    anomalies = []
    for idx, pred in enumerate(preds):
        if pred == -1:
            anomalies.append(
                {
                    "date": df.iloc[idx]["date"],
                    "value": float(series[idx]),
                    "score": float(scores[idx]),
                }
            )
    return anomalies
