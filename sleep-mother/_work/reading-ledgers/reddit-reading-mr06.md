# Reddit reading ledger — MR06 (sleep-mother, wave 2)

Reader MR06 · id prefix `sm06` · voice file `voice/reddit-mr06.jsonl` · brief `../_shared/_tools/brief-reading.md` · read 2026-10-25.
Window: posts 2026-06-25 → 2026-08-24 (wave 2, older posts). Corpus: `_raw/reddit/read-w2/chunks.jsonl` (frozen; not rebuilt).

## Chunks assigned

| chunk | units | read in full | excluded | read, no quote | quotes |
|---|---|---|---|---|---|
| read-w2-keep_core-019 | 16 | 16 | 1 | 0 | 39 |
| read-w2-keep_core-020 | 14 | 14 | 0 | 0 | 35 |
| read-w2-keep_core-021 | 20 | 20 | 0 | 1 | 37 |
| read-w2-keep_core-022 | 7 | 7 | 1 | 0 | 16 |
| read-w2-keep_otherside-001 | 11 | 11 | 0 | 0 | 28 |
| read-w2-keep_otherside-002 | 4 | 4 | 1 | 0 | 7 |
| read-w2-keep_otherside-003 | 3 | 3 | 0 | 0 | 11 |
| read-w2-keep_otherside-004 | 4 | 4 | 0 | 0 | 8 |
| read-w2-keep_purchase-001 | 14 | 14 | 1 | 0 | 35 |
| read-w2-keep_purchase-002 | 13 | 13 | 0 | 0 | 31 |
| read-w2-keep_success-001 | 8 | 8 | 1 | 0 | 16 |
| **total** | **114** | **114** | **5** | **1** | **263** |

108 units quoted. 56 of the 263 quotes are restricted (list in `synthesis/reader-notes-mr06.md`). Verify: `python3 -I _tools/verify_quotes.py voice/reddit-mr06.jsonl` → 263 quotes, 0 failed. Ids sm06-0001 … sm06-0263, unique.

## Units excluded (not quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1vp04qs.txt` | safe-sleep practices centre the post |
| `../_shared/_raw/reddit-2026/units/Mommit-1vx0az2.txt` | post centred on intrusive thoughts and acute distress |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1vjcr59.txt` | crisis wording in the poster's reply |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1uzdca4.txt` | post centred on a road-safety incident |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1uk7vtn.txt` | crisis wording in a looking-back post |

## Read in full, no quote

- `../_shared/_raw/reddit-2026/units/pregnant-1vtzw2i.txt` — 38 weeks, about induction; the only sleep line is "Can't sleep, so tired, etc.", too generic to use.

## Handling notes

- `daddit-1vcy6g3` (otherside-002): the post contains a road-safety passage (a drive he does not remember). That passage was not quoted. The unit was not dropped because it is not centred on that passage; its two quotes (sm06-0156, sm06-0157) come from a later reply and are restricted. `beyondthebump-1uzdca4` was dropped whole because the incident is the whole post.
- Several posts in r/Postpartum_Depression were read (core-019, core-020, otherside-002, otherside-003). Quotes from them are restricted.
- Mental-health, medication/supplement and safe-sleep wording was kept out of unrestricted quotes by trimming. Where a trim was not possible the quote is restricted.

## Continue

Nothing unread in this assignment. Don't append to `voice/reddit-mr06.jsonl` from another session; start a new reader file.
