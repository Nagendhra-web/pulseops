from fastapi import FastAPI

from app.core.config import settings
from app.routers.metrics import router as metrics_router
from app.routers.anomalies import router as anomalies_router
from app.db.init import init_db


app = FastAPI(title="PulseOps API", version="1.0.0")


@app.on_event("startup")
def startup() -> None:
    init_db()


app.include_router(metrics_router, prefix="/metrics", tags=["metrics"])
app.include_router(anomalies_router, prefix="/metrics", tags=["anomalies"])


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "environment": settings.environment}
