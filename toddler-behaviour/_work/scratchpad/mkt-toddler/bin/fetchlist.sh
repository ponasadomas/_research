#!/bin/bash
# fetchlist.sh <file with "slug url" lines>
cd /home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour
while read -r slug url; do [ -z "$slug" ] && continue; python3 -I _tools/fetch_page.py "$slug" "$url" --dir competitors; sleep 1; done < "$1"
