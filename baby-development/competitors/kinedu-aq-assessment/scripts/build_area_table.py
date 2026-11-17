#!/usr/bin/env python3
"""Build Phase 6 tables, audit and 12-line summary from saved evidence, offline."""
import collections
import csv
import datetime as dt
import hashlib
import json
import re

from collect_area_table import (
    ROOT, OUT, URL, MANIFEST, PACE_SECONDS, AREAS, ORDER_CHECKS, area_lists,
    plan, paths, records, validate_existing, blocking_tail, orphans, digest,
)

FIELDS = ["age", "area", "n_area", "K", "http", "state", "devAge",
          "area_state", "area_months", "atLeast", "file"]


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


def report(row):
    return row["observation"] == "observed_report"


def numeric(row):
    return report(row) and number(row["area_months"])


def signature(row):
    return tuple(row[key] for key in ("area_months", "atLeast", "area_state", "state", "observation"))


def collapse(rows):
    groups = []
    for row in rows:
        if groups and signature(row) == signature(groups[-1][-1]) and row["K"] == groups[-1][-1]["K"] + 1:
            groups[-1].append(row)
        else:
            groups.append([row])
    return groups


def k_range(group):
    lo, hi = group[0]["K"], group[-1]["K"]
    return str(lo) if lo == hi else f"{lo}–{hi}"


def first_k(rows, predicate):
    """First exposed value requires every earlier planned response to be known."""
    for row in rows:
        if not report(row):
            return "unknown"
        if predicate(row):
            return row["K"]
    return "none exposed"


def read_row(job, bank, by_key, issues):
    age, area, k, order = job
    path, _ = paths(*job)
    row = dict.fromkeys(FIELDS, "")
    row.update(age=age, area=area, n_area=len(bank[age]["areas"][area]["ranked"]), K=k,
               file=str(path.relative_to(ROOT)), observation="not_collected", order=order, areas={})
    rec = by_key.get(job)
    if rec is None:
        return row
    row["http"] = rec["http_status"]
    if rec["curl_exit_code"] != 0:
        row["observation"] = "transport_failure"
        return row
    if rec["http_status"] != 200:
        row["observation"] = "http_error"
        return row
    try:
        data = json.loads(path.read_bytes())
    except (ValueError, UnicodeDecodeError):
        row["observation"] = "invalid_json"
        return row
    basic, detail = (data.get("basic"), data.get("detail")) if isinstance(data, dict) else (None, None)
    # Validate structure before treating anything as an observed report.
    if not isinstance(data, dict) or not isinstance(basic, dict) or not isinstance(detail, dict):
        row["observation"] = "unexpected_schema"
        return row
    row["state"] = basic.get("state", "")
    row["devAge"] = basic.get("devAge", "")
    row["observation"] = "observed_report" if (
        data.get("stage") == "complete" and row["state"] in ("ok", "below_floor", "not_enough")
    ) else "unexpected_schema"
    if row["state"] == "ok" and not number(row["devAge"]):
        row["observation"] = "unexpected_schema"
    for name in ("basic", "detail"):
        if data[name].get("ageMonths", age) != age:
            issues.append(dict(file=row["file"], issue=f"{name} returned age differs"))
    for key in ("state", "devAge", "band", "capped"):
        if key in detail and detail[key] != basic.get(key):
            issues.append(dict(file=row["file"], issue=f"detail/basic {key} differs"))
    areas = detail.get("areas", [])
    if not isinstance(areas, list) or any(not isinstance(a, dict) for a in areas):
        row["observation"] = "unexpected_schema"
        return row
    row["areas"] = {a.get("area"): a for a in areas}
    if len(row["areas"]) != len(areas) or set(row["areas"]) - set(AREAS):
        issues.append(dict(file=row["file"], issue="duplicate/unknown reported area"))
    target = row["areas"].get(area, {})
    row["area_state"] = target.get("state", "")
    row["area_months"] = target.get("months", "")
    row["atLeast"] = target.get("atLeast", "")
    if row["state"] == "ok":
        if set(row["areas"]) != set(AREAS):
            row["observation"] = "unexpected_schema"
        for name, value in row["areas"].items():
            if value.get("state") == "ok":
                if not number(value.get("months")) or type(value.get("atLeast")) is not bool:
                    row["observation"] = "unexpected_schema"
            elif value.get("state") != "not_enough":
                issues.append(dict(file=row["file"], issue=f"unexpected {name} state"))
    return row


def audit_requests(recs, bank):
    gaps, header_verified, proxy_checks = [], 0, {}
    for i, rec in enumerate(recs):
        entry = bank[rec["age"]]
        if rec["N"] != len(entry["items"]) or rec["n_area"] != len(entry["areas"][rec["area"]]["ranked"]):
            raise ValueError("Manifest item count differs")
        if rec["baseline"] != {name: group["baseline"] for name, group in entry["areas"].items()}:
            raise ValueError("Manifest baseline differs")
        if rec["rate_sums"] != {name: group["rate_sum"] for name, group in entry["areas"].items()}:
            raise ValueError("Manifest rate sums differ")
        if rec["proxy_wrapper"] != "scripts/proxy_curl.sh" or rec["endpoint"] != URL:
            raise ValueError("Unexpected proxy wrapper/endpoint")
        proxy = rec["proxy_check"]
        if proxy["file"] not in proxy_checks:
            path = ROOT / proxy["file"]
            if digest(path) != proxy["sha256"]:
                raise ValueError("Proxy check hash differs")
            data = json.loads(path.read_text())
            if (data.get("passed") is not True or data.get("curl_exit_code") != 0
                    or data.get("country") != proxy["country"] or data.get("country") == "LT"
                    or data.get("sleep_before_request_seconds", 0) < PACE_SECONDS):
                raise ValueError("Proxy country check did not pass")
            proxy_checks[proxy["file"]] = data
        if rec["sleep_before_request_seconds"] < PACE_SECONDS:
            raise ValueError("Recorded sleep below two seconds")
        headers = (ROOT / rec["headers"]).read_text()
        statuses = [int(s) for s in re.findall(r"^HTTP/\S+\s+(\d{3})", headers, re.M)]
        if rec["curl_exit_code"] == 0:
            if not statuses or statuses[-1] != rec["http_status"]:
                raise ValueError(f"HTTP header status differs: {rec['file']}")
            header_verified += 1
        started = dt.datetime.fromisoformat(rec["timestamp"])
        completed = dt.datetime.fromisoformat(rec["completed_at"])
        if completed < started:
            raise ValueError("Response completion precedes request start")
        check_completed = dt.datetime.fromisoformat(proxy_checks[proxy["file"]]["completed_at"])
        if (started - check_completed).total_seconds() < PACE_SECONDS:
            raise ValueError("Request preceded proxy check or two-second pacing")
        if i:
            gap = (started - dt.datetime.fromisoformat(recs[i - 1]["completed_at"])).total_seconds()
            if gap < PACE_SECONDS:
                raise ValueError(f"Request gap below 2 seconds: {gap}")
            gaps.append(gap)
        if len(blocking_tail(recs[:i])) >= 3:
            raise ValueError("Request occurred after three blocking failures")
    return dict(header_statuses_verified=header_verified, minimum_gap_seconds=min(gaps) if gaps else None,
                proxy_countries=sorted({v["country"] for v in proxy_checks.values()}),
                proxy_preflight_requests=len(proxy_checks),
                proxy_check_files=sorted(proxy_checks))


def order_comparisons(all_rows):
    result = []
    index = {(r["age"], r["area"], r["K"], r["order"]): r for r in all_rows}
    for age, area in ORDER_CHECKS.items():
        asc = [r for r in all_rows if r["age"] == age and r["area"] == area and r["order"] == "ascending"]
        pairs, numeric_pairs, month_matches, area_pairs, area_matches, unavailable, mismatches = 0, 0, 0, 0, 0, [], []
        interior_numeric_pairs = 0
        for a in asc:
            b = index[(age, area, a["K"], "descending")]
            if not (report(a) and report(b)):
                continue
            pairs += 1
            if numeric(a) and numeric(b):
                numeric_pairs += 1
                month_matches += a["area_months"] == b["area_months"]
                interior_numeric_pairs += 0 < a["K"] < a["n_area"]
            if a["area_state"] and b["area_state"]:
                area_pairs += 1
                matched = tuple(a[key] for key in ("area_state", "area_months", "atLeast")) == tuple(
                    b[key] for key in ("area_state", "area_months", "atLeast"))
                area_matches += matched
                if not matched:
                    mismatches.append(dict(K=a["K"], ascending={key:a[key] for key in ("area_state", "area_months", "atLeast", "file")},
                                           descending={key:b[key] for key in ("area_state", "area_months", "atLeast", "file")}))
            else:
                unavailable.append(a["K"])
        result.append(dict(age=age, area=area, expected=len(asc), report_pairs=pairs,
                           numeric_pairs=numeric_pairs, month_matches=month_matches,
                           interior_numeric_pairs=interior_numeric_pairs,
                           area_pairs=area_pairs, area_matches=area_matches,
                           unexposed_K=unavailable, mismatches=mismatches))
    return result


def repeat_area_checks(all_rows, bank):
    """Check independence at equal per-area counts, including other-target sweeps."""
    known, comparisons, conflicts = {}, 0, []
    for row in all_rows:
        if not report(row):
            continue
        for name, value in row["areas"].items():
            k = row["K"] if name == row["area"] else bank[row["age"]]["areas"][name]["baseline"]
            key = row["age"], name, k
            sig = value.get("state"), value.get("months"), value.get("atLeast")
            if key in known:
                comparisons += 1
                if known[key][0] != sig:
                    conflicts.append(dict(age=row["age"], area=name, K=k,
                                          previous=known[key][1], current=row["file"],
                                          previous_value=known[key][0], current_value=sig))
            else:
                known[key] = sig, row["file"]
    return dict(comparisons=comparisons, conflicts=conflicts)


def main():
    bank = area_lists()
    jobs = list(plan(bank))
    recs = records()
    validate_existing(recs, bank)
    by_key = {(r["age"], r["area"], r["K"], r["order"]):r for r in recs}
    if len(by_key) != len(recs):
        raise ValueError("Duplicate manifest key")
    request_audit = audit_requests(recs, bank)
    issues = []
    all_rows = [read_row(job, bank, by_key, issues) for job in jobs]
    rows = [r for r in all_rows if r["order"] == "ascending"]
    (ROOT / "logs").mkdir(exist_ok=True)
    with (ROOT / "area-table.csv").open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows({key:str(row[key]).lower() if isinstance(row[key], bool) else row[key]
                         for key in FIELDS} for row in rows)

    grouped = {(age, area): [r for r in rows if r["age"] == age and r["area"] == area]
               for age in range(49) for area in AREAS}
    summary, decreases = [], []
    for (age, area), group in grouped.items():
        entry = bank[age]["areas"][area]
        nums = [r for r in group if numeric(r)]
        for before, after in zip(nums, nums[1:]):
            if after["area_months"] < before["area_months"]:
                decreases.append(dict(age=age, area=area, from_K=before["K"], to_K=after["K"],
                                      from_months=before["area_months"], to_months=after["area_months"],
                                      from_file=before["file"], to_file=after["file"]))
        summary.append(dict(age=age, area=area, n=len(entry["ranked"]), expected_yes=entry["rate_sum"],
                            baseline_K=entry["baseline"],
                            first_equals_A=first_k(group, lambda r:numeric(r) and r["area_months"] == age),
                            first_numeric=first_k(group, numeric),
                            first_atLeast=first_k(group, lambda r:r["atLeast"] is True),
                            reports=sum(report(r) for r in group), expected=len(group)))

    no_numeric_groups = [s for s in summary if s["reports"] == s["expected"]
                         and s["first_numeric"] == "none exposed"]
    checks = order_comparisons(all_rows)
    independence = repeat_area_checks(all_rows, bank)
    unknown = orphans(recs)
    observed = sum(report(r) for r in all_rows)
    status = "COMPLETED" if (len(recs) == len(jobs) and observed == len(jobs)
                             and not issues and not unknown) else "BLOCKED"
    counts = collections.Counter(r["http_status"] for r in recs)
    transports = sum(r["curl_exit_code"] != 0 for r in recs)
    complete_groups = sum(all(report(r) for r in g) for g in grouped.values())
    complete_ages = sum(all(report(r) for a in AREAS for r in grouped[age, a]) for age in range(49))
    glitch_groups = sorted({(d["age"], d["area"]) for d in decreases})
    available = sum(numeric(r) for r in rows)
    floor = sum(report(r) and r["state"] == "below_floor" for r in rows)
    not_enough = sum(report(r) and r["area_state"] == "not_enough" for r in rows)
    order_numeric = sum(c["numeric_pairs"] for c in checks)
    order_matches = sum(c["month_matches"] for c in checks)
    order_area = sum(c["area_pairs"] for c in checks)
    order_area_matches = sum(c["area_matches"] for c in checks)
    tail = blocking_tail(recs)
    bad_rows = [{key:r[key] for key in ("age", "area", "K", "order", "file", "observation", "http")}
                for r in all_rows if r["observation"] not in ("observed_report", "not_collected")]
    audit = dict(status=status, expected_requests=len(jobs), requests=len(recs), complete_reports=observed,
                 ascending_expected=len(rows), descending_expected=len(jobs)-len(rows),
                 http_counts=dict(counts), transport_failures=transports,
                 complete_age_area_groups=complete_groups, complete_ages=complete_ages,
                 numeric_area_rows=available, below_floor_rows=floor, area_not_enough_rows=not_enough,
                 no_numeric_groups=no_numeric_groups,
                 schema_issues=issues, bad_rows=bad_rows, unmanifested_files=unknown,
                 blocking_tail=[{key:r[key] for key in ("timestamp", "http_status", "curl_exit_code", "file")} for r in tail],
                 summary=summary, decreases=decreases, order_checks=checks, area_independence=independence,
                 **request_audit)
    (ROOT / "logs/phase6-validation.json").write_text(json.dumps(audit, indent=2) + "\n")

    summary_lines = [
        f"{status}: {len(recs)}/{len(jobs)} assessment requests; {observed}/{len(jobs)} complete reports.",
        f"Coverage: {complete_ages}/49 complete ages; {complete_groups}/196 complete age-area sweeps.",
        f"HTTP: {', '.join(f'{k}={v}' for k,v in sorted(counts.items())) or 'none'}; transport failures={transports}.",
        f"Proxy: {', '.join(request_audit['proxy_countries']) or 'unverified'}; {request_audit['proxy_preflight_requests']} country check(s); wrapper only; sequential; 2.0s sleep.",
        f"Ascending rows: {len(rows)} planned; {available} numeric area months; {floor} below_floor; {not_enough} area not_enough.",
        "Baselines: per-item area grouping; exact decimal rate sums; nearest-integer rounding with .5 ties to even.",
        f"Glitches: {len(glitch_groups)} age-area groups with {len(decreases)} observed decreases; exact K values in AREA-TABLE.md.",
        f"Descending order checks: {order_matches}/{order_numeric} numeric-month pairs match; {order_area_matches}/{order_area} exposed area records match.",
        f"Repeated area/count checks: {independence['comparisons']} comparisons; {len(independence['conflicts'])} conflicts.",
        f"Abort streak: {len(tail)}; HTTP codes={[r['http_status'] for r in tail]}; curl codes={[r['curl_exit_code'] for r in tail]}.",
        "Outputs: area-table.csv, AREA-TABLE.md, raw/api/area-sweep/requests.jsonl, logs/phase6-validation.json.",
        "Recipe: choose returned age and its served area IDs, count Yes, then look up K; hidden or unmeasured months stay unknown.",
    ]
    assert len(summary_lines) == 12
    (ROOT / "logs/phase6-summary.txt").write_text("\n".join(summary_lines) + "\n")

    md = [f"{status}: {len(recs)}/{len(jobs)} assessment requests; {observed}/{len(jobs)} complete reports.",
          "", "# Kinedu AQ: per-area Yes-count tables (Phase 6)", "",
          "## 12-line summary", "", "```text", *summary_lines, "```", "",
          "## Method and evidence", "",
          "**Observed** values come only from the linked saved API responses. **Inferred** describes an explanatory model, not recovered server code. Blank CSV cells and — here mean the API omitted the field or the request has not been collected; zero is a numeric observed month value. No missing value is filled from Phase 3, Phase 5, a neighboring K, or a norm hypothesis.", "",
          "The [collector](scripts/collect_area_table.py) reuses Phase 5's returned-age indexing and flattens every section anchor, section item and calibration item. It groups by each **item's own `area`**, including calibration displayed under another domain. For each age and area, sort by ascending `(rate,id)` and set the first `round(sum(rates))` IDs to Yes. Rounding uses exact decimal saved rates and nearest integer with .5 ties to even. This defines the requested expected-count baseline; it is not a claim that every baseline produces on_pace or months=A.", "",
          "Sweep one target area's K from 0 through its item count, retaining the other three areas at their individual baselines. Every request supplies every served ID exactly once, numeric y=0/1, `action:result`, the returned age, and `extended:true`. The answer-array order stays fixed. Descending controls reverse the target-area `(rate,id)` ranking for ages 3/Physical, 12/Cognitive and 30/Language, keeping all other answers identical.", "",
          "All HTTP calls use [scripts/proxy_curl.sh](scripts/proxy_curl.sh). The first call was the required ipinfo country check; collection aborts for LT or an unverifiable country. Assessment calls use only POST `/api/assessment`, with exactly the User-Agent, Content-Type, Origin and Referer in [ENUMERATION.md](ENUMERATION.md). Requests are sequential with a 2.0-second sleep before every request, including preflight. No proxy credentials are read or included in this report.", "",
          f"Assessment HTTP counts: **{dict(sorted(counts.items()))}**; transport failures: **{transports}**. There were **{request_audit['proxy_preflight_requests']}** additional proxy-country check requests. Minimum measured response-completion to next request-start gap: **{request_audit['minimum_gap_seconds']} seconds**. Verified response/header/source hashes and HTTP header statuses: **{request_audit['header_statuses_verified']} requests**. Proxy countries recorded for these requests: **{request_audit['proxy_countries']}**.", "",
          "Raw bodies and `.json.headers.txt` files are immutable under [raw/api/area-sweep/](raw/api/area-sweep/); descending controls are in its `order-check/` subdirectory. The [manifest](raw/api/area-sweep/requests.jsonl) records UTC timestamps, age, area, K, HTTP status, request body, source and response SHA-256s, proxy-check evidence and curl exit status. Existing manifested files are verified and skipped. Unmanifested files stop collection for offline reconciliation. Three consecutive 429/403/5xx/transport failures stop collection and prevent restart requests. The [builder](scripts/build_area_table.py) is entirely offline; [validation JSON](logs/phase6-validation.json) records its checks. Rebuild with `python3 scripts/build_area_table.py`.", ""]
    if status == "BLOCKED":
        md += [f"**BLOCKED / incomplete evidence:** {len(jobs)-len(recs)} requests are uncollected; {len(bad_rows)} attempted requests lack a complete report. Blocking streak HTTP codes: {[r['http_status'] for r in tail]}; curl codes: {[r['curl_exit_code'] for r in tail]}. Unmanifested files: {unknown}. Schema issues: {issues}.", ""]
    if bad_rows:
        md += [table(["Age", "Area", "K", "Order", "HTTP", "Observation", "Evidence"],
                     [[r["age"], r["area"], r["K"], r["order"], r["http"], r["observation"],
                       f"[raw]({r['file']})"] for r in bad_rows]), ""]
    md += ["## Summary by age and area", "",
           "First-K columns mean the first **exposed** match, numeric month, or true atLeast in this exact sweep. `none exposed` means every K was measured but no such value was returned; `unknown` means an earlier missing/error response prevents identifying the first K. A below_floor report exposes no area months, so it cannot establish a latent area age. Odd A may have no equality on the observed two-month grid.", "",
           f"**{len(no_numeric_groups)} complete age-area sweeps expose no numeric months at any K:** "
           + ("; ".join(f"age {s['age']} / {s['area']} (n={s['n']})" for s in no_numeric_groups) or "none")
           + ". Their returned states remain in the tables; no numeric ages are substituted.", "",
           table(["Age A", "Area", "n", "Σ rates (expected Yes)", "Baseline K", "First K: months=A", "Min K: numeric months", "First K: atLeast", "Reports"],
                 [[s["age"],s["area"],s["n"],s["expected_yes"],s["baseline_K"],s["first_equals_A"],
                   s["first_numeric"],s["first_atLeast"],f"{s['reports']}/{s['expected']}"] for s in summary]), "",
           "## Nonmonotonic area months (the glitch)", "",
           f"Observed **{len(decreases)} decreases across {len(glitch_groups)} age-area pairs**. The table lists every decrease between successive exposed numeric observations in increasing K, with exact K and months. Omitted/uncollected months are not assigned a number; a K gap is visible in the listed endpoints. This is an observed scoring defect, not an inferred norm curve.", ""]
    if decreases:
        md += [table(["Age", "Area", "K before → after", "Months before → after", "Evidence"],
                     [[d["age"],d["area"],f"{d['from_K']} → {d['to_K']}",
                       f"{d['from_months']} → {d['to_months']}",
                       f"[before]({d['from_file']}) / [after]({d['to_file']})"] for d in decreases]), ""]
    else:
        md += ["No decrease has been observed in the collected numeric values. Incomplete sweeps cannot establish monotonicity for unmeasured K.", ""]
    md += ["## Descending order checks", "",
           "Equal K compares different Yes identities within the target area, with the same served IDs and other-area baseline. Only pairs with exposed numeric months contribute to the months denominator. The endpoints K=0 and K=n use identical Yes sets; the interior-pair count identifies numeric comparisons with different Yes sets. Exposed `not_enough` records can contribute to the complete area-record comparison; matching below_floor responses do not reveal months and are excluded from both denominators.", "",
           table(["Age", "Area", "Report pairs", "Numeric months match", "Interior numeric pairs", "Area state/months/atLeast match", "K with no exposed area", "Result"],
                 [[c["age"], c["area"], f"{c['report_pairs']}/{c['expected']}",
                   f"{c['month_matches']}/{c['numeric_pairs']}", c["interior_numeric_pairs"], f"{c['area_matches']}/{c['area_pairs']}",
                   ", ".join(map(str,c["unexposed_K"])),
                   "MISMATCH" if c["mismatches"] else ("all exposed pairs match" if c["report_pairs"] == c["expected"] else "incomplete")]
                  for c in checks]), ""]
    for check in checks:
        for mismatch in check["mismatches"]:
            md += [f"Order mismatch at age {check['age']}, {check['area']}, K={mismatch['K']}: `{json.dumps(mismatch, sort_keys=True)}`.", ""]
    md += [f"Repeated `(age, own area, own Yes count)` outputs across all sweeps: **{independence['comparisons']} comparisons, {len(independence['conflicts'])} conflicts**. This also checks other-area independence wherever area records are exposed. Conflicts, if any, are listed in the validation JSON.", "",
           "**Inference:** agreement at equal K supports a count lookup for these fixed served-area ID sets. Three control sweeps do not prove identity-independence for every age, arbitrary subset, future server version or extension set. The underlying norm projection and quantization formula remain unresolved.", "",
           "## How to compute an area's months from its Yes count", "",
           "1. Use the assessment's returned integer `ageMonths` to select the saved initial list. Include every anchor, item and calibration question, assigning it to its own `area` field.",
           "2. For the target area, count the Yes answers among that exact area's served IDs. This integer is K; n is the number of those IDs. The rates set the experimental baseline and ordering, but are not demonstrated per-answer score weights.",
           "3. Find `(age, area, K)` in [area-table.csv](area-table.csv) or the compact tables below. Read `area_months`, `area_state` and `atLeast` together; true atLeast means a lower-bound month value, not an exact ceiling-free age.",
           "4. Keep the global reporting gate: below_floor hides area months, and area not_enough supplies no numeric month. Missing fields are unknown, not zero. This table directly measures the other-three-areas baseline; applying its area mapping to other profiles relies on the separately tested independence inference and still requires an exposed report.",
           "5. Use the measured lookup as it stands, including low-K decreases. Interpolation, smoothing, a universal Yes percentage, and an exact formula from the rounded rates would add unobserved assumptions. A changed ID set or extension requires a different lookup.", "",
           "## Compact tables for every returned age", "",
           "State is shown as `area state / headline state`; — means omitted. Consecutive rows collapse only when months, atLeast, both states and observation status match. Each evidence link points to the first/last raw response in that K range; every individual path remains in the CSV. Uncollected ranges have no evidence link.", ""]
    for age in range(49):
        md += [f"### Age {age}", ""]
        for area in AREAS:
            entry = bank[age]["areas"][area]
            md += [f"#### {area} (n={len(entry['ranked'])}, Σ rates={entry['rate_sum']}, baseline K={entry['baseline']})", ""]
            compact = []
            for group in collapse(grouped[age, area]):
                r = group[0]
                state = f"{r['area_state'] or '—'} / {r['state'] or '—'}"
                if not report(r):
                    state = r["observation"] + (f" (HTTP {r['http']})" if r["http"] != "" else "")
                if r["observation"] == "not_collected":
                    evidence = ""
                elif len(group) == 1:
                    evidence = f"[raw]({r['file']})"
                else:
                    evidence = f"[first]({r['file']}) / [last]({group[-1]['file']})"
                compact.append([k_range(group),r["area_months"],r["atLeast"],state,evidence])
            md += [table(["K", "Months", "atLeast", "State (area / headline)", "Evidence"], compact), ""]
    (ROOT / "AREA-TABLE.md").write_text("\n".join(md))
    print("\n".join(summary_lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
