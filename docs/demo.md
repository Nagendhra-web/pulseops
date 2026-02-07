# Demo Guide

## Quick start

1. Start the stack:
   - `docker compose -f infra/docker-compose.yml up --build`
2. Run event producer:
   - `docker compose -f infra/docker-compose.yml run --rm producer`
3. Open the dashboard:
   - `http://localhost:3000`

## Optional: send synthetic traffic locally

Run the producer outside Docker:
1. Install dependencies: `pip install -r streaming/producer/requirements.txt`
2. Execute: `python streaming/producer/producer.py`
