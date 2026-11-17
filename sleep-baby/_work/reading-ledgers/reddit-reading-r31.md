# Reddit reading ledger — R31 (prefix sb31), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md` and `../_shared/_tools/prompt-sleep-baby-reader-w2.txt`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, posts 2026-06-25 → 2026-08-24). Voice file: `voice/reddit-r31.jsonl`. Scratch (unit list `units.tsv`, per-chunk spec files `c054.py`…`c062.py`, builder `add.py`, exclusion log `log.md`, `restricted.tsv`, chunk dumps `chunk055.txt`…`chunk062.txt`): `scratchpad/R31/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 9 (`read-w2-keep_core-054` … `-062`) |
| units in those chunks | 132 (17/11/17/20/15/4/16/17/15) |
| units read in full (post + every OP reply) | 132 |
| units excluded entirely | 8 |
| units read, nothing quoted | 1 (cross-post quoted from its other copy) |
| units quoted | 123 |
| quotes written | 416 (sb31-0001 … sb31-0416), 103 from OP replies; `verify_quotes.py` 0 failed |
| restricted quotes | 29 (listed in `synthesis/reader-notes-r31.md`) |

Counts are of quotes chosen, never of people. Posts span 2026-07-18 to 2026-07-21; OP replies run to 2026-10-05.

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `FirstTimeMom-1v06glv` | 054 | safe-sleep detail (prone and chest sleeping), infant-death fear, medication |
| `daddit-1v0g1v5` | 055 | child 3.25 years (over the niche age) |
| `AttachmentParenting-1v0rtes` | 056 | bedsharing on an adult bed, floor-bed safety details |
| `AttachmentParenting-1v1gsoh` | 057 | child over 3 years (over the niche age) |
| `sleeptrain-1v2d9n6` | 061 | child 3.5 years (over the niche age); parents yelling at the child |
| `Mommit-1v2goih` | 061 | medical condition and medication |
| `AttachmentParenting-1v2jni1` | 061 | bedsharing with an infant, sleeping-position details |
| `toddlers-1v2rwcq` | 062 | cross-post of `sleeptrain-1v2d9n6` (same reasons) |

Read, no quote: `NewParents-1v1863l` (cross-post of `ScienceBasedParenting-1v17za1`, quoted there).

## Lines left out of quoted units (neutral reasons)

Medication, illness, vaccine and test details (e.g. `sleeptrain-1v0k3rd`, `sleeptrain-1v1kjee`, `NewParents-1v2siry`, `beyondthebumpUK-1v2iod0`); prone sleeping, smart-bassinet, swaddle-rolling and bedsharing lines (e.g. `sleeptrain-1v17qal`, `NewParents-1v1sftp`, `sleeptrain-1v24vwe`); lines about speaking sharply to, snapping at, yelling at or physically holding a child's eyes closed (`sahm-1v1eect`, `toddlers-1v1igxt`, `Parenting-1v1uofa`, `toddlers-1v1ulph`, `NewParents-1v2ctx1`); intrusive-thoughts and anxiety disclosures (`beyondthebump-1v2lbhm`); a joke about drowsy driving (`NewParents-1v0ujy8`). Full list in `scratchpad/R31/log.md`.

## Speaker fixes in my own file

`Parenting-1v2jo8n` quotes relabelled `experienced_mother` (same author's cross-post `sleeptrain-1v2p3yz` is titled "Exhausted mom of 3"); `Mommit-1v16m1i` quotes relabelled `new_mother` (same author's follow-up `Mommit-1v22n51` self-identifies as mom); `Parenting-1v0dqhh` ("momma") and `sleeptrain-1v17qal` (nursing) relabelled `new_mother`.

## What has and hasn't been read

All 132 units in chunks 054–062 read in full, including every archived OP reply. Nothing unfinished.
