#!/bin/bash
cd /home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour
for f in $(sed -n "$1,$2p" scratchpad/TR24/paths.txt); do cat "$f"; echo; echo '#################'; done
