#!/usr/bin/env python3
"""Paced, auditable curl collection. Run from the assessment folder."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "raw/api"
TODAY = dt.date(2026, 11, 2)
URL = "https://webpromo.kinedu.com/api/assessment"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
MANIFEST = OUT / "requests.jsonl"


def birthdate(age, day=15):
    year, month0 = divmod(TODAY.year * 12 + TODAY.month - 1 - age, 12)
    return dt.date(year, month0 + 1, day).isoformat()


def request(stem, payload, **metadata):
    OUT.mkdir(parents=True, exist_ok=True)
    # Preserve every attempt, including failed HTTP and transport responses.
    target = OUT / (stem + ".json")
    if target.exists():
        raise FileExistsError(target)
    time.sleep(0.5)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    command = [
        "curl", "--request", "POST", URL,
        "--user-agent", UA,
        "--header", "Content-Type: application/json",
        "--header", "Origin: https://webpromo.kinedu.com",
        "--header", "Referer: https://webpromo.kinedu.com/aq-assessment",
        "--data-raw", json.dumps(payload, separators=(",", ":")),
        "--connect-timeout", "20", "--max-time", "60",
        "--silent", "--show-error",
        "--dump-header", str(OUT / (stem + ".headers.txt")),
        "--output", str(target), "--write-out", "%{http_code}",
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if not target.exists():
        target.write_bytes(b"")
    raw = target.read_bytes()
    try:
        data = json.loads(raw)
    except (ValueError, UnicodeDecodeError):
        data = None
    record = dict(
        file=str(target.relative_to(ROOT)), requested_at_utc=started,
        request=payload, http_status=int(result.stdout or 0),
        curl_exit_code=result.returncode, stderr=result.stderr,
        sha256=hashlib.sha256(raw).hexdigest(), **metadata,
    )
    if isinstance(data, dict):
        record.update(response_age_months=data.get("ageMonths"),
                      corrected=data.get("corrected"), error=data.get("error"))
    with MANIFEST.open("a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(json.dumps(record, ensure_ascii=False), flush=True)
    return record, data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["sweep", "preterm"])
    args = parser.parse_args()
    if args.mode == "sweep":
        consecutive = 0
        for age in range(100):
            rec, data = request(
                f"start_age{age:02d}_gw-null",
                dict(action="start", birthdate=birthdate(age), gestationalWeeks=None),
                series="monthly_sweep", nominal_age_months=age,
            )
            if rec["http_status"] == 422 and isinstance(data, dict) and data.get("error") == "age_range":
                consecutive += 1
            elif rec["http_status"] == 200:
                consecutive = 0
            else:
                consecutive = 0
            if consecutive == 3:
                print(f"STOP: three consecutive age_range responses through nominal age {age}", flush=True)
                break
        else:
            raise RuntimeError("No age_range boundary before 100 months")
    else:
        for age in [0, 1, 2, 3, 4, 6, 9, 12, 18, 24]:
            # Day 2 matches today's day of month. The day-15 sweep's
            # filename labels are not the server's completed-month ages.
            request(
                f"sample_age{age:02d}_gw-null",
                dict(action="start", birthdate=birthdate(age, day=2), gestationalWeeks=None),
                series="preterm_baseline", nominal_age_months=age,
            )
            for weeks in [28, 32, 36, 37]:
                request(
                    f"start_age{age:02d}_gw{weeks:02d}",
                    dict(action="start", birthdate=birthdate(age, day=2), gestationalWeeks=weeks),
                    series="preterm_sample", nominal_age_months=age,
                )


if __name__ == "__main__":
    main()
