import json
ex = {
"pregnant-1vj0k7g": "excluded: severe mental-health post in pregnancy, medication question",
"beyondthebump-1vj0w67": "excluded: postnatal mental-health post centred on diagnosis and medication",
"beyondthebump-1vj1xeu": "excluded: acute birth emergency and newborn medication-withdrawal concerns",
"beyondthebump-1vj5bvm": "excluded: crisis wording in post",
"NewParents-1vj5t4l": "excluded: postnatal mental-health post centred on diagnosis",
"pregnant-1vjc1lr": "excluded: serious screening findings and fear of loss",
"pregnant-1vjehxe": "excluded: centred on fear of loss after a previous loss",
"BabyBumps-1vjet55": "excluded: severe mental-health post (medical leave for treatment); crossposted as pregnant-1vjetja",
"pregnant-1vjetja": "excluded: crosspost of BabyBumps-1vjet55, same author and text",
"pregnant-1vk3inr": "excluded: partner conflict with yelling (partner aggression)",
"pregnant-1vkfm1c": "excluded: serious screening finding",
"FirstTimeMom-1vkk183": "excluded: money solicitation (registry link asking strangers to buy)",
"pregnant-1vkk5bd": "excluded: relationship-safety concern and partner substance use",
"Mommit-1vko4ne": "excluded: severe postnatal mental-health post, medication-centred",
"Mommit-1vkonq4": "excluded: severe perinatal mental-health post",
"pregnant-1vkrqg7": "excluded: weighing whether to continue the pregnancy",
"NewParents-1vksfd0": "excluded: postnatal mental-health post",
"pregnant-1vkuoue": "excluded: serious screening finding (growth restriction) leading to induction",
"pregnant-1vl044t": "excluded: acute medical emergency in pregnancy",
"pregnant-1vl3til": "excluded: relationship-safety and custody concern",
"beyondthebumpUK-1vldqgg": "excluded: postnatal mental-health post centred on screening score",
"pregnant-1vllbg1": "excluded: substance use in pregnancy",
}
nq = {
"Mommit-1vj5tfv": "read, no quote: 8 weeks postpartum appearance question, off-stage",
"pregnant-1vjcwql": "read, no quote: symptom question, nothing new",
"pregnant-1vjvny9": "read, no quote: flagged as likely AI-written/polished (bold paragraphs, essay cadence)",
"beyondthebump-1vk0cc6": "read, no quote: car-seat base reuse question",
"BabyBumps-1vkd4wx": "read, no quote: crosspost of pregnant-1vkd3sv (quoted once there)",
"beyondthebump-1vkp2v9": "read, no quote: medication-centred postnatal insomnia, 8 weeks",
"pregnant-1vkq4ag": "read, no quote: generic early-pregnancy tiredness",
"pregnant-1vl0k5e": "read, no quote: body-change humour, nothing pullable",
"beyondthebumpUK-1vld76k": "read, no quote: 9-week physio appointment question, off-stage",
"pregnant-1vlmlws": "read, no quote: flagged as a likely service-idea research probe ('would you have considered paying for it?')",
"BabyBumps-1vlp7jg": "read, no quote: radiation-exposure fear, nothing pullable; crossposted as pregnant-1vlpnkg",
"pregnant-1vlpnkg": "read, no quote: crosspost of BabyBumps-1vlp7jg",
}
R = {}
for l in open("scratchpad/PR41/restricted.tsv"):
    rid, unit, why = l.rstrip("\n").split("\t"); R.setdefault(unit, []).append(rid)
pu = json.load(open("scratchpad/PR41/perunit.json"))
rows = []; cq = cn = ce = 0
for l in open("scratchpad/PR41/units.txt"):
    ch, path = l.split()
    u = path.split("/")[-1][:-4]
    n = pu.get(u, 0)
    if u in ex: st = ex[u]; ce += 1
    elif u in nq: st = nq[u]; cn += 1
    elif n:
        st = "quoted"; cq += 1
        if u in R: st += " (all restricted)" if len(R[u]) == n else " (%d restricted)" % len(R[u])
    else: st = "??"
    assert not (n and (u in ex or u in nq)), u
    rows.append("| %s | `%s` | %s | %d |" % (ch[-3:], u, st, n))
print(cq, cn, ce, sum(pu.values()))
open("scratchpad/PR41/ledger_rows.md", "w").write("\n".join(rows) + "\n")
