# H-008: Shopify's markets per plan, its business types, and the checkout's address form per buyer country

**Repository:** observed-sh. **Instruments:** the repository's own dev stores, each on its own plan (`index/instruments.json`): demo-fake-dev-store (Basic), capture-grow (Grow), capture-advanced (Advanced) and capture-plus (Plus). For the checkout, any one of them whose online store has a product.

**What to capture:**
1. **Markets past the first, on each plan.** On each of the four stores, Settings > Markets: create one more market of each kind the page offers, past the first (a country or region market, a B2B market, a retail market, a channel market), and a submarket. Record what the page allows, and any limit or upgrade message it shows, with the store's plan. Delete what was created at the end, where the page allows it.
2. **Business types.** On one store, Settings > General > Business details: the business types the form offers for a business entity. For each type the form saves without a document, record whether Settings > Markets, Managed Markets (the `markets/managed*` routes) and assigning a market to a business entity are offered. Restore the entity's type at the end.
3. **The checkout's address form, per buyer country.** On one store, add these countries to a market, where they aren't in one: Saudi Arabia, the United Arab Emirates, Japan, Brazil, Italy and the United States. Then, as a buyer with a product in the cart, open the checkout and choose each country in the delivery address in turn. Record the form as shown for each: its fields, their order and labels, which are required, and the answers the checkout fetches when the country changes. Remove the countries added at the end.

**Stop before** paying, subscribing to a plan, activating Shopify Payments or Managed Markets for real, accepting any agreement, submitting identity or business documents, or anything that charges.

**Already held:**
- the Help Center's and plan pages' statements on markets per plan (`studies/subjects/S-02/shopify/statements.tsv`, S02-SH-689, S02-SH-697, S02-SH-703, S02-SH-704, S02-SH-706, S02-SH-707): every plan includes an unlimited number of country or region markets; Shopify B2B is offered on the Basic, Grow, Advanced and Plus plans, with up to 3 active catalogs across all B2B markets on Basic and unlimited B2B catalogs on Plus; and the number of markets depends on the plan. None gives a number of B2B, retail or channel markets, or of submarkets, per plan;
- the market journey on a store based in Yemen (run `20260930T170204Z-journey-market`): one market, for Saudi Arabia;
- the business details journey (run `20261006T213517Z-journey-business-details-save`), whose address service answer holds every country's address format as the admin asks for it (S02-SH-665 to S02-SH-687);
- a buyer's checkout (run `20260930T025819Z-journey-buyer-checkout`), whose countries answer holds each country's name, code and phone prefix only (S02-SH-688);
- the Help Center's pages that tie business types to payment methods and to Shopify Payments (S02-SH-632, S02-SH-635, S02-SH-640, S02-SH-643), not to Markets.

**Why:** S-02, root decisions 2 and 3: how many markets of each kind a store can hold on each plan (gap S02-SH-G07); for which business types Markets, Managed Markets and per-market business entities are offered (S02-SH-G08); and the address format the checkout applies for each buyer's country (S02-SH-G06). The gaps are in `studies/subjects/S-02/shopify/gaps.tsv`.

**Needs:** nothing from the founder. The stores are the repository's own dev stores.

**Done when** runs hold, for each of the four plans, what Settings > Markets allows past one market of each kind; the business types offered, and what each changes in Markets; and the checkout's address form for each of the six countries. Or they show where each stops.
