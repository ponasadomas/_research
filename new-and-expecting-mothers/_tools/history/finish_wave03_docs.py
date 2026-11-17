#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];C=json.loads((R/'synthesis/counts.json').read_text());V=json.loads((R/'synthesis/coverage.json').read_text());D='_raw/audit/wave03-2026-10-24'
assert C['total']==2162 and V['all_reddit_full_original_post_ids_distinct']==6605
ledger='''| Source / finite scope | Downloaded or prepared | Matched / triaged | Kept | Fully read | New excerpts |
|---|---:|---:|---:|---:|---:|
| Canada/Australia/UK B cards | 847 cards | 847 | 584 | 584 posts | 117 |
| Main-archive payment censuses | 136 card occurrences | 136 | 27 occurrences | 26 distinct posts | 3 |
| Country duplicate inspections | 5 originals | 5 | 5 | 5 posts | 0 |
| Targeted historical native leads | 7 originals | 7 | 7 | 7 posts | 3 |
| Additional sleeptrain/parentsnark commercial archive | 15,226 window posts | 391 cards | 122 | 122 posts | 56 |
| CA/AU App Store review shelves | 8 pages / 80 reviews | 80 | 80 | 80 reviews | 22 |
| Root seller-offer extension | 9 requests | 8 valid full pages | 8 | 8 pages, including 2 reinspections | 6 |
| Report/registry buyer-source extension | 5 retained pages | 5 | 5 | 4 offers + 1 affiliate article | 7 |
| Final four seller follow-ups | 15 retained pages | 15 | 15 | 15 pages | 4 |
'''
(R/'synthesis/wave03-ledger-table.md').write_text(ledger)
report=f'''# Research session ledger — completed 2026-10-25

This finite pass completed the four owner-confirmed research tasks. It added **218 excerpts**, taking the database from1,944to**2,162**, with**2,162**distinct language-bank IDs and every record included. No product, pilot, outreach, accounts, purchases or advertising was performed. The ranked recommendation and buyer tables are research conclusions, with unresolved standalone-report demand.

## Exact new-wave ledger

{ledger}
Rows overlap: the two main payment packets contain one retained post twice and18previously read originals; only eight new main-archive IDs arise from their26distinct reads. The country duplicate inspections add five separately read IDs. New-wave Reddit reading is745occurrences/744distinct IDs, of which726are new versus the5,879baseline. Counts are post IDs, not people or independently authenticated customers.

Country cards:182Canada/385Australia/280UK →142/256/186full keeps. All847cards triaged,584keeps fully read,478eligible/106post-read exclusions,263card-drop bodies unread. The separate commercial extension has391cards →122full keeps (107eligible/15excluded),269card-drop bodies unread;14,697readable originals did not match. Both scopes have zero partial or unread keeps. Exact per-ID ownership/triage/full-read inventories are retained.

The new seller-source work also read22complete distinct seller-hosted testimonials, one seller-written process illustration, all17BSAFAQanswers and six Nesting FAQanswers; one external Facebook-review preview remains partial. These are separate from80original App Store reviews. Four original seller-discovery gaps were closed. Five already-known indexed leads now have complete archived original-post reads, but their important buyer-comment originals remain unavailable; no reply claim was upgraded to an original purchase.

## Cumulative coverage, recomputed from files

| Source | Captured / matched | Kept scope | Completed reading | Selected excerpts |
|---|---|---|---|---:|
| Main nine-community Reddit H2window |112,665posts /98,000readable |All A handled plus declared B/commercial scopes |6,476distinct posts +2,150OP +43exact other comments |1,066 |
| Additional two-community H2window |15,226posts /391commercial cards |122keeps |122posts; comments unavailable |56 |
| Historical native-ID lookups |7known leads |7readable originals |7posts; comments unavailable |3 |
| JustParents |505threads /505cards |94initial keeps |94full discussions /706posts |26 |
| MSE |343captured threads |343initial keeps |328full discussions /4,423posts;15partial safety boundaries |297 |
| GeoBaby |183captured threads |183 |183full discussions /1,422posts |111 |
| Parenting Q&A API |1,155questions /248cards |119 |119full saved threads /298answers /713comments |134 |
| Original app/book reviews |299available selected units |299 |284app +15book reviews |231 |
| Competitor/resource/hosted/affiliate material |55notes |73valid public offer/terms/pricing pages plus affiliate article |All retained pages complete; hosted proof separate |67 |
| Meta Ad Library |20queries /68retained IDs |68visible texts |Visible text only; videos/unloaded variants unclaimed |6 |
| Official guidance |11valid documents |11 |Bounded initial guidance reading |10 |
| Legacy search extracts |155records |Discovery only |No original full-read credit |155 |

**All Reddit sources combined:6,605distinct fully read post IDs.** Raw publication/license/authenticity and live completeness remain unverified. The main and additional H2window inventories are separate; seven targeted historical posts span2021–2024. Source-class totals sum to2,162selected records; these are not prevalence, payment rates, independent buyers or sales.

## Verification

Required exact-source result: `TOTAL 2162 quotes, 0 failed`. Current whole report is `{D}/whole-quote-verification.txt`. Strict competitor checks:55notes/55verbatim lines/0failures. Root's native audit covers all current new Reddit excerpts, full-read ledgers,22native Apple review records and43unchanged baseline voice/inventory hashes.

Human audit:23stratified random new-wave source-context checks plus20earlier root checks,31new safety hits reviewed and targeted checks of the five late-resolved historical originals. One payment classification was corrected: Premium access/annual-price rationale in rvw03-0006 does not explicitly establish a charge. Native wording/raw stayed unchanged. Three selected repeated-author groups and additional unquoted/related-account sequences were reviewed; earlier complaints and later improvement were kept together. Final audit files name every checked ID and unresolved source limitation.

## What remains unread or unavailable

- Main Reddit:2,531A /50,530B /38,463Creadable bodies unread;14,665unavailable. Exact lists `_raw/reddit-deep/wave03-v1/unread-A-post-ids.json`, `unread-B-post-ids.json`, `unread-C-post-ids.json`. Available comments unread145,386at `unread-available-comment-ids.json`; seven community comment files absent.
- Additional archive:14,966readable bodies unread (269card drops +14,697unmatched),138unavailable, both comment files absent. Exact lists `_raw/report-purchase-archive-wave03/final-v1/`. All391candidates were triaged and all122keeps fully read.
- Forums:411card-dropped JustParents discussions/2,766posts;231later MSE safety-tail posts deliberately unread. Exact boundary paths in `sources/not-harvested.md` and `_raw/oblique-deep/final-safety-unread-tails.jsonl`. Some historical GeoBaby original-question provenance remains uncertain.
- Q&A:129card-excluded and907unmatched questions, with original candidate paths `_raw/qa-deep/thread-index.jsonl` and `all-questions.jsonl`.
- Market/buyers: original app/book review histories and paid delivered artifacts uninspected. Eleven initial discovery leads still have an unresolved component, with five archived original posts now read but their buyer comments unavailable; one additional external review preview is partial. Exact current statuses `{D}/final-discovery-status.jsonl` and `_raw/offer-followups-wave03/`.
- Media/private: top200YouTube/videos/comments, private groups, social comment archives and owner customer data remain absent; access/policy reasons preserved. Named serious products from new buyer accounts, including Little Ones, Moms on Call and Blissful Baby Expert, do not yet all have current individual offer teardowns; observed historical use/payment is separate from current terms.

This is a completed bounded research wave, not global playbook completion. Next research priority is accessible independent post-use buyer evidence for a materially customized written deliverable and exact bundle/support boundaries. A bounded follow-up would use roughly one reader for three named offer teardowns plus two to four original-buyer reading chunks once permitted sources are identified; actual volume/access and cost are unknown. Broad remaining B/Creading needs a separately declared assignment. No product-building or outreach sequence is proposed.
'''
(R/'synthesis/session-report.md').write_text(report)
# Current source-map rows; retain the previous map in baseline snapshots.
p=R/'sources/source-map.md';s=p.read_text().replace('2026-10-24','2026-10-25',1)
s=s.replace('5,879 distinct full posts, 2,149 OP replies, 43 other comments cumulatively. All new 4,689 A keeps and 126 B comparison originals complete; 946 excerpts.','6,476 distinct full posts, 2,150 OP replies and43other comments; all847countrycards/584keeps complete, with1,066native excerpts in this main corpus.').replace('219 full original reviews read; 209 excerpts.','299full original app/book reviews read;231excerpts. Eight new CA/AUpages supply80complete original reviews.').replace('48 valid public page reads, 41 notes:','73valid public offer/pricing/terms page reads,55notes:')
s=s.replace('| Primary parenting forum sweep |','| Additional commercial Reddit archive | Two complete published files;15,226H2posts |391cards triaged;all122keeps fully read;56excerpts. Both comment sources absent | `report-purchase-archive-wave03.md`, `report-purchase-supplement-04.md`, `report-purchase-supplement-05.md` |\n| Historical buyer-lead lookups | Seven exact archived native post IDs,2021–2024 |All7original bodies read;3excerpts from2posts. Indexed buyer comments remain unavailable | `reddit-purchase-followups-wave03.md`, `reddit-index-leads-wave03.md` |\n| Primary parenting forum sweep |')
s=s.replace('`reviews-media.md`, `reviews-followups.md`, `market-deep.md`','`reviews-media.md`, `reviews-followups.md`, `market-deep.md`, `reviews-wave-03.md`').replace('`competitors.md`, `competitors-wave2.md`, `market-deep.md`, `../competitors/README.md`','`competitors.md`, `market-wave-03.md`, `report-buyers-wave03.md`, `offer-followups-wave03.md`, `../competitors/README.md`')
s=s.replace('Every eligible retained assignment is read.','Every retained assigned original in this wave is fully read, including post-read exclusions. Seller-hosted testimonials and affiliate access remain separate from independent buyer proof.')
p.write_text(s)
# Refresh the main-source current status while preserving the original collection narrative.
p=R/'sources/reddit-deep.md';s=p.read_text();a=s.index('**Current completed update');b=s.index('##',a)
s=s[:a]+'''**Current completed update — 2026-10-25:** main nine-community H2coverage is6,476distinct full posts,2,150identifiableOPreplies,43exactothercomments and1,066selected native excerpts. All847preparedcountryBcards and all584keeps are now complete;five additional duplicate originals and eight new IDs from root commercial reinspection are separately logged. Older Areading and comparison scopes remain complete. These are archived record counts, not independent people or transactions.

**Current unread main scope:**2,531A /50,530B /38,463Creadable bodies,14,665unavailable;145,386availablecomments unread and seven comment sources absent. Current exact inventories `_raw/reddit-deep/wave03-v1/`; older inventories remain frozen. Separate additional-community commercial reading adds122full posts, and targeted historical native-ID lookups add7, for6,605distinct archived posts globally. Those additions do not silently change main A/B/Cdenominators. [Session ledger](../synthesis/session-report.md).

The collection/handoff counts below describe earlier preparation snapshots; current reading completion comes from named per-ID ledgers and current inventories, not capture-time zero-progress fields.

'''+s[b:];p.write_text(s)
# New rows in competitor index, without rewriting historical source notes.
p=R/'competitors/README.md';s=p.read_text().replace('2026-10-24','2026-10-25',1).replace('41 individual notes (27 original, 7 first-solids follow-up, 7 report/registry follow-up).','55individual notes:41from the prior committed baseline and14new offer teardowns. There are73complete public offer/pricing/terms page reads; notes are not independent businesses or customer purchases.')
s+='''

## Current written-plan and service follow-ups

All retained public texts were read; full paid outputs and independent transactions were not. Prices below are advertised, dated observations with currency codes only when explicit. Service/bundle fees cannot be allocated to documents.

| New note | Advertised price | Format and proof limit |
|---|---|---|
|[BedtimeCoach](wave03-bedtimecoach.md)|$19one-off;optional$4.99monthly|Printable personalized PDF/log; seller explicitly new with no reviews/success count.|
|[Dawnly](wave03-dawnly.md)|$67one-off|Profile/playbook/fourteen-day PDF; seller-hosted proof, no inspected buyer.|
|[Sweet Siestas](wave03-sweetsiestas.md)|$225/$375/$525|Calls, personalized plan and support bundle.|
|[Nested Sleep](wave03-nested.md)|$649/$849/$1,399|Assessment, emailed PDF and continuing human support.|
|[Baby Sleep & Smile](wave03-babysleepandsmile.md)|Not displayed|English UAE written plan plus WhatsApp support.|
|[Riverbend Birth](wave03-pittsburgh.md)|$550/$850/$1,450|Even DIY includes intake/planning/support sessions plus PDF.|
|[Baby Sleep Answers](wave03-buyers-babysleepanswers.md)|$107/$177|Survey-routed videos/PDFs/community, current course bundle; historical testimonials not independent proof.|
|[By Hads](wave03-buyers-byhads-registry.md)|$350audit/$750curation|Feedback document plus review call; broader registry construction.|
|[Baby Chick](wave03-buyers-babychick-registry.md)|Not displayed|Questionnaire, consultation and written recommendations.|
|[The Baby Planner](wave03-buyers-babyplanner-registry.md)|Not displayed|Call, recording and notes; seller-hosted testimonials.|
|[Stress Less Mom](wave03-followup-stresslessmom.md)|Free review/call;premium unpriced|Free personalized alternatives plus concierge execution.|
|[The Village](wave03-followup-village.md)|$75room/$149home;registry fee absent|Photo-based written childproofing recommendations and follow-up; no independent buyer, physical inspection or qualification validation.|
|[Curated to Grow](wave03-followup-curatedtogrow.md)|Service fee absent|Individualized lists/consulting; gift-card amounts are not service prices.|
|[Nesting Notes](wave03-followup-nestingnotes.md)|Starting US$300/$400/$1,500|Registry documents inside consultation/refinement/support; deposit/full-booking wording preserved.|

Current MyMatLeave and Kinedu Assessment reinspections confirmed their public format/pricing; no extra quote or distinct-note credit. One stale sleep-offer lead returned404 and is not current verified pricing. Source ledgers: `../sources/market-wave-03.md`, `report-buyers-wave03.md`, `offer-followups-wave03.md`.
''';p.write_text(s)
# Global gaps retain all original denial history.
p=R/'sources/not-harvested.md';s=p.read_text();s+='''

## Current wave update — 2026-10-25

All847countrycards/584keeps and391additionalcommercialcards/122keeps are complete. Current unread IDs are in `_raw/reddit-deep/wave03-v1/` and `_raw/report-purchase-archive-wave03/final-v1/`. Nine of the eleven collected communities lack published comment files. Original-body lookup resolved seven historical leads, but indexed buyer replies remain unavailable; a post-body read does not verify its commenters. Current discovery statuses are `_raw/audit/wave03-2026-10-24/final-discovery-status.jsonl`.

Eighty new CA/AUoriginal reviews, fourteen offer notes and twenty-five new distinct seller pages close specified gaps. Four previously unretained serious seller leads are now complete. Seller-hosted testimonials and an affiliate article remain separate from independent buyers. One Village external-review preview is partial, with its full Facebook original outside the retained scope. Paid delivered artifacts, broad review histories, owner customers, current terms for newly named programs, media/private/social sources and the exact remaining source restrictions above remain gaps. No captcha, identity-switch, denied-route workaround, account, payment or contact was used.
''';p.write_text(s)
# Reader index carries every new written report, avoiding orphaned sub-agent conclusions.
p=R/'synthesis/reader-notes.md';s=p.read_text();s+='''

## Completed wave03 — 2026-10-25

Current ranking: [niche evidence](niche-opportunities.md); [purchase field audit](purchase-evidence.md). No product/pilot work. All assigned keeps complete; source counts are exact ledgers, not people or prevalence.

- Country readers [01](reader-notes-reddit-country-B-01.md), [02](reader-notes-reddit-country-B-02.md), [03](reader-notes-reddit-country-B-03.md):847cards/584full originals; [country/filter comparison](country-comparison-wave03.md).
- Root [commercial/review/offer notes](reader-notes-wave03-root.md):26distinct main-corpus reinspection posts,80new original reviews, current written-plan offers; seven historical lookups separately recorded.
- Commercial archive [03](reader-notes-report-purchase-archive-wave03.md), [04](reader-notes-report-purchase-supplement-04.md), [05](reader-notes-report-purchase-supplement-05.md):391cards/122full originals; paid plans/services, books/apps, prospective prices, gifts/trials and repeated authors separated.
- [Named buyer/registry-source extension](reader-notes-report-buyers-wave03.md):4offers,1affiliate article,18hosted testimonials; no independent report transaction.
- [Four remaining serious offers](reader-notes-offer-followups-wave03.md):15pages,4notes,free alternatives and photo-based written childproofing plan; seller-only proof and qualification limitations explicit.

The final human audit downgraded rvw03-0006 to Premium access with charge unconfirmed. Existing raw wording is unchanged, and apparent payment from access alone is not used as proof. Source-status snapshots remain frozen; current cumulative truth is [coverage](coverage.json) and [session ledger](session-report.md).
''';p.write_text(s)
# Add a qualitative positive/mixed case without treating clinical efficacy as proved.
p=R/'synthesis/success-stories.md';s=p.read_text();s+='''

## Wave03 use and outcome distinctions — 2026-10-25

| Account | What is reported | Limits |
|---|---|---|
| [rpa03-0013] | Bought general book; values digestibility and all-in-one organization despite free overlap | No customization/price; partial sleep chronology is not causal or durable efficacy. |
| [rcb02-0022] | Ordinary housework/cooking participation works for one twelve-month-old's household | Temperament/context differ; no purchased report or universal activity prescription. |
| [rpa04-0001] / [rpa04-0006] | Same archived account moves from consultant dissatisfaction to one better night | Dependent chronology, fee/written output unstated, no isolated consultant effect; retained as ordinary evidence. |

These are reported experiences, not a success rate or recommendation to build an offer.
''';p.write_text(s)
# Finish the state file; raw/voice snapshots are never rebuilt by this renderer.
(R/'synthesis/research-wave-03.md').write_text('''# Completed wave03 — 2026-10-25

All four owner-confirmed research tasks were pursued and this bounded pass is complete: actual purchase/deliverable field audit; whole-shortlist comparison; all847preparedcountrycards and584kept originals; competitor/review gaps and ranked support/contrary/unresolved recommendation. Research only, no product/pilot/outreach/accounts/payment.

Final source counts:2,162excerpts (218new),2,162language-bank IDs,zero subject exclusions;6,605distinct full archived Reddit posts,2,150OP/43othercomments;605full forum discussions,119Q&Athreads,299original reviews;55competitor notes/73publicoffer-term-pricingpages. Country584keeps and additionalcommercial122keeps all complete, no partial/unread keep. Seven targeted historical post reads are outside the H2windows. Report-only buyer proof remains unestablished in inspected scopes; actual plans/services and general information purchases are recorded in their categories.

Current main inventory `_raw/reddit-deep/wave03-v1/`; additional `_raw/report-purchase-archive-wave03/final-v1/`; all-global posts `_raw/audit/wave03-2026-10-24/all-reddit-full-post-ids-v2.json`. Older raw/voice inventories stay frozen. Baseline34voices+9inventories hash-protected, no old appenders/rebuilders rerun.

Audit folder `_raw/audit/wave03-2026-10-24/`:native-source/structural/word-budget/quote/competitor/context/safety/dependence/semantic-correction proofs. One root Premium-access payment inference was downgraded; raw/quote text unchanged. Current buyer/discovery source statuses distinguish archived original-post reads from unavailable buyer comments. Full unread and next research effort are in `session-report.md`; no global playbook completion claim.

Canonical conclusions: `findings.md`, `niche-opportunities.md`, `purchase-evidence.md`, `country-comparison-wave03.md`. Local commit is authorized by the owner's earlier instruction; no push. Unrelated first_command_research.md remains untouched. Any future source pass must use new capture/prefix/ownership files and finish every human keep; do not rerun frozen appenders or overwrite cited corpora.
''')
# Fix current README resume wording without changing historical baseline artifacts.
p=R/'README.md';s=p.read_text().replace("commit34ec30af's","commit `34ec30af`'s").replace('The baseline was committed as `2613feb3`; new continuation work follows it.','Prior baselines are commits `2613feb3` and `34ec30af`; current wave03 completion is recorded in the named source ledgers.').replace('The baseline is committed; unrelated workspace files remain unchanged.','Prior baseline artifacts are committed and frozen; unrelated workspace files remain unchanged.');p.write_text(s)
print({'documents_updated':10,'ledger_rows':9,'quotes':C['total'],'bank':C['language_bank_entries']})
