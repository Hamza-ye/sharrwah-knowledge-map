# The check of part six: what was done with each finding

This is the coordinator's record of the independent check of `reports/M1-route.md` (`M1-route-check.tsv`).
- **The check:** 46 rows: 17 hold, 22 fix and 7 open. Its cost was 2.4 million tokens over 17 requests, counted by `method/count_tokens.py`.
- **How it was handled:** each fix was tested against the evidence it cites before it was applied (`METHOD.md` section 6). None was rejected.
- **The founder's rule.** In the same hour, the founder set the rule that no decision is valid merely because it was accepted before (`founder-decisions.tsv`:64). Together with RC-17 and RC-33, it changed the report's recommendation. Part six now recommends the founder's own route, from G1, done by a full list. It no longer sets that route against a rebaseline at the current state, as the first draft did.

## Applied

| Finding | What was done |
| --- | --- |
| RC-01 | Items 5 and 10 are marked as the coordinator's reading in the header, in short, and in section 1 |
| RC-02 | Amendment 4 is said to fix items 1 and 2, as a reading of 4d and 4f. The table says items 4 to 10 remain, since item 3 was corrected in D-001 |
| RC-05 | Item 2: D-006 follows the founder's market test (`founder-decisions.tsv`:58–59; `D-006`:23). Only 4f writes up its form as a market row |
| RC-08 | Item 5: that cheap-to-undo decisions reach the founder in reports was the founder's own decision of 24 October (`founder-decisions.tsv`:35). Only the drop in review went unlisted |
| RC-12 | Item 9: findings 36 and 29 were carried into the re-frame's drafting (`PLAN.md`:34, :616) and dropped on 24 October. The letter rows were lapsed by the re-frame, though D-001 still uses them |
| RC-13 | Item 10: three amendments were made on 24 October, and a fourth was proposed on 25 October |
| RC-15, RC-16 | The cost now names the founder's added 5 million and the go to continue past the stop line. It cites both sources and notes how each groups the 2.2 million check. This check's 2.4 million is added: 77.5 million in all |
| RC-17 | "Discard the 53 rows" is gone. A literal reset is excluded by `HISTORY.md`:48, and the founder's route is answered as framed (`founder-decisions.tsv`:63): G1 as the base, carrying forward what works |
| RC-19 | About 2,600 statements, each quoted from its source (`METHOD.md`:394) |
| RC-21 | "The pilot's entry recommended C for Yemen now" (`entry.md`:123), in both places |
| RC-28 | "Your direction of 25 October, as framed at `founder-decisions.tsv`:59 and :61" |
| RC-29 | The founder's note (`method-accepted.md`:30; `founder-decisions.tsv`:34) and the approved plan's weighing by source type (`METHOD.md`:162–163) are now separated |
| RC-31 | Marked as reading. "Waiting costs nothing I can find", with the guard cited (`founder-decisions.tsv`:9) |
| RC-33 | Marked as reading. The route is recast: with the founder's rule, the two rebaselines differ only in which side must show it holds, and part six takes G1 as the base, with its reasons |
| RC-34 | The cause step's first run "read 14 of 23 variation points as vendor choice, 12 of them as founder decisions", before its rulings corrected it |
| RC-35 | Cites `method-report.md`:182 and :185 |
| RC-37 | The budget is re-estimated, with the assessment of the founder's decisions added: about 31 to 50 million (an estimate). Steps 3 and 7 are outside it, and the table's costs are marked as estimates |
| RC-38 | Step 3 says how later changes are controlled: each lists what it drops or weakens, and the founder sees that list with the change (`founder-decisions.tsv`:55). W-03 and the amendment rule in `CLAUDE.md` are rewritten to match |
| RC-42 | Marked as reading: a text whose changes sit in amendments beside the parts they change, and contradict them in one place, is hard to read as one agreed text |
| RC-43 | The OSHA rule is now quoted from the regulation itself (see RC-44). Applying it to a design method is marked as the coordinator's reading |
| RC-46 | Marked as reading: "a related failure happened here", lost at restart (`M1-plan-trace.md`:28, :58) |

## Open rows answered

- **RC-23:** the concern map is now "the record the work draws from" (`g1-answer.md`:100; `M1-plan-changes.md`:28). The report no longer calls it the index of subjects.
- **RC-36:** "The test form took its variants from the five platforms (`2842819:PLAN.md`:188), and *on my reading* names no outside designs."
- **RC-39:** step 1 says what happens to the pull requests:
  - PR #7 stays open until the founder answers;
  - on this route, PR #7 merges as M1's pause;
  - version 2 comes in its own pull request, with its own report and a row in `HISTORY.md`.

  Step 5 says what happens to the documents:
  - superseded method documents carry a status line, as `PLAN.md` already does;
  - dated reports stay as they were, and `STATE.md` marks them (`HISTORY.md`:50).
- **RC-40:** step 2 explains why the brief check needs no amendment:
  - G1's Keep list was never retired, and isn't among the decisions the method changed (`METHOD.md`:413–420);
  - so the check applies now;
  - its merit is the first plan's risk 2 (`2842819:PLAN.md`:254).
- **RC-41:** the coordinator read SEBoK's glossary entry on 25 October 2026 (page last edited 25 March 2026). The quoted definition matches, attributed there to ISO/IEC/IEEE 12207:2008.
- **RC-44:** the coordinator read 29 CFR 1910.119(l) at Cornell's Legal Information Institute on 25 October 2026. "to manage changes", "process chemicals, technology, equipment, and procedures", "The technical basis for the proposed change" and "Impact of change on safety and health" match.
- **RC-45:** the coordinator read Anthropic's "Effective context engineering for AI agents" on 25 October 2026 (published 29 September 2025). Both quotes match.
