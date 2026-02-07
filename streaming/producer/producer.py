import json
import os
import random
import time
import uuid
from datetime import datetime, timezone

from confluent_kafka import Producer

from schemas import validate_event


KAFKA_BROKERS = os.getenv("KAFKA_BROKERS", "redpanda:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "pulseops.events")
SLEEP_SECONDS = float(os.getenv("PRODUCER_SLEEP_SEC", "0.5"))

COUNTRIES = ["US", "CA", "GB", "DE", "IN", "AU", "BR"]
PLANS = ["free", "starter", "growth", "enterprise"]


def generate_event() -> dict:
    event_type = random.choices(
        ["user_signup", "payment", "feature_usage", "churn"],
        weights=[0.2, 0.3, 0.4, 0.1],
    )[0]
    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "user_id": f"user_{random.randint(1000, 9999)}",
        "plan": random.choice(PLANS),
        "country": random.choice(COUNTRIES),
        "event_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if event_type == "payment":
        event["amount"] = round(random.uniform(10, 500), 2)
    if event_type == "feature_usage":
        event["feature"] = random.choice(["dashboards", "alerts", "exports"])
    return event


def main() -> None:
    producer = Producer({"bootstrap.servers": KAFKA_BROKERS})
    while True:
        event = generate_event()
        if not validate_event(event):
            continue
        producer.produce(KAFKA_TOPIC, json.dumps(event).encode("utf-8"))
        producer.flush()
        time.sleep(SLEEP_SECONDS)


if __name__ == "__main__":
    main()
