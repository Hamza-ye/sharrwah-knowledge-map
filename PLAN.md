# Plan: from the evidence to the decisions that are expensive to change

**Status: proposed on 12 October 2026. It waits for the founder's go (gate G0).** Until then `NEXT.md` stands and nothing runs.

The coordinating session wrote this plan after the founder asked who would manage the work until it reaches a safe shore, with the right engineering, sequence and framing, leaving the founder only what is genuinely theirs to decide. Where a rule comes from known practice, it names its source, and section 10 lists the sources. A rule without a source is the coordinator's own.

## 1. The aim and the safe shore

Sharrwah is one platform for many markets. Yemen is its first market, not its design target. Before building, the decisions that would be expensive to change later have to be made on evidence. Everything else is decided while building, where it is cheap to change.

- **One platform, many markets.** The platform is built once and each market is set up on it: product line engineering (Pohl, Böckle & van der Linden 2005).
- **Hide what is likely to change.** Each decision likely to change sits behind its own module (Parnas 1972).
- **Effort follows risk.** Analysis effort goes where a wrong decision costs most (Fairbanks 2010; Boehm 1988), and each decision is taken at the last responsible moment (Poppendieck & Poppendieck 2003).

**The safe shore.** This plan ends when:
1. every subject in scope has its variation points, each with the variants the five references show, their evidence, their cause and how they coexist;
2. every Yemen case is marked against every subject;
3. every existing question row is placed against a subject, or listed as unplaced with its reason;
4. a decision register states, for each subject, what follows by engineering rule and what the founder decided or deferred;
5. nothing in the register rests on a derived document, or on the founder's words taken as evidence of what a platform does.

Then the design of the first build starts, under its own plan: a thin slice for Yemen, with each variation point behind its own module.

## 2. What changes from the run so far

- **Q1's question stands, but "done" changes.** Done no longer means every concern on every placement on every platform. It means every subject in scope. The five platforms' inventories, concerns and 8,191 statements stay as they are and become the index the subjects draw from. Known practice scopes analysis by what will be built and by risk (Schmid 2002; Clements & Northrop 2001).
- **The test form becomes the main instrument.** It runs per subject, with matching and gap-closing inside the subject. It no longer waits for a full re-match.
- **Q2 splits.** Its first step, Yemen's axes and cases, runs early because scoping needs it. Its marks run per subject.
- **Q3 runs per subject.** At the end it lists the rows no subject took and the subjects no row asks about.
- **Retired:** the 84 unclear matches, unreviewed. The 88 matches stay only as hints for scoping.
- **Gaps** are closed only where a subject needs them. Before a gap goes to anyone, its route is checked against what is held.

## 3. Who does what

**The founder decides what is genuinely theirs:**
1. **Scope:** what Sharrwah will and won't be, its business model, and which markets come after Yemen.
2. **Company and legal questions:** legal entities, licences, whether Sharrwah holds funds, and partners. Where law is involved, these are decided with a lawyer.
3. **Building ahead:** how far to build for markets not yet planned, that is, whether a variation point stays open or is bound now.
4. **Spending:** stores on paid plans and consultations.
5. **What only the founder can do:**
   - capturing from inside Yemen;
   - journeys in real stores;
   - contacting platforms, partners and regulators;
   - attestations.
6. **The gates** in section 5.

Nothing reaches the founder without a decision attached. Each item comes with its evidence, its options and the coordinator's recommendation, marked as such. Section 5 says when each is needed and what an item looks like.

**Not the founder's to settle.** These follow from evidence and rule, or are the coordinator's engineering calls. The founder may challenge any of them.
- what a platform states, and whether two platforms' concepts match (section 6);
- whether a page is held, and each gap's kind and route;
- causes, coexistence and generality (the test form);
- what follows from a result by engineering rule;
- sequencing, briefs, and fixes to the method within this plan.

**The coordinating session (Claude Code).** It:
- frames each step and writes the briefs;
- runs the agents and checks;
- integrates the results;
- keeps this plan and `STATE.md`;
- brings the gates.

It never takes the founder's decisions, and never treats the founder's words as evidence of what a platform does.

**Agents.** Each gets one bounded task from a written brief. Before a brief runs, a separate agent reads it for anything that presupposes the answer (inspection: Fagan 1976). After it runs, a separate agent reviews the result against its sources (independent verification: IEEE 1012).

**The checker** (`method/check_concern_map.py`, extended) enforces the rules mechanically:
- quotes are verbatim;
- citations are at a commit;
- gap routes are checked against what is held;
- a "searched, not found" lists what it read;
- every row is tied to a subject.

## 4. The sequence

Gate G0 comes first: the founder's go on this plan. Stages 0 and 1 don't depend on each other and run side by side.

### Stage 0. Repair and freeze

*The coordinator does this with no input from the founder.*

- **Freeze.** No new concerns, statements or gaps go into the five platform folders unless a subject needs them.
- **Read what is held.** observed-sa at `57ba48d1` now holds as text:
  - the help centre's 2,938 articles (`structures/salla/help-articles`);
  - the eleven pages about Salla's terms (`structures/salla/com-policies`, `structures/salla/partners-legal`).

  Its fetch archives are in git, except five that are over GitHub's size limit. A WARC reader is added only if a subject needs a page that is held nowhere else.
- **Check every gap's route against what is held,** on all five platforms. That means observed-sa's and observed-sh's indexes and structures, and this repository's capture runs.
  - A gap whose page is held goes to an agent as "page not read".
  - `gaps-to-close.md` and `evidence/product-class/to-save-from-browser.md` are regenerated, so neither asks the founder for anything held.
  - No gap is closed in this stage.
- **Checker rules.**
  - A "searched, not found" lists what it read, at a commit. An index or a sitemap doesn't count, and a held corpus left unsearched rules that kind out.
  - Every gap route is checked against what is held.
- **Continuity.** Write `CLAUDE.md` and start using `STATE.md` (section 9).
- **Done when:**
  - the checker passes on all five platforms with the new rules;
  - the statements are unchanged;
  - the founder's capture list holds only what isn't held;
  - the founder has the counts of gaps re-routed per platform.

### Stage 1. Yemen's axes and cases

*This is Q2's first step, run on its own.*

- It finds the axes Yemen varies along, and builds the cases on them, with today as the anchor case. It uses Yemen evidence only, as Q2 says.
- Where an axis has no evidence, the case is marked unknown, not inferred. The founder's capture list says what would show it.
- **Done when** every axis and case cites its evidence or is marked unknown.

### Stage 2. The pilot: one subject end to end

**Subject:** who holds the merchant's funds between the buyer's payment and the merchant's payout. It was chosen because:
- holding money is the first of the concerns Q1 names as shaping the architecture in every market;
- it touches every placement and each axis Q2 names as an example;
- matching by words failed on it (U-027), so it tests the fix;
- taking the riskiest subject first shows early whether the method holds (Boehm 1988).

**Steps:**
1. Run the test form across the five references, with matching and gap-closing inside it.
2. Mark it against every Yemen case (Q2).
3. Place the existing rows that touch it (Q3).
4. Write its decision-register entry.
5. Have it reviewed independently.
6. Write a method report: what broke and what changed.

**Done when** there is one register entry the founder can decide from, or a clear account of why not.

**Gate G1.** Does the entry let the founder decide? If so, the founder chooses to scale up, change the method, or re-frame.

**Kill rule.** If the entry lets the founder decide nothing, or the errors come from the method again rather than the evidence, nothing scales until the frame has been re-examined.

### Stage 3. The subject list

**Candidates come from evidence only:**
- the seven concerns Q1 names:
  - holding money;
  - licences and regulated activity;
  - legal entities per country;
  - sanctions and screening;
  - where data lives;
  - partners, and what happens when one fails;
  - currency and tax;
- every concern whose statements, in the platforms' own material, are scoped by country or region;
- every concern a Yemen axis touches;
- as hints only, the existing matches whose platforms state different things.

**Ranked by cost of change.** A subject ranks high when getting it wrong would mean changing money flows, the legal structure, the data model or partner contracts after launch. This criterion is the coordinator's own reading of Parnas's criterion and of architecturally significant requirements (Chen, Ali Babar & Nuseibeh 2013).

**Gate G2.** The founder marks business scope: what Sharrwah certainly won't do, and what it must. Nothing else.

**Output:** `studies/subjects/subjects.tsv`, with the subject, its question ("who or what fills X"), its rank, and the evidence that put it in scope.

### Stage 4. The subjects, in batches, riskiest first

- Each subject goes through the pilot's six steps. Its files go in `studies/subjects/<id>/`.
- Each batch of three to five subjects ends with:
  - a commit;
  - an update to `STATE.md`;
  - a short summary for the founder: the register entries, and the decisions that are genuinely theirs (gate G3).
- The founder's decisions go in `founder-decisions.tsv`: date, gate, question, decision, and the evidence it rested on.
- A deferred decision is recorded with what it binds: the variation point stays open and is set per market.

### Stage 5. Close-out

- **Interactions.** Subjects that touch each other, such as currency, payments and tax, are checked for bindings that conflict (Calder et al. 2003).
- **Q3's step 3.** List the rows no subject took, and the subjects no row asks about.
- **A last sweep** of the inventory's remaining concerns, for anything expensive to change that the subject list missed.
- **Gate G4, the safe shore.** The founder accepts the register, and the design of the first build starts under its own plan.

## 5. The gates

| Gate | When | What the founder decides |
| --- | --- | --- |
| G0 | Now | This plan, including the rules in section 6 |
| G1 | After the pilot | Scale up, change the method, or re-frame |
| G2 | After the subject list | Business scope: what Sharrwah won't do, and what it must |
| G3 | After each batch | The decisions the batch raised that are genuinely the founder's |
| G4 | At close-out | Accept the register, and start the design |

**When the founder is needed:**
- **Now, at G0:** the go on this plan, and Q3's rows.
- **Stages 0 and 1:** no decisions. The founder may get a capture list: what only the founder can capture, each item with why. Capturing is optional, and whatever isn't captured stays unknown.
- **At G1, after the pilot:** whether the pilot's entry lets the founder decide, and the decisions the pilot raised.
- **At G2:** business scope, marked on the subject list as won't do or must do.
- **At G3, after each batch:** that batch's decisions.
- **At G4:** accepting the register.

**What a decision item looks like.** It takes the form of an architecture decision record (Nygard 2011):
- the question in one line, and why it is the founder's;
- the evidence: each platform's statement, quoted and cited, and Q2's marks for the Yemen cases;
- the options, each with what it needs built and what it needs from outside, such as a licence, a partner or money;
- the coordinator's recommendation and its reason;
- the answer: an option, or **defer**. Defer is always allowed. The variation point stays open and is set per market, at the build cost the item states.

**Standing decisions.** The founder can state a decision once as a rule that settles every later item of its kind, such as a default business model.
- It is recorded in `founder-decisions.tsv` like any decision.
- Items it settles don't reach the founder. Each settled item names the rule that settled it.

**Spending** means money paid for evidence or advice the work needs: a store on a paid plan, a lawyer's or accountant's consultation, or an official record.
- Each request says what it buys, which decision depends on it, the cost if known, and what happens without it: the item stays unknown or open.
- Building and running Sharrwah are not part of this plan.

## 6. The rules this plan adopts

These rules are settled, each from the source named, unless the founder objects at G0.

### The test form, per subject

0. **Subject.** Is it about the product, the market context, or the company? Company questions go to the founder.
1. **Variation points.** Split the subject into questions of the form "who or what fills X".
2. **Variants.** Take them from each of the five references, each with its evidence id, its kind and its scope.
   - **Kind** comes from the citation's source:
     - observed: a recorded store or journey;
     - shipped: code or a schema the platform ships;
     - stated: the platform's docs or help centre;
     - official page: terms, pricing or legal pages.

     Kinds are compared like with like, as Q1's 12 October rule says.
   - **Absence** counts only from a complete list the platform publishes, such as an enumerated schema or a full plan table. Otherwise it is a gap.
3. **Cause,** found by comparing the references (Mill's methods of agreement and difference):
   - market, named rule: a source names the law, regulator or rule;
   - market, pattern: Salla and Zid agree with each other and differ from Shopify and BigCommerce;
   - vendor choice: platforms in the same market differ;
   - maturity: only from the platform's own release markers, such as beta or sunset;
   - business model: follows from how the platform earns or what it holds;
   - unknown.

   A cause is a reading and is labelled as one. It never becomes a platform statement.
4. **Coexistence,** by how the variant is bound (Czarnecki, Helsen & Eisenecker 2005):
   - A: the variants coexist in one store;
   - B: one per store, market or plan, set by configuration;
   - C: one per product, so one store can hold several;
   - D: mutually exclusive: a platform offers only one.

   **Generality.** When one variant is a restricted form of another, and the general one can reach it by configuration, keep the general one.
5. **What follows by rule** (Parnas 1972; Svahnberg, van Gurp & Bosch 2005):
   - A: the platform carries all the variants at once;
   - B: a variation point behind one interface, bound per market, store or plan;
   - C: bound per product;
   - D with a market cause: a variation point bound per market;
   - vendor choice or business model:
     - if expensive to change, the founder decides, on a recommendation;
     - if cheap to change, it is left to the build;
   - maturity or unknown, when expensive to change: kept open as a variation point until evidence settles it;
   - a Yemen case with no placement: a product gap, written without Yemen's name (Q2's rule 3), and a design decision for the founder.

### Matching, inside a subject

Two concerns from different platforms match only on one of four bases, each shown in the platforms' own words:
1. the same term, including a platform's own translation of it;
2. the same identifiers: a key, scope, topic or entitlement;
3. the same definition, with both quoted;
4. both answer the same variation point.

A partial overlap is split into variation points and recorded. It doesn't go to the founder. Matching on names alone fails on synonyms and homonyms (Rahm & Bernstein 2001), which is why the third and fourth bases exist.

### Evidence

- **Statements** stay verbatim, cited at a pinned commit, under Q1's rules.
- **Before a gap goes to anyone,** its route is checked against what is held:
  - if the page is held and readable, the gap is "page not read", for an agent;
  - if it is held but not readable, the reader is extended;
  - only what isn't held goes to the founder, with what exactly to capture and why.
- **A "searched, not found"** lists what it read, at a commit.
- **Incorporated agreements.** An agreement that a platform's terms incorporate, such as Stripe's Connected Account Agreement under WooPayments and Shopify Payments, is part of that platform's terms. It may be read when a subject needs it.
- **The founder's words** are never evidence of what a platform does. The founder's decisions about Sharrwah are recorded as decisions.

### Q3's rows

Both sets are placed, subject by subject: the 81 payment rows and the Knowledge Map's 179 questions. Rows no subject takes are listed at close-out. *This one is the founder's choice. The coordinator recommends both, because placing them per subject makes it cheap.*

## 7. Risks, and what happens when one shows

| # | Risk | How it shows | What happens |
| --- | --- | --- | --- |
| 1 | The analysis grows past what decisions need | A row or file tied to no subject; a stage past its expected size | The checker rejects untied rows; growth goes to the next gate |
| 2 | A rule, label, example or brief of ours makes the result, as our category names, the matching example and the salla.com rule did | The brief review finds a presupposition; the pilot shows it; an error traces to a rule | Briefs are reviewed before they run, and the pilot runs before anything scales. Each error is traced to its cause, and everything it touched is re-run |
| 3 | Evidence we hold goes unread | A gap's route is held | The gap can't go to the founder; the reader is extended |
| 4 | A search claims more than it read | A "searched, not found" without its list | The checker rejects it |
| 5 | Depth differs by platform: accounts for Shopify and Salla, declarations for Zid and BigCommerce, code for WooCommerce | A cause resting on absence at a weaker kind of evidence | Absence counts only from a complete list; otherwise the cause is unknown |
| 6 | The same word names different things, or different words name the same thing | A match on none of the four bases | No match. It is recorded, and it matters only if a decision depends on it |
| 7 | Evidence changes mid-work: the founder's new commits, or a platform changes a page | New commits touch cited paths | The subjects whose citations changed are listed, and only those re-run |
| 8 | A session loses its context, the container resets, or a usage limit cuts a step | Designed for in advance | Every step resumes from the repository; `STATE.md` is updated at every checkpoint, with a commit per subject |
| 9 | The founder becomes the bottleneck | An item reaches the founder with no decision attached | It doesn't reach them; each gate brings only decisions, each with a recommendation |
| 10 | Yemen evidence is thin, or only reachable from inside Yemen | An axis or case with no evidence | It is marked unknown, not inferred; the capture list says what to capture and why |
| 11 | A reading of terms becomes legal advice | A statement taken as what Sharrwah must do | Quotes only. Sharrwah's legal position is a company question, for the founder with a lawyer |
| 12 | An agent misreads: the quote is right but the meaning wrong | The independent review disagrees | The source is re-read, and the disagreement is recorded |
| 13 | The frame is wrong after all | The pilot entry lets the founder decide nothing; errors keep coming from the method | Nothing scales; the frame is re-examined at G1, with evidence |
| 14 | Old documents return as evidence | A citation to a derived or excluded path | The checker rejects it, as it does now |

## 8. When work stops and comes to the founder

- **An error touches results already delivered.** It is measured and reported, then fixed, as with the Salla gaps.
- **The pilot misses its "done when".**
- **A stage overruns its expected size twice.** `STATE.md` records the expected size before each stage starts.
- **A founder decision blocks the next subject,** where the decision is genuinely the founder's.
- **New evidence changes more than one finished subject.**
- **Something needs money, contact with a third party, or a legal judgment.**

## 9. Keeping it coherent across sessions

- **How this plan changes.** Only by a dated entry in section 11, with the reason and the source.
  - A change to the frame needs the founder's go.
  - A fix to the method within this plan is recorded and reported at the next gate.
- **`STATE.md` says where the work is:** the stage, the subject, what is done, the next step and the open gate. It is updated and committed at every checkpoint.
- **Every unit ends with a commit,** whether one subject or one batch. Every step can resume from the repository alone.
- **Every result traces back** through subject, variation point, variant and statement to a source at a commit (Gotel & Finkelstein 1994).
- **`CLAUDE.md` sets what each session reads first.**
  - The coordinating session reads this plan, `STATE.md` and `founder-decisions.tsv` before anything else.
  - An agent working from a brief reads only its brief and what the brief names, so that nothing in this plan steers its reading.

## 10. Sources

- Boehm, B. (1988). A spiral model of software development and enhancement. *IEEE Computer* 21(5). Risk-driven sequencing; the riskiest part first.
- Calder, M., Kolberg, M., Magill, E., Reiff-Marganiec, S. (2003). Feature interaction: a critical review and considered forecast. *Computer Networks* 41(1). Interactions between subjects.
- Chen, L., Ali Babar, M., Nuseibeh, B. (2013). Characterizing architecturally significant requirements. *IEEE Software* 30(2). What makes a subject rank high.
- Clements, P., Northrop, L. (2001). *Software Product Lines: Practices and Patterns.* Addison-Wesley. Scoping as a core practice.
- Coplien, J., Hoffman, D., Weiss, D. (1998). Commonality and variability in software engineering. *IEEE Software* 15(6). The test form's analysis.
- Czarnecki, K., Helsen, S., Eisenecker, U. (2005). Staged configuration through specialization and multilevel configuration of feature models. *Software Process: Improvement and Practice* 10(2). Who binds a variant, and when.
- Fagan, M. (1976). Design and code inspections to reduce errors in program development. *IBM Systems Journal* 15(3). Inspection, used here on briefs.
- Fairbanks, G. (2010). *Just Enough Software Architecture: A Risk-Driven Approach.* Marshall & Brainerd. Effort in proportion to risk.
- Gotel, O., Finkelstein, A. (1994). An analysis of the requirements traceability problem. *First International Conference on Requirements Engineering.* Tracing each result to its source.
- IEEE 1012, Standard for System, Software, and Hardware Verification and Validation. Independent review.
- Kang, K., Cohen, S., Hess, J., Novak, W., Peterson, A. (1990). *Feature-Oriented Domain Analysis (FODA) Feasibility Study.* CMU/SEI-90-TR-21. Domain analysis from existing systems, which is what Q1 is.
- Mill, J. S. (1843). *A System of Logic.* The methods of agreement and difference.
- Nygard, M. (2011). Documenting architecture decisions. Cognitect blog. The form of a decision item.
- Parnas, D. (1972). On the criteria to be used in decomposing systems into modules. *Communications of the ACM* 15(12). Each decision likely to change behind its own module.
- Pohl, K., Böckle, G., van der Linden, F. (2005). *Software Product Line Engineering.* Springer. One platform, many products.
- Poppendieck, M., Poppendieck, T. (2003). *Lean Software Development: An Agile Toolkit.* Addison-Wesley. Deciding at the last responsible moment.
- Rahm, E., Bernstein, P. (2001). A survey of approaches to automatic schema matching. *VLDB Journal* 10(4). Why matching on names alone fails.
- Schmid, K. (2002). A comprehensive product line scoping approach and its validation. *ICSE 2002.* Scoping by what will be built.
- Svahnberg, M., van Gurp, J., Bosch, J. (2005). A taxonomy of variability realization techniques. *Software: Practice and Experience* 35(8). How a variation point is realized, by when it is bound.

## 11. Changes

- **12 October 2026:** proposed by the coordinating session. It waits for G0.
- **12 October 2026,** after the founder's questions: section 5 now says when the founder is needed, what a decision item looks like, how standing decisions work, and what spending covers.
