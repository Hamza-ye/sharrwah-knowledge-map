# Brief: S-02, the independent review (step 5)

This is `PLAN.md` Stage 4, subject S-02, step 5. You review what other agents and the coordinator produced for the subject's end. You made none of it. You change nothing; you report. Try to break it: the pilot's first review found that 16 of 71 checked claims were wrong.

**Read only:**
- this brief;
- `PLAN.md`, sections 1 and 6;
- `founder-decisions.tsv`;
- in `studies/subjects/S-02/`: `register.tsv`, `decisions.md`, `yemen-row.tsv`, `scenario-walk.tsv`, phase C's files (`c/RD1/`, `c/RD2/`, `c/RD3/`), `variation-points.tsv`, `variants.tsv`, and statements by id (`python3 -I method/subject_slice.py studies/subjects/S-02 --print RD --ids ...`);
- of `studies/subjects/S-02/briefs/`: `C-analysis.md` (its rules), `D-register.md`, `E-yemen-row.md` and `F-scenario-walk.md`;
- Stage 1's records in `studies/yemen-cases/`, and the sources any of these files cite, to check them.

Leave out `notes*.md` and `note` columns, so that your reading is your own.

## What to check

1. **The grouping.** Does each founder decision ask one question the founder can answer once? Was anything grouped that should stand apart, because changing it later costs more in kind, or split that is one question? Run `python3 -I method/register_items.py studies/subjects/S-02`: every founder item answered or moved exactly once.
2. **The options and the evidence.** Does each option's description of the platforms follow from phase C's rows and the statements they cite? Read the statements.
3. **The recommendations.**
   - Is each marked as engineering's, and does it follow the rule it names?
   - Is anything presented as decided that is the founder's to decide?
   - Does any recommendation rest on one market's facts, or name a market?
4. **What each closes, and its cost.** Does each closed option have one of the three reasons? Is each `cost_later` right? Look for the option the register missed, and the case where a recommendation fails.
5. **The Yemen row.** Does each fact show what the row claims, read with its date and `corrections.md`? Is any need that only Yemen shows written as a product gap, without Yemen's name?
6. **The scenario walk.** Does each cost follow? Is any `a redesign` or `premature` flag missing, or wrong?
7. **Citations.** Run `python3 -I method/check_register.py studies/subjects/S-02/register.tsv`, and check a sample of the other files' citations by hand.

## Output

`studies/subjects/S-02/review.md` holds:
- a numbered list of findings, each with:
  - the file and id;
  - the problem;
  - the evidence for it;
  - `must fix` or `optional`;
- at the end, the count of items checked under each heading above.

**Size:** about 60 requests. At about 90, write what you have and stop.

**Report:** your findings, most serious first, and the counts.
