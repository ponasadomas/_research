# Pregnancy-birth unfilter report — 2026-11-16

Initial inventory written before changing findings, instructions or tools. Scope: `pregnancy-birth/` only; shared scripts and the already-corrected pregnancy prompts are read-only for this task. No network, git, new extraction or raw mutations. Source bodies were opened only by the existing automated provenance verifier; no queue unit was re-read for research. Reader notes, source ledgers and historical run logs remain unchanged. Counts describe selected quotes and recorded omissions, never people or prevalence.

## Verified baseline, by stage

- **Intake / triage:** `_raw/reddit/filter-v1/safety-candidates.jsonl` contains **8,822 distinct posts** routed away before ordinary A/B/C selection. Frozen `_raw/reddit/triage/*.tsv` have **832 distinct dropped posts with subject-related or mixed reasons** (595 explicitly contain `safety:`; 237 have other medical, symptom, safety or mixed-topic reasons) in the conservative review queue. Metadata and reasons, not source bodies, were inspected; overlapping queues must not be added.
- **Reading / quote extraction:** all 72 `sources/reddit-reading-prNN.md` ledgers and corresponding reader notes were scanned for whole-unit exclusions, medical-only no-quote decisions, passing-mention rules and omitted passages. The inventory identifies **2,226 distinct named units** for review: 2,038 have no existing voice quote; 188 have some words extracted but may have withheld passages. Exact ids and recorded reasons are listed below and in the queue; ambiguous mixed reasons are preserved for review rather than recast as proved censorship. The pressure-to-end rule became stricter from PR57, excluding even a passing reference. Recorded withdrawals are detailed below; their ids stay burned. 
- **Marking:** `synthesis/restricted-ids.md` lists **2,265 unique resolving ids**: 2,232 Reddit + 33 reviews. `synthesis/restricted-review-pr01-pr05.tsv` is a quote-level re-review; `restricted-overrides.tsv` adds orchestrator decisions. The review TSV contains 1,176 unique quote rows (206 true, 970 false), and the overrides TSV has 11 unique ids. These overlap the register and are not additional quotes. Wave totals in the register are 763 wave-1 Reddit, 569 wave-2 Reddit, 900 wave-3 Reddit, and 33 reviews. Original `voice/*.jsonl` contain 18,578 records; 33 review records carry historical restriction fields. Before this change, the merged file applied active flags to all marked ids. Those derived flags are now false; `formerly_restricted` preserves the history. Original voice records, including their 33 historical review labels, are unchanged; current lookup and verification tools do not use them to withhold evidence.
- **Findings:** original findings cite **1,158 distinct explicit ids**, including **57 marked ids**, and omit **2,208 marked ids**. Marked citations substitute descriptions or amounts for the speaker's words. The off-limits conclusion in §§6/10/12 and §§16/17 repeated the selection rule as a limitation on research. The shared verifier counted 1,047 bracketed ids in the original; the 1,158 baseline also counts plain references and range endpoints. No ids were inferred between endpoints for this count.
- **Instructions / tooling:** `README.md` and `product/product-brief.md` direct subject exclusions. `_tools/query.py` offers `--exclude-restricted` and an eligibility warning. `scratchpad/FINDINGS/check_frags.py` and `scratchpad/FINDINGS-W2/check_restricted.py`, `scratchpad/FINDINGS-W3/check_restricted.py` reject quoting marked ids; the FINDINGS and FINDINGS-W3 lookup scripts offered an unrestricted-only search. `scratchpad/FINDINGS-W3/trim.py` also omitted restriction-list sections from its output. The wave count scripts read active flags for historical method tables; they now explicitly read the historical marker. Historical per-reader builders and scratch quote inputs record the old selection and must not be rerun to rebuild voice. The three pregnancy reader prompts and pregnancy triage prompt in `../_shared/_tools/` already state the 2026-11-16 principle; no shared file needs editing. Shared verification checks provenance and resolution, not subject.

## What requires re-reading

Removing a marking cannot recover words never extracted. Missing material includes loss and decisions about continuing pregnancy, partner/family coercion and abuse, crises, mental health, medication and substance use, screenings, emergencies/NICU, diagnoses, birth procedures/injuries/outcomes, recovery, exercise and infant safety. Do not infer their frequency or exact missing wording from the surviving voice records. The number of missing quotes is unknown. No raw unit is re-read for this task; metadata-only intake and triage inspection is distinct from provenance checks on existing quotes.

### Extraction decisions and withdrawn records

The queue contains **2,226 named reading-stage units**: **2,038 have no existing voice quote** and **188 have surviving quotes but documented or potentially omitted passages**. An explicit-exclusion subset of 1,250 unit ids is identifiable from exclusion headings/status rows; additional rows record medical-only/symptom-only no-quote decisions, passing-mention handling, mirrored omitted crossposts and passage withdrawals. These are not all proven censorship cases: a thin, duplicate, off-topic or promotional reason can coexist with a subject reason. Each row preserves the actual ledger/note reason so a future reader can distinguish them. All 2,226 ids resolve to units in the frozen reading assignments.

Known selection-related withdrawals leave **36 reserved ids absent from voice** (not 36 newly restored quotes):

| ledger / notes | withdrawn ids |
|---|---|
| `sources/reddit-reading-pr19.md`, `synthesis/reader-notes-pr19.md` | pb19-0076–0078, pb19-0168–0170; `PregnancyUK-1x4qtgl` and `pregnant-1x5lyc5` |
| `sources/reddit-reading-pr24.md` | pb24-0219, 0220, 0240, 0241, 0242, 0248, 0251, 0252 |
| `sources/reddit-reading-pr42.md` | pb42-0132, pb42-0201–0204; `pregnant-1vn9rf1`, `pregnant-1vodfml` |
| `sources/reddit-reading-pr45.md` | pb45-0023–0025, 0055–0056, 0065–0066, 0194–0195, 0209 |
| `sources/reddit-reading-pr50.md` | pb50-0227, pb50-0228 |
| `sources/reddit-reading-pr63.md`, `synthesis/reader-notes-pr63.md` | pb63-0009 (`BabyBumps-1td8qjo`); pb63-0253 (`pregnant-1tgmox3`, friends urging a father to leave, interpreted under the pressure-to-end rule) |
| `sources/reddit-reading-pr64.md` | pb64-0184, pb64-0307, pb64-0308; `BabyBumps-1tivds3`, `pregnant-1tktdfu` |

No absent id was reissued. PR47 additionally records a possible-seeding quote withdrawn before ids were fixed (`Mommit-1ted27k`); that is a provenance omission, not evidence that its subject caused censorship. It is left in the historical ledger rather than miscounted as a restored restricted quote.

### Named units from ledgers and reader notes

These are the exact deduplicated named units in the queue, grouped by the historical reader who logged the reason. A unit may appear under two readers here but has one queue row. Ordinary thin/off-topic reasons mixed with subject reasons remain visible in the TSV for review.

#### Wave 1

**PR01 (7):** `PregnancyUK-1w5ii1i`, `PregnancyUK-1wfdqvx`, `beyondthebump-1w4wbog`, `beyondthebumpUK-1w5l3zw`, `pregnant-1vyycmf`, `pregnant-1wfig6y`, `pregnant-1wl8edq`.

**PR02 (22):** `BabyBumps-1vzg66p`, `BabyBumps-1vzwm41`, `BabyBumps-1w66v0t`, `Doulas-1x4iaw4`, `NewParents-1vzyb0f`, `PregnancyUK-1w69m1c`, `PregnancyUK-1waep30`, `PregnancyUK-1we1pnz`, `beyondthebump-1x4de0b`, `beyondthebump-1x4i7t6`, `pregnant-1vztgcx`, `pregnant-1w0ke6u`, `pregnant-1w2kqyf`, `pregnant-1w558q9`, `pregnant-1w5hk6p`, `pregnant-1w5u2wa`, `pregnant-1w6mybw`, `pregnant-1w7mowo`, `pregnant-1w9nvft`, `pregnant-1x5yf7l`, `pregnant-1xa5pkw`, `pregnant-1xdvvts`.

**PR03 (19):** `BabyBumps-1w5r224`, `BabyBumps-1x6i318`, `PregnancyUK-1wu59vi`, `PregnancyUK-1wy1lqr`, `PregnancyUK-1x4dfmn`, `PregnancyUK-1xcvxp1`, `daddit-1w0v6m3`, `pregnant-1w05mnm`, `pregnant-1w13thm`, `pregnant-1wbgmpu`, `pregnant-1whfe3a`, `pregnant-1wnpjou`, `pregnant-1x5is5n`, `pregnant-1x5pkc2`, `pregnant-1x8eb8h`, `pregnant-1x90fo3`, `pregnant-1xa6jqq`, `pregnant-1xbknhq`, `pregnant-1xcw08z`.

**PR04 (14):** `BabyBumps-1wn6zm2`, `BabyBumps-1wsku94`, `BabyBumps-1x42giv`, `daddit-1wmtazi`, `daddit-1wx314d`, `daddit-1x8yymw`, `pregnant-1wh55wd`, `pregnant-1wnch4w`, `pregnant-1wqduiy`, `pregnant-1wtsxg5`, `pregnant-1wv8s4a`, `pregnant-1wzitm0`, `pregnant-1x5hdu8`, `pregnant-1x5zr7t`.

**PR05 (23):** `BabyBumps-1vz2lwu`, `BabyBumps-1vz3df5`, `BabyBumps-1vz6rpy`, `NewParents-1vzpawo`, `PregnancyUK-1vyripz`, `beyondthebump-1vy8rki`, `beyondthebump-1vz2n7u`, `daddit-1xc3ywm`, `pregnant-1vxlc1s`, `pregnant-1vxm3wd`, `pregnant-1vxrxxy`, `pregnant-1vxu7vk`, `pregnant-1vxxomh`, `pregnant-1vya6d8`, `pregnant-1vyhzkz`, `pregnant-1vyirpn`, `pregnant-1vyw78i`, `pregnant-1vz3uef`, `pregnant-1vzacg2`, `pregnant-1vzbbrv`, `pregnant-1vzdjkd`, `pregnant-1vzeplb`, `pregnant-1vziu19`.

**PR06 (44):** `BabyBumps-1w01r50`, `BabyBumps-1w09tkq`, `BabyBumps-1w0cvnx`, `BabyBumps-1w0xoi2`, `BabyBumps-1w10j7b`, `BabyBumps-1w1g3ni`, `BabyBumps-1w1l5oh`, `BabyBumps-1w32cdn`, `Mommit-1w1bl1g`, `Mommit-1w23z99`, `NewParents-1w01zn4`, `NewParents-1w2a29p`, `PregnancyUK-1w21hd0`, `beyondthebump-1w0ssbt`, `beyondthebump-1w10c6j`, `beyondthebump-1w20csg`, `beyondthebump-1w33zv8`, `pregnant-1vzsvq7`, `pregnant-1vzxt60`, `pregnant-1w01q50`, `pregnant-1w02u7z`, `pregnant-1w04mov`, `pregnant-1w09bpk`, `pregnant-1w0hczq`, `pregnant-1w0p8mz`, `pregnant-1w0wabt`, `pregnant-1w0y0ua`, `pregnant-1w0zlh8`, `pregnant-1w16136`, `pregnant-1w17ask`, `pregnant-1w182ko`, `pregnant-1w19or6`, `pregnant-1w1juw5`, `pregnant-1w1mo12`, `pregnant-1w1oto9`, `pregnant-1w25035`, `pregnant-1w2ga5b`, `pregnant-1w2hmmo`, `pregnant-1w2may7`, `pregnant-1w2nvvd`, `pregnant-1w31ut0`, `pregnant-1w3244f`, `pregnant-1w37gvh`, `pregnant-1w39ccq`.

**PR07 (7):** `BabyBumps-1w4k0wr`, `pregnant-1w45fy4`, `pregnant-1w460o8`, `pregnant-1w4dca3`, `pregnant-1w5pvsg`, `pregnant-1w5qu58`, `pregnant-1w6fs7z`.

**PR08 (26):** `BabyBumps-1w73219`, `BabyBumps-1w7sutd`, `BabyBumps-1w947a4`, `PregnancyUK-1w7lgxu`, `PregnancyUK-1w9ysn7`, `beyondthebump-1w83xqc`, `pregnant-1w6p0e2`, `pregnant-1w74t4v`, `pregnant-1w767dq`, `pregnant-1w782vh`, `pregnant-1w7a5ud`, `pregnant-1w7m5ew`, `pregnant-1w7mueg`, `pregnant-1w7p3p5`, `pregnant-1w80n0l`, `pregnant-1w81fb4`, `pregnant-1w83mra`, `pregnant-1w8t308`, `pregnant-1w8vtmg`, `pregnant-1w8zlit`, `pregnant-1w90stw`, `pregnant-1w99bnb`, `pregnant-1w9au14`, `pregnant-1wa1vxm`, `pregnant-1wa472u`, `pregnant-1wa5xfq`.

**PR09 (29):** `BabyBumps-1waosu0`, `Mommit-1wbza4q`, `NewParents-1waidqr`, `NewParents-1wb7qg3`, `NewParents-1wb88lw`, `PregnancyUK-1wb3308`, `PregnancyUK-1wbsnyb`, `PregnancyUK-1wbswno`, `beyondthebump-1war0q6`, `beyondthebump-1wbpzf0`, `pregnant-1wa759k`, `pregnant-1wa7t9z`, `pregnant-1wac1ab`, `pregnant-1wad828`, `pregnant-1wapm0b`, `pregnant-1wav0eb`, `pregnant-1wb2vxt`, `pregnant-1wb3xq6`, `pregnant-1wb6emm`, `pregnant-1wb8y9x`, `pregnant-1wbblce`, `pregnant-1wbv3cs`, `pregnant-1wbwj15`, `pregnant-1wbx03q`, `pregnant-1wby9s8`, `pregnant-1wc19qm`, `pregnant-1wc4l3f`, `pregnant-1wc4o13`, `pregnant-1wcairk`.

**PR10 (32):** `BabyBumps-1wd437s`, `BabyBumps-1wev971`, `BabyBumps-1wfbkdw`, `Mommit-1wev8ty`, `PregnancyUK-1wd54pg`, `PregnancyUK-1wed0gg`, `beyondthebump-1wd20th`, `beyondthebump-1wd75as`, `pregnant-1wcoexe`, `pregnant-1wcqqna`, `pregnant-1wcsyad`, `pregnant-1wcua3y`, `pregnant-1wcvpd9`, `pregnant-1wcykog`, `pregnant-1wd0y4j`, `pregnant-1wdgowx`, `pregnant-1wdjruw`, `pregnant-1wdm58t`, `pregnant-1wdor47`, `pregnant-1wdx5ag`, `pregnant-1webk69`, `pregnant-1weljdd`, `pregnant-1wes7w6`, `pregnant-1weudlc`, `pregnant-1wevrnm`, `pregnant-1wewjb1`, `pregnant-1wf6dis`, `pregnant-1wf7vkq`, `pregnant-1wf8bxs`, `pregnant-1wfjagz`, `pregnant-1wfoj19`, `pregnant-1wfrx2w`.

**PR11 (35):** `BabyBumps-1wgedwf`, `BabyBumps-1wgf9xo`, `BabyBumps-1wggrws`, `BabyBumps-1wh5vxy`, `BabyBumps-1whwq3c`, `PregnancyUK-1wj11f2`, `beyondthebump-1whgsua`, `beyondthebumpUK-1wi97xj`, `beyondthebumpUK-1wizrwo`, `pregnant-1wgaix2`, `pregnant-1wgg6t0`, `pregnant-1wgi8kk`, `pregnant-1wgmch6`, `pregnant-1wgowx5`, `pregnant-1wgp7qr`, `pregnant-1wgx71z`, `pregnant-1wh09oc`, `pregnant-1wh1fp0`, `pregnant-1wh55m3`, `pregnant-1whbp6y`, `pregnant-1whdwpl`, `pregnant-1whge27`, `pregnant-1who0d0`, `pregnant-1whp80g`, `pregnant-1wi1ani`, `pregnant-1wi9kbt`, `pregnant-1widh2h`, `pregnant-1winvar`, `pregnant-1winxs6`, `pregnant-1wiy65q`, `pregnant-1wj0um0`, `pregnant-1wj3c0i`, `pregnant-1wj3sb6`, `pregnant-1wj4p8f`, `pregnant-1wj5p0n`.

**PR12 (21):** `BabyBumps-1wk627b`, `BabyBumps-1wk9ktr`, `BabyBumps-1wlv57c`, `Mommit-1wj70gb`, `Mommit-1wkxzu3`, `NewParents-1wjpkus`, `NewParents-1wk8cgd`, `beyondthebump-1wjyekk`, `beyondthebump-1wkn1ek`, `beyondthebumpUK-1wkqegu`, `pregnant-1wj8ijh`, `pregnant-1wjba17`, `pregnant-1wjhkg8`, `pregnant-1wjk7i3`, `pregnant-1wjwea2`, `pregnant-1wkee65`, `pregnant-1wkscug`, `pregnant-1wl6v40`, `pregnant-1wl7384`, `pregnant-1wl7fuc`, `pregnant-1wl7qkm`.

**PR13 (57):** `BabyBumps-1wmp5xe`, `BabyBumps-1wn2yur`, `BabyBumps-1wnbj09`, `BabyBumps-1wnnq3x`, `BabyBumps-1wnqgll`, `BabyBumps-1wofcue`, `FirstTimeMom-1wo4bla`, `NewParents-1wn37wn`, `PregnancyUK-1wn6yxt`, `PregnancyUK-1wnfdv1`, `PregnancyUK-1wnj55o`, `PregnancyUK-1wobgst`, `PregnancyUK-1woe3yx`, `beyondthebump-1wmob14`, `beyondthebump-1wn38ir`, `beyondthebump-1wnz8x4`, `beyondthebump-1wocwcs`, `beyondthebump-1wod3st`, `beyondthebump-1woi2hr`, `beyondthebump-1wosmok`, `beyondthebumpUK-1woyf76`, `pregnant-1wmg9m8`, `pregnant-1wmhv5w`, `pregnant-1wmkuzm`, `pregnant-1wmmqo7`, `pregnant-1wmv4x1`, `pregnant-1wmxgee`, `pregnant-1wn0inz`, `pregnant-1wn51g0`, `pregnant-1wn66xq`, `pregnant-1wn7ytg`, `pregnant-1wnan3j`, `pregnant-1wnc0q5`, `pregnant-1wnd923`, `pregnant-1wnovcv`, `pregnant-1wnu9mi`, `pregnant-1wnvm2o`, `pregnant-1wnwh8u`, `pregnant-1wnwmfz`, `pregnant-1wnyjyy`, `pregnant-1wnzj53`, `pregnant-1wo0s7j`, `pregnant-1wo1yqx`, `pregnant-1wo6jpv`, `pregnant-1wo7n7d`, `pregnant-1wobgfk`, `pregnant-1wodumv`, `pregnant-1wof3la`, `pregnant-1wofpyu`, `pregnant-1wogqyu`, `pregnant-1wogx18`, `pregnant-1wojxjz`, `pregnant-1woqsfa`, `pregnant-1worxox`, `pregnant-1woupys`, `pregnant-1wp2dlp`, `pregnant-1wp3m00`.

**PR14 (35):** `BabyBumps-1wqbi7l`, `Mommit-1wq865v`, `Mommit-1wqhhbz`, `Mommit-1wqi6co`, `NewParents-1wrq06r`, `PregnancyUK-1wp71vc`, `PregnancyUK-1wqtxd3`, `beyondthebump-1wq1ydt`, `beyondthebump-1wqjt5o`, `beyondthebump-1wrl6zo`, `pregnant-1wp4uei`, `pregnant-1wp5ucc`, `pregnant-1wpcik0`, `pregnant-1wpenjc`, `pregnant-1wplvos`, `pregnant-1wpm4wz`, `pregnant-1wpmw5m`, `pregnant-1wps16m`, `pregnant-1wq1zb6`, `pregnant-1wq28ub`, `pregnant-1wq4j3g`, `pregnant-1wq5oou`, `pregnant-1wq94cm`, `pregnant-1wq9atb`, `pregnant-1wqbtxi`, `pregnant-1wqhugm`, `pregnant-1wqi6rh`, `pregnant-1wqp8zm`, `pregnant-1wqs1kh`, `pregnant-1wqv8c3`, `pregnant-1wr5kjl`, `pregnant-1wr7kgl`, `pregnant-1wr85qy`, `pregnant-1wr91dc`, `pregnant-1wrpbgk`.

**PR15 (34):** `BabyBumps-1wsupfq`, `Mommit-1wu8cay`, `PregnancyUK-1wsiogf`, `PregnancyUK-1wsnn13`, `PregnancyUK-1wt572d`, `PregnancyUK-1wtgqtu`, `beyondthebump-1ws4m83`, `beyondthebump-1wt4hzq`, `beyondthebump-1wu8e49`, `pregnant-1ws8z2v`, `pregnant-1ws9pcr`, `pregnant-1wsbgnp`, `pregnant-1wsl77r`, `pregnant-1wspuwi`, `pregnant-1wssvda`, `pregnant-1wsz2r1`, `pregnant-1wt6vkx`, `pregnant-1wtbf7j`, `pregnant-1wtgr59`, `pregnant-1wth098`, `pregnant-1wtl7j0`, `pregnant-1wtm4qg`, `pregnant-1wtw4jp`, `pregnant-1wtzga1`, `pregnant-1wtzuqv`, `pregnant-1wu7p4g`, `pregnant-1wu8557`, `pregnant-1wu8jwe`, `pregnant-1wudn5p`, `pregnant-1wue3wt`, `pregnant-1wufrfg`, `pregnant-1wugvyd`, `pregnant-1wujn1r`, `pregnant-1wuk85o`.

**PR16 (29):** `BabyBumps-1wuvqd9`, `BabyBumps-1wvl9fj`, `BabyBumps-1wwegjd`, `BabyBumps-1wwpdff`, `NewParents-1wvdtw5`, `PregnancyUK-1wvqcm1`, `PregnancyUK-1wvrlmc`, `PregnancyUK-1wxzgye`, `beyondthebump-1wusa5x`, `beyondthebump-1wvyqyp`, `beyondthebump-1wwt9ad`, `beyondthebump-1wwuw1m`, `pregnant-1wuydcy`, `pregnant-1wv7bc3`, `pregnant-1wv8onb`, `pregnant-1wv8zzb`, `pregnant-1wvbv9c`, `pregnant-1wvjflz`, `pregnant-1wvy8ra`, `pregnant-1ww3xq5`, `pregnant-1ww5jwi`, `pregnant-1ww79gu`, `pregnant-1wwii4l`, `pregnant-1wwuael`, `pregnant-1wwy8i0`, `pregnant-1wx0oju`, `pregnant-1wxfaro`, `pregnant-1wxk0sy`, `pregnant-1wxmuj2`.

**PR17 (42):** `BabyBumps-1wy7r5z`, `BabyBumps-1wyfyn0`, `BabyBumps-1wzscwq`, `BabyBumps-1x0junq`, `Mommit-1wylt39`, `PregnancyUK-1wz923z`, `PregnancyUK-1wzppbb`, `PregnancyUK-1wzpq7u`, `beyondthebump-1wzqwlf`, `beyondthebumpUK-1wyc920`, `pregnant-1wya10v`, `pregnant-1wybhin`, `pregnant-1wyewzq`, `pregnant-1wyg5wy`, `pregnant-1wyh5dj`, `pregnant-1wylrmi`, `pregnant-1wymoi5`, `pregnant-1wyphw6`, `pregnant-1wyr2l3`, `pregnant-1wyuo5d`, `pregnant-1wywym7`, `pregnant-1wz3fso`, `pregnant-1wz3gwl`, `pregnant-1wz4y3n`, `pregnant-1wz60dc`, `pregnant-1wz956y`, `pregnant-1wzbx73`, `pregnant-1wze9ax`, `pregnant-1wzh6f6`, `pregnant-1wzjm8e`, `pregnant-1wzptsl`, `pregnant-1wzxnlj`, `pregnant-1x044cj`, `pregnant-1x05yoc`, `pregnant-1x0ct7n`, `pregnant-1x0d0ig`, `pregnant-1x0d8ks`, `pregnant-1x0eccj`, `pregnant-1x0eren`, `pregnant-1x0nffp`, `pregnant-1x0oezy`, `pregnant-1x0w3p0`.

**PR18 (19):** `FirstTimeMom-1x20ph1`, `FirstTimeMom-1x2nu1o`, `NewParents-1x347i5`, `PregnancyUK-1x2sqlm`, `PregnancyUK-1x3xmoh`, `beyondthebump-1x351x1`, `pregnant-1x11lci`, `pregnant-1x14ztn`, `pregnant-1x16dl1`, `pregnant-1x1a1c5`, `pregnant-1x1csgv`, `pregnant-1x1gbn7`, `pregnant-1x1hsty`, `pregnant-1x1lj12`, `pregnant-1x1tk1b`, `pregnant-1x24muu`, `pregnant-1x2uem6`, `pregnant-1x3c8i9`, `pregnant-1x3i4ee`.

**PR19 (33):** `BabyBumps-1x4zegh`, `BabyBumps-1x5yfqf`, `BabyBumps-1x6lwy3`, `FirstTimeMom-1x4jfjk`, `FirstTimeMom-1x5snya`, `PregnancyUK-1x45w0a`, `PregnancyUK-1x4qtgl`, `PregnancyUK-1x4s1yo`, `PregnancyUK-1x616ko`, `PregnancyUK-1x6gh03`, `beyondthebumpUK-1x4ez8s`, `pregnant-1x48y0f`, `pregnant-1x4inkd`, `pregnant-1x4nv71`, `pregnant-1x4nyhd`, `pregnant-1x4xztu`, `pregnant-1x58quy`, `pregnant-1x5aobh`, `pregnant-1x5g7pg`, `pregnant-1x5hxqd`, `pregnant-1x5lyc5`, `pregnant-1x5oev8`, `pregnant-1x5qn02`, `pregnant-1x5v0xj`, `pregnant-1x5yelt`, `pregnant-1x62nn6`, `pregnant-1x63trm`, `pregnant-1x68znj`, `pregnant-1x6a1ua`, `pregnant-1x6cmn3`, `pregnant-1x6e50w`, `pregnant-1x6ej83`, `pregnant-1x6fe4z`.

**PR20 (50):** `BabyBumps-1x74cwp`, `BabyBumps-1x7ii81`, `BabyBumps-1x7iq44`, `BabyBumps-1x8o36a`, `BabyBumps-1x9ecf4`, `BabyBumps-1xaf7qb`, `FirstTimeMom-1x9zut9`, `Mommit-1x91uvs`, `NewParents-1xaf01e`, `PregnancyUK-1x7b71t`, `PregnancyUK-1x7f2bb`, `PregnancyUK-1x7psd3`, `PregnancyUK-1x83avz`, `PregnancyUK-1x85g64`, `PregnancyUK-1x86wqp`, `beyondthebumpUK-1x8dvua`, `pregnant-1x7bo27`, `pregnant-1x7oeyk`, `pregnant-1x7olkx`, `pregnant-1x7tn09`, `pregnant-1x7y813`, `pregnant-1x82gz3`, `pregnant-1x83nia`, `pregnant-1x83xyu`, `pregnant-1x88a12`, `pregnant-1x8a3h7`, `pregnant-1x8dt22`, `pregnant-1x8k3oh`, `pregnant-1x8lg1n`, `pregnant-1x8vxlg`, `pregnant-1x92m14`, `pregnant-1x96xzh`, `pregnant-1x9aqr2`, `pregnant-1x9dkib`, `pregnant-1x9g68h`, `pregnant-1x9gapa`, `pregnant-1x9i0vw`, `pregnant-1x9iiey`, `pregnant-1x9jhth`, `pregnant-1x9l8ij`, `pregnant-1x9zaxb`, `pregnant-1x9zvqi`, `pregnant-1xa0cbb`, `pregnant-1xa20nq`, `pregnant-1xa28ot`, `pregnant-1xa61ca`, `pregnant-1xa6zbe`, `pregnant-1xa74bn`, `pregnant-1xaahlg`, `pregnant-1xaf024`.

**PR21 (32):** `BabyBumps-1xalapm`, `BabyBumps-1xb1lh2`, `BabyBumps-1xb9j6u`, `BabyBumps-1xbfc5e`, `BabyBumps-1xbfy57`, `FirstTimeMom-1xcucjl`, `NewParents-1xc5qi2`, `PregnancyUK-1xbp720`, `PregnancyUK-1xcnvs0`, `beyondthebumpUK-1xc7ugk`, `pregnant-1xaig0u`, `pregnant-1xannqs`, `pregnant-1xao9fn`, `pregnant-1xaqivv`, `pregnant-1xatjs0`, `pregnant-1xaxk1y`, `pregnant-1xaxkft`, `pregnant-1xb2rm9`, `pregnant-1xb3pa4`, `pregnant-1xb7seb`, `pregnant-1xb9kem`, `pregnant-1xbgve7`, `pregnant-1xbmod8`, `pregnant-1xbmz2a`, `pregnant-1xbq4sy`, `pregnant-1xbyk2u`, `pregnant-1xc2fi3`, `pregnant-1xc2wht`, `pregnant-1xc6rf9`, `pregnant-1xcamfp`, `pregnant-1xcccns`, `pregnant-1xcl3yw`.

**PR22 (19):** `BabyBumps-1xcx130`, `BabyBumps-1xdl8xu`, `BabyBumps-1xdqau8`, `Mommit-1xdnztg`, `PregnancyUK-1xeiizo`, `pregnant-1xcuxyd`, `pregnant-1xcvuuq`, `pregnant-1xcx0jy`, `pregnant-1xcxzby`, `pregnant-1xdg6at`, `pregnant-1xdif63`, `pregnant-1xdkphx`, `pregnant-1xdqhvw`, `pregnant-1xdv88d`, `pregnant-1xdw9qf`, `pregnant-1xeaxez`, `pregnant-1xejavh`, `pregnant-1xelgts`, `pregnant-1xem80n`.

#### Wave 2

**PR23 (11):** `BabyBumps-1urckhv`, `Mommit-1v1qtqj`, `PregnancyUK-1v8sjl1`, `beyondthebumpUK-1vbfq9s`, `pregnant-1ufndmj`, `pregnant-1ufwbav`, `pregnant-1urzdz1`, `pregnant-1us1thy`, `pregnant-1v41uu3`, `pregnant-1v45o2c`, `pregnant-1vb5mjj`.

**PR24 (9):** `BabyBumps-1ufp5jb`, `beyondthebump-1um1nkx`, `pregnant-1ufoxxn`, `pregnant-1ug6cnj`, `pregnant-1ukl4kd`, `pregnant-1ul9wl0`, `pregnant-1uldtd8`, `pregnant-1ulgd8e`, `pregnant-1ulwa1t`.

**PR25 (40):** `BabyBumps-1uqgehr`, `BabyBumps-1v58pvs`, `BabyBumps-1vfn3vh`, `BabyBumps-1vk61nh`, `PregnancyUK-1uqvjnp`, `PregnancyUK-1uvepdu`, `PregnancyUK-1v402lk`, `PregnancyUK-1vjvt93`, `PregnancyUK-1vqepb4`, `beyondthebump-1v5hlug`, `daddit-1uiy41b`, `pregnant-1uew6kz`, `pregnant-1ukldyz`, `pregnant-1up3urn`, `pregnant-1upfb4s`, `pregnant-1upjnzx`, `pregnant-1uqanod`, `pregnant-1urjvvw`, `pregnant-1uta224`, `pregnant-1uzd5mb`, `pregnant-1uziatw`, `pregnant-1v14xee`, `pregnant-1v1i3z8`, `pregnant-1v2bp46`, `pregnant-1v52xam`, `pregnant-1v7b9p3`, `pregnant-1v9ibog`, `pregnant-1ve1ffx`, `pregnant-1vh4lar`, `pregnant-1vht81g`, `pregnant-1viw8yb`, `pregnant-1vkk2bn`, `pregnant-1vktkvy`, `pregnant-1vluvxk`, `pregnant-1vmk6ym`, `pregnant-1vp4gqc`, `pregnant-1vqesty`, `pregnant-1vqmuxk`, `pregnant-1vvyx0l`, `pregnant-1vwgbj9`.

**PR26 (18):** `BabyBumps-1urdcby`, `BabyBumps-1uu6r1g`, `BabyBumps-1uv1wpj`, `NewParents-1vbzrwd`, `NewParents-1vc4w71`, `PregnancyUK-1ur63a0`, `PregnancyUK-1urrsll`, `beyondthebump-1uwk6ng`, `beyondthebump-1v8vuff`, `daddit-1ux76wz`, `daddit-1vaysz7`, `daddit-1vehzsk`, `pregnant-1uy8buo`, `pregnant-1v08z9s`, `pregnant-1v486uj`, `pregnant-1v6x692`, `pregnant-1v9s929`, `pregnant-1vazur1`.

**PR27 (12):** `BabyBumps-1uf1amy`, `BabyBumps-1ufyqqg`, `FirstTimeMom-1ufbvcz`, `Mommit-1ufovgf`, `NewParents-1vioyer`, `beyondthebump-1vlmuqc`, `daddit-1vmo020`, `pregnant-1uf1sjc`, `pregnant-1uf7yvt`, `pregnant-1ufbhgo`, `pregnant-1ufky4g`, `pregnant-1ufuxv8`.

**PR28 (18):** `Mommit-1ugv10l`, `PregnancyUK-1ugwiar`, `PregnancyUK-1uh7l4u`, `PregnancyUK-1uhv7ep`, `beyondthebump-1uh4aqd`, `beyondthebump-1uhgneo`, `beyondthebumpUK-1uhzqlf`, `pregnant-1ug7gkb`, `pregnant-1ugc36x`, `pregnant-1ugd3au`, `pregnant-1ugl5lg`, `pregnant-1ugrcfz`, `pregnant-1uh49iq`, `pregnant-1uh77or`, `pregnant-1uh9bzu`, `pregnant-1uhmm85`, `pregnant-1uim5h3`, `pregnant-1uj1nw6`.

**PR29 (32):** `BabyBumps-1ul55s0`, `BabyBumps-1ulhzmo`, `BabyBumps-1ulmn1n`, `Mommit-1ulj9nd`, `PregnancyUK-1ujpzyj`, `PregnancyUK-1ukk6gx`, `PregnancyUK-1ulraf5`, `beyondthebump-1uk0k84`, `beyondthebump-1uk1avc`, `beyondthebump-1uk38zq`, `beyondthebumpUK-1uk59ih`, `pregnant-1ujmf8x`, `pregnant-1ujtxrp`, `pregnant-1ujxo4c`, `pregnant-1uk101t`, `pregnant-1uk6d2t`, `pregnant-1uk8g4m`, `pregnant-1ukazpg`, `pregnant-1ukgiol`, `pregnant-1ukj2r4`, `pregnant-1ukrfot`, `pregnant-1ukt8wl`, `pregnant-1ukz79z`, `pregnant-1ul2jyo`, `pregnant-1ul56al`, `pregnant-1ul6l56`, `pregnant-1ulbsnd`, `pregnant-1ullks6`, `pregnant-1ulnkgp`, `pregnant-1uls7wn`, `pregnant-1ultobi`, `pregnant-1ulvlc8`.

**PR30 (41):** `BabyBumps-1ummjba`, `BabyBumps-1un5zzf`, `BabyBumps-1unhcit`, `BabyBumps-1uo17bz`, `BabyBumps-1uogpma`, `PregnancyUK-1umhl9e`, `PregnancyUK-1unkb02`, `beyondthebump-1ums7lq`, `beyondthebump-1uok4pc`, `pregnant-1um57pr`, `pregnant-1uma1ko`, `pregnant-1umiogu`, `pregnant-1umiw72`, `pregnant-1umkcnd`, `pregnant-1umss10`, `pregnant-1umtzzq`, `pregnant-1umxk4o`, `pregnant-1umziqy`, `pregnant-1umzo9i`, `pregnant-1un14yi`, `pregnant-1un2e5z`, `pregnant-1un5p9h`, `pregnant-1un73zj`, `pregnant-1unb9ni`, `pregnant-1unbvor`, `pregnant-1und4ru`, `pregnant-1unhaa5`, `pregnant-1unnyc0`, `pregnant-1unsobb`, `pregnant-1unwliw`, `pregnant-1unze18`, `pregnant-1uo13p9`, `pregnant-1uo2dtb`, `pregnant-1uo2rfu`, `pregnant-1uo2x3m`, `pregnant-1uo6mol`, `pregnant-1uo7j4n`, `pregnant-1uo8gh6`, `pregnant-1uoadn4`, `pregnant-1uofqc8`, `pregnant-1uoo6o8`.

**PR31 (26):** `BabyBumps-1upaov4`, `BabyBumps-1upccmc`, `BabyBumps-1upxxrs`, `BabyBumps-1uqoyh2`, `BabyBumps-1uqrp46`, `FirstTimeMom-1uqbzn4`, `Mommit-1upeld1`, `Mommit-1uqa016`, `NewParents-1uq8udg`, `NewParents-1uqci6w`, `PregnancyUK-1upaazp`, `PregnancyUK-1upmxrd`, `PregnancyUK-1uqvkd6`, `beyondthebump-1upztpw`, `pregnant-1uop47m`, `pregnant-1upcpde`, `pregnant-1upr9g8`, `pregnant-1upy1yp`, `pregnant-1upy2f2`, `pregnant-1uq3jks`, `pregnant-1uq9594`, `pregnant-1uqdo2p`, `pregnant-1uqk8y2`, `pregnant-1uqnv78`, `pregnant-1uqsvj8`, `pregnant-1ur8t3b`.

**PR32 (29):** `BabyBumps-1urv4yc`, `BabyBumps-1urxr94`, `BabyBumps-1ut6r7b`, `BabyBumps-1utahpi`, `BabyBumps-1utqfle`, `PregnancyUK-1urhulf`, `beyondthebump-1usgla3`, `beyondthebump-1ustij6`, `beyondthebump-1usvd4g`, `beyondthebump-1ut0s1o`, `beyondthebump-1utqv9r`, `beyondthebumpUK-1usosml`, `pregnant-1urbyrm`, `pregnant-1ure2ji`, `pregnant-1uroysz`, `pregnant-1us3hh0`, `pregnant-1us5a06`, `pregnant-1us61nc`, `pregnant-1usbaz8`, `pregnant-1ut0uu0`, `pregnant-1ut2qi7`, `pregnant-1ut3we5`, `pregnant-1ut6dh4`, `pregnant-1utotvl`, `pregnant-1utpyu7`, `pregnant-1utucn5`, `pregnant-1uu23zx`, `pregnant-1uu3toa`, `pregnant-1uuc3qv`.

**PR33 (32):** `BabyBumps-1uuoe7x`, `BabyBumps-1uus9vu`, `BabyBumps-1uvpitn`, `BabyBumps-1uw3199`, `BabyBumps-1uw5nsk`, `BabyBumps-1uwl854`, `BabyBumps-1uwlfqp`, `BabyBumps-1uwlzxo`, `NewParents-1uw0no7`, `NewParents-1ux0aqg`, `PregnancyUK-1uvofjc`, `pregnant-1uugdte`, `pregnant-1uup8od`, `pregnant-1uurnks`, `pregnant-1uuro5l`, `pregnant-1uut6kh`, `pregnant-1uv0lhf`, `pregnant-1uv9x5o`, `pregnant-1uvdp1s`, `pregnant-1uvh25m`, `pregnant-1uvkbzm`, `pregnant-1uvmyjn`, `pregnant-1uvqhwm`, `pregnant-1uvr4s1`, `pregnant-1uvzirq`, `pregnant-1uw3dnq`, `pregnant-1uw74j8`, `pregnant-1uw7d7y`, `pregnant-1uwcepd`, `pregnant-1uwe8o8`, `pregnant-1uwp4yv`, `pregnant-1ux2ch1`.

**PR34 (36):** `BabyBumps-1uxbwqm`, `BabyBumps-1uym528`, `BabyBumps-1uzzdwh`, `Mommit-1uxcvnm`, `NewParents-1ux7g4n`, `PregnancyUK-1uxzgor`, `PregnancyUK-1uy24qp`, `PregnancyUK-1uyhsda`, `PregnancyUK-1uysd4j`, `PregnancyUK-1uytlyj`, `PregnancyUK-1uzszvo`, `PregnancyUK-1uzv2ni`, `beyondthebump-1uylex1`, `beyondthebump-1v03ja2`, `pregnant-1ux7inz`, `pregnant-1uxih82`, `pregnant-1uxku20`, `pregnant-1uxpo2z`, `pregnant-1uy0qrx`, `pregnant-1uy4ucv`, `pregnant-1uy4w50`, `pregnant-1uy6pvb`, `pregnant-1uy9vvb`, `pregnant-1uydby4`, `pregnant-1uyhv54`, `pregnant-1uyzrg8`, `pregnant-1uz0cpn`, `pregnant-1uz2yic`, `pregnant-1uzd449`, `pregnant-1uze8ps`, `pregnant-1uzii06`, `pregnant-1uzzpek`, `pregnant-1v02f3y`, `pregnant-1v030wp`, `pregnant-1v07f37`, `pregnant-1v07nbz`.

**PR35 (25):** `BabyBumps-1v0abgw`, `BabyBumps-1v0bf24`, `BabyBumps-1v2fedo`, `BabyBumps-1v2h1ij`, `BabyBumps-1v2z70y`, `BabyBumps-1v2zid1`, `Mommit-1v2437j`, `PregnancyUK-1v0t28i`, `PregnancyUK-1v1s54f`, `beyondthebump-1v09wq1`, `pregnant-1v0c4bs`, `pregnant-1v0zp0b`, `pregnant-1v1380a`, `pregnant-1v14w5d`, `pregnant-1v167tb`, `pregnant-1v19ddq`, `pregnant-1v1afkr`, `pregnant-1v1lesc`, `pregnant-1v1ns1h`, `pregnant-1v22a9a`, `pregnant-1v297g3`, `pregnant-1v2d5rb`, `pregnant-1v2m21i`, `pregnant-1v2qhi6`, `pregnant-1v2vc2c`.

**PR36 (25):** `BabyBumps-1v3ubts`, `BabyBumps-1v49obz`, `BabyBumps-1v4ggjn`, `BabyBumps-1v53urs`, `BabyBumps-1v5dw3c`, `BabyBumps-1v5tnv3`, `NewParents-1v33b8t`, `PregnancyUK-1v50k0t`, `PregnancyUK-1v5chga`, `beyondthebump-1v53w2q`, `pregnant-1v3en85`, `pregnant-1v3enrr`, `pregnant-1v3pkh6`, `pregnant-1v3ua0u`, `pregnant-1v3x5kl`, `pregnant-1v3z7yf`, `pregnant-1v42u1h`, `pregnant-1v499ng`, `pregnant-1v4m46h`, `pregnant-1v4oc4v`, `pregnant-1v4s2na`, `pregnant-1v4tcbh`, `pregnant-1v5ap8c`, `pregnant-1v5fn89`, `pregnant-1v5w6dj`.

**PR37 (26):** `BabyBumps-1v6kjo4`, `BabyBumps-1v82c4s`, `BabyBumps-1v89y53`, `BabyBumps-1v8d219`, `BabyBumps-1v8im7y`, `BabyBumps-1v8pldy`, `NewParents-1v6meuc`, `PregnancyUK-1v72avf`, `pregnant-1v632ht`, `pregnant-1v6oqkv`, `pregnant-1v6ovm8`, `pregnant-1v6z3hr`, `pregnant-1v73khm`, `pregnant-1v77s6a`, `pregnant-1v7coz0`, `pregnant-1v7q4jl`, `pregnant-1v7qoza`, `pregnant-1v86eyy`, `pregnant-1v86ns8`, `pregnant-1v8i5p4`, `pregnant-1v8jygl`, `pregnant-1v8m545`, `pregnant-1v8pkc4`, `pregnant-1v8q54e`, `pregnant-1v8y0z8`, `pregnant-1v92fx6`.

**PR38 (33):** `BabyBumps-1va71i7`, `BabyBumps-1vba67r`, `BabyBumps-1vbgl6u`, `BabyBumps-1vbznny`, `Mommit-1v9evwl`, `Mommit-1valhe4`, `NewParents-1vbugbf`, `NewParents-1vc25m2`, `PregnancyUK-1v9a531`, `PregnancyUK-1v9mkln`, `PregnancyUK-1v9rm9c`, `PregnancyUK-1v9vhzf`, `PregnancyUK-1vb7oaq`, `beyondthebump-1va545w`, `beyondthebump-1va5kp3`, `beyondthebump-1vb4wl8`, `pregnant-1v9jylc`, `pregnant-1va7uk5`, `pregnant-1vacolq`, `pregnant-1vaekuk`, `pregnant-1vaf1ho`, `pregnant-1vafnuz`, `pregnant-1vafo4k`, `pregnant-1vagjin`, `pregnant-1vak2w8`, `pregnant-1vb2noi`, `pregnant-1vb344t`, `pregnant-1vb6oqg`, `pregnant-1vb7ovh`, `pregnant-1vb9ze6`, `pregnant-1vbdn6i`, `pregnant-1vbi7qc`, `pregnant-1vbr89q`.

**PR39 (35):** `BabyBumps-1vdhd55`, `BabyBumps-1versy7`, `Mommit-1veinqs`, `Mommit-1vej7a2`, `NewParents-1vcgrrg`, `NewParents-1vdcy8q`, `PregnancyUK-1vcsmrd`, `PregnancyUK-1vdlq6i`, `PregnancyUK-1ve6w8d`, `PregnancyUK-1vekkqh`, `beyondthebump-1vdhk8l`, `beyondthebump-1vfevxq`, `pregnant-1vca8sy`, `pregnant-1vcagqv`, `pregnant-1vcetmn`, `pregnant-1vco9z1`, `pregnant-1vd1rs2`, `pregnant-1vd29di`, `pregnant-1vd866d`, `pregnant-1vd8pf1`, `pregnant-1vdvhci`, `pregnant-1vdyzdo`, `pregnant-1vdzhdp`, `pregnant-1vdzr4l`, `pregnant-1ve2jq5`, `pregnant-1ve3vp7`, `pregnant-1ve4j9i`, `pregnant-1ve9jki`, `pregnant-1veawvy`, `pregnant-1vehio6`, `pregnant-1venyss`, `pregnant-1veyrfp`, `pregnant-1vf43mx`, `pregnant-1vf6m94`, `pregnant-1vfg74l`.

**PR40 (35):** `BabyBumps-1vgthw7`, `BabyBumps-1viii9o`, `FirstTimeMom-1vhhmre`, `NewParents-1vg6f8b`, `PregnancyUK-1vgf90n`, `PregnancyUK-1vh1xyc`, `PregnancyUK-1vic9jp`, `beyondthebump-1vhrsi3`, `beyondthebump-1vhuio7`, `pregnant-1vfhx0d`, `pregnant-1vfjx1f`, `pregnant-1vflswe`, `pregnant-1vfw05v`, `pregnant-1vfzf7i`, `pregnant-1vgggf9`, `pregnant-1vgn50r`, `pregnant-1vgoxdq`, `pregnant-1vgsoqu`, `pregnant-1vgx6yz`, `pregnant-1vh1qrr`, `pregnant-1vh5vhr`, `pregnant-1vhb03i`, `pregnant-1vhc8h0`, `pregnant-1vhcz9d`, `pregnant-1vhefdj`, `pregnant-1vhher5`, `pregnant-1vhip4s`, `pregnant-1vhlyio`, `pregnant-1vhmzvt`, `pregnant-1vhpbp7`, `pregnant-1vi1vtd`, `pregnant-1vidni8`, `pregnant-1viic48`, `pregnant-1vijv0i`, `pregnant-1vik2de`.

**PR41 (24):** `BabyBumps-1vjet55`, `Mommit-1vko4ne`, `Mommit-1vkonq4`, `NewParents-1vj5t4l`, `NewParents-1vksfd0`, `beyondthebump-1vj0w67`, `beyondthebump-1vj1xeu`, `beyondthebump-1vj5bvm`, `beyondthebump-1vkp2v9`, `beyondthebumpUK-1vld76k`, `beyondthebumpUK-1vldqgg`, `pregnant-1vj0k7g`, `pregnant-1vjc1lr`, `pregnant-1vjcwql`, `pregnant-1vjehxe`, `pregnant-1vjetja`, `pregnant-1vk3inr`, `pregnant-1vkfm1c`, `pregnant-1vkk5bd`, `pregnant-1vkrqg7`, `pregnant-1vkuoue`, `pregnant-1vl044t`, `pregnant-1vl3til`, `pregnant-1vllbg1`.

**PR42 (34):** `Mommit-1vltryj`, `Mommit-1vntzx5`, `NewParents-1vmylcs`, `PregnancyUK-1vmi9sx`, `PregnancyUK-1vmto0p`, `beyondthebump-1vny1kd`, `beyondthebump-1vo7cuy`, `beyondthebump-1vooc96`, `beyondthebump-1voov23`, `pregnant-1vlsokr`, `pregnant-1vlvx4i`, `pregnant-1vlw69s`, `pregnant-1vmcmh5`, `pregnant-1vmipyh`, `pregnant-1vmp517`, `pregnant-1vmr7jd`, `pregnant-1vmsu95`, `pregnant-1vmt1tr`, `pregnant-1vmvzdt`, `pregnant-1vn1soj`, `pregnant-1vn3wk4`, `pregnant-1vn9rf1`, `pregnant-1vnagz9`, `pregnant-1vnczh5`, `pregnant-1vnfuix`, `pregnant-1vngwn9`, `pregnant-1vnqxi7`, `pregnant-1vo87l0`, `pregnant-1vodfml`, `pregnant-1vofkf6`, `pregnant-1vojojj`, `pregnant-1voo2o6`, `pregnant-1vooyr1`, `pregnant-1vosv6c`.

**PR43 (23):** `BabyBumps-1vp3vc1`, `PregnancyUK-1voweiq`, `beyondthebump-1vowtz5`, `beyondthebump-1vpm0f8`, `beyondthebump-1vr8yuj`, `beyondthebumpUK-1vqq0gw`, `pregnant-1vp3wfa`, `pregnant-1vp5r5q`, `pregnant-1vp6550`, `pregnant-1vp80v0`, `pregnant-1vp8llf`, `pregnant-1vpag58`, `pregnant-1vpbl1y`, `pregnant-1vpnrt5`, `pregnant-1vpt5b7`, `pregnant-1vqc4tz`, `pregnant-1vqq0vt`, `pregnant-1vqwcnj`, `pregnant-1vqyblj`, `pregnant-1vr547j`, `pregnant-1vr8bl1`, `pregnant-1vroop0`, `pregnant-1vrvm4w`.

**PR44 (29):** `BabyBumps-1vs9vc2`, `BabyBumps-1vslwpc`, `BabyBumps-1vsnmhi`, `BabyBumps-1vthpsn`, `Mommit-1vs8797`, `Mommit-1vti3hv`, `NewParents-1vs5ct2`, `NewParents-1vscv2i`, `NewParents-1vsyjry`, `beyondthebump-1vsapmg`, `beyondthebump-1vsl6i1`, `beyondthebumpUK-1vtkt4h`, `pregnant-1vrzsps`, `pregnant-1vs4aqx`, `pregnant-1vsg96t`, `pregnant-1vsiupw`, `pregnant-1vso0tg`, `pregnant-1vsro0k`, `pregnant-1vsw4gg`, `pregnant-1vt0rjm`, `pregnant-1vt5963`, `pregnant-1vt6g64`, `pregnant-1vta6gx`, `pregnant-1vtlwfg`, `pregnant-1vu15od`, `pregnant-1vu3gts`, `pregnant-1vu7a8q`, `pregnant-1vudd6x`, `pregnant-1vugk5m`.

**PR45 (29):** `BabyBumps-1vupfib`, `BabyBumps-1vv0xxe`, `BabyBumps-1vvcdxp`, `BabyBumps-1vvxucp`, `PregnancyUK-1vvgfb5`, `beyondthebump-1vw48g0`, `beyondthebumpUK-1vvqj9c`, `pregnant-1vumm03`, `pregnant-1vuqdo8`, `pregnant-1vv14to`, `pregnant-1vv4fs2`, `pregnant-1vv8mho`, `pregnant-1vv9auy`, `pregnant-1vvc9wr`, `pregnant-1vvqxys`, `pregnant-1vw3fly`, `pregnant-1vw7j5w`, `pregnant-1vwh2gp`, `pregnant-1vwjssw`, `pregnant-1vwkuz1`, `pregnant-1vwo15p`, `pregnant-1vwoz3k`, `pregnant-1vwsxhl`, `pregnant-1vwvc67`, `pregnant-1vx5wmp`, `pregnant-1vx8nlo`, `pregnant-1vxg93o`, `pregnant-1vxifox`, `pregnant-1vxjfx5`.

#### Wave 3

**PR46 (17):** `BabyBumps-1sb13yh`, `BabyBumps-1slwor5`, `BabyBumps-1t2ib0b`, `Doulas-1svavdo`, `PregnancyUK-1sjh9zj`, `PregnancyUK-1srjc1r`, `beyondthebumpUK-1srugwf`, `beyondthebumpUK-1syzpj5`, `beyondthebumpUK-1t06rzy`, `pregnant-1so4lzj`, `pregnant-1spty1l`, `pregnant-1sq58eh`, `pregnant-1sqwd6j`, `pregnant-1srn04r`, `pregnant-1stg7mz`, `pregnant-1svpdnv`, `pregnant-1t14wcv`.

**PR47 (11):** `BabyBumps-1th0dxm`, `BabyBumps-1thn0gz`, `BabyBumps-1tjwsmj`, `BabyBumps-1tlfh6k`, `NewParents-1tmcn8g`, `pregnant-1t30fxz`, `pregnant-1te7n3i`, `pregnant-1tnbwfc`, `pregnant-1tr3los`, `pregnant-1tr9pa1`, `pregnant-1tskv7d`.

**PR48 (20):** `BabyBumps-1sgax4e`, `BabyBumps-1u5j0kc`, `BabyBumps-1u6tbjy`, `NewParents-1sbfbmf`, `NewParents-1tyycp1`, `PregnancyUK-1s96iqs`, `PregnancyUK-1sbnb91`, `PregnancyUK-1sgzpa5`, `PregnancyUK-1t348hr`, `beyondthebump-1spgoe2`, `pregnant-1sav8by`, `pregnant-1semlne`, `pregnant-1skujg5`, `pregnant-1srtx1r`, `pregnant-1svixtm`, `pregnant-1t0ix95`, `pregnant-1t0sps9`, `pregnant-1t14m5x`, `pregnant-1tw0eok`, `pregnant-1uesvdg`.

**PR49 (27):** `BabyBumps-1sebowu`, `BabyBumps-1t4zsss`, `BabyBumps-1tjqkyz`, `BabyBumps-1tstx1q`, `BabyBumps-1tuf20m`, `BabyBumps-1u630m4`, `BabyBumps-1u78ea9`, `Mommit-1sgm7pu`, `NewParents-1u34wur`, `PregnancyUK-1tsueia`, `PregnancyUK-1tycgqp`, `beyondthebump-1t9r75q`, `daddit-1trvntz`, `pregnant-1sexhfn`, `pregnant-1sgt1cg`, `pregnant-1shcpa7`, `pregnant-1shj939`, `pregnant-1tcxi0s`, `pregnant-1td1lci`, `pregnant-1tgp0hc`, `pregnant-1ti1jjq`, `pregnant-1tuvly0`, `pregnant-1tvw795`, `pregnant-1twm3sn`, `pregnant-1u8xf9s`, `pregnant-1ubnxaq`, `pregnant-1ubzkck`.

**PR50 (26):** `BabyBumps-1sjrtfx`, `BabyBumps-1sraqoj`, `BabyBumps-1t2dr0w`, `BabyBumps-1t3axma`, `BabyBumps-1t3fk9o`, `NewParents-1t7dz3h`, `NewParents-1tg2972`, `beyondthebump-1sq08j3`, `beyondthebump-1swr3ld`, `beyondthebumpUK-1siwu4s`, `daddit-1sr39yr`, `daddit-1szye0r`, `daddit-1tdkd3k`, `daddit-1tfmdzy`, `daddit-1tfvmas`, `daddit-1tg2qiw`, `pregnant-1si7u6c`, `pregnant-1siyt40`, `pregnant-1sjs2wv`, `pregnant-1smdqju`, `pregnant-1snbvbe`, `pregnant-1sqiftj`, `pregnant-1sxygyp`, `pregnant-1t2irza`, `pregnant-1t3uqpi`, `pregnant-1tdxxkn`.

**PR51 (20):** `BabyBumps-1s9gpxe`, `BabyBumps-1tkwchk`, `Mommit-1udfcwe`, `NewParents-1tmrx41`, `beyondthebump-1tolva4`, `daddit-1tylc3k`, `daddit-1u4q783`, `pregnant-1s94z3j`, `pregnant-1s9orqw`, `pregnant-1tips68`, `pregnant-1tivtkc`, `pregnant-1tkwuoe`, `pregnant-1tmjiij`, `pregnant-1tqm5vp`, `pregnant-1ts6s5c`, `pregnant-1u211up`, `pregnant-1u2ev17`, `pregnant-1u2ury2`, `pregnant-1u4k4bg`, `pregnant-1ubu5d3`.

**PR52 (65):** `BabyBumps-1s9pflu`, `BabyBumps-1sa10h9`, `BabyBumps-1sabmmm`, `BabyBumps-1sbev1i`, `BabyBumps-1sbg169`, `BabyBumps-1sc1wgk`, `BabyBumps-1scd1ne`, `BabyBumps-1scldwx`, `BabyBumps-1scltco`, `BabyBumps-1scohcg`, `BabyBumps-1scugn4`, `Mommit-1sahe10`, `NewParents-1s9xnpp`, `NewParents-1sa5lyc`, `NewParents-1scxfq4`, `PregnancyUK-1s9r0hh`, `PregnancyUK-1s9vu1a`, `PregnancyUK-1savhlz`, `PregnancyUK-1sckbs6`, `PregnancyUK-1scwqhi`, `PregnancyUK-1sd0pn6`, `PregnancyUK-1sd6u6e`, `PregnancyUK-1sde5yo`, `PregnancyUK-1sdid1x`, `beyondthebump-1sa1wzo`, `beyondthebump-1sb28lc`, `beyondthebump-1sbm3oq`, `beyondthebump-1sbw8v6`, `beyondthebump-1scwwc4`, `beyondthebumpUK-1sa83vn`, `beyondthebumpUK-1sc7r3e`, `pregnant-1s9pgox`, `pregnant-1s9sj02`, `pregnant-1s9tqxx`, `pregnant-1s9vdwf`, `pregnant-1sa14ba`, `pregnant-1sa41aw`, `pregnant-1sa4saj`, `pregnant-1sa7j9j`, `pregnant-1sabqn9`, `pregnant-1saizyo`, `pregnant-1saj5gy`, `pregnant-1sal4p0`, `pregnant-1san1x6`, `pregnant-1sapy3g`, `pregnant-1sarhal`, `pregnant-1sat503`, `pregnant-1satjgf`, `pregnant-1sb22zf`, `pregnant-1sb2gmw`, `pregnant-1sbcdbr`, `pregnant-1sbdpns`, `pregnant-1sbgsm7`, `pregnant-1sbtuaj`, `pregnant-1sbwzr2`, `pregnant-1scekgf`, `pregnant-1sceuj4`, `pregnant-1scmssl`, `pregnant-1sd6zd6`, `pregnant-1sd9geo`, `pregnant-1sde6vd`, `pregnant-1sde7r0`, `pregnant-1sdieux`, `pregnant-1sdjsow`, `pregnant-1sdjz7b`.

**PR53 (30):** `BabyBumps-1sdm673`, `BabyBumps-1sebrhf`, `BabyBumps-1sev922`, `BabyBumps-1sg11a1`, `BabyBumps-1sg2gm0`, `Mommit-1sgf6db`, `PregnancyUK-1sf1pgf`, `PregnancyUK-1sgqkxu`, `beyondthebump-1sehia6`, `beyondthebump-1send92`, `beyondthebumpUK-1sgo2of`, `pregnant-1sdkm89`, `pregnant-1sehsdr`, `pregnant-1sejzs6`, `pregnant-1semmz8`, `pregnant-1seoiaz`, `pregnant-1seoifn`, `pregnant-1sf9zbu`, `pregnant-1sffd3m`, `pregnant-1sffx3s`, `pregnant-1sfj52g`, `pregnant-1sfjesq`, `pregnant-1sfm4dx`, `pregnant-1sfy5gr`, `pregnant-1sgbq0f`, `pregnant-1sgemei`, `pregnant-1sgfxva`, `pregnant-1sgm442`, `pregnant-1sgrrto`, `pregnant-1sgtaga`.

**PR54 (42):** `BabyBumps-1shdudc`, `BabyBumps-1shq9c5`, `BabyBumps-1si7i6c`, `BabyBumps-1sk51a0`, `Mommit-1sim5x4`, `PregnancyUK-1shgm9w`, `PregnancyUK-1shu2c8`, `PregnancyUK-1ske2p4`, `beyondthebump-1shv5cb`, `beyondthebump-1sim8ag`, `beyondthebump-1sjsdk0`, `pregnant-1sgz69b`, `pregnant-1sgzkt6`, `pregnant-1sh110y`, `pregnant-1sh65uh`, `pregnant-1shc6rg`, `pregnant-1shjocs`, `pregnant-1shk6pa`, `pregnant-1shpsrt`, `pregnant-1shv8q5`, `pregnant-1si4b2o`, `pregnant-1sifsdf`, `pregnant-1sigj99`, `pregnant-1sijy7x`, `pregnant-1sirir0`, `pregnant-1sixtvh`, `pregnant-1sizpzk`, `pregnant-1sj0sdm`, `pregnant-1sj5ohx`, `pregnant-1sj7q4w`, `pregnant-1sje2ak`, `pregnant-1sjn18v`, `pregnant-1sjnvyb`, `pregnant-1sjtlad`, `pregnant-1sjtm6k`, `pregnant-1sjuia7`, `pregnant-1sjum0i`, `pregnant-1sjyqvk`, `pregnant-1sk2ih2`, `pregnant-1sk4uup`, `pregnant-1skhky4`, `pregnant-1skjzk9`.

**PR55 (43):** `BabyBumps-1skrijm`, `BabyBumps-1sl8b01`, `BabyBumps-1slnlnw`, `BabyBumps-1slzuhs`, `BabyBumps-1snfgfm`, `BabyBumps-1snhz2k`, `NewParents-1smkyav`, `PregnancyUK-1slnjos`, `PregnancyUK-1sm9ara`, `PregnancyUK-1smf37e`, `PregnancyUK-1smz5af`, `PregnancyUK-1snb4q3`, `beyondthebump-1slbfwl`, `beyondthebumpUK-1so8spi`, `pregnant-1skt4xm`, `pregnant-1skviq6`, `pregnant-1sl2qnj`, `pregnant-1sl9qb1`, `pregnant-1slbnxz`, `pregnant-1slg918`, `pregnant-1slnizm`, `pregnant-1slp3q8`, `pregnant-1slpts2`, `pregnant-1slrwfu`, `pregnant-1slvbdq`, `pregnant-1slxcsr`, `pregnant-1sm7ixb`, `pregnant-1smcyn3`, `pregnant-1smf483`, `pregnant-1smgftq`, `pregnant-1smhb0m`, `pregnant-1smp1ld`, `pregnant-1smrsgz`, `pregnant-1smuwy8`, `pregnant-1smz5y5`, `pregnant-1sn65im`, `pregnant-1snfmol`, `pregnant-1sngzd5`, `pregnant-1sno01r`, `pregnant-1snpdax`, `pregnant-1snppm4`, `pregnant-1so2ddd`, `pregnant-1so7ni0`.

**PR56 (20):** `BabyBumps-1sq9pnh`, `BabyBumps-1sqa8xr`, `BabyBumps-1sqsirh`, `BabyBumps-1sqw14r`, `BabyBumps-1srrheb`, `Mommit-1sokp03`, `NewParents-1spfr3t`, `NewParents-1spyl8g`, `NewParents-1sqjzhz`, `beyondthebumpUK-1sp1azf`, `pregnant-1sprkd8`, `pregnant-1sq2zhb`, `pregnant-1sqh7yu`, `pregnant-1sqjzzg`, `pregnant-1sqsxw0`, `pregnant-1srm481`, `pregnant-1srrt8c`, `pregnant-1ss2zas`, `pregnant-1ss5jl0`, `pregnant-1ssb1cp`.

**PR57 (53):** `BabyBumps-1ssi0k5`, `BabyBumps-1ssttw8`, `BabyBumps-1sugfqe`, `BabyBumps-1sv7ekt`, `BabyBumps-1sv7t3u`, `Mommit-1ssgl7j`, `Mommit-1suzvyv`, `NewParents-1st5d2v`, `PregnancyUK-1ssyhro`, `PregnancyUK-1suovfv`, `beyondthebump-1sskm6p`, `beyondthebumpUK-1su9jo5`, `beyondthebumpUK-1sufmyu`, `pregnant-1ssc56v`, `pregnant-1ssp1vw`, `pregnant-1ssq82g`, `pregnant-1ssqxkl`, `pregnant-1ssrpzy`, `pregnant-1ssubkz`, `pregnant-1ssundx`, `pregnant-1ssz6l3`, `pregnant-1st2c7g`, `pregnant-1st5fg0`, `pregnant-1st71hs`, `pregnant-1stf09x`, `pregnant-1stf95a`, `pregnant-1stgk9h`, `pregnant-1stkdd8`, `pregnant-1stkeu7`, `pregnant-1stl575`, `pregnant-1stsgri`, `pregnant-1stu837`, `pregnant-1stuj3m`, `pregnant-1su0mde`, `pregnant-1su28se`, `pregnant-1su4khv`, `pregnant-1sua75c`, `pregnant-1suf1vk`, `pregnant-1suffaf`, `pregnant-1suggpc`, `pregnant-1suh22q`, `pregnant-1suiy2i`, `pregnant-1sujaba`, `pregnant-1suki0j`, `pregnant-1supopk`, `pregnant-1sutae8`, `pregnant-1suwotc`, `pregnant-1sv4zol`, `pregnant-1sve0gf`, `pregnant-1svfryu`, `pregnant-1svgbvg`, `pregnant-1svnbtv`, `pregnant-1svrww1`.

**PR58 (32):** `BabyBumps-1sy4t6a`, `BabyBumps-1syorp2`, `BabyBumps-1syzeeq`, `BabyBumps-1syzpd9`, `PregnancyUK-1syvnyr`, `beyondthebump-1swern8`, `beyondthebump-1sxbhmz`, `beyondthebump-1sxhj2r`, `beyondthebump-1sxv3ts`, `pregnant-1svscsg`, `pregnant-1svsxbi`, `pregnant-1svuon8`, `pregnant-1sw4oci`, `pregnant-1swbqge`, `pregnant-1swfvf8`, `pregnant-1swlnmh`, `pregnant-1swqoj8`, `pregnant-1swt370`, `pregnant-1swtrj4`, `pregnant-1swv164`, `pregnant-1swx5l3`, `pregnant-1sx4jfv`, `pregnant-1sx7i8r`, `pregnant-1sxjpub`, `pregnant-1sxqwxi`, `pregnant-1sy2a5b`, `pregnant-1sy3x5d`, `pregnant-1sy6s9v`, `pregnant-1sy90pd`, `pregnant-1syanur`, `pregnant-1syh6sh`, `pregnant-1syl9kv`.

**PR59 (23):** `BabyBumps-1szi4si`, `BabyBumps-1t0ex7v`, `BabyBumps-1t1361y`, `BabyBumps-1t1bkn1`, `PregnancyUK-1t0cxev`, `beyondthebump-1t01bfz`, `beyondthebump-1t1524k`, `pregnant-1sz7m5c`, `pregnant-1sz85vx`, `pregnant-1szazbg`, `pregnant-1szh7w4`, `pregnant-1szkq58`, `pregnant-1szvidm`, `pregnant-1t012ft`, `pregnant-1t06t6h`, `pregnant-1t0e5xy`, `pregnant-1t0ezcr`, `pregnant-1t0gfqz`, `pregnant-1t186m6`, `pregnant-1t1b24k`, `pregnant-1t1lm0b`, `pregnant-1t204c9`, `pregnant-1t23j1w`.

**PR60 (54):** `BabyBumps-1t26482`, `BabyBumps-1t2vw1y`, `BabyBumps-1t2xsrx`, `BabyBumps-1t33w38`, `BabyBumps-1t3j1gw`, `BabyBumps-1t3trby`, `BabyBumps-1t3yqd6`, `BabyBumps-1t40r4v`, `BabyBumps-1t42v61`, `BabyBumps-1t4hl9t`, `BabyBumps-1t4inrd`, `BabyBumps-1t4je3k`, `BabyBumps-1t4jw4d`, `BabyBumps-1t4ziyy`, `FirstTimeMom-1t29hva`, `FirstTimeMom-1t2r2wx`, `Mommit-1t3z3hb`, `PregnancyUK-1t2423u`, `PregnancyUK-1t29h1w`, `PregnancyUK-1t3l0bz`, `PregnancyUK-1t4nv3t`, `beyondthebump-1t3c4y3`, `pregnant-1t29fut`, `pregnant-1t2air3`, `pregnant-1t2dhc4`, `pregnant-1t2gzbp`, `pregnant-1t2ia8n`, `pregnant-1t2j671`, `pregnant-1t2kvlw`, `pregnant-1t2lb5j`, `pregnant-1t2yb4f`, `pregnant-1t32txt`, `pregnant-1t388cj`, `pregnant-1t3b8hj`, `pregnant-1t3bsmy`, `pregnant-1t3h0av`, `pregnant-1t410vo`, `pregnant-1t4f3z7`, `pregnant-1t4jzda`, `pregnant-1t4m3vb`, `pregnant-1t4r6c1`, `pregnant-1t4rykf`, `pregnant-1t4snrm`, `pregnant-1t4ucgm`, `pregnant-1t4w6o8`, `pregnant-1t4wy8n`, `pregnant-1t4xmla`, `pregnant-1t4xuh1`, `pregnant-1t4zyto`, `pregnant-1t4zyyo`, `pregnant-1t50esd`, `pregnant-1t51g6f`, `pregnant-1t53713`, `pregnant-1t542oq`.

**PR61 (30):** `BabyBumps-1t55vfv`, `BabyBumps-1t5qiwb`, `BabyBumps-1t5w4zc`, `BabyBumps-1t6rzob`, `BabyBumps-1t76111`, `BabyBumps-1t7b57y`, `BabyBumps-1t8fh6h`, `BabyBumps-1t8h3ec`, `BabyBumps-1t9b7br`, `BabyBumps-1t9i8rw`, `Mommit-1t7lljf`, `beyondthebump-1t65fdo`, `beyondthebump-1t7m731`, `beyondthebump-1t7ucyg`, `pregnant-1t5ijd0`, `pregnant-1t5mzqa`, `pregnant-1t5svq0`, `pregnant-1t6fgbo`, `pregnant-1t6tkt0`, `pregnant-1t75g4g`, `pregnant-1t78c4c`, `pregnant-1t7e2fu`, `pregnant-1t7t2u8`, `pregnant-1t7vvwh`, `pregnant-1t7wo3o`, `pregnant-1t88lp0`, `pregnant-1t8o08a`, `pregnant-1t8oyah`, `pregnant-1t95dhm`, `pregnant-1t9i0ut`.

**PR62 (36):** `BabyBumps-1taqv5y`, `BabyBumps-1tb3dfd`, `BabyBumps-1tc0oot`, `BabyBumps-1tc4ix5`, `BabyBumps-1tch30k`, `Mommit-1tbxjwe`, `Mommit-1tc70tu`, `NewParents-1t9yyd1`, `NewParents-1tafyc4`, `NewParents-1tajk04`, `PregnancyUK-1tab4wg`, `PregnancyUK-1taicjh`, `PregnancyUK-1tazih7`, `PregnancyUK-1tcb7y1`, `PregnancyUK-1tcbztx`, `beyondthebump-1taaqz6`, `beyondthebump-1tasxh7`, `beyondthebump-1tbazj7`, `beyondthebump-1tc09i4`, `pregnant-1t9uyjo`, `pregnant-1ta580d`, `pregnant-1ta6hk9`, `pregnant-1taaxwe`, `pregnant-1tb3k4i`, `pregnant-1tb6dv7`, `pregnant-1tbby1a`, `pregnant-1tbho8b`, `pregnant-1tbpmq7`, `pregnant-1tbsfjq`, `pregnant-1tbwcux`, `pregnant-1tc48b4`, `pregnant-1tcatgp`, `pregnant-1tcbd44`, `pregnant-1tcezwf`, `pregnant-1tcjbw5`, `pregnant-1tcudic`.

**PR63 (50):** `BabyBumps-1td8qjo`, `BabyBumps-1tdzzqu`, `BabyBumps-1telyjj`, `BabyBumps-1tepmn7`, `BabyBumps-1tew6vg`, `BabyBumps-1tezp0p`, `BabyBumps-1tfacvi`, `BabyBumps-1tfaz6t`, `BabyBumps-1tfq8ff`, `BabyBumps-1tfy73n`, `BabyBumps-1tg55vh`, `Mommit-1tfxdlp`, `NewParents-1tdepb7`, `PregnancyUK-1te7j0o`, `PregnancyUK-1teqczw`, `PregnancyUK-1tggwte`, `beyondthebump-1tf4qhj`, `beyondthebump-1tfgi8u`, `beyondthebumpUK-1teqzmt`, `pregnant-1tdg2f8`, `pregnant-1tdoc9y`, `pregnant-1tdshsi`, `pregnant-1tdvg3b`, `pregnant-1tdxgd9`, `pregnant-1teavuk`, `pregnant-1tecmdt`, `pregnant-1teewm0`, `pregnant-1tefgdf`, `pregnant-1teisuy`, `pregnant-1tepy47`, `pregnant-1texlut`, `pregnant-1tezm1i`, `pregnant-1tf0mgj`, `pregnant-1tf0uqo`, `pregnant-1tf4p8e`, `pregnant-1tf9q6o`, `pregnant-1tfie3k`, `pregnant-1tfn2f2`, `pregnant-1tfp3wp`, `pregnant-1tfqxx1`, `pregnant-1tfxdu1`, `pregnant-1tg30ua`, `pregnant-1tg4110`, `pregnant-1tg6ozg`, `pregnant-1tg7tuk`, `pregnant-1tgf47t`, `pregnant-1tgj8eu`, `pregnant-1tgkezu`, `pregnant-1tgmox3`, `pregnant-1tgp16o`.

**PR64 (27):** `BabyBumps-1ti64cu`, `BabyBumps-1tir0pv`, `BabyBumps-1tivds3`, `BabyBumps-1tj1bbx`, `PregnancyUK-1tjlwzh`, `beyondthebumpUK-1tidrts`, `pregnant-1thal00`, `pregnant-1thiftr`, `pregnant-1thnsix`, `pregnant-1thp2dw`, `pregnant-1ti64t5`, `pregnant-1ti9ey4`, `pregnant-1ti9s59`, `pregnant-1tim33b`, `pregnant-1tin6ep`, `pregnant-1titau4`, `pregnant-1tiyr9k`, `pregnant-1tj1uev`, `pregnant-1tjbohz`, `pregnant-1tjutin`, `pregnant-1tjwziz`, `pregnant-1tjxcpe`, `pregnant-1tk883t`, `pregnant-1tkgm7z`, `pregnant-1tkik0q`, `pregnant-1tknfh1`, `pregnant-1tktdfu`.

**PR65 (24):** `BabyBumps-1tmrdwa`, `BabyBumps-1tnn92l`, `BabyBumps-1tnuqlu`, `BabyBumps-1tof65m`, `BabyBumps-1tp5dq3`, `Mommit-1to84pn`, `NewParents-1tm6p2q`, `beyondthebump-1tlwhfx`, `beyondthebump-1tmppwq`, `beyondthebump-1to6kkg`, `beyondthebumpUK-1tmz9pb`, `beyondthebumpUK-1tozism`, `beyondthebumpUK-1tozvts`, `pregnant-1tl3znj`, `pregnant-1tlbg7e`, `pregnant-1tlm953`, `pregnant-1tlvyyf`, `pregnant-1tm6x8r`, `pregnant-1tmjlx2`, `pregnant-1tn8uto`, `pregnant-1tnle5c`, `pregnant-1tns9l7`, `pregnant-1tof8ra`, `pregnant-1totigk`.

**PR66 (44):** `BabyBumps-1tpnafa`, `BabyBumps-1tpveks`, `BabyBumps-1tq8ldf`, `BabyBumps-1tqhxae`, `BabyBumps-1tqkpjk`, `BabyBumps-1tqp56f`, `BabyBumps-1trar7l`, `BabyBumps-1trvg1z`, `BabyBumps-1tsamt5`, `FirstTimeMom-1tqmf16`, `FirstTimeMom-1trxihy`, `PregnancyUK-1tq30ns`, `PregnancyUK-1trhb0j`, `PregnancyUK-1trxkql`, `PregnancyUK-1trzsrp`, `beyondthebump-1tqdv9y`, `pregnant-1tpf3ar`, `pregnant-1tphwvq`, `pregnant-1tpkly7`, `pregnant-1tplwi7`, `pregnant-1tpnhhh`, `pregnant-1tpr75l`, `pregnant-1tpry69`, `pregnant-1tq205z`, `pregnant-1tq2nl2`, `pregnant-1tqd8jr`, `pregnant-1tqkggq`, `pregnant-1tqmxsu`, `pregnant-1tqn13i`, `pregnant-1tqr1mx`, `pregnant-1tquw3e`, `pregnant-1tqwq7s`, `pregnant-1tqz8qo`, `pregnant-1tr3t2m`, `pregnant-1tr3vbv`, `pregnant-1trbove`, `pregnant-1trf4so`, `pregnant-1trm7wp`, `pregnant-1trnzfs`, `pregnant-1trs50d`, `pregnant-1trxh1h`, `pregnant-1ts1ihj`, `pregnant-1ts94px`, `pregnant-1tsdsas`.

**PR67 (48):** `BabyBumps-1tsk1jt`, `BabyBumps-1tsut8p`, `BabyBumps-1ttge3q`, `BabyBumps-1tu11jr`, `BabyBumps-1tu5dgn`, `BabyBumps-1tumu7e`, `BabyBumps-1tv93js`, `FirstTimeMom-1tucf76`, `NewParents-1tsj2su`, `PregnancyUK-1tsxmle`, `PregnancyUK-1tt34uz`, `PregnancyUK-1tu9j0f`, `PregnancyUK-1tuvkr6`, `PregnancyUK-1tv0wrz`, `PregnancyUK-1tv1zi5`, `PregnancyUK-1tv2o0v`, `PregnancyUK-1tvmeoc`, `beyondthebump-1tsjpbs`, `beyondthebump-1tsonr4`, `pregnant-1tsikzf`, `pregnant-1tsl1fx`, `pregnant-1tslsve`, `pregnant-1tso3vk`, `pregnant-1tstj1o`, `pregnant-1tstnq3`, `pregnant-1tsxm4z`, `pregnant-1tsyjpb`, `pregnant-1tsyynb`, `pregnant-1tt5nap`, `pregnant-1ttdwwi`, `pregnant-1ttgctc`, `pregnant-1tthdzu`, `pregnant-1ttk0jk`, `pregnant-1ttmnw1`, `pregnant-1ttmr2j`, `pregnant-1tu80fe`, `pregnant-1tu9vq5`, `pregnant-1tut0nm`, `pregnant-1tuy6kc`, `pregnant-1tv4agf`, `pregnant-1tv507u`, `pregnant-1tv6shw`, `pregnant-1tv7vcj`, `pregnant-1tv9ajz`, `pregnant-1tv9pse`, `pregnant-1tvcfvt`, `pregnant-1tvonok`, `pregnant-1tvsdve`.

**PR68 (52):** `BabyBumps-1tvymhu`, `BabyBumps-1tw090z`, `BabyBumps-1tz716y`, `BabyBumps-1tzcr4x`, `FirstTimeMom-1typf3p`, `PregnancyUK-1txhok1`, `PregnancyUK-1tykaja`, `PregnancyUK-1tzhrl9`, `beyondthebump-1tvyuzn`, `beyondthebump-1tw8x4d`, `beyondthebump-1txlavp`, `beyondthebump-1txr7ln`, `beyondthebump-1txzpn0`, `beyondthebump-1ty9a71`, `pregnant-1tw024p`, `pregnant-1tw5tt3`, `pregnant-1tw8e5n`, `pregnant-1tw9am8`, `pregnant-1twceko`, `pregnant-1twdlvw`, `pregnant-1tweliv`, `pregnant-1twjrjr`, `pregnant-1twrnlj`, `pregnant-1twu7aw`, `pregnant-1twzlpi`, `pregnant-1tx346v`, `pregnant-1tx4202`, `pregnant-1tx4i37`, `pregnant-1tx6iad`, `pregnant-1tx7wg7`, `pregnant-1txglb3`, `pregnant-1txi64z`, `pregnant-1txqt3l`, `pregnant-1txv3g2`, `pregnant-1ty00bv`, `pregnant-1ty0g94`, `pregnant-1ty17gm`, `pregnant-1ty1m5b`, `pregnant-1ty6uxd`, `pregnant-1ty82uu`, `pregnant-1tyckw0`, `pregnant-1tydee0`, `pregnant-1tyfioh`, `pregnant-1tygzm0`, `pregnant-1tylvo0`, `pregnant-1tyxcdl`, `pregnant-1tz0xv5`, `pregnant-1tz3p4w`, `pregnant-1tz44k6`, `pregnant-1tzbxps`, `pregnant-1tzbzul`, `pregnant-1tzdwmg`.

**PR69 (41):** `BabyBumps-1tzpytd`, `BabyBumps-1tzvz5b`, `BabyBumps-1tzxebp`, `BabyBumps-1tzzgke`, `BabyBumps-1u0esjb`, `BabyBumps-1u0gyya`, `BabyBumps-1u0mmzy`, `BabyBumps-1u0ov13`, `BabyBumps-1u0v5mg`, `BabyBumps-1u16jv4`, `BabyBumps-1u1nsop`, `BabyBumps-1u1qbo1`, `FirstTimeMom-1u0pd6x`, `Mommit-1u15brw`, `NewParents-1u0kad3`, `PregnancyUK-1u19zoi`, `PregnancyUK-1u21i0u`, `beyondthebump-1tzxbds`, `beyondthebump-1u0rctj`, `beyondthebump-1u2d103`, `beyondthebumpUK-1u11v2k`, `pregnant-1tzsah2`, `pregnant-1tzt0uc`, `pregnant-1tzumyw`, `pregnant-1tzy9me`, `pregnant-1u06327`, `pregnant-1u09oan`, `pregnant-1u09xqc`, `pregnant-1u0atbm`, `pregnant-1u0beqn`, `pregnant-1u0j8qp`, `pregnant-1u111g5`, `pregnant-1u12zs9`, `pregnant-1u13iux`, `pregnant-1u16ty4`, `pregnant-1u1gusd`, `pregnant-1u1hb2z`, `pregnant-1u1nqsa`, `pregnant-1u1yhk5`, `pregnant-1u2a80r`, `pregnant-1u2g0l6`.

**PR70 (35):** `BabyBumps-1u2juao`, `BabyBumps-1u3tlns`, `BabyBumps-1u4pum6`, `BabyBumps-1u5kcoa`, `BabyBumps-1u5l44f`, `BabyBumps-1u61bbk`, `BabyBumps-1u6g343`, `Mommit-1u2rjn8`, `PregnancyUK-1u2rumq`, `PregnancyUK-1u2uq3o`, `PregnancyUK-1u3ohab`, `PregnancyUK-1u5sx7x`, `beyondthebump-1u6jsv5`, `pregnant-1u2hhtr`, `pregnant-1u2lvk9`, `pregnant-1u2mjop`, `pregnant-1u2mx24`, `pregnant-1u30pkk`, `pregnant-1u31hlw`, `pregnant-1u37k23`, `pregnant-1u3drl9`, `pregnant-1u3wmlx`, `pregnant-1u3zzmy`, `pregnant-1u48cv8`, `pregnant-1u4awtu`, `pregnant-1u4egnn`, `pregnant-1u54so5`, `pregnant-1u5p3q8`, `pregnant-1u5qjwc`, `pregnant-1u5vjat`, `pregnant-1u61wa9`, `pregnant-1u64191`, `pregnant-1u64bi3`, `pregnant-1u6khaw`, `pregnant-1u6lw6i`.

**PR71 (52):** `BabyBumps-1u6v9pz`, `BabyBumps-1u7mp5y`, `BabyBumps-1u7pefa`, `BabyBumps-1u7ujvt`, `BabyBumps-1u7wd0g`, `BabyBumps-1u8j5cl`, `BabyBumps-1u8jr1r`, `BabyBumps-1u9ih9u`, `Mommit-1u716rh`, `NewParents-1u6pl8i`, `NewParents-1u7wznv`, `NewParents-1u9n5dq`, `PregnancyUK-1u78pqs`, `PregnancyUK-1u7eny1`, `PregnancyUK-1u9ekv8`, `beyondthebump-1u7djlz`, `beyondthebump-1u8v9zc`, `beyondthebumpUK-1u7w34p`, `beyondthebumpUK-1u85mtk`, `pregnant-1u6twa1`, `pregnant-1u6uel1`, `pregnant-1u6v8d9`, `pregnant-1u71wu2`, `pregnant-1u73wxl`, `pregnant-1u78488`, `pregnant-1u78nok`, `pregnant-1u7avv4`, `pregnant-1u7f56r`, `pregnant-1u7fr2c`, `pregnant-1u7fs6k`, `pregnant-1u7jg8i`, `pregnant-1u7noxb`, `pregnant-1u7olaz`, `pregnant-1u7rp3t`, `pregnant-1u7xfjm`, `pregnant-1u7y28u`, `pregnant-1u81ztu`, `pregnant-1u8ahrk`, `pregnant-1u8aobl`, `pregnant-1u8b4jm`, `pregnant-1u8ep3g`, `pregnant-1u8n3oh`, `pregnant-1u8u6dq`, `pregnant-1u93d9y`, `pregnant-1u97fng`, `pregnant-1u9a2s9`, `pregnant-1u9ay79`, `pregnant-1u9bjkw`, `pregnant-1u9bxjc`, `pregnant-1u9m4m4`, `pregnant-1u9myxi`, `pregnant-1u9n4vm`.

**PR72 (53):** `BabyBumps-1ubx2q6`, `BabyBumps-1uc95uy`, `BabyBumps-1uc9i77`, `BabyBumps-1ucgkit`, `BabyBumps-1ucpxuf`, `BabyBumps-1ud6764`, `BabyBumps-1ud7gu2`, `BabyBumps-1ueaat2`, `BabyBumps-1uec9bx`, `BabyBumps-1ueibx8`, `BabyBumps-1ueq3gx`, `Mommit-1ub9aem`, `Mommit-1ueksk0`, `PregnancyUK-1uap4mp`, `PregnancyUK-1ub6d87`, `PregnancyUK-1ucf82k`, `PregnancyUK-1ud4tqo`, `PregnancyUK-1ueqbvd`, `beyondthebump-1uaeg92`, `beyondthebump-1uccwk5`, `beyondthebump-1uduknw`, `pregnant-1ua8na3`, `pregnant-1uaih0x`, `pregnant-1uaihkh`, `pregnant-1uajq4k`, `pregnant-1uaotv9`, `pregnant-1uazrve`, `pregnant-1ub3xb9`, `pregnant-1uba6vb`, `pregnant-1ubq3wg`, `pregnant-1uc83j7`, `pregnant-1uca49i`, `pregnant-1ucm1py`, `pregnant-1ucsdy6`, `pregnant-1ucx7lp`, `pregnant-1ucz17g`, `pregnant-1ud2ihu`, `pregnant-1ud37jv`, `pregnant-1ud67xa`, `pregnant-1ud6dl0`, `pregnant-1uda9es`, `pregnant-1udu8js`, `pregnant-1udu900`, `pregnant-1ue79dw`, `pregnant-1ueakiy`, `pregnant-1ueekwv`, `pregnant-1uemg9l`, `pregnant-1uemjwo`, `pregnant-1uenkfh`, `pregnant-1uepjkf`, `pregnant-1ueqegf`, `pregnant-1uerqwj`, `pregnant-1uesaob`.

## Result and conclusions that moved

**2,265 distinct formerly marked quotes are now reproduced in full as ordinary evidence:** 57 previously cited without their words and 2,208 previously uncited. Each restored passage was read from `voice/*.jsonl`, including the 33 reviews. All 1,158 original explicit cited ids remain. Wording, case and punctuation are preserved; whitespace is collapsed for inline Markdown. Evidence is placed in §§2–9 and §15, with original later-wave citations also restored at their existing locations; it is not collected in an appendix. Existing provenance flags accompany the affected quotes. The dated closing section lists the moved conclusions and their ids.

The original planning account now includes consent and care decisions, pain relief that helped or failed, the consequences of promised outcomes, physical and emotional recovery, feeding pressure, being believed, cost shaping birth choices, the practical limits of another pregnancy with a child at home, reassurance loops, and contrary positive accounts. The earlier identity-only exercise reading and blanket absence claims about paid pregnancy information are qualified. There is still no direct buyer evidence for the proposed Mamivio guide; adjacent books, the breech ebook, classes and apps are their own evidence.

The queue has **11,880 rows: 2,226 units + 9,654 posts** (8,822 intake safety posts + 832 triage drops), no duplicate ids and no missing safety-lane ids. These three current sets do not overlap; `kind=unit` is used for a frozen reading-assignment unit, and `kind=post` for intake/triage metadata. Every id includes its known subreddit. No source candidate, triage file, source body, voice original, reader note or historical run log was changed. No queued material was re-read for findings.

## Every changed file (19)

Paths below are relative to `pregnancy-birth/`. No other build or shared file was edited.

- `README.md` — replace subject exclusions with the owner’s principle; document current state and historical-instruction precedence.
- `_tools/query.py` — make the legacy exclude option a no-op and remove the eligibility warning.
- `_tools/verify_unfilter.py` — check full restored wording, every literal id, queue uniqueness/completeness and inactive merged flags.
- `product/product-brief.md` — remove subject exclusions and copy prohibitions from the research brief.
- `scratchpad/FINDINGS-W2/check_restricted.py` — remove subject rejection while retaining id and quotation checks; return failure status for real problems.
- `scratchpad/FINDINGS-W2/w2counts.py` — read the historical marker for historical counts.
- `scratchpad/FINDINGS-W3/check_restricted.py` — remove subject rejection while retaining id and quotation checks; return failure status for real problems.
- `scratchpad/FINDINGS-W3/q.py` — remove unrestricted-only selection; display historical label.
- `scratchpad/FINDINGS-W3/trim.py` — stop suppressing historical restriction sections.
- `scratchpad/FINDINGS-W3/w3counts.py` — read the historical marker for historical counts.
- `scratchpad/FINDINGS/check_frags.py` — remove subject rejection while retaining fragment checks; pair short quote delimiters before length filtering and avoid distant prose-label pairings.
- `scratchpad/FINDINGS/q.py` — remove unrestricted-only selection; display historical label.
- `scratchpad/unfilter-reread/queue.tsv` — deduplicated intake, triage and reading-stage re-reading queue with recorded reasons.
- `synthesis/audit-safety-hits.tsv` — rename the old flag column as historical; preserve rows and matches.
- `synthesis/counts.md` — keep historical marking count and record zero active restrictions.
- `synthesis/findings.md` — restore all marked words, integrate uncited evidence, revise conclusions and add the dated change section.
- `synthesis/restricted-ids.md` — retitle as historical, preserve every id/reason, explain that companion TSVs have no active effect.
- `synthesis/unfilter-report.md` — inventory before editing; full gap list, changed files and validation.
- `voice-merged/all.jsonl` — clear derived active flags, retain historical labels and every record.

Already corrected shared prompts checked, unchanged: `../_shared/_tools/prompt-pregnancy-reader.txt`, `prompt-pregnancy-reader-w2.txt`, `prompt-pregnancy-reader-w3.txt`, `prompt-pregnancy-triage-w3.txt`. Shared `brief-reading.md`, `brief-findings.md`, `niche_filter.py`, `collect_restricted.py`, `audit_niche.py`, `verify_findings_ids.py` and `check_ids.py` were inspected, never edited or used to regenerate raw artifacts. `niche_filter.py` now treats the safety match as descriptive; the frozen safety-candidate queue records the old route. Historical per-reader builders and scratch data remain records, superseded by the README principle and not instructions to rebuild this corpus.

## Verification

All commands used `python3 -I`. Commands below are run from the repo root unless stated otherwise. `audit_niche.py --check-only` checks frozen assignment metadata and ledgers without regenerating artifacts. The raw-source check validates existing extracted quotes only; it performs no research re-reading or new extraction.

`python3 -I mamivio.com/research/_shared/_tools/verify_findings_ids.py mamivio.com/research/pregnancy-birth/synthesis/findings.md pregnancy-birth` — exit 0:

```text
3312 distinct ids cited, 0 unresolved
2825 verbatim fragments paired with an id, 0 failed
```

`python3 -I mamivio.com/research/_shared/_tools/check_ids.py pregnancy-birth` — exit 0:

```text
18578 records, 18578 distinct ids, 0 duplicated
```

`python3 -I mamivio.com/research/_shared/_tools/audit_niche.py pregnancy-birth read-v1 read-w2 read-w3 --check-only` — exit 0:

```text
{"quotes": 18578, "assigned": 10274, "units_quoted": 7642, "assigned_units_quoted": 7586, "uncited": 2688, "unexplained": 0, "historically_marked": 2265, "active_restrictions": 0, "safety_hits": 58}
```

`python3 -I mamivio.com/research/pregnancy-birth/_tools/verify_unfilter.py` — exit 0:

```text
3366 explicit ids, 0 unresolved; 2265 historically marked full quotes, 0 missing or changed
11880 queue rows, 0 duplicate ids, 0 malformed rows; 8822 safety-routed posts, 0 absent from queue
0 active merged restrictions; 0 old findings labels
```

`python3 -I mamivio.com/research/pregnancy-birth/_tools/verify_quotes.py` — exit 0:

```text
reddit-pr01.jsonl: 246 quotes, 0 failed
reddit-pr02.jsonl: 257 quotes, 0 failed
reddit-pr03.jsonl: 248 quotes, 0 failed
reddit-pr04.jsonl: 211 quotes, 0 failed
reddit-pr05.jsonl: 214 quotes, 0 failed
reddit-pr06.jsonl: 224 quotes, 0 failed
reddit-pr07.jsonl: 203 quotes, 0 failed
reddit-pr08.jsonl: 261 quotes, 0 failed
reddit-pr09.jsonl: 277 quotes, 0 failed
reddit-pr10.jsonl: 251 quotes, 0 failed
reddit-pr11.jsonl: 201 quotes, 0 failed
reddit-pr12.jsonl: 190 quotes, 0 failed
reddit-pr13.jsonl: 302 quotes, 0 failed
reddit-pr14.jsonl: 245 quotes, 0 failed
reddit-pr15.jsonl: 237 quotes, 0 failed
reddit-pr16.jsonl: 230 quotes, 0 failed
reddit-pr17.jsonl: 293 quotes, 0 failed
reddit-pr18.jsonl: 368 quotes, 0 failed
reddit-pr19.jsonl: 257 quotes, 0 failed
reddit-pr20.jsonl: 274 quotes, 0 failed
reddit-pr21.jsonl: 289 quotes, 0 failed
reddit-pr22.jsonl: 168 quotes, 0 failed
reddit-pr23.jsonl: 336 quotes, 0 failed
reddit-pr24.jsonl: 254 quotes, 0 failed
reddit-pr25.jsonl: 348 quotes, 0 failed
reddit-pr26.jsonl: 257 quotes, 0 failed
reddit-pr27.jsonl: 308 quotes, 0 failed
reddit-pr28.jsonl: 240 quotes, 0 failed
reddit-pr29.jsonl: 210 quotes, 0 failed
reddit-pr30.jsonl: 225 quotes, 0 failed
reddit-pr31.jsonl: 230 quotes, 0 failed
reddit-pr32.jsonl: 181 quotes, 0 failed
reddit-pr33.jsonl: 249 quotes, 0 failed
reddit-pr34.jsonl: 219 quotes, 0 failed
reddit-pr35.jsonl: 189 quotes, 0 failed
reddit-pr36.jsonl: 256 quotes, 0 failed
reddit-pr37.jsonl: 221 quotes, 0 failed
reddit-pr38.jsonl: 190 quotes, 0 failed
reddit-pr39.jsonl: 231 quotes, 0 failed
reddit-pr40.jsonl: 177 quotes, 0 failed
reddit-pr41.jsonl: 239 quotes, 0 failed
reddit-pr42.jsonl: 232 quotes, 0 failed
reddit-pr43.jsonl: 263 quotes, 0 failed
reddit-pr44.jsonl: 210 quotes, 0 failed
reddit-pr45.jsonl: 254 quotes, 0 failed
reddit-pr46.jsonl: 259 quotes, 0 failed
reddit-pr47.jsonl: 286 quotes, 0 failed
reddit-pr48.jsonl: 282 quotes, 0 failed
reddit-pr49.jsonl: 320 quotes, 0 failed
reddit-pr50.jsonl: 236 quotes, 0 failed
reddit-pr51.jsonl: 346 quotes, 0 failed
reddit-pr52.jsonl: 217 quotes, 0 failed
reddit-pr53.jsonl: 301 quotes, 0 failed
reddit-pr54.jsonl: 205 quotes, 0 failed
reddit-pr55.jsonl: 274 quotes, 0 failed
reddit-pr56.jsonl: 271 quotes, 0 failed
reddit-pr57.jsonl: 332 quotes, 0 failed
reddit-pr58.jsonl: 206 quotes, 0 failed
reddit-pr59.jsonl: 246 quotes, 0 failed
reddit-pr60.jsonl: 241 quotes, 0 failed
reddit-pr61.jsonl: 226 quotes, 0 failed
reddit-pr62.jsonl: 260 quotes, 0 failed
reddit-pr63.jsonl: 257 quotes, 0 failed
reddit-pr64.jsonl: 327 quotes, 0 failed
reddit-pr65.jsonl: 224 quotes, 0 failed
reddit-pr66.jsonl: 262 quotes, 0 failed
reddit-pr67.jsonl: 223 quotes, 0 failed
reddit-pr68.jsonl: 246 quotes, 0 failed
reddit-pr69.jsonl: 277 quotes, 0 failed
reddit-pr70.jsonl: 331 quotes, 0 failed
reddit-pr71.jsonl: 258 quotes, 0 failed
reddit-pr72.jsonl: 419 quotes, 0 failed
reviews-rv1.jsonl: 281 quotes, 0 failed
TOTAL 18578 quotes, 0 failed
```

Local checks from `mamivio.com/research/pregnancy-birth/`, each exit 0:

```text
python3 -I scratchpad/FINDINGS/check_frags.py
fragments checked 3183 problems 0
python3 -I scratchpad/FINDINGS-W2/check_restricted.py
ids 787 problems 0
python3 -I scratchpad/FINDINGS-W3/check_restricted.py
ids 455 problems 0
```

Compatibility checks: `_tools/query.py --exclude-restricted --id pb01-0032` returns `# 1 match` and the complete quote. Both FINDINGS lookup scripts with `-g 'WHAT THE FUCK' -u` return three matching records, including formerly marked `pb01-0032`; the compatibility flag no longer hides it. A baseline-to-final id comparison found **0 original explicit cited ids missing**. The stricter full-quote audit checks all 2,265 restorations with whitespace normalization only, beyond the shared verifier’s adjacent-fragment detection. The shared verifier’s 3,312 bracketed citations and the full audit’s 3,366 explicit ids differ because the latter also checks plain references/range endpoints.

## Remaining uncertainty

The queue is deliberately conservative. Reasons such as symptom-only, thin, off-topic, duplicate, age, promotion or mixed reasons do not by themselves prove the safety rule caused a drop; the TSV retains them wherever subject and disposition were entangled. Unlogged omissions cannot be enumerated, and neither their words nor their count can be recovered from voice. Intake matches are metadata labels, not a claim about the source’s full meaning. Queued re-reading may move conclusions again.

The old money table attributed £240 to `pb01-0231`, but that voice record contains no amount; the table now says so rather than inventing price wording. The historical notes mention £240, but verifying that figure against its unit is outside this restoration. The selection-related withdrawn ids listed above are not present in voice, so none has been reconstructed or reused.


## Re-reading closed and findings integrated — 2026-11-17

The 2026-11-16 exclusion queue is complete: **11,880/11,880 assigned rows read**, **0 missing or unfinished**, **11,539 rows with new quotes**, **341 explained no-new-quote rows**, and **15,768 verified new quotes** across UR01–UR40. Every per-row ledger id and count reconciles to its assignment and voice file. All 13 digests were considered together for this integration; their 2,048 money ids and 5,133 request/question ids (6,484 in the union) are retained in full, including broader peer questions without calling them product demand. Findings now cite **11,273 distinct bracketed ids**, including **7,961 re-reading quotes reproduced in full**. All **3,366 earlier explicit ids** remain, including all 3,312 bracketed ids and all 2,265 complete restored historical quotations. There are **21 new evidence subsections, nine money subdivisions and the dated closing change section** (31 new headings). Seventy-four earlier fragment typography differences were corrected to exact voice wording; no source field was changed.

The revised conclusions include pregnancy decisions and loss as lived stages, pregnancy history separate from living children and actual knowledge, reproductive/sexual coercion distinct from a task gap, severe prenatal/postpartum distress despite support, treatment continuity and substance coping, blocked or unsafe-feeling disclosure, clinical uncertainty distinct from reassurance loops, consent and bodily privacy, recovery/separation beyond two weeks, grief-sensitive family support, and money shaping access and autonomy. Positive care, relief, joy and easier recoveries remain. Each moved conclusion is recorded with before/after wording and ids in the findings’ final section. No purchase or price acceptance of the proposed Mamivio guide is demonstrated.

**Nothing in the named queue remains unread.** The ordinary available backlog is **56,212 distinct posts**: 2,763 tier A, 31,785 tier B and 21,664 tier C, calculated by post identity against both completed reading sets. The **5,838 unavailable bodies** are separate. Archive-only reads cannot supply absent replies; some passages retain chronology, credibility, promotional or third-party limitations. Reported medical effects, allegations, policies, laws and causal explanations were not independently adjudicated. Other source/collection gaps remain as listed in findings §13 and `sources/reddit.md`. These are not prevalence or independent-person counts.

Changed for this integration: `README.md`, `synthesis/findings.md`, `synthesis/counts.md`, `sources/reddit.md`, this report, `voice-merged/all.jsonl`, `synthesis/audit-safety-hits.tsv`, and the new local `_tools/rebuild_voice.py`. The unchanged shared audit rebuilt all **34,346 records**; the local wrapper preserves the historical spot-check worksheet and original reader speaker attributions, rejecting nine incorrect father-regex relabels. A second wrapper rebuild changed no artifact. No raw file, original voice file, reader ledger, digest, shared script or other build was modified. No network or git was used.

### Integration checks — all exit 0

From `mamivio.com/research/`:

```text
python3 -I _shared/_tools/verify_findings_ids.py pregnancy-birth/synthesis/findings.md pregnancy-birth
11273 distinct ids cited, 0 unresolved
10180 verbatim fragments paired with an id, 0 failed

python3 -I _shared/_tools/check_ids.py pregnancy-birth
34346 records, 34346 distinct ids, 0 duplicated

python3 -I _shared/_tools/audit_niche.py pregnancy-birth read-v1 read-w2 read-w3 --check-only
{"quotes": 34346, "assigned": 10274, "units_quoted": 9689, "assigned_units_quoted": 9609, "uncited": 665, "unexplained": 0, "historically_marked": 2265, "active_restrictions": 0, "safety_hits": 1042}

python3 -I pregnancy-birth/_tools/verify_unfilter.py
3366 explicit ids, 0 unresolved; 2265 historically marked full quotes, 0 missing or changed
11880 queue rows, 0 duplicate ids, 0 malformed rows; 8822 safety-routed posts, 0 absent from queue
0 active merged restrictions; 0 old findings labels
```

Additional read-only checks in `/tmp/pb-source-check.py` and `/tmp/pb-final-checks.py`:

```text
UR raw provenance: 15768/15768 complete quote fields match their own decoded post or cited unit literally; 0 failed.
Build source verifier: TOTAL 34346 quotes, 0 failed.
Full new quotations: 7961/7961 complete fields match voice after whitespace collapse only; 0 failed.
Strict paired-fragment check: 10216 fragments; 0 failed; case and punctuation retained.
Mandatory money/request union: 6484/6484 ids retained; 0 missing.
Citation preservation: 3366/3366 earlier explicit ids retained; 0 lost.
Merged integrity: 34346/34346 source records and speaker labels retained; only derived historical/active flags differ.
Protected integrity: 455 original JSONL/reader-ledger/digest files unchanged; no raw changes; historical spot-check unchanged.
```

The existing `_tools/verify_quotes.py` was executed unchanged with a read-only in-memory adapter that decodes JSONL and returns the record’s own `post_id`; searching serialized JSON escapes would misread source text. The separate UR check used literal matching without normalization. The audit’s 665 uncovered original raw paths and 9,689 quoted raw paths are path measures, not UR assignment gaps or independent-post counts; `counts.md` explains their scope. Descriptive regex matches do not restrict evidence, and this rebuild does not claim a new manual adjudication of every match.
