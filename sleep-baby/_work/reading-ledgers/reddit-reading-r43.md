# Reddit reading ledger — R43 (wave 3, sleep-baby)

Reader R43 · id prefix `sb43` · voice file `voice/reddit-r43.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 12: `read-w3-keep_otherside-001` … `-004` (16/17/17/21 units) and `read-w3-keep_success-001` … `-008` (10/1/14/12/12/16/14/4), from `_raw/reddit/read-w3/chunks.jsonl` |
| Units in those chunks | 154 (posts dated 2026-04-01 → 2026-06-24; OP replies to 2026-10-07) |
| Units read in full | 154 (including `sleeptrain-1shxa07`, 805 lines: the poster's 104 replies over six months) |
| Units excluded entirely | 6 (5 for content or age, 1 duplicate cross-post) |
| Units quoted | 148 |
| Quotes written | 585 (ids sb43-0001 … sb43-0585, unique) |
| Restricted quotes | 6 (listed in `synthesis/reader-notes-r43.md`) |
| Possible seeded quotes (`possible_promo`, never count) | 7 |
| verify_quotes.py | 585 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R43/units.tsv`. Short-form sources `scratchpad/R43/q01–q11.tsv`, built into the voice file by `scratchpad/R43/build.py` (it takes url and date from the unit file).

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/Parenting-1semhaj.txt` | the child in question is 3.5 years (over 36 months) |
| `../_shared/_raw/reddit-2026/units/Parenting-1smqzo3.txt` | the child in question is 3.5 years (over 36 months) |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tpjiez.txt` | the success described is at age 4 (over 36 months) |
| `../_shared/_raw/reddit-2026/units/Mommit-1sm0fdy.txt` | domestic-conflict incident around the baby and a third party's crisis |
| `../_shared/_raw/reddit-2026/units/NewParents-1t6rvss.txt` | parent describes shouting at the child; postpartum crisis wording |
| `../_shared/_raw/reddit-2026/units/workingmoms-1stp3ni.txt` | duplicate cross-post of `Mommit-1stp505` (same author, same text); quoted once from Mommit |

## Units read and quoted, with passages left out (neutral reasons)

| unit | not quoted |
|---|---|
| `NewParents-1sck46o` | the poster's replies (partner's mental-health diagnosis and aggression wording); the post is quoted |
| `sleeptrain-1sfx554` | dozing while driving (road safety) and crisis wording |
| `Parenting-1si3qrh` | bedsharing-with-pillows safety passage |
| `AttachmentParenting-1skb4zd` | chest-sleeping and bedsharing details |
| `ScienceBasedParenting-1sjufmg`, `beyondthebump-1so1tbv`, `NewParents-1st7a4w`, `NewParents-1swauh1`, `beyondthebump-1ueh4pk`, `sleeptrain-1u2acev`, `sleeptrain-1tqs5rd`, `sleeptrain-1te5ljk`, `NewParents-1tkf7ay`, `NewParents-1tv25sx`, `beyondthebump-1san0bg` | medication, diagnoses, tests, ER visit |
| `Parenting-1sz4qz0` | the claim that crying harms the child (README) |
| `NewParents-1sczq7s`, `sleeptrain-1si77xa`, `sleeptrain-1sj6e2l`, `sleeptrain-1sq3z2a`, `sleeptrain-1sz9qk0`, `sleeptrain-1taa41t`, `sleeptrain-1tfqikg`, `NewParents-1u7nazo`, `NewParents-1tv25sx` | named postpartum conditions, crisis or intrusive-thought wording |
| `sleeptrain-1sgptiu`, `sleeptrain-1srbxf1`, `sleeptrain-1taa41t`, `sleeptrain-1tg4w4q`, `sleeptrain-1thzyf6`, `sleeptrain-1u2acev` | rolling, belly sleeping, swaddle or sleep-suit swaps near rolling (the post body of `1thzyf6` is about belly sleeping; only two replies are quoted) |
| `Parenting-1sdlg73`, `sleeptrain-1spgh82`, `toddlers-1sylj38`, `beyondthebump-1t0zt63`, `beyondthebump-1u0wkw2`, `sleeptrain-1udz93p`, `sleeptrain-1u28yb8` | bedsharing, sidecar-cot and cosleeping details |
| `sleeptrain-1t81zhv`, `NewParents-1sczq7s`, `Mommit-1uaxyam` | breathing checks, smothering fear, dozing with the baby in a chair |
| `sleeptrain-1sfnsht`, `sleeptrain-1spgh82` | adult injury or surgery |
| `sleeptrain-1si77xa` | the consultant's personal name (business noted in reader notes) |

## Seeding flags

`sleeptrain-1sxyry7` (2026-04-28) and `sleeptrain-1tl3sae` (2026-05-23) tell the same story in near-identical words under different authors: nearly 6 months old, waking 17 or 18 times, "1 hour 28 minutes" or "1 hour and 23 minutes" of sleep, the Ferber book read in one day, cries of 3/5/10/10/4 minutes, gaming before bed, found asleep on the floor. All 7 quotes from them carry `possible_promo` (sb43-0370…0374, sb43-0479, sb43-0480). Seeding candidate, not tagged: `sleeptrain-1si77xa`, a CIO/Ferber success story whose poster, when asked, names an online consultancy found on Facebook and praises its flexibility (sb43-0289 … -0294); the brief warns of "the same consultant story under different authors". No second copy in my chunks. `sleeptrain-1sf2oxi` is a parent calling a Taking Cara Babies Facebook thread a fake testimonial post (sb43-0046, a sceptic, not seeded).

## What has and hasn't been read

Every unit in the 12 chunks was read in full. Nothing unread.
