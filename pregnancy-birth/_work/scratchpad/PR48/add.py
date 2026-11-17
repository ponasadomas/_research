# usage: python3 -I add.py batch.py  -> appends records to voice file with next ids
import json, sys, re, os, runpy
NICHE = '/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth'
VOICE = NICHE + '/voice/reddit-pr48.jsonl'
UNITS = '../_shared/_raw/reddit-2026/units/'
def meta(unit):
    path = os.path.join(NICHE, UNITS + unit + '.txt')
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'^POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)', txt, re.M)
    post = dict(id=m.group(1), sub=m.group(2), date=m.group(3), url=m.group(4))
    com = {}
    for c in re.finditer(r'^COMMENT (\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)', txt, re.M):
        com[c.group(1)] = (c.group(2), c.group(3))
    return post, com
recs = runpy.run_path(sys.argv[1])['R']
n = sum(1 for l in open(VOICE) if l.strip()) if os.path.exists(VOICE) else 0
out = open(VOICE, 'a', encoding='utf-8')
for r in recs:
    unit, cid, speaker, stage, typ, themes, quote, context = r[:8]
    restricted = len(r) > 8 and r[8]
    post, com = meta(unit)
    n += 1
    d = {'id': 'pb48-%04d' % n, 'source': 'reddit r/' + post['sub']}
    if cid:
        d['url'], d['date'] = com[cid][1], com[cid][0]
    else:
        d['url'], d['date'] = post['url'], post['date']
    d.update(speaker=speaker, stage=stage, type=typ, themes=themes, quote=quote, context=context,
             raw_file=UNITS + unit + '.txt', source_class='reddit_archive', post_id=post['id'])
    if cid: d['comment_id'] = cid
    if restricted: open(NICHE+'/scratchpad/PR48/restricted.txt','a').write(d['id']+'\n')
    out.write(json.dumps(d, ensure_ascii=False) + '\n')
    print(d['id'], unit, (cid or ''), 'R' if restricted else '')
