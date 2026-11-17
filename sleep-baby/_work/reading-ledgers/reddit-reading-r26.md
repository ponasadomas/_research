# Reddit reading ledger — R26 (prefix sb26), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md` with `../_shared/_tools/prompt-sleep-baby-reader-w2.txt`. Corpus: `_raw/reddit/read-w2/chunks.jsonl` (wave 2, posts 2026-06-25 → 2026-08-24). Voice file: `voice/reddit-r26.jsonl`. Scratch: `scratchpad/R26/` (unit list `units.txt`, per-chunk record specs `q014.jsonl` … `q021.jsonl`, exclusion log `excluded.txt`, restricted list `restricted.txt`, id map `idmap.txt`, builder `build.py`). The voice file is regenerated from the spec files by `build.py` (ids are assigned in spec order); the voice file is the record. Do not reorder the spec files.

## Counts

| step | count |
|---|---|
| chunks assigned | 8: `read-w2-keep_core-014` … `read-w2-keep_core-021` |
| units in those chunks | 137 (16 / 20 / 17 / 16 / 17 / 16 / 20 / 15) |
| units read in full (post + every OP reply in the unit) | 137 |
| units excluded entirely | 7 |
| units read, not quoted (other than exclusions) | 0 |
| units with passages left out (rest quoted) | 89 (listed below) |
| units quoted | 130 |
| quotes written | 447 (sb26-0001 … sb26-0447), `verify_quotes.py` 0 failed, ids unique |
| restricted quotes | 10 (listed in `synthesis/reader-notes-r26.md`) |

Counts are of quotes chosen, never of people. Posts span 2026-07-01 to 2026-07-04 (all core chunks); OP replies run to 2026-09-14.

Same-author pairs (not double-counted as separate voices): `NewParents-1uk9os2` and `sleeptrain-1uljr29` (same baby details a day apart, different subs); `sleeptrain-1umcskh` and `sleeptrain-1umdqzy` (author says she deleted and reposted); `Mommit-1um6jim` and `NewParents-1um6nk3` (identical cross-post, both excluded).

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `NewParents-1ul7zt2` | core-016 | safe-sleep detail (infant sleep position) and medical follow-up throughout |
| `toddlers-1ult75k` | core-017 | excluded under the brief's rule on harshness toward a child |
| `sleeptrain-1um15y0` | core-018 | safe-sleep detail (swaddling a rolling infant) throughout |
| `Mommit-1um6jim` | core-018 | safe-sleep detail (infant sleep position, prematurity) throughout |
| `NewParents-1um6nk3` | core-018 | cross-post of Mommit-1um6jim; safe-sleep detail throughout |
| `beyondthebump-1umcn5f` | core-019 | safe-sleep detail (cosleeping bedding, face covering) throughout |
| `NewParents-1unawhe` | core-021 | excluded under the brief's rule on force or harshness toward a child (urges) |

## Units with passages left out (rest of unit quoted)

| unit | chunk | left out |
|---|---|---|
| `NewParents-1uk9os2` | core-014 | mental-health condition wording and feeding/medical details left out |
| `sleeptrain-1ukar8q` | core-014 | road-safety incident sentence left out; 4-year-old bedtime scene out of age range |
| `sleeptrain-1ukc48z` | core-014 | cosleeping sentence left out (safe-sleep detail) |
| `beyondthebump-1ukdcgx` | core-014 | cosleeping/anxiety sentence left out |
| `sleeptrain-1ukdw26` | core-014 | cosleeping sentence left out |
| `toddlers-1ukfptl` | core-014 | bedsharing and supplement passages left out |
| `sleeptrain-1ukglp1` | core-014 | bringing toddler into parents' bed left out |
| `beyondthebump-1ukk691` | core-014 | off-topic relationship passages left out |
| `beyondthebump-1ukkcq7` | core-014 | mental-health conditions, family crisis, medical check and sleep-object detail left out |
| `sleeptrain-1ukl3fl` | core-014 | medication passages left out |
| `NewParents-1uklax3` | core-015 | feeding, weight and paediatric visit details left out (medical) |
| `sleeptrain-1uknbkc` | core-015 | bedsharing and side-lying feeding passages left out |
| `Mommit-1ukng9t` | core-015 | parent not hearing a toddler at night left out (safety-adjacent) |
| `sleeptrain-1uknk0b` | core-015 | bringing baby into parents' bed left out |
| `NewParents-1ukockz` | core-015 | arms-up swaddle and rolling comment left out (sleepwear near rolling) |
| `sleeptrain-1ukpnio` | core-015 | bedsharing after night feed left out |
| `NewParents-1ukpo5l` | core-015 | cosleeping passage left out |
| `sleeptrain-1ukpsuy` | core-015 | cosleeping background left out |
| `sleeptrain-1ukw6rl` | core-015 | cosleeping and sleeping beside parent left out |
| `sleeptrain-1ukyk5e` | core-015 | room heater detail left out (safe-sleep) |
| `FirstTimeMom-1ukyt2p` | core-015 | feeding/tongue-tie comment left out (medical) |
| `Parenting-1ul00av` | core-015 | mental-health wording, cosleeping and road-trip detail left out |
| `NewParents-1ul3897` | core-015 | medication, bloodwork and doctor passages left out |
| `sleeptrain-1ul3org` | core-016 | bedsharing, supplement-food and crib-biting passages left out |
| `AttachmentParenting-1ul6yyd` | core-016 | baby-nest detail left out |
| `toddlers-1ul9snv` | core-016 | room-locking, hyperventilating and bedsharing passages left out |
| `daddit-1ula7xd` | core-016 | mental-health support, fertility treatment and weighted sleepwear passages left out |
| `sleeptrain-1ulc8qd` | core-016 | medication and illness passages left out |
| `sleeptrain-1ulg9ws` | core-016 | supplement given to a toddler left out (rest quoted) |
| `sleeptrain-1ulgfdu` | core-016 | doctor visit and medication left out |
| `toddlers-1ulgnrx` | core-016 | neurodivergence mention left out |
| `sleeptrain-1ulex7k` | core-016 | cosleeping sentence left out |
| `NewParents-1uli1to` | core-016 | bedsharing passages left out |
| `AttachmentParenting-1ulim8k` | core-016 | medical conditions, mental-health wording, feeding/weight and cosleeping left out |
| `sleeptrain-1uljr29` | core-017 | feeding-related medical conditions and medication left out |
| `sleeptrain-1ull3u1` | core-017 | cosleeping passage left out |
| `Parenting-1ull7lz` | core-017 | bedsharing and sidecar-crib passages left out |
| `sleeptrain-1ullsq6` | core-017 | teething/illness speculation left out |
| `sleeptrain-1uloncq` | core-017 | head-hitting-in-crib detail left out |
| `NewParents-1ulp2sq` | core-017 | fan placement left out |
| `sleeptrain-1ulqk6d` | core-017 | "feeling like I'm dying" line, growth/weight replies and cosleeping reply left out |
| `NewParents-1ultt14` | core-017 | cosleeping and regret-having-a-child lines left out |
| `NewParents-1ulwa8x` | core-017 | injury-prevention product passage left out |
| `sleeptrain-1ulymm5` | core-017 | rolling-to-belly detail left out |
| `NewParents-1ulzw3v` | core-018 | floor-bed and fall-risk setup passages left out (one restricted price quote kept) |
| `sleeptrain-1ulzwu8` | core-018 | parent's past severe symptoms of sleep deprivation, bedsharing and child's night fears left out |
| `AttachmentParenting-1um2g2l` | core-018 | sidecar-crib detail left out |
| `sleeptrain-1um48z9` | core-018 | cosleeping and anxiety wording left out |
| `sleeptrain-1um4nys` | core-018 | cosleeping passage left out |
| `sleeptrain-1um4vk0` | core-018 | illness and bedsharing passages left out |
| `NewParents-1um65ce` | core-018 | mental-health wording left out |
| `sleeptrain-1um6wyh` | core-018 | paediatric check left out |
| `NewParents-1um85tb` | core-018 | bedsharing passages left out |
| `beyondthebump-1um9sqc` | core-018 | cosleeping setup, postpartum health and crisis-adjacent wording left out |
| `NewParents-1um9tnc` | core-019 | mental-health condition wording and supply details left out |
| `NewParents-1umajsw` | core-019 | parent's anger passage left out |
| `NewParents-1umbnek` | core-019 | mental-health framing, reflux and feeding/weight passages left out |
| `sleeptrain-1umbtcc` | core-019 | illness, body check and bedsharing passages left out |
| `beyondthebump-1umc1rt` | core-019 | childhood-background and gas-remedy passages left out |
| `sleeptrain-1umcskh` | core-019 | breath-holding/medical passage left out |
| `beyondthebump-1umcx0i` | core-019 | bedsharing passage left out |
| `AttachmentParenting-1ume1xb` | core-019 | cosleeping background left out |
| `FirstTimeMom-1umezph` | core-019 | bedsharing passage left out |
| `sleeptrain-1umf3mf` | core-019 | parent and baby asleep in a rocking chair left out (safe-sleep) |
| `NewParents-1umfc7w` | core-019 | sleep sack on a play mat with a rolling baby left out |
| `NewParents-1umgiaf` | core-019 | list of medical/therapy professionals left out |
| `sleeptrain-1umjprq` | core-020 | cosleeping option left out |
| `sleeptrain-1umllph` | core-020 | pacifier-and-rolling detail and medication mention left out |
| `sleeptrain-1umlyqv` | core-020 | nursing-while-asleep-in-arms detail left out |
| `NewParents-1umm0iw` | core-020 | floor-bed reply left out |
| `sleeptrain-1umnhqe` | core-020 | cosleeping and surgery passages left out |
| `sleeptrain-1umnyq7` | core-020 | medication passage left out |
| `toddlers-1umo6t5` | core-020 | toileting passage left out |
| `sleeptrain-1umpyx0` | core-020 | room temperature during heatwave left out (sleep-environment safety) |
| `Mommit-1umvu94` | core-020 | child hitting/kicking the parent left out |
| `toddlers-1umy8u4` | core-020 | medical (digestive, medication, parent condition) and accidental cosleeping passages left out |
| `sleeptrain-1umzhq8` | core-020 | side-lying nursing and bedsharing passages, "breaking point" wording left out |
| `sleeptrain-1un00fe` | core-021 | mental-health and nervous-system wording, cosleeping attempt left out |
| `sleeptrain-1un20mm` | core-021 | medication passages left out |
| `sleeptrain-1un2yfr` | core-021 | dry-heaving detail left out |
| `NewParents-1un7li7` | core-021 | front-sleeping reply and feeding-benefit reply left out |
| `NewParents-1un8al8` | core-021 | weight and spit-up passages left out |
| `sleeptrain-1un8ksh` | core-021 | cosleeping and bringing into bed left out |
| `toddlers-1un8mcs` | core-021 | cosleeping sentence left out |
| `sleeptrain-1unb4wd` | core-021 | reflux sentence left out |
| `sleeptrain-1uncumg` | core-021 | cosleeping with bed rails and colic passages left out |
| `sleeptrain-1unf4s9` | core-021 | comfort item in cot left out |
| `sleeptrain-1ungff1` | core-021 | parent injury, partner surgery and bedsharing left out |
| `sleeptrain-1unh1vi` | core-021 | named postpartum condition, physical symptoms and cosleeping passages left out |

## How to continue

Nothing in these 8 chunks is unread. To add quotes, append new spec lines to the end of `scratchpad/R26/q021.jsonl` (never reorder earlier lines) and re-run `python3 -I scratchpad/R26/build.py`, then `python3 -I _tools/verify_quotes.py voice/reddit-r26.jsonl`.
