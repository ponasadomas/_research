# Reddit reading ledger — R55 (wave 3, sleep-baby)

Reader R55 · id prefix `sb55` · voice file `voice/reddit-r55.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` · scratch `scratchpad/R55/` (unit list, batch files b01–b10, add script, restricted list, exclusions, progress log, id index).

## Chunks assigned

`read-w3-keep_core-096` … `read-w3-keep_core-105` (10 chunks, line `R55` of `_raw/reddit/read-w3/assignments.txt`; 151 units). Posts dated 2026-05-14 → 2026-05-19; OP replies up to 2026-08-19.

| chunk | units | read in full | units quoted | quotes |
|---|---|---|---|---|
| read-w3-keep_core-096 | 18 | 18 | 15 | 55 |
| read-w3-keep_core-097 | 18 | 18 | 18 | 67 |
| read-w3-keep_core-098 | 12 | 12 | 11 | 43 |
| read-w3-keep_core-099 | 15 | 15 | 14 | 45 |
| read-w3-keep_core-100 | 12 | 12 | 12 | 48 |
| read-w3-keep_core-101 | 19 | 19 | 18 | 47 |
| read-w3-keep_core-102 | 18 | 18 | 15 | 40 |
| read-w3-keep_core-103 | 13 | 13 | 10 | 37 |
| read-w3-keep_core-104 | 14 | 14 | 11 | 31 |
| read-w3-keep_core-105 | 12 | 12 | 7 | 25 |
| **total** | **151** | **151** | **131** | **438** |

All 151 units read in full. Quotes written: 438 (ids sb55-0001 … sb55-0438, unique). Verify: `python3 -I _tools/verify_quotes.py voice/reddit-r55.jsonl` → 438 quotes, 0 failed.

## Units excluded (nothing quoted)

| # | unit | chunk | reason |
|---|---|---|---|
| 6 | `toddlers-1tcu9nv` | 096 | verbal harshness toward a toddler at night (parent anger) |
| 42 | `toddlers-1tdw6co` | 098 | safe-sleep detail (toddler bed rail entrapment worry) |
| 54 | `NewParents-1teat0n` | 099 | medical throughout (birth injury, allergy and reflux history, testing, medication); posted on behalf of a friend |
| 92 | `NewParents-1tfe9r5` | 101 | parent mental-health wording (named postnatal condition, breaking-point crisis wording) |
| 99 | `toddlers-1tfnfwe` | 102 | parent restraining a toddler and raising voice at bedtime (physical force / verbal harshness); bereavement and therapy |
| 100 | `Parenting-1tfnr08` | 102 | cross-post of unit 99, same content, excluded for the same reason |
| 108 | `beyondthebump-1tfssib` | 102 | safe-sleep detail (toddler climbing out of cot, rolling out of bed, floor mattress) |
| 117 | `NewParents-1tg4wtq` | 103 | parent mental-health crisis wording, named condition and medication |
| 122 | `sleeptrain-1tg9qtj` | 103 | safe-sleep detail (prone sleeping on parents, couch sleeping); birth medical history |
| 127 | `sleeptrain-1tgcvhu` | 104 | parent crisis wording |
| 134 | `NewParents-1tgozy3` | 104 | safe-sleep detail (newborn sleeping on a parent overnight, recliner sleeping) |
| 142 | `NewParents-1tgxsu8` | 105 | safe-sleep incident (parent fell asleep with a newborn in a recliner); infant breathing scare; postnatal mood wording |
| 144 | `toddlers-1th0888` | 105 | medical and mental-health history throughout (named diagnoses, medication, therapy) |
| 145 | `AttachmentParenting-1th0hd5` | 105 | child about 41 months (over 36 months, out of scope) |

## Read in full, not quoted (not exclusions)

| # | unit | reason |
|---|---|---|
| 16 | `Parenting-1td3c42` | cross-post of unit 15 (same text, same author) |
| 17 | `NewParents-1td3dti` | cross-post of unit 15 |
| 139 | `beyondthebump-1tgum67` | cross-post of unit 138 |
| 148 | `sleeptrain-1th73fb` | cross-post of unit 147 |
| 116 | `NewParents-1tg3l06` | feeding and mood change; nothing sleep-specific worth quoting |
| 141 | `NewParents-1tgvzil` | possible illness and feeding; nothing sleep-specific worth quoting |

Also: unit 5 (`beyondthebumpUK-1tcu5cd`) is the same author's UK cross-post of unit 1 with different wording; one quote taken from it (sb55-0029).

## Quote-level handling inside quoted units

Lines about bedsharing, cosleeping set-ups, rolling to the belly, sleepwear for a rolling baby, falls from beds, named illnesses, medication, monitors' heart-rate readings and parent mental-health conditions were left out of quotes in units 2, 9, 19, 23, 26, 27, 28, 29, 32, 33, 34, 37, 40, 46, 48, 49, 50, 53, 55, 56, 57, 60, 61, 70, 71, 74, 75, 79, 80, 87, 91, 94, 103, 104, 105, 109, 110, 118, 120, 123, 124, 125, 128, 132, 146, 147, 150. Eight quotes still touch a restricted topic and are listed in `synthesis/reader-notes-r55.md` under "Restricted ids".
