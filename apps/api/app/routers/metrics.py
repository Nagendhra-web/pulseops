from fastapi import APIRouter

from app.schemas import MetricSeries
from app.services.metrics import get_metric_series


router = APIRouter()


@router.get("/dau", response_model=MetricSeries)
async def dau() -> MetricSeries:
    return await get_metric_series("dau")


@router.get("/revenue", response_model=MetricSeries)
async def revenue() -> MetricSeries:
    return await get_metric_series("revenue")


@router.get("/churn", response_model=MetricSeries)
async def churn() -> MetricSeries:
    return await get_metric_series("churn")
