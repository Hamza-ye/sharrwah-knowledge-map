# Batch P-3: notes (S-02, S02-VP-01 to S02-VP-12), stopped partway

**Status: stopped at S02-VP-05.** While I was drafting it, `land_points.py cell` and `check` started printing: "C-anchor's model files changed after the last merge: stop, and tell the coordinator to merge again before landing on domain C" (the same for C-bigcommerce). At the start of the run the working tree was clean (HEAD 03699d92). Later, `git status` showed uncommitted changes I didn't make: `method/check_class_part.py`, `method/class_merge.py`, `method/class_slice.py`, `method/km_page.py`, and `studies/class-model/parts/C-anchor/` and `C-bigcommerce/` (cells, derived, evidence, slot-fillers). The brief says to stop on this warning. So `P-3.tsv` holds S02-VP-01 to S02-VP-04, which all land on domain A (ACC, ONB). S02-VP-05 to S02-VP-12 are not drafted. The views for VP-01 to VP-04 were read before the warning appeared: none of them printed it.

## The points drafted

- **S02-VP-01 (what fills "store country"):** landed on CM-ACC-006 (store details, where all five hold the country and the address), CM-ONB-001 (the country given at sign-up) and CM-ACC-004 (Shopify's business entity). Reach is cross-cutting (markets and the seller's country): every store has a country.
  - **Conflict, count on WooCommerce.** The subject's side:
    - S02-WC-294, shipped: the core profiler's "Where is your store located?".
    - S02-WC-322: WooCommerce Setup's "confirm your store location".
    - The model's rules place these core on CM-ONB-001.
  - The model's side: the CM-ONB-001 WooCommerce cell is none-held. Its reading says no held statement shows what the onboarding profile (WC-S-0198) asks.
  - A reading: the statements bear out core.
  - Not a conflict, a reading: CM-ACC-004 joins two things.
    - Shopify's business entity is a record that holds a country and an address.
    - Salla's legal-entity choice (SA-S-0142, SA-S-0133) and Zid's activity type (ZD-S-0753) hold no country, as their cells show.
    - S02-D1's alternative (b), "a business entity holds it: Shopify", agrees with this. The coordinator may want to see it as a possible `structure` question for S02-VP-63 or S02-VP-85.
  - Shopify's S02-V-003 (the country from the billing address) answers in platform billing (CM-PLN-004). I didn't add that capability: S02-D1 closes the billing address as a source of the country.
- **S02-VP-02 (countries kept out):** landed on CM-ACC-008, kind open.
  - **Conflict, count on Salla.** The subject's side: S02-SA-492 (observed) is Salla's own onboarding stopping an "Other country" at sign-up, which the model's rules place core. The model's side: the Salla cell is not-stated, and every statement it cites is shows.
  - Shopify's, WooCommerce's and BigCommerce's statements are terms and help, so they support no placement, as the cells hold.
  - **Slot-filler leads.** CM-ACC-008 lists only WooCommerce's US sanctions and OFAC. The subject also names:
    - BigCommerce's "any other region subject to comprehensive U.S. sanctions" (S02-BC-073);
    - Shopify's list of unsupported countries and regions (S02-SH-273, S02-SH-274), which names no law.
- **S02-VP-03 (countries served):** landed on CM-ACC-008.
  - **Conflict, count on Salla:** the same S02-SA-492, which also sits behind S02-V-020.
  - BigCommerce answers through its table of contracting entities by the merchant's jurisdiction (S02-BC-066, "Any other jurisdiction: Commerce.com Pty. Ltd."), which is CM-ACC-002's thing. I named it in the reading and didn't land it there: the table names entities, not a list of countries served.
- **S02-VP-04 (who sets "location"):** landed on the same three capabilities as VP-01, with no conflict.
  - The seller, a staff permission (Shopify's legal-entity permissions, BigCommerce's Manage Settings) and the platform's default (BigCommerce's `store_country` default United States, WooCommerce's `US:CA`) are each the platform's own core.
  - No third party sets the location.
  - CM-ACC-006 wasn't among this point's leads: its route is `search`, with keys from its WooCommerce and BigCommerce cells.

## S02-VP-05, read but not drafted

These were read before or across the change. They need checking against the merged model.
- **Capabilities:**
  - CM-PAY-003, payment onboarding and verification, domain C. It holds Shopify's banking partners, WorldFirst, WooPayments' Stripe, Zid's activation, and Salla's store verification reviewed by Salla's team (SA-S-0134).
  - CM-ACC-004: Zid's Saudi Business Center and Shopify's "assessors", S02-SH-589.
  - CM-ONB-001: WooCommerce's core-profiler geolocation check, S02-WC-295 and S02-WC-530. This would again be a count against the none-held WooCommerce cell.
  - CM-PLN-004: BigCommerce validating the account's VAT number, S02-BC-277.
- **A possible placement conflict on Shopify.** WorldFirst verifies the business before Shopify Payments in China (S02-SH-582, Early access). The CM-PAY-003 Shopify cell places banking partners and Payment Processors outside, but not WorldFirst.
- **Slot-filler leads:**
  - Shopify's banking partners (S02-SH-573, S02-SH-580), which the cell places outside but doesn't list as a slot filler;
  - WorldFirst;
  - SPL's national address proof on Zid (S02-ZD-085);
  - the VAT number's issuing country on BigCommerce (S02-BC-277).

## For the coordinator

- Merge again, or say whether the uncommitted changes to domain C and to `method/` are meant to stand. Then the batch can resume from S02-VP-05.
- The checker passes the four rows drafted. Its last line was "# 4 points in P-3, 8 problems", the 8 being the undrafted points.
