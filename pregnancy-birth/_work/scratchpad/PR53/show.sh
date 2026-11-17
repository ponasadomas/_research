#!/bin/sh
cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
sed -n "$1,$2p" scratchpad/PR53/units.txt | while IFS='	' read c u s; do echo "=================== #UNIT $(basename $u .txt)"; cat "$u"; echo; done
