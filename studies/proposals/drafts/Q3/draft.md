# Q3: What a seller must do or meet before doing particular things, a draft proposal

## 1. How the platforms handle it

### [1] [2]

**Registering**

- Shopify's terms ask for the seller's "full legal name, business address, phone number, a valid email address" to complete Account registration; Zid's ask for the name as it appears in official papers, an address, a mobile number and an email. Salla's usage agreement asks for a commercial registration or a freelance document, an Absher account, a Saudi bank account and a Saudi mobile number. Q3-SH-K1238; Q3-ZD-042; Q3-SA-P0075

**Opening the store to buyers**

- On Shopify, a store on its free trial is automatically in private mode, its pages inaccessible, and the seller launches it by turning off the Private mode setting. Before launch the seller must select a plan, add a store address, and set up a payment method with test mode deactivated. Q3-SH-027; Q3-SH-031; Q3-SH-028
- On WooCommerce, "Coming soon mode controls who can visit your site while you prepare it for launch", and the shipped code adds the option `woocommerce_coming_soon` as yes at install. It matches Shopify's private mode on role: a store setting that keeps buyers out until launch (both help pages, stated; WooCommerce's also shipped code). BigCommerce's storefront status, with `prelaunch_message` and `prelaunch_password`, overlaps in part (its API reference, stated). Q3-WC-K1235; Q3-WC-K1236; Q3-SH-027; Q3-BC-013
- Salla calls Store Verification (توثيق المتجر) "المحطة الأخيرة لتدشين متجرك". On the store named Store 1, on the Basic plan, observed 8 October 2026, the onboarding steps `kyc` and `launch` were pending and not optional. Q3-SA-026; Q3-SA-086
- Zid's onboarding ends with a preview and a test order before launch. A check or condition Zid applies before a store is opened to buyers was not in what was read. Q3-ZD-034; Q3-ZD-N03
- BigCommerce's free trial allows launching the store and taking payments once a payments partner is set up. Q3-BC-010

**Taking payments: where the business is**

- Each platform offers its own payment product by where the business or store is, a match on role. Shopify Payments needs "a business located in your Designated Country" (its terms, official page). On help pages (stated), Zid Pay is offered to merchants of Saudi Arabia and Kuwait, and WooPayments needs a business "based in one of our supported countries". BigCommerce's pages disagree: a help page read 13 October 2026 says the United Kingdom or the United States, a product page read 12 October 2026 the US only; the proposal rests on neither page's list. Q3-SH-K1536; Q3-ZD-P0113; Q3-WC-010; Q3-BC-P0068; Q3-BC-P0029
- Checked against a merchant selling in the Yemeni market: any country beyond the 40 on Shopify's list of supported countries is absent, and Yemen is not among the 40. For store fake-demo-sharrwah, whose business entity is in Yemen, observed 5 October 2026, the admin's ShopifyPaymentsData answer gave Shopify Payments "eligible":false. Zid Pay's Kuwait terms bar activities dealing with countries under international sanctions and name اليمن among them; the list in its Saudi terms does not. Q3-SH-A0002; Q3-SH-100; Q3-ZD-P0112; Q3-ZD-P0111

**Taking payments: who and what is verified**

- All five verify the person and the business before payments, a match on role (help pages, stated). Shopify and its banking partners "collect and verify information about you and your business". WooPayments verifies the business details with its partner Stripe. Salla's verification asks for an ID or iqama matching Absher, the entity's document, and a stamped IBAN certificate in a matching name. Zid gives the gateway requirements set by business entity, and the gateway approves the account. BigCommerce Payments shows KYC status among the tasks in its Actions section. Q3-SH-012; Q3-WC-012; Q3-SA-013; Q3-ZD-P0118; Q3-BC-P0072
- What is asked differs by entity type and by place. Zid: "تختلف المتطلبات والبيانات المطلوبة حسب نوع النشاط التجاري والدولة". Salla's table asks an individual for a freelance document (Saudi citizens only), an establishment or company for a commercial registration, and a charity for its registration certificate, each with its own kind of bank account. Shopify's Proof of Liveness check depends on the country. Q3-ZD-K0240; Q3-SA-014; Q3-SH-041
- Other steps come first. Zid needs one published product matching the activity before the request, and the store owner's Nafath check (not checked on WooCommerce; shown by Zid). Shopify needs two-step authentication. Shopify and WooCommerce need test mode off, the same term for the same thing. Salla's activation includes accepting سياسة البيع. Q3-ZD-P0116; Q3-ZD-P0117; Q3-SH-K1274; Q3-SH-028; Q3-WC-017; Q3-SA-K1532
- Plans gate payments on three platforms, a match on role. Salla's electronic payment methods come only with paid plans; on store merchant, on the Basic plan, observed 8 October 2026, mada, credit card, Apple Pay and STC Pay were each `blocked_by` `requires_paid_plan`. BigCommerce Payments needs a Core, Growth or Scale plan. On Shopify store ts15uk-ug, observed 7 October 2026 in its trial, the Orders page said "To get orders and accept payments from customers, you need to select a plan." Q3-SA-P0068; Q3-SA-074; Q3-BC-P0068; Q3-SH-101
- Other parties add their own requirements, a match on role. American Express sets address and name rules on a Shopify Payments account. Tabby in Salla's UAE stores needs a verified store, a Tabby merchant account with its keys, and an eligible plan. Tap on Zid asks for the ID registered with Tap, checked by Nafath. On BigCommerce each provider has its own application and underwriting. Q3-SH-057; Q3-SA-069; Q3-ZD-K0093; Q3-BC-P0048

**Receiving payouts**

- The payout bank account follows verification: Shopify's is connected after the account is verified, Salla's payouts go to the account given at verification, and Zid's account is chosen during activation. Q3-SH-009; Q3-SA-K1568; Q3-ZD-P0037
- Its holder must match the verified identity, a match on role. Shopify compares the bank account's name with the legal business name or the account representative's. Salla: "تأكد من أن اسم صاحب الحساب البنكي مطابق لبيانات التوثيق". Zid: "لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح". On both Salla and Zid an establishment needs a business account in its own name. Q3-SH-062; Q3-SA-K1563; Q3-ZD-K0037; Q3-SA-010; Q3-ZD-015
- New accounts wait: WooPayments sends the first payout after 7 days, and BigCommerce Payments holds initial payments for up to 21 days. Shopify's payouts might be held until two-step authentication is on. Q3-WC-P0038; Q3-BC-P0083; Q3-SH-001
- Salla requires verification to withdraw the store balance and to transfer the electronic payments balance; on store merchant (Basic, observed 8 October 2026), withdrawal was disabled for `store_documents_required`. Zid's wallet takes balance the seller adds and spends, and "لا يتاح لك سحب المبالغ حتى يتم إكمال عملية توثيق الحساب"; by its words it holds top-ups, not sales proceeds, so it is outside the money flow. Q3-SA-P0162; Q3-SA-077; Q3-ZD-P0063

**Selling particular products**

- Payment providers and card networks set lists of what may not be sold, a match on role. On Shopify, "Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment Processor's Financial Services Providers" (its terms, official page). WooPayments cites "restrictions put in place by card networks, our payment processors, and their financial service providers", and BigCommerce points to Stripe's list (help pages, stated). Zid Pay's terms accept some digital products on the service provider's assessment. Q3-SH-P0045; Q3-WC-K0416; Q3-BC-021; Q3-ZD-K0070
- The platforms keep their own lists too: Salla's سياسة البيع (gambling, harm, piracy, sexual content, fortune-telling, pre-selling, sales without proof, resold shipping labels) and Zid Pay's الأنشطة المحظورة. Q3-SA-054; Q3-SA-K1532; Q3-ZD-P0111
- A provider's exclusion closes only that provider, a match on role: Shopify Payments doesn't support hemp, CBD or THC, which compatible third-party providers may process, and WooPayments' CBD sellers must use Square or Viva Wallet. Q3-SH-095; Q3-WC-K0417
- Salla's agreement and Zid's terms carry the same clause for products that need an official licence, "بالإفصاح عن الترخيص وكافة بياناته": the same term, in both platforms' terms (official pages). Neither platform's full list of such products was in what was read; Zid says the need is decided after the data is reviewed, with books and the Ministry of Media as its example. Q3-SA-047; Q3-ZD-K0247; Q3-SA-N02; Q3-ZD-N04; Q3-ZD-023
- Shopify lists licences and age checks for alcohol, and confirmations for hemp, in the United States; when it checks them, beyond asking for documents, was not in what was read. Q3-SH-051; Q3-SH-053; Q3-SH-N02
- The registered activity must match the products, a match on role: Salla's KYC schema, observed 8 October 2026, says "Commercial registration activity must match the store activity", and Zid's help page "أن يكون نشاط الوثيقة مطابق لنشاط منتجات المتجر". Q3-SA-058; Q3-ZD-003
- Salla's Basic plan allows only ready-made products (منتج جاهز); digital products, food, made-to-order products, bundles and bookings need Plus or Pro. Q3-SA-029
- BigCommerce leaves legality to the seller: Commerce "disclaims any responsibility for evaluating or confirming the legality of your products or services". Q3-BC-K0460

**Things gated by other things**

- A program or channel often needs another capability active, a match on role. Shop needs Shopify Payments activated; Mahally needs a paid plan and a verified store (not checked on WooCommerce; shown by Salla); Jahez needs Mazeed activated; and Zid Financing needs Zid Pay activated and approved. Q3-SH-077; Q3-SA-061; Q3-ZD-P0144; Q3-ZD-P0132
- The business's country is hard to change: WooPayments' country "cannot be changed later", and Zid asks a merchant moving the store to another country to bring the wallet balance to zero first. Q3-WC-011; Q3-ZD-K0230

### [3]

- The platforms put requirements on two subjects, the person and the business. Shopify's person signing up is the contracting party, the "Store Owner". Every Shopify Payments account names one individual as account representative, never a company, and lists owners of 25% or more. Q3-SH-K1237; Q3-SH-020; Q3-SH-023
- Salla requires every verification document to be in the store owner's own name. Its KYC schema for a demo store, observed 8 October 2026, offers the entity types `single`, `company`, `institution`, `charity` and `government`; Zid's business types are فرد، مؤسسة، شركة، جمعية خيرية. They match on role in four of five; Salla adds government. Q3-SA-019; Q3-SA-056; Q3-ZD-K0239
- For WooPayments the relevant country is "the one where your business is registered — not the one in which you personally live". BigCommerce deems the entity or person who creates the Account, Store or website the owner. Q3-WC-K0402; Q3-BC-004
- Some checks fall on the owner in person: on Shopify only the account owner can complete a Proof of Liveness check; on Zid the store owner passes Nafath (not checked on WooCommerce; shown by Zid); on Salla an ID suspended for violations can register no new store. Q3-SH-043; Q3-ZD-P0117; Q3-SA-059

### [4]

**Who sets it**

- Salla calls its verification an "إجراء تشغيلي داخلي لتفعيل بوابات الدفع والحساب البنكي", apart from the government's Business Platform licence. Q3-SA-037
- Payment partners approve, a match on role. Zid's requirements go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and its Nafath request is made in the service provider's name. On BigCommerce, applying for a PayPal Braintree account does not guarantee approval. WooPayments verifies with Stripe, and Shopify's banking partners require a real person on every account. Q3-ZD-P0118; Q3-ZD-P0047; Q3-BC-P0065; Q3-WC-012; Q3-SH-020
- Law, regulators and networks set others, as the platforms report them. Shopify's European and UK verification follows the FCA and the Central Bank of Ireland, and its prohibited categories may come from law, network rules, Shopify or processors' providers. Zid's licences come from the relevant authorities, and Salla's e-commerce obligations from the e-commerce law and the Ministry of Commerce's guide. Q3-SH-065; Q3-SH-P0045; Q3-ZD-023; Q3-SA-033

**When it is checked**

- When the seller applies, with review times that differ: Salla 24 to 48 hours; Shopify's documents up to 24 hours; WooPayments typically a couple of days; BigCommerce's payment methods usually within one business day of a completed profile. Zid's team reviews and notifies by email. Q3-SA-003; Q3-SH-014; Q3-WC-004; Q3-BC-018; Q3-ZD-P0038
- Attempts are limited: Absher three a day on Salla, Nafath three a day on Zid. Q3-SA-008; Q3-ZD-K0262
- And again later. Shopify re-verifies periodically, and re-checks bank ownership when a payout account is added or replaced or business details change. Salla may ask for documents at any time, and Zid Pay's seller must report changes within a week. Stripe flags accounts for verification after a processing threshold. Q3-SH-066; Q3-SH-061; Q3-SA-051; Q3-ZD-078; Q3-BC-020

**What the seller can and can't do while it isn't met**

- The store keeps working while a payment requirement is pending. On Shopify, the store stays usable while payouts are on hold. Salla lets the seller prepare the store and products before verification, a rejection leaves settings and products intact, and a verified store updating its data keeps taking orders and payments. Q3-SH-P0085; Q3-SA-016; Q3-SA-023; Q3-SA-006
- Effects can be narrow: a detail failing American Express's rules stops American Express at checkout while other card brands continue, and a revoked P24 makes only P24 orders fail. Q3-SH-058; Q3-WC-034
- Deadlines escalate. On Shopify in Europe and the UK, for accounts created in or after June 2026, payouts pause at once, charges after 30 days, and payments are refunded 90 days after the first order, while payments through other providers are unaffected. Such a timeline outside Europe and the UK was not in what was read. Q3-SH-072; Q3-SH-073; Q3-SH-N01
- Zid Pay gives 14 days to correct wrong data, then disables the account and returns all amounts to end customers. Salla suspends payments and settlement "بعد انتهاء المهلة", a period whose length was not in what was read. WooPayments may restrict payments or payouts once a deadline for missing information passes. Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01; Q3-WC-P0055
- Returning buyers' money matches on role across kinds: Zid Pay's terms (official page), Shopify's European and UK help page (stated), and Salla's agreement, which allows returning pending electronic payments to consumers for a breach of its tenth article (official page). Q3-ZD-P0012; Q3-SH-072; Q3-SA-P0083
- Each records the state, a match on role across kinds. Shopify's ShopifyPaymentsAccount has a field for whether setup is completed (developer documentation, stated). Salla's payments answer carries `blocks_payment_activation` and each method's `blocked_by` (observed, store merchant, 8 October 2026). WooCommerce's shipped code gives an onboarding step a blocked status. BigCommerce shows tasks and fund holds in its Actions section (stated). Q3-SH-086; Q3-SA-073; Q3-SA-074; Q3-WC-041; Q3-BC-P0072
- Each tells the seller what is missing: Shopify's alert that takes the seller to the upload page, WooCommerce's notices on "Payments > Overview", and BigCommerce's list of PayPal Pay Later requirements still to meet. Q3-SH-017; Q3-WC-051; Q3-BC-023

## 2. Proposed: names, structure and behaviour

- **Seller** (proposed): the person who opens the account and contracts with Sharrwah, and the first subject of requirements: registration details, and the identity checks only that person can complete. It takes Shopify's Store Owner as the contracting party and BigCommerce's creator as the owner, and puts the owner-only checks on it, as Shopify's Proof of Liveness and Zid's Nafath do. Why: rule 3, since who carries a requirement is the data model. Q3-SH-K1237; Q3-BC-004; Q3-SH-043; Q3-ZD-P0117
- **Business** (proposed): the legal entity behind one or more stores, with its **entity type** and its **registration place**, the place whose government documents it uses. These two choose each requirement set. The registration place comes from Salla's question for the country whose government documents the store uses and WooPayments' country of registration; the entity types from Salla and Zid, whose requirements differ by entity type and country. Why: rule 1, since the place selects configuration rather than code, and rule 3. Q3-SA-085; Q3-WC-K0402; Q3-SA-056; Q3-ZD-K0239; Q3-ZD-K0240
  - Not taken: keying requirements to where the store or business is located, as Shopify Payments and BigCommerce Payments do. Documents come from the place of registration, as Salla and WooPayments say; the store's own places stay with Q1. Q3-SH-K1536; Q3-BC-P0068
  - Changing the registration place is a fresh verification with its own requirement set, not an edit, since WooPayments can't change it and Zid asks for the wallet at zero first. Why: rule 3. Q3-WC-011; Q3-ZD-K0230
  - **Business person** (proposed): each individual the business must name, with a role, such as Shopify's one individual representative and its owners of 25% or more. The roles and the ownership threshold are set per registration place, as Shopify's "For most regions" shows. Why: rules 1 and 3. Q3-SH-020; Q3-SH-023
- **Capability** (proposed): a thing a seller may do that a requirement set can gate: open the store to buyers, take payments through one method or provider, receive payouts, withdraw a balance, sell a product type or category, join a sales channel or program, or use a financing or tax service. One capability can require another, as Shop requires Shopify Payments, Mahally a verified store, Jahez Mazeed, and Zid Financing Zid Pay. Why: rule 2, since each gate sits behind its own capability, so a change in one provider's requirements changes only that capability. Q3-SH-077; Q3-SA-061; Q3-ZD-P0144; Q3-ZD-P0132
  - **Capability status** (proposed): for each store and capability, available, blocked or restricted, with machine-readable reasons naming the unmet requirements. It takes Salla's `blocks_payment_activation`, `blocked_by` and `withdraw_disabled_reason`, WooCommerce's blocked onboarding step, and Shopify's field for setup completed. Why: rule 3, the data model. Q3-SA-073; Q3-SA-074; Q3-SA-077; Q3-WC-041; Q3-SH-086
- **Requirement** (proposed): one condition, with its kind, its subject, its setter, how long it stays valid, and how it is checked. The kinds come from the platforms: information, a document, an identity check, a plan, an agreement accepted, a store setting such as an address or test mode off, a product state such as a published product matching the activity, account security such as two-step authentication, account history such as Shop's chargeback rate under 1%, and another capability being active. Validity comes from rules such as Zid's commercial register valid two months from activation. The subject is the seller, a business person, the business, the store, a product or the payout account. Why: rule 2, since kinds will grow and each requirement is data. Q3-SH-028; Q3-ZD-P0116; Q3-SH-K1274; Q3-SH-078; Q3-ZD-013
- **Requirement set** (proposed): the requirements one capability needs, for one registration place, entity type, plan and provider; configured, versioned and shown to the seller. It combines Salla's per-country verification (in the UAE, a trade licence, Emirates ID and passport per owner, and an IBAN certificate; in Saudi Arabia, an Absher-matched ID and a citizens-only freelance document), Zid's per-entity and per-country requirements, and Shopify's per-country Proof of Liveness. Why: rule 1. Q3-SA-072; Q3-SA-014; Q3-ZD-K0240; Q3-SH-041
  - The lists change: Shopify's Shop requirements are "subject to change without notice", its European and UK verification is being updated throughout 2026, and Zid's prohibited activities "يمكن تحديثها في أي وقت، مع إشعار التاجر". So a set is versioned data, and a met requirement keeps the version it was met under. Why: rule 2. Q3-SH-083; Q3-SH-065; Q3-ZD-P0111
- **Submission** and **Review** (proposed): the seller gives information and documents once, inside Sharrwah, and a review decides: pending, approved, rejected with reasons, or more needed. Details already given are drawn in, as Zid draws activation details from the store's settings, and the seller declares them true, as Salla's KYC schema requires. Each review has a checker, which is Sharrwah's team, a provider or an identity service, with its own attempt limits and timing. Documents come only through Sharrwah, as Shopify accepts them only through its admin. Why: rule 2 for the checker, rule 3 for the data. Q3-ZD-054; Q3-SA-057; Q3-ZD-P0038; Q3-ZD-P0118; Q3-SA-008; Q3-SH-015
  - **Re-verification** (proposed): a met requirement is checked again when business details or the payout account change, at intervals, on request, or after a threshold; a duty to report changes within a set time is a per-place setting. While an update is reviewed, the met state holds and the store keeps taking orders and payments, as on Salla. Q3-SH-061; Q3-SH-066; Q3-SA-051; Q3-BC-020; Q3-ZD-078; Q3-SA-006
  - Not taken: a seller's declaration in place of any review, BigCommerce's way with products' legality. A declaration stays one requirement kind, used where a set calls for it. Q3-BC-K0460; Q3-SA-057
- **Restriction** (proposed): what an unmet requirement does, scoped to the capability it gates: keep the store from buyers, block a payment method or checkout, hold payouts, block withdrawals, or suspend the store. Each records its reason and the requirements it waits on, and lifts when they are met, as Shopify's pauses lift "automatically after you complete verification". It follows the narrow effects the platforms show: American Express alone stopping, other providers unaffected, the store usable while payouts are held, products kept after a rejection. Why: rule 2. Q3-SH-058; Q3-SH-073; Q3-SH-P0085; Q3-SA-023; Q3-SH-070
  - **Escalation** (proposed): a restriction can step up on a schedule (hold payouts, then pause charges, then return payments to buyers), with steps and days set per registration place, as Shopify's European and UK timeline and Zid Pay's 14 days show. Why: rule 1. Q3-SH-072; Q3-ZD-P0012
  - Holding payouts, blocking withdrawals and returning payments to buyers act on sellers' money. The design provides for them, and for gating payouts and a balance; any arrangement in which sellers' money is held through Sharrwah, by Sharrwah itself or by a payment company in an account opened through Sharrwah, goes live only by the founder's decision. Q3-SA-077; Q3-ZD-P0012; Q3-SH-P0085
  - Not taken: one store-wide check blocking all selling until met, as Salla's Basic stores show with verification "متطلب أساسي للبدء في عملية البيع". It ties every capability to one check; the design can still express it as the requirement set for opening the store. Q3-SA-001
- **Store launch state** (proposed): the seller's own setting that keeps buyers out before launch, showing a page and optionally a password; new stores start with it on. Launching is a capability with its own requirement set per place, which may be empty. It takes the state from Shopify's private mode, WooCommerce's Coming soon mode with `woocommerce_coming_soon` on at install, and BigCommerce's `prelaunch_password`. The platforms differ on what launching needs (Shopify a plan, an address and a payment method; Salla verification; Zid nothing found), so that part is per place. Why: rule 1. Q3-SH-027; Q3-WC-K1236; Q3-BC-013; Q3-SH-028; Q3-SA-026; Q3-ZD-N03
- **Product rule** (proposed): a rule on what may be sold, with its setter and its reach. It may bar a product for all of Sharrwah; bar it for one provider, blocking only that provider's capability; require a licence disclosed on the store with its details; require the registered activity to match the product; or require a plan for a product type. It takes Salla's selling policy, Shopify Payments' hemp rule and WooPayments' CBD rule, Salla's and Zid's licence clause, their activity match, and Salla's plan-limited product types. Why: rule 2, since each setter's list changes on its own. Q3-SA-054; Q3-SH-095; Q3-WC-K0417; Q3-SA-047; Q3-ZD-K0247; Q3-SA-058; Q3-ZD-003; Q3-SA-029
- **Agreement acceptance** (proposed): each agreement a capability needs (Sharrwah's terms, a selling policy, a provider's terms) is recorded with its version and the time accepted, and declining a new version ends that capability. It takes Salla's selling policy accepted on activating e-payments, WooPayments' terms accepted by "Finish setup", and WooPayments ending when the seller opts out of an updated agreement. Why: rule 3, partner contracts. Q3-SA-K1532; Q3-WC-K0369; Q3-WC-K0714
- **Seller action list** (proposed): one list of each blocked capability, the requirements it waits on, any deadline and the next step, read from the capability status, like BigCommerce's Actions section and Shopify's alerts. Left to the build. Q3-BC-P0072; Q3-SH-017; Q3-WC-051

## 3. What can plug in, what is set per what, and who sets it

**What can plug in**

- Checkers: an identity service, such as Nafath on Zid and Absher on Salla, or a provider's own onboarding, such as Stripe's for WooPayments and the gateway that approves a Zid Pay account. Q3-ZD-P0117; Q3-SA-013; Q3-WC-012; Q3-ZD-P0118
- Payment providers, each with its own requirement set and approval: American Express on Shopify, Tabby on Salla, Tap on Zid, and the providers on BigCommerce. Q3-SH-057; Q3-SA-069; Q3-ZD-K0093; Q3-BC-P0048
- Sales channels and programs, each with its own requirement set: Shop, Mahally and Jahez. Q3-SH-077; Q3-SA-061; Q3-ZD-P0144
- Government services a requirement can call on: the Business Platform (منصة الأعمال), ZATCA's link for tax invoices, and SPL's national address. Q3-SA-037; Q3-SA-071; Q3-ZD-039
- Financing providers that decide their own eligibility, such as Shopify Credit's Issuing Bank. Q3-SH-K2933

**What is set per what**

- Per registration place: the documents and checks, as on Salla by country, on Zid by country, and for Shopify's Proof of Liveness. Q3-SA-072; Q3-ZD-K0240; Q3-SH-041
- Per entity type: the documents and the kind of payout account, as in Salla's table and on Zid. Q3-SA-014; Q3-SA-010; Q3-ZD-015
- Per plan: payment methods and product types on Salla, and BigCommerce Payments. Q3-SA-P0068; Q3-SA-029; Q3-BC-P0068
- Per provider or payment method: American Express's rules, and Tabby's on Salla. Q3-SH-057; Q3-SA-069
- Per product category: a provider's exclusions, such as hemp and CBD, and Zid Pay's assessment of digital products. Q3-SH-095; Q3-WC-K0417; Q3-ZD-K0070
- Per store: the launch state. Q3-SH-031; Q3-WC-K1235
- Per person: the identity checks only the owner completes. Q3-SH-043; Q3-ZD-P0117

**Who sets it**

- The seller: the launch state, and which providers and channels to apply to. Q3-SH-031; Q3-BC-P0048
- Sharrwah: its own requirement sets, such as its review, its plans and its selling policy, as Salla's own verification and selling policy show. Q3-SA-037; Q3-SA-054
- A provider: its own requirements and its approval. Q3-ZD-P0118; Q3-BC-P0065
- A card network: American Express on Shopify, and the networks behind WooPayments' restricted businesses. Q3-SH-057; Q3-WC-K0416
- Authorities and the law, as the platforms report them: licences on Zid, and the e-commerce law's obligations on Salla. These show what the platforms require of their sellers, not what any law requires of Sharrwah. Q3-ZD-023; Q3-SA-033

## 4. Parts, in the order they can be built

1. Subjects: **Seller**, **Business** with its **entity type** and **registration place**, and **Business person**. Needs nothing before it.
2. The requirement catalogue: **Requirement** and **Requirement set**, as versioned configuration. Needs part 1.
3. The gate: **Capability**, **Capability status**, and the **Restriction** types that hold no money. Needs part 2.
4. **Store launch state**, the first capability, which needs no checker. Needs part 3.
5. **Submission** and **Review**, with document storage and **Re-verification**. Needs parts 1 and 2.
6. The checkers a **Review** calls: identity services and providers' onboarding. Needs part 5, and each waits on a company decision in section 7.
7. **Agreement acceptance**. Needs part 1.
8. **Seller action list**. Needs parts 3 and 5.
9. **Product rule**. Needs parts 2 and 3, and the product catalogue (area A-04).
10. Gates on payments, payouts and balances, with the money **Restriction** types and **Escalation**. Needs parts 3, 5 and 6, and Q5's payment design. Any arrangement in which sellers' money is held through Sharrwah goes live only by the founder's decision.

## 5. What the design must keep open

- Who checks a seller before payments in a place: Sharrwah's own review, as on Salla; a gateway's approval, as on Zid; a partner's check, as Stripe's for WooPayments and Shopify's banking partners'; or more than one. It is costly to change, being legal structure and partner contracts. Keep open: the checker as a plug-in and the setter on every requirement, with no single path built in. Settled by the company decisions on providers and on Sharrwah's own position (section 7). Q3-SA-037; Q3-ZD-P0118; Q3-WC-012; Q3-SH-012
- What unmet requirements do to money: holding payouts, blocking withdrawals, returning payments to buyers, and the days between, as Shopify, Zid and Salla show them; Salla's period was not in what was read. It is a money flow. Keep open: a restriction type for each, with schedules per place, all off until decided. Settled by the founder's decision under the guard, Q5's proposal and providers' terms. Q3-SH-072; Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01
- Which place selects a requirement set, and what moving it costs: the country of the documents (Salla), of registration (WooPayments), or of the business's or store's location (Shopify, BigCommerce). Keep open: the registration place kept apart from the store's selling places, and rules for moving it, such as Zid's zero balance first. Settled by the proposals for Q1 and Q6. Q3-SA-085; Q3-WC-K0402; Q3-SH-K1536; Q3-ZD-K0230
- Which products need a licence in a place, and when it is checked: no full list for Salla or Zid, and no time Shopify checks, was in what was read. Keep open: product rules as data per place, licence fields on products, and the timing of any check. Settled by legal advice for each place. Q3-SA-N02; Q3-ZD-N04; Q3-SH-N02
- Which entity types a place admits, and what each gives, as Salla's freelance document is for Saudi citizens only. Keep open: entity types as a list per place. Settled by Q6 and the company decision on who may register. Q3-SA-014; Q3-ZD-K0239

## 6. Yemen: what its evidence allows, forbids or doesn't show

## 7. Company decisions it raises

- Whether Sharrwah checks sellers itself, relies on payment providers' checks, or both, and in which places. Q3-SA-037; Q3-ZD-P0118; Q3-WC-012
- Which identity services and payment providers Sharrwah works with, since their requirements then bind its sellers. Q3-ZD-P0117; Q3-SA-013; Q3-SH-057
- Who may register and take payments, by entity type and nationality, as Salla verifies a foreign merchant's store only with a Saudi commercial registration. Q3-SA-005; Q3-SA-014
- Which countries and parties Sharrwah won't serve, under whose sanctions lists, which turns on where the company is based. Q3-SH-K2268; Q3-BC-K0430; Q3-ZD-P0112
- Whether Sharrwah reviews products against licences or takes the seller's declaration, and who answers when a product breaks a law. Q3-BC-K0460; Q3-SA-057; Q3-SH-053
- Whether plans gate capabilities such as payment methods, product types and channels. Q3-SA-P0068; Q3-SA-029; Q3-BC-P0068
- How Sharrwah receives and keeps identity and business documents. Q3-SH-015; Q3-SA-013
- Sharrwah's own legal position in checking sellers and in returning buyers' payments, for the founder with a lawyer. Q3-SA-037; Q3-SH-072
