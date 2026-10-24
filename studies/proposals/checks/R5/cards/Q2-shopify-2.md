# Cards: Q2 on shopify

16 records cited by `studies/proposals/drafts/Q2/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 27:** - For store fake-demo-sharrwah (countryCode YE), observed 30 September 2026, Shopify's admin answered Shopify Payments `"eligible":false`. The Subscribe to Plus step's saved HTML held "Shopify Payments is not available on your store." beside "0.2% third-party transaction fees apply if not using Shopify Payments", for that store, demo-fake-dev-store (30 September 2026) and capture-plus (business details: Yemen; 2 October 2026), as each step's accessibility tree did. Q2-SH-058; Q2-SH-071
- **section 1, line 28:** - For store ts15uk-ug (countryCode YE), observed 7 October 2026, the third-party providers page listed Bogus Gateway (for testing), Cybersource, Integration-UseePay, ONERWAY (Direct), PagBrasil - Cartão de crédito and Tap Payments. The same step's saved HTML held that list without ONERWAY (Direct) for fake-demo-sharrwah (30 September 2026), and without Bogus Gateway for demo-fake-dev-store (30 September 2026) and capture-plus (2 October 2026), as did the accessibility trees of the first two. Q2-SH-064; Q2-SH-072; Q2-SH-073
- **section 1, line 32:** - Shopify's contracting party is set "based on the billing address of your Store", with a row for all other jurisdictions (Shopify International Limited). Woo services come from WooCommerce Ireland Ltd. for those residing in its "Designated Countries", among them "all countries located in Europe", and from WooCommerce, Inc. for others. BigCommerce's table sets company and law per place, ending "Any other jurisdiction". They match by role, as do Shopify's and BigCommerce's rows for every remaining place. Q2-SH-K1243; Q2-SH-K1248; Q2-WC-K0499; Q2-WC-K0496; Q2-WC-K0498; Q2-BC-K0419; Q2-BC-K0425
- **section 1, line 34:** - A service can have its own company in a place: Shopify Payment Activities Inc. contracts in Canada solely for "payment activities regulated under the Canadian Retail Payment Activities Act". Q2-SH-K1615
- **section 1, line 35:** - Shopify's Terms of Service are governed by the laws of Ontario. The Stripe Services Agreement applies Regional Terms by country, and to countries it doesn't list the United States' Regional Terms in the Americas and Ireland's elsewhere (not checked on Zid). Salla's Arabic text prevails over translations (النص العربي لاتفاقية الاستخدام يظل هو الأصل), BigCommerce's English text: these match by role. Q2-SH-K1253; Q2-WC-055; Q2-SA-030; Q2-BC-015
- **section 1, line 36:** - Each platform names an agreement made directly between the seller and a provider. Shopify "is not a party to any of the Payment Processor Terms"; Stripe's Connected Account Agreement is between the seller and "the applicable Stripe entity"; with BigCommerce Payments "the merchant’s payment relationship remains directly with PayPal" (a press page); Salla calls such dealings "علاقة تعاقدية مستقلة عن منصة سلّة"; Zid is "ليست طرفًا" in logistics agreements. They match by role. Q2-SH-K1580; Q2-WC-P0103; Q2-BC-P0040; Q2-SA-004; Q2-ZD-K0347
- **section 1, line 37:** - Shopify stores new European merchants' data "at rest in Europe by default", its admin showing the Customer data hosting location. BigCommerce makes "regional hosting available", in Europe or the Asia-Pacific region rather than the United States, its primary storage being Google Cloud's U.S.-Central1. They match by role. Q2-SH-K2321; Q2-SH-031; Q2-BC-031; Q2-BC-032
- **section 1, line 43:** - Some name partners. Shopify can't support business involving certain regions "due to local regulatory requirements, commercial partnerships, and/or other pertinent factors"; WooPayments limits account types because "our partner (Stripe) strictly adheres to the laws and regulations of the country each account is based in"; a Przelewy24 change "comes directly from Przelewy24 themselves" (not checked on Zid or BigCommerce). Shopify's and WooCommerce's match by role, from an official page and a help page. Q2-SH-K2270; Q2-WC-K0405; Q2-WC-020
- **section 1, line 44:** - Some are the platform's own. Salla offers online payment "بغرض التسهيل والمحافظة على حقوق التجار والمتاجر"; Shopify's third-party transaction fees "cover the cost for Shopify to provide a secure checkout platform"; WooCommerce hides a method the customer "cannot use". Q2-SA-012; Q2-SH-K1338; Q2-WC-039
- **section 2, line 50:** - Draws on: areas within a country (Shopify's Crimea, Donetsk and Luhansk; WooPayments' states, Washington D.C. and Puerto Rico), a group (WooCommerce's Designated Countries), and defaults for unlisted places, by row (Shopify's all other jurisdictions; BigCommerce's "Any other jurisdiction") or by region (Stripe's Regional Terms), which the tree's inheritance combines. Q2-SH-K2275; Q2-WC-K0407; Q2-WC-K0496; Q2-SH-K1248; Q2-BC-K0425; Q2-WC-055
- **section 2, line 52:** - **Place reference**: which of a party's places a **Place rule** reads, each kept apart: a seller's registered country, location, document-issuing country, billing address and residence; a buyer's billing country and destination; a product's origin; a store's selling regions. Q2-WC-K0402; Q2-SH-K1243; Q2-SA-062; Q2-WC-029; Q2-SH-K2278
- **section 2, line 53:** - Draws on: WooPayments' registered country beside WooCommerce's contracting company by residence; Shopify's contracting party by billing address beside Shopify Payments' location in its Designated Country; Salla's issuing country (observed); the buyer's billing country (WooCommerce), and destinations, product origin and selling regions (Shopify). Q2-WC-K0402; Q2-WC-K0499; Q2-SH-K1243; Q2-SH-K1536; Q2-SA-062; Q2-WC-029; Q2-SH-K2279; Q2-SH-K2278; Q2-SH-K1745
- **section 2, line 59:** - **Contracting entity**: the Sharrwah company a seller contracts with, per **Place** on the **Place reference** its terms choose, and per service (the platform, a payment service, a regulated activity), each row with its governing law, forum and prevailing language. The root's row covers every other place. Q2-SH-K1243; Q2-SH-K1615; Q2-BC-K0419; Q2-BC-K0425
- **section 2, line 60:** - Draws on: Shopify's table by billing address and its Canadian company for regulated payments; BigCommerce's table with law per row; WooCommerce's split by residence; Salla's and Zid's single Saudi company, here a one-row table; the prevailing text (Arabic at Salla, English at BigCommerce). Q2-SH-K1248; Q2-SH-K1615; Q2-BC-K0425; Q2-WC-K0499; Q2-SA-033; Q2-ZD-K0212; Q2-SA-030; Q2-BC-015
- **section 2, line 64:** - Sharrwah's own choices among providers, one turning another off (Zid Pay; Salla Payments, observed) or a fee on others (Shopify; BigCommerce), are **Place rules** whose source is Sharrwah, set per **Place** (rule 1), so that one can differ where Sharrwah's own service isn't offered: for two stores registered in Yemen, the saved HTML of Shopify's Subscribe to Plus step held its third-party transaction fees beside Shopify Payments being unavailable (30 September and 2 October 2026). Whether to have any is a company decision. Q2-ZD-K0088; Q2-SA-K1653; Q2-SH-K1337; Q2-BC-K0143; Q2-SH-071
- **section 2, line 65:** - **Provider agreement**: the seller's own agreement with a **Provider**, named per **Place**. Sharrwah is not a party by default: Shopify says it isn't party to its processors' terms, and the other four name the seller's agreement as one with the provider. Q2-SH-K1580; Q2-WC-P0103; Q2-BC-P0040; Q2-SA-004; Q2-ZD-K0347
- **section 2, line 66:** - Provided for, not by default: Sharrwah as a party, as a Shopify affiliate acts as Payment Facilitator in certain Designated Countries. If that would hold sellers' money through Sharrwah, by Sharrwah or by a payment company in an account opened through Sharrwah, it goes live only by the founder's decision. Why: rule 3, partner contracts; rule 4. Q2-SH-K1603; Q2-SH-K1580
- **section 2, line 74:** - **Data location**: where a store's data, orders and customers' personal data are held, per **Place** on the seller's **Place reference**, the root's location by default, shown to the seller; with, per place, who is controller and who processor, and the basis for any transfer abroad. Q2-SH-K2321; Q2-SH-031; Q2-BC-031; Q2-BC-K0436
- **section 2, line 75:** - Draws on: Shopify's European storage by default, shown in its admin; BigCommerce's regional hosting and its processor and controller roles; WooCommerce's controller by service and location; Zid's transfers under safeguards. Why: rule 3, where data sits is expensive to change after launch, so data is placeable by region from the first build. Not taken: one fixed location, as Shopify and BigCommerce set it per place. Q2-SH-K2321; Q2-BC-031; Q2-BC-K0436; Q2-WC-K0502; Q2-ZD-K0283
- **section 3, line 88:** - Set per seller's **Place reference**: the contracting company (billing address at Shopify, residence at WooCommerce), the platform's payment service (located; registered), required documents (their issuing country), data location, tax services. Q2-SH-K1243; Q2-WC-K0499; Q2-WC-K0402; Q2-SA-K0083; Q2-SH-K2321; Q2-SH-K1865
- **section 3, line 90:** - Set per seller's legal form (Zid Pay's documents and KNET; WooPayments' UAE accounts), per service within one platform (Shopify Payments' sanctions term; Zid Pay's Saudi and Kuwaiti lists; Shopify's Canadian payments company), and per date (Przelewy24, not checked on Zid or BigCommerce). Q2-ZD-K0003; Q2-WC-K0411; Q2-ZD-K0042; Q2-SH-K2268; Q2-ZD-K0254; Q2-SH-K1615; Q2-WC-021
- **section 3, line 91:** - Set by Sharrwah, as the platform: its **Restricted places** (Shopify's, partly for commercial partnerships), its own list of goods (Salla's selling policy), its processors per place (Shopify), its exclusions among providers (Zid Pay). Q2-SH-K2270; Q2-SA-042; Q2-SH-K1561; Q2-ZD-K0088
- **section 3, line 93:** - Set by payment networks and providers: categories from Payment Network Rules and processors (Shopify); a provider's discretion over approval (Shopify's hemp providers); Przelewy24's own changes; account types Stripe limits by a country's laws (WooPayments). Q2-SH-K2262; Q2-SH-003; Q2-WC-020; Q2-WC-K0405
- **section 5, line 112:** - Which company or companies contract with sellers, under which law and forum, with which language prevailing. Keep the **Contracting entity** table with its root row, so one company now and others later are both set-ups. Settled by the company decision on where Sharrwah is based (section 7). Q2-SH-K1243; Q2-SA-033
- **section 5, line 114:** - Whether Sharrwah is a party to any payment arrangement, and whether any arrangement holds sellers' money through it. Keep each **Provider agreement** direct by default, and any holding arrangement as an option left off until the founder decides. Settled by the founder, with the company decisions in section 7. The parties of Salla's payment services contract were not in what was read. Q2-SH-K1580; Q2-SH-K1603; Q2-SA-G0177
- **section 5, line 115:** - Where a seller's data is held, and on what basis it moves. Keep **Data location** settable per place. Settled by the company decision on hosting. Q2-SH-K2321; Q2-BC-031
- **section 5, line 116:** - Which **Place reference** each rule reads for a seller. Keep the references apart. Settled rule by rule, as Sharrwah's terms and providers are chosen. Q2-WC-K0402; Q2-SH-K1243
- **section 5, line 117:** - Which providers serve which places. Keep **Availability** as dated settings: Shopify's third-party provider lists for three stores registered in Yemen, observed 30 September to 7 October 2026, differ in two providers. Settled by the company decision on partners and by each provider's own lists, as Yemen's evidence shows for Stripe. Q2-SH-064; Q2-SH-072; Q2-SH-073; YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 7, line 136:** - Where Sharrwah's company is based, and which company contracts with sellers at each place, under which law, forum and prevailing language. Q2-SH-K1243; Q2-BC-K0419; Q2-SA-020; Q2-ZD-K0212; Q2-SA-030
- **section 7, line 139:** - Whether Sharrwah is a party to sellers' payment arrangements or only connects sellers to providers; whether any holds sellers' money through Sharrwah is the founder's decision. Q2-SH-K1603; Q2-BC-P0040
- **section 7, line 140:** - Any licence Sharrwah's own activities need at a place; the platforms show their own or their partners' (Shopify's Canadian payments company, registered with the Bank of Canada; Paylink, licensed as Salla describes it, not checked on Zid or BigCommerce; Tap, authorised as Zid describes it). Sharrwah's own position is for the founder with a lawyer. Q2-SH-K1614; Q2-SA-047; Q2-ZD-K0091; YA-103 (the central bank in Aden @ the internationally recognized government's area, as of 2024-06-30)
- **section 7, line 142:** - Where sellers' and buyers' data is hosted at each place, and whether Sharrwah is its processor or its controller. Q2-SH-K2321; Q2-BC-K0436; Q2-WC-K0502

## The cards

### Q2-SH-071

**Cited at:** section 1, line 27; section 2, line 64

**Record** (`studies/proposals/records/Q2/shopify/statements.tsv`):
- stmt_id: Q2-SH-071
- bears_on: 1
- identifier: Subscribe to Plus (route plus_inactive_account:upgrade:overview)
- statement: Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments
- scope: store fake-demo-sharrwah, observed 2026-09-30; countryCode YE, currencyCode YER; store demo-fake-dev-store, observed 2026-09-30; store capture-plus, observed 2026-10-02; Business details: Yemen, Yemeni Rial (YER)
- cite_ids: Q2-SH-C077;Q2-SH-C078;Q2-SH-C079;Q2-SH-C063;Q2-SH-C080;Q2-SH-C081
- from: held
- note: In the saved HTML of step 422 of runs 20260930T002940Z-sweep-trial, 20260930T103225Z-sweep-dev and 20261002T003831Z-sweep-capture-plus (address access_account/plus/upgrade). Each step's aria.yaml shows the same words. Adds to Q2-SH-058 and Q2-SH-K1337.

**Citation Q2-SH-C077:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T002940Z-sweep-trial/422.html.txt` | run 20260930T002940Z-sweep-trial, step 422 | 2026-09-30 | kind: observed | quote check: found
- step 422: visit route plus_inactive_account:upgrade:overview (path from router) | https://admin.shopify.com/store/fake-demo-sharrwah/access_account/plus/upgrade | "Shopify" | 2026-09-30T03:17:32.864Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/422.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/422.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T002940Z-sweep-trial/422.html.txt`
- quote: Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments
- in context: … My Store [initials: MS] [alt: My Store] My Store View Dev Dashboard [accessibilitylabel: View Dev Dashboard] [initials: ds] [alt: demo fake dev store] demo fake dev store dev My Store [initials: MS] [alt: My Store] My Store My Store Create store [initials: Dd] [alt: Demo-name demo-last-name] Demo-name demo-last-name 7amza.it@gmail.com Log out [heading: Subscribe to Plus] Plus For fast growing, high-volume businesses Starting at $2,300 USD/month ⟪Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments⟫ Shopify Plus plan features Priority 24/7 support Get top-tier technical support by phone, chat, or email B2B on Shopify Sell wholesale and direct, integrated in one admin and store Custom checkout Personalize your checkout with unique discounts, shipping rates, and payment options through Shopify Functions Submit [heading: Business information] [label: Legal business name] [details: The business name that appears on your legal paperwork, such as…

**Citation Q2-SH-C078:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T103225Z-sweep-dev/422.html.txt` | run 20260930T103225Z-sweep-dev, step 422 | 2026-09-30 | kind: observed | quote check: found
- step 422: visit route plus_inactive_account:upgrade:overview (path from router) | https://admin.shopify.com/store/demo-fake-dev-store/access_account/plus/upgrade | "Shopify" | 2026-09-30T13:00:12.642Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/422.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/422.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T103225Z-sweep-dev/422.html.txt`
- quote: Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments
- in context: …fake dev store dev [initials: ds] [alt: demo fake dev store] demo fake dev store dev View Dev Dashboard [accessibilitylabel: View Dev Dashboard] [initials: MS] [alt: My Store] My Store My Store [initials: MS] [alt: My Store] My Store Create store [initials: Dd] [alt: Demo-name demo-last-name] Demo-name demo-last-name 7amza.it@gmail.com Log out [heading: Subscribe to Plus] Plus For fast growing, high-volume businesses Starting at $2,300 USD/month ⟪Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments⟫ Shopify Plus plan features Priority 24/7 support Get top-tier technical support by phone, chat, or email B2B on Shopify Sell wholesale and direct, integrated in one admin and store Custom checkout Personalize your checkout with unique discounts, shipping rates, and payment options through Shopify Functions Submit [heading: Business information] [label: Legal business name] [details: The business name that appears on your legal paperwork, such as…

**Citation Q2-SH-C079:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/422.html.txt` | run 20261002T003831Z-sweep-capture-plus, step 422 | 2026-10-02 | kind: observed | quote check: found
- step 422: visit route plus_inactive_account:upgrade:overview (path from router) | https://admin.shopify.com/store/capture-plus/access_account/plus/upgrade | "Shopify" | 2026-10-02T04:46:22.971Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/422.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/422.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/422.html.txt`
- quote: Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments
- in context: Skip to content [initials: cp] [alt: capture plus] capture plus dev [heading: Subscribe to Plus] Plus For fast growing, high-volume businesses Starting at $2,300 USD/month ⟪Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments⟫ Shopify Plus plan features Priority 24/7 support Get top-tier technical support by phone, chat, or email B2B on Shopify Sell wholesale and direct, integrated in one admin and store Custom checkout Personalize your checkout with unique discounts, shipping rates, and payment options through Shopify Functions Your Shopify Plus subscription is active. Our support can help answer any questions about your plan. Contact support

**Citation Q2-SH-C063:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/PaymentProviders/358609ed207db4bfd705bd547da93e9d4bbe461ae8217b305d7ee7fb28b8ceb5.json` | PaymentProviders, store fake-demo-sharrwah, step 164 | 2026-09-30 | kind: observed | quote check: found
- quote: "url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …tedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"GIFT_CARDS_ONLY","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store","description":null,⟪"url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/165290082519","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":true,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings":{"id":"g…

**Citation Q2-SH-C080:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt` | run 20261002T003831Z-sweep-capture-plus, step 60 | 2026-10-02 | kind: observed | quote check: found
- step 60: visit route inactive-account:checkout:select-plan (path from router) | https://admin.shopify.com/store/capture-plus/settings/general | "capture plus · General · Shopify" | 2026-10-02T01:04:39.293Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt`
- quote: capture plus - entity Yemen
- in context: …Plan G B P Go to Settings: Metafields G S M My Store 5 stores [Search] Organization Users Billing [initials: cp] [alt: capture plus] capture plus capture-plus.myshopify.com General Plan Payments Checkout Customer accounts Taxes and duties Locations Apps Sales channels Domains Notifications Metafields and metaobjects Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: General] [heading: Business details] ⟪capture plus - entity Yemen⟫ [heading: Store contact details] capture plus 7amza.it@gmail.com · No phone number Store address Yemen Submit [heading: Store defaults] Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER) [label: Backup Region] [details: Determines settings for customers outside of your markets] Canada Yemen [label: Unit system] Metric system Imperial system [label: Default weight unit] Kilogram (kg) Gram (g) [label: Time zon…

**Citation Q2-SH-C081:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt` | run 20261002T003831Z-sweep-capture-plus, step 60 | 2026-10-02 | kind: observed | quote check: found
- step 60: visit route inactive-account:checkout:select-plan (path from router) | https://admin.shopify.com/store/capture-plus/settings/general | "capture plus · General · Shopify" | 2026-10-02T01:04:39.293Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt`
- quote: Yemeni Rial (YER)
- title, opening and note boxes: as for this source's citation above
- in context: …ies Locations Apps Sales channels Domains Notifications Metafields and metaobjects Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: General] [heading: Business details] capture plus - entity Yemen [heading: Store contact details] capture plus 7amza.it@gmail.com · No phone number Store address Yemen Submit [heading: Store defaults] Currency display To manage the currencies customers see, go to Markets ⟪Yemeni Rial (YER)⟫ [label: Backup Region] [details: Determines settings for customers outside of your markets] Canada Yemen [label: Unit system] Metric system Imperial system [label: Default weight unit] Kilogram (kg) Gram (g) [label: Time zone] [details: Sets the time for when orders and analytics are recorded] To change your user level time zone and language visit your account settings [heading: Order ID format] [label: Prefix] [label: Suffix] Your order ID will…

### Q2-SH-064

**Cited at:** section 1, line 28; section 5, line 117

**Record** (`studies/proposals/records/Q2/shopify/statements.tsv`):
- stmt_id: Q2-SH-064
- bears_on: 1
- identifier: Third-party payment providers
- statement: (for testing) Bogus Gateway Cybersource Supports 3DS Integration-UseePay Supports 3DS ONERWAY (Direct) Supports 3DS PagBrasil - Cartão de crédito Tap Payments Supports 3DS
- scope: store ts15uk-ug, observed 2026-10-07; countryCode YE, currencyCode YER
- cite_ids: Q2-SH-C068;Q2-SH-C069
- from: held

**Citation Q2-SH-C068:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/387.text.txt` | step 387 (settings/payments/third-party-providers) | 2026-10-07 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/ts15uk-ug/settings/payments/third-party-providers | "My Store 8 · Payments · Third-party payment providers · Shopify" | 2026-10-07T01:16:53.596Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/387.html`, `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/387.text.txt`
- quote: (for testing) Bogus Gateway Cybersource Supports 3DS Integration-UseePay Supports 3DS ONERWAY (Direct) Supports 3DS PagBrasil - Cartão de crédito Tap Payments Supports 3DS
- in context: …ork with Sidekick My Store 6 stores [Search] Organization Users Billing MS8 My Store 8 ts15uk-ug.myshopify.com General Plan Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com Third-party payment providers Search [Filter third-party payment providers] ⟪(for testing) Bogus Gateway Cybersource Supports 3DS Integration-UseePay Supports 3DS ONERWAY (Direct) Supports 3DS PagBrasil - Cartão de crédito Tap Payments Supports 3DS⟫ Learn more about third-party payment providers Close

**Citation Q2-SH-C069:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261006T225457Z-sweep-trial-my-store-8/answers/admin.shopify.com/PaymentProviders/e2e77d781eb9362fa7263e6c56f6322b09351180fdbe58cd221eb97f97c2701d.json` | PaymentProviders, store ts15uk-ug, step 164 | 2026-10-07 | kind: observed | quote check: found
- quote: "countryCode":"YE","currencyCode":"YER"
- in context: …name":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"MANUAL","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store 8","description":null,"url":"https://ts15uk-ug.myshopify.com",⟪"countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/164899946732","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":true,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings":{"id":"g…

### Q2-SH-072

**Cited at:** section 1, line 28; section 5, line 117

**Record** (`studies/proposals/records/Q2/shopify/statements.tsv`):
- stmt_id: Q2-SH-072
- bears_on: 1
- identifier: Third-party payment providers
- statement: (for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]
- scope: store fake-demo-sharrwah, observed 2026-09-30; countryCode YE, currencyCode YER
- cite_ids: Q2-SH-C082;Q2-SH-C083;Q2-SH-C084;Q2-SH-C085;Q2-SH-C063
- from: held
- note: In the saved HTML of step 387 (address settings/payments/third-party-providers). The step's aria.yaml shows the same five provider names. The list holds no ONERWAY (Direct). Adds to Q2-SH-064.

**Citation Q2-SH-C082:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt` | run 20260930T002940Z-sweep-trial, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment written as "settings" (hypothesis from settings-nav urls); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T03:04:52.403Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt`
- quote: (for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club]
- in context: …pify.com [initials: MS] [alt: My Store] General Plan Billing Users Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: Third-party payment providers] Payments [label: Search] [placeholder: Filter third-party payment providers] ⟪(for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club]⟫ [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibi…

**Citation Q2-SH-C083:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt` | run 20260930T002940Z-sweep-trial, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment written as "settings" (hypothesis from settings-nav urls); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T03:04:52.403Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt`
- quote: [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB]
- title, opening and note boxes: as for this source's citation above
- in context: …] Demo-name demo-last-name 7amza.it@gmail.com [heading: Third-party payment providers] Payments [label: Search] [placeholder: Filter third-party payment providers] (for testing) Bogus Gateway [accessibilitylabel: Test payment gateway] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] ⟪[accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB]⟫ [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilityl…

**Citation Q2-SH-C084:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt` | run 20260930T002940Z-sweep-trial, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment written as "settings" (hypothesis from settings-nav urls); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T03:04:52.403Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt`
- quote: [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments
- title, opening and note boxes: as for this source's citation above
- in context: …] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] ⟪[accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments⟫ Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit] Learn more about third-party payment providers [heading: Keyboard Shortcuts] General shortcuts Keyboard help ? Focus save bar S Focus filter bar F Open app O A Open sales channel O C Open store O S Your profile M E Log…

**Citation Q2-SH-C085:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt` | run 20260930T002940Z-sweep-trial, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment written as "settings" (hypothesis from settings-nav urls); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/payments/third-party-providers | "My Store · Payments · Third-party payment providers · Shopify" | 2026-09-30T03:04:52.403Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T002940Z-sweep-trial/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T002940Z-sweep-trial/387.html.txt`
- quote: Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]
- title, opening and note boxes: as for this source's citation above
- in context: …S [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments ⟪Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]⟫ Learn more about third-party payment providers [heading: Keyboard Shortcuts] General shortcuts Keyboard help ? Focus save bar S Focus filter bar F Open app O A Open sales channel O C Open store O S Your profile M E Log out B Y E Adding items to your store Add product A P Add collection A C Add discount A D Add order A O Add customer A U Add blog post A B Add blog A L Add page A G Navigating your admin panel Go to Home G H Go to Orders G O Go to …

**Citation Q2-SH-C063:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/PaymentProviders/358609ed207db4bfd705bd547da93e9d4bbe461ae8217b305d7ee7fb28b8ceb5.json` | PaymentProviders, store fake-demo-sharrwah, step 164 | 2026-09-30 | kind: observed | quote check: found
- quote: "url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"
- in context: …tedOrderAction":"NOT_SET","__typename":"FraudProtectSettings"},"features":{"highRiskOrdersWithFlow":{"onboardingStage":"NEEDS_FLOW","__typename":"HighRiskOrdersWithFlow"},"__typename":"ShopFeatures","threeDSecureEligibilityForCountry":false,"sellsSubscriptions":false,"bankAccountChangesLocked":false},"checkoutSettings":{"shippingBehaviour":"GIFT_CARDS_ONLY","__typename":"CheckoutSettings"},"__typename":"Shop","name":"My Store","description":null,⟪"url":"https://fake-demo-sharrwah.myshopify.com","countryCode":"YE","currencyCode":"YER"⟫,"checkoutExtensibilityMigrationStatus":"MIGRATED","accountOwner":{"id":"gid://shopify/StaffMember/165290082519","name":"Demo-name demo-last-name","email":"7amza.it@gmail.com","__typename":"StaffMember"},"plan":{"trial":true,"shopifyPlus":false,"__typename":"ShopPlan"},"entitlements":{"multiPrimaryGateways":true,"__typename":"EntitlementsType"},"developmentShop":false,"multiLegalEntitiesPhase":"INELIGIBLE"},"paymentAuthorizationSettings":{"id":"g…

### Q2-SH-073

**Cited at:** section 1, line 28; section 5, line 117

**Record** (`studies/proposals/records/Q2/shopify/statements.tsv`):
- stmt_id: Q2-SH-073
- bears_on: 1
- identifier: Third-party payment providers
- statement: Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]
- scope: store demo-fake-dev-store, observed 2026-09-30; store capture-plus, observed 2026-10-02; Business details: Yemen
- cite_ids: Q2-SH-C086;Q2-SH-C087;Q2-SH-C088;Q2-SH-C089;Q2-SH-C090;Q2-SH-C091;Q2-SH-C080
- from: held
- note: In the saved HTML of step 387 of runs 20260930T103225Z-sweep-dev and 20261002T003831Z-sweep-capture-plus (address settings/payments/third-party-providers); both hold the same lines. The sweep-dev step's aria.yaml shows the same five provider names. The list holds no (for testing) Bogus Gateway. Adds to Q2-SH-064.

**Citation Q2-SH-C086:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt` | run 20260930T103225Z-sweep-dev, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/demo-fake-dev-store/settings/payments/third-party-providers | "demo fake dev store · Payments · Third-party payment providers · Shopify" | 2026-09-30T12:48:14.251Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt`
- quote: Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay]
- in context: …n Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: Third-party payment providers] Payments [label: Search] [placeholder: Filter third-party payment providers] ⟪Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay]⟫ [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessi…

**Citation Q2-SH-C087:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt` | run 20260930T103225Z-sweep-dev, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/demo-fake-dev-store/settings/payments/third-party-providers | "demo fake dev store · Payments · Third-party payment providers · Shopify" | 2026-09-30T12:48:14.251Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt`
- quote: [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro]
- title, opening and note boxes: as for this source's citation above
- in context: …hird-party payment providers] Payments [label: Search] [placeholder: Filter third-party payment providers] Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] ⟪[accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro]⟫ ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessi…

**Citation Q2-SH-C088:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt` | run 20260930T103225Z-sweep-dev, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/demo-fake-dev-store/settings/payments/third-party-providers | "demo fake dev store · Payments · Third-party payment providers · Shopify" | 2026-09-30T12:48:14.251Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt`
- quote: ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro]
- title, opening and note boxes: as for this source's citation above
- in context: …] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay] [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ⟪ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro]⟫ PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibility…

**Citation Q2-SH-C089:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt` | run 20260930T103225Z-sweep-dev, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/demo-fake-dev-store/settings/payments/third-party-providers | "demo fake dev store · Payments · Third-party payment providers · Shopify" | 2026-09-30T12:48:14.251Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt`
- quote: PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard]
- title, opening and note boxes: as for this source's citation above
- in context: …iscover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] ⟪PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard]⟫ [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit] Learn more about third-party payment providers [heading: Keyboard Shortcuts] General shortcuts Keyboard help ? Focus save bar S Focus filter bar F Open app O A Open sales channel O C Open store O S Your profile M E Log out B Y…

**Citation Q2-SH-C090:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt` | run 20260930T103225Z-sweep-dev, step 387 | 2026-09-30 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/demo-fake-dev-store/settings/payments/third-party-providers | "demo fake dev store · Payments · Third-party payment providers · Shopify" | 2026-09-30T12:48:14.251Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T103225Z-sweep-dev/387.html.txt`
- quote: [accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]
- title, opening and note boxes: as for this source's citation above
- in context: …bel: Diners Club] [accessibilitylabel: Visa Electron] [accessibilitylabel: Maestro] PagBrasil - Cartão de crédito [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Elo] [accessibilitylabel: Hypercard] [accessibilitylabel: Hyper] Tap Payments Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] ⟪[accessibilitylabel: American Express] [accessibilitylabel: OmanNet] [accessibilitylabel: Apple Pay] [accessibilitylabel: Mada] [accessibilitylabel: Benefit]⟫ Learn more about third-party payment providers [heading: Keyboard Shortcuts] General shortcuts Keyboard help ? Focus save bar S Focus filter bar F Open app O A Open sales channel O C Open store O S Your profile M E Log out B Y E Adding items to your store Add product A P Add collection A C Add discount A D Add order A O Add customer A U Add blog post A B Add blog A L Add page A G N…

**Citation Q2-SH-C091:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/387.html.txt` | run 20261002T003831Z-sweep-capture-plus, step 387 | 2026-10-02 | kind: observed | quote check: found
- step 387: visit route payments:settings:third-party-providers (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:third-party-providers:list) | https://admin.shopify.com/store/capture-plus/settings/payments/third-party-providers | "capture plus · Payments · Third-party payment providers · Shopify Plus" | 2026-10-02T04:24:54.004Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/387.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/387.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/387.html.txt`
- quote: Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay]
- in context: …stomer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: Third-party payment providers] [accessibilitylabel: Payments] [label: Search] [placeholder: Filter third-party payment providers] ⟪Cybersource Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: UnionPay] [accessibilitylabel: Apple Pay]⟫ [accessibilitylabel: Google Pay] Integration-UseePay Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessibilitylabel: American Express] [accessibilitylabel: Discover] [accessibilitylabel: JCB] [accessibilitylabel: Diners Club] [accessibilitylabel: Maestro] ONERWAY (Direct) Supports 3DS [accessibilitylabel: Visa] [accessibilitylabel: Mastercard] [accessi…

**Citation Q2-SH-C080:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt` | run 20261002T003831Z-sweep-capture-plus, step 60 | 2026-10-02 | kind: observed | quote check: found
- step 60: visit route inactive-account:checkout:select-plan (path from router) | https://admin.shopify.com/store/capture-plus/settings/general | "capture plus · General · Shopify" | 2026-10-02T01:04:39.293Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261002T003831Z-sweep-capture-plus/steps/060.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261002T003831Z-sweep-capture-plus/060.html.txt`
- quote: capture plus - entity Yemen
- in context: …arch] Organization Users Billing [initials: cp] [alt: capture plus] capture plus capture-plus.myshopify.com General Plan Payments Checkout Customer accounts Taxes and duties Locations Apps Sales channels Domains Notifications Metafields and metaobjects Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: General] [heading: Business details] ⟪capture plus - entity Yemen⟫ [heading: Store contact details] capture plus 7amza.it@gmail.com · No phone number Store address Yemen Submit [heading: Store defaults] Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER) [label: Backup Region] [details: Determines settings for customers outside of your markets] Canada Yemen [label: Unit system] Metric system Imperial system [la…

### Q2-SH-K1243

**Cited at:** section 1, line 32; section 2, line 52; section 2, line 53; section 2, line 59; section 3, line 88; section 5, line 112; section 5, line 116; section 7, line 136

**The same record as Q1-SH-K1243,** whose card is in `Q1-shopify-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Contracting Party. You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store.
- scope: 

### Q2-SH-K1248

**Cited at:** section 1, line 32; section 2, line 50; section 2, line 60

**Record** (`studies/proposals/records/Q2/shopify/copied.tsv`):
- concern_id: SH-C-002
- placement: responsible
- structure: https://www.shopify.com/legal/terms
- identifier: 13. Shopify Contracting Party and Forum, table row "All other jurisdictions"
- statement: Shopify International Limited, a private company limited by shares incorporated in Ireland under registration number 560279
- scope: billing address in all other jurisdictions (including EMEA, Europe, the Middle East, Africa, South America, the Caribbean, and Mexico)
- cite_ids: SH-S-0007
- note: first run's citation

**Citation SH-S-0007:** `https://www.shopify.com/legal/terms` | 13. Shopify Contracting Party and Forum, table row "All other jurisdictions" | 2026-08-01 | kind: official page | quote check: found
- quote: Shopify International Limited, a private company limited by shares incorporated in Ireland under registration number 560279
- title: Shopify Terms of Service - Shopify
- in context: …defined Section 13.4 below. 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada Asia Pacific (including Australia, New Zealand, China, Japan, and Singapore) Shopify Commerce Singapore Pte. Ltd, a corporation formed under the laws of Singapore 77 Robinson Road, #13-00 Robinson 77, Singapore 068896 Courts of Singapore All other jurisdictions (including EMEA, Europe, the Middle East, Africa, South America, the Caribbean, and Mexico) ⟪Shopify International Limited, a private company limited by shares incorporated in Ireland under registration number 560279⟫ (VAT number IE 3347697KH) The Sidings, 4th Floor, Grand Canal Quay, Dublin D02 E7K8, Ireland Courts of Ireland Billing and Collection. Shopify Inc. may act as the billing agent for Shopify Technology (USA) Inc. and/or another Shopify Contracting Party, including to collect and remit Fees and remit taxes in some jurisdictions, as applicable. Regulated Payment Services (Canada). The Shopify Contracting Party shall be Shopify Payment Activities Inc…

### Q2-SH-K1615

**Cited at:** section 1, line 34; section 2, line 59; section 2, line 60; section 3, line 90

**Record** (`studies/proposals/records/Q2/shopify/copied.tsv`):
- concern_id: SH-C-067
- placement: responsible
- structure: https://www.shopify.com/legal/terms
- identifier: 13. Shopify Contracting Party and Forum, Regulated Payment Services (Canada)
- statement: Regulated Payment Services (Canada). The Shopify Contracting Party shall be Shopify Payment Activities Inc., solely with respect to any aspect of the Services that are payment activities regulated under the Canadian Retail Payment Activities Act ("Regulated Payment Services").
- scope: Canada; aspects of the Services regulated under the Canadian Retail Payment Activities Act
- cite_ids: SH-S-0009
- note: first run's citation

**Citation SH-S-0009:** `https://www.shopify.com/legal/terms` | 13. Shopify Contracting Party and Forum, Regulated Payment Services (Canada) | 2026-08-01 | kind: official page | quote check: found
- quote: Regulated Payment Services (Canada). The Shopify Contracting Party shall be Shopify Payment Activities Inc., solely with respect to any aspect of the Services that are payment activities regulated under the Canadian Retail Payment Activities Act ("Regulated Payment Services").
- title: Shopify Terms of Service - Shopify
- in context: …onal Limited, a private company limited by shares incorporated in Ireland under registration number 560279 (VAT number IE 3347697KH) The Sidings, 4th Floor, Grand Canal Quay, Dublin D02 E7K8, Ireland Courts of Ireland Billing and Collection. Shopify Inc. may act as the billing agent for Shopify Technology (USA) Inc. and/or another Shopify Contracting Party, including to collect and remit Fees and remit taxes in some jurisdictions, as applicable. ⟪Regulated Payment Services (Canada). The Shopify Contracting Party shall be Shopify Payment Activities Inc., solely with respect to any aspect of the Services that are payment activities regulated under the Canadian Retail Payment Activities Act ("Regulated Payment Services").⟫ 14. Term and Termination Which means To initiate a termination, you must contact Support. Shopify will respond with specific information regarding the termination process for your account. Once termination is confirmed, domains purchased through Shopify will no longer be automatically renewed. If you cancel in the middle of your billing cycle, you'll have one last email invoice. We may terminate your account at any time. The term of these Terms …

### Q2-SH-K1253

**Cited at:** section 1, line 35

**Record** (`studies/proposals/records/Q2/shopify/copied.tsv`):
- concern_id: SH-C-002
- placement: responsible
- structure: https://www.shopify.com/legal/terms
- identifier: 16. General Conditions
- statement: The Terms of Service will be governed by and interpreted in accordance with the laws of the Province of Ontario and the laws of Canada applicable therein, without regard to principles of conflicts of laws.
- cite_ids: SH-S-0010
- note: first run's citation, moved from boundary: governing law of the Terms of Service is a legal placement, not a boundary of the software

**Citation SH-S-0010:** `https://www.shopify.com/legal/terms` | 16. General Conditions | 2026-08-01 | kind: official page | quote check: found
- quote: The Terms of Service will be governed by and interpreted in accordance with the laws of the Province of Ontario and the laws of Canada applicable therein, without regard to principles of conflicts of laws.
- title: Shopify Terms of Service - Shopify
- in context: …f Service, unless otherwise provided in these Terms of Service, no person or entity who is not a party to these Terms of Service will have any right to enforce any term of these Terms of Service, regardless of whether such person or entity has been identified by name, as a member of a class or as answering a particular description. For the avoidance of doubt, this will not affect the rights of any permitted assignee or transferee of these Terms. ⟪The Terms of Service will be governed by and interpreted in accordance with the laws of the Province of Ontario and the laws of Canada applicable therein, without regard to principles of conflicts of laws.⟫ The United Nations Convention on Contracts for the International Sale of Goods will not apply to these Terms of Service. The Terms of Service may be available in languages other than English. To the extent of any inconsistencies or conflicts between these English Terms of Service and Shopify's Terms of Service available in another language, the most current English version of the Terms of Service at https://www.shopify.com/legal/aup will prevail…

### Q2-SH-K1580

**Cited at:** section 1, line 36; section 2, line 65; section 2, line 66; section 5, line 114

**Record** (`studies/proposals/records/Q2/shopify/copied.tsv`):
- concern_id: SH-C-064
- placement: responsible
- structure: https://www.shopify.com/legal/terms-shopify-payments
- identifier: Part I, A. The Payment Processor
- statement: Shopify is not a party to any of the Payment Processor Terms and is not liable to you in respect thereof.
- cite_ids: SH-S-0083
- note: first run's citation

**Citation SH-S-0083:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, A. The Payment Processor | 2026-10-10 | kind: official page | quote check: found
- quote: Shopify is not a party to any of the Payment Processor Terms and is not liable to you in respect thereof.
- title: Shopify Payments Terms of Service - Shopify
- in context: … is carried out by one or more Payment Processors and any of its Financial Services Providers under the separate terms of service identified in the Payment Processor List (the "Payment Processor Terms"). By accepting this Agreement, you are also accepting and agreeing to be bound by all of the Payment Processor Terms applicable in your Designated Country, which, in each case, is a legal agreement between you and the applicable Payment Processor. ⟪Shopify is not a party to any of the Payment Processor Terms and is not liable to you in respect thereof.⟫ By accepting this Agreement and the Payment Processor Terms for your Designated Country you are agreeing to open financial accounts and/or cryptocurrency wallets with one or more Payment Processors for Payment Processing (each a "Payment Processor Account"). You authorize Shopify to determine which Payment Processor Account(s) we will facilitate opening on your behalf, and where you have multiple Payment Processor Accounts, which Payment Process…

### Q2-SH-K2321

**Cited at:** section 1, line 37; section 2, line 74; section 2, line 75; section 3, line 88; section 5, line 115; section 7, line 142

**The same record as Q1-SH-K2321,** whose card is in `Q1-shopify-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: New merchants in Europe automatically avail of this new infrastructure and now have their store data, order data and customer personal data stored at rest in Europe by default.
- scope: new merchants in Europe

### Q2-SH-031

**Cited at:** section 1, line 37; section 2, line 74

**Record** (`studies/proposals/records/Q2/shopify/statements.tsv`):
- stmt_id: Q2-SH-031
- bears_on: 2
- identifier: Customer data hosting location
- statement: In the **Customer data hosting location** section, you can find the primary location where Shopify stores your store data, order data, and customer personal data.
- cite_ids: Q2-SH-C032
- from: held

**Citation Q2-SH-C032:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/privacy-and-security/privacy/customer-privacy-settings/understanding-customer-privacy-settings.md` | Customer data hosting locations | 2026-10-16 | kind: stated | quote check: found
- quote: In the **Customer data hosting location** section, you can find the primary location where Shopify stores your store data, order data, and customer personal data.
- title: Understanding customer privacy settings in your Shopify admin
- the page opens: When you sell products through Shopify, it's crucial to comply with privacy and data protection laws and regulations that apply to your business. Privacy and data protection are fundamental aspects of ecommerce and are important to your customers. These requirements focus on data minimization, transparency, control, and security. Understanding customer privacy settings in your Shopify Admin When you log in to your Shopify admin, you can set up a privacy policy, add a cookie banner, allow visitor…
- headings: Understanding customer privacy settings in your Shopify admin > Customer data hosting locations
- in context: …t are relevant in a privacy context: * **E-mail and SMS marketing at checkout**: This feature allows you to confirm customer marketing preferences during the checkout process, ensuring compliance with privacy regulations. * **Double opt-in for marketing**: By activating this setting, you can confirm customer contact details for marketing purposes, providing an additional layer of consent and privacy protection. ## Customer data hosting locations ⟪In the **Customer data hosting location** section, you can find the primary location where Shopify stores your store data, order data, and customer personal data.⟫ To learn more about data hosting locations, you can refer to the documentation on [data hosting locations](/manual/privacy-and-security/privacy/international-data-transfers/onward-transfers#data-hosting-locations).

### Q2-SH-K2270

**Cited at:** section 1, line 43; section 3, line 91

**Record** (`studies/proposals/records/Q2/shopify/copied.tsv`):
- concern_id: SH-C-174
- placement: decides
- structure: https://help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.md
- identifier: help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.md
- statement: Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors.
- cite_ids: SH-S-0298
- note: first run's citation

**Citation SH-S-0298:** `https://help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.md` | introduction | 2026-10-10 | kind: official page | quote check: found
- quote: Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors.
- title: Unsupported countries and regions
- the page opens: Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors. The following list contains the countries and regions that aren't supported by Shopify: * Cuba * Iran * North Korea * Syria * The Crimea region of Ukraine, and the so-called Donetsk and Luhansk People's Republics in Ukraine The following restrictions apply to all users of Shopify: * Individuals and businesses within unsupported countries a…
- headings: Unsupported countries and regions
- in context: # Unsupported countries and regions ⟪Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors.⟫ The following list contains the countries and regions that aren't supported by Shopify: * Cuba * Iran * North Korea * Syria * The Crimea region of Ukraine, and the so-called Donetsk and Luhansk People's Republics in Ukraine The following restrictions apply to all users of Shopify: * Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account. * Access to storefronts and accounts is prohibite…

### Q2-SH-K1338

**Cited at:** section 1, line 44

**Record** (`studies/proposals/records/Q2/shopify/copied.tsv`):
- concern_id: SH-C-018
- placement: reason
- structure: https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/third-party-transaction-fees.md
- identifier: help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/third-party-transaction-fees.md
- statement: Third-party transaction fees cover the cost for Shopify to provide a secure checkout platform and integrate with external payment providers.
- cite_ids: SH-S-0272
- note: first run's citation

**Citation SH-S-0272:** `https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/third-party-transaction-fees.md` | introduction | 2026-10-10 | kind: stated | quote check: found
- quote: Third-party transaction fees cover the cost for Shopify to provide a secure checkout platform and integrate with external payment providers.
- title: Third-party transaction fees on your Shopify bills
- the page opens: Third-party transaction fees cover the cost for Shopify to provide a secure checkout platform and integrate with external payment providers. Transaction fees vary depending on the Shopify plan that you choose, and are charged in the following circumstances: * When you use a third-party payment provider to accept customer payments. * When an order includes store credit or gift cards as a payment method, on Shopify stores created on or after May 12, 2025. For example, if your store uses Shopify Pa…
- a note box: Note For Shopify stores created on or after May 12, 2025, orders that include store credit or gift cards as a payment method are charged third-party transaction fees on the amount paid for using store credit or gift cards. Store credit and gift card transaction fees don't apply to Shopify stores cre
- a note box: Note The Advanced Cash on Delivery app is no longer available from the Shopify App Store. You can use the standard Cash on Delivery option in your payment settings.
- a note box: Note To view third-party transaction fees for stores on the Plus plan, in your Shopify admin, go to the Billing page for your organization, and then export the bill that you want to review.
- headings: Third-party transaction fees on your Shopify bills
- in context: # Third-party transaction fees on your Shopify bills ⟪Third-party transaction fees cover the cost for Shopify to provide a secure checkout platform and integrate with external payment providers.⟫ Transaction fees vary depending on the [Shopify plan](https://www.shopify.com/pricing) that you choose, and are charged in the following circumstances: * When you use a [third-party payment provider](/manual/payments/third-party-providers) to accept customer payments. * When an order includes [store credit](/manual/customers/store-credit) or [gift cards](/manual/products/gift-card-products) as a payment method, on Shopify stores created on or af…

### Q2-SH-K1603

**Cited at:** section 2, line 66; section 5, line 114; section 7, line 139

**Record** (`studies/proposals/records/Q2/shopify/copied.tsv`):
- concern_id: SH-C-066
- placement: responsible
- structure: https://www.shopify.com/legal/terms-shopify-payments
- identifier: Part I, A. The Shopify Payments Service
- statement: In certain Designated Countries, pursuant to separate Payment Facilitator Terms, a Shopify affiliate acts as a Payment Facilitator (as defined in the Payment Facilitator Terms) to facilitate your acceptance of Transactions (as defined below).
- scope: certain Designated Countries
- cite_ids: SH-S-0081
- note: first run's citation, moved from decides: the sentence names a Shopify affiliate acting as Payment Facilitator, which answers who is responsible

**Citation SH-S-0081:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, A. The Shopify Payments Service | 2026-10-10 | kind: official page | quote check: found
- quote: In certain Designated Countries, pursuant to separate Payment Facilitator Terms, a Shopify affiliate acts as a Payment Facilitator (as defined in the Payment Facilitator Terms) to facilitate your acceptance of Transactions (as defined below).
- title: Shopify Payments Terms of Service - Shopify
- in context: …r, Grand Canal Quay, Dublin D02 E7K8, Ireland Australia, Hong Kong, Japan, New Zealand, Singapore, Shopify Commerce Singapore Pte. Ltd., organized under the laws of Singapore, with offices at 77 Robinson Road, 13-00 Robinson 77, Singapore 068896 None of the Shopify entities listed above are licensed as a bank, payment institution, or money services business, but are instead, respectively, a supplier of the Payments Services under this Agreement. ⟪In certain Designated Countries, pursuant to separate Payment Facilitator Terms, a Shopify affiliate acts as a Payment Facilitator (as defined in the Payment Facilitator Terms) to facilitate your acceptance of Transactions (as defined below).⟫ The Designated Countries where a Shopify affiliate acts as a Payment Facilitator are listed in the Payment Facilitator Terms. If your Designated Country is one where a Shopify affiliate acts as a Payment Facilitator, the Payment Facilitator Terms apply and form part of this Agreement, and you agree to the Payment Facilitator Terms by accepting this Agreement. The Payment Processor. The Payment Processor under this Agreement may be one or more of…

### Q2-SH-003

**Cited at:** section 3, line 93

**Record** (`studies/proposals/records/Q2/shopify/statements.tsv`):
- stmt_id: Q2-SH-003
- bears_on: 1
- identifier: Hemp transactions
- statement: Approval decisions are at the discretion of each third-party payment provider, and Shopify can’t guarantee the approval of your store.
- cite_ids: Q2-SH-C003
- from: held

**Citation Q2-SH-C003:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/payments.md` | Hemp transactions | 2026-10-16 | kind: stated | quote check: found
- quote: Approval decisions are at the discretion of each third-party payment provider, and Shopify can’t guarantee the approval of your store.
- title: Payment options for hemp sales on Shopify
- the page opens: Shopify Payments doesn't support the sale of hemp, cannabidiol (CBD), and tetrahydrocannabinol (THC) products. To process the sales of hemp or hemp-derived products through your Shopify store, you can use third-party payment providers that are compatible with Shopify and support the sale of these products. Hemp transactions Third-party payment providers have a thorough vetting process for stores that apply to sell hemp through their services. Each payment provider may consider various factors su…
- headings: Payment options for hemp sales on Shopify > Hemp transactions
- in context: …-party payment providers that are compatible with Shopify and support the sale of these products. ## Hemp transactions Third-party payment providers have a thorough vetting process for stores that apply to sell hemp through their services. Each payment provider may consider various factors such as product type, business creation date, transaction history, volume, and product mix when approving payments and rates for stores selling hemp products. ⟪Approval decisions are at the discretion of each third-party payment provider, and Shopify can't guarantee the approval of your store.⟫ ## Shopify Payments and third-party payment providers Currently, Shopify Payments doesn't support the sale of hemp and hemp derived CBD and THC products. However, Shopify has partnered with integrated third-party payment providers that support the sale of these products. You can use any integrated third-party payment provider that's compatible with Shopify and supports the sale of hemp products. Examples of third-party providers that you can app…

### Q2-SH-K1614

**Cited at:** section 7, line 140

**The same record as Q1-SH-K1614,** whose card is in `Q1-shopify-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Shopify Payment Activities Inc. is registered with the Bank of Canada as a Payment Service Provider under the Retail Payment Activities Act.
- scope: Canada
