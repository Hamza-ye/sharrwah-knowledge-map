# Brief: S-02, the scenario walk (step 3)

This is `PLAN.md` Stage 4, subject S-02, its section 6, step 7: the scenario walk. You are one agent with one task. The coordinator checks your rows, and an agent that made none of it reviews them.

**Why.** A recommendation that turns a plausible future into a redesign is closing an option. The walk finds those before anything builds on them, so that each one reaches the founder: either it is changed, or it is kept with its reason on the record (change scenarios in architecture evaluation: Kazman, Klein & Clements 2000).

**Read only:**
- this brief;
- `PLAN.md`, section 1 and section 6, step 7;
- `founder-decisions.tsv`, its row of 28 October (Sharrwah's markets: the GCC; North Africa, among them Egypt, Morocco, Algeria and Tunisia; Jordan, Lebanon and others; Yemen among them);
- `studies/subjects/S-02/register.tsv` and `decisions.md`;
- S-02's evidence, as a scenario needs it: phase C's files (`c/RD1/`, `c/RD2/`, `c/RD3/`), statements by id through `python3 -I method/subject_slice.py studies/subjects/S-02 --print RD1 --ids ...`, with RD2 or RD3 for their slices; a statement in no slice is in its platform's `statements.tsv`.

## The task

For each root decision, take each founder decision's recommendation, and each engineering constraint, through these scenarios:
1. **A second market whose conditions differ on the decision's question.** Prefer a market of the founder's where S-02's evidence shows such a difference, and cite it. Examples: Zid's contracting company and law for Egypt; a store's VAT on Zid's fees varying by the store's country; Salla's verification flow for the UAE. Where the evidence shows none, state the difference as a hypothesis and mark it as one.
2. **The company based in another country,** such as Oman or Egypt.
3. **The first market dropped.**

For each scenario, write:
- what changes;
- the cost of meeting it under the recommendation:
  - `a setting`: a value configured;
  - `one module`: a change inside one part, behind its interface;
  - `a redesign`: a change to the model or to several parts;
- which alternatives the recommendation keeps open, and which it closes. Give each closed one its reason: a confirmed fact, the founder's choice, or an engineering cost greater than the option's value. A closed option with none of these reasons is flagged `premature`.

Use S-02's evidence only. A fact it lacks is marked `unknown`, not inferred.

## Rules

- **No decision.** The walk tests recommendations; it doesn't choose between options. Where a scenario turns a recommendation into a redesign, say so plainly: that finding is for the founder.
- **No scenario rests on today's circumstances being permanent,** in any market. A constraint that traces only to one market today, or to today's capacity, is flagged.

## Output, in `studies/subjects/S-02/`

- `scenario-walk.tsv`: tab-separated, with a header row and no quoting. Columns: `root_decision` · `decision_id` · `scenario` · `market` (named, or `hypothetical`) · `what_changes` · `cost` (`a setting`, `one module`, `a redesign`) · `keeps_open` · `closes` · `reason` · `flag` (`premature`, `one market`, or empty) · `evidence` · `note`.
- Your notes in `notes-scenario-walk.md`.

**Size:** about 50 requests. At about 80, write what you have and stop, saying which decisions are left.

**Report:** per root decision, each scenario's cost under each recommendation, in a line; every `a redesign` and every flag, with why; problems.
