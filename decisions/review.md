# Review of the founder's earlier decisions

*1 November 2026. Each decision marked "To review" in `founder-decisions.tsv`, checked by product line engineering against the decision of 1 November (line 35). Reviewed by an engineering agent that made none of them.*

**How to read it.** "Line N" is the row's line in `founder-decisions.tsv`. "First decision N" is in `decisions/first-decisions.md`. "decision-1.md" and S-01's register are in `studies/subjects/S-01/`; S-02's `decisions.md` and register are in `studies/subjects/S-02/`. Every verdict is a reading: engineering's judgement, for your veto. Other judgements are marked *Reading*.

## For the founder

**What this page does.** For each of the 33 rows marked "To review" (lines 2 to 34) it asks: what does it decide; does it belong to the platform, to a market's setup, to how the work is done, or to your own list of business decisions; when does it bind; and does it still hold under your decision of 1 November. It does the same for what Decision 1 and S-02 decided beneath those rows.

**Four terms.**
- **The platform:** what is built once, for every market.
- **A place that varies:** a slot in the platform built to take a different value in each market (engineers call it a variation point).
- **A market's setup:** filling those slots with one market's providers, law and limits, when you decide to set that market up.
- **A first decision:** one of the fifteen concerns every part of the platform depends on, read from Shopify's shape.

**The count, for the 33 rows.**

| Verdict | Rows | Lines |
|---|---|---|
| Stays as it is | 8 | 4, 9, 10, 11, 14, 20, 28, 34 |
| Stays, with new words | 12 | 7, 8, 12, 13, 17, 19, 23, 24, 25, 26, 32, 33 |
| Split: the platform's part stays, the market's part waits for its setup | 2 | 16, 30 |
| Retired | 11 | 2, 3, 5, 6, 15, 18, 21, 22, 27, 29, 31 |

Most new words only drop a pointer to a part of the plan that no longer exists, or put Shopify's model where "the class" of several platforms stood. The retired rows governed ways of working the plan of 1 November replaced: the Yemen row, the subjects, the class's model, the GM milestone.

Beneath the rows: of S-02's nine rulings, seven stay with new words (Shopify's shape alone, without the other four platforms) and two split (D8 and D9). Of Decision 1's follow-ons, E2 and defaults 1 and 3 stay; E1 and default 2 take new words.

**The ten rows built on Decision 1's frictions, in plain words.**
- **Your Decision 1 stands.** At launch, in every market, Sharrwah holds no seller's money: each seller is paid through its own providers, and Sharrwah bills its own fees apart. That is your business choice, and it names no market (lines 16, 17, 20).
- **What changes is where its parts sit.** The platform builds one slot, "who holds sellers' money", set for the business that takes the payment, and an order's payment record that is the same whatever the answer, as Shopify keeps its own payments account apart from an order's payments. Yemen's couriers, wallets and transfers are not built in: they are filled in when Yemen is set up (lines 16, 19).
- **Checking every decision against Yemen stops** (the "Yemen row", line 15). A market's facts are read at its setup. Two rows that rested on that check are retired with it (lines 21, 22).
- **Two of S-02's rulings came from Yemen alone** (D8 and D9, carried by line 30). D8's room for areas within a country waits for the market that needs it: its own analysis says waiting costs one module. D9 asks how every amount names its currency; that is decided once, at the first decision on money, with its cost stated, and Yemen's two currency areas wait for Yemen's setup.
- **Your guard stays** (line 8). It limits what goes live in a market. It no longer leaves open whether the platform keeps room for A and B: your decision of 29 October settled that.
- **Your markets stay** (line 25), without the exception that let Yemen's present circumstances become permanent given "a genuine, justified reason". Under 1 November, a market's limits never define the platform.

**What needs your decision.** Each is yours; each gives engineering's recommendation.
1. **The new words** for the 12 reworded rows and for the parts of the 2 split rows. Only words you approve go in `founder-decisions.tsv`. Recommended: approve them as written below.
2. **Line 8:** drop its last sentence ("Whether the design provides for either arrangement is for the work to recommend ... and for the founder to decide"). Recommended: drop it.
3. **Line 25:** drop the exception "without a genuine, justified reason". Recommended: drop it.
4. **Line 26:** read "the class" as Shopify's model throughout. Recommended: yes.
5. **Line 29:** you reserved a go before architecture starts. Recommended: your go on the first decisions' records (`PLAN.md`, the steps, 3) is that go.
6. **Line 23 (spending):** keep "a budget must never cost evidence", now about Shopify's evidence, for every step. Recommended: yes.
7. **A veto, if you want one:** on the 11 retirements, and on D9's question going to the first decision on money (engineering's call).

Nothing here reopens Decision 1, the guard, or which markets Sharrwah serves.

---

## Part 1: the ten rows built on Decision 1's frictions

### Line 8 · The guard on sellers' money (18 October)
- **What it decides:** no arrangement that holds sellers' money through Sharrwah goes live anywhere without your decision: Sharrwah holding it (option A), or a payment company holding it in an account opened through Sharrwah (option B).
- **Where it belongs:** your own list: whether Sharrwah's own company runs payments or balances in the merchant's business, where and when (line 26). It is not part of the platform.
- **When it binds:** at a market's setup, whenever A or B would go live there.
- **Verdict: stays, reworded.** Its last sentence leaves to you "whether the design provides for either arrangement". Line 26, later, settled that: "the platform keeps room for each of these, whoever provides it", and how is engineering's. Proposed words: "No arrangement that holds sellers' money through Sharrwah goes live in any market without the founder's decision: whether Sharrwah itself holds it (option A) or a payment company holds it in an account opened through Sharrwah (option B). It limits only what goes live. The platform keeps room for both, as the decision of 29 October keeps room for each such service; how is engineering's."
- **The platform's place:** who holds sellers' money, a setting of the business that takes the payment (S-02's E5; Part 3, S-01's E1 and E2).
- **The market's values:** which arrangement is switched on in that market, and which provider or partner holds the money there.
- **Could Yemen enter through it?** *Reading:* yes, as it stands. Leaving "whether the design provides" open allows a platform built for C alone, the one arrangement Yemen's facts show working (decision-1.md, 'Recommendation', 4). One market's present limits would then be the platform's shape. The new words keep the guard on what goes live, and off what is built.

### Line 15 · One Yemen row per decision (25 October)
- **What it decides:** Yemen's scenarios are cut; instead every decision gets one Yemen row (what each option needs in Yemen today, and whether that exists); no more work on Stage 1's model.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** Line 35 replaced it: a market's providers, law and limits are that market's setup, "filled into those places, and never define the platform". The plan reads a market when you decide to set it up (`PLAN.md`, 'The aim'), and its method and steps have no market row per decision.
- **The platform's place:** none; it is a way of working.
- **The market's values:** what each place needs in a market, and whether that exists there. That check now runs at the market's setup, for any market, Yemen included.
- **Could Yemen enter through it?** Yes, as it stands: it brings Yemen's facts into every platform decision before Yemen is set up. S-02's D8 and D9 are needs "the Yemen row found that no platform meets" (S-02 `decisions.md`, its opening). Retired, it can't: a need found at a market's setup that Shopify's shape lacks is met then, case by case (line 35).

### Line 16 · Decision 1: who holds sellers' money (25 October)
- **What it decides:** at launch, in every market, Sharrwah holds no seller's money. Each payment method's provider holds it, in the seller's own account; a courier holds cash on delivery until it settles with the seller; a transfer or cash goes to the seller. Three defaults; A and B off.
- **Where it belongs:** three parts.
  - *Your own list:* Sharrwah's own company runs no payments or balances service at launch (A and B off; defaults 1 and 3), from line 26's list.
  - *The platform, a place that varies:* who holds sellers' money, under first decision 5, where a market's legal entity "can carry its own payments account" (first-decisions.md, 'Payment providers'). C is its value everywhere at launch. Default 2's platform part is the merchant's one bill (first decision 12).
  - *A market's setup:* which providers, couriers and ways of paying outside a provider fill C there.
- **When it binds:** your part now, and again at each market's setup where A or B would go live; the place at first decisions 5 and 12; the providers at each market's setup.
- **Verdict: split.**
  - *Platform part, stays:* "Who holds sellers' money is a place in the platform, set for the business that takes the payment. At launch its value is C in every market: each payment method's own provider holds the money, in the seller's own account with that provider; a payment taken outside any provider goes to the seller."
  - *Your part, stays as yours:* A and B stay off until you decide (the guard, line 8); defaults 1 and 3 as written; default 2 as line 20 narrows it.
  - *Market part, waits for each market's setup:* which providers, which couriers collecting cash on delivery, and which transfer or cash channels fill C there.
- **The platform's place:** the holding setting, and a way to record a payment taken outside any provider, as Shopify lets a merchant "mark the order as paid" (decision-1.md, 'Recommendation', 3).
- **The market's values:** that market's providers, couriers and offline channels, and the terms each sets.
- **Could Yemen enter through it?** *Reading:* yes, in two ways, as it stands. Its words make Yemen's ways of being paid part of the platform decision: a courier holding cash on delivery and buyers paying by transfer (decision-1.md, 'Recommendation', 4, YK-203 and YA-131). And "in every market at launch", read as a property of the platform rather than a value, would build in the one arrangement Yemen shows working (the pilot's "C for Yemen now", same page). The split keeps a market-neutral place in the platform, makes Yemen's couriers, wallets and transfers Yemen's setup, and leaves your choice, which names no market, with you.

### Line 17 · Decisions 2 to 12, settled by Decision 1 (25 October)
- **What it decides:** under C, each provider or courier collects, settles, pays out and deducts its own fees, on its own terms. Sharrwah sends no payouts, has no agency role in receiving payments, takes no security interest in sellers' money, and bills its fees apart. Installments (13) and currency (14) go to their subjects.
- **Where it belongs:** the values line 16's place takes under C, following from your choice; each provider's terms are a market's setup. Each answer reopens when A or B is switched on in a market (S-01's register, S01-D2 to S01-D12).
- **When it binds:** with line 16; each provider's terms at that market's setup.
- **Verdict: stays, reworded.** The subjects it sends Decisions 13 and 14 to are gone (line 18). Proposed words: "While a market runs C, the pilot's Decisions 2 to 12 follow from Decision 1: each provider or courier collects, settles, pays out and deducts its own fees, on its own terms; Sharrwah sends no payouts, has no agency role in receiving payments, takes no security interest in sellers' money, and bills its own fees apart. Where A or B is switched on in a market, those answers come to the founder with it. Installments (Decision 13) are decided with the payments area's design, and currency (Decision 14) with first decision 7, Money."
- **The platform's place:** line 16's, and the order's payment record with a separate holder's ledger (S-01's E2).
- **The market's values:** each provider's terms there: settlement, payout timing, fees, refunds, reserves.
- **Could Yemen enter through it?** *Reading:* yes, as it stands, through currency. It sends currency to its subject (S-09), where D9's condition on every money record, drawn from Yemen alone, waits (S-02's register, S02-M6). The new words send currency to first decision 7, read from Shopify's shape, where D9's platform part is weighed with its cost (Part 3, D9). The pilot's Yemen-specific currency proposal, "the rial recorded apart by area", is already not carried (S01-D14).

### Line 19 · Keeping room for A and B (26 October)
- **What it decides:** keep room in the design for A and B. Who holds sellers' money is a market's setting, C everywhere at launch (S-01's E1). An order's payment record is the same whoever holds the money, and a holder's ledger of balances, holds and payouts is a separate part, empty under C (E2).
- **Where it belongs:** the platform: a place that varies (E1, under first decision 5) and a common record (E2, the payments area, under first decisions 2 and 7).
- **When it binds:** first decision 5 for the setting; the payments area's design for the record.
- **Verdict: stays, reworded.** Two things moved since. Line 26 made keeping room the platform's rule, and how it is kept engineering's. And S-02's E5 read "market" as the evidence shows it, as you asked ("my words of 26 October were a working description", `founder-messages/2026-10-29-intent-handoff.md`, line 39): Shopify assigns businesses to markets "to determine payment processing". Proposed words: "Who holds sellers' money is a setting of the business that takes the payment, which each market reaches through the business assigned to it; it is not a property of the platform. C is its value everywhere at launch. An order's payment record is the same whoever holds the money; a holder's ledger of balances, holds and payouts is a separate part, empty under C. A and B stay off under the guard. How the room is built is engineering's."
- **The platform's place:** the holding setting on the business record, and a payment record that doesn't depend on it, as Shopify keeps its payments account (balance, payouts) apart from an order's transactions (S-01's register, S01-E2's evidence).
- **The market's values:** which business serves that market, and which arrangement is on there.
- **Could Yemen enter through it?** *Reading:* yes, as it stands. "A market's setting", read as a country or an area within one, could key the holding arrangement on Yemen's two areas, where holding money would need a licence in each, under different authorities (decision-1.md, 'Recommendation', 4, YA-102). The new words key it on the business, as Shopify's shape does. Yemen's split then becomes that market's businesses and providers, not a key of the platform.

### Line 20 · Default 2 holds while a market runs C (26 October)
- **What it decides:** Sharrwah's fees are never taken from sellers' money at a provider while a market runs only C. Where A or B is switched on in a market, how fees are collected there comes to you with it.
- **Where it belongs:** the platform, common: the merchant's one bill (first decision 12), kept apart from sellers' payments (S-01's E3). Your list: plans and prices, and, with A or B, how fees are collected there.
- **When it binds:** first decision 12; and at a market's setup where A or B would be switched on.
- **Verdict: stays.**
- **The platform's place:** the bill. Shopify does the same where its own payment service is off: its fees go on its bill (decision-1.md, 'Three edges of C', 2).
- **The market's values:** which arrangement runs there; with A or B, your choice of how fees are collected.
- **Could Yemen enter through it?** *Reading:* no. It names no market's facts; it follows from C and the guard.

### Line 21 · No test of Decision 1 against Shopify alone (26 October)
- **What it decides:** not to test Decision 1 against Shopify's evidence alone.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** Line 35 replaced it. The platform is built on Shopify's model, so Decision 1's platform part is read from Shopify's shape anyway, at first decisions 5, 7 and 12 (`PLAN.md`, the steps, 3).
- **The platform's place, the market's values:** none of its own; it governed a check.
- **Could Yemen enter through it?** *Reading:* yes, as it stands. Declining the test left the holding place resting on the pilot's reading of five platforms and of Yemen (decision-1.md, 'Recommendation', 1 to 4), never on Shopify's shape alone. Your choice needs no test: it is a decision. The place it fills does, and is now read where Yemen's facts carry no weight.

### Line 22 · B1 to B8 left in history (26 October)
- **What it decides:** your G1 intent (B1 to B8) is not restated. Its concern, one market's limits becoming permanent architecture, is covered by the plan's aim and its guard on the first market; the questions it raises go to subjects S-04, S-07 and S-09.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** Line 35 replaced it: it states the concern itself ("never define the platform"), and the guard on the first market and the subjects this row relied on are not in the plan of 1 November. B1 to B8 stay in history and bind nothing. A question they raise is taken up when a first decision or an area's design reaches it, through the pinned link in line 22. The registers' drivers that cite the old guard (S01-R3, S02-R3) lapse with it.
- **The platform's place, the market's values:** none.
- **Could Yemen enter through it?** *Reading:* yes, as it stands. The guard it relies on worked by testing each recommendation with the Yemen row (S-02's register, S02-R3), the path by which D8 and D9 entered (S-02 `decisions.md`, 'Needs no reference meets'). Retired, line 35 is the guard.

### Line 25 · Sharrwah's markets (28 October)
- **What it decides:** Sharrwah's markets are in MENA, Yemen among them, and not all at launch. Yemen's present circumstances and today's business capacity don't become permanent constraints "without a genuine, justified reason". Sharrwah competes on regional fit and product quality.
- **Where it belongs:** your own list: markets, their order, partners (line 26 restates the list). Its rule on Yemen's circumstances is now line 35's.
- **When it binds:** now for the list; each market at its setup.
- **Verdict: stays, reworded.** Proposed words: "Sharrwah's markets are in MENA: the GCC and North Africa (Egypt, Morocco, Algeria, Tunisia), Jordan, Lebanon and others. Yemen is one of them, and its circumstances may change. Not all are in launch scope: pursuing each depends on resources and a team for its business side, not on any intention to rule it out. Sharrwah competes on regional fit, through strong support for local ecosystems and partners, and on product quality: performance, completeness, coherence, trustworthiness, user experience and care. A standing decision." The dropped sentence is replaced by line 35 (a market's limits "never define the platform") and line 26 ("Launch and today's resources decide when, never whether").
- **The platform's place:** none of its own. Local partners reach the platform through places it builds anyway: each business's payment accounts (first decision 5) and extensions (first decision 14).
- **The market's values:** which markets, in what order (yours); each market's circumstances, Yemen's included, at its setup.
- **Could Yemen enter through it?** Yes, as it stands: "without a genuine, justified reason" lets Yemen's present circumstances become a permanent constraint once a reason is found. The new words leave no such exception.

### Line 30 · No veto on S-02's rulings (30 October)
- **What it decides:** no veto on S-02's rulings D1 to D9 and E1 to E5. How many markets a plan allows, and of which kinds, are your plans and prices. A conflict between a ruling and the model is reopened with its evidence, not forced to fit.
- **Where it belongs:** the platform (the rulings, at first decisions 5 and 7), your list (plans and prices), the method (the reopening rule).
- **When it binds:** first decisions 5 and 7; the plan line when you set plans; D8's and D9's market parts at the setup of the market that needs them.
- **Verdict: split.**
  - *Platform part, stays:* D1 to D7, and S-02's E1 to E5, as Part 3 sets them out, go into first decisions 5 and 7; D9's platform part goes to first decision 7. The reopening rule, reworded: "When a first decision is recorded from Shopify's shape, a ruling that conflicts with it is reopened with its evidence, not forced to fit."
  - *Your part, stays:* the number and kinds of markets per plan come to you with plans.
  - *Market part, waits:* D8's extension (payment and currency rules keyed on an area within a country, the dated area kept for them, a move's checks on an area change, and E2's area input) and D9's (a market and a currency record for each currency area), until the setup of the market that needs them.
- **The platform's place:** the market and the settings it inherits from the store (first decision 5); both amounts on every money record (first decision 7).
- **The market's values:** each market's countries, currencies, rates and rules, and any area within a country its rules use.
- **Could Yemen enter through it?** Yes, as it stands. "No veto" accepted D8 and D9, which come "from the Yemen row alone" (S-02 `decisions.md`, D8 and D9), and each builds room into the platform now: a dated area on every business record, with an area input to the country entry point (D8, S-02's E2), and a currency record behind every amount (D9). D1 to D7 also rest on five platforms' readings, which line 35 keeps out of the model. The split holds D8's room back (by its own analysis, waiting costs one module), sends D9's question to first decision 7 where its cost is weighed, and re-reads D1 to D7 from Shopify's shape.

---

## Part 2: the other 23 rows, in order

### Line 2 · Go on the plan of 12 October
- **What it decides:** go on `PLAN.md` as it stood on 12 October (at `79c866c`), with the rules in its section 6.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** Replaced twice: by line 12, which returned to the plan at `e4d5cee`, and by line 35, on which today's `PLAN.md` rests ('The aim'). Two register drivers cite this go for "one platform for many markets" (S01-R1, S02-R1); lines 26 and 35 now say it.

### Line 3 · No standing business model
- **What it decides:** no standing business model (what Salla and Zid do was offered); let it come from the evidence.
- **Where it belongs:** the method, for where the model comes from; the business choices around it are your list.
- **When it binds:** no longer.
- **Verdict: retired.** Replaced by line 35: the model is Shopify's, and "No other platform's reading shapes the model". The business decisions around it (plans and prices, partners, whether Sharrwah's own company runs a service) are your list (line 26).

### Line 4 · Credentials in evidence
- **What it decides:** evidence holding credentials, cookies or tokens is read and cited like any other; they come from synthetic environments you rotate.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays.** *Reading:* nothing in it turns on a market or on the old frame.

### Line 5 · Q3's two sets of rows
- **What it decides:** Q3 uses both the 81 payment rows and the 179 questions; both are agent-written and are not Sharrwah's requirements.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** The method it governed is gone: Q3's check of the class's model (line 31) has no step in the plan of 1 November. Its caution, that an agent's list is not a requirement, is carried by the rule that every claim is a fact, a reading or an assumption (`PLAN.md`, the method, 1).

### Line 6 · Agents' effort, delegated
- **What it decides:** the coordinator sets the agents' effort by step (`PLAN.md`, section 11).
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** Replaced by line 32, which sets the floor and says it replaces the 13 October table, and by line 13 (engineering owns the method). `PLAN.md` has no section 11.

### Line 7 · How work comes to you
- **What it decides:** the pilot's entry let you decide. From then on: plain business words, a term that can't be avoided defined in one line, quotes and ids kept in the files; several decisions in one message, each with its own answer line; method rulings listed one plain line each, any of which you may overturn.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays, reworded.** Its answer about the pilot's entry is history; the rest holds. Line 26 widened engineering's share beyond the method, so "method rulings" becomes "engineering's rulings". Proposed words: "Everything for the founder is in plain business words, with a term that can't be avoided defined in one line, and quotes and ids kept in the files. Several decisions may come in one message, each with its own answer line. Engineering's rulings go on as the plan allows, each listed in one plain line the next time work comes back, and the founder may overturn any."

### Line 9 · Following the work
- **What it decides:** you follow the work through a report at each milestone and planned pause.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays.** *Reading:* it fits the plan, where every step ends in a decision for you (`PLAN.md`, the method, 5), and this step in one page (the steps, 2).

### Line 10 · Code
- **What it decides:** spikes and exploratory code are allowed; production code waits for requirements, architecture and engineering documentation.
- **Where it belongs:** the method.
- **When it binds:** now; it governs building.
- **Verdict: stays.** `PLAN.md` carries it (the steps, 4).

### Line 11 · No merchant interviews
- **What it decides:** none, ever.
- **Where it belongs:** the method; your own choice.
- **When it binds:** now.
- **Verdict: stays.**

### Line 12 · The reset of 25 October
- **What it decides:** return to the plan as it stood at G1 (`e4d5cee`). Everything after G1 is history and binds nothing; Decision 1 is open again; your decisions of 10 October (F-00 to F-06, O-01) bind nothing; three decisions of 24 October stay (lines 9 to 11).
- **Where it belongs:** the method.
- **When it binds:** now for its rule on history; the rest no longer.
- **Verdict: stays, reworded.** The plan it returned to was replaced by the plan of 1 November (line 35); Decision 1 was answered (line 16); lines 9 to 11 stand on their own. One rule still holds, and no other decision of yours states it. Proposed words: "History, everything outside the working files, binds nothing. What it found that holds is used only through its sources, pinned to a commit. The founder's decisions of 10 October (F-00 to F-06, and O-01's open question on which company contracts with sellers) bind nothing; what they raise is decided when the work reaches it." *Reading:* O-01's question is on your list (the company, line 26), and comes to you at a market's setup.

### Line 13 · Who decides what
- **What it decides:** engineering owns the method; you decide business questions only, and aren't asked to audit lists.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays, reworded.** Its pointer to `PLAN.md` section 3 names a section the plan no longer has, and your questions are now listed in line 26. Proposed words: "Engineering owns the method: the coordinator decides how the work is done. The founder decides business questions only, as the decision of 29 October lists them, may veto any of engineering's decisions, and is not asked to audit lists of practices or decisions."

### Line 14 · No decision holds because it was accepted before
- **What it decides:** a decision is assessed on its merits before anything builds on it.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays.** This review applies it.

### Line 18 · The subjects S-02 to S-11
- **What it decides:** each of the ten subjects runs on the evidence, in the list's order.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** The method it governed is gone. The plan of 1 November works by first decisions read from Shopify's shape, then areas (`PLAN.md`, the steps), and line 35 keeps out the other platforms' readings the subjects ran on. What the subjects held for you still comes to you when the work reaches it: the contracting company, partners, whether Sharrwah's own company runs payments or shipping, the markets served, and prices (S-02 `decisions.md`, 'What moved to other subjects').

### Line 23 · A budget never costs evidence
- **What it decides:** S-02 continues at a budget of 700 million tokens. A budget must never cost evidence about the references: you move to a higher plan first, and the coordinator says when one is needed. Standing, for every subject.
- **Where it belongs:** your list (spending), applied to the method.
- **When it binds:** now.
- **Verdict: stays, reworded.** S-02's own budget is history, the subjects are gone, and the references are now Shopify alone (line 35). Proposed words: "A budget must never cost evidence about Shopify's shape: the founder moves to a higher plan before that happens, and the coordinator says when one is needed. A standing decision for every step."

### Line 24 · Evidence not held is a request
- **What it decides:** evidence a run could capture but that isn't held goes out as a request: the coordinator records the gap and leaves a handoff naming the run; you hand it on; the local agent captures what it can, pushes and notifies. Standing.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays, reworded.** Line 35 leaves Shopify's evidence the only evidence that shapes the model, and the subjects are gone. Proposed words: the row as written, with two changes: "in observed-sh or observed-sa" becomes "in observed-sh", and "when a subject needs them" becomes "when a decision needs them".

### Line 26 · Sharrwah's intent (29 October)
- **What it decides:** Sharrwah belongs to the class that Shopify, Salla and Zid represent, and its extent comes from that class. What fills a slot in a market is that market's setup. It lists your business decisions; everything else is engineering's, under your veto. It sets the test for narrowing the platform, and the rule for a product gap.
- **Where it belongs:** your own list, and the frame of platform and market setup.
- **When it binds:** now.
- **Verdict: stays, reworded.** Its own review note says the decision of 1 November holds where they differ. They differ in one thing: a class of several platforms against Shopify's model alone. Proposed words: "Sharrwah is a merchant platform built on Shopify's model, meant to grow across MENA, one market after another as resources and teams for each market's deals allow. Yemen is the first market set up on it. Its extent comes from Shopify's model, not from the launch. What Shopify's shape establishes, and the places it leaves for outside parties, belong to the platform. What fills a place in a market (its providers, partners and law) is that market's setup, needed when the place is filled; it never defines the platform. Engineering establishes from Shopify's evidence what is common, how it fits together, where variation is genuine, and which commitments keep growth open. Launch and today's resources decide when, never whether. I decide which markets, in what order and when, and which merchants Sharrwah goes after first; plans and prices; commercial agreements and partners; the company, its legal structure and licences; spending; and whether Sharrwah's own company runs a service in the merchant's business (payments, balances, financing, shipping, a marketplace, point of sale, data services, a buyer app), where and when. The platform's capabilities for each are Shopify's shape: Sharrwah rules out nothing it shows, and the platform keeps room for each, whoever provides it. Everything else is engineering's, and I may veto any of it. The test for any work: narrowing what Shopify's shape establishes needs a decision of mine or an engineering reason with evidence. Ordering it is ordinary engineering. A need one of my markets shows that Shopify's shape doesn't meet is a product gap: building it goes with that market's setup, and it never defines the platform. How the platform keeps room for it is engineering's. My decision of 28 October stays in force where this one doesn't restate it."
- *Reading:* the changes are "the class" to Shopify's model or shape; "slots" to "places", line 35's word; "which shape is better where they differ" dropped, since one reference no longer differs from itself; and the added lines (1), (2) and (4) folded in. Your list is unchanged, and it is the list this review sorts against.

### Line 27 · The class's model before architecture
- **What it decides:** architecture waits until the class's model has its extent (at a budget of 250 million tokens), then grows area by area beside the subjects, starting once the extent's report has reached you.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** Replaced by line 35 (Shopify's model, not the class's) and the plan's steps (`PLAN.md`, the steps, 1 to 4). *Reading:* its order, the domain's shape before architecture, survives: Shopify's shape is read before any first decision is recorded.

### Line 28 · Which quality wins
- **What it decides:** trustworthiness first; then coherence and user experience; then performance; then completeness, read as what each release delivers. Scale numbers later.
- **Where it belongs:** the platform, common to every market: it orders the qualities every first decision weighs.
- **When it binds:** now, at each first decision that turns on a quality (`PLAN.md`, the method, 4).
- **Verdict: stays.** *Reading:* "never what the model covers" now reads as Shopify's model, and still holds.

### Line 29 · Architecture's own plan; line (3) taken out
- **What it decides:** architecture gets its own plan by established practice (what it needs to know and where from; who decides and how; which areas come first), brought to you at GM, starting on your go. Line (3) comes out of line 26; what keeping room means is stated in that plan; D9 is the worked example.
- **Where it belongs:** the method.
- **When it binds:** no longer, as worded.
- **Verdict: retired.** The method it governed is gone: GM, the extent's report, and an architecture plan beside the class's model aren't in the plan of 1 November. Its parts are carried. Line (3) is out of line 26. Engineering's decisions are listed for your veto (line 26; `PLAN.md`, 'Who decides'). *Reading:* what keeping room means is now stated by practice in `PLAN.md` (the method, 3 and 5): a place for whatever varies, naming its mechanism and when it is bound, decided when something resting on it is about to be built. **Needs you:** this row made architecture start on your go. Recommended: your go on the first decisions' records (`PLAN.md`, the steps, 3) is that go.

### Line 31 · What comes at GM
- **What it decides:** the architecture plan grades its sources by the Knowledge Map's source types; at GM, the Knowledge Map's page is rebuilt from the model's files, with Q3's check.
- **Where it belongs:** the method.
- **When it binds:** no longer.
- **Verdict: retired.** The method it governed is gone (GM, the class's model and its files). Your view of each step is now its one page (`PLAN.md`, the steps, 2).

### Line 32 · The agents' effort floor
- **What it decides:** no agent runs at `medium` or `low` for reading evidence, reviewing or making an engineering judgement; only `high`, `xhigh` or `max`. A type of task that `high` or `xhigh` keeps missing runs higher, judged by the quality and completeness of results.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays, reworded.** Its last sentence points to a table and a section (`PLAN.md`, section 11) that are gone, along with line 6. Proposed words: the row without its last sentence ("It replaces the 13 October effort table's ...").

### Line 33 · Read the evidence through its guides
- **What it decides:** before any capture request goes out, the evidence repositories are read through their own reading guides and indexes, not by search alone; search follows the guides.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays, reworded.** Line 35 leaves only Shopify's evidence shaping the model, and `method/held_index.py` is not among the tools the repository keeps (`CLAUDE.md`, 'The working files'). Proposed words: "Before any capture request goes out, what observed-sh holds is read through its own reading guides and indexes, not by search alone: README.md, docs/READING.md, docs/GAPS.md, docs/OPERATING.md, index/, structures/README.md and structures/REGISTER.tsv. Search (method/corpus_search.py) follows the guides."

### Line 34 · Up to four agents at once
- **What it decides:** up to four agents at once, where it had been two; fewer if agents start being stopped mid-run.
- **Where it belongs:** the method.
- **When it binds:** now.
- **Verdict: stays.**

---

## Part 3: what lines 16 to 20 and 30 carry

### Decision 1's follow-ons (S-01's register)

#### S-01's E1 · The holding arrangement, bound per market
- **What it decides:** who holds sellers' money is a market's setting, C everywhere at launch, not a property of the platform.
- **Where it belongs:** the platform, a place that varies, under first decision 5.
- **When it binds:** first decision 5.
- **Verdict: stays, reworded,** in the form of S-02's E5: a setting of the business that takes the payment, reached by each market through the business assigned to it. The words are those proposed for line 19.
- **The platform's place:** the setting on the business record. **The market's values:** which business serves each market, and its arrangement (C at launch).
- **Could Yemen enter through it?** *Reading:* as for line 19. Keyed on "market" read as a country or an area within one, it could take Yemen's two areas as a key; keyed on the business, it can't.

#### S-01's E2 · One payment record, a separate holder's ledger
- **What it decides:** an order's payment record is the same whoever holds the money. A holder's ledger (balance, holds, payouts) is a separate part, present only where Sharrwah or a payment company holds; under C, a provider's balance is read from the provider.
- **Where it belongs:** the platform, common: the payments area, under first decisions 2 (areas meet only through each other's interfaces) and 7 (money).
- **When it binds:** the payments area's design.
- **Verdict: stays.** It is Shopify's own shape: an order transaction names its gateway, with Shopify's own payment service as an optional part, and the payments account, with its balance and payouts, is a record apart (S-01's register, S01-E2's evidence).
- **Could Yemen enter through it?** No: it is read from Shopify's schema.

#### Default 1 · An account a seller asks for through Sharrwah
- **What it decides:** an account a seller asks for through Sharrwah, but holds under its own agreement with the provider, counts as C. Where Sharrwah would be party to the money, or to the provider's agreement for it, it is B and comes to you.
- **Where it belongs:** your list: whether Sharrwah's own company is party to sellers' money, and agreements and partners (line 26).
- **When it binds:** at a market's setup, when an account is offered through Sharrwah there.
- **Verdict: stays.** *Reading:* it names no market. Its examples (Salla with Tabby, Shopify with PayPal: decision-1.md, 'Three edges of C', 1) don't shape the model, and your choice is a decision, not a claim to check.

#### Default 2 · Sharrwah's fees billed apart
- **What it decides:** Sharrwah's fees are billed apart, never taken from sellers' money at a provider.
- **Where it belongs:** the platform's part is the merchant's one bill (first decision 12); your part is plans and prices.
- **When it binds:** first decision 12; and at a market's setup where A or B would be switched on.
- **Verdict: stays, reworded,** with line 20 folded in: "Sharrwah's fees are billed apart, on the merchant's bill. While a market runs only C, they are never taken from sellers' money at a provider; where A or B is switched on in a market, how they are collected there comes to the founder with it." S-01's E3 (Sharrwah's fees in a billing part apart from sellers' payments) follows from it and stays, under first decision 12.
- **Could Yemen enter through it?** No (line 20).

#### Default 3 · No balance that sellers pay into
- **What it decides:** no balance that sellers top up, at launch.
- **Where it belongs:** your list ("balances", line 26).
- **When it binds:** at a market's setup, if a balance would be offered there.
- **Verdict: stays.** The platform keeps room for it, as for every service on your list (line 26).
- **Could Yemen enter through it?** No: it names no market.

S-01's E4 (a refund is carried out by whoever holds the money, and its result is recorded on the order) stays, for the payments area's design.

### S-02's rulings (S-02 `decisions.md` and register)

D1 to D7 "come from the five references alone, with no market's facts" (S-02 `decisions.md`, its opening), so no Yemen concern enters through them. Their risk under line 35 is the other four platforms' readings. Each new wording keeps what Shopify's shape shows (first decisions 5 and 7) and drops the rest.

#### D1 · Where a store's country is held
- **What it decides:** a store's country is the country of the business record behind it, one per store at launch, with room for more. The address, a map location, the billing address and the currency never set it.
- **Where it belongs:** the platform, common: the seller's legal entity under first decision 5 (Shopify: "A legal entity through which a merchant operates").
- **When it binds:** first decision 5.
- **Verdict: stays, reworded,** without its line on the seat, a Salla setting (S-02 `decisions.md`, D1). Proposed words: "A business record holds the store's country, one per store at launch, with room for more, as Shopify's business entities do. The address, a map location, the billing address and the currency never set the country. A market may show buyers another country or address, for display only."
- **The platform's place:** the business record and its country. A store's country is the merchant's own data, not a market's setup.

#### D2 · When a seller moves country
- **What it decides:** a business's country never changes in place; a seller who moves adds a business record for the new country.
- **Where it belongs:** the platform, common: the area that holds business records (first decision 5's legal entity).
- **When it binds:** that area's design.
- **Verdict: stays, reworded,** its pointers to S-04, S-07 and S-05 replaced: "The checks of the areas that rest on the country (payment accounts, verification, tax forms) run first." *Reading:* the rule is Shopify's own lock: a change only once every financial service is off, and a new business record for a person trading alone (S-02 `decisions.md`, D2).

#### D3 · What follows the seller's country
- **What it decides:** every rule that depends on the seller's country reads one country, through one entry point: that of the store's main business, or of the business that served the order or market in question.
- **Where it belongs:** the platform, a place that varies (first decision 5): the rules differ by country, and where they are read is common.
- **When it binds:** first decision 5.
- **Verdict: stays, reworded,** its "not ruled out" line without subject pointers: "other places with rules of their own, decided by the areas that own them: where stock is held, each owner's residence, a payment account's country, and an area within the country where a rule such as tax uses one." *Reading:* the entry point is Shopify's shape: it assigns businesses to markets "to determine payment processing and Order attribution", and orders keep the business they were placed under (S-02's register, S02-E2's evidence).
- **The market's values:** each country's rules (its terms, providers and law), filled in at that market's setup.

#### D4 · What a market can be
- **What it decides:** a market is a named set of conditions of a few kinds. Markets nest, and a buyer is matched by their whole context.
- **Where it belongs:** the platform, common (first decision 5).
- **When it binds:** first decision 5.
- **Verdict: stays, reworded** to Shopify's kinds: "A market is a named set of conditions a buyer matches, of Shopify's kinds: a region, a location, a company location (business customers) and a channel. A market may sit inside another and inherit from it. A buyer is matched by their whole context, not only their country." It drops the storefront kind and the customer group kept beside markets, both BigCommerce's (S-02 `decisions.md`, D4). *Reading:* whether a price can key on a group of customers is the catalog area's design, read from Shopify's shape.

#### D5 · How markets overlap
- **What it decides:** a market may hold several countries; markets nest within one kind; across kinds the most specific market wins, and lists may combine.
- **Where it belongs:** the platform, common (first decision 5, where a buyer resolves to one set of values).
- **When it binds:** first decision 5.
- **Verdict: stays, reworded** on Shopify alone: "A market may hold several countries; one country per market remains a choice. Within one kind, markets nest: a market inside another inherits from it and takes priority. Across kinds, a single value comes from the most specific market, and a list may combine, as Shopify combines catalogs. Which kind comes first is stated for business-customer, retail and region markets, in that order, as Shopify states it; for other kinds it stays open. A market's conditions say who it applies to." It drops the reasons drawn from all five platforms (tax by the buyer's country "on all five"; Salla's and BigCommerce's limits on who enters).

#### D6 · Settings that vary by market
- **What it decides:** each setting a seller may vary by market is held once for the store, and each market may change it; 18 settings are named; a product may narrow its shipping and payment methods.
- **Where it belongs:** the platform, a common pattern (first decision 5: market customizations "inherit your store's default settings" and may override them).
- **When it binds:** first decision 5 for the pattern; each area's design for which of its settings a market may hold.
- **Verdict: stays, reworded:** "Each setting a market may hold is held once for the store, and a market may override it, as Shopify's market customizations inherit the store's settings. A single value comes from the most specific market, a market's over the store's; a list may combine across the markets a buyer matches, as Shopify combines catalogs. Which settings a market may hold is each area's to say, from Shopify's shape, as the area is designed." It drops the 18 settings counted across five platforms, and engineering's own choice to combine payment methods and shipping options. *Reading:* each is its area's to decide, as first decision 5 says: "Each area must say which of its settings a market may hold".

#### D7 · Currency and prices per market
- **What it decides:** each market may sell in its own currency, at its own prices and exchange rate. Every order, refund and report keeps both amounts, with the market and rate used. The store's currency stays the one for its reports and gift cards. Sharrwah sets no payout currency.
- **Where it belongs:** the platform, common: both amounts on every money record (first decision 7: Shopify's pair holds "the equivalent in the shop's base currency"), and a market's currency settings (first decisions 5 and 7).
- **When it binds:** first decision 7.
- **Verdict: stays, reworded,** "Which currencies and rate sources is S-09's question" becoming "Which currencies a market uses, and where its rates come from, are that market's values, set at its setup." Its "no payout currency" follows from Decision 1, and reopens with it.
- **The market's values:** each market's currencies and rates. D7 itself carries no Yemen fact; D9 builds on it.

#### D8 · A seller's area within a country
- **What it decides:** tax rules may use an area within a country. The area is held from the start as a dated field of the business record and of the store's locations. Room is kept for payment and currency rules keyed on an area, and for a move's checks when the area changes, built with the setup of the market that needs them.
- **Where it belongs:** two parts.
  - *The platform, a place that varies:* an area within a country for tax rules, as Shopify ties a seller's tax to a province (S-02 `decisions.md`, D8, 'What the platforms do'). Taxes have their place under first decision 5; calculating them is the tax area's job (first-decisions.md, 'Taxes and duties').
  - *A market's setup:* payment and currency rules keyed on an area, the dated area kept for them, and a move's checks on an area change.
- **When it binds:** the tax part at the tax area's design; the rest at the setup of the market that needs it.
- **Verdict: split.**
  - *Platform part, stays:* "Tax rules may use an area within a country, as Shopify's do."
  - *Market part, waits for the market that needs it:* payment and currency rules keyed on an area, the dated area field on the business record and locations, a move's checks on an area change, and the area input to the country entry point (S-02's E2).
- **The platform's place:** a country's subdivision, readable by tax rules. **The market's values:** which areas a market's rules use, and the payment, currency and rate rules keyed on them.
- **Could Yemen enter through it?** Yes, as it stands. The need is Yemen's: areas of one country answering to different rules for payment services, the currency and the rate (S-02 `decisions.md`, D8, 'The need'; decision-1.md, 'Recommendation', 4, YA-102). D8 would put a dated area on every business record from the start, and make the country entry point take an area, before Yemen is set up. Its own reckoning puts the cost of waiting at one module, past records being the only loss, and "whether they need it isn't shown" (S-02's register, S02-D8). *Reading:* so the last responsible moment (`PLAN.md`, the method, 5) is that market's setup. The split keeps in the platform only what Shopify's shape shows: tax by area.

#### D9 · Two currency areas under one currency code
- **What it decides:** for now, two currency areas sharing one code are told apart only by market, each market with its own rate. Room is kept for naming an area in the currency itself: amounts refer to a currency record, one per code at launch, a choice left to S-09.
- **Where it belongs:** two parts.
  - *The platform, common:* how every amount names its currency (first decision 7). Shopify names it by its code ("The currency codes that represent the world currencies throughout the Admin API", first decision 7).
  - *A market's setup:* the two currency areas, a market and a rate for each, and a currency record naming an area.
- **When it binds:** the platform part at first decision 7; the market part at the setup of the market that needs it.
- **Verdict: split.**
  - *Platform part, stays,* as engineering's recommendation to first decision 7, moved there from S-09, which is gone: "Amounts refer to a currency record, one per currency code at launch." First decision 7's record states it as an extension of Shopify's shape, as line 35 allows case by case, with its cost either way (`PLAN.md`, 'Risks': "named in the decision that meets it").
  - *Market part, waits:* a second currency record under one code, with its markets and rates, at the setup of the market that needs it.
- **The platform's place:** a currency record that amounts refer to. **The market's values:** which records a market's currencies need, and their rates.
- **Could Yemen enter through it?** Yes, as it stands. The need is Yemen's alone (S-02 `decisions.md`, D9, 'The need': one code over two currency areas with different notes and rates), and the room would have shaped every money record through S-09, with no first decision weighing it. The split admits only a place that names no market, decided at first decision 7 with its cost; no Yemen value enters. *Reading:* first decision 7, not the market's setup, is the last responsible moment here, because D9's own reckoning makes a bare code in every amount a later redesign of "every money record, rate and report" (D9, 'Changing course later'). You placed this room "in the core: how every amount names its currency" (`founder-messages/2026-10-29-go.md`, edit 4), and called D9 the worked example of keeping room (line 29).

#### S-02's engineering constraints, E1 to E5
| | What it decides | Verdict | Binds at |
|---|---|---|---|
| E1 | Each per-market setting is read through one entry point: a single value from the most specific market, then the store; a list may combine | Stays, reworded: without its customer-group clause (as D4) | First decision 5 |
| E2 | Each rule keyed on the seller's country is read through one entry point, keyed on the business serving the order or market; each order records that business | Stays, reworded: without "with D8 the entry point also takes an area", which waits with D8 | First decision 5 |
| E3 | Every store has one main market, carrying the store's own values | Stays: Shopify's primary market (S-02's register, S02-E3) | First decision 5 |
| E4 | A store keeps its own currency for its reports and as the default for gift cards; past records keep the currency of their day | Stays: the shop's base currency in Shopify's pair (first decision 7) | First decision 7 |
| E5 | Who holds sellers' money is a setting of the business that takes the payment, reached by each market through its business | Stays: Shopify's business entities carry payment processing (S02-E5's evidence); it is the new form of S-01's E1 | First decision 5 |
