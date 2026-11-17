# Baby and toddler sleep unfilter report — 2026-11-16

Initial inventory was written before changing findings, instructions or tools; the sections through “Result” record that completed restoration audit. The final completion section supersedes its future-reading status. Scope: `sleep-baby/` only. No git, network, push, other-build edits, shared-script edits, raw mutations or re-reading for new extraction. Reader notes, source ledgers and historical run logs remain unchanged. Counts describe selected quotes, records or units, never people or prevalence.

## Verified baseline, by stage

### Intake and triage

- `_raw/reddit/filter-v1/safety-candidates.jsonl` contains **1,641 records and 1,641 distinct post identities**. There is no second filter-version safety file in this build. The old shared `niche_filter.py` routed safety hits away from A/B/C reading cards before full reading. The corrected shared script is already in place; frozen intake files were not regenerated.
- The frozen `_raw/reddit/triage/wave1-T1.tsv` … `wave1-T6.tsv`, `wave2-W2T1.tsv` … `wave2-W2T6.tsv`, and `wave3-W3T1.tsv` … `wave3-W3T14.tsv` contain **6,937 drop rows**. **278** reasons explicitly start with `safety`; **1,114 more** name subject-related material such as illness, medical care, conditions, PPD/PPA, distress, anger, unsafe sleep, physical handling or harm. All **1,392 identities** are in the queue with their recorded reasons. Many of the latter combine a subject with an ordinary off-topic, age or duplication reason; they are review candidates, not 1,114 proven censorship cases. The intake and selected triage sets are disjoint.
- `synthesis/reader-notes-triage.md` records sick-baby-night drops (T1), nine safety drops with neutral reasons (T3), breathing emergency / caregiver distress / conflict drops (T5), and a paediatrician-disagreement post left dropped (T6). Reasons and identities were recovered from triage metadata, not source bodies. The already corrected `prompt-sleep-baby-triage-w3.txt` no longer directs subject exclusions.

### Reading and extraction

- `sources/reddit-reading-r01.md` … `r63.md`, the corresponding `synthesis/reader-notes-rNN.md` and linked working logs show filtering **before** `voice/`: whole units excluded, OP replies withheld, individual sentences dropped, clauses trimmed, and medical information left only in context. This was not merely a flag on an otherwise complete extraction.
- The four frozen assignment sets (`_raw/reddit/read-v1a/`, `read-v1b/`, `read-w2/`, `read-w3/`) contain **8,747 distinct assigned units**. **8,139** have a Reddit quote; **608** have none. The audit finds **0 unexplained** no-quote units. The 8,173 `raw_file` values in the full voice database also include review source files, so that is not the count of assigned Reddit units quoted.
- The omission inventory directly identifies **358 no-quote units with subject-indicating ledger reasons** and **1,467 quoted units with subject-related passage omissions**: **1,825 named identities**. It also retains **377 other skipped/partly quoted ledger identities** (232 no-quote and 145 quoted) for completeness, including duplicate, off-age, thin or ordinary selection reasons. These other cases are not described as censorship. Those groups total **2,202** unique ledger identities; the structured extraction accounts directly for 590 of the 608 no-quote units.
- Linked working logs supply **448 additional named review identities**, including the remaining 18 no-quote units; the other 430 have voice records. Some log lines combine omissions with duplicate targets or fully quoted examples, so these are labelled review candidates with the full recorded log line, rather than falsely counting every reference as a confirmed omission. Additional reader-note references yield **170 further review identities**; unrelated quoted examples sometimes share a sentence with an omission, and this uncertainty is explicit in the queue.
- Twelve ledgers explicitly describe omitted categories without a complete unit list: **R01, R02, R04, R08, R12, R13, R35, R37, R38, R46, R54, R62**. The remaining **1,269 assigned identities** in those readers' sets are queued as **unmapped review candidates**, not confirmed drops. This conservatively makes the missing passages findable without inventing unit-level certainty. R55 and R60's numbered omission lists were resolved from frozen assignment order (47 and 37 numbered units respectively), not by reading raw text.
- R32 also applied the erroneous 0–24-month reader scope to ordinary 2.5–3-year-olds, despite the build's 0–36-month scope. Its ledger names more such omissions than the findings' old “two in-scope units” summary suggests. All skipped R32 identities and the partly quoted over-age records are retained in the queue with their original reasons; they need reassessment, not an assumed count of two.

**What cannot be restored from voice.** Intrusive images of harming the baby (`NewParents-1vype6d`, R03), fear-of-harm wording trimmed from the source of sb05-0274 (`beyondthebump-1w5khx9`, R05), the colour-change account during prolonged crying (`sleeptrain-1w731pn`, R06), punishment/harshness/physical handling (R12, R17, R24 and later readers), infant breathing and death fears, positions/surfaces/bedsharing arrangements, medication names/doses, conditions, tests, birth and hospital history, reported professional advice and claims about crying were withheld. A midnight panic purchase of a monitor sock (`NewParents-1szpvsc`, R41) and a £415 tongue-tie procedure price (`beyondthebumpUK-1sn8f76`, R48 log) never reached voice either. These words and prices require returning to the units; none was invented or reconstructed here. The total number of missing quotations is unknown.

The named identities, additional review identities and unmapped candidates are listed by reader below; the complete deduplicated queue also includes the intake and triage posts. No queued source was re-read to decide its substantive content. The later source-matching check only mechanically verifies already extracted quotes against their cited files.

### Marking

- `synthesis/restricted-ids.md` contains **689 unique ids**, all resolving in the **25,419 original voice records**: **673 Reddit + 16 book/app review quotes**. The Reddit wave split is **197 wave 1, 244 wave 2, 232 wave 3**. Prefix-by-prefix counts are available by reading the historical table; earlier findings totals of 164 and 457 were incomplete/earlier corpus states, not the final list.
- `voice-merged/all.jsonl` originally had **689 active `restricted` flags**. Original `voice/*.jsonl` have **no restriction or eligibility fields**. Historical notes and the orchestrator sweep supplied the list; the old shared audit copied it into active merged flags. The shared collector/audit have already been corrected and were not edited here.
- The historical list, including every id and recorded reason, is preserved byte-for-byte from its table heading onward. Its new title and first paragraph make the marking inert. The merged copy now has `restricted: false` and `formerly_restricted` as a descriptive historical label; original reader records are untouched.

### Findings

- Baseline `synthesis/findings.md` cited **992 distinct ids**: **31** of the 689 marked ids and **658 not cited anywhere**. The marked quotes contain **21,003 whitespace-separated words**. The rule replaced marked words with descriptions and omitted the rest, while §§12, 16.6 and 17.8 explicitly directed non-quotation.
- All **689 full voice quotes** are now reproduced in their relevant main sections: 31 restored at the original citations and 658 introduced where their subject is analysed. Every original cited id is retained; the current total is **1,650 distinct cited ids**. The thematic additions include reported clinical advice, treatment experiences, repeated setbacks, gear, methods stopped, partners, cosleeping, fears, judgement, money, the parent's physical and emotional state, constraints, and reviews. They are not relegated to an appendix.
- The dated closing section records the conclusions that moved and their ids. Regret now includes regret about training; cosleeping includes contentment, discomfort, sleeplessness, changing needs and refusal; the parent's mental/physical capacity and coercive conflict widen the fit problem; medical uncertainty and cost widen the help sought; breathing/vomiting/injury accounts sharpen reasons to stop; tracking/content can worsen anxiety; and the bouncer, heating pad and benefits/therapy evidence widen the money record. Relapse follow-ups remain observed sequences, not proven causes or a validated restart protocol.

### Instructions and tooling

- `README.md`'s “Lines not to cross” section and `product/product-brief.md`'s corresponding cautions were replaced with the owner's research principle. Findings §12 now states the same principle in three sentences. No instruction to withhold words because of their subject remains in these current instructions.
- `_tools/query.py` had `--exclude-restricted` (filtering `marketing_eligible=false`) and a research-boundary warning. No original record currently has that field, but the enforcing branch is removed; the option remains a documented compatibility no-op. `scratchpad/FINDINGS/q.py` also hid historically marked records under `--norestr`; that branch is removed and its display now says `FORMERLY_MARKED`.
- `scratchpad/FINDINGS-W2/chk_restricted.py` demanded marks and checked for marked quotations; `scratchpad/FINDINGS-W3/restricted_check.py` counted their quotation as problems. Both paths now invoke the shared id/fragment verifier, preserving optional section selection and propagating its exit status. A marked id or its words no longer causes a problem; unresolved ids and mismatched fragments still fail.
- Shared `verify_findings_ids.py` never rejected marked ids; it checks resolution and fragments. Shared `check_ids.py` checks uniqueness. Local `_tools/verify_quotes.py` checks required fields and exact source fragments in order. All remain intact. Shared `audit_niche.py` was run with `--check-only`, preserving historical safety-hit and spot-check records. Only current counts labels and merged restriction flags were updated locally.
- Build-specific prompts inspected: `../_shared/_tools/prompt-sleep-baby-reader-w2.txt`, `prompt-sleep-baby-reader-w3.txt`, `prompt-sleep-baby-triage-w3.txt`. All three already contain the 2026-11-16 principle; **0 prompt/brief changes and 0 shared-script changes** were needed.
- Historical reader notes, source ledgers, scratch extraction builders/specifications, run logs, count helpers, frozen draft sections, `synthesis/audit-safety-hits.tsv` and `audit-spotcheck.md` were left as records of the earlier runs. Their former labels are not current instructions; do not rebuild voice from the old extraction specifications.

## Re-reading queue and limits

`scratchpad/unfilter-reread/queue.tsv` has exactly the requested header `kind	id	why_it_was_dropped` and **7,122 rows: 4,089 unit rows + 3,033 post rows**, with **0 duplicate ids**. All 1,641 safety-intake identities are present. Each reason retains its source path/line or intake/triage provenance. Multiple reasons for one identity share one row.

The unit rows comprise the 2,202 ledger identities, 448 additional log references, 170 additional note references and 1,269 unmapped review candidates described above. The post rows comprise 1,641 intake and 1,392 triage identities. These partitions are disjoint after identity deduplication. Ordinary duplicate/off-age/no-quote rows and review candidates are retained for completeness and explicitly distinguished from documented subject-based omissions. No prevalence or missing-quote count can be inferred from this queue.

Identities use `<subreddit>-<postid>` throughout. Five recorded subreddit errors/abbreviations were resolved by unique post id in assignment/candidate metadata: `bbUK-1sq6ao7` → `beyondthebumpUK-1sq6ao7`; `beyondthebump-1wwzsvd` → `NewParents-1wwzsvd`; `sleeptrain-1u7ghqj` → `NewParents-1u7ghqj`; `sleeptrain-1u7nfg5` → `toddlers-1u7nfg5`; `sleeptrain-1v72pie` → `AttachmentParenting-1v72pie`. R40's `FirstTimeMom-1vucqn` was resolved to its assigned `FirstTimeMom-1vtucqn` (a missing `t`, supported by `scratchpad/R40/units.txt:23` and frozen chunk 133). Queue reasons preserve the recorded spelling and correction. This last correction is an identity inference, not a source-content inference.

Uncertainty remains about the exact passages in anonymous category omissions, mixed subject/relevance triage reasons, and extra log/note references. R21's notes call `sleeptrain-1xctz6x` excluded, while its ledger and voice records show it was partly quoted; the queue uses one identity and retains the omission reason. The source words can only settle these questions in later reading.

## Files changed

- `README.md` — replace subject boundaries; identify historical run state and current unfilter outputs.
- `_tools/query.py` — make the legacy exclusion option inert; remove boundary warning.
- `product/product-brief.md` — replace subject-based research cautions with the owner’s principle.
- `scratchpad/FINDINGS-W2/chk_restricted.py` — replace censorship checks with id/fragment verification.
- `scratchpad/FINDINGS-W3/restricted_check.py` — replace censorship checks with id/fragment verification.
- `scratchpad/FINDINGS/q.py` — remove the hidden --norestr filter and describe historical labels.
- `scratchpad/unfilter-reread/audit_unfilter.py` — verify complete restored quotes, retained ids, unchanged original voice and queue invariants.
- `scratchpad/unfilter-reread/queue.tsv` — write the deduplicated future-reading/review queue.
- `synthesis/counts.md` — make marking counts historical and active restrictions zero; preserve original numerical counts.
- `synthesis/findings.md` — restore all 689 quotes, revise conclusions/instructions, retain all original cited ids and add dated change section.
- `synthesis/restricted-ids.md` — retitle and add inert historical-record paragraph; preserve the entire list.
- `synthesis/unfilter-report.md` — write initial inventory first, then complete this report and check outputs.
- `voice-merged/all.jsonl` — clear active flags and retain the former marking descriptively.

**13 files changed.** No original voice, reader note, source ledger, historical run log, raw file, other build or shared tool/prompt was edited.

## Verification

Commands below run from the `ads` repository root, all with `python3 -I`; every command exited 0. Shared audit was deliberately check-only so it did not overwrite historical audit artifacts.

`python3 -I mamivio.com/research/_shared/_tools/verify_findings_ids.py mamivio.com/research/sleep-baby/synthesis/findings.md sleep-baby`

```text
1650 distinct ids cited, 0 unresolved
1473 verbatim fragments paired with an id, 0 failed
```

`python3 -I mamivio.com/research/_shared/_tools/check_ids.py sleep-baby`

```text
25419 records, 25419 distinct ids, 0 duplicated
```

`python3 -I mamivio.com/research/_shared/_tools/audit_niche.py sleep-baby read-v1a read-v1b read-w2 read-w3 --check-only`

```text
{"quotes": 25419, "assigned": 8747, "units_quoted": 8173, "assigned_units_quoted": 8139, "uncited": 608, "unexplained": 0, "historically_marked": 689, "active_restrictions": 0, "safety_hits": 86}
```

`python3 -I mamivio.com/research/sleep-baby/scratchpad/FINDINGS-W2/chk_restricted.py mamivio.com/research/sleep-baby/synthesis/findings.md`

```text
1650 distinct ids cited, 0 unresolved
1473 verbatim fragments paired with an id, 0 failed
```

`python3 -I mamivio.com/research/sleep-baby/scratchpad/FINDINGS-W3/restricted_check.py mamivio.com/research/sleep-baby/synthesis/findings.md --from '## 17.'`

```text
317 distinct ids cited, 0 unresolved
160 verbatim fragments paired with an id, 0 failed
```

`python3 -I mamivio.com/research/sleep-baby/scratchpad/unfilter-reread/audit_unfilter.py`

```text
Original voice files unchanged: 64 files, 25419 records
Original cited ids retained: 992; current cited ids resolve: 1650
Full formerly marked quotes match voice exactly (whitespace normalized): 689/689
Historical list preserved; active merged restrictions: 0
Queue: 7122 rows, 0 duplicate ids; safety intake covered: 1641/1641
```

`python3 -I mamivio.com/research/sleep-baby/_tools/query.py --exclude-restricted --max 0`

```text
# 25419 match
```

`python3 -I mamivio.com/research/sleep-baby/_tools/verify_quotes.py`

```text
reddit-r01.jsonl: 328 quotes, 0 failed
reddit-r02.jsonl: 294 quotes, 0 failed
reddit-r03.jsonl: 327 quotes, 0 failed
reddit-r04.jsonl: 314 quotes, 0 failed
reddit-r05.jsonl: 317 quotes, 0 failed
reddit-r06.jsonl: 347 quotes, 0 failed
reddit-r07.jsonl: 321 quotes, 0 failed
reddit-r08.jsonl: 291 quotes, 0 failed
reddit-r09.jsonl: 305 quotes, 0 failed
reddit-r10.jsonl: 278 quotes, 0 failed
reddit-r11.jsonl: 299 quotes, 0 failed
reddit-r12.jsonl: 220 quotes, 0 failed
reddit-r13.jsonl: 320 quotes, 0 failed
reddit-r14.jsonl: 253 quotes, 0 failed
reddit-r15.jsonl: 308 quotes, 0 failed
reddit-r16.jsonl: 310 quotes, 0 failed
reddit-r17.jsonl: 372 quotes, 0 failed
reddit-r18.jsonl: 384 quotes, 0 failed
reddit-r19.jsonl: 306 quotes, 0 failed
reddit-r20.jsonl: 378 quotes, 0 failed
reddit-r21.jsonl: 387 quotes, 0 failed
reddit-r22.jsonl: 367 quotes, 0 failed
reddit-r23.jsonl: 353 quotes, 0 failed
reddit-r24.jsonl: 361 quotes, 0 failed
reddit-r25.jsonl: 391 quotes, 0 failed
reddit-r26.jsonl: 447 quotes, 0 failed
reddit-r27.jsonl: 363 quotes, 0 failed
reddit-r28.jsonl: 443 quotes, 0 failed
reddit-r29.jsonl: 337 quotes, 0 failed
reddit-r30.jsonl: 343 quotes, 0 failed
reddit-r31.jsonl: 416 quotes, 0 failed
reddit-r32.jsonl: 386 quotes, 0 failed
reddit-r33.jsonl: 337 quotes, 0 failed
reddit-r34.jsonl: 390 quotes, 0 failed
reddit-r35.jsonl: 362 quotes, 0 failed
reddit-r36.jsonl: 421 quotes, 0 failed
reddit-r37.jsonl: 396 quotes, 0 failed
reddit-r38.jsonl: 349 quotes, 0 failed
reddit-r39.jsonl: 436 quotes, 0 failed
reddit-r40.jsonl: 388 quotes, 0 failed
reddit-r41.jsonl: 508 quotes, 0 failed
reddit-r42.jsonl: 434 quotes, 0 failed
reddit-r43.jsonl: 585 quotes, 0 failed
reddit-r44.jsonl: 400 quotes, 0 failed
reddit-r45.jsonl: 553 quotes, 0 failed
reddit-r46.jsonl: 576 quotes, 0 failed
reddit-r47.jsonl: 455 quotes, 0 failed
reddit-r48.jsonl: 441 quotes, 0 failed
reddit-r49.jsonl: 358 quotes, 0 failed
reddit-r50.jsonl: 437 quotes, 0 failed
reddit-r51.jsonl: 470 quotes, 0 failed
reddit-r52.jsonl: 496 quotes, 0 failed
reddit-r53.jsonl: 514 quotes, 0 failed
reddit-r54.jsonl: 522 quotes, 0 failed
reddit-r55.jsonl: 438 quotes, 0 failed
reddit-r56.jsonl: 495 quotes, 0 failed
reddit-r57.jsonl: 580 quotes, 0 failed
reddit-r58.jsonl: 464 quotes, 0 failed
reddit-r59.jsonl: 532 quotes, 0 failed
reddit-r60.jsonl: 528 quotes, 0 failed
reddit-r61.jsonl: 489 quotes, 0 failed
reddit-r62.jsonl: 525 quotes, 0 failed
reddit-r63.jsonl: 440 quotes, 0 failed
reviews-rv1.jsonl: 234 quotes, 0 failed
TOTAL 25419 quotes, 0 failed
```

The source verifier normalizes whitespace/HTML entities and checks each existing quote fragment in order. The added audit separately checks every formerly marked **full** quote against `voice/` with whitespace normalization only, keeps all 992 baseline cited ids, verifies the 64 original voice-file hashes and the historical list, and checks queue uniqueness and full safety-intake coverage. It reads no raw source bodies.

## Reader identities for later re-reading/review

Each reader heading names its unchanged ledger. The categories below are disjoint within that reader, with priority given to ledger subject omissions, then other ledger selection, then additional log/note references, then unmapped candidates. Category counts are identifiers, not missing quotes. A candidate is not a claim that the unit contains omitted words. Exact provenance/reasons are in `queue.tsv`.

### R01 — `sources/reddit-reading-r01.md`

**Subject-based passage ledger references (2):** `NewParents-1wrhlo5`, `sleeptrain-1wzgkhv`.

**Other skipped/partly quoted ledger references (4):** `Mommit-1wkjqjv`, `NewParents-1w3o0yz`, `beyondthebump-1wkjq68`, `toddlers-1wo6vvd`.

**Unmapped category review candidates (135):** `FirstTimeMom-1wlgw2a`, `FirstTimeMom-1wmmhnh`, `FirstTimeMom-1wowlfm`, `Mommit-1w3lggx`, `Mommit-1w5c4te`, `Mommit-1wml54e`, `NewParents-1vyfvju`, `NewParents-1vzh348`, `NewParents-1w0d9nm`, `NewParents-1w2sl9q`, `NewParents-1w39kui`, `NewParents-1w6ifpx`, `NewParents-1w8gezk`, `NewParents-1w99up2`, `NewParents-1waywon`, `NewParents-1wcpqyl`, `NewParents-1wdldsb`, `NewParents-1wdqxs9`, `NewParents-1we0tnl`, `NewParents-1wir7sx`, `NewParents-1wivtfp`, `NewParents-1wj1pyg`, `NewParents-1wkcp0n`, `NewParents-1wkjpfx`, `NewParents-1wl4n39`, `NewParents-1wl7sf3`, `NewParents-1wngsfw`, `NewParents-1wpbv5m`, `Parenting-1wbjikw`, `Parenting-1wi7k0g`, `beyondthebump-1w9zd8u`, `beyondthebump-1wgyymc`, `beyondthebump-1wi5rez`, `beyondthebump-1wiivf2`, `beyondthebump-1wiss8m`, `beyondthebump-1wngter`, `beyondthebumpUK-1wces7k`, `beyondthebumpUK-1wjn0v5`, `daddit-1wfa290`, `sleeptrain-1vy6zuz`, `sleeptrain-1vyea2e`, `sleeptrain-1vylpc6`, `sleeptrain-1vyump3`, `sleeptrain-1vyx6fw`, `sleeptrain-1vzgh9p`, `sleeptrain-1vzh8vw`, `sleeptrain-1vzlrs8`, `sleeptrain-1vznjoa`, `sleeptrain-1vzv767`, `sleeptrain-1w0ki2g`, `sleeptrain-1w0nhv3`, `sleeptrain-1w0poiz`, `sleeptrain-1w0z817`, `sleeptrain-1w10uu6`, `sleeptrain-1w128nh`, `sleeptrain-1w1fbyn`, `sleeptrain-1w1jbo5`, `sleeptrain-1w1ngz6`, `sleeptrain-1w1p915`, `sleeptrain-1w23l3b`, `sleeptrain-1w24j2e`, `sleeptrain-1w2l5pg`, `sleeptrain-1w2nksa`, `sleeptrain-1w39wzb`, `sleeptrain-1w3m3cw`, `sleeptrain-1w3nz8p`, `sleeptrain-1w4u5xe`, `sleeptrain-1w56m7f`, `sleeptrain-1w5updn`, `sleeptrain-1w6azfc`, `sleeptrain-1w6kbow`, `sleeptrain-1w7174x`, `sleeptrain-1w7h96t`, `sleeptrain-1w7xj8a`, `sleeptrain-1w82cr3`, `sleeptrain-1w856b8`, `sleeptrain-1w87bbg`, `sleeptrain-1w9ynnd`, `sleeptrain-1waph26`, `sleeptrain-1wasp4x`, `sleeptrain-1wavrf1`, `sleeptrain-1wb5zfi`, `sleeptrain-1wb77ix`, `sleeptrain-1wbfx2h`, `sleeptrain-1wbj0ob`, `sleeptrain-1wbxc6h`, `sleeptrain-1wcflyg`, `sleeptrain-1wcidww`, `sleeptrain-1wdf7ce`, `sleeptrain-1wdjot6`, `sleeptrain-1wdn7ui`, `sleeptrain-1wdqozn`, `sleeptrain-1wduf0i`, `sleeptrain-1we0vtj`, `sleeptrain-1we29h7`, `sleeptrain-1weebp5`, `sleeptrain-1weehk3`, `sleeptrain-1wehmli`, `sleeptrain-1wfccr5`, `sleeptrain-1wff3wa`, `sleeptrain-1wgab96`, `sleeptrain-1wgomwm`, `sleeptrain-1wgzpxz`, `sleeptrain-1wh95xk`, `sleeptrain-1who46i`, `sleeptrain-1wiv2tb`, `sleeptrain-1wiwy17`, `sleeptrain-1wjag8e`, `sleeptrain-1wjzscu`, `sleeptrain-1wk1kry`, `sleeptrain-1wlwyj9`, `sleeptrain-1wlysg1`, `sleeptrain-1wnq4gr`, `sleeptrain-1wo1w1n`, `sleeptrain-1woo1no`, `sleeptrain-1wophlh`, `sleeptrain-1wybrbo`, `sleeptrain-1wyr8y8`, `sleeptrain-1wyspbm`, `sleeptrain-1wytqom`, `sleeptrain-1wywlia`, `sleeptrain-1wztyod`, `sleeptrain-1x01bod`, `sleeptrain-1x0784y`, `sleeptrain-1x0947b`, `sleeptrain-1x0a22k`, `sleeptrain-1x0aoo5`, `toddlers-1wchjtb`, `toddlers-1wi9b5v`, `toddlers-1wjkudt`, `toddlers-1wnfe4z`, `toddlers-1wo56ky`, `toddlers-1worplc`, `toddlers-1wp2gny`, `toddlers-1wy3zey`.

### R02 — `sources/reddit-reading-r02.md`

**Subject-based whole-unit ledger references (1):** `sleeptrain-1wddvir`.

**Subject-based passage ledger references (1):** `daddit-1wr8zks`.

**Other skipped/partly quoted ledger references (4):** `ScienceBasedParenting-1vy45nm`, `beyondthebump-1w30dhf`, `beyondthebump-1wkuxjp`, `workingmoms-1vzdit5`.

**Additional reader-note review candidates (1):** `NewParents-1w2y21r`.

**Unmapped category review candidates (66):** `AttachmentParenting-1w0tmdg`, `AttachmentParenting-1w3uuvq`, `AttachmentParenting-1wkzvfn`, `FirstTimeMom-1w23zxf`, `FirstTimeMom-1wkuuzc`, `Mommit-1vxp1ky`, `Mommit-1vyuqld`, `Mommit-1vza2rp`, `Mommit-1w0efku`, `Mommit-1w23z99`, `Mommit-1w30cgg`, `Mommit-1w4sd22`, `Mommit-1wnuui1`, `NewParents-1vxk4e7`, `NewParents-1vzdi5f`, `NewParents-1w0xwkx`, `NewParents-1w16xux`, `NewParents-1w206ru`, `NewParents-1w2hzuc`, `NewParents-1w3kiyv`, `NewParents-1w422ha`, `NewParents-1w4lynf`, `NewParents-1w5euyp`, `NewParents-1w92xtg`, `NewParents-1wf70kk`, `NewParents-1wgiwk0`, `NewParents-1wke9e8`, `NewParents-1wp4zec`, `Parenting-1wbi9zt`, `Parenting-1whwgta`, `beyondthebump-1vzhtuy`, `beyondthebump-1w1cgbb`, `beyondthebump-1w450b2`, `beyondthebumpUK-1vy8y3g`, `daddit-1w95ils`, `daddit-1wp7wqh`, `sleeptrain-1vxv9xx`, `sleeptrain-1w0ihfa`, `sleeptrain-1w0o698`, `sleeptrain-1w0uh3w`, `sleeptrain-1w29wi1`, `sleeptrain-1w3am1s`, `sleeptrain-1w3y5rv`, `sleeptrain-1w57714`, `sleeptrain-1w5b8f3`, `sleeptrain-1w5bjnx`, `sleeptrain-1w6nvtp`, `sleeptrain-1wc92tj`, `sleeptrain-1wctb57`, `sleeptrain-1wdki0l`, `sleeptrain-1wgmnmb`, `sleeptrain-1whaf09`, `sleeptrain-1whwp0k`, `sleeptrain-1wike61`, `sleeptrain-1wj3sul`, `sleeptrain-1wkodvn`, `sleeptrain-1wkywud`, `sleeptrain-1wlyewm`, `sleeptrain-1wn1w02`, `sleeptrain-1wogybv`, `sleeptrain-1woksq0`, `sleeptrain-1wybvq0`, `sleeptrain-1wywa5x`, `sleeptrain-1wzplmv`, `toddlers-1w082cq`, `toddlers-1wgmb5z`.

### R03 — `sources/reddit-reading-r03.md`

**Subject-based passage ledger references (8):** `Mommit-1vz1a0b`, `Mommit-1vz6zj4`, `NewParents-1vxnkoj`, `NewParents-1vy8fyp`, `NewParents-1vype6d`, `beyondthebumpUK-1vyry3l`, `sleeptrain-1vyzcg3`, `sleeptrain-1vzgt0j`.

**Other skipped/partly quoted ledger references (3):** `NewParents-1vxpdw7`, `sleeptrain-1vy7kg5`, `sleeptrain-1vzapy6`.

**Additional reader-note review candidates (3):** `AttachmentParenting-1vyiwut`, `sleeptrain-1vyy0by`, `sleeptrain-1vz6ciw`.

### R04 — `sources/reddit-reading-r04.md`

**Subject-based whole-unit ledger references (2):** `beyondthebumpUK-1vzop43`, `sleeptrain-1w1uerz`.

**Subject-based passage ledger references (3):** `NewParents-1w1dtan`, `NewParents-1w1rzq3`, `sleeptrain-1w0sxy2`.

**Other skipped/partly quoted ledger references (5):** `Mommit-1w1evcx`, `NewParents-1w24zvw`, `NewParents-1w2khj3`, `sleeptrain-1w2ha2k`, `toddlers-1w0l06k`.

**Unmapped category review candidates (118):** `AttachmentParenting-1vzq9rx`, `AttachmentParenting-1w0fw0j`, `AttachmentParenting-1w0htrk`, `AttachmentParenting-1w0o0f8`, `AttachmentParenting-1w2dy81`, `FirstTimeMom-1vzummo`, `FirstTimeMom-1vzxo6d`, `FirstTimeMom-1w03ss6`, `Mommit-1w0aoqv`, `Mommit-1w0krcd`, `Mommit-1w19p6y`, `Mommit-1w27zuy`, `Mommit-1w2khx3`, `NewParents-1vzx6ue`, `NewParents-1w022pz`, `NewParents-1w0289k`, `NewParents-1w04ujw`, `NewParents-1w0cjln`, `NewParents-1w0s393`, `NewParents-1w0u0os`, `NewParents-1w0w7va`, `NewParents-1w1540d`, `NewParents-1w1e7km`, `NewParents-1w1fe50`, `NewParents-1w1kuwu`, `NewParents-1w1mtav`, `NewParents-1w1rumk`, `NewParents-1w1suh0`, `NewParents-1w1uger`, `NewParents-1w1xvtb`, `NewParents-1w29jpb`, `NewParents-1w2ckc3`, `NewParents-1w2fdig`, `NewParents-1w2h7c8`, `NewParents-1w2lga0`, `Parenting-1w0s3mb`, `Parenting-1w1aobo`, `Parenting-1w1exiz`, `Parenting-1w1udzb`, `Parenting-1w2a6vj`, `Parenting-1w2i8lk`, `beyondthebump-1vzv7rg`, `beyondthebump-1w02u6x`, `beyondthebump-1w03msu`, `beyondthebump-1w1c96j`, `beyondthebump-1w1yka6`, `beyondthebump-1w29m8q`, `beyondthebump-1w2itgc`, `beyondthebumpUK-1vzyhbb`, `beyondthebumpUK-1w0dddt`, `beyondthebumpUK-1w122cv`, `beyondthebumpUK-1w1q9kt`, `daddit-1w28l4z`, `sleeptrain-1vzjr9f`, `sleeptrain-1vzk1c5`, `sleeptrain-1vzla41`, `sleeptrain-1vzpluo`, `sleeptrain-1vzt9pz`, `sleeptrain-1vzu0eb`, `sleeptrain-1vzw8f7`, `sleeptrain-1vzxn5h`, `sleeptrain-1vzyib5`, `sleeptrain-1w02lio`, `sleeptrain-1w031b2`, `sleeptrain-1w03qr7`, `sleeptrain-1w04g75`, `sleeptrain-1w04nb3`, `sleeptrain-1w0864h`, `sleeptrain-1w08ucr`, `sleeptrain-1w0913v`, `sleeptrain-1w0gw7r`, `sleeptrain-1w0hiww`, `sleeptrain-1w0mftq`, `sleeptrain-1w0nhch`, `sleeptrain-1w0ojp9`, `sleeptrain-1w0oquh`, `sleeptrain-1w0pbgi`, `sleeptrain-1w0q45z`, `sleeptrain-1w0rh2x`, `sleeptrain-1w0rz3w`, `sleeptrain-1w0t8uo`, `sleeptrain-1w0tjt6`, `sleeptrain-1w0u20b`, `sleeptrain-1w0veyj`, `sleeptrain-1w0yfyq`, `sleeptrain-1w10mio`, `sleeptrain-1w13f1l`, `sleeptrain-1w15kv1`, `sleeptrain-1w190od`, `sleeptrain-1w1cgh9`, `sleeptrain-1w1f79t`, `sleeptrain-1w1j63x`, `sleeptrain-1w1ne93`, `sleeptrain-1w1o0vq`, `sleeptrain-1w1ocob`, `sleeptrain-1w1pupo`, `sleeptrain-1w1r3ab`, `sleeptrain-1w1u6i2`, `sleeptrain-1w1vm4y`, `sleeptrain-1w1x3sz`, `sleeptrain-1w1y0af`, `sleeptrain-1w26pgg`, `sleeptrain-1w27vtl`, `sleeptrain-1w28xe4`, `sleeptrain-1w2ekex`, `sleeptrain-1w2ii6l`, `sleeptrain-1w2jdws`, `toddlers-1w024sn`, `toddlers-1w040i3`, `toddlers-1w0l84e`, `toddlers-1w0mw18`, `toddlers-1w0npx8`, `toddlers-1w0r2n1`, `toddlers-1w0wwjw`, `toddlers-1w136io`, `toddlers-1w1bske`, `toddlers-1w1eye6`, `toddlers-1w2n9vq`.

### R05 — `sources/reddit-reading-r05.md`

**Subject-based whole-unit ledger references (1):** `sleeptrain-1w5u4b0`.

**Subject-based passage ledger references (1):** `beyondthebump-1w5khx9`.

**Other skipped/partly quoted ledger references (3):** `NewParents-1w33dh9`, `NewParents-1w3lipl`, `toddlers-1w4pija`.

**Additional reader-note review candidates (26):** `Mommit-1w5oah2`, `NewParents-1w3y0rb`, `NewParents-1w5v98r`, `Parenting-1w2odsr`, `Parenting-1w4q86n`, `beyondthebump-1w31169`, `beyondthebumpUK-1w42sk6`, `beyondthebumpUK-1w54n9x`, `daddit-1w5vh0r`, `sleeptrain-1w2tqv4`, `sleeptrain-1w3fdjr`, `sleeptrain-1w3foo4`, `sleeptrain-1w3uuod`, `sleeptrain-1w3wsph`, `sleeptrain-1w3zw8i`, `sleeptrain-1w47unr`, `sleeptrain-1w4f6cq`, `sleeptrain-1w4ijdg`, `sleeptrain-1w4in2f`, `sleeptrain-1w4ymnu`, `sleeptrain-1w5a9g3`, `sleeptrain-1w5dflf`, `sleeptrain-1w5u7no`, `toddlers-1w3zixe`, `toddlers-1w4x2nb`, `toddlers-1w5c5xg`.

### R06 — `sources/reddit-reading-r06.md`

**Subject-based passage ledger references (7):** `Mommit-1w8lqum`, `NewParents-1w808zu`, `NewParents-1w8rag1`, `ScienceBasedParenting-1w8lxl0`, `beyondthebump-1w6gxkl`, `daddit-1w8cetj`, `sleeptrain-1w731pn`.

**Other skipped/partly quoted ledger references (1):** `sleeptrain-1w75vig`.

### R07 — `sources/reddit-reading-r07.md`

**Subject-based passage ledger references (11):** `NewParents-1wabshb`, `NewParents-1wayryz`, `beyondthebump-1wa46ob`, `beyondthebump-1wbnpvq`, `beyondthebump-1wc79r5`, `sleeptrain-1w9pc54`, `sleeptrain-1wado1k`, `sleeptrain-1wb66m1`, `sleeptrain-1wbe72m`, `sleeptrain-1wbjwpm`, `sleeptrain-1wbrknv`.

**Other skipped/partly quoted ledger references (5):** `Mommit-1wbqlci`, `NewParents-1wakfqb`, `beyondthebump-1wbc4wz`, `sleeptrain-1wazwmh`, `sleeptrain-1wbb9k5`.

**Additional reader-note review candidates (4):** `NewParents-1wanby0`, `NewParents-1waucen`, `beyondthebump-1w98az8`, `sleeptrain-1wb0q98`.

### R08 — `sources/reddit-reading-r08.md`

**Subject-based whole-unit ledger references (5):** `NewParents-1wd1vdk`, `NewParents-1wfg998`, `beyondthebump-1we7dvm`, `beyondthebump-1wfrgys`, `sleeptrain-1wdyeeq`.

**Subject-based passage ledger references (11):** `AttachmentParenting-1wez14j`, `NewParents-1weebyn`, `NewParents-1wfoluc`, `NewParents-1wfskf6`, `beyondthebump-1wchoap`, `beyondthebumpUK-1wfrb1w`, `sleeptrain-1wdtded`, `sleeptrain-1wdx7ug`, `sleeptrain-1wdz912`, `sleeptrain-1we0mf0`, `sleeptrain-1wftslu`.

**Other skipped/partly quoted ledger references (6):** `Mommit-1wch42h`, `NewParents-1wd02gq`, `beyondthebump-1wczvqu`, `beyondthebump-1wd4oht`, `sleeptrain-1wdkkv8`, `toddlers-1wcn6gh`.

**Unmapped category review candidates (120):** `AttachmentParenting-1wcop6o`, `AttachmentParenting-1wczv8u`, `AttachmentParenting-1wdawmy`, `AttachmentParenting-1wes6oe`, `AttachmentParenting-1wevmfx`, `AttachmentParenting-1wfq0ll`, `FirstTimeMom-1wegrx2`, `Mommit-1wd701m`, `Mommit-1wdn3db`, `Mommit-1wdy5c2`, `Mommit-1weq9w8`, `Mommit-1wetn81`, `NewParents-1wcayam`, `NewParents-1wci883`, `NewParents-1wco7qw`, `NewParents-1wcv1vp`, `NewParents-1wd0tkh`, `NewParents-1wdbkse`, `NewParents-1wdmz9e`, `NewParents-1wdo6k9`, `NewParents-1we1qla`, `NewParents-1we3enk`, `NewParents-1wepf1n`, `NewParents-1wesk36`, `NewParents-1wewt3s`, `NewParents-1wf6kc9`, `NewParents-1wfl3ve`, `NewParents-1wfp7kp`, `NewParents-1wfrx8q`, `Parenting-1wd0esr`, `Parenting-1wdd3dv`, `Parenting-1we7zer`, `Parenting-1wfpih7`, `beyondthebump-1wch6pi`, `beyondthebump-1wchpwu`, `beyondthebump-1wcijuh`, `beyondthebump-1wewxw5`, `beyondthebump-1wf3bej`, `beyondthebump-1wfqw85`, `beyondthebumpUK-1wdz13g`, `daddit-1wcv1pe`, `sahm-1wcpcdn`, `sleeptrain-1wc89rh`, `sleeptrain-1wc8a78`, `sleeptrain-1wc980x`, `sleeptrain-1wcc6on`, `sleeptrain-1wcdxtp`, `sleeptrain-1wcgh1j`, `sleeptrain-1wcj83k`, `sleeptrain-1wcjgok`, `sleeptrain-1wcjyxu`, `sleeptrain-1wcn2xn`, `sleeptrain-1wcngbr`, `sleeptrain-1wcnn3z`, `sleeptrain-1wcprl3`, `sleeptrain-1wcqh7k`, `sleeptrain-1wcvczu`, `sleeptrain-1wcybej`, `sleeptrain-1wczscx`, `sleeptrain-1wczwyx`, `sleeptrain-1wd2fzo`, `sleeptrain-1wd3m6y`, `sleeptrain-1wd5u9u`, `sleeptrain-1wd9ve6`, `sleeptrain-1wdayer`, `sleeptrain-1wdd1ls`, `sleeptrain-1wddix3`, `sleeptrain-1wdf7di`, `sleeptrain-1wdhcad`, `sleeptrain-1wdhh6w`, `sleeptrain-1wdlsdi`, `sleeptrain-1wdn8aa`, `sleeptrain-1wdoiia`, `sleeptrain-1wdoqox`, `sleeptrain-1wdppfe`, `sleeptrain-1wdsply`, `sleeptrain-1wdx96f`, `sleeptrain-1we0dyc`, `sleeptrain-1we3vdv`, `sleeptrain-1we7h3u`, `sleeptrain-1we7hyg`, `sleeptrain-1we7osf`, `sleeptrain-1we7yoz`, `sleeptrain-1we8pse`, `sleeptrain-1we8r1b`, `sleeptrain-1wed6c0`, `sleeptrain-1wedubt`, `sleeptrain-1weepvu`, `sleeptrain-1wejdw6`, `sleeptrain-1wen7kf`, `sleeptrain-1wet47q`, `sleeptrain-1wev872`, `sleeptrain-1wf0b3w`, `sleeptrain-1wf0hsn`, `sleeptrain-1wf1cch`, `sleeptrain-1wf55gr`, `sleeptrain-1wf9bl3`, `sleeptrain-1wfawtw`, `sleeptrain-1wfdni6`, `sleeptrain-1wfe3xu`, `sleeptrain-1wfih2w`, `sleeptrain-1wfjkxp`, `sleeptrain-1wfnqlz`, `sleeptrain-1wfpupd`, `sleeptrain-1wfs2rj`, `sleeptrain-1wftv9w`, `sleeptrain-1wfuncp`, `sleeptrain-1wfwtf6`, `toddlers-1wc7r76`, `toddlers-1wcgjqw`, `toddlers-1wcmcam`, `toddlers-1wd4wff`, `toddlers-1wd9mfo`, `toddlers-1we0yp9`, `toddlers-1we1nia`, `toddlers-1we7gs0`, `toddlers-1wensba`, `toddlers-1weov88`, `toddlers-1wf7yj6`, `toddlers-1wfk1ns`.

### R09 — `sources/reddit-reading-r09.md`

**Subject-based whole-unit ledger references (1):** `NewParents-1witiab`.

**Subject-based passage ledger references (7):** `NewParents-1wgqgh9`, `NewParents-1whmbw3`, `NewParents-1whmhs4`, `NewParents-1wik6au`, `Parenting-1wgdd9i`, `ScienceBasedParenting-1wgzv7g`, `sleeptrain-1wgl6a4`.

**Other skipped/partly quoted ledger references (5):** `Mommit-1wgajfg`, `Mommit-1wgq6gf`, `Mommit-1whdtqf`, `NewParents-1wijuim`, `beyondthebump-1whcej6`.

**Additional working-log review candidates (7):** `NewParents-1wgrv8w`, `sleeptrain-1wgqpuo`, `sleeptrain-1wh9wro`, `sleeptrain-1whdtaa`, `sleeptrain-1whnwxz`, `toddlers-1wgnawc`, `toddlers-1wiof0c`.

### R10 — `sources/reddit-reading-r10.md`

**Subject-based whole-unit ledger references (4):** `FirstTimeMom-1wltf5u`, `NewParents-1wk5ebm`, `NewParents-1wmal5l`, `toddlers-1wjpp01`.

**Subject-based passage ledger references (10):** `FirstTimeMom-1wiyukm`, `NewParents-1wjujfy`, `NewParents-1wl72ux`, `ScienceBasedParenting-1wk0t1i`, `beyondthebumpUK-1wkt6xo`, `sleeptrain-1wjgpio`, `sleeptrain-1wjph0n`, `sleeptrain-1wkimp2`, `sleeptrain-1wldili`, `sleeptrain-1wlf9bb`.

**Other skipped/partly quoted ledger references (5):** `Mommit-1wkvx9n`, `beyondthebump-1wjj60s`, `sleeptrain-1wkhrtj`, `sleeptrain-1wl0p56`, `sleeptrain-1wlg2hm`.

**Additional reader-note review candidates (19):** `FirstTimeMom-1wldvwc`, `Mommit-1wkxylm`, `NewParents-1wixkfw`, `Parenting-1wluh9g`, `beyondthebump-1wm181m`, `beyondthebumpUK-1wjmef8`, `daddit-1wjek9j`, `sleeptrain-1wiy4hu`, `sleeptrain-1wjj9kc`, `sleeptrain-1wjmkis`, `sleeptrain-1wk1iii`, `sleeptrain-1wk8g40`, `sleeptrain-1wkb92e`, `sleeptrain-1wl81lc`, `sleeptrain-1wmauwr`, `sleeptrain-1wmfl8x`, `toddlers-1wjzndt`, `toddlers-1wkbtu5`, `toddlers-1wl60qa`.

### R11 — `sources/reddit-reading-r11.md`

**Subject-based passage ledger references (11):** `Mommit-1wmqdvl`, `NewParents-1wmwhos`, `NewParents-1wn4dl1`, `NewParents-1wocngi`, `NewParents-1wphv6k`, `beyondthebump-1wnxwuw`, `beyondthebumpUK-1wovbqs`, `daddit-1woyr6q`, `sleeptrain-1woj4c1`, `sleeptrain-1wp1j29`, `sleeptrain-1wp3v7e`.

**Additional reader-note review candidates (4):** `beyondthebump-1wohglc`, `sleeptrain-1wnklg2`, `sleeptrain-1wno8q3`, `sleeptrain-1wodeju`.

### R12 — `sources/reddit-reading-r12.md`

**Subject-based whole-unit ledger references (1):** `NewParents-1wrf610`.

**Subject-based passage ledger references (11):** `NewParents-1wq8qie`, `NewParents-1wqacg1`, `NewParents-1wrm7kt`, `daddit-1wt8f67`, `daddit-1wward4`, `sleeptrain-1wyavk3`, `sleeptrain-1wz22a7`, `sleeptrain-1wzdsid`, `sleeptrain-1wzr88o`, `sleeptrain-1wzurf5`, `toddlers-1x0d5sw`.

**Other skipped/partly quoted ledger references (1):** `sleeptrain-1wzl25l`.

**Additional working-log review candidates (1):** `daddit-1wvl86l`.

**Additional reader-note review candidates (1):** `NewParents-1wqllbo`.

**Unmapped category review candidates (55):** `NewParents-1wptfrk`, `NewParents-1wpu3ic`, `NewParents-1wpuzxp`, `NewParents-1wq26js`, `NewParents-1wqwrpu`, `NewParents-1wrt7w5`, `ScienceBasedParenting-1wzmkyc`, `daddit-1wq99u4`, `daddit-1wytrl8`, `sleeptrain-1wya8u3`, `sleeptrain-1wyaizm`, `sleeptrain-1wyeeub`, `sleeptrain-1wyej86`, `sleeptrain-1wyeoso`, `sleeptrain-1wygd36`, `sleeptrain-1wyic3t`, `sleeptrain-1wyioo7`, `sleeptrain-1wyj8ac`, `sleeptrain-1wyjopn`, `sleeptrain-1wyolvj`, `sleeptrain-1wyr16f`, `sleeptrain-1wyrgcv`, `sleeptrain-1wyvxjc`, `sleeptrain-1wyxugm`, `sleeptrain-1wz02ja`, `sleeptrain-1wz10w4`, `sleeptrain-1wz3n9e`, `sleeptrain-1wz5f84`, `sleeptrain-1wz67uc`, `sleeptrain-1wz8ra4`, `sleeptrain-1wz9ys8`, `sleeptrain-1wzaj43`, `sleeptrain-1wzc9gh`, `sleeptrain-1wzcqwg`, `sleeptrain-1wzem7g`, `sleeptrain-1wziwv5`, `sleeptrain-1wzlgss`, `sleeptrain-1wzn64z`, `sleeptrain-1wznfzj`, `sleeptrain-1wznx26`, `sleeptrain-1wzp4iy`, `sleeptrain-1wzqyic`, `sleeptrain-1wztroa`, `sleeptrain-1wzwyx7`, `sleeptrain-1wzxk8l`, `sleeptrain-1wzxor3`, `sleeptrain-1x02fj9`, `sleeptrain-1x084l7`, `sleeptrain-1x08l10`, `sleeptrain-1x0buzp`, `sleeptrain-1x0cnan`, `toddlers-1wy38hi`, `toddlers-1wymjqb`, `toddlers-1wzsa9g`, `toddlers-1x01cgk`.

### R13 — `sources/reddit-reading-r13.md`

**Subject-based whole-unit ledger references (5):** `NewParents-1wzd6i8`, `NewParents-1x34xct`, `beyondthebump-1wykpw5`, `beyondthebump-1xctqsr`, `beyondthebumpUK-1x5mqu0`.

**Subject-based passage ledger references (14):** `FirstTimeMom-1xcpe2h`, `NewParents-1wshay4`, `NewParents-1wvytj6`, `NewParents-1x0vxy1`, `NewParents-1x2fpzu`, `NewParents-1x2pein`, `NewParents-1x2wzz2`, `NewParents-1x4no2l`, `beyondthebumpUK-1wzqvuy`, `beyondthebumpUK-1x3ir5j`, `sleeptrain-1wwlawg`, `sleeptrain-1wxy229`, `sleeptrain-1x92yfi`, `sleeptrain-1x9c6j8`.

**Unmapped category review candidates (106):** `Mommit-1wvzsoa`, `Mommit-1x4krb3`, `NewParents-1wwfqr6`, `NewParents-1wxygrd`, `NewParents-1x0y5kq`, `NewParents-1x2fcw7`, `NewParents-1x7fbyb`, `NewParents-1x8h5ui`, `NewParents-1xbm9i1`, `NewParents-1xbwaxs`, `NewParents-1xc03wo`, `beyondthebump-1wpvngj`, `beyondthebump-1wrasjs`, `beyondthebump-1wsb5ix`, `beyondthebump-1wu2fqt`, `beyondthebump-1x28ee6`, `beyondthebump-1x552qz`, `beyondthebump-1x9ngjg`, `beyondthebumpUK-1wuervk`, `beyondthebumpUK-1ww70o0`, `beyondthebumpUK-1wwz4gp`, `beyondthebumpUK-1x0z7ue`, `beyondthebumpUK-1x62noy`, `beyondthebumpUK-1x6fqgn`, `daddit-1x4i0jx`, `sahm-1xdtjo3`, `sleeptrain-1wqe5ox`, `sleeptrain-1wr0c28`, `sleeptrain-1wrcsar`, `sleeptrain-1wrqgst`, `sleeptrain-1wru3az`, `sleeptrain-1wrx8a1`, `sleeptrain-1ws3m1u`, `sleeptrain-1ws58sy`, `sleeptrain-1wsi77i`, `sleeptrain-1wsr744`, `sleeptrain-1wt80q0`, `sleeptrain-1wu1aof`, `sleeptrain-1wullyg`, `sleeptrain-1wuq7nl`, `sleeptrain-1wv0c78`, `sleeptrain-1wvjwsz`, `sleeptrain-1wvq8xs`, `sleeptrain-1wvx58k`, `sleeptrain-1ww8p3j`, `sleeptrain-1wxqb6k`, `sleeptrain-1wxrrq3`, `sleeptrain-1wy3s76`, `sleeptrain-1wy7b3w`, `sleeptrain-1wy96t0`, `sleeptrain-1x12k4k`, `sleeptrain-1x1amzb`, `sleeptrain-1x1v40b`, `sleeptrain-1x260fh`, `sleeptrain-1x2akqs`, `sleeptrain-1x2mskb`, `sleeptrain-1x2qwr4`, `sleeptrain-1x2t2vp`, `sleeptrain-1x3att3`, `sleeptrain-1x3gj3r`, `sleeptrain-1x3h9dx`, `sleeptrain-1x3pzvm`, `sleeptrain-1x3sqmh`, `sleeptrain-1x49d74`, `sleeptrain-1x4r1ub`, `sleeptrain-1x4w7t2`, `sleeptrain-1x55uj8`, `sleeptrain-1x5fhps`, `sleeptrain-1x5foxq`, `sleeptrain-1x5k2qu`, `sleeptrain-1x61oof`, `sleeptrain-1x7f8sz`, `sleeptrain-1x7s3lr`, `sleeptrain-1x7v29i`, `sleeptrain-1x7z0r7`, `sleeptrain-1x89e9i`, `sleeptrain-1x8hv51`, `sleeptrain-1x8nyvq`, `sleeptrain-1x8w8so`, `sleeptrain-1x952j9`, `sleeptrain-1x99yep`, `sleeptrain-1x9b8en`, `sleeptrain-1x9g9fd`, `sleeptrain-1x9vaem`, `sleeptrain-1xa220s`, `sleeptrain-1xadgsv`, `sleeptrain-1xaixrr`, `sleeptrain-1xatmjl`, `sleeptrain-1xbnld4`, `sleeptrain-1xbuwdk`, `sleeptrain-1xby01p`, `sleeptrain-1xcbqe0`, `sleeptrain-1xcddf9`, `sleeptrain-1xcfrm1`, `sleeptrain-1xchbcv`, `sleeptrain-1xcmw6p`, `sleeptrain-1xcwhi4`, `sleeptrain-1xcy90v`, `sleeptrain-1xd2gbc`, `sleeptrain-1xdfq3r`, `sleeptrain-1xdhv8a`, `sleeptrain-1xe5hy6`, `sleeptrain-1xedvpk`, `toddlers-1x3ose5`, `toddlers-1x4n2an`, `toddlers-1xdhll2`.

### R14 — `sources/reddit-reading-r14.md`

**Subject-based whole-unit ledger references (6):** `AttachmentParenting-1wr1ed0`, `AttachmentParenting-1wr50kz`, `NewParents-1wyeyva`, `NewParents-1xeaf94`, `Parenting-1wqfs8o`, `sahm-1xdqj43`.

**Subject-based passage ledger references (9):** `Mommit-1wqfiov`, `NewParents-1x3il0i`, `NewParents-1x46ift`, `beyondthebump-1wpifnt`, `beyondthebumpUK-1wph47q`, `sleeptrain-1wq5f45`, `sleeptrain-1wq9vwk`, `sleeptrain-1wqfwub`, `sleeptrain-1xe3cw8`.

**Other skipped/partly quoted ledger references (3):** `FirstTimeMom-1wtdhm8`, `Parenting-1wpgthh`, `beyondthebump-1wyf8qj`.

### R15 — `sources/reddit-reading-r15.md`

**Subject-based whole-unit ledger references (5):** `NewParents-1wsno03`, `NewParents-1wstnpg`, `NewParents-1wtkgtm`, `Parenting-1wsjwas`, `sleeptrain-1wrvyg6`.

**Subject-based passage ledger references (15):** `NewParents-1ws9ddl`, `NewParents-1wtp5yd`, `beyondthebump-1wt4hzq`, `beyondthebump-1wtdphx`, `sleeptrain-1wrsbc9`, `sleeptrain-1ws1d58`, `sleeptrain-1ws8nvn`, `sleeptrain-1wsmzb1`, `sleeptrain-1wsqaw1`, `sleeptrain-1wsw0os`, `sleeptrain-1wt1q9t`, `sleeptrain-1wtgqyz`, `toddlers-1wr92aq`, `toddlers-1wspjah`, `toddlers-1wtibnj`.

**Other skipped/partly quoted ledger references (2):** `beyondthebump-1wsqdba`, `toddlers-1wtu8lb`.

**Additional reader-note review candidates (2):** `sleeptrain-1wrfyj9`, `sleeptrain-1wtqcl7`.

### R16 — `sources/reddit-reading-r16.md`

**Subject-based whole-unit ledger references (9):** `AttachmentParenting-1ww3dtr`, `Mommit-1wwx17a`, `NewParents-1wvwwk5`, `NewParents-1wwjf6g`, `NewParents-1wxgr8o`, `Parenting-1wxan8x`, `beyondthebump-1wvhd1s`, `beyondthebump-1wwyt0d`, `beyondthebumpUK-1wu38ap`.

**Subject-based passage ledger references (20):** `AttachmentParenting-1www5pz`, `NewParents-1wupa4s`, `NewParents-1wurye0`, `NewParents-1wv1aba`, `NewParents-1ww0nkm`, `NewParents-1wwzsvd`, `Parenting-1wwkq33`, `Parenting-1wx5pc6`, `beyondthebump-1wvky8d`, `beyondthebump-1wwiffj`, `sleeptrain-1wu59k5`, `sleeptrain-1wuw38n`, `sleeptrain-1wvqxoc`, `sleeptrain-1wvurt7`, `sleeptrain-1ww4i62`, `sleeptrain-1wx19c5`, `sleeptrain-1wx31nc`, `sleeptrain-1wxicii`, `toddlers-1wva4bl`, `toddlers-1wx58je`.

**Other skipped/partly quoted ledger references (5):** `NewParents-1wu5alx`, `sleeptrain-1wu3bdp`, `sleeptrain-1wuvpp2`, `sleeptrain-1wuww8o`, `sleeptrain-1wxaitr`.

### R17 — `sources/reddit-reading-r17.md`

**Subject-based whole-unit ledger references (5):** `Mommit-1x1fbhj`, `NewParents-1wznc4o`, `NewParents-1x06br2`, `NewParents-1x2a6fd`, `sleeptrain-1x212de`.

**Subject-based passage ledger references (22):** `AttachmentParenting-1wzhybp`, `AttachmentParenting-1x0k0qy`, `Mommit-1x0e0p8`, `NewParents-1wzmq1i`, `NewParents-1wzmwqf`, `NewParents-1x0ei0f`, `NewParents-1x0f17c`, `NewParents-1x0uzt7`, `NewParents-1x176k6`, `NewParents-1x1ccxd`, `beyondthebump-1wy4p5g`, `beyondthebump-1wyp8ak`, `beyondthebump-1wzvmjl`, `beyondthebump-1x1b0v8`, `beyondthebumpUK-1x1nna2`, `sleeptrain-1wy1012`, `sleeptrain-1x0dh04`, `sleeptrain-1x112zg`, `sleeptrain-1x11imt`, `sleeptrain-1x25qdb`, `toddlers-1wxxdyt`, `toddlers-1x1gsbe`.

**Additional working-log review candidates (7):** `NewParents-1wz51rt`, `NewParents-1x1aqu9`, `beyondthebump-1wz564w`, `beyondthebump-1x1aoyd`, `beyondthebump-1x22714`, `beyondthebumpUK-1wxpq55`, `toddlers-1x1emac`.

### R18 — `sources/reddit-reading-r18.md`

**Subject-based whole-unit ledger references (9):** `AttachmentParenting-1x2qq2m`, `AttachmentParenting-1x2wpcg`, `FirstTimeMom-1x4oi07`, `Mommit-1x4u4vu`, `Mommit-1x5dzg9`, `beyondthebump-1x3qt5w`, `beyondthebumpUK-1x2rs3u`, `toddlers-1x36utj`, `toddlers-1x4ijmm`.

**Subject-based passage ledger references (55):** `AttachmentParenting-1x2ua8v`, `AttachmentParenting-1x2wk68`, `AttachmentParenting-1x3n586`, `AttachmentParenting-1x3pd8w`, `AttachmentParenting-1x3sgqz`, `FirstTimeMom-1x4g4oo`, `Mommit-1x39ogo`, `Mommit-1x5682t`, `NewParents-1x2sczf`, `NewParents-1x3d4y2`, `NewParents-1x40uf4`, `NewParents-1x48g8o`, `NewParents-1x48t21`, `NewParents-1x4l8f7`, `NewParents-1x4whdc`, `NewParents-1x570bf`, `Parenting-1x4uu4g`, `beyondthebump-1x2chn5`, `beyondthebump-1x3qjkc`, `beyondthebump-1x4z6r6`, `beyondthebump-1x5700m`, `beyondthebumpUK-1x3qe40`, `sahm-1x3m9lb`, `sleeptrain-1x2c19u`, `sleeptrain-1x2dxhk`, `sleeptrain-1x2muw8`, `sleeptrain-1x2whdg`, `sleeptrain-1x3ddtg`, `sleeptrain-1x3im6b`, `sleeptrain-1x3jd85`, `sleeptrain-1x3q5j4`, `sleeptrain-1x3t9o3`, `sleeptrain-1x3wqsc`, `sleeptrain-1x3yc8z`, `sleeptrain-1x3yinp`, `sleeptrain-1x3ys8w`, `sleeptrain-1x41wz2`, `sleeptrain-1x44lgi`, `sleeptrain-1x45k7j`, `sleeptrain-1x45lbs`, `sleeptrain-1x4845c`, `sleeptrain-1x4az9c`, `sleeptrain-1x4ebmn`, `sleeptrain-1x4h1js`, `sleeptrain-1x4ib9p`, `sleeptrain-1x4iktz`, `sleeptrain-1x4imyz`, `sleeptrain-1x4pk6b`, `sleeptrain-1x4r8gn`, `sleeptrain-1x4yv8h`, `sleeptrain-1x51gom`, `sleeptrain-1x58rwl`, `sleeptrain-1x5dvee`, `toddlers-1x3esk0`, `toddlers-1x3lx0g`.

**Other skipped/partly quoted ledger references (6):** `Mommit-1x40bsg`, `NewParents-1x4c5ua`, `NewParents-1x4ecyb`, `beyondthebump-1x571kw`, `sleeptrain-1x2h0ln`, `toddlers-1x3xcyh`.

**Additional working-log review candidates (3):** `daddit-1x4k1ru`, `sleeptrain-1x3nm4j`, `toddlers-1x44853`.

**Additional reader-note review candidates (1):** `Mommit-1x2bz4u`.

### R19 — `sources/reddit-reading-r19.md`

**Subject-based whole-unit ledger references (6):** `Mommit-1x5v1x3`, `Mommit-1x68mc9`, `NewParents-1x82hb6`, `beyondthebump-1x5sgiu`, `beyondthebumpUK-1x7a4ct`, `sleeptrain-1x5hfo0`.

**Subject-based passage ledger references (32):** `AttachmentParenting-1x7ko40`, `Mommit-1x6mh7e`, `Mommit-1x6o4bi`, `Mommit-1x7gcns`, `NewParents-1x5jp8f`, `NewParents-1x69z9l`, `NewParents-1x70ujg`, `NewParents-1x72ci4`, `NewParents-1x73xwi`, `NewParents-1x7bpeg`, `Parenting-1x67ow6`, `beyondthebump-1x7hexl`, `beyondthebumpUK-1x5l1l7`, `beyondthebumpUK-1x6u1s2`, `sleeptrain-1x5go9r`, `sleeptrain-1x5h406`, `sleeptrain-1x5q4q4`, `sleeptrain-1x5rv7i`, `sleeptrain-1x5tj7k`, `sleeptrain-1x62qc3`, `sleeptrain-1x62zjo`, `sleeptrain-1x63bep`, `sleeptrain-1x6f5lj`, `sleeptrain-1x6ult3`, `sleeptrain-1x7rqaw`, `sleeptrain-1x7tqpg`, `sleeptrain-1x85htv`, `sleeptrain-1x863dd`, `toddlers-1x5hepy`, `toddlers-1x5oion`, `toddlers-1x6sg6t`, `toddlers-1x7y4sp`.

**Other skipped/partly quoted ledger references (2):** `Mommit-1x5gous`, `beyondthebumpUK-1x5w35p`.

### R20 — `sources/reddit-reading-r20.md`

**Subject-based whole-unit ledger references (5):** `GentleParenting-1x8tzjs`, `NewParents-1x9ypaz`, `Parenting-1xaoncf`, `beyondthebump-1x9vb15`, `sleeptrain-1xbaleb`.

**Subject-based passage ledger references (22):** `AttachmentParenting-1xa3fub`, `FirstTimeMom-1xau13r`, `Mommit-1x8qwo3`, `NewParents-1x8lh9u`, `NewParents-1x96myg`, `NewParents-1x9gsdl`, `NewParents-1xafkw4`, `NewParents-1xb0xjf`, `NewParents-1xb2lmn`, `NewParents-1xb2p6j`, `beyondthebump-1x9xqdu`, `beyondthebump-1xb7jqh`, `beyondthebumpUK-1xavjal`, `sleeptrain-1x8ai8u`, `sleeptrain-1x9jmds`, `sleeptrain-1x9uj7m`, `sleeptrain-1x9wsux`, `sleeptrain-1xa8vhu`, `sleeptrain-1xafy0s`, `sleeptrain-1xag4d0`, `sleeptrain-1xb36kw`, `toddlers-1xaurm9`.

**Other skipped/partly quoted ledger references (2):** `Mommit-1xb1gv3`, `beyondthebump-1xa292l`.

**Additional reader-note review candidates (2):** `beyondthebumpUK-1x9q9fx`, `sleeptrain-1xad6iv`.

### R21 — `sources/reddit-reading-r21.md`

**Subject-based whole-unit ledger references (13):** `AttachmentParenting-1xd7zm7`, `AttachmentParenting-1xdx5hp`, `AttachmentParenting-1xeanbp`, `NewParents-1xbtpx3`, `NewParents-1xc6jgg`, `NewParents-1xcuv43`, `Parenting-1xdoapx`, `ScienceBasedParenting-1xdvj9k`, `beyondthebumpUK-1xd05x7`, `sleeptrain-1xbi07t`, `sleeptrain-1xcrwf0`, `toddlers-1xcga5j`, `toddlers-1xco5gr`.

**Subject-based passage ledger references (46):** `AttachmentParenting-1xc4mc3`, `AttachmentParenting-1xejkea`, `FirstTimeMom-1xd91pn`, `NewParents-1xbcxxz`, `NewParents-1xblksb`, `NewParents-1xbvmk1`, `NewParents-1xc25fw`, `NewParents-1xefpci`, `Parenting-1xby662`, `beyondthebump-1xblg5d`, `beyondthebump-1xeam9o`, `beyondthebumpUK-1xbgwav`, `beyondthebumpUK-1xcapzp`, `beyondthebumpUK-1xci6ce`, `sleeptrain-1xbb2bo`, `sleeptrain-1xbmvf3`, `sleeptrain-1xbryo5`, `sleeptrain-1xbvtc0`, `sleeptrain-1xbxndj`, `sleeptrain-1xbyctc`, `sleeptrain-1xc2muq`, `sleeptrain-1xc73bg`, `sleeptrain-1xc7l44`, `sleeptrain-1xcdymz`, `sleeptrain-1xclpdh`, `sleeptrain-1xctz6x`, `sleeptrain-1xcurva`, `sleeptrain-1xcxk73`, `sleeptrain-1xcy0uv`, `sleeptrain-1xd4ygf`, `sleeptrain-1xd650n`, `sleeptrain-1xd9e93`, `sleeptrain-1xd9s7g`, `sleeptrain-1xdbr90`, `sleeptrain-1xdguyr`, `sleeptrain-1xdgx2o`, `sleeptrain-1xdhrgy`, `sleeptrain-1xdlkji`, `sleeptrain-1xdpc3c`, `sleeptrain-1xducsd`, `sleeptrain-1xdxxf2`, `toddlers-1xbqbwk`, `toddlers-1xcg5lx`, `toddlers-1xcvd18`, `toddlers-1xd0i9m`, `toddlers-1xd5bft`.

**Other skipped/partly quoted ledger references (1):** `beyondthebump-1xdz4p0`.

**Additional reader-note review candidates (1):** `sleeptrain-1xe8qin`.

### R22 — `sources/reddit-reading-r22.md`

**Subject-based whole-unit ledger references (9):** `Mommit-1ukxb51`, `Mommit-1v5xo8r`, `NewParents-1ugegyp`, `NewParents-1vl3uxi`, `beyondthebump-1vj3g72`, `daddit-1un930m`, `sleeptrain-1v41coy`, `sleeptrain-1vizehy`, `toddlers-1ut838u`.

**Other skipped/partly quoted ledger references (2):** `sleeptrain-1ufvke4`, `toddlers-1uf16v2`.

**Additional working-log review candidates (1):** `daddit-1ufvmjk`.

**Additional reader-note review candidates (2):** `NewParents-1uvw9vb`, `sleeptrain-1uwp9cl`.

### R23 — `sources/reddit-reading-r23.md`

**Subject-based whole-unit ledger references (1):** `NewParents-1ukhgat`.

**Subject-based passage ledger references (31):** `AttachmentParenting-1vtlfaj`, `FirstTimeMom-1vmoeb8`, `NewParents-1ugqdcr`, `NewParents-1uikj0g`, `NewParents-1usv0lv`, `NewParents-1vvq4at`, `NewParents-1vw7uqh`, `Parenting-1ukwmkp`, `beyondthebump-1vag2u0`, `beyondthebump-1vp2oee`, `sleeptrain-1uk7vtn`, `sleeptrain-1uke8ac`, `sleeptrain-1ulxjdq`, `sleeptrain-1uqdyh2`, `sleeptrain-1utfyhl`, `sleeptrain-1uxzgsu`, `sleeptrain-1v06qu9`, `sleeptrain-1v0b7dk`, `sleeptrain-1v3chjv`, `sleeptrain-1v3w4i7`, `sleeptrain-1v4ngky`, `sleeptrain-1v7pn5m`, `sleeptrain-1veizmd`, `sleeptrain-1vfv351`, `sleeptrain-1vh15er`, `sleeptrain-1vl2uoe`, `sleeptrain-1vmyet5`, `sleeptrain-1vvl10e`, `sleeptrain-1vwa77w`, `sleeptrain-1vwzfj7`, `toddlers-1ve33m9`.

**Other skipped/partly quoted ledger references (4):** `NewParents-1vu42zg`, `sleeptrain-1up6oeh`, `sleeptrain-1vxic9z`, `toddlers-1v4j049`.

### R24 — `sources/reddit-reading-r24.md`

**Subject-based whole-unit ledger references (5):** `Mommit-1vm81uz`, `NewParents-1ufh4yh`, `beyondthebump-1ug5ra6`, `beyondthebump-1va46h8`, `sleeptrain-1vw4qd2`.

**Subject-based passage ledger references (42):** `AttachmentParenting-1ugvls3`, `AttachmentParenting-1vmh60t`, `FirstTimeMom-1v8g08g`, `Mommit-1uevm3z`, `Mommit-1ufrdp8`, `Mommit-1ug38ik`, `Mommit-1vq9oxy`, `NewParents-1uex70m`, `NewParents-1ufboux`, `NewParents-1ufd7zh`, `NewParents-1ufqcfi`, `NewParents-1ufru81`, `NewParents-1ugqj95`, `NewParents-1uh44kn`, `Parenting-1uewisx`, `Parenting-1ugqms1`, `Parenting-1v8of9t`, `beyondthebump-1uf75a5`, `beyondthebump-1ug71rg`, `beyondthebump-1uggsfo`, `beyondthebump-1ugxgqc`, `beyondthebump-1uh388s`, `beyondthebump-1vklw8s`, `beyondthebump-1vq8qtc`, `beyondthebumpUK-1v7dn5w`, `beyondthebumpUK-1vae5cy`, `daddit-1ufiopb`, `sleeptrain-1uf3ank`, `sleeptrain-1ufc48m`, `sleeptrain-1ufmsei`, `sleeptrain-1ufzyb4`, `sleeptrain-1ug3ml0`, `sleeptrain-1ug7hjm`, `sleeptrain-1ugv2i6`, `sleeptrain-1ugvy6m`, `sleeptrain-1uh2sdf`, `sleeptrain-1v4tun2`, `sleeptrain-1vpkih2`, `toddlers-1uf6npm`, `toddlers-1ufiupn`, `toddlers-1ufn8y4`, `workingmoms-1uh365k`.

**Other skipped/partly quoted ledger references (5):** `NewParents-1uftrqq`, `beyondthebump-1ugvo34`, `daddit-1ufktk6`, `sleeptrain-1ufh34r`, `sleeptrain-1va46xi`.

### R25 — `sources/reddit-reading-r25.md`

**Subject-based whole-unit ledger references (8):** `Mommit-1ujfqc7`, `NewParents-1uhmtqa`, `NewParents-1ui0ugf`, `NewParents-1ui8m7m`, `Parenting-1ujqpru`, `beyondthebumpUK-1uj5rts`, `sleeptrain-1uhrjpb`, `toddlers-1ujqgeh`.

**Subject-based passage ledger references (18):** `AttachmentParenting-1uic400`, `AttachmentParenting-1uk5cfx`, `FirstTimeMom-1uhsoho`, `Mommit-1ui3mzr`, `Mommit-1ujw8s9`, `NewParents-1ujc93w`, `NewParents-1ujt9b7`, `NewParents-1uk4jfb`, `Parenting-1ujnhu3`, `beyondthebump-1uhqdcq`, `sleeptrain-1uhk4od`, `sleeptrain-1uhl91n`, `sleeptrain-1uhw86q`, `sleeptrain-1uizje7`, `sleeptrain-1ujprvh`, `sleeptrain-1ujzcav`, `toddlers-1uif24e`, `workingmoms-1ui64li`.

**Other skipped/partly quoted ledger references (8):** `AttachmentParenting-1uhx2x4`, `AttachmentParenting-1uk3i8t`, `Mommit-1uk3r9o`, `NewParents-1uhasj4`, `sleeptrain-1uhblij`, `toddlers-1uifx68`, `toddlers-1uipiq5`, `toddlers-1uk6s5w`.

### R26 — `sources/reddit-reading-r26.md`

**Subject-based whole-unit ledger references (7):** `Mommit-1um6jim`, `NewParents-1ul7zt2`, `NewParents-1um6nk3`, `NewParents-1unawhe`, `beyondthebump-1umcn5f`, `sleeptrain-1um15y0`, `toddlers-1ult75k`.

**Subject-based passage ledger references (73):** `AttachmentParenting-1ulim8k`, `AttachmentParenting-1ume1xb`, `FirstTimeMom-1ukyt2p`, `FirstTimeMom-1umezph`, `Mommit-1ukng9t`, `Mommit-1umvu94`, `NewParents-1uk9os2`, `NewParents-1uklax3`, `NewParents-1ukockz`, `NewParents-1ukpo5l`, `NewParents-1ul3897`, `NewParents-1uli1to`, `NewParents-1ultt14`, `NewParents-1ulwa8x`, `NewParents-1um65ce`, `NewParents-1um85tb`, `NewParents-1um9tnc`, `NewParents-1umbnek`, `NewParents-1umfc7w`, `NewParents-1umgiaf`, `Parenting-1ul00av`, `Parenting-1ull7lz`, `beyondthebump-1ukdcgx`, `beyondthebump-1ukkcq7`, `beyondthebump-1um9sqc`, `beyondthebump-1umcx0i`, `daddit-1ula7xd`, `sleeptrain-1ukar8q`, `sleeptrain-1ukc48z`, `sleeptrain-1ukdw26`, `sleeptrain-1ukl3fl`, `sleeptrain-1uknbkc`, `sleeptrain-1ukpnio`, `sleeptrain-1ukpsuy`, `sleeptrain-1ukw6rl`, `sleeptrain-1ukyk5e`, `sleeptrain-1ul3org`, `sleeptrain-1ulc8qd`, `sleeptrain-1ulex7k`, `sleeptrain-1ulg9ws`, `sleeptrain-1ulgfdu`, `sleeptrain-1uljr29`, `sleeptrain-1ull3u1`, `sleeptrain-1ullsq6`, `sleeptrain-1uloncq`, `sleeptrain-1ulqk6d`, `sleeptrain-1ulymm5`, `sleeptrain-1ulzwu8`, `sleeptrain-1um48z9`, `sleeptrain-1um4nys`, `sleeptrain-1um4vk0`, `sleeptrain-1um6wyh`, `sleeptrain-1umbtcc`, `sleeptrain-1umcskh`, `sleeptrain-1umf3mf`, `sleeptrain-1umjprq`, `sleeptrain-1umllph`, `sleeptrain-1umnhqe`, `sleeptrain-1umnyq7`, `sleeptrain-1umpyx0`, `sleeptrain-1umzhq8`, `sleeptrain-1un00fe`, `sleeptrain-1un20mm`, `sleeptrain-1un8ksh`, `sleeptrain-1unb4wd`, `sleeptrain-1uncumg`, `sleeptrain-1unf4s9`, `sleeptrain-1ungff1`, `sleeptrain-1unh1vi`, `toddlers-1ukfptl`, `toddlers-1ul9snv`, `toddlers-1umy8u4`, `toddlers-1un8mcs`.

**Other skipped/partly quoted ledger references (16):** `AttachmentParenting-1ul6yyd`, `AttachmentParenting-1um2g2l`, `NewParents-1ulp2sq`, `NewParents-1ulzw3v`, `NewParents-1umajsw`, `NewParents-1umm0iw`, `NewParents-1un7li7`, `NewParents-1un8al8`, `beyondthebump-1ukk691`, `beyondthebump-1umc1rt`, `sleeptrain-1ukglp1`, `sleeptrain-1uknk0b`, `sleeptrain-1umlyqv`, `sleeptrain-1un2yfr`, `toddlers-1ulgnrx`, `toddlers-1umo6t5`.

### R27 — `sources/reddit-reading-r27.md`

**Subject-based whole-unit ledger references (8):** `Mommit-1upnk23`, `Mommit-1uqiakq`, `beyondthebump-1uojbpq`, `beyondthebump-1uq5nik`, `beyondthebumpUK-1uost71`, `beyondthebumpUK-1uou0ef`, `toddlers-1up2ohg`, `toddlers-1up32no`.

**Subject-based passage ledger references (45):** `AttachmentParenting-1upqa6d`, `AttachmentParenting-1upqhm2`, `FirstTimeMom-1up1zkp`, `Mommit-1uodrau`, `Mommit-1uolf9g`, `Mommit-1uov94c`, `Mommit-1upg1v6`, `Mommit-1uqi79s`, `Mommit-1uqi7s2`, `NewParents-1unjeeo`, `NewParents-1uolxp4`, `NewParents-1uoq7f0`, `NewParents-1up1mdf`, `NewParents-1up405a`, `NewParents-1up7ye5`, `NewParents-1uphj99`, `NewParents-1uq5jq1`, `NewParents-1uq8udg`, `Parenting-1uokmkj`, `Parenting-1uq4lyj`, `Parenting-1uqe6i9`, `beyondthebumpUK-1unku2n`, `beyondthebumpUK-1uozj06`, `beyondthebumpUK-1upoop5`, `beyondthebumpUK-1uqa8lk`, `sleeptrain-1unqbcc`, `sleeptrain-1unrt37`, `sleeptrain-1unx5en`, `sleeptrain-1uom4n9`, `sleeptrain-1uoojn9`, `sleeptrain-1uowssd`, `sleeptrain-1uoy57g`, `sleeptrain-1up7fs8`, `sleeptrain-1upg52w`, `sleeptrain-1upkd6n`, `sleeptrain-1upkivl`, `sleeptrain-1upossh`, `sleeptrain-1upx6c9`, `sleeptrain-1upzc1t`, `sleeptrain-1upzsos`, `sleeptrain-1uqce4z`, `sleeptrain-1uqd6vt`, `sleeptrain-1uqios4`, `toddlers-1unna32`, `toddlers-1uochv0`.

**Other skipped/partly quoted ledger references (5):** `Mommit-1up50mz`, `NewParents-1uq9oub`, `Parenting-1upwj0h`, `sleeptrain-1uo81vq`, `toddlers-1uoknsj`.

**Additional working-log review candidates (3):** `NewParents-1up4ya2`, `beyondthebump-1uo8025`, `toddlers-1uprpvh`.

### R28 — `sources/reddit-reading-r28.md`

**Subject-based whole-unit ledger references (5):** `NewParents-1uqw2r2`, `NewParents-1usv1yg`, `NewParents-1utiv1w`, `beyondthebump-1urvaq8`, `beyondthebumpUK-1us21ai`.

**Subject-based passage ledger references (29):** `AttachmentParenting-1us7nu7`, `AttachmentParenting-1usczbt`, `NewParents-1ur3jaq`, `NewParents-1uruami`, `NewParents-1usulr9`, `NewParents-1uszboq`, `Parenting-1urpqyf`, `ScienceBasedParenting-1ura5hr`, `beyondthebump-1urw7k4`, `beyondthebump-1us1ekv`, `beyondthebump-1usbvfb`, `beyondthebump-1ut2xku`, `beyondthebump-1utg65l`, `sahm-1ut6e9p`, `sleeptrain-1uqwwrr`, `sleeptrain-1ur8qk9`, `sleeptrain-1urk1xt`, `sleeptrain-1urwtq1`, `sleeptrain-1us0yl8`, `sleeptrain-1us388s`, `sleeptrain-1usp42t`, `sleeptrain-1ust95b`, `sleeptrain-1utg5fy`, `sleeptrain-1utgvaa`, `sleeptrain-1utlz2k`, `sleeptrain-1utnr6j`, `sleeptrain-1utozgn`, `sleeptrain-1utsiwe`, `toddlers-1utj75w`.

### R29 — `sources/reddit-reading-r29.md`

**Subject-based whole-unit ledger references (7):** `AttachmentParenting-1uwj77y`, `NewParents-1uv45xu`, `NewParents-1uv8on2`, `NewParents-1uvylas`, `NewParents-1uwc5o9`, `sleeptrain-1uuwecq`, `toddlers-1uvtpbx`.

**Subject-based passage ledger references (44):** `AttachmentParenting-1uv3yay`, `AttachmentParenting-1uvsjwt`, `AttachmentParenting-1uvyc8d`, `NewParents-1uu42ps`, `NewParents-1uumo70`, `NewParents-1uuswst`, `NewParents-1uv25c7`, `NewParents-1uv26xf`, `NewParents-1uvsp6f`, `NewParents-1uw0nnb`, `Parenting-1uuz2ye`, `Parenting-1uuzlre`, `Parenting-1uv01nz`, `Parenting-1uvsfs7`, `beyondthebump-1uukdh0`, `beyondthebump-1uv97q1`, `beyondthebump-1uvc0u5`, `beyondthebump-1uvshkj`, `daddit-1uucgs3`, `daddit-1uvev7c`, `sleeptrain-1utzypz`, `sleeptrain-1uu8rxt`, `sleeptrain-1uug8qv`, `sleeptrain-1uuj0hl`, `sleeptrain-1uum34j`, `sleeptrain-1uuqdp8`, `sleeptrain-1uuup86`, `sleeptrain-1uuzw7l`, `sleeptrain-1uuzxh6`, `sleeptrain-1uv517x`, `sleeptrain-1uv688m`, `sleeptrain-1uv9wgr`, `sleeptrain-1uvg5b7`, `sleeptrain-1uvgpin`, `sleeptrain-1uvjf50`, `sleeptrain-1uvk9x4`, `sleeptrain-1uvrse2`, `sleeptrain-1uvxysb`, `sleeptrain-1uw6kdo`, `sleeptrain-1uwjcf2`, `toddlers-1uu5js0`, `toddlers-1uup9t2`, `toddlers-1uuu2hq`, `toddlers-1uvtltb`.

**Other skipped/partly quoted ledger references (5):** `NewParents-1uwatoz`, `Parenting-1uvuo81`, `beyondthebump-1uuppmq`, `beyondthebump-1uvf3lj`, `toddlers-1uuviqi`.

**Additional working-log review candidates (9):** `NewParents-1uuns4x`, `beyondthebump-1uv8vss`, `beyondthebump-1uvp9k4`, `sleeptrain-1uuubi3`, `sleeptrain-1uv8v6r`, `sleeptrain-1uvft9i`, `sleeptrain-1uw26ax`, `toddlers-1uv418i`, `toddlers-1uvkib7`.

### R30 — `sources/reddit-reading-r30.md`

**Subject-based whole-unit ledger references (4):** `AttachmentParenting-1uzb2at`, `NewParents-1ux7g4n`, `NewParents-1uzgd0w`, `toddlers-1uxr9k4`.

**Subject-based passage ledger references (36):** `AttachmentParenting-1uz2cve`, `Mommit-1ux7w6d`, `NewParents-1uwkr5h`, `NewParents-1uwvxgg`, `NewParents-1ux2tye`, `NewParents-1ux35hg`, `NewParents-1ux44me`, `NewParents-1uxed6r`, `beyondthebump-1uwjy7f`, `beyondthebump-1uwzuiu`, `beyondthebump-1ux96nw`, `beyondthebump-1ux9cok`, `beyondthebump-1uy8uez`, `beyondthebump-1uzt4zs`, `beyondthebumpUK-1uzposq`, `sleeptrain-1uwk4m3`, `sleeptrain-1ux3ar0`, `sleeptrain-1ux3gok`, `sleeptrain-1ux9cf2`, `sleeptrain-1uxbqxp`, `sleeptrain-1uxdsr0`, `sleeptrain-1uy9jwz`, `sleeptrain-1uyjezp`, `sleeptrain-1uyu4dn`, `sleeptrain-1uz6mna`, `sleeptrain-1uzbi5g`, `sleeptrain-1uzbuw1`, `sleeptrain-1uzfser`, `sleeptrain-1uzkh5h`, `sleeptrain-1uzkizs`, `sleeptrain-1uzlbr3`, `toddlers-1ux8nig`, `toddlers-1uxdvsb`, `toddlers-1uxll6k`, `toddlers-1uydb0k`, `toddlers-1uyz2qy`.

**Other skipped/partly quoted ledger references (1):** `sleeptrain-1uxmwvm`.

**Additional reader-note review candidates (5):** `daddit-1uxp58i`, `sleeptrain-1uxmey4`, `sleeptrain-1uy0l5k`, `toddlers-1uy3ybc`, `toddlers-1uzm2ww`.

### R31 — `sources/reddit-reading-r31.md`

**Subject-based whole-unit ledger references (4):** `AttachmentParenting-1v0rtes`, `AttachmentParenting-1v2jni1`, `FirstTimeMom-1v06glv`, `Mommit-1v2goih`.

**Subject-based passage ledger references (14):** `NewParents-1v0ujy8`, `NewParents-1v1sftp`, `NewParents-1v2ctx1`, `NewParents-1v2siry`, `Parenting-1v1uofa`, `beyondthebump-1v2lbhm`, `beyondthebumpUK-1v2iod0`, `sahm-1v1eect`, `sleeptrain-1v0k3rd`, `sleeptrain-1v17qal`, `sleeptrain-1v1kjee`, `sleeptrain-1v24vwe`, `toddlers-1v1igxt`, `toddlers-1v1ulph`.

**Other skipped/partly quoted ledger references (5):** `AttachmentParenting-1v1gsoh`, `NewParents-1v1863l`, `daddit-1v0g1v5`, `sleeptrain-1v2d9n6`, `toddlers-1v2rwcq`.

**Additional working-log review candidates (26):** `AttachmentParenting-1v2ai9k`, `Mommit-1v29ukp`, `NewParents-1v0sjyy`, `NewParents-1v1jrt1`, `NewParents-1v29gtj`, `NewParents-1v2nkus`, `ScienceBasedParenting-1v17za1`, `beyondthebump-1v2pack`, `beyondthebump-1v2pkcf`, `beyondthebump-1v2taar`, `sleeptrain-1v0rknq`, `sleeptrain-1v0th2s`, `sleeptrain-1v1j9za`, `sleeptrain-1v1m9di`, `sleeptrain-1v1xl17`, `sleeptrain-1v2c97t`, `sleeptrain-1v2itmw`, `sleeptrain-1v2mmat`, `sleeptrain-1v2qkbe`, `sleeptrain-1v2stmu`, `toddlers-1v0dy8i`, `toddlers-1v1vaxo`, `toddlers-1v1wwqg`, `toddlers-1v23n17`, `toddlers-1v2qd2c`, `workingmoms-1v1oh9o`.

**Additional reader-note review candidates (14):** `NewParents-1v0ombu`, `NewParents-1v1jvm9`, `beyondthebumpUK-1v0k0b9`, `sleeptrain-1uzuppj`, `sleeptrain-1uzxla3`, `sleeptrain-1v0e19x`, `sleeptrain-1v0n4w4`, `sleeptrain-1v0ninl`, `sleeptrain-1v0qpck`, `sleeptrain-1v1ilvg`, `sleeptrain-1v1n0s5`, `sleeptrain-1v1rncv`, `sleeptrain-1v25hgl`, `toddlers-1v0cofp`.

### R32 — `sources/reddit-reading-r32.md`

**Subject-based whole-unit ledger references (7):** `Mommit-1v2xkjp`, `NewParents-1v4isa5`, `Parenting-1v4yaeq`, `Parenting-1v5snzg`, `beyondthebump-1v3sjt1`, `sleeptrain-1v4fg7e`, `toddlers-1v4ul0e`.

**Other skipped/partly quoted ledger references (14):** `AttachmentParenting-1v5mmyr`, `Mommit-1v4qbhv`, `Mommit-1v4uwvr`, `NewParents-1v596rk`, `Parenting-1v4woz9`, `sleeptrain-1v48y1z`, `sleeptrain-1v4fq6u`, `toddlers-1v32rpy`, `toddlers-1v3dz43`, `toddlers-1v4lf83`, `toddlers-1v4wtm1`, `toddlers-1v5my9p`, `toddlers-1v5t7ur`, `toddlers-1v5tljt`.

### R33 — `sources/reddit-reading-r33.md`

**Subject-based whole-unit ledger references (6):** `NewParents-1v65eb5`, `NewParents-1v7ef16`, `beyondthebump-1v85f1r`, `beyondthebump-1v8xkht`, `sleeptrain-1v9h8y0`, `toddlers-1v8jf0c`.

**Subject-based passage ledger references (3):** `AttachmentParenting-1v72pie`, `sleeptrain-1v75p6z`, `sleeptrain-1v9fv5a`.

**Other skipped/partly quoted ledger references (3):** `NewParents-1v6i0iy`, `sleeptrain-1v8y5b9`, `toddlers-1v7fmyj`.

### R34 — `sources/reddit-reading-r34.md`

**Subject-based whole-unit ledger references (7):** `NewParents-1vcgrrg`, `Parenting-1v9pl9f`, `Parenting-1v9ybhc`, `Parenting-1vbyq38`, `beyondthebump-1va545w`, `beyondthebump-1vaf5uo`, `sleeptrain-1vaei8j`.

**Subject-based passage ledger references (30):** `AttachmentParenting-1v9vpqo`, `AttachmentParenting-1va2asm`, `AttachmentParenting-1vaokvt`, `AttachmentParenting-1vbm6dd`, `FirstTimeMom-1vb95lm`, `Mommit-1va3bug`, `Mommit-1vausfc`, `NewParents-1vaosks`, `NewParents-1vasgqg`, `NewParents-1vbo9sl`, `beyondthebump-1vaa6gb`, `beyondthebump-1vbx981`, `beyondthebump-1vcomoc`, `beyondthebumpUK-1vb5j10`, `beyondthebumpUK-1vcgvmq`, `sahm-1v9y5d3`, `sleeptrain-1va4to5`, `sleeptrain-1va85pe`, `sleeptrain-1va9fge`, `sleeptrain-1vaofr9`, `sleeptrain-1vaxrvz`, `sleeptrain-1vbebfj`, `sleeptrain-1vbvtjc`, `sleeptrain-1vbwxof`, `sleeptrain-1vc98vn`, `sleeptrain-1vcc52q`, `sleeptrain-1vcncfa`, `toddlers-1vaiomt`, `toddlers-1vb5c2g`, `toddlers-1vc68ji`.

**Other skipped/partly quoted ledger references (1):** `ScienceBasedParenting-1vaubpg`.

**Additional reader-note review candidates (18):** `Mommit-1vaoyjf`, `Mommit-1vbnvvb`, `Mommit-1vckqqf`, `NewParents-1v9r8ix`, `NewParents-1vb3xgt`, `NewParents-1vbmsfq`, `beyondthebumpUK-1vbkflc`, `daddit-1v9olj8`, `sleeptrain-1va43ge`, `sleeptrain-1vaj3og`, `sleeptrain-1vaudpx`, `sleeptrain-1vavv9x`, `sleeptrain-1vayxuf`, `sleeptrain-1vbr4bp`, `sleeptrain-1vbrnpe`, `sleeptrain-1vbtxzp`, `sleeptrain-1vc3479`, `sleeptrain-1vcbcca`.

### R35 — `sources/reddit-reading-r35.md`

**Subject-based whole-unit ledger references (8):** `AttachmentParenting-1vdi0cm`, `NewParents-1vdieiu`, `Parenting-1ve7oxl`, `beyondthebump-1vdr6sb`, `beyondthebumpUK-1vg4doy`, `daddit-1vcy6g3`, `sleeptrain-1vfvc7l`, `toddlers-1vd1t7t`.

**Other skipped/partly quoted ledger references (7):** `AttachmentParenting-1vdah4i`, `AttachmentParenting-1ve9jek`, `AttachmentParenting-1vfetfq`, `ScienceBasedParenting-1vcrdxm`, `beyondthebump-1ve1sb4`, `sleeptrain-1vfjox5`, `sleeptrain-1vfsv41`.

**Additional reader-note review candidates (21):** `Mommit-1venv0f`, `Mommit-1vfe2d4`, `NewParents-1vd2ima`, `NewParents-1vee587`, `NewParents-1vehx5k`, `Parenting-1vffdoa`, `sleeptrain-1vcpmnn`, `sleeptrain-1vcse04`, `sleeptrain-1vd90ak`, `sleeptrain-1vdp4v5`, `sleeptrain-1vdqx90`, `sleeptrain-1ve00e6`, `sleeptrain-1ve0i2p`, `sleeptrain-1vedlql`, `sleeptrain-1velm4y`, `sleeptrain-1vfj050`, `sleeptrain-1vfjs0x`, `sleeptrain-1vfsmxv`, `sleeptrain-1vfszqm`, `toddlers-1vdpnnu`, `toddlers-1veoqti`.

**Unmapped category review candidates (99):** `AttachmentParenting-1vdhgsz`, `AttachmentParenting-1vdy0h4`, `AttachmentParenting-1ve2xqp`, `AttachmentParenting-1vemcsr`, `Mommit-1vcwriw`, `Mommit-1vdiupe`, `Mommit-1vel9gi`, `Mommit-1velehr`, `NewParents-1vcrd0o`, `NewParents-1vcvjc9`, `NewParents-1vcy916`, `NewParents-1vd3cfz`, `NewParents-1vdgw0g`, `NewParents-1ve7rse`, `NewParents-1vee16n`, `NewParents-1vf9ht1`, `NewParents-1vfbte1`, `NewParents-1vfgxra`, `NewParents-1vfh386`, `NewParents-1vfsun7`, `NewParents-1vg4i58`, `Parenting-1vdqw8n`, `Parenting-1vds6ka`, `Parenting-1ve1gvt`, `Parenting-1vejb37`, `Parenting-1vezk59`, `Parenting-1vfgv2y`, `ScienceBasedParenting-1ve5j1y`, `ScienceBasedParenting-1vf7zkw`, `beyondthebump-1vcvlay`, `beyondthebumpUK-1veclm9`, `beyondthebumpUK-1vejkpz`, `daddit-1vdmp2h`, `daddit-1vdok7c`, `sahm-1ve1k0v`, `sleeptrain-1vcse9y`, `sleeptrain-1vd03ur`, `sleeptrain-1vd1w12`, `sleeptrain-1vd73us`, `sleeptrain-1vd7sz0`, `sleeptrain-1vd84eq`, `sleeptrain-1vd9zid`, `sleeptrain-1vde0g0`, `sleeptrain-1vdeqzx`, `sleeptrain-1vdfbju`, `sleeptrain-1vdtx1f`, `sleeptrain-1vdu680`, `sleeptrain-1vdvxug`, `sleeptrain-1vdyr10`, `sleeptrain-1vdytms`, `sleeptrain-1vdz4n2`, `sleeptrain-1ve21ae`, `sleeptrain-1ve3d1n`, `sleeptrain-1ve4cth`, `sleeptrain-1ve9bbg`, `sleeptrain-1ve9ixw`, `sleeptrain-1ve9j8r`, `sleeptrain-1veagk1`, `sleeptrain-1vebksh`, `sleeptrain-1vedtn5`, `sleeptrain-1vefe4u`, `sleeptrain-1veit7o`, `sleeptrain-1vemjk7`, `sleeptrain-1venhx2`, `sleeptrain-1vepls7`, `sleeptrain-1vev09e`, `sleeptrain-1vewstx`, `sleeptrain-1vexn0a`, `sleeptrain-1vf3rh8`, `sleeptrain-1vf4owr`, `sleeptrain-1vf5cd8`, `sleeptrain-1vf6lp0`, `sleeptrain-1vf7jhj`, `sleeptrain-1vfabgv`, `sleeptrain-1vfbmf9`, `sleeptrain-1vfcyar`, `sleeptrain-1vfepdj`, `sleeptrain-1vff2rl`, `sleeptrain-1vfhcft`, `sleeptrain-1vfhmfn`, `sleeptrain-1vfo58u`, `sleeptrain-1vforgb`, `sleeptrain-1vftdp1`, `sleeptrain-1vfu2sd`, `sleeptrain-1vfwt7v`, `sleeptrain-1vfxpyj`, `sleeptrain-1vfzdf8`, `sleeptrain-1vg4ua0`, `sleeptrain-1vg5hq9`, `sleeptrain-1vg5ses`, `toddlers-1vcruxm`, `toddlers-1vdht15`, `toddlers-1vdixbh`, `toddlers-1vdx1df`, `toddlers-1vf6lmg`, `toddlers-1vffl37`, `toddlers-1vfmaaa`, `toddlers-1vfrrux`, `toddlers-1vfvuky`.

### R36 — `sources/reddit-reading-r36.md`

**Subject-based whole-unit ledger references (5):** `NewParents-1vgs902`, `NewParents-1vh829r`, `NewParents-1vhkn8k`, `NewParents-1vhpanh`, `Parenting-1vi7jvt`.

**Subject-based passage ledger references (15):** `AttachmentParenting-1vgzduc`, `AttachmentParenting-1vj9du9`, `Mommit-1vg79cg`, `Mommit-1vipo3y`, `Mommit-1vj0j7c`, `NewParents-1vif7tm`, `NewParents-1vj9szk`, `NewParents-1vjhlmj`, `beyondthebumpUK-1vjka34`, `daddit-1vh3sxr`, `daddit-1vir8qf`, `sleeptrain-1vhk8hu`, `sleeptrain-1vi1q1s`, `sleeptrain-1vith0z`, `sleeptrain-1viygde`.

**Additional working-log review candidates (32):** `AttachmentParenting-1vgvd7u`, `AttachmentParenting-1vh11q5`, `NewParents-1vglsfy`, `NewParents-1vh33ir`, `NewParents-1vjaby8`, `NewParents-1vjljgl`, `NewParents-1vjlvqq`, `Parenting-1vhphhy`, `beyondthebump-1vhy2jy`, `beyondthebump-1vimkvk`, `beyondthebumpUK-1vhfmj2`, `beyondthebumpUK-1vjc22s`, `daddit-1vjgb4n`, `sahm-1vi46p1`, `sleeptrain-1vhflog`, `sleeptrain-1vhn26b`, `sleeptrain-1vhxzbw`, `sleeptrain-1vi0lhp`, `sleeptrain-1vi0m3i`, `sleeptrain-1via82x`, `sleeptrain-1vilr7t`, `sleeptrain-1vj6kzi`, `sleeptrain-1vjbin1`, `sleeptrain-1vjh7sp`, `sleeptrain-1vjj8bc`, `sleeptrain-1vjkku3`, `toddlers-1vgg1u9`, `toddlers-1vgv3ir`, `toddlers-1vhmyju`, `toddlers-1vi00yz`, `toddlers-1vijk7a`, `toddlers-1vjcg3i`.

### R37 — `sources/reddit-reading-r37.md`

**Subject-based whole-unit ledger references (4):** `NewParents-1vmaxvw`, `Parenting-1vm2dla`, `ScienceBasedParenting-1vmudlm`, `toddlers-1vmneck`.

**Subject-based passage ledger references (29):** `AttachmentParenting-1vkhl4k`, `AttachmentParenting-1vl1bec`, `AttachmentParenting-1vlvmv2`, `AttachmentParenting-1vmh7ho`, `AttachmentParenting-1vmmh1z`, `FirstTimeMom-1vm61su`, `NewParents-1vjubgz`, `NewParents-1vkphju`, `NewParents-1vl0y31`, `NewParents-1vmv7ta`, `beyondthebump-1vkntnp`, `beyondthebump-1vkqg81`, `beyondthebumpUK-1vjuar1`, `beyondthebumpUK-1vki7e9`, `sleeptrain-1vjp7g9`, `sleeptrain-1vkc4kr`, `sleeptrain-1vkh07t`, `sleeptrain-1vkiz79`, `sleeptrain-1vkudwv`, `sleeptrain-1vl88qo`, `sleeptrain-1vlgk2k`, `sleeptrain-1vlpas4`, `sleeptrain-1vlsv3h`, `sleeptrain-1vm1l8f`, `sleeptrain-1vmh30e`, `sleeptrain-1vmniy5`, `sleeptrain-1vmpxwh`, `sleeptrain-1vms2we`, `toddlers-1vmlk6l`.

**Other skipped/partly quoted ledger references (3):** `NewParents-1vl3cic`, `beyondthebump-1vl0zhu`, `daddit-1vlmo0f`.

**Additional reader-note review candidates (16):** `Parenting-1vmfjqh`, `beyondthebumpUK-1vmo81f`, `daddit-1vke0mr`, `sleeptrain-1vjtoih`, `sleeptrain-1vk77ta`, `sleeptrain-1vkpmel`, `sleeptrain-1vl2xpc`, `sleeptrain-1vl5y4e`, `sleeptrain-1vl6rkg`, `sleeptrain-1vlb1h0`, `sleeptrain-1vlsjem`, `sleeptrain-1vlsq9t`, `sleeptrain-1vmpase`, `toddlers-1vkekcu`, `toddlers-1vmb07a`, `toddlers-1vmlcs8`.

**Unmapped category review candidates (76):** `AttachmentParenting-1vkuts4`, `AttachmentParenting-1vli6r1`, `AttachmentParenting-1vm40u5`, `Mommit-1vjo1ta`, `Mommit-1vlacoo`, `NewParents-1vjs6ft`, `NewParents-1vko24m`, `NewParents-1vkvgmc`, `NewParents-1vlcyux`, `NewParents-1vljbxe`, `NewParents-1vlt07l`, `NewParents-1vlyv2q`, `NewParents-1vm23og`, `NewParents-1vmnudk`, `NewParents-1vmpdkh`, `NewParents-1vmqjjw`, `NewParents-1vmu3ml`, `Parenting-1vm76yn`, `beyondthebump-1vkv7g8`, `beyondthebump-1vlv1j1`, `beyondthebump-1vm2uxm`, `daddit-1vjxfer`, `sleeptrain-1vjoj7a`, `sleeptrain-1vjpo3f`, `sleeptrain-1vjqbzg`, `sleeptrain-1vjrkwz`, `sleeptrain-1vjvup6`, `sleeptrain-1vjy34v`, `sleeptrain-1vjyhej`, `sleeptrain-1vjzl7b`, `sleeptrain-1vk2hhm`, `sleeptrain-1vk2zve`, `sleeptrain-1vk8mme`, `sleeptrain-1vkfp38`, `sleeptrain-1vkhtno`, `sleeptrain-1vkopx3`, `sleeptrain-1vkpcum`, `sleeptrain-1vkpmpt`, `sleeptrain-1vkrk6l`, `sleeptrain-1vksbg5`, `sleeptrain-1vkugjx`, `sleeptrain-1vkwqx7`, `sleeptrain-1vkxd4d`, `sleeptrain-1vkyzz7`, `sleeptrain-1vl0j6a`, `sleeptrain-1vlbhge`, `sleeptrain-1vlbye4`, `sleeptrain-1vldqk4`, `sleeptrain-1vlh3gf`, `sleeptrain-1vlii8h`, `sleeptrain-1vlippi`, `sleeptrain-1vlk1lr`, `sleeptrain-1vlkoxr`, `sleeptrain-1vllf5g`, `sleeptrain-1vllrkw`, `sleeptrain-1vlsb92`, `sleeptrain-1vltvxb`, `sleeptrain-1vlu34l`, `sleeptrain-1vm0ny9`, `sleeptrain-1vm409y`, `sleeptrain-1vm7htn`, `sleeptrain-1vmad4a`, `sleeptrain-1vmd5rs`, `sleeptrain-1vmgj2v`, `sleeptrain-1vmk056`, `sleeptrain-1vmrakm`, `sleeptrain-1vmvhum`, `sleeptrain-1vmwkvi`, `toddlers-1vjrf4i`, `toddlers-1vjzvel`, `toddlers-1vkld3d`, `toddlers-1vkp61v`, `toddlers-1vldn9i`, `toddlers-1vlxr47`, `toddlers-1vmorlt`, `toddlers-1vmprca`.

### R38 — `sources/reddit-reading-r38.md`

**Subject-based whole-unit ledger references (8):** `Mommit-1vn4eq7`, `NewParents-1vnhzzg`, `NewParents-1vo6kcz`, `NewParents-1voxuja`, `NewParents-1vp04qs`, `ScienceBasedParenting-1vngt2w`, `beyondthebumpUK-1vokmpd`, `daddit-1vpe7fx`.

**Subject-based passage ledger references (14):** `Mommit-1vmwu6g`, `Mommit-1voj6ng`, `NewParents-1vn7kat`, `NewParents-1vnf5co`, `NewParents-1vpjgla`, `NewParents-1vpngmc`, `NewParents-1vpughs`, `beyondthebumpUK-1vp03w4`, `sahm-1vnhvfd`, `sleeptrain-1vn41d4`, `sleeptrain-1vnzoq6`, `toddlers-1vnnl41`, `toddlers-1vnvy57`, `toddlers-1vpuypk`.

**Other skipped/partly quoted ledger references (5):** `AttachmentParenting-1vnw6o0`, `Parenting-1vonei4`, `daddit-1vmy4no`, `toddlers-1vn7x9w`, `toddlers-1vpidkr`.

**Unmapped category review candidates (107):** `AttachmentParenting-1vnn6r9`, `Mommit-1vn7jtl`, `Mommit-1vn9y5y`, `Mommit-1vomprt`, `Mommit-1votu9b`, `Mommit-1vpbuzd`, `Mommit-1vps1zh`, `NewParents-1vn3jfe`, `NewParents-1vnonka`, `NewParents-1vntaqm`, `NewParents-1vnv4c8`, `NewParents-1vnvomg`, `NewParents-1vo1vcg`, `NewParents-1vofqyl`, `NewParents-1vol694`, `NewParents-1vp75af`, `NewParents-1vp9rw9`, `NewParents-1vpbz0m`, `Parenting-1vnuuy2`, `Parenting-1vnvo6c`, `Parenting-1vohqph`, `ScienceBasedParenting-1vn9yrr`, `beyondthebump-1vn0q0m`, `beyondthebump-1vnab4q`, `beyondthebump-1vnam1k`, `beyondthebump-1vnboos`, `beyondthebump-1vno4bo`, `beyondthebump-1vosr3z`, `beyondthebump-1vp93py`, `beyondthebump-1vpbf65`, `beyondthebumpUK-1vnbbh3`, `beyondthebumpUK-1vnmg6q`, `beyondthebumpUK-1vo25cu`, `beyondthebumpUK-1vo7e4z`, `beyondthebumpUK-1voj0uo`, `beyondthebumpUK-1vpdpqt`, `beyondthebumpUK-1vplp1c`, `daddit-1vpbp3h`, `sleeptrain-1vmwrpe`, `sleeptrain-1vmwwrw`, `sleeptrain-1vmyv2u`, `sleeptrain-1vn11ev`, `sleeptrain-1vn49al`, `sleeptrain-1vn71t3`, `sleeptrain-1vn8g5z`, `sleeptrain-1vnbitm`, `sleeptrain-1vnbqw0`, `sleeptrain-1vnf38i`, `sleeptrain-1vnggo9`, `sleeptrain-1vngpzm`, `sleeptrain-1vnj8lg`, `sleeptrain-1vnm4fe`, `sleeptrain-1vnmrql`, `sleeptrain-1vnov5m`, `sleeptrain-1vnr2qv`, `sleeptrain-1vntsme`, `sleeptrain-1vnvjgx`, `sleeptrain-1vnx06z`, `sleeptrain-1vnx75j`, `sleeptrain-1vnxlbx`, `sleeptrain-1vnylcg`, `sleeptrain-1vo296n`, `sleeptrain-1vo4lp7`, `sleeptrain-1vo726n`, `sleeptrain-1vo77u5`, `sleeptrain-1vo7d59`, `sleeptrain-1vo8dqz`, `sleeptrain-1vo8heg`, `sleeptrain-1vo934k`, `sleeptrain-1vo93ju`, `sleeptrain-1vo9abm`, `sleeptrain-1vob1sa`, `sleeptrain-1vob60d`, `sleeptrain-1vocnak`, `sleeptrain-1voj4ye`, `sleeptrain-1vok9cj`, `sleeptrain-1vond7e`, `sleeptrain-1voo6al`, `sleeptrain-1vooncf`, `sleeptrain-1voout8`, `sleeptrain-1vopu01`, `sleeptrain-1vor5en`, `sleeptrain-1vosuvs`, `sleeptrain-1vou2go`, `sleeptrain-1vox9ar`, `sleeptrain-1voymbf`, `sleeptrain-1vozby5`, `sleeptrain-1vp0vtt`, `sleeptrain-1vp3vvj`, `sleeptrain-1vp497g`, `sleeptrain-1vp5hwf`, `sleeptrain-1vp76fz`, `sleeptrain-1vp94wl`, `sleeptrain-1vpb8md`, `sleeptrain-1vpihqd`, `sleeptrain-1vpy751`, `toddlers-1vmwoh3`, `toddlers-1vmy4oy`, `toddlers-1vnrxtz`, `toddlers-1vo4ik4`, `toddlers-1vob7rc`, `toddlers-1voo6gk`, `toddlers-1vozabs`, `toddlers-1vp52lk`, `toddlers-1vpothb`, `toddlers-1vppxg3`, `toddlers-1vptbuq`.

### R39 — `sources/reddit-reading-r39.md`

**Subject-based whole-unit ledger references (3):** `NewParents-1vstz9l`, `beyondthebump-1vqcn5c`, `beyondthebump-1vsapmg`.

**Subject-based passage ledger references (23):** `FirstTimeMom-1vsmwyt`, `FirstTimeMom-1vsqnlu`, `Mommit-1vtaz9y`, `NewParents-1vq7d2d`, `NewParents-1vqy1mb`, `beyondthebump-1vsalmg`, `beyondthebumpUK-1vrq3jh`, `beyondthebumpUK-1vsarwb`, `beyondthebumpUK-1vszndz`, `sleeptrain-1vqpach`, `sleeptrain-1vqz7zr`, `sleeptrain-1vrg71p`, `sleeptrain-1vrlch4`, `sleeptrain-1vrq8uk`, `sleeptrain-1vrtbgj`, `sleeptrain-1vrw7sw`, `sleeptrain-1vs0ew7`, `sleeptrain-1vsk20g`, `sleeptrain-1vsnihj`, `sleeptrain-1vsu74z`, `sleeptrain-1vsvdia`, `toddlers-1vsgr3t`, `toddlers-1vstm85`.

**Other skipped/partly quoted ledger references (6):** `AttachmentParenting-1vpzq2b`, `AttachmentParenting-1vs5x5b`, `Mommit-1vrq7a3`, `sleeptrain-1vq6u6z`, `sleeptrain-1vrmj8w`, `toddlers-1vr0tb6`.

### R40 — `sources/reddit-reading-r40.md`

**Subject-based whole-unit ledger references (10):** `NewParents-1vujwpy`, `NewParents-1vvjhvn`, `NewParents-1vwp85d`, `NewParents-1vxf6dr`, `NewParents-1vxg58y`, `Parenting-1vtl8a1`, `beyondthebump-1vu3hvg`, `sleeptrain-1vue535`, `sleeptrain-1vufbue`, `sleeptrain-1vv89bg`.

**Subject-based passage ledger references (46):** `AttachmentParenting-1vtgoff`, `AttachmentParenting-1vtj1g0`, `AttachmentParenting-1vvlcub`, `FirstTimeMom-1vtucqn`, `Mommit-1vx9wz6`, `Mommit-1vx9xaq`, `NewParents-1vtfw3m`, `NewParents-1vtkgqq`, `NewParents-1vuxzk0`, `NewParents-1vv9n1o`, `NewParents-1vwvqkm`, `Parenting-1vvlw15`, `Parenting-1vwyqyu`, `Parenting-1vx7xwl`, `beyondthebump-1vtht1m`, `beyondthebump-1vtsrtl`, `beyondthebump-1vw8gyg`, `beyondthebumpUK-1vu81p6`, `beyondthebumpUK-1vwyyhg`, `beyondthebumpUK-1vxesuq`, `daddit-1vtfcx3`, `daddit-1vum3r4`, `sleeptrain-1vu4c6n`, `sleeptrain-1vus2xh`, `sleeptrain-1vuyyqc`, `sleeptrain-1vvj8vd`, `sleeptrain-1vvmwem`, `sleeptrain-1vvrakc`, `sleeptrain-1vvyx3n`, `sleeptrain-1vw1guq`, `sleeptrain-1vw4j9j`, `sleeptrain-1vwh1xu`, `sleeptrain-1vwm9tg`, `sleeptrain-1vwotjj`, `sleeptrain-1vx0bld`, `sleeptrain-1vx0lyf`, `sleeptrain-1vx233o`, `sleeptrain-1vx4eyc`, `sleeptrain-1vx5art`, `sleeptrain-1vxajul`, `sleeptrain-1vxd6jr`, `sleeptrain-1vxdzp1`, `toddlers-1vu1ppo`, `toddlers-1vvbgai`, `toddlers-1vvf9wu`, `toddlers-1vvq22b`.

**Other skipped/partly quoted ledger references (4):** `Mommit-1vvycxh`, `beyondthebump-1vvgoon`, `beyondthebump-1vvyfb6`, `sleeptrain-1vvfm7s`.

### R41 — `sources/reddit-reading-r41.md`

**Subject-based whole-unit ledger references (6):** `NewParents-1sdlayz`, `NewParents-1szpvsc`, `NewParents-1t2unm5`, `beyondthebump-1su4g0o`, `sleeptrain-1t53rxk`, `sleeptrain-1tbi8qn`.

**Subject-based passage ledger references (60):** `Mommit-1sbmjla`, `Mommit-1t02fm3`, `Mommit-1tbk9c0`, `Mommit-1tbo5g1`, `NewParents-1sl2ysk`, `NewParents-1sr7riy`, `NewParents-1ss1eli`, `NewParents-1ssiva7`, `NewParents-1swmxvc`, `NewParents-1syncqa`, `NewParents-1sz7ssw`, `NewParents-1szaut5`, `NewParents-1t0chhe`, `NewParents-1t1pcx3`, `NewParents-1t1r7np`, `NewParents-1t3jlwh`, `NewParents-1t84ulr`, `NewParents-1tbhpy6`, `beyondthebump-1skj0qb`, `beyondthebump-1sve9jt`, `beyondthebumpUK-1stgjc6`, `beyondthebumpUK-1sy0ujs`, `sleeptrain-1saguit`, `sleeptrain-1sar6er`, `sleeptrain-1sbxvt3`, `sleeptrain-1sdjjdc`, `sleeptrain-1sdmz51`, `sleeptrain-1sfh14g`, `sleeptrain-1sgh9y4`, `sleeptrain-1sgy911`, `sleeptrain-1sibvdu`, `sleeptrain-1sjkeq6`, `sleeptrain-1sl7hpd`, `sleeptrain-1sldo35`, `sleeptrain-1smfuzj`, `sleeptrain-1smiwhl`, `sleeptrain-1sn7gb5`, `sleeptrain-1sn7svy`, `sleeptrain-1sq42oo`, `sleeptrain-1sq5wde`, `sleeptrain-1sqvddg`, `sleeptrain-1sr8lp1`, `sleeptrain-1srdogs`, `sleeptrain-1ssj64r`, `sleeptrain-1staq91`, `sleeptrain-1sw5g9a`, `sleeptrain-1swrb4c`, `sleeptrain-1t1yth3`, `sleeptrain-1t2ak4d`, `sleeptrain-1t4ddea`, `sleeptrain-1t4ycba`, `sleeptrain-1t6fzzj`, `sleeptrain-1ta6tfk`, `sleeptrain-1tb8mn8`, `sleeptrain-1tb8wcb`, `sleeptrain-1tc5fc7`, `sleeptrain-1tc6z12`, `toddlers-1sm9xtw`, `toddlers-1sym6hv`, `toddlers-1tb0rhr`.

**Other skipped/partly quoted ledger references (5):** `NewParents-1sdifjn`, `NewParents-1t31ciw`, `NewParents-1t53sxz`, `beyondthebump-1t53sji`, `beyondthebump-1tc6emd`.

**Additional working-log review candidates (4):** `sleeptrain-1sdi7lx`, `sleeptrain-1tc6dpp`, `toddlers-1sevck9`, `toddlers-1shyehf`.

### R42 — `sources/reddit-reading-r42.md`

**Subject-based whole-unit ledger references (6):** `beyondthebump-1thpk62`, `beyondthebump-1tzrur5`, `beyondthebump-1uerzg8`, `beyondthebumpUK-1tutp5p`, `beyondthebumpUK-1u3anhl`, `beyondthebumpUK-1u9l5tm`.

**Subject-based passage ledger references (32):** `NewParents-1tdh0m3`, `NewParents-1th8pqt`, `NewParents-1toncwd`, `NewParents-1u9yjdg`, `Parenting-1thabhn`, `Parenting-1tmew7k`, `Parenting-1u8w22y`, `Parenting-1u95wax`, `beyondthebump-1tr7d0i`, `beyondthebump-1u9og1z`, `daddit-1tx1jrr`, `sleeptrain-1tfui05`, `sleeptrain-1tja2ix`, `sleeptrain-1tjy589`, `sleeptrain-1tksulc`, `sleeptrain-1tluwbf`, `sleeptrain-1tm3ylc`, `sleeptrain-1tnxwll`, `sleeptrain-1to4yno`, `sleeptrain-1triirr`, `sleeptrain-1trmx6u`, `sleeptrain-1trwwcr`, `sleeptrain-1tstlun`, `sleeptrain-1ttmn6m`, `sleeptrain-1tynkng`, `sleeptrain-1tzkxyw`, `sleeptrain-1u09dda`, `sleeptrain-1u6k3hg`, `sleeptrain-1u715v7`, `sleeptrain-1ub1ho2`, `sleeptrain-1uc9mkq`, `sleeptrain-1uec61v`.

**Other skipped/partly quoted ledger references (3):** `beyondthebump-1te175e`, `toddlers-1tk5a9n`, `toddlers-1uegyxd`.

**Additional working-log review candidates (45):** `AttachmentParenting-1tshrtv`, `NewParents-1tuo2gl`, `NewParents-1tzm2mn`, `Parenting-1tu6tx7`, `sleeptrain-1tcnqtp`, `sleeptrain-1tdhzl1`, `sleeptrain-1teop1x`, `sleeptrain-1tg8z9v`, `sleeptrain-1tggtla`, `sleeptrain-1tgqu2z`, `sleeptrain-1tgqz6o`, `sleeptrain-1tiu5to`, `sleeptrain-1tjaqjo`, `sleeptrain-1tjx152`, `sleeptrain-1tk30cs`, `sleeptrain-1tk48y3`, `sleeptrain-1tkzke8`, `sleeptrain-1tnai5f`, `sleeptrain-1to5mh0`, `sleeptrain-1tpock9`, `sleeptrain-1tqmqom`, `sleeptrain-1tr96pw`, `sleeptrain-1tr983n`, `sleeptrain-1tryqed`, `sleeptrain-1tsz0zd`, `sleeptrain-1turq7l`, `sleeptrain-1tv00pf`, `sleeptrain-1tyfpkb`, `sleeptrain-1tyl4d4`, `sleeptrain-1u1csks`, `sleeptrain-1u2btnt`, `sleeptrain-1u3nlpn`, `sleeptrain-1u5gx65`, `sleeptrain-1u67xme`, `sleeptrain-1u6xi8j`, `sleeptrain-1u79bi1`, `sleeptrain-1u8v917`, `sleeptrain-1u8z8ja`, `sleeptrain-1ua2wo5`, `sleeptrain-1ua66lx`, `sleeptrain-1uay82w`, `sleeptrain-1ubywv4`, `sleeptrain-1ucuxu9`, `sleeptrain-1ud03ym`, `toddlers-1u6qwru`.

### R43 — `sources/reddit-reading-r43.md`

**Subject-based whole-unit ledger references (2):** `Mommit-1sm0fdy`, `NewParents-1t6rvss`.

**Subject-based passage ledger references (38):** `AttachmentParenting-1skb4zd`, `Mommit-1uaxyam`, `NewParents-1sck46o`, `NewParents-1sczq7s`, `NewParents-1st7a4w`, `NewParents-1swauh1`, `NewParents-1tkf7ay`, `NewParents-1tv25sx`, `NewParents-1u7nazo`, `Parenting-1sdlg73`, `Parenting-1si3qrh`, `Parenting-1sz4qz0`, `ScienceBasedParenting-1sjufmg`, `beyondthebump-1san0bg`, `beyondthebump-1so1tbv`, `beyondthebump-1t0zt63`, `beyondthebump-1u0wkw2`, `beyondthebump-1ueh4pk`, `sleeptrain-1sfnsht`, `sleeptrain-1sfx554`, `sleeptrain-1sgptiu`, `sleeptrain-1si77xa`, `sleeptrain-1sj6e2l`, `sleeptrain-1spgh82`, `sleeptrain-1sq3z2a`, `sleeptrain-1srbxf1`, `sleeptrain-1sz9qk0`, `sleeptrain-1t81zhv`, `sleeptrain-1taa41t`, `sleeptrain-1te5ljk`, `sleeptrain-1tfqikg`, `sleeptrain-1tg4w4q`, `sleeptrain-1thzyf6`, `sleeptrain-1tqs5rd`, `sleeptrain-1u28yb8`, `sleeptrain-1u2acev`, `sleeptrain-1udz93p`, `toddlers-1sylj38`.

**Other skipped/partly quoted ledger references (4):** `AttachmentParenting-1tpjiez`, `Parenting-1semhaj`, `Parenting-1smqzo3`, `workingmoms-1stp3ni`.

**Additional reader-note review candidates (5):** `daddit-1swrmyo`, `sleeptrain-1si3iuo`, `sleeptrain-1tjw7iw`, `sleeptrain-1tukij9`, `toddlers-1see9qc`.

### R44 — `sources/reddit-reading-r44.md`

**Subject-based whole-unit ledger references (10):** `AttachmentParenting-1tu5b15`, `NewParents-1sa46f1`, `NewParents-1u13707`, `Parenting-1taptjw`, `beyondthebump-1s97vni`, `beyondthebump-1s98con`, `beyondthebump-1s99q1h`, `beyondthebump-1tl1tg2`, `sleeptrain-1s9ripu`, `toddlers-1s9ilpm`.

**Subject-based passage ledger references (38):** `AttachmentParenting-1t4atni`, `AttachmentParenting-1tmnw9s`, `AttachmentParenting-1u1l8ys`, `NewParents-1s957ez`, `NewParents-1s9aev1`, `NewParents-1s9hbzp`, `NewParents-1s9vznv`, `NewParents-1s9wuej`, `NewParents-1sa4xdq`, `NewParents-1t76sip`, `NewParents-1tfkbq5`, `NewParents-1tp92hv`, `NewParents-1tqrzh3`, `NewParents-1twpo2d`, `NewParents-1txfpn7`, `NewParents-1u2g6o6`, `NewParents-1ud3mla`, `beyondthebump-1s9klf4`, `beyondthebump-1sa80k5`, `beyondthebump-1tady5m`, `beyondthebump-1tep0ja`, `beyondthebump-1teqkwl`, `beyondthebump-1tkocih`, `beyondthebump-1tr5pcj`, `beyondthebump-1tsmz4e`, `beyondthebump-1tywe5c`, `sleeptrain-1s9ax2g`, `sleeptrain-1s9n1be`, `sleeptrain-1s9ymx3`, `sleeptrain-1sa4jsi`, `sleeptrain-1t0w40b`, `sleeptrain-1t7m93p`, `sleeptrain-1tdu6p1`, `sleeptrain-1tlk3ph`, `sleeptrain-1twemlp`, `toddlers-1tvf3r2`, `toddlers-1txlxmw`, `toddlers-1u786ja`.

**Other skipped/partly quoted ledger references (16):** `AttachmentParenting-1u5e3xk`, `AttachmentParenting-1u7mhi9`, `Mommit-1tduosi`, `Mommit-1u4xoje`, `NewParents-1s94inq`, `NewParents-1s9a8zo`, `NewParents-1s9ip0v`, `NewParents-1s9knzg`, `NewParents-1s9wie9`, `NewParents-1u1l1xo`, `sleeptrain-1s9c05u`, `sleeptrain-1s9uohh`, `sleeptrain-1sa4s10`, `sleeptrain-1tvto1m`, `sleeptrain-1twx0ig`, `workingmoms-1t703ue`.

**Additional reader-note review candidates (3):** `NewParents-1s9gnl4`, `Parenting-1s9cp77`, `sleeptrain-1u95oum`.

### R45 — `sources/reddit-reading-r45.md`

**Subject-based whole-unit ledger references (2):** `NewParents-1scj7ht`, `sleeptrain-1sdmi09`.

**Subject-based passage ledger references (53):** `AttachmentParenting-1sbyrwu`, `AttachmentParenting-1sdde0l`, `AttachmentParenting-1se6l6h`, `AttachmentParenting-1se73vx`, `FirstTimeMom-1sc312r`, `Mommit-1sbjgc9`, `Mommit-1sc7893`, `NewParents-1saocv5`, `NewParents-1sax8se`, `NewParents-1sb456x`, `NewParents-1sc16fp`, `NewParents-1sc87t5`, `NewParents-1scbz26`, `NewParents-1scvija`, `NewParents-1sdksf5`, `NewParents-1se8h4u`, `Parenting-1sayv4f`, `Parenting-1sdkss5`, `beyondthebump-1sba4f1`, `beyondthebump-1scjdd7`, `beyondthebump-1sddm18`, `beyondthebumpUK-1sa83vn`, `beyondthebumpUK-1sdcyvm`, `beyondthebumpUK-1sdigpp`, `sleeptrain-1sajasv`, `sleeptrain-1sanzjj`, `sleeptrain-1sap3x0`, `sleeptrain-1sarmo4`, `sleeptrain-1satv4r`, `sleeptrain-1sb2zwr`, `sleeptrain-1sb8g5u`, `sleeptrain-1sbb1gg`, `sleeptrain-1sbbq0m`, `sleeptrain-1sbeijw`, `sleeptrain-1sbjedx`, `sleeptrain-1sbmidb`, `sleeptrain-1sbqlpi`, `sleeptrain-1sc8hdn`, `sleeptrain-1scpgqo`, `sleeptrain-1scrkcy`, `sleeptrain-1sdbnhi`, `sleeptrain-1sdd8oy`, `sleeptrain-1sdktvx`, `sleeptrain-1sdr8yb`, `sleeptrain-1sdwntt`, `sleeptrain-1se59mb`, `sleeptrain-1se8omo`, `toddlers-1sanbnf`, `toddlers-1sawjvl`, `toddlers-1sb25mv`, `toddlers-1sbaytz`, `toddlers-1sbmvuw`, `toddlers-1sedenq`.

**Other skipped/partly quoted ledger references (6):** `NewParents-1se3sjx`, `NewParents-1se548s`, `Parenting-1segy5i`, `sleeptrain-1segxkh`, `toddlers-1scm7g5`, `toddlers-1sdq0on`.

### R46 — `sources/reddit-reading-r46.md`

**Subject-based whole-unit ledger references (11):** `Mommit-1sem5kl`, `NewParents-1sf37dw`, `NewParents-1sfz5nb`, `NewParents-1sgfuke`, `NewParents-1shcg0a`, `beyondthebumpUK-1sgfz48`, `sleeptrain-1sg16s9`, `sleeptrain-1sg1n6g`, `sleeptrain-1sgzggk`, `toddlers-1sfsv4o`, `toddlers-1shc94m`.

**Subject-based passage ledger references (31):** `AttachmentParenting-1sh3euf`, `FirstTimeMom-1sfp06a`, `Mommit-1shazy4`, `NewParents-1semtix`, `NewParents-1sfaseb`, `NewParents-1sg7cmy`, `NewParents-1sg9g8d`, `NewParents-1sh3upx`, `NewParents-1sh54ld`, `NewParents-1shgs2e`, `Parenting-1selc6c`, `sahm-1sewq5d`, `sleeptrain-1seqgqg`, `sleeptrain-1sesycm`, `sleeptrain-1seu2k2`, `sleeptrain-1sevoqt`, `sleeptrain-1sexkvr`, `sleeptrain-1sftz1r`, `sleeptrain-1sgcptc`, `sleeptrain-1sgl4se`, `sleeptrain-1sgmug7`, `sleeptrain-1sgmvo2`, `sleeptrain-1sgo482`, `sleeptrain-1sgu8im`, `sleeptrain-1sgx8fh`, `sleeptrain-1sgxovg`, `toddlers-1sehveq`, `toddlers-1sesyqw`, `toddlers-1sfugnz`, `toddlers-1sgn1an`, `toddlers-1shhvfk`.

**Other skipped/partly quoted ledger references (4):** `beyondthebump-1sgfvf7`, `sleeptrain-1sfamtk`, `toddlers-1sf3ukz`, `toddlers-1sg9haj`.

**Unmapped category review candidates (105):** `Mommit-1seyjg1`, `Mommit-1sf3wd3`, `Mommit-1sgpd21`, `Mommit-1sh59e5`, `NewParents-1sev976`, `NewParents-1sey0pt`, `NewParents-1sf201o`, `NewParents-1sf3si2`, `NewParents-1sfabi4`, `NewParents-1sfvffg`, `NewParents-1sfy2ns`, `NewParents-1sgbq8g`, `NewParents-1sgi9hh`, `NewParents-1sgkcu6`, `NewParents-1sgn3ck`, `NewParents-1sgogvf`, `NewParents-1sgp51b`, `NewParents-1sgxj5z`, `NewParents-1sh7m5u`, `NewParents-1sh7qyo`, `NewParents-1shf29w`, `NewParents-1shf3j7`, `Parenting-1sfh7oq`, `Parenting-1sfvpkm`, `Parenting-1sgskpz`, `Parenting-1sgtdgr`, `ScienceBasedParenting-1sfvx9y`, `beyondthebump-1sfhmsl`, `beyondthebump-1sgkf4x`, `beyondthebump-1shgt0t`, `beyondthebumpUK-1shginv`, `daddit-1sfjfqw`, `sleeptrain-1semh59`, `sleeptrain-1semtw3`, `sleeptrain-1seov3i`, `sleeptrain-1sep4mi`, `sleeptrain-1serkeh`, `sleeptrain-1sevd7z`, `sleeptrain-1sewoqm`, `sleeptrain-1sez1o2`, `sleeptrain-1sez5bb`, `sleeptrain-1sezfd4`, `sleeptrain-1sezsa1`, `sleeptrain-1sf0hcv`, `sleeptrain-1sf15tm`, `sleeptrain-1sf6mmm`, `sleeptrain-1sfe32r`, `sleeptrain-1sfer7t`, `sleeptrain-1sffq9l`, `sleeptrain-1sfgcs5`, `sleeptrain-1sfhpvp`, `sleeptrain-1sfhrug`, `sleeptrain-1sfibbm`, `sleeptrain-1sfkfwv`, `sleeptrain-1sfktlu`, `sleeptrain-1sfm4sd`, `sleeptrain-1sfmoxe`, `sleeptrain-1sftbey`, `sleeptrain-1sfw6x5`, `sleeptrain-1sfxx67`, `sleeptrain-1sg07xr`, `sleeptrain-1sg0bc1`, `sleeptrain-1sg2cya`, `sleeptrain-1sg2zen`, `sleeptrain-1sg3bzo`, `sleeptrain-1sg4ckh`, `sleeptrain-1sg548g`, `sleeptrain-1sg63sz`, `sleeptrain-1sg7xu7`, `sleeptrain-1sg96wl`, `sleeptrain-1sg9wul`, `sleeptrain-1sgaukf`, `sleeptrain-1sgb6jp`, `sleeptrain-1sgenup`, `sleeptrain-1sgenxg`, `sleeptrain-1sgijkz`, `sleeptrain-1sgl325`, `sleeptrain-1sglt71`, `sleeptrain-1sgp9e7`, `sleeptrain-1sgpy0h`, `sleeptrain-1sgrirp`, `sleeptrain-1sgs9lr`, `sleeptrain-1sgsgy8`, `sleeptrain-1sgsjmw`, `sleeptrain-1sgvf6p`, `sleeptrain-1sh09ny`, `sleeptrain-1sh1kqk`, `sleeptrain-1sh238d`, `sleeptrain-1sh81x3`, `sleeptrain-1sh837i`, `sleeptrain-1shbp0w`, `toddlers-1senoz4`, `toddlers-1setgoo`, `toddlers-1setnak`, `toddlers-1seu0oc`, `toddlers-1sexg4l`, `toddlers-1sf3p2j`, `toddlers-1sfe3d2`, `toddlers-1sfuxfa`, `toddlers-1sg1p3h`, `toddlers-1sgbrvp`, `toddlers-1sgdvcc`, `toddlers-1sh2a7d`, `workingmoms-1sfojmj`, `workingmoms-1sg3m8z`.

### R47 — `sources/reddit-reading-r47.md`

**Subject-based whole-unit ledger references (3):** `sleeptrain-1sjf3oe`, `sleeptrain-1sjzep2`, `toddlers-1siu0th`.

**Subject-based passage ledger references (1):** `Mommit-1sk3543`.

**Other skipped/partly quoted ledger references (19):** `FirstTimeMom-1sk37uj`, `Mommit-1sih1hm`, `Mommit-1sjv230`, `NewParents-1sk3hss`, `NewParents-1sk8pr7`, `Parenting-1sk3h0d`, `Parenting-1skkpyd`, `beyondthebump-1sigq06`, `beyondthebump-1sju8uj`, `beyondthebump-1sk4rso`, `daddit-1si47am`, `sleeptrain-1signi0`, `sleeptrain-1sjp4em`, `sleeptrain-1sk3hn4`, `sleeptrain-1skr4n6`, `toddlers-1shqoes`, `toddlers-1si47yr`, `toddlers-1si7bvr`, `toddlers-1skqegh`.

**Additional working-log review candidates (62):** `AttachmentParenting-1siqnvj`, `AttachmentParenting-1sjfxji`, `AttachmentParenting-1skhjun`, `FirstTimeMom-1sitm18`, `Mommit-1sji1tu`, `Mommit-1skh880`, `NewParents-1sho01y`, `NewParents-1si7j36`, `NewParents-1sidw0y`, `NewParents-1siev86`, `NewParents-1sihb36`, `NewParents-1siuo9j`, `NewParents-1sizl4x`, `NewParents-1sju87c`, `NewParents-1sk1va7`, `NewParents-1sk2cqp`, `NewParents-1sk3svf`, `NewParents-1sk64t1`, `NewParents-1sk7iyw`, `Parenting-1silmj6`, `Parenting-1sj23ru`, `Parenting-1sjwfgy`, `Parenting-1ska3ik`, `Parenting-1ska4rr`, `Parenting-1skk3tl`, `beyondthebump-1sil1r6`, `beyondthebumpUK-1shiaj3`, `beyondthebumpUK-1sjgd3y`, `beyondthebumpUK-1sjwmjw`, `sleeptrain-1shk60t`, `sleeptrain-1shno0p`, `sleeptrain-1shpgbm`, `sleeptrain-1shtjyd`, `sleeptrain-1shuc9w`, `sleeptrain-1si3ib0`, `sleeptrain-1si5dl9`, `sleeptrain-1si7lpm`, `sleeptrain-1sia89z`, `sleeptrain-1siep63`, `sleeptrain-1sigfha`, `sleeptrain-1sijrkz`, `sleeptrain-1siyidm`, `sleeptrain-1sizl99`, `sleeptrain-1sj2jyg`, `sleeptrain-1sjasbn`, `sleeptrain-1sjepvi`, `sleeptrain-1sjgf6r`, `sleeptrain-1sjioaq`, `sleeptrain-1sjk5gh`, `sleeptrain-1sjrqva`, `sleeptrain-1sk491a`, `sleeptrain-1sk8opx`, `sleeptrain-1skdu76`, `sleeptrain-1skgyqp`, `sleeptrain-1skjlgp`, `sleeptrain-1skqilb`, `sleeptrain-1skr4qs`, `sleeptrain-1skraxn`, `toddlers-1sj9ol2`, `toddlers-1sjmgyl`, `toddlers-1sjrsnw`, `toddlers-1sk3xax`.

**Additional reader-note review candidates (7):** `NewParents-1sio1fj`, `NewParents-1sj7ziq`, `NewParents-1sjs9nu`, `Parenting-1skgewy`, `sleeptrain-1sk8812`, `toddlers-1sipdnu`, `toddlers-1sjjsoi`.

### R48 — `sources/reddit-reading-r48.md`

**Subject-based whole-unit ledger references (10):** `NewParents-1sla9gq`, `NewParents-1smk4ur`, `NewParents-1smptt8`, `NewParents-1snek4o`, `Parenting-1sni1mn`, `ScienceBasedParenting-1slgpcm`, `beyondthebump-1sn6zt1`, `sleeptrain-1sl9ee7`, `sleeptrain-1sne678`, `toddlers-1snkk4f`.

**Other skipped/partly quoted ledger references (9):** `NewParents-1sljuii`, `NewParents-1slxbjd`, `NewParents-1sn0xqp`, `beyondthebump-1sm9qno`, `beyondthebump-1smxjdv`, `sleeptrain-1sl4pxo`, `sleeptrain-1sm9s42`, `sleeptrain-1sn7pry`, `sleeptrain-1snejhd`.

**Additional working-log review candidates (68):** `AttachmentParenting-1slunt2`, `AttachmentParenting-1slxlsu`, `Mommit-1sm9p95`, `Mommit-1sn324c`, `Mommit-1sndzsy`, `NewParents-1sl4n8t`, `NewParents-1sljaeh`, `NewParents-1sltjtp`, `NewParents-1sm9g48`, `NewParents-1smtfk9`, `NewParents-1sn6ufu`, `Parenting-1slw62k`, `Parenting-1sm8bmr`, `Parenting-1smukqh`, `Parenting-1smxidb`, `Parenting-1sne50l`, `Parenting-1snei4d`, `beyondthebump-1skxhdy`, `beyondthebump-1sljgfh`, `beyondthebump-1smq3xv`, `beyondthebump-1snbdkl`, `beyondthebump-1snis2i`, `beyondthebumpUK-1smj1bs`, `beyondthebumpUK-1sn8f76`, `daddit-1slktx2`, `daddit-1slqp4o`, `sleeptrain-1skrcvt`, `sleeptrain-1skxgf1`, `sleeptrain-1skzhj5`, `sleeptrain-1sl1uic`, `sleeptrain-1sl7axy`, `sleeptrain-1sl9nn4`, `sleeptrain-1sldesx`, `sleeptrain-1sleeam`, `sleeptrain-1slfak2`, `sleeptrain-1slhunk`, `sleeptrain-1slhyog`, `sleeptrain-1sljp0p`, `sleeptrain-1slkw5x`, `sleeptrain-1sloat2`, `sleeptrain-1sls7g5`, `sleeptrain-1sm0hf6`, `sleeptrain-1sm23t1`, `sleeptrain-1sm47o6`, `sleeptrain-1sm47x8`, `sleeptrain-1sm48w1`, `sleeptrain-1sm7nw6`, `sleeptrain-1smeot6`, `sleeptrain-1smesjf`, `sleeptrain-1smgk83`, `sleeptrain-1smj1eb`, `sleeptrain-1smjjjs`, `sleeptrain-1smx2us`, `sleeptrain-1sn3dr9`, `sleeptrain-1sn4nam`, `sleeptrain-1sn51dn`, `sleeptrain-1snasjn`, `sleeptrain-1sne0wl`, `sleeptrain-1snjb2b`, `toddlers-1skzg3x`, `toddlers-1sl4ihq`, `toddlers-1sm57sv`, `toddlers-1sm6wdq`, `toddlers-1smmptr`, `toddlers-1sn7dl3`, `toddlers-1sneiyu`, `toddlers-1snfqtt`, `toddlers-1sngjsh`.

**Additional reader-note review candidates (6):** `beyondthebumpUK-1smx2fo`, `sleeptrain-1slw8ih`, `sleeptrain-1smq6f9`, `sleeptrain-1smxieg`, `sleeptrain-1snaed5`, `toddlers-1skvxeh`.

### R49 — `sources/reddit-reading-r49.md`

**Subject-based whole-unit ledger references (13):** `FirstTimeMom-1snqbpq`, `NewParents-1snlrtw`, `NewParents-1spkds5`, `NewParents-1sqlh40`, `NewParents-1srr2aj`, `NewParents-1srrmb5`, `NewParents-1sruft5`, `beyondthebump-1sotd4s`, `beyondthebump-1srdb2p`, `beyondthebumpUK-1sqkiem`, `sleeptrain-1snsogb`, `sleeptrain-1sr8cg7`, `toddlers-1spyh1w`.

**Subject-based passage ledger references (1):** `NewParents-1sqoiib`.

**Other skipped/partly quoted ledger references (6):** `AttachmentParenting-1sottwe`, `Mommit-1sqio4j`, `NewParents-1snpe2h`, `NewParents-1sq848h`, `beyondthebump-1sra6fw`, `toddlers-1sporc7`.

**Additional working-log review candidates (61):** `AttachmentParenting-1so8eex`, `AttachmentParenting-1sp3ebg`, `AttachmentParenting-1spd5j5`, `AttachmentParenting-1sqj66b`, `AttachmentParenting-1sqqrpl`, `Mommit-1spu41s`, `Mommit-1sq3xia`, `Mommit-1srnmus`, `NewParents-1so4i1z`, `NewParents-1sphs0h`, `NewParents-1sppsy7`, `NewParents-1sq20l0`, `NewParents-1sq2nkl`, `NewParents-1sql8pn`, `NewParents-1sqt8zj`, `NewParents-1sqtliv`, `NewParents-1sr1w15`, `NewParents-1srsci3`, `Parenting-1sqtx0t`, `beyondthebump-1sokaq2`, `beyondthebump-1spviyn`, `beyondthebumpUK-1sq6ao7`, `sleeptrain-1sob6r7`, `sleeptrain-1socsha`, `sleeptrain-1sofdbx`, `sleeptrain-1soltb0`, `sleeptrain-1sop5z1`, `sleeptrain-1soupf4`, `sleeptrain-1sp1ago`, `sleeptrain-1sp2r5n`, `sleeptrain-1sp3v2y`, `sleeptrain-1spfbao`, `sleeptrain-1spg6lc`, `sleeptrain-1spk59m`, `sleeptrain-1spse9y`, `sleeptrain-1sptxxe`, `sleeptrain-1spup0d`, `sleeptrain-1sq9gtr`, `sleeptrain-1sqdj9g`, `sleeptrain-1sqe0iq`, `sleeptrain-1sqgdri`, `sleeptrain-1sqghjn`, `sleeptrain-1sqke7c`, `sleeptrain-1sql5il`, `sleeptrain-1sqq4e8`, `sleeptrain-1sqqbap`, `sleeptrain-1sqr7ij`, `sleeptrain-1sqv83x`, `sleeptrain-1sr3ub4`, `sleeptrain-1sr6763`, `sleeptrain-1sr73a7`, `sleeptrain-1sr8ade`, `sleeptrain-1sr8q4w`, `sleeptrain-1srbvhz`, `sleeptrain-1srcjre`, `sleeptrain-1srfjpu`, `sleeptrain-1srjuhy`, `sleeptrain-1sroy9e`, `sleeptrain-1srq1s2`, `toddlers-1spgji4`, `toddlers-1sqwi71`.

### R50 — `sources/reddit-reading-r50.md`

**Subject-based whole-unit ledger references (3):** `NewParents-1srxt8a`, `beyondthebump-1ssbhbh`, `sleeptrain-1suelbo`.

**Subject-based passage ledger references (44):** `AttachmentParenting-1st5rc0`, `AttachmentParenting-1st7yym`, `AttachmentParenting-1sw1j1w`, `FirstTimeMom-1suv29m`, `FirstTimeMom-1svyrv5`, `Mommit-1ss9k7k`, `Mommit-1ssaxdw`, `NewParents-1st9099`, `NewParents-1st996r`, `NewParents-1stbhdl`, `NewParents-1su8ex3`, `NewParents-1sudw05`, `NewParents-1sug00k`, `NewParents-1svkaja`, `NewParents-1svpy77`, `NewParents-1svtht8`, `Parenting-1st4zmf`, `beyondthebump-1ss5jx3`, `beyondthebump-1stqgnl`, `beyondthebump-1svi2ms`, `beyondthebumpUK-1svo5hr`, `sleeptrain-1ss8a3v`, `sleeptrain-1sshtjd`, `sleeptrain-1ssk2jm`, `sleeptrain-1ssnp2d`, `sleeptrain-1stmbfg`, `sleeptrain-1stnzvs`, `sleeptrain-1su1r0m`, `sleeptrain-1su8ntm`, `sleeptrain-1su943z`, `sleeptrain-1su9rux`, `sleeptrain-1suskhx`, `sleeptrain-1suwt5w`, `sleeptrain-1sv1a3z`, `sleeptrain-1sv3woo`, `sleeptrain-1sv5dfk`, `sleeptrain-1svaiu8`, `sleeptrain-1svfa4m`, `sleeptrain-1svielx`, `sleeptrain-1svvxoy`, `sleeptrain-1sw0uwx`, `toddlers-1ss1o4q`, `toddlers-1ssaiw1`, `toddlers-1stj7w3`.

**Other skipped/partly quoted ledger references (5):** `Mommit-1stygr8`, `NewParents-1ssq1xf`, `sleeptrain-1sug1t9`, `toddlers-1ssaycl`, `toddlers-1st4c8o`.

**Additional working-log review candidates (15):** `NewParents-1ssr73n`, `NewParents-1stnw6q`, `NewParents-1stpa94`, `NewParents-1stpt3c`, `Parenting-1suj7u2`, `beyondthebump-1ssq0v0`, `beyondthebump-1sunrhd`, `beyondthebumpUK-1st076b`, `sahm-1sto986`, `sleeptrain-1ss1f5z`, `sleeptrain-1suim7e`, `sleeptrain-1suny7k`, `sleeptrain-1sv2etf`, `sleeptrain-1svttrk`, `toddlers-1sv46vb`.

**Additional reader-note review candidates (9):** `NewParents-1srva4r`, `NewParents-1ss984m`, `NewParents-1stfj6r`, `beyondthebump-1stfci3`, `sleeptrain-1star1r`, `sleeptrain-1stkefx`, `sleeptrain-1stutca`, `sleeptrain-1sv0kjv`, `sleeptrain-1svm60v`.

### R51 — `sources/reddit-reading-r51.md`

**Subject-based whole-unit ledger references (10):** `FirstTimeMom-1sz1h4x`, `NewParents-1sy47t7`, `NewParents-1syayoy`, `NewParents-1syq42j`, `beyondthebump-1swn8fm`, `beyondthebump-1sxlqes`, `beyondthebump-1sy2nb8`, `sahm-1sxz1lw`, `sleeptrain-1sw7j07`, `sleeptrain-1swxg6u`.

**Other skipped/partly quoted ledger references (3):** `NewParents-1sya6rt`, `NewParents-1sz11wm`, `beyondthebump-1swdnik`.

**Additional working-log review candidates (41):** `AttachmentParenting-1sz10wn`, `Mommit-1sxc8i6`, `Mommit-1sxjf24`, `NewParents-1swzr2a`, `NewParents-1swzudk`, `NewParents-1synkb1`, `NewParents-1sz402z`, `NewParents-1szamgo`, `Parenting-1sxp4sd`, `Parenting-1sydn9y`, `Parenting-1szaoe2`, `beyondthebumpUK-1sy2ru2`, `beyondthebumpUK-1synp70`, `daddit-1syk4k4`, `daddit-1sym6pf`, `sleeptrain-1sw7mdl`, `sleeptrain-1swmf7z`, `sleeptrain-1swr69w`, `sleeptrain-1swsmbo`, `sleeptrain-1swxqpz`, `sleeptrain-1sx8naa`, `sleeptrain-1sx9mm4`, `sleeptrain-1sxk9cv`, `sleeptrain-1sxkteg`, `sleeptrain-1sxrsrp`, `sleeptrain-1sy18c6`, `sleeptrain-1sy38rb`, `sleeptrain-1syb2ty`, `sleeptrain-1syn3vp`, `sleeptrain-1syrgev`, `sleeptrain-1syut8c`, `sleeptrain-1sywe04`, `sleeptrain-1sywjio`, `sleeptrain-1syyavg`, `sleeptrain-1sz120l`, `sleeptrain-1sz1klf`, `sleeptrain-1sz1lgb`, `sleeptrain-1sz5a63`, `sleeptrain-1szbhco`, `toddlers-1sxv6t2`, `toddlers-1sxxuuo`.

### R52 — `sources/reddit-reading-r52.md`

**Subject-based whole-unit ledger references (7):** `Mommit-1t1krah`, `NewParents-1t10wax`, `NewParents-1t17uks`, `NewParents-1t2b517`, `beyondthebump-1t33wss`, `daddit-1t0x2cx`, `sleeptrain-1t2zpn3`.

**Subject-based passage ledger references (45):** `AttachmentParenting-1szkvmw`, `AttachmentParenting-1t104zf`, `AttachmentParenting-1t1k2bd`, `AttachmentParenting-1t2lf40`, `FirstTimeMom-1t0msz6`, `Mommit-1t04q9l`, `NewParents-1sze5nq`, `NewParents-1t06ei2`, `NewParents-1t06tzx`, `NewParents-1t0kfe5`, `NewParents-1t0qdes`, `NewParents-1t0un68`, `NewParents-1t0uzy3`, `NewParents-1t1jei7`, `NewParents-1t1oubs`, `NewParents-1t1yrm5`, `NewParents-1t2frvr`, `NewParents-1t3bz59`, `beyondthebump-1t07xul`, `beyondthebump-1t0sxur`, `beyondthebump-1t1y8mo`, `beyondthebump-1t370og`, `beyondthebumpUK-1szce4g`, `beyondthebumpUK-1t1kozb`, `sleeptrain-1szhx8a`, `sleeptrain-1szkl5a`, `sleeptrain-1szr6ud`, `sleeptrain-1sztcnx`, `sleeptrain-1t00aj9`, `sleeptrain-1t02ss5`, `sleeptrain-1t0o0qh`, `sleeptrain-1t0w1sd`, `sleeptrain-1t1fx6q`, `sleeptrain-1t1ock6`, `sleeptrain-1t1qhi3`, `sleeptrain-1t1shyj`, `sleeptrain-1t1smgo`, `sleeptrain-1t225oo`, `sleeptrain-1t2logt`, `sleeptrain-1t2n6xt`, `sleeptrain-1t2s5i0`, `sleeptrain-1t2xtcm`, `sleeptrain-1t31sw4`, `toddlers-1szcoii`, `toddlers-1t2kwha`.

**Other skipped/partly quoted ledger references (5):** `Mommit-1t0coxo`, `beyondthebump-1t0cqlx`, `sleeptrain-1szdftd`, `toddlers-1t0sz1z`, `toddlers-1t1qnic`.

**Additional working-log review candidates (11):** `NewParents-1t0cnv9`, `beyondthebump-1szdecd`, `beyondthebump-1t0rga5`, `beyondthebump-1t2y5vk`, `sleeptrain-1t0pj22`, `sleeptrain-1t0q8r8`, `sleeptrain-1t0sx3b`, `sleeptrain-1t2twmc`, `sleeptrain-1t33qq4`, `sleeptrain-1t3auz0`, `toddlers-1t0dpul`.

### R53 — `sources/reddit-reading-r53.md`

**Subject-based whole-unit ledger references (5):** `NewParents-1t515kf`, `beyondthebumpUK-1t55cpb`, `toddlers-1t52mcg`, `toddlers-1t6u8g7`, `workingmoms-1t67w5z`.

**Subject-based passage ledger references (2):** `sleeptrain-1t3kacb`, `sleeptrain-1t5hytc`.

**Other skipped/partly quoted ledger references (2):** `beyondthebumpUK-1t55dpi`, `toddlers-1t7e2i0`.

### R54 — `sources/reddit-reading-r54.md`

**Subject-based whole-unit ledger references (13):** `Mommit-1tbkpi8`, `NewParents-1t9oqqz`, `NewParents-1t9yyd1`, `NewParents-1tb1o73`, `NewParents-1tb9w7o`, `NewParents-1tbr0rb`, `NewParents-1tbu04j`, `NewParents-1tck6jy`, `beyondthebump-1tblwtj`, `beyondthebump-1tbx9ym`, `daddit-1tblybw`, `sleeptrain-1tc95k1`, `sleeptrain-1tcn6f7`.

**Subject-based passage ledger references (1):** `NewParents-1tcsy5n`.

**Other skipped/partly quoted ledger references (3):** `AttachmentParenting-1tbwz7r`, `sleeptrain-1tc9m2x`, `toddlers-1tae1we`.

**Unmapped category review candidates (144):** `AttachmentParenting-1t7xn33`, `AttachmentParenting-1tboxr0`, `AttachmentParenting-1tc5doz`, `FirstTimeMom-1t9an9b`, `FirstTimeMom-1tb2nv0`, `Mommit-1t99kd1`, `Mommit-1t9ejb1`, `Mommit-1t9r72a`, `Mommit-1tbk64h`, `NewParents-1t89jz8`, `NewParents-1t8d0tm`, `NewParents-1t8rk85`, `NewParents-1t8t6mj`, `NewParents-1t8tp9w`, `NewParents-1t99vw5`, `NewParents-1t9n24j`, `NewParents-1t9or1o`, `NewParents-1t9rsxn`, `NewParents-1t9s1mi`, `NewParents-1taib3d`, `NewParents-1tan10l`, `NewParents-1tb0vn8`, `NewParents-1tb36lh`, `NewParents-1tb5a99`, `NewParents-1tb8u3z`, `NewParents-1tbh4e3`, `NewParents-1tbmq62`, `NewParents-1tbmr3z`, `NewParents-1tbo9d3`, `NewParents-1tc4a0h`, `NewParents-1tc510m`, `NewParents-1tceyit`, `Parenting-1tan8xo`, `Parenting-1taobxl`, `Parenting-1tbwua3`, `Parenting-1tc82cy`, `beyondthebump-1t8zqly`, `beyondthebump-1t92eq2`, `beyondthebump-1t92l5m`, `beyondthebump-1t9m1eo`, `beyondthebump-1t9orv7`, `beyondthebump-1t9uq7u`, `beyondthebump-1taq9eb`, `beyondthebump-1tavc9a`, `beyondthebump-1tb5w5n`, `beyondthebump-1tb9ilz`, `beyondthebump-1tbi20l`, `beyondthebump-1tbmdk0`, `beyondthebump-1tbszub`, `beyondthebump-1tci5rh`, `beyondthebump-1tcke8j`, `beyondthebumpUK-1t8daqj`, `beyondthebumpUK-1tagow4`, `beyondthebumpUK-1tbuaps`, `daddit-1t8buqz`, `daddit-1ta3ad2`, `sleeptrain-1t7wfa8`, `sleeptrain-1t85rd4`, `sleeptrain-1t87yhi`, `sleeptrain-1t89caj`, `sleeptrain-1t8gqkg`, `sleeptrain-1t8ht21`, `sleeptrain-1t8ijfe`, `sleeptrain-1t8od0r`, `sleeptrain-1t8pibg`, `sleeptrain-1t8wwl7`, `sleeptrain-1t8zsq2`, `sleeptrain-1t9172p`, `sleeptrain-1t955s1`, `sleeptrain-1t96y1s`, `sleeptrain-1t98e2c`, `sleeptrain-1t98jny`, `sleeptrain-1t9aplk`, `sleeptrain-1t9dpfx`, `sleeptrain-1t9fb9m`, `sleeptrain-1t9m6ia`, `sleeptrain-1t9mnsc`, `sleeptrain-1t9ofcv`, `sleeptrain-1t9pob0`, `sleeptrain-1t9qvcf`, `sleeptrain-1t9rmpn`, `sleeptrain-1t9sfcw`, `sleeptrain-1t9sxf1`, `sleeptrain-1t9vnqc`, `sleeptrain-1t9wciu`, `sleeptrain-1t9z4kp`, `sleeptrain-1t9zoql`, `sleeptrain-1ta1ini`, `sleeptrain-1ta2xv5`, `sleeptrain-1ta3s1d`, `sleeptrain-1ta5cxb`, `sleeptrain-1ta5q14`, `sleeptrain-1ta8ao0`, `sleeptrain-1ta9bvr`, `sleeptrain-1tac2uz`, `sleeptrain-1tafg25`, `sleeptrain-1tafj1f`, `sleeptrain-1taifc2`, `sleeptrain-1tam88o`, `sleeptrain-1taozsp`, `sleeptrain-1tavoh1`, `sleeptrain-1tayks2`, `sleeptrain-1tb1alr`, `sleeptrain-1tb1gwn`, `sleeptrain-1tb4ix0`, `sleeptrain-1tb4yfo`, `sleeptrain-1tbarwk`, `sleeptrain-1tbc4mb`, `sleeptrain-1tbcfe6`, `sleeptrain-1tbf5y0`, `sleeptrain-1tbmga2`, `sleeptrain-1tbnwjq`, `sleeptrain-1tbqqxj`, `sleeptrain-1tbt0vf`, `sleeptrain-1tbtver`, `sleeptrain-1tbwu8w`, `sleeptrain-1tc0k8s`, `sleeptrain-1tc0kvu`, `sleeptrain-1tc0ryl`, `sleeptrain-1tc3ev6`, `sleeptrain-1tc4vbd`, `sleeptrain-1tc68en`, `sleeptrain-1tc78ul`, `sleeptrain-1tc7usf`, `sleeptrain-1tc84ch`, `sleeptrain-1tc94yl`, `sleeptrain-1tcb9wf`, `sleeptrain-1tcdzfg`, `sleeptrain-1tck8np`, `sleeptrain-1tcpk8z`, `sleeptrain-1tcqrds`, `sleeptrain-1tcr09e`, `sleeptrain-1tcrmsu`, `sleeptrain-1tcsqo6`, `toddlers-1t85mmz`, `toddlers-1t8i83x`, `toddlers-1t9njnc`, `toddlers-1ta2fyv`, `toddlers-1ta4v3b`, `toddlers-1tamm4z`, `toddlers-1tb04m3`, `toddlers-1tbw2xh`, `toddlers-1tc5mo8`, `toddlers-1tcjhi4`.

### R55 — `sources/reddit-reading-r55.md`

**Subject-based whole-unit ledger references (13):** `NewParents-1teat0n`, `NewParents-1tfe9r5`, `NewParents-1tg4wtq`, `NewParents-1tgozy3`, `NewParents-1tgvzil`, `NewParents-1tgxsu8`, `beyondthebump-1tfssib`, `sleeptrain-1tg9qtj`, `sleeptrain-1tgcvhu`, `toddlers-1tcu9nv`, `toddlers-1tdw6co`, `toddlers-1tfnfwe`, `toddlers-1th0888`.

**Other skipped/partly quoted ledger references (54):** `AttachmentParenting-1teclfa`, `AttachmentParenting-1th0hd5`, `AttachmentParenting-1th2mcb`, `FirstTimeMom-1tes2fw`, `FirstTimeMom-1tfszr5`, `Mommit-1tfqsrl`, `NewParents-1td3dti`, `NewParents-1tdfz76`, `NewParents-1tdmq89`, `NewParents-1tdq3t6`, `NewParents-1teehri`, `NewParents-1tev10m`, `NewParents-1tfqev2`, `NewParents-1tg3l06`, `NewParents-1tgb2km`, `Parenting-1td3c42`, `Parenting-1teydz5`, `Parenting-1tfnr08`, `beyondthebump-1tdf02n`, `beyondthebump-1tdghil`, `beyondthebump-1tdzyb1`, `beyondthebump-1tgum67`, `beyondthebump-1th6c0r`, `beyondthebump-1th7o0j`, `beyondthebumpUK-1tf93sk`, `sleeptrain-1tctbup`, `sleeptrain-1tcx9y5`, `sleeptrain-1tdbv3u`, `sleeptrain-1tdhvd5`, `sleeptrain-1tdjhvx`, `sleeptrain-1tdsufr`, `sleeptrain-1tdvbyv`, `sleeptrain-1te1kvl`, `sleeptrain-1te1wc1`, `sleeptrain-1te3weh`, `sleeptrain-1teces3`, `sleeptrain-1tei2nj`, `sleeptrain-1teit4w`, `sleeptrain-1ter7n4`, `sleeptrain-1tevhdr`, `sleeptrain-1tf0mmv`, `sleeptrain-1tfcu1p`, `sleeptrain-1tfgkp6`, `sleeptrain-1tfpnee`, `sleeptrain-1tft3p1`, `sleeptrain-1tg5sec`, `sleeptrain-1tg92vn`, `sleeptrain-1tgb11f`, `sleeptrain-1tgb9dw`, `sleeptrain-1tgdakg`, `sleeptrain-1tgmiz7`, `sleeptrain-1th73fb`, `toddlers-1td68cu`, `toddlers-1teaqvm`.

### R56 — `sources/reddit-reading-r56.md`

**Subject-based whole-unit ledger references (4):** `NewParents-1tjhvdi`, `ScienceBasedParenting-1tiy3z6`, `sahm-1ti5x95`, `sleeptrain-1tj802e`.

**Subject-based passage ledger references (50):** `AttachmentParenting-1thbh0f`, `AttachmentParenting-1thc7xj`, `AttachmentParenting-1tie8mw`, `AttachmentParenting-1tkjlvj`, `Mommit-1thi0wr`, `Mommit-1tjd2hw`, `NewParents-1thk9ra`, `NewParents-1ticwl0`, `NewParents-1tie624`, `NewParents-1tijxs2`, `NewParents-1tis935`, `NewParents-1tj9tp0`, `NewParents-1tjrmx9`, `NewParents-1tk3t78`, `NewParents-1tk89eh`, `NewParents-1tke1co`, `NewParents-1tkeuk3`, `NewParents-1tki3y6`, `Parenting-1tinaj8`, `Parenting-1tkctab`, `beyondthebump-1tilxzg`, `beyondthebump-1tim3h6`, `beyondthebump-1tj54kc`, `beyondthebump-1tj6jg8`, `beyondthebump-1tjwivp`, `beyondthebump-1tk3p44`, `beyondthebumpUK-1tibszz`, `beyondthebumpUK-1tii3b1`, `sleeptrain-1thh8hg`, `sleeptrain-1thkqz9`, `sleeptrain-1thsq3d`, `sleeptrain-1thvyfu`, `sleeptrain-1thx59j`, `sleeptrain-1thz5bh`, `sleeptrain-1ti0s75`, `sleeptrain-1tiadq5`, `sleeptrain-1tiecpz`, `sleeptrain-1tijyvh`, `sleeptrain-1tiyw70`, `sleeptrain-1tiz8zz`, `sleeptrain-1tj07h5`, `sleeptrain-1tjf0vt`, `sleeptrain-1tjgaur`, `sleeptrain-1tjkn4e`, `sleeptrain-1tjnx2s`, `sleeptrain-1tjq60o`, `sleeptrain-1tk2z0i`, `sleeptrain-1tk3v07`, `sleeptrain-1tk76hb`, `toddlers-1tj30ei`.

**Other skipped/partly quoted ledger references (5):** `NewParents-1tj3fpa`, `NewParents-1tkcypf`, `Parenting-1tinx51`, `sleeptrain-1thbral`, `toddlers-1thaapd`.

### R57 — `sources/reddit-reading-r57.md`

**Subject-based whole-unit ledger references (10):** `NewParents-1tkpivw`, `NewParents-1tml295`, `NewParents-1tn1jp8`, `Parenting-1to4hkm`, `beyondthebumpUK-1tknsgt`, `beyondthebumpUK-1tlpekf`, `beyondthebumpUK-1tm4gox`, `daddit-1totq8a`, `sleeptrain-1tmw7ga`, `toddlers-1tn7srt`.

**Subject-based passage ledger references (60):** `AttachmentParenting-1tm1ufl`, `AttachmentParenting-1tm32oh`, `AttachmentParenting-1tmlx6s`, `AttachmentParenting-1tmw06j`, `AttachmentParenting-1tn9a49`, `AttachmentParenting-1to6gjd`, `FirstTimeMom-1tmzcmx`, `Mommit-1tmnunu`, `Mommit-1tohpiq`, `NewParents-1tl2q58`, `NewParents-1tl2q9g`, `NewParents-1tlbjma`, `NewParents-1tmbzbf`, `NewParents-1tmx155`, `NewParents-1tn492n`, `NewParents-1tn5xdl`, `NewParents-1tnax2d`, `NewParents-1tnjng2`, `NewParents-1tnni12`, `NewParents-1tnnl97`, `NewParents-1to0erq`, `NewParents-1todhp0`, `Parenting-1tkoc3f`, `Parenting-1tlohhm`, `beyondthebump-1tmlp9l`, `beyondthebump-1tn7oaz`, `beyondthebump-1to4mja`, `beyondthebump-1top7xv`, `beyondthebumpUK-1tlqjuz`, `beyondthebumpUK-1tls3a0`, `beyondthebumpUK-1togex2`, `beyondthebumpUK-1togx32`, `sleeptrain-1tkn8g4`, `sleeptrain-1tl5h9b`, `sleeptrain-1tlfq32`, `sleeptrain-1tlidhw`, `sleeptrain-1tlus0o`, `sleeptrain-1tlzo4h`, `sleeptrain-1tm82w2`, `sleeptrain-1tmcm0h`, `sleeptrain-1tmws57`, `sleeptrain-1tmzk34`, `sleeptrain-1tn0q3k`, `sleeptrain-1tn7ecj`, `sleeptrain-1tnanf3`, `sleeptrain-1tneb0x`, `sleeptrain-1tneydy`, `sleeptrain-1tng1xs`, `sleeptrain-1tnu9jf`, `sleeptrain-1tnvq2w`, `sleeptrain-1to44rs`, `sleeptrain-1tog9pz`, `sleeptrain-1tok2w5`, `toddlers-1tmnhdl`, `toddlers-1tmyu39`, `toddlers-1tofsv5`, `toddlers-1toj00r`, `toddlers-1tol14c`, `toddlers-1tolfy7`, `toddlers-1toq34w`.

**Other skipped/partly quoted ledger references (9):** `NewParents-1tn3yst`, `Parenting-1to9wek`, `sleeptrain-1tmbkx7`, `sleeptrain-1tmedbe`, `sleeptrain-1togqyd`, `sleeptrain-1toipsd`, `toddlers-1tlln67`, `toddlers-1tnjt83`, `toddlers-1to4q1q`.

### R58 — `sources/reddit-reading-r58.md`

**Subject-based whole-unit ledger references (10):** `NewParents-1towuwn`, `NewParents-1trta2e`, `NewParents-1tsl5x9`, `beyondthebump-1tsbfc8`, `beyondthebump-1tsl6nl`, `beyondthebumpUK-1trcwmv`, `sleeptrain-1tq4fz0`, `sleeptrain-1tqbd8q`, `sleeptrain-1tqq20t`, `toddlers-1tqmtn5`.

**Subject-based passage ledger references (36):** `AttachmentParenting-1tryo0t`, `Mommit-1tpv213`, `Mommit-1tr209t`, `Mommit-1trjysf`, `NewParents-1tp9j94`, `NewParents-1tpoxji`, `NewParents-1tpt4gm`, `NewParents-1tq41mg`, `NewParents-1tq493b`, `NewParents-1tq6kk4`, `NewParents-1tqb0ts`, `NewParents-1tqkw91`, `NewParents-1tr66zd`, `NewParents-1tra6mm`, `NewParents-1troixj`, `NewParents-1tsf3h7`, `NewParents-1tsivh5`, `Parenting-1tq1evi`, `Parenting-1tqdweh`, `Parenting-1tqpf8v`, `daddit-1tq6i6n`, `sleeptrain-1tq3w1s`, `sleeptrain-1tq84eu`, `sleeptrain-1tq9yoc`, `sleeptrain-1tqfuqs`, `sleeptrain-1tqll3u`, `sleeptrain-1tr5q7o`, `sleeptrain-1trw38h`, `sleeptrain-1trx0vw`, `sleeptrain-1ts025t`, `sleeptrain-1ts58m3`, `sleeptrain-1ts9qjh`, `sleeptrain-1tsaivy`, `toddlers-1tq1nku`, `toddlers-1trppav`, `toddlers-1ts8p50`.

**Other skipped/partly quoted ledger references (13):** `AttachmentParenting-1tr66ih`, `Mommit-1trzyhv`, `NewParents-1tpwml3`, `NewParents-1tr9mn2`, `NewParents-1trddvb`, `NewParents-1trk3ur`, `NewParents-1tsjl7g`, `Parenting-1tqbnqd`, `Parenting-1trcklj`, `Parenting-1trohxt`, `sleeptrain-1tphn4k`, `sleeptrain-1trqljo`, `sleeptrain-1trvved`.

### R59 — `sources/reddit-reading-r59.md`

**Subject-based whole-unit ledger references (4):** `Mommit-1tvxhof`, `beyondthebump-1tuu9oz`, `toddlers-1tur8t6`, `toddlers-1tvxfnz`.

**Subject-based passage ledger references (50):** `AttachmentParenting-1tukyd5`, `AttachmentParenting-1twbb1m`, `AttachmentParenting-1twv1kb`, `FirstTimeMom-1tstgnz`, `NewParents-1tt06do`, `NewParents-1tt2723`, `NewParents-1ttd3aq`, `NewParents-1ttpaoy`, `NewParents-1ttz3qj`, `NewParents-1tuij5n`, `NewParents-1tuyi7l`, `NewParents-1tvh78h`, `NewParents-1tvse4q`, `NewParents-1tvu13t`, `NewParents-1tw2cwf`, `NewParents-1twskts`, `Parenting-1tvric3`, `beyondthebump-1tu13lz`, `beyondthebump-1tuaj60`, `beyondthebump-1tucbjw`, `beyondthebump-1tv28uu`, `beyondthebump-1tv4can`, `daddit-1tsl7ow`, `sahm-1tutdj9`, `sleeptrain-1tt6r6f`, `sleeptrain-1ttlikq`, `sleeptrain-1ttvifz`, `sleeptrain-1ttzhkl`, `sleeptrain-1tu0ce2`, `sleeptrain-1tu1x7y`, `sleeptrain-1tudaid`, `sleeptrain-1tugxjf`, `sleeptrain-1tullyh`, `sleeptrain-1tv69ld`, `sleeptrain-1tvbodw`, `sleeptrain-1tvc7xx`, `sleeptrain-1tvfvkl`, `sleeptrain-1tvhle5`, `sleeptrain-1tvm5zx`, `sleeptrain-1tvpfau`, `sleeptrain-1tvuabt`, `sleeptrain-1tw4j4l`, `sleeptrain-1tw5vpg`, `sleeptrain-1tw8fhw`, `sleeptrain-1tw9s3v`, `sleeptrain-1twatnc`, `sleeptrain-1twi11q`, `sleeptrain-1twjsd7`, `toddlers-1tthyo9`, `toddlers-1twjq91`.

**Other skipped/partly quoted ledger references (6):** `FirstTimeMom-1tuh27j`, `Mommit-1ttshhe`, `NewParents-1tui7gk`, `Parenting-1tt295p`, `beyondthebump-1tt28bc`, `toddlers-1tsmuzh`.

### R60 — `sources/reddit-reading-r60.md`

**Subject-based whole-unit ledger references (10):** `AttachmentParenting-1tx1uy2`, `Mommit-1tykbr2`, `NewParents-1txb2ky`, `NewParents-1txmbkb`, `NewParents-1tzmk58`, `NewParents-1u106v0`, `Parenting-1u15dna`, `beyondthebump-1u0hfnf`, `sleeptrain-1u0j0d2`, `toddlers-1u0ridu`.

**Subject-based passage ledger references (11):** `Mommit-1u15426`, `NewParents-1txfdav`, `NewParents-1tzckcn`, `NewParents-1u0vhjy`, `beyondthebumpUK-1tzmi6q`, `daddit-1tx11k4`, `sleeptrain-1u0mq7t`, `sleeptrain-1u1diok`, `sleeptrain-1u1gony`, `toddlers-1u0pv2o`, `toddlers-1u10z9r`.

**Other skipped/partly quoted ledger references (39):** `AttachmentParenting-1tzsmz1`, `AttachmentParenting-1u0baqg`, `AttachmentParenting-1u0qiet`, `Mommit-1u07a8k`, `NewParents-1tyuvyh`, `NewParents-1tzc88c`, `NewParents-1u05vl3`, `NewParents-1u0alt0`, `NewParents-1u0k0i6`, `NewParents-1u0kq2h`, `NewParents-1u0ntwh`, `beyondthebump-1tz99uy`, `beyondthebumpUK-1tyd02y`, `sleeptrain-1twwg85`, `sleeptrain-1tx0w4z`, `sleeptrain-1txdcj1`, `sleeptrain-1txt6wu`, `sleeptrain-1ty1ayf`, `sleeptrain-1tyddiq`, `sleeptrain-1tymnfz`, `sleeptrain-1tyv31x`, `sleeptrain-1tz0iyy`, `sleeptrain-1tz8cns`, `sleeptrain-1tzb12f`, `sleeptrain-1tzoraf`, `sleeptrain-1tzppj5`, `sleeptrain-1tzxiju`, `sleeptrain-1u01d1d`, `sleeptrain-1u01xx9`, `sleeptrain-1u06g5m`, `sleeptrain-1u0d3rk`, `sleeptrain-1u0fupq`, `sleeptrain-1u0j7ja`, `sleeptrain-1u0kvfg`, `sleeptrain-1u15m3b`, `sleeptrain-1u1bv70`, `sleeptrain-1u1g5gg`, `toddlers-1txwpmu`, `toddlers-1u1d3px`.

### R61 — `sources/reddit-reading-r61.md`

**Subject-based whole-unit ledger references (2):** `NewParents-1u4h0rf`, `toddlers-1u3r55i`.

**Subject-based passage ledger references (25):** `FirstTimeMom-1u334xt`, `NewParents-1u1rket`, `NewParents-1u307gu`, `NewParents-1u39qdi`, `NewParents-1u4091b`, `NewParents-1u46559`, `NewParents-1u54br7`, `NewParents-1u5glbp`, `Parenting-1u3bdg4`, `Parenting-1u5h00i`, `beyondthebump-1u2urv8`, `sleeptrain-1u1ijgv`, `sleeptrain-1u25q2s`, `sleeptrain-1u2b8hj`, `sleeptrain-1u2kmfe`, `sleeptrain-1u2u1je`, `sleeptrain-1u36bqg`, `sleeptrain-1u4j1vl`, `sleeptrain-1u4s40o`, `sleeptrain-1u4uxdm`, `sleeptrain-1u53k8x`, `sleeptrain-1u56rgo`, `toddlers-1u4rcid`, `toddlers-1u566o0`, `toddlers-1u57nou`.

**Additional working-log review candidates (52):** `AttachmentParenting-1u26irk`, `AttachmentParenting-1u2y6nw`, `AttachmentParenting-1u4cgx6`, `AttachmentParenting-1u4ddy0`, `AttachmentParenting-1u5lq0l`, `GentleParenting-1u2fpcb`, `Mommit-1u48s0q`, `Mommit-1u4o28i`, `NewParents-1u1nu3y`, `NewParents-1u30xxw`, `NewParents-1u34ruq`, `NewParents-1u3ymp9`, `NewParents-1u54zvm`, `Parenting-1u5hlrw`, `Parenting-1u5ig8k`, `beyondthebump-1u3n8xn`, `beyondthebump-1u5fugf`, `daddit-1u4swnw`, `sleeptrain-1u1yuhb`, `sleeptrain-1u1zhi3`, `sleeptrain-1u1zjsj`, `sleeptrain-1u26yfr`, `sleeptrain-1u29fbl`, `sleeptrain-1u2gjsb`, `sleeptrain-1u2jsia`, `sleeptrain-1u2lkvy`, `sleeptrain-1u2lp51`, `sleeptrain-1u2vgdw`, `sleeptrain-1u30p35`, `sleeptrain-1u311qd`, `sleeptrain-1u31oth`, `sleeptrain-1u32j18`, `sleeptrain-1u34txm`, `sleeptrain-1u35sr5`, `sleeptrain-1u36v39`, `sleeptrain-1u3jwj9`, `sleeptrain-1u3jzz4`, `sleeptrain-1u3l50a`, `sleeptrain-1u3pfm6`, `sleeptrain-1u3pkfm`, `sleeptrain-1u40hvn`, `sleeptrain-1u4mt1h`, `sleeptrain-1u4o2pt`, `sleeptrain-1u4uxrg`, `sleeptrain-1u539o9`, `sleeptrain-1u58clw`, `sleeptrain-1u5e0zs`, `sleeptrain-1u5i7gr`, `sleeptrain-1u5j584`, `sleeptrain-1u5j8vp`, `sleeptrain-1u5jcc7`, `sleeptrain-1u5kxio`.

### R62 — `sources/reddit-reading-r62.md`

**Subject-based whole-unit ledger references (7):** `AttachmentParenting-1u892nd`, `NewParents-1u64z85`, `NewParents-1u9buwe`, `Parenting-1u9w3gd`, `sleeptrain-1u6qzjm`, `sleeptrain-1u7vera`, `sleeptrain-1u9btw6`.

**Subject-based passage ledger references (10):** `Mommit-1u5x0t7`, `NewParents-1u7ghqj`, `sleeptrain-1u63vqq`, `sleeptrain-1u8t62t`, `sleeptrain-1u988t9`, `sleeptrain-1u9osix`, `sleeptrain-1ua0qco`, `sleeptrain-1uamhai`, `toddlers-1u7nfg5`, `toddlers-1u87xvf`.

**Other skipped/partly quoted ledger references (4):** `Mommit-1u8dvi3`, `NewParents-1ua8ei6`, `NewParents-1uawafj`, `beyondthebump-1u8jnkj`.

**Unmapped category review candidates (138):** `AttachmentParenting-1u5vx9n`, `AttachmentParenting-1u84n5u`, `AttachmentParenting-1u8o7qv`, `AttachmentParenting-1uadna0`, `AttachmentParenting-1uagm0j`, `AttachmentParenting-1uapgm0`, `FirstTimeMom-1u6oa9u`, `Mommit-1u5pwgd`, `Mommit-1u7q2mg`, `Mommit-1u8zozu`, `NewParents-1u5t5yb`, `NewParents-1u5u5ux`, `NewParents-1u6ch8t`, `NewParents-1u6k9zx`, `NewParents-1u6kkb5`, `NewParents-1u6n6ti`, `NewParents-1u7a42o`, `NewParents-1u7c5qo`, `NewParents-1u7f8cu`, `NewParents-1u7wquw`, `NewParents-1u82rae`, `NewParents-1u8h3x3`, `NewParents-1u8jmm6`, `NewParents-1u990g2`, `NewParents-1u9jk5z`, `NewParents-1u9q5vm`, `NewParents-1u9qhpp`, `NewParents-1ua4oc1`, `NewParents-1uaq4k6`, `Parenting-1u6zspa`, `Parenting-1u7ft8b`, `Parenting-1u8dv78`, `Parenting-1u9y8uf`, `Parenting-1uahj95`, `Parenting-1uaybym`, `ScienceBasedParenting-1u8kml7`, `beyondthebump-1u6otjh`, `beyondthebump-1u6zsuc`, `beyondthebump-1u72454`, `beyondthebump-1u756l0`, `beyondthebump-1uaehdf`, `beyondthebump-1uaqdz2`, `beyondthebumpUK-1u7x7hi`, `beyondthebumpUK-1u8byqe`, `beyondthebumpUK-1u8z9aj`, `daddit-1u9yj4k`, `daddit-1uatewl`, `sahm-1ua6xpi`, `sahm-1uaaxp5`, `sleeptrain-1u5obqh`, `sleeptrain-1u5qrca`, `sleeptrain-1u5s3yc`, `sleeptrain-1u5swgg`, `sleeptrain-1u5xhq4`, `sleeptrain-1u69c53`, `sleeptrain-1u6avkf`, `sleeptrain-1u6ca9z`, `sleeptrain-1u6dm0w`, `sleeptrain-1u6l1u0`, `sleeptrain-1u6ow00`, `sleeptrain-1u6rp4h`, `sleeptrain-1u6uhk6`, `sleeptrain-1u6xyhf`, `sleeptrain-1u70lzn`, `sleeptrain-1u74hex`, `sleeptrain-1u74pbc`, `sleeptrain-1u7556g`, `sleeptrain-1u79qr3`, `sleeptrain-1u7acfg`, `sleeptrain-1u7f4le`, `sleeptrain-1u7fy3l`, `sleeptrain-1u7gblr`, `sleeptrain-1u7ipo4`, `sleeptrain-1u7jo1o`, `sleeptrain-1u7l0dz`, `sleeptrain-1u7lw6i`, `sleeptrain-1u7mnp8`, `sleeptrain-1u7ni1l`, `sleeptrain-1u7nuib`, `sleeptrain-1u7nw0n`, `sleeptrain-1u7qhtw`, `sleeptrain-1u7vx26`, `sleeptrain-1u7xj8z`, `sleeptrain-1u7yyw0`, `sleeptrain-1u7z3js`, `sleeptrain-1u836q0`, `sleeptrain-1u84q7q`, `sleeptrain-1u8536s`, `sleeptrain-1u86qpc`, `sleeptrain-1u8a5az`, `sleeptrain-1u8cwtv`, `sleeptrain-1u8g7x8`, `sleeptrain-1u8iv5l`, `sleeptrain-1u8mpfg`, `sleeptrain-1u8okpi`, `sleeptrain-1u8tqcn`, `sleeptrain-1u8vubz`, `sleeptrain-1u8zcg6`, `sleeptrain-1u95tzg`, `sleeptrain-1u970xk`, `sleeptrain-1u975v2`, `sleeptrain-1u97jcq`, `sleeptrain-1u99y0m`, `sleeptrain-1u9bvii`, `sleeptrain-1u9cylz`, `sleeptrain-1u9gnwk`, `sleeptrain-1u9grhe`, `sleeptrain-1u9ke9t`, `sleeptrain-1u9mx2q`, `sleeptrain-1u9n4s6`, `sleeptrain-1u9q3ni`, `sleeptrain-1u9sgmz`, `sleeptrain-1u9v78f`, `sleeptrain-1u9wdke`, `sleeptrain-1u9zrez`, `sleeptrain-1ua06y8`, `sleeptrain-1ua2hbt`, `sleeptrain-1ua87gp`, `sleeptrain-1ua95sp`, `sleeptrain-1uac4u0`, `sleeptrain-1uajjt3`, `sleeptrain-1uakm9m`, `sleeptrain-1uap89z`, `sleeptrain-1uaupd8`, `sleeptrain-1uavkhl`, `sleeptrain-1uavp4y`, `sleeptrain-1uaznp0`, `toddlers-1u5ugkh`, `toddlers-1u60zu4`, `toddlers-1u632iq`, `toddlers-1u6mmjr`, `toddlers-1u6nzi4`, `toddlers-1u75x5z`, `toddlers-1u8g8kd`, `toddlers-1u8y0gf`, `toddlers-1u921cy`, `toddlers-1u9om1o`, `toddlers-1uakv5s`.

### R63 — `sources/reddit-reading-r63.md`

**Subject-based whole-unit ledger references (3):** `NewParents-1ucy1td`, `NewParents-1ue2jln`, `beyondthebump-1uef292`.

**Subject-based passage ledger references (69):** `AttachmentParenting-1ucohpf`, `AttachmentParenting-1uda4jh`, `AttachmentParenting-1uenjs1`, `AttachmentParenting-1uep74s`, `Mommit-1uc6vok`, `Mommit-1uc9lgn`, `Mommit-1udx2yt`, `NewParents-1ub53cg`, `NewParents-1ubmcbq`, `NewParents-1ubnjat`, `NewParents-1uc3vff`, `NewParents-1uc55cw`, `NewParents-1ucp0o0`, `NewParents-1ud33b9`, `NewParents-1ud3slu`, `NewParents-1udk75h`, `NewParents-1uecmpk`, `NewParents-1ueo2es`, `Parenting-1ud2405`, `beyondthebump-1ubncva`, `beyondthebump-1uc04y0`, `beyondthebump-1uc23dh`, `beyondthebump-1uc8tus`, `beyondthebump-1uccijo`, `beyondthebump-1ud3veu`, `beyondthebump-1udjiy0`, `beyondthebump-1ue17x3`, `beyondthebump-1ue4rsf`, `beyondthebumpUK-1ubj588`, `daddit-1ub87o5`, `daddit-1uc3w0b`, `sleeptrain-1ub7z3j`, `sleeptrain-1ubam0s`, `sleeptrain-1ubba74`, `sleeptrain-1ubjo16`, `sleeptrain-1ubs7sm`, `sleeptrain-1ubt0vr`, `sleeptrain-1ubyi2i`, `sleeptrain-1ubzbef`, `sleeptrain-1uc8a03`, `sleeptrain-1ucb4yr`, `sleeptrain-1ucbpv0`, `sleeptrain-1ucermi`, `sleeptrain-1ucj67s`, `sleeptrain-1uckpt9`, `sleeptrain-1ucsqra`, `sleeptrain-1ud2yp9`, `sleeptrain-1ud36ub`, `sleeptrain-1ud3vb9`, `sleeptrain-1ud60xf`, `sleeptrain-1ud9o63`, `sleeptrain-1udcvi7`, `sleeptrain-1udfcpt`, `sleeptrain-1udqtlz`, `sleeptrain-1udzr7f`, `sleeptrain-1ue0i83`, `sleeptrain-1ue8hc6`, `sleeptrain-1ueax0d`, `sleeptrain-1uefpl6`, `sleeptrain-1ueg7qe`, `sleeptrain-1uepwjf`, `toddlers-1ub24mp`, `toddlers-1ub3dtt`, `toddlers-1ubh71u`, `toddlers-1uc6cur`, `toddlers-1ucho45`, `toddlers-1ud42ma`, `toddlers-1ue7cd9`, `toddlers-1uejx43`.

## Result

689 extracted quotes restored (31 already cited, 658 newly integrated), all original ids retained, and active restriction flags removed. The conclusions moved as recorded in the findings’ dated closing section. Missing whole units, replies and trimmed passages remain for the 7,122-row reading/review queue; their words were not re-created. All required checks passed; the remaining uncertainty concerns unmapped omissions, mixed triage reasons and log/note references as stated above.


## Re-reading complete — integrated 2026-11-17

UR01–UR24 completed **7,122/7,122** assigned omission/review reads: **6,213 rows** produced **8,772 verified quote records**, **909** produced no new quote with a ledger reason, **0** are missing or unfinished. All seven digest shares are reconciled into the relevant findings sections. Findings now cite **4,407 distinct ids**, including **2,757 complete UR quote fields**; all **1,650 earlier ids** remain. Every indexed money item (**436 ids**) and request/context item (**1,788 ids**) is retained in full (**2,065 distinct records** across the overlapping registers). All **602 outlier/gap-register ids** are also reproduced. These broad registers include proposed purchases, gifts, unpriced use and rhetorical questions; they are not counts of independent buyers or demand.

The **28 new thematic/provenance subsections** and the final “What the 2026-11-16 re-reading changed” section revise the opening philosophy/peer-trust claims, outcome definitions, schedule-first and duration assumptions, stopping guidance, feeding and treatment feasibility, adult recovery, fathers, usable handovers, shared-sleep goals, grief/adoption/reproductive decisions, accessibility/shelter, disclosure/police claims, money and source status. The free council programme corrects a universal price advantage over people; a received nanny refund corrects the surviving no-refund assertion. **32 older fragments** were aligned with literal source punctuation. Original source line breaks in the new quotations are displayed as spaces; words, case, spelling and punctuation remain exact.

The stock audit rebuilt **34,191 merged records** (**33,957 Reddit + 234 reviews**, **88 voice files**), with **0 active restrictions**, **689 historical labels** and **17 documented father-convention speaker relabels**. Its coverage measure concerns original unit paths, not the UR identity queue: **8,681/8,747** original paths now have a quote; **66** do not, all explained in reader ledgers. The **8,965 raw-file-path total** includes shared archive paths and review files. `counts.md` and `sources/reddit.md` reconcile those measures with **11,780 distinct identities read** (8,747 + 7,122 − 4,089 overlap).

**Still unread:** ordinary tier A **5,540**, B **27,352**, C **7,324** identities, outside the completed queue. The **1,641 safety-intake identities are all read**. Another **1,455** candidate bodies were removed/deleted at harvest and remain unavailable. Absent archived replies cannot be recreated. The original uncertainty about anonymous omission categories and mixed review reasons remains a provenance limit; it is no longer an unfinished assigned read. No clinical explanation, allegation, device claim, causal outcome or promotional intent was independently adjudicated. Broader-source/browser/ad-search gaps remain as recorded in findings §13.

Changed for this integration: `README.md`, `synthesis/findings.md`, `synthesis/counts.md`, `sources/reddit.md`, `synthesis/unfilter-report.md`, `voice-merged/all.jsonl`, and `synthesis/audit-safety-hits.tsv`. All **182 original voice/reader-ledger/digest file hashes** match the pre-integration snapshot; raw-file size/mtime checks and the historical spot-check worksheet are unchanged. No raw file, source quote, reader ledger, digest, other build or shared script was edited. No network or git was used.

### Integration checks (all exit 0)

Run from `mamivio.com/research/`:

```text
python3 -I _shared/_tools/verify_findings_ids.py sleep-baby/synthesis/findings.md sleep-baby
4407 distinct ids cited, 0 unresolved
4235 verbatim fragments paired with an id, 0 failed

python3 -I _shared/_tools/check_ids.py sleep-baby
34191 records, 34191 distinct ids, 0 duplicated

python3 -I _shared/_tools/audit_niche.py sleep-baby read-v1a read-v1b read-w2 read-w3 --check-only
{"quotes": 34191, "assigned": 8747, "units_quoted": 8965, "assigned_units_quoted": 8681, "uncited": 66, "unexplained": 0, "historically_marked": 689, "active_restrictions": 0, "safety_hits": 565}
```

The unchanged audit was also run in write mode to rebuild the merged copy, counts and descriptive hit table; the historical hand-check worksheet was restored byte-for-byte. The new hit count is not represented as a completed hand inspection or an eligibility rule.

Additional isolated checks used `/tmp/sleep_baby_verify.py` and `/tmp/sleep_baby_build_source_check.py`. The build’s `_tools/verify_quotes.py` ran unchanged with an in-memory JSONL decoder so archive serialization escapes are not mistaken for wording differences. A separate strict check restricts each UR quotation to its own decoded `post_id` or cited unit. No source or shared tool was changed.

```text
Strict UR source check: 8772 records, 8783 literal fragments in their own post/unit, 0 failed.
Build source verifier: TOTAL 34191 quotes, 0 failed.
Complete UR fields in findings: 2757, 0 failed (layout whitespace only).
Exact findings fragments: 4235, 0 failed (whitespace only; no quote-character normalization).
Citation preservation: 1650/1650; 4407 current ids; all resolve.
Digest-register coverage: 436/436 money; 1788/1788 request; 602/602 outlier/gap ids.
Merged integrity: 34191/34191 records preserved; only audit flags and 17 documented relabels; 0 active restrictions.
Protected integrity: 182 hashes unchanged; raw size/mtime checks and historical spot-check worksheet unchanged.
```
