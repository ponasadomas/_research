# Toddler-behaviour unfilter report — 2026-11-16

Initial inventory written before changing findings, instructions or tools. Scope: `toddler-behaviour/` only; no network, git, raw mutations or raw-unit re-reading. All counts are records, ids or units, never people or prevalence. Reader notes, source ledgers and run logs remain historical records.

## Verified baseline, by stage

- **Intake / triage:** `_raw/reddit/filter-v1/safety-candidates.jsonl` contains **806 distinct posts** routed away from A/B/C by the old safety tier. The frozen triage TSVs contain **131 explicit `safety:` drops** and **305 additional subject-related review candidates** (436 total), retaining mixed off-age/off-topic reasons rather than assuming all were censorship. Metadata in `filter-v1/index.jsonl` resolves their subreddits; no source bodies were re-read. These sets and reader omissions overlap and must not be added without deduplication. A second metadata sweep also checked illness, fever, rash, choking, hospital/dental material and explicit mental-health labels; this found 100 of the additional mixed-reason candidates beyond the first keyword pass. The shared `niche_filter.py` has already been corrected; frozen intake is not regenerated.
- **Reading / quote extraction:** all 27 `sources/reddit-reading-trNN.md` ledgers and their `synthesis/reader-notes-trNN.md` were inspected. Named omissions concern adult yelling, restraint and punishment, child self-injury, bodily and hygiene topics, diagnosis/assessment, medical treatment and medication, family medical history, bereavement and parents' own mental health. Some exclusions mix subject and ordinary relevance reasons; the queue preserves the recorded reason. TR21 withdrew **28 ids from seven units** after review; they are not reissued. See the unit lists below.
- **Marking:** `synthesis/restricted-ids.md` contains **683 unique ids**, all resolving among **9,293 voice records**: **678 Reddit + 5 review ids**. Its repeated tb03-0297 and tb06-0008 entries do not add ids. The original derived `voice-merged/all.jsonl` actively flagged all 683. Original voice files have 399 legacy `restricted` fields: 34 true (13 tb24 and 21 tb26) and 365 false; none has `marketing_eligible=false`. The 34 true ids are all in the 683-id historical list. Original quote files and these legacy labels are preserved byte-for-byte; the README makes their historical, non-enforcing status explicit. Regeneration sets all merged `restricted` flags false and adds `formerly_restricted`.
- **Findings:** the baseline text mentions **978 distinct ids** (including plain ids and endpoint ids), but only **30** of the 683 historical ids; **653** are completely absent. Historical labels in §16 additionally suppress ids that the final list no longer flags. The old wave-2 set was 301, later reduced to 148; that is a parsing/marking history, not a change in what the source said. No current restriction is justified by that discrepancy. The opening guidance, §6.3, §12, wave summaries, price tables and method/check sections instruct or demonstrate withholding words.
- **Tooling / instructions:** `README.md` and `product/product-brief.md` require subject exclusions. `_tools/query.py` offers `--exclude-restricted` using `marketing_eligible=false` (zero such records now) and prints an eligibility warning. `scratchpad/FINDINGS/strict_check.py`, `FINDINGS-W2/strict_check_w2.py` and `FINDINGS-W3/strict_check_w3.py` report quotation/bracket citations as forbidden and demand restriction labels; W3 additionally suppresses TR19/TR21's unmarked not-for-hooks ranges. They check fragments too; those provenance checks must remain. The three `FINDINGS*/q.py` helpers display an active restriction label and also skip marked ids with `--norestr`; those skips have been removed and the legacy option is now a no-op. Historical extraction specs/builders and `avoid.txt`/range/category analyses record the old choices; they cannot recover unsaved words and must not be used to rebuild the corpus. `verify_findings_ids.py`, `check_ids.py` and local `_tools/verify_quotes.py` check ids/provenance, not subject.
- **Shared tools, read only:** the owner says these were corrected on 2026-11-16. Inspection confirms the current `brief-reading.md`, `brief-findings.md`, `brief-triage.md`, `audit_niche.py`, `niche_filter.py` and `prompt-toddler-reader-w3.txt` preserve evidence irrespective of subject. The toddler prompt is already corrected, so no shared file needs changing. No shared script is edited.

## Historical recovery inventory — now completed (see closing section)

Removing a rule cannot restore words never saved into `voice/*.jsonl`. The following named units have either no saved quote or documented partial extraction; their raw words, missing quote count and any change to conclusions cannot be established without re-reading. No raw unit was re-read for this task. Quote verification may read existing quotes' sources mechanically, which does not extract missing material.

The metadata inventory names **319 no-quote units** and **810 partially quoted units**. These are named omission/review candidates, not a claim that every mixed-reason exclusion was solely censorship. It also queues **152 marked-unit reviews** where no precise omitted passage was logged, and **90 further TR06 units** because its ledger says medical treatment lines were left out ‘everywhere’. That latter statement cannot identify which specific units lost medical words; the assignment is queued to locate them.

The re-reading queue is [`../scratchpad/unfilter-reread/queue.tsv`](../scratchpad/unfilter-reread/queue.tsv): **2,647 distinct ids, 1,406 unit rows and 1,241 post rows**, with the three requested columns and no duplicate ids. Unit takes precedence when a post also has a named reading omission. Reasons retain file and line provenance; review-only entries explicitly say an omission is not proven. The 806 intake posts and all 436 subject-related triage candidates are covered.

### No saved quote

- `reddit-reading-tr01.md` (7): `daddit-1wt7us8`, `daddit-1wu1zqm`, `pottytraining-1we1zcm`, `pottytraining-1wxjvk7`, `pottytraining-1x11c1h`, `toddlers-1w7jnxm`, `toddlers-1wulqnd`.
- `reddit-reading-tr02.md` (9): `AttachmentParenting-1x1r7dk`, `Mommit-1w09q4e`, `Parenting-1vznzvg`, `Parenting-1w1kza3`, `Parenting-1w1yrpk`, `toddlers-1vxn344`, `toddlers-1vxw7wq`, `toddlers-1w09u8y`, `toddlers-1w2ikfq`.
- `reddit-reading-tr03.md` (4): `daddit-1w5ki1d`, `toddlers-1w2xl9d`, `toddlers-1w4zt1g`, `toddlers-1w53tmc`.
- `reddit-reading-tr04.md` (8): `Mommit-1waczd6`, `Mommit-1wcql62`, `NewParents-1wanby0`, `Parenting-1wdped0`, `toddlers-1wbms70`, `toddlers-1wc7cnz`, `toddlers-1wdiagj`, `toddlers-1we6oc3`.
- `reddit-reading-tr05.md` (8): `GentleParenting-1wgbb6x`, `Parenting-1wl28fn`, `ScienceBasedParenting-1wkswms`, `pottytraining-1wfghxn`, `pottytraining-1wg3jw2`, `pottytraining-1wgbf4i`, `pottytraining-1widuzi`, `toddlers-1wk6fcm`.
- `reddit-reading-tr06.md` (12): `AttachmentParenting-1wrbzv7`, `GentleParenting-1woktb4`, `Mommit-1wmjy6e`, `Mommit-1wmzpxp`, `Mommit-1wo47jn`, `Parenting-1wpsf6f`, `pottytraining-1wohb94`, `pottytraining-1wpkwcp`, `pottytraining-1wrrht0`, `toddlers-1wn77j1`, `toddlers-1wo4549`, `toddlers-1wp3bpb`.
- `reddit-reading-tr07.md` (10): `GentleParenting-1wxd3s7`, `Mommit-1wu8bct`, `NewParents-1wyp4lh`, `Parenting-1wvl32h`, `daddit-1wsrvts`, `sahm-1ws8mm3`, `toddlers-1wscdk0`, `toddlers-1wut7ny`, `toddlers-1wxanhg`, `toddlers-1wzkc4n`.
- `reddit-reading-tr08.md` (29): `GentleParenting-1x127sh`, `Mommit-1x1htbj`, `Mommit-1x4ad4h`, `Mommit-1x4lhra`, `NewParents-1x2afe8`, `NewParents-1x2lx82`, `NewParents-1x49te7`, `Parenting-1x1cfwl`, `Parenting-1x4bc0t`, `Parenting-1x4h86d`, `Parenting-1x4z67c`, `daddit-1x37a7c`, `pottytraining-1x04527`, `pottytraining-1x1w04k`, `pottytraining-1x3kr2u`, `sahm-1x52gkf`, `toddlers-1wzyh85`, `toddlers-1wzzqvq`, `toddlers-1x0t4cn`, `toddlers-1x0zsqw`, `toddlers-1x14ycp`, `toddlers-1x1wlcj`, `toddlers-1x1ylnw`, `toddlers-1x2ru4w`, `toddlers-1x37av8`, `toddlers-1x3drd7`, `toddlers-1x4aijb`, `toddlers-1x4hwou`, `toddlers-1x511zs`.
- `reddit-reading-tr09.md` (11): `GentleParenting-1x8tzjs`, `Mommit-1x5jima`, `Mommit-1x67ezs`, `Mommit-1x7w4pp`, `Parenting-1xbuher`, `daddit-1x61usp`, `daddit-1xcjw54`, `toddlers-1x6rwhz`, `toddlers-1xbq8e1`, `toddlers-1xc6nx5`, `toddlers-1xeagyj`.
- `reddit-reading-tr10.md` (10): `Parenting-1ugd6ra`, `Parenting-1uw76km`, `daddit-1ui40gi`, `daddit-1v5nu9q`, `pottytraining-1uu2khi`, `pottytraining-1uvuacw`, `toddlers-1ufb395`, `toddlers-1ug4mmy`, `toddlers-1un7twc`, `toddlers-1us1ijf`.
- `reddit-reading-tr11.md` (26): `AttachmentParenting-1ukoqvz`, `AttachmentParenting-1vrjpua`, `Mommit-1ufrdp8`, `Mommit-1ugatki`, `Mommit-1ugq6a4`, `Mommit-1uhludz`, `Mommit-1ui9f8j`, `Mommit-1vi5csd`, `Mommit-1vl1964`, `NewParents-1ui66if`, `Parenting-1uf9rwi`, `Parenting-1uhgvoy`, `Parenting-1uie6r7`, `Parenting-1uizcct`, `Parenting-1vjo0c2`, `pottytraining-1uj8pgy`, `pottytraining-1vnfocm`, `toddlers-1ugufhf`, `toddlers-1uh8vji`, `toddlers-1uielge`, `toddlers-1uitkjk`, `toddlers-1uiu6pl`, `toddlers-1uj3d3w`, `toddlers-1ujcu5v`, `toddlers-1vog0pn`, `toddlers-1vr2i2f`.
- `reddit-reading-tr12.md` (15): `Mommit-1un7ecx`, `Mommit-1upeex0`, `Mommit-1uphmor`, `NewParents-1umsxv9`, `Parenting-1uq1mfj`, `pottytraining-1umosig`, `pottytraining-1uncvzs`, `pottytraining-1uogolt`, `pottytraining-1upfeqr`, `pottytraining-1uqfz7f`, `toddlers-1um0jah`, `toddlers-1umulj2`, `toddlers-1upe37e`, `toddlers-1uqdkni`, `toddlers-1ur9amm`.
- `reddit-reading-tr13.md` (7): `FirstTimeMom-1uz7pkb`, `pottytraining-1uz5qbr`, `toddlers-1ussovb`, `toddlers-1uu53zs`, `toddlers-1uw5ojc`, `toddlers-1ux1k0s`, `toddlers-1uxpjjd`.
- `reddit-reading-tr14.md` (8): `AttachmentParenting-1v6elva`, `daddit-1v7kcsj`, `pottytraining-1v50bac`, `toddlers-1v2hxjj`, `toddlers-1v37wtj`, `toddlers-1v3iwea`, `toddlers-1v3tvh8`, `toddlers-1v7nr7g`.
- `reddit-reading-tr15.md` (20): `GentleParenting-1ve0yjn`, `GentleParenting-1velmm0`, `Mommit-1v9dibs`, `Mommit-1vc4l41`, `NewParents-1veo2ax`, `NewParents-1vfkxcx`, `Parenting-1vachuz`, `Parenting-1vekr2v`, `ScienceBasedParenting-1vd4x0w`, `daddit-1vcuuuq`, `pottytraining-1vcwwqi`, `toddlers-1v8zg1p`, `toddlers-1vb9h2o`, `toddlers-1vben98`, `toddlers-1vc3x5t`, `toddlers-1vck8vd`, `toddlers-1vdo0jk`, `toddlers-1vdyrd5`, `toddlers-1vev33u`, `toddlers-1veys99`.
- `reddit-reading-tr16.md` (3): `GentleParenting-1vjdehl`, `toddlers-1via0zo`, `toddlers-1vnk7uo`.
- `reddit-reading-tr17.md` (11): `GentleParenting-1vr9883`, `Mommit-1vrcubp`, `Mommit-1vsd2bs`, `Mommit-1vujdt5`, `Mommit-1vwotm2`, `daddit-1voapqe`, `daddit-1vwkrpo`, `pottytraining-1vtv89s`, `toddlers-1vpz4a7`, `toddlers-1vqxbtb`, `toddlers-1vxc9zj`.
- `reddit-reading-tr18.md` (9): `AttachmentParenting-1sc03fh`, `Mommit-1sq4gvt`, `Parenting-1smp1ie`, `Parenting-1sqpq5a`, `pottytraining-1si47cd`, `pottytraining-1tll3ap`, `toddlers-1ss091o`, `toddlers-1t6m0cq`, `toddlers-1u3jpre`.
- `reddit-reading-tr19.md` (16): `AttachmentParenting-1tyqevi`, `Mommit-1sbmnpz`, `Mommit-1tgytkk`, `Mommit-1u8ef3z`, `Parenting-1s9yh7d`, `Parenting-1tiw6su`, `pottytraining-1sa2sj7`, `pottytraining-1sb2r9s`, `toddlers-1sa33u0`, `toddlers-1sak4br`, `toddlers-1sblk8f`, `toddlers-1sdeo1y`, `toddlers-1sdkuxx`, `toddlers-1u1enx8`, `toddlers-1uc8tib`, `workingmoms-1sc37w2`.
- `reddit-reading-tr20.md` (14): `Mommit-1sge68i`, `Mommit-1skjyx3`, `Mommit-1sklk2a`, `Parenting-1sg1m9y`, `ScienceBasedParenting-1sf1yc9`, `toddlers-1sf501m`, `toddlers-1sfaagh`, `toddlers-1shayeg`, `toddlers-1shty2k`, `toddlers-1shy5ko`, `toddlers-1si3n5a`, `toddlers-1si4ju1`, `toddlers-1sjkrhh`, `toddlers-1skm57w`.
- `reddit-reading-tr21.md` (20): `AttachmentParenting-1sosxay`, `Mommit-1sr9afi`, `NewParents-1sqic71`, `NewParents-1svn06c`, `Parenting-1soeqoy`, `Parenting-1stocy4`, `Parenting-1suvgb2`, `pottytraining-1sojuk4`, `pottytraining-1sp513a`, `pottytraining-1sqwywk`, `toddlers-1smpweu`, `toddlers-1sn2696`, `toddlers-1solau1`, `toddlers-1soopky`, `toddlers-1sq2c9i`, `toddlers-1sq3huk`, `toddlers-1sraugr`, `toddlers-1srml5t`, `toddlers-1ssaiw1`, `toddlers-1sszkx2`.
- `reddit-reading-tr22.md` (6): `Mommit-1t3xvzt`, `Parenting-1t0kjq9`, `pottytraining-1t2q3l2`, `toddlers-1swnu4p`, `toddlers-1t3kg0x`, `toddlers-1t3uter`.
- `reddit-reading-tr23.md` (9): `GentleParenting-1tcmwpv`, `Mommit-1tcjs1j`, `Mommit-1thn5j7`, `Parenting-1taavyj`, `daddit-1t5t1xl`, `daddit-1tgn5a1`, `toddlers-1tamm4z`, `toddlers-1tbe593`, `toddlers-1tbo2t7`.
- `reddit-reading-tr24.md` (13): `Mommit-1ti79s7`, `Mommit-1tjotup`, `Mommit-1tk4z1u`, `Mommit-1tkellz`, `Parenting-1thsjdb`, `daddit-1tn7p9m`, `pottytraining-1tk1o2d`, `toddlers-1ti7ivf`, `toddlers-1tk2xhb`, `toddlers-1tle5lr`, `toddlers-1tniijm`, `toddlers-1to0dam`, `toddlers-1to9773`.
- `reddit-reading-tr25.md` (9): `GentleParenting-1tslxq7`, `Mommit-1txk1bv`, `Parenting-1tvqvon`, `sahm-1txdm5c`, `toddlers-1tqmtn5`, `toddlers-1trjn38`, `toddlers-1tsl3du`, `toddlers-1tysj5y`, `toddlers-1tythlq`.
- `reddit-reading-tr26.md` (18): `Mommit-1u736vp`, `Parenting-1tz28pq`, `Parenting-1u36789`, `Parenting-1u7376i`, `Parenting-1u7r6u6`, `pottytraining-1u1osdv`, `pottytraining-1u4u2bc`, `pottytraining-1u86rvj`, `pottytraining-1u8t2f1`, `toddlers-1tzlb9i`, `toddlers-1u2kxyo`, `toddlers-1u2nbor`, `toddlers-1u3gjp6`, `toddlers-1u472h9`, `toddlers-1u53ofv`, `toddlers-1u6fq30`, `toddlers-1u7qc2w`, `toddlers-1u8il4j`.
- `reddit-reading-tr27.md` (7): `Parenting-1uccmb4`, `Parenting-1ucxyrg`, `daddit-1ubsclz`, `daddit-1ubyfgd`, `toddlers-1u9qzga`, `toddlers-1uc8r9p`, `toddlers-1uczlb0`.

### Partial extraction

- `reader-notes-tr01.md` (1): `toddlers-1x0rwq8`.
- `reader-notes-tr02.md` (1): `toddlers-1vzpv86`.
- `reader-notes-tr06.md` (2): `Mommit-1wmcbn6`, `pottytraining-1wnmutd`.
- `reader-notes-tr10.md` (1): `Parenting-1v4hulj`.
- `reader-notes-tr19.md` (7): `pottytraining-1samym7`, `pottytraining-1sborci`, `pottytraining-1tna7tw`, `toddlers-1sbgv0d`, `toddlers-1sc6ubf`, `toddlers-1u6zm76`, `toddlers-1uee2jv`.
- `reddit-reading-tr01.md` (18): `Mommit-1w588xl`, `Mommit-1wxuezh`, `Mommit-1wy9247`, `Parenting-1w068sr`, `pottytraining-1wbxja3`, `pottytraining-1wdm05y`, `pottytraining-1wo7j3r`, `pottytraining-1wogizw`, `pottytraining-1x9gxlr`, `sahm-1w03794`, `sahm-1wbq40s`, `toddlers-1vzk7cx`, `toddlers-1w5fts3`, `toddlers-1wef4lj`, `toddlers-1wks1w5`, `toddlers-1wsh09m`, `toddlers-1ww50it`, `workingmoms-1w5s6m4`.
- `reddit-reading-tr02.md` (21): `Mommit-1vzgzgz`, `Mommit-1w1tloh`, `pottytraining-1vy72x4`, `pottytraining-1vzv8ky`, `pottytraining-1w181q3`, `pottytraining-1w2fe36`, `pottytraining-1xb6gf5`, `toddlers-1vyl0oz`, `toddlers-1vzut6j`, `toddlers-1vzvwt9`, `toddlers-1vzzbnz`, `toddlers-1w08gaz`, `toddlers-1w08jgj`, `toddlers-1w1bt8l`, `toddlers-1w1q3b4`, `toddlers-1w1sjmj`, `toddlers-1w2ayjn`, `toddlers-1w2k1tz`, `toddlers-1w2sg00`, `toddlers-1xcr7r1`, `workingmoms-1xdop35`.
- `reddit-reading-tr03.md` (30): `AttachmentParenting-1w4h0de`, `Mommit-1w4qcc6`, `Mommit-1w4tbac`, `Mommit-1w5ax16`, `Mommit-1w5e91p`, `Mommit-1w5p27u`, `Mommit-1w79yt1`, `Mommit-1w84d6f`, `NewParents-1w7agpl`, `NewParents-1w857bz`, `Parenting-1w3x4qa`, `Parenting-1w3ys2g`, `Parenting-1w8aobo`, `daddit-1w6q4ou`, `daddit-1w6z3o3`, `pottytraining-1w3s65h`, `pottytraining-1w4hs1o`, `pottytraining-1w5lvbr`, `pottytraining-1w7a6kg`, `pottytraining-1w7p65x`, `toddlers-1w2tubz`, `toddlers-1w3wp5z`, `toddlers-1w4b8y5`, `toddlers-1w4sc66`, `toddlers-1w4ykhe`, `toddlers-1w5dxqh`, `toddlers-1w5zxiz`, `toddlers-1w7jzth`, `toddlers-1w7mr94`, `toddlers-1w8jf4x`.
- `reddit-reading-tr04.md` (36): `GentleParenting-1wdtry7`, `Mommit-1w8lqum`, `Mommit-1w9bfid`, `Mommit-1w9upan`, `Mommit-1wa62uo`, `Mommit-1wb101z`, `Mommit-1wb7hog`, `Mommit-1wbp05s`, `NewParents-1wcw04f`, `Parenting-1w8qkal`, `Parenting-1wb6po5`, `Parenting-1wcqbn0`, `Parenting-1wcyip6`, `Parenting-1wd2kru`, `pottytraining-1w8xdsw`, `pottytraining-1w9uc38`, `pottytraining-1wa6vrt`, `pottytraining-1wao5nq`, `pottytraining-1wc81f7`, `pottytraining-1wcrjg5`, `pottytraining-1wdi4vc`, `pottytraining-1we8hmz`, `toddlers-1w8tw41`, `toddlers-1w98mua`, `toddlers-1w9czvn`, `toddlers-1wa8sju`, `toddlers-1wadek3`, `toddlers-1wah9y6`, `toddlers-1wayx8a`, `toddlers-1wb2e5h`, `toddlers-1wbrsbn`, `toddlers-1wd21ln`, `toddlers-1we1c11`, `toddlers-1we2lva`, `toddlers-1weaqe0`, `toddlers-1ween3y`.
- `reddit-reading-tr05.md` (18): `Mommit-1wfkg57`, `Mommit-1wi6bz4`, `Mommit-1wkmm0r`, `Mommit-1wl28kq`, `Parenting-1wk1vbm`, `pottytraining-1wg8rs8`, `pottytraining-1wgd1ew`, `pottytraining-1wgfago`, `pottytraining-1win1yt`, `pottytraining-1winem5`, `toddlers-1weuudd`, `toddlers-1weywox`, `toddlers-1wfqlb5`, `toddlers-1wfqunt`, `toddlers-1wg9hgc`, `toddlers-1whk8p1`, `toddlers-1wk0cug`, `toddlers-1wlmn4k`.
- `reddit-reading-tr06.md` (5): `Mommit-1wpt1c7`, `Parenting-1wn9vm1`, `Parenting-1wrkvtj`, `toddlers-1wo1ft8`, `toddlers-1woogpe`.
- `reddit-reading-tr07.md` (21): `AttachmentParenting-1wz7u41`, `AttachmentParenting-1wzf1is`, `Mommit-1wst3cs`, `Mommit-1wwrnot`, `Mommit-1wxjhbk`, `NewParents-1wvxkjn`, `NewParents-1wwup2q`, `Parenting-1wxu5m2`, `ScienceBasedParenting-1wyocf0`, `pottytraining-1wwfeer`, `pottytraining-1www285`, `pottytraining-1wyv95d`, `toddlers-1wtazjq`, `toddlers-1wtk0vm`, `toddlers-1wuok9p`, `toddlers-1wvbptm`, `toddlers-1wvztw3`, `toddlers-1wxrprh`, `toddlers-1wyg4n3`, `toddlers-1wyqm2s`, `toddlers-1wzitwd`.
- `reddit-reading-tr08.md` (28): `AttachmentParenting-1x56nge`, `Mommit-1x0cebc`, `Mommit-1x0nhlw`, `Mommit-1x22zx1`, `Mommit-1x4hwqo`, `NewParents-1x2tjsf`, `Parenting-1x09x8o`, `Parenting-1x3li4n`, `Parenting-1x49jv3`, `ScienceBasedParenting-1x191hu`, `daddit-1x0bqmd`, `daddit-1x3d7l7`, `pottytraining-1wzwkqo`, `pottytraining-1wzxpob`, `pottytraining-1x0p8du`, `pottytraining-1x15nid`, `pottytraining-1x1or17`, `pottytraining-1x47c30`, `pottytraining-1x4avnp`, `pottytraining-1x4b6rb`, `pottytraining-1x5450n`, `toddlers-1x1976q`, `toddlers-1x1qcp6`, `toddlers-1x1vb86`, `toddlers-1x2krbo`, `toddlers-1x2l5nn`, `toddlers-1x2xq32`, `toddlers-1x53owd`.
- `reddit-reading-tr09.md` (40): `AttachmentParenting-1xdh7m1`, `Mommit-1x5bctn`, `Mommit-1x9fa96`, `Mommit-1xahz2o`, `Mommit-1xbslkx`, `Mommit-1xdc7lp`, `Parenting-1x7iugj`, `Parenting-1x9e1gl`, `daddit-1xa6kyj`, `pottytraining-1x5789k`, `pottytraining-1x5rfpm`, `pottytraining-1x65jbb`, `pottytraining-1x6s9ff`, `pottytraining-1x72wqm`, `pottytraining-1x7kfd3`, `pottytraining-1x7qpud`, `pottytraining-1x8e5a1`, `pottytraining-1x8k8hd`, `pottytraining-1x97w9y`, `pottytraining-1xa5fy7`, `pottytraining-1xb1pbo`, `pottytraining-1xb4ur1`, `pottytraining-1xctjn1`, `pottytraining-1xe3xao`, `sahm-1x6uo2p`, `sahm-1xdqj43`, `toddlers-1x5dt4i`, `toddlers-1x5hepy`, `toddlers-1x5tvsv`, `toddlers-1x66z9b`, `toddlers-1x6c5mp`, `toddlers-1x8yug9`, `toddlers-1xagsdc`, `toddlers-1xaqyxx`, `toddlers-1xb8u6l`, `toddlers-1xboxrj`, `toddlers-1xbs0hn`, `toddlers-1xc4flb`, `toddlers-1xdftke`, `toddlers-1xek4ko`.
- `reddit-reading-tr10.md` (15): `Parenting-1vbv7ak`, `daddit-1uwfc0c`, `daddit-1vfpv1h`, `pottytraining-1ukzeb5`, `pottytraining-1uws4j9`, `pottytraining-1uzczf7`, `pottytraining-1v1o2tq`, `pottytraining-1v2ylps`, `pottytraining-1v5v7ph`, `pottytraining-1v6be1h`, `pottytraining-1v8n700`, `sahm-1v9axzd`, `toddlers-1uk0vsn`, `toddlers-1vccdbq`, `toddlers-1vcsx5y`.
- `reddit-reading-tr11.md` (29): `GentleParenting-1vr5r6u`, `Mommit-1ugd2so`, `Mommit-1uj8avu`, `Mommit-1vmsx37`, `Parenting-1uflu90`, `Parenting-1ufm5u7`, `daddit-1uipynj`, `pottytraining-1ufao07`, `pottytraining-1uio85r`, `pottytraining-1uj3qa5`, `pottytraining-1ujtzmj`, `pottytraining-1uk6ska`, `pottytraining-1vila5v`, `pottytraining-1vuraa4`, `toddlers-1ug3idd`, `toddlers-1ugayob`, `toddlers-1ugpsy8`, `toddlers-1uhbq1y`, `toddlers-1uhzrzd`, `toddlers-1uif16s`, `toddlers-1uj4nb1`, `toddlers-1vk0pc0`, `toddlers-1vlqm5b`, `toddlers-1vmnfbf`, `toddlers-1vnukzq`, `toddlers-1vrctli`, `toddlers-1vsgkhs`, `toddlers-1vsyrhw`, `toddlers-1vws6w2`.
- `reddit-reading-tr12.md` (27): `Mommit-1upx56q`, `Mommit-1urb1i2`, `Parenting-1umbaxf`, `Parenting-1un4myu`, `Parenting-1up1qx3`, `Parenting-1uqex49`, `daddit-1uo8rjp`, `daddit-1upv1zr`, `pottytraining-1ulgzdk`, `pottytraining-1um0iaq`, `pottytraining-1un8dl4`, `pottytraining-1unl5e8`, `pottytraining-1unpoa6`, `pottytraining-1unqhzu`, `pottytraining-1up2x8u`, `pottytraining-1up5y2z`, `pottytraining-1upfe44`, `pottytraining-1uprfpb`, `toddlers-1um5f7y`, `toddlers-1umbziv`, `toddlers-1un4s8c`, `toddlers-1unzekj`, `toddlers-1uoalek`, `toddlers-1uor2k7`, `toddlers-1upbely`, `toddlers-1uqcojh`, `workingmoms-1upvasp`.
- `reddit-reading-tr13.md` (54): `AttachmentParenting-1uv3yay`, `Mommit-1urvomw`, `Mommit-1utxirw`, `Mommit-1uypu5f`, `Parenting-1us0hiv`, `Parenting-1us99gb`, `Parenting-1ut4m25`, `Parenting-1utc2j5`, `Parenting-1utwxol`, `Parenting-1uupz68`, `Parenting-1uvfj4g`, `Parenting-1uxdrpr`, `Parenting-1uy1cow`, `Parenting-1uy8l3w`, `Parenting-1uz78r2`, `daddit-1uu3vsg`, `daddit-1uxzdw8`, `daddit-1uyb41c`, `pottytraining-1us4v80`, `pottytraining-1us7tb6`, `pottytraining-1us8mq6`, `pottytraining-1utltlo`, `pottytraining-1uu2ni8`, `pottytraining-1uu4zum`, `pottytraining-1uuumqo`, `pottytraining-1uve6zu`, `pottytraining-1uvsvgy`, `pottytraining-1uvtfk6`, `pottytraining-1uxglpb`, `sahm-1uuh8k3`, `sahm-1uvhct9`, `toddlers-1urixt4`, `toddlers-1urnuce`, `toddlers-1us50l8`, `toddlers-1us5v4i`, `toddlers-1usup5w`, `toddlers-1uszfzl`, `toddlers-1ut0shr`, `toddlers-1ut1gjj`, `toddlers-1utxg2u`, `toddlers-1uvi699`, `toddlers-1uvraoy`, `toddlers-1uvy6q1`, `toddlers-1uw44bz`, `toddlers-1uwh1b4`, `toddlers-1uwrolo`, `toddlers-1ux265s`, `toddlers-1uxfkwk`, `toddlers-1uxsu38`, `toddlers-1uybesz`, `toddlers-1uykpv4`, `toddlers-1uytl58`, `toddlers-1uz254q`, `toddlers-1uz4l27`.
- `reddit-reading-tr14.md` (59): `AttachmentParenting-1v5i3dg`, `GentleParenting-1v2um1k`, `Mommit-1uz889p`, `Mommit-1uzvbyr`, `Mommit-1v0ezhq`, `Mommit-1v5bj5x`, `Mommit-1v5hxgm`, `Mommit-1v5qoze`, `Mommit-1v6o9lo`, `Mommit-1v7xu7l`, `NewParents-1v2o8or`, `Parenting-1v0syl5`, `Parenting-1v2w2q9`, `Parenting-1v5xjyu`, `Parenting-1v6at04`, `Parenting-1v6ecoc`, `Parenting-1v6hmts`, `Parenting-1v6uhiz`, `Parenting-1v79e1k`, `Parenting-1v7w8kd`, `ScienceBasedParenting-1v7fsa5`, `daddit-1v07d3y`, `daddit-1v4hgqe`, `daddit-1v4n0xh`, `daddit-1v6bd4t`, `daddit-1v7anhe`, `pottytraining-1v03oi8`, `pottytraining-1v0lh58`, `pottytraining-1v1grwl`, `pottytraining-1v2bmqg`, `pottytraining-1v2uvvi`, `pottytraining-1v3ziou`, `pottytraining-1v4kh6k`, `pottytraining-1v6m7kj`, `toddlers-1uzmvxu`, `toddlers-1uzu6ar`, `toddlers-1v0ebso`, `toddlers-1v0w5rl`, `toddlers-1v1191e`, `toddlers-1v1mb4g`, `toddlers-1v2qd2c`, `toddlers-1v2r685`, `toddlers-1v2rwcq`, `toddlers-1v2se28`, `toddlers-1v2t8ht`, `toddlers-1v3w255`, `toddlers-1v4f7f2`, `toddlers-1v4quxm`, `toddlers-1v4y43j`, `toddlers-1v5my9p`, `toddlers-1v5t7ur`, `toddlers-1v663qm`, `toddlers-1v698yz`, `toddlers-1v6cewu`, `toddlers-1v6ujm8`, `toddlers-1v7he91`, `toddlers-1v7hzsz`, `toddlers-1v87lfi`, `workingmoms-1v0rm1v`.
- `reddit-reading-tr15.md` (32): `Mommit-1vbuaqc`, `Mommit-1vfkz0l`, `NewParents-1vc6xvu`, `NewParents-1vfihqm`, `Parenting-1vdngo5`, `daddit-1vc7fpo`, `daddit-1vduwig`, `pottytraining-1v9duog`, `pottytraining-1vagqrt`, `pottytraining-1vanih6`, `pottytraining-1vcaf61`, `pottytraining-1vcxgsz`, `pottytraining-1vd3mzu`, `pottytraining-1vdjxhu`, `pottytraining-1vdpuky`, `pottytraining-1vectox`, `toddlers-1v96dfl`, `toddlers-1v9ftlt`, `toddlers-1v9iftv`, `toddlers-1va2a9s`, `toddlers-1va6t7b`, `toddlers-1vazhiu`, `toddlers-1vbsmgv`, `toddlers-1vctr98`, `toddlers-1vcyc0f`, `toddlers-1vd53nw`, `toddlers-1vdpnnu`, `toddlers-1vegi9b`, `toddlers-1vf1hct`, `toddlers-1vfgruu`, `toddlers-1vfljal`, `toddlers-1vg2y0g`.
- `reddit-reading-tr16.md` (49): `AttachmentParenting-1vl1bec`, `Mommit-1vgj21m`, `Mommit-1vhl6ea`, `Mommit-1vmkb32`, `Mommit-1vnd18y`, `Mommit-1vnirg5`, `NewParents-1vg7xxb`, `NewParents-1vg99ac`, `NewParents-1vh7o2w`, `NewParents-1vkwh2n`, `Parenting-1vjkvv2`, `Parenting-1vjqzov`, `Parenting-1vkiqsv`, `Parenting-1vlikdq`, `daddit-1vizzae`, `pottytraining-1vgs57e`, `pottytraining-1vigi3j`, `pottytraining-1vj2npp`, `pottytraining-1vk0t3g`, `pottytraining-1vkl15h`, `pottytraining-1vkptt1`, `pottytraining-1vkq7p8`, `pottytraining-1vlewjy`, `pottytraining-1vmizm3`, `pottytraining-1vn8l2i`, `pottytraining-1vnnqcn`, `sahm-1vgjm2m`, `sahm-1vi10j8`, `sahm-1vl0vnn`, `sahm-1vlsfad`, `sahm-1vnb4tm`, `toddlers-1vgekgi`, `toddlers-1vjdmpr`, `toddlers-1vjdwjs`, `toddlers-1vjvbcd`, `toddlers-1vjwv18`, `toddlers-1vk5zs7`, `toddlers-1vk89o0`, `toddlers-1vk9uqe`, `toddlers-1vlipn3`, `toddlers-1vlvtag`, `toddlers-1vlw413`, `toddlers-1vmf7lo`, `toddlers-1vmh67s`, `toddlers-1vmm83t`, `toddlers-1vmneck`, `toddlers-1vmww9u`, `toddlers-1vn6byq`, `toddlers-1vna98z`.
- `reddit-reading-tr17.md` (65): `AttachmentParenting-1vwiah0`, `GentleParenting-1vpes8q`, `GentleParenting-1vpgqhu`, `Mommit-1vocz4s`, `Mommit-1vt5h85`, `NewParents-1vrlsr3`, `NewParents-1vs8049`, `NewParents-1vwsr8z`, `Parenting-1vpd7f2`, `Parenting-1vpklb4`, `Parenting-1vqtlr3`, `Parenting-1vr5pte`, `Parenting-1vrx2ft`, `Parenting-1vssvr1`, `Parenting-1vun3fa`, `Parenting-1vw937o`, `ScienceBasedParenting-1vuipdd`, `pottytraining-1vo5e13`, `pottytraining-1voiytq`, `pottytraining-1vokagb`, `pottytraining-1voypwi`, `pottytraining-1vpa1u7`, `pottytraining-1vpgjuh`, `pottytraining-1vpjtuc`, `pottytraining-1vpmlq1`, `pottytraining-1vq4jf9`, `pottytraining-1vqtw8r`, `pottytraining-1vrnep7`, `pottytraining-1vrwuob`, `pottytraining-1vs222w`, `pottytraining-1vt6f4m`, `pottytraining-1vuj6cr`, `pottytraining-1vummea`, `pottytraining-1vuo75k`, `pottytraining-1vuohxk`, `pottytraining-1vupr9i`, `pottytraining-1vvivfh`, `pottytraining-1vvofju`, `pottytraining-1vxabut`, `pottytraining-1vxavvu`, `toddlers-1vo3elv`, `toddlers-1vo3zl5`, `toddlers-1vokss7`, `toddlers-1voqu1k`, `toddlers-1vp5ghx`, `toddlers-1vpdb3w`, `toddlers-1vqdhtk`, `toddlers-1vqln21`, `toddlers-1vqsl41`, `toddlers-1vqtz8n`, `toddlers-1vqw181`, `toddlers-1vqx9sm`, `toddlers-1vr4yku`, `toddlers-1vrwzs7`, `toddlers-1vs7sr0`, `toddlers-1vs8ap0`, `toddlers-1vsqq7a`, `toddlers-1vt401p`, `toddlers-1vu35ap`, `toddlers-1vuaybc`, `toddlers-1vush3z`, `toddlers-1vv9l93`, `toddlers-1vvlts5`, `toddlers-1vvr09i`, `toddlers-1vwbavc`.
- `reddit-reading-tr18.md` (14): `Mommit-1sdddcy`, `Mommit-1t2qp5i`, `Mommit-1ta03do`, `daddit-1snfcs4`, `daddit-1sohfy5`, `daddit-1t7p509`, `pottytraining-1so97mg`, `pottytraining-1t5vt7g`, `pottytraining-1u39l8m`, `toddlers-1sgcybr`, `toddlers-1sjy8bn`, `toddlers-1snabch`, `toddlers-1sp86mi`, `toddlers-1u9ye3q`.
- `reddit-reading-tr19.md` (14): `GentleParenting-1tk397u`, `GentleParenting-1tnip1z`, `Mommit-1sa3qsf`, `Mommit-1ue3daz`, `pottytraining-1ubdb0n`, `toddlers-1s9quxt`, `toddlers-1sbzr1c`, `toddlers-1sco5go`, `toddlers-1scpah1`, `toddlers-1td5t64`, `toddlers-1thrsjc`, `toddlers-1tn7aue`, `toddlers-1u786ja`, `toddlers-1udzurp`.
- `reddit-reading-tr21.md` (56): `AttachmentParenting-1sox6qq`, `AttachmentParenting-1st7yym`, `Mommit-1soif5o`, `Mommit-1sq5lqx`, `Mommit-1sqyv0e`, `Mommit-1sr7ot5`, `Mommit-1sr9tqr`, `Mommit-1srr2rt`, `Mommit-1srw01k`, `Mommit-1sso2c9`, `Mommit-1ssthtt`, `Mommit-1sswqax`, `Mommit-1st5q9c`, `Mommit-1stba2k`, `NewParents-1snxfis`, `NewParents-1st9qab`, `NewParents-1stoi7a`, `Parenting-1snhzhx`, `Parenting-1souh48`, `Parenting-1sp95yf`, `Parenting-1sq62pf`, `Parenting-1ss0ydu`, `Parenting-1stm14a`, `Parenting-1stxhne`, `Parenting-1su1l1g`, `Parenting-1suktb2`, `Parenting-1sveao5`, `daddit-1sup697`, `pottytraining-1spy08x`, `pottytraining-1ssdhwe`, `pottytraining-1stlbg7`, `sahm-1sul9w4`, `toddlers-1slplzl`, `toddlers-1sn6884`, `toddlers-1so8rsg`, `toddlers-1sp3qmv`, `toddlers-1spahuy`, `toddlers-1spwazj`, `toddlers-1spwuij`, `toddlers-1sqjmse`, `toddlers-1sqso1n`, `toddlers-1sqwk6x`, `toddlers-1sqx5a0`, `toddlers-1sraisk`, `toddlers-1srmwz8`, `toddlers-1srrwks`, `toddlers-1ssu328`, `toddlers-1st46wx`, `toddlers-1stm63q`, `toddlers-1stoscd`, `toddlers-1stx8ac`, `toddlers-1su64pz`, `toddlers-1svk7oj`, `toddlers-1svwwgv`, `toddlers-1sw113s`, `workingmoms-1sw1dvo`.
- `reddit-reading-tr22.md` (44): `GentleParenting-1syyr5e`, `Mommit-1swo3gx`, `Mommit-1sz835i`, `Mommit-1t3l45v`, `Parenting-1sxdvan`, `Parenting-1sxiopq`, `Parenting-1sy8wa2`, `Parenting-1sza889`, `Parenting-1szf3fo`, `Parenting-1t19m46`, `Parenting-1t34hlh`, `Parenting-1t5k6o6`, `Parenting-1t5od3i`, `daddit-1syk4k4`, `daddit-1t0rrjr`, `daddit-1t4sdh9`, `pottytraining-1sxeo9j`, `pottytraining-1sxhvug`, `pottytraining-1sxkckj`, `pottytraining-1t02lll`, `pottytraining-1t19xsl`, `pottytraining-1t2xqcp`, `pottytraining-1t4sq2c`, `sahm-1t3p3xr`, `toddlers-1sw9vlp`, `toddlers-1swfifb`, `toddlers-1swg3lk`, `toddlers-1swhohq`, `toddlers-1sxv6t2`, `toddlers-1symp78`, `toddlers-1szanb9`, `toddlers-1szxdvn`, `toddlers-1szz2r5`, `toddlers-1t05us2`, `toddlers-1t13bju`, `toddlers-1t1x5o3`, `toddlers-1t2498j`, `toddlers-1t2h7ux`, `toddlers-1t2x3tq`, `toddlers-1t3nfak`, `toddlers-1t44s5s`, `toddlers-1t51hak`, `toddlers-1t5b2zy`, `toddlers-1t5dob6`.
- `reddit-reading-tr23.md` (44): `AttachmentParenting-1t94007`, `AttachmentParenting-1tbwz7r`, `AttachmentParenting-1tdhmjk`, `Mommit-1t5rzss`, `Mommit-1t8bx6e`, `Mommit-1t94k70`, `Mommit-1t9r72a`, `Mommit-1ta6p83`, `Mommit-1tdgd54`, `Mommit-1teg35w`, `Mommit-1thqggt`, `Parenting-1t6xgqn`, `Parenting-1t8rixn`, `Parenting-1ta6y4v`, `Parenting-1taov6y`, `Parenting-1tbtc8m`, `Parenting-1tdhcxt`, `Parenting-1tfnr08`, `Parenting-1tg1hld`, `pottytraining-1t9kkpd`, `pottytraining-1td2hst`, `pottytraining-1tf7n7w`, `pottytraining-1tfwl1d`, `pottytraining-1th7bqy`, `toddlers-1t6g000`, `toddlers-1t6mnyt`, `toddlers-1t7fjjf`, `toddlers-1t7nywf`, `toddlers-1t899n6`, `toddlers-1ta77tu`, `toddlers-1tabdxz`, `toddlers-1tah1c5`, `toddlers-1tb8s2n`, `toddlers-1tbcp62`, `toddlers-1tbl79f`, `toddlers-1tcgxv4`, `toddlers-1tew8p3`, `toddlers-1tffhfi`, `toddlers-1tfnfwe`, `toddlers-1tfsuae`, `toddlers-1tgb81o`, `toddlers-1tgu7kf`, `toddlers-1th02b2`, `toddlers-1th9bmz`.
- `reddit-reading-tr24.md` (22): `FirstTimeMom-1tlf3gw`, `GentleParenting-1tpy5vf`, `NewParents-1ti9yd0`, `NewParents-1tknseh`, `NewParents-1tnmwpf`, `Parenting-1tnkz9i`, `Parenting-1tp11ia`, `Parenting-1tpwbed`, `pottytraining-1thvtiz`, `pottytraining-1tjp9js`, `pottytraining-1toosif`, `pottytraining-1tpkmk1`, `toddlers-1tk0bu6`, `toddlers-1tlzrxy`, `toddlers-1tm7h81`, `toddlers-1tmb3m2`, `toddlers-1tmiby4`, `toddlers-1tmmsm6`, `toddlers-1tnkjxx`, `toddlers-1to6o7x`, `toddlers-1tofsv5`, `toddlers-1tpklkt`.
- `reddit-reading-tr25.md` (6): `pottytraining-1ty37jo`, `pottytraining-1tyi8iw`, `toddlers-1ts9dbu`, `toddlers-1tt0bdk`, `toddlers-1tvadix`, `toddlers-1typv1n`.
- `reddit-reading-tr26.md` (31): `AttachmentParenting-1u71bhn`, `NewParents-1u2t5ah`, `NewParents-1u3ymp9`, `Parenting-1tzztcr`, `Parenting-1u1862e`, `Parenting-1u3cfjh`, `Parenting-1u6g3eh`, `Parenting-1u6u0x5`, `daddit-1u4swnw`, `daddit-1u6wb7q`, `pottytraining-1u0dx75`, `pottytraining-1u1oj81`, `pottytraining-1u22z90`, `pottytraining-1u2k1vt`, `pottytraining-1u7fbqh`, `pottytraining-1u8pud8`, `sahm-1u7q2j4`, `toddlers-1u0rb7r`, `toddlers-1u1dm13`, `toddlers-1u35v7b`, `toddlers-1u4aml0`, `toddlers-1u4log0`, `toddlers-1u52t4s`, `toddlers-1u540az`, `toddlers-1u582ii`, `toddlers-1u58kpr`, `toddlers-1u5zzm8`, `toddlers-1u6fjxz`, `toddlers-1u7al3r`, `toddlers-1u7h2m1`, `toddlers-1u87xvf`.
- `reddit-reading-tr27.md` (20): `Mommit-1uc6vok`, `Mommit-1uc9lgn`, `NewParents-1u9dj6r`, `NewParents-1ue315b`, `Parenting-1u9zvmo`, `Parenting-1ucp2ey`, `Parenting-1ud0z16`, `Parenting-1ud8819`, `pottytraining-1u9sb67`, `pottytraining-1ua0vmi`, `pottytraining-1ucorn0`, `pottytraining-1udjou5`, `pottytraining-1ueg7lv`, `toddlers-1u9rs9g`, `toddlers-1ua1hv4`, `toddlers-1ua2ok8`, `toddlers-1uad7kv`, `toddlers-1ucth4b`, `toddlers-1ucza5q`, `toddlers-1udqx6q`.

### marked-unit review

- `synthesis/restricted-ids.md` (152): `AttachmentParenting-1sicefc`, `AttachmentParenting-1x3etnd`, `Mommit-1sedkoe`, `Mommit-1tgbtyi`, `Mommit-1toq9qh`, `Mommit-1tsqmtf`, `Mommit-1tsxd8s`, `Mommit-1tuce40`, `Mommit-1txxyjv`, `Mommit-1uxo9uu`, `Mommit-1valhe4`, `Mommit-1vdvone`, `Mommit-1vhv3c9`, `Mommit-1vmqjgm`, `Mommit-1wng2t4`, `Mommit-1wqdvmw`, `Mommit-1ww7j96`, `Mommit-1ww9ldk`, `Mommit-1wyf99w`, `NewParents-1sjjyyz`, `NewParents-1swlu8s`, `NewParents-1tr9wly`, `NewParents-1uyk9bi`, `NewParents-1wp1399`, `Parenting-1sh7n68`, `Parenting-1tmjk47`, `Parenting-1ubcugr`, `Parenting-1udqnt9`, `Parenting-1ue649o`, `Parenting-1up9sfj`, `Parenting-1ur98gw`, `Parenting-1uydjlr`, `Parenting-1uz9ggm`, `Parenting-1wsceqc`, `Parenting-1wvyd0l`, `ScienceBasedParenting-1t1ntuw`, `ScienceBasedParenting-1wse0kj`, `daddit-1sx3wk8`, `daddit-1tw5dki`, `daddit-1u94ngy`, `daddit-1ubwznh`, `daddit-1upifzs`, `daddit-1v2iy67`, `daddit-1vi46dg`, `daddit-1wj3lcs`, `daddit-1wog4h5`, `daddit-1wujh4x`, `pottytraining-1sf9m95`, `pottytraining-1siv2vx`, `pottytraining-1sjr6a6`, `pottytraining-1sn5rh0`, `pottytraining-1szrg3o`, `pottytraining-1tco6dt`, `pottytraining-1ti8onq`, `pottytraining-1tkrr8z`, `pottytraining-1tmljdn`, `pottytraining-1u36fde`, `pottytraining-1u8rsuk`, `pottytraining-1unzu9h`, `pottytraining-1upeid1`, `pottytraining-1vkurok`, `pottytraining-1w5tp13`, `pottytraining-1wlqva3`, `sahm-1u2h9vs`, `sahm-1u4cpur`, `toddlers-1s9ib1z`, `toddlers-1san0ul`, `toddlers-1sbxb95`, `toddlers-1scgzpk`, `toddlers-1sdkpsc`, `toddlers-1sdmmdw`, `toddlers-1sfbqu7`, `toddlers-1sfcx5a`, `toddlers-1sfdhmi`, `toddlers-1sfdy9i`, `toddlers-1sffva5`, `toddlers-1sfgh5n`, `toddlers-1sfsv4o`, `toddlers-1sfzb7z`, `toddlers-1shuzw7`, `toddlers-1shz64u`, `toddlers-1sine8k`, `toddlers-1sio6lg`, `toddlers-1siun7v`, `toddlers-1skb11i`, `toddlers-1skpitj`, `toddlers-1sl89si`, `toddlers-1squym3`, `toddlers-1swnm7k`, `toddlers-1sy4n54`, `toddlers-1sycn09`, `toddlers-1t37s5g`, `toddlers-1t3ucqo`, `toddlers-1t6i1og`, `toddlers-1t8cyoi`, `toddlers-1t8guw9`, `toddlers-1td10pv`, `toddlers-1tgzxug`, `toddlers-1tj1cye`, `toddlers-1tk6duh`, `toddlers-1tkvedj`, `toddlers-1tlfjf4`, `toddlers-1tmkmqc`, `toddlers-1toay0p`, `toddlers-1tww5c9`, `toddlers-1tx7lfq`, `toddlers-1u08pfb`, `toddlers-1u0tfa1`, `toddlers-1u29ge3`, `toddlers-1u32hw9`, `toddlers-1u43edt`, `toddlers-1u71kn7`, `toddlers-1u8o5gl`, `toddlers-1uagzoh`, `toddlers-1ul3p7g`, `toddlers-1ulblvt`, `toddlers-1umtk1e`, `toddlers-1un04va`, `toddlers-1uq6zai`, `toddlers-1uri3ak`, `toddlers-1uz5zsg`, `toddlers-1v3y2mr`, `toddlers-1v4hht0`, `toddlers-1v64iq2`, `toddlers-1v6k68u`, `toddlers-1v84a88`, `toddlers-1v9vmp0`, `toddlers-1vhnmea`, `toddlers-1vzz9ia`, `toddlers-1w25b3g`, `toddlers-1w8dg6o`, `toddlers-1wgc0vd`, `toddlers-1wierp2`, `toddlers-1wldw20`, `toddlers-1wmin1h`, `toddlers-1wmoelf`, `toddlers-1wmrpi0`, `toddlers-1wn0uww`, `toddlers-1wnpcvk`, `toddlers-1wo8fkk`, `toddlers-1woap15`, `toddlers-1womkxx`, `toddlers-1wpf0cp`, `toddlers-1wrk29r`, `toddlers-1wrumkl`, `toddlers-1wspjah`, `toddlers-1wte89d`, `toddlers-1wuef1k`, `toddlers-1wvbw5x`, `toddlers-1ww5936`, `toddlers-1wxeek7`, `toddlers-1x02vqv`.

### unitemised review

- `reddit-reading-tr06.md` (90): `AttachmentParenting-1wnkrek`, `AttachmentParenting-1wpafxo`, `AttachmentParenting-1wqn6fx`, `Mommit-1wmo8gu`, `Mommit-1wntokd`, `Mommit-1woeyo9`, `Mommit-1womvwq`, `Mommit-1wp6u8w`, `Mommit-1wpf193`, `NewParents-1wnghqd`, `NewParents-1wqc85w`, `NewParents-1wre8jt`, `Parenting-1wlpqo4`, `Parenting-1wm78lh`, `Parenting-1wmsuef`, `Parenting-1wmzt2g`, `Parenting-1wnr5nx`, `Parenting-1wo7kkl`, `Parenting-1wq0zxr`, `Parenting-1wr0fuv`, `Parenting-1wrodc7`, `daddit-1wnrpu8`, `daddit-1woj9ih`, `pottytraining-1wlnxcf`, `pottytraining-1wlqrqm`, `pottytraining-1wlwikf`, `pottytraining-1wmbiwn`, `pottytraining-1wmboen`, `pottytraining-1wmkmz2`, `pottytraining-1wni94c`, `pottytraining-1wo841i`, `pottytraining-1wocw3v`, `pottytraining-1wofcor`, `pottytraining-1wogyy6`, `pottytraining-1wohr3j`, `pottytraining-1wp8fdu`, `pottytraining-1wplk5a`, `pottytraining-1wpywtl`, `pottytraining-1wq0uu4`, `pottytraining-1wqym57`, `pottytraining-1wrlson`, `pottytraining-1wrqeiz`, `pottytraining-1wrru80`, `pottytraining-1wrstfi`, `sahm-1wnq14f`, `toddlers-1wlw1bq`, `toddlers-1wlwhgi`, `toddlers-1wmc2eh`, `toddlers-1wmd5ho`, `toddlers-1wmfty4`, `toddlers-1wmidqs`, `toddlers-1wmlctt`, `toddlers-1wmo5rd`, `toddlers-1wmt2xo`, `toddlers-1wmubri`, `toddlers-1wmv9hz`, `toddlers-1wmx300`, `toddlers-1wmxfcd`, `toddlers-1wn0hns`, `toddlers-1wn1xbh`, `toddlers-1wn7vav`, `toddlers-1wnf1ko`, `toddlers-1wnh6ku`, `toddlers-1wnigln`, `toddlers-1wnjyse`, `toddlers-1wnn7y2`, `toddlers-1wnn8eg`, `toddlers-1wo37g2`, `toddlers-1wo6f5p`, `toddlers-1wovdpj`, `toddlers-1woy4lx`, `toddlers-1wpgop1`, `toddlers-1wpu9wf`, `toddlers-1wpvj2j`, `toddlers-1wq1c8a`, `toddlers-1wq9w36`, `toddlers-1wqd1hs`, `toddlers-1wqea7e`, `toddlers-1wqevs5`, `toddlers-1wqfm5j`, `toddlers-1wqg2ho`, `toddlers-1wqhp4u`, `toddlers-1wqnyoh`, `toddlers-1wqoek3`, `toddlers-1wqpavw`, `toddlers-1wqywi7`, `toddlers-1wr8mnb`, `toddlers-1wru48v`, `workingmoms-1wmls2k`, `workingmoms-1wrpoo7`.

### Review-stage gaps (35 review units)

`sources/reviews.md:47` records **31 unquoted review units** among the 121 read, with aggregate reasons including an adult's medical condition and older-child/custody detail, as well as ordinary thin/off-topic reasons. It does not map the reason to individual ids. The queue includes all 31 as review candidates so the subject-based omissions cannot be lost; it does not claim all 31 were censored. Ids were recovered solely from `REVIEW` headers and compared with `review_id`/`raw_file` in the voice records; no review body was re-read. The five marked quote ids belong to four further review units, queued for possible omitted context even though every saved quote has been restored.

- `apple-us-we-customer-review-272` — `_raw/books/apple-happiest-toddler-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `apple-us-we-customer-review-1376` — `_raw/books/apple-how-to-talk-little-kids-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `apple-us-we-customer-review-255` — `_raw/books/apple-hunt-gather-parent-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `barnes-846603623` — `_raw/books/barnes-happiest-toddler-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `barnes-842712228` — `_raw/books/barnes-whole-brain-child-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `barnes-843612391` — `_raw/books/barnes-whole-brain-child-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `aiparentingcoach-ca-10138473526` — `_raw/reviews/aiparentingcoach-ca-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `aiparentingcoach-gb-10135414079` — `_raw/reviews/aiparentingcoach-gb-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `aiparentingcoach-us-12030953927` — `_raw/reviews/aiparentingcoach-us-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-au-11528661777` — `_raw/reviews/goodinside-au-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-au-11550117074` — `_raw/reviews/goodinside-au-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-au-11551560103` — `_raw/reviews/goodinside-au-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-au-11557373908` — `_raw/reviews/goodinside-au-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-au-12311079072` — `_raw/reviews/goodinside-au-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-ca-13368715086` — `_raw/reviews/goodinside-ca-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-ca-13633123058` — `_raw/reviews/goodinside-ca-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-ca-14616039226` — `_raw/reviews/goodinside-ca-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-gb-11544080080` — `_raw/reviews/goodinside-gb-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-gb-11550652178` — `_raw/reviews/goodinside-gb-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-gb-11555467960` — `_raw/reviews/goodinside-gb-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `goodinside-gb-13411570985` — `_raw/reviews/goodinside-gb-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `granny-us-10566017623` — `_raw/reviews/granny-us-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `granny-us-10566857122` — `_raw/reviews/granny-us-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-au-6994554779` — `_raw/reviews/pottywhiz-au-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-ca-11628011418` — `_raw/reviews/pottywhiz-ca-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-ca-6445303884` — `_raw/reviews/pottywhiz-ca-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-gb-5748219975` — `_raw/reviews/pottywhiz-gb-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-gb-6062255467` — `_raw/reviews/pottywhiz-gb-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-us-6920289309` — `_raw/reviews/pottywhiz-us-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-us-7095121715` — `_raw/reviews/pottywhiz-us-corpus.txt` (unquoted review; individual drop reason unrecorded).
- `pottywhiz-us-8103259276` — `_raw/reviews/pottywhiz-us-corpus.txt` (unquoted review; individual drop reason unrecorded).

Further marked review units: `apple-ca-we-customer-review-1380`, `apple-us-we-customer-review-796`, `pottywhiz-gb-6717351083`, `pottywhiz-us-12229336842`.

## Restoration and changed conclusions

**774 full saved quotations restored to the main topical sections:** all **683 final-list ids** (30 formerly mentioned, 653 entirely omitted), **15 further ids labelled in the older findings but absent from the final list**, and **76 additional ids from the TR19/TR21 unit-level guard lists**. The old guard contained 77 ids: one was already in the 683-id list. Four of those guarded TR19 accounts had previously been cited; the rest had been omitted. No voice id or quote changed. All **978 previously named ids** remain; findings now name **1,703** resolved ids. The shared bracket-citation verifier counts **1,679** because it does not count plain ids; this is a syntax difference, not unresolved evidence.

The older labelled ids are `tb14-0018`, `tb14-0022`, `tb14-0025`, `tb14-0059`, `tb14-0161`, `tb14-0184`, `tb14-0209`, `tb14-0258`, `tb14-0259`, `tb17-0080`, `tb17-0081`, `tb17-0200`, `tb17-0219`, `tb17-0260`, `tb17-0419`. The four previously cited TR19 accounts are `tb19-0260`, `tb19-0371`, `tb19-0372`, `tb19-0373`. All 77 ids in the retired W3 unit guard are now fully quoted in topical sections: `tb19-0075`, `tb19-0076`, `tb19-0077`, `tb19-0078`, `tb19-0079`, `tb19-0095`, `tb19-0096`, `tb19-0097`, `tb19-0104`, `tb19-0105`, `tb19-0110`, `tb19-0111`, `tb19-0112`, `tb19-0113`, `tb19-0121`, `tb19-0122`, `tb19-0123`, `tb19-0124`, `tb19-0125`, `tb19-0152`, `tb19-0153`, `tb19-0154`, `tb19-0155`, `tb19-0156`, `tb19-0157`, `tb19-0158`, `tb19-0255`, `tb19-0256`, `tb19-0257`, `tb19-0258`, `tb19-0259`, `tb19-0260`, `tb19-0261`, `tb19-0262`, `tb19-0263`, `tb19-0264`, `tb19-0265`, `tb19-0266`, `tb19-0346`, `tb19-0347`, `tb19-0348`, `tb19-0349`, `tb19-0350`, `tb19-0371`, `tb19-0372`, `tb19-0373`, `tb19-0374`, `tb19-0383`, `tb19-0384`, `tb19-0385`, `tb19-0386`, `tb19-0387`, `tb19-0388`, `tb19-0389`, `tb21-0070`, `tb21-0071`, `tb21-0143`, `tb21-0144`, `tb21-0145`, `tb21-0146`, `tb21-0194`, `tb21-0274`, `tb21-0275`, `tb21-0276`, `tb21-0282`, `tb21-0304`, `tb21-0305`, `tb21-0306`, `tb21-0307`, `tb21-0308`, `tb21-0309`, `tb21-0341`, `tb21-0342`, `tb21-0343`, `tb21-0344`, `tb21-0372`, `tb21-0373`. Quotes were inserted programmatically from the voice `quote` fields after reading them, with interpretation separately written. The all-774 exact-text assertion covers full multiline and nested-quotation records that a fragment regex may only partially inspect.

The conclusions that moved, with the full account in the dated closing section of `findings.md`:

- The parent-state portrait now includes yelling, punishment, panic, resentment, impaired connection and wanting to escape, including fathers' accounts. The earlier claim that acted-out rage was entirely absent was too strong (`tb05-0047`, `tb09-0090`, `tb20-0085`, `tb13-0022`, `tb15-0233`). Missing raw passages still prevent any prevalence conclusion.
- Household fit includes prematurity/hospital history, sensory overload, postpartum strain, communication needs and travel, alongside work and housing (`tb01-0007`, `tb16-0125`, `tb20-0031`, `tb25-0255`, `tb26-0367`). Picky eating receives a main section because weight loss, underweight concerns and conflicting feeding advice sharpen that problem (`tb07-0133`–`tb07-0138`, `tb22-0047`, `tb26-0090`).
- Daycare pressure can connect assessment, expulsion and loss of work; accommodation and negotiated underwear policies remain contrary evidence (`tb02-0035`, `tb02-0036`, `tb18-0367`, `tb19-0231`, `tb06-0008`, `tb19-0373`).
- Paid behaviour help is sparse rather than absent: a Good Inside app subscription is explicit (`tb23-0311`). A coach consumes half a grocery budget (`tb09-0168`); an UpAiry buyer notices repeated Facebook promotion and reports failure (`tb09-0255`, `tb09-0256`). These do not establish demand for Mamivio.
- Referral is not the end of the research or a demonstrated solution: waiting, generic reassurance, non-specific therapy, failure to transfer home and cost matter (`tb20-0083`, `tb17-0092`, `tb17-0093`, `tb24-0134`, `tb22-0249`, `tb24-0276`). The statement that the only prices were childcare is corrected.
- Family conflict includes explicit pressure to hit and rejection of the parents' own childhood model, beyond a stricter/softer split (`tb05-0083`, `tb06-0046`, `tb03-0297`, `tb20-0154`, `tb27-0035`). Reassurance/solidarity and a paid plan are different asks (`tb14-0018`, `tb14-0259`).
- The review comparison includes a shared paid subscription, supplement use, a claimed four-week success, an objection to forcing toilet use and a counselling account (`tbr1-0058`, `tbr1-0059`, `tbr1-0076`, `tbr1-0128`, `tbr1-0134`). These remain reports, not verified effects.

The opening guidance, §12, product brief, README and competitor instructions now apply the owner's principle. Historical counts/method statements are labelled as historical. Synthetic objection headings are explicitly interpretations, with quotation marks removed so they cannot be mistaken for verbatim source words. The 683-id list retains every original list entry and its historical reasons under a retired title and first paragraph.

## Files changed

**27 files**, all under `toddler-behaviour/`:

- `README.md`
- `_tools/query.py`
- `competitors/README.md`
- `competitors/big-little-feelings.md`
- `competitors/go-potty.md`
- `competitors/good-inside.md`
- `competitors/mary-barbera.md`
- `competitors/mindnest-bloomlittle.md`
- `competitors/nurtured-first.md`
- `competitors/oh-crap.md`
- `competitors/saphire.md`
- `competitors/unconstipated-kids.md`
- `competitors/upairy.md`
- `product/product-brief.md`
- `scratchpad/FINDINGS/q.py`
- `scratchpad/FINDINGS/strict_check.py`
- `scratchpad/FINDINGS-W2/q.py`
- `scratchpad/FINDINGS-W2/strict_check_w2.py`
- `scratchpad/FINDINGS-W3/q.py`
- `scratchpad/FINDINGS-W3/strict_check_w3.py`
- `scratchpad/unfilter-reread/queue.tsv`
- `synthesis/audit-safety-hits.tsv`
- `synthesis/counts.md`
- `synthesis/findings.md`
- `synthesis/restricted-ids.md`
- `synthesis/unfilter-report.md`
- `voice-merged/all.jsonl`

No shared file was changed: the toddler reader prompt was already corrected. No other build, `_raw/` file, source ledger, reader note, original voice file, run log or historical spot-check was edited. `audit_niche.py` regenerated counts, descriptive safety-hit metadata and the merged copy; its regenerated spot-check was byte-identical to the original.

## Verification

All commands below exited **0**. Commands are shown from the repository root. Raw quote checks are mechanical provenance checks against already-extracted evidence; no missing raw material was interpreted or extracted.

```sh
python3 -I mamivio.com/research/_shared/_tools/verify_findings_ids.py mamivio.com/research/toddler-behaviour/synthesis/findings.md toddler-behaviour
```

```text
1679 distinct ids cited, 0 unresolved
1425 verbatim fragments paired with an id, 0 failed
```

```sh
python3 -I mamivio.com/research/_shared/_tools/check_ids.py toddler-behaviour
```

```text
9293 records, 9293 distinct ids, 0 duplicated
```

```sh
python3 -I mamivio.com/research/_shared/_tools/audit_niche.py toddler-behaviour read-v1 read-w2 read-w3
```

```text
{"quotes": 9293, "assigned": 3583, "units_quoted": 3176, "uncited": 435, "unexplained": 0, "historically_marked": 683, "active_restrictions": 0, "safety_hits": 60, "hits_without_historical_mark": 50, "relabeled": 3}
```

```sh
python3 -I mamivio.com/research/_shared/_tools/audit_niche.py toddler-behaviour read-v1 read-w2 read-w3 --check-only
```

```text
{"quotes": 9293, "assigned": 3583, "units_quoted": 3176, "assigned_units_quoted": 3148, "uncited": 435, "unexplained": 0, "historically_marked": 683, "active_restrictions": 0, "safety_hits": 60}
```

```sh
python3 -I mamivio.com/research/toddler-behaviour/_tools/verify_quotes.py
```

```text
reddit-tr01.jsonl: 215 quotes, 0 failed
reddit-tr02.jsonl: 270 quotes, 0 failed
reddit-tr03.jsonl: 306 quotes, 0 failed
reddit-tr04.jsonl: 304 quotes, 0 failed
reddit-tr05.jsonl: 286 quotes, 0 failed
reddit-tr06.jsonl: 284 quotes, 0 failed
reddit-tr07.jsonl: 342 quotes, 0 failed
reddit-tr08.jsonl: 287 quotes, 0 failed
reddit-tr09.jsonl: 303 quotes, 0 failed
reddit-tr10.jsonl: 324 quotes, 0 failed
reddit-tr11.jsonl: 245 quotes, 0 failed
reddit-tr12.jsonl: 284 quotes, 0 failed
reddit-tr13.jsonl: 357 quotes, 0 failed
reddit-tr14.jsonl: 339 quotes, 0 failed
reddit-tr15.jsonl: 296 quotes, 0 failed
reddit-tr16.jsonl: 434 quotes, 0 failed
reddit-tr17.jsonl: 490 quotes, 0 failed
reddit-tr18.jsonl: 392 quotes, 0 failed
reddit-tr19.jsonl: 389 quotes, 0 failed
reddit-tr20.jsonl: 292 quotes, 0 failed
reddit-tr21.jsonl: 356 quotes, 0 failed
reddit-tr22.jsonl: 435 quotes, 0 failed
reddit-tr23.jsonl: 430 quotes, 0 failed
reddit-tr24.jsonl: 378 quotes, 0 failed
reddit-tr25.jsonl: 497 quotes, 0 failed
reddit-tr26.jsonl: 378 quotes, 0 failed
reddit-tr27.jsonl: 246 quotes, 0 failed
reviews-rv1.jsonl: 134 quotes, 0 failed
TOTAL 9293 quotes, 0 failed
```

```sh
python3 -I mamivio.com/research/toddler-behaviour/scratchpad/FINDINGS/strict_check.py mamivio.com/research/toddler-behaviour/synthesis/findings.md
```

```text
1703 ids, 0 unresolved; checked 1496 fragments, 0 failed
```

```sh
python3 -I mamivio.com/research/toddler-behaviour/scratchpad/FINDINGS-W2/strict_check_w2.py mamivio.com/research/toddler-behaviour/synthesis/findings.md
```

```text
611 ids, 0 unresolved; checked 410 fragments, 0 failed
```

```sh
python3 -I mamivio.com/research/toddler-behaviour/scratchpad/FINDINGS-W3/strict_check_w3.py mamivio.com/research/toddler-behaviour/synthesis/findings.md
```

```text
324 ids, 0 unresolved; checked 209 fragments, 0 failed
```

### Additional restoration and preservation audit

A one-off snapshot comparison also checks every restored full quote, all prior ids, all queue ids, every safety-intake id, unchanged original records, and all four retired query switches. Its output:

```text
774 full saved quotes restored: 683 final-list + 15 earlier-labelled + 76 additional unit-level accounts; 0 mismatches
1703 named ids resolve; all 978 original named ids retained
2647 queue rows: post=1241, unit=1406; 0 duplicate ids; all 806 safety-intake posts covered
Voice files, source ledgers and reader notes unchanged; merged ids/quotes/metadata unchanged except historical flags; 0 active restrictions
All 4 legacy exclusion switches are no-ops and return the formerly marked coach quote
```

## Remaining uncertainty and re-reading boundary

The queue is deliberately explicit about review candidates: mixed off-topic/off-age triage reasons do not prove censorship; 152 marked units have no precise omitted-passage log; TR06's broad medical omission statement leaves 90 further assignment units to review; and 31 unquoted reviews have no per-unit reason map. The queue retains recorded causes rather than inventing missing words or treating every candidate as a confirmed omission. The other 319 no-quote and 810 partially quoted Reddit units are named in the source metadata, with some reasons also mixed. These counts describe the inventory, not a count of missing quotes.

Nothing withheld before extraction was reconstructed. The 806 safety-intake posts, subject-based triage drops, whole-unit exclusions, omitted passages and review candidates require later reading. No new voice records were created, no ids were reused, no network or git command was used, and no push was attempted.


## Re-reading completed and integrated — 2026-11-16

UR01–UR09 read all **2,647** assigned source rows: **2,612 Reddit sources and 35 review blocks**. Every queue id is accounted for exactly once in their ledgers; **0 sources were missing and 0 recovery rows remain unread**. There are 2,292 rows yielding new quotations and 355 without new quotations (328 off-niche, 27 nothing new beyond saved evidence). The original inventory above remains a record of what required recovery at that time.

The synthesis revision read **all 3,489 recovered quotes**, without sampling, and every reader’s “What these posts add” section. It integrated **379 recovered quote ids** into the topical findings, added **24 topical subsections** and the closing **“What the 2026-11-16 re-reading changed”** section, and rewrote undercut conclusions. All **1,703 earlier id mentions** and **774 earlier full saved quotations** remain. Current findings cite **2,058 distinct bracketed quote ids** (2,082 distinct id mentions including plain historical endpoints).

The merged corpus was regenerated with the shared `audit_niche.py` using `read-v1 read-w2 read-w3`: **12,782 quote records = 12,620 Reddit + 162 review quotes**. Recovery adds 3,461 Reddit and 28 review quotes to the earlier 9,293 records. No source voice file, reader ledger or raw file was changed. All 683 old markings remain descriptive history; merged active restrictions are zero. The historical completed spot check was retained; generation did not leave a new blank-verdict template.

Checks: `verify_findings_ids.py` reports **2,058 distinct ids cited, 0 unresolved; 1,761 verbatim fragments paired with an id, 0 failed**; all 2,082 id mentions, including plain historical endpoints, also resolve; `check_ids.py` reports 12,782 distinct ids and zero duplicates; `audit_niche.py --check-only` reports 3,583 original assigned units, 115 with no quote, zero unexplained and zero active restrictions. Full bullet quotation comparison passes for all 1,158 occurrences, including all 774 earlier full quotations. Source verification uses the build’s own whitespace/entity/trim logic with an in-memory JSONL decoder and individual review-block selection: **12,782 quotes, 0 failed**. A stricter literal comparison independently passes **all 3,489 UR excerpts** against their own sources. The 72 protected Reddit voice/reading-ledger files retain their pre-integration hashes.

Still unread outside this recovery: **10,431 tier-B posts, 3,174 tier-C posts and 2,661 ordinary tier-A triage drops** (868 wave 1, 796 wave 2, 997 wave 3). The **982 removed/deleted bodies** remain unavailable. Other uncollected channels and unfinished synthesis work remain listed in findings §13. The known subject-exclusion queue is complete; none of those ordinary or unavailable sources is silently represented as having been read. Records and excerpts are counts of quotes or explicitly labelled source assignments, never people or prevalence.
