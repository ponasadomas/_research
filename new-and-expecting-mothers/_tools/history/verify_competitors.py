#!/usr/bin/env python3
"""Check that every verbatim line in competitors/<slug>.md appears in that offer's raw capture.

Convention: in a competitor note, any line starting with ">" is a VERBATIM quote from the page.
It must be found in one of  _raw/competitors/<slug>*.txt  (e.g. <slug>.txt, <slug>--pricing.txt,
<slug>--yt-<id>.txt). Trim with " […] "; pieces must appear in order. Comparison ignores case,
punctuation, whitespace and markdown markers (only letters and digits are compared), so curly
quotes or a heading marker never cause a false failure. Lines that are not verbatim (your own
description, interpretation) must NOT be blockquotes.

    python3 -I verify_competitors.py            # all notes
    python3 -I verify_competitors.py little-lunches
"""
import sys, os, re, glob, html, unicodedata

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def norm(s):
    s = unicodedata.normalize("NFKD", html.unescape(s))
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def main():
    notes = [os.path.join(ROOT, "competitors", a + ".md") for a in sys.argv[1:]] or sorted(
        glob.glob(os.path.join(ROOT, "competitors", "*.md")))
    total = bad = 0
    for note in notes:
        slug = os.path.basename(note)[:-3]
        if slug.lower() == "readme":
            continue
        raws = sorted(glob.glob(os.path.join(ROOT, "_raw", "competitors", slug + "*.txt")))
        # New capture waves declare their immutable text path in the note.
        for relative in re.findall(r"`(_raw/[^`\n]+)`", open(note, encoding="utf-8").read()):
            path = os.path.realpath(os.path.join(ROOT, relative))
            raw_root = os.path.realpath(os.path.join(ROOT, "_raw"))
            if path.startswith(raw_root + os.sep) and os.path.isfile(path) and path.endswith((".txt", ".json")):
                raws.append(path)
        raws = sorted(set(raws))
        texts = [norm(open(r, encoding="utf-8", errors="replace").read()) for r in raws]
        n = fbad = 0
        for i, line in enumerate(open(note, encoding="utf-8"), 1):
            if not line.lstrip().startswith(">"):
                continue
            body = line.lstrip()[1:].strip()
            if not norm(body):
                continue
            n += 1
            pieces = [norm(p) for p in re.split(r"\[(?:…|\.\.\.)\]", body) if norm(p)]
            ok = False
            for t in texts:
                pos = 0
                for p in pieces:
                    at = t.find(p, pos)
                    if at < 0:
                        break
                    pos = at + len(p)
                else:
                    ok = True
                    break
            if not ok:
                fbad += 1
                print(f"{slug}.md:{i} NOT IN RAW: {body[:100]!r}")
        print(f"{slug}: {n} verbatim lines, {fbad} failed, {len(raws)} raw file(s)")
        total += n; bad += fbad
    print(f"TOTAL {total} verbatim lines, {bad} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
