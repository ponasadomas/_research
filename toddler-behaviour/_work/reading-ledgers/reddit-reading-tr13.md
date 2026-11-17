# Reddit full reads — TR13 (wave 2, 2026-06-25 → 08-24)

Brief: `../_shared/_tools/brief-reading.md`. Reader TR13, id prefix `tb13`, voice file `voice/reddit-tr13.jsonl`, scratch `scratchpad/TR13/` (per-chunk compact records `q-0NN.jsonl`, builder `build.py`, per-chunk notes `ledger-notes.txt`). Read 2026-10-25. Units in this set are dated 2026-07-09 → 2026-07-17 (replies to 2026-08-21).

## Chunks assigned (from `_raw/reddit/read-w2/assignments.txt`)

| chunk | units |
|---|---|
| read-w2-keep_core-015 | 18 |
| read-w2-keep_core-016 | 13 |
| read-w2-keep_core-017 | 12 |
| read-w2-keep_core-018 | 21 |
| read-w2-keep_core-019 | 18 |
| read-w2-keep_core-020 | 14 |
| read-w2-keep_core-021 | 14 |
| read-w2-keep_core-022 | 13 |
| read-w2-keep_core-023 | 12 |
| **total** | **135** |

## Counts

- Units in chunks: 135
- Units read in full: 135 (none unfinished)
- Units excluded (safety or medical; nothing quoted): 7
- Units read, no quote (exact duplicates of another unit in this set): 3
- Units quoted: 125
- Quotes written: 357 (tb13-0001 … tb13-0357), ids unique
- Restricted quotes: 10 (listed in `synthesis/reader-notes-tr13.md`, "Restricted ids")
- Verify: `python3 -I _tools/verify_quotes.py voice/reddit-tr13.jsonl` → 357 quotes, 0 failed

## Units excluded (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1ussovb.txt` | verbal harshness toward a child; parent mental-health detail |
| `../_shared/_raw/reddit-2026/units/toddlers-1uw5ojc.txt` | verbal harshness toward a child |
| `../_shared/_raw/reddit-2026/units/toddlers-1ux1k0s.txt` | medical treatment details; verbal harshness toward a child |
| `../_shared/_raw/reddit-2026/units/toddlers-1uxpjjd.txt` | physical force toward a child |
| `../_shared/_raw/reddit-2026/units/pottytraining-1uz5qbr.txt` | restraint of a child; medical history |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1uz7pkb.txt` | physical discipline of a child |
| `../_shared/_raw/reddit-2026/units/toddlers-1uu53zs.txt` | child body/privacy topic (duplicate of pottytraining-1uu4zum, where only the method sentence was quoted) |

## Units read, no quote (duplicates)

| unit | duplicate of |
|---|---|
| `../_shared/_raw/reddit-2026/units/pottytraining-1usnfk2.txt` | toddlers-1us50l8 |
| `../_shared/_raw/reddit-2026/units/toddlers-1uugaw0.txt` | pottytraining-1uu2ni8 |
| `../_shared/_raw/reddit-2026/units/toddlers-1uu53zs.txt` | pottytraining-1uu4zum (also listed above) |

Cross-posts where the second copy added an OP reply and that reply alone was quoted: toddlers-1usmnm2 (= pottytraining-1us7tb6), toddlers-1uw44bz (= pottytraining-1uvtfk6), toddlers-1uwrcmz (= Mommit-1uwrban).

## Quoted units with passages left out (quote-level exclusions)

Passages describing a parent shouting, snapping, physical handling or a child's self-injury, parents' own childhood abuse, medication, supplements, laxatives, fevers and other medical detail were not quoted in: Parenting-1us99gb, toddlers-1urnuce, Mommit-1urvomw, Parenting-1us0hiv, pottytraining-1us4v80, toddlers-1us50l8, pottytraining-1us8mq6, toddlers-1us5v4i, toddlers-1urixt4, pottytraining-1us7tb6, toddlers-1ut1gjj, toddlers-1uszfzl, Parenting-1utwxol, Parenting-1ut4m25, Parenting-1utc2j5, Mommit-1utxirw, daddit-1uu3vsg, toddlers-1utxg2u, pottytraining-1uu2ni8, pottytraining-1uu4zum, sahm-1uuh8k3, AttachmentParenting-1uv3yay, pottytraining-1uve6zu, Parenting-1uvfj4g, pottytraining-1uuumqo, Parenting-1uupz68, sahm-1uvhct9, pottytraining-1uvtfk6, toddlers-1uw44bz, pottytraining-1uvsvgy, toddlers-1uvi699, toddlers-1uvraoy, toddlers-1uvy6q1, toddlers-1uwrolo, toddlers-1uwh1b4, toddlers-1ux265s, toddlers-1uxsu38, daddit-1uxzdw8, toddlers-1uxfkwk, Parenting-1uxdrpr, pottytraining-1uxglpb, Parenting-1uy1cow, Parenting-1uy8l3w, Mommit-1uypu5f, toddlers-1uytl58, toddlers-1uz254q, toddlers-1uz4l27, Parenting-1uz78r2 (the carrying struggle at pickup).

## Units with a diagnosis or developmental/medical question (only the parent's fear or strain quoted)

toddlers-1usup5w, pottytraining-1utltlo, toddlers-1uwrolo, daddit-1uyb41c, toddlers-1uybesz, pottytraining-1uvtfk6 / toddlers-1uw44bz, Mommit-1uypu5f, toddlers-1ut0shr, toddlers-1uwh1b4, toddlers-1uykpv4. Restricted quote ids are in the reader notes.

## How to continue

Nothing unread in this assignment. The voice file is rebuilt from `scratchpad/TR13/q-*.jsonl` by `scratchpad/TR13/build.py`; ids are final now that other files cite them — do not rebuild.
