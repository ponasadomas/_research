# Reddit reading ledger — R47 (wave 3, sleep-baby, core chunks)

Reader R47 · id prefix `sb47` · voice file `voice/reddit-r47.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 9 (`read-w3-keep_core-022` … `read-w3-keep_core-030`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 154 (8/17/22/21/15/18/19/13/21; posts dated 2026-04-10 → 2026-04-13; OP replies to 2026-09-27) |
| Units read in full | 154 |
| Units excluded entirely | 4 (3 for safe-sleep or infant medical-emergency content, 1 for age over 36 months) |
| Duplicate cross-posts, not quoted | 4 |
| Units quoted | 146 |
| Quotes written | 455 (ids sb47-0001 … sb47-0455, unique) |
| Restricted quotes | 9 (listed in `synthesis/reader-notes-r47.md`) |
| possible_promo quotes | 3, from 2 units (never counted as parent voice) |
| verify_quotes.py | 455 quotes, 0 failed |

Per chunk (units / units quoted / quotes): 022 8/8/52 · 023 17/17/57 · 024 22/22/61 · 025 21/20/51 · 026 15/14/49 · 027 18/16/46 · 028 19/16/42 · 029 13/12/43 · 030 21/21/54.

Chunk-to-unit list: `scratchpad/R47/units.txt`. Short-form quote sources: `scratchpad/R47/q01–q10.jsonl`, built into the voice file by `scratchpad/R47/build.py` (which also writes `restricted.txt` and `promo.txt`). Working log with lines deliberately not quoted per unit: `scratchpad/R47/log.md`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1siu0th.txt` | child is past 36 months (turned 3 in February, posted in April); also medical detail throughout |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sjf3oe.txt` | infant choking episode and medical fear run through the whole post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sjzep2.txt` | safe-sleep detail is the whole post (family sleeping on a sofa, cosleeping, a net over the bassinet) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sk4rso.txt` | same post as `sleeptrain-1sjzep2` in another sub; same reason |

## Duplicate cross-posts (read, not quoted)

| unit | duplicate of |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sju8uj.txt` | `NewParents-1sju87c` (identical text) |
| `../_shared/_raw/reddit-2026/units/Mommit-1sjv230.txt` | `NewParents-1sju87c` (identical text) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sk3hn4.txt` | `FirstTimeMom-1sk37uj` (identical text) |
| `../_shared/_raw/reddit-2026/units/NewParents-1sk3hss.txt` | `FirstTimeMom-1sk37uj` (identical text) |

Partial duplicates where only new lines were quoted: `toddlers-1si47yr` (= `daddit-1si47am`), `Mommit-1sih1hm` (= `toddlers-1si7bvr`, reworded), `beyondthebump-1sigq06` (= `sleeptrain-1signi0` plus one line), `sleeptrain-1sjp4em` (= `toddlers-1shqoes` plus schedule), `Parenting-1sk3h0d` (= `FirstTimeMom-1sk37uj`; one distinct OP reply), `Parenting-1skkpyd` (= `NewParents-1sk8pr7` plus one line), `sleeptrain-1skr4n6` (= `toddlers-1skqegh` plus one line).

## Passages read but deliberately not quoted (neutral reasons; details per unit in `scratchpad/R47/log.md`)

Bedsharing and cosleeping set-ups, sleepwear or swaddle near rolling, rolling/side-sleeping, a grandparent's sleep-position suggestion, a hand over the face during contact naps, a newborn moved to its own room at two weeks (safe-sleep detail); reflux, skin, allergy, ear, tongue-tie and medication lines (medical); a parent holding a baby down to make him sleep and "force him to lay down" (physical force); anger-at-night and "I snapped" wording; postpartum-rage and weaning-mood lines (mental-health wording). Mommit-1sk3543: the 4-year-old's wakings are out of age scope; only the 20-month-old's lines quoted.
