# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
from pathlib import Path
import json,gzip,hashlib
from collections import defaultdict
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent
m=json.loads((S/'full-manifest.json').read_text());wanted={x['post_id'] for x in m['keeps']};native={}
for p in (R/'_raw/report-purchase-archive-wave03/window').glob('*.gz'):
 with gzip.open(p,'rt') as f:
  for l in f:
   n=json.loads(l)
   if n['id'] in wanted:native[n['id']]=n
# Human-selected excerpts only, after all 15 complete originals and full assigned card triage.
selections=[
('1mjy4lb','failure_story','baby_6_12_months','parent_unspecified',['personalization','sleep_training_values','conflicting_advice'],
'we are working with a sleep consultant for the past 2 weeks but honestly it’s not getting better and she is against sleep training',
'Initial consultant dissatisfaction; same archived author later reports improvement. Service payment, written output and fee are unstated.'),
('1mkirw4','objection','baby_6_12_months','parent_unspecified',['price_value','free_alternatives'],
"I'm hoping there's something glaringly obvious I'm missing here that can help her sleep because I'm just at a loss and the thought of spending thousands on a sleep consultant is a hard pill to swallow.",
'Prospective consultant fee objection and community help request; no purchase, exact fee, currency or report format established.'),
('1mv70zf','objection','baby_6_12_months','experienced_mother',['price_value','household_support'],
'If I had the money we’d be spending it on a sleep consultant.',
'Expresses need for human help and insufficient funds; no accepted price or completed transaction.'),
('1n2ffio','tried_failed','unknown','parent_unspecified',['price_value','personalization','free_alternatives'],
'Ideally a consultant who offers hands on support and not one who sells an e-book and responds to a few of your emails. […] I’ve spent upwards of $1000 of sleep training at this point from buying multiple sleep books, 3 different sleep courses, and working with a sleep consultant for 2 weeks who turned out to be awful…',
'Reports aggregate spending across books, courses and consultant; prefers hands-on assistance. Currency code and separate fees unknown; repeated-author dependence flagged.'),
('1n8cxd4','belief','toddler','professional',['daycare_handoff','personalization'],
'There’s too much nuance in these situations for me to feel comfortable communicating about them via text or email. I really feel like it’s important to talk and then send recap emails.',
'Self-described daycare provider supplements a phone discussion with written recap; no standalone report price or purchase. Credentials and licensing assertions unverified.'),
('1n9334h','success_story','baby_6_12_months','parent_unspecified',['household_support','sleep_routines'],
'Last night we got ourselves a 9 hours stretch, something we couldn’t possibly dream of a month ago.',
'Later same-author consultant account reports one improved night after family support and gradual changes; payment and written format unstated, causal efficacy unverified.'),
('1njban5','objection','toddler','experienced_mother',['price_value','personalization','daycare_handoff'],
"With the service we're looking at, we would have 2 weeks of daily check ins/touch points, schedule help and adjustments and support.",
'Considering daily human support and a separately mentioned $39 guide; neither purchased. Feeding-readiness uncertainty is part of the source context, not verified care guidance.'),
('1nokc85','tried_failed','baby_6_12_months','parent_unspecified',['personalization','free_alternatives'],
"but I chatGPT'd these based on todays naps.",
'Used AI for calculations from actual nap inputs and still asks community for clarification; payment, model and output accuracy unknown.'),
('1noqk43','trigger_moment','baby_6_12_months','parent_unspecified',['price_value','free_alternatives'],
'Hi Everyone! I am having a sleep consultant come on Friday, but before I spend $$$$ just wanted to see if something is glaring.',
'Scheduled consultant visit motivates a final community check; prospective symbolic cost, no completed payment or written deliverable.'),
('1o0hc4b','failure_story','toddler','parent_unspecified',['price_value','skepticism'],
'I spent $600 for no changes in my newly 1 year olds naps.',
'Reports consultant spending and no nap improvement; fee belongs to service, with currency code, written output, intake and refund unstated.'),
('1o1qp4z','objection','toddler','parent_unspecified',['price_value','sleep_training_values'],
'I was recommended TCB but I can’t pay $150 for videos lol.',
'Rejects quoted video price while seeking another approach; historical stated price, currency code unknown, no payment or report preference established.'),
('1oejemy','objection','baby_6_12_months','new_mother',['skepticism','free_alternatives'],
'I was thinking about getting a sleep consultant but I read how many of them are just scams.',
'Consultant trust objection after DIY attempts; perception from prior reading, no verified fraud claim or purchase.'),
('1ofia69','success_story','baby_6_12_months','parent_unspecified',['personalization','sleep_routines'],
'Just finished 4 weeks with a sleep consultant for my 7-month-old. Overall things are so much better (she used to wake every hour 😩), but we still can’t fix the false start — she wakes 45–60 mins after bedtime every night.',
'Four-week consultant program has reported improvement and a persistent problem; payment, fee and written format unstated, clinical efficacy unverified.')]
rows=[]
for i,(id,typ,stage,speaker,themes,quote,context) in enumerate(selections,1):
 n=native[id];k=next(k for k in m['keeps'] if k['post_id']==id)
 rows.append(dict(id=f'rpa04-{i:04}',source='Reddit r/sleeptrain — additional commercial archive',url='https://www.reddit.com'+n['permalink'],date=k['date'],author=n['author'],speaker=speaker,stage=stage,type=typ,themes=themes,quote=quote,context=context,raw_file=k['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset=k['archive_dataset'],archive_commit=k['archive_commit'],post_id=id,read_scope='full_post_comment_source_unavailable',paid_customized_report_purchase_proven=False))
(R/'voice/report-purchase-supplement-04.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
(S/'selections.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
annotations={
'1mjy4lb':('eligible','service_used_payment_unstated','Two-week consultant dissatisfied; ordinary fatigue and sadness without explicit acute danger. Retain only research service evidence; later same-author improvement linked.',dict(trigger='Repeated night wakes; information overload; consultant against training',deliverable='Two weeks human consultant; written artifact and intake unstated',price=None,personalization='Routine described to community; actual consultant intake/output absent',outcome='No improvement at this date',later_same_author_post='1n9334h')),
'1mkirw4':('eligible','prospective_fee_objection','No completed payment. Ordinary sleep concern; no clinical instruction selected.',dict(trigger='Persistent false starts after several methods',deliverable='Potential consultant; no artifact described',price='thousands, no exact amount/currency',personalization='None described',outcome='No purchase or consultant outcome stated')),
'1mv70zf':('eligible','unaffordable_prospective_service','Need and affordability separated. Historical vomiting stopped method; no health recommendation or acute danger inferred.',dict(trigger='Split nights; pregnancy and limited partner help',deliverable='Desired human consultant',price=None,personalization='Unstated',outcome='Cannot afford desired consultant; no payment')),
'1mvgzud':('eligible','service_used_payment_unstated','Corrected age and ongoing nap concerns; retain service-format account only, no validated sleep assessment or quote selected.',dict(trigger='Short naps and apparent tiredness',deliverable='Two-week consultant schedule',price=None,personalization='Schedule supplied; intake and written format unstated',outcome='Night sleep good; naps still short and parent doubts advice')),
'1n2ffio':('eligible','explicit_aggregate_spend_books_courses_consultant','Research-only commercial evidence. Unsuccessful infant plan and distress retained as source evidence; same-author safety-excluded later account prevents independence inference.',dict(trigger='Persistent night wakes despite multiple solutions',deliverable='Several books, three courses, two-week human consultant; wants hands-on virtual service',price='upwards of $1000 aggregate; currency code absent',personalization='Prior plan reported, output format/intake unstated; seeks individual attention',outcome='Prior consultant described negatively; no refund or resolution',same_author_other_assignment_ids=['1mclz85','1n6hnju'])),
'1n8cxd4':('eligible','written_plan_bundled_with_daycare_not_sale','Research-only format comparison. Self-described provider, licensing and feeding claims unverified; no clinical instruction or standalone purchase claimed.',dict(trigger='Daycare transition mismatch in feeding/naps',deliverable='Phone meeting; emailed mutually agreed home plan; proposed recap phone/email',price=None,personalization='Family-specific care history and agreed actions',outcome='Parents report plan not resolving naps; provider wants another call')),
'1n9334h':('eligible','hired_consultant_fee_unstated','Same native author as initial complaint; one account over time. Outcome self-report and no efficacy/safe-sleep claims endorsed.',dict(trigger='Failed chair method during extended disruption',deliverable='Human consultant; family support and gradual method, written format unstated',price=None,personalization='Rest-first family coaching; intake artifact absent',outcome='Reports calmer family and one nine-hour stretch',earlier_same_author_post='1mjy4lb')),
'1njban5':('eligible','prospective_service_and_guide_not_purchased','Research-only comparison of human support and guide; infant-feeding readiness/weaning choice retained as source evidence.',dict(trigger='Two night feeds; questions marginal value after extensive reading',deliverable='Considering two-week daily contact/schedule support and separate Hey Sleepy Baby weaning guide',price='$39 guide considered; currency code absent; consultant fee absent',personalization='Expected schedule help; parent questions need, daycare constrains routine',outcome='Question only; no payment, use, refund or outcome')),
'1nokc85':('eligible','ai_use_payment_unstated','Ordinary arithmetic and uncertainty, not validated advice. Do not infer free tier or medically safe output.',dict(trigger='Confusion about wake-hour and nap totals',deliverable='ChatGPT wake-window calculations based on naps',price=None,personalization='Todays naps used as inputs',outcome='Still asks community how totals work; correctness unknown')),
'1noqk43':('eligible','scheduled_consultant_payment_not_completed','Ordinary routine uncertainty; pending fee not accepted payment.',dict(trigger='Upcoming consultant visit; inconsistent mornings and false starts',deliverable='Consultant coming Friday; written format unstated',price='$$$$ symbolic prospective cost; not numerical/currency',personalization='Actual visit/intake/output unknown',outcome='Community check before spending; no completed payment')),
'1o0hc4b':('eligible','explicit_consultant_spend','Service fee and no nap improvement are reported; no clinical inference, guarantee or standalone written plan inferred.',dict(trigger='Short naps and perceived child tiredness',deliverable='Sleep consultant, details unspecified',price='$600 service spend, currency code absent',personalization='Intake and output unspecified',outcome='No nap improvement; refund not stated')),
'1o1qp4z':('eligible','video_price_rejection_no_purchase','Historical video price objection; seeking non-CIO approach, no safe-sleep claim endorsed.',dict(trigger='Contact naps and crib distress at one year',deliverable='Recommended TCB videos; not purchased',price='$150 rejected; currency code absent',personalization='Not described',outcome='Cannot pay; community request')),
'1o22qg2':('read_pending_topic_review','hired_consultant_fee_unstated_clinical_context','Full original read. Clinical investigation and prolonged distress remain attributed evidence; review ordinary topic fit without subject exclusions.',dict(trigger='Prolonged toddler sleep concerns with clinical consultations',deliverable='Historical hired consultant and later behavioral provider; written output unstated',price=None,personalization='Prior-attempt history discussed; written assessment absent',outcome='Earlier partial improvement without total-hour increase; current concern unresolved')),
'1oejemy':('eligible','consultant_trust_objection_no_purchase','Ordinary fatigue idiom does not establish self-harm. Keep only research perception of trust; no verified fraud allegation.',dict(trigger='DIY gentle approach inconsistent at night',deliverable='Potential consultant; no artifact',price=None,personalization='No consultant use',outcome='Trust objection; no purchase')),
'1ofia69':('eligible','service_used_payment_unstated','Mixed outcome retained. No safe/optimal schedule or efficacy inference; quote is service self-report only.',dict(trigger='Hourly wakes before program',deliverable='Four-week consultant program and significant schedule change',price=None,personalization='Schedule adjusted to child; no intake or written artifact shown',outcome='Much better overall, persistent false starts and longer crying after program; no refund stated')),
}
ledger=[]
for k in m['keeps']:
 id=k['post_id'];status,classification,reason,transaction=annotations[id]
 n=native[id]
 ledger.append(dict(post_id=id,raw_file=k['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=0,op_reply_ids_read=[],primary_unit_sha256=k['sha256'],native_body_sha256=k['native_body_sha256'],native_author_sha256=k['native_author_sha256'],native_author=n['author'],date=k['date'],url=k['url'],status=status,reason=reason,quote_ids=[q['id'] for q in rows if q['post_id']==id],purchase_classification=classification,transaction=transaction,standalone_customized_written_report_purchase_proven=False,comment_source_available=False,comment_source_status='publisher_comment_file_unavailable',read_scope='full_post_comment_source_unavailable',affiliation='No disclosure in retained original; independence and authenticity unverified'))
(R/'sources/report-purchase-supplement-04-reading.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in ledger))
print('ledger',len(ledger),'quotes',len(rows),'eligible',sum(x['status']=='eligible' for x in ledger),'excluded',sum(x['status']=='excluded_after_read' for x in ledger))
