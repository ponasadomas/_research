cd /home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour
for f in $(awk -F'\t' -v b=$1 '$1==b{print $3}' scratchpad/TR16/batches.tsv); do echo "######## $(basename $f .txt)"; cat $f; done
