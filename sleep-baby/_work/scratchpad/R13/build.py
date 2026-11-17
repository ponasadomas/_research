# usage: python3 -I build.py specs1.py specs2.py ... -> writes voice file
import json, re, sys, os
SB = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
UNITS = {os.path.basename(l.split('\t')[1].strip())[:-4]: l.split('\t')[1].strip() for l in open(os.path.join(SB,'scratchpad/R13/units.txt'))}
recs = []
SEED = set("night_wakings contact_naps short_naps wake_windows early_waking bedtime_battle regression_4_month feeding_to_sleep dream_feed night_weaning cosleeping bedsharing room_sharing transition_to_cot sleep_training_values cry_it_out ferber gentle_method chair_method pick_up_put_down consistency_failure partner_split_nights partner_disagreement daycare_naps nap_transition drop_nap sleep_props pacifier swaddle_transition white_noise schedule_rigidity sleep_consultant course_purchase app_tracking information_overload conflicting_advice maternal_exhaustion resentment guilt comparison_other_babies safe_sleep_fear money_back price_value personalization".split())
def add(unit, cid, speaker, stage, typ, themes, quote, context):
    rf = UNITS[unit]
    txt = open(os.path.join(SB, rf), encoding='utf-8').read()
    sub, pid = unit.rsplit('-', 1)
    if cid:
        m = re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)' % cid, txt)
    else:
        m = re.search(r'POST %s \| r/\S+ \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)' % pid, txt)
    assert m, (unit, cid)
    r = {"id": None, "source": "reddit r/" + sub, "url": m.group(2), "date": m.group(1), "speaker": speaker,
         "stage": stage, "type": typ, "themes": themes, "quote": quote, "context": context, "raw_file": rf,
         "source_class": "reddit_archive", "post_id": pid}
    if cid: r["comment_id"] = cid
    assert len(context.split()) <= 25, context
    themes[:] = [t for t in themes if t in SEED] + [t for t in themes if t not in SEED]
    recs.append(r)
for f in sys.argv[1:]:
    exec(open(f, encoding='utf-8').read())
out = os.path.join(SB, 'voice/reddit-r13.jsonl')
with open(out, 'w', encoding='utf-8') as o:
    for i, r in enumerate(recs, 1):
        r["id"] = "sb13-%04d" % i
        o.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(recs), "written")
