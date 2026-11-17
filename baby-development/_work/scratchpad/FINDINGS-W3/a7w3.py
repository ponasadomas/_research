import json,re,sys
norm=lambda s:re.sub(r'[^a-z0-9 ]','',s.lower().replace('’',"'"))
r={json.loads(l)['id']:json.loads(l) for l in open('voice-merged/all.jsonl')}
R={i for i,x in r.items() if x['restricted']}
t=open('synthesis/findings.md').read()
t=t.split('## 17. What wave 3 added')[1]
for sent in re.split(r'(?<=[.!?])\s+|\n',t):
  for i in set(re.findall(r'\[([a-z]+\d{2}-\d{4})\]',sent)):
    if i in R:
      q=norm(r[i]['quote']).split(); s=norm(re.sub(r'\[[^\]]*\]','',sent)).split()
      g={' '.join(q[k:k+3]) for k in range(len(q)-2)}&{' '.join(s[k:k+3]) for k in range(len(s)-2)}
      if g: print(i,g)
