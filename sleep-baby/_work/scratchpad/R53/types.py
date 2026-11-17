import json,sys
T={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said','purchase','price_signal'}
S={'new_mother','experienced_mother','expecting_mother','recovered_parent','parent_unspecified','partner','relative_caregiver','advisor','professional','reviewer','skeptic','gave_up_parent'}
G={'newborn_0_8_weeks','baby_2_4_months','regression_4_months','baby_5_8_months','baby_9_12_months','toddler_12_24_months','toddler_24_36_months','looking_back','unknown'}
for k,r in enumerate(json.load(open(sys.argv[1]))):
    if r[4] not in T or r[2] not in S or r[3] not in G: print(k,r[2],r[3],r[4])
