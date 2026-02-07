DAU_QUERY = """
SELECT
    event_date AS date,
    COUNT(DISTINCT user_id) AS dau
FROM {table}
WHERE event_date >= CURRENT_DATE - INTERVAL '{lookback_days} days'
GROUP BY event_date
ORDER BY event_date
"""

DAU_MODEL_QUERY = """
SELECT
    event_date AS date,
    dau AS value
FROM daily_active_users
WHERE event_date >= CURRENT_DATE - INTERVAL '{lookback_days} days'
ORDER BY event_date
"""

REVENUE_QUERY = """
SELECT
    event_date AS date,
    SUM(amount) AS revenue
FROM {table}
WHERE event_type = 'payment'
  AND event_date >= CURRENT_DATE - INTERVAL '{lookback_days} days'
GROUP BY event_date
ORDER BY event_date
"""

REVENUE_MODEL_QUERY = """
SELECT
    event_date AS date,
    revenue AS value
FROM revenue_metrics
WHERE event_date >= CURRENT_DATE - INTERVAL '{lookback_days} days'
ORDER BY event_date
"""

CHURN_QUERY = """
SELECT
    event_date AS date,
    COUNT(*) AS churns
FROM {table}
WHERE event_type = 'churn'
  AND event_date >= CURRENT_DATE - INTERVAL '{lookback_days} days'
GROUP BY event_date
ORDER BY event_date
"""

CHURN_MODEL_QUERY = """
SELECT
    event_date AS date,
    churns AS value
FROM churn_metrics
WHERE event_date >= CURRENT_DATE - INTERVAL '{lookback_days} days'
ORDER BY event_date
"""

EVENTS_BY_DIMENSION_QUERY = """
SELECT
    {dimension} AS dimension_value,
    COUNT(*) AS event_count
FROM {table}
WHERE event_date = ?
GROUP BY {dimension}
ORDER BY event_count DESC
LIMIT 5
"""
