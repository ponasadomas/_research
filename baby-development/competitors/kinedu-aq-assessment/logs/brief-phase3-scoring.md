# Phase 3 — Reverse-engineer the scoring of the Kinedu "AQ assessment" report

Context: Phase 2 (read ENUMERATION.md, age-map.md, questions.csv, and the saved raw/api/result_*.json files first) established:
- POST https://webpromo.kinedu.com/api/assessment with {"action":"start","birthdate":"YYYY-MM-DD","gestationalWeeks":null} returns the age-specific question list (sections[].anchor / items[], plus calibration[]). Each item has id, area, skill, title, rate (0..0.98).
- POST {"action":"result","ageMonths":N,"extended":<bool>,"answers":[{"id":<int>,"y":0|1},...]} returns either
  {"stage":"extension","items":[...8 more items...]} or {"stage":"complete","basic":{...},"detail":{...},"skills":[...],"activity":...} or below_floor variants.
- basic/detail expose: state (ok|below_floor), band (e.g. on_pace, little_ahead, well_ahead, ...), devAge, capped, ageMonths, tier, areasLocked, teaserArea, per-area {months, atLeast}. skills expose from,to,total,reached,focus,childPct,curve[{age,pct,lo,hi}].
- Anomaly: age 1, all 39 answers = 0 → band on_pace, devAge 1 (expected below_floor). Repeat identical.
- Use the exact curl headers from ENUMERATION.md. Sleep 0.5 s between calls. Budget: at most ~350 requests. Only call /api/assessment. Never call /api/lead, /api/track, /api/send-reading.
Work only in this folder, no browser. Save every raw response under raw/api/scoring/ with descriptive names, plus a requests manifest (jsonl: timestamp, body, file, http status). Write a reusable script scripts/probe_scoring.py.

Goal: decide, with evidence, whether the report is a real computation from the answers (and roughly which formula) or cosmetic/fake, and fully describe the extension mechanics.

Experiments (pick ages 3, 12, 24, 36 unless stated; reuse the start lists from raw/api/start_age*_gw-null.json — mind the filename-vs-returned-age offset documented in ENUMERATION.md, index by RETURNED age):
A. Determinism: send the same mixed answer vector 3 times at age 12 → identical JSON? Also send it with answers shuffled in order → identical?
B. Monotonicity: at age 12 start with all 0 and flip items to 1 one at a time in ascending `rate` order (cumulative), recording devAge/band/per-area months after each flip. Then do the same in descending rate order. Does devAge move smoothly and monotonically? Which single flips move it most?
C. Rate hypothesis: answer y=1 exactly for items with rate >= 0.5 and 0 otherwise (a "typical" child). Expect devAge ≈ ageMonths and band on_pace if the model is real. Repeat with threshold 0.25 and 0.75. Do this at all four ages.
D. Per-area independence: at age 12, set all Physical items to 1 and everything else 0; then Cognitive only; Language only; Social-Emotional only. Does only that area's `months` move? How is overall devAge derived from the 4 area months (mean? median? min? weighted)? Try to fit a formula against all results collected so far.
E. Extension mechanics: find the minimal condition that triggers stage "extension" (all 1 in one area? N consecutive 1s? top-rate items all 1?). Binary-search over the fraction of 1s at age 12. When extension triggers, answer the extension items (a) all 1, (b) all 0, (c) mixed, each with extended=true — is there a second extension round (stage chain depth)? What does `extended:true` vs `false` change when the vector would otherwise trigger extension? What does `capped:true` mean (devAge ceiling)?
F. Input validation: (1) send answers for IDs NOT in that age's list (take IDs from another age) — accepted, ignored, or error? Does it change devAge? (2) send only a subset (e.g. first 10 answers) — does it complete? (3) send y=2 or y=-1. (4) omit calibration answers. This tells us whether scoring is a per-ID lookup over the whole bank or bound to the served list.
G. The anomaly: reproduce age 1 all-0 → on_pace; also test age 0 and age 2 all-0; test age 1 with all-0 except calibration = 1; find what makes age 1 not below_floor.
H. Skills curves: for one complete report, document what `curve[{age,pct,lo,hi}]` contains (is it the same for every child at that age? does it depend on answers?) and how childPct relates to reached/total. Check if the curve values are consistent with the item `rate`s across ages from the start lists (e.g. does pct at age A equal the mean rate of that skill's items at age A?).
I. Report gating: list which fields are only present with tier detail / areasLocked / teaserArea, i.e. what the free report shows vs what's behind the paywall.

Write SCORING.md: method, tables of results per experiment, the best-fit formula for devAge/band/area months with how well it fits (exact matches / total), the extension rules found, the validation behaviour, the anomaly explanation (or "unexplained"), and a one-paragraph verdict: REAL (answer-driven, consistent model) / PARTLY REAL / COSMETIC, with the strongest 3 pieces of evidence for the verdict. Separate observed from inferred. Do not fabricate. Finish by printing a 15-line summary.
