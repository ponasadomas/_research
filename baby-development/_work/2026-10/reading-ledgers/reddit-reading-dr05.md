# Reddit full reads — DR05 (development, read-w3: keep_purchase-001, keep_success-001, keep_otherside-001–002, keep_core-001–005)

Reader DR05, 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md` via `../../_shared/_tools/prompt-development-reader-w3.txt`. Corpus: `_raw/reddit/read-w3/chunks.jsonl` (wave 3; posts dated 2026-04-01 → 2026-06-24, OP replies up to 2026-08-03). Voice file: `voice/reddit-dr05.jsonl` (ids dv05-0001 to dv05-0299). Builder and staged records: `scratchpad/DR05/` (`build.py` turns `q.jsonl` into the voice file; url, date, post_id and comment_id are read from the unit text; `units.tsv` lists the 142 units; `restricted.txt` the restricted ids).

## Counts

| step | n |
|---|---|
| chunks assigned | 9 |
| units in them | 142 |
| units read in full | 142 |
| units excluded (line not to cross) | 17 |
| duplicate crossposts (read; quoted from the other copy only) | 2 |
| units read, on topic or near it, no quote worth keeping | 4 |
| units quoted | 119 |
| quotes written | 299 |
| of which restricted (see reader notes) | 32 |
| of which flagged `possible_promo` (app builder) | 5 (dv05-0051 – dv05-0055) |

Verify: `python3 -I _tools/verify_quotes.py voice/reddit-dr05.jsonl` → `reddit-dr05.jsonl: 299 quotes, 0 failed`. Ids unique (299 of 299).

## Per chunk

| chunk | units | read in full | quoted | excluded, duplicate or no quote | quotes |
|---|---|---|---|---|---|
| read-w3-keep_purchase-001 | 26 | 26 | 24 | 2 | 50 |
| read-w3-keep_success-001 | 8 | 8 | 7 | 1 | 17 |
| read-w3-keep_otherside-001 | 10 | 10 | 8 | 2 | 25 |
| read-w3-keep_otherside-002 | 3 | 3 | 2 | 1 | 6 |
| read-w3-keep_core-001 | 14 | 14 | 11 | 3 | 37 |
| read-w3-keep_core-002 | 19 | 19 | 13 | 6 | 33 |
| read-w3-keep_core-003 | 20 | 20 | 16 | 4 | 47 |
| read-w3-keep_core-004 | 22 | 22 | 21 | 1 | 46 |
| read-w3-keep_core-005 | 20 | 20 | 17 | 3 | 38 |

## Excluded units (not quoted)

| unit | reason |
|---|---|
| `NewParents-1sanmle` | centred on a condition worry, therapy and a parent's medication; excluded |
| `NewParents-1sd0fl6` | centred on a condition worry; excluded |
| `NewParents-1segz90` | head injury and medication dose; excluded |
| `Parenting-1sfd733` | centred on a speech and walking delay concern; excluded |
| `NewParents-1sfz45v` | centred on a parent's postpartum mental-health diagnosis and medication; excluded |
| `FirstTimeMom-1sg8rkl` | safe-sleep incident (bed-sharing, baby found on stomach); excluded |
| `toddlers-1sjjm1v` | centred on a diagnosis evaluation; a therapy price in it is not quoted; excluded |
| `Mommit-1smixd1` | centred on a developmental evaluation result and an intervention programme; excluded |
| `beyondthebump-1spygnj` | centred on a head-shape condition and hospital history; excluded |
| `Mommit-1sqyv0e` | centred on a medical procedure and hearing concern; excluded |
| `beyondthebump-1szztjf` | infant head injury; excluded |
| `toddlers-1t7bn61` | centred on a speech delay and intervention programme; excluded |
| `toddlers-1t8guw9` | centred on a diagnosis-assessment question; excluded |
| `NewParents-1tb1qj4` | safe-sleep position and a medical condition; excluded |
| `beyondthebump-1t4mgmn` | partner's post centred on a mental-health condition, medication and a diagnosis fear; excluded |
| `daddit-1txrfxv` | centred on an early-intervention evaluation for speech therapy; excluded |
| `toddlers-1s9o7sr` | centred on an early-intervention evaluation result; excluded |

## Duplicates (read; quoted from the other copy)

| unit | quoted copy |
|---|---|
| `beyondthebump-1smj2rz` | `beyondthebumpUK-1smfmsx` (same text) |
| `NewParents-1u7qstu` | `beyondthebump-1u7qr77` (same text) |

## Read in full, no quote

| unit | why |
|---|---|
| `beyondthebump-1si5mcb` | clothing for a crawler; no development or play content |
| `NewParents-1tfs1wz` | general baby-hacks list; one toy-storage tip, nothing quotable |
| `NewParents-1spnju0` | rolling timeline curiosity; nothing beyond generic |
| `beyondthebump-1sur2km` | a single behaviour concern when sat down; nothing quotable |

## What has and hasn't been read

All 142 units in the nine assigned chunks were read in full, including every OP reply. Nothing assigned to DR05 is unread.
