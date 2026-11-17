#!/usr/bin/env python3
"""Hand classification of every restricted id (merged `restricted` flag) by reason, from the
reader-notes "Restricted ids" sections. Checks each flagged id is classified exactly once."""
import json,os,collections
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
flag={json.loads(l)['id'] for l in open(os.path.join(ROOT,'voice-merged','all.jsonl')) if l.strip() and json.loads(l)['restricted']}
def rng(p,a,b): return [f'{p}-{n:04d}' for n in range(a,b+1)]
MED='Medical history or treatment in the unit (laxatives, softeners, GI, feeding tube, prematurity, prescribed treatment, "something medically wrong")'
HARSH='Harshness or violence: parent shouting, a child kept on the potty while distressed, relatives advising hitting, a parent hit as a child'
GUILT='Guilt wording that names abuse ("I feel like I am abusing her")'
DIAG='Diagnosis, assessment or development question in the unit (ADHD, autism, sensory, speech delay, evaluation, therapy referral, IEP, special-needs school)'
cat={}
for i in ['tb01-0007']+['tb01-0046','tb01-0047','tb01-0048']+['tb06-0032']+rng('tb06',62,64)+['tb06-0118','tb06-0119']+rng('tb06',146,148)+['tb06-0186','tb06-0187']+rng('tb08',27,31)+['tb09-0110','tb09-0111','tb09-0168','tb09-0169','tb09-0170']:
    cat[i]=MED
for i in ['tb03-0297','tb05-0046','tb05-0047','tb05-0075','tb05-0083']: cat[i]=HARSH
cat['tb07-0222']=GUILT
for i in flag:
    cat.setdefault(i,DIAG)
missing=[i for i in cat if i not in flag]
assert not missing, missing
c=collections.Counter(cat[i] for i in flag)
print('flagged',len(flag))
for k,v in c.most_common(): print(v,'|',k)
pur=[i for i in ['tb09-0048','tb09-0049','tb09-0110','tb09-0111','tb09-0168','tb09-0244','tb09-0255','tb09-0256','tb09-0257','tb09-0258','tb09-0259','tb09-0260'] if i in flag]
print('tr09 purchase/price/objection lines kept from restricted units and flagged:',len(pur))
