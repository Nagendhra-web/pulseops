import os
from pydantic import BaseModel


class Settings(BaseModel):
    environment: str = os.getenv("ENVIRONMENT", "local")
    kafka_brokers: str = os.getenv("KAFKA_BROKERS", "redpanda:9092")
    kafka_topic: str = os.getenv("KAFKA_TOPIC", "pulseops.events")
    kafka_group_id: str = os.getenv("KAFKA_GROUP_ID", "pulseops-ingestion")
    duckdb_path: str = os.getenv("DUCKDB_PATH", "/data/pulseops.duckdb")
    anomaly_lookback_days: int = int(os.getenv("ANOMALY_LOOKBACK_DAYS", "30"))
    anomaly_min_points: int = int(os.getenv("ANOMALY_MIN_POINTS", "14"))
    llm_provider: str = os.getenv("LLM_PROVIDER", "stub")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")


settings = Settings()
