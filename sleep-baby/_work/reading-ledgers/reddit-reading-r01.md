# Reddit full reads: reader R01 (keep_purchase 001–008)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder).

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_purchase-001` … `-008`) |
| units in those chunks | 141 |
| units read in full (post + every OP reply archived in the unit) | 141 |
| units excluded | 0 |
| units read, no quote taken | 4 (below) |
| units quoted | 137 |
| quotes written | 328 (`voice/reddit-r01.jsonl`, ids `sb01-0001` … `sb01-0328`) |
| verify | `verify_quotes.py voice/reddit-r01.jsonl` → 328 quotes, 0 failed |

Units per chunk: 001 = 25, 002 = 19, 003 = 19, 004 = 15, 005 = 17, 006 = 20, 007 = 19, 008 = 7.

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1w3o0yz.txt` | cross-post, same text as `sleeptrain-1w3nz8p` (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wkjq68.txt` | cross-post, same text as `NewParents-1wkjpfx` (quoted there) |
| `../_shared/_raw/reddit-2026/units/Mommit-1wkjqjv.txt` | cross-post, same text as `NewParents-1wkjpfx` (quoted there) |
| `../_shared/_raw/reddit-2026/units/toddlers-1wo6vvd.txt` | bed-frame shopping, nothing about sleep beyond style choice |

`beyondthebump-1wngter` is a cross-post of `NewParents-1wngsfw`; only its one unique OP reply was quoted (sb01-0268).

## Passages read but deliberately not quoted (lines not to cross)

Units stay in; only these passages were skipped.

- `NewParents-1wrhlo5` comment `pccn0rn` and nearby: argument between parents with a safe-sleep statistic in it. Not quoted (README: safe-sleep statements only from primary guidance). The parent's own fear lines from the same thread are quoted.
- `sleeptrain-1wzgkhv` comments `pebw27g` / `pebyvak`: a blanket in the cot described as a choice. Only the daycare line from `pebw27g` was quoted.
- `sleeptrain-1wdn7ui`: wanting to place the baby on the tummy for naps. Not quoted.
- Medical detail (reflux, CMPA, ferritin, eczema, vomiting, sleep-study referral) is in context lines only where needed, never as a cause.

## How to continue

Nothing assigned is unread. Do not append to `voice/reddit-r01.jsonl` from another agent; start a new file with a new prefix.
