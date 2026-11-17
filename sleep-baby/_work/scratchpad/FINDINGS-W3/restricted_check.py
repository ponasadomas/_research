#!/usr/bin/env python3
"""Verify cited ids and verbatim fragments; historical markings have no effect.
Usage: restricted_check.py FILE [--from 'heading']
"""
from pathlib import Path
import subprocess
import sys
import tempfile

BUILD = Path(__file__).resolve().parents[2]
VERIFIER = BUILD.parent / "_shared/_tools/verify_findings_ids.py"
path = Path(sys.argv[1])
if "--from" in sys.argv:
    heading = sys.argv[sys.argv.index("--from") + 1]
    text = path.read_text(encoding="utf-8")
    text = text[text.index(heading):]
    with tempfile.TemporaryDirectory(prefix="sleep-baby-verify-") as work:
        selected = Path(work) / "findings.md"
        selected.write_text(text, encoding="utf-8")
        result = subprocess.run([sys.executable, "-I", str(VERIFIER), str(selected), "sleep-baby"])
else:
    result = subprocess.run([sys.executable, "-I", str(VERIFIER), str(path), "sleep-baby"])
sys.exit(result.returncode)
