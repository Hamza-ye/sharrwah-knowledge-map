# Cards: Q3 on woocommerce

16 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 10:** - On WooCommerce, "Coming soon mode controls who can visit your site while you prepare it for launch", and the shipped install code sets `woocommerce_coming_soon` to yes. It matches Shopify's private mode on role, a store setting that keeps buyers out until launch (help pages, stated; WooCommerce's also shipped code); BigCommerce's storefront status, with `prelaunch_message` and `prelaunch_password`, overlaps in part (API reference, stated). Q3-WC-K1235; Q3-WC-K1236; Q3-SH-027; Q3-BC-013
- **section 1, line 16:** - The platforms offer their own payment products by where the business is, a match on role. Shopify Payments needs "a business located in your Designated Country" (its terms, official page). On help pages (stated), Zid Pay is offered to merchants of Saudi Arabia and Kuwait, and WooPayments needs a business "based in one of our supported countries". Q3-SH-K1536; Q3-ZD-P0113; Q3-WC-010
- **section 1, line 21:** - All five verify the person and the business before payments, a match on role (help pages, stated): Shopify and its banking partners "collect and verify information about you and your business"; WooPayments verifies business details with Stripe; Salla asks for an ID or iqama matching Absher, the entity's document, and a stamped IBAN certificate in a matching name; Zid's gateway approves the account on requirements set by business entity; and BigCommerce Payments shows KYC status among its Actions tasks. Q3-SH-012; Q3-WC-012; Q3-SA-013; Q3-ZD-P0118; Q3-BC-P0072
- **section 1, line 23:** - Other steps come first. Zid needs one published product matching the activity, and the store owner's Nafath check (not checked on WooCommerce; shown by Zid). Shopify needs two-step authentication; on store ibx5bt-xy, the saved markup of the Payments step, observed 30 September 2026, holds in a dialog "You need to set-up two-step authentication before adding a bank account.", words its accessibility tree doesn't show. Shopify and WooCommerce need test mode off, the same term for the same thing, and on store demo-fake-dev-store the saved markup of the Payments step, observed 30 September 2026, says "Development stores can only process test payments", as its accessibility tree did. Salla's activation includes accepting سياسة البيع. Q3-ZD-P0116; Q3-ZD-P0117; Q3-SH-K1274; Q3-SH-107; Q3-SH-028; Q3-WC-017; Q3-SH-106; Q3-SA-K1532
- **section 1, line 34:** - Payment providers and card networks set lists of what may not be sold, a match on role. On Shopify, "Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers" (its terms, official page). WooPayments cites "restrictions put in place by card networks, our payment processors, and their financial service providers", and BigCommerce points to Stripe's list (help pages, stated). Zid Pay's terms accept some digital products on the service provider's assessment. Q3-SH-P0045; Q3-WC-K0416; Q3-BC-021; Q3-ZD-K0070
- **section 1, line 36:** - A provider's exclusion closes only that provider, a match on role: Shopify Payments doesn't support hemp, CBD or THC, which compatible third-party providers may process, and WooPayments' CBD sellers must use Square or Viva Wallet. Q3-SH-095; Q3-WC-K0417
- **section 1, line 46:** - The business's country is hard to change: WooPayments' country "cannot be changed later", and Zid's terms for merchants outside Saudi Arabia ask one moving the store to another country to zero the wallet balance first. Q3-WC-011; Q3-ZD-K0230
- **section 1, line 52:** - For WooPayments the relevant country is "the one where your business is registered — not the one in which you personally live". BigCommerce generally deems the entity or person who creates the Account, Store or website the owner. Q3-WC-K0402; Q3-BC-004
- **section 1, line 60:** - Payment partners approve, a match on role (BigCommerce's pricing page, official; the others help pages, stated): Zid's requirements go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and its Nafath request is in the service provider's name; a PayPal Braintree application on BigCommerce doesn't guarantee approval; WooPayments verifies with Stripe; and Shopify's banking partners require a real person on every account. Q3-ZD-P0118; Q3-ZD-P0047; Q3-BC-P0065; Q3-WC-012; Q3-SH-020
- **section 1, line 65:** - When the seller applies, with review times that differ: Salla 24 to 48 hours; Shopify's documents up to 24 hours; WooPayments typically a couple of days. Zid's team reviews and notifies by email. Q3-SA-003; Q3-SH-014; Q3-WC-004; Q3-ZD-P0038
- **section 1, line 72:** - Effects can be narrow: a detail failing American Express's rules stops American Express at checkout while other card brands continue, and a revoked P24 makes only P24 orders fail. Q3-SH-058; Q3-WC-034
- **section 1, line 74:** - Zid Pay gives 14 days to correct wrong data, then disables the account and returns all amounts to end customers. Salla suspends payments and settlement "بعد انتهاء المهلة", a period whose length was not in what was read. WooPayments may restrict payments or payouts once a deadline for missing information passes. Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01; Q3-WC-P0055
- **section 1, line 76:** - Each records the state, a match on role across kinds: Shopify's ShopifyPaymentsAccount has a field for whether setup is completed (developer documentation, stated); Salla's payments answer carries `blocks_payment_activation` and each method's `blocked_by` (observed, store merchant, 8 October 2026); WooCommerce's shipped code gives an onboarding step a blocked status; and BigCommerce shows tasks and fund holds in its Actions section (stated). On Shopify store ibx5bt-xy, the saved markup of the Subscribe to Plus step, observed 30 September 2026, says "Shopify Payments is not available on your store.", as its accessibility tree did. Q3-SH-086; Q3-SA-073; Q3-SA-074; Q3-WC-041; Q3-BC-P0072; Q3-SH-108
- **section 1, line 77:** - Each tells the seller what is missing, as Shopify's alert takes the seller to the upload page, WooCommerce's notices appear on "Payments > Overview", and BigCommerce's Actions section lists the tasks. Q3-SH-017; Q3-WC-051; Q3-BC-P0072
- **section 2, line 82:** - **Business** (proposed): the legal entity behind one or more stores, with its **entity type** and its **registration place**, the place whose government documents it uses. These two choose each requirement set. The registration place comes from Salla's question for the country whose government documents the store uses (observed, Store 1, 8 October 2026) and WooPayments' country of registration; the entity types from Salla and Zid, whose requirements differ by entity type and country. Why: rule 1, since the place selects configuration rather than code, and rule 3. Q3-SA-085; Q3-WC-K0402; Q3-SA-056; Q3-ZD-K0239; Q3-ZD-K0240
- **section 2, line 84:** - Changing the registration place is a fresh verification with its own requirement set, not an edit, since WooPayments can't change it and Zid asks for the wallet at zero first. Why: rule 3. Q3-WC-011; Q3-ZD-K0230
- **section 2, line 87:** - **Capability status** (proposed): for each store and capability, available, blocked or restricted, with machine-readable reasons naming the unmet requirements. It takes Salla's `blocks_payment_activation`, `blocked_by` and `withdraw_disabled_reason`, WooCommerce's blocked onboarding step, and Shopify's field for setup completed. Why: rule 3, the data model. Q3-SA-073; Q3-SA-074; Q3-SA-077; Q3-WC-041; Q3-SH-086
- **section 2, line 88:** - **Requirement** (proposed): one condition, with its kind, subject, setter, validity and check. Its kinds come from the platforms: information, a document, an identity check, a plan, an accepted agreement, a store setting such as an address or test mode off, a product state such as a published product matching the activity, account security such as two-step authentication, account age such as WooPayments' 7 days before a first payout, a match between subjects such as the payout account's holder and the verified name, not being a listed party, as under Shopify Payments' sanctions rule, and another capability being active. Validity follows rules such as Zid's commercial register valid two months from activation. Its subject is the seller, a business person, the business, the store, a product or the payout account. Why: rule 2, since kinds will grow and each requirement is data. Q3-SH-028; Q3-ZD-P0116; Q3-SH-K1274; Q3-WC-P0038; Q3-SA-K1563; Q3-SH-K2268; Q3-ZD-013
- **section 2, line 98:** - **Store launch state** (proposed): the seller's own setting that keeps buyers out before launch, showing a page and optionally a password the seller gives to visitors; new stores start with it on. Launching is a capability whose requirement set may be empty. It takes the state from Shopify's private mode, WooCommerce's Coming soon mode with `woocommerce_coming_soon` on at install, and BigCommerce's `prelaunch_password`. What launching needs differs (Shopify a plan, an address and a payment method; Salla verification; Zid nothing found), so it is set per place. Why: rule 1. Q3-SH-027; Q3-SH-109; Q3-WC-K1236; Q3-BC-013; Q3-SH-028; Q3-SA-026; Q3-ZD-N03
- **section 2, line 99:** - **Product rule** (proposed): a rule on what may be sold, with its setter and its reach. It may bar a product for all of Sharrwah; bar it for one provider, blocking only that provider's capability; require a licence disclosed on the store with its details; require the registered activity to match the product; or require a plan for a product type. It takes Salla's selling policy, Shopify Payments' hemp rule and WooPayments' CBD rule, Salla's and Zid's licence clause, their activity match, and Salla's plan-limited product types. Why: rule 2, since each setter's list changes on its own. Q3-SA-054; Q3-SH-095; Q3-WC-K0417; Q3-SA-047; Q3-ZD-K0247; Q3-SA-058; Q3-ZD-003; Q3-SA-029
- **section 2, line 100:** - **Agreement acceptance** (proposed): each agreement a capability needs (Sharrwah's terms, a selling policy, a provider's terms) is recorded with its version and the time accepted, and declining a new version ends that capability. It takes Salla's selling policy accepted on activating e-payments, and WooPayments ending when the seller opts out of an updated agreement. Why: rule 3, partner contracts. Q3-SA-K1532; Q3-WC-K0714
- **section 2, line 101:** - **Seller action list** (proposed): one list of each blocked capability, the requirements it waits on, any deadline and the next step, read from the capability status, like BigCommerce's Actions section and Shopify's alerts. Left to the build. Q3-BC-P0072; Q3-SH-017; Q3-WC-051
- **section 3, line 107:** - Checkers: an identity service, such as Nafath on Zid and Absher on Salla, or a provider's own onboarding, such as Stripe's for WooPayments and the gateway that approves a Zid Pay account. Q3-ZD-P0117; Q3-SA-013; Q3-WC-012; Q3-ZD-P0118
- **section 3, line 118:** - Per product category: a provider's exclusions, such as hemp and CBD, and Zid Pay's assessment of digital products. Q3-SH-095; Q3-WC-K0417; Q3-ZD-K0070
- **section 3, line 119:** - Per store: the launch state. Q3-SH-027; Q3-WC-K1235
- **section 3, line 124:** - The seller: the launch state, and which providers to apply to. Q3-WC-K1235; Q3-BC-P0048
- **section 3, line 127:** - A card network: American Express on Shopify, and the networks behind WooPayments' restricted businesses. Q3-SH-057; Q3-WC-K0416
- **section 5, line 145:** - Who checks a seller before payments in a place: Sharrwah's own review (Salla), a gateway's approval (Zid), a partner's check (Stripe for WooPayments, Shopify's banking partners), or more than one. It is costly to change, being legal structure and partner contracts, and a partner's check may not reach a place, as for Yemen. Keep open: the checker as a plug-in and the setter on every requirement, with no single path built in. Settled by the company decisions on providers and on Sharrwah's own position (section 7). Q3-SA-037; Q3-ZD-P0118; Q3-WC-012; Q3-SH-012; YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 5, line 147:** - Which place selects a requirement set, and what moving it costs: the country of the documents (Salla), of registration (WooPayments), or of the business's location (Shopify). Yemen adds places below a country, where two areas set one requirement differently. Keep open: a registration place that can name an area within a country, kept apart from the store's selling places, and rules for moving it, such as Zid's zero balance first. Settled by the proposals for Q1 and Q6. Q3-SA-085; Q3-WC-K0402; Q3-SH-K1536; Q3-ZD-K0230; YA-150 (within thirty days of founding or licensing @ Houthis' area, as of 2026-10-10); YA-150 (within sixty days of starting its activity @ the unified Republic's area, as of 1991)
- **section 6, line 159:** - Stripe, the partner whose check WooPayments uses, is unavailable for Yemen at its own service as of that date, which forbids it as a checker for Yemen. Q3-WC-012; YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 7, line 168:** - Whether Sharrwah checks sellers itself, relies on payment providers' checks, or both, and in which places. Q3-SA-037; Q3-ZD-P0118; Q3-WC-012

## The cards

### Q3-WC-K1235

**Cited at:** section 1, line 10; section 3, line 119; section 3, line 124

**Record** (`studies/proposals/records/Q3/woocommerce/copied.tsv`):
- concern_id: WC-C-082
- placement: decides
- structure: https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/
- identifier: WooCommerce Coming soon mode
- statement: Coming soon mode controls who can visit your site while you prepare it for launch.
- cite_ids: WC-S-0891

**Citation WC-S-0891:** `https://woocommerce.com/document/configuring-woocommerce-settings/coming-soon-mode/` | WooCommerce Coming soon mode | 2026-08-06 | kind: stated | quote check: found
- quote: Coming soon mode controls who can visit your site while you prepare it for launch.
- title: WooCommerce Coming soon mode Documentation - WooCommerce
- in context: …erce Getting started Migrating to WooCommerce ProductsExpand Taxes ShippingExpand Payments Orders Data and reporting Customers Marketing Site administrationExpand Store settings How-to guides Automation Performance Localization Security Store designExpand Mobile AppExpand Get helpExpand Documentation / WooCommerce / Site administration / Store settings / Configuring WooCommerce settings / WooCommerce Coming soon mode WooCommerce Coming soon mode ⟪Coming soon mode controls who can visit your site while you prepare it for launch.⟫ Manage it from WooCommerce > Settings > Site visibility. Manage Coming soon mode and the visibility badge ↑ Back to top Go to WooCommerce > Settings > Site visibility to switch between Coming soon and Live. Use Display site visibility badge in admin bar to show or hide the status badge for users who can manage WooCommerce. This toggle does not change what visitors can see. The badge reads Coming soon, Store coming soon, or Live based on your vis…

### Q3-WC-K1236

**Cited at:** section 1, line 10; section 2, line 98

**Record** (`studies/proposals/records/Q3/woocommerce/copied.tsv`):
- concern_id: WC-C-082
- placement: decides
- structure: woocommerce-11.2.1:includes/class-wc-install.php
- identifier: woocommerce_coming_soon
- statement: public static function add_coming_soon_option() { add_option( 'woocommerce_coming_soon', 'yes' ); add_option( 'woocommerce_store_pages_only', 'yes' );
- cite_ids: WC-S-5421
- note: The method's docblock: 'Add the coming soon options for new shops.'

**Citation WC-S-5421:** `woocommerce-11.2.1:includes/class-wc-install.php` | lines 1317-1319 | 2026-10-09 | kind: shipped | quote check: found
- quote: public static function add_coming_soon_option() { add_option( 'woocommerce_coming_soon', 'yes' ); add_option( 'woocommerce_store_pages_only', 'yes' );
- in context: …/ public static function maybe_enable_hpos() { if ( self::should_enable_hpos_for_new_shop() ) { $feature_controller = wc_get_container()->get( FeaturesController::class ); $feature_controller->change_feature_enable( 'custom_order_tables', true ); } } /** * Add the coming soon options for new shops. * * Ensure that the options are set for all shops for performance even if core profiler is disabled on the host. * * @since 9.3.0 * * @return void */ ⟪public static function add_coming_soon_option() { add_option( 'woocommerce_coming_soon', 'yes' ); add_option( 'woocommerce_store_pages_only', 'yes' );⟫ } /** * Enable email improvements by default for new shops. * * @since 9.8.0 * * @return void */ public static function enable_email_improvements_for_newly_installed() { $feature_controller = wc_get_container()->get( FeaturesController::class ); $feature_controller->change_feature_enable( 'email_improvements', true ); update_option( 'woocommerce_email_improvements_default_enabled', 'yes' ); update_option( 'woocommerce_email_auto_sync_with_theme'…

### Q3-WC-010

**Cited at:** section 1, line 16

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-010
- bears_on: 1
- identifier: Requirements for WooPayments
- statement: Your business is based in one of our supported countries. PHP, WordPress, and WooCommerce are on recent versions. Your site has an SSL certificate and is accessible over HTTPS. You are at least 18 years old.
- scope: WooPayments
- cite_ids: Q3-WC-C012;Q3-WC-C013
- from: held

**Citation Q3-WC-C012:** `https://woocommerce.com/document/woopayments/startup-guide/` | Requirements for WooPayments | 2026-09-25 | kind: stated | quote check: found
- quote: Your business is based in one of our supported countries. PHP, WordPress, and WooCommerce are on recent versions. Your site has an SSL certificate and is accessible over HTTPS. You are at least 18 years old.
- title: WooPayments: Startup Guide Documentation - WooCommerce
- in context: …s Automated payouts to your bank account Buy now, pay later payment methods Built-in multi-currency support Easy integration of popular digital wallets Managing payments - including refunds, disputes, and payouts - is integrated into your site's WordPress administrator dashboard, so it all happens from within your site's admin dashboard. Requirements for WooPayments First, let's make sure you have what's required to ensure a smooth installation: ⟪Your business is based in one of our supported countries. PHP, WordPress, and WooCommerce are on recent versions. Your site has an SSL certificate and is accessible over HTTPS. You are at least 18 years old.⟫ Check for WooPayments Go to Plugins > Installed Plugins to see if WooPayments is already installed. If it is, great! Head to the Signing up for WooPayments section and continue from there. If it's not listed, please follow the instructions in the Installing WooPayments section below. Installing WooPayments Most users will be able to install WooPayments directly from the WooCommerce > Payments settings. You can access the Payments settings throug…

**Citation Q3-WC-C013:** `https://woocommerce.com/document/woopayments/startup-guide/` | Requirements for WooPayments | 2026-09-25 | kind: stated | quote check: found
- quote: First, let’s make sure you have what’s required to ensure a smooth installation:
- title, opening and note boxes: as for this source's citation above
- in context: …get: Credit and debit card acceptance Local payment method offerings Automated payouts to your bank account Buy now, pay later payment methods Built-in multi-currency support Easy integration of popular digital wallets Managing payments - including refunds, disputes, and payouts - is integrated into your site's WordPress administrator dashboard, so it all happens from within your site's admin dashboard. Requirements for WooPayments ↑ Back to top ⟪First, let's make sure you have what's required to ensure a smooth installation:⟫ Your business is based in one of our supported countries. PHP, WordPress, and WooCommerce are on recent versions. Your site has an SSL certificate and is accessible over HTTPS. You are at least 18 years old. Check for WooPayments ↑ Back to top Go to Plugins > Installed Plugins to see if WooPayments is already installed. If it is, great! Head to the Signing up for WooPayments section and continue from there. If it's not listed, please follow the …

### Q3-WC-012

**Cited at:** section 1, line 21; section 1, line 60; section 3, line 107; section 5, line 145; section 6, line 159; section 7, line 168

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-012
- bears_on: 1
- identifier: The WooPayments signup process
- statement: Provide the required business information and select Continue. Verify your business details with our payments partner, Stripe.
- scope: WooPayments
- cite_ids: Q3-WC-C015
- from: held

**Citation Q3-WC-C015:** `https://woocommerce.com/document/woopayments/startup-guide/` | The WooPayments signup process | 2026-09-25 | kind: stated | quote check: found
- quote: Provide the required business information and select Continue. Verify your business details with our payments partner, Stripe.
- title: WooPayments: Startup Guide Documentation - WooCommerce
- in context: …rompt to connect to your WordPress.com account. The login screen for connecting to your WordPress.com account. The confirmation screen for connecting your WordPress.com account. Select Start accepting payments to begin creating your WooPayments account. Note: Selecting Test payments will create a test account, which will allow you to safely test payments in a sandbox-like environment. However, you cannot accept real payments with a test account. ⟪Provide the required business information and select Continue. Verify your business details with our payments partner, Stripe.⟫ After you click the Add information button, a popup from connect.stripe.com will appear, asking for your phone number and email address. This is a normal part of the account creation process. Once you've verified your phone number, you'll start entering your personal and business details. Note that the phone number you provide during signup also becomes your store's support phone number, which is semi-public business contact info. After you've g…

### Q3-WC-017

**Cited at:** section 1, line 23

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-017
- bears_on: 1
- identifier: Test mode
- statement: When you’re ready to go live, remember to disable test mode before accepting live payments.
- scope: WooPayments
- cite_ids: Q3-WC-C020
- from: held

**Citation Q3-WC-C020:** `https://woocommerce.com/document/woopayments/startup-guide/` | Test mode | 2026-09-25 | kind: stated | quote check: found
- quote: When you’re ready to go live, remember to disable test mode before accepting live payments.
- title: WooPayments: Startup Guide Documentation - WooCommerce
- in context: … you want to test WooPayments before taking any real payments, you can do that by also checking the Enable test mode box. Test mode ↑ Back to top Test mode lets you simulate transactions using test card numbers so that you can ensure your checkout process is working as expected. Simply put any product in the cart and go through the checkout process and the order confirmation page to see exactly what customers would see during an actual purchase. ⟪When you're ready to go live, remember to disable test mode before accepting live payments.⟫ NOTE: Test mode only works with test credit card numbers. Using real credit card information while WooPayments is in test mode will cause the order to fail and an error will be displayed. Payments accepted on checkout ↑ Back to top In the Payments accepted on checkout section, you'll see that by default you are already able to take credit and debit card payments: By checking the boxes for other payment methods, you can also offer additional paym…

### Q3-WC-K0416

**Cited at:** section 1, line 34; section 3, line 127

**The same record as Q2-WC-K0416,** whose card is in `Q2-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Due to restrictions put in place by card networks, our payment processors, and their financial service providers, some business types and product types are not allowed to transact using WooPayments.
- scope: 

### Q3-WC-K0417

**Cited at:** section 1, line 36; section 2, line 99; section 3, line 118

**The same record as Q2-WC-K0417,** whose card is in `Q2-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Merchants selling CBD must use Square or Viva Wallet.
- scope: merchants selling CBD

### Q3-WC-011

**Cited at:** section 1, line 46; section 2, line 84

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-011
- bears_on: 1;4
- identifier: Signing up for WooPayments: Before you begin
- statement: Be sure to select the correct country for your account, as it cannot be changed later.
- scope: WooPayments
- cite_ids: Q3-WC-C014
- from: held

**Citation Q3-WC-C014:** `https://woocommerce.com/document/woopayments/startup-guide/` | Before you begin | 2026-09-25 | kind: stated | quote check: found
- quote: Be sure to select the correct country for your account, as it cannot be changed later.
- title: WooPayments: Startup Guide Documentation - WooCommerce
- in context: … up for WooPayments ↑ Back to top After you've installed and activated WooPayments, it's time to start the signup process. Before you begin ↑ Back to top Before starting the signup process, keep the following information in mind: Although most of the signup process takes place on your site, there will be a popup shown from connect.stripe.com (Stripe is our payments partner) that collects your phone number and email address. This popup is normal. ⟪Be sure to select the correct country for your account, as it cannot be changed later.⟫ If you're using WooPayments for a business, the relevant country is the one where your business is registered, not the one in which you personally live. You will have the option to create a test account as a part of the signup process, which allows you to explore WooPayments using simulated information. If you run into any issues with the signup form itself, please read our onboarding troubleshooting document to help diagnose the problem. The Wo…

### Q3-WC-K0402

**Cited at:** section 1, line 52; section 2, line 82; section 5, line 147

**The same record as Q1-WC-K0402,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: NOTE: If you’re using WooPayments for a business, the relevant country is the one where your business is registered — not the one in which you personally live.
- scope: 

### Q3-WC-004

**Cited at:** section 1, line 65

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-004
- bears_on: 4
- identifier: How quickly will you confirm my identity?
- statement: Typically, we’ll confirm your application within a couple of days.
- scope: WooPayments
- cite_ids: Q3-WC-C006
- from: held

**Citation Q3-WC-C006:** `https://woocommerce.com/document/woopayments/our-policies/know-your-customer/` | How quickly will you confirm my identity? | 2025-08-15 | kind: stated | quote check: found
- quote: Typically, we’ll confirm your application within a couple of days.
- title: WooPayments: &quot;Know Your Customer&quot; Documentation - WooCommerce
- in context: …ed, especially if the site accepts live transactions before the correct account information is entered. Is my data safe with WooCommerce? ↑ Back to top We take every step required to safeguard your personal data. WooPayments is built in partnership with Stripe to store your data in a safe and secure manner. How quickly will you confirm my identity? ↑ Back to top We'll do our best to work with Stripe to confirm your identity as quickly as we can. ⟪Typically, we'll confirm your application within a couple of days.⟫ What information will I need? ↑ Back to top Here's a brief list of the information you'll need to finish payment signup: Business owner information Legal name Date of birth Home address Email address Mobile phone number Bank account information Social Security number (SSN) or Taxpayer Identification Number Business information Country where your business is based Type of business Industry Company address Company phone number Company URL EIN or o…

### Q3-WC-034

**Cited at:** section 1, line 72

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-034
- bears_on: 4
- identifier: Przelewy24 (P24) additional requirements
- statement: When access to P24 payments is revoked, orders using it will fail at checkout with an authentication error rather than P24 simply being disabled in your settings.
- scope: Przelewy24 (P24)
- cite_ids: Q3-WC-C041
- from: held

**Citation Q3-WC-C041:** `https://woocommerce.com/document/woopayments/payment-methods/local-payment-methods/` | Przelewy24 (P24) additional requirements | 2026-09-25 | kind: stated | quote check: found
- quote: When access to P24 payments is revoked, orders using it will fail at checkout with an authentication error rather than P24 simply being disabled in your settings.
- title: Local payment methods Documentation - WooCommerce
- in context: …our company address, tax number, and registration number. Refund and privacy policies. An MCC that is not one of the prohibited MCCs listed below. If you do not meet these criteria, your ability to accept P24 payments may be removed without warning at any time. P24 reviews merchants on an ongoing basis, not just when you first activate it. This means that your access might be revoked even if you've accepted P24 payments successfully in the past. ⟪When access to P24 payments is revoked, orders using it will fail at checkout with an authentication error rather than P24 simply being disabled in your settings.⟫ Sadly this is not something that we (WooPayments/Automattic) can control. If your P24 payments have started failing unexpectedly, contact our support team. Przelewy24 (P24) prohibited businesses In addition to our general list of prohibited or restricted products, businesses using the following MCCs are not eligible to use Przelewy24. (If you would like to change your MCC to a different one, please see this document.) CATEGORY MCC Airlines and A…

### Q3-WC-P0055

**Cited at:** section 1, line 74

**Record** (`studies/proposals/records/Q3/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-054
- bullet: a;c
- placement: decides
- identifier: WooPayments: Our Policies > Restricted accounts
- statement: On rare occasions, payments and/or payouts may be restricted on your account. This can happen for a variety of reasons: Your account is missing some information and the deadline to add it has passed. Dispute activity has increased substantially — beyond reasonable thresholds. Our payments partner, Stripe, has found other issues with your account.
- scope: WooPayments
- cite_ids: S01-WC-C057;S01-WC-C058
- from: new

**Citation S01-WC-C057:** `https://woocommerce.com/document/woopayments/our-policies/` | Restricted accounts | 2026-09-25 | kind: stated | quote check: found
- quote: On rare occasions, payments and/or payouts may be restricted on your account. This can happen for a variety of reasons:
- title: WooPayments: Our Policies Documentation - WooCommerce
- in context: …Payments. For example, during the signup process you may be asked for the following: Personal information Your name Date of birth Home address Bank account info etc. Business information Type of business Business address Phone number Business tax ID etc. In the payments industry, this process is called "know your customer" or just "KYC." Please consult our Know Your Customer FAQ for answers to further questions. Restricted accounts ↑ Back to top ⟪On rare occasions, payments and/or payouts may be restricted on your account. This can happen for a variety of reasons:⟫ Your account is missing some information and the deadline to add it has passed. Dispute activity has increased substantially - beyond reasonable thresholds. Our payments partner, Stripe, has found other issues with your account. Restricted accounts won't be able to fully manage WooPayments, so some menu items will be hidden. However, restricted accounts will still be able to access the Transactions and Disputes menus in order to manage new and e…

**Citation S01-WC-C058:** `https://woocommerce.com/document/woopayments/our-policies/` | Restricted accounts | 2026-09-25 | kind: stated | quote check: found
- quote: Your account is missing some information and the deadline to add it has passed. Dispute activity has increased substantially — beyond reasonable thresholds. Our payments partner, Stripe, has found other issues with your account.
- title, opening and note boxes: as for this source's citation above
- in context: … of birth Home address Bank account info etc. Business information Type of business Business address Phone number Business tax ID etc. In the payments industry, this process is called "know your customer" or just "KYC." Please consult our Know Your Customer FAQ for answers to further questions. Restricted accounts ↑ Back to top On rare occasions, payments and/or payouts may be restricted on your account. This can happen for a variety of reasons: ⟪Your account is missing some information and the deadline to add it has passed. Dispute activity has increased substantially - beyond reasonable thresholds. Our payments partner, Stripe, has found other issues with your account.⟫ Restricted accounts won't be able to fully manage WooPayments, so some menu items will be hidden. However, restricted accounts will still be able to access the Transactions and Disputes menus in order to manage new and existing disputes. If your account is restricted, you should receive an email with more information from either the WooCommerce team or Stripe. Please respond to this email to address the issue. If your account is restricted, but …

### Q3-WC-041

**Cited at:** section 1, line 76; section 2, line 87

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-041
- bears_on: 4
- identifier: ONBOARDING_STEP_STATUS_BLOCKED ('blocked')
- statement: For example, the store may not use HTTPS, or live onboarding might be prevented due to environment settings.
- cite_ids: Q3-WC-C048
- from: held

**Citation Q3-WC-C048:** `woocommerce-11.2.1:src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsService.php` | line 66 (comment on ONBOARDING_STEP_STATUS_BLOCKED) | 2026-10-09 | kind: shipped | quote check: found
- quote: For example, the store may not use HTTPS, or live onboarding might be prevented due to environment settings.
- in context: …efers to some error that occurred during a step action. * Retrying the action should be possible and lead to a different step status. */ const ONBOARDING_STEP_STATUS_FAILED = 'failed'; /** * Blocked generally refers to a step can't progress to a completed state due to some technical requirements * that are beyond the purview of the Payments Settings page or the WooPayments extension. * Most of the time, the reasons will be environment-related. * ⟪For example, the store may not use HTTPS, or live onboarding might be prevented due to environment settings.⟫ */ const ONBOARDING_STEP_STATUS_BLOCKED = 'blocked'; /** * Marker recorded alongside a step's completed status when the step was skipped forward * rather than actually completed (e.g. the test account could not be created due to a * non-recoverable failure). It is never reported as a step status; it only informs the * status determination logic. Being stored with the step statuses, it shares their * lifecycle: it is removed when the step progres…

### Q3-WC-051

**Cited at:** section 1, line 77; section 2, line 101

**Record** (`studies/proposals/records/Q3/woocommerce/statements.tsv`):
- stmt_id: Q3-WC-051
- bears_on: 4
- identifier: Payments > Overview
- statement: Finally, note that if Stripe has a problem verifying any personal or business information, you will be alerted to this on the Payments > Overview page and asked to update your information inside the WordPress dashboard.
- scope: WooPayments
- cite_ids: Q3-WC-C058
- from: held

**Citation Q3-WC-C058:** `https://woocommerce.com/document/woopayments/account-management/` | Updating your information | 2026-09-25 | kind: stated | quote check: found
- quote: Finally, note that if Stripe has a problem verifying any personal or business information, you will be alerted to this on the Payments > Overview page and asked to update your information inside the WordPress dashboard.
- title: WooPayments: Account Management Documentation - WooCommerce
- in context: …my business name or DBA with WooPayments? How do I update my tax ID number with WooPayments? How do I change my business type, e.g. from an individual to an LLC? How do I change my merchant category code (MCC)? How do I change the email address that WooPayments emails go to? If your business has moved from one country to another, there isn't a way to update the country. Please contact our support staff for assistance with the how to handle this. ⟪Finally, note that if Stripe has a problem verifying any personal or business information, you will be alerted to this on the Payments > Overview page and asked to update your information inside the WordPress dashboard.⟫ Switching and deleting accounts The following scenarios are rare, but you may run into them when operating multiple sites or shutting down a website for a business that's no longer operating. Can one WooPayments account be used with multiple websites? Is WooPayments compatible with WordPress Multisite? Can I migrate my information between two different accounts? How do I transfer a site that uses WooPayments to a new owner? How do I delete my Wo…

### Q3-WC-P0038

**Cited at:** section 2, line 88

**Record** (`studies/proposals/records/Q3/woocommerce/copied-pilot.tsv`):
- stmt_id: S01-WC-037
- bullet: c
- placement: decides
- identifier: When will I receive payouts for my WooPayments account balance? > New account waiting period
- statement: The first payout for all new accounts is sent after a 7 day waiting period. This delay is necessary for risk mitigation and cannot be waived under any circumstances.
- scope: WooPayments new accounts
- cite_ids: S01-WC-C037
- from: new

**Citation S01-WC-C037:** `https://woocommerce.com/document/woopayments/payouts/payout-schedule/` | New account waiting period | 2026-08-21 | kind: stated | quote check: found
- quote: The first payout for all new accounts is sent after a 7 day waiting period. This delay is necessary for risk mitigation and cannot be waived under any circumstances.
- title: When will I receive payouts for my WooPayments account balance? Documentation - WooCommerce
- in context: …ridays. If a customer orders from their store on Thursday, 4 business days after that would be the following Wednesday. However, due to their "weekly on Fridays" payout schedule, the funds remain in their account for 2 more days, and are paid out on the following Friday. NOTE: Changing your payout schedule might not be possible if your payouts are suspended or if your schedule has been manually set by us. New account waiting period ↑ Back to top ⟪The first payout for all new accounts is sent after a 7 day waiting period. This delay is necessary for risk mitigation and cannot be waived under any circumstances.⟫ The new account waiting period starts after the first successful payment is processed on your account, not when the account is created. After the 7 day waiting period is over, the first payout will be sent according to the pending period chart and the payout schedule set on the account. For example, consider a new U.S. merchant who creates their account on Monday and makes their first sale on Wednesday. Their 7 day waiting period ends on the fol…

### Q3-WC-K0714

**Cited at:** section 2, line 100

**Record** (`studies/proposals/records/Q3/woocommerce/copied.tsv`):
- concern_id: WC-C-048
- placement: decides
- structure: https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/
- identifier: Stripe agreement updates
- statement: In short, opting out will effectively end your usage of WooPayments immediately.
- cite_ids: WC-S-0508

**Citation WC-S-0508:** `https://woocommerce.com/document/woopayments/account-management/partnership-with-stripe/` | Stripe agreement updates | 2026-09-30 | kind: stated | quote check: found
- quote: In short, opting out will effectively end your usage of WooPayments immediately.
- title: WooPayments built in partnership with Stripe Documentation - WooCommerce
- in context: …reply to that email and let us know. Keep in mind that opting out in this way means that you will no longer be able to use WooPayments at all. Although your remaining account balance will still be paid out as per your usual schedule, you will not be able to: Have customers place new orders via WooPayments Refund any orders placed with WooPayments Challenge disputes filed for WooPayments orders Log into the WooPayments Stripe Express account etc. ⟪In short, opting out will effectively end your usage of WooPayments immediately.⟫ On this page Who will provide support Access to the Stripe dashboard Updating account information Existing Stripe Accounts Stripe agreement updates 30-day money-back guarantee Support teams across the world Safe and secure online payments Sell WooCommerce WooCommerce pricing Payments No-code customization Marketing Checkout Shipping Mobile app Enterprise ecommerce Marketplace WooCommerce extensions WooCommerce themes New Essentials Collections D…
