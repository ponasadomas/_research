#!/usr/bin/env python3
"""Build voice/reddit-dr03.jsonl from rec_*.py record lists (R = list of dicts).
Keys: u unit basename, c comment id or None, sp speaker, st stage, ty type, th themes, q quote, cx context, r restricted."""
import json, os, re, glob, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DEV = os.path.abspath(os.path.join(HERE, "..", ".."))
UNITS = "../_shared/_raw/reddit-2026/units/"
recs = []
for f in sorted(glob.glob(os.path.join(HERE, "rec_*.py"))):
    ns = {}
    exec(open(f).read(), ns)
    recs += ns["R"]
SEED = "what_to_do_all_day awake_time tummy_time tummy_time_hate floor_play rolling sitting crawling pulling_up walking first_words babbling fine_motor milestone_comparison milestone_anxiety corrected_age pediatrician_checkup cdc_milestones wonder_weeks leaps screen_time toys_too_many montessori play_ideas boredom_mum maternal_guilt not_enough_play container_time baby_classes app_tracking information_overload conflicting_advice reassurance_seeking social_comparison grandparent_comments early_intervention_question personalization price_value".split()
out, restricted = [], []
for i, r in enumerate(recs, 1):
    rid = f"dv03-{i:04d}"
    raw = UNITS + r["u"] + ".txt"
    text = open(os.path.join(DEV, raw), encoding="utf-8").read()
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", text)
    pid, sub, date, url = m.groups()
    rec = {"id": rid, "source": f"reddit r/{sub}"}
    if r.get("c"):
        cm = re.search(r"COMMENT " + r["c"] + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", text)
        if not cm:
            sys.exit(f"comment {r['c']} not in {r['u']}")
        date, url = cm.groups()
    rec.update({"url": url, "date": date, "speaker": r["sp"], "stage": r["st"], "type": r["ty"],
                "themes": [x for x in r["th"] if x in SEED] + [x for x in r["th"] if x not in SEED], "quote": r["q"], "context": r["cx"], "raw_file": raw,
                "source_class": "reddit_archive", "post_id": pid})
    if r.get("c"):
        rec["comment_id"] = r["c"]
    if len(r["cx"].split()) > 25:
        print("long context", rid)
    out.append(rec)
    if r.get("r"):
        restricted.append(rid)
with open(os.path.join(DEV, "voice", "reddit-dr03.jsonl"), "w") as fh:
    for rec in out:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
open(os.path.join(HERE, "restricted.txt"), "w").write("\n".join(restricted) + "\n")
print(len(out), "records,", len(restricted), "restricted")
