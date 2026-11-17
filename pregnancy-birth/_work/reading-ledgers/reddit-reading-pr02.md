# Reddit full reads — reader PR02 (pregnancy-birth, keep_purchase + keep_success)

Date: 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md`. Voice file: `../voice/reddit-pr02.jsonl` (ids pb02-0001 → pb02-0257). Notes: `../synthesis/reader-notes-pr02.md`. Scratch: `../scratchpad/PR02/` (chunk dumps c1–c8.txt and split parts p*_0*, per-batch quote inputs q1–q7.jsonl, helpers add.py / chk.py / dump.py, restricted.txt).

## Ledger

| step | count |
|---|---:|
| chunks assigned | 8 (`read-v1-keep_purchase-009` → `-012`, `read-v1-keep_success-001` → `-004`) |
| units in those chunks | 126 |
| units read in full (post + every OP reply) | 126 |
| units excluded (safety, nothing quoted) | 4 |
| units read, not quoted for medical-claim / medication reasons | 4 |
| duplicate / cross-posted units read, no new quote | 5 |
| units read, nothing quotable (generic or off-target) | 10 |
| units with at least one quote | 103 |
| quotes written | 257 |
| restricted ids (listed in notes) | 69 |
| `verify_quotes.py` | 257 quotes, 0 failed |

## By chunk

| chunk | units | quotes | units with no quote |
|---|---:|---:|---|
| read-v1-keep_purchase-009 | 20 | 46 | pregnant-1wy11du (cats + baby registry, generic), pregnant-1wze2fj (babymoon timing, generic), Mommit-1wzstu3 (cross-post of PregnancyUK-1wzssr2) |
| read-v1-keep_purchase-010 | 23 | 37 | beyondthebump-1wzy8cu (registry-discount tip), BabyBumps-1x1dged (duplicate of pregnant-1x1dlix), BabyBumps-1x2prcy (shower invite etiquette), pregnant-1x2q3wu (duplicate of BabyBumps-1x2q350), BabyBumps-1x3o13h (not pregnant; aunt asking about courses, off-target) |
| read-v1-keep_purchase-011 | 24 | 38 | beyondthebump-1x4de0b (crib fit; medical stress only in passing), pregnant-1x5ecui (advent calendars), BabyBumps-1x60u34 (clearance jeans tip) |
| read-v1-keep_purchase-012 | 20 | 36 | pregnant-1xa5pkw (sexual anecdote with a product link), pregnant-1xdvvts (one-line supplement question) |
| read-v1-keep_success-001 | 7 | 16 | pregnant-1vztgcx (**excluded**), pregnant-1vzxrz4 (duplicate of BabyBumps-1vzg66p) |
| read-v1-keep_success-002 | 10 | 30 | pregnant-1w2kqyf (not quoted: medical/vaccine claim), pregnant-1w5u2wa (**excluded**) |
| read-v1-keep_success-003 | 10 | 25 | PregnancyUK-1w69m1c (not quoted: medication side effects, mental health), pregnant-1w6mybw (not quoted: medical self-treatment advice), pregnant-1w7mowo (not quoted: condition + panic during surgery) |
| read-v1-keep_success-004 | 12 | 29 | pregnant-1w9nvft (**excluded**), PregnancyUK-1waep30 (**excluded**), pregnant-1wecz35 (duplicate of PregnancyUK-1we1pnz) |

## Excluded units (neutral reason, nothing quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/pregnant-1vztgcx.txt` | birth story centred on an acute obstetric emergency |
| `../_shared/_raw/reddit-2026/units/pregnant-1w5u2wa.txt` | birth story centred on an acute medical complication after delivery |
| `../_shared/_raw/reddit-2026/units/pregnant-1w9nvft.txt` | birth story centred on an acute emergency during labour |
| `../_shared/_raw/reddit-2026/units/PregnancyUK-1waep30.txt` | short post centred on an acute pregnancy complication and emergency surgery |

## Read, not quoted (medical claim or medication)

`pregnant-1w2kqyf` (newborn illness, vaccine advocacy), `PregnancyUK-1w69m1c` (anti-nausea medication side effects), `pregnant-1w6mybw` (self-treatment tips for a condition), `pregnant-1w7mowo` (condition diagnosis and panic during surgery).

## Handled under the passing-mention / medical rule (quoted only away from the sensitive lines; ids restricted)

`beyondthebump-1x4i7t6` + `Doulas-1x4iaw4` (same author; doula-contract story with an emergency surgical birth and a mental-health diagnosis in the background), `BabyBumps-1w66v0t` (reflective story whose birth became an emergency), `BabyBumps-1vzg66p` (positive story listing medical conditions), `BabyBumps-1vzwm41` (treatment story), `NewParents-1vzyb0f`, `pregnant-1w0ke6u`, `pregnant-1w558q9` (postpartum or pregnancy mental health), `pregnant-1w5hk6p` (prior birth complication), `pregnant-1x5yf7l` (fertility treatment mentioned), `PregnancyUK-1we1pnz` (conditions and medication). Full list of restricted ids in the notes.

## How to continue

Nothing unread in these chunks. Do not re-run this reader; it appends to `voice/reddit-pr02.jsonl`.
