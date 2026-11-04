# Sharrwah: the engineering plan

**Status.** The founder accepted this plan as the base on 3 November 2026, with the amendments below. An agent that read none of the earlier work wrote it on 1 November 2026, as an independent assessment and proposal; "I" in the text is that agent. The coordinator applied the amendments.

**The amendments of 3 November 2026:**
1. **The reset is applied.** Every decision taken before 1 November lapsed, and the founder's earlier messages with them. Two decisions remain, in `decisions/founder.tsv`: the direction of 1 November (FD-1) and "At launch, Sharrwah runs no payment service of its own." (FD-2). Q5 is answered.
2. **Legal matters are the founder's.** The founder consults a lawyer and takes the necessary steps as the work progresses. This plan raises no legal concern, puts none into the evidence capture and turns none into a decision. Where the platform needs legal content, such as its terms and policies or a country's legal texts, the founder supplies it. The legal readings, questions, risks and recommendations of the first draft are removed.
3. **Capture serves the decisions, throughout the work.** Capture when a gap could change a decision that is coming up, or when an observation would be lost if it isn't taken now. Captures include new or repeated captures, API states before and after journeys, missed evidence, documentation, engineering talks and blogs, sitemaps and open-source code. A capture tool found faulty is fixed before the next capture. Requests go to observed-sh's local agent as issues on that repository (§3).
4. **Finding the evidence is observed-sh's concern.** What is held, its coverage, what is missing, where it is and how to read it are kept in observed-sh's own guides and indexes, apart from Sharrwah's readings (§3).
5. **Cut 1: the first market's facts are gathered when its setup is built.** S1 keeps only a short list of what the first release must work with in Yemen: its payment methods, delivery practice, currency and language. The full study moves to S5.
6. **Cut 2: each piece is created when its stage first needs it.** Identifier schemes, registers, templates, audits, and the code repository with its CI begin at that stage, not at S0.
7. **Merchant interviews are the founder's choice.** The plan needs the founder's answer on who the first merchants are and what they need (Q2), not interviews.
8. **What Sharrwah calls a market is the founder's decision (Q17).** How a country's setup is structured is decided in S2, from the reference's evidence.

**Evidence baseline.** Shopify's evidence repository `observed-sh` at commit `04de369da9ac84ae530ae80a55749167ff4139d4` (31 October 2026), and from the amendments of 3 November at `cc5d3f26404f403cd71b5222078a8827dfa35831`. Each Shopify fact cites **[E-n]**, which §7.1 resolves to `path:line` at its commit. Published practice and other sources cite **[P-n]** (§7.2). "Brief" marks a fact given in the request for this plan.

**How claims are labelled.** A statement with a citation is a fact. **Reading:** marks my interpretation; recommendations are readings. **Assumption:** marks something unverified and says how to verify it. "My count" marks a number I computed from the cited file.

---

## 0. Summary

**Starting position.** No part of the product exists yet: there is no code, no requirements document and no architecture (Brief). What does exist is a wide, pinned record of Shopify's public surface and observed behaviour, built to be "the reference Sharrwah is validated against" [E1]. It includes stores set up with a Yemen business entity and the Yemeni rial [E24].

Shopify itself already serves a Yemen merchant without its own payment service. Shopify Payments covers 41 listed countries and regions, and the UAE is the only Arab state among them. Everywhere else, merchants use third-party providers or manual methods such as cash on delivery [E19, E20]. The founder's "no payment service at launch" therefore fits inside Shopify's shape.

The gap is decisions and first-market facts, not evidence:
- who the first merchants are, and what v1 must do for them;
- the short list of what the first release must work with in Yemen (the rest of Yemen's setup is gathered in S5);
- production targets;
- who is accountable for running a production service when there are no human engineers.

**Reading:** the project has plenty of evidence and few decisions. This plan therefore takes the decisions first.

**Stages** (detail in §2.2):

| Stage | One line | Gate |
|---|---|---|
| S0 Reset and inception | The reset (done), the founder's first decisions, the charter | G0 founder |
| S1 Reference model and the first market's short list | Capability and variation-point catalogue from the evidence; the short list for Yemen's first release; default v1 scope | G1 founder |
| S2 Requirements and architecture | Requirements and quality scenarios; architecture description and ADRs; architecture evaluation; second-market desk check | G2 founder + coordinator |
| S3 Walking skeleton | One end-to-end slice (sign-up, COD order, webhook) deployed by the pipeline, with tenancy, RTL, observability and a tested restore | G3 coordinator |
| S4 Core commerce increments | The v1 capabilities in two-week increments, highest risk first | G4 coordinator |
| S5 Extensibility and the Yemen market setup | Yemen's setup gathered; provider interfaces and adapters, public API and webhooks; Yemen bound as configuration | G5 founder |
| S6 Production readiness and pilot | External security test, load and recovery drills, readiness review, legal texts from the founder, on-call humans, closed pilot | G6 founder go/no-go |
| S7 Launch and operate | General availability under SLOs and error budgets; quarterly refresh of the reference | G7 (after 90 days) |
| S8 Second market | The "built once" test: a new market by setup only, with extensions decided case by case | G8 founder |

**What to ask the founder first** (§1.3), one at a time:
- Q17: what Sharrwah calls what varies by the country it serves.
- Q1: what "Shopify's model" binds.
- Q2: the first merchants, and what v1 must do for them.
- Q3: what "no payment service" covers, and how Sharrwah charges merchants.
- Q6: accountable humans before production.
- Q7: the budget and the date.
- Q8: how the founder wants to be kept informed.

Q4 is removed (amendment 2), and Q5 is answered (amendment 1).

---

## 1. Assessment

### 1.1 The real starting position

**What exists**

- **Evidence.** `observed-sh` holds what Shopify publishes and what it does when used [E1], and records no interpretation [E2]. It contains:
  - the admin GraphQL schema: 3,716 types in version 2026-10 [E8];
  - the admin route manifest: 1,364 routes, 515 of them with eligibility conditions [E9];
  - 236 webhook topics [E10];
  - the staff permission tree: 21 categories, 142 permissions [E11];
  - the Help Center in English and Arabic [E30d];
  - 436 engineering-blog posts [E13];
  - open-source code [E15];
  - plans and prices [E35];
  - browser runs on stores whose business entity is in Yemen and whose currency is YER [E24].
- **Coverage** (my sums over [E3]):
  - admin route × store pairs: 5,328 of 17,732 visited;
  - admin mutations: 422 of 1,525 observed;
  - admin units of work: 162 of 311 journeyed and 115 swept;
  - pages captured: 8,868 from shopify.dev and 5,173 from the Help Center.

  Two things were not held on 1 November: the data model as the public API returns it before and after journeys [E4], and webhook deliveries from real events [E5]. By 3 November both were held for the buyer and order journeys on a store whose currency is YER: the Admin API's state before and after each step [E42], and the deliveries [E43].
- **Capacity.** A coordinator, up to four agents, a capture agent that works on request, and a founder who decides. There are no human engineers (Brief).

**What the evidence says about Shopify's model that shapes the plan**

(a) **Breadth.** All of the above is the product of a codebase "worked on for over a decade by more than a thousand developers" [E13].
**Reading:** "built on Shopify's model" cannot mean rebuilding that surface for launch. The model is the reference from which v1 is chosen. v1's data model and extension points must still leave room for the rest.

(b) **Payments in Yemen.**
- Shopify Payments lists 41 countries and regions [E19, lines 14–54]. The UAE is the only Arab state among them [E19, line 52].
- The same page says: "If your country isn't listed ... you need to use a third-party payment provider" [E19, line 7].
- Manual methods include "cash on delivery (COD), money orders, and bank transfers". Such orders stay "marked as unpaid" until the merchant marks them paid [E20].
- Third-party providers are either "direct" or "external" [E21]. They connect through a session-based Payments Apps API, with payment, capture, refund, void and verification sessions and with pending and redirect states [E22].
- On the paid Advanced store, whose admin shows "Yemeni Rial (YER)", the payments page listed a third-party direct provider in test mode, with a "0.6% transaction fee" [E23].

**Reading:** "At launch, Sharrwah runs no payment service of its own" is Shopify's own shape in this market. It needs no extension.

(c) **Capabilities coupled to Shopify Payments.**
- Shop Pay is activated through Shopify Payments [E25a].
- Subscription products "need to use Shopify Payments as your primary payment gateway" [E25a].
- Selling in several currencies requires "Shopify Payments or Adyen" [E25b].
- Managed Markets answered `INELIGIBLE` with `MISSING_SHOPIFY_PAYMENTS` [E25c].

**Reading:** each coupled capability needs a recorded disposition: drop it, defer it, or re-base it on what providers offer. Multi-currency is the one most likely to matter across MENA.

(d) **Where things vary in Shopify's shape, and a name collision.**
- **Markets:** "a merchant-defined group of buyers", with regions, currency settings, catalogs, price lists and a web presence [E26a].
- **Business entities:** one per legal entity [E26b].
- **Payment providers:** through the Payments Apps API [E22].
- **Shipping rates:** carrier-calculated rates by callback, offered on higher plans [E26c, E29a].
- **Functions:** 13 Function APIs, covering payment and delivery customization, validation and discounts, among others [E27].
- **Tax:** default rates the merchant confirms or overrides, tax apps, or Shopify Tax in the US, EU, UK and Canada [E28].
- **Tracking carriers:** held as a list [E41].
- **Languages:** 136 for the storefront, 50 in checkout, and 49 in the admin, where Arabic is in beta and renders right-to-left as `ar-YE` [E30].
- **Per-country availability:** 515 routes carry eligibility conditions [E9], and pricing pages vary by country [E35b].

Shopify's settings areas already name most of what a market setup must fill: Payments, Shipping and delivery, Taxes and duties, Languages, Domains, Notifications, Customer privacy, Policies [E23].

**Reading:** the founder's "market" is not Shopify's "Market".
- The founder's market is a country where Sharrwah operates, with its own providers, law and limits.
- Shopify's Market is a merchant's group of buyers.
- In Shopify, the variation by the merchant's country is spread across eligibility, availability and per-country terms.

Sharrwah should model the founder's market explicitly, under its own name (here, *market setup*), as platform configuration. Merchants' own Markets then still work inside it. The name is the founder's decision (Q17); how a country's setup is structured is decided in S2, from the reference's evidence.

(e) **The architecture Shopify publishes.**
- One codebase whose component boundaries are enforced, a "modular monolith" [E13], enforced with Packwerk [E15].
- The database was sharded only in 2015. Shops were then isolated into pods: "A pod consists of a set of shops that live on a fully isolated set of datastores". Each unit of work runs in a single pod [E14].
- Public APIs are versioned quarterly, and each version is "supported for a minimum of 12 months" [E18].
- For payment integrations it lists ten practices: timeouts, circuit breakers, capacity, monitoring, structured logging, idempotency keys, reconciliation, load testing, incident management and retrospectives [E16].
- For peak readiness it uses "What Could Go Wrong" risk assessments, Game Days, and load and scale tests [E17].
- Apps must handle mandatory data-request and redaction topics [E34].
- It publishes SOC 3 reports and a PCI DSS v4.0.1 attestation as a service provider [E36].

**Reading:** start as a modular monolith in which every shop-owned row and job is scoped to one shop, so shops can later move into pods. Build pods only when load requires them.

(f) *Removed by amendment 2.*

(g) **The reference keeps moving.** The developer changelog holds 795 items [E37], and "The router hash changed within one day" [E6]. observed-sh moves too: 215 commits between this plan's two evidence baselines, 1 to 3 November (the coordinator's count, from git).
**Reading:** freeze the reference at one commit per stage, and adopt later Shopify changes only by decision.

**The first market**

Yemen's facts are gathered when its setup is built, in S5 (amendment 5). Until then the plan carries only the short list S1 gathers. One fact in the evidence bears on that list already: Shopify sets local delivery by distance or postal code [E29b].

**Reading:** the founder's rule that a market's setup never defines the platform is the right guard, and it needs a test: a second-market desk check at G2, and a real second market at S8.

**People and process**

**Reading:** agents can write the documents and the code. They cannot give accountable sign-off: accepting security risk, answering incidents at night, signing provider and merchant contracts, holding production credentials. That gap must close before real merchants depend on the service (§5).

### 1.2 What is missing before a good engineering plan, and how to get it

| ID | Missing input | Why it blocks | How to obtain it | Owner | By |
|---|---|---|---|---|---|
| M1 | What "Shopify's model" binds | It sets the scope of every later decision | Founder decision (Q1) | Founder | G0 |
| M2 | The first merchants: who they are, what they sell, how they sell today, how many | Scope, sizing, quality targets | The founder's answer (Q2); merchant interviews only if the founder chooses (amendment 7) | Founder | G1 |
| M3 | v1 scope | Requirements, architecture, estimates | The coordinator proposes a default disposition for each capability in the S1 catalogue; the founder approves (MoSCoW) | Founder | G1 |
| M4 | The business model and Sharrwah's own billing | Billing capability, terms, choice of provider | Founder (Q3, Q9). The coordinator lays out options with the evidence: Shopify charges third-party transaction fees [E21, E23] and none on manual methods [E20] | Founder | G1 |
| M5 | *Removed by amendment 2: legal matters are the founder's.* | | | | |
| M6 | Yemen's facts. By G1, only the short list: payment methods, delivery practice, currency, language. In S5: providers and their APIs, banks, exchange practice, tax, addresses, connectivity and devices | v1 scope (the short list); the market setup and the extension list (S5) | Research agents (web sources, cited and dated); the founder's local knowledge and contacts; the law from the founder | Coordinator + founder | The short list by G1; the rest in S5 |
| M7 | Production targets: availability, data-loss and restore limits, support hours, security level, attestations | Architecture, cost, the S6 criteria | The coordinator presents options with their cost; the founder decides (Q10) | Founder | G2 |
| M8 | Budget and date | Sequencing, team mix | Founder (Q7) | Founder | G0 |
| M9 | Hosting region and data residency | Architecture, latency | ADR options from the coordinator, with any legal requirement the founder supplies; the founder decides (Q11) | Founder | G2 |
| M10 | Accountable humans for security and operations | S6 cannot pass without them | Founder (Q6); the coordinator writes the role descriptions | Founder | Decide by G2; in place for S6 |
| M11 | Evidence v1 needs that is not held. Held since 3 November for the YER store's journeys: API state before and after each step [E42], real webhook deliveries [E43], a buyer's checkout with cash on delivery [E44] | Reference-behaviour tests | Issues on observed-sh to its local agent (§3), whenever a gap could change a decision | Coordinator | Throughout |
| M12 | The founder's working preferences | How visibility is designed | Q8 | Founder | G0 |
| M13 | The status of decisions taken before 1 November | Avoids carrying commitments nobody has re-examined | Answered: they lapsed (amendment 1) | Founder | Done, 3 November |

### 1.3 Questions for the founder, and when

Ask Q17, Q1–Q3 and Q6–Q8 at G0, which is now, one at a time. Q4 is removed and Q5 is answered. Ask Q9–Q16 later, each with a decision card prepared in advance (§2.6).

| Q | Question | My recommendation | Needed by |
|---|---|---|---|
| Q1 | Does "Shopify's model" bind (a) only the domain and extension model, (b) the internal architecture as well, or (c) the business model too (plans, fees, partners, app ecosystem)? | (a) binds. (b) is adopted by ADR where the evidence supports it. (c) is decided separately (Q9) | G0 |
| Q2 | Who are the first 10–20 merchants? What do they sell, and how do they sell today? What would make them switch? How many at the pilot, and after a year? | Answer from what you know; interviews only if you choose | Ask at G0; answer by G1 |
| Q3 | Does "no payment service of its own" mean Sharrwah never holds, routes or settles buyers' money, and merchants contract providers directly? How will Sharrwah charge merchants? | Yes. No charge during the pilot. Later, invoice merchants through a provider: Sharrwah billing its own merchants is not a payment service for buyers | G0 |
| Q6 | Will you engage at least one accountable human for security and operations, and an external penetration test, before real merchants use the service? | Yes, in place by S6 | Ask at G0; decide by G2 |
| Q7 | What budget and what date? If they conflict, which gives way: scope or date? | Fix the date and vary the scope | G0 |
| Q8 | In which language, how often, and with how much of your time each week do you want status and decisions? | A weekly page in your chosen language, with decisions batched | G0 |
| Q9 | Plans, prices and fees, including any fee on third-party or manual payments | Decide once the first merchants are known (Q2) | G1 |
| Q10 | Availability, data-loss and restore limits, and support hours, weighed against their cost | Choose from costed options | G2 |
| Q11 | Hosting region and data residency | Choose from costed options, with any legal requirement you supply | G2 |
| Q12 | Yemen footprint at launch: regions served, currencies shown and settled, languages | Decide after the dossier | G1 |
| Q13 | Third-party apps at launch: none, selected partners, or anyone? | Selected partners | G1 |
| Q14 | Which payment, courier and messaging providers to contract | Choose from the dossier's shortlist | S5 |
| Q15 | The pilot merchants, then go or no-go for general availability | Decide from the G6 packet | G6 |
| Q16 | The second market, and the country for the G2 desk check | Name the desk-check country by G2 | G2, G7 |
| Q17 | What does Sharrwah call what varies by the country it serves, so that Shopify's "Markets" (a merchant's groups of buyers [E26a]) keeps its meaning? | The coordinator's: "country" for the unit, as Shopify's own data and interface name it [E45], and "country configuration" for what is bound there: product-line engineering's term for a resolved set of variation points, bound in stages, the country's before the merchant's [P9, P48, P49]. "Market" stays a business word, never in the platform's model | G0 |

---

## 2. The engineering plan

### 2.1 Method, by established practice

- **Life cycle.**
  - Tailor the ISO/IEC/IEEE 12207 processes [P1].
  - Take the founder's decisions at stage gates [P7].
  - Work in iterative increments inside each stage.
  - Order the work by risk, so the largest risks get the earliest spikes [P6, P8].
- **Requirements from a reference model.**
  - The evidence is the reference [E1]. Capture closes its gaps throughout the work (amendment 3).
  - A capability catalogue (C-n) follows Shopify's own organization: router sections and resources [E9, E12], schema types [E8], permissions [E11], webhooks [E10].
  - Requirements follow ISO/IEC/IEEE 29148 [P2]. Qualities follow ISO/IEC 25010 [P4] and are written as quality-attribute scenarios with measures [P10].
  - Observed Shopify behaviours become *reference-behaviour tests*. A deliberate divergence needs a recorded decision.
- **Variability.**
  - Product-line engineering [P9]: the platform defines variation points (V-n), and each market setup binds them.
  - A gap becomes a proposed extension (X-n) for the founder.
  - Architecture fitness functions in CI [P19] enforce "markets never define the platform".
- **Architecture.**
  - Described per ISO/IEC/IEEE 42010 [P3], using arc42 [P14] and C4 [P15].
  - Decisions recorded as ADRs [P12, P13].
  - Bounded contexts [P11].
  - Evaluated with a lightweight ATAM [P10].
  - Multi-tenant design per the SaaS Lens [P45], and twelve-factor operation [P44].
- **Delivery.** A walking skeleton first [P16], then continuous delivery [P17], measured with DORA's measures [P18].
- **Security and privacy.**
  - NIST SSDF [P22].
  - OWASP ASVS 5.0 Level 2 as the target [P23]. **Assumption:** Level 2 suits a commerce service that holds personal data; it is confirmed at G2.
  - A threat model per feature [P24], and build provenance per SLSA [P25].
  - Card data stays out of Sharrwah's systems through provider-hosted flows, to keep PCI DSS scope small [P26]. **Reading:** the exact obligations depend on each provider's integration type, to be confirmed with that provider.
- **Reliability and operations.** SLOs, error budgets and a production readiness review [P20, P21], plus Shopify's own practices for payments and peaks [E16, E17].
- **Accessibility and language.** WCAG 2.2 AA [P40]; right-to-left text through structural markup [P41]; locale data from CLDR [P42].
- **Agentic execution.**
  - The orchestrator–workers and evaluator–optimizer patterns [P30].
  - Parallel subagents with explicit briefs and effort budgets [P31].
  - Context treated as a finite resource, with state kept in files rather than in agent memory [P32].
  - Tests first, and independent review [P33, P34].
- **Decisions and risk.**
  - Decisions are classed as hard to reverse (Type 1) or reversible (Type 2) [P29].
  - Risk management follows ISO 31000 [P5] and the SEI's cycle: identify, analyze, plan, track, control, communicate [P27].
  - A pre-mortem at G2 [P28] (amendment 6).

### 2.2 Stages

**Assumption:** durations add up to about 7–11 months to general availability. They are re-estimated at G3 from measured throughput.

**S0 Reset and inception** (1–2 weeks; depends on nothing)
- *Objective:* agree what is built, by whom and under which rules, and obtain the inputs that block planning.
- *Deliverables:*
  - The reset, applied on 3 November: the earlier work's files left the working tree, and `README.md` names the commit that holds them (§4).
  - The decision log, `decisions/founder.tsv`: FD-1, the direction of 1 November verbatim, and FD-2, "At launch, Sharrwah runs no payment service of its own." The answers to Q17, Q1–Q3 and Q6–Q8 follow.
  - A charter, as this plan's first section: purpose, first market, constraints, success measures, once Q1, Q2 and Q7 are answered.
  - Working rules, in `CLAUDE.md`. The brief template and the definition of done for documents come with S1's first briefs (amendment 6).
  - `risks.tsv`, seeded from §2.3; the founder's risk appetite, asked with Q7.
  - `STATE.md`, generated from `work.tsv` and `risks.tsv`.
  - The coordinator's advice to observed-sh's local agent on finding the evidence (amendment 4, §3).
- *Acceptance:*
  - The founder approved this plan with its amendments (3 November).
  - Q17, Q1–Q3 and Q6–Q8 are answered, or defaulted with the founder's consent, and the charter is approved.
  - Every document that cites the evidence passes the quote check (`method/check_report.py`).
- *Gate G0 (founder):* proceed to S1.

**S1 Reference model and the first market's short list** (3–5 weeks; depends on G0)
- *Objective:* turn the evidence into a catalogue that makes scope choices cheap, and gather the short list of what the first release must work with in Yemen (amendment 5).
- *Deliverables:*
  1. The capability catalogue (C-n). For each capability: Shopify's types, admin units of work, webhooks, permissions and eligibility, each cited.
  2. The variation-point catalogue (V-n), seeded from §1.1(d).
  3. The capabilities coupled to Shopify Payments, each with a proposed disposition.
  4. Reference behaviours worth testing. Example: an order paid by a manual method stays unpaid until the merchant marks it paid [E20].
  5. The short list for Yemen's first release: its payment methods, delivery practice, currency and language, each fact sourced and dated. The full study is in S5.
  6. The founder's answer on the first merchants (Q2).
  7. A default v1 scope proposal, with the rationale and a cost class for each capability.
- *Acceptance:*
  - Every catalogue row cites the pinned commit and passes the quote check.
  - A second agent re-derives a 10% sample and agrees on at least 95% of it; disagreements are resolved and logged.
  - Every short-list fact carries a source and a date. Unknowns are listed, not guessed.
  - Every gap that could change a scope choice is an issue on observed-sh (amendment 3).
  - The founder gets a two-page summary.
- *Gate G1 (founder):*
  - v1 scope;
  - the Yemen footprint (Q12);
  - an outline of the business model (Q9);
  - dispositions for the capabilities coupled to Shopify Payments;
  - the first extensions;
  - acceptance or treatment of the red risks.

**S2 Requirements and architecture** (4–6 weeks; depends on G1)
- *Objective:* specify v1, and design a platform in which markets are configuration.
- *Deliverables:*
  - **Requirements** (REQ-n), each traced to a C-n and to evidence.
  - **Quality scenarios** (QS-n) with measures, among them:
    - storefront page weight and latency on a constrained mobile network profile;
    - admin use on an intermittent connection;
    - availability;
    - data-loss and restore limits;
    - isolation between tenants.
  - **The architecture description:**
    - a modular monolith, organized by bounded context, with enforced boundaries;
    - tenancy: every shop-owned row and job is scoped to one shop, ready for pods [E14];
    - the extension architecture: a public Admin API with date-named versions [E18]; signed webhooks, including the privacy topics [E34]; app authorization by scopes; provider interfaces for payments (a session state machine, as in [E22]), shipping rates (a callback, as in [E26c]), tax and messaging. Hooks like Shopify's Functions are deferred;
    - the model of a country's setup (its name per Q17): what it holds and how it is bound, derived from the reference's evidence. Shopify holds each country's currency, tax rate and name, unit system, address format, languages and time zone as data keyed by its code [E45], and feature availability as eligibility [E9];
    - the data model;
    - the threat model and security architecture;
    - the operations architecture: environments, infrastructure as code, CI/CD, observability, backup and recovery.
  - **ADRs** for the stack, database, hosting region, identity, search and messaging.
  - **A test strategy:** unit tests, provider contract tests, end-to-end tests, reference-behaviour tests.
  - **A cost model.**
  - **An increment plan** for S4–S5.
  - **A pre-mortem** [P28], folded into `risks.tsv`.
- *Acceptance:*
  - Every REQ traces to a C-n, and to evidence or a decision.
  - Every QS has a measure and a test method.
  - Two independent agents run the architecture evaluation; each finding is closed or accepted.
  - The fitness functions are specified.
  - The second-market desk check is done: a second country (Q16) is expressed through the same V-n, and every gap is listed as an X-n.
  - The founder has decided Q10, Q11 and the budget.
- *Gate G2 (founder and coordinator).*
- **Reading** on the stack, which is an engineering ADR rather than a founder decision: Ruby on Rails with MySQL would let Sharrwah reuse tooling Shopify publishes, such as Packwerk, job-iteration, maintenance_tasks, Semian and Ghostferry [E15], some of it under MIT-style permission [E40]. Any mainstream stack in which agents and future hires are strong is defensible. Licences are checked for each dependency.

**S3 Walking skeleton** (3–4 weeks; depends on G2)
- *Objective:* the thinnest slice through every architectural element, on production-like infrastructure.
- *Deliverables:*
  - The platform repository, CI/CD and infrastructure as code.
  - The slice, end to end:
    1. an operator creates a market setup for a test country;
    2. a merchant signs up and gets a shop, then adds a product;
    3. a buyer checks out with cash on delivery, and the order shows as unpaid;
    4. the merchant marks the order paid;
    5. a webhook reaches a test app.
  - Arabic (right-to-left) and English.
  - Logs, metrics and traces.
  - Backups, with a tested restore.
  - A security baseline: a secrets manager, dependency and secret scanning, static analysis, an SBOM, build provenance [P25].
  - Fitness functions in CI: module boundaries; no market literals in the core; cross-shop access tests that must fail.
- *Acceptance:*
  - A clean deploy from the pipeline, with all checks green.
  - A restore drill passed.
  - A DORA baseline [P18].
  - A five-minute recorded demo for the founder.
  - Throughput measured, and the plan re-estimated.
- *Gate G3 (coordinator; the founder sees the demo).*

**S4 Core commerce increments** (12–20 weeks; depends on G3)
- *Objective:* build the approved v1 capabilities in two-week increments, highest risk first: checkout, orders, the payment interface, tenancy and permissions.
- *Deliverables per increment:* working capabilities with tests; merchant help written per Diátaxis [P35]; the API reference; an increment report.
- *Acceptance per increment:* the Definition of Done (§2.5), with performance budgets met and right-to-left and accessibility checks passed.
- *Gate G4 (coordinator; the founder is informed):* v1 is complete for the pilot.

**S5 Extensibility and the Yemen market setup** (6–10 weeks, overlapping S4; depends on S4's progress and the provider contracts)
- *Objective:* complete the provider interfaces, and bind Yemen's setup without changing the core.
- *Deliverables:*
  - Yemen's setup gathered (amendment 5): payment, courier and messaging providers and their APIs; banks; currencies and exchange practice; tax; addresses; connectivity and devices. Each fact is sourced, dated and mapped to a V-n, and each gap is an X-n for the founder. Its law comes from the founder.
  - Payment adapters: manual methods, and selected wallet or bank providers through the session interface.
  - Courier adapters: rates, tracking, and cash remittance if the dossier shows it is needed.
  - Messaging adapters.
  - Yemen's tax rules; its legal texts, from the founder.
  - The public API and webhooks, for first-party apps and selected partners (Q13).
  - A contract-test suite for each adapter.
  - Reconciliation reports [E16].
- *Acceptance:*
  - The Yemen setup changes only `markets/ye/` and adapters; any core change is an extension (X-n) the founder approved.
  - Adapters pass contract tests and sandbox end-to-end tests, including timeouts, retries and idempotency [E16].
  - The provider contracts are signed (Q14).
- *Gate G5 (founder).*

**S6 Production readiness and pilot** (6–8 weeks; depends on G4, G5 and Q6 being in place)
- *Objective:* show the service is production-grade before real merchants depend on it.
- *Deliverables:*
  - An external penetration test and verification against ASVS Level 2.
  - Load and scale tests at a multiple of the expected peak, game days, and "What Could Go Wrong" exercises [E17].
  - A disaster-recovery drill.
  - SLOs, alerting, an on-call rota of accountable humans, an incident process and post-incident reviews [P20].
  - A production readiness review [P20].
  - Terms, a privacy notice, data-processing terms and an acceptable-use policy, from the founder (amendment 2).
  - A support process.
  - A closed pilot of at least four weeks.
- *Acceptance:*
  - No open critical or high findings.
  - SLOs met throughout the pilot.
  - The recovery drill met the limits set at G2.
  - The readiness review is complete.
- *Gate G6 (founder):* general availability in Yemen.

**S7 Launch and operate** (from G6)
- *Objective:* run within SLOs, learn, and keep the reference current by decision.
- *Deliverables:*
  - a release cadence and an error-budget policy [P21];
  - quarterly API versions;
  - a quarterly refresh of the reference: Shopify's changes at a new evidence commit, with proposed adoptions;
  - a monthly review of cost and risk.
- *Gate G7 (after 90 days):* SLOs met, or the error-budget policy applied; the charter's merchant measures reviewed.

**S8 Second market** (from G7, or earlier if the founder decides; Q16)
- *Objective:* prove that the platform is built once.
- *Deliverables:* the dossier, the setup and the adapters, with extensions decided case by case.
- *Acceptance:* no unrecorded core change; the time and cost to add the market are compared with the G2 desk-check forecast.
- *Gate G8 (founder).*

**Dependencies.**
- S0 → S1 → S2 → S3 → S4, in sequence.
- S5 starts in the middle of S4.
- S6 follows S4 and S5.
- S7 follows G6, and S8 follows G7.
- Captures close gaps throughout (amendment 3).

### 2.3 Risks

- **Identify** at every agent report, at every gate, in the pre-mortems, and in "What Could Go Wrong" exercises before the pilot [E17].
- **Assess** each risk's likelihood (1–5) and impact (1–5), and note how soon it could strike. The founder sets the risk appetite at G0.
- **Route** by score and kind:
  - Red (a score of 15 or more), and any money-flow or reputational risk, goes to the founder within two working days, with options and a recommendation. Only the founder may accept such a risk. Legal matters are the founder's and stay out of this register (amendment 2).
  - Amber (8–14) technical risk is treated by the coordinator and reported weekly.
  - Green risk is tracked by its owner.
  - Security findings block a release according to severity: critical and high block.
- **Manage** each risk with an owner, a response (avoid, reduce, transfer or accept), a trigger and a status, all in `risks.tsv`. The top five appear in `STATE.md`.

Initial register. The risks are my assessment, and every score is a **Reading**. RISK-02 and RISK-03 were removed by amendment 2, and RISK-16 is the coordinator's:

| ID | Risk | L | I | Route | First treatment |
|---|---|---|---|---|---|
| RISK-01 | Copying Shopify's breadth swamps v1 [E8–E10] | 5 | 4 | Founder (scope) | A catalogue with default dispositions; v1 by MoSCoW at G1 |
| RISK-04 | No local payment provider with a usable API at launch | 3 | 4 | Founder | The short list in S1, the full study in S5; manual methods first; the interface is built regardless |
| RISK-05 | Capabilities coupled to Shopify Payments, multi-currency above all [E25] | 5 | 3 | Founder | Dispositions at G1 |
| RISK-06 | No accountable humans for production security and operations | 4 | 5 | Founder | Q6 decided by G2; a condition of G6 |
| RISK-07 | Defects or vulnerabilities written by agents go unnoticed | 4 | 4 | Coordinator | Layered checks; independent review; an external test |
| RISK-08 | One merchant's data exposed to another | 2 | 5 | Coordinator; founder if it occurs | A shop-scoped access layer; negative tests; a penetration test |
| RISK-09 | Yemen-specific logic leaks into the core | 4 | 3 | Coordinator | Fitness functions; the desk check at G2; S8 |
| RISK-10 | Slow founder decisions stall the work | 3 | 4 | Founder | Batched decision cards, with defaults and deadlines |
| RISK-11 | The reference drifts as Shopify changes [E6, E37] | 5 | 2 | Coordinator | A pinned baseline; a quarterly refresh by decision |
| RISK-12 | Limits on connectivity, power and devices degrade use (**Assumption**) | 4 | 3 | Coordinator | Performance budgets; tests on constrained profiles |
| RISK-13 | Merchant abuse, such as illegal goods or fraud | 3 | 4 | Founder | Onboarding checks and a takedown process; the policy's text from the founder |
| RISK-14 | Cloud, service or AI costs overrun | 3 | 3 | Coordinator; founder at threshold | A budget per stage; token counts; a monthly review |
| RISK-15 | Secrets found in the evidence [E7] spread into new artifacts | 2 | 3 | Coordinator | Never copy them; secret scanning with push protection |
| RISK-16 | Agents spend their budgets rediscovering what observed-sh holds | 4 | 3 | Coordinator | observed-sh's guides and indexes (§3); every evidence brief keeps a discovery log for its local agent |

### 2.4 The founder's decisions, and when

A Type 1 decision is hard to reverse and is made deliberately. A Type 2 decision is reversible, is made quickly, and has a default [P29].

Each decision becomes a record, FD-n [P13]. The record holds the question, the options, the decision in words the founder approved, its consequences, and what would reopen it.

| Decision | Q | Needed by | Type | Default if undecided |
|---|---|---|---|---|
| Accept the plan, the method and the repository reset | — | G0 | 2 | Done, 3 November |
| What Sharrwah calls what varies by country | Q17 | G0 | 2 | The recommendation under Q17 |
| What "Shopify's model" binds | Q1 | G0 | 1 | The recommendation under Q1 |
| Decisions taken before 1 November | Q5 | G0 | 2 | Done, 3 November: they lapsed |
| Budget and date | Q7 | G0 | 2 | Fix the date, vary the scope |
| Working preferences | Q8 | G0 | 2 | A weekly page |
| v1 scope; dispositions of capabilities coupled to Shopify Payments | Q2 | G1 | 2 | The coordinator's default proposal; coupled capabilities deferred |
| Yemen footprint | Q12 | G1 | 1 | None: blocks S2 |
| The business model and Sharrwah's own billing | Q3, Q9 | G1 | 2 | No charge during the pilot |
| Apps at launch | Q13 | G1 | 2 | First-party apps and selected partners |
| Production targets and their cost | Q10 | G2 | 2 | The coordinator's middle option |
| Hosting region and data residency | Q11 | G2 | 1 | None: blocks S3 |
| Accountable humans and an external test | Q6 | G2 (in place by S6) | 1 | None: blocks G6 |
| Each extension beyond Shopify's shape (X-n) | — | When raised | Mostly 2 | Not extended |
| Accepting a red risk | — | Within two working days | — | Not accepted; work on that path stops |
| Provider contracts | Q14 | S5 | 1 | None |
| The pilot, then general availability | Q15 | G6 | 1 | No-go |
| The second market | Q16 | G2 (desk check), G7 | 2 | The coordinator proposes |

### 2.5 How the coordinator and agents work, and how the work is checked

**Roles.**
- The founder decides.
- The coordinator plans, writes briefs, dispatches, integrates, and holds the technical gates. It never both builds and accepts the same item.
- Each agent either authors or checks, and no agent reviews its own work.
- The capture agent acquires evidence when an issue on observed-sh asks for it (§3).
- The usual mix of agents is: in S1, two evidence analysts, one market researcher and one checker; in S2, two analysts, one security agent and one reviewer; in S3–S5, two or three builders and one reviewer-tester, adding a security agent for high-risk work.

**The loop.**
1. **Plan.** The coordinator keeps the backlog in `work.tsv`, one item per brief, until S3 moves it to GitHub issues (amendment 6). Milestones are gates and increments.
2. **Ready.** A brief states:
   - its objective;
   - its inputs, pinned to commits;
   - its outputs, as paths;
   - testable acceptance criteria;
   - constraints: the evidence is read-only, Python runs with `-I`, no secrets, no production access;
   - a budget in tokens and time;
   - a risk class;
   - the reviewer assigned to it;
   - what to report.
3. **Do.** One agent per brief, each in its own branch or worktree, writing tests first. At most four agents run at once, and at least one of them is a checker.
4. **Report.** A pull request whose template asks for: what changed, how it was verified, the evidence cited, the assumptions made, open questions, risks found, and cost.
5. **Check.** CI runs first, then an independent review against the brief. Authentication, tenancy, payments, personal data and infrastructure get two reviews and a security checklist.
6. **Accept.** The coordinator merges with a squash commit in Conventional Commits form that references the issue [P36]. The status page regenerates.
7. **Escalate.** An agent escalates to the coordinator on ambiguity, a blocked brief or an amber risk. The coordinator escalates to the founder on decisions and red risks. A brief that fails its checks twice is re-scoped, not retried.

**Checks.**

| Check | How | When |
|---|---|---|
| Automated | Tests, lint, types, static analysis, dependency and licence audit, secret scanning, fitness functions, link check, and a citation and quote check against the pinned evidence | Every pull request |
| Independent review | An agent with a fresh context reviews against the brief and its acceptance criteria [P34] | Every pull request |
| Evidence review | The reviewer re-opens a sample of citations at the pinned commit, and checks that every claim is labelled fact, reading or assumption | Every pull request that changes a document |
| Acceptance | Reference-behaviour and end-to-end tests; a demo for each increment | Each increment and gate |
| Audit | A gate-audit agent checks each gate's criteria against the artifacts; from S3, 10% of merged work re-reviewed each week and a red-team agent each month | Each gate; weekly and monthly from S3 |
| Human | An external penetration test; once engaged, accountable humans review high-risk changes | From S6 |

From S3, to make "never reviewed by its author" enforceable, the reviewer role uses a separate GitHub identity, such as a GitHub App or a machine user. Branch protection can then require an approval from someone other than the author.

**Definition of Done (code).** A change is done when it has:
- tests, including reference-behaviour tests;
- an independent review;
- every CI check green;
- documentation and traceability updated;
- a reversible migration;
- observability added;
- performance and accessibility budgets met;
- a feature flag, if it is risky.

**Measures.** DORA's four keys [P18]; review findings and defects that escaped; how many requirements have tests; the cost of each merged change; how long decisions take.

**Continuity.** State lives in the repository: the plan, decisions, risks, briefs and reports. It never lives only in a session's context [P32], so any session can resume from `main`.

### 2.6 Keeping the founder oriented without burden

- **One status view.** Now `STATE.md`, generated on every change to `work.tsv` or `risks.tsv`; a private page once the work needs more than it shows (amendment 6). It shows:
  - where the work is: the stage, and the checklist for its gate;
  - what has changed since the founder's last visit, in at most seven lines;
  - the decisions needed, as cards: question, options, recommendation, default, deadline, and the cost of delay;
  - the top five risks, in plain words;
  - the next milestones and demos;
  - spending against the budget;
  - links to the gate packets.

  Every claim on the page is labelled fact, reading or assumption.
- **A gate packet** of at most two pages, with a recorded demo and the decision cards.
- **Cadence.** A weekly digest, with decisions batched weekly. Anything outside that cadence is for red risks only.
- **Answering.** The founder answers on the page or by message. The coordinator records the decision in the founder's words and shows it back; it binds only once the founder confirms it.
- The founder never needs to read logs, issues or pull requests.

---

## 3. Organizing documents, artifacts, code and evidence

**Repositories.**
- From S3, a new monorepo, `sharrwah`, holds the code and its documentation together (docs-as-code). Requirements, ADRs and code change together, so they are reviewed together. Until then this repository holds the plan, the decisions and the documents, which move into the monorepo's `docs/` at S3 (amendment 6).
- `observed-sh` stays separate and read-only.
- `sharrwah-knowledge-map` is archived when its documents move.

```
README.md                  what this is, and how to find things (one page)
docs/
  charter.md
  plan/                    plan.md; status.md (generated)
  decisions/founder/       FD-0001-....md (MADR form)
  decisions/architecture/  ADR-0001-....md
  requirements/            capabilities.tsv (C-n), variation-points.tsv (V-n),
                           extensions.tsv (X-n), requirements/ (REQ-n), quality/ (QS-n)
  reference-model/         one page per capability, cited to the evidence
  markets/ye/              dossier.md (with sources), setup.md
  architecture/            arc42 sections; C4 diagrams as code
  security/  operations/   threat models; SLOs; runbooks
  risks/risks.tsv          RISK-n
  evidence/                BASELINE (the pinned commit); citation guide (capture requests are issues on observed-sh)
  references.md            P-n bibliography
platform/                  modules, one per bounded context
markets/ye/                Yemen's setup: configuration and adapters
tools/                     evidence search, quote check, status and traceability generators
.github/                   brief issue template, PR template, workflows, CODEOWNERS
```

**Identifiers.** Stable and never reused: FD-n, ADR-n, Q-n, C-n, V-n, X-n, REQ-n, QS-n, RISK-n, W-n. Each scheme starts when its stage first needs it (amendment 6). Work items are W-n in `work.tsv` until S3, then GitHub issue numbers.

**Citing.**
- **Shopify evidence:** `observed-sh@<full sha>:<path>:L<start>-L<end>`, with a short verbatim quote. A WARC record is cited as `…:<warc>@<offset> <URI>`, followed by the line in its body.
  - CI checks each quote against the source at the pinned commit.
  - Each stage pins one baseline commit of observed-sh, recorded in this plan's header until S3, then in `docs/evidence/BASELINE`. Moving it is a decision, made with a diff of what changed.
- **Published practice:** author, title, year, URL (with DOI or ISBN if there is one) and access date, keyed P-n in `docs/references.md`.
- **Every statement** in a working document is one of: a fact (cited); a reading; an assumption (with an owner and a way to verify it); or a decision (linked to its FD or ADR).

**Linking.**
- Links inside the repository are relative.
- Links to other repositories are commit permalinks [P39], never branch links.
- External pages carry an access date and, where possible, an archived copy.

**Traceability.**
- Requirements trace to capabilities, which trace to evidence and practice (E and P); from there to ADRs, code and tests.
- Tests name the REQ they verify, and commits name their issue.
- CI generates the traceability matrix. Every generated file says so in its header and is never edited by hand.

**Versions.**
- Commits follow Conventional Commits [P36].
- Libraries and SDKs follow SemVer [P37].
- The public API uses date-named versions, as Shopify does [E18].
- A changelog per Keep a Changelog [P38].
- A git tag for each gate.

**Evidence handling.**
- The evidence is read-only, and Python that reads it runs with `python3 -I`.
- Secrets found in the evidence [E7] are never copied into any artifact. The new repository has push protection and secret scanning.
- A capture request is an issue on `observed-sh` (amendment 3). It states:
  - what to capture: the surface, store, plan, role and locale;
  - why: the decision, C, REQ or Q it could change;
  - how: manually or by the agent, read-only or as a journey;
  - what must be visible for the capture to count;
  - when it expires.

  The local agent closes it with the run and the commit that hold the result, which is cited at that commit.

**Finding the evidence** (amendment 4). What is held, its coverage, what is missing, where it is, how to read it, which versions of Shopify's APIs it holds, and how to open an issue are observed-sh's to keep, in its own guides and generated indexes, with no interpretation in them. Sharrwah's readings stay in Sharrwah's repositories. The coordinator's advice to the local agent is an issue on observed-sh.

---

## 4. The existing repository (applied on 3 November 2026)

The reset removed from the working tree:
- `founder-decisions.tsv`, replaced by `decisions/founder.tsv`;
- `decisions/review.md`, `studies/`, `founder-messages/`, `INVENTORY.md` and `HISTORY.md`;
- the earlier plan. `work.tsv` and `risks.tsv` were rewritten for this plan, and `method/status.py` generates `STATE.md` from them.

Commit `b4dbde78` holds all of them, and `README.md` names it.

What stays:
- `decisions/first-decisions.md`, at the founder's word, as an input to S2. It is reviewed against observed-sh's newer evidence.
- The method tools, in `method/`. They move to `tools/` with tests at S3.
- The branches `evidence/other-product-class` and `founder/bigcommerce-help-capture` stay out of the work. Whether to delete them is the founder's call.

---

## 5. Where I recommend against the brief

1. **Running production with no human engineers.** A production-grade service needs accountable people to accept security risk, respond to incidents, sign contracts and hold credentials. I recommend against general availability until at least one accountable human for security and operations is engaged and an external penetration test is done (Q6, G6).
2. **Treating "trusting its maturity" as a backlog.** Shopify's maturity represents more than a decade of work by more than a thousand developers [E13]. Trust its *shape* (the domain model, the extension points, the published practice), and choose a v1 subset of it.
3. *Removed by amendment 2.*
4. **Reading "No other platform's reading shapes the model" too broadly.** It should exclude other commerce platforms' evidence, as the brief does. It should not exclude standards, published engineering practice, or the first market's own laws, providers and conditions, all of which the plan needs. I recommend the founder confirm this boundary when answering Q1.
5. **Using one word, "market", for two things.** Keep "Markets" for a merchant's groups of buyers, as Shopify uses it [E26a], and give the country-level configuration its own name: the founder's decision, Q17.
6. **Tolerating secrets in the evidence.** Even if they are synthetic and rotated, keep them out of every new artifact and scan for them. Habits formed on test data carry over into production.

---

## 6. Limits of this assessment

- I did not read the earlier work or the other evidence repositories. This plan may therefore repeat or contradict findings I have not seen.
- I read the evidence by targeted sampling. Numbers marked "my count" or "my sums" are computed from the cited files.
- Yemen's facts are gathered in S1 (the short list) and S5 (amendment 5); until then, anything about Yemen is an assumption.
- Durations, scores and targets are assumptions, to be re-estimated at G3 from measured throughput.

---

## 7. References

### 7.1 Shopify evidence, at `observed-sh@04de369da9ac84ae530ae80a55749167ff4139d4`

Abbreviations:
- HC = `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual`
- EB = `structures/shopify/engineering-blog/20261031T004307Z-shopify-engineering-posts/items.jsonl`
- AS = `structures/shopify/admin-graphql-schema/2026-10/items.jsonl`
- REG = `structures/REGISTER.tsv`

**Coverage of the evidence**
- E1 `README.md:16-17`: the scope statement, "the reference Sharrwah is validated against".
- E2 `README.md:8-9`: "Nothing here interprets the platform."
- E3 `index/ledger-summary.tsv` (sums are mine):
  - `:138-150` admin mutations;
  - `:151-229` admin routes × stores;
  - `:232-234` journey units;
  - `:240-242` Help Center;
  - `:254-255` shopify.dev.
- E4 `docs/GAPS.md:46`: the API state before and after journeys is not held.
- E5 `docs/GAPS.md:47`: webhook deliveries from real events are not held.
- E6 `docs/READING.md:174`: "The router hash changed within one day."
- E7 `docs/READING.md:180-191`: tokens and secrets held as captured.

**The admin and its schema**
- E8 `structures/shopify/admin-graphql-schema/2026-10/meta.json:20`: 3,716 types.
- E9 `structures/shopify/admin-router/meta.json:18,23`: 1,364 routes, 515 with eligibility.
- E10 `AS:3704`: `WebhookSubscriptionTopic`, 236 values (my count).
- E11 `REG:132`: 21 permission categories, 142 permissions.
- E12 `derived/journey-catalog.jsonl:1-311`: 311 units of work in 72 router sections (my count).

**Engineering blog, open source and API versioning**
- E13 `EB:338`: K. Westeinde, "Deconstructing the Monolith: Designing Software that Maximizes Developer Productivity", 2019-02-21: the modular monolith; "worked on for over a decade by more than a thousand developers". Also `REG:142`: 436 posts.
- E14 `EB:369`: X. Denis, "A Pods Architecture To Allow Shopify To Scale", 2018-03-02.
- E15 `REG:140`: the open-source repositories. Also `EB:55`: "A Packwerk Retrospective", 2024-02-07.
- E16 `EB:132`: B. de Water, "10 Tips for Building Resilient Payment Systems", 2022-07-28.
- E17 `EB:32`: K. Petroski and M. Frail, "How we prepare Shopify for BFCM", 2025-11-20.
- E18 `raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@21171067` <https://shopify.dev/docs/api/usage/versioning.md>, body line 67.

**Payments**
- E19 `HC/payments/shopify-payments/supported-countries.md:7,14-54,52`.
- E20 `HC/payments/manual-payments.md:5,7,10`.
- E21 `HC/payments/third-party-providers.md:5,7`.
- E22 `structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl:26`: `MutationRoot`, with 16 session mutations.
- E23 `raw/runs/20261005T013804Z-sweep-paid-store/steps/376.text.txt`:
  - `:20-38` settings areas;
  - `:44-46` the provider and its "0.6% transaction fee";
  - `:55` manual payment methods.

  Also `steps/008.text.txt:32`: "Yemeni Rial (YER)".
- E24 `index/instruments.json:94,131`: stores with a Yemen business entity and YER.
- E25 Capabilities coupled to Shopify Payments:
  - (a) `HC/payments.md:9,17`;
  - (b) `HC/markets/customizations/local-currencies.md:3`;
  - (c) `docs/GAPS.md:28`.

**Markets, tax, shipping and languages**
- E26 `AS`:
  - (a) `:1951` Market;
  - (b) `:217` BusinessEntity;
  - (c) `:1162` DeliveryCarrierService;
  - (d) `:978,985,1885`: the country, currency and language codes include YE, YER and AR.
- E27 `REG:23`: 13 Functions APIs; see also `structures/shopify/functions-graphql-schema/` (13 directories).
- E28 `HC/taxes.md:3,5,8` and `HC/taxes/shopify-tax.md:7`.
- E29 Shipping:
  - (a) `HC/fulfillment/setup/shipping-rates/third-party-carrier-calculated-shipping.md:3`;
  - (b) `HC/fulfillment/setup/delivery-methods/local-delivery.md:5`.
- E30 Languages:
  - (a) `REG:144`: the admin, 49 languages, Arabic in beta;
  - (b) `REG:145`: checkout, 50 languages;
  - (c) `REG:121`: the storefront, 136 languages;
  - (d) `REG:12`: Help Center URLs, 2,592 in English and 2,591 in Arabic;
  - (e) `raw/runs/20261031T014053Z-journey-admin-language-arabic/steps/030.html:1`: `lang="ar-YE"`, `dir="rtl"`.

**Compliance, plans and licences**
- E31 to E33: *removed by amendment 2.*
- E34 `structures/shopify/webhook-sample-payloads/shopify.dev@2026-07/items.jsonl:49,55,188`.
- E35 Plans and prices:
  - (a) `REG:87`: billing plans;
  - (b) `REG:141`: pricing pages for each country site.
- E36 `REG:54`: SOC 3 reports; a PCI DSS v4.0.1 attestation for service providers.
- E37 `REG:33`: 795 changelog items.
- E38, E39: *removed by amendment 2.*
- E40 `structures/shopify/open-source/packwerk/main@31e534283f93/files/packwerk-31e534283f93a225b520cddab3c2d735557c76de/LICENSE.md:3`; `structures/shopify/open-source/semian/main@ddeab8c829b6/files/semian-ddeab8c829b67d4e2a8c3401fa6599e1ad25263e/LICENSE.md:1`.
- E41 `REG:82`: 204 tracking carriers.

### 7.1b Shopify evidence added on 3 November, at `observed-sh@cc5d3f26404f403cd71b5222078a8827dfa35831`

- E42 `structures/REGISTER.tsv:160`: `shopify/admin-api-state`, the Admin API's state before and after each step of the buyer and order journeys on demo-fake-dev-store, whose shop currency is YER.
- E43 `structures/REGISTER.tsv:162`: `shopify/webhook-deliveries`, the deliveries Shopify sent while those journeys ran.
- E44 `index/run-notes.tsv:398`: after the Cash on Delivery checkout, "#1007 PENDING, paymentGatewayNames ['Cash on Delivery (COD)'], one SALE PENDING (manualPaymentGateway true)".
- E45 Shopify's `worldwide` library, at `structures/shopify/open-source/worldwide/main@15d9289e57cb/files/worldwide-15d9289e57cb49f99a4f10e392c4114cd72cc06c/`:
  - `README.md:108-114`: the library's unit is the region, "or political subdivision"; it keeps the name "country" for "what we describe in our user interface as" a country / region;
  - `data/regions/YE.yml:1-23`: Yemen's data, keyed `code: YE`: its currency (YER), tax rate and tax name, unit system, phone prefix, week start, address format, languages and time zone.

### 7.2 Published practice and other sources (accessed 1 November 2026)

**Standards**
- P1 ISO/IEC/IEEE 12207:2017, *Software life cycle processes*. https://www.iso.org/standard/63712.html
- P2 ISO/IEC/IEEE 29148:2018, *Requirements engineering*. https://www.iso.org/standard/72089.html
- P3 ISO/IEC/IEEE 42010:2022, *Architecture description*. https://www.iso.org/standard/74393.html
- P4 ISO/IEC 25010:2023, *Product quality model*. https://www.iso.org/standard/78176.html
- P5 ISO 31000:2018, *Risk management: Guidelines*. https://www.iso.org/standard/65694.html

**Process, risk and decisions**
- P6 B. W. Boehm, "A Spiral Model of Software Development and Enhancement", *IEEE Computer* 21(5), 1988. https://doi.org/10.1109/2.59
- P7 R. G. Cooper, "Stage-Gate Systems: A New Tool for Managing New Products", *Business Horizons* 33(3), 1990. https://doi.org/10.1016/0007-6813(90)90040-I
- P8 G. Fairbanks, *Just Enough Software Architecture: A Risk-Driven Approach*, 2010. https://www.georgefairbanks.com/book/
- P27 A. J. Dorofee et al., *Continuous Risk Management Guidebook*, SEI, 1996. https://www.sei.cmu.edu/library/continuous-risk-management-guidebook/
- P28 G. Klein, "Performing a Project Premortem", *Harvard Business Review*, 2007. https://hbr.org/2007/09/performing-a-project-premortem
- P29 J. Bezos, *2015 Letter to Shareholders* (Type 1 and Type 2 decisions), 2016. https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm

**Requirements and architecture**
- P9 K. Pohl, G. Böckle, F. van der Linden, *Software Product Line Engineering*, Springer, 2005. https://doi.org/10.1007/3-540-28901-1
- P10 R. Kazman, M. Klein, P. Clements, *ATAM: Method for Architecture Evaluation*, CMU/SEI-2000-TR-004, 2000. https://insights.sei.cmu.edu/library/atam-method-for-architecture-evaluation/
- P11 E. Evans, *Domain-Driven Design*, Addison-Wesley, 2003. https://www.domainlanguage.com/ddd/
- P12 M. Nygard, "Documenting Architecture Decisions", 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- P13 *MADR: Markdown Architectural Decision Records*. https://adr.github.io/madr/
- P14 G. Starke, P. Hruschka, *arc42*. https://arc42.org/
- P15 S. Brown, *The C4 model*. https://c4model.com/
- P19 N. Ford, R. Parsons, P. Kua, P. Sadalage, *Building Evolutionary Architectures*, 2nd ed., O'Reilly, 2022. https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/
- P44 A. Wiggins, *The Twelve-Factor App*, 2011. https://12factor.net/
- P45 Amazon Web Services, *SaaS Lens, AWS Well-Architected Framework*. https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html

**Delivery and reliability**
- P16 A. Cockburn, *Crystal Clear*, Addison-Wesley, 2004 (the walking skeleton); summarized in C. Shank, "Start with a Walking Skeleton", *97 Things Every Software Architect Should Know*, O'Reilly, 2009. https://www.oreilly.com/library/view/97-things-every/9780596800611/ch60.html
- P17 J. Humble, D. Farley, *Continuous Delivery*, Addison-Wesley, 2010. https://continuousdelivery.com/
- P18 N. Forsgren, J. Humble, G. Kim, *Accelerate*, IT Revolution, 2018; the DORA research program. https://dora.dev/
- P20 B. Beyer, C. Jones, J. Petoff, N. R. Murphy (eds.), *Site Reliability Engineering*, O'Reilly, 2016. https://sre.google/sre-book/table-of-contents/ (the production readiness review is in chapter 32: https://sre.google/sre-book/evolving-sre-engagement-model/)
- P21 B. Beyer et al. (eds.), *The Site Reliability Workbook*, "Implementing SLOs", 2018. https://sre.google/workbook/implementing-slos/

**Security**
- P22 M. Souppaya, K. Scarfone, D. Dodson, *Secure Software Development Framework (SSDF) 1.1*, NIST SP 800-218, 2022. https://csrc.nist.gov/pubs/sp/800/218/final
- P23 OWASP, *Application Security Verification Standard 5.0.0*, 2025. https://owasp.org/www-project-application-security-verification-standard/
- P24 Z. Braiterman, A. Shostack et al., *Threat Modeling Manifesto*, 2020. https://www.threatmodelingmanifesto.org/
- P25 OpenSSF, *SLSA v1.1*. https://slsa.dev/spec/v1.1/
- P26 PCI Security Standards Council, *PCI DSS v4.0.1*, 2024. https://www.pcisecuritystandards.org/document_library/

**Agentic engineering**
- P30 E. Schluntz, B. Zhang, "Building effective agents", Anthropic, 2024. https://www.anthropic.com/engineering/building-effective-agents
- P31 Anthropic, "How we built our multi-agent research system", 2025. https://www.anthropic.com/engineering/multi-agent-research-system
- P32 Anthropic, "Effective context engineering for AI agents", 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- P33 Anthropic, "Claude Code: Best practices for agentic coding", 2025. https://www.anthropic.com/engineering/claude-code-best-practices
- P34 Google, *Engineering Practices: Code Review*. https://google.github.io/eng-practices/review/

**Documentation, versioning and linking**
- P35 D. Procida, *Diátaxis*. https://diataxis.fr/
- P36 *Conventional Commits 1.0.0*. https://www.conventionalcommits.org/en/v1.0.0/
- P37 T. Preston-Werner, *Semantic Versioning 2.0.0*. https://semver.org/spec/v2.0.0.html
- P38 O. Lacan, *Keep a Changelog 1.1.0*. https://keepachangelog.com/en/1.1.0/
- P39 GitHub Docs, "Getting permanent links to files". https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files

**Accessibility and language**
- P40 W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, 2023. https://www.w3.org/TR/WCAG22/
- P41 W3C Internationalization, "Structural markup and right-to-left text in HTML". https://www.w3.org/International/questions/qa-html-dir
- P42 Unicode Consortium, *Common Locale Data Repository (CLDR)*. https://cldr.unicode.org/

**Product-line configuration** (added on 3 November, for Q17)
- P48 K. Czarnecki, S. Helsen, U. Eisenecker, "Staged configuration through specialization and multilevel configuration of feature models", *Software Process: Improvement and Practice* 10(2):143–169, 2005. https://doi.org/10.1002/spip.225
- P49 R. Mietzner, A. Metzger, F. Leymann, K. Pohl, "Variability modeling to support customization and deployment of multi-tenant-aware Software as a Service applications", PESOS 2009, ICSE workshop, pp. 18–25. https://doi.org/10.1109/PESOS.2009.5068815
