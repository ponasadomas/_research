# Reddit reading ledger — R45 (wave 3, sleep-baby)

Reader R45 · id prefix `sb45` · voice file `voice/reddit-r45.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 9: `read-w3-keep_core-004` … `-012` (15/19/19/18/15/19/19/18/14 units), from `_raw/reddit/read-w3/chunks.jsonl` |
| Units in those chunks | 156 (posts dated 2026-04-02 → 2026-04-07; OP replies to 2026-10-12) |
| Units read in full | 156 |
| Units excluded entirely | 7 (2 content/age, 5 duplicate cross-posts) |
| Units read, nothing to quote | 1 (`NewParents-1se3sjx`: solids, play and boredom, not sleep) |
| Units quoted | 148 (one is the duplicate cross-post `beyondthebump-1sbuf98`, quoted only for its distinct OP reply) |
| Quotes written | 553 (ids sb45-0001 … sb45-0553, unique) |
| Restricted quotes | 8 (listed in `synthesis/reader-notes-r45.md`) |
| Possible seeded quotes (`possible_promo`, never count) | 1 (sb45-0497) |
| verify_quotes.py | 553 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R45/units.tsv`. Short-form sources `scratchpad/R45/q01–q09.tsv` (one per chunk), built into the voice file by `scratchpad/R45/build.py` (it takes url and date from the unit file); `check.py` validates the vocabulary; `resolve.py` fills quote ids into the notes.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1scj7ht.txt` | the whole post is a safe-sleep question (rolling in a bassinet, room safety) -> excluded |
| `../_shared/_raw/reddit-2026/units/toddlers-1scm7g5.txt` | child turned 3 in December, over 36 months at posting -> excluded |
| `../_shared/_raw/reddit-2026/units/toddlers-1sdq0on.txt` | child has turned 3 and is described as a 3-year-old (over-36-month boundary unclear); also health questions -> excluded |
| `../_shared/_raw/reddit-2026/units/NewParents-1se548s.txt` | duplicate cross-post of sleeptrain-1se59mb (same author, same text); quoted once from sleeptrain |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1segxkh.txt` | duplicate cross-post of toddlers-1segwuk (same author, same text) |
| `../_shared/_raw/reddit-2026/units/Parenting-1segy5i.txt` | duplicate cross-post of toddlers-1segwuk (same author, same text) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sdmi09.txt` | duplicate cross-post of toddlers-1sdmgk9 (same author, same text); its OP reply is a cosleeping detail |

## Units read and quoted, with passages left out (neutral reasons)

| unit | not quoted |
|---|---|
| `beyondthebumpUK-1sa83vn` | medication request, mental-health wording, partner's anxiety, cosleeping attempt, formula/intolerance -> not quoted |
| `NewParents-1saa1r6` | formula, gas drops, allergy question -> not quoted |
| `sleeptrain-1sai6s3` | reply odwe0a8 (postpartum condition wording) -> not quoted |
| `sleeptrain-1sajasv` | bedsharing arrangement line -> not quoted |
| `sleeptrain-1sak5gv` | hand-on-baby-in-bassinet detail -> not quoted |
| `toddlers-1sanbnf` | hospital visit; a parent snapping at the child -> not quoted |
| `NewParents-1saocv5` | reflux medication -> not quoted |
| `sleeptrain-1sap3x0` | vaccination and reflux -> not quoted (post quoted) |
| `sleeptrain-1sarmo4` | cosleeping-after-wakings arrangement -> not quoted |
| `sleeptrain-1satv4r` | crisis wording in the closing line -> not quoted (rest of post quoted) |
| `toddlers-1sawjvl` | illness, cosleeping reply -> not quoted |
| `NewParents-1sax8se` | cosleeping, parent's flu -> not quoted |
| `Parenting-1sayv4f` | reflux, tongue-tie procedure, therapy, doctor appointment replies -> not quoted |
| `sleeptrain-1sanzjj` | bedsharing detail -> not quoted |
| `AttachmentParenting-1sb0pqu` | feeding tube, allergies, weight gain, floor-bed detail -> not quoted |
| `toddlers-1sb25mv` | hotel bed-sharing detail -> not quoted |
| `sleeptrain-1sb2zwr` | chest-sleeping detail -> not quoted |
| `NewParents-1sb456x` | rolling while in sleep sack in smart bassinet (sleepwear near rolling) -> not quoted |
| `sleeptrain-1sb81na` | overnight pram sleeping, hypoallergenic formula -> not quoted |
| `sleeptrain-1sb8g5u` | parent's health, hospital and crisis-adjacent wording -> not quoted |
| `beyondthebump-1sba4f1` | cosleeping attempt, medication given before bed -> not quoted |
| `toddlers-1sbaytz` | climbing out of crib, door-banging; melatonin quote kept restricted |
| `sleeptrain-1sbb1gg` | accidental bedsharing -> not quoted |
| `sleeptrain-1sbbq0m` | bedsharing in summary -> not quoted |
| `sleeptrain-1sbeijw` | same author as sleeptrain-1sanzjj reposting with night-one result; bedsharing goals -> not quoted |
| `NewParents-1sbfh67` | suspected allergy, elimination diet -> not quoted |
| `sleeptrain-1sbjedx` | cosleeping after travel -> not quoted |
| `Mommit-1sbjgc9` | diagnoses, therapy, postpartum mental-health wording -> not quoted (two sleep lines quoted) |
| `beyondthebump-1sbkm6s` | self-described neurotype; postpartum condition in reply -> not quoted |
| `sleeptrain-1sbmidb` | weight, swaddle-to-rolling and unswaddled-nap monitoring details -> not quoted |
| `toddlers-1sbmvuw` | pain medication -> not quoted |
| `sleeptrain-1sbqlpi` | bedsharing at 3:30am -> not quoted |
| `NewParents-1sbubqc` | colic history -> not quoted |
| `beyondthebump-1sbuf98` | post is a duplicate cross-post of NewParents-1sbubqc (same author, same text); only its distinct OP reply quoted |
| `AttachmentParenting-1sbyrwu` | illness, fever, weight, GP comments, cosleeping -> not quoted |
| `NewParents-1sc16fp` | cosleeping question -> not quoted |
| `FirstTimeMom-1sc312r` | bedsharing descriptions and replies -> not quoted (two non-safety lines quoted) |
| `sleeptrain-1sc5bp2` | bringing the child into the parents' bed -> not quoted |
| `Mommit-1sc7893` | bedsharing history -> not quoted |
| `NewParents-1sc87t5` | cosleeping, feeding-while-asleep, choking on bottle, developmental worries, doctor -> not quoted |
| `sleeptrain-1sc8hdn` | weight gain, therapists and clinicians, feeding detail -> not quoted |
| `NewParents-1scbz26` | early-morning cosleeping, swing sleep -> not quoted |
| `NewParents-1scef56` | allergy -> not quoted |
| `workingmoms-1sci25z` | fertility treatment; daycare $4k/month amounts noted in notes (not sleep help) |
| `beyondthebump-1scjdd7` | newborn weight loss, supplementing -> not quoted |
| `Parenting-1sck0kb` | bringing the baby into the parents' bed; parent's blood pressure -> not quoted |
| `sleeptrain-1scpgqo, sleeptrain-1scrkcy` | cosleeping arrangements -> not quoted |
| `NewParents-1scvija` | rolling positions in sleep -> not quoted |
| `sleeptrain-1sdbnhi` | rolling and getting stuck at night -> not quoted |
| `beyondthebumpUK-1sdcyvm` | postpartum mental-health conditions, therapy, medication, panic wording, pain medication -> not quoted (sleep-only lines quoted) |
| `sleeptrain-1sdd8oy` | cosleeping -> not quoted |
| `AttachmentParenting-1sdde0l` | pain medication, gum gel, cosleeping -> not quoted |
| `sleeptrain-1sddffv` | bringing baby into bed -> not quoted |
| `beyondthebump-1sddm18` | child hitting himself; night drives to get him to sleep -> not quoted |
| `beyondthebumpUK-1sdigpp` | cosleeping and chest-sleeping attempts -> not quoted |
| `sleeptrain-1sdk9db` | parent's headaches -> not quoted |
| `NewParents-1sdksf5` | surgical recovery, post-birth anxiety and trauma wording, nausea -> not quoted (one sleep line quoted) |
| `Parenting-1sdkss5` | panic attack, crisis-adjacent hyperbole, cosleeping -> not quoted |
| `sleeptrain-1sdktvx` | couch/floor-rocker sleeping -> not quoted |
| `sleeptrain-1sdr8yb` | cosleeping, reverse cycling -> not quoted |
| `beyondthebumpUK-1sdrd02` | bringing baby into the parents' bed -> not quoted |
| `beyondthebumpUK-1sdvi7s` | ear-infection remark -> not quoted |
| `sleeptrain-1sdwkgf` | weight gain -> not quoted |
| `sleeptrain-1sdwntt` | bringing baby into bed; parent's anxiety wording -> not quoted |
| `NewParents-1sdyv1v` | head-banging on crib bars -> not quoted |
| `beyondthebump-1se06co` | doctor and weight comments -> not quoted |
| `NewParents-1se3sjx` | read in full; about solids, play and boredom, not sleep -> no quote |
| `sleeptrain-1se59mb` | post's rolling-to-sleep-sack switch, parent's sleep anxiety and vomiting, wish to escape -> not quoted; cosleeping in reply -> trimmed out |
| `sleeptrain-1se5h5x` | congestion -> not quoted |
| `AttachmentParenting-1se6l6h` | reflux, formula changes, family bed -> not quoted |
| `AttachmentParenting-1se73vx` | exhausted rocking described as almost dangerous, pain medication -> not quoted; "DM me for details" reply tagged possible_promo |
| `NewParents-1se8h4u` | title's mental-health wording; head-against-wall line -> not quoted |
| `sleeptrain-1se8omo` | cosleeping -> not quoted |
| `sleeptrain-1seck3h` | head bumping in crib -> not quoted |
| `toddlers-1sedenq` | child's speech delay, therapist and paediatrician appointments, child hitting during wake-ups, bed-sharing by husband, adoption arguments -> not quoted (sleep lines quoted) |
| `toddlers-1segwuk` | child ending up in parents' bed; night terrors -> not quoted |

## What has and hasn't been read

All 156 units in the nine assigned chunks were read in full, including every original-poster reply in each unit. Nothing is unread.
