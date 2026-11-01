# Plan: building Sharrwah

**What this is.** The engineering plan for Sharrwah, a merchant platform for many markets built on Shopify's model (the founder's decision of 1 November 2026). It sets out:
- how the work is done, and in what order;
- what each stage delivers, and when it is accepted;
- how risks and the founder's decisions are handled;
- how progress stays visible.

The current stage is planned in detail. Later stages stay in outline until they start (rolling-wave planning, PMI 2017).

## 1. The method

Each practice does one job:
- **Product line engineering** (Pohl, Böckle and van der Linden 2005). The platform is built once, with a *variation point*, a place built to take different values, wherever markets differ. Each market is then set up by filling those places. No market shapes the platform before its own setup stage.
- **A reference architecture.** Shopify's model is the reference. Sharrwah adopts Shopify's shape unless a concrete case proves that Shopify's model can't represent something Sharrwah needs now. A departure carries that proof in its decision record.
- **Requirements as measurable scenarios** (Bass, Clements and Kazman 2012; ISO/IEC 25010:2023). Each scenario states what the platform must do and how well.
- **Attribute-driven design** (Cervantes and Kazman 2016). The architecture is designed in iterations, each driven by the requirements and risks that matter most at that point.
- **Architecture decision records** (Nygard 2011). One page per decision: its context, Shopify's shape with its evidence, the decision, its consequences, and the alternatives that were genuinely open.
- **Risk-driven design** (Fairbanks 2010). Effort goes in proportion to risk. A question only code can settle gets a *spike*: throwaway code that answers it.
- **A walking skeleton** (Cockburn 2004). A thin end-to-end slice runs in production-like conditions before the areas are built out.
- **Continuous delivery** (Humble and Farley 2010) and **site reliability engineering** (Beyer and others 2016). Every change is built, tested and deployable, and readiness is checked against a list before launch.
- **Threat modelling** (Shostack 2014) and **OWASP ASVS 4.0** (2019). Security is designed in, then verified.

The practice sources are cited from knowledge. A source is checked before any record quotes it.

## 2. What we know, what's missing, and how each gap closes

**Known:**
- **Shopify's model, as held in observed-sh:** its admin API schema, webhook topics, permissions and roles, admin routes, plans, Help Center (English and Arabic), engineering writing, open-source code and legal documents. It is strong on what Shopify's records and interfaces are, partial on how Shopify runs them, and silent on its operating numbers.
- **The sixteen first decisions:** the concerns every area depends on, each with Shopify's answer and which part is needed first (`decisions/first-decisions.md`).
- **The founder's decisions,** once stage 0 has reset them.

**Missing, and how each gap closes:**

| Gap | How it closes | Stage |
|---|---|---|
| A decision baseline free of inherited constraints | The reset | 0 |
| What release 1 does, and for whom | Shopify's capabilities, generated from its own structures. Engineering proposes the scope; the founder decides it | 1 |
| How well it must work: isolation, scale, speed, availability, security | Quality scenarios. The founder gives the business volumes; the rest is engineering's | 1 |
| The platform's structure and its technology | Decision records, views and area models | 2 |
| Proof that the structure works | The walking skeleton | 3 |
| The areas themselves | Built in increments | 4 |
| Readiness for real merchants | Security, privacy, recovery and operations checks | 5 |
| What the first market needs | Its setup, with its facts read fresh at that point | 6 |

**When evidence is missing,** in this order:
1. Search observed-sh through its guides first.
2. If it isn't held, a capture request goes to the founder's local agent as a work item, naming what it serves.
3. If no platform can show it, such as a law or a market's practice, it is marked as such and goes to that market's setup, or to the founder.

## 3. The stages

### Stage 0. Reset
- **Objective:** a decision baseline in which nothing constrains or extends the platform because it survived from earlier work.
- **Delivers:** `decisions/founder.tsv`, holding the founder's decisions in force, each with a stable id. Every row is one of three kinds:
  1. a business choice, in one line, in Shopify's terms (for example, which of Shopify's ways of taking payment Sharrwah offers);
  2. a standing working preference of the founder's that this plan doesn't already carry;
  3. an architectural distinction, kept only with a cited, concrete case showing that Shopify's model can't represent it.
- **Removed:** every other row, once the founder accepts the removal. Each is listed with what depends on it, so the founder can decide whether that goes too. The old decision pages and the review then leave the working files.
- **Accepted when:** every row passes the test, the founder has approved every row, and no working file cites a removed one.
- **Founder:** approves the rows, in one sitting.

### Stage 1. Scope and quality
- **Objective:** know what release 1 must do, for whom, and how well.
- **Delivers:**
  - `requirements/capabilities.tsv`: Shopify's capabilities, area by area, generated by script from its admin navigation and API schema, not read by hand.
  - `requirements/scope.md`: release 1's capabilities and the journeys they serve, each traced to that map or to a founder decision. Merchant journeys: open a shop, list products, take an order and get paid, fulfil it. Buyer journeys: find, buy, track.
  - `requirements/quality.md`: measurable scenarios for isolation between shops, availability, speed, durability, security and privacy. Each number is marked as an assumption until the founder confirms the business volumes.
- **Accepted when:**
  - every scope item traces to Shopify's evidence or a founder decision;
  - every scenario is measurable;
  - an independent review passes;
  - the founder has decided the scope and the volumes.
- **Founder:** which merchants release 1 serves first, what it includes (from engineering's proposal), and the volumes expected in year one.

### Stage 2. Architecture
- **Objective:** decide the structure that release 1 and every later market rest on.
- **Delivers:**
  - decision records, first for the first decisions needed before any area (`first-decisions.md` says which), then for the technology: language, data store and hosting;
  - `architecture/views.md`: the system's context and its containers, the deployable parts (the C4 model, Brown 2018);
  - `architecture/domain/<area>.md` for each area in release 1: its records and their states, taken from Shopify's schema, and how it works with the other areas;
  - the variability model: each place that varies by market, how it varies (data, a plug-in or a module), and when it is set;
  - a threat model, and a map of where personal data is held.
- **Accepted when:**
  - each record cites Shopify's shape, and any departure carries its proven case;
  - each is reviewed by an agent that didn't write it;
  - an evaluation against the quality scenarios, a light ATAM (Kazman, Klein and Clements 2000), leaves no high risk unanswered.
- **Founder:** the spending envelope for hosting, and a veto on any record.

### Stage 3. Walking skeleton
- **Objective:** prove the structure end to end.
- **Delivers:** a running thin slice:
  - a shop is created, and its staff signs in and adds a product;
  - a buyer checks out with a manual payment method;
  - the order is recorded, an event goes out, and the order is fulfilled.

  The slice is built and deployed by pipeline, with infrastructure as code, automated tests, logs, metrics and traces.
- **Accepted when:**
  - its acceptance tests run on every change, and it deploys to staging without hands;
  - a test shows that no shop can reach another shop's data;
  - a load test at the assumed scale meets the slice's scenarios;
  - a restore from backup works.
- **Founder:** nothing, unless spending passes the envelope.

### Stage 4. Release 1, area by area
- **Objective:** build release 1's scope.
- **Delivers, for each area:** its model, its API (Shopify's where adopted), code, tests and documentation, shown working on staging.
- **Accepted when:**
  - each area's acceptance tests and API contract tests pass;
  - no high-severity security finding is open;
  - the quality scenarios still hold under load.
- **Founder:** priority calls, if scope has to be cut.

### Stage 5. Production readiness
- **Objective:** the platform is safe for real merchants' businesses.
- **Delivers:**
  - security verified to OWASP ASVS level 2, and a penetration test;
  - card data confirmed to stay with the providers, outside Sharrwah's systems;
  - export and erasure of personal data working;
  - a recovery drill;
  - service levels, alerts, on-call and an incident process;
  - merchant and API documentation.
- **Accepted when:** a production readiness review passes (Beyer and others 2016), and every finding is closed or accepted by the founder.
- **Founder:** accepts the remaining risks, and has the company, its licences, plans and prices in place.

### Stage 6. The first market's setup
- **Objective:** set up Yemen, the founder's first market, by filling the platform's places for it.
- **Delivers:**
  - its currency, languages, tax and domains;
  - its payment providers and couriers, connected through the platform's extension points;
  - what its law requires, met as data in the places built for it.

  Its facts are read fresh at this stage.
- **Accepted when:** Yemen's merchants can complete release 1's journeys with local providers, and the core has changed only through a decision record that carries a proven case.
- **Can start:** its research once stage 2's variability model exists; its build after stage 4.
- **Founder:** partners and commercial agreements, and the go for the market.

### Stage 7. Launch and operate
- **Objective:** go live, run, and learn.
- **Delivers:** the launch, watched service levels, reviewed incidents and a release rhythm. Each further market goes through stage 6 again.
- **Founder:** the launch, and the next markets.

**The order:** 0, 1, 2, 3, 4, 5, then 7, with 6 running alongside 4 and 5. Every stage ends at a gate.

## 4. How the work runs
- **Work items** are in `work.tsv`. Each has:
  - an id and its stage;
  - what it delivers, and what it serves;
  - its inputs and its output, as exact files;
  - its acceptance check;
  - what it depends on;
  - its status.

  Only the current stage is broken into items; the next one stays in outline.
- **Agents do items from a brief.** An agent reads only the inputs named and writes only the output named. An item is done when:
  - its acceptance check passes, by script where possible;
  - an agent that didn't make it has reviewed it;
  - it is committed.

  The coordinator audits what each agent read. Any design that depends on how agents follow instructions is tried on a small batch first.
- **At most four agents run at once.** Effort is high or above for reading evidence, reviewing and judging.
- **A gate closes each stage.** At it, the acceptance criteria are checked and the risks reviewed. The next stage is broken into items, and the founder's decisions for it are asked for together.
- **Code, from stage 3:**
  - short-lived branches and pull requests, each reviewed by an agent that didn't write it;
  - automated checks on every change: lint, types, tests, and dependency and security scans;
  - infrastructure as code, and staging before production;
  - feature flags for unfinished work;
  - versioned data migrations.

## 5. Risks
- **The register** is `risks.tsv`, following ISO 31000:2018 in outline. Each risk has:
  - its id, and what could happen and why;
  - its likelihood and impact, each from 1 to 3;
  - what would show it happening;
  - the response: avoid, reduce, transfer or accept;
  - its owner and its status.
- **Risks are found** at each stage's start, by a premortem (assume the stage failed, and ask why; Klein 2007), in every review and spike, and from the founder.
- **Each risk is routed:**
  - a technical risk to a decision record or a spike in the current stage;
  - a business or legal risk to the founder, as a decision request;
  - a fact that only a market's law settles, to that market's setup.
- **The register is reviewed at every gate.** The top risks are on the status page.

## 6. The founder's decisions
- **The founder's:** markets and their order, which merchants come first, scope priorities, plans and prices, partners and agreements, the company and its licences, spending, and whether Sharrwah's own company runs a service in the merchant's business. Everything else is engineering's, and the founder may veto any of it.
- **When they're asked:** at the gate before the stage that needs them. Each request gives:
  - the question, and why now;
  - the options and their consequences;
  - a recommendation;
  - by when it is needed.

  Work that doesn't depend on a pending decision goes on meanwhile.
- **Recorded** in `decisions/founder.tsv`, in the founder's approved words only.
- **Expected:**
  - stage 0: the reset, now;
  - stage 1: which merchants first, the scope, and the volumes;
  - stage 2: the hosting spend;
  - stage 5: the remaining risks, the company, its licences, and prices;
  - stage 6: partners;
  - stage 7: the launch.

## 7. Staying oriented
- **`STATE.md` is generated by `method/status.py`** from `work.tsv`, `risks.tsv` and the founder's decisions. It shows the stage, what's done and what's next, what needs the founder and by when, and the top risks. Nothing in it is written by hand.
- **At each gate,** the founder gets one short message: what was delivered and accepted, what comes next, and what needs the founder.
- **The founder never tracks work items.**

## 8. Evidence and citation
- **A Shopify fact:** a link pinned to observed-sh at a full commit and line, followed by its quote, as `[source, L<n>](https://github.com/Hamza-ye/observed-sh/blob/<commit>/<path>?plain=1#L<n>) "the quote"`. `method/check_report.py` checks every quote.
- **Published practice:** its author, year and title, with its address once checked. Otherwise, "cited from memory".
- **The work's own items, by stable id only, never by line number:**
  - FD-n for a founder's decision;
  - ADR-n for a decision record;
  - R-n for a risk;
  - W-n for a work item.
- **Every claim is one of three:**
  - a fact, cited;
  - a reading, marked as one;
  - an assumption, marked as one.

## 9. The repository
- **What everyone reads:**
  - `README.md` and `CLAUDE.md`: what this is, and the rules for sessions and agents;
  - `PLAN.md` (this file), `STATE.md` (generated), `work.tsv` and `risks.tsv`.
- **`decisions/`:** `founder.tsv` from stage 0, `adr/` from stage 2, and `first-decisions.md` until each first decision has its record.
- **`requirements/`** from stage 1, and **`architecture/`** from stage 2.
- **From stage 3:** `src/`, `tests/`, `infra/` and `docs/`.
- **`method/`:** the tools for searching evidence, checking quotes, counting tokens and generating the status.
- **`HISTORY.md`:** where anything that left the working files can be found.

Nothing else is kept. A file no current item needs leaves the working files.

## 10. Lessons from the work so far

| What went wrong | What it changed |
|---|---|
| Reading with no decision to serve | Every item names what it serves |
| Completeness taken as the goal | Every stage has acceptance criteria, and ends |
| A market set up before the platform existed | A market enters only at its setup, or through a proven case |
| Work kept because it had cost something | Whatever no current item needs leaves the working files; the history keeps it |
| Process produced instead of product | Documents only as deliverables, one file per subject, status by script |
| Decisions written for the founder that the founder never made | Only words the founder approved are recorded |
| Agents drifting from a design | Checkable briefs, audited reads, independent review, a small trial first |
| Claims beyond the evidence, and conditions misread | Every quote checked by script; reviews check claims against evidence; conditions read at their source |
| Line numbers used as names, then broken | Stable ids |
| Orientation written by hand, then out of date | Generated |
