# Reddit reading ledger — PR31 (wave 2, 2026-10-25)

Reader PR31 · id prefix `pb31` · voice file `voice/reddit-pr31.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-pregnancy-reader-w2.txt` · chunks from `_raw/reddit/read-w2/chunks.jsonl` (line "PR31" in `_raw/reddit/read-w2/assignments.txt`). Window: posts 2026-07-06 → 2026-07-09.

## Counts

| chunk | units | read in full | excluded | units quoted | quotes |
|---|---|---|---|---|---|
| read-w2-keep_core-034 | 15 | 15 | 1 | 14 | 31 |
| read-w2-keep_core-035 | 16 | 16 | 3 | 11 | 30 |
| read-w2-keep_core-036 | 12 | 12 | 1 | 11 | 22 |
| read-w2-keep_core-037 | 22 | 22 | 1 | 19 | 34 |
| read-w2-keep_core-038 | 19 | 19 | 3 | 11 | 27 |
| read-w2-keep_core-039 | 21 | 21 | 3 | 15 | 29 |
| read-w2-keep_core-040 | 19 | 19 | 2 | 11 | 22 |
| read-w2-keep_core-041 | 16 | 16 | 1 | 15 | 35 |
| **total** | **140** | **140** | **15** | **107** | **230** |

Read with no quote: 18 units (listed below). Restricted quotes: 25 (listed in `synthesis/reader-notes-pr31.md`). Verify: `python3 -I _tools/verify_quotes.py voice/reddit-pr31.jsonl` → 230 quotes, 0 failed. Nothing unread.

## Excluded (not quoted; unit ids, neutral reason)

- `pregnant-1uop47m` — partner substance use and relationship conflict
- `BabyBumps-1upaov4` — severe mental-health post
- `BabyBumps-1upccmc` — severe mental-health post
- `pregnant-1upcpde` — crisis wording and relationship distress
- `Mommit-1upeld1` — acute anxiety post with possible harm wording
- `BabyBumps-1upxxrs` — infant safe-sleep / child-safety concern
- `pregnant-1upy1yp` — serious screening finding
- `NewParents-1uq8udg` — severe mental-health and exhaustion post
- `pregnant-1uq9594` — screening results and monitoring concerns
- `Mommit-1uqa016` — acute postpartum medical condition and medication
- `Mommit-1uqcckg` — partner controlling behaviour
- `pregnant-1uqdo2p` — substance use (nicotine withdrawal)
- `BabyBumps-1uqrp46` — acute medical illness in pregnancy
- `pregnant-1uqsvj8` — acute medical emergency (ER visits)
- `pregnant-1ur8t3b` — severe mental-health post (medication)

## Read in full, no quote

- `pregnant-1upr9g8` — read, no quote: same author as PregnancyUK-1upaazp (repeat author, medical decision)
- `pregnant-1upy2f2` — read, no quote: physician PSA giving medication advice (would need fact-checking)
- `BabyBumps-1upzk8z` — read, no quote: neighbour behaviour, off-theme
- `Mommit-1upafdo` — read, no quote: 7-week-old resemblance, off-niche
- `PregnancyUK-1upaazp` — read, no quote: medical induction decision (platelets); same author reposted as pregnant-1upr9g8
- `PregnancyUK-1upmxrd` — read, no quote: screening-test fear centred on a condition name
- `beyondthebump-1upztpw` — read, no quote: post after a difficult birth, mental-health centred, nothing usable unrestricted
- `beyondthebumpUK-1uq0v1q` — read, no quote: 5-week-old latch question, off-niche
- `pregnant-1uq3jks` — read, no quote: travel infection worry, medical and mental-health centred
- `FirstTimeMom-1uqbzn4` — read, no quote: early bleeding worry, medical
- `NewParents-1uqci6w` — read, no quote: preterm baby feeding after NICU, off-niche (jargon noted: paladai/sangu)
- `NewParents-1uqdu5h` — read, no quote: 5-week-old bonding feelings, off-niche
- `pregnant-1uqk8y2` — read, no quote: thyroid results, medical
- `pregnant-1uqnv78` — read, no quote: treatment for a blood result, medical
- `BabyBumps-1uqoyh2` — read, no quote: early bleeding and loss-fear
- `daddit-1uqqig5` — read, no quote: crosspost of pregnant-1uqpxsy by the same author
- `pregnant-1uqrgya` — read, no quote: crosspost of PregnancyUK-1uqr8zs (identical text, same author)
- `PregnancyUK-1uqvkd6` — read, no quote: blood results and supplements, medical

## Crossposts and repeat authors

- `PregnancyUK-1uqr8zs` = `pregnant-1uqrgya` (identical text); quoted once (pb31-0186, pb31-0187).
- `pregnant-1uqpxsy` = `daddit-1uqqig5` (same author, same text); quoted once (pb31-0181).
- `PregnancyUK-1upaazp` and `pregnant-1upr9g8`: same author, same medical question; neither quoted.

No seeded posts found (no "Nurava"/"@nuravaa", no vitamin pushing); no post read as AI-written or rage-bait.
