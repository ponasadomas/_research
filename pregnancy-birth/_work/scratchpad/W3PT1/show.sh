#!/bin/bash
# usage: show.sub id... ; prints first 900 chars of selftext
sub=$1; shift
python3 -I - "$sub" "$@" <<'PY'
import sys,json
sub=sys.argv[1]; ids=set(sys.argv[2:])
p=f"/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/{sub}.posts.jsonl"
for l in open(p):
    d=json.loads(l)
    if d.get('id') in ids:
        print('##',d['id'],d.get('title','')[:80],'|',(d.get('selftext') or '')[:int(900)].replace('\n',' '))
PY
