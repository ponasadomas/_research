# Reddit — sleep-mother

Harvest: Arctic Shift API, 2026-04-01 → 2026-10-25, saved untouched in `../../_shared/_raw/reddit-2026/<sub>.posts.jsonl` (log: `harvest.log`). Frozen intake: `../_raw/reddit/filter-v1/`. A = topic plus purchase/brand signal or multiple pain words; B = topic plus one pain/help/tool signal; C = topic only. Historically the safety regex routed 425 posts into a separate tier before ordinary triage. That exclusion is retired; the frozen artifacts document history and were not regenerated. Non-core subreddits also required the niche's person regex.

## Current ledger — 2026-11-16

| measure | count |
|---|---:|
| posts scanned in this niche's subreddits | 247503 |
| matched the niche, all frozen tiers including unavailable | 8056 |
| original-wave assigned Reddit post/unit identities | 1120 |
| original-wave Reddit quotes / review quotes | 2961 / 44 |
| UR assigned/read rows, all sources | 918 / 918 |
| UR Reddit identities / saved review rows | 905 / 13 |
| overlap of original and UR Reddit assignments | 223 |
| distinct Reddit identities recorded as read, union | 1802 |
| UR rows with new quotes / without new quotes | 849 / 69 |
| UR quotes, all read for synthesis | 1238 |
| UR Reddit quotes / review quotes | 1226 / 12 |
| current Reddit quotes / app-book review quotes | 4187 / 56 |
| current quotes, all fourteen voice files | 4243 |
| distinct Reddit post identities with quotes | 1719 |
| read Reddit identities without a selected quote | 83 |
| findings: distinct cited ids / UR cited ids | 1583 / 256 |
| previous findings ids retained | 1327 |
| UR missing sources / unfinished reads | 0 / 0 |
| active restrictions | 0 |

UR01–UR04's immutable `reddit-reading-ur*.md` ledgers record every row and its result. All four “What these posts add” sections and every one of the 1,238 quotes were read for this integration. Actual source reads were 343 complete frozen Reddit units (including available archived OP replies), 562 decoded archive title/body records, and 13 saved reviews. A queue label of `post` did not prevent using an existing unit. A complete archive post does not recover replies absent from the archive. The 69 no-new-quote rows comprise 58 off-niche and 11 duplicate/nothing-new results; no assignment is left unread.

The 223 original/UR overlapping Reddit assignments cover the report's 91 whole reader exclusions plus 132 partial-omission/trim candidates. The additional 682 Reddit reads cover 425 safety-lane posts and 257 subject-related triage candidates, with the queue's mixed-relevance reasons retained. All 918 queue ids match the union of the four assignment TSVs, without duplication. This completes the known re-reading queue, without claiming that unlogged historical omissions cannot exist.

### Remaining full-read inventory

| frozen tier | posts | read identities in that tier | still unread in full |
|---|---:|---:|---:|
| A | 3023 | 1377 | 1646 |
| B | 3694 | 0 | 3694 |
| C | 882 | 0 | 882 |
| historical safety lane | 425 | 425 | 0 |
| unavailable bodies | 32 | 0 | 32 unavailable |

Method: union the post keys from the three original `read-v1`, `read-w2`, `read-w3` manifests with the 905 Reddit keys in the UR TSVs. Subtract that union from each `filter-v1/{A,B,C,safety,unavailable}-candidates.jsonl` key set (`subreddit + '-' + id`). The tiers are disjoint in this frozen intake, so the ordinary full-read remainder is 6,222 available posts, plus 32 unavailable bodies. All tier-A date ranges were triaged, but the 1,646 ordinary triaged-out tier-A posts were not thereby read in full. The superseded blanket claim that all tier A had been read, and that safety posts were still unread, is corrected here and in findings.

These are counts of post identities or assignments where labelled, not people. Quote counts remain counts of selected quotes; crossposts, follow-ups and multiple excerpts are not independent parent experiences. `synthesis/counts.md` distinguishes these identities from the audit's raw-file-path coverage (1,246 paths, 1,098 original assigned paths quoted, 22 original paths without quotes). The twelve new app-review quotes are stored in UR files but counted by source; the thirteen reassessed review rows are part of the original 279 saved review units. `sources/reviews.md` and all reading ledgers retain their historical decisions; old subject/role restrictions there have no active force.

### Original wave-1 record, retained as history

The first wave triaged 910 tier-A cards dated 2026-08-25 → 10-25 and assigned 315 units; 278 supplied 834 quotes, with 37 no-quote units named in the reader ledgers. The older 222-unit/696-quote line was an intermediate count, not the completed wave. The other 2,113 tier-A cards were scheduled for later date waves; waves 2 and 3 subsequently assigned 383 and 422 units. The original usage-limit cut explains that staging, not a present unread-date-range decision. No corpus or raw file was rebuilt for this integration.

## By subreddit (filter-v1)

| sub | scanned | A | B | C | safety | unavailable |
|---|---:|---:|---:|---:|---:|---:|
| r/BabyBumps | 26597 | 137 | 174 | 78 | 27 | 5 |
| r/FirstTimeMom | 4111 | 42 | 48 | 6 | 3 | 0 |
| r/Mommit | 19451 | 246 | 201 | 55 | 43 | 3 |
| r/NewParents | 27258 | 526 | 639 | 176 | 44 | 6 |
| r/Parenting | 29349 | 109 | 143 | 23 | 6 | 6 |
| r/Postpartum_Depression | 2256 | 90 | 44 | 12 | 25 | 3 |
| r/PregnancyUK | 6941 | 50 | 64 | 24 | 12 | 0 |
| r/beyondthebump | 16469 | 346 | 345 | 89 | 43 | 2 |
| r/beyondthebumpUK | 6909 | 97 | 120 | 31 | 13 | 0 |
| r/daddit | 18390 | 107 | 111 | 36 | 12 | 3 |
| r/postpartumprogress | 2081 | 11 | 8 | 12 | 2 | 1 |
| r/pregnant | 61664 | 376 | 648 | 248 | 117 | 2 |
| r/sahm | 4231 | 58 | 43 | 8 | 7 | 1 |
| r/sleeptrain | 16084 | 778 | 1051 | 74 | 70 | 0 |
| r/workingmoms | 5712 | 50 | 55 | 10 | 1 | 0 |
