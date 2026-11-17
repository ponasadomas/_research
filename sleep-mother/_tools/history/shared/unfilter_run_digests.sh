#!/usr/bin/env bash
# Digest a build's re-read quotes in shares (five agents at a time), verify, commit, then run
# the final integration agent.   unfilter_run_digests.sh <niche> <id-prefix> <logdir> [quotes-per-share]
set -u
NICHE="$1"; PREFIX="$2"; LOGS="$3"; PER="${4:-1200}"
T="$(cd "$(dirname "$0")" && pwd)"; REPO="$(git -C "$T" rev-parse --show-toplevel)"
B="mamivio.com/research/$NICHE"; D="$B/scratchpad/unfilter-reread"; cd "$REPO"; mkdir -p "$LOGS"
commit() { for i in 1 2 3 4 5 6; do git add -A "$B" 2>/dev/null && git commit -q -m "$1" && return 0; sleep 5; done; }
DIGEST_BRIEF="${DIGEST_BRIEF:-brief-unfilter-digest.md}" python3 -I "$T/unfilter_assign_digests.py" "$NICHE" "$PER" || exit 1
run() { codex exec -s workspace-write -C "$REPO" -o "$D/digest-$1.last.md" - < "$D/brief-digest-$1.md" > "$LOGS/$NICHE-digest-$1.log" 2>&1; }
ALL=$(ls "$D" | sed -n 's/^brief-digest-\([0-9][0-9]\)\.md$/\1/p'); FAILED=""
set -- $ALL
while [ $# -gt 0 ]; do
  BATCH=""; for i in 1 2 3 4 5; do [ $# -gt 0 ] && { BATCH="$BATCH $1"; shift; }; done
  for nn in $BATCH; do run "$nn" & done; wait
  for nn in $BATCH; do
    if ! python3 -I "$T/unfilter_verify_digest.py" "$NICHE" "$nn"; then
      echo "rerunning digest $nn"; rm -f "$B/synthesis/unfilter-digest-$nn.md"; run "$nn"
      python3 -I "$T/unfilter_verify_digest.py" "$NICHE" "$nn" || FAILED="$FAILED $nn"
    fi
  done
  commit "$NICHE: unfilter digests$BATCH"; echo "committed digests:$BATCH ($(date +%H:%M))"
done
echo "DIGESTS-DONE $NICHE failed=[${FAILED# }]"
[ -n "$FAILED" ] && { echo "stopping before integration"; exit 1; }
POSTS=$(($(wc -l < "$D/queue.tsv") - 1)); READERS=$(ls "$B"/voice/reddit-ur*.jsonl | wc -l); QUOTES=$(cat "$B"/voice/reddit-ur*.jsonl | grep -c .)
sed -e "s#{NICHE}#$NICHE#g" -e "s#{POSTS}#$POSTS#g" -e "s#{READERS}#$READERS#g" -e "s#{QUOTES}#$QUOTES#g" -e "s#{PREFIX}#$PREFIX#g" "$T/${INTEGRATE_BRIEF:-brief-unfilter-integrate-digests.md}" > "$D/brief-integrate.md"
codex exec -s workspace-write -C "$REPO" -o "$D/integrate.last.md" - < "$D/brief-integrate.md" > "$LOGS/$NICHE-integrate.log" 2>&1
echo "INTEGRATE-DONE $NICHE exit=$?"
