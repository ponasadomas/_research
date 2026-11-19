#!/usr/bin/env python3
"""menu.py NN [nearmin]  -> for each ### of section NN, each cited quote widened to whole sentences."""
import json,glob,os,re,sys,csv
Q=os.path.expanduser('~/GitHub/_research/baby-development/quotes')
D=os.path.expanduser('~/GitHub/_research/baby-development/findings/2026-11/patterns')
rec={}
for f in glob.glob(Q+'/reddit-sr*.jsonl'):
    for l in open(f,encoding='utf-8'):
        if l.strip():
            r=json.loads(l); rec[r['id']]=r
posts={}
with open(os.path.expanduser('~/GitHub/_research/baby-development/evidence/2026-11/second-reading/posts.tsv'),encoding='utf-8') as fh:
    for row in csv.DictReader(fh,delimiter='\t'): posts[row['post_id']]=row
def widen(text,a,b):
    # sentence boundaries
    s=a
    while s>0 and not (text[s-1] in '\n' or (text[s-1]==' ' and s>=2 and text[s-2] in '.!?…”"')): s-=1
    m=re.search(r'[.!?…]+["”’)]*(?=\s|$)|\n',text[max(b-1,0):])
    e=max(b-1,0)+m.end() if m else len(text)
    return s,e
def expand(q,i):
    text=rec[i]['quote']
    parts=[p.strip() for p in re.split(r'\[…\]',q) if p.strip()]
    spans=[]
    for p in parts:
        k=text.find(p)
        if k<0: k=text.find(p.rstrip('.,;'))
        if k<0: return '??'+q
        spans.append(widen(text,k,k+len(p)))
    spans.sort(); out=[list(spans[0])]
    for a,b in spans[1:]:
        if a<=out[-1][1]+1: out[-1][1]=max(out[-1][1],b)
        else: out.append([a,b])
    return ' […] '.join(text[a:b].strip() for a,b in out)
k=sys.argv[1]; nearmin=int(sys.argv[2]) if len(sys.argv)>2 else 0
part=None; show=True
for l in open(f"{D}/pattern-{k}.md",encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('## '):
        part=l[3:]
        if part=='Coverage': break
        print('\n=== '+part); continue
    if l.startswith('### '): head=l; pending=True; continue
    m=re.match(r'^(\d+) of (\d+) posts',l)
    if m:
        show = not (part=='Near posts' and int(m.group(1))<nearmin)
        if show: print(f"\n{head}  ({m.group(1)})")
        continue
    if not show: continue
    for q,i in re.findall(r'"([^"\n]+)" \[(sr\d+-\d+)\]',l):
        r=rec[i]; p=posts.get(r['post_id'],{})
        tag=('B ' if l.startswith('**But') else '')
        sp={'parent_unspecified':'','new_mother':'NM','experienced_mother':'EM'}.get(p.get('speaker',''),p.get('speaker',''))
        st=p.get('stage','').replace('toddler_','t').replace('baby_','b').replace('_months','m').replace('newborn_0_8_weeks','nb')
        ex=expand(q,i)
        if len(ex.split())>60: ex=' '.join(ex.split()[:60])+' ~~'
        print(f"{tag}[{i}] {p.get('subreddit','')[:6]}/{sp}/{st}/{p.get('border','')}: {ex}")
