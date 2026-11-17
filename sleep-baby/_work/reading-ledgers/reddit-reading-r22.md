# Reddit reading ledger — R22 (prefix sb22), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, posts 2026-06-25 → 2026-08-24). Voice file: `voice/reddit-r22.jsonl`. Scratch (unit list `units.txt`, exclusion log `log.md`, per-chunk spec files `c1.py`…`c7.py`, `add.py` builder, `restricted.tsv`): `scratchpad/R22/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 7 (`read-w2-keep_purchase-001` … `-007`) |
| units in those chunks | 132 (20/18/18/16/21/21/18) |
| units read in full (post + every OP reply) | 132 |
| units excluded entirely | 9 |
| units read, nothing worth quoting | 2 (one is a cross-post quoted from its other copy) |
| units quoted | 121 |
| quotes written | 367 (sb22-0001 … sb22-0367), `verify_quotes.py` 0 failed |
| restricted quotes | 19 (listed in `synthesis/reader-notes-r22.md`) |

Counts are of quotes chosen, never of people. Posts span 2026-06-25 to 2026-08-12; OP replies run to 2026-09-23.

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `NewParents-1ugegyp` | 001 | infant medical-emergency fear around a breathing monitor |
| `Mommit-1ukxb51` | 002 | safe-sleep incident with a hired night carer (a night-nanny refund is in it; not quoted) |
| `daddit-1un930m` | 002 | travel-cot safety incident |
| `toddlers-1ut838u` | 003 | child 3.5 years (over the niche age); medication |
| `sleeptrain-1v41coy` | 005 | smart-bassinet swaddle and rolling safe-sleep details |
| `Mommit-1v5xo8r` | 005 | infant-death fear, breathing monitor, medical history |
| `sleeptrain-1vizehy` | 007 | infant-death intrusive fears |
| `beyondthebump-1vj3g72` | 007 | infant-death fears, breathing monitor |
| `NewParents-1vl3uxi` | 007 | weighted-sleepwear safety controversy |

## Read in full, not quoted

| unit | chunk | reason |
|---|---|---|
| `toddlers-1uf16v2` | 001 | bed shopping for a nearly-3-year-old, no sleep problem |
| `sleeptrain-1ufvke4` | 001 | cross-post of `daddit-1ufvmjk` (also `Mommit-1ufvojy`); quoted from those copies |

Also near-duplicates, both quoted: `sleeptrain-1uk49i5` / `sleeptrain-1ukc550` (same story a day apart), and `sleeptrain-1ut93q3` / `sleeptrain-1vd6fvb` (likely the same author three weeks apart; read as one arc, but speakers labelled per unit: `new_mother` in 1ut93q3, `parent_unspecified` in 1vd6fvb).

Within quoted units, lines about bedsharing, rolling, breathing monitors, medication and child-safety incidents were left out and the rest quoted.

Stage `regression_4_months` is used for babies about 16–22 weeks, matching earlier readers (56 quotes).

## What has and hasn't been read

Every unit in the seven chunks was read in full. Nothing unread. `read-w2-keep_purchase-008` and `-009` are not part of this assignment.

## How to continue

Nothing left in this assignment. Never append to `voice/reddit-r22.jsonl` from another agent; new reads take a new prefix.
