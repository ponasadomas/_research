import sys
# usage: mk.py out cardfile  (reads keep spec from stdin: id|label|reason ; drops: id|code ; codes in D)
D={'inf':'baby under 1 year, not toddler behaviour','slp':'sleep-only post, other niche','off':'off-topic for toddler behaviour','old':'child 5 or older','med':'medical or feeding question, no behaviour fight','dup':'duplicate repost'}
import re
out=sys.argv[1]; card=sys.argv[2]
ids=re.findall(r'^ID (\w+) ',open(card).read(),re.M)
spec={}
for l in sys.stdin:
    l=l.rstrip('\n')
    if not l.strip(): continue
    p=l.split('|')
    spec[p[0]]=p
rows=[]
for i in ids:
    if i not in spec: print('MISSING',i); continue
    p=spec[i]
    if len(p)==2: rows.append((i,'drop',D.get(p[1],p[1])))
    else: rows.append((i,p[1],p[2]))
extra=set(spec)-set(ids)
if extra: print('EXTRA',extra)
open(out,'w').write(''.join(f"{a}\t{b}\t{c}\n" for a,b,c in rows)); print(len(rows))
