import json, re, glob, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SP={'nm':'new_mother','em':'experienced_mother','pu':'parent_unspecified','pa':'partner','rc':'relative_caregiver','gp':'gave_up_parent','rp':'recovered_parent','sk':'skeptic','ex':'expecting_mother'}
ST={'nb':'newborn_0_8_weeks','b24':'baby_2_4_months','r4':'regression_4_months','b58':'baby_5_8_months','b912':'baby_9_12_months','t12':'toddler_12_24_months','t24':'toddler_24_36_months','lb':'looking_back','un':'unknown','unknown':'unknown'}
SEED='night_wakings contact_naps short_naps wake_windows early_waking bedtime_battle regression_4_month feeding_to_sleep dream_feed night_weaning cosleeping bedsharing room_sharing transition_to_cot sleep_training_values cry_it_out ferber gentle_method chair_method pick_up_put_down consistency_failure partner_split_nights partner_disagreement daycare_naps nap_transition drop_nap sleep_props pacifier swaddle_transition white_noise schedule_rigidity sleep_consultant course_purchase app_tracking information_overload conflicting_advice maternal_exhaustion resentment guilt comparison_other_babies safe_sleep_fear money_back price_value personalization'.split()
TY={'guilt':'pain','gave_up':'failure_story'}
TYPES={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said','purchase','price_signal'}
units={}
for l in open('scratchpad/R46/units.txt'):
    p=l.split()
    if len(p)==3: units[os.path.basename(p[1])[:-4]]=p[1]
out=[]; n=0; restricted=[]
for f in sorted(glob.glob('scratchpad/R46/q*.jsonl')):
    for line in open(f):
        if not line.strip(): continue
        row=json.loads(line); u,c,sp,st,ty,th,q,cx=row[:8]; rflag=len(row)>8
        rf=units[u]; txt=open(rf).read()
        m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
        pid,sub,d,url=m.groups()
        rec={}
        if c:
            mm=re.search(r'COMMENT '+c+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
            d,url=mm.groups()
        n+=1
        rec={'id':'sb46-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':d,'speaker':SP[sp],'stage':ST[st],'type':TY.get(ty,ty),'themes':[t for t in th if t in SEED]+[t for t in th if t not in SEED],'quote':q,'context':cx,'raw_file':rf,'source_class':'reddit_archive','post_id':pid}
        if c: rec['comment_id']=c
        if rflag: restricted.append(rec['id'])
        assert len(cx.split())<=25, (u,cx)
        assert rec['type'] in TYPES, (u,ty)
        out.append(rec)
with open('voice/reddit-r46.jsonl','w') as o:
    for r in out: o.write(json.dumps(r,ensure_ascii=False)+'\n')
print(n)
open('scratchpad/R46/restricted.txt','w').write('\n'.join(restricted)+'\n')
print('restricted',len(restricted))
