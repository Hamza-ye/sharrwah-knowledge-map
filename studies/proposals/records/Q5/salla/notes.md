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
