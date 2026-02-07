EVENT_SCHEMA = {
    "type": "object",
    "required": [
        "event_id",
        "event_type",
        "user_id",
        "plan",
        "country",
        "event_timestamp",
    ],
}


def validate_event(event: dict) -> bool:
    for key in EVENT_SCHEMA["required"]:
        if key not in event:
            return False
    return True
