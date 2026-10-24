-- Bound parameters keep the requested period separate from SQL syntax.
-- Rank revisions within each roster day, then attach schedule provenance.
WITH ranked AS (
    SELECT id, saved_at_utc, payload_json,
           json_extract(payload_json, '$.date') AS roster_date,
           ROW_NUMBER() OVER (
               PARTITION BY json_extract(payload_json, '$.date')
               ORDER BY saved_at_utc DESC, id DESC
           ) AS revision_rank
    FROM roster_revisions
)
SELECT r.id, r.roster_date, r.saved_at_utc, s.source_file,
       json_extract(r.payload_json, '$.routeTarget') AS route_target
FROM ranked AS r
LEFT JOIN roster_schedule_sources AS s
  ON s.source_hash = json_extract(r.payload_json, '$.scheduleHash')
WHERE r.revision_rank = 1
  AND r.roster_date BETWEEN :start_date AND :end_date
ORDER BY r.roster_date;
