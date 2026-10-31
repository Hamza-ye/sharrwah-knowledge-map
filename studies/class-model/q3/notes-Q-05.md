# Q3's check, batch Q-05: notes

Rows: km:PAY-01 to km:PAY-07, km:SHP-01 to km:SHP-06, km:RET-01 to km:RET-03 (16). The check file is `check-Q-05.tsv`, beside this one.

## Count by result

- covered: 10 (km:PAY-01, PAY-02, PAY-03, PAY-04, PAY-05, SHP-01, SHP-02, SHP-03, RET-01, RET-03)
- partly: 5
  - km:PAY-06 and km:SHP-06: the rest is beyond the class;
  - km:SHP-04, SHP-05 and RET-02: the rest is a candidate miss, not held.
- beyond the class: 1 (km:PAY-07)
- candidate miss, held: 0
- unclear: 0

## Rows that were hard to place

- **km:PAY-01, the provider's contract.** Authorize, capture, refund and void are in the cells (CM-PAY-020, CM-RET-002; Salla's Transactions endpoint, SA-S-0180, names refund, void and reverse). 3-D Secure has no capability of its own. Its one statement, BigCommerce's BC-S-0130, is cited in CM-PAY-022@bigcommerce, and its concern lands in CM-PAY-020. Shopify's SH-S-6071, a subscription billing attempt challenged under 3-D Secure, is cited in no cell; its concerns land in CM-API-003 and CM-SEL-001. Reading: 3-D Secure is a step in the transaction's flow, so it is detail of CM-PAY-020, not a miss.
- **km:PAY-03 and km:RET-03, and Decision 1.** Both are in the present tense and name neither the platforms nor Sharrwah, so they ask the class, and the cells answer them. Sharrwah's own side is already settled by Decision 1 and the decisions paired with it (25 October): each provider pays out and refunds, Sharrwah sends no payouts, and under C a provider's balance is read from the provider (S-01 register, S01-D3, S01-D11, S01-E2 and S01-E4). Reading: the rows only touch this in passing, so `founder:decided` is not among their answerers. The coordinator may add it if it reads them as asking about Sharrwah.
- **km:PAY-03, statements.** Statements are covered by Zid's account statement (كشف الحساب, ZD-S-0544, ZD-I-0527), which is cited in CM-PAY-005@zid. Searches for statements on Shopify, WooCommerce and BigCommerce found nothing.
- **km:PAY-04, cash-on-delivery fees.** Covered by CM-PAY-029@salla: cash on delivery per carrier, with its fee raised or lowered (SA-S-0126), and the threshold under which it isn't shown (SA-S-0125). Zid's ZD-S-0638 is a different fee: the one Zid itself charges for its cash-on-delivery service, not a fee the merchant sets for buyers.
- **km:PAY-06 and km:SHP-06, the target market.** The market's expectations and practices are the market's facts, so they go to S-04 and S-10, which haven't run. What each method or carrier needs from the platform is covered by the cells. Which market comes first is already decided (Yemen; 29 October, "Intent (standing)"). Reading: the rows touch that only in passing, so it isn't one of their answerers.
- **km:SHP-06, address systems.** Salla's setting that requires the Saudi national address (SA-S-5020, a requirement of the transport authority) sits in CM-CUS-008. S-02 binds the address form per market (S02-F8, S02-VP-69). No subject fills what that form holds in a given market. So `subject:none`, with the subject it would need named for Stage 3's list.
- **km:PAY-07.** Under C, who holds sellers' money is decided, held as a market's setting (26 October). Whether Sharrwah's own company runs payments or a balance, and the licences and partners that would need, is still open on the founder's list. Who may hold funds under a market's law belongs to S-06. No capability answers the row, since it asks about a market and about Sharrwah, so `cap_ids` is empty. CM-PAY-004 shows how the class places processors and licensed entities, for reference.
- **km:SHP-05, pick lists.** These are covered by Zid's plan line Export Order Fulfillment List (تصدير قائمة تجهيز الطلبات, ZD-I-0270), which is cited in CM-SHP-009@zid. Reading: a list for preparing orders is a pick list. Its concern, ZD-C-080, lands in CM-ORD-001.
- **km:RET-02.** The brief counts rules as detail. But the model gives payment-method rules a capability of their own (CM-PAY-019), and no platform holds anything on return rules, so the rest is placed as a candidate miss, not held, rather than as detail of CM-RET-003. The coordinator may read it as detail instead.

## Candidate misses, with what was searched

All three are **not held**: no statement and no out-of-scope entry matched. Each search ran with `class_slice.py search` and `outscope`, in English on all five platforms, and also in Arabic for Salla and Zid.

1. **km:SHP-04, scheduled delivery** (the buyer choosing a delivery date or time slot).
   - Searched: scheduled delivery; delivery date; delivery time; time slot; delivery window; delivery schedule; same-day; next-day; express delivery; موعد التوصيل; مواعيد التوصيل; وقت التوصيل; أوقات التوصيل; توصيل مجدول; جدولة التوصيل; تاريخ التوصيل; موعد التسليم; مواعيد التسليم; توصيل في نفس اليوم; التوصيل السريع; موعد.
   - The only match was WooCommerce Bookings' time slots (WC-S-5352), which is about booking a service, not delivery.
   - Delivery promises (CM-SHP-018) are a different thing.
2. **km:SHP-05, packages and box sizes** (package dimensions saved for labels and rates).
   - Searched: package; packages; package dimensions; box; boxes; box size; saved packages; dimensions; packing; أبعاد; الأبعاد; الطرد; الطرود; طرد; حجم الشحنة; صندوق; الصناديق; كرتون.
   - The matches were packing slips (CM-ORD-009), Salla's packaging materials (CM-SHP-021), BigCommerce's package protection through Route (BC-S-0101, which is insurance, in CM-CHK-004), and Zid's limit of 7 boxes on a return label (ZD-S-1013, in CM-RET-001's concern).
3. **km:RET-02, return rules** (return window, return fees, restocking fee, final sale).
   - Searched: return rules; return policy; refund policy; restocking; restocking fee; final sale; return window; return fee; self-serve returns; سياسة الاسترجاع; سياسة الإرجاع; سياسة الاستبدال; مدة الاسترجاع; فترة الاسترجاع; أسباب الإرجاع; رسوم الإرجاع; رسوم الاسترجاع; غير قابل للاسترجاع.
   - The matches were return reasons (SH-I-2096, in CM-RET-003), return-policy pages (CM-CNT-008), Salla Point's return-policy permission (SA-S-2655) and the platforms' own refund policies for their plans (not the merchant's).
   - Assumption: Shopify has a return-rules setting. This comes from general knowledge, not from the evidence; a capture would confirm or refute it.

The pages that would settle each miss are named in the row's `what_would_settle_it`. The coordinator routes them by `PLAN.md`, section 6, "Evidence".

## Time bombs

- km:PAY-06: bundles; wrong time. Its answerers' times differ: S-04 and S-10 before build, outside before release. Its `needed_by` is `launch`, but its subjects answer before build.
- km:PAY-07: bundles; wrong time. S-06 before build, the founder and outside before release; its `needed_by` is `later`.
- km:SHP-06: bundles; wrong time. S-10 before build, outside before release; its `needed_by` is `launch`.
- No row raises `wrong party` or `market fact`. PAY-06, PAY-07 and SHP-06 ask the market's facts openly, as questions about the market, rather than asking what the product should do.

## Problems with the brief or the evidence

- The brief lists "rules" among the detail that doesn't make a row `partly`. But the model gives some rules capabilities of their own (CM-PAY-019 payment method rules, CM-SHP-013 delivery customization). Where a row asks about rules that no platform holds at all, the brief doesn't say whether they are detail or a miss. km:RET-02 is placed as a miss, as said above.
- None of the subjects S-03 to S-11 carries the value of the address form per market, which S-02 binds per market (S02-F8). This is flagged on km:SHP-06 as `subject:none`.
