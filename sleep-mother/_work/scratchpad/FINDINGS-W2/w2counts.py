#!/usr/bin/env python3
"""Wave-2 counts for findings section 16. Run from sleep-mother/: python3 -I scratchpad/FINDINGS-W2/w2counts.py"""
import json, re, collections, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs=[json.loads(l) for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8') if l.strip()]
w2=[r for r in recs if r['id'][:4] in ('sm04','sm05','sm06')]
C=collections.Counter
P=('pregnancy_first','pregnancy_second','pregnancy_third','second_pregnancy')
print('1 wave-2 quotes',len(w2),'restricted',sum(r['restricted'] for r in w2))
for p in ('sm04','sm05','sm06'):
    s=[r for r in w2 if r['id'].startswith(p)]
    print('  ',p,len(s),'restricted',sum(r['restricted'] for r in s),'partner',sum(r['speaker']=='partner' for r in s))
print('  dates',min(r['date'] for r in w2),max(r['date'] for r in w2))
print('2 pregnancy-stage quotes',sum(r['stage'] in P for r in w2), C(r['stage'] for r in w2 if r['stage'] in P))
for p in ('sm04','sm05','sm06'):
    s=[r for r in w2 if r['id'].startswith(p)]
    print('  ',p,'second_pregnancy',sum(r['stage']=='second_pregnancy' for r in s),
          'experienced_mother on trimester stage',sum(r['speaker']=='experienced_mother' and r['stage'] in P[:3] for r in s))
preg=[r for r in w2 if r['stage'] in P]
def th(t,rs): return sum(t in r.get('themes',[]) for r in rs)
print('3 pregnancy-stage quotes with theme return_to_work_exhausted',th('return_to_work_exhausted',preg),'working_pregnant',th('working_pregnant',preg))
print('  pregnancy-stage themes bathroom_trips',th('bathroom_trips',preg),'body_pain',th('body_pain',preg),'physical_discomfort',th('physical_discomfort',preg),'racing_mind',th('racing_mind',preg),'pregnancy_pillow',th('pregnancy_pillow',preg))
for name,rx in [('heartburn/reflux/acid',r'heartburn|reflux|acid'),('pee/bathroom/toilet/urinat/bladder',r'\bpee|bathroom|toilet|urinat|bladder'),('hip/pelvi/pubic/back pain',r'\bhips?\b|pelvi|pubic|back pain|back hurts|sciatica')]:
    m=[r['id'] for r in preg if re.search(rx,r['quote'],re.I)]
    print('  pregnancy-stage quotes matching',name,len(m),' '.join(m))
print('4 type purchase',sum(r['type']=='purchase' for r in w2),'price_signal',sum(r['type']=='price_signal' for r in w2))
amt=re.compile(r'[$£€]\s?\d|\d\s?(k|K)\b|\d\s?\$|\d+\s?(dollars|pounds|euros|bucks)|thirty-two|\$\$')
print('5 amount pattern:',' '.join(r['id']+('(R)' if r['restricted'] else '') for r in w2 if amt.search(r['quote'])))
bad=re.compile(r'refund|money back|scam|waste of money|rip.?off|robb|overpay|worth more money')
print('6 scam/waste pattern:',' '.join(r['id']+('(R)' if r['restricted'] else '') for r in w2 if bad.search(r['quote'],0) or re.search(bad,r['quote'].lower())))
info=re.compile(r'meditat|cbt|sleepio|stellar|headspace|calm podcast|podcast|audiobook|hypno|youtube|insomnia coach|app\b|course|book',re.I)
print('7 info/app pattern:',' '.join(r['id']+('(R)' if r['restricted'] else '') for r in w2 if info.search(r['quote'])))
