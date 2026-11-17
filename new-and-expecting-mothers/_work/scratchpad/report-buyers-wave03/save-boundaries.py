import json
from pathlib import Path
S=Path(__file__).resolve().parent;W=S.parents[1]/'_raw/report-buyers-wave03'
def save(p,a):p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
policy=[
('www.babysleepanswers.com','public_original_allowed','robots200 wildcard empty Disallow; ordinary JavaScript rendering and FAQ expansion only.'),
('byhads.com','public_original_allowed','robots404 no robots rules; public registry page200.'),
('www.baby-chick.com','public_original_allowed','robots200 public service path allowed; restricted WordPress/search/transaction routes not used.'),
('thebabyplanner.co','public_original_allowed','robots200 empty body; public review page200.'),
('blundersinbabyland.com','public_original_allowed','robots200 public article path allowed; no admin/AJAX routes used.'),
('www.taylormadebabyco.com','not_fetched_policy_conflict','robots includes explicit GPTBot whole-site deny and later whole-site allow, plus content signals. Conservative exclusion under owner rule, no alternate user-agent/route.'),
('www.netmums.com','not_fetched_robots_http403','Robots request403; original older forum buyer account not requested or counted.'),
('www.reddit.com','not_fetched_saved_policy_deny','Existing saved robots wildcard Disallow:/; indexed comment leads are discovery only; no alternate live Reddit, proxy or archive route requested.'),
('strolleria.com','not_fetched_agent_identification_requirement','Public robots plus fully read agents.md require agent identification/Web Bot Auth for public HTML. No authorized identity mechanism available; review originals not requested; no account or workaround.'),
('thebigstuff.co','not_retained_discovery_policy_unresolved','Discovery excerpt only mentions following sleep accounts; robots requires agent identification and references agent requirements. Original article not retained/read, and no buyer evidence inferred.')]
save(W/'policy-review.jsonl',[dict(domain=d,decision=v,reason=r) for d,v,r in policy])
leads=[
('https://www.taylormadebabyco.com/about','not_fetched_policy_conflict','Specific assigned discovery URL; offer and retailer testimonials remain index-only, no independent paid registry-report buyer established.'),
('https://www.reddit.com/r/parentsnark/comments/1e9jsil/which_influencer_courses_have_you_bought/','not_fetched_policy_deny','Index suggests both nonuse and negative value accounts for personalized plan/course; whole originals/native comment attribution unavailable.'),
('https://www.reddit.com/r/sleeptrain/comments/1c9b66j/','not_fetched_policy_deny','Index suggests paid guide and approximate100-dollar recollection, but original comment, exact paid amount/currency and historical bundle cannot be checked.'),
('https://www.reddit.com/r/sleeptrain/comments/11t5pg8/','not_fetched_policy_deny','Index mentions course obtained and flexibility preference; got does not demonstrate payment and original unavailable.'),
('https://www.reddit.com/r/NewParents/comments/uc4o27/','not_fetched_policy_deny','Indexed BSA course use appears in comments, not original buyer record available here; no fresh read/quote credit.'),
('https://www.reddit.com/r/sleeptrain/comments/pdbazy/','not_fetched_policy_deny','Indexed low-price/free-content recommendation is not a completed transaction; original not read.'),
('https://www.netmums.com/coffeehouse/drop-clinic-984/sleep-988/383276-please-help-end-my-tether-co-sleeping-needs-stop-4.html','not_fetched_robots_http403','Index describes2010 book/forum bundle complaint; identity with present .com provider unestablished, no conflation or quotation.'),
('https://strolleria.com/','review_lead_not_fetched_agent_policy','Taylor discovery material points to retailer reviews, not independently established paid registry consulting; exact review native URLs unverified.'),
('https://thebigstuff.co/blogs/the-baby-files/baby-sleep','discovery_not_retained','Excerpt lists accounts followed; no inspected buyer claim, no new original reading credit.'),
('https://www.linkedin.com/posts/hadleyristvedt_i-raised-my-baby-registry-curation-prices-activity-7498363757715312640-CfKd','seller_discovery_only','Provider asserts price acceptance, not an independent buyer. Original not fetched, no price acceptance validated.'),
('https://www.stresslessmom.com/','seller_discovery_not_retained','Free review/concierge indexed lead, outside this retained named-offer extension; original and terms uninspected.'),
('https://thevillageparentcommunity.com/','seller_discovery_not_retained','Registry/childproofing service indexed lead; no independent buyer identified and original uninspected.'),
('https://www.curatedtogrow.com/home','seller_discovery_not_retained','Additional seller-hosted endorsement lead; original uninspected, no new purchaser proof.'),
('https://www.nestingnotesco.com/terms-of-service','seller_discovery_not_retained','Terms describe service payment process, not a buyer transaction. Original uninspected.'),
('https://pk.worldorgs.com/catalog/aurora/baby-store/buybuy-baby','republication_discovery_not_retained','Republished retail-review snippets concern registry shopping/customer service, not authenticated paid consulting/report purchases; original reviewer source unknown.')]
save(W/'unread-leads.jsonl',[dict(url=u,status=s,reason=r,original_fully_read=False,new_quote_selected=False) for u,s,r in leads])
queries=[
['"Baby Sleep Answers" "plan" review bought','"By Hads" registry review','"Baby Chick" "registry review" review paid','"Taylor Made Baby" registry review purchased'],
['"Baby Sleep Answers" review "bought" -site:babysleepanswers.com','"Baby Sleep Answers" "personalized" review -site:babysleepanswers.com','"By Hads" "registry" -site:byhads.com','"Baby Chick" "registry review" -site:baby-chick.com'],
['"Baby Sleep Answers" "review" -site:reddit.com -site:babysleepanswers.com -site:scribd.com','"baby registry audit" "paid" review','"Taylor" "Strolleria" "review" "Amanda"','"By Hads" registry review -site:byhads.com -site:linkedin.com'],
['"Baby Sleep Answers" "paid" "personalized" -site:babysleepanswers.com -site:scribd.com','"baby registry" "consultation" "paid" review -site:reddit.com -site:taylormadebabyco.com','"Baby Chick" "Registry" "bought" -site:baby-chick.com','"registry audit" "By Hads" review'],
['"paid for" "registry review" baby -site:babylist.com','"bought" "registry audit" baby','"baby registry consultant" "I paid" -site:linkedin.com','"Baby Sleep Answers" "purchased" review -site:babysleepanswers.com -site:reddit.com -site:scribd.com -site:pinterest.com']]
(W/'search-manifest.json').write_text(json.dumps(dict(date='2026-10-24',query_batches=[dict(batch=n,queries=q,raw_response=f'searches/discovery-{n:02d}.json') for n,q in enumerate(queries,1)],query_count=20,search_results_are_discovery_not_original_reads=True,display_truncation_note='One combined discovery response was truncated; no quote or full-original reading is based on that display. Every retained primary page/body and all expanded FAQs were displayed completely.'),ensure_ascii=False,indent=2)+'\n')
(W/'local-search-review.json').write_text(json.dumps(dict(scope='Nine saved H2 submission files, not a new download or all historical Reddit',search_pattern='Baby Sleep Answers / registry audit-review / named supplier lexical variants',matches=1,post_id='1n9mv2w',disposition='Not retained: title asks about baby-food chicken/turkey jars, a literal baby-chick false positive rather than the named service.',human_full_original_body_read=False,new_excerpt=False,root_owned_outside_window_reads=['1co3vfc','1fwzsfj'],root_reads_reused_only_as_context=True),indent=2)+'\n')
