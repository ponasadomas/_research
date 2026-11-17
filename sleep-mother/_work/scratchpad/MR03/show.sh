#!/bin/sh
# show units of chunk N (e.g. 011)
cd /home/thinkpad/GitHub/ads/mamivio.com/research/sleep-mother
awk -v c="read-v1-keep_core-$1" '$1==c{f=1;next} /^read-v1/{f=0} f' scratchpad/MR03/units.txt | while read u; do echo "=========== UNIT $(basename $u .txt)"; cat "$u"; done
