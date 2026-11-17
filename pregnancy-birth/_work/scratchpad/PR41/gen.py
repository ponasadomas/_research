import json, re, html, sys, os
ROOT = "/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth"
sys.path.insert(0, os.path.dirname(__file__))
from rows import ROWS
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
out = []; restricted = []; bad = 0
for i, r in enumerate(ROWS, 1):
    unit, cid, spk, stg, typ, th, q, ctx, R = r
    rf = "../_shared/_raw/reddit-2026/units/%s.txt" % unit
    txt = open(os.path.join(ROOT, rf), encoding="utf-8").read()
    head = txt.splitlines()[0].split(" | ")
    post_id = head[0].split()[1]; sub = head[1]; url = head[3].strip(); date = head[2][:10]
    if cid:
        m = re.search(r"^COMMENT %s \| (\S+) \S+ UTC \| (\S+)" % re.escape(cid), txt, re.M)
        if not m: print("NO COMMENT", i, unit, cid); bad += 1; continue
        date, url = m.group(1), m.group(2)
    t = norm(txt); pos = 0
    for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", q):
        piece = norm(piece)
        at = t.find(piece, pos)
        if at < 0: print("MISS", i, unit, piece[:80]); bad += 1; break
        pos = at + len(piece)
    if len(ctx.split()) > 25: print("CTX LONG", i)
    rid = "pb41-%04d" % i
    d = {"id": rid, "source": "reddit " + sub, "url": url, "date": date, "speaker": spk, "stage": stg,
         "type": typ, "themes": th, "quote": q, "context": ctx, "raw_file": rf,
         "source_class": "reddit_archive", "post_id": post_id}
    if cid: d["comment_id"] = cid
    out.append(d)
    if R: restricted.append((rid, unit, R))
print("rows", len(ROWS), "bad", bad)
if not bad:
    with open(os.path.join(ROOT, "voice/reddit-pr41.jsonl"), "w", encoding="utf-8") as f:
        for d in out: f.write(json.dumps(d, ensure_ascii=False) + "\n")
    with open(os.path.join(os.path.dirname(__file__), "restricted.tsv"), "w") as f:
        for x in restricted: f.write("\t".join(x) + "\n")
