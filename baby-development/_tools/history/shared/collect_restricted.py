#!/usr/bin/env python3
"""Compatibility entry point: report historical labels without changing any file.

The owner retired restriction decisions on 2026-11-16. Labels never affect
selection, quotation, or verification. python3 -I collect_restricted.py <niche>
"""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2] / sys.argv[1]
path = root / "synthesis" / "restricted-ids.md"
listed = set(re.findall(r"\b[a-z]+\d{1,2}-\d{4}\b", path.read_text())) if path.exists() else set()
ids = {json.loads(line)["id"] for voice in (root / "voice").glob("*.jsonl")
       for line in voice.read_text().splitlines() if line.strip()}
missing = sorted(listed - ids)
print(f"{sys.argv[1]}: {len(listed)} historical labels, {len(missing)} unresolved; no restrictions applied or written")
for quote_id in missing:
    print("UNRESOLVED", quote_id)
sys.exit(bool(missing))
