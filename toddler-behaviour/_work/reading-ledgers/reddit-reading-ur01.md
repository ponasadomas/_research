# UR01 — unfilter reread, 2026-11-16

Assignment: `scratchpad/unfilter-reread/assign-ur01.tsv`. Full source text read locally; no network or git. Only these two UR01 outputs written. Counts describe selected evidence, not people or prevalence. Existing quotes checked across `voice/*.jsonl`.

## Coverage and verification

- Rows assigned: **295** (138 post rows, 157 unit rows).
- Rows read in full: **295**; not found: **0**.
- Exact sources read: **158** frozen Reddit units with all archived original-poster replies, **131** posts decoded from the named subreddit JSONL archives, **6** individual review blocks from the corpora identified in the assignment. The six review rows were found; they are not missing Reddit posts.
- Rows quoted: **256**. Rows without new quotes: **39** — **35 off-niche**, **4 nothing new beyond existing quotes**.
- Quotes written: **401** (`tbu01-0001`–`tbu01-0401`): **395 Reddit**, **5 App Store**, **1 book review**.
- Quotes verified literally in their cited source: **401/401**, **0 failed**. JSONL checks decode the correct post by `post_id` and search its title or body, not the encoded line. Unit reply URLs, dates and comment ids were also checked against the preceding source header.
- The supplied `_tools/verify_quotes.py` also reports `401 quotes, 0 failed`, run in memory with a JSONL-decoding source loader because its default loader treats JSONL as plain text. No shared checker was edited.
- IDs are sequential and unique; **0** collisions with other voice files. All schema vocabulary and context lengths checked. Comparison against other `voice/*.jsonl` records found **0** duplicate quotes or substantial shared passages, including whitespace/entity-normalized comparisons.
- Quotes are contiguous literal excerpts; no paraphrases or ellipsis joins. Reply dates are the reply's own date. The Spanish reply remains Spanish. Diagnosis, causation and treatment claims remain attributed reports.
- Mother labels require self-identification; otherwise `parent_unspecified` is used, including for fathers. Reviews use `reviewer` and their original review identifiers and source classes. No new theme tags were added.
- Most of the assignment was on-niche. **35/295 rows** were off-niche, chiefly general relationship/custody accounts, infant-only concerns, or acute symptoms without a behaviour or potty issue. Subject matter was never an exclusion reason.

## Row ledger

| Assignment id | Quotes | Result / reason if none |
|---|---:|---|
| AttachmentParenting-1sbhkq9 | 0 | Off-niche: asks about acute symptoms after swimming, without a behaviour or potty-training issue. |
| AttachmentParenting-1syn7c9 | 3 | Read in full; new evidence. |
| AttachmentParenting-1u3sw1o | 2 | Read in full; new evidence. |
| AttachmentParenting-1vrayrx | 2 | Read in full; new evidence. |
| AttachmentParenting-1wyzv28 | 2 | Read in full; new evidence. |
| GentleParenting-1tdhseo | 2 | Read in full; new evidence. |
| GentleParenting-1vhqg0w | 3 | Read in full; new evidence. |
| GentleParenting-1x7mh2p | 2 | Read in full; new evidence. |
| Mommit-1sb308s | 2 | Read in full; new evidence. |
| Mommit-1shbxqa | 2 | Read in full; new evidence. |
| Mommit-1smsv0o | 0 | Off-niche: newborn preparation for a pregnant relative; no toddler behaviour or potty training. |
| Mommit-1sr5s4v | 0 | Off-niche: emergency allergy response disagreement, without a behaviour, feeding refusal or potty issue. |
| Mommit-1sydh1l | 0 | Off-niche: general historical argument about childcare and grandmothers; no specific toddler behaviour or potty experience. |
| Mommit-1t4mw40 | 1 | Read in full; new evidence. |
| Mommit-1t9dq2x | 0 | Off-niche: parent recounts a nightmare, explicitly not an actual child-behaviour or potty event. |
| Mommit-1te2mue | 0 | Off-niche: developmental milestones and diagnostic uncertainty; no behaviour-management, feeding refusal or potty issue. |
| Mommit-1thny03 | 0 | Off-niche: current concerns concern a six-year-old; historical age-four caregiving context adds no 1–4 behaviour or potty account. |
| Mommit-1tn57ky | 0 | Off-niche: family illness and household care workload without a behaviour or potty issue. |
| Mommit-1tqoj57 | 1 | Read in full; new evidence. |
| Mommit-1txu747 | 1 | Read in full; new evidence. |
| Mommit-1u1s3oe | 1 | Read in full; new evidence. |
| Mommit-1u7n3j8 | 0 | Off-niche: partner abuse and barriers to leaving; no toddler behaviour, potty training or sibling adjustment described. |
| Mommit-1ucqbvf | 0 | Off-niche: anxiety about croup treatment and imaging, without a behaviour or potty issue. |
| Mommit-1ues171 | 0 | Off-niche: postpartum body image and partner comment; no toddler behaviour or potty content. |
| Mommit-1ukelks | 1 | Read in full; new evidence. |
| Mommit-1uwkm0i | 3 | Read in full; new evidence. |
| Mommit-1v17fnq | 0 | Off-niche: divorce decision and finances; toddler age alone does not establish niche relevance. |
| Mommit-1v8z7p6 | 1 | Read in full; new evidence. |
| Mommit-1vdyvgu | 0 | Off-niche: parent’s diagnostic fears and regret, without a toddler behaviour or potty issue. |
| Mommit-1vlamqp | 3 | Read in full; new evidence. |
| Mommit-1vooiny | 2 | Read in full; new evidence. |
| Mommit-1vt4z2i | 2 | Read in full; new evidence. |
| Mommit-1vxj1mw | 2 | Read in full; new evidence. |
| Mommit-1w3c620 | 0 | Off-niche: grief about ending childbearing and children growing up; no behaviour or potty issue. |
| Mommit-1wdht1q | 2 | Read in full; new evidence. |
| Mommit-1wi54ny | 2 | Read in full; new evidence. |
| Mommit-1wsjftp | 3 | Read in full; new evidence. |
| Mommit-1wwcpyz | 2 | Read in full; new evidence. |
| Mommit-1x1yvrz | 2 | Read in full; new evidence. |
| Mommit-1x8igot | 2 | Read in full; new evidence. |
| NewParents-1saaya1 | 1 | Read in full; new evidence. |
| NewParents-1smncw0 | 2 | Read in full; new evidence. |
| NewParents-1t3twhj | 0 | Off-niche: play-mat and flooring safety for a pre-walking infant; no behaviour or potty issue. |
| NewParents-1tmrk8m | 1 | Read in full; new evidence. |
| NewParents-1u4w79h | 2 | Read in full; new evidence. |
| NewParents-1ugbj7h | 0 | Off-niche: hot-car prevention and caregiver memory; no child behaviour or potty issue. |
| NewParents-1uyjx0l | 1 | Read in full; new evidence. |
| NewParents-1vb1kkf | 2 | Read in full; new evidence. |
| NewParents-1vlq1cp | 0 | Off-niche: crying and feeding concerns centre on a nine-month-old, not the toddler sibling. |
| NewParents-1vzez4p | 1 | Read in full; new evidence. |
| NewParents-1whgihn | 0 | Off-niche: feeding refusal and temperament centre on a ten-month-old, below this build’s age range. |
| NewParents-1wsid2k | 1 | Read in full; new evidence. |
| NewParents-1xdou1b | 0 | Off-niche: response to reported treatment of a dog; toddler age is incidental. |
| Parenting-1sm3h2l | 2 | Read in full; new evidence. |
| Parenting-1stiaby | 1 | Read in full; new evidence. |
| Parenting-1ta985l | 2 | Read in full; new evidence. |
| Parenting-1tinx51 | 1 | Read in full; new evidence. |
| Parenting-1tt9yzo | 0 | Off-niche: newborn-help arrangements and dogs’ house-training; no child behaviour or potty issue. |
| Parenting-1ufb812 | 0 | Off-niche: bedroom allocation driven by older siblings’ privacy; no toddler behaviour or potty issue. |
| Parenting-1umohnd | 2 | Read in full; new evidence. |
| Parenting-1ute04v | 1 | Read in full; new evidence. |
| Parenting-1v7ro5g | 1 | Read in full; new evidence. |
| Parenting-1vh2s7t | 1 | Read in full; new evidence. |
| Parenting-1voo1n5 | 2 | Read in full; new evidence. |
| Parenting-1w2dmqj | 1 | Read in full; new evidence. |
| Parenting-1wlkeuu | 4 | Read in full; new evidence. |
| Parenting-1wwdtg3 | 1 | Read in full; new evidence. |
| ScienceBasedParenting-1stc808 | 1 | Read in full; new evidence. |
| daddit-1sct0aw | 1 | Read in full; new evidence. |
| daddit-1t1yjfz | 2 | Read in full; new evidence. |
| daddit-1ti675z | 1 | Read in full; new evidence. |
| daddit-1u8umdl | 2 | Read in full; new evidence. |
| daddit-1us006k | 1 | Read in full; new evidence. |
| daddit-1v3clfy | 2 | Read in full; new evidence. |
| daddit-1viwyro | 3 | Read in full; new evidence. |
| daddit-1vya30i | 2 | Read in full; new evidence. |
| daddit-1wmtyd3 | 1 | Read in full; new evidence. |
| daddit-1wzrm4c | 0 | Off-niche: father’s custody access, identity and relocation decision; no child behaviour or potty problem described. |
| daddit-1xdy03u | 2 | Read in full; new evidence. |
| pottytraining-1t08cn2 | 3 | Read in full; new evidence. |
| pottytraining-1vjnb2u | 2 | Read in full; new evidence. |
| pottytraining-1wq7ju7 | 2 | Read in full; new evidence. |
| sahm-1snnyr9 | 1 | Read in full; new evidence. |
| sahm-1u8zvrs | 1 | Read in full; new evidence. |
| sahm-1va70t3 | 0 | Off-niche: separation logistics and partner mistreatment; no toddler behaviour or potty issue described. |
| sahm-1x13p2k | 2 | Read in full; new evidence. |
| toddlers-1sbuakl | 1 | Read in full; new evidence. |
| toddlers-1sefitl | 2 | Read in full; new evidence. |
| toddlers-1shpta6 | 1 | Read in full; new evidence. |
| toddlers-1sl13fi | 1 | Read in full; new evidence. |
| toddlers-1snfqtt | 1 | Read in full; new evidence. |
| toddlers-1sputjs | 0 | Off-niche: acute stomach illness, diet and doctor timing; no feeding refusal, behaviour or potty-training issue. |
| toddlers-1sum08l | 0 | Off-niche: choosing a cat or kitten; toddler is described as gentle, without a behaviour or potty issue. |
| toddlers-1t0rq1w | 2 | Read in full; new evidence. |
| toddlers-1t3lvab | 2 | Read in full; new evidence. |
| toddlers-1t5pam0 | 1 | Read in full; new evidence. |
| toddlers-1t99fuk | 1 | Read in full; new evidence. |
| toddlers-1tcjhi4 | 1 | Read in full; new evidence. |
| toddlers-1tgo9ra | 0 | Off-niche: food insecurity, housing and parent’s shoplifting; no toddler behaviour or potty issue described. |
| toddlers-1tksmau | 3 | Read in full; new evidence. |
| toddlers-1togvdp | 2 | Read in full; new evidence. |
| toddlers-1tq9qpd | 2 | Read in full; new evidence. |
| toddlers-1tu1rmu | 2 | Read in full; new evidence. |
| toddlers-1tz9e0j | 0 | Off-niche: milestone and diagnostic prognosis questions; no behaviour-management or potty issue described. |
| toddlers-1u26rqn | 1 | Read in full; new evidence. |
| toddlers-1u4rhtt | 1 | Read in full; new evidence. |
| toddlers-1u8dk0r | 1 | Read in full; new evidence. |
| toddlers-1ucq45j | 1 | Read in full; new evidence. |
| toddlers-1uetbya | 2 | Read in full; new evidence. |
| toddlers-1ujzepv | 2 | Read in full; new evidence. |
| toddlers-1ulsm3p | 1 | Read in full; new evidence. |
| toddlers-1upp92a | 2 | Read in full; new evidence. |
| toddlers-1uu443g | 1 | Read in full; new evidence. |
| toddlers-1v28hcg | 2 | Read in full; new evidence. |
| toddlers-1v5oeq9 | 1 | Read in full; new evidence. |
| toddlers-1v7gmsj | 0 | Off-niche: weight-bearing difficulty after injury and medical follow-up; no behaviour-management or potty issue. |
| toddlers-1vbh5ak | 1 | Read in full; new evidence. |
| toddlers-1vgmzwn | 0 | Off-niche: worsening swollen eye and hospital timing; no behaviour or potty issue. |
| toddlers-1vkl6wd | 1 | Read in full; new evidence. |
| toddlers-1vp1mrf | 2 | Read in full; new evidence. |
| toddlers-1vsqov6 | 1 | Read in full; new evidence. |
| toddlers-1vwblr7 | 2 | Read in full; new evidence. |
| toddlers-1w29ymc | 0 | Off-niche: gross-motor concerns centre on an eleven-month-old; later PT update adds no toddler behaviour or potty account. |
| toddlers-1w620i1 | 1 | Read in full; new evidence. |
| toddlers-1w8ukch | 2 | Read in full; new evidence. |
| toddlers-1wd6ev8 | 1 | Read in full; new evidence. |
| toddlers-1wfe9gm | 1 | Read in full; new evidence. |
| toddlers-1wjz1o9 | 0 | Off-niche: snack choking-risk timing; child eats well and no feeding refusal or behaviour issue is described. |
| toddlers-1worplc | 1 | Read in full; new evidence. |
| toddlers-1wssspm | 2 | Read in full; new evidence. |
| toddlers-1wvk6qg | 0 | Off-niche: acute seizure episode and medical aftermath; no behaviour-management or potty issue. |
| toddlers-1wzhpdp | 1 | Read in full; new evidence. |
| toddlers-1x63fvx | 1 | Read in full; new evidence. |
| toddlers-1x778q2 | 1 | Read in full; new evidence. |
| toddlers-1xc8z6d | 1 | Read in full; new evidence. |
| workingmoms-1tso35c | 1 | Read in full; new evidence. |
| workingmoms-1uvio4l | 0 | Off-niche: illness and sleep concern a four-month-old infant. |
| workingmoms-1vpb7ux | 0 | Off-niche: parent’s mood and household workload; no toddler behaviour or potty issue described. |
| AttachmentParenting-1sicefc | 3 | Read in full; new evidence. |
| AttachmentParenting-1ukoqvz | 3 | Read in full; new evidence. |
| AttachmentParenting-1wpafxo | 1 | Read in full; new evidence. |
| FirstTimeMom-1tlf3gw | 1 | Read in full; new evidence. |
| GentleParenting-1ve0yjn | 3 | Read in full; new evidence. |
| GentleParenting-1woktb4 | 1 | Read in full; new evidence. |
| Mommit-1skjyx3 | 1 | Read in full; new evidence. |
| Mommit-1srr2rt | 2 | Read in full; new evidence. |
| Mommit-1t2qp5i | 1 | Read in full; new evidence. |
| Mommit-1tcjs1j | 3 | Read in full; new evidence. |
| Mommit-1tk4z1u | 0 | Off-niche: parent burnout amid custody conflict and infant sleep loss; no toddler behaviour or potty issue described. |
| Mommit-1u8ef3z | 2 | Read in full; new evidence. |
| Mommit-1ui9f8j | 3 | Read in full; new evidence. |
| Mommit-1uxo9uu | 1 | Read in full; new evidence. |
| Mommit-1v7xu7l | 1 | Read in full; new evidence. |
| Mommit-1vhv3c9 | 1 | Read in full; new evidence. |
| Mommit-1vrcubp | 2 | Read in full; new evidence. |
| Mommit-1w4tbac | 3 | Read in full; new evidence. |
| Mommit-1w9upan | 2 | Read in full; new evidence. |
| Mommit-1wkmm0r | 3 | Read in full; new evidence. |
| Mommit-1woeyo9 | 1 | Read in full; new evidence. |
| Mommit-1ww9ldk | 1 | Read in full; new evidence. |
| Mommit-1x22zx1 | 1 | Read in full; new evidence. |
| Mommit-1xahz2o | 2 | Read in full; new evidence. |
| NewParents-1swlu8s | 2 | Read in full; new evidence. |
| NewParents-1ui66if | 2 | Read in full; new evidence. |
| NewParents-1vg99ac | 1 | Read in full; new evidence. |
| NewParents-1wcw04f | 1 | Read in full; new evidence. |
| NewParents-1x2lx82 | 2 | Read in full; new evidence. |
| Parenting-1souh48 | 1 | Read in full; new evidence. |
| Parenting-1suktb2 | 1 | Read in full; new evidence. |
| Parenting-1t19m46 | 2 | Read in full; new evidence. |
| Parenting-1tbtc8m | 1 | Read in full; new evidence. |
| Parenting-1tpwbed | 1 | Read in full; new evidence. |
| Parenting-1u7376i | 2 | Read in full; new evidence. |
| Parenting-1udqnt9 | 0 | nothing new beyond existing quotes |
| Parenting-1umbaxf | 1 | Read in full; new evidence. |
| Parenting-1ut4m25 | 2 | Read in full; new evidence. |
| Parenting-1uydjlr | 1 | Read in full; new evidence. |
| Parenting-1v6hmts | 1 | Read in full; new evidence. |
| Parenting-1vjo0c2 | 2 | Read in full; new evidence. |
| Parenting-1vssvr1 | 2 | Read in full; new evidence. |
| Parenting-1w8aobo | 1 | Read in full; new evidence. |
| Parenting-1wlpqo4 | 1 | Read in full; new evidence. |
| Parenting-1wr0fuv | 1 | Read in full; new evidence. |
| Parenting-1x3li4n | 1 | Read in full; new evidence. |
| ScienceBasedParenting-1t1ntuw | 2 | Read in full; new evidence. |
| aiparentingcoach-gb-10135414079 | 1 | Read in full; new evidence. |
| barnes-846603623 | 1 | Read in full; new evidence. |
| daddit-1t7p509 | 1 | Read in full; new evidence. |
| daddit-1ubyfgd | 3 | Read in full; new evidence. |
| daddit-1uyb41c | 2 | Read in full; new evidence. |
| daddit-1vc7fpo | 1 | Read in full; new evidence. |
| daddit-1w6q4ou | 1 | Read in full; new evidence. |
| daddit-1wujh4x | 2 | Read in full; new evidence. |
| goodinside-au-11551560103 | 1 | Read in full; new evidence. |
| goodinside-gb-13411570985 | 1 | Read in full; new evidence. |
| pottytraining-1siv2vx | 1 | Read in full; new evidence. |
| pottytraining-1stlbg7 | 1 | Read in full; new evidence. |
| pottytraining-1t4sq2c | 1 | Read in full; new evidence. |
| pottytraining-1ti8onq | 1 | Read in full; new evidence. |
| pottytraining-1ty37jo | 2 | Read in full; new evidence. |
| pottytraining-1u4u2bc | 2 | Read in full; new evidence. |
| pottytraining-1ucorn0 | 1 | Read in full; new evidence. |
| pottytraining-1ukzeb5 | 2 | Read in full; new evidence. |
| pottytraining-1unzu9h | 2 | Read in full; new evidence. |
| pottytraining-1us4v80 | 1 | Read in full; new evidence. |
| pottytraining-1uvsvgy | 2 | Read in full; new evidence. |
| pottytraining-1v1grwl | 1 | Read in full; new evidence. |
| pottytraining-1v6be1h | 1 | Read in full; new evidence. |
| pottytraining-1vd3mzu | 1 | Read in full; new evidence. |
| pottytraining-1vkl15h | 1 | Read in full; new evidence. |
| pottytraining-1vo5e13 | 2 | Read in full; new evidence. |
| pottytraining-1vqtw8r | 2 | Read in full; new evidence. |
| pottytraining-1vuohxk | 2 | Read in full; new evidence. |
| pottytraining-1w181q3 | 1 | Read in full; new evidence. |
| pottytraining-1w9uc38 | 1 | Read in full; new evidence. |
| pottytraining-1we8hmz | 2 | Read in full; new evidence. |
| pottytraining-1winem5 | 1 | Read in full; new evidence. |
| pottytraining-1wnmutd | 1 | Read in full; new evidence. |
| pottytraining-1wp8fdu | 1 | Read in full; new evidence. |
| pottytraining-1wrru80 | 1 | Read in full; new evidence. |
| pottytraining-1x0p8du | 2 | Read in full; new evidence. |
| pottytraining-1x5450n | 1 | Read in full; new evidence. |
| pottytraining-1x8k8hd | 2 | Read in full; new evidence. |
| pottywhiz-au-6994554779 | 1 | Read in full; new evidence. |
| pottywhiz-us-8103259276 | 1 | Read in full; new evidence. |
| sahm-1v9axzd | 3 | Read in full; new evidence. |
| sahm-1ws8mm3 | 1 | Read in full; new evidence. |
| toddlers-1sbgv0d | 1 | Read in full; new evidence. |
| toddlers-1sdkpsc | 1 | Read in full; new evidence. |
| toddlers-1sffva5 | 1 | Read in full; new evidence. |
| toddlers-1shz64u | 1 | Read in full; new evidence. |
| toddlers-1skm57w | 3 | Read in full; new evidence. |
| toddlers-1solau1 | 2 | Read in full; new evidence. |
| toddlers-1sqjmse | 1 | Read in full; new evidence. |
| toddlers-1srrwks | 1 | Read in full; new evidence. |
| toddlers-1su64pz | 1 | Read in full; new evidence. |
| toddlers-1swnu4p | 2 | Read in full; new evidence. |
| toddlers-1t13bju | 1 | Read in full; new evidence. |
| toddlers-1t3uter | 2 | Read in full; new evidence. |
| toddlers-1t7fjjf | 1 | Read in full; new evidence. |
| toddlers-1tb8s2n | 1 | Read in full; new evidence. |
| toddlers-1tffhfi | 2 | Read in full; new evidence. |
| toddlers-1ti7ivf | 3 | Read in full; new evidence. |
| toddlers-1tm7h81 | 2 | Read in full; new evidence. |
| toddlers-1to6o7x | 1 | Read in full; new evidence. |
| toddlers-1tt0bdk | 2 | Read in full; new evidence. |
| toddlers-1u0rb7r | 2 | Read in full; new evidence. |
| toddlers-1u3gjp6 | 2 | Read in full; new evidence. |
| toddlers-1u582ii | 1 | Read in full; new evidence. |
| toddlers-1u7h2m1 | 1 | Read in full; new evidence. |
| toddlers-1ua2ok8 | 2 | Read in full; new evidence. |
| toddlers-1udzurp | 2 | Read in full; new evidence. |
| toddlers-1uhbq1y | 1 | Read in full; new evidence. |
| toddlers-1uk0vsn | 1 | Read in full; new evidence. |
| toddlers-1un4s8c | 2 | Read in full; new evidence. |
| toddlers-1uqdkni | 2 | Read in full; new evidence. |
| toddlers-1usup5w | 2 | Read in full; new evidence. |
| toddlers-1uw44bz | 1 | Read in full; new evidence. |
| toddlers-1uybesz | 1 | Read in full; new evidence. |
| toddlers-1v0w5rl | 1 | Read in full; new evidence. |
| toddlers-1v37wtj | 1 | Read in full; new evidence. |
| toddlers-1v5my9p | 1 | Read in full; new evidence. |
| toddlers-1v7hzsz | 1 | Read in full; new evidence. |
| toddlers-1va2a9s | 1 | Read in full; new evidence. |
| toddlers-1vcsx5y | 2 | Read in full; new evidence. |
| toddlers-1veys99 | 7 | Read in full; new evidence. |
| toddlers-1vjdwjs | 2 | Read in full; new evidence. |
| toddlers-1vlvtag | 1 | Read in full; new evidence. |
| toddlers-1vna98z | 2 | Read in full; new evidence. |
| toddlers-1vpdb3w | 1 | Read in full; new evidence. |
| toddlers-1vr2i2f | 3 | Read in full; new evidence. |
| toddlers-1vt401p | 1 | Read in full; new evidence. |
| toddlers-1vxc9zj | 2 | Read in full; new evidence. |
| toddlers-1vzzbnz | 1 | Read in full; new evidence. |
| toddlers-1w2ikfq | 1 | Read in full; new evidence. |
| toddlers-1w4zt1g | 2 | Read in full; new evidence. |
| toddlers-1w8jf4x | 1 | Read in full; new evidence. |
| toddlers-1wbms70 | 1 | Read in full; new evidence. |
| toddlers-1ween3y | 1 | Read in full; new evidence. |
| toddlers-1wierp2 | 1 | Read in full; new evidence. |
| toddlers-1wmd5ho | 1 | Read in full; new evidence. |
| toddlers-1wmubri | 1 | Read in full; new evidence. |
| toddlers-1wnf1ko | 0 | nothing new beyond existing quotes |
| toddlers-1wo4549 | 3 | Read in full; new evidence. |
| toddlers-1wpf0cp | 1 | Read in full; new evidence. |
| toddlers-1wqfm5j | 1 | Read in full; new evidence. |
| toddlers-1wru48v | 0 | nothing new beyond existing quotes |
| toddlers-1wulqnd | 2 | Read in full; new evidence. |
| toddlers-1wxeek7 | 0 | nothing new beyond existing quotes |
| toddlers-1x0rwq8 | 2 | Read in full; new evidence. |
| toddlers-1x2krbo | 1 | Read in full; new evidence. |
| toddlers-1x53owd | 1 | Read in full; new evidence. |
| toddlers-1xaqyxx | 2 | Read in full; new evidence. |
| toddlers-1xeagyj | 2 | Read in full; new evidence. |
| workingmoms-1xdop35 | 2 | Read in full; new evidence. |

## What these posts add

These observations compare the reread with the existing **2026-11-16** version of `synthesis/findings.md`. That version already restores yelling, punishment, medical context, referral barriers and paid help. Those broad themes are not new discoveries here. The additions below supply missing scenes, mechanisms, outcomes or contrary cases. They are interpretations of selected accounts, not prevalence estimates.

1. **Fear of losing the child can obstruct the parent's own care, beyond fear of being judged.** Section 10.8 records fear of CPS at a paediatric visit. Here a mother plans to conceal suicidal thoughts when seeking medication, reports being told emergency care without childcare could mean foster placement, and later reports better mood after preschool starts. Another parent fears a CPS call over ordinary clutter during home intervention. The practical barrier is who cares for the child while the parent receives help. [tbu01-0357] [tbu01-0359] [tbu01-0360] [tbu01-0362] [tbu01-0040]

2. **The acts hidden before extraction are specific, and some are followed by the child's interpretation.** Beyond the current broad account of acted-on rage: a parent reports slapping a child to stop hitting; a parent reports yelling and squeezing a nursing toddler; another mother shatters a jar after hours of screaming. After a parent calls a potty-trained child a baby, threatens diapers and bins underwear, the child says pooping means the parent is angry. The stated request becomes repairing trust as well as restoring toilet use. [tbu01-0092] [tbu01-0016] [tbu01-0397] [tbu01-0321] [tbu01-0322] [tbu01-0323]

3. **A feared future teenager can drive today's escalation.** One mother explicitly locates her rage in fear that failure to make a toddler obey now will make him unmanageable as a teenager. The parent who slapped a four-year-old first imagined the child hitting his wife as a teenager. A stepfather interprets repeated words after punishment as strategic evasion. These are parents' interpretations of intention, not proof of manipulation or future outcomes. The findings' discussion of discipline needs this time horizon as well as immediate exhaustion. [tbu01-0080] [tbu01-0092] [tbu01-0085]

4. **The starting assumption that behaviour parents already possess the scripts is too broad.** Section 10.3's experienced-parent pattern holds for some, but a first-time mother raised with beating explicitly asks what to say and do when she refuses a knife, and is open to paying for real examples. Other parents describe nonverbal children, limited comprehension, and attempts at signing, pictures, tablets or AAC. A phrase can be unavailable, unusable by the child, or known but ineffective; those are different gaps. [tbu01-0008] [tbu01-0009] [tbu01-0327] [tbu01-0328] [tbu01-0191] [tbu01-0197] [tbu01-0198] [tbu01-0352]

5. **Medical history changes the acceptability of an ordinary tactic.** A parent fears ignoring head banging after a previous fall-related seizure. A mother rejects pinning a child in the bath; another parent restrains a child for dirty pull-up changes while in constant back pain. A pregnant mother cannot physically enforce timeouts because of pain and hard kicks. This makes section 10.2's capacity argument more concrete: the same suggested action has different physical and emotional costs in different homes. [tbu01-0235] [tbu01-0190] [tbu01-0335] [tbu01-0336] [tbu01-0200]

6. **Soft stool and desire to use the potty do not end reported withholding.** The findings recognise constipation and fear, but these passages distinguish stool softness from release: continued withholding on lactulose, repeated rescue suppositories, soft frequent smears, painful holding despite treatment, and anxiety heightened by suppositories. One child cannot accept peeing in the bathtub because the rule says pee does not go there. A parent also describes a four-year-old pooping while asleep. These accounts should not be flattened into refusal, readiness or a reward problem. [tbu01-0257] [tbu01-0266] [tbu01-0290] [tbu01-0293] [tbu01-0377] [tbu01-0385] [tbu01-0386] [tbu01-0387] [tbu01-0066]

7. **Consequences can become an escalating problem of their own.** An increasingly long timeout ends with a child buckled in a booster facing a wall. Removing a movie also removes the father's ninety-minute break. Cleanup can lose its deterrent effect; withholding a twin's snack fails because the other twin kindly shares. There is contrary evidence too: a parent reports initial poop success after forcing a sit, while another explicitly refuses force. These are reported outcomes, not endorsements or recommendations. [tbu01-0244] [tbu01-0245] [tbu01-0278] [tbu01-0389] [tbu01-0261] [tbu01-0282]

8. **Daycare loss is sometimes a stated staffing/body-capacity mismatch, not evidence the child is abnormal.** A provider explicitly calls the behaviours age-expected while explaining stairs, five other children and inability to lift a heavy toddler who goes limp. Another parent considers changing custody arrangements because a 3 p.m. collection demand conflicts with work. A mother takes six weeks of unpaid leave after suspected misconduct and reports less hitting at home. That sits alongside a mother reporting improved mood once preschool provides time for care and appointments. More care and less care each help in different accounts. [tbu01-0163] [tbu01-0192] [tbu01-0296] [tbu01-0297] [tbu01-0362]

9. **Referral accounts include later success, not only refusal, waiting and mismatch.** One parent first reports being denied OT, then months later reports the face-grabbing behaviour has stopped after OT and daycare resume, crediting sensory activities. This is a single, self-reported improvement with multiple changes, not a demonstrated treatment effect. Section 13 says the duration of fixes is unknown; the frozen OP replies nevertheless contain dated later observations that should be distinguished from an absence of follow-up evidence. They do not establish durability. Another cot-transition follow-up reports overnight improvement but continuing rocking needs after a new sibling. [tbu01-0320] [tbu01-0319] [tbu01-0123]

10. **Body/privacy boundaries and grief produce concrete behaviour questions absent from the topical findings.** Parents describe teaching refusal of unwanted touching, a preschooler's privacy requests in public toilets, and a speech-delayed child's limited ability to explain unexpected body-boundary behaviour. A 21-month-old's increased tantrums follow pet loss; the parent asks how to explain death and whether a lookalike toy would help. These belong beside transitions and scripts rather than disappearing under their subject labels. [tbu01-0017] [tbu01-0018] [tbu01-0048] [tbu01-0049] [tbu01-0180] [tbu01-0150] [tbu01-0151]

11. **Fathers' guilt and repair deserve direct visibility beside section 9's scale/rules portrait.** The force-dressing father describes guilt, fear of lasting damage to the relationship, an apology and relief after peer reassurance. Another parent tracks non-yelling days on a fridge list and reports that the streak helps interrupt snapping. A father in a custody arrangement also explicitly asks for help building a safe connection. These do not establish a gender comparison; the father's own emotional vulnerability deserves visibility. [tbu01-0074] [tbu01-0075] [tbu01-0053] [tbu01-0054] The fridge-list case is not assigned a gender. [tbu01-0063] [tbu01-0064]

12. **Judgement-free access and continuing ownership are separate product values.** A parent names a chat tool, in the source's own typo, as the most nonjudgmental guide after books and tactics fail; another explicitly rejects generic articles and AI. A Potty Whiz buyer loses the purchase after a phone upgrade and gets no support response, while another values the at-a-glance accident log. Good Inside reviewers value affirming reminders and, in one reviewer's account, steadiness sufficient to stop therapy. The last claim is personal testimony, not clinical evidence or proof of the proposed plan's value. [tbu01-0347] [tbu01-0028] [tbu01-0294] [tbu01-0295] [tbu01-0253] [tbu01-0254]

The six assigned review units were retained as competitive product feedback, with unknown child ages and no assumption that a review documents a toddler-specific result. No numeric course/app price or verified general efficacy claim was recovered from these six reviews. Named books, programmes and products remain source evidence; selection counts do not estimate demand.
