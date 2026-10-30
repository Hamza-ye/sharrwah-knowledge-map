# Batch P-3: notes (S-02, S02-VP-01 to S02-VP-12)

## The run

- **A stop, then a resume.** The run stopped at S02-VP-05 when `cell` warned that C-anchor's and C-bigcommerce's model files had changed after the last merge. The coordinator merged again at a11d4727, and the run resumed from there.
- **VP-01 to VP-04 were re-checked.** They land in domain A. Between 03699d92 and the merge, `merged/cells.tsv` changed only in C's CM-PAY-006, 009, 011, 015, 016, 029 and 030, so those four rows stand as drafted.
- **The count:** 12 points, 7 landed and 5 with conflicts (8 conflicts in all).
- **The checker's final line:** `# 12 points in P-3, 0 problems`. It printed no `lead:` lines.

## The points that were hard to land

- **S02-VP-01, S02-VP-04 and S02-VP-06 (the store's country, who sets it, who changes it).**
  - The country is held in three places: the store's general settings (CM-ACC-006, on all five platforms), the sign-up (CM-ONB-001) and Shopify's business entity (CM-ACC-004).
  - I marked their reach `cross-cutting: markets and the seller's country`, as the brief's "every store a country" reads. For S02-VP-04 and S02-VP-06 this is a reading: the setter is held through configuration, but the thing set is the seller's country, which every area reads through S02-E2.
  - S02-VP-07, the conditions on a move, I marked `capability`.
- **S02-VP-05 and S02-VP-10 (who checks; what decides the documents).** The checks are split across several capabilities:
  - the payment service's verification (CM-PAY-003);
  - the business record (CM-ACC-004);
  - the sign-up (CM-ONB-001);
  - BigCommerce's billing (CM-PLN-004, for S02-VP-05);
  - Shopify's Managed Markets (CM-MKS-003) and Zid's sender name (CM-NTF-004), for S02-VP-10.
  - I landed each platform's answer where its statements sit.
- **S02-VP-08 and S02-VP-09 (the contracting party and the terms).** Both land on CM-ACC-002. Shopify's Designated Country entity and Regional Terms, the Stripe Services Agreement by Stripe Account Country, and Salla's payment services contract are the payment service's own. They land on CM-PAY-004, which holds the Payment Facilitator, the Acquirer and Stripe. Shopify's Managed Markets Terms land on CM-MKS-003. I marked both points cross-cutting ("every contract a contracting party"), under markets and the seller's country, since S02-E2 keys the contracting company on it. The coordinator may prefer to hold S-03's contracting company under a decision of its own: the architecture plan's section 3 says it is "settled with the cross-cutting decisions, or kept open there".
- **S02-VP-11 (what decides the platform's own payment service).**
  - WooCommerce's shipped code gates WooPayments' onboarding on the stored business location:
    - `WooPaymentsRestController`, under `/wc-admin/settings/payments/woopayments/onboarding`: S02-WC-224 to S02-WC-227 (shipped), S02-WC-527 and S02-WC-528 (observed).
  - I landed this on CM-PAY-001, WooCommerce's own payment settings, which is core. The alternative reading lands it on CM-PAY-002. There the WooCommerce cell is own-service and outside, with no core, and the shipped route would be a `count`. I read it as the settings page's behaviour, so I made no conflict. The coordinator should check this reading.
- **S02-VP-12 (what decides the third-party providers).**
  - I used the brief's rule for a capability per flow. Each flow lands on its own capability only where a platform's answer is that flow's alone:
    - Shopify's PayPal Express Checkout per entity: CM-PAY-013;
    - Salla's deferred payment for Kuwait: CM-PAY-015;
    - Salla's `bank_transfer.country_not_supported`: CM-PAY-030;
    - Shopify's Managed Markets local methods: CM-MKS-003.
  - BigCommerce's PayPal, Braintree and Fastlane requirements stay on CM-PAY-011. The model reads BigCommerce's PayPal gateways as CM-PAY-011's slot fillers, and its CM-PAY-013 cell says so.
  - WooCommerce's "Their billing country matches your WooPayments account country" (S02-V-294) is a WooPayments condition, not a third party's. I didn't land it on its own.

## Each conflict, with both sides

1. **S02-VP-01, `count`** (rows: S02-D1, model). WooCommerce.
   - Subject: S02-WC-294 (shipped, the core profiler's "Where is your store located?") and S02-WC-322 (WooCommerce Setup, "confirm your store location").
   - Model: the CM-ONB-001 WooCommerce cell is none-held. Its reading says no held statement shows what the onboarding profile (WC-S-0198) asks.
   - A reading: core is borne out.
2. **S02-VP-02, `count`** (rows: S02-M4, model). Salla.
   - Subject: S02-SA-492 (observed): Salla's own onboarding at /persona/qna answers Other country with "We're currently available in Saudi Arabia and the UAE...". It is built-in behaviour.
   - Model: the CM-ACC-008 Salla cell is not-stated, and all of its statements are shows (SA-C-167/decides/SA-S-0003, SA-S-0141, SA-S-3101, SA-I-1206, SA-I-1207).
   - A reading: core is borne out.
3. **S02-VP-03, `count`** (rows: S02-M4, S02-F1, model). Salla: the same S02-SA-492, behind S02-V-020, against the same cell.
4. **S02-VP-05, `placement`** (rows: S02-F3, model). Shopify.
   - Subject: S02-SH-582 (China, Early access): "WorldFirst verifies your identity and business information before Shopify Payments is activated".
   - Model: CM-PAY-003 Shopify places outside only the banking partners and Payment Processors (SH-C-068/decides/SH-S-0357, SH-S-0098, SH-C-068/responsible/SH-S-0100). WorldFirst is not among its slot fillers.
5. **S02-VP-05, `placement`** (rows: S02-M4, model). Zid.
   - Subject: S02-ZD-090, "توثيق منصة المركز السعودي للأعمال".
   - Model: CM-ACC-004 Zid cites ZD-C-035/where/ZD-S-0752 as core and holds the Saudi Business Center as a slot filler, but places no party outside.
   - What would settle it: a statement on whether Zid or the Saudi Business Center makes the check.
6. **S02-VP-05, `count`** (rows: S02-F3, model). WooCommerce.
   - Subject: S02-WC-295 (shipped) and S02-WC-530 (observed): the core profiler's own geolocation notice, "It looks like you're located in Yemen. Are you sure you want to create a store in United States (US) — California?".
   - Model: the CM-ONB-001 WooCommerce cell is none-held, as in conflict 1.
7. **S02-VP-05, `count`** (rows: S02-M3, model). BigCommerce.
   - Subject: S02-BC-277, the Account Dashboard FAQ on its VAT Information: "an issue validating the VAT number with the issuing country".
   - Model: the CM-PLN-004 BigCommerce cell is not-stated, its statements all shows (BC-I-0462, BC-C-030/where/BC-S-0184, BC-C-030/decides/BC-S-0188).
   - The coordinator may instead read the merchant's VAT number as CM-TAX-005's, whose cells hold buyers' VAT numbers.
8. **S02-VP-10, `placement`** (rows: S02-M4, model). Zid: the same as conflict 5, through S02-V-175 (S02-ZD-090 among its statements).

None of these rests on a founder's own decision. The rows are engineering's rulings (S02-D1), moved rows (M3 to S-05, M4 to S-07) and rows that follow by rule (F1, F3).

## Not conflicts, but worth the coordinator's eye

- **CM-ACC-004 joins two things.** Shopify's business entity is a record holding a country and an address. Salla's legal-entity choice (SA-S-0142, SA-S-0133) and Zid's activity type (ZD-S-0753) hold no country, as their cells show. This agrees with S02-D1's alternative (b), "a business entity holds it: Shopify". It is a possible `structure` question for a later point (S02-VP-63, S02-VP-85), not raised here, because S02-VP-01's variants don't set the two apart.
- **Shopify's "assessors".** S02-SH-589: "Business entity information is sent to assessors to verify your business". Whether the assessors are a third party isn't stated, so I made no placement conflict. A statement naming who the assessors are would settle it.
- **BigCommerce's countries served.** BigCommerce answers S02-VP-03 only through its table of contracting entities (S02-BC-066, CM-ACC-002's). I named it in the reading and didn't land it.
- **Shopify's billing address as the country.** Shopify's S02-V-003 (the store country from the billing address) belongs to platform billing. S02-D1 closes the billing address as a source of the country, so I didn't land it.

## Slot fillers the subject names that `cell` doesn't list

These are leads, not conflicts.
- **CM-ACC-008 (S02-VP-02, S02-VP-03):** BigCommerce's "any other region subject to comprehensive U.S. sanctions" (S02-BC-073). The cell lists US sanctions and OFAC only for WooCommerce.
- **CM-PAY-003 (S02-VP-05):**
  - WorldFirst on Shopify (S02-SH-582);
  - Shopify's banking partners (S02-SH-573, S02-SH-580), which the cell places outside but doesn't list as a slot filler;
  - Stripe on WooCommerce is already listed.
- **CM-ACC-004 (S02-VP-05):** SPL's national address proof on Zid (S02-ZD-085), required for some services such as payments. A reading: it is the document the merchant supplies, so no placement.
- **CM-PLN-004 (S02-VP-05):** the VAT number's issuing country on BigCommerce (S02-BC-277).
- **CM-PAY-004 (S02-VP-09):** Salla's payment services contract, signed during verification (S02-SA-146, S02-SA-152), names no counterparty.

## Problems with the brief or the script

- **The warning came from a working tree changed mid-run.** No view of S02-VP-01 to S02-VP-04 printed it, so a drafter can't tell from those views that something changed. The check runs per call, and it caught the change.
- **`show` clips a lead's basis** ("+26 more"). `leads` doesn't print the full basis either. I took the keys from the lines shown and from `cell`. The checker accepted them.
