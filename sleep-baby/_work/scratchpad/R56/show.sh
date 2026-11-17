#!/bin/bash
# show units $1..$2 (1-based)
cd /home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby
sed -n "$1,$2p" scratchpad/R56/units.txt | while IFS=$'\t' read c u; do echo "=================== #UNIT $(basename $u .txt)"; cat "$u"; echo; done
