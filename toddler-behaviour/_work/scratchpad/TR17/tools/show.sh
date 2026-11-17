#!/bin/bash
# show.sh START END : print units by line number in units.tsv (1-based, inclusive)
cd /home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour
sed -n "$1,$2p" scratchpad/TR17/units.tsv | while IFS=$'\t' read c f s; do echo "########## $(basename $f .txt) [$c]"; sed -E 's#\| https://www.reddit.com/r/[^ ]*##' "$f"; done
