# Reddit reading ledger — PR64 (wave 3, read-w3 keep_core 110–117)

Reader PR64 · id prefix pb64 · voice file `../voice/reddit-pr64.jsonl` · notes `../synthesis/reader-notes-pr64.md` · scratch `../scratchpad/PR64/` (record sources `c110.py`–`c117.py`, builder `build.py`, exclusion list `ledger.tsv`). Written 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md` + `../../_shared/_tools/prompt-pregnancy-reader-w3.txt`.

## Counts

| step | n |
|---|---|
| chunks assigned | 8 (read-w3-keep_core-110 → 117) |
| units in those chunks | 161 (18 + 19 + 16 + 20 + 28 + 23 + 17 + 20) |
| units read in full | 161 |
| units excluded (no quote, neutral reason) | 25 (23 at first read + 2 withdrawn on a safety review) |
| units read, kept, no quote (incl. 2 same-author crossposts) | 9 |
| units quoted | 127 |
| quotes written | 327 (ids pb64-0001 → pb64-0330; pb64-0184, pb64-0307, pb64-0308 withdrawn with their units, not reused), 47 restricted |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr64.jsonl` → 327 quotes, 0 failed |

Post dates in these chunks: 2026-05-18 → 2026-05-23 (quoted OP replies up to 2026-05-31).

## Units excluded (neutral reasons, not quoted)

| unit | reason |
|---|---|
| pregnant-1thal00 | centred on medication and stopping a substance |
| BabyBumps-1thc691 | centred on a partner's hostile remarks |
| pregnant-1thiftr | mentions pressure to end the pregnancy |
| pregnant-1thnsix | severe mental-health post |
| pregnant-1thp2dw | substance use and a termination mention in the thread |
| BabyBumps-1ti64cu | mentions a disagreement about continuing the pregnancy |
| pregnant-1ti64t5 | serious screening finding, long inpatient stay |
| pregnant-1ti9ey4 | mentions sexual assault |
| pregnant-1ti9s59 | severe anxiety post centred on loss stories and medication |
| beyondthebumpUK-1tidrts | family violence and severe mental-health content |
| pregnant-1tim33b | severe mental-health post |
| BabyBumps-1tir0pv | substance use and relationship-safety content |
| pregnant-1tiu3ce | past personal trauma disclosure |
| pregnant-1tiyr9k | acute medical episode |
| BabyBumps-1tj1bbx | acute medical episode (repost of pregnant-1tiyr9k) |
| pregnant-1tj1uev | severe mental-health post |
| pregnant-1tjbohz | acute medical emergency at the birth |
| pregnant-1tjutin | serious screening finding |
| pregnant-1tjwziz | relationship-safety concern and severe distress |
| pregnant-1tjxcpe | severe mental-health post |
| BabyBumps-1tivds3 | serious screening finding (withdrawn on review) |
| pregnant-1tktdfu | repeated acute medical emergencies (withdrawn on review) |
| pregnant-1tk883t | mentions sexual assault |
| pregnant-1tkik0q | severe mental-health post |
| pregnant-1tknfh1 | severe mental-health post |

## Units read, no quote

| unit | reason |
|---|---|
| pregnant-1th4r4j | off-niche food post, nothing usable |
| PregnancyUK-1tht0yp | read; examination detail only, nothing usable |
| pregnant-1tin6ep | read; medication question only |
| pregnant-1titau4 | read; supplement-dose question only |
| pregnant-1tiwssr | read; nothing usable |
| pregnant-1tiz9h5 | crosspost of BabyBumps-1tiyktm (same author), quoted once there |
| pregnant-1tj4bm5 | crosspost of Mommit-1tio38q (same author), quoted once there |
| PregnancyUK-1tjlwzh | read; medication question only |
| pregnant-1tkgm7z | read; medication question, prior-loss mention |

## Notes on the ledger

- pregnant-1thiftr is excluded under the extra instruction for this reader: the post mentions a doctor's advice to end the pregnancy.
- pregnant-1tkd6o4 (quoted, all quotes restricted) uses the words "end this pregnancy earlier" about an induction at term, not termination; kept on that reading.
- Units with crisis-like or emergency wording anywhere had every quote restricted: pregnant-1tjdw5u, pregnant-1tkd6o4, pregnant-1tk09ek, pregnant-1tkzsqa, pregnant-1tiyvvh, pregnant-1tgt5en; also restricted on review: pb64-0127 (tearing), pb64-0268 (medication-centred post).
- Nothing is unread. How to continue: nothing to continue for these chunks; rebuild the voice file only by re-running `scratchpad/PR64/build.py` (it rewrites the file from c110–c117.py with the same ids; records flagged 2 are withdrawn and their ids skipped).
