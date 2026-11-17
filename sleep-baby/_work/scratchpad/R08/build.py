import json,re,sys,os
B=os.path.dirname(os.path.abspath(__file__))
NICHE=os.path.join(B,'..','..')
def meta(unit):
    p=os.path.join(NICHE,'../_shared/_raw/reddit-2026/units/'+unit+'.txt')
    t=open(p,encoding='utf-8').read()
    m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',t)
    com={c:(d,u) for c,d,u in re.findall(r'^COMMENT (\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)',t,re.M)}
    return m.groups(),com
SEED=set('night_wakings contact_naps short_naps wake_windows early_waking bedtime_battle regression_4_month feeding_to_sleep dream_feed night_weaning cosleeping bedsharing room_sharing transition_to_cot sleep_training_values cry_it_out ferber gentle_method chair_method pick_up_put_down consistency_failure partner_split_nights partner_disagreement daycare_naps nap_transition drop_nap sleep_props pacifier swaddle_transition white_noise schedule_rigidity sleep_consultant course_purchase app_tracking information_overload conflicting_advice maternal_exhaustion resentment guilt comparison_other_babies safe_sleep_fear money_back price_value personalization'.split())
out=[];n=0
for f in sorted(x for x in os.listdir(B) if x.startswith('drafts') and x.endswith('.jsonl')):
    for line in open(os.path.join(B,f),encoding='utf-8'):
        if not line.strip(): continue
        d=json.loads(line); n+=1
        (pid,sub,date,url),com=meta(d['u'])
        r={'id':'sb08-%04d'%n,'source':'reddit r/'+sub}
        if d.get('c'):
            cd,cu=com[d['c']]; r['url']=cu; r['date']=cd
        else: r['url']=url; r['date']=date
        r.update(speaker=d['sp'],stage=d['st'],type=d['ty'],themes=sorted(d['th'],key=lambda t: t not in SEED),quote=d['q'],context=d['cx'],
          raw_file='../_shared/_raw/reddit-2026/units/'+d['u']+'.txt',source_class='reddit_archive',post_id=pid)
        if d.get('c'): r['comment_id']=d['c']
        assert len(d['cx'].split())<=25, d['cx']
        out.append(r)
with open(os.path.join(NICHE,'voice','reddit-r08.jsonl'),'w',encoding='utf-8') as o:
    for r in out: o.write(json.dumps(r,ensure_ascii=False)+'\n')
print(n)
