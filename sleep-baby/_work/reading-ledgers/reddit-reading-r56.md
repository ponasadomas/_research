# Reddit reading ledger — R56 (wave 3, keep_core 106–114)

Reader R56, id prefix `sb56`, voice file `voice/reddit-r56.jsonl`. Brief: `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` → `../_shared/_tools/brief-reading.md`.

| step | count |
|---|---|
| chunks assigned | 9 (`read-w3-keep_core-106` … `read-w3-keep_core-114`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in those chunks | 150 |
| units read in full (post + every OP reply in the unit) | 150 |
| units excluded entirely (neutral reason below) | 4 |
| cross-posts read in full, not quoted (the twin was quoted) | 4 |
| read in full, nothing quotable for this niche | 1 |
| units quoted | 141 |
| quotes written | 495 (`sb56-0001` … `sb56-0495`, ids unique) |
| restricted quotes | 13 (listed in `synthesis/reader-notes-r56.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-r56.jsonl` → 495 quotes, 0 failed |

Posts are dated 19–22 May 2026; OP replies run to 21 September 2026.

## Units excluded entirely

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sahm-1ti5x95.txt` | mental-health crisis wording and a parent's verbal harshness; baby sleep is a passing mention |
| `../_shared/_raw/reddit-2026/units/ScienceBasedParenting-1tiy3z6.txt` | sleep-space product safety question; a partner's mental-health detail |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tj802e.txt` | safe-sleep detail (baby rolling to stomach in the cot) |
| `../_shared/_raw/reddit-2026/units/NewParents-1tjhvdi.txt` | safe-sleep detail (long naps in a car-seat stroller) |

## Read in full, not quoted

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1thaapd.txt` | cross-post of `sleeptrain-1tha6y0` (same author) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1thbral.txt` | cross-post of `Parenting-1thbmcg` |
| `../_shared/_raw/reddit-2026/units/Parenting-1tinx51.txt` | cross-post of `sleeptrain-1tinyix` |
| `../_shared/_raw/reddit-2026/units/NewParents-1tkcypf.txt` | cross-post of `Parenting-1tkctab` |
| `../_shared/_raw/reddit-2026/units/NewParents-1tj3fpa.txt` | flight seating and car-seat logistics; no sleep problem stated |

## Passages left out of quoted units (neutral reasons)

Quote-level restriction was used: a unit with one unsafe line still gave quotes, and the line itself was not copied.

- Bedsharing / cosleeping / overnight chest-sleeping detail not quoted in: `AttachmentParenting-1thc7xj`, `sleeptrain-1thkqz9`, `sleeptrain-1thsq3d`, `sleeptrain-1thx59j`, `sleeptrain-1ti0s75`, `NewParents-1ticwl0`, `sleeptrain-1tiecpz`, `AttachmentParenting-1tie8mw`, `beyondthebumpUK-1tii3b1`, `beyondthebump-1tim3h6`, `sleeptrain-1tj07h5`, `toddlers-1tj30ei`, `beyondthebump-1tj54kc`, `beyondthebump-1tj6jg8`, `sleeptrain-1tjf0vt`, `sleeptrain-1tjgaur`, `sleeptrain-1tjnx2s`, `sleeptrain-1tjkn4e`, `NewParents-1tjrmx9`, `sleeptrain-1tk2z0i`, `beyondthebump-1tk3p44`, `sleeptrain-1tk3v07`, `NewParents-1tk3t78`, `Parenting-1tkctab`, `NewParents-1tke1co`, `NewParents-1tkeuk3`, `AttachmentParenting-1tkjlvj`.
- Other safe-sleep detail (parent falling asleep while feeding, sleeping position, swing/car-seat sleep, belly sleeping, sleep-space weight limits, SIDS, injury in the cot) not quoted in: `sleeptrain-1thvyfu`, `sleeptrain-1thz5bh`, `NewParents-1tijxs2`, `sleeptrain-1tijyvh`, `NewParents-1tis935` (only a babysitter remark quoted), `sleeptrain-1tiyw70`, `sleeptrain-1tjq60o` (one neutral line quoted), `NewParents-1tj9tp0`, `sleeptrain-1tiz8zz` (room-sharing guidance).
- Parent's verbal harshness / snapping not quoted in: `AttachmentParenting-1thbh0f`, `toddlers-1tj30ei`.
- Mental-health crisis or named-condition wording, medication and medical detail not quoted in: `sleeptrain-1thh8hg`, `Mommit-1thi0wr`, `NewParents-1thk9ra`, `sleeptrain-1tiadq5`, `beyondthebumpUK-1tibszz`, `NewParents-1tie624`, `beyondthebump-1tilxzg`, `Parenting-1tinaj8`, `sleeptrain-1tiz8zz`, `Mommit-1tjd2hw`, `beyondthebump-1tjwivp`, `sleeptrain-1tk76hb`, `NewParents-1tk89eh`, `NewParents-1tki3y6`.
- Drowsy-driving worry (`beyondthebump-1tim3h6`), a door-locking idea (`toddlers-1tjrvlg`), a child's first name (`sleeptrain-1tk78dp`) and a hyperbolic "kill me" line (`toddlers-1tk4jpv`) not quoted.

## Not done

Nothing unread in this assignment.
