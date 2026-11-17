#!/usr/bin/env python3
"""For the id groups cited in findings 10.1, 10.2 and 10.4: how many come from posts also quoted in ../sleep-baby."""
import json, re, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..','..'))
def pid(r):
    m=re.search(r'/comments/([a-z0-9]+)',r.get('url','')); return r.get('post_id') or (m.group(1) if m else None)
sm={json.loads(l)['id']:json.loads(l) for l in open(os.path.join(ROOT,'sleep-mother','voice-merged','all.jsonl')) if l.strip()}
sbp={pid(json.loads(l)) for l in open(os.path.join(ROOT,'sleep-baby','voice-merged','all.jsonl')) if l.strip()}
groups={'10.1':'sm01-0068 sm01-0069 sm02-0171 sm02-0172 sm02-0173 sm03-0128 sm03-0315 sm03-0083 sm02-0289 sm02-0108 sm03-0281 sm03-0215 sm03-0216 sm03-0171',
'10.2':'sm03-0325 sm03-0326 sm03-0327 sm02-0291 sm01-0141 sm01-0162 sm03-0147 sm01-0161 sm03-0044 sm02-0024 sm02-0248 sm03-0115 sm02-0122 sm02-0243 sm02-0246 sm03-0186 sm03-0240',
'10.4':'sm01-0155 sm02-0126 sm03-0003 sm03-0207 sm03-0319 sm02-0044 sm02-0018 sm03-0182 sm02-0103 sm02-0152 sm03-0088 sm03-0175 sm03-0330'}
for g,ids in groups.items():
    ids=ids.split(); s=[i for i in ids if pid(sm[i]) in sbp]
    print(g,'ids',len(ids),'restricted',sum(1 for i in ids if sm[i].get('restricted')),'from shared posts',len(s),' '.join(s))
