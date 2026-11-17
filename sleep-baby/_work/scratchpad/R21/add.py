# usage: python3 -I add.py specfile.json  -> appends to voice file
# spec: list of [unit_basename, comment_id or "", speaker, stage, type, themes(list), quote, context]
import json, sys, re, os, ast
SB = "/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby"
VOICE = SB + "/voice/reddit-r21.jsonl"
specs = ast.literal_eval(open(sys.argv[1]).read())
existing = [json.loads(l) for l in open(VOICE)] if os.path.exists(VOICE) else []
n = len(existing)
out = open(VOICE, "a")
for s in specs:
    unit, cid, speaker, stage, typ, themes, quote, context = s
    raw_file = "../_shared/_raw/reddit-2026/units/%s.txt" % unit
    txt = open(os.path.join(SB, raw_file), encoding="utf-8").read()
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)", txt)
    pid, sub, date, url = m.groups()
    rec = {}
    if cid:
        mc = re.search(r"COMMENT %s \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)" % re.escape(cid), txt)
        assert mc, (unit, cid)
        date, url = mc.groups()
    n += 1
    rec = {"id": "sb21-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date,
           "speaker": speaker, "stage": stage, "type": typ, "themes": themes, "quote": quote,
           "context": context, "raw_file": raw_file, "source_class": "reddit_archive", "post_id": pid}
    if cid: rec["comment_id"] = cid
    assert len(context.split()) <= 25, context
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
print("total", n)
