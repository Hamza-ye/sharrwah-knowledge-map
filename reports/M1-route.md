# The route: rebaseline the method, not the repository

**25 October 2026.** Part six of M1's assessment. It answers your question of 25 October: continue with the current method and its amendments, or go back to G1 and rebuild from there (framed in `founder-decisions.tsv`, 25 October).
- **Who assessed it:** an agent that wrote none of the method, and saw neither my view nor the amendments' reasoning. It judged the routes from the files alone (`decisions/checks/M1-route-assessment.md`; 4.7 million tokens).
- **How it was checked:** I tested each of its findings against the files it cites (`decisions/checks/M1-route-assessment-dispositions.md`). All of them hold, two with qualifications, and I add four.

## In short

- **Don't continue as is.** The files confirm ten problems:
  - the method contradicts its own guard;
  - two records rest on rules it hasn't adopted;
  - amendment 4 would reverse decisions of yours without saying so.

  Amendment 4 fixes two of the ten.
- **Don't reset the repository to G1 either.** That would discard the 53 rows of your decision record added since G1, and evidence corrections that later records rest on. The G1 plan also has gaps of its own. And every wholesale change of the method so far has lost safeguards. Going back and then forward again would be two more such changes.
- **Rebaseline the method:**
  - **Pause.**
  - **List every practice.** An agent that wrote none of the versions lists every practice in every version, each with the risk it controls. That covers the first plan, G1, the re-frame, the method and all four amendments. A practice stays unless someone with the authority to retire it did so on purpose, and said so.
  - **Write one text.** From that list comes `METHOD.md` version 2, with no amendments layered on it. You approve it once.
  - **Check, then try.** The six decision records are checked again under it, and it runs on one decision, measured, before anything scales.
- **This is your proposal in substance.** It brings back what G1 had, checks what G1 missed, and carries the lessons forward. The one difference: nothing after G1 is thrown away. Each piece is either carried or retired by name.
- **You asked this on 24 October** (`founder-messages/2026-10-24-method-accepted.md`:42). I answered with a new method rather than a return, and today I argued against a reset again. The evidence supports your direction: a clean baseline that restores what G1 had. It doesn't support going back to G1's text.
- **Decision 1 doesn't depend on the route.** The pilot recommended C, and the test made without the first market reaches the same line. Waiting costs nothing, because your guard already keeps A and B from going live.

## 1. Can the current method be reconciled as it stands?

Not by continuing. Each of these was confirmed in the files.

| | Problem | Where |
| --- | --- | --- |
| 1 | **The method contradicts its own guard.** It says "References first, then the market". Yet its evidence step, which comes before any option, takes the first market's facts | `METHOD.md`:87, :173; also :12, :255 |
| 2 | **Two records rest on rules the method hasn't adopted.** D-001 rests on the first plan's analysis of variants, which the method doesn't contain. D-006 rests on amendment 4f, before your approval. Yet the method says "No new rule or step is added without an amendment" | `D-001`:31, :229–234; `METHOD.md`:20 |
| 3 | **D-001 claimed more than the pilot's analysis gives.** The analysis gives one interface, bound per market, store or plan, and "a decision for the founder, on a recommendation". C at launch came from the pilot's recommendation for Yemen, and without Yemen from one agent's run. Corrected today in D-001 | `analysis.tsv`, S01-VP-01; `entry.md`:123 |
| 4 | **A safeguard you kept at G1 was lost on 24 October, and never listed:** "a separate check of each brief before it runs" | `g1-answer.md`:65; `METHOD.md` (searched) |
| 5 | **Your G1 rule was narrowed:** "one independent review of each result before it reaches me". Decisions that are cheap to undo now get only a script's check of their quotes, and reach you in reports | `g1-answer.md`:66; `METHOD.md`:210 |
| 6 | **Amendment 4 reverses your G1 decisions without saying so.** You stopped "labelling why platforms differ" and "checking each money question against Yemen's cases", and you said questions "don't take the test form". 4d and 4f bring these back, and say the re-frame stopped them. My part two calls the first "two choices of mine" | `g1-answer.md`:69–70, :97; `M1-method-assessment.md`:167, :186; `M1-plan-changes.md`:53 |
| 7 | **Two of my reports disagree** on whether the cause labels come back | `M1-plan-changes.md`:81; `M1-method-assessment.md`:168–169 |
| 8 | **`STATE.md`'s next step would enter amendment 4 in only 4 of the 10 sections it changes** | `STATE.md`:84 |
| 9 | **Three of the pilot's open items were never carried:** finding 36, finding 29, and the letter rule that "21 of 23" variation points no longer separate | `method-report.md`:146–149 |
| 10 | **The risk "the plan keeps being rewritten" can't see it happening.** Its trigger is a change made without an amendment, and there were four amendments in two days | `risks.tsv`:4 |

**Why another amendment won't close these** *(my reading)*:
- **The losses share one cause.** Changes were "checked for what they add, not for what they drop", and carried "by summary, not by trace" (`M1-plan-trace.md`:59, :28).
- **My lists of losses have been incomplete each time.** Each amendment is my own list of what was lost, and none was complete. Item 4 was found today, by an agent that wrote none of the method.
- **So a fifth amendment would repeat the cause.**

**What the churn cost.** S-01 used 75.1 million agent tokens against its budget of 20 million:

| Work | Agent tokens |
| --- | --- |
| The subject's own records, before amendment 2 | 22.4 million |
| Amendment 2's pass | 35.4 million |
| Two checks of the method assessment | 7.1 million |
| Your market test and its check | 5.5 million |
| This assessment | 4.7 million |
| **Total** | **75.1 million** |

The figures are from `STATE.md`:74–77, plus this report. *My reading:* about two thirds of it went to changing the method and checking the changes, not to the decision.

## 2. Was G1 the biggest mistake?

**In part.** This section is my reading of the facts it cites.
- **What G1 stopped.** At G1 you stopped three things: the cause labels, the market marks and the subject batches (`g1-answer.md`:68–71). You also said questions take no test form (:97).
  - The re-frame then cost 1.32 billion agent tokens (`studies/proposals/costs.tsv`).
  - Its drafts are now candidates, not deliverables (`METHOD.md`, section 13).
- **The cheaper path would have kept the safeguards.** The pilot's own report proposed keeping them at lower cost (`method-report.md`:185–196):
  - scope each subject to its decisions;
  - reuse what is recorded;
  - keep agent runs short;
  - set a budget per subject;
  - match depth to risk;
  - take standing decisions early.

  Amendment 4 now "restores the safeguards that were dropped, in the form they already had" (`M1-method-assessment.md`:138). That is the cheaper path, taken a week late.
- **But G1 wasn't the only point of loss.** Four practices survived G1 and were lost on 24 October, when the method replaced the plan:
  - the absence audit (`M1-plan-changes.md`:24, :28);
  - the separate check of each brief (item 4);
  - the concern map as the index of subjects (`M1-plan-changes.md`:28);
  - the kill rule (`PLAN.md`:155; not in `METHOD.md`, searched).

  So going back to G1 doesn't remove the cause. Changing how the method itself is changed does.
- **The money question, then and now.** The pilot recommended C (`entry.md`:123). D-001 reaches C for every market at launch, and so does the test made without the first market. You could have answered it minimally at G1, and you still can.
- **What the re-frame left that holds:**
  - the 34 areas you kept at G2;
  - 2,600 statements recorded in the platforms' own words;
  - Stage 1's corrections;
  - the evidence gathered for the company decisions.

## 3. The three routes

| | Continue | Reset to G1 and rebuild forward | Rebaseline the method (recommended) |
| --- | --- | --- | --- |
| **What it does** | Adopt amendment 4, fold it in, start M2 | Take G1's plan and the pilot's proposals as the method, and take up again what came after | List every practice of every version, with the risk it controls; write one text from the list; you approve it once |
| **What it keeps** | All current work | G1's safeguards, by default | Both: every practice stays unless retired on purpose, by name |
| **What it loses or puts at risk** | Items 3 to 10 remain, and the next change repeats the cause | Your decisions since G1, and the method's newer rules, must each be carried again. History can't be rewritten (`HISTORY.md`:48), so this means re-taking work, not deleting it | Only what the list retires, each by name, with its risk |
| **Your decisions it reverses** | Some, silently (item 6) | The G1 re-frame and your acceptance of the method on 24 October | Only those you approve, each with its own answer line |
| **What agents read** | The method, three amendments in it, a fourth proposed, and the earlier documents beside them | An older text, with the newer rules returning as new layers | One text. Each brief is drawn from it and checked before it runs, and superseded documents leave the reading path |
| **Cost to reach one baseline** | Lowest | Highest | In between: about 25 to 45 million agent tokens over one to three days *(an estimate)* |
| **Shown wrong if** | The list finds nothing beyond amendment 4 and item 4 | The current method's core, not how it was changed, causes the losses | Version 2 needs an amendment within its first subject: then a deeper re-frame is due |

## 4. The recommended route, step by step

1. **Pause.** M2 doesn't start, nothing is accepted, and no new amendment is made. Amendment 4 is withdrawn as an amendment, and its items go into the list. Decision 1 waits, since your guard already covers its one-way part.
2. **The list, with its brief checked first.**
   - **Its brief is checked first,** by a separate agent, before it runs. That is your G1 rule, restored at once.
   - **Who writes it:** an agent that wrote none of the versions, in short runs, one version at a time.
   - **What it covers:**
     - the first plan and the pilot: its rulings, proposals, open items and review;
     - your G1 answer, with its Keep and Stop lists;
     - the re-frame and the rules of 19 October;
     - the method, its amendments 1 to 4, and the plan of 24 October.
   - **For each practice it records:**
     - the risk the practice controls;
     - where it stands now;
     - who retired it and why, if anyone did.

   A practice stays unless someone with the authority retired it on purpose. Your decisions change only by you.
3. **Version 2, one text.** I write it from the list.
   - Every rule cites its row in the list, and nothing goes in that isn't on it.
   - It has no amendments section, only a dated record of changes.
   - It resolves items 1 to 10, and rules on the pilot's open items.
   - It puts each reversal of an earlier decision of yours to you, with its evidence and its own answer line.
4. **An independent check** of version 2 against the list: every row kept appears at its step, and no rule lacks a row.
5. **You approve it once.**
   - `HISTORY.md` names it as the baseline.
   - Superseded documents get a status line and are taken out of the reading path in `CLAUDE.md` and `STATE.md`.
   - Nothing is deleted or rewritten.
6. **The six decision records are checked again** under version 2, each at its level. Then Decision 1 comes to you once.
7. **Version 2 runs on M2's first decision,** on a measured budget, before anything scales. The first plan's kill rule comes back: if errors come from the method again, nothing scales until you and I re-examine the frame (`2842819:PLAN.md`:130).

**Budget** *(an estimate)*:

| Step | Agent tokens |
| --- | --- |
| The brief's check and the list | 12 to 22 million |
| The check of version 2 | about 5 million |
| The records' re-checks | 10 to 15 million |
| **In all** | **about 25 to 45 million** |

Work stops at the budget plus a quarter, your rule of 24 October. My own work comes on top.

## 5. What the G1 point missed

Version 2 brings back G1's safeguards, but not its gaps. Each gap below is in the files.
- **It ended at a register,** with the design left to another plan (`2842819:PLAN.md`:22). Your decisions of 24 October make the architecture description the outcome.
- **The first market came in early, to set the scope:**
  - Stage 1 ran before the subjects "because scoping needs it" (:28);
  - the subject list took "every concern a Yemen axis touches" (:144);
  - the plan ended in "a thin slice for Yemen" (:22).

  Your framing of 25 October binds a market once, after the references.
- **Its unit of work was every word the platforms use:** 23 variation points, at a cost that "doesn't scale" (`method-report.md`:182). Version 2 works per decision, from what is already recorded: the pilot's proposals 1 and 2.
- **The cause step's first run put 12 of 14 items to you** (`PLAN.md`:496), before its rulings corrected it.
- **Options came only from the five platforms.** Your note of 24 October adds established designs and engineering writing, each weighed by its kind of source.
- **A rule without a check didn't hold.** The absence rule was written on 12 October, yet the pilot still recorded held Salla articles as missing. You found them on 13 October, and the audit was added then (`PLAN.md`:487). Version 2 gives each rule a check.
- **Cost was measured only at the end** (`method-report.md`:182).
- **Plain words for you** came later, with G1's A1.

## 6. Why this is established practice

- **One baseline.** A baseline is "A specification or product that has been formally reviewed and agreed upon, that thereafter serves as the basis for further development, and that can be changed only through formal change control procedures". Source: ISO/IEC/IEEE 12207:2008, as SEBoK's glossary gives it, read 25 October 2026. `METHOD.md`:40 cites IEEE 828 for baselines. A method with amendments layered on it is not one agreed text.
- **Management of change.** A change is assessed for the risks its removed parts controlled, and each risk is reassigned or accepted on purpose. Part two cites OSHA, 29 CFR 1910.119(l), for this. The list does it for every change at once.
- **What agents read.** Anthropic's guidance, "Effective context engineering for AI agents" (29 September 2025), says:
  - "good context engineering means finding the smallest possible set of high-signal tokens";
  - "as the number of tokens in the context window increases", "the model's ability to accurately recall information from that context decreases".

  This happened here. The coordinating session lost items of the plan of 24 October, because "the method's resume path doesn't read the plan's copy" (`M1-plan-trace.md`:28).
- **Try before scaling:** Boehm 1988, as the first plan cites it, and its kill rule.

## What I need from you

- **The route:** rebaseline the method, as in section 4 / continue, with amendment 4 / reset to G1 and rebuild forward / other: …
- **The pause until version 2 is approved:** yes / no. Decision 1 and amendment 4 would come back inside version 2.
