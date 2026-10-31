# H-007: how Shopify sets a store's country at sign-up, and checks it when it changes

**Repository:** observed-sh. **Instruments:** a new Shopify account made for this run, and a capture store that doesn't use Shopify Payments.

**What to capture:**
1. **A sign-up whose "I'm located in:" differs from where the network is:** choose a country other than Yemen, such as the United States, while the network is in Yemen (or the reverse). Then record the new store's Settings > General (store address, store currency, backup region) and its business details (business entity, its country).
2. **On a capture store that doesn't use Shopify Payments:** change the country of its business entity in Settings > General > Business details. Record whether verification is asked, what evidence, and what the page says will change, to the store address among it. Stop before submitting any identity or business document.

   *Narrowed on 27 October 2026* by the audit of Shopify's claims of absence (`studies/subjects/S-02/shopify/absence-audit.tsv`, S02-SH-G01, partly contradicted). The billing address's country can't be changed on its own: its dialog disables the field (S02-SH-598), and it must match an active entity's country (S02-SH-253). The Help Center says that changing the store's country creates a new business entity, which the store address then follows (S02-SH-593, S02-SH-594). It says that adding or changing an entity "might require additional verification", and that entity information "is sent to assessors" (S02-SH-589, S02-SH-590). What isn't held is whether a check is made, and what is asked, on a store that uses no financial services.

The new store from step 1 may serve as the store H-006 asks for, if its country is one where Managed Markets can be activated.

**Stop before** submitting identity or business documents, accepting any agreement, activating Shopify Payments, or anything that charges. Changes to a capture store's address are reversed at the end, where the page allows it.

**Already held:**
- the Help Center's page on business entities, read in the absence audit (S02-SH-589 to S02-SH-597);
- what the sign-up sends: `SignupMutation`'s `storeCreatePayload` with `"country": "YE"` and empty address fields (S02-SH-599);
- a sign-up with Yemen chosen, from a network in Yemen (run `20261006T232216Z-journey-signup-new-account`): the store took YE as its country, its billing address's country and its billing account's country;
- a store made while Shopify saw the browser in the United Kingdom, which still took Yemen from its organization (run `20261005T002448Z-journey-dev-store-region`);
- switching a store's business entity to a US one, which says the store address will update, then stops (run `20261004T223401Z-journey-business-entity`).

**Why:** S-02, root decision 1, the store's own country: what sets it at sign-up, and who checks it when it changes (gaps S02-SH-G01 and S02-SH-G02, in `studies/subjects/S-02/shopify/gaps.tsv`).

**Needs:** nothing from the founder, beyond an email address for the new account if the local agent has none.

**Done when** runs hold the sign-up and its store's settings, and the address changes up to any check, or show where each stops.
