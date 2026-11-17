# Reddit full reads: reader R03 (keep_otherside 003–004, keep_core 001–006)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder). Voice file: `voice/reddit-r03.jsonl` (ids `sb03-0001` … `sb03-0327`). Notes: `synthesis/reader-notes-r03.md`. Staging files the voice file was built from: `scratchpad/R03/q1-…q8-*.txt` (one per chunk, in id order); the chunk text as read is in `scratchpad/R03/read-v1a-*.txt`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_otherside-003`, `-004`, `read-v1a-keep_core-001` … `-006`) |
| units in those chunks | 127 |
| units read in full (post + every OP reply archived in the unit) | 127 |
| units excluded (lines not to cross) | 0 |
| units read, no quote taken | 3 (below) |
| units quoted | 124 |
| quotes written | 327 |
| verify | `verify_quotes.py voice/reddit-r03.jsonl` → 327 quotes, 0 failed |

Units per chunk: otherside-003 = 16, otherside-004 = 14, core-001 = 19, core-002 = 19, core-003 = 10, core-004 = 14, core-005 = 18, core-006 = 17.

Ids by chunk: otherside-003 → 0001–0050; otherside-004 → 0051–0087; core-001 → 0088–0132; core-002 → 0133–0177; core-003 → 0178–0203; core-004 → 0204–0247; core-005 → 0248–0287; core-006 → 0288–0327.

Counts are counts of quotes chosen, never of people.

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1vxpdw7.txt` | cross-post, same text as `sleeptrain-1vxp7np` (quoted there; ages differ, 6 vs 7 months) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1vy7kg5.txt` | cross-post, same text as `NewParents-1vy6sd2` (quoted there) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1vzapy6.txt` | short-nap question with no scene, no named attempt and no parent state beyond generic lines |

Other cross-posts: `sahm-1w9fmkp` repeats `Parenting-1w9f61y`; the post body was quoted from `Parenting-1w9f61y` only, and the r/sahm unit gave only its own OP replies (sb03-0021 to 0023).

## Passages read but deliberately not quoted (lines not to cross)

Units stay in; only these passages were skipped.

- `NewParents-1vype6d`: the parent's intrusive images of harming the baby during rage at night. Not quoted; the anger and the door-slam scene are (sb03-0240, 0241).
- `beyondthebumpUK-1vyry3l`: belief that crying raises intracranial pressure. Not quoted (no claims about crying harm either way); the reservation line is (sb03-0251).
- `sleeptrain-1vyzcg3` comment `p60swvz` (sleep apnoea referral question), `NewParents-1vxnkoj` (baby turns blue when crying, heart condition), `sleeptrain-1vzgt0j` (helmet temperature rules), `Mommit-1vz1a0b` (allergy/ER detail, a relative's illness), `NewParents-1vy8fyp` and `Mommit-1vz6zj4` (reflux medicines, diet eliminations): medical detail kept to context lines where needed, never quoted as a cause.
- `sleeptrain-1vxp7np`: the parent's "night terrors" guess is in the title only; the quote is the scene (sb03-0112).
- sb03-0007 quotes a father's report that his wife believes CIO "can have some serious negative effects on kids". It is kept as the other side's stated reason, not as a claim; do not reuse it as fact.

## How to continue

Nothing assigned to R03 is unread. Do not re-run R03 or append to `voice/reddit-r03.jsonl`; a new reader takes a new prefix.
