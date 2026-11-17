# Reddit August–December batch 03 — complete

This is a new continuation of baseline `2613feb3`, using parent-supplied local archive material only. No network collection, outreach, subagents, or commits were performed. The publisher dataset is `yikeee/reddit-subreddits25`, pinned commit `ea497c510aa68765c07ed744ec9f84d68bbedf7f`. Publication rights/provenance, author authenticity, transactions, and live thread completeness remain unverified. Statements describe historical 2025 accounts, not current product features, prices, legal rules, or medically valid advice.

## Exact coverage

The fresh packet contains 6,597 tier-A candidates. Original batch 03 assigned 2,205 cards in 37 files. Before this reader opened its final ten files, root transferred their 620 IDs to rad04. The revised manifest is `_raw/reddit-deep/aug-dec-2025-wave-v1/assignments/batch-03-after-transfer.json`: **all 1,585 cards in 27 files**, without topic caps or quote targets. Original manifests and raw units were preserved.

| Step | Actual result |
|---|---:|
| Assigned cards fully read and human-triaged | 1,585 |
| Card drops, with per-ID reasons | 464 |
| Human keeps requiring full original reads | 1,121 |
| Complete original titles/bodies read | 1,121 |
| All available identifiable OP replies read | 50 |
| Additional exact native non-OP parent comments read | 18 |
| Post-read eligible units | 917 |
| Post-read excluded units | 204 |
| Partial reads / unread kept originals / unread available OP replies | 0 / 0 / 0 |
| Excerpts | 207 from 206 post IDs |
| Post-body excerpts / OP-reply excerpts | 205 / 2 |
| Excerpts explicitly restricted to research use | 39 |

The denominator includes every kept original, including full-body safety, clinical, promotional, duplicate and context exclusions. Eligible means retained bounded research context, not proven demand or approved advertising material. These counts are records and works, never independent people, independent buyers, market prevalence, or live-thread coverage. The 464 drops were listing cards, not full originals; their unopened full units must not be described as read. No additional card-drop full inspections were performed in this batch.

Complete originals by community: BabyBumps 221; BabyBumpsCanada 25; BabyBumpsandBeyondAu 48; BabyLedWeaning 30; BeyondTheBumpUK 55; ExclusivelyPumping 211; NewParents 531. These sum to 1,121. The individual saved units total 2,666,008 UTF-8 bytes. All 53 kept-only frozen views (1,766,871 bytes) were displayed and read fully, one view per tool call; no truncated view was accepted as complete.

## Reading boundaries

All 50 available identifiable OP replies belong to the 30 BabyLedWeaning units with a comment source. Their own native bodies, dates, canonical URLs, post links and nondeleted matching authors were checked. The other **1,091 kept originals have no publisher comment file**: zero archived replies does not mean no replies existed live. There are 330 available non-OP comments in the assigned kept units; only 18 exact parents needed for context were additionally read. **312 available non-OP comments remain unread.** None is claimed as a complete discussion thread.

`scratchpad/reddit-augdec-03/final-coverage.json` lists every read post ID, every read OP comment ID, all 18 auxiliary parent IDs, all 312 available unread non-OP IDs, and the exact 1,091 post IDs with unavailable comment sources. Native auxiliary parents are separately logged in `sources/reddit-augdec-03-auxiliary-read.jsonl`; they are not additional customer quotes or original posts. Embedded quoted comments inside an original were read as context, not counted as newly inspected commenters.

The per-ID card decisions are `_raw/reddit-deep/triage/augdec-03.tsv`. The 27 complete card-file reads and hashes are in `scratchpad/reddit-augdec-03/triage-reading-ledger.jsonl`. The 53 reading-view completion records are in `scratchpad/reddit-augdec-03/full-reading-chunks.jsonl`. Every full original and OP count is accounted for exactly once in `sources/reddit-augdec-03-reading.jsonl`. Quoted `raw_file` fields always name an immutable individual primary unit, never a card or rewritten view.

## Interpretation and duplicate handling

Ordinary fatigue, worry, therapy history and resolved NICU experience were not automatically treated as crises. Full-body exclusions include explicit death-related distress (`1pvv7dc`), recent inpatient postpartum treatment (`1n9safs`), current neonatal dehydration/jaundice, feeding/readiness and allergy complications, open wounds and infection, and individualized supply/medication questions. Those do not become report opportunities merely because they mention spending or ask for a plan. Examples deliberately excluded despite superficially useful demand language include low-weight infant meal-list request `1nfo3li`, PT/OT feeding-progression guide request `1mrzulv`, and medically complicated paid sleep-product account `1mrt9i2`.

Explicit creators and promotion risks are separately recorded, not independent buyers: own sleep-guide promotion `1mjbsed`; campaign-tagged Tinyhood link `1njgvau`; branded cry-translator promotion `1n86eh5`; BeFreed recommendation `1o1ieko`; linked tracker posts `1ni0r25` and `1ompfl3`; and endorsement-style warmer posts `1on85p1` and `1onb7x6`. Exclusion means independence was unestablished, not an allegation of fraud or a proven seller identity. Less conclusive named-site/AI-photo questions are retained only with uncertainty: the data-book excerpt rad03-0192 is research-only; `1olq5z1` was not quoted. The feeding-app purchase rad03-0206 includes promotional sale language elsewhere, so its claimed payment is not a verified independent transaction or current price.

`scratchpad/reddit-augdec-03/duplicate-human-review.jsonl` records manual exact/near-body comparisons and related updates. Later duplicate copies were not independent corroboration. The earliest NewParents bedtime work `1mjyh1i` supersedes later BabyBumps `1mjyq8j`; the earliest Australian-couple/London-move work `1o21nne` supersedes later BabyBumps `1o3khlx`. Both later records were changed to excluded duplicates without changing quotes. Other cases include identical success stories, branded packaging accounts, hair-care reposts, same-party theme updates and related feeding/nanny accounts. A possible shared household is labeled possible, not asserted identity.

All **26 machine duplicate-flag groups touching the read scope** were reviewed against the in-scope bodies; their exact index membership and limits are in `scratchpad/reddit-augdec-03/exact-body-flag-scope-review.jsonl`. External index copies are not additional full original reads. Root owns cross-assignment reconciliation. Only two quoted works touch those exact flags: rad03-0040 selects earliest gifted Vista body `1p3ysdn` over `1p3yssl`/`1p3ytwt`; rad03-0166 is the sole selected in-scope Thrive question `1mtjmcb`, with earlier matching `1mtjiug` explicitly linked by root instruction. Both records carry duplicate-group metadata. Neither copy adds independent corroboration. No quoted post currently duplicates another wave’s quoted post ID.

OP follow-ups materially correct interpretation: `1pljxxh` retracts its opening paywall impression as a glitch. Only its clarifying OP replies are quoted (rad03-0089 and 0090). The original opening must not be cited as a continuing paywall limitation. Research-only Willow Method recommendation rad03-0088 has unverified affiliation/payment; it is not a confirmed buyer.

## Verification and files

`voice/reddit-augdec-03.jsonl` contains rad03-0001 through rad03-0207. `sources/reddit-augdec-03-verification.json` is the final complete audit. It verifies exact assignment/triage and keep/read ID sets, unique records, raw-unit hashes, every complete original body against native submissions, all OP identities/links/counts, all displayed view bodies and immutable view hashes, exact auxiliary native body hashes, and every excerpt against its **own native post or comment body** with whitespace-only normalization. Case, punctuation and typography are unchanged. It also checks native timestamps/canonical URLs, README vocabulary, context length, per-ID quote ledgers and global ID uniqueness. **Zero errors and zero strict quote failures.** The copied `_tools/verify_quotes.py` also reports **207 quotes, zero failed**.

Two uncertain pregnancy phases were conservatively changed to `unknown`, with IDs and reasons in `scratchpad/reddit-augdec-03/metadata-corrections.jsonl`; raw text and excerpts were unchanged. Added theme definitions are in `scratchpad/reddit-augdec-03/theme-glossary.md`. Interpretation and proposed tests are in `synthesis/reader-notes-reddit-augdec-03.md`. Final output hashes are frozen in `scratchpad/reddit-augdec-03/final-freeze.json`.
