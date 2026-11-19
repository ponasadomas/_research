#!/usr/bin/env python3
import json,glob,os,re,sys
sys.path.insert(0,os.path.dirname(__file__))
from sections import load
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE=os.path.expanduser('~/GitHub/_research/baby-development/findings/what-hurts-and-what-she-wants.md')
OUT=os.path.expanduser('~/GitHub/_research/baby-development/her-words.md')
DROP=set(open(S+'/words-drop.txt').read().split())
def norm(s):
    for x, y in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("\\n", " "), ("\\", "")): s = s.replace(x, y)
    return re.sub(r"\s+", " ", s).strip().lower()
rec={}
for f in glob.glob(os.path.expanduser('~/GitHub/_research/baby-development/quotes/reddit-sr*.jsonl')):
    for l in open(f,encoding='utf-8'):
        if l.strip(): r=json.loads(l); rec[r['id']]=norm(r['quote'])
atag=json.load(open(S+'/atag.json')); sec=load(); went={(k,p,h):c for k,p,h,c in json.load(open(S+'/went.json'))}
page=open(PAGE,encoding='utf-8').read().split('\n## Coverage')[0]
count={}
for b in re.split(r'^### ',page,flags=re.M)[1:]:
    m=re.search(r'^(\d[\d,]*) of ([\d,]+) posts\.',b,re.M); count[b.split('\n')[0].strip()]=(m.group(1),m.group(2))
PR={'On-niche posts':0,'Near posts':1,'Across the on-niche posts':2}
where={}
for k,v in sec.items():
    for h in v['heads']:
        if h['level']!=3: continue
        for i in h['ids']:
            cand=(PR[h['part']],k,h['part'],h['head'])
            if i not in where or cand<where[i]: where[i]=cand
out=['# Baby development: her words','','**Written:** 2026-11-20. **Reviewed by the owner:** not yet','',
'Phrases copied word for word from the posts behind `findings/what-hurts-and-what-she-wants.md`, grouped as that page is. The bracket after each phrase is the count of the finding it belongs to on that page (posts tagged by one reader, out of the pattern\'s on-niche posts). A count that starts with "tried", "others said", "paid" or "how they feel" is the count of posts in the pattern that show that at all, not of posts that say this; "near" counts are out of the 5,534 near posts; "once" marks a wording that is rare but sharp. "She" is whoever wrote the post: 81.5% of the posts do not say whether the writer is a mother, and some of these lines are fathers\'.','',
'Her vocabulary: the jargon glossary for this round is not made yet, so that group is left out.','']
group=None; items=[]; total=0; bad=0
def flush():
    global items
    if group is None: return
    out.append('## '+group); out.append('')
    non=[x for x in items if not x[2]]; once=[x for x in items if x[2]]
    non.sort(key=lambda x:-x[3])
    for ph,i,o,n,ann in non+once: out.append(f'- "{ph}" [{i}] ({ann})')
    out.append(''); items=[]
for l in open(S+'/words.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if not l.strip(): continue
    if l.startswith('## '): flush(); group=l[3:]; continue
    parts=[x.strip() for x in l.split(' | ')]; i,ph=parts[0],parts[1]; once=len(parts)>2 and parts[2]=='once'; label=parts[3] if len(parts)>3 else ''
    if i in DROP: continue
    if norm(ph).rstrip('.,;') not in rec.get(i,''): print('NOT WORD FOR WORD',i,ph); bad+=1; continue
    if i not in where: print('NO HEADING',i); bad+=1; continue
    _,k,part,head=where[i]; claim=went[(k,part,head)]; n,m=count[claim]
    ann='once' if once else (f'near: {n} of {m} posts' if part=='Near posts' else (f'{atag[claim]}: {n} of {m} posts' if part.startswith('Across') else f'{n} of {m} posts'))
    if label: ann+='; '+label
    items.append((ph,i,once,int(n.replace(',','')),ann)); total+=1
flush()
open(OUT,'w',encoding='utf-8').write('\n'.join(out))
print('phrases',total,'problems',bad,'written',OUT)
