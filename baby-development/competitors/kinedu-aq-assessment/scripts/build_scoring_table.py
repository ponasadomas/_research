#!/usr/bin/env python3
"""Build Phase 5 CSV, Markdown and audit entirely from saved evidence.

No network access. Every planned (age, K) gets a CSV row; uncollected values
stay empty. Reported area values describe the ascending-rate vector only.
"""
import collections
import csv
import datetime as dt
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import re

from collect_scoring_table import (
    ROOT, OUT, URL, MANIFEST, PACE_SECONDS, blocking_tail, paths, payload,
    records, served_lists, validate_existing,
)

AREAS = {"Physical": "Physical", "Cognitive": "Cognitive", "Language": "Language",
         "Social-Emotional": "SocialEmotional"}
FIELDS = ["age", "N", "K", "http", "stage", "state", "devAge", "band", "capped"]
FIELDS += ["months_" + value for value in AREAS.values()]
FIELDS += ["atLeast_" + value for value in AREAS.values()]
FIELDS += ["file", "observation"]


def number(value):
    return type(value) in (int, float)


def table(headers, rows):
    def cell(value):
        if value is None or value == "":
            return "—"
        if isinstance(value, bool):
            return str(value).lower()
        return str(value).replace("|", "\\|").replace("\n", " ")
    return "\n".join(["| " + " | ".join(map(cell, headers)) + " |",
                      "| " + " | ".join("---" for _ in headers) + " |"] +
                     ["| " + " | ".join(map(cell, row)) + " |" for row in rows])


def expected_band(age, dev_age):
    r = dev_age / max(age, 1)
    if r > 1.15:
        return "well_ahead"
    if r > 1.05:
        return "little_ahead"
    return "on_pace" if r >= 0.95 else "building"


def rate_sum(entry):
    # Avoid binary floating-point deciding the rounding of an exact .50 tie.
    return sum((Decimal(str(q["rate"])) for q in entry["items"]), Decimal(0))


def is_report(row):
    return row["observation"] == "observed_report"


def is_numeric(row):
    return is_report(row) and number(row["devAge"])


def headline(row):
    return tuple(row[key] for key in ("observation", "stage", "state", "devAge", "band", "capped"))


def ranges(rows):
    result = []
    for row in rows:
        if result and row["K"] == result[-1][-1]["K"] + 1 and headline(row) == headline(result[-1][-1]):
            result[-1].append(row)
        else:
            result.append([row])
    return result


def k_range(group):
    lo, hi = group[0]["K"], group[-1]["K"]
    return str(lo) if lo == hi else f"{lo}–{hi}"


def main():
    bank = served_lists()
    recs = records()
    validate_existing(recs, bank)
    by_key = {(r["age"], r["K"]): r for r in recs}
    if len(by_key) != len(recs):
        raise ValueError("Duplicate age/K in manifest")
    gaps = []
    header_statuses_verified = 0
    for i, rec in enumerate(recs):
        if rec["endpoint"] != URL or rec["body"] != payload(rec["age"], bank[rec["age"]], rec["K"]):
            raise ValueError("Unexpected endpoint or request payload")
        source = ROOT / rec["source"]
        if (rec["source"] != bank[rec["age"]]["file"] or
                hashlib.sha256(source.read_bytes()).hexdigest() != rec["source_sha256"]):
            raise ValueError("Served-list source changed")
        if rec["N"] != len(bank[rec["age"]]["items"]):
            raise ValueError("Manifest N differs from served list")
        if rec["sleep_before_request_seconds"] < PACE_SECONDS:
            raise ValueError("Recorded sleep below two seconds")
        headers = (ROOT / rec["headers"]).read_text()
        statuses = [int(s) for s in re.findall(r"^HTTP/\S+\s+(\d{3})", headers, re.M)]
        if rec["curl_exit_code"] == 0:
            if not statuses or statuses[-1] != rec["http_status"]:
                raise ValueError(f"Header status differs: {rec['file']}")
            header_statuses_verified += 1
        started = dt.datetime.fromisoformat(rec["timestamp"])
        completed = dt.datetime.fromisoformat(rec["completed_at"])
        if completed < started:
            raise ValueError("Response completion precedes request start")
        if i:
            gap = (started - dt.datetime.fromisoformat(recs[i - 1]["completed_at"])).total_seconds()
            if gap < PACE_SECONDS:
                raise ValueError(f"Response-to-next-request gap below 2s: {gap}")
            gaps.append(gap)
        if len(blocking_tail(recs[:i])) >= 3:
            raise ValueError("Manifest contains a request after the abort threshold")

    rows = []
    schema_issues = []
    for age in range(49):
        n = len(bank[age]["items"])
        for k in range(n + 1):
            path, _ = paths(age, k)
            row = dict.fromkeys(FIELDS, "")
            row.update(age=age, N=n, K=k, file=str(path.relative_to(ROOT)), observation="not_collected")
            rec = by_key.get((age, k))
            if rec is not None:
                row["http"] = rec["http_status"]
                if rec["curl_exit_code"]:
                    row["observation"] = "transport_failure"
                elif rec["http_status"] != 200:
                    row["observation"] = "http_error"
                else:
                    try:
                        data = json.loads(path.read_bytes())
                    except (ValueError, UnicodeDecodeError):
                        data = None
                    if not isinstance(data, dict):
                        row["observation"] = "invalid_json"
                    else:
                        row["stage"] = data.get("stage", "")
                        basic = data.get("basic", {})
                        detail = data.get("detail", {})
                        if not isinstance(basic, dict) or not isinstance(detail, dict):
                            basic, detail = {}, {}
                        for key in ("state", "devAge", "band", "capped"):
                            row[key] = basic.get(key, "")
                        row["observation"] = "observed_report" if (
                            row["stage"] == "complete" and row["state"] in ("ok", "below_floor", "not_enough")
                        ) else "unexpected_schema"
                        if row["state"] == "ok" and (not number(row["devAge"]) or
                                type(row["capped"]) is not bool or not row["band"]):
                            row["observation"] = "unexpected_schema"
                        if basic.get("ageMonths", age) != age:
                            schema_issues.append(dict(age=age, K=k, issue="returned age differs", file=row["file"]))
                        for key in ("state", "devAge", "band", "capped"):
                            if key in detail and detail[key] != basic.get(key):
                                schema_issues.append(dict(age=age, K=k, issue=f"detail/basic {key} differs", file=row["file"]))
                        for area in detail.get("areas", []):
                            suffix = AREAS.get(area["area"])
                            if suffix:
                                row["months_" + suffix] = area.get("months", "")
                                row["atLeast_" + suffix] = area.get("atLeast", "")
            rows.append(row)

    with (ROOT / "scoring-table.csv").open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows({key: str(value).lower() if isinstance(value, bool) else value
                         for key, value in row.items()} for row in rows)

    grouped = {age: [r for r in rows if r["age"] == age] for age in range(49)}
    numeric = [r for r in rows if is_numeric(r)]
    mismatches = [dict(age=r["age"], K=r["K"], devAge=r["devAge"], band=r["band"],
                       expected=expected_band(r["age"], r["devAge"]), file=r["file"])
                  for r in numeric if r["band"] != expected_band(r["age"], r["devAge"])]
    decreases = []
    numeric_to_floor = []
    exceptions, unknown_controls, controls, ties = [], [], [], []
    age_summary = []
    complete_ages = []
    for age, age_rows in grouped.items():
        complete = all(is_report(r) for r in age_rows)
        if complete:
            complete_ages.append(age)
        nums = [r for r in age_rows if is_numeric(r)]
        for previous, current in zip(nums, nums[1:]):
            if current["devAge"] < previous["devAge"]:
                decreases.append(dict(age=age, from_K=previous["K"], to_K=current["K"],
                                      from_devAge=previous["devAge"], to_devAge=current["devAge"]))
        for previous, current in zip(age_rows, age_rows[1:]):
            if is_numeric(previous) and is_report(current) and current["state"] == "below_floor":
                numeric_to_floor.append(dict(age=age, from_K=previous["K"], to_K=current["K"]))
        total = rate_sum(bank[age])
        k = int(total.to_integral_value(rounding=ROUND_HALF_EVEN))
        control = age_rows[k]
        control_entry = dict(age=age, expected_yes=str(total), K=k,
                             devAge=control["devAge"], state=control["state"],
                             observation=control["observation"], file=control["file"])
        controls.append(control_entry)
        if not is_report(control):
            unknown_controls.append(control_entry)
        elif control["devAge"] != age:
            exceptions.append(control_entry)
        if total % 1 == Decimal("0.5"):
            up_k = int(total.to_integral_value(rounding=ROUND_HALF_UP))
            ties.append(dict(age=age, expected_yes=str(total), even_K=k,
                             even_devAge=control["devAge"], half_up_K=up_k,
                             half_up_devAge=age_rows[up_k]["devAge"],
                             half_up_observation=age_rows[up_k]["observation"]))

        equal = [r["K"] for r in nums if r["devAge"] == age]
        not_floor = [r["K"] for r in age_rows if is_report(r) and r["state"] != "below_floor"]
        caps = [r for r in nums if r["capped"] is True]
        # A partial run cannot establish a first K unless every smaller K was observed.
        def first_label(values):
            if not values:
                return "none" if complete else "unknown"
            first = min(values)
            return first if all(is_report(r) for r in age_rows[:first + 1]) else f"{first} (observed; earlier gaps)"
        cap_ages = sorted({r["devAge"] for r in caps})
        age_summary.append([age, age_rows[0]["N"], f"{total:.2f}",
                            first_label(equal), first_label(not_floor),
                            first_label([r["K"] for r in caps]),
                            ", ".join(map(str, cap_ages)) if cap_ages else ("none" if complete else "unknown"),
                            f"{sum(is_report(r) for r in age_rows)}/{len(age_rows)}"])

    failures = [r for r in rows if r["observation"] not in ("observed_report", "not_collected")]
    n_reports = sum(is_report(r) for r in rows)
    n_missing = sum(r["observation"] == "not_collected" for r in rows)
    tail = blocking_tail(recs)
    status = "COMPLETED" if n_reports == len(rows) and not schema_issues else "BLOCKED"
    counts = dict(sorted(collections.Counter(r["http_status"] for r in recs).items()))
    transports = sum(r["curl_exit_code"] != 0 for r in recs)
    known_control_count = 49 - len(unknown_controls)
    control_matches = known_control_count - len(exceptions)
    band_matches = len(numeric) - len(mismatches)
    nonmonotonic_ages = sorted({r["age"] for r in decreases})
    orphan_paths = sorted(str(p.relative_to(ROOT)) for p in OUT.glob("result_age*")
                          if str(p.relative_to(ROOT)) not in
                          ({r["file"] for r in recs} | {r["headers"] for r in recs}))
    if orphan_paths:
        status = "BLOCKED"
    abort_failures = [{key: r[key] for key in ("timestamp", "http_status", "curl_exit_code", "file")}
                      for r in tail] if len(tail) >= 3 else []
    stop_reason = ("Appear blocked: " + "; ".join(
        f"HTTP {r['http_status']} / curl {r['curl_exit_code']} at {r['timestamp']}" for r in abort_failures
    )) if abort_failures else ("All requested reports collected." if status == "COMPLETED" else
                              "Incomplete evidence; see coverage and failures. No values filled by inference.")
    audit = dict(status=status, expected_requests=len(rows), requests=len(recs),
                 complete_reports=n_reports, missing_requests=n_missing,
                 failed_or_unusable=len(failures), complete_ages=complete_ages,
                 http_status_counts=counts, transport_failures=transports,
                 first_request=recs[0]["timestamp"] if recs else None,
                 last_response=recs[-1]["completed_at"] if recs else None,
                 minimum_response_to_next_request_gap_seconds=min(gaps) if gaps else None,
                 body_hashes_verified=len(recs), header_hashes_verified=len(recs),
                 header_statuses_verified=header_statuses_verified,
                 source_hashes_verified=len(recs), all_payloads_verified=True,
                 endpoint=URL, sleep_before_each_request_seconds=PACE_SECONDS,
                 numeric_reports=len(numeric), band_matches=band_matches,
                 band_mismatches=mismatches, expected_count_matches=control_matches,
                 expected_count_observed=known_control_count,
                 expected_count_exceptions=exceptions, expected_count_unknown=unknown_controls,
                 expected_count_controls=controls, rounding_ties=ties,
                 nonmonotonic_ages=nonmonotonic_ages, numeric_decreases=decreases,
                 numeric_to_floor=numeric_to_floor, schema_issues=schema_issues,
                 unmanifested_files=orphan_paths, abort_failures=abort_failures,
                 stop_reason=stop_reason)
    (ROOT / "logs/phase5-validation.json").write_text(json.dumps(audit, indent=2) + "\n")

    http_text = ", ".join(f"{key}={value}" for key, value in counts.items()) or "none"
    min_gap = f"{min(gaps):.6f}s" if gaps else "not measurable"
    summary = [
        f"{status} — {len(recs)}/{len(rows)} requests; {n_reports}/{len(rows)} complete reports.",
        f"Coverage: {len(complete_ages)}/49 full ages; {n_missing} missing requests; {len(failures)} unusable responses.",
        f"HTTP: {http_text}; transport failures: {transports}.",
        f"Rounded expected-count control: {control_matches}/{known_control_count} observed matches; {len(exceptions)} exceptions; {len(unknown_controls)} unknown ages.",
        f"Band formula: {band_matches}/{len(numeric)} numeric reports match; {len(mismatches)} mismatches.",
        f"Nonmonotonic devAge ages: {', '.join(map(str, nonmonotonic_ages)) or 'none observed'}.",
        f"Integrity: {len(recs)} bodies, headers and source hashes verified; {len(schema_issues)} schema issues.",
        f"Pacing: 2.0s sleep before every request; minimum completion-to-next-start gap {min_gap}.",
        "Artifacts: scoring-table.csv; SCORING-TABLE.md; logs/phase5-validation.json.",
        "Collector: python3 scripts/collect_scoring_table.py (resumable; saved files immutable).",
        "Offline rebuild: python3 scripts/build_scoring_table.py.",
        stop_reason,
    ]
    assert len(summary) == 12
    (ROOT / "logs/phase5-summary.txt").write_text("\n".join(summary) + "\n")

    doc = ["# Kinedu AQ: full Yes-count → headline table (Phase 5)",
           f"**{status}: {len(recs)}/{len(rows)} requests; {n_reports}/{len(rows)} complete reports.** "
           f"Coverage is {len(complete_ages)}/49 full ages. " + stop_reason,
           "Observed means a saved response, with the exact served ID set and cumulative ascending "
           "`(rate, id)` Yes vector. Every numeric cell comes from that response; missing ages and flags "
           "remain empty in the CSV and appear as — here. `below_floor` is a returned state, not age zero. "
           "The 1,886-row CSV also keeps uncollected combinations as `not_collected`, without invented scores.",
           "## Collection and evidence",
           f"Only POST `{URL}` with `action:result`, `extended:true`, numeric 0/1 answers, and the exact "
           "User-Agent, Content-Type, Origin and Referer in [ENUMERATION.md](ENUMERATION.md) was used. "
           "Initial lists were indexed by returned `ageMonths` from `start_age*_gw-null.json`. Each section's "
           "anchor and items, followed by calibration items, supplies the complete unique ID set; sorting "
           "by ascending `(rate,id)` determines the cumulative vector. No other endpoint was called.",
           f"Sequential calls slept 2.0 seconds before every request. Observed minimum response-completion "
           f"to next request-start interval: **{min_gap}**. HTTP counts: **{http_text}**; transport failures: "
           f"**{transports}**. UTC interval: {audit['first_request']} to {audit['last_response']}.",
           "Raw responses and `.json.headers.txt` headers are immutable in [raw/api/scoring-all/](raw/api/scoring-all/). "
           "The [manifest](raw/api/scoring-all/requests.jsonl) records timestamp, age, N, K, status, "
           "request payload, curl outcome, source and response hashes. The offline builder verifies "
           "body/header/source hashes, HTTP headers, exact vectors, pacing, and the three-failure abort rule. "
           "It never requests the network. See [audit](logs/phase5-validation.json) and [CSV](scoring-table.csv).",
           "An existing manifested file is verified and skipped on resume. Unmanifested files are preserved "
           "and stop collection for offline reconciliation. Three consecutive HTTP 429, 403, 5xx or transport "
           "failures stop collection immediately; the persisted streak prevents automatic restart calls."]
    if abort_failures:
        doc += ["**We appear blocked. Collection stopped on the third consecutive blocking failure.**",
                table(["UTC request start", "HTTP", "curl exit", "Saved response"],
                      [[r["timestamp"], r["http_status"], r["curl_exit_code"],
                        f"[raw]({r['file']})"] for r in abort_failures])]
    if failures:
        doc += ["Failed/unusable observations (these are not score-table measurements):",
                table(["Age", "K", "HTTP", "Observation", "Evidence"],
                      [[r["age"], r["K"], r["http"], r["observation"], f"[raw]({r['file']})"]
                       for r in failures])]
    if schema_issues or orphan_paths:
        doc += ["Integrity issues requiring review: `" + json.dumps(
            dict(schema_issues=schema_issues, unmanifested_files=orphan_paths)) + "`."]
    doc += ["## Summary by returned age",
            "First-K columns require all lower K values to have observed reports. `none` means absent "
            "across the complete age sweep; `unknown` means collection is incomplete. The capped-age "
            "column lists every observed numeric devAge with `capped:true`.",
            table(["Age A", "N", "Σ served rates", "First K: devAge=A", "Min K: not below_floor",
                   "First K: capped", "Capped devAge", "Reports"], age_summary),
            "## Rounded expected Yes count",
            f"At K = round(Σ served rates), devAge equals A in **{control_matches}/{known_control_count} "
            f"observed ages**. There are **{len(exceptions)} observed exceptions** and "
            f"**{len(unknown_controls)} unmeasured ages**. " + (
                "The relation holds for every age 0–48." if control_matches == 49 else
                "The relation does not hold for every age 0–48." if exceptions else
                "The available evidence does not establish whether it holds for every age."),
            "Rounding uses the exact decimal sum of saved rates and nearest integer, with .5 ties to even "
            "(Python's `round` convention). This avoids a binary floating-point summation artifact. "
            "The alternative .5-up result is shown for every exact tie below. The rounded local rates "
            "do not reveal the server's underlying norm curves."]
    if exceptions:
        doc.append(table(["Age", "Σ rates", "K", "Returned state", "Returned devAge", "Evidence"],
                         [[r["age"], r["expected_yes"], r["K"], r["state"], r["devAge"],
                           f"[raw]({r['file']})"] for r in exceptions]))
    else:
        doc.append("Observed exceptions: none.")
    if unknown_controls:
        doc.append("Unmeasured control ages: " + ", ".join(str(r["age"]) for r in unknown_controls) + ".")
    if ties:
        doc.append(table(["Age", "Σ rates", "Ties-even K", "devAge", ".5-up K", ".5-up devAge", ".5-up observation"],
                         [[r["age"], r["expected_yes"], r["even_K"], r["even_devAge"],
                           r["half_up_K"], r["half_up_devAge"], r["half_up_observation"]] for r in ties]))
    doc += ["## Band formula check",
            "For every new numeric report, compute `r = devAge / max(A,1)`: `r > 1.15` → `well_ahead`; "
            "else `r > 1.05` → `little_ahead`; else `r >= 0.95` → `on_pace`; else `building`. "
            f"Observed matches: **{band_matches}/{len(numeric)}**. Mismatches: **{len(mismatches)}**. "
            "The denominator includes only Phase 5 HTTP-200 complete numeric reports, and excludes "
            "below-floor responses, failures and uncollected combinations."]
    if mismatches:
        doc.append(table(["Age", "K", "devAge", "Returned band", "Formula band", "Evidence"],
                         [[r["age"], r["K"], r["devAge"], r["band"], r["expected"],
                           f"[raw]({r['file']})"] for r in mismatches]))
    else:
        doc.append("Band mismatches: none observed.")
    doc += ["## Monotonicity",
            "Ages with any decreasing numeric devAge as K increases: **" +
            (", ".join(map(str, nonmonotonic_ages)) or "none observed") + "**. "
            "This compares consecutive observed numeric reports for each age, including across gaps; "
            "omitted ages in below-floor reports have no numeric value to compare. "
            f"Complete-sweep coverage: {len(complete_ages)}/49 ages."]
    if decreases:
        doc.append(table(["Age", "From K", "To K", "From devAge", "To devAge"],
                         [[r[key] for key in ("age", "from_K", "to_K", "from_devAge", "to_devAge")]
                          for r in decreases]))
    doc.append("Numeric-to-below_floor transitions at adjacent K: " +
               (json.dumps(numeric_to_floor) if numeric_to_floor else "none observed") + ".")
    doc += ["## How to rebuild the headline score",
            "1. Choose the served list whose returned ageMonths equals the child's effective assessment "
            "age A. Flatten its section anchors/items and calibration entries, keeping each ID once.",
            "2. Collect one numeric Yes/No answer for every ID in that exact list. Count the Yes answers "
            "to obtain K. Use row (A,K) in scoring-table.csv, or the K range in the age table below.",
            "3. Return that row's stage, state, devAge, band and capped flag exactly. An omitted devAge "
            "stays omitted; a cap is part of the measured result. Do not interpolate or replace a missing row.",
            "4. These are the headline outputs with extended:true. Extending the answered ID set changes "
            "the scoring context and is outside this lookup. Area months, atLeast flags, skills and activity "
            "can depend on which answers are Yes; do not reproduce them from global K alone.",
            "**Observed versus inferred:** these tables directly measure one cumulative vector per K. "
            "Applying a row to every other answer arrangement with the same served IDs and K uses the "
            "Phase 3 count-sufficiency finding (40/40 reversed-order and 6/6 randomized age-12 controls). "
            "This phase does not independently test all answer arrangements at every age. The lookup "
            "reproduces measured behavior; it does not recover hidden norm tables or establish validity. "
            "The four area columns and their atLeast flags in the CSV are observations for the specific "
            "ascending-rate vector only.",
            "## Per-age headline lookups",
            "Rows collapse consecutive K only when stage, state, devAge, band and capped are identical. "
            "Each range links its first and last raw response; every individual observation is in the CSV. "
            "— means not returned. Unknown/failure rows are explicitly labeled."]
    for age, age_rows in grouped.items():
        compact = []
        for group in ranges(age_rows):
            first, last = group[0], group[-1]
            if first["observation"] == "not_collected":
                evidence = "not collected"
            else:
                evidence = f"[K={first['K']}]({first['file']})"
                if len(group) > 1:
                    evidence += f" … [K={last['K']}]({last['file']})"
            compact.append([k_range(group), first["state"], first["devAge"], first["band"],
                            first["capped"], "complete" if is_report(first) else first["observation"], evidence])
        doc += [f"### Age {age} months — N={age_rows[0]['N']}",
                table(["K range", "State", "devAge", "Band", "Capped", "Stage / observation", "Evidence"], compact)]
    doc += ["## 12-line summary", "```text\n" + "\n".join(summary) + "\n```"]
    (ROOT / "SCORING-TABLE.md").write_text("\n\n".join(doc) + "\n")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
