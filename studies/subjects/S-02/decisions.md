# S-02, what a market is: the decisions for the founder (draft)

**What this page is:** the draft of S-02's register (`register.tsv`), written for you. Phase C left 142 items for you, in 90 wordings. Most asked one question setting by setting, so here each question is asked once. Each decision gives what the five reference platforms do, engineering's recommendation and why, what the recommendation rules out, and what changing course later would cost.

**Nothing here is decided.** Each decision ends with an answer line for you. You can accept the recommendation, pick another option, or ask. Every recommendation was made from the five references alone, without any market's facts. The Yemen row and the scenario walk test them next.

**Three terms, used below:**
- **Market:** a group of buyers a store sells to and sets up in its own way, such as a country or a region.
- **Business entity:** a record of the legal business behind a store, holding its country and address. The business is a company, or a person trading on their own.
- **One entry point:** a single place in the design that every feature asks for a value, so that a rule changes in one place.

## RD1. The store's own country

### D1. Where a store's country is held

**Question:** Is a store's country the country of the business behind it, held on a business-entity record so that a store can later trade through more than one business? Or is it a single field of the store?

**What the platforms do:**
- All five hold a country and an address for the store, which the seller sets.
- Shopify holds the country on a business entity that has its own address. A store can have several entities, each serving chosen markets.
- Shopify also uses the billing address the seller pays it from, and the store's currency, to set the country.
- Salla, Zid, Shopify and WooCommerce hold a location set on a map.
- Salla has a separate "seat" setting (مقر المتجر).
- BigCommerce lets each storefront show a country of its own.

**Recommendation (engineering's):** a business-entity record holds the store's country: one per store at launch, with room for more.
- The address, the map location, the billing address and the currency are separate records. None of them sets the country.
- A market may show buyers a different country or address, but only for display.

**Why:** one entity per store is the simple case of several, so it costs little now. And every rule that depends on the seller's country then reads one record.

**What it rules out:** taking the country from the billing address, a map pin, the currency or a seat setting. Two sources for one fact can disagree. Shopify itself requires the store address and the billing address to match an entity's country.

**Changing course later: a redesign.** Suppose the country is a field of the store and a second business is needed later. Every rule tied to the seller's country, and every record made under it, would have to move.

**Answer:** (open)

### D2. When a seller moves country

**Question:** When a seller moves to another country, does the store take on a new business record for the new country, keeping its products, customers and orders? Or does its country change in place?

**What the platforms do:**
- BigCommerce lets the seller change its default country at any time.
- Shopify allows a change only after every financial service is switched off and the addresses agree with the business's country. For a person trading alone, no one can change the country: a change creates a new business record. WooPayments' account country can never be changed.
- Shopify's support changes it on request for some stores, such as those under its Plus contract.

**Recommendation (engineering's):** a business's country never changes in place.
- A seller who moves adds a business record for the new country, which becomes the store's main one. The old record closes once nothing open rests on it.
- Sharrwah's staff do it only where a contract, or a store with several business records, requires it.
- The checks other subjects set, such as closing payment accounts (S-04), a new verification (S-07) and tax forms (S-05), run before the switch.
- A display country that only sets defaults stays changeable at any time.

**Why:** the platforms that tie money or a contract to the country lock it. Contracts, payment accounts and tax forms made under the old country keep their meaning.

**What it rules out:** changing the legal country in place, because rules and records tied to it would change meaning silently.

**Changing course later: one module,** if D1's business record exists: only the move's procedure changes. Without it, a redesign.

**Answer:** (open)

### D3. What follows the seller's country

**Question:** Does everything that depends on the seller's country follow one record, the country of the business behind the store, rather than each feature keeping a country of its own? Examples: the services a store may use, its starting currency and language, its own tax settings, and the checkout fields its country's tax asks for.

**What the platforms do:** all five tie terms, payment services, fees and features to where the seller is. Beyond that, they differ:
- Salla, Zid, Shopify and WooCommerce also use the store's country.
- Zid and Shopify use the country where the business is registered.
- Shopify uses a business entity.
- Zid and Shopify offer some services to every store alike.

**Recommendation (engineering's):** every such rule reads the business record's country, through one entry point.
- For a person trading alone, that country is where they live. For a company, it is where the company is registered.
- "Every store alike" means the rule gives the same answer for every country.
- The billing address serves only Sharrwah's own invoices.
- The rules moved to other subjects (below) use the same entry point.

**Why:** the rules then agree with each other, and a change happens in one place.

**What it rules out:** a rule keyed on a second country of the seller, such as the billing address or a feature's own field. Two countries for one seller can disagree. Shopify itself requires the billing address to be in an active business's country.

**Changing course later: one module,** if every rule reads through the one entry point. A redesign if features keep countries of their own.

**Answer:** (open)

**What follows by rule (RD1):**
- Carried as all five carry it: the seller sets and changes the store's country and address, and where the seller is decides terms, payment services, fees and features.
- Set per seller's country, by a named rule or a regional pattern: the store's own taxes, the privacy law, and one contracting company where one serves every store.
- Kept open until evidence settles them: which countries are kept out, who else checks a business, and whether a balance must be cleared before a move. At launch no balance exists that sellers pay into, under your Decision 1.
- Left to the build: staff permissions for a move, and the address fields it asks for.

**Moved:** 45 of RD1's items, to S-03 (the contracting company), S-04 (payment providers and payouts), S-05 (tax on Sharrwah's fees), S-07 (countries served, documents and checks), S-08 (privacy), S-09 (the billing currency) and S-11 (Sharrwah's fees). See the table at the end.

## RD2. The markets a store sells into

### D4. What a market can be

**Question:** Is a market only a group of places (one or several countries, a region, a city)? Or may it also be a sales channel, a shop's point of sale, a group of business customers, or a separate storefront?

**What the platforms do:**
- Salla, Zid, Shopify and WooCommerce define markets by one or several countries. Salla and Shopify also use regions, and Salla also uses cities.
- Zid, Shopify and BigCommerce treat sales channels as markets.
- Shopify defines a market by conditions a buyer matches: a place, a business customer, a point of sale or a channel. Shopify also allows a market within a market.
- BigCommerce uses separate storefronts.
- WooCommerce, Zid and BigCommerce handle channels, points of sale and customer groups apart from markets.

**Recommendation (engineering's):** a market is a named set of conditions of a few kinds.
- Places come first.
- Channel, point-of-sale, business-customer and storefront kinds are added later, as new kinds of condition.
- A market may sit inside another and inherit from it.

**Why:** the most general form the platforms show covers every narrower one by setting. A later kind of market then needs a new condition, not a second system beside markets.

**What it rules out:** separate systems for channels, points of sale or customer groups, alongside markets. Two systems would answer the same question: which prices and settings a buyer sees.

**Changing course later: a redesign,** if markets hold only countries and a later kind must be added. One module if conditions have kinds from the start.

**Answer:** (open)

### D5. How markets overlap, and which one a buyer is in

**Question:** May one market hold several countries, and may a country fall in more than one market? Each buyer would then be placed in one market, by their country and the closest match.

**What the platforms do:**
- Salla allows one country per market, because its taxes follow the market's country. Shopify's main market is one country or region.
- Shopify lets a country fall in several markets, and uses the most specific match.
- BigCommerce ties each site and each language version to one storefront.
- Salla and Shopify place a buyer by their country. Salla and BigCommerce let the seller choose which customers may enter a market.

**Recommendation (engineering's):** a market may hold several countries; one country per market remains a choice.
- A country may fall in markets of different kinds, but in only one market of each kind.
- Each buyer is placed in one market, by their country and the most specific match.
- The seller may limit which customers enter a market.

**Why:** a seller can sell to a region as one market and still treat one country apart. Tax doesn't need one country per market: all five work it out from the buyer's country.

**What it rules out:** two markets of the same kind claiming one buyer, with nothing to choose between them.

**Changing course later: one module.**

**Answer:** (open)

**What follows by rule (RD2):**
- Every store has a main market, which the platform creates. The seller creates the others.
- Left to the build: how many markets a plan allows, which kinds a plan offers, and who may remove a market.

**Moved:** one item to S-07: whether a market may hold only the countries Sharrwah serves.

## RD3. What is set per market

### D6. Settings that vary by market

**Question:** Should each setting a seller may want to vary by market be held once for the store, with each market able to override it, and a product able to narrow its shipping and payment methods? The settings: language, web address, products offered, discounts, design, checkout and accounts, taxes, shipping, payment methods, returns, stock locations, contact details, staff access, units and time zone, store status, messages, apps and notifications.

**What the platforms do:**
- Salla, Zid, Shopify and BigCommerce hold many of these per market. Others they hold once for the whole store, and all five do so for some settings.
- The general pattern is a store value that each market inherits and may change. Salla's market designs, Shopify's per-market design and BigCommerce's message templates work this way.
- Zid and Shopify also restrict shipping or payment per product.
- Salla, Shopify and WooCommerce ask for checkout fields by the buyer's country.

**Recommendation (engineering's):** that general pattern for every such setting, through one entry point. The most specific value wins: a product's over a market's, and a market's over the store's.
- Which settings sellers may change per market, and when each reaches them, is a later setting.

**Why:** a setting held once for the whole store is the same model with no market change made. Each setting is ready the day a seller wants it per market.

**What it rules out:** a market keeping its own full copy of every setting. Copies drift apart, and each store-wide change would have to be repeated per market. Nothing a platform shows is ruled out.

**Changing course later: a setting,** on the recommendation. A redesign if settings are first held for the store only and markets come later.

**Answer:** (open)

### D7. Currency and prices per market

**Question:** May each market sell in its own currency at its own prices, either converted by Sharrwah from the store's prices at an exchange rate or set by the seller? Every order would then keep its amounts in both the market's currency and the store's.

**What the platforms do:**
- Salla, Zid and Shopify hold a currency and prices per market, and BigCommerce per storefront. WooCommerce allows one base currency per store.
- Salla, Zid and WooCommerce convert a market's prices at the exchange rate when the seller chooses, and Shopify states that it does the same.
- Zid, Shopify, BigCommerce and WooCommerce vary prices by the buyer's country; Shopify does so for a country within a market.
- Shopify keeps gift cards in the store's own currency, and BigCommerce's Stripe pays sellers out in it.

**Recommendation (engineering's):** each market may carry its own currency, starting from the store's.
- Prices are converted from the store's at a rate, unless the seller sets them for the market, or for a country inside it.
- Every order, refund and report keeps both amounts.
- The store's own currency stays the one used for gift cards and payouts.
- Which currencies, and which rates, is S-09's question.

**Why it stands apart from D6:** changing it later reaches every money record, not one setting. A second amount on each record costs little now and a redesign later.

**What it rules out:** money records that keep one currency only.

**Changing course later: a redesign.**

**Answer:** (open)

**What follows by rule (RD3):**
- Carried as all five carry it: the seller sets each market's settings; tax, shipping, payment methods, the address form and the currency shown follow the buyer's country; one currency, tax setup and set of units hold for the whole store.
- Set per market by a named rule or a regional pattern: returns, messages to buyers and the address form.
- Kept open: business entities per market (D1 leaves room); returns, privacy, analytics and notifications per market.
- Left to the build: who besides the seller may set each setting.

**Moved:** a merchant of record selling for a store, and Sharrwah closing a store under its terms, to S-03; providers converting currencies, to S-04; a partner calculating duties, to S-05; couriers' cash on delivery and a fulfilment service's locations, to S-10.

## What moved to other subjects

Each subject decides the values. S-02 holds where each rule lives and what it is tied to: on D1 and D3, the business record's country, through one entry point.

| Subject, and what it decides | What S-02 holds for it |
| --- | --- |
| S-03: the contracting company and its law; a merchant of record; when Sharrwah may close a store | Tied to the business record's country, one company for all being one value; a merchant of record is a per-market setting; a closure by Sharrwah ranks above the seller's store status |
| S-04: payment services and providers, their checks, conversion and payouts | Tied to the business record's country; the payment methods offered are set per market (D6); under Decision 1 each provider acts on its own terms |
| S-05: tax on Sharrwah's fees, checks of tax numbers, duties partners | Tied to the business record's country; a store's tax settings follow D6 and D3 |
| S-07: countries served and kept out, documents and checks | One list the platform holds, checked wherever a country enters: a business record, a move, a market |
| S-08: one privacy policy for all stores, or not | Tied to the business record's country; one policy for all is one value |
| S-09: the currency of Sharrwah's bill to a seller | Held on Sharrwah's own billing record, not the store's country |
| S-10: couriers' cash on delivery; a fulfilment service's locations | Payment methods and stock locations are per-market settings (D6) |
| S-11: the price and currency of Sharrwah's fees | Billed apart from sellers' money, to the store's billing record; a fee that varies by country uses the one entry point |

## Engineering constraints

Proposed by engineering; you may veto any.
- **E1.** Every setting that varies by market is read through one entry point, which returns the most specific value set.
- **E2.** Every rule tied to the seller's country is read through one entry point, keyed on the business record's country.
- **E3.** Every store has one main market, which carries the store's own values.
- **E4.** A store keeps one currency of its own beside any market's.
- **E5,** *a reading:* who holds sellers' money (your decision of 26 October that it is a market's setting) is set by the seller's own country, through the business that takes the payment. The payment methods offered in each market then choose among the seller's provider accounts allowed there. C still holds everywhere at launch.
