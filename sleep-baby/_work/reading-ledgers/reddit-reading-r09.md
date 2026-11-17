# Reddit full reads — R09 ledger (2026-10-25)

Brief: `../_shared/_tools/brief-reading.md`. Voice file: `voice/reddit-r09.jsonl` (`sb09-0001` to `sb09-0305`). Notes: `synthesis/reader-notes-r09.md`. Scratch: `scratchpad/R09/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_core-047` to `-054` in `_raw/reddit/read-v1a/chunks.jsonl`) |
| units in those chunks | 133 (16 + 13 + 18 + 15 + 20 + 13 + 20 + 18) |
| units read in full | 133 |
| units excluded | 0 |
| units read, no quote taken | 6 (below) |
| units quoted | 127 |
| quotes written | 305 |
| `verify_quotes.py` | 305 quotes, 0 failed |

Posts dated 2026-09-14 to 2026-09-17; OP follow-ups run to 2026-10-14. Unit list in order: `scratchpad/R09/units.txt`.

## Read in full, no quote taken

| unit | reason |
|---|---|
| `Mommit-1wgajfg` | cross-post of `toddlers-1wga559` (same text; quoted there) |
| `Mommit-1wgq6gf` | cross-post of `sleeptrain-1wgqpuo` (quoted there) |
| `beyondthebump-1whcej6` | cross-post of `NewParents-1wgrv8w` (quoted there) |
| `Mommit-1whdtqf` | cross-post of `sleeptrain-1whdtaa` (quoted there) |
| `NewParents-1wijuim` | humour piece ("baby's POV" of a contact nap); no account of their own nights |
| `NewParents-1witiab` | one week postpartum; post is mainly about the mother's mental state and feeding pain. Mental-health content, not quoted (see restricted) |

`Mommit-1wg71qa` is a cross-post of `sleeptrain-1wg6ujx` but has one extra line; one quote taken from it.

## Restricted (safe sleep, infant-death fear, mental health)

Quoted only where the research needs it; flagged "RESTRICTED" in `context` and listed in the notes.

| id | unit | why |
|---|---|---|
| sb09-0117 | `ScienceBasedParenting-1wgzv7g` | parent fell asleep on the couch with a 3.5-month-old; how bedsharing began |
| sb09-0154 | `sleeptrain-1wh9wro` | exhausted parent brings baby into adult bed with bed rails |
| sb09-0189 | `NewParents-1whmbw3` | both parents keep falling asleep in the rocking chair with a six-week-old |
| sb09-0198 | `sleeptrain-1whnwxz` | ten-month-old rolled off an adult bed; trigger for crib training |
| sb09-0237 | `beyondthebump-1wi2z5q` | sleep-loss dreams of hallucinating and misplacing the baby |
| sb09-0289 | `toddlers-1wiof0c` | "slipping into a depression" |
| sb09-0052, sb09-0055 | `NewParents-1wgdsza` | "I'd be hospitalized"; "hallucinating and physical health decline" |
| sb09-0085 | `toddlers-1wgnawc` | "my mental health is deteriorating" |

Recorded, not quoted: `NewParents-1whmbw3` (wakes in panic to check the baby is breathing; asks about an Owlet); `NewParents-1whmhs4` comment pa5k736 (health "will get to an unsafe place"); `NewParents-1wik6au` (says she has PTSD from the screaming, baby "loses her breadth"); `NewParents-1witiab` (postpartum distress); `Parenting-1wgdd9i` ("making me so depressed"); `NewParents-1wgqgh9` (baby vomited from crying; quoted as vomiting, not restricted); `ScienceBasedParenting-1wgzv7g` (tummy-sleep questions, not quoted). No unit names a child except `sleeptrain-1wgl6a4` (one night-log line; that line was not quoted).

## How to continue

Nothing unread in this assignment. Do not re-run R09: the voice file is append-only and ids would collide.
