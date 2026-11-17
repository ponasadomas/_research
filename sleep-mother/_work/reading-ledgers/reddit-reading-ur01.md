# UR01 — unfilter reread ledger

Assignment: `scratchpad/unfilter-reread/assign-ur01.tsv`. Read on 2026-11-16.

| Check | Count |
|---|---:|
| Rows assigned | 230 |
| Rows read in full | 230 |
| Rows not found | 0 |
| Rows with new quotes | 210 |
| Rows without new quotes | 20 |
| Quotes written | 328 |
| Quotes verified against exact source text | 328 |
| Failed source matches | 0 |

The 230 rows comprise 228 Reddit posts/units and two assigned app reviews. I read the 88 available Reddit unit files in full, including all archived original-poster replies, and the other 140 posts from their subreddit's saved posts JSONL. Both assigned reviews were found in the saved app-review material. The voice file contains 327 Reddit quotes and one Slumber review quote, with unique ids `smu01-0001`–`smu01-0328`.

I compared assigned posts with the existing `voice/*.jsonl` records by post id and raw-file identity. The selections below add unquoted passages; two crossposts add nothing beyond this reader's earlier selections, and one trim candidate adds nothing beyond the older extraction. No raw file, synthesis file, other reader's file or shared tool was changed. No network or git was used.

Verification requires literal, contiguous text matches, without whitespace, spelling, punctuation or HTML-entity normalization. For JSONL sources, the check decodes JSON and looks only in the cited post's title/selftext, identified by `post_id`; it does not search unrelated posts or JSON serialization. Unit and review-corpus quotes match the exact file text. Comment dates, comment ids and comment permalinks come from the unit's matching comment header.

The stock `_tools/verify_quotes.py` reads JSONL as serialized text, so its direct run reported 111 serialization mismatches. Its unchanged verification logic was also run with a JSON-decoding source reader supplied in memory: `reddit-ur01.jsonl: 328 quotes, 0 failed`; `TOTAL 328 quotes, 0 failed`. The stricter independent check described above likewise verified all 328 against their exact source/post, checked schema and comment provenance, and found no duplicate of an existing quote. No shared tool was edited.

Reproduce the literal source check from the ads repo:

```sh
python3 -I - <<'PY'
import json
from pathlib import Path
b = Path('mamivio.com/research/sleep-mother')
qs = [json.loads(line) for line in (b/'voice/reddit-ur01.jsonl').open()]
needed, archives, texts = {}, {}, {}
for q in qs:
    if q['raw_file'].endswith('.jsonl'):
        needed.setdefault(q['raw_file'], set()).add(q['post_id'])
for rel, ids in needed.items():
    archives[rel] = {}
    for line in (b/rel).open():
        post = json.loads(line)
        if post.get('id') in ids:
            archives[rel][post['id']] = post
for q in qs:
    rel = q['raw_file']
    if rel.endswith('.jsonl'):
        post = archives[rel][q['post_id']]
        assert any(q['quote'] in post.get(k, '') for k in ('title', 'selftext')), q['id']
    else:
        if rel not in texts:
            texts[rel] = (b/rel).read_text()
        assert q['quote'] in texts[rel], q['id']
assert len({q['id'] for q in qs}) == len(qs)
print(f'{len(qs)} quotes verified; 0 failed; ids unique')
PY
```

## Assigned-row ledger

The row ids below reproduce the assignment exactly. Counts are new quotes in this reader's voice file. A zero records a relevance reason or nothing new beyond existing quotes.

| Assignment id | New quotes | Quote ids or reason |
|---|---:|---|
| BabyBumps-1sa7jan | 2 | smu01-0001, smu01-0002 |
| BabyBumps-1shnat6 | 1 | smu01-0003 |
| BabyBumps-1srlhdj | 3 | smu01-0004, smu01-0005, smu01-0006 |
| BabyBumps-1swh124 | 1 | smu01-0007 |
| BabyBumps-1t8h3ec | 2 | smu01-0008, smu01-0009 |
| BabyBumps-1to5jfc | 3 | smu01-0010, smu01-0011, smu01-0012 |
| BabyBumps-1tvay39 | 1 | smu01-0013 |
| BabyBumps-1ugw94y | 1 | smu01-0014 |
| BabyBumps-1uv6o3m | 1 | smu01-0015 |
| BabyBumps-1v5tnv3 | 2 | smu01-0016, smu01-0017 |
| BabyBumps-1vdph15 | 1 | smu01-0018 |
| BabyBumps-1vpv7vm | 2 | smu01-0019, smu01-0020 |
| BabyBumps-1wescw9 | 2 | smu01-0021, smu01-0022 |
| BabyBumps-1ws8yzt | 1 | smu01-0023 |
| BabyBumps-1xaf7qb | 3 | smu01-0024, smu01-0025, smu01-0026 |
| FirstTimeMom-1sncmu4 | 1 | smu01-0027 |
| FirstTimeMom-1v85677 | 2 | smu01-0028, smu01-0029 |
| Mommit-1s9p1cb | 2 | smu01-0030, smu01-0031 |
| Mommit-1sh17j3 | 1 | smu01-0032 |
| Mommit-1sq2bic | 1 | smu01-0033 |
| Mommit-1t0coxo | 1 | smu01-0034 |
| Mommit-1ta0e68 | 1 | smu01-0035 |
| Mommit-1tjqczq | 0 | Off-niche: infant illness and the child's inability to sleep; no account of the parent's own sleep. |
| Mommit-1ty7k1o | 1 | smu01-0036 |
| Mommit-1u42ymk | 2 | smu01-0037, smu01-0038 |
| Mommit-1ucn5pm | 1 | smu01-0039 |
| Mommit-1uh12n9 | 1 | smu01-0040 |
| Mommit-1urd8dg | 1 | smu01-0041 |
| Mommit-1uz39ji | 0 | Off-niche: child's sleepover and boundaries with neighbours; no maternal sleep account. |
| Mommit-1v2lsze | 0 | Off-niche: parenting and relationship strain; night-shift work is named, but no own-sleep problem is described. |
| Mommit-1vhn43g | 1 | smu01-0042 |
| Mommit-1vko4ne | 1 | smu01-0043 |
| Mommit-1vwonnr | 2 | smu01-0044, smu01-0045 |
| Mommit-1w008e7 | 2 | smu01-0046, smu01-0047 |
| Mommit-1w3mhdm | 2 | smu01-0048, smu01-0049 |
| Mommit-1wa5i5d | 2 | smu01-0050, smu01-0051 |
| Mommit-1wgnryp | 2 | smu01-0062, smu01-0063 |
| Mommit-1wqghv9 | 2 | smu01-0064, smu01-0065 |
| Mommit-1x0patj | 1 | smu01-0066 |
| Mommit-1x8xc78 | 1 | smu01-0328 |
| NewParents-1s961qo | 2 | smu01-0052, smu01-0053 |
| NewParents-1sf4ldf | 1 | smu01-0054 |
| NewParents-1sld7p7 | 2 | smu01-0055, smu01-0056 |
| NewParents-1sph7zb | 3 | smu01-0057, smu01-0058, smu01-0059 |
| NewParents-1stbhdl | 2 | smu01-0060, smu01-0061 |
| NewParents-1syn53l | 2 | smu01-0067, smu01-0068 |
| NewParents-1t2bdvu | 2 | smu01-0069, smu01-0070 |
| NewParents-1t4lpoc | 2 | smu01-0071, smu01-0072 |
| NewParents-1t7i7ur | 2 | smu01-0073, smu01-0074 |
| NewParents-1tbr0rb | 2 | smu01-0075, smu01-0076 |
| NewParents-1tjq828 | 2 | smu01-0077, smu01-0078 |
| NewParents-1tqhs83 | 2 | smu01-0079, smu01-0080 |
| NewParents-1u00hb3 | 1 | smu01-0081 |
| NewParents-1u43x4u | 2 | smu01-0082, smu01-0083 |
| NewParents-1u7wznv | 3 | smu01-0084, smu01-0085, smu01-0086 |
| NewParents-1ue7uc2 | 2 | smu01-0087, smu01-0088 |
| NewParents-1uh2o23 | 1 | smu01-0089 |
| NewParents-1upygy5 | 1 | smu01-0090 |
| NewParents-1v1sn4a | 2 | smu01-0091, smu01-0092 |
| NewParents-1vbugbf | 4 | smu01-0093, smu01-0094, smu01-0095, smu01-0096 |
| NewParents-1vp04qs | 3 | smu01-0097, smu01-0098, smu01-0099 |
| NewParents-1vuya0s | 3 | smu01-0100, smu01-0101, smu01-0102 |
| NewParents-1vzasdc | 2 | smu01-0103, smu01-0104 |
| NewParents-1w2hzuc | 1 | smu01-0105 |
| NewParents-1w4bjur | 1 | smu01-0106 |
| NewParents-1w7un5x | 1 | smu01-0107 |
| NewParents-1wbqpl1 | 1 | smu01-0108 |
| NewParents-1weebyn | 2 | smu01-0109, smu01-0110 |
| NewParents-1wgf7qw | 1 | smu01-0111 |
| NewParents-1wn2qhk | 2 | smu01-0112, smu01-0113 |
| NewParents-1wvdtw5 | 1 | smu01-0114 |
| NewParents-1x093xe | 1 | smu01-0115 |
| NewParents-1x8lh9u | 1 | smu01-0116 |
| Parenting-1sipz7j | 0 | Off-niche: asks how to preserve infant sleep after standing; no parent's sleep difficulty or deprivation stated. |
| Parenting-1tgm2d4 | 2 | smu01-0117, smu01-0118 |
| Parenting-1vezk59 | 0 | Off-niche: toddler bedtime and sibling logistics; no mother's own sleep difficulty stated. |
| Parenting-1werbre | 1 | smu01-0119 |
| Postpartum_Depression-1sk1q0s | 4 | smu01-0120, smu01-0121, smu01-0122, smu01-0123 |
| Postpartum_Depression-1t3k3rp | 3 | smu01-0124, smu01-0125, smu01-0126 |
| Postpartum_Depression-1tlugyq | 1 | smu01-0127 |
| Postpartum_Depression-1tzzzz3 | 2 | smu01-0128, smu01-0129 |
| Postpartum_Depression-1u736h6 | 2 | smu01-0130, smu01-0131 |
| Postpartum_Depression-1ur9dhf | 1 | smu01-0132 |
| Postpartum_Depression-1uyrc57 | 1 | smu01-0133 |
| Postpartum_Depression-1vcc8oz | 3 | smu01-0146, smu01-0147, smu01-0148 |
| Postpartum_Depression-1vjjjsx | 3 | smu01-0134, smu01-0135, smu01-0136 |
| Postpartum_Depression-1vtu8bp | 1 | smu01-0137 |
| Postpartum_Depression-1w3w0k5 | 1 | smu01-0138 |
| Postpartum_Depression-1w6zz8b | 1 | smu01-0139 |
| Postpartum_Depression-1wgtrc9 | 3 | smu01-0140, smu01-0141, smu01-0142 |
| Postpartum_Depression-1wojqka | 3 | smu01-0143, smu01-0144, smu01-0145 |
| Postpartum_Depression-1wvfb60 | 2 | smu01-0149, smu01-0150 |
| Postpartum_Depression-1wy82ez | 1 | smu01-0151 |
| Postpartum_Depression-1x9ir1i | 2 | smu01-0152, smu01-0153 |
| PregnancyUK-1soxlxz | 2 | smu01-0154, smu01-0155 |
| PregnancyUK-1tvmeoc | 3 | smu01-0156, smu01-0157, smu01-0158 |
| PregnancyUK-1umoztq | 0 | Off-niche: constipation, contractions and a triage scare before a night shift; no own-sleep problem stated. |
| PregnancyUK-1vfzljj | 1 | smu01-0159 |
| PregnancyUK-1w21hd0 | 2 | smu01-0160, smu01-0161 |
| PregnancyUK-1wqvqoj | 1 | smu01-0162 |
| beyondthebump-1sa80k5 | 2 | smu01-0163, smu01-0164 |
| beyondthebump-1sflo8z | 2 | smu01-0165, smu01-0166 |
| beyondthebump-1sjiq9w | 2 | smu01-0167, smu01-0168 |
| beyondthebump-1so1tbv | 1 | smu01-0169 |
| beyondthebump-1ss5m7b | 1 | smu01-0170 |
| beyondthebump-1syjct2 | 1 | smu01-0171 |
| beyondthebump-1t14mp2 | 2 | smu01-0172, smu01-0173 |
| beyondthebump-1ta6ji7 | 1 | smu01-0174 |
| beyondthebump-1tep0ja | 5 | smu01-0175, smu01-0176, smu01-0177, smu01-0178, smu01-0179 |
| beyondthebump-1tjcg2y | 2 | smu01-0180, smu01-0181 |
| beyondthebump-1tr68qv | 1 | smu01-0182 |
| beyondthebump-1tzjrff | 1 | smu01-0183 |
| beyondthebump-1u5hu4f | 2 | smu01-0184, smu01-0185 |
| beyondthebump-1ue1nhs | 3 | smu01-0186, smu01-0187, smu01-0188 |
| beyondthebump-1urvaq8 | 2 | smu01-0189, smu01-0190 |
| beyondthebump-1uzdca4 | 3 | smu01-0191, smu01-0192, smu01-0193 |
| beyondthebump-1v3sjt1 | 2 | smu01-0194, smu01-0195 |
| beyondthebump-1vbm2mo | 2 | smu01-0196, smu01-0197 |
| beyondthebump-1vgx8vn | 1 | smu01-0198 |
| beyondthebump-1vkxkvs | 2 | smu01-0199, smu01-0200 |
| beyondthebump-1vp9qth | 1 | smu01-0201 |
| beyondthebump-1vtax9s | 1 | smu01-0202 |
| beyondthebump-1w0rqia | 1 | smu01-0203 |
| beyondthebump-1w70kt8 | 2 | smu01-0204, smu01-0205 |
| beyondthebump-1war0q6 | 1 | smu01-0206 |
| beyondthebump-1wfakdw | 1 | smu01-0207 |
| beyondthebump-1wt1w4l | 1 | smu01-0208 |
| beyondthebump-1wy5itf | 2 | smu01-0209, smu01-0210 |
| beyondthebump-1xd1vte | 1 | smu01-0211 |
| beyondthebumpUK-1svr1mf | 0 | Off-niche: hospital pumping/sterilisation dispute without an account of the mother's sleep. |
| beyondthebumpUK-1tbt9yh | 1 | smu01-0212 |
| beyondthebumpUK-1us21ai | 2 | smu01-0213, smu01-0214 |
| beyondthebumpUK-1vqq0gw | 1 | smu01-0215 |
| beyondthebumpUK-1vu0n2f | 1 | smu01-0216 |
| beyondthebumpUK-1wbfv5a | 1 | smu01-0217 |
| beyondthebumpUK-1wia1z0 | 2 | smu01-0218, smu01-0219 |
| beyondthebumpUK-1ws1t19 | 1 | smu01-0220 |
| calm-au-10472913125 | 0 | Off-niche: child's own sleep/app-use review; no pregnancy, maternal or caregiver-sleep experience. The reason is relevance, not the reviewer's age. |
| daddit-1t0g4qd | 1 | smu01-0221 |
| daddit-1ubq1dq | 2 | smu01-0222, smu01-0223 |
| daddit-1v0mp4o | 1 | smu01-0224 |
| daddit-1vcy6g3 | 2 | smu01-0225, smu01-0226 |
| daddit-1vzv2hz | 0 | Off-niche: terminal-illness and future single-parenting account; night-shift work is background and no parent's sleep problem is stated. |
| daddit-1wk38pn | 1 | smu01-0227 |
| daddit-1wy2vmu | 3 | smu01-0228, smu01-0229, smu01-0230 |
| postpartumprogress-1twsthz | 1 | smu01-0231 |
| pregnant-1saa9bk | 1 | smu01-0232 |
| pregnant-1sj00me | 1 | smu01-0233 |
| pregnant-1sjzs7m | 1 | smu01-0234 |
| pregnant-1sqh7yu | 1 | smu01-0235 |
| pregnant-1sr81qx | 2 | smu01-0236, smu01-0237 |
| pregnant-1sv6si8 | 1 | smu01-0238 |
| pregnant-1t0o5hm | 1 | smu01-0239 |
| pregnant-1t2gzbp | 2 | smu01-0240, smu01-0241 |
| pregnant-1t5aibh | 1 | smu01-0242 |
| pregnant-1t98tjb | 1 | smu01-0243 |
| pregnant-1tave9l | 1 | smu01-0244 |
| pregnant-1tdkyuc | 1 | smu01-0245 |
| pregnant-1tiik9n | 1 | smu01-0246 |
| pregnant-1tmwfzn | 1 | smu01-0247 |
| pregnant-1tsda6q | 1 | smu01-0248 |
| pregnant-1tstj1o | 3 | smu01-0249, smu01-0250, smu01-0251 |
| pregnant-1tvaw84 | 0 | Nothing new beyond existing quotes: crosspost of BabyBumps-1tvay39, whose insomnia/symptom passage is already captured as smu01-0013. |
| pregnant-1tx4202 | 1 | smu01-0252 |
| pregnant-1u3drl9 | 1 | smu01-0260 |
| pregnant-1u897qr | 1 | smu01-0253 |
| pregnant-1ucm1py | 1 | smu01-0254 |
| pregnant-1ujlzik | 1 | smu01-0255 |
| pregnant-1umivw5 | 4 | smu01-0256, smu01-0257, smu01-0258, smu01-0259 |
| pregnant-1ut0uu0 | 2 | smu01-0261, smu01-0262 |
| pregnant-1uw2o98 | 1 | smu01-0263 |
| pregnant-1uy4ucv | 2 | smu01-0264, smu01-0265 |
| pregnant-1v6oqkv | 1 | smu01-0266 |
| pregnant-1v8r8on | 1 | smu01-0267 |
| pregnant-1vc0n3j | 1 | smu01-0268 |
| pregnant-1vdop2p | 1 | smu01-0269 |
| pregnant-1vfncoq | 1 | smu01-0270 |
| pregnant-1vjwh48 | 1 | smu01-0271 |
| pregnant-1vo9teo | 1 | smu01-0272 |
| pregnant-1vsrb83 | 1 | smu01-0273 |
| pregnant-1vva033 | 1 | smu01-0274 |
| pregnant-1w2b7pj | 1 | smu01-0275 |
| pregnant-1w3qxtu | 2 | smu01-0276, smu01-0277 |
| pregnant-1w6qzqv | 1 | smu01-0278 |
| pregnant-1wb8y9x | 3 | smu01-0279, smu01-0280, smu01-0281 |
| pregnant-1wes7w6 | 0 | Nothing new beyond existing quotes: exact post-text crosspost of BabyBumps-1wescw9, captured as smu01-0021; no additional replies. |
| pregnant-1wh172o | 1 | smu01-0282 |
| pregnant-1wjk7i3 | 2 | smu01-0283, smu01-0284 |
| pregnant-1wlarsi | 2 | smu01-0285, smu01-0286 |
| pregnant-1wnwmfz | 1 | smu01-0287 |
| pregnant-1wpny5l | 1 | smu01-0288 |
| pregnant-1wrvn01 | 1 | smu01-0289 |
| pregnant-1wz8c38 | 1 | smu01-0290 |
| pregnant-1x4xgpx | 1 | smu01-0291 |
| pregnant-1x7umic | 1 | smu01-0292 |
| pregnant-1x9yend | 1 | smu01-0293 |
| pregnant-1xd36w7 | 1 | smu01-0294 |
| sahm-1tep837 | 1 | smu01-0295 |
| sahm-1vj4hir | 1 | smu01-0296 |
| sahm-1w8dhg7 | 0 | Off-niche: childcare, income and prospective job-schedule choice; no account or question about the mother's own sleep. |
| sleeptrain-1sesycm | 0 | Off-niche: infant crib refusal and later retraining outcome; no parent's sleep difficulty or deprivation stated. |
| sleeptrain-1sipvdh | 0 | Off-niche: infant standing and preserving sleep training, near-crosspost of Parenting-1sipz7j; no own-sleep difficulty stated. |
| sleeptrain-1sn7svy | 2 | smu01-0297, smu01-0298 |
| sleeptrain-1svaxs2 | 2 | smu01-0299, smu01-0300 |
| sleeptrain-1t78cy6 | 1 | smu01-0301 |
| sleeptrain-1tbbpl2 | 0 | Off-niche: toddler's split nights and nap scheduling; no parent's own sleep difficulty or deprivation stated. |
| sleeptrain-1tevhdr | 1 | smu01-0302 |
| sleeptrain-1tmw7ga | 1 | smu01-0303 |
| sleeptrain-1tzc1o5 | 1 | smu01-0304 |
| sleeptrain-1u79dnk | 2 | smu01-0305, smu01-0306 |
| sleeptrain-1uk7vtn | 3 | smu01-0307, smu01-0308, smu01-0309 |
| sleeptrain-1uql4iy | 2 | smu01-0310, smu01-0311 |
| sleeptrain-1uw1mwt | 1 | smu01-0312 |
| sleeptrain-1v0swr2 | 1 | smu01-0313 |
| sleeptrain-1v938pf | 0 | Off-niche: toddler nap transition only; no parent's own sleep problem. |
| sleeptrain-1ve56ra | 1 | smu01-0314 |
| sleeptrain-1vg9qix | 0 | Off-niche: infant settling and crib association; says mother's caregiving is harder but gives no own-sleep account. |
| sleeptrain-1vk6va6 | 0 | Off-niche: infant nap-transition planning only; no parent's own sleep problem. |
| sleeptrain-1vs5cvz | 0 | Off-niche: toddler waking and quick resettling; no parent's own sleep difficulty or deprivation stated. |
| sleeptrain-1vws7g5 | 1 | smu01-0315 |
| sleeptrain-1w3vvre | 1 | smu01-0316 |
| sleeptrain-1wel231 | 1 | smu01-0317 |
| sleeptrain-1wj5yqw | 2 | smu01-0318, smu01-0319 |
| sleeptrain-1wn6ove | 1 | smu01-0320 |
| sleeptrain-1wwxnq7 | 2 | smu01-0321, smu01-0322 |
| sleeptrain-1x5y7ew | 2 | smu01-0323, smu01-0324 |
| slumber-au-10725315963 | 1 | smu01-0327 |
| workingmoms-1ss1yof | 1 | smu01-0325 |
| workingmoms-1vrnwqm | 0 | Nothing new beyond existing quotes: sm06-0039 retains the night-shift exhaustion and pregnancy-management question; omitted childcare detail adds no new sleep evidence. |
| workingmoms-1wig5vv | 1 | smu01-0326 |

## What these posts add

Most of this assignment was relevant to the mother's own sleep. **17 of 230 rows were off-niche**, and three had nothing new beyond existing quotes. A previous triage description such as “sleep absent,” “only mood,” or “medical question” often did not describe the full text. The extracted evidence includes brief sleep mentions as well as sustained sleep accounts. Older-child maternal insomnia, a grandparent report, prospective parents and the adult-app comparator are identified in context; they should not silently become evidence about mothers of newborns.

The 2026-11-16 findings already restore fear, hallucinations, medication, bedsharing, treatment attempts and unequal nights. Those broad topics are not discoveries of this reread. What was still missing was the following detail and contrary evidence. These are patterns in assigned accounts, not prevalence estimates or demonstrated effects of a product.

- **A plan is explicitly requested in a post dropped by an age match.** A parent at 15 gestational weeks asks for low-effort routines and says “I want a simple plan I can stick to without spiraling.” Her earlier dinner, cooler room, reduced fluids, audiobook and magnesium have inconsistent results. This adds a direct request for manageable instructions to sections 10.4 and 11; it is not a purchase or evidence that she wants a subscription. The intake match “I'm 15” referred to pregnancy weeks. Other numerical matches likewise referred to gestational weeks or children's ages, not automatically to a young poster. [smu01-0010] [smu01-0011] [smu01-0012] [smu01-0253] [smu01-0275] [smu01-0320]

- **Institutional care can supply the rest that household arrangements did not.** One eight-month postpartum parent reports her first five-hour stretch since birth in a mothers-and-babies unit, with nurses and an overnight plan that did not feel like abandonment. Another describes fighting for admission, sleeping after zopiclone, then later starting sertraline and CBT together. These supply concrete recovery pathways absent from the findings' mainly household account of help. The latter reports general CBT, not CBT-I, and several interventions occurred together. [smu01-0079] [smu01-0080] [smu01-0143] [smu01-0144] [smu01-0145]

- **There is more mother-directed spending, with treatment-specific reasons to stop.** One parent reports next-day psychiatric care costing “almost 200 bucks each visit.” Another reports improved sleep during ketamine infusions, then stopping because they were extremely expensive and, in her account, incompatible with planning another pregnancy. A father reports ongoing expensive therapy and starting medication. Sections 8 and 10 should include these alongside the earlier private-therapy and prescription examples. They remain spending on care, not purchases of a mother-specific quiz or plan; no currency or unreported treatment price is inferred. [smu01-0131] [smu01-0124] [smu01-0227]

- **Medication is entangled with withdrawal, recovery history, responsiveness and disagreement between providers.** A first-trimester teacher describes withdrawing from long-term clonazepam, fear of her doctor's response, and vivid dreams while using magnesium. Another pregnant parent says repeated prescriptions trigger memories of addiction recovery and fears being seen as drug-seeking; a later reply reports some unmedicated improvement. A mother says a higher Seroquel dose makes her sleep through everything. These add mechanisms behind sections 4.11 and 10.2 beyond a list of attempted products or next-day grogginess. These are the speakers' accounts, not verified prescribing conclusions. [smu01-0004] [smu01-0005] [smu01-0006] [smu01-0168] [smu01-0279] [smu01-0280] [smu01-0281]

- **Protected sleep can be an explicit accommodation planned before conception.** A prospective parent says eight hours is “not a luxury, it's an accommodation,” describes prior mania after short sleep, and considers a grandmother-and-partner rota before deciding how to have children. A pregnant parent with severe restless legs reports losing the ability to drive or care for her children, improved functioning on prescribed medication, and then guilt about possible neonatal withdrawal. The findings discuss conditions and medication, but these accounts make the required continuity and competing fears much more specific. [smu01-0115] [smu01-0261] [smu01-0262]

- **Some “hypervigilance” follows a concrete event or prior loss.** A partner reorganizes work around being awake at night after seeing his newborn choke; the baby later sleeps well while he still jumps at noises. Another parent refuses bedsharing after losing a previous infant. A pregnant survivor describes vivid recurring nightmares and having previously refused sleep subconsciously. A parent with a new baby cannot sleep after a toddler's near miss at an upstairs window. This adds origins for the fear to sections 6 and 10.2, rather than treating all listening and checking as interchangeable. [smu01-0087] [smu01-0088] [smu01-0068] [smu01-0008] [smu01-0009] [smu01-0119]

- **The mother describes a mismatch between her waking intentions and decisions made half asleep.** One parent starts with a bassinet, prepares a floor mattress, becomes cold, then pulls the blanket up and covers the baby while half asleep. She asks how to arrange the environment for when she is no longer thinking clearly. Another forgot to restore monitor volume and slept deeply, then felt she had failed her baby; her later reply says separate rooms had improved both their sleep. These add specific decision sequences to the findings' already mixed bedsharing/monitor accounts. They also contradict any assumption that every exhausted parent remains a light sleeper. [smu01-0097] [smu01-0098] [smu01-0099] [smu01-0184] [smu01-0185]

- **Night care can include coercion and physical violence; the obstacle is more than agreement on hours.** A retrospective account says a husband refused a night nurse for her but intended to hire one for his own leave; it includes the later suicide attempt and admission. Another mother describes a night-feeding/support argument becoming physical. In a previously quoted unit, the missing replies describe her partner opposing medication and escalating when she tries to leave an argument. These sharpen section 10's statement that a plan does not bind the partner: rest, treatment and de-escalation themselves can be contested. [smu01-0134] [smu01-0135] [smu01-0136] [smu01-0128] [smu01-0129] [smu01-0177] [smu01-0178] [smu01-0179]

- **Available help can become unusable for concrete reasons.** Childcare specifically arranged to permit sleep after night shifts ends when a babysitter transports the baby without a car seat and asks the partner to keep it secret. Weekly therapy that required a child-free hour ended because coordinating it with the partner's lunch was impractical. A parent with severe insomnia says fear of separation and an unanswered insurance-covered therapist prevented disclosure and care. These add actual failed access pathways to the findings' affordability and no-village accounts. [smu01-0191] [smu01-0192] [smu01-0193] [smu01-0218] [smu01-0142]

- **Recovery stories need both improvement and continuing cost.** The omitted end of an existing sleep-training success quote says sleep paralysis, auditory hallucinations and insomnia stopped when the author began getting six to seven hours. Another parent reports recovery through medication, therapy, husband and village after hallucinations despite his attempts to take entire nights. Another is mostly recovered after admission and sleeping pills but remains afraid of recurrence months later. These broaden the outcome evidence in sections 4.9, 10 and 17.4; none isolates one intervention. [smu01-0105] [smu01-0100] [smu01-0101] [smu01-0102] [smu01-0199] [smu01-0200]

- **The time horizon extends beyond a baby under one, including into another pregnancy.** A mother pregnant again describes needing relief from a 19-month-old's early wakes while experiencing HG. A recovered parent describes improvement only after years and says the turning point for her was shifting attention from solving infant sleep to getting through her own day; she reports buying programmes that did not last. A father describes memory gaps during his commute and painful bedsharing with a 2.5-year-old. This extends the introduction's “under about a year” frame while reinforcing the findings' existing toddler and cumulative-deprivation material. [smu01-0305] [smu01-0306] [smu01-0307] [smu01-0308] [smu01-0309] [smu01-0225] [smu01-0226]

- **Birth settings and physical impairment constrain the sleep arrangement itself.** A mental-health birth plan includes a private room and partner presence but does not prevent over 30 hours awake during induction: ward noise, heat, unpredictable routines and contractions remain. Another account explains why injury, anaemia and medication made both bedsharing and lifting to a conventional crib impractical, and how a bedside crib and a patchwork of helpers were used instead. These add implementation limits to sections 4.1, 4.2 and 10.2. [smu01-0156] [smu01-0157] [smu01-0158] [smu01-0256] [smu01-0257]

- **The adult-app evidence includes a grandparent's completed purchase and personal sleep benefit.** The Slumber review explicitly says the reviewer bought it and reports improved personal sleep; the granddaughter mention is not the only relevant content. This adds a buyer example to section 15's adult-sleep comparison. It does not identify the reviewer as a postpartum mother, give a price, or establish demand for Mamivio. The Calm review instead describes a child's own sleep and app habits without a maternal/caregiver outcome, which is why that row produced no quote. [smu01-0327]

The other-side evidence also includes a parent reporting a grandparent who says worry about a four-year-old prevents sleep. This is another caregiver voice, not proof about newborn mothers; the report also shows the belief that worry is an inherited trait. [smu01-0328]

### Vocabulary, products and interpretation limits

No new theme tags were introduced; all tags use README seeds. “CBT” was retained as the speaker's term and not recoded as CBT-I. Some short fatigue/night-symptom accounts are peripheral to insomnia and are identified as such in context, including possible-pregnancy posts with no confirmed pregnancy. Their inclusion does not establish a diagnosis or sleep cause.

Useful additional language includes “a simple plan I can stick to without spiraling” [smu01-0012], “not a luxury, it's an accommodation” [smu01-0115], “permalatcher” and the “Nerds Gummy Cluster” description of nipple damage [smu01-0297], and a “patchwork of people” [smu01-0257]. The blood/vomiting/ER details of the permalatching account are preserved with the practical sleep failure, rather than reducing it to discomfort.

Named attempts include prescriptions and supplements, ketamine infusions, CBT, Slumber, Huckleberry, a Snoo, pregnancy pillows, blackout curtains, bedside/floor beds, doulas and psychiatric/therapy care. Paid baby programmes/apps remain distinct from the mother's own treatment or an adult-sleep app; use of an app, a prescription, or a service is not automatically a purchase. Only stated purchases/ongoing paid care are typed as purchases.

The conservative trim candidates do not all prove prior censorship: the omitted span in `PregnancyUK-1vfzljj` contains shopping URLs, and the omitted span in `sleeptrain-1v0swr2` contains infant waking/mood detail. I added other genuinely unquoted relevant content without labelling those trims medical exclusions. `workingmoms-1vrnwqm` had no new sleep evidence.

No synthesis claim or corpus-wide count was rewritten here. These findings are a reader's additions for reconciliation, with all original raw text and historical records left intact.
