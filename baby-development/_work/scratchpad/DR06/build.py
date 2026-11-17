import json,re,sys,os
D='/home/thinkpad/GitHub/ads/mamivio.com/research/development'
src=os.path.join(D,'scratchpad/DR06/drafts.jsonl')
out=os.path.join(D,'voice/reddit-dr06.jsonl')
recs=[];restr=[]
SEED=set('what_to_do_all_day awake_time tummy_time tummy_time_hate floor_play rolling sitting crawling pulling_up walking first_words babbling fine_motor milestone_comparison milestone_anxiety corrected_age pediatrician_checkup cdc_milestones wonder_weeks leaps screen_time toys_too_many montessori play_ideas boredom_mum maternal_guilt not_enough_play container_time baby_classes app_tracking information_overload conflicting_advice reassurance_seeking social_comparison grandparent_comments early_intervention_question personalization price_value'.split())
for i,l in enumerate([l for l in open(src) if l.strip()],1):
    d=json.loads(l)
    rf='../_shared/_raw/reddit-2026/units/%s.txt'%d['u']
    txt=open(os.path.join(D,rf)).read()
    pid=d['u'].rsplit('-',1)[1]
    sub=re.search(r'^POST \S+ \| r/(\S+) \| (\d{4}-\d\d-\d\d)',txt,re.M)
    url='https://www.reddit.com/r/%s/comments/%s/'%(sub.group(1),pid); date=sub.group(2)
    r={'id':'dv06-%04d'%i,'source':'reddit r/'+sub.group(1)}
    if d.get('c'):
        m=re.search(r'^COMMENT %s \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)'%d['c'],txt,re.M)
        date=m.group(1); url=m.group(2)
    r.update(url=url,date=date,speaker=d['sp'],stage=d['st'],type=d['ty'],themes=sorted(d['th'],key=lambda t:t not in SEED),quote=d['q'],context=d['cx'],raw_file=rf,source_class='reddit_archive',post_id=pid)
    if d.get('c'): r['comment_id']=d['c']
    if d.get('promo'): r['possible_promo']=True
    assert len(d['cx'].split())<=25, (i,d['cx'])
    recs.append(r)
    if d.get('r'): restr.append(r['id'])
open(out,'w').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in recs))
print(len(recs),'restricted',restr)
