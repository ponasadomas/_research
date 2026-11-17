# Reddit — sleep-baby

Harvest: Arctic Shift API, 2026-04-01 → 2026-10-25, saved untouched in `../../_shared/_raw/reddit-2026/<sub>.posts.jsonl` (log: `harvest.log`). Historical filter run: `../../_shared/_tools/niche_filter.py sleep-baby` → `../_raw/reddit/filter-v1/` (frozen). Rule: A = topic + explicit purchase/paid-tool/brand signal or 2+ distinct pain words; B = topic + one pain word, a help question or a generic tool word (plan, method, guide, book, app, class, schedule, routine); C = topic only; safety = the former safety lane, routed away from full reading at intake; all 1,641 identities are now read; non-core subs also need the niche's person regex.

## Historical intake and wave-1 ledger

| step | count |
|---|---:|
| posts scanned in this niche's subreddits | 174915 |
| matched the niche (A+B+C+safety+unavailable) | 53451 |
| tier A | 15679 |
| tier B (on disk, unread) | 27352 |
| tier C (on disk, unread) | 7324 |
| safety-routed intake identities (all now read by UR) | 1641 |
| body removed or deleted | 1455 |
| **wave 1 cards: tier A dated 2026-08-25 → 10-25** | 4577 |
| historical tier A outside wave 1 (later reading below; frozen ids in `filter-v1/wave1/unread-rest.jsonl`) | 11102 |
| triaged (wave 1, 6 Sonnet readers T1–T6) | 4,577 |
| kept (incl. 5 orchestrator corrections) | 2,630 |
| read in full (21 readers R01–R21, main model; units = post + the original poster's replies) | 2,630 |
| units with at least one quote · quotes | 2,486 · 6,659 |

**Historical cut rule (2026-10-25; current coverage below):** tier A outside the last two months is listed as unread, by id, not dropped. Reason: about 46,000 tier-A posts across the five niches would need about 70 triage agents before reading, and the owner's monthly usage limit was hit once on 2026-10-25. Wave 2 = tier A 2026-06-25 → 08-24, then earlier.

## By subreddit (filter-v1)

| sub | scanned | A | B | C | safety | unavailable |
|---|---:|---:|---:|---:|---:|---:|
| r/AttachmentParenting | 2375 | 442 | 613 | 126 | 68 | 116 |
| r/FirstTimeMom | 4111 | 201 | 344 | 98 | 20 | 68 |
| r/GentleParenting | 719 | 16 | 28 | 3 | 8 | 5 |
| r/Mommit | 19451 | 1329 | 1520 | 521 | 250 | 72 |
| r/NewParents | 27258 | 2924 | 5567 | 2035 | 247 | 243 |
| r/Parenting | 29349 | 948 | 1645 | 483 | 121 | 362 |
| r/ScienceBasedParenting | 3124 | 85 | 214 | 171 | 16 | 15 |
| r/beyondthebump | 16469 | 1632 | 2274 | 859 | 178 | 65 |
| r/beyondthebumpUK | 6909 | 654 | 1124 | 485 | 62 | 73 |
| r/daddit | 18390 | 625 | 965 | 420 | 107 | 39 |
| r/sahm | 4231 | 297 | 306 | 59 | 39 | 12 |
| r/sleeptrain | 16084 | 4644 | 9676 | 1189 | 345 | 67 |
| r/toddlers | 20733 | 1560 | 2762 | 805 | 163 | 314 |
| r/workingmoms | 5712 | 322 | 314 | 70 | 17 | 4 |

## Reading (2026-10-25)

Units: `../../_shared/_raw/reddit-2026/units/`. Chunks: `../_raw/reddit/read-v1a/` (R01–R12) and `read-v1b/` (R13–R21; R22's single chunk folded into R21). Per-reader ledgers: `reddit-reading-r01.md` … `r21.md`. 144 units read with no quote, each named in a reader ledger (cross-posts, safety exclusions, nothing usable). Verify: `python3 -I ../_tools/verify_quotes.py` → 6,659 quotes, 0 failed. Audit: `../synthesis/counts.md`, `audit-safety-hits.tsv`, `audit-spotcheck.md`, `restricted-ids.md`.


## Completed waves and re-reading — integrated 2026-11-17

The original four manifests (`read-v1a`, `read-v1b`, `read-w2`, `read-w3`) assign **8,747 distinct unit identities**: wave 1 **2,630**, wave 2 **2,547**, wave 3 **3,570**. Their voice files contain **25,185 Reddit quote records**; the separate review file contains **234**, giving the pre-UR total **25,419**.

UR01–UR24 completed **7,122/7,122** omission/review identities: **6,213** rows supplied **8,772 new quote records**, **909** supplied no new quote and a ledger reason, **0** are missing or unfinished. The voice-file totals equal the sums in all 24 ledgers. All **seven digest shares** cover these 8,772 records; every money/request-index id is carried into findings. Original queue reasons, assignments, voice fields, digests and `reddit-reading-*.md` ledgers are preserved unchanged.

The queue has **4,089** identities already assigned in the original manifests and **3,033** newly read post identities. The union read across both runs is therefore **11,780**, not 8,747 + 7,122. This includes all **1,641** historical safety-intake identities and **1,392** additional tier-A triage-drop identities. Queue completion includes relevance-only, duplicate and nothing-new outcomes; it does not mean every row produced a new quote.

### Current candidate-set coverage

Sets are keyed by `<subreddit>-<postid>`. For each frozen `filter-v1/*-candidates.jsonl`, form its candidate set, then subtract the union of original manifest stems and completed UR assignment ids. These filter lanes are disjoint; original and UR reads overlap as shown.

| frozen lane | candidate identities | original assigned | UR queue | union read | remaining unread |
|---|---:|---:|---:|---:|---:|
| A | 15,679 | 8,747 | 5,481 | 10,139 | 5,540 |
| B | 27,352 | 0 | 0 | 0 | 27,352 |
| C | 7,324 | 0 | 0 | 0 | 7,324 |
| former safety lane | 1,641 | 0 | 1,641 | 1,641 | 0 |

The **40,216 ordinary unread A/B/C identities** are outside the completed omission/review queue. Another **1,455** candidate bodies were removed/deleted at harvest and remain unavailable; that is not an unfinished UR read. The earlier ledger's wave-1-only and safety-unread statements are historical and superseded by this table.

### Source limits and current quote records

Unit files supply the saved post plus archived original-poster replies. Where a unit does not exist, the reader decoded the matching post from the saved subreddit archive; absent replies were not invented. Completion cannot recover text absent from disk or prove that anonymous historical category notes identified every omitted passage. Diagnoses, medication effects, safety claims, allegations and causal explanations remain the speakers’ reports.

The rebuilt merged file has **34,191 distinct quote ids**, comprising **33,957 Reddit + 234 review records** in **88 voice files**, with **0 active restrictions**. Counts describe selected quote records, never people or prevalence; these re-read posts were chosen to revisit omissions and review candidates. Distinct raw-file paths in the stock audit are not post-identity coverage because one archive path contains many posts. See `synthesis/counts.md` for both measures.

Findings cite **4,407 distinct ids**, including **2,757 full UR quote fields**, preserving all **1,650** earlier cited ids. The closing section of `synthesis/unfilter-report.md` records the checks and remaining limits. No new collection, network access or git operation was used.
