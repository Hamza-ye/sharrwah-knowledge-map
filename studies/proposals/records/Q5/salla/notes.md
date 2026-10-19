# Notes: Q5, salla

## What was read

All held, at observed-sa `4ca2e896a729215f422a137a364e7e9488610ba3`, except the docs page, which is cited by its URL.

- **Help centre, through `method/help_map.py salla`.** Category `om3wn15sdn7taao0ra0bbkmr` (💳 طرق الدفع والمحفظة), and these articles in Arabic:
  - dcrwxldslve7spa8eqdgii8g (تفعيل طرق الدفع في المتجر)
  - mwmsy60840mp73dpv7n0wd4s (طريقة تفعيل خدمات التقسيط | الدفع الآجل في متجرك)
  - vnmcb3lad5fiwd7xnrmbteql (تفعيل أبل باي Apple Pay)
  - fc8ttcpkn978atei99mcq6bw (تفعيل stc pay)
  - rkpltd2whn11d8f8v5ml53u8 (تفعيل الربط مع باي بال paypal)
  - gftxxtu5ykwzlyfmpo39bqbi (الربط مع Knet tap)
  - d9me3k8vqi09hdiun8r2ngfr (إعدادات قيود الدفع)
  - bqrpidrk4v27bhquze2a9blo (حدود معاملات الدفع الإلكتروني)
  - ppros5gh7uqhilhqddqnjgbd (تفعيل المدفوعات الإلكترونية)
- **Help articles opened from corpus-search hits:**
  - k93ekm8hwa183qrplyil2eaa (- إدارة المحافظ الرقمية, filed under مقالات قديمة)
  - wmmkc305vzb52ka2al4zbfrh (تفعيل تابي على متجرك في سلة الإمارات | سلة)
  - cibzvzd4edofyfsygrxmp3p1, in English (Accept Apple Pay without the setup complexity)
- **salla.com pages, from `structures/salla/com-policies/`:**
  - `terms/text.txt` (https://salla.com/terms): المادة الأولى, الثالثة, السابعة, الثامنة, الرابعة عشرة, التاسعة عشرة, التاسعة والعشرون
  - `payments/text.txt` (https://salla.com/payments), whole
  - `policies-selling/text.txt` (https://salla.com/policies/selling-policies), whole
  - `shipping/text.txt` (https://salla.com/shipping), lines on الدفع عند الاستلام only
  - `privacy/text.txt`, the line on بوابات الدفع only
- **Dashboard text:**
  - `structures/salla/dashboard-translations/ar/payments.json`: the keys under gateway_settings, gcc_banner, salla_payments, charity_payments, cod and verification_banner, and every key searched for تعطيل, إيقاف, غير متاح, توقف and إلغاء
  - `structures/salla/dashboard-translations/ar/apps.json`: the keys containing الدفع, المدفوعات and إيقاف التطبيق
- **Developer docs:** https://docs.salla.dev/recurring-payments/overview.md, read through `method/warc_text.py` from `raw/runs/20261005T234928Z-docs-md/fetch.warc.gz@1329598`. `held_index.py` also shows it held as a capture in this repository, so it is cited by its URL.

Corpus searches (commands in `not-found.tsv`'s `searched`):
- for [4], on stopping or disconnecting a method or gateway;
- for [5], on PayPal;
- for [1] and [2], on the merchant's agreements with providers;
- for [3], on lists of other gateways.

## Live pages

None were read. What was held answered every sentence that live reading would have covered. The pages the copied gaps say were "not read" (salla.com/terms, /payments, /policies/selling-policies, /shipping) are all readable from `structures/salla/com-policies/`.

## What couldn't be read

Merchant dashboard pages are not held: `held_index.py` reports https://s.salla.sa/payments, /payments/gateways and /payments/gateways/comparison as not held. They are routed to the founder in Q5-SA-N02 and Q5-SA-N04.

## Tables and lists

- **BNPL comparison table** (جدول المقارنة بين وسائل الدفع الآجل المختلفة, article mwmsy60840mp73dpv7n0wd4s). It has fewer than 20 rows. Recorded: تفعيل خارج السعودية, المنتجات المسموح بتقسيطها, المسؤول عن التحصيل للعميل and ملاحظات خاصة. Left out: عدد الدفعات المتاحة, الحد الأدنى للطلب, الحد الأقصى للطلب and العملات المدعومة.
- **Restriction types in إعدادات قيود الدفع.** Recorded as two runs, Q5-SA-043 and Q5-SA-044, because a note line separates them in the source. The opening words "حيث تشمل الأنواع التالية" are cited on Q5-SA-043.

## Copied gaps

- **Closed:** Q5-SA-G0171 (a reason the selling policy gives) is closed by Q5-SA-010.
- **Still open after reading the held pages:**
  - G0113 to G0116: salla.com/payments and the usage agreement name no processor, acquirer or licence. The agreement says only "عبر شركائها".
  - G0169 and G0170: the selling policy has no change clause and no party clause.
  - G0224 to G0226.
- **Wording of the copied gaps:** many give `why_not_held` = "page not read" for pages that are held and readable. Statements from those same pages are already among the copies (for example Q5-SA-P0079 and Q5-SA-P0082 from the terms).

## Copies wrong or out of date

None found.

## Problems with the method

- **`selection.tsv` was briefly truncated.** My first script to set the actions failed partway through writing it (a Python csv quoting error), and `copy_statements.py copy` then ran on the truncated file.
  - I regenerated the selection with `copy_statements.py candidates Q5 salla <scratch dir>`. The result was byte-identical in size to the original (30,482 bytes).
  - I copied it back, deleted the copied files and set the actions again.
  - I then ran the copy again. The copied files now in the folder come from that second run.
- **Quote matching.** Typed Arabic quotes can differ from the source in the order of diacritics (shadda and kasra). Every quote here was taken from the source text by a script, so it matches the source exactly.

## Re-check against the observed runs, 19 October 2026

### What was read

All at observed-sa `4ca2e896a729215f422a137a364e7e9488610ba3`, through `git show` from outside the repository.
- **Guides:** `README.md` and `docs/READING.md`, whole.
- **Index:** `index/rest-endpoints.tsv`, its rows for payments, gateways, onboarding and persona.
- **Saved responses:**
  - `raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/1683.json` (GET /admin/v2/gateways/payment, store merchant, step 71);
  - `raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/1488.json` (the same endpoint, store real-merchant, step 42), `0614.json` (wallet/summary, step 17), `0617.json`, `0661.json`, `10106.json`, `12135.json`, `12176.json`;
  - `raw/runs/20261008T133523Z-sweep-demo-store-en/responses/2703.json` (kyc schema), searched for عقد, contract, agreement and terms only;
  - `raw/runs/20261008T125139Z-sweep-merchant-routes-ar/responses/0535.json` (onboarding/persona-country) and `0527.json` (persona translations, searched for دفع).
- **Steps:** `20261008T122729Z-sweep-merchant-menus-ar/steps/071.text.txt`; `20261012T010906Z-sweep-real-merchant-full-en/steps/017.text.txt`, `042.text.txt`, `063.text.txt`, `067.text.txt`; `20261008T125139Z-sweep-merchant-routes-ar/steps/023.text.txt` and `024.text.txt` (the onboarding question page /persona/qna); and each run's `actions.jsonl` and `run.json`.
- **Stores:** each run names its store in `run.json` `extra.store`: merchant, real-merchant.
- **Corpus searches** (`python3 -I method/corpus_search.py salla … --max 10`):
  - "gateways/payment" "بوابات الدفع" "payment gateways" (sentences [1] and [3]);
  - the four searches now in `not-found.tsv`'s `searched` for N01 to N04;
  - "عقد خدمات الدفع" "payment services contract" "payment services agreement" "مزود خدمات الدفع" "payment service provider" "ترخيص" "license" (G0113 to G0115, G0177, H0002, H0004, H0008);
  - "سياسة البيع" "selling policy" "selling-policies" (G0169, G0170): it listed no run document;
  - "store-wallet" "رصيد المدفوعات الإلكترونية" "المدفوعات الإلكترونية" "Electronic Payments" "Online payment payouts" "payout" (sentence [5]);
  - "payment_methods_activation" "تفعيل وإلغاء تفعيل طرق الدفع" "blocks_payment_activation" "requires_paid_plan" "قم بترقية باقتك" (sentences [1] and [2]).
- **held_index:** https://s.salla.sa/payments is readable as run steps; https://s.salla.sa/payments/gateways and /payments/gateways/comparison are not held; https://s.salla.sa/persona/qna is readable as run steps.

### Open items

- **Q5-SA-N01:** unchanged. Nothing in the runs read shows a notice before a payment method is withdrawn.
- **Q5-SA-N02:** unchanged. The real store's gateways answer and page list PayPal (not active); no run holds the PayPal connection drawer. Route narrowed: the page's list is held; the drawer is not.
- **Q5-SA-N03:** unchanged.
- **Q5-SA-N04:** unchanged in what is missing. The gateways answers list `online_payment_gateways` with one item, and no words present the lists as complete (recorded as Q5-SA-073). Route narrowed: the طرق الدفع page is read in the runs at /payments, so the row now routes only مقارنة بوابات الدفع.
- **Copied gaps G0113, G0114, G0115, G0177, H0002, H0004, H0008:** still open. The kyc schema answer read holds no contract clause.
- **G0169, G0170:** still open; the search listed no run document.
- **G0224, G0225, G0226:** still open (N01's search).

### Wording check

Every name, label and path in the four rows is in what their `read` names or in the folder's copies (`copied-view.tsv` for عقد التاجر مع جيديا, بوابات الدفع الأخرى and ميسر - هايبر باي). No wording changes.

### New statements

Q5-SA-069 to Q5-SA-077, cited by Q5-SA-C104 to Q5-SA-C115. Statements from saved responses are written as the checker decodes the JSON (Arabic as letters, `json.dumps` spacing). Q5-SA-070 records the quick_methods list's four items in full; Q5-SA-073 the four consecutive lists online_payment_gateways, digital_wallets, bnpl and other_payment_methods in full; Q5-SA-075 the wallets list's three items in full.

### Not recorded, and not read

- Not recorded because copies already say it: the real store's payout messages (every 48 hours above 100 SAR; cash on delivery every Sunday and Wednesday: K1550, K1544, P0093), and its cash-on-delivery wallet page's flow (P0041, P0042).
- The onboarding question page (/persona/qna) and its answer ask the store's country and name no payment method; nothing recorded.
- Not read: the gateways answers of store-sherawya and public-demo, the wallet answers of the other stores, the Partners portal payouts page, and the sdk and mahally translations' payment labels.

### Problems

- The corpus search's output puts the published material first. With `--max 10` per corpus the run documents come after several hundred lines, so I saved each search's output and filtered it.
