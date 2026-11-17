# Phase 3 offline cross-checks

This note analyzes saved first-party client source and saved API bodies only. It makes no requests. Counts are reproducible with [phase3-offline-analysis.py](phase3-offline-analysis.py); the live collection can add records after a particular run, so [phase3-offline-stats.json](phase3-offline-stats.json) records the latest snapshot.

## Report gating observed in the saved client

The result API itself supplies `basic`, `detail`, `skills`, and `activity` together for successful reports. These are not separate authenticated API requests. The saved classic completion handler stores all four, plus optional `floorActivities` ([page bundle, line 2322](../raw/js/beautified/page-5f182d70f1f24a3d.js:2322)). The default component stores only `basic` and `skills` (line 391).

| Field/data | API availability | Saved classic/hook presentation |
|---|---|---|
| `basic.state`, `band`, `devAge`, `capped`, `ageMonths` | Basic successful report | Overall developmental age, chronological age and gauge are visible; ahead bands receive a positive badge; capped adds `+` and ceiling copy. |
| `basic.tier="basic"`, `areasLocked=true` | Basic successful report | Metadata; neither field is consulted by the saved client rendering. |
| `basic.teaserArea` | Optional basic field | Fallback strongest-area label; shown without a numeric month value when areas are default-hidden. |
| `detail.tier="detail"`, `areas[{area,state,months,atLeast}]` | Same unauthenticated response | Used to choose the strongest area only when `areasDefaultHidden=false`; only that area's actual month value is displayed. |
| `detail.areasDefaultHidden` | Detail field | When true, even numeric values already received for the teaser are hidden. |
| Other three area tiles | Actual values already in `detail` | Locked buttons use literal blurred `"around 88"`; they do not blur the child's actual area ages. |
| Skills inventory/curves | Same response | Default skills mode can show actual skill cards; classic/hook select one open milestone per area and show the first, blur up to two more. |
| Activity recommendation | Same response | Classic/hook retain the activity; a paywall handoff controls the broader plan. |
| `below_floor` | Basic and detail contain only `state` | Free alternative screen uses `floorActivities`; the missing ages/skills were not merely hidden in JSON. |

Evidence: visible overall report [lines 3354–3427](../raw/js/beautified/page-5f182d70f1f24a3d.js:3354); strongest area and `areasDefaultHidden` [line 3376](../raw/js/beautified/page-5f182d70f1f24a3d.js:3376); actual teaser months [line 3493](../raw/js/beautified/page-5f182d70f1f24a3d.js:3493); literal blurred 88 [line 3538](../raw/js/beautified/page-5f182d70f1f24a3d.js:3538); real blurred milestone titles [line 3596](../raw/js/beautified/page-5f182d70f1f24a3d.js:3596); paywall URL [lines 1904–1919](../raw/js/beautified/page-5f182d70f1f24a3d.js:1904). No paid page was requested; these observations establish free-page presentation, not the eventual paid product.

## Skills curves

Observed in the ten Phase 2 complete reports: 166 skill records all satisfy `reached = count(items.status in {yes,typical})`, `total=len(items)`, and `childPct=reached/total`. Thus `childPct` includes `typical` milestones inferred for unasked IDs, not merely explicit yes answers divided by the questions asked. For example the all-zero age-one report still marks six unasked newborn milestones `typical`, giving that skill `reached=6`, `total=10`, `childPct=.6` ([raw report](../raw/api/result_age01_all_no_numeric.json)).

Curves are identical across every repeated `(skill, inventory IDs)` observed in Phase 2, despite different ages/answers; later Phase 3 checks continue to find no variation. They are baseline skill data, whereas `childPct`, item statuses and focus are child-specific. The default chart renders `pct` as its line, `lo`/`hi` as a filled envelope, and the child dot at chronological age with height `childPct` ([chart code, lines 152–161](../raw/js/beautified/page-5f182d70f1f24a3d.js:152)). The source does not name the envelope a confidence interval.

| Baseline example | Curve data | Comparison to served item rates |
|---|---|---|
| One-item Phonetics, ID948, age47 | `pct=lo=hi=.843537` | Start rate `.84` |
| Same, age48 | `pct=lo=hi=.833333` | Start rate `.83` |
| Two-item Developing peer relationships, age32 | `lo=.617778`, `hi=.836591`, `pct=.7271845=(lo+hi)/2` | Served ID694 rate `.62`; other ID619 not served at age32 |
| Same skill, age37 | `lo=.700981`, `hi=.890535`, `pct=.795758` | Served ID694 rate `.70` |
| Developing musical skills, age12 | `pct=.5904693333` | Only ID338 served at rate `.64`; not equal to the mean of served questions |

Evidence: [age42 complete report](../raw/api/result_age42_all_yes_numeric.json), [age6 complete report](../raw/api/result_age06_all_yes_extended.json), and returned-age start lists [age47](../raw/api/start_age48_gw-null.json), [age48](../raw/api/start_age49_gw-null.json), [age32](../raw/api/start_age33_gw-null.json), [age37](../raw/api/start_age38_gw-null.json), [age12](../raw/api/start_age13_gw-null.json). Every curve of a one-item skill has equal pct/lo/hi; every two-item skill curve satisfies pct=(lo+hi)/2 exactly to floating-point tolerance. Inference: `pct` averages underlying item probabilities over the whole skill inventory, with `lo`/`hi` likely the item-rate extrema. Full inventories' exact underlying probabilities are not directly returned, so the inference is stronger than a comparison with the incomplete asked subset but is not server-source proof.

## Independent count-model checks

The age12 ascending and descending sweeps match on global `state`, `devAge`, `band`, `capped` at all 40 equal success counts, while succeeding on very different IDs. Differences remain in the area months and teaser. This rejects a model where each current answer is weighted directly by its displayed rate in a way that distinguishes those patterns. It is consistent with equating a raw count to an ID-set-specific expected-count curve, and also with some Rasch-family models having a sufficient raw score; these two mechanisms cannot be distinguished by the sweep alone.

| Age12 yes count, fixed 39 IDs | Global output |
|---|---|
| 0–16 | below_floor |
| 17–20 | 11 months, building |
| 21–24 | 12 months, on_pace |
| 25–27 | 13 months, little_ahead |
| 28–29 | 14 months, well_ahead |
| 30 | 15 months |
| 31 | 16 months |
| 32 | 17 months |
| 33 | 19 months |
| 34 | 21 months |
| 35–39 | 33 months, capped |

Training an area lookup on the ascending sweep, keyed only by area success count for its fixed answered IDs, predicts all 83 available descending-sweep area outputs exactly, including `atLeast`. This is a held-out pattern check, unlike the broader in-sample grouping conflict counts in the JSON stats file. The latter also include adjacent flips outside the area, duplicates, and additional probes.

Overall devAge is not a simple rounded mean, median, minimum or maximum of reported area months. At ascending count17, area ages are 12,12,8,0 yet overall is11; at the typical threshold profile, areas14,16,12,16 average14.5 but overall is14. See the stats snapshot for exact aggregate-fit counts over all current reports with four numeric area ages.

Chronological age must be included when predicting the `below_floor` state: the same age12 typical vector gives devAge14 and identical area ages at chronological ages0,1,2,3,6,12, but returns below_floor at24,36,48. Numeric devAge/count lookup can be age-independent only conditional on a numeric result being returned. [Cross-age raw evidence](../raw/api/scoring/M_age24_same_age12_typical.json).

## Direct full-inventory norm probe

All 11 Secure Attachment inventory IDs were answered at age12. Counts0–9 return below_floor; count10 returns devAge14, with that area's months14 and no cap; count11 returns devAge15 capped, with that area's months16/atLeast. `10/11=.9090909` is close to curve age14 `.90691118`, supporting expected-proportion inversion. The cap15 is not the curve's last age18 or maximum-pct age17. Its precise ceiling formula remains unresolved by this probe. [Count10](../raw/api/scoring/M_secure_attachment_count10.json), [count11](../raw/api/scoring/M_secure_attachment_count11.json).

The same complete inventory was then tested at chronological age0, exposing numeric values for every count. The following formula predicts all **11/11 uncapped** developmental ages (also 11/12 overall; the exceptional twelfth is capped):

```text
q = number_of_yes / 11
D = max(1, age of curve point minimizing abs(point.pct - q))
```

| Yes | Global devAge | Area months | Nearest whole-month curve prediction | Nearest even-month curve prediction |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 2 | 1 | 0 | 1 | 0 |
| 3 | 1 | 0 | 1 | 0 |
| 4 | 2 | 2 | 2 | 2 |
| 5 | 3 | 4 | 3 | 2 |
| 6 | 4 | 4 | 4 | 4 |
| 7 | 5 | 4 | 5 | 6 |
| 8 | 6 | 6 | 6 | 6 |
| 9 | 9 | 8 | 9 | 10 |
| 10 | 14 | 14 | 14 | 14 |
| 11 | 15 capped | 16 atLeast | 17 | 16 |

Evidence: files `M_secure_age00_count00.json` through `M_secure_age00_count11.json` in [the scoring directory](../raw/api/scoring/). Nearest exposed pct at even ages predicts only **8/11 uncapped** area ages, so area calibration is separate from that simple curve subsampling. The area count lookup itself remains exact for the observed same-ID comparisons. A rounded piecewise-linear inverse also fits these uncapped global examples; these probes do not distinguish the interpolation details.

## Final snapshot and exact band boundaries

Snapshot after all **348 Phase 3 requests**: 446 HTTP200 result records across both phases, including 364 complete responses and 227 reports with a numeric global age. Counts below include repeated requests and thus should not be presented as independent sample sizes.

| Check | Exact matches / comparisons |
|---|---:|
| Band formula below | 227/227 numeric reports |
| Global count lookup, fixed chronological age and effective answered-ID set | 114/114 repeated-key comparisons |
| Numeric global count lookup, ignoring chronological age when a numeric report exists | 115/115 repeated-key comparisons |
| Area count lookup, fixed area's effective answered-ID set | 679/679 repeated-key comparisons |
| Curve stability, fixed skill/inventory | 5,728/5,728 comparisons over 48 groups |
| `reached=count(yes or typical)` | 5,776/5,776 skill records |
| `childPct=reached/total` | 5,776/5,776 skill records |
| Floor of four-area mean | 49/176 full-area reports |
| Rounded/ceiling four-area mean | 24/176 each |
| Median (floor/rounded/ceiling) | 24/176 each |
| Four-area minimum | 2/176 |
| Four-area maximum | 2/176 |

The lookup models canonicalize duplicate IDs using the last supplied value, as established by the duplicate-order validation probes. Without that normalization the deliberate conflicting-duplicate pair appears as a conflict, so normalization is an observed API behavior rather than a silent exclusion.

The final four controls answer yes on exactly `round(sum(served item.rate))` IDs, assigning the yes IDs in a randomized order. This yields **on_pace and devAge exactly equal to chronological age in 4/4 cases**: ages3,12,24,36 use20,22,22,24 yes respectively. See `M_age03_count_matches_expected_rate_sum.json` through the corresponding age36 response. This is stronger evidence for aggregate expected-count equating than the threshold-at-.5 profiles: a deterministic threshold is not the expected Bernoulli success count and need not map to a typical developmental age.

With `r=devAge/max(ageMonths,1)`, the exact observed band rule is:

```text
r < .95               -> building
.95 <= r <= 1.05      -> on_pace
1.05 < r <= 1.15      -> little_ahead
r > 1.15             -> well_ahead
```

Exact boundary probes establish `.95` on_pace ([D19 at20](../raw/api/scoring/M_band_age20_count33.json)), `1.05` on_pace ([D21 at20](../raw/api/scoring/M_band_age20_count34.json)), and `1.15` little_ahead ([D46 at40](../raw/api/scoring/M_band_exact_115_dev46_age40.json)). The lower `.85` boundary concerns floor state, not a fifth band: uncapped D17 at20 (`.85`) is building, while at21 (`.80952`) it is below_floor. The same D14 vector is building at16 (`.875`) and below_floor at17 (`.82353`). Capped D33 remains building at48 (`.6875`), establishing that cap handling bypasses the floor condition that affects those uncapped cases. This supports an uncapped relative floor at `.85`; it does not by itself explain every age0/all-zero lower-support outcome.

## Verdict limits

The evidence decisively rejects wholly cosmetic scoring: different success counts change global numeric ages monotonically in both complete age12 sweeps, area changes follow area counts independently, and a complete skill inventory's raw score inverts its exposed age norm exactly in 11 uncapped cases. The free page does contain cosmetic elements (literal blurred 88s, generic locked bars), and the final controls reveal substantive nonmonotone area projections, alongside unresolved floor/ceiling behavior. If the requested verdict combines score computation, consistency and presentation, **PARTLY REAL** is defensible: real count/norm computation with independently verified area-scoring glitches and cosmetic gating. None of these API experiments establishes clinical validity, representative normative sampling, or accurate developmental measurement; those are separate questions rather than evidence that answer-driven computation is fake.

## Final edge controls: area computation is deterministic but not monotone

The full age12 initial IDs, including calibration, yield the following complete count lookup. Each row uses the same answered IDs within its area. A `+` marks `atLeast=true`.

| Area yes count | Physical (9 IDs) | Cognitive (9 IDs) | Language (10 IDs) | Social-Emotional (11 IDs) |
|---:|---:|---:|---:|---:|
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

The late control series holds every other area's answers fixed at the typical threshold profile. Increasing Cognitive successes 1→2→3→4 changes its month estimate **8→2→0→12**; increasing Social-Emotional successes 2→3→4 changes **6→0→8**. Other three area ages remain unchanged throughout each series. These are direct violations of area monotonicity, not consequences of changing the IDs, other answers, or chronological age. They also confirm that the area independence/count lookup can be exact while the resulting age mapping has pathological low-score behavior. Raw controls: [Cognitive count1](../raw/api/scoring/D3_age12_Cognitive_count01_others_typical.json), [count2](../raw/api/scoring/D3_age12_Cognitive_count02_others_typical.json), [count3](../raw/api/scoring/D3_age12_Cognitive_count03_others_typical.json), [count4](../raw/api/scoring/D3_age12_Cognitive_count04_others_typical.json); [Social-Emotional count2](../raw/api/scoring/D3_age12_Social_Emotional_count02_others_typical.json), [count3](../raw/api/scoring/D3_age12_Social_Emotional_count03_others_typical.json), [count4](../raw/api/scoring/D3_age12_Social_Emotional_count04_others_typical.json). The exact internal cause remains unexplained; nearest-age inversion of noisy/nonmonotone norm data is one possible mechanism, not an observed implementation.

The offline statistics include this full lookup and identify all three decreasing transitions. The previous global monotonicity conclusion remains limited to the two age12 whole-vector sweeps; it does not extend to area scores.
