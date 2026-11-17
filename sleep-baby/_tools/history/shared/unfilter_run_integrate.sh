#!/usr/bin/env bash
# Run the integration agent for one build.   unfilter_run_integrate.sh <niche> <id-prefix> <logdir>
set -u
NICHE="$1"; PREFIX="$2"; LOGS="$3"
T="$(cd "$(dirname "$0")" && pwd)"; REPO="$(git -C "$T" rev-parse --show-toplevel)"
B="mamivio.com/research/$NICHE"; D="$B/scratchpad/unfilter-reread"; cd "$REPO"; mkdir -p "$LOGS"
POSTS=$(($(wc -l < "$D/queue.tsv") - 1)); READERS=$(ls "$B"/voice/reddit-ur*.jsonl | wc -l); QUOTES=$(cat "$B"/voice/reddit-ur*.jsonl | grep -c .)
sed -e "s#{NICHE}#$NICHE#g" -e "s#{POSTS}#$POSTS#g" -e "s#{READERS}#$READERS#g" -e "s#{QUOTES}#$QUOTES#g" -e "s#{PREFIX}#$PREFIX#g" "$T/brief-unfilter-integrate.md" > "$D/brief-integrate.md"
codex exec -s workspace-write -C "$REPO" -o "$D/integrate.last.md" - < "$D/brief-integrate.md" > "$LOGS/$NICHE-integrate.log" 2>&1
echo "INTEGRATE-DONE $NICHE exit=$?"
