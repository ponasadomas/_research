# Reddit reading ledger — PR69 (wave 3, core chunks 155–163)

Reader PR69 · id prefix `pb69` · voice file `voice/reddit-pr69.jsonl` · notes `synthesis/reader-notes-pr69.md` · scratch `scratchpad/PR69/` (`units.txt` chunk→unit list, `ledger.tsv` per-unit status, `c155.jsonl` … `c163.jsonl` record inputs, `restricted.txt`, `idmap.tsv`, `c155.txt` … `c163.txt` concatenated reading copies).

Brief: `../_shared/_tools/prompt-pregnancy-reader-w3.txt` → `../_shared/_tools/brief-reading.md`. Window: posts 7–10 June 2026. Extra rule from the orchestrator: any unit that mentions pressure from anyone to end the pregnancy is excluded, even in passing (none quoted; ambiguous cases excluded below).

| step | count |
|---|---|
| chunks assigned | 9 (`read-w3-keep_core-155` … `-163`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in them | 160 (15 + 15 + 23 + 23 + 13 + 17 + 17 + 16 + 21) |
| units read in full (post + every OP reply) | 160 |
| units excluded under the lines not to cross | 24 |
| units read, nothing quoted (medical-only, thin, off-niche, crossposts, seeded/rage-bait) | 32 |
| units with at least one quote | 104 |
| quotes written | 277 (pb69-0001 … pb69-0277), 26 restricted |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr69.jsonl` → 277 quotes, 0 failed |

Unread: none. Every unit in the nine chunks was read to the end.

## Excluded (neutral reasons, never quoted)

| unit | reason |
|---|---|
| pregnant-1tzsah2 | partner aggression / relationship-safety concern |
| pregnant-1tzt0uc | severe mental-health post |
| pregnant-1tzumyw | weighs ending the pregnancy; loss history |
| BabyBumps-1tzvz5b | severe mental-health post; author pregnant at 18 |
| beyondthebump-1tzxbds | self-harm wording |
| BabyBumps-1tzxebp | severe mental-health post with medication |
| BabyBumps-1tzzgke | self-described severe health anxiety/OCD post |
| pregnant-1u06327 | centred on an acute medical emergency at the previous birth |
| pregnant-1u09oan | severe mental-health post with medication |
| pregnant-1u0atbm | severe mental-health post |
| pregnant-1u0beqn | relationship-safety concern (sexual pressure) |
| pregnant-1u0j8qp | acute medical emergency |
| NewParents-1u0kad3 | acute medical emergency at birth; financial-aid ask |
| BabyBumps-1u0mmzy | serious scan findings with health conditions |
| FirstTimeMom-1u0pd6x | acute medical emergency; crosspost of pregnant-1u0j8qp |
| beyondthebump-1u0rctj | severe mental-health post with medication |
| BabyBumps-1u0v5mg | relationship breakdown; hints at a dispute over continuing the pregnancy |
| pregnant-1u111g5 | bereavement with crisis wording |
| Mommit-1u15brw | severe mental-health post with medication; same author and text as pregnant-1u09oan |
| pregnant-1u1hb2z | severe mental-health post with medication |
| pregnant-1u1sl3a | unplanned pregnancy, ambiguous about continuing |
| PregnancyUK-1u21i0u | severe mental-health post with medication |
| pregnant-1u2azna | centred on early-pregnancy viability worry |
| pregnant-1u2g0l6 | substance use |

## Read, nothing quoted

| unit | reason |
|---|---|
| BabyBumps-1tzpytd | medical-only (condition and medication) |
| pregnant-1tzy9me | centred on medication fear and anxiety |
| pregnant-1u07pv1 | off-niche (paternity question) |
| BabyBumps-1u0901i | cravings list, no usable material; likely same author as BabyBumps-1tzz0ap |
| pregnant-1u09xqc | medical-only (medication) |
| BabyBumps-1u0esjb | centred on medication and mental health |
| pregnant-1u0f9hx | travel question; nothing usable |
| BabyBumps-1u0gyya | medical-only |
| pregnant-1u0lc4o | nutrition advice list needing fact-check |
| BabyBumps-1u0mseh | thin (snack request) |
| BabyBumps-1u0ov13 | likely seeded supplement post (AZO named, testimonial format); not quoted |
| beyondthebumpUK-1u11v2k | medical-only (condition and medication) |
| pregnant-1u12zs9 | medical-only (blood pressure, tests) |
| pregnant-1u13iux | medical-only; repeat of BabyBumps-1tzpytd by the same author |
| BabyBumps-1u16jv4 | medical-only |
| pregnant-1u16ty4 | infant sleep-safety question; not quoted |
| PregnancyUK-1u19zoi | medical-only (dental procedure, medication) |
| pregnant-1u1d2lh | off-niche (pet rehoming) |
| BabyBumps-1u1fcwo | likely rage-bait or AI-written (no OP replies to 243 comments, stylised); not quoted |
| pregnant-1u1gusd | off-niche (sexual content) |
| pregnant-1u1nqsa | centred on medication and weight; crossposted as BabyBumps-1u1nsop |
| BabyBumps-1u1nsop | crosspost of pregnant-1u1nqsa |
| BabyBumps-1u1qbo1 | food-safety scare at 4 weeks; possibly young author; not quoted |
| pregnant-1u1qs3h | thin |
| pregnant-1u1yhk5 | medical-only (infection, medication) |
| pregnant-1u243r3 | off-niche (body change question) |
| pregnant-1u24it4 | crosspost of BabyBumps-1u24i84 |
| BabyBumps-1u25tpf | crosspost of pregnant-1u25t5g |
| beyondthebump-1u25uxb | crosspost of pregnant-1u25t5g |
| pregnant-1u2a80r | scan-finding worry; not quoted |
| beyondthebump-1u2d103 | medical-only (postpartum breast lump) |
| pregnant-1u2dlxz | crosspost of BabyBumps-1u2djfr |
