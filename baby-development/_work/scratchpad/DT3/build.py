import glob,re,os,sys
base='/home/thinkpad/GitHub/ads/mamivio.com/research/development/'
cards=base+'_raw/reddit/filter-v1/wave1/cards/'
files="A-Mommit-002 A-Mommit-005 A-NewParents-002 A-NewParents-005 A-Parenting-002 A-ScienceBasedParenting-001 A-beyondthebump-003 A-daddit-001 A-sahm-002 A-toddlers-003 A-toddlers-006".split()
ids=[]
for f in files:
    for l in open(cards+f+'.txt'):
        m=re.match(r'ID (\S+) \|',l)
        if m: ids.append(m.group(1))
lab={}
for k in glob.glob('keeps*.txt'):
    for l in open(k):
        p=l.rstrip('\n').split('\t')
        if len(p)==3:
            assert p[0] not in lab,p[0]
            lab[p[0]]=(p[1],p[2])
out=[]
for i in ids:
    l,r=lab.get(i,('drop','off-topic: older child, other niche, or not baby development'))
    out.append((i,l,r))
open(base+'_raw/reddit/triage/wave1-DT3.tsv','w').write('post_id\tlabel\treason\n'+''.join('\t'.join(o)+'\n' for o in out))
from collections import Counter
print(len(ids),len(set(ids)),Counter(o[1] for o in out))
extra=set(lab)-set(ids);print('unknown keeps',extra)
