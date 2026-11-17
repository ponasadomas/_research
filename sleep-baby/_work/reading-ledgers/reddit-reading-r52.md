# Reddit reading ledger — R52 (wave 3, sleep-baby)

Reader R52 · id prefix `sb52` · voice file `voice/reddit-r52.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` · scratch `scratchpad/R52/` (unit list, batch files, helper scripts, restricted list, progress log).

## Chunks assigned

`read-w3-keep_core-068` … `read-w3-keep_core-076` (9 chunks, line `R52` of `_raw/reddit/read-w3/assignments.txt`; 160 units). Posts dated 2026-04-29 → 2026-05-04; OP replies up to 2026-07-11.

| chunk | units | read in full | units quoted | quotes |
|---|---|---|---|---|
| read-w3-keep_core-068 | 19 | 19 | 18 | 69 |
| read-w3-keep_core-069 | 13 | 13 | 13 | 50 |
| read-w3-keep_core-070 | 18 | 18 | 16 | 53 |
| read-w3-keep_core-071 | 17 | 17 | 15 | 50 |
| read-w3-keep_core-072 | 19 | 19 | 17 | 53 |
| read-w3-keep_core-073 | 17 | 17 | 15 | 50 |
| read-w3-keep_core-074 | 21 | 21 | 20 | 62 |
| read-w3-keep_core-075 | 14 | 14 | 14 | 49 |
| read-w3-keep_core-076 | 22 | 22 | 20 | 60 |
| **total** | **160** | **160** | **148** | **496** |

All 160 units read in full. Quotes written: 496 (ids sb52-0001 … sb52-0496, unique). Verify: `python3 -I _tools/verify_quotes.py voice/reddit-r52.jsonl` → 0 failed.

## Units excluded (nothing quoted)

| unit | reason |
|---|---|
| `daddit-1t0x2cx` | toddler climbing out of crib and fall-injury fear (safety incident) |
| `NewParents-1t10wax` | infant breathing and choking episodes, hospital stay (medical/safety) |
| `NewParents-1t17uks` | newborn safety worry after a special-care stay; parents' distress |
| `Mommit-1t1krah` | parent mental-health crisis wording and a partner's self-harm remark |
| `NewParents-1t2b517` | parent describes being hit as a child (physical force toward a child); self-reported neurodivergence |
| `sleeptrain-1t2zpn3` | face-down sleep position (safe-sleep detail) and breakdown wording |
| `beyondthebump-1t33wss` | child hitting head and falling in the crib (injury risk) |

## Units read, nothing quoted (not excluded)

| unit | reason |
|---|---|
| `sleeptrain-1szdftd` | cross-post of beyondthebump-1szdecd (no OP replies) |
| `Mommit-1t0coxo` | cross-post of NewParents-1t0cnv9 |
| `beyondthebump-1t0cqlx` | cross-post of NewParents-1t0cnv9 |
| `toddlers-1t0sz1z` | cross-post of sleeptrain-1t0sx3b; OP reply only about crib transition |
| `toddlers-1t1qnic` | cross-post of sleeptrain-1t1qhi3 |

Cross-posts quoted on both sides only where the text differs: `sleeptrain-1t0pj22` / `sleeptrain-1t0q8r8` (same parent's night log, posted twice; distinct lines quoted).

## Lines skipped inside kept units (neutral reasons)

Medical or medication detail (painkillers, Calpol/Nurofen/ibuprofen/paracetamol, reflux, CMPA, ear infection, fever, iron, vitamin worry, kidney issue, chiropractor, tongue tie, dentist/teeth, prematurity, parent's back injury): 1szce4g, 1szcoii, 1sze5nq, 1szkl5a, 1szkvmw, 1t02ss5, 1t06ei2, 1t0msz6, 1t0qdes, 1t0sxur, 1t104zf, 1t1fx6q, 1t1k2bd, 1t1kozb, 1t1ock6, 1t1qhi3, 1t1y8mo, 1t2frvr, 1t2lf40, 1t2logt, 1t2s5i0, 1t2xtcm, 1t370og.
Safe-sleep detail (bedsharing/cosleeping arrangements and their risks, rolling to tummy, unsupervised glider sleep, soft mattress, belly sleeping, heat in bed, crib falls, jumping off bed, sleep surfaces): 1szhx8a, 1szr6ud, 1t00aj9, 1t06ei2, 1t06tzx, 1t07xul, 1t0kfe5, 1t0o0qh, 1t0sxur, 1t0un68, 1t0uzy3, 1t0w1sd, 1t104zf, 1t1jei7, 1t1k2bd, 1t1oubs, 1t1smgo, 1t1yrm5, 1t225oo, 1t2kwha, 1t2n6xt, 1t31sw4, 1t3bz59 (rolling-on-baby fear, alcohol, unsafe relative care).
Mental-health wording (PPD/PPA, the parent's own MH): 1sztcnx, 1t0un68, 1t1shyj. Road safety: 1t04q9l (street darting). Nipple-touching sleep association: 1t370og.

Restricted quotes (quote-level, listed in `synthesis/reader-notes-r52.md` § Restricted ids): 12.

## How to continue

Nothing unread in this assignment. The voice file is complete; do not re-run R52 (it would append duplicates).
