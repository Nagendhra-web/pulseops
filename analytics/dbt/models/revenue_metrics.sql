{{ config(materialized="incremental", unique_key="event_date") }}

select
    event_date,
    sum(amount) as revenue
from {{ ref("fact_events") }}
where event_type = 'payment'
{% if is_incremental() %}
  and event_date > (select max(event_date) from {{ this }})
{% endif %}
group by event_date
