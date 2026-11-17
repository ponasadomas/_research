#!/bin/sh
# usage: show.sh start end  (1-based line numbers in units.txt)
cd /home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour
sed -n "$1,$2p" scratchpad/TR12/units.txt | while IFS='	' read c u; do echo "=========== $c $u"; cat "$u"; echo; done
