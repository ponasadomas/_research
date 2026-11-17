# Reddit full reads: reader R15 (read-v1b keep_core 005–012)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1b/chunks.jsonl` (frozen; unit paths relative to this folder).

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1b-keep_core-005` … `-012`) |
| units in those chunks | 127 |
| units read in full (post + every OP reply archived in the unit) | 127 |
| units excluded | 7 (below) |
| units read, no quote taken (other than exclusions) | 0 |
| units quoted | 120 |
| quotes written | 308 (`voice/reddit-r15.jsonl`, ids `sb15-0001` … `sb15-0308`) |
| verify | `verify_quotes.py voice/reddit-r15.jsonl` → 308 quotes, 0 failed |

Units per chunk: 005 = 19, 006 = 19, 007 = 16, 008 = 15, 009 = 13, 010 = 13, 011 = 14, 012 = 18.

Speakers (counts of quotes chosen, not of people): new_mother 161, parent_unspecified 109, experienced_mother 31, partner 7 (fathers: `NewParents-1wsoeo4`, `sleeptrain-1wspb38`, `NewParents-1wttisp`). Mothers tagged only where the author says mum/mom/mama, wife-of-husband with breastfeeding/pumping, or pregnancy; `experienced_mother` where she names an older child.

## Units excluded

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wrvyg6.txt` | safe-sleep: swaddle, rolling to belly and pacifier-as-safety questions run through the whole post |
| `../_shared/_raw/reddit-2026/units/Parenting-1wsjwas.txt` | safe-sleep (bed/side-car arrangement, fall risk) and infant-breathing fear |
| `../_shared/_raw/reddit-2026/units/NewParents-1wsno03.txt` | safe-sleep: rolling onto belly at night is the whole topic |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wsqdba.txt` | crosspost of the unit above; same reason |
| `../_shared/_raw/reddit-2026/units/NewParents-1wstnpg.txt` | mental-health crisis wording; replies are about treatment |
| `../_shared/_raw/reddit-2026/units/NewParents-1wtkgtm.txt` | safe-sleep: cosleeping and falling asleep with the baby in arms |
| `../_shared/_raw/reddit-2026/units/toddlers-1wtu8lb.txt` | child almost 4 (outside 0–36 months); post is about the parent's anger at night |

## Passages read but deliberately not quoted (lines not to cross)

The rest of each unit was used; only these passages were left out.

- `toddlers-1wr92aq`: the doctor's medication suggestion for bedtime (second-hand medical advice).
- `sleeptrain-1ws1d58`: the head-bumping-in-crib detail and the postpartum-anxiety aside.
- `NewParents-1ws9ddl`: the SIDS-risk note and the comment about drifting off with the baby on her (safe-sleep); the pumping/mental-health aside.
- `sleeptrain-1ws8nvn`, `sleeptrain-1wrsbc9`, `sleeptrain-1wsmzb1`, `sleeptrain-1wsw0os`, `NewParents-1wtp5yd`: medication dosing lines.
- `toddlers-1wspjah`: the breath-holding / self-injury passage.
- `sleeptrain-1wsqaw1`: the baby falling against the crib rail.
- `sleeptrain-1wt1q9t`: the lounger-between-parents sleep arrangement (safe-sleep).
- `beyondthebump-1wt4hzq`: the birth-trauma detail and the self-blame lines after telling the baby to "shut up".
- `beyondthebump-1wtdphx`: comment about past severe postpartum illness.
- `sleeptrain-1wtgqyz`: the depression / medication wording.
- `NewParents-1wtp5yd`: sleeping in the nursing chair with the baby; postpartum-depression mention.
- `beyondthebump-1wty87b` / `AttachmentParenting-1wtya6b`: rocking all night in the recliner and the fear of falling asleep there.
- `sleeptrain-1wu1a09`: "contact sleeping on the recliner".
- `toddlers-1wtibnj`: "really depressing", "miserable having a child".
- `NewParents-1wtziuw`: lines about never wanting children.

## Caution ids (verbatim, usable for research; check before any ad use)

`sb15-0033` (baby moved into the parents' bed out of exhaustion during pregnancy), `sb15-0129` (bringing the baby to bed "out of tiredness"), `sb15-0142` ("my nervous system is shot"), `sb15-0259` (cosleeping while latched all night).

## Continue

Nothing unread in this assignment.
