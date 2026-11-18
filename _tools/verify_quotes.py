#!/usr/bin/env python3
"""Check that every quote in the quote files appears, word for word, in the raw file it cites.
Decodes JSON (.json, .jsonl) and .gz raw files. A quote may be trimmed with " […] ".
python3 -I _tools/verify_quotes.py <quotes dir or file> [--root DIR]   (run from ~/GitHub/_research)
raw_file in each record is read relative to --root (default: ~/GitHub/_research)."""
import glob, gzip, html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
QARG = os.path.abspath(sys.argv[1])
ROOT = os.path.abspath(sys.argv[sys.argv.index("--root") + 1]) if "--root" in sys.argv else os.path.dirname(HERE)
norm = lambda s: re.sub(r"\s+", " ", html.unescape(s).replace("\\n", " ")).strip()
def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)
cache = {}
def raw(p):
    if p not in cache:
        full = os.path.normpath(os.path.join(ROOT, p))
        if not os.path.isfile(full): cache[p] = None; return None
        t = gzip.open(full, "rt", encoding="utf-8", errors="replace").read() if full.endswith(".gz") else open(full, encoding="utf-8", errors="replace").read()
        parts = []
        if ".jsonl" in full:
            for l in t.split("\n"):
                try: parts.extend(strings(json.loads(l)))
                except Exception: pass
        elif ".json" in full:
            try: parts.extend(strings(json.loads(t)))
            except Exception: pass
        if len(cache) > 3: cache.clear()
        cache[p] = norm(t + "\n" + "\n".join(parts))
    return cache[p]
total = failed = missing = 0
for f in ([QARG] if os.path.isfile(QARG) else sorted(glob.glob(os.path.join(QARG, "*.jsonl")))):
    recs = [json.loads(l) for l in open(f) if l.strip()]; bad = 0
    for r in sorted(recs, key=lambda r: r.get("raw_file", "")):
        t = raw(r.get("raw_file", ""))
        if t is None: missing += 1; bad += 1; continue
        pos = 0; ok = True
        for piece in [x for x in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*", r["quote"]) if x.strip()]:
            k = t.find(norm(piece), pos)
            if k < 0: k = t.find(norm(piece))
            if k < 0: ok = False; break
            pos = k
        if not ok: bad += 1; print(f"  {r['id']} NOT IN SOURCE ({r.get('raw_file')})")
    total += len(recs); failed += bad
    print(f"{os.path.basename(f)}: {len(recs)} quotes, {bad} failed")
print(f"TOTAL {total} quotes, {failed} failed, {missing} with a missing raw file")
sys.exit(1 if failed else 0)
