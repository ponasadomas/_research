#!/usr/bin/env python3
"""Check every [id] cited in a Markdown file against the global voice files.

For each id: does it resolve? For each `"fragment" [id]` or `> fragment `[id]``
pair: is the fragment a substring of that record's quote (whitespace-normalised,
curly quotes normalised)?

Usage: python3 -I verify_findings_ids.py <markdown file> <niche folder name>
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VOICE = os.path.normpath(os.path.join(HERE, "..", "..", sys.argv[2] if len(sys.argv) > 2 else "global", "voice"))

ID_RX = re.compile(r"\[([a-z]+\d{1,2}-\d{4})\]")
PAIR_RX = re.compile(r"[\"“]([^\"”]{12,}?)[\"”]\s*`?\[([a-z]+\d{1,2}-\d{4})\]`?")
BQ_RX = re.compile(r"^>\s*(.+?)\s*`\[([a-z]+\d{1,2}-\d{4})\]`", re.M)


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def load():
    recs = {}
    for f in glob.glob(os.path.join(VOICE, "*.jsonl")):
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if "id" in r:
                    recs[r["id"]] = r
    return recs


def main():
    path = sys.argv[1]
    text = open(path, encoding="utf-8").read()
    recs = load()
    ids = sorted(set(ID_RX.findall(text)))
    unresolved = [i for i in ids if i not in recs]
    pairs = PAIR_RX.findall(text) + BQ_RX.findall(text)
    bad = []
    for frag, i in pairs:
        if i not in recs:
            bad.append((i, frag, "UNRESOLVED"))
            continue
        q = norm(recs[i].get("quote", ""))
        f = norm(frag)
        if f not in q:
            bad.append((i, frag, "NOT IN QUOTE: " + q[:140]))
    print(f"{len(ids)} distinct ids cited, {len(unresolved)} unresolved")
    for i in unresolved:
        print("  UNRESOLVED", i)
    print(f"{len(pairs)} verbatim fragments paired with an id, {len(bad)} failed")
    for i, frag, why in bad:
        print(f"  FAIL {i}: \"{frag[:80]}\" -> {why}")
    sys.exit(1 if unresolved or bad else 0)


if __name__ == "__main__":
    main()
