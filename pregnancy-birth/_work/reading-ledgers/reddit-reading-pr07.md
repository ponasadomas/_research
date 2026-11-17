# Reddit full reads — reader PR07 (pregnancy-birth, keep_core 016–023)

Date: 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md`. Voice file: `../voice/reddit-pr07.jsonl` (ids pb07-0001 → pb07-0203). Notes: `../synthesis/reader-notes-pr07.md`. Scratch: `../scratchpad/PR07/` (units.txt = assigned unit list; s016–s023.py = per-chunk quote specs as start/end anchors cut from the raw unit; build.py writes the voice file and restricted list; rs_override.py = quote-level restriction for pb07-0001–0130 after the coordinator's rule clarification; excluded.tsv).

## Ledger

| step | count |
|---|---:|
| chunks assigned | 8 (`read-v1-keep_core-016` → `-023`) |
| units in those chunks | 143 |
| units read in full (post + every OP reply) | 143 |
| units excluded (safety) | 6 |
| units read, no quote (medical-centred, duplicate crosspost, or off-niche) | 29 |
| units with at least one quote | 108 |
| quotes written | 203 |
| restricted ids (quote level; see notes) | 18 |
| `verify_quotes.py` | 203 quotes, 0 failed |

## By chunk

| chunk | units | quotes | units read, no quote | excluded |
|---|---:|---:|---|---|
| keep_core-016 | 19 | 18 | pregnant-1w3iagx, pregnant-1w3nmbv, NewParents-1w3nn7d, BabyBumps-1w3q4xq, pregnant-1w3qlb1 (all symptom/test/medication questions) | — |
| keep_core-017 | 18 | 28 | pregnant-1w3vsb3 (fetal heart condition), BabyBumps-1w3zxz9 (GD supply logistics), pregnant-1w44h6n (tick bite) | pregnant-1w45fy4, pregnant-1w460o8 |
| keep_core-018 | 18 | 25 | BabyBumps-1w4k0wr and pregnant-1w4k3qs (identical crosspost on blood-pressure technique) | pregnant-1w4dca3 |
| keep_core-019 | 21 | 28 | pregnant-1w4miht (early location worry, ER), pregnant-1w4sa5b (symptom loss worry), pregnant-1w4u1qs (hospitalised, early induction), pregnant-1w4uzed (medication dose), pregnant-1w4waz7 (old marital hurt, off-niche), pregnant-1w4x94x (early spotting worry) | — |
| keep_core-020 | 22 | 31 | BabyBumps-1w5eb77 (crosspost of pregnant-1w5ea5x), Mommit-1w5k4hk (crosspost of BabyBumps-1w5gzvf), pregnant-1w5g41i (generic), pregnant-1w5hq0l (medication), pregnant-1w5k5ha (monitoring) | — |
| keep_core-021 | 11 | 23 | pregnant-1w5owtb (partner infidelity, off-niche) | pregnant-1w5pvsg |
| keep_core-022 | 18 | 21 | pregnant-1w5ry0z, pregnant-1w5vkxp, pregnant-1w5vmr1, pregnant-1w5z76n, PregnancyUK-1w62aw4, pregnant-1w62ug6 (all medical-centred), pregnant-1w5w4h1 (household anecdote) | pregnant-1w5qu58 |
| keep_core-023 | 16 | 29 | — | pregnant-1w6fs7z |

## Excluded (neutral reasons; nothing copied)

| unit | reason |
|---|---|
| pregnant-1w45fy4 | crisis wording |
| pregnant-1w460o8 | weighing ending the pregnancy |
| pregnant-1w4dca3 | centred on a wish to end the pregnancy; mental-health crisis |
| pregnant-1w5pvsg | crisis wording in OP reply |
| pregnant-1w5qu58 | self-harm wording in post |
| pregnant-1w6fs7z | crisis-adjacent wording; mental-health crisis at its centre |

## What has and hasn't been read

All 143 assigned units read in full. Nothing unread.

## How to continue

Do not append to `reddit-pr07.jsonl` from another agent. To rebuild exactly: `python3 -I scratchpad/PR07/build.py . scratchpad/PR07/s0[12]*.py` from the pregnancy-birth folder (it needs `scratchpad/PR07/rs_override.py`).
