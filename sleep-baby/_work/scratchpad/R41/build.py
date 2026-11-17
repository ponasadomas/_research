#!/usr/bin/env python3
"""Expand short-form R41 records (scratchpad/R41/q*.jsonl) into voice/reddit-r41.jsonl.
Short form: {"u": "<sub>-<postid>", "c": "<comment id or empty>", "sp","st","ty","th":[...],"q","x"(context)}"""
import json, re, glob, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
units = [l.strip() for l in open(os.path.join(D, "scratchpad/R41/units.txt")) if l.strip()]
bykey = {os.path.basename(u)[:-4]: u for u in units}
out = []
n = 0
for f in sorted(glob.glob(os.path.join(D, "scratchpad/R41/q*.jsonl"))):
    for line in open(f):
        if not line.strip():
            continue
        r = json.loads(line)
        raw = bykey[r["u"]]
        text = open(os.path.join(D, raw), encoding="utf-8").read()
        m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d{2}-\d{2}) [^|]*\| (\S+)", text)
        pid, sub, date, url = m.groups()
        rec = {}
        n += 1
        rec["id"] = f"sb41-{n:04d}"
        rec["source"] = f"reddit r/{sub}"
        if r.get("c"):
            cm = re.search(r"^COMMENT " + re.escape(r["c"]) + r" \| (\d{4}-\d{2}-\d{2}) [^|]*\| (\S+)", text, re.M)
            date, url = cm.group(1), cm.group(2)
        rec.update({"url": url, "date": date, "speaker": r["sp"], "stage": r["st"], "type": r["ty"],
                    "themes": r["th"], "quote": r["q"], "context": r["x"], "raw_file": raw,
                    "source_class": "reddit_archive", "post_id": pid})
        if r.get("c"):
            rec["comment_id"] = r["c"]
        out.append(rec)
with open(os.path.join(D, "voice/reddit-r41.jsonl"), "w") as w:
    for rec in out:
        w.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(len(out), "records")
