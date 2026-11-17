# Kinedu AQ: full Yes-count → headline table (Phase 5)

**COMPLETED: 1886/1886 requests; 1886/1886 complete reports.** Coverage is 49/49 full ages. All requested reports collected.

Observed means a saved response, with the exact served ID set and cumulative ascending `(rate, id)` Yes vector. Every numeric cell comes from that response; missing ages and flags remain empty in the CSV and appear as — here. `below_floor` is a returned state, not age zero. The 1,886-row CSV also keeps uncollected combinations as `not_collected`, without invented scores.

## Collection and evidence

Only POST `https://webpromo.kinedu.com/api/assessment` with `action:result`, `extended:true`, numeric 0/1 answers, and the exact User-Agent, Content-Type, Origin and Referer in [ENUMERATION.md](ENUMERATION.md) was used. Initial lists were indexed by returned `ageMonths` from `start_age*_gw-null.json`. Each section's anchor and items, followed by calibration items, supplies the complete unique ID set; sorting by ascending `(rate,id)` determines the cumulative vector. No other endpoint was called.

Sequential calls slept 2.0 seconds before every request. Observed minimum response-completion to next request-start interval: **2.001633s**. HTTP counts: **200=1886**; transport failures: **0**. UTC interval: 2026-11-02T21:46:40.176778+00:00 to 2026-11-02T22:58:46.823652+00:00.

Raw responses and `.json.headers.txt` headers are immutable in [raw/api/scoring-all/](raw/api/scoring-all/). The [manifest](raw/api/scoring-all/requests.jsonl) records timestamp, age, N, K, status, request payload, curl outcome, source and response hashes. The offline builder verifies body/header/source hashes, HTTP headers, exact vectors, pacing, and the three-failure abort rule. It never requests the network. See [audit](logs/phase5-validation.json) and [CSV](scoring-table.csv).

An existing manifested file is verified and skipped on resume. Unmanifested files are preserved and stop collection for offline reconciliation. Three consecutive HTTP 429, 403, 5xx or transport failures stop collection immediately; the persisted streak prevents automatic restart calls.

## Summary by returned age

First-K columns require all lower K values to have observed reports. `none` means absent across the complete age sweep; `unknown` means collection is incomplete. The capped-age column lists every observed numeric devAge with `capped:true`.

| Age A | N | Σ served rates | First K: devAge=A | Min K: not below_floor | First K: capped | Capped devAge | Reports |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 39 | 20.70 | none | 22 | 37 | 20 | 40/40 |
| 1 | 39 | 19.70 | 0 | 0 | 37 | 32 | 40/40 |
| 2 | 39 | 19.10 | 19 | 19 | 37 | 19 | 40/40 |
| 3 | 39 | 19.91 | 19 | 19 | 37 | 18 | 40/40 |
| 4 | 39 | 20.75 | 19 | 19 | 36 | 28 | 40/40 |
| 5 | 39 | 21.53 | 19 | 19 | 36 | 32 | 40/40 |
| 6 | 39 | 22.74 | 21 | 21 | 36 | 31 | 40/40 |
| 7 | 39 | 21.76 | 21 | 18 | 36 | 20 | 40/40 |
| 8 | 39 | 22.43 | 21 | 17 | 36 | 33 | 40/40 |
| 9 | 39 | 21.38 | 20 | 17 | 36 | 36 | 40/40 |
| 10 | 39 | 20.73 | 19 | 16 | 35 | 40 | 40/40 |
| 11 | 39 | 20.91 | 20 | 16 | 36 | 34 | 40/40 |
| 12 | 39 | 22.41 | 21 | 17 | 35 | 33 | 40/40 |
| 13 | 39 | 20.50 | 19 | 16 | 34 | 31 | 40/40 |
| 14 | 39 | 21.75 | 21 | 16 | 35 | 26 | 40/40 |
| 15 | 39 | 22.38 | 21 | 16 | 35 | 38 | 40/40 |
| 16 | 39 | 22.01 | 21 | 16 | 34 | 34 | 40/40 |
| 17 | 39 | 22.10 | 21 | 16 | 34 | 33 | 40/40 |
| 18 | 39 | 24.13 | 23 | 18 | 33 | 40 | 40/40 |
| 19 | 39 | 23.30 | 23 | 17 | 32 | 34 | 40/40 |
| 20 | 39 | 21.97 | 22 | 15 | 33 | 41 | 40/40 |
| 21 | 39 | 21.08 | 20 | 15 | 33 | 42 | 40/40 |
| 22 | 39 | 21.69 | 21 | 16 | 32 | 43 | 40/40 |
| 23 | 39 | 21.57 | 21 | 15 | 33 | 44 | 40/40 |
| 24 | 39 | 21.80 | 22 | 16 | 32 | 44 | 40/40 |
| 25 | 39 | 22.29 | 22 | 18 | 32 | 44 | 40/40 |
| 26 | 39 | 21.90 | 22 | 18 | 31 | 44 | 40/40 |
| 27 | 39 | 22.36 | 22 | 17 | 31 | 44 | 40/40 |
| 28 | 39 | 22.37 | 23 | 18 | 31 | 44 | 40/40 |
| 29 | 39 | 22.94 | 23 | 19 | 31 | 44 | 40/40 |
| 30 | 39 | 24.07 | 24 | 20 | 32 | 44 | 40/40 |
| 31 | 39 | 22.56 | 22 | 18 | 32 | 44 | 40/40 |
| 32 | 39 | 22.73 | 22 | 18 | 32 | 46 | 40/40 |
| 33 | 39 | 23.07 | 23 | 18 | 31 | 46 | 40/40 |
| 34 | 39 | 23.85 | 24 | 18 | 31 | 46 | 40/40 |
| 35 | 39 | 24.08 | 24 | 19 | 31 | 46 | 40/40 |
| 36 | 39 | 23.92 | 24 | 20 | 31 | 46 | 40/40 |
| 37 | 36 | 23.98 | 24 | 19 | 29 | 45 | 37/37 |
| 38 | 36 | 23.82 | 24 | 19 | 28 | 46 | 37/37 |
| 39 | 36 | 24.30 | 24 | 20 | 28 | 46 | 37/37 |
| 40 | 36 | 25.28 | 25 | 19 | 28 | 46 | 37/37 |
| 41 | 36 | 25.80 | 26 | 21 | 28 | 46 | 37/37 |
| 42 | 36 | 23.08 | 23 | 17 | 27 | 53 | 37/37 |
| 43 | 36 | 23.85 | 24 | 18 | 27 | 53 | 37/37 |
| 44 | 36 | 24.05 | 24 | 19 | 27 | 53 | 37/37 |
| 45 | 33 | 22.46 | none | 18 | 25 | 53 | 34/34 |
| 46 | 27 | 18.10 | 18 | 15 | 20 | 53 | 28/28 |
| 47 | 24 | 16.35 | none | 13 | 17 | 53 | 25/25 |
| 48 | 22 | 14.91 | none | 12 | 16 | 53 | 23/23 |

## Rounded expected Yes count

At K = round(Σ served rates), devAge equals A in **44/49 observed ages**. There are **5 observed exceptions** and **0 unmeasured ages**. The relation does not hold for every age 0–48.

Rounding uses the exact decimal sum of saved rates and nearest integer, with .5 ties to even (Python's `round` convention). This avoids a binary floating-point summation artifact. The alternative .5-up result is shown for every exact tie below. The rounded local rates do not reveal the server's underlying norm curves.

| Age | Σ rates | K | Returned state | Returned devAge | Evidence |
| --- | --- | --- | --- | --- | --- |
| 0 | 20.70 | 21 | below_floor | — | [raw](raw/api/scoring-all/result_age00_k21.json) |
| 28 | 22.37 | 22 | ok | 27 | [raw](raw/api/scoring-all/result_age28_k22.json) |
| 45 | 22.46 | 22 | ok | 44 | [raw](raw/api/scoring-all/result_age45_k22.json) |
| 47 | 16.35 | 16 | ok | 46 | [raw](raw/api/scoring-all/result_age47_k16.json) |
| 48 | 14.91 | 15 | ok | 47 | [raw](raw/api/scoring-all/result_age48_k15.json) |

| Age | Σ rates | Ties-even K | devAge | .5-up K | .5-up devAge | .5-up observation |
| --- | --- | --- | --- | --- | --- | --- |
| 13 | 20.50 | 20 | 13 | 21 | 13 | observed_report |

## Band formula check

For every new numeric report, compute `r = devAge / max(A,1)`: `r > 1.15` → `well_ahead`; else `r > 1.05` → `little_ahead`; else `r >= 0.95` → `on_pace`; else `building`. Observed matches: **1042/1042**. Mismatches: **0**. The denominator includes only Phase 5 HTTP-200 complete numeric reports, and excludes below-floor responses, failures and uncollected combinations.

Band mismatches: none observed.

## Monotonicity

Ages with any decreasing numeric devAge as K increases: **16, 23, 25, 30, 32**. This compares consecutive observed numeric reports for each age, including across gaps; omitted ages in below-floor reports have no numeric value to compare. Complete-sweep coverage: 49/49 ages.

| Age | From K | To K | From devAge | To devAge |
| --- | --- | --- | --- | --- |
| 16 | 33 | 34 | 36 | 34 |
| 23 | 32 | 33 | 56 | 44 |
| 25 | 31 | 32 | 60 | 44 |
| 30 | 31 | 32 | 60 | 44 |
| 32 | 31 | 32 | 51 | 46 |

Numeric-to-below_floor transitions at adjacent K: [{"age": 1, "from_K": 20, "to_K": 21}].

## How to rebuild the headline score

1. Choose the served list whose returned ageMonths equals the child's effective assessment age A. Flatten its section anchors/items and calibration entries, keeping each ID once.

2. Collect one numeric Yes/No answer for every ID in that exact list. Count the Yes answers to obtain K. Use row (A,K) in scoring-table.csv, or the K range in the age table below.

3. Return that row's stage, state, devAge, band and capped flag exactly. An omitted devAge stays omitted; a cap is part of the measured result. Do not interpolate or replace a missing row.

4. These are the headline outputs with extended:true. Extending the answered ID set changes the scoring context and is outside this lookup. Area months, atLeast flags, skills and activity can depend on which answers are Yes; do not reproduce them from global K alone.

**Observed versus inferred:** these tables directly measure one cumulative vector per K. Applying a row to every other answer arrangement with the same served IDs and K uses the Phase 3 count-sufficiency finding (40/40 reversed-order and 6/6 randomized age-12 controls). This phase does not independently test all answer arrangements at every age. The lookup reproduces measured behavior; it does not recover hidden norm tables or establish validity. The four area columns and their atLeast flags in the CSV are observations for the specific ascending-rate vector only.

## Per-age headline lookups

Rows collapse consecutive K only when stage, state, devAge, band and capped are identical. Each range links its first and last raw response; every individual observation is in the CSV. — means not returned. Unknown/failure rows are explicitly labeled.

### Age 0 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–21 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age00_k00.json) … [K=21](raw/api/scoring-all/result_age00_k21.json) |
| 22–25 | ok | 1 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age00_k22.json) … [K=25](raw/api/scoring-all/result_age00_k25.json) |
| 26–29 | ok | 2 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age00_k26.json) … [K=29](raw/api/scoring-all/result_age00_k29.json) |
| 30–31 | ok | 3 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age00_k30.json) … [K=31](raw/api/scoring-all/result_age00_k31.json) |
| 32–33 | ok | 4 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age00_k32.json) … [K=33](raw/api/scoring-all/result_age00_k33.json) |
| 34 | ok | 5 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age00_k34.json) |
| 35 | ok | 7 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age00_k35.json) |
| 36 | ok | 13 | well_ahead | false | complete | [K=36](raw/api/scoring-all/result_age00_k36.json) |
| 37–39 | ok | 20 | well_ahead | true | complete | [K=37](raw/api/scoring-all/result_age00_k37.json) … [K=39](raw/api/scoring-all/result_age00_k39.json) |

### Age 1 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–20 | ok | 1 | on_pace | false | complete | [K=0](raw/api/scoring-all/result_age01_k00.json) … [K=20](raw/api/scoring-all/result_age01_k20.json) |
| 21 | below_floor | — | — | — | complete | [K=21](raw/api/scoring-all/result_age01_k21.json) |
| 22–23 | ok | 2 | well_ahead | false | complete | [K=22](raw/api/scoring-all/result_age01_k22.json) … [K=23](raw/api/scoring-all/result_age01_k23.json) |
| 24–26 | ok | 3 | well_ahead | false | complete | [K=24](raw/api/scoring-all/result_age01_k24.json) … [K=26](raw/api/scoring-all/result_age01_k26.json) |
| 27–29 | ok | 4 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age01_k27.json) … [K=29](raw/api/scoring-all/result_age01_k29.json) |
| 30–31 | ok | 5 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age01_k30.json) … [K=31](raw/api/scoring-all/result_age01_k31.json) |
| 32 | ok | 6 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age01_k32.json) |
| 33 | ok | 7 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age01_k33.json) |
| 34 | ok | 8 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age01_k34.json) |
| 35 | ok | 13 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age01_k35.json) |
| 36 | ok | 23 | well_ahead | false | complete | [K=36](raw/api/scoring-all/result_age01_k36.json) |
| 37–39 | ok | 32 | well_ahead | true | complete | [K=37](raw/api/scoring-all/result_age01_k37.json) … [K=39](raw/api/scoring-all/result_age01_k39.json) |

### Age 2 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age02_k00.json) … [K=18](raw/api/scoring-all/result_age02_k18.json) |
| 19–21 | ok | 2 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age02_k19.json) … [K=21](raw/api/scoring-all/result_age02_k21.json) |
| 22–25 | ok | 3 | well_ahead | false | complete | [K=22](raw/api/scoring-all/result_age02_k22.json) … [K=25](raw/api/scoring-all/result_age02_k25.json) |
| 26–28 | ok | 4 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age02_k26.json) … [K=28](raw/api/scoring-all/result_age02_k28.json) |
| 29–30 | ok | 5 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age02_k29.json) … [K=30](raw/api/scoring-all/result_age02_k30.json) |
| 31–32 | ok | 6 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age02_k31.json) … [K=32](raw/api/scoring-all/result_age02_k32.json) |
| 33 | ok | 7 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age02_k33.json) |
| 34 | ok | 8 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age02_k34.json) |
| 35 | ok | 10 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age02_k35.json) |
| 36 | ok | 15 | well_ahead | false | complete | [K=36](raw/api/scoring-all/result_age02_k36.json) |
| 37–39 | ok | 19 | well_ahead | true | complete | [K=37](raw/api/scoring-all/result_age02_k37.json) … [K=39](raw/api/scoring-all/result_age02_k39.json) |

### Age 3 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age03_k00.json) … [K=18](raw/api/scoring-all/result_age03_k18.json) |
| 19–21 | ok | 3 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age03_k19.json) … [K=21](raw/api/scoring-all/result_age03_k21.json) |
| 22–25 | ok | 4 | well_ahead | false | complete | [K=22](raw/api/scoring-all/result_age03_k22.json) … [K=25](raw/api/scoring-all/result_age03_k25.json) |
| 26–28 | ok | 5 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age03_k26.json) … [K=28](raw/api/scoring-all/result_age03_k28.json) |
| 29–30 | ok | 6 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age03_k29.json) … [K=30](raw/api/scoring-all/result_age03_k30.json) |
| 31–32 | ok | 7 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age03_k31.json) … [K=32](raw/api/scoring-all/result_age03_k32.json) |
| 33 | ok | 8 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age03_k33.json) |
| 34 | ok | 9 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age03_k34.json) |
| 35 | ok | 11 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age03_k35.json) |
| 36 | ok | 17 | well_ahead | false | complete | [K=36](raw/api/scoring-all/result_age03_k36.json) |
| 37–39 | ok | 18 | well_ahead | true | complete | [K=37](raw/api/scoring-all/result_age03_k37.json) … [K=39](raw/api/scoring-all/result_age03_k39.json) |

### Age 4 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age04_k00.json) … [K=18](raw/api/scoring-all/result_age04_k18.json) |
| 19–23 | ok | 4 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age04_k19.json) … [K=23](raw/api/scoring-all/result_age04_k23.json) |
| 24–27 | ok | 5 | well_ahead | false | complete | [K=24](raw/api/scoring-all/result_age04_k24.json) … [K=27](raw/api/scoring-all/result_age04_k27.json) |
| 28–30 | ok | 6 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age04_k28.json) … [K=30](raw/api/scoring-all/result_age04_k30.json) |
| 31–32 | ok | 7 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age04_k31.json) … [K=32](raw/api/scoring-all/result_age04_k32.json) |
| 33 | ok | 8 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age04_k33.json) |
| 34 | ok | 9 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age04_k34.json) |
| 35 | ok | 18 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age04_k35.json) |
| 36–39 | ok | 28 | well_ahead | true | complete | [K=36](raw/api/scoring-all/result_age04_k36.json) … [K=39](raw/api/scoring-all/result_age04_k39.json) |

### Age 5 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age05_k00.json) … [K=18](raw/api/scoring-all/result_age05_k18.json) |
| 19–24 | ok | 5 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age05_k19.json) … [K=24](raw/api/scoring-all/result_age05_k24.json) |
| 25–27 | ok | 6 | well_ahead | false | complete | [K=25](raw/api/scoring-all/result_age05_k25.json) … [K=27](raw/api/scoring-all/result_age05_k27.json) |
| 28–30 | ok | 7 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age05_k28.json) … [K=30](raw/api/scoring-all/result_age05_k30.json) |
| 31–32 | ok | 8 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age05_k31.json) … [K=32](raw/api/scoring-all/result_age05_k32.json) |
| 33 | ok | 9 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age05_k33.json) |
| 34 | ok | 15 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age05_k34.json) |
| 35 | ok | 19 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age05_k35.json) |
| 36–39 | ok | 32 | well_ahead | true | complete | [K=36](raw/api/scoring-all/result_age05_k36.json) … [K=39](raw/api/scoring-all/result_age05_k39.json) |

### Age 6 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–20 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age06_k00.json) … [K=20](raw/api/scoring-all/result_age06_k20.json) |
| 21–24 | ok | 6 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age06_k21.json) … [K=24](raw/api/scoring-all/result_age06_k24.json) |
| 25–27 | ok | 7 | well_ahead | false | complete | [K=25](raw/api/scoring-all/result_age06_k25.json) … [K=27](raw/api/scoring-all/result_age06_k27.json) |
| 28–30 | ok | 8 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age06_k28.json) … [K=30](raw/api/scoring-all/result_age06_k30.json) |
| 31–32 | ok | 9 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age06_k31.json) … [K=32](raw/api/scoring-all/result_age06_k32.json) |
| 33 | ok | 10 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age06_k33.json) |
| 34 | ok | 15 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age06_k34.json) |
| 35 | ok | 18 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age06_k35.json) |
| 36–39 | ok | 31 | well_ahead | true | complete | [K=36](raw/api/scoring-all/result_age06_k36.json) … [K=39](raw/api/scoring-all/result_age06_k39.json) |

### Age 7 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age07_k00.json) … [K=17](raw/api/scoring-all/result_age07_k17.json) |
| 18–20 | ok | 6 | building | false | complete | [K=18](raw/api/scoring-all/result_age07_k18.json) … [K=20](raw/api/scoring-all/result_age07_k20.json) |
| 21–24 | ok | 7 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age07_k21.json) … [K=24](raw/api/scoring-all/result_age07_k24.json) |
| 25–28 | ok | 8 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age07_k25.json) … [K=28](raw/api/scoring-all/result_age07_k28.json) |
| 29–30 | ok | 9 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age07_k29.json) … [K=30](raw/api/scoring-all/result_age07_k30.json) |
| 31 | ok | 10 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age07_k31.json) |
| 32 | ok | 11 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age07_k32.json) |
| 33 | ok | 12 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age07_k33.json) |
| 34 | ok | 15 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age07_k34.json) |
| 35 | ok | 19 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age07_k35.json) |
| 36–39 | ok | 20 | well_ahead | true | complete | [K=36](raw/api/scoring-all/result_age07_k36.json) … [K=39](raw/api/scoring-all/result_age07_k39.json) |

### Age 8 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–16 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age08_k00.json) … [K=16](raw/api/scoring-all/result_age08_k16.json) |
| 17–20 | ok | 7 | building | false | complete | [K=17](raw/api/scoring-all/result_age08_k17.json) … [K=20](raw/api/scoring-all/result_age08_k20.json) |
| 21–24 | ok | 8 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age08_k21.json) … [K=24](raw/api/scoring-all/result_age08_k24.json) |
| 25–27 | ok | 9 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age08_k25.json) … [K=27](raw/api/scoring-all/result_age08_k27.json) |
| 28–30 | ok | 10 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age08_k28.json) … [K=30](raw/api/scoring-all/result_age08_k30.json) |
| 31 | ok | 11 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age08_k31.json) |
| 32 | ok | 12 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age08_k32.json) |
| 33 | ok | 13 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age08_k33.json) |
| 34 | ok | 17 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age08_k34.json) |
| 35 | ok | 21 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age08_k35.json) |
| 36–39 | ok | 33 | well_ahead | true | complete | [K=36](raw/api/scoring-all/result_age08_k36.json) … [K=39](raw/api/scoring-all/result_age08_k39.json) |

### Age 9 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–16 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age09_k00.json) … [K=16](raw/api/scoring-all/result_age09_k16.json) |
| 17–19 | ok | 8 | building | false | complete | [K=17](raw/api/scoring-all/result_age09_k17.json) … [K=19](raw/api/scoring-all/result_age09_k19.json) |
| 20–23 | ok | 9 | on_pace | false | complete | [K=20](raw/api/scoring-all/result_age09_k20.json) … [K=23](raw/api/scoring-all/result_age09_k23.json) |
| 24–26 | ok | 10 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age09_k24.json) … [K=26](raw/api/scoring-all/result_age09_k26.json) |
| 27–29 | ok | 11 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age09_k27.json) … [K=29](raw/api/scoring-all/result_age09_k29.json) |
| 30 | ok | 12 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age09_k30.json) |
| 31 | ok | 13 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age09_k31.json) |
| 32 | ok | 14 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age09_k32.json) |
| 33 | ok | 17 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age09_k33.json) |
| 34 | ok | 20 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age09_k34.json) |
| 35 | ok | 34 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age09_k35.json) |
| 36–39 | ok | 36 | well_ahead | true | complete | [K=36](raw/api/scoring-all/result_age09_k36.json) … [K=39](raw/api/scoring-all/result_age09_k39.json) |

### Age 10 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age10_k00.json) … [K=15](raw/api/scoring-all/result_age10_k15.json) |
| 16–18 | ok | 9 | building | false | complete | [K=16](raw/api/scoring-all/result_age10_k16.json) … [K=18](raw/api/scoring-all/result_age10_k18.json) |
| 19–22 | ok | 10 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age10_k19.json) … [K=22](raw/api/scoring-all/result_age10_k22.json) |
| 23–26 | ok | 11 | little_ahead | false | complete | [K=23](raw/api/scoring-all/result_age10_k23.json) … [K=26](raw/api/scoring-all/result_age10_k26.json) |
| 27–28 | ok | 12 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age10_k27.json) … [K=28](raw/api/scoring-all/result_age10_k28.json) |
| 29–30 | ok | 13 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age10_k29.json) … [K=30](raw/api/scoring-all/result_age10_k30.json) |
| 31 | ok | 14 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age10_k31.json) |
| 32 | ok | 15 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age10_k32.json) |
| 33 | ok | 17 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age10_k33.json) |
| 34 | ok | 20 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age10_k34.json) |
| 35–39 | ok | 40 | well_ahead | true | complete | [K=35](raw/api/scoring-all/result_age10_k35.json) … [K=39](raw/api/scoring-all/result_age10_k39.json) |

### Age 11 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age11_k00.json) … [K=15](raw/api/scoring-all/result_age11_k15.json) |
| 16–19 | ok | 10 | building | false | complete | [K=16](raw/api/scoring-all/result_age11_k16.json) … [K=19](raw/api/scoring-all/result_age11_k19.json) |
| 20–22 | ok | 11 | on_pace | false | complete | [K=20](raw/api/scoring-all/result_age11_k20.json) … [K=22](raw/api/scoring-all/result_age11_k22.json) |
| 23–25 | ok | 12 | little_ahead | false | complete | [K=23](raw/api/scoring-all/result_age11_k23.json) … [K=25](raw/api/scoring-all/result_age11_k25.json) |
| 26–28 | ok | 13 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age11_k26.json) … [K=28](raw/api/scoring-all/result_age11_k28.json) |
| 29 | ok | 14 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age11_k29.json) |
| 30 | ok | 15 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age11_k30.json) |
| 31 | ok | 16 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age11_k31.json) |
| 32 | ok | 17 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age11_k32.json) |
| 33 | ok | 19 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age11_k33.json) |
| 34 | ok | 20 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age11_k34.json) |
| 35 | ok | 33 | well_ahead | false | complete | [K=35](raw/api/scoring-all/result_age11_k35.json) |
| 36–39 | ok | 34 | well_ahead | true | complete | [K=36](raw/api/scoring-all/result_age11_k36.json) … [K=39](raw/api/scoring-all/result_age11_k39.json) |

### Age 12 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–16 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age12_k00.json) … [K=16](raw/api/scoring-all/result_age12_k16.json) |
| 17–20 | ok | 11 | building | false | complete | [K=17](raw/api/scoring-all/result_age12_k17.json) … [K=20](raw/api/scoring-all/result_age12_k20.json) |
| 21–24 | ok | 12 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age12_k21.json) … [K=24](raw/api/scoring-all/result_age12_k24.json) |
| 25–27 | ok | 13 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age12_k25.json) … [K=27](raw/api/scoring-all/result_age12_k27.json) |
| 28–29 | ok | 14 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age12_k28.json) … [K=29](raw/api/scoring-all/result_age12_k29.json) |
| 30 | ok | 15 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age12_k30.json) |
| 31 | ok | 16 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age12_k31.json) |
| 32 | ok | 17 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age12_k32.json) |
| 33 | ok | 19 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age12_k33.json) |
| 34 | ok | 21 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age12_k34.json) |
| 35–39 | ok | 33 | well_ahead | true | complete | [K=35](raw/api/scoring-all/result_age12_k35.json) … [K=39](raw/api/scoring-all/result_age12_k39.json) |

### Age 13 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age13_k00.json) … [K=15](raw/api/scoring-all/result_age13_k15.json) |
| 16–18 | ok | 12 | building | false | complete | [K=16](raw/api/scoring-all/result_age13_k16.json) … [K=18](raw/api/scoring-all/result_age13_k18.json) |
| 19–21 | ok | 13 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age13_k19.json) … [K=21](raw/api/scoring-all/result_age13_k21.json) |
| 22–24 | ok | 14 | little_ahead | false | complete | [K=22](raw/api/scoring-all/result_age13_k22.json) … [K=24](raw/api/scoring-all/result_age13_k24.json) |
| 25–26 | ok | 15 | well_ahead | false | complete | [K=25](raw/api/scoring-all/result_age13_k25.json) … [K=26](raw/api/scoring-all/result_age13_k26.json) |
| 27–28 | ok | 16 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age13_k27.json) … [K=28](raw/api/scoring-all/result_age13_k28.json) |
| 29 | ok | 17 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age13_k29.json) |
| 30 | ok | 18 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age13_k30.json) |
| 31 | ok | 19 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age13_k31.json) |
| 32 | ok | 20 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age13_k32.json) |
| 33 | ok | 21 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age13_k33.json) |
| 34–39 | ok | 31 | well_ahead | true | complete | [K=34](raw/api/scoring-all/result_age13_k34.json) … [K=39](raw/api/scoring-all/result_age13_k39.json) |

### Age 14 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age14_k00.json) … [K=15](raw/api/scoring-all/result_age14_k15.json) |
| 16–17 | ok | 12 | building | false | complete | [K=16](raw/api/scoring-all/result_age14_k16.json) … [K=17](raw/api/scoring-all/result_age14_k17.json) |
| 18–20 | ok | 13 | building | false | complete | [K=18](raw/api/scoring-all/result_age14_k18.json) … [K=20](raw/api/scoring-all/result_age14_k20.json) |
| 21–23 | ok | 14 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age14_k21.json) … [K=23](raw/api/scoring-all/result_age14_k23.json) |
| 24–25 | ok | 15 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age14_k24.json) … [K=25](raw/api/scoring-all/result_age14_k25.json) |
| 26–27 | ok | 16 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age14_k26.json) … [K=27](raw/api/scoring-all/result_age14_k27.json) |
| 28–29 | ok | 17 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age14_k28.json) … [K=29](raw/api/scoring-all/result_age14_k29.json) |
| 30 | ok | 18 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age14_k30.json) |
| 31 | ok | 19 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age14_k31.json) |
| 32 | ok | 20 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age14_k32.json) |
| 33 | ok | 21 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age14_k33.json) |
| 34 | ok | 25 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age14_k34.json) |
| 35–39 | ok | 26 | well_ahead | true | complete | [K=35](raw/api/scoring-all/result_age14_k35.json) … [K=39](raw/api/scoring-all/result_age14_k39.json) |

### Age 15 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age15_k00.json) … [K=15](raw/api/scoring-all/result_age15_k15.json) |
| 16–18 | ok | 13 | building | false | complete | [K=16](raw/api/scoring-all/result_age15_k16.json) … [K=18](raw/api/scoring-all/result_age15_k18.json) |
| 19–20 | ok | 14 | building | false | complete | [K=19](raw/api/scoring-all/result_age15_k19.json) … [K=20](raw/api/scoring-all/result_age15_k20.json) |
| 21–23 | ok | 15 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age15_k21.json) … [K=23](raw/api/scoring-all/result_age15_k23.json) |
| 24–26 | ok | 16 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age15_k24.json) … [K=26](raw/api/scoring-all/result_age15_k26.json) |
| 27–28 | ok | 17 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age15_k27.json) … [K=28](raw/api/scoring-all/result_age15_k28.json) |
| 29 | ok | 18 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age15_k29.json) |
| 30 | ok | 19 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age15_k30.json) |
| 31 | ok | 20 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age15_k31.json) |
| 32 | ok | 21 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age15_k32.json) |
| 33 | ok | 24 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age15_k33.json) |
| 34 | ok | 35 | well_ahead | false | complete | [K=34](raw/api/scoring-all/result_age15_k34.json) |
| 35–39 | ok | 38 | well_ahead | true | complete | [K=35](raw/api/scoring-all/result_age15_k35.json) … [K=39](raw/api/scoring-all/result_age15_k39.json) |

### Age 16 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age16_k00.json) … [K=15](raw/api/scoring-all/result_age16_k15.json) |
| 16–17 | ok | 14 | building | false | complete | [K=16](raw/api/scoring-all/result_age16_k16.json) … [K=17](raw/api/scoring-all/result_age16_k17.json) |
| 18–20 | ok | 15 | building | false | complete | [K=18](raw/api/scoring-all/result_age16_k18.json) … [K=20](raw/api/scoring-all/result_age16_k20.json) |
| 21–23 | ok | 16 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age16_k21.json) … [K=23](raw/api/scoring-all/result_age16_k23.json) |
| 24–25 | ok | 17 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age16_k24.json) … [K=25](raw/api/scoring-all/result_age16_k25.json) |
| 26–27 | ok | 18 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age16_k26.json) … [K=27](raw/api/scoring-all/result_age16_k27.json) |
| 28–29 | ok | 19 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age16_k28.json) … [K=29](raw/api/scoring-all/result_age16_k29.json) |
| 30 | ok | 20 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age16_k30.json) |
| 31 | ok | 21 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age16_k31.json) |
| 32 | ok | 24 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age16_k32.json) |
| 33 | ok | 36 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age16_k33.json) |
| 34–39 | ok | 34 | well_ahead | true | complete | [K=34](raw/api/scoring-all/result_age16_k34.json) … [K=39](raw/api/scoring-all/result_age16_k39.json) |

### Age 17 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age17_k00.json) … [K=15](raw/api/scoring-all/result_age17_k15.json) |
| 16–18 | ok | 15 | building | false | complete | [K=16](raw/api/scoring-all/result_age17_k16.json) … [K=18](raw/api/scoring-all/result_age17_k18.json) |
| 19–20 | ok | 16 | building | false | complete | [K=19](raw/api/scoring-all/result_age17_k19.json) … [K=20](raw/api/scoring-all/result_age17_k20.json) |
| 21–23 | ok | 17 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age17_k21.json) … [K=23](raw/api/scoring-all/result_age17_k23.json) |
| 24–25 | ok | 18 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age17_k24.json) … [K=25](raw/api/scoring-all/result_age17_k25.json) |
| 26–27 | ok | 19 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age17_k26.json) … [K=27](raw/api/scoring-all/result_age17_k27.json) |
| 28–29 | ok | 20 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age17_k28.json) … [K=29](raw/api/scoring-all/result_age17_k29.json) |
| 30 | ok | 21 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age17_k30.json) |
| 31 | ok | 23 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age17_k31.json) |
| 32 | ok | 25 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age17_k32.json) |
| 33 | ok | 30 | well_ahead | false | complete | [K=33](raw/api/scoring-all/result_age17_k33.json) |
| 34–39 | ok | 33 | well_ahead | true | complete | [K=34](raw/api/scoring-all/result_age17_k34.json) … [K=39](raw/api/scoring-all/result_age17_k39.json) |

### Age 18 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age18_k00.json) … [K=17](raw/api/scoring-all/result_age18_k17.json) |
| 18–20 | ok | 16 | building | false | complete | [K=18](raw/api/scoring-all/result_age18_k18.json) … [K=20](raw/api/scoring-all/result_age18_k20.json) |
| 21–22 | ok | 17 | building | false | complete | [K=21](raw/api/scoring-all/result_age18_k21.json) … [K=22](raw/api/scoring-all/result_age18_k22.json) |
| 23–25 | ok | 18 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age18_k23.json) … [K=25](raw/api/scoring-all/result_age18_k25.json) |
| 26–27 | ok | 19 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age18_k26.json) … [K=27](raw/api/scoring-all/result_age18_k27.json) |
| 28 | ok | 20 | little_ahead | false | complete | [K=28](raw/api/scoring-all/result_age18_k28.json) |
| 29–30 | ok | 21 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age18_k29.json) … [K=30](raw/api/scoring-all/result_age18_k30.json) |
| 31 | ok | 23 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age18_k31.json) |
| 32 | ok | 27 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age18_k32.json) |
| 33–39 | ok | 40 | well_ahead | true | complete | [K=33](raw/api/scoring-all/result_age18_k33.json) … [K=39](raw/api/scoring-all/result_age18_k39.json) |

### Age 19 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–16 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age19_k00.json) … [K=16](raw/api/scoring-all/result_age19_k16.json) |
| 17–19 | ok | 17 | building | false | complete | [K=17](raw/api/scoring-all/result_age19_k17.json) … [K=19](raw/api/scoring-all/result_age19_k19.json) |
| 20–22 | ok | 18 | building | false | complete | [K=20](raw/api/scoring-all/result_age19_k20.json) … [K=22](raw/api/scoring-all/result_age19_k22.json) |
| 23–24 | ok | 19 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age19_k23.json) … [K=24](raw/api/scoring-all/result_age19_k24.json) |
| 25–26 | ok | 20 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age19_k25.json) … [K=26](raw/api/scoring-all/result_age19_k26.json) |
| 27–28 | ok | 21 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age19_k27.json) … [K=28](raw/api/scoring-all/result_age19_k28.json) |
| 29 | ok | 23 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age19_k29.json) |
| 30 | ok | 24 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age19_k30.json) |
| 31 | ok | 28 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age19_k31.json) |
| 32–39 | ok | 34 | well_ahead | true | complete | [K=32](raw/api/scoring-all/result_age19_k32.json) … [K=39](raw/api/scoring-all/result_age19_k39.json) |

### Age 20 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–14 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age20_k00.json) … [K=14](raw/api/scoring-all/result_age20_k14.json) |
| 15–16 | ok | 17 | building | false | complete | [K=15](raw/api/scoring-all/result_age20_k15.json) … [K=16](raw/api/scoring-all/result_age20_k16.json) |
| 17–18 | ok | 18 | building | false | complete | [K=17](raw/api/scoring-all/result_age20_k17.json) … [K=18](raw/api/scoring-all/result_age20_k18.json) |
| 19–21 | ok | 19 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age20_k19.json) … [K=21](raw/api/scoring-all/result_age20_k21.json) |
| 22–23 | ok | 20 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age20_k22.json) … [K=23](raw/api/scoring-all/result_age20_k23.json) |
| 24–25 | ok | 21 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age20_k24.json) … [K=25](raw/api/scoring-all/result_age20_k25.json) |
| 26 | ok | 22 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age20_k26.json) |
| 27 | ok | 23 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age20_k27.json) |
| 28 | ok | 24 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age20_k28.json) |
| 29 | ok | 25 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age20_k29.json) |
| 30 | ok | 27 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age20_k30.json) |
| 31 | ok | 31 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age20_k31.json) |
| 32 | ok | 37 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age20_k32.json) |
| 33–39 | ok | 41 | well_ahead | true | complete | [K=33](raw/api/scoring-all/result_age20_k33.json) … [K=39](raw/api/scoring-all/result_age20_k39.json) |

### Age 21 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–14 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age21_k00.json) … [K=14](raw/api/scoring-all/result_age21_k14.json) |
| 15 | ok | 18 | building | false | complete | [K=15](raw/api/scoring-all/result_age21_k15.json) |
| 16–17 | ok | 19 | building | false | complete | [K=16](raw/api/scoring-all/result_age21_k16.json) … [K=17](raw/api/scoring-all/result_age21_k17.json) |
| 18–19 | ok | 20 | on_pace | false | complete | [K=18](raw/api/scoring-all/result_age21_k18.json) … [K=19](raw/api/scoring-all/result_age21_k19.json) |
| 20–22 | ok | 21 | on_pace | false | complete | [K=20](raw/api/scoring-all/result_age21_k20.json) … [K=22](raw/api/scoring-all/result_age21_k22.json) |
| 23 | ok | 22 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age21_k23.json) |
| 24 | ok | 23 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age21_k24.json) |
| 25 | ok | 24 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age21_k25.json) |
| 26 | ok | 25 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age21_k26.json) |
| 27 | ok | 26 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age21_k27.json) |
| 28 | ok | 27 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age21_k28.json) |
| 29 | ok | 28 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age21_k29.json) |
| 30 | ok | 30 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age21_k30.json) |
| 31 | ok | 32 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age21_k31.json) |
| 32 | ok | 35 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age21_k32.json) |
| 33–39 | ok | 42 | well_ahead | true | complete | [K=33](raw/api/scoring-all/result_age21_k33.json) … [K=39](raw/api/scoring-all/result_age21_k39.json) |

### Age 22 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age22_k00.json) … [K=15](raw/api/scoring-all/result_age22_k15.json) |
| 16 | ok | 19 | building | false | complete | [K=16](raw/api/scoring-all/result_age22_k16.json) |
| 17–18 | ok | 20 | building | false | complete | [K=17](raw/api/scoring-all/result_age22_k17.json) … [K=18](raw/api/scoring-all/result_age22_k18.json) |
| 19–20 | ok | 21 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age22_k19.json) … [K=20](raw/api/scoring-all/result_age22_k20.json) |
| 21–22 | ok | 22 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age22_k21.json) … [K=22](raw/api/scoring-all/result_age22_k22.json) |
| 23 | ok | 23 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age22_k23.json) |
| 24 | ok | 24 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age22_k24.json) |
| 25 | ok | 25 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age22_k25.json) |
| 26 | ok | 26 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age22_k26.json) |
| 27 | ok | 27 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age22_k27.json) |
| 28 | ok | 29 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age22_k28.json) |
| 29 | ok | 31 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age22_k29.json) |
| 30 | ok | 33 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age22_k30.json) |
| 31 | ok | 37 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age22_k31.json) |
| 32–39 | ok | 43 | well_ahead | true | complete | [K=32](raw/api/scoring-all/result_age22_k32.json) … [K=39](raw/api/scoring-all/result_age22_k39.json) |

### Age 23 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–14 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age23_k00.json) … [K=14](raw/api/scoring-all/result_age23_k14.json) |
| 15–16 | ok | 20 | building | false | complete | [K=15](raw/api/scoring-all/result_age23_k15.json) … [K=16](raw/api/scoring-all/result_age23_k16.json) |
| 17–18 | ok | 21 | building | false | complete | [K=17](raw/api/scoring-all/result_age23_k17.json) … [K=18](raw/api/scoring-all/result_age23_k18.json) |
| 19–20 | ok | 22 | on_pace | false | complete | [K=19](raw/api/scoring-all/result_age23_k19.json) … [K=20](raw/api/scoring-all/result_age23_k20.json) |
| 21–22 | ok | 23 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age23_k21.json) … [K=22](raw/api/scoring-all/result_age23_k22.json) |
| 23 | ok | 24 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age23_k23.json) |
| 24 | ok | 25 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age23_k24.json) |
| 25 | ok | 26 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age23_k25.json) |
| 26 | ok | 27 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age23_k26.json) |
| 27 | ok | 28 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age23_k27.json) |
| 28 | ok | 29 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age23_k28.json) |
| 29 | ok | 31 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age23_k29.json) |
| 30 | ok | 36 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age23_k30.json) |
| 31 | ok | 38 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age23_k31.json) |
| 32 | ok | 56 | well_ahead | false | complete | [K=32](raw/api/scoring-all/result_age23_k32.json) |
| 33–39 | ok | 44 | well_ahead | true | complete | [K=33](raw/api/scoring-all/result_age23_k33.json) … [K=39](raw/api/scoring-all/result_age23_k39.json) |

### Age 24 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–15 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age24_k00.json) … [K=15](raw/api/scoring-all/result_age24_k15.json) |
| 16–18 | ok | 21 | building | false | complete | [K=16](raw/api/scoring-all/result_age24_k16.json) … [K=18](raw/api/scoring-all/result_age24_k18.json) |
| 19 | ok | 22 | building | false | complete | [K=19](raw/api/scoring-all/result_age24_k19.json) |
| 20–21 | ok | 23 | on_pace | false | complete | [K=20](raw/api/scoring-all/result_age24_k20.json) … [K=21](raw/api/scoring-all/result_age24_k21.json) |
| 22 | ok | 24 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age24_k22.json) |
| 23 | ok | 25 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age24_k23.json) |
| 24–25 | ok | 26 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age24_k24.json) … [K=25](raw/api/scoring-all/result_age24_k25.json) |
| 26 | ok | 27 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age24_k26.json) |
| 27 | ok | 28 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age24_k27.json) |
| 28 | ok | 29 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age24_k28.json) |
| 29 | ok | 32 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age24_k29.json) |
| 30 | ok | 35 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age24_k30.json) |
| 31 | ok | 38 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age24_k31.json) |
| 32–39 | ok | 44 | well_ahead | true | complete | [K=32](raw/api/scoring-all/result_age24_k32.json) … [K=39](raw/api/scoring-all/result_age24_k39.json) |

### Age 25 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age25_k00.json) … [K=17](raw/api/scoring-all/result_age25_k17.json) |
| 18–19 | ok | 22 | building | false | complete | [K=18](raw/api/scoring-all/result_age25_k18.json) … [K=19](raw/api/scoring-all/result_age25_k19.json) |
| 20 | ok | 23 | building | false | complete | [K=20](raw/api/scoring-all/result_age25_k20.json) |
| 21 | ok | 24 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age25_k21.json) |
| 22 | ok | 25 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age25_k22.json) |
| 23–24 | ok | 26 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age25_k23.json) … [K=24](raw/api/scoring-all/result_age25_k24.json) |
| 25 | ok | 27 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age25_k25.json) |
| 26 | ok | 28 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age25_k26.json) |
| 27 | ok | 29 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age25_k27.json) |
| 28 | ok | 30 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age25_k28.json) |
| 29 | ok | 32 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age25_k29.json) |
| 30 | ok | 37 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age25_k30.json) |
| 31 | ok | 60 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age25_k31.json) |
| 32–39 | ok | 44 | well_ahead | true | complete | [K=32](raw/api/scoring-all/result_age25_k32.json) … [K=39](raw/api/scoring-all/result_age25_k39.json) |

### Age 26 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age26_k00.json) … [K=17](raw/api/scoring-all/result_age26_k17.json) |
| 18 | ok | 23 | building | false | complete | [K=18](raw/api/scoring-all/result_age26_k18.json) |
| 19–20 | ok | 24 | building | false | complete | [K=19](raw/api/scoring-all/result_age26_k19.json) … [K=20](raw/api/scoring-all/result_age26_k20.json) |
| 21 | ok | 25 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age26_k21.json) |
| 22 | ok | 26 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age26_k22.json) |
| 23 | ok | 27 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age26_k23.json) |
| 24 | ok | 28 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age26_k24.json) |
| 25–26 | ok | 29 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age26_k25.json) … [K=26](raw/api/scoring-all/result_age26_k26.json) |
| 27 | ok | 31 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age26_k27.json) |
| 28 | ok | 32 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age26_k28.json) |
| 29 | ok | 35 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age26_k29.json) |
| 30 | ok | 38 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age26_k30.json) |
| 31–39 | ok | 44 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age26_k31.json) … [K=39](raw/api/scoring-all/result_age26_k39.json) |

### Age 27 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–16 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age27_k00.json) … [K=16](raw/api/scoring-all/result_age27_k16.json) |
| 17–18 | ok | 23 | building | false | complete | [K=17](raw/api/scoring-all/result_age27_k17.json) … [K=18](raw/api/scoring-all/result_age27_k18.json) |
| 19 | ok | 24 | building | false | complete | [K=19](raw/api/scoring-all/result_age27_k19.json) |
| 20 | ok | 25 | building | false | complete | [K=20](raw/api/scoring-all/result_age27_k20.json) |
| 21 | ok | 26 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age27_k21.json) |
| 22 | ok | 27 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age27_k22.json) |
| 23 | ok | 28 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age27_k23.json) |
| 24–25 | ok | 29 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age27_k24.json) … [K=25](raw/api/scoring-all/result_age27_k25.json) |
| 26 | ok | 30 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age27_k26.json) |
| 27 | ok | 31 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age27_k27.json) |
| 28 | ok | 33 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age27_k28.json) |
| 29 | ok | 37 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age27_k29.json) |
| 30 | ok | 40 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age27_k30.json) |
| 31–39 | ok | 44 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age27_k31.json) … [K=39](raw/api/scoring-all/result_age27_k39.json) |

### Age 28 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age28_k00.json) … [K=17](raw/api/scoring-all/result_age28_k17.json) |
| 18 | ok | 24 | building | false | complete | [K=18](raw/api/scoring-all/result_age28_k18.json) |
| 19–20 | ok | 25 | building | false | complete | [K=19](raw/api/scoring-all/result_age28_k19.json) … [K=20](raw/api/scoring-all/result_age28_k20.json) |
| 21 | ok | 26 | building | false | complete | [K=21](raw/api/scoring-all/result_age28_k21.json) |
| 22 | ok | 27 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age28_k22.json) |
| 23 | ok | 28 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age28_k23.json) |
| 24 | ok | 29 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age28_k24.json) |
| 25 | ok | 30 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age28_k25.json) |
| 26 | ok | 31 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age28_k26.json) |
| 27 | ok | 33 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age28_k27.json) |
| 28 | ok | 35 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age28_k28.json) |
| 29 | ok | 38 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age28_k29.json) |
| 30 | ok | 41 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age28_k30.json) |
| 31–39 | ok | 44 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age28_k31.json) … [K=39](raw/api/scoring-all/result_age28_k39.json) |

### Age 29 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age29_k00.json) … [K=18](raw/api/scoring-all/result_age29_k18.json) |
| 19 | ok | 25 | building | false | complete | [K=19](raw/api/scoring-all/result_age29_k19.json) |
| 20 | ok | 26 | building | false | complete | [K=20](raw/api/scoring-all/result_age29_k20.json) |
| 21 | ok | 27 | building | false | complete | [K=21](raw/api/scoring-all/result_age29_k21.json) |
| 22 | ok | 28 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age29_k22.json) |
| 23 | ok | 29 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age29_k23.json) |
| 24 | ok | 30 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age29_k24.json) |
| 25 | ok | 31 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age29_k25.json) |
| 26 | ok | 32 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age29_k26.json) |
| 27 | ok | 33 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age29_k27.json) |
| 28 | ok | 35 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age29_k28.json) |
| 29 | ok | 38 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age29_k29.json) |
| 30 | ok | 40 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age29_k30.json) |
| 31–39 | ok | 44 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age29_k31.json) … [K=39](raw/api/scoring-all/result_age29_k39.json) |

### Age 30 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–19 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age30_k00.json) … [K=19](raw/api/scoring-all/result_age30_k19.json) |
| 20 | ok | 26 | building | false | complete | [K=20](raw/api/scoring-all/result_age30_k20.json) |
| 21 | ok | 27 | building | false | complete | [K=21](raw/api/scoring-all/result_age30_k21.json) |
| 22–23 | ok | 29 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age30_k22.json) … [K=23](raw/api/scoring-all/result_age30_k23.json) |
| 24 | ok | 30 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age30_k24.json) |
| 25 | ok | 31 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age30_k25.json) |
| 26 | ok | 32 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age30_k26.json) |
| 27 | ok | 33 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age30_k27.json) |
| 28 | ok | 35 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age30_k28.json) |
| 29 | ok | 38 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age30_k29.json) |
| 30 | ok | 40 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age30_k30.json) |
| 31 | ok | 60 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age30_k31.json) |
| 32–39 | ok | 44 | well_ahead | true | complete | [K=32](raw/api/scoring-all/result_age30_k32.json) … [K=39](raw/api/scoring-all/result_age30_k39.json) |

### Age 31 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age31_k00.json) … [K=17](raw/api/scoring-all/result_age31_k17.json) |
| 18–19 | ok | 28 | building | false | complete | [K=18](raw/api/scoring-all/result_age31_k18.json) … [K=19](raw/api/scoring-all/result_age31_k19.json) |
| 20 | ok | 29 | building | false | complete | [K=20](raw/api/scoring-all/result_age31_k20.json) |
| 21 | ok | 30 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age31_k21.json) |
| 22–23 | ok | 31 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age31_k22.json) … [K=23](raw/api/scoring-all/result_age31_k23.json) |
| 24 | ok | 32 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age31_k24.json) |
| 25 | ok | 33 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age31_k25.json) |
| 26 | ok | 34 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age31_k26.json) |
| 27 | ok | 35 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age31_k27.json) |
| 28 | ok | 37 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age31_k28.json) |
| 29 | ok | 38 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age31_k29.json) |
| 30 | ok | 40 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age31_k30.json) |
| 31 | ok | 43 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age31_k31.json) |
| 32–39 | ok | 44 | well_ahead | true | complete | [K=32](raw/api/scoring-all/result_age31_k32.json) … [K=39](raw/api/scoring-all/result_age31_k39.json) |

### Age 32 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age32_k00.json) … [K=17](raw/api/scoring-all/result_age32_k17.json) |
| 18–19 | ok | 29 | building | false | complete | [K=18](raw/api/scoring-all/result_age32_k18.json) … [K=19](raw/api/scoring-all/result_age32_k19.json) |
| 20 | ok | 30 | building | false | complete | [K=20](raw/api/scoring-all/result_age32_k20.json) |
| 21 | ok | 31 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age32_k21.json) |
| 22–23 | ok | 32 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age32_k22.json) … [K=23](raw/api/scoring-all/result_age32_k23.json) |
| 24 | ok | 33 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age32_k24.json) |
| 25 | ok | 34 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age32_k25.json) |
| 26 | ok | 36 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age32_k26.json) |
| 27 | ok | 37 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age32_k27.json) |
| 28 | ok | 38 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age32_k28.json) |
| 29 | ok | 40 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age32_k29.json) |
| 30 | ok | 42 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age32_k30.json) |
| 31 | ok | 51 | well_ahead | false | complete | [K=31](raw/api/scoring-all/result_age32_k31.json) |
| 32–39 | ok | 46 | well_ahead | true | complete | [K=32](raw/api/scoring-all/result_age32_k32.json) … [K=39](raw/api/scoring-all/result_age32_k39.json) |

### Age 33 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age33_k00.json) … [K=17](raw/api/scoring-all/result_age33_k17.json) |
| 18 | ok | 29 | building | false | complete | [K=18](raw/api/scoring-all/result_age33_k18.json) |
| 19–20 | ok | 30 | building | false | complete | [K=19](raw/api/scoring-all/result_age33_k19.json) … [K=20](raw/api/scoring-all/result_age33_k20.json) |
| 21 | ok | 31 | building | false | complete | [K=21](raw/api/scoring-all/result_age33_k21.json) |
| 22 | ok | 32 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age33_k22.json) |
| 23 | ok | 33 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age33_k23.json) |
| 24 | ok | 34 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age33_k24.json) |
| 25 | ok | 36 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age33_k25.json) |
| 26 | ok | 37 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age33_k26.json) |
| 27 | ok | 38 | well_ahead | false | complete | [K=27](raw/api/scoring-all/result_age33_k27.json) |
| 28 | ok | 39 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age33_k28.json) |
| 29 | ok | 41 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age33_k29.json) |
| 30 | ok | 43 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age33_k30.json) |
| 31–39 | ok | 46 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age33_k31.json) … [K=39](raw/api/scoring-all/result_age33_k39.json) |

### Age 34 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age34_k00.json) … [K=17](raw/api/scoring-all/result_age34_k17.json) |
| 18–19 | ok | 29 | building | false | complete | [K=18](raw/api/scoring-all/result_age34_k18.json) … [K=19](raw/api/scoring-all/result_age34_k19.json) |
| 20 | ok | 30 | building | false | complete | [K=20](raw/api/scoring-all/result_age34_k20.json) |
| 21 | ok | 31 | building | false | complete | [K=21](raw/api/scoring-all/result_age34_k21.json) |
| 22 | ok | 32 | building | false | complete | [K=22](raw/api/scoring-all/result_age34_k22.json) |
| 23 | ok | 33 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age34_k23.json) |
| 24 | ok | 34 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age34_k24.json) |
| 25 | ok | 36 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age34_k25.json) |
| 26 | ok | 37 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age34_k26.json) |
| 27 | ok | 38 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age34_k27.json) |
| 28 | ok | 39 | little_ahead | false | complete | [K=28](raw/api/scoring-all/result_age34_k28.json) |
| 29 | ok | 41 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age34_k29.json) |
| 30 | ok | 43 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age34_k30.json) |
| 31–39 | ok | 46 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age34_k31.json) … [K=39](raw/api/scoring-all/result_age34_k39.json) |

### Age 35 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age35_k00.json) … [K=18](raw/api/scoring-all/result_age35_k18.json) |
| 19 | ok | 30 | building | false | complete | [K=19](raw/api/scoring-all/result_age35_k19.json) |
| 20 | ok | 31 | building | false | complete | [K=20](raw/api/scoring-all/result_age35_k20.json) |
| 21–22 | ok | 32 | building | false | complete | [K=21](raw/api/scoring-all/result_age35_k21.json) … [K=22](raw/api/scoring-all/result_age35_k22.json) |
| 23 | ok | 33 | building | false | complete | [K=23](raw/api/scoring-all/result_age35_k23.json) |
| 24 | ok | 35 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age35_k24.json) |
| 25 | ok | 37 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age35_k25.json) |
| 26 | ok | 38 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age35_k26.json) |
| 27 | ok | 39 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age35_k27.json) |
| 28 | ok | 40 | little_ahead | false | complete | [K=28](raw/api/scoring-all/result_age35_k28.json) |
| 29 | ok | 42 | well_ahead | false | complete | [K=29](raw/api/scoring-all/result_age35_k29.json) |
| 30 | ok | 45 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age35_k30.json) |
| 31–39 | ok | 46 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age35_k31.json) … [K=39](raw/api/scoring-all/result_age35_k39.json) |

### Age 36 months — N=39

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–19 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age36_k00.json) … [K=19](raw/api/scoring-all/result_age36_k19.json) |
| 20 | ok | 31 | building | false | complete | [K=20](raw/api/scoring-all/result_age36_k20.json) |
| 21 | ok | 32 | building | false | complete | [K=21](raw/api/scoring-all/result_age36_k21.json) |
| 22 | ok | 33 | building | false | complete | [K=22](raw/api/scoring-all/result_age36_k22.json) |
| 23 | ok | 34 | building | false | complete | [K=23](raw/api/scoring-all/result_age36_k23.json) |
| 24 | ok | 36 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age36_k24.json) |
| 25 | ok | 37 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age36_k25.json) |
| 26 | ok | 38 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age36_k26.json) |
| 27 | ok | 39 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age36_k27.json) |
| 28 | ok | 40 | little_ahead | false | complete | [K=28](raw/api/scoring-all/result_age36_k28.json) |
| 29 | ok | 41 | little_ahead | false | complete | [K=29](raw/api/scoring-all/result_age36_k29.json) |
| 30 | ok | 44 | well_ahead | false | complete | [K=30](raw/api/scoring-all/result_age36_k30.json) |
| 31–39 | ok | 46 | well_ahead | true | complete | [K=31](raw/api/scoring-all/result_age36_k31.json) … [K=39](raw/api/scoring-all/result_age36_k39.json) |

### Age 37 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age37_k00.json) … [K=18](raw/api/scoring-all/result_age37_k18.json) |
| 19–20 | ok | 32 | building | false | complete | [K=19](raw/api/scoring-all/result_age37_k19.json) … [K=20](raw/api/scoring-all/result_age37_k20.json) |
| 21 | ok | 33 | building | false | complete | [K=21](raw/api/scoring-all/result_age37_k21.json) |
| 22 | ok | 35 | building | false | complete | [K=22](raw/api/scoring-all/result_age37_k22.json) |
| 23 | ok | 36 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age37_k23.json) |
| 24 | ok | 37 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age37_k24.json) |
| 25 | ok | 38 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age37_k25.json) |
| 26 | ok | 39 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age37_k26.json) |
| 27 | ok | 41 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age37_k27.json) |
| 28 | ok | 43 | well_ahead | false | complete | [K=28](raw/api/scoring-all/result_age37_k28.json) |
| 29–36 | ok | 45 | well_ahead | true | complete | [K=29](raw/api/scoring-all/result_age37_k29.json) … [K=36](raw/api/scoring-all/result_age37_k36.json) |

### Age 38 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age38_k00.json) … [K=18](raw/api/scoring-all/result_age38_k18.json) |
| 19 | ok | 33 | building | false | complete | [K=19](raw/api/scoring-all/result_age38_k19.json) |
| 20 | ok | 34 | building | false | complete | [K=20](raw/api/scoring-all/result_age38_k20.json) |
| 21 | ok | 36 | building | false | complete | [K=21](raw/api/scoring-all/result_age38_k21.json) |
| 22–23 | ok | 37 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age38_k22.json) … [K=23](raw/api/scoring-all/result_age38_k23.json) |
| 24 | ok | 38 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age38_k24.json) |
| 25 | ok | 39 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age38_k25.json) |
| 26 | ok | 41 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age38_k26.json) |
| 27 | ok | 42 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age38_k27.json) |
| 28–36 | ok | 46 | well_ahead | true | complete | [K=28](raw/api/scoring-all/result_age38_k28.json) … [K=36](raw/api/scoring-all/result_age38_k36.json) |

### Age 39 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–19 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age39_k00.json) … [K=19](raw/api/scoring-all/result_age39_k19.json) |
| 20 | ok | 34 | building | false | complete | [K=20](raw/api/scoring-all/result_age39_k20.json) |
| 21 | ok | 36 | building | false | complete | [K=21](raw/api/scoring-all/result_age39_k21.json) |
| 22 | ok | 37 | building | false | complete | [K=22](raw/api/scoring-all/result_age39_k22.json) |
| 23 | ok | 38 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age39_k23.json) |
| 24 | ok | 39 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age39_k24.json) |
| 25 | ok | 40 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age39_k25.json) |
| 26 | ok | 41 | little_ahead | false | complete | [K=26](raw/api/scoring-all/result_age39_k26.json) |
| 27 | ok | 43 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age39_k27.json) |
| 28–36 | ok | 46 | well_ahead | true | complete | [K=28](raw/api/scoring-all/result_age39_k28.json) … [K=36](raw/api/scoring-all/result_age39_k36.json) |

### Age 40 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age40_k00.json) … [K=18](raw/api/scoring-all/result_age40_k18.json) |
| 19 | ok | 34 | building | false | complete | [K=19](raw/api/scoring-all/result_age40_k19.json) |
| 20 | ok | 35 | building | false | complete | [K=20](raw/api/scoring-all/result_age40_k20.json) |
| 21 | ok | 36 | building | false | complete | [K=21](raw/api/scoring-all/result_age40_k21.json) |
| 22 | ok | 37 | building | false | complete | [K=22](raw/api/scoring-all/result_age40_k22.json) |
| 23 | ok | 38 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age40_k23.json) |
| 24 | ok | 39 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age40_k24.json) |
| 25 | ok | 40 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age40_k25.json) |
| 26 | ok | 41 | on_pace | false | complete | [K=26](raw/api/scoring-all/result_age40_k26.json) |
| 27 | ok | 43 | little_ahead | false | complete | [K=27](raw/api/scoring-all/result_age40_k27.json) |
| 28–36 | ok | 46 | little_ahead | true | complete | [K=28](raw/api/scoring-all/result_age40_k28.json) … [K=36](raw/api/scoring-all/result_age40_k36.json) |

### Age 41 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–20 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age41_k00.json) … [K=20](raw/api/scoring-all/result_age41_k20.json) |
| 21 | ok | 36 | building | false | complete | [K=21](raw/api/scoring-all/result_age41_k21.json) |
| 22–23 | ok | 37 | building | false | complete | [K=22](raw/api/scoring-all/result_age41_k22.json) … [K=23](raw/api/scoring-all/result_age41_k23.json) |
| 24 | ok | 38 | building | false | complete | [K=24](raw/api/scoring-all/result_age41_k24.json) |
| 25 | ok | 40 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age41_k25.json) |
| 26 | ok | 41 | on_pace | false | complete | [K=26](raw/api/scoring-all/result_age41_k26.json) |
| 27 | ok | 43 | on_pace | false | complete | [K=27](raw/api/scoring-all/result_age41_k27.json) |
| 28–36 | ok | 46 | little_ahead | true | complete | [K=28](raw/api/scoring-all/result_age41_k28.json) … [K=36](raw/api/scoring-all/result_age41_k36.json) |

### Age 42 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–16 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age42_k00.json) … [K=16](raw/api/scoring-all/result_age42_k16.json) |
| 17 | ok | 36 | building | false | complete | [K=17](raw/api/scoring-all/result_age42_k17.json) |
| 18 | ok | 37 | building | false | complete | [K=18](raw/api/scoring-all/result_age42_k18.json) |
| 19 | ok | 38 | building | false | complete | [K=19](raw/api/scoring-all/result_age42_k19.json) |
| 20 | ok | 39 | building | false | complete | [K=20](raw/api/scoring-all/result_age42_k20.json) |
| 21 | ok | 40 | on_pace | false | complete | [K=21](raw/api/scoring-all/result_age42_k21.json) |
| 22 | ok | 41 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age42_k22.json) |
| 23 | ok | 42 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age42_k23.json) |
| 24 | ok | 44 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age42_k24.json) |
| 25 | ok | 45 | little_ahead | false | complete | [K=25](raw/api/scoring-all/result_age42_k25.json) |
| 26 | ok | 52 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age42_k26.json) |
| 27–36 | ok | 53 | well_ahead | true | complete | [K=27](raw/api/scoring-all/result_age42_k27.json) … [K=36](raw/api/scoring-all/result_age42_k36.json) |

### Age 43 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age43_k00.json) … [K=17](raw/api/scoring-all/result_age43_k17.json) |
| 18 | ok | 37 | building | false | complete | [K=18](raw/api/scoring-all/result_age43_k18.json) |
| 19 | ok | 38 | building | false | complete | [K=19](raw/api/scoring-all/result_age43_k19.json) |
| 20 | ok | 39 | building | false | complete | [K=20](raw/api/scoring-all/result_age43_k20.json) |
| 21 | ok | 40 | building | false | complete | [K=21](raw/api/scoring-all/result_age43_k21.json) |
| 22 | ok | 41 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age43_k22.json) |
| 23 | ok | 42 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age43_k23.json) |
| 24 | ok | 43 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age43_k24.json) |
| 25 | ok | 45 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age43_k25.json) |
| 26 | ok | 52 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age43_k26.json) |
| 27–36 | ok | 53 | well_ahead | true | complete | [K=27](raw/api/scoring-all/result_age43_k27.json) … [K=36](raw/api/scoring-all/result_age43_k36.json) |

### Age 44 months — N=36

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–18 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age44_k00.json) … [K=18](raw/api/scoring-all/result_age44_k18.json) |
| 19 | ok | 38 | building | false | complete | [K=19](raw/api/scoring-all/result_age44_k19.json) |
| 20 | ok | 39 | building | false | complete | [K=20](raw/api/scoring-all/result_age44_k20.json) |
| 21 | ok | 40 | building | false | complete | [K=21](raw/api/scoring-all/result_age44_k21.json) |
| 22 | ok | 41 | building | false | complete | [K=22](raw/api/scoring-all/result_age44_k22.json) |
| 23 | ok | 42 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age44_k23.json) |
| 24 | ok | 44 | on_pace | false | complete | [K=24](raw/api/scoring-all/result_age44_k24.json) |
| 25 | ok | 46 | on_pace | false | complete | [K=25](raw/api/scoring-all/result_age44_k25.json) |
| 26 | ok | 52 | well_ahead | false | complete | [K=26](raw/api/scoring-all/result_age44_k26.json) |
| 27–36 | ok | 53 | well_ahead | true | complete | [K=27](raw/api/scoring-all/result_age44_k27.json) … [K=36](raw/api/scoring-all/result_age44_k36.json) |

### Age 45 months — N=33

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–17 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age45_k00.json) … [K=17](raw/api/scoring-all/result_age45_k17.json) |
| 18 | ok | 39 | building | false | complete | [K=18](raw/api/scoring-all/result_age45_k18.json) |
| 19 | ok | 40 | building | false | complete | [K=19](raw/api/scoring-all/result_age45_k19.json) |
| 20 | ok | 41 | building | false | complete | [K=20](raw/api/scoring-all/result_age45_k20.json) |
| 21 | ok | 42 | building | false | complete | [K=21](raw/api/scoring-all/result_age45_k21.json) |
| 22 | ok | 44 | on_pace | false | complete | [K=22](raw/api/scoring-all/result_age45_k22.json) |
| 23 | ok | 46 | on_pace | false | complete | [K=23](raw/api/scoring-all/result_age45_k23.json) |
| 24 | ok | 51 | little_ahead | false | complete | [K=24](raw/api/scoring-all/result_age45_k24.json) |
| 25–33 | ok | 53 | well_ahead | true | complete | [K=25](raw/api/scoring-all/result_age45_k25.json) … [K=33](raw/api/scoring-all/result_age45_k33.json) |

### Age 46 months — N=27

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–14 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age46_k00.json) … [K=14](raw/api/scoring-all/result_age46_k14.json) |
| 15 | ok | 40 | building | false | complete | [K=15](raw/api/scoring-all/result_age46_k15.json) |
| 16 | ok | 41 | building | false | complete | [K=16](raw/api/scoring-all/result_age46_k16.json) |
| 17 | ok | 43 | building | false | complete | [K=17](raw/api/scoring-all/result_age46_k17.json) |
| 18 | ok | 46 | on_pace | false | complete | [K=18](raw/api/scoring-all/result_age46_k18.json) |
| 19 | ok | 52 | little_ahead | false | complete | [K=19](raw/api/scoring-all/result_age46_k19.json) |
| 20–27 | ok | 53 | well_ahead | true | complete | [K=20](raw/api/scoring-all/result_age46_k20.json) … [K=27](raw/api/scoring-all/result_age46_k27.json) |

### Age 47 months — N=24

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–12 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age47_k00.json) … [K=12](raw/api/scoring-all/result_age47_k12.json) |
| 13 | ok | 41 | building | false | complete | [K=13](raw/api/scoring-all/result_age47_k13.json) |
| 14 | ok | 42 | building | false | complete | [K=14](raw/api/scoring-all/result_age47_k14.json) |
| 15 | ok | 44 | building | false | complete | [K=15](raw/api/scoring-all/result_age47_k15.json) |
| 16 | ok | 46 | on_pace | false | complete | [K=16](raw/api/scoring-all/result_age47_k16.json) |
| 17–24 | ok | 53 | little_ahead | true | complete | [K=17](raw/api/scoring-all/result_age47_k17.json) … [K=24](raw/api/scoring-all/result_age47_k24.json) |

### Age 48 months — N=22

| K range | State | devAge | Band | Capped | Stage / observation | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 0–11 | below_floor | — | — | — | complete | [K=0](raw/api/scoring-all/result_age48_k00.json) … [K=11](raw/api/scoring-all/result_age48_k11.json) |
| 12 | ok | 41 | building | false | complete | [K=12](raw/api/scoring-all/result_age48_k12.json) |
| 13 | ok | 43 | building | false | complete | [K=13](raw/api/scoring-all/result_age48_k13.json) |
| 14 | ok | 45 | building | false | complete | [K=14](raw/api/scoring-all/result_age48_k14.json) |
| 15 | ok | 47 | on_pace | false | complete | [K=15](raw/api/scoring-all/result_age48_k15.json) |
| 16–22 | ok | 53 | little_ahead | true | complete | [K=16](raw/api/scoring-all/result_age48_k16.json) … [K=22](raw/api/scoring-all/result_age48_k22.json) |

## 12-line summary

```text
COMPLETED — 1886/1886 requests; 1886/1886 complete reports.
Coverage: 49/49 full ages; 0 missing requests; 0 unusable responses.
HTTP: 200=1886; transport failures: 0.
Rounded expected-count control: 44/49 observed matches; 5 exceptions; 0 unknown ages.
Band formula: 1042/1042 numeric reports match; 0 mismatches.
Nonmonotonic devAge ages: 16, 23, 25, 30, 32.
Integrity: 1886 bodies, headers and source hashes verified; 0 schema issues.
Pacing: 2.0s sleep before every request; minimum completion-to-next-start gap 2.001633s.
Artifacts: scoring-table.csv; SCORING-TABLE.md; logs/phase5-validation.json.
Collector: python3 scripts/collect_scoring_table.py (resumable; saved files immutable).
Offline rebuild: python3 scripts/build_scoring_table.py.
All requested reports collected.
```
