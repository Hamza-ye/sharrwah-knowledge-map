# The plan change after G1 (draft)

**Status: draft, 18 October 2026.** Nothing here is in `PLAN.md` yet. It goes in only with the founder's go (`PLAN.md` section 9: a change to the frame needs the founder's go). Until then, `PLAN.md` stands as it is, and no work agent runs.

**What this file holds:**
- **Part 1:** the dated entry for `PLAN.md` section 11;
- **Part 2:** the sections it rewrites, in full, each headed with the section it replaces. Sections 10 and 11's earlier entries are unchanged.

**What it rests on:**
- the founder's G1 answer (`founder-messages/2026-10-18-g1-answer.md`), and its decisions as recorded in `founder-decisions.tsv`;
- the questions (`studies/proposals/questions.md`);
- the first step's briefs (`studies/proposals/briefs/`);
- the sizing (`studies/proposals/sizing.md`).

# Part 1. The entry for section 11

- **18 October 2026, the re-frame after G1,** by the founder's answer (`founder-messages/2026-10-18-g1-answer.md`; `founder-decisions.tsv`, G1). The pilot's entry let the founder decide, and the founder chose to re-frame. This change has the founder's go of [date to be filled in].
  - **The aim.** For each item of the founder's intent (that message's section B), the best of what the five platforms do, framed as Sharrwah's proposed model. The work ends when the founder has accepted or changed the proposals. This replaces the safe shore and G4.
  - **Questions, not subjects.** Section B's items are the questions the work answers, in neutral words. There is no subject list, and no batches.
  - **Stopped:** labelling why platforms differ (the test form's step 3, and the step 5 rows that use it); marking each money question against Yemen's cases (phase D); Stages 3 and 4. Stage 0's freeze ends: new reading is allowed where the work needs it.
  - **Kept:**
    - verbatim quotes at a pinned commit;
    - the search and audit behind anything a proposal rests on that was not found or is recorded absent;
    - a separate check of each brief before it runs;
    - one independent review of each result before it reaches the founder;
    - gate G2, on the areas list.
  - **Added:**
    - a budget: the agents' work aims to stay within about 2 billion tokens, with the coordinator's own work shown on top;
    - a sample that measures the cost per statement before recording runs in full;
    - a stop at the first step that runs past its expected cost;
    - the founder's guard on holding sellers' money;
    - plain words in everything that reaches the founder.
  - **Replaced:**
    - sections 1, 2, 4 (Stages 3 to 5), 5, 6, 7 and 8 are rewritten;
    - sections 3 and 9 are amended;
    - Q3's rows are proposed for dropping, for the founder's go (section 6);
    - Stage 1's `within` relation and its faithfulness pass over every axis are replaced by re-checking each Yemen fact a proposal uses (section 6).

# Part 2. The sections, rewritten

## 1. The aim and the end *(replaces "The aim and the safe shore")*

Sharrwah is one platform for many markets. Yemen is its first market, not its design target.

**The aim.** For each item of the founder's intent (`founder-messages/2026-10-18-g1-answer.md`, section B), the best of what the five platforms do, framed as Sharrwah's proposed model:
- what it is called, how it is structured and how it behaves;
- what can plug in, what is set per what, and who sets it;
- how the design divides into parts that can be built in order;
- where the founder's item says something is decided later, what the design must keep open instead.

That should be enough to start the design of the first build.

**The principles stay:**
- one platform, many markets: product line engineering (Pohl, Böckle & van der Linden 2005);
- each decision likely to change sits behind its own module (Parnas 1972);
- effort follows risk (Fairbanks 2010; Boehm 1988), and each decision is taken at the last responsible moment (Poppendieck & Poppendieck 2003).

**The end.** The work ends when the founder has accepted or changed the proposals. Then the first build's design starts under its own plan.
- Anything the accepted proposals leave open comes to the founder during that design, when it is needed. How far currencies can be set or changed is one such item.
- No proposal rests on a derived document, or on the founder's words taken as evidence of what a platform does.

## 2. What changes from the run so far *(replaces section 2)*

- **The pilot is done.** Its entry (`studies/subjects/S-01/entry.md`) let the founder decide.
  - Its Decisions 1 to 14 are deferred. They stay open, and bind nothing, not even per market. They come back as proposals once the work has framed them.
  - Its files are the coordinator's to use. Its 23 variation points, and its open review findings (among them 29 and 36), feed the money proposals.
- **The guard** (`founder-decisions.tsv`, G1). No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision. That covers Sharrwah itself holding it (the entry's option A), and a payment company holding it in an account opened through Sharrwah (option B). It limits only what goes live. It neither requires a proposal to provide for either arrangement nor rules one out.
- **Questions, not subjects.** Section B's items, in neutral words (`studies/proposals/questions.md`), are what the work answers. They are not subjects, and don't take the test form.
- **What is recorded is reused:**
  - the concern map's `concerns.tsv` and `statements.tsv` for all five platforms, in every placement, but not the first runs' `placements.tsv`;
  - the pilot's files;
  - Stage 1's output.

  A script copies a recorded statement unchanged, with its citation, wherever a question needs it.
- **New reading is allowed** where what is held doesn't show what a question needs. This replaces Stage 0's freeze.

## 3. Who does what *(amended)*

**The founder decides:**
- what this section already reserved: scope and the business model, company and legal questions, building ahead, spending, what only the founder can do, and the gates;
- every proposal for section B;
- the marks on the areas list;
- the company decisions;
- whether any arrangement that holds sellers' money through Sharrwah goes live;
- changes to this plan's frame.

The founder may challenge any decision of the coordinator's.

**The coordinator decides** how the work is done, within the founder's G1 answer, and the facts. It:
- plans the steps and writes the briefs;
- runs the agents and checks;
- owns the proposals' recommendations;
- keeps this plan and `STATE.md`;
- brings the founder what is the founder's.

**What reaches the founder:**
- **Plain business words.** A term that can't be avoided is defined in one line. Quotes and ids stay in the files.
- **Several decisions may come in one message,** each standing on its own, with its own answer line.
- **Method rulings go on as this plan allows.** Each is listed the next time work comes back to the founder, in one plain line saying what it changes. The founder may overturn any.

**Agents.** Each gets one short task from a written brief, as the method report's proposal 3 asks. Scripts do the mechanical work. A separate agent checks each brief before it runs. An agent that did none of the work reviews each result before it reaches the founder.

**The checker.** `method/check_proposals.py`, built from the pilot's checker before step R2, enforces mechanically:
- quotes are verbatim, at a commit;
- a statement copied by script is unchanged, with its citation;
- each record is tied to a question;
- each fact a proposal rests on is tied to a statement or a Stage 1 id;
- a "not in what was read" lists what was read;
- an absence rests on a complete list.

## 4. The sequence *(Stages 3 to 5 replaced)*

Stages 0, 1 and 2 are done. They stay below as a record, unchanged. The work from here runs as steps R0 to R6. Each step records its expected cost in `STATE.md` before it starts (`studies/proposals/sizing.md` gives the first estimates).

### Step R0. The plan change

- This change, the first step's briefs, and the neutral wording of each question are drafted.
- An agent that did none of the drafting checks them against the founder's G1 answer and the recorded data, for whether they can work and what they will cost.
- The founder gets a plain summary. Nothing else runs before the founder's go.

### Step R1. The platforms' broad areas, then gate G2

- **A script** (`method/areas_extract.py`) extracts each platform's own organizing lists from all that is recorded:
  - the concern map's inventory lists and concerns;
  - Shopify's Help Center menus;
  - Salla's help-centre categories.

  So legal, place and eligibility matters show too, not one menu only.
- **One short agent run per platform** (`briefs/R1-areas-one-platform.md`) names the platform's broad areas in its own names, each with a plain line.
- **The coordinator merges the five lists into tens of areas.** Where the platforms' own names can't bring the list down to tens, the coordinator groups further, and marks each such grouping as its own. With the list, the coordinator says:
  - what a "won't do" mark on each area removes from the work;
  - what evidence the section B proposals keep anyway;
  - what the work would leave out, and why;
  - for each question, which platforms to read in depth and which only to check for anything that differs from or goes beyond them, with why.
- **An independent review** (`briefs/R1-areas-review.md`), then the founder.
- **Gate G2.** The founder marks what Sharrwah won't do and what it must. Anything unmarked stays in.

### Step R2. The sample

- Before recording runs in full, one short run records one question on one platform. That is question 3 on Shopify, a typical run rather than the cheapest.
- **What is measured:** its cost per statement recorded, not counting statements a script copies unchanged.
- **If it isn't below half the pilot's 1.1 million per statement for phases A and A2,** the work stops and comes to the founder.
- **Otherwise** the steps that record or audit statements are re-sized from the measurement, and the others as before.

### Step R3. Recording, by question

- **Depth by question.** For each question, the platforms the coordinator chose with the areas list are read in depth. The others are checked only for anything that differs or goes beyond.
- **A script copies first.** For each question and platform, it copies the recorded statements that bear on the question, unchanged. The run then reads only what is still needed:
  - held material first, through the corpus search;
  - new material only where what is held doesn't show it.
- **Each run is short:** one question on one platform.
- **What a run records:**
  - each statement in the platform's own words and terms, scoped as its source scopes it;
  - what it doesn't find, as "not in what was read", listing what it read.

  It records something as absent only from a complete list the platform publishes.
- **What shows only by signing up** to a platform goes on the founder's capture list. Capturing is optional, and the work doesn't wait for it.
- **Depth goes where a wrong guess would be expensive to change after launch:** money flows, legal structure, the data model, and partner contracts. Every question gets enough to propose from. What lies outside the questions gets a line each, with the reason.

### Step R4. The proposals

- **Drafting runs** draft each question's proposal from its records, two questions per run. Each draft gives:
  - how the platforms handle it, in their own terms;
  - Sharrwah's proposed names, structure and behaviour;
  - what can plug in, what is set per what, and who sets it;
  - how it divides into parts that can be built in order;
  - what the design must keep open.
- **The coordinator finishes each proposal** and owns its recommendation.
- **Yemen.** For each proposal, from Stage 1, the proposal records what Yemen's evidence allows, forbids or doesn't show.
- **The money proposals** (questions 4 and 5) take up the pilot's deferred Decisions 1 to 14. They say what the design provides for, under the founder's guard.
- **Company decisions** are collected as the work finds them: where the company is based, which providers and partners Sharrwah works with, any licence, who may register, and any others. Each comes to the founder in plain words, with a recommendation and whether it needs a lawyer.

### Step R5. Checks by risk

Once a proposal is drafted, and before its review:
- **Each fact it rests on gets the full checks:** a re-check against its source, and, for anything not found or recorded as absent, the search and audit.
- **Each Yemen fact it uses** is re-checked against its quotes.
- **Every quote is checked by script.**
- The rest is recorded as read, without audits.

### Step R6. Independent review, then the founder

- An agent that did none of the work reviews the proposals, in two batches.
- They then reach the founder, several in one message, each with its own answer line. The company decisions come with them.

## 5. The gates *(replaces section 5)*

| Gate | When | What the founder decides |
| --- | --- | --- |
| G0 | 12 October 2026, done | The plan |
| G1 | 18 October 2026, done | Re-frame, with the decisions in `founder-decisions.tsv` |
| The go on this change | After step R0 | This plan change |
| G2 | After step R1 | The areas: what Sharrwah won't do, and what it must |
| The proposals | After step R6 | Each proposal, accepted or changed, and the company decisions |

The proposals replace G3 and G4. The work ends when every proposal is accepted or changed.

**A decision item** reaches the founder in plain words:
- the question in one line, and why it is the founder's;
- what the platforms do, and what Yemen's evidence allows, forbids or doesn't show;
- the options, each with what it needs built and what it needs from outside, such as a licence, a partner or money;
- the coordinator's recommendation, and its reason;
- the answer line.

Defer is always allowed. A deferred item stays open and binds nothing, unless the founder says otherwise.

**Standing decisions and spending** stay as they were.

## 6. The rules *(replaces section 6)*

### Recording

- **Questions, not categories.** Agents get section B's items only as the neutral questions in `studies/proposals/questions.md`.
- **The platforms' own words.** Agents record what each platform says and does in its own words and terms. The founder's working words never become the names or categories they record under. Q1's rule against our own category names (11 October, rule 1; the pilot's A brief, rule 1) holds for everything agents record.
- **No level or setter fixed in advance.** Nothing fixes where something is set or decided, or who sets it. "Per market" in the founder's section B is a working description, not a fixed level.
- **All that is recorded, not only menus:** how the platforms organize their products, and also their terms, country rules, eligibility and availability.

### Evidence

- **Statements stay verbatim,** cited at a pinned commit. Every quote is checked by script.
- **Kinds of source** stay as the pilot assigned them, by rule (`method/source_kinds.py`).
- **Before a gap goes to anyone,** its route is checked against what is held, as before.
- **"Not in what was read" and "absent".** What a run doesn't find is recorded as "not in what was read", with what it read. It is recorded as absent only from a complete list the platform publishes.
- **Incorporated agreements** may be read, as before.
- **The founder's words** are never evidence of what a platform does. The founder's decisions are recorded as decisions.

### Checks by risk

- **The full checks** apply to each fact a proposal rests on: the search and audit for anything not found or recorded absent, and a re-check against its source.
- **The rest** is recorded as read, without audits.

### Comparing platforms

When a proposal compares platforms, the matching rules stand:
- two concepts are the same only on a shared term, identifier or definition, or by answering the same question;
- the merchant, the buyer and the platform itself are one party on every platform;
- a statement that a party has no part names no one filling the role.

### Yemen

- **Each proposal records** what Yemen's evidence allows, forbids or doesn't show, from Stage 1.
- **Each Yemen fact it uses is re-checked against its quotes.** That includes whether a later state covers the same place or a place that contains it.
- **This replaces the faithfulness pass over every axis, and Stage 1's `within` relation, which is not built.**
  - The `within` relation addressed a stale state taken as today's for a place another state covers.
  - Each fact's re-check now catches that, for the facts the work uses.
- **Stage 1's other open items are done only if a proposal uses them:** the review's "can follow" items, such as the internet shutdowns, and its two minor items.
- **Other markets** wait until the founder decides to enter them.

### Q3's rows

The coordinator proposes dropping them, for the founder's go.
- **What they were kept for.** They were agent-written beliefs that might return as false requirements.
- **Why they can be dropped.** Under this change, nothing reads them. Section B and the areas list come from the founder and the platforms, so the rows can't return as requirements.
- **They stay in `register/` as a record.**
- **If the founder would rather reconcile them,** one short run after step R6 places each row against the accepted proposals, and lists the rows they don't answer. It costs about 30 to 40 million tokens, with its brief check.

## 7. Risks, and what happens when one shows *(rows changed or added)*

| # | Risk | How it shows | What happens |
| --- | --- | --- | --- |
| 1 | The work grows past what the proposals need | A record tied to no question; a step past its expected cost | The checker rejects untied records. A step past its expected cost stops and comes to the founder |
| 2 | A word of ours, or the founder's, makes the result | A brief or question uses a working word as a category; an agent records under it | The questions are worded neutrally and checked before they run. The independent review looks for it |
| 15 | Statements copied by script carry an old error | A copied statement fails its quote check, or the review finds it wrong | Copies are checked like new ones. A fact a proposal rests on gets the full checks |
| 16 | Depth by question misses a platform's different answer | A checked platform shows something the in-depth platforms don't | Checking runs record what differs or goes beyond. The review checks each depth choice against the records |
| 17 | The budget doesn't fit | A step's measured cost, scaled, passes the total | The plan says what it would cut, and the founder decides |

Risks 3 to 12 and 14 stand as they were. Risk 13 (the frame is wrong) was met at G1.

## 8. When work stops and comes to the founder *(added to)*

- **The sample misses its bar:** its cost per statement isn't below half the pilot's 1.1 million.
- **A step runs past its expected cost,** once. This is added to the stop for a stage that overruns its size twice.
- **The plan can't fit its budget.** It says what it would cut, and the founder decides.

The other stops stand as they were.

## 9. Keeping it coherent across sessions *(amended)*

- **Every result traces back** through proposal, question and record to a statement or a Stage 1 fact, and from there to a source at a commit (Gotel & Finkelstein 1994).
- **The new work's files live in `studies/proposals/`:**
  - `areas/`;
  - `records/<question>/<platform>/`;
  - `sample/`;
  - `drafts/`;
  - `checks/`;
  - `review/`;
  - `company-decisions.md`;
  - `briefs/`;
  - `costs.tsv`, each run's measured cost.
- **Every step ends with a commit and an update to `STATE.md`.**

The rest of section 9 stands.
