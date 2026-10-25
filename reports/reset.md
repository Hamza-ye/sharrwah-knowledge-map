# The reset

**What this file is:** a report to the founder at a planned pause (`PLAN.md`, section 9). It was written on 25 October 2026.

## In short

- **The work is back on the plan you agreed on 12 October,** as it stood at G1, with the pilot's own changes ([`PLAN.md`](../PLAN.md)).
- **Everything done between G1 and today is history.** It is outside the working files, so no search of them finds it. It can still be read at [commit `4923e1c`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf).
- **This page says what I carried forward, and why.** It needs no answer. If any line looks wrong to you, say so, and I'll take it out or explain it.
- **Waiting on you:** [Decision 1](../studies/subjects/S-01/decision-1.md), and your word to go on.

## What governs now

[`CLAUDE.md`](../CLAUDE.md), which every agent reads first, lists these working files and what each is:
- [`PLAN.md`](../PLAN.md): the plan. It is the only authority on how the work is done.
- [`STATE.md`](../STATE.md): where the work is, and the next step.
- [`founder-decisions.tsv`](../founder-decisions.tsv): your 13 decisions in force. It is the only authority on what Sharrwah does.
- The evidence, plus the inputs the plan names:
  - the concern map;
  - the Yemen study, with [its corrections](../studies/yemen-cases/corrections.md);
  - the pilot.

## What I carried forward from after G1, and why

**Facts.** A fact checked against its source holds, whichever plan found it.
- **Ten corrections and cautions to the Yemen study's records** ([`corrections.md`](../studies/yemen-cases/corrections.md)). For example, Stripe is not supported for a business in Yemen. That does not mean payments to or from Yemen are barred.
- **The facts on Decision 1's page** ([`decision-1.md`](../studies/subjects/S-01/decision-1.md)), each linked to its source:
  - the conditions both references put on their own payment services;
  - sellers' own provider accounts, and payment outside any provider, in both;
  - the three edges of C;
  - the test made without Yemen.
- **The scripts the plan uses.** Six changed after G1. Two were added: the token count, and the recorded store runs as a corpus for the search. Four were improved: the search for claims of absence, and how a page is found held, matched and given its kind. I re-ran the checkers with them on the G1 inputs:
  - the concern map and the Yemen study: the same results as at G1;
  - the pilot: two findings G1's scripts missed. Three Salla gaps sent to you point to a page we already hold, which is read before anything goes to you. And five statements change their kind of source. Both are ruled before the next subject ([Stage 4](../PLAN.md#stage-4-the-subjects-one-at-a-time-riskiest-first)).

**My engineering choices.** Each fixes a failure we actually hit. They are written into the plan, and you can veto any:
1. **Every claim is marked as a fact, a reading or an assumption,** because claims had gone beyond their sources ([section 6](../PLAN.md#evidence)).
2. **Reviews try to refute, and I check each finding before I apply it,** because checks had agreed instead of testing ([section 3](../PLAN.md#3-who-does-what)).
3. **A review also looks for what an entry never cites,** because held evidence had been missed ([section 3](../PLAN.md#3-who-does-what)).
4. **Cost is counted once per request, and measured early in each run,** because costs had been double-counted and measured too late ([Stage 4](../PLAN.md#stage-4-the-subjects-one-at-a-time-riskiest-first)).
5. **Where the references aren't enough, options come from established designs, each weighed by its kind of source.** This is your "buying architectural intelligence" ([section 6](../PLAN.md#the-test-form-per-subject)).
6. **Changes to the plan are made in place, and each lists what it removes or weakens,** because safeguards had been dropped without notice ([section 9](../PLAN.md#9-keeping-it-coherent-across-sessions)).
7. **History stays outside the working files, and is used only by a deliberate link,** because old work had kept returning and steering the work ([section 9](../PLAN.md#9-keeping-it-coherent-across-sessions); [`method/check_surface.py`](../method/check_surface.py)).

**Corrections to the G1 plan's own gaps:**
- The design is for many markets, with an architecture description before any production code. This replaces "a thin slice for Yemen".
- Yemen's study no longer puts concerns on the subject list. Yemen enters after each subject's analysis.
- Subjects run one at a time, each with a budget and a short report, instead of in batches.

**Your decisions in force** ([`founder-decisions.tsv`](../founder-decisions.tsv)). I assessed each on its merits, and none rests on the work that is now history:
- **The plan's go** (G0): the plan is again the one in force.
- **No standing business model:** it comes from the evidence, which is how each subject decides.
- **Plain words** (G1): about how I write to you, whatever the plan.
- **The guard on sellers' money** (G1): it follows the plan's rule that holding sellers' money is your company and legal question ([section 3](../PLAN.md#3-who-does-what)). Decision 1's page stands on it.
- **Credentials in evidence:** read and cited like any other evidence.
- **Q3's rows, reconciled at the end** (G0): the reset doesn't touch them.
- **Agents' effort levels, delegated to me:** still how agents are run.
- **Reports at each milestone and pause; spikes allowed, with no production code before requirements, an architecture description and engineering documentation; no merchant interviews** (24 October): each is about how you follow the work, about code or about merchants, and holds without the method of that day.
- **Today's three:** the reset itself, engineering owning the method, and every decision assessed on its merits.

## What left the working files

All of it is readable at [commit `4923e1c`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf). Nothing was rewritten.
- **The re-frame's work:** its questions, areas, records, drafts and checks.
- **The method of 24 October,** with its amendments.
- **The decision records,** and their checks.
- **The M0 and M1 reports.**
- **The glossary, the risk register and the Knowledge Map register.** The register is read once at the end, through a link.
- **The studies from before the plan:** the obligation model, the Yemen setup options and the Shopify payments study.
- **Your message files.**
- **19 scripts.**
- **59 decision rows** that had lapsed, or were questions. Among them:
  - your decisions of 10 October, F-00 to F-06 and O-01, restored on 24 October. What they raise is decided when a subject reaches it;
  - G1's deferral of Decisions 1 to 14 until the re-frame had framed them. So Decision 1 comes back to you now.

## The tests

- **The search test** ([`method/check_surface.py`](../method/check_surface.py)) passes. The history's terms appear in the working files only in 20 named places, each with its reason. Most are the old briefs' own lists of what their agents must not read.
- **The cold-start test.** An agent with none of our conversation is given only "resume the work".
  - **First run:** it named the working files and what each is, found the right next step, and opened nothing in history. It also reported 19 places where a new session could misread the files. Among them: which file wins when the plan and your decisions differ, and what follows from Decision 1 if your answer isn't C. I checked each against the files, and fixed the ones that held.
  - **Second run,** on the fixed files: not yet run at this commit.

## What I need from you

- **Decision 1:** [its page](../studies/subjects/S-01/decision-1.md). The answer line is at its end, and the page says what follows from each answer.
- **Your word to go on.** Then I start with the pilot's open items and the subject list, which don't wait on Decision 1 ([`STATE.md`](../STATE.md)).
