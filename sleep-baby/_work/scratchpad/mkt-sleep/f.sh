#!/bin/bash
# usage: f.sh slug url [slug url ...]
T=/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/_tools/fetch_page.py
while [ $# -ge 2 ]; do python3 -I $T "$1" "$2" --dir competitors; shift 2; done
