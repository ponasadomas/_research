#!/usr/bin/env bash
# Run a build's unfilter readers five at a time, verify each, rerun a failed one once,
# commit after every batch.   unfilter_run_readers.sh <niche> <id-prefix> <logdir>
set -u
NICHE="$1"; PREFIX="$2"; LOGS="$3"
T="$(cd "$(dirname "$0")" && pwd)"; REPO="$(git -C "$T" rev-parse --show-toplevel)"
B="mamivio.com/research/$NICHE"; D="$B/scratchpad/unfilter-reread"
cd "$REPO"; mkdir -p "$LOGS"
python3 -I "$T/${ASSIGN:-unfilter_assign.py}" "$NICHE" "$PREFIX" || exit 1
git add -A "$B" && git commit -q -m "$NICHE: unfilter reader assignments" 
run() { codex exec -s workspace-write -C "$REPO" -o "$D/ur$1.last.md" - < "$D/brief-ur$1.md" > "$LOGS/$NICHE-ur$1.log" 2>&1; }
ALL=$(ls "$D" | sed -n 's/^assign-ur\([0-9][0-9]\)\.tsv$/\1/p'); FAILED=""
set -- $ALL
while [ $# -gt 0 ]; do
  BATCH=""; for i in 1 2 3 4 5; do [ $# -gt 0 ] && { BATCH="$BATCH $1"; shift; }; done
  for nn in $BATCH; do python3 -I "$T/unfilter_verify_reader.py" "$NICHE" "$nn" "$PREFIX" >/dev/null 2>&1 || run "$nn" & done; wait   # skip a reader whose output already passes
  for nn in $BATCH; do
    if ! python3 -I "$T/unfilter_verify_reader.py" "$NICHE" "$nn" "$PREFIX"; then
      echo "rerunning ur$nn"; rm -f "$B/voice/reddit-ur$nn.jsonl" "$B/sources/reddit-reading-ur$nn.md"; run "$nn"
      python3 -I "$T/unfilter_verify_reader.py" "$NICHE" "$nn" "$PREFIX" || FAILED="$FAILED $nn"
    fi
  done
  git add -A "$B" && git commit -q -m "$NICHE: unfilter readers$BATCH" && echo "committed batch:$BATCH ($(date +%H:%M))"
done
echo "READERS-DONE $NICHE failed=[${FAILED# }]"
