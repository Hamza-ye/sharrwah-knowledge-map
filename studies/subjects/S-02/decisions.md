# S-02, what a market is: the decisions for the founder (draft)

**What this page is:** the draft of S-02's register (`register.tsv`), for you. Phase C's 142 items for you, in 90 wordings, are asked here as seven questions; an eighth is a need the Yemen row found that no platform meets. Each gives what the five reference platforms do, engineering's recommendation and why, what it rules out, and what changing course later would cost.

**Nothing here is decided.** Each decision ends with an answer line: accept the recommendation, pick another option, or ask. Every recommendation comes from the five references alone, with no market's facts.

**Terms:**
- **Market:** a group of buyers a store sells to and sets up in its own way, such as a country or a region.
- **Business record** (a "business entity"): the legal business behind a store, a company or a person trading alone, with its country and address.
- **One entry point:** a single place in the design that every feature asks for a value, so a rule changes in one place.

## RD1. The store's own country

### D1. Where a store's country is held

**Question:** Is a store's country the country of the business behind it, held on a business record so that a store can later trade through more than one business, rather than a single field of the store?

**What the platforms do:**
- All five hold a country and an address the seller sets.
- Shopify holds it on a business entity with its own address; a store can have several, each serving chosen markets. Shopify also draws on the billing address and the currency.
- Four platforms hold a map location, Salla a "seat", and BigCommerce a country per storefront.

**Recommendation (engineering's):** a business record holds the country: one per store at launch, with room for more.
- The address, the map location, the billing address and the currency never set the country.
- A market may show buyers another country or address, for display only.

**Why:** one business per store is the simple case of several, so it costs little now.

**What it rules out:** taking the country from the billing address, a map pin, the currency or a seat setting. Two sources for one fact can disagree, and Shopify itself makes the store and billing addresses match a business's country.

**Changing course later: a redesign** if the country is a store field and a second business comes later, since every rule tied to the seller's country would move. With the business record it is a setting, as each order records the business that served it (E2).

**Answer:** (open)

### D2. When a seller moves country

**Question:** When a seller moves to another country, does the store take a new business record for the new country, keeping its products, customers and orders, rather than changing its country in place?

**What the platforms do:**
- BigCommerce lets the seller change its default country at any time.
- Shopify allows a change only once every financial service is off and the addresses agree with the business's country. For a person trading alone, a change creates a new business record.
- WooPayments' account country never changes.
- Shopify's support changes it on request for some stores, such as Plus stores.

**Recommendation (engineering's):** a business's country never changes in place. A seller who moves adds a business record for the new country, which becomes the main one; the old one closes once nothing open rests on it. Sharrwah's staff do this only where a contract or several business records require it. Other subjects' checks run before the switch: payment accounts (S-04), verification (S-07), tax forms (S-05). A display country that only sets defaults stays changeable.

**Why:** the platforms that tie money or a contract to the country lock it, so what was made under the old country keeps its meaning.

**What it rules out:** changing the legal country in place. That would silently change the meaning of the rules and records tied to it.

**Changing course later: one module** with D1's business record; a redesign without it.

**Answer:** (open)

### D3. What follows the seller's country

**Question:** Does everything that depends on the seller's country follow a business record's country, rather than each feature keeping a country of its own? That includes the services a store may use, its starting currency and language, its own tax settings, and the checkout fields its country's tax asks for.

**What the platforms do:** all five tie terms, payment services, fees and features to where the seller is. Some also use the store's country (four platforms), the business's registered country (Zid, Shopify), a business entity (Shopify), or nothing, every store alike (Zid, Shopify).

**Recommendation (engineering's):** every such rule reads one country through one entry point: that of the store's main business, or of the business that served the order or market in question; where a person trading alone lives, or where a company is registered. "Every store alike" is one answer for every country; the billing address serves only Sharrwah's invoices.

**Why:** the rules agree with each other, and change in one place.

**What it rules out:** a second copy of the seller's own country used as a key, such as the billing address's country or a feature's own country field. Copies can disagree, and Shopify itself keeps the billing address in an active business's country.

**Not ruled out:** other places that carry rules of their own, which their subjects decide: where stock is held (S-10), each owner's country of residence for documents (S-07), a payment account's country (S-04), and an area within the seller's country (D8).

**Changing course later: one module,** since each order records its business (E2); a redesign if features keep countries of their own.

**Answer:** (open)

**What follows by rule (RD1):** as all five do, the seller sets the store's country and address, and where the seller is decides terms, payment services, fees and features. Set per seller's country by rule: the store's taxes, the privacy law, one contracting company for all. Kept open: which countries are kept out, who else checks a business, a balance cleared before a move (none exists at launch, under Decision 1). Left to the build: permissions and address fields for a move. **Moved:** 45 items (below).

## RD2. The markets a store sells into

### D4. What a market can be

**Question:** Is a market only a group of places (one or several countries, a region, a city), or may it also be a sales channel, a point of sale, a group of business customers or a separate storefront?

**What the platforms do:**
- Four platforms define markets by countries; Salla and Shopify also by regions, Salla by cities.
- Zid, Shopify and BigCommerce treat sales channels as markets, BigCommerce through storefronts.
- Shopify defines a market by conditions a buyer matches (a place, a business customer, a point of sale, a channel), and allows a market within a market.
- WooCommerce, Zid and BigCommerce handle channels, points of sale or customer groups apart from markets.

**Recommendation (engineering's):** a market is a named set of conditions of a few kinds: places first, then channel, point-of-sale, business-customer and storefront kinds as new kinds of condition. A market may sit inside another and inherit from it.

**Why:** the most general form the platforms show covers every narrower one by setting. A new kind of market is then a new condition, not a second system.

**What it rules out:** separate systems for channels, points of sale or customer groups beside markets. Two systems would answer the same question: which prices and settings a buyer sees.

**Changing course later: a redesign,** if markets hold only countries and a later kind must come; one module if conditions have kinds from the start.

**Answer:** (open)

### D5. How markets overlap

**Question:** May one market hold several countries, and may a country fall in more than one market? A buyer would then match, by their country, at most one market of each kind.

**What the platforms do:**
- Salla allows one country per market, as its taxes follow the market's country; Shopify's main market is one country or region.
- Shopify lets a country fall in several markets: the most specific settings apply, and their catalogs combine.
- BigCommerce ties each site and language version to one storefront. Salla and Shopify place a buyer by country; Salla and BigCommerce let the seller choose who enters.

**Recommendation (engineering's):** a market may hold several countries, one per market remaining a choice. A country may fall in markets of different kinds, but in one market of each kind. Where several kinds apply, a single value (a currency, a language) comes from the most specific, and a list (the products offered) may combine, as Shopify does. The seller may limit who enters a market.

**Why:** a seller can sell to a region as one market and still treat one country apart. Tax doesn't need one country per market, since all five work it out from the buyer's country.

**What it rules out:** two markets of one kind claiming the same buyer, with nothing to choose between them.

**Changing course later: one module.**

**Answer:** (open)

**What follows by rule (RD2):** every store has a main market, which the platform makes; the seller makes the others. Left to the build: how many markets a plan allows, which kinds, who may remove one. **Moved:** to S-07, whether a market may hold only countries Sharrwah serves.

## RD3. What is set per market

### D6. Settings that vary by market

**Question:** Should each setting a seller may want to vary by market be held once for the store, with each market able to change it and a product able to narrow its shipping and payment methods? The settings are: language, web address, products offered, discounts, design, checkout and accounts, taxes, shipping, payment methods, returns, stock locations, contact details, staff access, units and time zone, store status, messages, apps and notifications.

**What the platforms do:**
- Four platforms hold many of these per market and others once for the store; all five hold some once.
- The general pattern is a store value each market inherits and may change (Salla's and Shopify's market designs, BigCommerce's message templates).
- Zid and Shopify restrict shipping or payment per product; three platforms vary checkout fields by the buyer's country.

**Recommendation (engineering's):** that pattern for every such setting, through one entry point. A single value takes the most specific, a market's over the store's; a list, such as the products offered, may combine across the markets a buyer matches, as Shopify's catalogs do; a product may narrow its shipping and payment methods. Which settings sellers may change, and when, is a later setting.

**Why:** a store-wide value is the same model with no market change made, so each setting is ready the day a seller wants it per market.

**What it rules out:** a market keeping a full copy of every setting. Copies drift apart, and each store-wide change would have to be repeated. Nothing a platform shows is ruled out.

**Changing course later: a setting** on the recommendation; a redesign if settings start store-only and markets come later.

**Answer:** (open)

### D7. Currency and prices per market

**Question:** May each market sell in its own currency at its own prices, either converted by Sharrwah at an exchange rate held for that market or set by the seller? Every order would keep its amounts in both the market's currency and the store's.

**What the platforms do:**
- Salla, Zid and Shopify hold a currency and prices per market, BigCommerce per storefront; WooCommerce allows one base currency per store.
- Shopify and Salla hold an exchange rate per market, Zid and WooCommerce per currency; all four convert prices when the seller chooses.
- Four platforms vary prices by the buyer's country; Shopify keeps gift cards in the store's own currency.

**Recommendation (engineering's):** each market may carry its own currency and exchange rate, starting from the store's. Prices convert at the market's rate unless the seller sets them for the market or a country inside it. Every order, refund and report keeps both amounts, with the market and rate used. The store's currency stays the one for gift cards and its own reports. Sharrwah sets no payout currency: under your Decision 1, each provider pays out on its own terms. Which currencies and rate sources is S-09's question.

**Why it stands apart from D6:** a later change reaches every money record, not one setting. A second amount costs little now, and a redesign later.

**What it rules out:** money records that keep one currency only.

**Changing course later: a redesign.**

**Answer:** (open)

**What follows by rule (RD3):** as all five do, the seller sets each market's settings; tax, shipping, payment methods, the address form and the currency shown follow the buyer's country; one currency, tax setup and set of units hold for the store. Set per market by rule: returns, messages to buyers, the address form. Kept open: business entities per market (D1 leaves room); returns, privacy, analytics and notifications per market. Left to the build: who besides the seller sets each setting. **Moved:** a merchant of record and store closures to S-03, currency conversion by providers to S-04, duties partners to S-05, couriers' cash on delivery and fulfilment services' locations to S-10.

## Needs no reference meets

The Yemen row found three needs, written without the market's name. Each was checked against the five platforms first.

### D8. A seller's area within a country

**The need** (gaps 1 and 2; `yemen-row.tsv`, lines 13 and 14): the areas of one country can answer to different rules for payment services, the currency and the exchange rate. A rule tied to the seller's country then gives one answer where they differ, and a seller moving between such areas keeps its country, so a move's checks wouldn't run.

**What the platforms do:** for payment services they count an area only where it has a country code of its own. For tax and one feature, Shopify and WooCommerce tie a seller's rules to a province, a state or a part of one country. None ties payment services, the currency or the rate to such an area, or runs a move's checks when it changes.

**Question:** Should the rules that depend on where the seller is, payment services and currency among them, be able to use an area within a country beside the country, with a change of such an area running the checks of a move?

**Options:** (a) don't provide for it: countries only, as the platforms do for payment services; (b) areas for some rules, as they do for tax; (c) any rule may use the country or an area within it, and a change of an area a rule uses runs that rule's checks.

**Recommendation (engineering's):** (c). The business record's address already holds the area, and the one entry point takes it beside the country; area changes are dated on the business record, and each order keeps the area that served it. At launch no rule needs an area. **Why:** it costs little now, and rests on no one market: the platforms themselves tie rules to areas of one country.

**What it rules out:** countries only, as a rule of the design.

**Changing course later: a redesign** without it: rules re-keyed from country to area, and plain address edits turned into checked moves, across records that kept no area. One module with it.

**Answer:** (open)

### Gap 3, one currency code over two currency areas: met

The need is at `yemen-row.tsv`, line 35. Shopify and Salla hold an exchange rate per market, and a market can be drawn for an area within a country, so two areas sharing one currency code can sell at two rates. That follows into D7 (a rate per market, kept on each order) and D4. Whether an amount's currency should also name its area, beyond its code, moves to S-09, which will bring it to you.

## What moved to other subjects

Each subject decides its values; S-02 holds where each rule lives, tied to a business record's country (D1, D3) or set per market (D6). The register's rows S02-M1 to S02-M8 give the detail.
- **S-03:** the contracting company and its law, a merchant of record, and store closures.
- **S-04:** which payment services and providers a seller may connect; each provider pays out on its own terms (Decision 1).
- **S-05:** tax on Sharrwah's fees, and checks of tax numbers.
- **S-07:** the countries served and kept out, documents and checks.
- **S-08:** privacy.
- **S-09:** the currency of Sharrwah's bill, and whether an amount's currency names its area (gap 3).
- **S-10:** couriers' cash on delivery, and fulfilment services' locations.
- **S-11:** Sharrwah's fees.

## Engineering constraints

Engineering proposes these; you may veto any.
- **E1.** Each setting that varies by market is read through one entry point. A single value comes from the most specific market, then the store; a list may combine across the markets a buyer matches.
- **E2.** Each rule tied to the seller's country is read through one entry point, for the order or market in question. It uses the country of the store's main business, or of the business that served the order. Each order records that business, and keeps it if a market's business changes later.
- **E3.** Every store has one main market, which carries the store's own values.
- **E4.** A store keeps a currency of its own beside any market's, for its gift cards and its own reports.
- **E5, for you to confirm:** your decision of 26 October says who holds sellers' money "is a market's setting". Engineering reads "market" as the seller's own country, through the business that takes the payment, each market's payment methods choosing among the provider accounts allowed there. The other reading is the markets a store sells into, as Shopify assigns businesses to markets for payment processing. C holds everywhere at launch either way.
