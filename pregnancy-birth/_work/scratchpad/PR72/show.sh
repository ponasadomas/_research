#!/bin/bash
# usage: show.sh from to
cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
awk -F'\t' -v a=$1 -v b=$2 '$1>=a && $1<=b {print $1"\t"$3}' scratchpad/PR72/units.tsv | while IFS=$'\t' read n p; do echo "=================== UNIT $n $p"; cat "$p"; echo; done
