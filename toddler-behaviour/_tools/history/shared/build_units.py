#!/usr/bin/env python3
"""Turn kept post ids into frozen reading units: the post plus its original poster's own replies.

    python3 -I build_units.py <niche> <triage tsv> [<triage tsv> ...] --label read-v1

For each kept id (label != drop): fetch all archived comments once into
_shared/_raw/reddit-2026/comments/<id>.json (Arctic Shift; cached), write
_shared/_raw/reddit-2026/units/<sub>-<id>.txt if absent (never rewritten), then write
<niche>/_raw/reddit/<label>/chunks.jsonl: ~45 KB assignment lists of unit paths, grouped by keep label.
Units are shared across niches; a unit is the same text whichever niche cites it.
"""
import collections, csv, datetime, json, os, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RESEARCH = os.path.normpath(os.path.join(HERE, "..", ".."))
RAW = os.path.join(RESEARCH, "_shared", "_raw", "reddit-2026")
API = "https://arctic-shift.photon-reddit.com/api/comments/search?limit=100&fields=id,body,author,parent_id,created_utc&link_id="


def d(ts):
    return datetime.datetime.fromtimestamp(int(ts), datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def comments(pid):
    dest = os.path.join(RAW, "comments", pid + ".json")
    if os.path.exists(dest):
        return json.load(open(dest))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    data, after = [], None
    for _ in range(30):
        url = API + pid + (f"&after={after}" if after else "") + "&sort=asc"
        for attempt in range(5):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research"}), timeout=60) as r:
                    batch = json.load(r)["data"] or []
                break
            except Exception:
                time.sleep(3 * (attempt + 1))
        else:
            raise SystemExit(f"comments failed for {pid}")
        data += batch
        time.sleep(0.5)
        if len(batch) < 100:
            break
        after = batch[-1]["created_utc"]
    json.dump(data, open(dest, "w"))
    return data


def main():
    niche = sys.argv[1]
    label = sys.argv[sys.argv.index("--label") + 1]
    tsvs = [a for a in sys.argv[2:] if a.endswith(".tsv")]
    out = os.path.join(RESEARCH, niche, "_raw", "reddit", label)
    if os.path.exists(os.path.join(out, "chunks.jsonl")):
        raise SystemExit("frozen chunks exist; choose a new --label")
    os.makedirs(out, exist_ok=True)
    keep = {}
    for t in tsvs:
        for row in csv.DictReader(open(t), delimiter="\t"):
            pid, lab = row["post_id"].strip(), row["label"].strip()
            if lab == "drop":
                keep.pop(pid, None)  # a later drop (e.g. an orchestrator safety override) removes an earlier keep
            else:
                keep[pid] = lab
    posts = {}
    want = set(keep)
    for f in os.listdir(RAW):
        if f.endswith(".posts.jsonl"):
            for line in open(os.path.join(RAW, f)):
                q = json.loads(line)
                if q["id"] in want:
                    q["subreddit"] = f[: -len(".posts.jsonl")]
                    posts[q["id"]] = q
    os.makedirs(os.path.join(RAW, "units"), exist_ok=True)
    groups = collections.defaultdict(list)
    missing = sorted(want - set(posts))
    for pid, lab in sorted(keep.items()):
        if pid not in posts:
            continue
        q = posts[pid]; sub = q["subreddit"]
        upath = os.path.join(RAW, "units", f"{sub}-{pid}.txt")
        if not os.path.exists(upath):
            cs = comments(pid)
            op = q.get("author") or ""
            mine = [c for c in cs if op and op not in ("[deleted]", "AutoModerator") and c.get("author") == op]
            txt = (f"POST {pid} | r/{sub} | {d(q['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/\n"
                   f"TITLE: {q.get('title','')}\n\n{q.get('selftext','')}\n\n"
                   f"--- ORIGINAL POSTER'S REPLIES IN THE THREAD: {len(mine)} of {len(cs)} archived comments ---\n")
            for c in mine:
                txt += f"\nCOMMENT {c['id']} | {d(c['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/comment/{c['id']}/\n{c.get('body','')}\n"
            open(upath, "w", encoding="utf-8").write(txt)
        size = os.path.getsize(upath)
        groups[lab].append((f"../_shared/_raw/reddit-2026/units/{sub}-{pid}.txt", size))
    chunks = []
    for lab in sorted(groups):
        buf, tot, i = [], 0, 1
        for path, size in groups[lab]:
            if buf and tot + size > 45000:
                chunks.append({"chunk": f"{label}-{lab}-{i:03d}", "label": lab, "units": buf, "bytes": tot}); buf, tot, i = [], 0, i + 1
            buf.append(path); tot += size
        if buf:
            chunks.append({"chunk": f"{label}-{lab}-{i:03d}", "label": lab, "units": buf, "bytes": tot})
    open(os.path.join(out, "chunks.jsonl"), "w").write("".join(json.dumps(c) + "\n" for c in chunks))
    print(json.dumps({"kept": len(keep), "units": sum(len(c["units"]) for c in chunks), "missing_posts": len(missing), "chunks": len(chunks), "by_label": {k: len(v) for k, v in groups.items()}}))


if __name__ == "__main__":
    main()
