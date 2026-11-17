#!/usr/bin/env python3
"""Build voice/reviews-rv1.jsonl from RV1 pick files. Run once; refuses to overwrite."""
import json, os, sys, datetime, importlib.util, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'voice', 'reviews-rv1.jsonl')
if os.path.exists(OUT) and '--force' not in sys.argv:
    sys.exit('refusing to overwrite ' + OUT)
APPNAME = {'huckleberry':'Huckleberry','napper':'Napper','nara':'Nara Baby','glowbaby':'Glow Baby','littleones':'Little Ones','happybaby':'Happy Baby','smartsleepcoach':'Smart Sleep Coach by Pampers'}
GPID = {'nara':'com.naraorganics.nara','glowbaby':'com.glow.android.baby','smartsleepcoach':'com.pg.smartsleepcoach','littleones':'nz.co.littleones.prod','happybaby':'com.aumio.baby'}
BOOK = {'nocry':'The No-Cry Sleep Solution','happysleeper':'The Happy Sleeper','twelvehours':"Twelve Hours' Sleep by Twelve Weeks Old",'hshhc':'Healthy Sleep Habits, Happy Child','momsoncall':'Moms on Call Basic Baby Care 0-6 Months','pls':'Precious Little Sleep','sleeplady':"The Sleep Lady's Good Night, Sleep Tight"}
ABDATE = {'ab-happysleeper-us':'2018-12-07','ab-happysleeper-us#2':'2021-01-12','ab-hshhc-gb':'2011-08-26','ab-momsoncall-us':'2025-08-24','ab-momsoncall-us#2':'2026-10-07','ab-momsoncall-us#3':'2025-05-09','ab-nocry-us':'2021-07-03','ab-nocry-us#2':'2021-04-05','ab-nocry-us#3':'2015-07-26','ab-nocry-gb':'2018-10-08','ab-pls-au':'2026-01-09','ab-twelvehours-us':'2025-12-12'}

def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.P

units = {}
import glob
for f in glob.glob(os.path.join(ROOT, '_raw/reviews/*-reviews.units.json')):
    d = json.load(open(f))
    for r in d['reviews']:
        units[f"{d['app']}-{d['country']}-{r['id']}"] = (d, r)
bn = {f"bn-{u['book']}-{u['review_id']}": u for u in json.load(open(os.path.join(ROOT, '_raw/books/barnes-review-units-rv1.json')))}

def final_url(txt):
    for line in open(os.path.join(ROOT, txt), encoding='utf-8'):
        if line.startswith('FINAL:'): return line.split(':', 1)[1].strip()

def meta(key):
    if key.startswith('gp-'):
        app, shown = key[3:].split('|')
        date = datetime.datetime.strptime(shown, '%B %d, %Y').strftime('%Y-%m-%d')
        return (f"Google Play {APPNAME[app]}", f"https://play.google.com/store/apps/details?id={GPID[app]}&hl=en_US&gl=US", date, f"_raw/reviews/googleplay-{app}.txt", 'app_review')
    if key.startswith('bn-'):
        u = bn[key]; ed = {'twelvehours':'twelvehours'}.get(u['book'], u['book'])
        return (f"Barnes & Noble {BOOK[u['book']]}", final_url(f"_raw/books/barnes-{ed}.txt"), u['date'], f"_raw/books/barnes-{u['book']}-corpus.txt", 'book_review')
    if key.startswith('ab-'):
        base = key.split('#')[0]; _, book, cc = base.split('-')
        txt = f"_raw/books/apple-{book}-{cc}.txt"
        return (f"Apple Books {cc} {BOOK[book]}", final_url(txt), ABDATE[key], txt, 'book_review')
    d, r = units[key]
    return (f"App Store {d['country']} {APPNAME[d['app']]}", d['url'], r['date'][:10], d['corpus_file'], 'app_review')

files = ['picks_huck','picks_napper','picks_nara','picks_glow','picks_lo','picks_hb','picks_gp_books']
n = 0; recs = []; restricted = []
for f in files:
    for key, speaker, stage, typ, themes, quote, ctx, restr in load(f):
        n += 1
        src, url, date, raw, cls = meta(key)
        rid = f"sbr1-{n:04d}"
        assert len(ctx.split()) <= 25, (rid, ctx)
        rec = {'id': rid, 'source': src, 'url': url, 'date': date, 'speaker': 'reviewer', 'segment': {'advisor':'parent_unspecified','professional':'parent_unspecified'}.get(speaker, speaker), 'stage': stage, 'type': typ,
               'themes': themes, 'quote': quote.replace('[...]', '[…]'), 'context': ctx, 'raw_file': raw,
               'source_class': cls, 'review_key': key.split('|')[0] if not key.startswith('gp-') else key}
        if restr: restricted.append((rid, restr, src))
        recs.append(rec)
with open(OUT, 'w', encoding='utf-8') as o:
    for r in recs: o.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(restricted, open(os.path.join(HERE, 'restricted.json'), 'w'), ensure_ascii=False, indent=1)
print(len(recs), 'quotes;', len(restricted), 'restricted')
