import duckdb

from app.core.config import settings


def get_connection() -> duckdb.DuckDBPyConnection:
    return duckdb.connect(database=settings.duckdb_path, read_only=False)


def table_exists(conn: duckdb.DuckDBPyConnection, table_name: str) -> bool:
    result = conn.execute(
        "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = ?",
        [table_name],
    ).fetchone()
    return bool(result and result[0] > 0)
