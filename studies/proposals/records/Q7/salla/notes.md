# Q7 salla (checking run): notes

## What was read
- Salla's help map (`help_map.py salla`), categories ⚙️ إعدادات المتجر, 🧭 قائمة الكل, 💳 طرق الدفع والمحفظة and مقالات قديمة › إعدادات وخيارات المتجر. Five articles were read from it: u4s3nz2yd3gxd92e8r4dpwbd (إضافة عملة جديدة للمتجر), epj429qolc9kuugn5gqroamo (تخصيص إعدادات الأسواق المتعددة), gkq7zm64xnf29y8wew2r8x7h (تجربة العميل للأسواق المتعددة), wv9wyqrnhwpm6m2rp3cmg653 (تفعيل وإدارة الأسواق المتعددة) and rvmsx19zkex4wgybruk7ovii (الأسئلة الشائعة حول الأسواق المتعددة), all in observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl.
- Three corpus searches. Their commands are in not-found.tsv. Documents read from them:
  - help articles fqieyzzp3p4jrvbbasqhfp0i, oj8gcbnnxczon55fz5ifpv3p and rkpltd2whn11d8f8v5ml53u8;
  - docs.salla.dev currencies/list.md, currencies/activate.md, twilight-sdk/currency-list.md and webhook-events/orders.md, all in observed-sa@4ca2e896:raw/runs/20261005T234928Z-docs-md/fetch.warc.gz, through warc_text.py;
  - salla.com/en-sa/ai-info, in observed-sa@4ca2e896:raw/runs/20261005T235211Z-com-en-scheme/fetch.warc.gz@472866. Its "15+ currencies and payments from 79+ countries" is the English form of the copy Q7-SA-K1959, so nothing new was recorded from it.
- No live page was read.

## Not read
- These listed documents were not read: the Tabby, Tamara and BNPL articles (their English snippets name SAR, AED and KWD), the coupon article xr4loly2dibn8qb8ovyja137, the promotions article okwxus4xcmvkz359dwhu0ucc, docs.salla.dev's country list (5394258e0.md), the Twilight currency-change endpoint, and the dashboard translation files.

## Account points not checked
Each sentence had used its two searches, and their terms were not in either, so these account points were neither searched nor recorded:
- Shopify [1]: POS local currency (Q7-SH-072), Managed Markets (Q7-SH-184), Bulgaria's dual display (Q7-SH-115), the API bank account and account currency (Q7-SH-134).
- Zid [1]: partners converting order totals (Q7-ZD-K0304), the transactions table's currency column (Q7-ZD-023), the Payments Open APIs' amount and currency (Q7-ZD-024), the cash on delivery limit in $ and SAR (Q7-ZD-K0120).
- Shopify [2]: submarket inheritance and single- or multi-country market defaults (Q7-SH-077, Q7-SH-079), the API market currency settings (Q7-SH-128), `multiCurrencyGatewayEnabled` (Q7-SH-186), draft order currency (Q7-SH-103), the domestic payout currency and plan limits (Q7-SH-011, Q7-SH-016, Q7-SH-K1636), business entities (Q7-SH-K1268), SG/HK/UAE accounts (Q7-SH-060), the conversion fee by country (Q7-SH-K1946).
- Zid [2]: activating a currency activates shipping (Q7-ZD-K0229).
- Shopify [3]: the admin after a change (Q7-SH-007), market exchange rate modes (Q7-SH-078), draft order rates (Q7-SH-101), editing international orders (Q7-SH-073), chargebacks (Q7-SH-066), timeline exchange rates (Q7-SH-014), owner-only activation of Multi-Currency Payouts (Q7-SH-059), Bulgaria (Q7-SH-106 and following).
- Zid [3]: plan and fee changes with notice (Q7-ZD-K0157).
- Shopify [4]: the Global-e account under Managed Markets (Q7-SH-K1600).

## Copies
- No copy was found wrong or out of date. Q7-SA-K1976's statement ends at "من حيث:". Its list of items is recorded as Q7-SA-007.
- On salla.com/payments, K1959 is stated as "أكثر من 15 عملة", while the plan feature K1949 reads "+33 عملة". This is recorded as read, not reconciled.

## Problems with the method
- With two searches per sentence, many account points (above) could not get a search of their own. Those rows are left unrecorded, not recorded with a search that didn't carry their terms.
- The run was interrupted by the session's usage limit after the copy step, and resumed. No rows had been written before the interruption.
