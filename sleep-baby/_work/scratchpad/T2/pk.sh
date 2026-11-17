#!/bin/zsh
# usage: pk.sh N line numbers...
n=$1; shift
for l in "$@"; do awk -v L=$l 'NR==L{print $1}' compact.txt; done | xargs python3 peek.py $n
