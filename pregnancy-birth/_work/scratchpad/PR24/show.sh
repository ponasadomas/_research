#!/bin/sh
cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
awk -v b="$1" '$1==b{print $2}' scratchpad/PR24/batches.txt | while read n; do p=$(sed -n "${n}p" scratchpad/PR24/idx.tsv | cut -f2); echo "######## U$n $p"; cat "$p"; echo; done
