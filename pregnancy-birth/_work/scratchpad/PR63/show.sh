#!/bin/bash
cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
for u in $(cut -f2 scratchpad/PR63/units.tsv | sed -n "$1,$2p"); do echo "=================== $u"; cat $u; echo; done > scratchpad/PR63/view.txt
wc -c scratchpad/PR63/view.txt
