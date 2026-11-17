# Reddit reading ledger — PR25 (pregnancy-birth, read-w2 keep_success 003–012, keep_otherside 001–002)

Date 2026-10-25. Reader PR25, id prefix pb25. Voice file `../voice/reddit-pr25.jsonl`. Brief: `../../_shared/_tools/brief-reading.md` and `../../_shared/_tools/prompt-pregnancy-reader-w2.txt`. Chunks: `../_raw/reddit/read-w2/chunks.jsonl` (line PR25 in `../_raw/reddit/read-w2/assignments.txt`). Wave 2: posts dated 2026-06-25 to 2026-08-24 (OP replies to 2026-10-19).

| step | count |
|---|---|
| chunks assigned | 12 (read-w2-keep_success-003 … 012, read-w2-keep_otherside-001 … 002) |
| units in chunks | 128 |
| units read in full | 128 |
| units excluded (lines not to cross) | 17 |
| units read, no quote taken | 11 (incl. 2 reposts/crossposts, 4 flagged possible seeding or AI-written) |
| units quoted | 100 |
| quotes written | 348 (pb25-0001 → pb25-0348) |
| quotes restricted (quote level) | 42 (listed in `../synthesis/reader-notes-pr25.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr25.jsonl` → 348 quotes, 0 failed |

Nothing unread. Exclusions are logged with a neutral reason; no excluded passage was copied. keep_success chunks are mostly post-birth "graduation" stories, so many units sit on the acute-emergency line; where a story is centred on an emergency it is excluded, where it ends in an unplanned but non-emergency change of plan it is kept and its procedure lines restricted.

Reposts and crossposts (same author, same text) quoted once: BabyBumps-1vlno25 = beyondthebump-1vnirq1; PregnancyUK-1vqepb4 = pregnant-1vqesty; BabyBumps-1vwu1rc = pregnant-1vwu3mn (post quoted from the BabyBumps copy, one OP reply that exists only in the r/pregnant thread quoted from that copy). No unit mentions Nurava/@nuravaa (grep). Posts in these chunks also quoted in other niches' voice files (checked by post_id): 1uhc2iz, 1vr4mp7 (sleep-mother mr06), 1vag2u0 (sleep-baby r23, sleep-mother mr06), 1vltec9 (toddler-behaviour tr16); none in another pregnancy-birth voice file.

## Every unit

| chunk | unit | status |
|---|---|---|
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uew6kz.txt` | quoted: pb25-0286 … 0289 (4); early loss mentioned in the post; no quote touches it |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ueyzlq.txt` | quoted: pb25-0290 … 0296 (7) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/daddit-1uf8ub7.txt` | quoted: pb25-0297 … 0300 (4) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/BabyBumps-1ufmao9.txt` | quoted: pb25-0301 (1) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ufu4hb.txt` | quoted: pb25-0302 … 0303 (2) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/pregnant-1ug7vi8.txt` | quoted: pb25-0304 … 0308 (5) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/NewParents-1ugflzt.txt` | read; no quote taken (gift-buyer asking about pyjama sizes for a coworker; off-niche) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1uh5cxm.txt` | quoted: pb25-0309 … 0311 (3) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uh7nn5.txt` | quoted: pb25-0312 … 0314 (3) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/daddit-1uhc2iz.txt` | quoted: pb25-0315 … 0318 (4); also quoted in sleep-mother (mr06) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/daddit-1uhs515.txt` | read; no quote taken (reads as AI-assisted (heavy em dashes, polished reflective arc, 0 comments); not quoted) |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uhzjuq.txt` | quoted: pb25-0319 … 0321 (3); statistic in the post not quoted |
| keep_otherside-001 | `../_shared/_raw/reddit-2026/units/pregnant-1uhzxw5.txt` | quoted: pb25-0322 … 0324 (3) |
| keep_otherside-002 | `../_shared/_raw/reddit-2026/units/pregnant-1uikilm.txt` | quoted: pb25-0325 … 0327 (3) |
| keep_otherside-002 | `../_shared/_raw/reddit-2026/units/daddit-1uiy41b.txt` | quoted: pb25-0328 … 0330 (3); a reply mentions substance use and the partner's high-risk pregnancy; not quoted |
| keep_otherside-002 | `../_shared/_raw/reddit-2026/units/Doulas-1uj3tkx.txt` | quoted: pb25-0331 … 0333 (3) |
| keep_otherside-002 | `../_shared/_raw/reddit-2026/units/pregnant-1ujxuwz.txt` | quoted: pb25-0334 … 0338 (5) |
| keep_otherside-002 | `../_shared/_raw/reddit-2026/units/pregnant-1ukjcnu.txt` | quoted: pb25-0339 … 0346 (8) |
| keep_otherside-002 | `../_shared/_raw/reddit-2026/units/pregnant-1ukldyz.txt` | quoted: pb25-0347 … 0348 (2); reply mentions IVF and placenta monitoring; not quoted |
| keep_otherside-002 | `../_shared/_raw/reddit-2026/units/pregnant-1ukma41.txt` | read; no quote taken (relationship breakup from the partner's side; nothing on pregnancy or birth preparation) |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/BabyBumps-1umygvz.txt` | quoted: pb25-0001 … 0003 (3); positive induction story; history mentioned in passing not quoted |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/pregnant-1umznot.txt` | quoted: pb25-0004 … 0007 (4) |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/pregnant-1unfbnw.txt` | quoted: pb25-0008 … 0010 (3) |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1uong86.txt` | quoted: pb25-0011 (1) |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1uoxo5p.txt` | quoted: pb25-0012 … 0016 (5) |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/pregnant-1up3urn.txt` | EXCLUDED: birth story centred on an acute medical emergency and its aftermath |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/BabyBumps-1up6zwq.txt` | quoted: pb25-0017 … 0020 (4) |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/pregnant-1upfb4s.txt` | EXCLUDED: birth story centred on an acute medical emergency |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/pregnant-1upjnzx.txt` | read; no quote taken (single-product recommendation post ("Not an ad I swear"), possible product seeding; also medical content) |
| keep_success-003 | `../_shared/_raw/reddit-2026/units/pregnant-1uqanod.txt` | EXCLUDED: birth story centred on an acute medical emergency |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/BabyBumps-1uqgehr.txt` | EXCLUDED: post centred on a postpartum mental-health struggle |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1uqvjnp.txt` | EXCLUDED: title-only post about an emergency birth |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/pregnant-1ur3ozh.txt` | quoted: pb25-0021 … 0024 (4) |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/pregnant-1urjvvw.txt` | quoted: pb25-0025 (1); post about a condition-led induction; only the feeding-help line quoted |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/beyondthebump-1urydyg.txt` | quoted: pb25-0026 … 0028 (3) |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/daddit-1usytrf.txt` | quoted: pb25-0029 … 0032 (4) |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/pregnant-1ut3bq0.txt` | quoted: pb25-0033 … 0035 (3) |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/BabyBumps-1ut62ir.txt` | read; no quote taken (reads as AI-written or a prompt-style engagement post (\"Small win\", self-experiment, 0 OP replies); not quoted) |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/pregnant-1uta224.txt` | EXCLUDED: birth story centred on an acute medical emergency |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/BabyBumps-1utctbc.txt` | quoted: pb25-0036 … 0038 (3) |
| keep_success-004 | `../_shared/_raw/reddit-2026/units/NewParents-1uv8on2.txt` | quoted: pb25-0039 (1) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1uvepdu.txt` | quoted: pb25-0040 … 0043 (4); borderline: story ends in a postpartum bleed and theatre; kept because it is framed around heat, an unplanned induction and the plan going out the window; bleed passage not quoted, heat/reduced-movement line restricted |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uvswcl.txt` | quoted: pb25-0044 … 0046 (3) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uvwff6.txt` | quoted: pb25-0047 … 0048 (2) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1ux1fnr.txt` | quoted: pb25-0049 … 0050 (2) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uxpa1z.txt` | quoted: pb25-0051 … 0052 (2) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uyodee.txt` | quoted: pb25-0053 … 0055 (3) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1uyxena.txt` | quoted: pb25-0056 … 0061 (6); borderline: ends in an emergency birth; kept for decision-making and hypnobirthing lines, procedure lines restricted |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uz996c.txt` | quoted: pb25-0062 … 0063 (2) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uzd5mb.txt` | quoted: pb25-0064 … 0065 (2); borderline: story ends in a postpartum haemorrhage; kept for the busy-ward and "never again" lines, the latter restricted; bleed passage not quoted |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uziatw.txt` | read; no quote taken (centred on surgery during pregnancy; all content medical) |
| keep_success-005 | `../_shared/_raw/reddit-2026/units/pregnant-1uzjc9j.txt` | quoted: pb25-0066 … 0068 (3) |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1uzvely.txt` | quoted: pb25-0069 … 0070 (2) |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1uzxu9f.txt` | quoted: pb25-0071 … 0075 (5) |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1v0lnm1.txt` | quoted: pb25-0076 … 0079 (4) |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1v14xee.txt` | quoted: pb25-0080 (1); preterm birth; only the maternity-leave timing line quoted, infant-safety questions not quoted |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1v1cm2b.txt` | quoted: pb25-0081 … 0086 (6) |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1v1i3z8.txt` | EXCLUDED: birth story centred on an acute medical emergency |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1v1rhpz.txt` | quoted: pb25-0087 … 0092 (6); listicle may be AI-tidied (bold numbered headings); OP replies read as genuine; one voice |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/BabyBumps-1v229pd.txt` | quoted: pb25-0093 … 0095 (3) |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1v2bp46.txt` | EXCLUDED: birth story centred on an acute medical emergency and its emotional aftermath |
| keep_success-006 | `../_shared/_raw/reddit-2026/units/pregnant-1v3tsty.txt` | quoted: pb25-0096 … 0098 (3) |
| keep_success-007 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1v402lk.txt` | quoted: pb25-0099 … 0109 (11); OP reply on emergency surgery and sepsis not quoted |
| keep_success-007 | `../_shared/_raw/reddit-2026/units/pregnant-1v44k5p.txt` | quoted: pb25-0110 … 0113 (4) |
| keep_success-007 | `../_shared/_raw/reddit-2026/units/pregnant-1v4llxf.txt` | quoted: pb25-0114 … 0116 (3) |
| keep_success-007 | `../_shared/_raw/reddit-2026/units/pregnant-1v52xam.txt` | quoted: pb25-0117 … 0119 (3); birth-injury lines not quoted |
| keep_success-007 | `../_shared/_raw/reddit-2026/units/BabyBumps-1v58pvs.txt` | quoted: pb25-0120 … 0123 (4); newborn admission passage not quoted |
| keep_success-007 | `../_shared/_raw/reddit-2026/units/beyondthebump-1v5hlug.txt` | quoted: pb25-0124 … 0127 (4); birth-injury and therapy lines not quoted |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/pregnant-1v77ozc.txt` | quoted: pb25-0128 … 0134 (7) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/pregnant-1v7b9p3.txt` | read; no quote taken (list of pregnancy conditions; nothing quotable without medical content) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/BabyBumps-1v8n2lf.txt` | quoted: pb25-0135 … 0139 (5) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/beyondthebump-1v8vy91.txt` | read; no quote taken (likely seeded: names Zeel in-home massage, stresses HSA/FSA eligibility, OP reply repeats the HSA point; 'registry useless' hook) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/BabyBumps-1v9b06y.txt` | quoted: pb25-0140 … 0145 (6) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/BabyBumps-1v9d3rc.txt` | quoted: pb25-0146 … 0153 (8) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/pregnant-1v9ibog.txt` | read; no quote taken (generic thank-you post; reply medical) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/pregnant-1v9ochv.txt` | quoted: pb25-0154 … 0156 (3) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1v9vkwj.txt` | quoted: pb25-0157 … 0161 (5) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/pregnant-1v9yrah.txt` | quoted: pb25-0162 (1) |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/beyondthebump-1vag2u0.txt` | quoted: pb25-0163 … 0164 (2); baby 3 months (off-stage); also quoted in other niches |
| keep_success-008 | `../_shared/_raw/reddit-2026/units/pregnant-1vbdvxz.txt` | quoted: pb25-0165 … 0166 (2) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vbi3vh.txt` | quoted: pb25-0167 … 0168 (2) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vc451q.txt` | quoted: pb25-0169 … 0179 (11); reply links an Amazon probiotic (not quoted) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/NewParents-1vcv3gs.txt` | quoted: pb25-0180 … 0181 (2) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vcv6es.txt` | quoted: pb25-0182 … 0187 (6) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/daddit-1vduam1.txt` | quoted: pb25-0188 … 0192 (5) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1ve1ffx.txt` | EXCLUDED: post discusses a named mental-health condition and a panic episode in detail |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vfn3vh.txt` | quoted: pb25-0193 … 0194 (2); symptom lines only; treatment content not quoted |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vfw7bz.txt` | quoted: pb25-0195 … 0197 (3) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vg69kq.txt` | quoted: pb25-0198 … 0200 (3) |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vh4lar.txt` | quoted: pb25-0201 (1); procedure account; only the reading-Reddit line quoted |
| keep_success-009 | `../_shared/_raw/reddit-2026/units/pregnant-1vh7h4i.txt` | quoted: pb25-0202 … 0205 (4) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vhpw3j.txt` | quoted: pb25-0206 … 0208 (3) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vht81g.txt` | EXCLUDED: birth story centred on an acute medical emergency |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1viw8yb.txt` | EXCLUDED: post discusses ending a pregnancy and a severe mental-health period |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vjvt93.txt` | EXCLUDED: crisis wording and thoughts of not continuing the pregnancy |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vk5ww5.txt` | quoted: pb25-0209 … 0213 (5) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vk61nh.txt` | quoted: pb25-0214 … 0216 (3); consent and birth-injury passages not quoted |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vkk2bn.txt` | quoted: pb25-0217 … 0218 (2); young couple, no age given; nothing suggests a minor |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vkobx7.txt` | quoted: pb25-0219 … 0221 (3) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vktkvy.txt` | quoted: pb25-0222 … 0223 (2); procedure account; links Evidence Based Birth; only reading/fear lines quoted |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vky3uu.txt` | quoted: pb25-0224 … 0225 (2) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vl5fjr.txt` | quoted: pb25-0226 (1) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vlno25.txt` | quoted: pb25-0227 … 0228 (2) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/daddit-1vltec9.txt` | quoted: pb25-0229 … 0232 (4); also quoted in toddler-behaviour (tr16) |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vluvxk.txt` | EXCLUDED: acute medical emergency in pregnancy |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/pregnant-1vmk6ym.txt` | EXCLUDED: preterm birth centred on a pregnancy condition and NICU stay |
| keep_success-010 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vmscyv.txt` | quoted: pb25-0233 (1); post makes an outcome claim (no tearing); only one restricted line quoted |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/beyondthebump-1vnirq1.txt` | read; no quote taken (repost: same author, identical text to BabyBumps-1vlno25; quoted once from the first) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/pregnant-1voo5gp.txt` | quoted: pb25-0234 … 0235 (2) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vp4gqc.txt` | EXCLUDED: centred on serious screening findings after prior losses |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/NewParents-1vpjkx0.txt` | quoted: pb25-0236 … 0241 (6) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vpsunm.txt` | quoted: pb25-0242 … 0243 (2) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vqepb4.txt` | quoted: pb25-0244 … 0245 (2); polished/bolded write-up of a home remedy for a skin condition, possibly AI-tidied; crossposted verbatim as pregnant-1vqesty; only family lines quoted, remedy not quoted; one voice |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vqesty.txt` | read; no quote taken (crosspost: same author, same text as PregnancyUK-1vqepb4; quoted once from the first) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vqmuxk.txt` | EXCLUDED: birth story centred on an acute medical emergency |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vqyyr8.txt` | quoted: pb25-0246 … 0249 (4) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vr4mp7.txt` | quoted: pb25-0250 … 0252 (3); also quoted in sleep-mother (mr06) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/pregnant-1vrg9aq.txt` | quoted: pb25-0253 … 0254 (2) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vu6eob.txt` | quoted: pb25-0255 … 0256 (2) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vvgbtm.txt` | quoted: pb25-0257 … 0260 (4) |
| keep_success-011 | `../_shared/_raw/reddit-2026/units/PregnancyUK-1vvhd30.txt` | quoted: pb25-0261 … 0262 (2) |
| keep_success-012 | `../_shared/_raw/reddit-2026/units/pregnant-1vvyx0l.txt` | quoted: pb25-0263 … 0267 (5); condition and treatment replies not quoted |
| keep_success-012 | `../_shared/_raw/reddit-2026/units/pregnant-1vw7xgd.txt` | quoted: pb25-0268 … 0273 (6) |
| keep_success-012 | `../_shared/_raw/reddit-2026/units/pregnant-1vwgbj9.txt` | EXCLUDED: birth story centred on a pregnancy condition and emergency treatment |
| keep_success-012 | `../_shared/_raw/reddit-2026/units/BabyBumps-1vwu1rc.txt` | quoted: pb25-0274 … 0279 (6); crossposted as pregnant-1vwu3mn (same author, same text) |
| keep_success-012 | `../_shared/_raw/reddit-2026/units/pregnant-1vwu3mn.txt` | quoted: pb25-0280 (1); crosspost of BabyBumps-1vwu1rc; one reply quoted from this copy only (not in the other); therapist reply not quoted |
| keep_success-012 | `../_shared/_raw/reddit-2026/units/pregnant-1vwyxx3.txt` | quoted: pb25-0281 … 0282 (2); polished structure, possibly AI-tidied; one voice |
| keep_success-012 | `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1vxd3xh.txt` | quoted: pb25-0283 … 0285 (3); baby 12 weeks (off-stage) |
