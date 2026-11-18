#!/usr/bin/env bash
# Send the readers of one sample reading, all at once, check each, and redo a failed one once.
#   _tools/run_readers.sh <niche> <niche>/_work/<round>/<label> <prefix> <readers> <model> <effort> <logdir>
# (run from ~/GitHub/_research)
# Model and effort have no default: they are what the owner agreed to for this batch, and
# they are passed to Codex explicitly, so a changed ~/.codex/config.toml cannot alter them.
# What was sent is written to <dir>/sent.txt.
# The brief is <dir>/brief-reader.md with {NN} standing for the reader's number.
set -u
[ $# -eq 7 ] || { echo "usage: run_readers.sh <niche> <dir> <prefix> <readers> <model> <effort> <logdir>"; exit 1; }
NICHE="$1"; D="${2%/}"; PREFIX="$3"; N="$4"; MODEL="$5"; EFFORT="$6"; LOGS="$7"; mkdir -p "$LOGS"
echo "$(date "+%Y-%m-%d %H:%M") codex $(codex --version 2>/dev/null | tail -1) | $N readers | model $MODEL | effort $EFFORT | prefix $PREFIX" >> "$D/sent.txt"
run() { sed "s/{NN}/$1/g" "$D/brief-reader.md" | codex exec -m "$MODEL" -c model_reasoning_effort="\"$EFFORT\"" -s workspace-write -C "$PWD" -o "$LOGS/$PREFIX$1.last.md" - > "$LOGS/$PREFIX$1.log" 2>&1; }
ALL=$(seq -f "%02g" 1 "$N"); FAILED=""
for nn in $ALL; do [ -f "$D/reader-$nn.tsv" ] || { echo "no share for reader $nn"; exit 1; }; done
status() {   # one line per reader, so a person watching can see that work is going on
  echo "--- $(date +%H:%M:%S)  $N readers, model $MODEL, effort $EFFORT"
  for nn in $ALL; do
    P="$D/posts-$PREFIX$nn.tsv"; Q="$NICHE/quotes/reddit-$PREFIX$nn.jsonl"; L="$LOGS/$PREFIX$nn.log"
    rows=$([ -f "$P" ] && echo $(( $(wc -l < "$P") - 1 )) || echo 0); quotes=$([ -f "$Q" ] && wc -l < "$Q" || echo 0)
    age=$([ -f "$L" ] && echo $(( $(date +%s) - $(stat -c %Y "$L") )) || echo "-")
    echo "  reader $nn: $rows of $(( $(wc -l < "$D/reader-$nn.tsv") - 1 )) posts written down, $quotes quotes, last sign of life ${age}s ago"
  done
}
for nn in $ALL; do python3 -I _tools/verify_reading.py "$NICHE" "$D" "$PREFIX" "$nn" >/dev/null 2>&1 || run "$nn" & done
echo "sent $(date +%H:%M). Readers usually write their files near the end, so the post numbers stay at 0 for a long time."
while [ -n "$(jobs -r)" ]; do status; sleep 30; done; wait; status
for nn in $ALL; do
  if ! python3 -I _tools/verify_reading.py "$NICHE" "$D" "$PREFIX" "$nn"; then
    echo "redoing $PREFIX$nn whole ($(date +%H:%M))"
    mkdir -p "$LOGS/failed-first-try"; mv -f "$NICHE/quotes/reddit-$PREFIX$nn.jsonl" "$D/posts-$PREFIX$nn.tsv" "$D/notes-$PREFIX$nn.md" "$LOGS/failed-first-try/" 2>/dev/null
    run "$nn"; python3 -I _tools/verify_reading.py "$NICHE" "$D" "$PREFIX" "$nn" || FAILED="$FAILED $nn"
  fi
done
echo "READERS-DONE failed=[${FAILED# }] ($(date +%H:%M))"
