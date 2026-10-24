-- Small schema excerpt adapted from schedule provenance and roster history.
-- The sample contains only fictional fixture data; it is not a database dump.
CREATE TABLE roster_schedule_sources (
    source_hash TEXT PRIMARY KEY,
    source_file TEXT,
    start_date TEXT,
    end_date TEXT,
    imported_at_utc TEXT,
    payload_json TEXT,
    source_bytes BLOB
);

CREATE TABLE roster_schedule_records (
    source_hash TEXT,
    sheet TEXT,
    source_row INTEGER,
    driver_id TEXT,
    payload_json TEXT,
    PRIMARY KEY (source_hash, sheet, source_row)
);

CREATE TABLE roster_revisions (
    id TEXT PRIMARY KEY,
    source_hash TEXT NOT NULL,
    saved_at_utc TEXT NOT NULL,
    payload_json TEXT NOT NULL
);

-- source_hash in roster_revisions fingerprints the saved revision input.
-- Its payload's scheduleHash identifies the originating schedule source.
-- The source-record relationship is logical here, not an enforced FOREIGN KEY.
-- SQLite's primary-key indexes enforce the uniqueness shown above.
