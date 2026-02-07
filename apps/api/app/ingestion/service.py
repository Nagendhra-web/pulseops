from datetime import datetime
from typing import Dict, Any

from app.db.duckdb import get_connection


def ingest_event(event: Dict[str, Any]) -> None:
    conn = get_connection()
    timestamp = datetime.fromisoformat(event["event_timestamp"])
    event_date = timestamp.date().isoformat()
    conn.execute(
        """
        INSERT OR IGNORE INTO raw_events (
            event_id,
            event_type,
            user_id,
            plan,
            country,
            amount,
            event_timestamp,
            event_date,
            raw
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            event["event_id"],
            event["event_type"],
            event.get("user_id"),
            event.get("plan"),
            event.get("country"),
            event.get("amount"),
            timestamp,
            event_date,
            event,
        ],
    )
    conn.close()
