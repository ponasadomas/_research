#!/bin/sh
cd /home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby
sed -n "$1,$2p" scratchpad/R32/units.txt | while IFS="$(printf '\t')" read c u; do echo "=========== $(basename $u)"; cat "$u"; echo; done
