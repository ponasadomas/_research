# Reddit reading ledger — R40 (wave 2, sleep-baby)

Reader R40 · id prefix `sb40` · voice file `voice/reddit-r40.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w2.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25. Final wave-2 assignment.

## Counts

| step | count |
|---|---|
| Chunks assigned | 10 (`read-w2-keep_core-132` … `read-w2-keep_core-141`, from `_raw/reddit/read-w2/chunks.jsonl`) |
| Units in those chunks | 151 (13/15/20/20/15/17/11/19/13/8; posts dated 2026-08-20 → 2026-08-24; OP replies to 2026-09-13) |
| Units read in full | 151 |
| Units excluded entirely | 14 (10 for content or age, 4 duplicate cross-posts) |
| Units quoted | 137 |
| Quotes written | 388 (ids sb40-0001 … sb40-0388, unique) |
| Restricted quotes | 9 (listed in `synthesis/reader-notes-r40.md`) |
| verify_quotes.py | 388 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R40/units.txt`. Short-form quote sources: `scratchpad/R40/q01–q16.jsonl`, built by `scratchpad/R40/build.py`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1vu3hvg.txt` | infant-death fear and safe-sleep (clothing, blanket) details run through the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1vujwpy.txt` | safe-sleep incident (newborn wedged in bassinet) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1vue535.txt` | safe-sleep detail (prone sleeping, limbs caught in cot rails) is the whole post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1vufbue.txt` | the ask is about bedsharing |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1vv89bg.txt` | safe-sleep detail (rolling to and sleeping on the belly) is the whole post |
| `../_shared/_raw/reddit-2026/units/NewParents-1vxg58y.txt` | safe-sleep detail (rolling to the stomach) is the whole post |
| `../_shared/_raw/reddit-2026/units/NewParents-1vvjhvn.txt` | worry about settling with vigorous motion (physical-force line) |
| `../_shared/_raw/reddit-2026/units/NewParents-1vwp85d.txt` | medical illness and bedsharing throughout; no quotable sleep line without them |
| `../_shared/_raw/reddit-2026/units/NewParents-1vxf6dr.txt` | breastfeeding and biting, no sleep content; mental-health wording in replies |
| `../_shared/_raw/reddit-2026/units/Parenting-1vtl8a1.txt` | child 3.5 years (out of scope); also verbal harshness |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1vvfm7s.txt` | child past 36 months (turned 3 "a couple months back") |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1vvgoon.txt` | duplicate cross-post of NewParents-1vvgf0o (quoted there) |
| `../_shared/_raw/reddit-2026/units/Mommit-1vvycxh.txt` | duplicate cross-post of NewParents-1vuxzk0 (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1vvyfb6.txt` | duplicate cross-post of NewParents-1vuxzk0 (quoted there) |

## Units read, passages left out (neutral reasons)

Quotes were taken from the rest of each unit.

| unit | left out |
|---|---|
| daddit-1vtfcx3 | mental-health crisis wording, losing temper, medication (reply p4sqwj0), anxiety lines |
| daddit-1vum3r4 | mental-health and medication lines (post and replies p52ijvr, p528ebj second sentence) |
| beyondthebump-1vtsrtl | therapy, medication, suffocation fear, mental-health wording |
| beyondthebump-1vtht1m, toddlers-1vvf9wu, sleeptrain-1vw4j9j, sleeptrain-1vx0lyf, sleeptrain-1vx5art, sleeptrain-1vvyx3n, sleeptrain-1vvrakc | medical conditions, tests, medication |
| NewParents-1vtfw3m, toddlers-1vu1ppo, sleeptrain-1vvj8vd, NewParents-1vuxzk0, sleeptrain-1vuyyqc, AttachmentParenting-1vtgoff, AttachmentParenting-1vvlcub | medication for pain/teething |
| NewParents-1vwvqkm | infant-death fear (reply p5lypr4), prematurity/reflux details |
| Parenting-1vx7xwl | breathing checks, anxiety and mental-health wording |
| Parenting-1vvlw15 | rage at night |
| Parenting-1vwyqyu | named diagnoses (reply p5l3p0q) |
| Mommit-1vx9wz6 | birth trauma and mental-health passages |
| Mommit-1vx9xaq | allergy, anxiety, bedsharing |
| sleeptrain-1vxajul | infant-death risk, bedsharing set-up, named illness |
| beyondthebumpUK-1vwyyhg | fear of dropping or injuring the baby |
| sleeptrain-1vxdzp1 | colic and day-time safety wording |
| beyondthebump-1vw8gyg | antique rocking crib safety remark |
| NewParents-1vtkgqq | prone-sleep question (reply p4wxzo7) |
| sleeptrain-1vwotjj, sleeptrain-1vx233o, sleeptrain-1vwh1xu, sleeptrain-1vx0bld, sleeptrain-1vus2xh, sleeptrain-1vu4c6n, beyondthebumpUK-1vu81p6, NewParents-1vv9n1o, sleeptrain-1vw1guq, sleeptrain-1vvmwem, toddlers-1vvq22b, sleeptrain-1vx4eyc, sleeptrain-1vwm9tg, sleeptrain-1vxd6jr, AttachmentParenting-1vtj1g0 | bedsharing and chest-sleeping sentences |
| FirstTimeMom-1vucqn, toddlers-1vvbgai, beyondthebumpUK-1vxesuq | bassinet/crib limits and sleepwear safety details (the one sleepwear quote is restricted) |

## Duplicates and same-author pairs (both read)

- NewParents-1vvd4m2 = beyondthebump-1vvdn45 (quoted the first; only the OP's unique reply from the second).
- sleeptrain-1vw43rn = NewParents-1vwip65 (post quoted from the first; unique replies from the second).
- sleeptrain-1vx9i81 = AttachmentParenting-1vx9nv5 (one added line quoted from the second).
- AttachmentParenting-1vwai6x and sleeptrain-1vwkmm0: same family, different text and replies; both quoted.
- NewParents-1vvgf0o = beyondthebump-1vvgoon; NewParents-1vuxzk0 = Mommit-1vvycxh = beyondthebump-1vvyfb6 (excluded copies listed above).

## Unfinished

None. All 151 units read in full.
