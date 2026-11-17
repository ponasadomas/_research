#!/usr/bin/env python3
"""Append records from a ' || '-separated batch file to the PR18 voice file.
Line: unit || cid|- || speaker || stage || type || themes,comma || quote || context || restricted-reason|-"""
import json, sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.join(HERE, "..", "..")
VOICE = os.path.join(NICHE, "voice", "reddit-pr18.jsonl")
RESTR = os.path.join(HERE, "restricted.tsv")
SPK = {"expecting_mother","new_mother","experienced_mother","recovered_parent","parent_unspecified","partner","relative_caregiver","advisor","professional","reviewer","skeptic","gave_up_parent"}
STG = {"trying","first_trimester","second_trimester","third_trimester","birth","newborn_0_2_weeks","newborn_2_8_weeks","second_pregnancy","looking_back","unknown"}
TYP = {"trigger_moment","pain","fear","tried_failed","desire","belief","question","objection","advice_given","success_story","failure_story","regret","others_said","purchase","price_signal"}
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = []
restr = []
for ln, line in enumerate(open(sys.argv[1]), 1):
    line = line.rstrip("\n")
    if not line.strip() or line.startswith("#"):
        continue
    f = [x.strip() for x in line.split(" || ")]
    assert len(f) == 9, (ln, len(f), line[:80])
    unit, cid, spk, stg, typ, th, q, ctx, rr = f
    assert spk in SPK and stg in STG and typ in TYP, (ln, spk, stg, typ)
    assert len(ctx.split()) <= 25, (ln, "context too long")
    raw_file = f"../_shared/_raw/reddit-2026/units/{unit}.txt"
    text = open(os.path.join(NICHE, raw_file), encoding="utf-8").read()
    m = re.match(r"POST (\w+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", text)
    pid, sub, date, url = m.groups()
    rec = {}
    if cid != "-":
        mc = re.search(r"^COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", text, re.M)
        assert mc, (ln, cid)
        date, url = mc.groups()
    n += 1
    rid = f"pb18-{n:04d}"
    rec = {"id": rid, "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": spk, "stage": stg,
           "type": typ, "themes": [t.strip() for t in th.split(",") if t.strip()], "quote": q, "context": ctx,
           "raw_file": raw_file, "source_class": "reddit_archive", "post_id": pid}
    if cid != "-":
        rec["comment_id"] = cid
    out.append(rec)
    if rr != "-":
        restr.append(f"{rid}\t{rr}\n")
with open(VOICE, "a") as fh:
    for r in out:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(RESTR, "a") as fh:
    fh.writelines(restr)
print(f"added {len(out)}; total {n}; restricted +{len(restr)}")
