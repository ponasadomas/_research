import collections, hashlib, json, re
from pathlib import Path
from reader import ROOT, WORK, MANIFEST

d=json.loads((WORK/'decisions.json').read_text())
quotes=d['quotes']; threads=d['threads']
# Recount OP posts from native metadata; prose counts are not authoritative.
for m in MANIFEST:
 t=threads[m['thread_id']]
 if t['fully_read']:
  native=json.loads((ROOT/m['thread_json']).read_text())
  n=sum(p['is_op'] for p in native['posts'])
  t['reason']=re.sub(r'and (?:two|three|four|five|six|seven|eight|nine|ten|\d+) OP (posts|questions)',lambda z:'and '+str(n)+' OP '+z.group(1),t['reason'])
threads['4367609']['reason']=threads['4367609']['reason'].replace('all four OP updates','all four OP posts')
threads['4367609']['post_read_eligible']=0
threads['4448109']['post_read_eligible']=0
threads['6165381']['reason']=threads['6165381']['reason'].replace('Nonparent giver','Gift giver with no stated parent identity')
# Final metadata pass: purchases and intentions alone do not prove improvement.
fix={
 'odeep04-0021': {'quote':"doubles tend to all do a mediocre to less mediocre annoying job at what they do and it's finding the ones with the least trade-offs."},
 'odeep04-0003': {'stage':'unknown'},
 'odeep04-0020': {'speaker':'parent_unspecified'},
 'odeep04-0041': {'speaker':'parent_unspecified'},
 'odeep04-0065': {'context':"Granny bought a reviewed car seat but finds her general-review subscription insufficient for the next occasional-use, lower-budget purchase; payment terms unstated."},
 'odeep04-0023': {'type':'belief'},
 'odeep04-0030': {'stage':'unknown'},
 'odeep04-0031': {'stage':'unknown'},
 'odeep04-0045': {'type':'belief'},
 'odeep04-0069': {'type':'belief'},
 'odeep04-0079': {'type':'belief'},
 # Own pregnancy/mother identity is not explicit in these original authors' text.
 'odeep04-0010': {'speaker':'parent_unspecified','context':"Preparing for first baby; considering cloth nappies for cost and environment, asks users before investing."},
 'odeep04-0011': {'speaker':'parent_unspecified','stage':'unknown'},
 'odeep04-0014': {'speaker':'parent_unspecified','context':"Respondent describes a small casual wardrobe of maternity basics and cardigans, using eBay for work clothes."},
 'odeep04-0043': {'speaker':'parent_unspecified'},
 'odeep04-0045': {'speaker':'parent_unspecified','type':'belief'},
 'odeep04-0069': {'speaker':'parent_unspecified','type':'belief'},
 'odeep04-0079': {'speaker':'advisor','type':'belief','context':"Gift buyer abandons proposed baby advice book after peer discussion; planner is a generic gift with no recipient outcome."},
}
fix['odeep04-0021']['stage']='unknown'
for q in quotes:q.update(fix.get(q['id'],{}))
voice=ROOT/'voice/oblique-deep-04.jsonl'
voice.write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in quotes))

ledger=[]
for m in MANIFEST:
 i=m['thread_id'];t=threads[i]
 ledger.append(dict(thread_id=i,status=t['status'],fully_read=t['fully_read'],posts_read=t['posts_read'],posts_total=t['posts_total'],post_read_eligible=t['post_read_eligible'],reason=t['reason'],raw_file=t['raw_file'],quote_ids=[q['id'] for q in quotes if q['thread_id']==i]))
lf=ROOT/'sources/mse-completion-02-reading.jsonl'
lf.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in ledger))

counts={
 'assigned_threads':len(MANIFEST),'assigned_posts':sum(x['posts'] for x in MANIFEST),
 'assigned_pages':sum(x['pages'] for x in MANIFEST),'assigned_chunks':31,
 'full_threads':sum(x['fully_read'] for x in ledger),
 'full_thread_posts':sum(x['posts_total'] for x in ledger if x['fully_read']),
 'partial_safety_excluded_threads':sum(not x['fully_read'] for x in ledger),
 'partial_posts_read':sum(x['posts_read'] for x in ledger if not x['fully_read']),
 'total_posts_read':sum(x['posts_read'] for x in ledger),
 'deliberately_unread_posts':sum(x['posts_total']-x['posts_read'] for x in ledger),
 'quotes':len(quotes),'quoted_threads':len(set(q['thread_id'] for q in quotes)),
 'source_selected_posts':len(set((q['thread_id'],q['post_id']) for q in quotes)),
}
(WORK/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
lines=['# MSE completion batch 02: reading ledger','',
 'Completed 2026-10-24. This is one frozen assignment, not a prevalence sample. No network collection, outreach, accounts, subagents or edits to global findings.',
 '',
 'The batch contains 104 whole discussions, 1,457 visible posts, 191 captured pages and 31 chunks. All 31 chunks were processed. Actual full reads: **100 discussions / 1,366 posts**. Four discussions were stopped for safety after **42 posts** combined; their **49 remaining posts** are deliberately unread. Total posts actually read: **1,408**. Full reads include unquoted and wholly ineligible discussions; they are not automatically market evidence.',
 '',
 f"Selected evidence: **{counts['quotes']} excerpts from {counts['quoted_threads']} discussions and {counts['source_selected_posts']} original posts**. Counted from the finished files; no quota or purchaser prevalence implied.",
 '',
 '`post_read_eligible` is a count of posts eligible for further practical evidence selection after discussion-level screening. It is zero for the four partial safety exclusions and four fully exposed but wholly ineligible discussions (4367609, 4448109, 4750904, 5873485). A nonzero value does not mean every passage was suitable or quoted. Incidental clinical, loss, child-safety and abusive passages were excluded from extraction in otherwise practical discussions.',
 '',
 'Reading used immutable v2 individual units and their underlying native post JSON, including every unique `body_with_quotes` paragraph and OP follow-up. The display renderer abbreviates only exact paragraphs already displayed in the same discussion, with the prior post ID; it never removes unique quoted context. Two tool-output truncations were recovered by reading the complete affected post/range (4388437/Comment_58653003; 4718725/Comment_62864866 through Comment_62888528). Quoted material is always attached to its actual original author/post, and every chosen excerpt is present in the author\'s unquoted native body.',
 '',
 'Four precise partial exclusions: 4883262 (1/5 posts); 4978593 (6/15); 5782171 (34/66, through Comment_73774772); 5842375 (1/5). Their remaining individual-unit passages are not full-read. All 22 posts of 4750904 and all four posts of 5873485 were exposed and read, then fully excluded from excerpts: this ledger truthfully retains them as full reads, not OP-only exclusions. Clinical discussion 4367609 was fully read but never excerpted.',
 '',
 'The quoted record at 4936780 is only the OP\'s resolved work-choice outcome after reading all 63 posts and follow-ups. OP disclosed no violence or threat; third-party hostile labels are not treated as factual diagnoses. Later thread 5015478 has the same native author ID and shows that the resolved hours choice still leaves a savings constraint.',
 '',
 'Historical prices, benefit eligibility, employment rules, health claims, product availability and event dates are not current guidance. Paid gear, human help, reported general-review subscriptions and planner gifts are distinct from willingness to buy a personalised report. The Which? subscriber does not state payment terms. No personalised-report purchase was observed. Current free tailoring competitors named in the assignment (StarterSet and Babylist) remain unresolved competition, not validated by these historical posts.',
 '',
 '## Complete per-discussion ledger','',
 '| Thread | Pages | Read / total posts | Status | Excerpts | Reading outcome |',
 '|---|---:|---:|---|---|---|']
for m,l in zip(MANIFEST,ledger):
 reason=l['reason'].replace('|','/');ids=', '.join(l['quote_ids']) or 'None'
 lines.append(f"| {m['thread_id']} — {m['title'].replace('|','/')} | {m['pages']} | {l['posts_read']}/{l['posts_total']} | {l['status']} | {ids} | {reason} |")
lines.extend(['','## Unread boundary','',
 'No permitted assigned discussion remains unfinished. The 49 deliberately unread posts are the tails of the four partial safety exclusions, located at:',
 '',*['- `'+x['raw_file']+'` — '+str(x['posts_total']-x['posts_read'])+' remaining posts.' for x in ledger if not x['fully_read']],
 '', 'All other batches, GeoBaby threads and pre-existing global gaps are outside this reader\'s assignment. No global completion claim is made.',
 '', '## Local theme additions','',
 'The README speaker/stage/type vocabularies are unchanged. Additional themes describe observed jobs or constraints: `budget`, `gear_preparation`, `maternity_budget`, `nappy_choice`, `second_hand`, `home_layout`, `laundry_capacity`, `tradeoff`, `gift_mismatch`, `hidden_costs`, `retailer_trust`, `maternity_clothing`, `financial_independence`, `identity`, `group_access`, `father_involvement`, `family_influence`, `baby_clothing`, `purchase_observed`, `contrary_evidence`, `tried_failed`. `purchase_observed` identifies a record with a separately described actual purchase, not a proven causal outcome or report customer; `contrary_evidence` marks a counterexample. Existing equivalent local themes were reused where available.',
 '', '## Artifacts and audit','',
 '- `voice/oblique-deep-04.jsonl`: fresh prefix `odeep04-`, 81 excerpts.',
 '- `sources/mse-completion-02-reading.jsonl`: exact assigned ID set, one row per discussion.',
 '- `synthesis/reader-notes-mse-completion-02.md`: interpretation with IDs checked after writing.',
 '- `sources/mse-completion-02-audit.json`: strict body/metadata/word-limit/ledger/hash verification.',
 '- `scratchpad/mse-completion-02/`: incremental reading decisions, finaliser and reproducible audit; immutable captured evidence was not rewritten.',
 ''])
(ROOT/'sources/mse-completion-02.md').write_text('\n'.join(lines))
print(json.dumps(counts,indent=2))
