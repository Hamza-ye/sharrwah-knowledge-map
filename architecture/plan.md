# The architecture plan

**Status: a draft by the coordinating session, 30 October 2026.** It comes to the founder at GM, with the class's model's extent and the Knowledge Map's page rebuilt from it. Architecture starts on the founder's go on this plan (`PLAN.md`, Stage 4A; `founder-decisions.tsv`, 30 October). Section 1 is drafted with the dry run of the model, so that the model records what architecture needs before its other domains run. The rest is finished before GM, and reviewed by an agent that made none of it.

## For the founder, on one page

**What this is.** How the architecture will be worked out once the class's model has its extent:
- what it needs to know, and from where;
- who decides, and how each decision is made, recorded and checked;
- what comes first;
- what "keeping room" means;
- how the whole is evaluated.

It decides no part of the architecture itself.

**What you decide:** your go on this plan, at GM. Nothing else in it is yours, except where an architecture decision touches your list: markets, plans and prices, agreements and partners, the company and its licences, spending, and whether Sharrwah's own company runs a service. Such a decision comes to you with its evidence, its options and a recommendation. Every other decision is engineering's, and each is listed for your veto at the next report.

**What happens on your go:**
1. The decisions that cut across every area are made first (section 3).
2. Then the areas, in the order section 3 sets, beside the subjects still to run.
3. The whole is evaluated at milestones, against scenarios drawn from your quality order (section 5).

**What you'll see:** at each milestone, a short report of the decisions made (for veto), the options kept open with their cost, the evaluation's findings, and the cost.

## 1. What architecture needs to know, and where each part comes from

Each source is graded by the Knowledge Map's source types, with what each can't tell (`studies/class-model/seed/km-source-types.tsv`; the founder, 30 October). The grade goes with the source, not the platform: a Zid help page is a platform's declaration, and WooCommerce's release is shipped code. The types are reconciled with the plan's kinds of evidence (`PLAN.md`, section 6):
- *observed* is OBS;
- *shipped* is SHIP;
- *stated* and *official page* are DECL, for the platform's own docs, terms and plan tables.

| What architecture needs | Where it comes from | Source types | What that can't tell |
| --- | --- | --- | --- |
| What the class establishes: each capability, where each platform puts it, how many establish it, its kind | The class's model (`studies/class-model/`) | DECL, SHIP, OBS, as each cited statement's kind | What a platform doesn't publish; why it chose so; behaviour on stores never observed |
| The class's data and events: the objects, webhook topics and access scopes each capability shows | The model's evidence: the `boundary` statements of each capability's concerns, derived per capability at the merge | SHIP, DECL | What the server does with them; a platform's internal model |
| What varies, by market, store and plan | The subjects' registers (S-01, S-02, and each later one); the model's `decides` statements and scopes | DECL, OBS | A market not yet studied |
| What fills a slot in a market: providers, partners, law | The model's slot fillers; each subject's evidence; providers' and regulators' own documents | PROV, LAW | The platform's own design |
| The qualities the class states: limits, certifications, uptime, where data lives | The model's qualities | DECL | Real performance; Sharrwah's own numbers |
| What Sharrwah has decided, and the quality order | `founder-decisions.tsv` | DEC | Nothing about the world: a decision is not evidence |
| Scale | The founder, later. Until then, engineering's stated bands | DEC; an assumption, marked as one | What load will really come |
| How comparable systems are built | Open-source commerce systems, standards, engineering writing, read for each decision that needs them | OSS, STD, LIT | What merchants of this class get; facts about the five |
| How one of the five built itself | Shopify's own engineering talks, posts and repositories, held in `evidence/shopify-engineering/` (E001 to E040, captured 10 October 2026): payments beside the rest of the platform, pods, Packwerk, Functions, payment apps and the provider contract | LIT, OSS | Whether the design still stands: the detailed write-ups of its internal payment architecture date from 2019 to 2022. Why another of the five built otherwise. What it costs to run |
| Whether a design works on Sharrwah's stack, at what cost | Spikes | EXP | The reference products |

**Left out:**
- **Practitioners (PRAC):** merchants are never asked (`founder-decisions.tsv`, 24 October), and the agencies and former platform engineers it also names could be reached only by the founder;
- **capture indexes (IDX):** a finding aid, never evidence;
- **"further reference platform" (REF):** means a platform beyond the five, such as Adobe Commerce. It is read only where a decision needs one more comparison.

**What the model must record for this.** Its brief records the capabilities, cells, qualities and slot fillers. Each capability's data, events and deciding statements are derived by the merge in two grades (the dry run's review, S15; `studies/class-model/review-dry-run-rulings.md`, convention 10):
- **exact:** the `boundary` and `decides` statements its cells cite;
- **by landing:** the other statements of the concerns landed in it. This attribution is coarse: a coarse concern's statements go to its landing capability, though some belong to its children.

Each area's design refines the coarse grade as it reads its capabilities in depth. No part writes more, so the extent's cost doesn't grow for it, and what is coarse is said plainly.

## 2. Who decides, and how each decision is made, recorded and checked

- **Who decides:** engineering, by the founder's intent. A decision that touches the founder's list goes to the founder. Every other decision is listed for the founder's veto.
- **How a decision is made:** by its drivers, as attribute-driven design does it (Cervantes & Kazman 2016):
  - the capabilities it serves, from the model;
  - the quality scenarios it must meet (section 5);
  - its constraints: the founder's decisions, the subjects' rulings, and the law where a market's law binds.

  The options come from the references first. Where their shapes differ, the decision weighs which is better and says why (`PLAN.md`, Stage 4A). Then come established designs and standards.
- **How it is recorded:** one record per decision, in `architecture/records/`, in the form of an architecture decision record (Nygard 2011), with:
  - its context and drivers;
  - the options and the evidence for each;
  - the decision and why;
  - what it keeps open, what it closes, and what would reopen it.

  The architecture description gathers the records into views of the whole (ISO/IEC/IEEE 42010:2022).
- **How it is checked:**
  - an agent that made none of it reviews each record against its evidence before anything builds on it;
  - every option kept open has its check (section 4);
  - the whole is evaluated at milestones (section 5).

## 3. What comes first

**The model's areas aren't architecture's parts.** The 41 areas index what the class does. Architecture's parts are cut by what changes together and by what data they own: each decision likely to change sits behind its own module (Parnas 1972), and each part owns its model and its language (Evans 2003, bounded contexts).
- So once the model has its extent, its capabilities are grouped into candidate parts, by the data and events they share and the decisions that would change them.
- Each part records which capabilities and areas it holds.

**The decisions that cut across every area come first,** as attribute-driven design's first iteration settles the overall structure for a new system:
1. how stores are kept apart, and where their data lives;
2. identity and permissions: staff, customers, apps and partners;
3. money records and currency: how every amount names its currency (section 4's worked example);
4. markets and the seller's country: S-02's two entry points (E1, E2) and the business record (D1);
5. events and extension points: how apps and providers plug into the class's slots;
6. configuration: how a setting is held for a store, varied per market and limited per plan (S-02's D6; plans and prices are the founder's).

**Then the areas,** in the order of their dependencies: those whose data the others refer to come first. An area waits for the subjects that cover its open questions. The order is set when the model's parts are known, with:
- the payments area after S-04, payment methods and providers;
- tax after S-05;
- where data lives after S-08;
- delivery after S-10;
- what Sharrwah charges after S-11.

S-03's contracting company and S-09's currency of records bind every area that holds a contract or an amount. So they are settled with the cross-cutting decisions, or kept open there as variation points until the subject has run (`PLAN.md`, Stage 4A).

## 4. What keeping room means

The founder took line (3) out of the intent on 30 October: read literally, "no commitment closes it" is something no design delivers, and "not designing it before its time" can be read as designing nothing now, which is how options are closed by a default nobody examined. So keeping room is defined here by established practice, the options a modular design keeps open at a stated cost (Baldwin & Clark 2000; Sullivan et al. 2001), the variation points that name their binding time (Pohl, Böckle & van der Linden 2005; Svahnberg, van Gurp & Bosch 2005), and the checks that stop an architecture's properties eroding (Ford, Parsons & Kua 2017).

**An option is kept when:**
1. it is named, with the trigger that would exercise it;
2. the commitments that would close it are named;
3. the design takes the cheapest step that keeps it reachable, and no more: an indirection, a declared variation point with its binding time, or an interface that hides the decision;
4. what it costs to hold, and what it would cost to exercise later, are both stated;
5. a check stops a later commitment from closing it unexamined: a test that fails when the step is undone (a fitness function), or a review rule.

This guards both failures: an option closed by a default nobody examined, and one built before it is worth its cost.

**The worked example: S-02's D9, two currency areas under one currency code.**
- **The option:** a currency that names a currency area within its code, so that prices, stored amounts and reports tell the two areas apart by currency, not only by market.
- **Its trigger:** a market where two currency areas share one code, with different notes and rates, and must be told apart in money records.
- **What would close it:** storing a bare currency code in every amount. Every money record, rate and report would then have to learn the area: a redesign.
- **The cheapest step:** every amount refers to a currency record, one per code at launch. Naming an area later is a new record, mapped to the bare code where a provider takes only the code.
- **The cost to hold:** one reference per amount, and one table of currencies.
- **The cost to exercise:** a new record, and its mapping at each provider: one module.
- **Its check:** a test that fails if any money record stores a bare code, and a review rule for every new money field.
- **The gap it shows:** D9 left the currency record to S-09. The step is cheap now and a redesign later, so it is taken with the cross-cutting decisions (section 3, item 3) rather than waiting for S-09, which then decides which currencies and areas fill it.

## 5. How the whole is evaluated

- **Quality scenarios.** The founder's order (trustworthiness; then coherence and user experience; then performance; then completeness, read as what each release delivers) is a ranking. Architecture needs measurable scenarios. Each quality gets scenarios with a stimulus, a response and a measure, in a utility tree ranked by that order (Kazman, Klein & Clements 2000).
- **Scale bands.** Until the founder gives numbers, engineering states its bands (stores, orders a day, catalogue size, markets per store), each an assumption, marked, with the decisions it touches.
- **Evaluation at milestones.** After the cross-cutting decisions, and after each group of areas, the architecture as a whole is walked through the scenarios:
  - its risks, sensitivity points and trade-offs are recorded;
  - the plan's change scenarios are walked too: a second market, the company based elsewhere, the first market dropped (`PLAN.md`, section 6, step 7).

## 6. The rules it carries

From `PLAN.md`, Stage 4A:
- **where the references' shapes differ,** each design weighs which is better, and states why, against the founder's quality order and regional fit, and tests the hypothesis in `reports/intent-review.md`, section 14;
- **until the founder gives scale numbers,** engineering assumes scale bands and states them, with the decisions each band touches;
- **an area's architecture that would bind a question a subject not yet run covers** keeps that variation point open until the subject has run;
- **no production code** before requirements, an architecture description and engineering documentation exist to validate it against; spikes are allowed (`founder-decisions.tsv`, 24 October).

## Sources

- Baldwin, C., Clark, K. (2000). *Design Rules, Vol. 1: The Power of Modularity.* MIT Press.
- Cervantes, H., Kazman, R. (2016). *Designing Software Architectures: A Practical Approach.* Addison-Wesley.
- Evans, E. (2003). *Domain-Driven Design.* Addison-Wesley. Bounded contexts: a part owns its model and its language.
- Ford, N., Parsons, R., Kua, P. (2017). *Building Evolutionary Architectures.* O'Reilly.
- ISO/IEC/IEEE 42010:2022, Architecture description. ISO/IEC/IEEE 42020:2019, Architecture processes.
- Kazman, R., Klein, M., Clements, P. (2000). *ATAM: Method for Architecture Evaluation.* CMU/SEI-2000-TR-004.
- Nygard, M. (2011). Documenting architecture decisions.
- Parnas, D. (1972). On the criteria to be used in decomposing systems into modules. *CACM* 15(12).
- Pohl, K., Böckle, G., van der Linden, F. (2005). *Software Product Line Engineering.* Springer.
- Sullivan, K., Griswold, W., Cai, Y., Hallen, B. (2001). The structure and value of modularity in software design. *ESEC/FSE 2001.*
- Svahnberg, M., van Gurp, J., Bosch, J. (2005). A taxonomy of variability realization techniques. *Software: Practice and Experience* 35(8).
