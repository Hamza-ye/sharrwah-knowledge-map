# Cards: Q5 on zid

21 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - The merchant turns methods on, from those offered to its store: Shopify's buyers pay with "any of the methods that you've activated"; Salla's merchant presses (تفعيل) on its طرق الدفع page; BigCommerce's uses Settings › Payments; WooCommerce's gateways carry an "Enable/Disable" box; Zid's merchant turns networks on in إدارة زد باي. They match by role, on stated pages and WooCommerce's shipped code. Q5-SH-K1524, Q5-SA-017, Q5-BC-066, Q5-WC-K0032, Q5-ZD-K0041
- **section 1, line 8:** - Staff need a payments permission, matching by role: `MANAGE_PAYMENTS_SETTINGS` (Shopify's admin code), `payment_methods_activation` (Salla's partner portal, as captured on 8 October 2026, observed), `manage_woocommerce` (WooCommerce's code), and a right Zid's owner grants (stated); at Shopify "Only the store owner can add a payment provider". Q5-SH-K0193, Q5-SA-K1509, Q5-WC-001, Q5-ZD-002, Q5-SH-009
- **section 1, line 9:** - The merchant's own rules then decide what a buyer sees, matching by role: Salla's قيود الدفع hide a method or reject or review the order by amount, country, customer group or category; Zid's restrictions hide a method; Shopify's Payment Customization lets an app "rename, reorder, hide the payment methods"; WooCommerce keeps cash on delivery to chosen shipping methods (shipped code); BigCommerce's merchant ticks "the countries where this payment method is available at checkout". Q5-SA-043, Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 1, line 10:** - Shopify, Zid and Salla limit methods by the store's country, matching by role: Shopify filters providers "based on your store's address"; Zid offers options "حسب دولتك", and زد باي only in Saudi Arabia and Kuwait; Salla's مدى and فيزا are "مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط". WooCommerce goes by country only in its suggestions, "The payment extension list for each country" (shipped code), and BigCommerce by the shopper's "geolocation" for local methods (stated; not checked on WooCommerce). Q5-SH-012, Q5-ZD-001, Q5-ZD-P0113, Q5-SA-036, Q5-WC-K0054, Q5-BC-081
- **section 1, line 11:** - Plans decide too, matching by role: Salla's electronic methods are "متاحة ضمن الباقات المدفوعة فقط"; Zid's Starter plan has only "Basic payment methods (bank transfer, cash on delivery)"; Shopify's custom payment extensions are "limited to eligible Shopify Plus Merchants only". A plan level that decides which methods a store can use was not in what was read on WooCommerce. Q5-SA-P0068, Q5-ZD-P0150, Q5-SH-K1700, Q5-WC-N09
- **section 1, line 12:** - The platform's own service checks the business first, matching by role: Salla's dashboard text, as captured on 8 October 2026, reads "مطلوب توثيق المتجر لتفعيل طريقة الدفع هذه" (observed); زد باي needs the owner to pass نفاذ; "Only eligible merchants can use Shopify Payments". Q5-SA-K0091, Q5-ZD-P0117, Q5-SH-K1532
- **section 1, line 13:** - The own service and other gateways, matching by role: Shopify allows "only one credit card payment provider activated at a time"; Zid's terms say "عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر" (official page); Salla's dashboard text, as captured on 8 October 2026, blocks its own service "لوجود ربط فعَّال مع تاب" (observed). WooCommerce differs: WooPayments and the Stripe plugin can run "at the same time", which "does cause a few issues". Q5-SH-008, Q5-ZD-P0109, Q5-SA-K1653, Q5-WC-031
- **section 1, line 14:** - The platform approves what plugs in, matching by role: at Shopify "Only approved Partners can build payments extensions", and a new method "must be submitted for review and approval"; Zid reviews apps "before publishing it to the public"; "The Marketplace team reviews all app submissions" (BigCommerce). These are stated pages but Shopify's partner terms (official). Q5-SH-K1696, Q5-SH-062, Q5-SH-058, Q5-ZD-K0363, Q5-BC-K0316
- **section 1, line 16:** - Amount limits: Salla's, for stores in Saudi Arabia, can't be raised by hand, being set "وفقاً للسياسات المحلية لكل دولة"; Zid's MIS pay takes orders from 200 to 2,000 riyals. Q5-SA-048, Q5-ZD-K0105
- **section 1, line 17:** - Providers decide on the merchant and the buyer, matching by role: at BigCommerce "Each provider has its own application process"; at Salla a provider can reject the merchant's request (dashboard text as captured on 8 October 2026, observed), and "تحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة"; Zid's electronic payment needs the gateway's approval; Shopify's Adyen needs "an existing Adyen approval". Q5-BC-P0048, Q5-SA-057, Q5-SA-066, Q5-ZD-K0003, Q5-SH-071
- **section 1, line 18:** - Law, card networks and processors bar some sellers, matching by role: Shopify's restrictions "may be imposed by law or through the Payment Network Rules"; Zid bars زد باي for activities forbidden "من زد باي أو المملكة العربية السعودية أو بلد النشاط". Both are official pages. Q5-SH-K2262, Q5-ZD-P0111
- **section 1, line 23:** - Each platform has a payment service of its own, run through other companies, matching by role: Shopify Payments, processed and settled by "one or more Payment Processors"; WooPayments, "powered by Stripe"; Salla's, provided "عبر شركائها"; BigCommerce Payments, "powered by PayPal"; and زد باي, through "مقدمي خدمات الدفع". These are official pages but BigCommerce's (stated). Q5-SH-K1555, Q5-WC-K0008, Q5-SA-P0079, Q5-BC-P0055, Q5-ZD-P0003
- **section 1, line 24:** - Other companies' gateways, matching by role: Shopify's "over 100 credit card payment providers"; Salla's بوابات الدفع الأخرى (not checked on WooCommerce); Zid's بوابات الدفع الأُخرى; BigCommerce's providers on and off its Embedded list; WooCommerce's gateways, "created as additional plugins". Q5-SH-006, Q5-SA-K1638, Q5-ZD-K0084, Q5-BC-036, Q5-WC-K0007
- **section 1, line 25:** - Methods recorded outside any provider: Shopify's "manual payments"; BigCommerce's "offline payment methods"; WooCommerce's Offline type, where "No online payment is made"; Salla's طرق دفع أخرى; Zid's bank transfer. BigCommerce and WooCommerce match by the same term, offline; the others by role. In Shopify's store ibx5bt-xy (countryCode YE), observed on 30 September 2026, Cash on Delivery (COD), Money Order and Bank Deposit each carried `"group":"MANUAL"`. Q5-SH-027, Q5-BC-060, Q5-WC-016, Q5-SA-015, Q5-ZD-P0075, Q5-SH-083
- **section 1, line 26:** - Providers plug in as add-ons, matching by role: Shopify's "payments extensions"; WooCommerce's gateway classes, added "through traditional plugins"; Zid's Open APIs model for "partners / payment service providers (PSPs)"; BigCommerce's "app payment processors"; Salla's apps, through "the Recurring Payments API". Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-SA-064
- **section 1, line 27:** - Where the buyer pays: Shopify's "direct providers and external providers", the latter on a page outside the store; WooCommerce's Direct type, with payment fields "directly on the checkout page"; Zid's Open APIs, where in one checkout type "Zid will draw the payment form"; BigCommerce's gateways that "redirect shoppers to a hosted payment page". Shopify and WooCommerce match by the same term, direct; Zid and BigCommerce by role. Q5-SH-007, Q5-WC-016, Q5-ZD-K0080, Q5-BC-068
- **section 1, line 31:** - The platform may withdraw what it offers, mostly without notice, matching by role: Salla's agreement reserves "الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع"; Shopify may disable third-party services "without notice to you", and so may BigCommerce; WooCommerce may "suspend or remove a Product from the Marketplace(s)" (vendor agreement, stated); زد باي "قد توقف أو تلغي الحساب في أي وقت". The others are official pages. Q5-SA-001, Q5-SH-K2168, Q5-BC-K0455, Q5-WC-K0462, Q5-ZD-010
- **section 1, line 37:** - Money held when a merchant leaves the own service is paid out: WooPayments' remaining balance "will still be paid out as per your usual schedule"; Zid's, "يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي", though not before its financing is repaid. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-BC-H0040
- **section 1, line 42:** - Through the platform's own service, money goes into a balance, then to the merchant's bank account, matching by role on stated pages and Zid's terms (official): Salla's "رصيد المدفوعات الإلكترونية" comes before the transfer to the bank account; Zid's terms add "المبلغ المستحق لرصيد التاجر" after fees; WooPayments adds the payment "(minus our fees)" to the balance; BigCommerce Payments and Shopify Payments pay out to the merchant's bank account. Q5-SA-P0006, Q5-ZD-P0024, Q5-WC-P0024, Q5-BC-P0074, Q5-SH-P0060
- **section 2, line 56:** - It draws on the five platforms' split between provider and manual methods, and on the waiting order of Shopify, BigCommerce and WooCommerce. Q5-SH-083, Q5-BC-060, Q5-SA-015, Q5-ZD-P0075, Q5-SH-K1736, Q5-WC-K0037
- **section 2, line 62:** - It draws on BigCommerce's Embedded Providers; Shopify's approved payments extensions, review of new methods and readiness step; Zid's Open APIs and app review; and the direct and hosted payment of Shopify, WooCommerce and BigCommerce. Q5-BC-105, Q5-SH-062, Q5-ZD-K0077, Q5-ZD-K0363, Q5-SH-007, Q5-WC-016, Q5-BC-068
- **section 2, line 63:** - Why: rule 2, each provider behind its own part; rule 1, one interface for every place. Q5-SH-K1694, Q5-ZD-K0077
- **section 2, line 68:** - **Place payment list**: Sharrwah's list, for each place it serves, of the providers and methods a store there may activate, each with its conditions: plan, verification, business type and amount limits. A store sees only its place's list, filtered by its conditions. Q5-SH-012, Q5-ZD-001, Q5-SA-036
- **section 2, line 69:** - It draws on Shopify's, Zid's and Salla's methods by the store's address or country, and, for conditions, on their plans, Salla's verification, Zid's كي نت for institutions and companies only, and Salla's limits by country. Q5-SH-012, Q5-ZD-001, Q5-SA-036, Q5-SA-P0068, Q5-ZD-P0150, Q5-SA-K0091, Q5-ZD-K0042, Q5-SA-048
- **section 2, line 70:** - Why: rule 1; what differs between places is set up as data, not built apart. Q5-SH-012, Q5-ZD-001
- **section 2, line 76:** - **Checkout payment rules**: rules the merchant sets, within its place's list, to hide a method, or to reject an order or hold it for review, by amount, quantity, the buyer's or card's country, customer group, category, shipping method or market. Q5-SA-043, Q5-ZD-013
- **section 2, line 77:** - It draws on Salla's قيود الدفع, Zid's restrictions, Shopify's Payment Customization, WooCommerce's cash on delivery by shipping method and BigCommerce's countries per offline method. Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 2, line 83:** - It draws on the direct route the platforms show for gateways the merchant connects, pay-later providers that pay the store, and bank transfer, and on the held route of their own services. Q5-SH-P0050, Q5-ZD-P0107, Q5-ZD-P0077, Q5-SA-P0099, Q5-WC-P0024, Q5-ZD-P0024
- **section 2, line 86:** - Not taken, for the first build: an own service that shuts other card gateways out once active, as Shopify's and Zid's do, since it would be a held route. Q5-SH-008, Q5-ZD-P0109
- **section 2, line 87:** - **Merchant balance**, with its payouts, on the held route only, and live only by the founder's decision: a ledger, per merchant, holder and currency, of credits from payments and debits for fees, refunds, chargebacks, reserves and other deductions, each debit naming the party it pays and the merchant's authorization for it; and payouts of the amount available to the merchant's own bank account, given at verification, on a schedule. Q5-ZD-P0024, Q5-SA-P0055, Q5-WC-P0124
- **section 2, line 92:** - It draws on BigCommerce's and Shopify's notice, P24's ending, Shopify's earlier provider kept for returns and its Wind Down Period, WooCommerce's six months, and the payout of the balance left at WooCommerce and Zid. Q5-BC-102, Q5-SH-021, Q5-WC-013, Q5-SH-K1704, Q5-WC-033, Q5-WC-K0715, Q5-ZD-P0042
- **section 3, line 98:** - Payment providers plug in, through a built-in integration or a payments add-on, as on all five platforms. Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-BC-105
- **section 3, line 103:** - Which providers and methods are offered is set per place, by Sharrwah; the records go by the store's address or country, or where the business is registered. Q5-SH-012, Q5-ZD-001, Q5-WC-K0402
- **section 3, line 106:** - Restrictions on businesses are set by law, card networks, processors and the platform (Shopify), and per country of activity (Zid). Q5-SH-K2262, Q5-ZD-P0111
- **section 3, line 108:** - Checkout payment rules are set per rule, by the merchant. Q5-SA-043, Q5-ZD-013
- **section 3, line 109:** - Amount limits are set per place by Sharrwah, as Salla's are by country, and per provider and method by the provider, as for Zid's MIS pay. Q5-SA-048, Q5-ZD-K0105
- **section 3, line 114:** - Approval of an add-on, and of each new method in it, is set by Sharrwah. Q5-SH-062, Q5-ZD-K0363
- **section 5, line 130:** - What a place is: the platforms go by the store's address or country, or where the business is registered. The design keys the place payment list by a place that may be narrower or wider than a country. Q1's proposal settles it. Q5-SH-012, Q5-WC-K0402, Q5-ZD-001
- **section 5, line 133:** - Which conditions a list entry may carry: plans gate methods on Salla and Zid, while a plan level was not in what was read on WooCommerce; the design keeps conditions as data. A company decision on plans settles it. Q5-SA-P0068, Q5-ZD-P0150, Q5-WC-N09
- **section 7, line 161:** - Whether providers and partners may build payments add-ons, and under what agreement and review. Q5-SH-K1696, Q5-SH-063, Q5-WC-K0353, Q5-ZD-K0077
- **section 7, line 163:** - Whether plans limit which methods a store can offer. Q5-SA-P0068, Q5-ZD-P0150, Q5-WC-N09
- **section 7, line 165:** - Whether Sharrwah offers financing repaid from sellers' sales, which needs a held route. Q5-SA-P0131, Q5-ZD-P0097
- **section 8, line 176:** - Records: Shopify Payments' processors, Stripe for WooPayments, and BigCommerce Payments' PayPal platform account settle; Zid's terms credit "المبلغ المستحق لرصيد التاجر" after fees; who settles Salla's payments was not in what was read. S01-VP-02, Q5-SH-K1555, Q5-WC-P0122, Q5-BC-P0070, Q5-ZD-P0024, Q5-SA-H0004
- **section 8, line 188:** - Records: Shopify deducts refunds from the next payout; Stripe pays out net of fees, disputes and refunds; Zid takes fees from amounts collected, and dues by "الخصم الآلي والمباشر"; Salla's dashboard text, as captured on 8 October 2026, takes postpaid label amounts from the wallet or coming dues (observed). S01-VP-09, Q5-SH-P0094, Q5-WC-P0124, Q5-ZD-P0024, Q5-ZD-P0061, Q5-SA-P0129
- **section 8, line 197:** - Records: WooPayments credits payments "(minus our fees)"; Shopify's terms for the EU, EEA and UK settle "net of fees, refunds, chargebacks, reserves, and other amounts owed"; Salla transfers "بعد خصم الرسوم والضريبة" (dashboard text as captured on 8 October 2026, observed), while its store balance is for Salla's subscriptions and services (UAE help); Zid takes fees from amounts collected. S01-VP-19, Q5-WC-P0024, Q5-SH-P0107, Q5-SA-P0037, Q5-SA-P0057, Q5-ZD-P0024
- **section 8, line 200:** - Records: Shopify's funds in custody are paid out "subject to the Payment Processor Terms"; WooPayments' and Zid's balances are paid out, Zid's not before its financing is repaid; Salla may stop the service and close the store for a breach. On BigCommerce, what happens to funds when a provider is disconnected was not in what was read. S01-VP-20, Q5-SH-P0033, Q5-WC-K0715, Q5-ZD-P0042, Q5-ZD-P0097, Q5-SA-P0083, Q5-BC-H0040

## The cards

### Q5-ZD-K0041

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q5/zid/copied.tsv`):
- concern_id: ZD-C-005
- placement: where
- structure: help.zid.sa article: عن زد باي
- identifier: إدارة زد باي
- statement: يمكنك إتاحة الشبكات في زد باي عن طريق تفعيل الشبكة المرغوبة من خلال إدارة زد باي
- cite_ids: ZD-S-0563

**Citation ZD-S-0563:** `https://help.zid.sa/about_zidpay/` | الشبكات المدعومة | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/082-help.zid.sa/text.txt` (8063 bytes), fetched 2026-10-12T04:52:14Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/047-help.zid.sa/text.txt` (8063 bytes), fetched 2026-10-12T10:50:23Z, captured
- quote: يمكنك إتاحة الشبكات في زد باي عن طريق تفعيل الشبكة المرغوبة من خلال إدارة زد باي
- title: زد - مركز المساعدة - عن زد باي
- the page opens: زد - مركز المساعدة - عن زد باي menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي عن زد باي عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة المخزون --> إدارة المخزون إدارة المنتجات --> إدارة ال…
- in context: …رافية رسوم زد باي : لا يتم فرض رسوم إنشاء حساب أو رسوم شهرية، فقط يتم تطبيق رسوم زد باي كنسبة على العمليات فقط. بالإضافة الى رسوم تشغيلية ثابتة لكل عملية دفع الكتروني. رسوم الاسترداد : لا يتم فرض رسوم إضافية لعملية الاسترداد ،يتم احتساب رسوم العملية الأساسية فقط. رسوم الايداع : هناك رسوم رمزية ثابته على إجمالي عملية الإيداع في الحساب البنكي للتاجر بقيمة 3 ريال ، في حال كان حساب التاجر في بنك الرياض يتم الإعفاء من رسوم الايداع. الشبكات المدعومة : ⟪يمكنك إتاحة الشبكات في زد باي عن طريق تفعيل الشبكة المرغوبة من خلال إدارة زد باي⟫ العملات النقدية : يمكنك إتاحة العملات في زد باي عن طريق تفعيل خاصية العملات في إعدادات المتجر. تحصيل المدفوعات : يتم إيداع المبالغ في حسابك البنكي بشكل دوري خلال الأيام التالية : الأحد ، الثلاثاء ، الخميس الحد الأدنى للإيداع هو 100 ريال. رسوم عملية الإيداع 3 ريال على إجمالي عملية الإيداع. الشبكات المدعومة: يمكنك إتاحة الشبكات في زد باي عن طريق تفعيل الشبكة المرغوبة من خلال إدارة زد باي العملات النقدية: يمكنك إتاحة العملات في زد باي عن طريق تفعيل…

### Q5-ZD-002

**Cited at:** section 1, line 8

**Record** (`studies/proposals/records/Q5/zid/statements.tsv`):
- stmt_id: Q5-ZD-002
- bears_on: 1;2
- identifier: صلاحيات فريق العمل > إدارة زد باي
- statement: إدارة زد باي : من خلال هذه الصفحة بإمكانك تحديد صلاحية تفعيل | تعطيل زد باي أو شبكات الدفع.
- scope: زد باي
- cite_ids: Q5-ZD-C002
- from: held

**Citation Q5-ZD-C002:** `https://help.zid.sa/zidpay_staff_and_currencies/` | صلاحيات فريق العمل > إدارة زد باي | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/184-help.zid.sa/text.txt` (4194 bytes), fetched 2026-10-12T04:53:56Z, captured
- quote: إدارة زد باي : من خلال هذه الصفحة بإمكانك تحديد صلاحية تفعيل | تعطيل زد باي أو شبكات الدفع.
- title: زد - مركز المساعدة - صلاحيات فريق العمل و خاصية العملات
- the page opens: زد - مركز المساعدة - صلاحيات فريق العمل و خاصية العملات menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي صلاحيات فريق العمل و خاصية العملات عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة الم…
- in context: …فعيل زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال زد باي صلاحيات فريق العمل و خاصية العملات مشاركة متصفح الكمبيوتر آخر تحديث August 6, 2026 تدعم زد باي خصائص إضافية في ادارة متجرك تتمثل بالتالي : صلاحيات فريق العمل : من خلال الاعدادات > فريق عمل تتيح لك هذه الخاصية التحكم في صلاحيات فريق العمل والحفاظ على سرية البيانات، بإمكانك تحديد الصلاحيات بشكل تفصيلي ، مما يساعدك كتاجر أو صاحب متجر الكتروني تحديد الصلاحيات لكل عضو. ⟪إدارة زد باي : من خلال هذه الصفحة بإمكانك تحديد صلاحية تفعيل | تعطيل زد باي أو شبكات الدفع.⟫ قائمة العمليات : من خلال هذه الصفحة بإمكانك تحديد صلاحية الاطلاع على كافة العمليات (الناجحة | الفاشلة | الملغاة) و تفاصيلها. استرداد المبالغ : من خلال هذه الخاصية بامكانك تحديد صلاحية استرداد المبالغ بشكل ( كلي | جزئي) للعميل النهائي. كشف الحساب : من خلال هذه الصفحة بإمكانك تحديد صلاحية الاطلاع على التفاصيل المالية للعمليات الناجحة وعمليات الإيداعات التي تتمثل ب 3 مراحل ( تم الايداع - قيد المعالجة - لم يتم الإيداع ). خاصية العملات : تتيح لك هذه …

### Q5-ZD-013

**Cited at:** section 1, line 9; section 2, line 76; section 2, line 77; section 3, line 108

**Record** (`studies/proposals/records/Q5/zid/statements.tsv`):
- stmt_id: Q5-ZD-013
- bears_on: 1;2
- identifier: الإعدادات > قيود الشحن والدفع
- statement: إخفاء وسيلة دفع معينة مثل (الدفع عند الاستلام) في حال توافقت شروط معينة من نفس الإعدادات
- cite_ids: Q5-ZD-C014
- from: held
- note: the settings path is copy Q5-ZD-K0356

**Citation Q5-ZD-C014:** `https://help.zid.sa/logistics-shipping-methods/` | طرق الشحن (body, after قيود الشحن والدفع) | 2026-08-05 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/134-help.zid.sa/text.txt` (13296 bytes), fetched 2026-10-12T04:53:06Z, captured
- quote: إخفاء وسيلة دفع معينة مثل (الدفع عند الاستلام) في حال توافقت شروط معينة من نفس الإعدادات
- title: زد - مركز المساعدة - الشحن المباشر - دون الحاجة لعقد ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - الشحن المباشر - دون الحاجة لعقد ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة طرق الشحن زد لوجيستك الشحن المباشر - دون الحاجة لعقد ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصني…
- in context: …مناسب للعميل، وتعطيل أو تفعيل خدمة الدفع عند الاستلام بكل سهولة وفي الفيديو التالي شرح لكيفية تخصيص خيار الشحن المفعل من هنا معلومات أُخرى عن الشحن إعدادات الشحن : ترتيب أولوية عرض شركات الشحن لدى العميل في صفحة الدفع شروط الشحن المجاني، كمثال: متى يكون الشحن مجاني؟ في حال كانت قيمة السلة 300+ ريال فأعلى، ولتفاصيل اكثر من هنا بإمكانك إخفاء شركة الشحن عن العميل في حال توافقت شروط معينة ،من خلال: الإعدادات > قيود الشحن والدفع و لتفاصيل اكثر من هنا ⟪إخفاء وسيلة دفع معينة مثل (الدفع عند الاستلام) في حال توافقت شروط معينة من نفس الإعدادات⟫ ، ولتفاصيل اكثر من هنا اسم المرسل للشحن وهو تخصيص رقم جوال محدد لكل مخزون بحيث شركة الشحن تتواصل مع الرقم المسجل لهذا المخزون لاستلام أو إرجاع الشحنات ، ولتفاصيل اكثر من هنا ولتفاصيل اكثر عن اعدادات الشحن من هنا لمزيد من التفاصيل حول أنواع الشحن يرجى الإطلاع على الفديو التالي: https://help.zid.sa/wp-content/uploads/2025/10/6-الفرق-بين-انواع-طرق-الشحن-سارة.mp4 لتفاصيل أكثر ومعلومات كل شركة شحن يرجى الإطلاع على الفديو التالي : https://help.zid.sa/…

### Q5-ZD-001

**Cited at:** section 1, line 10; section 2, line 68; section 2, line 69; section 2, line 70; section 3, line 103; section 5, line 130

**Record** (`studies/proposals/records/Q5/zid/statements.tsv`):
- stmt_id: Q5-ZD-001
- bears_on: 1
- identifier: بوابات الدفع الأُخرى
- statement: في زد نوفر لك خيارات دفع متعددة حسب دولتك، لتسهيل إتمام معاملاتك بكل سلاسة وأمان، وتمكينك من إدارة المدفوعات بالطريقة الأنسب لك.
- cite_ids: Q5-ZD-C001
- from: held

**Citation Q5-ZD-C001:** `https://help.zid.sa/payment-gateways/` | بوابات الدفع الأُخرى (opening) | 2025-11-16 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/145-help.zid.sa/text.txt` (3753 bytes), fetched 2026-10-12T04:53:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/065-help.zid.sa/text.txt` (3753 bytes), fetched 2026-10-12T10:50:41Z, captured
- quote: في زد نوفر لك خيارات دفع متعددة حسب دولتك، لتسهيل إتمام معاملاتك بكل سلاسة وأمان، وتمكينك من إدارة المدفوعات بالطريقة الأنسب لك.
- title: زد - مركز المساعدة - بوابات الدفع الأُخرى( لوحة التحكم الجديدة)
- the page opens: زد - مركز المساعدة - بوابات الدفع الأُخرى( لوحة التحكم الجديدة) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الجمعيات بوابات الدفع بوابات الدفع الأُخرى( لوحة التحكم الجديدة) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجا…
- in context: …واصل معنا مركز المساعدة الجمعيات بوابات الدفع بوابات الدفع الأُخرى( لوحة التحكم الجديدة) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال الجمعيات بوابات الدفع الأُخرى( لوحة التحكم الجديدة) مشاركة متصفح الكمبيوتر آخر تحديث November 16, 2025 ⟪في زد نوفر لك خيارات دفع متعددة حسب دولتك، لتسهيل إتمام معاملاتك بكل سلاسة وأمان، وتمكينك من إدارة المدفوعات بالطريقة الأنسب لك.⟫ يمكنك الوصول الى بوابات الدفع الأُخرى من خلال : المدفوعات > بوابات الدفع الأُخرى بوابات الدفع الأُخرى: باي موب Paymob بوابة الدفع باي موب (Paymob) متاحة للتجار في الإمارات، السعودية، وعمان. كيفية التفعيل: ادخل على لوحة التحكم > المدفوعات > بوابات الدفع الأُخرى اختر Paymob وقم بتعبأة النموذج المطلوب اموال باي amwal pay بوابة الدفع اموال باي amwal pay متاحة للتجار في عمان كيفية التفعيل: ادخل على لوحة التحكم > المدفوعات >بوابات الدفع الأُخرى اختر A…

### Q5-ZD-P0113

**Cited at:** section 1, line 10

**The same record as Q3-ZD-P0113,** whose card is in `Q3-zid-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: في الوقت الحالي خيار زد باي متاح لتجار المملكة العربية السعودية و دولة الكويت.
- scope: 

### Q5-ZD-P0150

**Cited at:** section 1, line 11; section 2, line 69; section 5, line 133; section 7, line 163

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-149
- bullet: e
- placement: decides
- identifier: zid.sa/en/egypt > Plans that fit your needs > Starter > Standout features (Arabic in the page data: طرق دفع أساسية (تحويل بنكي، دفع عند الاستلام))
- statement: Basic payment methods (bank transfer, cash on delivery)
- scope: Egypt; Starter
- conditions: S01-ZD-069;S01-ZD-070;S01-ZD-071;S01-ZD-072;S01-ZD-075
- cite_ids: S01-ZD-C371
- from: new
- note: Phase A3 (audit of S01-ZD-N01), from the held Egypt page; the rendered page shows the line under Starter, Free, Forever.

**Citation S01-ZD-C371:** `sharrwah-knowledge-map@a920665d3307544df27207fd40905340d9eaadfe:evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/190-zid.sa/raw.html` | Plans that fit your needs > Starter > Standout features | 2026-10-12 | kind: stated | quote check: found
- quote: Basic payment methods (bank transfer, cash on delivery)
- title: Create your online store easily with Zid | Join Egypt merchants
- in context: …s your average monthly orders?50 - 300 orders300 - 500 ordersMore than 1000 orders Did you have a website before? YesNo Contact us Plans that fit your needs and grow your business Monthly Yearly Monthly Yearly Beginning Rise Growth Professional Starter Free Forever The first step to launch your business Start for free Standout features Unlimited number of products, orders, and customers Add discount coupons Receive customer questions and reviews ⟪Basic payment methods (bank transfer, cash on delivery)⟫ Integration with shipping companies via Zid logistics Trusted by major brands The complete platform for e-commerce in the Middle East and North Africa Why choose Zid for your business in Egypt? Our partners in EgyptWe work with more than 100,000 traders in Egypt With you in growth, whatever your businessNo matter what your business is, from fashion to restaurants and services, Zid has the solutions that serve you and grow your business Fashion &…

### Q5-ZD-P0117

**Cited at:** section 1, line 12

**The same record as Q3-ZD-P0117,** whose card is in `Q3-zid-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: لتفعيل زد باي و استقبال عمليات الدفع الإلكتروني يشترط لمالك المتجر اجتياز التحقق من نفاذ.
- scope: 

### Q5-ZD-P0109

**Cited at:** section 1, line 13; section 2, line 86

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-108
- bullet: e
- placement: decides
- identifier: شروط وأحكام زد باي > طريقة الاستفادة من خدمات زد باي > تفعيل الخدمة
- statement: عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر.
- scope: السعودية; الكويت
- conditions: S01-ZD-001;S01-ZD-002;S01-ZD-003;S01-ZD-004;S01-ZD-005;S01-ZD-006;S01-ZD-007;S01-ZD-008;S01-ZD-009;S01-ZD-010;S01-ZD-011;S01-ZD-012;S01-ZD-013;S01-ZD-014;S01-ZD-015;S01-ZD-016;S01-ZD-017;S01-ZD-019;S01-ZD-020;S01-ZD-021;S01-ZD-022;S01-ZD-023;S01-ZD-024;S01-ZD-025;S01-ZD-026;S01-ZD-027;S01-ZD-028;S01-ZD-029;S01-ZD-030;S01-ZD-031;S01-ZD-032;S01-ZD-033;S01-ZD-034;S01-ZD-035;S01-ZD-037;S01-ZD-038;S01-ZD-039;S01-ZD-040;S01-ZD-041;S01-ZD-043;S01-ZD-044;S01-ZD-045;S01-ZD-046;S01-ZD-047;S01-ZD-061;S01-ZD-066;S01-ZD-068;S01-ZD-095;S01-ZD-082;S01-ZD-152;S01-ZD-157
- cite_ids: S01-ZD-C216;S01-ZD-C217
- from: index:ZD-C-011:ZD-S-0608

**Citation S01-ZD-C216:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | طريقة الاستفادة من خدمات زد باي | 2025-01-21 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر.
- title: Zid | Create your online store with modern retail services
- in context: …فق مع مزود الخدمة. طريقة الاستفادة من خدمات زد باي -تفعيل الخدمة: يجب أن تكون المعلومات المقدمة من التاجر لتفعيل الخدمة صحيحة. يجب أن يكون نشاط التاجر صحيح ولا يخدم أي من النشاطات المحظورة. في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين. التاجر وحده مسؤول عن مطابقة المنتجات مع المنتجات الموجودة في المتجر، وعن توصيلها للعميل النهائي. ⟪عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر.⟫ -رسوم العمليات: رسوم زد باي تعتمد على حسب باقتك المختارة في متجر زد، فإن كانت باقتك الأساسية تُفرض عليك رسوم زد باي للباقة الأساسية وإن كانت باقة النمو تُفرض عليك رسوم زد باي لباقة النمو. يتم فرض رسوم كنسبة مقتطعة من العمليات الناجحة. تحديد سقف أعلى بقيمة ٢٠٠ ريال لنسبة شبكة الدفع مدى (غير شامل لضريبة القيمة المضافه). يتم فرض رسوم تشغيلية على العمليات الناجحة بمختلف شبكات الدفع وذلك حسب نوع باقة التاجر. يمكن لزد باي تحديث رسوم العمليات في أي وقت…

**Citation S01-ZD-C217:** `https://zid.sa/ar/legal/zidpay-terms-conditions-kw/` | طريقة الاستفادة من خدمات زد باي، تفعيل الخدمة | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T10:51:27Z, captured
- quote: عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر.
- title: Zid | Create your online store with modern retail services
- in context: …اق صورة الهوية الوطنية من الخلف والامام للاستفادة من خدمة زد باي. يجب أن تكون المعلومات المقدمة من التاجر لتفعيل الخدمة صحيحة. يجب أن يكون نشاط التاجر صحيح ولا يخدم أي من النشاطات المحظورة. في حالة عدم صحة البيانات المقدمة لتفعيل الخدمة يعطى التاجر مهلة تصحيحية مدتها ١٤ يوم، وفي حال عدم التصحيح سيتم تعطيل الحساب وإعادة جميع المبالغ للعملاء النهائيين. التاجر وحده مسؤول عن مطابقة المنتجات مع المنتجات الموجودة في المتجر، وعن توصيلها للعميل النهائي. ⟪عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر.⟫ -رسوم العمليات: رسوم زد باي تعتمد على حسب باقتك المختارة في متجر زد، فإن كانت باقتك الأساسية تُفرض عليك رسوم زد باي للباقة الأساسية وإن كانت باقة النمو تُفرض عليك رسوم زد باي لباقة النمو، وفي حال كانت باقتك الباقة الاحترافية ستفرض عليك رسوم الباقة الاحترافية. يتم فرض رسوم كنسبة مقتطعة من العمليات. يمكن لزد باي تحديث رسوم العمليات في أي وقت بعد تنويه التاجر. -تحصيل المبالغ: تُحصّل المبالغ بشكل يومي. تحوّل المبالغ عند اجتياز المبالغ المحصلة ١ دينا…

### Q5-ZD-K0363

**Cited at:** section 1, line 14; section 2, line 62; section 3, line 114

**Record** (`studies/proposals/records/Q5/zid/copied.tsv`):
- concern_id: ZD-C-070
- placement: decides
- structure: docs.zid.sa: Overview (app types)
- identifier: Submit for Review
- statement: After developing the app, our team will take some time to review your submission and test the app functionality before publishing it to the public.
- cite_ids: ZD-S-0863

**Citation ZD-S-0863:** `https://docs.zid.sa/zid-apps-overview.md` | App Development Cycle | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/072-docs.zid.sa/text.txt` (4427 bytes), fetched 2026-10-12T04:52:10Z, captured
- quote: After developing the app, our team will take some time to review your submission and test the app functionality before publishing it to the public.
- title: 🗂️ Overview
- the page opens: Zid offers a strong platform for partners to develop applications that enhance the functionality of online stores. Understanding the different types of apps in Zid is essential for developers aiming for successful integrations. This article provides an overview of the app types supported by Zid, the development process, and the publishing options. App Types When you develop an app in Zid, you must decide whether it will be public or private. These options determine how the app is published and w…
- headings: App Development Cycle
- in context: …artnership-details). This step is not required for private apps. </Step> <Step title="Create Your App"> Follow our [step-by-step guide](https://docs.zid.sa/create-first-app) to get started. Whether you're building a Public, Private, or Shipping app, this guide covers all the key steps </Step> <Step title="Start Development"> Utilize Zid's APIs available in this documentation to begin your app development. </Step> <Step title="Submit for Review"> ⟪After developing the app, our team will take some time to review your submission and test the app functionality before publishing it to the public.⟫ </Step> <Step title="Publish Your App"> Once your app is tested and approved, your app will be listed in Zid App Market for all merchants or installed directly to the store if it's a private app. </Step> </Steps> --- # Additional Features to Discover The [Partner Dashboard](https://partner.zid.sa) offers a suite of tools designed to help you manage and optimize your app's performance, including: - **Promotions Management**: Easily create and man…

### Q5-ZD-K0105

**Cited at:** section 1, line 16; section 3, line 109

**Record** (`studies/proposals/records/Q5/zid/copied.tsv`):
- concern_id: ZD-C-013
- placement: decides
- structure: help.zid.sa article: خدمات التقسيط (لوحة التحكم الجديدة )
- identifier: MIS pay
- statement: تقدم لك أم آي إس باي خدمة الدفع بالأقساط وتقسيم قيمة مدفوعات العملاء على 3 دفعات شهرية بدون رسوم تأخير و بحد أدنى للطلب 200 ريال و حد أعلى 2000 ريال.
- cite_ids: ZD-S-0624

**Citation ZD-S-0624:** `https://help.zid.sa/bnpl-2/` | خدمة أم آي إس باي | 2026-10-07 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/090-help.zid.sa/text.txt` (8691 bytes), fetched 2026-10-12T04:52:22Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/050-help.zid.sa/text.txt` (8691 bytes), fetched 2026-10-12T10:50:26Z, captured
- quote: تقدم لك أم آي إس باي خدمة الدفع بالأقساط وتقسيم قيمة مدفوعات العملاء على 3 دفعات شهرية بدون رسوم تأخير و بحد أدنى للطلب 200 ريال و حد أعلى 2000 ريال.
- title: زد - مركز المساعدة - خدمات التقسيط (لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - خدمات التقسيط (لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي خدمات التقسيط (لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتجات إدارة…
- in context: … يوجد لديك حساب في تابي وترغب في تفعيله ، قم بإدخال رمز وثيقة العمل الحر وسنقوم بطلب إنشاء الحساب لك تلقائيا من لوحة التحكم بعد ذلك، قم بالضغط على ايقونة تفعيل 2. لدي حساب تابي للأعمال في حال لديك حساب في تابي وترغب في ربطه، قم بإدخال الرموز التالية : Public key secret key قم بوضع علامة✅ لإظهار تابي في صفحة المنتج في المتجر قم بوضع علامة ✅ لإظهار تابي في صفحة السلة قم بوضع علامة ✅ لتفعيل تابي لمزيد من المعلومات حول تابي هنا . خدمة أم آي إس باي : ⟪تقدم لك أم آي إس باي خدمة الدفع بالأقساط وتقسيم قيمة مدفوعات العملاء على 3 دفعات شهرية بدون رسوم تأخير و بحد أدنى للطلب 200 ريال و حد أعلى 2000 ريال.⟫ لتفعيل أم آي إس باي بالمتجر يتطلب أن يكون لديك حساب لديهم , وللتسجيل اتبع التالي : سجل طلبك عن طريق أم آي إس باي. بعد الانتهاء من عملية التسجيل، ستظهر لك مفاتيح التفعيل (App ID and App Secret) ومن ثم بإمكانك ربط أم آي إس باي على متجركم في زد. قم بوضع علامة ✅ لتفعيل MIS pay خدمة تمارا : تقدم تمارا حل مالي يُبسط عملية الدفع للعملاء و يوفر لهم حل مثالي و آمن يسهل لهم تجربة التسوق والدفع من خلال إعطائهم إمكانية الشراء وتقسيم الفاتورة على 3 أو 6 دفعا…

### Q5-ZD-K0003

**Cited at:** section 1, line 17

**The same record as Q2-ZD-K0003,** whose card is in `Q2-zid.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: لإتاحة خيار الدفع الإلكتروني في المتجر يتطلب تزويد بوابة الدفع بمتطلبات التفعيل حسب الكيان التجاري (فرد – شركة – مؤسسة) ليتم اعتماد الحساب لدى بوابة الدفع.
- scope: متطلبات تفعيل الدفع الالكتروني للسعودية

### Q5-ZD-P0111

**Cited at:** section 1, line 18; section 3, line 106

**The same record as Q3-ZD-P0111,** whose card is in `Q3-zid-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو المملكة العربية السعودية أو بلد النشاط، تتضمن: الأشخاص المتوفر عنهم معلومات باحتمالية تورطهم في نشاطات إجرامية أو مذكورين في اللوائح العامة (القائمة السوداء) للأنشطة الإجرامية والاتجار بالمخدرات والمنظمات الإرهابية. الأشخاص ذوو طبيعة نشاط من الصعب التحقق من شرعيته أو مصدر دخله، أو ذوو مصدر دخل لا يتوافق مع أوضاعهم المالية. الأشخاص الذين يرفضون تزويدنا بأي معلومات أو مستندات مطلوبة للتحقق من أنشطتهم أو مصادر الدخل أو الذين يزودونا بمستندات مشكوك في صحتها أو شرعيتها أو متلاعب بها. المؤسسات والشركات التي لا يمكن تحديد المساهمين فيها أو هيكلها التنظيمي. مكاتب الصرافة أو غيرها من الكيانات المشابهة غير المصرح لها. المؤسسات المالية المتمركزة في البلاد أو الأقاليم دون أن يكون لها حضورًا ماديًا والمشار إليها بـ (المصارف الصورية) والتي لا تنتمي إلى أي منظمة مالية خاضعة للرقابة. الأنشطة غير المتوافقة مع الشريعة الإسلامية. الوكلاء الوسطاء غير الرسميين. شركات العملات الرقمية مثل البيتكوين/ حسابات تداول العملات الرقمية. الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الوسطى) وما إلى ذلك. التجار الذين لا يقدموا أي معلومات كافية للتحقق من هوياتهم، أو هوية المستفيد النهائي. التاجر أو المستفيد النهائي (الشريك في عملية البيع والشراء) الذين طبقت عليهم عقوبات بناء على قرارات الأمم المتحدة، أو وزارة الخزانة الإنجليزية، أو الاتحاد الأوروبي، أو مكتب مراقبة الأصول الأجنبية، أو من هو مطالب للامتثال إذا كان الاسم مطابق لأي قائمة عقوبات أخرى. التاجر أو المستفيد النهائي ( الشريك في عملية البيع والشراء) الذي يقطن في البلدان الخاضعة للعقوبات الدولية تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية أفريقيا الوسطى) وما إلى ذلك. التجار مقدمي الخدمات المالية بدون موافقة البنك المركزي على سبيل المثال (الاستثمارات المالية غير المصرح بها، شركات التداول، تجميع الأموال أو الحوالات وخلافه). الجمعيات الخيرية والمنظمات غير الربحية غير المعتمدة من الجهات المعنية في المملكة العربية السعودية. الحسابات المجهولة والمسجلة بأسماء وهمية. الحسابات المرقمة التي يتعرف على مالكها بواسطة رقم بدلاً عن الأسماء. التجار الذين لم تكتمل إجراءات التحقق الواجبة عنهم أو لا يمكن التحري عنهم نظرًا لعدم اليقين أو الغموض في المعلومات المتوفرة عنهم. تجارة السجائر والسجائر الإلكترونية وجميع منتجات ومستلزمات التبغ. المراهنة/ المزاد. الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر. المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة أو أي نشاط آخر لا يتوافق مع مزود الخدمة.
- scope: السعودية

### Q5-ZD-P0003

**Cited at:** section 1, line 23

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-002
- bullet: a
- placement: where
- identifier: شروط وأحكام زد باي > التعريفات > زد باي
- statement: زد باي: هي خدمة تمكين التاجر من تنفيذ عمليات البيع والتجارة الإلكترونية من خلال مقدمي خدمات الدفع على منصة تابعة لزد
- scope: السعودية
- cite_ids: S01-ZD-C003
- from: index:ZD-C-009:ZD-S-0589
- note: The platform's definition of زد باي; it names مقدمي خدمات الدفع without naming any provider. The Kuwait document's definition is recorded in terms.tsv.

**Citation S01-ZD-C003:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | التعريفات | 2025-01-21 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: زد باي: هي خدمة تمكين التاجر من تنفيذ عمليات البيع والتجارة الإلكترونية من خلال مقدمي خدمات الدفع على منصة تابعة لزد
- title: Zid | Create your online store with modern retail services
- in context: …جارفريق جاهز لتمكين نموك مجتمع التجاركن مع تجار يفهموك ويشبهون طموحك أكاديمية زدتعلّم أحدث طرق واستراتيجيات التجارة مكتبة زد تقارير زد كل ما تحتاج معرفته عن السوق أدلة زدأدلة متكاملة للبدء والنمو في التجارة الإلكترونية الانتقال إلى زد زد x سلة زد x شوبيفاي زد x أوبن كارت زد x ماجنتو زد x ووردبريس EN تسجيل الدخول أنشئ متجرك شروط وأحكام زد باي الشروط والأحكام: تمثل الشروط والأحكام المذكورة أدناه العقد المبرم بين مستخدمي زد باي وشركة زد. التعريفات: ⟪زد باي: هي خدمة تمكين التاجر من تنفيذ عمليات البيع والتجارة الإلكترونية من خلال مقدمي خدمات الدفع على منصة تابعة لزد⟫، ويشار إليها -أيضًا- في هذه الشروط والأحكام ب (" زد باي، أو الخدمة"). تفعيل الخدمة: وهي عملية طلب التاجر لتفعيل خدمة زد باي. التاجر: هو المستخدم المشترك في زد باي، والمالك لمتجر على منصة زد. الشروط العامة: يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي. ولا يجوز استخدام زد باي ممن لا يسمح لهم باستلام الأموال أو القيام بعمليات تجارية أو غير تجارية…

### Q5-ZD-K0084

**Cited at:** section 1, line 24

**Record** (`studies/proposals/records/Q5/zid/copied.tsv`):
- concern_id: ZD-C-011
- placement: where
- structure: help.zid.sa article: بوابات الدفع الأُخرى( لوحة التحكم الجديدة)
- identifier: المدفوعات > بوابات الدفع الأُخرى
- statement: يمكنك الوصول الى بوابات الدفع الأُخرى من خلال : المدفوعات > بوابات الدفع الأُخرى
- cite_ids: ZD-S-0604

**Citation ZD-S-0604:** `https://help.zid.sa/payment-gateways/` | intro | 2025-11-16 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/145-help.zid.sa/text.txt` (3753 bytes), fetched 2026-10-12T04:53:17Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/065-help.zid.sa/text.txt` (3753 bytes), fetched 2026-10-12T10:50:41Z, captured
- quote: يمكنك الوصول الى بوابات الدفع الأُخرى من خلال : المدفوعات > بوابات الدفع الأُخرى
- title: زد - مركز المساعدة - بوابات الدفع الأُخرى( لوحة التحكم الجديدة)
- the page opens: زد - مركز المساعدة - بوابات الدفع الأُخرى( لوحة التحكم الجديدة) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة الجمعيات بوابات الدفع بوابات الدفع الأُخرى( لوحة التحكم الجديدة) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجا…
- in context: …الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال الجمعيات بوابات الدفع الأُخرى( لوحة التحكم الجديدة) مشاركة متصفح الكمبيوتر آخر تحديث November 16, 2025 في زد نوفر لك خيارات دفع متعددة حسب دولتك، لتسهيل إتمام معاملاتك بكل سلاسة وأمان، وتمكينك من إدارة المدفوعات بالطريقة الأنسب لك. ⟪يمكنك الوصول الى بوابات الدفع الأُخرى من خلال : المدفوعات > بوابات الدفع الأُخرى⟫ بوابات الدفع الأُخرى: باي موب Paymob بوابة الدفع باي موب (Paymob) متاحة للتجار في الإمارات، السعودية، وعمان. كيفية التفعيل: ادخل على لوحة التحكم > المدفوعات > بوابات الدفع الأُخرى اختر Paymob وقم بتعبأة النموذج المطلوب اموال باي amwal pay بوابة الدفع اموال باي amwal pay متاحة للتجار في عمان كيفية التفعيل: ادخل على لوحة التحكم > المدفوعات >بوابات الدفع الأُخرى اختر Amwal Pay وقم بتعبأة النموذج المطلوب بوابة الدفع تاب Tap : بوابة الدفع تاب متاحة ل…

### Q5-ZD-P0075

**Cited at:** section 1, line 25; section 2, line 56

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-074
- bullet: end-payment
- placement: where
- identifier: الحسابات البنكية ( لوحة التحكم الجديدة ); إدارة طرق الدفع > الحسابات البنكية
- statement: من خلال هذه الخاصية يمكنك عرض بيانات حسابك البنكي في صفحة الدفع لتمكين العملاء من الدفع عن طريق التحويل البنكي، مع إمكانية التحكم الكامل في عرض أو إخفاء التفاصيل.
- cite_ids: S01-ZD-C144
- from: index:ZD-C-016:ZD-S-0643

**Citation S01-ZD-C144:** `https://help.zid.sa/bank-accounts/` | intro | 2026-08-06 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/088-help.zid.sa/text.txt` (5691 bytes), fetched 2026-10-12T04:52:20Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/049-help.zid.sa/text.txt` (5691 bytes), fetched 2026-10-12T10:50:25Z, captured
- quote: من خلال هذه الخاصية يمكنك عرض بيانات حسابك البنكي في صفحة الدفع لتمكين العملاء من الدفع عن طريق التحويل البنكي، مع إمكانية التحكم الكامل في عرض أو إخفاء التفاصيل.
- title: زد - مركز المساعدة - الحسابات البنكية ( لوحة التحكم الجديدة )
- the page opens: زد - مركز المساعدة - الحسابات البنكية ( لوحة التحكم الجديدة ) menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة زد باي زد باي الحسابات البنكية ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> المنتج…
- in context: … ( لوحة التحكم الجديدة ) عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي العمليات روابط الدفع الإيداعات الحسابات البنكية المدفوعات تفعيل زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال زد باي الحسابات البنكية ( لوحة التحكم الجديدة ) مشاركة متصفح الكمبيوتر آخر تحديث August 6, 2026 ⟪من خلال هذه الخاصية يمكنك عرض بيانات حسابك البنكي في صفحة الدفع لتمكين العملاء من الدفع عن طريق التحويل البنكي، مع إمكانية التحكم الكامل في عرض أو إخفاء التفاصيل.⟫ يمكنك الوصول الى الحسابات البنكية من خلال : إدارة طرق الدفع > الحسابات البنكية خطوات إضافة حساب بنكي جديد: بإمكانك إضافة أكثر من حساب بنكي و تخصيص كل حساب بنكي على حدة إما إظهار معلومات الحساب البنكي في صفحة خيارات الدفع و التوصيل في المتجر وإتاحته كوسيلة دفع للعملاء أو إخفائها من خلال خيار التعديل. عند الدخول إلى صفحة الحسابات البنكية، اضغط على زر إنشاء في أعلى يسار الصفحة، ثم اختر إضافة حساب بنكي جديد. عرض تفاصيل الحساب البنكي في صفحة الدفع وا…

### Q5-ZD-K0077

**Cited at:** section 1, line 26; section 2, line 62; section 2, line 63; section 3, line 98; section 7, line 161

**Record** (`studies/proposals/records/Q5/zid/copied.tsv`):
- concern_id: ZD-C-010
- placement: where
- structure: docs.zid.sa: Overview (Zid Payments Open APIs)
- identifier: Zid Payments
- statement: This document provides a clear explanation for partners / payment service providers (PSPs) who want to integrate with Zid Payments through the Open APIs model.
- cite_ids: ZD-S-0597

**Citation ZD-S-0597:** `https://docs.zid.sa/overview-1340225m0.md` | intro | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/052-docs.zid.sa/text.txt` (746 bytes), fetched 2026-10-12T04:51:50Z, captured
- quote: This document provides a clear explanation for partners / payment service providers (PSPs) who want to integrate with Zid Payments through the Open APIs model.
- title: Overview
- the page opens: This document provides a clear explanation for partners / payment service providers (PSPs) who want to integrate with Zid Payments through the Open APIs model. The Open APIs integration model sets an API contract for our partners to implement. This includes listing the APIs that we require, in Zid Payments, in addition to sepcifying the request / response structure and format for each of these APIs. Partners are also expected to send some events / updates through webhooks. For this purpose, we s…
- headings: Overview
- in context: # Overview ⟪This document provides a clear explanation for partners / payment service providers (PSPs) who want to integrate with Zid Payments through the Open APIs model.⟫ The Open APIs integration model sets an API contract for our partners to implement. This includes listing the APIs that we require, in Zid Payments, in addition to sepcifying the request / response structure and format for each of these APIs. Partners are also expected to send some events / updates through webhooks. For this purpose, we specify webhook endpoint(s) in our system to be invoked. These are the base URLs for Zid Payments' system base…

### Q5-ZD-K0080

**Cited at:** section 1, line 27

**Record** (`studies/proposals/records/Q5/zid/copied.tsv`):
- concern_id: ZD-C-010
- placement: boundary
- structure: docs.zid.sa: Payment Overview
- identifier: Direct payment
- statement: Zid will draw the payment form, then collect and submit the card info using an API, exposed by the provider, through a call made directly from the client side.
- cite_ids: ZD-S-0600

**Citation ZD-S-0600:** `https://docs.zid.sa/overview-1340608m0.md` | Direct payment | 2026-10-12 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/053-docs.zid.sa/text.txt` (573 bytes), fetched 2026-10-12T04:51:51Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/011-docs.zid.sa/text.txt` (573 bytes), fetched 2026-10-12T10:49:45Z, captured
- quote: Zid will draw the payment form, then collect and submit the card info using an API, exposed by the provider, through a call made directly from the client side.
- title: Overview
- the page opens: There are two types of payment checkout on Zid and the provider will choose based on their preference; 1. Direct payment: Zid will draw the payment form, then collect and submit the card info using an API, exposed by the provider, through a call made directly from the client side. 2. Embedded payment: The provider will provide a JavaScript library that draws the payment form and submits the card info then provides Zid with a token. These actions (drawing the form, submitting the form) will be th…
- headings: Overview
- in context: # Overview There are two types of payment checkout on Zid and the provider will choose based on their preference; 1. **Direct payment:** ⟪Zid will draw the payment form, then collect and submit the card info using an API, exposed by the provider, through a call made directly from the client side.⟫ 2. **Embedded payment:** The provider will provide a JavaScript library that draws the payment form and submits the card info then provides Zid with a token. These actions (drawing the form, submitting the form) will be through functions in the JavaScript library / plugin.

### Q5-ZD-010

**Cited at:** section 1, line 31

**Record** (`studies/proposals/records/Q5/zid/statements.tsv`):
- stmt_id: Q5-ZD-010
- bears_on: 4
- identifier: شروط وأحكام زد باي > مدة/ إنهاء التعاقد
- statement: زد باي قد توقف أو تلغي الحساب في أي وقت وقد ترسل زد باي كتاب إلى بريدك الإلكتروني المسجل إليها بالأسباب. ومثل هذه الأسباب قد تخضع إلى السلطة التقديرية لزد باي وقد تتضمن على سبيل المثال لا الحصر زيادة مخاطر العمليات، أو عمليات مشبوهة، أو أنشطة ممنوعة والغير قانونية من المستخدم، أو تغير في العمليات أو الملكية والإدارة للمستخدم.
- scope: Zid Pay, Saudi Arabia
- cite_ids: Q5-ZD-C010;Q5-ZD-C011
- from: held

**Citation Q5-ZD-C010:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | مدة/ إنهاء التعاقد | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: زد باي قد توقف أو تلغي الحساب في أي وقت وقد ترسل زد باي كتاب إلى بريدك الإلكتروني المسجل إليها بالأسباب.
- title: Zid | Create your online store with modern retail services
- in context: …والأحكام سارية طالما تفعيلك لخدمة زد باي ساريًا. مدة التعاقد مع زد باي سنة واحدة من تاريخ استلام بريد التحقق الإلكتروني وتجدد تلقائيًا مالم يتم إنهاء التعاقد من المستخدم أو زد باي. إنهاء التعاقد لا يعني التنازل عن المتطلبات المطلوبة من المستخدم فيما يخص عمليات الدفع سابقة. في حالة فتح حساب لدى زد باي ولم تتوفر المعلومات والمستندات المطلوبة لاستكمال عملية التسجيل خلال ١٤ يوم سيلغى الحساب تلقائيًا، وستعاد المبالغ المحصلة لمصادرها -العميل النهائي-. ⟪زد باي قد توقف أو تلغي الحساب في أي وقت وقد ترسل زد باي كتاب إلى بريدك الإلكتروني المسجل إليها بالأسباب.⟫ ومثل هذه الأسباب قد تخضع إلى السلطة التقديرية لزد باي وقد تتضمن على سبيل المثال لا الحصر زيادة مخاطر العمليات، أو عمليات مشبوهة، أو أنشطة ممنوعة والغير قانونية من المستخدم، أو تغير في العمليات أو الملكية والإدارة للمستخدم. حدود المسؤولية يتحمل التاجر منفردا مسؤولية طبيعة المشترين أو العملاء الذين يتعامل معهم، ويوافق على التعامل مع العملاء الشرعيين فقط. التاجر هو المسؤول الوحيد عن طبيعة عمليات الدفع التي تتم على حسابه سواء خاطئة أو مشبوهة، وزد با…

**Citation Q5-ZD-C011:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | مدة/ إنهاء التعاقد | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: ومثل هذه الأسباب قد تخضع إلى السلطة التقديرية لزد باي وقد تتضمن على سبيل المثال لا الحصر زيادة مخاطر العمليات، أو عمليات مشبوهة، أو أنشطة ممنوعة والغير قانونية من المستخدم، أو تغير في العمليات أو الملكية والإدارة للمستخدم.
- title, opening and note boxes: as for this source's citation above
- in context: …حقق الإلكتروني وتجدد تلقائيًا مالم يتم إنهاء التعاقد من المستخدم أو زد باي. إنهاء التعاقد لا يعني التنازل عن المتطلبات المطلوبة من المستخدم فيما يخص عمليات الدفع سابقة. في حالة فتح حساب لدى زد باي ولم تتوفر المعلومات والمستندات المطلوبة لاستكمال عملية التسجيل خلال ١٤ يوم سيلغى الحساب تلقائيًا، وستعاد المبالغ المحصلة لمصادرها -العميل النهائي-. زد باي قد توقف أو تلغي الحساب في أي وقت وقد ترسل زد باي كتاب إلى بريدك الإلكتروني المسجل إليها بالأسباب. ⟪ومثل هذه الأسباب قد تخضع إلى السلطة التقديرية لزد باي وقد تتضمن على سبيل المثال لا الحصر زيادة مخاطر العمليات، أو عمليات مشبوهة، أو أنشطة ممنوعة والغير قانونية من المستخدم، أو تغير في العمليات أو الملكية والإدارة للمستخدم.⟫ حدود المسؤولية يتحمل التاجر منفردا مسؤولية طبيعة المشترين أو العملاء الذين يتعامل معهم، ويوافق على التعامل مع العملاء الشرعيين فقط. التاجر هو المسؤول الوحيد عن طبيعة عمليات الدفع التي تتم على حسابه سواء خاطئة أو مشبوهة، وزد باي لن تتحمل أي مسؤولية عن أي عملية دفع لابد من ردها إلى مصدرها. إذا كان التاجر متشككا في أي معاملة فمسؤولية الإبقاء على عدم تنفيذ المعاملة تقع على عاتقه حتى يتواصل مع العميل النهائي ويجري كافة التحقيقات المطلوبة لضمان صحة وش…

### Q5-ZD-P0042

**Cited at:** section 1, line 37; section 2, line 92; section 8, line 200

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-041
- bullet: c;end-payout
- placement: decides
- identifier: FAQ: في حال تم تعطيل زد باي هل يتم تحويل رصيد المبالغ؟
- statement: نعم يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي.
- cite_ids: S01-ZD-C081
- from: index:ZD-C-003:ZD-S-0556

**Citation S01-ZD-C081:** `https://help.zid.sa/faqs/%d9%81%d9%8a-%d8%ad%d8%a7%d9%84-%d8%aa%d9%85-%d8%aa%d8%b9%d8%b7%d9%8a%d9%84-%d8%b2%d8%af-%d8%a8%d8%a7%d9%8a-%d9%87%d9%84-%d9%8a%d8%aa%d9%85-%d8%aa%d8%ad%d9%88%d9%8a%d9%84-%d8%b1%d8%b5%d9%8a%d8%af/` | answer | 2023-07-15 | kind: stated | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/115-help.zid.sa/text.txt` (2426 bytes), fetched 2026-10-12T04:52:47Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/053-help.zid.sa/text.txt` (2426 bytes), fetched 2026-10-12T10:50:29Z, captured
- quote: نعم يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي.
- title: في حال تم تعطيل زد باي هل يتم تحويل رصيد المبالغ؟ - زد - مركز المساعدة
- the page opens: في حال تم تعطيل زد باي هل يتم تحويل رصيد المبالغ؟ - زد - مركز المساعدة menu right alt الدخول لمتجرك --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا EN --> الدخول لمتجرك close --> الرئيسية الأكاديمية مجتمع تجار زد الأسئلة الشائعة تواصل معنا English --> مركز المساعدة في حال تم تعطيل زد باي هل يتم تحويل رصيد المبالغ؟ عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية --> تعرف على زد --> تعرف على زد إعدادات المتجر --> إعدادات المتجر المنتجات --> التصنيفات --> التصنيفات المنتجات --> ال…
- in context: … زد الأسئلة الشائعة تواصل معنا مركز المساعدة في حال تم تعطيل زد باي هل يتم تحويل رصيد المبالغ؟ عن ماذا تبحث ؟ دليل استخدام منصة التاجر الرئيسية المنتجات الطلبات العملاء التسويق واتساب زد الجمعيات تصميم المتجر الإعدادات منصات البيع التحليلات سفير زد منتجات وخدمات زد مزيد زد لوجيستك زد باي سوق التطبيقات زد نمو زد كاشير تمويل زد سوق الثيمات تطبيق الجوال في حال تم تعطيل زد باي هل يتم تحويل رصيد المبالغ؟ مشاركة متصفح الكمبيوتر آخر تحديث July 15, 2023 ⟪نعم يتم تحويل المبلغ المتوفر في رصيد التاجر إلى الحساب البنكي.⟫ سوف تتعلم: التقييمات والمراجعات 0 0 من أصل 5 نجوم (بناءً على 0 تقييمات) ممتاز جيد جدًا متوسط ضعيف سيئ جدًا إرسال تقييمك Select a Rating 5 Stars 4 Stars 3 Stars 2 Stars 1 Star إرسال التقييم هل زد باي تدعم خاصية العملات المتاحة في زد؟ كيف يمكن إتمام إحدى عمليات الاسترجاع للعملاء النهائيين في حال عدم وجود رصيد كافي؟ تواصل معنا هل تحتاج إلى مساعدة إضافية؟ تواصل معنا لماذا زد لماذا ابدأ مع زد؟ لماذا أنتقل إلى زد؟ لماذا أتوسع مع زد؟ الأسعار الدعم والت…

### Q5-ZD-P0097

**Cited at:** section 1, line 37; section 7, line 165; section 8, line 200

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-096
- bullet: c
- placement: decides
- identifier: الشروط والأحكام > تمويل زد > أحكام وشروط عامة إضافية
- statement: بعد اشتراك التاجر في الخدمة، فإنه لن يتمكن من إلغاء اشتراكه في زد باي، أو التحويل إلى قناة دفع أخرى إلى حين استكمال كامل التزاماته بالسداد.
- cite_ids: S01-ZD-C190
- from: index:ZD-C-023:ZD-S-0697

**Citation S01-ZD-C190:** `https://zid.sa/ar/legal/terms-conditions/` | تمويل زد: أحكام وشروط عامة إضافية | 2026-08 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/187-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T04:53:53Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/122-zid.sa/raw.html` (626842 bytes), fetched 2026-10-12T10:51:26Z, captured
- quote: بعد اشتراك التاجر في الخدمة، فإنه لن يتمكن من إلغاء اشتراكه في زد باي، أو التحويل إلى قناة دفع أخرى إلى حين استكمال كامل التزاماته بالسداد.
- title: Zid | Create your online store with modern retail services
- in context: …ما اتفق عليه مع جهة التمويل، دون أي تدخل أو علاقة من أي نوع مع زد. تمكّن زد التاجر من متابعة عمليات السداد عن طريق لوحة تحكم الكترونية، لمساعدة التجار على الإطلاع على حالة التمويل والسداد، وبقدر ما تلتزم زد بأقصى قدرة في توفير بيانات دقيقة ومتزامنة مع جهة التمويل للتسهيل على التجار، إلا أنه عند التعارض والاختلاف، فإن البيانات والمعلومات المقدمة من جهة التمويل التي تحوزها، هي الحاكمة على البيانات والمعلومات في لوحة التحكم. أحكام وشروط عامة إضافية ⟪بعد اشتراك التاجر في الخدمة، فإنه لن يتمكن من إلغاء اشتراكه في زد باي، أو التحويل إلى قناة دفع أخرى إلى حين استكمال كامل التزاماته بالسداد.⟫ لن يتمكن التاجر من إلغاء أو تعديل أي من طرق حصوله على الخدمة، بعد تقديم خدمة التمويل له من جهة التمويل، أو بعد توقيعه بالالتزام معها. لأغراض تقديم الخدمة، ستشارك زد كافة المعلومات المتعلقة بمبيعات التاجر مع جهة التمويل. في حال المنازعات، وتحت طلب السلطات والجهات الرسمية، فإن زد ستقدم للجهات الرسمية ما تطلبه من معلومات وبيانات. يُعد استخدام التاجر للخدمة، موافقة على هذه الشروط والأحكام، ومنحا للأذونات اللازمة لتنفيذها الأحكام العامة لا يجوز للتاج…

### Q5-ZD-P0024

**Cited at:** section 1, line 42; section 2, line 83; section 2, line 87; section 8, line 176; section 8, line 188; section 8, line 197

**Record** (`studies/proposals/records/Q5/zid/copied-pilot.tsv`):
- stmt_id: S01-ZD-023
- bullet: a
- placement: responsible
- identifier: شروط وأحكام زد باي > تسوية المدفوعات وعملية الاسترداد > رصيد التاجر
- statement: يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.
- scope: السعودية; الكويت
- cite_ids: S01-ZD-C045;S01-ZD-C046
- from: index:ZD-C-003:ZD-S-0555

**Citation S01-ZD-C045:** `https://zid.sa/ar/legal/zidpay-terms-conditions-sa/` | تسوية المدفوعات وعملية الاسترداد | 2025-01-21 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/189-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T04:53:55Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/124-zid.sa/raw.html` (223074 bytes), fetched 2026-10-12T10:51:28Z, captured
- quote: يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.
- title: Zid | Create your online store with modern retail services
- in context: …د الأموال". قد تقوم زد باي بحجز مبلغ احتياطي يحسب من حجم معاملات العملاء ذوى المخاطر العالية. يتم تسوية هذا المبلغ الاحتياطي عند إغلاق الحسابات في حالة عدم استخدامها. يجوز لزد باي رد المبالغ إلى مصادرها والتي لم يتم تحويلها إلى الحساب البنكي للمستخدم لمدة أكثر من ١٤يوم وذلك لعدم قدرة المستخدم على تقديم بيانات صالحة وعليه يعتبر حسابه مهمل مما يترتب عليه إيقاف الحساب. قد تحتجز زد باي المبالغ المعلقة أو تسلمها إلى جهات أخرى وفقًا لتقدير زد باي فقط. ⟪يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.⟫ يجوز لزد باي ومزودو الخدمة باقتطاع رسوم رمزية على إجمالي العملية. يلتزم المستخدم بدفع أي رسوم غير مسددة خلال خمسة أيام عمل. التصديق على التوقيعات والإشعارات الإلكترونية تمثل الموافقة على تسجيل حساب في زد باي توقيعك الإلكتروني وتعتبر مراسلتنا من خلال خيار الدعم على الإيميل ([email protected]) يعتبر بمثابة إشعار رسمي منك وتعادل توقيعك الشخصي. الموافقة على أن البريد الإلكتروني المستخدم للتسجيل حساب في زد باي هو بريدك الإلكتروني المعتمد وأن كافة الم…

**Citation S01-ZD-C046:** `https://zid.sa/ar/legal/zidpay-terms-conditions-kw/` | تسوية المدفوعات وعملية الاسترداد | 2026-10-12 | kind: official page | quote check: found
- captured: `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/188-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T04:53:54Z, captured
- captured: `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/text.txt` (91 bytes), `evidence/product-class/runs/20261012T104936Z-s01-sources/items/123-zid.sa/raw.html` (219276 bytes), fetched 2026-10-12T10:51:27Z, captured
- quote: يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.
- title: Zid | Create your online store with modern retail services
- in context: …د الأموال". قد تقوم زد باي بحجز مبلغ احتياطي يحسب من حجم معاملات العملاء ذوى المخاطر العالية. يتم تسوية هذا المبلغ الاحتياطي عند إغلاق الحسابات في حالة عدم استخدامها. يجوز لزد باي رد المبالغ إلى مصادرها والتي لم يتم تحويلها إلى الحساب البنكي للمستخدم لمدة أكثر من x يوم وذلك لعدم قدرة المستخدم على تقديم بيانات صالحة وعليه يعتبر حسابه مهمل مما يترتب عليه إيقاف الحساب. قد تحتجز زد باي المبالغ المعلقة أو تسلمها إلى جهات أخرى وفقًا لتقدير زد باي فقط. ⟪يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.⟫ يجوز لزد باي ومزودو الخدمة باقتطاع رسوم رمزية على إجمالي العملية. يلتزم المستخدم بدفع أي رسوم غير مسددة خلال خمسة أيام عمل. التصديق على التوقيعات والإشعارات الإلكترونية تمثل الموافقة على تسجيل حساب في زد باي توقيعك الإلكتروني وتعتبر مراسلتنا من خلال خيار الدعم على الإيميل ([email protected]) يعتبر بمثابة إشعار رسمي منك وتعادل توقيعك الشخصي. الموافقة على أن البريد الإلكتروني المستخدم للتسجيل حساب في زد باي هو بريدك الإلكتروني المعتمد وأن كافة الم…
