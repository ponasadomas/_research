# usage: python3 -I build.py entries1.py entries2.py ... -> writes voice/reddit-r19.jsonl
import sys, re, json, os
BASE = "/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby"
UP = "../_shared/_raw/reddit-2026/units/"
out = []
n = 0
for f in sys.argv[1:]:
    ns = {}
    exec(open(f).read(), ns)
    for e in ns["E"]:
        unit, cid, spk, stg, typ, th, q, ctx = e
        rf = UP + unit + ".txt"
        txt = open(os.path.join(BASE, rf), encoding="utf-8").read()
        sub = unit.split("-")[0]
        m = re.search(r"^POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d).*?\| (\S+)$", txt, re.M)
        pid, date, url = m.group(1), m.group(3), m.group(4)
        rec = {}
        if cid:
            mc = re.search(r"^COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)$", txt, re.M)
            date, url = mc.group(1), mc.group(2)
        assert len(ctx.split()) <= 25, ctx
        n += 1
        rec = {"id": "sb19-%04d" % n, "source": "reddit r/" + m.group(2), "url": url, "date": date,
               "speaker": spk, "stage": stg, "type": typ, "themes": th, "quote": q, "context": ctx,
               "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
        if cid: rec["comment_id"] = cid
        out.append(rec)
with open(os.path.join(BASE, "voice/reddit-r19.jsonl"), "w") as fh:
    for r in out: fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(out))
