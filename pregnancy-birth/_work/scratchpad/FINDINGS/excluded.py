#!/usr/bin/env python3
"""Collect excluded units from every reading ledger and bucket the neutral reason by keyword."""
import re,glob,collections
rows=[]
for f in sorted(glob.glob('/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/sources/reddit-reading-pr*.md')):
    t=open(f,encoding='utf-8').read()
    sec=re.search(r'\n#+ [^\n]*[Ee]xcluded[^\n]*\n(.*?)(?=\n#+ |\Z)',t,re.S)
    secl=set(sec.group(1).splitlines()) if sec else set()
    for line in t.splitlines():
        u=re.findall(r'([A-Za-z]+-1[0-9a-z]{6})',line)
        if not u or not line.lstrip().startswith(('|','-','*')): continue
        if line in secl or re.search(r'\|\s*(excluded|EXCLUDED)\b|excluded:|EXCLUDED:',line):
            rows.append((f[-7:-3],u[-1] if 'units/' in line else u[0],line))
seen=set(); uniq=[]
for p,u,l in rows:
    if (p,u) in seen: continue
    seen.add((p,u)); uniq.append((p,u,l.lower()))
B=[('loss / termination decision / stillbirth','loss|miscarri|terminat|continu\\w* (the|a|a very early) pregnancy|end(ing)? (the|a) pregnancy|stillbirth|abortion|tfmr|ectopic|chemical|bereave|dying|pregnancy decision'),
   ('crisis / self-harm / severe mental health','crisis|suicid|self-harm|harm|psychosis|severe mental|intrusive|overdose|want to die|mental.health|depression'),
   ('acute medical emergency / NICU / hospital admission','emergen|nicu|breathing support|complication|admission|admitted|bleeding|preterm|acute|hospitali|injur|seizure|icu'),
   ('screening result / diagnosis-centred','screen|scan finding|diagnos|result|anomal|condition|genetic|nipt'),
   ('substance use','substance|alcohol|drug|weed|cannabis|wine|smok'),
   ('abuse / partner aggression / child safety','abuse|aggress|violen|mistreat|safety|assault|threat|unsafe|sexual|coercion|police'),
   ('minor / age','minor|under 18|age'),
   ('off-niche, duplicate, seller or other','')]
c=collections.Counter(); ex=collections.defaultdict(list)
for p,u,l in uniq:
    for name,rx in B:
        if not rx or re.search(rx,l):
            c[name]+=1; ex[name].append(u); break
print('excluded unit rows found:',len(uniq))
for name,_ in B: print(f'{c[name]:4d}  {name}')
import sys
if '-v' in sys.argv:
    for name,_ in B:
        print('##',name); [print('  ',l[:160]) for p,u,l in uniq if u in ex[name]][:0]
        for p,u,l in uniq:
            if u in ex[name]: print('   ',p,l[:170])
