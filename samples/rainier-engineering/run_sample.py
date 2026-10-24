"""Run an independent fictional work sample using only Python's standard library.

Adapted from metadata validation, source preservation, and revision-review
patterns. This is not the full dashboard parser, importer, or save pipeline.
All database work is in memory. No Access file, network, or employer data is used.
"""
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import hashlib
import json
import sqlite3

HERE = Path(__file__).resolve().parent


def validate_metadata(first, second, requested_sunday=None):
    # A manually selected date must never bypass source metadata checks.
    for field in ("exported_at", "company", "station", "start_date"):
        if not first.get(field) or first[field] != second.get(field):
            raise ValueError(f"Missing or conflicting {field}")
    datetime.fromisoformat(first["exported_at"])
    if first["station"] != "DEMO":
        raise ValueError("Unexpected example station")
    sunday = date.fromisoformat(first["start_date"])
    if sunday.weekday() != 6:
        raise ValueError("Schedule must start on Sunday")
    if requested_sunday and date.fromisoformat(requested_sunday) != sunday:
        raise ValueError("Selected Sunday differs from source week")
    return [str(sunday + timedelta(days=i)) for i in range(7)]


def save_revision(db, revision):
    canonical = json.dumps(revision, sort_keys=True)
    old = db.execute(
        "SELECT payload_json FROM roster_revisions WHERE id=?",
        (revision["id"],),
    ).fetchone()
    if old:
        if json.loads(old[0]) != revision:
            raise ValueError("Existing revision ID has different content")
        return "duplicate"
    db.execute(
        "INSERT INTO roster_revisions VALUES (?, ?, ?, ?)",
        (revision["id"], hashlib.sha256(canonical.encode()).hexdigest(),
         revision["savedUTC"], canonical),
    )
    return "saved"


def run():
    checks = []
    metadata = {"exported_at": "2030-01-05T08:00:00", "company": "Fictional Demo",
                "station": "DEMO", "start_date": "2030-01-06"}
    second = dict(metadata)
    days = validate_metadata(metadata, second)
    assert days[0] == "2030-01-06" and days[-1] == "2030-01-12"
    checks.append({"check": "valid metadata produces seven dates", "result": "pass"})
    assert validate_metadata(metadata, second, days[0]) == days
    checks.append({"check": "matching explicit Sunday retains same source week", "result": "pass"})
    cases = [
        ("station mismatch without selected date", metadata, {**second, "station": "OTHER"}, None),
        ("station mismatch with selected date", metadata, {**second, "station": "OTHER"}, days[0]),
        ("missing timestamp with selected date", {**metadata, "exported_at": ""}, {**second, "exported_at": ""}, days[0]),
        ("wrong selected Sunday", metadata, second, "2030-01-13"),
    ]
    for label, first, other, sunday in cases:
        try:
            validate_metadata(first, other, sunday)
        except ValueError:
            checks.append({"check": label, "result": "pass: rejected"})
        else:
            raise AssertionError(label)

    with sqlite3.connect(":memory:") as db:
        db.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))
        raw = json.dumps({"metadata": metadata, "drivers": ["DEMO-001", "DEMO-002"]}, sort_keys=True).encode()
        source_hash = hashlib.sha256(raw).hexdigest()
        db.execute("INSERT INTO roster_schedule_sources VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (source_hash, "fictional-schedule.json", days[0], days[-1],
                    "2030-01-05T08:15:00Z", json.dumps(metadata), raw))
        for row, driver in enumerate(("DEMO-001", "DEMO-002"), 2):
            db.execute("INSERT INTO roster_schedule_records VALUES (?, ?, ?, ?, ?)",
                       (source_hash, "Demo schedule", row, driver, json.dumps({"driverId": driver})))
        revision = {"id": "demo-revision-a", "date": days[0], "scheduleHash": source_hash,
                    "savedUTC": "2030-01-06T09:00:00Z", "routeTarget": 1, "notes": "Fictional saved A"}
        assert save_revision(db, revision) == "saved"
        assert save_revision(db, revision) == "duplicate"
        checks.append({"check": "identical revision retry does not duplicate", "result": "pass"})
        try:
            save_revision(db, {**revision, "notes": "Conflicting content"})
        except ValueError:
            checks.append({"check": "same revision ID with changed content is held", "result": "pass"})
        else:
            raise AssertionError("Revision overwrite was accepted")
        save_revision(db, {**revision, "id": "demo-revision-b", "savedUTC": "2030-01-06T10:00:00Z", "routeTarget": 2})
        db.row_factory = sqlite3.Row
        latest = [dict(row) for row in db.execute(
            (HERE / "latest_revision.sql").read_text(encoding="utf-8"),
            {"start_date": days[0], "end_date": days[-1]},
        )]
        assert len(latest) == 1 and latest[0]["id"] == "demo-revision-b"
        assert latest[0]["route_target"] == 2 and latest[0]["source_file"] == "fictional-schedule.json"
        checks.append({"check": "latest daily revision joins correct schedule provenance", "result": "pass"})
        stored = db.execute("SELECT source_bytes FROM roster_schedule_sources WHERE source_hash=?", (source_hash,)).fetchone()[0]
        assert stored == raw and hashlib.sha256(stored).hexdigest() == source_hash
        checks.append({"check": "fictional source bytes and fingerprint retained", "result": "pass"})
        assert db.execute("SELECT COUNT(*) FROM roster_revisions").fetchone()[0] == 2
        checks.append({"check": "both distinct revision versions retained", "result": "pass"})

    return {"artifact": "independent synthetic engineering sample", "status": "passed",
            "executed_at_utc": datetime.now(timezone.utc).isoformat(),
            "check_count": len(checks), "checks": checks, "latest_revision": latest,
            "limits": ["Not a dashboard regression suite or human acceptance test.",
                       "Fixtures are JSON, not XLSX workbooks; full workbook parsing is outside this sample.",
                       "PowerShell excerpt is not executed by this runner."]}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
