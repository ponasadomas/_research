# Sleep-mother unfilter report — 2026-11-16

Initial inventory written before changing findings, instructions or tools. Scope: `sleep-mother/` only; the build-specific shared prompt and review brief were inspected and are already corrected, so no shared file needs an edit. No network, git, push, raw mutations or manual re-reading of raw units. Reader notes, source ledgers and run logs remain historical records. Counts describe selected quotes, records, units or queued posts, never people or prevalence.

## Verified baseline, by stage

- **Intake:** `_raw/reddit/filter-v1/safety-candidates.jsonl` contains **425** posts routed to the separate safety tier before A/B/C reading cards. There is only one `filter-*` directory in this build. Those 425 ids are queued from candidate metadata, without inspecting post bodies. The corrected shared `niche_filter.py` no longer imposes this exclusion, but frozen intake artifacts retain the history.
- **Triage:** seven wave/reader TSVs plus `wave3-corrections-orchestrator.tsv` in `_raw/reddit/triage/` document **41 explicit `safety:` drops**, including the orchestrator override. A broader subject-word scan identifies **257 unique dropped posts**, including those 41. All 257 are queued with their recorded reasons: many combine a subject with an off-topic or incidental-sleep judgement, so the broader count is a conservative re-reading set, not 257 proven safety drops. `synthesis/reader-notes-triage.md` records 15 wave-1 safety drops; the wave-1 TSVs contain 16, a historical count discrepancy.
- **Reading:** `README.md` and `product/product-brief.md` directed crisis, psychosis, self-harm and suicide exclusions and imposed copy decisions on research. Nine source ledgers name **87 formally excluded Reddit units** (MR01 9, MR02 11, MR03 14, MR04 11, MR05 10, MR06 5, MR07 10, MR08 9, MR09 8). MR02 includes one duplicate with the same subject reason and one disaster post with little sleep detail; both recorded exclusions are retained. MR04 additionally recorded 3 subject-based “nothing quotable” units, and MR09 withheld a named-phobia unit: **91 whole Reddit units** in all. Review metadata additionally records **13 unquoted age/role candidates**, including an illness/GAD review: mixed relevance reasons are retained, not assumed to be censorship. The 238 app reviews without a parent/partner mention and 2 generic book reviews are ordinary relevance omissions, recorded separately in `sources/reviews.md`, not counted as proven subject censorship.
- **Quote extraction:** named partial omissions in MR01/MR02 prose, MR03/MR04 prose, MR06 and MR07 handling notes, and MR08's unit ledger removed mental-health words, hallucinations, infant harm and safety events, bereavement, medical history, advice, medication and supplements. MR08 explicitly cut subject clauses from sm08-0096, sm08-0196, sm08-0326 and sm08-0327. MR06 says it trimmed subject wording but does not identify every affected id: all 15 of its trimmed quote units are conservatively queued. There are **117 named partial omissions plus 15 MR06 trim-candidate units: 132 units** in all; lists are below. MR01 contributes 10 named partial units (9 in its ledger plus the OB-advice omission in its notes), MR02 26, MR03 2, MR04 5, MR06 1 named omission and 15 trim candidates, MR07 16, and MR08 57 (56 skipped-passage ledger rows plus a further explicitly trimmed unit). Existing voice quotations cannot restore any words these readers never extracted.
- **Marking:** `synthesis/restricted-ids.md` lists **486 unique resolving ids**: **478 Reddit and 8 review ids** in 3,005 voice records. Prefix counts: sm01 47, sm02 95, sm03 120, sm04 41, sm05 29, sm06 33, sm07 42, sm08 24, sm09 47, smr1 8. `synthesis/restricted-review-mr04-mr06.tsv` contains 869 decisions (103 true, 766 false), superseding 425 wave-2 reader flags. `voice-merged/all.jsonl` copied the historical decisions into active `restricted` booleans; `synthesis/counts.md` called them active research-only restrictions. Original `voice/*.jsonl` remain the verbatim source of truth.
- **Findings:** the baseline `synthesis/findings.md` cites **910 distinct ids**, including **73 marked ids** whose words were replaced or omitted, and leaves **413 marked ids uncited**. It also withholds the words of additional unmarked ids solely for anxiety vocabulary or the source subreddit. Sections 4.7, 6, 9.6, 10, 12, 16.5 and 17.5 perpetuate the filter. They turn absence of quotation into a narrow account of physical purchases, advice and treatment, and claim nobody paid for information despite review evidence of a paid insomnia program.
- **Tooling / instructions:** `_tools/query.py` implements `--exclude-restricted` against `marketing_eligible=false` and prints a research-boundary warning. `scratchpad/FINDINGS/q.py` has a hidden `--norestr` skip and marks lookup results as restricted. `scratchpad/FINDINGS/check_restricted_pairs.py` and `scratchpad/FINDINGS-W3/check17.py` detect/report quotation of marked ids as forbidden; neither actually has a nonzero failure exit, despite the first docstring saying “Fail”. These active helpers will be corrected while keeping provenance checks. The corrected shared `verify_findings_ids.py`, `check_ids.py` and local `_tools/verify_quotes.py` already check ids and verbatim provenance, with no subject rejection. Shared `audit_niche.py` now supports `--check-only` and zero active restrictions. Shared `prompt-sleep-mother-reader-w3.txt` and `brief-restricted-review-sm-w2.md` already state the owner's principle and require no edits. Historical reader builders and count/category scripts remain run records; none is re-run to rebuild voice files.

## Reading gaps that require raw re-reading

The following inventory comes from ledgers/notes and quote metadata only. No missing words or conclusions are invented. Re-reading must recover whole excluded units and omitted passages, including the explicitly trimmed clauses; the number of missing quotes and any unlogged omissions is unknown. Queued triage and intake posts require their own initial reading. The queue also identifies uncertain trim/relevance candidates explicitly.

### Whole-unit exclusions and review candidates (104)

| unit or review id | recorded reason / source |
|---|---|
| `BabyBumps-1sc1wgk` | reddit-reading-mr07.md: acute illness and medication centre the post |
| `BabyBumps-1ssi0k5` | reddit-reading-mr08.md: centred on named mental-health conditions and medication |
| `BabyBumps-1sto7db` | reddit-reading-mr08.md: intrusive thoughts and rough handling of the child |
| `BabyBumps-1t8h3ec` | reddit-reading-mr08.md: centred on named mental-health conditions and medication |
| `BabyBumps-1tl5h3z` | reddit-reading-mr07.md: possible medical emergency and monitor alarms centre the post |
| `BabyBumps-1tsut8p` | reddit-reading-mr09.md (read, no quote): only content is a named phobia |
| `BabyBumps-1va6d41` | reddit-reading-mr05.md: centred on a named medication and dose in pregnancy |
| `BabyBumps-1wescw9` | reddit-reading-mr02.md: repost of the previous unit; same reason |
| `BabyBumps-1xaf7qb` | reddit-reading-mr03.md: centred on eating disorder, self-harm behaviour and psychiatric medication |
| `FirstTimeMom-1xcucjl` | reddit-reading-mr03.md: centred on prescription medication dosing |
| `Mommit-1ugf62m` | reddit-reading-mr04.md: centred on mental-health crisis wording |
| `Mommit-1ur164q` | reddit-reading-mr04.md (read, no quote): holiday logistics; the sleep lines are co-sleeping and child medication |
| `Mommit-1uruosa` | reddit-reading-mr04.md (read, no quote): teething; infant medication dosing and the mother's medical condition |
| `Mommit-1uw2p64` | reddit-reading-mr04.md: safe-sleep incident |
| `Mommit-1vko4ne` | reddit-reading-mr05.md: centred on a sequence of named psychiatric medications |
| `Mommit-1vx0az2` | reddit-reading-mr06.md: post centred on intrusive thoughts and acute distress |
| `Mommit-1w008e7` | reddit-reading-mr01.md: centred on starting psychiatric medication |
| `Mommit-1w23z99` | reddit-reading-mr01.md: safe-sleep incident |
| `Mommit-1wa5i5d` | reddit-reading-mr02.md: medication names and dosing for postpartum insomnia |
| `Mommit-1wb59qv` | reddit-reading-mr02.md: infant-supervision incident while the parent was asleep |
| `Mommit-1wq27xs` | reddit-reading-mr01.md: centred on postpartum mental-health recovery; mentions intrusive thoughts; little sleep detail |
| `Mommit-1x681rf` | reddit-reading-mr01.md: substance and medication use for sleep and mood |
| `Mommit-1xahz2o` | reddit-reading-mr03.md: centred on child injury incidents, trauma and medication enquiries |
| `NewParents-1scclfx` | reddit-reading-mr07.md: post centred on a named condition, its treatment and intrusive thoughts |
| `NewParents-1sld7p7` | reddit-reading-mr07.md: safe-sleep worry centres the post |
| `NewParents-1sox5xq` | reddit-reading-mr08.md: safe-sleep incident |
| `NewParents-1sqjzhz` | reddit-reading-mr08.md: contains suicidal-thought wording |
| `NewParents-1t3ziwd` | reddit-reading-mr08.md: centred on accidental substance ingestion while caring for the baby |
| `NewParents-1t7zmq8` | reddit-reading-mr07.md: safe-sleep incident centres the post |
| `NewParents-1tmrx41` | reddit-reading-mr07.md: acute distress with the newborn centres the post |
| `NewParents-1tv25sx` | reddit-reading-mr07.md: crisis wording in a looking-back post |
| `NewParents-1u7wznv` | reddit-reading-mr09.md: post contains self-injury used to cope with pain |
| `NewParents-1ubl0l8` | reddit-reading-mr09.md: post centred on a named postpartum condition and its treatment |
| `NewParents-1ue7uc2` | reddit-reading-mr07.md: newborn emergency and safe-sleep fears centre the post |
| `NewParents-1uhqf72` | reddit-reading-mr04.md: contains wording about not wanting to be here; medication offered |
| `NewParents-1uoq7f0` | reddit-reading-mr04.md: safe-sleep incident; hallucination content |
| `NewParents-1utiv1w` | reddit-reading-mr04.md: safe-sleep incident |
| `NewParents-1vbugbf` | reddit-reading-mr05.md: self-harm wording and medication |
| `NewParents-1vp04qs` | reddit-reading-mr06.md: safe-sleep practices centre the post |
| `NewParents-1vzpawo` | reddit-reading-mr01.md: medication names and dosing for postpartum insomnia |
| `NewParents-1w3gmh0` | reddit-reading-mr01.md: author describes not sleeping because of overwhelming emotion and says she is "starting to lose it a bit from lack of sleep"; held back for review, not quoted |
| `NewParents-1w71l4f` | reddit-reading-mr02.md: centred on distress wording; held back for review, not quoted |
| `NewParents-1x9ypaz` | reddit-reading-mr03.md: centred on a safe-sleep near-incident |
| `Postpartum_Depression-1t3k3rp` | reddit-reading-mr08.md: centred on named conditions, hospital stay and medication |
| `Postpartum_Depression-1tt9sn2` | reddit-reading-mr07.md: crisis wording in the post |
| `Postpartum_Depression-1tzzzz3` | reddit-reading-mr09.md: post centred on a physical fight between partners |
| `Postpartum_Depression-1uq35v3` | reddit-reading-mr04.md: medication and an acute incident |
| `Postpartum_Depression-1uun3w3` | reddit-reading-mr04.md: medication dosing |
| `Postpartum_Depression-1uv9tjd` | reddit-reading-mr04.md: wording about not being here |
| `Postpartum_Depression-1v9is74` | reddit-reading-mr05.md: medication changes with a dose, a safe-sleep incident and crisis wording |
| `Postpartum_Depression-1vjcr59` | reddit-reading-mr06.md: crisis wording in the poster's reply |
| `Postpartum_Depression-1vodxhp` | reddit-reading-mr05.md: includes a self-harm passage |
| `Postpartum_Depression-1vxo5b0` | reddit-reading-mr01.md: acute medical emergency involving the infant |
| `Postpartum_Depression-1w4o3kv` | reddit-reading-mr01.md: centred on a parent's mental-health crisis wording |
| `Postpartum_Depression-1wgncie` | reddit-reading-mr02.md: centred on intrusive thoughts and a medication decision |
| `Postpartum_Depression-1wko0ph` | reddit-reading-mr02.md: centred on a parent's acute mental-health wording; dropped under the README rule |
| `Postpartum_Depression-1wug0yb` | reddit-reading-mr03.md: centred on acute mental-health distress and medication decisions |
| `Postpartum_Depression-1wxjlnp` | reddit-reading-mr03.md: centred on postpartum mental-health distress, including distressing thoughts about the baby |
| `Postpartum_Depression-1x2k4c2` | reddit-reading-mr03.md: centred on postpartum mental-health distress with crisis-adjacent wording |
| `PregnancyUK-1tvmeoc` | reddit-reading-mr09.md: post centred on named mental-health conditions and medication during a hospital induction |
| `PregnancyUK-1w69m1c` | reddit-reading-mr02.md: centred on a medication's side effects on sleep |
| `bettersleep-us-7235161411` | reading-ledger-rv1.tsv: read, not quoted: reviewer appears to be a minor (school, "my mom uses it"); age/role exclusion candidate, mixed relevance where stated |
| `beyondthebump-1sjiq9w` | reddit-reading-mr08.md: centred on named mental-health conditions and medication, with a self-harm reference |
| `beyondthebump-1u0hfnf` | reddit-reading-mr09.md: post contains thoughts of harming the baby |
| `beyondthebump-1u5hu4f` | reddit-reading-mr09.md: post centred on a night-time monitoring and safe-sleep scare |
| `beyondthebump-1uabud7` | reddit-reading-mr09.md: post contains possible crisis wording |
| `beyondthebump-1uk1avc` | reddit-reading-mr04.md: centred on medication and injections |
| `beyondthebump-1uwx8vc` | reddit-reading-mr04.md (read, no quote): medical symptoms and remedies |
| `beyondthebump-1uzdca4` | reddit-reading-mr06.md: post centred on a road-safety incident |
| `beyondthebump-1v1wffd` | reddit-reading-mr05.md: centred on a medication decision and dosing questions |
| `beyondthebump-1v3sjt1` | reddit-reading-mr05.md: centred on an unsafe sleep arrangement for the baby |
| `beyondthebump-1vo9bjs` | reddit-reading-mr05.md: describes a safe-sleep incident |
| `beyondthebump-1x351x1` | reddit-reading-mr03.md: centred on mental-health distress and prescription sleep medication |
| `beyondthebumpUK-1uuf2wo` | reddit-reading-mr04.md: safe-sleep incident |
| `beyondthebumpUK-1x4ez8s` | reddit-reading-mr03.md: centred on a mental-health crisis and medication |
| `calm-au-10472913125` | reading-ledger-rv1.tsv: read, not quoted: reviewer states she is 11; age/role exclusion candidate, mixed relevance where stated |
| `calm-us-4697206150` | reading-ledger-rv1.tsv: read, not quoted: professional caregiver, not a parent; age/role exclusion candidate, mixed relevance where stated |
| `calm-us-6055007108` | reading-ledger-rv1.tsv: read, not quoted: reviewer states age nine; age/role exclusion candidate, mixed relevance where stated |
| `calm-us-6114739748` | reading-ledger-rv1.tsv: read, not quoted: school-age reviewer using her mother's phone; age/role exclusion candidate, mixed relevance where stated |
| `daddit-1ub87o5` | reddit-reading-mr07.md: safe-sleep incident centres the post |
| `headspace-au-11279364037` | reading-ledger-rv1.tsv: read, not quoted: grandparent/husband illness and GAD; not about sleep; mental-health frame; age/role exclusion candidate, mixed relevance where stated |
| `headspace-us-7669171053` | reading-ledger-rv1.tsv: read, not quoted: reviewer is the child (father paid); age/role exclusion candidate, mixed relevance where stated |
| `pregnant-1ut0uu0` | reddit-reading-mr04.md: prescription medication for sleep; dark-thoughts wording |
| `pregnant-1vhmzvt` | reddit-reading-mr05.md: acute medical emergency and medication in pregnancy |
| `pregnant-1wb8y9x` | reddit-reading-mr02.md: centred on medication and emergency visits; crisis wording |
| `pregnant-1wej560` | reddit-reading-mr02.md: centred on a natural disaster; little sleep detail |
| `pregnant-1wes7w6` | reddit-reading-mr02.md: centred on panic attacks and current medication |
| `pregnant-1wkee65` | reddit-reading-mr02.md: medication names and dosing for pregnancy insomnia |
| `pregnant-1wpenjc` | reddit-reading-mr03.md: centred on cold and supplement remedies in early pregnancy |
| `pregnant-1ws9015` | reddit-reading-mr03.md: centred on mental-health distress; sleep detail secondary |
| `pregnant-1x7umic` | reddit-reading-mr03.md: centred on medication choice in pregnancy |
| `rise-us-10837947205` | reading-ledger-rv1.tsv: read, not quoted: teen reviewer; age/role exclusion candidate, mixed relevance where stated |
| `rise-us-12213698339` | reading-ledger-rv1.tsv: read, not quoted: "my parents would say" (reviewer is the adult child); age/role exclusion candidate, mixed relevance where stated |
| `sahm-1tj70y2` | reddit-reading-mr09.md: post centred on domestic violence and a named postpartum condition with treatment |
| `sahm-1vj4hir` | reddit-reading-mr05.md: crisis wording |
| `sleeptrain-1uk7vtn` | reddit-reading-mr06.md: crisis wording in a looking-back post |
| `sleeptrain-1w0sxy2` | reddit-reading-mr01.md: safe-sleep incident |
| `sleeptrain-1wzwyx7` | reddit-reading-mr03.md: trigger is a road-safety incident |
| `sleeptrain-1x212de` | reddit-reading-mr03.md: contains thoughts of harming the baby |
| `slumber-au-10725315963` | reading-ledger-rv1.tsv: read, not quoted: grandparent; granddaughter mention only; age/role exclusion candidate, mixed relevance where stated |
| `slumber-au-6048536682` | reading-ledger-rv1.tsv: read, not quoted: reviewer is a child (parents' screen-time limit); age/role exclusion candidate, mixed relevance where stated |
| `slumber-au-9977194584` | reading-ledger-rv1.tsv: read, not quoted: school-age reviewer; age/role exclusion candidate, mixed relevance where stated |
| `slumber-us-4748296436` | reading-ledger-rv1.tsv: read, not quoted: says she has no kids; age/role exclusion candidate, mixed relevance where stated |
| `workingmoms-1t67w5z` | reddit-reading-mr08.md: bed-sharing post describing rough physical handling of the toddler |

### Partly extracted units and trim candidates (132)

| unit or review id | recorded reason / source |
|---|---|
| `BabyBumps-1srlhdj` | reddit-reading-mr08.md: two clean lines quoted; medication-withdrawal content skipped (2 quotes) |
| `BabyBumps-1swh124` | reddit-reading-mr08.md: quoted (one restricted: named condition; supplement reply skipped) (3 quotes) |
| `BabyBumps-1umdu30` | MR04: road incident omitted |
| `BabyBumps-1uogsr1` | MR04: medication lines omitted |
| `BabyBumps-1uyx4xf` | MR06: sm06-0200 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `BabyBumps-1vlrjl5` | MR06: sm06-0240 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `BabyBumps-1wb7wqq` | reddit-reading-mr02.md: substance use lines (beyondthebump-1w70kt8, BabyBumps-1wb7wqq, beyondthebump-1wfakdw) |
| `BabyBumps-1wjhxsq` | reddit-reading-mr02.md: BabyBumps-1wjhxsq prescription and dose |
| `FirstTimeMom-1sdz5rl` | reddit-reading-mr07.md: condition names not quoted. |
| `FirstTimeMom-1t1bvbw` | reddit-reading-mr08.md: two clean lines quoted; bed-sharing/safe-sleep account skipped (2 quotes) |
| `FirstTimeMom-1uos7gg` | MR04: medication lines omitted |
| `Mommit-1sa3jlg` | reddit-reading-mr07.md: medication and condition detail not quoted. |
| `Mommit-1sm9p95` | reddit-reading-mr08.md: quoted (bed-sharing lines skipped) (2 quotes) |
| `Mommit-1stbb9p` | reddit-reading-mr08.md: quoted (one restricted; child supplement list skipped) (5 quotes) |
| `Mommit-1t0coxo` | reddit-reading-mr08.md: quoted (bed-sharing line skipped) (2 quotes) |
| `Mommit-1t26lvb` | reddit-reading-mr08.md: quoted (choking incident skipped) (3 quotes) |
| `Mommit-1udfcwe` | reddit-reading-mr07.md: a baby-safety incident in the post is not quoted. |
| `Mommit-1vz1a0b` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `Mommit-1w3mhdm` | reddit-reading-mr02.md: Partial skips inside quoted units (passages left out, unit still quoted): medication and supplement passages (Mommit-1w3mhdm except one sleep line |
| `Mommit-1w5oah2` | reddit-reading-mr02.md: falling asleep holding the baby in a glider (Mommit-1w5oah2) |
| `Mommit-1w5y0co` | reddit-reading-mr02.md: a partner asleep with the baby on a sofa edge and a bath incident (Mommit-1w5y0co) |
| `NewParents-1sck46o` | reddit-reading-mr07.md: poster's replies name a condition; not quoted. |
| `NewParents-1sdksf5` | reddit-reading-mr07.md: birth trauma detail not quoted. |
| `NewParents-1sf4ldf` | reddit-reading-mr07.md: safe-sleep wording not quoted. |
| `NewParents-1sk665j` | reddit-reading-mr07.md: physical incident and abuse history in replies; not quoted. |
| `NewParents-1so0im5` | reddit-reading-mr08.md: quoted (medication line skipped) (3 quotes) |
| `NewParents-1sqlh40` | reddit-reading-mr08.md: quoted (road-safety, bed-sharing, condition and loss lines skipped) (10 quotes) |
| `NewParents-1stbhdl` | reddit-reading-mr08.md: quoted (one restricted: bed-sharing; infant medical lines skipped) (5 quotes) |
| `NewParents-1stnkb6` | reddit-reading-mr08.md: quoted (condition line skipped); likely same author as NewParents-1sr0jm1 (4 quotes) |
| `NewParents-1stvtvo` | reddit-reading-mr08.md: quoted (condition line skipped) (2 quotes) |
| `NewParents-1sv324y` | reddit-reading-mr08.md: two clean lines quoted; post centred on safe-sleep fear, rest skipped (2 quotes) |
| `NewParents-1t0logp` | reddit-reading-mr08.md: clean lines quoted; minor injury incident and bed-sharing lines skipped (3 quotes) |
| `NewParents-1t1jei7` | reddit-reading-mr08.md: clean lines quoted; bed-sharing and mattress lines skipped (2 quotes) |
| `NewParents-1t1r7np` | reddit-reading-mr08.md: quoted (infant sleep-position line skipped) (2 quotes) |
| `NewParents-1t4cpzk` | reddit-reading-mr08.md: quoted (bed-sharing and infant weight lines skipped) (3 quotes) |
| `NewParents-1t4p7op` | reddit-reading-mr08.md: clean lines quoted; condition, treatment and hospital lines skipped (3 quotes) |
| `NewParents-1t657ya` | reddit-reading-mr08.md: quoted (infant medical and bed-sharing lines skipped) (2 quotes) |
| `NewParents-1t6a4ft` | reddit-reading-mr08.md: clean lines quoted with trims; supplement and condition lines skipped (3 quotes); MR08: sm08-0326 trimmed a sleep-aid, supplement, therapy-technique or medication clause (ledger names these four ids collectively); MR08: sm08-0327 trimmed a sleep-aid, supplement, therapy-technique or medication clause (ledger names these four ids collectively) |
| `NewParents-1t8d0tm` | reddit-reading-mr08.md: quoted (bed-sharing fear lines skipped) (3 quotes) |
| `NewParents-1taib3d` | reddit-reading-mr08.md: quoted (infant medical line skipped) (4 quotes) |
| `NewParents-1tcsy5n` | reddit-reading-mr08.md: quoted; partner-asleep-with-baby incident and monitor lines skipped (4 quotes) |
| `NewParents-1tdmq89` | reddit-reading-mr08.md: quoted (bed-sharing and medication replies skipped) (4 quotes) |
| `NewParents-1w2hzuc` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `NewParents-1wajuwt` | reddit-reading-mr02.md: NewParents-1wajuwt medication lines; reddit-reading-mr02.md: the opening panic episode (NewParents-1wajuwt post) |
| `NewParents-1wbvw1q` | reddit-reading-mr02.md: "I can't do this" (NewParents-1wbvw1q) |
| `NewParents-1weebyn` | reddit-reading-mr02.md: co-sleeping risk rationalisation (NewParents-1weebyn) |
| `NewParents-1wn2qhk` | reddit-reading-mr02.md: NewParents-1wn2qhk supplement reply |
| `NewParents-1wnjxcw` | reddit-reading-mr02.md: NewParents-1wnjxcw infant pain-relief) |
| `NewParents-1wyeyva` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `NewParents-1x8lh9u` | MR03: doctor's feeding instruction withheld |
| `Parenting-1t6jf8c` | reddit-reading-mr08.md: quoted (child's medical condition skipped) (3 quotes) |
| `Postpartum_Depression-1t4rfgm` | reddit-reading-mr08.md: one clean line quoted; condition, supplement and medication content skipped (1 quotes) |
| `PregnancyUK-1vfzljj` | MR06: sm06-0231 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `PregnancyUK-1vv6qfk` | MR06: sm06-0091 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `PregnancyUK-1w21hd0` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `beyondthebump-1sa80k5` | reddit-reading-mr07.md: condition detail not quoted. |
| `beyondthebump-1sagsjh` | reddit-reading-mr07.md: medication detail not quoted. |
| `beyondthebump-1sflo8z` | reddit-reading-mr07.md: medication not quoted. |
| `beyondthebump-1sizipp` | reddit-reading-mr08.md: quoted (bereavement/anxiety passages skipped) (7 quotes) |
| `beyondthebump-1so1tbv` | reddit-reading-mr08.md: quoted (one restricted: sleep aid; bed-sharing lines skipped) (10 quotes) |
| `beyondthebump-1spz2sp` | reddit-reading-mr08.md: quoted (one restricted: supplement; sleep-aid and bed-sharing lines skipped) (10 quotes); MR08: sm08-0096 trimmed a sleep-aid, supplement, therapy-technique or medication clause (ledger names these four ids collectively) |
| `beyondthebump-1ss5jx3` | reddit-reading-mr08.md: quoted (safe-sleep and loss lines skipped) (3 quotes) |
| `beyondthebump-1swav1o` | reddit-reading-mr08.md: quoted (bed-sharing and infant medication lines skipped) (4 quotes) |
| `beyondthebump-1syjct2` | reddit-reading-mr08.md: quoted (medical test reply skipped) (3 quotes) |
| `beyondthebump-1t14mp2` | reddit-reading-mr08.md: quoted (bed-sharing lines skipped) (2 quotes) |
| `beyondthebump-1t5b2im` | reddit-reading-mr08.md: quoted (panic wording skipped) (2 quotes) |
| `beyondthebump-1tbi20l` | reddit-reading-mr08.md: quoted (road incident line skipped) (3 quotes) |
| `beyondthebump-1tep0ja` | reddit-reading-mr07.md: replies name conditions and medication; not quoted. |
| `beyondthebump-1v1qj75` | MR04: upright-sleeping question omitted |
| `beyondthebump-1va73eo` | MR06: sm06-0154 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `beyondthebump-1vq6jr3` | MR06: sm06-0028 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `beyondthebump-1w70kt8` | reddit-reading-mr02.md: substance use lines (beyondthebump-1w70kt8, BabyBumps-1wb7wqq, beyondthebump-1wfakdw); reddit-reading-mr02.md: "regret having my baby" (beyondthebump-1w70kt8) |
| `beyondthebump-1w98az8` | reddit-reading-mr02.md: "mental hospital" line (beyondthebump-1w98az8) |
| `beyondthebump-1w9e6f7` | reddit-reading-mr02.md: beyondthebump-1w9e6f7 prescription and supplement lines |
| `beyondthebump-1wdmfnd` | reddit-reading-mr02.md: beyondthebump-1wdmfnd supplement replies |
| `beyondthebump-1wfakdw` | reddit-reading-mr02.md: substance use lines (beyondthebump-1w70kt8, BabyBumps-1wb7wqq, beyondthebump-1wfakdw) |
| `beyondthebump-1wgiqdf` | reddit-reading-mr02.md: "slowly losing it" / "close to the edge" (beyondthebump-1wgiqdf, beyondthebump-1wijutx) |
| `beyondthebump-1wijutx` | reddit-reading-mr02.md: "slowly losing it" / "close to the edge" (beyondthebump-1wgiqdf, beyondthebump-1wijutx) |
| `beyondthebumpUK-1sa83vn` | reddit-reading-mr07.md: medication request not quoted. |
| `beyondthebumpUK-1srtfg9` | reddit-reading-mr08.md: clean lines quoted; condition and medication lines skipped (3 quotes) |
| `beyondthebumpUK-1synp70` | reddit-reading-mr08.md: quoted (unsafe-surface line skipped) (3 quotes) |
| `beyondthebumpUK-1tasbr7` | reddit-reading-mr08.md: quoted (bed-sharing and unsafe-surface reply skipped) (4 quotes) |
| `beyondthebumpUK-1tbkq3x` | reddit-reading-mr08.md: quoted (bed-sharing line skipped) (2 quotes) |
| `beyondthebumpUK-1vqq0gw` | MR06: sm06-0037 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `beyondthebumpUK-1vqvebt` | MR06: sm06-0038 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `beyondthebumpUK-1vsarwb` | MR06: sm06-0058 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `beyondthebumpUK-1vtuma1` | MR06: sm06-0080 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `beyondthebumpUK-1vu0n2f` | MR06: sm06-0084 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `daddit-1vcy6g3` | reddit-reading-mr06.md: the post contains a road-safety passage (a drive he does not remember). That passage was not quoted. The unit was not dropped because it is not centred on that passage; its two quotes (sm06-0156, sm06-0157) come from a later reply and are restricted. `beyondthebump-1uzdca4` was dropped whole because the incident is the whole post.; MR06: road-safety passage (unremembered drive) omitted |
| `daddit-1w8e2qa` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `daddit-1wk38pn` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `daddit-1wward4` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `postpartumprogress-1twsthz` | reddit-reading-mr07.md: medical detail not quoted. |
| `pregnant-1sjnmte` | reddit-reading-mr08.md: quoted (illness/medication lines skipped) (2 quotes) |
| `pregnant-1sjzs7m` | reddit-reading-mr08.md: quoted (medication/blood-pressure lines skipped) (3 quotes) |
| `pregnant-1sqx5x6` | reddit-reading-mr08.md: quoted (one restricted: medication; identity passage skipped) (4 quotes) |
| `pregnant-1swfvf8` | MR08: sm08-0196 trimmed a sleep-aid, supplement, therapy-technique or medication clause (ledger names these four ids collectively) |
| `pregnant-1sxrj1g` | reddit-reading-mr08.md: quoted (symptom/hospital lines skipped) (2 quotes) |
| `pregnant-1t2gzbp` | reddit-reading-mr08.md: three clean lines quoted; medication content skipped (3 quotes) |
| `pregnant-1t542oq` | reddit-reading-mr08.md: quoted (loss lines skipped) (2 quotes) |
| `pregnant-1t55ef0` | reddit-reading-mr08.md: quoted (supplement and earlier breakdown lines skipped) (3 quotes) |
| `pregnant-1ta2c6r` | reddit-reading-mr08.md: quoted once; labour-symptom content skipped (1 quotes) |
| `pregnant-1tdkyuc` | reddit-reading-mr08.md: quoted (medication line skipped) (2 quotes) |
| `pregnant-1tstj1o` | reddit-reading-mr07.md: a reply holds a past crisis reference; not quoted. |
| `pregnant-1uoadn4` | MR04: medication lines omitted |
| `pregnant-1vsm1v1` | MR06: sm06-0062 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `pregnant-1w6qzqv` | reddit-reading-mr02.md: pregnant-1w6qzqv reply naming a prescription |
| `pregnant-1w8o7j5` | reddit-reading-mr02.md: pregnant-1w8o7j5 OTC sleep-aid line |
| `pregnant-1wf33ut` | MR01: reported OB advice not fact-checked, withheld; sm01-0062 retains outcome only |
| `pregnant-1wh2z0m` | reddit-reading-mr02.md: drowsy-driving line (pregnant-1wh2z0m) |
| `pregnant-1wnd923` | reddit-reading-mr02.md: "hallucinating" wording (pregnant-1wnd923). |
| `pregnant-1wnwmfz` | reddit-reading-mr02.md: pregnant-1wnwmfz OTC suggestion |
| `pregnant-1x88a12` | MR03: sleep-position claim withheld |
| `sleeptrain-1sfamtk` | reddit-reading-mr07.md: medication not quoted. |
| `sleeptrain-1sgx8fh` | reddit-reading-mr07.md: bed-sharing detail not quoted. |
| `sleeptrain-1sn7svy` | reddit-reading-mr08.md: quoted (medical/bed-sharing item skipped) (11 quotes) |
| `sleeptrain-1t78cy6` | reddit-reading-mr08.md: quoted (one restricted: safe-sleep detail; migraine line skipped) (4 quotes) |
| `sleeptrain-1t7wfa8` | reddit-reading-mr08.md: quoted (infant illness line skipped) (2 quotes) |
| `sleeptrain-1tb1gwn` | reddit-reading-mr08.md: quoted (infant medication and medical history skipped) (2 quotes) |
| `sleeptrain-1tc68en` | reddit-reading-mr08.md: quoted (bed-sharing lines skipped) (3 quotes) |
| `sleeptrain-1tdbv3u` | reddit-reading-mr08.md: quoted (infant allergy and chest-sleep lines skipped) (2 quotes) |
| `sleeptrain-1v0b7dk` | MR06: sm06-0251 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `sleeptrain-1v0swr2` | MR06: sm06-0253 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `sleeptrain-1w2ekex` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `sleeptrain-1w731pn` | reddit-reading-mr02.md: an infant breath-holding episode (sleeptrain-1w731pn reply) |
| `sleeptrain-1wmc90a` | reddit-reading-mr02.md: toddler head-hitting (sleeptrain-1wmpqkw, sleeptrain-1wmc90a) |
| `sleeptrain-1wmpqkw` | reddit-reading-mr02.md: toddler head-hitting (sleeptrain-1wmpqkw, sleeptrain-1wmc90a) |
| `workingmoms-1ss1yof` | reddit-reading-mr08.md: quoted (condition line skipped) (3 quotes) |
| `workingmoms-1t9kltx` | reddit-reading-mr08.md: quoted (one restricted; condition and medication lines skipped) (2 quotes) |
| `workingmoms-1vrnwqm` | MR06: sm06-0039 has an extraction trim; ledger says subject clauses were trimmed but does not identify which trims; candidate for re-reading, not proof every trim censored |
| `workingmoms-1vz1jqo` | reddit-reading-mr01.md: Partial skips inside quoted units (passages left out, unit still quoted): self-described hallucinations from sleep loss (NewParents-1w2hzuc), a father's hostile thoughts about the newborn and "won't make it" wording (daddit-1wward4), a father's "spiralling"/hatred lines (daddit-1w8e2qa), "I can't do this anymore" (Mommit-1vz1a0b), medication passages (daddit-1wk38pn, workingmoms-1vz1jqo), a sibling's past medical emergency (NewParents-1wyeyva), toddler self-injury at the door (sleeptrain-1w2ekex), the OP's later update describing a medical emergency (PregnancyUK-1w21hd0 |
| `workingmoms-1wig5vv` | reddit-reading-mr02.md: a third party's bereavement in a reply (workingmoms-1wig5vv) |

### Re-reading queue

`scratchpad/unfilter-reread/queue.tsv` has the exact header `kind\tid\twhy_it_was_dropped`, one row per distinct id, with `unit` taking precedence where a post also has a known unit or a documented extraction gap. Subreddits are recovered from candidate metadata. Reasons from overlapping stages are combined. Ordinary relevance/duplicate omissions are not automatically treated as subject exclusions; ambiguous subject-related triage decisions and unnamed MR06 trims are included conservatively and labelled.

Queue: **918 rows** (236 unit, 682 post); 104 whole-unit/review candidates and 132 partially extracted/trim-candidate units; 257 triage subject candidates and 425 safety intake posts. Overlap is deduplicated by id.

## Changes made

- **486 quote records restored in full in main findings sections:** 73 previously cited without words and 413 previously uncited (478 Reddit + 8 reviews). Exact spelling, punctuation and recorded extraction ellipses are copied from `voice/*.jsonl`; no new voice records or ids were created. All 910 originally cited ids remain. The revised findings cite 1,327 distinct ids. Twelve unmarked ids explicitly withheld by the old synthesis now have their words restored too; three further anxiety-wording ids from MR08’s notes and the existing subscription-gift record are newly cited. The additional unmarked ids are sm08-0102, sm08-0107, sm08-0196 and smr1-0022.
- **Conclusions moved:** the cost includes panic, hallucinations, impairment and a reported infant fall (sm01-0148, sm06-0009, sm07-0201); bedsharing has both relief and failed-relief outcomes (sm02-0019, sm03-0048, sm08-0404, sm09-0265); mother-directed attempts include medication trade-offs, apps, free information, referrals and private therapy (sm03-0299, sm05-0260, sm07-0088, sm07-0371). Dismissal and rejected depression labels are visible beside conditions affecting either parent’s capacity (sm03-0175, sm03-0330, sm09-0226, sm09-0239). Work, driving and dusk dread sharpen the account (sm03-0309, sm08-0105, sm09-0086). The categorical standalone-product rejection is now a hypothesis: broader adult-sleep use, gift and book-buying evidence qualifies the absence claim, while no mother-specific quiz/plan purchase or tested outcome is established (smr1-0022, smr1-0044, sm06-0229). The dated closing section in findings records these movements and their words.
- **Instructions:** README and product brief now state the owner’s three-sentence research principle. Findings §12 replaces “Lines not to cross” with that principle and the evidence gap. `restricted-ids.md` keeps its complete original list under a historical title and opening paragraph; the marking has no effect. The wave-2 decision TSV remains unchanged as a historical record.
- **Tooling:** query `--exclude-restricted` and lookup `--norestr` are compatibility no-ops; output no longer imposes a marketing boundary. Both legacy findings checkers now call the shared id/quotation verifier, including its failure exit for unresolved ids or mismatched words. No shared script was edited. Merged records retain every original voice field, add `formerly_restricted`, and set all `restricted` flags false; counts identify 486 historical labels and zero active restrictions.
- **Re-reading queue:** **918 unique entries: 236 unit and 682 post**. This comprises 91 excluded Reddit units, 117 named partial omissions, 425 intake safety posts and 41 explicit triage safety drops, plus 15 uncertain MR06 trim units, 13 age/role review candidates and 216 further subject-related triage candidates. The final completeness sweep expanded the initial 144-post triage candidate scan to 257 by also checking anxiety, panic, rage, illness, injury, safe-sleep, symptom and related reasons. These additional mixed-relevance entries are candidates, not proven safety exclusions. No queued source was manually re-read.

### Every changed file (relative to `sleep-mother/`)

- `README.md`
- `_tools/query.py`
- `product/product-brief.md`
- `scratchpad/FINDINGS-W3/check17.py`
- `scratchpad/FINDINGS/check_restricted_pairs.py`
- `scratchpad/FINDINGS/q.py`
- `scratchpad/unfilter-reread/queue.tsv`
- `synthesis/counts.md`
- `synthesis/findings.md`
- `synthesis/restricted-ids.md`
- `synthesis/unfilter-report.md`
- `voice-merged/all.jsonl`

The shared `../_shared/_tools/prompt-sleep-mother-reader-w3.txt` and `brief-restricted-review-sm-w2.md` were inspected and already corrected; neither was changed. No other build, `_raw/` file, original voice file, source ledger, reader note, historical audit or historical review decision was changed. No git command, network request or push was used.

## Verification

All commands ran from the ads repository root with `python3 -I`; every command exited 0. `audit_niche.py` used `--check-only` so it did not regenerate historical audit notes. `_tools/verify_quotes.py` compared the existing extracted quote strings against their cited source files programmatically; that is a provenance check, not new reading/extraction of the queued gaps.

```text
$ python3 -I mamivio.com/research/_shared/_tools/verify_findings_ids.py mamivio.com/research/sleep-mother/synthesis/findings.md sleep-mother
1327 distinct ids cited, 0 unresolved
1246 verbatim fragments paired with an id, 0 failed
exit 0

$ python3 -I mamivio.com/research/_shared/_tools/check_ids.py sleep-mother
3005 records, 3005 distinct ids, 0 duplicated
exit 0

$ python3 -I mamivio.com/research/_shared/_tools/audit_niche.py sleep-mother read-v1 read-w2 read-w3 --check-only
{"quotes": 3005, "assigned": 1120, "units_quoted": 1026, "assigned_units_quoted": 1008, "uncited": 112, "unexplained": 0, "historically_marked": 486, "active_restrictions": 0, "safety_hits": 20}
exit 0

$ python3 -I mamivio.com/research/sleep-mother/_tools/verify_quotes.py
reddit-mr01.jsonl: 198 quotes, 0 failed
reddit-mr02.jsonl: 306 quotes, 0 failed
reddit-mr03.jsonl: 330 quotes, 0 failed
reddit-mr04.jsonl: 321 quotes, 0 failed
reddit-mr05.jsonl: 285 quotes, 0 failed
reddit-mr06.jsonl: 263 quotes, 0 failed
reddit-mr07.jsonl: 460 quotes, 0 failed
reddit-mr08.jsonl: 421 quotes, 0 failed
reddit-mr09.jsonl: 377 quotes, 0 failed
reviews-rv1.jsonl: 44 quotes, 0 failed
TOTAL 3005 quotes, 0 failed
exit 0

$ python3 -I mamivio.com/research/sleep-mother/scratchpad/FINDINGS/check_restricted_pairs.py
1327 distinct ids cited, 0 unresolved
1246 verbatim fragments paired with an id, 0 failed
exit 0

$ python3 -I mamivio.com/research/sleep-mother/scratchpad/FINDINGS-W3/check17.py
1327 distinct ids cited, 0 unresolved
1246 verbatim fragments paired with an id, 0 failed
exit 0

Additional assertions: PASS
486/486 historically marked quotes reproduced as exact complete voice records in main findings sections.
910/910 original cited ids retained; 1327 distinct ids now cited.
918 queue rows, 918 distinct ids: 236 unit, 682 post; all inventoried stage ids covered.
3005 merged records retained; 486 historical labels, 0 active restrictions; all other original voice fields unchanged.
Query --exclude-restricted and lookup --norestr leave results unchanged.
Four edited Python tools compile; both legacy checkers now run provenance checks.
Original voice files, source ledgers, reader notes, historical audits and review table unchanged by SHA-256 comparison.
```

The audit’s `units_quoted: 1026` counts distinct `raw_file` paths, which combines 1,008 assigned Reddit unit paths with 18 review corpus paths. The 44 review quotes come from 26 review units (`review_unit` metadata); do not interpret 1,026 as Reddit posts or independent people. The 112 assigned Reddit units without a voice quotation are explained in historical ledgers, including exclusions and ordinary no-quote/duplicate cases.

## Remaining uncertainty and handoff

Removing the rule cannot recover words omitted before extraction. The 91 whole Reddit exclusions, 117 named partial units, 425 safety intake posts and 41 explicit triage drops need reading; their eventual words and effect on findings are unknown. MR06’s 15 trimmed units cannot be separated into subject trims versus shortening from the ledger alone, and the 13 review age/role decisions and 216 further triage decisions mix subject and relevance; the queue preserves those reasons for the next readers. Unlogged omissions may exist. No inference about the content of the unread safety lane is made.

## Re-reading closed and findings integrated — 2026-11-16

The preceding inventory and handoff are historical. **UR01–UR04 completed all 918 assigned rows**: 905 Reddit posts/units and 13 saved reviews, with **0 missing or unfinished**. The four assignments match the queue exactly, each id assigned once. Their ledgers reconcile to 849 rows with new quotes and 69 relevance/duplicate/nothing-new results. All **1,238 quotes** (1,226 Reddit + 12 reviews) and all four “What these posts add” sections were read in full for this revision.

Findings now cite **1,583 distinct ids**, including **256 UR quotes reproduced in full**; all **1,327 previously cited ids** remain, and all **486 historically marked full quotes** remain verbatim in the main sections. Eleven new evidence subsections and the final dated section record fifteen conclusions that moved. The revision integrates weaning, institutions, disclosure/access fears, treatment and coverage trade-offs, actual incidents behind vigilance, coercion and violence, caregiver breakdown, self-harm and infant harm, separate sleep/recovery outcomes, broader spending and explicit plan requests. The proposed mother-specific plan's purchase and efficacy remain untested. Exact typography was also restored to 133 older paired fragments; no source wording was rewritten.

The existing audit rebuilt **4,243 merged records** (4,187 Reddit + 56 reviews) across fourteen voice files, with **0 active restrictions**. Its raw-file coverage differs from post coverage: 1,120 original assignments plus 905 UR Reddit identities, overlapping 223, give **1,802 distinct Reddit identities recorded as read**; 1,719 supply quotes and 83 do not. All 91 whole reader exclusions and 132 partial/trim candidates in the queue are covered, as are all 425 intake safety posts and 257 subject-related triage candidates. Some conservative candidates did not prove censorship; the reader ledgers retain that distinction.

**Nothing in the assigned re-reading queue remains unread.** Ordinary full-read gaps remain: **1,646 tier-A, 3,694 tier-B and 882 tier-C posts** (6,222 available bodies), plus 32 removed/deleted bodies. `sources/reddit.md` gives the identity subtraction method. Actual UR source reads were 343 frozen units with available OP replies, 562 archive-only title/body records and 13 reviews; archive reads cannot supply absent replies. Unlogged earlier omissions may exist. Reported events, diagnoses and treatment outcomes remain attributed accounts rather than independently established causes or effects.

Changed for this integration: `README.md`, `synthesis/findings.md`, `synthesis/counts.md`, `sources/reddit.md`, this report, `voice-merged/all.jsonl` and `synthesis/audit-safety-hits.tsv`. The generated regex-hit list is descriptive; the historical spot-check worksheet was preserved by diverting only its generated output in memory. All 27 original voice/reader-ledger files were checked unchanged. No raw file, shared tool, other build or reader output was changed; no network or git was used.

### Integration checks (all exit 0)

Run from `mamivio.com/research/`:

```text
python3 -I _shared/_tools/verify_findings_ids.py sleep-mother/synthesis/findings.md sleep-mother
1583 distinct ids cited, 0 unresolved
1486 verbatim fragments paired with an id, 0 failed

python3 -I _shared/_tools/check_ids.py sleep-mother
4243 records, 4243 distinct ids, 0 duplicated

python3 -I _shared/_tools/audit_niche.py sleep-mother read-v1 read-w2 read-w3 --check-only
{"quotes": 4243, "assigned": 1120, "units_quoted": 1246, "assigned_units_quoted": 1098, "uncited": 22, "unexplained": 0, "historically_marked": 486, "active_restrictions": 0, "safety_hits": 144}
```

The unchanged local `_tools/verify_quotes.py` was run with an in-memory raw loader decoding JSONL posts and review JSON. Its literal serialized-file loader does not interpret JSON escapes; neither the source nor the tool was edited. A separate strict check matches each UR quote only to its own decoded post, cited unit or identified review block, without normalization. Additional checks include short paired fragments omitted by the stock findings check, full quote reproduction, previous-id retention, ledger totals, derived-record equality and protected-file hashes.

```text
Strict UR source check: 1238 quotes, 0 failed.
Build source verifier with decoded JSON loader: TOTAL 4243 quotes, 0 failed.
Exact findings check: 1493 all-length paired fragments, 0 failed.
Citation preservation: 1327/1327 previous ids; 256/256 cited UR quotes reproduced in full.
Historical restoration preservation: 486/486 full quotes remain in main findings.
Queue and ledger reconciliation: 918/918 distinct assigned ids, 1238 quotes, 69 zero-new-quote rows.
Merged integrity: 4243/4243 records preserved; only audit flags differ; 0 active restrictions.
Protected-file integrity: 27 voice/reader-ledger files and historical spot-check unchanged.
```

Historical inconsistencies are preserved and explained: triage notes say 15 wave-1 safety drops, TSVs have 16; MR04’s narrative says 147 restrictions, its old flag list has 235; the earlier review later reduced wave-2 labels to 103. No old labels remain active. Current evidence broadens the research conclusion but establishes neither prevalence nor paid demand or efficacy for the proposed product.
