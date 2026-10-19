# Plan: from the evidence to the decisions that are expensive to change

**Status: agreed by the founder on 12 October 2026 (gate G0), and re-framed after G1 with the founder's go of 18 October 2026 (section 11).** `STATE.md` says where the work is.

The coordinating session wrote this plan after the founder asked who would manage the work until it reaches a safe shore, with the right engineering, sequence and framing, leaving the founder only what is genuinely theirs to decide. At G1 the founder re-framed it: the work now ends with proposals the founder accepts or changes (section 1). Where a rule comes from known practice, it names its source, and section 10 lists the sources. A rule without a source is the coordinator's own.

## 1. The aim and the end

Sharrwah is one platform for many markets. Yemen is its first market, not its design target. Before building, the decisions that would be expensive to change later have to be made on evidence. Everything else is decided while building, where it is cheap to change.

**The aim.** For each item of the founder's intent (`founder-messages/2026-10-18-g1-answer.md`, section B), the best of what the five platforms do, framed as Sharrwah's proposed model:
- what it is called, how it is structured and how it behaves;
- what can plug in, what is set per what, and who sets it;
- how the design divides into parts that can be built in order;
- where the founder's item says something is decided later, what the design must keep open instead.

That should be enough to start the design of the first build.

**The principles stay:**
- **One platform, many markets.** The platform is built once and each market is set up on it: product line engineering (Pohl, Böckle & van der Linden 2005).
- **Hide what is likely to change.** Each decision likely to change sits behind its own module (Parnas 1972).
- **Effort follows risk.** Analysis effort goes where a wrong decision costs most (Fairbanks 2010; Boehm 1988), and each decision is taken at the last responsible moment (Poppendieck & Poppendieck 2003).

**The end.** The work ends when the founder has accepted or changed every proposal. Then the design of the first build starts, under its own plan.
- **It starts from the areas list, with the founder's marks, as Sharrwah's whole extent.** What the first build covers within it is for that plan.
- **It reads open-source commerce platforms,** such as Saleor, Medusa and Vendure, for how each part is structured. Never as evidence of what sellers get.
- Anything the accepted proposals leave open comes to the founder during that design, when it is needed. How far currencies can be set or changed is one such item.
- No proposal rests on a derived document, or on the founder's words taken as evidence of what a platform does.

## 2. What changes from the run so far

- **The pilot is done.** Its entry (`studies/subjects/S-01/entry.md`) let the founder decide.
  - Its Decisions 1 to 14 are deferred. They stay open, and bind nothing, not even per market. They come back as proposals once the work has framed them: Decisions 1 to 13 with question 5, and Decision 14 with question 7.
  - Its files are the coordinator's to use. Its 23 variation points, and its open review findings (among them 29 and 36), feed the money proposals.
- **The guard** (`founder-decisions.tsv`, G1). No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision. That covers Sharrwah itself holding it (the entry's option A), and a payment company holding it in an account opened through Sharrwah (option B). It limits only what goes live. It neither requires a proposal to provide for either arrangement nor rules one out.
- **Questions, not subjects.** Section B's items, in neutral words (`studies/proposals/questions.md`), are what the work answers. They are not subjects, and don't take the test form. Section B's items are not standing decisions under section 5. A proposal that answers one becomes a decision only when the founder accepts it.
- **What is recorded is reused:**
  - the concern map's `concerns.tsv` and `statements.tsv` for all five platforms, in every placement, but not the first runs' `placements.tsv`;
  - the pilot's files;
  - Stage 1's output.

  For each question and platform, a script copies, unchanged and with their citations, the statements under the concerns of the areas the question draws on (step R1). A gap recorded under a copied concern comes with it, as what was not found then.
- **The 88 matches and the 84 retired unclear matches** from the concern map's first runs aren't used. Merging the platforms' areas rests on their own names, or is marked as the coordinator's own.
- **New reading is allowed** where what is held doesn't show what a question needs. This replaces Stage 0's freeze. A page read new is captured and committed before it is cited (section 9).
- **The count of tokens is corrected** (section 11, 18 October). This plan's figures are in the corrected count.

## 3. Who does what

**The founder decides what is genuinely theirs:**
1. **Scope:** what Sharrwah will and won't be, its business model, and which markets come after Yemen. This includes the marks on the areas list.
2. **Company and legal questions:** legal entities, licences, whether Sharrwah holds funds, and partners. Where law is involved, these are decided with a lawyer.
3. **Building ahead:** how far to build for markets not yet planned.
4. **Spending:** stores on paid plans and consultations.
5. **What only the founder can do:**
   - capturing from inside Yemen, or by signing up to a platform;
   - journeys in real stores;
   - contacting platforms, partners and regulators;
   - attestations.
6. **Every proposal for section B,** accepted or changed.
7. **Whether any arrangement that holds sellers' money through Sharrwah goes live.**
8. **Changes to this plan's frame,** and what to cut when the re-sized plan would pass its budget.
9. **The gates** in section 5.

**Nothing reaches the founder without a decision attached.** Each item comes with its evidence, its options and the coordinator's recommendation, marked as such. Section 5 says when each is needed and what an item looks like. Everything that reaches the founder:
- **is in plain business words.** A term that can't be avoided is defined in one line. Quotes and ids stay in the files;
- **may carry several decisions in one message,** each standing on its own, with its own answer line;
- **lists the method rulings made since the last message,** each in one plain line saying what it changes. The founder may overturn any.

**Not the founder's to settle.** These follow from evidence and rule, or are the coordinator's engineering calls. The founder may challenge any of them.
- what a platform states, and whether two platforms' concepts match (section 6);
- whether a page is held, and each gap's kind and route;
- what follows from a result by engineering rule;
- the recommendation in each proposal;
- sequencing, briefs, and fixes to the method within this plan.

**The coordinating session (Claude Code).** It:
- frames each step and writes the briefs;
- runs the agents and checks;
- integrates the results, and finishes each proposal;
- keeps this plan and `STATE.md`;
- brings the gates.

It never takes the founder's decisions, and never treats the founder's words as evidence of what a platform does.

**Agents.** Each gets one short task from a written brief (the method report's proposal 3), and scripts do the mechanical work.
- **Before a brief runs,** a separate agent checks it for anything that presupposes the answer, for whether it can work, and for what it will cost (inspection: Fagan 1976).
- **Before a result reaches the founder,** an agent that did none of the work reviews it against its sources (independent verification: IEEE 1012).

**The checker,** `method/check_proposals.py`, is built from the pilot's checker before step R2. It enforces mechanically:
- quotes are verbatim, at a commit;
- a statement a script copied is unchanged, with its citation;
- each record is tied to a question;
- each fact a proposal cites is tied to a statement or a Stage 1 id;
- a "not in what was read" lists what was read, with the corpus search behind it;
- an absence rests on a complete list;
- a page read new is committed before it is cited.

**Counting.** `method/count_tokens.py` counts each run's tokens from its transcript, each API request once: input, output, cache reads and cache writes. Each run's count goes into `studies/proposals/costs.tsv`.

## 4. The sequence

Stages 0, 1 and 2 are done. Their text stays below as a record, unchanged. Stages 3 to 5 are replaced by steps R0 to R6. Before each step, `STATE.md` records its expected cost (`studies/proposals/sizing.md`). After it, it records the measured cost.

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
3. Write its decision-register entry.
4. Have it reviewed independently.
5. Write a method report: what broke and what changed.

**Done when** there is one register entry the founder can decide from, or a clear account of why not.

**Gate G1.** Does the entry let the founder decide? If so, the founder chooses to scale up, change the method, or re-frame.

**Kill rule.** If the entry lets the founder decide nothing, or the errors come from the method again rather than the evidence, nothing scales until the frame has been re-examined.

### Step R0. The plan change

1. This change, the first step's briefs and scripts, and the neutral wording of each question are drafted.
2. An agent that did none of the drafting checks them against the founder's G1 answer and the recorded data, for whether they can work and what they will cost.
3. The coordinator fixes what it finds, and the same agent checks the fixes.
4. The founder gets a plain summary. Nothing else runs before the founder's go.
5. The founder's go, of 18 October 2026, with five changes of the founder's, made in this text.

### Step R1. The platforms' broad areas, then gate G2

1. **A script** (`method/areas_extract.py`) extracts each platform's own organizing lists from all that is recorded:
   - the concern map's inventory lists, and its concerns, with what their statements show by country, plan and arrangement;
   - Shopify's Help Center menus;
   - Salla's help-centre categories.

   So legal, place and eligibility matters show too, not one menu only.
2. **One short run per platform** (`briefs/R1-areas-one-platform.md`) names the platform's broad areas in its own names, each with a plain line, and places each concern under one. A script (`method/place_entries.py`) places each inventory entry under the area of its concerns, and `method/check_areas.py` checks the names and the placing.
3. **The coordinator merges the five lists into tens of areas.**
   - Where the platforms' own names can't bring the list down to tens, the coordinator groups further, and marks each such grouping as its own.
   - It ties each area to the questions that draw on it. For each question, a script later copies the statements under those areas' concerns (step R3).
   - For each area, it says what a "won't do" mark removes from the work, and what evidence the questions keep anyway.
   - For each area no question draws on, it writes one line saying why the work leaves it out. This replaces Stage 5's last sweep.
   - For each question, it picks which platforms to read in depth and which only to check for anything that differs from or goes beyond them, each with why and what that rests on. Every platform is read for every question, in depth or as a check.
   - It picks the sample (step R2).

   Its files are `areas.tsv`, `areas.md` and `depth.tsv`, as `briefs/R1-areas-review.md` describes them.
4. **An independent review** (`briefs/R1-areas-review.md`), with its re-checks, then the founder.
5. **Gate G2.** The founder marks what Sharrwah won't do and what it must.
   - **"Won't do"** removes the area from the work, except the evidence the questions keep.
   - **"Must do"** confirms the area is in Sharrwah's scope. Where no question draws on a "must do" area, the coordinator brings the founder what reading it would need, and its cost, for the founder to decide.
   - **Anything unmarked** stays in.

### Step R2. The sample

1. **Built first:**
   - `method/copy_statements.py`, which makes the copies for each question and platform;
   - `method/check_proposals.py`.
2. **The recording brief and the checking brief** are each checked before they run.
3. **The sample** is one of the in-depth runs step R3 will make: one question on one platform. It is chosen after the depth choice, by a stated rule: of the in-depth runs, the one whose copied statements are nearest the median. It runs while the founder marks the areas, since the marks can't remove a question.
4. **What is measured:** the run's tokens, by its transcript, over the statements it records that a script didn't copy.
5. **For comparison,** the pilot's phases A and A2 cost 0.52 million per statement, or 0.75 million per statement not taken from the concern map.
6. **Whatever it shows, the work goes on.** The steps that record or audit statements are re-sized from the measurement, and the others as before. The work stops and comes to the founder only if the re-sized whole would pass the budget (section 8).

### Step R3. Recording, by question

- **Depth by question.** For each question, the platforms chosen with the areas list are read in depth. The others are checked only for anything that differs or goes beyond.
- **A script copies first, in two phases** (`method/copy_statements.py`):
  - it lists as candidates the concerns of the areas the question draws on;
  - the run marks each candidate as bearing on the question or not, gives its reason for each set aside, and may add concerns from other areas (`selection.tsv`);
  - the script then copies the chosen concerns' statements, gaps and citations, unchanged.

  The run then reads only what is still needed: held material first, starting from the platform's own organization of its help where it is held, then the corpus search; new material only where what is held doesn't show it.
- **Each run is short:** one question on one platform.
- **An in-depth run records:**
  - each statement in the platform's own words and terms, scoped as its source scopes it;
  - where they bear on the question, the platform's own structure (the things it names, and the levels its settings are set at) and the contracts behind its providers, including agreements its terms incorporate. This is how depth reaches the data model and the partner contracts;
  - what it doesn't find, as "not in what was read", listing what it read. It records something as absent only from a complete list the platform publishes.
- **A checking run** reads the in-depth runs' accounts for the question and its own platform's copies, and records only what differs from them or goes beyond them.
- **Each run ends with a short account** of what its platform shows for the question, in the platform's own terms. Each point cites statement ids, and the account adds no claim of its own.
- **What shows only by signing up** to a platform goes on the founder's capture list. The list reaches the founder when recording ends, so that anything captured can still feed the proposals. Capturing is optional, and the work doesn't wait for it.
- **Depth goes where a wrong guess would be expensive to change after launch:** money flows, legal structure, the data model, and partner contracts. Every question gets enough to propose from.

### Step R4. The proposals

- **One drafting run per question** (its brief checked first). It reads:
  - the question's accounts, and the records it cites;
  - the areas list, with the founder's marks;
  - a digest of Stage 1's axes and constants, made by script;
  - for question 5, the pilot's entry and records: its 23 variation points, its open review findings, and Decisions 1 to 13;
  - for question 7, the pilot's Decision 14.
- **Each draft gives:**
  - how the platforms handle it, in their own terms;
  - Sharrwah's proposed names, structure and behaviour;
  - what can plug in, what is set per what, and who sets it;
  - how it divides into parts that can be built in order;
  - what the design must keep open;
  - what Yemen's evidence allows, forbids or doesn't show, each Yemen fact read with its date under section 6's Yemen rules;
  - the company decisions it raises.
- **The coordinator finishes each proposal** and owns its recommendation.
- **The money proposals** (questions 4 and 5) say what the design provides for, under the founder's guard.
- **Company decisions.** One short run gathers, from the drafts and their records, the evidence bearing on each company decision: where the company is based, which providers and partners Sharrwah works with, any licence, who may register, and any others found. The coordinator writes each in plain words, with a recommendation and whether it needs a lawyer.

### Step R5. Checks by risk

Once a proposal or company decision is drafted, and before its review, with each brief checked first, everything it cites gets the full checks:
- **Each fact it cites** is re-checked against its source.
- **Anything it cites as not found, or recorded absent,** gets the corpus search, and an audit by an agent that made none of the claims, batched by platform.
- **Each Yemen fact it uses** is re-checked against its quotes, including whether a later state covers the same place or a place that contains it.
- **A "Yemen's evidence doesn't show" it cites** gets the search and audit too.
- **Every quote is checked by script.**
- **What no proposal cites** is recorded as read, without audits.

### Step R6. Independent review, then the founder

- **An agent that did none of the work reviews the proposals,** in two batches of four, with the company decisions in the second, and re-checks the fixes.
- **One short run checks how the proposals bear on each other,** for bindings that conflict: such as currency, payment methods, payouts, what must be met before taking payment, and the guard (Calder et al. 2003). This replaces Stage 5's check of interactions.
- **One short run checks Q3's rows** against the reviewed proposals (section 6). Its list comes with them.
- **Then the founder** gets the proposals and the company decisions, several in one message, each with its own answer line, with the method rulings made since the last message, and the rows of Q3's lists the proposals don't answer.

## 5. The gates

| Gate | When | What the founder decides |
| --- | --- | --- |
| G0 | 12 October 2026, done | The plan |
| G1 | 18 October 2026, done | Re-frame, with the decisions in `founder-decisions.tsv` |
| The go on the change | 18 October 2026, done | The plan change, with five changes; Q3's rows checked at the end; no cuts |
| G2 | After step R1 | The areas: what Sharrwah won't do, and what it must |
| The proposals | After step R6 | Each proposal, accepted or changed, and the company decisions |

The proposals replace G3 and G4. The work ends when every proposal is accepted or changed.

**When the founder is needed:**
- **At G2:** the marks on the areas list.
- **After recording:** the capture list, which is optional.
- **At the proposals:** each proposal, and the company decisions, with the rows of Q3's lists the proposals don't answer.
- **Between these, only when work stops** under section 8. A step that ran past its expected cost is told in the next message, with the re-sized whole.

**What a decision item looks like** (the coordinator's own form, after the architecture decision record: Nygard 2011), in plain words:
- the question in one line, and why it is the founder's;
- what the platforms do;
- what Yemen's evidence allows, forbids or doesn't show;
- the options, each with what it needs built and what it needs from outside, such as a licence, a partner or money;
- the coordinator's recommendation, and its reason;
- for a company decision, whether it needs a lawyer;
- the answer line.

**Defer** is always allowed.
- For the pilot's Decisions 1 to 14, it means the decision stays open and binds nothing, by the founder's G1 answer.
- For later items, the coordinator reads it the same way, unless the founder says otherwise.

**Standing decisions.** The founder can state a decision once as a rule that settles every later item of its kind, such as a default business model.
- It is recorded in `founder-decisions.tsv` like any decision.
- Items it settles don't reach the founder. Each settled item names the rule that settled it.

**Spending** means money paid for evidence or advice the work needs: a store on a paid plan, a lawyer's or accountant's consultation, or an official record.
- Each request says what it buys, which decision depends on it, the cost if known, and what happens without it: the item stays unknown or open.
- Building and running Sharrwah are not part of this plan.

**The founder's decisions** go in `founder-decisions.tsv`: the date, the gate, the question, the decision, and the evidence it rested on.

## 6. The rules this plan adopts

These rules are settled, each from the source named. The founder may challenge any.

### Recording

- **Questions, not categories.** Agents get section B's items only as the neutral questions in `studies/proposals/questions-for-agents.md`. A script writes it from `studies/proposals/questions.md`, leaving out the founder's items and expectations.
- **The platforms' own words.** Agents record what each platform says and does in its own words and terms. The founder's working words never become the names or categories they record under. The rule against our own category names (Q1, 11 October, rule 1; the pilot's A brief, rule 1) holds for everything agents record.
- **No level or setter fixed in advance.** Nothing fixes where something is set or decided, or who sets it. "Per market" in the founder's section B is a working description, not a fixed level.
- **All that is recorded, not only menus:** how the platforms organize their products, and also their terms, country rules, eligibility and availability.

### Evidence

- **Statements stay verbatim,** cited at a pinned commit. A script checks every quote.
- **Kinds of source** are assigned by rule (`method/source_kinds.py`): observed, a recorded store or journey; shipped, code or a schema the platform ships; stated, its docs or help centre; official page, its terms, pricing or legal pages. Kinds are compared like with like.
- **"Not in what was read" and "absent".** What a run doesn't find is recorded as "not in what was read", with what it read and the corpus search behind it (`method/corpus_search.py`), in every language the platform uses and by each country, plan and arrangement it names. Something is recorded as absent only from a complete list the platform publishes, such as an enumerated schema or a full plan table.
- **Before a gap goes to anyone,** its route is checked against what is held:
  - if the page is held and readable, it is read;
  - if it is held but not readable, the reader is extended;
  - only what isn't held goes to the founder, with what exactly to capture and why.
- **A page read new** is captured and committed before it is cited.
- **Incorporated agreements.** An agreement that a platform's terms incorporate, such as Stripe's Connected Account Agreement under WooPayments and Shopify Payments, is part of that platform's terms, and may be read.
- **The founder's words** are never evidence of what a platform does. The founder's decisions are recorded as decisions.

### Checks by risk

- **Everything a proposal cites** gets the full checks, by the founder's choice at the go: a re-check against its source, and, for anything not found or recorded absent, the search and audit.
- **What no proposal cites** is recorded as read, without audits.

### Comparing platforms

When a proposal compares platforms, two concepts match only on one of four bases, each shown in the platforms' own words:
1. the same term, including a platform's own translation of it;
2. the same identifiers: a key, scope, topic or entitlement;
3. the same definition, with both quoted;
4. both fill the same role in what a question asks, each by its own words (the role test). This replaces "both answer the same variation point", since there are no variation points now, and is the coordinator's own.

Matching on names alone fails on synonyms and homonyms (Rahm & Bernstein 2001), which is why bases 3 and 4 exist. A partial overlap is recorded as such. Two more rules hold:
- **one party on every platform:** the merchant, the buyer, and the platform itself (its name, its payment product, its company);
- **"no part":** a statement that a party has no part names no one filling the role, but shows that party isn't in its platform's set.

### Money

- **The flow ends** at the payout to the merchant's own bank account.
- **A wallet is in the flow** when its own words say it holds the merchant's sales proceeds before that payout. Where the wallet itself is the answer, the statement must say so. One whose words say only that it holds top-ups for the platform's services is outside it.
- **A time, condition, fee or deduction** acting on an in-flow wallet's funds answers as usual.

### Yemen

- **Each proposal records** what Yemen's evidence allows, forbids or doesn't show, from Stage 1.
- **Stage 1's rules for reading a state hold:**
  - a condition's states are alternatives: only one holds at a place and time;
  - a state's place is the scope its source gives it;
  - only a state whose source says it holds in all of Yemen supersedes states at other places;
  - a proposed state is never today;
  - each part of today is read with its date.
- **Q2's frame holds:** the merchant sells in the Yemeni market. A platform's condition naming only countries or regions is checked against it.
- **Each Yemen fact a proposal uses is re-checked against its quotes,** including whether a later state covers the same place or a place that contains it.
- **This replaces the faithfulness pass over every axis, and Stage 1's `within` relation, which is not built.**
  - The `within` relation addressed a stale state taken as today's, at a place a later state covers.
  - Each fact's re-check now catches that, for the facts the work uses.
- **Stage 1's other open items are done only if a proposal uses them:** the review's "can follow" items, such as the internet shutdowns, and its two minor items.
- **Other markets** wait until the founder decides to enter them.

### Q3's rows

Both sets, by the founder's choice at G0: the 81 payment rows and the Knowledge Map's 179 questions (`register/README.md`). They are checked once, at the end, by the founder's choice at the go.
- **Why.** They are agent-written beliefs that might return as false requirements, and the founder said at G0 that some may be genuine questions. Nothing else in this plan reads them, so they can't steer the work.
- **How.** After the review (step R6), one short run, from its own checked brief, places each row against the reviewed proposals. It lists the rows the proposals don't answer, and the rows that state as a requirement something the proposals' evidence contradicts. It reads each row only for its `id`, `question`, `needed_by` and `lane`.
- **What comes of it.** Its list reaches the founder with the proposals. A row never adds to a proposal by itself: the founder decides what an unanswered row needs.
- **They stay in `register/`.**

## 7. Risks, and what happens when one shows

| # | Risk | How it shows | What happens |
| --- | --- | --- | --- |
| 1 | The work grows past what the proposals need | A record tied to no question; a step past its expected cost | The checker rejects untied records. A step past its expected cost re-sizes the rest, and the founder hears of it in the next message. The work stops only when the re-sized whole would pass the budget |
| 2 | A word of ours, or the founder's, makes the result, as our category names, the matching example and the salla.com rule did | A brief or question uses a working word as a category; an agent records under it | Questions and briefs are checked before they run. The independent review looks for it. Each error is traced to its cause, and everything it touched is re-run |
| 3 | Evidence we hold goes unread | A gap's route is held | The gap can't go to the founder; the reader is extended |
| 4 | A search claims more than it read | A "not in what was read" without its list and search | The checker rejects it |
| 5 | Depth differs by platform: accounts for Shopify and Salla, declarations for Zid and BigCommerce, code for WooCommerce | A proposal resting on absence at a weaker kind of evidence | Absence counts only from a complete list. Otherwise the proposal says "not in what was read" |
| 6 | The same word names different things, or different words name the same thing | A comparison on none of the four bases | No match. It is recorded, and it matters only if a proposal depends on it |
| 7 | Evidence changes mid-work: the founder's new commits, or a platform changes a page | New commits touch cited paths | The records and proposals whose citations changed are listed, and only those re-run |
| 8 | A session loses its context, the container resets, or a usage limit cuts a step | Designed for in advance | Every run resumes from the repository. `STATE.md` is updated at every checkpoint, with a commit per run |
| 9 | The founder becomes the bottleneck | An item reaches the founder with no decision attached | It doesn't reach them. Each message brings only decisions, each with a recommendation |
| 10 | Yemen evidence is thin, or only reachable from inside Yemen | A proposal needs a Yemen fact no source gives | "Yemen's evidence doesn't show", not an inference. The capture list says what would show it |
| 11 | A reading of terms becomes legal advice | A statement taken as what Sharrwah must do | Quotes only. Sharrwah's legal position is a company decision, for the founder with a lawyer |
| 12 | An agent misreads: the quote is right but the meaning wrong | The independent review disagrees | The source is re-read, and the disagreement is recorded |
| 13 | The frame is wrong | The proposals let the founder decide nothing | The frame is re-examined, with evidence. This was met at G1 |
| 14 | Old documents return as evidence | A citation to a derived or excluded path | The checker rejects it |
| 15 | Statements a script copied carry an old error | A copy fails its quote check, or the review finds it wrong | Copies are checked like new ones. Everything a proposal cites gets the full checks |
| 16 | Depth by question misses a platform's different answer | A checked platform shows something the in-depth platforms don't | Checking runs record what differs or goes beyond. The review checks each depth choice against the records |
| 17 | The budget doesn't fit | The re-sized whole would pass 2 billion agent tokens | The work stops and comes to the founder, with what it would cut, and the founder decides |
| 18 | A count of cost is wrong, as the pilot's first count was | A run's count disagrees with its transcript checked by hand | A script counts each run. At R2, the coordinator checks the sample's count by hand |

## 8. When work stops and comes to the founder

- **An error touches results already delivered.** It is measured and reported, then fixed.
- **The re-sized whole would pass the budget,** 2 billion agent tokens.
  - When a step runs past its expected cost, it doesn't stop. The coordinator re-sizes the rest, and tells the founder in its next message.
  - The work stops and comes to the founder only when the re-sized whole would pass the budget. The coordinator then says what it would cut, and the founder decides.
  - This replaces the stop for a stage that overruns its size twice.
- **A decision that is genuinely the founder's blocks the next step,** or a proposal.
- **New evidence changes more than one finished proposal,** or the records of more than one question.
- **Something needs money, contact with a third party, or a legal judgment.**

## 9. Keeping it coherent across sessions

- **How this plan changes.** Only by a dated entry in section 11, with the reason and the source.
  - A change to the frame needs the founder's go.
  - A fix to the method within this plan is recorded, and listed the next time work comes back to the founder.
- **`STATE.md` says where the work is:** the step, the runs going and done, the next step, the open gate, and each step's expected and measured cost. It is updated and committed at every checkpoint.
- **Every run ends with a commit.** Every step can resume from the repository alone.
- **Every result traces back** through proposal, question and record to a statement or a Stage 1 fact, and from there to a source at a commit (Gotel & Finkelstein 1994).
- **The new work's files live in `studies/proposals/`:**
  - `questions.md` and `briefs/`;
  - `areas/`: the extracts, the platforms' areas, the merged list, the depth choice and its review;
  - `records/<question>/<platform>/`: the copies, `selection.tsv`, the statements recorded, what wasn't found, and the run's account;
  - `sample/`: the sample's measurement;
  - `drafts/`, `checks/` and `review/`;
  - `company-decisions.md` and `capture-list.md`;
  - `costs.tsv`: each run's measured cost.
- **Pages read new** are captured with the repository's capture tool into `evidence/product-class/runs/<time>-proposals-<question>-<platform>/`, and committed before they are cited.
- **How the kept checks run on these files:**
  - verbatim quotes: `method/check_proposals.py`, on every record and draft;
  - the search and audit: R5's runs, on what each proposal cites;
  - each brief's check: a separate agent, before the brief runs;
  - the independent review: R1's review of the areas list, and R6's of the proposals.
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
- **18 October 2026, the re-frame after G1,** by the founder's answer (`founder-messages/2026-10-18-g1-answer.md`; `founder-decisions.tsv`, G1). The pilot's entry let the founder decide, and the founder chose to re-frame. This change has the founder's go of 18 October 2026, with five changes of the founder's, made here (`founder-messages/2026-10-18-go-on-the-plan-change.md`).
  - **The aim.** For each item of the founder's intent (that message's section B), the best of what the five platforms do, framed as Sharrwah's proposed model. The work ends when the founder has accepted or changed the proposals. This replaces the safe shore and G4.
  - **Questions, not subjects.** Section B's items are the questions the work answers, in neutral words. There is no subject list, and there are no batches.
  - **Stopped:**
    - labelling why platforms differ: the test form's step 3, and the step 5 rows that use it;
    - marking each money question against Yemen's cases: phase D;
    - Stages 3 and 4.

    Stage 0's freeze ends: new reading is allowed where the work needs it.
  - **Kept:**
    - verbatim quotes at a pinned commit;
    - the search and audit behind anything a proposal cites that was not found, or is recorded absent;
    - a separate check of each brief before it runs;
    - one independent review of each result before it reaches the founder;
    - gate G2, on the areas list.
  - **Added:**
    - a budget: 2 billion agent tokens, in the corrected count, with the coordinator's own work shown on top;
    - a sample that measures the cost per new statement before recording runs in full, and re-sizes the rest. It doesn't stop the work;
    - re-sizing whenever a step runs past its expected cost, told to the founder in the coordinator's next message, and a stop only when the re-sized whole would pass the budget;
    - the founder's guard on holding sellers' money;
    - plain words in everything that reaches the founder.
  - **Replaced:**
    - sections 1 to 9 are rewritten in full (Part 2), and the plan's status line and opening paragraph;
    - Stages 3 to 5 become steps R0 to R6;
    - Q3's rows are checked once, at the end, against the proposals (section 6);
    - Stage 1's `within` relation, and its faithfulness pass over every axis, are replaced by re-checking each Yemen fact a proposal uses (section 6).
  - **The count of tokens is corrected.** The method report's first count took each API request once per line of its transcript, and so roughly doubled the pilot's figures (`studies/subjects/S-01/method-report.md`, section 12). The founder's G1 answer stated its budget and bar in that count. At the go, the founder set the budget at 2 billion agent tokens in the corrected count, which this plan uses, and made the sample a measurement with no bar. A week's limit is about 2.8 billion tokens in this count.
  - **Rulings that still bind,** each with the steps it governs:
    - **kinds of source by rule** (12 October; `method/source_kinds.py`). Kinds are compared like with like: R3, R4, R6;
    - **claims of absence** (13 October). A "not in what was read" shows the corpus search behind it, in every language the platform uses and by each country, plan and arrangement it names. The audit by an agent that made none of the claims now covers what each proposal cites (R5);
    - **the role test** (17 October). A statement answers only where its own words name what fills the role the question asks about. It now anchors matching basis 4 (section 6): R3, R4, R6;
    - **one party on every platform** (17 October, phase C): the merchant, the buyer, and the platform itself. R4, R6;
    - **"no part"** (17 October). A statement that a party has no part names no one, but shows that party isn't in its platform's set: R4, R6;
    - **where the money's flow ends** (17 October). It ends at the payout to the merchant's own bank account. A wallet is in the flow when its own words say it holds the merchant's sales proceeds before that payout. This governs Q5's last paragraph: R3, R4;
    - **Stage 1's rules for reading a state** (12 October, pass 2). A condition's states are alternatives; a state's place is the scope its source gives it; only a state whose source says it holds in all of Yemen supersedes states at other places; a proposed state is never today. R4, R5;
    - **reading each part of Yemen's today with its date** (17 October): R4, R5;
    - **Q2's frame** (17 October, phase D). The merchant sells in the Yemeni market, and a condition naming only countries is checked against that: R4, R5;
    - **agents' effort by step** (13 October), extended to the new steps below.
  - **Rulings that lapse:**
    - with the test form: step 3's order of tags, "no difference" and the "business model" test; step 5's added rows and its letter rule; causes compared on overlapping scopes; coexistence `unknown`; several coexistence letters joined by `+`; "names a law";
    - also with the test form, since they rest on step 5's rows: the mapping of when a Q3 row must be answered (`briefs/E-rows.md`), and the four time-bomb types. The check of Q3's rows at the end gets its own brief;
    - Q3 at close-out, which this change supersedes.
  - **Effort by step:**
    - `max`: each brief's check; the check of this change; R1's review; R4's drafting runs and its company-decisions run; R6's review and its check of interactions;
    - `high`: R1's per-platform runs; R5's re-checks and audits; the check of Q3's rows at the end;
    - `medium`: recording and checking runs (R2 and R3). A run whose check or review shows gaps is re-run at `high`, and the re-run counts in its step's cost;
    - `low`: one-off mechanical questions.
  - **The coordinator's own.** These are the coordinator's, not the founder's message's. The founder may overturn any:
    - basis 4 anchored to roles (section 6);
    - the per-platform runs that name each platform's areas, grouping further where needed, each grouping marked as the agent's own (step R1);
    - each area tied to the questions that draw on it, with a script copying the statements under those areas (steps R1 and R3);
    - the sample chosen by rule after the depth choice, and run while the founder marks the areas (step R2);
    - each recording run ending with a short account, and drafting from those accounts, one question per run (steps R3 and R4);
    - two review batches, and a separate check of how the proposals bear on each other (step R6);
    - the capture list sent when recording ends (step R3);
    - what a "must do" mark does (step R1);
    - the form of a decision item (section 5);
    - risks 15 to 18 (section 7);
    - the check of Q3's rows run just before the proposals reach the founder, so that its list comes with them (section 6);
    - Stage 1's open items done only if a proposal uses them (section 6).
- **18 October 2026,** method fixes during step R1, within this plan. Each is listed to the founder in one plain line in the next message:
  - **A platform's own names** include each part of a list entry's path, each half of an English / Arabic pair, and entries out of the concern map's scope. These are all the platform's own words; scope decides only what is placed (`method/areas_extract.py`).
  - **The corpus search reads Shopify's Help Center** held in observed-sh, in English and Arabic, under each page's address. Before, it reached the Help Center only through older fetch archives (`method/corpus_search.py`).
  - **The copy is in two phases** (step R3, above). Tying whole areas to a question would have handed several runs over 1,000 statements, most not bearing on it.
  - **Agents get the questions without the founder's items or expectations,** from `studies/proposals/questions-for-agents.md` (section 6). The check of the review brief found that `questions.md` carried both.
  - **The sample is Q2 on Salla,** by step R2's rule: of the in-depth runs, the one whose candidate statements are nearest the median, the lower on a tie.

- **18 October 2026,** method fixes from the check of the R3 briefs (`studies/proposals/checks/R3-briefs-check.md`), within this plan. Each is listed to the founder in one plain line in the next message:
  - **Reading is bounded, sentence by sentence** (step R3). For each sentence of its question, a recording run reads at most 10 pages from its platform's own map of its help, chosen by title; one corpus search, reading at most 5 of the documents it lists (10 where no map is held); and at most 5 live pages. It stops sooner once 5 pages in a row add nothing new. A checking run reads less.
  - **Depth goes only to the sentences** that concern money flows, legal structure, the data model or partner contracts, with at most 5 more pages each (step R3).
  - **The contracts behind a platform's providers** are recorded as the platform's own material shows them, with any agreement its terms incorporate or name as binding on the seller. A provider's own terms are otherwise not read: where the platform names them, they are recorded as not in what was read, with their address. This narrows step R3's "the contracts behind its providers".
  - **The search behind a "not in what was read"** is one corpus search for what is missing, in each language as alternatives, and one more with the places, plans or arrangements the row is about, reading at most 5 of the documents listed. This narrows section 6's "by each country, plan and arrangement it names", which would otherwise mean one search for each.
  - **Live pages read in step R3** are captured after each run, and before any proposal cites them. This changes, for R3's runs, the rule that a page read new is "captured and committed before it is cited", wherever the plan states it (sections 2, 3, 6 and 9): a run cites a live page before the coordinator captures it, and the checker reports its quotes as pending until then.
  - **Copies keep their ids.** Each copy is numbered by its line in its source, and copied gaps get ids too, so an account can cite them and an id never moves to another statement.
  - **Each question's sentences are numbered** by `method/agent_questions.py`, so that every run, and the checks, count them alike.
- **18 October 2026,** fixes from the review of the areas list (`studies/proposals/areas/review.md`: 25 findings, 15 must fix), within this plan. Each is listed to the founder in one plain line in the next message:
  - **Five areas added, 34 in all,** so that the founder can mark apart what the platforms keep apart: languages (A-30) and currencies (A-31), split from selling to several countries (A-15, now per-country versions of one store, with the countries a store sells to in A-16); gift cards, store credit and customer wallets (A-32), from marketing and elsewhere; catalogs and price lists (A-33); and charity stores (A-34), a help-centre category of Salla's that no area held.
  - **Platform areas re-cut by the coordinator,** each with its reason in its note and in the platform's notes: Salla Payments and BigCommerce Payments join the platforms' own payment services (A-12); Salla's and WooCommerce's financing join A-13; WooCommerce's WordPress.com account joins accounts (A-01); Zid's list of countries joins where the platform operates (A-16).
  - **Questions draw on more areas.** Each question now draws on the areas where the review found statements bearing on it, and Q8 draws on every area, since any unit can be introduced by plan, place or release stage. A run sets aside what doesn't bear, so wider ties lengthen its selection most, and its copies only by what it chooses to copy. Candidate statements for the in-depth runs rose from about 12,400 to about 23,000; the sample measures what that costs. A few single concerns the reviews found bearing on a question its areas miss are added as candidates (`studies/proposals/areas/extra-candidates.tsv`), and the pointers the reviews asked for go in the runs' starting messages (`studies/proposals/briefs/R3-starting-messages.md`).
  - **The pilot's statements are offered to every question,** as the selection's last row: copied for Q5, as before, and judged like any other row for the other questions.
  - **Zid is read in depth for Q6,** since its record shows what Shopify's and Salla's don't: Syria among the countries it lists, while Zid Pay bars dealings with it.
  - **The checks by script** now also check that each concern a depth reason cites is reached by its question, that no area both draws a question and says the work leaves it out, and that what is kept anyway names each question drawing on the area (`method/check_areas.py`). `areas.md` shows every platform name.
  - **The sample is now Q3 on Salla.** The same rule, applied to the revised list, picks the in-depth run whose candidate statements are nearest the median of 875: Q3 on Salla holds exactly 875.
  - **The review's re-check** (`studies/proposals/areas/review-recheck.md`) found 21 of its 25 findings fixed and one new one to fix before the founder sees the list: A-15's heading claimed more than it held. It is now "Per-country versions of one store", and BigCommerce's Geography moved to A-16.
- **19 October 2026,** fixes from the last read of the checking brief (`studies/proposals/checks/R3-checking-brief-read.md`: 14 findings, 8 must fix), within this plan. Each is listed to the founder in one plain line in the next message:
  - **Basis 1 of section 6's matching rule is read narrowly in checking runs:** the same term matches only where both platforms use it for what the question's sentence asks about, each quoted with what it names. A word both platforms use for different things is no basis, as section 6's warning on homonyms intends.
  - **A checking run's "not in what was read" rests on its search for the sentence** it belongs to, read among the documents that search listed, with one more search only for a place or plan its statements name. This narrows, for checking runs, the search behind a not-found that the entry of 18 October set.
  - **An in-depth account's points that record only what it didn't find** are not sorted against, and a checking run cites its own open copied gaps before it records a new row.
  - **The corpus search lists the documents most about the terms first,** by how densely they hold them, so that a capped listing doesn't fill with long reference pages.
- **19 October 2026,** fixes from the first checking runs, within this plan. Each is listed to the founder in one plain line in the next message:
  - **A checking run may search twice for a sentence.** Some runs chose their search terms before reading and left points out, so those points were never checked: about 30 in Q4 on WooCommerce and on Zid. A run now lists the points first, and runs one more search for any the first left out. Q3 and Q4 on WooCommerce and Q4 on Zid are continued to search for the points they left out.
  - **Every point a checking run's reading doesn't show gets a row,** up to 20. Two runs recorded fewer than 20 and left the rest unchecked.
