from typing import Dict


def _format_dimension(dim_values: list) -> str:
    if not dim_values:
        return "no dominant segments"
    top = dim_values[0]
    return f"top segment {top['value']} ({top['count']} events)"


def build_explanation(metric: str, value: float, score: float, top_dimensions: Dict) -> str:
    country_hint = _format_dimension(top_dimensions.get("country", []))
    plan_hint = _format_dimension(top_dimensions.get("plan", []))
    event_hint = _format_dimension(top_dimensions.get("event_type", []))
    return (
        f"{metric.upper()} deviated from expected levels. "
        f"Anomaly score {score:.2f}. "
        f"Key contributors: {country_hint}, {plan_hint}, {event_hint}."
    )
