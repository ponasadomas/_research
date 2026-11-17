# Reddit reading ledger — PR52 (wave 3, keep_core chunks 003–012)

Reader PR52 · id prefix `pb52` · voice file `voice/reddit-pr52.jsonl` · notes `synthesis/reader-notes-pr52.md` · scratch `scratchpad/PR52/` (`units.tsv` unit list with sizes, `log.md` running exclusions/restrictions).

Brief: `../_shared/_tools/prompt-pregnancy-reader-w3.txt` → `../_shared/_tools/brief-reading.md`. Window: posts 1–6 April 2026 (replies by the poster up to September 2026).

| step | count |
|---|---|
| chunks assigned | 10 (`read-w3-keep_core-003` … `-012`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in them | 161 (21, 18, 13, 13, 19, 15, 11, 12, 17, 22) |
| units read in full (post + every OP reply) | 161 |
| units excluded under the lines not to cross | 28 |
| crossposts (same author, same text) | 4 pairs; one copy quoted at most |
| units read, nothing quotable (medical-only, thin or duplicate) | 36 |
| units with at least one quote | 97 |
| quotes written | 217 (pb52-0001 … pb52-0217), 23 restricted |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr52.jsonl` → 217 quotes, 0 failed |

Unread: none. Every unit in the ten chunks was read to the end.

## Excluded (neutral reasons, never quoted)

| unit | reason |
|---|---|
| PregnancyUK-1s9r0hh | severe mental-health wording |
| pregnant-1s9sj02 | substance use |
| pregnant-1s9vdwf | severe mental-health and relationship content |
| NewParents-1s9xnpp | infant medical question, beyond stage |
| BabyBumps-1sa10h9 | infection/medication and relationship disclosure |
| pregnant-1sa14ba | serious screening finding |
| pregnant-1sa41aw | bereavement and depression |
| pregnant-1sa4saj | acute medical question |
| NewParents-1sa5lyc | severe mental-health post, beyond stage |
| beyondthebumpUK-1sa83vn | severe mental-health wording |
| Mommit-1sahe10 | birth injury and crisis-team contact |
| pregnant-1saj5gy | acute housing/financial crisis with an assault reference |
| pregnant-1san1x6 | acute medical emergency |
| pregnant-1sarhal | relationship-safety concern |
| PregnancyUK-1savhlz | serious scan finding and acute anxiety |
| pregnant-1sb22zf | family violence and safety concerns |
| beyondthebump-1sb28lc | severe mental-health post with medication, beyond stage |
| BabyBumps-1sbev1i | acute medical emergency after birth |
| beyondthebump-1sbm3oq | medical complications and severe postpartum distress |
| pregnant-1sbtuaj | acute medical admission; mental-health medication |
| pregnant-1sbwzr2 | partner aggression / relationship-safety |
| BabyBumps-1scd1ne | birth trauma with a sexual-assault reference |
| BabyBumps-1scldwx | acute medical symptoms |
| BabyBumps-1scltco | relationship-safety concern |
| pregnant-1scmssl | panic and mental-health medication |
| PregnancyUK-1sd6u6e | prior loss history and termination thoughts |
| pregnant-1sd6zd6 | substance-use history and medical conditions |
| pregnant-1sde6vd | acute medical (emergency visit for dehydration) |

## Read, no quote

BabyBumps-1s9pflu, pregnant-1s9pgox (crosspost pair), pregnant-1s9tqxx, PregnancyUK-1s9vu1a, beyondthebump-1sa1wzo, pregnant-1sa7j9j, BabyBumps-1sabmmm (crosspost of pregnant-1sabqn9, which is quoted), pregnant-1saizyo, pregnant-1sal4p0, pregnant-1sapy3g, pregnant-1sat503, pregnant-1satjgf, pregnant-1sb2gmw, pregnant-1sbcdbr (screening wait with loss history; held back under the loss rule), pregnant-1sbdpns, BabyBumps-1sbg169, pregnant-1sbgsm7, beyondthebump-1sbw8v6, BabyBumps-1sc1wgk, beyondthebumpUK-1sc7r3e, pregnant-1scekgf, pregnant-1sceuj4, PregnancyUK-1sckbs6, BabyBumps-1scohcg, BabyBumps-1scugn4, PregnancyUK-1scwqhi, beyondthebump-1scwwc4, NewParents-1scxfq4, PregnancyUK-1sd0pn6, pregnant-1sd9geo, PregnancyUK-1sde5yo + pregnant-1sde7r0 (crosspost pair), PregnancyUK-1sdid1x + pregnant-1sdieux (crosspost pair), pregnant-1sdjsow, pregnant-1sdjz7b.

## Crossposts and repeat authors

BabyBumps-1s9pflu = pregnant-1s9pgox; BabyBumps-1sabmmm = pregnant-1sabqn9 (r/pregnant copy quoted); PregnancyUK-1sde5yo = pregnant-1sde7r0; PregnancyUK-1sdid1x = pregnant-1sdieux. Likely repeat author: PregnancyUK-1scbvg4 and pregnant-1scdd87 (twins, single, same test date): count as one voice.

## Flagged (quoted, one voice each)

BabyBumps-1sbw9ne (polished prose, 312 comments; possibly tool-tidied), beyondthebump-1sd78tr (polished "Hi beautiful people" list request; possibly tool-written). No Nurava/@nuravaa or vitamin seeding seen; no promo post in these chunks.

## How to continue

Nothing unread. The next reader takes the following keep_core chunks from `_raw/reddit/read-w3/assignments.txt`.
