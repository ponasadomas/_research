# Build voice file from scratch/q-*.jsonl compact records.
# compact: {"u":"sub-postid","c":commentid|null,"sp","st","ty","th":[...],"q","cx","r":0/1}
import json, re, glob, os, sys
TB = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
units = {}
for line in open(os.path.join(TB, "scratchpad/TR13/units.txt")):
    ch, p = line.rstrip("\n").split("\t")
    units[os.path.basename(p)[:-4]] = p
out = []; restricted = []; n = 0
for f in sorted(glob.glob(os.path.join(TB, "scratchpad/TR13/q-*.jsonl"))):
    for line in open(f):
        if not line.strip(): continue
        r = json.loads(line)
        p = units[r["u"]]
        txt = open(os.path.join(TB, p), encoding="utf-8").read()
        m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)", txt)
        pid, sub, date, url = m.groups()
        if r.get("c"):
            cm = re.search(r"COMMENT %s \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)" % r["c"], txt)
            date, url = cm.groups()
        n += 1
        rid = "tb13-%04d" % n
        rec = {"id": rid, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": r["sp"],
               "stage": r["st"], "type": r["ty"], "themes": r["th"], "quote": r["q"], "context": r["cx"],
               "raw_file": p, "source_class": "reddit_archive", "post_id": pid}
        if r.get("c"): rec["comment_id"] = r["c"]
        assert len(r["cx"].split()) <= 25, (rid, r["cx"])
        out.append(rec)
        if r.get("r"): restricted.append(rid)
with open(os.path.join(TB, "voice/reddit-tr13.jsonl"), "w") as fo:
    for rec in out: fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
open(os.path.join(TB, "scratchpad/TR13/restricted.txt"), "w").write("\n".join(restricted) + "\n")
print(n, "records;", len(restricted), "restricted")
