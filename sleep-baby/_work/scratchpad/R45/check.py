import glob
T=set("trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said purchase price_signal".split())
S=set("newborn_0_8_weeks baby_2_4_months regression_4_months baby_5_8_months baby_9_12_months toddler_12_24_months toddler_24_36_months looking_back unknown".split())
P=set("new_mother experienced_mother expecting_mother recovered_parent parent_unspecified partner relative_caregiver advisor professional reviewer skeptic gave_up_parent".split())
for f in sorted(glob.glob("q*.tsv")):
    for i,l in enumerate(open(f),1):
        p=[x.strip() for x in l.split(" || ")]
        if len(p)<8: continue
        if p[2] not in P or p[3] not in S or p[4] not in T: print(f,i,p[2],p[3],p[4])
