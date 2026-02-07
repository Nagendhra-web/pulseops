#!/usr/bin/env bash

set -u

INTERVAL="${DBT_RUN_INTERVAL_SEC:-60}"

while true; do
  echo "Running dbt models..."
  if ! dbt run --project-dir /app; then
    echo "dbt run failed"
  fi
  if ! dbt test --project-dir /app; then
    echo "dbt test failed"
  fi
  echo "Sleeping for ${INTERVAL}s"
  sleep "${INTERVAL}"
done
