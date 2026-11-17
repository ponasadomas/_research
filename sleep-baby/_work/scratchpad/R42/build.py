# build voice file from scratch q-*.jsonl (compact records)
import json, glob, re, os, sys
SB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UN = "../_shared/_raw/reddit-2026/units/"
def meta(u, c):
    t = open(os.path.join(SB, UN + u + ".txt"), encoding="utf-8").read()
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t)
    pid, sub, date, url = m.groups()
    if c:
        mc = re.search(r"COMMENT " + c + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t)
        date, url = mc.groups()
    return pid, sub, date, url
out = []; restricted = []
n = 0
for f in sorted(glob.glob(os.path.join(SB, "scratchpad/R42/q-*.jsonl"))):
    for line in open(f, encoding="utf-8"):
        if not line.strip(): continue
        r = json.loads(line); n += 1
        pid, sub, date, url = meta(r["u"], r.get("c"))
        rid = "sb42-%04d" % n
        rec = {"id": rid, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": r["sp"], "stage": r["st"],
               "type": r["ty"], "themes": r["th"], "quote": r["q"], "context": r["cx"], "raw_file": UN + r["u"] + ".txt",
               "source_class": "reddit_archive", "post_id": pid}
        if r.get("c"): rec["comment_id"] = r["c"]
        assert len(r["cx"].split()) <= 25, (rid, r["cx"])
        out.append(rec)
        if r.get("r"): restricted.append(rid)
with open(os.path.join(SB, "voice/reddit-r42.jsonl"), "w", encoding="utf-8") as w:
    for rec in out: w.write(json.dumps(rec, ensure_ascii=False) + "\n")
open(os.path.join(SB, "scratchpad/R42/restricted.txt"), "w").write("\n".join(restricted) + "\n")
print(len(out), "records;", len(restricted), "restricted")
