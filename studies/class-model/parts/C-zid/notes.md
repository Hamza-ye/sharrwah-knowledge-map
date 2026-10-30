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
