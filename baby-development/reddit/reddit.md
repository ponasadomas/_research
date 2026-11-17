# Reddit — development

Harvest: Arctic Shift API, 2026-04-01 → 2026-10-25, saved untouched in `../../_shared/_raw/reddit-2026/<sub>.posts.jsonl` (log: `harvest.log`). Historical filter: `../../_shared/_tools/niche_filter.py development` → `../_raw/reddit/filter-v1/` (frozen). Rule: A = topic + explicit purchase/paid-tool/brand signal or 2+ distinct pain words; B = topic + one pain word, a help question or a generic tool word (plan, method, guide, book, app, class, schedule, routine); C = topic only; safety = safety regex hit (inspected, not auto-dropped); non-core subs also need the niche's person regex.

## Historical filter-v1 and wave-1 ledger

| step | count |
|---|---:|
| posts scanned in this niche's subreddits | 156551 |
| matched the niche (A+B+C+safety+unavailable) | 24326 |
| tier A | 6801 |
| tier B (on disk, unread) | 11096 |
| tier C (on disk, unread) | 4919 |
| historical safety lane (all 938 now read in UR assignments) | 938 |
| body removed or deleted | 572 |
| **wave 1 cards: tier A dated 2026-08-25 → 10-25** | 1962 |
| tier A outside wave 1 (unread, ids in `filter-v1/wave1/unread-rest.jsonl`) | 4839 |
| triaged (wave 1, orchestrator-verified TSVs incl. corrections) | 1,962 |
| kept | 288 |
| read in full (units = post + the original poster's replies) | 288 |
| units with at least one quote · quotes | 244 · 603 |

**Historical cut rule (2026-10-25):** tier A outside the last two months is listed as unread, by id, not dropped. Reason: about 46,000 tier-A posts across the five niches would need about 70 triage agents before reading, and the owner's monthly usage limit was hit once on 2026-10-25. The later waves and current unread inventory are reconciled below; these dated figures are not current unread totals.

## By subreddit (filter-v1)

| sub | scanned | A | B | C | safety | unavailable |
|---|---:|---:|---:|---:|---:|---:|
| r/FirstTimeMom | 4111 | 83 | 158 | 74 | 11 | 28 |
| r/Mommit | 19451 | 953 | 1146 | 493 | 206 | 23 |
| r/Montessori | 814 | 174 | 222 | 124 | 10 | 79 |
| r/NewParents | 27258 | 1279 | 2516 | 1192 | 126 | 76 |
| r/Parenting | 29349 | 941 | 1625 | 590 | 138 | 145 |
| r/ScienceBasedParenting | 3124 | 96 | 295 | 267 | 25 | 13 |
| r/beyondthebump | 16469 | 722 | 1105 | 523 | 110 | 31 |
| r/beyondthebumpUK | 6909 | 301 | 459 | 241 | 38 | 13 |
| r/daddit | 18390 | 526 | 809 | 425 | 87 | 23 |
| r/sahm | 4231 | 231 | 247 | 76 | 20 | 10 |
| r/toddlers | 20733 | 1264 | 2277 | 856 | 146 | 130 |
| r/workingmoms | 5712 | 231 | 237 | 58 | 21 | 1 |


## Completed re-reading and current ledger — 2026-11-16

UR01–UR05 read all 1,169 assigned previously excluded post ids, offline. Their immutable ledgers are `reddit-reading-ur01.md` through `reddit-reading-ur05.md`; the assignment TSVs are under `../scratchpad/unfilter-reread/`. All 1,182 resulting quotes (`dv21-` through `dv25-`) were read in full for the revised findings. Evidence totals count selected quotes; coverage totals below count posts or rows, never people. Crossposts and repeated extractions are not independent corroboration.

| reader | assigned/read rows | quoted rows | no-quote rows | quotes |
|---|---:|---:|---:|---:|
| UR01 | 113 / 113 | 112 | 1 | 247 |
| UR02 | 113 / 113 | 97 | 16 | 184 |
| UR03 | 315 / 315 | 184 | 131 | 241 |
| UR04 | 314 / 314 | 173 | 141 | 248 |
| UR05 | 314 / 314 | 161 | 153 | 262 |
| total | 1169 / 1169 | 727 | 442 | 1182 |

Rows not found or unfinished: **0**. Unit-file reads: **127**, including every archived original-poster reply in those units. Archive-only reads: **1,042**, complete available title/body records with no claim to missing replies. UR03 notes one saved post ending mid-sentence; the absent continuation has not been invented or obtained. The UR05 fiction record and UR03 possible promotion remain labelled, and some quoted accounts are retrospective or have unknown ages.

The original waves supplied **1,624 Reddit quotes**; adding **1,182 UR quotes** yields **2,806 Reddit quotes**. With **164 public reviews**, the build now has **2,970 quotes in twelve voice files**. Findings cite **1,086 distinct ids**, including **240 UR ids**, preserving all **846 previously cited ids**. This is a citation count, including provenance-only references, not a count of independent experiences.

### Coverage by post id

The original reading manifests (`read-v1`, `read-w2`, `read-w3`) assigned **723** distinct post ids. The UR assignments contain **1,169** distinct post ids, **107** overlapping the original manifests: union **1,785** assigned posts recorded as read. Current quotes refer to **1,314** distinct Reddit post ids; **471** read ids have no selected quote. Of the **727** UR quote-bearing post ids, **23** already supplied earlier quotes. These relationships are why quote totals cannot be interpreted as people or additional independent evidence.

`audit_niche.py` correctly rebuilds the derived corpus, but its coverage counter is keyed by `raw_file`: many archived posts share one JSONL file. Its **757 quoted paths** comprise **725 Reddit paths and 32 review paths**; they are not 757 posts. For the original manifests only, **694** assigned paths now supply quotes and **29** do not; every no-quote path is named in a reader ledger. The TSV/post-id reconciliation above supplies the UR coverage the audit does not ingest.

### What remains unread

Computed offline by subtracting the union of original and UR assigned post ids from frozen candidate-id lists; no candidate files were rewritten. Historical tiers describe the frozen intake, not present research exclusions.

| frozen queue | ids on disk | assigned ids now read | ids without a full read |
|---|---:|---:|---:|
| filter-v1 safety | 938 | 938 | 0 |
| filter-v2 safety | 349 | 349 | 0 |
| filter-v2 A | 2475 | 746 | 1729 |
| filter-v2 B | 4220 | 0 | 4220 |
| filter-v2 C | 2019 | 0 | 2019 |
| filter-v1 outside-wave-1 A list | 4839 | 537 | 4302 |
| of that list, ids not selected by filter-v2 A | 3106 | 0 | 3106 |
| filter-v1 B | 11096 | 0 | 11096 |
| filter-v1 C | 4919 | 0 | 4919 |

All filter-v2 A ids were already triaged across the three original waves. Its remaining **1,729** are triage drops without a full-read assignment, not an untriaged backlog. The two safety queues overlap in **344** ids: all **943** distinct ids in their union are covered. The other queues also overlap across filter versions; **do not add these rows**. The old 15% wave-1 keep rate cannot estimate the relevance of the unread queues after subject-based exclusions.

### Earlier extraction gaps outside these assignments

The UR assignments cover **107 of the 108 named units** in the initial unfilter report. The exception is `toddlers-1tjvzoj`: DR06 says it was read in full, with nothing quoted because delay worry was already covered. It was not assigned to UR01–UR05, so its extraction omission is not recovered. Three separately noted DR05 omissions—prices in `beyondthebump-1tnt8fi` and `NewParents-1t8dis1`, and the first-word bet in `beyondthebump-1sdj400`—are also outside the UR assignments and remain unextracted. No subject-based reason was established for those three. These are extraction gaps, not four unread UR posts.

The merged file and counts were regenerated with the existing audit tool; original voice and reader-ledger files remain unchanged. Findings distinguish diagnoses, treatments, alleged harm, outcomes, fiction, promotions and ordinary parent testimony by their recorded provenance.
