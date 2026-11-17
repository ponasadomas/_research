#!/usr/bin/env python3
"""For every quoted fragment in findings.md, find the next ids on the same line; report if the fragment is in none of them; historical subject markings have no effect."""
import json,re,sys
R={}
for l in open('voice-merged/all.jsonl',encoding='utf-8'):
    if l.strip(): r=json.loads(l); R[r['id']]=r
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace(' ',' ')
    return re.sub(r'\s+',' ',s).strip()
bad=0;n=0
for ln,line in enumerate(open('synthesis/findings.md',encoding='utf-8'),1):
    for m in re.finditer(r'"([^"]*)"',line):
        frag=m.group(1)
        if len(frag) < 6: continue
        rest=line[m.end():]
        ids=[]
        mm=re.search(r'\[([^\]]*pb\d\d-\d{4}[^\]]*)\]',rest)
        if mm: ids=re.findall(r"pb\d\d-\d{4}",mm.group(1))
        if line.startswith("|"): ids=re.findall(r"pb\d\d-\d{4}",rest)
        if not ids: continue
        # A quotation in prose is not paired with a distant citation.
        # Parse short quotation pairs too, so they cannot shift the delimiters.
        if mm and (mm.start() > 120 or chr(34) in rest[:mm.start()]): continue
        n+=1
        hit=[i for i in ids if i in R and norm(frag) in norm(R[i]['quote'])]
        if not hit: print(f'L{ln} NOTFOUND {ids} "{frag[:70]}"'); bad+=1
print('fragments checked',n,'problems',bad)

sys.exit(1 if bad else 0)
