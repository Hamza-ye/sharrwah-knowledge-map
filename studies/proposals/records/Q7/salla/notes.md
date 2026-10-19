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

## Re-check against the observed runs, 19 October 2026

### What was read
- The guides of observed-sa at 4ca2e896a729215f422a137a364e7e9488610ba3: README.md and docs/READING.md, whole; index/rest-endpoints.tsv, grepped for currency, wallet, payment, onboarding, settlement and refund endpoints.
- Searches, each with --max 10:
  - for sentence [1]: `python3 -I method/corpus_search.py salla "عملة" currency currencies "سعر الصرف" exchange_rate --max 10`;
  - for N01 and N03: `python3 -I method/corpus_search.py salla رسوم تحويل العملة فرق العملة سعر الصرف exchange_rate conversion fee conversion fees عملة الدفع --max 10`;
  - for N02, Q7-SA-G0151, Q7-SA-G0153 and sentence [4]: `python3 -I method/corpus_search.py salla تحصيل المدفوعات رصيد المدفوعات دورة التحويل settlement settlements payout payouts --max 10`;
  - for N04: `python3 -I method/corpus_search.py salla عملات رقمية العملات المشفرة crypto cryptocurrency cryptocurrencies bitcoin --max 10`;
  - for N05: `python3 -I method/corpus_search.py salla عملة المتجر store currency دولة المتجر store country --max 10`, then `python3 -I method/corpus_search.py salla "persona-country" "create-store" "دولة المتجر" "عملة المتجر" "store country" "store currency" --max 10` (the onboarding pointer; also sentence [2]);
  - for N06: `python3 -I method/corpus_search.py salla عملة السوق market currency market currencies غير مدعومة unsupported currency --max 10`;
  - for N07 and sentence [3]: `python3 -I method/corpus_search.py salla تغيير العملة change the currency change currency طلبات شراء --max 10`;
  - for N08: `python3 -I method/corpus_search.py salla عملة الاسترجاع استرجاع المبلغ refund refunds --max 10 --with currency عملة`;
  - for N09: `python3 -I method/corpus_search.py salla نقل المتجر تغيير الدولة change country تغيير دولة --max 10`;
  - for Q7-SA-H0002: `python3 -I method/corpus_search.py salla عقد خدمات الدفع payment services agreement مدفوعات سلة Salla Payments --max 10`.
- Files read, all at observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3, under raw/runs/:
  - 20261012T010906Z-sweep-real-merchant-full-en (store real-merchant): steps/306.text.txt, steps/067.text.txt, steps/042.text.txt, responses/11108.json (GET /admin/v2/currencies), responses/1488.json (GET /admin/v2/gateways/payment), responses/2294.json (GET /admin/v2/orders/1202316591), responses/0614.json (GET /admin/v2/store-wallet/wallet/summary), run.json, actions.jsonl and responses.jsonl for steps and dates;
  - 20261008T141131Z-sweep-merchant-en (store merchant): responses/2481.json (wallet summary), responses/2443.json (GET /admin/v2/gateways/payment);
  - 20261009T033607Z-sweep-settings-demo-en (store demo): responses/1441.json (GET /admin/v2/currencies/available), steps/030.text.txt;
  - 20261008T131847Z-sweep-merchant-routes-ar (store merchant): steps/075.text.txt;
  - 20261008T133523Z-sweep-demo-store-en (store store-sherawya): steps/231.text.txt and 231.frame-1.text.txt, responses/0153.json (settings translations), responses/5134.json (GET /admin/v2/onboarding/persona-country), responses/5171.json (GET /admin/v2/onboarding/create-store);
  - 20261008T135130Z-sweep-merchant-settings-ar: responses/0791.json (the settings section for /general/currencies, a layout without currencies);
  - 20261012T045412Z-journey-real-merchant-details-en: responses/0089.json (GET /admin/v2/orders, 15 orders, each "currency":"SAR" and "exchange_rate":[]);
  - 20261009T055452Z-journey-order-lifecycle-demo: responses/0150.json; 20261008T150518Z-journey-orders-demo: responses/0057.json.
- No live page and no published page was read.

### Open items
- Q7-SA-N01 to Q7-SA-N09: unchanged. The re-check searches and the run documents opened are added to each row's searched and read. No row was closed or narrowed, so not-found-closed.tsv is not written.
- Q7-SA-G0151: not closed. Q7-SA-023 shows, for store real-merchant, a paid electronic payments payout in SAR; where the currency is set is not shown. Its note names the gap.
- Q7-SA-G0153: not closed. The wallet page (step 067 of the real-merchant run) shows the payouts of electronic payments by order without a currency; the wallet summary answer gives the last payout's currency (Q7-SA-023). Its note names the gap.
- Q7-SA-H0002: unchanged. The payments pages and gateway answers read name no entity or licence.
- Phrases from the coordinator: none for this folder.

### Wording check
- Every row's what_is_missing is in plain words and names no platform label, path or phrase. No change.

### Statements and scope
- Q7-SA-017 to Q7-SA-035 are new, from the runs. The scope of the real-merchant statements adds "merchant_type":"KSA" from the same run's GET /admin/v2/gateways/payment (Q7-SA-C018).
- The currencies/available answer is a list of 31 items; Q7-SA-026 to Q7-SA-031 record the items for SA, AE, KW, BH, QA and YE. The same answer (same sha256 in the search) was received by store real-merchant at step 306.
- Q7-SA-032 and Q7-SA-033 give the plan named in the page's header (بيسك) in their scope, from the same step's text (Q7-SA-C038).
- The real-merchant page's sentence ends with the letter ز, as the page and the settings translations show it.

### Not read
- The gateway answers' fees (each in SAR) were read but not recorded: the list of gateways is long and its fees bear on the question only through their currency.
- Not opened: the Partners portal payouts answers and pages (they concern a partner's payouts), the other orders and transactions answers, the translation files other than 0153, the storefront steps listed for N09, and the docs and help documents the searches listed beside the runs.

### Problems
- The brief asks for one search per open item; items N01 and N03, and N02 with the two copied gaps, shared a search since their terms are the same.
