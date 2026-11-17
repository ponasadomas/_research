#!/usr/bin/env python3
"""One-time README vocabulary correction; exact excerpts and source files unchanged."""
from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
types=['desire','tried_failed','belief','advice_given','pain','success_story','success_story','pain','pain','question','question','desire','trigger_moment','regret','question','question','success_story','desire','pain','question','belief','fear','tried_failed','desire','success_story','belief','success_story','advice_given','tried_failed','success_story','success_story','success_story','advice_given','success_story','advice_given','tried_failed','objection','pain','objection','advice_given','question','pain','regret','question','pain','success_story','failure_story','success_story','pain','objection','pain','pain','failure_story','others_said','failure_story','desire','pain']
speaker={4:'advisor',26:'advisor',28:'advisor',29:'relative_caregiver',30:'relative_caregiver',33:'advisor',35:'advisor',37:'experienced_mother',40:'advisor',44:'expecting_mother',45:'expecting_mother',46:'expecting_mother',48:'expecting_mother',55:'partner',56:'relative_caregiver',57:'relative_caregiver'}
def digest(obj):return hashlib.sha256(json.dumps(obj,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def main():
 p=ROOT/'voice/oblique-deep-01.jsonl';a=[json.loads(s) for s in p.read_text().splitlines()]
 assert len(a)==len(types)==57
 immutable=lambda rows:[{k:r[k] for k in ['id','quote','raw_file','url','date','context']} for r in rows]
 original=digest(immutable(a));changes=[]
 for i,r in enumerate(a,1):
  if 'original_reader_speaker' in r:raise RuntimeError('Already normalized')
  old={k:r[k] for k in ['speaker','type']}
  r['original_reader_speaker']=r['speaker'];r['original_reader_type']=r['type']
  r['speaker']=speaker.get(i,'parent_unspecified');r['type']=types[i-1]
  basis='Gender and mother identity not inferred; parent/family context or identity remains unspecified.'
  if r['speaker']=='advisor':basis='The selected original passage gives advice or a general opinion; professional credentials not inferred.'
  if r['speaker']=='relative_caregiver':basis='Original author explicitly describes their daughter/grandchild and speaks as the relative.'
  if r['speaker']=='expecting_mother':basis='Original author identifies as a first-time mum and describes their current pregnancy.'
  if i==37:basis='Original author explicitly calls themself a mom and describes employment and nanny care.'
  if i==55:basis='Original author explicitly describes their wife and shared daughter; no gender inferred.'
  changes.append({'id':r['id'],'before':old,'after':{k:r[k] for k in ['speaker','type']},'basis':basis})
 assert original==digest(immutable(a))
 p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in a))
 log={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reason':'Parent metadata audit: align finished records with README speaker/type vocabulary','immutable_fields_hash_before_after':original,'ids_quotes_raw_urls_dates_contexts_unchanged':True,'records':changes,'new_voice_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 (ROOT/'sources/oblique-deep-metadata-corrections.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
 audit=ROOT/'sources/oblique-deep-audit.json';d=json.loads(audit.read_text());d['voice_sha256']=log['new_voice_sha256'];d['metadata_correction_log']='sources/oblique-deep-metadata-corrections.json';d['metadata_corrected_utc']=log['date_utc'];audit.write_text(json.dumps(d,indent=2)+'\n')
 print('Normalized57 records; immutable excerpt/source fields unchanged; SHA256',log['new_voice_sha256'])
if __name__=='__main__':main()
