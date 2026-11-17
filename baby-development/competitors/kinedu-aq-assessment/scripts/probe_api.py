#!/usr/bin/env python3
"""Focused correction probes and result extension discovery; no leads/tracking."""
import argparse
import json
from enumerate_api import ROOT, request


def ordered(data):
    result = []
    for i, section in enumerate(data["sections"]):
        if section.get("anchor"):
            result.append(section["anchor"])
        result.extend(section["items"])
        if i < len(data.get("calibration", [])):
            result.append(data["calibration"][i])
    return result


def correction():
    # Distinguish rounding correction in whole months from day-level subtraction.
    for dob in ["2026-05-02", "2026-05-15"]:
        for gw in [30, 34, 35]:
            request(f"probe_dob{dob}_gw{gw}",
                    dict(action="start", birthdate=dob, gestationalWeeks=gw),
                    series="correction_formula_probe")
    for dob in ["2024-11-01", "2024-11-02", "2024-11-03", "2024-12-02"]:
        for gw in [None, 28]:
            request(f"probe_cutoff_dob{dob}_gw{gw if gw else 'null'}",
                    dict(action="start", birthdate=dob, gestationalWeeks=gw),
                    series="correction_cutoff_probe")


def supplemental():
    for gw in [24, 25, 26, 27, 29, 31, 33]:
        request(f"probe_integer_gw{gw}",
                dict(action="start", birthdate="2026-05-02", gestationalWeeks=gw),
                series="correction_integer_probe")
    for gw in [None, 30]:
        request(f"probe_rounding_dob2026-05-30_gw{gw if gw else 'null'}",
                dict(action="start", birthdate="2026-05-30", gestationalWeeks=gw),
                series="correction_rounding_probe")
    data = json.loads((ROOT / "raw/api/sample_age06_gw-null.json").read_text())
    request("result_age06_all_yes_extended",
            dict(action="result", ageMonths=6, extended=True,
                 answers=[dict(id=q["id"], y=1) for q in ordered(data)]),
            series="report_inventory_probe", profile="all_yes",
            nominal_age_months=6)


def extensions(ages, profiles):
    records = [json.loads(line) for line in (ROOT / "raw/api/requests.jsonl").read_text().splitlines()]
    by_age = {}
    for rec in records:
        if rec["series"] == "monthly_sweep" and rec["http_status"] == 200:
            by_age[rec["response_age_months"]] = json.loads((ROOT / rec["file"]).read_text())
    for age in ages:
        for name, value in profiles:
            request(f"result_age{age:02d}_{name}_numeric",
                    dict(action="result", ageMonths=age, extended=False,
                         answers=[dict(id=q["id"], y=value) for q in ordered(by_age[age])]),
                    series="extension_discovery", profile=name,
                    nominal_age_months=age)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["correction", "supplemental", "extension_smoke", "extensions", "anomaly_repeat"])
    mode = p.parse_args().mode
    if mode == "correction":
        correction()
    elif mode == "supplemental":
        supplemental()
    elif mode == "anomaly_repeat":
        records = [json.loads(line) for line in (ROOT / "raw/api/requests.jsonl").read_text().splitlines()]
        original = next(r for r in records if r["file"] == "raw/api/result_age01_all_no_numeric.json")
        request("result_age01_all_no_repeat", original["request"],
                series="result_anomaly_repeat", profile="all_no", nominal_age_months=1)
    elif mode == "extension_smoke":
        extensions([6], [("all_yes", 1), ("all_no", 0)])
    else:
        extensions([a for a in range(49) if a != 6], [("all_yes", 1), ("all_no", 0)])
