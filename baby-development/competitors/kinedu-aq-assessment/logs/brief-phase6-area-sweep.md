# Phase 6 — Per-area (topic) scoring table for every age 0–48 (Kinedu AQ assessment)

Read SCORING.md (sections D, "Best-fit scoring model") and scripts/collect_scoring_table.py (Phase 5 collector) first; reuse its
structure. Phase 3 found that each area's reported `months` depends on the Yes count inside that area; Phase 5 (finished, see
scoring-table.csv / SCORING-TABLE.md if present) measured the headline K→devAge for all ages. Goal now: the per-area table.

NETWORK RULE (mandatory): every HTTP request MUST go through `scripts/proxy_curl.sh` (a curl wrapper that routes via a SOCKS5
proxy; it takes normal curl arguments). Never call curl directly, never print or read the proxy credentials. First call:
`scripts/proxy_curl.sh -s https://ipinfo.io/json` and confirm the country is NOT "LT"; abort if it is. Use the same headers
as ENUMERATION.md. Sleep 2.0 s before every request. Sequential. Never call any endpoint other than /api/assessment.

Design:
- For each returned age A in 0..48, take the served list (raw/api/start_age*_gw-null.json indexed by RETURNED ageMonths).
  Group every served item (anchor, items, calibration) by the item's own `area` field (not the section it is displayed under).
- Baseline for each area = Yes to the first round(sum of that area's rates) items in ascending-rate order, the rest No
  (an "on pace" child). 
- For each target area T: keep the other three areas at baseline; set T's Yes count K_T = 0..n_T (cumulative, ascending rate).
  POST {"action":"result","ageMonths":A,"extended":true,"answers":[...]}. ~2,100 calls total.
- Save raw under raw/api/area-sweep/result_age{AA}_{area}_k{KK}.json(.headers.txt) + requests.jsonl manifest (timestamp, age,
  area, K, http, file, sha256). Resumable: skip existing files. Abort after 3 consecutive 429/403/5xx/transport failures and
  say BLOCKED in the summary with status codes.
- Order check: at ages 3, 12, 30 repeat the target-area sweep in DESCENDING rate order for one area each and report whether the
  area months match the ascending run at equal K (does only the count matter inside an area?).
- Scripts: scripts/collect_area_table.py (collector, uses subprocess to call scripts/proxy_curl.sh) and scripts/build_area_table.py.

Outputs:
1. area-table.csv: age, area, n_area, K, http, state, headline devAge, area_state, area_months, atLeast, file.
2. AREA-TABLE.md: per age, one compact table per area: K range → months / atLeast / state (collapse identical consecutive rows);
   a summary: for each age+area, n, sum of rates (expected Yes), the K where months first equals A, the min K with a numeric
   months, the K where atLeast first true; list every (age, area) where months is NOT non-decreasing in K (the glitch), with the
   exact K values; the order-check result; and a plain-words recipe "how to compute an area's months from its Yes count".
   Observed vs inferred, no fabrication. 12-line summary, first line COMPLETED or BLOCKED with request counts.
