# Earlier research, and the model, the seam and the decisions

**25 October 2026, revised the same day after its independent check** (`decisions/checks/M1-evidence-and-model-check.tsv`; what was done with each finding: `decisions/checks/M1-evidence-and-model-dispositions.md`). Part three of the assessment you asked for before Decision 1. Parts one and two are `reports/M1-method-assessment.md` and `reports/M1-plan-changes.md`; part four, on where the plan of 24 October lives, is `reports/M1-plan-trace.md`.

It answers two questions:
- whose words the research from before this repository is, and how to use it;
- what role the obligation-to-payout model has, and how the model, the seam, the evidence and the decisions relate.

## In short

- **Earlier agent-made work is a source of candidates and pointers.** It is never evidence, and never a ceiling on the design.
  - The method says this only in part:
    - amendment 2c says a record never rests "on another record's or a draft's wording";
    - section 13 lists what is "Not safe to rely on as they stand", each "checked when a decision rests on it", but names only the drafts and the seam's currency edition;
    - and section 13 keeps the seam, the drafts and the checks' findings "as evidence and inputs, not as deliverables". That heading counts agents' writing as evidence.
  - D-002 states the rule: it "takes no fact from" the seam "unless the fact is traced to a held source". It mostly applies it. One claim of absence still rests on the seam's reading, for Salla (D-002:193), and the record says so (:207).
- **Three gaps remain:**
  - three of the four artifacts have no disposition. 4c, proposed in part one, gives them one;
  - section 13's heading lets an agent's note count as evidence. And I applied a reviewer's suggestion without checking it against the schema, which section 6 already requires. That is how D-003's false "reversal twin" claim came in;
  - known errors stay in the artifacts, ready to be picked up again.
- **"The model behind the seam" was half right, and my correction of it was wrong.**
  - The model came first. Its 81 question rows were filed with it at 04:11 UTC on 10 October. The seam tagged each of them to its contract's elements, and the gaps the tagging found produced the seam's rules (`8946887:studies/payment-seam/seam.md`:104–106, 170; `rows-tagged.tsv`). So through its rows, the model was one of the seam's inputs.
  - The seam's facts about Shopify came from the payments study, which its notes cite on 121 lines, and from the engineering sources. No file of the seam cites the model's eight lines.
- **The model never read Shopify's engineering sources.** Its page says it was "read from Shopify's help center, developer docs and shipped schemas", dated 9 October. The engineering sources were captured at 08:30 UTC on 10 October, after the model's commit, and it cites none of them.
  - By the Knowledge Map's source types, those are a platform's declarations and its shipped artefacts. Neither can tell why a design exists or how it is built inside. Engineering writing and open-source code can.
  - The seam read the engineering sources; the model didn't.
- **What the work produces** is decisions and the architecture description. The model is part of that description, not a separate artifact. Earlier models are candidate concepts, judged against the drivers: your yardsticks.
- **The seam's place:**
  - **The route put a candidate first.** The plan of 24 October, which you approved, made the seam's contract v0 the boundary's starting draft (`METHOD.md` section 14), and put the money boundary before the spine's quality scenarios. M1 followed it. The same line on F-06's restored row was my annotation, not your decision.
  - **The acceptance rule already covered the scenarios.** It requires a record to name anything that could reverse it, and the scenarios could. Neither D-002 nor D-003 named them, and their checks didn't catch it.
  - **Corrected:** both now list M2's scenarios (S-02) among what they don't carry, with the outcomes that could change them.

## 1. Whose words are whose

All four came from a session before this repository. The first three, with the 81 payment rows, were added in its first commit (`caad5aa`, 10 October, 04:11 UTC). The Knowledge Map's questions came on 12 October (`7cdba34`).

| Artifact | Whose words | What to keep | How it is verified | Known errors |
| --- | --- | --- | --- | --- |
| **Shopify payments study** (`shopify-payments-study/`), eight reading passes | Agents' readings of Shopify's help, developer docs and schemas, with about 90 passages marked as inference. Some sources are a schema extract never held here ("scratchpad/schema"). The schema itself is in observed-sh | A reading map of Shopify's payments in eight slices, and its pointers to sources | Each claim a record relies on is traced again to observed-sh at its pinned commit | "Every type has a reversal twin" (`E-pos-finance-billing.md`:189), and "Nearly every non-core type has a `_REVERSAL` twin" (`A2-processor.md`:242): 38 of 114 types are reversals (D-003, `GQL:3240`) |
| **Yemen setup options** (`yemen-setup-options/`) | Agents' research on Yemen's payments, from web sources | 17 setup options in 5 positions (`report.md`:92), as candidate options for S-07; its sources as leads | Stage 1 worked from the captured sources, including those the options cited, and its brief barred it from reading the options themselves (`studies/yemen-cases/brief.md`:194). The options' own claims were never checked one by one | Built around the first market, by design. The market guard now keeps that to Context |
| **Obligation-to-payout model** (`model/`), "payments study · read from Shopify's help center, developer docs and shipped schemas · 2026-10-09" | Agents' synthesis of the two studies above: eight lines, and 81 question rows (42 from the study, 39 from the Yemen options), filed as `register/pay-questions.tsv` | Its eight lines as candidate design concepts. At least four already appear in D-002, D-003 and the market guard: the attempt's identity; outcomes from more than processors; the four records kept apart; "the shape is fixed; the values vary" | A line a record uses is set first beside what the held engineering writing and code say of the same concern, each weighed by its source type. Then it is judged against the drivers. Its rows are S-01's (`decisions/subjects.tsv`, PAY-01 to PAY-81): the seam tagged them, and they are reconciled at the end (M8) | Made before the engineering sources were captured. *Interpretation:* its settlement line, "a reversal type for each correction", rests on the same reading as the study's. One of its Yemen rows asks how "a currency edition (YER-old, YER-new) and a zone travel with every amount" (PAY-73), which G1's B7 rules out of the core; whether the seam took its edition from PAY-73 isn't shown |
| **Knowledge Map questions** (`register/km-questions.tsv`) | Questions from a session before this repository | Already disposed of: pulled at each subject's framing, and reconciled at the end | Your decision of 24 October ("judge its provenance and value"), applied at M0 | 46 of its 51 Salla paths moved (R-03) |

**When agents build on agents.** The reversal-twin claim shows the chain:
1. the study read Shopify's schema through an extract never held here, and wrote "Nearly every non-core type has a `_REVERSAL` twin" (`A2-processor.md`:242);
2. the seam's note made it absolute, citing that passage: "114 balance-transaction types, each with a reversal twin" (`8946887:studies/payment-seam/notes/shopify-crossings.md`:141);
3. a reviewer recommended it to D-003 as a precedent (`decisions/checks/D-002-D-003-review.md`:67);
4. I applied the suggestion without checking it against the schema, and D-003 cited the seam's note (`b9ff59d`).

Steps 2 to 4 each cited the agent before them, and none went back to Shopify. Each step dropped a hedge. M1's Terms and Scope pass corrected the claim against the schema (`24961d6`; D-003, `GQL:3240`). The study and the note still say it.

**Already covered:**
- amendment 2c, on another record's or a draft's wording;
- section 13's list of what is not safe to rely on, each "checked when a decision rests on it". It names the drafts and the seam's currency edition, not the three artifacts;
- section 6's rule that the coordinator checks each finding against its evidence before applying it;
- the evidence standard's facts, interpretations and assumptions;
- your decision of 12 October: the 81 payment rows and the Knowledge Map's 179 questions "are agent-written and must not be taken as Sharrwah's requirements, though some may be genuine questions" (`founder-decisions.tsv`, G0);
- your decision on the Knowledge Map of 24 October.

**Proposed with this:**
- **4c** (part one): a disposition for every body of earlier work, naming whose words it holds and its known errors, without editing the artifacts. The evidence base stays frozen.
- **4e, revised after the check:**
  - **Amendment 2c is widened.** A record never rests on the wording of another record, a draft, a study, a note, a model or a check. Each of these can point to a source, and a fact rests on the source.
  - **Section 13's heading** becomes "Kept as inputs and pointers, not as deliverables". What it lists as evidence stays evidence: `evidence/`, and Stage 1's quoted sources.
  - **The checker at levels 2 and 3** confirms that each fact a record rests on resolves to a source, not to agents' writing.
  - **A checker that recommends a precedent** cites the source for it.

  The version sent earlier would have barred D-002's own drivers: Shopify's developer docs (E030 to E036) are held in this repository's `evidence/`, not in the evidence repositories. It also proposed a script flag that would hit the records' deliberate pointers to the seam. Both are dropped.

**Not proposed:**
- reconciling or updating the four artifacts in bulk (W-01, research without end). They are reconciled when a subject reaches their area, as the Knowledge Map's rows are;
- making them a ceiling, or the seam's given input. A candidate is one option among others.

## 2. The model, the seam, the evidence and the decisions

**In this project:**
- **Evidence** is:
  - what the platforms say and do, held in observed-sh, observed-sa and this repository's `evidence/`;
  - and the first market's facts, quoted from their sources by Stage 1.
- **Drivers** are your yardsticks:
  - your goals and decisions: the guard on money, the market guard, the 34 areas. Your decisions of 10 October, F-06 among them, came from the early studies: none of them chooses among design options (your note of 25 October);
  - the constraints;
  - the quality scenarios, with your business targets. These come at M2 and don't exist yet.
- **Candidates** are known designs: the references' own designs, outside experience such as engineering writing and open-source code, and earlier research such as the seam's contract v0 and the obligation model.
- **Decisions** choose among candidates, against the drivers, on evidence, one record each.
- **The seam** is the subject of one decision, D-002: where the line between the order side and payments falls, and what crosses it.
- **The model** is the resulting structure: the architecture description's building blocks, concepts and glossary. It is an output, not an input.

**The order, after Attribute-Driven Design (Cervantes and Kazman 2016) and ATAM:**
1. drivers;
2. design concepts from known designs;
3. decisions, with views sketched as they are made;
4. evaluation against the scenarios (ATAM, section 8);
5. then again, a part at a time.

The architecture description records the result.

**Where M1 stands against that order:**
- **D-001 used only drivers we already had:** your guard, who the references show holding the money, the first market's licensing, and one platform for many markets.
  - Its outcome doesn't depend on the seam's details. *Interpretation:* it needs only that some boundary keeps the order side out of the money. Both references keep payment providers apart from orders (glossary, *payments side*), so the boundary comes from the product class's evidence, not from F-06.
  - D-001 states the reversal path as conditional, "if the payment boundary holds, which is still being proven (D-002)", and takes neither F-06 nor D-002 as given. D-002 no longer takes F-06 as given either. *(Interpretation:* as a given, F-06 pre-empted D-002's own option 2, the order side calling each provider directly.)
- **D-002 took the seam's contract v0 as option 1 of three,** as the route set out. It judged them against drivers we had:
  - D-001's room for A and B;
  - providers' interfaces that keep changing (E032, E035);
  - Shopify's asynchronous contract with providers (E031);
  - the market guard.

  It did this before M2's quality scenarios existed. So for D-002 and D-003 the work so far has validated a candidate early, as proposals. *Interpretation:* the risk is anchoring. The seam's shape could steer the scenarios meant to judge it.
- **What was wrong:**
  - D-002 and D-003 could have been accepted once S-03, S-05, S-06, S-07, S-10 and S-11 had settled their items, without meeting M2's scenarios.
  - The acceptance rule already required them to name the scenarios, since the scenarios could reverse them. They didn't, and their scope checks missed it.
- **What is corrected now:**
  - Each lists M2's quality scenarios (S-02) among the items it doesn't carry, with the outcomes that could change it. For D-002: a target on how long a payment may stay pending, or on what checkout does while a provider can't be reached, could change its outcome record or its capabilities. For D-003: a reconciliation or audit target could change when an entry posts.
  - The scenarios are written by an agent whose brief names neither D-002, D-003 nor the seam, from your targets and the capability map. Then D-002 is walked through them beside its alternatives.

**"Are we producing the model, deriving it, or validating one that should have come first?"**
- We derive it: decisions on evidence, against your yardsticks, recorded as the architecture description.
- No earlier model had to come first. The method's first outcome is the decisions and the description (`METHOD.md` section 1). The model is part of the description, not a separate artifact.
- Earlier models contribute as candidates, which is how they inform without deciding.
- In D-002 and D-003 we are validating one candidate early, as proposals, until M2's scenarios judge them.

**Why this order is right:**
- **Drivers before candidates** keep the yardsticks from being shaped by the answer.
- **Candidates before inventing** keep years of others' engineering in view, as you asked on 24 October ("we're buying architectural intelligence"). The engineering sources we already hold come before any new ones, each weighed by its type.
- **Evaluation before acceptance** keeps an early candidate from hardening by default.

For the money boundary, the route kept the second rule and bent the first. The third is what now holds D-002 and D-003.

## What you're asked

One thing to decide, with amendment 4: 4e as revised here, which changes section 13's heading and widens 2c.

Section 14 still says the boundary "starts from" the seam's contract. It governed only the first subject, and D-002 treated the contract as one option of three. The general rule stays: drafts and studies are candidate options. The same answer covers amendment 4: approve / approve with changes / not now.
