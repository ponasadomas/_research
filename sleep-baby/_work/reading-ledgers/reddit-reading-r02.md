# Reddit full reads, reader R02 (2026-10-25)

Brief: `../../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (never rebuilt). Voice file: `voice/reddit-r02.jsonl` (ids `sb02-0001` to `sb02-0294`). Notes: `synthesis/reader-notes-r02.md`. Staging scripts that build the voice file: `scratchpad/R02/` (`q_*.py` plus `assemble.py`).

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_success-001` to `-006`, `read-v1a-keep_otherside-001`, `-002`) |
| units in those chunks | 73 (success 46, other side 27) |
| units read in full (post + every OP reply in the unit) | 73 |
| units excluded, no quotes | 5 (listed below) |
| units quoted | 68 |
| quotes written | 294 |
| `verify_quotes.py` | 294 quotes, 0 failed |

Counts are counts of quotes chosen, not of people. `sb02-0294` (from `sleeptrain-1whwp0k`) was added last, after the other-side chunks, so earlier ids did not move.

## Units read with no quotes taken (all read in full)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/ScienceBasedParenting-1vy45nm.txt` | Hypothetical question with no baby of sleep-training age yet; the substance is a claim about crying and stress hormones (README line not to cross). OP replies are thank-yous only. |
| `../_shared/_raw/reddit-2026/units/workingmoms-1vzdit5.txt` | Word-for-word cross-post of `NewParents-1vzdi5f` (quoted there). |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1w30dhf.txt` | Word-for-word cross-post of `NewParents-1w206ru` / `Mommit-1w30cgg` (quoted there). |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wddvir.txt` | Near-identical repost of `sleeptrain-1w6nvtp` (same story and wording, minor edits) (quoted there). |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wkuxjp.txt` | Word-for-word cross-post of `FirstTimeMom-1wkuuzc` (quoted there). |

Cross-post note: `Mommit-1w30cgg` is the second copy of the no-cry nap post; it got one quote, a paragraph missing from the `NewParents-1w206ru` copy.

## Units by chunk (quotes per unit)

- **keep_success-001** (12): NewParents-1vxk4e7 2 · sleeptrain-1vxv9xx 9 · sleeptrain-1w0o698 2 · AttachmentParenting-1w0tmdg 8 · sleeptrain-1w0uh3w 5 · NewParents-1w206ru 2 · NewParents-1w2hzuc 4 · Mommit-1w30cgg 1 · beyondthebump-1w30dhf 0 · NewParents-1w3kiyv 3 · NewParents-1w422ha 2 · sleeptrain-1w5b8f3 5
- **keep_success-002** (8): sleeptrain-1w6nvtp 7 · NewParents-1w92xtg 4 · daddit-1w95ils 2 · Parenting-1wbi9zt 8 · sleeptrain-1wc92tj 2 · sleeptrain-1wctb57 2 · sleeptrain-1wddvir 0 · sleeptrain-1wdki0l 7
- **keep_success-003** (13): NewParents-1wf70kk 5 · NewParents-1wgiwk0 1 · toddlers-1wgmb5z 2 · sleeptrain-1wgmnmb 6 · sleeptrain-1whaf09 1 · Parenting-1whwgta 2 · sleeptrain-1whwp0k 9 · sleeptrain-1wike61 4 · sleeptrain-1wj3sul 4 · NewParents-1wke9e8 2 · sleeptrain-1wkodvn 1 · FirstTimeMom-1wkuuzc 3 · beyondthebump-1wkuxjp 0
- **keep_success-004** (6): sleeptrain-1wkywud 5 · AttachmentParenting-1wkzvfn 10 · sleeptrain-1wlyewm 1 · sleeptrain-1wn1w02 2 · Mommit-1wnuui1 6 · sleeptrain-1wogybv 8
- **keep_success-005** (3): sleeptrain-1woksq0 7 · NewParents-1wp4zec 16 · daddit-1wp7wqh 4
- **keep_success-006** (4): daddit-1wr8zks 13 · sleeptrain-1wybvq0 8 · sleeptrain-1wywa5x 2 · sleeptrain-1wzplmv 6
- **keep_otherside-001** (13): Mommit-1vxp1ky 3 · ScienceBasedParenting-1vy45nm 0 · beyondthebumpUK-1vy8y3g 2 · Mommit-1vyuqld 4 · Mommit-1vza2rp 6 · NewParents-1vzdi5f 3 · workingmoms-1vzdit5 0 · beyondthebump-1vzhtuy 4 · toddlers-1w082cq 1 · Mommit-1w0efku 3 · sleeptrain-1w0ihfa 4 · NewParents-1w0xwkx 5 · NewParents-1w16xux 6
- **keep_otherside-002** (14): beyondthebump-1w1cgbb 5 · Mommit-1w23z99 5 · FirstTimeMom-1w23zxf 4 · sleeptrain-1w29wi1 2 · NewParents-1w2y21r 4 · sleeptrain-1w3am1s 2 · AttachmentParenting-1w3uuvq 5 · sleeptrain-1w3y5rv 1 · beyondthebump-1w450b2 6 · NewParents-1w4lynf 2 · Mommit-1w4sd22 4 · sleeptrain-1w57714 3 · sleeptrain-1w5bjnx 4 · NewParents-1w5euyp 3

## What was not read

Nothing in the assigned chunks is unread. Units only hold the original poster's own replies; other commenters' words appear only where the poster quotes or reports them (tagged `others_said`, speaker stays the author).

## Passages deliberately not quoted

Medication names and doses, teething remedies, iron/ferritin details (trimmed out of sb02-0183), cosleeping product links and the "safe sleep seven", and claims that crying harms or does not harm babies (including cortisol and "nervous system" claims) were left out or quoted only as the parent's own feeling, per the README.
