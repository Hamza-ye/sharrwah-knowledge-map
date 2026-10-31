# H-006: Shopify's admin as a store based outside Yemen sees it

**Repository:** observed-sh. **Instrument:** a store set up for this, whose business entity, store address and currency are in a country where the held Help Center says Managed Markets can be activated. Its own example is a business based in the United States, with a store currency of USD (`manual/international/managed-markets/requirements-and-considerations.md`).

**What to capture,** on that store, as observed runs:
1. Settings > General: the store address, business entity, store currency and backup region.
2. Markets: the markets the store starts with, then create one for another country, and record what each part offers: conditions, currency, domain or subfolder, catalogs, duties, and the business entity assigned.
3. Managed Markets (the `markets/managed*` routes): whether it can be activated, and the steps up to activation.
4. Payments: which payment providers Settings > Payments offers this store, Shopify Payments among them.
5. Business entities: assigning a market to a business entity, if offered.

**Stop before** activating Shopify Payments or Managed Markets for real, accepting any agreement, entering real tax or identity numbers, or anything that charges.

**Already held,** every one on stores based in Yemen with the rial:
- the market journey (run `20260930T170204Z-journey-market`: a market for Saudi Arabia, SAR, /en-sa, duties, a catalog);
- the business-entity region test (run `20261004T223401Z-journey-business-entity`: switching to a US entity says the store address will update, then stops);
- a store made while Shopify saw the browser in the United Kingdom, which still took Yemen from its organization (run `20261005T002448Z-journey-dev-store-region`);
- `docs/GAPS.md`, the row "Other countries (store is Yemen)", deferred by the founder on 5 October; capture requests now go to the local agent as handoffs (`founder-decisions.tsv`, 27 October).

**Why:** S-02, root decisions 1 and 3: what Shopify binds to a store's country (payments, Managed Markets, business entities, taxes), and which settings a market takes, observed from a country other than Yemen. Every Shopify store held is based in Yemen, so what turns on with another country has been seen only in Shopify's help pages.

**Needs:** a store set up for this in another country. If that needs a business entity Shopify verifies, stop where it asks for verification, and say so.

**Done when** runs hold the five parts above on a store based outside Yemen, or show where each stops.
