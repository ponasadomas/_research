# Reddit reading ledger — R60 (wave 3, sleep-baby)

Reader R60 · id prefix `sb60` · voice file `voice/reddit-r60.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` · scratch `scratchpad/R60/` (unit list `units.tsv`, batch files `b01.json`–`b14.json`, `add.py`, `show.sh`, `excluded.tsv`, `restricted.txt`, `index.txt`).

## Chunks assigned

`read-w3-keep_core-144` … `read-w3-keep_core-153` (10 chunks, line `R60` of `_raw/reddit/read-w3/assignments.txt`; 160 units). Posts dated 2026-06-04 → 2026-06-09; original-poster replies up to 2026-10-13.

| chunk | units | read in full | units quoted | quotes |
|---|---|---|---|---|
| read-w3-keep_core-144 | 16 | 16 | 15 | 64 |
| read-w3-keep_core-145 | 18 | 18 | 16 | 59 |
| read-w3-keep_core-146 | 16 | 16 | 15 | 47 |
| read-w3-keep_core-147 | 12 | 12 | 11 | 50 |
| read-w3-keep_core-148 | 19 | 19 | 19 | 64 |
| read-w3-keep_core-149 | 17 | 17 | 16 | 50 |
| read-w3-keep_core-150 | 16 | 16 | 15 | 49 |
| read-w3-keep_core-151 | 16 | 16 | 14 | 53 |
| read-w3-keep_core-152 | 11 | 11 | 9 | 35 |
| read-w3-keep_core-153 | 19 | 19 | 18 | 57 |
| **total** | **160** | **160** | **148** | **528** |

All 160 units read in full. Quotes written: 528 (ids sb60-0001 … sb60-0528, unique, counted from disk). Verify: `python3 -I _tools/verify_quotes.py voice/reddit-r60.jsonl` → 528 quotes, 0 failed. Restricted: 7 quote ids (listed in `synthesis/reader-notes-r60.md`).

Unit numbers below are the line numbers of `scratchpad/R60/units.tsv` (chunk order).

## Units with nothing quoted (12)

| # | unit | chunk | reason |
|---|---|---|---|
| 12 | `AttachmentParenting-1tx1uy2` | 144 | safe-sleep detail throughout (bedsharing set-up, mattress) |
| 20 | `NewParents-1txb2ky` | 145 | safe-sleep detail throughout (prone sleeping after rolling) |
| 32 | `NewParents-1txmbkb` | 146 | safe-sleep detail throughout (baby caught in cot slats, liners, bumpers) |
| 39 | `sleeptrain-1txt6wu` | 146 | cross-post of unit 38, same author and text; quoted once from 38 |
| 57 | `Mommit-1tykbr2` | 147 | sleep only as background; the sleep passage is a bedsharing detail |
| 86 | `NewParents-1tzmk58` | 149 | cross-post of unit 85; replies are medical and safe-sleep detail |
| 106 | `Mommit-1u07a8k` | 150 | sleep in passing only (infant fussiness; parents' neurodivergence) |
| 116 | `beyondthebump-1u0hfnf` | 151 | parent's stated urge toward physical harm (excluded in full) |
| 118 | `sleeptrain-1u0j0d2` | 151 | infant breathing scare during crying; parent panic wording (excluded in full) |
| 135 | `toddlers-1u0ridu` | 152 | safe-sleep detail (loose blanket, items round the neck); sibling diagnosis |
| 138 | `NewParents-1u106v0` | 152 | safe-sleep detail throughout (prone sleeping after rolling) |
| 145 | `Parenting-1u15dna` | 152 | safe-sleep detail throughout (sleepwear layers, swaddle, loose blanket) |

## Units quoted only in part (passages left out, neutral reason)

| # | unit | left out |
|---|---|---|
| 10 | `daddit-1tx11k4` | parent mental-health and medication wording; the child's tests and supplements |
| 27 | `NewParents-1txfdav` | road-safety incident; parent mental-health and medication wording |
| 83 | `NewParents-1tzckcn` | parent mental-health wording |
| 85 | `beyondthebumpUK-1tzmi6q` | medical, medication and safe-sleep detail (swaddling, rolling, dozing while feeding) |
| 128 | `sleeptrain-1u0mkcp` | drowsy-driving fear; bed-attached sleeper detail |
| 129 | `sleeptrain-1u0mq7t` | bedsharing and floor-mattress detail |
| 131 | `toddlers-1u0pv2o` | bedsharing, supplement and diagnosis passages |
| 136 | `NewParents-1u0vhjy` | medication and bedsharing (two lines kept, both restricted: sb60-0452, sb60-0457) |
| 140 | `toddlers-1u10z9r` | medication, diagnosis and bedsharing |
| 144 | `Mommit-1u15426` | bedsharing, medication, mental-health wording |
| 155 | `sleeptrain-1u1diok` | bedsharing, medical |
| 158 | `sleeptrain-1u1gony` | bedsharing; infant breathing wording |

Other bedsharing, medication and illness lines in quoted units (3, 9, 22, 41, 42, 51, 52, 59, 68, 69, 72, 78, 79, 81, 82, 87, 89, 92, 94, 99, 100, 103, 104, 110, 111, 113, 115, 120, 124, 125, 126, 130, 133, 146, 151, 154, 157) were not quoted.

## Cross-posts

Units 60 and 65 (same post, two subs): post quoted from 60, original-poster replies from 65. Units 88 and 90: post quoted from 88, one reply from 90. Units 38/39 and 85/86 as above. Units 41 (`toddlers-1txwpmu`) and 115 (`sleeptrain-1u0fupq`) are the same family's story (3-year-old, newborn brother, grandma visiting) posted three days apart in two subs in different words; both quoted, overlap to be noted at merge. Unit 50 reads like AI-written text (one quote, marked in context).

## How to continue

Nothing is unread. Do not re-run this reader: `voice/reddit-r60.jsonl` is append-only; `scratchpad/R60/add.py` appends with the next id.
