# The architecture plan

**Status: a draft by the coordinating session, 30 October 2026, revised on 31 October with every finding of its review.** It comes to the founder at GM, with the class's model's extent and the Knowledge Map's page rebuilt from it. Architecture starts on the founder's go on this plan (`PLAN.md`, Stage 4A; `founder-decisions.tsv`, 30 October). Section 1 was drafted with the dry run of the model, so that the model records what architecture needs before its other domains run. The whole was finished on 31 October, once the held pass's first stage was in the model. It was reviewed by an agent that made none of it, and each finding was taken as the review's last section records (`architecture/plan-review.md`). Section 1's counts are measured again before GM, once the held pass's second stage, the qualities pass, the omission review and the final review have run.

## For the founder, on one page

**What this is.** How the architecture will be worked out once the class's model has its extent: what it needs to know, and from where; who decides, and how each decision is made, recorded and checked; what comes first; what "keeping room" means; and how the whole is evaluated. It decides two things of the architecture, and one reading of how sources are graded, each listed for your veto in section 7. The rest is how the work is done.

**What you decide:** your go on this plan, at GM. Nothing else in it is yours, except where an architecture decision touches your list: which markets, in what order and when, and which merchants Sharrwah goes after first; plans and prices; commercial agreements and partners; the company, its legal structure and licences, and whether Sharrwah holds funds; spending; and whether Sharrwah's own company runs a service in the merchant's business, where and when. Building or switching on an arrangement that holds sellers' money, A or B, is yours too, under your guard: the design keeps room for both, empty while C holds (your decisions of 18, 25 and 26 October). Such a decision comes to you with its evidence, its options and a recommendation. Every other decision is engineering's, and each is listed for your veto at the next report.

**What this plan decides, for your veto** (section 7):
- every amount of money points to an entry in one table of currencies, decided now, before the currency subject runs. It changes a ruling of the markets subject that you passed on 30 October, which left this choice to the currency subject;
- each part of the platform owns its records, and the others reach them only through it;
- Zid, BigCommerce and WooCommerce are graded as three of the five references, like Shopify and Salla, and not as further reference platforms, as the source types you chose name them.

**What happens on your go,** in this order:
1. The quality scenarios and the scale bands are written (section 5), and the model's capabilities are grouped into candidate parts (section 3). They come to you in a first short report, before any decision builds on them: the bands stand in for your scale numbers, so you can correct them.
2. The six decisions that cut across every area (section 3). Each keeps open what a subject not yet run will decide.
3. Then the parts, in the order section 3 sets, each after the subjects it waits for, beside the subjects still to run.
4. The whole is evaluated after step 2, and after each group of parts (section 5).

**What it costs.** Each step has a budget, set before it starts from measured cost, and recorded in `STATE.md`. Past a quarter over it, the cost comes to you with a projection, and the work goes on, re-planned to cost less (`PLAN.md`, section 8).

**What you'll see:** at each report:
- each decision made, in plain words, for your veto: what it decides, why, what it risks and its alternative;
- the options kept open, with their cost;
- the evaluation's findings;
- any decision on your list, with its evidence, its options and a recommendation, or defer;
- the cost against the budget.

A veto reverses a decision as section 2 says.

## Words used below

- **variation point:** a place in the design where markets, stores or plans can differ;
- **binding time:** when that difference is set: at build, when a market is set up, or by a store's setting;
- **indirection:** a reference that lets what it points to change without changing the records that use it;
- **utility tree:** your qualities in your order, each broken into tests with a measure;
- **sensitivity point:** a design choice that a quality depends on;
- **trade-off:** a choice that helps one quality and costs another;
- **attribute-driven design:** designing step by step, each step settling the decisions that the highest-ranked qualities depend on.

## 1. What architecture needs to know, and where each part comes from

Each source is graded by the Knowledge Map's source types, with what each can't tell (`studies/class-model/seed/km-source-types.tsv`; the founder, 30 October). The grade goes with the source, not the platform: a Zid help page is a platform's declaration, and WooCommerce's release is shipped code.

Each citation's type follows section 6's kind (`PLAN.md`, section 6), which `method/source_kinds.py` assigns by rule: observed is OBS, shipped is SHIP, and stated and official page are DECL. Where the two schemes sort a source differently, the Knowledge Map's sort holds, and section 6's kind is kept beside it, so that like is still compared with like:
- an API's published schema is DECL, though section 6 calls it shipped;
- a list or menu the admin served in a recorded session is SHIP, though section 6 calls it observed.

The model records no type: each design grades the citations it uses.

Each type's limits, in the Knowledge Map's own words:

| Type | What it can't tell | Its grading |
| --- | --- | --- |
| DECL | Whether it behaves that way, or why it exists | Authoritative on intent; check against OBS, because declarations disagree with what is served (sa.readme) |
| SHIP | What the server allows for a given store, plan or role | Strong for existence, weak for availability |
| OBS | Whether it generalises to other stores, plans or regions | Strongest for behaviour; always cite the instrument it was seen with (sh.instruments) |
| ECO | The platform's intent | Weak one by one, strong in aggregate |
| OSS | Product completeness, or what SaaS merchants actually get | Strong for internals; check the fit with the product class |
| STD | Product behaviour | Normative wherever it is adopted |
| LAW | How platforms implement it (Salla shows one implementation for its market) | Normative; cite the instrument and its date |
| PROV | The platform's own behaviour | Authoritative for the provider; changes often |
| LIT | Facts about this product | Strong for method; a vendor blog is one company's account |
| EXP | The reference product | Strongest for engineering questions |
| DEC | Nothing about the world: a decision is not evidence | Recorded with date and rationale (an ADR) |

What each part of architecture's knowledge comes from. The last column says only what a row adds to its types' limits above:

| What architecture needs | Where it comes from | Source types | What it can't tell, beyond its types' limits |
| --- | --- | --- | --- |
| What the class establishes: each capability, where each platform puts it, how many establish it, its kind | The class's model (`studies/class-model/`) | DECL, SHIP, OBS, as each cited statement's kind | What a platform doesn't publish |
| The class's data and events: the objects, webhook topics and access scopes each capability shows | The model's evidence: the `boundary` statements of each capability's concerns, derived per capability at the merge (`studies/class-model/merged/interfaces.tsv`) | SHIP, DECL | What the server does with them; a platform's internal model |
| What varies, by market, store and plan | The subjects' registers (S-01, S-02, and each later one); the model's `decides` statements and scopes | DECL, SHIP, OBS, as each cited statement's kind. A register's causes are readings, and its rulings engineering's: neither is evidence | A market not yet studied |
| What fills a slot in a market: providers, partners, law | The model's slot fillers: a platform's statement naming a provider or a law (DECL, SHIP, OBS). Each subject's evidence. Providers' and regulators' own documents (PROV, LAW) | DECL, SHIP, OBS; PROV, LAW | Which market a filler serves, unless its statement's scope names one |
| What merchants add through apps and partners | The app and theme stores' listings the model cites, read where a slot's design needs them | ECO | The platform's intent; weak one by one, strong in aggregate |
| The qualities the class states: its commitments, bounds, attestations, and how data is kept | The qualities pass (`PLAN.md`, Stage 4A, "The qualities pass"), each quality quoted at its commit, on the capability it bears on | DECL, SHIP | Real performance; Sharrwah's own numbers |
| What Sharrwah has decided, and the quality order | `founder-decisions.tsv` | DEC | Nothing beyond its type's |
| Scale | The founder, later. Until then, engineering's stated bands | DEC; an assumption, marked as one | What load will really come |
| How comparable systems are built | Open-source commerce systems, standards, engineering writing, read for each decision that needs them | OSS, STD, LIT | Nothing beyond their types' |
| How one of the five built itself | Shopify's own engineering talks, posts and repositories, held in `evidence/shopify-engineering/` (E001 to E040, captured 10 October 2026): payments beside the rest of the platform, pods, Packwerk, Functions, payment apps and the provider contract | LIT, OSS | Whether the design still stands: the detailed write-ups of its internal payment architecture date from 2019 to 2022. Why another of the five built otherwise. What it costs to run |
| Whether a design works on Sharrwah's stack, at what cost | Spikes (section 2) | EXP | Nothing beyond its type's |

**Left out:**
- **Practitioners (PRAC):** merchants are never asked (`founder-decisions.tsv`, 24 October). Agencies and former platform engineers aren't planned. Where documents can't settle a decision, a request to reach one may come to you, since contacting them, and paying for advice, are yours (`PLAN.md`, section 3);
- **capture indexes (IDX):** how evidence is found, never what is cited (below);
- **REF:** the Knowledge Map's file names Zid, BigCommerce and WooCommerce as further references: one more vote, read at declaration level. Here they are three of the five references, which the model counts alike (`PLAN.md`, Stage 4A), so their sources are graded by type, as Shopify's and Salla's are. REF is kept for a platform beyond the five, such as Adobe Commerce, read only where a decision needs one more comparison. This reading of the file is engineering's, listed for your veto (section 7).

**Where a decision needs more than the model holds,** its design reads the evidence through the evidence map and each repository's own guides and indexes first, then searches (`PLAN.md`, section 6; your decision of 30 October). What isn't held goes as a capture request in `handoffs/`, not to you (your decision of 27 October).

**What the model must record for this.** Its brief records the capabilities, cells, qualities and slot fillers. Each capability's data, events and deciding statements are derived by the merge in two grades (the dry run's review, S15; `studies/class-model/review-dry-run-rulings.md`, convention 10):
- **exact:** the `boundary` and `decides` statements its cells cite;
- **by landing:** the other statements of the concerns landed in it. This attribution is coarse: a coarse concern's statements go to its landing capability, though some belong to its children.

Each design refines the coarse grade as it reads its capabilities in depth. No part writes more, so the extent's cost doesn't grow for it, and what is coarse is said plainly.

As merged at `d9524f74`, what is missing is a gap, not a derivation (the dry run's review, S15):
- 572 of the 1,215 cells that hold statements have no data or events of their own platform, and 260 nothing that decides them; 74 of the 367 capabilities have no data or events from any platform. A design that needs them reads the evidence for them, through the evidence map (`PLAN.md`, section 6);
- the exact grade is incomplete too: a part cites a sample of a family of topics or scopes, and the rest goes by landing to the parent, or nowhere;
- a held-pass entry is `boundary` or `decides` by its structure, not by what it says;
- **qualities:** the model holds few today. Of its 3,881 quality rows, 3,297 are Shopify's and 2,609 come from one structure, Shopify's pricing pages; about 2,490 are prices, fees, rates or trials (a reading, by a pattern on the label). So they are mostly prices and plan allowances (`architecture/plan-review.md`, APR-7). Of what the first decisions need, little is held: uptime from Shopify, Salla and BigCommerce; where data lives from Shopify and BigCommerce; card-data certification from Shopify, WooCommerce's payments service and BigCommerce. Salla holds nothing on where data lives or on card data, and Zid nothing on uptime or on card data. The plan therefore relies on the qualities pass (`PLAN.md`, Stage 4A, "The qualities pass"), which the coordinator added on 31 October. It reads the class's stated qualities from the evidence's side, before the omission review. A quality there is a commitment, a bound, an attestation, or how data is kept, by the characteristics of ISO/IEC 25010:2023, with isolation between stores, where data lives and identity named. Prices, fees and plan allowances are relabelled as the plans' terms, and kept. Architecture reads its row on qualities, above, from that pass. The first decisions read the evidence for what it still doesn't hold, and say so;
- **slot fillers** carry no market. A filler's market is its statement's scope, where one is stated; what fills a slot in a given market comes from the subjects;
- **scopes** are the statements' own words, untyped. A design that needs a market's, a plan's or a store's scope (configuration, item 6, and the test of `reports/intent-review.md`, section 14) types them as it reads them.

The held pass's second stage, the qualities pass, the omission review and the final review may close some of these before GM; the counts are measured again then.

## 2. Who decides, and how each decision is made, recorded and checked

- **Who decides:** engineering, by the founder's intent. A decision that touches the founder's list goes to the founder. Every other decision is listed for the founder's veto; this plan's own are in section 7.
- **How a decision is made:** by its drivers, as attribute-driven design does it (Cervantes & Kazman 2016; its five kinds of driver are a reading of that book):
  - its design purpose: one platform for many markets, with the first version's build planned at the shore on the architecture written by then (`PLAN.md`, section 1);
  - the capabilities it serves, from the model (the design's primary functionality);
  - the quality scenarios it must meet (section 5);
  - the architectural concerns it settles: the six first decisions (section 3) are such concerns;
  - its constraints: the law where a market's law binds; the subjects' rulings, which a design may rule again on evidence, listed for your veto; and your decisions in force, which engineering doesn't reopen: Decision 1 (C in every market at launch, with its three defaults); E1 and E2 (who holds sellers' money is a market's setting; an order's payment record is the same whoever holds it; a holder's ledger is a separate part, empty under C); default 2, at launch; the guard on A and B; and RD2's plan items, which are yours.

  The options come from the references first. Where their shapes differ, the decision weighs which is better and says why (`PLAN.md`, Stage 4A). Then come established designs and standards.
- **How it is recorded:** one record per decision, in `architecture/records/`, in the form of an architecture decision record (Nygard 2011), with:
  - its context and drivers;
  - the options and the evidence for each;
  - the decision and why;
  - what it keeps open, what it closes, and what would reopen it;
  - its status: proposed, accepted on its review, vetoed, or superseded by a later record, which it names. An accepted record is never edited: a change is a new record that supersedes it (Nygard 2011);
  - what it builds on: the records, rulings and capabilities it rests on, the capabilities at the model's commit.
- **The description:** the architecture description names its stakeholders and their concerns (ISO/IEC/IEEE 42010:2022): you (your list and your quality order), engineering, the teams who set up each market, the developers of apps and providers, and the build that validates against it. Each view answers named concerns:
  - parts: each part, the capabilities and areas it holds, and what it hides;
  - records: which part owns each record, and how the others reach it (Evans 2003, the context map);
  - variation: each variation point, its variants and its binding time (Pohl, Böckle & van der Linden 2005);
  - where data lives: per market and store, once S-08 has run;
  - slots and events: how apps, providers and couriers plug in, from the model's data and events.

  The records sit beside the views, and each view names the records it rests on. The description is enough for the first version's build when each capability that version needs sits in a part, each first decision is accepted, and each option kept open has its check. The build's requirements and engineering documentation are planned with it, at the shore (`PLAN.md`, section 1).
- **How it is checked:**
  - an agent that made none of it reviews each record against its evidence before anything builds on it;
  - every option kept open has its check (section 4);
  - the whole is evaluated after the first decisions, and after each group of parts (section 5).
- **How a decision is reversed:**
  - your veto: the record is marked vetoed. Engineering takes its alternative, or the one you name; each record that builds on it is listed and ruled again on its evidence, and the list comes with the next report;
  - a subject's result: a record that conflicts with a subject's ruling is reopened with the subject's evidence, not forced to fit, and ruled again for your veto. A conflict with your own decision comes to you (`PLAN.md`, Stage 4A, for the subjects' points);
  - a change in the model: when a capability a record cites changes, the records that cite it are listed and checked again (`PLAN.md`, section 7, risk 7).
- **Spikes,** for the questions the model raises (your decision of 29 October: architecture grows "with spikes for the questions the model raises"). Engineering decides a spike, for a question a record needs answered, from the budget of the step that record belongs to. Its result is cited, as EXP, in the record it serves. A spike is throwaway code: production code waits (section 6).

## 3. What comes first

**The model's areas aren't architecture's parts.** The 41 areas, 36 of which hold capabilities, index what the class does (`studies/class-model/seed/km-areas.tsv`). Architecture's parts are cut by what changes together and by what data they own: each decision likely to change sits behind its own module (Parnas 1972), and each part owns its model and its language (Evans 2003, bounded contexts). That each part owns its records is a decision of this plan, listed for your veto (section 7).
- So once the model has its extent, the coordinator groups its capabilities into candidate parts. A decision likely to change gets a module of its own first, even where several parts use it, as the currency record does (Parnas). Then the capabilities that share and change the same records form a part (Evans). Each part records which capabilities and areas it holds, and what it hides. An agent that made none of it reviews the grouping against the model before any decision builds on it.

**The decisions that cut across every area come first,** as attribute-driven design's first iteration settles the overall structure for a new system:
1. how stores are kept apart, and where their data lives;
2. identity and permissions: staff, customers, apps and partners;
3. money records and currency: how every amount names its currency (section 4's worked example; section 7's first decision);
4. markets and the seller's country: S-02's two entry points (E1, E2) and the business record (D1);
5. events and extension points: how apps and providers plug into the class's slots;
6. configuration: how a setting is held for a store, varied per market and limited per plan (S-02's D6; plans and prices are the founder's).

Each first decision keeps open what a subject not yet run will decide (`studies/subjects/subjects.tsv` gives each subject's question; which subjects each decision meets is a reading of those questions):

| First decision | Subjects it meets | Kept open until they run |
| --- | --- | --- |
| 1. How stores are kept apart, and where their data lives | S-08 | where data lives and is processed, and under which law |
| 2. Identity and permissions | S-07 | who verifies sellers, and how |
| 3. Money records and currency | S-04, S-05, S-09, S-11 | what identifies a currency (unless section 7's first decision stands); the payment, tax and charge records' own fields |
| 4. Markets and the seller's country | S-03, S-07 | the contracting company in each market; which countries are served |
| 5. Events and extension points | S-04, S-10 | how a payment provider or a courier connects, and what happens when one fails |
| 6. Configuration | S-11 | what Sharrwah charges, and each plan's limits (plans and prices are yours) |

**Then the parts,** in the order of their dependencies, the coordinator's own rule: those whose data the others refer to come first. A part waits for the subjects that cover its open questions. The order is set when the candidate parts are known, and it comes to you in the first report. By the model's areas:
- the parts that hold payments (PAY) after S-04;
- taxes and invoicing (TAX) after S-05;
- licences (S-06) before any part that runs a regulated activity;
- seller verification and screening (S-07) before onboarding (ONB) and trust (TRU);
- where data is stored and processed (CM-TRU-014), and hosting (CM-OPS-003), after S-08;
- shipping and delivery (SHP) after S-10;
- the platform's plans and billing (PLN) after S-11.

S-03's contracting company and S-09's currency of records bind every area that holds a contract or an amount. Each is kept open in the first decisions, as a variation point, until its subject has run. The contracting company is yours to decide (the company), so the design only keeps a place for it, and decides nothing of who it is.

## 4. What keeping room means

The founder took line (3) out of the intent on 30 October: read literally, "no commitment closes it" is something no design delivers, and "It doesn't mean designing it before its time" can be read as designing nothing now, which is how options are closed by a default nobody examined. So keeping room is defined here by established practice, the options a modular design keeps open at a stated cost (Baldwin & Clark 2000; Sullivan et al. 2001), the variation points that name their binding time (Pohl, Böckle & van der Linden 2005; Svahnberg, van Gurp & Bosch 2005), and the checks that stop an architecture's properties eroding (Ford, Parsons & Kua 2017).

**The grain.** Options are named per part: a part's interface keeps room for every capability it holds. An option gets a record of its own only where a step beyond that interface is needed: a variation point, a reference such as the currency record, or a part kept empty, as a holder's ledger is under C.

**An option is kept when:**
1. it is named, with the trigger that would exercise it;
2. the commitments that would close it are named;
3. the design takes the cheapest step that keeps it reachable, and no more: an indirection, a declared variation point with its binding time, or an interface that hides the decision;
4. what it costs to hold, what it would cost to exercise later, and how likely its trigger is, and why (a reading, where no evidence states it), are stated. A step costlier than an interface is taken only where its trigger is likely enough to be worth it. Otherwise the option is named, with what would close it, and left to the build;
5. a check stops a later commitment from closing it unexamined: a test that fails when the step is undone (a fitness function), or a review rule. Until code exists, the check is a review rule, applied to each record by its reviewer. The test is written with the first code that could undo the step.

This guards both failures: an option closed by a default nobody examined, and one built before it is worth its cost.

**A and B, under your guard,** are kept by your E1 and E2 (26 October). The first decision on money records shows E1 and E2 against the five conditions above. Where a condition disagrees with what you decided, the conflict comes to you with its evidence.

**The worked example: S-02's D9, two currency areas under one currency code.**
- **The option:** a currency that names a currency area within its code, so that prices, stored amounts and reports tell the two areas apart by currency, not only by market.
- **Its trigger:** a market where two currency areas share one code, with different notes and rates, and must be told apart in money records.
- **What would close it:** storing a bare currency code in every amount. Every money record, rate and report would then have to learn the area: a redesign.
- **The cheapest step:** every amount refers to a currency record, one per code at launch. Naming an area later is a new record, mapped to the bare code where a provider takes only the code.
- **The cost to hold:** one reference per amount, and one table of currencies.
- **The cost to exercise:** a new record, and its mapping at each provider: one module.
- **Its binding time:** when a market that needs it is set up: a new currency record and its mappings. That is a setting, not a release.
- **Its check:** until code exists, a review rule for every new money field: no record stores a bare code. With the first code of money records, a test that fails if any money record stores a bare code.
- **The gap it shows:** D9 left the currency record to S-09. The step is cheap now and a redesign later, so it is taken with the cross-cutting decisions (section 3, item 3) rather than waiting for S-09, which then decides which currencies and areas fill it. This changes S-02's D9 and its move to S-09 (S02-M6), engineering's rulings you passed on 30 October. It is listed for your veto (section 7). `PLAN.md` allows it before S-09 runs (section 6 below): it closes only a bare code in every amount, which S-02's ruling already leaves S-09 to avoid (`studies/subjects/S-02/register.tsv`, S02-D9, its `closes`). Its need comes from one market alone (S-02's D9); whether the step comes out the same without that market is a reading, given in section 7.

## 5. How the whole is evaluated

- **Quality scenarios.** Your order (trustworthiness; then coherence and user experience; then performance; then completeness, read as what each release delivers, never what the model covers) is a ranking. Architecture needs measurable scenarios. Each quality gets scenarios with a stimulus, the conditions it comes in, a response and a measure, in a utility tree (Kazman, Klein & Clements 2000). Each leaf is rated twice: how much it matters, by your order, and how hard it is to meet, by engineering's estimate. The design and the evaluation start with the leaves high on both. The tree is written before the first decision, and comes to you with the first report. Each measure is engineering's assumption, marked as one, like the bands. A measure that would become a promise to merchants, such as an uptime, comes to you.
- **Scale bands.** Until the founder gives numbers, engineering states its bands (stores, orders a day, catalogue size, markets per store), each an assumption, marked, with the decisions it touches.
- **Evaluation at milestones.** After the cross-cutting decisions, and after each group of parts, the architecture as a whole is walked through the scenarios. The walk is made by an agent that made none of the architecture. It records risks, non-risks, sensitivity points and trade-offs. The plan's change scenarios are walked too: a second market, the company based elsewhere, the first market dropped (`PLAN.md`, section 6, step 7), and regional fit's: a market's local payment provider or courier plugs into its slot with no change to the core.

## 5A. Risks, and how they are watched

| Risk | How it shows | What happens |
| --- | --- | --- |
| A first decision binds a question a subject hasn't run | A record decides what `studies/subjects/subjects.tsv` gives a subject not yet run | The review refuses it; the question is kept open as a variation point (section 6) |
| A design rests on what the model doesn't hold | A record cites a capability with no data or events of its own, or only "by landing" | The design reads the evidence for it, and the record says so |
| One platform shapes the qualities | A measure or a band rests on one platform's statements | The record says so, and the measure stays an assumption |
| The cost grows unseen | A step's projection passes its budget | It is re-planned; past a quarter over, it comes to you (`PLAN.md`, section 8) |
| An option erodes before code exists | A record adds a field or a path that undoes a step | The review rule refuses it; the test comes with the first code |
| One market's need shapes a core decision | A record's reason comes from one market alone | The record says whether it comes out the same without that market |

## 6. The rules it carries

From `PLAN.md`, Stage 4A:
- **where the references' shapes differ,** each design weighs which is better, and states why, against the founder's quality order and regional fit, and tests the hypothesis in `reports/intent-review.md`, section 14;
- **until the founder gives scale numbers,** engineering assumes scale bands and states them, with the decisions each band touches;
- **an area's architecture that would bind a question a subject not yet run covers,** such as S-09's currency of records or S-03's contracting company, keeps that variation point open until the subject has run. The cheapest step that keeps a subject's variation point open may be taken before the subject runs, where it closes only what a ruling in force already rules out. It is listed for the founder's veto (31 October; section 4's worked example is one);
- **no production code** before requirements, an architecture description and engineering documentation exist to validate it against; spikes are allowed (`founder-decisions.tsv`, 24 October).

From `PLAN.md`, sections 6 and 1, binding every decision this plan governs:
- **the narrowing test:** a design that leaves out what the class establishes, or its room, needs your decision or a reason with evidence (`PLAN.md`, section 6);
- **the guard on the first market:** a need only one market shows is written without its name, and each record says whether it comes out the same without that market (`PLAN.md`, section 1).

## 7. What this plan decides, for your veto

Each is engineering's, listed in plain words. A veto reverses it as section 2 says.

### Every amount points to a currency entry, decided now
- **Decides:** every amount in the platform's money records (prices, stored amounts and reports) points to an entry in one table of currencies, instead of holding a bare currency code such as SAR. At launch the table has one entry per code. This is decided with the first decisions, before S-09 (the currency subject) runs; S-09 then decides which currencies and currency areas the table holds. It changes S-02's D9, which left this choice to S-09, and D9's move to S-09 (S02-M6).
- **Why:** now it costs one reference per amount and one table. If amounts held bare codes and a market later needed two currency areas under one code, every money record, rate and report would have to change: a redesign (S-02's D9).
- **Risks:** it settles part of S-09's question before S-09 has looked at it; if S-09 finds that a currency needs more than a table entry holds, the entry's shape changes. Each provider that takes only a code needs the entry mapped back to it. The need came from one market alone (S-02's D9). Without that market, the step would rest on other needs of the same form, such as a currency that changes its unit, which one ledger design read for D9 keeps as a new record. Whether they alone would justify it is a reading.
- **Instead:** keep D9 as ruled. The first decision on money records keeps "what identifies a currency" open, and S-09 decides it; until then, a review rule stops any record from storing a bare code. It costs a wait, and a placeholder in every money record's design until S-09 has run.

### Each part of the platform owns its records
- **Decides:** the platform is divided into parts, each owning its records and its own words for them. Another part reads or changes them only through the part that owns them (section 3).
- **Why:** a decision likely to change is then held in one place (Parnas 1972), and each word keeps one meaning inside its part (Evans 2003).
- **Risks:** a report or a search across parts needs a path to each part's records; a part cut wrongly means moving records between parts later.
- **Instead:** one shared set of records for every part, with the decisions likely to change hidden behind modules. It is simpler at first; a change to a shared record then reaches every part that uses it.

### Zid, BigCommerce and WooCommerce are graded as three of the five references
- **Decides:** the source types you chose name Zid, BigCommerce and WooCommerce as further references (REF): one more vote on commonality, read at declaration level (`studies/class-model/seed/km-source-types.tsv`). Here their sources are graded by type, as Shopify's and Salla's are: a Zid help page is DECL, WooCommerce's release is SHIP, an observed page is OBS. REF is kept for a platform beyond the five, such as Adobe Commerce, read only where a decision needs one more comparison (section 1).
- **Why:** the model counts the five alike: a capability's count is how many of the five place it in their core or as their own service (`PLAN.md`, Stage 4A, "The kind and the count"). A reading: grading three of them as one more vote, read at declaration level, would have designs weigh them below Shopify and Salla, against the count the model gives, and would set aside what is held for them beyond declarations, such as WooCommerce's shipped release (`evidence/product-class/woocommerce-11.2.1/`).
- **Risks:** it departs from the file you chose, for three of its examples. The three are held at less depth than Shopify and Salla: declarations for Zid and BigCommerce, code for WooCommerce (`PLAN.md`, section 7, risk 5). Graded by type, a declaration still carries its type's limit, but a design could give a thinly held platform the same weight as a deeply held one, unless it says what each citation can't tell.
- **Instead:** grade the three as the file says, REF: one more vote on commonality, read at declaration level. It keeps your chosen scale as written; designs then weigh the three below Shopify and Salla, and the model's count, which counts the five alike, and the designs' weighing no longer match.

## Sources

- Baldwin, C., Clark, K. (2000). *Design Rules, Vol. 1: The Power of Modularity.* MIT Press.
- Cervantes, H., Kazman, R. (2016). *Designing Software Architectures: A Practical Approach.* Addison-Wesley.
- Evans, E. (2003). *Domain-Driven Design.* Addison-Wesley. Bounded contexts: a part owns its model and its language. The context map: how parts relate.
- Ford, N., Parsons, R., Kua, P. (2017). *Building Evolutionary Architectures.* O'Reilly.
- ISO/IEC 25010:2023, Product quality model: the qualities pass's characteristics (`PLAN.md`, Stage 4A).
- ISO/IEC/IEEE 42010:2022, Architecture description. ISO/IEC/IEEE 42020:2019, Architecture processes. This plan follows 42020's processes, a reading of it: governance in section 2; management in the cost and the order, on the page; conceptualization in section 3; evaluation in section 5; elaboration in the description (section 2).
- Kazman, R., Klein, M., Clements, P. (2000). *ATAM: Method for Architecture Evaluation.* CMU/SEI-2000-TR-004.
- Nygard, M. (2011). Documenting architecture decisions.
- Parnas, D. (1972). On the criteria to be used in decomposing systems into modules. *CACM* 15(12).
- Pohl, K., Böckle, G., van der Linden, F. (2005). *Software Product Line Engineering.* Springer.
- Sullivan, K., Griswold, W., Cai, Y., Hallen, B. (2001). The structure and value of modularity in software design. *ESEC/FSE 2001.*
- Svahnberg, M., van Gurp, J., Bosch, J. (2005). A taxonomy of variability realization techniques. *Software: Practice and Experience* 35(8).
