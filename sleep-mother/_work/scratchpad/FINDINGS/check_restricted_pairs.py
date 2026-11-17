#!/usr/bin/env python3
"""Legacy entry point: verify findings ids and verbatim words, regardless of subject.

The former subject restriction is retired. Keep the provenance checks by delegating
to the shared verifier; historical markings have no effect on quotation.
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
