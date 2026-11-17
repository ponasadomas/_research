# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
import json,hashlib,collections,re
from pathlib import Path
R=Path(__file__).resolve().parents[2]
def rows(p):return [json.loads(s) for s in (R/p).read_text().splitlines() if s.strip()]
M=rows('_raw/oblique-deep/mse-completion-v2/batch-03/manifest.jsonl'); C=rows('_raw/oblique-deep/mse-completion-v2/batch-03/chunks.jsonl'); L=rows('sources/mse-completion-03-reading.jsonl'); Q=rows('voice/oblique-deep-05.jsonl'); md={x['thread_id']:x for x in M};ld={x['thread_id']:x for x in L}
full=[x for x in L if x['fully_read']];partial=[x for x in L if not x['fully_read']]
source='''# MSE retained completion — batch 03

Completed local reading on 2026-10-24. Exact frozen allocation: 104 whole discussions, 1,523 posts, 195 original pages, 33 packet chunks. No network, recapture, outreach, accounts, or global synthesis edits. The original pagination was already captured and remains immutable; capture completeness is separate from reading.

| Measure | Count |
|---|---:|
| Assigned threads | 104 |
| Fully read threads | 101 |
| Posts in fully read threads | 1,444 |
| Pages in fully read threads | 185 |
| Partial safety exclusions | 3 |
| Complete posts before exclusion boundaries | 18 |
| Boundary posts inspected for eligibility | 3 |
| Posts encountered including boundary inspection | 1,465 |
| Posts after safety boundaries deliberately unread | 58 |
| Excerpts retained | 53 |
| Distinct quoted threads | 40 |
| Excerpts eligible for ordinary practical research | 52 |
| Excerpt retained only to establish clinical boundary | 1 |
| Paid personalized-report purchases observed | 0 |

Every eligible whole thread was read through its final visible post, including OP follow-ups and `body_with_quotes`. Repeated earlier-post quotations were treated as context, not new voices. All 33 packet allocations were processed; three contain a safety boundary and are not represented as fully read packets. Native source post identifiers, author IDs, original timestamps and exact page/fragment URLs are preserved in the voice file. `raw_file` points to the frozen individual v2 unit, never the old quote-stripped v1 packets.

The structured ledger is `sources/mse-completion-03-reading.jsonl`. `posts_read` includes an inspected safety-boundary post, so it is not synonymous with complete read posts. `posts_fully_read` and `eligibility_posts_inspected` make that difference explicit. `post_read_eligible` is a Boolean eligibility flag, not a count or assertion that every passage is marketing material; `post_read_eligible_count` is separate. A fully read custody discussion is marked ineligible for selection, with no quotes. Incidental crisis, injury, loss or child-punishment passages in otherwise ordinary discussions are not selected.

## Scope ledger

The notes below describe the whole-thread reading, including unquoted discussions. They paraphrase, do not republish personal identifiers, and do not establish prevalence. Historical prices, benefits, legal interpretations, product specifications and safety advice are not present-day evidence or endorsed guidance.

| Thread | Status | Posts read / total | Fully read posts | Pages | Quote IDs |
|---|---|---:|---:|---:|---|
'''
for m in M:
 x=ld[m['thread_id']]; source+=f"| MSE{x['thread_id']} | {x['status']} | {x['posts_read']}/{x['posts_total']} | {x['posts_fully_read']} | {m['pages']} | {', '.join(x['quote_ids']) or '—'} |\n"
source+='\n## Whole-thread notes\n\n'
for m in M:
 x=ld[m['thread_id']];source+=f"- **MSE{x['thread_id']}** — {x['reader_note']}\n"
source+='''
## Exclusions and deliberately unread paths

No eligible assigned discussion remains unread. These safety remainders are deliberately excluded, not research backlog to mine for marketing:

'''
for x in partial:source+=f"- MSE{x['thread_id']}: stopped at `{x['safety_boundary_post_id']}` after {x['posts_read_before_boundary']} complete posts and one eligibility inspection; {x['posts_unread_after_boundary']} later posts unread. `{x['raw_file']}`. {x['reason']}\n"
source+='''
MSE5583868 was fully read (9 posts), then excluded from marketing selection as a child-centered custody dispute. It is not counted as a partial read. No excerpts from the three partial discussions or this fully read ineligible discussion were selected. The excluded opening and follow-up content is described only in neutral eligibility language.

## Vocabulary and limits

Speaker/stage/type values use the global README vocabulary. Identity remains `parent_unspecified` where the author did not identify as mother; an explicitly stated relative or partner role is retained. Uncertain pregnancy timing remains `unknown` rather than inferred from a due-month calculation. No diagnoses or credentials are inferred. New theme `maternity_budget` identifies leave-income, childcare-fee and benefits administration concerns distinct from food budgeting. No other new theme is introduced.

Gear, grocery delivery, paid classes and association membership are actual non-report spending categories. Proposed gifts, trial plans and unresolved searches are not purchases or results. Free forums, libraries, borrowing, retailer questionnaires, public groups, DIY and resale are substitutes. Existing current StarterSet personalized registry picks and Babylist free consultants remain competitive context supplied by the broader brief, not independently verified here. No claim of current free-service availability follows from these historical threads.

`odeep05-0023` is explicitly `marketing_eligible=false`, `evidence_use=clinical_boundary_only`: a later reported diagnosis changes the interpretation of a solids-refusal thread. It is retained to prevent a commercial reading that erases clinical referral; the source records a reported clinical finding rather than proving meal-plan success.

## Verification and continuation

Run `python3 mamivio.com/research/global/_tools/verify_quotes.py mamivio.com/research/global/voice/oblique-deep-05.jsonl` and `python3 mamivio.com/research/global/scratchpad/odeep05/audit.py`. The audit saves `sources/mse-completion-03-audit.json`, including hashes, exact ledger/manifest/chunk ID set checks, duplicates, all post metadata/body verification, cross-voice per-original-post 25-word aggregation, vocabulary, context limits, cited-ID lookup and scope counts. Source and voice files were never reused from an earlier reader; prefix is `odeep05-`.

Future collection or current rules/prices research would be a separate assignment. This completion does not claim the whole research playbook's global definition of done.
'''
(R/'sources/mse-completion-03.md').write_text(source)
notes='''# Reader notes — MSE retained completion 03

2026-10-24. Local frozen batch: 104 threads / 1,523 posts / 195 pages / 33 packets. 101 threads (1,444 posts, 185 pages) read fully; three precise safety exclusions. Eighteen additional posts fully read before boundaries, three boundary posts inspected, 58 later posts deliberately unread. Fifty-three selected excerpts from 40 threads are evidence selections, not counts of people or market prevalence. One includes a reported clinical finding and remains ordinary source evidence. There is no observed purchase of a personalized report and no Mamivio conversion evidence.

The interpretations below are grounded in the looked-up excerpt records and complete thread follow-ups. Source ledger contains the individual unquoted thread notes. All historical health, safety, legal, financial, benefits and product claims stay peer opinion, not current guidance. Brand prices here are past reported transactions, never current offers.

## Practical jobs and constraints

**Buying fewer unsuitable items, with the household's real constraints, is a plausible job.** A list request distinguishes needs from things to live without [odeep05-0006]. A buyer needed six shop visits before purchase [odeep05-0020]; another had to replace a used pushchair before birth because of boot fit [odeep05-0021]. A car also serves as pram storage because the flat and access alley are small [odeep05-0046]. The problem changes after purchase: losing car access and the bus route turns a beloved double into a painful uphill push [odeep05-0019]. This is context fit, not a universal gear ranking or proof someone would pay for written advice.

**Contrary evidence: premium and budget can both satisfy, and the answer can remain unknowable before use.** One parent regretted a bulky new travel system and poor resale recovery [odeep05-0027], but the sub-£300 city-system buyer explicitly reports satisfaction [odeep05-0052]. Whether removing wheels for a boot becomes annoying was still uncertain to the questioner before daily use [odeep05-0026]. The same wider discussion includes users who do not mind wheel removal. Recommending one model or telling everyone to wait is unsupported: a pregnant buyer became unable to shop or handle deliveries and valued early completion [odeep05-0050].

**Free tailoring and hands-on trials are strong competition.** A confused Google searcher declined the proposed cloth bundle after forum replies and planned library/sample trials [odeep05-0032]. A respondent says a retailer questionnaire helped even without a purchase there [odeep05-0033]. Another reports a local-council advisor explaining options/costs, with visit cost unstated [odeep05-0018]. Where a library was unavailable, the user bought small samples and resold disliked nappies [odeep05-0017]. These show interest in individual fit and competing routes to it; none shows payment for a report. Laundry's time cost competes with batch cooking and paid work, and the OP's child/material/nursery constraints defeat generic easy-wash advice [odeep05-0028].

## Food, feeding and care handoffs

**Household food planning extends beyond infant solids.** A parent of one- and three-year-olds already knows the web has countless recipes but wants meals other children actually accept [odeep05-0025]. Another actively collects free forum recipes into a notebook [odeep05-0005]. A parent about to have baby two bought a grocery delivery pass because shopping around would be difficult [odeep05-0031]. That is real payment to reduce physical shopping effort; saved money and payment for a meal plan are not demonstrated. Prepared lunches in the fridge were remembered as an especially valued birth gift [odeep05-0001].

**Feeding purchases have practical failure and satisfaction evidence.** Existing electric-pump use took a long time for modest reported output [odeep05-0009]; the OP later confirms a replacement and enthusiasm, without measured new output [odeep05-0010]. Antenatally fitted bras became too small and required another purchase [odeep05-0011]. An eight-/nine-month bottle user decided remaining use was too short to justify replacing equipment yet again [odeep05-0040]. A working parent had six rejected sippy cups while the child could drink from an ordinary cup [odeep05-0049]. These are gear-fit/time/remaining-lifespan issues; product physiology and safety explanations are not validated here.

**A separation deadline can turn familiar care into coordination work.** A work-trip deadline prompted a £15 bottle order after prior attempts [odeep05-0034]. The complete thread later showed expressed milk accepted from a bottle, formula still uncertain, and the trip canceled due to traffic; no successful formula transition should be inferred. A seven-week baby's mother tried an expressed-milk night handoff but still woke to express and leaked; she considered a different partner-settling arrangement, without later outcome [odeep05-0024]. Some human teaching is more useful than more equipment: a parent credits patient in-person instruction by a student midwife [odeep05-0016].

**Solids is not confirmed as the leading paid-report niche by these discussions.** The highchair regret concerns cleaning gear [odeep05-0007]; the OP's later highchair purchase is confirmed but not a feeding outcome [odeep05-0008]. The apparent solids-refusal problem later reached a reported GP diagnosis [odeep05-0023, clinical boundary only, not marketing eligible]. Reassurance, opposing peer methods and a book appeared before that finding; a shopping/preparation report must not be portrayed as solving the problem. The breakfast/cup case also involved good eating at other meals and deadline/guilt, not a demonstrated shortage of recipes [odeep05-0049].

## Information, time, support and comparison

**Some parents need permission to do less, or real help, rather than more suggestions.** A mother with a baby and toddler says she already knows and has tried the activity menu [odeep05-0029]. She values the friends made through classes but recalls becoming short of money, exhausted and stressed trying to keep up [odeep05-0030]. The full follow-ups include retained paid childcare and an aborted work-trip break. A routine book initially increased confidence [odeep05-0013], yet difficulties returned and free peer reassurance helped [odeep05-0014]. These are mixed trajectories, not book failure or sleep-success guarantees. An expecting second-time parent adopts basics and buying as needed after free replies [odeep05-0015].

**No village can mean operational questions, not just emotional labels.** The expectant poster asking where night changes actually happen confirms that books and a forum are their only baby-information contacts [odeep05-0036]. The source thread includes reassuring practical replies and ridicule; local human groups are suggested, not confirmed attended. Shared care should not be framed as the partner granting favors: a reply rejects that gift framing [odeep05-0022]. Meanwhile the gift-seeking partner plans entertainment for hospital/night feeding plus a keepsake [odeep05-0002], and another parent declines a proposed ring [odeep05-0003]. Gifts, care and report demand are distinct.

**Brand reassurance does not land uniformly.** A poster finds a formula ad patronizing [odeep05-0038], while a self-identified new mother likes it and expressly has not converted to formula [odeep05-0039]. The full thread also contains mistaken brand recall, so discussion/recall cannot establish sales effectiveness. This supports testing tone, not presuming that all mothers want generic praise.

## Income, administration and actual spending

**Leave/return decisions need household-specific sequence and assumptions.** HR can confirm the broad mechanism but leave the amount unclear in a close-second-pregnancy case [odeep05-0012]. A nursery-voucher user initially misunderstands take-home cost and only understands after several free replies [odeep05-0037]. Flexible work remains unanswered while the childminder needs booked days [odeep05-0043]. A father finds guidance mother-oriented and the employer policy missing [odeep05-0045]; contradictory eligibility replies in the full thread underline the need for qualified, current, country-specific verification. A higher-earner partner perceives a self-employment/support catch-22, but the numerical threshold assumption is unverified and may be mistaken [odeep05-0053]. These are researched needs, not validated financial guidance or paid-report willingness.

**Contrary evidence prevents a simple childcare-cost calculator conclusion.** One parent regrets saving for leave but not later childcare [odeep05-0035]. Another worked for a negative immediate return because nursery was valued in its own right [odeep05-0044]. Career continuity and child/family preference can outweigh short-term net income. The savings-site grandmother rejects another generic Google instruction after already searching [odeep05-0041]. A twin mother reports paying an association for discounts plus information/forum [odeep05-0042]; this is actual membership spending with bundled benefits, not report buying. Low income, debt or lost pay in other fully read threads are affordability problems, not evidence of willingness to spend on an informational product.

**Paid human services have a different value bundle.** A confident swimmer changes work hours for a teacher's lower-cost lessons, valuing expertise, commitment and social contact [odeep05-0047]. Another parent paid for baby swim classes attracted by an underwater photo but stopped because the child disliked the activity [odeep05-0048]. The full thread includes expensive satisfied long-term users, cheaper council substitutes, stopping for price and stopping for fear. None validates a DIY infant-swim report or the peer safety claims. Social costs can surprise even budget-conscious parents: the coffee invitation became a recurring expense, later replaced by visiting homes [odeep05-0051].

## Implications and limits

Candidate jobs to test are constrained gear/household preparation, family food logistics around a new arrival, and employer/childcare coordination. They remain hypotheses. A compact report would face free retailer tailoring, practical trials, libraries, peer groups and human services; current StarterSet registry personalization and Babylist free consultants are additional competition identified by the broader brief, not verified anew here. Nothing in this batch establishes a purchase, price test or conversion for a personalized report.

One hundred four assigned ID records reconcile exactly to the frozen manifest. Three discussions have deliberate safety remainders (MSE4250813, MSE5056453, MSE5869066); MSE5583868 was fully read but is ineligible for marketing selection. Their neutral boundaries and paths are in `sources/mse-completion-03-reading.jsonl` and `sources/mse-completion-03.md`. No eligible assigned original post remains unread. Captured pagination, repeated quoted context and selected excerpts never add independent voices. Broader research gaps remain outside this batch; this is not a global research-completion claim.
'''
(R/'synthesis/reader-notes-mse-completion-03.md').write_text(notes)
print('wrote source ledger and synthesis notes')
