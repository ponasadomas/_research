#!/bin/bash
cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
sed -n "$1,$2p" scratchpad/PR43/units.txt | while IFS=$'\t' read c u; do echo "=================== #$(grep -n "$u" scratchpad/PR43/units.txt | cut -d: -f1) $c $u"; cat "$u"; echo; done
