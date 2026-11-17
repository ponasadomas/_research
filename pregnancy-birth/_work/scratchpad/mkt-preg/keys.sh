#!/bin/bash
# keys.sh slugprefix [maxlines] : key lines from all raw txt for a seller
D=/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/_raw/competitors
N=${2:-60}
for f in $D/$1*.txt; do echo "######## $(basename $f) | $(sed -n 2p $f)"; sed '1,/^-----/d' "$f" | grep -nE '^#|[$£€][0-9]|refund|guarantee|money.back|personali|tailor|second (baby|pregnan|time)|toddler|first.time|trimester|week|anxi|fear|pain|shorter|tear|calm|confiden|partner|reviews?|rated|★|[0-9,]+\+? (mums|moms|women|parents|families|couples)|insurance|HSA|lifetime|access' | awk 'length($0)<260' | head -$N; done
