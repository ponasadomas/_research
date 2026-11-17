# Reddit full reads, reader R05 (2026-10-25)

Brief: `../../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (never rebuilt). Voice file: `voice/reddit-r05.jsonl` (ids `sb05-0001` to `sb05-0317`). Notes: `synthesis/reader-notes-r05.md`. Staging: `scratchpad/R05/` (`q-015.json` … `q-022.json` hold the picks per chunk; `build.py` turns them into the voice file, deriving url/date/post_id/comment_id from each unit's header lines; `units.txt` is the assigned unit list).

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_core-015` to `read-v1a-keep_core-022`) |
| units in those chunks | 127 |
| units read in full (post + every OP reply in the unit) | 127 |
| units read with no quotes taken | 4 (listed below) |
| units quoted | 123 |
| quotes written | 317 |
| `verify_quotes.py voice/reddit-r05.jsonl` | 317 quotes, 0 failed |

Counts are counts of quotes chosen, not of people. Ids unique (checked from disk). No unit was left unfinished.

## Units read with no quotes taken (all read in full)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1w33dh9.txt` | Word-for-word cross-post of `sleeptrain-1w2yvf5` (quoted there). No OP replies. |
| `../_shared/_raw/reddit-2026/units/NewParents-1w3lipl.txt` | Light "would you rather" post about a poor feeder who sleeps well; nothing on a sleep problem. |
| `../_shared/_raw/reddit-2026/units/toddlers-1w4pija.txt` | Toddler nightmares after a fright at a festival; anecdote with no sleep-solution, purchase or parent-state content beyond generic. |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1w5u4b0.txt` | Short floor-bed equipment question after a crib-slat scare; a safe-sleep product query, nothing quotable without implying safety advice. |

Cross-post note: `toddlers-1w5g1ar` repeats `sleeptrain-1w5fm2n` word for word; quotes were taken from the sleeptrain copy, plus one from the OP's distinct reply in the toddlers copy.

Speaker note: `new_mother` / `experienced_mother` / `expecting_mother` only where the author says mom/mum/FTM/STM, pregnant, postpartum, or nurses from her own breast; "my husband" alone was left as `parent_unspecified`.

## Units by chunk (quotes per unit)

- **keep_core-015** (16): Parenting-1w2odsr 4 · NewParents-1w2oso3 1 · sleeptrain-1w2ozlj 4 · beyondthebumpUK-1w2sc5x 1 · sleeptrain-1w2tqv4 4 · NewParents-1w2u172 2 · sleeptrain-1w2yvf5 1 · sleeptrain-1w2z16w 2 · NewParents-1w2zkzs 3 · beyondthebump-1w31169 4 · Mommit-1w320hh 1 · NewParents-1w328en 3 · NewParents-1w33dh9 0 · sleeptrain-1w35b8m 6 · beyondthebumpUK-1w38c0r 5 · sleeptrain-1w3aefu 4
- **keep_core-016** (17): toddlers-1w3cmab 2 · NewParents-1w3dfz8 3 · sleeptrain-1w3fdjr 2 · sleeptrain-1w3foo4 7 · sleeptrain-1w3hpnk 2 · sleeptrain-1w3k7m6 1 · NewParents-1w3lipl 0 · sleeptrain-1w3mjfa 1 · sleeptrain-1w3mwom 3 · sleeptrain-1w3p0to 4 · beyondthebumpUK-1w3q8y3 1 · sleeptrain-1w3tkbj 3 · NewParents-1w3u9t3 5 · sleeptrain-1w3ua7k 3 · sleeptrain-1w3uuod 5 · sleeptrain-1w3v233 5 · sleeptrain-1w3w36z 2
- **keep_core-017** (19): sleeptrain-1w3wsph 3 · sleeptrain-1w3xg8s 1 · sleeptrain-1w3y0e3 1 · NewParents-1w3y0rb 3 · toddlers-1w3zixe 2 · sleeptrain-1w3zw8i 2 · sleeptrain-1w403c0 2 · sleeptrain-1w41cjx 3 · sleeptrain-1w4247d 1 · beyondthebumpUK-1w42dh2 2 · beyondthebumpUK-1w42sk6 5 · sleeptrain-1w43r1v 4 · Parenting-1w45mgt 1 · sleeptrain-1w463a4 4 · toddlers-1w467xn 5 · sleeptrain-1w47unr 2 · NewParents-1w48452 1 · sleeptrain-1w4baob 2 · sleeptrain-1w4cdcf 3
- **keep_core-018** (15): sleeptrain-1w4dezm 3 · sleeptrain-1w4e3r6 2 · sleeptrain-1w4eugq 2 · NewParents-1w4eyz2 1 · sleeptrain-1w4f6cq 2 · NewParents-1w4gamk 1 · AttachmentParenting-1w4h0de 7 · sleeptrain-1w4heg7 3 · sleeptrain-1w4hj2w 3 · AttachmentParenting-1w4ib2j 1 · toddlers-1w4igjx 1 · sleeptrain-1w4ijdg 5 · sleeptrain-1w4in2f 3 · NewParents-1w4jkyh 2 · sleeptrain-1w4kh8j 3
- **keep_core-019** (17): sleeptrain-1w4lf9v 3 · toddlers-1w4loe3 3 · sleeptrain-1w4mokt 2 · sleeptrain-1w4mrzd 4 · sleeptrain-1w4nljo 1 · toddlers-1w4pija 0 · NewParents-1w4q0t4 1 · Parenting-1w4q86n 2 · NewParents-1w4qy5n 2 · sleeptrain-1w4s0uv 1 · NewParents-1w4s8ai 7 · sleeptrain-1w4uvkd 1 · sleeptrain-1w4wwin 3 · toddlers-1w4x2nb 2 · sleeptrain-1w4x5jd 2 · NewParents-1w4xchh 1 · sleeptrain-1w4xfa4 3
- **keep_core-020** (13): sleeptrain-1w4ymnu 10 · AttachmentParenting-1w50e96 1 · sleeptrain-1w50fs7 2 · toddlers-1w511fh 1 · sleeptrain-1w52evc 2 · beyondthebumpUK-1w533sh 1 · beyondthebumpUK-1w54n9x 2 · sleeptrain-1w57a42 1 · AttachmentParenting-1w59nhm 4 · sleeptrain-1w59yc7 2 · NewParents-1w5a43x 1 · sleeptrain-1w5a9g3 1 · toddlers-1w5c5xg 3
- **keep_core-021** (14): sleeptrain-1w5d1wy 1 · sleeptrain-1w5dflf 4 · toddlers-1w5efkb 1 · sleeptrain-1w5fgvu 3 · sleeptrain-1w5fm2n 3 · toddlers-1w5g1ar 1 · sleeptrain-1w5h2af 1 · sleeptrain-1w5i0cf 2 · Parenting-1w5icls 3 · ScienceBasedParenting-1w5jkld 2 · NewParents-1w5ke6p 1 · beyondthebumpUK-1w5kfwb 1 · beyondthebump-1w5khx9 3 · beyondthebump-1w5kiry 1
- **keep_core-022** (16): sleeptrain-1w5lsrm 4 · Mommit-1w5oah2 5 · Parenting-1w5psn5 1 · NewParents-1w5t2kb 1 · sleeptrain-1w5tkbq 3 · sleeptrain-1w5u4b0 0 · sleeptrain-1w5u7no 5 · NewParents-1w5v98r 2 · toddlers-1w5va3m 1 · daddit-1w5vh0r 6 · NewParents-1w5vyfx 2 · sleeptrain-1w5w2sr 1 · sleeptrain-1w5xxkv 3 · sleeptrain-1w5yxkl 2 · toddlers-1w62ngm 1 · toddlers-1w636es 4
