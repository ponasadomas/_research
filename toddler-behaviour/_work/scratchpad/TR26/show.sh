#!/bin/bash
cd /home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour
for i in $(seq $1 $2); do u=$(sed -n "${i}p" scratchpad/TR26/units.tsv | cut -f2); echo "=========== U$i"; cat "$u"; done
