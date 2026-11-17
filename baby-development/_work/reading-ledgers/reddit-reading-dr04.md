# Reddit full reads — DR04 (development, read-w2 keep_core 006–013)

Reader DR04, 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, tighter filter; posts dated 2026-07-22 → 2026-10-10). Voice file: `voice/reddit-dr04.jsonl` (ids dv04-0001 to dv04-0235). Builder and staged records: `scratchpad/DR04/` (`build.py` turns `staged.jsonl` into the voice file; url, date, post_id and comment_id come from the unit text; `excluded.tsv`, `restricted.txt`, `units.txt`).

## Counts

| step | n |
|---|---|
| chunks assigned | 8 (read-w2-keep_core-006 … 013) |
| units in them | 91 |
| units read in full | 91 |
| units excluded (line not to cross) | 6 |
| duplicate crossposts (read; quoted from the other copy only) | 1 |
| units read, kept, no quote | 0 |
| units quoted | 84 |
| quotes written | 235 |
| of which restricted (see reader notes) | 26 |

Verify: `python3 -I _tools/verify_quotes.py voice/reddit-dr04.jsonl` → `reddit-dr04.jsonl: 235 quotes, 0 failed`. Ids unique (235 of 235).

## Per chunk

| chunk | units | read in full | excluded or duplicate | quotes |
|---|---|---|---|---|
| read-w2-keep_core-006 | 18 | 18 | 2 | 42 |
| read-w2-keep_core-007 | 15 | 15 | 1 | 39 |
| read-w2-keep_core-008 | 9 | 9 | 0 | 25 |
| read-w2-keep_core-009 | 3 | 3 | 0 | 9 |
| read-w2-keep_core-010 | 4 | 4 | 1 | 11 |
| read-w2-keep_core-011 | 21 | 21 | 1 | 55 |
| read-w2-keep_core-012 | 20 | 20 | 2 | 51 |
| read-w2-keep_core-013 | 1 | 1 | 0 | 3 |

## Excluded units (not quoted)

| unit | reason |
|---|---|
| `toddlers-1v3hna0` | centred on a diagnosis and screening referral (medical detail); excluded |
| `beyondthebump-1v6cynu` | centred on a parent's mental-health crisis and a delay concern; excluded |
| `NewParents-1vjubgz` | centred on infant sleep position and rolling in sleep (safe-sleep topic); excluded |
| `beyondthebump-1vmvm9v` | centred on a medical history and delay concern with a parent's mental-health crisis; excluded |
| `NewParents-1vuqkpa` | centred on a check-up finding, referral and medical monitoring; excluded |
| `NewParents-1vxebr6` | centred on a suspected condition, physio and osteopath treatment; excluded |
| `Mommit-1vd0poy` | duplicate crosspost of `NewParents-1vd0nwm` (same text); read in full, quoted once from the other copy |

## Units quoted but with passages left out

Read in full and quoted only from passages that do not touch a line: `toddlers-1v3z3vy` (last reply lists condition signs and a parent's own medical history: not quoted), `NewParents-1vg7gos` (a relative's condition: not quoted), `NewParents-1vh9o73` (medication line not quoted), `beyondthebump-1vjb8zp` (long speculation about a condition: not quoted), `beyondthebumpUK-1vjrxym` (a reflux line not quoted), `FirstTimeMom-1vjw0hd` (medication and therapy replies not quoted), `toddlers-1vmww9u` (feeding-therapy line not quoted), `NewParents-1vnhzrd` (medication line not quoted), `Mommit-1vrtn1b` (pregnancy, birth and medication history not quoted), `FirstTimeMom-1vsqnlu` (reflux and sleep-device lines not quoted; trimmed with ` […] `), `FirstTimeMom-1vss9qh` (head-injury line not quoted), `beyondthebump-1vtkr8u` (medication reply not quoted), `NewParents-1wvxkjn` (a relative's illness guess not quoted).

## What has and hasn't been read

All 91 units in DR04's eight chunks were read in full, including every original-poster reply archived in each unit. Nothing in the assignment is unread.
