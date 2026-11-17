# Build voice/reddit-tr07.jsonl from spec files spec-*.py (python literal lists of dicts).
import ast, glob, json, os, re, sys
NICHE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(NICHE, "voice", "reddit-tr07.jsonl")
TR = str.maketrans("’‘“”\xa0", "''\"\" ")
def segs(text):
    out = []
    for m in re.finditer(r"^(POST|COMMENT) (\S+) \| (?:(r/\S+) \| )?(\d{4}-\d\d-\d\d)[^|]*\| (\S+)", text, re.M):
        out.append((m.start(), m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)))
    return out
def find(text, low, s, e, pos):
    a = low.find(s.translate(TR), pos)
    if a < 0: raise SystemExit(f"start not found: {s!r}")
    b = low.find(e.translate(TR), a)
    if b < 0: raise SystemExit(f"end not found after start: {e!r}")
    return a, b + len(e)
recs = []; n = 0
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "spec-*.py"))):
    for d in ast.literal_eval(open(f, encoding="utf-8").read()):
        raw = "../_shared/_raw/reddit-2026/units/" + d["u"] + ".txt"
        text = open(os.path.join(NICHE, raw), encoding="utf-8").read()
        low = text.translate(TR)
        parts = d.get("p") or [[d["s"], d["e"]]]
        pos = 0; pieces = []; first = None
        for s, e in parts:
            a, b = find(text, low, s, e, pos)
            if first is None: first = a
            pieces.append(re.sub(r"\s+", " ", text[a:b]).strip()); pos = b
        sg = [x for x in segs(text) if x[0] <= first][-1]
        post = segs(text)[0]
        n += 1
        r = {"id": f"tb07-{n:04d}", "source": "reddit " + post[3], "url": sg[5], "date": sg[4],
             "speaker": d["sp"], "stage": d["st"], "type": d["t"], "themes": d["th"],
             "quote": " […] ".join(pieces), "context": d["c"], "raw_file": raw,
             "source_class": "reddit_archive", "post_id": post[2]}
        if sg[1] == "COMMENT": r["comment_id"] = sg[2]
        if len(d["c"].split()) > 25: print("context too long", r["id"], file=sys.stderr)
        recs.append(r)
with open(OUT, "w", encoding="utf-8") as o:
    for r in recs: o.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(recs), "records")
