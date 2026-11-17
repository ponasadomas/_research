#!/bin/bash
# usage: robots.sh domain...  -> saves robots/<domain>.txt, prints status + AI bans
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
for d in "$@"; do
  code=$(curl -sSL --compressed --max-time 20 -A "$UA" -o robots/$d.txt -w "%{http_code}" "https://$d/robots.txt" 2>/dev/null)
  ai=$(python3 -I - robots/$d.txt <<'PY'
import sys,re
t=open(sys.argv[1],errors='replace').read()
if '<html' in t.lower()[:500]: print('html-not-robots'); sys.exit()
groups=[];cur=None;last_ua=False
for line in t.splitlines():
  l=line.split('#')[0].strip()
  if not l: continue
  k,_,v=l.partition(':');k=k.strip().lower();v=v.strip()
  if k=='user-agent':
    if not last_ua: cur={'ua':[],'dis':[]};groups.append(cur)
    cur['ua'].append(v.lower());last_ua=True
  else:
    last_ua=False
    if cur and k=='disallow': cur['dis'].append(v)
out=[]
for g in groups:
  for u in g['ua']:
    if any(b in u for b in ['gptbot','claude','anthropic','ccbot','chatgpt','*']):
      if '/' in g['dis']: out.append(u+':ALL')
print(' '.join(out) or 'ok')
PY
)
  echo "$d $code $ai"
done
