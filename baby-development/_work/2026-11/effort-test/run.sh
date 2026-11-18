#!/usr/bin/env bash
# Effort test: the same 150 posts read at medium (shown live) and at high (to a log).
cd ~/GitHub/_research; T=baby-development/_work/2026-11/effort-test
brief() { sed -e "s/{NN}/01/g" -e "s/{PREFIX}/$1/g" -e "s|{DIR}|$T|g" -e "s|{QUOTES}|$T|g" baby-development/_work/2026-11/brief-read-and-sort.md; }
echo "$(date "+%Y-%m-%d %H:%M") effort test | gpt-6.1-sol | tm = medium, th = high | 150 posts each" >> $T/sent.txt
date +%s > $T/start.txt
( brief th | codex exec -m gpt-6.1-sol -c model_reasoning_effort='"high"' -s workspace-write -C "$PWD" -o $T/logs/th01.last.md - > $T/logs/th01.log 2>&1; date +%s > $T/end-th.txt ) &
echo "=== 2 test agents sent $(date +%H:%M). Below: the MEDIUM one, live. ==="
brief tm | codex exec -m gpt-6.1-sol -c model_reasoning_effort='"medium"' -s workspace-write -C "$PWD" -o $T/logs/tm01.last.md - 2>&1 | tee $T/logs/tm01.log; date +%s > $T/end-tm.txt
echo "=== medium has stopped $(date +%H:%M). Waiting for high. ==="; wait
python3 -I _tools/verify_pass.py $T $T tm 01 12; python3 -I _tools/verify_pass.py $T $T th 01 12
echo "TEST-DONE $(date +%H:%M)"
