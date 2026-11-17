# Reddit reading ledger — MR09 (sleep-mother, wave 3)

Reader MR09 · id prefix `sm09` · voice file `voice/reddit-mr09.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-sleep-mother-reader-w3.txt` · read 2026-10-25.
Window: posts 2026-05-15 → 2026-06-24 (wave 3 runs 1 April – 24 June). Corpus: `_raw/reddit/read-w3/chunks.jsonl` (frozen; not rebuilt). Assignment line `MR09` in `_raw/reddit/read-w3/assignments.txt` (125 units).

## Chunks assigned

| chunk | units | read in full | excluded | read, no quote | quotes | of which restricted |
|---|---|---|---|---|---|---|
| read-w3-keep_core-013 | 14 | 14 | 0 | 0 | 40 | 4 |
| read-w3-keep_core-014 | 16 | 16 | 1 | 0 | 43 | 3 |
| read-w3-keep_core-015 | 14 | 14 | 0 | 0 | 43 | 5 |
| read-w3-keep_core-016 | 10 | 10 | 0 | 1 | 41 | 6 |
| read-w3-keep_core-017 | 13 | 13 | 1 | 0 | 50 | 8 |
| read-w3-keep_core-018 | 17 | 17 | 2 | 1 | 42 | 10 |
| read-w3-keep_core-019 | 13 | 13 | 1 | 1 | 35 | 4 |
| read-w3-keep_core-020 | 17 | 17 | 2 | 0 | 45 | 5 |
| read-w3-keep_core-021 | 11 | 11 | 1 | 0 | 38 | 2 |
| **total** | **125** | **125** | **8** | **3** | **377** | **47** |

114 units quoted. Every unit was read in full, including every original-poster reply. Verify: `python3 -I _tools/verify_quotes.py voice/reddit-mr09.jsonl` → 377 quotes, 0 failed. Ids sm09-0001 … sm09-0377, unique. Restriction is quote-level (prompt rule); the list is in `synthesis/reader-notes-mr09.md`.

## Units excluded (not quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sahm-1tj70y2.txt` | post centred on domestic violence and a named postpartum condition with treatment |
| `../_shared/_raw/reddit-2026/units/PregnancyUK-1tvmeoc.txt` | post centred on named mental-health conditions and medication during a hospital induction |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1tzzzz3.txt` | post centred on a physical fight between partners |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1u0hfnf.txt` | post contains thoughts of harming the baby |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1u5hu4f.txt` | post centred on a night-time monitoring and safe-sleep scare |
| `../_shared/_raw/reddit-2026/units/NewParents-1u7wznv.txt` | post contains self-injury used to cope with pain |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1uabud7.txt` | post contains possible crisis wording |
| `../_shared/_raw/reddit-2026/units/NewParents-1ubl0l8.txt` | post centred on a named postpartum condition and its treatment |

## Units read, no quote

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/BabyBumps-1tsut8p.txt` | only content is a named phobia |
| `../_shared/_raw/reddit-2026/units/NewParents-1u1rket.txt` | identical cross-post of `beyondthebump-1u1rktw` (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1u5lpnt.txt` | cross-post of `sleeptrain-1u5i7gr` (quoted there) |

## Notes for whoever continues

- Possibly templated posts, tagged `possible_promo`, not to be counted as independent: `Mommit-1to34nv` (sm09-0096, sm09-0097) and `workingmoms-1to5h1j` (sm09-0098 … sm09-0101).
- Dates: records carry the post or comment date. Four comment dates fall after 24 June: sm09-0158, sm09-0159, sm09-0160 (2026-10-17, a five-month update in the same thread) and sm09-0377 (2026-06-25).
- Stage convention: a pregnant author with an older child is `experienced_mother` / `second_pregnancy` (prompt rule; 24 quotes), never a trimester stage.
- Helper used to build the file: `scratchpad/MR09/add.py` (rebuilds `voice/reddit-mr09.jsonl` from `scratchpad/MR09/drafts/*.jsonl`; do not re-run after another agent edits the voice file).
