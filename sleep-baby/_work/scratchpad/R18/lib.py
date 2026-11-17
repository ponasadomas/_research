import json, re, os, sys
SB = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
VOICE = os.path.join(SB, 'voice', 'reddit-r18.jsonl')
U = '../_shared/_raw/reddit-2026/units/'

def meta(unit, cid=None):
    path = U + unit + '.txt'
    txt = open(os.path.join(SB, path), encoding='utf-8').read()
    m = re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
    pid, sub, date, url = m.groups()
    if cid:
        c = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        date, url = c.groups()
    return path, pid, sub, date, url

def next_id():
    if not os.path.exists(VOICE): return 1
    n = [int(json.loads(l)['id'].split('-')[1]) for l in open(VOICE) if l.strip()]
    return max(n) + 1 if n else 1

def add(rows):
    i = next_id()
    with open(VOICE, 'a', encoding='utf-8') as f:
        for r in rows:
            unit, cid, speaker, stage, typ, themes, quote, ctx = r
            assert len(ctx.split()) <= 25, ctx
            path, pid, sub, date, url = meta(unit, cid)
            rec = {'id': 'sb18-%04d' % i, 'source': 'reddit r/' + sub, 'url': url, 'date': date,
                   'speaker': speaker, 'stage': stage, 'type': typ, 'themes': themes, 'quote': quote,
                   'context': ctx, 'raw_file': path, 'source_class': 'reddit_archive', 'post_id': pid}
            if cid: rec['comment_id'] = cid
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
            i += 1
    print('now at', i - 1)
