# Reddit reading ledger — R21 (prefix sb21), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1b/chunks.jsonl` (second chunk set). Voice file: `voice/reddit-r21.jsonl`. Scratch (unit list, exclusion log, progress log, per-chunk spec files `c053.py`…`c061.py`, `add.py` builder): `scratchpad/R21/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 9 (`read-v1b-keep_core-053` … `-061`, the final assignment, includes 061) |
| units in those chunks | 162 (14/15/14/19/20/19/19/27/15) |
| units read in full (post + every OP reply) | 162 |
| units excluded entirely | 14 |
| cross-posts read, quoted from the other copy only | 3 |
| units with passages excluded (rest quoted) | 55 |
| units quoted | 145 |
| quotes written | 387 (sb21-0001 … sb21-0387), `verify_quotes.py` 0 failed |

Counts are of quotes chosen, never of people.

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `sleeptrain-1xbi07t` | 053 | safe-sleep fear after rolling (swaddle transition); not quoted |
| `NewParents-1xbtpx3` | 054 | safe-sleep fear after rolling in bedside sleeper; not quoted |
| `NewParents-1xc6jgg` | 056 | safe-sleep incident (fall during adult bed sleep); not quoted |
| `toddlers-1xcga5j` | 056 | post centred on bedsharing arrangements; not quoted |
| `toddlers-1xco5gr` | 057 | post centred on bedsharing arrangements; not quoted |
| `sleeptrain-1xcrwf0` | 057 | swaddle/sleepwear details near rolling; not quoted |
| `NewParents-1xcuv43` | 057 | crosspost of sleeptrain-1xcrwf0; swaddle/sleepwear details near rolling; not quoted |
| `beyondthebumpUK-1xd05x7` | 058 | bedsharing arrangement and parent anger toward toddler; not quoted |
| `AttachmentParenting-1xd7zm7` | 059 | infant choking episodes, reflux medication decision and bedsharing; not quoted |
| `Parenting-1xdoapx` | 060 | post centred on bedsharing; not quoted |
| `ScienceBasedParenting-1xdvj9k` | 060 | bedsharing-centred post with fear of hurting baby; not quoted |
| `beyondthebump-1xdz4p0` | 060 | crosspost of ScienceBasedParenting-1xdvj9k; same reason |
| `AttachmentParenting-1xdx5hp` | 060 | mental-health crisis wording; not quoted |
| `AttachmentParenting-1xeanbp` | 060 | truncated crosspost of beyondthebump-1xeam9o; bedsharing-centred |

## Cross-posts and duplicate copies

| unit | chunk | note |
|---|---|---|
| `beyondthebump-1xc274t` | 056 | crosspost of NewParents-1xc25fw, identical text; read, quoted from the other copy |
| `toddlers-1xci2fk` | 057 | crosspost of sleeptrain-1xchu1e, identical text; read, quoted from the other copy |
| `sleeptrain-1xd0nyp` | 058 | crossposted as NewParents-1xd0oqv; both read |
| `toddlers-1xd6756` | 059 | crosspost of sleeptrain-1xd650n, identical text; read, quoted from the other copy |
| `Parenting-1xek739` | 061 | crossposted as sleeptrain-1xek92f; both read |

## Units with passages excluded (other passages quoted)

| unit | chunk | passage not quoted |
|---|---|---|
| `NewParents-1xbcxxz` | 053 | bedsharing arrangement passages not quoted; other passages quoted |
| `sleeptrain-1xbb2bo` | 053 | early-morning bedsharing line not quoted |
| `beyondthebumpUK-1xbgwav` | 053 | infant breathing/health worry passage not quoted |
| `beyondthebump-1xblg5d` | 054 | bedsharing/comfort-nursing arrangement not quoted |
| `NewParents-1xblksb` | 054 | bedsharing-from-birth passage not quoted |
| `sleeptrain-1xbmvf3` | 054 | bedsharing line not quoted |
| `sleeptrain-1xbryo5` | 054 | early-morning bedsharing passages not quoted |
| `NewParents-1xbvmk1` | 054 | bedsharing and fall-risk passages not quoted |
| `sleeptrain-1xbvtc0` | 054 | physical restraint at nap passage not quoted |
| `toddlers-1xbqbwk` | 054 | bedsharing passage not quoted |
| `sleeptrain-1xbxndj` | 055 | despair wording and bedsharing passage not quoted |
| `Parenting-1xby662` | 055 | bedsharing passages not quoted |
| `sleeptrain-1xbyctc` | 055 | bedsharing-after-illness line not quoted |
| `NewParents-1xc25fw` | 055 | bedsharing camp sentence not quoted |
| `sleeptrain-1xc2muq` | 056 | bedsharing line not quoted |
| `AttachmentParenting-1xc4mc3` | 056 | bedsharing line not quoted |
| `sleeptrain-1xc73bg` | 056 | bedsharing lines not quoted |
| `sleeptrain-1xc7l44` | 056 | earlier bedsharing line not quoted |
| `NewParents-1xc8yb7` | 056 | sleeping-in-arms-overnight line not quoted |
| `beyondthebumpUK-1xcapzp` | 056 | bedsharing attempt line not quoted |
| `Parenting-1xcbcan` | 056 | toddler-in-parents-bed lines not quoted |
| `sleeptrain-1xcdymz` | 056 | bedsharing line not quoted |
| `toddlers-1xcg5lx` | 056 | bedsharing line not quoted |
| `sleeptrain-1xctz6x` | 057 | safe-sleep incident during crying and bedsharing lines not quoted |
| `NewParents-1xcpbvg` | 057 | sleep-position reply not quoted |
| `beyondthebumpUK-1xci6ce` | 057 | bedsharing line not quoted |
| `sleeptrain-1xcurva` | 057 | bedsharing-to-nurse passage not quoted |
| `toddlers-1xcvd18` | 057 | crib safety-hazard reply not quoted |
| `sleeptrain-1xclpdh` | 057 | bedsharing-before-training clause trimmed out of quote |
| `sleeptrain-1xcxk73` | 058 | bedsharing references not quoted |
| `sleeptrain-1xcy0uv` | 058 | illness breathing detail not quoted |
| `toddlers-1xd0i9m` | 058 | bedsharing reply not quoted |
| `sleeptrain-1xd4ygf` | 058 | swaddle/sleeping-bag details near rolling and bedsharing line not quoted |
| `toddlers-1xd5bft` | 058 | bedsharing line not quoted |
| `sleeptrain-1xd650n` | 058 | bedsharing lines not quoted |
| `sleeptrain-1xd9e93` | 059 | bedsharing reply not quoted |
| `sleeptrain-1xd9s7g` | 059 | bedsharing line and panic-attack line not quoted |
| `sleeptrain-1xda0tm` | 059 | sleep-proximity line not quoted |
| `sleeptrain-1xdbr90` | 059 | swaddle/rolling and bedsharing lines not quoted |
| `sleeptrain-1xdguyr` | 059 | bedsharing and repositioning-on-tummy lines not quoted |
| `sleeptrain-1xdgx2o` | 059 | bedsharing and rolling lines not quoted |
| `sleeptrain-1xdhrgy` | 059 | bedsharing passage not quoted |
| `FirstTimeMom-1xd91pn` | 059 | stool/medical detail not quoted |
| `beyondthebump-1xeam9o` | 060 | bedsharing passages not quoted; one non-bedsharing belief line quoted |
| `sleeptrain-1xdpc3c` | 060 | infant suffocation fear sentence and bedsharing lines not quoted |
| `sleeptrain-1xdlkji` | 060 | bedsharing mention not quoted |
| `Mommit-1xdlzdh` | 060 | hopelessness wording not quoted |
| `NewParents-1xdrnhw` | 060 | sleep-position line not quoted |
| `sleeptrain-1xducsd` | 060 | bedsharing lines not quoted |
| `sleeptrain-1xdxxf2` | 060 | bedsharing lines not quoted |
| `NewParents-1xe461q` | 060 | overnight on-parent sleep and back-sleep lines not quoted |
| `beyondthebump-1xe6dzd` | 060 | parent snapping at child passage not quoted |
| `sleeptrain-1xebyos` | 061 | parent anger line not quoted |
| `NewParents-1xefpci` | 061 | bedsharing attempt line not quoted |
| `AttachmentParenting-1xejkea` | 061 | bedsharing openness, parent medical history and distress passages not quoted |

## What has and hasn't been read

All 162 units in chunks 053–061 were read in full, including every archived original-poster reply. Nothing in this assignment is unread. Replies by other commenters are not in the units and were not read.
