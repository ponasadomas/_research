# Reddit reading ledger — PR18 (pregnancy-birth, read-v1)

Date 2026-10-25. Reader PR18, id prefix `pb18`. Brief: `../../_shared/_tools/brief-reading.md`. Voice file: `../voice/reddit-pr18.jsonl`. Notes: `../synthesis/reader-notes-pr18.md`. Scratch: `../scratchpad/PR18/` (unit list, batch files, `add.py`, running notes, restricted list).

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1-keep_core-104` → `111`) |
| units in chunks | 145 |
| units read in full | 145 |
| units excluded (README / brief lines) | 13 |
| units read as crossposts of another unit | 2 |
| units read, no quote taken | 8 |
| units quoted | 122 |
| quotes written | 368 (pb18-0001 → pb18-0368), ids unique |
| restricted quotes (quote level) | 50 |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr18.jsonl` → 368 quotes, 0 failed |

Posts date from 8 Oct to 12 Oct 2026 (author replies to 22 Oct). Subs: r/pregnant 218 quotes, r/BabyBumps 70, r/PregnancyUK 37, r/Mommit 17, r/NewParents 10, r/FirstTimeMom 6, r/beyondthebump 5, r/beyondthebumpUK 5. Nothing left unread.

## Excluded units (neutral reasons, nothing copied)

| unit | reason |
|---|---|
| `pregnant-1x11lci` | centred on an early scan finding |
| `pregnant-1x14ztn` | relationship-safety concern |
| `pregnant-1x16dl1` | sexual-coercion disclosure |
| `pregnant-1x1csgv` | crisis wording |
| `pregnant-1x1gbn7` | acute medical / emergency care centred |
| `pregnant-1x1hsty` | medication risk and whether to continue a pregnancy |
| `pregnant-1x1lj12` | partner's serious diagnosis; whether to continue a pregnancy |
| `FirstTimeMom-1x20ph1` | possible family-safety concern |
| `pregnant-1x2uem6` | same author, near-repost of `FirstTimeMom-1x20ph1`; same reason |
| `FirstTimeMom-1x2nu1o` | centred on an emergency-room visit |
| `PregnancyUK-1x2sqlm` | mental-health and medication centred; continuation wording |
| `NewParents-1x347i5` | sexual-assault disclosure |
| `beyondthebump-1x351x1` | mental-health crisis wording and medication |

## Crossposts (read, quoted once under the other unit)

| unit | same text as |
|---|---|
| `FirstTimeMom-1x1gfpu` | `pregnant-1x1ftl5` |
| `BabyBumps-1x2k150` | `pregnant-1x2jyv9` |

## Read in full, no quote

| unit | why |
|---|---|
| `pregnant-1x1a1c5` | short scan-dating worry, nothing beyond the title |
| `pregnant-1x1tk1b` | fear of loss after a bumpy drive; loss history in reply |
| `pregnant-1x24muu` | toilet humour about a symptom |
| `pregnant-1x3c8i9` | question about athletes and hidden pregnancies (exercise) |
| `pregnant-1x3i4ee` | constipation humour; medication named |
| `pregnant-1x3qwrr` | generic post; replies templated — possible AI or engagement account |
| `pregnant-1x3wyd3` | bold header and structured question list, reads AI-written |
| `PregnancyUK-1x3xmoh` | question about a sterilisation procedure at surgery |

## How to continue

Nothing assigned is unread. Restricted ids are listed in full in `../synthesis/reader-notes-pr18.md` (section "Restricted ids"). Do not re-run this reader; it appends to `reddit-pr18.jsonl`.
