import json, re, sys, os, glob
NB = os.path.dirname(os.path.abspath(__file__)) + "/../.."
os.chdir(NB)
UD = "../_shared/_raw/reddit-2026/units/"
def pat(s):
    out = ""
    for ch in s:
        if ch == "'": out += "[’'‘]"
        elif ch == '"': out += '[“”"]'
        elif ch == " ": out += r"\s+"
        else: out += re.escape(ch)
    return out
entries = []
def Q(unit, cid, sp, st, ty, th, pieces, ctx, r=False):
    entries.append((unit, cid, sp, st, ty, th, pieces, ctx, r))
for f in sorted(glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/q*.py")):
    exec(open(f).read())
recs = []; restricted = []; errs = 0
for n, (unit, cid, sp, st, ty, th, pieces, ctx, r) in enumerate(entries, 1):
    path = UD + unit + ".txt"
    txt = open(path, encoding="utf-8").read()
    head = txt.split("\n", 1)[0]
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*\| (\S+)$", head)
    pid, sub, date, url = m.groups()
    seg = txt
    if cid:
        cm = re.search(r"COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)\n", txt)
        date, url = cm.group(1), cm.group(2)
        rest = txt[cm.end():]
        nx = re.search(r"\nCOMMENT \S+ \| \d{4}", rest)
        seg = rest[:nx.start()] if nx else rest
    else:
        e = txt.find("--- ORIGINAL POSTER")
        seg = txt[:e] if e > 0 else txt
    if isinstance(pieces, str): pieces = [(pieces, "")]
    parts = []; ok = True; pos = 0
    for a, b in pieces:
        p = pat(a) + ((r".*?" + pat(b)) if b else "")
        mm = re.compile(p, re.S).search(seg, pos)
        if not mm:
            print("NOTFOUND", n, unit, cid, a[:50]); ok = False; errs += 1; break
        parts.append(mm.group(0)); pos = mm.end()
    if not ok: continue
    i = len(recs) + 1
    rid = "pb39-%04d" % i
    d = {"id": rid, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": sp, "stage": st,
         "type": ty, "themes": th, "quote": " […] ".join(parts), "context": ctx, "raw_file": path,
         "source_class": "reddit_archive", "post_id": pid}
    if cid: d["comment_id"] = cid
    if len(ctx.split()) > 25: print("LONGCTX", rid, len(ctx.split()))
    recs.append(d)
    if r: restricted.append(rid)
if errs: print("ERRORS", errs); sys.exit(1)
with open("voice/reddit-pr39.jsonl", "w", encoding="utf-8") as f:
    for d in recs: f.write(json.dumps(d, ensure_ascii=False) + "\n")
open(os.path.dirname(os.path.abspath(__file__)) + "/restricted.txt", "w").write("\n".join(restricted) + "\n")
print(len(recs), "records;", len(restricted), "restricted")
