**The plan the founder approved on 24 October 2026,** in planning mode, at about 20:30 UTC. The coordinating session wrote it after its own reading and an independent architect's review of the same files. It is copied as approved. Amendment 1 to `METHOD.md` carries it out. The founder's messages of that day are in `2026-10-24-method-accepted.md`.

---

# Plan: adopt the method, close the record's gaps, then work subject by subject

## Context

On 24 October the founder accepted `METHOD.md`, with three clarifications:
- a report at each milestone and planned pause;
- spikes are allowed, but production code waits for documented requirements and architecture;
- the Knowledge Map is assessed and used only where it helps.

PR #4 is merged into `main` (`a05974a`), with nothing rewritten. `HISTORY.md` indexes the baselines by commit; this session's proxy refuses tag pushes. Closed PR #3 is kept in the history (`968cc8a`) without its files.

This plan comes from my own reading, checked against an independent architect's review of the same files. Every finding below was checked against its file.

**Already done:** the scheduled check-in is turned off: disabled, not deleted, so it can be switched back on. Its prompt would have resumed stopped agents and the R5 checks the method stopped. It last fired at 20:09 UTC, and I took no action then.

## What planning found

1. **`METHOD.md` would quietly drop the founder's guard.** It retires `PLAN.md`, and with it these lines:
   - "Yemen is the first market, not the design target" (`PLAN.md`:9);
   - one platform for many markets (`PLAN.md`:20–21);
   - "Yemen's evidence is read after the design sections are written" (`PLAN.md`:617).

   And it says the opposite in four places:
   - "Yemen's conditions are drivers for every decision" (:69, and W-07 at :148);
   - success measured as "Yemen's core flows" (:11);
   - a subject on "the rial by area" (:199).

   Your G1 answer already said "Rules land as availability, not as design" and "The rial's two editions are not part of the core" (`g1-answer.md`:28, :33). Yet the Q7 draft keeps the currency table able to hold two rials (`drafts/Q7/draft.md`:127), and PR #3's seam puts a currency "edition" on every amount.
2. **The guard you asked for was built on 10 October and lost with PR #3.** `8946887:method/frame.md` types every outcome:
   - **Built:** decided by engineering, the same for every market;
   - **Configured:** set per market or plan;
   - **Chosen:** set by the merchant;
   - **Context:** law, providers, the market.

   Its rule: "Volatile Context may feed Configured outcomes, never Built ones: build for the range, configure the value." It comes from product-line engineering, from requirements engineering's assumptions about the world, and from information hiding.
3. **Your first decisions dropped out of the record.** PR #3 (`8946887:decisions/founder.md`) holds F-00 to F-06 and the open question O-01: "Which legal entity and domicile contracts with sellers and partners?" This is the Oman question.
   - Only F-00 and F-05 survive today, in other words.
   - F-01 (no US ties), F-02 (Sana'a zone first), F-03 (both zones modelled), F-06 (payments behind a contract) and O-01 appear nowhere.
   - F-02 and F-03 are shaped by Yemen, so they get the guard test, not a quiet revival.
4. **Decision 1 is deferred on record, but your sense of it is right in substance.**
   - G1 deferred Decisions 1 to 14, and set the guard: nothing that holds sellers' money goes live without you.
   - That guard already covers the one-way part, A or B going live. What remains is one line for you to confirm, and an engineering boundary.
   - The boundary already exists twice: as the pilot's recommendation C, and as PR #3's "contract, version 0".
5. **Changes to earlier founder decisions that `METHOD.md` §13 doesn't list:**
   - at G1, every proposal for section B was yours (`g1-answer.md`:76); the method makes cheap-to-undo ones engineering's;
   - the overrun rule changed: from "re-size and tell", to stopping at budget plus a quarter (`founder-decisions.tsv`:14);
   - your decision to check the 179 questions and the 81 payment rows at the end (`founder-decisions.tsv`:17) was dropped.
6. **Scope:**
   - the method's subjects are money, payment methods, markets, sellers and compliance. Tenancy, roles, catalogue and orders, apps, events and webhooks are missing;
   - it never mentions the 34 areas you decided are the full extent (`founder-decisions.tsv`:16, :19);
   - nothing turns the 34 areas into a map of what the first version must cover.
7. **There's no architecture description, no milestone report and no rule for spikes.**
   - §1 and §4 ("only these" artifacts) leave no room for an arc42 description;
   - `HISTORY.md` promises milestone reports that `METHOD.md` doesn't define;
   - "It is not code" predates your clarification about spikes.
8. **Five overlapping question sets, and no single backlog:**
   - the 652 concerns;
   - the 179 Knowledge Map questions;
   - the 81 payment rows;
   - the 8 re-frame questions;
   - S-01's 14 decisions.

   So progress can't be measured.
9. **Not safe to rely on as they stand:**
   - **The drafts.** About 3 in 10 of their checked points claim more than their source, and Q5 to Q8 are mostly unchecked.
   - **Decision 1's evidence** needs three fixes:
     - the Sana'a and Aden bar runs one way;
     - Stripe's exclusion concerns businesses based in Yemen;
     - YK-131 says more than its quotes (`R5/yemen/yemen-2.tsv`:7).
   - **The engineering sources** cover payments only, and 14 of their 37 are from before 2023.
   - **`CLAUDE.md` and `STATE.md`** still point to `PLAN.md` and to resuming old agents (`STATE.md`:452–457).
10. **Already held, and unused:**
    - Shopify's engineering talks and posts in `evidence/shopify-engineering/`: pods (E024), Packwerk (E016, E018–E022), Functions and payment apps (E027, E030–E036);
    - the drafts, which already confine Yemen to their section 6;
    - the pilot's table of options and consequences;
    - `studies/proposals/areas/areas.tsv`.

## The Knowledge Map

- **Where it comes from:**
  - your page, data as of 8 October, made before this repository;
  - copied on 12 October, byte-identical to the live page;
  - its own method was never run.
- **Still valuable:**
  - **The architecture questions found nowhere else:**
    - tenancy and the engineering set ENG-01 to ENG-08;
    - authorization (STF-07), app isolation (APP-06) and events and webhooks (API-02);
    - account and store structure (ACC-01, ACC-05).
  - **Its kinds of question.** "World: what fills a slot … it does not define the product" is the guard in one line.
  - **Its timing** (`needed_by`) and risk.
  - **Its source types:** what each kind of source is good for, what it can't tell you, and how to grade it. This is the rule for "buying architectural intelligence".
- **Needs updating, only when used:**
  - **Its Salla citations.** 46 of its 51 Salla evidence paths no longer exist, because observed-sa was reorganized: `salla/api.salla.dev/organizes/dashboard-nav/` is now `structures/salla/dashboard-nav/`. As a result, 130 of its 153 questions with evidence cite a broken Salla path.
  - **Its Shopify citations.** All 145 paths still exist, but none is pinned to a commit.
  - **Its pointers** date from 8 October.
  - **Rows that clash with later decisions:**
    - rows assuming Saudi rules (SAMA, ZATCA, PDPL);
    - seven rows naming merchants as a source;
    - "a walking skeleton" and "build slice";
    - "ADRs owned by the founder";
    - MTH-04, already answered.
- **How it informs the work without delaying it:**
  - at each subject's framing, a script pulls that subject's high-risk rows needed for the spine or the model;
  - each gets one disposition: answered by a record, a driver, a scenario, or deferred with a trigger;
  - a pointer is repaired only when its row is used;
  - the end reconciliation you chose stays (M8);
  - it costs minutes per subject. No bulk re-check, and no rebuild of the page.

## The route

Each milestone is one pull request, closed by a short report. It is merged with a merge commit and gets a row in `HISTORY.md`. A milestone with a one-way founder decision waits for your answer. Others merge when the report is sent, and the veto window starts then.

| Milestone | What | Exit | What you get |
| --- | --- | --- | --- |
| **M0. Re-baseline.** Half a day, no agents. | Amendment 1 (below); the record repaired (list below) | The scheduled check-in is off; `METHOD.md` is adopted; your 24 October decisions and F-00 to O-01 are recorded; `STATE.md` fits on one page; `risks.tsv` and the backlog exist | One page with answer lines: the restored decisions, and how F-02 and F-03 are handled |
| **M1. The money boundary.** About a day, 20 million agent tokens. | The three evidence fixes first. Then the payment boundary as an engineering record: PR #3's contract v0 after the guard test. Also a seller ledger that records and holds nothing, and Decisions 2 to 12 as records. 13 is deferred with its trigger; 14 moves to markets. | Done checks met; the scenarios pass from the records alone | One line to confirm: "No sellers' money is held through Sharrwah at launch. A and B are reserved, not built. Switching either on stays yours." |
| **M2. The spine.** One to two days. | A feasibility test first, read-only, about an hour: do Shopify's structures (schema, permission tree, roles, events, navigation) and Salla's join by area? Then the capability map (the 34 areas: capabilities, roles, interactions), using the commonality rule of KM-MTH-01. Also the system context, quality scenarios (KM-ENG-02), constraints and a starting glossary. | arc42 sections 1 to 3, 10 and 12 | What the first version covers first, by area (an order, not a cut), and the business targets for the quality scenarios |
| **M3 to M7.** One subject each, in order of risk, each confirmed at its framing. | (1) Tenancy, identity and permissions. (2) Markets and currency as configuration. (3) Core commerce and how it divides into modules. (4) Apps, events and webhooks. (5) Seller conditions and payment methods. | Method §5 step 6, the guard check, and the arc42 sections each fills | The engineering decisions, with the veto window; one-way decisions, each on one page |
| **Last subject.** | Company and compliance, with one lawyer consultation. These are founder decisions whose result is configuration: a contracting company per market. | Answered, or deferred with a trigger | One page per decision |
| **M8. Evaluation.** One to two days. | A walkthrough of the scenarios; the 179 questions and 81 rows reconciled; the first full architecture description (arc42's 12 sections, with what ISO 42010 requires: stakeholders and concerns, views, traceability and decisions) | The life-cycle architecture milestone | The go or no-go on production code, part by part |

**Rough size:** about 0.3 billion agent tokens to M8, give or take half, over two to three weeks of work. Each subject's budget is fixed at its framing, and the stop rules apply.

### M0's repairs

1. **`METHOD.md`:** status set to adopted, with amendment 1.
2. **`founder-decisions.tsv`:**
   - your 24 October acceptance and clarifications, with the message saved as `founder-messages/2026-10-24-method-accepted.md`;
   - F-00 to F-06 and O-01, restored from `8946887`, each marked: in force, revoked (F-04), open (O-01), or to be tested against the guard (F-02, F-03).
3. **`decisions/`:**
   - `README.md`: the record template, MADR plus door, integrity level, outcome type, risks, evidence and status;
   - `subjects.tsv`: the one backlog. Each row has the area, the question ids it covers, door, risk, needed-by, the arc42 section and status.
4. **`risks.tsv`:** W-01 to W-08 (W-07 reworded), the route's risks (below), and the open findings.
5. **`STATE.md`:** one page. **`PLAN.md`** gets a dated §11 entry saying it is superseded and kept as the record.
6. **`CLAUDE.md` and `README.md`:**
   - read first `METHOD.md`, `STATE.md`, `founder-decisions.tsv` and `HISTORY.md`;
   - the method changes only by amendment.
7. **The register:**
   - disposition columns added to `km-questions.tsv`, and the selection script;
   - the provenance and staleness notes added to `register/README.md`.
8. **The scheduled check-in:** now off. Its prompt is rewritten to §9, and it is turned back on only while tasks run.
9. **`reports/M0.md`** and its pull request.

## Amendment 1 to `METHOD.md`

- **1a. The market guard:**
  - every record states its outcome type (Built, Configured, Chosen or Context) and, if it varies, what by;
  - no market's name appears in anything Built, and a script checks this;
  - drafts start from the references, and Yemen then tests them;
  - a market's facts are Context: they set Configured values, or turn a Built outcome into a Configured one, and never shape a Built outcome;
  - general mechanisms that have a precedent stay allowed: cash on delivery, long-pending payments, courier cash custody;
  - a record that fails goes to you;
  - subjects that touch money, markets, sellers or the company run three change scenarios: a second market whose processor holds funds; the company based in Oman; and Yemen dropped;
  - this carries `PLAN.md`'s principles and G1's B1, B2 and B7 into the method, and replaces :11, :69, :148 and :199.
- **1b. Investigations** ask providers, lawyers or official sources. Never merchants.
- **1c. Words:** "first build" becomes "first version". "Build" means production code.
- **1d. The extent and outside experience:**
  - the extent is the 34 areas;
  - at step 3, options come first from Shopify and Salla, then from established designs and engineering writing, typed by the Knowledge Map's source types. This is Attribute-Driven Design's "choose design concepts" (SEI);
  - open-source platforms are used only where they fit, and Medusa, Saleor and Vendure don't fit tenancy;
  - each subject adds outside sources for what it needs, for example webhooks and the app platform.
- **1e. Milestone reports,** at most two pages, set out:
  - what is settled, open or invalidated;
  - the engineering decisions, with the veto window starting at the report;
  - any exceptions to the guard;
  - the top risks;
  - cost against budget;
  - what is needed from you.
- **1f. Spikes:**
  - throwaway code that answers one stated question, in a separate repository, within a timebox;
  - it counts as evidence;
  - its code is never promoted.
- **1g. Outcome and artifacts:**
  - the outcome is an architecture description in arc42's shape that meets ISO 42010, with the decision records as its section 9;
  - `HISTORY.md`, `decisions/subjects.tsv` and the reports are added.
- **1h. Reversals made explicit:**
  - cheap-to-undo decisions are engineering's, shown in reports with a veto (this replaces G1's "every proposal for section B is mine");
  - the overrun rule is now "stop at budget plus a quarter";
  - the end check of the 179 questions and 81 rows is kept.
- **1i. No stall:** a subject waiting only for your answer doesn't block the next subject's framing and evidence steps.

## Definition of ready for production code, per part

1. Its decisions are accepted, and your decisions on it answered.
2. Its parts, interfaces and data are in the architecture description, in glossary terms.
3. Its quality scenarios are measurable, and acceptance tests come from them and from captured platform journeys (KM-ENG-06).
4. Its high risks are mitigated or accepted, and the guard passes.
5. Its security and tenant-isolation tests are specified.
6. Its spikes are closed.
7. It has had an independent review at its integrity level, and you have seen it in a report.

## Risks of the route

| Risk | Mitigation |
| --- | --- |
| The guard becomes ceremony | One field per record, and a script; people review only at levels 2 and 3 |
| Over-correction drops real constraints | General mechanisms with a precedent are allowed (1a) |
| Scope balloons | Only high-risk rows needed for the spine or the model are admitted; budgets and stop rules |
| Spikes become the product | A separate repository, a timebox, and no promotion |
| Engineering decisions pass by silent veto | The window starts at the report; level 2 decisions get an independent review |
| Copying Shopify's scale too early | Blogs are one company's account; options that can grow, with stated triggers |

## Files

**Change:**
- `METHOD.md`, `STATE.md`, `founder-decisions.tsv`, `PLAN.md` §11, `CLAUDE.md`, `README.md`, `HISTORY.md`;
- `register/km-questions.tsv`, `register/README.md`.

**New:**
- `founder-messages/2026-10-24-method-accepted.md`;
- `decisions/README.md`, `decisions/subjects.tsv`;
- `risks.tsv`, `reports/M0.md`;
- `method/decision_status.py` (the guard check and status lists);
- `method/km_select.py`.

**Reuse:**
- `method/quote_check.py`, `record_ids.py`, `corpus_search.py`, `source_kinds.py`, `yemen_digest.py` and `count_tokens.py`.

## Verification

- **M0:**
  - the check-in shows as off;
  - `decision_status.py` lists every backlog row;
  - each restored decision cites `8946887:decisions/founder.md`;
  - `km_select.py` returns M1's rows;
  - the links in `HISTORY.md` and `README.md` resolve;
  - `git diff --stat` touches only the files above.
- **The guard:**
  - the script flags any Built record that names a market, or whose evidence is only one market's Context;
  - run on today's drafts, it should flag the Q7 two-rial line.
- **Every milestone:**
  - the report's numbers come from scripts;
  - the pull request is merged with a merge commit and recorded in `HISTORY.md`.
