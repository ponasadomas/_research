#!/usr/bin/env python3
"""Per-unit reading ledger for RV1 -> _raw/reviews/reading-ledger-rv1.tsv and counts JSON."""
import json, glob, os, re, collections
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
q = [json.loads(l) for l in open(os.path.join(ROOT, 'voice/reviews-rv1.jsonl'))]
byrid = collections.defaultdict(list)
for r in q: byrid[r['review_id']].append(r['id'])
EXCL = {}
for k in ['babycenter-us-9372999702','babycenter-au-6976876200','wte-ca-3487264929','wte-ca-4961349853','wte-gb-6172451165','wte-us-7856022642','ovia-us-4041881153','ovia-ca-5522268466','pregnancyplus-us-12191983467','pregnancyplus-au-7161691234','pregnancyplus-au-7246069012','googleplay-thebump-1']:
    EXCL[k] = 'not quoted: centred on pregnancy loss (README line)'
for k in ['flo-us-4482435400','flo-gb-12671146522','flo-ca-2941096917','flo-au-8851443877','flo-au-4935944406']:
    EXCL[k] = 'not quoted: reviewer is or may be a minor'
for k in ['pregnancyplus-ca-7916851025','pregnancyplus-ca-1661511380','pregnancyplus-ca-14493396927']:
    EXCL[k] = 'not quoted: non-English'
units = []
for f in sorted(glob.glob(os.path.join(ROOT, '_raw/reviews/*.units.json'))):
    d = json.load(open(f))
    for r in d['reviews']:
        units.append((f"App Store {d['country']} {d['app']}", f"{d['app']}-{d['country']}-{r['id']}", d['corpus_file']))
gp = {'babycenter':3,'christianhypno':3,'everymother':3,'flo':3,'freya':3,'gentlebirth':3,'ovia':3,'pregnancyplus':3,'thebump':3,'wte':3}
for a, n in gp.items():
    for i in range(1, n+1): units.append((f"Google Play {a}", f"googleplay-{a}-{i}", f"_raw/reviews/googleplay-{a}.txt"))
for f in sorted(glob.glob(os.path.join(ROOT, '_raw/books/barnes-*-corpus.txt'))):
    for m in re.finditer(r'^REVIEW (\S+)', open(f).read(), re.M):
        units.append((f"Barnes & Noble {os.path.basename(f)[7:-11]}", m.group(1), os.path.relpath(f, ROOT)))
for f in sorted(glob.glob(os.path.join(ROOT, '_raw/books/apple-*.txt'))):
    t = open(f).read()
    m = re.search(r'## Customer Reviews\n(.*?)\n##\s*\n', t, re.S)
    if not m: continue
    n = len(re.findall(r'^###$', m.group(1), re.M))
    pg = os.path.basename(f)[6:-4]
    for i in range(1, n+1): units.append((f"Apple Books {pg}", f"applebooks-{pg}-{i}", os.path.relpath(f, ROOT)))
out = os.path.join(ROOT, '_raw/reviews/reading-ledger-rv1.tsv')
cnt = collections.OrderedDict()
with open(out, 'w') as o:
    o.write('source\tunit\traw_file\tstatus\tquote_ids\tnote\n')
    for src, u, rf in units:
        ids = byrid.get(u, [])
        note = 'quoted' if ids else EXCL.get(u, 'not quoted: generic, redundant or off-niche (period/fertility tracking, bugs)')
        o.write(f"{src}\t{u}\t{rf}\tfull_read\t{','.join(ids)}\t{note}\n")
        c = cnt.setdefault(src, [0, 0, 0]); c[0] += 1; c[1] += 1; c[2] += len(ids)
missing = set(byrid) - {u for _, u, _ in units}
print('units', len(units), 'quotes', len(q), 'quote review_ids not in ledger:', missing)
json.dump(cnt, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'counts.json'), 'w'), indent=1)
for k, v in cnt.items(): print(k, v)
