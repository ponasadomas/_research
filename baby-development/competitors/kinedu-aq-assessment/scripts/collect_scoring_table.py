#!/usr/bin/env python3
"""Collect Phase 5, sequentially: only POST result to /api/assessment.

Run without arguments to collect every missing (age, K). Existing response or
header paths are never overwritten. --plan is offline. The manifest is fsynced
after every attempt; three consecutive blocking failures prevent further calls,
including after a restart. No automatic retries are made.
"""
import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "raw/api/scoring-all"
MANIFEST = OUT / "requests.jsonl"
URL = "https://webpromo.kinedu.com/api/assessment"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
PACE_SECONDS = 2.0


def utcnow():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def served_lists():
    """Index initial responses by RETURNED age, never the nominal filename."""
    bank = {}
    for path in sorted((ROOT / "raw/api").glob("start_age*_gw-null.json")):
        data = json.loads(path.read_text())
        if "sections" not in data:
            continue
        age = data["ageMonths"]
        if type(age) is not int or age in bank:
            raise ValueError(f"Invalid or duplicate returned age: {path}")
        items = []
        for section in data["sections"]:
            if section.get("anchor") is not None:
                items.append(section["anchor"])
            items.extend(section["items"])
        items.extend(data.get("calibration", []))
        if not 22 <= len(items) <= 39 or len({q["id"] for q in items}) != len(items):
            raise ValueError(f"Invalid served list: {path}")
        if any(type(q["id"]) is not int or not isinstance(q["rate"], (int, float))
               or not 0 <= q["rate"] <= 1 for q in items):
            raise ValueError(f"Invalid ID/rate: {path}")
        bank[age] = dict(file=str(path.relative_to(ROOT)), items=items,
                         ranked=sorted(items, key=lambda q: (q["rate"], q["id"])))
    if set(bank) != set(range(49)):
        raise ValueError("Expected exactly returned ages 0..48")
    return bank


def payload(age, entry, k):
    # The ranked vector is cumulative; every served ID occurs exactly once.
    return dict(action="result", ageMonths=age, extended=True,
                answers=[dict(id=q["id"], y=int(i < k))
                         for i, q in enumerate(entry["ranked"])])


def records():
    if not MANIFEST.exists():
        return []
    return [json.loads(line) for line in MANIFEST.read_text().splitlines() if line.strip()]


def blocking(rec):
    status = rec["http_status"]
    return rec["curl_exit_code"] != 0 or status in (403, 429) or 500 <= status < 600


def blocking_tail(recs):
    tail = []
    for rec in reversed(recs):
        if not blocking(rec):
            break
        tail.append(rec)
    return list(reversed(tail))


def paths(age, k):
    path = OUT / f"result_age{age:02d}_k{k:02d}.json"
    return path, path.with_name(path.name + ".headers.txt")


def validate_existing(recs, bank):
    seen = set()
    for rec in recs:
        age, k = rec["age"], rec["K"]
        if age not in bank or not 0 <= k <= len(bank[age]["items"]):
            raise ValueError("Manifest age/K outside served lists")
        path, headers = paths(age, k)
        if rec["file"] in seen or rec["file"] != str(path.relative_to(ROOT)):
            raise ValueError("Duplicate/unexpected manifest path")
        seen.add(rec["file"])
        if rec["body"] != payload(age, bank[age], k):
            raise ValueError(f"Saved payload differs: {path}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != rec["sha256"]:
            raise ValueError(f"Saved response hash differs: {path}")
        if rec["headers"] != str(headers.relative_to(ROOT)) or not headers.exists():
            raise ValueError(f"Missing/unexpected headers: {path}")
        if hashlib.sha256(headers.read_bytes()).hexdigest() != rec["headers_sha256"]:
            raise ValueError(f"Saved header hash differs: {path}")
    return seen


def collect():
    bank = served_lists()
    expected = sum(len(entry["items"]) + 1 for entry in bank.values())
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / ".collector.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("Another Phase 5 collector holds the lock")
        recs = records()
        seen = validate_existing(recs, bank)
        tail = blocking_tail(recs)
        if len(tail) >= 3:
            print(json.dumps(dict(status="BLOCKED", requests=len(recs), expected=expected,
                                  failures=[{key: r[key] for key in
                                             ("timestamp", "http_status", "curl_exit_code", "file")}
                                            for r in tail])), flush=True)
            return 2
        # Verify all existing files before sending anything. An interrupted,
        # unmanifested response is preserved and needs offline reconciliation.
        known = {r["file"] for r in recs} | {r["headers"] for r in recs}
        orphans = [str(p.relative_to(ROOT)) for p in OUT.glob("result_age*")
                   if str(p.relative_to(ROOT)) not in known]
        if orphans:
            raise RuntimeError(f"Preserved unmanifested files; no calls made: {orphans}")
        for age in range(49):
            entry = bank[age]
            for k in range(len(entry["items"]) + 1):
                path, headers = paths(age, k)
                rel = str(path.relative_to(ROOT))
                if rel in seen:
                    continue
                # O_EXCL protects even empty responses against accidental reuse.
                with path.open("xb"), headers.open("xb"):
                    pass
                body = payload(age, entry, k)
                time.sleep(PACE_SECONDS)  # before EVERY request, also on resume
                timestamp = utcnow()
                cmd = ["curl", "--request", "POST", URL, "--user-agent", UA,
                       "--header", "Content-Type: application/json",
                       "--header", "Origin: https://webpromo.kinedu.com",
                       "--header", "Referer: https://webpromo.kinedu.com/aq-assessment",
                       "--data-raw", json.dumps(body, separators=(",", ":")),
                       "--connect-timeout", "20", "--max-time", "60",
                       "--silent", "--show-error", "--dump-header", str(headers),
                       "--output", str(path), "--write-out", "%{http_code}"]
                try:
                    run = subprocess.run(cmd, capture_output=True, text=True)
                    status = int(run.stdout.strip() or "0")
                    curl_exit, stderr = run.returncode, run.stderr
                except OSError as exc:
                    status, curl_exit, stderr = 0, -1, str(exc)
                completed = utcnow()
                rec = dict(timestamp=timestamp, completed_at=completed, age=age,
                           N=len(entry["items"]), K=k, http_status=status, file=rel,
                           sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                           headers=str(headers.relative_to(ROOT)),
                           headers_sha256=hashlib.sha256(headers.read_bytes()).hexdigest(),
                           curl_exit_code=curl_exit, stderr=stderr, body=body,
                           endpoint=URL, source=entry["file"],
                           source_sha256=hashlib.sha256((ROOT / entry["file"]).read_bytes()).hexdigest(),
                           sleep_before_request_seconds=PACE_SECONDS)
                with MANIFEST.open("a") as out:
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    out.flush()
                    os.fsync(out.fileno())
                recs.append(rec)
                seen.add(rel)
                tail = tail + [rec] if blocking(rec) else []
                print(json.dumps(dict(requests=len(recs), expected=expected, age=age,
                                      K=k, http=status, curl_exit_code=curl_exit,
                                      consecutive_blocking=len(tail), timestamp=timestamp)), flush=True)
                if len(tail) >= 3:
                    print(json.dumps(dict(status="BLOCKED", failures=[
                        {key: r[key] for key in ("timestamp", "http_status", "curl_exit_code", "file")}
                        for r in tail])), flush=True)
                    return 2
        print(json.dumps(dict(status="FINISHED", requests=len(recs), expected=expected)), flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true", help="List coverage without any network calls")
    args = parser.parse_args()
    if args.plan:
        bank = served_lists()
        recs = records()
        validate_existing(recs, bank)
        print(json.dumps(dict(expected=sum(len(e["items"]) + 1 for e in bank.values()),
                              recorded=len(recs), pace_seconds=PACE_SECONDS,
                              ages={age: len(e["items"]) for age, e in bank.items()})))
        return 0
    return collect()


if __name__ == "__main__":
    sys.exit(main())
