# Build voice/reddit-dr04.jsonl from staged.jsonl (u, c, sp, st, t, th, q, cx, r)
import json, re, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
st = [json.loads(l) for l in open(os.path.join(D, "scratchpad/DR04/staged.jsonl")) if l.strip()]
out, restricted = [], []
for i, s in enumerate(st, 1):
    rf = "../_shared/_raw/reddit-2026/units/%s.txt" % s["u"]
    txt = open(os.path.join(D, rf), encoding="utf-8").read()
    m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
    pid, sub, date, url = m.groups()
    rec = {"id": "dv04-%04d" % i, "source": "reddit r/" + sub}
    if s.get("c"):
        cm = re.search(r"COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)" % s["c"], txt)
        assert cm, s
        date, url = cm.group(1), cm.group(2)
    rec.update(url=url, date=date, speaker=s["sp"], stage=s["st"], type=s["t"], themes=s["th"],
               quote=re.sub(r"\s+", " ", s["q"]).strip(), context=s["cx"], raw_file=rf, source_class="reddit_archive", post_id=pid)
    if s.get("c"): rec["comment_id"] = s["c"]
    assert len(s["cx"].split()) <= 25, s["cx"]
    out.append(rec)
    if s.get("r"): restricted.append(rec["id"])
with open(os.path.join(D, "voice/reddit-dr04.jsonl"), "w") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
open(os.path.join(D, "scratchpad/DR04/restricted.txt"), "w").write("\n".join(restricted) + "\n")
print(len(out), "records;", len(restricted), "restricted")
