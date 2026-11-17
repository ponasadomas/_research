#!/usr/bin/env python3
"""Consolidate preserved ordinary-access probes; classifications are manual observations."""
import json,pathlib,urllib.parse,collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/forums-deep/access'
POLICY={
'babycenteraustralia':'Explicit automation/commercial dataset prohibition in robots; no thread harvest.',
'babycenterindia':'Redirects to BabyCentre UK; target has explicit automation/commercial prohibition; no thread harvest.',
'babycenterus':'Explicit automation/commercial dataset prohibition in robots; no thread harvest.',
'babycentreuk':'Explicit automation/commercial dataset prohibition in robots; no thread harvest.',
'whattoexpect':'Explicit automation/commercial dataset prohibition in robots; no thread harvest.',
'mothering':'Robots explicitly blocks AI agents, including ChatGPT-User; no thread harvest.',
'fertilityfriends':'Robots explicitly blocks AI agents, including ChatGPT-User; no thread harvest.',
'mumsnet':'Robots GPTBot/CCBot/cohere-ai restrictions; no bulk corpus.',
'everybump':'Robots explicitly blocks ChatGPT-User and other AI Agents; no thread harvest.',
'hellobee':'Readable public boards; linked Terms grants solely personal/non-commercial use and forbids collecting personal data; no bulk commercial corpus.',
'heymammy':'Readable index; actual Babies, Weaning and Pregnancy boards require guest login/permission. Robots forbids training (use=reference), not a blanket inference that reference is banned. No private access.',
'justparents':'Public boards and posts readable. Robots permits forums. Linked Terms prohibits unapproved researcher/advertiser posting, not passive public reading. No accounts, posting or outreach. Whole selected boards harvested.',
'ohbaby':'Readable public archive; locked icons concern posting. Correct linked Terms prohibits downloading/storing content except personal/non-commercial copies. No bulk corpus.',
'babyandbump':'Actual canonical robots permits topics; landing redirects to .stile browser challenge. No challenge attempted; old Momtastic robot not transferred to this host.',
'thebump':'Robots permits ordinary topic paths; actual landing Cloudflare challenge403. No wall bypass.',
'bellybelly':'Robots lists canonical /forums/ paths. Both /forum/ and canonical /forums/ return403 Security Verification. No wall bypass.',
'healthboards':'Robots403 means unknown policy; actual content403 challenge. No wall bypass; not classified as site AI ban.',
'babywhisperer':'Robots403 means unknown policy; actual content403 challenge. No wall bypass.',
'netmums':'Robots403 means unknown policy; actual public coffeehouse403. No wall bypass; not classified as AI ban.',
'pregnancyforumco':'Robots and public landing403 challenge; policy unknown. No wall bypass.',
'magicmum':'Robots200; actual forum403 challenge. No wall bypass.',
'singaporemotherhood':'Robots403 policy unknown; actual forum403 challenge. No wall bypass.',
'rollercoaster':'Robots403 policy unknown; actual community route403. No wall bypass.',
'pregnancyinfo':'Robots allows with10s crawl delay; actual forums403 Forbidden. No wall bypass.',
'parentingforums':'Redirects to unrelated reprightsongs.com JS lander; not a working parenting forum.',
'clothdiapernation':'114-byte JavaScript /lander shell; not a working public forum.',
'pregnantcommunity':'Parked/domain-for-sale landing, no forum.',
'madeformums':'Former forum host redirects to editorial homepage; no forum exposed.',
'bubhub':'Forum path404; linked current homepage exposes no forum link. Archive not recovered.',
'bubhubforum':'Non-www canonical check also404; current homepage no forum link. Same site as www probe.',
'raisingthem':'Current editorial site, no public forum links exposed.',
'diaperswappers':'404 at former forum; domain now unrelated Indonesian fashion content.',
'justmommies':'Former forums410 Gone.',
'fertilethoughts':'Former forums404 empty response.',
'babycrowd':'Former forums404.',
'mumzone':'Former forum route404.',
'babyledweaning':'Former forum503 General Error; not a policy prohibition.',
'pregnancyforum':'Robots404, landing exceeds redirect limit; not a verified working forum.',
'pregnancyorg':'Broken redirect to malformed www.optum.combulletinboards host; no working forum.',
}

rows=[];group={}
for f in sorted(RAW.glob('*.json')):
    x=json.loads(f.read_text())
    if 'slug' not in x:x.update(slug='hellobee',kind='terms')
    x['observation']=POLICY.get(x['slug'],'Connection/TLS/DNS failure; no working public content obtained. Policy unknown; no verification disabling or identity workaround.')
    rows.append(x);group.setdefault(x['slug'],{})[x['kind']]=x
(ROOT/'sources/forums-deep-access.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
landing=[x for x in rows if x['kind']=='landing'];hosts={urllib.parse.urlsplit(x['requested_url']).netloc for x in landing};collapsed={x.removeprefix('www.') for x in hosts}
lines=['# Expanded primary parenting forum discovery','',f'Ordinary public probes on2026-10-24: **{len(landing)} candidate URL/host variants, {len(collapsed)} hosts after collapsing www**, {len(rows)} saved response/status records. This is a discovery/access count, not a count of usable communities or harvested threads.','',
'Raw responses and request/status/final-URL/header metadata are preserved in `_raw/forums-deep/access/`; the machine ledger is `sources/forums-deep-access.jsonl`. Failed requests retain exception metadata. No TLS checks disabled, identities changed, cookies obtained, accounts created, private boards entered, challenges solved, proxy used, or posting performed. Robots403 is unknown policy, never a blanket site ban. Canonical differences and redirects were checked as listed.','',
'JustParents is the one core forum carried into a full corpus in this wave. Public access and observed policies were sufficient for passive reference research; this is not a claim of a separately negotiated reuse license. All quoted material remains subject to the playbook’s short exact quotation limits. Other readable indexes were insufficient when actual boards required login or explicit policies excluded the intended collection.','',
'|Candidate|Robots|Landing|Observed outcome|','|---|---:|---:|---|']
for slug,g in sorted(group.items()):
    if 'landing' not in g:continue
    l=g['landing'];r=g.get('robots',{});label=urllib.parse.urlsplit(l['requested_url']).netloc
    lines.append(f"|[{label}]({l['requested_url']})|{r.get('status') or 'request failure'}|{l.get('status') or 'request failure'}|{POLICY.get(slug,'Connection/TLS/DNS failure; policy unknown. No workaround.')}|")
lines.extend(['','Linked policy detail: `hellobee-terms.bin`, `justparents-terms.bin`, `heymammy-terms.bin`, and `ohbaby-terms-correct.bin`; the guessed OHbaby terms route returned404 and was superseded by its actual footer link. Heymammy guest-permission walls are saved separately for Babies, Weaning and Pregnancy. BellyBelly’s actual canonical `/forums/` was checked separately from the supplied `/forum/`.','',
'Harvest inventory, completion counts, exclusions, reading and quote verification belong in `sources/forums-deep.md` and the frozen corpus manifests; they are not inferred from these access probes.',''])
(ROOT/'sources/forums-deep-discovery.md').write_text('\n'.join(lines))
print({'candidate_variants':len(landing),'www_collapsed_hosts':len(collapsed),'response_metadata':len(rows)})
