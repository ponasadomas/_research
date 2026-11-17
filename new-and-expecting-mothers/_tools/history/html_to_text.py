#!/usr/bin/env python3
"""Extract text from an already-saved HTML file using fetch_page.py's extractor.

    python3 -I html_to_text.py <name> <source-url> "<note>" [--dir competitors]

Reads _raw/<dir>/_html/<name>.html, writes _raw/<dir>/<name>.txt with the usual header.
For pages fetch_page.py can't get itself (e.g. expired TLS certificate fetched with curl -k,
a Wayback Machine copy). <note> goes in the header so the reader knows how it was obtained.
"""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch_page as fp

args = [a for a in sys.argv[1:]]
sub = "competitors"
if "--dir" in args:
    i = args.index("--dir"); sub = args[i + 1]; del args[i:i + 2]
name, url, note = args[0], args[1], (args[2] if len(args) > 2 else "")
d = os.path.join(fp.ROOT, sub)
raw = open(os.path.join(d, "_html", name + ".html"), encoding="utf-8", errors="replace").read()
title, meta, text = fp.extract(raw)
with open(os.path.join(d, name + ".txt"), "w", encoding="utf-8") as f:
    f.write(f"SOURCE: {url}\nNOTE: {note}\nFETCHED: {datetime.date.today()}\nTITLE: {title}\n"
            + "\n".join(meta) + "\n" + "-" * 70 + "\n" + text + "\n")
print(f"{name}: {len(raw)} bytes html | {len(text.split())} words | {title[:70]}")
