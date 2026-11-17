#!/usr/bin/env python3
"""skim.py file [maxchars]: print lines once (dedup), skipping very short nav lines seen in a global stoplist."""
import sys
seen=set(); out=[]; n=int(sys.argv[2]) if len(sys.argv)>2 else 12000
for l in open(sys.argv[1],encoding='utf-8',errors='replace'):
    l=l.rstrip()
    if not l or l in seen: continue
    seen.add(l); out.append(l[:500])
s="\n".join(out); print(s[:n])
