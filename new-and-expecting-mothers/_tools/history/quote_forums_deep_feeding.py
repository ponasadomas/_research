#!/usr/bin/env python3
"""Fresh fdeep01 selection after complete retained Feeding read; exact-match validation."""
import collections,datetime,hashlib,json,pathlib,re,sys
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
from bs4 import BeautifulSoup
ROOT=pathlib.Path(__file__).resolve().parents[1]
SELECTIONS=[
('10762','91256','Can I ask what has made you think that I need to rest more and improve my diet?','objection',['generic_advice','work_transition','individual_constraints'],'Breastfeeding parent rejects unsolicited assumptions after describing return to12-hour day/night shifts and difficulty expressing.','breastfeeding_parent','baby_10_12_months'),
('9037','86358','buying some very pricey bottles that were suppose to mimic my nipple shape, and those proved to be a huge flop as well.','failed_solution',['bottle_transition','equipment_spending','caregiver_breaks'],'Respondent reports buying expensive bottles unsuccessfully; equipment purchase does not establish demand for reports.','breastfeeding_parent','multiple_children_past_experience'),
('4091','42600','yes I would be interested in buying ur pump off you','purchase_intent',['equipment_choice','price','compatibility'],'OP expresses interest after a seller offers a pump for£30, then asks about bottle compatibility; transaction remains unconfirmed.','parent_unspecified','unknown'),
('9629','86905','They are usually free or very cheap and can help you have a plan','alternative',['free_support','pregnancy_preparation','human_help'],'Respondent recommends feeding consultants, reports positive experience, and describes planning support; prices are a dated peer claim.','parent_unspecified','past_feeding_experience'),
('8593','81034','Just heard it bandied about a bit lately about this child led stuff.','counterevidence',['free_information','terminology','existing_method_satisfaction'],'After a freewebsite link, OP says current weaning already works and only wanted to understand the term.','parent_unspecified','baby_starting_solids_unspecified'),
('2967','32355','iv looked thru it no end of times but iv never done anything out of it','counterevidence',['book_nonuse','family_meals','convenience'],'Respondent owns an AnnabelKarmel book but uses own recipes or family meals; ownership does not confirm purchasing it.','parent_unspecified','baby_solids_unspecified'),
('4514','46178','Really starting to think about another career','counterevidence',['work_transition','structural_constraints','maternal_preferences'],'Expecting trainee nurse has work breaks but considers changing career because of time apart; planning information cannot resolve that preference.','expecting_parent','pregnancy_unspecified'),
('2170','23889','im worried i wont have the time.','pain',['siblings','time_constraints','feeding_preparation'],'Parent planning a fourth child fears breastfeeding will reduce time available for three existing children.','parent_unspecified','trying_for_additional_child'),
('1646','15084',"have been bombarded by lots of information regarding breastfeeding,it's a minefield with do's and don'ts.",'pain',['information_overload','pregnancy_preparation','conflicting_advice'],'First expecting parent at3months asks for lived experiences after too much feeding information.','expecting_parent','pregnancy_around_three_months'),
('3774','39497','i think some of these special breastfeeding bottles can be quite expencive.','objection',['price','basic_alternative','equipment_choice'],'Respondent reports basic bottles worked alongside breastfeeding and questions expensive specialist bottles; peer comparison, not a universal claim.','parent_unspecified','past_baby_feeding'),
('2432','27776','Thankyou for helping me with my decision.xxx','counterevidence',['free_peer_support','social_pressure','decision_resolution'],'OP credits freepeer responses for deciding to continue feeding after discouraging comments; no paid information request.','breastfeeding_parent','baby_10_months'),
]
def norm(s):return re.sub(r'\s+',' ',s).strip()
out=[];author_words=collections.Counter();fail=[]
for i,(tid,pid,q,typ,themes,ctx,speaker,stage) in enumerate(SELECTIONS,1):
    t=json.loads((ROOT/f'_raw/forums-deep/justparents/threads/{tid}.json').read_text());p=next(p for p in t['posts'] if p['post_id']==pid)
    n=len(q.split());author_words[p['author_handle']]+=n
    rawtext=BeautifulSoup((ROOT/p['raw_file']).read_bytes(),'html.parser').get_text(' ',strip=True)
    exact=q in p['body'] and norm(q) in norm(rawtext)
    if not exact or n>25:fail.append((tid,pid,n,exact))
    out.append({'id':f'fdeep01-{i:04}','source':'justparents-feeding','url':p['permalink'],'date':'','date_as_displayed':p['date_as_displayed'],'fetched_at':t['pages'][0]['fetched_at'],'speaker':speaker,'stage':stage,'type':typ,'themes':themes,'quote':q,'context':ctx.replace('12-hour','12 hour').replace('for£30','for £30').replace('freewebsite','free website').replace('AnnabelKarmel','Annabel Karmel').replace('at3months','at 3 months').replace('freepeer','free peer'),'raw_file':p['raw_file'],'raw_thread_json':f'_raw/forums-deep/justparents/threads/{tid}.json','source_class':'forum','evidence_kind':'original_thread_post','thread_id':t['thread_id'],'post_id':pid,'post_role':p['role'],'original_thread_read_in_full':True,'visible_pages_fetched':t['visible_pages_fetched'],'country':'unknown','community_market':'UK','paid_report_demand_proven':False,'quote_words':n})
if any(n>25 for n in author_words.values()):fail.append(('author_word_limit',dict(author_words)))
assert not fail,fail
dest=ROOT/'voice/forums-deep-01.jsonl'
payload=''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in out)
if dest.exists() and dest.read_text()!=payload:raise RuntimeError('Fresh wave exists; do not overwrite/reappend.')
dest.write_text(payload)
report={'file':str(dest.relative_to(ROOT)),'quotes':len(out),'failed':0,'max_quote_words':max(x['quote_words'] for x in out),'author_aggregate_word_max':max(author_words.values()),'checks':['exact post-body substring','normalized raw HTML text match','<=25words perpost','<=25words aggregate perauthor in thiswave','complete retained thread read']}
(ROOT/'synthesis/forums-deep-01-quote-verification.json').write_text(json.dumps(report,indent=2))
print(report)
