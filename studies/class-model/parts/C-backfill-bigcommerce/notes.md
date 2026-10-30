# C-backfill-bigcommerce: notes

## What this part did

C-bigcommerce added two capabilities to domain C (its notes, batch 1 and the SHP batch):
- **CM-CHK-010, Persistent cart,** parent CM-CHK-002, made a capability by the coordinator after batch 1. BigCommerce's cell rests on the plan line Persistent cart, "Improve your customer's experience by saving their shopping cart to their account, so when they switch devices, their cart is still there" (BC-C-014/decides/BC-S-0084).
- **CM-SHP-023, Shipping rules engine,** parent CM-SHP-001. BigCommerce's cell rests on the plan line ShipperHQ shipping rules engine (BC-I-0410). That is an inventory entry, and no statement defines it.

This part writes their Shopify, Salla, WooCommerce and Zid cells, eight in all. All eight are `none-held`. It adds no capability, lands no concern and writes no ruling. `evidence.tsv` holds only its header, because no cell cites a statement. Each row is a reading unless it quotes a statement.

What I read:
- the brief;
- `model --domain C --areas CHK,SHP`;
- C-bigcommerce's notes and rows on the two capabilities;
- `candidates --domain C --platform <platform> --areas CHK,SHP` for the four platforms. It found 0 statements for either capability on every platform, because the only terms are BigCommerce's own;
- CM-CHK-002's evidence on every platform, to keep the cart itself apart;
- `caps --terms` for shipping rules, rules engine, ShipperHQ, قيود الشحن, persistent cart and saved cart. Beyond the two capabilities themselves, it matched only CM-PAY-019, CM-SHP-001 and CM-SHP-013, on قيود الشحن;
- then `search` on each platform with the terms in each cell's `searched`, in English, and for Salla and Zid in Arabic too (singular and plural, with and without ال). Where a term is a single common word (cart, سلة, rules, قيود, شروط), I read its hits for the words named in `searched`.

## The cells (readings)

**CM-CHK-010, Persistent cart: `none-held` on all four.**

No statement found names a cart kept with the buyer's account, or one that stays when the buyer changes device. The cart itself (CM-CHK-002) and abandoned carts (CM-CHK-007) hold their own statements, and none of those says where the cart is kept, so none is cited here. Each cell's reading lists its hits. The nearest ones:
- **Shopify:** the cart webhooks, carts/create "Occurs when a cart is created in the online store" (SH-S-6066, CM-CHK-002's), and the customer-account order-status cart-line targets (SH-I-1644, SH-I-1645). Neither says the cart is saved to the account.
- **Salla:**
  - the storefront events Cart Shared, Cart Updated and Signed In (SA-S-1364, SA-S-1320, SA-S-1356). None says the cart is kept with the account;
  - "حفظ بطاقة وعنوان العميل" in Salla Payments' fee (SA-S-0104), which saves the card and address, not the cart;
  - سلة also matches the brand name everywhere.
- **WooCommerce:**
  - the feature name Clear Customer Sessions When Empty (WC-I-0347). It has no definition held, which is a gap: what a WooCommerce customer session holds, and whether it is kept with the account, isn't in the concern map;
  - Save for Later in Cart (WC-S-5456, WC-S-5458, WC-I-0350). It is a shopper list beside the wishlist, in WC-C-097, which `scope.tsv` gives domain D. It isn't the cart saved to the account.
- **Zid:** Zid Cashier's devices, and the plan line Abandoned Cart Details (ZD-S-0913, CM-CHK-007's).

**CM-SHP-023, Shipping rules engine: `none-held` on all four.**

BigCommerce never defines the capability: its only evidence is the plan line's name (BC-I-0410). So each cell says the definition isn't stated. A statement could be this capability's only where its own words name a shipping rules engine, and none found does. The brief: "A shared term joins only where the cited definitions or identifiers show the same object."
- **Salla shares the words but not a definition.** It has three hits, none of which says what its rules do, and all three are already `core` or `shows` in CM-SHP-001's Salla cell:
  - the staff permission shipping_rules_management, "shipping rules management" (SA-S-2400). Its Arabic name is "قيود شركات الشحن", restrictions on shipping companies (SA-S-2617);
  - the released flag shipping-rules (SA-S-3005, plans pro and special);
  - the plan line قيود الشحن والتوصيل (SA-S-2112, SA-S-2146).

  I didn't cite them here.
- **Zid's** shipping restrictions are already in CM-SHP-001's Zid cell, and ZD-C-063's statements also in CM-PAY-019's. I didn't cite them here either. They are:
  - "تحديد قيود الشحن لكل منتج أو منطقة" in the shipping settings (ZD-S-0855);
  - the route الاعدادات > عام > قيود الشحن والدفع, with its plans (ZD-S-0857, ZD-S-0858, ZD-I-0134).
- **Shopify's** fulfillment constraint rules (SH-S-5995, SH-S-6203) are CM-SHP-014's, rules on how orders are fulfilled, and its delivery customizations are CM-SHP-013's. Neither is named a shipping rules engine.
- **WooCommerce's** only shipping hit is the merchant's legal duty in WooCommerce Shipping's terms (WC-S-0484). The other rules are WooPayments' fraud and Radar rules and Bookings' availability rules.

**For the coordinator:** if BigCommerce's definition of the ShipperHQ engine is captured, compare it with Salla's shipping-rules and قيود الشحن والتوصيل, and with Zid's قيود الشحن. Those statements could then join CM-SHP-023, or the capability could join CM-SHP-001. Neither Salla's nor Zid's definition of its own shipping rules is held either: Salla's flag and plan line are names, and Zid's ZD-S-0855 says only "restrictions per product or region".

## Statements kept apart

No statement is cited here, so no statement is cited in two places through this part. The hits each reading names stay where they are:
- CM-CHK-002: SH-S-6066, ZD-S-0049, WC-S-0149;
- CM-CHK-007: SA-S-3250, SA-S-3458, ZD-S-0913;
- CM-SHP-001: SA-S-2400, SA-S-2617, SA-S-3005, SA-S-2112, SA-S-2146, ZD-S-0855, ZD-S-0857, ZD-S-0858;
- CM-PAY-019: ZD-C-063's statements;
- CM-SHP-014: SH-S-5995, SH-S-6203;
- domain D: WC-C-097.

## Gaps

- **Persistent cart:** no platform's statements say whether its cart is kept with the buyer's account. The structures that would hold it are each platform's cart and customer-session documentation. For WooCommerce, that includes what Clear Customer Sessions When Empty (WC-I-0347) does.
- **The shipping rules engine:** BigCommerce's ShipperHQ shipping rules engine has no definition, and no statement names a maker (as C-bigcommerce noted). Salla's shipping-rules and Zid's قيود الشحن have no definition beyond their names and ZD-S-0855's phrase.

## What the checker flagged

The final check prints `0 problems, 8 flags for the reviewer`. All eight flags are of one kind: "none-held, and N statements match its searched terms". They come from the common single words searched (cart, devices, sessions, سلة, جهاز, rules, قيود, شروط, condition), whose hits I read. Each cell's reading names the hits that bear on the capability's words and why they aren't cited. The rest are other things: payment sessions, POS devices, the brand name سلة, payment, fraud and product restrictions, legal terms, and search engines (محركات البحث).

## Problems

- None with the brief.
- The candidates step gives no lead for a capability that only one platform names, because it searches the other platforms' terms. Here those are BigCommerce's alone, so every lead came from my own searches.
