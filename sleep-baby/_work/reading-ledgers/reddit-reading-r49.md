# Reddit reading ledger — R49 (wave 3, sleep-baby, core chunks)

Reader R49 · id prefix `sb49` · voice file `voice/reddit-r49.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 9 (`read-w3-keep_core-041` … `read-w3-keep_core-049`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 156 (16/21/18/13/19/16/17/16/20; posts dated 2026-04-17 → 2026-04-21; OP replies to 2026-09-05) |
| Units read in full | 156 |
| Units excluded entirely | 19 (12 safe-sleep, crisis, road-safety or similar; 4 out of age range or sleep-space-only; 3 duplicate cross-posts) |
| Units read, nothing quoted | 1 (`../_shared/_raw/reddit-2026/units/beyondthebump-1srgvb0.txt`: the whole ask is a suspected digestive/allergy medical issue in a 7-week-old) |
| Units quoted | 136 |
| Quotes written | 358 (ids sb49-0001 … sb49-0358, unique) |
| Restricted quotes | 4 (listed in `synthesis/reader-notes-r49.md`) |
| possible_promo quotes | 0 (no seeded-looking post in this set) |
| verify_quotes.py | 358 quotes, 0 failed |

Per chunk (units / units quoted / quotes): 041 16/12/31 · 042 21/21/46 · 043 18/16/42 · 044 13/13/46 · 045 19/16/41 · 046 16/14/45 · 047 17/15/31 · 048 16/14/42 · 049 20/15/34.

Chunk-to-unit list: `scratchpad/R49/units.txt`. Short-form quote sources: `scratchpad/R49/q01–q14.jsonl`, built into the voice file by `scratchpad/R49/build.py` (fills url, date, post and comment ids from the unit headers; puts seed themes first). Working log with per-batch skipped lines: `scratchpad/R49/log.md`.

**Exclusion rule used.** A unit is excluded entirely when a never-quote category (mental-health crisis wording, a safe-sleep incident or bedsharing or sleepwear-near-rolling detail, a road-safety incident) is the substance of the post. Otherwise only the lines in that category were skipped and the rest of the unit was quoted. Lines naming a medical condition, medication or test were skipped, or the quote was restricted.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1snlrtw.txt` | mental-health crisis wording in the post |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1snqbpq.txt` | the whole ask is a sleep-space choice; bedsharing detail |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1snsogb.txt` | bedsharing and swaddle detail throughout |
| `../_shared/_raw/reddit-2026/units/NewParents-1snpe2h.txt` | duplicate cross-post of `sleeptrain-1snpfvg` (same text; the sleeptrain copy is longer and was quoted) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sotd4s.txt` | safe-sleep (cot-edge and bumper) detail is the whole post |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1sottwe.txt` | car-journey crying incident with a choking-risk detail; not a sleep question |
| `../_shared/_raw/reddit-2026/units/NewParents-1spkds5.txt` | sleepwear-near-rolling detail is the whole post (swaddle dropped for rolling) |
| `../_shared/_raw/reddit-2026/units/toddlers-1sporc7.txt` | child over 36 months (3.5 years) |
| `../_shared/_raw/reddit-2026/units/toddlers-1spyh1w.txt` | child over 36 months (3.5 years); bedsharing detail |
| `../_shared/_raw/reddit-2026/units/NewParents-1sq848h.txt` | duplicate cross-post of `sleeptrain-1sq854j` (identical text) |
| `../_shared/_raw/reddit-2026/units/Mommit-1sqio4j.txt` | duplicate cross-post of `NewParents-1sqikcy` (identical text) |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1sqkiem.txt` | safe-sleep detail throughout (rolling in a swaddle, sleep positioner, dozing with the baby) |
| `../_shared/_raw/reddit-2026/units/NewParents-1sqlh40.txt` | road-safety incident, mental-health and medical detail, bedsharing throughout |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sr8cg7.txt` | sleepwear-near-rolling detail is the whole post; medication |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sra6fw.txt` | the whole ask is a sleep-space suitability choice (outgrown bassinet) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1srdb2p.txt` | child over 36 months ("a little over three"); bedsharing transition |
| `../_shared/_raw/reddit-2026/units/NewParents-1srr2aj.txt` | mental-health crisis wording in the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1srrmb5.txt` | safe-sleep detail throughout (swaddling against loose blankets) |
| `../_shared/_raw/reddit-2026/units/NewParents-1sruft5.txt` | sleepwear-near-rolling detail is the whole post |

**Partly quoted.** `../_shared/_raw/reddit-2026/units/NewParents-1sqoiib.txt`: the post is a safe-sleep scare and was not quoted. Only three replies by the original poster, about choosing not to sleep train and about social media, were quoted (sb49-0258 … sb49-0260).

## Lines read but not quoted (whole categories)

Bedsharing or cosleeping detail (about 20 units), pain relievers and reflux or allergy treatment (8), named parental or child medical conditions (6), the parent's mental-health wording (5), sleepwear and room temperature (4), a child's breath-holding (1), a parent dozing while holding the baby (2). Each unit and line is listed per batch in `scratchpad/R49/log.md`.
