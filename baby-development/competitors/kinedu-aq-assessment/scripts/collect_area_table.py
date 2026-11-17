#!/usr/bin/env python3
"""Phase 6: sequential, proxy-only per-area count sweeps for returned ages 0..48.

Reuse Phase 5's served lists, request headers, immutable evidence and resume
structure. --plan is offline. Normal collection first checks the proxy country;
--preflight-file accepts a successful check made in the preceding 30 minutes.
Three consecutive blocking failures stop this and all subsequent invocations.
"""
import argparse
import datetime as dt
from decimal import Decimal, ROUND_HALF_EVEN
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from collect_scoring_table import ROOT, URL, UA, PACE_SECONDS, served_lists

OUT = ROOT / "raw/api/area-sweep"
MANIFEST = OUT / "requests.jsonl"
PROXY = ROOT / "scripts/proxy_curl.sh"
AREAS = ("Physical", "Cognitive", "Language", "Social-Emotional")
ORDER_CHECKS = {3: "Physical", 12: "Cognitive", 30: "Language"}


def utcnow():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def area_lists():
    bank = served_lists()
    for entry in bank.values():
        if {q["area"] for q in entry["items"]} != set(AREAS):
            raise ValueError("Unexpected item area")
        entry["areas"] = {}
        for area in AREAS:
            ranked = sorted((q for q in entry["items"] if q["area"] == area),
                            key=lambda q: (q["rate"], q["id"]))
            total = sum((Decimal(str(q["rate"])) for q in ranked), Decimal(0))
            baseline = int(total.to_integral_value(rounding=ROUND_HALF_EVEN))
            entry["areas"][area] = dict(ranked=ranked, rate_sum=str(total), baseline=baseline)
    return bank


def plan(bank):
    for age in range(49):
        for area in AREAS:
            for k in range(len(bank[age]["areas"][area]["ranked"]) + 1):
                yield age, area, k, "ascending"
        if age in ORDER_CHECKS:
            area = ORDER_CHECKS[age]
            for k in range(len(bank[age]["areas"][area]["ranked"]) + 1):
                yield age, area, k, "descending"


def payload(age, entry, area, k, order="ascending"):
    yes = set()
    for name, group in entry["areas"].items():
        ranked = group["ranked"]
        count = k if name == area else group["baseline"]
        if name == area and order == "descending":
            ranked = list(reversed(ranked))
        yes.update(q["id"] for q in ranked[:count])
    # Keep the submitted array order fixed, changing which target IDs are Yes.
    return dict(action="result", ageMonths=age, extended=True,
                answers=[dict(id=q["id"], y=int(q["id"] in yes)) for q in entry["ranked"]])


def paths(age, area, k, order="ascending"):
    directory = OUT if order == "ascending" else OUT / "order-check"
    suffix = "" if order == "ascending" else "_descending"
    path = directory / f"result_age{age:02d}_{area}{suffix}_k{k:02d}.json"
    return path, path.with_name(path.name + ".headers.txt")


def records():
    if not MANIFEST.exists():
        return []
    return [json.loads(line) for line in MANIFEST.read_text().splitlines() if line.strip()]


def blocking(rec):
    code = rec["http_status"]
    return rec["curl_exit_code"] != 0 or code in (403, 429) or 500 <= code < 600


def blocking_tail(recs):
    tail = []
    for rec in reversed(recs):
        if not blocking(rec):
            break
        tail.append(rec)
    return list(reversed(tail))


def validate_existing(recs, bank):
    allowed = set(plan(bank))
    seen = set()
    for rec in recs:
        key = rec["age"], rec["area"], rec["K"], rec["order"]
        if key not in allowed:
            raise ValueError("Manifest key outside collection plan")
        path, headers = paths(*key)
        rel = str(path.relative_to(ROOT))
        if rec["file"] != rel or rel in seen:
            raise ValueError("Duplicate/unexpected manifest path")
        seen.add(rel)
        age, area, k, order = key
        entry = bank[age]
        if rec["body"] != payload(age, entry, area, k, order):
            raise ValueError(f"Saved payload differs: {rel}")
        if rec["sha256"] != digest(path):
            raise ValueError(f"Saved response hash differs: {rel}")
        if rec["headers"] != str(headers.relative_to(ROOT)) or rec["headers_sha256"] != digest(headers):
            raise ValueError(f"Saved headers differ: {rel}")
        if rec["source"] != entry["file"] or rec["source_sha256"] != digest(ROOT / entry["file"]):
            raise ValueError(f"Served-list source differs: {rel}")
        if rec["endpoint"] != URL or rec["http"] != rec["http_status"]:
            raise ValueError(f"Endpoint/status differs: {rel}")
    return seen


def orphans(recs):
    known = {r["file"] for r in recs} | {r["headers"] for r in recs}
    return sorted(str(p.relative_to(ROOT)) for p in OUT.rglob("result_age*")
                  if str(p.relative_to(ROOT)) not in known)


def preflight(existing=None):
    if existing:
        path = Path(existing).resolve()
        data = json.loads(path.read_text())
        elapsed = (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(data["completed_at"])).total_seconds()
        if not 0 <= elapsed <= 1800:
            raise ValueError("Supplied proxy preflight is older than 30 minutes")
    else:
        path = OUT / f"proxy-check_{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')}.json"
        time.sleep(PACE_SECONDS)
        timestamp = utcnow()
        try:
            run = subprocess.run([str(PROXY), "-s", "https://ipinfo.io/json"],
                                 capture_output=True, text=True, timeout=90)
            response = json.loads(run.stdout)
            code = run.returncode
        except (OSError, ValueError, subprocess.TimeoutExpired):
            response, code = {}, -1
        country = response.get("country") if isinstance(response, dict) else None
        data = dict(timestamp=timestamp, completed_at=utcnow(), country=country,
                    curl_exit_code=code, response=response,
                    passed=code == 0 and isinstance(country, str) and len(country) == 2 and country != "LT",
                    sleep_before_request_seconds=PACE_SECONDS)
        with path.open("x") as out:
            json.dump(data, out, indent=2)
            out.write("\n")
    if not (data.get("passed") is True and data.get("curl_exit_code") == 0
            and isinstance(data.get("country"), str) and len(data["country"]) == 2
            and data["country"] != "LT" and data.get("sleep_before_request_seconds", 0) >= PACE_SECONDS):
        print(json.dumps(dict(status="BLOCKED", reason="Proxy country check failed", country=data.get("country"))), flush=True)
        return None
    print(json.dumps(dict(proxy_country=data["country"], preflight=str(path.relative_to(ROOT)))), flush=True)
    return dict(file=str(path.relative_to(ROOT)), sha256=digest(path), country=data["country"])


def blocked_summary(recs, expected):
    return dict(status="BLOCKED", requests=len(recs), expected=expected,
                failures=[{key: r[key] for key in ("timestamp", "http_status", "curl_exit_code", "file")}
                          for r in blocking_tail(recs)])


def collect(args):
    bank = area_lists()
    jobs = list(plan(bank))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "order-check").mkdir(exist_ok=True)
    with (OUT / ".collector.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("Another Phase 6 collector holds the lock")
        recs = records()
        seen = validate_existing(recs, bank)
        tail = blocking_tail(recs)
        if len(tail) >= 3:
            print(json.dumps(blocked_summary(recs, len(jobs))), flush=True)
            return 2
        unknown = orphans(recs)
        if unknown:
            raise RuntimeError(f"Preserved unmanifested files; no calls made: {unknown}")
        if len(recs) == len(jobs):
            print(json.dumps(dict(status="FINISHED", requests=len(recs), expected=len(jobs))), flush=True)
            return 0
        proxy_check = preflight(args.preflight_file)
        if proxy_check is None:
            return 2
        for age, area, k, order in jobs:
            path, headers = paths(age, area, k, order)
            rel = str(path.relative_to(ROOT))
            if rel in seen:
                continue
            with path.open("xb"), headers.open("xb"):
                pass
            entry = bank[age]
            body = payload(age, entry, area, k, order)
            time.sleep(PACE_SECONDS)
            timestamp = utcnow()
            cmd = [str(PROXY), "--request", "POST", URL, "--user-agent", UA,
                   "--header", "Content-Type: application/json",
                   "--header", "Origin: https://webpromo.kinedu.com",
                   "--header", "Referer: https://webpromo.kinedu.com/aq-assessment",
                   "--data-raw", json.dumps(body, separators=(",", ":")),
                   "--connect-timeout", "20", "--max-time", "60",
                   "--silent", "--show-error", "--dump-header", str(headers),
                   "--output", str(path), "--write-out", "%{http_code}"]
            try:
                run = subprocess.run(cmd, capture_output=True, text=True, timeout=75)
                value = run.stdout.strip()
                status = int(value) if value.isdigit() and len(value) == 3 else 0
                curl_exit = run.returncode
                if not status and not curl_exit:
                    curl_exit = -2
                stderr_present = bool(run.stderr)
            except (OSError, subprocess.TimeoutExpired):
                status, curl_exit, stderr_present = 0, -1, True
            completed = utcnow()
            rec = dict(timestamp=timestamp, completed_at=completed, age=age, area=area,
                       N=len(entry["items"]), n_area=len(entry["areas"][area]["ranked"]),
                       K=k, order=order, http=status, http_status=status, file=rel,
                       sha256=digest(path), headers=str(headers.relative_to(ROOT)),
                       headers_sha256=digest(headers), curl_exit_code=curl_exit,
                       stderr_present=stderr_present, body=body, endpoint=URL,
                       source=entry["file"], source_sha256=digest(ROOT / entry["file"]),
                       baseline={name: group["baseline"] for name, group in entry["areas"].items()},
                       rate_sums={name: group["rate_sum"] for name, group in entry["areas"].items()},
                       proxy_wrapper="scripts/proxy_curl.sh", proxy_check=proxy_check,
                       sleep_before_request_seconds=PACE_SECONDS)
            with MANIFEST.open("a") as out:
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                out.flush()
                os.fsync(out.fileno())
            recs.append(rec)
            seen.add(rel)
            tail = tail + [rec] if blocking(rec) else []
            print(json.dumps(dict(requests=len(recs), expected=len(jobs), age=age,
                                  area=area, K=k, order=order, http=status,
                                  curl_exit_code=curl_exit, consecutive_blocking=len(tail),
                                  timestamp=timestamp)), flush=True)
            if len(tail) >= 3:
                print(json.dumps(blocked_summary(recs, len(jobs))), flush=True)
                return 2
        print(json.dumps(dict(status="FINISHED", requests=len(recs), expected=len(jobs))), flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true", help="Offline coverage and integrity check")
    parser.add_argument("--preflight-file", help="Reuse a recent archived proxy country check")
    args = parser.parse_args()
    if args.plan:
        bank = area_lists()
        recs = records()
        validate_existing(recs, bank)
        jobs = list(plan(bank))
        print(json.dumps(dict(expected=len(jobs), ascending=sum(j[3] == "ascending" for j in jobs),
                              descending=sum(j[3] == "descending" for j in jobs), recorded=len(recs),
                              pace_seconds=PACE_SECONDS, order_checks=ORDER_CHECKS,
                              unmanifested_files=orphans(recs))))
        return 0
    return collect(args)


if __name__ == "__main__":
    sys.exit(main())
