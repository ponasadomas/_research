# Reddit reading ledger — R27 (prefix sb27), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md` and `../_shared/_tools/prompt-sleep-baby-reader-w2.txt`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, posts 2026-06-25 → 2026-08-24). Voice file: `voice/reddit-r27.jsonl`. Scratch (unit list `units.txt`, reading batches `batch01–10.txt`, per-batch record specs `b01.py`…`b09.py`, builder `build.py`, `restricted.tsv`, exclusion log `notes.txt`): `scratchpad/R27/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-w2-keep_core-022` … `-029`) |
| units in those chunks | 125 (12/15/21/18/14/14/16/15) |
| units read in full (post + every OP reply) | 125 |
| units excluded entirely | 12 |
| units read, nothing worth quoting | 1 |
| units quoted | 112 |
| quotes written | 363 (sb27-0001 … sb27-0363), `verify_quotes.py` 0 failed |
| restricted quotes | 8 (listed in `synthesis/reader-notes-r27.md`) |

Counts are of quotes chosen, never of people. Posts span 2026-07-04 to 2026-07-08; OP replies run to 2026-10-08 (one three-month update, sb27-0249/-0250).

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `sleeptrain-1uo81vq` | 023 | duplicate cross-post of `beyondthebump-1uo8025` (quoted from that copy) |
| `beyondthebump-1uojbpq` | 024 | safe-sleep incident (adult sleeping with infant on a couch); medical |
| `toddlers-1uoknsj` | 024 | duplicate cross-post of `Parenting-1uokmkj` (quoted from that copy) |
| `beyondthebumpUK-1uost71` | 025 | bedsharing safety question |
| `beyondthebumpUK-1uou0ef` | 025 | infant bedding / sleep-death risk discussion |
| `toddlers-1up2ohg` | 025 | bedsharing plus physically holding a child still to sleep |
| `toddlers-1up32no` | 025 | bedsharing and couch sleep with toddlers; harsh wording toward child |
| `Mommit-1up50mz` | 025 | duplicate cross-post of `NewParents-1up4ya2` (quoted from that copy) |
| `Mommit-1upnk23` | 027 | mental-health crisis wording |
| `Parenting-1upwj0h` | 028 | duplicate cross-post of `toddlers-1uprpvh` (quoted from that copy) |
| `beyondthebump-1uq5nik` | 028 | bedsharing safety question |
| `Mommit-1uqiakq` | 029 | child 3.5 years (over the niche age); medication advice |

## Read in full, not quoted

| unit | chunk | reason |
|---|---|---|
| `NewParents-1uq9oub` | 029 | bottle-to-sleep and dental worry; no sleep scene worth quoting |

Within quoted units, lines about bedsharing and cosleeping, prone or chest sleeping, loungers and swings, medication and supplements (except one restricted purchase quote), named medical conditions, and a parent's raised voice or restraint were left out, and the rest quoted. Units where this applied: 1unjeeo, 1unku2n, 1unna32, 1unqbcc, 1unrt37, 1unx5en, 1uochv0, 1uodrau, 1uokmkj, 1uolf9g, 1uolxp4, 1uom4n9, 1uoojn9, 1uoq7f0, 1uov94c, 1uowssd, 1uoy57g, 1uozj06, 1up1mdf, 1up1zkp, 1up405a, 1up7fs8, 1up7ye5, 1upg1v6, 1upg52w, 1uphj99, 1upkd6n, 1upkivl, 1upoop5, 1upossh, 1upqa6d, 1upqhm2, 1upx6c9, 1upzc1t, 1upzsos, 1uq4lyj, 1uq5jq1, 1uq8udg, 1uqa8lk, 1uqce4z, 1uqd6vt, 1uqe6i9, 1uqi79s, 1uqi7s2, 1uqios4.

Stage: 4-month babies outside a regression context are `baby_2_4_months`; `regression_4_months` is used where the post is about the regression or the baby is about 16–19 weeks in a regression (8 quotes). Speakers: `FTM`, `first time mum`, nursing, pumping or pregnancy count as self-identification; posting in r/FirstTimeMom alone does not.

## What has and hasn't been read

Every unit in the eight chunks was read in full. Nothing unread.

## How to continue

Nothing left in this assignment. Never append to `voice/reddit-r27.jsonl` from another agent; new reads take a new prefix.
