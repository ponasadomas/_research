# Reddit reading ledger — PR19 (pregnancy-birth, read-v1)

Date 2026-10-25. Reader PR19, id prefix `pb19`. Brief: `../../_shared/_tools/brief-reading.md`. Voice file: `../voice/reddit-pr19.jsonl`. Notes: `../synthesis/reader-notes-pr19.md`. Scratch: `../scratchpad/PR19/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1-keep_core-112` → `119`) |
| units in chunks | 136 |
| units read in full | 136 |
| units excluded (README / brief lines) | 28 (one of them a crosspost) |
| units read, no quote taken | 6 |
| units quoted | 102 |
| quotes written | 257 (ids pb19-0001 → pb19-0263; 0076–0078 and 0168–0170 unused after two units were moved to excluded) |
| restricted quotes (quote level) | 26 |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr19.jsonl` → 257 quotes, 0 failed |

Posts date from 12 to 15 Oct 2026 (OP replies to 22 Oct). Subs: r/pregnant, r/BabyBumps, r/PregnancyUK, r/beyondthebump, r/beyondthebumpUK, r/FirstTimeMom, r/NewParents, r/Mommit. Nothing left unread.

## Excluded units (neutral reasons)

| unit | reason |
|---|---|
| `PregnancyUK-1x45w0a` | centred on a serious scan finding and fear of loss |
| `pregnant-1x48y0f` | centred on an early scan finding and fear of loss |
| `beyondthebumpUK-1x4ez8s` | crisis wording |
| `pregnant-1x4inkd` | substance use |
| `FirstTimeMom-1x4jfjk` | centred on a serious scan finding |
| `pregnant-1x4nv71` | acute medical episode (bleeding, emergency visit) |
| `PregnancyUK-1x4s1yo` | centred on whether to continue a pregnancy |
| `pregnant-1x4xztu` | centred on a decision to end a pregnancy |
| `BabyBumps-1x4zegh` | centred on a screening result |
| `pregnant-1x5aobh` | sexual assault disclosure and partner coercion |
| `pregnant-1x5g7pg` | substance use |
| `pregnant-1x5hxqd` | centred on a medical condition and lab results |
| `pregnant-1x5oev8` | acute medical emergency (emergency-room visit) |
| `pregnant-1x5qn02` | centred on a scan finding |
| `FirstTimeMom-1x5snya` | family aggression and housing instability |
| `pregnant-1x5v0xj` | centred on a screening result |
| `pregnant-1x5yelt` | centred on mental-health medication |
| `BabyBumps-1x5yfqf` | crosspost of pregnant-1x5yelt; centred on mental-health medication |
| `PregnancyUK-1x616ko` | centred on a screening result |
| `pregnant-1x62nn6` | acute medical emergency |
| `pregnant-1x63trm` | centred on medical complications and bereavement |
| `pregnant-1x6a1ua` | centred on mental-health medication and a very early previous birth |
| `pregnant-1x6cmn3` | centred on screening findings |
| `pregnant-1x6ej83` | centred on a medical condition test |
| `pregnant-1x6fe4z` | centred on whether to continue a pregnancy |
| `BabyBumps-1x6lwy3` | centred on a medical condition with emergency visits |
| `PregnancyUK-1x4qtgl` | substance use (alcohol in pregnancy) |
| `pregnant-1x5lyc5` | safety concern about the newborn (pet aggression) |

## Read, no quote taken

| unit | reason |
|---|---|
| `pregnant-1x4nyhd` | centred on a medication-safety question |
| `pregnant-1x58quy` | centred on an intimate medical symptom |
| `pregnant-1x5q1r5` | centred on a breakup dispute; no on-niche lines |
| `pregnant-1x68znj` | labour-symptom question; update describes an emergency visit |
| `pregnant-1x6e50w` | medication question |
| `PregnancyUK-1x6gh03` | waiting on a screening result; no on-niche lines |

## Crossposts, reposts and flagged posts

- `BabyBumps-1x5yfqf` is the same text as `pregnant-1x5yelt` (both excluded).
- `pregnant-1x5txpj`: author says it is reposted from another sub (one restricted quote, pb19-0183).
- Flagged as possibly AI-polished, engagement or rage-bait (quoted with the flag in the context line, not to be counted as independent): `pregnant-1x4qi7x`, `BabyBumps-1x502l9`, `pregnant-1x59s43`, `pregnant-1x59tsw`, `pregnant-1x5zyp4`.
- No "Nurava" / "@nuravaa" or other brand-seeded post in these chunks.

## How to continue

Nothing is unread. Never re-run this reader on the same voice file (ids would collide); a new pass takes a new prefix.
