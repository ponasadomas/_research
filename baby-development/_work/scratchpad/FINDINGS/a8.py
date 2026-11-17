import json,re
def norm(s):
  s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
  return re.sub(r'\s+',' ',s).strip()
r={json.loads(l)['id']:json.loads(l) for l in open('voice-merged/all.jsonl')}
t=open('synthesis/findings.md').read().split('## Appendix')[0]
for n,line in enumerate(t.split('\n'),1):
  ids=re.findall(r'\[([a-z]+\d{2}-\d{4})\]',line)
  if not ids: continue
  qs=[norm(r[i]['quote']) for i in ids if i in r]
  for f in re.findall(r'"([^"]{12,}?)"',norm(line)):
    if not any(f in q for q in qs): print(n,repr(f[:90]))
