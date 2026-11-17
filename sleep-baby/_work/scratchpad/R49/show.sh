#!/bin/sh
# show.sh FROM TO : print units FROM..TO (1-based) from paths.txt
cd /home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby
sed -n "$1,$2p" scratchpad/R49/paths.txt | while read p; do echo "=================== $(basename $p .txt)"; cat "$p"; done
