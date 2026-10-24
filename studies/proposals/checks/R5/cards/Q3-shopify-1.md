# Cards: Q3 on shopify

18 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 9:** - On Shopify, a free-trial store is automatically in private mode, its pages inaccessible, and before launch the seller must select a plan, add a store address, and set up a payment method with test mode deactivated. On store capture-plus, the saved markup of the Online Store Preferences step, observed 4 October 2026, gives Private mode a landing page that "requires a password to enter your store" and tells the seller to give visitors the password, as its accessibility tree did. Q3-SH-027; Q3-SH-028; Q3-SH-109
- **section 1, line 10:** - On WooCommerce, "Coming soon mode controls who can visit your site while you prepare it for launch", and the shipped install code sets `woocommerce_coming_soon` to yes. It matches Shopify's private mode on role, a store setting that keeps buyers out until launch (help pages, stated; WooCommerce's also shipped code); BigCommerce's storefront status, with `prelaunch_message` and `prelaunch_password`, overlaps in part (API reference, stated). Q3-WC-K1235; Q3-WC-K1236; Q3-SH-027; Q3-BC-013
- **section 1, line 16:** - The platforms offer their own payment products by where the business is, a match on role. Shopify Payments needs "a business located in your Designated Country" (its terms, official page). On help pages (stated), Zid Pay is offered to merchants of Saudi Arabia and Kuwait, and WooPayments needs a business "based in one of our supported countries". Q3-SH-K1536; Q3-ZD-P0113; Q3-WC-010
- **section 1, line 17:** - Checked against a merchant selling in the Yemeni market: any country beyond the 40 on Shopify's list of supported countries is absent, Yemen not among the 40, and for store fake-demo-sharrwah, whose business entity is in Yemen, observed 5 October 2026, the admin's ShopifyPaymentsData answer gave Shopify Payments "eligible":false. Zid Pay's Kuwait terms bar activities dealing with countries under international sanctions, naming اليمن; its Saudi terms' list doesn't. Q3-SH-A0002; Q3-SH-100; Q3-ZD-P0112; Q3-ZD-P0111
- **section 1, line 21:** - All five verify the person and the business before payments, a match on role (help pages, stated): Shopify and its banking partners "collect and verify information about you and your business"; WooPayments verifies business details with Stripe; Salla asks for an ID or iqama matching Absher, the entity's document, and a stamped IBAN certificate in a matching name; Zid's gateway approves the account on requirements set by business entity; and BigCommerce Payments shows KYC status among its Actions tasks. Q3-SH-012; Q3-WC-012; Q3-SA-013; Q3-ZD-P0118; Q3-BC-P0072
- **section 1, line 22:** - What is asked differs by entity type and place. Zid: "تختلف المتطلبات والبيانات المطلوبة حسب نوع النشاط التجاري والدولة". Salla's table asks an individual for a freelance document (Saudi citizens only), an establishment or company for a commercial registration, and a charity for its certificate, each with its own kind of bank account. Shopify's Proof of Liveness depends on the country; on store capture-advanced, the saved markup of the business details step, observed 4 October 2026, gives a US Individual's Social Security Number field as "Used for tax filing and verification.", as its accessibility tree did. Q3-ZD-K0240; Q3-SA-014; Q3-SH-041; Q3-SH-111
- **section 1, line 23:** - Other steps come first. Zid needs one published product matching the activity, and the store owner's Nafath check (not checked on WooCommerce; shown by Zid). Shopify needs two-step authentication; on store ibx5bt-xy, the saved markup of the Payments step, observed 30 September 2026, holds in a dialog "You need to set-up two-step authentication before adding a bank account.", words its accessibility tree doesn't show. Shopify and WooCommerce need test mode off, the same term for the same thing, and on store demo-fake-dev-store the saved markup of the Payments step, observed 30 September 2026, says "Development stores can only process test payments", as its accessibility tree did. Salla's activation includes accepting سياسة البيع. Q3-ZD-P0116; Q3-ZD-P0117; Q3-SH-K1274; Q3-SH-107; Q3-SH-028; Q3-WC-017; Q3-SH-106; Q3-SA-K1532
- **section 1, line 24:** - Plans gate payments on three platforms, a match on role across kinds. Salla's help page (stated) puts electronic payment methods only in paid plans, and on store merchant (Basic, observed 8 October 2026) mada, credit card, Apple Pay and STC Pay were each `blocked_by` `requires_paid_plan`. BigCommerce's pages (stated) disagree on which plans qualify, Core, Growth or Scale (read 13 October 2026) or self-serve and retail plans (read 12 October 2026); the proposal rests only on a plan being needed. On Shopify store ts15uk-ug, observed 7 October 2026 in its trial, the Orders page said "To get orders and accept payments from customers, you need to select a plan." Q3-SA-P0068; Q3-SA-074; Q3-BC-P0068; Q3-BC-P0029; Q3-SH-101
- **section 1, line 25:** - Other parties add their own requirements, a match on role. On help pages (stated): American Express's address and name rules on a Shopify Payments account; for Tabby in Salla's UAE stores, a verified store, a Tabby merchant account with its keys, and an eligible plan; and each BigCommerce provider's own application and underwriting. On store ibx5bt-xy, the saved markup of the Shop Pay Installments terms step, observed 30 September 2026, says "Affirm reserves the right to deny you access to the Affirm Services" and asks for information identifying the seller and its beneficial owners, as its accessibility tree did. Q3-SH-057; Q3-SA-069; Q3-BC-P0048; Q3-SH-110
- **section 1, line 29:** - The payout account's holder must match the verified identity, a match on role. Shopify compares the bank account's name with the legal business name or the account representative's. Salla: "تأكد من أن اسم صاحب الحساب البنكي مطابق لبيانات التوثيق". Zid: "لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح". On both Salla and Zid an establishment needs a business account in its own name. Q3-SH-062; Q3-SA-K1563; Q3-ZD-K0037; Q3-SA-010; Q3-ZD-015
- **section 1, line 34:** - Payment providers and card networks set lists of what may not be sold, a match on role. On Shopify, "Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers" (its terms, official page). WooPayments cites "restrictions put in place by card networks, our payment processors, and their financial service providers", and BigCommerce points to Stripe's list (help pages, stated). Zid Pay's terms accept some digital products on the service provider's assessment. Q3-SH-P0045; Q3-WC-K0416; Q3-BC-021; Q3-ZD-K0070
- **section 1, line 36:** - A provider's exclusion closes only that provider, a match on role: Shopify Payments doesn't support hemp, CBD or THC, which compatible third-party providers may process, and WooPayments' CBD sellers must use Square or Viva Wallet. Q3-SH-095; Q3-WC-K0417
- **section 1, line 38:** - Shopify's hemp confirmations in the United States include providing documents whenever Shopify asks; when it checks licences and confirmations beyond that was not in what was read. Q3-SH-053; Q3-SH-N02
- **section 1, line 61:** - Law, regulators and networks set others, as the platforms report them: Shopify's European and UK verification follows the FCA and the Central Bank of Ireland, and its prohibited categories may come from law, network rules, Shopify or processors' providers; Zid's licences come from the relevant authorities; and Salla's e-commerce obligations from the e-commerce law and the Ministry of Commerce's guide. Q3-SH-065; Q3-SH-P0045; Q3-ZD-023; Q3-SA-033
- **section 2, line 83:** - Not taken: keying requirements to where the business is located, as Shopify Payments does. Documents come from the place of registration, as Salla and WooPayments say, and the store's own selling places stay with Q1. Q3-SH-K1536
- **section 2, line 85:** - **Business person** (proposed): each individual the business must name, with a role, such as Shopify's one individual representative and its owners of 25% or more, and the beneficial owners a provider asks about, as the Shop Pay Installments terms do in store ibx5bt-xy's saved markup, observed 30 September 2026. The roles and the ownership threshold are set per registration place, as Shopify's "For most regions" shows. Why: rules 1 and 3. Q3-SH-020; Q3-SH-023; Q3-SH-110
- **section 2, line 88:** - **Requirement** (proposed): one condition, with its kind, subject, setter, validity and check. Its kinds come from the platforms: information, a document, an identity check, a plan, an accepted agreement, a store setting such as an address or test mode off, a product state such as a published product matching the activity, account security such as two-step authentication, account age such as WooPayments' 7 days before a first payout, a match between subjects such as the payout account's holder and the verified name, not being a listed party, as under Shopify Payments' sanctions rule, and another capability being active. Validity follows rules such as Zid's commercial register valid two months from activation. Its subject is the seller, a business person, the business, the store, a product or the payout account. Why: rule 2, since kinds will grow and each requirement is data. Q3-SH-028; Q3-ZD-P0116; Q3-SH-K1274; Q3-WC-P0038; Q3-SA-K1563; Q3-SH-K2268; Q3-ZD-013
- **section 2, line 89:** - **Requirement set** (proposed): the requirements one capability needs, for one registration place, entity type, plan and provider; configured, versioned and shown to the seller. It combines Salla's per-country verification (a UAE trade licence, Emirates IDs and an IBAN certificate; in Saudi Arabia, an Absher-matched ID and a citizens-only freelance document), Zid's per-entity and per-country requirements, and Shopify's per-country Proof of Liveness. Why: rule 1. Q3-SA-072; Q3-SA-014; Q3-SA-013; Q3-ZD-K0240; Q3-SH-041
- **section 2, line 94:** - **Restriction** (proposed): what an unmet requirement does, scoped to the capability it gates: keep the store from buyers, block a payment method or checkout, allow only test payments (as store demo-fake-dev-store's saved markup, observed 30 September 2026, says of development stores), hold payouts, block withdrawals, or suspend the store. Each records its reason and the requirements it waits on, and lifts when they are met, as Shopify's pauses lift "automatically after you complete verification". It follows the narrow effects the platforms show: American Express alone stopping, other providers unaffected, the store usable while payouts are held, products kept after a rejection. Why: rule 2. Q3-SH-058; Q3-SH-073; Q3-SH-P0085; Q3-SA-023; Q3-SH-070; Q3-SH-106
- **section 2, line 98:** - **Store launch state** (proposed): the seller's own setting that keeps buyers out before launch, showing a page and optionally a password the seller gives to visitors; new stores start with it on. Launching is a capability whose requirement set may be empty. It takes the state from Shopify's private mode, WooCommerce's Coming soon mode with `woocommerce_coming_soon` on at install, and BigCommerce's `prelaunch_password`. What launching needs differs (Shopify a plan, an address and a payment method; Salla verification; Zid nothing found), so it is set per place. Why: rule 1. Q3-SH-027; Q3-SH-109; Q3-WC-K1236; Q3-BC-013; Q3-SH-028; Q3-SA-026; Q3-ZD-N03
- **section 2, line 99:** - **Product rule** (proposed): a rule on what may be sold, with its setter and its reach. It may bar a product for all of Sharrwah; bar it for one provider, blocking only that provider's capability; require a licence disclosed on the store with its details; require the registered activity to match the product; or require a plan for a product type. It takes Salla's selling policy, Shopify Payments' hemp rule and WooPayments' CBD rule, Salla's and Zid's licence clause, their activity match, and Salla's plan-limited product types. Why: rule 2, since each setter's list changes on its own. Q3-SA-054; Q3-SH-095; Q3-WC-K0417; Q3-SA-047; Q3-ZD-K0247; Q3-SA-058; Q3-ZD-003; Q3-SA-029
- **section 3, line 108:** - Payment providers, each with its own requirement set and approval: American Express on Shopify, Tabby on Salla, Tap on Zid, and the providers on BigCommerce. Q3-SH-057; Q3-SA-069; Q3-ZD-K0093; Q3-BC-P0048
- **section 3, line 114:** - Per registration place: the documents and checks, as on Salla by country, on Zid by country, and for Shopify's Proof of Liveness. Q3-SA-072; Q3-ZD-K0240; Q3-SH-041
- **section 3, line 115:** - Per entity type and place: the documents, the fields, and the kind of payout account, as in Salla's table, on Zid, and in the Social Security Number field for a US Individual in Shopify store capture-advanced's saved markup, observed 4 October 2026. Q3-SA-014; Q3-SA-010; Q3-ZD-015; Q3-SH-111
- **section 3, line 117:** - Per provider or payment method: American Express's rules, and Tabby's on Salla. Q3-SH-057; Q3-SA-069
- **section 3, line 118:** - Per product category: a provider's exclusions, such as hemp and CBD, and Zid Pay's assessment of digital products. Q3-SH-095; Q3-WC-K0417; Q3-ZD-K0070
- **section 3, line 119:** - Per store: the launch state. Q3-SH-027; Q3-WC-K1235
- **section 3, line 126:** - A provider: its own requirements and its approval. Q3-ZD-P0118; Q3-BC-P0065; Q3-SH-110
- **section 3, line 127:** - A card network: American Express on Shopify, and the networks behind WooPayments' restricted businesses. Q3-SH-057; Q3-WC-K0416
- **section 5, line 145:** - Who checks a seller before payments in a place: Sharrwah's own review (Salla), a gateway's approval (Zid), a partner's check (Stripe for WooPayments, Shopify's banking partners), or more than one. It is costly to change, being legal structure and partner contracts, and a partner's check may not reach a place, as for Yemen. Keep open: the checker as a plug-in and the setter on every requirement, with no single path built in. Settled by the company decisions on providers and on Sharrwah's own position (section 7). Q3-SA-037; Q3-ZD-P0118; Q3-WC-012; Q3-SH-012; YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 5, line 147:** - Which place selects a requirement set, and what moving it costs: the country of the documents (Salla), of registration (WooPayments), or of the business's location (Shopify). Yemen adds places below a country, where two areas set one requirement differently. Keep open: a registration place that can name an area within a country, kept apart from the store's selling places, and rules for moving it, such as Zid's zero balance first. Settled by the proposals for Q1 and Q6. Q3-SA-085; Q3-WC-K0402; Q3-SH-K1536; Q3-ZD-K0230; YA-150 (within thirty days of founding or licensing @ Houthis' area, as of 2026-10-10); YA-150 (within sixty days of starting its activity @ the unified Republic's area, as of 1991)
- **section 7, line 169:** - Which identity services and payment providers Sharrwah works with, since their requirements then bind its sellers. Q3-ZD-P0117; Q3-SA-013; Q3-SH-057
- **section 7, line 172:** - Whether Sharrwah reviews products against licences or takes the seller's declaration, and who answers when a product breaks a law. Q3-BC-K0460; Q3-SA-057; Q3-SH-053

## The cards

### Q3-SH-027

**Cited at:** section 1, line 9; section 1, line 10; section 2, line 98; section 3, line 119

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-027
- bears_on: 1;4
- identifier: Launch your store
- statement: During your free trial, your online store is automatically in private mode. In private mode, your site's pages are inaccessible, and a customizable landing page with a password option is displayed instead.
- cite_ids: Q3-SH-C039
- from: held

**Citation Q3-SH-C039:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/setup-prepare-for-launch.md` | Launch your store {#remove-your-online-store-password} | 2026-10-18 | kind: stated | quote check: found
- quote: During your free trial, your online store is automatically in private mode. In private mode, your site's pages are inaccessible, and a customizable landing page with a password option is displayed instead.
- title: Preparing your Shopify store for launch
- the page opens: Before you launch your store, place some test orders to review how the checkout process works. When you're ready, you can launch your store to change access from private to public. Placing a test order By placing a test order, you can make sure that your settings for the following parts of your store are working correctly: * checkout process * order processing * inventory * shipping * taxes Charges don't apply to test orders. You should place at least one test order during your store setup, or w…
- a note box: Note If you want your store to be displayed in the Shop app, then launching your store is one of the Shop merchant requirements. After you launch your store, it can take up to 48 hours for your Shop eligibility status to update.
- headings: Preparing your Shopify store for launch > Launch your store {#remove-your-online-store-password}
- in context: …Shopify admin, click **Online Store**. Then, click **Preview store**. Learn more about [navigating your theme preview](/manual/online-store/themes/adding-themes#theme-preview). The preview opens in a new tab and displays your store as it would be displayed to a customer. To return to the Shopify admin, return to your previous tab or click **Navigate to admin** at the bottom of the screen. ## Launch your store {#remove-your-online-store-password} ⟪During your free trial, your online store is automatically in private mode. In private mode, your site's pages are inaccessible, and a customizable landing page with a password option is displayed instead.⟫ You can [create a password and add a custom message](/manual/online-store/themes/password-page) for your customers when they visit your store. Before you can launch your store, you must complete the following required steps: * Select a subscription plan. If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires. * Add a store address to the **Business details** section of the **Settings…

### Q3-SH-028

**Cited at:** section 1, line 9; section 1, line 23; section 2, line 88; section 2, line 98

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-028
- bears_on: 1;4
- identifier: Launch your store
- statement: Before you can launch your store, you must complete the following required steps: * Select a subscription plan. If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires. * Add a store address to the **Business details** section of the **Settings** > **General** page. * Set up a payment method, and make sure that test mode is deactivated.
- cite_ids: Q3-SH-C040;Q3-SH-C041;Q3-SH-C042;Q3-SH-C043
- from: held

**Citation Q3-SH-C040:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/setup-prepare-for-launch.md` | Launch your store | 2026-10-18 | kind: stated | quote check: found
- quote: Before you can launch your store, you must complete the following required steps:
- title: Preparing your Shopify store for launch
- the page opens: Before you launch your store, place some test orders to review how the checkout process works. When you're ready, you can launch your store to change access from private to public. Placing a test order By placing a test order, you can make sure that your settings for the following parts of your store are working correctly: * checkout process * order processing * inventory * shipping * taxes Charges don't apply to test orders. You should place at least one test order during your store setup, or w…
- a note box: Note If you want your store to be displayed in the Shop app, then launching your store is one of the Shop merchant requirements. After you launch your store, it can take up to 48 hours for your Shop eligibility status to update.
- headings: Preparing your Shopify store for launch > Launch your store {#remove-your-online-store-password}
- in context: …te to admin** at the bottom of the screen. ## Launch your store {#remove-your-online-store-password} During your free trial, your online store is automatically in private mode. In private mode, your site's pages are inaccessible, and a customizable landing page with a password option is displayed instead. You can [create a password and add a custom message](/manual/online-store/themes/password-page) for your customers when they visit your store. ⟪Before you can launch your store, you must complete the following required steps:⟫ * Select a subscription plan. If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires. * Add a store address to the **Business details** section of the **Settings** > **General** page. * Set up a payment method, and make sure that test mode is deactivated. <aside class="note"><h4>Note</h4><p>If you want your store to be displayed in the Shop app, then launching your store is one of th…

**Citation Q3-SH-C041:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/setup-prepare-for-launch.md` | Launch your store, list item 1 | 2026-10-18 | kind: stated | quote check: found
- quote: Select a subscription plan. If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires.
- title: Preparing your Shopify store for launch
- the page opens: Before you launch your store, place some test orders to review how the checkout process works. When you're ready, you can launch your store to change access from private to public. Placing a test order By placing a test order, you can make sure that your settings for the following parts of your store are working correctly: * checkout process * order processing * inventory * shipping * taxes Charges don't apply to test orders. You should place at least one test order during your store setup, or w…
- a note box: Note If you want your store to be displayed in the Shop app, then launching your store is one of the Shop merchant requirements. After you launch your store, it can take up to 48 hours for your Shop eligibility status to update.
- headings: Preparing your Shopify store for launch > Launch your store {#remove-your-online-store-password}
- in context: …-store-password} During your free trial, your online store is automatically in private mode. In private mode, your site's pages are inaccessible, and a customizable landing page with a password option is displayed instead. You can [create a password and add a custom message](/manual/online-store/themes/password-page) for your customers when they visit your store. Before you can launch your store, you must complete the following required steps: * ⟪Select a subscription plan. If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires.⟫ * Add a store address to the **Business details** section of the **Settings** > **General** page. * Set up a payment method, and make sure that test mode is deactivated. <aside class="note"><h4>Note</h4><p>If you want your store to be displayed in the Shop app, then launching your store is one of the <a href="/en/manual/online-sales-channels/shop/eligibility/requirements">Shop merchant requirements</a>. After you launch your store, it can take u…

**Citation Q3-SH-C042:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/setup-prepare-for-launch.md` | Launch your store, list item 2 | 2026-10-18 | kind: stated | quote check: found (markup removed)
- quote: Add a store address to the Business details section of the Settings > General page.
- title: Preparing your Shopify store for launch
- the page opens: Before you launch your store, place some test orders to review how the checkout process works. When you're ready, you can launch your store to change access from private to public. Placing a test order By placing a test order, you can make sure that your settings for the following parts of your store are working correctly: * checkout process * order processing * inventory * shipping * taxes Charges don't apply to test orders. You should place at least one test order during your store setup, or w…
- a note box: Note If you want your store to be displayed in the Shop app, then launching your store is one of the Shop merchant requirements. After you launch your store, it can take up to 48 hours for your Shop eligibility status to update.
- headings: Preparing your Shopify store for launch > Launch your store {#remove-your-online-store-password}
- in context: …mode, your site's pages are inaccessible, and a customizable landing page with a password option is displayed instead. You can create a password and add a custom message for your customers when they visit your store. Before you can launch your store, you must complete the following required steps: * Select a subscription plan. If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires. * ⟪Add a store address to the Business details section of the Settings > General page.⟫ * Set up a payment method, and make sure that test mode is deactivated. Note If you want your store to be displayed in the Shop app, then launching your store is one of the Shop merchant requirements. After you launch your store, it can take up to 48 hours for your Shop eligibility status to update. When you're ready to launch your online store, you can launch from any of the following areas of your Shopify admin: * From the access setting menu …  (matched markup removed)

**Citation Q3-SH-C043:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/intro-to-shopify/initial-setup/setup-prepare-for-launch.md` | Launch your store, list item 3 | 2026-10-18 | kind: stated | quote check: found
- quote: Set up a payment method, and make sure that test mode is deactivated.
- title: Preparing your Shopify store for launch
- the page opens: Before you launch your store, place some test orders to review how the checkout process works. When you're ready, you can launch your store to change access from private to public. Placing a test order By placing a test order, you can make sure that your settings for the following parts of your store are working correctly: * checkout process * order processing * inventory * shipping * taxes Charges don't apply to test orders. You should place at least one test order during your store setup, or w…
- a note box: Note If you want your store to be displayed in the Shop app, then launching your store is one of the Shop merchant requirements. After you launch your store, it can take up to 48 hours for your Shop eligibility status to update.
- headings: Preparing your Shopify store for launch > Launch your store {#remove-your-online-store-password}
- in context: …rd and add a custom message](/manual/online-store/themes/password-page) for your customers when they visit your store. Before you can launch your store, you must complete the following required steps: * Select a subscription plan. If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires. * Add a store address to the **Business details** section of the **Settings** > **General** page. * ⟪Set up a payment method, and make sure that test mode is deactivated.⟫ <aside class="note"><h4>Note</h4><p>If you want your store to be displayed in the Shop app, then launching your store is one of the <a href="/en/manual/online-sales-channels/shop/eligibility/requirements">Shop merchant requirements</a>. After you launch your store, it can take up to 48 hours for your Shop eligibility status to update.</p> </aside> When you're ready to launch your online store, you can launch from any of the following areas of yo…

### Q3-SH-109

**Cited at:** section 1, line 9; section 2, line 98

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-109
- bears_on: 1;4
- identifier: Online Store > Preferences (admin /online_store/preferences), Store access, Private mode
- statement: Displays a landing page that requires a password to enter your store [label: Restrict access to visitors with the password, currently on] Your online store is in development. To let visitors access your store, give them the password.
- scope: store capture-plus, observed 2026-10-04
- cite_ids: Q3-SH-C153
- from: held
- note: In the saved HTML of step 1, frame 0; the step's steps/001.frame-0.aria.yaml shows the same words, apart from the label. The label is an attribute as the markup states it. Observation of one store on one date.

**Citation Q3-SH-C153:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T115543Z-storefront-page-types/001.frame-0.html.txt` | run 20261004T115543Z-storefront-page-types, step 1, frame 0 (online_store/preferences) | 2026-10-04 | kind: observed | quote check: found
- step 1: open Online Store > Preferences (store access and its password) | https://admin.shopify.com/store/capture-plus/online_store/preferences | "capture plus · Preferences · Shopify Plus" | 2026-10-04T11:55:49.060Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T115543Z-storefront-page-types/steps/001.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T115543Z-storefront-page-types/steps/001.frame-0.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T115543Z-storefront-page-types/steps/001.frame-0.html`, `observed-sh@febbf6c98:raw/runs/20261004T115543Z-storefront-page-types/steps/001.frame-1.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T115543Z-storefront-page-types/steps/001.frame-1.html`, `observed-sh@febbf6c98:raw/runs/20261004T115543Z-storefront-page-types/steps/001.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T115543Z-storefront-page-types/001.frame-0.html.txt`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T115543Z-storefront-page-types/001.frame-1.html.txt`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T115543Z-storefront-page-types/001.html.txt`
- quote: Displays a landing page that requires a password to enter your store [label: Restrict access to visitors with the password, currently on] Your online store is in development. To let visitors access your store, give them the password. Learn more
- in context: [heading: Preferences] [accessibilitylabel: Themes] Submit [heading: Store access] Private mode [accessibilitylabel: Learn more] Learn more ⟪Displays a landing page that requires a password to enter your store [label: Restrict access to visitors with the password, currently on] Your online store is in development. To let visitors access your store, give them the password. Learn more⟫ Password [liagag] 6 of 100 characters used Message to your visitors 0 of 5,000 characters used Restrict access to B2B customers only [accessibilitylabel: Learn more] Learn more B2B customers will need to log in and verify their account to access your store. Manage companies [label: Restrict access to B2B customers only, currently off] [heading: Social sharing image and SEO] [accessibilitylabel: Learn more] Learn more Upload image [accessibilityl…

### Q3-SH-K1536

**Cited at:** section 1, line 16; section 2, line 83; section 5, line 147

**The same record as Q1-SH-K1536,** whose card is in `Q1-shopify-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Your Role. To utilize the Payments Services, you must be a business located in your Designated Country.
- scope: 

### Q3-SH-100

**Cited at:** section 1, line 17

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-100
- bears_on: 1;4
- identifier: ShopifyPaymentsData: businessEntity.shopifyPayments (name, eligible, idVerificationForOnboardingRequired, idVerificationOutcome, missingAttributesInfo)
- statement: "name":"Shopify Payments","eligible":false,"cardPresentSupported":false,"transactionFee":0.0,"discountedTransactionFee":0.0,"discountedTransactionFeeEndedAt":"2026-10-02T06:00:00Z","idVerificationForOnboardingRequired":false,"idVerificationOutcome":null,"missingAttributesInfo":null
- scope: store fake-demo-sharrwah, observed 2026-10-05; Business details: My Store - entity, Yemen; Currency display: Yemeni Rial (YER)
- cite_ids: Q3-SH-C140;Q3-SH-C141;Q3-SH-C142
- from: held
- note: Observation of one store on one date.

**Citation Q3-SH-C140:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/answers/admin.shopify.com/ShopifyPaymentsData/a54107f80a0b8ccbde8f087b4e5edaad86d8f1a4d67af7212a07bc4049cfa3d8.json` | ShopifyPaymentsData, store fake-demo-sharrwah, step 376 (also steps 164, 357) | 2026-10-05 | kind: observed | quote check: found
- quote: "name":"Shopify Payments","eligible":false,"cardPresentSupported":false,"transactionFee":0.0,"discountedTransactionFee":0.0,"discountedTransactionFeeEndedAt":"2026-10-02T06:00:00Z","idVerificationForOnboardingRequired":false,"idVerificationOutcome":null,"missingAttributesInfo":null
- in context: {"data":{"businessEntity":{"id":"gid://shopify/BusinessEntity/47940239575","shopifyPayments":{"id":"gid://shopify/PaymentProvider/87",⟪"name":"Shopify Payments","eligible":false,"cardPresentSupported":false,"transactionFee":0.0,"discountedTransactionFee":0.0,"discountedTransactionFeeEndedAt":"2026-10-02T06:00:00Z","idVerificationForOnboardingRequired":false,"idVerificationOutcome":null,"missingAttributesInfo":null⟫,"paymentMethods":[{"name":"visa","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"mastercard","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"american_express","type":"CREDIT_CARD","__typename":"PaymentMethod"},{"name":"apple_pay","type":"WALLET","__typename":"PaymentMethod"},{"name":"google_pay","type":"WALLET","__typename":"PaymentMethod"}],"configuration":null,"__typename":"PaymentProvider"},"localPaymentMethodsForMerch…

**Citation Q3-SH-C141:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.text.txt` | step 477 (settings/general), Business details | 2026-10-05 | kind: observed | quote check: found
- step 477: visit route settings:general (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath)) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/general | "My Store · General · Shopify" | 2026-10-05T05:35:19.867Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.html`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.text.txt`
- quote: Business entity used for financial products, markets, apps, and taxes in this shop My Store - entity Yemen
- in context: …s Growth Discounts Content Markets Analytics Sales channels Apps Settings MS Settings [Search] My Store fake-demo-sharrwah.myshopify.com MS General Plan Billing Users Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com General General Business details ⟪Business entity used for financial products, markets, apps, and taxes in this shop My Store - entity Yemen⟫ Store contact details My Store 7amza.it@gmail.com · No phone number Store address Sanaa, Yemen Submit Store defaults Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER) Backup Region Yemen [Yemen] Determines settings for customers outside of your markets Unit system Metric system [Metric system] Default weight unit Kilogram (kg) [Kilogram (kg)] Time zone (GMT+03:00) Riyadh [(GMT+03:00) Riyadh] Sets the time f…

**Citation Q3-SH-C142:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.text.txt` | step 477 (settings/general), Store defaults | 2026-10-05 | kind: observed | quote check: found
- step 477: visit route settings:general (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath)) | https://admin.shopify.com/store/fake-demo-sharrwah/settings/general | "My Store · General · Shopify" | 2026-10-05T05:35:19.867Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.html`, `observed-sh@febbf6c98:raw/runs/20261005T013804Z-sweep-paid-store/steps/477.text.txt`
- quote: Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER)
- in context: … Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies Demo-name demo-last-name 7amza.it@gmail.com General General Business details Business entity used for financial products, markets, apps, and taxes in this shop My Store - entity Yemen Store contact details My Store 7amza.it@gmail.com · No phone number Store address Sanaa, Yemen Submit Store defaults ⟪Currency display To manage the currencies customers see, go to Markets Yemeni Rial (YER)⟫ Backup Region Yemen [Yemen] Determines settings for customers outside of your markets Unit system Metric system [Metric system] Default weight unit Kilogram (kg) [Kilogram (kg)] Time zone (GMT+03:00) Riyadh [(GMT+03:00) Riyadh] Sets the time for when orders and analytics are recorded To change your user level time zone and language visit your account settings Order ID format Shown on the order page, customer pages, and customer order notificatio…

### Q3-SH-012

**Cited at:** section 1, line 21; section 5, line 145

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-012
- bears_on: 1;4
- identifier: Information requirements for Shopify Payments
- statement: Shopify and its banking partners are required to collect and verify information about you and your business, to comply with regulations that are designed to prevent financial crimes. As local rules and regulations evolve, you might be contacted by Shopify and its banking partners to provide additional information throughout the lifespan of your Shopify Payments account.
- cite_ids: Q3-SH-C013;Q3-SH-C014
- from: held

**Citation Q3-SH-C013:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | Information requirements for Shopify Payments | 2026-10-18 | kind: stated | quote check: found
- quote: Shopify and its banking partners are required to collect and verify information about you and your business, to comply with regulations that are designed to prevent financial crimes.
- title: Setting up your Shopify Payments account
- the page opens: To get started with Shopify Payments, first check the list of supported countries to confirm availability in your region. After confirming your eligibility, you can activate the service and complete the verification process. Your Shopify Payments payouts might be placed on hold until two-step authentication is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your store currency bef…
- a note box: Staff permissions Only the store owner can activate or switch to Shopify Payments. Staff members can't switch to Shopify Payments.
- a note box: Note Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- headings: Setting up your Shopify Payments account > Information requirements for Shopify Payments {#documents}
- in context: …-methods} Some local payment methods for Shopify Payments require additional approval before they can be activated. Once you activate Shopify Payments, the review process for applicable [local payment methods](/manual/payments/shopify-payments/local-payment-methods) begins automatically and approved payment methods will become available for you to activate in the payment methods page. ## Information requirements for Shopify Payments {#documents} ⟪Shopify and its banking partners are required to collect and verify information about you and your business, to comply with regulations that are designed to prevent financial crimes.⟫ As local rules and regulations evolve, you might be contacted by Shopify and its banking partners to provide additional information throughout the lifespan of your Shopify Payments account. The information that is collected is used to confirm the identity of the business, the identities of individuals linked to it, and the nature of the relationship between the two. Shopify never physically mails documentation to you. Any important documents or …

**Citation Q3-SH-C014:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | Information requirements for Shopify Payments | 2026-10-18 | kind: stated | quote check: found
- quote: As local rules and regulations evolve, you might be contacted by Shopify and its banking partners to provide additional information throughout the lifespan of your Shopify Payments account.
- title, opening and note boxes: as for this source's citation above
- headings: Setting up your Shopify Payments account > Information requirements for Shopify Payments {#documents}
- in context: …le [local payment methods](/manual/payments/shopify-payments/local-payment-methods) begins automatically and approved payment methods will become available for you to activate in the payment methods page. ## Information requirements for Shopify Payments {#documents} Shopify and its banking partners are required to collect and verify information about you and your business, to comply with regulations that are designed to prevent financial crimes. ⟪As local rules and regulations evolve, you might be contacted by Shopify and its banking partners to provide additional information throughout the lifespan of your Shopify Payments account.⟫ The information that is collected is used to confirm the identity of the business, the identities of individuals linked to it, and the nature of the relationship between the two. Shopify never physically mails documentation to you. Any important documents or communications are emailed, or made digitally available to the person listed as Account Owner of the store in your Shopify admin. ## Uploading documents for Shopify Payments verification {#r…

### Q3-SH-041

**Cited at:** section 1, line 22; section 2, line 89; section 3, line 114

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-041
- bears_on: 1;4
- identifier: Proof of Liveness check
- statement: The requirement for a Proof of Liveness check for Shopify Payments is based on your country.
- cite_ids: Q3-SH-C056
- from: held

**Citation Q3-SH-C056:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/proof-of-liveness.md` | Proof of Liveness check | 2026-10-18 | kind: stated | quote check: found
- quote: The requirement for a Proof of Liveness check for Shopify Payments is based on your country.
- title: Proof of Liveness check
- the page opens: The requirement for a Proof of Liveness check for Shopify Payments is based on your country. Learn more about supported countries and documentation requirements. To complete a Proof of Liveness check, you'll use your webcam or phone to upload a selfie. You also need to verify your photo ID using one of the following methods: * Use your webcam or phone to take a photo of your ID document. * Upload a photo of your ID document. Only the account owner can complete a Liveness check and photo ID verif…
- headings: Proof of Liveness check
- in context: # Proof of Liveness check ⟪The requirement for a Proof of Liveness check for Shopify Payments is based on your country.⟫ Learn more about [supported countries and documentation requirements](/manual/payments/shopify-payments/supported-countries). To complete a Proof of Liveness check, you'll use your webcam or phone to upload a selfie. You also need to verify your photo ID using one of the following methods: * Use your webcam or phone to take a photo of your ID document. * Upload a photo of your ID document. Only the account owner can complete a Liveness check and…

### Q3-SH-111

**Cited at:** section 1, line 22; section 3, line 115

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-111
- bears_on: 1
- identifier: Organization > Edit business details (admin /settings/organization-details/business-details), Individual, United States, Social Security Number (SSN)
- statement: Social Security Number (SSN) [xxx-xx-xxxx] 9 digits. Used for tax filing and verification. Use ITIN instead.
- scope: store capture-advanced, observed 2026-10-04
- cite_ids: Q3-SH-C155
- from: held
- note: In the saved HTML of step 13, after a United States business entity was saved with other fields empty; [xxx-xx-xxxx] is the field's placeholder as the markup states it. The step's steps/013.aria.yaml shows the same words, apart from the placeholder. Observation of one store on one date.

**Citation Q3-SH-C155:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20261004T223401Z-journey-business-entity/013.html.txt` | run 20261004T223401Z-journey-business-entity, step 13 (settings/organization-details/business-details) | 2026-10-04 | kind: observed | quote check: found
- step 13: Save (US entity, other fields empty) | https://admin.shopify.com/store/capture-advanced/settings/organization-details/business-details/197525452 | "capture advanced · Organization · Add business entity · Shopify" | 2026-10-04T22:37:27.792Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/013.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261004T223401Z-journey-business-entity/steps/013.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20261004T223401Z-journey-business-entity/013.html.txt`
- quote: Social Security Number (SSN) [xxx-xx-xxxx] 9 digits. Used for tax filing and verification. Use ITIN instead.
- in context: … Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: Edit business details] Archive [accessibilitylabel: Organization] [heading: About your business] What type of business do you have? Country code What type of business do you have? Individual [label: Nickname] First name [Capture] Last name [Entity] Date of birth Month [Month] DD [DD] YYYY [YYYY] Residential address Apartment, suite, etc City State [Select a state] Select a state ZIP code ⟪Social Security Number (SSN) [xxx-xx-xxxx] 9 digits. Used for tax filing and verification. Use ITIN instead.⟫ Add personal information Country [Select...] United States Individual Taxpayer Identification Number Driver's License Number Passport Number [accessibilitylabel: Show optional fields] Show optional fields Business entity created successfully Close [heading: Archive Capture Entity?] Archive Cancel Are you sure you want to archive this legal entity? This action cannot be undone and will remove this entity from active use.

### Q3-SH-K1274

**Cited at:** section 1, line 23; section 2, line 88

**Record** (`studies/proposals/records/Q3/shopify/copied.tsv`):
- concern_id: SH-C-007
- placement: decides
- structure: https://help.shopify.com/en/manual/payments/shopify-payments.md
- identifier: Note (requirements)
- statement: To use Shopify Payments, you must secure your account with <a href="/en/manual/your-account/logging-in/secure-sign-in">two-step authentication</a>.
- scope: stores using Shopify Payments
- cite_ids: SH-S-0260
- note: first run's citation

**Citation SH-S-0260:** `https://help.shopify.com/en/manual/payments/shopify-payments.md` | Note (requirements) | 2026-10-10 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/059-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:01Z, captured)
- quote: To use Shopify Payments, you must secure your account with <a href="/en/manual/your-account/logging-in/secure-sign-in">two-step authentication</a>.
- title: Shopify Payments
- the page opens: Shopify Payments is the simplest way to accept payments online. It eliminates the hassle of setting up a third-party payment provider or merchant account and having to enter the credentials into Shopify. With Shopify Payments you're automatically set up to accept all major payment methods as soon as you create your Shopify store. If you already use a direct third-party payment provider, then you can also use Shopify Payments alongside your existing provider to offer additional payment methods su…
- a note box: Note Before you use Shopify Payments, review the following requirements: Shopify Payments is only available to online stores in certain countries and regions. If you operate a retail store, then check the list of countries that support Shopify Payments for in-person selling. To use Shopify Payments,
- headings: Shopify Payments
- in context: … Payments, review the following requirements:</p> <ul> <li>Shopify Payments is only available to online stores in <a href="/en/manual/payments/shopify-payments/supported-countries">certain countries and regions</a>. If you operate a retail store, then check the <a href="/en/manual/sell-in-person/getting-started/setup-payment-method/shopify-payments-pos#supported">list of countries that support Shopify Payments for in-person selling</a>.</li> <li>⟪To use Shopify Payments, you must secure your account with <a href="/en/manual/your-account/logging-in/secure-sign-in">two-step authentication</a>.⟫ Learn more about <a href="/en/manual/privacy-and-security/account-security">account security</a>. If you deactivate two-step authentication in the future, then you expose your account and financial information to potential criminal attacks.</li> </ul> </aside> When you use [Shopify Payments](/manual/payments/shopify-payments), you aren't charged third-party transaction fees for orders that are processed through Shopify Payments, Shop Pay, and Sh…

### Q3-SH-107

**Cited at:** section 1, line 23

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-107
- bears_on: 1
- identifier: Payments (admin /settings/payments), Secure your account with two-step authentication
- statement: [heading: Secure your account with two-step authentication] Set up two-step You need to set-up two-step authentication before adding a bank account.
- scope: store ibx5bt-xy, observed 2026-09-30
- cite_ids: Q3-SH-C151
- from: held
- note: In the saved HTML of step 376, in a dialog after a Close button; not between hidden markers. The step's steps/376.aria.yaml doesn't show these words; the saved markup doesn't say whether the dialog was open. The same sentence is in the saved HTML of step 387 (Third-party payment providers) and step 154 (capital:bankAccountDetails) of the same run. Adds to Q3-SH-K1274 and Q3-SH-103.

**Citation Q3-SH-C151:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/376.html.txt` | run 20260930T045741Z-sweep-trial2, step 376 (settings/payments) | 2026-09-30 | kind: observed | quote check: found
- step 376: visit route payments:settings (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:index,payments:settings:secondary-gateways) | https://admin.shopify.com/store/ibx5bt-xy/settings/payments | "My Store · Payments · Shopify" | 2026-09-30T07:52:56.988Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/376.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/376.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/376.html.txt`
- quote: [heading: Secure your account with two-step authentication] Set up two-step You need to set-up two-step authentication before adding a bank account.
- in context: … that enable you to accept payment methods at a rate set by the third-party. An additional fee will apply to new orders once you select a plan . Choose a provider Additional payment providers Offer methods processed offsite or through custom checkout integrations Add [heading: Payment configuration] Payment capture method Manual payment methods Payment method customizations Gift card expiration Apple Wallet passes Learn more about payments Close ⟪[heading: Secure your account with two-step authentication] Set up two-step You need to set-up two-step authentication before adding a bank account.⟫ Two-step authentication helps secure your important details. Once it's turned on, it's much more difficult for unauthorized persons to access your account. With two-step authentication, you can login more securely by using methods such as fingerprint sensor or push notifications. If two-step authentication isn't turned on, your account may be less secure. You may also have your payouts paused. Learn more about two-step authentication .

### Q3-SH-106

**Cited at:** section 1, line 23; section 2, line 94

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-106
- bears_on: 1;4
- identifier: Payments (admin /settings/payments), heading and paragraph
- statement: [heading: Development stores can only process test payments] Activate the test payment provider , or set your payment provider to test mode.
- scope: store demo-fake-dev-store, observed 2026-09-30
- cite_ids: Q3-SH-C150
- from: held
- note: In the saved HTML of step 376; the step's steps/376.aria.yaml shows the same heading and words. The saved HTML of step 376 in runs 20261002T003831Z-sweep-capture-plus and 20261002T004032Z-sweep-capture-grow holds the same heading and paragraph. Observation of one store on one date.

**Citation Q3-SH-C150:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T103225Z-sweep-dev/376.html.txt` | run 20260930T103225Z-sweep-dev, step 376 (settings/payments) | 2026-09-30 | kind: observed | quote check: found
- step 376: visit route payments:settings (path from router; computed segment ${o.settings()} = "settings" (common-205e414c721f.js: ft="settings", routePath); same path: payments:settings:index,payments:settings:secondary-gateways) | https://admin.shopify.com/store/demo-fake-dev-store/settings/payments | "demo fake dev store · Payments · Shopify" | 2026-09-30T12:45:01.856Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/376.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T103225Z-sweep-dev/steps/376.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T103225Z-sweep-dev/376.html.txt`
- quote: [heading: Development stores can only process test payments] Activate the test payment provider , or set your payment provider to test mode. Learn more about testing in development stores .
- in context: …k [Search] My Store 2 stores Organization Users Billing demo fake dev store demo-fake-dev-store.myshopify.com [initials: ds] [alt: demo fake dev store] General Plan Payments Checkout Customer accounts Shipping and delivery Taxes and duties Locations Apps Sales channels Domains Customer events Notifications Metafields and metaobjects Languages Customer privacy Policies [initials: Dd] Demo-name demo-last-name 7amza.it@gmail.com [heading: Payments] ⟪[heading: Development stores can only process test payments] Activate the test payment provider , or set your payment provider to test mode. Learn more about testing in development stores .⟫ Submit [heading: Test payment gateway] Payment methods [accessibilitylabel: Test payment gateway] Additional payment providers Offer methods processed offsite or through custom checkout integrations Add [heading: Payment configuration] Payment capture method Manual payment methods Payment method customizations Gift card expiration Apple Wallet passes Learn more about payments [heading: Keyboard Shortcuts] General shortcuts Keyboard help ? Focus …

### Q3-SH-101

**Cited at:** section 1, line 24

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-101
- bears_on: 1;4
- identifier: Orders page (admin /orders), empty state
- statement: To get orders and accept payments from customers, you need to select a plan. You’ll only be charged for your plan after your free trial ends.
- scope: store ts15uk-ug, observed 2026-10-07; Trial ends in 1 day
- cite_ids: Q3-SH-C143;Q3-SH-C144
- from: held
- note: Observation of one store on one date.

**Citation Q3-SH-C143:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.text.txt` | step 346 (orders) | 2026-10-07 | kind: observed | quote check: found
- step 346: visit route orders (path from router; same path: order:list,order:return-label:parent) | https://admin.shopify.com/store/ts15uk-ug/orders | "My Store 8 · Orders · Shopify" | 2026-10-07T00:54:06.306Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.html`, `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.text.txt`
- quote: To get orders and accept payments from customers, you need to select a plan. You’ll only be charged for your plan after your free trial ends.
- in context: Skip to content Search CTRL K 1 MS8 My Store 8 Home Orders Drafts Products Customers Growth Discounts Content Markets Analytics Sales channels Online Store Agentic Apps Add Settings Trial ends in 1 day Subscribe for $1 Select a plan Orders More actions Your orders will show here ⟪To get orders and accept payments from customers, you need to select a plan. You'll only be charged for your plan after your free trial ends.⟫ Select plan Learn more about orders New conversation New conversation Where should we begin? Work with Sidekick

**Citation Q3-SH-C144:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.text.txt` | step 346 (orders), page header | 2026-10-07 | kind: observed | quote check: found
- step 346: visit route orders (path from router; same path: order:list,order:return-label:parent) | https://admin.shopify.com/store/ts15uk-ug/orders | "My Store 8 · Orders · Shopify" | 2026-10-07T00:54:06.306Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.html`, `observed-sh@febbf6c98:raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/346.text.txt`
- quote: Trial ends in 1 day
- in context: Skip to content Search CTRL K 1 MS8 My Store 8 Home Orders Drafts Products Customers Growth Discounts Content Markets Analytics Sales channels Online Store Agentic Apps Add Settings ⟪Trial ends in 1 day⟫ Subscribe for $1 Select a plan Orders More actions Your orders will show here To get orders and accept payments from customers, you need to select a plan. You'll only be charged for your plan after your free trial ends. Select plan Learn more about orders New conversation New conversation Where should we begin? Work with Sidekick

### Q3-SH-057

**Cited at:** section 1, line 25; section 3, line 108; section 3, line 117; section 3, line 127; section 7, line 169

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-057
- bears_on: 1;4
- identifier: American Express requirements for Shopify Payments
- statement: American Express sets its own requirements for the addresses and the names recorded on a payment account. These requirements apply to your Shopify Payments account in addition to the general Shopify Payments eligibility requirements.
- cite_ids: Q3-SH-C085
- from: held

**Citation Q3-SH-C085:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/american-express-requirements.md` | American Express requirements for Shopify Payments | 2026-10-18 | kind: stated | quote check: found (markup removed)
- quote: American Express sets its own requirements for the addresses and the names recorded on a payment account. These requirements apply to your Shopify Payments account in addition to the general Shopify Payments eligibility requirements.
- title: American Express requirements for Shopify Payments
- the page opens: American Express sets its own requirements for the addresses and the names recorded on a payment account. These requirements apply to your Shopify Payments account in addition to the general Shopify Payments eligibility requirements. If a detail on your account doesn't meet these requirements, then American Express stops being available at checkout in your store. Your store keeps accepting other card brands throughout. In some cases you're contacted by Shopify Trust teams and asked to make the u…
- headings: American Express requirements for Shopify Payments
- in context: American Express requirements for Shopify Payments ⟪American Express sets its own requirements for the addresses and the names recorded on a payment account. These requirements apply to your Shopify Payments account in addition to the general Shopify Payments eligibility requirements.⟫ If a detail on your account doesn't meet these requirements, then American Express stops being available at checkout in your store. Your store keeps accepting other card brands throughout. In some cases you're contacted by Shopify Trust teams and asked to make the update by a specific date instead. American Express stays available at checkout until that date passes. When American Express is unavailable at checkout, your payment methods settings …  (matched markup removed)

### Q3-SH-110

**Cited at:** section 1, line 25; section 2, line 85; section 3, line 126

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-110
- bears_on: 1;4
- identifier: Shop Pay Installments Terms of Service (admin /shop-pay-installments/terms), 2. Access to Affirm Services
- statement: Affirm reserves the right to deny you access to the Affirm Services. We will require you to provide certain information when requesting access to the Affirm Services through Shop Pay Installments, including, but not limited to, information that identifies you and your beneficial owners. The information may include your name, address and tax identification number and the name, address, date of birth and tax identification or social security number of your beneficial owners or controlling persons.
- scope: store ibx5bt-xy, observed 2026-09-30
- cite_ids: Q3-SH-C154
- from: held
- note: In the saved HTML of step 408; the step's steps/408.aria.yaml shows the same words.

**Citation Q3-SH-C154:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/408.html.txt` | run 20260930T045741Z-sweep-trial2, step 408 (shop-pay-installments/terms) | 2026-09-30 | kind: observed | quote check: found
- step 408: visit route shop-pay-installments-terms (path from router) | https://admin.shopify.com/store/ibx5bt-xy/shop-pay-installments/terms | "Shopify" | 2026-09-30T08:06:08.061Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/408.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/408.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/408.html.txt`
- quote: Affirm reserves the right to deny you access to the Affirm Services. We will require you to provide certain information when requesting access to the Affirm Services through Shop Pay Installments, including, but not limited to, information that identifies you and your beneficial owners.
- in context: …ou use the Affirm Services. These Shop Pay Installments Terms and the Shopify TOS are collectively, the " Agreement ". 1. Use of Affirm Services and Acceptance of Affirm Terms You wish to use the Affirm Services through Shop Pay Installments. By accepting the Shop Pay Installments Terms of Service you are also accepting and agreeing to be bound by the Affirm Terms, which is the legal agreement between you and Affirm. 2. Access to Affirm Services ⟪Affirm reserves the right to deny you access to the Affirm Services. We will require you to provide certain information when requesting access to the Affirm Services through Shop Pay Installments, including, but not limited to, information that identifies you and your beneficial owners.⟫ The information may include your name, address and tax identification number and the name, address, date of birth and tax identification or social security number of your beneficial owners or controlling persons. Shopify will develop, operate, maintain, and host a secure application programming interface between the Affirm site and systems and Shopify's systems in order to enable access to and use of the Affirm Services (" Shopify-Affirm API ").…

### Q3-SH-062

**Cited at:** section 1, line 29

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-062
- bears_on: 1
- identifier: When bank account ownership verification is required
- statement: Verification compares the name on your bank account with information on your Shopify Payments account. This information can include your legal business name or account representative name.
- cite_ids: Q3-SH-C092
- from: held

**Citation Q3-SH-C092:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/bank-account-ownership-verification.md` | When bank account ownership verification is required | 2026-10-18 | kind: stated | quote check: found
- quote: Verification compares the name on your bank account with information on your Shopify Payments account. This information can include your legal business name or account representative name.
- title: Verifying ownership of your Shopify Payments bank account
- the page opens: When you use Shopify Payments, your payout bank account might need ownership verification. This check confirms that the bank account belongs to you or your business. If your bank account ownership can't be verified, then the store owner receives a notification in the Shopify admin and might also receive an email. You can review your bank account status in your Shopify Payments settings. When bank account ownership verification is required Bank account ownership verification might be required whe…
- headings: Verifying ownership of your Shopify Payments bank account > When bank account ownership verification is required
- in context: …fy admin and might also receive an email. You can review your bank account status in your [Shopify Payments settings](https://admin.shopify.com/settings/payments). ## When bank account ownership verification is required Bank account ownership verification might be required when you add or replace a payout bank account for Shopify Payments. You might also be asked to verify your bank account again if your Shopify Payments business details change. ⟪Verification compares the name on your bank account with information on your Shopify Payments account. This information can include your legal business name or account representative name.⟫ ## Ways to verify your bank account Depending on your region and account, you might be able to verify your bank account in one of the following ways: * Connect your bank account using your bank login. * Enter your bank account details manually. * Upload a supporting document, such as a bank statement, if more information is required. ## Verify your bank account Add or update your payout bank account in your Shopify Payments settings to start ban…

### Q3-SH-P0045

**Cited at:** section 1, line 34; section 1, line 61

**Record** (`studies/proposals/records/Q3/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-044
- bullet: e
- placement: decides
- identifier: Part I, B. Prohibited and Restricted Businesses
- statement: Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers.
- conditions: S01-SH-005;S01-SH-006;S01-SH-009;S01-SH-019;S01-SH-022;S01-SH-023;S01-SH-027
- cite_ids: S01-SH-C058
- from: index:SH-C-173:SH-S-0108

**Citation S01-SH-C058:** `https://www.shopify.com/legal/terms-shopify-payments` | Part I, B. Prohibited and Restricted Businesses | 2026-10-10 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/149-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/119-shopify.com/text.txt` (fetched 2026-10-12T10:51:25Z, captured)
- quote: Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers.
- title: Shopify Payments Terms of Service - Shopify
- in context: …he Payments Services and Shopify Payments Account may only be used in the Designated Country. By accepting this Agreement, you confirm that you will satisfy these requirements. Prohibited and Restricted Businesses. Certain categories of businesses and business practices are prohibited from using the Payments Services ("Prohibited Businesses"), or require additional review and approval by us to use the Payments Services ("Restricted Businesses"). ⟪Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers.⟫ The types of business categories and business practices that are considered Prohibited Businesses or Restricted Businesses are provided by each Payment Processor in your Designated Country and can be located at the links found in the Payment Processor List. These lists are meant to be representative but not exhaustive. If you are uncertain as to whether your business is a Prohibited Business or Restricted Business, or you have questions about ho…

### Q3-SH-095

**Cited at:** section 1, line 36; section 2, line 99; section 3, line 118

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-095
- bears_on: 1;3
- identifier: Payment options for hemp sales on Shopify
- statement: Shopify Payments doesn't support the sale of hemp, cannabidiol (CBD), and tetrahydrocannabinol (THC) products. To process the sales of hemp or hemp-derived products through your Shopify store, you can use third-party payment providers that are compatible with Shopify and support the sale of these products.
- cite_ids: Q3-SH-C132;Q3-SH-C133
- from: held

**Citation Q3-SH-C132:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/payments.md` | Payment options for hemp sales on Shopify | 2026-10-18 | kind: stated | quote check: found
- quote: Shopify Payments doesn't support the sale of hemp, cannabidiol (CBD), and tetrahydrocannabinol (THC) products.
- title: Payment options for hemp sales on Shopify
- the page opens: Shopify Payments doesn't support the sale of hemp, cannabidiol (CBD), and tetrahydrocannabinol (THC) products. To process the sales of hemp or hemp-derived products through your Shopify store, you can use third-party payment providers that are compatible with Shopify and support the sale of these products. Hemp transactions Third-party payment providers have a thorough vetting process for stores that apply to sell hemp through their services. Each payment provider may consider various factors su…
- headings: Payment options for hemp sales on Shopify
- in context: # Payment options for hemp sales on Shopify ⟪Shopify Payments doesn't support the sale of hemp, cannabidiol (CBD), and tetrahydrocannabinol (THC) products.⟫ To process the sales of hemp or hemp-derived products through your Shopify store, you can use third-party payment providers that are compatible with Shopify and support the sale of these products. ## Hemp transactions Third-party payment providers have a thorough vetting process for stores that apply to sell hemp through their services. Each payment provider may consider various factors such as product type, business creation date, transaction h…

**Citation Q3-SH-C133:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/payments.md` | Payment options for hemp sales on Shopify | 2026-10-18 | kind: stated | quote check: found
- quote: To process the sales of hemp or hemp-derived products through your Shopify store, you can use third-party payment providers that are compatible with Shopify and support the sale of these products.
- title, opening and note boxes: as for this source's citation above
- headings: Payment options for hemp sales on Shopify
- in context: # Payment options for hemp sales on Shopify Shopify Payments doesn't support the sale of hemp, cannabidiol (CBD), and tetrahydrocannabinol (THC) products. ⟪To process the sales of hemp or hemp-derived products through your Shopify store, you can use third-party payment providers that are compatible with Shopify and support the sale of these products.⟫ ## Hemp transactions Third-party payment providers have a thorough vetting process for stores that apply to sell hemp through their services. Each payment provider may consider various factors such as product type, business creation date, transaction history, volume, and product mix when approving payments and rates for stores selling hemp products. Approval decisions are at the discretion of each third-party payment provider, and Shopify can't …

### Q3-SH-053

**Cited at:** section 1, line 38; section 7, line 172

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-053
- bears_on: 1;3
- identifier: Hemp and hemp-derived product compliance statements, I confirm that:
- statement: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as long as it sells, or offers to sell, hemp and hemp-derived products. 2. The address listed in my Shopify admin matches the state from which I conduct my business. 3. My Shopify store operates from a jurisdiction where the online listing and sale of hemp and hemp-derived products is permitted by applicable federal, state, and local laws. I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US. 4. I will notify Shopify in writing to legal@shopify.com of any class action demand letter or Food and Drug Administration (FDA) or Federal Trade Commission (FTC) enforcement action commenced against my business, including any warning letters or other related correspondence within ten days of receipt. 5. Any time Shopify requests, I will provide documentation that confirms that my Shopify store, business, and cannabis products are in compliance with laws, regulations, and any of the requirements outlined here.
- scope: in the United States (US)
- cite_ids: Q3-SH-C071;Q3-SH-C072;Q3-SH-C073;Q3-SH-C074;Q3-SH-C075;Q3-SH-C076
- from: held

**Citation Q3-SH-C071:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/requirements-for-selling-hemp-in-the-united-states.md` | Hemp and hemp-derived product compliance statements, item 1 | 2026-10-18 | kind: stated | quote check: found
- quote: I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as long as it sells, or offers to sell, hemp and hemp-derived products.
- title: Requirements for selling hemp and hemp-derived products in the United States (US)
- the page opens: To sell hemp and hemp-derived products containing cannabidiol (CBD) on Shopify in the United States (US), you must ensure that you comply with the requirements described on this page. Remember, you always need to follow the laws of your store's location and the places you ship products. Hemp and hemp-derived product compliance statements I confirm that: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as l…
- a note box: Note If you require further guidance, then it's recommended to consult with a lawyer, as Shopify can't provide legal advice regarding what and where you can sell.
- headings: Requirements for selling hemp and hemp-derived products in the United States (US) > Hemp and hemp-derived product compliance statements > I confirm that:
- in context: # Requirements for selling hemp and hemp-derived products in the United States (US) To sell hemp and hemp-derived products containing cannabidiol (CBD) on Shopify in the United States (US), you must ensure that you comply with the requirements described on this page. Remember, you always need to follow the laws of your store's location and the places you ship products. ## Hemp and hemp-derived product compliance statements ### I confirm that: 1. ⟪I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as long as it sells, or offers to sell, hemp and hemp-derived products.⟫ 2. The address listed in my Shopify admin matches the state from which I conduct my business. 3. My Shopify store operates from a jurisdiction where the online listing and sale of hemp and hemp-derived products is permitted by applicable federal, state, and local laws. I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US. 4. I will notify Shopify in writing…

**Citation Q3-SH-C072:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/requirements-for-selling-hemp-in-the-united-states.md` | Hemp and hemp-derived product compliance statements, item 2 | 2026-10-18 | kind: stated | quote check: found
- quote: The address listed in my Shopify admin matches the state from which I conduct my business.
- title: Requirements for selling hemp and hemp-derived products in the United States (US)
- the page opens: To sell hemp and hemp-derived products containing cannabidiol (CBD) on Shopify in the United States (US), you must ensure that you comply with the requirements described on this page. Remember, you always need to follow the laws of your store's location and the places you ship products. Hemp and hemp-derived product compliance statements I confirm that: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as l…
- a note box: Note If you require further guidance, then it's recommended to consult with a lawyer, as Shopify can't provide legal advice regarding what and where you can sell.
- headings: Requirements for selling hemp and hemp-derived products in the United States (US) > Hemp and hemp-derived product compliance statements > I confirm that:
- in context: …ou comply with the requirements described on this page. Remember, you always need to follow the laws of your store's location and the places you ship products. ## Hemp and hemp-derived product compliance statements ### I confirm that: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as long as it sells, or offers to sell, hemp and hemp-derived products. 2. ⟪The address listed in my Shopify admin matches the state from which I conduct my business.⟫ 3. My Shopify store operates from a jurisdiction where the online listing and sale of hemp and hemp-derived products is permitted by applicable federal, state, and local laws. I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US. 4. I will notify Shopify in writing to legal@shopify.com of any class action demand letter or Food and Drug Administration (FDA) …

**Citation Q3-SH-C073:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/requirements-for-selling-hemp-in-the-united-states.md` | Hemp and hemp-derived product compliance statements, item 3 | 2026-10-18 | kind: stated | quote check: found
- quote: My Shopify store operates from a jurisdiction where the online listing and sale of hemp and hemp-derived products is permitted by applicable federal, state, and local laws.
- title: Requirements for selling hemp and hemp-derived products in the United States (US)
- the page opens: To sell hemp and hemp-derived products containing cannabidiol (CBD) on Shopify in the United States (US), you must ensure that you comply with the requirements described on this page. Remember, you always need to follow the laws of your store's location and the places you ship products. Hemp and hemp-derived product compliance statements I confirm that: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as l…
- a note box: Note If you require further guidance, then it's recommended to consult with a lawyer, as Shopify can't provide legal advice regarding what and where you can sell.
- headings: Requirements for selling hemp and hemp-derived products in the United States (US) > Hemp and hemp-derived product compliance statements > I confirm that:
- in context: …e laws of your store's location and the places you ship products. ## Hemp and hemp-derived product compliance statements ### I confirm that: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as long as it sells, or offers to sell, hemp and hemp-derived products. 2. The address listed in my Shopify admin matches the state from which I conduct my business. 3. ⟪My Shopify store operates from a jurisdiction where the online listing and sale of hemp and hemp-derived products is permitted by applicable federal, state, and local laws.⟫ I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US. 4. I will notify Shopify in writing to legal@shopify.com of any class action demand letter or Food and Drug Administration (FDA) or Federal Trade Commission (FTC) enforcement action commenced against my business, including any warning letters or other related correspondence within ten days of receipt. 5.…

**Citation Q3-SH-C074:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/requirements-for-selling-hemp-in-the-united-states.md` | Hemp and hemp-derived product compliance statements, item 3 | 2026-10-18 | kind: stated | quote check: found
- quote: I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US.
- title, opening and note boxes: as for this source's citation above
- headings: Requirements for selling hemp and hemp-derived products in the United States (US) > Hemp and hemp-derived product compliance statements > I confirm that:
- in context: …iness owner and have authority to bind my business to these statements. My business will follow these rules as long as it sells, or offers to sell, hemp and hemp-derived products. 2. The address listed in my Shopify admin matches the state from which I conduct my business. 3. My Shopify store operates from a jurisdiction where the online listing and sale of hemp and hemp-derived products is permitted by applicable federal, state, and local laws. ⟪I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US.⟫ 4. I will notify Shopify in writing to legal@shopify.com of any class action demand letter or Food and Drug Administration (FDA) or Federal Trade Commission (FTC) enforcement action commenced against my business, including any warning letters or other related correspondence within ten days of receipt. 5. Any time Shopify requests, I will provide documentation that confirms that my Shopify store, business, and cannabis products are in compliance …

**Citation Q3-SH-C075:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/requirements-for-selling-hemp-in-the-united-states.md` | Hemp and hemp-derived product compliance statements, item 4 | 2026-10-18 | kind: stated | quote check: found
- quote: I will notify Shopify in writing to legal@shopify.com of any class action demand letter or Food and Drug Administration (FDA) or Federal Trade Commission (FTC) enforcement action commenced against my business, including any warning letters or other related correspondence within ten days of receipt.
- title: Requirements for selling hemp and hemp-derived products in the United States (US)
- the page opens: To sell hemp and hemp-derived products containing cannabidiol (CBD) on Shopify in the United States (US), you must ensure that you comply with the requirements described on this page. Remember, you always need to follow the laws of your store's location and the places you ship products. Hemp and hemp-derived product compliance statements I confirm that: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as l…
- a note box: Note If you require further guidance, then it's recommended to consult with a lawyer, as Shopify can't provide legal advice regarding what and where you can sell.
- headings: Requirements for selling hemp and hemp-derived products in the United States (US) > Hemp and hemp-derived product compliance statements > I confirm that:
- in context: … hemp and hemp-derived products. 2. The address listed in my Shopify admin matches the state from which I conduct my business. 3. My Shopify store operates from a jurisdiction where the online listing and sale of hemp and hemp-derived products is permitted by applicable federal, state, and local laws. I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US. 4. ⟪I will notify Shopify in writing to legal@shopify.com of any class action demand letter or Food and Drug Administration (FDA) or Federal Trade Commission (FTC) enforcement action commenced against my business, including any warning letters or other related correspondence within ten days of receipt.⟫ 5. Any time Shopify requests, I will provide documentation that confirms that my Shopify store, business, and cannabis products are in compliance with laws, regulations, and any of the requirements outlined here. ## Compliance requirements for hemp and hemp-derived products ### I confirm that for all hemp and hemp-derived products listed or sold on my Shopify store: 1. Those products don't contain more than 0.3% tetrahydrocannabinol (THC) concen…

**Citation Q3-SH-C076:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/compliance/legal/hemp/requirements-for-selling-hemp-in-the-united-states.md` | Hemp and hemp-derived product compliance statements, item 5 | 2026-10-18 | kind: stated | quote check: found
- quote: Any time Shopify requests, I will provide documentation that confirms that my Shopify store, business, and cannabis products are in compliance with laws, regulations, and any of the requirements outlined here.
- title: Requirements for selling hemp and hemp-derived products in the United States (US)
- the page opens: To sell hemp and hemp-derived products containing cannabidiol (CBD) on Shopify in the United States (US), you must ensure that you comply with the requirements described on this page. Remember, you always need to follow the laws of your store's location and the places you ship products. Hemp and hemp-derived product compliance statements I confirm that: 1. I am the account owner or business owner and have authority to bind my business to these statements. My business will follow these rules as l…
- a note box: Note If you require further guidance, then it's recommended to consult with a lawyer, as Shopify can't provide legal advice regarding what and where you can sell.
- headings: Requirements for selling hemp and hemp-derived products in the United States (US) > Hemp and hemp-derived product compliance statements > I confirm that:
- in context: …I have all of the applicable state and local licenses, approvals, and certifications required to sell hemp and hemp-derived products in the US. 4. I will notify Shopify in writing to legal@shopify.com of any class action demand letter or Food and Drug Administration (FDA) or Federal Trade Commission (FTC) enforcement action commenced against my business, including any warning letters or other related correspondence within ten days of receipt. 5. ⟪Any time Shopify requests, I will provide documentation that confirms that my Shopify store, business, and cannabis products are in compliance with laws, regulations, and any of the requirements outlined here.⟫ ## Compliance requirements for hemp and hemp-derived products ### I confirm that for all hemp and hemp-derived products listed or sold on my Shopify store: 1. Those products don't contain more than 0.3% tetrahydrocannabinol (THC) concentration on a dry weight basis or such lower percentage as required by applicable state and local law. 2. Those products have been sourced, processed, tested, labeled and marketed in compliance with all applicable …
