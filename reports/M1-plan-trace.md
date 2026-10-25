# Where the plan of 24 October lives, and whether it was applied

**25 October 2026.** Part four of the assessment before Decision 1. It answers your three messages of today:
- where each item of the plan you approved on 24 October was preserved, and whether it was applied when due;
- why a plan you approved, trusting I would apply it, wasn't applied at its time;
- your note on F-06.

The plan is in `founder-messages/2026-10-24-approved-plan.md`. Each of its 50 items is traced in `decisions/checks/M1-plan-trace.tsv`, with when it applies, where it lives, whether it was applied, and a check anyone can re-run.

## In short

- **Of the 50 items:**
  - **31 were applied where due.** Five of them with a defect:
    - a wrong claim of absence: the engineering sources "cover payments only";
    - M2's feasibility report, kept only in my session's scratchpad;
    - a tool named for reuse and never used, with its rule;
    - a report over its length;
    - a merge rule held only in effect, not in words.
  - **11 are held where the work will read them when they fall due,** such as the Knowledge Map's architecture questions at each subject's framing.
  - **2 are held in effect only:** the rule each supports is in the method.
  - **2 were held but not applied when due:** the Knowledge Map's source types, and with them amendment 1d's typing of outside experience.
  - **4 were not held, in whole or part:**
    - Packwerk's sources for S-05;
    - Shopify Functions (E027) for S-06;
    - the commonality rule for M2's capability map;
    - the route's size.
- **All of these are now placed or applied** (section 1). Nothing the plan asks to be done lives only in its copy now. Two of its observations are carried by the rules they support.
- **Why:** I carried the plan into the method at M0 by summary, not by trace. Ids and instructions became general words. Rules went in as sentences, with no field, script or step to make them happen. And the method's resume path doesn't read the plan's copy, so what wasn't carried was lost to any restart.
- **The correction:** amendment 4c, widened. A plan you approve is traced into the places the work reads before its work starts. Each amendment lists what it changes, and each milestone report lists what changed in the method and the backlog.
- **The obligation model never read Shopify's engineering sources,** and no record applied the source types. Both are fixed for the records, and M2 is set to use them before its scenarios judge D-002 and D-003.
- **F-06 is no longer taken as a given** by D-001 or D-002. The separation of payments rests on both references' own words.

## 1. What the trace found, and what is done now

| Item | What happened | Now |
| --- | --- | --- |
| **The source types** (plan :95; `METHOD.md` section 5), "the rule for buying architectural intelligence" | Held in `register/README.md` and named in the method, but no record, template field or script named a source's type. D-002 and D-003 cited Shopify's developer docs (E030 to E036) and Active Merchant (E040) untyped | The template's Evidence section gives each outside source's type. `method/decision_status.py` flags one without, and D-002 and D-003 are typed: DECL, OSS |
| **Packwerk and the modular monolith** (E016, E018 to E022) | Named as held and unused. The method kept only "engineering writing such as Shopify's own talks and posts", which wouldn't have led S-05 to them | In S-05's backlog row, which its framing reads |
| **Shopify Functions** (E027) | Not held anywhere | In S-06's row, with E036 and E030 to E032 |
| **Pods** (E024) | Held in S-03's row as "Shopify's on pods" | Its id added |
| **The commonality rule for the capability map** (KM-MTH-01) | Section 14 kept "the capability map" without "using the commonality rule". The selection script would list the question, not the instruction to build the map with it | In S-02's row |
| **M2's feasibility test** | Done on 24 October (8.2 million tokens). Its report was only in my session's scratchpad, which doesn't outlast the session | In `studies/subjects/S-02/`, with its brief and scripts |
| **The route's size,** about 0.3 billion agent tokens to M8, give or take half | Not held. Per-subject budgets and stop rules are held and applied | In `STATE.md`, beside the spend so far |
| **"Cover payments only"** (plan :74; `METHOD.md` section 13; R-04) | A claim of absence made without a search. The sources were gathered for the payment seam, and also cover pods, Packwerk and sharding (E015, E023) | R-04 corrected. Section 13's words are corrected under 4c |
| **`method/source_kinds.py`,** named for reuse | Never used since M0. Its rule, "Kinds are compared like with like" (`PLAN.md`:311), didn't reach the method | 4c brings the rule back at step 3 |

**The rest:**
- **The guard, your restored decisions, the backlog, the risks, the architecture description, the reports, and M0's repairs** are applied.
- **The Knowledge Map's architecture questions** are held in the backlog. `method/km_select.py` lists each one at its subject's framing: STF-07, ACC-01 and ACC-05 at S-03; APP-06 and API-02 at S-06; ENG-02 and the commonality question at S-02.
- **The definition of ready, spikes and investigations** are in the method, and none has fallen due.

## 2. Why the plan wasn't applied at its time

**The root cause is a missing safeguard, which made the execution failures possible:** nothing traced an approved plan into the places the work reads at each step.
- **At M0 I wrote amendment 1 from the plan, and checked it by eye.**
  - Where an item named ids or an instruction, the method kept a general phrase, and the pointer was lost. Packwerk's ids, E027, and "using the commonality rule" went this way.
  - Where an item was a rule, the method kept the sentence, but nothing at its step made it happen. The source types went this way. The absence audit had gone the same way at the same change (part one).
- **The method's resume path is the method, `STATE.md`, the backlog, the risks and the records (section 9).** The plan's copy isn't among them, and shouldn't need to be. So an item the method didn't carry survives only in my working memory, and a restart loses it.
- **Changes were checked for what they add, not for what they drop.** Part two found the same at each change of `PLAN.md`. Amendments 2 and 3 changed one practice of this plan, saving your messages, and that by your own decision. The losses happened when the plan became the method.

**Your expectation isn't mistaken.** A plan approved is a plan to be carried out, item by item, at its time. A practice the plan names is used at its step, or isn't named.

**The practice behind the correction:**
- **Traceability,** which the method already cites (ISO/IEC/IEEE 29148): each approved item is traced forward to where it is satisfied, and checked there.
- **Management of change** (OSHA 29 CFR 1910.119(l), part two): before a change, what it does to existing safeguards is reviewed.

**The correction is 4c, widened** (`reports/M1-method-assessment.md`, amendment 4):
- **A plan you approve is traced before its work starts.** Each item is placed in the method, in the backlog row of the subject it applies to, or in `STATE.md`, with the check that will show it was applied. An item that can't be placed is named to you.
- **Each amendment lists what it retires or changes,** with the risk each controlled, reassigned or accepted. You see that list with the amendment.
- **Each milestone report lists what changed in the method and the backlog** since the last report, from their diff, by function.
- **Section 13 takes three corrections:**
  - the engineering sources' coverage;
  - F-06 and the decisions of 10 October;
  - kinds of source compared like with like.

This adds no new artifact. The trace is a check sheet, made once per approved plan, and its items land in files the work already reads.

## 3. The model, the engineering sources and the source types

**Facts:**
- **The model's own page** says it was "read from Shopify's help center, developer docs and shipped schemas", dated 9 October (`model/obligation-to-payout.html`).
- **It was committed at 04:11 UTC on 10 October** (`caad5aa`). The engineering sources were captured from 08:30 UTC (run `20261010T083026Z`; commit `983e305`), and the model cites none of them.
- **The seam read them all** (`8946887:studies/payment-seam/notes/shopify-engineering.md`, E001 to E040).

**By the source types** (`register/README.md`):
- the model read platform declarations (DECL) and shipped artefacts (SHIP);
- a declaration can't tell "whether it behaves that way, or why it exists";
- engineering writing (LIT) is good for "patterns, trade-offs, how mature teams built similar systems", and is one company's account;
- open-source code (OSS) is good for how the same behaviour is built.

So the model's eight lines are readings of what Shopify declares and ships, not of how or why it was built. *(Interpretation.)*

**Done, before M2's scenarios judge D-002 and D-003:**
- **The candidates walked beside D-002** at M2 include any design the held engineering writing shows for the same line, weighed as one company's account (D-002, Confirmation).
- **A model line a record uses is first set beside what the engineering writing and code say of the same concern,** each weighed by its type (part three).
- **The held engineering sources come before any new ones:**
  - for the scenarios, those on peak load and resilience (E001 to E008, in S-02's row);
  - for tenancy, pods (S-03);
  - for modules, Packwerk (S-05);
  - for apps, Functions (S-06).
- **The agent that writes M2's scenarios** has a brief naming neither D-002, D-003 nor the seam.

## 4. F-06

As framed (`founder-decisions.tsv`, 25 October): F-06 and the other decisions of 10 October came from the early studies. Whether payments are a separate concern is an engineering decision drawn from the references' evidence, not a founder premise.

**Done:**
- **D-002 no longer takes F-06 as given.** As a given, it had pre-empted D-002's own option 2, the order side calling each provider directly. *(Interpretation.)*
- **D-001 never took it as given.** I had added it earlier today, after the check suggested it, and removed it on your note.
- **The glossary's *payments side* now rests on both references' own words:**
  - on Shopify, "All Shopify-supported payment methods rely on third-party providers to process your transactions." (`HC:payments/getting-paid.md:3`), and each transaction names its gateway (`GQL:2447`);
  - on Salla, its own Electronic Payments sits beside outside gateways (`SA-en:24`, `SA-en:807`), and each transaction names its provider (`SAPI:208`).

  Your expectation holds on this evidence: the product class keeps payment providers apart from orders.
- **The line on F-06's restored row** naming the seam's contract as the first subject's starting draft was my annotation, not your decision. Part three says so.

## 5. What you're asked

**Amendment 4,** with 4c widened and 4e revised: approve / approve with changes / not now.

**Decision 1:** nothing here changes its line or its three choices.

**Cost of this round:**
- the independent check of part three: 3.0 million tokens (22 requests, `method/count_tokens.py`);
- S-01 in all: 64.9 million.
- This part had no check of its own. Every row of the trace names a check anyone can re-run.
