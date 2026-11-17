# Reddit full reads — TR19 (wave 3, keep_otherside 007–013 and keep_core 001–005, posts 2026-04-01 → 06-24)

Brief: `../_shared/_tools/brief-reading.md` and `../_shared/_tools/prompt-toddler-reader-w3.txt`. Reader TR19, id prefix `tb19`, voice file `voice/reddit-tr19.jsonl`, scratch `scratchpad/TR19/`. Read 2026-10-25.

## Chunks assigned (from `_raw/reddit/read-w3/assignments.txt`)

| chunk | units |
|---|---|
| read-w3-keep_otherside-007 | 14 |
| read-w3-keep_otherside-008 | 11 |
| read-w3-keep_otherside-009 | 11 |
| read-w3-keep_otherside-010 | 10 |
| read-w3-keep_otherside-011 | 13 |
| read-w3-keep_otherside-012 | 13 |
| read-w3-keep_otherside-013 | 5 |
| read-w3-keep_core-001 | 16 |
| read-w3-keep_core-002 | 17 |
| read-w3-keep_core-003 | 13 |
| read-w3-keep_core-004 | 13 |
| read-w3-keep_core-005 | 13 |
| **total** | **149** |

Note: in `chunks.jsonl` the keep_core-001 … 005 units are dated 2026-04-01 → 04-06 and the keep_otherside 007 … 013 units 2026-05-14 → 06-24. The unit list with sizes is in `scratchpad/TR19/units.tsv`; the working log in `scratchpad/TR19/log.md`.

## Counts

- Units in chunks: 149
- Units read in full: 149 (none unfinished)
- Units excluded under a line not to cross (not quoted): 16
- Units read, reposts of a quoted or excluded unit (no quotes): 4
- Units quoted: 129
- Quotes written: 389 (tb19-0001 … tb19-0389), ids unique (checked from disk)
- Restricted quotes: 29 (listed in `synthesis/reader-notes-tr19.md`, "Restricted ids")
- Quotes tagged `possible_promo` (one seeded-looking unit; never count): 3 (tb19-0285 … tb19-0287)
- Verify: `python3 -I _tools/verify_quotes.py voice/reddit-tr19.jsonl` → 389 quotes, 0 failed

## Units excluded or not quoted (neutral reasons)

| unit | status | reason |
|---|---|---|
| NewParents-1s9wie9 | repost | same text as Parenting-1s9wd2o (quoted there) |
| Mommit-1sccy8y | repost | same text as pottytraining-1sccxcf (quoted there) |
| Parenting-1scmpt0 | repost | same text as pottytraining-1sce3kz (quoted there) |
| Parenting-1u79sf8 | repost | same text as toddlers-1u79k8w (quoted there) |
| Parenting-1s9yh7d | excluded | parent shuts the child in a room as discipline; restraint |
| pottytraining-1sa2sj7 | excluded | physical force toward a child on the potty |
| toddlers-1sa33u0 | excluded | cross-post of the above, same force scene (the OP's later success reply sits here too) |
| toddlers-1sak4br | excluded | force and raised voice to keep the child in place |
| pottytraining-1sb2r9s | excluded | yelling and guilt-tripping listed as methods; child body/privacy detail |
| toddlers-1sblk8f | excluded | child hits himself (self-injury) |
| Mommit-1sbmnpz | excluded | child self-injury during tantrums; evaluation question |
| workingmoms-1sc37w2 | excluded | child self-endangerment, parent restrains the child, medical history |
| toddlers-1sdeo1y | excluded | medical treatment details (constipation remedies) |
| toddlers-1sdkuxx | excluded | parent restrains and smacks the child |
| Mommit-1tgytkk | excluded | parent's own childhood abuse is the subject |
| Parenting-1tiw6su | excluded | an adult yelling at a two-year-old is the subject |
| AttachmentParenting-1tyqevi | excluded | an onlooker reports a parent yelling at a crying child; that is the subject |
| toddlers-1u1enx8 | excluded | parent pinches the child back |
| Mommit-1u8ef3z | excluded | child body/privacy topic and injuries |
| toddlers-1uc8tib | excluded | spanking, parent's own childhood abuse, child self-injury |

Units quoted with care (only clean lines; the line-crossing passage left out): Mommit-1sa3qsf, toddlers-1s9quxt, toddlers-1sbzr1c, toddlers-1sco5go, toddlers-1scpah1, toddlers-1td5t64, toddlers-1thrsjc, GentleParenting-1tk397u (the parent's own yelling not quoted), toddlers-1tn7aue, GentleParenting-1tnip1z, toddlers-1u786ja, pottytraining-1ubdb0n, toddlers-1udzurp, Mommit-1ue3daz.

## What has and hasn't been read

All 149 units in the twelve assigned chunks were read in full, including every original-poster reply in each unit. Nothing is unread. Contexts in `voice/reddit-tr19.jsonl` were neutralised to "parent" wherever the speaker is `parent_unspecified`.

## How to continue

Nothing left in this assignment. Do not re-run this reader against `voice/reddit-tr19.jsonl` (it would append duplicates); a new reader takes a new prefix.
