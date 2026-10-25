# Earlier research, and the model, the seam and the decisions

**25 October 2026.** Part three of the assessment you asked for before Decision 1 (parts one and two: `reports/M1-method-assessment.md`, `reports/M1-plan-changes.md`). It answers two questions:
- whose words the research from before this repository is, and how to use it;
- what role the obligation-to-payout model has, and how the model, the seam, the evidence and the decisions relate.

## In short

- **Earlier agent-made work is a source of candidates and pointers.** It is never evidence, and never a ceiling on the design.
  - The method already says this for part of it. Section 13 keeps the drafts as "candidate options" and the seam among "evidence and inputs, not deliverables". It lists what is "Not safe to rely on as they stand", each "checked when a decision rests on it". Amendment 2c says a record never rests "on another record's or a draft's wording".
  - D-002 applied it: it "takes no fact from" the seam "unless the fact is traced to a held source".
- **Three gaps remain:**
  - three of the four artifacts have no disposition (4c covers that);
  - the evidence standard lets an agent's note pass as "a file at a commit". D-003's false "reversal twin" claim came in that way;
  - known errors stay in the artifacts, ready to be picked up again.
- **"The model behind the seam" was my error.** The seam's Shopify notes cite the Shopify payments study on 121 lines (27 in the note, 94 in its table), and no file of the seam cites the model. The model and the seam are siblings from 10 October, both built on that study.
- **What the work produces** is decisions and the architecture description, and the model emerges from them. Earlier models are candidate concepts, judged against the drivers: your yardsticks.
- **The seam's place** rests on drivers we already had. Its details should be judged against the quality scenarios M2 will set. Until now nothing required that before D-002 or D-003 could be accepted. That is corrected: both now list M2's scenarios (S-02) among what they don't carry.

## 1. Whose words are whose

All four came from a session before this repository. The first three were added in its first commit (`caad5aa`, 10 October, 04:11 UTC). The Knowledge Map's questions came on 12 October (`7cdba34`).

| Artifact | Whose words | What to keep | How it is verified | Known errors |
| --- | --- | --- | --- | --- |
| **Shopify payments study** (`shopify-payments-study/`), eight reading passes | Agents' readings of Shopify's help, developer docs and schemas, with about 70 marked inferences. Some sources are a schema extract never held here ("scratchpad/schema"); the schema itself is in observed-sh | A reading map of Shopify's payments in eight slices, and its pointers to sources | Each claim a record relies on is traced again to observed-sh at its pinned commit | "Every type has a reversal twin" (`E-pos-finance-billing.md`:189): 38 of 114 types are reversals |
| **Yemen setup options** (`yemen-setup-options/`) | Agents' research on Yemen's payments, from web sources | 17 setup options in 5 positions (`report.md`:92), as candidate options for S-07; its sources as leads | Its facts were redone, with checks, by Stage 1 (`studies/yemen-cases/`) | Built around the first market, by design. The market guard now keeps that to Context |
| **Obligation-to-payout model** (`model/`), "a study filed beside the Knowledge Map" | Agents' synthesis of the two studies above: eight lines, and 81 proposed question rows (42 from the study, 39 from the Yemen options) | Its eight lines as candidate design concepts. Most already appear in D-002, D-003 and the market guard: the attempt's identity, outcomes from more than processors, the four records kept apart, "the shape is fixed; the values vary" | Judged against the drivers when a record uses a line; its rows are placed at the end (M8) | *Interpretation:* its settlement line, "a reversal type for each correction", rests on the same reading as the study's |
| **Knowledge Map questions** (`register/km-questions.tsv`) | Questions from a session before this repository | Already disposed of: pulled at each subject's framing, and reconciled at the end | Your decision of 24 October ("judge its provenance and value"), applied at M0 | 46 of its 51 Salla paths moved (R-03) |

**When agents build on agents.** The reversal-twin claim shows the chain:
1. the study stated it;
2. the seam's notes repeated it, citing the study ("114 balance-transaction types, each with a reversal twin", `9831536:studies/payment-seam/notes/shopify-crossings.md`:141);
3. a reviewer recommended it to D-003 (`decisions/checks/D-002-D-003-review.md`:67);
4. D-003 cited the seam's note as its source.

Each step cited the agent before it, and none cited Shopify. M1's terms inventory caught it against the schema. The study and the notes still say it.

**Already covered:**
- section 13's rule that earlier work is input, "checked when a decision rests on it";
- amendment 2c;
- the evidence standard's facts, interpretations and assumptions;
- your decision on the Knowledge Map of 24 October;
- 4c, proposed in part one: a disposition for every body of earlier work.

**Missing, and the smallest addition:**
- **Facts about platforms must come from the platforms (proposed as 4e, joining amendment 4).**
  - One sentence in section 6: "A fact about what a platform does traces to the platform's own words or behaviour, held in the evidence repositories. A study, note, draft, model or check sheet can point to it; it is never the source."
  - `method/decision_status.py` flags a record whose facts cite such a path.
  - This extends 2c from "another record's or a draft's wording" to everything agents write.
- **4c's dispositions name whose words each artifact holds and its known errors,** without editing the artifacts: the evidence base stays frozen.

**Not proposed:**
- reconciling or updating the four artifacts in bulk (W-01, research without end). They are reconciled when a subject reaches their area, as the Knowledge Map's rows are;
- making them a ceiling, or the seam's given input. A candidate is one option among others.

## 2. The model, the seam, the evidence and the decisions

**In this project:**
- **Evidence** is what the platforms say and do, held in observed-sh and observed-sa, and the first market's facts, held in Stage 1.
- **Drivers** are your yardsticks:
  - your goals and decisions: the guard on money, F-06 (payments as their own concern), the market guard, the 34 areas;
  - the constraints;
  - the quality scenarios, with your business targets. These come at M2 and don't exist yet.
- **Candidates** are known designs: the references' own designs, outside experience, and earlier research such as the seam's contract v0 and the obligation model.
- **Decisions** choose among candidates, against the drivers, on evidence, one record each.
- **The seam** is the subject of one decision, D-002: where the line between the order side and payments falls, and what crosses it.
- **The model** is the resulting structure, recorded in the architecture description: its building blocks, concepts and glossary. It is an output, not an input.

**The order, as Attribute-Driven Design gives it (Cervantes and Kazman 2016, which the method cites):**
1. drivers;
2. candidate concepts from known designs;
3. decisions among them;
4. evaluation: scenarios walked through the decisions (ATAM, section 8);
5. the model, recorded in the architecture description.

**Where M1 stands against that order:**
- **D-001 used only drivers we already had:** your guard, and the risks of holding money. Its outcome doesn't depend on the seam's details. It needs only that some boundary keeps the order side out of the money, which F-06 already required.
- **D-002 took the seam's contract v0 as option 1 of three.** It judged them against drivers we had:
  - D-001's room for A and B;
  - providers' interfaces that keep changing (E032, E035);
  - Shopify's asynchronous contract with providers (E031);
  - the market guard.

  It did this before M2's quality scenarios existed. So for D-002 and D-003 the work so far has validated a candidate early, as proposals. *Interpretation:* the risk is anchoring. The seam's shape could steer the scenarios meant to judge it.
- **What was wrong:** D-002 and D-003 could have been accepted once S-05 and S-07 settled their items, without ever meeting M2's scenarios.
- **What is corrected now:**
  - Each lists the quality scenarios (S-02) among the items it doesn't carry. So neither can be accepted before it is judged against them, under the existing acceptance rule.
  - At M2, the scenarios are written from your targets and the capability map, with D-002 not among their inputs. Then D-002 is walked through them beside its alternatives.

**"Are we producing the model, deriving it, or validating one that should have come first?"**
- We derive it: decisions on evidence, against your yardsticks, recorded as the architecture description.
- No earlier model had to come first. The method's first outcome is the decisions and the description, not a model (`METHOD.md` section 1).
- Earlier models contribute as candidates, which is how they inform without deciding.
- In D-002 and D-003 we are validating one candidate early, as proposals, until M2's scenarios judge them.

**Why this order is right:**
- **Drivers before candidates** keep the yardsticks from being shaped by the answer.
- **Candidates before inventing** keep years of others' engineering in view, as you asked on 24 October ("we're buying architectural intelligence").
- **Evaluation before acceptance** keeps an early candidate from hardening by default.

M1 kept the second rule. It bent the first for D-002 and D-003. The third is what now holds them.

## What you're asked

Nothing new to decide. 4e joins amendment 4, for the same answer: approve / approve with changes / not now.
