#!/usr/bin/env python3
"""Hand classification of the 164 restricted ids (merged flag + restricted-ids.md) by reason,
from the reasons in synthesis/restricted-ids.md and the reader-notes restricted tables.
Run: python3 -I scratchpad/FINDINGS/restricted_categories.py"""
import subprocess, collections
C = {
 'safe_sleep': 'sb04-0152 sb04-0171 sb04-0235 sb04-0271 sb04-0308 sb05-0022 sb05-0282 sb06-0228 sb07-0130 sb07-0204 '
   'sb10-0002 sb10-0041 sb10-0100 sb10-0112 sb10-0118 sb10-0231 sb10-0234 sb11-0085 sb11-0202 sb14-0067 sb14-0068 sb14-0175 '
   'sb16-0255 sb16-0256 sb16-0257 sb17-0026 sb17-0107 sb17-0121 sb17-0180 sb18-0102 sb18-0112 sb19-0014 sb19-0117 '
   'sb19-0216 sb19-0217 sb19-0218 sb19-0219 sb19-0235 sb20-0240 sb21-0194 sb21-0276 sb21-0335',
 'mental_health': 'sb03-0142 sb05-0153 sb05-0274 sb07-0025 sb08-0201 sb10-0010 sb10-0086 sb10-0096 sb10-0124 sb10-0156 '
   'sb10-0168 sb10-0175 sb10-0192 sb10-0255 sb10-0256 sb11-0054 sb11-0204 sb16-0130 sb16-0231 sb16-0232 sb17-0100 sb17-0133 '
   'sb18-0168 sb19-0041 sb19-0042 sb20-0016 sb20-0017 sb20-0018 sb20-0064 sb20-0320 sb20-0338 sb20-0339 sb20-0345 sb20-0360 '
   'sb21-0106 sb21-0160 sb21-0235 sb21-0261 sb21-0330 sb21-0339 sb21-0357 sb21-0372',
 'medical_secondhand': 'sb08-0165 sb10-0176 sb10-0273 sb11-0089 sb11-0216 sb16-0113 sb16-0117 sb16-0248 sb18-0052 sb18-0057 '
   'sb18-0101 sb18-0194 sb18-0340 sb19-0022 sb19-0034 sb19-0244 sb19-0245 sb19-0251 sb19-0265 sb20-0029 sb20-0071 sb20-0095 '
   'sb20-0250 sb21-0058 sb21-0097 sb21-0098 sb21-0122 sb21-0268 sb21-0303',
 'crying_harms_belief': 'sb03-0007 sb10-0165 sb10-0206 sb20-0324 sb21-0024 sb21-0130 sb21-0172 sb21-0316 sb21-0377 sb21-0378 sb21-0379',
 'distress_image': 'sb13-0145 sb18-0207 sb18-0219 sb20-0279 sb21-0108 sb21-0346',
 'exhaustion_danger': 'sb07-0224 sb08-0141 sb08-0142 sb08-0265 sb10-0101 sb10-0102 sb12-0186',
 'anger_at_child': 'sb07-0173 sb14-0213 sb18-0001 sb18-0157',
 'mixed_reader_list': 'sb09-0052 sb09-0055 sb09-0085 sb09-0117 sb09-0154 sb09-0189 sb09-0198 sb09-0237 sb09-0289 '
   'sb15-0033 sb15-0129 sb15-0142 sb15-0259',
 'other': 'sb02-0166 sb04-0067 sb06-0025 sb18-0240 sb21-0219 sb21-0311 sb19-0094 sb20-0062 sb20-0145 sb20-0146',
}
R=set(subprocess.run(['python3','-I','scratchpad/FINDINGS/q.py','restricted'],capture_output=True,text=True).stdout.split('\n')[1].split())
seen=collections.Counter()
for k,v in C.items():
    ids=v.split(); seen.update(ids); print(k, len(ids))
allc=set(seen)
print('total classified', len(allc), 'dupes', [i for i,n in seen.items() if n>1])
print('restricted not classified', sorted(R-allc)); print('classified not restricted', sorted(allc-R))
