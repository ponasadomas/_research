# Reddit reading ledger — R42 (wave 3, sleep-baby)

Reader R42 · id prefix `sb42` · voice file `voice/reddit-r42.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 9 (`read-w3-keep_purchase-009` … `read-w3-keep_purchase-017`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 153 (16/18/17/20/22/26/15/14/5; posts dated 2026-05-14 → 2026-06-24; OP replies to 2026-09-28) |
| Units read in full | 153 |
| Units excluded entirely | 5 (4 for content, 1 duplicate cross-post) |
| Units read, no quote taken | 4 (product-sizing or safety-equipment posts with nothing for this niche) |
| Units quoted | 144 |
| Quotes written | 434 (ids sb42-0001 … sb42-0434, unique) |
| Restricted quotes | 6 (listed in `synthesis/reader-notes-r42.md`) |
| verify_quotes.py | 434 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R42/units.txt`. Short-form quote sources: `scratchpad/R42/q-009.jsonl` … `q-017.jsonl`, built by `scratchpad/R42/build.py` (fills url, date, post and comment ids from the unit header); field check `scratchpad/R42/check.py`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1thpk62.txt` | sleepwear-near-rolling detail is the whole post |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1tutp5p.txt` | sleepwear-near-rolling detail and overheating workaround are the whole post |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1u3anhl.txt` | safe-sleep detail (bedside-cot gap) is the whole post |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1uerzg8.txt` | safe-sleep detail (belly sleeping, travel-cot mattress) is the whole post |
| `../_shared/_raw/reddit-2026/units/toddlers-1uegyxd.txt` | duplicate cross-post of sleeptrain-1uegu71 (quoted there) |

## Units read, no quote taken

| unit | why |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1te175e.txt` | sleep-sack sizing question only |
| `../_shared/_raw/reddit-2026/units/toddlers-1tk5a9n.txt` | sleep-sack fabric search only |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tzrur5.txt` | toddler pillow shopping (bedding near safe-sleep line) |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1u9l5tm.txt` | radar-monitor alerts when the baby rolls (safety-monitor detail) |

## Units read, passages left out (neutral reasons)

| unit | passage not quoted |
|---|---|
| `NewParents-1tdh0m3` | partner's named mental-health condition |
| `sleeptrain-1teop1x` | iron question |
| `sleeptrain-1tfui05` | reflux history and medication |
| `NewParents-1th8pqt` | feeding disorder, allergy, medication, hospital, swaddle-and-rolling question |
| `Parenting-1thabhn` | mattress-firmness safety worry (only the price line quoted) |
| `sleeptrain-1tja2ix`, `sleeptrain-1tjy589`, `Parenting-1tmew7k`, `sleeptrain-1u09dda`, `sleeptrain-1triirr`, `sleeptrain-1tstlun`, `sleeptrain-1uec61v` | bedsharing and sleep-position details |
| `Parenting-1tmew7k`, `NewParents-1toncwd`, `sleeptrain-1ttmn6m`, `sleeptrain-1u6k3hg`, `sleeptrain-1trwwcr` | rolling with sleepwear or near cot rails |
| `sleeptrain-1tksulc`, `sleeptrain-1tluwbf`, `sleeptrain-1trmx6u` | prematurity, teething guidance, NICU and hip condition |
| `sleeptrain-1tm3ylc`, `beyondthebump-1u9og1z`, `sleeptrain-1uc9mkq` | reflux, allergy formula, iron supplements, ear tubes |
| `sleeptrain-1to4yno` | mental-health wording, unsafe holding position |
| `sleeptrain-1tnxwll`, `sleeptrain-1u715v7` | baby hitting head in the cot |
| `sleeptrain-1tynkng`, `Parenting-1u8w22y`, `sleeptrain-1ub1ho2`, `Parenting-1u95wax` | parent mental-health wording; parent injury |
| `sleeptrain-1tzkxyw` | car-nap safety details |
| `daddit-1tx1jrr` | worry about baby getting stuck in cot corners |
| `beyondthebump-1tr7d0i` | wish for sleep medication for the baby |
| `NewParents-1u9yjdg` | speculation about a carer's medication or substances; a relative's dementia |
| `sleeptrain-1ua2wo5` | parent falling asleep with the baby |

## Notes on the set

- `sleeptrain-1tksulc` and `sleeptrain-1tluwbf` are very likely the same parent (same ages, same schedules, a day apart); count as one voice.
- `daddit-1tx1jrr` tagged `possible_promo` (a three-brand comparison that ends on one brand's feature list). Not to be counted.
- Two quotes that name cosleeping or overnight contact sleep are kept but restricted (sb42-0081, sb42-0425).
- No units in this set from the "Actually Sleeping" testimonial authors, the four-copy coach, "DM for PDF" or teaser posts; `sleeptrain-1tk30cs` is a parent asking whether Actually Sleeping is a scam.
