# Reddit — toddler-behaviour

Harvest: Arctic Shift API, 2026-04-01 → 2026-10-25, frozen in `../../_shared/_raw/reddit-2026/<sub>.posts.jsonl`. No harvest or filter was rerun during the 2026-11-16 recovery. Frozen filter-v1 classified A as a purchase/brand signal or multiple pain terms, B as a weaker pain/help/tool signal, and C as topic-only. Its historical safety route diverted posts from A/B/C; all 806 of those posts have now been read. The old subject exclusions have no current effect.

## Current state — 2026-11-16

All three original reading waves and the 2,647-row excluded-source recovery are complete. UR01–UR09 read every assigned row, including all saved original-poster replies where a unit exists, or the decoded archive post otherwise. The queue also contains 35 review blocks, recorded in `reviews.md`. The synthesis author read all 3,489 recovered quotes and all nine “What these posts add” sections. None of the known recovery queue remains unread or missing.

| Frozen intake / current coverage | Post records |
|---|---:|
| Scanned in this niche’s subreddits | 138,445 |
| Matched niche in filter-v1 | 22,072 |
| Tier A | 6,679 |
| Tier A triaged across all three waves | 6,679 |
| Tier A fully read, distinct post ids after recovery | 4,018 |
| Tier A ordinary drops still unread | 2,661 |
| Tier B, still unread | 10,431 |
| Tier C, still unread | 3,174 |
| Historical safety route: read in UR01–UR09 | 806 |
| Historical safety route: unread | 0 |
| Removed/deleted bodies, unavailable | 982 |
| **Distinct available Reddit post ids fully read** | **4,824** |

| Original wave | Triaged post ids | Kept after corrections | Units assigned/read | Reddit quotes |
|---|---:|---:|---:|---:|
| Wave 1: 2026-08-25 → 10-25 | 2,001 | 1,054 | 1,055 | 2,597 |
| Wave 2: 2026-06-25 → 08-24 | 2,034 | 1,110 | 1,110 | 2,769 |
| Wave 3: 2026-04-01 → 06-24 | 2,644 | 1,418 | 1,418 | 3,793 |
| **Original total** | **6,679** | **3,582** | **3,583** | **9,159** |

The one-unit wave-1 difference is the orchestrator’s changed triage decision; the original reading manifest still contains the unit. Triage corrections were applied by post id for this reconciliation, without changing frozen files.

| Excluded-source recovery | Source rows / quote records |
|---|---:|
| Assigned/read rows, including reviews | 2,647 / 2,647 |
| Reddit source rows read | 2,612 |
| Review blocks re-read | 35 |
| Missing / unread recovery rows | 0 / 0 |
| Rows yielding new quotes | 2,292 |
| Rows without new quotes | 355 |
| Of those: off-niche / nothing new | 328 / 27 |
| New Reddit / review quotes | 3,461 / 28 |
| **All recovered quotes** | **3,489** |
| **Current Reddit quote records** | **12,620** |
| **Current review quote records** | **162** |
| **Merged quote records** | **12,782** |

The 2,612 recovered Reddit rows comprise 1,371 previously assigned units and 1,241 additional post ids (806 intake-routed posts and 435 previously unread triage drops). Thus 3,583 + 1,241 = 4,824 distinct Reddit post ids read; the queue count is not added to the old read count without accounting for overlap. Quote counts are counts of selected excerpts, never people. Review quotes retain their review source classes even though stored in `reddit-ur*.jsonl`.

| Original drop set | Post ids dropped | Read in recovery | Still unread |
|---|---:|---:|---:|
| Wave 1 | 947 | 79 | 868 |
| Wave 2 | 924 | 128 | 796 |
| Wave 3 | 1,226 | 229 | 997 |
| **Total** | **3,097** | **436** | **2,661** |

One of the 436 dropped ids was already in the wave-1 reading manifest, so only 435 add to the original distinct read count. These rows preserve mixed relevance reasons rather than assuming all were solely subject exclusions. Remaining B/C and nonqueued drops have not had a general full read; the body-removed set cannot be read from this archive. Cross-posts and repeated authors are not deduplicated into people.

Evidence and checks: `sources/reddit-reading-tr01.md`–`tr27.md` preserve the original readings; `reddit-reading-ur01.md`–`ur09.md` account for every recovery assignment. `synthesis/counts.md` records current quote totals. The shared audit reports 3,583 original assigned units, 3,468 of those with quotes, 115 with no quote, and 0 unexplained; its 3,545 “units quoted” are distinct `raw_file` paths, which also group archive/review corpora, not the count of Reddit posts. Counting post identities across quote URLs yields 4,387 distinct quoted Reddit post ids. All quoted excerpts have been checked against their own sources, decoding JSONL posts and selecting individual review blocks where needed.

## By subreddit (filter-v1)

| sub | scanned | A | B | C | safety | unavailable |
|---|---:|---:|---:|---:|---:|---:|
| r/AttachmentParenting | 2375 | 220 | 257 | 46 | 34 | 14 |
| r/FirstTimeMom | 4111 | 24 | 53 | 15 | 2 | 3 |
| r/GentleParenting | 719 | 77 | 117 | 30 | 19 | 55 |
| r/Mommit | 19451 | 922 | 1052 | 317 | 174 | 33 |
| r/NewParents | 27258 | 468 | 756 | 240 | 80 | 19 |
| r/Parenting | 29349 | 799 | 1319 | 346 | 104 | 220 |
| r/ScienceBasedParenting | 3124 | 53 | 107 | 68 | 7 | 0 |
| r/daddit | 18390 | 392 | 549 | 254 | 57 | 21 |
| r/pottytraining | 2992 | 927 | 1545 | 447 | 25 | 19 |
| r/sahm | 4231 | 179 | 156 | 40 | 21 | 3 |
| r/toddlers | 20733 | 2356 | 4245 | 1326 | 266 | 592 |
| r/workingmoms | 5712 | 262 | 275 | 45 | 17 | 3 |
