# Reddit reading ledger — R51 (wave 3, sleep-baby, core chunks)

Reader R51 · id prefix `sb51` · voice file `voice/reddit-r51.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 9 (`read-w3-keep_core-059` … `read-w3-keep_core-067`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 151 (12/18/17/15/18/18/16/17/20; posts dated 2026-04-26 → 2026-04-29; OP replies to 2026-07-03) |
| Units read in full | 151 |
| Units excluded entirely | 12 (3 duplicate cross-posts, 9 for lines not to cross) |
| Units read, nothing quoted | 1 (`NewParents-1sya6rt`) |
| Units quoted | 138 |
| Quotes written | 470 (ids sb51-0001 … sb51-0470, unique) |
| Restricted quotes | 24 (listed in `synthesis/reader-notes-r51.md`) |
| possible_promo quotes | 0 (no seeded-looking post in this set) |
| verify_quotes.py | 470 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R51/units.tsv`. Short-form quote sources: `scratchpad/R51/q01–q09.jsonl` (one per chunk, `"r":1` marks restricted), built into the voice file by `scratchpad/R51/build.py`. Working log (per-chunk exclusions and lines deliberately not quoted): `scratchpad/R51/log.md`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sw7j07.txt` | swaddle exit because the baby rolled; sleepwear-near-rolling detail throughout |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1swdnik.txt` | duplicate cross-post of `sleeptrain-1sw7mdl` |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1swn8fm.txt` | duplicate cross-post of `sleeptrain-1swmf7z` (bedsharing and positioning detail) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1swxg6u.txt` | safe-sleep incident during training is the core of the post |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sxlqes.txt` | physical restraint of a child and caregiver anger at bedtime |
| `../_shared/_raw/reddit-2026/units/sahm-1sxz1lw.txt` | caregiver rage toward the baby; crisis wording |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sy2nb8.txt` | physical punishment of a toddler |
| `../_shared/_raw/reddit-2026/units/NewParents-1sy47t7.txt` | overnight chest sleeping and infant-death fear are the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1syayoy.txt` | prone and side day-sleep positioning is the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1syq42j.txt` | safety-monitor worry, sleep medication and missed-crying fear |
| `../_shared/_raw/reddit-2026/units/NewParents-1sz11wm.txt` | duplicate cross-post of `AttachmentParenting-1sz10wn` |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1sz1h4x.txt` | not a sleep-help post; centres on an infant-neglect news story and a caregiving lapse |

## Read, nothing quoted

| unit | why |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1sya6rt.txt` | a 17-month-old's possible nightmares; nothing beyond generic lines |

## Partial quoting

In about 30 quoted units, single lines were left out (bedsharing or chest sleeping, prone positioning, heating pads in cots, medication, named medical conditions, crisis wording). Each is listed per chunk in `scratchpad/R51/log.md`. Restriction was quote-level per the brief.

## Unfinished

None. Every unit in the nine chunks was read in full.
