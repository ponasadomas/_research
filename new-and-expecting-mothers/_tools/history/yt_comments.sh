#!/bin/bash
# usage: yt_comments.sh <ids.txt> <json-dir> <txt-dir>
# Downloads top comments (max 400, up to 100 replies, 10 per thread) per video; skips ids already converted.
mkdir -p "$2"
while IFS= read -r id; do
  [ -z "$id" ] && continue
  [ -f "$3/$id.txt" ] || [ -f "$2/$id.info.json" ] && continue
  yt-dlp --skip-download --write-comments --no-warnings --extractor-args "youtube:max_comments=400,all,100,10;comment_sort=top" -o "$2/%(id)s" "https://www.youtube.com/watch?v=$id" >> "$2/log.txt" 2>&1
  sleep 3
done < "$1"
echo DONE >> "$2/log.txt"
