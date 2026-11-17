import re,glob,os
R='../../'
asg=[l for l in open(R+'_raw/reddit/filter-v1/wave2/assignments.txt') if l.startswith('W2T1')][0].split()[1:]
rows=[];allids=[]
for f in asg:
    key=f[2:-4]
    ids=re.findall(r'^ID (\S+) \|',open(R+'_raw/reddit/filter-v1/wave2/cards/'+f).read(),re.M)
    allids+=ids
    ex={};dl=None
    for l in open(f'ex-{key}.txt'):
        l=l.rstrip('\n')
        if l.startswith('# default:'):
            dl=l[10:].strip().split('|'); continue
        p=l.split('\t'); ex[p[0]]=(p[1],p[2])
    assert dl or True
    bad=[i for i in ex if i not in ids]
    if bad: print('NOT IN FILE',f,bad)
    for i in ids:
        if i in ex: rows.append((i,)+ex[i])
        elif dl: rows.append((i,dl[0],dl[1]))
        else: print('UNLABELLED',f,i)
# dup check
from collections import Counter
c=Counter(r[0] for r in rows); print('dups',[k for k,v in c.items() if v>1][:20])
print(len(allids),len(rows),Counter(r[1] for r in rows))
open(R+'_raw/reddit/triage/wave2-W2T1.tsv','w').write('post_id\tlabel\treason\n'+''.join('\t'.join(r)+'\n' for r in rows))
print(set(allids)==set(r[0] for r in rows), len(set(allids)))
