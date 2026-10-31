# A-backfill-woocommerce: notes

## What this part did

A-woocommerce added five capabilities to domain A: CM-ACC-009 (the site hidden before launch, coming-soon mode, under CM-ACC-006), CM-ACC-010 (connecting the store to the platform company's account for its services), CM-ACC-011 (the licence of the platform's software), CM-ONB-004 (store setup in the admin: the setup wizard, the onboarding profile and the setup tasks) and CM-TRU-021 (store data sent from the merchant's own site to the platform company). This part writes their ten cells for Shopify and Salla. It adds no capabilities, lands no concerns, and writes no rulings, qualities or slot fillers: no cited statement gives a quality or a filler.

For each platform I ran `candidates --domain A --areas ACC,ONB,TRU`, read the leads with `key`, and searched further with `search` for the thing itself: a store closed to visitors until it opens, or a password page; an account with the platform's company that the store connects to; the terms under which the merchant may use the platform's software; the steps or checklist the admin gives a new store; data the platform collects about how the store uses it. Salla was searched in English and in Arabic, each Arabic term in its singular and its plural, with and without ال. The terms are in each cell's `searched`.

All ten cells are `none-held`. `none-held` means only that the concern map holds nothing found by those terms; it never means the platform lacks the capability. Each row is a reading unless it quotes a statement.

| Capability | Shopify | Salla |
|---|---|---|
| CM-ACC-009 coming-soon mode | none-held | none-held |
| CM-ACC-010 connection to the company's account | none-held | none-held |
| CM-ACC-011 software licence | none-held | none-held |
| CM-ONB-004 store setup in the admin | none-held | none-held |
| CM-TRU-021 store data sent to the company | none-held | none-held |

## The readings

- **CM-ACC-009.** The candidates by WooCommerce's terms hold nothing on either platform. Shopify: its hits are account and Theme Access passwords, the plan line Test new features before launch (CM-EVO-001's), and the entitlement `storefront.enabled` on Online Store routes (SH-S-5031, SH-S-5364), which gates routes on the store having a storefront, not its visibility before launch (a reading). Salla: its hits are maintenance mode (SA-S-1726, SA-S-2084), the theme component `salla-maintenance-alert` (SA-S-1467, readme empty) and the review of ready stores before they are published (SA-S-5111, domain F's demo stores). Kept apart from CM-ACC-007, maintenance mode, as the brief's message says: no held statement says what Salla's maintenance mode does to the storefront, so none shows it is the same as a mode for a store before launch, and Q1's U-069 stays `apart`. The definition of a coming-soon mode isn't stated for Shopify or Salla.
- **CM-ACC-010.** Shopify: the store is created under the Shopify Account itself (SH-C-001/boundary/SH-S-0229, CM-ACC-001's); the organization settings and third-party accounts created at sign-up (PayPal Express Checkout, SH-S-0022) aren't a connection of the store to a separate account with Shopify. Salla: its hits are plan lines for connecting the store to third parties' services and the App Maker's apps on Salla's accounts in mobile app stores (SA-S-5035), which aren't the store's connection to Salla's company.
- **CM-ACC-011.** Shopify: the Shopify API License and Terms of Use (SH-C-156/boundary/SH-S-0214) binds app developers' use of the API, which is domain F's; the licence in SH-S-0042 is the merchant's to Shopify for their Materials, the other direction. Salla: its hits are trade, freelance and marketing licences held by merchants or partners, intellectual property in apps, and the heading اتفاقية الاستخدام (SA-I-1201), whose text isn't held. On both hosted platforms the merchant's terms with the platform are CM-ACC-002's; no held statement states a licence of software to the merchant.
- **CM-ONB-004.** Shopify: every `onboarding` hit is onboarding to Shopify Payments, Balance or Credit (domain C); the sign-up form is CM-ONB-001's; the staff permission Home > Home (SH-I-0867) names the page, not a setup guide on it. Salla: the candidates `apps-onboarding` (SA-S-3440, SA-C-194) and App Onboarding (SA-S-1095, CM-APP-006's) are onboarding to apps. A help article calls the store's verification one of the last steps to prepare the store to work in the UAE (SA-C-006/boundary/SA-S-0137); it is about verification, cited in CM-PAY-003, and names no wizard, profile or tasks of the admin, so it isn't cited (a reading).
- **CM-TRU-021.** Shopify and Salla run the store on their own service, so no statement holds a flow of the store's data from a site the merchant runs. The hits are buyers' tracking by web pixels and advertising pixels, the processing of the merchant's customers' data (Shopify's Data Processing Addendum, Salla's store privacy pages), Salla's sharing of the store's data with a payment or shipping company at the merchant's request (SA-S-0109, SA-S-5048), sync with third parties, and the analytics the store sees. None is data the platform collects about how the store uses it.

## Gaps

- Shopify's privacy policy is held only as headings, among them How we use "cookies" and other tracking technologies (SH-I-2406); Salla's privacy policy (SA-I-1203) and usage agreement (SA-I-1201) are held only as headings. Their text would say whether either platform collects data about the store's use of it (CM-TRU-021) or grants a licence to use its software (CM-ACC-011).
- The seed's leads "home setup" (Shopify) and "help: New store" (Salla) aren't held as statements; a page on Shopify's setup guide or Salla's new-store help would settle CM-ONB-004.
- Shopify's Online Store > Preferences page and any password page aren't held; they would settle CM-ACC-009 for Shopify. For Salla, a definition of maintenance mode would say whether it is CM-ACC-009's thing too.

## The checker's flags

The checker flags every cell: `none-held`, with statements matching its searched terms or the other platforms' terms. Each cell's `reading` names the hits and why none is cited; the counts are large because the terms are short (password, launch, setup, sync, tracking, licence, ضمان). No flag is left unanswered.
