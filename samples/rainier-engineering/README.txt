RAINIER ENGINEERING WORK SAMPLE

This independent portfolio adaptation uses fictional records only. It is not the
complete private application or a production database export.

Run: python run_sample.py
Requirements: Python 3.9+ with SQLite JSON and window-function support.
The runner uses only the standard library and an in-memory SQLite database.
It prints its results and does not access Access, the network, or employer files.

schema.sql adapts three small tables from the working application's schedule
provenance and saved-roster storage. Primary keys retain source-row identity and
revision identity. The source-record relationship is logical, not an enforced
foreign-key constraint. No extra production index is claimed.

latest_revision.sql is a NEW illustrative reporting query over those structures.
It selects the latest saved revision per day and attaches the originating
schedule. A revision's source_hash fingerprints the revision input; its payload's
scheduleHash identifies the schedule. Those two hashes must not be confused.

run_sample.py is NEW simplified sample code adapted from source validation and
revision-preservation patterns. It is not the genuine workbook parser. The
metadata check applies equally with an inferred or explicitly selected date.
The sample exercises rejection, repeat handling, conflicting revision IDs, the
reporting query and preservation of fictional source bytes.

read_only_access_export.ps1 adapts the project's read-only DAO export pattern.
Company table filters were replaced by an explicit allowlist and generic paths.
Only syntax was checked. DAO availability and actual Access export were not
executed in this portfolio task. No Slack messages or external writes are sent.

sample-results.json records the independent sample run on October 24, 2026.
The separate acceptance evidence on the website summarizes recorded October 23
tests of copied application code with manufactured workbooks and a disposable
dashboard. Those tests were not rerun here and are not human operational signoff.
