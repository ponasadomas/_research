# Reddit reading ledger — R48 (wave 3, sleep-baby, core chunks)

Reader R48 · id prefix `sb48` · voice file `voice/reddit-r48.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 10 (`read-w3-keep_core-031` … `read-w3-keep_core-040`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 156 (13/18/16/16/14/17/19/16/13/14; posts dated 2026-04-13 → 2026-04-17; OP replies to 2026-09-22) |
| Units read in full | 156 |
| Units excluded entirely | 16 (8 for safe-sleep, infant-health-fear, mental-health-crisis, harsh-words or medical-device content; 8 duplicate cross-posts) |
| Units read, nothing quoted | 3 (see below) |
| Units quoted | 137 |
| Quotes written | 441 (ids sb48-0001 … sb48-0441, unique) |
| Restricted quotes | 3 (listed in `synthesis/reader-notes-r48.md`) |
| possible_promo quotes | 2, from 2 units (never counted as parent voice) |
| verify_quotes.py | 441 quotes, 0 failed |

Per chunk (units / units quoted / quotes): 031 13/13/50 · 032 18/16/47 · 033 16/14/48 · 034 16/15/51 · 035 14/13/47 · 036 17/15/44 · 037 19/17/46 · 038 16/12/39 · 039 13/13/39 · 040 14/9/30. (Units quoted counts cross-posts whose body was not quoted but whose distinct OP reply was.)

Chunk-to-unit list: `scratchpad/R48/units.txt`. Short-form quote sources: `scratchpad/R48/q031.jsonl … q040.jsonl`, built into the voice file by `scratchpad/R48/build.py`. Working log (per-chunk exclusions, lines not quoted, money): `scratchpad/R48/log.md`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sl4pxo.txt` | duplicate cross-post of `NewParents-1sl4n8t` (same text, no OP replies) |
| `../_shared/_raw/reddit-2026/units/NewParents-1sla9gq.txt` | parent mental-health crisis wording throughout, plus newborn bedsharing detail |
| `../_shared/_raw/reddit-2026/units/ScienceBasedParenting-1slgpcm.txt` | infant injury in the cot (safe-sleep incident) |
| `../_shared/_raw/reddit-2026/units/NewParents-1slxbjd.txt` | parent fears a seizure during sleep (infant-health fear throughout) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sm9qno.txt` | duplicate cross-post of `Parenting-1sm8bmr` |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sm9s42.txt` | duplicate cross-post of `Parenting-1sm8bmr` |
| `../_shared/_raw/reddit-2026/units/NewParents-1smk4ur.txt` | bedsharing, tummy sleeping, monitor sock and SIDS detail throughout |
| `../_shared/_raw/reddit-2026/units/NewParents-1smptt8.txt` | room-sharing / SIDS-risk question; safe-sleep detail throughout |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1smxjdv.txt` | duplicate cross-post of `Parenting-1smxidb` |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sn6zt1.txt` | duplicate cross-post of `NewParents-1sn6ufu` (OP replies only on cosleeping and nap length) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sn7pry.txt` | duplicate cross-post of `toddlers-1sn7dl3` |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sne678.txt` | duplicate cross-post of `Parenting-1sne50l`; OP replies are medication and diet only |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1snejhd.txt` | duplicate cross-post of `Parenting-1snei4d` |
| `../_shared/_raw/reddit-2026/units/NewParents-1snek4o.txt` | parent's harsh words to the baby (never quoted) |
| `../_shared/_raw/reddit-2026/units/Parenting-1sni1mn.txt` | medical brace and sleepwear change throughout |
| `../_shared/_raw/reddit-2026/units/toddlers-1snkk4f.txt` | a baby rolled off the adult bed (safe-sleep incident) |

156 units = 137 quoted + 16 excluded (above) + 3 read with nothing quoted (below). `toddlers-1sneiyu` and `sleeptrain-1skzhj5`, `beyondthebump-1skxhdy`, `NewParents-1sljaeh`, `toddlers-1smmptr` are cross-posts whose bodies were not re-quoted but whose distinct OP replies or lines were, so they count as quoted.

## Units read, nothing quoted

| unit | why |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sl9ee7.txt` | the whole ask hinges on a named medical condition |
| `../_shared/_raw/reddit-2026/units/NewParents-1sljuii.txt` | floor-bed product question with a one-line reply; nothing on the sleep problem |
| `../_shared/_raw/reddit-2026/units/NewParents-1sn0xqp.txt` | preterm birth and triple-feeding context is the whole post |

## Quote-level omissions inside quoted units

Bedsharing / cosleeping descriptions, crib accessories, room temperature, sleepwear near rolling, tummy or side sleeping, medication doses, named diagnoses (reflux, tongue tie, allergy, postpartum conditions), weight and percentile lines, a physical-restraint line and two yelling lines were not quoted; each is noted per chunk in `scratchpad/R48/log.md`.

## Continue

Nothing unread in this assignment. Duplicate cross-posts were resolved within these chunks only; cross-chunk duplicates were not checked.
