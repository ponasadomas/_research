#!/bin/sh
# show.sh A B : print units A..B
cd /home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby
awk -F'\t' -v a=$1 -v b=$2 'NR>=a && NR<=b {print $1"\t"$2}' scratchpad/R60/units.tsv | while IFS="$(printf '\t')" read n p; do echo "=================== UNIT $n $p"; cat "$p"; echo; done
