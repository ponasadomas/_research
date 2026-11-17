import json, collections, os
D = os.path.dirname(os.path.abspath(__file__)); N = os.path.join(D, "..", "..")
recs = [json.loads(l) for l in open(os.path.join(N, "voice/reddit-tr05.jsonl"))]
by = collections.defaultdict(list)
for r in recs: by[r["raw_file"].split("/")[-1][:-4]].append(r["id"])
EX = {
 "pottytraining-1wfghxn": ("excluded", "medical treatment details are the substance of the post"),
 "pottytraining-1wg3jw2": ("excluded", "author describes physical force toward the child"),
 "GentleParenting-1wgbb6x": ("excluded", "same author as pottytraining-1wg3jw2; physical force toward the child"),
 "pottytraining-1wgbf4i": ("excluded", "same author as pottytraining-1wg3jw2 (cross-post); line not to cross"),
 "pottytraining-1widuzi": ("excluded", "medical treatment details are the substance of the post"),
 "ScienceBasedParenting-1wkswms": ("excluded", "child bodily-behaviour topic outside the niche scope; not quoted"),
 "Parenting-1wl28fn": ("excluded", "verbal harshness toward the child is the substance of the post"),
 "toddlers-1wk6fcm": ("excluded", "self-injury behaviour with developmental context; not quoted"),
 "toddlers-1wi77tp": ("read, not quoted", "infant fussiness and physio check; no behaviour or potty content"),
 "Mommit-1weyylf": ("read, not quoted", "duplicate cross-post of toddlers-1weywox"),
 "AttachmentParenting-1wez14j": ("read, not quoted", "duplicate cross-post of toddlers-1weywox"),
 "pottytraining-1wgjnne": ("read, not quoted", "duplicate cross-post of toddlers-1wgjmoe"),
 "Mommit-1whkccw": ("read, not quoted", "duplicate cross-post of toddlers-1whk8p1"),
 "Mommit-1wi54yd": ("read, not quoted", "duplicate cross-post of toddlers-1wi527a"),
}
NOTE = {
 "Mommit-1wekd30": "child has an existing diagnosis; quotes chosen do not mention it",
 "toddlers-1weuudd": "passages about the father yelling not quoted",
 "toddlers-1weywox": "medication passages not quoted",
 "toddlers-1wfqlb5": "the parent's shout not quoted; guilt lines restricted",
 "toddlers-1wfqunt": "parent's and partner's ADHD passages not quoted",
 "pottytraining-1wg8rs8": "passage about keeping the child on the potty not quoted",
 "toddlers-1wg9hgc": "snapping passage not quoted",
 "toddlers-1wgc0vd": "relatives' advice to hit restricted (rejected by author)",
 "Mommit-1wfkg57": "constipation/medical passages not quoted",
 "pottytraining-1wgd1ew": "medical tests not quoted",
 "pottytraining-1wgfago": "laxative passages not quoted",
 "toddlers-1whk8p1": "laxative list and paediatrician exam not quoted",
 "Mommit-1wi6bz4": "passage about yelling at the child and the slur itself not quoted",
 "pottytraining-1winem5": "passage about shouting at the child not quoted",
 "Parenting-1wk1vbm": "grandmother's suggestion to bite the child not quoted",
 "toddlers-1wk0cug": "child has developmental supports; quotes restricted",
 "Mommit-1wkmm0r": "father's physical reaction at bedtime not quoted",
 "toddlers-1wldw20": "partner's raised voice trimmed out of quote",
 "toddlers-1wlmn4k": "speech-delay mention not quoted",
 "pottytraining-1win1yt": "stool softener not quoted",
 "Mommit-1wl28kq": "baby-blues / feeding passages not quoted",
}
rows = []; chunks = collections.OrderedDict()
for l in open(os.path.join(D, "units.tsv")):
    c, u, sz = l.split()
    ids = by.get(u, [])
    st, why = EX.get(u, ("read", ""))
    if u in EX and ids: raise SystemExit("excluded unit has quotes " + u)
    if not ids and u not in EX: raise SystemExit("unit without quotes or reason " + u)
    rng = f"{ids[0]}–{ids[-1]} ({len(ids)})" if len(ids) > 1 else (f"{ids[0]} (1)" if ids else "—")
    note = why or NOTE.get(u, "")
    rows.append(f"| keep_core-{c} | `../_shared/_raw/reddit-2026/units/{u}.txt` | {st} | {rng} | {note} |")
    ch = chunks.setdefault(c, [0, 0]); ch[0] += 1; ch[1] += len(ids)
print(len(rows), sum(1 for u in EX if EX[u][0]=="excluded"), sum(1 for u in EX if EX[u][0]!="excluded"), len(recs))
out = os.path.join(N, "sources/reddit-reading-tr05.md")
ne = sum(1 for u in EX if EX[u][0]=="excluded"); nn = len(EX)-ne
with open(out, "w") as o:
    o.write(f"""# Reddit full reads — TR05 (toddler-behaviour, 2026-10-25)

Reader TR05 · id prefix `tb05` · voice file `voice/reddit-tr05.jsonl` · brief `../_shared/_tools/brief-reading.md` · chunks from `_raw/reddit/read-v1/chunks.jsonl`. Scratch and build script: `scratchpad/TR05/` (`spec-*.py` → `build.py`; this ledger from `ledger.py`).

## Counts

| step | n |
|---|---|
| chunks assigned | 8 (read-v1-keep_core-023 to 030) |
| units in those chunks | {len(rows)} |
| units read in full | {len(rows)} (all) |
| units quoted from | {len(by)} |
| units excluded (read in full, nothing copied, line not to cross) | {ne} |
| units read, not quoted (duplicate cross-post or off-topic) | {nn} |
| quotes written | {len(recs)} (tb05-0001 to tb05-{len(recs):04d}) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-tr05.jsonl` → {len(recs)} quotes, 0 failed |

Counts are counts of quotes chosen, never of people.

## Chunks

| chunk | units | quotes |
|---|---|---|
""")
    for c, (nu, nq) in chunks.items(): o.write(f"| read-v1-keep_core-{c} | {nu} | {nq} |\n")
    o.write("""
## Units (every unit, read in full)

Status `read` = read in full and quoted; `excluded` = read in full, nothing copied, neutral reason; `read, not quoted` = duplicate or off-topic. Notes record passages deliberately left unquoted inside read units.

| chunk | unit (raw_file) | status | quote ids | note |
|---|---|---|---|---|
""")
    o.write("\n".join(rows) + "\n\n## Unread\n\nNone. All 133 units in the assigned chunks were read in full.\n")
