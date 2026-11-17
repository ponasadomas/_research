#!/usr/bin/env python3
"""DR02 builder: reads rec_*.py record lists, derives url/date/post/comment from unit, writes voice file."""
import json, re, html, os, sys, glob, importlib.util
DEV = "/home/thinkpad/GitHub/ads/mamivio.com/research/development"
HERE = os.path.join(DEV, "scratchpad/DR02")
OUT = os.path.join(DEV, "voice/reddit-dr02.jsonl")
UNITS = {}
for line in open(os.path.join(HERE, "units.txt")):
    p = line.split()
    if len(p) == 3:
        UNITS[os.path.basename(p[1])[:-4]] = p[1]

def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()

def blocks(path):
    txt = open(os.path.join(DEV, path), encoding="utf-8").read()
    out = []; cur = None
    for ln in txt.split("\n"):
        m = re.match(r"^POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [\d:]+ UTC \| (\S+)", ln)
        c = re.match(r"^COMMENT (\w+) \| (\d{4}-\d\d-\d\d) [\d:]+ UTC \| (\S+)", ln)
        if m:
            cur = dict(post_id=m.group(1), sub=m.group(2), date=m.group(3), url=m.group(4), comment_id=None, text=[]); out.append(cur)
        elif c:
            cur = dict(post_id=out[0]["post_id"], sub=out[0]["sub"], date=c.group(2), url=c.group(3), comment_id=c.group(1), text=[]); out.append(cur)
        elif cur is not None:
            cur["text"].append(ln)
    for b in out:
        b["norm"] = norm("\n".join(b["text"]))
    return out

recs = []
for f in sorted(glob.glob(os.path.join(HERE, "rec_*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    recs.extend(mod.R)

# Post-review corrections (advisor pass): speaker by unit, type by quote prefix.
SPEAKER_FIX = {  # strict rule (coordinator, 2026-10-25): mother only if she self-identifies
    "beyondthebump-1wlqmtu": "parent_unspecified", "Parenting-1wm3mlq": "parent_unspecified",
    "NewParents-1wmhsud": "new_mother", "beyondthebumpUK-1x0yl00": "parent_unspecified",
    "beyondthebumpUK-1x5pjq1": "parent_unspecified", "Mommit-1x8tvcu": "new_mother",
    "Mommit-1wk5egr": "parent_unspecified", "NewParents-1wlq3lh": "parent_unspecified",
    "FirstTimeMom-1wltf5u": "parent_unspecified", "NewParents-1wnl5op": "parent_unspecified",
    "FirstTimeMom-1wqbuvt": "parent_unspecified", "Mommit-1wsymut": "parent_unspecified",
    "beyondthebump-1wzi3lu": "parent_unspecified", "Mommit-1x65xz1": "parent_unspecified",
    "NewParents-1xe8osp": "parent_unspecified", "Mommit-1xc7plk": "parent_unspecified",
    "Mommit-1xd2mgy": "parent_unspecified"}
TYPE_FIX = {"Guess I gotta buy some cabinet toys": "desire", "I've never heard Yoto player": "desire"}
SEED = "what_to_do_all_day awake_time tummy_time tummy_time_hate floor_play rolling sitting crawling pulling_up walking first_words babbling fine_motor milestone_comparison milestone_anxiety corrected_age pediatrician_checkup cdc_milestones wonder_weeks leaps screen_time toys_too_many montessori play_ideas boredom_mum maternal_guilt not_enough_play container_time baby_classes app_tracking information_overload conflicting_advice reassurance_seeking social_comparison grandparent_comments early_intervention_question personalization price_value".split()
STUBS = ("Same post", "Closing line", "Reply in the same thread", "Same reply", "Reply to commenters", "Her ask", "Same mother's", "The questions she lists", "His ask")
base = {}
for r in recs:
    if not r["cx"].startswith(STUBS) and r["u"] not in base:
        base[r["u"]] = r["cx"]
base.setdefault("NewParents-1wjqguz", base.get("sahm-1wjqfp4"))
base.setdefault("Mommit-1wjqhxl", base.get("sahm-1wjqfp4"))
base.setdefault("Parenting-1x3c1c6", base.get("Mommit-1x3btko"))
for r in recs:
    r["sp"] = SPEAKER_FIX.get(r["u"], r["sp"])
    for k, v in TYPE_FIX.items():
        if r["q"].startswith(k):
            r["ty"] = v
    r["th"] = [t for t in r["th"] if t in SEED] + [t for t in r["th"] if t not in SEED]
    r["q"] = re.sub(r"\s*\[\.\.\.\]\s*", " […] ", r["q"])
    if r["cx"].startswith(STUBS):
        b = base.get(r["u"])
        if not b:
            print("NO BASE", r["u"]); continue
        rest = r["cx"]
        for st in STUBS:
            if rest.startswith(st):
                rest = rest[len(st):].lstrip(" .;,:")
        cand = b.rstrip(".") + ("; " + rest if rest else "") + ("" if (rest or b).endswith((".", "?", "'", "!")) else ".")
        if len(cand.split()) > 25:
            cand = b.rstrip(".") + "; later in the same post."
            if len(cand.split()) > 25:
                cand = b
        r["cx"] = cand
lines = []; errs = 0; restricted = []
for i, r in enumerate(recs, 1):
    path = UNITS[r["u"]]
    bl = blocks(path)
    pieces = [norm(p) for p in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", r["q"]) if norm(p)]
    hit = [b for b in bl if all(p in b["norm"] for p in pieces)]
    if not hit:
        print("NOT FOUND", r["u"], r["q"][:80]); errs += 1; continue
    b = hit[0]
    if len(r["cx"].split()) > 25:
        print("CONTEXT LONG", i, r["u"], len(r["cx"].split()))
    o = dict(id=f"dv02-{i:04d}", source=f"reddit r/{b['sub']}", url=b["url"], date=b["date"],
             speaker=r["sp"], stage=r["st"], type=r["ty"], themes=r["th"], quote=r["q"], context=r["cx"],
             raw_file=path, source_class="reddit_archive", post_id=b["post_id"])
    if b["comment_id"]:
        o["comment_id"] = b["comment_id"]
    if r.get("rs"):
        restricted.append((o["id"], r["u"], r["rs"]))
    lines.append(json.dumps(o, ensure_ascii=False))
if errs:
    sys.exit(f"{errs} errors; not written")
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote", len(lines))
open(os.path.join(HERE, "restricted.tsv"), "w").write("".join(f"{a}\t{b}\t{c}\n" for a, b, c in restricted))
print("restricted", len(restricted))
