# Reddit full reads — MR04, wave 2 (2026-10-25)

Reader MR04 · id prefix `sm04` · voice file `voice/reddit-mr04.jsonl` · brief `../_shared/_tools/brief-reading.md` · corpus `_raw/reddit/read-w2/chunks.jsonl` (frozen; unit paths relative to this folder). Posts dated 2026-06-25 → 2026-07-20 (the older end of wave 2). Scratch scripts, batch files and chunk dumps: `scratchpad/MR04/`.

## Ledger

| step | count |
|---|---:|
| chunks assigned | 9 (read-w2-keep_core-001 → 009) |
| units in them | 139 |
| units read in full (post + every OP reply in the unit) | 139 |
| units excluded (not quoted, neutral reason below) | 11 |
| units read, not quoted as reposts of a unit already quoted | 3 |
| units read, nothing quotable for this niche | 5 |
| units quoted | 120 |
| quotes written | 321 (sm04-0001 → sm04-0321) |
| restricted quotes (listed in `synthesis/reader-notes-mr04.md`) | 235 |
| verify_quotes.py | 321 quotes, 0 failed |

## Chunks

| chunk | units | read | excluded | reposts | quoted units | quotes |
|---|---:|---:|---:|---:|---:|---:|
| read-w2-keep_core-001 | 17 | 17 | 1 | 1 | 15 | 45 |
| read-w2-keep_core-002 | 14 | 14 | 1 | 0 | 13 | 38 |
| read-w2-keep_core-003 | 16 | 16 | 1 | 0 | 13 | 46 |
| read-w2-keep_core-004 | 12 | 12 | 1 | 0 | 11 | 35 |
| read-w2-keep_core-005 | 13 | 13 | 1 | 0 | 11 | 24 |
| read-w2-keep_core-006 | 17 | 17 | 0 | 0 | 16 | 40 |
| read-w2-keep_core-007 | 13 | 13 | 4 | 1 | 8 | 20 |
| read-w2-keep_core-008 | 19 | 19 | 2 | 1 | 15 | 31 |
| read-w2-keep_core-009 | 18 | 18 | 0 | 0 | 18 | 42 |

## Units excluded (neutral reasons; passages not copied)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/Mommit-1ugf62m.txt` | centred on mental-health crisis wording |
| `../_shared/_raw/reddit-2026/units/NewParents-1uhqf72.txt` | contains wording about not wanting to be here; medication offered |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1uk1avc.txt` | centred on medication and injections |
| `../_shared/_raw/reddit-2026/units/NewParents-1uoq7f0.txt` | safe-sleep incident; hallucination content |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1uq35v3.txt` | medication and an acute incident |
| `../_shared/_raw/reddit-2026/units/pregnant-1ut0uu0.txt` | prescription medication for sleep; dark-thoughts wording |
| `../_shared/_raw/reddit-2026/units/NewParents-1utiv1w.txt` | safe-sleep incident |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1uuf2wo.txt` | safe-sleep incident |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1uun3w3.txt` | medication dosing |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1uv9tjd.txt` | wording about not being here |
| `../_shared/_raw/reddit-2026/units/Mommit-1uw2p64.txt` | safe-sleep incident |

## Reposts (read, quoted once under the other copy)

| unit | quoted as |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1uf5yi6.txt` | `NewParents-1uf12ue` |
| `../_shared/_raw/reddit-2026/units/NewParents-1uu5z99.txt` | `Mommit-1uu5ymi` |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1uur8b7.txt` | `pregnant-1uur6zf` |

## Read, nothing quotable

| unit | why |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1ukockz.txt` | swaddle transition; baby sleep only |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1umlyqv.txt` | baby nap schedule only |
| `../_shared/_raw/reddit-2026/units/Mommit-1ur164q.txt` | holiday logistics; the sleep lines are co-sleeping and child medication |
| `../_shared/_raw/reddit-2026/units/Mommit-1uruosa.txt` | teething; infant medication dosing and the mother's medical condition |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1uwx8vc.txt` | medical symptoms and remedies |

Lines left out inside quoted units: a road incident (BabyBumps-1umdu30), medication lines (BabyBumps-1uogsr1, pregnant-1uoadn4, FirstTimeMom-1uos7gg), an upright-sleeping question (beyondthebump-1v1qj75).

## How to continue

Nothing in chunks 001–009 is unread. Speaker and stage follow the lead's rule: a pregnant author who already has a child is `experienced_mother` with stage `second_pregnancy` (15 records; not in the README vocabulary, and wave 1 used trimester stages for these). Restricted ids were set by a keyword pass over every quoted unit (mental health, medication, co-sleeping, monitors), then per unit; false hits such as "scream" for "cream" were left unrestricted.
