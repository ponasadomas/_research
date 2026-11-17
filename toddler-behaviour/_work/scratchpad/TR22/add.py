#!/usr/bin/env python3
"""Append records. JSON lines on stdin: {"u","c","sp","st","ty","th","q","cx","r"(optional restricted)}. Checks quote before writing."""
import json, sys, os, re, html
ROOT = "/home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour"
OUT = os.path.join(ROOT, "voice/reddit-tr22.jsonl")
RES = os.path.join(ROOT, "scratchpad/TR22/restricted.txt")
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
n = sum(1 for l in open(OUT) if l.strip()) if os.path.exists(OUT) else 0
recs = []; res = []; bad = 0
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    e = json.loads(line)
    rf = "../_shared/_raw/reddit-2026/units/%s.txt" % e["u"]
    txt = open(os.path.join(ROOT, rf), encoding="utf-8").read()
    nt = norm(txt); pos = 0
    for piece in e["q"].split(" […] "):
        i = nt.find(norm(piece), pos)
        if i < 0: print("QUOTE FAIL", e["u"], piece[:70]); bad += 1; break
        pos = i + len(norm(piece))
    sub, pid = e["u"].rsplit("-", 1)
    m = re.search(r"^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)", txt, re.M)
    date, url = m.group(3), m.group(4)
    c = e.get("c") or ""
    if c:
        m2 = re.search(r"^COMMENT %s \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)" % re.escape(c), txt, re.M)
        if not m2: sys.exit("no comment %s in %s" % (c, e["u"]))
        date, url = m2.group(1), m2.group(2)
    if len(e["cx"].split()) > 25: print("CONTEXT LONG", e["cx"]); bad += 1
    recs.append((e, {"source": "reddit r/%s" % m.group(2), "url": url, "date": date,
         "speaker": e["sp"], "stage": e["st"], "type": e["ty"], "themes": e["th"], "quote": e["q"],
         "context": e["cx"], "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}, c))
if bad: sys.exit("aborted, nothing written")
with open(OUT, "a", encoding="utf-8") as f, open(RES, "a") as rr:
    for e, r, c in recs:
        n += 1
        r = {"id": "tb22-%04d" % n, **r}
        if c: r["comment_id"] = c
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
        if e.get("r"): rr.write(r["id"] + "\t" + e["u"] + "\n")
print("wrote", len(recs), "last", "tb22-%04d" % n)
