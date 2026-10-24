# Cards: Q6 on bigcommerce

9 records cited by `studies/proposals/drafts/Q6/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 14:** - The contracting company follows the seller's place on three platforms, a match on role, all in their terms: Shopify contracts "based on the billing address of your Store"; BigCommerce keys its table to "Country of Residence of Merchant", with a row for "Any other jurisdiction"; WooCommerce: "If you reside outside of the Designated Countries: WooCommerce, Inc." The keys overlap only in part, a billing address or residence. BigCommerce adds terms that "supplement, replace or modify" its own for customers domiciled where they list. Q6-SH-K1243; Q6-BC-008; Q6-BC-K0425; Q6-WC-K0498; Q6-BC-010
- **section 1, line 16:** - Places barred, a match on role among three, all on their legal pages: "Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account"; WooCommerce bars sellers "located or residing in any country or territory subject to comprehensive US sanctions"; BigCommerce bars nationals and residents of Iran, Cuba, North Korea, Syria, Crimea and other regions under comprehensive US sanctions. Shopify's grounds are "local regulatory requirements, commercial partnerships, and/or other pertinent factors". Q6-SH-K1270; Q6-WC-K0526; Q6-BC-K0430; Q6-SH-K2270
- **section 1, line 17:** - Screening: BigCommerce puts "sanctions screenings of your Relevant Parties and customers" on the seller; Shopify's screening interface was not found, and who screens for Zid Pay is open. Q6-BC-K0431; Q6-SH-G0217; Q6-ZD-G0055
- **section 1, line 20:** - Verification as a gate, a match on role: without Salla's verification "يتم تعليق عمليات الدفع والسداد", and on "باقة بيسك" "التحقق متطلب أساسي للبدء في عملية البيع"; for store store-sherawya, observed 8 October 2026, Salla's payment data gave `"blocks_payment_activation": true`. On BigCommerce's payment service, funds "may be held or blocked", and the seller is told to complete any requests for documents or verification. Q6-SA-037; Q6-SA-036; Q6-SA-061; Q6-BC-P0084
- **section 1, line 27:** - What a seller elsewhere uses, a match on role: on Shopify, a third-party provider, for which Shopify charges transaction fees by plan while "Your third-party payment provider charges you their credit card rates themselves, separately."; on Zid, by its Gulf store-creation article, Tap: "يمكنك تفعيل بوابة الدفع تاب من خلال الاعدادات > طرق الدفع"; on Salla, for a store outside Saudi Arabia, Tabby: "تواصل مع تابي مباشرة لاستكمال إعداد حساب التاجر". On BigCommerce, "Each provider has its own application process." Q6-SH-024; Q6-ZD-K0090; Q6-SA-056; Q6-BC-P0048
- **section 1, line 30:** - Other parts limited by place, a match on role: Zid's financing is "متاح لتجار المملكة العربية السعودية فقط"; BigCommerce's digital wallets depend on "your store’s country and currency combination"; Shopify's sales channels on "your region, product types, and sometimes your subscription plan" (not checked on BigCommerce). Q6-ZD-K0177; Q6-BC-022; Q6-SH-030
- **section 1, line 33:** - Saying so for one part, a match on role with Salla's notice: WooCommerce asks sellers to "vote for your country to be supported", and weighs "the number of requests by WooCommerce store owners in that country"; BigCommerce says of its payment service "Additional regions and countries will be launching soon."; these are help pages, Salla's notice observed. Q6-WC-007; Q6-WC-K0403; Q6-BC-P0030; Q6-SA-007
- **section 2, line 47:** - **Contracting company map**: which Sharrwah company contracts with a Seller, chosen by its **Business place**, with a row for any other place, and each place's supplement to the seller terms. It follows Shopify, BigCommerce and WooCommerce, which choose the company by the seller's place, and BigCommerce's supplements. It sits behind its own part (rule 2), and its structure is decided now (rule 3: legal structure and partner contracts); with one company, it has one row. Not taken: one company written into the terms, as Salla's and Zid's terms read, since adding a company later would then touch every seller's contract. Q6-SH-K1243; Q6-BC-008; Q6-BC-K0425; Q6-WC-K0498; Q6-BC-010; Q6-SA-023; Q6-ZD-K0214
- **section 2, line 48:** - **Verification**: checks in stages, each opening particular capabilities, with requirements set per place and entity type in the **Place set-up**. First, the Account user's phone at sign-up. Second, the Seller entity's identity and documents, before Sharrwah activates any part that takes payments or pays out, as Salla's payment data showed `"blocks_payment_activation": true` for store store-sherawya on 8 October 2026, and WooCommerce has sellers verify with Stripe when they sign up for its payments. Third, a provider's own checks when it plugs in. A store can be built and opened before the second stage, as on Zid, where a commercial registration is needed only to connect payment gateways; whether the second stage comes before any selling, as on Salla's "باقة بيسك", is set per place in the **Place set-up** (rule 1). Q6-SA-061; Q6-WC-K0393; Q6-ZD-K0241; Q6-SA-036; Q6-BC-P0048
- **section 2, line 49:** - Gating activation, not money: Sharrwah takes no payment for a seller before the second stage, rather than suspending payments and settlement afterwards, as Salla's FAQ describes, or holding funds, as BigCommerce's payment service may. Either would hold sellers' money, and under the guard could go live only by the founder's decision. Rule 3: money flows are decided now. Q6-SA-037; Q6-BC-P0084
- **section 2, line 51:** - **Part availability**: for each part Sharrwah offers, its own or a provider's, where it is available: the places, and, where the evidence shows a second key, the currencies, plans and product types; with a reason when a seller can't use it. Zid limits a part by place, BigCommerce adds currency, Shopify plan and product type, and Salla's payment data, observed for store real-merchant on 12 October 2026, carry per method `"available_countries": []` and `"unavailable_reason": null`. Rule 2: availability is data per part, so opening a part in a new place changes no code. Q6-ZD-K0177; Q6-BC-022; Q6-SH-030; Q6-SA-062
- **section 2, line 52:** - **Provider choice**: for each place, the providers Sharrwah offers there for each kind of part, payments first, in order; the seller picks and connects one, and each provider approves the seller itself. It follows WooCommerce's list per country, Shopify's third-party providers where its own service isn't available, and BigCommerce's application process per provider. Where Sharrwah has no payment service of its own, this list is how a seller takes online payments, as Shopify's admin showed `"thirdPartyDirectEligible":true` for store ts15uk-ug, with its entity in Yemen, on 7 October 2026; two Yemen stores' records name the same six third-party providers, Tap Payments among them. A payment service of Sharrwah's own, as each platform has, is not decided here: section 5 keeps it open under the guard. Q6-WC-K0054; Q6-SH-022; Q6-BC-P0048; Q6-SH-037; Q6-SH-041; Q6-SH-048
- **section 3, line 60:** - Plugs in: payment providers, and providers of other parts such as pay-later, each with its own places, approval and rules, as BigCommerce's application process, Zid's gateway approval and Salla's direct Tabby account show. Q6-BC-P0048; Q6-ZD-K0003; Q6-SA-056
- **section 3, line 64:** - Set per Business place: the contracting company and the terms supplements, as on Shopify, BigCommerce and WooCommerce. Q6-SH-K1243; Q6-BC-008; Q6-WC-K0498; Q6-BC-010
- **section 3, line 66:** - Set per part: availability by place; by place and currency, as BigCommerce's wallets; by plan and product type, as Shopify's sales channels; by business category, as Shopify's own payment service. Q6-BC-022; Q6-SH-030; Q6-SH-022
- **section 3, line 69:** - Each provider sets its own places, approval and checks, as on BigCommerce and Zid. Q6-BC-P0048; Q6-ZD-K0003
- **section 3, line 71:** - The company, with the founder, sets which regimes the **Restricted places** follow and which company contracts where (section 7), as WooCommerce and BigCommerce name the regime theirs follow. Q6-WC-K0526; Q6-BC-K0430
- **section 5, line 88:** - Which address decides what: the place of registration on Salla, observed for store store-sherawya on 8 October 2026, and on WooCommerce, residence on BigCommerce, the billing address on Shopify, the seller's or inventory's location on Zid. The design records each address apart, and each rule names the address it reads; the company decision on contracting, with a lawyer's advice to the founder, settles which address keys the contract. Q6-SA-059; Q6-WC-K0402; Q6-BC-008; Q6-SH-K1243; Q6-ZD-K0231
- **section 5, line 91:** - Which places are restricted, and who screens: the platforms' lists differ, Shopify's screening interface was not found, who screens for Zid Pay is open, and BigCommerce puts screening on the seller. The US designation of a party in Yemen, not of Yemen as a place, means the screening must look at parties as well as places. The design keeps the lists as data, per regime and per provider, with a screening step on places and parties at sign-up and before payments; the company decision on regimes and on a screening partner settles it. Q6-WC-K0526; Q6-ZD-035; Q6-SH-G0217; Q6-ZD-G0055; Q6-BC-K0431; YA-27 (FTO and SDGT @ the United States' area, as of 2025-03-05)
- **section 5, line 92:** - A payment service or wallet of Sharrwah's own: Salla suspends payments and settlement until a store is verified, and BigCommerce's payment service holds a new account's first payments before payout. The design keeps payments behind **Provider choice**, so that such a service, if the founder decides on one, plugs in as one more provider; under the guard, nothing that holds sellers' money goes live without the founder's decision. Q6-SA-037; Q6-BC-P0084
- **section 6, line 99:** - **Part availability**, a second key: at Kuraimi's E-Pay service, as of 2026-10-10, the payment API accepts customers by rial zone, old, new or all. This allows **Part availability** to carry a currency zone as its second key, as BigCommerce's wallets carry currency. YK-452 (by currency zone, old, new or all @ E-Pay (Kuraimi Islamic Microfinance Bank)'s service, as of 2026-10-10); Q6-BC-022
- **section 7, line 112:** - Which company contracts with sellers in Yemen, where it is based, and under which law. Q6-SH-K1243; Q6-BC-K0425; Q6-WC-K0498; Q6-ZD-K0211
- **section 7, line 113:** - Which sanctions regimes and lists Sharrwah applies, at registration and to each part, and who screens. Q6-WC-K0526; Q6-BC-K0431; Q6-ZD-035; Q6-SH-G0217
- **section 7, line 118:** - Whether Sharrwah offers a payment service of its own, or any arrangement holding sellers' money, anywhere: under the guard, only by the founder's decision. Q6-SA-037; Q6-BC-P0084

## The cards

### Q6-BC-008

**Cited at:** section 1, line 14; section 2, line 47; section 3, line 64; section 5, line 88

**Record** (`studies/proposals/records/Q6/bigcommerce/statements.tsv`):
- stmt_id: Q6-BC-008
- bears_on: 1
- identifier: Country of Residence of Merchant
- statement: Country of Residence of Merchant
- cite_ids: Q6-BC-C008
- from: held

**Citation Q6-BC-C008:** `https://www.commerce.com/terms/` | Contracting Entity: table, first column heading | 2026-06-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/108-commerce.com/text.txt` (fetched 2026-10-12T04:20:53Z, captured)
- quote: Country of Residence of Merchant
- title: Master Services Agreement | Commerce
- in context: Master Services Agreement | Commerce Master Services Agreement Date of Last Revision: June 1, 2026 ⟪Country of Residence of Merchant⟫ Commerce Entity Governing Law Services United States Commerce.com US, Inc., a Texas corporation in the United States New York Ecommerce Platform, Extensions, and certain Professional Services United Kingdom Commerce Software UK Ltd., a United Kingdom limited company England and Wales Ecommerce Platform, Extensions, and certain Professional Services European Union Commerce Software Ireland Ltd., an Irish limited company Ireland Ecommerce Platform…

### Q6-BC-K0425

**Cited at:** section 1, line 14; section 2, line 47; section 7, line 112

**The same record as Q1-BC-K0425,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Any other jurisdiction Commerce.com Pty. Ltd., an Australia proprietary limited company New York Ecommerce Platform, Extensions, and certain Professional Services
- scope: Country of Residence of Merchant: Any other jurisdiction

### Q6-BC-010

**Cited at:** section 1, line 14; section 2, line 47; section 3, line 64

**Record** (`studies/proposals/records/Q6/bigcommerce/statements.tsv`):
- stmt_id: Q6-BC-010
- bears_on: 1
- identifier: Incorporated Terms – Jurisdiction-Specific Terms
- statement: The following terms supplement, replace or modify the referenced terms for Customers domiciled in the jurisdictions below.
- cite_ids: Q6-BC-C010
- from: held

**Citation Q6-BC-C010:** `https://www.commerce.com/terms/jurisdiction-specific-terms/` | Incorporated Terms – Jurisdiction-Specific Terms (preamble) | 2025-10-17 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/115-commerce.com/text.txt` (fetched 2026-10-12T04:21:00Z, captured)
- quote: The following terms supplement, replace or modify the referenced terms for Customers domiciled in the jurisdictions below.
- title: Jurisdiction-Specific Terms | Commerce
- in context: … FeedonomicsFeedonomics MakeswiftMakeswift United States AboutAbout CareersCareers PressPress ContactContact Become an investorBecome an investor Incorporated Terms - Jurisdiction-Specific Terms Date of Last Revision: October 17, 2025 The terms below are incorporated into, and form an integral part of, the Commerce Master Services Agreement. Unless otherwise defined herein, capitalized terms shall have the meaning ascribed them in the Agreement. ⟪The following terms supplement, replace or modify the referenced terms for Customers domiciled in the jurisdictions below.⟫ EMEA. European Union and United Kingdom. For Customers domiciled within the European Union or the United Kingdom: Arbitration. The 'Arbitration Agreement and Class Action Waiver' section of the Agreement is supplemented with the following two additional provisions:| Internal Dispute Resolution. If you are a business established within the European Union or the United Kingdom, you are also eligible to make use of our internal dispute resolution p…

### Q6-BC-K0430

**Cited at:** section 1, line 16; section 3, line 71

**The same record as Q2-BC-K0430,** whose card is in `Q2-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: are not, and will ensure that your Relevant Parties and customers are not, (a) nationals, residents, agents or representatives of Iran, Cuba, North Korea, Syria, the Crimea Region of Ukraine, or any other region subject to comprehensive U.S. sanctions
- scope: 

### Q6-BC-K0431

**Cited at:** section 1, line 17; section 5, line 91; section 7, line 113

**The same record as Q2-BC-K0431,** whose card is in `Q2-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: shall implement an effective, risk-based compliance program and necessary internal controls (including, but not limited to, conducting sanctions screenings of your Relevant Parties and customers)
- scope: 

### Q6-BC-P0084

**Cited at:** section 1, line 20; section 2, line 49; section 5, line 92; section 7, line 118

**Record** (`studies/proposals/records/Q6/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-083
- bullet: c
- placement: decides
- identifier: FAQ: Troubleshooting and support: Why are some of my funds held or otherwise unavailable for payout?
- statement: Why are some of my funds held or otherwise unavailable for payout? Funds may be held or blocked for several reasons, depending on different factors. Check the Actions section for any notifications and complete any requests for documents or verification. For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal’s New PayPal account – payments on hold and accessing your money quicker. If you have added the requested account details and the funds are still held or blocked, contact PayPal support.
- cite_ids: S01-BC-C124;S01-BC-C125;S01-BC-C126;S01-BC-C127
- from: new

**Citation S01-BC-C124:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 633: FAQ, Troubleshooting and support | 2026-10-13 | kind: stated | quote check: found
- quote: Why are some of my funds held or otherwise unavailable for payout?
- in context: … need additional assistance with setting up your account, contact PayPal support. Why did my refund fail? Insufficient funds are a common cause for failed refunds. As refunds are issued from your BigCommerce Payments balance rather than linked bank accounts, your balance may have been too low for the refund to be successful. Note that failed refunds cannot be retried in the BigCommerce control panel and must be completed in the PayPal dashboard. ⟪Why are some of my funds held or otherwise unavailable for payout?⟫ Funds may be held or blocked for several reasons, depending on different factors. Check the Actions section for any notifications and complete any requests for documents or verification. For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal's New PayPal account - payments on hold and accessing your money quicker. If you have added the requested accou…

**Citation S01-BC-C125:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 635: FAQ, Troubleshooting and support | 2026-10-13 | kind: stated | quote check: found
- quote: Funds may be held or blocked for several reasons, depending on different factors. Check the Actions section for any notifications and complete any requests for documents or verification.
- in context: …ayPal support. Why did my refund fail? Insufficient funds are a common cause for failed refunds. As refunds are issued from your BigCommerce Payments balance rather than linked bank accounts, your balance may have been too low for the refund to be successful. Note that failed refunds cannot be retried in the BigCommerce control panel and must be completed in the PayPal dashboard. Why are some of my funds held or otherwise unavailable for payout? ⟪Funds may be held or blocked for several reasons, depending on different factors. Check the Actions section for any notifications and complete any requests for documents or verification.⟫ For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal's New PayPal account - payments on hold and accessing your money quicker. If you have added the requested account details and the funds are still held or blocked, contact PayPal support. Why do I see different balances in the BigCommerce Payments Balance dashboard and my PayPal account? The balanc…

**Citation S01-BC-C126:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 637: FAQ, Troubleshooting and support | 2026-10-13 | kind: stated | quote check: found
- quote: For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal’s New PayPal account – payments on hold and accessing your money quicker.
- in context: …thing about it changes. Your new BigCommerce Payments account is what processes and settles all transactions made through your BigCommerce store going forward. You can view your BigCommerce Payments account through your Balance dashboard. You can also access it by logging in to your PayPal account, clicking your business name in the upper left, and in the pop-up window, clicking on your BigCommerce Payments account under Platform accounts. Note: ⟪For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal's New PayPal account - payments on hold and accessing your money quicker.⟫ I linked the wrong PayPal account. How do I switch my configuration to the correct account? To switch the PayPal account that is linked to BigCommerce Payments, you must disconnect your current configuration and reconnect the BigCommerce Payments integration. To disconnect BigCommerce Payments, go to Settings › Payments and select the appropriate currency from the drop-down list. Under the Embedded tab, click Online Payment Methods, then click t…

**Citation S01-BC-C127:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 639: FAQ, Troubleshooting and support | 2026-10-13 | kind: stated | quote check: found
- quote: If you have added the requested account details and the funds are still held or blocked, contact PayPal support.
- in context: … or otherwise unavailable for payout? Funds may be held or blocked for several reasons, depending on different factors. Check the Actions section for any notifications and complete any requests for documents or verification. For new BigCommerce Payments accounts, initial payments are held for up to 21 days before being available for payout. For more information, see PayPal's New PayPal account - payments on hold and accessing your money quicker. ⟪If you have added the requested account details and the funds are still held or blocked, contact PayPal support.⟫ Why do I see different balances in the BigCommerce Payments Balance dashboard and my PayPal account? The balance in the BigCommerce control panel displays funds from your BigCommerce Payments account while your PayPal business account contains any other funds, including funds transferred by automatic payout. To access your BigCommerce Payments funds, go to Finance › BigCommerce Payments in the BigCommerce control panel. To access your PayPal fun…

### Q6-BC-P0048

**Cited at:** section 1, line 27; section 2, line 48; section 2, line 52; section 3, line 60; section 3, line 69

**The same record as Q1-BC-P0048,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Each provider has its own application process. 3. Apply and configure Apply with your chosen provider, complete underwriting, then add them in your BigCommerce dashboard under Store Setup, Payments.
- scope: 

### Q6-BC-022

**Cited at:** section 1, line 30; section 2, line 51; section 3, line 66; section 6, line 99

**Record** (`studies/proposals/records/Q6/bigcommerce/statements.tsv`):
- stmt_id: Q6-BC-022
- bears_on: 2
- identifier: Digital wallets
- statement: Note that digital wallet availability depends on your store’s country and currency combination.
- scope: BigCommerce Payments
- cite_ids: Q6-BC-C022
- from: held

**Citation Q6-BC-C022:** `https://support.bigcommerce.com/s/article/Connecting-with-BigCommerce-Payments?language=en_US` | BigCommerce Payments: Payment Methods: Digital Wallets | 2026-10-13 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261013T003518Z-s01-a2-sources/items/016-support.bigcommerce.com/text.txt` (fetched 2026-10-13T00:35:36Z, captured)
- captured: `evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` (fetched 2026-10-13T05:39:50Z, captured)
- quote: Note that digital wallet availability depends on your store’s country and currency combination.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …vacy display option is right for your business? We highly recommend consulting your legal advisor to ensure you are displaying the necessary information at checkout. Note that our support team is not qualified to give advice on regional privacy requirements. DIGITAL WALLETS Under Payment Methods, the Digital Wallets section lets you manage the PayPal button and other digital wallet payment methods that appear at checkout and on storefront pages. ⟪Note that digital wallet availability depends on your store's country and currency combination.⟫ PayPal Checkout - Check to add PayPal a button to product, cart, and checkout pages. PayPal will also appear as a payment option on the payment step of checkout. When enabled, shoppers will be able to pay using their PayPal account. Venmo*† - Check to accept Venmo payments. Only available for USD. Stored payment methods and recurring payments are not supported. Google Pay*† - Check to accept Google Pay payments. Note that Google Pay can only be …

### Q6-BC-P0030

**Cited at:** section 1, line 33

**The same record as Q1-BC-P0030,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Initially, BigCommerce Payments is available only to US- and UK-based merchants with self-serve and retail plans. Additional regions and countries will be launching soon.
- scope: US- and UK-based merchants with self-serve and retail plans
