#!/usr/bin/env python3
"""Expand short-form R49 records (scratchpad/R49/q*.jsonl) into voice/reddit-r49.jsonl.
Short form: {"u": "<sub>-<postid>", "c": "<comment id or empty>", "sp","st","ty","th":[...],"q","x"(context)}"""
import json, re, glob, os
SEED = set("night_wakings contact_naps short_naps wake_windows early_waking bedtime_battle regression_4_month feeding_to_sleep dream_feed night_weaning cosleeping bedsharing room_sharing transition_to_cot sleep_training_values cry_it_out ferber gentle_method chair_method pick_up_put_down consistency_failure partner_split_nights partner_disagreement daycare_naps nap_transition drop_nap sleep_props pacifier swaddle_transition white_noise schedule_rigidity sleep_consultant course_purchase app_tracking information_overload conflicting_advice maternal_exhaustion resentment guilt comparison_other_babies safe_sleep_fear money_back price_value personalization".split())
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
units = [l.strip() for l in open(os.path.join(D, "scratchpad/R49/paths.txt")) if l.strip()]
bykey = {os.path.basename(u)[:-4]: u for u in units}
out = []
restricted = []
n = 0
for f in sorted(glob.glob(os.path.join(D, "scratchpad/R49/q*.jsonl"))):
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
        rec["id"] = f"sb49-{n:04d}"
        rec["source"] = f"reddit r/{sub}"
        if r.get("c"):
            cm = re.search(r"^COMMENT " + re.escape(r["c"]) + r" \| (\d{4}-\d{2}-\d{2}) [^|]*\| (\S+)", text, re.M)
            date, url = cm.group(1), cm.group(2)
        rec.update({"url": url, "date": date, "speaker": r["sp"], "stage": r["st"], "type": r["ty"],
                    "themes": [t for t in r["th"] if t in SEED] + [t for t in r["th"] if t not in SEED], "quote": r["q"], "context": r["x"], "raw_file": raw,
                    "source_class": "reddit_archive", "post_id": pid})
        if r.get("c"):
            rec["comment_id"] = r["c"]
        out.append(rec)
        if r.get("r"): restricted.append(rec["id"])
with open(os.path.join(D, "voice/reddit-r49.jsonl"), "w") as w:
    for rec in out:
        w.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(len(out), "records")
print("restricted:", " ".join(restricted))
