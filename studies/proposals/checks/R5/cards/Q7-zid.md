# Cards: Q7 on zid

16 records cited by `studies/proposals/drafts/Q7/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - Prices held: Shopify, Zid, WooCommerce and BigCommerce hold a seller's own prices in one currency per store, and match on role (basis 4). Shopify's store currency is the one "for pricing products and running reports"; Zid's العملة الأساسية is "العملة التي تم إدخال أسعار المنتجات باستخدامها"; WooCommerce allows "one base currency per store", and "WooCommerce uses it to display product prices and record new orders"; BigCommerce's default currency is "assigned during store creation, is always a transactional currency". Salla's seller sets the store's current currency, but the words read don't say prices are entered in it, so Salla's match is partial. Q7-SH-K1935 Q7-ZD-002 Q7-WC-K0745 Q7-WC-K0747 Q7-BC-013 Q7-SA-001
- **section 1, line 8:** - Below the store, Zid also holds prices per market, set for each market and channel "وبعملة السوق نفسها". WooCommerce's reading didn't show groups of countries below the store with their own currency and prices. Q7-ZD-019 Q7-WC-N16
- **section 1, line 9:** - Amounts: Zid passes an amount to payment providers "in the smallest currency unit"; Shopify's MoneyBag carries `shopMoney` and `presentmentMoney` side by side; WooCommerce's shipped code records an order's currency "in ISO format". Not checked on Salla, for Zid's amount unit (Q7-ZD-024). Q7-ZD-024 Q7-SH-123 Q7-WC-055
- **section 1, line 10:** - Shown to buyers: Shopify and Zid set the shown currency per market, and match on role (basis 4). Shopify's currency customization "determines what currency is displayed to customers in that market"; Zid's عملة السوق is the currency "لعرض أسعار المنتجات داخل هذا السوق". WooCommerce keeps one list for the whole store, its "Enabled currencies". Q7-SH-076 Q7-ZD-K0236 Q7-WC-013
- **section 1, line 16:** - Zid: with مدفوعات زد the buyer sees the chosen currency, but "في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر", except كي نت, paid in Kuwaiti dinar (help, 3 August 2026). Its Zid Pay help (6 August 2026) says خاصية العملات allows "استقبال المدفوعات من عملات مختلفة في زد باي". The two aren't reconciled in what was read, and the proposal rests on neither for what Zid charges. Q7-ZD-P0149 Q7-ZD-004
- **section 1, line 18:** - Each order records its currency, and four record the store's currency or a rate beside it, matching on role (basis 4): Shopify's order has `presentmentCurrencyCode`, and its MoneyBag holds both amounts; Zid's order gives the "Exchange rate of the store currency relative to the order currency"; BigCommerce's has `currency_code`, `default_currency_code` and `currency_exchange_rate`; Salla's an `exchange_rate` with `base_currency`, `exchange_currency` and `rate`; WooCommerce's a single "Currency the order was created with, in ISO format." (shipped code; the others stated). Q7-SH-124 Q7-SH-123 Q7-ZD-010 Q7-BC-020 Q7-SA-016 Q7-WC-055
- **section 1, line 27:** - A store's own currency is set for the store, by the seller, with a default from the store's country; Zid, WooCommerce and BigCommerce match on role (basis 4). Zid asks for it "بناء على عملة دولتك"; WooCommerce's onboarding sets `woocommerce_currency` from the country's `currency_code` (shipped code); BigCommerce's default currency "is assigned based on your location" (stated). Q7-ZD-001 Q7-WC-054 Q7-BC-029
- **section 1, line 29:** - A market takes its default currency from its countries or its place: a Shopify market for one country is "automatically set to that country's local currency" (not checked on Salla, Q7-SH-079); Zid shows "السوق الافتراضي وهو السوق المحلي" (stated). On store demo-fake-dev-store (30 September 2026, observed), saved markup held, for a market including Saudi Arabia, Saudi Riyal (SAR) as "Recommended" above an "All currencies" list marking Yemeni Rial (YER) as "Store currency"; and, on a draft order for the market Yemen, "Market currency" Yemeni Rial (YER) with eight "Other currencies". Q7-SH-079 Q7-ZD-020 Q7-SH-202 Q7-SH-203 Q7-SH-201
- **section 1, line 37:** - A change treats prices in one of three ways: Q7-SH-006 Q7-ZD-K0302 Q7-SA-004
- **section 1, line 39:** - Zid converts: "عند تغيير العملة سيتم تحويل أسعار المنتجات إلى العملة الجديدة بناءً على سعر الصرف في وقت التغيير". Q7-ZD-K0302
- **section 1, line 41:** - What is already recorded: WooCommerce's "Orders placed before the change keep the currency and symbol they were placed in, and their totals stay the same." Zid's help says instead "سيتم تحويل المبيعات إلى العملة الجديدة بناءً على سعر الصرف في تلك اللحظة", so total sales may change. Q7-WC-027 Q7-ZD-003
- **section 1, line 52:** - Zid: Zid Pay may add the amount due to the merchant's balance, "إضافة المبلغ المستحق لرصيد التاجر"; the pages read don't name that balance's currency (not checked on BigCommerce). For cash on delivery through its shipping service, Zid collects from buyers and transfers "إجمالي المستحقات إلى محفظة التاجر". Its terms say the wallet is "محددة بالريال السعودي كعملة أساسية" for merchants outside Saudi Arabia, while Gulf merchants use it "بالعملة المحلية لبلدهم". Q7-ZD-K0033 Q7-ZD-N01 Q7-ZD-K0117 Q7-ZD-P0122
- **section 2, line 57:** - **Currency table**. Proposed: each currency Sharrwah supports is a row of data, with its code, the size of its smallest unit and its symbol; a currency is added, renamed or retired by changing rows, not code. Q7-ZD-024 Q7-WC-055
- **section 2, line 59:** - **Money amount**. Proposed: every stored amount is a whole number of its currency's smallest unit, with that currency's code; a converted amount keeps the original, the result and the rate between them. Q7-ZD-024 Q7-SH-123
- **section 2, line 60:** - From the platforms: the unit from Zid, and the pair from Shopify's MoneyBag, which holds the shop's and the customer's amounts. Why: rule 3, as changing how amounts are stored after launch would touch every order and balance. Q7-ZD-024 Q7-SH-123
- **section 2, line 61:** - **Store currency**. Proposed: each store has exactly one, in which the seller's prices are entered and reports run. The seller picks it when creating the store, from those its place allows, with the place's default preselected. Q7-WC-K0745 Q7-SH-K1935 Q7-ZD-001
- **section 2, line 62:** - From the platforms: one currency per store for a seller's prices (Shopify, Zid, WooCommerce, BigCommerce), with a default from the store's country (Zid, WooCommerce, BigCommerce). Why: rule 1, as the default and choices come from **place currency settings**, not a build per place; and rule 3, as each **order currency record** converts to it. Q7-ZD-002 Q7-BC-013 Q7-WC-054 Q7-BC-029
- **section 2, line 63:** - **Place currency settings**. Proposed: for each place it serves, Sharrwah sets a default currency and the currencies a store there may price in, show, charge in and be paid out in; the last two are also bounded by the **provider currency capability** of the providers connected there. Q7-ZD-001 Q7-WC-054
- **section 2, line 65:** - **Market**, with its **display currency**. Proposed: a group of buyer countries within one store, with one display currency, other currencies its buyers may pick, and, optionally, its own prices in its own currency. Every store starts with one market for its own place, in the store currency. A buyer is placed by country, then may pick among the market's currencies. Q7-SH-076 Q7-ZD-K0236 Q7-ZD-020
- **section 2, line 66:** - From the platforms: Shopify's currency per market and one-country default; Zid's market currency, local default market and prices "وبعملة السوق نفسها"; Salla's default by location and the buyer's own pick. Why: rule 1, as one store is set up for each place it sells to; and rule 3, as the level at which prices and currencies sit is part of the data model. Q7-SH-079 Q7-ZD-019 Q7-SA-K1957 Q7-SA-K1956
- **section 2, line 71:** - **Order currency record**. Proposed: an order records, when placed, the charged currency and every amount in it, the same amounts in the store currency, the display currency if different, and each rate used, with its source and time; none is recomputed. A refund goes out in the charged currency, any conversion of it at that day's rate, recorded beside the first. Q7-SH-123 Q7-ZD-010 Q7-BC-020
- **section 2, line 73:** - Not taken: converting recorded sales at the rate of the moment the store currency changes, as Zid's help describes; reports may convert, but an order keeps its amounts. Q7-ZD-003
- **section 2, line 79:** - From the platforms: per-currency balances (Shopify, WooCommerce, BigCommerce), Salla's wallets, each with a currency (store real-merchant, 12 October 2026, observed), and Zid's wallet, its currency set by country. Why: rule 3. Q7-SA-022 Q7-ZD-P0122
- **section 2, line 80:** - The guard: the ledger records balances and holds no money. Any arrangement in which Sharrwah holds sellers' money, or a payment company holds it in an account opened through Sharrwah, as Salla's رصيد المدفوعات الإلكترونية and Zid's wallet hold their sellers' proceeds, goes live only by the founder's decision. Q7-SA-K1560 Q7-ZD-K0117
- **section 2, line 82:** - From the platforms: Salla's bar once there are orders; Shopify's owner-only change; prices kept by number (Shopify, BigCommerce) or converted (Zid); Shopify's Bulgaria change, made on its stores' behalf, and WooCommerce's routine rewriting orders' currency code. Why: rule 3, as a later change mustn't rewrite an order's currency; and rule 4, as the treatment of prices stays open (section 5). Q7-SH-006 Q7-BC-053 Q7-ZD-K0302 Q7-SH-107 Q7-WC-057
- **section 3, line 92:** - Per place: the default and allowed currencies, in **place currency settings**, as the country gives the default on Zid, WooCommerce and BigCommerce. Q7-ZD-001 Q7-BC-029
- **section 3, line 94:** - Per market: the **display currency**, its other currencies and its own prices, as Shopify and Zid set them per market. Q7-SH-076 Q7-ZD-019
- **section 3, line 98:** - Per order: the charged currency, the store-currency amounts and the rates, fixed when it is placed. Q7-ZD-010 Q7-WC-027
- **section 5, line 122:** - Who holds a seller's money before payout, and in which currency. The records name such balances' currencies only in part (section 1, [4]). Keep the **seller ledger** apart from whatever account holds the money, so the design fits a provider holding it, an arrangement through Sharrwah, or none. Settled by: the founder's decision under the guard, and the providers' contracts. Q7-SA-022 Q7-ZD-P0122 Q7-SH-N01
- **section 5, line 125:** - How a **currency migration** treats prices: converted at a stated rate, as Zid's help describes, or kept by number, as Shopify and BigCommerce say. Keep the **order currency record** self-contained, so either fits. Settled by: the first migration Sharrwah needs. Q7-ZD-K0302 Q7-SH-006
- **section 7, line 147:** - Whether any arrangement holds sellers' money through Sharrwah, by Sharrwah itself or a payment company in an account opened through Sharrwah, and in which currency: the founder's decision, under the guard. Q7-SA-K1560 Q7-ZD-P0122
- **section 7, line 149:** - In which currency Sharrwah bills its own fees at each place. BigCommerce's terms say "Fees are payable in U.S. Dollars, unless otherwise specified."; Zid's put its fees in Saudi riyals or the merchant's local currency. Q7-BC-K0177 Q7-ZD-K0156
- **section 8, line 159:** - What the records show: Shopify and WooCommerce define the payout currency in the same terms, and BigCommerce's settlement currency matches it on role (basis 4). It is set for the payment account: by region or business entity on Shopify, with more currencies on some plans; by country on WooCommerce; through the provider on BigCommerce; by the country's banks on Salla. Balances before payout are kept per currency on Shopify, WooCommerce and BigCommerce. Salla's balance holds sales proceeds before transfer; the page naming its currency wasn't read, and the run on store real-merchant gave the store's wallets in SAR (12 October 2026, observed). Zid's terms set its wallet's currency by the merchant's country; the currency of Zid Pay's balance and deposits, and of Shopify's reserved funds, wasn't in what was read. S01-VP-23 Q7-SH-004 Q7-WC-004 Q7-BC-P0014 Q7-SH-012 Q7-SH-K1268 Q7-SH-P0155 Q7-WC-K0739 Q7-BC-P0016 Q7-SA-K1964 Q7-SH-131 Q7-WC-048 Q7-BC-058 Q7-SA-K1560 Q7-SA-G0151 Q7-SA-022 Q7-ZD-P0122 Q7-ZD-N01 Q7-ZD-N02 Q7-SH-N01
- **section 8, line 162:** - Zid's list of currencies whose wallet balances can't be withdrawn names only what can't be withdrawn, so it names no currency in which the wallet is held or paid out. No reading here rests on it. S01-VP-23 Q7-ZD-P0123

## The cards

### Q7-ZD-002

**Cited at:** section 1, line 7; section 2, line 62

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-002
- bears_on: 1;3
- identifier: العملة الأساسية
- statement: العملة الأساسية هي العملة التي تم إدخال أسعار المنتجات باستخدامها، عند التعديل يرجى مراعاة القيام بتعديل أسعار جميع المنتجات للعملة الأساسية الجديدة.
- cite_ids: Q7-ZD-C002
- from: held

**Citation Q7-ZD-C002:** `https://help.zid.sa/store-language/` | ملاحظة | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:31Z, captured)
- quote: العملة الأساسية هي العملة التي تم إدخال أسعار المنتجات باستخدامها، عند التعديل يرجى مراعاة القيام بتعديل أسعار جميع المنتجات للعملة الأساسية الجديدة.
- title: زد - مركز المساعدة - لغة وعملات المتجر ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - لغة وعملات المتجر ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة عام الإعدادات لغة وعملات المتجر ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المن…
- in context: …ملات أخرى غير العملة الأساسية (الريال السعودي \ الدينار الكويتي) بالمتجر ، سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر (الريال السعودي\ الدينار الكويتي) لجميع الشبكات ما عدا "كي نت" سيتم الدفع بالدينار الكويتي. عند تغيير العملة سيتم تحويل أسعار المنتجات إلى العملة الجديدة بناءً على سعر الصرف في وقت التغيير، ونتيجة لذلك قد يحصل تغيير في مجموع المبيعات. ⟪العملة الأساسية هي العملة التي تم إدخال أسعار المنتجات باستخدامها، عند التعديل يرجى مراعاة القيام بتعديل أسعار جميع المنتجات للعملة الأساسية الجديدة.⟫ عند تفعيل عملة دولة يتم تفعيل الشحن إليها. لمزيد من المعلومات يرجى الإطلاع على الفديو التالي: سوف تتعلم: تفعيل اللغة الإنجليزية تحديد اللغة الأساسية للمتجر تفعيل العملات التقييمات والمراجعات 0 0 من أصل 5 نجوم (بناءً على 0 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars 1 Star إرسال التقييم اعدادات الامان (لوحة التحكم الجديدة ) إضافة عميل (لوحة التحكم الجديدة ) تواصل معنا هل تحتاج إلى مساعد…

### Q7-ZD-019

**Cited at:** section 1, line 8; section 2, line 66; section 3, line 94

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-019
- bears_on: 1;2
- identifier: عملة السوق
- statement: حيث يمكن تحديد سعر مخصص لكل سوق وقناة وبعملة السوق نفسها، دون الاعتماد على سعر عالمي واحد أو التحويل التلقائي للعملات.
- cite_ids: Q7-ZD-C020
- from: held

**Citation Q7-ZD-C020:** `https://help.zid.sa/markets/` | الأسواق ( لوحة التحكم الجديدة ) | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/136-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:08Z, captured)
- quote: حيث يمكن تحديد سعر مخصص لكل سوق وقناة وبعملة السوق نفسها، دون الاعتماد على سعر عالمي واحد أو التحويل التلقائي للعملات.
- title: زد - مركز المساعدة - الأسواق ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - الأسواق ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة عام الإعدادات الأسواق ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون -…
- in context: …لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال عام الأسواق ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 3, 2026 تتيح خاصية الأسواق للتاجر إدارة أسعار المنتجات وتوفّرها حسب كل سوق جغرافي بشكل مستقل. ⟪حيث يمكن تحديد سعر مخصص لكل سوق وقناة وبعملة السوق نفسها، دون الاعتماد على سعر عالمي واحد أو التحويل التلقائي للعملات.⟫ يمكنك الوصول الى خاصية الأسواق من خلال : الاعدادات > الأسواق ملاحظة : خاصية الأسواق تتيح لك عدد من الأسواق حسب باقتك: باقة الانطلاقة سوق واحد افتراضي باقة النمو سوقين افتراضي وجديد الباقة الاحترافية خمس أسواق خاصية الأسواق : في الصفحة الأولى سيظهر لك السوق الافتراضي وهو السوق المحلي بشكل تلقائي أيقونة الإجراءات قم بالضغط على ايقونة الإجراءات وهي الايقونة المحتوية على ثلاث نقاط في الإجراءات الخاصة بالسوق ستتمكن من : إضافة منتج تخصيص الثيم إدارة ا…

### Q7-ZD-024

**Cited at:** section 1, line 9; section 2, line 57; section 2, line 59; section 2, line 60

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-024
- bears_on: 1
- identifier: POST /{ProviderUrl}/payments > amount
- statement: Total payment amount in the smallest currency unit. For SAR, amount is provided in Halala (1 SAR = 100 Halalas).
- scope: Zid Payments Open APIs, Execute Payment Request
- cite_ids: Q7-ZD-C025
- from: live

**Citation Q7-ZD-C025:** `https://docs.zid.sa/execute-payment-request-17112105e0.md` | requestBody > amount | 2026-10-19 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261019T003327Z-proposals-Q7-zid/items/001-docs.zid.sa/text.txt` (fetched 2026-10-19T00:33:27Z, captured)
- quote: Total payment amount in the smallest currency unit. For SAR, amount is provided in Halala (1 SAR = 100 Halalas).
- title: Execute Payment Request
- the page opens: OpenAPI Specification yaml openapi: 3.0.1 info: title: '' description: '' version: 1.0.0 paths: /{ProviderUrl}/payments: post: summary: Execute Payment Request deprecated: false description: >- This is the request that is going to be sent from Zid Payments to you as a payment provider for creating / executing payments. tags: - Default module/Payment API/Payment parameters: - name: ProviderUrl in: path description: >- The base URL of the payment provider's API. ZidPay will use this URL to send re…
- headings: Execute Payment Request > OpenAPI Specification
- in context: …rization header using Basic Authentication. The value should be the secret key provided by the payment provider during merchant onboarding. required: true example: 'Authorization: Basic secret_key' schema: type: string requestBody: content: application/json: schema: type: object title: CreatePaymentRequestDto description: >- Request body for executing a payment via ZidPay to the payment provider. properties: amount: type: integer description: >- ⟪Total payment amount in the smallest currency unit. For SAR, amount is provided in Halala (1 SAR = 100 Halalas).⟫ examples: - 24900 currency: type: string description: Currency code in ISO 4217 format. examples: - SAR callbackUrl: type: string description: >- The URL to which the provider should redirect or send confirmation after a successful payment. examples: - >- https://zidpay.org/api/payment/98bbb6fb-bbd7-41cb-8d5f-f8854b13c9b1/ThirdPartyCallback errorUrl: type: string description: >- The URL to which the provider should redirect or notify in case of …

### Q7-ZD-K0236

**Cited at:** section 1, line 10; section 2, line 65

**Record** (`studies/proposals/records/Q7/zid/copied.tsv`):
- concern_id: ZD-C-034
- placement: decides
- structure: help.zid.sa article: الأسواق ( لوحة التحكم الجديدة )
- identifier: عملة السوق
- statement: عملة السوق: حدّد العملة التي سيتم اعتمادها لعرض أسعار المنتجات داخل هذا السوق.
- cite_ids: ZD-S-0750

**Citation ZD-S-0750:** `https://help.zid.sa/markets/` | خطوات إنشاء السوق | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/136-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:08Z, captured)
- quote: عملة السوق: حدّد العملة التي سيتم اعتمادها لعرض أسعار المنتجات داخل هذا السوق.
- title: زد - مركز المساعدة - الأسواق ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - الأسواق ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة عام الإعدادات الأسواق ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون -…
- in context: …نجليزية أيضًا. الدول المرتبطة بالسوق. عملة السوق. إنشاء سوق جديد: لإنشاء سوق جديد من الصفحة الرئيسية الخاصة بالسوق قم بالضغط على ايقونة إنشاء خطوات إنشاء السوق : 1. تفاصيل السوق في هذه الخطوة، قم بإدخال المعلومات الأساسية للسوق الذي ترغب بإنشائه، وذلك كما يلي: اسم السوق (باللغة العربية): أدخل اسم السوق لتمييزه داخلياً و في حال تفعيل اللغة الإنجليزية، ستتمكن من تخصيص اسم السوق باللغة الإنجليزية أيضًا. الدول: اختر الدول التي سيتم ربطها بهذا السوق. ⟪عملة السوق: حدّد العملة التي سيتم اعتمادها لعرض أسعار المنتجات داخل هذا السوق.⟫ بعد التأكد من إدخال جميع البيانات بشكل صحيح، اضغط على التالي للانتقال إلى الخطوة التالية. 2. إضافة المنتجات في خطوة إضافة المنتجات ، قم بإدخال المنتجات التي ترغب بإضافتها للسوق عن طريق الضغط على ايقونة إضافة منتجات بعد ذلك ، حدد المنتجات بعد الانتهاء من إدخال المنتجات التي تمت إضافتها إلى السوق، ثم يمكنك الانتقال إلى الخطوة التالية لاستكمال الإعدادات. 2. إعداد الأسعار حدد طريقة إعداد السعر نسخ الأسعار من السوق الرئيسي كما هي مع استخدام عملة السو…

### Q7-ZD-P0149

**Cited at:** section 1, line 16

**Record** (`studies/proposals/records/Q7/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-148
- bullet: e;end-payment
- placement: decides
- identifier: اللغات والعملات > ملاحظة (help.zid.sa/store-language)
- statement: في حال تم تفعيل المدفوعات لزد [ مدفوعات زد متاحة لتجار السعودية و الكويت] كخيار دفع إلكتروني وتم تفعيل عملات أخرى غير العملة الأساسية (الريال السعودي \ الدينار الكويتي) بالمتجر ، سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر (الريال السعودي\ الدينار الكويتي) لجميع الشبكات ما عدا “كي نت” سيتم الدفع بالدينار الكويتي.
- scope: تجار السعودية و الكويت
- conditions: S01-ZD-001;S01-ZD-002;S01-ZD-003;S01-ZD-004;S01-ZD-005;S01-ZD-006;S01-ZD-007;S01-ZD-008;S01-ZD-009;S01-ZD-010;S01-ZD-011;S01-ZD-012;S01-ZD-013;S01-ZD-014;S01-ZD-015;S01-ZD-016;S01-ZD-017;S01-ZD-019;S01-ZD-020;S01-ZD-021;S01-ZD-022;S01-ZD-023;S01-ZD-024;S01-ZD-025;S01-ZD-026;S01-ZD-027;S01-ZD-028;S01-ZD-029;S01-ZD-030;S01-ZD-031;S01-ZD-032;S01-ZD-033;S01-ZD-034;S01-ZD-035;S01-ZD-037;S01-ZD-038;S01-ZD-039;S01-ZD-040;S01-ZD-041;S01-ZD-043;S01-ZD-044;S01-ZD-045;S01-ZD-046;S01-ZD-047;S01-ZD-061;S01-ZD-066;S01-ZD-068;S01-ZD-095;S01-ZD-152;S01-ZD-157
- cite_ids: S01-ZD-C368;S01-ZD-C369;S01-ZD-C370
- from: new
- note: Phase A3 (audit of S01-ZD-N01). The parts in brackets with a backslash, (الريال السعودي \ الدينار الكويتي), are not quoted.

**Citation S01-ZD-C368:** `sharrwah-knowledge-map@a920665d3307544df27207fd40905340d9eaadfe:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt` | لتفعيل العملة الرئيسية للمتجر أو إضافة عملات أخرى > ملاحظة | 2026-08-03 | kind: stated | quote check: found
- quote: في حال تم تفعيل المدفوعات لزد [ مدفوعات زد متاحة لتجار السعودية و الكويت] كخيار دفع إلكتروني
- the page opens: الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا الدخول لمتجرك close الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا مركز المساعدة عام الإعدادات لغة وعملات المتجر ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال عام لغة وعملات المتجر ( لوحة ا…
- in context: … تفعيل اللغة لا يعد ترجمة تلقائية للغة العربية بل يتحتم عليك كتابة جميع ما يتم إضافته مرة أخرى باللغة الانجليزية. لتفعيل العملة الرئيسية للمتجر أو إضافة عملات أخرى من خلال: لوحة التحكم > الاعدادات > اللغات والعملات قم باختيار و تفعيل العملة الأساسية للمتجر بناء على عملة دولتك ، وفي حال أردت إضافة مزيد من العملات الأخرى قم بتفعيلها بالضغط على أيقونة تفعيل وبإمكانك تحديد العملة الأساسية بالمتجر من خلال الضغط على أيقونة اختيار كعملة أساسية. ملاحظة: ⟪في حال تم تفعيل المدفوعات لزد [ مدفوعات زد متاحة لتجار السعودية و الكويت] كخيار دفع إلكتروني⟫ وتم تفعيل عملات أخرى غير العملة الأساسية (الريال السعودي \ الدينار الكويتي) بالمتجر ، سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر (الريال السعودي\ الدينار الكويتي) لجميع الشبكات ما عدا "كي نت" سيتم الدفع بالدينار الكويتي. عند تغيير العملة سيتم تحويل أسعار المنتجات إلى العملة الجديدة بناءً على سعر الصرف في وقت التغيير، ونتيجة لذلك قد يحصل تغيير في مجمو…

**Citation S01-ZD-C369:** `sharrwah-knowledge-map@a920665d3307544df27207fd40905340d9eaadfe:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt` | لتفعيل العملة الرئيسية للمتجر أو إضافة عملات أخرى > ملاحظة | 2026-08-03 | kind: stated | quote check: found
- quote: سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر
- title, opening and note boxes: as for this source's citation above
- in context: …لتحكم > الاعدادات > اللغات والعملات قم باختيار و تفعيل العملة الأساسية للمتجر بناء على عملة دولتك ، وفي حال أردت إضافة مزيد من العملات الأخرى قم بتفعيلها بالضغط على أيقونة تفعيل وبإمكانك تحديد العملة الأساسية بالمتجر من خلال الضغط على أيقونة اختيار كعملة أساسية. ملاحظة: في حال تم تفعيل المدفوعات لزد [ مدفوعات زد متاحة لتجار السعودية و الكويت] كخيار دفع إلكتروني وتم تفعيل عملات أخرى غير العملة الأساسية (الريال السعودي \ الدينار الكويتي) بالمتجر ، ⟪سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر⟫ (الريال السعودي\ الدينار الكويتي) لجميع الشبكات ما عدا "كي نت" سيتم الدفع بالدينار الكويتي. عند تغيير العملة سيتم تحويل أسعار المنتجات إلى العملة الجديدة بناءً على سعر الصرف في وقت التغيير، ونتيجة لذلك قد يحصل تغيير في مجموع المبيعات. العملة الأساسية هي العملة التي تم إدخال أسعار المنتجات باستخدامها، عند التعديل يرجى مراعاة القيام بتعديل أسعار جميع المنتجات للعملة الأساسية الجديدة. عند تفعيل عملة دولة يتم تفعيل الشحن إليها. لمزيد من المعلومات ير…

**Citation S01-ZD-C370:** `sharrwah-knowledge-map@a920665d3307544df27207fd40905340d9eaadfe:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt` | لتفعيل العملة الرئيسية للمتجر أو إضافة عملات أخرى > ملاحظة | 2026-08-03 | kind: stated | quote check: found
- quote: لجميع الشبكات ما عدا “كي نت” سيتم الدفع بالدينار الكويتي.
- title, opening and note boxes: as for this source's citation above
- in context: …عيل وبإمكانك تحديد العملة الأساسية بالمتجر من خلال الضغط على أيقونة اختيار كعملة أساسية. ملاحظة: في حال تم تفعيل المدفوعات لزد [ مدفوعات زد متاحة لتجار السعودية و الكويت] كخيار دفع إلكتروني وتم تفعيل عملات أخرى غير العملة الأساسية (الريال السعودي \ الدينار الكويتي) بالمتجر ، سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر (الريال السعودي\ الدينار الكويتي) ⟪لجميع الشبكات ما عدا "كي نت" سيتم الدفع بالدينار الكويتي.⟫ عند تغيير العملة سيتم تحويل أسعار المنتجات إلى العملة الجديدة بناءً على سعر الصرف في وقت التغيير، ونتيجة لذلك قد يحصل تغيير في مجموع المبيعات. العملة الأساسية هي العملة التي تم إدخال أسعار المنتجات باستخدامها، عند التعديل يرجى مراعاة القيام بتعديل أسعار جميع المنتجات للعملة الأساسية الجديدة. عند تفعيل عملة دولة يتم تفعيل الشحن إليها. لمزيد من المعلومات يرجى الإطلاع على الفديو التالي: سوف تتعلم: تفعيل اللغة الإنجليزية تحديد اللغة الأساسية للمتجر …

### Q7-ZD-004

**Cited at:** section 1, line 16

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-004
- bears_on: 1;2
- identifier: خاصية العملات
- statement: تتيح لك هذه الخاصية إمكانية استقبال المدفوعات من عملات مختلفة في زد باي عن طريق تفعيل خاصية العملات في إعدادات المتجر.
- scope: زد باي
- cite_ids: Q7-ZD-C004
- from: held

**Citation Q7-ZD-C004:** `https://help.zid.sa/zidpay_staff_and_currencies/` | خاصية العملات | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/184-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:56Z, captured)
- quote: تتيح لك هذه الخاصية إمكانية استقبال المدفوعات من عملات مختلفة في زد باي عن طريق تفعيل خاصية العملات في إعدادات المتجر.
- title: زد - مركز المساعدة - صلاحيات فريق العمل و خاصية العملات
- the page opens: زد - مركز المساعدة - صلاحيات فريق العمل و خاصية العملات menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي صلاحيات فريق العمل و خاصية العملات عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة الم…
- in context: …شبكات الدفع. قائمة العمليات : من خلال هذه الصفحة بإمكانك تحديد صلاحية الاطلاع على كافة العمليات (الناجحة | الفاشلة | الملغاة) و تفاصيلها. استرداد المبالغ : من خلال هذه الخاصية بامكانك تحديد صلاحية استرداد المبالغ بشكل ( كلي | جزئي) للعميل النهائي. كشف الحساب : من خلال هذه الصفحة بإمكانك تحديد صلاحية الاطلاع على التفاصيل المالية للعمليات الناجحة وعمليات الإيداعات التي تتمثل ب 3 مراحل ( تم الايداع - قيد المعالجة - لم يتم الإيداع ). خاصية العملات : ⟪تتيح لك هذه الخاصية إمكانية استقبال المدفوعات من عملات مختلفة في زد باي عن طريق تفعيل خاصية العملات في إعدادات المتجر.⟫ ملاحظة: المبلغ المدفوع خاضع لتحويل سعر الصرف لبوابة الدفع المفعلة. سوف تتعلم: صلاحيات فريق العمل خاصية العملات التقييمات والمراجعات 0 0 من أصل 5 نجوم (بناءً على 0 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars 1 Star إرسال التقييم المنتجات الرقمية و إيداع المبالغ زد كاشير | إنشاء طلب من المتجر تواصل معنا هل تحتاج إلى مساعدة إضافية؟ تواصل معنا لماذا زد لماذا ابدأ مع زد؟ لماذا أنتقل إلى زد؟…

### Q7-ZD-010

**Cited at:** section 1, line 18; section 2, line 71; section 3, line 98

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-010
- bears_on: 1
- identifier: currency.order_store_currency.exchange_rate
- statement: Exchange rate of the store currency relative to the order currency. Typically 1 when both currencies are the same.
- cite_ids: Q7-ZD-C010
- from: held

**Citation Q7-ZD-C010:** `https://docs.zid.sa/view-order-12479054e0.md` | DefaultOrderCurrencySerializer > order_store_currency > exchange_rate | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/067-docs.zid.sa/text.txt` (fetched 2026-10-12T04:52:05Z, captured)
- quote: Exchange rate of the store currency relative to the order currency. Typically 1 when both currencies are the same.
- title: View Order
- the page opens: OpenAPI Specification yaml openapi: 3.0.1 info: title: '' description: '' version: 1.0.0 paths: /v1/managers/store/orders/{order-id}/view: get: summary: View Order deprecated: false description: > Get a specific order by ID. Optionally, when source is provided, the previous_order and next_order fields will be computed among only those orders whose source matches one of the values.:::info[] Currency Handling for Orders When the store currency, order currency, and the currency of the shipping addr…
- headings: View Order > OpenAPI Specification
- in context: … store currency. nullable: true required: - id - code - exchange_rate x-apidog-orders: - id - code - exchange_rate description: Represents the currency in which the order was placed and paid. x-apidog-ignore-properties: [] order_store_currency: type: object properties: id: type: integer description: Unique identifier of the store currency. code: type: string description: ISO currency code of the store. exchange_rate: type: number description: >- ⟪Exchange rate of the store currency relative to the order currency. Typically 1 when both currencies are the same.⟫ nullable: true required: - id - code - exchange_rate x-apidog-orders: - id - code - exchange_rate description: Represents the store's base currency. x-apidog-ignore-properties: [] required: - order_currency - order_store_currency x-apidog-orders: - order_currency - order_store_currency x-apidog-ignore-properties: [] x-apidog-folder: '' OrderReversePresenter: type: object properties: id: type: string description: Unique identifier of the reverse …

### Q7-ZD-001

**Cited at:** section 1, line 27; section 2, line 61; section 2, line 63; section 3, line 92

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-001
- bears_on: 1;2
- identifier: لوحة التحكم > الاعدادات > اللغات والعملات
- statement: قم باختيار و تفعيل العملة الأساسية للمتجر بناء على عملة دولتك ، وفي حال أردت إضافة مزيد من العملات الأخرى قم بتفعيلها بالضغط على أيقونة تفعيل وبإمكانك تحديد العملة الأساسية بالمتجر من خلال الضغط على أيقونة اختيار كعملة أساسية.
- cite_ids: Q7-ZD-C001
- from: held

**Citation Q7-ZD-C001:** `https://help.zid.sa/store-language/` | العملات | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:31Z, captured)
- quote: قم باختيار و تفعيل العملة الأساسية للمتجر بناء على عملة دولتك ، وفي حال أردت إضافة مزيد من العملات الأخرى قم بتفعيلها بالضغط على أيقونة تفعيل وبإمكانك تحديد العملة الأساسية بالمتجر من خلال الضغط على أيقونة اختيار كعملة أساسية.
- title: زد - مركز المساعدة - لغة وعملات المتجر ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - لغة وعملات المتجر ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة عام الإعدادات لغة وعملات المتجر ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المن…
- in context: … على ذلك قد يكون هناك تغيير في إجمالي المبيعات ملاحظة: عند تفعيل اللغة الإنجليزية سيتوجب عليك عند إضافة بيانات المنتج أو بيانات المتجر مثل (من نحن وسياسة الشروط والأحكام وسياسة الاسترجاع وغيرها) وكتابتها مرة أخرى باللغة الإنجليزية. حيث تفعيل اللغة لا يعد ترجمة تلقائية للغة العربية بل يتحتم عليك كتابة جميع ما يتم إضافته مرة أخرى باللغة الانجليزية. لتفعيل العملة الرئيسية للمتجر أو إضافة عملات أخرى من خلال: لوحة التحكم > الاعدادات > اللغات والعملات ⟪قم باختيار و تفعيل العملة الأساسية للمتجر بناء على عملة دولتك ، وفي حال أردت إضافة مزيد من العملات الأخرى قم بتفعيلها بالضغط على أيقونة تفعيل وبإمكانك تحديد العملة الأساسية بالمتجر من خلال الضغط على أيقونة اختيار كعملة أساسية.⟫ ملاحظة: في حال تم تفعيل المدفوعات لزد [ مدفوعات زد متاحة لتجار السعودية و الكويت] كخيار دفع إلكتروني وتم تفعيل عملات أخرى غير العملة الأساسية (الريال السعودي \ الدينار الكويتي) بالمتجر ، سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر (الريال السعودي\ الدينار الكويتي) لجميع الشبكات ما عدا "كي نت" سيتم الدفع بالدينار الكويتي. عند تغيير العملة سيتم تحويل أس…

### Q7-ZD-020

**Cited at:** section 1, line 29; section 2, line 65

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-020
- bears_on: 2
- identifier: السوق الافتراضي
- statement: في الصفحة الأولى سيظهر لك السوق الافتراضي وهو السوق المحلي بشكل تلقائي
- cite_ids: Q7-ZD-C021
- from: held

**Citation Q7-ZD-C021:** `https://help.zid.sa/markets/` | خاصية الأسواق | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/136-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:08Z, captured)
- quote: في الصفحة الأولى سيظهر لك السوق الافتراضي وهو السوق المحلي بشكل تلقائي
- title: زد - مركز المساعدة - الأسواق ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - الأسواق ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة عام الإعدادات الأسواق ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون -…
- in context: …حديث August 3, 2026 تتيح خاصية الأسواق للتاجر إدارة أسعار المنتجات وتوفّرها حسب كل سوق جغرافي بشكل مستقل. حيث يمكن تحديد سعر مخصص لكل سوق وقناة وبعملة السوق نفسها، دون الاعتماد على سعر عالمي واحد أو التحويل التلقائي للعملات. يمكنك الوصول الى خاصية الأسواق من خلال : الاعدادات > الأسواق ملاحظة : خاصية الأسواق تتيح لك عدد من الأسواق حسب باقتك: باقة الانطلاقة سوق واحد افتراضي باقة النمو سوقين افتراضي وجديد الباقة الاحترافية خمس أسواق خاصية الأسواق : ⟪في الصفحة الأولى سيظهر لك السوق الافتراضي وهو السوق المحلي بشكل تلقائي⟫ أيقونة الإجراءات قم بالضغط على ايقونة الإجراءات وهي الايقونة المحتوية على ثلاث نقاط في الإجراءات الخاصة بالسوق ستتمكن من : إضافة منتج تخصيص الثيم إدارة السوق لإدارة الأسواق، يرجى اتباع الخطوات التالية: قم بالضغط على أيقونة إدارة الأسواق. بعد ذلك، أدخل تفاصيل السوق المطلوبة، والتي تشمل: اسم السوق (باللغة العربية)، وفي حال تفعيل اللغة الإنجليزية ستتمكن من إدخال اسم السوق باللغة الإنجليزية أيضًا. الدول المرتبطة بالسوق. عملة السوق. إنشاء سوق جديد: ل…

### Q7-ZD-K0302

**Cited at:** section 1, line 37; section 1, line 39; section 2, line 82; section 5, line 125

**The same record as Q1-ZD-K0302,** whose card is in `Q1-zid.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: عند تغيير العملة سيتم تحويل أسعار المنتجات إلى العملة الجديدة بناءً على سعر الصرف في وقت التغيير، ونتيجة لذلك قد يحصل تغيير في مجموع المبيعات.
- scope: 

### Q7-ZD-003

**Cited at:** section 1, line 41; section 2, line 73

**Record** (`studies/proposals/records/Q7/zid/statements.tsv`):
- stmt_id: Q7-ZD-003
- bears_on: 3
- identifier: ملاحظة: تغيير العملة
- statement: عند تغيير العملة، سيتم تحويل المبيعات إلى العملة الجديدة بناءً على سعر الصرف في تلك اللحظة وبناءً على ذلك قد يكون هناك تغيير في إجمالي المبيعات
- cite_ids: Q7-ZD-C003
- from: held
- note: The same page also holds the wording copied as Q7-ZD-K0302, which speaks of أسعار المنتجات; this note speaks of المبيعات.

**Citation Q7-ZD-C003:** `https://help.zid.sa/store-language/` | ملاحظة | 2026-08-03 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/159-help.zid.sa/text.txt` (fetched 2026-10-12T04:53:31Z, captured)
- quote: عند تغيير العملة، سيتم تحويل المبيعات إلى العملة الجديدة بناءً على سعر الصرف في تلك اللحظة وبناءً على ذلك قد يكون هناك تغيير في إجمالي المبيعات
- title: زد - مركز المساعدة - لغة وعملات المتجر ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - لغة وعملات المتجر ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة عام الإعدادات لغة وعملات المتجر ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المن…
- in context: …لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 3, 2026 إن توفير أكثر من لغة و عملة في المتجر الالكتروني يعتبر فرصة ممتازة لزيادة أرباحك و رفع مبيعاتك و يسهل الوصول إلى قدر أكبر من العملاء ويساعد في الانتشار و تحسين ظهور متجرك في محركات البحث. بإمكانك تفعيل اللغة الإنجليزية لعملائك من خلال : لوحة التحكم > الضغط على أيقونة الاعدادات . بعد ذلك اللغات والعملات . من خانة اللغات ، قم بتفعيل اللغة الإنجليزية وسيتم تحويلها تلقائيا ملاحظة: ⟪عند تغيير العملة، سيتم تحويل المبيعات إلى العملة الجديدة بناءً على سعر الصرف في تلك اللحظة وبناءً على ذلك قد يكون هناك تغيير في إجمالي المبيعات⟫ ملاحظة: عند تفعيل اللغة الإنجليزية سيتوجب عليك عند إضافة بيانات المنتج أو بيانات المتجر مثل (من نحن وسياسة الشروط والأحكام وسياسة الاسترجاع وغيرها) وكتابتها مرة أخرى باللغة الإنجليزية. حيث تفعيل اللغة لا يعد ترجمة تلقائية للغة العربية بل يتحتم عليك كتابة جميع ما يتم إضافته مرة أخرى باللغة الانجليزية. لتفعيل العملة الرئيسية للمتجر أو إضافة عملات أخرى من خلال: لوحة التحكم > الاعدادات > اللغات والعملات قم باختيار و تفعيل العملة الأساسية للمتجر بناء…

### Q7-ZD-K0033

**Cited at:** section 1, line 52

**Record** (`studies/proposals/records/Q7/zid/copied.tsv`):
- concern_id: ZD-C-003
- placement: responsible
- structure: شروط وأحكام زد باي, Saudi Arabia (zid.sa/ar/legal/zidpay-terms-conditions-sa)
- identifier: رصيد التاجر
- statement: يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.
- scope: Zid Pay, Saudi Arabia
- cite_ids: ZD-S-0555

**Citation ZD-S-0555:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | تسوية المدفوعات وعملية الاسترداد | 2025-01-21 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (fetched 2026-10-12T04:53:55Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (fetched 2026-10-12T10:51:28Z, captured)
- quote: يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.
- title: Zid | Create your online store with modern retail services
- in context: …د الأموال". قد تقوم زد باي بحجز مبلغ احتياطي يحسب من حجم معاملات العملاء ذوى المخاطر العالية. يتم تسوية هذا المبلغ الاحتياطي عند إغلاق الحسابات في حالة عدم استخدامها. يجوز لزد باي رد المبالغ إلى مصادرها والتي لم يتم تحويلها إلى الحساب البنكي للمستخدم لمدة أكثر من ١٤يوم وذلك لعدم قدرة المستخدم على تقديم بيانات صالحة وعليه يعتبر حسابه مهمل مما يترتب عليه إيقاف الحساب. قد تحتجز زد باي المبالغ المعلقة أو تسلمها إلى جهات أخرى وفقًا لتقدير زد باي فقط. ⟪يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.⟫ يجوز لزد باي ومزودو الخدمة باقتطاع رسوم رمزية على إجمالي العملية. يلتزم المستخدم بدفع أي رسوم غير مسددة خلال خمسة أيام عمل. التصديق على التوقيعات والإشعارات الإلكترونية تمثل الموافقة على تسجيل حساب في زد باي توقيعك الإلكتروني وتعتبر مراسلتنا من خلال خيار الدعم على الإيميل ([email protected]) يعتبر بمثابة إشعار رسمي منك وتعادل توقيعك الشخصي. الموافقة على أن البريد الإلكتروني المستخدم للتسجيل حساب في زد باي هو بريدك الإلكتروني المعتمد وأن كافة الم…

### Q7-ZD-K0117

**Cited at:** section 1, line 52; section 2, line 80

**The same record as Q4-ZD-K0117,** whose card is in `Q4-zid.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع.
- scope: الشحن المباشر (زد شب)

### Q7-ZD-P0122

**Cited at:** section 1, line 52; section 2, line 79; section 5, line 122; section 7, line 147; section 8, line 159

**Record** (`studies/proposals/records/Q7/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-121
- bullet: e
- placement: decides
- identifier: الشروط والأحكام > محفظة زد > بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية
- statement: استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية، ويُستثنى من ذلك التجار في دول مجلس التعاون الخليجي (مملكة البحرين، دولة الكويت، سلطنة عُمان، دولة الإمارات العربية المتحدة، ودولة قطر)، حيث يُتاح لهم تفعيل، شحن، واستخدام رصيد المحفظة بالعملة المحلية لبلدهم.
- scope: التجار خارج المملكة
- conditions: S01-ZD-057;S01-ZD-058;S01-ZD-059;S01-ZD-060;S01-ZD-061;S01-ZD-062;S01-ZD-064;S01-ZD-065;S01-ZD-150;S01-ZD-151
- cite_ids: S01-ZD-C290;S01-ZD-C291
- from: index:ZD-C-017:ZD-S-0654

**Citation S01-ZD-C290:** `https://zid.sa/ar/legal/terms-conditions/` | بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (fetched 2026-10-12T04:53:53Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (fetched 2026-10-12T10:51:26Z, captured)
- quote: استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية، ويُستثنى من ذلك التجار في دول مجلس التعاون الخليجي
- title: Zid | Create your online store with modern retail services
- in context: …د اتخاذ الإجراءات التالية: سحب المبالغ من رصيد المحفظة. سحب أي مبالغ فور إيداعها في المحفظة، حتى تسديد المستحقات بالكامل. سحب المبالغ المستحقة من رصيد التاجر في زد باي. إرسال إشعار كتابي رسمي للتاجر يتضمن تفاصيل المستحقات ومهلة لا تقل عن ثلاثين (30) يوماً لتسويتها. في حال عدم الالتزام بالسداد خلال المهلة المحددة، يحق لزد اتخاذ الإجراءات القضائية اللازمة للمطالبة بالمستحقات. بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية ⟪استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية، ويُستثنى من ذلك التجار في دول مجلس التعاون الخليجي⟫ (مملكة البحرين، دولة الكويت، سلطنة عُمان، دولة الإمارات العربية المتحدة، ودولة قطر)، حيث يُتاح لهم تفعيل، شحن، واستخدام رصيد المحفظة بالعملة المحلية لبلدهم. يقر التاجر بأنه لا يمكن سحب المبالغ المالية المتاحة في المحفظة للعملات التالية: (الريال العماني، الدرهم الإماراتي، الدينار الكويتي، والدينار البحريني). في حال قيام التاجر بنقل أو تغيير دولته في إعدادات المتجر إلى دولة أخرى، يشترط تصفير رصيد المحفظة أولاً، وفي حال وجود رصيد يتعذر سحبه أو التص…

**Citation S01-ZD-C291:** `https://zid.sa/ar/legal/terms-conditions/` | محفظة زد، بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (fetched 2026-10-12T04:53:53Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (fetched 2026-10-12T10:51:26Z, captured)
- quote: (مملكة البحرين، دولة الكويت، سلطنة عُمان، دولة الإمارات العربية المتحدة، ودولة قطر)، حيث يُتاح لهم تفعيل، شحن، واستخدام رصيد المحفظة بالعملة المحلية لبلدهم.
- title: Zid | Create your online store with modern retail services
- in context: …لمستحقة من رصيد التاجر في زد باي. إرسال إشعار كتابي رسمي للتاجر يتضمن تفاصيل المستحقات ومهلة لا تقل عن ثلاثين (30) يوماً لتسويتها. في حال عدم الالتزام بالسداد خلال المهلة المحددة، يحق لزد اتخاذ الإجراءات القضائية اللازمة للمطالبة بالمستحقات. بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية، ويُستثنى من ذلك التجار في دول مجلس التعاون الخليجي ⟪(مملكة البحرين، دولة الكويت، سلطنة عُمان، دولة الإمارات العربية المتحدة، ودولة قطر)، حيث يُتاح لهم تفعيل، شحن، واستخدام رصيد المحفظة بالعملة المحلية لبلدهم.⟫ يقر التاجر بأنه لا يمكن سحب المبالغ المالية المتاحة في المحفظة للعملات التالية: (الريال العماني، الدرهم الإماراتي، الدينار الكويتي، والدينار البحريني). في حال قيام التاجر بنقل أو تغيير دولته في إعدادات المتجر إلى دولة أخرى، يشترط تصفير رصيد المحفظة أولاً، وفي حال وجود رصيد يتعذر سحبه أو التصرف فيه، يلزم رفع طلب خاص لمعالجته عن طريق فريق خدمة العملاء. يُعد استخدام التاجر للخدمة، موافقة على هذه الشروط والأحكام، ومنحاً للأذونات اللازمة لتنفيذها. خد…

### Q7-ZD-K0156

**Cited at:** section 7, line 149

**The same record as Q1-ZD-K0156,** whose card is in `Q1-zid.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: جميع الرسوم تكون بالريال السعودي أو بعملة التاجر المحلية ويجب أن تكون جميع المدفوعات بالعملة المحلية.
- scope: 

### Q7-ZD-P0123

**Cited at:** section 8, line 162

**Record** (`studies/proposals/records/Q7/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-122
- bullet: c;e
- placement: decides
- identifier: الشروط والأحكام > محفظة زد > بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية
- statement: يقر التاجر بأنه لا يمكن سحب المبالغ المالية المتاحة في المحفظة للعملات التالية: (الريال العماني، الدرهم الإماراتي، الدينار الكويتي، والدينار البحريني).
- scope: التجار خارج المملكة
- conditions: S01-ZD-057;S01-ZD-058;S01-ZD-059;S01-ZD-060;S01-ZD-061;S01-ZD-062;S01-ZD-064;S01-ZD-065;S01-ZD-150;S01-ZD-151
- cite_ids: S01-ZD-C292
- from: index:ZD-C-017:ZD-S-0655

**Citation S01-ZD-C292:** `https://zid.sa/ar/legal/terms-conditions/` | بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (fetched 2026-10-12T04:53:53Z, captured)
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (fetched 2026-10-12T10:51:26Z, captured)
- quote: يقر التاجر بأنه لا يمكن سحب المبالغ المالية المتاحة في المحفظة للعملات التالية: (الريال العماني، الدرهم الإماراتي، الدينار الكويتي، والدينار البحريني).
- title: Zid | Create your online store with modern retail services
- in context: …د خلال المهلة المحددة، يحق لزد اتخاذ الإجراءات القضائية اللازمة للمطالبة بالمستحقات. بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية، ويُستثنى من ذلك التجار في دول مجلس التعاون الخليجي (مملكة البحرين، دولة الكويت، سلطنة عُمان، دولة الإمارات العربية المتحدة، ودولة قطر)، حيث يُتاح لهم تفعيل، شحن، واستخدام رصيد المحفظة بالعملة المحلية لبلدهم. ⟪يقر التاجر بأنه لا يمكن سحب المبالغ المالية المتاحة في المحفظة للعملات التالية: (الريال العماني، الدرهم الإماراتي، الدينار الكويتي، والدينار البحريني).⟫ في حال قيام التاجر بنقل أو تغيير دولته في إعدادات المتجر إلى دولة أخرى، يشترط تصفير رصيد المحفظة أولاً، وفي حال وجود رصيد يتعذر سحبه أو التصرف فيه، يلزم رفع طلب خاص لمعالجته عن طريق فريق خدمة العملاء. يُعد استخدام التاجر للخدمة، موافقة على هذه الشروط والأحكام، ومنحاً للأذونات اللازمة لتنفيذها. خدمة المميزات الإضافية VAS آلية التنفيذ وحدود المسؤولية للاستفادة من خدمة المميزات الإضافية يجب أن يكون لديك متجرًا مفعلاً على منصة زد. تملك منصة زد الحق …
