# The first market, bound once

**25 October 2026.** Part five of the assessment before Decision 1. It answers your three questions of this evening:
- is the glossary right, now and in its form?
- your test: if Yemen had never been brought in, what would Decision 1 be?
- does "a market is one member, bound once" hold everywhere, and why is the first market still spread through the work?

## In short

- **Your test held.** An agent that never saw Yemen, D-001 or the glossary made Decision 1 from Shopify's and Salla's evidence and your guard alone.
  - It reached D-001's line: sellers' own provider accounts and offline methods in every market; A and B a switch per market, off at launch, built only on your decision.
  - It reached choices 2 and 3 as consequences.
  - It differs on choice 1: it read your guard literally, so an account created through a Sharrwah sign-up flow is B. That is the reading D-001 already puts to you.

  So Yemen shaped D-001's wording, not its decision.
- **Applied:**
  - D-001's reasons now come from the references;
  - Yemen is one row and its bounded decision, D-006;
  - D-001 and D-002 name no Yemen place, regulator, currency or id.

- **The glossary names no first-market place, regulator, currency or provider** (0 of 275 lines).
  - 11 of its 35 entries carried a decision's outcome inside a definition. That is how the first market reached the vocabulary: through D-001's outcome, not by name.
  - Those outcomes are now in their records, and no meaning changed.
- **Yes, it holds everywhere.** Yemen was bounded early, at G1: its rules "land as availability, not as design". Yet the first market is still spread through the work, by four paths the guard's check doesn't see:
  - the method itself;
  - the first subject's question set;
  - the earlier work kept as candidates;
  - the scenarios.
- **The root cause is in the method, and is mine.** Section 3a says options come from the references and "the first market's facts then test them". But section 5's evidence step, which comes before any option is proposed, takes "the first market's facts from the Stage 1 digest". So the first market enters every decision before it can test one. The guard's script looks for market names in two sections of a record, so it can't see this.
- **The correction is amendment 4f.** For each decision a market binds, the market is a row and a bounded decision, in one Configured record. D-006 is the first. The evidence step drops the first market, and each market's rows are walked through the decisions at close. Earlier work built for one market feeds its rows, never a subject's design.

## 1. The glossary

- **Names:** it names no first-market place, regulator, currency or provider. Each term is defined from Shopify's and Salla's own words. Its only market names are Salla's own markets, Saudi Arabia and the UAE, as facts about Salla.
- **Outcomes:** 11 of its 35 entries carried a decision's outcome inside a definition, such as "Under C each provider does both on its own terms, and Sharrwah sends no payouts".
  - The method puts every record that uses a term under review when the term's meaning changes (section 10). So any later switch, such as B in one market, would have rippled through the vocabulary.
  - Those outcomes are now in their records, and each entry names the record. No term's meaning or extent changed, and the quotes still match their sources (`method/inventory_quotes.py`).
- **The practice:** the commonality analysis of product-line engineering keeps four things apart:
  - a "Dictionary of Terms": "a standard set of key technical terms used in discussions about and descriptions of the domain";
  - the "Commonalities": "assumptions that are true for all family members";
  - the "Variabilities";
  - the "Parameters of Variation", "the value range and binding time for each variability" (Coplien, Hoffman and Weiss, *IEEE Software*, 1998, p. 43).

  The glossary is the dictionary. "Who holds sellers' money" is a variability. A market is one member: its row binds the values.

## 2. Your test: Decision 1 without the first market

**How it ran.** One agent was given:
- the question;
- your guard;
- the two evidence repositories.

Its brief named no market and barred it from this repository's records, glossary, studies and reports. It cost 3.3 million tokens. Its record is `decisions/checks/M1-blind-decision-1.md`, and each quote it relies on was found word for word by script.

**What it decided, beside D-001:**

| | The test, without the first market | D-001 |
| --- | --- | --- |
| Built for every market | The seller's own provider accounts, and offline methods marked paid by the seller | C: the seller's own provider, the seller's own courier, or the seller |
| A and B | "Per market, a switch each for O3 and O4, off; only a recorded founder's decision turns one on. Nothing behind them is built now." | "A and B are reserved, not built. Switching either on stays yours." |
| At launch | "O1 and O2 in every market; O3 and O4 off everywhere." | C at launch, in every market |
| Fees | "it bills sellers separately, as Shopify does" | Choice 2: billed apart at launch |
| A balance | "Sharrwah holds no balance, payout or reserve" | Choice 3: no balance sellers pay into |
| Where B ends | Your guard's words: an account created through a Sharrwah sign-up flow is B | Choice 1, both readings put to you, recommending its source's |

**What the references show,** which D-001 now uses as its reasons:
- **Shopify:** "Shopify Payments is only available to online stores in" "certain countries and regions" (`HC:payments/shopify-payments.md:9`), with Stripe as "Shopify Payments' banking partner" (`HC:payments/third-party-providers/payment-gateway-availability.md:17`).
- **Salla:** activates its own payments per country after verifying the store: "How to Activate Salla payments in Kuwait" (`SA-en:1046`); "Activate Salla payments in the UAE" (`SA-en:1080`); "You can only start using electronic payment gateways after your store verification is complete" (`SA-en:447`).
- **In both,** sellers' own provider accounts and offline payment work wherever a provider serves the seller.

So the product class itself treats a platform's own money-holding service as a switch per market. The common part is C.

**The market row it wrote,** in general terms, is the template for every market's row:
- the seller's own provider: "a provider integrated with Sharrwah states that it serves sellers established there and settles to them directly";
- offline: "each listed offline method may be accepted there";
- B: "a payment company permitted there to hold sellers' funds in accounts opened through a platform has accepted Sharrwah";
- A: "Sharrwah holds any authorisation required there to hold others' funds".

D-006 fills it for Yemen.

## 3. Where the first market is, and how it got there

**Measured, in the live files, before today's corrections** (lines naming the first market, its places, its currency, its zones or Stage 1's ids):

| File | Lines | Its role there |
| --- | --- | --- |
| `architecture/` (all five sections, the glossary included) | 0 | — |
| D-004 | 0 | — |
| D-002 and D-003 | 3 and 2 | D-002: a given and its guard section quoted the rial's two editions (now neutral, 0). D-003: the change scenario "the first market dropped" |
| D-001 | 31 of 256 | Mostly evidence and tests, but three of the four reasons on your page. Now 8, all pointers to D-006 or tests |
| `METHOD.md` | 19 of 484 | The guard and its history, and three paths in: section 5's evidence step (:173), section 1's end walkthrough (:12), and section 8's example scenario (:255) |
| `register/pay-questions.tsv`, S-01's question set | 42 of 81 rows | 34 of the 39 rows drawn from the Yemen setup options, and 8 of the 42 from the Shopify study, filed as questions of the money boundary itself |
| `yemen-setup-options/`, `model/` | 1,102 and 42 lines | Kept as candidates. Part three filed the setup options as candidate options for S-07, a subject for every market |
| `studies/proposals/drafts/` | 261 lines | Mostly confined to section 6. The Q7 draft's two rials leaked into design (R-05) |

**The paths, each verified:**
1. **The method's evidence step.**
   - Section 3a (:87): "Options are drafted from the references, and the first market's facts then test them."
   - Section 5, step 2 (:173): "Shopify and Salla first, then the first market's facts from the Stage 1 digest".

   Step 2 comes before step 3, where options are proposed. So the first market is already evidence when options are drafted. Amendment 1 removed the words "Yemen's conditions are drivers for every decision they touch", but left this step in place. My trace of the plan marked the guard "applied" and missed this. It is corrected (`decisions/checks/M1-plan-trace.tsv`, P-04).
2. **The question set.** Half of the money boundary's questions are the first market's, such as "Which authority zone does Sharrwah serve at launch: the Aden zone, the Sana'a zone, or both as separate ecosystems?" (PAY-43). Answering them in a subject for every market puts the first market into that subject's design.
3. **The candidates.** The setup options were built around the first market, and the obligation model's launch stages are Yemen's ("Zone chosen (PAY-43)"; a "Zone-aware money and rate service"). As candidates for a subject, they bring that market in as design.
4. **The scenarios.**
   - The method's end walkthrough "covers the first market's flows" (:12).
   - Its one example is "A buyer in Aden orders and pays cash on delivery" (:255).
   - M1's walkthrough began there.

   The yardstick for every decision was one market's flows.

**Why the guard didn't catch it.** Its script (`method/decision_status.py --guard`) flags a market's name in two sections of a Built record, Decision outcome and Consequences, and in the drafts' design sections. Each of the four paths runs elsewhere: through the evidence step, the reasons, the question sets, the candidates and the scenarios. The risk is registered (W-07), and its mitigation guards the outcome text, not the paths into it.

## 4. The correction

**Amendment 4f, a market is bound once** (in `reports/M1-method-assessment.md`, beside 4a to 4e):
- **A market is a row and a bounded decision, nothing more.** For each decision a market binds, one record, outcome Configured, varying by that market, holds:
  - its row: the condition each option needs there, and what holds there, each fact by its id and date;
  - what the row binds.

  D-006 is the first. Other records name the market only to point there, in their Confirmation.
- **Section 5's evidence step drops the first market.** At close, each market's row is walked through the subject's decisions:
  - what the decisions carry needs nothing more;
  - a value is bounded in that market's row;
  - what the design can't carry comes to you.
- **The end walkthrough and the method's example** speak of each launch market's row.
- **Earlier work built for one market feeds that market's rows.** That covers the setup options, the model's Yemen rows and stages, and the 42 payment rows. Part three's and part one's dispositions are revised to say so.
- **The guard's check widens to the paths:** a market's name or ids appear in a Built record only in its Confirmation, never in the glossary, and otherwise only in that market's rows.

It adds no artifact type: a market's row is a decision record. It replaces the first market's facts, restated across the method, the records and the question sets, with its rows.

## 5. Purge, or confine?

Your instinct is right on the risk, and the evidence shows where it bites. A blanket purge would go too far:
- it would erase the facts Yemen's rows need when it is bound, and the record of what you decided;
- in practice that is W-10, over-correction that drops real constraints.

What the practice calls for is binding time: the first market enters only at its binding, after the shared decisions, and only in its own rows.

| What | Where | What happens to it |
| --- | --- | --- |
| The market's evidence | `evidence/`'s Yemen captures, `studies/yemen-cases/`, the Stage 1 digest | Kept, frozen: the facts its rows cite |
| Your decisions about it | `founder-decisions.tsv`: F-00, F-02, F-03, G1's B1, B2 and B7 | Kept: the record of what you decided |
| Its rows | D-006, and one for each later decision it binds | Where it lives |
| Tests | the change scenario "the first market dropped", and each subject's market test | Kept, pointing to its rows |
| What shapes design | the method's evidence step, end walkthrough and example; records' reasons; the glossary; the shared question sets; work built for it, kept as candidates | Neutral terms, or moved to its rows |
| History | reports, check sheets, `PLAN.md`, the earlier studies | Left as the record. Their dispositions say what each is now |

**Done now** (engineering's, and reversible):
- the glossary is a dictionary of terms (0 first-market lines);
- D-001's reasons come from the references, and its first-market lines fell from 31 to 8, all pointers or tests;
- D-006 holds the first market's row for Decision 1;
- D-002 names no market;
- the setup options and the model's Yemen parts are re-filed as inputs to the first market's rows;
- the plan's trace is corrected (P-04).

**Waits for your answer on 4f,** since it changes the method:
- the evidence step, the end walkthrough and the example;
- the widened check;
- moving the 42 payment rows that name the first market, D-005's one driver line, and the drafts' Yemen sections into its rows.

**Is the work at risk of collapse?** Not on this evidence:
- the shared decision held without the first market;
- the architecture description, the glossary and D-002 to D-004 carry none of it.

What was exposed were the paths. Until 4f, two remain open:
- the method's evidence step, which would pull the first market into S-02's and every later subject's evidence;
- the payment rows, which would bring it into S-07's.

Both are named, and 4f closes them.

## Sources

- Coplien, J., Hoffman, D., Weiss, D. (1998). Commonality and Variability in Software Engineering. *IEEE Software* 15(6), pp. 37–45.
- W3C, "Localization vs. Internationalization": internationalization is "the design and development of a product, application or document content that enables easy localization for target audiences that vary in culture, region, or language", including "Separating localizable elements from source code or content".
- Shopify's own `Market`: "A merchant-defined group of buyers identified by conditions" (`GQL:1951`), with its conditions, currency settings and delivery as fields.
