# Reddit reading ledger — R32 (prefix sb32), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md` and `../_shared/_tools/prompt-sleep-baby-reader-w2.txt`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, posts 2026-06-25 → 2026-08-24). Voice file: `voice/reddit-r32.jsonl`. Scratch (unit list `units.txt`, per-batch spec files `b01.json`…`b10.json`, `add.py` builder, `show.sh` reader, `log.md` exclusion log, `index.txt`): `scratchpad/R32/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 9 (`read-w2-keep_core-063` … `-071`) |
| units in those chunks | 136 (15/18/10/21/16/13/15/13/15) |
| units read in full (post + every OP reply) | 136 |
| units excluded entirely (safety) | 5 |
| units read, not quoted (age, cross-post, thin) | 14 |
| units quoted | 117 |
| quotes written | 386 (sb32-0001 … sb32-0386), `verify_quotes.py` 0 failed, ids unique |
| restricted quotes | 14 (listed in `synthesis/reader-notes-r32.md`) |

Counts are of quotes chosen, never of people. Posts span 2026-07-21 to 2026-07-25; OP replies run to 2026-10-22.

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `Mommit-1v2xkjp` | 063 | safe-sleep incident (fall from a sleep space) |
| `beyondthebump-1v3sjt1` | 065 | safe-sleep incident (unsafe sleep arrangement, suffocation fear) |
| `sleeptrain-1v4fg7e` | 067 | safe-sleep incident (rolling, face in mattress) |
| `NewParents-1v4isa5` | 067 | mental-health crisis wording; unsafe sleep arrangement |
| `Parenting-1v4yaeq` | 069 | safe-sleep incident (parent fell asleep nursing in the adult bed) |

## Read in full, not quoted

| unit | chunk | reason |
|---|---|---|
| `toddlers-1v32rpy` | 063 | child almost 3 (over the 0–24 month brief); thin |
| `toddlers-1v3dz43` | 064 | cross-post of `sleeptrain-1v3egu2`; quoted from that copy |
| `sleeptrain-1v48y1z` | 066 | cross-post of `NewParents-1v48wjv`; quoted from that copy |
| `sleeptrain-1v4fq6u` | 067 | cross-post of `sleeptrain-1v4fuw9`; quoted from that copy |
| `toddlers-1v4lf83` | 067 | child 2.5 (over brief); toddler-bed transition |
| `toddlers-1v4ul0e` | 068 | child 2.5 (over brief); bed-sharing |
| `Mommit-1v4uwvr` | 068 | cross-post of `toddlers-1v4ul0e` |
| `toddlers-1v4wtm1` | 068 | child 2.5 (over brief); parent anger wording |
| `NewParents-1v596rk` | 069 | early-morning gas at 4 months; thin |
| `AttachmentParenting-1v5mmyr` | 071 | child 3 (over brief) |
| `toddlers-1v5my9p` | 071 | child 2.5, pacifier weaning |
| `Parenting-1v5snzg` | 071 | children 4 and 2; older child's anxiety |
| `toddlers-1v5t7ur` | 071 | children 2.5 and 4; parent anger wording |
| `toddlers-1v5tljt` | 071 | child 3.5, bed-rail product |

Partly quoted over-age units: `Mommit-1v4qbhv` (child 2.5; two looking-back lines about reaching independent sleep at ~19 months), `Parenting-1v4woz9` (12-month-old plus 3.5-year-old; quoted for the 12-month-old's bedtime).

## How to continue

Nothing unread in this assignment. Any re-run must use a new prefix; never append to `voice/reddit-r32.jsonl`.
