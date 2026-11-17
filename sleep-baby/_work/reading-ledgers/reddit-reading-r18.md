# Reddit full reads — reader R18 (2026-10-25)

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1b/chunks.jsonl` (second chunk set). Voice file: `voice/reddit-r18.jsonl` (ids `sb18-0001`–`sb18-0384`). Notes: `synthesis/reader-notes-r18.md`. Scratch (per-chunk builder scripts, unit list, exclusion log, id index): `scratchpad/R18/`.

## Counts

| step | n |
|---|---|
| chunks assigned | 8 (`read-v1b-keep_core-029` to `read-v1b-keep_core-036`) |
| units in them | 127 (029: 17, 030: 17, 031: 16, 032: 15, 033: 15, 034: 16, 035: 17, 036: 14) |
| units read in full | 127 |
| units excluded (line not to cross, nothing quoted) | 8 |
| units read, no quote (cross-post / medical) | 4 |
| units quoted | 115 |
| quotes written | 384 |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-r18.jsonl` → 384 quotes, 0 failed |

None of these 127 units was quoted by an earlier reader (checked each `raw_file` against every `voice/*.jsonl` before reading). Ids checked unique on disk.

## Excluded units (read in full, nothing quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1x2qq2m.txt` | newborn sleeping on a parent's chest; safe-sleep |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1x2rs3u.txt` | cot incident with the baby stuck face-down; safe-sleep |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1x2wpcg.txt` | post is about a bedsharing set-up |
| `../_shared/_raw/reddit-2026/units/toddlers-1x36utj.txt` | question about an item in the crib; safe-sleep |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1x3qt5w.txt` | postpartum-depression and crisis wording |
| `../_shared/_raw/reddit-2026/units/toddlers-1x4ijmm.txt` | fall from a crib, door lock on a toddler's room, cardiac-anxiety wording |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1x4oi07.txt` | parent asleep beside the baby with a phone under its head; safe-sleep incident |
| `../_shared/_raw/reddit-2026/units/Mommit-1x4u4vu.txt` | post is about bedsharing with a child |

## Read, no quote

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/Mommit-1x40bsg.txt` | cross-post of `sleeptrain-1x3yc8z` (quoted there) |
| `../_shared/_raw/reddit-2026/units/NewParents-1x4c5ua.txt` | cross-post of `sleeptrain-1x4az9c` (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1x571kw.txt` | cross-post of `NewParents-1x570bf` (quoted there) |
| `../_shared/_raw/reddit-2026/units/Mommit-1x5dzg9.txt` | acute feeding refusal with an allergy history; medical, sleep secondary |

## Partly quoted units (passages left out, neutral reasons)

- Bedsharing / cosleeping / safe-sleep detail left out: `sleeptrain-1x2c19u`, `sleeptrain-1x2muw8`, `NewParents-1x2sczf`, `sleeptrain-1x2whdg`, `Mommit-1x39ogo` (dozing in a glider, floor cosleeping, suffocation fear), `NewParents-1x3d4y2`, `sleeptrain-1x3ddtg`, `sleeptrain-1x3im6b`, `sleeptrain-1x3jd85`, `toddlers-1x3lx0g`, `sahm-1x3m9lb`, `AttachmentParenting-1x3n586`, `AttachmentParenting-1x3pd8w`, `sleeptrain-1x3q5j4`, `AttachmentParenting-1x3sgqz` (rolling-over and suffocation fear), `sleeptrain-1x3t9o3`, `sleeptrain-1x3yc8z`, `sleeptrain-1x3yinp`, `sleeptrain-1x3ys8w`, `sleeptrain-1x41wz2`, `sleeptrain-1x44lgi`, `sleeptrain-1x45k7j`, `sleeptrain-1x4845c`, `sleeptrain-1x4az9c`, `sleeptrain-1x4ebmn`, `sleeptrain-1x4imyz`, `sleeptrain-1x4pk6b`, `sleeptrain-1x4r8gn`, `Parenting-1x4uu4g`, `NewParents-1x4whdc`, `beyondthebump-1x5700m`, `sleeptrain-1x58rwl`, `sleeptrain-1x51gom`.
- Unsafe items or positions left out: `beyondthebump-1x2chn5` (heating pad), `sleeptrain-1x2dxhk` (stomach sleeping), `NewParents-1x48t21` (heating pad, blanket in bassinet), `beyondthebump-1x4z6r6` (tummy sleeping on chest / pillow), `AttachmentParenting-1x2ua8v` (adult in crib), `AttachmentParenting-1x2wk68` (sleeping in a rocking chair), `sleeptrain-1x4h1js` (holding the baby asleep all night), rolling-to-tummy detail kept out in `FirstTimeMom-1x4g4oo` and `sleeptrain-1x4h1js`.
- Injury or fall left out: `toddlers-1x3esk0` (climbing out of crib), `NewParents-1x48g8o` (head on bars), `sleeptrain-1x4yv8h` (head on rails), `sleeptrain-1x5dvee` (hand caught in crib), `NewParents-1x4whdc` (choking scare).
- Distress images left out: `sleeptrain-1x2h0ln` (baby lost voice; parent asleep during a feed), `sleeptrain-1x4ebmn` (hoarse voice), `toddlers-1x3xcyh` (hyperventilating), `NewParents-1x4ecyb` (crying until gagging).
- Mental-health wording left out: `beyondthebump-1x2chn5`, `beyondthebump-1x3qjkc` (breakdown, spiralling, resenting the child), `beyondthebumpUK-1x3qe40`, `sleeptrain-1x3wqsc`, `sleeptrain-1x45lbs` (feeding-anxiety diagnoses), `sleeptrain-1x4ib9p` (panic attack), `sleeptrain-1x4iktz` (postpartum anxiety), `NewParents-1x4l8f7`, `Mommit-1x5682t` (postpartum spiral), `NewParents-1x570bf` ("want to scream").
- Harshness toward a child left out: `NewParents-1x40uf4` (nearly raised voice), `Mommit-1x5682t` (raised voice), `sleeptrain-1x58rwl` (anger toward the baby), `sahm-1x3m9lb` (hostile thread with force wording; only the night-load reply quoted).
- A child's diagnosis left out: `sahm-1x3m9lb` (autism evaluation), `sleeptrain-1x51gom` (anxiety / OCD / therapy).

## How to continue

Nothing in this chunk set is left unread. Do not re-run R18 (it appends to `voice/reddit-r18.jsonl`).
