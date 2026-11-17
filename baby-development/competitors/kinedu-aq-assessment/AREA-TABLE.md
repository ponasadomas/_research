COMPLETED: 2064/2064 assessment requests; 2064/2064 complete reports.

# Kinedu AQ: per-area Yes-count tables (Phase 6)

## 12-line summary

```text
COMPLETED: 2064/2064 assessment requests; 2064/2064 complete reports.
Coverage: 49/49 complete ages; 196/196 complete age-area sweeps.
HTTP: 200=2064; transport failures=0.
Proxy: NL; 1 country check(s); wrapper only; sequential; 2.0s sleep.
Ascending rows: 2033 planned; 1665 numeric area months; 243 below_floor; 125 area not_enough.
Baselines: per-item area grouping; exact decimal rate sums; nearest-integer rounding with .5 ties to even.
Glitches: 33 age-area groups with 36 observed decreases; exact K values in AREA-TABLE.md.
Descending order checks: 24/24 numeric-month pairs match; 24/24 exposed area records match.
Repeated area/count checks: 5462 comparisons; 0 conflicts.
Abort streak: 0; HTTP codes=[]; curl codes=[].
Outputs: area-table.csv, AREA-TABLE.md, raw/api/area-sweep/requests.jsonl, logs/phase6-validation.json.
Recipe: choose returned age and its served area IDs, count Yes, then look up K; hidden or unmeasured months stay unknown.
```

## Method and evidence

**Observed** values come only from the linked saved API responses. **Inferred** describes an explanatory model, not recovered server code. Blank CSV cells and — here mean the API omitted the field or the request has not been collected; zero is a numeric observed month value. No missing value is filled from Phase 3, Phase 5, a neighboring K, or a norm hypothesis.

The [collector](scripts/collect_area_table.py) reuses Phase 5's returned-age indexing and flattens every section anchor, section item and calibration item. It groups by each **item's own `area`**, including calibration displayed under another domain. For each age and area, sort by ascending `(rate,id)` and set the first `round(sum(rates))` IDs to Yes. Rounding uses exact decimal saved rates and nearest integer with .5 ties to even. This defines the requested expected-count baseline; it is not a claim that every baseline produces on_pace or months=A.

Sweep one target area's K from 0 through its item count, retaining the other three areas at their individual baselines. Every request supplies every served ID exactly once, numeric y=0/1, `action:result`, the returned age, and `extended:true`. The answer-array order stays fixed. Descending controls reverse the target-area `(rate,id)` ranking for ages 3/Physical, 12/Cognitive and 30/Language, keeping all other answers identical.

All HTTP calls use [scripts/proxy_curl.sh](scripts/proxy_curl.sh). The first call was the required ipinfo country check; collection aborts for LT or an unverifiable country. Assessment calls use only POST `/api/assessment`, with exactly the User-Agent, Content-Type, Origin and Referer in [ENUMERATION.md](ENUMERATION.md). Requests are sequential with a 2.0-second sleep before every request, including preflight. No proxy credentials are read or included in this report.

Assessment HTTP counts: **{200: 2064}**; transport failures: **0**. There were **1** additional proxy-country check requests. Minimum measured response-completion to next request-start gap: **2.00209 seconds**. Verified response/header/source hashes and HTTP header statuses: **2064 requests**. Proxy countries recorded for these requests: **['NL']**.

Raw bodies and `.json.headers.txt` files are immutable under [raw/api/area-sweep/](raw/api/area-sweep/); descending controls are in its `order-check/` subdirectory. The [manifest](raw/api/area-sweep/requests.jsonl) records UTC timestamps, age, area, K, HTTP status, request body, source and response SHA-256s, proxy-check evidence and curl exit status. Existing manifested files are verified and skipped. Unmanifested files stop collection for offline reconciliation. Three consecutive 429/403/5xx/transport failures stop collection and prevent restart requests. The [builder](scripts/build_area_table.py) is entirely offline; [validation JSON](logs/phase6-validation.json) records its checks. Rebuild with `python3 scripts/build_area_table.py`.

## Summary by age and area

First-K columns mean the first **exposed** match, numeric month, or true atLeast in this exact sweep. `none exposed` means every K was measured but no such value was returned; `unknown` means an earlier missing/error response prevents identifying the first K. A below_floor report exposes no area months, so it cannot establish a latent area age. Odd A may have no equality on the observed two-month grid.

**19 complete age-area sweeps expose no numeric months at any K:** age 0 / Language (n=7); age 1 / Language (n=7); age 39 / Language (n=7); age 40 / Language (n=7); age 41 / Language (n=7); age 45 / Physical (n=7); age 45 / Cognitive (n=7); age 46 / Physical (n=7); age 46 / Cognitive (n=6); age 46 / Language (n=7); age 46 / Social-Emotional (n=7); age 47 / Physical (n=7); age 47 / Cognitive (n=4); age 47 / Language (n=6); age 47 / Social-Emotional (n=7); age 48 / Physical (n=6); age 48 / Cognitive (n=3); age 48 / Language (n=6); age 48 / Social-Emotional (n=7). Their returned states remain in the tables; no numeric ages are substituted.

| Age A | Area | n | Σ rates (expected Yes) | Baseline K | First K: months=A | Min K: numeric months | First K: atLeast | Reports |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Physical | 12 | 7.32 | 7 | none exposed | 9 | 12 | 13/13 |
| 0 | Cognitive | 11 | 5.48 | 5 | none exposed | 7 | 10 | 12/12 |
| 0 | Language | 7 | 3.01 | 3 | none exposed | none exposed | none exposed | 8/8 |
| 0 | Social-Emotional | 9 | 4.89 | 5 | none exposed | 7 | 9 | 10/10 |
| 1 | Physical | 13 | 6.32 | 6 | none exposed | 0 | 12 | 14/14 |
| 1 | Cognitive | 10 | 4.83 | 5 | none exposed | 0 | 10 | 11/11 |
| 1 | Language | 7 | 3.03 | 3 | none exposed | none exposed | none exposed | 8/8 |
| 1 | Social-Emotional | 9 | 5.52 | 6 | none exposed | 0 | 9 | 10/10 |
| 2 | Physical | 10 | 5.74 | 6 | none exposed | 6 | 10 | 11/11 |
| 2 | Cognitive | 10 | 5.09 | 5 | 5 | 5 | 10 | 11/11 |
| 2 | Language | 8 | 3.80 | 4 | 4 | 4 | 8 | 9/9 |
| 2 | Social-Emotional | 11 | 4.47 | 4 | 5 | 4 | 10 | 12/12 |
| 3 | Physical | 10 | 5.52 | 6 | none exposed | 5 | 9 | 11/11 |
| 3 | Cognitive | 11 | 5.31 | 5 | none exposed | 4 | 11 | 12/12 |
| 3 | Language | 9 | 4.48 | 4 | none exposed | 3 | 8 | 10/10 |
| 3 | Social-Emotional | 9 | 4.60 | 5 | none exposed | 4 | 9 | 10/10 |
| 4 | Physical | 9 | 5.51 | 6 | 5 | 4 | 9 | 10/10 |
| 4 | Cognitive | 9 | 4.85 | 5 | 3 | 3 | 9 | 10/10 |
| 4 | Language | 10 | 4.45 | 4 | 4 | 2 | 9 | 11/11 |
| 4 | Social-Emotional | 11 | 5.94 | 6 | 5 | 4 | 10 | 12/12 |
| 5 | Physical | 9 | 5.14 | 5 | none exposed | 2 | 9 | 10/10 |
| 5 | Cognitive | 12 | 6.14 | 6 | none exposed | 3 | 11 | 13/13 |
| 5 | Language | 9 | 4.68 | 5 | none exposed | 2 | 8 | 10/10 |
| 5 | Social-Emotional | 9 | 5.57 | 6 | none exposed | 3 | 9 | 10/10 |
| 6 | Physical | 9 | 5.01 | 5 | 5 | 4 | 9 | 10/10 |
| 6 | Cognitive | 11 | 6.18 | 6 | 6 | 5 | 10 | 12/12 |
| 6 | Language | 10 | 5.35 | 5 | none exposed | 4 | 9 | 11/11 |
| 6 | Social-Emotional | 9 | 6.20 | 6 | 6 | 5 | 9 | 10/10 |
| 7 | Physical | 9 | 5.13 | 5 | none exposed | 1 | 9 | 10/10 |
| 7 | Cognitive | 11 | 5.59 | 6 | none exposed | 2 | 10 | 12/12 |
| 7 | Language | 10 | 5.13 | 5 | none exposed | 1 | 9 | 11/11 |
| 7 | Social-Emotional | 9 | 5.91 | 6 | none exposed | 2 | 9 | 10/10 |
| 8 | Physical | 10 | 5.14 | 5 | 5 | 0 | 9 | 11/11 |
| 8 | Cognitive | 10 | 5.49 | 5 | 5 | 0 | 9 | 11/11 |
| 8 | Language | 10 | 5.63 | 6 | 5 | 1 | 9 | 11/11 |
| 8 | Social-Emotional | 9 | 6.17 | 6 | 5 | 1 | 9 | 10/10 |
| 9 | Physical | 11 | 4.98 | 5 | none exposed | 1 | 10 | 12/12 |
| 9 | Cognitive | 10 | 6.26 | 6 | none exposed | 2 | 9 | 11/11 |
| 9 | Language | 9 | 5.32 | 5 | none exposed | 1 | 8 | 10/10 |
| 9 | Social-Emotional | 9 | 4.82 | 5 | none exposed | 1 | 8 | 10/10 |
| 10 | Physical | 9 | 4.98 | 5 | 5 | 1 | 9 | 10/10 |
| 10 | Cognitive | 9 | 4.46 | 4 | 4 | 0 | 9 | 10/10 |
| 10 | Language | 12 | 6.09 | 6 | 6 | 2 | 10 | 13/13 |
| 10 | Social-Emotional | 9 | 5.20 | 5 | 5 | 1 | 8 | 10/10 |
| 11 | Physical | 9 | 4.82 | 5 | none exposed | 0 | 9 | 10/10 |
| 11 | Cognitive | 9 | 4.46 | 4 | none exposed | 0 | 8 | 10/10 |
| 11 | Language | 10 | 5.99 | 6 | none exposed | 1 | 9 | 11/11 |
| 11 | Social-Emotional | 11 | 5.64 | 6 | none exposed | 1 | 10 | 12/12 |
| 12 | Physical | 9 | 5.04 | 5 | 4 | 0 | 9 | 10/10 |
| 12 | Cognitive | 9 | 5.16 | 5 | 4 | 0 | 8 | 10/10 |
| 12 | Language | 10 | 5.72 | 6 | 6 | 1 | 9 | 11/11 |
| 12 | Social-Emotional | 11 | 6.49 | 6 | 6 | 1 | 10 | 12/12 |
| 13 | Physical | 11 | 5.45 | 5 | none exposed | 1 | 10 | 12/12 |
| 13 | Cognitive | 9 | 4.39 | 4 | none exposed | 0 | 8 | 10/10 |
| 13 | Language | 10 | 5.02 | 5 | none exposed | 1 | 9 | 11/11 |
| 13 | Social-Emotional | 9 | 5.64 | 6 | none exposed | 2 | 8 | 10/10 |
| 14 | Physical | 10 | 5.46 | 5 | none exposed | 0 | 9 | 11/11 |
| 14 | Cognitive | 10 | 4.77 | 5 | 5 | 0 | 9 | 11/11 |
| 14 | Language | 10 | 5.31 | 5 | 5 | 0 | 9 | 11/11 |
| 14 | Social-Emotional | 9 | 6.21 | 6 | 6 | 1 | 8 | 10/10 |
| 15 | Physical | 9 | 5.26 | 5 | none exposed | 0 | 8 | 10/10 |
| 15 | Cognitive | 10 | 5.03 | 5 | none exposed | 0 | 9 | 11/11 |
| 15 | Language | 9 | 5.83 | 6 | none exposed | 0 | 8 | 10/10 |
| 15 | Social-Emotional | 11 | 6.26 | 6 | none exposed | 0 | 10 | 12/12 |
| 16 | Physical | 11 | 5.28 | 5 | 5 | 0 | 9 | 12/12 |
| 16 | Cognitive | 10 | 5.06 | 5 | 4 | 0 | 9 | 11/11 |
| 16 | Language | 9 | 5.87 | 6 | 6 | 0 | 8 | 10/10 |
| 16 | Social-Emotional | 9 | 5.80 | 6 | 5 | 0 | 8 | 10/10 |
| 17 | Physical | 12 | 5.66 | 6 | none exposed | 0 | 10 | 13/13 |
| 17 | Cognitive | 9 | 5.08 | 5 | none exposed | 0 | 8 | 10/10 |
| 17 | Language | 9 | 4.95 | 5 | none exposed | 0 | 8 | 10/10 |
| 17 | Social-Emotional | 9 | 6.41 | 6 | none exposed | 0 | 8 | 10/10 |
| 18 | Physical | 10 | 5.66 | 6 | 6 | 0 | 8 | 11/11 |
| 18 | Cognitive | 10 | 6.04 | 6 | 6 | 0 | 8 | 11/11 |
| 18 | Language | 10 | 5.69 | 6 | none exposed | 0 | 8 | 11/11 |
| 18 | Social-Emotional | 9 | 6.74 | 7 | none exposed | 0 | 8 | 10/10 |
| 19 | Physical | 9 | 5.90 | 6 | none exposed | 0 | 8 | 10/10 |
| 19 | Cognitive | 10 | 6.10 | 6 | none exposed | 0 | 8 | 11/11 |
| 19 | Language | 10 | 5.00 | 5 | none exposed | 0 | 8 | 11/11 |
| 19 | Social-Emotional | 10 | 6.30 | 6 | none exposed | 0 | 8 | 11/11 |
| 20 | Physical | 10 | 5.15 | 5 | 5 | 0 | 9 | 11/11 |
| 20 | Cognitive | 9 | 5.60 | 6 | 5 | 0 | 8 | 10/10 |
| 20 | Language | 10 | 5.21 | 5 | 5 | 0 | 8 | 11/11 |
| 20 | Social-Emotional | 10 | 6.01 | 6 | 6 | 0 | 9 | 11/11 |
| 21 | Physical | 11 | 5.34 | 5 | none exposed | 0 | 9 | 12/12 |
| 21 | Cognitive | 9 | 5.10 | 5 | none exposed | 0 | 8 | 10/10 |
| 21 | Language | 9 | 4.74 | 5 | none exposed | 0 | 7 | 10/10 |
| 21 | Social-Emotional | 10 | 5.90 | 6 | none exposed | 0 | 9 | 11/11 |
| 22 | Physical | 12 | 5.63 | 6 | none exposed | 0 | 10 | 13/13 |
| 22 | Cognitive | 9 | 5.49 | 5 | none exposed | 0 | 8 | 10/10 |
| 22 | Language | 9 | 4.99 | 5 | 5 | 0 | 7 | 10/10 |
| 22 | Social-Emotional | 9 | 5.58 | 6 | none exposed | 0 | 8 | 10/10 |
| 23 | Physical | 12 | 5.65 | 6 | none exposed | 0 | 10 | 13/13 |
| 23 | Cognitive | 9 | 5.10 | 5 | none exposed | 0 | 8 | 10/10 |
| 23 | Language | 9 | 4.96 | 5 | none exposed | 0 | 7 | 10/10 |
| 23 | Social-Emotional | 9 | 5.86 | 6 | none exposed | 0 | 8 | 10/10 |
| 24 | Physical | 12 | 5.75 | 6 | 6 | 0 | 10 | 13/13 |
| 24 | Cognitive | 9 | 5.19 | 5 | 5 | 0 | 8 | 10/10 |
| 24 | Language | 9 | 4.90 | 5 | 5 | 0 | 7 | 10/10 |
| 24 | Social-Emotional | 9 | 5.96 | 6 | 6 | 0 | 8 | 10/10 |
| 25 | Physical | 10 | 5.61 | 6 | none exposed | 2 | 8 | 11/11 |
| 25 | Cognitive | 9 | 5.08 | 5 | none exposed | 1 | 8 | 10/10 |
| 25 | Language | 10 | 5.36 | 5 | none exposed | 1 | 7 | 11/11 |
| 25 | Social-Emotional | 10 | 6.24 | 6 | none exposed | 2 | 9 | 11/11 |
| 26 | Physical | 9 | 5.15 | 5 | none exposed | 1 | 8 | 10/10 |
| 26 | Cognitive | 9 | 4.59 | 5 | none exposed | 1 | 8 | 10/10 |
| 26 | Language | 10 | 5.43 | 5 | none exposed | 1 | 7 | 11/11 |
| 26 | Social-Emotional | 11 | 6.73 | 7 | none exposed | 3 | 9 | 12/12 |
| 27 | Physical | 11 | 5.36 | 5 | none exposed | 1 | 9 | 12/12 |
| 27 | Cognitive | 10 | 5.17 | 5 | none exposed | 1 | 8 | 11/11 |
| 27 | Language | 9 | 5.35 | 5 | none exposed | 1 | 6 | 10/10 |
| 27 | Social-Emotional | 9 | 6.48 | 6 | none exposed | 2 | 8 | 10/10 |
| 28 | Physical | 10 | 5.51 | 6 | 5 | 2 | 8 | 11/11 |
| 28 | Cognitive | 10 | 5.00 | 5 | 5 | 1 | 8 | 11/11 |
| 28 | Language | 10 | 5.43 | 5 | none exposed | 1 | 7 | 11/11 |
| 28 | Social-Emotional | 9 | 6.43 | 6 | none exposed | 2 | 8 | 10/10 |
| 29 | Physical | 11 | 5.54 | 6 | none exposed | 1 | 9 | 12/12 |
| 29 | Cognitive | 9 | 5.17 | 5 | none exposed | 0 | 8 | 10/10 |
| 29 | Language | 9 | 5.51 | 6 | none exposed | 1 | 6 | 10/10 |
| 29 | Social-Emotional | 10 | 6.72 | 7 | none exposed | 2 | 9 | 11/11 |
| 30 | Physical | 10 | 5.99 | 6 | 6 | 2 | 8 | 11/11 |
| 30 | Cognitive | 10 | 5.32 | 5 | none exposed | 1 | 8 | 11/11 |
| 30 | Language | 9 | 5.87 | 6 | none exposed | 2 | 7 | 10/10 |
| 30 | Social-Emotional | 10 | 6.89 | 7 | none exposed | 3 | 9 | 11/11 |
| 31 | Physical | 10 | 5.08 | 5 | none exposed | 1 | 8 | 11/11 |
| 31 | Cognitive | 9 | 4.93 | 5 | none exposed | 1 | 7 | 10/10 |
| 31 | Language | 10 | 6.08 | 6 | none exposed | 2 | 7 | 11/11 |
| 31 | Social-Emotional | 10 | 6.47 | 6 | none exposed | 2 | 9 | 11/11 |
| 32 | Physical | 9 | 5.25 | 5 | 5 | 1 | 7 | 10/10 |
| 32 | Cognitive | 10 | 5.27 | 5 | 5 | 1 | 8 | 11/11 |
| 32 | Language | 11 | 6.87 | 7 | none exposed | 3 | 8 | 12/12 |
| 32 | Social-Emotional | 9 | 5.34 | 5 | 5 | 1 | 8 | 10/10 |
| 33 | Physical | 9 | 5.36 | 5 | none exposed | 0 | 7 | 10/10 |
| 33 | Cognitive | 9 | 4.92 | 5 | none exposed | 0 | 7 | 10/10 |
| 33 | Language | 11 | 6.86 | 7 | none exposed | 2 | 8 | 12/12 |
| 33 | Social-Emotional | 10 | 5.93 | 6 | none exposed | 1 | 9 | 11/11 |
| 34 | Physical | 9 | 5.57 | 6 | none exposed | 0 | 7 | 10/10 |
| 34 | Cognitive | 9 | 5.27 | 5 | none exposed | 0 | 7 | 10/10 |
| 34 | Language | 11 | 6.75 | 7 | none exposed | 1 | 9 | 12/12 |
| 34 | Social-Emotional | 10 | 6.26 | 6 | none exposed | 0 | 9 | 11/11 |
| 35 | Physical | 9 | 5.25 | 5 | none exposed | 1 | 7 | 10/10 |
| 35 | Cognitive | 9 | 5.47 | 5 | none exposed | 1 | 7 | 10/10 |
| 35 | Language | 11 | 6.95 | 7 | none exposed | 3 | 8 | 12/12 |
| 35 | Social-Emotional | 10 | 6.41 | 6 | none exposed | 2 | 9 | 11/11 |
| 36 | Physical | 9 | 5.10 | 5 | 5 | 1 | 7 | 10/10 |
| 36 | Cognitive | 9 | 5.43 | 5 | 6 | 1 | 7 | 10/10 |
| 36 | Language | 11 | 6.87 | 7 | none exposed | 3 | 9 | 12/12 |
| 36 | Social-Emotional | 10 | 6.52 | 7 | 7 | 3 | 9 | 11/11 |
| 37 | Physical | 9 | 5.10 | 5 | none exposed | 0 | 7 | 10/10 |
| 37 | Cognitive | 9 | 5.95 | 6 | none exposed | 1 | 7 | 10/10 |
| 37 | Language | 9 | 6.42 | 6 | none exposed | 1 | 7 | 10/10 |
| 37 | Social-Emotional | 9 | 6.51 | 7 | none exposed | 2 | 8 | 10/10 |
| 38 | Physical | 9 | 5.13 | 5 | 5 | 1 | 7 | 10/10 |
| 38 | Cognitive | 9 | 6.30 | 6 | none exposed | 2 | 7 | 10/10 |
| 38 | Language | 9 | 5.97 | 6 | 6 | 2 | 7 | 10/10 |
| 38 | Social-Emotional | 9 | 6.42 | 6 | none exposed | 2 | 8 | 10/10 |
| 39 | Physical | 11 | 6.87 | 7 | none exposed | 3 | 8 | 12/12 |
| 39 | Cognitive | 9 | 6.44 | 6 | none exposed | 2 | 7 | 10/10 |
| 39 | Language | 7 | 4.68 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 39 | Social-Emotional | 9 | 6.31 | 6 | none exposed | 2 | 7 | 10/10 |
| 40 | Physical | 11 | 7.11 | 7 | 7 | 1 | 8 | 12/12 |
| 40 | Cognitive | 9 | 6.69 | 7 | 7 | 1 | 7 | 10/10 |
| 40 | Language | 7 | 5.00 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 40 | Social-Emotional | 9 | 6.48 | 6 | none exposed | 0 | 7 | 10/10 |
| 41 | Physical | 11 | 7.29 | 7 | none exposed | 2 | 8 | 12/12 |
| 41 | Cognitive | 9 | 6.72 | 7 | none exposed | 2 | 7 | 10/10 |
| 41 | Language | 7 | 5.17 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 41 | Social-Emotional | 9 | 6.62 | 7 | none exposed | 2 | 7 | 10/10 |
| 42 | Physical | 9 | 5.65 | 6 | none exposed | 0 | 7 | 10/10 |
| 42 | Cognitive | 9 | 6.18 | 6 | 6 | 0 | 7 | 10/10 |
| 42 | Language | 9 | 5.78 | 6 | none exposed | 0 | 7 | 10/10 |
| 42 | Social-Emotional | 9 | 5.47 | 5 | none exposed | 0 | 7 | 10/10 |
| 43 | Physical | 9 | 6.11 | 6 | none exposed | 0 | 7 | 10/10 |
| 43 | Cognitive | 9 | 6.14 | 6 | none exposed | 0 | 7 | 10/10 |
| 43 | Language | 9 | 5.90 | 6 | none exposed | 0 | 7 | 10/10 |
| 43 | Social-Emotional | 9 | 5.70 | 6 | none exposed | 0 | 7 | 10/10 |
| 44 | Physical | 9 | 5.87 | 6 | 6 | 1 | 7 | 10/10 |
| 44 | Cognitive | 9 | 6.19 | 6 | 7 | 1 | 7 | 10/10 |
| 44 | Language | 9 | 6.16 | 6 | 6 | 1 | 7 | 10/10 |
| 44 | Social-Emotional | 9 | 5.83 | 6 | 6 | 1 | 7 | 10/10 |
| 45 | Physical | 7 | 4.55 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 45 | Cognitive | 7 | 4.76 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 45 | Language | 8 | 5.44 | 5 | none exposed | 0 | 6 | 9/9 |
| 45 | Social-Emotional | 11 | 7.71 | 8 | none exposed | 3 | 9 | 12/12 |
| 46 | Physical | 7 | 4.72 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 46 | Cognitive | 6 | 4.03 | 4 | none exposed | none exposed | none exposed | 7/7 |
| 46 | Language | 7 | 4.82 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 46 | Social-Emotional | 7 | 4.53 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 47 | Physical | 7 | 4.76 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 47 | Cognitive | 4 | 2.68 | 3 | none exposed | none exposed | none exposed | 5/5 |
| 47 | Language | 6 | 4.24 | 4 | none exposed | none exposed | none exposed | 7/7 |
| 47 | Social-Emotional | 7 | 4.67 | 5 | none exposed | none exposed | none exposed | 8/8 |
| 48 | Physical | 6 | 4.15 | 4 | none exposed | none exposed | none exposed | 7/7 |
| 48 | Cognitive | 3 | 1.97 | 2 | none exposed | none exposed | none exposed | 4/4 |
| 48 | Language | 6 | 4.13 | 4 | none exposed | none exposed | none exposed | 7/7 |
| 48 | Social-Emotional | 7 | 4.66 | 5 | none exposed | none exposed | none exposed | 8/8 |

## Nonmonotonic area months (the glitch)

Observed **36 decreases across 33 age-area pairs**. The table lists every decrease between successive exposed numeric observations in increasing K, with exact K and months. Omitted/uncollected months are not assigned a number; a K gap is visible in the listed endpoints. This is an observed scoring defect, not an inferred norm curve.

| Age | Area | K before → after | Months before → after | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Physical | 6 → 8 | 2 → 0 | [before](raw/api/area-sweep/result_age01_Physical_k06.json) / [after](raw/api/area-sweep/result_age01_Physical_k08.json) |
| 3 | Physical | 5 → 6 | 2 → 0 | [before](raw/api/area-sweep/result_age03_Physical_k05.json) / [after](raw/api/area-sweep/result_age03_Physical_k06.json) |
| 4 | Language | 8 → 9 | 16 → 12 | [before](raw/api/area-sweep/result_age04_Language_k08.json) / [after](raw/api/area-sweep/result_age04_Language_k09.json) |
| 5 | Physical | 3 → 4 | 4 → 0 | [before](raw/api/area-sweep/result_age05_Physical_k03.json) / [after](raw/api/area-sweep/result_age05_Physical_k04.json) |
| 5 | Social-Emotional | 3 → 4 | 4 → 0 | [before](raw/api/area-sweep/result_age05_Social-Emotional_k03.json) / [after](raw/api/area-sweep/result_age05_Social-Emotional_k04.json) |
| 7 | Physical | 2 → 3 | 4 → 0 | [before](raw/api/area-sweep/result_age07_Physical_k02.json) / [after](raw/api/area-sweep/result_age07_Physical_k03.json) |
| 7 | Cognitive | 3 → 4 | 4 → 2 | [before](raw/api/area-sweep/result_age07_Cognitive_k03.json) / [after](raw/api/area-sweep/result_age07_Cognitive_k04.json) |
| 8 | Physical | 3 → 4 | 6 → 0 | [before](raw/api/area-sweep/result_age08_Physical_k03.json) / [after](raw/api/area-sweep/result_age08_Physical_k04.json) |
| 9 | Physical | 2 → 3 | 6 → 0 | [before](raw/api/area-sweep/result_age09_Physical_k02.json) / [after](raw/api/area-sweep/result_age09_Physical_k03.json) |
| 11 | Social-Emotional | 2 → 3 | 6 → 0 | [before](raw/api/area-sweep/result_age11_Social-Emotional_k02.json) / [after](raw/api/area-sweep/result_age11_Social-Emotional_k03.json) |
| 12 | Cognitive | 1 → 2 | 8 → 2 | [before](raw/api/area-sweep/result_age12_Cognitive_k01.json) / [after](raw/api/area-sweep/result_age12_Cognitive_k02.json) |
| 12 | Cognitive | 2 → 3 | 2 → 0 | [before](raw/api/area-sweep/result_age12_Cognitive_k02.json) / [after](raw/api/area-sweep/result_age12_Cognitive_k03.json) |
| 12 | Social-Emotional | 2 → 3 | 6 → 0 | [before](raw/api/area-sweep/result_age12_Social-Emotional_k02.json) / [after](raw/api/area-sweep/result_age12_Social-Emotional_k03.json) |
| 13 | Language | 1 → 2 | 8 → 0 | [before](raw/api/area-sweep/result_age13_Language_k01.json) / [after](raw/api/area-sweep/result_age13_Language_k02.json) |
| 14 | Social-Emotional | 1 → 2 | 8 → 0 | [before](raw/api/area-sweep/result_age14_Social-Emotional_k01.json) / [after](raw/api/area-sweep/result_age14_Social-Emotional_k02.json) |
| 15 | Cognitive | 1 → 2 | 8 → 0 | [before](raw/api/area-sweep/result_age15_Cognitive_k01.json) / [after](raw/api/area-sweep/result_age15_Cognitive_k02.json) |
| 15 | Social-Emotional | 1 → 2 | 8 → 2 | [before](raw/api/area-sweep/result_age15_Social-Emotional_k01.json) / [after](raw/api/area-sweep/result_age15_Social-Emotional_k02.json) |
| 16 | Physical | 1 → 2 | 8 → 2 | [before](raw/api/area-sweep/result_age16_Physical_k01.json) / [after](raw/api/area-sweep/result_age16_Physical_k02.json) |
| 16 | Physical | 2 → 3 | 2 → 0 | [before](raw/api/area-sweep/result_age16_Physical_k02.json) / [after](raw/api/area-sweep/result_age16_Physical_k03.json) |
| 16 | Social-Emotional | 1 → 2 | 8 → 2 | [before](raw/api/area-sweep/result_age16_Social-Emotional_k01.json) / [after](raw/api/area-sweep/result_age16_Social-Emotional_k02.json) |
| 17 | Cognitive | 0 → 1 | 10 → 2 | [before](raw/api/area-sweep/result_age17_Cognitive_k00.json) / [after](raw/api/area-sweep/result_age17_Cognitive_k01.json) |
| 17 | Language | 2 → 3 | 8 → 0 | [before](raw/api/area-sweep/result_age17_Language_k02.json) / [after](raw/api/area-sweep/result_age17_Language_k03.json) |
| 17 | Social-Emotional | 1 → 2 | 8 → 2 | [before](raw/api/area-sweep/result_age17_Social-Emotional_k01.json) / [after](raw/api/area-sweep/result_age17_Social-Emotional_k02.json) |
| 18 | Physical | 2 → 3 | 12 → 0 | [before](raw/api/area-sweep/result_age18_Physical_k02.json) / [after](raw/api/area-sweep/result_age18_Physical_k03.json) |
| 18 | Language | 2 → 3 | 10 → 4 | [before](raw/api/area-sweep/result_age18_Language_k02.json) / [after](raw/api/area-sweep/result_age18_Language_k03.json) |
| 18 | Language | 3 → 4 | 4 → 0 | [before](raw/api/area-sweep/result_age18_Language_k03.json) / [after](raw/api/area-sweep/result_age18_Language_k04.json) |
| 18 | Social-Emotional | 1 → 2 | 8 → 0 | [before](raw/api/area-sweep/result_age18_Social-Emotional_k01.json) / [after](raw/api/area-sweep/result_age18_Social-Emotional_k02.json) |
| 19 | Physical | 1 → 2 | 12 → 4 | [before](raw/api/area-sweep/result_age19_Physical_k01.json) / [after](raw/api/area-sweep/result_age19_Physical_k02.json) |
| 19 | Cognitive | 1 → 2 | 10 → 0 | [before](raw/api/area-sweep/result_age19_Cognitive_k01.json) / [after](raw/api/area-sweep/result_age19_Cognitive_k02.json) |
| 19 | Language | 1 → 2 | 12 → 2 | [before](raw/api/area-sweep/result_age19_Language_k01.json) / [after](raw/api/area-sweep/result_age19_Language_k02.json) |
| 19 | Social-Emotional | 1 → 2 | 10 → 0 | [before](raw/api/area-sweep/result_age19_Social-Emotional_k01.json) / [after](raw/api/area-sweep/result_age19_Social-Emotional_k02.json) |
| 21 | Language | 2 → 3 | 16 → 0 | [before](raw/api/area-sweep/result_age21_Language_k02.json) / [after](raw/api/area-sweep/result_age21_Language_k03.json) |
| 21 | Social-Emotional | 1 → 2 | 12 → 0 | [before](raw/api/area-sweep/result_age21_Social-Emotional_k01.json) / [after](raw/api/area-sweep/result_age21_Social-Emotional_k02.json) |
| 22 | Language | 2 → 3 | 16 → 0 | [before](raw/api/area-sweep/result_age22_Language_k02.json) / [after](raw/api/area-sweep/result_age22_Language_k03.json) |
| 26 | Cognitive | 7 → 8 | 60 → 38 | [before](raw/api/area-sweep/result_age26_Cognitive_k07.json) / [after](raw/api/area-sweep/result_age26_Cognitive_k08.json) |
| 34 | Language | 8 → 9 | 60 → 44 | [before](raw/api/area-sweep/result_age34_Language_k08.json) / [after](raw/api/area-sweep/result_age34_Language_k09.json) |

## Descending order checks

Equal K compares different Yes identities within the target area, with the same served IDs and other-area baseline. Only pairs with exposed numeric months contribute to the months denominator. The endpoints K=0 and K=n use identical Yes sets; the interior-pair count identifies numeric comparisons with different Yes sets. Exposed `not_enough` records can contribute to the complete area-record comparison; matching below_floor responses do not reveal months and are excluded from both denominators.

| Age | Area | Report pairs | Numeric months match | Interior numeric pairs | Area state/months/atLeast match | K with no exposed area | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | Physical | 11/11 | 6/6 | 5 | 6/6 | 0, 1, 2, 3, 4 | all exposed pairs match |
| 12 | Cognitive | 10/10 | 10/10 | 8 | 10/10 | — | all exposed pairs match |
| 30 | Language | 10/10 | 8/8 | 7 | 8/8 | 0, 1 | all exposed pairs match |

Repeated `(age, own area, own Yes count)` outputs across all sweeps: **5462 comparisons, 0 conflicts**. This also checks other-area independence wherever area records are exposed. Conflicts, if any, are listed in the validation JSON.

**Inference:** agreement at equal K supports a count lookup for these fixed served-area ID sets. Three control sweeps do not prove identity-independence for every age, arbitrary subset, future server version or extension set. The underlying norm projection and quantization formula remain unresolved.

## How to compute an area's months from its Yes count

1. Use the assessment's returned integer `ageMonths` to select the saved initial list. Include every anchor, item and calibration question, assigning it to its own `area` field.
2. For the target area, count the Yes answers among that exact area's served IDs. This integer is K; n is the number of those IDs. The rates set the experimental baseline and ordering, but are not demonstrated per-answer score weights.
3. Find `(age, area, K)` in [area-table.csv](area-table.csv) or the compact tables below. Read `area_months`, `area_state` and `atLeast` together; true atLeast means a lower-bound month value, not an exact ceiling-free age.
4. Keep the global reporting gate: below_floor hides area months, and area not_enough supplies no numeric month. Missing fields are unknown, not zero. This table directly measures the other-three-areas baseline; applying its area mapping to other profiles relies on the separately tested independence inference and still requires an exposed report.
5. Use the measured lookup as it stands, including low-K decreases. Interpolation, smoothing, a universal Yes percentage, and an exact formula from the rounded rates would add unobserved assumptions. A changed ID set or extension requires a different lookup.

## Compact tables for every returned age

State is shown as `area state / headline state`; — means omitted. Consecutive rows collapse only when months, atLeast, both states and observation status match. Each evidence link points to the first/last raw response in that K range; every individual path remains in the CSV. Uncollected ranges have no evidence link.

### Age 0

#### Physical (n=12, Σ rates=7.32, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–8 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age00_Physical_k00.json) / [last](raw/api/area-sweep/result_age00_Physical_k08.json) |
| 9 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age00_Physical_k09.json) |
| 10–11 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age00_Physical_k10.json) / [last](raw/api/area-sweep/result_age00_Physical_k11.json) |
| 12 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age00_Physical_k12.json) |

#### Cognitive (n=11, Σ rates=5.48, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–6 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age00_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age00_Cognitive_k06.json) |
| 7 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age00_Cognitive_k07.json) |
| 8–9 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age00_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age00_Cognitive_k09.json) |
| 10–11 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age00_Cognitive_k10.json) / [last](raw/api/area-sweep/result_age00_Cognitive_k11.json) |

#### Language (n=7, Σ rates=3.01, baseline K=3)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–4 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age00_Language_k00.json) / [last](raw/api/area-sweep/result_age00_Language_k04.json) |
| 5–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age00_Language_k05.json) / [last](raw/api/area-sweep/result_age00_Language_k07.json) |

#### Social-Emotional (n=9, Σ rates=4.89, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–6 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age00_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age00_Social-Emotional_k06.json) |
| 7 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age00_Social-Emotional_k07.json) |
| 8 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age00_Social-Emotional_k08.json) |
| 9 | 4 | true | ok / ok | [raw](raw/api/area-sweep/result_age00_Social-Emotional_k09.json) |

### Age 1

#### Physical (n=13, Σ rates=6.32, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–6 | 2 | false | ok / ok | [first](raw/api/area-sweep/result_age01_Physical_k00.json) / [last](raw/api/area-sweep/result_age01_Physical_k06.json) |
| 7 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age01_Physical_k07.json) |
| 8 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age01_Physical_k08.json) |
| 9 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age01_Physical_k09.json) |
| 10 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age01_Physical_k10.json) |
| 11 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age01_Physical_k11.json) |
| 12–13 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age01_Physical_k12.json) / [last](raw/api/area-sweep/result_age01_Physical_k13.json) |

#### Cognitive (n=10, Σ rates=4.83, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–5 | 0 | false | ok / ok | [first](raw/api/area-sweep/result_age01_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age01_Cognitive_k05.json) |
| 6 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age01_Cognitive_k06.json) |
| 7–8 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age01_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age01_Cognitive_k08.json) |
| 9 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age01_Cognitive_k09.json) |
| 10 | 24 | true | ok / ok | [raw](raw/api/area-sweep/result_age01_Cognitive_k10.json) |

#### Language (n=7, Σ rates=3.03, baseline K=3)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age01_Language_k00.json) / [last](raw/api/area-sweep/result_age01_Language_k03.json) |
| 4 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age01_Language_k04.json) |
| 5–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age01_Language_k05.json) / [last](raw/api/area-sweep/result_age01_Language_k07.json) |

#### Social-Emotional (n=9, Σ rates=5.52, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–6 | 0 | false | ok / ok | [first](raw/api/area-sweep/result_age01_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age01_Social-Emotional_k06.json) |
| 7 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age01_Social-Emotional_k07.json) |
| 8 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age01_Social-Emotional_k08.json) |
| 9 | 6 | true | ok / ok | [raw](raw/api/area-sweep/result_age01_Social-Emotional_k09.json) |

### Age 2

#### Physical (n=10, Σ rates=5.74, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–5 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age02_Physical_k00.json) / [last](raw/api/area-sweep/result_age02_Physical_k05.json) |
| 6 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Physical_k06.json) |
| 7–8 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age02_Physical_k07.json) / [last](raw/api/area-sweep/result_age02_Physical_k08.json) |
| 9 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Physical_k09.json) |
| 10 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age02_Physical_k10.json) |

#### Cognitive (n=10, Σ rates=5.09, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–4 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age02_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age02_Cognitive_k04.json) |
| 5 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Cognitive_k05.json) |
| 6–8 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age02_Cognitive_k06.json) / [last](raw/api/area-sweep/result_age02_Cognitive_k08.json) |
| 9 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Cognitive_k09.json) |
| 10 | 16 | true | ok / ok | [raw](raw/api/area-sweep/result_age02_Cognitive_k10.json) |

#### Language (n=8, Σ rates=3.80, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age02_Language_k00.json) / [last](raw/api/area-sweep/result_age02_Language_k03.json) |
| 4 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Language_k04.json) |
| 5 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Language_k05.json) |
| 6 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Language_k06.json) |
| 7 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Language_k07.json) |
| 8 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age02_Language_k08.json) |

#### Social-Emotional (n=11, Σ rates=4.47, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age02_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age02_Social-Emotional_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Social-Emotional_k04.json) |
| 5 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Social-Emotional_k05.json) |
| 6–7 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age02_Social-Emotional_k06.json) / [last](raw/api/area-sweep/result_age02_Social-Emotional_k07.json) |
| 8 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Social-Emotional_k08.json) |
| 9 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age02_Social-Emotional_k09.json) |
| 10–11 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age02_Social-Emotional_k10.json) / [last](raw/api/area-sweep/result_age02_Social-Emotional_k11.json) |

### Age 3

#### Physical (n=10, Σ rates=5.52, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–4 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age03_Physical_k00.json) / [last](raw/api/area-sweep/result_age03_Physical_k04.json) |
| 5 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Physical_k05.json) |
| 6 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Physical_k06.json) |
| 7–8 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age03_Physical_k07.json) / [last](raw/api/area-sweep/result_age03_Physical_k08.json) |
| 9–10 | 10 | true | ok / ok | [first](raw/api/area-sweep/result_age03_Physical_k09.json) / [last](raw/api/area-sweep/result_age03_Physical_k10.json) |

#### Cognitive (n=11, Σ rates=5.31, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age03_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age03_Cognitive_k03.json) |
| 4 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Cognitive_k04.json) |
| 5–7 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age03_Cognitive_k05.json) / [last](raw/api/area-sweep/result_age03_Cognitive_k07.json) |
| 8 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Cognitive_k08.json) |
| 9 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Cognitive_k09.json) |
| 10 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Cognitive_k10.json) |
| 11 | 18 | true | ok / ok | [raw](raw/api/area-sweep/result_age03_Cognitive_k11.json) |

#### Language (n=9, Σ rates=4.48, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age03_Language_k00.json) / [last](raw/api/area-sweep/result_age03_Language_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Language_k03.json) |
| 4–5 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age03_Language_k04.json) / [last](raw/api/area-sweep/result_age03_Language_k05.json) |
| 6 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Language_k06.json) |
| 7 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Language_k07.json) |
| 8–9 | 10 | true | ok / ok | [first](raw/api/area-sweep/result_age03_Language_k08.json) / [last](raw/api/area-sweep/result_age03_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=4.60, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age03_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age03_Social-Emotional_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Social-Emotional_k04.json) |
| 5–7 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age03_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age03_Social-Emotional_k07.json) |
| 8 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age03_Social-Emotional_k08.json) |
| 9 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age03_Social-Emotional_k09.json) |

### Age 4

#### Physical (n=9, Σ rates=5.51, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age04_Physical_k00.json) / [last](raw/api/area-sweep/result_age04_Physical_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Physical_k04.json) |
| 5–7 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age04_Physical_k05.json) / [last](raw/api/area-sweep/result_age04_Physical_k07.json) |
| 8 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Physical_k08.json) |
| 9 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age04_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=4.85, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age04_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age04_Cognitive_k02.json) |
| 3–6 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age04_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age04_Cognitive_k06.json) |
| 7 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Cognitive_k07.json) |
| 8 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Cognitive_k08.json) |
| 9 | 10 | true | ok / ok | [raw](raw/api/area-sweep/result_age04_Cognitive_k09.json) |

#### Language (n=10, Σ rates=4.45, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age04_Language_k00.json) / [last](raw/api/area-sweep/result_age04_Language_k01.json) |
| 2–3 | 0 | false | ok / ok | [first](raw/api/area-sweep/result_age04_Language_k02.json) / [last](raw/api/area-sweep/result_age04_Language_k03.json) |
| 4–5 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age04_Language_k04.json) / [last](raw/api/area-sweep/result_age04_Language_k05.json) |
| 6 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Language_k06.json) |
| 7 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Language_k07.json) |
| 8 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Language_k08.json) |
| 9–10 | 12 | true | ok / ok | [first](raw/api/area-sweep/result_age04_Language_k09.json) / [last](raw/api/area-sweep/result_age04_Language_k10.json) |

#### Social-Emotional (n=11, Σ rates=5.94, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age04_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age04_Social-Emotional_k03.json) |
| 4 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Social-Emotional_k04.json) |
| 5–7 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age04_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age04_Social-Emotional_k07.json) |
| 8 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Social-Emotional_k08.json) |
| 9 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age04_Social-Emotional_k09.json) |
| 10–11 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age04_Social-Emotional_k10.json) / [last](raw/api/area-sweep/result_age04_Social-Emotional_k11.json) |

### Age 5

#### Physical (n=9, Σ rates=5.14, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age05_Physical_k00.json) / [last](raw/api/area-sweep/result_age05_Physical_k01.json) |
| 2–3 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age05_Physical_k02.json) / [last](raw/api/area-sweep/result_age05_Physical_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Physical_k04.json) |
| 5–6 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age05_Physical_k05.json) / [last](raw/api/area-sweep/result_age05_Physical_k06.json) |
| 7 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Physical_k07.json) |
| 8 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Physical_k08.json) |
| 9 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age05_Physical_k09.json) |

#### Cognitive (n=12, Σ rates=6.14, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age05_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age05_Cognitive_k02.json) |
| 3–6 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age05_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age05_Cognitive_k06.json) |
| 7 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Cognitive_k07.json) |
| 8–9 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age05_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age05_Cognitive_k09.json) |
| 10 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Cognitive_k10.json) |
| 11–12 | 32 | true | ok / ok | [first](raw/api/area-sweep/result_age05_Cognitive_k11.json) / [last](raw/api/area-sweep/result_age05_Cognitive_k12.json) |

#### Language (n=9, Σ rates=4.68, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age05_Language_k00.json) / [last](raw/api/area-sweep/result_age05_Language_k01.json) |
| 2 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Language_k02.json) |
| 3 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Language_k03.json) |
| 4 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Language_k04.json) |
| 5 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Language_k05.json) |
| 6–7 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age05_Language_k06.json) / [last](raw/api/area-sweep/result_age05_Language_k07.json) |
| 8–9 | 10 | true | ok / ok | [first](raw/api/area-sweep/result_age05_Language_k08.json) / [last](raw/api/area-sweep/result_age05_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.57, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age05_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age05_Social-Emotional_k02.json) |
| 3 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Social-Emotional_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Social-Emotional_k04.json) |
| 5–6 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age05_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age05_Social-Emotional_k06.json) |
| 7 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Social-Emotional_k07.json) |
| 8 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age05_Social-Emotional_k08.json) |
| 9 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age05_Social-Emotional_k09.json) |

### Age 6

#### Physical (n=9, Σ rates=5.01, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age06_Physical_k00.json) / [last](raw/api/area-sweep/result_age06_Physical_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Physical_k04.json) |
| 5 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Physical_k05.json) |
| 6–7 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age06_Physical_k06.json) / [last](raw/api/area-sweep/result_age06_Physical_k07.json) |
| 8 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Physical_k08.json) |
| 9 | 12 | true | ok / ok | [raw](raw/api/area-sweep/result_age06_Physical_k09.json) |

#### Cognitive (n=11, Σ rates=6.18, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–4 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age06_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age06_Cognitive_k04.json) |
| 5 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Cognitive_k05.json) |
| 6 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Cognitive_k06.json) |
| 7–8 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age06_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age06_Cognitive_k08.json) |
| 9 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Cognitive_k09.json) |
| 10–11 | 32 | true | ok / ok | [first](raw/api/area-sweep/result_age06_Cognitive_k10.json) / [last](raw/api/area-sweep/result_age06_Cognitive_k11.json) |

#### Language (n=10, Σ rates=5.35, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age06_Language_k00.json) / [last](raw/api/area-sweep/result_age06_Language_k03.json) |
| 4–5 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age06_Language_k04.json) / [last](raw/api/area-sweep/result_age06_Language_k05.json) |
| 6–7 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age06_Language_k06.json) / [last](raw/api/area-sweep/result_age06_Language_k07.json) |
| 8 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Language_k08.json) |
| 9–10 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age06_Language_k09.json) / [last](raw/api/area-sweep/result_age06_Language_k10.json) |

#### Social-Emotional (n=9, Σ rates=6.20, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–4 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age06_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age06_Social-Emotional_k04.json) |
| 5 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Social-Emotional_k05.json) |
| 6 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age06_Social-Emotional_k06.json) |
| 7–8 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age06_Social-Emotional_k07.json) / [last](raw/api/area-sweep/result_age06_Social-Emotional_k08.json) |
| 9 | 8 | true | ok / ok | [raw](raw/api/area-sweep/result_age06_Social-Emotional_k09.json) |

### Age 7

#### Physical (n=9, Σ rates=5.13, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age07_Physical_k00.json) |
| 1–2 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Physical_k01.json) / [last](raw/api/area-sweep/result_age07_Physical_k02.json) |
| 3–4 | 0 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Physical_k03.json) / [last](raw/api/area-sweep/result_age07_Physical_k04.json) |
| 5–7 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Physical_k05.json) / [last](raw/api/area-sweep/result_age07_Physical_k07.json) |
| 8 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Physical_k08.json) |
| 9 | 12 | true | ok / ok | [raw](raw/api/area-sweep/result_age07_Physical_k09.json) |

#### Cognitive (n=11, Σ rates=5.59, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age07_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age07_Cognitive_k01.json) |
| 2–3 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Cognitive_k02.json) / [last](raw/api/area-sweep/result_age07_Cognitive_k03.json) |
| 4 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Cognitive_k04.json) |
| 5 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Cognitive_k05.json) |
| 6–7 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Cognitive_k06.json) / [last](raw/api/area-sweep/result_age07_Cognitive_k07.json) |
| 8 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Cognitive_k08.json) |
| 9 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Cognitive_k09.json) |
| 10–11 | 22 | true | ok / ok | [first](raw/api/area-sweep/result_age07_Cognitive_k10.json) / [last](raw/api/area-sweep/result_age07_Cognitive_k11.json) |

#### Language (n=10, Σ rates=5.13, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age07_Language_k00.json) |
| 1–4 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Language_k01.json) / [last](raw/api/area-sweep/result_age07_Language_k04.json) |
| 5–7 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Language_k05.json) / [last](raw/api/area-sweep/result_age07_Language_k07.json) |
| 8 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Language_k08.json) |
| 9–10 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age07_Language_k09.json) / [last](raw/api/area-sweep/result_age07_Language_k10.json) |

#### Social-Emotional (n=9, Σ rates=5.91, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age07_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age07_Social-Emotional_k01.json) |
| 2–4 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age07_Social-Emotional_k04.json) |
| 5 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Social-Emotional_k05.json) |
| 6–7 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age07_Social-Emotional_k06.json) / [last](raw/api/area-sweep/result_age07_Social-Emotional_k07.json) |
| 8 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age07_Social-Emotional_k08.json) |
| 9 | 12 | true | ok / ok | [raw](raw/api/area-sweep/result_age07_Social-Emotional_k09.json) |

### Age 8

#### Physical (n=10, Σ rates=5.14, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Physical_k00.json) / [last](raw/api/area-sweep/result_age08_Physical_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Physical_k04.json) |
| 5–6 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Physical_k05.json) / [last](raw/api/area-sweep/result_age08_Physical_k06.json) |
| 7 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Physical_k07.json) |
| 8 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Physical_k08.json) |
| 9–10 | 22 | true | ok / ok | [first](raw/api/area-sweep/result_age08_Physical_k09.json) / [last](raw/api/area-sweep/result_age08_Physical_k10.json) |

#### Cognitive (n=10, Σ rates=5.49, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age08_Cognitive_k03.json) |
| 4 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Cognitive_k04.json) |
| 5–6 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Cognitive_k05.json) / [last](raw/api/area-sweep/result_age08_Cognitive_k06.json) |
| 7 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Cognitive_k07.json) |
| 8 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Cognitive_k08.json) |
| 9–10 | 30 | true | ok / ok | [first](raw/api/area-sweep/result_age08_Cognitive_k09.json) / [last](raw/api/area-sweep/result_age08_Cognitive_k10.json) |

#### Language (n=10, Σ rates=5.63, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age08_Language_k00.json) |
| 1–4 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Language_k01.json) / [last](raw/api/area-sweep/result_age08_Language_k04.json) |
| 5–6 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Language_k05.json) / [last](raw/api/area-sweep/result_age08_Language_k06.json) |
| 7 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Language_k07.json) |
| 8 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Language_k08.json) |
| 9–10 | 18 | true | ok / ok | [first](raw/api/area-sweep/result_age08_Language_k09.json) / [last](raw/api/area-sweep/result_age08_Language_k10.json) |

#### Social-Emotional (n=9, Σ rates=6.17, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age08_Social-Emotional_k00.json) |
| 1–4 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age08_Social-Emotional_k04.json) |
| 5–6 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age08_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age08_Social-Emotional_k06.json) |
| 7 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Social-Emotional_k07.json) |
| 8 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age08_Social-Emotional_k08.json) |
| 9 | 12 | true | ok / ok | [raw](raw/api/area-sweep/result_age08_Social-Emotional_k09.json) |

### Age 9

#### Physical (n=11, Σ rates=4.98, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age09_Physical_k00.json) |
| 1–2 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Physical_k01.json) / [last](raw/api/area-sweep/result_age09_Physical_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Physical_k03.json) |
| 4–5 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Physical_k04.json) / [last](raw/api/area-sweep/result_age09_Physical_k05.json) |
| 6 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Physical_k06.json) |
| 7–8 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Physical_k07.json) / [last](raw/api/area-sweep/result_age09_Physical_k08.json) |
| 9 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Physical_k09.json) |
| 10–11 | 30 | true | ok / ok | [first](raw/api/area-sweep/result_age09_Physical_k10.json) / [last](raw/api/area-sweep/result_age09_Physical_k11.json) |

#### Cognitive (n=10, Σ rates=6.26, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age09_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age09_Cognitive_k01.json) |
| 2–3 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Cognitive_k02.json) / [last](raw/api/area-sweep/result_age09_Cognitive_k03.json) |
| 4 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Cognitive_k04.json) |
| 5–6 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Cognitive_k05.json) / [last](raw/api/area-sweep/result_age09_Cognitive_k06.json) |
| 7 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Cognitive_k07.json) |
| 8 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Cognitive_k08.json) |
| 9–10 | 30 | true | ok / ok | [first](raw/api/area-sweep/result_age09_Cognitive_k09.json) / [last](raw/api/area-sweep/result_age09_Cognitive_k10.json) |

#### Language (n=9, Σ rates=5.32, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age09_Language_k00.json) |
| 1–3 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Language_k01.json) / [last](raw/api/area-sweep/result_age09_Language_k03.json) |
| 4–5 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Language_k04.json) / [last](raw/api/area-sweep/result_age09_Language_k05.json) |
| 6 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Language_k06.json) |
| 7 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Language_k07.json) |
| 8–9 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age09_Language_k08.json) / [last](raw/api/area-sweep/result_age09_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=4.82, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age09_Social-Emotional_k00.json) |
| 1–2 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age09_Social-Emotional_k02.json) |
| 3 | 6 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Social-Emotional_k03.json) |
| 4–5 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age09_Social-Emotional_k04.json) / [last](raw/api/area-sweep/result_age09_Social-Emotional_k05.json) |
| 6 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Social-Emotional_k06.json) |
| 7 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age09_Social-Emotional_k07.json) |
| 8–9 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age09_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age09_Social-Emotional_k09.json) |

### Age 10

#### Physical (n=9, Σ rates=4.98, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age10_Physical_k00.json) |
| 1–4 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Physical_k01.json) / [last](raw/api/area-sweep/result_age10_Physical_k04.json) |
| 5 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Physical_k05.json) |
| 6–7 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Physical_k06.json) / [last](raw/api/area-sweep/result_age10_Physical_k07.json) |
| 8 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Physical_k08.json) |
| 9 | 16 | true | ok / ok | [raw](raw/api/area-sweep/result_age10_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=4.46, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age10_Cognitive_k03.json) |
| 4–5 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age10_Cognitive_k05.json) |
| 6–7 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Cognitive_k06.json) / [last](raw/api/area-sweep/result_age10_Cognitive_k07.json) |
| 8 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Cognitive_k08.json) |
| 9 | 16 | true | ok / ok | [raw](raw/api/area-sweep/result_age10_Cognitive_k09.json) |

#### Language (n=12, Σ rates=6.09, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age10_Language_k00.json) / [last](raw/api/area-sweep/result_age10_Language_k01.json) |
| 2–3 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Language_k02.json) / [last](raw/api/area-sweep/result_age10_Language_k03.json) |
| 4–5 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Language_k04.json) / [last](raw/api/area-sweep/result_age10_Language_k05.json) |
| 6 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Language_k06.json) |
| 7 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Language_k07.json) |
| 8 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Language_k08.json) |
| 9 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Language_k09.json) |
| 10–12 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age10_Language_k10.json) / [last](raw/api/area-sweep/result_age10_Language_k12.json) |

#### Social-Emotional (n=9, Σ rates=5.20, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age10_Social-Emotional_k00.json) |
| 1–2 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age10_Social-Emotional_k02.json) |
| 3–4 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Social-Emotional_k03.json) / [last](raw/api/area-sweep/result_age10_Social-Emotional_k04.json) |
| 5 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age10_Social-Emotional_k05.json) |
| 6–7 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age10_Social-Emotional_k06.json) / [last](raw/api/area-sweep/result_age10_Social-Emotional_k07.json) |
| 8–9 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age10_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age10_Social-Emotional_k09.json) |

### Age 11

#### Physical (n=9, Σ rates=4.82, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Physical_k00.json) / [last](raw/api/area-sweep/result_age11_Physical_k03.json) |
| 4 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Physical_k04.json) |
| 5–6 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Physical_k05.json) / [last](raw/api/area-sweep/result_age11_Physical_k06.json) |
| 7 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Physical_k07.json) |
| 8 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Physical_k08.json) |
| 9 | 20 | true | ok / ok | [raw](raw/api/area-sweep/result_age11_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=4.46, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age11_Cognitive_k02.json) |
| 3 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Cognitive_k03.json) |
| 4–6 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age11_Cognitive_k06.json) |
| 7 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Cognitive_k07.json) |
| 8–9 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age11_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age11_Cognitive_k09.json) |

#### Language (n=10, Σ rates=5.99, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age11_Language_k00.json) |
| 1–2 | 4 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Language_k01.json) / [last](raw/api/area-sweep/result_age11_Language_k02.json) |
| 3–5 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Language_k03.json) / [last](raw/api/area-sweep/result_age11_Language_k05.json) |
| 6–7 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Language_k06.json) / [last](raw/api/area-sweep/result_age11_Language_k07.json) |
| 8 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Language_k08.json) |
| 9–10 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age11_Language_k09.json) / [last](raw/api/area-sweep/result_age11_Language_k10.json) |

#### Social-Emotional (n=11, Σ rates=5.64, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age11_Social-Emotional_k00.json) |
| 1–2 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age11_Social-Emotional_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Social-Emotional_k03.json) |
| 4 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Social-Emotional_k04.json) |
| 5 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Social-Emotional_k05.json) |
| 6–7 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age11_Social-Emotional_k06.json) / [last](raw/api/area-sweep/result_age11_Social-Emotional_k07.json) |
| 8 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Social-Emotional_k08.json) |
| 9 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age11_Social-Emotional_k09.json) |
| 10–11 | 36 | true | ok / ok | [first](raw/api/area-sweep/result_age11_Social-Emotional_k10.json) / [last](raw/api/area-sweep/result_age11_Social-Emotional_k11.json) |

### Age 12

#### Physical (n=9, Σ rates=5.04, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Physical_k00.json) / [last](raw/api/area-sweep/result_age12_Physical_k02.json) |
| 3 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Physical_k03.json) |
| 4–6 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Physical_k04.json) / [last](raw/api/area-sweep/result_age12_Physical_k06.json) |
| 7 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Physical_k07.json) |
| 8 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Physical_k08.json) |
| 9 | 20 | true | ok / ok | [raw](raw/api/area-sweep/result_age12_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=5.16, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age12_Cognitive_k01.json) |
| 2 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Cognitive_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Cognitive_k03.json) |
| 4–6 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age12_Cognitive_k06.json) |
| 7 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Cognitive_k07.json) |
| 8–9 | 16 | true | ok / ok | [first](raw/api/area-sweep/result_age12_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age12_Cognitive_k09.json) |

#### Language (n=10, Σ rates=5.72, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age12_Language_k00.json) |
| 1–2 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Language_k01.json) / [last](raw/api/area-sweep/result_age12_Language_k02.json) |
| 3–4 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Language_k03.json) / [last](raw/api/area-sweep/result_age12_Language_k04.json) |
| 5 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Language_k05.json) |
| 6 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Language_k06.json) |
| 7 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Language_k07.json) |
| 8 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Language_k08.json) |
| 9–10 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age12_Language_k09.json) / [last](raw/api/area-sweep/result_age12_Language_k10.json) |

#### Social-Emotional (n=11, Σ rates=6.49, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age12_Social-Emotional_k00.json) |
| 1–2 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age12_Social-Emotional_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Social-Emotional_k03.json) |
| 4 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Social-Emotional_k04.json) |
| 5 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Social-Emotional_k05.json) |
| 6–7 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age12_Social-Emotional_k06.json) / [last](raw/api/area-sweep/result_age12_Social-Emotional_k07.json) |
| 8 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Social-Emotional_k08.json) |
| 9 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age12_Social-Emotional_k09.json) |
| 10–11 | 36 | true | ok / ok | [first](raw/api/area-sweep/result_age12_Social-Emotional_k10.json) / [last](raw/api/area-sweep/result_age12_Social-Emotional_k11.json) |

### Age 13

#### Physical (n=11, Σ rates=5.45, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age13_Physical_k00.json) |
| 1–2 | 6 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Physical_k01.json) / [last](raw/api/area-sweep/result_age13_Physical_k02.json) |
| 3 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Physical_k03.json) |
| 4–5 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Physical_k04.json) / [last](raw/api/area-sweep/result_age13_Physical_k05.json) |
| 6 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Physical_k06.json) |
| 7 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Physical_k07.json) |
| 8 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Physical_k08.json) |
| 9 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Physical_k09.json) |
| 10–11 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age13_Physical_k10.json) / [last](raw/api/area-sweep/result_age13_Physical_k11.json) |

#### Cognitive (n=9, Σ rates=4.39, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age13_Cognitive_k01.json) |
| 2 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Cognitive_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age13_Cognitive_k04.json) |
| 5 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Cognitive_k05.json) |
| 6–7 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Cognitive_k06.json) / [last](raw/api/area-sweep/result_age13_Cognitive_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age13_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age13_Cognitive_k09.json) |

#### Language (n=10, Σ rates=5.02, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age13_Language_k00.json) |
| 1 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Language_k01.json) |
| 2 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Language_k02.json) |
| 3 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Language_k03.json) |
| 4–5 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Language_k04.json) / [last](raw/api/area-sweep/result_age13_Language_k05.json) |
| 6 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Language_k06.json) |
| 7 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Language_k07.json) |
| 8 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Language_k08.json) |
| 9–10 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age13_Language_k09.json) / [last](raw/api/area-sweep/result_age13_Language_k10.json) |

#### Social-Emotional (n=9, Σ rates=5.64, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age13_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age13_Social-Emotional_k01.json) |
| 2–3 | 0 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age13_Social-Emotional_k03.json) |
| 4–5 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age13_Social-Emotional_k04.json) / [last](raw/api/area-sweep/result_age13_Social-Emotional_k05.json) |
| 6 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Social-Emotional_k06.json) |
| 7 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age13_Social-Emotional_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age13_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age13_Social-Emotional_k09.json) |

### Age 14

#### Physical (n=10, Σ rates=5.46, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Physical_k00.json) / [last](raw/api/area-sweep/result_age14_Physical_k03.json) |
| 4–5 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Physical_k04.json) / [last](raw/api/area-sweep/result_age14_Physical_k05.json) |
| 6–7 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Physical_k06.json) / [last](raw/api/area-sweep/result_age14_Physical_k07.json) |
| 8 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Physical_k08.json) |
| 9–10 | 22 | true | ok / ok | [first](raw/api/area-sweep/result_age14_Physical_k09.json) / [last](raw/api/area-sweep/result_age14_Physical_k10.json) |

#### Cognitive (n=10, Σ rates=4.77, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age14_Cognitive_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age14_Cognitive_k04.json) |
| 5 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Cognitive_k05.json) |
| 6–7 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Cognitive_k06.json) / [last](raw/api/area-sweep/result_age14_Cognitive_k07.json) |
| 8 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Cognitive_k08.json) |
| 9–10 | 24 | true | ok / ok | [first](raw/api/area-sweep/result_age14_Cognitive_k09.json) / [last](raw/api/area-sweep/result_age14_Cognitive_k10.json) |

#### Language (n=10, Σ rates=5.31, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Language_k00.json) / [last](raw/api/area-sweep/result_age14_Language_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Language_k03.json) / [last](raw/api/area-sweep/result_age14_Language_k04.json) |
| 5 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Language_k05.json) |
| 6–7 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Language_k06.json) / [last](raw/api/area-sweep/result_age14_Language_k07.json) |
| 8 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Language_k08.json) |
| 9–10 | 22 | true | ok / ok | [first](raw/api/area-sweep/result_age14_Language_k09.json) / [last](raw/api/area-sweep/result_age14_Language_k10.json) |

#### Social-Emotional (n=9, Σ rates=6.21, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age14_Social-Emotional_k00.json) |
| 1 | 8 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Social-Emotional_k01.json) |
| 2–3 | 0 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age14_Social-Emotional_k03.json) |
| 4–5 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age14_Social-Emotional_k04.json) / [last](raw/api/area-sweep/result_age14_Social-Emotional_k05.json) |
| 6 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Social-Emotional_k06.json) |
| 7 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age14_Social-Emotional_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age14_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age14_Social-Emotional_k09.json) |

### Age 15

#### Physical (n=9, Σ rates=5.26, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Physical_k00.json) / [last](raw/api/area-sweep/result_age15_Physical_k04.json) |
| 5–7 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Physical_k05.json) / [last](raw/api/area-sweep/result_age15_Physical_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age15_Physical_k08.json) / [last](raw/api/area-sweep/result_age15_Physical_k09.json) |

#### Cognitive (n=10, Σ rates=5.03, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age15_Cognitive_k01.json) |
| 2 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Cognitive_k02.json) |
| 3 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Cognitive_k03.json) |
| 4 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Cognitive_k04.json) |
| 5–6 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Cognitive_k05.json) / [last](raw/api/area-sweep/result_age15_Cognitive_k06.json) |
| 7 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Cognitive_k07.json) |
| 8 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Cognitive_k08.json) |
| 9–10 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age15_Cognitive_k09.json) / [last](raw/api/area-sweep/result_age15_Cognitive_k10.json) |

#### Language (n=9, Σ rates=5.83, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Language_k00.json) / [last](raw/api/area-sweep/result_age15_Language_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Language_k03.json) / [last](raw/api/area-sweep/result_age15_Language_k04.json) |
| 5 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Language_k05.json) |
| 6 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Language_k06.json) |
| 7 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Language_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age15_Language_k08.json) / [last](raw/api/area-sweep/result_age15_Language_k09.json) |

#### Social-Emotional (n=11, Σ rates=6.26, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age15_Social-Emotional_k01.json) |
| 2 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Social-Emotional_k02.json) |
| 3 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Social-Emotional_k03.json) |
| 4–5 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Social-Emotional_k04.json) / [last](raw/api/area-sweep/result_age15_Social-Emotional_k05.json) |
| 6–7 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age15_Social-Emotional_k06.json) / [last](raw/api/area-sweep/result_age15_Social-Emotional_k07.json) |
| 8 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Social-Emotional_k08.json) |
| 9 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age15_Social-Emotional_k09.json) |
| 10–11 | 36 | true | ok / ok | [first](raw/api/area-sweep/result_age15_Social-Emotional_k10.json) / [last](raw/api/area-sweep/result_age15_Social-Emotional_k11.json) |

### Age 16

#### Physical (n=11, Σ rates=5.28, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Physical_k00.json) / [last](raw/api/area-sweep/result_age16_Physical_k01.json) |
| 2 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Physical_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Physical_k03.json) |
| 4 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Physical_k04.json) |
| 5–6 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Physical_k05.json) / [last](raw/api/area-sweep/result_age16_Physical_k06.json) |
| 7 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Physical_k07.json) |
| 8 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Physical_k08.json) |
| 9–11 | 30 | true | ok / ok | [first](raw/api/area-sweep/result_age16_Physical_k09.json) / [last](raw/api/area-sweep/result_age16_Physical_k11.json) |

#### Cognitive (n=10, Σ rates=5.06, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age16_Cognitive_k01.json) |
| 2 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Cognitive_k02.json) |
| 3 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Cognitive_k03.json) |
| 4–6 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age16_Cognitive_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Cognitive_k07.json) |
| 8 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Cognitive_k08.json) |
| 9–10 | 24 | true | ok / ok | [first](raw/api/area-sweep/result_age16_Cognitive_k09.json) / [last](raw/api/area-sweep/result_age16_Cognitive_k10.json) |

#### Language (n=9, Σ rates=5.87, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Language_k00.json) / [last](raw/api/area-sweep/result_age16_Language_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Language_k03.json) / [last](raw/api/area-sweep/result_age16_Language_k04.json) |
| 5 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Language_k05.json) |
| 6 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Language_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Language_k07.json) |
| 8–9 | 22 | true | ok / ok | [first](raw/api/area-sweep/result_age16_Language_k08.json) / [last](raw/api/area-sweep/result_age16_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.80, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age16_Social-Emotional_k01.json) |
| 2 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Social-Emotional_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Social-Emotional_k03.json) / [last](raw/api/area-sweep/result_age16_Social-Emotional_k04.json) |
| 5–6 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age16_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age16_Social-Emotional_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age16_Social-Emotional_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age16_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age16_Social-Emotional_k09.json) |

### Age 17

#### Physical (n=12, Σ rates=5.66, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Physical_k00.json) / [last](raw/api/area-sweep/result_age17_Physical_k03.json) |
| 4–6 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Physical_k04.json) / [last](raw/api/area-sweep/result_age17_Physical_k06.json) |
| 7–8 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Physical_k07.json) / [last](raw/api/area-sweep/result_age17_Physical_k08.json) |
| 9 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Physical_k09.json) |
| 10–12 | 30 | true | ok / ok | [first](raw/api/area-sweep/result_age17_Physical_k10.json) / [last](raw/api/area-sweep/result_age17_Physical_k12.json) |

#### Cognitive (n=9, Σ rates=5.08, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | 10 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Cognitive_k00.json) |
| 1 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Cognitive_k01.json) |
| 2 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Cognitive_k02.json) |
| 3–5 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age17_Cognitive_k05.json) |
| 6 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Cognitive_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Cognitive_k07.json) |
| 8–9 | 22 | true | ok / ok | [first](raw/api/area-sweep/result_age17_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age17_Cognitive_k09.json) |

#### Language (n=9, Σ rates=4.95, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Language_k00.json) / [last](raw/api/area-sweep/result_age17_Language_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Language_k03.json) |
| 4–5 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Language_k04.json) / [last](raw/api/area-sweep/result_age17_Language_k05.json) |
| 6 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Language_k06.json) |
| 7 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Language_k07.json) |
| 8–9 | 24 | true | ok / ok | [first](raw/api/area-sweep/result_age17_Language_k08.json) / [last](raw/api/area-sweep/result_age17_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=6.41, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age17_Social-Emotional_k01.json) |
| 2 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Social-Emotional_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Social-Emotional_k03.json) / [last](raw/api/area-sweep/result_age17_Social-Emotional_k04.json) |
| 5–6 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age17_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age17_Social-Emotional_k06.json) |
| 7 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age17_Social-Emotional_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age17_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age17_Social-Emotional_k09.json) |

### Age 18

#### Physical (n=10, Σ rates=5.66, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Physical_k00.json) / [last](raw/api/area-sweep/result_age18_Physical_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Physical_k03.json) |
| 4–5 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Physical_k04.json) / [last](raw/api/area-sweep/result_age18_Physical_k05.json) |
| 6 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Physical_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Physical_k07.json) |
| 8–10 | 30 | true | ok / ok | [first](raw/api/area-sweep/result_age18_Physical_k08.json) / [last](raw/api/area-sweep/result_age18_Physical_k10.json) |

#### Cognitive (n=10, Σ rates=6.04, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age18_Cognitive_k01.json) |
| 2 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Cognitive_k02.json) |
| 3 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Cognitive_k03.json) |
| 4–5 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age18_Cognitive_k05.json) |
| 6 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Cognitive_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Cognitive_k07.json) |
| 8–10 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age18_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age18_Cognitive_k10.json) |

#### Language (n=10, Σ rates=5.69, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Language_k00.json) / [last](raw/api/area-sweep/result_age18_Language_k02.json) |
| 3 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Language_k03.json) |
| 4 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Language_k04.json) |
| 5 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Language_k05.json) |
| 6–7 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Language_k06.json) / [last](raw/api/area-sweep/result_age18_Language_k07.json) |
| 8–10 | 24 | true | ok / ok | [first](raw/api/area-sweep/result_age18_Language_k08.json) / [last](raw/api/area-sweep/result_age18_Language_k10.json) |

#### Social-Emotional (n=9, Σ rates=6.74, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 8 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age18_Social-Emotional_k01.json) |
| 2 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Social-Emotional_k02.json) |
| 3–4 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Social-Emotional_k03.json) / [last](raw/api/area-sweep/result_age18_Social-Emotional_k04.json) |
| 5–6 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age18_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age18_Social-Emotional_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age18_Social-Emotional_k07.json) |
| 8–9 | 20 | true | ok / ok | [first](raw/api/area-sweep/result_age18_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age18_Social-Emotional_k09.json) |

### Age 19

#### Physical (n=9, Σ rates=5.90, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Physical_k00.json) / [last](raw/api/area-sweep/result_age19_Physical_k01.json) |
| 2 | 4 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Physical_k02.json) |
| 3–4 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Physical_k03.json) / [last](raw/api/area-sweep/result_age19_Physical_k04.json) |
| 5 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Physical_k05.json) |
| 6–7 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Physical_k06.json) / [last](raw/api/area-sweep/result_age19_Physical_k07.json) |
| 8–9 | 24 | true | ok / ok | [first](raw/api/area-sweep/result_age19_Physical_k08.json) / [last](raw/api/area-sweep/result_age19_Physical_k09.json) |

#### Cognitive (n=10, Σ rates=6.10, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age19_Cognitive_k01.json) |
| 2 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Cognitive_k02.json) |
| 3–5 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age19_Cognitive_k05.json) |
| 6–7 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Cognitive_k06.json) / [last](raw/api/area-sweep/result_age19_Cognitive_k07.json) |
| 8–10 | 24 | true | ok / ok | [first](raw/api/area-sweep/result_age19_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age19_Cognitive_k10.json) |

#### Language (n=10, Σ rates=5.00, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Language_k00.json) / [last](raw/api/area-sweep/result_age19_Language_k01.json) |
| 2 | 2 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Language_k02.json) |
| 3–4 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Language_k03.json) / [last](raw/api/area-sweep/result_age19_Language_k04.json) |
| 5–6 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Language_k05.json) / [last](raw/api/area-sweep/result_age19_Language_k06.json) |
| 7 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Language_k07.json) |
| 8–10 | 24 | true | ok / ok | [first](raw/api/area-sweep/result_age19_Language_k08.json) / [last](raw/api/area-sweep/result_age19_Language_k10.json) |

#### Social-Emotional (n=10, Σ rates=6.30, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age19_Social-Emotional_k01.json) |
| 2 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Social-Emotional_k02.json) |
| 3 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Social-Emotional_k03.json) |
| 4–5 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age19_Social-Emotional_k04.json) / [last](raw/api/area-sweep/result_age19_Social-Emotional_k05.json) |
| 6 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Social-Emotional_k06.json) |
| 7 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age19_Social-Emotional_k07.json) |
| 8–10 | 32 | true | ok / ok | [first](raw/api/area-sweep/result_age19_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age19_Social-Emotional_k10.json) |

### Age 20

#### Physical (n=10, Σ rates=5.15, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 14 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Physical_k00.json) / [last](raw/api/area-sweep/result_age20_Physical_k03.json) |
| 4 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Physical_k04.json) |
| 5–6 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Physical_k05.json) / [last](raw/api/area-sweep/result_age20_Physical_k06.json) |
| 7 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Physical_k07.json) |
| 8 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Physical_k08.json) |
| 9–10 | 36 | true | ok / ok | [first](raw/api/area-sweep/result_age20_Physical_k09.json) / [last](raw/api/area-sweep/result_age20_Physical_k10.json) |

#### Cognitive (n=9, Σ rates=5.60, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age20_Cognitive_k01.json) |
| 2 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Cognitive_k02.json) |
| 3–4 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age20_Cognitive_k04.json) |
| 5–6 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Cognitive_k05.json) / [last](raw/api/area-sweep/result_age20_Cognitive_k06.json) |
| 7 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Cognitive_k07.json) |
| 8–9 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age20_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age20_Cognitive_k09.json) |

#### Language (n=10, Σ rates=5.21, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Language_k00.json) / [last](raw/api/area-sweep/result_age20_Language_k01.json) |
| 2 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Language_k02.json) |
| 3 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Language_k03.json) |
| 4 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Language_k04.json) |
| 5–6 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Language_k05.json) / [last](raw/api/area-sweep/result_age20_Language_k06.json) |
| 7 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Language_k07.json) |
| 8–10 | 26 | true | ok / ok | [first](raw/api/area-sweep/result_age20_Language_k08.json) / [last](raw/api/area-sweep/result_age20_Language_k10.json) |

#### Social-Emotional (n=10, Σ rates=6.01, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 10 | false | ok / ok | [first](raw/api/area-sweep/result_age20_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age20_Social-Emotional_k02.json) |
| 3 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Social-Emotional_k03.json) |
| 4 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Social-Emotional_k04.json) |
| 5 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Social-Emotional_k05.json) |
| 6 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Social-Emotional_k06.json) |
| 7 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Social-Emotional_k07.json) |
| 8 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age20_Social-Emotional_k08.json) |
| 9–10 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age20_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age20_Social-Emotional_k10.json) |

### Age 21

#### Physical (n=11, Σ rates=5.34, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Physical_k00.json) / [last](raw/api/area-sweep/result_age21_Physical_k03.json) |
| 4–5 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Physical_k04.json) / [last](raw/api/area-sweep/result_age21_Physical_k05.json) |
| 6 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Physical_k06.json) |
| 7 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Physical_k07.json) |
| 8 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Physical_k08.json) |
| 9–11 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age21_Physical_k09.json) / [last](raw/api/area-sweep/result_age21_Physical_k11.json) |

#### Cognitive (n=9, Σ rates=5.10, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 18 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age21_Cognitive_k03.json) |
| 4–5 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age21_Cognitive_k05.json) |
| 6 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Cognitive_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Cognitive_k07.json) |
| 8–9 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age21_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age21_Cognitive_k09.json) |

#### Language (n=9, Σ rates=4.74, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Language_k00.json) / [last](raw/api/area-sweep/result_age21_Language_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Language_k03.json) |
| 4–5 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Language_k04.json) / [last](raw/api/area-sweep/result_age21_Language_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Language_k06.json) |
| 7–9 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age21_Language_k07.json) / [last](raw/api/area-sweep/result_age21_Language_k09.json) |

#### Social-Emotional (n=10, Σ rates=5.90, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age21_Social-Emotional_k01.json) |
| 2 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Social-Emotional_k02.json) |
| 3 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Social-Emotional_k03.json) |
| 4 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Social-Emotional_k04.json) |
| 5–6 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age21_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age21_Social-Emotional_k06.json) |
| 7 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Social-Emotional_k07.json) |
| 8 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age21_Social-Emotional_k08.json) |
| 9–10 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age21_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age21_Social-Emotional_k10.json) |

### Age 22

#### Physical (n=12, Σ rates=5.63, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age22_Physical_k00.json) / [last](raw/api/area-sweep/result_age22_Physical_k03.json) |
| 4–5 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age22_Physical_k04.json) / [last](raw/api/area-sweep/result_age22_Physical_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Physical_k06.json) |
| 7 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Physical_k07.json) |
| 8 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Physical_k08.json) |
| 9 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Physical_k09.json) |
| 10–12 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age22_Physical_k10.json) / [last](raw/api/area-sweep/result_age22_Physical_k12.json) |

#### Cognitive (n=9, Σ rates=5.49, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 14 | false | ok / ok | [first](raw/api/area-sweep/result_age22_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age22_Cognitive_k02.json) |
| 3 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Cognitive_k03.json) |
| 4–5 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age22_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age22_Cognitive_k05.json) |
| 6 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Cognitive_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Cognitive_k07.json) |
| 8–9 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age22_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age22_Cognitive_k09.json) |

#### Language (n=9, Σ rates=4.99, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age22_Language_k00.json) / [last](raw/api/area-sweep/result_age22_Language_k02.json) |
| 3 | 0 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Language_k03.json) |
| 4 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Language_k04.json) |
| 5 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Language_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Language_k06.json) |
| 7–9 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age22_Language_k07.json) / [last](raw/api/area-sweep/result_age22_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.58, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 12 | false | ok / ok | [first](raw/api/area-sweep/result_age22_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age22_Social-Emotional_k02.json) |
| 3 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Social-Emotional_k03.json) |
| 4 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Social-Emotional_k04.json) |
| 5 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Social-Emotional_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age22_Social-Emotional_k07.json) |
| 8–9 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age22_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age22_Social-Emotional_k09.json) |

### Age 23

#### Physical (n=12, Σ rates=5.65, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age23_Physical_k00.json) / [last](raw/api/area-sweep/result_age23_Physical_k02.json) |
| 3–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age23_Physical_k03.json) / [last](raw/api/area-sweep/result_age23_Physical_k04.json) |
| 5 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Physical_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Physical_k06.json) |
| 7 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Physical_k07.json) |
| 8 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Physical_k08.json) |
| 9 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Physical_k09.json) |
| 10–12 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age23_Physical_k10.json) / [last](raw/api/area-sweep/result_age23_Physical_k12.json) |

#### Cognitive (n=9, Σ rates=5.10, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 18 | false | ok / ok | [first](raw/api/area-sweep/result_age23_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age23_Cognitive_k03.json) |
| 4 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Cognitive_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Cognitive_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Cognitive_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Cognitive_k07.json) |
| 8–9 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age23_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age23_Cognitive_k09.json) |

#### Language (n=9, Σ rates=4.96, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age23_Language_k00.json) / [last](raw/api/area-sweep/result_age23_Language_k02.json) |
| 3–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age23_Language_k03.json) / [last](raw/api/area-sweep/result_age23_Language_k04.json) |
| 5–6 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age23_Language_k05.json) / [last](raw/api/area-sweep/result_age23_Language_k06.json) |
| 7–9 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age23_Language_k07.json) / [last](raw/api/area-sweep/result_age23_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.86, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 14 | false | ok / ok | [first](raw/api/area-sweep/result_age23_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age23_Social-Emotional_k02.json) |
| 3 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Social-Emotional_k03.json) |
| 4 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Social-Emotional_k04.json) |
| 5 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Social-Emotional_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age23_Social-Emotional_k07.json) |
| 8–9 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age23_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age23_Social-Emotional_k09.json) |

### Age 24

#### Physical (n=12, Σ rates=5.75, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age24_Physical_k00.json) / [last](raw/api/area-sweep/result_age24_Physical_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Physical_k02.json) |
| 3–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age24_Physical_k03.json) / [last](raw/api/area-sweep/result_age24_Physical_k04.json) |
| 5 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Physical_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Physical_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Physical_k07.json) |
| 8 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Physical_k08.json) |
| 9 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Physical_k09.json) |
| 10–12 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age24_Physical_k10.json) / [last](raw/api/area-sweep/result_age24_Physical_k12.json) |

#### Cognitive (n=9, Σ rates=5.19, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 18 | false | ok / ok | [first](raw/api/area-sweep/result_age24_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age24_Cognitive_k02.json) |
| 3–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age24_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age24_Cognitive_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Cognitive_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Cognitive_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Cognitive_k07.json) |
| 8–9 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age24_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age24_Cognitive_k09.json) |

#### Language (n=9, Σ rates=4.90, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age24_Language_k00.json) / [last](raw/api/area-sweep/result_age24_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Language_k03.json) |
| 4 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Language_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Language_k05.json) |
| 6 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Language_k06.json) |
| 7–9 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age24_Language_k07.json) / [last](raw/api/area-sweep/result_age24_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.96, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age24_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age24_Social-Emotional_k03.json) |
| 4 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Social-Emotional_k04.json) |
| 5 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Social-Emotional_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age24_Social-Emotional_k07.json) |
| 8–9 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age24_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age24_Social-Emotional_k09.json) |

### Age 25

#### Physical (n=10, Σ rates=5.61, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age25_Physical_k00.json) / [last](raw/api/area-sweep/result_age25_Physical_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Physical_k02.json) |
| 3–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age25_Physical_k03.json) / [last](raw/api/area-sweep/result_age25_Physical_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Physical_k05.json) |
| 6 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Physical_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Physical_k07.json) |
| 8–10 | 36 | true | ok / ok | [first](raw/api/area-sweep/result_age25_Physical_k08.json) / [last](raw/api/area-sweep/result_age25_Physical_k10.json) |

#### Cognitive (n=9, Σ rates=5.08, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age25_Cognitive_k00.json) |
| 1–3 | 18 | false | ok / ok | [first](raw/api/area-sweep/result_age25_Cognitive_k01.json) / [last](raw/api/area-sweep/result_age25_Cognitive_k03.json) |
| 4 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Cognitive_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Cognitive_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Cognitive_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Cognitive_k07.json) |
| 8–9 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age25_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age25_Cognitive_k09.json) |

#### Language (n=10, Σ rates=5.36, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age25_Language_k00.json) |
| 1 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Language_k01.json) |
| 2 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Language_k03.json) |
| 4 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Language_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Language_k05.json) |
| 6 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Language_k06.json) |
| 7–10 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age25_Language_k07.json) / [last](raw/api/area-sweep/result_age25_Language_k10.json) |

#### Social-Emotional (n=10, Σ rates=6.24, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age25_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age25_Social-Emotional_k01.json) |
| 2 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Social-Emotional_k02.json) |
| 3 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Social-Emotional_k03.json) |
| 4–5 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age25_Social-Emotional_k04.json) / [last](raw/api/area-sweep/result_age25_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Social-Emotional_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Social-Emotional_k07.json) |
| 8 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age25_Social-Emotional_k08.json) |
| 9–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age25_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age25_Social-Emotional_k10.json) |

### Age 26

#### Physical (n=9, Σ rates=5.15, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age26_Physical_k00.json) |
| 1 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Physical_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Physical_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Physical_k03.json) |
| 4–5 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age26_Physical_k04.json) / [last](raw/api/area-sweep/result_age26_Physical_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Physical_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Physical_k07.json) |
| 8–9 | 36 | true | ok / ok | [first](raw/api/area-sweep/result_age26_Physical_k08.json) / [last](raw/api/area-sweep/result_age26_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=4.59, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age26_Cognitive_k00.json) |
| 1–3 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age26_Cognitive_k01.json) / [last](raw/api/area-sweep/result_age26_Cognitive_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Cognitive_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Cognitive_k05.json) |
| 6 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Cognitive_k06.json) |
| 7 | 60 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Cognitive_k07.json) |
| 8–9 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age26_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age26_Cognitive_k09.json) |

#### Language (n=10, Σ rates=5.43, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age26_Language_k00.json) |
| 1 | 14 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Language_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Language_k03.json) |
| 4–5 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age26_Language_k04.json) / [last](raw/api/area-sweep/result_age26_Language_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Language_k06.json) |
| 7–10 | 30 | true | ok / ok | [first](raw/api/area-sweep/result_age26_Language_k07.json) / [last](raw/api/area-sweep/result_age26_Language_k10.json) |

#### Social-Emotional (n=11, Σ rates=6.73, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age26_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age26_Social-Emotional_k02.json) |
| 3 | 12 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Social-Emotional_k03.json) |
| 4–5 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age26_Social-Emotional_k04.json) / [last](raw/api/area-sweep/result_age26_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Social-Emotional_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Social-Emotional_k07.json) |
| 8 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age26_Social-Emotional_k08.json) |
| 9–11 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age26_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age26_Social-Emotional_k11.json) |

### Age 27

#### Physical (n=11, Σ rates=5.36, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age27_Physical_k00.json) |
| 1 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k04.json) |
| 5 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k06.json) |
| 7 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k07.json) |
| 8 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Physical_k08.json) |
| 9–11 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age27_Physical_k09.json) / [last](raw/api/area-sweep/result_age27_Physical_k11.json) |

#### Cognitive (n=10, Σ rates=5.17, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age27_Cognitive_k00.json) |
| 1–3 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age27_Cognitive_k01.json) / [last](raw/api/area-sweep/result_age27_Cognitive_k03.json) |
| 4 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Cognitive_k04.json) |
| 5 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Cognitive_k05.json) |
| 6 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Cognitive_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Cognitive_k07.json) |
| 8–10 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age27_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age27_Cognitive_k10.json) |

#### Language (n=9, Σ rates=5.35, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age27_Language_k00.json) |
| 1 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Language_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Language_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Language_k04.json) |
| 5 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Language_k05.json) |
| 6–9 | 28 | true | ok / ok | [first](raw/api/area-sweep/result_age27_Language_k06.json) / [last](raw/api/area-sweep/result_age27_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=6.48, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age27_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age27_Social-Emotional_k01.json) |
| 2–3 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age27_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age27_Social-Emotional_k03.json) |
| 4 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Social-Emotional_k04.json) |
| 5 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Social-Emotional_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age27_Social-Emotional_k07.json) |
| 8–9 | 36 | true | ok / ok | [first](raw/api/area-sweep/result_age27_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age27_Social-Emotional_k09.json) |

### Age 28

#### Physical (n=10, Σ rates=5.51, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age28_Physical_k00.json) / [last](raw/api/area-sweep/result_age28_Physical_k01.json) |
| 2–3 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age28_Physical_k02.json) / [last](raw/api/area-sweep/result_age28_Physical_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Physical_k04.json) |
| 5–6 | 28 | false | ok / ok | [first](raw/api/area-sweep/result_age28_Physical_k05.json) / [last](raw/api/area-sweep/result_age28_Physical_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Physical_k07.json) |
| 8–10 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age28_Physical_k08.json) / [last](raw/api/area-sweep/result_age28_Physical_k10.json) |

#### Cognitive (n=10, Σ rates=5.00, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age28_Cognitive_k00.json) |
| 1–3 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age28_Cognitive_k01.json) / [last](raw/api/area-sweep/result_age28_Cognitive_k03.json) |
| 4 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Cognitive_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Cognitive_k05.json) |
| 6 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Cognitive_k06.json) |
| 7 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Cognitive_k07.json) |
| 8–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age28_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age28_Cognitive_k10.json) |

#### Language (n=10, Σ rates=5.43, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age28_Language_k00.json) |
| 1 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Language_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Language_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Language_k04.json) |
| 5 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Language_k05.json) |
| 6 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Language_k06.json) |
| 7–10 | 34 | true | ok / ok | [first](raw/api/area-sweep/result_age28_Language_k07.json) / [last](raw/api/area-sweep/result_age28_Language_k10.json) |

#### Social-Emotional (n=9, Σ rates=6.43, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age28_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age28_Social-Emotional_k01.json) |
| 2–3 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age28_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age28_Social-Emotional_k03.json) |
| 4 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Social-Emotional_k04.json) |
| 5–6 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age28_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age28_Social-Emotional_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age28_Social-Emotional_k07.json) |
| 8–9 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age28_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age28_Social-Emotional_k09.json) |

### Age 29

#### Physical (n=11, Σ rates=5.54, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age29_Physical_k00.json) |
| 1 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Physical_k01.json) |
| 2 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Physical_k02.json) |
| 3–4 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age29_Physical_k03.json) / [last](raw/api/area-sweep/result_age29_Physical_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Physical_k05.json) |
| 6 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Physical_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Physical_k07.json) |
| 8 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Physical_k08.json) |
| 9–11 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age29_Physical_k09.json) / [last](raw/api/area-sweep/result_age29_Physical_k11.json) |

#### Cognitive (n=9, Σ rates=5.17, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age29_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age29_Cognitive_k03.json) |
| 4 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Cognitive_k04.json) |
| 5 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Cognitive_k05.json) |
| 6 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Cognitive_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Cognitive_k07.json) |
| 8–9 | 38 | true | ok / ok | [first](raw/api/area-sweep/result_age29_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age29_Cognitive_k09.json) |

#### Language (n=9, Σ rates=5.51, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age29_Language_k00.json) |
| 1 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Language_k01.json) |
| 2 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Language_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Language_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Language_k05.json) |
| 6–9 | 32 | true | ok / ok | [first](raw/api/area-sweep/result_age29_Language_k06.json) / [last](raw/api/area-sweep/result_age29_Language_k09.json) |

#### Social-Emotional (n=10, Σ rates=6.72, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age29_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age29_Social-Emotional_k01.json) |
| 2–3 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age29_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age29_Social-Emotional_k03.json) |
| 4 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Social-Emotional_k04.json) |
| 5 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Social-Emotional_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Social-Emotional_k07.json) |
| 8 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age29_Social-Emotional_k08.json) |
| 9–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age29_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age29_Social-Emotional_k10.json) |

### Age 30

#### Physical (n=10, Σ rates=5.99, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age30_Physical_k00.json) / [last](raw/api/area-sweep/result_age30_Physical_k01.json) |
| 2 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Physical_k02.json) |
| 3 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Physical_k03.json) |
| 4 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Physical_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Physical_k05.json) |
| 6 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Physical_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Physical_k07.json) |
| 8–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age30_Physical_k08.json) / [last](raw/api/area-sweep/result_age30_Physical_k10.json) |

#### Cognitive (n=10, Σ rates=5.32, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age30_Cognitive_k00.json) |
| 1–3 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age30_Cognitive_k01.json) / [last](raw/api/area-sweep/result_age30_Cognitive_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Cognitive_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Cognitive_k05.json) |
| 6 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Cognitive_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Cognitive_k07.json) |
| 8–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age30_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age30_Cognitive_k10.json) |

#### Language (n=9, Σ rates=5.87, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age30_Language_k00.json) / [last](raw/api/area-sweep/result_age30_Language_k01.json) |
| 2 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Language_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Language_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Language_k05.json) |
| 6 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Language_k06.json) |
| 7–9 | 32 | true | ok / ok | [first](raw/api/area-sweep/result_age30_Language_k07.json) / [last](raw/api/area-sweep/result_age30_Language_k09.json) |

#### Social-Emotional (n=10, Σ rates=6.89, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age30_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age30_Social-Emotional_k02.json) |
| 3–4 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age30_Social-Emotional_k03.json) / [last](raw/api/area-sweep/result_age30_Social-Emotional_k04.json) |
| 5 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Social-Emotional_k05.json) |
| 6 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Social-Emotional_k06.json) |
| 7 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Social-Emotional_k07.json) |
| 8 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age30_Social-Emotional_k08.json) |
| 9–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age30_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age30_Social-Emotional_k10.json) |

### Age 31

#### Physical (n=10, Σ rates=5.08, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age31_Physical_k00.json) |
| 1 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Physical_k01.json) |
| 2 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Physical_k02.json) |
| 3 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Physical_k03.json) |
| 4 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Physical_k04.json) |
| 5–6 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age31_Physical_k05.json) / [last](raw/api/area-sweep/result_age31_Physical_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Physical_k07.json) |
| 8–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age31_Physical_k08.json) / [last](raw/api/area-sweep/result_age31_Physical_k10.json) |

#### Cognitive (n=9, Σ rates=4.93, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age31_Cognitive_k00.json) |
| 1–2 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age31_Cognitive_k01.json) / [last](raw/api/area-sweep/result_age31_Cognitive_k02.json) |
| 3 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Cognitive_k03.json) |
| 4 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Cognitive_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Cognitive_k05.json) |
| 6 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age31_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age31_Cognitive_k09.json) |

#### Language (n=10, Σ rates=6.08, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age31_Language_k00.json) / [last](raw/api/area-sweep/result_age31_Language_k01.json) |
| 2 | 16 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Language_k02.json) |
| 3 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Language_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Language_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Language_k05.json) |
| 6 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Language_k06.json) |
| 7–10 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age31_Language_k07.json) / [last](raw/api/area-sweep/result_age31_Language_k10.json) |

#### Social-Emotional (n=10, Σ rates=6.47, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age31_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age31_Social-Emotional_k01.json) |
| 2–3 | 16 | false | ok / ok | [first](raw/api/area-sweep/result_age31_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age31_Social-Emotional_k03.json) |
| 4 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Social-Emotional_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Social-Emotional_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Social-Emotional_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Social-Emotional_k07.json) |
| 8 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age31_Social-Emotional_k08.json) |
| 9–10 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age31_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age31_Social-Emotional_k10.json) |

### Age 32

#### Physical (n=9, Σ rates=5.25, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age32_Physical_k00.json) |
| 1 | 18 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Physical_k01.json) |
| 2 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Physical_k02.json) |
| 3 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Physical_k03.json) |
| 4 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Physical_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Physical_k05.json) |
| 6 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Physical_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age32_Physical_k07.json) / [last](raw/api/area-sweep/result_age32_Physical_k09.json) |

#### Cognitive (n=10, Σ rates=5.27, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age32_Cognitive_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Cognitive_k01.json) |
| 2 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Cognitive_k03.json) |
| 4 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Cognitive_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Cognitive_k05.json) |
| 6 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Cognitive_k06.json) |
| 7 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Cognitive_k07.json) |
| 8–10 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age32_Cognitive_k08.json) / [last](raw/api/area-sweep/result_age32_Cognitive_k10.json) |

#### Language (n=11, Σ rates=6.87, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age32_Language_k00.json) / [last](raw/api/area-sweep/result_age32_Language_k02.json) |
| 3–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age32_Language_k03.json) / [last](raw/api/area-sweep/result_age32_Language_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Language_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Language_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Language_k07.json) |
| 8–11 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age32_Language_k08.json) / [last](raw/api/area-sweep/result_age32_Language_k11.json) |

#### Social-Emotional (n=9, Σ rates=5.34, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age32_Social-Emotional_k00.json) |
| 1–3 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age32_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age32_Social-Emotional_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Social-Emotional_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Social-Emotional_k05.json) |
| 6 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Social-Emotional_k06.json) |
| 7 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age32_Social-Emotional_k07.json) |
| 8–9 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age32_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age32_Social-Emotional_k09.json) |

### Age 33

#### Physical (n=9, Σ rates=5.36, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 18 | false | ok / ok | [first](raw/api/area-sweep/result_age33_Physical_k00.json) / [last](raw/api/area-sweep/result_age33_Physical_k01.json) |
| 2 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Physical_k02.json) |
| 3 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Physical_k03.json) |
| 4 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Physical_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Physical_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Physical_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age33_Physical_k07.json) / [last](raw/api/area-sweep/result_age33_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=4.92, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age33_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age33_Cognitive_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Cognitive_k03.json) |
| 4–5 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age33_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age33_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age33_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age33_Cognitive_k09.json) |

#### Language (n=11, Σ rates=6.86, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age33_Language_k00.json) / [last](raw/api/area-sweep/result_age33_Language_k01.json) |
| 2–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age33_Language_k02.json) / [last](raw/api/area-sweep/result_age33_Language_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Language_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Language_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Language_k07.json) |
| 8–11 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age33_Language_k08.json) / [last](raw/api/area-sweep/result_age33_Language_k11.json) |

#### Social-Emotional (n=10, Σ rates=5.93, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age33_Social-Emotional_k00.json) |
| 1–3 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age33_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age33_Social-Emotional_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Social-Emotional_k04.json) |
| 5–6 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age33_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age33_Social-Emotional_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Social-Emotional_k07.json) |
| 8 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age33_Social-Emotional_k08.json) |
| 9–10 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age33_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age33_Social-Emotional_k10.json) |

### Age 34

#### Physical (n=9, Σ rates=5.57, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age34_Physical_k00.json) / [last](raw/api/area-sweep/result_age34_Physical_k01.json) |
| 2 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Physical_k02.json) |
| 3–4 | 28 | false | ok / ok | [first](raw/api/area-sweep/result_age34_Physical_k03.json) / [last](raw/api/area-sweep/result_age34_Physical_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Physical_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Physical_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age34_Physical_k07.json) / [last](raw/api/area-sweep/result_age34_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=5.27, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age34_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age34_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Cognitive_k03.json) |
| 4–5 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age34_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age34_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age34_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age34_Cognitive_k09.json) |

#### Language (n=11, Σ rates=6.75, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age34_Language_k00.json) |
| 1–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age34_Language_k01.json) / [last](raw/api/area-sweep/result_age34_Language_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Language_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Language_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Language_k07.json) |
| 8 | 60 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Language_k08.json) |
| 9–11 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age34_Language_k09.json) / [last](raw/api/area-sweep/result_age34_Language_k11.json) |

#### Social-Emotional (n=10, Σ rates=6.26, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age34_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age34_Social-Emotional_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Social-Emotional_k04.json) |
| 5–6 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age34_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age34_Social-Emotional_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Social-Emotional_k07.json) |
| 8 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age34_Social-Emotional_k08.json) |
| 9–10 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age34_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age34_Social-Emotional_k10.json) |

### Age 35

#### Physical (n=9, Σ rates=5.25, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age35_Physical_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Physical_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Physical_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Physical_k03.json) |
| 4 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Physical_k04.json) |
| 5 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Physical_k05.json) |
| 6 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Physical_k06.json) |
| 7–9 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age35_Physical_k07.json) / [last](raw/api/area-sweep/result_age35_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=5.47, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age35_Cognitive_k00.json) |
| 1–2 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age35_Cognitive_k01.json) / [last](raw/api/area-sweep/result_age35_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Cognitive_k03.json) |
| 4–5 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age35_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age35_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age35_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age35_Cognitive_k09.json) |

#### Language (n=11, Σ rates=6.95, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age35_Language_k00.json) / [last](raw/api/area-sweep/result_age35_Language_k02.json) |
| 3–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age35_Language_k03.json) / [last](raw/api/area-sweep/result_age35_Language_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Language_k05.json) |
| 6 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Language_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Language_k07.json) |
| 8–11 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age35_Language_k08.json) / [last](raw/api/area-sweep/result_age35_Language_k11.json) |

#### Social-Emotional (n=10, Σ rates=6.41, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age35_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age35_Social-Emotional_k01.json) |
| 2 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Social-Emotional_k02.json) |
| 3 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Social-Emotional_k03.json) |
| 4 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Social-Emotional_k04.json) |
| 5–6 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age35_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age35_Social-Emotional_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Social-Emotional_k07.json) |
| 8 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age35_Social-Emotional_k08.json) |
| 9–10 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age35_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age35_Social-Emotional_k10.json) |

### Age 36

#### Physical (n=9, Σ rates=5.10, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age36_Physical_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Physical_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Physical_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Physical_k03.json) |
| 4 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Physical_k04.json) |
| 5 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Physical_k05.json) |
| 6 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Physical_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age36_Physical_k07.json) / [last](raw/api/area-sweep/result_age36_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=5.43, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age36_Cognitive_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Cognitive_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Cognitive_k03.json) |
| 4–5 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age36_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age36_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age36_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age36_Cognitive_k09.json) |

#### Language (n=11, Σ rates=6.87, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age36_Language_k00.json) / [last](raw/api/area-sweep/result_age36_Language_k02.json) |
| 3–5 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age36_Language_k03.json) / [last](raw/api/area-sweep/result_age36_Language_k05.json) |
| 6 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Language_k06.json) |
| 7 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Language_k07.json) |
| 8 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Language_k08.json) |
| 9–11 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age36_Language_k09.json) / [last](raw/api/area-sweep/result_age36_Language_k11.json) |

#### Social-Emotional (n=10, Σ rates=6.52, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age36_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age36_Social-Emotional_k02.json) |
| 3 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Social-Emotional_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Social-Emotional_k04.json) |
| 5–6 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age36_Social-Emotional_k05.json) / [last](raw/api/area-sweep/result_age36_Social-Emotional_k06.json) |
| 7 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Social-Emotional_k07.json) |
| 8 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age36_Social-Emotional_k08.json) |
| 9–10 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age36_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age36_Social-Emotional_k10.json) |

### Age 37

#### Physical (n=9, Σ rates=5.10, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age37_Physical_k00.json) / [last](raw/api/area-sweep/result_age37_Physical_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Physical_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Physical_k03.json) |
| 4 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Physical_k04.json) |
| 5 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Physical_k05.json) |
| 6 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Physical_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age37_Physical_k07.json) / [last](raw/api/area-sweep/result_age37_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=5.95, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age37_Cognitive_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Cognitive_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Cognitive_k03.json) |
| 4 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Cognitive_k04.json) |
| 5 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age37_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age37_Cognitive_k09.json) |

#### Language (n=9, Σ rates=6.42, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age37_Language_k00.json) |
| 1–4 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age37_Language_k01.json) / [last](raw/api/area-sweep/result_age37_Language_k04.json) |
| 5 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Language_k05.json) |
| 6 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Language_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age37_Language_k07.json) / [last](raw/api/area-sweep/result_age37_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=6.51, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age37_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age37_Social-Emotional_k01.json) |
| 2–3 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age37_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age37_Social-Emotional_k03.json) |
| 4 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Social-Emotional_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Social-Emotional_k05.json) |
| 6 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Social-Emotional_k06.json) |
| 7 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age37_Social-Emotional_k07.json) |
| 8–9 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age37_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age37_Social-Emotional_k09.json) |

### Age 38

#### Physical (n=9, Σ rates=5.13, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age38_Physical_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Physical_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Physical_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Physical_k03.json) |
| 4 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Physical_k04.json) |
| 5 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Physical_k05.json) |
| 6 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Physical_k06.json) |
| 7–9 | 46 | true | ok / ok | [first](raw/api/area-sweep/result_age38_Physical_k07.json) / [last](raw/api/area-sweep/result_age38_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=6.30, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age38_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age38_Cognitive_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Cognitive_k03.json) |
| 4 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Cognitive_k04.json) |
| 5 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age38_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age38_Cognitive_k09.json) |

#### Language (n=9, Σ rates=5.97, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age38_Language_k00.json) / [last](raw/api/area-sweep/result_age38_Language_k01.json) |
| 2–4 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age38_Language_k02.json) / [last](raw/api/area-sweep/result_age38_Language_k04.json) |
| 5 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Language_k05.json) |
| 6 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Language_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age38_Language_k07.json) / [last](raw/api/area-sweep/result_age38_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=6.42, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age38_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age38_Social-Emotional_k01.json) |
| 2–3 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age38_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age38_Social-Emotional_k03.json) |
| 4 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Social-Emotional_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Social-Emotional_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Social-Emotional_k06.json) |
| 7 | 42 | false | ok / ok | [raw](raw/api/area-sweep/result_age38_Social-Emotional_k07.json) |
| 8–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age38_Social-Emotional_k08.json) / [last](raw/api/area-sweep/result_age38_Social-Emotional_k09.json) |

### Age 39

#### Physical (n=11, Σ rates=6.87, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age39_Physical_k00.json) / [last](raw/api/area-sweep/result_age39_Physical_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Physical_k03.json) |
| 4 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Physical_k04.json) |
| 5 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Physical_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Physical_k06.json) |
| 7 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Physical_k07.json) |
| 8–11 | 46 | true | ok / ok | [first](raw/api/area-sweep/result_age39_Physical_k08.json) / [last](raw/api/area-sweep/result_age39_Physical_k11.json) |

#### Cognitive (n=9, Σ rates=6.44, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age39_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age39_Cognitive_k01.json) |
| 2–3 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age39_Cognitive_k02.json) / [last](raw/api/area-sweep/result_age39_Cognitive_k03.json) |
| 4–5 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age39_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age39_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age39_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age39_Cognitive_k09.json) |

#### Language (n=7, Σ rates=4.68, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age39_Language_k00.json) |
| 1–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age39_Language_k01.json) / [last](raw/api/area-sweep/result_age39_Language_k07.json) |

#### Social-Emotional (n=9, Σ rates=6.31, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age39_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age39_Social-Emotional_k01.json) |
| 2 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Social-Emotional_k02.json) |
| 3 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Social-Emotional_k03.json) |
| 4 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Social-Emotional_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Social-Emotional_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age39_Social-Emotional_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age39_Social-Emotional_k07.json) / [last](raw/api/area-sweep/result_age39_Social-Emotional_k09.json) |

### Age 40

#### Physical (n=11, Σ rates=7.11, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age40_Physical_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Physical_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Physical_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Physical_k03.json) |
| 4 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Physical_k04.json) |
| 5 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Physical_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Physical_k06.json) |
| 7 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Physical_k07.json) |
| 8–11 | 46 | true | ok / ok | [first](raw/api/area-sweep/result_age40_Physical_k08.json) / [last](raw/api/area-sweep/result_age40_Physical_k11.json) |

#### Cognitive (n=9, Σ rates=6.69, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age40_Cognitive_k00.json) |
| 1 | 20 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Cognitive_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Cognitive_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Cognitive_k03.json) |
| 4 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Cognitive_k04.json) |
| 5 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age40_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age40_Cognitive_k09.json) |

#### Language (n=7, Σ rates=5.00, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age40_Language_k00.json) / [last](raw/api/area-sweep/result_age40_Language_k07.json) |

#### Social-Emotional (n=9, Σ rates=6.48, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age40_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age40_Social-Emotional_k02.json) |
| 3 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Social-Emotional_k03.json) |
| 4 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Social-Emotional_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Social-Emotional_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age40_Social-Emotional_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age40_Social-Emotional_k07.json) / [last](raw/api/area-sweep/result_age40_Social-Emotional_k09.json) |

### Age 41

#### Physical (n=11, Σ rates=7.29, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age41_Physical_k00.json) / [last](raw/api/area-sweep/result_age41_Physical_k01.json) |
| 2 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Physical_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Physical_k03.json) |
| 4–5 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age41_Physical_k04.json) / [last](raw/api/area-sweep/result_age41_Physical_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Physical_k06.json) |
| 7 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Physical_k07.json) |
| 8–11 | 46 | true | ok / ok | [first](raw/api/area-sweep/result_age41_Physical_k08.json) / [last](raw/api/area-sweep/result_age41_Physical_k11.json) |

#### Cognitive (n=9, Σ rates=6.72, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age41_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age41_Cognitive_k01.json) |
| 2–3 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age41_Cognitive_k02.json) / [last](raw/api/area-sweep/result_age41_Cognitive_k03.json) |
| 4–5 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age41_Cognitive_k04.json) / [last](raw/api/area-sweep/result_age41_Cognitive_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Cognitive_k06.json) |
| 7–9 | 40 | true | ok / ok | [first](raw/api/area-sweep/result_age41_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age41_Cognitive_k09.json) |

#### Language (n=7, Σ rates=5.17, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age41_Language_k00.json) / [last](raw/api/area-sweep/result_age41_Language_k07.json) |

#### Social-Emotional (n=9, Σ rates=6.62, baseline K=7)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age41_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age41_Social-Emotional_k01.json) |
| 2 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Social-Emotional_k02.json) |
| 3 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Social-Emotional_k03.json) |
| 4 | 30 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Social-Emotional_k04.json) |
| 5 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Social-Emotional_k05.json) |
| 6 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age41_Social-Emotional_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age41_Social-Emotional_k07.json) / [last](raw/api/area-sweep/result_age41_Social-Emotional_k09.json) |

### Age 42

#### Physical (n=9, Σ rates=5.65, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age42_Physical_k00.json) / [last](raw/api/area-sweep/result_age42_Physical_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Physical_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Physical_k03.json) |
| 4 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Physical_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Physical_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Physical_k06.json) |
| 7–9 | 46 | true | ok / ok | [first](raw/api/area-sweep/result_age42_Physical_k07.json) / [last](raw/api/area-sweep/result_age42_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=6.18, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age42_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age42_Cognitive_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Cognitive_k02.json) |
| 3–4 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age42_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age42_Cognitive_k04.json) |
| 5 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Cognitive_k05.json) |
| 6 | 42 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Cognitive_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age42_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age42_Cognitive_k09.json) |

#### Language (n=9, Σ rates=5.78, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 26 | false | ok / ok | [first](raw/api/area-sweep/result_age42_Language_k00.json) / [last](raw/api/area-sweep/result_age42_Language_k03.json) |
| 4 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Language_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Language_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Language_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age42_Language_k07.json) / [last](raw/api/area-sweep/result_age42_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.47, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age42_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age42_Social-Emotional_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Social-Emotional_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Social-Emotional_k03.json) |
| 4 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Social-Emotional_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Social-Emotional_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age42_Social-Emotional_k06.json) |
| 7–9 | 52 | true | ok / ok | [first](raw/api/area-sweep/result_age42_Social-Emotional_k07.json) / [last](raw/api/area-sweep/result_age42_Social-Emotional_k09.json) |

### Age 43

#### Physical (n=9, Σ rates=6.11, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 20 | false | ok / ok | [first](raw/api/area-sweep/result_age43_Physical_k00.json) / [last](raw/api/area-sweep/result_age43_Physical_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Physical_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Physical_k03.json) |
| 4 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Physical_k04.json) |
| 5 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Physical_k05.json) |
| 6 | 42 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Physical_k06.json) |
| 7–9 | 46 | true | ok / ok | [first](raw/api/area-sweep/result_age43_Physical_k07.json) / [last](raw/api/area-sweep/result_age43_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=6.14, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age43_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age43_Cognitive_k01.json) |
| 2 | 26 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Cognitive_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Cognitive_k03.json) |
| 4 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Cognitive_k04.json) |
| 5 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Cognitive_k05.json) |
| 6 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Cognitive_k06.json) |
| 7–9 | 42 | true | ok / ok | [first](raw/api/area-sweep/result_age43_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age43_Cognitive_k09.json) |

#### Language (n=9, Σ rates=5.90, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 26 | false | ok / ok | [first](raw/api/area-sweep/result_age43_Language_k00.json) / [last](raw/api/area-sweep/result_age43_Language_k03.json) |
| 4 | 34 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Language_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Language_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Language_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age43_Language_k07.json) / [last](raw/api/area-sweep/result_age43_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.70, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | 22 | false | ok / ok | [first](raw/api/area-sweep/result_age43_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age43_Social-Emotional_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Social-Emotional_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Social-Emotional_k03.json) |
| 4 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Social-Emotional_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Social-Emotional_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age43_Social-Emotional_k06.json) |
| 7–9 | 52 | true | ok / ok | [first](raw/api/area-sweep/result_age43_Social-Emotional_k07.json) / [last](raw/api/area-sweep/result_age43_Social-Emotional_k09.json) |

### Age 44

#### Physical (n=9, Σ rates=5.87, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age44_Physical_k00.json) |
| 1 | 24 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Physical_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Physical_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Physical_k03.json) |
| 4 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Physical_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Physical_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Physical_k06.json) |
| 7–9 | 46 | true | ok / ok | [first](raw/api/area-sweep/result_age44_Physical_k07.json) / [last](raw/api/area-sweep/result_age44_Physical_k09.json) |

#### Cognitive (n=9, Σ rates=6.19, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age44_Cognitive_k00.json) |
| 1 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Cognitive_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Cognitive_k02.json) |
| 3–4 | 32 | false | ok / ok | [first](raw/api/area-sweep/result_age44_Cognitive_k03.json) / [last](raw/api/area-sweep/result_age44_Cognitive_k04.json) |
| 5 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Cognitive_k05.json) |
| 6 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Cognitive_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age44_Cognitive_k07.json) / [last](raw/api/area-sweep/result_age44_Cognitive_k09.json) |

#### Language (n=9, Σ rates=6.16, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age44_Language_k00.json) |
| 1–3 | 24 | false | ok / ok | [first](raw/api/area-sweep/result_age44_Language_k01.json) / [last](raw/api/area-sweep/result_age44_Language_k03.json) |
| 4 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Language_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Language_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Language_k06.json) |
| 7–9 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age44_Language_k07.json) / [last](raw/api/area-sweep/result_age44_Language_k09.json) |

#### Social-Emotional (n=9, Σ rates=5.83, baseline K=6)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age44_Social-Emotional_k00.json) |
| 1 | 22 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Social-Emotional_k01.json) |
| 2 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Social-Emotional_k02.json) |
| 3 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Social-Emotional_k03.json) |
| 4 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Social-Emotional_k04.json) |
| 5 | 40 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Social-Emotional_k05.json) |
| 6 | 44 | false | ok / ok | [raw](raw/api/area-sweep/result_age44_Social-Emotional_k06.json) |
| 7–9 | 52 | true | ok / ok | [first](raw/api/area-sweep/result_age44_Social-Emotional_k07.json) / [last](raw/api/area-sweep/result_age44_Social-Emotional_k09.json) |

### Age 45

#### Physical (n=7, Σ rates=4.55, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age45_Physical_k00.json) / [last](raw/api/area-sweep/result_age45_Physical_k07.json) |

#### Cognitive (n=7, Σ rates=4.76, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age45_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age45_Cognitive_k07.json) |

#### Language (n=8, Σ rates=5.44, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | 28 | false | ok / ok | [first](raw/api/area-sweep/result_age45_Language_k00.json) / [last](raw/api/area-sweep/result_age45_Language_k03.json) |
| 4 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Language_k04.json) |
| 5 | 42 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Language_k05.json) |
| 6–8 | 44 | true | ok / ok | [first](raw/api/area-sweep/result_age45_Language_k06.json) / [last](raw/api/area-sweep/result_age45_Language_k08.json) |

#### Social-Emotional (n=11, Σ rates=7.71, baseline K=8)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–2 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age45_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age45_Social-Emotional_k02.json) |
| 3 | 28 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Social-Emotional_k03.json) |
| 4 | 32 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Social-Emotional_k04.json) |
| 5 | 36 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Social-Emotional_k05.json) |
| 6 | 38 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Social-Emotional_k06.json) |
| 7 | 42 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Social-Emotional_k07.json) |
| 8 | 48 | false | ok / ok | [raw](raw/api/area-sweep/result_age45_Social-Emotional_k08.json) |
| 9–11 | 52 | true | ok / ok | [first](raw/api/area-sweep/result_age45_Social-Emotional_k09.json) / [last](raw/api/area-sweep/result_age45_Social-Emotional_k11.json) |

### Age 46

#### Physical (n=7, Σ rates=4.72, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age46_Physical_k00.json) |
| 1–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age46_Physical_k01.json) / [last](raw/api/area-sweep/result_age46_Physical_k07.json) |

#### Cognitive (n=6, Σ rates=4.03, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–6 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age46_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age46_Cognitive_k06.json) |

#### Language (n=7, Σ rates=4.82, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age46_Language_k00.json) |
| 1–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age46_Language_k01.json) / [last](raw/api/area-sweep/result_age46_Language_k07.json) |

#### Social-Emotional (n=7, Σ rates=4.53, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age46_Social-Emotional_k00.json) |
| 1–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age46_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age46_Social-Emotional_k07.json) |

### Age 47

#### Physical (n=7, Σ rates=4.76, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age47_Physical_k00.json) |
| 1–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age47_Physical_k01.json) / [last](raw/api/area-sweep/result_age47_Physical_k07.json) |

#### Cognitive (n=4, Σ rates=2.68, baseline K=3)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–4 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age47_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age47_Cognitive_k04.json) |

#### Language (n=6, Σ rates=4.24, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–6 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age47_Language_k00.json) / [last](raw/api/area-sweep/result_age47_Language_k06.json) |

#### Social-Emotional (n=7, Σ rates=4.67, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age47_Social-Emotional_k00.json) |
| 1–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age47_Social-Emotional_k01.json) / [last](raw/api/area-sweep/result_age47_Social-Emotional_k07.json) |

### Age 48

#### Physical (n=6, Σ rates=4.15, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age48_Physical_k00.json) |
| 1–6 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age48_Physical_k01.json) / [last](raw/api/area-sweep/result_age48_Physical_k06.json) |

#### Cognitive (n=3, Σ rates=1.97, baseline K=2)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–3 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age48_Cognitive_k00.json) / [last](raw/api/area-sweep/result_age48_Cognitive_k03.json) |

#### Language (n=6, Σ rates=4.13, baseline K=4)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0 | — | — | — / below_floor | [raw](raw/api/area-sweep/result_age48_Language_k00.json) |
| 1–6 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age48_Language_k01.json) / [last](raw/api/area-sweep/result_age48_Language_k06.json) |

#### Social-Emotional (n=7, Σ rates=4.66, baseline K=5)

| K | Months | atLeast | State (area / headline) | Evidence |
| --- | --- | --- | --- | --- |
| 0–1 | — | — | — / below_floor | [first](raw/api/area-sweep/result_age48_Social-Emotional_k00.json) / [last](raw/api/area-sweep/result_age48_Social-Emotional_k01.json) |
| 2–7 | — | — | not_enough / ok | [first](raw/api/area-sweep/result_age48_Social-Emotional_k02.json) / [last](raw/api/area-sweep/result_age48_Social-Emotional_k07.json) |
