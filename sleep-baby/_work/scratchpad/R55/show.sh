#!/bin/bash
# usage: show.sh from to
cd /home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby
awk -F'\t' -v a=$1 -v b=$2 '$1>=a && $1<=b {print $1"\t"$2}' scratchpad/R55/units.tsv | while IFS=$'\t' read i u; do echo "=====UNIT $i $u"; cat "$u"; echo; done
