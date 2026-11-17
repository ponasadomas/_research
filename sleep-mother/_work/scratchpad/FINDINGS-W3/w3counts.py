#!/usr/bin/env python3
"""Wave-3 counts for findings section 17. Run from sleep-mother/: python3 -I scratchpad/FINDINGS-W3/w3counts.py"""
import json, re, collections, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs=[json.loads(l) for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8') if l.strip()]
w3=[r for r in recs if r['id'][:4] in ('sm07','sm08','sm09')]
C=collections.Counter
P=('pregnancy_first','pregnancy_second','pregnancy_third','second_pregnancy')
promo=lambda r:'possible_promo' in r.get('themes',[])
print('1 wave-3 quotes',len(w3),'restricted',sum(r['restricted'] for r in w3),'possible_promo',sum(promo(r) for r in w3),'units',len({r['post_id'] for r in w3}))
for p in ('sm07','sm08','sm09'):
    s=[r for r in w3 if r['id'].startswith(p)]
    print('  ',p,len(s),'restricted',sum(r['restricted'] for r in s),'partner',sum(r['speaker']=='partner' for r in s),'promo',sum(promo(r) for r in s),' '.join(r['id'] for r in s if promo(r)))
print('  dates',min(r['date'] for r in w3),max(r['date'] for r in w3), 'outside window:',[ (r['id'],r['date']) for r in w3 if not ('2026-04-01'<=r['date']<='2026-06-24')])
print('  all quotes',len(recs),'restricted',sum(r['restricted'] for r in recs))
print('2 pregnancy-stage quotes',sum(r['stage'] in P for r in w3),C(r['stage'] for r in w3 if r['stage'] in P))
print('  speakers',C(r['speaker'] for r in w3))
ind=[r for r in w3 if not promo(r)]
def th(t,rs=ind): return sum(t in r.get('themes',[]) for r in rs)
for t in ['shift_system','night_feeds_split','help_arrives_still_awake','cant_sleep_when_baby_sleeps','partner_sleeps_through','night_nanny','sleep_consultant','protecting_partner_sleep','partner_job_safety','partner_job','ai_chatbot','partner_snoring','wants_to_be_heard','price_value']:
    print('  theme (non-promo)',t,th(t))
amt=re.compile(r'[$£€]\s?\d|\d\s?(k|K)\b|\d\s?\$|\d+\s?(dollars|pounds|euros|bucks|yen)|\$\$|hundreds of|thousand|/hr|per hour|an hour\b|a week|a month|/week|/month',re.I)
print('3 amount pattern:',' '.join(r['id']+('(R)' if r['restricted'] else '')+('(P)' if promo(r) else '') for r in w3 if amt.search(r['quote'])))
bad=re.compile(r'refund|money back|scam|waste|rip.?off|robb|overpay|charlatan|regret|throwing our money|\bBS\b',re.I)
print('4 scam/waste pattern:',' '.join(r['id']+('(R)' if r['restricted'] else '') for r in w3 if bad.search(r['quote'])))
info=re.compile(r'meditat|cbt|sleepio|stellar|headspace|calm\b|podcast|audiobook|hypno|youtube|insomnia|app\b|course|book|chat ?gpt|\bAI\b',re.I)
print('5 info/app pattern:',' '.join(r['id']+('(R)' if r['restricted'] else '') for r in w3 if info.search(r['quote'])))
nh=re.compile(r'night (nanny|nurse|doula)|overnight doula|doula|mother hotel|night help|carrot',re.I)
print('6 night-help pattern:',' '.join(r['id']+('(R)' if r['restricted'] else '')+('(P)' if promo(r) else '') for r in w3 if nh.search(r['quote'])))
preg=[r for r in ind if r['stage'] in P]
print('7 non-promo pregnancy-stage quotes',len(preg),'racing_mind',th('racing_mind',preg),'return_to_work_exhausted',th('return_to_work_exhausted',preg),'working_pregnant',th('working_pregnant',preg))
for name,rx in [('bladder',r'\bpee|bathroom|toilet|urinat|bladder|\bwee\b'),('heartburn',r'heartburn|reflux|acid'),('hips/back',r'\bhips?\b|pelvi|pubic|back pain|back hurts|sciatica'),('insomnia word',r'insomnia'),('snor',r'snor')]:
    m=[r['id']+('(R)' if r['restricted'] else '') for r in preg if re.search(rx,r['quote'],re.I)]
    print('  pregnancy-stage',name,len(m),' '.join(m))
def grp(name,ids):
    d={r['id']:r for r in recs}; ids=ids.split()
    print('8 group',name,len(ids),'ids; units',len({d[i]['post_id'] for i in ids}),'; restricted',[i for i in ids if d[i]['restricted']],'; promo',[i for i in ids if promo(d[i])],'; speakers',dict(C(d[i]['speaker'] for i in ids)))
grp('10.1','sm07-0084 sm07-0086 sm07-0087 sm07-0090 sm07-0125 sm07-0368 sm07-0369 sm08-0095 sm08-0096 sm08-0098 sm08-0099 sm08-0100 sm08-0116 sm08-0118 sm08-0215 sm08-0216 sm09-0022 sm09-0023 sm09-0140 sm09-0143 sm09-0174 sm09-0236 sm09-0286 sm09-0287 sm09-0358 sm09-0359')
grp('10.2','sm07-0032 sm07-0033 sm07-0181 sm07-0342 sm07-0360 sm07-0408 sm08-0041 sm08-0042 sm08-0139 sm08-0291 sm08-0292 sm08-0293 sm08-0319 sm08-0326 sm08-0327 sm08-0374 sm09-0005 sm09-0038 sm09-0176 sm09-0201 sm09-0292 sm09-0310 sm09-0338 sm09-0363 sm09-0368')
grp('10.4','sm07-0205 sm07-0366 sm07-0401 sm07-0293 sm08-0336 sm08-0339 sm08-0316 sm08-0368 sm08-0406 sm08-0067 sm09-0075 sm09-0235 sm09-0177 sm09-0130 sm09-0372 sm09-0313')
grp('rejects-father/breast','sm07-0177 sm07-0179 sm07-0250 sm07-0413 sm07-0260 sm07-0304 sm07-0305 sm07-0154 sm08-0207 sm09-0224 sm09-0190 sm09-0362 sm09-0263 sm09-0307 sm09-0365 sm09-0310')
grp('cannot-wake','sm07-0180 sm07-0159 sm07-0329 sm07-0217 sm07-0146 sm08-0300 sm09-0350 sm09-0352 sm09-0355 sm09-0018 sm09-0215')
