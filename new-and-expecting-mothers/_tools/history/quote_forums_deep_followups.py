#!/usr/bin/env python3
"""Fresh fdeep02 after every retained followup post/page has been read."""
import collections,json,pathlib,re,sys
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
from bs4 import BeautifulSoup
ROOT=pathlib.Path(__file__).resolve().parents[1]
S=[
('9382','84512',"What's the best way to prepare for the new baby coming",'desire',['siblings','postpartum_preparation','parent_attention'],'Parent at35weeks plans attention for2.5year and10month siblings when another baby arrives.','expecting_parent','pregnancy_35_weeks'),
('9791','85529',"speak to someone who knows  what they're talking about face to face",'alternative',['information_overload','human_support','pregnancy_events'],'First expecting parent overwhelmed online seeks knowledgeable face-to-face support; event affiliation is not verified.','expecting_parent','pregnancy_unspecified'),
('9894','86577',"I just remember that I didn't need any of it.",'counterevidence',['packing','minimalism','free_checklists'],'Respondent needed few packed items; other parents in this same free checklist thread forgot personal belongings.','parent_unspecified','past_birth_experience'),
('8027','77246',"I'm worried that i will get there and realised i have forgotten something",'pain',['first_trip','packing','family_visit'],'Parent packing for first weekend visit with7week baby gets a free simple-checklist suggestion.','parent_unspecified','baby_7_weeks'),
('707','5697',"We live in a flat, so don't have a garden",'constraint',['home_space','transport','activities'],'Parent of2year child also lacks car; holiday groups close and nearby softplay does not fit child.','parent_unspecified','toddler_2_years_adjacent'),
('1307','11656','anything i can do with my baby that wont cost me more than a tenner ?','objection',['activity_budget','free_alternatives','local_activities'],'Parent seeks baby outings below£10; this is an activity budget, not willingness to buy a report.','parent_unspecified','baby_unspecified'),
('8660','81385','childcare would make my pay worthless.','constraint',['childcare_cost','work_load','structural_limit'],'Parent works after children sleep; childcare cost makes extra work unattractive. A report cannot supply care hours.','parent_unspecified','children_ages_unknown'),
('9889','86343','my husband tends to think that I sit at home all day and do nothing','pain',['household_recognition','work_boundaries','caregiver_coordination'],'Respondent with young baby describes partner assumptions while seeking home work; no report request.','parent_unspecified','baby_unspecified'),
('12170','93743','what kitchen blender is better for blending baby puree until completely smooth?','question',['first_solids','puree_method','equipment_choice'],'Parent asks about smooth-puree equipment; first solids cannot be assumed to mean BLW. No purchase confirmed.','parent_unspecified','baby_solids_unspecified'),
('10012','87053','My hubby has actually taken my daughter out for some daddy daughter time this morning','solution',['hands_on_help','maternal_rest','partner_tasks'],'After peer reassurance, OP gets time to nap while partner takes child on errands; no paid plan.','parent_unspecified','young_child_unspecified'),
('9172','83699','i may struggle with amount of time i need to prepare all of his food at home.','constraint',['food_preparation','household_diet','first_solids'],'Parent considering vegan child diet worries about preparation time. Quote conveys workload, not diet safety or nutritional adequacy.','parent_unspecified','planning_baby_diet'),
('5903','58108','considered the cost of buying them in the first place','objection',['upfront_cost','laundry_work','product_tradeoffs'],'Respondent rejects reusable nappies over initial cost and washing; OP later reports ordering a full-time pack.','parent_unspecified','pregnancy_unspecified'),
('4216','43418','I have tried vanish, oxi crystals and other no brand stuff and nothings working.','failed_solution',['solids_mess','cleaning','household_work'],'Parent tried cleaning products on baby-food stains without success; problem is cleanup rather than selecting another recipe.','parent_unspecified','baby_solids_unspecified'),
('2726','30079','not sure what sauces he can have.','question',['first_solids','food_choices','free_recipes'],'Parent of7month child bought baby pasta but needs sauce/sandwich ideas; free peer recipes and books are suggested.','parent_unspecified','baby_7_months'),
('9952','86797','The flight was not too bad.','counterevidence',['first_trip','free_peer_help','positive_outcome'],'OP returns during holiday after a mostly manageable first flight; free reassurance helped, no paid report mentioned.','parent_unspecified','baby_1_year'),
]
def norm(s):return re.sub(r'\s+',' ',s).strip()
counts=collections.Counter();out=[];fail=[]
def post(tid,pid):
    t=json.loads((ROOT/f'_raw/forums-deep/justparents/threads/{tid}.json').read_text());return t,next(p for p in t['posts'] if p['post_id']==pid)
for line in (ROOT/'voice/forums-deep-01.jsonl').read_text().splitlines():
    q=json.loads(line);t,p=post(q['thread_id'][3:],q['post_id']);counts[p['author_handle'].lower()]+=len(q['quote'].split())
for i,(tid,pid,q,typ,themes,context,speaker,stage) in enumerate(S,1):
    t,p=post(tid,pid);raw=BeautifulSoup((ROOT/p['raw_file']).read_bytes(),'html.parser').get_text(' ',strip=True)
    context=context.replace('at35weeks','at 35 weeks').replace('for2.5year and10month','for 2.5 year and 10 month').replace('with7week','with 7 week').replace('of2year','of 2 year').replace('below£10','below £10').replace('of7month','of 7 month')
    wc=len(q.split());counts[p['author_handle'].lower()]+=wc
    if q not in p['body'] or norm(q) not in norm(raw) or wc>25 or len(context.split())>25:fail.append((tid,pid,wc,len(context.split())))
    out.append({'id':f'fdeep02-{i:04}','source':'justparents-followups','url':p['permalink'],'date':'','date_as_displayed':p['date_as_displayed'],'fetched_at':t['pages'][0]['fetched_at'],'speaker':speaker,'stage':stage,'type':typ,'themes':themes,'quote':q,'context':context,'raw_file':p['raw_file'],'raw_thread_json':f'_raw/forums-deep/justparents/threads/{tid}.json','source_class':'forum','evidence_kind':'original_thread_post','thread_id':t['thread_id'],'post_id':pid,'post_role':p['role'],'original_thread_read_in_full':True,'visible_pages_fetched':t['visible_pages_fetched'],'country':'unknown','community_market':'UK','paid_report_demand_proven':False,'quote_words':wc})
if any(n>25 for n in counts.values()):fail.append(('cross_wave_author_budget',dict(counts)))
assert not fail,fail
payload=''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in out);dest=ROOT/'voice/forums-deep-02.jsonl'
if dest.exists() and dest.read_text()!=payload:raise RuntimeError('Fresh wave exists; do not overwrite/reappend.')
dest.write_text(payload)
report={'file':'voice/forums-deep-02.jsonl','quotes':len(out),'failed':0,'max_quote_words':max(q['quote_words'] for q in out),'cross_wave_author_aggregate_word_max':max(counts.values()),'checks':['exact original post substring','normalized raw HTML text match','quote/context<=25words','aggregate author quote words<=25 across fdeep01+02','complete thread/page read']}
(ROOT/'synthesis/forums-deep-02-quote-verification.json').write_text(json.dumps(report,indent=2));print(report)
for f in (ROOT/'sources').glob('forums-deep-*-final.jsonl'):
    rows=[json.loads(l) for l in f.read_text().splitlines()]
    for x in rows:x['quote_ids']=sorted({*x.get('quote_ids',[]),*(q['id'] for q in out if q['thread_id']==x['thread_id'])})
    f.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
