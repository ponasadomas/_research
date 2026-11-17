from build import build
k={
'1ulblvt':('keep_core','screen time worry, 22-month-old after heavy-screen period'),
'1ulsy66':('keep_purchase','first-birthday gift hunt for second child, toys vs milestones'),
'1umffne':('keep_purchase','large birthday and Christmas toy haul list for nearly 2-year-old'),
'1upvakm':('keep_purchase','weighs buying push walker for 14-month-old taking single steps'),
'1usd6ah':('keep_core','delay worry, 14-month-old communication, comparing with cousin'),
'1utml2h':('keep_core','16-month-old twins, Montessori open-ended play and independence'),
'1utsjav':('keep_otherside','delay worry, speech therapist and SLP sister disagree about near-2-year-old words'),
'1uz5zsg':('keep_core','delay worry, 2-year-old, daycare teacher suggests developmental evaluation'),
'1uzuo2b':('keep_purchase','choosing play kitchen for 15-month-old, Lovevery versus others'),
'1v2cxlw':('keep_otherside','delay worry, relative sees 20-month-old cousin not progressing, mother ignores'),
'1v3hna0':('keep_core','delay worry, 20-month-old walker with few words, asks if speech lag resolved'),
'1v3z3vy':('keep_core','delay worry, 18-month-old not talking, early intervention in progress'),
'1v4csza':('keep_core','13-month-old plays alone most of day, asks if too much'),
'1v96dfl':('keep_core','17-month-old cannot sit at story time, fears screens harmed attention'),
'1vbsmgv':('keep_core','delay worry, 16-month-old not walking or talking, comparing with peers'),
'1ve1way':('keep_core','delay worry, 15-month-old not pointing, late walker'),
'1upg0fg':('drop','duplicate repost of 1upg1v6'),
'1v7r29w':('drop','duplicate repost of 1v7r1wi'),
'1v3f4se':('drop','near-duplicate repost of 1v3e6ht naming a condition'),
'1uyt5g6':('drop','duplicate repost of 1uyt69l'),
'1uwrcmz':('drop','duplicate repost of 1uwrban'),
'1ve39eb':('drop','duplicate repost of 1vegd8f'),
'1usup5w':('drop','safety: child with diagnosed condition, 2.5 years'),
'1v75lnz':('drop','safety: screening and evaluation for a condition'),
}
d={
'1ueuknu':'sleep-only, 22-month-old bedtime','1uf7acl':'sleep after new sibling, 2.5 years','1ufn8y4':'sleep-only, 14-month-old split nights','1ufqajk':'soccer class for 28-month-old',
'1ugp71i':'potty training, near 3 years','1uh7odl':'preparing 22-month-old for sibling, bed move','1uhy6a7':'sleep-only, almost 3-year-old','1uif24e':'clingy 2.5-year-old behaviour',
'1uj0q4c':'3-year-old outdoors vs indoors','1ujqgeh':'co-sleeping regret','1ujrxus':'diaper-change resistance, behaviour','1uk5gu5':'3.5-year-old confidence and social worry',
'1unowfb':'sleep and bedtime protest, 2 years','1uobsg8':'working mother routine, 27-month-old','1up2eoj':'daily routine logistics, toddler fights, no development focus',
'1urnuce':'20-month-old whining, behaviour','1ursqa5':'photo session for 2-year-old','1usctet':'sleep-only, 25-month-old','1ut0shr':'14.5-month-old whining and bath crying, behaviour',
'1utd4gz':'3.5-year-old spoiled question','1uup9t2':'sleep-only, 18-month-old','1uw44bz':'potty training, 3 years 9 months','1uwrolo':'19-month-old tantrums everywhere, behaviour',
'1uxr5xp':None,'1uydb0k':'toddler bed transition, sleep','1uyr7xg':'home daycare visit smell','1uyvfhs':'sleep and husband, near 3-year-old','1uz254q':'3-year-old high-needs and baby, older child',
'1v0cofp':'pacifier weaning for school','1v0w5rl':'potty training, 3-year-old','1v2kus0':'burnout with near-2-year-old behaviour','1v4j049':'daycare transition and naps','1v4y43j':'sensory-seeking 18-month-old with OT, parent burnout, condition focus',
'1v7lxg3':'thumb sucking','1v8xdqs':'21-month-old behaviour after camp','1v9jspg':'balance bike for 2.8-year-old','1vawqiw':'potty training','1vazhiu':'17-month-old morning meltdown, teething',
'1vbool2':'nap logistics, 3-year-old and 10-month-old','1vc4utz':'parent burnout with 2.5-year-old and baby','1vcdaya':'sleep-only, 2-year-old','1vctr98':'potty training','1vdfv5d':'terrible twos behaviour',
'1vdhfby':'flying with nearly 2-year-old, travel tips',
}
k['1uxr5xp']=('keep_core','20-month-old rough on toys, keep nice toys or not, sibling contrast')
ids=[l.split(' | ')[0] for l in open('A-toddlers-001.txt')]
build('A-toddlers-001.txt','m8.tsv',{i:(k[i] if i in k else ('drop',d[i])) for i in ids})
