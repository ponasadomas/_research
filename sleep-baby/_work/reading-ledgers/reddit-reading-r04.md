# Reddit full reads: reader R04 (keep_core 007–014)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder). Unit list used: `scratchpad/R04/units.txt`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_core-007` … `-014`) |
| units in those chunks | 128 |
| units read in full (post + every OP reply archived in the unit) | 128 |
| units excluded | 0 |
| units read, no quote taken | 7 (below) |
| units quoted | 121 |
| quotes written | 314 (`voice/reddit-r04.jsonl`, ids `sb04-0001` … `sb04-0314`) |
| verify | `verify_quotes.py voice/reddit-r04.jsonl` → 314 quotes, 0 failed |

Units per chunk: 007 = 17, 008 = 11, 009 = 14, 010 = 14, 011 = 20, 012 = 16, 013 = 19, 014 = 17.

Note: sb04-0313 and sb04-0314 (`NewParents-1w1uger`) were added last, so their ids are out of chunk order.

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vzop43.txt` | expecting twins, planning which cots to buy; restates safe-sleep guidance, no sleep problem yet |
| `../_shared/_raw/reddit-2026/units/toddlers-1w0l06k.txt` | cross-post, same text as `Mommit-1w0krcd` (quoted there) |
| `../_shared/_raw/reddit-2026/units/Mommit-1w1evcx.txt` | cross-post, same text as `Parenting-1w1exiz` (quoted there) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1w1uerz.txt` | the question is whether a baby who rolled onto her front during Ferber is safe; safe-sleep content, not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1w24zvw.txt` | red-eye flight with a 9-month-old; two lines, nothing beyond travel nerves |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1w2ha2k.txt` | same author and same 20-week-old as `sleeptrain-1vzw8f7` / `-1w0ojp9` (quoted there); post says "20 month" but means 20 weeks |
| `../_shared/_raw/reddit-2026/units/NewParents-1w2khj3.txt` | cross-post, same text as `sleeptrain-1w2ha2k` |

Cross-posts where only unique lines were quoted: `toddlers-1w1eye6` (the OP's update comment, sb04-0223), `NewParents-1w1fe50` (sb04-0228, -0229), `NewParents-1w1rumk` (sb04-0249).

## Passages read but deliberately not quoted (lines not to cross)

Units stay in; only these passages were skipped.

- `beyondthebumpUK-1w1q9kt`: the newborn sleeps in a sleep pod or on a nursing pillow, on her side. Not quoted. Only the mother's fear lines were taken (sb04-0245, -0246).
- `NewParents-1w1rzq3`: co-sleeping "as safely as possible" on a floor mattress, and torticollis / helmet detail. Not quoted.
- `sleeptrain-1w0sxy2`: the parent's own account of falling asleep with the baby is quoted as a trigger scene (sb04-0171). Her plans to move the cot (bathroom, SlumberPod) and the AAP mention are not quoted.
- Medical detail (reflux meds, GI specialist, iron/ferritin, sleep study, g-tube/NICU, breath holding, ear tubes, ADHD/ASD) shows up only in context lines where it is needed, never as a cause. `NewParents-1w1dtan` comment `p6kvblr` (breath holding) was not quoted.

## How to continue

Nothing assigned is left unread. Do not append to `voice/reddit-r04.jsonl` from another agent; start a new file with a new prefix.
