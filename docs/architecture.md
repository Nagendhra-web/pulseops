# Architecture

PulseOps is designed for real-time KPI monitoring with deterministic ingestion and analytics modeling.

## Design decisions

- **Redpanda for Kafka compatibility**: fast local setup, Kafka APIs for producer/consumer parity.
- **DuckDB as the analytics warehouse**: embedded OLAP engine with minimal operational overhead.
- **dbt for modeling**: clear lineage and tested metrics definitions.
- **FastAPI for serving**: async endpoints with explicit schemas.
- **Next.js dashboard**: server-rendered, executive-focused UI.
- **Anomaly engine**: STL decomposition for seasonality + Isolation Forest for outlier detection.
- **LLM interface**: pluggable design; default stub to avoid secrets and preserve determinism.

## Data flow

1. Producer generates typed JSON events into Kafka.
2. Ingestion service consumes events and writes into `raw_events` in DuckDB.
3. dbt models produce `fact_events` and KPI aggregates.
4. Anomaly engine evaluates KPI time series and attributes root causes.
5. FastAPI serves KPIs and anomalies to the dashboard.

## Runtime services

- `ingestion` container streams Kafka events into DuckDB.
- `dbt` container refreshes models on a fixed interval.

## Reliability

- Idempotent ingestion via primary key + `INSERT OR IGNORE`.
- Partition-ready storage by `event_date`.
- dbt freshness tests guard against stalled ingestion.
