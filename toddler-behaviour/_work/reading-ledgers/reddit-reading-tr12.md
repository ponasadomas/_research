# Reddit full reads — TR12 (wave 2, 2026-06-25 → 08-24)

Brief: `../_shared/_tools/brief-reading.md`. Reader TR12, id prefix `tb12`, voice file `voice/reddit-tr12.jsonl`, scratch `scratchpad/TR12/`. Read 2026-10-25 (one session, resumed once after a usage-limit stop; no records were lost or re-numbered: ids are assigned at assembly from the staging files `scratchpad/TR12/s01–s13.jsonl` by `scratchpad/TR12/assemble.py`).

## Chunks assigned (from `_raw/reddit/read-w2/assignments.txt`)

| chunk | units |
|---|---|
| read-w2-keep_core-007 | 16 |
| read-w2-keep_core-008 | 17 |
| read-w2-keep_core-009 | 17 |
| read-w2-keep_core-010 | 17 |
| read-w2-keep_core-011 | 18 |
| read-w2-keep_core-012 | 17 |
| read-w2-keep_core-013 | 15 |
| read-w2-keep_core-014 | 17 |
| **total** | **134** |

Post dates in these chunks run 2026-07-01 → 2026-07-09 (OP follow-ups up to 2026-08-22).

## Counts

- Units in chunks: 134
- Units read in full: 134 (none unfinished)
- Units excluded (safety, medical or privacy lines; nothing quoted): 15
- Units read, no quote (not a safety exclusion): 1
- Units quoted: 118
- Quotes written: 284 (tb12-0001 … tb12-0284), ids unique
- Restricted units (diagnosis, developmental or ADHD/autism question, or the author's own diagnosis; only fear or strain quoted): 17 units, 38 quotes (listed in `synthesis/reader-notes-tr12.md`, "Restricted ids")
- Verify: `python3 -I _tools/verify_quotes.py voice/reddit-tr12.jsonl` → 284 quotes, 0 failed

## Units excluded (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1um0jah.txt` | physical force toward a child; parent's own childhood abuse |
| `../_shared/_raw/reddit-2026/units/pottytraining-1umosig.txt` | physical restraint; medication details |
| `../_shared/_raw/reddit-2026/units/NewParents-1umsxv9.txt` | child body / privacy topic |
| `../_shared/_raw/reddit-2026/units/toddlers-1umulj2.txt` | restraint used as a consequence (13-month-old) |
| `../_shared/_raw/reddit-2026/units/Mommit-1un7ecx.txt` | child-safety incident with a co-parent; child trauma response |
| `../_shared/_raw/reddit-2026/units/pottytraining-1uncvzs.txt` | medical treatment details |
| `../_shared/_raw/reddit-2026/units/pottytraining-1uogolt.txt` | medical treatment details (emergency visit, medication) |
| `../_shared/_raw/reddit-2026/units/toddlers-1upe37e.txt` | medical growth concern; force-feeding mention |
| `../_shared/_raw/reddit-2026/units/Mommit-1upeex0.txt` | verbal harshness toward children; medication |
| `../_shared/_raw/reddit-2026/units/pottytraining-1upfeqr.txt` | medical diagnosis and treatment details |
| `../_shared/_raw/reddit-2026/units/Mommit-1uphmor.txt` | physical punishment of a child |
| `../_shared/_raw/reddit-2026/units/Parenting-1uq1mfj.txt` | physical punishment of a child |
| `../_shared/_raw/reddit-2026/units/toddlers-1uqdkni.txt` | physical restraint; verbal harshness |
| `../_shared/_raw/reddit-2026/units/pottytraining-1uqfz7f.txt` | physical restraint; ADHD question |
| `../_shared/_raw/reddit-2026/units/toddlers-1ur9amm.txt` | physical restraint; medical procedure |

## Units read, no quote

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1umbdah.txt` | duplicate cross-post of `Parenting-1umbaxf` (quoted there) |

## Other cross-posts (both copies read; quotes taken from different text)

`pottytraining-1umo23m` / `toddlers-1umyjy6` (post quoted in the first, OP's day-2 update in the second); `toddlers-1upg0fg` / `Mommit-1upg1v6` (post quoted in the first, OP reply in the second). `pottytraining-1ulgzdk`, `pottytraining-1ulriob` and `pottytraining-1un8dl4` are the same parent's three posts (Oh Crap day 13–15, poop withholding); quotes differ. Dedupe by post text at merge.

## Lines I kept out of quotes inside quoted units

Carrying or dragging a child to the car seat and the child's "don't hit me" (1umbaxf); "half-drag them to the toilet" (1up2x8u); relatives' advice to hit or smack the child (1um5f7y, 1uoalek — trimmed out with ` […] ` in tb12-0127); the child's cruelty to a pet (1um5f7y); parents' own yelling or screaming at the child (1umbziv, 1upvasp, 1uqcojh, 1uo8rjp post); a child scratching their own face or biting themselves (1un4s8c, 1unl5e8, 1umbziv reply); laxatives, suppositories, stool details, rashes, wiping and genital mentions (1ulgzdk, 1un8dl4, 1um0iaq, 1unpoa6, 1unqhzu, 1upfe44, 1upbely, 1uprfpb, 1upx56q); sleep pills and medication (1urb1i2); a speech-therapy start (1up1qx3); a daycare teacher's arrest named as the reason for leaving daycare (1uqex49 reply);
 UTI and antibiotic rounds (1up5y2z, quoted only for the shame line tb12-0160); the laxative reply (1un4myu); the pool accident's details (1unzekj); a parent's postpartum depression medication and own diagnoses (1uor2k7, 1upv1zr).

## How to continue

Nothing unread in these chunks. If records must be rebuilt, rerun `python3 -I scratchpad/TR12/assemble.py` (deterministic: files in name order, ids in order), then verify. Never renumber once findings cite `tb12` ids.
