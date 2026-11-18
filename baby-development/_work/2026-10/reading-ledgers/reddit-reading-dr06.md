# Reddit full reads — DR06 (development, read-w3: keep_core-006 – keep_core-011)

Reader DR06, 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md` via `../../_shared/_tools/prompt-development-reader-w3.txt`. Corpus: `_raw/reddit/read-w3/chunks.jsonl` (wave 3; posts dated 2026-05-17 → 2026-06-24 in these chunks, OP replies up to 2026-09-15). Voice file: `voice/reddit-dr06.jsonl` (ids dv06-0001 to dv06-0211). Builder and staged records: `scratchpad/DR06/` (`build.py` turns `drafts.jsonl` into the voice file; url, date, post_id and comment_id are read from the unit text; `units.tsv` lists the 86 units; `excl.txt` the excluded units).

## Counts

| step | n |
|---|---|
| chunks assigned | 6 |
| units in them | 86 |
| units read in full | 86 |
| units excluded (line not to cross) | 11 |
| units read, nothing quoted (delay-assessment only) | 1 |
| units quoted | 74 |
| quotes written | 211 |
| of which restricted (see reader notes) | 25 |
| of which flagged `possible_promo` | 0 (no app-builder posts in these chunks) |

Verify: `python3 -I _tools/verify_quotes.py voice/reddit-dr06.jsonl` → `reddit-dr06.jsonl: 211 quotes, 0 failed`. Ids unique (211 of 211).

## Per chunk

| chunk | units | read in full | quoted | excluded or no quote | quotes |
|---|---|---|---|---|---|
| read-w3-keep_core-006 | 19 | 19 | 16 | 3 | 48 |
| read-w3-keep_core-007 | 13 | 13 | 13 | 0 | 36 |
| read-w3-keep_core-008 | 13 | 13 | 11 | 2 | 29 |
| read-w3-keep_core-009 | 17 | 17 | 14 | 3 | 36 |
| read-w3-keep_core-010 | 19 | 19 | 16 | 3 | 47 |
| read-w3-keep_core-011 | 5 | 5 | 4 | 1 | 15 |

## Excluded units (not quoted)

| unit | reason |
|---|---|
| `NewParents-1th1h1i` | centred on a medical condition and its treatment |
| `toddlers-1tkex9t` | centred on a diagnosis and therapy referrals |
| `beyondthebump-1tuo158` | centred on a child's therapy and conditions |
| `NewParents-1tx3k34` | centred on a premature baby's therapy referral and medical tests |
| `toddlers-1u3mzg6` | centred on a possible diagnosis and therapy referral |
| `Mommit-1u4e459` | centred on a medical history and an early-intervention referral after a clinician's finding |
| `toddlers-1u55kub` | centred on fear of a diagnosis and specialist appointments |
| `NewParents-1u5fyp3` | contains a mental-health crisis signal and diagnoses |
| `beyondthebump-1u7lnjh` | centred on therapy and fear of a diagnosis |
| `NewParents-1u7vii0` | same author and text as `1u7lnjh` (crosspost); same reason |
| `Mommit-1ue5ajf` | centred on a developmental-clinic evaluation and therapy referral after a medical history |

Read in full, nothing quoted: `toddlers-1tjvzoj` (speech-assessment question; every usable line is delay worry already well covered by restricted quotes elsewhere).

Units quoted around medical side-detail (quote-level care, no medical words quoted): `beyondthebump-1ttxang`, `beyondthebump-1tv28uu`, `beyondthebump-1tv484w`, `NewParents-1u5a9av`, `NewParents-1uaad37`, `Parenting-1uadc72` (physiotherapy in progress; kept because the post is about the baby's frustration on the floor, unlike `1tuo158`, which is about the conditions themselves; its blame-the-toys quote is restricted), `Mommit-1to2gxt`, `NewParents-1tsiofa`, `FirstTimeMom-1u334xt`. Safe-sleep practice mentioned in `1tv28uu` and `1ud3veu` is not quoted.

## What has and hasn't been read

All 86 units in the six assigned chunks were read in full, post and every OP reply. Nothing unread.

## How to continue

Do not re-run DR06 or append to `voice/reddit-dr06.jsonl`. To change a record, edit `scratchpad/DR06/drafts.jsonl` and rerun `python3 -I scratchpad/DR06/build.py` (ids are assigned in draft order; changing the order renumbers them), then verify.
