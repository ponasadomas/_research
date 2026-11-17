# Phase 5 — Full Yes-count → reported-age table for every age 0–48 (Kinedu AQ assessment)

Read ENUMERATION.md, SCORING.md (sections "Best-fit scoring model" and "Band formula") and scripts/probe_scoring.py first.
Phase 3 established: for a fixed served question set, the headline result (state, devAge, band, capped) depends only on
K = number of Yes answers, not on which ones. We measured the full K → result lookup for age 12 only. Goal now: measure it for
ALL 49 ages so the test can be rebuilt.

Method:
- For each returned age A in 0..48, take its served list from raw/api/start_age*_gw-null.json (index by the RETURNED ageMonths,
  not the filename; see ENUMERATION.md). Flatten anchor → items → calibration = N ids (22..39).
- Order the ids by ascending rate (tie: id). For K = 0..N, answer the first K ids y=1, the rest y=0 (cumulative).
- POST {"action":"result","ageMonths":A,"extended":true,"answers":[...]} with the exact curl headers from ENUMERATION.md.
  extended:true so saturated vectors return a complete (capped) report instead of stage "extension".
- PACE: sleep 2.0 seconds before every request (not 0.5). Sequential. ~1,890 calls, ~65 minutes. Never call any other endpoint.
- Save every raw response + headers under raw/api/scoring-all/result_age{AA}_k{KK}.json(.headers.txt) and a manifest
  raw/api/scoring-all/requests.jsonl (timestamp, age, K, http status, file, sha256). Skip (do not overwrite) files that already exist,
  so the run is resumable.
- ABORT RULE: if 3 consecutive responses are HTTP 429, 403, 5xx, or a transport failure, stop immediately, write what you have,
  and say clearly in the summary that we appear blocked (status codes + timestamps). Do not retry aggressively.
- Write scripts/collect_scoring_table.py (collector, resumable) and scripts/build_scoring_table.py (offline builder).

Outputs:
1. scoring-table.csv: age, N, K, http, stage, state, devAge, band, capped, months_Physical, months_Cognitive, months_Language,
   months_SocialEmotional (empty where not returned), atLeast flags, file.
2. SCORING-TABLE.md: 
   - one compact table per age: K range → devAge / band / capped (collapse consecutive K with identical headline into one row).
   - a summary table: age, N, sum of served rates (expected Yes count), the K at which devAge first equals A, min K that is not
     below_floor, the K at which capped first becomes true, the capped devAge. Check and state: does round(sum of rates) → devAge == A
     hold for every age? List any exceptions.
   - the band formula check (r = devAge/max(A,1): >1.15 well_ahead, >1.05 little_ahead, >=0.95 on_pace, else building) over all
     new numeric reports: matches/total, list mismatches.
   - any age where devAge is not non-decreasing in K (list them).
   - a short "how to rebuild the headline score" recipe in plain words, using only the served lists + this table.
   Observed vs inferred, no fabrication. Finish with a 12-line summary (first line: BLOCKED or COMPLETED, with request counts).
