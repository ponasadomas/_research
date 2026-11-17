# Phase 2 — Enumerate the question bank of the Kinedu "AQ assessment" via its API

Context: https://webpromo.kinedu.com/aq-assessment is a Next.js quiz. The browser POSTs JSON to
https://webpromo.kinedu.com/api/assessment with body {"action":"start","birthdate":<string>,"gestationalWeeks":<number|null>}
and gets back {ageMonths, corrected, sections, calibration, ...}. Ages above some limit return HTTP 422 with {"error":"age_range","ageMonths":...}.
The birthdate format is not yet known — look at raw/js/page-5f182d70f1f24a3d.js (search for `birthdate` and the date input) to find it (likely "YYYY-MM-DD").
Work only inside this folder. Do NOT open a browser. Use curl (or python3 urllib) from the shell.
Send a realistic User-Agent and `Content-Type: application/json`, Origin/Referer https://webpromo.kinedu.com. Sleep 0.5s between calls. Today is 2026-11-02.

Goal: the complete question bank and the mapping from baby age to questions, so we can tell whether this is one tree or many.

Steps:
1. Confirm the request works with one call (birthdate = 6 months ago, gestationalWeeks=null). Save the raw response to raw/api/start_age06_gw-null.json. If it fails, inspect the JS for the exact field names/format and fix. Save any failing response too.
2. For every age from 0 to the 422 boundary (compute birthdate = today minus N months, use the 15th of the month to avoid rounding issues), call start with gestationalWeeks=null. Save each as raw/api/start_age{NN}_gw-null.json. Stop after 3 consecutive 422s past the boundary; record the boundary.
3. Repeat for a sample of ages (0,1,2,3,4,6,9,12,18,24) with gestationalWeeks = 28, 32, 36 (and 37 as control). Save as raw/api/start_age{NN}_gw{WW}.json. Document how `corrected` and ageMonths change, i.e. the correction formula, and up to what age correction is applied.
4. Also call once with lang variations if the API accepts a language field (check JS first; if the API has no lang field, note that text is localised client-side and skip).
5. Build questions.csv with columns: question_id, section_id, section_title, kind (anchor|item|calibration), text, age_months_min, age_months_max (the range of ages for which this id was returned), any other per-item fields the API returns (keep all raw fields as extra columns). One row per unique question id.
6. Build age-map.md: a table age_month → ordered list of question ids (sections + calibration), plus a count. Then state plainly: how many DISTINCT question sets exist (group identical ordered lists), which age ranges share a set, and whether the sets overlap (sliding window) or are disjoint buckets.
7. Write ENUMERATION.md: method, the exact curl used, boundary, correction formula, number of unique questions, number of distinct sets, a mermaid diagram of age → set, and anything unexpected in the responses (extra fields, flags like difficulty/weight/skill/domain that hint at scoring).
Do not fabricate: if a call fails, say so. Finish by printing a 15-line summary.
