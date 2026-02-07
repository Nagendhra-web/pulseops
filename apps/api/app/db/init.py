from app.db.duckdb import get_connection


def init_db() -> None:
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS raw_events (
            event_id VARCHAR PRIMARY KEY,
            event_type VARCHAR,
            user_id VARCHAR,
            plan VARCHAR,
            country VARCHAR,
            amount DOUBLE,
            event_timestamp TIMESTAMP,
            event_date DATE,
            raw JSON
        );
        """
    )
    conn.close()
