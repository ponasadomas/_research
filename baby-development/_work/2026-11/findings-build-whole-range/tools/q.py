#!/usr/bin/env python3
"""q.py id [id...] -> full quote records with the post's mark, stage, main pattern.  q.py -w 'text' id -> the text widened to whole sentences."""
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from common import *
rec=records(); P=posts()
a=sys.argv[1:]
for i in a:
    r=rec.get(i)
    if not r: print(i,'MISSING'); continue
    p=P.get(r['post_id'],{})
    print(f"[{i}] {p.get('subreddit','?')}|{p.get('mark','?')}|{p.get('border','')}|{p.get('speaker','')}|{p.get('stage','')}|m{p.get('main_pattern','')} :: {r['quote']}")
