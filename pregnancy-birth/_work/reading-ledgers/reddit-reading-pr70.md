# Reddit reading ledger — PR70 (wave 3, core chunks 164–173)

Reader PR70 · id prefix `pb70` · voice file `voice/reddit-pr70.jsonl` · notes `synthesis/reader-notes-pr70.md` · scratch `scratchpad/PR70/` (`units.txt` chunk→unit list, `log.txt` exclusions and no-quote reasons, `restricted.txt`).

Brief: `../_shared/_tools/prompt-pregnancy-reader-w3.txt` → `../_shared/_tools/brief-reading.md`. Window: posts 10–15 June 2026. Extra rule from the orchestrator: units mentioning pressure from anyone to end the pregnancy are excluded, even in passing.

| step | count |
|---|---|
| chunks assigned | 10 (`read-w3-keep_core-164` … `-173`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in them | 167 (15 + 22 + 22 + 16 + 9 + 9 + 20 + 13 + 20 + 21) |
| units read in full (post + every OP reply) | 167 |
| units excluded under the lines not to cross | 29 |
| units read, nothing quotable (medical-only, thin, off-niche or crosspost duplicate) | 18 |
| units with at least one quote | 120 |
| quotes written | 331 (pb70-0001 … pb70-0331), 45 restricted |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr70.jsonl` → 331 quotes, 0 failed |

Unread: none. Every unit in the ten chunks was read to the end.

## Excluded (neutral reasons, never quoted)

| unit | reason |
|---|---|
| pregnant-1u2hhtr | early-pregnancy waiting post centred on prior loss history and treatment |
| BabyBumps-1u2juao | acute obstetric symptoms, repeated L&D visits |
| pregnant-1u2lvk9 | relationship difficulties and pressure from others about continuing the pregnancy |
| pregnant-1u2mx24 | acute bleeding, ER visit |
| Mommit-1u2rjn8 | infant-safety concern (overheating, animals) |
| PregnancyUK-1u2rumq | centred on mental health |
| pregnant-1u30pkk | chronic pain with crisis-adjacent wording |
| pregnant-1u37k23 | alcohol context |
| pregnant-1u3drl9 | severe mental-health post with substance context |
| PregnancyUK-1u3ohab | scan finding and specialist referral |
| BabyBumps-1u3tlns | medication and mental-health post |
| pregnant-1u3wmlx | weight post centred on eating-disorder history |
| pregnant-1u3zzmy | screening test result |
| pregnant-1u48cv8 | anger post with violent wording |
| pregnant-1u4awtu | road accident and injuries during pregnancy |
| pregnant-1u4egnn | relationship-safety concern |
| BabyBumps-1u4pum6 | monitoring decision centred on a mental-health diagnosis and family loss |
| BabyBumps-1u5kcoa | centred on acute pain and medication decisions |
| pregnant-1u5p3q8 | centred on severe anxiety/intrusive thoughts |
| PregnancyUK-1u5sx7x | crisis-adjacent wording, admission, multiple hardships |
| pregnant-1u5vjat | hospital admission and scan finding near term |
| BabyBumps-1u61bbk | alcohol context |
| pregnant-1u61wa9 | relationship breakdown and depressed mood |
| pregnant-1u61zoi | partner hostility about her body |
| pregnant-1u64191 | acute symptom, ER visit and surgical referral |
| pregnant-1u64bi3 | acute illness, ER visit |
| BabyBumps-1u6g343 | centred on a lab result and treatment access |
| beyondthebump-1u6jsv5 | diagnosis and infant weight-loss concern |
| pregnant-1u6lw6i | relationship crisis; author questions continuing the pregnancy |

## Read, no quote

| unit | reason |
|---|---|
| beyondthebump-1u2j4qh | infant travel planning, off niche |
| pregnant-1u2mjop | medication question only |
| pregnant-1u2nb6n | lonely birthday, nothing specific to the niche beyond one line |
| PregnancyUK-1u2uq3o | dental procedure timing question |
| Mommit-1u2z2ie | travel with an 8-week-old, off niche |
| pregnant-1u309pj | early test-line speculation |
| pregnant-1u31hlw | mood post, nothing usable beyond medication context |
| pregnant-1u3y401 | lab-value question only |
| BabyBumps-1u46z6c | crosspost of pregnant-1u46tlr (same author, same text); quoted once there. Text reads possibly tool-polished; one voice |
| beyondthebumpUK-1u4b5mi | crosspost of beyondthebump-1u4al9o (same author, same text); quoted once there |
| pregnant-1u50oet | dream anecdote |
| pregnant-1u54so5 | product-safety question; prior loss mentioned |
| pregnant-1u5hqo4 | positive-test announcement only |
| BabyBumps-1u5l44f | device-safety question |
| pregnant-1u5qjwc | food-safety question and hiding early pregnancy |
| pregnant-1u6ied8 | how to announce to a relative; nothing on niche |
| BabyBumps-1u6j2sm | crosspost of pregnant-1u6j158 (same author, same text); quoted once there |
| pregnant-1u6khaw | symptom question only |

## Unit notes

| unit | note |
|---|---|
| BabyBumps-1u3iaph | OP reply uses grave hyperbole; all quotes from unit restricted |
| beyondthebump-1u4d72d | OP reply contains idiomatic self-harm wording ("not kill myself over it"); all quotes from unit restricted |
| BabyBumps-1u4hl2v | two identical OP replies (ord7w55, ord7z4a); quoted once |
| NewParents-1u5ytwf | polished, possibly AI-written viral-style post, 0 OP replies; quoted as one voice, flagged in context |

## Per unit

| chunk | unit | quotes |
|---|---|---|
| 164 | pregnant-1u2ha5x | 4 |
| 164 | pregnant-1u2hhtr | excluded |
| 164 | pregnant-1u2iar1 | 3 |
| 164 | beyondthebump-1u2j4qh | 0 |
| 164 | BabyBumps-1u2jkvn | 2 |
| 164 | BabyBumps-1u2juao | excluded |
| 164 | pregnant-1u2jxdv | 5 |
| 164 | BabyBumps-1u2kcyv | 1 |
| 164 | pregnant-1u2lvk9 | excluded |
| 164 | BabyBumps-1u2lyye | 4 |
| 164 | pregnant-1u2mjop | 0 |
| 164 | BabyBumps-1u2mqs7 | 7 |
| 164 | pregnant-1u2mx24 | excluded |
| 164 | BabyBumps-1u2mz4f | 1 |
| 164 | pregnant-1u2nb6n | 0 |
| 165 | pregnant-1u2nzvk | 4 |
| 165 | BabyBumps-1u2qd5w | 5 |
| 165 | NewParents-1u2qfzq | 5 |
| 165 | Mommit-1u2rjn8 | excluded |
| 165 | PregnancyUK-1u2rumq | excluded |
| 165 | pregnant-1u2tdqm | 1 |
| 165 | PregnancyUK-1u2tp22 | 1 |
| 165 | pregnant-1u2ug98 | 3 |
| 165 | PregnancyUK-1u2uq3o | 0 |
| 165 | BabyBumps-1u2vozi | 3 |
| 165 | pregnant-1u2x024 | 4 |
| 165 | pregnant-1u2x8jc | 2 |
| 165 | pregnant-1u2yx70 | 2 |
| 165 | pregnant-1u2yy4n | 1 |
| 165 | Mommit-1u2z2ie | 0 |
| 165 | pregnant-1u309pj | 0 |
| 165 | pregnant-1u30pkk | excluded |
| 165 | pregnant-1u314mh | 2 |
| 165 | pregnant-1u31hlw | 0 |
| 165 | PregnancyUK-1u32iv2 | 3 |
| 165 | pregnant-1u33oqp | 2 |
| 165 | pregnant-1u33tc0 | 4 |
| 166 | pregnant-1u341x5 | 4 |
| 166 | PregnancyUK-1u366f2 | 3 |
| 166 | BabyBumps-1u36g3g | 4 |
| 166 | pregnant-1u37k23 | excluded |
| 166 | pregnant-1u3bimz | 2 |
| 166 | pregnant-1u3bvbj | 5 |
| 166 | pregnant-1u3drl9 | excluded |
| 166 | BabyBumps-1u3ef7t | 1 |
| 166 | pregnant-1u3hybc | 3 |
| 166 | BabyBumps-1u3iaph | 2 |
| 166 | BabyBumps-1u3ipbs | 2 |
| 166 | pregnant-1u3j9ue | 1 |
| 166 | pregnant-1u3jeq7 | 1 |
| 166 | pregnant-1u3jfmo | 2 |
| 166 | pregnant-1u3k8vi | 2 |
| 166 | BabyBumps-1u3ltna | 1 |
| 166 | PregnancyUK-1u3ohab | excluded |
| 166 | pregnant-1u3psee | 2 |
| 166 | beyondthebump-1u3r1s9 | 1 |
| 166 | beyondthebump-1u3rtig | 2 |
| 166 | Mommit-1u3rvma | 3 |
| 166 | PregnancyUK-1u3s6dh | 2 |
| 167 | BabyBumps-1u3stf7 | 11 |
| 167 | BabyBumps-1u3tlns | excluded |
| 167 | pregnant-1u3ujwg | 3 |
| 167 | pregnant-1u3v0oz | 2 |
| 167 | pregnant-1u3vpk5 | 3 |
| 167 | pregnant-1u3wbkd | 1 |
| 167 | pregnant-1u3wmlx | excluded |
| 167 | pregnant-1u3y401 | 0 |
| 167 | PregnancyUK-1u3ym6o | 3 |
| 167 | pregnant-1u3zzmy | excluded |
| 167 | pregnant-1u43b4w | 3 |
| 167 | beyondthebump-1u448ci | 6 |
| 167 | BabyBumps-1u465m2 | 3 |
| 167 | PregnancyUK-1u46hdv | 2 |
| 167 | pregnant-1u46tlr | 3 |
| 167 | BabyBumps-1u46z6c | 0 |
| 168 | PregnancyUK-1u471di | 3 |
| 168 | pregnant-1u48cv8 | excluded |
| 168 | pregnant-1u48hgp | 2 |
| 168 | pregnant-1u4acel | 4 |
| 168 | beyondthebump-1u4al9o | 6 |
| 168 | pregnant-1u4awtu | excluded |
| 168 | beyondthebumpUK-1u4b5mi | 0 |
| 168 | pregnant-1u4bg63 | 2 |
| 168 | BabyBumps-1u4bmad | 1 |
| 169 | beyondthebump-1u4d72d | 10 |
| 169 | pregnant-1u4dddh | 2 |
| 169 | pregnant-1u4egnn | excluded |
| 169 | BabyBumps-1u4hl2v | 3 |
| 169 | BabyBumps-1u4kzkx | 2 |
| 169 | pregnant-1u4lb2y | 2 |
| 169 | pregnant-1u4p689 | 2 |
| 169 | BabyBumps-1u4pum6 | excluded |
| 169 | NewParents-1u4siyv | 3 |
| 170 | PregnancyUK-1u4t0ve | 3 |
| 170 | pregnant-1u4t6oh | 1 |
| 170 | PregnancyUK-1u4t9vf | 3 |
| 170 | pregnant-1u4zmok | 1 |
| 170 | BabyBumps-1u4zrvv | 1 |
| 170 | pregnant-1u50esi | 3 |
| 170 | pregnant-1u50oet | 0 |
| 170 | pregnant-1u53luk | 3 |
| 170 | pregnant-1u54smm | 5 |
| 170 | pregnant-1u54so5 | 0 |
| 170 | NewParents-1u56yu6 | 2 |
| 170 | pregnant-1u57ihq | 2 |
| 170 | pregnant-1u57x2y | 5 |
| 170 | pregnant-1u5bohs | 3 |
| 170 | pregnant-1u5ehf3 | 2 |
| 170 | PregnancyUK-1u5few0 | 1 |
| 170 | BabyBumps-1u5h0s9 | 1 |
| 170 | beyondthebump-1u5hfcy | 3 |
| 170 | pregnant-1u5hqo4 | 0 |
| 170 | BabyBumps-1u5kcoa | excluded |
| 171 | BabyBumps-1u5l44f | 0 |
| 171 | BabyBumps-1u5oamh | 10 |
| 171 | pregnant-1u5p3q8 | excluded |
| 171 | pregnant-1u5q1dv | 5 |
| 171 | pregnant-1u5qjwc | 0 |
| 171 | pregnant-1u5qnqf | 1 |
| 171 | beyondthebump-1u5qwts | 5 |
| 171 | pregnant-1u5r4rb | 2 |
| 171 | PregnancyUK-1u5sx7x | excluded |
| 171 | pregnant-1u5tjnz | 1 |
| 171 | pregnant-1u5tzdp | 1 |
| 171 | pregnant-1u5vjat | excluded |
| 171 | pregnant-1u5vy4c | 1 |
| 172 | Mommit-1u5x0az | 2 |
| 172 | pregnant-1u5xwcu | 2 |
| 172 | PregnancyUK-1u5ycps | 3 |
| 172 | NewParents-1u5ytwf | 3 |
| 172 | pregnant-1u5z53t | 2 |
| 172 | BabyBumps-1u5zxe0 | 4 |
| 172 | BabyBumps-1u61bbk | excluded |
| 172 | pregnant-1u61wa9 | excluded |
| 172 | pregnant-1u61zoi | excluded |
| 172 | pregnant-1u62avx | 2 |
| 172 | pregnant-1u62gmw | 1 |
| 172 | pregnant-1u64191 | excluded |
| 172 | pregnant-1u643q9 | 1 |
| 172 | pregnant-1u64bi3 | excluded |
| 172 | pregnant-1u6623z | 1 |
| 172 | pregnant-1u68njg | 6 |
| 172 | pregnant-1u69o3q | 2 |
| 172 | pregnant-1u6ahd6 | 2 |
| 172 | pregnant-1u6aqtk | 4 |
| 172 | PregnancyUK-1u6ce6m | 2 |
| 173 | pregnant-1u6dh8c | 1 |
| 173 | pregnant-1u6djg6 | 2 |
| 173 | BabyBumps-1u6eaq9 | 2 |
| 173 | Mommit-1u6fpyu | 2 |
| 173 | BabyBumps-1u6g343 | excluded |
| 173 | pregnant-1u6gtmi | 4 |
| 173 | beyondthebumpUK-1u6h0up | 2 |
| 173 | BabyBumps-1u6huuf | 4 |
| 173 | pregnant-1u6i094 | 1 |
| 173 | NewParents-1u6i09l | 3 |
| 173 | pregnant-1u6idk4 | 2 |
| 173 | pregnant-1u6ied8 | 0 |
| 173 | pregnant-1u6j158 | 2 |
| 173 | BabyBumps-1u6j2sm | 0 |
| 173 | beyondthebump-1u6jsv5 | excluded |
| 173 | pregnant-1u6k7qb | 5 |
| 173 | pregnant-1u6khaw | 0 |
| 173 | pregnant-1u6klki | 3 |
| 173 | pregnant-1u6l649 | 1 |
| 173 | pregnant-1u6lw6i | excluded |
| 173 | PregnancyUK-1u6lwf0 | 1 |
