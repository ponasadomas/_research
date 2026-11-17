from pathlib import Path
import json,hashlib,re,sys
from urllib.parse import urlsplit,parse_qs
from datetime import datetime
from zoneinfo import ZoneInfo
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent;W=R/'_raw/advertiser-map04-leave-registry';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
e=[]
def check(b,m):
 if not b:e.append(m)
a=rows(W/'access.jsonl');r=rows(W/'reading.jsonl');c=json.loads((W/'candidates.json').read_text());pol=rows(W/'policy-review.jsonl');ids=json.loads((W/'root-identity-source-check.json').read_text())
check(len(a)==len(r)==28 and len({x['url'] for x in a})==28,'exact28 responses/read statuses');check({x['url'] for x in a}=={x['url'] for x in r},'read URL set')
check(sum(x['status']=='full_saved_text_read' for x in r)==26,'26 complete saved text reads');check(len(c)==27 and len({x['name'] for x in c})==27,'27 unique brand candidates');check(len(pol)==24,'24 policy responses')
for x in a:
 check(H(R/x['html_file'])==x['html_sha256'],'native HTML hash '+x['slug']);check(H(R/x['text_file'])==x['text_sha256'],'text hash '+x['slug'])
 soup=BeautifulSoup((R/x['html_file']).read_bytes(),'html.parser')
 for n in soup(['script','style','noscript']):n.decompose()
 check(soup.get_text('\n',strip=True)+'\n'==(R/x['text_file']).read_text(),'full native extraction '+x['slug'])
 check(datetime.fromisoformat(x['captured_utc']).astimezone(ZoneInfo('Europe/Vilnius')).date().isoformat()=='2026-10-25','local observed date '+x['slug'])
 if x['slug']=='tilt-pricing':check(x['status']==403,'Tilt denial')
 else:check(x['status']==200,'page access '+x['slug'])
for x in pol:
 check(x.get('human_policy_read') is True and x.get('status')==200,'policy read/status '+x['url']);check(H(R/x['raw_file'])==x['sha256'],'policy raw hash '+x['url'])
requested={x['url'] for x in a};check(not any(urlsplit(u).hostname in ['strolleria.com','shop.safeintheseat.com','www.getohai.com'] for u in requested),'restricted/unverified storefront requests absent')
for x in c:
 check(x['accepted_price_or_sales_verified'] is False,'purchase boundary '+x['name']);check(x['offer_observed_date'] in ['2026-10-24','2026-10-25'],'offer date '+x['name'])
 for f in x['raw_files']:check((R/f).exists(),'source path '+x['name']+' '+f)
 if x.get('root_library_raw_file'):
  check(H(R/x['root_library_raw_file'])==x['root_library_raw_sha256'],'root source frozen at lookup '+x['name']);check('047-myregistry' not in x['root_library_raw_file'],'invalid047 excluded')
for x in ids:
 p=R/x['source_file'];o=json.loads(p.read_text());check(str(o['expected_page_id'])==x['library_page_id'],'root expected Page ID '+x['name']);check(H(p)==x['sha256'],'root source sha '+x['name'])
 v=o['browser_response']['content'][0]['text'];j=json.loads(re.search(r'```json\n([\s\S]*?)\n```',v).group(1));check(parse_qs(urlsplit(j['url']).query).get('view_all_page_id')==[x['library_page_id']],'native selected page URL '+x['name']);check(x['ad_bodies_read_by_this_reader']==0,'no ad body credit')
check(len(ids)==11,'11 root Page identities attached');master=next(x for x in c if x['name']=='Master Maternity Leave');check(master['candidate_numeric_page_id']=='106151438925030' and master['official_linked_profile_id']=='100085875948221','Master namespaces separated')
check(next(x for x in c if x['name']=='MyRegistry')['candidate_numeric_page_id'] is None,'MyRegistry remains unresolved, invalid047 unused')
check(next(x for x in c if x['name']=='Maple')['advertised_price'].find('no longer renew')>=0,'Maple sunset boundary')
check(not list((R/'voice').glob('advertiser-map04-leave-registry*')),'no new voice file')
p=R/'synthesis/reader-notes-advertiser-map04-leave-registry.md';s=p.read_text();check('getohai.com' in s and 'sunset Dec31,2026' in s,'contrary/identity evidence retained');check('**Direct parent-paid' in s and '**Employer buyers.' in s and '**Daily work-return' in s and '**Large registry/gear commerce' in s,'buyer/channel boundaries');check(not re.search(r'^> ',s,re.M),'no newly selected verbatim blocks')
for x in ids:check(x['library_page_id'] in s,'memo ID present '+x['name'])
# Exact source amounts/periods, checked against human-read native pages.
checks=[('master-blueprint','$997 USD'),('master-blueprint','$347 USD'),('nugget-membership','£29.99/year'),('nugget','£14.99'),('mindful-course','$499 US'),('starterset','$100'),('sits-consults','$29.99'),('sits-consults','$149'),('sits-course-store','$179.00 USD'),('myregistry-cash','Handling Fee'),('ohai-how','$9.99 per month'),('ohai-how','$19.99 per month'),('ohai-how','$29.99 per month'),('familywall-premium','$4.99/month'),('familywall-premium','$44.99 billed annually'),('cozi-plans','39'),('cozi-plans','79'),('skylight-calendar','$299.99'),('skylight-plus','$79'),('maple','December 31, 2026')]
for slug,text in checks:check(text in (W/'pages'/(slug+'.txt')).read_text(),'native price/period '+slug+' '+text)
report=dict(status='passed' if not e else 'failed',errors=e,counts=dict(candidates=27,new_source_HTTP_responses=28,complete_saved_HTML_text_reads=26,JS_shell_offer_not_read=1,HTTP403_original_unread=1,policy_documents_read=24,root_verified_Page_IDs_attached=11,root_library_sources_metadata_checked=11,new_voice_quotes=0,ad_bodies_read_by_this_reader=0),price_period_checks=len(checks),source_scope='Official permitted HTML text; no Chrome, accounts, forms or paid artifacts; seller claims not independently validated; reused Oct24 sources keep original dates',ads_provenance='Native result counts supplied by root; local check limited to expected Page IDs/selected URLs and hashes, not ad-body inventory, spend or outcomes',invalid_source_excluded='047-MyRegistry SPA race / preceding Busy Toddler',manual_findings='PDF vs live/course/app/hardware; parent vs employer buyer; cash/gear fees vs report fees; bare currency vs explicit USD; old sources vs current captures; Maple sunset and Ohai near-name identity reviewed',note_file=str(p.relative_to(R)))
(S/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));sys.exit(bool(e))
