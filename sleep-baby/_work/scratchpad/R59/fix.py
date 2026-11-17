p='synthesis/reader-notes-r59.md'
s=open(p).read()
reps=[
('  - Planning for the setback before training even starts: "I just want to prep for if we happen to encounter those rare “wide awake” nights" [sb59-0094] … see [sb59-0094] for the good night and [sb59-0367] for this question (15-week-old). A "quick reset" rule they invented themselves, with the fear it undoes the work [sb59-0394].',
 '  - Planning for the setback before training even starts (a 15-week-old): "I just want to prep for if we happen to encounter those rare “wide awake” nights" [sb59-0337].\n  - A "quick reset" rule a family made up themselves, and the fear that it undoes the work [sb59-0394].'),
(' A planned trip is a reason to delay [sb59-0270].',''),
("\nCorrection to the bullet above: the 15-week-old's setback-planning question is [sb59-0094]'s neighbour in my file only by number. The right id is the one quoting \"rare “wide awake” nights\" (see the id lookup at the end of this file).\n",''),
('  - Standing or crawling: [sb59-0197] [sb59-0058].','  - Standing or crawling: [sb59-0197] [sb59-0055]. Dropping the swaddle: [sb59-0058].'),
('nursing [sb59-0101] [sb59-0161]','nursing [sb59-0101] [sb59-0163]'),
('night wakes still there [sb59-0377].','night wakes still there [sb59-0388].'),
('A full crib for the camper [sb59-0103]','A full crib for the camper [sb59-0106]'),
('this young" [sb59-0068]','this young" [sb59-0077]'),
('travels a lot for work" [sb59-0410]','travels a lot for work" [sb59-0412]'),
('[sb59-0138] [sb59-0398] [sb59-0383] [sb59-0430]','[sb59-0138] [sb59-0384] [sb59-0430]'),
('bit off") [sb59-0367] [sb59-0434]','bit off") [sb59-0336] [sb59-0432]'),
('in awake time?" [sb59-0160].','in awake time?" [sb59-0161].'),
('behind a nap cap [sb59-0367].','behind a nap cap [sb59-0336].'),
('correctly?" [sb59-0054]','correctly?" [sb59-0054]'),
('correctly?" [sb59-0053]','correctly?" [sb59-0054]'),
('any earlier)" [sb59-0167]','any earlier)" [sb59-0168]'),
('when the parents cannot [sb59-0169]','when the parents cannot [sb59-0215]'),
('when she was tired." [sb59-0332]','when she was tired." [sb59-0426]'),
(' "2 year regression" [sb59-0457];',''),
]
for a,b in reps:
    n=s.count(a)
    if a==b: continue
    if n!=1: print('COUNT',n,a[:60]); continue
    s=s.replace(a,b)
open(p,'w').write(s)
