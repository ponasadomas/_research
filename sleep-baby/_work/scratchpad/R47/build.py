#!/usr/bin/env python3
import json, re, glob, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
units = [l.strip() for l in open(os.path.join(D, "scratchpad/R47/units.txt")) if l.strip()]
bykey = {os.path.basename(u)[:-4]: u for u in units}
out = []; restricted = []; promo = []
n = 0
for f in sorted(glob.glob(os.path.join(D, "scratchpad/R47/q*.jsonl"))):
    for line in open(f):
        if not line.strip():
            continue
        r = json.loads(line)
        raw = bykey[r["u"]]
        text = open(os.path.join(D, raw), encoding="utf-8").read()
        m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d{2}-\d{2}) [^|]*\| (\S+)", text)
        pid, sub, date, url = m.groups()
        n += 1
        rec = {"id": f"sb47-{n:04d}", "source": f"reddit r/{sub}"}
        if r.get("c"):
            cm = re.search(r"^COMMENT " + re.escape(r["c"]) + r" \| (\d{4}-\d{2}-\d{2}) [^|]*\| (\S+)", text, re.M)
            date, url = cm.group(1), cm.group(2)
        rec.update({"url": url, "date": date, "speaker": r["sp"], "stage": r["st"], "type": r["ty"],
                    "themes": r["th"], "quote": r["q"], "context": r["x"], "raw_file": raw,
                    "source_class": "reddit_archive", "post_id": pid})
        if r.get("c"):
            rec["comment_id"] = r["c"]
        if r.get("r"): restricted.append(rec["id"])
        if "possible_promo" in r["th"]: promo.append(rec["id"])
        out.append(rec)
with open(os.path.join(D, "voice/reddit-r47.jsonl"), "w") as w:
    for rec in out:
        w.write(json.dumps(rec, ensure_ascii=False) + "\n")
open(os.path.join(D, "scratchpad/R47/restricted.txt"), "w").write("\n".join(restricted) + "\n")
open(os.path.join(D, "scratchpad/R47/promo.txt"), "w").write("\n".join(promo) + "\n")
print(len(out), "records;", len(restricted), "restricted;", len(promo), "promo")
