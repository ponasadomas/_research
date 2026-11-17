# July country B reader01 — complete assigned coverage

Completed 2026-10-24. The owner’s four research tasks remain open globally; this finite reader assignment is complete. All topics were eligible for manual consideration. No product, prototype, advertising, outreach, new capture, account, payment, delegation or commit was performed.

The immutable parent packet contains **847 July 2025 B candidates** from BabyBumpsCanada, BabyBumpsandBeyondAu and BeyondTheBumpUK. Exact assignment: [`batch-01.json`](../_raw/reddit-deep/next-july-country-B-v1/primary-v1/assignments/batch-01.json), four original card chunks, **292 cards**. The assigned IDs are disjoint from the authoritative frozen **5,879 full original post IDs** in [`continuation-v1/final-read-post-ids.json`](../_raw/reddit-deep/continuation-v1/final-read-post-ids.json), key `full_original_post_ids`. The older `reddit-deep/final-*` inventory is historical and was not used as the current baseline. The frozen 1,944 quotes were checked from commit `34ec30af`; old sources, quote files and appenders were left unchanged.

| Step | Canada | Australia | UK | Total |
|---|---:|---:|---:|---:|
| Assigned cards, all personally triaged | 111 | 109 | 72 | 292 |
| Keeps, all personally read in full | 93 | 80 | 51 | 224 |
| Card drops, bodies not human-read | 18 | 29 | 21 | 68 |

Manual triage retained 49 registry, 45 pumping/work, 38 other, 33 pregnancy, 28 sleep, 23 postpartum, seven play and one solids cards. These are bookkeeping categories, not independent needs, market proportions or niche rankings. Every kept title and whole body was read; **184 remained eligible and 40 were excluded after full reading**. There are **zero partial originals, zero unread keeps, zero additional human-read originals and zero additional comments**. The complete reading ledger includes the 40 exclusions rather than silently removing them from coverage.

All 292 cards were displayed in 12 frozen complete-card views below 15 KB. All 224 keeps were frozen into 16 whole-unit views below 25 KB before extraction. One complete view was displayed per tool call; no truncated output was accepted as a read. Individual immutable units, rather than these display views or cards, are the cited `raw_file` sources. The new file contains **31 excerpts from 31 original post IDs**; there was no extraction quota. These counts describe selected evidence, not independent buyers or prevalence.

## Source and missing material

The publisher dataset is `yikeee/reddit-subreddits25`, pinned to archive commit `ea497c510aa68765c07ed744ec9f84d68bbedf7f`. Native submission files already existed under `_raw/reddit-deep/windows/2025-h2-v1/`; individual units and metadata are frozen under [`primary-v1`](../_raw/reddit-deep/next-july-country-B-v1/primary-v1/). The capture is historical, July 2025 within an H2 archive window ending exclusively 2026-01-01. No live page, external link, image or article was opened. Publisher provenance, license, rights, authenticity, real identities and live completeness remain unverified.

**Country comment files are unavailable for all three communities.** Zero saved identifiable OP replies means missing comment sources, not that the live posts had no replies. No complete-thread or complete-live-followup claim is made. The ledger uses `post_body_read_complete=true`, `available_identifiable_OP_replies_read=0` and `op_reply_ids_read=[]`; each quote uses `read_scope=full_post_comment_source_unavailable`.

The 68 card-drop bodies remain unread by a human, even though the audit mechanically compares their frozen native title/body metadata. Unassigned cards and the parent packet’s other readers are outside this completion claim. Later outcomes, followups, accepted offers, refunds, external product reviews and live purchases remain unavailable unless explicitly described in the saved original.

## Boundaries, buying and dependence

Card drops have specific reasons in the TSV. Post-read exclusions have neutral reasons in the reading ledger. They cover clinical treatment or diagnostic interpretation, active medical risk, loss, sensitive relationship/safeguarding situations and unsafe infant sleep or equipment reassurance. Ordinary worry, figurative fatigue, past therapy or diagnosis, resolved NICU history and positive/free alternatives were not automatically excluded. `eligible` describes this research ledger’s practical evidence status, not an automatic marketing clearance.

Eight excerpts are explicitly research-only with `marketing_eligible=false` and `evidence_use`: `rcb01-0003`, `0010`, `0014`, `0016`, `0017`, `0019`, `0024`, `0028` (all use the full `rcb01-` prefix). They retain administrative, developmental-belief or service-capacity evidence without supplying clinical, financial, legal or safety advice. No excerpt was selected from any of the 40 post-read exclusions. Author roles come from the actual original: two expecting-mother, three new-mother, three partner and 23 conservative parent-unspecified records. Pregnancy or a spouse reference alone did not supply gender.

No completed paid customized-report transaction was found in the 224 originals. Physical gear orders/purchases, human childcare payments, professional care fees, quoted prices, app consideration, advice requests and free workarounds remain distinct. Detailed distinctions and contrary evidence appear in the [reader notes](../synthesis/reader-notes-reddit-country-B-01.md). Neither willingness to buy gear nor a prospective fee establishes a report’s accepted price.

Eight exact-body flag groups touch the assignment. All were reviewed against saved native body, author and date metadata, and the frozen baseline. Every group has one shared saved author label and one body after whitespace collapse; this establishes dependent archive accounts, not authenticated people or fraud. Five groups touch kept originals and three touch card drops. No excerpt was minted from any flagged group. Counterparts received machine comparison only, not additional human full-read credit. Two further explicit semantic sequences were grouped: the workplace followup `1m85bdn` → `1m96cgn`, and corrected-province repost `1mck70c` → `1mck87w`. Repeated saved author labels across the full-read set are recorded as dependence, without an independent buyer total.

## Files and verification

- [Per-ID triage](../_raw/reddit-deep/triage/country-B-01.tsv): all 292 cards, original card file and explicit decision.
- [Per-ID reading](reddit-country-B-01-reading.jsonl): all 224 keeps, whole-body flag, missing-comment scope, immutable unit hash, final status, reason and quote IDs.
- [Voice](../voice/reddit-country-B-01.jsonl): fresh prefix `rcb01-0001` through `rcb01-0031`.
- [Scratch and frozen manifests](../scratchpad/reddit-country-B-01/): new helpers, 12 card views and 16 full-body views, progress checkpoints.
- [Duplicate review](../scratchpad/reddit-country-B-01/duplicate-review.json), [author dependence](../scratchpad/reddit-country-B-01/native-author-dependence.json), [frozen baseline check](../scratchpad/reddit-country-B-01/baseline-dedup-check.json) and [native quote audit](../scratchpad/reddit-country-B-01/native-quote-audit.json).
- [Strict verification](reddit-country-B-01-verification.json): exact assignment/triage/keep/read ID sets, card/view/unit hashes, all 292 native title/body/date/permalink comparisons, 31 native-selftext quotations, schema/vocabulary/context, own-ID global uniqueness and looked-up reader-note IDs. Mechanical comparison of card-drop bodies does not change human reading counts.

Reproduce with `python3 mamivio.com/research/global/scratchpad/reddit-country-B-01/verify.py`. The separate required `_tools/verify_quotes.py` check is also run on this own voice file. Both must finish with zero failures; final hashes are in the verification record.

The final [own prefreeze correction log](../scratchpad/reddit-country-B-01/audit-corrections.json) makes two conservative metadata adjustments without changing quote wording: “born last month” does not establish a six-week age bracket, and an administrative workaround with no fee mentioned does not prove zero cost.

## Added themes

These tags describe the saved evidence, not established market segments or efficacy. Related words are intentionally explicit enough to distinguish payment from consideration and consumer needs from unverified clinical explanations.

| Meaning | Tags |
|---|---|
| Reported physical acquisition and fit | `actual_gear_order`, `actual_gear_purchase`, `after_purchase_friction`, `registry_gear`, `pumping_equipment`, `feeding_equipment`, `compatibility`, `functional_fit`, `comfort_fit`, `material_fit`, `failed_product`, `multipurpose_fit`, `space_constraints` |
| Price, reuse and consumption choices | `budget_constraint`, `gear_price_objection`, `shipping_cost`, `secondhand`, `secondhand_tradeoff`, `frugal_alternative`, `preconception_budgeting`, `consumption_objection`, `registry_opt_out`, `pumping_opt_out`, `feeding_preference`, `tracking_burden` |
| Actual human service versus quoted deliverable | `actual_human_help_payment`, `qualified_human_help`, `service_deliverable`, `price_opacity`, `childcare_administration`, `payroll_navigation` |
| Work, benefits and care availability | `work_return_economics`, `work_return_planning`, `partner_work_return`, `benefit_administration`, `benefit_comparison`, `benefit_timing`, `repeat_paperwork`, `childcare_selection`, `childcare_availability`, `childcare_capacity`, `childcare_waitlist`, `service_cancellation`, `work_from_home_conflict`, `shared_night_care` |
| Navigation and practical preparation | `service_navigation`, `service_access`, `identity_verification`, `administrative_workaround`, `beginner_orientation`, `partner_preparation`, `books`, `newborn_workflows`, `household_routine_request`, `preparation_gap`, `routine_request`, `practical_guidance`, `generic_advice_objection`, `multiple_children`, `clothing_decision`, `context_gap`, `context_specific_need`, `information_gap`, `decision_criteria`, `peer_experience`, `family_advice_pressure`, `research_time`, `trust` |
| Reviews and uncertain purchase trust | `buyer_review_gap`, `real_use_evidence`, `marketing_skepticism`, `advertising_skepticism`, `purchase_hesitation` |
| Sleep, existing success and explanatory beliefs | `sleep_advice_conflict`, `anticipatory_worry`, `current_success`, `existing_guide_success`, `sleep_change`, `sleep_counterevidence`, `routine_flexibility`, `reported_uncontrolled_success`, `development_framework`, `unverified_causal_belief` |
