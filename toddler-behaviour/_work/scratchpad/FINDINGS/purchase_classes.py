#!/usr/bin/env python3
"""Hand classification of every quote with type=purchase in voice-merged/all.jsonl (checks coverage)."""
import json,os,collections
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
P={json.loads(l)['id'] for l in open(os.path.join(ROOT,'voice-merged','all.jsonl')) if l.strip() and json.loads(l)['type']=='purchase'}
C={
'course, consultant or coach (paid program or human)':'tb01-0008 tb01-0064 tb08-0282 tb09-0168',
'book or audiobook (parent or picture book)':'tb01-0022 tb02-0103 tb02-0219 tb03-0270 tb04-0151 tb04-0198 tb05-0154 tb06-0115 tb07-0054 tb09-0160 tb09-0217 tb09-0237',
'gear or product (potties, seats, undies, pull-ups, rewards, stickers, timers, chewlery, toys)':'tb01-0034 tb01-0111 tb03-0020 tb03-0128 tb03-0170 tb03-0181 tb03-0195 tb03-0215 tb04-0046 tb04-0077 tb04-0235 tb04-0240 tb04-0279 tb05-0094 tb05-0228 tb05-0230 tb05-0244 tb07-0071 tb07-0130 tb07-0175 tb07-0340 tb08-0101 tb08-0107 tb08-0152 tb08-0192 tb08-0195 tb08-0219 tb08-0278 tb08-0284 tb09-0190 tb09-0205 tb09-0220 tb09-0250 tb09-0255 tb09-0274',
'childcare (tuition, nanny)':'tb08-0173 tb09-0270'}
seen=[i for v in C.values() for i in v.split()]
assert len(seen)==len(set(seen)) and set(seen)==P, (set(seen)^P)
print('purchase-type quotes',len(P))
for k,v in C.items(): print(len(v.split()),'|',k)
