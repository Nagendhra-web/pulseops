FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir dbt-core dbt-duckdb

COPY analytics/dbt /app

ENV DBT_PROFILES_DIR=/app

CMD ["bash", "runner.sh"]
