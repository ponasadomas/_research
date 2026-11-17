import json, re, os, sys, html, glob
NICHE = "/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth"
UNITS = "../_shared/_raw/reddit-2026/units/"
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
def blocks(path):
    txt = open(os.path.join(NICHE, path), encoding="utf-8").read()
    parts = re.split(r"(?m)^(?=POST |COMMENT )", txt)
    out = []
    for p in parts:
        m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", p)
        if m:
            out.append(dict(kind="post", pid=m.group(1), sub=m.group(2), date=m.group(3), url=m.group(4), text=norm(p))); continue
        m = re.match(r"COMMENT (\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", p)
        if m:
            out.append(dict(kind="comment", cid=m.group(1), date=m.group(2), url=m.group(3), text=norm(p)))
    return out
recs = []; restricted = []
n = 0
for bf in sorted(glob.glob(os.path.join(NICHE, "scratchpad/PR47/batch*.py"))):
    ns = {}
    exec(open(bf, encoding="utf-8").read(), ns)
    for r in ns["R"]:
        unit, sp, st, ty, th, q, ctx = r[:7]
        flag = r[7] if len(r) > 7 else ""
        raw = UNITS + unit + ".txt"
        bl = blocks(raw)
        post = bl[0]
        first = norm(re.split(r"\s*\[(?:…|\.\.\.)\]\s*", q)[0])
        hit = [b for b in bl if first in b["text"]]
        if not hit:
            print("NOT FOUND", unit, q[:60]); continue
        b = hit[0]
        n += 1
        rid = "pb47-%04d" % n
        rec = {"id": rid, "source": "reddit r/" + post["sub"], "url": b["url"], "date": b["date"], "speaker": sp, "stage": st, "type": ty,
               "themes": [t.strip() for t in th.split(",") if t.strip()], "quote": q, "context": ctx, "raw_file": raw,
               "source_class": "reddit_archive", "post_id": post["pid"]}
        if b["kind"] == "comment": rec["comment_id"] = b["cid"]
        if len(ctx.split()) > 25: print("LONG CONTEXT", rid)
        recs.append(rec)
        if flag == "R": restricted.append(rid)
with open(os.path.join(NICHE, "voice/reddit-pr47.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
open(os.path.join(NICHE, "scratchpad/PR47/restricted.txt"), "w").write("\n".join(restricted) + "\n")
print(len(recs), "records,", len(restricted), "restricted")
