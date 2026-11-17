# usage: python3 -I add.py batchfile.py  -- batchfile defines R = [ (unit, cid, speaker, stage, type, themes, quote, context, restricted), ...]
import json, re, sys, os
BASE = "/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-mother"
VOICE = BASE + "/voice/reddit-mr05.jsonl"
RESTR = BASE + "/scratchpad/MR05/restricted.txt"
ns = {}
exec(open(sys.argv[1]).read(), ns)
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = open(VOICE, "a"); ro = open(RESTR, "a")
for (unit, cid, sp, st, ty, th, q, ctx, rs) in ns["R"]:
    rf = "../_shared/_raw/reddit-2026/units/%s.txt" % unit
    txt = open(os.path.join(BASE, rf), encoding="utf-8").read()
    sub, pid = unit.split("-", 1)
    if cid:
        m = re.search(r"COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)" % cid, txt)
    else:
        m = re.search(r"POST %s \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)" % pid, txt)
    assert m, (unit, cid)
    if cid: date, url = m.group(1), m.group(2)
    else: sub, date, url = m.group(1), m.group(2), m.group(3)
    msub = re.search(r"\| r/(\S+) \|", txt); sub = msub.group(1)
    assert len(ctx.split()) <= 25, ctx
    n += 1
    i = "sm05-%04d" % n
    r = dict(id=i, source="reddit r/" + sub, url=url, date=date, speaker=sp, stage=st, type=ty, themes=th, quote=q, context=ctx, raw_file=rf, source_class="reddit_archive", post_id=pid)
    if cid: r["comment_id"] = cid
    out.write(json.dumps(r, ensure_ascii=False) + "\n")
    if rs: ro.write(i + "\t" + rs + "\n")
    print(i, unit, cid or "")
