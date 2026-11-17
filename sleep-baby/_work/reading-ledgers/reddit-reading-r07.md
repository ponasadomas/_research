# Reddit full reads: reader R07 (keep_core 031–038)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder). Unit list with chunk ids: `scratchpad/R07/units.txt`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_core-031` … `-038`) |
| units in those chunks | 129 |
| units read in full (post + every OP reply archived in the unit) | 129 |
| units excluded | 0 |
| units read, no quote taken | 5 (below) |
| units quoted | 124 |
| quotes written | 321 (`voice/reddit-r07.jsonl`, ids `sb07-0001` … `sb07-0321`) |
| verify | `verify_quotes.py voice/reddit-r07.jsonl` → 321 quotes, 0 failed |

Units per chunk: 031 = 14, 032 = 14, 033 = 16, 034 = 17, 035 = 15, 036 = 17, 037 = 20, 038 = 16.
Ids per chunk: 031 = 0001–0042, 032 = 0043–0090, 033 = 0091–0127, 034 = 0128–0168, 035 = 0169–0206, 036 = 0207–0244, 037 = 0245–0281, 038 = 0282–0321.

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1wakfqb.txt` | cross-post, same text as `sleeptrain-1wakdy5` (quoted there) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wazwmh.txt` | cross-post, same text as `NewParents-1wayryz` (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wbc4wz.txt` | cross-post, same text as `NewParents-1wbbw3t` (quoted there) |
| `../_shared/_raw/reddit-2026/units/Mommit-1wbqlci.txt` | cross-post, same text as `toddlers-1wbqxb6` (quoted there) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wbb9k5.txt` | technical nap-transition schedule question, nothing beyond numbers |

`NewParents-1wa6wza` is a cross-post of `beyondthebump-1wa6pwz`; only its unique OP reply was quoted (sb07-0123).

## Safe-sleep incidents and infant-death fears (recorded, not quoted)

Units stay in; only these passages were skipped.

- `sleeptrain-1w9dc9k`: baby placed to sleep on his belly / side by preference. Not quoted.
- `Mommit-1w9s9mi`: baby fell off the bed during a nappy change the week before. Not quoted; the partner-conflict lines from the same post are quoted (sb07-0088 to -0090).
- `sleeptrain-1w9pc54`: bedsharing "safe sleep 7", checking breathing, fear of the baby rolling off the bed as the reason to start Ferber. Only the guilt lines quoted.
- `beyondthebump-1wa46ob`: mother falling asleep while burping the baby. Not quoted (dozing while holding the baby).
- `sleeptrain-1wado1k`, `sleeptrain-1wbjwpm`, `NewParents-1wayryz`: side-nursing / cosleeping "just to survive", baby sleeping on the parent. Only the survival framing quoted, no sleep-position detail.
- `NewParents-1wabshb` replies: "unable to cosleep safely because we have dogs". Not quoted.
- `sleeptrain-1wb66m1` replies `p8pwixa`, `p8q7tcw`, `p8qcj62`: toddler falls asleep face-down hunched over his legs during crying it out; parent "worried he can't breathe". Not quoted.
- `beyondthebump-1wb9miv`: family dispute over a shared bassinet and how long babies may sleep in one. Not quoted beyond the crib-transfer line (sb07-0234).
- `sleeptrain-1wbe72m`: 11-week-old sleeps only in the adult bed or on the couch; nurse-mother "so anxious about safe sleep". Not quoted.
- `beyondthebump-1wbnpvq`: fear of "accidentally" sleeping "somewhere unsafe" with a 2-week-old. Not quoted.
- `sleeptrain-1wbrknv`: "so tired that there's going to be an accident"; reply on cosleeping a first child for 9 months "because I was so scared of SIDS". Not quoted.
- `sleeptrain-1w9vyio`: 14-month-old slept on the parent from 5am to 7am after graduated extinction. Quoted (sb07-0094) because the child is past infancy and no parent dozing is described; judged not a safe-sleep incident.
- `beyondthebump-1wc79r5` reply `p8vzika`: "scared to fall asleep" if cosleeping. Not quoted.

## Restricted quotes (in `voice/`, research only, never ads)

- sb07-0173: parent describes rage, yelling at and smacking a 15-month-old after a 90-minute bedtime.
- sb07-0224: husband "prone to falling asleep behind the wheel" from broken nights (drowsy driving).
- sb07-0025: "How many days of this before I end up in the mental hospital?" (mental-health wording; exhaustion research only).
- sb07-0204: "absolutely HATE cosleeping, from fear and discomfort" (safe-sleep fear).

Medical detail (reflux, CMPA, eczema, sleep apnoea, congestion, teething medicine) is kept to context lines and never given as a cause.

## How to continue

Nothing in this slice is unread. Do not re-run R07 or append to `voice/reddit-r07.jsonl`; a new reader takes a new prefix.
