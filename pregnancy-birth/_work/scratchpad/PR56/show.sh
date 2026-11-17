#!/bin/bash
# usage: show.sh start end
cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
sed -n "$1,$2p" scratchpad/PR56/units.tsv | while IFS=$'\t' read c u; do echo "##### $u"; sed -e 's#https://www.reddit.com/r/[^ ]*comment/\([a-z0-9]*\)/#c:\1#' "$u"; echo; done
