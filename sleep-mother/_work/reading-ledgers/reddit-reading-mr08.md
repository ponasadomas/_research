# Reddit reading ledger — MR08 (sleep-mother, wave 3)

Reader MR08 · id prefix `sm08` · voice file `voice/reddit-mr08.jsonl` · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-sleep-mother-reader-w3.txt` · read 2026-10-25.
Window: posts 2026-04-10 → 2026-05-15 inside wave 3 (1 April – 24 June 2026). Corpus: `_raw/reddit/read-w3/chunks.jsonl` (frozen; not rebuilt). Assignment line `MR08` in `_raw/reddit/read-w3/assignments.txt` (149 units).

## Chunks assigned

| chunk | units | read in full | excluded | read, no quote | quotes |
|---|---|---|---|---|---|
| read-w3-keep_core-004 | 8 | 8 | 0 | 2 | 25 |
| read-w3-keep_core-005 | 14 | 14 | 1 | 1 | 46 |
| read-w3-keep_core-006 | 19 | 19 | 2 | 0 | 70 |
| read-w3-keep_core-007 | 15 | 15 | 2 | 0 | 50 |
| read-w3-keep_core-008 | 17 | 17 | 0 | 2 | 41 |
| read-w3-keep_core-009 | 20 | 20 | 1 | 0 | 55 |
| read-w3-keep_core-010 | 22 | 22 | 2 | 1 | 47 |
| read-w3-keep_core-011 | 16 | 16 | 1 | 0 | 39 |
| read-w3-keep_core-012 | 18 | 18 | 0 | 0 | 48 |
| **total** | **149** | **149** | **9** | **6** | **421** |

134 units quoted. 24 of the 421 quotes are restricted, judged quote by quote (list in `synthesis/reader-notes-mr08.md`). Verify: `python3 -I _tools/verify_quotes.py voice/reddit-mr08.jsonl` → 421 quotes, 0 failed. Ids sm08-0001 … sm08-0421, unique. Records are dated by the comment when quoted from a reply; two fall after 2026-05-15 (sm08-0406 2026-05-18, sm08-0189 2026-07-23).

## Units excluded (not quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sjiq9w.txt` | centred on named mental-health conditions and medication, with a self-harm reference |
| `../_shared/_raw/reddit-2026/units/NewParents-1sox5xq.txt` | safe-sleep incident |
| `../_shared/_raw/reddit-2026/units/NewParents-1sqjzhz.txt` | contains suicidal-thought wording |
| `../_shared/_raw/reddit-2026/units/BabyBumps-1ssi0k5.txt` | centred on named mental-health conditions and medication |
| `../_shared/_raw/reddit-2026/units/BabyBumps-1sto7db.txt` | intrusive thoughts and rough handling of the child |
| `../_shared/_raw/reddit-2026/units/Postpartum_Depression-1t3k3rp.txt` | centred on named conditions, hospital stay and medication |
| `../_shared/_raw/reddit-2026/units/NewParents-1t3ziwd.txt` | centred on accidental substance ingestion while caring for the baby |
| `../_shared/_raw/reddit-2026/units/workingmoms-1t67w5z.txt` | bed-sharing post describing rough physical handling of the toddler |
| `../_shared/_raw/reddit-2026/units/BabyBumps-1t8h3ec.txt` | centred on named mental-health conditions and medication |

## Read in full, no quote

- `../_shared/_raw/reddit-2026/units/sleeptrain-1si3mx5.txt` — possible_promo: near-identical wording to NewParents-1si55ll same night; not quoted
- `../_shared/_raw/reddit-2026/units/NewParents-1si55ll.txt` — possible_promo: near-identical wording to sleeptrain-1si3mx5; not quoted
- `../_shared/_raw/reddit-2026/units/NewParents-1slwy85.txt` — duplicate crosspost of beyondthebumpUK-1slwza8 by same author; quoted from the UK unit only
- `../_shared/_raw/reddit-2026/units/NewParents-1t0cnv9.txt` — triple crosspost of Mommit-1t0coxo by same author; not quoted separately
- `../_shared/_raw/reddit-2026/units/beyondthebump-1t0cqlx.txt` — triple crosspost of Mommit-1t0coxo by same author; not quoted separately
- `../_shared/_raw/reddit-2026/units/beyondthebump-1t4rbjc.txt` — identical crosspost of NewParents-1t4p7op; not quoted separately

## Possible promo / templated (tagged `possible_promo`, not independent)

- `../_shared/_raw/reddit-2026/units/Parenting-1sihgep.txt` — quoted once, tagged possible_promo (whole post in quote marks, asks for hacks)
- `../_shared/_raw/reddit-2026/units/pregnant-1so2ddd.txt` — quoted once, possible_promo (search-style title, supplement question)
- `../_shared/_raw/reddit-2026/units/NewParents-1srinrx.txt` — quoted, possible_promo (polished essay, no replies)
- `../_shared/_raw/reddit-2026/units/BabyBumps-1t1u0o4.txt` — quoted once, possible_promo (polished, health-site link)

## Every unit, in order

| chunk | unit | status | note |
|---|---|---|---|
| 004 | beyondthebumpUK-1shiaj3 | read | quoted (6 quotes) |
| 004 | sleeptrain-1si3mx5 | read | possible_promo: near-identical wording to NewParents-1si55ll same night; not quoted (0 quotes) |
| 004 | Parenting-1si3qrh | read | quoted (5 quotes) |
| 004 | NewParents-1si55ll | read | possible_promo: near-identical wording to sleeptrain-1si3mx5; not quoted (0 quotes) |
| 004 | Parenting-1sihgep | read | quoted once, tagged possible_promo (whole post in quote marks, asks for hacks) (1 quotes) |
| 004 | BabyBumps-1simt83 | read | quoted (2 quotes) |
| 004 | beyondthebump-1sizipp | read | quoted (bereavement/anxiety passages skipped) (7 quotes) |
| 004 | sleeptrain-1sjioaq | read | quoted (4 quotes) |
| 005 | beyondthebump-1sjiq9w | excluded | centred on named mental-health conditions and medication, with a self-harm reference; not quoted (0 quotes) |
| 005 | beyondthebump-1sjk4op | read | quoted (5 quotes) |
| 005 | pregnant-1sjnmte | read | quoted (illness/medication lines skipped) (2 quotes) |
| 005 | pregnant-1sjzs7m | read | quoted (medication/blood-pressure lines skipped) (3 quotes) |
| 005 | pregnant-1skcq7g | read | quoted (5 quotes) |
| 005 | NewParents-1slwy85 | read | duplicate crosspost of beyondthebumpUK-1slwza8 by same author; quoted from the UK unit only (0 quotes) |
| 005 | beyondthebumpUK-1slwza8 | read | quoted (5 quotes) |
| 005 | workingmoms-1sm8sn3 | read | quoted (3 quotes) |
| 005 | Mommit-1sm9p95 | read | quoted (bed-sharing lines skipped) (2 quotes) |
| 005 | beyondthebump-1smvs5r | read | quoted (2 quotes) |
| 005 | sleeptrain-1sn7svy | read | quoted (medical/bed-sharing item skipped) (11 quotes) |
| 005 | NewParents-1snek4o | read | quoted (1 quotes) |
| 005 | sleeptrain-1snu7mi | read | quoted (2 quotes) |
| 005 | pregnant-1snvbqi | read | quoted (5 quotes) |
| 006 | NewParents-1so0im5 | read | quoted (medication line skipped) (3 quotes) |
| 006 | beyondthebump-1so1tbv | read | quoted (one restricted: sleep aid; bed-sharing lines skipped) (10 quotes) |
| 006 | pregnant-1so2ddd | read | quoted once, possible_promo (search-style title, supplement question) (1 quotes) |
| 006 | beyondthebump-1so442s | read | quoted (2 quotes) |
| 006 | NewParents-1sot9se | read | quoted (2 quotes) |
| 006 | NewParents-1sox5xq | excluded | safe-sleep incident; not quoted (0 quotes) |
| 006 | pregnant-1spgsm0 | read | quoted (3 quotes) |
| 006 | PregnancyUK-1spol7x | read | quoted (2 quotes) |
| 006 | beyondthebump-1spz2sp | read | quoted (one restricted: supplement; sleep-aid and bed-sharing lines skipped) (10 quotes) |
| 006 | NewParents-1sqjzhz | excluded | contains suicidal-thought wording; not quoted (0 quotes) |
| 006 | NewParents-1sqlh40 | read | quoted (road-safety, bed-sharing, condition and loss lines skipped) (10 quotes) |
| 006 | NewParents-1sqmz33 | read | quoted (4 quotes) |
| 006 | pregnant-1sqx5x6 | read | quoted (one restricted: medication; identity passage skipped) (4 quotes) |
| 006 | PregnancyUK-1sqx7xp | read | quoted (3 quotes) |
| 006 | NewParents-1sr0jm1 | read | quoted (7 quotes) |
| 006 | NewParents-1srhd6u | read | quoted (2 quotes) |
| 006 | NewParents-1srinrx | read | quoted, possible_promo (polished essay, no replies) (2 quotes) |
| 006 | BabyBumps-1srlhdj | read | two clean lines quoted; medication-withdrawal content skipped (2 quotes) |
| 006 | beyondthebumpUK-1srtfg9 | read | clean lines quoted; condition and medication lines skipped (3 quotes) |
| 007 | beyondthebump-1sru1fw | read | quoted (2 quotes) |
| 007 | Parenting-1srxt5a | read | quoted (one restricted: safe-sleep detail) (6 quotes) |
| 007 | workingmoms-1ss1yof | read | quoted (condition line skipped) (3 quotes) |
| 007 | beyondthebump-1ss5jx3 | read | quoted (safe-sleep and loss lines skipped) (3 quotes) |
| 007 | BabyBumps-1ssi0k5 | excluded | centred on named mental-health conditions and medication; not quoted (0 quotes) |
| 007 | Mommit-1stbb9p | read | quoted (one restricted; child supplement list skipped) (5 quotes) |
| 007 | NewParents-1stbhdl | read | quoted (one restricted: bed-sharing; infant medical lines skipped) (5 quotes) |
| 007 | NewParents-1stnkb6 | read | quoted (condition line skipped); likely same author as NewParents-1sr0jm1 (4 quotes) |
| 007 | BabyBumps-1sto7db | excluded | intrusive thoughts and rough handling of the child; not quoted (0 quotes) |
| 007 | beyondthebump-1stqgnl | read | quoted (one restricted: bed-sharing) (11 quotes) |
| 007 | NewParents-1stvtvo | read | quoted (condition line skipped) (2 quotes) |
| 007 | BabyBumps-1su8oon | read | quoted (1 quotes) |
| 007 | NewParents-1suyhpq | read | quoted (4 quotes) |
| 007 | NewParents-1sv324y | read | two clean lines quoted; post centred on safe-sleep fear, rest skipped (2 quotes) |
| 007 | Parenting-1sw6b7g | read | bed-sharing post; one restricted quote and one clean quote (2 quotes) |
| 008 | beyondthebump-1swav1o | read | quoted (bed-sharing and infant medication lines skipped) (4 quotes) |
| 008 | pregnant-1swfvf8 | read | quoted (one restricted: sleep aid) (2 quotes) |
| 008 | BabyBumps-1swh124 | read | quoted (one restricted: named condition; supplement reply skipped) (3 quotes) |
| 008 | beyondthebump-1swn8fm | read | bed-sharing and infant reflux post; two clean lines quoted (2 quotes) |
| 008 | BabyBumps-1swyw29 | read | quoted (2 quotes) |
| 008 | NewParents-1sxnij6 | read | quoted once (1 quotes) |
| 008 | beyondthebump-1sxoz8y | read | quoted (4 quotes) |
| 008 | pregnant-1sxrj1g | read | quoted (symptom/hospital lines skipped) (2 quotes) |
| 008 | FirstTimeMom-1sycsyw | read | quoted (3 quotes) |
| 008 | beyondthebump-1syjct2 | read | quoted (medical test reply skipped) (3 quotes) |
| 008 | beyondthebumpUK-1synp70 | read | quoted (unsafe-surface line skipped) (3 quotes) |
| 008 | NewParents-1syq42j | read | quoted (two restricted: medication, safe-sleep device) (5 quotes) |
| 008 | beyondthebumpUK-1sz7dwz | read | quoted (3 quotes) |
| 008 | NewParents-1t0cnv9 | read | triple crosspost of Mommit-1t0coxo by same author; not quoted separately (0 quotes) |
| 008 | Mommit-1t0coxo | read | quoted (bed-sharing line skipped) (2 quotes) |
| 008 | beyondthebump-1t0cqlx | read | triple crosspost of Mommit-1t0coxo by same author; not quoted separately (0 quotes) |
| 008 | NewParents-1t0kfe5 | read | quoted (one restricted: bed-sharing) (2 quotes) |
| 009 | NewParents-1t0logp | read | clean lines quoted; minor injury incident and bed-sharing lines skipped (3 quotes) |
| 009 | beyondthebump-1t14mp2 | read | quoted (bed-sharing lines skipped) (2 quotes) |
| 009 | NewParents-1t17uks | read | quoted (3 quotes) |
| 009 | Mommit-1t1bsc0 | read | quoted (4 quotes) |
| 009 | FirstTimeMom-1t1bvbw | read | two clean lines quoted; bed-sharing/safe-sleep account skipped (2 quotes) |
| 009 | pregnant-1t1ftv8 | read | quoted (4 quotes) |
| 009 | NewParents-1t1jei7 | read | clean lines quoted; bed-sharing and mattress lines skipped (2 quotes) |
| 009 | NewParents-1t1r7np | read | quoted (infant sleep-position line skipped) (2 quotes) |
| 009 | Parenting-1t1s16j | read | quoted (5 quotes) |
| 009 | BabyBumps-1t1u0o4 | read | quoted once, possible_promo (polished, health-site link) (1 quotes) |
| 009 | Mommit-1t1xejw | read | quoted (contrary: mother sleeps a lot) (3 quotes) |
| 009 | pregnant-1t1xsn8 | read | quoted (3 quotes) |
| 009 | Mommit-1t26lvb | read | quoted (choking incident skipped) (3 quotes) |
| 009 | pregnant-1t2gzbp | read | three clean lines quoted; medication content skipped (3 quotes) |
| 009 | PregnancyUK-1t3anlm | read | quoted (3 quotes) |
| 009 | NewParents-1t3bz59 | read | quoted (one restricted: bed-sharing) (5 quotes) |
| 009 | pregnant-1t3jbbm | read | quoted (2 quotes) |
| 009 | Postpartum_Depression-1t3k3rp | excluded | centred on named conditions, hospital stay and medication; not quoted (0 quotes) |
| 009 | NewParents-1t3m8fq | read | quoted (3 quotes) |
| 009 | NewParents-1t3r99d | read | quoted (2 quotes) |
| 010 | NewParents-1t3ziwd | excluded | centred on accidental substance ingestion while caring for the baby; not quoted (0 quotes) |
| 010 | NewParents-1t4cpzk | read | quoted (bed-sharing and infant weight lines skipped) (3 quotes) |
| 010 | NewParents-1t4p7op | read | clean lines quoted; condition, treatment and hospital lines skipped (3 quotes) |
| 010 | beyondthebump-1t4rbjc | read | identical crosspost of NewParents-1t4p7op; not quoted separately (0 quotes) |
| 010 | Postpartum_Depression-1t4rfgm | read | one clean line quoted; condition, supplement and medication content skipped (1 quotes) |
| 010 | sleeptrain-1t4xrg1 | read | quoted (one restricted: bed-sharing) (2 quotes) |
| 010 | pregnant-1t542oq | read | quoted (loss lines skipped) (2 quotes) |
| 010 | beyondthebumpUK-1t552d7 | read | quoted (3 quotes) |
| 010 | pregnant-1t55ef0 | read | quoted (supplement and earlier breakdown lines skipped) (3 quotes) |
| 010 | NewParents-1t58dg5 | read | quoted (2 quotes) |
| 010 | beyondthebump-1t5b2im | read | quoted (panic wording skipped) (2 quotes) |
| 010 | sleeptrain-1t5ffbv | read | quoted (3 quotes) |
| 010 | pregnant-1t5s0rd | read | quoted (2 quotes) |
| 010 | beyondthebump-1t5su9w | read | quoted (3 quotes) |
| 010 | sleeptrain-1t5xhob | read | one restricted quote (safe-sleep detail) (1 quotes) |
| 010 | beyondthebump-1t646fk | read | quoted (3 quotes) |
| 010 | NewParents-1t657ya | read | quoted (infant medical and bed-sharing lines skipped) (2 quotes) |
| 010 | workingmoms-1t67qpr | read | quoted (2 quotes) |
| 010 | workingmoms-1t67w5z | excluded | bed-sharing post describing rough physical handling of the toddler; not quoted (0 quotes) |
| 010 | NewParents-1t6a4ft | read | clean lines quoted with trims; supplement and condition lines skipped (3 quotes) |
| 010 | Parenting-1t6jf8c | read | quoted (child's medical condition skipped) (3 quotes) |
| 010 | sahm-1t6vc88 | read | quoted (one restricted: named condition) (4 quotes) |
| 011 | Parenting-1t6xgqn | read | quoted once (1 quotes) |
| 011 | sleeptrain-1t78cy6 | read | quoted (one restricted: safe-sleep detail; migraine line skipped) (4 quotes) |
| 011 | pregnant-1t7g0ua | read | quoted (2 quotes) |
| 011 | sleeptrain-1t7idft | read | quoted (one restricted: bed-sharing) (2 quotes) |
| 011 | sleeptrain-1t7wfa8 | read | quoted (infant illness line skipped) (2 quotes) |
| 011 | NewParents-1t8d0tm | read | quoted (bed-sharing fear lines skipped) (3 quotes) |
| 011 | BabyBumps-1t8h3ec | excluded | centred on named mental-health conditions and medication; not quoted (0 quotes) |
| 011 | workingmoms-1t8t9fw | read | quoted (4 quotes) |
| 011 | beyondthebump-1t8zqly | read | quoted (4 quotes) |
| 011 | NewParents-1t91lbv | read | quoted (2 quotes) |
| 011 | BabyBumps-1t9k2lq | read | quoted once (1 quotes) |
| 011 | workingmoms-1t9kltx | read | quoted (one restricted; condition and medication lines skipped) (2 quotes) |
| 011 | sleeptrain-1t9ofcv | read | quoted (one restricted: bed-sharing) (3 quotes) |
| 011 | Mommit-1t9po82 | read | quoted (5 quotes) |
| 011 | pregnant-1ta2c6r | read | quoted once; labour-symptom content skipped (1 quotes) |
| 011 | beyondthebump-1taaqz6 | read | quoted (3 quotes) |
| 012 | NewParents-1tac311 | read | quoted (2 quotes) |
| 012 | NewParents-1taib3d | read | quoted (infant medical line skipped) (4 quotes) |
| 012 | beyondthebumpUK-1tasbr7 | read | quoted (bed-sharing and unsafe-surface reply skipped) (4 quotes) |
| 012 | NewParents-1taw2qq | read | quoted once; relationship content not sleep-related (1 quotes) |
| 012 | sleeptrain-1tb1gwn | read | quoted (infant medication and medical history skipped) (2 quotes) |
| 012 | beyondthebump-1tb5w5n | read | quoted (2 quotes) |
| 012 | beyondthebump-1tbi20l | read | quoted (road incident line skipped) (3 quotes) |
| 012 | beyondthebumpUK-1tbkq3x | read | quoted (bed-sharing line skipped) (2 quotes) |
| 012 | sleeptrain-1tc68en | read | quoted (bed-sharing lines skipped) (3 quotes) |
| 012 | NewParents-1tcsy5n | read | quoted; partner-asleep-with-baby incident and monitor lines skipped (4 quotes) |
| 012 | sleeptrain-1tdbv3u | read | quoted (infant allergy and chest-sleep lines skipped) (2 quotes) |
| 012 | beyondthebump-1tdghil | read | quoted (one restricted: bed-sharing) (4 quotes) |
| 012 | NewParents-1tdh0m3 | read | quoted (one restricted: partner's named condition) (4 quotes) |
| 012 | pregnant-1tdkyuc | read | quoted (medication line skipped) (2 quotes) |
| 012 | NewParents-1tdmpen | read | quoted (2 quotes) |
| 012 | NewParents-1tdmq89 | read | quoted (bed-sharing and medication replies skipped) (4 quotes) |
| 012 | BabyBumps-1tds9fo | read | quoted once (1 quotes) |
| 012 | sleeptrain-1tdsufr | read | quoted (one restricted: bed-sharing) (2 quotes) |

## Handling notes

- Restriction is quote-level, per the wave-3 prompt. Clean lines from posts that discuss bed-sharing, medication or a condition elsewhere were quoted unrestricted; any quote whose own words touch bed-sharing, a safe-sleep detail or device, a sleep aid, a supplement, medication, a named condition or treatment is flagged restricted. Units centred on self-harm or suicidal wording, rough handling of a child, a safe-sleep incident, substance ingestion, or named conditions with medication were excluded whole.
- Trims use ` […] `. Four trims cut a restricted clause (sleep aid, supplement, therapy technique, medication) out of an otherwise clean run, so the record stays quotable: sm08-0096, sm08-0196, sm08-0326, sm08-0327. The others only shorten (sm08-0001, sm08-0064, sm08-0087, sm08-0360).
- Crossposts by one author were quoted from one unit only: NewParents-1slwy85 = beyondthebumpUK-1slwza8; beyondthebump-1t4rbjc = NewParents-1t4p7op; NewParents-1t0cnv9 and beyondthebump-1t0cqlx = Mommit-1t0coxo. NewParents-1stnkb6 and NewParents-1sr0jm1 read as the same author (same details); counted as one voice.
- Speaker rule applied strictly: authors who never say mom/mum/mother, breastfeeding, pumping, postpartum or pregnancy are `parent_unspecified` even when the post implies a mother (e.g. sm08-0215, sm08-0405). Pregnant authors with a child are `experienced_mother` / `second_pregnancy`.
- How to continue: nothing in MR08's assignment is unread.
