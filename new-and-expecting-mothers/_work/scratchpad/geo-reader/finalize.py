import json,hashlib,re,collections
from pathlib import Path
R=Path(__file__).resolve().parents[2]
vp=R/'voice/oblique-deep-02.jsonl'; lp=R/'sources/geobaby-deep-reading.jsonl'
v=[json.loads(x) for x in vp.read_text().splitlines()];l=[json.loads(x) for x in lp.read_text().splitlines()]
changes=[]
def change(i,field,value,reason):
 q=next(q for q in v if q['id']=='odeep02-%04d'%i)
 if q[field]!=value:changes.append(dict(id=q['id'],field=field,before=q[field],after=value,reason=reason));q[field]=value
for i in [7,20,31,36,38,39,40,62,66,70]:change(i,'speaker','parent_unspecified','Selected author has parent/expecting-family context without an explicit self-identification as mother in the cited post; conservative role.')
change(16,'stage','pregnancy_early','Stated August 21 due date and May 6 post put pregnancy near 24 weeks, before late pregnancy.')
change(28,'speaker','experienced_mother','Author describes experience after first child and contrasts maternal confidence; new_mother overstates current stage.')
for i in [55,66,93,109]:change(i,'stage','unknown','No sufficiently precise gestational age established at selected-post date; avoid guessed early/late assignment.')
change(18,'type','belief','Advocacy of feasibility without a detailed first-person use outcome; do not label demonstrated success.')
change(18,'themes',['twins','price_value'],'Nappy economy belongs to price_value, not food_budget.')
change(60,'themes',['not_enough_time','price_value'],'Remove unnecessary custom theme that duplicates an existing type.')
change(111,'type','belief','Confirmed group creation is an action, with no demonstrated support outcome yet.')
uncertain={'166090':'First visible post begins as another participant response; originating question is absent from the visible capture.','166302':'First visible post responds to prior question about hours; originating question is absent from the visible capture.','166622':'Wanted/borrow title contrasts with first visible sale offer; originating request/role cannot be independently established.'}
for row in l:
 row['reading_scope']='all_captured_visible_posts_including_body_with_quotes'
 row['complete_original_thread_verified']=row['thread_id'] not in uncertain
 row['is_op_semantics']='frozen extraction flag; does not independently prove original question author'
 if row['thread_id'] in uncertain:
  row['source_role_uncertain']=True;row['source_role_uncertainty_reason']=uncertain[row['thread_id']]
 if row['thread_id']=='124580':row['note']='Twin-parent OP advocates cloth feasibility against reported workload objections, without detailed personal use or purchase outcome. Expecting parent asks tiny-baby fit without reply; late generic poll not independent testimony. Advocacy counterevidence, not demonstrated sustained use.'
for q in v:
 if q['thread_id'] in uncertain:q['source_role_uncertain']=True
vp.write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in v));lp.write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in l))
(R/'sources/geobaby-deep-metadata-audit.json').write_text(json.dumps({'changes':changes,'uncertain_first_visible_threads':uncertain,'uncertain_thread_selected_ids':[q['id'] for q in v if q.get('source_role_uncertain')],'note':'Each selected quote is from actual author-owned body, not a repeated quotation. Uncertainty concerns original question/OP provenance; frozen is_op unchanged.'},indent=2)+'\n')
print('Final metadata edits',len(changes))
