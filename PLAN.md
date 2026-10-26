# Plan: from the evidence to the decisions that are expensive to change

**Status: agreed by the founder on 12 October 2026 (gate G0). On 25 October 2026, after G1, the founder reset the work to this plan, with the changes section 11 lists.** It is the only plan, and it works within the founder's decisions (`founder-decisions.tsv`): where the two differ, the decision holds and this plan is corrected. `STATE.md` says where the work is.

The coordinating session wrote this plan after the founder asked who would manage the work until it reaches a safe shore, with the right engineering, sequence and framing, leaving the founder only what is genuinely theirs to decide. Where a rule comes from known practice, it names its source, and section 10 lists the sources. A rule without a source is the coordinator's own.

## 1. The aim and the safe shore

Sharrwah is one platform for many markets. Yemen is its first market, not its design target. Before building, the decisions that would be expensive to change later have to be made on evidence. Everything else is decided while building, where it is cheap to change.

- **One platform, many markets.** The platform is built once and each market is set up on it: product line engineering (Pohl, Böckle & van der Linden 2005).
- **Hide what is likely to change.** Each decision likely to change sits behind its own module (Parnas 1972).
- **Effort follows risk.** Analysis effort goes where a wrong decision costs most (Fairbanks 2010; Boehm 1988), and each decision is taken at the last responsible moment (Poppendieck & Poppendieck 2003).
- **The guard on the first market.** The founder asked for a "very visible guard" against Yemen being "used to define the hard to change product decisions" ([24 October](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf/founder-messages/2026-10-24-method-accepted.md?plain=1#L48)). So each subject's analysis is made from the references before its Yemen row (section 6, step 6), a gap only Yemen shows is written without Yemen's name (section 6, step 5), and each decision page says whether its recommendation comes out the same without Yemen, as Decision 1's does.

**The safe shore.** This plan ends when:
1. every subject in scope has its variation points, each with the variants the five references show, their evidence, their cause and how they coexist;
2. every decision in scope has its Yemen row: what each option needs in Yemen today, and whether that exists;
3. every existing question row is placed against a subject, or listed as unplaced with its reason;
4. a decision register states, for each subject, what follows by engineering rule and what the founder decided or deferred;
5. nothing in the register rests on a derived document, or on the founder's words taken as evidence of what a platform does.

Then the design of the first version starts, under its own plan. It is designed for many markets, with Yemen the first set up on it, and each variation point behind its own module. Spikes, throwaway code that answers one stated question, are allowed. Production code waits until requirements, an architecture description and engineering documentation exist to validate it against (the founder, 24 October).

## 2. What changes from the run so far

- **Q1's question stands, but "done" changes.** Done no longer means every concern on every placement on every platform. It means every subject in scope. The five platforms' inventories, concerns and 8,191 statements stay as they are and become the index the subjects draw from. Known practice scopes analysis by what will be built and by risk (Schmid 2002; Clements & Northrop 2001).
- **The test form becomes the main instrument.** It runs per subject, with matching and gap-closing inside the subject. It no longer waits for a full re-match.
- **Q2 splits.** Its first step, Yemen's axes and cases, runs early (Stage 1). Its marks ran in the pilot. From Stage 4, one Yemen row per decision replaces them, after the subject's analysis (section 6, step 6; the founder, 25 October).
- **Q3 runs once, at close-out.** It reconciles the existing rows against the finished register (Stage 5). The rows never feed a subject's analysis.
- **Retired:** the 84 unclear matches, unreviewed. The 88 matches stay only as hints for scoping.
- **Gaps** are closed only where a subject needs them. Before a gap goes to anyone, its route is checked against what is held.

## 3. Who does what

**The founder decides what is genuinely theirs:**
1. **Scope:** what Sharrwah will and won't be, its business model, and which markets come after Yemen.
2. **Company and legal questions:** legal entities, licences, whether Sharrwah holds funds, and partners. Where law is involved, these are decided with a lawyer.
   - **The guard** (the founder, 18 October): no arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision, whether Sharrwah itself holds it or a payment company holds it in an account opened through Sharrwah.
3. **Building ahead:** how far to build for markets not yet planned, that is, whether a variation point stays open or is bound now.
4. **Spending:** stores on paid plans and consultations.
5. **What only the founder can do:**
   - capturing from inside Yemen;
   - journeys in real stores;
   - contacting platforms, partners and regulators;
   - attestations.
6. **The gates** in section 5.

Nothing reaches the founder without a decision attached. Each item comes with its evidence, its options and the coordinator's recommendation, marked as such. Section 5 says when each is needed and what an item looks like.

**Plain words** (the founder, 18 October). Everything for the founder is in plain business words, and a term that can't be avoided is defined in one line. Quotes and ids stay in the files. Several decisions may come in one message, each with its own answer line. Each method ruling is listed in one plain line at the next report, and the founder may overturn any.

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
- **A review tries to refute** what it reviews, claim by claim, and reports counter-evidence and missing evidence, not agreement. The coordinator checks each finding against its evidence before applying it.
- **A review also looks for what an entry never cites:** the concerns in the subject's reach, from the concern map, that the entry doesn't cite, and which of them bear on a decision.

**The checkers** enforce the rules mechanically: `method/check_concern_map.py` on the concern map, `method/check_yemen_cases.py` on Stage 1, and `method/check_subject.py` on each subject. Between them:
- quotes are verbatim;
- citations are at a commit;
- gap routes are checked against what is held;
- a "searched, not found" lists what it read;
- every row is tied to a subject.

## 4. The sequence

Gate G0 comes first: the founder's go on this plan. Stages 0 and 1 don't depend on each other and run side by side.

### Stage 0. Repair and freeze

*Done on 12 October 2026 (`3e5b37b`). The coordinator did this with no input from the founder.*

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

*Done on 17 October 2026, in `studies/yemen-cases/`. Its independent review found errors in `today` on 12 of 45 sampled axes, and later checks found ten of its records that need a correction or a caution: [`corrections.md`](studies/yemen-cases/corrections.md). This is Q2's first step, run on its own. Since 25 October 2026 no more work goes into it: it is a reference, read only for the facts a Yemen row needs, with `corrections.md`.*

- It finds the axes Yemen varies along, and builds the cases on them, with today as the anchor case. It uses Yemen evidence only, as Q2 says.
- Where an axis has no evidence, the case is marked unknown, not inferred. The founder's capture list says what would show it.
- **Done when** every axis and case cites its evidence or is marked unknown.

### Stage 2. The pilot: one subject end to end

*Done on 17 October 2026, in `studies/subjects/S-01/`: the entry, its independent review and the method report. G1 was answered on 18 October with a re-frame. On 25 October the founder reset the work to this plan, with the pilot's own changes (`founder-decisions.tsv`, the reset). Decision 1 was answered on 25 October, and its two follow-ons on 26 October (`founder-decisions.tsv`; [`decision-1.md`](studies/subjects/S-01/decision-1.md)).*

**Subject:** who holds the merchant's funds between the buyer's payment and the merchant's payout. It was chosen because:
- holding money is the first of the concerns Q1 names as shaping the architecture in every market;
- it touches every placement and each axis Q2 names as an example;
- matching by words failed on it (U-027), so it tests the fix;
- taking the riskiest subject first shows early whether the method holds (Boehm 1988).

**Steps:**
1. Run the test form across the five references, with matching and gap-closing inside it.
2. Mark it against every Yemen case (Q2).
3. Write its decision-register entry.
4. Have it reviewed independently.
5. Write a method report: what broke and what changed.

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
- as hints only, the existing matches whose platforms state different things.

**Ranked by cost of change.** A subject ranks high when getting it wrong would mean changing money flows, the legal structure, the data model or partner contracts after launch. This criterion is the coordinator's own reading of Parnas's criterion and of architecturally significant requirements (Chen, Ali Babar & Nuseibeh 2013).

**Gate G2.** The founder marks business scope: what Sharrwah certainly won't do, and what it must. Nothing else.

**Output:** `studies/subjects/subjects.tsv`, with the subject, its question ("who or what fills X"), its rank, and the evidence that put it in scope. S-01, the pilot, is its first row.

### Stage 4. The subjects, one at a time, riskiest first

- **Before the next subject runs,** these are ruled, and each ruling is marked in the pilot's briefs, from which the next subject's briefs are made:
  - the pilot's three open items ([its method report, section 11, "Still open after the re-check"](studies/subjects/S-01/method-report.md#11-the-independent-review-f)):
    - finding 36, a variant that names only what doesn't fill the role;
    - finding 29, whether WooCommerce's policy pages are terms;
    - step 5's letter rows, which no longer separate the variation points once letters join;
  - what the checker reports on the pilot with the scripts as they now stand, and did not report at G1 (`method/check_subject.py`, given every capture run in `evidence/product-class/runs/`, run on a copy of the pilot's folder, since it rewrites the subject's `kinds.tsv`):
    - three Salla gaps routed to the founder whose page is held (S01-SA-G01, G03 and G07);
    - five statements whose source kind changes (S01-WC-078 to 080, S01-BC-123 and 124).
- Each subject goes through the pilot's five steps, with its Yemen row in place of the Yemen marks (section 6, step 6), and its scenario walk (step 7). Its files go in `studies/subjects/<id>/`. The pilot's own changes apply ([its method report, "Proposed changes before more subjects"](studies/subjects/S-01/method-report.md#proposed-changes-before-more-subjects)):
  - **Scoped to its decisions first.** The subject names its few root decisions, from the platforms' own top-level statements. Its variation points are the facets that can change one of them, and the rest stay as notes (section 6, step 1). Phase C marks which of the founder's items depend on which (its method report, section 10).
  - **From what is recorded.** Variants come first from the statements the concern map and the pilot already hold. New reading happens only where a decision needs it.
  - **Short agent runs.** Each brief caps its steps and asks for small outputs. Mechanical steps are scripts. An agent's cost is measured after its first steps (`method/count_tokens.py`), and a run whose projection passes its share of the budget is stopped.
  - **A budget per subject,** set before it starts from the last subject's measured cost, and recorded in `STATE.md`.
  - **Depth by risk.** The analysis goes deep where a decision is both expensive to change and uncertain, and runs a light check where the references agree and Yemen's facts don't bear on it.
  - **Shopify and Salla first.** Their held evidence is the deepest (risk 5), so they are read first and in full. Zid, WooCommerce and BigCommerce come from what the concern map and the pilot recorded, and are read further only where a cause or a gap needs them. The founder asked for others "only when a specific question requires them" ([24 October](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf/founder-messages/2026-10-24-method-accepted.md?plain=1#L42)); a cause by comparison is such a question (section 6, step 3).
  - **The pilot's other lessons** (its method report, sections 4 and 9): gaps that ask one question of different sources are audited together; and a Yemen fact with an exclusion such as "only" is read as two facts, since the exclusion states a second one.
  - **Yemen's facts checked before a Yemen row uses them.** Each fact is read with its date and with Stage 1's corrections, and checked against its source's quote. Stage 1 gets no `within` relation and no faithfulness pass: a fact is checked when a row uses it.
- Each subject ends with:
  - a commit;
  - an update to `STATE.md`;
  - a short report for the founder: the decisions that are genuinely theirs (gate G3), and the subject's cost against its budget.
- **Standing decisions early.** The founder's answer to a root decision settles the later items it pairs with (section 5, standing decisions), as an answer to Decision 1 can settle the pilot's Decisions 2 to 12, which its entry pairs with each option.
- The founder's decisions go in `founder-decisions.tsv`: date, gate, question, decision, and the evidence it rested on.
- A deferred decision is recorded with what it binds: the variation point stays open and is set per market.

### Stage 5. Close-out

- **Interactions.** Subjects that touch each other, such as currency, payments and tax, are checked for bindings that conflict (Calder et al. 2003).
- **Q3, once.** Reconcile the existing rows against the register:
  - place each row, and flag its time bombs;
  - list the rows the register doesn't cover;
  - list the register's decisions no row asked about.

  A row the register doesn't cover enters scope only if the evidence, not the row, shows it is expensive to change. Before starting, the coordinator decides again whether reconciling is worth its cost.
- **A last sweep** of the inventory's remaining concerns, for anything expensive to change that the subject list missed. A list of the platforms' broad areas, made after G1, may serve as a cross-check that no area was missed ([`areas.tsv`](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf/studies/proposals/areas/areas.tsv)). It is a grouping, not evidence, and it sets no subject's boundary.
- **Gate G4, the safe shore.** The founder accepts the register, and the design of the first version starts under its own plan (section 1).

## 5. The gates

| Gate | When | What the founder decides |
| --- | --- | --- |
| G0 | Before Stage 0 | This plan, including the rules in section 6 |
| G1 | After the pilot | Scale up, change the method, or re-frame |
| G2 | After the subject list | Business scope: what Sharrwah won't do, and what it must |
| G3 | After each subject | The decisions the subject raised that are genuinely the founder's |
| G4 | At close-out | Accept the register, and start the design |

G1 was answered on 18 October with a re-frame. On 25 October the founder reset the work to this plan, with the pilot's own changes (section 11).

**When the founder is needed:**
- **At G0:** the go on this plan, and Q3's rows.
- **Stages 0 and 1:** no decisions. The founder may get a capture list: what only the founder can capture, each item with why. Capturing is optional, and whatever isn't captured stays unknown.
- **At G1, after the pilot:** whether the pilot's entry lets the founder decide, and the decisions the pilot raised.
- **At G2:** business scope, marked on the subject list as won't do or must do.
- **At G3, after each subject:** that subject's decisions.
- **At G4:** accepting the register.

**What a decision item looks like.** It takes the form of an architecture decision record (Nygard 2011):
- the question in one line, and why it is the founder's;
- the evidence: each platform's statement, quoted and cited, the decision's Yemen row, and its scenario walk;
- the options, each with what it needs built and what it needs from outside, such as a licence, a partner or money;
- the coordinator's recommendation and its reason;
- the answer: an option, or **defer**. Defer is always allowed. The variation point stays open and is set per market, at the build cost the item states.

**Standing decisions.** The founder can state a decision once as a rule that settles every later item of its kind, such as a default business model.
- It is recorded in `founder-decisions.tsv` like any decision.
- Items it settles don't reach the founder. Each settled item names the rule that settled it.

**Spending** means money paid for evidence or advice the work needs: a store on a paid plan, a lawyer's or accountant's consultation, or an official record.
- Each request says what it buys, which decision depends on it, the cost if known, and what happens without it: the item stays unknown or open.
- Building and running Sharrwah are not part of this plan.
- The agents' own cost is the coordinator's to plan: each subject's budget is set from measured cost (Stage 4), and only an overrun by a quarter comes to the founder (section 8).

## 6. The rules this plan adopts

These rules are settled, each from the source named, unless the founder objects at G0.

### The test form, per subject

0. **Subject.** Is it about the product, the market context, or the company? Company questions go to the founder.
1. **Decisions, then variation points.** Name the subject's few root decisions first, from the platforms' own top-level statements. Then split each into the facets that can change it, each a question of the form "who or what fills X".
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
   - a need the Yemen row shows that no reference meets: a product gap, written without Yemen's name (Q2's rule 3), and a design decision for the founder.
6. **The Yemen row,** after the analysis (the founder, 25 October). For each decision, it says what each option needs in Yemen today, and whether that exists: a provider, a partner, a licence, a way to pay. Each fact comes from Stage 1's records, read with its date and with `corrections.md`, and is checked against its source's quote before it is used. A fact with no evidence is marked unknown, not inferred. Q2's scenarios are used only where a decision depends on a condition that is changing.
7. **The scenario walk,** after the Yemen row (the founder's proposal, 26 October). Each root decision is walked through three more scenarios: a second market whose conditions differ on the decision's question; the company based in another country, such as Oman or Egypt; and the first market dropped. The walk shows whether the decision keeps the alternatives the evidence justifies, or names what it closes, so that this reaches the founder before anything builds on it. It uses the subject's own evidence, and a fact it lacks is marked unknown, not inferred (change scenarios in architecture evaluation: Kazman, Klein & Clements 2000).

**Options beyond the references.** Where a recommendation needs more than the references show, established designs and engineering writing are read for that decision. Each is weighed by its kind of source: a company's blog is that company's own account (choosing design concepts: Cervantes & Kazman 2016). This is what the founder called "buying architectural intelligence" ([24 October](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf/founder-messages/2026-10-24-method-accepted.md?plain=1#L28)).

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
- **Every claim** in an entry or a report is one of three: a fact traced to its source at a commit, a reading marked as one, or an assumption marked as one. A gap stays visible, with the work that would close it (claims and evidence: ISO/IEC/IEEE 15026-2).
- **Evidence is looked up through the evidence repositories' own guides first:** their `README.md` and `docs/READING.md`.
- **Merchants are never asked** (the founder, 24 October). Where documents can't settle a question, it goes to the platforms, partners, regulators or a lawyer, through the founder (section 3).

### Q3's rows

Both sets, by the founder's choice: the 81 payment rows and the Knowledge Map's 179 questions, held outside the working files ([`register/`, as it stood at G1](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/e4d5cee3aaea9a12b3e27c1e641075a01d88052c/register)). They are reconciled once, at close-out, and read only for their `id`, `question`, `needed_by` and `lane`. A row never adds a variation point, a variant or a cause.

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
| 10 | Yemen evidence is thin, or only reachable from inside Yemen | A fact a Yemen row needs has no evidence | It is marked unknown, not inferred; the capture list says what to capture and why |
| 11 | A reading of terms becomes legal advice | A statement taken as what Sharrwah must do | Quotes only. Sharrwah's legal position is a company question, for the founder with a lawyer |
| 12 | An agent misreads: the quote is right but the meaning wrong | The independent review disagrees | The source is re-read, and the disagreement is recorded |
| 13 | The frame is wrong after all | The pilot entry lets the founder decide nothing; errors keep coming from the method | Nothing scales; the frame is re-examined at G1, with evidence |
| 14 | Old documents return as evidence, or old work governs again | A citation to a derived or excluded path; a brief, entry or search that draws on history outside the working files | The checker rejects the citation. History is reached only through a link pinned to a commit in a working file (section 9), and `method/check_surface.py` searches the working files for its framings |
| 15 | A decision is carried forward on its past acceptance alone | A step builds on a decision whose plan or premise has changed | It is assessed on its merits first: its rationale, its evidence, and whether it still holds (the founder, 25 October) |
| 16 | A change to this plan drops a safeguard without saying so | A change lists what it adds, not what it removes | Each change lists what it removes or weakens, with the risk that part controlled (section 9) |

## 8. When work stops and comes to the founder

- **An error touches results already delivered.** It is measured and reported, then fixed, as with the Salla gaps.
- **The pilot misses its "done when".**
- **A subject runs past its budget by a quarter.** It stops, and comes to the founder with its measured cost. Below that, a run whose projection passes its share of the budget is stopped, and the coordinator re-plans the rest (Stage 4).
- **A founder decision blocks the next subject,** where the decision is genuinely the founder's.
- **New evidence changes more than one finished subject.**
- **Something needs money, contact with a third party, or a legal judgment.**

## 9. Keeping it coherent across sessions

- **How this plan changes.** In the section it changes, so the plan stays one text, with one dated line in section 11 giving the reason and the source.
  - Each change lists what it removes or weakens, with the risk that part controlled, and whether that risk is reassigned or accepted. The list goes in the next report, where the founder sees it; it asks nothing of them (management of change; the founder, 25 October).
  - A change to the frame needs the founder's go. The frame is the aim, the safe shore and the guard on the first market (section 1), who decides what (section 3), and the gates (section 5). The rest is method, which is the coordinator's (the founder, 25 October).
  - A fix to the method within this plan is recorded, and listed at the next report (section 3).
- **`STATE.md` says where the work is:** the stage, the subject, what is done, the next step and the open gate. It is updated and committed at every checkpoint.
- **Every subject ends with a commit.** Every step can resume from the repository alone.
- **Every result traces back** through subject, variation point, variant and statement to a source at a commit (Gotel & Finkelstein 1994).
- **`CLAUDE.md` sets what each session reads first.**
  - The coordinating session reads this plan, `STATE.md` and `founder-decisions.tsv` before anything else.
  - An agent working from a brief reads only its brief and what the brief names, so that nothing in this plan steers its reading.
- **Nothing outside the working files governs.** The work done between G1 and the reset is history. It is outside the working files, at [commit `4923e1c`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf), and is reached only through a link pinned to a commit in a working file, saying what it is for.
- **The founder's messages.** The coordinator states its reading of each message at the top of its reply, so the founder can correct it. Only decisions go in `founder-decisions.tsv`. A question gets an answer, not a row.
- **Reports** at each milestone and planned pause (the founder, 24 October): what is settled, what is open, the decisions that are the founder's, and the cost.

## 10. Sources

- Boehm, B. (1988). A spiral model of software development and enhancement. *IEEE Computer* 21(5). Risk-driven sequencing; the riskiest part first.
- Cervantes, H., Kazman, R. (2016). *Designing Software Architectures: A Practical Approach.* Addison-Wesley. Attribute-Driven Design: options come from known design concepts.
- Calder, M., Kolberg, M., Magill, E., Reiff-Marganiec, S. (2003). Feature interaction: a critical review and considered forecast. *Computer Networks* 41(1). Interactions between subjects.
- Chen, L., Ali Babar, M., Nuseibeh, B. (2013). Characterizing architecturally significant requirements. *IEEE Software* 30(2). What makes a subject rank high.
- Clements, P., Northrop, L. (2001). *Software Product Lines: Practices and Patterns.* Addison-Wesley. Scoping as a core practice.
- Coplien, J., Hoffman, D., Weiss, D. (1998). Commonality and variability in software engineering. *IEEE Software* 15(6). The test form's analysis.
- Czarnecki, K., Helsen, S., Eisenecker, U. (2005). Staged configuration through specialization and multilevel configuration of feature models. *Software Process: Improvement and Practice* 10(2). Who binds a variant, and when.
- Fagan, M. (1976). Design and code inspections to reduce errors in program development. *IBM Systems Journal* 15(3). Inspection, used here on briefs.
- Fairbanks, G. (2010). *Just Enough Software Architecture: A Risk-Driven Approach.* Marshall & Brainerd. Effort in proportion to risk.
- Gotel, O., Finkelstein, A. (1994). An analysis of the requirements traceability problem. *First International Conference on Requirements Engineering.* Tracing each result to its source.
- IEEE 1012, Standard for System, Software, and Hardware Verification and Validation. Independent review.
- ISO/IEC/IEEE 15026-2:2022, Systems and software engineering, Assurance case. Claims, arguments and evidence: every claim a fact, a reading or an assumption.
- Kang, K., Cohen, S., Hess, J., Novak, W., Peterson, A. (1990). *Feature-Oriented Domain Analysis (FODA) Feasibility Study.* CMU/SEI-90-TR-21. Domain analysis from existing systems, which is what Q1 is.
- Kazman, R., Klein, M., Clements, P. (2000). *ATAM: Method for Architecture Evaluation.* CMU/SEI-2000-TR-004, Software Engineering Institute. Change scenarios that test whether an architecture's decisions hold as conditions change.
- Mill, J. S. (1843). *A System of Logic.* The methods of agreement and difference.
- Nygard, M. (2011). Documenting architecture decisions. Cognitect blog. The form of a decision item.
- OSHA, 29 CFR 1910.119(l), Management of change ([Cornell's Legal Information Institute](https://www.law.cornell.edu/cfr/text/29/1910.119), read 25 October 2026). Procedures to manage changes address "The technical basis for the proposed change" and its "Impact of change on safety and health" before any change. Applying it to a design method is the coordinator's reading.
- Parnas, D. (1972). On the criteria to be used in decomposing systems into modules. *Communications of the ACM* 15(12). Each decision likely to change behind its own module.
- Pohl, K., Böckle, G., van der Linden, F. (2005). *Software Product Line Engineering.* Springer. One platform, many products.
- Poppendieck, M., Poppendieck, T. (2003). *Lean Software Development: An Agile Toolkit.* Addison-Wesley. Deciding at the last responsible moment.
- Rahm, E., Bernstein, P. (2001). A survey of approaches to automatic schema matching. *VLDB Journal* 10(4). Why matching on names alone fails.
- Schmid, K. (2002). A comprehensive product line scoping approach and its validation. *ICSE 2002.* Scoping by what will be built.
- Svahnberg, M., van Gurp, J., Bosch, J. (2005). A taxonomy of variability realization techniques. *Software: Practice and Experience* 35(8). How a variation point is realized, by when it is bound.

## 11. Changes

A dated log. Where an entry differs from a later one, the later holds, and the sections above are the current text.

- **12 October 2026:** proposed by the coordinating session.
- **12 October 2026,** after the founder's questions: section 5 now says when the founder is needed, what a decision item looks like, how standing decisions work, and what spending covers.
- **12 October 2026:** the founder's go (G0).
- **12 October 2026,** method fixes within the plan, from inspecting the pilot's briefs. They are for the founder at G1:
  - The test form's step 3 takes its tags in a set order. `no difference` comes first, and `business model` has a defined test.
  - Step 5 adds "maturity or unknown, cheap to change: left to the build".
  - In step 5, a letter's row applies when any platform has that letter.
  - A source's kind (observed, shipped, stated, official page) is assigned by rule, in `method/source_kinds.py`.
  - When a question row must be answered is mapped from what follows, in `studies/subjects/S-01/briefs/E-rows.md`.
  - Causes compare variants whose scopes overlap.
  - Coexistence can be `unknown`.
  - `no difference` gives "a commonality, carried as the references carry it".
  - The four time-bomb types are decided by stated rules on the rows' `lane` and `needed_by`.
- **12 October 2026,** Q3 moves to close-out, by the coordinator's engineering decision. The founder delegated this decision, asking that it not rest on the rows merely existing.
  - **Why the rows are worth reconciling at all.** They are agent-written beliefs, already circulating, that would return as false requirements. That is the time bombs Q3 was agreed for.
  - **Why once, at close-out, and not per subject.** Read inside each subject, they would anchor the analysis. Reconciled once against a register built from evidence, they cost less and can't steer it.
  - **What changes.** The pilot drops its rows step. `briefs/E-rows.md` waits for Stage 5.
- **12 October 2026,** Stage 1's method, after its first run stopped at the axis cap having read 23 of 262 items:
  - every source is read before any axis is formed;
  - conditions are recorded first, and then grouped into axes;
  - the cap becomes a stop for review after grouping.
  `studies/yemen-cases/first-run-stopped/` keeps that first run as a record.
- **12 October 2026,** Stage 1's pass 2, before it runs, given pass 1's size (over 1,500 rows):
  - Its judgments are split from its rules. Agents group the rows into conditions and places, and label each row's state. `method/build_yemen_cases.py` applies the rules for axes, today and cases, and the checker compares its output.
  - A condition's states are alternatives: only one holds at a place and time.
  - A state's place is the scope its source gives it: an authority's area for a rule it sets, a party's service for what it says of its own, or a named area. Today's parts may overlap.
  - Only a state whose source says it holds in all of Yemen supersedes states at other places.
  - No source attests a state after the evidence was captured. A proposed state is never today and builds no case.
  - The review past 20 axes changes nothing itself: it may only return groups to step 2a, naming the rule each breaks.
- **13 October 2026,** agents' effort by step, delegated by the founder. On Anthropic's guidance, research work loses little at `medium`, intelligence-sensitive work needs at least `high`, and failures can be re-run higher.
  - `max`: inspections of a method; Stage 1's step 2a; the pilot's B, C and D; review F.
  - `high`: Stage 1's step 2b, labelling states.
  - `medium`: reading and recording evidence (phase A, A2 and similar), where the checker verifies every quote. A part whose check or review shows gaps is re-run at `high`.
  - `low`: one-off mechanical questions.
- **13 October 2026,** claims of absence, after the founder found held Salla articles on settlement in Kuwait and the UAE that phase A and A2 had recorded as missing:
  - A new pilot step, A3, has an agent that made none of the claims audit every gap and absence.
  - A "searched, not found" must show the corpus search behind it: `method/corpus_search.py`, run in every language the platform uses, and by each country, plan and arrangement it names.
  - The checker enforces both.
- **17 October 2026,** Stage 1's axes review, after step 2b. Of 253 axes, 128 groups go back to step 2a. Most break rule 2: their states add up rather than replace each other, so the build's latest state drops facts that still hold. Bans and designations that each name only the parties they add are the clearest case. Two rulings follow from rule 2, and are added to the brief:
  - lists that grow, instruments in force together, and parts of one source: each addition, instrument or fact is its own condition;
  - rows that state one thing at different detail share one label, with the rest in `note`.

  The record is `studies/yemen-cases/review-axes.md`. It names an `axes.tsv` in full only when the review lets it through.
- **17 October 2026,** the pilot's phase C, after its first run. Its rule for "same" named the merchant as one party everywhere, but each platform's name as a different party. So two platforms that each name themselves "differed", and 14 of 23 variation points read as vendor choice, 12 of them founder decisions. Two changes follow, both marked in `briefs/C-analysis.md` as the coordinator's own:
  - the parties to the subject are one party on every platform: the merchant, the buyer, and the platform itself (its name, its payment product, its company);
  - "names a law" means a particular law, or a particular regulator with its rule. Generic legal wording doesn't count.

  Phase C re-applies steps 3 to 5. Its first run stays in git history, at commit `34a32b9`.
- **17 October 2026,** the pilot's phase D, at its first checkpoint. No Stage 1 id says where the merchant is, so a variant whose condition names only countries ("merchants in Saudi Arabia", "outside the Kingdom") could never be shown to fail, and `no placement` could never be given on 22 variation points. Every case shares Q2's frame: the merchant sells in the Yemeni market. A condition naming only countries or regions is checked against that frame, cited as `Q2`. This is marked in `briefs/D-yemen-marks.md` as the coordinator's own, and the checker accepts `Q2` as case evidence.
- **17 October 2026,** Stage 1, after its independent review found errors in `today` on 12 of 45 sampled axes. Before Stage 4:
  - a `within` relation between places, each link on a source, so that a strictly later state supersedes the states at places inside its own;
  - a faithfulness pass over every axis.

  Until then, for the pilot, the axes S-01 bears on are checked against their quotes before phase D marks on, and phase D reads each part of `today` with its date.
- **17 October 2026,** the pilot's independent review (`studies/subjects/S-01/review.md`) found 14 must-fix items. Two rulings follow, each marked in its brief as the coordinator's own:
  - **`answers` in phase B rests on what a statement says, not on shared words.** Its own words must name the party or thing that takes the variation point's role in the subject's flow, and `basis_evidence` says which role. This is what matching basis 4 above exists for: "matching on names alone fails on synonyms". Rule 0's "same" governs comparing answers between platforms. Variants that name something outside the flow, such as a wallet for buying the platform's services, are re-placed. The role test holds whatever a variant's basis, since shared words can be homonyms.
  - **A bullet (d) variant that says a party has no part names no one filling X,** so it doesn't break phase C's test 1.

  The other must-fix items are corrections under the rules as they stand: phase B's misplaced variants, phase C's VP-08, the source-kinds rules, Stage 1's YA-102 and YA-105, and the register entry.
- **17 October 2026,** the pilot's phase C, after its third run raised two questions (`studies/subjects/S-01/notes-c.md`, problems 6 and 15). Two rulings follow, each marked in `briefs/C-analysis.md` as the coordinator's own:
  - **A statement that a party has no part in X** names no one filling X, whatever bullet phase A gave it, so it doesn't break test 1. It does show that the party isn't in its platform's set, so that platform's gap can't hold it. Where another platform names the same party as filling X, the two differ. Phase A filed some such statements under bullet (a), such as BigCommerce's "No agency ... relationship is created" (S01-BC-128).
  - **A platform may carry more than one coexistence letter,** joined by `+`, where its statements show more than one way: some variants together in one store, others bound per market. The review found binding per market on four variation points that one letter per platform couldn't carry (`review.md`, finding 5). Each letter's row in step 5 then applies, as before.

  Phase C re-applies steps 3 to 5 under both. Phase B's rows don't change.
- **17 October 2026,** recorded after the independent review's re-check (`studies/subjects/S-01/review.md`, finding 37). The coordinator gave phase B this ruling the same day, with the role test, and it is now marked in `briefs/B-variation-points.md`:
  - the subject's flow ends at the payout to the merchant's own bank account;
  - a wallet is in the flow when its own words say it holds the merchant's sales proceeds before that payout. Where the wallet itself is the answer, the statement must say so. One whose words say only that it holds top-ups for the platform's services is outside it;
  - a time, condition, fee or deduction acting on an in-flow wallet's funds answers as usual.
- **18 to 25 October 2026: history.**
  - **The re-frame:** at G1 the founder chose a re-frame (18 October).
  - **A new method:** on 24 October a new method replaced this plan, and gained three amendments that day.
  - **The reset:** on 25 October the founder reset the work to this plan.

  That work, and every decision made on it, is outside the working files, at [commit `4923e1c`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/4923e1c96a0296abdaf3f5bdbd8c155e09acfebf) (`HISTORY.md`). What it found that holds is carried as facts:
  - Stage 1's corrections (`studies/yemen-cases/corrections.md`);
  - the facts on Decision 1's page (`studies/subjects/S-01/decision-1.md`);
  - the pilot's cost, corrected on 18 October (its method report, section 12);
  - six scripts' improvements, re-run against the G1 results (`reports/reset.md`).
- **25 October 2026, the reset,** with the founder's go. Each change is made in its section:
  - **Section 1:** the design of the first version is for many markets, and production code waits for requirements, an architecture description and engineering documentation (the founder, 24 October). This replaces "a thin slice for Yemen". The guard on the first market is named, from the founder's message of 24 October.
  - **Section 3:** the founder's guard on sellers' money; plain words; reviews that try to refute and look for what an entry never cites.
  - **Section 4, Stages 0 to 2:** marked done.
  - **Section 4, Stage 3:** concerns no longer reach the subject list through Yemen's axes. The market enters after the analysis (section 1; the pilot's analysis reached its line for Decision 1 from the references).
  - **Section 4, Stage 4:** one subject at a time, with the pilot's proposals 1 to 7. The pilot's open items, and what the checker now reports on it, are ruled first. Shopify and Salla are read first and in full, and the others from what is recorded (the founder, 24 October).
  - **Section 5:** G3 comes after each subject.
  - **Section 4, Stage 5:** the areas list as a cross-check only.
  - **Section 6:** decisions before variation points; options beyond the references; every claim a fact, a reading or an assumption; evidence looked up through its guides; merchants never asked.
  - **Section 7:** risks 14 to 16.
  - **Section 8:** a subject's budget plus a quarter.
  - **Section 9:** changes made in place and listed with what they remove; the frame defined; history outside the working files; the founder's messages; reports.

  **What this change removes or weakens,** with the risk each part controlled:
  - **"A thin slice for Yemen"** risked a design shaped by one market. Now replaced: designed for many markets, Yemen first.
  - **Stage 3's Yemen-axis candidates** covered concerns only the market raises. Reassigned: concerns the platforms scope by country or region still enter, and phase D's product gaps catch what only Yemen raises.
  - **Batches of three to five subjects** spread the founder's decisions over fewer gates. Reassigned: each subject's report carries only the decisions that are the founder's.
  - **Stage 1's faithfulness pass over every axis before Stage 4** guarded every axis. Weakened to the axes each subject bears on, before its phase D. Accepted: an axis no subject bears on binds nothing.
  - **All five references read alike** guarded against taking one market's pattern for a rule. Weakened: Zid, WooCommerce and BigCommerce come from what is recorded, and are read further where a cause needs them, so every cause still compares all five.
- **25 October 2026, after the reset's two cold-start tests:** wording made consistent with the founder's decisions, the checkers named, and history's links defined as pinned links in any working file. Two decisions of the founder's of 24 October that the reset had dropped without saying so are carried, since they hold: the guard on the first market (section 1) and Shopify and Salla first (Stage 4). "Buying architectural intelligence" is attributed to the founder (section 6). The pilot's lessons it hadn't carried are added (Stage 4).
- **25 October 2026, Yemen's scenarios cut,** with the founder's go, on the pilot's evidence. Its 183 Yemen marks, against 30 scenarios, moved no result ([its method report, section 8](studies/subjects/S-01/method-report.md#8-phase-d-marking-the-subject-in-yemens-cases)). Stage 1 cost about 1.5 billion tokens ([section 12](studies/subjects/S-01/method-report.md#12-what-a-subject-costs)), and Decision 1 used 15 of its 743 axes and constants. Changed: the safe shore's item 2 and the guard (section 1), Q2's marks (section 2), Stage 1's note and Stage 4 (section 4), the decision item (section 5), the test form's steps 5 and 6 (section 6), and risk 10 (section 7).

  **What this change removes or weakens,** with the risk each part controlled:
  - **Marking every subject against every Yemen scenario** showed, before it happened, whether a change in Yemen would rule an option in or out. Accepted: options stay switchable per market, so such a change is a setting, not a redesign. A scenario is still used where a decision depends on a condition that is changing.
  - **Stage 1's `within` relation and faithfulness pass before each subject** guarded every axis a subject bore on. Replaced: each fact is checked against its quote when a Yemen row uses it.
  - **The pilot's open item on variants with no stated condition** existed only because phase D had to show each variant fail. Removed with phase D's marks.
- **26 October 2026, after the orientation page,** with the founder's answers (`founder-decisions.tsv`): G2, evidence for all ten subjects; Decision 1's follow-ons, E1 and E2 kept, and default 2's "never" at launch; no test of Decision 1 against Shopify alone; the founder's G1 intent stays in history. Changed:
  - **Section 6:** the scenario walk becomes the test form's step 7, on the founder's proposal. It restores the change scenarios of the method of 24 October (history), without its outcome types: the walk tests the same thing, whether one market's facts shape what is built, more directly. Stage 4 and the decision item (section 5) name it, and section 10 adds its source.
  - **Stage 2's note** is brought up to date.

  **What this change removes or weakens:** nothing. It adds one step per subject, made by reasoning over the subject's own evidence, with no new reading.
