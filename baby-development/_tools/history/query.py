#!/usr/bin/env python3
"""Search the quote database (voice/*.jsonl).

    python3 query.py --speaker new_mother --type tried_failed --theme tummy_time
    python3 query.py --text "meal plan" --max 20
    python3 query.py --id aud01-0001 guide01-001
    python3 query.py --stats

Filters combine with AND; --speaker/--type/--stage/--theme/--source accept a prefix
(e.g. --speaker new_, --source reddit). --short N keeps quotes of at most N characters.
"""
import argparse, glob, json, os, random, collections

VOICE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "voice")


def load():
    for f in sorted(glob.glob(os.path.join(VOICE, "*.jsonl"))):
        for line in open(f):
            if line.strip():
                yield json.loads(line)


def main():
    a = argparse.ArgumentParser()
    for k in ("speaker", "type", "stage", "theme", "source", "text"):
        a.add_argument("--" + k)
    a.add_argument("--source-class", help="Prefix filter, e.g. reddit_archive or forum")
    a.add_argument("--evidence-kind", help="Prefix filter, e.g. archived_original")
    a.add_argument("--theme-group", help="Named group from theme_groups.json")
    a.add_argument("--original-only", action="store_true", help="Original customer/community evidence; excludes index extracts, sellers, ads and guidance")
    a.add_argument("--exclude-restricted", action="store_true", help="Deprecated compatibility option; all matching quotes are retained")
    a.add_argument("--id", nargs="*")
    a.add_argument("--short", type=int)
    a.add_argument("--max", type=int, default=40)
    a.add_argument("--shuffle", action="store_true")
    a.add_argument("--stats", action="store_true")
    o = a.parse_args()
    rows = list(load())
    if o.stats:
        print(len(rows), "quotes")
        for k in ("source_class", "evidence_kind", "source", "speaker", "stage", "type"):
            print(f"\n{k}:")
            for v, n in collections.Counter(r.get(k, 'unspecified') for r in rows).most_common():
                print(f"  {n:5d}  {v}")
        print("\nthemes:")
        for v, n in collections.Counter(t for r in rows for t in r["themes"]).most_common():
            print(f"  {n:5d}  {v}")
        return
    if o.id:
        rows = [r for r in rows if r["id"] in o.id]
    for k in ("speaker", "type", "stage", "source", "source_class", "evidence_kind"):
        v = getattr(o, k)
        if v:
            rows = [r for r in rows if r.get(k, '').startswith(v)]
    if o.original_only:
        rows = [r for r in rows if r.get('source_class') in {'reddit_archive','forum','forum_oblique','qa_community','app_review','book_review'}]
    if o.theme_group:
        with open(os.path.join(os.path.dirname(__file__), 'theme_groups.json')) as f:
            groups = json.load(f)
        if o.theme_group not in groups:
            a.error('Unknown theme group; choose: ' + ', '.join(groups))
        tags = set(groups[o.theme_group])
        rows = [r for r in rows if tags.intersection(r['themes'])]
    if o.theme:
        rows = [r for r in rows if any(t.startswith(o.theme) for t in r["themes"])]
    if o.text:
        rows = [r for r in rows if o.text.lower() in r["quote"].lower()]
    if o.short:
        rows = [r for r in rows if len(r["quote"]) <= o.short]
    print(f"# {len(rows)} match")
    if o.shuffle:
        random.shuffle(rows)
    for r in rows[: o.max]:
        print(f"\n[{r['id']}] {r['speaker']} · {r['stage']} · {r['type']} · {', '.join(r['themes'])}")
        print(f"  \"{r['quote']}\"")
        print(f"  — {r['context']}  <{r['url']}>")


if __name__ == "__main__":
    main()
