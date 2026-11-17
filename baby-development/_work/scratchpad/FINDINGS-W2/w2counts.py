import json,collections
r=[json.loads(l) for l in open('voice-merged/all.jsonl')]
w={'w1':[x for x in r if x['id'][:4] in('dv01','dv02')],'w2':[x for x in r if x['id'][:4] in('dv03','dv04')]}
for k,v in w.items():
    print(k,len(v),'restricted',sum(x['restricted'] for x in v))
    print(' speaker',collections.Counter(x['speaker'] for x in v).most_common())
    print(' type',{t:n for t,n in collections.Counter(x['type'] for x in v).items() if t in('purchase','price_signal')}, 'unrestricted',collections.Counter(x['type'] for x in v if x['type'] in('purchase','price_signal') and not x['restricted']))
    c=collections.Counter(t for x in v for t in x['themes']);cr=collections.Counter(t for x in v for t in x['themes'] if x['restricted'])
    for t in ['what_to_do_all_day','wont_play_alone','boredom_baby','bored_baby','maternal_guilt','screen_time','container_time','working_parent','personalization','app_tracking','grandparent_comments','milestone_anxiety','first_words','pediatrician_checkup','independent_play','price_value','household_objects','stuck_inside']:
        print('  ',t,c[t],cr[t])
