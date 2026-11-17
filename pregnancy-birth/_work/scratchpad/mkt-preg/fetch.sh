#!/bin/bash
# reads "slug url" lines on stdin
T=/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/_tools/fetch_page.py
while read s u; do [ -z "$s" ] && continue; python3 -I "$T" "$s" "$u" --dir competitors; done
