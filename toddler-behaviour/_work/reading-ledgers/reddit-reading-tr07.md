# Reddit full reads — TR07 (toddler-behaviour, 2026-10-25)

Reader TR07 · id prefix `tb07` · voice file `voice/reddit-tr07.jsonl` · brief `../_shared/_tools/brief-reading.md` · chunks from `_raw/reddit/read-v1/chunks.jsonl`. Scratch and build script: `scratchpad/TR07/` (`spec-039.py` … `spec-046.py` → `build.py`; per-unit status in `units-status.txt`).

## Counts

| step | n |
|---|---|
| chunks assigned | 8 (read-v1-keep_core-039 to 046) |
| units in those chunks | 124 |
| units read in full | 124 (all) |
| units quoted from | 110 |
| units excluded (read in full, nothing copied, line not to cross) | 7 |
| units read, not quoted (duplicate cross-post, restricted with nothing safe to add, or off-topic) | 7 |
| quotes written | 342 (tb07-0001 to tb07-0342) |
| quotes from restricted units (diagnosis / developmental question in the unit) | 54 |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-tr07.jsonl` → 342 quotes, 0 failed |

Counts are counts of quotes chosen, never of people. Speakers: parent_unspecified 151, new_mother 121, experienced_mother 35, partner 35 (no professional or relative_caregiver authors; daycare staff and grandparents appear only as `others_said`).

## Chunks

| chunk | units | quotes |
|---|---|---|
| read-v1-keep_core-039 | 14 | 48 |
| read-v1-keep_core-040 | 16 | 47 |
| read-v1-keep_core-041 | 19 | 51 |
| read-v1-keep_core-042 | 16 | 38 |
| read-v1-keep_core-043 | 14 | 34 |
| read-v1-keep_core-044 | 14 | 41 |
| read-v1-keep_core-045 | 18 | 45 |
| read-v1-keep_core-046 | 13 | 38 |

## Units excluded (read in full, nothing copied)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sahm-1ws8mm3.txt` | child confinement / supervision arrangement (safety) |
| `../_shared/_raw/reddit-2026/units/daddit-1wsrvts.txt` | parent describes a physical act toward the child |
| `../_shared/_raw/reddit-2026/units/Mommit-1wu8bct.txt` | centred on parent's postpartum medical and mental-health treatment; verbal harshness toward the child |
| `../_shared/_raw/reddit-2026/units/toddlers-1wut7ny.txt` | parent describes physical force and verbal harshness toward the child |
| `../_shared/_raw/reddit-2026/units/GentleParenting-1wxd3s7.txt` | parent describes physical force toward the child |
| `../_shared/_raw/reddit-2026/units/NewParents-1wyp4lh.txt` | centred on parent's mental-health diagnosis and treatment |
| `../_shared/_raw/reddit-2026/units/toddlers-1wzkc4n.txt` | child injury and medical care; parent's anxiety disorder |

## Units read, not quoted

| unit | reason |
|---|---|
| `pottytraining-1ws8y4n` | duplicate cross-post of toddlers-1ws8w44 |
| `pottytraining-1wsitaq` | duplicate cross-post of toddlers-1wsgv1w |
| `pottytraining-1wyh0zs` | duplicate cross-post of Mommit-1wybnt4 |
| `toddlers-1wscdk0` | restricted: parent asks about autism evaluation and medical tests |
| `toddlers-1wxanhg` | restricted: father asks whether a speech delay is autism |
| `toddlers-1wu64jz` | bath-time fear after a move; nothing beyond a routine question |
| `Parenting-1wvl32h` | bathing distress, parent asks about sensory issue; nothing safe to add |

## Units quoted in part (a passage left out under the lines not to cross)

Mommit-1wst3cs (stool softeners), toddlers-1wtazjq (child self-injury), toddlers-1wtk0vm (yelling), toddlers-1wuok9p (raised voice), toddlers-1wvbptm (parent's cancer treatment), toddlers-1wvztw3 (screaming at child), NewParents-1wvxkjn (relative's medical guess), pottytraining-1wwfeer (threat), Mommit-1wwrnot (another parent's forced feeding), NewParents-1wwup2q (medication), pottytraining-1www285 (cold-shower punishment urged by relatives; suppositories), Mommit-1wxjhbk (carrying the child out), toddlers-1wxrprh (stool softener), Parenting-1wxu5m2 (partner's depression), toddlers-1wyg4n3 (spanking thought; head-banging), ScienceBasedParenting-1wyocf0 (name-calling of the child), pottytraining-1wyv95d (laxative), AttachmentParenting-1wz7u41 (OT referral; animal harm), toddlers-1wzitwd (injury to the newborn), AttachmentParenting-1wzf1is (parent's mental health), toddlers-1wyqm2s (dental advice), plus the restricted units listed in the reader notes.

## How to continue

Nothing in these chunks is unread. To rebuild the voice file from the specs: `python3 -I scratchpad/TR07/build.py` (overwrites `voice/reddit-tr07.jsonl` with the same ids in the same order), then verify.
