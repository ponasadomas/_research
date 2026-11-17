#!/bin/bash
# usage: full.sh sub id [chars]
python3 -I - "$@" <<'PY'
import sys,json
sub,i=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 1500
for l in open(f'/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/{sub}.posts.jsonl'):
    d=json.loads(l)
    if d.get('id')==i:
        print(i,d.get('title'),'||',(d.get('selftext') or '')[:n].replace('\n',' '));break
PY
