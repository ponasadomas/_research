#!/usr/bin/env python3
"""near.py -> the hand-typed figures of spec/17-near.md, computed and asserted: near posts about a child older than 48 months by age and by main pattern;
how many near posts the first reading's sections sorted that were about a child over 24 months, and how many of those are on the niche now;
the sorted near posts of the second reading that are by makers, developers or promoters."""
import os,sys,csv,collections
sys.path.insert(0,os.path.dirname(__file__))
from common import *
from sections import load
P=posts(); near=[p for p in P.values() if p['mark']=='near']; o48=[p for p in near if p['border']=='age_over_48']
G={'4 years':('child_4_years','4.5-year-old','4-year-old'),'5 years':('child_5_years','5-year-old'),'6 to 8':('child_6_to_8_years','7-year-old','6-year-old','7- and 8-year-olds','niece turning 6'),
'9 to 12':('child_9_to_12_years','12-year-old','9-year-old','11-year-old','turning 12','10- and 12-year-olds'),'13 to 17':('teen_13_to_17_years','13-year-old','16-year-old')}
c=collections.Counter()
for p in o48:
    for g,st in G.items():
        if p['stage'] in st: c[g]+=1; break
    else: c['unclear or other']+=1
print(len(o48),dict(c)); assert (len(o48),c['4 years'],c['5 years'],c['6 to 8'],c['9 to 12'],c['13 to 17'],c['unclear or other'])==(1976,438,299,523,335,248,133)
mp=collections.Counter(p['main_pattern'] for p in o48); print('main patterns',mp.most_common(4)); assert (mp['3'],mp['9'],mp['0'])==(363,252,387)
old=list(csv.DictReader(open(R+'/evidence/2026-11/second-reading/posts.tsv',encoding='utf-8'),delimiter='\t'))
x=[r for r in old if r['mark']=='near' and r['ties_to_development']=='yes']; y=[r for r in x if r['border']=='age_over_24']
now=collections.Counter(P[r['post_id']]['mark'] for r in y); print('first-reading sorted near',len(x),'over 24 months',len(y),'now',dict(now)); assert (len(x),len(y),now['yes'])==(1917,183,132)
sec=load()
PROMO=[('00','Makers ask parents to shape family tools.'),('04','Some speakers promote digital development resources.'),('09','Writers promote developmental promises.'),('11','They promote expert potty advice and support resources.'),('12','Parents are asked whether home speech practice would help or burden them.')]
t=0
for k,h in PROMO:
    hh=[x for x in sec[('a23',k)]['heads'] if x['level']==3 and x['part']=='Near posts' and x['head']==h]; assert len(hh)==1,(k,h); t+=hh[0]['n']
print('makers, developers, promoters among the second reading\'s sorted near posts',t); assert t==17
print('near checks OK')
