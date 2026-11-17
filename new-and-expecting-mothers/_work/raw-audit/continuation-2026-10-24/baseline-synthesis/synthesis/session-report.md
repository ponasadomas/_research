# Deepening pass — exact coverage and continuation

2026-10-24. Reopened after the owner identified missing Reddit and forums. The original synthesis has been preserved in `_raw/pre-integration-synthesis-2026-10-24/`; it is superseded by the current findings. Nine collector/reader agents worked in waves, with at most three active alongside the root agent. No outreach, accounts, payments, advertisements, site changes or commits were performed.

**Result: 1,296 exact-source excerpts, 878 additions to the initial 418; 977 context-bearing language-bank entries.** All eligible items assigned for full reading are complete. Remaining unhandled candidates and safety exclusions are explicitly separate.

The lead test is a weekly baby-meal/lunch preparation report based on the household's actual routine. The earlier first-time/low-cooking restriction was withdrawn. This is not commercial validation. See [the decision](niche-opportunities.md), [findings](findings.md), [machine recount](counts.md), [coverage JSON](coverage.json) and [audit](audit.md).

## Downloaded → matched/triaged → kept → read → quotes

Units differ by source and must not be summed as people. Original post records, whole discussions, reviews and seller pages are separate units. Exact counts are recomputed by `_tools/reconcile_deep_coverage.py` and `_tools/audit_database.py`.

| Source | Downloaded / saved scope | Matched or human triaged | Kept for full reading | Actually read | Excerpts |
|---|---|---|---|---|---:|
| Reddit, nine communities | 112,665 July–December 2025 post records; 98,000 readable bodies; 147,579 comments in two communities | 8,284 A candidates; all 1,661 July A cards triaged; separate 39-post payment-language cohort | 1,031 initial July keeps; 933 eligible after full reading; payment cohort overlaps seven July keeps | **1,063 distinct original post IDs**, 449 OP replies and seven exact other comments | 298 |
| JustParents, eight boards | 505 discussions / 530 thread pages / 3,472 posts | All 505 cards | 94 initial; 78 after full reading | **94 complete visible discussions / 706 posts** | 26 |
| MoneySavingExpert, two boards | 1,356 listing cards; 343 kept discussions / 620 pages / 4,736 posts | 480 matched cards, all triaged | 343 initially | **328 complete visible discussions / 4,423 posts**; fifteen safety exclusions with 82 records inspected/read, 231 later posts deliberately unread | 297 |
| GeoBaby publisher archive, three boards | 1,224 listing cards; 183 discussions / 251 pages / 1,422 posts | 594 broad matches; 231 declared-scope cards triaged | 183 initially; 169 after full reading | **183 complete visible captures / 1,422 posts**, including quoted context | 111 |
| Parenting Stack Exchange API | 1,155 dated questions; 248 candidates with 514 answers and 1,356 comments saved | All 248 candidate cards | 119 initially; 106 after full reading | **119 complete available API threads**, 298 answers and 713 comments | 134 |
| Original app and book reviews | 204 exposed app-review units and fifteen book-review units | Exposed units read; complete store histories unavailable | 219 units for reading | **219 full original review units** | 209 |
| Public offers | 48 successfully read offer pages | Forty-one discovered offers/substitutes noted | Forty-one teardowns | All 48 captured public offer texts; no paid contents or checkout purchase | 50 |
| Meta Ad Library | Twenty searches; 68 on-niche IDs retained | Initial sixteen queries plus four report/registry follow-ups | 68 visible ad texts | All retained visible text read; videos and unloaded variants not viewed | 6 |
| Official guidance | Twelve responses; eleven valid documents and one 404 in the initial pass | Clinical/product-boundary checks | Eleven | Public guidance read; not customer-demand evidence | 10 |
| Legacy community search extracts | Sixty-two retained extract units in initial pass | Extract-only selection | Sixty-two | Full available extracts, **zero original reads credited from these snippets** | 155 |

Forum reconciliation: **1,031 discussions / 9,630 posts captured**, 620 provisional reading selections, **605 discussions fully read**, fifteen safety inspections. The complete discussions contain **6,551 posts**. Another 82 posts were inspected/read at the safety boundaries; their completion status is not inflated. The other 2,766 JustParents posts were in 411 card-dropped discussions. Some original GeoBaby questions are absent/uncertain despite complete visible pagination.

The native archive scale is not human reading: eleven complete published native files contain 2,949,821 scanned JSON records. The fixed six-month window and actual original reads above are the relevant research denominators. The public publisher's license/provenance and live completeness remain unverified.

## Verification summary

```text
TOTAL 1296 quotes, 0 failed
TOTAL 214 id references, 2 exact quote pairs, 0 failed
```

The latter is the current findings/opportunity/success-story reference check. Final logs are under `_raw/audit/deep-wave/`. Strict source-specific native-author checks also pass. All 49 new hits from the expanded safety regex were manually reviewed. Forty new random source/context spot checks and two additional targeted checks are recorded; conservative metadata corrections and three boundary-only flags are logged. Initial frozen audit samples were preserved. See `audit.md` for scope and limits.

## Exact unread and unavailable inventory

| Remaining material | Exact location / interpretation |
|---|---|
| **6,597 unhandled August–December A candidates** | `_raw/reddit-deep/final-unhandled-A.jsonl`; their cards occur in 110 existing chunks listed in `outside-july-card-queue-v1.jsonl`. Twenty-six of the original 6,623 outside-July candidates were completed in the payment cohort. |
| **625 July card-dropped A original bodies** | `_raw/reddit-deep/final-A-reading-inventory.jsonl`, status `card_excluded_original_unread`. Initial drops totaled 630; five were separately read in the payment cohort. |
| **51,252 B and 38,463 C original bodies** | `filter-v1/B-candidates.jsonl`, `C-candidates.jsonl` and native `windows/2025-h2-v1/`. One B post, 1oth01f, was read in the payment cohort. Not claimed irrelevant or read. |
| **14,665 unavailable bodies** | `filter-v1/unavailable-candidates.jsonl`; empty/deleted/removed records, not recovered text. |
| Other archived comments | Window comment files; exclude exact read IDs in `final-read-post-ids.json`. The focused kept queue has 1,789 unread non-OP comments; the whole July A auxiliary packet has 3,174 after its seven exact reads. Seven communities' comment files are unavailable, not merely unread. |
| **411 JustParents discussions / 2,766 posts** | `sources/forums-deep-thread-registry.jsonl` minus read IDs in the effective-kept manifest; card-excluded original bodies remain saved. |
| **231 later MSE safety-tail posts** | `_raw/oblique-deep/final-safety-unread-tails.jsonl` gives all fifteen units and exact read boundaries. Deliberately excluded from marketing extraction. |
| Q&A unselected originals | 129 card exclusions in `_raw/qa-deep/reconciliation-qdeep01.tsv`; 907 filter-unmatched questions in `all-questions.jsonl` minus `candidates.jsonl`. All 119 kept threads are complete. |
| Broader source gaps | `sources/not-harvested.md`: full review histories, source restrictions, uncollected main communities, YouTube top-200/comments, private/social sources, full books and post-purchase contents. |

The old full-comment A corpus has 865 frozen chunks. It includes material partly read as posts/OP replies and separately unread non-OP discussion; it is not an 865-chunk wholly unread primary queue. Do not rewrite cited corpora or restart completed reader files.

## Continuation and cost in reading units

For the next Reddit expansion, distribute the **110 named card chunks** across roughly **three readers × 37 chunks** (one gets 36), skipping the exact handled IDs. Then freeze **every newly human-kept original plus all identifiable available OP replies** into new reading units. The number of full-read chunks is determined after triage, not by a top-N or a pattern-saturation claim. Existing archive files supply the data; no fresh download is needed. B/C are a separate, much larger queue requiring a stated next scope.

No eligible kept forum or Q&A original needs another reading wave. A new global market claim would still need current buyer-country research and actual Mamivio purchase/use data. The proposed twelve interviews and five paid manual fulfillments in `niche-opportunities.md` are future work, not completed fieldwork or a statistical sample. YouTube/comment collection needs a permitted route; access restrictions are not solved by assigning more readers.

No raw file exceeds 100 MB. Oversized original compressed Reddit files were split losslessly into ≤95,000,000-byte parts with reassembly hashes. Raw sources remain unignored. No commit was made; `first_command_research.md` was left untouched.
