#!/usr/bin/env bash
cd /home/thinkpad/GitHub/mamiVio.com/research/kinedu-aq-assessment
while ! grep -q '^exit=' logs/phase5.run.log; do sleep 30; done
echo "phase5 finished at $(date -Is); starting phase6" > logs/phase6.queue.log
codex exec --skip-git-repo-check -s workspace-write -c 'sandbox_workspace_write.network_access=true' -C "$PWD" -o logs/phase6.last.md - < logs/brief-phase6-area-sweep.md > logs/phase6.run.log 2>&1; echo "exit=$?" >> logs/phase6.run.log
