# C-zid: notes

**What this part is.** Domain C's mapping part for Zid, onto the model so far: C-anchor and C-woocommerce. It runs in four batches: batch 1 maps CHK and ORD, batches 2 and 3 PAY and TAX, batch 4 SHP and RET and checks the whole part. `scope.tsv` gives Zid 36 concerns of domain C, and 6 concerns of other domains name C under `also` (ZD-C-017 A, ZD-C-019 D, ZD-C-033 E, ZD-C-035 A, ZD-C-103 D, ZD-C-111 A); batch 1 cites ZD-C-111 (ZD-S-0996). Each row is a reading unless it quotes a statement.

## Batch 1: CHK and ORD

**Concerns:** ZD-C-082, ZD-C-099, ZD-C-100, ZD-C-112, ZD-C-028, ZD-C-080, ZD-C-104. **Areas:** CHK (9 capabilities), ORD (14, plus 1 new). **What it holds:** 1 new capability (CM-ORD-015), 7 landings (5 into existing capabilities, 1 new, 1 moved), 24 cells (Zid's, one per capability of CHK and ORD), 64 evidence rows, 1 slot filler, no quality, no ruling (Zid has no Q1 matches or unclear candidates).

### How I cut, and why

- **ZD-C-082 Abandoned carts → CM-CHK-007, terms, strained.** Zid's Abandoned Carts / السلات المتروكة, with its Merchant API folder and permission إدارة السلات المتروكة, are Salla's by name. Its Zid Alerts statements (ZD-S-1018, ZD-S-1019) are recovery: D-zid cites them in domain D's CM-MKT-022 (Abandoned cart and order recovery), and by "One thing, one domain" they stay there, uncited here. That puts the concern's statements in another tree, so it is strained.
- **ZD-C-099 Checkout page settings → CM-CHK-001, terms.** Not CM-CHK-003: the anchor puts Shopify's checkout settings and Salla's Settings > Checkout in CM-CHK-001, and CM-CHK-003 is the checkout's look and branding, which no Zid statement shows. Zid's own folder is named API's > Checkout (ZD-S-0049), which is why I read إتمام الشراء as checkout. ZD-S-0049 is held under two concerns: ZD-C-099 (C), which I cite, and ZD-C-075 (E).
- **ZD-C-100 Order and product properties → CM-CHK-009, terms, strained.** Custom Fields / حقول مخصصة for orders matches Salla's custom fields for orders (/orders/custom-fields, إضافة حقول مخصصة للطلبات). The concern also holds product properties:
  - its plan line ZD-S-0963 is also cited as `core` in E's CM-CNT-002 by E-zid. I cite it as `core` here too, because it is this concern's own plan line and names orders, and E-anchor's Salla cell for CM-CNT-002 left Salla's order custom fields out of CM-CNT-002 (they are in CM-CHK-009). E-zid's notes expected that the merge would flag this. **For the coordinator:** one of the two domains should hold ZD-S-0963. By how the anchor cut Salla's, I read that as C for the orders side.
  - its product hold ZD-S-0965 is `core` in B's CM-INV-008 (B-zid) and `shows` here in CM-CHK-002;
  - its product API **ZD-S-0964 (List Product Settings) is uncited in every part.** It shows products, not orders, so I don't cite it in CM-CHK-009. B's CM-CAT-001 or E's CM-CNT-002 could take it. That is for the coordinator.
- **ZD-C-104 Working hours → CM-ORD-010, role, strained.** Zid's official working hours do the job of Salla's Ordering hours. Zid never says the hours govern when orders are received, so this is a join on role. Its one statement (ZD-S-0970) also covers closing the store temporarily, which A-zid cites as `core` in A's CM-ACC-007. I cite it as `core` here for the working hours, so the merge will flag it in two domains. The statement holds two things, so it bears on both.
- **ZD-C-080 Orders → CM-ORD-001, terms.** It is the parent, because the concern holds the orders as a whole. Its statements are spread across the children: editing (002), statuses (003), drafts (005), tags (011) and notes (013). Its Bulk Export Orders entry (ZD-I-0263) is in G's CM-MIG-001. That is an inventory entry, not a statement, so I kept the fit `clean` and said so in the reading.
- **ZD-C-028 Order payment status → new CM-ORD-015.** I searched every domain (`caps`: payment status; حالة الدفع; financial status; paid; unpaid). CM-ORD-003 holds an order's stages, and CM-PAY-020 holds its payment transactions. Zid gives the paid or unpaid state its own webhook topic, separate from order.status.update, and its own plan lines under Payments. That is a place of its own, by the dry-run convention. **For the back-fill:** Salla's order.payment.updated (SA-S-1583) and Shopify's orders/paid (SH-I-0535) are cited in CM-ORD-001. They may show this capability, and WooCommerce's statuses Pending payment and Failed (CM-ORD-003) may as well.
- **ZD-C-112 Zid Voice → moved:D.** It is abandoned cart recovery by a voice agent, which is D's CM-MKT-022. D-zid's cell there already cites ZD-S-0452 (`core`) and ZD-S-1069 (`shows`). Its other five statements (ZD-S-1067, 1068, 1070, 1071, 1072) are left to that cell. The coordinator may add them there. No statement names Zid's company as Zid Voice's maker, and Q1's `responsible` gap says the provider wasn't found.

### Services of Zid's company

- **Zid Pay.** Three cells cite statements of Zid Pay's concerns. Batch 2 places Zid Pay; I don't.
  - CM-CHK-001: ZD-S-0571, `shows` only.
  - CM-CHK-008: ZD-S-0362, `core`, a plan card of Zid's plan Rise.
  - CM-ORD-006: ZD-S-0580 and ZD-S-0374, `core`. Fraud Shield is on Zid's own product page Payments and in the Growth plan card.
  
  ZD-S-0589 defines Zid Pay as a service "على منصة تابعة لزد", and ZD-S-0592 names Zid. Whether those are maker statements for Zid Pay as a separate service is batch 2's reading. **For batch 2:** if you place Zid Pay as `own-service` and read Fraud Shield and Apple Pay as features of it, CM-ORD-006 and CM-CHK-008 may need the same placement. Tell the coordinator; don't rewrite these rows.
- **Zid Alerts and Zid Voice** are domain D's (above).

### Joins on role

- ZD-C-104 to Salla's Ordering hours (CM-ORD-010): ZD-S-0970 against SA-S-1738 and SA-S-1991.
- In cells, not landings:
  - CM-CHK-008 (Apple Pay "for faster checkout" read as an express or wallet checkout);
  - CM-ORD-006 (Fraud Shield read as the platform's fraud protection);
  - CM-ORD-010 (above).

### Homonyms kept apart

- **ملخص الطلب / Order Summary.** Salla prints its order summary (CM-ORD-009). Zid's is a document it issues and emails in place of an invoice (ZD-S-0823), with no statement saying it is printed. So Zid's CM-ORD-009 is `none-held`, and ZD-S-0823 is cited in CM-ORD-008. Orders Summary / ملخص الطلبات (ZD-I-0261) isn't defined and isn't cited.
- **Validate Order Request** (ZD-S-0004) isn't CM-CHK-005's app-written validation. No statement says what it validates.
- **Bundle (حزمة)**: Zid's bundle offers (ZD-C-089, domain B) aren't CM-CHK-006's cart transform.
- **Tags**: Zid's Order Tags are added by the merchant. They aren't Salla's Auto tags, although they share CM-ORD-011.

### Strained fits

ZD-C-082, ZD-C-100 and ZD-C-104 are strained (above).

### Gaps

- ZD-C-082/responsible and ZD-C-082/reason. Neither changes what CM-CHK-007 claims.
- ZD-C-099/decides, observation needed: which options the checkout page holds, beyond Zid Assurance (ZD-S-0996), isn't stated.
- ZD-C-104/decides and ZD-C-104/boundary: no plan, permission or API is held for working hours.
- ZD-C-112/decides and ZD-C-112/responsible: Zid Voice's price beyond the free calls, and its provider.
- CM-ORD-002: which plans have Unlimited Order Editing, and what limit the others have, isn't stated.
- CM-ORD-003: what a custom order status is isn't stated.
- **The `third_` scopes** aren't cited: third_order_read, third_order_write, third_create_order (in ZD-S-0908's text) and third_abandoned_carts_read (ZD-I-0092, ZD-I-0093, ZD-I-0098). No statement says what they are. ZD-S-0908 is cited for its endpoint, POST /v1/managers/store/drafts.
- **For domain D:** the abandoned-cart measures among Zid's plan lines aren't cited by D-zid's CM-ANL-001. They are ZD-I-0277, ZD-I-0283, ZD-I-0289, ZD-I-0290, ZD-I-0299, ZD-I-0305 and ZD-I-0306, all in ZD-C-082. They are measures, so I left them to analytics rather than CM-CHK-007.

### What later batches need from this one

- **Batch 2 (PAY):** read "Services of Zid's company" above. ZD-S-0571, ZD-S-0362, ZD-S-0580 and ZD-S-0374 are already cited in CHK and ORD. CM-ORD-015 (payment status) sits beside CM-PAY-020. Its cell cites only ZD-C-028.
- **Batch 3 (TAX):** CM-ORD-008's Zid cell cites the five statements of ZD-C-052 (Invoice settings). Batch 3 lands ZD-C-052, most likely in CM-ORD-008 by the terms اعدادات الفاتورة / Invoice settings. The slot filler Ministry of Commerce (ZD-S-0824) is already written. ZD-C-054 (credit notes) is cited as `shows` in CM-ORD-002 (ZD-S-1007) and CM-ORD-004 (ZD-S-0833, ZD-S-1007).
- **Batch 4 (SHP, RET):** ZD-S-1010 (the carrier sets جاري التوصيل) and ZD-S-1011 (linked carriers told an order is ready) are cited in CM-ORD-003 as `outside` and `shows`. ZD-S-0852 (Add Order Comment, ZD-C-061) is cited as `core` in CM-ORD-013. CM-ORD-009's parent is CM-SHP-001. Its Zid cell is `none-held`, and Zid's shipping labels and papers (ZD-I-0188, ZD-I-0204, ZD-I-0220) are left to SHP.

### What the checker flagged, and answers

The batch check printed 0 problems and 5 flags:
- **cells.tsv line 3 (CM-CHK-002): `core` rests only on boundary statements.** Get Cart is an operation in Zid's own API folder API's > Checkout. By the dry-run convention, the platform's own API for its own feature is `core`. No admin place for live carts is held.
- **Lines 5, 6, 17 and 19 (CM-CHK-004, CM-CHK-005, CM-ORD-007, CM-ORD-009): `none-held` with matching statements.** Each cell's reading names the hits and why they aren't the capability. The matches are generic words (إضافة, التحقق, حد أدنى, طباعة, print, assign), or another capability's statements: invoices in CM-ORD-008, shipping labels in SHP, campaign attribution in domain D.
- **Flags the merge will raise (C and another domain both `core` on one statement):**
  - ZD-S-0963: E's CM-CNT-002 and C's CM-CHK-009;
  - ZD-S-0970: A's CM-ACC-007 and C's CM-ORD-010.
  
  Both are answered above.

## Batch 2: PAY, first half

**Concerns:** ZD-C-001 to ZD-C-012. **Area:** PAY (32 capabilities, no new one). **What it holds:** 12 landings, all into existing capabilities (7 by terms, 5 by definition, none on role), 32 cells (Zid's, one per capability of PAY: 21 `statements`, 11 `none-held`), 169 evidence rows, 9 qualities, 6 slot fillers, no ruling (Zid has no Q1 matches or unclear candidates). I wrote every PAY cell, so several cite the statements of concerns that batch 3 lands (ZD-C-013 to ZD-C-016, ZD-C-023, ZD-C-037) or that a later batch lands (ZD-C-063). Batch 3 adds to those cells. Each row is a reading unless it quotes a statement.

### How I landed them, and why

- **ZD-C-001 Zid Pay activation → CM-PAY-003, definition.** The requirements go to the payment gateway, which approves the account, and a published product is needed before the request. Those are the checks before a store takes payments through the platform's service. The concern's plan line and contract are cited in CM-PAY-002, the parent.
- **ZD-C-002 Transactions and refunds → CM-PAY-020, terms.** العمليات is Salla's Transactions, and refunding a transaction is acting on it, as Salla's endpoint does. **For batch 4:** refunds to the buyer are also CM-RET-002's. If you cite ZD-S-0538 to ZD-S-0541 or ZD-I-0521 there, ZD-C-002's fit becomes strained (the RET tree): tell the coordinator.
- **ZD-C-003 Deposits and account statement → CM-PAY-005, definition**, and **ZD-C-004 Bank accounts → CM-PAY-005, definition.** The balance is deposited to the bank account on a schedule, and the bank account is the one that receives the deposits.
- **ZD-C-005 Payment networks → CM-PAY-002, terms, strained.** Its mada, Visa and Mastercard are Salla Payments' plan lines. Its Apple Pay is in CM-PAY-012 and its KNET in CM-PAY-017, both in the same tree. It is strained because batch 1 cites ZD-S-0362 in CM-CHK-008 and ZD-S-0571 in CM-CHK-001.
- **ZD-C-006 Transaction fees → CM-PAY-007, terms.**
- **ZD-C-007 Chargebacks, fraud and held funds → CM-PAY-002, terms, strained.** It is coarser than the capabilities: chargebacks are CM-PAY-009 and reserves and holds CM-PAY-006, so it lands in their common parent. I cite ZD-S-0581 in CM-PAY-002 (suspension of the service), so that the landing's cell cites the concern. It is strained because batch 1 cites its Fraud Shield (ZD-S-0580, ZD-S-0374) in CM-ORD-006. Fraud Shield isn't CM-PAY-010: no statement says it covers chargebacks.
- **ZD-C-008 Payment links → CM-PAY-032, terms** (روابط الدفع, the plural of Salla's رابط الدفع).
- **ZD-C-009 Providers behind Zid Pay → CM-PAY-004, definition.**
- **ZD-C-010 Zid Payments Open APIs → CM-PAY-004, definition, strained.** I read the PSPs as processors behind Zid's own service, Zid Payments, which is the English name of Zid's own gateway in the Rise plan line (ZD-S-0361). Q1 also put the Open APIs model (ZD-S-0595) in ZD-C-009. Two things don't fit:
  - the Open APIs are a provider interface, cited as `extension-point`, and the anchor's CM-PAY-004 cells show none;
  - the merchant_linked flow (ZD-S-0534, ZD-S-0535) onboards the merchant at the provider, with the merchant's own keys, which is how CM-PAY-011's gateways connect.

  **For the reviewer:** split out a payment provider interface, or move it to CM-PAY-011 beside Shopify's Payments Apps API.
- **ZD-C-011 Other payment gateways → CM-PAY-011, terms** (بوابات الدفع الأُخرى, Salla's بوابات الدفع الأخرى).
- **ZD-C-012 Store payment methods → CM-PAY-001, terms** (طرق الدفع / Payment methods).

### Zid Pay, a service of Zid's company

- **The maker statement (a reading).** I read **ZD-S-0533** as Zid Pay's maker statement: "تمثل الشروط والأحكام المذكورة أدناه العقد المبرم بين مستخدمي زد باي وشركة زد". It names the company as the party that contracts the service with its users. ZD-S-0589 ("على منصة تابعة لزد") names Zid only as the owner of the platform the service runs on, so I take it as support, not as the maker statement on its own. ZD-S-0692 (ZD-C-023) also calls Zid Pay "منصة زد لحلول الدفع". It is cited only in CM-PAY-026, so that batch 3's ZD-C-023 isn't strained by a support row.
- **Two placements.** Zid Pay is both:
  - `core`, where a statement names Zid's own admin (المدفوعات, إدارة زد باي, العمليات, كشف الحساب), its plan lines, its staff permissions (manage.zidpay.setting, list.zidpay.transactions, refund.zidpay.transactions, list.zidpay.deposits) or its own Merchant API;
  - `own-service`, where a statement of Zid Pay's terms names Zid Pay or Zid as doing the thing: reviewing deposits, deducting fees, holding funds, executing transactions.

  By the coordinator's rule, the maker statement counts for each Zid Pay feature that a cell's own statements show. So `own-service` is in CM-PAY-002, 005, 006, 007 and 020, each resting on that cell's statements, with ZD-S-0533 named in the reading. This matches the anchor's Shopify Payments (`core`, with `own-service` from its terms' supplier entities).
- **Batch 1's rows still hold, in my reading. No correction is needed.**
  - CM-CHK-008 (ZD-S-0362) and CM-ORD-006 (ZD-S-0374, ZD-S-0580) are `core` on Zid's own plan cards and its own Payments product page. None of the three names Zid Pay. Fraud Shield is tied to Zid Pay only by Q1's placement of it in ZD-C-007, which is not a statement. If the coordinator reads Fraud Shield or Apple Pay as features of Zid Pay, `own-service` could be added on the same keys, with ZD-S-0533 as the maker statement.
  - CM-CHK-001's ZD-S-0571 names Zid Pay, but it is a reason statement about the payment step. `shows` stays right: it places nothing about the checkout settings. I also cite it as `shows` in CM-PAY-002.
- **Zid's other services** in this batch's cells:
  - Zid Financing: `own-service` on ZD-S-0692, "خدمة إلكترونية تقدمها زد", a maker statement in its own words;
  - COD collection under direct shipping, ZD-S-0641 and ZD-S-0636: Zid names itself as collecting. I placed them `core`, because no statement makes COD collection a separate service of Zid's company. Batch 3 may revisit this with ZD-C-015.

### Joins on role

None in landings. In cells, as readings:
- CM-PAY-016: Zid's Starter card groups bank transfer and COD as "Basic payment methods", read as the anchor's manual payment methods;
- CM-PAY-017: KNET inside Zid Pay, read as a local method through the platform's own service, as Salla's KNET through مدفوعات سلة.

### Homonyms and false hits kept apart

- **الحسابات البنكية.** Zid's (ZD-C-004) is the account that receives Zid Pay deposits (CM-PAY-005). Salla's إدارة الحسابات البنكية is the accounts shown for bank transfer (CM-PAY-030). Q1's split of ZD-C-004 says Zid's accounts serve both, but no statement of it says so, so ZD-C-004 isn't cited in CM-PAY-030.
- **رصيد التاجر** in Zid Pay (ZD-S-0555) is the payout balance (CM-PAY-005), not the merchant wallet (A's CM-PLN-006).
- **Plan "cards"** (ZD-I-03xx) are plan descriptions, not payment cards (the CM-PAY-024 hits).
- **ZD-S-0625** matched "بي بال" across "تابي بالدفع". It isn't PayPal.
- **The Arabic احتياطي** is read as reserve (CM-PAY-006).

### Strained fits

- ZD-C-005: CHK tree, through batch 1's citations.
- ZD-C-007: ORD tree, through batch 1's CM-ORD-006, and landed in the parent.
- ZD-C-010: a provider interface, beside CM-PAY-011's connection flow.

### Statements of other domains cited

- **Concerns that name C under `also`:** ZD-C-035/boundary/ZD-S-0757, `shows` in CM-PAY-003 (A's `core` in CM-ACC-004).
- **Concerns that don't name C, each the only Zid statement on its point:**
  - ZD-C-038/decides/ZD-S-0775 (Nafath for Zid Pay's activation; A's `core` in CM-TRU-002): `shows` in CM-PAY-003;
  - ZD-C-108/where/ZD-S-0978 (the POS payment device; E's `core` in CM-POS-002): `shows` in CM-PAY-021;
  - ZD-I-0440 and ZD-I-0443 (ZD-C-070, F: the App Market categories for accounting and ERP): `extension-point` in CM-PAY-028.
- **Read, not cited:**
  - ZD-C-017 (Zid Wallet, A): CM-PAY-023's reading names it, and leaves it to CM-PLN-006;
  - ZD-C-111 (Zid Assurance, A): CM-PAY-010's reading. Its terms aren't held here.

### Gaps

- **CM-PAY-004:** the providers behind Zid Pay aren't named, and their licences aren't held (ZD-C-009/responsible, searched, not found). The agreement between Zid and a PSP on the Open APIs needs observation (ZD-C-010/responsible). So no slot filler is held.
- **CM-PAY-005:** which licensed entity or bank holds collected funds before deposit needs observation (ZD-C-003/responsible). No API is held for deposits or bank accounts (ZD-C-003/boundary, ZD-C-004/boundary).
- **CM-PAY-006 and CM-PAY-009:** no admin place, permission or API for disputes or holds (ZD-C-007/boundary). So CM-PAY-009's cell is `shows` only, and is derived `not-stated`.
- **CM-PAY-007:** no API exposes the fees (ZD-C-006/boundary).
- **CM-PAY-021:** who processes card payments at Zid's POS isn't stated. So the cell is `shows` only.
- **CM-PAY-026:** the financing party isn't named.
- **CM-PAY-032:** whether the link is sent to the buyer isn't stated. Its responsible placement is 'stated only in general terms'.

### For batch 3 (the rest of PAY, then TAX)

- **Cells already written** that cite your concerns' statements, so add to them, and don't write them again:
  - CM-PAY-015 (ZD-C-013);
  - CM-PAY-029 (ZD-C-014, ZD-C-015);
  - CM-PAY-030 (ZD-C-016);
  - CM-PAY-026 (ZD-C-023);
  - CM-PAY-006 (ZD-C-037's ZD-S-0772);
  - CM-PAY-002 (the cell where Shopify's prohibited businesses, SH-C-173, sit; ZD-C-037 most likely lands there);
  - CM-PAY-019 (ZD-C-063, a later batch's concern).

  Slot fillers already written: Tabby, MIS pay (CM-PAY-015). Not yet written: Tamara, Emkan, Madfu.
- **Concerns with no cell of their own.** ZD-C-018 (wallet deduction from Zid Pay) and ZD-C-024 (Mazeed collections and dues) have no cell that fits them cleanly:
  - ZD-C-018 moves part of the Zid Pay balance to the wallet (ZD-S-0663, ZD-S-0664). CM-PAY-005 (payouts) or a new capability are the candidates. It isn't CM-PAY-031 (an app's partner settlement). Read CM-PAY-023's reading;
  - ZD-C-024's collections, payout schedule and holds (ZD-S-0704 to ZD-S-0709) bear on CM-PAY-005 and CM-PAY-006. The cells don't cite them yet.
- **TAX:** CM-PAY-028's reading names ZD-S-0825 (ZD-C-052) as a hit not cited, because it is about invoices (CM-ORD-008). Fees in PAY are quoted "exclude VAT" (ZD-S-0575, ZD-S-0574), and the merchant mustn't charge VAT to the cardholder (ZD-S-0579, `shows` in CM-PAY-007). TAX may cite ZD-S-0579.
- **Strained fits that may follow:** ZD-S-0636 and ZD-S-0641 are cited in CM-PAY-029. If batch 4 cites them in SHP (Zid Ship), ZD-C-015's fit is strained.

### What the checker flagged, and answers

The batch check printed 0 problems and 33 flags. Two problems on the first run were mine, and I fixed them:
- ZD-C-007 landed in CM-PAY-002, whose cell cited none of its statements. I added ZD-S-0581.
- A term in CM-PAY-028 wasn't in a cited statement. I removed it.

Answers to the flags:
- **`own-service`, "does the statement name zid's company as the maker or provider?"** (ZD-S-0533, ZD-S-0589, and the Zid Pay rows in CM-PAY-005, 006, 007 and 020):
  - ZD-S-0533 names شركة زد as Zid Pay's contracting party, and is the maker statement (above);
  - the other rows rest on statements naming Zid Pay (or زد, ZD-S-0543) as doing the thing, with ZD-S-0533 counted for each feature, as the coordinator's rule allows;
  - for Zid Financing, ZD-S-0692 names Zid as the provider ("تقدمها زد"), and ZD-S-0699 rests on it.
- **Another domain's statement:** ZD-S-0775, ZD-S-0978, ZD-I-0440 and ZD-I-0443, answered above, each cited where it is the only Zid evidence. None supports `core` or `own-service` here.
- **More than one tree:** ZD-S-0362 (CM-CHK-008, CM-PAY-012) and ZD-S-0571 (CM-CHK-001, CM-PAY-002). They bear on both, and ZD-C-005 is marked strained for it.
- **`none-held` with matching statements** (CM-PAY-010, 013, 014, 022, 023, 024, 025, 031). Each cell's reading names the hits and why they aren't the capability.
- **Batch 1's flags reprinted** (cells.tsv lines 3, 5, 6, 17, 19: CM-CHK-002, CHK-004, CHK-005, ORD-007, ORD-009) are batch 1's, answered in its section. The checker printed no problem on batch 1's rows.

### The coordinator, after batch 1

- **ZD-C-112 is landed in D,** in CM-MKT-022, through D-amend (scope.tsv now gives it D, with C and F under `also`).
- **ZD-S-0963** (Custom Fields: extra information "to products or orders") names two things, so it is `core` in C's CM-CHK-009 for orders and in E's CM-CNT-002 for products, as a statement naming several things counts in each. **ZD-S-0970** (working hours, and closing the store entirely for a time) likewise counts in C's CM-ORD-010 and A's CM-ACC-007.
- **ZD-S-0964,** the List Product Settings operation, stays uncited: nothing held says what a product setting is, and its thing is a product's, not C's. It is left as a lead for the final review.
- **CM-ORD-015** needs Shopify's, Salla's and WooCommerce's cells: C-backfill-zid writes them after the part's last batch.

### The coordinator, after batch 2

- **Zid Pay's maker statement is ZD-S-0533:** Zid Pay's terms are "العقد المبرم بين مستخدمي زد باي وشركة زد", the contract between Zid Pay's users and Zid's company, which names the company as the service's provider (the brief's "Maker evidence"). It counts for each feature of Zid Pay that a cell's own statements show. Batch 1's cells (CM-CHK-008's Apple Pay, CM-ORD-006's Fraud Shield) stand as they are: none of their statements names Zid Pay.

## Batch 3: PAY, second half, and TAX

**Concerns:** ZD-C-013, ZD-C-014, ZD-C-015, ZD-C-016, ZD-C-018, ZD-C-023, ZD-C-024, ZD-C-037 (PAY), ZD-C-051, ZD-C-052, ZD-C-053, ZD-C-054 (TAX). **Areas:** PAY (32 capabilities, no new one) and TAX (9, no new one). **What it holds:** 12 landings: 11 into existing capabilities (8 by terms, 2 by definition, 1 on role) and 1 moved (ZD-C-018 to A); no new capability. 9 cells, Zid's for every TAX capability (5 `statements`, 4 `none-held`), 43 evidence rows (25 added to batch 1's and 2's cells: 19 in PAY, 6 in CM-ORD-008; 18 in TAX), 8 slot fillers, 1 quality, no ruling (Zid has no Q1 matches or unclear candidates). Each row is a reading unless it quotes a statement.

TAX cells: `statements` for CM-TAX-001, 003, 004, 007 and 008; `none-held` for CM-TAX-002, 005, 006 and 009.

### How I landed them, and why

- **ZD-C-013 Instalments → CM-PAY-015, terms.** خدمات التقسيط / الدفع لاحقاً, with Tabby and Tamara, is Salla's وسائل الدفع الآجلة and its plan line الدفع بالتقسيط عبر تابي وتمارا. Batch 2's cell already cites all eight statements. I added the slot fillers Tamara, Madfu and Emkan.
- **ZD-C-014 COD option and ZD-C-015 COD collection → CM-PAY-029, terms.** The cell holds both arrangements, the merchant's own carrier (a third party's service, ZD-S-0635) and Zid's collection under direct shipping (ZD-S-0641, ZD-S-0636), as Salla's has its own carrier and بوليصات سلة. I added ZD-C-014's payment_method value (ZD-S-0634) as `shows`. Batch 2 placed COD collection `core`, because no statement makes it a separate service of Zid's company. I keep that: ZD-S-0641 names زد as collecting, under Zid's own plan line Cash on Delivery Collection (ZD-S-0637), and no maker statement for Zid Ship is held among these concerns.
- **ZD-C-016 Bank transfer → CM-PAY-030, terms.** Already fully cited by batch 2.
- **ZD-C-018 Wallet deduction from Zid Pay → moved:A.** It tops up Zid's merchant wallet from the Zid Pay balance (ZD-S-0663, ZD-S-0664), reached from إدارة المحفظة (ZD-S-0660), so that the wallet holds a balance for expenses such as shipping labels (ZD-S-0665). That is a way of topping up the wallet, domain A's CM-PLN-006 ("topped up, spent on the platform's services and withdrawn"). It isn't CM-PAY-005: nothing goes to the bank account. It isn't CM-PAY-031 either: no app partner is settled. None of its six statements is cited in C. **For the coordinator:** scope.tsv gives it C with no `also`, so A-amend, or A-zid's cell for CM-PLN-006, would take ZD-S-0660 to ZD-S-0665. Salla's SA-S-0091 (no move from the e-payments balance to the store balance) is already cited there, the opposite rule.
- **ZD-C-023 Zid Financing → CM-PAY-026, definition.** Financing repaid from a share of the store's sales: Zid's repayments come from Zid Pay sales (ZD-S-0692, ZD-S-0699), and Salla's capital takes 25% of net sales from each payment (SA-S-0111). Batch 2's cell already cites all ten statements.
- **ZD-C-024 Mazeed collections → CM-PAY-005, role, strained.** I read it as a payout: Zid's company collects the Mazeed orders' payments and pays the merchant's bank account on a schedule, with a minimum (ZD-S-0704, ZD-S-0706, ZD-S-0707). What doesn't fit: CM-PAY-005 is the payment service's balance, and Mazeed's money comes through Mazeed's own gateway (ZD-S-0703), not Zid Pay. No other platform shows a marketplace's collections, and Zid gives them no place of their own: they are reached from the Mazeed page (ZD-S-0702). So by the dry-run convention I add no capability. It is strained because E-zid cites ZD-S-0702 (`core`) and ZD-S-0703 (`shows`) in E's CM-CHN-002. Its holds (ZD-S-0708, ZD-S-0709) are cited `own-service` in CM-PAY-006, because they name شركة زد, and Mazeed is a service of Zid's company, as E-zid reads ZD-S-0989. **For the reviewer:** split out the marketplace's collections and payouts, or move them to CM-CHN-002.
  - **Reading:** ZD-S-0706 (weekly, every Tuesday, no minimum), ZD-S-0707 (monthly, with sales of 500 riyals or more) and ZD-S-0704 (on the 30th of each month, at least 500 riyals) don't agree. I cite all three and don't reconcile them.
  - **Not placed:** the share Zid takes from each Mazeed purchase by sector (ZD-S-0705) is a marketplace commission, which no capability holds. I cite it `shows` in CM-PAY-005, as an amount deducted before the payout. It is a lead for E's CM-CHN-002 or A's CM-PLN-003.
  - **Uncited:** its reason ZD-S-0712 (Q1's note: refund costs shared between the merchant and Mazeed). It isn't about payouts. **For batch 4:** RET may take it.
- **ZD-C-037 Zid Pay's prohibited activities → CM-PAY-002, terms, strained.** الأنشطة المحظورة أو المقيدة is Shopify's Prohibited and Restricted Businesses for Shopify Payments (SH-C-173), which the anchor lands in CM-PAY-002. Its scope.tsv row names A under `also`.
  - **The citations:** ZD-S-0765 is `own-service` (the activities "محظورة من زد باي", with Zid Pay's maker statement ZD-S-0533). The lists and the update rule (ZD-S-0766, 0767, 0768, 0770, 0771, 0773) are `shows`. ZD-S-0769 (deposits stopped for large sums from abroad) is `shows` in CM-PAY-006, since it names no actor.
  - **Why it is strained:** A-zid cites nine of its statements in A's CM-TRU-009 (Acceptable use and enforcement), with ZD-S-0765, 0769, 0770 and 0772 as `core`. CM-PAY-006 is also another tree of PAY.
  - **For the coordinator:** by One thing, one domain, I read Zid Pay's own prohibited list as CM-PAY-002's, where the anchor put Shopify's. A's CM-TRU-009 is the platform's rules for what merchants do with the platform as a whole, and A-zid's own reading says none is held for Zid. One of the two domains should hold these statements. A-zid's three slot fillers on CM-TRU-009 repeat two of mine on CM-PAY-002: the sanctions lists, ZD-S-0767, and the Central Bank's approval, ZD-S-0773.
- **ZD-C-051 Tax settings → CM-TAX-001, terms.** اعدادات الضرائب / ضريبة القيمة المضافة is Salla's إعدادات الضريبة / ضريبة القيمة المضافة. Its country form (ZD-S-0817) holds the VAT rate, so it is `core` in CM-TAX-001. The same form holds the tax number and VAT certificate, so it is also `core` in CM-TAX-003, the child of CM-TAX-001.
- **ZD-C-052 Invoice settings → CM-ORD-008, terms**, as batch 1 expected. Its five statements are batch 1's cell.
- **ZD-C-053 ZATCA e-invoicing → CM-TAX-007, terms.** Its terms are الربط مع منصة فاتورة and هيئة الزكاة والضريبة والجمارك. The slot filler is ZATCA (ZD-S-0829). The merchant's activation code made in Fatoora (ZD-S-0830) is `shows`: it is the merchant's step at the authority, while Salla's statement has the code grant Salla authority (`core`).
- **ZD-C-054 Credit notes → CM-ORD-008, definition, strained.** Zid calls its credit and debit notes "إشعارات فواتير", issued and sent when an order is edited or cancelled (ZD-S-1007), with the invoice left unchanged by ZATCA's rules (ZD-S-1009). I read them as documents on the order's invoice. What doesn't fit: a note against an invoice isn't the invoice. I add no capability for three reasons: no other platform's cell shows credit notes (`caps`: credit note; debit note; إشعار دائن; إشعارات الدائن; refund receipt), Zid's List Order Credit Notes is one operation in the Orders folder rather than an API group, and Q1 found no plan line for it (ZD-C-054/decides). Batch 1 cites ZD-S-0833 and ZD-S-1007 as `shows` in CM-ORD-002 and CM-ORD-004, in the same tree. I added six rows to CM-ORD-008. The API operation, its endpoint and scope, and the notes issued on edit are `core`. The rule on VAT-registered stores (ZD-S-1008) and ZATCA's rule (ZD-S-1009) are `shows`, and ZATCA is a slot filler.

### TAX cells

- **CM-TAX-001:** core on the tax settings page, the country form, the plan lines Invoice & Tax Settings and Tax-Applicable Countries, the Growth card Calculate and display VAT, the staff permission manage.store.vat.settings (ZD-I-0488, placed inventory) and the API operation that returns the VAT settings (ZD-S-0819). That operation sits under `/third-party/` with the scope third_vat_read. Batch 1 left the `third_` scopes uncited because no statement says what they are. This statement does say what the operation returns, and nothing says apps do the work, so it is `core`.
- **CM-TAX-002, none-held:** the VAT is worked out from the merchant's rates. That is how the anchor treated Salla, whose "show and calculate" plan line is in CM-TAX-001 and whose CM-TAX-002 is none-held.
- **CM-TAX-004:** the App Market category الضريبة والزكاة (ZD-I-0441, ZD-C-070, domain F, not naming C), `extension-point`, as WooCommerce's Marketplace category is. It is the only Zid evidence, which is why it is cited here, as batch 2 cited ZD-I-0440 in CM-PAY-028.
- **CM-TAX-008:** ZD-S-0842 (ZD-C-060, Zid Ship, domain C): under Global Shipping, duties the customer refuses are charged to the merchant from the Zid wallet. It is `core`, as Salla's customs fees settled from its wallet (SA-S-5075). **For batch 4:** this puts a ZD-C-060 statement in the TAX tree. If you land ZD-C-060 in SHP, its fit is strained.
- **CM-TAX-005, 006 and 009, none-held:** each reading names its hits.

### Slot fillers and the quality

- **Slot fillers:**
  - CM-PAY-015: Tamara, Madfu and Emkan;
  - CM-PAY-002: the sanctions lists and the Central Bank's approval (ZD-C-037);
  - CM-TAX-003: اللائحة الضريبية للمتاجر الإلكترونية (Saudi stores);
  - CM-TAX-007: ZATCA;
  - CM-ORD-008: ZATCA's requirements (ZD-S-1009).
- **The quality** is on CM-PAY-005: Mazeed's transfer day, minimum age and minimum amount (ZD-S-0704).

### Joins on role

ZD-C-024 to CM-PAY-005: ZD-S-0704 and ZD-S-0706 against Salla's SA-S-0076 and Shopify's SH-S-0342.

### Homonyms and false hits kept apart

- **المحفظة:** the wallet that ZD-C-018 tops up, and that receives COD and pays customs (ZD-S-0636, ZD-S-0842), is A's CM-PLN-006. It isn't CM-PAY-023.
- **الإقرار** in the tax settings (ZD-S-0818) is the merchant's declaration, not a tax return (CM-TAX-006).
- **الرقم الضريبي:** the store's own number (ZD-S-0817, CM-TAX-003), Zid's own numbers (ZD-S-0731, ZD-S-0738, domain A), and no buyer's VAT number (CM-TAX-005).
- **فواتير ضريبية B2B** (ZD-S-0711) are the merchant's invoices to Zid for Mazeed's dues, not VAT invoices to business buyers (CM-TAX-005).

### Strained fits

ZD-C-024 (E's CM-CHN-002; and not the payment service), ZD-C-037 (A's CM-TRU-009; CM-PAY-006), and ZD-C-054 (a note isn't the invoice).

### Gaps

- ZD-C-013/reason: no stated reason for outside instalment providers. It changes nothing in CM-PAY-015.
- ZD-C-015/responsible, observation needed: who holds the COD amounts before the wallet. ZD-C-015/boundary: no API for COD collections. CM-PAY-029 claims no API.
- ZD-C-016/reason: searched, not found.
- ZD-C-023/responsible: the financing party isn't named, so no slot filler (as batch 2 said).
- ZD-C-037/responsible, observation needed: who screens against the sanctions lists. ZD-C-037/boundary: no API for screening.
- ZD-C-052/reason: searched, not found.
- ZD-C-053/responsible and ZD-C-054/responsible: stated only in general terms. ZD-C-054/decides: which plans include credit and debit notes isn't stated.
- CM-TAX-007: whether the Fatoora link is limited to a plan isn't stated. ZD-S-0827 says only that it is free.

### Problems on earlier batches' rows, for the coordinator

None of these makes a row wrong. Some readings and terms no longer name all of a cell's evidence:
- **CM-PAY-002's reading** (batch 2) ends "Batch 3 lands ZD-C-037". Its evidence now holds ZD-C-037's rows: one `own-service`, six `shows`. The reading could name them.
- **CM-PAY-005's reading** says ZD-C-018 "moves part of the Zid Pay balance to the wallet" and that ZD-C-024 may bear on it. ZD-C-018 is now moved:A, and ZD-C-024's rows (two `core`, one `own-service`, four `shows`) are in its evidence, unnamed in its reading. CM-PAY-006's reading likewise doesn't name ZD-S-0708, ZD-S-0709 or ZD-S-0769.
- **CM-PAY-023's reading** calls ZD-C-018 "which batch 3 lands". It is now moved:A.
- **CM-ORD-008's reading and terms** (batch 1) don't name ZD-C-054's six rows. Its terms could add إشعارات الدائن;List Order Credit Notes.

### What batch 4 needs

- ZD-C-060's ZD-S-0842 is cited in CM-TAX-008 (above).
- ZD-C-015's statements (ZD-S-0636, ZD-S-0640, ZD-S-0641, Zid Ship) are in CM-PAY-029. If you cite them in SHP, ZD-C-015's fit becomes strained.
- ZD-S-0712 (Mazeed refund costs) is uncited, a lead for RET.
- Batch 2's note on ZD-C-002 and CM-RET-002 still holds.

### What the checker flagged, and answers

The batch check printed **0 problems and 40 flags**. My flags:
- **`own-service`** on ZD-S-0765 (ZD-C-037), and on ZD-S-0704, ZD-S-0708 and ZD-S-0709 (ZD-C-024):
  - ZD-S-0765 rests on Zid Pay's maker statement ZD-S-0533, which counts for this feature: the activities "محظورة من زد باي";
  - the three ZD-C-024 statements each name شركة زد as transferring or holding the funds, a statement naming the company.
- **ZD-I-0441 is ZD-C-070's (F, not naming C):** answered in CM-TAX-004, the only Zid evidence on tax apps.
- **CM-TAX-002 and CM-TAX-005, none-held with matching statements:** each reading names the hits and why they aren't the capability. CM-TAX-002's count is large because the terms I searched include the bare ضريبة / الضرائب, which I searched to be sure nothing was missed.
- **Flags the merge will raise, where C and another domain are both `core` on one statement:**
  - ZD-S-0702: E's CM-CHN-002 and C's CM-PAY-005. The statement names the Mazeed page and the dues reached there, so it holds two things;
  - ZD-S-0765: A's CM-TRU-009 `core`, and C's CM-PAY-002 `own-service`. ZD-S-0769 and ZD-S-0772 are A's `core` and C's `shows` or `own-service`. Answered under ZD-C-037.

The other 33 flags are batch 1's and batch 2's rows, which they answered in their sections. The checker printed no problem on their rows.

### The coordinator, after batch 3

- **ZD-C-018,** the wallet deduction from Zid Pay, is moved to A and landed in CM-PLN-006, Zid's merchant wallet, in A-zid, where its statements are now cited; scope.tsv gives it A, naming C under `also`. CM-PAY-023's reading says so.
- **ZD-S-0702** (Mazeed's financial dues, reached at Dashboard > Sales platforms > Mazeed) is `core` in C's CM-PAY-005 and in E's CM-CHN-002, and neither cell rests on it alone: the merge's counted-twice flag goes to the final review with the other such flags.
- **The readings of CM-PAY-002, CM-PAY-005, CM-PAY-006 and CM-ORD-008** don't yet name batch 3's evidence. The coordinator brings them up to date after batch 4.
