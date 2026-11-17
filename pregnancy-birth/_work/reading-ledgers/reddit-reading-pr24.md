# Reddit reading ledger — PR24 (pregnancy-birth, read-w2 keep_purchase 007–012, keep_success 001–002)

Date 2026-10-25. Reader PR24, id prefix pb24. Voice file `../voice/reddit-pr24.jsonl`. Brief: `../../_shared/_tools/brief-reading.md` and `../../_shared/_tools/prompt-pregnancy-reader-w2.txt`. Chunks: `../_raw/reddit/read-w2/chunks.jsonl` (line PR24 in `read-w2/assignments.txt`). Wave 2: keep_purchase posts dated 2026-07-31 to 2026-08-24, keep_success posts 2026-06-25 to 2026-07-03 (OP replies to 2026-10-05).

| step | count |
|---|---|
| chunks assigned | 8 (keep_purchase-007 … 012, keep_success-001 … 002) |
| units in chunks | 133 |
| units read in full | 133 |
| units excluded (lines not to cross) | 8 |
| units read, no quote taken | 11 (5 crossposts or repeat authors, 3 likely seeded, 2 AI-style or generic, 1 other) |
| units quoted | 114 |
| quotes written | 254 (pb24-0001 → pb24-0262; 0219, 0220, 0240, 0241, 0242, 0248, 0251, 0252 withdrawn when their units were excluded on a consistency pass; ids not reused) |
| quotes restricted (quote level) | 35 (listed in `../synthesis/reader-notes-pr24.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr24.jsonl` → 254 quotes, 0 failed |

Nothing unread. Exclusions are logged with a neutral reason; no excluded passage is in the voice file. Rule applied to the keep_success birth stories: a unit whose account includes an acute obstetric or newborn emergency, or a serious scan finding, is excluded; birth stories without one are kept, with procedure, medication and pain-relief quotes restricted. Every quote from Doulas-1vnv41v is restricted because an OP reply describes an emergency birth. Crossposts (same author, same text) quoted once: PregnancyUK-1vtw0s2 = beyondthebumpUK-1vtvzqk; pregnant-1vs4vac = Doulas-1vs616b; Mommit-1vu422h = NewParents-1vu42zg; pregnant-1vuh1dp = BabyBumps-1vuh1yl; pregnant-1ufoxxn = BabyBumps-1ufp5jb (both excluded). pregnant-1uleapk and beyondthebump-1um1nkx are the same author's story a day apart; quoted from the first only. No post in these chunks is cited by another reader's voice file (checked by post_id against `../voice/*.jsonl`). No unit mentions Nurava/@nuravaa; three vitamin posts look seeded (see notes) and are not quoted.

## Every unit

| chunk | unit | status |
|---|---|---|
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vbsqlq.txt` | quoted: pb24-0001 … 0002 (2) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vbt8s0.txt` | quoted: pb24-0003 … 0005 (3) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vc2fei.txt` | quoted: pb24-0006 … 0007 (2) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vc8vim.txt` | quoted: pb24-0008 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vcigln.txt` | quoted: pb24-0009 … 0010 (2) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vd6oxv.txt` | quoted: pb24-0011 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vd9jfh.txt` | quoted: pb24-0012 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vdhghx.txt` | quoted: pb24-0013 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vdmcnj.txt` | quoted: pb24-0014 … 0018 (5) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vdux7l.txt` | quoted: pb24-0019 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1veil7m.txt` | quoted: pb24-0020 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vewcxu.txt` | quoted: pb24-0021 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vf4618.txt` | quoted: pb24-0022 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vf5n38.txt` | quoted: pb24-0023 … 0025 (3) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vfdhxl.txt` | quoted: pb24-0026 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/NewParents-1vflekz.txt` | quoted: pb24-0027 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/pregnant-1vfsav4.txt` | quoted: pb24-0028 … 0029 (2) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vfzljj.txt` | quoted: pb24-0030 … 0034 (5) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vg19h4.txt` | quoted: pb24-0035 … 0036 (2) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vgau7b.txt` | quoted: pb24-0037 … 0039 (3) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vgbhce.txt` | quoted: pb24-0040 … 0042 (3) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vgf4wx.txt` | quoted: pb24-0043 … 0044 (2) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vgx4jm.txt` | quoted: pb24-0045 (1) |
| keep_purchase-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vgy2w9.txt` | quoted: pb24-0046 (1) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/Mommit-1vh9f4q.txt` | quoted: pb24-0047 … 0049 (3) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vha9bn.txt` | quoted: pb24-0050 … 0052 (3) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vhi0md.txt` | quoted: pb24-0053 (1) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vi0etg.txt` | quoted: pb24-0054 (1) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1viejby.txt` | quoted: pb24-0055 … 0057 (3) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vivhlu.txt` | quoted: pb24-0058 (1) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/beyondthebump-1vj2tth.txt` | quoted: pb24-0059 … 0060 (2) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vj3606.txt` | quoted: pb24-0061 (1) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vj4clg.txt` | quoted: pb24-0062 … 0065 (4) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vj606b.txt` | quoted: pb24-0066 … 0068 (3) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vjq3y8.txt` | quoted: pb24-0069 … 0073 (5) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vjq4ip.txt` | quoted: pb24-0074 … 0076 (3) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vkhggy.txt` | quoted: pb24-0077 … 0078 (2) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vkjzhu.txt` | EXCLUDED: asks strangers to buy registry items (money solicitation) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/Mommit-1vkkdqa.txt` | quoted: pb24-0079 (1) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vkm375.txt` | quoted: pb24-0080 … 0082 (3) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vkzx3z.txt` | quoted: pb24-0083 (1) |
| keep_purchase-008 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vlibcl.txt` | quoted: pb24-0084 … 0086 (3) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vll8jh.txt` | quoted: pb24-0087 … 0089 (3) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vlm3zo.txt` | quoted: pb24-0090 … 0091 (2) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vlnglz.txt` | quoted: pb24-0092 … 0094 (3) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vlr839.txt` | quoted: pb24-0095 … 0097 (3) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vmc1uv.txt` | quoted: pb24-0098 (1) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/FirstTimeMom-1vmc48m.txt` | quoted: pb24-0099 … 0100 (2) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vmfrrv.txt` | quoted: pb24-0101 (1) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vmrvuz.txt` | quoted: pb24-0102 … 0108 (7) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/NewParents-1vn3c45.txt` | quoted: pb24-0109 … 0110 (2) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vn3yx8.txt` | read; no quote taken (generic keyword-style post (possible SEO/AI), nothing specific) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vneepk.txt` | quoted: pb24-0111 … 0112 (2) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vngn8a.txt` | quoted: pb24-0113 … 0115 (3) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/NewParents-1vns0l6.txt` | quoted: pb24-0116 … 0118 (3) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/Doulas-1vnv41v.txt` | quoted: pb24-0119 … 0123 (5) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vo4ggh.txt` | quoted: pb24-0124 … 0126 (3) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/beyondthebump-1vo5pr8.txt` | quoted: pb24-0127 (1) |
| keep_purchase-009 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vomgk4.txt` | quoted: pb24-0128 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/Doulas-1vovsqi.txt` | read; no quote taken (doula-wanted list, bullet style reads AI-assisted; nothing personal) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vp2w8w.txt` | quoted: pb24-0129 … 0130 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vpd60t.txt` | quoted: pb24-0131 … 0132 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vpdpqt.txt` | quoted: pb24-0133 … 0135 (3) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/NewParents-1vpsx9x.txt` | quoted: pb24-0136 … 0137 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vq9aba.txt` | quoted: pb24-0138 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vqfkm7.txt` | quoted: pb24-0139 … 0140 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vqgdu3.txt` | quoted: pb24-0141 … 0143 (3) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vqpwy9.txt` | quoted: pb24-0144 … 0145 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vr79kg.txt` | quoted: pb24-0146 … 0148 (3) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vrgkuh.txt` | quoted: pb24-0149 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vrkgzh.txt` | quoted: pb24-0150 … 0152 (3) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vrq07m.txt` | quoted: pb24-0153 … 0154 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vrx055.txt` | read; no quote taken (likely seeded (prenatal-vitamin brand comparison favouring BabyRx, "real experiences rather than ads")) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/Mommit-1vryhmb.txt` | quoted: pb24-0155 … 0156 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vs4iv0.txt` | quoted: pb24-0157 … 0159 (3) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vs4vac.txt` | quoted: pb24-0160 … 0161 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/Doulas-1vs616b.txt` | read; no quote taken (crosspost of pregnant-1vs4vac (same author, same text)) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vscabc.txt` | read; no quote taken (likely seeded/AI-written (iron-free prenatal pitch, OP reply "game changer")) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vsp82i.txt` | quoted: pb24-0162 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vsv4hr.txt` | quoted: pb24-0163 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vsz3hv.txt` | quoted: pb24-0164 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vt0vdh.txt` | quoted: pb24-0165 … 0166 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vt38xw.txt` | quoted: pb24-0167 … 0168 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vtflha.txt` | quoted: pb24-0169 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vtg2tk.txt` | quoted: pb24-0170 … 0173 (4) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vtg80j.txt` | quoted: pb24-0174 … 0175 (2) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vtpimo.txt` | quoted: pb24-0176 (1) |
| keep_purchase-010 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vtqhnz.txt` | quoted: pb24-0177 (1) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vtvzqk.txt` | read; no quote taken (crosspost of PregnancyUK-1vtw0s2 (same author; stray "Mumsnet" lines suggest also posted there)) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vtw0s2.txt` | quoted: pb24-0178 … 0179 (2) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vtye93.txt` | quoted: pb24-0180 (1) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/Mommit-1vu422h.txt` | quoted: pb24-0181 (1) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/NewParents-1vu42zg.txt` | read; no quote taken (crosspost of Mommit-1vu422h) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vubr97.txt` | quoted: pb24-0182 … 0184 (3) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vuh1dp.txt` | quoted: pb24-0185 (1) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vuh1yl.txt` | read; no quote taken (crosspost of pregnant-1vuh1dp) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vunjhn.txt` | quoted: pb24-0186 … 0188 (3) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vuqbpe.txt` | quoted: pb24-0189 … 0192 (4) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vuuh15.txt` | quoted: pb24-0193 … 0194 (2) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/beyondthebump-1vvmpev.txt` | quoted: pb24-0195 … 0197 (3) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vw7b2k.txt` | quoted: pb24-0198 … 0199 (2) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vw7ccp.txt` | read; no quote taken (likely vitamin seeding (choline/methylfolate label comparison, asks for brands; same wording as U73/U78)) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vwg72z.txt` | quoted: pb24-0200 … 0201 (2) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/beyondthebump-1vwjugh.txt` | quoted: pb24-0202 (1) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/Mommit-1vwlucr.txt` | quoted: pb24-0203 (1) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vwrve9.txt` | quoted: pb24-0204 … 0205 (2) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vww7c0.txt` | quoted: pb24-0206 (1) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vx1d55.txt` | quoted: pb24-0207 … 0212 (6) |
| keep_purchase-011 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vx2d5d.txt` | quoted: pb24-0213 … 0214 (2) |
| keep_purchase-012 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vx8yn3.txt` | quoted: pb24-0215 (1) |
| keep_purchase-012 | `../_shared/_raw/reddit-2026/units/pregnant-1vxbpki.txt` | quoted: pb24-0216 … 0217 (2) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uf769e.txt` | quoted: pb24-0218 (1) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ufoxxn.txt` | EXCLUDED: birth account includes an acute postpartum emergency |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/BabyBumps-1ufp5jb.txt` | EXCLUDED: crosspost of the same birth account (acute postpartum emergency) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uftaa5.txt` | quoted: pb24-0221 … 0222 (2) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ufumlx.txt` | quoted: pb24-0223 … 0225 (3) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ug6cnj.txt` | EXCLUDED: centred on an acute obstetric emergency at birth |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1ughcfq.txt` | quoted: pb24-0226 … 0228 (3) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uh0tl7.txt` | quoted: pb24-0229 (1) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uivsgo.txt` | quoted: pb24-0230 … 0233 (4) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ujvhde.txt` | quoted: pb24-0234 … 0237 (4) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uk2ndk.txt` | quoted: pb24-0238 … 0239 (2) |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ukl4kd.txt` | EXCLUDED: birth account centred on an emergent complication and newborn intensive care |
| keep_success-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ul9wl0.txt` | read; no quote taken (short induction announcement centred on a condition; nothing beyond a stock line) |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/pregnant-1uldtd8.txt` | EXCLUDED: birth account centred on an emergency surgical delivery |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/pregnant-1uleapk.txt` | quoted: pb24-0243 … 0247 (5) |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/pregnant-1ulgd8e.txt` | EXCLUDED: centred on a serious scan finding |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/pregnant-1ulrorn.txt` | quoted: pb24-0249 … 0250 (2) |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/pregnant-1ulwa1t.txt` | EXCLUDED: birth account centred on a newborn emergency and a traumatic birth |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/pregnant-1um03zo.txt` | quoted: pb24-0253 … 0256 (4) |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/beyondthebump-1um1nkx.txt` | read; no quote taken (same author and story as pregnant-1uleapk (U126), posted a day later; also grief and birth-injury wording throughout) |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/pregnant-1um2x8x.txt` | quoted: pb24-0257 (1) |
| keep_success-002 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1umnixd.txt` | quoted: pb24-0258 … 0262 (5) |
