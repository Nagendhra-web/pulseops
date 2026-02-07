{{ config(materialized="incremental", unique_key="event_id") }}

select
    event_id,
    event_type,
    user_id,
    plan,
    country,
    amount,
    event_timestamp,
    event_date
from {{ source("pulseops", "raw_events") }}
{% if is_incremental() %}
where event_timestamp > (select max(event_timestamp) from {{ this }})
{% endif %}
