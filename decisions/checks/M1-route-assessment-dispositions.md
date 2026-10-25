# The route assessment: what was done with each finding

This is the coordinator's record of the independent assessment of the founder's question of 25 October: continue, or rebaseline at G1 (`M1-route-assessment.md`).
- **The assessor** wrote none of the method, and saw neither the coordinator's view nor the amendments' reasoning.
- **Its cost:** 4.7 million tokens over 30 requests, counted by `method/count_tokens.py`. It reports using 31 of its 35 allowed tool calls.

Each finding was tested against the lines it cites (`METHOD.md` section 6). None was rejected, two are qualified, and the coordinator adds four.

## The findings

| Finding | Verdict | What the files show |
| --- | --- | --- |
| 1. The method contradicts its guard | Holds | "References first, then the market" (`METHOD.md`:87). The evidence step, which comes before options, takes "the first market's facts from the Stage 1 digest" (:173). First-market yardsticks: :12 and :255 |
| 2. Records run ahead of the method | Holds | `METHOD.md` has no "variation point", "coexist" or "test form" (searched). D-001 rests on the first plan's step 5 rule (`D-001`:31, :146, :229–234). The re-frame lapsed the letter rule and the joined letters (`plan-change.md`:57). D-006 uses 4f's construct, which is not adopted. The method says "No new rule or step is added without an amendment" (`METHOD.md`:20) |
| 3. D-001 claims more than the analysis it cites | Holds | S01-VP-01's "what follows" gives "the platform carries all the variants at once; a variation point behind one interface, bound per market, store or plan; a decision for the founder, on a recommendation" (`studies/subjects/S-01/analysis.tsv`). It doesn't give C at launch. C came from the pilot's recommendation, "C for Yemen now" (`entry.md`:123), and, without Yemen, from one agent's run (`M1-blind-decision-1.md`). Part five repeats the claim: "re-derived what the pilot had concluded" (`reports/M1-market-binding.md`:190). **Applied:** D-001's reason now says what the analysis gives, and where C came from. Part five is a dated report and is left as it was |
| 4. The separate check of each brief was lost | Holds | G1 kept it (`g1-answer.md`:65), and so did the re-frame (`plan-change.md`:30). `METHOD.md` mentions briefs at :146, :175, :221 and :298, and none of these is that check. It isn't among the founder decisions the method changed (:413–420), and no report names it (searched) |
| 5. G1's independent review was narrowed | Holds, as interpretation | G1: "one independent review of each result before it reaches me" (`g1-answer.md`:66). Level 1: "Quotes are checked by script. Nothing else." (`METHOD.md`:210). Level-1 decisions reach the founder in reports (:51) |
| 6. Founder decisions reversed without saying so | Holds, and is wider | **What the founder stopped at G1:** "labelling why platforms differ" and "checking each money question against Yemen's cases" (`g1-answer.md`:69–70). The founder also said section B's questions "don't take the test form" (:97). 4d and 4f bring these back, and say "the re-frame" stopped them (`M1-method-assessment.md`:167, :186).<br><br>**Wider:** part two calls dropping the variability analysis "two choices of mine" (`M1-plan-changes.md`:53). In fact the founder's G1 answer dropped it; only coarsening the sweep to areas was the coordinator's (`plan-change.md`:207).<br><br>**Qualified:** G1 stopped "going subject by subject in batches, as the plan does now" (:71). The method runs one subject at a time, not in batches. That is a partial return to subjects. The founder accepted it with the method, but it is not listed at `METHOD.md`:413–420 |
| 7. Two reports disagree | Holds | Part two: "Not proposed: bringing back the test form's cause labels" (`M1-plan-changes.md`:81). 4d brings back the cause step (`M1-method-assessment.md`:168–169) |
| 8. STATE under-applies amendment 4 | Holds | `STATE.md`:84 names sections 5, 6, 7 and 13. Amendment 4's own items also name sections 1, 3a, 4, 8, 10 and 12 (4c to 4f) |
| 9. The pilot's open items were not carried | Holds as stated: not in the method, the M1 reports or `STATE.md` | Finding 36, the "21 of 23" letter rows, and finding 29 (`method-report.md`:146–149). **Qualified by the check of part six (RC-12):** findings 36 and 29 were carried into the re-frame's drafting (`PLAN.md`:34, :616) and dropped on 24 October, and the re-frame lapsed the letter rows (`plan-change.md`:57) |
| 10. The rewrite risk can't trip | Holds, as interpretation | W-03's trigger is "a change to METHOD.md without an amendment" (`risks.tsv`:4). Amendments 2 and 3 came the day the method was adopted, and 4 the next day |

## The routes

- **Continue:** its risks hold. The first plan's kill rule (`2842819:PLAN.md`:130) applies once errors come "from the method again". The coordinator's own finding is that "The root cause is in the method" (`reports/M1-market-binding.md`:31).
- **Rebaseline at G1:**
  - "Every wholesale re-cut has lost safeguards" holds (`M1-method-assessment.md`:52–57).
  - So does "the last was itself called the re-baseline, made after the founder asked this same question" (`HISTORY.md`:44; `founder-messages/2026-10-24-method-accepted.md`:42).
  - The added constraint: a literal reset is excluded. History is never rewritten (`HISTORY.md`:48; `METHOD.md`:135), and documents cite commits by hash.
  - **Qualified:** "about half a billion tokens a subject … covers about four of the 15 open subjects" is the pilot's form, run per platform word. The form per decision, from statements already recorded, has never been measured. The assessor marks the figure as interpretation.
- **Rebaseline at the current state, by function:** its list of every practice in every version, its one text and its trial are adopted. Its base is not: after the founder's rule that no decision is valid merely because it was accepted before (`founder-decisions.tsv`:64), part six recommends the founder's route, from G1, done by the same full list (`reports/M1-route.md`, sections 3 and 5). Its list of founder decisions to carry into version 2 is replaced: each decision is assessed on its merits first.

## Added by the coordinator

- **The founder asked this on 24 October,** and set criteria (`founder-messages/2026-10-24-method-accepted.md`:42):
  - "a reliable engineering method";
  - "address its root cause through established practice rather than inventing another corrective layer";
  - "take our actual current position—not restart blindly";
  - "keeping future changes localized and recoverable".

  Amendments 2, 3 and 4 have each followed a concern since then.
- **Where S-01's cost went** (`STATE.md`:74–77; `decisions/subjects.tsv`, S-01):
  - 22.4 million for its records before amendment 2;
  - 35.4 million for amendment 2's pass;
  - 7.1 million for the two checks of the method assessment;
  - 5.5 million for the founder's market test and its check;
  - 4.7 million for this assessment.

  In all, 75.1 million, against a budget of 20 million and about 5 million the founder added for amendment 2's pass, which went past its stop line under the founder's go to continue while productive (`founder-decisions.tsv`:47). The check of part six added 2.4 million: 77.5 million.
- **Losses are not only of G1's practices.** The drafting rule of 19 October, "Yemen's evidence is read after the design sections are written" (`PLAN.md`:617), came after G1, and the method's evidence step contradicted it. So the list must cover every version, not G1's alone.
- **The G1 point's own gaps,** for the list: the register as its end; the first market used for scope (`2842819:PLAN.md`:28, :144, :22); its unit per platform word; the cause step's first run (`PLAN.md`:496); options from the five platforms only; and cost measured only at the end (`method-report.md`:182).
