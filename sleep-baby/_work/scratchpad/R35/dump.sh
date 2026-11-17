cd /home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby
i=0; while IFS=$'\t' read c u; do i=$((i+1)); if [ $i -ge $1 ] && [ $i -le $2 ]; then echo "=#=#= U$i $u"; cat "$u" | sed -E 's/\(https?:[^)]{80,}\)/(URL)/g'; fi; done < scratchpad/R35/units.tsv > scratchpad/R35/dump.txt
wc -c scratchpad/R35/dump.txt
