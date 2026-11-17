import sys, json, importlib
sys.path.insert(0, "/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/scratchpad/R14")
import lib
SEED = set('night_wakings contact_naps short_naps wake_windows early_waking bedtime_battle regression_4_month feeding_to_sleep dream_feed night_weaning cosleeping bedsharing room_sharing transition_to_cot sleep_training_values cry_it_out ferber gentle_method chair_method pick_up_put_down consistency_failure partner_split_nights partner_disagreement daycare_naps nap_transition drop_nap sleep_props pacifier swaddle_transition white_noise schedule_rigidity sleep_consultant course_purchase app_tracking information_overload conflicting_advice maternal_exhaustion resentment guilt comparison_other_babies safe_sleep_fear money_back price_value personalization'.split())
TMAP = {"only_mum_settles_reverse": "parent_preference", "grandparent_help": "relative_caregiver_conflict",
        "free_advice_followed": "free_advice_fail", "vomiting_stops_cio": "vomiting_stop",
        "paid_plan_not_personal": "plan_not_personal", "purchase_half_asleep": "night_panic_buy",
        "relative_night_help": "relative_help"}
UNSPEC = {"sleeptrain-1wq5f45","sleeptrain-1wpo28m","sleeptrain-1wq1m6n","beyondthebump-1xc7b9o","NewParents-1xd1xv7",
          "sleeptrain-1xdkv7u","sleeptrain-1xaflyw","sleeptrain-1wq5zmt","beyondthebump-1wyg2k4","NewParents-1x1zff8",
          "sleeptrain-1wqdfhj","beyondthebumpUK-1wqltl3","sleeptrain-1wqwfw3","beyondthebump-1wqynoc"}
for m in sys.argv[2:]:
    importlib.import_module(m)
with open(sys.argv[1], "w", encoding="utf-8") as f:
    for i, r in enumerate(lib.RECS, 1):
        r["id"] = f"sb14-{i:04d}"
        assert r["context"]
        unit = r["raw_file"].rsplit("/", 1)[1][:-4]
        if unit in UNSPEC: r["speaker"] = "parent_unspecified"
        if unit == "sleeptrain-1wqstba": r["speaker"] = "experienced_mother"
        th = []
        for t in r["themes"]:
            t = TMAP.get(t, t)
            if t not in th: th.append(t)
        if unit in ("sleeptrain-1wq4awk",) and "relative_caregiver_conflict" in th:
            pass
        r["themes"] = sorted(th, key=lambda t: t not in SEED)
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(lib.RECS))
