# S-02, the scenario walk (step 3, SW-1): notes

**What this is:** the scenario walk of `PLAN.md` section 6, step 7, done from the brief `briefs/F-scenario-walk.md`. Each of S-02's seven decisions for the founder (S02-D1 to S02-D7) and five engineering constraints (S02-E1 to S02-E5) goes through three scenarios: a second market, the company based elsewhere, and the first market dropped. The rows are in `scenario-walk.tsv`: 39 rows, 12 items × 3 scenarios, with two second-market rows for S02-D1 and S02-D3 and two company-elsewhere rows for S02-E2. The walk tests the recommendations. It chooses nothing.

## What was read

- The brief; `PLAN.md` section 1 and section 6, step 7; `founder-decisions.tsv`, the row of 28 October; `register.tsv` and `decisions.md`.
- Phase C's files: `c/RD1/`, `c/RD2/`, `c/RD3/` (`answers.tsv`, `points.tsv`).
- Statements by id, through `python3 -I method/subject_slice.py studies/subjects/S-02 --print RD<n> --ids ...`.
- Nine rows of `variants.tsv`, for the platform and statements behind a variant id: S02-V-153, 154, 186, 228, 229, 230, 649, 650 and 1048.
- **Not read:** S-01's register, Stage 1, Q2, and YR-1's `yemen-row.tsv`, which was being written at the same time. So A and B, the holding arrangements, are known here only from S02-R4's words ("A and B off under the guard").

## How to read the table

- **scenario:**
  - `second market`: a market whose conditions differ on the item's question;
  - `company elsewhere`: Sharrwah's company based in another country;
  - `first market dropped`.
- **market:**
  - named, where S-02's evidence shows that market's difference;
  - `hypothetical`, where the difference is a hypothesis, with an example market given in `what_changes`.
  - The first market is named in its rows as "Yemen (the first market)". Yemen's facts are not used.
- **cost:** each is a reading, engineering's. `a setting`, `one module` and `a redesign` are as the brief defines them. Where a cost holds only on a condition, the `note` names the condition.
- **closes / reason / flag:** a row flags `premature` when the item closes an option and none of the three reasons covers it: a confirmed fact, the founder's choice, or an engineering cost greater than the option's value. `one market`: no row needed it (see the findings).
- **evidence:**
  - statement ids (S02-SH-..., S02-SA-..., S02-ZD-..., S02-BC-..., S02-WC-...);
  - variant ids (S02-V-...);
  - phase C rows (`c/RD1/answers.tsv S02-VP-07`);
  - register rows (`register S02-D2`).

  A statement id resolves, through the slice script, to the statement's verbatim words and its first citation's source. The table at the end pins the sources behind the findings.
- **Marking:**
  - `Hypothesis:` marks an assumption about a market;
  - `Reading:` marks an interpretation;
  - `unknown` marks a fact S-02's evidence lacks.
- **Assumption:** "the company" in scenario 2 is Sharrwah's own company, as `PLAN.md` section 6, step 0 uses the word ("the product, the market context, or the company").

## Findings for the founder, most important first

### 1. A redesign behind a "setting": a second business that serves a market (S02-D1, S02-E2)

**The claim.** S02-D1 says that with the business record in place, "a second one is a setting". Its trade-off says that a market served through another business "needs no re-keying" of the rules that depend on the seller's country.

**What the walk finds.** As written, it is not a setting.
- S02-E2 and S02-D3 read every such rule through one interface "keyed on the store's business-entity country". That names one business.
- With two businesses, the rules applied to an order need to know whose order it is: payments, invoices and order attribution, the selling business's tax and checks. That interface can't say.
- Adding the order or the market later changes every part that asks for an order. Orders made before then need their business recorded. That is a change to several parts: a redesign (`scenario-walk.tsv`, the Egypt rows of S02-D1 and S02-E2).

**The evidence**, from Shopify, whose model S02-D1 follows:
- Market objects can be assigned to a business entity "to determine payment processing and Order attribution" (S02-SH-280).
- "Changing the business entity for a market affects only new orders. Existing orders continue to be associated with the business entity that was active when the order was placed" (S02-SH-147).
- One entity is still used "for financial products, markets, apps, and taxes in this shop" (S02-SH-318), and subscription payments go through the primary entity (S02-SH-1146).
- Reading: Shopify keeps two keys, the store's business and the order's business, and each rule uses one of them.

**Egypt shows why a second business is plausible.** Zid serves Egypt through a separate company with its own terms, its own fees in EGP with VAT, and its own privacy controller under Egypt's Law 151 of 2020 (S02-ZD-367, S02-ZD-371, S02-ZD-383, S02-ZD-384). Whether a seller would need an Egyptian business to sell in Egypt is unknown from S-02's evidence.

**What keeps it a setting** (reading). State three things now, at almost no cost:
1. The entry point takes the order or the market, as well as the store.
2. Each order records the business it was placed under.
3. Each rule says whether it reads the store's main business or the order's business.

S02-E5 already resolves per market ("where an entity is assigned to a market ... that entity's arrangement applies"). As worded, then, S02-E2 and S02-E5 disagree on the key.

### 2. Four options closed with no reason that covers them (`premature`)

**S02-D3, Saudi Arabia: a rule keyed on where the store or its stock is.**
- Zid's Jahez needs "the store's or the stock's location in one of the Kingdom's cities" (S02-ZD-120, S02-V-186).
- D3 closes "rules keyed on a country held apart from the entity". Its reason, "two countries for one seller can disagree", is argued for a second record of the seller's own country, such as the billing address or a feature's field.
- A stock location is a different fact. Hypothesis: a business registered in the UAE with stock in Riyadh meets Zid's condition but fails D3's key.
- Cost to keep it: one module (D3's own cost_later allows "one rule's own key").

**S02-D3, the UAE: a check keyed on an owner's residence, and a payment rule keyed on a provider account's country.**
- Salla's UAE verification asks a passport and Emirates ID per owner "If you are a UAE resident; if not use a national ID from the country you reside in" (S02-SA-134).
- BigCommerce keys Fastlane by PayPal on the store's, the provider account's and the shopper's countries (S02-BC-128). BigCommerce Payments needs "a UK or US-based PayPal Business account" (S02-BC-081).
- Under Decision 1 a provider account is the seller's own with the provider (S02-R4). Its country is the provider's record, which Sharrwah doesn't keep.
- S02-E5 itself chooses "among the seller's provider accounts allowed there", which D3's closure as worded forbids.
- Cost to keep it: one module each (S-07's checks; S-04's rules).

**S02-D6 (with S02-E1 and S02-D5): combining a setting across the markets a buyer matches.**
- D6 states "Nothing a reference shows is closed". Shopify, though, combines catalogs: "Catalogs from all applicable markets are combined, so customers can access products from all relevant catalogs" (S02-SH-109).
- A customer-segment discount on Shopify "applies to all markets" (S02-SH-198).
- Under D5 a buyer is placed in one market, and under D6 and E1 the most specific value wins. A buyer who matches a business-customer market and a country market sees only one market's catalog.
- Cost to keep it: one module. The resolver finds every market a buyer matches and combines a set-valued setting, while the order still records one market.

**S02-E4 (repeated in S02-D7): payouts and gift cards in the store's one currency.**
- E4 makes the store's currency the one "its gift cards, payouts and own reports use".
- On Shopify each entity's account has its own payout currency (S02-SH-183). Stores on Advanced and Plus may add a payout account in a non-domestic currency (S02-SH-035). Salla pays UAE stores in AED and Kuwait stores in KWD, on schedules of their own (S02-SA-145, S02-SA-150).
- The evidence for E4 is two vendors' choices: Shopify's gift cards (S02-SH-189) and BigCommerce's Stripe payouts (S02-BC-224).
- Under Decision 1 a payout is the provider's, made into the seller's own account (S02-R4). It isn't Sharrwah's to set.
- A store with a Saudi and a UAE business, which S02-D1 makes room for, is paid out in SAR and AED.
- Cost to keep it: one module each (payout records in the holder's ledger, a separate part under S01-E2; gift-card balances).

### 3. Conditions that keep "one module" true

None of these is a closure. Each is a condition the register doesn't state.
- **S02-D4:** one module per new kind of market holds if matching takes a buyer context from the start (country, city, channel, location, company). A matcher fed the buyer's country alone makes each new kind a change wherever a buyer is placed.
  - D4 closes channels and customer groups as mechanisms apart from markets, on an engineering cost. That judgment doesn't weigh Shopify keeping segment discounts apart from markets (S02-SH-198).
- **S02-D7:** a provider converting at payment puts a third currency on the payment. With Stripe Adaptive Pricing, "shoppers can complete orders in their local currency, while payouts to your account are settled in your default currency" (S02-BC-224).
  - That stays one module if each amount carries its own currency code. "Both amounts" shouldn't be built as two fixed columns.
- **S02-E1:** some per-market values are set by the platform or by law, not by the seller.
  - Salla shows cash on delivery only in Saudi Arabia and hides it in other markets automatically (S02-SA-283).
  - Zid gives none on international shipping (S02-ZD-129).
  - Messages to UK buyers fall under the UK's PECR (S02-SH-954).
  - These need a rule layer in the one resolver: one module. The register already sets returns, messages and the address form per market "by a named rule or a regional pattern", which needs this layer.
- **S02-E3:** a store's own country and its main market can differ. On Zid's development store the business address moved to Kuwait while the primary market stayed Saudi Arabia (S02-ZD-468, S02-ZD-471).
  - E3 should not tie the two.
  - E3 should say that the main market's places may change (Shopify: "Change your primary market", S02-SH-128). The first-market-dropped row needs this.
- **S02-E4, first market dropped:** a seller who moves may change the store's own currency. Shopify sets the store currency from the business country (S02-SH-883).
  - This is a setting if every record's store amount carries its currency code. It is a redesign if records assume one store currency that never changes. E4 doesn't say which.
- **S02-E5:** a merchant of record per market sold into (S-03's) holds that market's orders' money, whatever the seller's country. Shopify selects its Managed Markets merchant of record automatically (S02-SH-541).
  - E5's resolver letting it take precedence is one module, given the resolver takes the order's market.
  - Whether a merchant of record counts under Decision 1 is unknown here.
  - E5 is engineering's reading of the founder's "a market's setting". S02-R5 leaves S-02 to place it, so it is for the founder to confirm.

### 4. The company elsewhere: settings, and one redesign outside S-02

**Settings.** With Sharrwah based in Oman or Egypt, or contracting through a company per region as Zid does (S02-ZD-003, S02-ZD-367, S02-ZD-140), only values change in S-02:
- which Sharrwah company and law each seller country maps to;
- the tax on Sharrwah's fees;
- the privacy controller;
- the countries kept out;
- Sharrwah's own billing currency.

These values are S-03's, S-05's, S-07's, S-08's and S-09's. An Omani or Egyptian company's list of countries kept out is unknown from S-02's evidence. The references' lists follow their own jurisdictions: comprehensive US sanctions (S02-BC-073, S02-WC-079).

**One redesign outside S-02,** on a hypothesis. If the company's country, or a seller's, requires data to be held in that country, meeting it changes storage. E2's one interface, a value per country, doesn't reach where data is stored.
- Shopify stores new European merchants' "store data, order data and customer personal data ... at rest in Europe by default" (S02-SH-625).
- Shopify's applicable data protection laws include those "that apply based on the location or residence of Merchant and/or Your Customer(s)" (S02-SH-621).
- Egypt's Law 151 of 2020 governs Zid Egypt's policy (S02-ZD-384). What that law requires about storage is unknown from S-02's evidence.
- No S-02 option causes or avoids this. It is S-08's to settle before storage is designed.

### 5. The first market dropped: settings throughout; no `one market` flag

- No recommendation names a market. The register made each from the five references alone (`decisions.md`, opening), and no register row ties a recommendation to Yemen.
- Dropping the first market changes values only:
  - S-07's list;
  - the places of the stores' main markets;
  - moves under S02-D2, which keep old records' meaning.
- "At launch" appears in two forms, and neither is permanent:
  - S02-D1's one business per store, a starting configuration the model goes beyond;
  - C everywhere, the founder's Decision 1 for every market (S02-R4).
- No item traces to one market today or to today's capacity, so no row is flagged `one market`.
- Salla's Saudi-only features (S02-SA-169, S02-SA-280, S02-SA-350, S02-SA-358) are cited as differences between markets. They are not adopted as constraints.

## Per root decision: each scenario's cost, in a line

Each line gives the second market · the company elsewhere · the first market dropped.

**RD1, the store's own country**
- **S02-D1:** one module (the UAE, Kuwait: papers by country), and **a redesign** (Egypt: a second business for a market, as S02-E2 is worded) · a setting · a setting.
- **S02-D2:** one module (the Gulf: a balance cleared before a move) · a setting · a setting.
- **S02-D3:** one module, `premature` (Saudi Arabia: stock location), and one module, `premature` (the UAE: owner's residence, provider account's country) · a setting · a setting.
- **S02-E2:** **a redesign** (Egypt: a second business for a market) · a setting, and **a redesign** (hypothetical: data held in-country, outside S02-E2, S-08's) · a setting.
- **S02-E5:** one module (Saudi Arabia, the UAE: cash on delivery and a merchant of record by the market sold into) · a setting · a setting.

**RD2, the markets a store sells into**
- **S02-D4:** one module per new kind (Saudi Arabia: channels, point of sale, cities) · a setting · a setting.
- **S02-D5:** a setting (the UAE and Saudi Arabia: one market of several countries, each buyer taxed by their own) · a setting · a setting.
- **S02-E3:** a setting (Kuwait: store country and main market apart) · a setting · a setting, if the main market's places may change.

**RD3, what is set per market**
- **S02-D6:** one module, `premature` (hypothetical: combining across the markets a buyer matches) · a setting · a setting.
- **S02-D7:** a setting (Kuwait, the UAE), one module for a provider's third currency if amounts carry their own currency · a setting · a setting.
- **S02-E1:** one module (Saudi Arabia, the UAE: a rule layer for platform and law limits) · a setting · a setting.
- **S02-E4:** one module, `premature` (the UAE, Kuwait: payout currency per business; gift cards) · a setting · a setting if records carry their currency, a redesign if not.

## Problems

1. **The register disagrees with itself in four places,** each found by the walk:
   - S02-E2's key, "the store's business-entity country", against S02-D1's "each assignable to markets" and S02-E5's business per market.
   - S02-D3's closure against S02-E5's "provider accounts allowed there".
   - S02-D6's "Nothing a reference shows is closed" against S02-SH-109.
   - S02-E4's and S02-D7's payout currency against Decision 1, under which the provider pays out into the seller's own account.
2. **Unknown from S-02's evidence:**
   - whether any founder market requires a local business to sell there, or data held in-country;
   - whether a market's currency needs a precision the store's lacks;
   - what B is, and whether a merchant of record counts under Decision 1;
   - an Omani or Egyptian company's list of countries kept out;
   - the tax effect of a move under a company based in Egypt.
3. **Assumption:** "the company" in scenario 2 is Sharrwah's own company. If the founder meant the seller's company, S02-D3's rows already cover a business registered in one country and trading in another.
4. **Costs are engineering's readings,** not facts. Where a cost holds only on a condition, the row says so. The redesign in finding 1 is the cost as the register is worded.

## Sources behind the findings

The source shown is each statement's first citation, as the slice prints it. A URL source's capture is in phase A's citations.

| Statement | Kind | Source |
| --- | --- | --- |
| S02-SH-280 | shipped | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:raw/runs/20260930T002617Z-graphql-introspection/fetch.warc.gz |
| S02-SH-142, S02-SH-143, S02-SH-147 | stated | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md |
| S02-SH-318 | observed | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:raw/runs/20261005T090923Z-journey-settings-general/steps/001.text.txt |
| S02-SH-1146, S02-SH-1149 | stated | observed-sh@19a5f6435a6dd49b6f4f62d37a5fe8d7c47f950c:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md |
| S02-ZD-367; S02-ZD-371 | official page | https://zid.eg/ar/legal/terms-conditions/ |
| S02-ZD-383; S02-ZD-384 | official page | https://zid.eg/ar/legal/privacy-policy/ |
| S02-ZD-120 | stated | https://help.zid.sa/jahez/ |
| S02-SA-134 | stated | observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/en/texts.jsonl |
| S02-BC-128; S02-BC-081 | stated | through S02-V-230 and S02-V-228 (`variants.tsv`) |
| S02-SH-109 | stated | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md |
| S02-SH-198 | stated | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/rollouts/managing-rollouts.md |
| S02-SH-183 | stated | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md |
| S02-SH-035 | stated | sharrwah-knowledge-map@0189968256432898fd8ec48937109901f18a6412:evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/073-help.shopify.com/text.txt |
| S02-SH-189 | stated | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/discounts-and-gift-cards.md |
| S02-BC-224 | stated | https://support.bigcommerce.com/s/article/Connecting-with-Stripe-OCS?language=en_US |
| S02-SA-145; S02-SA-150 | stated | help.salla.sa, the UAE's and Kuwait's payout articles (first citations as the slice prints them) |
| S02-SH-625 | stated | observed-sh@febbf6c98a1f2a464bb92bd97856b8ba070f3185:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/international-data-transfers/onward-transfers.md |
| S02-SH-621 | official page | https://www.shopify.com/legal/dpa |
| S02-ZD-468; S02-ZD-471 | observed | other-product-class@f44be3f3c97f5863cd58e56d1bf40f41ea3bf45f:zid/raw/runs/20261028T170107Z-devstore-markets-en/: the business address saved as Kuwait (S02-ZD-468); the Main Market, primary, SAR, `"countries": ["SA"]` (S02-ZD-471) |

**Checks run:** every row has 12 fields. Each of the 12 items has its three scenarios. Costs and flags take only the brief's values. All 127 ids cited resolve in S-02's slices, `variants.tsv`, the register or phase C's files. The script is in the scratchpad, outside the repository.
