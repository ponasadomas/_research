#!/usr/bin/env python3
"""Append records. Input: JSON lines on stdin, each {"u": "sub-id", "c": comment_id or "", "sp","st","ty","th":[...],"q","cx"}."""
import json, sys, os, re
ROOT = "/home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour"
OUT = os.path.join(ROOT, "voice/reddit-tr19.jsonl")
n = 0
if os.path.exists(OUT):
    n = sum(1 for l in open(OUT) if l.strip())
recs = []
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    e = json.loads(line)
    rf = "../_shared/_raw/reddit-2026/units/%s.txt" % e["u"]
    txt = open(os.path.join(ROOT, rf), encoding="utf-8").read()
    sub, pid = e["u"].rsplit("-", 1)
    m = re.search(r"^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)", txt, re.M)
    date, url = m.group(3), m.group(4)
    c = e.get("c") or ""
    if c:
        m2 = re.search(r"^COMMENT %s \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)" % re.escape(c), txt, re.M)
        if not m2: sys.exit("no comment %s in %s" % (c, e["u"]))
        date, url = m2.group(1), m2.group(2)
    n += 1
    r = {"id": "tb19-%04d" % n, "source": "reddit r/%s" % m.group(2), "url": url, "date": date,
         "speaker": e["sp"], "stage": e["st"], "type": e["ty"], "themes": e["th"], "quote": e["q"],
         "context": e["cx"], "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
    if c: r["comment_id"] = c
    if len(e["cx"].split()) > 25: sys.exit("context too long: " + e["cx"])
    import html as H
    def nm(x): return re.sub(r"\s+"," ",H.unescape(x).replace("\\n"," ")).strip()
    T=nm(txt); pos=0
    for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", e["q"]):
        piece=nm(piece)
        if not piece: continue
        at=T.find(piece,pos)
        if at<0: sys.exit("NOT IN SOURCE (%s): %s" % (e["u"], piece[:80]))
        pos=at+len(piece)
    recs.append(r)
with open(OUT, "a", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(recs), "last", recs[-1]["id"] if recs else None)
