#!/usr/bin/env python3
"""Ids inside the id ranges of reader-notes-tr17.md 'Units carrying a diagnosis' paragraph that are not flagged restricted.
With a file argument, also lists which of them that file cites."""
import json,re,os,sys
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
r={}
for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8'):
    if l.strip(): x=json.loads(l); r[x['id']]=x
t=open(os.path.join(ROOT,'synthesis','reader-notes-tr17.md'),encoding='utf-8').read()
sec=t.split('**Units carrying a diagnosis')[1].split('**Considered')[0]
un=[]
for a,b in re.findall(r'(tb17-\d{4}) … (tb17-\d{4})',sec):
    for n in range(int(a[5:]),int(b[5:])+1):
        i=f'tb17-{n:04d}'
        if not r[i]['restricted']: un.append(i)
print('unflagged ids inside ranges:',len(un))
if len(sys.argv)>1:
    f=open(sys.argv[1],encoding='utf-8').read()
    if '## 16.' in f: f=f[f.index('## 16.'):]
    print('cited in file:',sorted(set(un)&set(re.findall(r'tb17-\d{4}',f))))
