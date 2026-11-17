# Kinedu AQ scoring: Phase 3

Collected on **2026-11-02**. **Verdict: PARTLY REAL** — real answer-driven count/norm computation, with an unresolved all-zero anomaly, confirmed nonmonotonic low-score area ages, and cosmetic locked tiles. This establishes computational behavior; it does not establish the medical or psychometric validity of the assessment.

## Method and evidence boundaries

Read [ENUMERATION.md](ENUMERATION.md), [age-map.md](age-map.md), [questions.csv](questions.csv), and the saved Phase 2 results before probing. Reused the 49 initial lists indexed by their **returned** `ageMonths`; returned age 12 is in `start_age13_gw-null.json`. No browser or new start call was used.

Made **348 requests out of the 350-request limit**: 346 HTTP 200 and 2 expected HTTP 400 invalid-answer responses, with no transport failures. Every request was a POST `action:result` to `/api/assessment`, using the exact User-Agent, Content-Type, Origin and Referer in ENUMERATION.md. Slept 0.5 seconds before each call; the verified minimum gap from one response completion to the next request was **0.501 seconds**. No other endpoint was called.

All response bodies and HTTP headers are immutable under [raw/api/scoring/](raw/api/scoring/). The authoritative [requests manifest](raw/api/scoring/requests.jsonl) records UTC `timestamp`, `body`, `file`, `http_status`, completion time, curl status and SHA-256. [summary.csv](raw/api/scoring/summary.csv) records every probe's score, band and area values; [validation](logs/phase3-validation.json) verifies hashes, statuses, pacing, coverage and budget. All HTTP errors remain in the evidence.

The [collector](scripts/probe_scoring.py) supports `initial`, `extensions`, `chains`, `batch FILE`, and `summary`; it resumes only identical manifested requests, refuses overwrites, serializes calls with a lock, and enforces the shared 350-call budget. Additional batch plans are [followups](logs/phase3-followups.json), [followups2](logs/phase3-followups2.json), [followups3](logs/phase3-followups3.json), [rate controls](logs/phase3-rate-controls.json), and [area edge controls](logs/phase3-area-edge-controls.json). Rebuild this report and audit without network calls with `python scripts/build_scoring.py`.

**Observed** below means a saved API response or saved client source directly shows it. **Inferred** means an explanatory model fitted to those observations. The server's source and full item norm tables are unavailable. Fit denominators are named explicitly; repeated-group fits are consistency checks, not independent validation sets. Additional offline calculations and source citations are in [offline findings](logs/phase3-offline-findings.md) and [machine-readable statistics](logs/phase3-offline-stats.json).

## A. Determinism and answer order

Mixed profile: age 12, all 39 IDs, `y=1` iff `rate>=0.5` (28 yes), `extended:false`.

| Probe | HTTP | devAge / band | Area months P, C, L, S | Identical raw bytes |
| --- | --- | --- | --- | --- |
| [A_age12_mixed_repeat1](raw/api/scoring/A_age12_mixed_repeat1.json) | 200 | 14 / well_ahead | 14, 16, 12, 16 | yes |
| [A_age12_mixed_repeat2](raw/api/scoring/A_age12_mixed_repeat2.json) | 200 | 14 / well_ahead | 14, 16, 12, 16 | yes |
| [A_age12_mixed_repeat3](raw/api/scoring/A_age12_mixed_repeat3.json) | 200 | 14 / well_ahead | 14, 16, 12, 16 | yes |
| [A_age12_mixed_shuffled](raw/api/scoring/A_age12_mixed_shuffled.json) | 200 | 14 / well_ahead | 14, 16, 12, 16 | yes |

**Observed:** the three repeats and deterministic shuffle have identical JSON **and identical response bytes/SHA-256**. Changing only `extended` to true also gives the identical complete report ([flag control](raw/api/scoring/A_age12_mixed_extended.json)). JSON field ordering is therefore not masking a difference in these comparisons. These are same-session tests, not evidence of stability after future server updates.

## B. Cumulative monotonicity

Both sweeps use the same 39 age-12 IDs and `extended:true`, to obtain complete scores instead of stopping at extension. Sort by `(rate,id)`, ascending or descending, then flip one additional answer to 1 per row. `+` after overall age means `capped:true`; `+` after an area means `atLeast:true`. Area order is Physical, Cognitive, Language, Social-Emotional. Dashes mean the API omitted ages for `below_floor`, not that those ages are zero. Every row links to its raw report.

| Yes count | New ID asc / raw | New ID desc / raw | Overall: both | Asc area months | Desc area months |
| --- | --- | --- | --- | --- | --- |
| 0 | [—](raw/api/scoring/B_age12_ascending_00.json) | [—](raw/api/scoring/B_age12_descending_00.json) | below_floor | — | — |
| 1 | [611](raw/api/scoring/B_age12_ascending_01.json) | [135](raw/api/scoring/B_age12_descending_01.json) | below_floor | — | — |
| 2 | [686](raw/api/scoring/B_age12_ascending_02.json) | [349](raw/api/scoring/B_age12_descending_02.json) | below_floor | — | — |
| 3 | [441](raw/api/scoring/B_age12_ascending_03.json) | [183](raw/api/scoring/B_age12_descending_03.json) | below_floor | — | — |
| 4 | [32](raw/api/scoring/B_age12_ascending_04.json) | [31](raw/api/scoring/B_age12_descending_04.json) | below_floor | — | — |
| 5 | [53](raw/api/scoring/B_age12_ascending_05.json) | [85](raw/api/scoring/B_age12_descending_05.json) | below_floor | — | — |
| 6 | [436](raw/api/scoring/B_age12_ascending_06.json) | [308](raw/api/scoring/B_age12_descending_06.json) | below_floor | — | — |
| 7 | [688](raw/api/scoring/B_age12_ascending_07.json) | [454](raw/api/scoring/B_age12_descending_07.json) | below_floor | — | — |
| 8 | [360](raw/api/scoring/B_age12_ascending_08.json) | [340](raw/api/scoring/B_age12_descending_08.json) | below_floor | — | — |
| 9 | [279](raw/api/scoring/B_age12_ascending_09.json) | [109](raw/api/scoring/B_age12_descending_09.json) | below_floor | — | — |
| 10 | [415](raw/api/scoring/B_age12_ascending_10.json) | [7](raw/api/scoring/B_age12_descending_10.json) | below_floor | — | — |
| 11 | [355](raw/api/scoring/B_age12_ascending_11.json) | [103](raw/api/scoring/B_age12_descending_11.json) | below_floor | — | — |
| 12 | [470](raw/api/scoring/B_age12_ascending_12.json) | [126](raw/api/scoring/B_age12_descending_12.json) | below_floor | — | — |
| 13 | [5](raw/api/scoring/B_age12_ascending_13.json) | [54](raw/api/scoring/B_age12_descending_13.json) | below_floor | — | — |
| 14 | [309](raw/api/scoring/B_age12_ascending_14.json) | [19](raw/api/scoring/B_age12_descending_14.json) | below_floor | — | — |
| 15 | [4](raw/api/scoring/B_age12_ascending_15.json) | [338](raw/api/scoring/B_age12_descending_15.json) | below_floor | — | — |
| 16 | [335](raw/api/scoring/B_age12_ascending_16.json) | [476](raw/api/scoring/B_age12_descending_16.json) | below_floor | — | — |
| 17 | [471](raw/api/scoring/B_age12_ascending_17.json) | [472](raw/api/scoring/B_age12_descending_17.json) | 11 / building | 12, 12, 8, 0 | 8, 12, 10, 12 |
| 18 | [330](raw/api/scoring/B_age12_ascending_18.json) | [406](raw/api/scoring/B_age12_descending_18.json) | 11 / building | 14, 12, 8, 0 | 8, 12, 10, 12 |
| 19 | [538](raw/api/scoring/B_age12_ascending_19.json) | [368](raw/api/scoring/B_age12_descending_19.json) | 11 / building | 18, 12, 8, 0 | 8, 12, 12, 12 |
| 20 | [565](raw/api/scoring/B_age12_ascending_20.json) | [565](raw/api/scoring/B_age12_descending_20.json) | 11 / building | 18, 12, 8, 8 | 8, 12, 12, 16 |
| 21 | [368](raw/api/scoring/B_age12_ascending_21.json) | [538](raw/api/scoring/B_age12_descending_21.json) | 12 / on_pace | 18, 12, 10, 8 | 8, 12, 12, 16 |
| 22 | [406](raw/api/scoring/B_age12_ascending_22.json) | [330](raw/api/scoring/B_age12_descending_22.json) | 12 / on_pace | 18, 12, 10, 8 | 10, 12, 12, 16 |
| 23 | [472](raw/api/scoring/B_age12_ascending_23.json) | [471](raw/api/scoring/B_age12_descending_23.json) | 12 / on_pace | 18, 12, 10, 8 | 12, 12, 12, 16 |
| 24 | [476](raw/api/scoring/B_age12_ascending_24.json) | [335](raw/api/scoring/B_age12_descending_24.json) | 12 / on_pace | 18, 12, 10, 10 | 12, 12, 12, 16 |
| 25 | [338](raw/api/scoring/B_age12_ascending_25.json) | [4](raw/api/scoring/B_age12_descending_25.json) | 13 / little_ahead | 18, 16, 10, 10 | 12, 12, 12, 16 |
| 26 | [19](raw/api/scoring/B_age12_ascending_26.json) | [309](raw/api/scoring/B_age12_descending_26.json) | 13 / little_ahead | 18, 16+, 10, 10 | 12, 12, 12, 16 |
| 27 | [54](raw/api/scoring/B_age12_ascending_27.json) | [5](raw/api/scoring/B_age12_descending_27.json) | 13 / little_ahead | 18, 16+, 12, 10 | 12, 16, 12, 16 |
| 28 | [126](raw/api/scoring/B_age12_ascending_28.json) | [470](raw/api/scoring/B_age12_descending_28.json) | 14 / well_ahead | 18, 16+, 14, 10 | 14, 16, 12, 16 |
| 29 | [103](raw/api/scoring/B_age12_ascending_29.json) | [355](raw/api/scoring/B_age12_descending_29.json) | 14 / well_ahead | 18, 16+, 14, 12 | 18, 16, 12, 16 |
| 30 | [7](raw/api/scoring/B_age12_ascending_30.json) | [415](raw/api/scoring/B_age12_descending_30.json) | 15 / well_ahead | 18, 16+, 16, 12 | 20+, 16, 12, 16 |
| 31 | [109](raw/api/scoring/B_age12_ascending_31.json) | [279](raw/api/scoring/B_age12_descending_31.json) | 16 / well_ahead | 18, 16+, 20+, 12 | 20+, 16, 14, 16 |
| 32 | [340](raw/api/scoring/B_age12_ascending_32.json) | [360](raw/api/scoring/B_age12_descending_32.json) | 17 / well_ahead | 18, 16+, 20+, 12 | 20+, 16, 16, 16 |
| 33 | [454](raw/api/scoring/B_age12_ascending_33.json) | [688](raw/api/scoring/B_age12_descending_33.json) | 19 / well_ahead | 18, 16+, 20+, 16 | 20+, 16, 20+, 16 |
| 34 | [308](raw/api/scoring/B_age12_ascending_34.json) | [436](raw/api/scoring/B_age12_descending_34.json) | 21 / well_ahead | 18, 16+, 20+, 24 | 20+, 16+, 20+, 16 |
| 35 | [85](raw/api/scoring/B_age12_ascending_35.json) | [53](raw/api/scoring/B_age12_descending_35.json) | 33+ / well_ahead | 18, 16+, 20+, 36+ | 20+, 16+, 20+, 16 |
| 36 | [31](raw/api/scoring/B_age12_ascending_36.json) | [32](raw/api/scoring/B_age12_descending_36.json) | 33+ / well_ahead | 18, 16+, 20+, 36+ | 20+, 16+, 20+, 16 |
| 37 | [183](raw/api/scoring/B_age12_ascending_37.json) | [441](raw/api/scoring/B_age12_descending_37.json) | 33+ / well_ahead | 18, 16+, 20+, 36+ | 20+, 16+, 20+, 24 |
| 38 | [349](raw/api/scoring/B_age12_ascending_38.json) | [686](raw/api/scoring/B_age12_descending_38.json) | 33+ / well_ahead | 18, 16+, 20+, 36+ | 20+, 16+, 20+, 36+ |
| 39 | [135](raw/api/scoring/B_age12_ascending_39.json) | [611](raw/api/scoring/B_age12_descending_39.json) | 33+ / well_ahead | 20+, 16+, 20+, 36+ | 20+, 16+, 20+, 36+ |

**Observed:** global state/age/band/cap match at **40/40** equal-count pairs. Numeric overall ages and observed area ages never decrease within either sweep. Movement is stepwise, with plateaus, rather than smooth. The largest overall move is **+12 months at flip 35** (21→33): ascending flips ID 85, descending flips ID 53. The same jump occurring at the same total count for different IDs shows why this cannot be interpreted as an intrinsic weight of either milestone. Other +2 moves occur at flips 33 and 34; entering the numeric range at flip 17 cannot be assigned a numerical jump because the preceding report omits age.

Training the global count lookup on the ascending sweep predicts the descending sweep **40/40** and six separately shuffled vectors **6/6**, including cap and band. Training per-area `(area yes count)→(state,months,atLeast)` on the ascending sweep predicts **83/83** descending area outputs whose counts were present in training. The remaining descending area outputs have no matching training count; they are not counted as failed or successful predictions.

## C. Rate-threshold profiles and a corrected typical-child control

Original probes use `extended:false`; where they return extension, a separately saved bypass with the same answers and `extended:true` supplies the score shown below.

| Age | Rate threshold | Yes / 39 | Initial stage | devAge / band | Area months P,C,L,S | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | >=0.25 | 34 | complete | 9 / well_ahead | 10+, 12, 8, 6 | [report](raw/api/scoring/C_age03_rate_ge25.json) |
| 3 | >=0.5 | 15 | complete | below_floor | — | [report](raw/api/scoring/C_age03_rate_ge50.json) |
| 3 | >=0.75 | 8 | complete | below_floor | — | [report](raw/api/scoring/C_age03_rate_ge75.json) |
| 12 | >=0.25 | 36 | extension | 33+ / well_ahead | 20+, 16+, 20+, 16 | [report](raw/api/scoring/C_age12_rate_ge25_extended_bypass.json) |
| 12 | >=0.5 | 28 | complete | 14 / well_ahead | 14, 16, 12, 16 | [report](raw/api/scoring/C_age12_rate_ge50.json) |
| 12 | >=0.75 | 7 | complete | below_floor | — | [report](raw/api/scoring/C_age12_rate_ge75.json) |
| 24 | >=0.25 | 36 | extension | 44+ / well_ahead | 38, 38+, 28+, 34+ | [report](raw/api/scoring/C_age24_rate_ge25_extended_bypass.json) |
| 24 | >=0.5 | 27 | complete | 28 / well_ahead | 28, 38+, 24, 28 | [report](raw/api/scoring/C_age24_rate_ge50.json) |
| 24 | >=0.75 | 5 | complete | below_floor | — | [report](raw/api/scoring/C_age24_rate_ge75.json) |
| 36 | >=0.25 | 39 | extension | 46+ / well_ahead | 44+, 40+, 44+, 44+ | [report](raw/api/scoring/C_age36_rate_ge25_extended_bypass.json) |
| 36 | >=0.5 | 34 | extension | 46+ / well_ahead | 40, 40+, 44+, 44+ | [report](raw/api/scoring/C_age36_rate_ge50_extended_bypass.json) |
| 36 | >=0.75 | 5 | complete | below_floor | — | [report](raw/api/scoring/C_age36_rate_ge75.json) |

**Observed:** the threshold-0.5 profile does not consistently produce `on_pace`: age 3 is below-floor, age 12 gives 14, age 24 gives 28, and age 36 is capped at 46. These outcomes alone do not disprove a norm model. If `rate` is an age-conditioned achievement probability, `sum(rate)` is the expected total; the count of rates above 0.5 is a different statistic. A deterministic threshold profile is not a random draw of a typical child.

Four controls therefore choose a random set of `round(sum(rate))` yes answers, keeping the full served ID set. This is an aggregate-count control, not a claim that those particular milestones form a realistic child profile:

| Age | Sum of served rates | Yes count | Result | Evidence |
| --- | --- | --- | --- | --- |
| 3 | 19.91 | 20 | 3 / on_pace | [raw](raw/api/scoring/M_age03_count_matches_expected_rate_sum.json) |
| 12 | 22.41 | 22 | 12 / on_pace | [raw](raw/api/scoring/M_age12_count_matches_expected_rate_sum.json) |
| 24 | 21.80 | 22 | 24 / on_pace | [raw](raw/api/scoring/M_age24_count_matches_expected_rate_sum.json) |
| 36 | 23.92 | 24 | 36 / on_pace | [raw](raw/api/scoring/M_age36_count_matches_expected_rate_sum.json) |

**Observed:** age is recovered exactly and band is `on_pace` in **4/4** controls. **Inference:** equating the observed success count with an expected-count norm curve is a substantially better explanation than weighting individual yes answers by their current displayed rate.

## D. Area independence and overall aggregation

The four requested isolated-area profiles each return `below_floor`, with no area ages to inspect. Both flag values give the same below-floor response. This is an observability limitation, not evidence that the area score fails to respond.

| Only area set to yes | Yes / 39 | Result | Evidence |
| --- | --- | --- | --- |
| Physical | 9 | below_floor | [false](raw/api/scoring/D_age12_only_Physical.json); [true](raw/api/scoring/D_age12_only_Physical_extended.json) |
| Cognitive | 9 | below_floor | [false](raw/api/scoring/D_age12_only_Cognitive.json); [true](raw/api/scoring/D_age12_only_Cognitive_extended.json) |
| Language | 10 | below_floor | [false](raw/api/scoring/D_age12_only_Language.json); [true](raw/api/scoring/D_age12_only_Language_extended.json) |
| Social-Emotional | 11 | below_floor | [false](raw/api/scoring/D_age12_only_Social_Emotional.json); [true](raw/api/scoring/D_age12_only_Social_Emotional_extended.json) |

To expose area changes, hold all other answers at the 28-yes threshold-0.5 baseline and set one area's answers to all-zero or all-one. The baseline ages are **14,16,12,16**, overall 14.

| Changed area | Area answers | Overall | Area months P,C,L,S | Evidence |
| --- | --- | --- | --- | --- |
| Physical | 0 | 12 / on_pace | 8, 16, 12, 16 | [raw](raw/api/scoring/D2_age12_typical_Physical_all0.json) |
| Physical | 1 | 15 / well_ahead | 20+, 16, 12, 16 | [raw](raw/api/scoring/D2_age12_typical_Physical_all1.json) |
| Cognitive | 0 | 12 / on_pace | 14, 8, 12, 16 | [raw](raw/api/scoring/D2_age12_typical_Cognitive_all0.json) |
| Cognitive | 1 | 15 / well_ahead | 14, 16+, 12, 16 | [raw](raw/api/scoring/D2_age12_typical_Cognitive_all1.json) |
| Language | 0 | 12 / on_pace | 14, 16, 6, 16 | [raw](raw/api/scoring/D2_age12_typical_Language_all0.json) |
| Language | 1 | 17 / well_ahead | 14, 16, 20+, 16 | [raw](raw/api/scoring/D2_age12_typical_Language_all1.json) |
| Social-Emotional | 0 | 11 / building | 14, 16, 12, 6 | [raw](raw/api/scoring/D2_age12_typical_Social_Emotional_all0.json) |
| Social-Emotional | 1 | 16 / well_ahead | 14, 16, 12, 36+ | [raw](raw/api/scoring/D2_age12_typical_Social_Emotional_all1.json) |

**Observed:** all eight interventions change only the targeted area's age/atLeast; the other **24/24** area records remain identical. Global age can change. Across Phase 2 and Phase 3, an area lookup keyed by **that area's effective answered IDs and yes count** has **679/679** repeat-key comparisons without conflicts, including cases in which other areas change.

Overall age is **not** a simple mean, median, minimum or maximum of the four published ages. Fit against all **176** complete reports with four numeric area ages:

| Formula | Exact matches / reports |
| --- | --- |
| floor(mean) | 49/176 |
| round-half-up(mean) | 24/176 |
| ceil(mean) | 24/176 |
| floor(median) | 24/176 |
| round-half-up(median) | 24/176 |
| minimum | 2/176 |
| maximum | 2/176 |

A constrained least-squares weighted mean (nonnegative weights summing to one) fitted on the same 176 reports gives weights P,C,L,S = **0.3815, 0.0000, 0.1092, 0.5093**. After rounding half up it matches **19/176**, with unrounded RMSE **5.005 months**. These are fitted, in-sample metrics, not held-out accuracy. [Fit data](logs/phase3-formula-fit.json).

These aggregate fits pool repeated and deliberately extreme probes; the denominator is not a population sample. At ascending count 17, the four ages are 12,12,8,0 but overall is 11. At all-one, age 3 has overall 18 and areas 10,18,10,8; age 12 has overall 33 and areas 20,16,20,36. The first exact weighted-mean equality would require all weight on Cognitive, which predicts 16 for the second. Even rounding cannot reconcile this pair. The supported explanation is a separate overall norm projection over the answered-ID set.

**Exact observed per-area lookup for the fixed age-12 ID set.** The complete set contains 9 Physical, 9 Cognitive, 10 Language and 11 Social-Emotional answers, including calibration in its actual domain. Each cell is months, with `+` for atLeast. A dash means the count exceeds that area's item count or was unobserved. All observed entries agree across repeated profiles.

| Area yes count | Physical | Cognitive | Language | Social-Emotional |
| --- | --- | --- | --- | --- |
| 0 | 8 | 8 | 6 | 6 |
| 1 | 8 | 8 | 6 | 6 |
| 2 | 8 | 2 | 6 | 6 |
| 3 | 10 | 0 | 8 | 0 |
| 4 | 12 | 12 | 8 | 8 |
| 5 | 12 | 12 | 10 | 10 |
| 6 | 12 | 12 | 12 | 12 |
| 7 | 14 | 16 | 14 | 12 |
| 8 | 18 | 16+ | 16 | 16 |
| 9 | 20+ | 16+ | 20+ | 24 |
| 10 | — | — | 20+ | 36+ |
| 11 | — | — | — | 36+ |

**Nonmonotonic area edge behavior:** unlike the numeric portions of the cumulative sweeps, this full lookup reveals low-score drops: Cognitive zero yes gives 8 months, two yes gives 2, three yes gives 0, then four yes gives 12; Social-Emotional zero/two yes gives 6 months, three yes gives 0, then four gives 8. Final controls change only that area's cumulative yes count, holding every other answer at the same typical baseline, and reproduce these drops. See [Cognitive count 2](raw/api/scoring/D3_age12_Cognitive_count02_others_typical.json), [count 3](raw/api/scoring/D3_age12_Cognitive_count03_others_typical.json), [count 4](raw/api/scoring/D3_age12_Cognitive_count04_others_typical.json), [Social count 3](raw/api/scoring/D3_age12_Social_Emotional_count03_others_typical.json), and the zero controls in D2. This is a scoring pathology, not noise in repeated calls. A count lookup explains it exactly but a smooth monotone developmental model does not. The cumulative B tests did not expose it because their early whole reports were below_floor.

## Best-fit scoring model and exact-match limits

**Observed sufficient statistics:** normalize duplicate IDs with the **last value winning**, discard the observed unknown ID, let `S` be the effective known answered IDs, and let `K=sum(y)` over S. For a fixed S and chronological age, overall state/age/cap depends on K in every tested repeated group. Which particular IDs are yes affects skills and area counts, but did not alter global score at fixed K. Adding/removing IDs can change the norm curve, floor and ceiling; it is not just a universal yes percentage.

**Inferred norm projection:** let `p_i(m)` be the bank's underlying probability for item i at age m. A plausible approximate scorer is:

```text
observed_fraction = K / len(S)
expected_fraction_S(m) = mean(p_i(m) for i in S with usable norm data)
raw_age ≈ argmin_m abs(expected_fraction_S(m) - observed_fraction)
```

The valid candidate ages, missing-norm handling and ceiling rule matter. They are not fully recoverable from the rounded, age-local start rates. A Rasch-like norm model with raw count as sufficient statistic is also compatible with the count tests; the probes do not identify a unique server implementation.

**Direct numerical check:** submit the entire 11-ID Secure Attachment inventory at chronological age 0. Its published skill curve supplies the expected mean. Choosing the closest curve pct to `K/11` over positive integer ages predicts every uncapped global result. This is a fitted diagnostic using a complete skill inventory, not a proof that all arbitrary sets use the plotted skill curve.

| Yes / 11 | Nearest positive curve age | Returned overall age | Area months | Capped | Evidence |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 0 | False | [raw](raw/api/scoring/M_secure_age00_count00.json) |
| 1 | 1 | 1 | 0 | False | [raw](raw/api/scoring/M_secure_age00_count01.json) |
| 2 | 1 | 1 | 0 | False | [raw](raw/api/scoring/M_secure_age00_count02.json) |
| 3 | 1 | 1 | 0 | False | [raw](raw/api/scoring/M_secure_age00_count03.json) |
| 4 | 2 | 2 | 2 | False | [raw](raw/api/scoring/M_secure_age00_count04.json) |
| 5 | 3 | 3 | 4 | False | [raw](raw/api/scoring/M_secure_age00_count05.json) |
| 6 | 4 | 4 | 4 | False | [raw](raw/api/scoring/M_secure_age00_count06.json) |
| 7 | 5 | 5 | 4 | False | [raw](raw/api/scoring/M_secure_age00_count07.json) |
| 8 | 6 | 6 | 6 | False | [raw](raw/api/scoring/M_secure_age00_count08.json) |
| 9 | 9 | 9 | 8 | False | [raw](raw/api/scoring/M_secure_age00_count09.json) |
| 10 | 14 | 14 | 14 | False | [raw](raw/api/scoring/M_secure_age00_count10.json) |
| 11 | 17 | 15 | 16 | True | [raw](raw/api/scoring/M_secure_age00_count11.json) |

The nearest-curve model fits **11/11 uncapped global** results; including the all-one saturated case gives **11/12**. A naive nearest-mean calculation on even ages fits only **8/11 uncapped area** results, so the area's calibration is separate from this plotted mean. Per-area outputs are consistently count-driven and, in the collected numeric results, fall on a two-month grid; their low-score mapping can be nonmonotonic as shown in D. Their exact general norm/quantization function is unresolved.

The empirically exact age-12 lookup for the full 39-ID set is:

| K | Global output |
| --- | --- |
| 0–16 | below_floor |
| 17–20 | 11 / building |
| 21–24 | 12 / on_pace |
| 25–27 | 13 / little_ahead |
| 28–29 | 14 / well_ahead |
| 30 | 15 / well_ahead |
| 31 | 16 / well_ahead |
| 32 | 17 / well_ahead |
| 33 | 19 / well_ahead |
| 34 | 21 / well_ahead |
| 35–39 | 33 / well_ahead / capped |

The complete `(chronological age,S,K)→(state,devAge,capped)` consistency model has **114/114** repeated-group comparisons without conflict. Conditional on a numeric result, `(S,K)→(devAge,capped)` has **115/115**, ignoring chronological age. These are internal consistency checks; the held-out pattern predictions are the 40+6 tests in B.

**Band formula, exact on 227/227 numeric reports** across both phases:

```text
r = devAge / max(ageMonths, 1)
if r > 1.15:        well_ahead
elif r > 1.05:      little_ahead
elif r >= 0.95:     on_pace
else:              building
```

Exact boundary controls return `on_pace` at **0.95** and **1.05**, and `little_ahead` at **1.15**. See [0.95](raw/api/scoring/M_band_age20_count33.json), [1.05](raw/api/scoring/M_band_age20_count34.json), [1.15](raw/api/scoring/M_band_exact_115_dev46_age40.json). The displayed band uses the returned integer age in every checked report.

**Floor:** chronological age changes whether an age is exposed. The same 28-yes age-12 vector yields age 14 at the tested chronological ages 0,1,2,3,6,12–16, but below-floor at 17–24,36,48. An uncapped age 17 is `building` at chronological age 20 (ratio .85), and below-floor at age 21. This supports a lower reporting boundary near **85%** of chronological age. It is an inference about the tested uncapped vectors, not a fully recovered floor algorithm: the underlying pre-rounded age is hidden in floor responses. Capped age 33 is still `building` at chronological age 48 (ratio .6875), so a universal `ratio<.85→below_floor` rule is false. [Boundary .85](raw/api/scoring/M_band_age20_count32.json), [below it](raw/api/scoring/M_band_age21_count32.json), [cap exception](raw/api/scoring/M_age48_same_age12_all_one.json).

**Ceilings:** `capped:true` means saturation for the supplied answered-ID set, rather than a fixed age limit. Ages 3/12/24/36 all-one initial sets cap at 18/33/44/46. At age 12, answering additional extension items can lift the cap to 42,45,53. The identical devAge 33 can be capped before extension and uncapped after eight zero extension answers. An area's `atLeast` is its own saturation flag; it can be true when the global cap is false. The precise ceiling formula remains unresolved.

## E. Extension mechanics

**Observed trigger at age 12, fixed full 39-ID list:** binary search in ascending-rate, descending-rate and client order gives the same boundary. The first two orderings deliberately disagree about which milestones are yes.

| Ordering | Last complete | First extension | First extension IDs |
| --- | --- | --- | --- |
| ascending | [34 / 39 yes; age 21, uncapped](raw/api/scoring/E_age12_ascending_34.json) | [35 / 39 yes](raw/api/scoring/E_age12_ascending_35.json) | 558, 684, 651, 503, 695, 566, 658, 612 |
| descending | [34 / 39 yes; age 21, uncapped](raw/api/scoring/E_age12_descending_34.json) | [35 / 39 yes](raw/api/scoring/E_age12_descending_35.json) | 558, 684, 651, 503, 695, 566, 658, 612 |
| client_order | [34 / 39 yes; age 21, uncapped](raw/api/scoring/E_age12_client_order_34.json) | [35 / 39 yes](raw/api/scoring/E_age12_client_order_35.json) | 558, 684, 651, 503, 695, 566, 658, 612 |

A fourth randomized ordering confirms 34 complete / 35 extension. Thus all-one in any one area is insufficient, and neither consecutive yes answers, anchors being yes, nor a particular top-rate set is necessary. At the 35-yes boundary the ascending profile has all four anchors at zero, while descending has them at one. Answer order is irrelevant in A. This identifies the minimal yes **count for this fixed full set**; it does not establish a universal percentage threshold.

The cutoff changes with the supplied IDs: **34/38**, **34/37**, **34/36** all trigger extension, and their forced scores cap at 34 instead of 33. Age 36's threshold-0.5 profile triggers at **34/39**, so 35/39 is not a universal rule. Even only eight all-yes IDs at age 12 trigger extension ([subset probe](raw/api/scoring/E_age12_first08_yes_false.json)). Paired complete responses support **global saturation plus available extension candidates** as the trigger; area saturation alone is not sufficient.

Append the eight first age-12 extension IDs to the original all-one answers:

| Extension answers | Total yes / 47 | extended=true result | extended=false result | Evidence |
| --- | --- | --- | --- | --- |
| all_one | 47 | 42+ / well_ahead | extension | [true](raw/api/scoring/E_age12_extension_all_one.json); [false](raw/api/scoring/E_age12_extension_all_one_false.json) |
| all_zero | 39 | 33 / well_ahead | complete; 33 / well_ahead | [true](raw/api/scoring/E_age12_extension_all_zero.json); [false](raw/api/scoring/E_age12_extension_all_zero_false.json) |
| mixed | 42 | 42+ / well_ahead | extension | [true](raw/api/scoring/E_age12_extension_mixed.json); [false](raw/api/scoring/E_age12_extension_mixed_false.json) |

Mixed uses `id % 2` on the eight new items (three yes). `extended:true` completes in all three cases, and even with no extension answers supplied ([bypass](raw/api/scoring/E_age12_all_yes_bypass.json)). Therefore the flag is a caller-controlled **stop-extension switch**, not proof that an extension round occurred. With the all-zero extension, false and true produce identical reports; with all-one or mixed, false returns another new batch.

**Full all-one chains, keeping `extended:false` at every round:** each row below lists the number of new items in successive extension stages. At every depth after the first batch, a paired `extended:true` request returns complete. Original answers are retained and new IDs appended.

| Age | Extension stages | New batch sizes | Final answered IDs | Ceilings before/after batches | Evidence |
| --- | --- | --- | --- | --- | --- |
| 3 | 7 | 8, 8, 8, 8, 8, 8, 1 | 88 | 18→26→32→40→44→47→51→53 | [terminal raw](raw/api/scoring/E_chain_age03_depth07_false.json) |
| 12 | 4 | 8, 8, 8, 5 | 68 | 33→42→45→53→53 | [terminal raw](raw/api/scoring/E_chain_age12_depth04_false.json) |
| 24 | 3 | 8, 8, 3 | 58 | 44→46→53→53 | [terminal raw](raw/api/scoring/E_chain_age24_depth03_false.json) |
| 36 | 2 | 8, 8 | 55 | 46→47→53 | [terminal raw](raw/api/scoring/E_chain_age36_depth02_false.json) |

**Observed selection invariants:** extension batches have **at most two items per area**, contain known bank IDs, never repeat an already answered ID in these chains, and may be shorter than eight when fewer candidates remain. The first age-12 batch is balanced 2/2/2/2 and identical across the four boundary orderings; later batches depend on the enlarged answered-ID set. Its returned rates are evaluated at chronological age 12 (including 0 and .02), so it does not simply choose items closest to displayed .5 at chronological age. At global ceiling 53, extension can still occur (age-12 depth 3), and a later complete result can still be capped. Saturation is therefore not itself a terminal stage.

**Client versus API:** the saved client initially sends false, then sends true after one extension, so its normal path has **at most one extension round**. The API itself allows the longer false-flag chains above. Source: [initial result and stage handling](raw/js/beautified/page-5f182d70f1f24a3d.js:360), [classic handler](raw/js/beautified/page-5f182d70f1f24a3d.js:2291). The per-item ranking/eligibility formula for extension candidates is **not fully recovered**; max-two-per-area, unseen-ID selection, the fixed-set minimal trigger, stop flag, and observed chain depths are established. No claim is made for every possible answer pattern.

## F. Input validation and ID scope

All validation probes use age 12 and, except noted, `extended:true`. Known foreign IDs are taken from the returned-age-36 initial list and exclude overlap with age 12.

| Input | Submitted count | HTTP | Result | Area months P,C,L,S | Evidence |
| --- | --- | --- | --- | --- | --- |
| Only foreign IDs, all yes | 38 | 200 | 46+ / well_ahead | 44+, 40+, 44+, 42+ | [raw](raw/api/scoring/F_age12_foreign_age36_only.json) |
| Typical baseline plus foreign yes | 77 | 200 | 46+ / well_ahead | 44+, 40+, 60, 42 | [raw](raw/api/scoring/F_age12_typical_plus_foreign_yes.json) |
| Typical baseline plus foreign no | 77 | 200 | 11 / building | 12, 12, 6, 12 | [raw](raw/api/scoring/F_age12_typical_plus_foreign_no.json) |
| Only first 10 baseline answers | 10 | 200 | 14 / well_ahead | 14, not_enough, not_enough, not_enough | [raw](raw/api/scoring/F_age12_first10_only.json) |
| One y=2 | 39 | 400 | invalid_body | — | [raw](raw/api/scoring/F_age12_invalid_y_2.json) |
| One y=-1 | 39 | 400 | invalid_body | — | [raw](raw/api/scoring/F_age12_invalid_y_minus1.json) |
| Omit three calibration answers | 36 | 200 | 14 / well_ahead | 14, 16, 12, 16+ | [raw](raw/api/scoring/F_age12_typical_omit_calibration.json) |
| Empty answers | 0 | 200 | not_enough | — | [raw](raw/api/scoring/F_age12_empty_answers.json) |
| Append unknown ID 999999=yes | 40 | 200 | 14 / well_ahead | 14, 16, 12, 16 | [raw](raw/api/scoring/F_age12_typical_plus_unknown.json) |
| Duplicate first ID with same value | 40 | 200 | 14 / well_ahead | 14, 16, 12, 16 | [raw](raw/api/scoring/F_age12_duplicate_first.json) |
| Append conflicting first-ID value 0 | 40 | 200 | 13 / little_ahead | 12, 16, 12, 16 | [raw](raw/api/scoring/F_age12_duplicate_conflict.json) |
| Prepend conflicting first-ID value 0 | 40 | 200 | 14 / well_ahead | 14, 16, 12, 16 | [raw](raw/api/scoring/F_age12_duplicate_conflict_first.json) |

**Observed:** foreign known IDs are accepted and scored, not bound to a remembered start response. Adding foreign yes changes the baseline age 14→46; adding foreign no changes it to 11. The same submitted vector can be sent at multiple chronological ages without a session token. This supports a per-ID bank lookup.

Partial answers can complete. First 1–7 all-yes IDs each return `not_enough`; first **8** complete (age 19, capped), and eight extension-only answers can complete even though every individual area is `not_enough`. A minimum of eight effective usable answers is consistent with these tests. Age 1's seven Language answers are `not_enough`, while its other sufficiently sized areas can expose months. This boundary was tested with these ID sets, not every mix of known/unknown IDs.

Non-binary numbers return HTTP 400 `invalid_body`. Omitting calibration is accepted; the typical baseline global score remains 14 but Social-Emotional `atLeast` changes false→true. Unknown ID 999999 is accepted and the **entire response is unchanged** in this single unknown-ID test. Repeated IDs are accepted; equal duplicates do not change the report, and a conflicting duplicate uses the **last value** (appending no yields age 13, prepending it restores age 14). Thus shuffling contradictory duplicates is a different case from shuffling unique answers.

These are permissive-input observations, not a claim that validation is absent: y=2/-1 are rejected, and minimum-answer gating exists. Gestation and birthdate validation were outside this phase.

## G. The all-zero age-1 anomaly

The age-1 all-zero response is reproduced, identical to both Phase 2 captures. All 39 supplied `y` values really are numeric zero.

| Chronological age | Profile | Result | Area months P,C,L,S | Evidence |
| --- | --- | --- | --- | --- |
| 0 | All zero | below_floor | — | [raw](raw/api/scoring/G_age00_all_zero.json) |
| 0 | Only calibration yes | below_floor | — | [raw](raw/api/scoring/G_age00_zero_calibration_yes.json) |
| 0 | All zero, omit calibration | below_floor | — | [raw](raw/api/scoring/G_age00_zero_omit_calibration.json) |
| 1 | All zero | 1 / on_pace | 2, 0, not_enough, 0 | [raw](raw/api/scoring/G_age01_all_zero.json) |
| 1 | Only calibration yes | 1 / on_pace | 2, 0, not_enough, 0 | [raw](raw/api/scoring/G_age01_zero_calibration_yes.json) |
| 1 | All zero, omit calibration | 1 / on_pace | 2, 0, not_enough, 0 | [raw](raw/api/scoring/G_age01_zero_omit_calibration.json) |
| 2 | All zero | below_floor | — | [raw](raw/api/scoring/G_age02_all_zero.json) |
| 2 | Only calibration yes | below_floor | — | [raw](raw/api/scoring/G_age02_zero_calibration_yes.json) |
| 2 | All zero, omit calibration | below_floor | — | [raw](raw/api/scoring/G_age02_zero_omit_calibration.json) |

Additional isolating probes:

| Change | Observed output | Evidence |
| --- | --- | --- |
| Keep age-1 zero IDs, send chronological age 0 | age 1 / on_pace | [raw](raw/api/scoring/G_age00_age01_zero_ids.json) |
| Keep age-1 zero IDs, send age 2 or 12 | below_floor | [age 2](raw/api/scoring/G_age02_age01_zero_ids.json), [age 12](raw/api/scoring/G_age12_age01_zero_ids.json) |
| Send age-0 zero IDs at age 1 | below_floor | [raw](raw/api/scoring/G_age01_age00_zero_ids.json) |
| Send age-2 zero IDs at age 1 | age 1 / on_pace | [raw](raw/api/scoring/G_age01_age02_zero_ids.json) |
| Remove all four anchors from age-1 zero vector | age 1 / on_pace | [raw](raw/api/scoring/G_age01_zero_omit_anchors.json) |
| Remove the entire Physical domain | below_floor | [raw](raw/api/scoring/G_age01_zero_omit_Physical.json) |
| Remove any single one of the 13 Physical IDs | age 1 / on_pace in all 13 | G_age01_zero_omit_id* in [summary](raw/api/scoring/summary.csv) |
| Only the 13 Physical zeros, age 1 | age 2 / well_ahead | [raw](raw/api/scoring/G_age01_age01_Physical_zero_only.json) |
| First ten Physical zeros, age 1 | age 3 / well_ahead | [raw](raw/api/scoring/G_age01_Physical_first10_zero.json) |
| Age-12 IDs, all zero, sent at age 0 | age 5 / well_ahead | [raw](raw/api/scoring/M_age00_initial12_count00.json) |

**Observed explanation of the label:** once the server emits devAge 1 for chronological age 1, the recovered ratio formula produces `on_pace`. The anomaly is not caused by answer booleans, answer ordering, calibration yes values, or a single mandatory Physical milestone. It follows the answered-ID set and chronological floor behavior. The same low-score problem can produce an even more implausible age when older question IDs are supplied for a newborn.

**Inferred cause, not proven:** projection onto the minimum usable norm age may be clamping scores below the supported range, then the relative reporting floor sees that projected age. This is consistent with count-zero Secure Attachment yielding age 1 and count-zero older IDs yielding age 5. The server's norm support and floor code are unavailable, and the age-0 own-list all-zero response behaves differently. Therefore the causal explanation remains **unexplained**; support/clamping is a hypothesis, not a recovered implementation. This anomaly limits interpretation of the numeric report even though the calculation is reproducible.

## H. Skills curves and childPct

Each skill has an inventory, `from/to` age metadata, `total`, `reached`, `focus`, childPct, and a baseline curve. `from/to` are not the child's achieved ages; the curve can extend beyond them (Secure Attachment from=1,to=16 has ages 0–18). The exact statistical definition of from/to is not exposed. Focus/status selection is answer-sensitive; a complete formula for those selections was not a scoring probe target.

| Check across saved Phase 2 + Phase 3 reports | Matches / total |
| --- | --- |
| reached = count(status in {yes,typical}) | 5776/5776 |
| childPct = reached / total | 5776/5776 |
| Same skill + inventory gives identical curve | 5728/5728 repeated comparisons; 48 distinct groups |

**Observed:** curves do not vary with a child's answers for the same skill inventory. `childPct` does vary, includes inferred `typical` milestones, and is not explicit yes count divided by questions asked. The age-1 all-zero report still counts six unasked newborn milestones as `typical`, giving that skill childPct=.6. Unasked milestones can also remain `open`. This is report inference, not a direct assertion supplied by the caregiver. [Age-1 raw report](raw/api/scoring/G_age01_all_zero.json).

The source draws `pct` as the baseline line, shades between `lo` and `hi`, and places the child's dot at chronological age and childPct. Its text says the shading spans the skill's milestones from earliest to latest, supporting the extrema interpretation rather than a statistical confidence interval. [Chart rendering](raw/js/beautified/page-5f182d70f1f24a3d.js:152), [explanation copy](raw/js/beautified/page-5f182d70f1f24a3d.js:1261).

| Curve example | Baseline values | Served rate comparison |
| --- | --- | --- |
| One-item Phonetics, ID948, age 47 | pct=lo=hi=.843537 | start rate .84 |
| Same skill, age 48 | pct=lo=hi=.833333 | start rate .83 |
| Two-item Developing peer relationships, age 32 | lo=.617778, hi=.836591, pct=.7271845=(lo+hi)/2 | ID694 rate .62; ID619 absent from that start list |
| Same skill, age 37 | lo=.700981, hi=.890535, pct=.795758 | ID694 rate .70 |
| Developing musical skills, age 12 | pct=.5904693333 | only served skill item ID338 has rate .64; not equal |

Sources: [age-42 complete inventory](raw/api/result_age42_all_yes_numeric.json), [age-6 inventory](raw/api/result_age06_all_yes_extended.json), returned-age start lists [47](raw/api/start_age48_gw-null.json), [48](raw/api/start_age49_gw-null.json), [32](raw/api/start_age33_gw-null.json), [37](raw/api/start_age38_gw-null.json), [12](raw/api/start_age13_gw-null.json). Every observed one-item curve has equal pct/lo/hi and every two-item curve has pct=(lo+hi)/2 to floating-point tolerance, as checked in the offline analysis.

**Inference:** `pct` is the mean of underlying item probabilities across the skill inventory's usable norms, with lo/hi the item extrema; start rates are rounded versions of those probabilities. It is **not** generally the mean of the currently served questions for that skill. Full bank per-item probabilities are not returned, so exact whole-bank averaging cannot be verified for every skill. Some curves dip with increasing age: they are empirical-looking baseline arrays, not universally monotone logistic lines.

## I. Report gating and paywall presentation

The API returns both tiers together without authentication in every successful probe. No paid endpoint or checkout was opened. This table distinguishes response schema from presentation in the saved client; it does not assert what a purchased product contains.

| Data/flag | Basic JSON | Detail/top-level JSON | Free classic/hook presentation in saved source |
| --- | --- | --- | --- |
| state, band, devAge, capped, ageMonths | Present on ok | Repeated in detail | Overall age/gauge and ahead badge visible; capped gets a plus/ceiling treatment |
| tier | basic | detail | Metadata; rendering does not consult tier |
| areasLocked | true | Absent | Declares locking; rendering does not consult this field directly |
| teaserArea | Optional | Absent as a standalone field | Fallback strongest-area label |
| areas[{area,state,months,atLeast}] | Absent | Present; months/atLeast absent for not_enough area | Only one strongest area may show its actual numeric months |
| areasDefaultHidden | Absent | Present | If true, even received area months are hidden and the fallback teaser has no number |
| Three other area tiles | No numeric area values | Actual computed values already returned | Locked/blurred tiles contain literal **around 88**, not the child's actual values |
| skills/curves/items/childPct | Not nested in basic | Top-level skills present on ok | Default skills view can render cards; classic/hook show one milestone, blur more and hand off to the paywall |
| activity | Not nested in basic | Top-level activity on ok | Broader plan is promoted through the paywall; recommendation data is already returned |
| below_floor or not_enough | Only state | Detail only state; no numeric report/skills | Alternative incomplete/floor flow; below_floor includes floorActivities |

Evidence: [state storage](raw/js/beautified/page-5f182d70f1f24a3d.js:2322), [free overall report](raw/js/beautified/page-5f182d70f1f24a3d.js:3354), [area hiding/teaser selection](raw/js/beautified/page-5f182d70f1f24a3d.js:3376), [actual teaser age](raw/js/beautified/page-5f182d70f1f24a3d.js:3493), [literal 88](raw/js/beautified/page-5f182d70f1f24a3d.js:3538), [blurred milestones](raw/js/beautified/page-5f182d70f1f24a3d.js:3596), [paywall handoff](raw/js/beautified/page-5f182d70f1f24a3d.js:1904).

**Observed:** gating is substantially client presentation; detail values are already in the public response. The literal blurred 88 tiles are cosmetic placeholders. That does not imply the actual computed overall/area ages or skills are fabricated.

## Verdict

**PARTLY REAL — real computation with defective low-score behavior and cosmetic gating.** The strongest three pieces of evidence are: **(1)** the ascending count lookup predicts 40/40 descending and 6/6 randomized overall scores, while expected-rate totals recover chronological age in 4/4 controls and a published skill norm predicts 11/11 uncapped ages; **(2)** fixed-answer controls reproduce Cognitive ages 8→2→0→12 as successes rise 1→2→3→4, and all-zero profiles can produce on_pace/ahead ages, establishing material scoring defects rather than random response noise; **(3)** the public API supplies actual answer-sensitive detail and skills, while the saved free client locks those values and inserts literal blurred 88 tiles. Thus the underlying report is substantially computed, not merely a fixed decorative result, but it does not meet a consistent monotone developmental-model interpretation at low scores. A single ratio rule explains every numeric band; extension/foreign answers alter scores and ceilings predictably. The unexplained minimum-age/floor behavior and coarse area calibration limit interpretation, and computational evidence does not establish validated developmental measurement.
