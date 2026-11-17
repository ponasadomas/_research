#!/usr/bin/env python3
"""Verify competitor blockquotes without discarding case or punctuation.

The copied reference verifier remains available separately. This check only
normalizes HTML entities and whitespace; omission pieces must occur in order
in one saved text from the corresponding offer.
"""
from pathlib import Path
import html
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def norm(text):
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def contains(text, pieces):
    position = 0
    for piece in pieces:
        found = text.find(piece, position)
        if found < 0:
            return False
        position = found + len(piece)
    return True


def main():
    total = failed = notes = 0
    for note in sorted((ROOT / "competitors").glob("*.md")):
        if note.stem.lower() == "readme":
            continue
        notes += 1
        raws = set((ROOT / "_raw/competitors").glob(note.stem + "*.txt"))
        # Later waves keep immutable captures in their own directory and name
        # the exact source in the note instead of copying it into the baseline.
        for relative in re.findall(r"`(_raw/[^`\n]+)`", note.read_text()):
            path = (ROOT / relative).resolve()
            if path.is_relative_to((ROOT / "_raw").resolve()) and path.is_file() and path.suffix in {".txt", ".json"}:
                raws.add(path)
        raws = sorted(raws)
        texts = [norm(path.read_text()) for path in raws]
        for number, line in enumerate(note.read_text().splitlines(), 1):
            if not line.lstrip().startswith(">"):
                continue
            quote = line.lstrip()[1:].strip()
            if not quote:
                continue
            total += 1
            pieces = [norm(piece) for piece in re.split(r"\[(?:…|\.\.\.)\]", quote) if norm(piece)]
            if not pieces or not any(contains(text, pieces) for text in texts):
                failed += 1
                print(f"FAIL {note.name}:{number}: {quote[:120]!r}")
    print(f"TOTAL {notes} notes, {total} verbatim lines, {failed} strict failures")
    return bool(failed)


if __name__ == "__main__":
    sys.exit(main())
