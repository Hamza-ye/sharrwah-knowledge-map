# Cards: Q7 on salla

13 records cited by `studies/proposals/drafts/Q7/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - Prices held: Shopify, Zid, WooCommerce and BigCommerce hold a seller's own prices in one currency per store, and match on role (basis 4). Shopify's store currency is the one "for pricing products and running reports"; Zid's العملة الأساسية is "العملة التي تم إدخال أسعار المنتجات باستخدامها"; WooCommerce allows "one base currency per store", and "WooCommerce uses it to display product prices and record new orders"; BigCommerce's default currency is "assigned during store creation, is always a transactional currency". Salla's seller sets the store's current currency, but the words read don't say prices are entered in it, so Salla's match is partial. Q7-SH-K1935 Q7-ZD-002 Q7-WC-K0745 Q7-WC-K0747 Q7-BC-013 Q7-SA-001
- **section 1, line 11:** - The buyer's place picks the shown currency first, and the buyer may then pick another: on Salla the default "تعتمد على موقع العميل الجغرافي", and the buyer can choose from a list beside the cart. Q7-SA-K1957 Q7-SA-K1956
- **section 1, line 12:** - Paid by buyers: on Shopify, BigCommerce, WooCommerce and Salla the currency shown and the currency charged can differ, and what the payment provider supports decides the charge; they match on role (basis 4). Zid's pages aren't reconciled (below): Q7-SH-K1938 Q7-BC-014 Q7-WC-029 Q7-SA-K1963
- **section 1, line 17:** - Salla: "عند تفعيل التاجر لبوابة دفع سلة، يتم استقبال جميع المدفوعات بالريال السعودي". Q7-SA-K1963
- **section 1, line 18:** - Each order records its currency, and four record the store's currency or a rate beside it, matching on role (basis 4): Shopify's order has `presentmentCurrencyCode`, and its MoneyBag holds both amounts; Zid's order gives the "Exchange rate of the store currency relative to the order currency"; BigCommerce's has `currency_code`, `default_currency_code` and `currency_exchange_rate`; Salla's an `exchange_rate` with `base_currency`, `exchange_currency` and `rate`; WooCommerce's a single "Currency the order was created with, in ISO format." (shipped code; the others stated). Q7-SH-124 Q7-SH-123 Q7-ZD-010 Q7-BC-020 Q7-SA-016 Q7-WC-055
- **section 1, line 22:** - Salla ties the payout to the country's banks and currency, as "الحساب لدى بنك إماراتي و بعملة الدرهم الإماراتي" in the UAE (stated). In a run on store real-merchant (12 October 2026, observed), the latest payout was 5171.76 in SAR. Q7-SA-K1964 Q7-SA-023
- **section 1, line 28:** - In the runs (observed), a Shopify store with an address in Sanaa, Yemen showed "Yemeni Rial (YER)" in its store defaults (store fake-demo-sharrwah, 5 October 2026), and Salla's list of currencies a store could add held Yemen's YER (store demo, 9 October 2026). Q7-SH-191 Q7-SA-031
- **section 1, line 35:** - Who may change a store's currency: on Shopify "Only the store owner can change store currency", and a change after the first order needs a check of "I understand the risk of changing the store currency" (stated); on Salla, holders of the staff permission `currency_setting_edit` (observed in store demo's staff permission list, 8 October 2026). On store capture-plus (2 October 2026, observed), the General settings page's saved markup held a "Change store currency" heading with only Save and Cancel under it. Q7-SH-008 Q7-SH-181 Q7-SA-K1950 Q7-SH-205
- **section 1, line 36:** - Salla allows a change only "بشرط أن لا يكون هناك طلبات شراء للعملاء". Q7-SA-004
- **section 1, line 37:** - A change treats prices in one of three ways: Q7-SH-006 Q7-ZD-K0302 Q7-SA-004
- **section 1, line 40:** - Salla doesn't allow the change once orders exist. Q7-SA-004
- **section 1, line 51:** - Salla: "يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها" (stated). The page that would say in which currency Salla Payments receives and settles funds is held but wasn't read. In the run on store real-merchant (12 October 2026, observed), the wallet summary gave three wallets, Wallet, Electronic Payments and Cash on Delivery Payments, each in SAR. Q7-SA-K1560 Q7-SA-G0151 Q7-SA-022
- **section 2, line 64:** - From the platforms: country defaults (Zid, WooCommerce, BigCommerce), Salla's list of currencies a store could add, each tied to a country (observed, store demo, 9 October 2026), and WooCommerce's payout currencies by country. Why: rule 1. Q7-BC-029 Q7-SA-031 Q7-WC-K0739
- **section 2, line 66:** - From the platforms: Shopify's currency per market and one-country default; Zid's market currency, local default market and prices "وبعملة السوق نفسها"; Salla's default by location and the buyer's own pick. Why: rule 1, as one store is set up for each place it sells to; and rule 3, as the level at which prices and currencies sit is part of the data model. Q7-SH-079 Q7-ZD-019 Q7-SA-K1957 Q7-SA-K1956
- **section 2, line 69:** - From the platforms: BigCommerce's transactional or display-only setting per currency, and its gateway rule; Shopify's and Salla's charge in one currency when the provider can't take the shown one. Why: rule 2, as a change of provider then changes a market's set-up, not checkout or orders. Q7-SH-K1938 Q7-SA-K1963
- **section 2, line 72:** - From the platforms: the currencies and rates Shopify, Zid, BigCommerce and Salla record on orders; WooCommerce's earlier orders, which keep their currency and totals; refunds in the currency paid (Shopify) at the refund's rate (WooCommerce). Why: rule 3, as an order whose amounts follow a later rate or store currency no longer shows what the buyer paid. Q7-SA-016 Q7-WC-027 Q7-SH-068 Q7-WC-019
- **section 2, line 77:** - From the platforms: Shopify's and WooCommerce's payout currency and default account, and Shopify's Multi-Currency Payouts; payout currencies bounded by region or entity (Shopify), country and its banks (WooCommerce, Salla), or the provider (BigCommerce). Why: rule 3, as the money flow ends at this payout, and partner contracts decide its currencies. Q7-SH-012 Q7-SH-K1268 Q7-WC-K0739 Q7-SA-K1964 Q7-BC-P0016
- **section 2, line 79:** - From the platforms: per-currency balances (Shopify, WooCommerce, BigCommerce), Salla's wallets, each with a currency (store real-merchant, 12 October 2026, observed), and Zid's wallet, its currency set by country. Why: rule 3. Q7-SA-022 Q7-ZD-P0122
- **section 2, line 80:** - The guard: the ledger records balances and holds no money. Any arrangement in which Sharrwah holds sellers' money, or a payment company holds it in an account opened through Sharrwah, as Salla's رصيد المدفوعات الإلكترونية and Zid's wallet hold their sellers' proceeds, goes live only by the founder's decision. Q7-SA-K1560 Q7-ZD-K0117
- **section 2, line 81:** - **Currency migration**. Proposed: the store owner may change the store currency until the first order; after it, only a currency migration run by Sharrwah can, leaving every recorded order as it is and stating whether prices convert at a stated rate or keep their numbers. The same migration serves a change Sharrwah makes for a whole place. Q7-SA-004 Q7-SH-008 Q7-WC-027
- **section 3, line 97:** - Per payout account: the **payout currency**, as Shopify's and Salla's bank accounts each carry one. Q7-SH-004 Q7-SA-K1964
- **section 3, line 100:** - Who sets each: Q7-SH-008 Q7-SA-K1956 Q7-BC-P0015
- **section 3, line 102:** - The store owner sets the **store currency**, as only the owner can on Shopify; staff holding a currency permission, like Salla's `currency_setting_edit` (store demo, 8 October 2026, observed), set the markets' currencies and rate sources. Q7-SH-008 Q7-SA-K1950
- **section 3, line 103:** - The buyer picks among a market's currencies, as on Salla. Q7-SA-K1956
- **section 3, line 105:** - The bank and its country bound a payout account's currency, as Salla requires an account at the country's bank, in its currency. Q7-SA-K1964
- **section 5, line 122:** - Who holds a seller's money before payout, and in which currency. The records name such balances' currencies only in part (section 1, [4]). Keep the **seller ledger** apart from whatever account holds the money, so the design fits a provider holding it, an arrangement through Sharrwah, or none. Settled by: the founder's decision under the guard, and the providers' contracts. Q7-SA-022 Q7-ZD-P0122 Q7-SH-N01
- **section 7, line 146:** - Which payment providers Sharrwah works with at each place, given that what they support decides the currencies buyers can be charged in, and sellers paid out in; Stripe isn't available for Yemen. Q7-SH-K1937 Q7-BC-P0016 Q7-SA-K1963 YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 7, line 147:** - Whether any arrangement holds sellers' money through Sharrwah, by Sharrwah itself or a payment company in an account opened through Sharrwah, and in which currency: the founder's decision, under the guard. Q7-SA-K1560 Q7-ZD-P0122
- **section 7, line 153:** - Sharrwah's own legal position on keeping sellers' balances and on converting currencies, and any licence either needs, for the founder with a lawyer. The platforms' terms show only what they require of their sellers: Shopify's, that a seller opens accounts with Payment Processors; Salla's, that it provides payment and settlement through its partners. Q7-SH-P0010 Q7-SA-P0079
- **section 8, line 159:** - What the records show: Shopify and WooCommerce define the payout currency in the same terms, and BigCommerce's settlement currency matches it on role (basis 4). It is set for the payment account: by region or business entity on Shopify, with more currencies on some plans; by country on WooCommerce; through the provider on BigCommerce; by the country's banks on Salla. Balances before payout are kept per currency on Shopify, WooCommerce and BigCommerce. Salla's balance holds sales proceeds before transfer; the page naming its currency wasn't read, and the run on store real-merchant gave the store's wallets in SAR (12 October 2026, observed). Zid's terms set its wallet's currency by the merchant's country; the currency of Zid Pay's balance and deposits, and of Shopify's reserved funds, wasn't in what was read. S01-VP-23 Q7-SH-004 Q7-WC-004 Q7-BC-P0014 Q7-SH-012 Q7-SH-K1268 Q7-SH-P0155 Q7-WC-K0739 Q7-BC-P0016 Q7-SA-K1964 Q7-SH-131 Q7-WC-048 Q7-BC-058 Q7-SA-K1560 Q7-SA-G0151 Q7-SA-022 Q7-ZD-P0122 Q7-ZD-N01 Q7-ZD-N02 Q7-SH-N01

## The cards

### Q7-SA-001

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q7/salla/statements.tsv`):
- stmt_id: Q7-SA-001
- bears_on: 1;2
- identifier: مركز الإعدادات > عام > العملات
- statement: 1- عيّن العملة الحالية للمتجر.
- cite_ids: Q7-SA-C001
- from: held

**Citation Q7-SA-C001:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 134 (article u4s3nz2yd3gxd92e8r4dpwbd, إضافة عملة جديدة للمتجر), 🚀 خطوات إضافة العملات إلى المتجر | 2026-08-31 | kind: stated | quote check: found
- quote: 1- عيّن العملة الحالية للمتجر.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …AC%D8%AF%D9%8A%D8%AF%D8%A9-%D9%84%D9%84%D9%85%D8%AA%D8%AC%D8%B1/u4s3nz2yd3gxd92e8r4dpwbd لديك زبائن من بلدان مختلفة، ولديهم تفضيلات باستخدام عملات معينة، يمكنك إتاحة العملات التي يُفضلها عملاؤك إلى متجرك. 📌 المحاور الرئيسية للمقالة: - خطوات إضافة العملات إلى المتجر - الأسئلة الشائعة 🚀 خطوات إضافة العملات إلى المتجر 1. من القائمة الرئيسية، اضغط (مركز الإعدادات). 2. من تبويب ( عام )، اضغط (العملات). 3. عيّن العملات المتاحة في متجرك، ثم اضغط (حفظ). ⟪1- عيّن العملة الحالية للمتجر.⟫ 2- فعّل حالة العملات المتاحة حسب حاجة متجرك. 3- اختر عملة جديدة، ثم اضغط (إضافة) لإضافة عملة إلى العملات المتاحة في متجرك. 🚀 الأسئلة الشائعة ❓هل يمكنني تغيير العملة الافتراضية للمتجر عندما أرغب بذلك؟ نعم ، بشرط أن لا يكون هناك طلبات شراء للعملاء. ❓كيف يستطيع العميل اختيار العملة التي يُفضل الدفع بها؟ عندما يتصفح العميل المتجر، يمكنه اختيار العملة المتاحة التي تناسبه من قائمة العملات بجوار سلة المشتريات في أعلى المتجر. فتظهر له أسعار المنتجات بال…

### Q7-SA-K1957

**Cited at:** section 1, line 11; section 2, line 66

**Record** (`studies/proposals/records/Q7/salla/copied.tsv`):
- concern_id: SA-C-163
- placement: decides
- structure: https://help.salla.sa/article/إضافة-عملة-جديدة-للمتجر/u4s3nz2yd3gxd92e8r4dpwbd
- identifier: 💡 توضيح مهم
- statement: عملة المتجر الافتراضية التي تظهر للعميل تعتمد على موقع العميل الجغرافي، وليست مرتبطة بالعملة الافتراضية المضافة داخل إعدادات المتجر.
- cite_ids: SA-S-0154

**Citation SA-S-0154:** `https://help.salla.sa/article/إضافة-عملة-جديدة-للمتجر/u4s3nz2yd3gxd92e8r4dpwbd` | 💡 توضيح مهم (line 697 of the rendered text) | 2026-08-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/018-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:37Z, captured)
- quote: عملة المتجر الافتراضية التي تظهر للعميل تعتمد على موقع العميل الجغرافي، وليست مرتبطة بالعملة الافتراضية المضافة داخل إعدادات المتجر.
- title: إضافة عملات جديدة وتفعيلها للمتجر | مركز المساعدة - سلة
- the page opens: إضافة عملات جديدة وتفعيلها للمتجر مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل ح…
- in context: …اجة متجرك. 3- اختر عملة جديدة، ثم اضغط (إضافة) لإضافة عملة إلى العملات المتاحة في متجرك. 🚀 الأسئلة الشائعة ❓هل يمكنني تغيير العملة الافتراضية للمتجر عندما أرغب بذلك؟ نعم، بشرط أن لا يكون هناك طلبات شراء للعملاء. ❓كيف يستطيع العميل اختيار العملة التي يُفضل الدفع بها؟ عندما يتصفح العميل المتجر، يمكنه اختيار العملة المتاحة التي تناسبه من قائمة العملات بجوار سلة المشتريات في أعلى المتجر. فتظهر له أسعار المنتجات بالعملة المختارة، بالشكل: 💡 توضيح مهم: ⟪عملة المتجر الافتراضية التي تظهر للعميل تعتمد على موقع العميل الجغرافي، وليست مرتبطة بالعملة الافتراضية المضافة داخل إعدادات المتجر.⟫ هذا يعني أن الأسعار قد تُعرض بعملة محلية مختلفة تلقائياً لتسهيل تجربة الشراء لدى عملائك من بلدان متعددة. اسأل, واطلب الدعم من التجار وفريق سلة. السابق التالي تصنيفات ذات صلة نطاق | دومين المتجر لغات المتجر والترجمة الفورية أقسام ذات صلة 🏡 الصفحة الرئيسية 📦 الطلبات 🏷️ المنتجات 📢 التسويق 🎨 تصميم المتجر 💳 طرق الدفع والمحفظة 🚛 إدارة الشحن والتوصيل 📱 تطبيق التاجر وتطبيق الجوال 🏪 كاشير سلة بوينت 🧩 التطبيقات المثبتة ومتجر التطبيقات

### Q7-SA-K1956

**Cited at:** section 1, line 11; section 2, line 66; section 3, line 100; section 3, line 103

**Record** (`studies/proposals/records/Q7/salla/copied.tsv`):
- concern_id: SA-C-163
- placement: decides
- structure: https://help.salla.sa/article/إضافة-عملة-جديدة-للمتجر/u4s3nz2yd3gxd92e8r4dpwbd
- identifier: الأسئلة الشائعة
- statement: عندما يتصفح العميل المتجر، يمكنه اختيار العملة المتاحة التي تناسبه من قائمة العملات بجوار سلة المشتريات في أعلى المتجر.
- cite_ids: SA-S-0155

**Citation SA-S-0155:** `https://help.salla.sa/article/إضافة-عملة-جديدة-للمتجر/u4s3nz2yd3gxd92e8r4dpwbd` | الأسئلة الشائعة (line 689 of the rendered text) | 2026-08-31 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/018-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:37Z, captured)
- quote: عندما يتصفح العميل المتجر، يمكنه اختيار العملة المتاحة التي تناسبه من قائمة العملات بجوار سلة المشتريات في أعلى المتجر.
- title: إضافة عملات جديدة وتفعيلها للمتجر | مركز المساعدة - سلة
- the page opens: إضافة عملات جديدة وتفعيلها للمتجر مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل ح…
- in context: … الرئيسية، اضغط (مركز الإعدادات). 2. من تبويب (عام)، اضغط (العملات). 3. عيّن العملات المتاحة في متجرك، ثم اضغط (حفظ). 1- عيّن العملة الحالية للمتجر. 2- فعّل حالة العملات المتاحة حسب حاجة متجرك. 3- اختر عملة جديدة، ثم اضغط (إضافة) لإضافة عملة إلى العملات المتاحة في متجرك. 🚀 الأسئلة الشائعة ❓هل يمكنني تغيير العملة الافتراضية للمتجر عندما أرغب بذلك؟ نعم، بشرط أن لا يكون هناك طلبات شراء للعملاء. ❓كيف يستطيع العميل اختيار العملة التي يُفضل الدفع بها؟ ⟪عندما يتصفح العميل المتجر، يمكنه اختيار العملة المتاحة التي تناسبه من قائمة العملات بجوار سلة المشتريات في أعلى المتجر.⟫ فتظهر له أسعار المنتجات بالعملة المختارة، بالشكل: 💡 توضيح مهم: عملة المتجر الافتراضية التي تظهر للعميل تعتمد على موقع العميل الجغرافي، وليست مرتبطة بالعملة الافتراضية المضافة داخل إعدادات المتجر. هذا يعني أن الأسعار قد تُعرض بعملة محلية مختلفة تلقائياً لتسهيل تجربة الشراء لدى عملائك من بلدان متعددة. اسأل, واطلب الدعم من التجار وفريق سلة. السابق التالي تصنيفات ذات صلة نطاق | دومين المتجر لغات المتجر والترجمة الفورية أقسام ذات صلة 🏡 الصفحة الرئيسي…

### Q7-SA-K1963

**Cited at:** section 1, line 12; section 1, line 17; section 2, line 69; section 7, line 146

**Record** (`studies/proposals/records/Q7/salla/copied.tsv`):
- concern_id: SA-C-164
- placement: decides
- structure: https://help.salla.sa/article/-إدارة-طرق-الدفع-وتفعيل-المدفوعات-الإلكترونية/dtdojcntv3f4lwqzj4h0jvij
- identifier: ثانياً: تخصيص المدفوعات الإلكترونية > دورة التحويل
- statement: 📝 ملاحظة: عند تفعيل التاجر لبوابة دفع سلة، يتم استقبال جميع المدفوعات بالريال السعودي.
- cite_ids: SA-S-0067

**Citation SA-S-0067:** `https://help.salla.sa/article/-إدارة-طرق-الدفع-وتفعيل-المدفوعات-الإلكترونية/dtdojcntv3f4lwqzj4h0jvij` | ثانياً: تخصيص المدفوعات الإلكترونية > دورة التحويل (line 744 of the rendered text) | 2026-08-22 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/013-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:32Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/014-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:46Z, captured)
- quote: 📝 ملاحظة: عند تفعيل التاجر لبوابة دفع سلة، يتم استقبال جميع المدفوعات بالريال السعودي.
- title: تفعيل طرق الدفع الإلكتروني في متجرك | مركز المساعدة - سلة
- the page opens: تفعيل طرق الدفع الإلكتروني في متجرك مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل…
- in context: …إعدادات الأساسية المطلوب ضبطها للمدفوعات الإلكترونية هي: 1. دورة التحويل: ما هي دورة تحويل المدفوعات الإلكترونية؟ هي عدد مرات تحويل المبالغ المستحقة والتي تمت عبر الدفع الإلكتروني على طلبات متجرك إلى حسابك البنكي. تنويه هام: الحد الأدنى لمجموع المبالغ التي يمكن تحويلها للتاجر هو 100 ريال. خطوات إعداد دورة التحويل: من صفحة طرق الدفع، من المدفوعات الإلكترونية، اضغط على (دورة التحويل). حدد دورة التحويل، واضغط (حفظ). وخيارات دورة التحويل المتاحة هي: ⟪📝 ملاحظة: عند تفعيل التاجر لبوابة دفع سلة، يتم استقبال جميع المدفوعات بالريال السعودي.⟫ لمزيد من التفاصيل حول دورة تحويل المدفوعات الإلكترونية 2. وسائل الدفع المفعلة: لتفعيل وسائل الدفع الإلكتروني في المدفوعات الإلكترونية اضغط على (وسائل الدفع المفعلة). فعّل وسائل الدفع الإلكتروني التي ترغب بها في متجرك واضغط على (حفظ). بمجرد تفعيل وسيلة الدفع مدى وفيزا سيتم تفعيل أبل باي تلقائياً. وستظهر طرق الدفع ووسائله كما في الشكل التالي: ويمكنك تعطيل المدفوعات الإلكترونية بشكل مؤقت عن طريق الضغط على (تعطيل) 3. قيود الدفع: اضبط وخصّص قيود الدف…

### Q7-SA-016

**Cited at:** section 1, line 18; section 2, line 72

**Record** (`studies/proposals/records/Q7/salla/statements.tsv`):
- stmt_id: Q7-SA-016
- bears_on: 1
- identifier: amounts.exchange_rate; scope_exchange_rate
- statement: "exchange_rate": { "base_currency": "KWD", "exchange_currency": "KWD", "rate": "1.00000000" }, "scope_exchange_rate": "12.13695338",
- scope: Orders Webhook Events Model (example payload)
- cite_ids: Q7-SA-C016
- from: held
- note: an example payload, not a schema description

**Citation Q7-SA-C016:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261005T234928Z-docs-md/fetch.warc.gz` | offset 204989 (https://docs.salla.dev/webhook-events/orders.md), ## Orders Webhook Events Model, example | 2026-10-05 | kind: stated | quote check: found
- quote: "exchange_rate": { "base_currency": "KWD", "exchange_currency": "KWD", "rate": "1.00000000" }, "scope_exchange_rate": "12.13695338",
- title: Order
- in context: …t_methods": [ { "amount": 146, "payment_method": "bank", "transaction_reference": null }, { "amount": 50, "payment_method": "customer_wallet", "transaction_reference": "30543" } ], "currency": "SAR", "amounts": { "sub_total": { "amount": 186, "currency": "SAR" }, "shipping_cost": { "amount": 15, "currency": "SAR" }, "cash_on_delivery": { "amount": 0, "currency": "SAR" }, "tax": { "percent": "0.00", "amount": { "amount": 0, "currency": "SAR" } }, ⟪"exchange_rate": { "base_currency": "KWD", "exchange_currency": "KWD", "rate": "1.00000000" }, "scope_exchange_rate": "12.13695338",⟫ "discounts": [ { "title": "new offer", "type": "special", "code": "new offer", "discount": "5.00", "discounted_shipping": 0 } ], "total": { "amount": 196, "currency": "SAR" } }, "shipping": { "id": 1833934431, "app_id": null, "company": "السعودية", "logo": "", "receiver": { "name": "Mohammed Ali", "email": "usertest@gmail.com", "phone": "999123456789" }, "shipper": { "name": "Demo", "company_name": "dev-wofftr4xsra5xtlv", "email": "wofftr4xsra5x…

### Q7-SA-K1964

**Cited at:** section 1, line 22; section 2, line 77; section 3, line 97; section 3, line 105; section 8, line 159

**The same record as Q2-SA-K1964,** whose card is in `Q2-salla.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: 4-الحساب لدى بنك إماراتي و بعملة الدرهم الإماراتي.
- scope: الإمارات

### Q7-SA-023

**Cited at:** section 1, line 22

**Record** (`studies/proposals/records/Q7/salla/statements.tsv`):
- stmt_id: Q7-SA-023
- bears_on: 1;4
- identifier: GET /admin/v2/store-wallet/wallet/summary: data.latest_payment.epayment
- statement: "epayment":{"is_available":true,"id":811079824,"transaction_number":6871605,"type":"epayment","status":"paid","status_label":"Paid","due_date":"Sunday 11 October 2026","due_date_format":"1 day ago","due_amount":5171.76,"send_date":"2026-10-11","send_date_humans":"1 day ago","amount":5171.76,"currency":"SAR","is_over_limit":false,"hint":"It will reach your account within 2-4 business days."}
- scope: store real-merchant, observed 2026-10-12; "merchant_type":"KSA" (GET /admin/v2/gateways/payment, same run, step 42)
- cite_ids: Q7-SA-C027;Q7-SA-C028;Q7-SA-C018
- from: held
- note: shows, for this store, part of what Q7-SA-G0151 and Q7-SA-G0153 ask: the currency of a paid payout of the electronic payments balance; not where it is set

**Citation Q7-SA-C027:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/0614.json` | GET api.salla.dev/admin/v2/store-wallet/wallet/summary, store real-merchant, step 17, data.latest_payment | 2026-10-12 | kind: observed | quote check: found
- quote: "epayment":{"is_available":true,"id":811079824,"transaction_number":6871605,"type":"epayment","status":"paid","status_label":"Paid","due_date":"Sunday 11 October 2026"
- in context: {"status":200,"success":true,"data":{"total_balance":1760.33,"currency":"SAR","store_validation":{"is_store_documented":true,"is_store_verified":true,"has_active_bank_account":true,"iban_number":"SA0380000572608016281444"},"latest_payment":{⟪"epayment":{"is_available":true,"id":811079824,"transaction_number":6871605,"type":"epayment","status":"paid","status_label":"Paid","due_date":"Sunday 11 October 2026"⟫,"due_date_format":"1 day ago","due_amount":5171.76,"send_date":"2026-10-11","send_date_humans":"1 day ago","amount":5171.76,"currency":"SAR","is_over_limit":false,"hint":"It will reach your account within 2-4 business days."},"cod":{"is_available":false,"id":null,"transaction_number":null,"type":"cod","status":null,"status_label":null,"due_date":null,"due_date_format":null,"due_amount":0,"send_date":null,"send_date_humans":null,"amount":0,"curre…

**Citation Q7-SA-C028:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/0614.json` | GET api.salla.dev/admin/v2/store-wallet/wallet/summary, store real-merchant, step 17, data.latest_payment | 2026-10-12 | kind: observed | quote check: found
- quote: "due_amount":5171.76,"send_date":"2026-10-11","send_date_humans":"1 day ago","amount":5171.76,"currency":"SAR","is_over_limit":false,"hint":"It will reach your account within 2-4 business days."}
- title, opening and note boxes: as for this source's citation above
- in context: {"status":200,"success":true,"data":{"total_balance":1760.33,"currency":"SAR","store_validation":{"is_store_documented":true,"is_store_verified":true,"has_active_bank_account":true,"iban_number":"SA0380000572608016281444"},"latest_payment":{"epayment":{"is_available":true,"id":811079824,"transaction_number":6871605,"type":"epayment","status":"paid","status_label":"Paid","due_date":"Sunday 11 October 2026","due_date_format":"1 day ago",⟪"due_amount":5171.76,"send_date":"2026-10-11","send_date_humans":"1 day ago","amount":5171.76,"currency":"SAR","is_over_limit":false,"hint":"It will reach your account within 2-4 business days."}⟫,"cod":{"is_available":false,"id":null,"transaction_number":null,"type":"cod","status":null,"status_label":null,"due_date":null,"due_date_format":null,"due_amount":0,"send_date":null,"send_date_humans":null,"amount":0,"currency":"SAR","is_over_limit":false,"hint":null}},"payout_schedule_message":null,"payout_schedule_messages":{"epayment":"Your funds are transferred every 48 hours when the balance exceeds 100 SAR.","cod":"Your cash-on-delivery pa…

**Citation Q7-SA-C018:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/1488.json` | GET api.salla.dev/admin/v2/gateways/payment, store real-merchant, step 42 | 2026-10-12 | kind: observed | quote check: found
- quote: "merchant_type":"KSA"
- in context: {"status":200,"success":true,"data":{"master":{"epayment_enabled":true},"is_first_time_setup":false,"verification":{"status":"completed","is_owner":false,"blocks_payment_activation":false,"verify_url":"https:\/\/s.salla.sa\/entity\/verification\/verify","summary":{"store_documented":true,"kyc_complete":false,"has_approved_epayment_request":true},"rejection":null},⟪"merchant_type":"KSA"⟫,"quick_methods":[{"slug":"mada","is_enabled":true,"is_available":true,"is_effective":true,"blocked_by":null,"unavailable_reason":null,"has_advance_settings":false,"label":"\u0645\u062f\u0649","logo":"https:\/\/cdn.assets.salla.network\/prod\/admin\/cp\/assets\/images\/mada.png","description":null,"fees":{"percentage":1,"flat_amount":"1.00","currency":"SAR"},"limits":null,"advance_settings_state":null,"next_action_url":null,"verification_status":…

### Q7-SA-031

**Cited at:** section 1, line 28; section 2, line 64

**Record** (`studies/proposals/records/Q7/salla/statements.tsv`):
- stmt_id: Q7-SA-031
- bears_on: 1;3
- identifier: GET /admin/v2/currencies/available: data[] (country_code YE)
- statement: {"id": 1784627537, "country_name_en": "Yemen", "country_name_ar": "اليمن", "country_code": "YE", "currency_code": "YER", "currency_name_en": "Rials", "currency_name_ar": "ريال يمني"}
- scope: store demo, observed 2026-10-09
- cite_ids: Q7-SA-C036
- from: held
- note: one item of a list of 31; the same answer was received by store real-merchant in run 20261012T010906Z-sweep-real-merchant-full-en, step 306

**Citation Q7-SA-C036:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261009T033607Z-sweep-settings-demo-en/responses/1441.json` | GET api.salla.dev/admin/v2/currencies/available, store demo, step 24, data[] | 2026-10-09 | kind: observed | quote check: found
- quote: {"id": 1784627537, "country_name_en": "Yemen", "country_name_ar": "اليمن", "country_code": "YE", "currency_code": "YER", "currency_name_en": "Rials", "currency_name_ar": "ريال يمني"}
- in context: …rency_code": "SGD", "currency_name_en": "Dollars", "currency_name_ar": "Dollars"}, {"id": 195201146, "country_name_en": "Tunisia", "country_name_ar": "تونس", "country_code": "TN", "currency_code": "TND", "currency_name_en": null, "currency_name_ar": "دينار تونسي"}, {"id": 928298564, "country_name_en": "Turkey", "country_name_ar": "تركيا", "country_code": "TR", "currency_code": "TRY", "currency_name_en": "Lira", "currency_name_ar": "ليرة تركية"}, ⟪{"id": 1784627537, "country_name_en": "Yemen", "country_name_ar": "اليمن", "country_code": "YE", "currency_code": "YER", "currency_name_en": "Rials", "currency_name_ar": "ريال يمني"}⟫, {"id": 369266515, "country_name_en": "South Africa", "country_name_ar": "جنوب أفريقيا", "country_code": "ZA", "currency_code": "ZAR", "currency_name_en": "Rand", "currency_name_ar": "Rand"}]} {"status": 200, "success": true, "data": [{"id": 1473353380, "country_name_en": "Andorra", "country_name_ar": "اندورا", "country_code": "AD", "currency_code": "EUR", "currency_name_en": "Euro", "currency_name_ar": "يورو"}, {"id": 566146469, "country_name_e…

### Q7-SA-K1950

**Cited at:** section 1, line 35; section 3, line 102

**Record** (`studies/proposals/records/Q7/salla/copied.tsv`):
- concern_id: SA-C-163
- placement: decides
- structure: observed-sa@145f137:structures/salla/staff-permission-groups/demo@en/items.jsonl
- identifier: currency_setting_edit
- statement: "label": "store setting edit social media account"}, {"id": 16435258, "name": "currency_setting_edit", "label": "currency setting edit"}, {"id": 1318388567, "name": "domain_management", "label": "domain management"}, {"id": 410133072, "name": "restore_data_management"
- cite_ids: SA-S-2388
- note: Staff permission, group إعدادات المتجر.

**Citation SA-S-2388:** `observed-sa@145f137:structures/salla/staff-permission-groups/demo@en/items.jsonl` | line 11 (group إعدادات المتجر) | 2026-10-08 | kind: observed | quote check: found
- quote: "label": "store setting edit social media account"}, {"id": 16435258, "name": "currency_setting_edit", "label": "currency setting edit"}, {"id": 1318388567, "name": "domain_management", "label": "domain management"}, {"id": 410133072, "name": "restore_data_management"
- in context: …on": 9} {"id": 1904445108, "name": "إعدادات المتجر", "label": "إعدادات المتجر", "permissions": [{"id": 1309137353, "name": "store_setting_browse", "label": "store setting browse"}, {"id": 468515018, "name": "store_setting_edit_basic_info", "label": "store setting edit basic info"}, {"id": 1976109003, "name": "store_setting_edit_setting", "label": "store setting edit setting"}, {"id": 1201022676, "name": "store_setting_edit_social_media_account", ⟪"label": "store setting edit social media account"}, {"id": 16435258, "name": "currency_setting_edit", "label": "currency setting edit"}, {"id": 1318388567, "name": "domain_management", "label": "domain management"}, {"id": 410133072, "name": "restore_data_management"⟫, "label": "restore data management"}, {"id": 1957673870, "name": "store_setting_purchase_from_salla_store", "label": "store setting purchase from salla store"}, {"id": 1182063247, "name": "shipping_options_management", "label": "shipping options management"}, {"id": 273807752, "name": "wallet_and_invoices_management", "label": "wallet and invoices management"}, {"id": 1648236681, "name": "register_fields_management", "label": "register fields ma…

### Q7-SA-004

**Cited at:** section 1, line 36; section 1, line 37; section 1, line 40; section 2, line 81

**Record** (`studies/proposals/records/Q7/salla/statements.tsv`):
- stmt_id: Q7-SA-004
- bears_on: 3
- identifier: ❓هل يمكنني تغيير العملة الافتراضية للمتجر عندما أرغب بذلك؟
- statement: نعم ، بشرط أن لا يكون هناك طلبات شراء للعملاء.
- cite_ids: Q7-SA-C004
- from: held

**Citation Q7-SA-C004:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 134 (article u4s3nz2yd3gxd92e8r4dpwbd, إضافة عملة جديدة للمتجر), 🚀 الأسئلة الشائعة | 2026-08-31 | kind: stated | quote check: found
- quote: نعم ، بشرط أن لا يكون هناك طلبات شراء للعملاء.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …: - خطوات إضافة العملات إلى المتجر - الأسئلة الشائعة 🚀 خطوات إضافة العملات إلى المتجر 1. من القائمة الرئيسية، اضغط (مركز الإعدادات). 2. من تبويب ( عام )، اضغط (العملات). 3. عيّن العملات المتاحة في متجرك، ثم اضغط (حفظ). 1- عيّن العملة الحالية للمتجر. 2- فعّل حالة العملات المتاحة حسب حاجة متجرك. 3- اختر عملة جديدة، ثم اضغط (إضافة) لإضافة عملة إلى العملات المتاحة في متجرك. 🚀 الأسئلة الشائعة ❓هل يمكنني تغيير العملة الافتراضية للمتجر عندما أرغب بذلك؟ ⟪نعم ، بشرط أن لا يكون هناك طلبات شراء للعملاء.⟫ ❓كيف يستطيع العميل اختيار العملة التي يُفضل الدفع بها؟ عندما يتصفح العميل المتجر، يمكنه اختيار العملة المتاحة التي تناسبه من قائمة العملات بجوار سلة المشتريات في أعلى المتجر. فتظهر له أسعار المنتجات بالعملة المختارة، بالشكل: 💡 توضيح مهم: عملة المتجر الافتراضية التي تظهر للعميل تعتمد على موقع العميل الجغرافي، وليست مرتبطة بالعملة الافتراضية المضافة داخل إعدادات المتجر. هذا يعني أن الأسعار قد تُعرض بعملة محلية مختلفة تلقائياً لتسهيل تجربة الشراء ل…

### Q7-SA-K1560

**Cited at:** section 1, line 51; section 2, line 80; section 7, line 147; section 8, line 159

**Record** (`studies/proposals/records/Q7/salla/copied.tsv`):
- concern_id: SA-C-111
- placement: boundary
- structure: https://help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الإمارات-سلة/nvs6bt51hvlweulqzayp3o76
- identifier: الأسئلة الشائعة
- statement: لا. رصيد المتجر مخصص لاشتراكات سلة وخدماتها ومشترياتها، بينما يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها.
- scope: الإمارات
- cite_ids: SA-S-0083

**Citation SA-S-0083:** `https://help.salla.sa/article/تحويلات-مدفوعات-سلة-والتسويات-في-الإمارات-سلة/nvs6bt51hvlweulqzayp3o76` | الأسئلة الشائعة (line 843 of the rendered text) | 2026-09-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/items/021-help.salla.sa/text.txt` (fetched 2026-10-10T23:51:40Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/018-help.salla.sa/text.txt` (fetched 2026-10-12T10:49:52Z, captured)
- quote: لا. رصيد المتجر مخصص لاشتراكات سلة وخدماتها ومشترياتها، بينما يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها.
- title: تحويلات مدفوعات سلة والتسويات في الإمارات | سلة | مركز المساعدة - سلة
- the page opens: Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حلول تقنية متقدمة لنمو أعمال كبار التجار المدفوعات طرق …
- in context: …لمدفوعات الإلكترونية المؤهل 250 درهمًا إماراتيًا. ماذا يحدث إذا كان رصيدي أقل من 250 درهمًا؟ يبقى المبلغ في رصيد المدفوعات الإلكترونية حتى يتجاوز الحد الأدنى، ثم يُضمّن في دورة التحويل التالية. إلى أي حساب بنكي تصل التحويلات؟ إلى الحساب البنكي المستخدم أثناء توثيق المتجر. هل يمكنني تغيير الحساب البنكي المستخدم للتحويلات؟ نعم. أرسل بيانات بنكية محدثة من خلال التوثيق، ثم تواصل مع دعم سلة للمساعدة. هل رصيد المتجر هو نفسه رصيد المدفوعات الإلكترونية؟ ⟪لا. رصيد المتجر مخصص لاشتراكات سلة وخدماتها ومشترياتها، بينما يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها.⟫ كيف تُحتسب رسوم المدفوعات الإلكترونية؟ وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق المتجر. اسأل, واطلب الدعم من التجار وفريق سلة. السابق التالي تصنيفات ذات صلة أساسيات في طرق الدفع وسائل الدفع الآجل المحافظ الرقمية وسائل الدفع الأخرى أقسام ذات صلة 🏡 الصفحة الرئيسية 📦 الطلبات 🏷️ المنتجات 📢 التسويق 🎨 تصميم المتجر 🚛 إدارة الشحن والتوصيل 📱 تطبيق التاجر وتطبيق الجوال 🏪 كاشير سلة بوينت 🧩 التطبيقات المثبتة ومتجر التطبيقات

### Q7-SA-022

**Cited at:** section 1, line 51; section 2, line 79; section 5, line 122; section 8, line 159

**Record** (`studies/proposals/records/Q7/salla/statements.tsv`):
- stmt_id: Q7-SA-022
- bears_on: 4
- identifier: GET /admin/v2/store-wallet/wallet/summary: data.wallets[] (type, name, balance, currency)
- statement: "wallets":[{"type":"default","name":"Wallet","balance":69.96,"currency":"SAR","can_withdraw":true,"metadata":{"wallet_id":"140877344","disable_balance_draw":false,"is_withdraw_over_limit":0,"wallet_withdrawal_enabled":false,"withdraw_disabled_reason":null,"withdraw_disabled_message":null,"store_bank_account_exist":true,"is_store_documented":true,"daily_limit":"5008.05","total_deposits":27687.47,"total_withdrawals":27617.51}},{"type":"salla_pay","name":"Electronic Payments","balance":1690.37,"currency":"SAR","can_withdraw":true,"metadata":{"enable_transfer_balance":true,"is_balance_frozen":false,"day_amount_balance":0,"max_total_to_generate":100,"total_excluding_fees_and_tax":1690.37,"total_fees":23.15,"total_tax":3.48,"total_including_fees_and_tax":1717}},{"type":"salla_cod","name":"Cash on Delivery Payments","balance":0,"currency":"SAR","can_withdraw":true,"metadata":{"max_total_to_generate":100,"total_excluding_fees_and_tax":0,"total_fees":0,"total_tax":0,"total_including_fees_and_tax":0}}]
- scope: store real-merchant, observed 2026-10-12; "merchant_type":"KSA" (GET /admin/v2/gateways/payment, same run, step 42)
- cite_ids: Q7-SA-C024;Q7-SA-C025;Q7-SA-C026;Q7-SA-C018
- from: held
- note: the full list the answer gives: three wallets

**Citation Q7-SA-C024:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/0614.json` | GET api.salla.dev/admin/v2/store-wallet/wallet/summary, store real-merchant, step 17, data.wallets | 2026-10-12 | kind: observed | quote check: found
- quote: {"type":"default","name":"Wallet","balance":69.96,"currency":"SAR","can_withdraw":true,"metadata":{"wallet_id":"140877344","disable_balance_draw":false,"is_withdraw_over_limit":0,"wallet_withdrawal_enabled":false,"withdraw_disabled_reason":null,"withdraw_disabled_message":null
- in context: …er":null,"type":"cod","status":null,"status_label":null,"due_date":null,"due_date_format":null,"due_amount":0,"send_date":null,"send_date_humans":null,"amount":0,"currency":"SAR","is_over_limit":false,"hint":null}},"payout_schedule_message":null,"payout_schedule_messages":{"epayment":"Your funds are transferred every 48 hours when the balance exceeds 100 SAR.","cod":"Your cash-on-delivery payouts are sent every Sunday and Wednesday."},"wallets":[⟪{"type":"default","name":"Wallet","balance":69.96,"currency":"SAR","can_withdraw":true,"metadata":{"wallet_id":"140877344","disable_balance_draw":false,"is_withdraw_over_limit":0,"wallet_withdrawal_enabled":false,"withdraw_disabled_reason":null,"withdraw_disabled_message":null⟫,"store_bank_account_exist":true,"is_store_documented":true,"daily_limit":"5008.05","total_deposits":27687.47,"total_withdrawals":27617.51}},{"type":"salla_pay","name":"Electronic Payments","balance":1690.37,"currency":"SAR","can_withdraw":true,"metadata":{"enable_transfer_balance":true,"is_balance_frozen":false,"day_amount_balance":0,"max_total_to_generate":100,"total_excluding_fees_and_tax":1690.37,"total_fees":23.15,"total_tax":3.48,"total_inc…

**Citation Q7-SA-C025:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/0614.json` | GET api.salla.dev/admin/v2/store-wallet/wallet/summary, store real-merchant, step 17, data.wallets | 2026-10-12 | kind: observed | quote check: found
- quote: {"type":"salla_pay","name":"Electronic Payments","balance":1690.37,"currency":"SAR","can_withdraw":true,"metadata":{"enable_transfer_balance":true,"is_balance_frozen":false,"day_amount_balance":0,"max_total_to_generate":100,"total_excluding_fees_and_tax":1690.37,"total_fees":23.15
- title, opening and note boxes: as for this source's citation above
- in context: …day and Wednesday."},"wallets":[{"type":"default","name":"Wallet","balance":69.96,"currency":"SAR","can_withdraw":true,"metadata":{"wallet_id":"140877344","disable_balance_draw":false,"is_withdraw_over_limit":0,"wallet_withdrawal_enabled":false,"withdraw_disabled_reason":null,"withdraw_disabled_message":null,"store_bank_account_exist":true,"is_store_documented":true,"daily_limit":"5008.05","total_deposits":27687.47,"total_withdrawals":27617.51}},⟪{"type":"salla_pay","name":"Electronic Payments","balance":1690.37,"currency":"SAR","can_withdraw":true,"metadata":{"enable_transfer_balance":true,"is_balance_frozen":false,"day_amount_balance":0,"max_total_to_generate":100,"total_excluding_fees_and_tax":1690.37,"total_fees":23.15⟫,"total_tax":3.48,"total_including_fees_and_tax":1717}},{"type":"salla_cod","name":"Cash on Delivery Payments","balance":0,"currency":"SAR","can_withdraw":true,"metadata":{"max_total_to_generate":100,"total_excluding_fees_and_tax":0,"total_fees":0,"total_tax":0,"total_including_fees_and_tax":0}}]}}

**Citation Q7-SA-C026:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/0614.json` | GET api.salla.dev/admin/v2/store-wallet/wallet/summary, store real-merchant, step 17, data.wallets | 2026-10-12 | kind: observed | quote check: found
- quote: {"type":"salla_cod","name":"Cash on Delivery Payments","balance":0,"currency":"SAR","can_withdraw":true,"metadata":{"max_total_to_generate":100,"total_excluding_fees_and_tax":0,"total_fees":0,"total_tax":0
- title, opening and note boxes: as for this source's citation above
- in context: …true,"is_store_documented":true,"daily_limit":"5008.05","total_deposits":27687.47,"total_withdrawals":27617.51}},{"type":"salla_pay","name":"Electronic Payments","balance":1690.37,"currency":"SAR","can_withdraw":true,"metadata":{"enable_transfer_balance":true,"is_balance_frozen":false,"day_amount_balance":0,"max_total_to_generate":100,"total_excluding_fees_and_tax":1690.37,"total_fees":23.15,"total_tax":3.48,"total_including_fees_and_tax":1717}},⟪{"type":"salla_cod","name":"Cash on Delivery Payments","balance":0,"currency":"SAR","can_withdraw":true,"metadata":{"max_total_to_generate":100,"total_excluding_fees_and_tax":0,"total_fees":0,"total_tax":0⟫,"total_including_fees_and_tax":0}}]}}

**Citation Q7-SA-C018:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:raw/runs/20261012T010906Z-sweep-real-merchant-full-en/responses/1488.json` | GET api.salla.dev/admin/v2/gateways/payment, store real-merchant, step 42 | 2026-10-12 | kind: observed | quote check: found
- quote: "merchant_type":"KSA"
- in context: {"status":200,"success":true,"data":{"master":{"epayment_enabled":true},"is_first_time_setup":false,"verification":{"status":"completed","is_owner":false,"blocks_payment_activation":false,"verify_url":"https:\/\/s.salla.sa\/entity\/verification\/verify","summary":{"store_documented":true,"kyc_complete":false,"has_approved_epayment_request":true},"rejection":null},⟪"merchant_type":"KSA"⟫,"quick_methods":[{"slug":"mada","is_enabled":true,"is_available":true,"is_effective":true,"blocked_by":null,"unavailable_reason":null,"has_advance_settings":false,"label":"\u0645\u062f\u0649","logo":"https:\/\/cdn.assets.salla.network\/prod\/admin\/cp\/assets\/images\/mada.png","description":null,"fees":{"percentage":1,"flat_amount":"1.00","currency":"SAR"},"limits":null,"advance_settings_state":null,"next_action_url":null,"verification_status":…

### Q7-SA-P0079

**Cited at:** section 7, line 153

**The same record as Q2-SA-P0079,** whose card is in `Q2-salla.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: توفّر منصة سلة عبر شركائها نظام الدفع والسداد في منصة سلّة فيمكن أن يتم عبر الانترنت كلياً من خلال خيارات الدفع المتوفرة على منصة سلّة أو من خلال أي طريقة دفع توفرها منصة سلّة من حين لآخر.
- scope: 
