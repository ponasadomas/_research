#!/bin/sh
cd "$(dirname "$0")"
for i in "$@"; do grep "^$i " w3-compact.txt || echo "MISSING $i"; done
