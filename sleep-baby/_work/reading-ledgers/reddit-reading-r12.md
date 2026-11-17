# Reddit full reads: reader R12 (keep_core 071–074)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder).

## Counts

| step | count |
|---|---|
| chunks assigned | 4 (`read-v1a-keep_core-071` … `-074`) |
| units in those chunks | 70 |
| units read in full (post + every OP reply archived in the unit) | 70 |
| units excluded | 1 (below) |
| units read, no quote taken | 1 (below) |
| units quoted | 68 |
| quotes written | 220 (`voice/reddit-r12.jsonl`, ids `sb12-0001` … `sb12-0220`) |
| verify | `verify_quotes.py voice/reddit-r12.jsonl` → 220 quotes, 0 failed |

Units per chunk: 071 = 18, 072 = 18, 073 = 21, 074 = 13.

Speakers (counts of quotes chosen, not of people): parent_unspecified 117, new_mother 54, experienced_mother 29, partner 20 (fathers in r/daddit: `1wq99u4`, `1wt8f67`, `1wvl86l`, `1wward4`, `1wytrl8`). `sleeptrain-1wzqyic` reads as if written by the father ("this 'I need daddy' phase") but never says so, so it is `parent_unspecified`. Mothers are tagged only where the author says mum/mom/mama, or says they breastfeed or pump.

## Units excluded

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1wrf610.txt` | medical (reflux) and safe-sleep positioning; the replies are about whether a sleep product is safe. Not quoted. |

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wzl25l.txt` | routine nap-timing check for a 22-month-old, no scene or pain beyond the schedule |

## Passages read but deliberately not quoted (lines not to cross)

The rest of each unit was used; only these passages were left out.

- `NewParents-1wqacg1`: a sentence about the safety of the cosleeping setup (safe-sleep).
- `NewParents-1wq8qie`: the bed-sharing safety detail and monitor-sock line (safe-sleep).
- `daddit-1wward4`: the father's lines about his feelings towards the newborn and fear of not making it (mental-health crisis wording).
- `daddit-1wt8f67`: the punishment scene itself (leaving a 3-year-old in the dark). Only his "three choices" reflection is quoted (sb12-0039).
- `daddit-1wvl86l`: the line where he blows up at his wife and daughter, and his name-calling of the 2-year-old.
- `toddlers-1x0d5sw`: the bullet about the child being forced back to bed (physical handling).
- `sleeptrain-1wz22a7`, `sleeptrain-1wzurf5`, `sleeptrain-1wzr88o`: lines about rolling, being strapped into a bassinet and bed-sharing falls (safe-sleep).
- `sleeptrain-1wyavk3` (NICU trauma wording), `sleeptrain-1wzdsid` / `NewParents-1wrm7kt` (PPA mentions): not quoted.
- Medical detail (reflux, rice cereal in a bottle on paediatrician advice, Tylenol, honey, allergy medicine, ER visits for bronchiolitis/croup, pink eye) is left out or kept to context lines, never given as a cause. One Tylenol mention stays inside a list of things tried (sb12-0089).

## How to continue

Nothing is left unread in these four chunks. Do not re-run this reader; it would append to `voice/reddit-r12.jsonl`. Scratch files (batch inputs and the append script) are in `scratchpad/R12/`.
