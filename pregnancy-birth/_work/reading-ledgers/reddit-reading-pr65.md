# Reddit full read — reader PR65 (wave 3, 2026-10-25)

Brief: `../../_shared/_tools/brief-reading.md` with `../../_shared/_tools/prompt-pregnancy-reader-w3.txt` (NN=65). Voice file: `voice/reddit-pr65.jsonl` (ids pb65-0001 to pb65-0224). Notes: `synthesis/reader-notes-pr65.md`. Scratch: `scratchpad/PR65/` (unit list, batch files, exclusions, restricted ids).

## Chunks assigned
`read-w3-keep_core-118` … `read-w3-keep_core-126` (9 chunks) from `_raw/reddit/read-w3/chunks.jsonl`. Posts dated 2026-05-23 to 2026-05-27.

| chunk | units |
|---|---|
| read-w3-keep_core-118 | 18 |
| read-w3-keep_core-119 | 11 |
| read-w3-keep_core-120 | 23 |
| read-w3-keep_core-121 | 17 |
| read-w3-keep_core-122 | 21 |
| read-w3-keep_core-123 | 15 |
| read-w3-keep_core-124 | 17 |
| read-w3-keep_core-125 | 26 |
| read-w3-keep_core-126 | 22 |
| **total** | **170** |

## Counts
- Units in chunks: 170 (matches the assignment line).
- Units read in full: 170. None unfinished.
- Units excluded (not quoted): 20, listed below.
- Units read, kept, no quote taken: 36 (crossposts already quoted once, condition- or medication-centred posts with nothing quotable outside restricted ground, off-niche or trivial posts).
- Units quoted: 114.
- Quotes written: 224, of which 22 restricted (listed in the notes). `verify_quotes.py`: 224 quotes, 0 failed. Ids unique (224/224).

## Units excluded (neutral reasons)
| unit | reason |
|---|---|
| pregnant-1tl3znj | pregnancy loss |
| pregnant-1tlbg7e | substance use |
| pregnant-1tlm953 | relationship-safety concern |
| pregnant-1tlvyyf | family substance use, family crisis |
| beyondthebump-1tlwhfx | crisis wording, severe mental-health content |
| NewParents-1tm6p2q | acute medical emergency at birth |
| pregnant-1tm6x8r | termination decision discussed |
| pregnant-1tmjlx2 | mental-health-centred post |
| beyondthebump-1tmppwq | severe mental-health post |
| BabyBumps-1tmrdwa | severe mental-health content |
| pregnant-1tn8uto | mental-health-centred post |
| pregnant-1tnle5c | severe mental-health content, substance-use mention |
| BabyBumps-1tnn92l | termination mentioned, severe mental-health content |
| pregnant-1tns9l7 | termination mentioned, housing insecurity |
| BabyBumps-1tnuqlu | possible crisis wording |
| beyondthebump-1to6kkg | acute medical emergency at birth |
| Mommit-1to84pn | partner aggression |
| BabyBumps-1tof65m | child-safety concern |
| pregnant-1tof8ra | child-safety concern (crosspost of the above) |
| pregnant-1totigk | mental-health-centred post |

No unit in these chunks mentions pressure from anyone to end a pregnancy. The four units that mention termination at all are excluded: pregnant-1tm6x8r, BabyBumps-1tnn92l, pregnant-1tns9l7 (each the author's own words), and pregnant-1tlm953 (adoption pressure, excluded on relationship-safety grounds).

Rule for medical backstory: a unit is excluded when it is centred on an acute emergency at the birth (NewParents-1tm6p2q, beyondthebump-1to6kkg). Units where a hard birth is background and the post is about something else were kept and quoted only on that other subject, with no medical passage quoted: beyondthebumpUK-1tozvts (lack of help from her mother, partner shifts; pb65-0203, pb65-0204), BabyBumps-1tp5dq3 (older child kept apart, grandmother minding him), beyondthebumpUK-1tmz9pb and beyondthebumpUK-1tozism (feeding support).

## Read, no quote
Mommit-1tl4b88 (crosspost of BabyBumps-1tl48zh), pregnant-1tlhq5b, pregnant-1tlol5k, BabyBumps-1tlorl9, pregnant-1tlwf9w, pregnant-1tlzzmj, beyondthebump-1tm1pcu, NewParents-1tm6eft, pregnant-1tm8hh6, pregnant-1tmc5n4, pregnant-1tml3c9, pregnant-1tmlocd (crosspost of PregnancyUK-1tmlljl), pregnant-1tmml9e, pregnant-1tmp9eg, pregnant-1tn2pqx, BabyBumps-1tn66zh (crosspost of pregnant-1tn63em), pregnant-1tn6wao, BabyBumps-1tna8s9, pregnant-1tnhzyu, pregnant-1tnu7k3, pregnant-1tnwd8l, pregnant-1tnytpq, PregnancyUK-1to0sqo, BabyBumps-1to5pl2, pregnant-1to8iww, PregnancyUK-1tob8dy, pregnant-1togjez (removed-by-moderator crosspost of BabyBumps-1togl6v), PregnancyUK-1tojm9p, pregnant-1tomugb, pregnant-1toookn, pregnant-1tot7au, PregnancyUK-1towg0j (near-duplicate of pregnant-1tommnb), BabyBumps-1tp3j2u, pregnant-1tp4e81, BabyBumps-1tp8hqj (crosspost of pregnant-1tp8fbq), beyondthebump-1tpa1h8 (crosspost of pregnant-1tpa03k).

## How to continue
Nothing is unread. Do not re-run this reader (it appends to `voice/reddit-pr65.jsonl`).
