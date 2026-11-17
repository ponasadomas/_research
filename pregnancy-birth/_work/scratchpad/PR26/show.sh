#!/bin/bash
cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
sed -n "$1,$2p" scratchpad/PR26/units.tsv | while IFS=$'\t' read c u s; do echo "######## $c $u"; cat "$u"; echo; done
