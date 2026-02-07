# PulseOps

PulseOps is a real-time analytics and anomaly detection platform designed for modern product and revenue teams. It ingests streaming events, models KPIs, detects anomalies, and serves an executive dashboard with explanations.

```
Event Producer -> Redpanda (Kafka) -> Ingestion Service -> DuckDB -> dbt Models
                                              |                              |
                                              v                              v
                                     Anomaly Detection Engine --------> FastAPI
                                                                              |
                                                                              v
                                                                         Next.js
```

## Local setup

1. Copy environment variables:
   - `cp .env.example .env`
2. Start the stack:
   - `docker compose -f infra/docker-compose.yml up --build`
3. Generate events (from another terminal):
   - `docker compose -f infra/docker-compose.yml run --rm producer`
4. Open the dashboard:
   - `http://localhost:3000`
5. Optional: run dbt models locally:
   - `cp analytics/dbt/profiles.yml.example ~/.dbt/profiles.yml`
   - `dbt run --project-dir analytics/dbt`

## Services

- `Redpanda` runs Kafka-compatible streaming.
- `FastAPI` serves KPI and anomaly endpoints.
- `Next.js` renders the executive dashboard.
- `DuckDB` is the analytics warehouse (local file in `analytics/warehouse`).
- `dbt` models live in `analytics/dbt`.

## Screenshots

- KPI overview
- Anomaly feed
- Revenue trends

## Repository layout

- `apps/api`: FastAPI backend + ingestion worker
- `apps/web`: Next.js 14 dashboard
- `analytics/dbt`: dbt models and tests
- `analytics/warehouse`: DuckDB files
- `streaming/producer`: Kafka event generator
- `ml/anomaly_engine`: Detection + explanations
- `infra/docker-compose.yml`: Local stack
- `docs`: Architecture and metrics definitions

