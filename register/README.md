# Question rows: what they are

Two sets of questions that agents wrote before `PLAN.md`. **They are not Sharrwah's requirements.** Q3 and `PLAN.md` place them against the subjects, as inputs only, and each placement is read from its question text. Some may still be genuine questions. Their context is set out below.

| File | What it is |
| --- | --- |
| `pay-questions.tsv` | **The 81 payment rows, PAY-01 to PAY-81.** Earlier work expanded them while thinking about how to model payments. The founder's artifact "Obligation to Payout" (claude.ai/artifact/Af44iTiRyauqt7bhr8KrP8) shows them, and `model/obligation-to-payout.html` is a copy. |
| `km-questions.tsv` | **The Knowledge Map's 179 questions.** They were copied on 12 October 2026 from the founder's artifact "Sharrwah Knowledge Map" (claude.ai/artifact/Wj9kpisrCUiRUCmeCzRRZM, version 1791419535-9835). Their ids are prefixed `KM-`, because the map's PAY-01 to PAY-07 are different questions from the payment rows' PAY-01 to PAY-07. `km_id` keeps the original id. |
| `km-artifact-1791419535-9835.html` | The page as read, with sha256 `b7c82dc930e32139c26193cb234f87e23f8fa653d30c70d840f34d32b806a24d`. The rows were taken from its embedded data. |
| `pay-evidence-additions.tsv` | Evidence entries the payment rows cite. |

**Why they need care:**
- Agents wrote both sets from earlier, smaller states of observed-sh and observed-sa, at old commits.
- Their `evidence`, `pointers` and `other_sources` columns are not trusted, and no study cites them.
- A question can carry a frame or an answer inside it. Read as a requirement, it would steer the work.

So a brief that places rows reads only `id`, `question`, `needed_by` and `lane`.

## The Knowledge Map's questions under `METHOD.md`, 24 October 2026

**Where they come from.**
- The founder's page "Sharrwah Knowledge Map", data as of 8 October 2026. An earlier session made it before this repository existed.
- Its own method was never run: claims, a second agent re-deriving them, and decisions to the founder.
- The copy here is byte-identical to the live page as read on 24 October (same sha256).

**What is still worth having:**
- **The questions themselves,** especially the architecture questions that nothing else here asks:
  - tenancy and the engineering set, ENG-01 to ENG-08;
  - authorization (STF-07), isolating apps' code (APP-06), and events and webhooks (API-02);
  - account and store structure (ACC-01, ACC-05).
- **For each question:** what it feeds (a decision, a model, an arc42 section), when it is needed, and its risk.
- **Its kinds of question.** "World: what fills a slot … it does not define the product" is the market guard in one line (`METHOD.md` section 3a).
- **Its source types,** in the page's "Source types" tab. For each kind of source: what it is good for, what it can't tell, and how to grade it. `METHOD.md` section 5 weighs outside experience by them.

**What is stale.** It is repaired only when a row is used:
- **Its Salla citations.** 46 of the 51 Salla evidence paths no longer exist, because observed-sa was reorganized: `salla/api.salla.dev/organizes/dashboard-nav/` is now `structures/salla/dashboard-nav/`. As a result, 130 of the 153 questions with evidence cite at least one moved path. `method/km_select.py` marks them.
- **Its Shopify citations.** All 145 Shopify paths still exist, but none is pinned to a commit.
- **Its pointers,** such as counts of roles or permissions, are from 8 October.

**What conflicts with the founder's later decisions:**
- **Rows that assume Saudi Arabia's rules** (ZATCA, SAMA, PDPL): KM-TRU-04, KM-TRU-06, KM-PAY-06, KM-PAY-07, KM-TAX-04. They are read market-neutral.
- **Rows naming practitioners as a source:** KM-ONB-02, KM-ONB-04, KM-PAY-07, KM-SHP-06, KM-MIG-02, KM-MIG-03, KM-WLD-05. Merchants are never asked (founder, 24 October).
- **"A walking skeleton"** among the experiment sources, and the timing "slice", meaning before an area's first build slice. Production code waits for `METHOD.md` section 5's definition of ready. Spikes are allowed.
- **"Decisions … as ADRs owned by the founder"** no longer holds. Only one-way decisions are the founder's (`METHOD.md` section 3).
- **KM-MTH-04,** the choice of other references, is answered by `METHOD.md` section 5.

**How the questions are used now:**
- **At a subject's framing,** `method/km_select.py S-NN` lists the subject's questions. A question belongs to a subject by its area, or by its id in the subject's row of `decisions/subjects.tsv`.
- **Each question gets a disposition** in the two columns added on 24 October:
  - `disposition`: answered, driver, scenario, deferred, or dropped;
  - `disposition_ref`: the record, scenario or trigger.
- **At the end,** the 179 questions and the 81 payment rows are reconciled against the accepted decisions (`METHOD.md` section 8).
- **What isn't done:** the questions are not re-checked in bulk, and the page is not rebuilt.

**The source types,** as the page gives them. Under `METHOD.md`, PRAC never includes merchants, and EXP means spikes and tests, not a walking skeleton.

| Code | Source | Good for | Can't tell you | Grading | Examples |
| --- | --- | --- | --- | --- | --- |
| DECL | Platform declaration | What the platform says it offers, in its own names and grouping | Whether it behaves that way, or why it exists | Authoritative on intent; check against OBS, because declarations disagree with what is served (sa.readme) | Docs, help centre, API schemas, sitemaps, llms.txt, changelogs, plan tables |
| SHIP | Shipped artefact | What the client actually contains: routes, operations, components, flags | What the server allows for a given store, plan or role | Strong for existence, weak for availability | Route manifests, compiled GraphQL documents, served navigation trees, APKs, CLI packages, theme files |
| OBS | Observed behaviour | What happened on a named store, plan, region, role and date | Whether it generalises to other stores, plans or regions | Strongest for behaviour; always cite the instrument it was seen with (sh.instruments) | Journeys, sweeps, staff sweeps, Android walks, received emails, webhook deliveries |
| IDX | Capture index | Where to look, coverage and joins | Anything about the platform that is not already in the bytes | A finding aid only, never evidence on its own | Ledgers, COVERAGE.tsv, journey catalog, staff gates |
| REF | Further reference platform | Whether a feature belongs to the product class or to one vendor | Detail and behaviour, unless captured | One more vote on commonality; read at declaration level | Zid, BigCommerce, Adobe Commerce, WooCommerce docs and APIs |
| OSS | Open-source implementation | How the same behaviour is built: data models, state machines, algorithms | Product completeness, or what SaaS merchants actually get | Strong for internals; check the fit with the product class | Saleor, Medusa, Sylius, Solidus and Spree, Magento Open Source, Vendure |
| STD | Standard or specification | Formats and protocols the data and APIs should follow | Product behaviour | Normative wherever it is adopted | ISO 4217, ISO 3166, GS1, schema.org, OAuth 2.0 and OIDC, WebAuthn, UBL, PCI DSS, UCP, MCP |
| LAW | Law and regulators | What a market requires of platforms and merchants | How platforms implement it (Salla shows one implementation for its market) | Normative; cite the instrument and its date | ZATCA e-invoicing rules, PDPL, e-commerce and consumer protection law, SAMA rules |
| PROV | Provider documentation | What fills a slot: a payment, carrier, tax or messaging provider's contract | The platform's own behaviour | Authoritative for the provider; changes often | Payment gateway, BNPL, carrier, e-invoicing, SMS and WhatsApp provider docs |
| ECO | Third-party ecosystem | What merchants add, pay for and complain about; gaps in the core | The platform's intent | Weak one by one, strong in aggregate | App listings and reviews, community forums, partner sites, Wayback Machine snapshots |
| LIT | Literature and engineering writing | Patterns, trade-offs, how mature teams built similar systems | Facts about this product | Strong for method; a vendor blog is one company's account | Books, papers, vendor engineering blogs and talks |
| PRAC | Practitioners | Tacit knowledge: how merchants and operators really work | The full product surface | Anecdotal; corroborate | Merchants, agencies, former platform engineers, support staff |
| EXP | Own experiment | Feasibility, performance and cost on Sharrwah's own stack | The reference product | Strongest for engineering questions | Spikes, a walking skeleton, load tests, prototypes |
| DEC | Founder decision | What Sharrwah chooses | Nothing about the world: a decision is not evidence | Recorded with date and rationale (an ADR) | Scope, sequencing, pricing, market |
