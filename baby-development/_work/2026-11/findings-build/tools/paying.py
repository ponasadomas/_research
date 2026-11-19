#!/usr/bin/env python3
"""Sort the 82 paid-for rows of counts.md into kinds (the sorting is the findings writer's) and assert the sums."""
import re,os,json,glob,csv
from collections import Counter,defaultdict
C=os.path.expanduser('~/GitHub/_research/baby-development/evidence/2026-11/second-reading/counts.md')
rows=[]; on=False
for l in open(C,encoding='utf-8'):
    if l.startswith('| Post | Main pattern | Paid for'): on=True; continue
    if on:
        m=re.match(r'^\| (\w+) \| (\d+) \| (.+?) \|\s*$',l)
        if m: rows.append((m.group(1),int(m.group(2)),m.group(3)))
        elif l.startswith('##'): break
assert len(rows)==82,len(rows)
KIND={ # post id -> kind
'toys':'1v0a00t 1syfa0b 1stwdcq 1tw2tlw 1txfdav 1vp86gd 1xa2o4i 1s9u6xq 1sa1po2 1sq7837 1tnv5k3 1tt1o27 1vvcp57 1w99cso 1wk5egr 1sahmuz 1tc7cep 1tq4v8j 1sdhgk5',
'cups':'1t9jr8x 1sk8eaq 1t8bdde 1v6om42 1vbg9yk 1vlah1k 1vpkj7c',
'gear':'1uvdd0d 1sg8rkl 1t6z8il 1ulwa8x 1utc9ap 1u5mdfq 1v011zp 1v0v9i4 1vnbfze 1se4rlf 1scxsow 1szzunh 1umex3n 1utml2h 1uzc9mr 1vwj2mt 1w5zvfo 1wqrgm5 1sj2uyu 1wstnpg 1tgp9hl 1sl3bv6 1u3w3ne 1uesojn 1vdl60h 1ttxang',
'food':'1wid3te 1xec7s4 1t34i6o 1twrn3v 1vdrv6h 1vblk0k 1vtpizp 1whgihn 1wme7tq 1x0ivhz',
'person_or_place':'1skwjsb 1wmqdvl 1ssrp39 1v7m2m3 1sxiopq 1vplly1 1vut2ci 1txrtdi 1spy2kt 1upo5ms 1snng3h 1sq6dyu 1t9dvtx 1unn3ko 1wnhdy9',
'information':'1v04way 1stoi7a',
'self_or_unspecified':'1ve5iiz 1ud5ceu 1wfutpp'}
kind={p:k for k,v in KIND.items() for p in v.split()}
assert len(kind)==82 and set(kind)==set(r[0] for r in rows), set(r[0] for r in rows)^set(kind)
c=Counter(kind[r[0]] for r in rows); print(dict(c))
obj=c['toys']+c['cups']+c['gear']
assert (c['toys'],c['cups'],c['gear'],obj,c['food'],c['person_or_place'],c['information'],c['self_or_unspecified'])==(19,7,26,52,10,15,2,3)
print('by pattern',sorted(Counter(r[1] for r in rows).items()))
for k in KIND:
    print(k,':',' / '.join(r[2] for r in rows if kind[r[0]]==k)[:400])
# quotes in the Paying group belong to the 82?
rec={}
for f in glob.glob(os.path.expanduser('~/GitHub/_research/baby-development/quotes/reddit-sr*.jsonl')):
    for l in open(f,encoding='utf-8'):
        if l.strip(): r=json.loads(l); rec[r['id']]=r
page=open(os.path.expanduser('~/GitHub/_research/baby-development/findings/what-hurts-and-what-she-wants.md'),encoding='utf-8').read()
g=page.split('\n## Paying')[1].split('\n## ')[0]
for i in re.findall(r'\[(sr\d+-\d+)\]',g): print(i,rec[i]['post_id'],'in the 82' if rec[i]['post_id'] in kind else 'NOT in the 82', kind.get(rec[i]['post_id']))
# near posts: border by main pattern
posts=list(csv.DictReader(open(os.path.expanduser('~/GitHub/_research/baby-development/evidence/2026-11/second-reading/posts.tsv'),encoding='utf-8'),delimiter='\t'))
x=defaultdict(Counter)
for p in posts:
    if p['mark']=='near' and p['main_pattern']!='': x[p['main_pattern']][p['border']]+=1
for k in ('11','8','4','1','0'): print('near main',k,sum(x[k].values()),dict(x[k]))
