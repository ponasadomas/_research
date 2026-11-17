# Reddit reading ledger — R23 (prefix sb23), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, posts 2026-06-25 → 2026-08-24). Voice file: `voice/reddit-r23.jsonl`. Scratch (unit list `units.txt`, reading batches `batch01-08.txt`, per-batch record specs `q01-08.jsonl`, exclusion log `excluded.txt`, restricted list `restricted.txt`, id map `idmap.txt`): `scratchpad/R23/`. The builder that turns the specs into the voice file sits outside the repo (session scratchpad); the voice file is the record.

## Counts

| step | count |
|---|---|
| chunks assigned | 11: `read-w2-keep_purchase-008`, `-009`, `read-w2-keep_success-001` … `-007`, `read-w2-keep_otherside-001`, `-002` |
| units in those chunks | 133 (purchase 23 + 6; success 15/7/10/12/13/12/4; other side 10 + 21) |
| units read in full (post + every OP reply in the unit) | 133 |
| units excluded entirely | 1 |
| units read, not quoted (cross-posts / duplicates) | 4 |
| units with passages left out (rest quoted) | 32 (listed below) |
| units quoted | 128 |
| quotes written | 353 (sb23-0001 … sb23-0353), `verify_quotes.py` 0 failed, ids unique |
| restricted quotes | 13 (listed in `synthesis/reader-notes-r23.md`) |

Counts are of quotes chosen, never of people. Posts span 2026-06-25 to 2026-08-24; OP replies run to 2026-09-23 (one success thread has a reply dated 2026-10-20, not quoted).

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `NewParents-1ukhgat` | otherside-001 | safe-sleep incident (a caregiver repeatedly falling asleep holding the infant) |

## Read in full, not quoted

| unit | chunk | reason |
|---|---|---|
| `sleeptrain-1up6oeh` | otherside-002 | same text as `toddlers-1up6mga`; quoted from that copy (sb23-0040) |
| `toddlers-1v4j049` | otherside-002 | cross-post of `sleeptrain-1v3chjv`; quoted from that copy |
| `NewParents-1vu42zg` | purchase-008 | same text as `Mommit-1vu422h`; quoted from that copy (sb23-0107) |
| `sleeptrain-1vxic9z` | success-007 | same post as wave-1 unit `NewParents-1vxk4e7`, already quoted as sb02-0001/0002; not re-quoted |

`workingmoms-1v3p0ye` is a cross-post of `NewParents-1v3ozdx`; only its own OP reply was quoted (sb23-0067).

## Units with passages left out (rest quoted)

| unit | what was not quoted (neutral reason) |
|---|---|
| `NewParents-1uikj0g` | parent's medication/therapy reply (mental-health, medication) |
| `NewParents-1ugqdcr` | replies with claims that crying harms babies (README line) |
| `NewParents-1vw7uqh` | night passage of harsh words to the child (verbal harshness) |
| `sleeptrain-1uk7vtn` | crisis wording; therapist / emergency-session lines |
| `sleeptrain-1vwa77w` | bed-sharing nursing detail; rage line |
| `sleeptrain-1uke8ac` | bed-sharing arrangement passage |
| `sleeptrain-1ulxjdq` | medication replies (SSRI) |
| `sleeptrain-1uqdyh2` | sleepwear/rolling and pacifier-in-crib replies (safe-sleep) |
| `daddit-1ul1bwe` | psychological-help mention |
| `NewParents-1usv0lv` | bed-sharing detail; pasted ChatGPT safe-sleep paragraph |
| `sleeptrain-1utfyhl` | eczema (medical); cosleeping lines |
| `sleeptrain-1uxzgsu` | room-sharing guidance line (safe-sleep) |
| `sleeptrain-1v06qu9` | cosleeping safe-sleep detail |
| `sleeptrain-1v3w4i7` | bed-sharing feeding detail; vaccination line |
| `sleeptrain-1v7pn5m` | bed-sharing passage |
| `sleeptrain-1v0b7dk`, `sleeptrain-1v4ngky` | mental-health wording lines |
| `beyondthebump-1vag2u0` | reflux, medication and fertility-treatment lines |
| `toddlers-1ve33m9` | line on holding the child tight so he cannot move (physical restraint) |
| `sleeptrain-1veizmd` | bed-sharing and sleep-position details |
| `sleeptrain-1vfv351` | cosleeping detail |
| `sleeptrain-1vh15er` | rolling-to-front detail (safe-sleep) |
| `sleeptrain-1vl2uoe` | cosleeping lines; "losing my mind" |
| `sleeptrain-1vmyet5` | cosleeping detail |
| `beyondthebump-1vp2oee` | mental-health symptoms and sleep-medication lines |
| `AttachmentParenting-1vtlfaj` | medical test and iron-supplement content (one doctor line quoted, sb23-0340) |
| `sleeptrain-1vvl10e` | bed-sharing / stomach-sleeping details; depression wording |
| `NewParents-1vvq4at` | soft toy in the crib, rolling and vomiting details |
| `sleeptrain-1vwzfj7` | bed-sharing line |
| `Parenting-1ukwmkp` | SIDS and PTSD lines in replies |
| `FirstTimeMom-1vmoeb8` | infant hospital/ICU history |
| `sleeptrain-1v3chjv` | medication for teething |

## What has and hasn't been read

All 133 units in the 11 chunks were read in full. Nothing in R23's assignment is unread.

## How to continue

Nothing to continue for R23. Do not re-run R23 against `voice/reddit-r23.jsonl` (append-only, ids cited). For a cross-reader check: `sleeptrain-1vxic9z` duplicates the wave-1 unit `NewParents-1vxk4e7`.
