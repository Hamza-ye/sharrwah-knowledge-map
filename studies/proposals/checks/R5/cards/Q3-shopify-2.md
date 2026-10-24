# Cards: Q3 on shopify

20 records cited by `studies/proposals/drafts/Q3/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 45:** - A program or channel often needs another capability active, a match on role. Shop needs Shopify Payments activated; Mahally needs a paid plan and a verified store (not checked on WooCommerce; shown by Salla); and Zid Financing needs Zid Pay activated and approved. Q3-SH-077; Q3-SA-061; Q3-ZD-P0132
- **section 1, line 50:** - The platforms put requirements on two subjects, the person and the business. Shopify's person signing up is the contracting party, the "Store Owner". Every Shopify Payments account names one individual as account representative, never a company, and lists owners of 25% or more. Q3-SH-K1237; Q3-SH-020; Q3-SH-023
- **section 1, line 53:** - Some checks fall on the owner in person: on Shopify only the account owner can complete a Proof of Liveness check, and on Zid the store owner passes Nafath (not checked on WooCommerce; shown by Zid). Q3-SH-043; Q3-ZD-P0117
- **section 1, line 60:** - Payment partners approve, a match on role (BigCommerce's pricing page, official; the others help pages, stated): Zid's requirements go to the gateway "ليتم اعتماد الحساب لدى بوابة الدفع", and its Nafath request is in the service provider's name; a PayPal Braintree application on BigCommerce doesn't guarantee approval; WooPayments verifies with Stripe; and Shopify's banking partners require a real person on every account. Q3-ZD-P0118; Q3-ZD-P0047; Q3-BC-P0065; Q3-WC-012; Q3-SH-020
- **section 1, line 61:** - Law, regulators and networks set others, as the platforms report them: Shopify's European and UK verification follows the FCA and the Central Bank of Ireland, and its prohibited categories may come from law, network rules, Shopify or processors' providers; Zid's licences come from the relevant authorities; and Salla's e-commerce obligations from the e-commerce law and the Ministry of Commerce's guide. Q3-SH-065; Q3-SH-P0045; Q3-ZD-023; Q3-SA-033
- **section 1, line 65:** - When the seller applies, with review times that differ: Salla 24 to 48 hours; Shopify's documents up to 24 hours; WooPayments typically a couple of days. Zid's team reviews and notifies by email. Q3-SA-003; Q3-SH-014; Q3-WC-004; Q3-ZD-P0038
- **section 1, line 67:** - And again later. Shopify re-verifies periodically, and re-checks bank ownership when a payout account is added or replaced or business details change. Salla may ask for documents at any time, and Zid Pay's seller must report changes within a week. On BigCommerce, Stripe flags accounts for verification after a processing threshold. Q3-SH-066; Q3-SH-061; Q3-SA-051; Q3-ZD-078; Q3-BC-020
- **section 1, line 71:** - The store keeps working while a payment requirement is pending. On Shopify, the store stays usable while payouts are on hold. Salla lets the seller prepare the store and products before verification, a rejection leaves settings and products intact, and a verified store updating its data keeps taking orders and payments. Q3-SH-P0085; Q3-SA-016; Q3-SA-023; Q3-SA-006
- **section 1, line 72:** - Effects can be narrow: a detail failing American Express's rules stops American Express at checkout while other card brands continue, and a revoked P24 makes only P24 orders fail. Q3-SH-058; Q3-WC-034
- **section 1, line 73:** - Deadlines escalate. On Shopify in Europe and the UK, for new accounts, payouts pause at once, charges after 30 days, and payments are refunded 90 days after the first order, while payments through other providers are unaffected. Such a timeline outside Europe and the UK was not in what was read. Q3-SH-072; Q3-SH-073; Q3-SH-N01
- **section 1, line 75:** - Returning buyers' money matches on role across kinds: Zid Pay's terms (official page), Shopify's European and UK help page (stated), and Salla's agreement, which allows returning pending electronic payments to consumers for a breach of its tenth article (official page). Q3-ZD-P0012; Q3-SH-072; Q3-SA-P0083
- **section 1, line 76:** - Each records the state, a match on role across kinds: Shopify's ShopifyPaymentsAccount has a field for whether setup is completed (developer documentation, stated); Salla's payments answer carries `blocks_payment_activation` and each method's `blocked_by` (observed, store merchant, 8 October 2026); WooCommerce's shipped code gives an onboarding step a blocked status; and BigCommerce shows tasks and fund holds in its Actions section (stated). On Shopify store ibx5bt-xy, the saved markup of the Subscribe to Plus step, observed 30 September 2026, says "Shopify Payments is not available on your store.", as its accessibility tree did. Q3-SH-086; Q3-SA-073; Q3-SA-074; Q3-WC-041; Q3-BC-P0072; Q3-SH-108
- **section 1, line 77:** - Each tells the seller what is missing, as Shopify's alert takes the seller to the upload page, WooCommerce's notices appear on "Payments > Overview", and BigCommerce's Actions section lists the tasks. Q3-SH-017; Q3-WC-051; Q3-BC-P0072
- **section 2, line 81:** - **Seller** (proposed): the person who opens the account and contracts with Sharrwah, and the first subject of requirements, including the identity checks only that person can complete. It takes Shopify's Store Owner as the contracting party and BigCommerce's creator as the owner, and puts the owner-only checks on it, as Shopify's Proof of Liveness and Zid's Nafath do. Why: rule 3, since who carries a requirement is the data model. Q3-SH-K1237; Q3-BC-004; Q3-SH-043; Q3-ZD-P0117
- **section 2, line 85:** - **Business person** (proposed): each individual the business must name, with a role, such as Shopify's one individual representative and its owners of 25% or more, and the beneficial owners a provider asks about, as the Shop Pay Installments terms do in store ibx5bt-xy's saved markup, observed 30 September 2026. The roles and the ownership threshold are set per registration place, as Shopify's "For most regions" shows. Why: rules 1 and 3. Q3-SH-020; Q3-SH-023; Q3-SH-110
- **section 2, line 86:** - **Capability** (proposed): a thing a seller may do that a requirement set can gate: open the store to buyers, take payments through one method or provider, receive payouts, withdraw a balance, sell a product type or category, join a sales channel or program, or use a financing or tax service. One capability can require another, as Shop requires Shopify Payments, Mahally a verified store, and Zid Financing Zid Pay. Why: rule 2, so a change in one provider's requirements changes only its capability. Q3-SH-077; Q3-SA-061; Q3-ZD-P0132
- **section 2, line 87:** - **Capability status** (proposed): for each store and capability, available, blocked or restricted, with machine-readable reasons naming the unmet requirements. It takes Salla's `blocks_payment_activation`, `blocked_by` and `withdraw_disabled_reason`, WooCommerce's blocked onboarding step, and Shopify's field for setup completed. Why: rule 3, the data model. Q3-SA-073; Q3-SA-074; Q3-SA-077; Q3-WC-041; Q3-SH-086
- **section 2, line 88:** - **Requirement** (proposed): one condition, with its kind, subject, setter, validity and check. Its kinds come from the platforms: information, a document, an identity check, a plan, an accepted agreement, a store setting such as an address or test mode off, a product state such as a published product matching the activity, account security such as two-step authentication, account age such as WooPayments' 7 days before a first payout, a match between subjects such as the payout account's holder and the verified name, not being a listed party, as under Shopify Payments' sanctions rule, and another capability being active. Validity follows rules such as Zid's commercial register valid two months from activation. Its subject is the seller, a business person, the business, the store, a product or the payout account. Why: rule 2, since kinds will grow and each requirement is data. Q3-SH-028; Q3-ZD-P0116; Q3-SH-K1274; Q3-WC-P0038; Q3-SA-K1563; Q3-SH-K2268; Q3-ZD-013
- **section 2, line 90:** - The lists change: Shopify's Shop requirements are "subject to change without notice", its European and UK verification is being updated throughout 2026, and Zid's prohibited activities "يمكن تحديثها في أي وقت، مع إشعار التاجر". So a set is versioned data, and a met requirement keeps the version it was met under. Why: rule 2. Q3-SH-083; Q3-SH-065; Q3-ZD-P0111
- **section 2, line 91:** - **Submission** and **Review** (proposed): the seller gives information and documents inside Sharrwah and declares them true, as Salla's KYC schema requires; a review decides: pending, approved, rejected with reasons, or more needed. Each review has a checker, which is Sharrwah's team, a provider or an identity service, with its own attempt limits and timing, as Zid's team, Zid's gateway, and the daily attempts of Absher and Nafath show. Documents come only through Sharrwah, as Shopify accepts them only through its admin. Why: rule 2 for the checker, rule 3 for the data. Q3-SA-057; Q3-ZD-P0038; Q3-ZD-P0118; Q3-SA-008; Q3-ZD-K0262; Q3-SH-015
- **section 2, line 92:** - **Re-verification** (proposed): a met requirement is checked again when business details or the payout account change, at intervals, on request, or after a threshold; a duty to report changes within a set time is a per-place setting. While an update is reviewed, the met state holds and the store keeps taking orders and payments, as on Salla. Q3-SH-061; Q3-SH-066; Q3-SA-051; Q3-BC-020; Q3-ZD-078; Q3-SA-006
- **section 2, line 94:** - **Restriction** (proposed): what an unmet requirement does, scoped to the capability it gates: keep the store from buyers, block a payment method or checkout, allow only test payments (as store demo-fake-dev-store's saved markup, observed 30 September 2026, says of development stores), hold payouts, block withdrawals, or suspend the store. Each records its reason and the requirements it waits on, and lifts when they are met, as Shopify's pauses lift "automatically after you complete verification". It follows the narrow effects the platforms show: American Express alone stopping, other providers unaffected, the store usable while payouts are held, products kept after a rejection. Why: rule 2. Q3-SH-058; Q3-SH-073; Q3-SH-P0085; Q3-SA-023; Q3-SH-070; Q3-SH-106
- **section 2, line 95:** - **Escalation** (proposed): a restriction can step up on a schedule (hold payouts, then pause charges, then return payments to buyers), with steps and days set per registration place, as Shopify's European and UK timeline and Zid Pay's 14 days show. Why: rule 1. Q3-SH-072; Q3-ZD-P0012
- **section 2, line 96:** - Holding payouts, blocking withdrawals and returning payments to buyers act on sellers' money. The design provides for them, and for gating payouts and a balance; any arrangement in which sellers' money is held through Sharrwah, by Sharrwah itself or by a payment company in an account opened through Sharrwah, goes live only by the founder's decision. Q3-SA-077; Q3-ZD-P0012; Q3-SH-P0085
- **section 2, line 101:** - **Seller action list** (proposed): one list of each blocked capability, the requirements it waits on, any deadline and the next step, read from the capability status, like BigCommerce's Actions section and Shopify's alerts. Left to the build. Q3-BC-P0072; Q3-SH-017; Q3-WC-051
- **section 3, line 109:** - Sales channels and programs, each with its own requirement set: Shop and Mahally. Q3-SH-077; Q3-SA-061
- **section 3, line 120:** - Per person: the identity checks only the owner completes. Q3-SH-043; Q3-ZD-P0117
- **section 5, line 146:** - What unmet requirements do to money: holding payouts, blocking withdrawals, returning payments to buyers, and the days between, as Shopify, Zid and Salla show them; Salla's period was not in what was read. Keep open, as a money flow: a restriction type for each, with schedules per place, all off until decided. Settled by the founder's decision under the guard, Q5's proposal and providers' terms. Q3-SH-072; Q3-ZD-P0012; Q3-SA-002; Q3-SA-N01
- **section 5, line 150:** - Which lists a seller is checked against: the platforms name their own (US, Canadian and EU lists on Shopify Payments; US lists on BigCommerce), and Yemen's evidence shows Ansarallah designated at the United States' area. Keep open: the lists as a setting of the requirement, by place and by the company's jurisdiction. Settled by the company decision on where it is based (section 7). Q3-SH-K2268; Q3-BC-K0430; YA-27 (FTO and SDGT @ the United States' area, as of 2025-03-05)
- **section 7, line 171:** - Which countries and parties Sharrwah won't serve, under whose sanctions lists, which turns on where the company is based. Q3-SH-K2268; Q3-BC-K0430; Q3-ZD-P0112
- **section 7, line 174:** - How Sharrwah receives and keeps identity and business documents. Q3-SH-015; Q3-SA-013
- **section 7, line 175:** - Sharrwah's own legal position in checking sellers and in returning buyers' payments, for the founder with a lawyer. Q3-SA-037; Q3-SH-072

## The cards

### Q3-SH-077

**Cited at:** section 1, line 45; section 2, line 86; section 3, line 109

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-077
- bears_on: 1;4
- identifier: Requirements for displaying your store in Shop
- statement: * **Activation of Shopify Payments** - Your store has Shopify Payments activated.
- cite_ids: Q3-SH-C112
- from: held

**Citation Q3-SH-C112:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shop/eligibility/requirements.md` | Requirements for displaying your store in Shop, list item 3 | 2026-10-18 | kind: stated | quote check: found (markup removed)
- quote: * **Activation of Shopify Payments** - Your store has Shopify Payments activated.
- title: Requirements for displaying your store in Shop
- the page opens: Note The list of merchant requirements is subject to change without notice. To have your store displayed in the Shop app and shop.com, there are certain requirements that your store must meet. These requirements ensure a consistent experience for merchants and customers. It's important to review and fulfill the following main criteria: * Compliance with Terms of Service and Acceptable Use Policy - Your store complies with Shopify's Terms of Service and Acceptable Use Policy. * Active Starter pla…
- a note box: Note The list of merchant requirements is subject to change without notice.
- headings: Requirements for displaying your store in Shop
- in context: …ur store must meet. These requirements ensure a consistent experience for merchants and customers. It's important to review and fulfill the following main criteria: * Compliance with Terms of Service and Acceptable Use Policy - Your store complies with Shopify's Terms of Service and Acceptable Use Policy. * Active Starter plan or higher - Your store is on an active Starter plan or higher. Learn more about checking or upgrading your current plan. ⟪* Activation of Shopify Payments - Your store has Shopify Payments activated.⟫ Learn more about Shopify Payments requirements. * Chargeback rate - Your store has had a chargeback rate of less than 1% in the last six months. Your chargeback rate includes any chargebacks placed on transactions that are processed with Shopify Payments. * Shop visibility - Eligible merchants are automatically added to become searchable within the Shop app and shop.com. You don't need to have the Shop channel installed to be eligible, though in…  (matched markup removed)

### Q3-SH-K1237

**Cited at:** section 1, line 50; section 2, line 81

**Record** (`studies/proposals/records/Q3/shopify/copied.tsv`):
- concern_id: SH-C-001
- placement: responsible
- structure: https://www.shopify.com/legal/terms
- identifier: 2.1 Store Owner
- statement: the person signing up for the Service by opening an Account will be the contracting party ("Store Owner") for the purposes of our Terms of Service
- cite_ids: SH-S-0019
- note: first run's citation, moved from decides: the sentence names the Store Owner as the contracting party, which answers who is responsible

**Citation SH-S-0019:** `https://www.shopify.com/legal/terms` | 2.1 Store Owner | 2026-08-01 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/143-shopify.com/text.txt` (fetched 2026-10-11T06:13:11Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/117-shopify.com/text.txt` (fetched 2026-10-12T10:51:23Z, captured)
- quote: the person signing up for the Service by opening an Account will be the contracting party ("Store Owner") for the purposes of our Terms of Service
- title: Shopify Terms of Service - Shopify
- in context: …Store Owner responsible for your Account. We automatically create certain accounts for you to accept payments. You are responsible for activating and deactivating these accounts and complying with their terms, which may be with various third parties, including but not limited to PayPal, Apple Pay, Google Payment and Shop Pay. Any domain you purchase through us will automatically renew unless you opt out. 2.1 Store Owner Subject to Section 2.1.2, ⟪the person signing up for the Service by opening an Account will be the contracting party ("Store Owner") for the purposes of our Terms of Service⟫ and will be the person who is authorized to use any corresponding Account we may provide to the Store Owner in connection with the Service. You are responsible for ensuring that the name of the Store Owner (including the legal name of the company that owns the Store, if applicable) is clearly visible on the Store's website. If you are signing up for the Services on behalf of your employer, your employer will be the Store Owner. If you are signin…

### Q3-SH-020

**Cited at:** section 1, line 50; section 1, line 60; section 2, line 85

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-020
- bears_on: 1;4
- identifier: The account representative
- statement: Every Shopify Payments account must list one individual as the account representative, even when the business is a registered company or is owned by another company. Shopify's banking partners require identity information for a real person on every account, so you can't list a company as the account representative.
- cite_ids: Q3-SH-C028;Q3-SH-C029
- from: held

**Citation Q3-SH-C028:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | The account representative | 2026-10-18 | kind: stated | quote check: found
- quote: Every Shopify Payments account must list one individual as the account representative, even when the business is a registered company or is owned by another company.
- title: Setting up your Shopify Payments account
- the page opens: To get started with Shopify Payments, first check the list of supported countries to confirm availability in your region. After confirming your eligibility, you can activate the service and complete the verification process. Your Shopify Payments payouts might be placed on hold until two-step authentication is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your store currency bef…
- a note box: Staff permissions Only the store owner can activate or switch to Shopify Payments. Staff members can't switch to Shopify Payments.
- a note box: Note Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- headings: Setting up your Shopify Payments account > Uploading documents for Shopify Payments verification {#required-documentation} > The account representative {#account-representative}
- in context: …match. Correct that address on your account, or upload a document that matches the address that's already on your account. Your account details and your documents must match. Depending on the reason, you can correct the details on your account, or you can upload a document that matches your account. Before you change a business address, review the address requirements for Shopify Payments. ### The account representative {#account-representative} ⟪Every Shopify Payments account must list one individual as the account representative, even when the business is a registered company or is owned by another company.⟫ Shopify's banking partners require identity information for a real person on every account, so you can't list a company as the account representative. The person you list depends on your business type: * **Individuals and sole proprietorships**: The person who owns and operates the business. * **All other business types**: An owner or a senior executive who has the authority to legally bind the business to the [Shopify Payments Terms of Service]…

**Citation Q3-SH-C029:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | The account representative | 2026-10-18 | kind: stated | quote check: found
- quote: Shopify's banking partners require identity information for a real person on every account, so you can't list a company as the account representative.
- title, opening and note boxes: as for this source's citation above
- headings: Setting up your Shopify Payments account > Uploading documents for Shopify Payments verification {#required-documentation} > The account representative {#account-representative}
- in context: …t match. Depending on the reason, you can correct the details on your account, or you can upload a document that matches your account. Before you change a business address, review the address requirements for Shopify Payments. ### The account representative {#account-representative} Every Shopify Payments account must list one individual as the account representative, even when the business is a registered company or is owned by another company. ⟪Shopify's banking partners require identity information for a real person on every account, so you can't list a company as the account representative.⟫ The person you list depends on your business type: * **Individuals and sole proprietorships**: The person who owns and operates the business. * **All other business types**: An owner or a senior executive who has the authority to legally bind the business to the [Shopify Payments Terms of Service](https://www.shopify.com/legal). Who qualifies as an account representative may vary slightly depending on your region. [Check your region's specific r…

### Q3-SH-023

**Cited at:** section 1, line 50; section 2, line 85

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-023
- bears_on: 1
- identifier: Understanding the terms Owner, Director and Executive
- statement: For most regions, owners are defined as any individual person who directly or indirectly (through ownership in a parent or holding company) owns 25% or more of the business’s equity. If there are individuals who own equity of your business through their ownership of the holding company, then you must list them as beneficial owners.
- scope: For most regions
- cite_ids: Q3-SH-C033;Q3-SH-C034
- from: held

**Citation Q3-SH-C033:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | Understanding the terms Owner, Director and Executive | 2026-10-18 | kind: stated | quote check: found
- quote: For most regions, owners are defined as any individual person who directly or indirectly (through ownership in a parent or holding company) owns 25% or more of the business’s equity.
- title: Setting up your Shopify Payments account
- the page opens: To get started with Shopify Payments, first check the list of supported countries to confirm availability in your region. After confirming your eligibility, you can activate the service and complete the verification process. Your Shopify Payments payouts might be placed on hold until two-step authentication is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your store currency bef…
- a note box: Staff permissions Only the store owner can activate or switch to Shopify Payments. Staff members can't switch to Shopify Payments.
- a note box: Note Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- headings: Setting up your Shopify Payments account > Uploading documents for Shopify Payments verification {#required-documentation} > Understanding the terms Owner, Director and Executive
- in context: …s a beneficial owner. Ownership is recorded in a separate field on the account, and only applies if the person is simultaneously given the **Owner** role. Businesses where no individual owns 25% or more, such as publicly traded companies, government entities, and non-profits, still need to name an account representative. This requirement comes from banking regulations and can't be waived. ### Understanding the terms Owner, Director and Executive ⟪For most regions, owners are defined as any individual person who directly or indirectly (through ownership in a parent or holding company) owns 25% or more of the business's equity.⟫ If there are individuals who own equity of your business through their ownership of the holding company, then you must list them as beneficial owners. [See your country's specific page for more guidance](/manual/payments/shopify-payments/supported-countries/index) on who is required to be listed on your account, and who qualifies as a beneficial owner. Directors are individuals who are members of the governing board of your company, and are typi…

**Citation Q3-SH-C034:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | Understanding the terms Owner, Director and Executive | 2026-10-18 | kind: stated | quote check: found
- quote: If there are individuals who own equity of your business through their ownership of the holding company, then you must list them as beneficial owners.
- title, opening and note boxes: as for this source's citation above
- headings: Setting up your Shopify Payments account > Uploading documents for Shopify Payments verification {#required-documentation} > Understanding the terms Owner, Director and Executive
- in context: …al owns 25% or more, such as publicly traded companies, government entities, and non-profits, still need to name an account representative. This requirement comes from banking regulations and can't be waived. ### Understanding the terms Owner, Director and Executive For most regions, owners are defined as any individual person who directly or indirectly (through ownership in a parent or holding company) owns 25% or more of the business's equity. ⟪If there are individuals who own equity of your business through their ownership of the holding company, then you must list them as beneficial owners.⟫ [See your country's specific page for more guidance](/manual/payments/shopify-payments/supported-countries/index) on who is required to be listed on your account, and who qualifies as a beneficial owner. Directors are individuals who are members of the governing board of your company, and are typically shown on most business registration extracts. Executives are individuals who have a significant control over the business and are responsible for…

### Q3-SH-043

**Cited at:** section 1, line 53; section 2, line 81; section 3, line 120

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-043
- bears_on: 1;4
- identifier: Proof of Liveness check
- statement: Only the account owner can complete a Liveness check and photo ID verification. This check is necessary to complete the Shopify Payments setup process and ensure that your store can process transactions using Shopify Payments.
- cite_ids: Q3-SH-C058
- from: held

**Citation Q3-SH-C058:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/proof-of-liveness.md` | Proof of Liveness check | 2026-10-18 | kind: stated | quote check: found
- quote: Only the account owner can complete a Liveness check and photo ID verification. This check is necessary to complete the Shopify Payments setup process and ensure that your store can process transactions using Shopify Payments.
- title: Proof of Liveness check
- the page opens: The requirement for a Proof of Liveness check for Shopify Payments is based on your country. Learn more about supported countries and documentation requirements. To complete a Proof of Liveness check, you'll use your webcam or phone to upload a selfie. You also need to verify your photo ID using one of the following methods: * Use your webcam or phone to take a photo of your ID document. * Upload a photo of your ID document. Only the account owner can complete a Liveness check and photo ID verif…
- headings: Proof of Liveness check
- in context: …ess check for Shopify Payments is based on your country. Learn more about [supported countries and documentation requirements](/manual/payments/shopify-payments/supported-countries). To complete a Proof of Liveness check, you'll use your webcam or phone to upload a selfie. You also need to verify your photo ID using one of the following methods: * Use your webcam or phone to take a photo of your ID document. * Upload a photo of your ID document. ⟪Only the account owner can complete a Liveness check and photo ID verification. This check is necessary to complete the Shopify Payments setup process and ensure that your store can process transactions using Shopify Payments.⟫ ## Guidance for providing your identity document When providing your identity document, ensure the following so that your identity document submission is successful: * Capture a clear image. Make sure that the images aren't too dark or too bright, and that they don't have glare. * Take a live photo of the ID with your mobile device instead of uploading a scan. * Capture the ID against a dark background. Light, colorful or patterned backgrounds a…

### Q3-SH-065

**Cited at:** section 1, line 61; section 2, line 90

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-065
- bears_on: 1;4
- identifier: Shopify Payments account verification updates in Europe and the United Kingdom
- statement: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI).
- scope: Europe and the United Kingdom (UK)
- cite_ids: Q3-SH-C097
- from: held

**Citation Q3-SH-C097:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/eu-verification.md` | Shopify Payments account verification updates in Europe and the United Kingdom | 2026-10-18 | kind: stated | quote check: found
- quote: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI).
- title: Shopify Payments account verification updates in Europe and the United Kingdom
- the page opens: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI). If your Shopify Payments account is affected, then you receive a notification in your Shopify admin and by email. If you receive a prompt to update or confirm your Shopify Payments account details, then comple…
- a note box: Staff permissions Only the store owner can view and complete verification requests for Shopify Payments accounts. Staff members don't have access to the verification request page.
- a note box: Note If you're based in Denmark, Italy, Poland, Spain, or Sweden, then you can optionally provide a national identification number to help complete verification.
- a note box: Caution Payments processed using payment providers other than Shopify Payments aren't affected.
- headings: Shopify Payments account verification updates in Europe and the United Kingdom
- in context: # Shopify Payments account verification updates in Europe and the United Kingdom ⟪Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI).⟫ If your Shopify Payments account is affected, then you receive a notification in your Shopify admin and by email. If you receive a prompt to update or confirm your Shopify Payments account details, then complete the process as soon as possible to avoid disruptions to your Shopify Payments account. ## Scope and timeline for verification updates {#update-scope-and-timeline} The following details summarize who's affected by these updates, what's ch…

### Q3-SH-014

**Cited at:** section 1, line 65

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-014
- bears_on: 4
- identifier: Uploading documents for Shopify Payments verification, Note
- statement: Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- cite_ids: Q3-SH-C016
- from: held

**Citation Q3-SH-C016:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | Uploading documents for Shopify Payments verification, Note | 2026-10-18 | kind: stated | quote check: found
- quote: Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- title: Setting up your Shopify Payments account
- the page opens: To get started with Shopify Payments, first check the list of supported countries to confirm availability in your region. After confirming your eligibility, you can activate the service and complete the verification process. Your Shopify Payments payouts might be placed on hold until two-step authentication is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your store currency bef…
- a note box: Staff permissions Only the store owner can activate or switch to Shopify Payments. Staff members can't switch to Shopify Payments.
- a note box: Note Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- headings: Setting up your Shopify Payments account > Uploading documents for Shopify Payments verification {#required-documentation}
- in context: …dentity of the business, the identities of individuals linked to it, and the nature of the relationship between the two. Shopify never physically mails documentation to you. Any important documents or communications are emailed, or made digitally available to the person listed as Account Owner of the store in your Shopify admin. ## Uploading documents for Shopify Payments verification {#required-documentation} <aside class="note"><h4>Note</h4><p>⟪Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.⟫</p> </aside> Due to the sensitive nature of the personal information that's requested, Shopify can only accept documents that are uploaded through the secure banners in your Shopify admin. For your security and privacy, any documents sent through email or support chat are redacted and rendered unusable. To complete the verification process, ensure that any documentation you submit meets the following requirements: * The documentation is photogra…

### Q3-SH-066

**Cited at:** section 1, line 67; section 2, line 92

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-066
- bears_on: 4
- identifier: Verification requirements
- statement: Periodic re-verification is a normal part of using Shopify Payments. Verification requirements from financial partners and card networks evolve over time, which means you might be asked to confirm or update information even if nothing about your business has changed.
- cite_ids: Q3-SH-C098
- from: held

**Citation Q3-SH-C098:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/eu-verification.md` | Verification requirements {#verification-requirements} | 2026-10-18 | kind: stated | quote check: found
- quote: Periodic re-verification is a normal part of using Shopify Payments. Verification requirements from financial partners and card networks evolve over time, which means you might be asked to confirm or update information even if nothing about your business has changed.
- title: Shopify Payments account verification updates in Europe and the United Kingdom
- the page opens: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI). If your Shopify Payments account is affected, then you receive a notification in your Shopify admin and by email. If you receive a prompt to update or confirm your Shopify Payments account details, then comple…
- a note box: Staff permissions Only the store owner can view and complete verification requests for Shopify Payments accounts. Staff members don't have access to the verification request page.
- a note box: Note If you're based in Denmark, Italy, Poland, Spain, or Sweden, then you can optionally provide a national identification number to help complete verification.
- a note box: Caution Payments processed using payment providers other than Shopify Payments aren't affected.
- headings: Shopify Payments account verification updates in Europe and the United Kingdom > Verification requirements {#verification-requirements}
- in context: …"row">Spain</td> <td>Sweden</td> <td>Switzerland</td> </tr> <tr> <td scope="row">United Kingdom</td> <td></td> <td></td> </tr> </tbody> </table> ## Verification requirements {#verification-requirements} <aside class="note note-staff-permissions"><h4>Staff permissions</h4><p>Only the store owner can view and complete verification requests for Shopify Payments accounts. Staff members don't have access to the verification request page.</p> </aside> ⟪Periodic re-verification is a normal part of using Shopify Payments. Verification requirements from financial partners and card networks evolve over time, which means you might be asked to confirm or update information even if nothing about your business has changed.⟫ If your account requires re-verification, then the store owner receives a notification by email and in the Shopify admin. The verification request is accessible from **Settings** > **Payments** > **Shopify Payments** in your Shopify admin. Your information might be verified with no action required. If your information can't be verified, then you might be asked to complete one or more of the following verification types. ### Person verification {…

### Q3-SH-061

**Cited at:** section 1, line 67; section 2, line 92

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-061
- bears_on: 1;4
- identifier: When bank account ownership verification is required
- statement: Bank account ownership verification might be required when you add or replace a payout bank account for Shopify Payments. You might also be asked to verify your bank account again if your Shopify Payments business details change.
- cite_ids: Q3-SH-C091
- from: held

**Citation Q3-SH-C091:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/bank-account-ownership-verification.md` | When bank account ownership verification is required | 2026-10-18 | kind: stated | quote check: found
- quote: Bank account ownership verification might be required when you add or replace a payout bank account for Shopify Payments. You might also be asked to verify your bank account again if your Shopify Payments business details change.
- title: Verifying ownership of your Shopify Payments bank account
- the page opens: When you use Shopify Payments, your payout bank account might need ownership verification. This check confirms that the bank account belongs to you or your business. If your bank account ownership can't be verified, then the store owner receives a notification in the Shopify admin and might also receive an email. You can review your bank account status in your Shopify Payments settings. When bank account ownership verification is required Bank account ownership verification might be required whe…
- headings: Verifying ownership of your Shopify Payments bank account > When bank account ownership verification is required
- in context: …bank account might need ownership verification. This check confirms that the bank account belongs to you or your business. If your bank account ownership can't be verified, then the store owner receives a notification in the Shopify admin and might also receive an email. You can review your bank account status in your [Shopify Payments settings](https://admin.shopify.com/settings/payments). ## When bank account ownership verification is required ⟪Bank account ownership verification might be required when you add or replace a payout bank account for Shopify Payments. You might also be asked to verify your bank account again if your Shopify Payments business details change.⟫ Verification compares the name on your bank account with information on your Shopify Payments account. This information can include your legal business name or account representative name. ## Ways to verify your bank account Depending on your region and account, you might be able to verify your bank account in one of the following ways: * Connect your bank account using your bank login. * Enter your bank account details manually. * Upload a supp…

### Q3-SH-P0085

**Cited at:** section 1, line 71; section 2, line 94; section 2, line 96

**Record** (`studies/proposals/records/Q3/shopify/copied-pilot.tsv`):
- stmt_id: S01-SH-084
- bullet: c
- placement: decides
- identifier: Shopify Payments account holds, note
- statement: You can still use your Shopify store when your Shopify Payments account is on hold. You can continue to work on your store, however, you can't receive payouts through Shopify Payments until the reason for the hold is resolved.
- cite_ids: S01-SH-C131
- from: new

**Citation S01-SH-C131:** `https://help.shopify.com/en/manual/payments/shopify-payments/payouts/account-holds.md` | note | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/068-help.shopify.com/text.txt` (fetched 2026-10-11T06:13:02Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/036-help.shopify.com/text.txt` (fetched 2026-10-12T10:50:14Z, captured)
- quote: You can still use your Shopify store when your Shopify Payments account is on hold. You can continue to work on your store, however, you can't receive payouts through Shopify Payments until the reason for the hold is resolved.
- title: Shopify Payments account holds
- the page opens: After you set up your Shopify Payments account, you might receive a notification in your Shopify admin or an email from Shopify indicating that your Shopify Payments account is on hold. The message in your Shopify admin might include information that's specific to your store, or it might request that you contact Shopify Support. Only the store owner can access specific account details. The best source of information to resolve the issue is either the notification in your Shopify admin or the ema…
- a note box: Note You can still use your Shopify store when your Shopify Payments account is on hold. You can continue to work on your store, however, you can't receive payouts through Shopify Payments until the reason for the hold is resolved.
- headings: Shopify Payments account holds
- in context: …wner can access specific account details. The best source of information to resolve the issue is either the notification in your Shopify admin or the email that's sent to the store owner. Ensure that you follow any email requests or admin messages to resolve the issue as quickly as possible. If there isn't enough information, then you can [contact Shopify Support](/manual/your-account/contact-shopify-support). <aside class="note"><h4>Note</h4><p>⟪You can still use your Shopify store when your Shopify Payments account is on hold. You can continue to work on your store, however, you can't receive payouts through Shopify Payments until the reason for the hold is resolved.⟫</p> </aside> ## Reasons for account holds {#reasons-for-account-holds} Account holds are placed for a variety of reasons, and are account specific. Shopify Payments accounts are subject to standard reviews throughout the account's lifespan. Some possible reasons for account holds are related to [information requirements](/manual/payments/shopify-payments/onboarding/account-setup), [incorrect bank account details](/manual/payments/shopify-payment…

### Q3-SH-058

**Cited at:** section 1, line 72; section 2, line 94

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-058
- bears_on: 4
- identifier: American Express requirements for Shopify Payments
- statement: If a detail on your account doesn't meet these requirements, then American Express stops being available at checkout in your store. Your store keeps accepting other card brands throughout. In some cases you're contacted by Shopify Trust teams and asked to make the update by a specific date instead. American Express stays available at checkout until that date passes.
- cite_ids: Q3-SH-C086;Q3-SH-C087
- from: held

**Citation Q3-SH-C086:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/american-express-requirements.md` | American Express requirements for Shopify Payments | 2026-10-18 | kind: stated | quote check: found
- quote: If a detail on your account doesn't meet these requirements, then American Express stops being available at checkout in your store. Your store keeps accepting other card brands throughout. In some cases you're contacted by Shopify Trust teams and asked to make the update by a specific date instead.
- title: American Express requirements for Shopify Payments
- the page opens: American Express sets its own requirements for the addresses and the names recorded on a payment account. These requirements apply to your Shopify Payments account in addition to the general Shopify Payments eligibility requirements. If a detail on your account doesn't meet these requirements, then American Express stops being available at checkout in your store. Your store keeps accepting other card brands throughout. In some cases you're contacted by Shopify Trust teams and asked to make the u…
- headings: American Express requirements for Shopify Payments
- in context: # American Express requirements for Shopify Payments American Express sets its own requirements for the addresses and the names recorded on a payment account. These requirements apply to your Shopify Payments account in addition to the general [Shopify Payments eligibility](/manual/payments/shopify-payments/onboarding/eligibility) requirements. ⟪If a detail on your account doesn't meet these requirements, then American Express stops being available at checkout in your store. Your store keeps accepting other card brands throughout. In some cases you're contacted by Shopify Trust teams and asked to make the update by a specific date instead.⟫ American Express stays available at checkout until that date passes. When American Express is unavailable at checkout, your payment methods settings display a notice under **American Express** that says your business details don't meet American Express requirements. <figure class="figure"><img src="https://cdn.shopify.com/shopifycloud/help-center/manual/shopify-pay/american-express-unavailable-at-checkout.png" alt="The American Express payment m…

**Citation Q3-SH-C087:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/american-express-requirements.md` | American Express requirements for Shopify Payments | 2026-10-18 | kind: stated | quote check: found
- quote: American Express stays available at checkout until that date passes.
- title, opening and note boxes: as for this source's citation above
- headings: American Express requirements for Shopify Payments
- in context: …fy Payments account in addition to the general [Shopify Payments eligibility](/manual/payments/shopify-payments/onboarding/eligibility) requirements. If a detail on your account doesn't meet these requirements, then American Express stops being available at checkout in your store. Your store keeps accepting other card brands throughout. In some cases you're contacted by Shopify Trust teams and asked to make the update by a specific date instead. ⟪American Express stays available at checkout until that date passes.⟫ When American Express is unavailable at checkout, your payment methods settings display a notice under **American Express** that says your business details don't meet American Express requirements. <figure class="figure"><img src="https://cdn.shopify.com/shopifycloud/help-center/manual/shopify-pay/american-express-unavailable-at-checkout.png" alt="The American Express payment method in the payment methods settings, with a notice that it's unavai…

### Q3-SH-072

**Cited at:** section 1, line 73; section 1, line 75; section 2, line 95; section 5, line 146; section 7, line 175

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-072
- bears_on: 4
- identifier: Verification timeline for new accounts
- statement: - Your payouts are paused immediately. - Your charges are paused 30 days after your first Shopify Payments order. - Payments processed through Shopify Payments are refunded to your customers 90 days after your first Shopify Payments order.
- scope: Shopify Payments accounts in Europe and the United Kingdom (UK)
- cite_ids: Q3-SH-C106;Q3-SH-C107
- from: held

**Citation Q3-SH-C106:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/eu-verification.md` | Verification timeline for new accounts {#new-account-deadline} | 2026-10-18 | kind: stated | quote check: found
- quote: Until you complete verification, the following actions occur:
- title: Shopify Payments account verification updates in Europe and the United Kingdom
- the page opens: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI). If your Shopify Payments account is affected, then you receive a notification in your Shopify admin and by email. If you receive a prompt to update or confirm your Shopify Payments account details, then comple…
- a note box: Staff permissions Only the store owner can view and complete verification requests for Shopify Payments accounts. Staff members don't have access to the verification request page.
- a note box: Note If you're based in Denmark, Italy, Poland, Spain, or Sweden, then you can optionally provide a national identification number to help complete verification.
- a note box: Caution Payments processed using payment providers other than Shopify Payments aren't affected.
- headings: Shopify Payments account verification updates in Europe and the United Kingdom > Verification timeline for new accounts {#new-account-deadline}
- in context: …ines that apply to your account. ## Verification timeline for new accounts {#new-account-deadline} If you created your Shopify Payments account in or after June 2026, then you must complete verification to receive payouts and to continue processing payments. Your payouts are paused until you complete verification, and if verification isn't complete within 90 days of your first Shopify Payments order, then payments are refunded to your customers. ⟪Until you complete verification, the following actions occur:⟫ - Your payouts are paused immediately. - Your charges are paused 30 days after your first Shopify Payments order. - Payments processed through Shopify Payments are refunded to your customers 90 days after your first Shopify Payments order. To prevent these holds, complete verification as soon as possible. After verification is successful, your payouts and charges resume automatically. <aside class="note note-caution"><h4>Caution</h4><p>Payments …

**Citation Q3-SH-C107:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/eu-verification.md` | Verification timeline for new accounts {#new-account-deadline}, list | 2026-10-18 | kind: stated | quote check: found
- quote: - Your payouts are paused immediately. - Your charges are paused 30 days after your first Shopify Payments order. - Payments processed through Shopify Payments are refunded to your customers 90 days after your first Shopify Payments order.
- title: Shopify Payments account verification updates in Europe and the United Kingdom
- the page opens: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI). If your Shopify Payments account is affected, then you receive a notification in your Shopify admin and by email. If you receive a prompt to update or confirm your Shopify Payments account details, then comple…
- a note box: Staff permissions Only the store owner can view and complete verification requests for Shopify Payments accounts. Staff members don't have access to the verification request page.
- a note box: Note If you're based in Denmark, Italy, Poland, Spain, or Sweden, then you can optionally provide a national identification number to help complete verification.
- a note box: Caution Payments processed using payment providers other than Shopify Payments aren't affected.
- headings: Shopify Payments account verification updates in Europe and the United Kingdom > Verification timeline for new accounts {#new-account-deadline}
- in context: …new accounts {#new-account-deadline} If you created your Shopify Payments account in or after June 2026, then you must complete verification to receive payouts and to continue processing payments. Your payouts are paused until you complete verification, and if verification isn't complete within 90 days of your first Shopify Payments order, then payments are refunded to your customers. Until you complete verification, the following actions occur: ⟪- Your payouts are paused immediately. - Your charges are paused 30 days after your first Shopify Payments order. - Payments processed through Shopify Payments are refunded to your customers 90 days after your first Shopify Payments order.⟫ To prevent these holds, complete verification as soon as possible. After verification is successful, your payouts and charges resume automatically. <aside class="note note-caution"><h4>Caution</h4><p>Payments processed using payment providers other than Shopify Payments aren't affected.</p> </aside> If this timeline applies to your account, then warnings are displayed in the store owner's Shopify admin indicating when each action will occur. If …

### Q3-SH-073

**Cited at:** section 1, line 73; section 2, line 94

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-073
- bears_on: 4
- identifier: Verification timeline for new accounts, Caution
- statement: Payments processed using payment providers other than Shopify Payments aren't affected.
- scope: Shopify Payments accounts in Europe and the United Kingdom (UK)
- cite_ids: Q3-SH-C108
- from: held

**Citation Q3-SH-C108:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/eu-verification.md` | Verification timeline for new accounts, Caution | 2026-10-18 | kind: stated | quote check: found
- quote: Payments processed using payment providers other than Shopify Payments aren't affected.
- title: Shopify Payments account verification updates in Europe and the United Kingdom
- the page opens: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI). If your Shopify Payments account is affected, then you receive a notification in your Shopify admin and by email. If you receive a prompt to update or confirm your Shopify Payments account details, then comple…
- a note box: Staff permissions Only the store owner can view and complete verification requests for Shopify Payments accounts. Staff members don't have access to the verification request page.
- a note box: Note If you're based in Denmark, Italy, Poland, Spain, or Sweden, then you can optionally provide a national identification number to help complete verification.
- a note box: Caution Payments processed using payment providers other than Shopify Payments aren't affected.
- headings: Shopify Payments account verification updates in Europe and the United Kingdom > Verification timeline for new accounts {#new-account-deadline}
- in context: …ns occur: - Your payouts are paused immediately. - Your charges are paused 30 days after your first Shopify Payments order. - Payments processed through Shopify Payments are refunded to your customers 90 days after your first Shopify Payments order. To prevent these holds, complete verification as soon as possible. After verification is successful, your payouts and charges resume automatically. <aside class="note note-caution"><h4>Caution</h4><p>⟪Payments processed using payment providers other than Shopify Payments aren't affected.⟫</p> </aside> If this timeline applies to your account, then warnings are displayed in the store owner's Shopify admin indicating when each action will occur. If you created your Shopify Payments account before June 2026, then this timeline doesn't apply to you. Your payouts can still be paused if you [miss a verification deadline](#missed-deadline). ## Troubleshooting verification issues {#troubleshoot} If you're having difficulty completing a S…

### Q3-SH-086

**Cited at:** section 1, line 76; section 2, line 87

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-086
- bears_on: 4
- identifier: ShopifyPaymentsAccount.activated
- statement: Whether the Shopify Payments setup is completed.
- cite_ids: Q3-SH-C121
- from: held
- note: Field activated of the ShopifyPaymentsAccount object, GraphQL Admin API, api_version 2026-07

**Citation Q3-SH-C121:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz` | 8639159 | 2026-09-30 | kind: stated | quote check: found
- quote: Whether the Shopify Payments setup is completed.
- title: ShopifyPaymentsAccount - GraphQL Admin
- headings: Shopify​Payments​Account > Fields
- in context: …. Access balance transactions to review individual charges, refunds, and adjustments that affect your account balance. Query payouts to track money movement between your Shopify Payments balance and bank accounts. ## Fields * accountOpenerName [String](https://shopify.dev/docs/api/admin-graphql/latest/scalars/String) The name of the account opener. * activated [Boolean!](https://shopify.dev/docs/api/admin-graphql/latest/scalars/Boolean) non-null ⟪Whether the Shopify Payments setup is completed.⟫ * balance [\[MoneyV2!\]!](https://shopify.dev/docs/api/admin-graphql/latest/objects/MoneyV2) non-null Current balances in all currencies for the account. * balanceTransactions [ShopifyPaymentsBalanceTransactionConnection!](https://shopify.dev/docs/api/admin-graphql/latest/connections/ShopifyPaymentsBalanceTransactionConnection) non-null A list of balance transactions associated with the shop. * after [String](https://shopify.dev/docs/api/admin-g…

### Q3-SH-108

**Cited at:** section 1, line 76

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-108
- bears_on: 1;4
- identifier: Subscribe to Plus (admin /access_account/plus/upgrade), Shopify Payments card rates
- statement: Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments
- scope: store ibx5bt-xy, observed 2026-09-30
- cite_ids: Q3-SH-C152
- from: held
- note: In the saved HTML of step 422; the step's steps/422.aria.yaml shows the same words (term and definition). The saved HTML of step 422 in run 20260930T103225Z-sweep-dev (store demo-fake-dev-store) holds the same words. Observation of one store on one date.

**Citation Q3-SH-C152:** `observed-sh@51626891aa711ee9c3ef2d05ce63c95396dca949:derived/step-text-from-html/20260930T045741Z-sweep-trial2/422.html.txt` | run 20260930T045741Z-sweep-trial2, step 422 (access_account/plus/upgrade) | 2026-09-30 | kind: observed | quote check: found
- step 422: visit route plus_inactive_account:upgrade:overview (path from router) | https://admin.shopify.com/store/ibx5bt-xy/access_account/plus/upgrade | "Shopify" | 2026-09-30T08:15:36.604Z
- the step's files: `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/422.aria.yaml`, `observed-sh@febbf6c98:raw/runs/20260930T045741Z-sweep-trial2/steps/422.html`, `observed-sh@febbf6c98:derived/step-text-from-html/20260930T045741Z-sweep-trial2/422.html.txt`
- quote: Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments
- in context: Skip to content [initials: MS] [alt: My Store] My Store [heading: Subscribe to Plus] Plus For fast growing, high-volume businesses Starting at $2,300 USD/month ⟪Shopify Payments card rates are unavailable Shopify Payments is not available on your store. 0.2% third-party transaction fees apply if not using Shopify Payments⟫ Shopify Plus plan features Priority 24/7 support Get top-tier technical support by phone, chat, or email B2B on Shopify Sell wholesale and direct, integrated in one admin and store Custom checkout Personalize your checkout with unique discounts, shipping rates, and payment options through Shopify Functions Submit [heading: Business information] [label: Legal business name] [details: The business name that appears on your legal paperwork, such as…

### Q3-SH-017

**Cited at:** section 1, line 77; section 2, line 101

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-017
- bears_on: 4
- identifier: Uploading documents for Shopify Payments verification
- statement: Your Shopify Payments payouts might be placed on hold until your information and documents can be verified. If documentation is required, then an alert is sent to notify you and take you to the upload page where you can provide new information.
- cite_ids: Q3-SH-C024
- from: held

**Citation Q3-SH-C024:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | Uploading documents for Shopify Payments verification | 2026-10-18 | kind: stated | quote check: found (markup removed)
- quote: Your Shopify Payments payouts might be placed on hold until your information and documents can be verified. If documentation is required, then an alert is sent to notify you and take you to the upload page where you can provide new information.
- title: Setting up your Shopify Payments account
- the page opens: To get started with Shopify Payments, first check the list of supported countries to confirm availability in your region. After confirming your eligibility, you can activate the service and complete the verification process. Your Shopify Payments payouts might be placed on hold until two-step authentication is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your store currency bef…
- a note box: Staff permissions Only the store owner can activate or switch to Shopify Payments. Staff members can't switch to Shopify Payments.
- a note box: Note Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- headings: Setting up your Shopify Payments account
- in context: …sible is marked with a green check. Below it there are examples of bad photographs: One is too blurry, one is black-and-white, one has the left side of the document cropped out, and one has been altered to include a watermark. You can submit photo ID in PNG or JPEG format. Proof of address and business documents can additionally be in PDF format. Refer to your country's specific page to learn which types of documents are accepted in your region. ⟪Your Shopify Payments payouts might be placed on hold until your information and documents can be verified. If documentation is required, then an alert is sent to notify you and take you to the upload page where you can provide new information.⟫ If you receive a notification that your information wasn't verified, then you need to review the reasons provided on the upload page and take further action, such as uploading new documentation or updating your account information to match the uploaded documentation. When you upload documents for Shopify Payments verification or you try to update your Shopify Payments details, you might receive an error message indicating that you've reached the…  (matched markup removed)

### Q3-SH-K2268

**Cited at:** section 2, line 88; section 5, line 150; section 7, line 171

**The same record as Q2-SH-K2268,** whose card is in `Q2-shopify-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: You may not use the Payments Services if you are a resident of a sanctioned country or region embargoed by the United States, Canada, or the European Union, or are a person or entity blocked or denied by the governments of the United States, Canada or the European Union.
- scope: 

### Q3-SH-083

**Cited at:** section 2, line 90

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-083
- bears_on: 4
- identifier: Requirements for displaying your store in Shop, Note
- statement: The list of merchant requirements is subject to change without notice.
- cite_ids: Q3-SH-C118
- from: held

**Citation Q3-SH-C118:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shop/eligibility/requirements.md` | Requirements for displaying your store in Shop, Note | 2026-10-18 | kind: stated | quote check: found
- quote: The list of merchant requirements is subject to change without notice.
- title: Requirements for displaying your store in Shop
- the page opens: Note The list of merchant requirements is subject to change without notice. To have your store displayed in the Shop app and shop.com, there are certain requirements that your store must meet. These requirements ensure a consistent experience for merchants and customers. It's important to review and fulfill the following main criteria: * Compliance with Terms of Service and Acceptable Use Policy - Your store complies with Shopify's Terms of Service and Acceptable Use Policy. * Active Starter pla…
- a note box: Note The list of merchant requirements is subject to change without notice.
- headings: Requirements for displaying your store in Shop
- in context: # Requirements for displaying your store in Shop <aside class="note"><h4>Note</h4><p>⟪The list of merchant requirements is subject to change without notice.⟫</p> </aside> To have your store displayed in the Shop app and shop.com, there are certain requirements that your store must meet. These requirements ensure a consistent experience for merchants and customers. It's important to review and fulfill the following main criteria: * **Compliance with Terms of Service and Acceptable Use Policy** - Your store complies with Shopify's [Terms of Service](https://www.shopify.com/legal/terms) and [Acceptable …

### Q3-SH-015

**Cited at:** section 2, line 91; section 7, line 174

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-015
- bears_on: 1
- identifier: Uploading documents for Shopify Payments verification
- statement: Due to the sensitive nature of the personal information that's requested, Shopify can only accept documents that are uploaded through the secure banners in your Shopify admin. For your security and privacy, any documents sent through email or support chat are redacted and rendered unusable.
- cite_ids: Q3-SH-C017
- from: held

**Citation Q3-SH-C017:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/account-setup.md` | Uploading documents for Shopify Payments verification | 2026-10-18 | kind: stated | quote check: found
- quote: Due to the sensitive nature of the personal information that's requested, Shopify can only accept documents that are uploaded through the secure banners in your Shopify admin. For your security and privacy, any documents sent through email or support chat are redacted and rendered unusable.
- title: Setting up your Shopify Payments account
- the page opens: To get started with Shopify Payments, first check the list of supported countries to confirm availability in your region. After confirming your eligibility, you can activate the service and complete the verification process. Your Shopify Payments payouts might be placed on hold until two-step authentication is activated on your store. Two-step authentication helps to prevent security breaches that can lead to misdirected payouts or other financial loss. You need to choose your store currency bef…
- a note box: Staff permissions Only the store owner can activate or switch to Shopify Payments. Staff members can't switch to Shopify Payments.
- a note box: Note Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.
- headings: Setting up your Shopify Payments account > Uploading documents for Shopify Payments verification {#required-documentation}
- in context: …ents or communications are emailed, or made digitally available to the person listed as Account Owner of the store in your Shopify admin. ## Uploading documents for Shopify Payments verification {#required-documentation} <aside class="note"><h4>Note</h4><p>Once documentation is uploaded, it can take up to 24 hours to be reviewed. Your Shopify Payments account status will show the submission as "pending" until a response is received.</p> </aside> ⟪Due to the sensitive nature of the personal information that's requested, Shopify can only accept documents that are uploaded through the secure banners in your Shopify admin. For your security and privacy, any documents sent through email or support chat are redacted and rendered unusable.⟫ To complete the verification process, ensure that any documentation you submit meets the following requirements: * The documentation is photographed instead of scanned, copied, or screenshotted. Ensure photographs are in color and not grayscale. * For documents that are issued to you digitally, you must provide the original PDF without any alterations, and with all original pages included. * The documentation is clear enough to read, with all fo…

### Q3-SH-070

**Cited at:** section 2, line 94

**Record** (`studies/proposals/records/Q3/shopify/statements.tsv`):
- stmt_id: Q3-SH-070
- bears_on: 4
- identifier: Missed verification deadlines
- statement: Both pauses are temporary and are lifted automatically after you complete verification.
- scope: Shopify Payments accounts in Europe and the United Kingdom (UK)
- cite_ids: Q3-SH-C103
- from: held

**Citation Q3-SH-C103:** `observed-sh@c8b5fbee25966372a0475e6ed81f0b7760ac2921:structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/eu-verification.md` | Missed verification deadlines {#missed-deadline} | 2026-10-18 | kind: stated | quote check: found
- quote: Both pauses are temporary and are lifted automatically after you complete verification.
- title: Shopify Payments account verification updates in Europe and the United Kingdom
- the page opens: Verification requirements for Shopify Payments accounts in Europe and the United Kingdom (UK) are being updated throughout 2026. These updates align with local financial regulations, including requirements from the UK Financial Conduct Authority (FCA) and the Central Bank of Ireland (CBI). If your Shopify Payments account is affected, then you receive a notification in your Shopify admin and by email. If you receive a prompt to update or confirm your Shopify Payments account details, then comple…
- a note box: Staff permissions Only the store owner can view and complete verification requests for Shopify Payments accounts. Staff members don't have access to the verification request page.
- a note box: Note If you're based in Denmark, Italy, Poland, Spain, or Sweden, then you can optionally provide a national identification number to help complete verification.
- a note box: Caution Payments processed using payment providers other than Shopify Payments aren't affected.
- headings: Shopify Payments account verification updates in Europe and the United Kingdom > Missed verification deadlines {#missed-deadline}
- in context: …nual/payments/shopify-payments/supported-countries) for accepted document types. ## Missed verification deadlines {#missed-deadline} If you don't complete a verification request by the deadline displayed in your Shopify admin, then your payouts are temporarily paused until verification is complete. If your payouts are paused, then a second deadline might be displayed for when your ability to accept orders through Shopify Payments is also paused. ⟪Both pauses are temporary and are lifted automatically after you complete verification.⟫ Refer to your Shopify admin for the deadlines that apply to your account. ## Verification timeline for new accounts {#new-account-deadline} If you created your Shopify Payments account in or after June 2026, then you must complete verification to receive payouts and to continue processing payments. Your payouts are paused until you complete verification, and if verification isn't complete within 90 days of your first Shopify Payments order, then…
