# Reddit full reads — reader TR03 (2026-10-25)

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1/chunks.jsonl`. Voice file: `voice/reddit-tr03.jsonl` (ids `tb03-0001` to `tb03-0306`). Notes: `synthesis/reader-notes-tr03.md`. Scratch: `scratchpad/TR03/` (unit list, per-chunk batches, `ledger.tsv`).

Verify: `python3 -I _tools/verify_quotes.py voice/reddit-tr03.jsonl` → 306 quotes, 0 failed. Ids unique (306/306).

## Chunks assigned

| chunk | units | units with quotes | quotes |
|---|---|---|---|
| read-v1-keep_core-007 | 14 | 13 | 37 |
| read-v1-keep_core-008 | 9 | 9 | 41 |
| read-v1-keep_core-009 | 14 | 14 | 40 |
| read-v1-keep_core-010 | 14 | 12 | 32 |
| read-v1-keep_core-011 | 16 | 15 | 42 |
| read-v1-keep_core-012 | 17 | 16 | 37 |
| read-v1-keep_core-013 | 18 | 17 | 36 |
| read-v1-keep_core-014 | 16 | 15 | 41 |
| **total** | **118** | **111** | **306** |

Units read in full: **118 of 118** (post and every original-poster reply in each unit). Nothing left unread.

## Units excluded (4, nothing quoted)

| unit | reason |
|---|---|
| toddlers-1w2xl9d | parent describes physical force toward the child; also asks about a developmental diagnosis |
| toddlers-1w4zt1g | centred on a medical cause; medication and specialist details throughout |
| toddlers-1w53tmc | parent describes physical punishment of the child |
| daddit-1w5ki1d | parent describes physically restraining the child and holding a door shut; also a diagnosis question |

## Units read, no quote (3 cross-posts)

| unit | reason |
|---|---|
| pottytraining-1w6i8rr | same text as toddlers-1w6hkw8 (quoted there) |
| pottytraining-1w7k0lc | same text as toddlers-1w7jzth (quoted there) |
| toddlers-1w86h0j | same text as pottytraining-1w86gaq (quoted there) |

Near-duplicate: toddlers-1w7mr94 is a longer rewrite of toddlers-1w62pwc by the same parent; one non-overlapping line quoted from it.

## Restricted units (diagnosis context; quoted only as the parent's fear or state)

toddlers-1w3wp5z, Mommit-1w4tbac, Mommit-1w5ax16, toddlers-1w5dxqh, Mommit-1w5e91p, daddit-1w6z3o3, pottytraining-1w7a6kg, toddlers-1w7mr94. Ids listed in the notes under "Restricted ids".

## Partial quoting (unit quoted, passages left out)

| unit | not quoted |
|---|---|
| toddlers-1w2tubz | parent's own medication comments |
| pottytraining-1w3s65h, Parenting-1w3ys2g, pottytraining-1w4hs1o, pottytraining-1w5lvbr, toddlers-1w7jzth | laxative, suppository, enema, scan or hospital details |
| Parenting-1w3x4qa | commenters' suggestion to hit the child (rejected by OP); diet details |
| toddlers-1w4sc66, toddlers-1w4ykhe, Mommit-1w84d6f, daddit-1w6q4ou | lines about yelling or a harsh tone toward the child |
| toddlers-1w8jf4x | line where the parent labels the child to her face |
| AttachmentParenting-1w4h0de, Mommit-1w5p27u, Mommit-1w4qcc6, Mommit-1w79yt1, Parenting-1w8aobo, NewParents-1w857bz, pottytraining-1w7p65x | birth, bereavement, illness, medication or medical-history details |
| toddlers-1w4b8y5, daddit-1w6z3o3, toddlers-1w5zxiz | parent's own diagnosis or medical procedure |
| NewParents-1w7agpl | line about dark thoughts |

## How to continue

Nothing unread in this assignment. Do not re-run TR03 (it appends to `voice/reddit-tr03.jsonl`); the next id would be `tb03-0307`.
