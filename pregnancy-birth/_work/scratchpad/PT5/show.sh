#!/bin/bash
f=$1; shift
for i in "$@"; do awk -v I="$i" '/^ID /{p=($2==I)} p&&/^OPENING/{print I " " substr($0,10,330)}' /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/_raw/reddit/filter-v1/wave1/cards/$f.txt; done
