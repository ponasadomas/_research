"""Append compact quote inputs to the PR08 voice file. Usage: python3 -I add.py qNNN.jsonl
Input keys: u (unit stem), c (comment id or absent), sp, st, ty, th, q, cx, r (restriction reason, optional)."""
import json, sys, os, re
NICHE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
VOICE = os.path.join(NICHE, "voice", "reddit-pr08.jsonl")
RESTR = os.path.join(NICHE, "scratchpad", "PR08", "restricted.txt")
def meta(stem):
    p = os.path.join(NICHE, "..", "_shared", "_raw", "reddit-2026", "units", stem + ".txt")
    t = open(p, encoding="utf-8").read()
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t)
    com = {c: (d, u) for c, d, u in re.findall(r"^COMMENT (\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t, re.M)}
    return m.groups(), com, t
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = open(VOICE, "a"); ro = open(RESTR, "a")
for line in open(sys.argv[1]):
    if not line.strip(): continue
    r = json.loads(line)
    (pid, sub, pdate, purl), com, text = meta(r["u"])
    n += 1
    rec = {"id": f"pb08-{n:04d}", "source": f"reddit r/{sub}"}
    if r.get("c"):
        d, u = com[r["c"]]; rec.update(url=u, date=d)
    else:
        rec.update(url=purl, date=pdate)
    assert len(r["cx"].split()) <= 25, r["cx"]
    rec.update(speaker=r["sp"], stage=r["st"], type=r["ty"], themes=r["th"], quote=r["q"], context=r["cx"],
               raw_file=f"../_shared/_raw/reddit-2026/units/{r['u']}.txt", source_class="reddit_archive", post_id=pid)
    if r.get("c"): rec["comment_id"] = r["c"]
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if r.get("r"): ro.write(f"{rec['id']}\t{r['r']}\n")
    print(rec["id"], r["u"], r.get("c",""))
