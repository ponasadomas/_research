# Reddit reading ledger — MR07 (sleep-mother, wave 3)

Reader MR07 · id prefix `sm07` · voice file `voice/reddit-mr07.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-sleep-mother-reader-w3.txt` · read 2026-10-25.
Window: posts 2026-04-01 → 2026-06-24 (wave 3). Corpus: `_raw/reddit/read-w3/chunks.jsonl` (frozen; not rebuilt). Chunks from the `MR07` line of `_raw/reddit/read-w3/assignments.txt` (148 units).

## Chunks assigned

| chunk | units | read in full | excluded | read, no quote | quotes |
|---|---|---|---|---|---|
| read-w3-keep_purchase-001 | 22 | 22 | 2 | 0 | 58 |
| read-w3-keep_purchase-002 | 14 | 14 | 1 | 0 | 45 |
| read-w3-keep_success-001 | 10 | 10 | 0 | 0 | 30 |
| read-w3-keep_success-002 | 5 | 5 | 1 | 0 | 12 |
| read-w3-keep_otherside-001 | 5 | 5 | 0 | 0 | 27 |
| read-w3-keep_otherside-002 | 7 | 7 | 1 | 0 | 29 |
| read-w3-keep_otherside-003 | 5 | 5 | 0 | 0 | 29 |
| read-w3-keep_otherside-004 | 12 | 12 | 1 | 1 | 33 |
| read-w3-keep_otherside-005 | 12 | 12 | 0 | 0 | 47 |
| read-w3-keep_otherside-006 | 12 | 12 | 2 | 0 | 28 |
| read-w3-keep_core-001 | 11 | 11 | 0 | 1 | 35 |
| read-w3-keep_core-002 | 16 | 16 | 2 | 1 | 37 |
| read-w3-keep_core-003 | 17 | 17 | 0 | 0 | 50 |
| **total** | **148** | **148** | **10** | **3** | **460** |

135 units quoted. 36 of the 460 quotes are restricted, judged quote by quote (list in `synthesis/reader-notes-mr07.md`). Verify: `python3 -I _tools/verify_quotes.py voice/reddit-mr07.jsonl` → 460 quotes, 0 failed. Ids sm07-0001 … sm07-0460, unique.

## Units excluded (not quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1sld7p7.txt` | safe-sleep worry centres the post |
| `../_shared/_raw/reddit-2026/units/BabyBumps-1tl5h3z.txt` | possible medical emergency and monitor alarms centre the post |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1tt9sn2.txt` | crisis wording in the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1tv25sx.txt` | crisis wording in a looking-back post |
| `../_shared/_raw/reddit-2026/units/NewParents-1t7zmq8.txt` | safe-sleep incident centres the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1tmrx41.txt` | acute distress with the newborn centres the post |
| `../_shared/_raw/reddit-2026/units/daddit-1ub87o5.txt` | safe-sleep incident centres the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1ue7uc2.txt` | newborn emergency and safe-sleep fears centre the post |
| `../_shared/_raw/reddit-2026/units/BabyBumps-1sc1wgk.txt` | acute illness and medication centre the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1scclfx.txt` | post centred on a named condition, its treatment and intrusive thoughts |

## Read in full, no quote

- `../_shared/_raw/reddit-2026/units/daddit-1tq571a.txt` — joke thread about sleep-deprived mistakes; no material on anyone's sleep.
- `../_shared/_raw/reddit-2026/units/pregnant-1s9cf2b.txt` — post about the couple's sexual relationship, much of it pasted AI text; sleep only incidental.
- `../_shared/_raw/reddit-2026/units/beyondthebump-1sdksnt.txt` — duplicate cross-post of Mommit-1sdkonw by the same author.

## Handling notes (units quoted with care)

- `daddit-1s9r7ep` (purchase-001): AI-polished post, brands named: possible_promo.
- `pregnant-1sp59ar` (purchase-001): product pitch style: possible_promo.
- `NewParents-1szpvsc` (purchase-001): restricted only.
- `beyondthebump-1tvfjkf` (success-002): restricted only; post centred on medical conditions.
- `NewParents-1sck46o` (otherside-001): poster's replies name a condition; not quoted.
- `beyondthebump-1sjwwc8` (otherside-001): AI-written from the father's narration.
- `NewParents-1sk665j` (otherside-001): physical incident and abuse history in replies; not quoted.
- `beyondthebump-1tep0ja` (otherside-003): replies name conditions and medication; not quoted.
- `NewParents-1tqrzh3` (otherside-004): likely same author as NewParents-1spjxi9; not independent.
- `pregnant-1tstj1o` (otherside-005): a reply holds a past crisis reference; not quoted.
- `postpartumprogress-1twsthz` (otherside-005): medical detail not quoted.
- `daddit-1u14ufa` (otherside-005): crafted humour style like daddit-1uelrjb: possible_promo.
- `Mommit-1udfcwe` (otherside-006): a baby-safety incident in the post is not quoted.
- `daddit-1uelrjb` (otherside-006): templated humour style: possible_promo.
- `Mommit-1sa3jlg` (core-001): medication and condition detail not quoted.
- `beyondthebump-1sa80k5` (core-001): condition detail not quoted.
- `beyondthebumpUK-1sa83vn` (core-001): medication request not quoted.
- `beyondthebump-1sagsjh` (core-001): medication detail not quoted.
- `FirstTimeMom-1sc312r` (core-002): restricted only; bed-sharing centres the thread.
- `sahm-1scwbsg` (core-002): savings figures are not sleep spend; not quoted.
- `NewParents-1sdksf5` (core-002): birth trauma detail not quoted.
- `FirstTimeMom-1sdz5rl` (core-003): condition names not quoted.
- `beyondthebump-1sehia6` (core-003): restricted only.
- `NewParents-1sf4ldf` (core-003): safe-sleep wording not quoted.
- `sleeptrain-1sfamtk` (core-003): medication not quoted.
- `beyondthebump-1sflo8z` (core-003): medication not quoted.
- `sleeptrain-1sgx8fh` (core-003): bed-sharing detail not quoted.
- `beyondthebump-1sh0kci` (core-003): restricted only; safe-sleep fear centres the post.

## Not independent

- `possible_promo`: sm07-0001–0003 (AI-polished post naming several brands), sm07-0006 (product-pitch post), sm07-0308–0310 and sm07-0337–0338 (two daddit humour posts in a crafted, engagement style). Do not count them as independent voices.
- Same author twice: `NewParents-1spjxi9` (sm07-0173–0179) and `NewParents-1tqrzh3` (sm07-0257–0261), the same father, programmer, son of 8 then 10 months.
- Cross-post: `Mommit-1sdkonw` quoted once (sm07-0407); `beyondthebump-1sdksnt` is the same post and is not quoted.

## Unfinished

None. Every unit in the 13 chunks was read in full.
