# Reddit full reads — DR03 (development, read-w2: purchase, success, otherside, core 001–005)

Reader DR03, 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, tighter filter, posts dated 2026-06-25 → 2026-10-24). Voice file: `voice/reddit-dr03.jsonl` (ids dv03-0001 to dv03-0276). Builder and per-chunk record lists: `scratchpad/DR03/` (`build.py`, `rec_01.py` … `rec_08.py`; the voice file is generated from them, url/date/post_id/comment_id are taken from the unit text; `restricted.txt` lists restricted ids). Do not re-run the builder after anyone cites these ids unless the rec files are unchanged.

## Counts

| step | n |
|---|---|
| chunks assigned | 9 (read-w2-keep_purchase-001, -002, keep_success-001, keep_otherside-001, keep_core-001 … 005) |
| units in them | 116 |
| units read in full | 116 |
| units excluded (line not to cross) | 22 |
| units read, on file but nothing quotable on topic | 5 |
| duplicate reposts (read; body quoted from the first copy only) | 1 (Parenting-1upwkc6 = Mommit-1upwhrd; only its own edit and replies quoted) |
| units quoted | 89 |
| quotes written | 276 |
| of which restricted | 31 |

Verify: `python3 -I _tools/verify_quotes.py voice/reddit-dr03.jsonl` → `reddit-dr03.jsonl: 276 quotes, 0 failed`. Ids unique (checked from disk).

Per chunk (units / quoted units): purchase-001 19/15 · purchase-002 7/6 · success-001 5/5 · otherside-001 9/6 · core-001 13/9 · core-002 14/11 · core-003 15/13 · core-004 17/14 · core-005 17/10.

## Excluded units (not quoted)

| unit | reason |
|---|---|
| `beyondthebumpUK-1uizx8k` | centred on a suspected condition and paediatric referral; excluded |
| `NewParents-1veir62` | centred on head shape and a medical device; excluded |
| `NewParents-1ugd2rt` | centred on medical history and head-shape treatment; excluded |
| `beyondthebumpUK-1ujs5go` | centred on bath falls and a water-safety incident; excluded |
| `NewParents-1ul7zt2` | centred on a sudden loss of a motor skill under a doctor's watch; excluded |
| `Mommit-1uojnck` | centred on delays, medical history and therapies; excluded |
| `daddit-1up34sw` | centred on an early-intervention evaluation with delay results; excluded |
| `NewParents-1upkkiv` | centred on a therapy referral and a medical diagnosis; excluded |
| `NewParents-1uq9t89` | centred on motor delays and therapists' decisions; excluded |
| `toddlers-1usd6ah` | centred on a communication delay, therapy and diagnosis questions; excluded |
| `NewParents-1usv1yg` | safe-sleep question about rolling and swaddling; excluded |
| `NewParents-1utlmik` | centred on repeated head-bump injuries; excluded |
| `daddit-1uxhuvm` | centred on an early-intervention referral after a check-up; excluded |
| `NewParents-1uykt8x` | centred on a suspected condition and specialist visits; excluded |
| `toddlers-1uz5zsg` | centred on a developmental evaluation and behaviour at daycare; excluded |
| `beyondthebump-1uzyvam` | centred on medical and genetic worry and the parent's mental-health treatment; excluded |
| `NewParents-1v001hm` | centred on medical history and delay worry; excluded |
| `beyondthebump-1v2oaua` | centred on a feared neurological symptom; excluded |
| `NewParents-1v34t3n` | centred on therapy, surgery and a helmet; excluded |
| `toddlers-1utsjav` | centred on a speech evaluation; excluded |
| `toddlers-1v2cxlw` | centred on a suspected condition in a relative's child; excluded |
| `toddlers-1vgmn0n` | centred on a speech-therapy referral question, child over 24 months; excluded |

## Read, no quote

| unit | reason |
|---|---|
| `NewParents-1uh7z09` | shoe sizing for a cruising 14-month-old; off topic |
| `beyondthebump-1uzc9mr` | shoe-ordering mix-up; off topic |
| `beyondthebump-1vkvyqm` | gifted shoes for a pre-walker, no replies; nothing quotable |
| `beyondthebump-1uieydu` | one-paragraph anecdote about a 13-week-old after a nap; nothing on topic |
| `NewParents-1ume4vh` | feeding anecdote at 12 weeks; off topic |

## Restricted ids

dv03-0011, dv03-0013, dv03-0038, dv03-0046, dv03-0047, dv03-0048, dv03-0056, dv03-0071, dv03-0087, dv03-0088, dv03-0116, dv03-0167, dv03-0187, dv03-0189, dv03-0190, dv03-0194, dv03-0199, dv03-0220, dv03-0221, dv03-0222, dv03-0223, dv03-0235, dv03-0236, dv03-0237, dv03-0238, dv03-0239, dv03-0240, dv03-0242, dv03-0252, dv03-0268, dv03-0271
