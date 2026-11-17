#!/usr/bin/env python3
"""Build the bank and reports from saved responses, with no network access."""
import collections
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import re

from enumerate_api import ROOT, UA


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def runs(values):
    values = sorted(set(values))
    groups = []
    for value in values:
        if not groups or value != groups[-1][-1] + 1:
            groups.append([value])
        else:
            groups[-1].append(value)
    return ", ".join(str(g[0]) if len(g) == 1 else f"{g[0]}–{g[-1]}" for g in groups)


def flattened(data):
    output = []
    for index, section in enumerate(data["sections"]):
        if section.get("anchor"):
            output.append((section["anchor"], "anchor", section["area"]))
        output.extend((q, "item", section["area"]) for q in section["items"])
        if index < len(data.get("calibration", [])):
            output.append((data["calibration"][index], "calibration", section["area"]))
    assert len(data.get("calibration", [])) <= len(data["sections"]), "Undisplayed calibration tail"
    return output


def empirical_correction(weeks):
    if weeks is None or weeks == 37:
        return 0
    if weeks == 24:
        return 4
    if 25 <= weeks <= 29:
        return 3
    if 30 <= weeks <= 33:
        return 2
    if 34 <= weeks <= 36:
        return 1
    raise ValueError(weeks)


def main():
    records = [json.loads(line) for line in (ROOT / "raw/api/requests.jsonl").read_text().splitlines()]
    assert len({r["file"] for r in records}) == len(records), "Manifest paths must be unique"
    loaded = []
    for record in records:
        raw = (ROOT / record["file"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == record["sha256"], record["file"]
        assert record["curl_exit_code"] == 0, record
        header = (ROOT / record["file"]).with_suffix(".headers.txt").read_text()
        http_codes = re.findall(r"^HTTP/\S+ (\d+)", header, flags=re.M)
        assert int(http_codes[-1]) == record["http_status"], record["file"]
        loaded.append((record, json.loads(raw)))
    timestamps = [dt.datetime.fromisoformat(r["requested_at_utc"]) for r in records if r.get("requested_at_utc")]
    minimum_start_gap = min((b - a).total_seconds() for a, b in zip(timestamps, timestamps[1:]))
    assert minimum_start_gap >= 0.5, minimum_start_gap

    sweep = {data["ageMonths"]: (record, data) for record, data in loaded
             if record["series"] == "monthly_sweep" and record["http_status"] == 200}
    assert set(sweep) == set(range(49)), sorted(sweep)
    ordered = {age: tuple(q["id"] for q, _, _ in flattened(data)) for age, (_, data) in sweep.items()}
    set_groups = collections.defaultdict(list)
    for age in sorted(ordered):
        assert len(ordered[age]) == len(set(ordered[age])), age
        set_groups[ordered[age]].append(age)
    set_ids = {key: f"S{index:02d}" for index, key in enumerate(set_groups)}
    unordered_count = len({frozenset(ids) for ids in ordered.values()})

    occurrences = collections.defaultdict(list)
    raw_keys = set()
    phases = collections.defaultdict(set)

    def add(record, question, age, phase, kind, area, placement=None, report_skill=None):
        raw_keys.update(question)
        phases[phase].add(question["id"])
        occurrences[question["id"]].append(dict(
            age=age, phase=phase, kind=kind, section_title=area,
            displayed_under=placement, report_skill=report_skill,
            raw=question, source=record["file"]))

    extensions = {}
    success_cores = collections.defaultdict(set)
    for record, data in loaded:
        if record["http_status"] != 200:
            continue
        if record["request"]["action"] == "start":
            age = data["ageMonths"]
            success_cores[age].add(compact({k: v for k, v in data.items() if k != "corrected"}))
            for question, kind, placement in flattened(data):
                add(record, question, age, "start", kind, question["area"], placement)
        else:
            age = record["request"]["ageMonths"]
            if record["series"] == "extension_discovery":
                extensions[age, record["profile"]] = (record, data)
            for question in data.get("items", []):
                add(record, question, age, "extension", "item", question["area"])
            for skill in data.get("skills", []):
                for question in skill["items"]:
                    add(record, question, age, "report", "item", skill["area"],
                        report_skill=skill["skill"])
    assert all(len(cores) == 1 for cores in success_cores.values()), "Same effective age changed payload"

    # Compare the API-derived inventory against both independent client dictionaries.
    bundle = (ROOT / "raw/js/562-f8a0c4482aa81c7b.js").read_text()
    dictionary_ids = []
    for module in [5668, 7578]:
        match = re.search(rf"{module}:function\(e\)\{{e\.exports=JSON\.parse\('((?:\\.|[^'\\])*)'\)", bundle)
        assert match, f"Cannot locate translation module {module}"
        dictionary_ids.append(set(map(int, re.findall(r'"(\d+)":', match.group(1)))))
    assert dictionary_ids[0] == dictionary_ids[1]
    assert set(occurrences) == dictionary_ids[0], (set(occurrences) ^ dictionary_ids[0])

    raw_columns = sorted(raw_keys)
    columns = ["question_id", "section_id", "section_title", "kind", "text",
               "age_months_min", "age_months_max", "age_months", "start_age_months_min",
               "start_age_months_max", "start_age_months", "extension_age_months",
               "report_age_months", "source_phases", "displayed_under", "report_skill"]
    columns += raw_columns + ["rate_by_age_months", "raw_observations", "sources"]
    csv_rows = []
    for qid, obs in sorted(occurrences.items()):
        ages = sorted({o["age"] for o in obs})
        start_ages = sorted({o["age"] for o in obs if o["phase"] == "start"})
        asked_obs = [o for o in obs if o["phase"] != "report"]
        # For IDs also used as questions, kind describes their question roles;
        # report-only IDs are items, explicitly identified by source_phases.
        kinds = {o["kind"] for o in (asked_obs or obs)}
        texts = {o["raw"]["title"] for o in obs}
        areas = {o["section_title"] for o in obs}
        assert len(texts) == len(areas) == 1, (qid, texts, areas)
        row = dict(
            question_id=qid, section_id="", section_title=next(iter(areas)),
            kind="|".join(k for k in ["anchor", "item", "calibration"] if k in kinds),
            text=next(iter(texts)), age_months_min=min(ages), age_months_max=max(ages),
            age_months=compact(ages),
            start_age_months_min=min(start_ages) if start_ages else "",
            start_age_months_max=max(start_ages) if start_ages else "",
            start_age_months=compact(start_ages),
            extension_age_months=compact(sorted({o["age"] for o in obs if o["phase"] == "extension"})),
            report_age_months=compact(sorted({o["age"] for o in obs if o["phase"] == "report"})),
            source_phases="|".join(p for p in ["start", "extension", "report"] if any(o["phase"] == p for o in obs)),
            displayed_under=compact(sorted({o["displayed_under"] for o in obs if o["displayed_under"]})),
            report_skill=compact(sorted({o["report_skill"] for o in obs if o["report_skill"]})),
            sources=compact(sorted({o["source"] for o in obs})))
        rates = collections.defaultdict(set)
        for o in obs:
            if "rate" in o["raw"]:
                rates[o["age"]].add(o["raw"]["rate"])
        row["rate_by_age_months"] = compact({a: sorted(v) for a, v in sorted(rates.items())})
        for field in raw_columns:
            values = {compact(o["raw"][field]) for o in obs if field in o["raw"]}
            vals = [json.loads(v) for v in sorted(values)]
            row[field] = "" if not vals else (vals[0] if len(vals) == 1 and not isinstance(vals[0], (dict, list)) else compact(vals))
        variants = {compact({k: v for k, v in o.items() if k != "source"}) for o in obs}
        row["raw_observations"] = "[" + ",".join(sorted(variants)) + "]"
        csv_rows.append(row)
    with (ROOT / "questions.csv").open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_rows)

    start_ids = phases["start"]
    report_only = set(occurrences) - start_ids - phases["extension"]
    overlaps = [len(set(ordered[a]) & set(ordered[a + 1])) for a in range(48)]
    overlap_pairs = sum(bool(set(ordered[a]) & set(ordered[b])) for a in range(49) for b in range(a + 1, 49))
    role_changes = [qid for qid, obs in occurrences.items() if len({o["kind"] for o in obs if o["phase"] == "start"}) > 1]
    rate_changes = [qid for qid, obs in occurrences.items() if len({o["raw"]["rate"] for o in obs if "rate" in o["raw"]}) > 1]
    all_rates = [o["raw"]["rate"] for obs in occurrences.values() for o in obs if "rate" in o["raw"]]
    statuses = collections.Counter(r["http_status"] for r in records)
    stages = collections.Counter((r["profile"], d.get("stage")) for r, d in extensions.values())
    report_statuses = sorted({o["raw"]["status"] for obs in occurrences.values() for o in obs if "status" in o["raw"]})
    all_no_floor = [age for (age, profile), (_, data) in extensions.items()
                    if profile == "all_no" and data.get("basic", {}).get("state") == "below_floor"]
    all_no_ok = [age for (age, profile), (_, data) in extensions.items()
                 if profile == "all_no" and data.get("basic", {}).get("state") == "ok"]
    assert sorted(all_no_ok) == [1] and len(all_no_floor) == 48
    repeat_data = next(d for r, d in loaded if r["series"] == "result_anomaly_repeat")
    assert repeat_data == extensions[1, "all_no"][1], "Age-one all-zero anomaly changed on repeat"

    samples = {}
    for r, d in loaded:
        if r["series"] in ["preterm_sample", "preterm_baseline"]:
            assert r["http_status"] == 200
            samples[r["nominal_age_months"], r["request"]["gestationalWeeks"]] = d
    for age in [0, 1, 2, 3, 4, 6, 9, 12, 18, 24]:
        assert samples[age, None]["ageMonths"] == age
        for gw in [28, 32, 36, 37]:
            data = samples[age, gw]
            correction = empirical_correction(gw) if age < 24 else 0
            assert data["ageMonths"] == max(0, age - correction), (age, gw, data)
            assert data["corrected"] == (gw < 37 and age < 24), (age, gw, data)
    integer_probes = {r["request"]["gestationalWeeks"]: d["ageMonths"]
                      for r, d in loaded if r["series"] == "correction_integer_probe"}
    for gw, corrected_age in integer_probes.items():
        assert corrected_age == 6 - empirical_correction(gw)
    null_baselines = {r["request"]["birthdate"]: d["ageMonths"] for r, d in loaded
                      if r["request"]["action"] == "start" and r["http_status"] == 200
                      and r["request"]["gestationalWeeks"] is None}
    for r, d in loaded:
        if r["request"]["action"] != "start" or r["http_status"] != 200:
            continue
        weeks = r["request"]["gestationalWeeks"]
        if weeks is None:
            continue
        chronological = null_baselines[r["request"]["birthdate"]]
        expected = max(0, chronological - empirical_correction(weeks)) if chronological < 24 else chronological
        assert d["ageMonths"] == expected, r
        assert d["corrected"] == (weeks < 37 and chronological < 24), r

    table = ["# Age → initial question list", "",
             "Ages below are the API's returned `ageMonths` (effective age), not the nominal filename offset. "
             "The November 2 day-15 sweep maps nominal offsets 1–49 to API ages 0–48. "
             "Nominal offset 0 is a saved future-birthdate failure.", "",
             "Order matches the client: each section's optional anchor, its items, then calibration at that section index. "
             "Section order is Physical, Cognitive, Language, Social-Emotional. "
             "A calibration item's domain can differ from the section where it is displayed.", "",
             "| API age, months | Set | Count | Ordered question IDs | Raw response |",
             "| --- | --- | ---: | --- | --- |"]
    for age, ids in sorted(ordered.items()):
        record = sweep[age][0]
        table.append(f"| {age} | {set_ids[ids]} | {len(ids)} | {', '.join(map(str, ids))} | [{Path(record['file']).stem}]({record['file']}) |")
    table += ["", "## Distinct sets and overlap", "",
              f"There are **{len(set_groups)} distinct ordered lists** across 49 supported integer ages. "
              f"There are also {unordered_count} distinct unordered memberships, so these differences are not merely reordering. "
              "No two ages share a complete initial list.", "",
              "| Set | Shared age range(s), months | Count |", "| --- | --- | ---: |"]
    for ids, ages in set_groups.items():
        table.append(f"| {set_ids[ids]} | {runs(ages)} | {len(ids)} |")
    table += ["", f"Every adjacent pair overlaps: **{min(overlaps)}–{max(overlaps)} shared IDs**. "
              f"Across all 1,176 age pairs, {overlap_pairs} share at least one ID. "
              "These are overlapping, age-selected windows from one shared bank, rather than disjoint age buckets. "
              "The term sliding window describes the overlap; the evidence does not establish a simple contiguous-index window algorithm.", "",
              "| Adjacent API ages | Shared IDs |", "| --- | ---: |"]
    table += [f"| {age} → {age + 1} | {overlaps[age]} |" for age in range(48)]
    table += ["", "## Additional, answer-dependent lists", "",
              "Each age was also submitted to `result` with `extended:false` using all-zero and all-one numeric answers "
              "to the initial questions. All-zero completed at every age: `below_floor` at 48 ages, "
              "but unexpectedly `on_pace` / `devAge:1` at age 1 (identical on a repeat request). "
              "All-one returned the following extension lists at ages 0–41; ages 42–48 completed without extension. "
              "These are observed profiles, not an exhaustive enumeration of all answer combinations.", "",
              "| API age | All-one stage | Extra count | Ordered extension IDs | Raw response |",
              "| --- | --- | ---: | --- | --- |"]
    for age in range(49):
        r, d = extensions[age, "all_yes"]
        ids = [q["id"] for q in d.get("items", [])]
        table.append(f"| {age} | {d['stage']} | {len(ids)} | {', '.join(map(str, ids)) or '—'} | [{Path(r['file']).stem}]({r['file']}) |")
    table += ["", "Report inventories (`skills[].items`) are not initial or extension question lists. "
              f"They recover {len(report_only)} additional IDs; these are marked `source_phases=report` in [questions.csv](questions.csv).", ""]
    (ROOT / "age-map.md").write_text("\n".join(table))

    sample_lines = ["| Chronological API age | GW 28 | GW 32 | GW 36 | GW 37 control |",
                    "| --- | --- | --- | --- | --- |"]
    for age in [0, 1, 2, 3, 4, 6, 9, 12, 18, 24]:
        values = [f"{samples[age, gw]['ageMonths']} / {str(samples[age, gw]['corrected']).lower()}" for gw in [28, 32, 36, 37]]
        sample_lines.append(f"| {age} | " + " | ".join(values) + " |")
    bad_lines = []
    for r, d in loaded:
        if r["http_status"] != 200:
            bad_lines.append(f"| [{Path(r['file']).name}]({r['file']}) | {r['http_status']} | `{d.get('error')}` | {d.get('ageMonths', '—')} |")

    diagram = ["```mermaid", "flowchart LR"]
    for age, ids in sorted(ordered.items()):
        diagram.append(f'  A{age:02d}["{age} months"] --> {set_ids[ids]}["{set_ids[ids]}: {len(ids)} questions"]')
    diagram += ["```"]
    report = ["# Kinedu AQ API enumeration", "",
              "Collected on **2026-11-02** using the public first-party "
              "[assessment endpoint](https://webpromo.kinedu.com/api/assessment) and saved "
              "[client source](logs/phase2-source-contract.md). No browser was opened.", "",
              "## Findings", "",
              f"- **{len(occurrences)} unique IDs with English text recovered from the API**: {len(start_ids)} appear in initial questions; "
              f"{len(report_only)} additional IDs appear only in observed report inventories. The union exactly matches all 408 IDs "
              "in both saved Spanish and Portuguese client dictionaries; no dictionary ID is missing and no extra API ID was found.",
              f"- **{len(set_groups)} distinct ordered initial lists**, one per returned age 0–48 months. "
              f"All adjacent ages overlap ({min(overlaps)}–{max(overlaps)} shared IDs). Initial lists contain {min(map(len, ordered.values()))}–{max(map(len, ordered.values()))} questions.",
              "- The initial flow is one shared bank with age-specific overlapping lists. It is not one identical list for every age, "
              "and it is not a collection of disjoint age buckets. The API can add an answer-dependent extension; age alone does not determine the full assessment path.",
              "- The supported upper boundary is **48 returned months inclusive**. Returned ages 49, 50, and 51 all give HTTP 422 `age_range`.", "",
              "## Method and reproducibility", "",
              "1. Inspected the saved page JavaScript before calling the API: `input type=\"date\"` and explicit year/month/day concatenation establish `YYYY-MM-DD`. "
              "The exact start body contains only `action`, `birthdate`, and `gestationalWeeks`; see [source evidence](logs/phase2-source-contract.md).",
              "2. Confirmed start with `2026-05-02`, null gestation: HTTP 200, age 6, uncorrected. "
              "It was initially saved to `start_age06_gw-null.json`, then copied byte-for-byte to "
              "[smoke_start_age06_gw-null.json](raw/api/smoke_start_age06_gw-null.json) before the sweep reused the requested filename.",
              "3. Swept nominal offsets N=0…52 with DOB = November 2026 minus N calendar months, day 15, and null gestation. "
              "Stopped after three consecutive `age_range` responses. Every nominal response remains at the requested `start_ageNN_gw-null.json` path.",
              "4. For actual chronological ages 0,1,2,3,4,6,9,12,18,24, collected gestation 28,32,36,37 plus a paired null baseline. "
              "These use day 2, matching today's day, to obtain the actual requested completed-month age and a valid newborn DOB. "
              "Their files are `start_ageNN_gwWW.json`; paired baselines are `sample_ageNN_gw-null.json`.",
              "5. Added focused correction/cutoff probes, all-one/all-zero `result` profiles at all 49 ages, and one age-6 "
              "`extended:true` result to inspect report inventories. Numeric answers are exactly `y:0` or `y:1`, as in the client. "
              "Only `/api/assessment` was called; no leads, tracking, email, or checkout requests were sent.",
              "6. Saved every raw body, HTTP headers, request body, status, curl exit code, and SHA-256. "
              "Collector calls have UTC request-start timestamps; the initial manual smoke records only the response Date header, "
              "with request-start timestamp explicitly unknown. "
              f"There were {len(records)} requests: {statuses[200]} HTTP 200, {statuses[422]} HTTP 422, and {statuses[400]} HTTP 400; no transport failures. "
              "[requests.jsonl](raw/api/requests.jsonl) is the authoritative request-to-file manifest.",
              "7. Calls ran sequentially with a 0.5-second sleep before every subsequent request, realistic User-Agent, JSON Content-Type, Origin and Referer. "
              "No cookies or authorization header were needed. [Collector](scripts/enumerate_api.py), [focused probes](scripts/probe_api.py), "
              "and [offline report builder](scripts/build_enumeration.py) preserve the method. Collectors refuse to overwrite existing raw response paths.", "",
              "Exact first curl command (the archived smoke response is linked above):", "", "```sh",
              "curl --request POST 'https://webpromo.kinedu.com/api/assessment' \\",
              f"  --user-agent '{UA}' \\",
              "  --header 'Content-Type: application/json' \\",
              "  --header 'Origin: https://webpromo.kinedu.com' \\",
              "  --header 'Referer: https://webpromo.kinedu.com/aq-assessment' \\",
              "  --data-raw '{\"action\":\"start\",\"birthdate\":\"2026-05-02\",\"gestationalWeeks\":null}' \\",
              "  --connect-timeout 20 --max-time 60 --silent --show-error \\",
              "  --dump-header raw/api/start_age06_gw-null.headers.txt \\",
              "  --output raw/api/start_age06_gw-null.json \\",
              "  --write-out 'HTTP %{http_code}\\n'", "sleep 0.5", "```", "",
              "The sweep uses the same curl headers/options, changes the payload/output stem, and emits the numeric HTTP status into the manifest. "
              "Rebuild the derived artifacts without network calls using `python3 scripts/build_enumeration.py`.", "",
              "## Date labels and boundary", "",
              "The requested day-15 convention does not align nominal filenames with completed ages on November 2: "
              "`start_age00_gw-null.json` requests 2026-11-15, a future DOB, and returns HTTP 422 `invalid_birthdate`. "
              "`start_age01_gw-null.json` requests 2026-10-15 and returns age 0; `start_age06_gw-null.json` requests 2026-05-15 and returns age 5. "
              "The initial May 2 smoke call returns age 6. No failure was discarded or silently relabeled.", "",
              "| Nominal filename age | DOB | Returned ageMonths | HTTP / result |",
              "| --- | --- | ---: | --- |",
              "| 0 | 2026-11-15 | — | 422 invalid_birthdate |",
              "| 1 | 2026-10-15 | 0 | 200 |",
              "| 49 | 2022-10-15 | 48 | 200; last supported age |",
              "| 50 | 2022-09-15 | 49 | 422 age_range |",
              "| 51 | 2022-08-15 | 50 | 422 age_range |",
              "| 52 | 2022-07-15 | 51 | 422 age_range; stop |", "",
              "[age-map.md](age-map.md) therefore indexes by the API's returned age. "
              "All 49 integer ages 0–48 are covered despite the invalid nominal age-zero request.", "",
              "## Corrected age", "",
              "Let C be the paired null-gestation API age. In the observed integer-week UI range 24–36, the exact empirical rule is:", "",
              "```text", "d(g) = 4 months for g = 24",
              "       3 months for g = 25…29", "       2 months for g = 30…33",
              "       1 month  for g = 34…36", "       0 months for g = 37 or null (controls)",
              "if C < 24 and g is 24…36:", "    ageMonths = max(0, C - d(g))", "    corrected = true",
              "else:", "    ageMonths = C", "    corrected = false", "```", "",
              "This is consistent with rounding `(40 - gestationalWeeks) × 7 / 30.44` to whole months and subtracting that integer "
              "from the uncorrected completed-month age. The server source is unavailable: the precise days-per-month constant is an inference, "
              "not an observed implementation. The table above states what was directly established for every integer week accepted by the client slider. "
              "No claim is made for fractional weeks or weeks outside the tested UI/control range.", "",
              "Rounding is material: gestation 30 corrects 6 → 4 (two months), not three months. "
              "The May 30 null/GW30 pair returns 5 → 3, which rules out simply flooring continuous day age after subtracting 70 days "
              "with a 30.44-day month (that would give 2 at collection time). "
              "At chronological age 0, preterm responses still set `corrected:true` while age remains clamped to 0.", "",
              "Table cells are `ageMonths / corrected`; each row has a paired null baseline equal to the chronological age:", "",
              *sample_lines, "",
              "Correction stops at **chronological C=24**, not corrected age 24. With GW28: DOB 2024-11-03 gives C=23 → 20/true, "
              "while DOB 2024-11-02 gives C=24 → 24/false; DOB 2024-11-01 also gives 24/false. "
              "Thus the observed threshold is the completed 24th month. The age-24 sample returns 24/false for all four requested gestations.", "",
              "All repeated start responses with the same returned age were identical after removing only `corrected`, "
              "including their order and raw item fields. In these samples, gestation changes the list by changing effective age; it does not create a separate preterm bank.", "",
              "## Language", "",
              "Skipped language API variations because no assessment request in the saved client has a `lang`, `language`, or locale field. "
              "The client reads URL `lang`, chooses English/Spanish/Portuguese, and translates question IDs and area headings locally; "
              "API question `title` is the English fallback. This establishes the client contract, not whether the server accepts arbitrary unobserved fields. "
              "Some result activity titles do contain server-provided `en`/`es`/`pt` maps.", "",
              "## Bank, CSV semantics, and completeness", "",
              f"[questions.csv](questions.csv) has one row per ID ({len(occurrences)} data rows), with the requested columns plus every raw per-item field "
              f"observed: `{', '.join(raw_columns)}`. It includes {len(start_ids)} initial IDs, {len(phases['extension'])} extension IDs "
              f"(all already in the initial union), and {len(phases['report'])} report IDs. Exactly {len(report_only)} IDs occur only in observed report inventories.", "",
              "- `age_months_min/max` and exact `age_months` cover every observed API occurrence, including report inventories. "
              "They are bounds, not an assertion that an ID appears at every age between them. "
              "Use `start_age_months_min/max` and exact `start_age_months` for the initial question-selection range. "
              "Report-only rows have empty initial bounds and `start_age_months=[]`; `extension_age_months` and `report_age_months` keep other contexts explicit.",
              "- `source_phases` identifies `start`, `extension`, and/or `report`. `kind` lists observed question roles separated by `|` "
              "when an ID changes role. Extension and report inventory entries are `item`; report presence is not evidence that a question was asked in that assessment.",
              "- The API supplies no section ID or section title field. `section_id` is empty. `section_title` uses the domain heading (`area`) "
              "from the item or enclosing report skill. `displayed_under` preserves actual start section placement; calibration can be cross-domain. "
              "`report_skill` stores enclosing report skill labels separately from the raw question `skill`.",
              "- Raw columns retain scalar values when constant, JSON arrays when values differ, and empty cells when absent. "
              "`rate_by_age_months` preserves age-dependent rates. `raw_observations` preserves every distinct raw item with age, phase, kind, domain, "
              "display section and report-skill context; `sources` links all original bodies. A missing raw `rate` or `skill` for a report-only item is not invented.",
              "- This inventory is complete relative to all 408 IDs in both saved client translation dictionaries. "
              "It is not proof that the server contains no unreferenced, untranslated, historical, or otherwise unreachable IDs. "
              "All initial integer ages are enumerated; all possible extension answer combinations are not.", "",
              "Report-only IDs: `" + ", ".join(map(str, sorted(report_only))) + "`.", "",
              "## Response structure and scoring clues", "",
              "- Start top-level keys are exactly `ageMonths`, `corrected`, `sections`, `calibration`. "
              "Section keys are `area`, `anchor`, `items`; `anchor` may be null. Initial/extension question keys are exactly "
              "`id`, `area`, `skill`, `title`, `rate`. No `difficulty`, `weight`, or `domain` key was returned on those items.",
              f"- `rate` ranges from {min(all_rates)} to {max(all_rates)} across observed initial/extension items. "
              f"{len(rate_changes)} IDs have multiple rate values across contexts/ages; do not flatten one ID to a single rate. "
              f"{len(role_changes)} initial IDs change role among anchor/item/calibration. "
              "For example ID 285 has rate 0.92 at age 0, 0.96 at age 1, and 0.98 when returned at age 5. "
              "Area/skill/rate and report curves suggest age-based calibration; the field's exact statistical meaning and scoring weights are not exposed.",
              "- There are four domain sections at every supported age, but item distribution and anchor availability vary. "
              "Age 0 has 11 Physical items and 5 Language items; age 6 has 8 items per section. "
              "Calibration has three entries at ages 0–36 and zero at 37–48. Ages 0–36 have 39 initial questions; 37–44 have 36; "
              "45 has 33; 46 has 27; 47 has 24; 48 has 22. At age 45 only Social-Emotional retains an anchor; ages 46–48 have no anchors.",
              "- Numeric all-one results return eight extension items at each age 0–41, and complete at ages 42–48. "
              "All-zero completes as `below_floor` at 48 ages. **Unexpectedly, age 1 with all 39 numeric answers zero returns "
              "`state:\"ok\"`, `band:\"on_pace\"`, `devAge:1`, `capped:false`**, including a Physical area age of 2 and "
              "Language `not_enough`. A repeat returned the identical JSON body; see "
              "[original](raw/api/result_age01_all_no_numeric.json) and [repeat](raw/api/result_age01_all_no_repeat.json). "
              "This is a scoring anomaly to investigate, not evidence of a particular hidden formula. "
              "The 42 observed extension lists contain 77 unique IDs, all present in the initial union. "
              "This confirms answer-dependent server behavior; it does not disclose the extension selection algorithm for mixed answers.",
              "- A successful complete result can expose `basic`, `detail`, `skills`, `activity`; below-floor results expose "
              "`basic`, `detail`, `floorActivities`. Observed report flags include `band`, `devAge`, `capped`, `tier`, `areasLocked`, "
              "`teaserArea`, `areasDefaultHidden`, and per-area `atLeast`. Skill groups expose `from`, `to`, `total`, `reached`, "
              "`focus`, `childPct`, and `curve:[{age,pct,lo,hi}]`; their inventory items expose `id`, `title`, `status` "
              "(" + ", ".join(f"`{s}`" for s in report_statuses) + " observed). These report fields are not raw question weights.",
              "- For the age-6 all-one `extended:true` probe, `basic` returns `devAge:31`, `capped:true`, `band:\"well_ahead\"`; "
              "this bypassed extension solely to inspect the inventory, not to model a real child or validate scoring.", "",
              "## Saved failures", "",
              "The future-DOB failure and three range failures were expected from the sweep. "
              "Two exploratory `result` requests incorrectly used JSON booleans for `y` and returned HTTP 400 `invalid_body`. "
              "Both were preserved, then repeated successfully using numeric zero/one. No request failure is represented as a successful enumeration.", "",
              "| Raw body | HTTP | Error | ageMonths |", "| --- | ---: | --- | --- |", *bad_lines, "",
              "## Age → set diagram", "",
              "Each node uses returned effective age. Gestation maps chronological age to one of these effective ages as described above. "
              "See [age-map.md](age-map.md) for exact ordered IDs and extension lists.", "", *diagram, "",
              "## Validation", "",
              "The offline builder checks response SHA-256s, HTTP header statuses, transport success, recorded request-start spacing, "
              "all 49 initial ages, unique IDs within every initial list, "
              "paired correction samples, integer-week probes, identical payloads for equal effective ages, CSV ID uniqueness, "
              "and equality of the recovered bank with both independent translation dictionaries. "
              "All checks passed. Raw HTTP errors remain evidence, not failed validation.", ""]
    (ROOT / "ENUMERATION.md").write_text("\n".join(report))

    summary = [
        "1. Collected on 2026-11-02 using paced curl requests; no browser opened.",
        f"2. Saved {len(records)} requests: {statuses[200]} HTTP 200, four HTTP 422, two HTTP 400; no transport failures.",
        "3. Birthdate format is YYYY-MM-DD; assessment requests need no language field.",
        "4. The day-15 age-zero DOB is future and fails; nominal ages 1–49 return ages 0–48.",
        "5. All API ages 0–48 are covered; ages 49, 50, 51 return age_range.",
        f"6. Initial questions contain {len(start_ids)} unique IDs and {len(set_groups)} distinct ordered age lists.",
        f"7. Adjacent lists share {min(overlaps)}–{max(overlaps)} IDs: overlapping age windows in one shared bank.",
        "8. Initial list sizes range from 39 down to 22; calibration disappears at age 37.",
        "9. GW28/GW32/GW36 subtract 3/2/1 whole months below chronological age 24.",
        "10. Corrected age clamps at zero; GW37 is uncorrected; correction stops at 24 months.",
        "11. All-one gives eight extension items at ages 0–41; all-zero unexpectedly gives on_pace at age 1.",
        f"12. Extensions use {len(phases['extension'])} IDs, all already present among initial questions.",
        f"13. Reports add {len(report_only)} inventory-only IDs: {len(occurrences)} recovered IDs match both client dictionaries.",
        "14. questions.csv preserves roles, exact ages, raw fields, varying rates, contexts, and sources.",
        "15. ENUMERATION.md and age-map.md document results; unreachable server IDs remain unproven.",
    ]
    assert len(csv_rows) == len({row["question_id"] for row in csv_rows}) == 408
    assert len(summary) == 15
    (ROOT / "logs/phase2-summary.txt").write_text("\n".join(summary) + "\n")
    (ROOT / "logs/phase2-stats.json").write_text(json.dumps(dict(
        requests=len(records), http_statuses=statuses, unique_questions=len(occurrences),
        minimum_request_start_gap_seconds=minimum_start_gap,
        initial_questions=len(start_ids), extension_questions=len(phases["extension"]),
        report_questions=len(phases["report"]), report_only_questions=len(report_only),
        distinct_ordered_sets=len(set_groups), distinct_unordered_sets=unordered_count,
        adjacent_overlap_min=min(overlaps), adjacent_overlap_max=max(overlaps),
        overlapping_age_pairs=overlap_pairs, varying_rate_ids=len(rate_changes),
        multiple_initial_roles=len(role_changes), raw_item_fields=raw_columns,
        extension_stages={f"{k[0]}/{k[1]}": v for k, v in stages.items()},
        all_zero_below_floor_ages=sorted(all_no_floor), all_zero_ok_ages=sorted(all_no_ok),
        report_item_statuses=report_statuses,
    ), ensure_ascii=False, indent=2) + "\n")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
