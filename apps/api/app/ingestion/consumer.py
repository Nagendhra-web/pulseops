import json
from confluent_kafka import Consumer

from app.core.config import settings
from app.ingestion.service import ingest_event


def consume_events() -> None:
    consumer = Consumer(
        {
            "bootstrap.servers": settings.kafka_brokers,
            "group.id": settings.kafka_group_id,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False,
        }
    )
    consumer.subscribe([settings.kafka_topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                continue
            event = json.loads(msg.value().decode("utf-8"))
            ingest_event(event)
            consumer.commit(message=msg, asynchronous=False)
    finally:
        consumer.close()
