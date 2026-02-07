{{ config(materialized="incremental", unique_key="event_date") }}

select
    event_date,
    count(distinct user_id) as dau
from {{ ref("fact_events") }}
{% if is_incremental() %}
where event_date > (select max(event_date) from {{ this }})
{% endif %}
group by event_date
