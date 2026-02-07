from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class MetricPoint(BaseModel):
    date: date
    value: float


class MetricSeries(BaseModel):
    name: str
    points: List[MetricPoint]


class AnomalyDetail(BaseModel):
    date: date
    metric: str
    value: float
    score: float
    explanation: str
    top_dimensions: dict


class AnomalyResponse(BaseModel):
    anomalies: List[AnomalyDetail]
    total_anomalies: int
    lookback_days: int
