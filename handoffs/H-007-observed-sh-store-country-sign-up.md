# H-007: how Shopify sets a store's country at sign-up, and checks it when it changes

**Repository:** observed-sh. **Instruments:** a new Shopify account made for this run, and a capture store that doesn't use Shopify Payments.

**What to capture:**
1. **A sign-up whose "I'm located in:" differs from where the network is:** choose a country other than Yemen, such as the United States, while the network is in Yemen (or the reverse). Then record the new store's Settings > General (store address, store currency, backup region) and its business details (business entity, its country).
2. **On a capture store that doesn't use Shopify Payments:** change the country of the store address in Settings > General, then of the billing address. Record whether a check is made, what evidence is asked, and what the page says will change. Stop before submitting any identity or business document.

The new store from step 1 may serve as the store H-006 asks for, if its country is one where Managed Markets can be activated.

**Stop before** submitting identity or business documents, accepting any agreement, activating Shopify Payments, or anything that charges. Changes to a capture store's address are reversed at the end, where the page allows it.

**Already held:**
- a sign-up with Yemen chosen, from a network in Yemen (run `20261006T232216Z-journey-signup-new-account`): the store took YE as its country, its billing address's country and its billing account's country;
- a store made while Shopify saw the browser in the United Kingdom, which still took Yemen from its organization (run `20261005T002448Z-journey-dev-store-region`);
- switching a store's business entity to a US one, which says the store address will update, then stops (run `20261004T223401Z-journey-business-entity`).

**Why:** S-02, root decision 1, the store's own country: what sets it at sign-up, and who checks it when it changes (gaps S02-SH-G01 and S02-SH-G02, in `studies/subjects/S-02/shopify/gaps.tsv`).

**Needs:** nothing from the founder, beyond an email address for the new account if the local agent has none.

**Done when** runs hold the sign-up and its store's settings, and the address changes up to any check, or show where each stops.
