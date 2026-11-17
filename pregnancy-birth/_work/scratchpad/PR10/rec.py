# usage: python3 -I rec.py batch.py  -> appends records to voice file
import json, re, sys, os
BASE = "/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth"
VOICE = BASE + "/voice/reddit-pr10.jsonl"
U = "../_shared/_raw/reddit-2026/units/"
def meta(unit, cid):
    txt = open(os.path.join(BASE, U + unit + ".txt"), encoding="utf-8").read()
    m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
    pid, sub, date, url = m.groups()
    if cid:
        c = re.search(r"COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
        date, url = c.groups()
    return pid, sub, date, url
n = sum(1 for l in open(VOICE) if l.strip()) if os.path.exists(VOICE) else 0
recs = []
RS = []
def R(unit, cid, speaker, stage, typ, themes, quote, context, r=None):
    recs.append((unit, cid, speaker, stage, typ, themes, quote, context)); RS.append(r)
import html
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
exec(open(sys.argv[1], encoding="utf-8").read())
bad = 0
for unit, cid, sp, st, ty, th, q, cx in recs:
    meta(unit, cid)
    if len(cx.split()) > 25: print("LONG CONTEXT", cx); bad += 1
    text = norm(open(os.path.join(BASE, U + unit + ".txt"), encoding="utf-8").read()); pos = 0
    for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", q):
        piece = norm(piece)
        if not piece: continue
        at = text.find(piece, pos)
        if at < 0: print("NOT FOUND", unit, piece[:80]); bad += 1; break
        pos = at + len(piece)
if bad: sys.exit("aborted, nothing written")
with open(VOICE, "a", encoding="utf-8") as f:
    rf = open(BASE + "/scratchpad/PR10/restricted.tsv", "a", encoding="utf-8")
    for (unit, cid, sp, st, ty, th, q, cx), r in zip(recs, RS):
        n += 1
        if r: rf.write("pb10-%04d\t%s\n" % (n, r))
        pid, sub, date, url = meta(unit, cid)
        d = {"id": "pb10-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date,
             "speaker": sp, "stage": st, "type": ty, "themes": th, "quote": q, "context": cx,
             "raw_file": U + unit + ".txt", "source_class": "reddit_archive", "post_id": pid}
        if cid: d["comment_id"] = cid
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
        print(d["id"], unit, cid or "")
