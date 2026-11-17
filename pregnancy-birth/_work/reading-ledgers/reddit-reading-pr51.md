# Reddit reading ledger — PR51 (pregnancy-birth, wave 3)

Reader PR51 · id prefix `pb51` · voice file `voice/reddit-pr51.jsonl` · written 2026-10-25 · brief `../_shared/_tools/brief-reading.md` + `../_shared/_tools/prompt-pregnancy-reader-w3.txt`.

## Assignment

Chunks from `_raw/reddit/read-w3/chunks.jsonl` (line `PR51` in `_raw/reddit/read-w3/assignments.txt`, 152 units). Posts dated 2026-04-01 (core-001/002) and 2026-05-20 to 2026-06-24 (keep_otherside-018 to -028).

| chunk | units |
|---|---|
| read-w3-keep_core-001 | 16 |
| read-w3-keep_core-002 | 14 |
| read-w3-keep_otherside-018 | 14 |
| read-w3-keep_otherside-019 | 14 |
| read-w3-keep_otherside-020 | 9 |
| read-w3-keep_otherside-021 | 13 |
| read-w3-keep_otherside-022 | 5 |
| read-w3-keep_otherside-023 | 11 |
| read-w3-keep_otherside-024 | 15 |
| read-w3-keep_otherside-025 | 13 |
| read-w3-keep_otherside-026 | 13 |
| read-w3-keep_otherside-027 | 10 |
| read-w3-keep_otherside-028 | 5 |
| **total** | **152** |

## Counts

| step | n |
|---|---|
| units assigned | 152 |
| units read in full | 152 |
| units with at least one quote | 121 |
| units excluded (safety, seeded, rage-bait) | 22 |
| crossposts / same-author reposts (read, quoted once under the other copy) | 6 |
| read, nothing quotable | 3 |
| quotes written | 346 (pb51-0001 to pb51-0346) |
| restricted quote ids | 56 (listed in `synthesis/reader-notes-pr51.md`) |
| verify_quotes.py | 346 quotes, 0 failed |

Counts are counts of quotes chosen, not of people.

## Units excluded (neutral reasons, nothing copied)

| unit | reason |
|---|---|
| pregnant-1s94z3j | acute medical: failed fetal testing, possible induction next day |
| pregnant-1s9cf2b | AI-written (pasted chatbot reply) relationship and intimacy post; not niche, not independent |
| BabyBumps-1s9gpxe | acute medical: hospital admission in preterm labour |
| pregnant-1s9orqw | post centred on anxiety attacks and medication |
| pregnant-1tips68 | relationship-safety concern: controlling partner, pain dismissed |
| pregnant-1tivtkc | housing crisis: put out of home with no money mid-pregnancy |
| BabyBumps-1tkwchk | substance use before a positive test |
| pregnant-1tkwuoe | substance use; crosspost of BabyBumps-1tkwchk |
| pregnant-1tmjiij | sexual-consent and relationship-safety concern |
| NewParents-1tmrx41 | child-safety concern in a father's post |
| beyondthebump-1tolva4 | severe postpartum mental-health post with giving-up wording |
| pregnant-1tqm5vp | substance use in pregnancy (partner's post) |
| BabyBumps-1trb7lk | seeded: founder promoting a waitlist app ("Ahead", tryahead.app); not independent |
| pregnant-1ts6s5c | professional post centred on obstetric-emergency handling and staff injuries |
| daddit-1tylc3k | severe mental-health post (father, wishes to undo the birth) |
| pregnant-1u211up | bleeding in early pregnancy after a previous loss; centred on loss fear |
| pregnant-1u2ev17 | crisis wording and family coercion (considering a shelter) |
| PregnancyUK-1u3z04w | self-promotion: a partner offering his own contraction-timer app; not independent |
| daddit-1u4q783 | infant death (first child) in the post |
| pregnant-1ubu5d3 | high-risk bleeding, stopped psychiatric medication, depression; medical and mental-health centred |
| Mommit-1udfcwe | child-safety concern (past incident of the baby being dropped) |
| daddit-1uej8dc | likely rage-bait (bold-formatted rant about a name taken at a UK antenatal class); not quoted |

## Crossposts and reposts (read in full; quoted once)

| unit | note |
|---|---|
| pregnant-1s9mm54 | crosspost of BabyBumps-1s9cxyl (same author, same text); quoted once there |
| pregnant-1s9oqeq | crosspost of BabyBumps-1s9oqsq; quoted once there |
| pregnant-1tqux87 | crosspost of BabyBumps-1tquvmh; quoted once there |
| BabyBumps-1tr8pxb | crosspost of Mommit-1tr8nzc; quoted once there |
| BabyBumps-1u9b69u | crosspost of pregnant-1u9avzd; quoted once there |
| PregnancyUK-1u9fg5x | crosspost of pregnant-1u9fnbr; quoted once there |

## Read in full, nothing quoted

| unit | note |
|---|---|
| daddit-1tvap24 | joke thread, nothing quotable |
| pregnant-1u2ury2 | husband on a rumour about him and his wife's low mood; nothing usable and touches her mental health |
| pregnant-1u4k4bg | dental X-ray worry; medical, nothing usable |

## What has and has not been read

All 152 assigned units were read in full, including every original-poster reply in each unit. Nothing in this assignment is unread. Units whose quotes are all restricted at unit level: BabyBumps-1tus7q2 (a reply uses hurt/kill wording about sleep deprivation; every quote from the unit restricted), beyondthebump-1u23upy (leaving thoughts at night; every quote restricted), NewParents-1u9tkhb (readmission emergency), NewParents-1ue7uc2 (newborn choking at birth). Quotes from pregnant-1tk3mkt and pregnant-1u1sf9y are restricted because the posts mention an earlier pregnancy loss.

## How to continue

Nothing to continue for PR51. Do not re-run this reader against the same voice file; it is complete. Scratch files (per-chunk concatenations, the quote draft `q.jsonl`, `build.py`, `excluded.tsv`, `restricted.txt`) are in `scratchpad/PR51/`.
