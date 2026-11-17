#!/usr/bin/env python3
"""Append quotes. Input lines: unit ¦ cid(-) ¦ speaker ¦ stage ¦ type ¦ themes,comma ¦ R or - ¦ quote ¦ context"""
import sys, json, re, os, html
B = os.path.dirname(os.path.abspath(__file__))
PB = os.path.normpath(os.path.join(B, '..', '..'))
OUT = os.path.join(PB, 'voice', 'reddit-pr49.jsonl')
RES = os.path.join(B, 'restricted.txt')
def norm(s): return re.sub(r"\s+", " ", html.unescape(s)).strip()
n = 0
if os.path.exists(OUT):
    n = sum(1 for l in open(OUT) if l.strip())
recs = []; bad = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line.strip(): continue
    p = [x.strip() for x in line.split('¦')]
    if len(p) != 9: print('BADLINE', line[:80]); bad += 1; continue
    unit, cid, sp, st, ty, th, r, q, ctx = p
    rf = '../_shared/_raw/reddit-2026/units/%s.txt' % unit
    txt = open(os.path.join(PB, rf), encoding='utf-8').read()
    m = re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt, re.M)
    pid, sub, date, url = m.groups()
    if cid != '-':
        mc = re.search(r'^COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)' % re.escape(cid), txt, re.M)
        if not mc: print('NOCID', cid); bad += 1; continue
        date, url = mc.groups()
    nt = norm(txt); pos = 0; ok = True
    for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", q):
        piece = norm(piece)
        if not piece: continue
        at = nt.find(piece, pos)
        if at < 0: ok = False; break
        pos = at + len(piece)
    if not ok: print('NOTFOUND', unit, q[:70]); bad += 1; continue
    if len(ctx.split()) > 25: print('CTXLONG', ctx); bad += 1; continue
    recs.append((r, dict(source='reddit r/'+sub, url=url, date=date, speaker=sp, stage=st, type=ty,
        themes=[t.strip() for t in th.split(',') if t.strip()], quote=q, context=ctx, raw_file=rf,
        source_class='reddit_archive', post_id=pid, **({'comment_id': cid} if cid != '-' else {}))))
if bad: print('ABORT, nothing written', bad); sys.exit(1)
with open(OUT, 'a') as f, open(RES, 'a') as fr:
    for r, d in recs:
        n += 1; d = {'id': 'pb49-%04d' % n, **d}
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
        if r == 'R': fr.write(d['id'] + '\n')
print('wrote', len(recs), 'last', 'pb49-%04d' % n)
