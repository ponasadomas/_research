# Reddit reading ledger: R38 (wave 2, sleep-baby)

Reader R38 · id prefix `sb38` · voice file `voice/reddit-r38.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w2.txt` + `../_shared/_tools/brief-reading.md` · 2026-10-25.

## Chunks assigned

From `_raw/reddit/read-w2/assignments.txt`, line R38: `read-w2-keep_core-116` … `read-w2-keep_core-124` (9 chunks, 134 units; posts dated 2026-08-13 → 2026-08-16, OP replies to 2026-08-27).

| chunk | units | units with quotes |
|---|---|---|
| read-w2-keep_core-116 | 15 | 13 |
| read-w2-keep_core-117 | 12 | 11 |
| read-w2-keep_core-118 | 15 | 13 |
| read-w2-keep_core-119 | 15 | 14 |
| read-w2-keep_core-120 | 13 | 12 |
| read-w2-keep_core-121 | 16 | 15 |
| read-w2-keep_core-122 | 16 | 14 |
| read-w2-keep_core-123 | 18 | 17 |
| read-w2-keep_core-124 | 14 | 12 |

## Counts

- Units in chunks: 134
- Units read in full: 134 (the post and every OP reply in each unit)
- Units with at least one quote: 121
- Units with no quote: 13 (listed below)
- Quotes written: 349 (`sb38-0001` → `sb38-0349`), ids unique; verify: `reddit-r38.jsonl: 349 quotes, 0 failed`
- Restricted quotes: 5 (listed in `synthesis/reader-notes-r38.md`)
- Unread: none

## Units with no quote (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/daddit-1vmy4no.txt` | child is 3.5 years, outside 0-36 month scope (two quotes drafted and removed before ids were final) |
| `../_shared/_raw/reddit-2026/units/toddlers-1vn7x9w.txt` | cross-post of daddit-1vmy4no; child 3.5 years |
| `../_shared/_raw/reddit-2026/units/Mommit-1vn4eq7.txt` | safe-sleep incident |
| `../_shared/_raw/reddit-2026/units/ScienceBasedParenting-1vngt2w.txt` | safe-sleep detail throughout (room temperature, sleepwear) |
| `../_shared/_raw/reddit-2026/units/NewParents-1vnhzzg.txt` | safe-sleep detail throughout (sleep position) |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1vnw6o0.txt` | cross-post of ScienceBasedParenting-1vn9yrr, no OP replies |
| `../_shared/_raw/reddit-2026/units/NewParents-1vo6kcz.txt` | safe-sleep incident |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vokmpd.txt` | safe-sleep detail and infant-death fear throughout |
| `../_shared/_raw/reddit-2026/units/Parenting-1vonei4.txt` | child is about 40 months, outside scope |
| `../_shared/_raw/reddit-2026/units/NewParents-1voxuja.txt` | infant-death fear and safe-sleep monitoring throughout |
| `../_shared/_raw/reddit-2026/units/NewParents-1vp04qs.txt` | safe-sleep detail throughout |
| `../_shared/_raw/reddit-2026/units/daddit-1vpe7fx.txt` | verbal harshness toward a child |
| `../_shared/_raw/reddit-2026/units/toddlers-1vpidkr.txt` | child is 3.5 years, outside scope |

## Units quoted only in part (passages left out, neutral reasons)

| unit | passages not quoted |
|---|---|
| `toddlers-1vnnl41` | mental-health crisis wording; medication |
| `sleeptrain-1vnzoq6` | bedsharing, sleep position, medical condition |
| `Mommit-1voj6ng` | partner's anger near the baby; held-sleep safety; medical |
| `NewParents-1vpngmc` | held-sleep safety; medication; mental health |
| `NewParents-1vpughs` | bedsharing; sleep position |
| `toddlers-1vpuypk` | parent's anger; mental health |
| `Mommit-1vmwu6g`, `sahm-1vnhvfd`, `sleeptrain-1vn41d4`, `NewParents-1vn7kat`, `NewParents-1vnf5co`, `toddlers-1vnvy57`, `beyondthebumpUK-1vp03w4`, `NewParents-1vpjgla` and others | shared-sleep, medication, medical-condition and mental-health sentences skipped; only clean sentences quoted |
| `NewParents-1vp75af` | cross-post of toddlers-1vozabs; only its one new OP reply quoted |

## How to continue

Nothing left in R38's assignment. Scratch files (unit list, exclusion list, batch inputs, helper) are in `scratchpad/R38/`. Never append to `voice/reddit-r38.jsonl` from another reader.
