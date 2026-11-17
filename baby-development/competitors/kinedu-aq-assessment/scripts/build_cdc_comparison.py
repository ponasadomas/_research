#!/usr/bin/env python3
"""Build the CDC comparison and audit artifacts from local captures, without HTTP."""

import csv
import hashlib
import json
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw/cdc"
DOMAINS = ["Social/Emotional", "Language/Communication", "Cognitive", "Movement/Physical"]
VERDICTS = ["consistent", "stricter/later", "clearly later", "high >95%", "not estimable"]


def read_csv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def pct(value, estimate=False):
    if value is None:
        return "—"
    value = Decimal(str(value)) * 100
    return f"{value:.2f}%" if estimate else f"{value.normalize():f}%"


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers, rows):
    return ["| " + " | ".join(map(cell, headers)) + " |",
            "| " + " | ".join("---" for _ in headers) + " |"] + [
                "| " + " | ".join(map(cell, row)) + " |" for row in rows]


def verdict(value):
    if value is None:
        return "not estimable"
    if value > Decimal("0.95"):
        return "high >95%"
    if value >= Decimal("0.75"):
        return "consistent"
    if value >= Decimal("0.50"):
        return "stricter/later"
    return "clearly later"


def statistics(rows):
    values = [r["share"] for r in rows if r["share"] is not None]
    return {"matched": len(rows), "numeric": len(values),
            "observed": sum(r["method"] == "observed" for r in rows),
            "interpolated": sum(r["method"] == "interpolated" for r in rows),
            "verdicts": {v: sum(r["verdict"] == v for r in rows) for v in VERDICTS},
            "median": float(median(values)) if values else None,
            "below_75": sum(v < Decimal("0.75") for v in values)}


def build():
    cdc_rows = read_csv(RAW / "cdc-milestones.csv")
    cdc = {r["cdc_id"]: r for r in cdc_rows}
    questions = {int(r["question_id"]): r for r in read_csv(ROOT / "questions.csv")}
    matches = json.loads((RAW / "matches.json").read_text())
    unmatched = json.loads((RAW / "unmatched-reasons.json").read_text())
    assert len(cdc) == len(cdc_rows) == 144
    assert len({m[0] for m in matches}) == len(matches)
    assert len({m[1] for m in matches}) == len(matches), "Do not reuse a question in aggregate counts"
    assert {m[0] for m in matches}.isdisjoint(unmatched)
    assert set(cdc) == {m[0] for m in matches} | set(unmatched)
    for candidates, confidence, reason in unmatched.values():
        assert confidence in ("loose", "none") and bool(reason)
        assert all(qid in questions for qid in candidates)

    # Cross-check every input rate against the original observation objects, not just matched items.
    raw_rate_count = 0
    empty_rate_count = 0
    for q in questions.values():
        rates = json.loads(q["rate_by_age_months"])
        raw_rates = defaultdict(set)
        for observation in json.loads(q["raw_observations"]):
            if "rate" in observation["raw"]:
                raw_rates[str(observation["age"])].add(observation["raw"]["rate"])
                raw_rate_count += 1
        assert {age: sorted(values) for age, values in raw_rates.items()} == rates, q["question_id"]
        assert all(len(values) == 1 and 0 <= values[0] <= 1 for values in rates.values())
        empty_rate_count += not bool(rates)

    rows = []
    for cid, qid, confidence, reason in matches:
        assert confidence in ("exact", "close")
        c, q = cdc[cid], questions[qid]
        age = int(c["age_months"])
        rates = {int(k): Decimal(str(v[0])) for k, v in json.loads(q["rate_by_age_months"]).items()}
        before = max((m for m in rates if m < age), default=None)
        after = min((m for m in rates if m > age), default=None)
        value = rates.get(age)
        method = "observed" if value is not None else "not estimable"
        if value is None and before is not None and after is not None:
            assert before < age < after
            value = rates[before] + (rates[after] - rates[before]) * Decimal(age - before) / Decimal(after - before)
            method = "interpolated"
            assert min(rates[before], rates[after]) <= value <= max(rates[before], rates[after])
        row = {**c, "age": age, "qid": qid, "qtext": q["text"], "qarea": q["area"],
               "confidence": confidence, "reason": reason, "rates": rates,
               "before": before, "after": after, "share": value, "method": method,
               "verdict": verdict(value), "band": "0–12" if age <= 12 else "13–24" if age <= 24 else "25–48"}
        rows.append(row)

    overall = statistics(rows)
    observed = statistics([r for r in rows if r["method"] == "observed"])
    exact = statistics([r for r in rows if r["confidence"] == "exact"])
    exact_observed = statistics([r for r in rows if r["confidence"] == "exact" and r["method"] == "observed"])
    by_domain = {d: statistics([r for r in rows if r["domain"] == d]) for d in DOMAINS}
    by_band = {b: statistics([r for r in rows if r["band"] == b]) for b in ["0–12", "13–24", "25–48"]}
    stats = {"overall": overall, "observed_only": observed, "exact_only": exact,
             "exact_observed_only": exact_observed, "by_cdc_domain": by_domain, "by_age_band": by_band}
    for groups in (by_domain, by_band):
        assert sum(s["matched"] for s in groups.values()) == overall["matched"]
        assert sum(s["numeric"] for s in groups.values()) == overall["numeric"]
        for v in VERDICTS:
            assert sum(s["verdicts"][v] for s in groups.values()) == overall["verdicts"][v]
    (RAW / "comparison-summary.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n")

    export = []
    for r in rows:
        export.append({"cdc_id": r["cdc_id"], "cdc_age_months": r["age"], "cdc_domain": r["domain"],
                       "cdc_milestone": r["milestone"], "question_id": r["qid"], "question_text": r["qtext"],
                       "kinedu_area": r["qarea"], "rate_by_age_months": json.dumps({str(k): float(v) for k, v in sorted(r["rates"].items())}),
                       "nearest_before_month": r["before"], "nearest_before_rate": r["rates"].get(r["before"]),
                       "nearest_after_month": r["after"], "nearest_after_rate": r["rates"].get(r["after"]),
                       "share_at_cdc_age": "" if r["share"] is None else str(r["share"]),
                       "estimate_method": r["method"], "interpolation_gap_months": r["after"] - r["before"] if r["method"] == "interpolated" else "",
                       "verdict": r["verdict"], "match_confidence": r["confidence"], "match_reason": r["reason"],
                       "cdc_source_url": r["source_url"], "cdc_source_file": r["source_file"], "kinedu_sources": questions[r["qid"]]["sources"]})
    with (RAW / "matched-pairs.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(export[0]))
        writer.writeheader()
        writer.writerows(export)

    def summary_row(label, group, cdc_total="—"):
        return [label, cdc_total, group["matched"], group["observed"], group["interpolated"],
                group["verdicts"]["consistent"], group["verdicts"]["stricter/later"],
                group["verdicts"]["clearly later"], group["verdicts"]["high >95%"],
                group["verdicts"]["not estimable"], pct(group["median"], True)]

    lines = ["# Kinedu rates versus CDC milestones (Phase 9)", "",
             "**The usable comparisons lean toward making children look ahead, conditional on `rate` meaning “share already doing it.”** "
             "Of 20 matched pairs with a share available at the CDC age, 11 are below CDC's 75% floor, seven are 75–95%, "
             "and two exceed 95%. The median is 73.75%. Restricting to the 14 directly observed values gives a 67.50% median, "
             "with nine below 75%. This is evidence of lower Kinedu expectations in this selected subset, not proof of dishonesty or a bank-wide bias.", "",
             "## Method and sources", "",
             "Retrieved **2026-11-03**. All HTTP used `scripts/proxy_curl.sh`; no browser was used. "
             "The 11 requested ages are 2, 4, 6, 9, 12, 15, 18, 24, 30, 36 and 48 months. "
             "Ten legacy checklist URLs redirected successfully. The legacy 15-month URL and legacy index returned 404; "
             "the [current CDC index](https://www.cdc.gov/act-early/milestones/index.html) links the working "
             "[15-month checklist](https://www.cdc.gov/act-early/milestones/15-months.html). "
             "Every fetched response body, including failed HTTP responses, is saved under [raw/cdc/](raw/cdc/). "
             "[Fetch provenance](raw/cdc/fetch-manifest.json), [checklist counts and SHA-256 hashes](raw/cdc/checklist-manifest.json), "
             "and [methodology source notes](raw/cdc/methodology-notes.md) preserve the audit trail.", "",
             "CDC's February 2022 revision places milestones at checklist ages by which **about 75% or more** of children "
             "would be expected to do them. It shifted the selection rule away from average-age/50% expectations, using a literature "
             "review and clinical judgment. These are communication and developmental-monitoring checklists, not item-by-item empirical "
             "prevalence curves, developmental standards, or validated screening/diagnostic tools. "
             "[CDC's explanation of the revision](https://www.cdc.gov/act-early/milestones/key-points.html) supports these distinctions. "
             "The captures are current pages implementing that revision, not a frozen copy of the February 2022 website; page-update dates are later.", "",
             "**Extraction.** We extracted only the milestone bullet sentences under the four developmental headings, "
             "excluding parenting tips, doctor questions and duplicate media-modal captions. "
             "The result is **144 milestones** in [cdc-milestones.csv](raw/cdc/cdc-milestones.csv), with CDC age, normalized domain, "
             "original sentence, source URL and local capture path. The requested ages stop at four years; five-year milestones are excluded.", ""]

    counts = Counter(int(r["age_months"]) for r in cdc_rows)
    lines += table(["CDC age (months)", "Extracted milestones", "Matched", "Observed at age", "Interpolated at age"],
                   [[a, counts[a], sum(r["age"] == a for r in rows),
                     sum(r["age"] == a and r["method"] == "observed" for r in rows),
                     sum(r["age"] == a and r["method"] == "interpolated" for r in rows)] for a in counts])
    lines += ["", "**Semantic matching.** The 408 Kinedu questions were read against the CDC sentences; no text-similarity score "
              "was used as a substitute for matching the behavior and difficulty. We retained **71 pairs: 53 exact and 18 close**. "
              "“Exact” means the essential behavior and threshold agree, even if wording differs. “Close” preserves the core task/level "
              "with a narrower example or a small contextual qualification; the reason is stated for every pair. These remain human judgments, "
              "so the exact-only result is also reported. “Loose” candidates have a material difference or uncertainty in support, gesture cues, "
              "word count, task, reliability or complexity and are excluded from all numeric summaries. "
              "For example, a chuckle is not matched to a full laugh, trying a spoon is not matched to independent spoon feeding, "
              "and asking questions is not matched to answering them. Two tempting vocal-response pairs (143 and 23) are also excluded: "
              "Kinedu specifies babbling, which could be harder than CDC's unspecified sounds. Each CDC milestone and Kinedu question is counted at most once. "
              "Alternative hidden-toy, first-step, color and dressing questions are not multiplied into additional votes. "
              "The complete decisions are in [matches.json](raw/cdc/matches.json) and [unmatched-reasons.json](raw/cdc/unmatched-reasons.json).", "",
              "**Rates and estimates.** Inputs are [questions.csv](questions.csv), specifically `rate_by_age_months` and "
              "`raw_observations`, with [questions-by-age.md](questions-by-age.md) as the base-question presentation record. "
              "All rates in the CSV agree with the raw observations: 2,173 rate-bearing observation objects, with no conflicting "
              "rates at the same question/age. We use numeric rates from both base and extension questions; report-only `status` values "
              "are not converted to rates. Thirty-five questions have no rate observations, including three of the matched questions.", "",
              "For each pair, every available age-specific rate is listed in the table, sorted by month. An observed value at the "
              "CDC month takes precedence. Otherwise, we show the nearest observed month on each side and calculate "
              "`p(X) = p(L) + (X − L) × [p(U) − p(L)] / (U − L)` only when `L < X < U`. "
              "Interpolation is an inference, not an observation. All six interpolation gaps are 4–8 months, so these estimates are weak, "
              "especially near 75%. If only one side exists, or neither exists, the CDC-age value is **not estimable**: "
              "we do not carry a rate forward, extrapolate, treat a missing rate as zero, or substitute a report's `typical` status. "
              "We preserve non-monotonic rates without smoothing: for example, the approximately-50-word item (373) drops from "
              "67% at 30 months to 64% at 33 months. Thresholds use unrounded values; percentages are rounded only for display.", "",
              "**Verdict rules (mutually exclusive).** “Consistent” is 75% through 95%; “stricter/later” is 50% through less than 75%; "
              "“clearly later” is below 50%; and “high >95%” is above 95%. Exactly 50% belongs to stricter/later and exactly 75% to consistent. "
              "The high group is also compatible with the CDC floor and is separated only to implement the requested high-share flag. "
              "Lower Kinedu shares would tend to make the same achievements look better; high shares could make a missing skill look worse. "
              "These are interpretations of expectations, not measured changes to an individual child's AQ result.", "",
              "**The CDC floor is one-sided.** A rate above 95% at the CDC age does **not** establish earlier attainment or inflation: "
              "CDC allows any share at or above 75%. Nor does a CDC placement imply every earlier month's true share must be below 75%; "
              "checklist ages are discrete and do not identify an exact 75th-percentile crossing. "
              "Thus the requested “nearly all do it earlier / parents look worse” verdict is shown as a **high-share flag**, "
              "with actual earlier observations discussed separately. A “consistent” rate is compatible with the floor, not validated as the true population rate.", "",
              "## Summary", ""]

    verdict_notes = {
        "consistent": "75–95%; compatible with the CDC floor",
        "stricter/later": "50–<75%; lower share, tending to make children look ahead",
        "clearly later": "<50%; substantially below the CDC floor",
        "high >95%": ">95%; floor-compatible high flag, not proof of inflation",
        "not estimable": "No observed value or two-sided bracket at the CDC age"}
    lines += table(["Verdict", "Observed", "Interpolated", "Total", "Meaning"],
                   [[v, observed["verdicts"][v], sum(r["method"] == "interpolated" and r["verdict"] == v for r in rows),
                     overall["verdicts"][v], verdict_notes[v]] for v in VERDICTS])
    lines += ["", "The 20 numeric comparisons are **14 observed + 6 interpolated**. Of the **51 unestimable** pairs, "
              "47 have rates only before the CDC age, one only after it, and three have no numeric rates. "
              "Missing-age pairs remain in the matched table and denominator for coverage, but are excluded from medians and numeric verdict percentages. "
              "Below-floor pairs are **11/20 (55.0%)** with interpolation or **9/14 (64.3%)** observed only. "
              "Nine of 20 meet the floor, including both high flags. No retained strict pair is below 50%.", ""]

    summary_headers = ["Group", "CDC items", "Matched", "Observed", "Interpolated", "Consistent", "50–<75%", "<50%", ">95%", "No estimate", "Median of numeric shares"]
    lines += ["### By CDC domain", ""]
    lines += table(summary_headers, [summary_row(d, by_domain[d], sum(c["domain"] == d for c in cdc_rows)) for d in DOMAINS])
    lines += ["", "Domain follows the **CDC heading**, even when Kinedu assigns the question to a different area. "
              "The numeric sample sizes are only 5 social/emotional, 8 language, 2 cognitive and 5 movement/physical; "
              "the domain medians should not be read as population estimates.", "", "### By CDC age band", ""]
    lines += table(summary_headers, [summary_row(b, by_band[b], sum(("0–12" if int(c["age_months"]) <= 12 else "13–24" if int(c["age_months"]) <= 24 else "25–48") == b for c in cdc_rows)) for b in by_band])
    lines += ["", "Band membership uses CDC's milestone age. The 13–24-month numeric results are all at **15 months**: "
              "there are no estimable pairs at 18 or 24 months. The 25–48-month band has seven numeric pairs and all are below 75%; "
              "its two 48-month points are close matches. Uneven coverage prevents a claim about every age in a band.", "", "### Sensitivity to matching and interpolation", ""]
    lines += table(["Selection", "Matched/selected rows", "Numeric", "Below 75%", "75–95%", ">95%", "Median"],
                   [[label, st["matched"], st["numeric"], st["below_75"], st["verdicts"]["consistent"], st["verdicts"]["high >95%"], pct(st["median"], True)]
                    for label, st in [("Exact + close; observed + interpolation", overall),
                                      ("Exact + close; observed only", observed),
                                      ("Exact only; observed + interpolation", exact),
                                      ("Exact only; observed only", exact_observed)]])
    lines += ["", "The direction survives both restrictions: the **nine exact, directly observed** pairs have a 67% median, "
              "with six below 75%. This is a descriptive sensitivity check, not independent replication: items and developmental skills are correlated.", "",
              "## Matched pairs", "",
              "Each heading gives the CDC age in months; every CDC sentence links to its captured source page. "
              "In “all rates,” `m:value` means month `m` and the Kinedu rate as a percentage. "
              "For missing-age rows, “before” and “after” are the nearest rate-bearing months; `—` means none was observed. "
              "The CSV retains unrounded estimates and individual endpoint columns: [matched-pairs.csv](raw/cdc/matched-pairs.csv).", ""]

    for age in counts:
        lines += [f"### CDC age {age} months", ""]
        pair_table = []
        for r in (r for r in rows if r["age"] == age):
            rates_text = "; ".join(f"{m}:{pct(v)}" for m, v in sorted(r["rates"].items())) or "No numeric rates"
            if r["method"] == "observed":
                estimate = f"**{pct(r['share'])} observed** at {age}m"
            else:
                before = "—" if r["before"] is None else f"{r['before']}m:{pct(r['rates'][r['before']])}"
                after = "—" if r["after"] is None else f"{r['after']}m:{pct(r['rates'][r['after']])}"
                estimate = (f"**{pct(r['share'], True)} interpolated**" if r["share"] is not None else "**Not estimable**") + f"; before {before}; after {after}"
            pair_table.append([f"{r['cdc_id']} · {r['domain']} · [{r['milestone']}]({r['source_url']})",
                               f"**{r['qid']}** · {r['qtext']}", rates_text, estimate, r["verdict"],
                               f"**{r['confidence']}** — {r['reason']}"])
        lines += table(["CDC milestone and domain", "Kinedu id + question", "All Kinedu shares by month", "Share at CDC age / nearest months", "Verdict", "Confidence and reason"], pair_table)
        lines += [""]

    lines += ["## What is observed, and what is inferred", "",
              "**Observed in the API data:** Kinedu assigns 68% at nine months to shyness around strangers (186), "
              "57% at 15 months to stacking two blocks (179), "
              "67% at 30 months to about 50 words (373), and 58% at 36 months to being understood by most people (622). "
              "These are exact matches below the CDC floor. The recorded values establish what the API returned, not real-world prevalence. "
              "The tempting 26% vocal-response rate at four months (143) and 40% turn-taking rate at six months (23) are also observed, "
              "but their babbling-versus-any-sounds ambiguity prevents a strict comparison; they receive no verdict and do not enter the counts.", "",
              "**Observed high cases:** hand-to-mouth (41) is 97% at CDC's four-month checkpoint, with 96% at two months and 98% "
              "at three months. Familiar-caregiver recognition (97, close match) is 98% at six months, with 56% at birth-month zero "
              "and 73% at one month. These are the only two >95% checkpoint flags. Earlier high hand-to-mouth values are real API "
              "observations; CDC supplies no earlier prevalence curve against which to call them inflated. "
              "Other matched items also exceed 75% before their CDC checkpoint—such as noun-plus-verb phrases (696), 88–92% at "
              "21–22 months versus CDC's 30 months—but have no measurable checkpoint share. They cannot be assigned a checkpoint verdict.", "",
              "**Interpolation assumptions:** the six estimates below connect observations separated by 4–8 months. "
              "In particular, understanding no is estimated at **74.50%**, only half a percentage point below the cutoff; "
              "that classification is fragile. No uncertainty interval is available from the API.", ""]
    lines += table(["CDC age", "Question", "Before", "After", "Gap (months)", "Interpolated share", "Verdict"],
                   [[r["age"], r["qid"], f"{r['before']}m:{pct(r['rates'][r['before']])}", f"{r['after']}m:{pct(r['rates'][r['after']])}",
                     r["after"] - r["before"], pct(r["share"], True), r["verdict"]] for r in rows if r["method"] == "interpolated"])
    lines += ["", "**Inference about how parents look:** if `rate` is the proportion of children already achieving the skill, "
              "then a lower expected share generally makes a given child's achievements look more advanced. "
              "The checkpoint subset therefore leans **ahead**, especially in the usable older language and motor comparisons. "
              "Early-age comparisons are mixed, and many later checkpoints are missing. The data do not establish a systematic "
              "pattern of inflated shares designed to make parents feel behind.", "",
              "**What this cannot establish:** the meaning of `rate` remains our interpretation, not a verified Kinedu definition or "
              "a documented population dataset. CDC's thresholds mix published evidence with expert placement and are not exact norms "
              "for estimating inflation. Population, wording and reporting conditions could differ. The 71 semantic pairs are selected "
              "from 408 questions, and only 20/71 have a usable checkpoint value; these are not a random, independent sample. "
              "The comparison does not reconstruct or measure a parent's final AQ score. Consequently, “lower than CDC's floor in this "
              "subset” is supported; “dishonest,” “universally deflated,” or “all babies will look ahead” is not.", "",
              "## Unmatched CDC milestones", "",
              "**73 of 144** CDC milestones lack a strict counterpart. This includes 66 with only loose candidates and seven "
              "without a relevant candidate. They are distinct from the 51 matched pairs with missing checkpoint rates. "
              "All rejected candidates below have confidence **loose**, receive no rate verdict, and are excluded from summaries; "
              "“none” means no candidate. The full CDC sentences are retained so omissions can be reviewed.", ""]
    for age in counts:
        lines += [f"### Unmatched at {age} months", ""]
        for c in (c for c in cdc_rows if int(c["age_months"]) == age and c["cdc_id"] in unmatched):
            candidates, confidence, reason = unmatched[c["cdc_id"]]
            candidate_text = "loose candidates " + ", ".join(map(str, candidates)) if candidates else "no candidate"
            lines.append(f"- **{c['domain']} · {c['cdc_id']}** — [{c['milestone']}]({c['source_url']}). Rejected: {candidate_text}. {reason}")
        lines += [""]

    lines += ["## Reproduction", "",
              "Run `python3 scripts/extract_cdc_milestones.py` then `python3 scripts/build_cdc_comparison.py` from this folder. "
              "Both operate offline on the saved HTML, curated match decisions and Kinedu CSV; they perform no network calls. "
              "[comparison-summary.json](raw/cdc/comparison-summary.json) contains the summary counts and medians, and "
              "[comparison-validation.json](raw/cdc/comparison-validation.json) records input hashes and coverage/rate checks.", "",
              "## 12-line summary", "",
              "1. CDC's 2022 framework places milestones where about 75% or more are expected to do them.",
              "2. All 11 requested checklists were saved through the proxy; 144 milestone sentences were extracted.",
              "3. There are 71 retained pairs: 53 exact and 18 close; loose candidates are excluded.",
              "4. Seventy-three CDC milestones have no strict Kinedu counterpart.",
              "5. Only 14 pairs have an observed rate at the CDC age; six more permit interpolation.",
              "6. Fifty-one matched pairs have no estimable checkpoint rate; none was extrapolated.",
              "7. Of 20 numeric pairs, 11 are 50–<75% and none is below 50%.",
              "8. Seven are 75–95%; two exceed 95%, which remains compatible with CDC's floor.",
              "9. The overall median is 73.75%; the directly observed median is 67.50%.",
              "10. Exact, observed matches alone still lean low: six of nine below 75%, with a 67% median.",
              "11. Conditional on the rate interpretation, this subset tends to make children look ahead, not behind.",
              "12. Sparse coverage, uncertain rate meaning and CDC's floor prevent bank-wide or dishonesty claims."]
    (ROOT / "CDC-COMPARISON.md").write_text("\n".join(lines) + "\n")

    unestimated = [r for r in rows if r["share"] is None]
    assert sum(r["before"] is not None and r["after"] is None for r in unestimated) == 47
    assert sum(r["after"] is not None and r["before"] is None for r in unestimated) == 1
    assert sum(not r["rates"] for r in unestimated) == 3
    assert overall["verdicts"] == {"consistent": 7, "stricter/later": 11, "clearly later": 0, "high >95%": 2, "not estimable": 51}
    assert len(lines[-12:]) == 12 and all(line.startswith(f"{i}. ") for i, line in enumerate(lines[-12:], 1))
    validation = {"result": "passed", "cdc_milestones": len(cdc), "kinedu_questions": len(questions),
                  "matched": len(rows), "unmatched_cdc": len(unmatched), "duplicate_cdc_matches": 0,
                  "duplicate_kinedu_matches": 0, "rate_bearing_raw_observations_checked": raw_rate_count,
                  "questions_with_no_numeric_rates": empty_rate_count, "rate_conflicts": 0,
                  "extrapolated_values": 0, "unestimated_before_only": 47, "unestimated_after_only": 1,
                  "unestimated_no_rates": 3, "summary_lines": 12,
                  "input_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                   for p in [ROOT / "questions.csv", RAW / "cdc-milestones.csv", RAW / "matches.json", RAW / "unmatched-reasons.json"]}}
    (RAW / "comparison-validation.json").write_text(json.dumps(validation, indent=2) + "\n")
    print(json.dumps(stats, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    build()
