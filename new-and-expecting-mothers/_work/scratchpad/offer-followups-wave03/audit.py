# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
from pathlib import Path
import json,hashlib,re,subprocess,sys,html
from urllib.parse import urlsplit
from collections import defaultdict,Counter
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent;W=R/'_raw/offer-followups-wave03'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def lines(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
def norm(s):return re.sub(r'\s+',' ',html.unescape(s)).strip()
def canon(u):
 s=urlsplit(u);return s.hostname.removeprefix('www.')+(s.path.rstrip('/') or '/')
e=[]
def check(x,msg):
 if not x:e.append(msg)
q=lines(R/'voice/offer-followups-wave03.jsonl');rd=lines(R/'sources/offer-followups-wave03-reading.jsonl');acc=lines(W/'access.jsonl');lead=lines(W/'lead-status.jsonl');pol=lines(W/'policy-review.jsonl');test=lines(W/'testimonial-reading.jsonl')
allowed={'www.stresslessmom.com','thevillageparentcommunity.com','www.curatedtogrow.com','www.nestingnotesco.com'}
expected={
'https://www.stresslessmom.com/','https://www.stresslessmom.com/pregnancy-services','https://www.stresslessmom.com/postpartum-services','https://www.stresslessmom.com/vipregnancy',
'https://thevillageparentcommunity.com/','https://thevillageparentcommunity.com/registry-concierge','https://thevillageparentcommunity.com/virtual-baby-proofing','https://thevillageparentcommunity.com/in-home-services-1',
'https://www.curatedtogrow.com/home','https://www.curatedtogrow.com/copy-of-services',
'https://www.nestingnotesco.com/','https://www.nestingnotesco.com/services','https://www.nestingnotesco.com/how-it-works','https://www.nestingnotesco.com/faqs','https://www.nestingnotesco.com/terms-of-service'}
check({x['url'] for x in rd}==expected and len(rd)==15,'reading exact15 URL set');check({x['url'] for x in acc}==expected and len(acc)==15,'access exact15 URL set')
for x in acc:
 check(x['status']==200,'access status '+x['url']);check(urlsplit(x['url']).hostname in allowed and urlsplit(x['final_url']).hostname in allowed,'bounded domains')
 check(H(R/x['raw_file'])==x['raw_sha256'],'HTML hash '+x['url']);check(H(R/x['text_file'])==x['text_sha256'],'text hash '+x['url'])
 soup=BeautifulSoup((R/x['raw_file']).read_bytes(),'html.parser')
 for n in soup(['script','style','noscript']):n.decompose()
 check(soup.get_text('\n',strip=True)+'\n'==(R/x['text_file']).read_text(),'complete extraction from native HTML '+x['url'])
for x in rd:
 check(x['complete_extracted_public_text_read'] and x['complete_rendered_public_text_read'],'full reading status '+x['url'])
 check(H(R/x['rendered_file'])==x['rendered_sha256'],'render hash '+x['url'])
 o=json.loads((R/x['rendered_file']).read_text());check(canon(o['url'])==canon(x['url']),'rendered URL '+x['url'])
for x in pol:
 check(x['status']==200 and x['human_policy_read_complete'] and x['checked_before_offer_request'],'policy status')
 check(H(R/x['raw_file'])==x['sha256'],'policy immutable hash')
check(len(pol)==4 and len(lead)==4,'four policy/lead count')
old=R/'_raw/report-buyers-wave03/unread-leads.jsonl'
for x in lead:check(H(old)==x['prior_file_sha256'],'prior frozen lead file unchanged')
faq=json.loads((W/'pages/nesting-faqs-expanded.json').read_text());check(faq['faq_count']==6 and len(faq['steps'])==6,'FAQ6 controls')
original=(W/'pages/nesting-faqs.txt').read_text()
questions=[x['question'] for x in faq['steps']]
for i,x in enumerate(faq['steps']):
 check(x['expanded']=='true','FAQ actually opened '+x['question'])
 part=original.split(x['question'],1)[1].split(questions[i+1] if i<5 else "Let's Get Nesting!",1)[0].strip()
 check(norm(part) in norm(x['body']),'complete FAQ answer in native browser capture '+x['question'])
for x in test:
 check(x['complete_visible_testimonial_read'] and not x['independent_buyer'],'testimonial proof classification')
 check(H(R/x['raw_file'])==x['sha256'],'testimonial immutable hash')
 o=json.loads((R/x['raw_file']).read_text());body=(R/o['origin_page_file']).read_text()[o['origin_body_start']:o['origin_body_end']]
 check(body==o['body'] and len(body)>100,'native full testimonial offsets')
check(len(test)==4,'complete hosted testimonial4')
preview=lines(W/'unread-review.jsonl');check(len(preview)==1 and preview[0]['original_review_fully_read'] is False and preview[0]['new_quote_selected'] is False,'preview not full review')
other=[]
for p in (R/'voice').glob('*.jsonl'):
 if p.name!='offer-followups-wave03.jsonl':other+=lines(p)
check(len(q)==4 and len({x['id'] for x in q})==4,'four unique quote ids');check(not({x['id'] for x in q}&{x['id'] for x in other}),'global unique IDs')
works={canon(x['url']):x for x in q}
prior=[x for x in other if canon(x['url']) in works]
check(not prior,'existing source-work quote overlap')
manual=[]
for x in q:
 check(len(x['context'].split())<=25,'context25 '+x['id'])
 check(x['speaker']=='advisor' and x['stage']=='unknown' and x['type']=='advice_given','vocabulary '+x['id'])
 check(x['date']=='' and x['observed_date']=='2026-10-24','unknown publication / observed date '+x['id'])
 check(x['source_class']=='competitor' and x['evidence_kind']=='seller_claim','proof labels '+x['id'])
 row=next(z for z in rd if z['text_file']==x['raw_file']);check(canon(row['url'])==canon(x['url']),'native page attribution '+x['id'])
 check(norm(x['quote']) in norm((R/row['text_file']).read_text()),'quote in native HTML extraction '+x['id'])
 check(norm(x['quote']) in norm(json.loads((R/row['rendered_file']).read_text())['body']),'quote in browser body '+x['id'])
 hits=re.findall(r'\b(?:safety|medical|clinical|feeding|therapy|occupational|diagnos\w*|kill\w*|death|abuse|minor|panic\w*|suicid\w*)\b',x['quote']+' '+x['context'],re.I)
 manual.append(dict(id=x['id'],full_source_context_review=True,role_date_url_review=True,no_personal_names_or_usernames_selected=True,regex_hits=hits,decision='Research-only seller description; no safety, clinical, accepted-price, qualification or efficacy validation.'))
(S/'manual-quote-review.json').write_text(json.dumps(manual,indent=2)+'\n')
notes=sorted((R/'competitors').glob('wave03-followup-*.md'));check(len(notes)==4,'four unique competitor notes')
budgets=defaultdict(int)
for x in q+prior:budgets[canon(x['url'])]+=len(x['quote'].split())
for p in notes:
 s=p.read_text();mechanism=re.search(r'Mechanism: \*\*(.+?)\*\*',s).group(1);check(len(mechanism.split())<=8,'mechanism<=8 '+p.name)
 check('Raw: `' in s and 'Interpretation:' in s and 'Observed 2026-10-24' in s,'required note fields '+p.name)
 for b in re.findall(r'^> (.+)$',s,re.M):
  matches=[x for x in q if norm(x['quote'])==norm(b)];check(len(matches)==1,'verified blockquote '+p.name)
  if matches:budgets[canon(matches[0]['url'])]+=len(b.split())
for work,n in budgets.items():check(n<=25,'per-original aggregate quote25 '+work+' '+str(n))
refs=[]
for p in notes+[R/'sources/offer-followups-wave03.md',R/'synthesis/reader-notes-offer-followups-wave03.md']:
 ids=re.findall(r'ofw03-\d{4}',p.read_text());check(set(ids)<={x['id'] for x in q},'note ID lookup '+p.name);refs.append(dict(file=str(p.relative_to(R)),distinct_ids=len(set(ids)),mentions=len(ids)))
ver=(R/'_tools/verify_quotes.py').read_text().replace('ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")','ROOT = str(__import__("pathlib").Path(__file__).resolve().parents[2])')
(S/'verify_quotes.py').write_text(ver)
run=subprocess.run([sys.executable,str(S/'verify_quotes.py'),str(R/'voice/offer-followups-wave03.jsonl')],text=True,capture_output=True)
(S/'strict-verification.txt').write_text(run.stdout+run.stderr);check(run.returncode==0,'copied strict verifier')
report=dict(status='passed' if not e else 'failed',errors=e,counts=dict(domains=4,robots_read=4,retained_pages=15,full_public_pages=15,partial_retained_pages=0,unread_retained_pages=0,faq_answers_individually_expanded_read=6,complete_seller_hosted_testimonials=4,seller_process_illustrations=1,truncated_widget_previews_not_original_reads=1,new_competitor_notes=4,quotes=4,all_quotes_research_only=True,relevant_access_denials=0,independent_original_buyers=0,standalone_customized_report_transactions_established=0),per_original_quoted_words_including_note_repeats=dict(budgets),prior_work_quote_overlap=[x['id'] for x in prior],manual_full_context_checks=4,note_id_checks=refs,strict_verifier=run.stdout.strip(),source_limits='Seller offers/hosted testimonials/illustration only; external widget original and account/form/payment/output routes uninspected; earlier other11 leads untouched.')
(R/'sources/offer-followups-wave03-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));sys.exit(bool(e))
