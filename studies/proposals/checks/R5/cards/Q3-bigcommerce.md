# Cards: Q3 on bigcommerce

11 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 10:** - On WooCommerce, "Coming soon mode controls who can visit your site while you prepare it for launch", and the shipped install code sets `woocommerce_coming_soon` to yes. It matches Shopify's private mode on role, a store setting that keeps buyers out until launch (help pages, stated; WooCommerce's also shipped code); BigCommerce's storefront status, with `prelaunch_message` and `prelaunch_password`, overlaps in part (API reference, stated). Q3-WC-K1235; Q3-WC-K1236; Q3-SH-027; Q3-BC-013
- **section 1, line 21:** - All five verify the person and the business before payments, a match on role (help pages, stated): Shopify and its banking partners "collect and verify information about you and your business"; WooPayments verifies business details with Stripe; Salla asks for an ID or iqama matching Absher, the entity's document, and a stamped IBAN certificate in a matching name; Zid's gateway approves the account on requirements set by business entity; and BigCommerce Payments shows KYC status among its Actions tasks. Q3-SH-012; Q3-WC-012; Q3-SA-013; Q3-ZD-P0118; Q3-BC-P0072
- **section 1, line 24:** - Plans gate payments on three platforms, a match on role across kinds. Salla's help page (stated) puts electronic payment methods only in paid plans, and on store merchant (Basic, observed 8 October 2026) mada, credit card, Apple Pay and STC Pay were each `blocked_by` `requires_paid_plan`. BigCommerce's pages (stated) disagree on which plans qualify, Core, Growth or Scale (read 13 October 2026) or self-serve and retail plans (read 12 October 2026); the proposal rests only on a plan being needed. On Shopify store ts15uk-ug, observed 7 October 2026 in its trial, the Orders page said "To get orders and accept payments from customers, you need to select a plan." Q3-SA-P0068; Q3-SA-074; Q3-BC-P0068; Q3-BC-P0029; Q3-SH-101
- **section 1, line 25:** - Other parties add their own requirements, a match on role. On help pages (stated): American Express's address and name rules on a Shopify Payments account; for Tabby in Salla's UAE stores, a verified store, a Tabby merchant account with its keys, and an eligible plan; and each BigCommerce provider's own application and underwriting. On store ibx5bt-xy, the saved markup of the Shop Pay Installments terms step, observed 30 September 2026, says "Affirm reserves the right to deny you access to the Affirm Services" and asks for information identifying the seller and its beneficial owners, as its accessibility tree did. Q3-SH-057; Q3-SA-069; Q3-BC-P0048; Q3-SH-110
- **section 1, line 34:** - Payment providers and card networks set lists of what may not be sold, a match on role. On Shopify, "Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers" (its terms, official page). WooPayments cites "restrictions put in place by card networks, our payment processors, and their financial service providers", and BigCommerce points to Stripe's list (help pages, stated). Zid Pay's terms accept some digital products on the service provider's assessment. Q3-SH-P0045; Q3-WC-K0416; Q3-BC-021; Q3-ZD-K0070
- **section 1, line 41:** - BigCommerce leaves legality to the seller: Commerce "disclaims any responsibility for evaluating or confirming the legality of your products or services". Q3-BC-K0460
- **section 1, line 52:** - For WooPayments the relevant country is "the one where your business is registered — not the one in which you personally live". BigCommerce generally deems the entity or person who creates the Account, Store or website the owner. Q3-WC-K0402; Q3-BC-004
- **section 1, line 60:** - Payment partners approve, a match on role (BigCommerce's pricing page, official; the others help pages, stated): Zid's requirements go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and its Nafath request is in the service provider's name; a PayPal Braintree application on BigCommerce doesn't guarantee approval; WooPayments verifies with Stripe; and Shopify's banking partners require a real person on every account. Q3-ZD-P0118; Q3-ZD-P0047; Q3-BC-P0065; Q3-WC-012; Q3-SH-020
- **section 1, line 67:** - And again later. Shopify re-verifies periodically, and re-checks bank ownership when a payout account is added or replaced or business details change. Salla may ask for documents at any time, and Zid Pay's seller must report changes within a week. On BigCommerce, Stripe flags accounts for verification after a processing threshold. Q3-SH-066; Q3-SH-061; Q3-SA-051; Q3-ZD-078; Q3-BC-020
- **section 1, line 76:** - Each records the state, a match on role across kinds: Shopify's ShopifyPaymentsAccount has a field for whether setup is completed (developer documentation, stated); Salla's payments answer carries `blocks_payment_activation` and each method's `blocked_by` (observed, store merchant, 8 October 2026); WooCommerce's shipped code gives an onboarding step a blocked status; and BigCommerce shows tasks and fund holds in its Actions section (stated). On Shopify store ibx5bt-xy, the saved markup of the Subscribe to Plus step, observed 30 September 2026, says "Shopify Payments is not available on your store.", as its accessibility tree did. Q3-SH-086; Q3-SA-073; Q3-SA-074; Q3-WC-041; Q3-BC-P0072; Q3-SH-108
- **section 1, line 77:** - Each tells the seller what is missing, as Shopify's alert takes the seller to the upload page, WooCommerce's notices appear on "Payments > Overview", and BigCommerce's Actions section lists the tasks. Q3-SH-017; Q3-WC-051; Q3-BC-P0072
- **section 2, line 81:** - **Seller** (proposed): the person who opens the account and contracts with Sharrwah, and the first subject of requirements, including the identity checks only that person can complete. It takes Shopify's Store Owner as the contracting party and BigCommerce's creator as the owner, and puts the owner-only checks on it, as Shopify's Proof of Liveness and Zid's Nafath do. Why: rule 3, since who carries a requirement is the data model. Q3-SH-K1237; Q3-BC-004; Q3-SH-043; Q3-ZD-P0117
- **section 2, line 92:** - **Re-verification** (proposed): a met requirement is checked again when business details or the payout account change, at intervals, on request, or after a threshold; a duty to report changes within a set time is a per-place setting. While an update is reviewed, the met state holds and the store keeps taking orders and payments, as on Salla. Q3-SH-061; Q3-SH-066; Q3-SA-051; Q3-BC-020; Q3-ZD-078; Q3-SA-006
- **section 2, line 93:** - Not taken: a seller's declaration in place of any review, BigCommerce's way with products' legality. A declaration stays one requirement kind, used where a set calls for it. Q3-BC-K0460; Q3-SA-057
- **section 2, line 98:** - **Store launch state** (proposed): the seller's own setting that keeps buyers out before launch, showing a page and optionally a password the seller gives to visitors; new stores start with it on. Launching is a capability whose requirement set may be empty. It takes the state from Shopify's private mode, WooCommerce's Coming soon mode with `woocommerce_coming_soon` on at install, and BigCommerce's `prelaunch_password`. What launching needs differs (Shopify a plan, an address and a payment method; Salla verification; Zid nothing found), so it is set per place. Why: rule 1. Q3-SH-027; Q3-SH-109; Q3-WC-K1236; Q3-BC-013; Q3-SH-028; Q3-SA-026; Q3-ZD-N03
- **section 2, line 101:** - **Seller action list** (proposed): one list of each blocked capability, the requirements it waits on, any deadline and the next step, read from the capability status, like BigCommerce's Actions section and Shopify's alerts. Left to the build. Q3-BC-P0072; Q3-SH-017; Q3-WC-051
- **section 3, line 108:** - Payment providers, each with its own requirement set and approval: American Express on Shopify, Tabby on Salla, Tap on Zid, and the providers on BigCommerce. Q3-SH-057; Q3-SA-069; Q3-ZD-K0093; Q3-BC-P0048
- **section 3, line 116:** - Per plan: payment methods and product types on Salla, and BigCommerce Payments. Q3-SA-P0068; Q3-SA-029; Q3-BC-P0068
- **section 3, line 124:** - The seller: the launch state, and which providers to apply to. Q3-WC-K1235; Q3-BC-P0048
- **section 3, line 126:** - A provider: its own requirements and its approval. Q3-ZD-P0118; Q3-BC-P0065; Q3-SH-110
- **section 5, line 150:** - Which lists a seller is checked against: the platforms name their own (US, Canadian and EU lists on Shopify Payments; US lists on BigCommerce), and Yemen's evidence shows Ansarallah designated at the United States' area. Keep open: the lists as a setting of the requirement, by place and by the company's jurisdiction. Settled by the company decision on where it is based (section 7). Q3-SH-K2268; Q3-BC-K0430; YA-27 (FTO and SDGT @ the United States' area, as of 2025-03-05)
- **section 7, line 171:** - Which countries and parties Sharrwah won't serve, under whose sanctions lists, which turns on where the company is based. Q3-SH-K2268; Q3-BC-K0430; Q3-ZD-P0112
- **section 7, line 172:** - Whether Sharrwah reviews products against licences or takes the seller's declaration, and who answers when a product breaks a law. Q3-BC-K0460; Q3-SA-057; Q3-SH-053
- **section 7, line 173:** - Whether plans gate capabilities such as payment methods, product types and channels. Q3-SA-P0068; Q3-SA-029; Q3-BC-P0068

## The cards

### Q3-BC-013

**Cited at:** section 1, line 10; section 2, line 98

**Record** (`studies/proposals/records/Q3/bigcommerce/statements.tsv`):
- stmt_id: Q3-BC-013
- bears_on: 2
- identifier: StorefrontStatus: down_for_maintenance_message; prelaunch_message; prelaunch_password
- statement: - `down_for_maintenance_message` (string, optional) - `prelaunch_message` (string, optional) - `prelaunch_password` (string, optional) — A read-only value representing the auto-generated storefront password.
- cite_ids: Q3-BC-C014
- from: live
- note: GET https://api.bigcommerce.com/stores/{store_hash}/v3/settings/storefront/status

**Citation Q3-BC-C014:** `https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/settings/storefront-status/get-settings-storefront-status.md` | Types: StorefrontStatus | 2026-10-19 | kind: stated | quote check: found
- quote: `prelaunch_password` (string, optional) — A read-only value representing the auto-generated storefront password.
- title: Get Storefront Status
- the page opens: > This page is for Developer. > For clean Markdown of any page, append.md to the page URL. > For a complete documentation index, see https://docs.bigcommerce.com/llms.txt. > For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://docs.bigcommerce.com/_mcp/server. GET https://api.bigcommerce.com/stores/{store_hash}/v3/settings/storefront/status Returns storefront status-related settings. - Channel ID can be used as a query parameter for getting channel-specific…
- headings: Get Storefront Status > Types > StorefrontStatus
- in context: …eloper.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the response body. ## Response ### 200 OK, null indicates that a particular field has not been overridden on a channel level when channel level settings are requested - `data` (StorefrontStatus, optional) - `meta` (MetaOpen, optional) - Response metadata. ## Types ### StorefrontStatus - `down_for_maintenance_message` (string, optional) - `prelaunch_message` (string, optional) - ⟪`prelaunch_password` (string, optional) - A read-only value representing the auto-generated storefront password.⟫ ### MetaOpen Response metadata. ## Examples **Response** ```json { "data": { "down_for_maintenance_message": "Down for maintenance", "prelaunch_message": "Prelaunch", "prelaunch_password": "mezt1f77gd" }, "meta": {} } ``` **SDK Code** ```python example-1 import requests url = "https://api.bigcommerce.com/stores/store_hash/v3/settings/storefront/status" headers = { "Accept": "application/json", "X-Auth-Token": "<apiKey>" } response = requests.get…

### Q3-BC-P0072

**Cited at:** section 1, line 21; section 1, line 76; section 1, line 77; section 2, line 101

**Record** (`studies/proposals/records/Q3/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-071
- bullet: c
- placement: where
- identifier: Settings: Actions: fund holds
- statement: The Actions section allows you to see real-time alerts for your BigCommerce Payments account. Tasks, such as completing your profile, linking a bank account, Know Your Customer (KYC) status, and fund holds will be displayed here.
- cite_ids: S01-BC-C101
- from: new

**Citation S01-BC-C101:** `sharrwah-knowledge-map@7f7fdb3999568148dd5edb59912d3c47b3cd1b69:evidence/product-class/runs/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/001-support.bigcommerce.com/text.txt` | line 107: Settings, Actions | 2026-10-13 | kind: stated | quote check: found
- quote: The Actions section allows you to see real-time alerts for your BigCommerce Payments account. Tasks, such as completing your profile, linking a bank account, Know Your Customer (KYC) status, and fund holds will be displayed here.
- in context: … and link a new BigCommerce Payments account. Add info on your own - Select to create new PayPal Business and BigCommerce Payments accounts and link them together. Settings Actions Account Cards Digital wallets Buy Now, Pay Later Local payment methods Transaction settings Post-purchase & operations Once you have connected your PayPal Business account to a BigCommerce Payments account, you can customize your customer's payment experience. ACTIONS ⟪The Actions section allows you to see real-time alerts for your BigCommerce Payments account. Tasks, such as completing your profile, linking a bank account, Know Your Customer (KYC) status, and fund holds will be displayed here.⟫ Just above the Actions area is a link to access the Balance dashboard in the BigCommerce control panel, as well links to your account's portal pages on PayPal's website where you can manage payment disputes, view insights, and view reports. For more information about disputes and PayPal's Resolution Center, PayPal's merchant guide on dispute transactions. ACCOUNT Live account - When connected, your live account email address and Merchant ID are …

### Q3-BC-P0068

**Cited at:** section 1, line 24; section 3, line 116; section 7, line 173

**The same record as Q1-BC-P0068,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Your store must be on a Core, Growth, or Scale plan. Select Performance plan stores may be eligible to enable BigCommerce Payments. Check your store's control panel for availability. Your store’s checkout type must be Optimized One-Page Checkout or Custom Checkout. Your store must be located in the United Kingdom or the United States. Your new or existing PayPal Business account must be UK or US-based.
- scope: stores on a Core, Growth, or Scale plan (select Performance plan stores), located in the United Kingdom or the United States, with a UK or US-based PayPal Business account

### Q3-BC-P0029

**Cited at:** section 1, line 24

**Record** (`studies/proposals/records/Q3/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-028
- bullet: e
- placement: decides
- identifier: BigCommerce Payments: FAQs: Where is it available?
- statement: Initially, BigCommerce Payments is available only to US-based merchants with self-serve and retail plans.
- scope: US-based merchants with self-serve and retail plans
- conditions: S01-BC-039;S01-BC-041;S01-BC-043;S01-BC-044;S01-BC-051
- cite_ids: S01-BC-C030
- from: index:BC-C-025:BC-S-0143

**Citation S01-BC-C030:** `https://www.bigcommerce.com/payments/bigcommerce-payments/` | FAQs: Where is it available? | 2026-10-12 | kind: stated | quote check: found
- quote: Initially, BigCommerce Payments is available only to US-based merchants with self-serve and retail plans.
- title: BigCommerce Payments – a native payments experience.
- in context: …compliant? Yes. BigCommerce Payments is built with PayPal's infrastructure, which manages PCI compliance and risk controls at the platform level, so your team doesn't have to. Can I still use a third-party payments provider? BigCommerce supports multiple payment providers. Activating BigCommerce Payments does not prevent you from maintaining other gateway connections. Contact your account manager for configuration details. Where is it available? ⟪Initially, BigCommerce Payments is available only to US-based merchants with self-serve and retail plans.⟫ Additional regions and countries will be launching soon. See BigCommerce documentation or contact support to confirm whether your account qualifies. Where payments work Built with PayPal. Run inside BigCommerce. One platform for everything payments without the usual overhead slowing you down. Start your free trial PayPal is a trademark of PayPal, Inc., used under license. Availability and features may vary by region and merchant eligibility. See…

### Q3-BC-P0048

**Cited at:** section 1, line 25; section 3, line 108; section 3, line 124

**The same record as Q1-BC-P0048,** whose card is in `Q1-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Each provider has its own application process. 3. Apply and configure Apply with your chosen provider, complete underwriting, then add them in your BigCommerce dashboard under Store Setup, Payments.
- scope: 

### Q3-BC-021

**Cited at:** section 1, line 34

**Record** (`studies/proposals/records/Q3/bigcommerce/statements.tsv`):
- stmt_id: Q3-BC-021
- bears_on: 2
- identifier: Stripe OCS FAQ: What items are restricted for merchants to sell?
- statement: What items are restricted for merchants to sell? See Stripe's documentation for a list of prohibited and restricted businesses.
- scope: Stripe OCS
- cite_ids: Q3-BC-C023
- from: held

**Citation Q3-BC-C023:** `https://support.bigcommerce.com/s/article/Connecting-with-Stripe-OCS?language=en_US` | Common Questions: Account eligibility | 2026-10-13 | kind: stated | quote check: found
- quote: See Stripe's documentation for a list of prohibited and restricted businesses.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …IP KWD* MVR RON TRY ZMW BWP GMD KYD MWK RSD TTD *KWD is only supported for the United Arab Emirates. To enable this currency, your Stripe account country must be the United Arab Emirates. See Stripe's supported currencies article for more information. If you are managing transactions on your store with the Payments API, contact our support team to enable KWD as an available transactional currency. What items are restricted for merchants to sell? ⟪See Stripe's documentation for a list of prohibited and restricted businesses.⟫ Can I change the Credit Cards payment method display name? No. Payment methods are managed in the Stripe Dashboard, but their display names cannot be customized. TRANSACTIONS After I create an account, what is the waiting period before I can process transactions? There is no waiting period. However, Stripe does flag accounts for verification after a certain processing threshold. How long until a transaction's funds are transferred to my bank? St…

### Q3-BC-K0460

**Cited at:** section 1, line 41; section 2, line 93; section 7, line 172

**The same record as Q2-BC-K0460,** whose card is in `Q2-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Commerce disclaims any responsibility for evaluating or confirming the legality of your products or services. You are solely responsible for ensuring that your products comply with applicable laws.
- scope: 

### Q3-BC-004

**Cited at:** section 1, line 52; section 2, line 81

**Record** (`studies/proposals/records/Q3/bigcommerce/statements.tsv`):
- stmt_id: Q3-BC-004
- bears_on: 1
- identifier: Ownership & Disputes: Generally
- statement: Generally. The entity or person who creates the Commerce Account, Store, or website will generally be deemed the owner. Commerce may allow only the owner or the point of contact designated by the owner to make changes, cancellations, or designate a new point of contact.
- cite_ids: Q3-BC-C005
- from: held

**Citation Q3-BC-C005:** `https://www.commerce.com/terms/store-terms/` | Ownership & Disputes: Generally | 2025-07-31 | kind: official page | quote check: found
- quote: The entity or person who creates the Commerce Account, Store, or website will generally be deemed the owner.
- title: Store Terms | Commerce
- in context: … and your use of the Website or Services. Communications. You are solely responsible for all communications between you and Your Users. You represent, covenant, and warrant that all email communications between you and Your Users using the Services will be in compliance with your privacy policy and all Laws, including, without limitation, all Laws related to unsolicited emails, privacy, obscenity, and defamation. Ownership & Disputes. Generally. ⟪The entity or person who creates the Commerce Account, Store, or website will generally be deemed the owner.⟫ Commerce may allow only the owner or the point of contact designated by the owner to make changes, cancellations, or designate a new point of contact. Disclaimer. To the fullest extent permitted by applicable law, Commerce will have no obligation or liability whatsoever to you or any third party (i) to resolve any ownership dispute, or (ii) for any act taken to resolve any ownership dispute. Remedies. If a dispute arises between you and one or m…

### Q3-BC-P0065

**Cited at:** section 1, line 60; section 3, line 126

**Record** (`studies/proposals/records/Q3/bigcommerce/copied-pilot.tsv`):
- stmt_id: S01-BC-064
- bullet: e
- placement: decides
- identifier: PayPal Braintree account: approval
- statement: Application for a PayPal Braintree account does not guarantee approval.
- conditions: S01-BC-062
- cite_ids: S01-BC-C083
- from: new
- note: Phase A3.

**Citation S01-BC-C083:** `sharrwah-knowledge-map@7611d459e3e09c1503a27d4f02f57850e82e9ffb:evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/102-bigcommerce.com/text.txt` | line 354: footnote *** "To qualify for the PayPal Braintree rate", after step (4) | 2026-10-12 | kind: official page | quote check: found
- quote: Application for a PayPal Braintree account does not guarantee approval.
- in context: … We suggest adding echosign@echosign.com to your email whitelist to reduce the risk of it going to your spam folder. Follow the instructions in the email on how to sign and return the contract. (4) Your account will then be updated to reflect the new rate, and you will receive a notification email with the updated rate, which can take up to 10 business days. Your new rate will only apply to transactions after the date on your notification email. ⟪Application for a PayPal Braintree account does not guarantee approval.⟫ Periodically, PayPal Braintree reviews its customer accounts to make sure its services and rates fit your account activity. PayPal Braintree reserves the right to revise its fees at any time, subject to a thirty (30) day notice period to you prior to the new fees taking effect. The standard online rate for payments with American Express is and will continue to be 3.50% with no fixed fee after August 2, 2021. Product Features Services Enterprise …

### Q3-BC-020

**Cited at:** section 1, line 67; section 2, line 92

**Record** (`studies/proposals/records/Q3/bigcommerce/statements.tsv`):
- stmt_id: Q3-BC-020
- bears_on: 4
- identifier: Stripe OCS FAQ: waiting period before I can process transactions
- statement: After I create an account, what is the waiting period before I can process transactions? There is no waiting period. However, Stripe does flag accounts for verification after a certain processing threshold.
- scope: Stripe OCS
- cite_ids: Q3-BC-C022
- from: held

**Citation Q3-BC-C022:** `https://support.bigcommerce.com/s/article/Connecting-with-Stripe-OCS?language=en_US` | Common Questions: Transactions | 2026-10-13 | kind: stated | quote check: found
- quote: There is no waiting period. However, Stripe does flag accounts for verification after a certain processing threshold.
- title: BigCommerce Help Center
- the page opens: BigCommerce Help Center Loading ×Sorry to interrupt CSS Error Refresh…
- in context: …eam to enable KWD as an available transactional currency. What items are restricted for merchants to sell? See Stripe's documentation for a list of prohibited and restricted businesses. Can I change the Credit Cards payment method display name? No. Payment methods are managed in the Stripe Dashboard, but their display names cannot be customized. TRANSACTIONS After I create an account, what is the waiting period before I can process transactions? ⟪There is no waiting period. However, Stripe does flag accounts for verification after a certain processing threshold.⟫ How long until a transaction's funds are transferred to my bank? Stripe typically schedules your initial payout 7-14 days after the first successful payment. Your first payout might take longer, depending on your industry risk level and country of operation. Subsequent payouts are processed according to your account's payout schedule. See Stripe's Receive Payouts documentation for more information. Will my customers receive an additional email o…

### Q3-BC-K0430

**Cited at:** section 5, line 150; section 7, line 171

**The same record as Q2-BC-K0430,** whose card is in `Q2-bigcommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: are not, and will ensure that your Relevant Parties and customers are not, (a) nationals, residents, agents or representatives of Iran, Cuba, North Korea, Syria, the Crimea Region of Ukraine, or any other region subject to comprehensive U.S. sanctions
- scope: 
