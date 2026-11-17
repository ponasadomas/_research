#!/bin/bash
# usage: yt_search.sh <queries.txt> <out.tsv>
while IFS= read -r q; do
  [ -z "$q" ] && continue
  yt-dlp "ytsearch30:$q" --flat-playlist --print "%(id)s	%(view_count)s	%(channel)s	%(title)s	%(duration)s" 2>/dev/null | sed "s/^/$q	/" >> "$2"
  sleep 2
done < "$1"
