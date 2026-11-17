# UR10 unfilter re-read ledger

Completed 2026-11-17. Assignment: `scratchpad/unfilter-reread/assign-ur10.tsv`. Read offline; no network or git. Only this ledger and `voice/reddit-ur10.jsonl` were written. Historical exclusion reasons were treated as history, never as instructions.

## Counts and reading scope

| Measure | Count |
|---|---:|
| Rows assigned | 293 |
| Assigned units located | 293 |
| Assigned units read, including all text available in listing-only units | 293 |
| Complete saved source-unit captures read | 289 |
| Listing-only units: full discussion text not available on disk | 4 |
| Unit IDs / raw paths not found | 0 |
| Units quoted | 288 |
| Units with no quote | 5 |
| Quotes written | 385 |
| Quotes verified against decoded native text | 385 |
| Final exact-match, vocabulary, context-length, duplicate-ID and existing-excerpt errors | 0 |

The assignment was overwhelmingly on subject: **288 of 293 units yielded relevant new material**. Only five units said nothing about the subject in the saved text. No unit was rejected because of illness, crisis, loss, coercion, age, clinical detail, provenance or potential suitability for copy.

“Complete saved source unit” does not mean a complete live Reddit discussion. All 36 JustParents JSON threads were read through every saved post; their pagination-complete flags are true. Both GeoBaby text threads and both MSE text threads were read in full, including quoted context. All 11 saved Q&A threads were read through their questions, answers and comments. Reddit unit files were read through the complete original and every saved identifiable OP reply. The three gzip assignments were located by exact submission ID and their complete title/selftext read. Missing publisher comments, linked pages and external images were not retrieved or claimed read.

Full text is unavailable for `geo-146541`, `mse-4726793`, `mse-5141262` and `mse-5522325`: only their saved listing records exist in the assigned bundles. The first has a title and an empty excerpt; the other three have excerpts, two visibly truncated. Their surviving relevant words are retained. Nothing about absent replies or missing endings is inferred.

Existing `voice/*.jsonl` excerpts were checked by raw path, native unit/post/question identity and `raw_thread_json` where present. Existing excerpts were not repeated. Repeated quotations of earlier forum posts were read as context, not counted as independent voices. Commercial and second-hand accounts remain labelled in context/evidence_kind. No authorship was declared AI-generated merely from writing style. No new clinical diagnosis, effectiveness claim or population estimate is inferred.

## Assigned-row ledger

One line per assignment row, in assignment order. Counts refer to new UR10 quote records. “Full saved text” carries the source-specific limits above.

| Unit id | Quotes | Quote ids | Read status / no-quote reason |
|---|---:|---|---|
| jp-10 | 2 | glu10-0001, glu10-0002 | Full saved JSON thread; every post |
| jp-10099 | 1 | glu10-0003 | Full saved JSON thread; every post |
| jp-10444 | 2 | glu10-0004, glu10-0005 | Full saved JSON thread; every post |
| jp-10513 | 1 | glu10-0008 | Full saved JSON thread; every post |
| jp-10517 | 2 | glu10-0006, glu10-0007 | Full saved JSON thread; every post |
| jp-1066 | 0 | — | says nothing about the subject; music-stream promotion and scheduling replies contain no parenting or pregnancy content. |
| jp-10722 | 2 | glu10-0009, glu10-0010 | Full saved JSON thread; every post |
| jp-10911 | 1 | glu10-0011 | Full saved JSON thread; every post |
| jp-1119 | 1 | glu10-0012 | Full saved JSON thread; every post |
| jp-1168 | 2 | glu10-0013, glu10-0014 | Full saved JSON thread; every post |
| jp-1292 | 2 | glu10-0015, glu10-0016 | Full saved JSON thread; every post |
| jp-1420 | 0 | — | says nothing about the subject; perfume sales and distributor recruitment contain no parenting or pregnancy content. |
| jp-1569 | 1 | glu10-0017 | Full saved JSON thread; every post |
| jp-1621 | 3 | glu10-0018, glu10-0019, glu10-0020 | Full saved JSON thread; every post |
| jp-2409 | 0 | — | says nothing about the subject; handmade jewellery promotion and generic shopping replies contain no parenting or pregnancy content. |
| jp-2440 | 1 | glu10-0021 | Full saved JSON thread; every post |
| jp-2614 | 1 | glu10-0022 | Full saved JSON thread; every post |
| jp-2642 | 4 | glu10-0023, glu10-0024, glu10-0025, glu10-0026 | Full saved JSON thread; every post |
| jp-3050 | 1 | glu10-0027 | Full saved JSON thread; every post |
| jp-3560 | 2 | glu10-0028, glu10-0029 | Full saved JSON thread; every post |
| jp-4272 | 2 | glu10-0030, glu10-0031 | Full saved JSON thread; every post |
| jp-4620 | 1 | glu10-0032 | Full saved JSON thread; every post |
| jp-5948 | 2 | glu10-0033, glu10-0034 | Full saved JSON thread; every post |
| jp-5954 | 2 | glu10-0035, glu10-0036 | Full saved JSON thread; every post |
| jp-6728 | 2 | glu10-0037, glu10-0038 | Full saved JSON thread; every post |
| jp-7366 | 1 | glu10-0039 | Full saved JSON thread; every post |
| jp-7827 | 1 | glu10-0040 | Full saved JSON thread; every post |
| jp-8505 | 1 | glu10-0041 | Full saved JSON thread; every post |
| jp-8753 | 1 | glu10-0042 | Full saved JSON thread; every post |
| jp-8760 | 1 | glu10-0043 | Full saved JSON thread; every post |
| jp-9163 | 2 | glu10-0044, glu10-0045 | Full saved JSON thread; every post |
| jp-9292 | 1 | glu10-0046 | Full saved JSON thread; every post |
| jp-9422 | 1 | glu10-0047 | Full saved JSON thread; every post |
| jp-9569 | 1 | glu10-0048 | Full saved JSON thread; every post |
| jp-9917 | 2 | glu10-0049, glu10-0050 | Full saved JSON thread; every post |
| jp-9961 | 1 | glu10-0051 | Full saved JSON thread; every post |
| geo-127563 | 2 | glu10-0052, glu10-0053 | Full saved thread; existing odeep02-0020 not repeated |
| geo-174573 | 2 | glu10-0054, glu10-0055 | Full saved thread |
| geo-146541 | 1 | glu10-0056 | Listing title only; empty excerpt; full discussion text not available |
| mse-5502030 | 3 | glu10-0057, glu10-0058, glu10-0059 | Full saved thread; existing odeep04-0071 not repeated |
| mse-6092956 | 2 | glu10-0060, glu10-0061 | Full saved thread |
| mse-4726793 | 1 | glu10-0062 | Saved truncated listing excerpt read; full discussion and ending not available |
| mse-5141262 | 1 | glu10-0063 | Saved listing excerpt read; full discussion text not available |
| mse-5522325 | 0 | — | says nothing about the subject in the saved excerpt; adult leukaemia and work absence only. Full thread text not available. |
| qa-39445 | 5 | glu10-0064, glu10-0065, glu10-0066, glu10-0067, glu10-0068 | Full saved API thread |
| qa-40220 | 1 | glu10-0069 | Full saved API thread |
| qa-40226 | 2 | glu10-0070, glu10-0071 | Full saved API thread |
| qa-40806 | 2 | glu10-0072, glu10-0073 | Full saved API thread |
| qa-40814 | 2 | glu10-0074, glu10-0075 | Full saved API thread |
| qa-41305 | 2 | glu10-0076, glu10-0077 | Full saved API thread |
| qa-41506 | 1 | glu10-0078 | Full saved API thread |
| qa-42252 | 3 | glu10-0079, glu10-0080, glu10-0081 | Full saved API thread |
| qa-43450 | 1 | glu10-0082 | Full saved API thread |
| qa-44105 | 2 | glu10-0083, glu10-0084 | Full saved API thread |
| qa-44312 | 1 | glu10-0085 | Full saved API thread |
| 1melu71 | 1 | glu10-0086 | Full saved text |
| 1miwi9l | 2 | glu10-0087, glu10-0088 | Full saved text |
| 1mmskr8 | 1 | glu10-0089 | Full saved text |
| 1mqmjly | 2 | glu10-0090, glu10-0091 | Full saved text |
| 1mynpne | 1 | glu10-0092 | Full saved text |
| 1n1l1te | 2 | glu10-0093, glu10-0094 | Full saved text |
| 1n31qcg | 1 | glu10-0095 | Full saved text |
| 1narssq | 1 | glu10-0096 | Full saved text |
| 1nb1ljf | 1 | glu10-0097 | Full saved text |
| 1nivwut | 2 | glu10-0098, glu10-0099 | Full saved text |
| 1nsqa0e | 1 | glu10-0100 | Full saved text |
| 1nvrtv5 | 1 | glu10-0101 | Full saved text |
| 1o1p0q3 | 1 | glu10-0102 | Full saved text |
| 1oauvcy | 1 | glu10-0103 | Full saved text |
| 1obq4lz | 1 | glu10-0104 | Full saved text |
| 1ocg90k | 1 | glu10-0105 | Full saved text |
| 1ocl796 | 1 | glu10-0106 | Full saved text |
| 1odrrcl | 1 | glu10-0107 | Full saved text |
| 1oejb9f | 1 | glu10-0108 | Full saved text |
| 1of4nul | 1 | glu10-0109 | Full saved text |
| 1oh7k2q | 2 | glu10-0110, glu10-0111 | Full saved text |
| 1omik1h | 1 | glu10-0112 | Full saved text |
| 1ou485d | 1 | glu10-0113 | Full saved text |
| 1ouq5sg | 1 | glu10-0114 | Full saved text |
| 1ourvku | 1 | glu10-0115 | Full saved text |
| 1p8kizu | 1 | glu10-0116 | Full saved text |
| 1p9c4sf | 1 | glu10-0117 | Full saved text |
| 1pb75ll | 1 | glu10-0118 | Full saved text |
| 1pc817b | 1 | glu10-0119 | Full saved text |
| 1pk2pvl | 2 | glu10-0120, glu10-0121 | Full saved text |
| 1pnx3y5 | 1 | glu10-0122 | Full saved text |
| 1prpubp | 2 | glu10-0123, glu10-0124 | Full saved text |
| 1pspsw9 | 1 | glu10-0125 | Full saved text |
| 1pw3kfs | 1 | glu10-0126 | Full saved text |
| 1pxyy2n | 2 | glu10-0127, glu10-0128 | Full saved text |
| 1pyesei | 2 | glu10-0129, glu10-0130 | Full saved text |
| 1n01hco | 1 | glu10-0131 | Full saved text |
| 1n3zcga | 1 | glu10-0132 | Full saved text |
| 1n49e6a | 1 | glu10-0133 | Full saved text |
| 1p7id1p | 1 | glu10-0134 | Full saved text |
| 1pdlo4w | 1 | glu10-0135 | Full saved text |
| 1mkeb4s | 1 | glu10-0136 | Full saved text |
| 1o3q0a0 | 1 | glu10-0137 | Full saved text |
| 1oi0t8u | 0 | — | says nothing about the subject; trading, bank and wage-advance referral offers contain no parenting or pregnancy content. |
| 1pe89q4 | 2 | glu10-0138, glu10-0139 | Full saved text |
| 1pilryd | 1 | glu10-0140 | Full saved text |
| 1mqze3l | 3 | glu10-0141, glu10-0142, glu10-0143 | Full saved text |
| 1myan24 | 1 | glu10-0144 | Full saved text |
| 1oaw3md | 1 | glu10-0145 | Full saved text |
| 1ocb8tl | 1 | glu10-0146 | Full saved text |
| 1p1jsec | 1 | glu10-0147 | Full saved text |
| 1ptjesm | 1 | glu10-0148 | Full saved text |
| 1pttb1l | 1 | glu10-0149 | Full saved text |
| 1mej0wt | 1 | glu10-0150 | Full saved text |
| 1mgzxec | 1 | glu10-0151 | Full saved text |
| 1mi5ma5 | 1 | glu10-0152 | Full saved text |
| 1miqk1v | 1 | glu10-0153 | Full saved text |
| 1moqyd4 | 1 | glu10-0154 | Full saved text |
| 1mtk4wp | 1 | glu10-0155 | Full saved text |
| 1mxljet | 1 | glu10-0156 | Full saved text |
| 1mzra4l | 2 | glu10-0157, glu10-0158 | Full saved text |
| 1nay83e | 1 | glu10-0159 | Full saved text |
| 1ned18d | 1 | glu10-0160 | Full saved text |
| 1ngxzf5 | 1 | glu10-0161 | Full saved text |
| 1nko9fm | 1 | glu10-0162 | Full saved text |
| 1nl6x61 | 1 | glu10-0163 | Full saved text |
| 1nphw4y | 2 | glu10-0164, glu10-0165 | Full saved text |
| 1nqhiw7 | 2 | glu10-0166, glu10-0167 | Full saved text |
| 1ny893o | 3 | glu10-0168, glu10-0169, glu10-0170 | Full saved text |
| 1nywrgb | 2 | glu10-0171, glu10-0172 | Full saved text |
| 1o5s5me | 2 | glu10-0173, glu10-0174 | Full saved text |
| 1o6f9ea | 1 | glu10-0175 | Full saved text |
| 1o6fczf | 1 | glu10-0176 | Full saved text |
| 1oh0h98 | 2 | glu10-0177, glu10-0178 | Full saved text |
| 1ouriv4 | 1 | glu10-0179 | Full saved text |
| 1owqvkj | 2 | glu10-0180, glu10-0181 | Full saved text |
| 1owz5gw | 1 | glu10-0182 | Full saved text |
| 1oxl13y | 1 | glu10-0183 | Full saved text |
| 1p0giwi | 1 | glu10-0184 | Full saved text |
| 1p2ya01 | 2 | glu10-0185, glu10-0186 | Full saved text |
| 1p5n2m5 | 1 | glu10-0187 | Full saved text |
| 1p8ott2 | 2 | glu10-0188, glu10-0189 | Full saved text |
| 1pgqv0z | 1 | glu10-0190 | Full saved text |
| 1pi29ak | 1 | glu10-0191 | Full saved text |
| 1pil0jy | 2 | glu10-0192, glu10-0193 | Full saved text |
| 1pppcqm | 1 | glu10-0194 | Full saved text |
| 1pqw219 | 1 | glu10-0195 | Full saved text |
| 1pvi42x | 1 | glu10-0196 | Full saved text |
| 1mhn8r2 | 1 | glu10-0197 | Full saved text |
| 1mlfywh | 2 | glu10-0198, glu10-0199 | Full saved text |
| 1mnk1tp | 1 | glu10-0200 | Full saved text |
| 1mo769h | 1 | glu10-0201 | Full saved text |
| 1moj974 | 2 | glu10-0202, glu10-0203 | Full saved text |
| 1mokl3d | 1 | glu10-0204 | Full saved text |
| 1msfl03 | 1 | glu10-0205 | Full saved text |
| 1mxgchf | 2 | glu10-0206, glu10-0207 | Full saved text |
| 1n1vk26 | 1 | glu10-0208 | Full saved text |
| 1n48fiq | 1 | glu10-0209 | Full saved text |
| 1n4p6uo | 1 | glu10-0210 | Full saved text |
| 1nbhq05 | 1 | glu10-0211 | Full saved text |
| 1ncc30u | 2 | glu10-0212, glu10-0213 | Full saved text |
| 1nde062 | 1 | glu10-0214 | Full saved text |
| 1nr7dlu | 1 | glu10-0215 | Full saved text |
| 1nvnxzf | 1 | glu10-0216 | Full saved text |
| 1nwcm14 | 6 | glu10-0217, glu10-0218, glu10-0219, glu10-0220, glu10-0221, glu10-0222 | Full saved text |
| 1o03j1n | 1 | glu10-0223 | Full saved text |
| 1o1ltcw | 1 | glu10-0224 | Full saved text |
| 1o33wms | 1 | glu10-0225 | Full saved text |
| 1o79mfp | 1 | glu10-0226 | Full saved text |
| 1o8zwci | 1 | glu10-0227 | Full saved text |
| 1obffcc | 1 | glu10-0228 | Full saved text |
| 1od2nhh | 1 | glu10-0229 | Full saved text |
| 1ofohhk | 1 | glu10-0230 | Full saved text |
| 1olzn7b | 4 | glu10-0231, glu10-0232, glu10-0233, glu10-0234 | Full saved text |
| 1opk2vq | 2 | glu10-0235, glu10-0236 | Full saved text |
| 1ot7qno | 1 | glu10-0237 | Full saved text |
| 1p0n1xh | 1 | glu10-0238 | Full saved text |
| 1pc165x | 1 | glu10-0239 | Full saved text |
| 1pdyip7 | 1 | glu10-0240 | Full saved text |
| 1pjwp0k | 2 | glu10-0241, glu10-0242 | Full saved text |
| 1pk6ls7 | 1 | glu10-0243 | Full saved text |
| 1pp1711 | 1 | glu10-0244 | Full saved text |
| 1pqmo67 | 3 | glu10-0245, glu10-0246, glu10-0247 | Full saved text |
| 1pwpiai | 1 | glu10-0248 | Full saved text |
| 1mexu8m | 1 | glu10-0249 | Full saved text |
| 1mfajqv | 2 | glu10-0250, glu10-0251 | Full saved text |
| 1mhpzwp | 1 | glu10-0252 | Full saved text |
| 1mlxt1w | 1 | glu10-0253 | Full saved text |
| 1mqd8ij | 1 | glu10-0254 | Full saved text |
| 1muzh81 | 1 | glu10-0255 | Full saved text |
| 1n1inu8 | 1 | glu10-0256 | Full saved text |
| 1n2n7k0 | 2 | glu10-0257, glu10-0258 | Full saved text |
| 1n7onwb | 1 | glu10-0259 | Full saved text |
| 1nbr62f | 1 | glu10-0260 | Full saved text |
| 1ndjld5 | 2 | glu10-0261, glu10-0262 | Full saved text |
| 1ngovl6 | 1 | glu10-0263 | Full saved text |
| 1njivo8 | 2 | glu10-0264, glu10-0265 | Full saved text |
| 1nlcmzv | 1 | glu10-0266 | Full saved text |
| 1nlobc1 | 2 | glu10-0267, glu10-0268 | Full saved text |
| 1nlox00 | 1 | glu10-0269 | Full saved text |
| 1no8phr | 1 | glu10-0270 | Full saved text |
| 1nw96mh | 1 | glu10-0271 | Full saved post text; linked photos not available in assigned unit; no visual interpretation |
| 1nwragd | 1 | glu10-0272 | Full saved text |
| 1o1j5hv | 1 | glu10-0273 | Full saved text |
| 1o6gmt9 | 1 | glu10-0274 | Full saved text |
| 1od7fuh | 1 | glu10-0275 | Full saved text |
| 1oe8k7f | 1 | glu10-0276 | Full saved text |
| 1p1f946 | 1 | glu10-0277 | Full saved text |
| 1p1jlh1 | 2 | glu10-0278, glu10-0279 | Full saved text |
| 1p94gc7 | 1 | glu10-0280 | Full saved text |
| 1p9vrf9 | 1 | glu10-0281 | Full saved text |
| 1pbo23r | 1 | glu10-0282 | Full saved text |
| 1pc3q6n | 2 | glu10-0283, glu10-0284 | Full saved text |
| 1pc9ysi | 2 | glu10-0285, glu10-0286 | Full saved text |
| 1pitfq0 | 2 | glu10-0287, glu10-0288 | Full saved text |
| 1po861r | 1 | glu10-0289 | Full saved text |
| 1ppt6vb | 1 | glu10-0290 | Full saved text |
| 1ps3mf8 | 1 | glu10-0291 | Full saved text |
| 1psq0ki | 1 | glu10-0292 | Full saved text |
| 1pszl7q | 1 | glu10-0293 | Full saved text |
| 1pv3i7w | 1 | glu10-0294 | Full saved text |
| 1pz1b8o | 1 | glu10-0295 | Full saved text |
| 1n4jaka | 2 | glu10-0296, glu10-0297 | Full saved text |
| 1nai6iv | 1 | glu10-0298 | Full saved text |
| 1nbiqsr | 1 | glu10-0299 | Full saved text |
| 1no5dqi | 1 | glu10-0300 | Full saved text |
| 1nuknvs | 1 | glu10-0301 | Full saved text |
| 1ptidiz | 1 | glu10-0302 | Full saved text |
| 1luj5pl | 1 | glu10-0303 | Full saved text |
| 1lp6c26 | 1 | glu10-0304 | Full saved text |
| 1lq1bpy | 1 | glu10-0305 | Full saved text |
| 1lqaxfh | 1 | glu10-0306 | Full saved text |
| 1lrin1l | 1 | glu10-0307 | Full saved text |
| 1lszz7i | 1 | glu10-0308 | Full saved text |
| 1m0lurr | 1 | glu10-0309 | Full saved text |
| 1m1j7gk | 1 | glu10-0310 | Full saved text |
| 1m3pqp6 | 1 | glu10-0311 | Full saved text |
| 1m4ms41 | 1 | glu10-0312 | Full saved post text; referenced chart/image not available; no visual interpretation |
| 1m4tpox | 2 | glu10-0313, glu10-0314 | Full saved text |
| 1m5yxr1 | 1 | glu10-0315 | Full saved text |
| 1m62wop | 1 | glu10-0316 | Full saved text |
| 1m82b30 | 1 | glu10-0317 | Full saved text |
| 1m9y1ag | 1 | glu10-0318 | Full saved text |
| 1md9ree | 2 | glu10-0319, glu10-0320 | Full saved text |
| 1mde74f | 1 | glu10-0321 | Full saved text |
| 1lx0wbs | 1 | glu10-0322 | Full saved text |
| 1lop8c1 | 1 | glu10-0323 | Full saved text |
| 1lp5o0h | 1 | glu10-0324 | Full saved text |
| 1lp7qv3 | 1 | glu10-0325 | Full saved text |
| 1lwolxg | 1 | glu10-0326 | Full saved text |
| 1lx9w13 | 1 | glu10-0327 | Full saved text |
| 1m1edrx | 1 | glu10-0328 | Full saved text |
| 1lplqvf | 1 | glu10-0329 | Full saved text |
| 1ltq48s | 1 | glu10-0330 | Full saved text |
| 1lwd5t9 | 2 | glu10-0331, glu10-0332 | Full saved text |
| 1lwft9t | 1 | glu10-0333 | Full saved text |
| 1lxe271 | 1 | glu10-0334 | Full saved text |
| 1m08boh | 1 | glu10-0335 | Full saved text |
| 1m0ihdy | 2 | glu10-0336, glu10-0337 | Full saved text |
| 1m4m15t | 2 | glu10-0338, glu10-0339 | Full saved text |
| 1m4xvhb | 2 | glu10-0340, glu10-0341 | Full saved text |
| 1m6k0fd | 1 | glu10-0342 | Full saved text |
| 1mdtaip | 1 | glu10-0343 | Full saved text; new passages only; existing rjnp01-0146 encouragement not repeated |
| 1ltzaas | 1 | glu10-0344 | Full saved text |
| 1m5cxrj | 1 | glu10-0345 | Full saved text |
| 1m65vxl | 1 | glu10-0346 | Full saved text |
| 1m66dlw | 1 | glu10-0347 | Full saved text |
| 1m903u3 | 1 | glu10-0348 | Full saved text |
| 1m9fdh1 | 2 | glu10-0349, glu10-0350 | Full saved text |
| 1m9nfjt | 2 | glu10-0351, glu10-0352 | Full saved text |
| 1mdgich | 1 | glu10-0353 | Full saved text |
| 1me4kof | 2 | glu10-0354, glu10-0355 | Full saved text |
| 1lwh6mj | 1 | glu10-0356 | Full saved text |
| 1m2r961 | 1 | glu10-0357 | Full saved text |
| 1mdnkl1 | 1 | glu10-0358 | Full saved text |
| 1lx2f5f | 1 | glu10-0359 | Full saved text |
| 1lxqkc4 | 1 | glu10-0360 | Full saved text |
| 1lz8tif | 1 | glu10-0361 | Full saved text |
| 1m57p22 | 1 | glu10-0362 | Full saved text |
| 1m7wqkm | 1 | glu10-0363 | Full saved text |
| 1mait20 | 1 | glu10-0364 | Full saved text |
| 1mb5xz8 | 1 | glu10-0365 | Full saved text |
| 1mc2q5k | 1 | glu10-0366 | Full saved text |
| 1mdubbg | 1 | glu10-0367 | Full saved text |
| 1lrdp03 | 1 | glu10-0368 | Full saved text |
| 1lxc7u6 | 1 | glu10-0369 | Full saved text |
| 1lyq9zv | 1 | glu10-0370 | Full saved text |
| 1m5sydy | 1 | glu10-0371 | Full saved text |
| 1m6hmxi | 1 | glu10-0372 | Full saved text |
| 1m8324p | 1 | glu10-0373 | Full saved text |
| 1py99pc | 2 | glu10-0374, glu10-0375 | Full saved text |
| 1n43zp5 | 2 | glu10-0376, glu10-0377 | Full saved text |
| 1lqbvnm | 1 | glu10-0378 | Exact ID located in gzip; full submission title/selftext; no comment-thread read claimed |
| 1lzvybf | 1 | glu10-0379 | Exact ID located in gzip; full submission title/selftext; no comment-thread read claimed |
| 1me47un | 1 | glu10-0380 | Exact ID located in gzip; full submission title/selftext; no comment-thread read claimed |
| 1mcqbjb | 1 | glu10-0381 | Full saved text |
| 1o22qg2 | 2 | glu10-0382, glu10-0383 | Full saved text |
| 1pthl6r | 2 | glu10-0384, glu10-0385 | Full saved text |

## What these units add

These are comparisons with `synthesis/findings.md` and `synthesis/niche-opportunities.md` as read on 2026-11-17. Those pages already acknowledge clinical context, failed plans, paper rejection and the limits of household coordination. The recovered material supplies missing mechanisms and contradictions; it does not turn this deliberately selected exclusion queue into a prevalence survey or justify a new niche ranking by quote count.

1. **A feeding or sleep “schedule” is often inseparable from symptoms, treatment, pain and the adult's capacity.** The current operational-job framing needs these details in the evidence itself. Allergy-related pumping and discarding milk competes with bottle washing and care; a previously sustainable consultant-assisted schedule becomes unworkable with mastitis and a toddler. An early-intervention program can teach isolated skills while leaving the family without comprehensive day-to-day scheduling help for a rare condition. Reported advice to remove night feeds can reduce intake without fixing morning refusal. These are specific failures of fit, not absence of a practical need. [glu10-0151] [glu10-0157] [glu10-0158] [glu10-0241] [glu10-0242] [glu10-0331] [glu10-0381]

2. **“Ask a clinician” leaves an information and access problem of its own.** A parent with a booked glucose test wants only an arrival-and-test walkthrough; another did not know what questions to ask. Repeated doctors require the same history and recommend something already tried, prompting interest in private continuity. Other accounts allege a faulty weighing scale or describe later diagnosis after reassurance. Keep these attributed accounts rather than treating either parental worry or clinician reassurance as a universal explanation. They do not verify malpractice or establish that self-diagnosis is correct. [glu10-0134] [glu10-0135] [glu10-0136] [glu10-0304] [glu10-0336] [glu10-0337]

3. **The missing mental-health material contains concrete requests, barriers and severe experiences.** Parents ask for medication experiences before consultation, help interpreting infant cues, words for an employer, anonymous understanding, and support that fits caring for an infant. One retrospective account describes hiding voices, insomnia and suicidality for fear of appearing unable to parent. Another cannot answer support callbacks while caring for a clingy baby. A parent already in therapy and reading extensively still describes suicidal beliefs that the baby would be better off without them. “More information” or generic encouragement is not an adequate description of these needs. [glu10-0098] [glu10-0099] [glu10-0200] [glu10-0206] [glu10-0207] [glu10-0278] [glu10-0279] [glu10-0287] [glu10-0288] [glu10-0351] [glu10-0352]

4. **Pumping decisions are also decisions about bodily autonomy, identity, grief and time with the baby.** Pain can make more sessions impossible, and unusable frozen milk can retain emotional value after feeding ends. Stopping is described as joyful and devastating; another parent wants body and time back, while another is glad to have continued during toddler illness. Formula initially restores time in one account, then guilt returns. The comparison must retain continuing, stopping and ambivalence together, rather than assuming the desired outcome is maximum production or adherence. [glu10-0158] [glu10-0173] [glu10-0174] [glu10-0181] [glu10-0184] [glu10-0196] [glu10-0212] [glu10-0213] [glu10-0220]

5. **The new spending evidence strengthens distinctions between equipment, live care, a quote for care and a report.** One author explicitly reports paying a feeding consultant who introduced a relief product; another explicitly paid a sleep consultant without success. A separate author reports $2000+ spent testing pump parts and pumps. The $400 pumping consultation is a proposed fee, with payment unestablished; the $750 colic course is explicitly rejected. A hired sleep consultant can produce partial initial improvement followed by prolonged unresolved sleep. None supplies a separately priced customized written deliverable. [glu10-0168] [glu10-0177] [glu10-0234] [glu10-0303] [glu10-0382] [glu10-0383] [glu10-0384]

6. **Childcare handoff can involve clinical capability, trust and safety rather than a missing checklist.** Reflux, torticollis and inability to use ordinary containers motivate one-to-one nanny care. Study-dependent immigration status and lack of local feeding support push another parent toward months of overseas separation. Reported child abuse creates a need to supervise the other parent and cut working hours; a grandfather's falls and refusal to follow a seated-holding agreement threaten planned care. A new document cannot by itself create a suitable, trusted caregiver. [glu10-0228] [glu10-0280] [glu10-0296] [glu10-0297] [glu10-0302]

7. **Birth preparation includes control, consent, uncertainty and fixed family constraints.** A prepared parent fears that birth will happen to them without meaningful choices; pain-free-birth advertising adds inadequacy. Another considers induction to fit paternity leave and international visitors. A parent with a heart condition distinguishes a survival concern from the clinician's apparent interpretation as ordinary birth anxiety. These accounts expand prenatal orientation beyond information acquisition or generic birth confidence. They are attributed experiences, not recommendations for a delivery method. [glu10-0087] [glu10-0088] [glu10-0095] [glu10-0105] [glu10-0305]

8. **Work can represent identity, competence and relief, alongside a source of overload.** Parents feel guilty for wanting a valued job, distressed when reduced shifts remove usefulness, or unable to take treatment leave without consuming time needed after birth. A willing remote-working partner enables a mother to pursue promotion despite commute costs. A blanket return-to-work “choreography” frame misses positive ambition, identity loss and the bargaining over finite leave. [glu10-0217] [glu10-0300] [glu10-0301] [glu10-0310] [glu10-0350] [glu10-0376] [glu10-0377]

9. **Physical help and emotional readiness do not always move together.** A respectful grandmother can still trigger jealousy and distress, while elsewhere a sole caregiver envies even imperfect family help. Hospital-recovery visitors, withheld personal space and dismissive advice can add strain. These are different household states; neither “bring in a village” nor “set better boundaries” captures all of them. [glu10-0132] [glu10-0149] [glu10-0218] [glu10-0285] [glu10-0286]

10. **Developmental guidance can be sought for reassurance after difficult care, not only better activity matching.** Anxiety treatment begins to help and then reveals guilt about tummy time during near-solo newborn care. Food-preparation instructions by age do not answer a premature baby's postural-readiness concern. The rare-condition parent explicitly lacks comparable examples. A capability-matched play hypothesis remains open, but these records cannot be represented as simple activity demand or used to infer developmental deficit or acceleration. [glu10-0144] [glu10-0331] [glu10-0332] [glu10-0343]

11. **Loss, trauma and bodily recovery shape later choices for months or years.** Trauma-related gaps in memories of a first baby drive journalling and photographing the next. Prior loss makes pregnancy announcement feel unsafe. Persistent birth-injury pain deters a wanted subsequent pregnancy. These are concrete needs for memory, reassurance and recovery information that the narrow contenders underdescribe; they are not evidence that a commercial format has been purchased. [glu10-0268] [glu10-0356] [glu10-0369] [glu10-0370]

12. **Financial and care-access shocks belong inside the practical picture.** Leaving an abusive relationship creates an immediate housing search with a $400 monthly ceiling. A school closure ends a family's insurance on one day's notice. Specialist-care waits, appointment timing and recovery needs coexist with consumer decisions. A lower-priced document does not establish affordability or solve lost coverage, housing or capacity. [glu10-0317] [glu10-0321] [glu10-0274] [glu10-0363]

13. **Relevant seller material was also lost by the old authenticity/commercial boundary.** The recovered set contains a free gentle postpartum PDF offer, baby-tracker and family-calendar creators, a parental-fitness guide seller, and an app founder claiming medical credentials who asks about premium recovery support. These supply proposed formats and positioning, not independent proof of demand, qualified care or willingness to pay. Questioning authenticity changes attribution; it does not justify discarding the wording. [glu10-0197] [glu10-0133] [glu10-0299] [glu10-0333] [glu10-0338] [glu10-0339]

The recovered material adds direct paid-service self-reports and substantial unmet needs. It does **not** validate a standalone-report price, establish clinical efficacy, authenticate authors, measure population frequency or determine a launch market. The current ranking should be read with this formerly missing evidence beside it.

## Added theme vocabulary

Seed themes retain the README meanings. These additional tags identify the subject of a quote, never a restriction on its use.

| Tag | Meaning |
|---|---|
| abuse_coercion | Reported abuse, coercion, intimidation or safeguarding discomfort; allegations are not verified facts. |
| birth_autonomy | Preferences, perceived control and decisions around pregnancy care, birth and related family events. |
| body_image | Appearance, weight, bodily change and pressure to return to a previous body. |
| caregiver_health | Physical health of a caregiver where a maternal role is not established, including fathers. |
| child_autonomy | Respecting a child's assent, refusal or bodily boundaries. |
| child_safety | Safety questions involving children beyond infancy. |
| family_separation | Separation of parents or prolonged parent-child separation and its care consequences. |
| family_travel | Journeys, outings, visits, travel cost and disruptions involving children or pregnancy. |
| feeding_pain | Physical pain, tissue injury, engorgement or breast inflammation in feeding/pumping accounts. |
| gear_and_registry | Equipment fit, component compatibility, acquisition and use. |
| infant_health | Attributed symptoms, illness, assessment or treatment concerning a baby or toddler. |
| infant_safety | Perceived hazards, monitoring and safety-related decisions concerning a baby. |
| maternal_health | Physical pregnancy/postpartum health described by the source, without assigning a new diagnosis. |
| maternal_mental_health | Emotional distress, psychiatric experiences, treatment and coping in the pregnancy/postpartum context; self-report or second-hand provenance remains explicit. |
| maternity_clothing | Clothing for pregnancy, nursing and related practical/appearance needs. |
| medical_access | Availability, timing, continuity, cost, insurance or geographic access to care. |
| paid_care | Paid or offered human care/help and associated service scope. |
| parental_autonomy | Parent's request to accept or refuse care or make a family decision. |
| pregnancy_loss | Pregnancy-loss experience, fear and effects on subsequent pregnancies or family life. |
| premature_birth | Premature birth, NICU care and the resulting practical context. |
| reproductive_decisions | Conception, contraception, fertility and decisions about additional children. |
| surrogacy | Intended-parent or surrogate experience and related commercial offers; provenance remains explicit. |

## Verification

Every excerpt was checked as an exact, case- and punctuation-sensitive substring of its **native content field/post body**, with JSON decoded and gzip decompressed. Bundle checks selected the named unit, not any matching text elsewhere in the bundle. No whitespace normalization was needed for the strict check. The allowed ` […] ` form is supported; these 385 quotes use contiguous text.

The existing `_tools/verify_quotes.py` was also executed for the UR10 file with its raw loader adapted **in memory only** to decode JSON and gzip; its unmodified reader otherwise opens compressed files as plain UTF-8. No script was edited. Native-body checks additionally prevent a quote from spanning capture metadata or two separately attributed posts.

```text
STRICT_NATIVE_BODY_VERIFICATION 385 / 385 errors []
reddit-ur10.jsonl: 385 quotes, 0 failed
TOTAL 385 quotes, 0 failed
assigned 293; read 293; unit IDs not found 0
complete captures 289; listing-only/full thread unavailable 4
quoted units 288; quotes written 385; quotes verified 385
```

All IDs are unique and run from `glu10-0001` through `glu10-0385`. Required fields, allowed speaker/stage/type vocabulary, context length (25 words maximum), attribution and overlap with existing excerpts were checked. Raw sources, synthesis, other readers' files and scripts were not modified.

