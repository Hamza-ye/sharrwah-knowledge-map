# Sharrwah design method

**Status: adopted on 24 October 2026, with amendments 1 and 2 (section 12).** It governs the work. `PLAN.md` stays as the record of how the work got here and is no longer followed. This document changes only by a numbered amendment (section 12). Version 1 as first proposed is at commit `b78686e`.

## 1. What the work must produce

The work ends when Sharrwah's first version has:
1. **An architecture description:** arc42's twelve sections, meeting ISO/IEC/IEEE 42010 (section 4).
2. **A decision record for every decision on the first version's critical path.** Each one is accepted, deferred with a stated trigger, or superseded (section 4). The records are the description's section 9.
3. **An answer from the founder to every founder decision** (section 3), or a deferral with a trigger.
4. **A risk register** in which every high risk is mitigated, accepted by its owner, or closed.
5. **A walkthrough of the core flows** against the accepted decisions (section 8). It covers the first market's flows and the change scenarios of section 3a, with no gap and no clash left open.

This is the "life cycle architecture" milestone of Boehm's spiral model (1996). In plain terms: the design is defined, its major risks are resolved, and the people who decide have committed to it.

It is not production code. Production code comes after, part by part: when a part meets the definition of ready (section 5), and the founder decides.

## 2. The practices this method is built from

Each part of the method is an established practice, not one invented here. When a new problem appears, it is handled by one of these practices. No new rule or step is added without an amendment (section 12).

| Practice | Source | What it does here |
| --- | --- | --- |
| Risk-driven design | Fairbanks 2010; Boehm 1988 | Effort goes only where a wrong choice would hurt. Each subject stops when its risks are reduced enough, not when every fact is checked. |
| Attribute-Driven Design | Cervantes and Kazman 2016 (SEI) | Options come from known designs (reference architectures, patterns, tactics, existing components) before anything is invented. |
| Variability and binding time; assumptions about the world; information hiding | Clements and Northrop 2001; Pohl, Böckle and van der Linden 2005; Zave and Jackson 1997; Parnas 1972 | The market guard: what varies by market is configured, not built (section 3a). |
| Decision records | Nygard 2011; MADR 4 | One short record per decision: context, options, evidence, outcome, consequences, status. |
| A shared language, kept in a glossary | Evans 2003 (domain-driven design); arc42 section 12 | Each term a decision relies on has one meaning, taken from the domain's own structures: here, the reference platforms' (section 4). |
| Decision scope, assumptions and related decisions | Tyree and Akerman 2005; Lago and van Vliet 2005 | Each record says what it decides, what it takes as given, and what it leaves open to which subject (sections 4 and 10). |
| Stakeholder needs, stated and confirmed | ISO/IEC/IEEE 29148 | What a stakeholder says is stated as the need or decision it carries, in the project's terms, and the stakeholder confirms it. Here: the founder's messages are framed before they are acted on (section 3). |
| Ready and done checks for a decision | Zimmermann: START and ecADR | A decision is taken only when it is ready, and is closed only when it meets the done checklist. |
| One-way and two-way doors | Bezos, 2015 letter to shareholders | Decisions that are hard to undo go to the founder. Decisions that are cheap to undo are made quickly by engineering. |
| Integrity levels | IEEE 1012 | Verification effort scales with the consequence of being wrong, not uniformly. |
| Quality-attribute scenarios | ATAM, SEI 2000 | The design is judged by concrete scenarios with expected outcomes, walked through the decisions. |
| Architecture description | ISO/IEC/IEEE 42010:2022; arc42 | The shape of what the work produces (section 4). |
| Last responsible moment | Poppendieck 2003 | No decision and no document before it is needed. |
| Limits on work in progress | Anderson 2010 (Kanban) | Few tasks at a time, each finished before more start. |
| Traceability and change control | ISO/IEC/IEEE 29148; IEEE 828 | Each decision lists the evidence it rests on, so a change in evidence shows which decisions it reopens. Baselines are named by commit in `HISTORY.md`, one pull request per milestone. |
| Risk register | ISO 31000 | Each risk has an owner, a mitigation and a status. |

## 3. Who decides what

There are three kinds of question. Each has one owner.

| Kind | Test | Owner | How it is settled |
| --- | --- | --- | --- |
| **A fact** | "What is true?": what a platform does, or what a market's rules allow | Engineering investigation | By evidence. Never put to the founder. |
| **A founder decision** | "What do we want, and what risk do we accept?", where the answer has business, legal or money consequences and is hard to undo (a one-way door) | The founder | Given on one page: the question, the options, what the evidence shows, the risks and a recommendation. The founder answers or defers with a trigger. |
| **An engineering decision** | "How do we build it?", where the answer is cheap to change later (a two-way door) | The coordinator, as engineering lead | A decision record with its reasons. Each milestone report lists it. It stands unless the founder vetoes it within two days of that report. |

**Founder decisions** include:
- whether Sharrwah ever holds sellers' money;
- which markets it enters, and when;
- where the company is based, and which company contracts with sellers;
- which payment providers and partners it contracts with;
- who may register as a seller;
- Sharrwah's pricing model;
- the order in which the first version covers the areas;
- the business targets behind the quality scenarios;
- the budget and risk appetite of the work.

**Engineering decisions** include the data model, the level at which each setting lives, the interfaces between parts, naming, and build order. This replaces G1's rule that every proposal for section B was the founder's (18 October; amendment 1h).

Agents investigate and check. They never decide.

**The founder's messages are framed first** (amendment 2d):
- before acting on a message, the coordinator states what is genuine in it, the concern or the decision, in engineering terms, so that the founder can correct the framing;
- the record holds the framing (`founder-decisions.tsv`), never the message. Messages are no longer saved; the files in `founder-messages/` from before 24 October, 22:12 UTC, stay as the record;
- the founder's words are attestations, not evidence (F-05).

## 3a. The market guard

Sharrwah is one platform for many markets. Yemen is its first market, not its design target. This comes from the founder on 10 October, from G1's B1, B2 and B7 on 18 October, and from the founder again on 24 October.

The guard makes this checkable. It comes from the frame of 10 October (`8946887:method/frame.md`), which draws on product-line engineering, on requirements engineering's assumptions about the world, and on information hiding.
- **Every decision record states its outcome type:**
  - **Built:** engineering decides it, and it is the same in every market;
  - **Configured:** Sharrwah sets it per market or plan;
  - **Chosen:** the merchant sets it;
  - **Context:** law, regulators, providers and the market set it.

  If an outcome varies, the record says by what.
- **No market's name appears in anything Built.** A script checks this: `method/decision_status.py --guard`.
- **A market's facts are Context.** They may set Configured values, or turn a Built outcome into a Configured one. They never shape a Built outcome: build for the range, and configure the value.
- **References first, then the market.** Options are drafted from the references, and the first market's facts then test them.
- **General mechanisms that have a precedent are allowed,** even when the first market is what raises them. Examples: cash on delivery, payments that stay pending for a long time, a courier holding cash.
- **A record that fails the guard goes to the founder:** "Where a market needs something the design can't carry, it comes to me" (G1's B2).
- **Change scenarios.** A subject that touches money, markets, sellers or the company must pass three more scenarios:
  - a second market, where a payment processor holds the funds;
  - the company based in another country, Oman for example;
  - the first market dropped.

## 4. The artifacts

1. **The architecture description,** in `architecture/`, in arc42's twelve sections.
   - A section is written only when a subject fills it.
   - It carries what ISO/IEC/IEEE 42010 asks for: the stakeholders and their concerns, the views, the correspondences between them, and the decisions with their rationale.
   - Its glossary, section 12, grows from the first record on: each record adds the terms it relies on (item 2).
2. **Decision records,** one file each in `decisions/`, in MADR's short form. The template is in `decisions/README.md`. These fields are added:
   - door: one-way or two-way;
   - integrity level: 1, 2 or 3 (section 6);
   - outcome type, and what it varies by (section 3a);
   - the risks it addresses, by id;
   - the evidence it rests on, by id;
   - the records whose outcomes it depends on (section 10);
   - status: `proposed`, `accepted`, `deferred` (with its trigger), `under review` (its evidence or a term it uses changed), or `superseded by` another record.

   Each record also has two sections, checked like its facts (section 6; amendment 2):
   - **Terms:** each term the record relies on, with its extent: what it covers and what it leaves out.
     - A term for what platforms do is defined from Shopify's and Salla's own structures, such as settings pages, schemas, permissions and help pages, by file path. It says where the two differ.
     - A term for law, a regulator or a provider is defined from that source (Context).
     - A term Sharrwah coins is defined by its record, and placed against the platforms' nearest terms.
     - Each term goes into the glossary, `architecture/12-glossary.md`. A record uses the glossary's meaning, or changes it openly (section 10).
   - **Scope:** what the record decides; what it takes as given; and what it touches but leaves open, each item naming the subject in `decisions/subjects.tsv` that will decide it. A record decides nothing outside its scope.
3. **The backlog,** `decisions/subjects.tsv`. It has one row per subject, with:
   - the areas and questions it covers;
   - its door and risk;
   - when it is needed;
   - the arc42 sections it fills;
   - its status and budget.
4. **The risk register,** `risks.tsv`: id, risk, likelihood, impact, mitigation, owner, status (open, mitigated, accepted, closed), trigger, and the decisions it links to.
5. **The evidence base:** `evidence/` and `studies/` as they stand at the baseline (section 13).
   - It is frozen.
   - New evidence is added only by an investigation for a named decision (section 5, step 2), with its source and date.
6. **`STATE.md`,** one page:
   - the current milestone, subject and step;
   - the tasks in flight;
   - the budget used;
   - what is settled, open or superseded;
   - the next step.
7. **`HISTORY.md`:** the baselines, by commit.
   - Each milestone is one pull request. It is merged into `main` with a merge commit and gets a row there.
   - History is never rewritten.
8. **Milestone reports,** `reports/M<n>.md`, one at each milestone and each planned pause. Each is at most two pages, and is also the pull request's description. It sets out:
   - what is settled, open or invalidated;
   - the engineering decisions, with the veto window starting at the report;
   - any exception to the guard;
   - the top risks;
   - cost against budget;
   - what is needed from the founder: one-way decisions only, each with a recommendation and an answer line.

Briefs, check sheets and notes are working material for a task, made only when the task needs them. They are never deliverables.

## 5. How work is organized: one subject at a time

A **subject** is one decision area on the first version's critical path, small enough to finish in about a day. Subjects run one at a time, depth-first. A subject starts only when the one before it has closed.

There is one exception. **While a subject waits only for the founder's answer, the next subject's framing and evidence steps may start.**

**The extent is the 34 areas** (`studies/proposals/areas/areas.tsv`). On 18 and 19 October the founder decided they are Sharrwah's whole extent. The first version covers them in an order the founder sets.

**The references:**
- **Shopify and Salla are the primary references.**
  - Shopify is the most mature global model.
  - Salla is the regional, Arabic model.
- **Zid, WooCommerce and BigCommerce come in only when a decision needs them:** when Shopify and Salla are both silent on something a decision turns on, or disagree. Their records are already held, so bringing them in is a lookup, not new research.
- **The references supply options, not answers.** The first market's facts test the options (section 3a).
- **Outside experience.** After Shopify and Salla, options come from established designs: reference architectures, patterns, and engineering writing such as Shopify's own talks and posts (`evidence/shopify-engineering/`).
  - Each source is weighed by the Knowledge Map's source types (`register/README.md`): what it is good for, what it can't tell, and how far to trust it. A company's blog is that company's account.
  - Open-source platforms are read only for what they fit. Medusa, Saleor and Vendure don't keep independent sellers' stores apart as Shopify does, so they are no reference for tenancy.
  - Each subject adds the outside sources its decisions need.

**The steps of a subject:**
1. **Frame** (about two hours).
   - List the subject's decisions, each as a draft record, and check each one is ready (Zimmermann's START): the stakeholders are known, the time is right, there are at least two options, the criteria are known, and the template is chosen. Decisions that aren't needed yet are deferred with a trigger.
   - Pull the subject's questions from the Knowledge Map (`method/km_select.py`). Give each one a disposition: answered by a record, a driver, a scenario, or deferred with a trigger.
   - Mark each decision's door, integrity level and outcome type, and draft its scope: what it decides, and what it touches but leaves to another subject. Link its risks, and set the subject's budget.
2. **Evidence** (timeboxed).
   - Take what each decision turns on from the held records: Shopify and Salla first, then the first market's facts from the Stage 1 digest.
   - Take the extent of each term it turns on from the platforms' own structures, and enter it in the glossary (section 4).
   - Where something is missing, run one investigation with a stated question, a timebox and a budget. Where documents can't settle it, ask a provider, a lawyer or an official source. **Merchants are not asked** (the founder, 24 October).
   - **An investigation may be a spike:** throwaway code that answers one stated question within a timebox, kept in a separate repository. Its result is evidence, and its code is never promoted.
3. **Propose.** Each record states:
   - its terms and its scope (section 4), before its options;
   - at least two options, drawn first from the references and then from outside experience, compared against the decision's drivers;
   - the evidence, by id, with each fact's conditions (plan, country, product, store, date) written out;
   - its outcome type, and how it passes the guard (section 3a);
   - the consequences, including what would have to change if the decision were reversed;
   - the recommendation.
4. **Verify,** at the decision's integrity level (section 6).
5. **Decide.** The founder answers founder decisions. Engineering decisions stand once the two-day veto window, which starts with the milestone report, has passed.
6. **Close.**
   - Walk the subject's scenarios, and its change scenarios (section 3a), through the accepted decisions (section 8).
   - Run the guard check, and write the arc42 sections the subject fills.
   - Update the risk register. Mark the subject closed in `STATE.md` and `decisions/subjects.tsv`, and record its cost against its budget.
   - Send the milestone report.

**The definition of ready for production code.** A part of Sharrwah becomes production code only when:
1. its decisions are accepted, and the founder's decisions on it answered;
2. its parts, interfaces and data are in the architecture description, in the glossary's terms;
3. its quality scenarios are measurable, and its acceptance tests come from them and from the platforms' captured journeys;
4. its high risks are mitigated or accepted, and the guard passes;
5. its security and tenant-isolation tests are specified;
6. its spikes are closed;
7. it has had an independent review at its integrity level, and the founder has seen it in a report.

## 6. How much checking each decision gets

Following IEEE 1012, checking scales with what a wrong decision would cost. It covers **only the facts a decision rests on,** never everything a document mentions.

| Level | Which decisions | Checking |
| --- | --- | --- |
| **3** | One-way doors: money, legal structure, licensing, sanctions | An independent agent, who didn't write the record, checks every fact the decision rests on against its source, including the conditions the source puts on it. Quotes are checked by script. The scenario walkthrough must pass. |
| **2** | Engineering decisions that are expensive to change: the core data model, the money ledger | A script checks the quotes of the facts it rests on, and the coordinator checks their conditions. One independent agent reviews the record. |
| **1** | Engineering decisions that are cheap to change | Quotes are checked by script. Nothing else. |

**A record's terms and scope are checked like its facts,** at the same level (amendment 2): each term's meaning and extent against the paths it cites, and each item of its scope against what the record actually decides. At every level, a script checks that each term is in the glossary, that each item left open names a subject in the backlog, and that no record is accepted before the records it depends on.

A record is **done** when it passes Zimmermann's ecADR checklist:
- **E:** we are confident enough that it will work;
- **C:** at least two options were compared against the criteria;
- **A:** the people who must agree have agreed: the founder for founder decisions, the veto window for the others;
- **D:** it is recorded and shared;
- **R:** we know when it will be built, how it will be confirmed, and when it will be reviewed.

## 7. Limits and stop rules

These keep the plan bounded. They are the only stop rules.
1. **A budget per subject,** set at framing. If a subject reaches its budget plus a quarter, work stops and the coordinator reports to the founder before going on. This replaces the rule of 18 October that work stops only if the whole would pass 2 billion tokens (amendment 1h). The 2 billion stays as an upper bound.
2. **Sample before scaling.** Any check of more than 10 items is first run on 5. If 2 or more of the 5 fail, the check stops, and the step that produced the fault is fixed first.
3. **Stop on risk, not on completeness.** A subject's investigation stops when its decisions meet the ecADR "E" (confident enough), not when every fact has been checked (Fairbanks: effort in proportion to risk).
4. **At most 2 agent tasks at a time.** A task starts only if it can finish within the usage window that remains. A task that is stopped is started again on what it has left, not resumed with its old context.
5. **No new layers.** A new concern goes into the risk register, and an existing practice handles it. Changing the method needs an amendment.

## 8. How the design is judged

- **Each decision record:**
  - it passes the ready check before it is taken, and the done check after;
  - every evidence id resolves, and every quote is found word for word (by script);
  - at levels 2 and 3, every fact it rests on is written with the conditions its source gives;
  - its terms and scope pass their checks (section 6);
  - it passes the guard (section 3a).
- **Each subject:** it passes its scenarios, and its change scenarios.
  - A scenario follows ATAM's form: a stimulus (something happens), the environment (where and when), the expected response, and how we know.
  - The subject passes when every scenario can be answered from the accepted decisions alone.
  - One example: "A buyer in Aden orders and pays cash on delivery. The courier collects the cash and pays the seller; Sharrwah bills its own fee separately; at no point does Sharrwah hold the money."
- **The whole:** the outcome in section 1. It is checked at the end by a walkthrough in ATAM's style. Then the Knowledge Map's 179 questions and the 81 payment rows are reconciled against the accepted decisions: each row is placed, or listed as unanswered (the founder, 18 October).

## 9. Resuming and recovering

- **The durable state:** the decision records, the backlog, the risk register, `STATE.md` and `HISTORY.md`. A coordinator resumes by reading this document, then `STATE.md`, then the records of the open subject. Nothing else is needed to know what is settled, open or reopened.
- **Each task** has a stated output and a definition of done, and writes its output as it goes. It is committed when it ends.
- **After an interruption,** finished outputs stand, and unfinished tasks are run again on what they have left.
- **The scheduled check-in** is on only while a task runs. It reads this document and `STATE.md`, and starts any unfinished task again on what it has left. It commits only checked outputs.

## 10. Change control

- **A decision changes only through a new record that supersedes it.** Both records link to each other, and the old one is never edited.
- **What a record rests on** (amendment 2c): its facts on evidence, its terms on the glossary, and what it takes as given on accepted outcomes, which are accepted records and the founder's decisions. Never on another record's or a draft's wording.
  - A record may take a proposed record's outcome as given only by naming it in its `depends_on` field. It is then accepted no earlier than that record.
- **When evidence changes** (a new capture, a correction), a script lists the records that cite it. They become `under review` and are verified again at their own level.
- **When a glossary term's meaning changes,** the records that use it become `under review` in the same way.
- **A founder decision changes only by the founder.**
- **This method changes only by amendment** (section 12).

## 11. Risks of the work itself

These open the risk register, `risks.tsv`, which also holds the risks found on 24 October.

| Id | Risk | Mitigation |
| --- | --- | --- |
| W-01 | Research grows without end | Risk-driven stop; investigations timeboxed; a budget per subject |
| W-02 | The founder is asked too much, or can't follow | Only one-way doors go to the founder, each on one page, in plain words. A report at each milestone and planned pause. |
| W-03 | The plan keeps being rewritten | This document changes only by amendment; decisions are superseded, never rewritten |
| W-04 | Agents misread or over-generalize a source | Checks scaled by level on the facts decisions rest on; quotes by script; conditions written out |
| W-05 | Usage limits stop work in flight | Small tasks, at most 2 at a time, fresh restarts |
| W-06 | A market's facts change (two central banks, sanctions, rates) | Each record that depends on a market names its facts and their dates, and a trigger for review |
| W-07 | The first market shapes the core | The market guard (section 3a) |
| W-08 | Earlier work is lost or redone | The baseline is frozen and mapped (section 13); `HISTORY.md` |
| W-09 | The guard becomes ceremony | One field per record, and a script; people review only at levels 2 and 3 |
| W-10 | Over-correcting drops real constraints | General mechanisms with a precedent are allowed (section 3a) |
| W-11 | Scope balloons | Only the questions a subject needs, at framing; budgets and stop rules |
| W-12 | Spikes become the product | A separate repository, a timebox, and no promotion of their code |
| W-13 | Engineering decisions pass by silent veto | The window starts at the report; level 2 decisions get an independent review |
| W-14 | Copying Shopify's scale too early | A blog is one company's account; options that can grow, with stated triggers |
| W-15 | A record fixes a word's meaning without knowing its extent, decides beyond its limits, or rests on another record's wording | Terms and Scope in every record, checked at its level; the glossary; section 10's rule on what a record rests on (amendment 2) |
| W-16 | A message's wording is recorded in place of what it means | Each message from the founder is framed first, and the founder can correct the framing (section 3) |

## 12. Amendments

Each amendment is numbered and dated, gives its reason, and is approved by the founder.

### Amendment 1, 24 October 2026

**Approval.** The founder approved it with the plan of 24 October (`founder-messages/2026-10-24-approved-plan.md`).

**Reason.** Planning found five problems with version 1 as proposed (`b78686e`):
- it would have dropped the founder's guard against a market shaping the design;
- it contradicted the founder in three places;
- it left out the architecture description, the 34 areas, the milestone reports and a rule for spikes;
- it reversed three of the founder's earlier decisions without saying so;
- the founder's acceptance of 24 October added clarifications that it lacked.

**What it changes:**
- **1a. The market guard** (section 3a). It replaces three things:
  - "Yemen's conditions are drivers for every decision they touch" (section 5), and W-07's mitigation;
  - "Yemen's core flows" as the end (section 1);
  - "the rial by area" (section 14).
- **1b. Merchants are never asked** (section 5, step 2).
- **1c. Wording:** "first build" becomes "first version". "Build" means production code.
- **1d. The extent is the 34 areas,** and outside experience comes in at step 3 (section 5).
- **1e. Milestone reports** (section 4), and W-02's mitigation.
- **1f. Spikes, and the definition of ready for production code** (section 5).
- **1g. The architecture description is the outcome** (sections 1 and 4). `HISTORY.md`, the backlog and the reports are artifacts.
- **1h. Reversals of earlier founder decisions, made explicit** (sections 3, 7 and 13). The end check of the 179 questions and 81 rows is kept (section 8).
- **1i. A subject that waits only for the founder** doesn't block the next one's framing and evidence (section 5).

### Amendment 2, 24 October 2026

**Approval.** The founder approved 2a, 2b, 2c and 2e at 22:11 UTC, on the coordinator's framing of their concern, and gave 2d at 22:12 to 22:14 UTC (`founder-decisions.tsv`).

**Reason.** The founder's concern, framed:
- M1's records fix the meaning of words such as "payment method" and "provider" without establishing their extent from the platforms' own structures, though those structures are held. A record can then narrow an area it never examined. The founder's example was Shopify's payment settings.
- The records don't say where they stop, so what they leave to later subjects is not visible.
- Some records were drafted from other records' or drafts' wording rather than from evidence, so errors carried forward.

It asks each record to know its words and its boundary with work not yet done. It does not ask any record to decide more.

**What it changes:**
- **2a. Terms** in every record, entered in the glossary (sections 4, 5 and 6).
- **2b. Scope** in every record: what it decides, what it takes as given, and what it leaves open to which subject (sections 4, 5 and 6).
- **2c. What a record rests on:** evidence and accepted outcomes, never another record's or a draft's wording. A dependency on a proposed record is named, and gates acceptance (section 10).
- **2d. The founder's messages** are framed first, and the framing is recorded, not the message (section 3).
- **2e. M1's five records** get 2a to 2c in one pass of about 5 million agent tokens, before Decision 1 goes back to the founder. The pass neither broadens a decision nor starts another subject (section 14).
- Its practices are added to section 2, and its risks, W-15 and W-16, to section 11.

## 13. Where we start: the position on 24 October 2026

**The baseline** is `main` once amendment 1 is merged (milestone M0; `HISTORY.md`). Nothing is deleted.

**Settled, and still in force** (`founder-decisions.tsv`):
- **The guard on money:** no arrangement that holds sellers' money through Sharrwah goes live without the founder's decision (G1, 18 October).
- **Evidence that contains credentials, cookies or tokens** is read and cited like any other evidence (12 October).
- **What reaches the founder** is in plain words. Several decisions may come in one message, and each comes with a recommendation (G1).
- **The extent:** the 34 areas (18 and 19 October).
- **References:** Shopify and Salla are primary, and the others come in on demand (24 October).
- **No merchant interviews** (24 October).
- **Spikes are allowed.** Production code waits for the definition of ready (24 October).
- **The founder's decisions of 10 October,** restored from closed PR #3:
  - F-00: many markets, and Yemen first, not the design target;
  - F-01: no US ties;
  - F-05: the founder's words are attestations;
  - F-06: payments as their own concern.

**Open founder decisions:**
- **O-01:** which legal entity and domicile contracts with sellers and partners;
- **Decision 1's confirmation** (section 14);
- **the form of F-02** (the Sana'a zone first) **and F-03** (both zones), under the guard, at the markets and currency subject.

**Kept as evidence and inputs, not as deliverables:**
- **The pilot, S-01:** its decision entry (`studies/subjects/S-01/entry.md`), checked twice by an independent review, and its records.
- **Stage 1's Yemen facts,** and their digest (`studies/proposals/yemen-digest.md`).
- **The re-frame's records:** about 2,600 platform statements, each quoted from its source and checked by script.
- **The eight drafts** (`studies/proposals/drafts/`): their proposals are candidate options for the subjects.
- **What the checks found** (`studies/proposals/checks/R5/`). Each finding applies when a decision rests on that fact.
- **The frame and the payment seam of 10 October** (`8946887:method/frame.md`; `8946887:studies/payment-seam/seam.md`).
- **The Knowledge Map's questions** (`register/`), used as section 5 says.
- **Shopify's engineering sources** (`evidence/shopify-engineering/`).
- **The tools:** the quote checker, the record lookup and the corpus search.

**Not safe to rely on as they stand.** Each is checked when a decision rests on it:
- **The drafts' points:** about 3 in 10 of those checked say more than their source, and Q5 to Q8 are mostly unchecked.
- **Records that leave out a limit their source gives:** about 1 in 8 of those checked.
- **The Knowledge Map's Salla citations and pointers.** 46 of its 51 Salla evidence paths have moved, and its pointers date from 8 October.
- **The engineering sources:** they cover payments only, and 14 of the 37 are from before 2023.
- **The Q7 draft's currency table that holds two rials, and the seam's currency "edition" on every amount.** Both go against G1's B7.

**Stopped, and not resumed:**
- **The checks of everything the drafts cite:** 16 runs stopped by the usage limit, and 17 never started.
- **The planned review of the eight drafts as wholes,** and the separate company-decisions run. Their purposes move into the subjects.

**Founder decisions changed under this method:**
- **"The checks cover everything a proposal cites"** (18 October) is replaced by section 6's integrity levels.
- **"The drafts' citing counts are a guide"** (19 October) lapses, because the drafts are no longer deliverables.
- **The 2 billion token budget** stays as an upper bound. Each subject now has its own budget.
- **The deferral of the pilot's 14 decisions** is reopened, because the first subject brings them back as decision records.
- **"Every proposal for section B" being the founder's** (G1, 18 October). One-way decisions stay the founder's. Decisions that are cheap to undo are engineering's, with a veto (section 3).
- **"It doesn't stop … only if the re-sized whole would pass 2 billion"** (18 October) is replaced by section 7's rule 1.
- **Kept:** the end check of the 179 questions and the 81 payment rows (18 October), in section 8.

## 14. The first subject: the money boundary

The first subject is the pilot's own.
- **Decision 1, who holds sellers' money:** the founder confirms one line. "No sellers' money is held through Sharrwah at launch. A and B are reserved, not built. Switching either on stays yours."
  - The guard of 18 October already keeps A and B from going live without the founder. This line confirms what the record implies, and closes Decision 1.
  - It is a one-way door at level 3. Its checks cover only the facts it rests on.
- **The payment boundary** becomes an engineering record. It starts from the payment seam's contract, version 0 (`8946887:studies/payment-seam/seam.md`), after the guard test: the contract's currency "edition" on every amount gives way to G1's B7.
- **The seller ledger** records what is owed, and holds no money.
- **Decisions 2 to 12** become engineering records that follow from Decision 1.
- **Decision 13** (installments) is deferred, with the trigger "an installment provider is offered in a market Sharrwah serves".
- **Decision 14** (currency) moves to the markets and currency subject.
- **Three corrections come first.** The checks found that the facts behind Decision 1 need them:
  - the bar on payment companies crossing between Sana'a and Aden runs one way, not both;
  - Stripe's exclusion concerns businesses based in Yemen, not payments to or from it;
  - YK-131 says more than its quotes on one of its wallets (`studies/proposals/checks/R5/yemen/yemen-2.tsv`).
- **Budget:** about 20 million agent tokens, with no more than 2 tasks at a time.
- **Terms and scope** (amendment 2e): before Decision 1 goes back to the founder, the subject's records get their Terms and Scope, in one pass of about 5 million agent tokens. The pass neither broadens a decision nor starts another subject.
- **Output:** the founder's line, the subject's decision records, and the milestone report.

**The subjects after it** are in `decisions/subjects.tsv`, in order of risk. Each is confirmed at its framing, and none starts before the one before it closes, except as section 5 allows.
1. **The spine:**
   - the capability map from Shopify's and Salla's own structures, after a feasibility test;
   - the system context, the quality scenarios, the constraints and a glossary (arc42 sections 1 to 3, 10 and 12).
2. **Tenancy, identity and permissions.**
3. **Markets and currency, as configuration.**
4. **Core commerce, and how it divides into modules.**
5. **Apps, events and webhooks.**
6. **Seller conditions and payment methods.**
7. **The company and compliance:** founder decisions, with one lawyer consultation. Their result is configuration: a contracting company per market.
8. **Evaluation:** the walkthrough, the reconciliation, and the first full architecture description.

The areas these leave out, such as the storefront, sales channels, B2B, analytics, partners and AI, have rows in the backlog. Their order is set at the spine.

## References

- Anderson, D. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business.* Blue Hole Press.
- arc42, the template for architecture documentation: https://arc42.org
- Bezos, J. (2016). *2015 Letter to Shareholders* (Type 1 and Type 2 decisions).
- Boehm, B. (1988). A Spiral Model of Software Development and Enhancement. *IEEE Computer* 21(5).
- Boehm, B. (1996). Anchoring the Software Process. *IEEE Software* 13(4).
- Cervantes, H., Kazman, R. (2016). *Designing Software Architectures: A Practical Approach.* Addison-Wesley (Attribute-Driven Design 3.0).
- Clements, P., Northrop, L. (2001). *Software Product Lines: Practices and Patterns.* Addison-Wesley.
- Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Addison-Wesley (the ubiquitous language).
- Fairbanks, G. (2010). *Just Enough Software Architecture: A Risk-Driven Approach.* Marshall & Brainerd. Summary: "A Risk-Driven Model for Agile Software Architecture", *Methods & Tools*, https://www.methodsandtools.com/archive/agilearchi.html
- IEEE 1012, *Standard for System, Software, and Hardware Verification and Validation* (integrity levels).
- IEEE 828, *Standard for Configuration Management in Systems and Software Engineering.*
- ISO 31000:2018, *Risk management: Guidelines.*
- ISO/IEC/IEEE 29148:2018, *Requirements engineering* (traceability; stakeholder needs and requirements).
- ISO/IEC/IEEE 42010:2022, *Architecture description.*
- Kazman, R., Klein, M., Clements, P. (2000). *ATAM: Method for Architecture Evaluation.* CMU/SEI-2000-TR-004.
- Lago, P., van Vliet, H. (2005). Explicit Assumptions Enrich Architectural Models. *Proceedings of the 27th International Conference on Software Engineering (ICSE 2005),* pp. 206–214.
- MADR, *Markdown Architectural Decision Records,* version 4: https://adr.github.io/madr/
- Nygard, M. (2011). Documenting Architecture Decisions: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Parnas, D. (1972). On the Criteria To Be Used in Decomposing Systems into Modules. *Communications of the ACM* 15(12).
- Pohl, K., Böckle, G., van der Linden, F. (2005). *Software Product Line Engineering: Foundations, Principles and Techniques.* Springer.
- Poppendieck, M. and T. (2003). *Lean Software Development: An Agile Toolkit.* Addison-Wesley.
- Tyree, J., Akerman, A. (2005). Architecture Decisions: Demystifying Architecture. *IEEE Software* 22(2), pp. 19–27 (assumptions, implications and related decisions).
- Zave, P., Jackson, M. (1997). Four Dark Corners of Requirements Engineering. *ACM Transactions on Software Engineering and Methodology* 6(1).
- Zimmermann, O. (2020). A Definition of Done for Architectural Decision Making (ecADR): https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
- Zimmermann, O. (2023). A Definition of Ready for Architectural Decisions (START): https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
