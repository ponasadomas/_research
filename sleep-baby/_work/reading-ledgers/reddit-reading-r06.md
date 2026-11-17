# Reddit full reads: reader R06 (keep_core 023–030)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder). Voice file: `voice/reddit-r06.jsonl` (ids `sb06-0001` … `sb06-0347`). Notes: `synthesis/reader-notes-r06.md`. Staging files the voice file was built from: `scratchpad/R06/in-023.jsonl` … `in-030.jsonl` (one per chunk, in id order; `staging-all.jsonl` is their concatenation), built by `scratchpad/R06/build.py` (fills url, date, post/comment id from the unit). Chunk text as read: `scratchpad/R06/c024.txt` … `c030.txt` (023 was read from the same unit files directly). Unit list: `scratchpad/R06/units.tsv`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_core-023` … `-030`) |
| units in those chunks | 123 |
| units read in full (post + every OP reply archived in the unit) | 123 |
| units excluded (lines not to cross) | 0 |
| units read, no quote taken | 1 (below) |
| units quoted | 122 |
| quotes written | 347 |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-r06.jsonl` → 347 quotes, 0 failed |

Units / quotes per chunk: core-023 = 14 / 52 (ids 0001–0052); core-024 = 14 / 49 (0053–0101); core-025 = 17 / 50 (0102–0151); core-026 = 19 / 52 (0152–0203); core-027 = 20 / 47 (0204–0250); core-028 = 17 / 37 (0251–0287); core-029 = 11 / 35 (0288–0322); core-030 = 11 / 25 (0323–0347).

Post and reply dates span 2026-09-03 to 2026-09-28. Counts are counts of quotes chosen, never of people.

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1w75vig.txt` | cross-post, same text as `NewParents-1w75uiq` (quoted there); no OP replies in either |

## Units read that sit at the edge of the niche (kept, only the sleep lines quoted)

- `beyondthebumpUK-1w6645y`: reactive dogs waking a 5-month-old; most of the thread is dog training. Quoted only the night line and the replies about being criticised for asking (sb06-0007 to 0010).
- `daddit-1w6q4ou`: a 4-year-old and a 2-year-old; mostly daytime behaviour. Quoted only the bedtime-until-11pm scene and the list tried (sb06-0100, 0101).
- `toddlers-1w8yes7`: an "advanced" two-year-old; long side discussion on giftedness and on food dyes. Neither is quoted (the dye claim would need fact-checking); only the lying-down bedtime and nap lines (sb06-0342, 0343).
- `toddlers-1w8rxe3`: crib-to-bed timing before a new baby; one quote (sb06-0327).

## Passages read but deliberately not quoted (lines not to cross)

Units stay in; only these passages were skipped.

- `sleeptrain-1w731pn` comment `p7tiz65`: the parent's description of the baby's colour change during three hours of crying. Trimmed out (no crying-harm statements either way); the "never doing that again" line is kept (sb06-0171).
- `NewParents-1w808zu` (reflux, possible tongue tie, formula changes, medication), `ScienceBasedParenting-1w8lxl0` (gas, elimination diet), `beyondthebump-1w6gxkl` (dairy/soy elimination, stool detail), `NewParents-1w8rag1` (reflux medication), `daddit-1w8cetj` (a respiratory condition the father names as the reason crying is risky): medical detail kept to neutral context lines, never quoted as a cause.
- `Mommit-1w8lqum`: medication names and doses, the child's illnesses and a kidney issue; the parent's sleep, marriage and work lines are quoted, the medical list is not.
- `beyondthebump-1w70kt8`: a line about wanting to use cannabis at night; the exhaustion and regret lines are quoted (sb06-0145, 0146), that clause is not.

## What has and hasn't been read

All 123 units in chunks core-023 to core-030 were read in full. Nothing in the assignment is unread.

Safe-sleep verdicts trimmed (README: safe-sleep statements only from primary guidance): `NewParents-1w8rag1` — a paediatrician's reported "probably fine" on tummy sleeping was cut from sb06-0323, and the morning-after "totally fine" verdict was cut from sb06-0325; only the parent's fear and relief are quoted.
