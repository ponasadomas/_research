# Reddit — pregnancy-birth

Harvest: Arctic Shift API, 2026-04-01 → 2026-10-25, saved untouched in `../../_shared/_raw/reddit-2026/<sub>.posts.jsonl` (log: `harvest.log`). Filter: `../../_shared/_tools/niche_filter.py pregnancy-birth` → `../_raw/reddit/filter-v1/` (frozen). Rule: A = topic + explicit purchase/paid-tool/brand signal or 2+ distinct pain words; B = topic + one pain word, a help question or a generic tool word (plan, method, guide, book, app, class, schedule, routine); C = topic only; safety = the historical subject-match lane, which bypassed ordinary A/B/C triage; all named rows are now re-read; non-core subs also need the niche's person regex.

## Historical intake and wave-1 ledger

| step | count |
|---|---:|
| posts scanned in this niche's subreddits | 188283 |
| matched the niche (A+B+C+safety+unavailable) | 81978 |
| tier A | 13869 |
| tier B (on disk, unread) | 31785 |
| tier C (on disk, unread) | 21664 |
| historical safety lane (now all re-read) | 8822 |
| body removed or deleted | 5838 |
| **wave 1 cards: tier A dated 2026-08-25 → 10-25** | 3757 |
| tier A outside wave 1 (historical inventory; later waves triaged these) | 10112 |
| triaged (wave 1, orchestrator-verified TSVs incl. corrections) | 3,757 |
| kept | 2,860 |
| read in full (units = post + the original poster's replies) | 2,860 |
| wave-1 units with at least one quote · quotes | 2,181 · 5,446 |

**Cut rule (2026-10-25):** tier A outside the last two months is listed as unread, by id, not dropped. Reason: about 46,000 tier-A posts across the five niches would need about 70 triage agents before reading, and the owner's monthly usage limit was hit once on 2026-10-25. Wave 2 = tier A 2026-06-25 → 08-24, then earlier.

## By subreddit (filter-v1)

| sub | scanned | A | B | C | safety | unavailable |
|---|---:|---:|---:|---:|---:|---:|
| r/BabyBumps | 26597 | 2027 | 4419 | 3257 | 1129 | 3042 |
| r/Doulas | 493 | 153 | 108 | 118 | 16 | 43 |
| r/FirstTimeMom | 4111 | 160 | 330 | 198 | 58 | 138 |
| r/Mommit | 19451 | 1097 | 1515 | 824 | 380 | 131 |
| r/NewParents | 27258 | 869 | 1291 | 605 | 147 | 103 |
| r/PregnancyUK | 6941 | 986 | 2171 | 1360 | 509 | 195 |
| r/beyondthebump | 16469 | 1233 | 2012 | 1210 | 326 | 122 |
| r/beyondthebumpUK | 6909 | 375 | 554 | 324 | 58 | 37 |
| r/daddit | 18390 | 419 | 658 | 419 | 146 | 79 |
| r/pregnant | 61664 | 6550 | 18727 | 13349 | 6053 | 1948 |

## Current reading coverage — 2026-11-17

All three retained reading manifests are complete: `read-v1` 2,860 units, `read-w2` 3,083 and `read-w3` 4,331 (10,274 distinct unit identities). UR01–UR40 completed every row of the deduplicated 11,880-row exclusion queue: 2,226 named reading units plus 9,654 posts (8,822 historical safety-lane posts and 832 triage drops). The 2,226 unit identities also occur in the original assigned-unit set, so these are overlapping read sets, not additive counts of independent posts or people. Their union is 19,928 known full-read post identities.

The 40 unchanged UR ledgers reconcile exactly to the assignments and their voice files: 11,539 rows have new quotes, 341 have explained no-new-quote results, 15,768 new quotes in total, and 0 missing/unread assignments. Archive rows used their saved title/selftext; absent replies were not inferred. The 13 unchanged digests guide the revised findings, whose money/request indexes are fully carried forward. The complete corpus has 34,346 quotes (34,065 Reddit and 281 public app/book reviews), 113 reader voice files and no active quote restrictions. Findings cite 11,273 distinct ids, including 7,961 re-reading ids; all previous explicit ids survive.

### Still without a recorded full read

The calculation is by `subreddit-id`: take the union of stems in the three original `chunks.jsonl` manifests and ids in the completed UR queue; subtract that set from each frozen candidate file. A/B/C/safety/unavailable are disjoint intake tiers. This calculation does not call a relevance decision a full read and does not confuse archive paths with individual posts.

| frozen intake tier | distinct posts | known full reads | no recorded full read |
|---|---:|---:|---:|
| A | 13,869 | 11,106 | 2,763 |
| B | 31,785 | 0 | 31,785 |
| C | 21,664 | 0 | 21,664 |
| historical safety lane | 8,822 | 8,822 | 0 |
| unavailable / deleted body | 5,838 | 0 | 5,838 |

The ordinary available A/B/C backlog is 56,212 distinct posts. The 5,838 unavailable bodies are a separate source limitation. No named exclusion-queue row remains unread. Additional subreddits, older windows, forums, blocked platforms, paid product contents and owner/customer data remain the gaps described in findings §13; no new collection was attempted. Historical selection rules in the earlier ledger and run notes have no force as subject exclusions.
