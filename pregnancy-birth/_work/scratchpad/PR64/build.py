import json, re, glob, os, sys, importlib.util
NB = '/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth'
SP = NB + '/scratchpad/PR64'
UD = '../_shared/_raw/reddit-2026/units/'
recs = []; restricted = []; withdrawn = []; n = 0
for f in sorted(glob.glob(SP + '/c*.py')):
    spec = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for r in m.R:
        unit, cid, spk, stg, typ, th, q, ctx, rs = r
        raw = UD + unit + '.txt'
        txt = open(os.path.join(NB, raw), encoding='utf-8').read()
        sub = unit.split('-')[0]; pid = unit.split('-', 1)[1]
        if cid:
            mm = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        else:
            mm = re.search(r'POST ' + pid + r' \| [^|]*\| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        assert mm, (unit, cid)
        assert len(ctx.split()) <= 25, ctx
        n += 1; i = 'pb64-%04d' % n
        if rs == 2:
            withdrawn.append(i); continue
        d = {'id': i, 'source': 'reddit r/' + sub, 'url': mm.group(2), 'date': mm.group(1), 'speaker': spk, 'stage': stg,
             'type': typ, 'themes': th, 'quote': q, 'context': ctx, 'raw_file': raw, 'source_class': 'reddit_archive', 'post_id': pid}
        if cid: d['comment_id'] = cid
        recs.append(d)
        if rs: restricted.append(i)
with open(NB + '/voice/reddit-pr64.jsonl', 'w', encoding='utf-8') as o:
    for d in recs: o.write(json.dumps(d, ensure_ascii=False) + '\n')
open(SP + '/restricted.txt', 'w').write(', '.join(restricted) + '\n')
open(SP + '/withdrawn.txt', 'w').write(', '.join(withdrawn) + '\n')
print(len(recs), 'records;', len(restricted), 'restricted')
