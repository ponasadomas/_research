#!/usr/bin/env python3
"""Reviewed per-record README vocabulary correction; preserve raw/quotes/IDs and former detail."""
import datetime,hashlib,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
S=[
('fdeep01-0001','return_to_work','objection','Primary trigger is return to12hour shifts, not an inferred gender or clinical condition.'),
('fdeep01-0002','looking_back','tried_failed','Past purchase of expensive bottles did not achieve intended acceptance.'),
('fdeep01-0003','unknown','desire','Expressed resale interest is desire; sale and parental stage are unconfirmed.'),
('fdeep01-0004','looking_back','advice_given','Recommends free/cheap human support and describes past experience, not an observed current offer.'),
('fdeep01-0005','unknown','belief','Existing-method satisfaction/term curiosity is a stance; actual baby age is unspecified.'),
('fdeep01-0006','unknown','objection','Repeated book browsing without using recipes supports a usage objection, not inferred regret or purchase.'),
('fdeep01-0007','unknown','desire','Considering another career is a stated desire; gestational stage is not stated.'),
('fdeep01-0008','unknown','pain','Time pressure when planning another child; not yet established as pregnant.'),
('fdeep01-0009','pregnancy_early','pain','Body explicitly says3months pregnant; retain parent_unspecified conservatively.'),
('fdeep01-0010','looking_back','objection','Past bottle-use experience and price objection; no current child age established.'),
('fdeep01-0011','baby_6_12_months','success_story','OP has10month child and credits peers for a resolved decision; no clinical outcome asserted.'),
('fdeep02-0001','pregnancy_late','desire','Original post explicitly says35weeks; parental attention planning is desired.'),
('fdeep02-0002','unknown','desire','Wants face-to-face knowledgeable support; pregnancy stage is unstated.'),
('fdeep02-0003','looking_back','objection','Retrospective packing experience says many items unnecessary, not a current purchase failure.'),
('fdeep02-0004','baby_6_16_weeks','pain','Original title establishes7week baby; worry concerns packing for a trip.'),
('fdeep02-0005','toddler','pain','OP explicitly has2year child with space/transport constraints; not infant evidence.'),
('fdeep02-0006','unknown','objection','Explicit outing budget ceiling; baby age and report budget are unstated.'),
('fdeep02-0007','unknown','objection','Childcare cost is a barrier; children ages are unspecified.'),
('fdeep02-0008','unknown','pain','Young-baby context but no exact age; household recognition complaint.'),
('fdeep02-0009','unknown','question','Puree equipment inquiry; starting solids alone does not establish an age band.'),
('fdeep02-0010','unknown','success_story','Reports actual partner help enabling rest; child age is not stated in quoted unit.'),
('fdeep02-0011','unknown','fear','Anticipates preparation-time difficulty for proposed diet; actual child age is unconfirmed.'),
('fdeep02-0012','unknown','objection','Cost/laundry objection; no gestational band established.'),
('fdeep02-0013','unknown','tried_failed','Lists attempted cleaning products without success; child age is not established.'),
('fdeep02-0014','baby_6_12_months','question','OP explicitly has7month child and asks which sauces are suitable.'),
('fdeep02-0015','toddler','success_story','Source says child isone; conservatively toddler, not an invented exact12month age.'),
]
M={x[0]:x[1:] for x in S};log=[];changed=[];before=[];after=[]
for filename in ['forums-deep-01.jsonl','forums-deep-02.jsonl']:
    path=ROOT/'voice'/filename;rows=[json.loads(x) for x in path.read_text().splitlines()]
    for x in rows:
        before.append((x['id'],x['quote'],x['raw_file'],x['url']))
        stage,typ,reason=M[x['id']]
        old={k:x[k] for k in ['speaker','stage','type']}
        for k in old:x.setdefault('original_reader_'+k,old[k])
        x.update(speaker='parent_unspecified',stage=stage,type=typ)
        x['metadata_normalization_note']=reason.replace('to12hour','to 12 hour').replace('says3months','says 3 months').replace('has10month','has 10 month').replace('says35weeks','says 35 weeks').replace('establishes7week','establishes 7 week').replace('has2year','has 2 year').replace('has7month','has 7 month').replace('isone','is one').replace('exact12month','exact 12 month')
        log.append({'id':x['id'],'before':old,'after':{k:x[k] for k in old},'reason':x['metadata_normalization_note'],'richer_detail_preserved_in':['original_reader_speaker','original_reader_stage','original_reader_type']})
        after.append((x['id'],x['quote'],x['raw_file'],x['url']))
    path.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows));changed.append(str(path.relative_to(ROOT)))
assert before==after
out={'corrected_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':changed,'records_reviewed':len(log),'quotes_ids_raw_paths_urls_unchanged':True,'speaker_policy':'Conservative parent_unspecified for all26; pregnancy/breastfeeding does not establish self-identification as mother.','corrections':log}
(ROOT/'sources/forums-deep-metadata-corrections.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print({'records_reviewed':len(log),'ids_quotes_raw_urls_unchanged':True})
