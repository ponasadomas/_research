#!/usr/bin/env python3
"""Legacy wave-3 entry point: verify findings provenance with no subject exclusions.

Checks the whole current findings file, including section 17. Historical quote
labels never prohibit quotation or require an inline restriction warning.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
VERIFIER = ROOT.parent / '_shared' / '_tools' / 'verify_findings_ids.py'
result = subprocess.run([
    sys.executable, '-I', str(VERIFIER),
    str(ROOT / 'synthesis' / 'findings.md'), ROOT.name,
])
sys.exit(result.returncode)
