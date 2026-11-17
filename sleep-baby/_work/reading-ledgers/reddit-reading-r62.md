# Reddit reading ledger — R62 (wave 3, sleep-baby)

Reader R62 · id prefix `sb62` · voice file `voice/reddit-r62.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` · read 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 10 (`read-w3-keep_core-164` … `read-w3-keep_core-173`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 159 (12/20/16/18/20/10/15/17/14/17; posts dated 2026-06-14 → 2026-06-20; OP replies to 2026-10-12) |
| Units read in full | 159 |
| Units excluded entirely | 11 (7 for content, 4 duplicate cross-posts) |
| Units quoted | 148 |
| Quotes written | 525 (ids sb62-0001 … sb62-0525, unique) |
| Restricted quotes | 13 (listed in `synthesis/reader-notes-r62.md`) |
| verify_quotes.py | 525 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R62/units.txt`. Reading batches: `scratchpad/R62/batch01–18.txt`. Short-form quote sources: `scratchpad/R62/q01–q18.jsonl`, built into the voice file by `scratchpad/R62/build.py`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1u64z85.txt` | parent-anger / physical-force line; bedsharing details |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1u6qzjm.txt` | the ask is about moving twins out of bedsharing |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1u7vera.txt` | mental-health crisis wording and verbal anger in the post |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1u892nd.txt` | all-night bedsharing is the whole post; parent mental health |
| `../_shared/_raw/reddit-2026/units/Mommit-1u8dvi3.txt` | duplicate cross-post of `Parenting-1u8dv78` (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1u8jnkj.txt` | duplicate cross-post of `NewParents-1u8jmm6` (quoted there); OP replies add nothing new |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1u9btw6.txt` | safe-sleep detail (rolling to the stomach in the cot) is the whole post |
| `../_shared/_raw/reddit-2026/units/NewParents-1u9buwe.txt` | duplicate of `sleeptrain-1u9btw6`, same safe-sleep content |
| `../_shared/_raw/reddit-2026/units/Parenting-1u9w3gd.txt` | safe-sleep detail (swaddling a rolling baby, monitor readings) is the whole post |
| `../_shared/_raw/reddit-2026/units/NewParents-1ua8ei6.txt` | parent's own insomnia, hallucination and sleeping-pill wording; baby sleep is peripheral |
| `../_shared/_raw/reddit-2026/units/NewParents-1uawafj.txt` | duplicate cross-post of `sleeptrain-1uavp4y` (quoted there) |

## Units quoted with passages left out (neutral reasons)

- `Mommit-1u5x0t7`: mental-health crisis wording in the opening and one reply not copied; bedsharing reply not copied.
- `sleeptrain-1ua0qco`: reply `otq0d6a` not copied (crisis and road-safety wording); bedsharing lines skipped.
- `sleeptrain-1u7ghqj`: a passage about a baby hitting her head while crying not copied.
- `toddlers-1u87xvf`: a passage about a toddler's self-injury during tantrums not copied.
- Bedsharing, rolling-to-tummy, swaddle-with-rolling, medication and medical-condition sentences were skipped in many otherwise quoted units (e.g. `sleeptrain-1u63vqq`, `sleeptrain-1u7nfg5`, `sleeptrain-1u988t9`, `sleeptrain-1u9osix`, `sleeptrain-1uamhai`, `sleeptrain-1u8t62t`).
- Cross-posts by the same author kept once each where OP replies differed: `sleeptrain-1uac4u0` / `AttachmentParenting-1uagm0j` (post quoted from the first, replies from the second); `NewParents-1u8jmm6` / `ScienceBasedParenting-1u8kml7` (one later reply from the second).
