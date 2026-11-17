import json, re, sys, os, importlib.util
B = '/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth'
os.chdir(B)
idx = {int(l.split('\t')[0]): l.strip().split('\t')[1] for l in open('scratchpad/PR24/idx.tsv')}
VOICE = 'voice/reddit-pr24.jsonl'
RESTR = 'scratchpad/PR24/restricted.txt'
spec = importlib.util.spec_from_file_location('b', sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
n = sum(1 for l in open(VOICE) if l.strip()) if os.path.exists(VOICE) else 0
out = open(VOICE, 'a'); rf = open(RESTR, 'a')
for e in m.Q:
    u, cid, spk, stg, typ, th, q, ctx = e[:8]; restricted = len(e) > 8 and e[8]
    p = idx[u]; txt = open(p, encoding='utf-8').read()
    hm = re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)', txt)
    pid, sub, date, url = hm.groups()
    if cid:
        cm = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) .*?\| (\S+)', txt)
        date, url = cm.groups()
    assert len(ctx.split()) <= 25, ctx
    n += 1; rid = f'pb24-{n:04d}'
    r = dict(id=rid, source=f'reddit r/{sub}', url=url, date=date, speaker=spk, stage=stg, type=typ, themes=th, quote=q, context=ctx, raw_file=p, source_class='reddit_archive', post_id=pid)
    if cid: r['comment_id'] = cid
    out.write(json.dumps(r, ensure_ascii=False) + '\n')
    if restricted: rf.write(rid + '\n')
    print(rid, u, 'R' if restricted else '', q[:60])
