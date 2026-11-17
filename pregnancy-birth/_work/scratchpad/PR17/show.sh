cd /home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth
for u in $(awk -F'\t' -v b="$1" '$1==b{print $3}' scratchpad/PR17/batches.tsv); do echo "=================== $u"; cat "$u"; echo; done
