# Reddit reading ledger — R57 (wave 3, sleep-baby)

Reader R57 · id prefix `sb57` · voice file `voice/reddit-r57.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 10 (`read-w3-keep_core-115` … `read-w3-keep_core-124`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 156 (posts dated 2026-05-22 → 2026-05-27; OP replies to 2026-09-16) |
| Units read in full | 156 |
| Units excluded entirely | 13 (content or off-topic; 2 of them duplicate cross-posts) |
| Units quoted | 143 |
| Quotes written | 580 (ids sb57-0001 … sb57-0580, unique) |
| Restricted quotes | 8 (listed in `synthesis/reader-notes-r57.md`) |
| verify_quotes.py | 580 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R57/units.tsv`. Reading copies: `scratchpad/R57/part00–19.txt`. Short-form quote sources: `scratchpad/R57/q00–q19.tsv`, built by `scratchpad/R57/build.py` (restricted list in `scratchpad/R57/restricted.txt`).

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1tkpivw.txt` | safe-sleep detail (bedsharing, lounger on bed, rolling risk) runs through the post |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1tknsgt.txt` | the whole post is about room temperature and sleep-bag tog (safe-sleep detail) plus a medical treatment |
| `../_shared/_raw/reddit-2026/units/toddlers-1tlln67.txt` | duplicate cross-post of Mommit-1tlogx4 (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1tlpekf.txt` | the whole post is sleepwear tog in a heatwave (safe-sleep detail) |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1tm4gox.txt` | safe-sleep incident (rolling face down, legs caught in cot bars) is the whole post |
| `../_shared/_raw/reddit-2026/units/NewParents-1tml295.txt` | about car seat and carrier crying, little sleep content; sleeping in a swing (safe-sleep detail) and food intolerance |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tmw7ga.txt` | the whole post is about tummy sleeping and rolling at night (safe-sleep detail) |
| `../_shared/_raw/reddit-2026/units/NewParents-1tn1jp8.txt` | sleepwear choices tied to rolling and swaddle removal (safe-sleep detail) run through the post |
| `../_shared/_raw/reddit-2026/units/toddlers-1tn7srt.txt` | mental-health crisis wording, a fall injury and bedsharing run through the post and replies |
| `../_shared/_raw/reddit-2026/units/Parenting-1to4hkm.txt` | sleep content is a bedsharing line; the rest is daycare drop-off |
| `../_shared/_raw/reddit-2026/units/toddlers-1to4q1q.txt` | duplicate cross-post of Parenting-1to4hkm (also excluded) |
| `../_shared/_raw/reddit-2026/units/Parenting-1to9wek.txt` | diaper behaviour at nap time, not a sleep problem |
| `../_shared/_raw/reddit-2026/units/daddit-1totq8a.txt` | illness, medication and allergic reaction run through the post and replies |

## Units read, passages left out (neutral reasons)

Quotes were taken from the rest of these units; the passages named were not copied.

| unit | left out |
|---|---|
| `../_shared/_raw/reddit-2026/units/Parenting-1tkoc3f.txt` | comment onaeh3i left out (verbal harshness toward the child) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tkn8g4.txt` | medication and illness passage left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tl2q58.txt` | comment oncv66p left out (medication) |
| `../_shared/_raw/reddit-2026/units/NewParents-1tl2q9g.txt` | reflux passages and reply p9qq3k3 left out (medical) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tl5h9b.txt` | bedsharing line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tlbjma.txt` | medication line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tlcxxc.txt` | post body duplicates NewParents-1tlchmu; only its own reply quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tlfq32.txt` | bedsharing line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tlidhw.txt` | rolling reply onhssh1 left out |
| `../_shared/_raw/reddit-2026/units/Parenting-1tlohhm.txt` | mental-health wording (onha6wl), medical tests and diet (onhdvly rest), cosleeping reply left out |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1tlqjuz.txt` | co-sleeping / bed lines left out |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1tls3a0.txt` | cosleeping lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tlus0o.txt` | medication line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tlzo4h.txt` | bedsharing lines and crying-distress description left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tm1ufl.txt` | a passage of harsh feelings toward the child (urge-type wording) and bedsharing lines left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tm32oh.txt` | bedsharing-in-arms lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tm82w2.txt` | feeding-weight and congestion/snoring medical lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tmbkx7.txt` | constipation passage left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tmbzbf.txt` | tummy-sleeping lines (safe-sleep detail) left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tmcm0h.txt` | colic/reflux medication line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tmedbe.txt` | bed line left out |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tmlp9l.txt` | side-sleeping and cosleeping lines (safe-sleep detail) left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tmlx6s.txt` | bedsharing line left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1tmnhdl.txt` | bedsharing line and GP/health reply left out |
| `../_shared/_raw/reddit-2026/units/Mommit-1tmnunu.txt` | mental-health wording (onrt6i8) and feeding lines left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tmw06j.txt` | doctor/medication replies left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tmws57.txt` | bedsharing lines and face-scratching distress left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tmx155.txt` | safe-sleep details (heating pad, side placement, cosleeping) and reflux reply left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1tmyu39.txt` | cosleeping edit and blood-test line left out |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1tmzcmx.txt` | mental-health word, reflux and belly-sleeping lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tmzk34.txt` | bedsharing and hospital passages left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tn0q3k.txt` | bedsharing line left out; feeding-therapy quote restricted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tn3yst.txt` | feeding-volume/weight lines left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tn492n.txt` | mental-health line, bedsharing and room-temperature replies left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tn5xdl.txt` | tog/room-temperature lines left out; only the price lines quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tn7ecj.txt` | medical condition (wrists) and cosleeping lines left out |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tn7oaz.txt` | cosleeping safety line and a drowsy-driving fear left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tn9a49.txt` | bedsharing line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tnanf3.txt` | vigorous-rocking, arm-cosleeping, reflux and hospital passages left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tnax2d.txt` | co-sleeping line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tneb0x.txt` | a holding-down line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tneydy.txt` | illness and an anger line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tng1xs.txt` | hospital line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tnjng2.txt` | allergies, medication, treatments and bedsharing left out; one line quoted |
| `../_shared/_raw/reddit-2026/units/toddlers-1tnjt83.txt` | near-duplicate of sleeptrain-1tnlnjl by the same author; only the line naming the wife quoted; falling-out-of-bed line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tnni12.txt` | mental-health line (onv8z22) left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tnnl97.txt` | postpartum sadness, crying and feeding-failure lines left out (mental-health adjacent) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tnu9jf.txt` | stroller-sleep-in-room and bedsharing lines (safe-sleep detail) left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tnvq2w.txt` | dad-cosleeps line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1to0erq.txt` | reflux, allergy, illness, couch/chest sleeping and a hospital-stay wish left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1to44rs.txt` | mental-health wording and self-criticism sentence left out |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1to4mja.txt` | side-positioning, co-sleeping and illness lines left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1to6gjd.txt` | medical-test question left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1todhp0.txt` | post body duplicates FirstTimeMom-1tmzcmx (quoted there); only replies quoted; one restricted (medical conditions) |
| `../_shared/_raw/reddit-2026/units/toddlers-1tofsv5.txt` | bedsharing line and discipline replies left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tog9pz.txt` | head-hitting/falling lines left out |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1togex2.txt` | bedsharing and illness/vaccine lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tohb2x.txt` | body duplicates beyondthebumpUK-1togex2 (quoted there); only its extra paragraph and one reply quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1togqyd.txt` | napping-in-my-bed line left out |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1togx32.txt` | hospital, medication, rolling and older-child bedsharing lines left out |
| `../_shared/_raw/reddit-2026/units/Mommit-1tohpiq.txt` | medication and mental-health line, big-bed line left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1toj00r.txt` | child hitting passage and toileting detail left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tok2w5.txt` | medication line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1toipsd.txt` | feeding-aversion volumes left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1tol14c.txt` | medication and anxiety lines left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1tolfy7.txt` | anxiety wording, illness and spare-bed lines left out |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1top7xv.txt` | medical-test lines and bed-thrashing/clothing lines left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1toq34w.txt` | hitting line left out |

## Duplicate cross-posts inside this set

- `NewParents-1tlchmu` / `sleeptrain-1tlcxxc` (same post): body quoted once, each reply quoted from its own unit.
- `Mommit-1tlogx4` quoted; `toddlers-1tlln67` excluded as duplicate.
- `sleeptrain-1tnlnjl` quoted; `toddlers-1tnjt83` (same father) only for its unique line naming the wife.
- `beyondthebumpUK-1togex2` quoted; `sleeptrain-1tohb2x` (same mother) only for its extra paragraph and one reply.
- `FirstTimeMom-1tmzcmx` quoted; `NewParents-1todhp0` (same mother) only for its replies.
- `Parenting-1to4hkm` / `toddlers-1to4q1q` both excluded.

## What has and hasn't been read

All 156 units in the 10 assigned chunks were read in full, including every OP reply. Nothing is unread.

