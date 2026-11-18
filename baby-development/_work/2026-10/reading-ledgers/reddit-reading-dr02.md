# Reddit full reads — DR02 (development, read-v1 keep_core 005–015)

Reader DR02, 2026-10-25. Brief: `../../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1/chunks.jsonl`. Voice file: `voice/reddit-dr02.jsonl` (ids dv02-0001 to dv02-0388). Builder and per-chunk record lists: `scratchpad/DR02/` (`build.py`, `rec_05.py` … `rec_15.py`; the voice file is generated from them, url/date/post_id/comment_id are derived from the unit text).

## Counts

| step | n |
|---|---|
| chunks assigned | 11 (read-v1-keep_core-005 … 015) |
| units in them | 169 |
| units read in full | 169 |
| units excluded (line not to cross) | 15 |
| duplicate reposts (read; quoted from the first copy only) | 5 |
| units read, kept, no quote | 1 (Mommit-1wih14q) |
| units quoted | 148 |
| quotes written | 388 |
| of which restricted (see notes) | 70 |

Verify: `python3 -I _tools/verify_quotes.py voice/reddit-dr02.jsonl` → `reddit-dr02.jsonl: 388 quotes, 0 failed`.

## Excluded units (not quoted)

| unit | reason |
|---|---|
| `NewParents-1wh9jb6` | centred on a diagnosis referral; excluded |
| `Mommit-1wis5hu` | centred on diagnosis and therapies; excluded |
| `Mommit-1wmqdvl` | centred on a suspected condition and family diagnoses; excluded |
| `beyondthebumpUK-1wo9ry6` | centred on a night-time rolling and choking safe-sleep worry; excluded |
| `NewParents-1wwabxw` | centred on an injury incident during tummy time; excluded |
| `toddlers-1wxanhg` | centred on a possible diagnosis and evaluation; excluded |
| `toddlers-1x5849j` | centred on a possible condition and evaluation; excluded |
| `toddlers-1x5ctzl` | centred on delays, therapies and an injury requiring treatment; excluded |
| `NewParents-1x5s4o4` | centred on a diagnosis and medical history; excluded |
| `toddlers-1x60dzr` | centred on a speech-delay label and ongoing therapy; excluded |
| `Mommit-1x67ezs` | centred on a possible diagnosis checklist; excluded |
| `toddlers-1xb16wc` | centred on an evaluation with delay scores and therapies; excluded |
| `NewParents-1xbouyz` | centred on medical symptoms and possible conditions; excluded |
| `NewParents-1xbtpx3` | centred on a safe-sleep question about rolling in a bedside crib; excluded |
| `toddlers-1xcr7r1` | centred on an assessment referral and self-injury; excluded |

Borderline keep: `toddlers-1woenzo` names a worry about a condition but is not on a diagnosis or therapy path; three lines about the paediatrician's milestone survey and self-blame were kept (no condition named, all restricted). Comparable `Mommit-1wis5hu` was excluded because it is centred on active therapies and specialist work-up. The orchestrator may overrule.

Post-review fixes (same ids, same quotes): speaker relabelled on 34 records under the strict self-identification rule; 2 types changed purchase → desire (intent only); context stubs ('Same post.') expanded with the unit's first context; seed themes listed first; trim marker normalised to ` […] ` in 2 quotes. All applied in `scratchpad/DR02/build.py`.

## Duplicates and no-quote units

| unit | note |
|---|---|
| `NewParents-1wyigfn` | duplicate repost of Parenting-1wthk3u; read, nothing new |
| `toddlers-1x07s3a` | duplicate repost of NewParents-1x06dq6; read, nothing new |
| `NewParents-1x546o7` | duplicate repost of sahm-1x545s9; read, nothing new |
| `Mommit-1x7s985` | duplicate repost of toddlers-1x7s37c; read, nothing new |
| `Mommit-1wih14q` | read in full; nothing on-topic (fear of objects at 8 months) |
| `NewParents-1wjv84e` | duplicate repost of beyondthebump-1wjv6uf; read, nothing new |

Cross-posts quoted from more than one copy (only where the OP's replies differ): sahm-1wjqfp4 / NewParents-1wjqguz / Mommit-1wjqhxl; NewParents-1wnghqd / toddlers-1wnjyse; toddlers-1wrl9fk / Parenting-1wrodc7; Mommit-1x3btko / Parenting-1x3c1c6; Parenting-1x4hwnu / toddlers-1x4i0wo. Each quote is a different sentence; no sentence is quoted twice.

## Unit by unit

| chunk | unit | quotes | ids |
|---|---|---|---|
| 005 | `Mommit-1wepicm` | 4 | dv02-0001–dv02-0004 |
| 005 | `beyondthebump-1wf0bf8` | 3 | dv02-0005–dv02-0007 |
| 005 | `NewParents-1wf2td9` | 3 | dv02-0008–dv02-0010 |
| 005 | `toddlers-1wf4fm3` | 2 | dv02-0011–dv02-0012 |
| 005 | `NewParents-1wf888l` | 6 | dv02-0013–dv02-0018 |
| 005 | `beyondthebump-1wfejtm` | 4 | dv02-0019–dv02-0022 |
| 005 | `NewParents-1wfuzs1` | 3 | dv02-0023–dv02-0025 |
| 005 | `NewParents-1wg4k2b` | 3 | dv02-0026–dv02-0028 |
| 005 | `NewParents-1wg5key` | 1 | dv02-0029–dv02-0029 |
| 005 | `Parenting-1wgcj0e` | 3 | dv02-0030–dv02-0032 |
| 005 | `NewParents-1wgf774` | 3 | dv02-0033–dv02-0035 |
| 005 | `NewParents-1wgrv8w` | 1 | dv02-0036–dv02-0036 |
| 005 | `Mommit-1wgv0vj` | 3 | dv02-0037–dv02-0039 |
| 005 | `beyondthebump-1wh3zz3` | 2 | dv02-0040–dv02-0041 |
| 005 | `NewParents-1wh6kij` | 2 | dv02-0042–dv02-0043 |
| 005 | `NewParents-1wh9jb6` | 0 | excluded |
| 006 | `beyondthebump-1whfeqz` | 5 | dv02-0044–dv02-0048 |
| 006 | `NewParents-1whv9kl` | 5 | dv02-0049–dv02-0053 |
| 006 | `toddlers-1whzo26` | 1 | dv02-0054–dv02-0054 |
| 006 | `toddlers-1wi77tp` | 1 | dv02-0055–dv02-0055 |
| 006 | `toddlers-1wi9fbm` | 1 | dv02-0056–dv02-0056 |
| 006 | `Mommit-1wih14q` | 0 | read, none |
| 006 | `Mommit-1wis5hu` | 0 | excluded |
| 006 | `Mommit-1wiwx4b` | 4 | dv02-0057–dv02-0060 |
| 006 | `beyondthebump-1wjlkb5` | 4 | dv02-0061–dv02-0064 |
| 006 | `beyondthebump-1wjpfjw` | 2 | dv02-0065–dv02-0066 |
| 006 | `sahm-1wjqfp4` | 5 | dv02-0067–dv02-0071 |
| 006 | `NewParents-1wjqguz` | 2 | dv02-0072–dv02-0073 |
| 006 | `Mommit-1wjqhxl` | 1 | dv02-0074–dv02-0074 |
| 006 | `beyondthebump-1wjv6uf` | 1 | dv02-0075–dv02-0075 |
| 006 | `NewParents-1wjv84e` | 0 | read, none |
| 007 | `Mommit-1wk5egr` | 3 | dv02-0076–dv02-0078 |
| 007 | `NewParents-1wk9fpu` | 3 | dv02-0079–dv02-0081 |
| 007 | `NewParents-1wlq3lh` | 2 | dv02-0082–dv02-0083 |
| 007 | `NewParents-1wlqlqr` | 6 | dv02-0084–dv02-0089 |
| 007 | `beyondthebump-1wlqmtu` | 4 | dv02-0090–dv02-0093 |
| 007 | `FirstTimeMom-1wltf5u` | 1 | dv02-0094–dv02-0094 |
| 007 | `Parenting-1wm3mlq` | 5 | dv02-0095–dv02-0099 |
| 007 | `beyondthebumpUK-1wmanjx` | 3 | dv02-0100–dv02-0102 |
| 007 | `NewParents-1wme0g4` | 3 | dv02-0103–dv02-0105 |
| 007 | `NewParents-1wmhsud` | 2 | dv02-0106–dv02-0107 |
| 007 | `FirstTimeMom-1wmkkjs` | 3 | dv02-0108–dv02-0110 |
| 007 | `Mommit-1wmqdvl` | 0 | excluded |
| 007 | `NewParents-1wnghqd` | 1 | dv02-0111–dv02-0111 |
| 007 | `toddlers-1wnjyse` | 1 | dv02-0112–dv02-0112 |
| 007 | `NewParents-1wnl5op` | 1 | dv02-0113–dv02-0113 |
| 007 | `NewParents-1wnuiq4` | 3 | dv02-0114–dv02-0116 |
| 007 | `Mommit-1wo3vcx` | 3 | dv02-0117–dv02-0119 |
| 007 | `Parenting-1wo7nc0` | 3 | dv02-0120–dv02-0122 |
| 008 | `beyondthebumpUK-1wo9ry6` | 0 | excluded |
| 008 | `toddlers-1woenzo` | 3 | dv02-0123–dv02-0125 |
| 008 | `daddit-1wp7t93` | 3 | dv02-0126–dv02-0128 |
| 008 | `beyondthebump-1wpdb29` | 7 | dv02-0129–dv02-0135 |
| 008 | `NewParents-1wpu3ic` | 2 | dv02-0136–dv02-0137 |
| 008 | `Mommit-1wpx8bp` | 2 | dv02-0138–dv02-0139 |
| 008 | `Parenting-1wq150o` | 2 | dv02-0140–dv02-0141 |
| 008 | `Mommit-1wq8emy` | 3 | dv02-0142–dv02-0144 |
| 008 | `FirstTimeMom-1wqbuvt` | 3 | dv02-0145–dv02-0147 |
| 008 | `beyondthebump-1wqjjeq` | 3 | dv02-0148–dv02-0150 |
| 008 | `Mommit-1wr2fll` | 2 | dv02-0151–dv02-0152 |
| 008 | `NewParents-1wre8jt` | 3 | dv02-0153–dv02-0155 |
| 008 | `NewParents-1wrhhfx` | 4 | dv02-0156–dv02-0159 |
| 008 | `toddlers-1wrl9fk` | 1 | dv02-0161–dv02-0161 |
| 008 | `Parenting-1wrodc7` | 1 | dv02-0160–dv02-0160 |
| 008 | `toddlers-1wscqvg` | 3 | dv02-0162–dv02-0164 |
| 008 | `toddlers-1wsohvm` | 2 | dv02-0165–dv02-0166 |
| 008 | `NewParents-1wsot36` | 1 | dv02-0167–dv02-0167 |
| 009 | `Mommit-1wsymut` | 3 | dv02-0168–dv02-0170 |
| 009 | `beyondthebumpUK-1wt5gvm` | 1 | dv02-0171–dv02-0171 |
| 009 | `Parenting-1wthk3u` | 2 | dv02-0172–dv02-0173 |
| 009 | `sahm-1wtlpmp` | 3 | dv02-0174–dv02-0176 |
| 009 | `NewParents-1wtrul4` | 4 | dv02-0177–dv02-0180 |
| 009 | `ScienceBasedParenting-1wty7r4` | 1 | dv02-0181–dv02-0181 |
| 009 | `NewParents-1wtziuw` | 2 | dv02-0182–dv02-0183 |
| 009 | `NewParents-1wu1fvd` | 3 | dv02-0184–dv02-0186 |
| 009 | `NewParents-1wu625l` | 1 | dv02-0187–dv02-0187 |
| 009 | `Parenting-1wuddof` | 1 | dv02-0188–dv02-0188 |
| 009 | `NewParents-1wv5m3a` | 3 | dv02-0189–dv02-0191 |
| 009 | `beyondthebump-1wvbvjv` | 2 | dv02-0192–dv02-0193 |
| 009 | `NewParents-1wvcfdp` | 1 | dv02-0194–dv02-0194 |
| 009 | `NewParents-1wvd34l` | 2 | dv02-0195–dv02-0196 |
| 009 | `beyondthebump-1ww43wi` | 8 | dv02-0197–dv02-0204 |
| 009 | `beyondthebumpUK-1ww528v` | 3 | dv02-0205–dv02-0207 |
| 009 | `Mommit-1ww7xtr` | 2 | dv02-0208–dv02-0209 |
| 009 | `NewParents-1wwabxw` | 0 | excluded |
| 009 | `Parenting-1www9f8` | 2 | dv02-0210–dv02-0211 |
| 009 | `NewParents-1wwx70o` | 1 | dv02-0212–dv02-0212 |
| 010 | `toddlers-1wxanhg` | 0 | excluded |
| 010 | `NewParents-1wxgyl8` | 3 | dv02-0213–dv02-0215 |
| 010 | `NewParents-1wxk3b6` | 5 | dv02-0216–dv02-0220 |
| 010 | `NewParents-1wxwa7z` | 2 | dv02-0221–dv02-0222 |
| 010 | `Mommit-1wxwdtu` | 3 | dv02-0223–dv02-0225 |
| 010 | `NewParents-1wyigfn` | 0 | read, none |
| 010 | `toddlers-1wyx3xy` | 2 | dv02-0226–dv02-0227 |
| 010 | `toddlers-1wyzboq` | 6 | dv02-0228–dv02-0233 |
| 010 | `NewParents-1wz5px3` | 1 | dv02-0234–dv02-0234 |
| 010 | `beyondthebump-1wzb5tb` | 2 | dv02-0235–dv02-0236 |
| 010 | `NewParents-1wzcr8t` | 2 | dv02-0237–dv02-0238 |
| 010 | `sahm-1wzd851` | 1 | dv02-0239–dv02-0239 |
| 010 | `Mommit-1wzdqsk` | 3 | dv02-0240–dv02-0242 |
| 011 | `beyondthebump-1wzdsew` | 1 | dv02-0243–dv02-0243 |
| 011 | `beyondthebump-1wzi3lu` | 4 | dv02-0244–dv02-0247 |
| 011 | `NewParents-1wzk3f6` | 4 | dv02-0248–dv02-0251 |
| 011 | `NewParents-1wzr5u9` | 1 | dv02-0252–dv02-0252 |
| 011 | `NewParents-1x06dq6` | 2 | dv02-0253–dv02-0254 |
| 011 | `toddlers-1x07s3a` | 0 | read, none |
| 011 | `toddlers-1x0gojn` | 2 | dv02-0255–dv02-0256 |
| 011 | `beyondthebumpUK-1x0yl00` | 2 | dv02-0257–dv02-0258 |
| 011 | `NewParents-1x10awl` | 2 | dv02-0259–dv02-0260 |
| 011 | `ScienceBasedParenting-1x10s8t` | 1 | dv02-0261–dv02-0261 |
| 011 | `NewParents-1x19rgp` | 2 | dv02-0262–dv02-0263 |
| 011 | `NewParents-1x1g0do` | 2 | dv02-0264–dv02-0265 |
| 011 | `NewParents-1x2lx82` | 1 | dv02-0266–dv02-0266 |
| 011 | `Mommit-1x2uvst` | 3 | dv02-0267–dv02-0269 |
| 011 | `ScienceBasedParenting-1x3883z` | 2 | dv02-0270–dv02-0271 |
| 011 | `Mommit-1x3btko` | 1 | dv02-0272–dv02-0272 |
| 011 | `Parenting-1x3c1c6` | 1 | dv02-0273–dv02-0273 |
| 011 | `Parenting-1x4bc0t` | 2 | dv02-0274–dv02-0275 |
| 011 | `toddlers-1x4dwg0` | 4 | dv02-0276–dv02-0279 |
| 012 | `Parenting-1x4hwnu` | 4 | dv02-0280–dv02-0283 |
| 012 | `toddlers-1x4i0wo` | 1 | dv02-0284–dv02-0284 |
| 012 | `Mommit-1x4tlc2` | 3 | dv02-0285–dv02-0287 |
| 012 | `sahm-1x545s9` | 4 | dv02-0288–dv02-0291 |
| 012 | `NewParents-1x546o7` | 0 | read, none |
| 012 | `toddlers-1x5849j` | 0 | excluded |
| 012 | `NewParents-1x5as55` | 5 | dv02-0292–dv02-0296 |
| 012 | `toddlers-1x5ctzl` | 0 | excluded |
| 012 | `NewParents-1x5hexk` | 2 | dv02-0297–dv02-0298 |
| 012 | `beyondthebumpUK-1x5mtr9` | 3 | dv02-0299–dv02-0301 |
| 013 | `beyondthebumpUK-1x5pjq1` | 2 | dv02-0302–dv02-0303 |
| 013 | `NewParents-1x5rye7` | 2 | dv02-0304–dv02-0305 |
| 013 | `NewParents-1x5s4o4` | 0 | excluded |
| 013 | `NewParents-1x5vq15` | 4 | dv02-0306–dv02-0309 |
| 013 | `toddlers-1x60dzr` | 0 | excluded |
| 013 | `beyondthebump-1x644r2` | 3 | dv02-0310–dv02-0312 |
| 013 | `toddlers-1x6581u` | 2 | dv02-0313–dv02-0314 |
| 013 | `Mommit-1x65xz1` | 2 | dv02-0315–dv02-0316 |
| 013 | `NewParents-1x66wvv` | 3 | dv02-0317–dv02-0319 |
| 013 | `Mommit-1x67ezs` | 0 | excluded |
| 013 | `NewParents-1x6i01w` | 10 | dv02-0320–dv02-0329 |
| 013 | `beyondthebump-1x6rh4h` | 3 | dv02-0330–dv02-0332 |
| 014 | `beyondthebump-1x74ag0` | 1 | dv02-0333–dv02-0333 |
| 014 | `beyondthebump-1x76rfb` | 2 | dv02-0334–dv02-0335 |
| 014 | `toddlers-1x7s37c` | 5 | dv02-0336–dv02-0340 |
| 014 | `Mommit-1x7s985` | 0 | read, none |
| 014 | `beyondthebumpUK-1x7sze4` | 3 | dv02-0341–dv02-0343 |
| 014 | `NewParents-1x8cfgo` | 1 | dv02-0344–dv02-0344 |
| 014 | `NewParents-1x8r3g7` | 3 | dv02-0345–dv02-0347 |
| 014 | `Mommit-1x8tvcu` | 1 | dv02-0348–dv02-0348 |
| 014 | `ScienceBasedParenting-1x9dnhp` | 1 | dv02-0349–dv02-0349 |
| 014 | `Mommit-1x9jbbd` | 2 | dv02-0350–dv02-0351 |
| 014 | `sahm-1xa0kwq` | 7 | dv02-0352–dv02-0358 |
| 014 | `NewParents-1xadi8b` | 2 | dv02-0359–dv02-0360 |
| 015 | `toddlers-1xb16wc` | 0 | excluded |
| 015 | `NewParents-1xb9uoh` | 5 | dv02-0361–dv02-0365 |
| 015 | `NewParents-1xbouyz` | 0 | excluded |
| 015 | `NewParents-1xbtpx3` | 0 | excluded |
| 015 | `Mommit-1xc7plk` | 2 | dv02-0366–dv02-0367 |
| 015 | `beyondthebumpUK-1xcmtta` | 5 | dv02-0368–dv02-0372 |
| 015 | `NewParents-1xcndmt` | 2 | dv02-0373–dv02-0374 |
| 015 | `toddlers-1xcr7r1` | 0 | excluded |
| 015 | `NewParents-1xcu3a1` | 2 | dv02-0375–dv02-0376 |
| 015 | `Parenting-1xcv3jb` | 2 | dv02-0377–dv02-0378 |
| 015 | `Mommit-1xd2mgy` | 1 | dv02-0379–dv02-0379 |
| 015 | `beyondthebump-1xdoukq` | 2 | dv02-0380–dv02-0381 |
| 015 | `NewParents-1xdz6c1` | 2 | dv02-0382–dv02-0383 |
| 015 | `NewParents-1xe8osp` | 1 | dv02-0384–dv02-0384 |
| 015 | `NewParents-1xem2d8` | 2 | dv02-0385–dv02-0386 |
| 015 | `toddlers-1xemb4s` | 2 | dv02-0387–dv02-0388 |

## How to continue

All assigned units are read. Nothing unread. Do not re-run this reader on the same voice file; if the chunks need re-reading, use a new prefix.

