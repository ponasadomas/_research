#!/usr/bin/env bash
# Send the coders of one pattern-sorting pass, all at once; coder 01's work is shown live.
#   _tools/run_coders.sh <dir> <prefix> <coders> <highest pattern number> <model> <effort>
# (run from ~/GitHub/_research, in a terminal a person can watch)
# Model and effort have no default: they are what the owner agreed to for this batch.
set -u
[ $# -eq 6 ] || { echo "usage: run_coders.sh <dir> <prefix> <coders> <top pattern> <model> <effort>"; exit 1; }
D="${1%/}"; PREFIX="$2"; N="$3"; TOP="$4"; MODEL="$5"; EFFORT="$6"; LOGS="$D/logs"; mkdir -p "$LOGS"
echo "$(date "+%Y-%m-%d %H:%M") codex $(codex --version 2>/dev/null | tail -1) | $N coders | model $MODEL | effort $EFFORT | prefix $PREFIX" >> "$D/sent.txt"
run() { sed "s/{NN}/$1/g" "$D/brief-coder.md" | codex exec -m "$MODEL" -c model_reasoning_effort="\"$EFFORT\"" -s workspace-write -C "$PWD" -o "$LOGS/$PREFIX$1.last.md" - 2>&1; }
ALL=$(seq -f "%02g" 1 "$N")
for nn in $ALL; do [ "$nn" = 01 ] || { run "$nn" > "$LOGS/$PREFIX$nn.log" & }; done
echo "=== $N coders sent $(date +%H:%M). Below: coder 01, live. The others write to $LOGS/ ==="
run 01 | tee "$LOGS/${PREFIX}01.log"
echo "=== coder 01 has stopped $(date +%H:%M). Waiting for the others. ==="; wait
FAILED=""
for nn in $ALL; do
  if ! python3 -I _tools/verify_coding.py "$D" "$PREFIX" "$nn" "$TOP"; then
    echo "redoing $PREFIX$nn whole ($(date +%H:%M))"; mkdir -p "$LOGS/failed-first-try"; mv -f "$D/coded-$PREFIX$nn.tsv" "$LOGS/failed-first-try/" 2>/dev/null
    run "$nn" > "$LOGS/$PREFIX$nn.retry.log"; python3 -I _tools/verify_coding.py "$D" "$PREFIX" "$nn" "$TOP" || FAILED="$FAILED $nn"
  fi
done
echo "CODERS-DONE failed=[${FAILED# }] ($(date +%H:%M))"
