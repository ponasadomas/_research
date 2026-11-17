# Reddit reading ledger — R59 (wave 3, keep_core 135–143)

Reader R59, id prefix `sb59`, voice file `voice/reddit-r59.jsonl`. Brief: `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` → `../_shared/_tools/brief-reading.md`.

| step | count |
|---|---|
| chunks assigned | 9 (`read-w3-keep_core-135` … `read-w3-keep_core-143`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in those chunks | 158 |
| units read in full (post + every OP reply in the unit) | 158 |
| units excluded entirely (neutral reason below) | 3 |
| cross-posts read in full, not quoted (the twin was quoted) | 5 |
| read in full, nothing quotable | 2 |
| units quoted | 148 |
| quotes written | 532 (`sb59-0001` … `sb59-0532`, ids unique) |
| restricted quotes | 11 (listed in `synthesis/reader-notes-r59.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-r59.jsonl` → 532 quotes, 0 failed |

Posts are dated 31 May – 4 June 2026; OP replies run to 29 September 2026. Ids are in reading order.

## Units excluded entirely

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tuu9oz.txt` | infant-death (SIDS) fear and co-sleeping make up the whole post |
| `../_shared/_raw/reddit-2026/units/toddlers-1tvxfnz.txt` | medical tests, symptoms and parent's fear of serious illness make up the post |
| `../_shared/_raw/reddit-2026/units/Mommit-1tvxhof.txt` | cross-post of toddlers-1tvxfnz; same medical content |

## Read in full, not quoted

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tt28bc.txt` | cross-post of NewParents-1tt2723 (same text, same day); twin quoted |
| `../_shared/_raw/reddit-2026/units/Parenting-1tt295p.txt` | cross-post of NewParents-1tt2723 (same text, same day); twin quoted |
| `../_shared/_raw/reddit-2026/units/Mommit-1ttshhe.txt` | cross-post of NewParents-1tt2723 (same text, next day); twin quoted |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1tuh27j.txt` | cross-post of sleeptrain-1tugxjf (same text, same hour); twin quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tui7gk.txt` | cross-post of sleeptrain-1tugy9l (same text, same hour); twin quoted |
| `../_shared/_raw/reddit-2026/units/toddlers-1tsmuzh.txt` | pillow-timing question only, nothing quotable |
| `../_shared/_raw/reddit-2026/units/toddlers-1tur8t6.txt` | bed-sharing toddler and possible night terrors make up the post; nothing quotable without them |

## Quoted units where a passage was left out

Quote-level restriction: these units were quoted, but the passages below were not copied (safe-sleep detail, medical or mental-health detail). One row is a partly quoted cross-post instead. Every other assigned unit was quoted with nothing held back.

| unit | passage not quoted, or note |
|---|---|
| `../_shared/_raw/reddit-2026/units/daddit-1tsl7ow.txt` | safe-sleep line: parents drifting off with baby on chests, not quoted; gas drops not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tspshd.txt` | tummy-position line not quoted |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1tstgnz.txt` | bedsharing lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tt06do.txt` | cosleeping and migraine lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tt2723.txt` | co-sleeping line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tt6r6f.txt` | parent nearly falling asleep holding baby, and mental-health line, not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1ttd3aq.txt` | co-sleeping on top of/next to parent lines not quoted |
| `../_shared/_raw/reddit-2026/units/ScienceBasedParenting-1ttgr3l.txt` | parent dozing off line not quoted |
| `../_shared/_raw/reddit-2026/units/toddlers-1tthyo9.txt` | child banging head on crib rails not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttlikq.txt` | reflux line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttnouh.txt` | transfer to parents' bed and weight percentile lines not quoted |
| `../_shared/_raw/reddit-2026/units/toddlers-1ttoyyz.txt` | pregnancy spotting line not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1ttpaoy.txt` | milk-intolerance/medical and pumping-infection lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttvifz.txt` | reflux medicine, constipation, parent's physical symptoms and cosleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tty2o8.txt` | baby asleep on pillow on lap line not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1ttz3qj.txt` | cosleeping, hip pain, postpartum healing and intimacy lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttzhkl.txt` | cosleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tu0ce2.txt` | child hurting himself on cot rails line not quoted |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tu13lz.txt` | melatonin line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tu1x7y.txt` | bed-sharing lines not quoted |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tuaj60.txt` | allergy, ear infection, therapy and co-sleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tucbjw.txt` | reflux, gas medicine and breathing lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tudaid.txt` | co-sleeping line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tugxjf.txt` | reflux medication, Tylenol and holding-overnight lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tuij5n.txt` | co-sleeping naps and bed-sharing lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tuko0l.txt` | eczema line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tukpfd.txt` | parent and baby falling asleep together in a recliner, not quoted |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tukyd5.txt` | co-sleeping line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tullyh.txt` | reflux line not quoted |
| `../_shared/_raw/reddit-2026/units/toddlers-1tuqotp.txt` | tonsil/adenoid check and ear-tube lines not quoted |
| `../_shared/_raw/reddit-2026/units/sahm-1tutdj9.txt` | co-sleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tuqlfx.txt` | sleeping in parents' bed lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tuyi7l.txt` | co-sleeping line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tv0gou.txt` | parent lying in toddler bed all night lines not quoted |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tv28uu.txt` | co-sleeping, holding-while-asleep fear, stomach/dairy/reflux, belly-sleep and driving-distress lines not quoted |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tv4can.txt` | depression wording not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tv69ld.txt` | rolling on parents' bed line not quoted |
| `../_shared/_raw/reddit-2026/units/Parenting-1tv7k7a.txt` | contraceptive pill and menstrual-cycle lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvbodw.txt` | reflux medication and belly-sleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvc7xx.txt` | co-sleeping line and parent's fear for baby's wellbeing not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvfvkl.txt` | co-sleeping line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvghsl.txt` | eczema, dairy reaction, birth, latch and allergist lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvh78h.txt` | co-sleeping, monitor-sock and fear-of-harm lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvhle5.txt` | bed-sharing line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvm5zx.txt` | bed-sharing lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvngfl.txt` | falling asleep next to parent line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvpfau.txt` | co-sleeping, illness and cradle-cap lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvqyz4.txt` | fever check line not quoted |
| `../_shared/_raw/reddit-2026/units/Parenting-1tvric3.txt` | mental-breakdown wording not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvse4q.txt` | co-sleeping, SIDS room-sharing and monitor lines not quoted |
| `../_shared/_raw/reddit-2026/units/Mommit-1tvtq6z.txt` | parent's breakdown line not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvu13t.txt` | reflux question not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvuabt.txt` | co-sleeping line not quoted |
| `../_shared/_raw/reddit-2026/units/Mommit-1tvuuja.txt` | parents' bed lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw1ip9.txt` | cross-post of toddlers-1tw1h1k; only the unique OP reply quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tw2cwf.txt` | co-sleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw4j4l.txt` | weight-gain, feeding-therapy and bed lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw5vpg.txt` | mental-health line and ear check not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw8fhw.txt` | co-sleeping and rolling-to-stomach lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw9s3v.txt` | co-sleeping and parent dozing off with child lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twatnc.txt` | hitched-breathing line not quoted |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1twbb1m.txt` | co-sleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twi11q.txt` | co-sleeping, allergy, eczema, reflux and parent-frustration lines not quoted |
| `../_shared/_raw/reddit-2026/units/toddlers-1twjq91.txt` | tooth-decay and co-sleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twjsd7.txt` | bed-sharing feed lines not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twlc8a.txt` | bedside-crib line not quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twncbk.txt` | bringing baby into parents' bed line not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1twskts.txt` | reflux, allergy, eczema, belly-sleeping, anxiety and co-sleeping lines not quoted |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1twv1kb.txt` | reflux, co-sleeping and anger lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1twv5xv.txt` | aftermarket mattress insert and sleep-tent lines not quoted |

## Quotes per unit

| unit | quotes |
|---|---|
| `../_shared/_raw/reddit-2026/units/daddit-1tsl7ow.txt` | 6 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tsmuzh.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tsn2fk.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tspshd.txt` | 14 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tss1vp.txt` | 7 |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1tstgnz.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tsu3ci.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tsu86d.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tsw5o6.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tswhgp.txt` | 9 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tsx47q.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tszxb2.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tt06do.txt` | 7 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tt106g.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tt14rq.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tt1pu6.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tt2723.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tt28bc.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/Parenting-1tt295p.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tt2fec.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tt6mu5.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tt6r6f.txt` | 12 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tt8qi1.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tt8z44.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1ttc6g8.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/NewParents-1ttd3aq.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/NewParents-1ttdgxm.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttez9a.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/daddit-1ttf8fe.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/ScienceBasedParenting-1ttgr3l.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/daddit-1tthi87.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tthyo9.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1ttiged.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttlikq.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttnouh.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/toddlers-1ttoyyz.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttozue.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttpanj.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/NewParents-1ttpaoy.txt` | 10 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttpec4.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/Mommit-1ttshhe.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttsx38.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttudwb.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttvifz.txt` | 7 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttwk46.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tty2o8.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tty52v.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tty8pc.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/NewParents-1ttz3qj.txt` | 7 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ttzhkl.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tu0ce2.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tu0v3w.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tu13lz.txt` | 6 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tu1x7y.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tuai8r.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tuaj60.txt` | 6 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tucbjw.txt` | 6 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tucglx.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tudaid.txt` | 6 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tudjb6.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tudsn8.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tugxjf.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tugy9l.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/FirstTimeMom-1tuh27j.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tui7gk.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tuij5n.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tuko0l.txt` | 8 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tukpfd.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tukyd5.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tul69i.txt` | 6 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tullyh.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tum8zi.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tuozni.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tup9fm.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tuqlfx.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tuqotp.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tur8t6.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/sahm-1tutdj9.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tuu9oz.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tuv972.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tuvfrr.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tuyi7l.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tv0gou.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tv1zft.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tv28uu.txt` | 7 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tv4can.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tv4o1t.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tv69ld.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/Parenting-1tv7fhi.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/Parenting-1tv7k7a.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvb099.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvbodw.txt` | 8 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvby77.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvc7xx.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tvdcso.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvfvkl.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvghsl.txt` | 10 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvh78h.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvhle5.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvhtaz.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvjeph.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tvkhnm.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvm5zx.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvmuc1.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvngfl.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvnn3l.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvocdd.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvpfau.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvq45y.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvq5hs.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvqyz4.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvrgdp.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/Parenting-1tvric3.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvse4q.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvsedc.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/Mommit-1tvtq6z.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvu13t.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvu7jo.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvuabt.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/Mommit-1tvuuja.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvw8u0.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tvwxmc.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tvxfnz.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/Mommit-1tvxhof.txt` | 0 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvyc7g.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tw1h1k.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw1ip9.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/NewParents-1tw2cwf.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw2jln.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw4j4l.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw4v3e.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/toddlers-1tw4xfy.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw5vpg.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/Parenting-1tw8fbv.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw8fhw.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw9s3v.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tw9xk3.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/Mommit-1twae8q.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twatnc.txt` | 4 |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1twbb1m.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twbv03.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twd5l0.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twemyw.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/toddlers-1twg6dd.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twhbz6.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twi11q.txt` | 5 |
| `../_shared/_raw/reddit-2026/units/toddlers-1twjq91.txt` | 7 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twjsd7.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twjw5m.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twk9dg.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twlc8a.txt` | 7 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twmxu8.txt` | 2 |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twncbk.txt` | 6 |
| `../_shared/_raw/reddit-2026/units/Parenting-1twrmzx.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/NewParents-1twskts.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1twv1kb.txt` | 3 |
| `../_shared/_raw/reddit-2026/units/NewParents-1twv5xv.txt` | 1 |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1twvs46.txt` | 3 |
