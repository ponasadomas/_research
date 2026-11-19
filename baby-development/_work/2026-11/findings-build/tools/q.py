#!/usr/bin/env python3
"""q.py id [id...]  -> print full quote records (compact) for ids. Reads ids from args or stdin."""
import json,glob,os,sys,csv
Q=os.path.expanduser('~/GitHub/_research/baby-development/quotes')
rec={}
for f in glob.glob(Q+'/reddit-sr*.jsonl'):
    for l in open(f,encoding='utf-8'):
        if l.strip():
            r=json.loads(l); rec[r['id']]=r
posts={}
with open(os.path.expanduser('~/GitHub/_research/baby-development/evidence/2026-11/second-reading/posts.tsv'),encoding='utf-8') as fh:
    for row in csv.DictReader(fh,delimiter='\t'): posts[row['post_id']]=row
ids=sys.argv[1:] or sys.stdin.read().split()
for i in ids:
    r=rec.get(i)
    if not r: print(i,'MISSING'); continue
    p=posts.get(r['post_id'],{})
    print(f"[{i}] {p.get('subreddit','?')}|{p.get('mark','?')}|{p.get('border','')}|{p.get('speaker','')}|{p.get('stage','')}|m{p.get('main_pattern','')} :: {r['quote']}")
