# The fitness test: can architecture's first decisions be made from the class's model?

**Status:** a test by an agent that made none of the model or the architecture plan, 31 October 2026. It changes nothing: it reads, measures and proposes. It read this repository at `d0fb7f82` (the model's files at `f6e80c4a`; S2-ZD-1 checked but not landed), observed-sh at `04de369da`, observed-sa at `b0bd0b163` and other-product-class at `0d79b794f`.

**How to read the claims.** Counts are facts, by script over the model's files at `f6e80c4a`, unless marked otherwise. Quotes and file paths are facts at the commit named. Anything marked *a reading* is my interpretation; *an assumption* is a stand-in until something better exists. Every "what it needs" list is a reading of established practice (attribute-driven design: the requirements, quality scenarios and constraints a decision serves), not evidence. Every law named is a reading, to be confirmed by its subject from the instrument and its date.

**Words used:**
- *cell:* what the model holds for one capability on one platform;
- *placed:* the cell says where the platform puts the capability (its core, its own service, an extension point, or outside);
- *data and events:* the model's `boundary` rows in `interfaces.tsv`: the objects, webhook topics and access scopes a cell cites;
- *deciding statements:* its `decides` rows;
- *held, not read:* in the evidence repositories, but cited by nothing in the model;
- *decision pack:* a short reading of held evidence for one decision, each object or flow cited at a commit (this test's proposal).

## For the founder, on one page

**What was tested.** Whether architecture could make its six first decisions from the model (`architecture/plan.md`, section 3). Nobody had tried. The risk was that the model is a wide catalogue that architecture can't decide from (`STATE.md`, F1).

**The answer.** The model is a good index of *what* the class does, who does it, and where. It is a weak source for *how*: the data, the states, the rules and the qualities that decide. Much of that is held in the evidence repositories, but the model left it out as detail.

| Decision | Verdict |
| --- | --- |
| 1. How stores are kept apart, and where their data lives | Can be decided now with named gaps kept open, but from practice and Shopify's engineering writing, not from the model. Each store's home region stays open until S-08 has run. |
| 2. Identity and permissions | Can be decided now with named gaps kept open: who verifies sellers in each market (S-07). |
| 3. Money records and currency | **Can't be decided yet.** The model names the records but holds almost none of their shapes or states. Reading what is held, and S-05's e-invoicing rules, would let it. |
| 4. Markets and the seller's country | Can be decided now with named gaps kept open (S-03, S-07). S-02 has done most of it. |
| 5. Events and extension points | Can be decided now with named gaps kept open: the payment and courier contracts (S-04, S-10). |
| 6. Configuration | Can be decided now with named gaps kept open: the plans' limits (S-11, and your plans and prices). |

**The five gaps that most threaten the work:**
1. **The model holds names, not shapes.** Architecture's money and event decisions choose between record shapes, states and payloads. These are held in Shopify's admin schema, in Salla's 409 data schemas and in both platforms' webhook samples, but the model reads almost none of them. 574 of the 1,215 cells that hold statements have no data or events of their own platform.
2. **How stores are kept apart, and where data lives,** is the costliest decision to change. The model has no capability for keeping stores apart, and its Salla cell for where data lives is empty, though the evidence holds Salla's own answers placing store files in AWS Frankfurt. No market's law on where data must live has been read: that is S-08, which runs sixth in the subjects' order.
3. **The invoice record.** Sending invoices to the tax authority (ZATCA in Saudi Arabia) is held only through Salla and Zid. The authority's rules will shape the order and invoice records, and S-05 hasn't run. If architecture follows Shopify's shape, where an invoice is printed from an order rather than issued as a record of its own, that is rework *(a reading)*.
4. **The region's own practices are held thinly, or held and not read.** By evidence rows, Zid's evidence on these decisions is 15% of Shopify's, and Salla's 44%. Of the 29 capabilities that count for the global platforms but not for Salla or Zid, 24 hold nothing, or no placement, for either, so it isn't known whether those are real differences. Some regional practices are held but unread: identity checks through the state (Absher, Nafath) with a Hijri birth date, cash on delivery set per courier, buyer sign-in by phone or WhatsApp, and prices shown in one currency but paid in another.
5. **The subjects that bind these decisions haven't run,** and two of them run late in the list. Also, nothing in the model is scoped to Morocco, Algeria, Tunisia, Jordan or Lebanon, and no regional reference serves them *(a reading)*.

**For your decision: the subjects' order.** Your answer at G2 runs the subjects in the list's order (`founder-decisions.tsv`, 26 October). For the first decisions not to be rework, I propose S-03, then **S-08**, S-04, S-05, **S-10**, S-07, S-09, S-11, and S-06 last. That moves S-08 (where data lives) from sixth to second, and S-10 (delivery and cash on delivery) from eighth to fifth. S-06 (licences) moves to last, because under Decision 1 the providers hold the payment licences. The reasons are in "Which subjects bind which decisions" below.

**Where the remaining work should point.** The second stage reads 705 empty cells, but only 234 of them sit under these six decisions; 89 of those are Salla's and Zid's. Point it there first. Run the qualities pass, narrowed to the kinds these decisions read. Replace the omission review, before GM, with short readings of the held shapes for decisions 2, 3 and 5. Weight the final review toward these decisions' capabilities. Stop adding breadth.

**The test for "enough to start architecture"** is eight checks, each one countable from the files (the last section). Today, decisions 4 and 6 come closest to passing, and decision 3 is furthest from it.

## How the test was run

- **Which capabilities each decision rests on** is my reading. I took them from `python3 -I method/class_slice.py caps` searches and from the full list in `merged/capabilities.tsv`, read by script (the appendix). There are 146 capabilities in all; some serve more than one decision.
- **The depth measures,** per decision and platform, are counted over `merged/cells.tsv`, `evidence.tsv`, `interfaces.tsv` (exact and by landing), `qualities.tsv` and `slot-fillers.tsv`.
- **Qualities** are split into plan terms (prices, fees, rates, trials and allowances per plan) and the rest, by a pattern on each row's label and value. The split is *a reading*: the pattern is coarse.
- **Each gap** is one of three kinds:
  - *held, not read*;
  - *not held*;
  - *no platform can tell*: law, a market's practice, or Sharrwah's own choice.

  I traced each through the repositories' guides first: their `README.md`, `structures/REGISTER.tsv` and `studies/class-model/evidence-map.md`. Then I used `held/selection.tsv` (what the held pass reads, and why it leaves the rest), and searched only to tell whether a gap is held.
- **The scripts** were throwaway, in the session's scratchpad. Each count can be re-run from the appendix's lists and the definitions above.

## The six at a glance

Per platform, in the order Shopify / Salla / Zid / WooCommerce / BigCommerce, or Shopify / Salla / Zid where marked.

| | D1 | D2 | D3 | D4 | D5 | D6 |
| --- | --- | --- | --- | --- | --- | --- |
| Capabilities it rests on | 26 | 26 | 35 | 22 | 34 | 18 |
| Cells placed (of those) | 24/14/11/12/12 | 23/20/14/7/14 | 30/31/30/23/24 | 20/20/16/13/9 | 32/26/19/26/20 | 14/12/9/11/10 |
| Evidence rows, SH/SA/ZD | 553/318/146 | 1,280/809/142 | 1,723/832/427 | 1,242/393/230 | 1,864/789/204 | 1,805/485/104 |
| Data and events, exact, SH/SA/ZD | 24/14/9 | 47/35/10 | 108/100/34 | 54/27/11 | 141/313/19 | 41/16/2 |
| Deciding statements, exact, SH/SA/ZD | 159/145/85 | 463/252/53 | 526/348/222 | 338/178/118 | 219/199/80 | 991/187/48 |
| Capabilities with no data or events of Salla's own / Zid's own | 17/19 | 16/19 | 14/14 | 13/15 | 15/23 | 12/16 |
| Quality rows: plan terms / the rest (all platforms, a reading) | 53/27 | 180/11 | 288/48 | 61/11 | 62/58 | 1,453/34 |
| Empty or unplaced cells, Salla / Zid | 12/15 | 6/12 | 4/5 | 2/6 | 8/15 | 6/9 |

Whole model, for comparison: 574 of 1,215 cells holding statements have no data or events of their own platform, 278 have no deciding statement, and 74 capabilities have no data or events from any platform. The architecture plan gave 572, 260 and 74 at `d9524f74`.

## D1. How stores are kept apart, and where their data lives

**What it needs** (practice; each item a reading):
- **Entities and relations:**
  - the store as the unit kept apart, with every record carrying its store;
  - stores grouped into cells (Shopify calls its cells pods), each cell in one region, and each store with a home region;
  - the owner or organization above stores;
  - kinds of data, each with where it may live and how long it is kept: buyers' personal data, card data, money records, files, logs and backups.
- **Flows and states:**
  - a store's life (trial, active, paused, closed, deleted), and what happens to its data at each stage;
  - export on request and at closing, and erasure on request;
  - moving a store between cells or regions;
  - backup and restore, and a legal request for data.
- **Rules:**
  - no read crosses from one store to another, except by a named path: a partner's access, an app's grant, or the platform's staff, audited;
  - one store's load can't starve another;
  - card data stays inside a certified boundary, or never enters it.
- **Qualities,** each measure an assumption until you give numbers:
  - zero reads across stores in the isolation tests;
  - a store's surge to 50 times its usual traffic leaves the other stores' slowest-1% response time within 10%;
  - at most 5 minutes of data lost, and service back within an hour, if a cell fails;
  - a closed store's personal data deleted on a stated schedule;
  - a store's export ready within 24 hours.
- **What varies:**
  - by market: where personal data must stay, whether sending it abroad needs consent or a licence, and how long records are kept;
  - by plan: API limits (Shopify's "Up to 500% higher" on Plus, `SH-E-1dda6149`);
  - by store: its home region.
- **The law** *(readings, for S-08):*
  - Saudi Arabia's Personal Data Protection Law and its regulation on transfers abroad;
  - the UAE's Federal Decree-Law 45 of 2021;
  - Egypt's Law 151 of 2020, which licenses transfers abroad;
  - Jordan's law of 2023;
  - the card schemes' PCI DSS wherever card data is touched.

  That Yemen has no comprehensive data protection law is an assumption to check.

**What the model holds:**
- **No capability for keeping stores apart.** The qualities pass's design says so: "nothing on how stores are kept apart, and no capability for it" (`studies/class-model/briefs/QL-qualities-design.md`, section 2). There are three statements, all in CM-OPS-001:
  - Shopify: each pod "has a pair of data centers, one active, the other a recovery site" (`SH-C-181/where/SH-S-0673`), and each shard is "fully isolated so a failure couldn't spiral into a platform outage" (`SH-C-181/reason/SH-S-0674`);
  - BigCommerce: its infrastructure is segmented and replicated across availability zones (`BC-C-082/decides/BC-S-0450`).

  Nothing from Salla or Zid. A WooCommerce store runs on the merchant's own host, so it is kept apart by being its own installation *(a reading)*.
- **Where data lives (CM-TRU-014):**
  - Shopify: Google Cloud regions, and new European merchants' data at rest in Europe by default (`SH-C-181/where/SH-S-0638`);
  - BigCommerce: Google in the USA, Germany or Australia (`BC-C-082/where/BC-S-0446`);
  - Zid: its privacy policy lets it transfer data abroad with safeguards (`ZD-C-041/decides/ZD-S-0794`), and where it stores data "is not stated";
  - WooCommerce: the store site's own database;
  - **Salla: nothing.**
- **Retention after a store closes (CM-TRU-016):** Shopify deletes EU merchants' personal data within 90 days of termination (`SH-C-183/decides/SH-S-0209`). Salla has one row; Zid's and WooCommerce's cells are unplaced; BigCommerce has nothing.
- **Card data (CM-TRU-018):** Shopify (Level 1), WooCommerce's payment service and BigCommerce. **Salla and Zid: nothing.**
- **Qualities other than plan terms:**
  - uptime: Shopify "99.9%", Salla "100% uptime", BigCommerce's Cyber Week record;
  - scale: Salla's "15 million transactions in one day" (`SA-E-403ce980`);
  - Shopify's PCI rows, and the location rows above.

  Zid has none.
- **The registers:** S-02 moved "whether one privacy policy and controller govern every store's data" to S-08 (S02-M5). S-01 has nothing on it.
- **Your decisions:**
  - Yemen's present circumstances become no permanent constraint (28 October);
  - trustworthiness comes first (29 October).

**Gaps:**

| Gap | Kind | Where, or why not | Answered by |
| --- | --- | --- | --- |
| How each platform keeps stores apart, beyond Shopify's pods | Held, not read (Shopify); not held (Salla, Zid) | Shopify: `evidence/shopify-engineering/` (E001 to E040, on pods), and observed-sh's `engineering-blog` (436 posts), `open-source` and `compliance-reports` (two SOC 3 reports), which the held pass routes to the architecture plan or the qualities pass (`held/selection.tsv`). Salla, Zid: no trust page held (QL design, section 4) | The qualities pass (isolation kind), then practice and spikes. No subject |
| Where Salla keeps data | **Held, not read** | observed-sa@`b0bd0b163`, `docs/LOG.md`: exports are signed links to bucket `sallaexport` in region `eu-central-1` (AWS Frankfurt), and imports go to `migration-stores.s3.eu-central-1.amazonaws.com`. Verification documents go to a Google Cloud Storage bucket signed with region `auto`, which names no place. Its privacy policy names Saudi Arabia's Personal Data Protection Law and its regulation (`structures/salla/com-policies/privacy/text.txt`, lines 77 to 78) | The qualities pass (QL-SA); S-08 for what it means |
| Where Zid keeps data, and its certifications | Not held | Its policy states transfer abroad, not a location. H-010, for help.zid.sa and docs.zid.sa, is a draft | The qualities pass (QL-ZD). Asking Zid directly is yours |
| Salla's and Zid's card-data scope | Not held | CM-TRU-018 is empty for both | S-04: who renders the card form under C |
| Retention after closing, per market | Held, not read (Salla) | Salla's privacy policy, line 75: data kept "للفترة اللازمة لتحقيق الغرض من جمعها", or deleted at the user's request or when an integration is cancelled | S-08 |
| Each market's law on where data lives and how it may leave | No platform can tell | Law | S-08 |
| Scale: stores, orders a day, peaks | No platform can tell | Yours, later; engineering's bands meanwhile (plan, section 5) | No subject |

**Verdict: can be decided now with named gaps kept open,** from practice and Shopify's engineering writing, not from the model, which holds that these capabilities exist and almost nothing of what decides them. Keep personal data divided by store, and keep each store's home region as a variation point, fixed when the store is created. S-08's answer then becomes a setting per market, not a redesign. Don't pay for a second region before S-08 has run.

**The regional test:**
- **Whose shape:**
  - of the 26 capability names, 11 use Shopify's and Salla's terms, 8 Shopify's alone and 1 Salla's alone;
  - eight count for Shopify, WooCommerce or BigCommerce and for neither Salla nor Zid: TRU-005, TRU-018, TRU-021, API-004, API-011, MIG-006, DVT-006 and CHN-007. In every one, it's because Salla's and Zid's cells hold nothing or no placement, not because either places the capability outside its core;
  - Salla's evidence rows are 58% of Shopify's, and Zid's 26%.
- **Where practice differs:** what is held but unread shows Salla keeping at least store exports and imports in Frankfurt, under a Saudi-law policy, and Zid allowing transfer abroad. Neither shows hosting inside the country. *A reading:* hosting inside a country isn't a feature of the class. If a market requires it, the requirement comes from law, which is what the home region is kept open for.
- **What it would change:** nothing in the decision's form, if the home region is kept open. Whether a second region is likely soon, and so worth building early, is for S-08.

## D2. Identity and permissions: staff, customers, apps and partners

**What it needs** (practice; each item a reading):
- **Entities:**
  - a person, with one sign-in, who may own or work in many stores (CM-ACC-003; Shopify's organization);
  - a membership in a store, with a role and its permissions, which may be narrowed further (Salla narrows its order permissions), and groups (CM-STF-003);
  - a partner's access to a store, requested and granted per store (CM-STF-005);
  - an app's grant of scopes per store, with its tokens;
  - partners and their organizations;
  - buyers' accounts, and business buyers with company roles (CM-B2B-002);
  - the verification of the people and business behind a store (CM-TRU-002, CM-PAY-003).
- **Flows and states:**
  - sign-up, invitation and acceptance, two-step sign-in;
  - sessions and tokens that expire or are revoked;
  - transfer of ownership (Salla's `store.owner.changed`);
  - a partner's request for access, and its approval;
  - an app's install, a change of scope, and uninstall with its data deletion;
  - verification: submitted, pending, approved, rejected, expired.
- **Rules:**
  - least privilege;
  - permissions that depend on others (Zid lists what each one relies on);
  - permissions a plan restricts (Zid);
  - the owner can't be removed.
- **Qualities,** each measure an assumption:
  - a removed role stops working within a minute;
  - every admin operation passes a permission check;
  - audit entries are kept for at least a year. Shopify shows 30 days of API activity (`SH-E-da68e961`), and Salla's tokens are valid for 14 days (`SA-E-35a61e11`).
- **What varies:**
  - by market: who verifies the owner, with which documents, which calendar the dates use, and how buyers get their codes;
  - by plan: how many staff accounts (Shopify "Up to 5", "Up to 15"; Zid one, 5 or 20 more people);
  - by store: its own roles.
- **The law** *(readings, for S-07):*
  - rules on knowing the seller, wherever the platform or its provider must verify one;
  - consent to personal data;
  - a minimum age for a payment account (Shopify's 18, `SH-C-063/decides/SH-S-0326`).

**What the model holds:**
- **Permissions in depth on three platforms:**
  - Shopify: its 124 assignable permissions, 20 of its 27 roles and its permission tree;
  - Salla: its 16 permission groups, staff roles and restrictions, 24 app scope areas, and 15 groups of partner access;
  - Zid: 215 permissions, each with what it relies on and the plans that restrict it (`store-permissions`, read by the held pass).

  Shopify's app scopes come to 419 by landing.
- **Buyers' sign-in:**
  - Salla: a 4-digit code (`auth.otp.verification`) and WhatsApp verification;
  - Zid: WhatsApp sign-in;
  - Shopify: an email one-time code (CM-CUS-010, CM-CUS-013).
- **Verifying sellers:**
  - Salla: an SMS from Absher, and its verification workflow (`kyc-schema`);
  - Zid: Nafath, with three attempts a day (`ZD-C-038/decides/ZD-S-0776`);
  - Shopify: its own profile assessment.
- **Data and events are thin.** For staff roles (CM-STF-002), the model holds one identifier on Shopify and one on WooCommerce. A person, a membership and a grant are named, never shaped.
- **Qualities:**
  - Zid signs a member out after 30 minutes idle at security level High (`ZD-C-095/decides/ZD-S-0945`);
  - Salla's 14-day token, and Shopify's 365-day buyer sessions.

  The rest are staff counts per plan, which are plan terms.
- **The registers:**
  - S-01: an account a seller requests through Sharrwah but holds under its own agreement with the provider counts as C (S01-D1.1);
  - S-02: leaves to the build who may change a store's country (S02-F4).

**Gaps:**

| Gap | Kind | Where, or why not | Answered by |
| --- | --- | --- | --- |
| The shape of the identity records: person, account, organization, membership, grant | Held, not read (Shopify, Salla); not held (Zid) | Shopify: `structures/shopify/admin-graphql-schema/2026-10/items.jsonl`, types `StaffMember` (14 fields) and `AccessScope`, and the `account-organization` structure. Salla: `docs-dataschemas`. Zid: its dashboard's API calls are "backlogged" (`zid/structures/REGISTER.tsv`) | A decision pack. No subject |
| Session, token and revocation rules | Mostly held, not read | shopify.dev (8,868 of 8,871 pages captured), docs.salla.dev, and Zid's 75 developer pages held in this repository (`evidence/product-class/runs/`) | The qualities pass (identity kind) |
| Who verifies sellers in each market, and with what | No platform can tell, beyond Salla's and Zid's Saudi flows | Market practice and law | S-07; S-04 for providers' own checks (S02-M2) |
| Dates in a calendar | **Held, not read** | observed-sa@`b0bd0b163`, `structures/salla/help-articles/en/texts.jsonl`, line 1224: "Date of birth (Hijri for Saudi citizens, Gregorian for residents)." Salla's workflow-renderer code picks `hijri` or `gregorian` (run `20261008T115555Z-dashboard-bundles`). Not in the model at all | S-07 for its values; D2 keeps a calendar on dates |
| How long Salla and Zid keep audit logs | Not held in the model | | The qualities pass (audit kind) |
| Business buyers on Salla and Zid (CM-B2B-002) | Searched, nothing placed | | The second stage |
| One identity across regions | Sharrwah's choice | It follows D1 | D1, after S-08 |

**Verdict: can be decided now with named gaps kept open.** Seller verification is a slot per market (S-07), and the region that identities live in follows D1. The permission catalogues are deep enough for roles; practice supplies the rest.

**The regional test:**
- **Whose shape:**
  - 16 of the 26 names use Shopify's and Salla's terms;
  - five count only for the global platforms: TRU-004, CUS-011, B2B-002, API-004 and API-013, each because Salla and Zid hold nothing or no placement;
  - one counts only for the regional ones: CUS-013, WhatsApp codes;
  - Salla's evidence rows are 63% of Shopify's, and Zid's 11%.
- **Where practice differs:**
  - Saudi sellers are verified through the state (Absher, Nafath), with a 10-digit national ID and a Hijri birth date for citizens. Shopify runs its own assessment;
  - Salla's and Zid's buyers sign in with a code by phone or WhatsApp; Shopify's by email;
  - in Kuwait, Salla's verification asks for the beneficial owners (`SA-S-0138`).
- **What it would change:**
  - a phone number must be a first-class sign-in, beside email;
  - the code's channel and sender must be slots per market. CM-NTF-004's slot fillers include the communications regulator *(a reading)*;
  - verifying the owner must be a slot that each market's state identity provider fills;
  - dates in identity records must carry their calendar.

  An identity built on Shopify's shape (email first, the platform's own assessment) would need rework for Saudi Arabia.

## D3. Money records and currency

**What it needs** (practice; each item a reading):
- **Entities:**
  - an amount: a value in the currency's smallest unit, with its currency entry (the architecture plan, section 7);
  - the currency table: each currency's code, its decimal places, its rounding and its cash rounding. ISO 4217 gives three decimals to the Kuwaiti, Bahraini, Jordanian, Omani, Tunisian, Libyan and Iraqi currencies *(a reading of the standard)*;
  - the exchange rates used, and prices per market;
  - the order's money: lines, discounts, shipping, tax, duties, tips and fees, kept in both the buyer's and the store's currency, with the market and rate (S02-D7);
  - payment records (authorisation, capture, sale, void, refund), each with its provider's reference and state;
  - refunds and returns;
  - store credit and gift cards: what the store owes its buyers;
  - invoices and credit notes, in a numbered series per business entity, with their tax lines;
  - Sharrwah's own bills, in a part of their own (S01-E3). Under C, no ledger of held balances (S01-E2).
- **Flows and states:**
  - an order's payment state: Shopify has eight, held (below);
  - a transaction's kind and status;
  - cash on delivery, from the order to the courier's settlement;
  - a bank transfer, from the order to its confirmation;
  - instalments, which the provider pays;
  - an invoice, from issue to the authority's acceptance;
  - a refund, back to its method.
- **Rules:**
  - money is never changed in place: a correction is a new record (a credit note, an adjustment or a refund);
  - totals equal their lines, rounded by a stated rule. Shopify rounds per line; WooCommerce lets the merchant choose;
  - the provider's record is the truth for what it holds *(a reading of S01-E2)*;
  - no amount without its currency entry.
- **Qualities,** each measure an assumption:
  - every order's paid amount equals the sum of its successful transactions, checked daily;
  - each payment event takes effect once;
  - invoice numbers have no gaps in a series;
  - each e-invoice is reported within the authority's time.
- **What varies:**
  - by market: currencies and their decimals, cash rounding, e-invoicing, tax-inclusive prices and payment methods;
  - by store: its currency (S02-E4).
- **The law** *(readings, for S-05):*
  - Saudi Arabia's e-invoicing (ZATCA's Fatoora, whose second phase integrates each invoice with the authority);
  - Egypt's e-invoice and e-receipt, Jordan's national e-invoicing, and the UAE's planned e-invoicing;
  - how many years records must be kept;
  - VAT on Sharrwah's own fees (CM-PLN-007).

**What the model holds:**
- **Wide coverage, and the region is well represented:** of the 35 capabilities, Salla places 31 and Zid 30.
- **Names of money fields:**
  - Shopify's `Shop.currencyCode`;
  - Zid's `order_currency.exchange_rate`, "the rate applied to the order currency relative to the store currency" (`ZD-S-0811`);
  - BigCommerce's settlement and transactional currency;
  - Salla's currency API folders, and its flag `reflect-market-currency`.
- **Deciding statements:**
  - Salla's payouts by country: in the UAE every Thursday above 250 dirhams; in Kuwait the next working day, with at least one dinar;
  - Shopify's 7-day authorisation and 15-minute void window;
  - Zid's 30-day refund limit;
  - Salla allows one edit per order.
- **Not in the model: the shapes.**
  - Shopify gives every money field two amounts (`MoneyBag`: `shopMoney` and `presentmentMoney`; `MoneyV2`: `amount` and `currencyCode`). Its order has 8 payment states, and its transactions 8 kinds and 6 statuses. All of this is in observed-sh@`04de369da`, `structures/shopify/admin-graphql-schema/2026-10/items.jsonl`, unread: the held pass leaves "the admin API's types" out as "detail" (`held/selection.tsv`).
  - Salla's amounts are `{amount, currency}` pairs. The amount is an integer in the order's `amounts.sub_total` (schema `1698878`) and a number in `total` (schema `3632422`), in observed-sa@`b0bd0b163`, `structures/salla/docs-dataschemas/definitions/items.jsonl`, unread ("the API's data schemas: detail").
- **Rounding and decimals:** a few Shopify changelog rows (rounding per line; cash rounding) and WooCommerce's tax-rounding setting. Nothing on three-decimal currencies.
- **The registers:**
  - S-01: Decision 1 and its defaults, and E1 to E4;
  - S-02: D7 (both currencies on every order), D9 and E4;
  - the architecture plan's section 7: every amount points to a currency entry, for your veto at GM.

**Gaps:**

| Gap | Kind | Where, or why not | Answered by |
| --- | --- | --- | --- |
| The shapes of amounts, totals, transactions, refunds and their states | **Held, not read** | The Shopify and Salla files above; the WooCommerce release's order and refund code (`/home/user/woocommerce-release/11.2.1`); Zid's 75 developer pages held here (among them orders, events and order credit notes); BigCommerce's API pages | A decision pack, before D3 |
| The invoice record, and the rules for sending it to the authority | Existence held (Salla, Zid); the rules are law | CM-TAX-007 is held only through them. Salla uploads invoices once the merchant enters a code granting it the authority (`SA-S-0152`). Zid links the store to Fatoora (`ZD-S-0827` to `0830`). Shopify's cell is not-stated | S-05 |
| Decimal places, rounding and cash rounding per currency | Partly held (Shopify, WooCommerce); the rest is a standard | ISO 4217 | S-09 for the values; D3 for the field |
| The payment record under C: the provider's fields, and how it is reconciled | Partly held | CM-PAY-020's cells; the providers' own documents aren't held | S-04 |
| Cash on delivery, from collection to settlement | Held (Salla, Zid) | CM-PAY-029 | S-10 |
| Sharrwah's own bills and their tax | Held | CM-PLN-004, CM-PLN-007 | S-11, S-05 |
| Which currencies, and areas within a code | | | S-09 |

**Verdict: can't be decided yet.** The model says every platform keeps orders, payments, refunds, invoices and currencies. It holds almost nothing of their shapes, states or rules, which are what this decision chooses between. Three things would let it be decided:
1. a decision pack reading the held shapes at their commits, for at least Shopify, Salla, Zid and WooCommerce (the files named above);
2. S-05's reading of e-invoicing in the markets where it binds, before the invoice record is accepted;
3. S-04's provider fields, before the payment record is accepted.

Three rulings already stand and needn't wait:
- the currency entry (section 7), unless you veto it;
- both currencies on every order (S02-D7);
- one payment record whoever holds the money, and no ledger of held balances under C (S01-E2).

**The regional test:**
- **Whose shape:**
  - 26 of the 35 names use Shopify's and Salla's terms;
  - three count only for the global platforms (PAY-008, TAX-005 and POS-003), all thin on Salla and Zid;
  - three count only for the regional ones: PAY-031 (amounts withheld from the merchant's wallet for app partners), TAX-007 (e-invoicing) and PLN-006 (a prepaid store balance);
  - Salla's evidence rows are 48% of Shopify's, and Zid's 25%.
- **Where practice differs:**
  - Sending invoices to the tax authority is the regional platforms' alone.
  - Salla sets cash on delivery per courier, with its own fee (CM-PAY-029). Under Zid's own shipping, "Zid collects the amount from the customer on delivery and transfers it" to the merchant's wallet (`ZD-C-015/responsible/ZD-S-0641`, `ZD-C-015/where/ZD-S-0636`). That is an arrangement your Decision 1 rules out at launch: under C, the courier holds it. Shopify gives cash on delivery no place of its own (its cell is not-stated).
  - Zid's payment service shows prices in the buyer's currency and takes payment in the store's, except KNET in dinars (`ZD-C-050/decides/ZD-S-0808`). Where the store's, the order's and the delivery address's currencies differ, partners must convert the order total (`ZD-S-0812`).
  - Bank transfer is a method of its own on Salla and Zid. Salla offers Saudi instant payments (Sarie) on a plan.
- **What it would change:**
  - collection by a courier, with its fee and the courier's settlement, must be a first-class path of the payment record, not a manual note;
  - an invoice must be a document of its own: fixed once issued, corrected by credit notes, numbered in a series per business entity, with a place for the authority's answer;
  - the currency table must carry decimal places.

  A money record built on Shopify's shape would need rework on all three *(a reading)*.

## D4. Markets and the seller's country

**What it needs** (practice; each item a reading):
- **Entities:**
  - the business entity behind a store: its country, its legal form, and its registrations (commercial register, VAT number, freelance document). One per store at launch, with more allowed (S02-D1);
  - the contracting company in each market (S-03);
  - markets as typed sets of conditions (places, channels, points of sale, business buyers), which may nest (S02-D4, S02-D5);
  - the store's default market (S02-E3);
  - reference data: countries, cities and districts (CM-MKS-009), address forms (CM-CUS-008), languages and their direction, and currencies;
  - the countries served (S-07).
- **Flows:**
  - sign-up with a country (CM-ONB-001);
  - a seller's move to another country, which adds a new entity rather than changing one (S02-D2);
  - Sharrwah setting up a market: its providers, its law and its defaults.
- **Rules:**
  - every rule keyed on the seller's country reads the business entity's country, through one interface (S02-E2);
  - the buyer's market is matched from their context (S02-D4).
- **Qualities** (an assumption): a new market is set up by settings and slot fillers, with no change to the core. This is the regional-fit scenario of the plan's section 5.
- **What varies:**
  - by market: all of the above;
  - by plan: how many markets a store may have (S02-M9, yours);
  - by store: its own markets.
- **The law** *(readings, for S-03 and S-07):* each market's company, consumer, e-commerce and tax law, and who may contract with sellers there.

**What the model holds:**
- **Capabilities placed:** of the 22, Shopify places 20, Salla 20, Zid 16, WooCommerce 13 and BigCommerce 9.
- **S-02's register is the deepest work on any of the six:** 9 rulings, 5 engineering constraints and 9 moves to later subjects. Its points and S-01's (98 in all) landed on 101 capabilities (`studies/class-model/points/`).
- **The business entity (CM-ACC-004):** Shopify has 44 evidence rows, Zid 19 and Salla 2.
- **The contracting company (CM-ACC-002):** every platform's cell holds statements, but none states where the platform puts it.
- **Limits:** Salla allows 10 countries in its markets (`SA-E-706d44d1`), and Zid 5 active markets (`ZD-E-81f83cbc`).

**Gaps:**

| Gap | Kind | Where, or why not | Answered by |
| --- | --- | --- | --- |
| The contracting company and its law, per market | Held but unplaced. The choice is yours | The ACC-002 cells. S2-ZD-1, checked but not landed, finds Zid's operator by its commercial registration number, and its terms under Saudi law (`other-product-class@0d79b794f`, run `20261028T190806Z-terms-pricing-sa-eg`). BigCommerce's `contracting-entities` holds 5 of its page's 7 rows | S-03 |
| The countries served, and those kept out | Partly held | S02-VP-02, S02-VP-03 | S-07 |
| Address forms, and number and date formats, per country | **Held, not read:** "market data, the subjects'" | BigCommerce's `standard-formats` (245 countries); WooCommerce's `countries-states` (250); Salla's `dashboard-countries` (242). Shopify's checkout address form is requested in H-008 | Each market's setup; S-10 for delivery addresses *(a reading)* |
| North Africa and the Levant | Not held by any regional reference | No cell's scope names Morocco, Algeria, Tunisia, Jordan or Lebanon (by a pattern, a reading) | Each market's setup; S-03, S-07 |
| Salla's business entity | Thin: 2 rows | | The second stage |

**Verdict: can be decided now with named gaps kept open.** S-02 decided most of it. The company (S-03) and the countries served (S-07) are values behind S02-E2's interface.

**The regional test:**
- **Whose shape:**
  - 19 of the 22 names use both Shopify's and Salla's terms;
  - two count only for the global platforms: ACC-005 (several business entities), thin on Salla and Zid, and MKS-003 (a merchant of record), which Salla leaves to an extension point, a real difference;
  - one counts only for the regional ones: ACC-008 (the countries where the platform offers its service), core on Salla;
  - Salla's evidence rows are 32% of Shopify's, and Zid's 19%.
- **Where practice differs:**
  - Salla allows one country per market for tax (`SA-E-ab1789cb`), which S-02 noted as a Saudi-shaped constraint (D5);
  - Salla's "store seat" is held on the business record (S02-D1);
  - the regional platforms serve the Gulf, and Egypt only on Zid's side (`zid.eg`).
- **What it would change:** nothing in S-02's shape. The gap is that your North African and Levant markets have no regional reference, so setting them up will rest on the global platforms and on law *(a reading)*.

## D5. Events and extension points

**What it needs** (practice; each item a reading):
- **Entities:**
  - an event: its topic, its record, its version, an id to drop duplicates, and when it happened;
  - a subscription by an app or a merchant, per store, with conditions (Salla's conditional webhooks), and its delivery attempts;
  - app installations and grants (D2);
  - extension points: functions the platform calls and waits on (Shopify's Functions, Salla's App Functions), and app screens in the admin, the checkout, the storefront, point of sale and buyers' accounts;
  - a contract for each slot: payments, couriers, tax and e-invoicing, messages, identity checks and maps.
- **Flows and states:**
  - delivery and retry, and shutting off a subscription after repeated failure (BigCommerce does so after its final retry, 48 hours on: `BC-C-058/decides/BC-S-0318`);
  - an app's install, scope change and uninstall, with its privacy requests (CM-API-011);
  - a call to a provider, with its time limit and its fallback. Salla gives an order to the next courier in priority when the first doesn't deliver to the area (`SA-S-0162`).
- **Rules:**
  - events are delivered at least once, possibly out of order, and signed: Shopify with HMAC, Salla with a token or signature, WooCommerce with a signature header;
  - versions change with notice;
  - a function has a time and size budget;
  - an app sees only what it was granted;
  - a provider's failure never loses an order.
- **Qualities,** each measure an assumption:
  - 95% of events delivered within 5 seconds;
  - retries for at least 48 hours;
  - an hour's provider outage loses no order;
  - API limits by plan.
- **What varies:**
  - by market: which providers fill each slot;
  - by plan: limits, and which extensions are allowed;
  - by store: its apps.
- **The law** *(readings):*
  - a provider's licence (S-06);
  - what apps may do with data (S-08);
  - the communications regulator's rules for SMS senders. CM-NTF-004's slot fillers name هيئة الاتصالات.

**What the model holds:**
- **Capabilities placed:** of the 34, Shopify places 32, Salla 26, Zid 19, WooCommerce 26 and BigCommerce 20.
- **Event names,** counted as identifiers shaped like topics *(a reading)*: Salla 127, across 56 capabilities; Shopify 70, besides the CLI's list of 230 topics, which is cited; WooCommerce 36; BigCommerce 34; Zid 13.
- **Salla's webhooks are the most deeply read** of the five: 70 data and event rows on CM-API-008, against Shopify's 2, and 36 on conditional webhooks (CM-API-010). Its App Functions have 63 rows exact and 76 by landing.
- **Slot fillers:**
  - payments: Salla's HyperPay, Moyasar and Tap; Zid's Paymob, Tap and amwal pay;
  - instalments: Tabby, Tamara, Emkan, Madfu, MIS pay and Deema;
  - couriers: 45 for Salla, among them Aramex, Aymakan, J&T and Mrsool;
  - messages: Unifonic and WhatsApp Business (Zid);
  - identity checks: Absher and Nafath;
  - e-invoicing: ZATCA.
- **Delivery rules:** a handful of rows: Shopify 4, Salla 3, WooCommerce 1, BigCommerce 1.

**Gaps:**

| Gap | Kind | Where, or why not | Answered by |
| --- | --- | --- | --- |
| What an event carries | **Held, not read** | Shopify's `webhook-sample-payloads` (210) and `webhook-deliveries-cli` (230): "payload detail" (`held/selection.tsv`). Salla's `app-webhook-deliveries` (16) and data schemas. Zid's developer pages held here. WooCommerce's code | A decision pack |
| Delivery rules: retries, order, duplicates, signatures | Mostly held, not read | shopify.dev and docs.salla.dev, both captured | The qualities pass (interface bounds) or a decision pack |
| The provider contracts: a payment's session, capture and refund; a courier's rates, labels, tracking and cash settlement | Partly held: Shopify's payments-apps schema in `dev-mcp-schemas` ("detail"), and Salla's shipping-app docs. The region's providers' own APIs aren't held | | S-04, S-10 |
| What happens when a provider fails | Thin | Salla's next courier (above) | S-04, S-10 |
| Function budgets | Held, not read | shopify.dev | A decision pack |

**Verdict: can be decided now with named gaps kept open.** The general mechanism comes from practice and from the class's event catalogues: events, subscriptions, grants, versions and functions. The payment and courier contracts wait for S-04 and S-10. What each event carries follows each part's records.

**The regional test:**
- **Whose shape:** 20 of the 34 names use both platforms' terms, and 9 Shopify's alone. Eight count only for the global platforms:
  - four are real differences: Salla leaves storefront app extensions, workflow automation and outside analytics to apps (SFR-004, AUT-001, ANL-007), and Zid leaves tax services to apps (TAX-004);
  - four are too thin to tell: API-007, CHK-005, SHP-004 and SHP-013.

  One counts only for the regional ones: API-010, conditional webhooks. Salla's evidence rows are 42% of Shopify's, and Zid's 11%.
- **Where practice differs:**
  - Salla's events can carry conditions, and its App Functions mirror Shopify's Functions;
  - the regional platforms leave more to apps on automation and analytics;
  - their slots are filled by regional providers: card schemes and wallets, instalment companies, local couriers, messaging services, state identity providers and the tax authority. Slot fillers carry no market (the plan, section 1).
- **What it would change:** the slot contracts must take the region's providers as first-class:
  - a courier that collects cash and settles it;
  - a tax authority that accepts or rejects an invoice;
  - a state identity provider.

  Shopify's payment and carrier apps aren't enough on their own as the template *(a reading)*.

## D6. Configuration: a setting held for a store, varied per market and limited per plan

**What it needs** (practice; each item a reading):
- **Entities:**
  - each setting declared once, with:
    - its key and its type;
    - one value or a set (S02-E1);
    - its levels: the platform's default, Sharrwah's setup of a market, the store, the store's market, a group of customers;
    - when it is fixed: at build, at a market's setup, or by the store;
    - its default, and who may change it;
  - entitlements per store (a feature, on or off, with a limit), from its plan, add-ons, trials and exceptions;
  - feature switches and staged rollouts (CM-EVO-001, CM-MKS-002);
  - app settings and custom data (CM-APP-010, CM-CNT-002).
- **Flows:**
  - a change, its audit, and how it spreads;
  - a change of plan, and its effect: a downgrade below what the store already uses;
  - export and import of a configuration (CM-MIG-006), and a staging copy (CM-DVT-006).
- **Rules:** one-value settings take the most specific value; sets may combine across markets; a limit the platform or a law sets applies after values resolve (S02-E1).
- **Qualities,** each measure an assumption:
  - a change reaches every read within 30 seconds;
  - each setting's resolution is tested;
  - a change of entitlement needs no release.
- **What varies:**
  - by market: defaults, and limits set by law;
  - by plan: entitlements;
  - by store: its own values.

**What the model holds:**
- **Capabilities placed:** of the 18, Shopify places 14, Salla 12, Zid 9, WooCommerce 11 and BigCommerce 10.
- **S-02 decided** how a per-market setting is read: D6, E1, E3 and E4.
- **Plan limits are held in their own shape on three platforms:**
  - Shopify's entitlements per store: `entitlements.markets.b2b.catalogs` holds `{"enabled": true, "limit": 3}` (`SH-C-037/decides/SH-S-5532`);
  - Zid's 633 plan policies, each a key, enabled or not, a config of limits, and the plan it is available in (other-product-class@`0d79b794f`, `zid/structures/store-plan-policies/items.jsonl`);
  - Salla's plan gates per route.
- **Settings catalogues the held pass read:** Salla's settings centre, WooCommerce's options, BigCommerce's settings list and Shopify's settings navigation.
- **Qualities:** 1,408 rows on these capabilities are Shopify's prices and allowances.

**Gaps:**

| Gap | Kind | Where, or why not | Answered by |
| --- | --- | --- | --- |
| Each setting's levels, and when it is fixed | Not recorded. Scopes are free text: 789 of 1,835 cells carry one, untyped | | Engineering, as it designs |
| Each plan's limits, and what Sharrwah charges | No platform can tell: they are your plans and prices | | S-11, and you |
| Feature switches on Salla and Zid | Held, and cited on other capabilities (Salla's `dashboard-features`, Zid's `store-feature-flags`). EVO-001's Salla and Zid cells hold nothing | | The second stage |
| Configuration export and staging, on Salla and Zid | Searched, nothing placed | | The second stage |

**Verdict: can be decided now with named gaps kept open:** the plans' values (S-11, and your plans and prices).

**The regional test:**
- **Whose shape:**
  - 7 of the 18 names use both platforms' terms, and 4 use WooCommerce's alone;
  - six count only for the global platforms (ACC-009, EVO-001, PLN-003, MIG-006, DVT-006, CHK-003), all thin on Salla and Zid;
  - two count only for the regional ones: ACC-007 (maintenance mode) and ORD-010 (whether, when and how many orders the store accepts);
  - Salla's evidence rows are 27% of Shopify's, and Zid's 6%. That is the lowest of the six, because Shopify's prices fill these capabilities.
- **Where practice differs:** Salla and Zid limit by plan the way Shopify does, with a key, a plan and a limit. Nothing there changes the decision *(a reading)*. A store's switch to stop or limit taking orders is regional, and belongs among the store's settings.

## Across the six

### Which subjects bind which decisions

What each subject, not yet run, would fill in each decision. This adds to the plan's own table in section 3: a reading of each subject's question in `studies/subjects/subjects.tsv`, and of S-02's moves (S02-M1 to S02-M9).

| Subject | D1 | D2 | D3 | D4 | D5 | D6 |
| --- | --- | --- | --- | --- | --- | --- |
| S-03, the contracting company | who controls the data in each market | the party to a seller's account | who issues Sharrwah's own bills | the company per market (a place is kept) | | |
| S-04, payment providers under C | whose form takes card data | the providers' own checks of the business | the payment record's provider fields | which providers take which sellers' countries | the payment contract, and what a failure does | |
| S-05, tax and invoicing | how long invoices are kept | VAT registration as identity | invoices, credit notes, tax lines, e-invoicing | tax registrations per entity or area | the tax and e-invoicing slots | |
| S-06, licences | | | | which activities need a licence in a market | which providers must be licensed | |
| S-07, verification, screening, countries | the countries served | who verifies sellers, and screening | | the countries served | the verification and screening slots | |
| S-08, where data lives | **where data lives, by law; retention after closing** | which region identities live in | how long records are kept | the law per country | where apps and providers may process data | |
| S-09, currency of records | | | which currencies and areas fill the table | currencies per market | | |
| S-10, delivery and cash on delivery | | | cash collection and the courier's settlement | | the courier contract, and what a failure does | |
| S-11, what Sharrwah charges | | | Sharrwah's own bills | | | the plans' limits (your prices) |

**What must run before a first decision is accepted, so it isn't rework:**
- D1 needs S-08 (and S-03, for who controls the data).
- D3 needs S-05 for its invoice record, and S-04 for its payment record.
- D5's slots need S-04 and S-10.
- D2's verification slot needs S-07.
- D4 and D6 only take values: S-03 and S-07 for D4, S-11 for D6.
- S-09 fills the table that section 7 creates, unless you veto section 7: then S-09 must run before D3.
- Under C, S-06 binds none of the six *(a reading)*. It binds any part that runs a regulated activity.

**The order I propose,** which is yours to decide:

| Order | Subject | Why it is there | In the list's order |
| --- | --- | --- | --- |
| 1 | S-03 | the company is yours, and the design only keeps a place for it | 1 |
| 2 | **S-08** | D1 is the costliest decision to change, and D2 follows it | 6 |
| 3 | S-04 | under C, the providers are the money's path: D3's payment record and D5's payment contract | 2 |
| 4 | S-05 | D3's invoice record and e-invoicing | 3 |
| 5 | **S-10** | cash on delivery is a payment path under C: D3, and D5's courier contract | 8 |
| 6 | S-07 | D2's verification slot, and D4's countries served | 5 |
| 7 | S-09 | values only, once the currency entry stands | 7 |
| 8 | S-11 | D6's values; plans and prices are yours | 9 |
| 9 | S-06 | binds no first decision under C | 4 |

### Where the remaining model work should point, and what it should stop

The remaining work (`STATE.md`, "The path to GM") is the second stage, the qualities pass, the omission review and the final review. **None of the three briefs for the second stage, the omission review and the final review mentions architecture or its first decisions** (`studies/class-model/briefs/S2-held.md`, `O-omission.md`, `R-extent.md`, searched for "architect", "first decision" and "priorit"). The qualities pass's design does map its kinds onto D1 to D6 (`QL-qualities-design.md`, section 3).

**The second stage.** Of the 705 empty or unplaced cells, 234 sit on the 146 capabilities these decisions rest on: Shopify 16, Salla 35, Zid 54, WooCommerce 64 and BigCommerce 65. The other 471 bear on none of them. S2-ZD-1 spent 59.3 million tokens on 72 cells (`studies/class-model/method-report.md` at `d0fb7f82`), about 0.8 million a cell *(a reading of that measure)*. At that rate, the 633 cells left would cost about 520 million, against the step's estimate of 115 to 285 million *(a reading)*. S2-ZD-1 covers 6 of Zid's cells on these capabilities, and all 7 of its rows there found something. So the region's empty cells here are more likely thinly read than truly empty *(a reading, from six cells)*.
- **Point it** at Salla's 35 and Zid's 48 remaining cells on these capabilities first, then Shopify's 16: about 100 cells, roughly 80 million at the measured rate *(a reading)*.
- **Leave** WooCommerce's and BigCommerce's 129, and the 471 others, until after GM. Each part's design reads its capabilities in depth then anyway (the architecture plan, section 1).

**The qualities pass.** Run it, narrowed to the kinds the first decisions read, by its own table:
- isolation, where data lives, subprocessors, retention, encryption, availability, capacity, attestations, privacy, identity, audit, interface bounds, change, and stability;
- Salla first, as designed, with observed-sa's log of storage regions and the privacy policy's lines on Saudi law; then Zid; then Shopify's compliance reports and legal documents.

Leave support and accessibility, which only section 5's scenarios read, until after the first decisions. Stop at relabelling the plan terms by script.

**The omission review.** It asks whether the model lacks a capability, or a cell holds nothing where something is held. That measures breadth, and these decisions need depth.
- **Replace it before GM** with decision packs for D2, D3 and D5: the identity records, the money records and their states, what events carry, and the delivery rules. Each is read from the held files named in the gap tables above, cited at a commit, from at least two platforms, one of them Salla or Zid where held.
- **Keep the omission review** for after GM, sampled part by part as each part is designed.

**The final review.** Weight its sample toward the 146 capabilities, and toward Salla's and Zid's cells on them, with the high-weight rulings that place lines on them first. A ruling that places lines only elsewhere can be reviewed when its part is designed.

**Stop:**
1. adding capabilities before architecture starts: the 367 are enough as an index *(a reading)*;
2. reading prices and plan allowances as qualities. Relabel them by script, and leave Shopify's 61 country price sites to S-11;
3. treating schemas, payloads, terms and engineering writing as out-of-scope detail for the first decisions (the reasons recorded in `held/selection.tsv`). They needn't enter the model: a decision pack reads them;
4. counting how many platforms do a thing as if it decided anything. The count says who does it, never how;
5. running the second stage's eight remaining parts in full before GM.

### The test for "enough to start architecture"

Eight checks, one set per first decision. Each can be counted from the files.

| Check | What passes | Today |
| --- | --- | --- |
| E1. The list | The decision's capability list is written and reviewed by an agent that made neither the list nor the model | Proposed in this file's appendix; not reviewed |
| E2. The region's cells | Every Salla and Zid cell on the list is placed, or shows a second-stage search of the held pages at a commit, not only the concern map's search | 89 cells fail (Salla 35, Zid 54). S2-ZD-1, not landed, covers 6 |
| E3. Shapes | Every object on the decision's list has its fields cited at a commit from two or more platforms, one of them Salla or Zid where held. Where nothing is held, a capture request names it | Fails for D2, D3 and D5: the model holds names only. D4 passes through S-02's register *(a reading)*. D6 passes for plan limits (Shopify, Zid, Salla) |
| E4. States | Every flow on the decision's list has its states cited from two or more platforms | Fails for D3 (payment states held for Shopify, unread), D5 (delivery attempts) and D2 (verification: Salla's read, Zid's partly) |
| E5. Qualities | For every kind the decision reads (the qualities pass's table), each platform has a row: found and quoted at a commit, not found after reading its guides, or not published | Fails everywhere: the pass hasn't run |
| E6. Subjects | Each binding subject has run, or the decision names its variation point with when it is fixed, the cheapest step and its check (the plan's section 4). Where a subject could force rework (S-08 for D1, S-05 for D3), it has run before the decision is accepted | No drafts exist yet. S-08 and S-05 haven't run |
| E7. Your decisions | The decision's record lists every row of `founder-decisions.tsv` that binds it, and contradicts none | Not yet applicable. The rows that bind are named in each section above |
| E8. Scale and scenarios | The scale bands and the tree of quality scenarios exist, each measure marked as an assumption (the plan's section 5) | Not written |

- **Enough to start architecture:** E1, E2, E7 and E8 hold for all six decisions; E3 to E5 hold for whichever decision is designed first.
- **Enough to accept a decision:** E1 to E8 hold for that decision.

By today's measures, D4 and D6 could start once E1, E2 and E8 pass. D2 and D5 need their decision packs, which take E3 and E4. D1 needs the qualities pass on isolation and location, and S-08 before acceptance. D3 needs its decision pack and S-05.

## Appendix: the capabilities each decision rests on

My reading. Prefix each id with `CM-`.

- **D1 (26):** ACC-001, ACC-003, ACC-006, ONB-002, TRU-005, TRU-007, TRU-008, TRU-013, TRU-014, TRU-015, TRU-016, TRU-017, TRU-018, TRU-021, OPS-001, OPS-002, OPS-003, OPS-006, API-004, API-005, API-011, MIG-001, MIG-006, DVT-006, SFR-008, CHN-007.
- **D2 (26):** ACC-001, ACC-003, STF-001, STF-002, STF-003, STF-005, TRU-001, TRU-002, TRU-003, TRU-004, CUS-010, CUS-011, CUS-012, CUS-013, B2B-002, API-002, API-003, API-004, API-013, APP-009, PTN-001, PTN-002, DVT-003, PAY-003, AIA-004, PTN-010.
- **D3 (35):** MKS-005, MKS-006, MKS-007, ORD-001, ORD-002, ORD-003, ORD-015, PAY-020, PAY-016, PAY-029, PAY-030, PAY-015, PAY-008, PAY-005, PAY-007, PAY-009, PAY-031, RET-001, RET-002, LOY-001, LOY-002, TAX-001, TAX-005, TAX-007, TAX-008, ORD-008, PLN-004, PLN-005, PLN-006, PLN-007, APP-003, PTN-003, PAY-028, POS-003, B2B-003.
- **D4 (22):** ACC-002, ACC-004, ACC-005, ACC-008, ONB-001, MKS-001, MKS-002, MKS-003, MKS-004, MKS-008, MKS-009, TAX-003, SHP-001, CUS-008, CUS-009, PAY-017, PAY-001, PAY-002, TRU-010, CNT-008, SRF-003, TRU-009.
- **D5 (34):** API-001, API-002, API-003, API-005, API-006, API-007, API-008, API-009, API-010, APP-001, APP-003, APP-004, APP-005, APP-006, APP-007, APP-008, APP-010, CHK-004, CHK-005, CHK-006, PAY-011, PAY-019, SHP-004, SHP-011, SHP-013, SHP-015, TAX-004, NTF-004, SFR-004, AUT-001, CNT-002, SFR-012, OPS-007, ANL-007.
- **D6 (18):** ACC-006, ACC-007, ACC-009, EVO-001, PLN-001, PLN-002, PLN-003, MKS-001, MKS-002, CNT-002, APP-010, MIG-006, DVT-006, ORD-010, CHK-003, SFR-015, ONB-004, API-006.

**Across all 146:**
- **Names:** 89 use Shopify's and Salla's terms, 27 Shopify's alone, 15 Salla's alone, and 3 name Zid's.
- **Evidence rows:** Shopify 7,554, Salla 3,302 (44%), Zid 1,166 (15%).
- **Platforms that count:** 29 count for the global platforms but neither Salla nor Zid. Of those, 24 hold nothing or no placement for both, and 5 are real differences (AUT-001, SFR-004, MKS-003, TAX-004, ANL-007). Eight count for Salla or Zid alone.
