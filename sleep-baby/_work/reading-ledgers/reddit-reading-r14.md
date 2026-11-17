# Reddit full reads — reader R14 (2026-10-25)

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1b/chunks.jsonl` (second chunk set). Voice file: `voice/reddit-r14.jsonl` (ids `sb14-0001`–`sb14-0253`). Notes: `synthesis/reader-notes-r14.md`. Scratch (builder scripts, unit list): `scratchpad/R14/`.

## Counts

| step | n |
|---|---|
| chunks assigned | 8 (`read-v1b-keep_success-003`, `read-v1b-keep_otherside-001`–`003`, `read-v1b-keep_core-001`–`004`) |
| units in them | 104 (success-003: 2, otherside-001: 13, otherside-002: 13, otherside-003: 12, core-001: 10, core-002: 19, core-003: 18, core-004: 17) |
| units read in full | 104 |
| units excluded (line not to cross, nothing quoted) | 6 |
| units read, no quote (duplicate / nothing extractable) | 2 |
| units quoted | 96 |
| quotes written | 253 |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-r14.jsonl` → 253 quotes, 0 failed |

None of these 104 units was quoted by an earlier reader (checked `raw_file` against all `voice/*.jsonl` before reading).

## Excluded units (read in full, nothing quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1wyeyva.txt` | third-party account with a medical-emergency history, a parent's mental-health diagnosis and chest-cosleeping detail |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wyf8qj.txt` | cross-post of the unit above (same text, same reasons) |
| `../_shared/_raw/reddit-2026/units/sahm-1xdqj43.txt` | sustained stress / physical-symptom / "breaking point" wording |
| `../_shared/_raw/reddit-2026/units/NewParents-1xeaf94.txt` | infant overheating and safe-sleep wording |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1wr1ed0.txt` | mental-health crisis wording |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1wr50kz.txt` | unsafe-sleep set-up and infant-death wording; psychiatric history |

## Read, no quote

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/Parenting-1wpgthh.txt` | cross-post of `toddlers-1wpgop1` (quoted there) |
| `../_shared/_raw/reddit-2026/units/Parenting-1wqfs8o.txt` | single night-terror episode; medical-adjacent, no ask beyond it |

## Partly quoted units (passages left out)

- `FirstTimeMom-1wtdhm8`: grandmother letting the newborn sleep on her chest left out; only schedule and night-shift lines quoted (sb14-0017–0022).
- `NewParents-1x3il0i`: bedsharing-safety passages left out; values lines quoted (sb14-0067, 0068).
- `Mommit-1wqfiov`: parent's fear of harming the baby while feeding left out (sb14-0212–0214).
- `sleeptrain-1wq9vwk`: breath-holding spells left out; only the Owlet line quoted (sb14-0201).
- `sleeptrain-1wq5f45`, `sleeptrain-1xe3cw8`, `beyondthebump-1wpifnt`, `beyondthebumpUK-1wph47q`, `NewParents-1x46ift`, `sleeptrain-1wqfwub`: mental-health clauses trimmed or not quoted.

## Unit list by chunk

Every unit below was read in full; the per-chunk list is in `scratchpad/R14/units.tsv`.

## How to continue

Nothing left unread in this assignment. Do not re-run this reader: `voice/reddit-r14.jsonl` is final; add restrictions in `synthesis/restricted-ids.md`.
