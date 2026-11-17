#!/usr/bin/env python3
"""Counts the id groups cited in findings 16.1 (10.1, 10.2, 10.4). Run from sleep-mother/: python3 -I scratchpad/FINDINGS-W2/groups.py"""
import json, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
recs={}
for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8'):
    if l.strip(): r=json.loads(l); recs[r['id']]=r
G={
'10.1':'sm04-0063 sm04-0105 sm04-0107 sm04-0108 sm04-0137 sm04-0138 sm04-0139 sm04-0140 sm04-0141 sm04-0150 sm04-0217 sm04-0229 sm04-0230 sm04-0231 sm04-0256 sm06-0006 sm06-0007 sm06-0008 sm06-0012 sm06-0047 sm06-0084',
'10.2':'sm04-0075 sm04-0076 sm04-0102 sm04-0112 sm04-0113 sm04-0143 sm04-0179 sm04-0242 sm04-0257 sm04-0265 sm04-0277 sm04-0312 sm04-0313 sm05-0038 sm05-0115 sm05-0118 sm05-0183 sm05-0184 sm05-0234 sm05-0235 sm05-0241 sm05-0274 sm06-0019 sm06-0020 sm06-0032 sm06-0112 sm06-0124 sm06-0153 sm06-0205',
'10.4':'sm04-0090 sm04-0204 sm04-0245 sm04-0308 sm04-0318 sm05-0010 sm05-0122 sm05-0144 sm06-0036 sm06-0080 sm06-0113 sm06-0224',
}
for g,ids in G.items():
    ids=ids.split()
    print(g,len(ids),'ids; units',len({recs[i]['post_id'] for i in ids}),'; restricted',[i for i in ids if recs[i]['restricted']])
