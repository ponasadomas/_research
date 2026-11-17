#!/usr/bin/env python3
"""Phase 0-1 scaffolding for the five niche folders (2026-10-25). Writes only files that don't exist yet."""
import os
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
COMMON_SPEAKERS = ["parent_unspecified", "partner", "relative_caregiver", "advisor", "professional", "reviewer", "skeptic", "gave_up_parent"]
COMMON_TYPES = ["trigger_moment", "pain", "fear", "tried_failed", "desire", "belief", "question", "objection", "advice_given", "success_story", "failure_story", "regret", "others_said", "purchase", "price_signal"]

N = {
 "sleep-baby": dict(
  title="Baby and toddler sleep, 0–36 months",
  prefix="sb",
  who="Mothers (and partners) of babies and toddlers whose nights are broken: frequent wakings, short naps, contact naps, early rising, the 4-month regression, bedtime battles. The buyer is the exhausted parent, not the child.",
  buy="Sleep courses ($49–249: Taking Cara Babies, Let's Sleep, Just Chill, Good Inside), quiz-to-plan programs (Betteroo: quiz → personalized plan → 28-day challenge, money-back), sleep consultants, apps (Huckleberry SweetSpot, Napper), hardware (Cradlewise, Nanit, HALO).",
  model="Quiz on age, current wakings, feeding, where the baby sleeps, the parent's values on crying → a personalized, age-specific plan → a day-by-day program.",
  speakers=["new_mother","experienced_mother","expecting_mother","recovered_parent"],
  stages=["newborn_0_8_weeks","baby_2_4_months","regression_4_months","baby_5_8_months","baby_9_12_months","toddler_12_24_months","toddler_24_36_months","looking_back"],
  themes="night_wakings contact_naps short_naps wake_windows early_waking bedtime_battle regression_4_month feeding_to_sleep dream_feed night_weaning cosleeping bedsharing room_sharing transition_to_cot sleep_training_values cry_it_out ferber gentle_method chair_method pick_up_put_down consistency_failure partner_split_nights partner_disagreement daycare_naps nap_transition drop_nap sleep_props pacifier swaddle_transition white_noise schedule_rigidity sleep_consultant course_purchase app_tracking information_overload conflicting_advice maternal_exhaustion resentment guilt comparison_other_babies safe_sleep_fear money_back price_value personalization",
  lines="Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.",
  other_side="The partner who disagrees on sleep training; the daycare carer whose naps 'just work'; the parents who refused sleep training and are content; the ones who paid for a course and quit.",
 ),
 "sleep-mother": dict(
  title="The mother's own sleep",
  prefix="sm",
  who="Pregnant and postpartum mothers whose own sleep is the problem: pregnancy insomnia, can't fall back asleep after a feed, lying awake listening for the baby, cumulative deprivation, unequal night duty with the partner, returning to work exhausted.",
  buy="Unknown. Candidates to test: CBT-I apps (Sleepio, Stellar Sleep), meditation apps, postpartum doulas and night nannies, sleep supplements, pregnancy pillows. No info-product seller to this need was found in the 2026-10-25 Ad Library sweep.",
  model="Quiz on the mother's situation (pregnancy week or baby's age, feeding method, who does nights, what keeps her awake) → a personalized plan for her own sleep and the household's night split.",
  speakers=["expecting_mother","new_mother","experienced_mother","recovered_parent"],
  stages=["pregnancy_first","pregnancy_second","pregnancy_third","newborn_0_8_weeks","baby_2_6_months","baby_6_12_months","toddler","return_to_work","looking_back"],
  themes="pregnancy_insomnia cant_sleep_when_baby_sleeps hypervigilance listening_for_baby racing_mind night_feeds_split partner_sleeps_through resentment shift_system pumping_at_night formula_for_sleep return_to_work_exhausted cumulative_deprivation naps_for_mum caffeine sleep_aids_question melatonin_question cbti apps_meditation night_nanny family_help no_village body_pain physical_discomfort pregnancy_pillow bathroom_trips anxiety_at_night maternal_guilt self_care_guilt identity_loss baby_in_room bedsharing_mum_sleep white_noise_for_mum early_waking_mum information_overload price_value personalization",
  lines="Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.",
  other_side="The partner who sleeps through or works nights; grandparents who offer help; mothers who say they slept fine; professionals (sleep clinicians, doulas).",
 ),
 "development": dict(
  title="Baby development and play, 0–24 months, age-selected",
  prefix="dv",
  who="Mothers of babies 0–24 months who want to know what to do with the baby at this exact age, whether the baby is on track, and how to fill awake time without screens or guilt.",
  buy="Age-selected PDF guides (Pirmi Žingsniai €17.95, HU clone 72 active ads), apps (Kinedu 208 active ads, BabySparks, Pathways free, Wonder Weeks), subscription play kits (Lovevery), baby classes.",
  model="Selector of the baby's age in months and weeks (Pirmi) or a short quiz → an age-specific activity and milestone guide for the next weeks.",
  speakers=["new_mother","experienced_mother","recovered_parent"],
  stages=["newborn_0_8_weeks","baby_2_4_months","baby_4_6_months","baby_6_9_months","baby_9_12_months","toddler_12_18_months","toddler_18_24_months","looking_back"],
  themes="what_to_do_all_day awake_time tummy_time tummy_time_hate floor_play rolling sitting crawling pulling_up walking first_words babbling fine_motor milestone_comparison milestone_anxiety corrected_age pediatrician_checkup cdc_milestones wonder_weeks leaps screen_time toys_too_many montessori play_ideas boredom_mum maternal_guilt not_enough_play container_time baby_classes app_tracking information_overload conflicting_advice reassurance_seeking social_comparison grandparent_comments early_intervention_question personalization price_value",
  lines="Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.",
  other_side="Grandparents and in-laws who compare; paediatricians and physios; parents who say 'babies just develop'; Montessori purists; buyers of apps who cancelled.",
 ),
 "toddler-behaviour": dict(
  title="Toddler behaviour and potty training, 1–4 years",
  prefix="tb",
  who="Mothers of 1–4 year olds facing tantrums, hitting and biting, not listening, picky eating, transitions, a new sibling, and potty training.",
  buy="Video courses (Big Little Feelings: Potty Training Made Simple leads 20 of 30 top ads; Winning the Toddler Stage), Good Inside membership, potty products with a method (UpAiry 838 active ads), potty consultants, books (Oh Crap!, Good Inside, How to Talk So Little Kids Will Listen).",
  model="Quiz on the child's age, the behaviour, the household and what was tried → a personalized plan (potty: readiness, method, day-by-day; behaviour: scripts for the specific situations).",
  speakers=["new_mother","experienced_mother","recovered_parent"],
  stages=["toddler_12_18_months","toddler_18_24_months","toddler_2_3_years","preschool_3_4_years","new_sibling","daycare_start","looking_back"],
  themes="tantrum public_meltdown hitting biting throwing not_listening defiance no_phase transitions bedtime_battle screen_time picky_eating new_sibling daycare_behaviour daycare_report potty_readiness potty_regression potty_refusal poop_withholding accidents night_dryness potty_method_3_day pullups gentle_parenting gentle_parenting_backlash time_out consequences scripts big_little_feelings good_inside partner_disagreement grandparent_undermining maternal_rage maternal_guilt shame_in_public comparison_other_toddlers information_overload course_purchase price_value personalization",
  lines="Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.",
  other_side="Daycare teachers; the partner who is stricter or softer; grandparents; parents who reject gentle parenting; BLF and Good Inside buyers who cancelled.",
 ),
 "pregnancy-birth": dict(
  title="Pregnancy, birth preparation and the first weeks",
  prefix="pb",
  who="Expecting mothers by trimester and by pregnancy number (first, second, third+), preparing body and mind for birth and the first weeks.",
  buy="Pirmi pregnancy guide (€29.95, selector: which pregnancy; the HU clone's active ads), hypnobirthing and birth courses (not yet searched by brand), prenatal fitness programs, apps (Flo, BabyCenter, What to Expect, Ovia), doulas, hospital classes.",
  model="Selector or quiz on the week, which pregnancy, how the body feels, the birth plan → a personalized trimester guide (body, exercise, birth preparation, what to buy, the first two weeks).",
  speakers=["expecting_mother","new_mother","experienced_mother","recovered_parent"],
  stages=["trying","first_trimester","second_trimester","third_trimester","birth","newborn_0_2_weeks","newborn_2_8_weeks","second_pregnancy","looking_back"],
  themes="first_pregnancy second_pregnancy pregnancy_with_toddler nausea fatigue back_pain pelvic_pain sleep_in_pregnancy exercise_in_pregnancy exercise_fear weight_gain gestational_diabetes_question diet_rules what_to_buy registry hospital_bag birth_plan birth_fear tokophobia epidural_decision induction c_section vbac hypnobirthing birth_course perineal_prep doula partner_role birth_trauma_story first_two_weeks postpartum_recovery visitors maternity_leave work_in_pregnancy information_overload app_tracking week_by_week comparison_other_pregnancies previous_birth personalization price_value",
  lines="Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.",
  other_side="Partners; midwives, doulas and OBs; second-time mothers looking back on the first; mothers who say preparation didn't matter.",
 ),
}

def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        print("exists, kept:", os.path.relpath(path, ROOT)); return
    open(path, "w", encoding="utf-8").write(text); print("wrote", os.path.relpath(path, ROOT))

for slug, n in N.items():
    d = os.path.join(ROOT, slug)
    for sub in ["_raw/owner", "_raw/competitors", "_raw/ads-running", "_raw/youtube", "_raw/books", "_raw/reviews", "_tools", "voice", "sources", "competitors", "ads-running", "books", "synthesis", "product", "scratchpad"]:
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    speakers = n["speakers"] + COMMON_SPEAKERS
    w(os.path.join(d, "README.md"), f"""# Mamivio — {n['title']}

**State on 2026-10-25: Phase 0–1 written (brief, vocabulary, rules). Shared Reddit harvest running (`../_shared/_raw/reddit-2026/`). Nothing filtered, read or quoted yet.** Plan for all five builds: [`../PLAN-2026-10-25.md`](../PLAN-2026-10-25.md).

Built with `templates/00 - Deep Research Playbook.md`. `../global/` is a frozen earlier database; cite its ids as `[id]` only where they are re-verified, never copy its quotes into `voice/`.

## Layout

`product/` the brief · `sources/` one note per source with a ledger · `_raw/` untouched source text (shared Reddit lives in `../_shared/_raw/`) · `voice/*.jsonl` verbatim quotes · `competitors/` teardowns · `ads-running/` Ad Library write-ups · `books/` · `synthesis/` findings, quote index, reader notes, counts · `_tools/` scripts and agent briefs · `scratchpad/<prefix>/` one folder per agent.

## Quote schema

Every record: `id` (prefix `{n['prefix']}NN-NNNN`, never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: {', '.join('`'+s+'`' for s in speakers)}. Use `parent_unspecified` unless the author identifies as a mother.

Stages: {', '.join('`'+s+'`' for s in n['stages'])}, `unknown`.

Types: {', '.join('`'+t+'`' for t in COMMON_TYPES)}. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `synthesis/reader-notes.md`): {', '.join('`'+t+'`' for t in n['themes'].split())}.

The other side of the door: {n['other_side']}

## Research principle

{n['lines']}

Counts are counts of quotes chosen, never of people.

## Resuming

Read this state line, `sources/*.md` ledgers and `synthesis/reader-notes.md`. Never rebuild a corpus once quotes cite it; never re-run an agent that appends to an existing voice file.
""")
    w(os.path.join(d, "product", "product-brief.md"), f"""# Product brief — {n['title']}

Written 2026-10-25 from the niche title, the owner's brief (`../../../brief.md`) and the 2026-10-25 Ad Library sweep (`../../main/ads-running/`). **There is no product yet; every line below is an assumption the research must test.**

- **Who suffers (assumption):** {n['who']}
- **What they already buy (from the Ad Library sweep and `../../global/competitors/`):** {n['buy']}
- **The candidate Mamivio product (assumption):** {n['model']} Price ladder already used by Mamivio: $17.95 / $29.95 / $49.95 for 1 / 3 / 6 months.
- **Things to be careful with:** {n['lines']}

## Questions the research must answer

1. Which moment makes them search and pay, in their own words?
2. What have they already bought or tried, and how did it land? Who quit, and why?
3. Does personalization by age or situation matter to them, or is generic advice enough?
4. What do they say a solution is worth? What do they call a rip-off?
5. Who else is in the decision (partner, grandparents, daycare)?

## Open questions for the owner

- Any Facebook groups, forums or customer data for this audience you can share?
- Launch language and country (owner picked English-speaking markets on 2026-10-24; which first)?
""")
    w(os.path.join(d, "sources", "owner-data.md"), """# Owner data

Intake 2026-10-25. The owner supplied no customer data for Mamivio on 2026-10-24 (`../../global/sources/owner-data.md`), and none since. `_raw/owner/` is empty by design. Pirmi Žingsniai's public material is competitor data, not owner data.
""")
print("done")
