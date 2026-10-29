# S-02, what a market is: the decisions for the founder (draft)

**What this page is:** the draft of S-02's register (`register.tsv`), for you. Phase C left 143 items for you: 85 are asked here as seven questions (D1 to D7), and 58 go to the subjects that decide them. D8 and D9 are needs the Yemen row found that no platform meets. Each decision gives what the platforms do, engineering's recommendation and why, what it rules out, and what changing course later costs.

**Nothing here is decided.** Each decision ends with an answer line: accept the recommendation, pick another option, or ask. The recommendations for D1 to D7 come from the five references alone, with no market's facts. D8 and D9 go beyond the references, say where, and weigh the established designs read for them.

**Terms:**
- **Market:** a group of buyers a store sells to and sets up in its own way, such as a country or a region.
- **Business record** (a "business entity"): the legal business behind a store, a company or a person trading alone, with its country and address.
- **One entry point:** one place in the design that every feature asks for a value, so a rule changes in one place.

## RD1. The store's own country

### D1. Where a store's country is held

**Question:** Is a store's country the country of the business behind it, held on a business record so that a store can later trade through more than one business? Or is it a single field of the store?

**What the platforms do:** all five hold a country and an address that the seller sets. Shopify holds the country on a business entity with its own address, several per store, and also draws on the billing address and the currency. Four platforms hold a location set on a map or by hand; Salla also has a "seat", and BigCommerce a country per storefront.

**Recommendation (engineering's):** a business record holds the country, one per store at launch, with room for more. The address, location, billing address and currency never set the country. The seat, where the store is based, is the business record's address. A market may show buyers another country or address, for display only. **Why:** one business per store is the simple case of several, so it costs little now.

**What it rules out:** taking the country from the billing address, a map pin, the currency or a seat setting. Two sources for one fact can disagree, and Shopify itself makes the store and billing addresses match a business's country.

**Changing course later: a redesign,** if the country is a store field and a second business comes later. With the business record, a second business is a setting, since each order records the business that served it (E2).

**Answer:** (open)

### D2. When a seller moves country

**Question:** When a seller moves to another country, does the store take a new business record for the new country, keeping its products, customers and orders? Or does its country change in place?

**What the platforms do:** BigCommerce lets the seller change its default country at any time, and WooCommerce's store country changed in place on a test store with orders and tax rates present. Shopify allows a change only once every financial service is off and the addresses match the business's country; for a person trading alone a change creates a new business record, and its support changes the country on request for some stores. WooPayments' account country never changes.

**Recommendation (engineering's):** a business's country never changes in place. A seller who moves adds a business record for the new country, which becomes the main one; the old one closes once nothing open rests on it. Sharrwah's staff do this only where a contract or several business records require it. Other subjects' checks run first: payment accounts (S-04), verification (S-07) and tax forms (S-05). A display country that only sets defaults stays changeable. **Why:** the platforms lock the country while money is attached, and fix it for a person's business record and for a payment account. So what was made under the old country keeps its meaning.

**What it rules out:** changing the legal country in place, which would silently change what the rules and records tied to it mean.

**Changing course later: one module** with D1's business record; a redesign without it.

**Answer:** (open)

### D3. What follows the seller's country

**Question:** Does everything that depends on the seller's country follow a business record's country, rather than each feature keeping a country of its own? That covers the services a store may use, its starting currency and language, its own tax settings, and the checkout fields its country's tax asks for.

**What the platforms do:** all five tie terms, payment services, fees and features to where the seller is. Some also use the store's country, the business's registered country or a business entity. Zid and Shopify also offer some services to every store alike.

**Recommendation (engineering's):** every such rule reads one country, through one entry point: the country of the store's main business, or of the business that served the order or market in question. That is where a person trading alone lives, or where a company is registered. "Every store alike" means one answer for every country, and the billing address serves only Sharrwah's invoices. **Why:** the rules agree with each other, and change in one place.

**What it rules out:** a second copy of the seller's own country used as a key, such as the billing address's country. Copies can disagree, and Shopify itself keeps the billing address in an active business's country. **Not ruled out:** other places with rules of their own, which their subjects decide: where stock is held (S-10), each owner's residence (S-07), a payment account's country (S-04), and an area within the country (D8).

**Changing course later: one module,** since each order records its business (E2). A redesign if features keep countries of their own.

**Answer:** (open)

**What follows by rule (RD1):** as all five do, the seller sets the store's country and address, and where the seller is decides terms, payment services, fees and features. Bound per seller's country by rule: the store's taxes, the privacy law, and whether one contracting company serves every store there (S-03 decides). Kept open: which countries are kept out, who else checks a business, and a balance cleared before a move (none at launch, under Decision 1). Left to the build: permissions and address fields for a move. **Moved:** 47 items, to S-03, S-04, S-05, S-07, S-08, S-09 and S-11.

## RD2. The markets a store sells into

### D4. What a market can be

**Question:** Is a market only a group of places (one or several countries, a region, a city)? Or may it also be a sales channel, a point of sale, a group of business customers or a separate storefront?

**What the platforms do:** four platforms define markets by countries, Salla and Shopify also by regions, Salla by cities. Zid, Shopify and BigCommerce treat sales channels as markets, BigCommerce through storefronts. Shopify defines a market by conditions a buyer matches (a place, a business customer, a point of sale, a channel), and nests markets. WooCommerce and Zid hold some channel or point-of-sale values apart from markets; BigCommerce prices by customer group, which no platform makes a kind of market.

**Recommendation (engineering's):** a market is a named set of conditions of a few kinds. Places come first; channel, point-of-sale, business-customer and storefront kinds follow, as new kinds of condition. A market may sit inside another and inherit from it, and a buyer is matched by their whole context, not only their country. A group of customers stays beside markets, as a key that a setting such as a price may use. **Why:** the most general form the platforms show covers every narrower one by setting. A new kind of market is then a new condition, not a second system.

**What it rules out:** separate systems for channels and points of sale beside markets, which would answer twice which prices and settings a buyer sees. Customer groups are not ruled out, since no market kind reaches them.

**Changing course later: a redesign,** if markets hold only countries and a later kind must come; one module if conditions have kinds from the start.

**Answer:** (open)

### D5. How markets overlap

**Question:** May one market hold several countries, and may a country fall in more than one market, nested within one kind or across kinds? A buyer's values would then come from the most specific market that applies.

**What the platforms do:** Salla allows one country per market, as its taxes follow the market's country. Shopify lets a country fall in several markets: a submarket inherits from the market it sits in, and across kinds the most specific settings apply and catalogs combine. BigCommerce ties each site and language version to one storefront. Salla and Shopify place a buyer by country; Salla and BigCommerce let the seller choose who enters.

**Recommendation (engineering's):** a market may hold several countries; one country per market remains a choice. Within one kind, markets nest: a market inside another inherits from it and takes priority. Across kinds, a single value comes from the most specific market, and a list may combine. Which kind comes first is stated only for business-customer, retail and region markets, in that order (Shopify); for other kinds it is open. The seller may limit who enters a market. **Why:** a seller can sell to a region as one market and treat one country apart inside it. All five work tax out from the buyer's country (a fact), so a market of several countries can hold tax per buyer's country (engineering's reading).

**What it rules out:** two markets of one kind that partly overlap, neither inside the other, since nothing would order them. This is a reading: no platform's statement shows that case.

**Changing course later: one module.**

**Answer:** (open)

**What follows by rule (RD2):** every store has a main market, which the platform makes and whose places may change; the seller makes the others. Left to the build: how many markets a plan allows, which kinds it offers, and who may remove one.

**Moved:** to S-07, whether a market may hold only countries Sharrwah serves.

## RD3. What is set per market

### D6. Settings that vary by market

**Question:** Should each setting a seller may want to vary by market be held once for the store, with each market able to change it and a product able to narrow its shipping and payment methods? The settings are: language, web address, products offered, discounts, design, checkout and accounts, taxes, shipping, payment methods, returns, stock locations, contact details, staff access, units and time zone, store status, messages, apps and notifications.

**What the platforms do:** of these 18, BigCommerce holds 16 per market, Salla 15, Shopify 12, Zid 3 and WooCommerce 1. All five hold some once for the store. The general pattern is a store value that each market inherits and may change. Zid and Shopify restrict shipping or payment per product, and three platforms vary checkout fields by the buyer's country.

**Recommendation (engineering's):** that pattern for every such setting, through one entry point. A single value takes the most specific, a market's over the store's. A list may combine across the markets a buyer matches: the products offered, as Shopify combines catalogs, and, by engineering's own choice, payment methods and shipping options, with any limit the platform or a law sets applied after combining. A product may narrow its shipping and payment methods. Which settings sellers may change, and when, is a later setting.

**Why:** a store-wide value is the same model with no market change made, so each setting is ready the day a seller wants it per market.

**What it rules out:** a market keeping a full copy of every setting, which drifts and repeats each store-wide change. Nothing a platform shows is ruled out.

**Changing course later: a setting,** on the recommendation; a redesign if settings start store-only and markets come later.

**Answer:** (open)

### D7. Currency and prices per market

**Question:** May each market sell in its own currency at its own prices, converted by Sharrwah at an exchange rate held for that market or set by the seller? Every order would keep its amounts in both the market's currency and the store's.

**What the platforms do:** Salla, Zid and Shopify hold a currency and prices per market, and BigCommerce per storefront; WooCommerce allows one base currency per store. Shopify holds an exchange rate per market, for markets that have a currency of their own. Salla, Zid and WooCommerce work from the currency's rate and convert prices when the seller chooses; Shopify's automatic conversion reads the same way (engineering's reading). Four platforms vary prices by the buyer's country. Shopify keeps gift cards in the store's own currency.

**Recommendation (engineering's):** each market may carry its own currency and exchange rate, starting from the store's; prices convert at that rate unless the seller sets them for the market or a country inside it. Every order, refund and report keeps both amounts, with the market and rate used. The store's currency stays the one for its own reports and the default for gift cards; a gift card in a market's currency stays open. Sharrwah sets no payout currency: under your Decision 1, each provider pays out on its own terms. Which currencies and rate sources is S-09's question.

**Why it stands apart from D6:** its first part, two amounts on each record, would reach every money record if it were added later.

**What it rules out:** money records that keep one currency only.

**Changing course later, and your answer, by part:**
- **Two amounts on every record:** a redesign, if orders keep one currency and markets later sell in their own. **Answer:** (open)
- **Where the rate is held,** per market or per currency: one module. **Answer:** (open)
- **Which markets carry their own currency:** a setting, once both amounts are kept. **Answer:** (open)

**What follows by rule (RD3):** as all five do, the seller sets each market's settings; tax, shipping, payment methods, the address form and the currency shown follow the buyer's country; one currency, tax setup and set of units hold for the store. Set per market by rule or pattern: returns, messages to buyers, the address form, and a tax partner such as Avalara. Kept open: business entities per market (D1 leaves room); returns, privacy, analytics and notifications per market. Left to the build: who besides the seller sets each setting. **Moved:** a merchant of record and store closures to S-03; currency conversion by providers to S-04; couriers' cash on delivery and fulfilment services' locations to S-10.

## Needs no reference meets

The Yemen row found these needs, written without the market's name. Each was checked against the five platforms and comes from the Yemen row alone. For both, established designs were then read and weighed by their kind of source (`designs.tsv`). A recommendation to keep room for one is for you to weigh by its cost; it is not a reason drawn from one market.

### D8. A seller's area within a country

**The need** (`yemen-row.tsv`, lines 13 and 14): the areas of one country can answer to different rules for payment services, the currency and the exchange rate. A rule tied to the seller's country then gives one answer where the areas differ. And a seller moving between such areas keeps its country, so a move's checks wouldn't run.

**What the platforms do:** for payment services, they count an area only where it has a country code of its own. For tax, Shopify and WooCommerce tie a seller's rules to a province or a state. Shopify also ties one feature to where the seller's fulfilment locations are. None ties payment services, the currency or the rate to such an area, or runs a move's checks when it changes.

**Question:** Should the rules that depend on where the seller is, payment services and currency among them, be able to use an area within a country, held as a dated field of the business record, beside the country, with a change of such an area running the checks of a move?

**Options:** (a) don't provide for it: countries only, as the platforms do for payment services; (b) areas for some rules, as they do for tax; (c) any rule may use the country or an area within it, and a change of an area a rule uses runs that rule's checks.

**Recommendation (engineering's), weighed against the designs read:** (b) now, with room kept for (c). Tax rules may use an area, as the platforms do and as Stripe keys a dated tax registration on a state. The area is held from the start as a dated field at two levels (the business record, and the locations a store fulfils from, S-10's): a stable identifier, since published area codes change and are reused (Unicode); at a level named per country, since levels differ between countries (OpenStreetMap); and apart from the postal address, whose area is optional (Google). With E2, a payment or currency rule keyed on the area, or a move's checks on an area change, is then one module. **Where the sources cut against (c):** none ties payment services or currency to an area, and Fowler finds dating a field later easy in code, so the dated area now protects past records only. The extension comes from the Yemen row's need alone.

**What it rules out:** countries only, as a rule of the design. In engineering's reading, a dated area costs little now, and past records without one can't recover it.

**Changing course later: one module,** given E2's entry point and the dated area field; only past records kept without an area can't be recovered. A redesign only if E2 or D1 is declined.

**Answer:** (open)

### D9. Two currency areas under one currency code

**The need** (`yemen-row.tsv`, line 35): one currency code can cover two currency areas of one country, with different notes and exchange rates. Under D7, D4 and D5, two markets for the two areas can already sell at two rates under the one code, and each order keeps its market and rate. What a currency held by its code alone can't do is tell the areas apart in prices, stored amounts and reports, except through the market: totals by currency mix them.

**What the platforms and designs show:** Salla, Zid and WooCommerce work from one rate per currency. Shopify holds a rate per market, but its market for an area within a country takes its parent's currency (an early-access feature). The standards and platforms read identify a currency by its code alone: Unicode, Java's money type and Stripe's payments. The ISO 4217 lists read the same way (engineering's reading). One ledger design, TigerBeetle, holds each amount's currency as a record the application defines.

**Question:** Should a currency be able to name a currency area within its code, so that prices, stored amounts and reports tell two areas sharing one code apart by currency, not only by market?

**Options:**
- **(a) Don't provide for it,** with one rate per currency code: the two areas sell at one rate.
- **(b) What D7 already gives:** a market per area with its own rate, the areas told apart only by market.
- **(c) Name the area in the currency itself:** a currency record (a code, and an area where one is named) that prices, amounts and reports refer to, mapped to the bare code where a provider takes only the code.

**Recommendation (engineering's), weighed against the designs read:** (b) now, with room kept for (c). Amounts refer to a currency record, one per code at launch, so naming an area later is a new record; that choice is S-09's. **Where the sources cut against (c):** Unicode, Java and Stripe identify a currency by its code alone, so an area would have to map back to the bare code at every provider. They support the room's form: TigerBeetle defines its own currency numbers, and keeps a changed unit as a new record. The need comes from the Yemen row alone.

**What it rules out:** nothing a platform or a design shows; (c) stays reachable through the currency record.

**Changing course later: one module** if amounts in money records refer to a currency record; **a redesign** if a bare currency code is stored in every amount, since every money record, rate and report would then have to learn the area.

**Answer:** (open)

## What moved to other subjects

Each subject decides its values. S-02 holds where each rule lives, tied to a business record's country (D1, D3) or set per market (D6). The register's rows S02-M1 to S02-M8 give the detail, and S-09 takes D9's condition on money records.

## Engineering constraints

Engineering proposes these; you may veto any. **E1:** each per-market setting is read through one entry point: a single value from the most specific market, then the store; a list may combine across the markets a buyer matches, with limits applied after; a customer group can be a key beside the market. **E2:** each rule tied to the seller's country is read through one entry point, for the order or market in question, from the country of the business that served the order or the store's main business; each order records that business, and with D8 the entry point also takes an area. **E3:** every store has one main market, which carries the store's own values; its places may change. **E4:** a store keeps a currency of its own, for its reports and as the default for gift cards; a gift card in a market's currency stays open. The store's currency may change; records made before a change keep the currency of their day.

**E5, for you to confirm:** your decision of 26 October says that who holds sellers' money "is a market's setting". Engineering reads "market" here as the seller's own country, through the business that takes the payment. The other reading is the markets a store sells into, as Shopify assigns businesses to markets for payment processing. Either way, C holds everywhere at launch.
