#!/bin/bash
# usage: f.sh slug url [slug url ...]
cd /home/thinkpad/GitHub/ads/mamivio.com/research/development
while [ $# -ge 2 ]; do python3 -I _tools/fetch_page.py "$1" "$2" --dir competitors; shift 2; sleep 1; done
