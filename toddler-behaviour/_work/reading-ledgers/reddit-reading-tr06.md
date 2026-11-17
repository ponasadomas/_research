# Reddit full reads — reader TR06 (2026-10-25)

Brief: `../../_shared/_tools/brief-reading.md`. Voice file: `../voice/reddit-tr06.jsonl` (ids `tb06-0001` … `tb06-0284`). Notes: `../synthesis/reader-notes-tr06.md`. Scratch: `../scratchpad/TR06/` (unit list, batch files, per-batch quote drafts, build script).

## Counts

| step | n |
|---|---|
| chunks assigned | 8 (`read-v1-keep_core-031` … `read-v1-keep_core-038` in `../_raw/reddit/read-v1/chunks.jsonl`) |
| units in those chunks | 124 |
| units read in full (post + every OP reply in the unit) | 124 |
| units excluded (not quoted) | 10 |
| units read, kept, no quote taken | 5 (3 crossposts quoted from their twin, 2 thin) |
| units quoted | 109 |
| quotes written | 284 |
| quotes restricted (research only) | 46 ids from 18 units (see notes, "Restricted ids") |
| verify | `reddit-tr06.jsonl: 284 quotes, 0 failed` |

Nothing assigned is left unread.

## Units excluded (never quoted)

| # | unit | reason |
|---|---|---|
| 17 | `../_shared/_raw/reddit-2026/units/Mommit-1wmjy6e.txt` | physical force toward child (also an orchestrator safety drop) |
| 57 | `../_shared/_raw/reddit-2026/units/toddlers-1wo4549.txt` | medical treatment |
| 58 | `../_shared/_raw/reddit-2026/units/Mommit-1wo47jn.txt` | medical treatment (crosspost of #57) |
| 69 | `../_shared/_raw/reddit-2026/units/pottytraining-1wohb94.txt` | medical treatment; child privacy |
| 72 | `../_shared/_raw/reddit-2026/units/GentleParenting-1woktb4.txt` | verbal harshness; physical force toward child |
| 79 | `../_shared/_raw/reddit-2026/units/toddlers-1wp3bpb.txt` | verbal harshness |
| 86 | `../_shared/_raw/reddit-2026/units/pottytraining-1wpkwcp.txt` | diagnosis-centred; medical treatment; physical force toward child |
| 88 | `../_shared/_raw/reddit-2026/units/Parenting-1wpsf6f.txt` | physical force toward child |
| 113 | `../_shared/_raw/reddit-2026/units/AttachmentParenting-1wrbzv7.txt` | physical force toward child |
| 121 | `../_shared/_raw/reddit-2026/units/pottytraining-1wrrht0.txt` | verbal harshness |

## Read, no quote

| # | unit | why |
|---|---|---|
| 31 | `Mommit-1wmzpxp` | crosspost of #32 (`Parenting-1wmzt2g`), quoted there; OP reply names a diagnosis |
| 36 | `toddlers-1wn77j1` | child hitting himself when upset; thin, sensitive |
| 41 | `NewParents-1wnghqd` | crosspost of #45 (`toddlers-1wnjyse`), quoted there |
| 54 | `Mommit-1wntokd` | light bath-time anecdote |
| 111 | `Parenting-1wr0fuv` | crosspost of #110 (`toddlers-1wqywi7`), quoted there |

## Passages left out of quoted units

- `toddlers-1wo1ft8`: the sentence about a grandparent recommending physical discipline (physical force).
- `Mommit-1wpt1c7`: the parent's line about an urge to get physical, and a health condition.
- `Parenting-1wrkvtj`: the passage on a peer physically bullying the child.
- `toddlers-1woogpe`: the parent's thought about physical discipline.
- `Parenting-1wn9vm1`: the line about undressing the child.
- Medical treatment lines (laxatives, softeners, supplements, tests) everywhere.

## Judgement calls

- `toddlers-1wmo5rd` (#21): the author says they are 18, so they are an adult and was kept and quoted (tb06-0058 to tb06-0060).
- Crossposts: each one was quoted once, from the copy with more OP replies.

## How to continue

Nothing to continue for these chunks. If the file has to be rebuilt, `python3 -I ../scratchpad/TR06/build.py` regenerates `voice/reddit-tr06.jsonl` from `scratchpad/TR06/q/*.json` in the same id order. Never append another reader's records to it.
