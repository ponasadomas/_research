import json, re, html, sys, os, glob
ROOT = "/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth"
SP = ROOT + "/scratchpad/PR22"
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
def segs(unit):
    rf = f"../_shared/_raw/reddit-2026/units/{unit}.txt"
    txt = open(os.path.join(ROOT, rf), encoding="utf-8").read()
    out = []
    parts = re.split(r"(?m)^(POST \S+ \|.*|COMMENT \S+ \|.*)$", txt)
    for i in range(1, len(parts), 2):
        h = parts[i]; body = parts[i+1]
        m = re.match(r"(POST|COMMENT) (\S+) \| (?:r/(\S+) \| )?(\d{4}-\d\d-\d\d)[^|]*\| (\S+)", h)
        out.append(dict(kind=m.group(1), id=m.group(2), sub=m.group(3), date=m.group(4), url=m.group(5), text=norm(h + " " + body)))
    return rf, out
recs = []
for f in sorted(glob.glob(SP + "/draft*.jsonl")):
    for line in open(f):
        if line.strip(): recs.append(json.loads(line))
out = []; restricted = []; n = 0
for d in recs:
    rf, ss = segs(d["u"])
    first = norm(re.split(r"\s*\[(?:…|\.\.\.)\]\s*", d["q"])[0])
    hit = [s for s in ss if first in s["text"]]
    if not hit:
        print("NOT FOUND", d["u"], d["q"][:70]); continue
    s = hit[0]; post = ss[0]
    n += 1; rid = f"pb22-{n:04d}"
    r = dict(id=rid, source=f"reddit r/{post['sub']}", url=s["url"], date=s["date"], speaker=d["sp"], stage=d["st"], type=d["ty"], themes=d["th"], quote=d["q"], context=d["c"], raw_file=rf, source_class="reddit_archive", post_id=post["id"])
    if s["kind"] == "COMMENT": r["comment_id"] = s["id"]
    if d.get("flag"): r["segment"] = d["flag"]
    if len(d["c"].split()) > 25: print("LONG CONTEXT", rid)
    out.append(r)
    if d.get("r"): restricted.append((rid, d["r"]))
with open(ROOT + "/voice/reddit-pr22.jsonl", "w") as fh:
    for r in out: fh.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(SP + "/restricted.tsv", "w") as fh:
    for a, b in restricted: fh.write(f"{a}\t{b}\n")
with open(SP + "/idmap.tsv", "w") as fh:
    for r in out: fh.write(f"{r['id']}\t{r['raw_file'].split('/')[-1][:-4]}\t{r['type']}\t{','.join(r['themes'])}\t{r['quote'][:60]}\n")
print(len(out), "records;", len(restricted), "restricted")
