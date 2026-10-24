# Sharrwah design method, version 1

**Status: proposed on 24 October 2026, for the founder's acceptance.** Once accepted, this document governs the work. `PLAN.md` stays as the history of how we got here and is no longer followed. This document changes only by a numbered amendment (section 12).

## 1. What the work must produce

The work ends when Sharrwah's first build, with Yemen as its first market, has:
1. **A decision record for every decision on the build's critical path,** each one accepted, deferred with a stated trigger, or superseded (section 4).
2. **An answer from the founder to every founder decision** (section 3), or a deferral with a trigger.
3. **A risk register** in which every high risk is mitigated, accepted by its owner, or closed.
4. **A walkthrough of Yemen's core flows** against the accepted decisions, with no gap and no clash left open (section 8).

This is the "life cycle architecture" milestone of Boehm's spiral model (1996), in plain terms: the design is defined, its major risks are resolved, and the people who decide have committed to it. It is not code. The build comes after, when and as the founder decides.

## 2. The practices this method is built from

Each part of the method is an established practice, not one invented here. When a new problem appears, it is handled by one of these practices. No new rule or step is added without an amendment (section 12).

| Practice | Source | What it does here |
| --- | --- | --- |
| Risk-driven design | Fairbanks 2010; Boehm 1988 | Effort goes only where a wrong choice would hurt. Each subject stops when its risks are reduced enough, not when every fact is checked. |
| Decision records | Nygard 2011; MADR 4 | One short record per decision: context, options, evidence, outcome, consequences, status. |
| Ready and done checks for a decision | Zimmermann: START and ecADR | A decision is taken only when it is ready, and is closed only when it meets the done checklist. |
| One-way and two-way doors | Bezos, 2015 letter to shareholders | Decisions that are hard to undo go to the founder. Decisions that are cheap to undo are made quickly by engineering. |
| Integrity levels | IEEE 1012 | Verification effort scales with the consequence of being wrong, not uniformly. |
| Quality-attribute scenarios | ATAM, SEI 2000 | The design is judged by concrete scenarios with expected outcomes, walked through the decisions. |
| Last responsible moment | Poppendieck 2003 | No decision and no document before it is needed. |
| Limits on work in progress | Anderson 2010 (Kanban) | Few tasks at a time, each finished before more start. |
| Traceability and change control | ISO/IEC/IEEE 29148; IEEE 828 | Each decision lists the evidence it rests on, so a change in evidence shows which decisions it reopens. |
| Risk register | ISO 31000 | Each risk has an owner, a mitigation and a status. |

## 3. Who decides what

There are three kinds of question. Each has one owner.

| Kind | Test | Owner | How it is settled |
| --- | --- | --- | --- |
| **A fact** | "What is true?": what a platform does, or what Yemen's rules or market allow | Engineering investigation | By evidence. Never put to the founder. |
| **A founder decision** | "What do we want, and what risk do we accept?", where the answer has business, legal or money consequences and is hard to undo (a one-way door) | The founder | Given as one page: the question, the options, what the evidence shows, the risks and a recommendation. The founder answers or defers with a trigger. |
| **An engineering decision** | "How do we build it?", where the answer is cheap to change later (a two-way door) | The coordinator, as engineering lead | A decision record with its reasons. It stands unless the founder vetoes it within two days of seeing it. |

**Founder decisions** include whether Sharrwah ever holds sellers' money, which markets it enters and when, where the company is based and which company contracts with sellers, which payment providers and partners it contracts with, who may register as a seller, Sharrwah's pricing model, and the budget and risk appetite of the work.

**Engineering decisions** include the data model, the level at which each setting lives, the interfaces between parts, naming, and build order.

Agents investigate and check. They never decide.

## 4. The artifacts: only these

1. **Decision records,** one file each in `decisions/`, in MADR's short form, with these fields added:
   - door: one-way or two-way;
   - integrity level: 1, 2 or 3 (section 6);
   - the risks it addresses, by id;
   - the evidence it rests on, by id;
   - status: `proposed`, `accepted`, `deferred` (with its trigger), `under review` (its evidence changed) or `superseded by` another record.
2. **The risk register,** `risks.tsv`: id, risk, likelihood, impact, mitigation, owner, status (open, mitigated, accepted, closed), trigger, and the decisions it links to.
3. **The evidence base:** `evidence/` and `studies/` as they stand at the baseline commit (section 13). It is frozen. New evidence is added only by an investigation for a named decision (section 5, step 2), with its source and date.
4. **`STATE.md`,** one page: the current subject and step, the tasks in flight, the budget used, what is blocked, and the next step. A script lists every decision by status, so what is settled, open or reopened is always visible.

Briefs, check sheets and notes are working material for a task, made only when the task needs them. They are never deliverables.

## 5. How work is organized: one subject at a time

A **subject** is one decision area on the first build's critical path, small enough to finish in about a day. Subjects run one at a time, depth-first. A subject starts only when the one before it has closed.

**The references:**
- **Shopify and Salla are the primary references.** Shopify is the most mature global model. Salla is the regional, Arabic model closest to how selling and paying work in Yemen's neighbourhood: cash on delivery, local wallets and banks.
- **Zid, WooCommerce and BigCommerce come in only when a decision needs them:** when Shopify and Salla are both silent on something a decision turns on, or disagree. Their records are already held, so bringing them in is a lookup, not new research.
- **The references supply options, not answers.** None of them serves Yemen. Yemen's conditions are drivers for every decision they touch.

**The steps of a subject:**
1. **Frame** (about two hours).
   - List the subject's decisions, each as a draft record, and check each one is ready (Zimmermann's START: stakeholders known, the time is right, at least two options, the criteria are known, the template is chosen). Decisions that aren't needed yet are deferred with a trigger.
   - Mark each decision's door and integrity level, link its risks, and set the subject's budget.
2. **Evidence** (timeboxed).
   - Take what each decision turns on from the held records, Shopify and Salla first, and Yemen's facts from the Stage 1 digest.
   - Where something is missing, run one investigation with a stated question, a timebox and a budget. Prefer asking a provider, a merchant or a lawyer over reading more documents.
3. **Propose.** Each record states:
   - at least two options, compared against the decision's drivers;
   - the evidence, by id, with each fact's conditions (plan, country, product, store, date) written out;
   - the consequences, including what would have to change if the decision were reversed;
   - the recommendation.
4. **Verify,** at the decision's integrity level (section 6).
5. **Decide.** The founder answers founder decisions. Engineering decisions stand after the two-day veto window.
6. **Close.**
   - Walk the subject's scenarios through the accepted decisions (section 8).
   - Update the risk register, mark the subject closed in `STATE.md`, and record its cost against its budget.

## 6. How much checking each decision gets

Following IEEE 1012, checking scales with what a wrong decision would cost. It covers **only the facts a decision rests on,** never everything a document mentions.

| Level | Which decisions | Checking |
| --- | --- | --- |
| **3** | One-way doors: money, legal structure, licensing, sanctions | Every fact the decision rests on is checked against its source by someone who didn't write the record (an independent agent), including the conditions the source puts on it. Quotes are checked by script. The scenario walkthrough must pass. |
| **2** | Engineering decisions that are expensive to change: the core data model, the money ledger | The facts it rests on are checked by script for their quotes, and by the coordinator for their conditions. One independent agent reviews the record. |
| **1** | Engineering decisions that are cheap to change | Quotes are checked by script. Nothing else. |

A record is **done** when it passes Zimmermann's ecADR checklist:
- **E:** we are confident enough that it will work;
- **C:** at least two options were compared against the criteria;
- **A:** the people who must agree have agreed: the founder for founder decisions, the veto window for the others;
- **D:** it is recorded and shared;
- **R:** we know when it will be built, how it will be confirmed, and when it will be reviewed.

## 7. Limits and stop rules

These keep the plan bounded. They are the only stop rules.
1. **A budget per subject,** set at framing. If a subject reaches its budget plus a quarter, work stops and the coordinator reports to the founder before going on.
2. **Sample before scaling.** Any check of more than 10 items is first run on 5. If 2 or more of the 5 fail, the check stops and the step that produced the fault is fixed first.
3. **Stop on risk, not on completeness.** A subject's investigation stops when its decisions meet the ecADR "E" (confident enough), not when every fact has been checked (Fairbanks: effort in proportion to risk).
4. **At most 2 agent tasks at a time.** A task starts only if it can finish within the usage window that remains. A task that is stopped is started again on what it has left, not resumed with its old context.
5. **No new layers.** A new concern goes into the risk register, and an existing practice handles it. Changing the method needs an amendment.

## 8. How the design is judged

- **Each decision record:**
  - it passes the ready check before it is taken, and the done check after;
  - every evidence id resolves and every quote is found word for word (by script);
  - at levels 2 and 3, every fact it rests on is written with the conditions its source gives.
- **Each subject:** it passes its scenarios. A scenario follows ATAM's form: a stimulus (something happens), the environment (where and when), the expected response, and how we know. The subject passes when every scenario can be answered from the accepted decisions alone. One example: "A buyer in Aden orders and pays cash on delivery. The courier collects the cash and pays the seller; Sharrwah bills its own fee apart; at no point does Sharrwah hold the money."
- **The whole:** the outcome in section 1.

## 9. Resuming and recovering

- **The durable state is three files:** the decision records, the risk register and `STATE.md`. A coordinator resumes by reading this document, then `STATE.md`, then the records of the open subject. Nothing else is needed to know what is settled, open or reopened.
- **Each task** has a stated output and a definition of done, and writes its output as it goes. It is committed when it ends.
- **After an interruption,** finished outputs stand, and unfinished tasks are rerun on what they have left.

## 10. Change control

- **A decision changes only through a new record that supersedes it.** Both records link to each other, and the old one is never edited.
- **When evidence changes** (a new capture, a correction), a script lists the records that cite it. They become `under review` and are verified again at their own level.
- **A founder decision changes only by the founder.**
- **This method changes only by amendment** (section 12).

## 11. Risks of the work itself

These open the risk register.

| Id | Risk | Mitigation |
| --- | --- | --- |
| W-01 | Research grows without end | Risk-driven stop; investigations timeboxed; a budget per subject |
| W-02 | The founder is asked too much, or can't follow | Only one-way doors go to the founder, each on one page, in plain words |
| W-03 | The plan keeps being rewritten | This document changes only by amendment; decisions are superseded, never rewritten |
| W-04 | Agents misread or over-generalize a source | Level-scaled checks on the facts decisions rest on; quotes by script; conditions written out |
| W-05 | Usage limits stop work in flight | Small tasks, at most 2 at a time, fresh restarts |
| W-06 | Yemen's facts change (two central banks, sanctions, rates) | Each Yemen-dependent record names its facts and their dates, and a trigger for review |
| W-07 | The references don't fit Yemen | Yemen's conditions are drivers for every decision; references supply options only |
| W-08 | Earlier work is lost or redone | The baseline is frozen and mapped (section 13) |

## 12. Amendments

None yet. Each amendment is numbered and dated, gives its reason, and is approved by the founder.

## 13. Where we start: the position on 24 October 2026

**Baseline.** The repository at the commit that adds this document. Nothing is deleted.

**Settled, and still in force:**
- **The guard:** no arrangement that holds sellers' money through Sharrwah goes live without the founder's decision (G1, 18 October).
- **Evidence that contains credentials, cookies or tokens** is read and cited like any other evidence (12 October).
- **What reaches the founder** is in plain words, several decisions may come in one message, and each comes with a recommendation (G1).

**Kept as evidence and inputs, not as deliverables:**
- **The pilot, S-01:** its decision entry (`studies/subjects/S-01/entry.md`), checked twice by an independent review, and its records.
- **Stage 1's Yemen facts** and their digest (`studies/proposals/yemen-digest.md`).
- **The re-frame's records:** about 2,600 platform statements, each quoted from its source and checked by script.
- **The eight drafts** (`studies/proposals/drafts/`): their proposals are candidate options for the subjects.
- **What the checks found:** the platform facts behind Q1 to Q4, the first part of the Yemen facts, and what Yemen's evidence doesn't show (`studies/proposals/checks/R5/`). Each finding applies when a decision rests on that fact.
- **The tools:** the quote checker, the record lookup and the corpus search.

**Stopped, and not resumed:**
- **The checks of everything the drafts cite:** 16 runs stopped by the usage limit, and 17 never started.
- **The planned review of the eight drafts as wholes,** and the separate company-decisions run. Their purposes move into the subjects.

**Founder decisions to revisit under this method:**
- **"The checks cover everything a proposal cites"** (18 October) is replaced by section 6's integrity levels.
- **"The drafts' citing counts are a guide"** (19 October) lapses, because the drafts are no longer deliverables.
- **The 2 billion token budget** stays as an upper bound. Each subject now has its own budget.
- **The deferral of the pilot's 14 decisions** is reopened, because the first subject brings them back as decision records.

## 14. The first subject: the money flow

The first subject is the pilot's own, because it holds the one founder decision about Yemen that is needed first.
- **Decision 1** of the pilot's entry, who holds sellers' money between the buyer's payment and the payout, becomes a founder decision. It is a one-way door at level 3, with the entry's options A, B and C and its recommendation (C: each payment provider holds the money in the seller's own account with it; Sharrwah holds none, behind one interface that can carry A or B later).
- **Decisions 2 to 12** become engineering records that follow from the founder's answer.
- **Decision 13** (installments) is deferred, with the trigger "an installment provider is offered in Yemen".
- **Decision 14** (currency) moves to the markets and currency subject.
- **The checks behind Decision 1** cover only the facts it rests on. The checks already found two that must be corrected first:
  - the bar on payment companies crossing between Sana'a and Aden runs one way, not both;
  - Stripe's exclusion concerns businesses based in Yemen, not payments to or from it.
- **Budget:** about 20 million agent tokens, with no more than 2 tasks at a time.
- **Output:** one page for the founder on Decision 1, and the subject's decision records.

**The subjects after it,** in order of risk. They are confirmed at each subject's framing, and none starts before the one before it closes:
1. payment methods for Yemen (cash on delivery, wallets, bank transfer) and how providers plug in;
2. markets and currency, including the rial by area;
3. sellers: who may register, and what is checked before a store sells or takes payment;
4. compliance and the company: sanctions screening, licensing and the legal entity, as founder decisions with a lawyer.

## References

- Anderson, D. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business.* Blue Hole Press.
- Bezos, J. (2016). *2015 Letter to Shareholders* (Type 1 and Type 2 decisions).
- Boehm, B. (1988). A Spiral Model of Software Development and Enhancement. *IEEE Computer* 21(5).
- Boehm, B. (1996). Anchoring the Software Process. *IEEE Software* 13(4).
- Fairbanks, G. (2010). *Just Enough Software Architecture: A Risk-Driven Approach.* Marshall & Brainerd. Summary: "A Risk-Driven Model for Agile Software Architecture", *Methods & Tools*, https://www.methodsandtools.com/archive/agilearchi.html
- IEEE 1012, *Standard for System, Software, and Hardware Verification and Validation* (integrity levels).
- IEEE 828, *Standard for Configuration Management in Systems and Software Engineering.*
- ISO 31000:2018, *Risk management: Guidelines.*
- ISO/IEC/IEEE 29148:2018, *Requirements engineering* (traceability).
- ISO/IEC/IEEE 42010:2022, *Architecture description* (decisions and rationale).
- Kazman, R., Klein, M., Clements, P. (2000). *ATAM: Method for Architecture Evaluation.* CMU/SEI-2000-TR-004.
- MADR, *Markdown Architectural Decision Records,* version 4: https://adr.github.io/madr/
- Nygard, M. (2011). Documenting Architecture Decisions: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Poppendieck, M. and T. (2003). *Lean Software Development: An Agile Toolkit.* Addison-Wesley.
- Zimmermann, O. (2020). A Definition of Done for Architectural Decision Making (ecADR): https://ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html
- Zimmermann, O. (2023). A Definition of Ready for Architectural Decisions (START): https://ozimmer.ch/practices/2023/12/01/ADDefinitionOfReady.html
