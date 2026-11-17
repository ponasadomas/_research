import json, re, os
BASE = "/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby"
RECS = []
def R(unit, cid, speaker, stage, typ, themes, quote, context):
    rf = f"../_shared/_raw/reddit-2026/units/{unit}.txt"
    txt = open(os.path.join(BASE, rf), encoding="utf-8").read()
    m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
    pid, sub, date, url = m.groups()
    rec = {"id": None, "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": speaker,
           "stage": stage, "type": typ, "themes": themes, "quote": quote, "context": context,
           "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
    if cid:
        cm = re.search(r"COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
        rec["date"], rec["url"] = cm.group(1), cm.group(2)
        rec["comment_id"] = cid
    assert len(context.split()) <= 25, context
    RECS.append(rec)
