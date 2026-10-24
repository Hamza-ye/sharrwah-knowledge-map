# Cards: Q6 on woocommerce

12 records cited by `studies/proposals/drafts/Q6/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 9:** - Entity types: Salla and Zid name the same four in the same words, a match on term: Salla's "فرداَ, مؤسسة, شركة, أو جمعية خيرية" and Zid's "فرد، مؤسسة، شركة، جمعية خيرية". For country code YE, Shopify's admin offered an "Individual" type, observed for store ctcbwa-r1 on 30 September 2026; the same day, the saved markup's text of store ibx5bt-xy's organization step held two Yemen entities, one "Company" and one "Individual", words its accessibility tree also showed. The types differ by place: Salla's Saudi individual type is "للمواطنين السعوديين فقط", and on WooCommerce "Businesses in the United Arab Emirates (UAE) do not have access to the Individual account type." Q6-SA-026; Q6-ZD-K0239; Q6-SH-K2674; Q6-SH-045; Q6-WC-006
- **section 1, line 10:** - The seller's place: Shopify, Salla, Zid and WooCommerce each ask where the seller is, a match on role, but key it differently. Shopify's sign-up has a location field, observed on 6 October 2026, and its billing address "must match the country of one of your active business entities"; in store ibx5bt-xy, observed 30 September 2026, the saved markup's text of the billing-address step holds two legal entities marked "YE" and "Country/region [Yemen] Yemen", words its accessibility tree also showed. Salla's onboarding, observed for store store-sherawya on 8 October 2026, asks "Where is your business based?" with `"is_mandatory": true`, meaning "the country where your business is legally registered or where you issue official documents". For WooPayments the country is "the one where your business is registered — not the one in which you personally live". Zid asks for "تحديد موقعك أو موقع المخزون". The store records are observed, the others help pages. Q6-SH-043; Q6-SH-K1259; Q6-SH-046; Q6-SA-059; Q6-WC-K0402; Q6-ZD-K0231
- **section 1, line 12:** - Places below a country: WooCommerce records "The country and state or province, if any, in which your business is located.", and Shopify's restrictions name "The Crimea region of Ukraine, and the so-called Donetsk and Luhansk People’s Republics in Ukraine". Q6-WC-011; Q6-SH-K2275
- **section 1, line 14:** - The contracting company follows the seller's place on three platforms, a match on role, all in their terms: Shopify contracts "based on the billing address of your Store"; BigCommerce keys its table to "Country of Residence of Merchant", with a row for "Any other jurisdiction"; WooCommerce: "If you reside outside of the Designated Countries: WooCommerce, Inc." The keys overlap only in part, a billing address or residence. BigCommerce adds terms that "supplement, replace or modify" its own for customers domiciled where they list. Q6-SH-K1243; Q6-BC-008; Q6-BC-K0425; Q6-WC-K0498; Q6-BC-010
- **section 1, line 16:** - Places barred, a match on role among three, all on their legal pages: "Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account"; WooCommerce bars sellers "located or residing in any country or territory subject to comprehensive US sanctions"; BigCommerce bars nationals and residents of Iran, Cuba, North Korea, Syria, Crimea and other regions under comprehensive US sanctions. Shopify's grounds are "local regulatory requirements, commercial partnerships, and/or other pertinent factors". Q6-SH-K1270; Q6-WC-K0526; Q6-BC-K0430; Q6-SH-K2270
- **section 1, line 21:** - Who verifies differs: on Salla, "يقوم فريق سلة بمراجعة طلب التوثيق."; on Zid the documents go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and Zid Pay needs the store owner to pass Nafath; WooCommerce sellers "verify your personal and business information with Stripe". Q6-SA-K0087; Q6-ZD-K0003; Q6-ZD-K0261; Q6-WC-K0393
- **section 1, line 22:** - Changing place, a match on role, Zid's in its terms and Shopify's in its help: Shopify requires deactivating "all financial services before you can change your store's country", and Zid "تصفير رصيد المحفظة أولاً". For WooPayments "there isn’t a way to update the country". Q6-SH-006; Q6-ZD-K0230; Q6-WC-020
- **section 1, line 26:** - The platform's own payment service is limited to listed places, a match on role: Shopify sends the seller to a third-party provider "If your country isn't listed, or if Shopify Payments doesn't support your business category"; Zid Pay is "متاح لتجار المملكة العربية السعودية و دولة الكويت", in an answer dated 16 July 2024; WooPayments is for "an individual or business based in one of our supported countries". Q6-SH-022; Q6-ZD-K0005; Q6-WC-K0400
- **section 1, line 28:** - WooCommerce keeps its suggestions as "The payment extension list for each country.", in which `'YE'` names only `self::VISA`. Q6-WC-K0054; Q6-WC-K0333
- **section 1, line 33:** - Saying so for one part, a match on role with Salla's notice: WooCommerce asks sellers to "vote for your country to be supported", and weighs "the number of requests by WooCommerce store owners in that country"; BigCommerce says of its payment service "Additional regions and countries will be launching soon."; these are help pages, Salla's notice observed. Q6-WC-007; Q6-WC-K0403; Q6-BC-P0030; Q6-SA-007
- **section 2, line 41:** - **Seller entity**: the registered business, or the individual, that a Seller trades as: its type, its place of registration, its documents and its bank details. The types offered are set per place, since Salla limits its individual type to Saudi citizens and WooCommerce gives UAE businesses none; Salla's and Zid's four shared types are the starting list; for Yemen, the saved markup's text of store ibx5bt-xy's organization step held a company and an individual, on 30 September 2026. A Seller may hold several entities, as Shopify's billing rule speaks of "one of your active business entities" and that step held two; the first build gives each store one, and the data model keeps more (rule 3). Q6-SH-K1260; Q6-SA-026; Q6-ZD-K0239; Q6-WC-006; Q6-SH-045; Q6-SH-K1259
- **section 2, line 42:** - **Business place**: the place a Seller's business is based, which sets its requirements, its contracting company and the parts open to it. For a registered business it is where the business is registered, following Salla's question, observed for store store-sherawya on 8 October 2026, and WooCommerce's rule; for an individual, where they reside and trade, as Shopify's age rule reads. Sharrwah asks it at sign-up and requires it, as Salla does, offering the places Sharrwah has set up and an option for any other. Rules 1 and 3. Q6-SA-059; Q6-WC-K0402; Q6-SH-001
- **section 2, line 44:** - **Place set-up**: for each place Sharrwah serves, one record of what differs there: whether registration is open; the entity types and the documents each needs; the age of majority; the contracting company and any supplement to the terms; the parts available, with their providers in order; and the wording of notices. This is rule 1, following Salla's country choice that sets legal requirements, in its dashboard strings, Zid's requirements by type and country, Shopify's billing address and WooCommerce's list per country. Q6-SA-008; Q6-ZD-K0240; Q6-SH-013; Q6-WC-K0054
- **section 2, line 45:** - A place is a country, or a region within one, since WooCommerce records a state or province and Shopify's restrictions name regions of one country. Section 6 adds what Yemen's evidence shows. Q6-WC-011; Q6-SH-K2275
- **section 2, line 46:** - **Restricted places**: lists of places from which Sharrwah takes no registration, or serves no part, each naming the regime or provider it comes from and what it bars, as Shopify's bar on creating an account does. The lists sit behind their own part (rule 2), since the platforms' lists differ and Shopify's grounds include commercial partnerships as well as regulation. A provider may bring its own list for its part, as Zid Pay's Kuwait terms name "اليمن"; such a list bars that part, not registering. Which regimes Sharrwah follows is a company decision (section 7). Q6-SH-K1270; Q6-SH-K2270; Q6-WC-K0526; Q6-ZD-035
- **section 2, line 47:** - **Contracting company map**: which Sharrwah company contracts with a Seller, chosen by its **Business place**, with a row for any other place, and each place's supplement to the seller terms. It follows Shopify, BigCommerce and WooCommerce, which choose the company by the seller's place, and BigCommerce's supplements. It sits behind its own part (rule 2), and its structure is decided now (rule 3: legal structure and partner contracts); with one company, it has one row. Not taken: one company written into the terms, as Salla's and Zid's terms read, since adding a company later would then touch every seller's contract. Q6-SH-K1243; Q6-BC-008; Q6-BC-K0425; Q6-WC-K0498; Q6-BC-010; Q6-SA-023; Q6-ZD-K0214
- **section 2, line 48:** - **Verification**: checks in stages, each opening particular capabilities, with requirements set per place and entity type in the **Place set-up**. First, the Account user's phone at sign-up. Second, the Seller entity's identity and documents, before Sharrwah activates any part that takes payments or pays out, as Salla's payment data showed `"blocks_payment_activation": true` for store store-sherawya on 8 October 2026, and WooCommerce has sellers verify with Stripe when they sign up for its payments. Third, a provider's own checks when it plugs in. A store can be built and opened before the second stage, as on Zid, where a commercial registration is needed only to connect payment gateways; whether the second stage comes before any selling, as on Salla's "باقة بيسك", is set per place in the **Place set-up** (rule 1). Q6-SA-061; Q6-WC-K0393; Q6-ZD-K0241; Q6-SA-036; Q6-BC-P0048
- **section 2, line 52:** - **Provider choice**: for each place, the providers Sharrwah offers there for each kind of part, payments first, in order; the seller picks and connects one, and each provider approves the seller itself. It follows WooCommerce's list per country, Shopify's third-party providers where its own service isn't available, and BigCommerce's application process per provider. Where Sharrwah has no payment service of its own, this list is how a seller takes online payments, as Shopify's admin showed `"thirdPartyDirectEligible":true` for store ts15uk-ug, with its entity in Yemen, on 7 October 2026; two Yemen stores' records name the same six third-party providers, Tap Payments among them. A payment service of Sharrwah's own, as each platform has, is not decided here: section 5 keeps it open under the guard. Q6-WC-K0054; Q6-SH-022; Q6-BC-P0048; Q6-SH-037; Q6-SH-041; Q6-SH-048
- **section 2, line 53:** - Two arrangements are possible: the seller contracts with the provider directly, as Salla tells stores outside Saudi Arabia to do with Tabby, or an account is opened through the platform, as WooPayments signup creates a Stripe Express account. Under the guard, an arrangement in which a provider holds sellers' money in an account opened through Sharrwah goes live only by the founder's decision. Q6-SA-056; Q6-WC-K0393
- **section 2, line 55:** - **Place interest list**: a seller from a place not set up can leave its details and be told when Sharrwah opens there, as Salla's strings promise; the requests count toward which places come next, as WooCommerce counts them. Q6-SA-007; Q6-WC-K0403
- **section 2, line 56:** - **Change of place**: how a Seller moves its Business place: parts tied to the old place, and above all any money, are closed or settled first, as Shopify and Zid require; then the new place's set-up, contracting company and verification apply. WooCommerce's answer for its payments, no change at all, is not taken, since Sharrwah's places are to grow. Rule 3: money flows and legal structure. Q6-SH-006; Q6-ZD-K0230; Q6-WC-020
- **section 3, line 61:** - Plugs in: identity checks run by others, as Zid Pay requires Nafath and WooCommerce verifies with Stripe. Q6-ZD-K0261; Q6-WC-K0393
- **section 3, line 62:** - Plugs in: restricted-place lists from a regime or a provider, as WooCommerce follows US sanctions and Zid Pay has lists by terms country. The screening tool behind such lists was not found on Shopify, and who screens is open on Zid. Q6-WC-K0526; Q6-ZD-035; Q6-SH-G0217; Q6-ZD-G0055
- **section 3, line 64:** - Set per Business place: the contracting company and the terms supplements, as on Shopify, BigCommerce and WooCommerce. Q6-SH-K1243; Q6-BC-008; Q6-WC-K0498; Q6-BC-010
- **section 3, line 67:** - Sharrwah sets the places, the **Place set-up**, the **Contracting company map** and the provider lists, and applies the **Restricted places**, as Shopify sets its own bar and contracting table and WooCommerce its lists per country. Q6-SH-K1270; Q6-SH-K1243; Q6-WC-K0054
- **section 3, line 71:** - The company, with the founder, sets which regimes the **Restricted places** follow and which company contracts where (section 7), as WooCommerce and BigCommerce name the regime theirs follow. Q6-WC-K0526; Q6-BC-K0430
- **section 5, line 87:** - What a place is below the country: WooCommerce records a state or province, and Shopify's restrictions name regions of a country. In Yemen, payment providers from one area may operate in the other only with separate infrastructure there. The design keeps places as a hierarchy, a country and the regions within it, so that a rule can attach at either level; Yemen's areas of control are its first use (section 6), and each place's entry settles the levels it needs. Q6-WC-011; Q6-SH-K2275; YK-124 (only with separate infrastructure in the other area @ Aden, as of 2024-04-05)
- **section 5, line 88:** - Which address decides what: the place of registration on Salla, observed for store store-sherawya on 8 October 2026, and on WooCommerce, residence on BigCommerce, the billing address on Shopify, the seller's or inventory's location on Zid. The design records each address apart, and each rule names the address it reads; the company decision on contracting, with a lawyer's advice to the founder, settles which address keys the contract. Q6-SA-059; Q6-WC-K0402; Q6-BC-008; Q6-SH-K1243; Q6-ZD-K0231
- **section 5, line 90:** - Who verifies: Salla's own team, or the payment provider on Zid and WooCommerce. The design keeps **Verification** behind an interface that a Sharrwah review or a provider's check can fill; partner contracts settle it. Q6-SA-K0087; Q6-ZD-K0003; Q6-WC-K0393
- **section 5, line 91:** - Which places are restricted, and who screens: the platforms' lists differ, Shopify's screening interface was not found, who screens for Zid Pay is open, and BigCommerce puts screening on the seller. The US designation of a party in Yemen, not of Yemen as a place, means the screening must look at parties as well as places. The design keeps the lists as data, per regime and per provider, with a screening step on places and parties at sign-up and before payments; the company decision on regimes and on a screening partner settles it. Q6-WC-K0526; Q6-ZD-035; Q6-SH-G0217; Q6-ZD-G0055; Q6-BC-K0431; YA-27 (FTO and SDGT @ the United States' area, as of 2025-03-05)
- **section 6, line 100:** - **Provider choice**, providers from outside Yemen: as of 2026-10-10, Stripe's service is unavailable for payments from or to Yemen, and an account in Yemen cannot receive money through PayPal's service. This forbids, at those services and that date, a provider built on either as the way a seller in Yemen is paid, WooPayments' Stripe Express account among them. YA-62 (Unavailable @ Stripe's service, as of 2026-10-10); YK-514 (cannot receive money @ PayPal's service, as of 2026-10-10); Q6-WC-K0393
- **section 6, line 102:** - **Restricted places**: the United States designates a party, Ansarallah, as an FTO and SDGT, as of 2025-03-05, not Yemen as a place; WooCommerce's list of places under comprehensive US sanctions doesn't name Yemen. Zid Pay's Kuwait terms name "اليمن", and Stage 1 found Zid Pay Kuwait unavailable for Yemen as of 2026-10-10: this forbids that part, at that service and date, to a seller in Yemen; in Sharrwah's design such a list bars the part, not registering. YA-27 (FTO and SDGT @ the United States' area, as of 2025-03-05); YA-62 (Unavailable @ Zid Pay Kuwait (Zid)'s service, as of 2026-10-10); Q6-WC-K0526; Q6-ZD-035
- **section 7, line 112:** - Which company contracts with sellers in Yemen, where it is based, and under which law. Q6-SH-K1243; Q6-BC-K0425; Q6-WC-K0498; Q6-ZD-K0211
- **section 7, line 113:** - Which sanctions regimes and lists Sharrwah applies, at registration and to each part, and who screens. Q6-WC-K0526; Q6-BC-K0431; Q6-ZD-035; Q6-SH-G0217
- **section 7, line 115:** - Which payment providers and other partners Sharrwah works with in each place, and whether any would hold sellers' money in an account opened through Sharrwah, which goes live only by the founder's decision. Q6-SH-041; Q6-SH-048; Q6-WC-K0333; Q6-WC-K0393; Q6-SA-056

## The cards

### Q6-WC-006

**Cited at:** section 1, line 9; section 2, line 41

**Record** (`studies/proposals/records/Q6/woocommerce/statements.tsv`):
- stmt_id: Q6-WC-006
- bears_on: 1
- identifier: Restrictions on account types
- statement: Businesses in the United Arab Emirates (UAE) do not have access to the Individual account type.
- scope: United Arab Emirates (UAE)
- cite_ids: Q6-WC-C006
- from: held

**Citation Q6-WC-C006:** `https://woocommerce.com/document/woopayments/compatibility/countries/` | Restrictions on account types | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/054-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:03Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/086-woocommerce.com/text.txt` (fetched 2026-10-12T10:50:57Z, captured)
- quote: Businesses in the United Arab Emirates (UAE) do not have access to the Individual account type.
- title: WooPayments in Your Country Documentation - WooCommerce
- in context: … supported. Outlying territories of the U.S. A business must be located in the 50 states, Washington D.C., or Puerto Rico to sign up with WooPayments as a U.S. business. Businesses based in any other US territory, possession, etc. are not supported. Restrictions on account types Some countries do not have access to all account types because our partner (Stripe) strictly adheres to the laws and regulations of the country each account is based in. ⟪Businesses in the United Arab Emirates (UAE) do not have access to the Individual account type.⟫ Engaging in any commercial activities typically requires a trade license or permit in the UAE. Therefore, only the Business account type is available for the UAE. Other countries In support of creating a global commerce platform, the WooCommerce team is actively working to make WooPayments available to other countries. We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store o…

### Q6-WC-K0402

**Cited at:** section 1, line 10; section 2, line 42; section 5, line 88

**The same record as Q1-WC-K0402,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: NOTE: If you’re using WooPayments for a business, the relevant country is the one where your business is registered — not the one in which you personally live.
- scope: 

### Q6-WC-011

**Cited at:** section 1, line 12; section 2, line 45; section 5, line 87

**Record** (`studies/proposals/records/Q6/woocommerce/statements.tsv`):
- stmt_id: Q6-WC-011
- bears_on: 1
- identifier: woocommerce_default_country
- statement: 'title' => __( 'Country / State', 'woocommerce' ), 'desc' => __( 'The country and state or province, if any, in which your business is located.', 'woocommerce' ), 'id' => 'woocommerce_default_country', 'default' => 'US:CA',
- cite_ids: Q6-WC-C011
- from: held

**Citation Q6-WC-C011:** `woocommerce-11.2.1:includes/admin/settings/class-wc-settings-general.php` | lines 162-165 | 2026-10-09 | kind: shipped | quote check: found
- quote: 'title' => __( 'Country / State', 'woocommerce' ), 'desc' => __( 'The country and state or province, if any, in which your business is located.', 'woocommerce' ), 'id' => 'woocommerce_default_country', 'default' => 'US:CA',
- in context: …ess line 2', 'woocommerce' ), 'desc' => __( 'An additional, optional address line for your business location.', 'woocommerce' ), 'id' => 'woocommerce_store_address_2', 'default' => '', 'type' => 'text', 'desc_tip' => true, ), array( 'title' => __( 'City', 'woocommerce' ), 'desc' => __( 'The city in which your business is located.', 'woocommerce' ), 'id' => 'woocommerce_store_city', 'default' => '', 'type' => 'text', 'desc_tip' => true, ), array( ⟪'title' => __( 'Country / State', 'woocommerce' ), 'desc' => __( 'The country and state or province, if any, in which your business is located.', 'woocommerce' ), 'id' => 'woocommerce_default_country', 'default' => 'US:CA',⟫ 'type' => 'single_select_country', 'desc_tip' => true, ), array( 'title' => __( 'Postcode / ZIP', 'woocommerce' ), 'desc' => __( 'The postal code, if any, in which your business is located.', 'woocommerce' ), 'id' => 'woocommerce_store_postcode', 'css' => 'min-width:50px;', 'default' => '', 'type' => 'text', 'desc_tip' => true, ), array( 'type' => 'sectionend', 'id' => 'store_address', ), array( 'title' => __( 'General options', 'woocommerce' ),…

### Q6-WC-K0498

**Cited at:** section 1, line 14; section 2, line 47; section 3, line 64; section 7, line 112

**The same record as Q2-WC-K0498,** whose card is in `Q2-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: If you reside outside of the Designated Countries: WooCommerce, Inc.
- scope: residents outside the Designated Countries

### Q6-WC-K0526

**Cited at:** section 1, line 16; section 2, line 46; section 3, line 62; section 3, line 71; section 5, line 91; section 6, line 102; section 7, line 113

**The same record as Q2-WC-K0526,** whose card is in `Q2-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: (i) are not located or residing in any country or territory subject to comprehensive US sanctions (currently Cuba, Crimea, Iran, North Korea, Donetsk People’s Republic, Luhansk People’s Republic, and Syria)
- scope: 

### Q6-WC-K0393

**Cited at:** section 1, line 21; section 2, line 48; section 2, line 53; section 3, line 61; section 5, line 90; section 6, line 100; section 7, line 115

**Record** (`studies/proposals/records/Q6/woocommerce/copied.tsv`):
- concern_id: WC-C-009
- placement: where
- structure: https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/
- identifier: WooPayments built in partnership with Stripe
- statement: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the WooPayments service.
- cite_ids: WC-S-0504

**Citation WC-S-0504:** `https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/` | WooPayments built in partnership with Stripe | 2026-09-30 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/053-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:03Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/085-woocommerce.com/text.txt` (fetched 2026-10-12T10:50:56Z, captured)
- quote: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the WooPayments service.
- title: WooPayments built in partnership with Stripe Documentation - WooCommerce
- in context: …Expand Themes Expand WooPayments WooPay WooCommerce Shipping WooCommerce Tax Retired Products Expand Woo Marketplace Code Snippets Expand WooPayments / Documentation / WooPayments Documentation / WooPayments: Account Management / WooPayments built in partnership with Stripe WooPayments built in partnership with Stripe WooPayments is built in partnership with Stripe. This document provides more information and an overview of how we work together. ⟪When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the WooPayments service.⟫ The Express account is what's used in the background for managing your business account information and activity with WooPayments. Who will provide support Our Happiness Engineers are here to help you set up and manage your store and usage of WooPayments. The support team will assist you with all payment processing issues and other operational questions, such as why one of your customer's payments failed, or why a payout has not been received. A…

### Q6-WC-020

**Cited at:** section 1, line 22; section 2, line 56

**Record** (`studies/proposals/records/Q6/woocommerce/statements.tsv`):
- stmt_id: Q6-WC-020
- bears_on: 1
- identifier: Updating your information
- statement: If your business has moved from one country to another, there isn’t a way to update the country. Please contact our support staff for assistance with the how to handle this.
- cite_ids: Q6-WC-C022
- from: held

**Citation Q6-WC-C022:** `https://woocommerce.com/document/woopayments/account-management/` | Updating your information | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/084-woocommerce.com/text.txt` (fetched 2026-10-12T10:50:55Z, captured)
- quote: If your business has moved from one country to another, there isn’t a way to update the country. Please contact our support staff for assistance with the how to handle this.
- title: WooPayments: Account Management Documentation - WooCommerce
- in context: …ommon examples are: How do I change my payout account information with WooPayments? How do I update my contact details such as email address or phone number? How do I update my business name or DBA with WooPayments? How do I update my tax ID number with WooPayments? How do I change my business type, e.g. from an individual to an LLC? How do I change my merchant category code (MCC)? How do I change the email address that WooPayments emails go to? ⟪If your business has moved from one country to another, there isn't a way to update the country. Please contact our support staff for assistance with the how to handle this.⟫ Finally, note that if Stripe has a problem verifying any personal or business information, you will be alerted to this on the Payments > Overview page and asked to update your information inside the WordPress dashboard. Switching and deleting accounts The following scenarios are rare, but you may run into them when operating multiple sites or shutting down a website for a business that's no longer operating. Can one WooPayments account be used w…

### Q6-WC-K0400

**Cited at:** section 1, line 26

**Record** (`studies/proposals/records/Q6/woocommerce/copied.tsv`):
- concern_id: WC-C-010
- placement: decides
- structure: https://woocommerce.com/document/woopayments/compatibility/countries/
- identifier: WooPayments in Your Country
- statement: If you are an individual or business based in one of our supported countries, you can sign up as a merchant with WooPayments.
- cite_ids: WC-S-0510

**Citation WC-S-0510:** `https://woocommerce.com/document/woopayments/compatibility/countries/` | WooPayments in Your Country | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/054-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:03Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/086-woocommerce.com/text.txt` (fetched 2026-10-12T10:50:57Z, captured)
- quote: If you are an individual or business based in one of our supported countries, you can sign up as a merchant with WooPayments.
- title: WooPayments in Your Country Documentation - WooCommerce
- in context: … to content Develop on Woo Hire an expert Get support Sell Extensions Resources Enterprise ecommerce Documentation Documentation WooCommerceExpand ProductsExpand ExtensionsExpand ThemesExpand WooPayments WooPay WooCommerce Shipping WooCommerce Tax Retired ProductsExpand Woo Marketplace Code SnippetsExpand WooPayments / Documentation / WooPayments Documentation / WooPayments: Compatibility / WooPayments in Your Country WooPayments in Your Country ⟪If you are an individual or business based in one of our supported countries, you can sign up as a merchant with WooPayments.⟫ Once that's done, you can accept payments from customers anywhere in the world in over 100 supported currencies. Supported countries ↑ Back to top WooPayments is available for individuals and businesses in: 🇦🇺 Australia 🇦🇹 Austria 🇧🇪 Belgium 🇧🇬 Bulgaria 🇨🇦 Canada 🇭🇷 Croatia 🇨🇾 Cyprus 🇨🇿 Czech Republic 🇩🇰 Denmark 🇪🇪 Estonia 🇫🇮 Finland 🇫🇷 France 🇩🇪 Germany 🇬🇷 Greece 🇭🇰 Hong Kong 🇭🇺 Hungary 🇮🇪 Ireland 🇮🇹 Italy 🇯🇵 Japan 🇱🇻 Latvia 🇱🇹 Lithuania 🇱🇺 Lux…

### Q6-WC-K0054

**Cited at:** section 1, line 28; section 2, line 44; section 2, line 52; section 3, line 67

**The same record as Q1-WC-K0054,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: * The payment extension list for each country.
- scope: 

### Q6-WC-K0333

**Cited at:** section 1, line 28; section 7, line 115

**The same record as Q1-WC-K0333,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: 'YE' => array( self::VISA => array( '_append' => array( 'tags' => array( self::TAG_PREFERRED ), ), ), ),
- scope: store country YE

### Q6-WC-007

**Cited at:** section 1, line 33

**Record** (`studies/proposals/records/Q6/woocommerce/statements.tsv`):
- stmt_id: Q6-WC-007
- bears_on: 2
- identifier: Other countries
- statement: If you want to use WooPayments, but it’s not available in your country, please vote for your country to be supported on the WooPayments feature requests page.
- cite_ids: Q6-WC-C007
- from: held

**Citation Q6-WC-C007:** `https://woocommerce.com/document/woopayments/compatibility/countries/` | Other countries | 2026-09-25 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/054-woocommerce.com/text.txt` (fetched 2026-10-10T23:54:03Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/086-woocommerce.com/text.txt` (fetched 2026-10-12T10:50:57Z, captured)
- quote: If you want to use WooPayments, but it’s not available in your country, please vote for your country to be supported on the WooPayments feature requests page.
- title: WooPayments in Your Country Documentation - WooCommerce
- in context: …cial activities typically requires a trade license or permit in the UAE. Therefore, only the Business account type is available for the UAE. Other countries In support of creating a global commerce platform, the WooCommerce team is actively working to make WooPayments available to other countries. We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store owners in that country. ⟪If you want to use WooPayments, but it's not available in your country, please vote for your country to be supported on the WooPayments feature requests page.⟫ Was this guide helpful for you? ON THIS PAGE Supported countries Outlying territories of France Outlying territories of the Netherlands Outlying territories of the UK Outlying territories of the U.S. Restrictions on account types Other countries WooPayments by Woo No payment details required • Set up in minutes Install for free 30-day money-back guarantee Support teams across the world Safe and secure online payments Sell WooCommerce WooCommerce…

### Q6-WC-K0403

**Cited at:** section 1, line 33; section 2, line 55

**The same record as Q1-WC-K0403,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store owners in that country.
- scope: 
