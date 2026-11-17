# Reddit full reads: reader R10 (keep_core 055–062)

Read on 2026-10-25 under `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1a/chunks.jsonl` (frozen; unit paths relative to this folder). Posts dated 2026-09-17 to 2026-09-21; OP replies run to 2026-10-06.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1a-keep_core-055` … `-062`) |
| units in those chunks | 133 |
| units read in full (post + every OP reply archived in the unit) | 133 |
| units excluded (line not to cross) | 3 (below) |
| units read, no quote taken (other reasons) | 6 (below) |
| units quoted | 124 |
| quotes written | 278 (`voice/reddit-r10.jsonl`, ids `sb10-0001` … `sb10-0278`) |
| restricted quotes (research only) | 23 (listed in `synthesis/reader-notes-r10.md`) |
| verify | `verify_quotes.py voice/reddit-r10.jsonl` → 278 quotes, 0 failed |

Units per chunk: 055 = 18, 056 = 21, 057 = 14, 058 = 14, 059 = 18, 060 = 14, 061 = 19, 062 = 15. The unit list is in `scratchpad/R10/units.txt`; per-chunk working specs in `scratchpad/R10/c055.jsonl` … `c062.jsonl`.

## Units excluded (read in full, nothing quoted)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1wjpp01.txt` | safe-sleep set-up question (bed-sharing with a toddler in hotels) |
| `../_shared/_raw/reddit-2026/units/NewParents-1wk5ebm.txt` | safe-sleep incident (newborn chest sleeping; parent considering a non-recommended position) |
| `../_shared/_raw/reddit-2026/units/NewParents-1wmal5l.txt` | safe-sleep topic (bed-sharing with a baby who has just started rolling) |

## Units read, no quote taken

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1wjj60s.txt` | short post, nothing beyond a generic "worst night" line |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wkhrtj.txt` | bare early-waking schedule question |
| `../_shared/_raw/reddit-2026/units/Mommit-1wkvx9n.txt` | cross-post of `toddlers-1wkvwii` (quoted there) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wl0p56.txt` | bare nap-schedule question |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1wlg2hm.txt` | cross-post of `beyondthebump-1wlg033` (quoted there) |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1wltf5u.txt` | daytime rolling frustration, generic and next to the safe-sleep line |

## Quoted with care (partial quoting)

- `FirstTimeMom-1wiyukm`: mental-health crisis post (intrusive thoughts, possible PPD). Only the partner's dismissive remark was taken (sb10-0010, restricted); the crisis passage is not copied.
- `ScienceBasedParenting-1wk0t1i`: bed-sharing safety thread. Three restricted quotes on exhaustion (sb10-0100 … 0102); the mattress purchase and safety discussion are not quoted.
- Safe-sleep lines left out of otherwise quoted units: rolling to the belly (`sleeptrain-1wjgpio`, `NewParents-1wjujfy`), newborn chest/sling sleep (`sleeptrain-1wkimp2`), side-lying nursing in bed (`NewParents-1wl72ux`), a blanket in the crib (`sleeptrain-1wlf9bb`, trimmed out of sb10-0198).
- Medical lines noted, not quoted: silent reflux and lansoprazole (`beyondthebumpUK-1wkt6xo` reply), ear infections (`sleeptrain-1wldili`), iron level (`sleeptrain-1wjph0n`).
- Cross-post pairs quoted once: `Mommit-1wjbe66` / `sahm-1wjbi7a` (post quoted from Mommit, replies from sahm), `beyondthebump-1wlg033` / `sleeptrain-1wlg2hm`, `toddlers-1wkvwii` / `Mommit-1wkvx9n`.

## What has and hasn't been read

All 133 units in chunks 055–062 were read in full. Nothing in this assignment is unread.
