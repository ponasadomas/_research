import json,sys
S={"new_mother","experienced_mother","expecting_mother","recovered_parent","parent_unspecified","partner","relative_caregiver","advisor","professional","reviewer","skeptic","gave_up_parent"}
ST={"newborn_0_8_weeks","baby_2_4_months","regression_4_months","baby_5_8_months","baby_9_12_months","toddler_12_24_months","toddler_24_36_months","looking_back","unknown"}
T={"trigger_moment","pain","fear","tried_failed","desire","belief","question","objection","advice_given","success_story","failure_story","regret","others_said","purchase","price_signal"}
ids=set()
for l in open(sys.argv[1]):
    r=json.loads(l); assert r["id"] not in ids; ids.add(r["id"])
    for k,v in (("speaker",S),("stage",ST),("type",T)):
        if r[k] not in v: print(r["id"],k,r[k])
print(len(ids),"checked")
