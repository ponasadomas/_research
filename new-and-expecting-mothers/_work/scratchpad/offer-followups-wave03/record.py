# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[2];W=R/'_raw/offer-followups-wave03';S=Path(__file__).parent
assert not (S/'freeze-manifest.json').exists(), 'Frozen task; do not rerun record writer'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,a):p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
access=[json.loads(l) for l in (W/'access.jsonl').read_text().splitlines()]
rows=[]
for x in access:
 slug=Path(x['text_file']).stem;p=W/'pages'/f'{slug}-rendered.json';o=json.loads(p.read_text())
 rows.append(dict(work_id='ofw03-page-'+slug,url=x['url'],final_url=x['final_url'],raw_file=x['raw_file'],raw_html_sha256=x['raw_sha256'],text_file=x['text_file'],text_sha256=x['text_sha256'],rendered_file=str(p.relative_to(R)),rendered_sha256=H(p),complete_extracted_public_text_read=True,complete_rendered_public_text_read=True,source_control='seller_controlled_offer_or_terms',faq_scope='All six answers opened individually, captured and fully read' if slug=='nesting-faqs' else 'No FAQ accordion questions in retained text',observed_date='2026-10-24',publication_date='',independent_buyer=False,paid_standalone_report_purchase_established=False))
save(R/'sources/offer-followups-wave03-reading.jsonl',rows)
policies=[]
for x in [json.loads(l) for l in (W/'policy-access.jsonl').read_text().splitlines()]:
 f=R/('_raw/offer-followups-wave03/policies/'+Path(x['raw_file']).name)
 policies.append(dict(url=x['url'],raw_file=str(f.relative_to(R)),sha256=H(f),status=x['status'],human_policy_read_complete=True,decision='Relevant public offer routes permitted; no explicit AI denial in saved robots. Avoid prohibited lightbox query and disallowed partial/gallery routes on Wix sites; Village /404 disallowed.',checked_before_offer_request=True))
save(W/'policy-review.jsonl',policies)
# Native testimonial units: complete saved seller-hosted body, not independent reviewer accounts.
test=[];U=W/'testimonial-units';U.mkdir(exist_ok=True)
cur=(W/'pages/curated-home.txt').read_text()
items=[('curated-devan','Devan K.','Honestly she’s an amazing resource', 'Help through two babies; product-function perspective', 'Help used; no service payment, price or output artifact stated'),('curated-miriam','Miriam S.', 'I would have been totally lost', 'Registry overload and distrust of paid review sites','Help used; no service payment, price or delivered document stated'),('curated-alex','Alex B.', 'I connected with Sarah', 'Newborn preparation sessions with partner','Gear investment claimed; service payment not stated')]
for slug,author,start,trigger,claim in items:
 at=cur.index(start);qchar='"' if slug=='curated-devan' else '”';end=cur.index(qchar,at)
 body=cur[at:end];p=U/(slug+'.json');assert not p.exists();obj=dict(work_id='ofw03-testimonial-'+slug,source_url='https://www.curatedtogrow.com/home',author=author,date='',body=body,origin_page_file='_raw/offer-followups-wave03/pages/curated-home.txt',origin_body_start=at,origin_body_end=end);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');test.append(dict(work_id=obj['work_id'],raw_file=str(p.relative_to(R)),sha256=H(p),author=author,date='',complete_visible_testimonial_read=True,source_control='seller_hosted_testimonial',trigger=trigger,payment_claim=claim,independent_buyer=False,price=None,refund=None,standalone_written_report_purchase_established=False))
nest=(W/'pages/nesting-home.txt').read_text();at=nest.index('As a pediatrician, I felt');end=nest.index('"',at);body=nest[at:end]
p=U/'nesting-kiona.json';assert not p.exists();obj=dict(work_id='ofw03-testimonial-nesting-kiona',source_url='https://www.nestingnotesco.com/',author='Kiona - Chicago, IL',date='',body=body,origin_page_file='_raw/offer-followups-wave03/pages/nesting-home.txt',origin_body_start=at,origin_body_end=end);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');test.append(dict(work_id=obj['work_id'],raw_file=str(p.relative_to(R)),sha256=H(p),author=obj['author'],date='',complete_visible_testimonial_read=True,source_control='seller_hosted_testimonial',trigger='Busy first-parent gear decisions, lifestyle prioritization',payment_claim='Service use claimed; payment and price unstated',independent_buyer=False,price=None,refund=None,standalone_written_report_purchase_established=False,qualification_claim='Pediatrician self-description unverified'))
save(W/'testimonial-reading.jsonl',test)
save(W/'illustration-reading.jsonl',[dict(work_id='ofw03-nesting-process-illustration',url='https://www.nestingnotesco.com/how-it-works',raw_file='_raw/offer-followups-wave03/pages/nesting-process.txt',complete_public_narrative_read=True,source_control='seller_written_process_illustration',claimed_deposit='50% service-bundle deposit',client_authenticity='Unknown whether real clients, anonymized example or fictional illustration; not independently corroborated',independent_buyer=False,standalone_written_report_purchase_established=False)])
save(W/'unread-review.jsonl',[dict(url='https://facebook.com/104277479266731/reviews',discovered_at='https://thevillageparentcommunity.com/',raw_file='_raw/offer-followups-wave03/pages/village-home-rendered.json',status='truncated_seller_embedded_preview_only',native_author='Debi Martin',displayed_date='1/12/2026',date_normalized='',date_reason='Locale ambiguous display retained; original not inspected',preview_read_complete=True,original_review_fully_read=False,new_quote_selected=False,reason='Read-full-review and View-All-Reviews lead to Facebook, outside four-domain scope; not followed; no independent buyer/full-review credit.')])
old=R/'_raw/report-buyers-wave03/unread-leads.jsonl';oldrows=[json.loads(l) for l in old.read_text().splitlines()]
leads=[]
for x in oldrows:
 if x['url'] not in ['https://www.stresslessmom.com/','https://thevillageparentcommunity.com/','https://www.curatedtogrow.com/home','https://www.nestingnotesco.com/terms-of-service']:continue
 domain=x['url'].split('/')[2]; pages=[z['url'] for z in rows if z['url'].split('/')[2]==domain]
 leads.append(dict(url=x['url'],prior_status=x['status'],prior_status_file='_raw/report-buyers-wave03/unread-leads.jsonl',prior_file_sha256=H(old),status='complete_bounded_public_offer_followup',retained_full_page_urls=pages,retained_pages_read=len(pages),access_denial=False,independent_original_buyer_established=False,remaining_scope='No forms, contact, account, booking, paid output, off-domain original review or broader domain discovery.'))
save(W/'lead-status.jsonl',leads)
selected=[
('stresslessmom-home','Stress Less Mom','Let Our Experts Review Your Baby Registry for Free',['birth_preparation','free_alternatives','personalization'],'Seller offers free registry review beside premium concierge services; free personalized pregnancy plan involves a call. No delivered document or independent buyer inspected.'),
('village-babyproofing','The Village Parent Community','Personalized Written Safety Plan',['personalization','birth_preparation','price_value'],'Seller advertises photo-based written recommendations plus follow-up at $75/$149; no accepted payment, independent buyer, professional safety validation or inspected output established.'),
('curated-services','Curated to Grow','Individualized Toy and Gift Lists',['floor_play','personalization','birth_preparation'],'OT and parent-coaching seller lists individualized lists alongside registry, feeding and play services; prices shown are gift-card amounts, with no report purchase established.'),
('nesting-services','Nesting Notes Co.','Draft registry assembled  with Nesting Notes and delivered',['birth_preparation','personalization','price_value'],'Seller bundles registry drafts and notes with consultations, refinement and ongoing support; advertised service prices are not independently accepted report-only fees.')]
quotes=[]
for i,(slug,author,quote,themes,context) in enumerate(selected,1):
 x=next(z for z in rows if z['work_id']=='ofw03-page-'+slug)
 quotes.append(dict(id=f'ofw03-{i:04}',source=author+' — public seller offer',url=x['url'],date='',observed_date='2026-10-24',author=author,speaker='advisor',stage='unknown',type='advice_given',themes=themes,quote=quote,context=context,raw_file=x['text_file'],source_class='competitor',evidence_kind='seller_claim',work_id=x['work_id'],independent_buyer=False,standalone_customized_report_purchase_established=False))
save(R/'voice/offer-followups-wave03.jsonl',quotes)
print(json.dumps(dict(pages=len(rows),policies=len(policies),complete_testimonials=len(test),truncated_previews=1,seller_process_illustrations=1,quotes=len(quotes),lead_statuses=len(leads)),indent=2))
