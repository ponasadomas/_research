import json,collections,re
r=[json.loads(l) for l in open('voice-merged/all.jsonl')]
w3=[x for x in r if x['id'][:4] in('dv05','dv06')]
promo=lambda x:'possible_promo' in x['themes']
print('w3',len(w3),'restricted',sum(x['restricted'] for x in w3),'promo',sum(promo(x) for x in w3))
for p in ('dv05','dv06'):
    v=[x for x in w3 if x['id'][:4]==p]; print(p,len(v),sum(x['restricted'] for x in v))
print('dates',min(x['date'] for x in w3),max(x['date'] for x in w3),[x['id'] for x in w3 if x['date']>'2026-06-24'])
print('speaker',collections.Counter(x['speaker'] for x in w3).most_common())
print('stage',collections.Counter(x['stage'] for x in w3).most_common())
print('type pp',collections.Counter(x['type'] for x in w3 if x['type'] in('purchase','price_signal')),'unrestricted',collections.Counter(x['type'] for x in w3 if x['type'] in('purchase','price_signal') and not x['restricted']))
c=collections.Counter(t for x in w3 for t in x['themes']);cr=collections.Counter(t for x in w3 for t in x['themes'] if x['restricted'])
for t in ['maternal_guilt','screen_time','wont_play_alone','what_to_do_all_day','independent_play','bored_baby','boredom_baby','boredom_mum','mobility_frustration','container_time','lovevery','household_objects','partner_pressure','relatives_screens','grandparent_comments','working_parent','personalization','guide_ask','paid_program_ask','routine_ask','app_tracking','milestone_anxiety','pediatrician_checkup','first_words','information_overload','stuck_inside','social_media','price_value']:
    print('  ',t,c[t],cr[t])
for t in ['bored_baby','mobility_frustration']:
    for p in ('dv05','dv06'):
        print(t,p,collections.Counter(x['stage'] for x in w3 if t in x['themes'] and x['id'][:4]==p))
    print(t,'all',collections.Counter(x['stage'] for x in w3 if t in x['themes']))
# all-day posts that also carry restricted quotes in the same post
posts=collections.defaultdict(list)
for x in w3: posts[x['post_id']].append(x)
ad=[p for p,v in posts.items() if any('what_to_do_all_day' in x['themes'] for x in v)]
adr=[p for p in ad if any(x['restricted'] for x in posts[p])]
print('posts w3',len(posts),'all-day posts',len(ad),'of which with restricted quote',len(adr),[ [x['id'] for x in posts[p] if x['restricted']] for p in adr])
# app/guide name search
pat=r'\b(app|apps|kinedu|sprouty|huckleberry|wonder weeks|babysparks|lovevery|guide|guides|course|program|programs|pdf|e-?book|book for|tracker)\b'
print('search',[(x['id'],'R' if x['restricted'] else '', 'P' if promo(x) else '') for x in w3 if re.search(pat,x['quote'],re.I)])
print('money',[x['id'] for x in w3 if re.search(r'[$£€]\s?\d|\d+\s?(dollars|bucks|pounds)|\b\d+ a week',x['quote'],re.I)])
print('--- excluding possible_promo ---')
w=[x for x in w3 if not promo(x)]
print('independent quotes',len(w),'restricted',sum(x['restricted'] for x in w))
c=collections.Counter(t for x in w for t in x['themes']);cr=collections.Counter(t for x in w for t in x['themes'] if x['restricted'])
for t in ['maternal_guilt','screen_time','what_to_do_all_day','independent_play','wont_play_alone','bored_baby','mobility_frustration','container_time','lovevery','app_tracking','household_objects','partner_pressure','grandparent_comments','working_parent','not_enough_play','milestone_anxiety','pediatrician_checkup','first_words','price_value']:
    print('  ',t,c[t],cr[t])
for t in ['bored_baby','mobility_frustration','what_to_do_all_day']:
    print(t,collections.Counter(x['stage'] for x in w if t in x['themes']).most_common())
print('stage',collections.Counter(x['stage'] for x in w).most_common())
print('speaker partner',sum(x['speaker']=='partner' for x in w))
posts=collections.defaultdict(list)
for x in w: posts[x['post_id']].append(x)
ad=[p for p,v in posts.items() if any('what_to_do_all_day' in x['themes'] for x in v)]
print('all-day posts',len(ad),'with restricted quote',sum(1 for p in ad if any(x['restricted'] for x in posts[p])),'with not_enough_play or maternal_guilt quote',sum(1 for p in ad if any(set(x['themes'])&{'not_enough_play','maternal_guilt'} for x in posts[p])))
