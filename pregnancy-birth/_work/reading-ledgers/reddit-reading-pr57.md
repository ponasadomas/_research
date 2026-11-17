# Reddit reading ledger — PR57 (wave 3, keep_core chunks 050–058)

Reader PR57, id prefix pb57, written 2026-10-25. Brief: `_shared/_tools/prompt-pregnancy-reader-w3.txt` and `_shared/_tools/brief-reading.md`. Extra instruction for this reader: units that mention pressure from anyone to end the pregnancy are excluded, even in passing (none of the quoted units does; the two units that mention termination at all are excluded below).

| step | count |
|---|---|
| chunks assigned | 9 (read-w3-keep_core-050 … read-w3-keep_core-058) |
| units in them | 158 (21+20+15+17+20+14+19+16+16) |
| units read in full | 158 |
| units with at least one quote | 118 |
| units excluded under the lines not to cross | 16 |
| units read, nothing quoted (thin, medical-only or off-niche) | 19 |
| crossposts not quoted (same author, same text quoted once from the other copy) | 5 |
| quotes written | 332 (pb57-0001 … pb57-0332) |
| restricted quotes | 29 (listed in `synthesis/reader-notes-pr57.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr57.jsonl` → 332 quotes, 0 failed |

118 + 16 + 19 + 5 = 158. pregnant-1svkugm is a crosspost of PregnancyUK-1svilwa but has its own distinct reply, which is quoted, so it is counted among the 118. Posts dated 22–25 April 2026; the latest quoted reply is 29 April 2026. Unit list: `scratchpad/PR57/units.txt`. Quote source records: `scratchpad/PR57/recs/rec-0NN.py`, built by `scratchpad/PR57/build.py` (rebuilds the voice file from the records; never append by hand). Per-unit decisions: `scratchpad/PR57/ledger.tsv`.

## Not quoted (neutral reason)

| chunk | unit | decision | reason |
|---|---|---|---|
| 050 | pregnant-1ssc56v | excluded | severe mental-health post with medication |
| 050 | Mommit-1ssgl7j | excluded | child injury (child-safety concern) |
| 050 | BabyBumps-1ssi0k5 | excluded | mental-health post with medication |
| 050 | BabyBumps-1sska4z | crosspost | same author, same text as pregnant-1ssk359 |
| 050 | pregnant-1ssp1vw | excluded | severe mental-health post |
| 050 | pregnant-1ssq82g | nothing | medical-only |
| 050 | pregnant-1ssqxkl | nothing | medical-only, thin |
| 051 | pregnant-1ssrpzy | excluded | acute medical situation and discharge against advice |
| 051 | BabyBumps-1ssttw8 | excluded | mental-health post with medication |
| 051 | PregnancyUK-1ssyhro | nothing | medical-only |
| 051 | pregnant-1st2c7g | nothing | medical-only |
| 051 | pregnant-1st2v5m | nothing | announcement logistics, off-niche |
| 051 | pregnant-1st4ix6 | crosspost | same author, same text as BabyBumps-1st4lhr |
| 052 | pregnant-1st5yz3 | nothing | off-niche (gym fragrance complaint) |
| 052 | pregnant-1stf95a | excluded | previous loss and mental-health history central to the post |
| 052 | pregnant-1stgk9h | nothing | thin, symptom-only |
| 052 | BabyBumps-1sth5kw | nothing | announcement etiquette, off-niche |
| 052 | pregnant-1stkdd8 | excluded | severe mental-health post (panic attacks, PTSD and depression relapse) |
| 053 | pregnant-1stkeu7 | excluded | severe mental-health post; reply contains crisis wording |
| 053 | pregnant-1stu837 | excluded | acute medical (repeated bleeding, emergency visits) |
| 054 | pregnant-1stuj3m | excluded | termination mentioned in a reply (family-disclosure post) |
| 054 | pregnant-1stvens | nothing | announcement to a friend, off-niche |
| 054 | pregnant-1stznz1 | nothing | telling parents, off-niche |
| 054 | pregnant-1su0mde | nothing | positive test and early symptom question, thin |
| 054 | pregnant-1su15dc | crosspost | same author, same text as BabyBumps-1su1073 |
| 054 | pregnant-1su4khv | nothing | medical condition management, medical-only |
| 055 | pregnant-1sua75c | nothing | medical condition and treatment-centred, medical-only |
| 055 | pregnant-1suffaf | excluded | previous losses and a partner-safety incident |
| 055 | BabyBumps-1sugfqe | nothing | medical test wait, medical-only |
| 055 | pregnant-1suggpc | crosspost | same author, same text as BabyBumps-1sugfqe; medical-only |
| 055 | pregnant-1suh22q | nothing | early bleeding, medical-only |
| 055 | pregnant-1suiy2i | excluded | acute injury and emergency visit |
| 056 | pregnant-1sujaba | excluded | severe mental-health wording (hopeless, cannot get out of bed) |
| 056 | pregnant-1suki0j | excluded | acute illness and emergency visit; previous losses mentioned |
| 056 | pregnant-1sutae8 | excluded | termination mentioned in a reply |
| 057 | pregnant-1sv4zol | nothing | sexual dreams, off-niche |
| 058 | BabyBumps-1sve50f | nothing | bridesmaid dress, off-niche |
| 058 | pregnant-1svhnqu | crosspost | same author, same text as PregnancyUK-1svhf5k |
| 058 | pregnant-1svnbtv | nothing | medical conditions and monitoring, medical-only |
| 058 | pregnant-1svrww1 | nothing | cardiac test result, medical-only |

## Quoted with care (part of the unit left out)

Units where a passage was deliberately not quoted (medication, condition, previous-birth injury, a relative's health, an infant's medical details): beyondthebump-1sskm6p, pregnant-1ssubkz, pregnant-1ssundx, pregnant-1ssz6l3, NewParents-1st5d2v, pregnant-1st5fg0, pregnant-1st71hs, pregnant-1stf09x, pregnant-1stl575, pregnant-1su28se, beyondthebumpUK-1su9jo5, pregnant-1suf1vk, beyondthebumpUK-1sufmyu, PregnancyUK-1suovfv, pregnant-1supopk, pregnant-1suwotc, Mommit-1suzvyv, BabyBumps-1sv7ekt, BabyBumps-1sv7t3u, pregnant-1sve0gf, pregnant-1svfryu, pregnant-1svgbvg. pregnant-1stsgri: the post's exhaustion wording ("I don't want to do this anymore", "never come out again") was read as possible crisis wording, so both quotes from it are restricted.

## Unread

None. Every unit in the nine chunks was read in full.
