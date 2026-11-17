# Reddit full reads: reader R08 (keep_core 039–046)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder). Posts dated 2026-09-10 to 2026-09-14.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_core-039` … `-046`) |
| units in those chunks | 142 |
| units read in full (post + every OP reply archived in the unit) | 142 |
| units excluded (line not to cross) | 4 (below) |
| units read, no quote taken (other reasons) | 7 (below) |
| units quoted | 131 |
| quotes written | 291 (`voice/reddit-r08.jsonl`, ids `sb08-0001` … `sb08-0291`) |
| verify | `verify_quotes.py voice/reddit-r08.jsonl` → 291 quotes, 0 failed |

Units per chunk: 039 = 18, 040 = 16, 041 = 23, 042 = 23, 043 = 15, 044 = 19, 045 = 12, 046 = 16.

## Units excluded (read in full, nothing quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wfrgys.txt` | mental-health crisis content (OP later reports being okay) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1we7dvm.txt` | describes a non-recommended infant sleep position; safe-sleep incident |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wdyeeq.txt` | baby newly rolling to the belly and crying; safe-sleep topic, no other content |
| `../_shared/_raw/reddit-2026/units/NewParents-1wfg998.txt` | choosing an adult-size floor mattress for a 6-month-old; safe-sleep product question |

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/Mommit-1wch42h.txt` | cross-post, same author and text as `beyondthebump-1wch6pi` (quoted there) |
| `../_shared/_raw/reddit-2026/units/toddlers-1wcn6gh.txt` | cross-post, same text as `sleeptrain-1wcngbr` (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wd4oht.txt` | cross-post of `toddlers-1wd4wff` (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wczvqu.txt` | nursery furniture logistics, nothing about the night beyond that |
| `../_shared/_raw/reddit-2026/units/NewParents-1wd02gq.txt` | cross-post of the above |
| `../_shared/_raw/reddit-2026/units/NewParents-1wd1vdk.txt` | night sweating question; a medical question, not a sleep problem |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wdkkv8.txt` | bare schedule post, no scene or wording worth more than other quotes |

Other cross-posts quoted only once: `sahm-1wcpcdn` (one unique OP reply, sb08-0060) duplicates `AttachmentParenting-1wcop6o`; `sleeptrain-1we7hyg` (one unique reply, sb08-0165) duplicates `toddlers-1we7gs0`; `NewParents-1wfl3ve` is the same parent as `sleeptrain-1weepvu` reposting after a hostile reception.

## Passages read but deliberately not quoted (lines not to cross)

Units stay in; only these passages were skipped.

- `beyondthebump-1wchoap`: PPD/PPA mention and a paediatrician's PPD-screening comment. Quoted only her sleep, body and husband lines.
- `NewParents-1wd0tkh`: baby only naps on the belly. Quoted only the daycare fear (sb08-0085, restricted).
- `beyondthebump-1wcijuh`: 11-week-old moved to own room early. Only the Owlet purchase line (sb08-0034, restricted) and the "no judgement" opener.
- `Mommit-1wd701m`: newborn slept in a lounge pillow in the parents' bed. Not quoted; only the mother-in-law comparison.
- `sleeptrain-1wdz912`: cosleeping fall worries. Not quoted. The exhaustion lines are quoted and restricted (sb08-0141, -0142).
- `NewParents-1weebyn`: mother's fear about cosleeping with an 11-day-old. Not quoted; only her partner and resentment lines.
- `sleeptrain-1wdtded`, `sleeptrain-1we0mf0`: tummy rolling in the crib. Not quoted.
- `beyondthebumpUK-1wfrb1w` comment `p9ziil2`: checking the baby's breathing. Not quoted.
- `AttachmentParenting-1wez14j`: a doctor suggesting sleep medication for a toddler. Not quoted.
- `NewParents-1wfoluc`, `NewParents-1wfskf6`, `sleeptrain-1wftslu`, `sleeptrain-1wdx7ug`: antidepressant, PPD, "so depressed", "depressive pit". Not quoted.
- Medical detail (reflux, CMPA, formula trials, omeprazole, ENT, sinus, orchidopexy, sweating) appears in context only where needed, never as a cause.

## How to continue

Nothing assigned is unread. Do not append to `voice/reddit-r08.jsonl` from another agent; start a new file with a new prefix. Restricted ids are listed in `synthesis/reader-notes-r08.md` for the orchestrator to copy into `synthesis/restricted-ids.md`.
