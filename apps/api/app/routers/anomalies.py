from fastapi import APIRouter

from app.schemas import AnomalyResponse
from app.services.anomalies import get_anomalies


router = APIRouter()


@router.get("/anomalies", response_model=AnomalyResponse)
async def anomalies() -> AnomalyResponse:
    return await get_anomalies()
