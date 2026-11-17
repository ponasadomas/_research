import json, re, glob, datetime, sys, runpy
from pathlib import Path
ROOT = Path('/home/thinkpad/GitHub/ads/mamivio.com/research/development')
S = ROOT/'scratchpad/RV1'
NAMES = {'kinedu':'Kinedu','babysparks':'BabySparks','wonderweeks':'The Wonder Weeks','pathways':'Pathways.org','cdc':'CDC Milestone Tracker','lovevery':'Lovevery','bloomie':'Bloomie','littlesteps':'Little Steps','sprouty':'Sprouty'}
PLAY = {'wonderweeks':'org.twisevictory.apps.ex','sprouty':'happy.mom.android'}
app_units = {}
for f in glob.glob(str(ROOT/'_raw/reviews/*-reviews.units.json')):
    m = json.load(open(f))
    for r in m['reviews']:
        app_units[f"{m['app']}-{m['country']}-{r['id']}"] = (m, r)
play = {f"googleplay-{u['app']}-{u['n']}": u for u in json.load(open(ROOT/'_raw/reviews/googleplay-review-units-wonderweeks-sprouty.json'))}
books = {}
for u in json.load(open(ROOT/'_raw/books/barnes-wonder-weeks-review-units.json')):
    books[f"barnes-{u['review_id']}"] = dict(source='Barnes & Noble The Wonder Weeks', url='https://www.barnesandnoble.com/w/?ean='+u['ean'], date=u['date'], rating=u['score'], raw='_raw/books/barnes-wonder-weeks-corpus.txt')
TITLES = {'brain-rules-baby':'Brain Rules for Baby','montessori-baby':'The Montessori Baby','what-to-expect-first-year':'What to Expect the First Year'}
for slug, t in TITLES.items():
    for u in json.load(open(ROOT/f'_raw/books/apple-{slug}-review-units.json')):
        d = u['date']
        if '/' in d: mo, da, yr = d.split('/'); d = f'{yr}-{mo}-{da}'
        books[f"apple-{u['storefront']}-{u['review_id']}"] = dict(source=f"Apple Books {u['storefront']} {t}", url=u['url'], date=d, rating=u['rating'], raw=f'_raw/books/apple-{slug}-corpus.txt')
out = []; restricted = []; n = 0
for i in range(1, 7):
    for rid, typ, themes, stage, quote, ctx, restr in runpy.run_path(str(S/f'q{i}.py'))['Q']:
        n += 1; qid = f'dvr1-{n:04d}'
        if rid in app_units:
            m, r = app_units[rid]
            rec = dict(source=f"App Store {m['country']} {NAMES[m['app']]}", url=m['url'], date=r['date'][:10], raw_file=m['corpus_file'], source_class='app_review', engagement=f"{r['rating']} stars")
        elif rid in play:
            u = play[rid]
            d = datetime.datetime.strptime(u['date'], '%B %d, %Y').strftime('%Y-%m-%d')
            rec = dict(source=f"Google Play {NAMES[u['app']]}", url=f"https://play.google.com/store/apps/details?id={PLAY[u['app']]}&hl=en_US&gl=US", date=d, raw_file=f"_raw/reviews/googleplay-{u['app']}.txt", source_class='app_review', engagement=f"{u['rating']} stars" + (f"; {u['helpful']}" if u['helpful'] else ''))
        elif rid in books:
            b = books[rid]
            rec = dict(source=b['source'], url=b['url'], date=b['date'], raw_file=b['raw'], source_class='book_review', engagement=f"{b['rating']} stars")
        else:
            sys.exit('unknown unit ' + rid)
        full = dict(id=qid, source=rec['source'], url=rec['url'], date=rec['date'], speaker='reviewer', stage=stage, type=typ, themes=themes, quote=quote, context=ctx, raw_file=rec['raw_file'], source_class=rec['source_class'], engagement=rec['engagement'], review_id=rid)
        out.append(full)
        if restr: restricted.append((qid, rid, restr))
vf = ROOT/'voice/reviews-rv1.jsonl'
if vf.exists() and '--force-first-write' not in sys.argv: sys.exit('voice file exists')
vf.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in out))
(S/'restricted.tsv').write_text(''.join(f'{a}\t{b}\t{c}\n' for a, b, c in restricted))
print(len(out), 'quotes', len(restricted), 'restricted', len({r['review_id'] for r in out}), 'units quoted')
