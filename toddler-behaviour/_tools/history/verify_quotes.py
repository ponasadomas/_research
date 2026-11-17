#!/usr/bin/env python3
"""Check that every quote in voice/*.jsonl really appears in the raw file it cites.

A quote may be trimmed with " […] "; each piece must be found, in order, in raw_file
(only whitespace and HTML entities are normalised; case and punctuation are exact). Run from anywhere:

    python3 verify_quotes.py            # all files
    python3 verify_quotes.py voice/x.jsonl
"""
import json, sys, os, re, glob, html

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REQUIRED = ["id", "source", "url", "speaker", "stage", "type", "themes", "quote", "context", "raw_file"]
_cache = {}


def norm(s):
    # Compare original spelling, case and punctuation. Only decode entities and
    # normalize whitespace so extraction line wrapping does not change a quote.
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()


def raw(path):
    if path not in _cache:
        full = os.path.join(ROOT, path)
        _cache[path] = norm(open(full, encoding="utf-8", errors="replace").read()) if os.path.exists(full) else None
    return _cache[path]


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "voice", "*.jsonl")))
    total = bad = 0
    for f in files:
        fbad = n = 0
        for i, line in enumerate(open(f), 1):
            if not line.strip():
                continue
            n += 1
            try:
                q = json.loads(line)
            except Exception as e:
                print(f"{f}:{i} invalid JSON ({e})"); fbad += 1; continue
            missing = [k for k in REQUIRED if k not in q]
            if missing:
                print(f"{f}:{i} missing {missing}"); fbad += 1; continue
            text = raw(q["raw_file"])
            if text is None:
                print(f"{f}:{i} raw_file not found: {q['raw_file']}"); fbad += 1; continue
            pos = 0
            for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", q["quote"]):
                piece = norm(piece)
                if not piece:
                    continue
                at = text.find(piece, pos)
                if at < 0:
                    print(f"{f}:{i} {q['id']} NOT IN SOURCE: {piece[:90]!r}"); fbad += 1; break
                pos = at + len(piece)
        print(f"{os.path.basename(f)}: {n} quotes, {fbad} failed")
        total += n; bad += fbad
    print(f"TOTAL {total} quotes, {bad} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
