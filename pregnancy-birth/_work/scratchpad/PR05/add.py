#!/usr/bin/env python3
"""Append records from a spec file to the PR05 voice file.
Spec blocks:
@ <unit-stem> | <comment_id or -> | speaker | stage | type | theme1,theme2
Q: quote (multi-line until CX:)
CX: context
"""
import json, sys, os, re
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
VOICE = os.path.join(BASE, "voice", "reddit-pr05.jsonl")
UNITS = os.path.join(BASE, "..", "_shared", "_raw", "reddit-2026", "units")
SP = {"expecting_mother","new_mother","experienced_mother","recovered_parent","parent_unspecified","partner","relative_caregiver","advisor","professional","reviewer","skeptic","gave_up_parent"}
STG = {"trying","first_trimester","second_trimester","third_trimester","birth","newborn_0_2_weeks","newborn_2_8_weeks","second_pregnancy","looking_back","unknown"}
TY = {"trigger_moment","pain","fear","tried_failed","desire","belief","question","objection","advice_given","success_story","failure_story","regret","others_said","purchase","price_signal"}
def main(spec):
    n = sum(1 for l in open(VOICE) if l.strip()) if os.path.exists(VOICE) else 0
    blocks = re.split(r"^@ ", open(spec, encoding="utf-8").read(), flags=re.M)[1:]
    out = []
    for b in blocks:
        head, rest = b.split("\n", 1)
        u, c, sp, st, ty, th = [x.strip() for x in head.split("|")]
        q = rest.split("Q:", 1)[1].split("\nCX:", 1)
        quote = q[0].strip(); ctx = q[1].strip()
        assert sp in SP and st in STG and ty in TY, head
        assert len(ctx.split()) <= 25, ("ctx long", head)
        raw = open(os.path.join(UNITS, u + ".txt"), encoding="utf-8").read()
        m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", raw)
        pid, sub, date, url = m.groups()
        rec = {}
        if c != "-":
            mc = re.search(r"COMMENT " + re.escape(c) + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", raw)
            assert mc, ("no comment", head)
            date, url = mc.groups()
        n += 1
        rec = {"id": f"pb05-{n:04d}", "source": f"reddit r/{sub}", "url": url, "date": date,
               "speaker": sp, "stage": st, "type": ty, "themes": [t.strip() for t in th.split(",") if t.strip()],
               "quote": quote, "context": ctx,
               "raw_file": f"../_shared/_raw/reddit-2026/units/{u}.txt", "source_class": "reddit_archive", "post_id": pid}
        if c != "-": rec["comment_id"] = c
        out.append(rec)
    with open(VOICE, "a", encoding="utf-8") as f:
        for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"added {len(out)}: {out[0]['id'] if out else ''} -> {out[-1]['id'] if out else ''}")
main(sys.argv[1])
