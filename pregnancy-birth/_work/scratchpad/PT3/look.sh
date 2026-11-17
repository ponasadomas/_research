#!/bin/zsh
cd /home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026
for id in "$@"; do grep -h "\"id\": *\"$id\"" *.posts.jsonl | head -1 | python3 -I -c "import sys,json
for l in sys.stdin:
  d=json.loads(l);print('##',d['id'],d.get('title'),'|',(d.get('selftext') or '')[:int(900)].replace('\n',' '))"; done
