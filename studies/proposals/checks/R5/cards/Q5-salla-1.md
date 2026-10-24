# Cards: Q5 on salla

17 records cited by `studies/proposals/drafts/Q5/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 7:** - The merchant turns methods on, from those offered to its store: Shopify's buyers pay with "any of the methods that you've activated"; Salla's merchant presses (تفعيل) on its طرق الدفع page; BigCommerce's uses Settings › Payments; WooCommerce's gateways carry an "Enable/Disable" box; Zid's merchant turns networks on in إدارة زد باي. They match by role, on stated pages and WooCommerce's shipped code. Q5-SH-K1524, Q5-SA-017, Q5-BC-066, Q5-WC-K0032, Q5-ZD-K0041
- **section 1, line 8:** - Staff need a payments permission, matching by role: `MANAGE_PAYMENTS_SETTINGS` (Shopify's admin code), `payment_methods_activation` (Salla's partner portal, as captured on 8 October 2026, observed), `manage_woocommerce` (WooCommerce's code), and a right Zid's owner grants (stated); at Shopify "Only the store owner can add a payment provider". Q5-SH-K0193, Q5-SA-K1509, Q5-WC-001, Q5-ZD-002, Q5-SH-009
- **section 1, line 9:** - The merchant's own rules then decide what a buyer sees, matching by role: Salla's قيود الدفع hide a method or reject or review the order by amount, country, customer group or category; Zid's restrictions hide a method; Shopify's Payment Customization lets an app "rename, reorder, hide the payment methods"; WooCommerce keeps cash on delivery to chosen shipping methods (shipped code); BigCommerce's merchant ticks "the countries where this payment method is available at checkout". Q5-SA-043, Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 1, line 10:** - Shopify, Zid and Salla limit methods by the store's country, matching by role: Shopify filters providers "based on your store's address"; Zid offers options "حسب دولتك", and زد باي only in Saudi Arabia and Kuwait; Salla's مدى and فيزا are "مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط". WooCommerce goes by country only in its suggestions, "The payment extension list for each country" (shipped code), and BigCommerce by the shopper's "geolocation" for local methods (stated; not checked on WooCommerce). Q5-SH-012, Q5-ZD-001, Q5-ZD-P0113, Q5-SA-036, Q5-WC-K0054, Q5-BC-081
- **section 1, line 11:** - Plans decide too, matching by role: Salla's electronic methods are "متاحة ضمن الباقات المدفوعة فقط"; Zid's Starter plan has only "Basic payment methods (bank transfer, cash on delivery)"; Shopify's custom payment extensions are "limited to eligible Shopify Plus Merchants only". A plan level that decides which methods a store can use was not in what was read on WooCommerce. Q5-SA-P0068, Q5-ZD-P0150, Q5-SH-K1700, Q5-WC-N09
- **section 1, line 12:** - The platform's own service checks the business first, matching by role: Salla's dashboard text, as captured on 8 October 2026, reads "مطلوب توثيق المتجر لتفعيل طريقة الدفع هذه" (observed); زد باي needs the owner to pass نفاذ; "Only eligible merchants can use Shopify Payments". Q5-SA-K0091, Q5-ZD-P0117, Q5-SH-K1532
- **section 1, line 13:** - The own service and other gateways, matching by role: Shopify allows "only one credit card payment provider activated at a time"; Zid's terms say "عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر" (official page); Salla's dashboard text, as captured on 8 October 2026, blocks its own service "لوجود ربط فعَّال مع تاب" (observed). WooCommerce differs: WooPayments and the Stripe plugin can run "at the same time", which "does cause a few issues". Q5-SH-008, Q5-ZD-P0109, Q5-SA-K1653, Q5-WC-031
- **section 1, line 16:** - Amount limits: Salla's, for stores in Saudi Arabia, can't be raised by hand, being set "وفقاً للسياسات المحلية لكل دولة"; Zid's MIS pay takes orders from 200 to 2,000 riyals. Q5-SA-048, Q5-ZD-K0105
- **section 1, line 17:** - Providers decide on the merchant and the buyer, matching by role: at BigCommerce "Each provider has its own application process"; at Salla a provider can reject the merchant's request (dashboard text as captured on 8 October 2026, observed), and "تحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة"; Zid's electronic payment needs the gateway's approval; Shopify's Adyen needs "an existing Adyen approval". Q5-BC-P0048, Q5-SA-057, Q5-SA-066, Q5-ZD-K0003, Q5-SH-071
- **section 1, line 23:** - Each platform has a payment service of its own, run through other companies, matching by role: Shopify Payments, processed and settled by "one or more Payment Processors"; WooPayments, "powered by Stripe"; Salla's, provided "عبر شركائها"; BigCommerce Payments, "powered by PayPal"; and زد باي, through "مقدمي خدمات الدفع". These are official pages but BigCommerce's (stated). Q5-SH-K1555, Q5-WC-K0008, Q5-SA-P0079, Q5-BC-P0055, Q5-ZD-P0003
- **section 1, line 24:** - Other companies' gateways, matching by role: Shopify's "over 100 credit card payment providers"; Salla's بوابات الدفع الأخرى (not checked on WooCommerce); Zid's بوابات الدفع الأُخرى; BigCommerce's providers on and off its Embedded list; WooCommerce's gateways, "created as additional plugins". Q5-SH-006, Q5-SA-K1638, Q5-ZD-K0084, Q5-BC-036, Q5-WC-K0007
- **section 1, line 25:** - Methods recorded outside any provider: Shopify's "manual payments"; BigCommerce's "offline payment methods"; WooCommerce's Offline type, where "No online payment is made"; Salla's طرق دفع أخرى; Zid's bank transfer. BigCommerce and WooCommerce match by the same term, offline; the others by role. In Shopify's store ibx5bt-xy (countryCode YE), observed on 30 September 2026, Cash on Delivery (COD), Money Order and Bank Deposit each carried `"group":"MANUAL"`. Q5-SH-027, Q5-BC-060, Q5-WC-016, Q5-SA-015, Q5-ZD-P0075, Q5-SH-083
- **section 1, line 26:** - Providers plug in as add-ons, matching by role: Shopify's "payments extensions"; WooCommerce's gateway classes, added "through traditional plugins"; Zid's Open APIs model for "partners / payment service providers (PSPs)"; BigCommerce's "app payment processors"; Salla's apps, through "the Recurring Payments API". Q5-SH-K1694, Q5-WC-K0006, Q5-ZD-K0077, Q5-BC-031, Q5-SA-064
- **section 1, line 31:** - The platform may withdraw what it offers, mostly without notice, matching by role: Salla's agreement reserves "الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع"; Shopify may disable third-party services "without notice to you", and so may BigCommerce; WooCommerce may "suspend or remove a Product from the Marketplace(s)" (vendor agreement, stated); زد باي "قد توقف أو تلغي الحساب في أي وقت". The others are official pages. Q5-SA-001, Q5-SH-K2168, Q5-BC-K0455, Q5-WC-K0462, Q5-ZD-010
- **section 1, line 35:** - At Salla, a method tied to a provider goes with it: "وفي حال تمّ إلغاء خدمة الدفع Tap سيتم إلغاء الربط مع K net tap تلقائياً". Not checked on WooCommerce or Zid. Q5-SA-K1654
- **section 2, line 56:** - It draws on the five platforms' split between provider and manual methods, and on the waiting order of Shopify, BigCommerce and WooCommerce. Q5-SH-083, Q5-BC-060, Q5-SA-015, Q5-ZD-P0075, Q5-SH-K1736, Q5-WC-K0037
- **section 2, line 58:** - **Payment provider**: a company that processes provider methods and pays the money out, recorded once with the methods it carries, the places it serves, its money route and its terms. A method may come from several providers, a provider carry several methods. Q5-SH-001, Q5-BC-079, Q5-SA-K1654
- **section 2, line 59:** - It draws on Shopify's cards through "Shopify Payments, a third-party provider, or both together", BigCommerce's alternative methods offered "through a cooperating payment gateway", and Salla's K net, which hangs on Tap. Q5-SH-001, Q5-BC-079, Q5-SA-K1654
- **section 2, line 60:** - Why: rule 2; a provider's arrival or exit changes only its own record and its methods. Q5-SH-022, Q5-SA-K1654
- **section 2, line 65:** - **Provider account**: the merchant's own account with a provider, connected with the credentials of an account it holds, or applied for through Sharrwah. The provider decides each application; Sharrwah shows its state: applied, approved, rejected or connected. Q5-SA-053, Q5-SA-057, Q5-BC-P0048
- **section 2, line 66:** - It draws on Salla's choice between an existing account and a request the provider may reject, the own account Zid's pay-later providers need, BigCommerce's application and underwriting, and Shopify's apps, where the merchant may "log in or create an account with the payment provider". Q5-SA-053, Q5-SA-057, Q5-ZD-P0080, Q5-BC-P0048, Q5-SH-053
- **section 2, line 68:** - **Place payment list**: Sharrwah's list, for each place it serves, of the providers and methods a store there may activate, each with its conditions: plan, verification, business type and amount limits. A store sees only its place's list, filtered by its conditions. Q5-SH-012, Q5-ZD-001, Q5-SA-036
- **section 2, line 69:** - It draws on Shopify's, Zid's and Salla's methods by the store's address or country, and, for conditions, on their plans, Salla's verification, Zid's كي نت for institutions and companies only, and Salla's limits by country. Q5-SH-012, Q5-ZD-001, Q5-SA-036, Q5-SA-P0068, Q5-ZD-P0150, Q5-SA-K0091, Q5-ZD-K0042, Q5-SA-048
- **section 2, line 73:** - It draws on the activation and payments permissions the platforms show, Shopify's owner-only provider change and one card provider at a time, BigCommerce's change log, Salla's market selector and BigCommerce's methods per currency. Q5-SH-K0193, Q5-SA-K1509, Q5-BC-072, Q5-SA-016, Q5-BC-074
- **section 2, line 76:** - **Checkout payment rules**: rules the merchant sets, within its place's list, to hide a method, or to reject an order or hold it for review, by amount, quantity, the buyer's or card's country, customer group, category, shipping method or market. Q5-SA-043, Q5-ZD-013
- **section 2, line 77:** - It draws on Salla's قيود الدفع, Zid's restrictions, Shopify's Payment Customization, WooCommerce's cash on delivery by shipping method and BigCommerce's countries per offline method. Q5-SA-046, Q5-ZD-013, Q5-SH-K1761, Q5-WC-004, Q5-BC-P0121
- **section 2, line 78:** - Why: rule 3; they are cheap to change, so they come late, as data the checkout reads. Q5-SA-043, Q5-SH-K1761
- **section 2, line 91:** - **Provider withdrawal**: what Sharrwah does when a provider or method stops at a place. Sharrwah removes it from the place's list and checkout after notice to the stores using it, unless the provider or a regulator ends it at once; methods carried only by that provider go with it; the merchant is asked to choose another provider; the integration stays callable for refunds and disputes on earlier payments; an add-on's developer keeps it working through a wind-down period; and, on a held route, the balance left is paid out. Q5-BC-102, Q5-SH-015, Q5-SA-K1654
- **section 2, line 94:** - Not taken: withdrawal without notice, which Shopify's, BigCommerce's and Salla's terms reserve, because a method withdrawn under the merchants leaves orders that "fail at checkout", as P24's did. Q5-SH-K2168, Q5-BC-K0455, Q5-SA-001, Q5-WC-015
- **section 3, line 100:** - Checkout payment rules can come from apps, as at Shopify, or from the merchant's settings. Q5-SH-K1761, Q5-SA-043
- **section 3, line 101:** - Recurring payments come through apps. Q5-SA-064
- **section 3, line 104:** - An offered method's conditions are set per plan, verification state and business type, by Sharrwah. Q5-SA-P0068, Q5-SA-K0091, Q5-ZD-K0042
- **section 3, line 105:** - Approval of the merchant is set per provider account, and a buyer's or order's eligibility per order, by the provider. Q5-BC-P0048, Q5-SA-066
- **section 3, line 108:** - Checkout payment rules are set per rule, by the merchant. Q5-SA-043, Q5-ZD-013
- **section 3, line 109:** - Amount limits are set per place by Sharrwah, as Salla's are by country, and per provider and method by the provider, as for Zid's MIS pay. Q5-SA-048, Q5-ZD-K0105
- **section 5, line 133:** - Which conditions a list entry may carry: plans gate methods on Salla and Zid, while a plan level was not in what was read on WooCommerce; the design keeps conditions as data. A company decision on plans settles it. Q5-SA-P0068, Q5-ZD-P0150, Q5-WC-N09
- **section 7, line 163:** - Whether plans limit which methods a store can offer. Q5-SA-P0068, Q5-ZD-P0150, Q5-WC-N09

## The cards

### Q5-SA-017

**Cited at:** section 1, line 7

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-017
- bears_on: 1;2
- identifier: ❓ كيف يمكنني تفعيل طرق الدفع في متجري؟
- statement: من صفحة (طرق الدفع)، اختر وسيلة الدفع المناسبة واضغط (تفعيل) ثم أكمل بياناتها.
- cite_ids: Q5-SA-C030
- from: held

**Citation Q5-SA-C030:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 874 (article dcrwxldslve7spa8eqdgii8g, تفعيل طرق الدفع في المتجر), paragraph 55 | 2026-08-31 | kind: stated | quote check: found
- quote: من صفحة (طرق الدفع)، اختر وسيلة الدفع المناسبة واضغط (تفعيل) ثم أكمل بياناتها.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …عددة. الأسئلة الشائعة ❓ ما هي طرق الدفع المتاحة في باقة بيسك؟ في باقة بيسك يمكنك تفعيل خيار التحويل البنكي، حيث يقوم العميل بتحويل مبلغ الطلب مباشرة من حسابه البنكي إلى حسابك. كما يمكنك تفعيل الدفع عند الاستلام ليتم تحصيل المبلغ عبر شركة الشحن أو من خلال مندوبك الخاص. أما طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط. ❓من يمكنه استخدام ميزة عرض رسالة التبرع؟ التجار الذين يستخدمون مدفوعات سلة فقط. ❓ كيف يمكنني تفعيل طرق الدفع في متجري؟ ⟪من صفحة (طرق الدفع)، اختر وسيلة الدفع المناسبة واضغط (تفعيل) ثم أكمل بياناتها.⟫ ❓هل تكون ميزة عرض رسالة التبرع مفعّلة تلقائياً؟ نعم، تكون مفعّلة تلقائياً لجميع المتاجر التي تعمل عبر مدفوعات سلة، باستثناء تجار سبيشل. ❓في أي حالات لا تظهر رسالة التبرع؟ لا تظهر رسالة التبرع للتجار في الإمارات أو للجمعيات الخيرية. ❓ هل يمكنني عرض الطلبات وفق طريقة الدفع؟ نعم ، من صفحة الطلبات، اضغط (تصفية). ثم حدد طرق الدفع التي ترغب بعرض الطلبات المُنجزة وفقها. cw4f6o6uybt0z2lbch0mpkxj https://help.salla.sa/article/%D8%AA%D9%81%D8%B9%D9%8A%D9%…

### Q5-SA-K1509

**Cited at:** section 1, line 8; section 2, line 73

**Record** (`studies/proposals/records/Q5/salla/copied.tsv`):
- concern_id: SA-C-110
- placement: decides
- structure: observed-sa@145f137:structures/salla/portal-stores-access-requests-permissions/partner@en/items.jsonl
- identifier: payment_methods_activation
- statement: "en": "payment method browse"}}, {"id": 1431054059, "key": "payment_methods_activation", "name": {"ar": "تفعيل وإلغاء تفعيل طرق الدفع", "en": "payment methods activation"}}, {"id": 657016308, "key": "bank_accounts_management", "name": {"ar": "إدارة الحسابات البنكية"
- cite_ids: SA-S-2644
- note: Permission a partner can request on a merchant's store, group المدفوعات / Payments.

**Citation SA-S-2644:** `observed-sa@145f137:structures/salla/portal-stores-access-requests-permissions/partner@en/items.jsonl` | line 12 (group Payments) | 2026-10-08 | kind: observed | quote check: found
- quote: "en": "payment method browse"}}, {"id": 1431054059, "key": "payment_methods_activation", "name": {"ar": "تفعيل وإلغاء تفعيل طرق الدفع", "en": "payment methods activation"}}, {"id": 657016308, "key": "bank_accounts_management", "name": {"ar": "إدارة الحسابات البنكية"
- in context: …tsapp chat browse"}}, {"id": 1895195893, "key": "export_logs_management", "name": {"ar": "سجل التصدير", "en": "export logs management"}}, {"id": 1121747958, "key": "custom_fields_management", "name": {"ar": "الحقول المخصصة", "en": "custom fields management"}}], "position": 10} {"id": 106115202, "name": {"ar": "المدفوعات", "en": "Payments"}, "permissions": [{"id": 1451175644, "key": "payment_method_browse", "name": {"ar": "الاطلاع على طرق الدفع", ⟪"en": "payment method browse"}}, {"id": 1431054059, "key": "payment_methods_activation", "name": {"ar": "تفعيل وإلغاء تفعيل طرق الدفع", "en": "payment methods activation"}}, {"id": 657016308, "key": "bank_accounts_management", "name": {"ar": "إدارة الحسابات البنكية"⟫, "en": "bank accounts management"}}, {"id": 1591178023, "key": "list_epayments", "name": {"ar": "المدفوعات الإلكترونية", "en": "list epayments"}}], "position": 11} {"id": 1345871747, "name": {"ar": "محلي", "en": "Mahally"}, "permissions": [{"id": 481927927, "key": "mahally_browse", "name": {"ar": "الإطلاع على محلي", "en": "mahally browse"}}, {"id": 1854325232, "key": "mahally_edit", "name": {"ar": "تعديل على محلي", "en": "mahally edit"}}], "posi…

### Q5-SA-043

**Cited at:** section 1, line 9; section 2, line 76; section 2, line 78; section 3, line 100; section 3, line 108

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-043
- bears_on: 1;2
- identifier: ثانياً- خطوات إضافة قيود الدفع > 5
- statement: 5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية: المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد. كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة. دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مثل وضع الطلب تحت المراجعة عند اختلاف دولة البطاقة عن دولة الشحن. مجموعة العملاء: يتيح لك تطبيق القيود على مجموعة محددة من العملاء، مثل إخفاء الدفع عند الاستلام عن مجموعة معينة مثلا منعها عن العملاء غير الجادين. تصنيفات محددة: يتيح لك تطبيق القيود عند وجود منتجات من تصنيفات محددة في السلة، مثل إخفاء الدفع عند الاستلام عند شراء منتجات من تصنيف العناية بالبشرة.
- cite_ids: Q5-SA-C066;Q5-SA-C067;Q5-SA-C068;Q5-SA-C069;Q5-SA-C070;Q5-SA-C071;Q5-SA-C072;Q5-SA-C073
- from: held

**Citation Q5-SA-C066:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 21 | 2026-09-29 | kind: stated | quote check: found
- quote: 5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية:
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …فع ). 2. من صفحة قيود الدفع، اضغط (إضافة قيد جديد). 3. أدخل اسم القيد بحيث يكون بسيطاً ومعبراً عن شروطه وإجراءاته، علماً أنه لن يظهر للعميل. 4. حدّد طريقة الدفع التي ترغب بتقييدها, ويمكنك تحديد أكثر من طريقة دفع معاً. 🔔 تنويه هام: طرق الدفع (ٍSTC pay, الدفع عن التسليم, حوالة بنكية) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. ⟪5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية:⟫ المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد. كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات ا…

**Citation Q5-SA-C067:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 22 | 2026-09-29 | kind: stated | quote check: found
- quote: المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …القيد بحيث يكون بسيطاً ومعبراً عن شروطه وإجراءاته، علماً أنه لن يظهر للعميل. 4. حدّد طريقة الدفع التي ترغب بتقييدها, ويمكنك تحديد أكثر من طريقة دفع معاً. 🔔 تنويه هام: طرق الدفع (ٍSTC pay, الدفع عن التسليم, حوالة بنكية) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. 5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية: ⟪المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد.⟫ كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمل…

**Citation Q5-SA-C068:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 23 | 2026-09-29 | kind: stated | quote check: found
- quote: كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …يد أكثر من طريقة دفع معاً. 🔔 تنويه هام: طرق الدفع (ٍSTC pay, الدفع عن التسليم, حوالة بنكية) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. 5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية: المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد. ⟪كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة.⟫ دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة. دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مث…

**Citation Q5-SA-C069:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 24 | 2026-09-29 | kind: stated | quote check: found
- quote: دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …في المملكة العربية السعودية فقط. 5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية: المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد. كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. ⟪دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة.⟫ دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة. دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مثل وضع الطلب تحت المراجعة عند اختلاف دولة البطاقة عن دولة الشحن. مجموعة العملاء: يتيح لك تطبيق القيود على مجموعة محددة م…

**Citation Q5-SA-C070:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 25 | 2026-09-29 | kind: stated | quote check: found
- quote: دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد. كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. ⟪دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة.⟫ دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مثل وضع الطلب تحت المراجعة عند اختلاف دولة البطاقة عن دولة الشحن. مجموعة العملاء: يتيح لك تطبيق القيود على مجموعة محددة من العملاء، مثل إخفاء الدفع عند الاستلام عن مجموعة معينة مثلا منعها عن العملاء غير الجادين. تصنيفات محددة: يتيح لك تطبيق القيود عند وجود منتجات…

**Citation Q5-SA-C071:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 26 | 2026-09-29 | kind: stated | quote check: found
- quote: دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مثل وضع الطلب تحت المراجعة عند اختلاف دولة البطاقة عن دولة الشحن.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة. ⟪دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مثل وضع الطلب تحت المراجعة عند اختلاف دولة البطاقة عن دولة الشحن.⟫ مجموعة العملاء: يتيح لك تطبيق القيود على مجموعة محددة من العملاء، مثل إخفاء الدفع عند الاستلام عن مجموعة معينة مثلا منعها عن العملاء غير الجادين. تصنيفات محددة: يتيح لك تطبيق القيود عند وجود منتجات من تصنيفات محددة في السلة، مثل إخفاء الدفع عند الاستلام عند شراء منتجات من تصنيف العناية بالبشرة. 📝 ملاحظة: إذا تم تفعيل الخيار واحتوت الس…

**Citation Q5-SA-C072:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 27 | 2026-09-29 | kind: stated | quote check: found
- quote: مجموعة العملاء: يتيح لك تطبيق القيود على مجموعة محددة من العملاء، مثل إخفاء الدفع عند الاستلام عن مجموعة معينة مثلا منعها عن العملاء غير الجادين.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة. دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مثل وضع الطلب تحت المراجعة عند اختلاف دولة البطاقة عن دولة الشحن. ⟪مجموعة العملاء: يتيح لك تطبيق القيود على مجموعة محددة من العملاء، مثل إخفاء الدفع عند الاستلام عن مجموعة معينة مثلا منعها عن العملاء غير الجادين.⟫ تصنيفات محددة: يتيح لك تطبيق القيود عند وجود منتجات من تصنيفات محددة في السلة، مثل إخفاء الدفع عند الاستلام عند شراء منتجات من تصنيف العناية بالبشرة. 📝 ملاحظة: إذا تم تفعيل الخيار واحتوت السلة على منتجات من التصنيفات المحددة في القيد، بالإضافة إلى منتجات من تصنيفات أخرى، فسيتم تطبيق الإجراء المحدد على الطلب. الشراء كضيف: يتيح لك تحديد…

**Citation Q5-SA-C073:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 28 | 2026-09-29 | kind: stated | quote check: found
- quote: تصنيفات محددة: يتيح لك تطبيق القيود عند وجود منتجات من تصنيفات محددة في السلة، مثل إخفاء الدفع عند الاستلام عند شراء منتجات من تصنيف العناية بالبشرة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ة أو رفض العمليات التي لا تتوافق مع الدولة المحددة. دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مثل وضع الطلب تحت المراجعة عند اختلاف دولة البطاقة عن دولة الشحن. مجموعة العملاء: يتيح لك تطبيق القيود على مجموعة محددة من العملاء، مثل إخفاء الدفع عند الاستلام عن مجموعة معينة مثلا منعها عن العملاء غير الجادين. ⟪تصنيفات محددة: يتيح لك تطبيق القيود عند وجود منتجات من تصنيفات محددة في السلة، مثل إخفاء الدفع عند الاستلام عند شراء منتجات من تصنيف العناية بالبشرة.⟫ 📝 ملاحظة: إذا تم تفعيل الخيار واحتوت السلة على منتجات من التصنيفات المحددة في القيد، بالإضافة إلى منتجات من تصنيفات أخرى، فسيتم تطبيق الإجراء المحدد على الطلب. الشراء كضيف: يتيح لك تحديد القيود على طرق الدفع عند إتمام العميل للطلب دون تسجيل الدخول إلى حسابه. الأسواق المتعددة: يتيح لك تخصيص طرق الدفع حسب السوق الذي يختاره العميل، مثل إ…

### Q5-SA-046

**Cited at:** section 1, line 9; section 2, line 77

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-046
- bears_on: 1
- identifier: ❓ الميزة متاحة في أي باقة؟
- statement: تخصيص قيود الدفع متاح في باقتي برو وسبيشل فقط.
- cite_ids: Q5-SA-C079
- from: held

**Citation Q5-SA-C079:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع), paragraph 56 | 2026-09-29 | kind: stated | quote check: found
- quote: تخصيص قيود الدفع متاح في باقتي برو وسبيشل فقط.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ادة تفعيله بنفس الطريقة في أي وقت. الأسئلة الشائعة ❓ أين يمكنني مراجعة العمليات المرفوضة أو التي هي قيد المراجعة؟ أولاً: العمليات المرفوضة ستظهر في عمليات الدفع الإلكتروني. لمزيد من التفاصيل حول سجل عمليات الدفع الإلكتروني ثانياً: الطلبات التي في انتظار المراجعة، ستظهر بشكل طبيعي ضمن الطلبات مع تنبيه صغير في قسم الدفع يفيد أن الطلب أُحيل للمراجعة بسبب أحد قيود الدفع. للمزيد من التفاصيل حول العمليات والإجراءات على الطلب ❓ الميزة متاحة في أي باقة؟ ⟪تخصيص قيود الدفع متاح في باقتي برو وسبيشل فقط.⟫ 💫 اجعل عمليات الدفع في متجرك أكثر تحكمًا. جرّب قيود الدفع وخصّص طرق الدفع بما يتناسب مع منتجات متجرك وعملائك، وابدأ اليوم بتطبيق القيود التي تلبي احتياجات متجرك. iz5t4pco8lhfu41usey0u53z https://help.salla.sa/article/%D8%A5%D8%B9%D8%AF%D8%A7%D8%AF-%D8%A5%D8%B5%D8%AF%D8%A7%D8%B1-%D9%81%D9%88%D8%A7%D8%AA%D9%8A%D8%B1-%D8%A7%D9%84%D8%B7%D9%84%D8%A8%D8%A7%D8%AA/iz5t4pco8lhfu41usey0u53z الهدف من إعداد إصدار فواتير الطلبات: ضبط خصائص ومكونات العناصر ال…

### Q5-SA-036

**Cited at:** section 1, line 10; section 2, line 68; section 2, line 69

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-036
- bears_on: 1
- identifier: ثانياً: تفعيل باي بال كوسيلة دفع في متجرك
- statement: 🔔 تنويه هام: وسائل الدفع (مدى, فيزا, Google Pay) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.
- cite_ids: Q5-SA-C055
- from: held

**Citation Q5-SA-C055:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 859 (article rkpltd2whn11d8f8v5ml53u8, تفعيل الربط مع باي بال paypal), paragraph 16 | 2026-09-22 | kind: stated | quote check: found
- quote: 🔔 تنويه هام: وسائل الدفع (مدى, فيزا, Google Pay) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …وة الأولى: إنشاء حساب باي بال في حال لم يكن لديك حساب على باي بال، يجب أن تسجل حساب جديد على باي بال. 1. من الصفحة الرئيسية لباي بال اضغط (Sign Up for Free). 2. اختر نوع الحساب، ثم أكمل إدخال البيانات المطلوبة. ثانياً: تفعيل باي بال كوسيلة دفع في متجرك 1. من قائمة (الكل)، اضغط (طرق الدفع ). 2. من قسم المحافظ الرقمية، اضغط على (PayPal). 3. أدخل البريد الإلكتروني الخاص بك في Paypal واضغط (حفظ). ستظهر وسيلة الدفع باي بال في صفحة إتمام الطلب بالشكل: ⟪🔔 تنويه هام: وسائل الدفع (مدى, فيزا, Google Pay) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.⟫ الأسئلة الشائعة ❓ ما هي المحافظ الرقمية؟ المحفظة الرقمية: هي تطبيق إلكتروني ينظم حركاتك المالية على الإنترنت ويحفظ بيانات بطاقتك الإئتمانية بشكل مشفر، مما يتيح لك إجراء المدفوعات بسهولة وأمان. يوفر متجرك الإلكتروني خيارات لتفعيل الدفع عبر المحافظ الرقمية مثل PayPal وSTC Pay، مما يسهل عليك إجراء المعاملات المالية عبر الإنترنت. 🔔 تنويه هام: وسيلة الدفع (STC Pay) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. ❓ ما هو الحد الأدنى لمجموع المبا…

### Q5-SA-P0068

**Cited at:** section 1, line 11; section 2, line 69; section 3, line 104; section 5, line 133; section 7, line 163

**The same record as Q3-SA-P0068,** whose card is in `Q3-salla-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: أما طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط.
- scope: 

### Q5-SA-K0091

**Cited at:** section 1, line 12; section 2, line 69; section 3, line 104

**Record** (`studies/proposals/records/Q5/salla/copied.tsv`):
- concern_id: SA-C-006
- placement: boundary
- structure: observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json
- identifier: common.verification_required_tooltip
- statement: مطلوب توثيق المتجر لتفعيل طريقة الدفع هذه.
- cite_ids: SA-S-0108

**Citation SA-S-0108:** `observed-sa@145f137:structures/salla/dashboard-translations/ar/payments.json` | common.verification_required_tooltip | 2026-10-08 | kind: observed | quote check: found
- quote: مطلوب توثيق المتجر لتفعيل طريقة الدفع هذه.
- in context: …ا واحدًا على الأقل. تأكد من إتاحة خيار الدفع عند الاستلام من إعدادات شركة الشحن. شروط الدفع عند الاستلام كجم إجراءات بيانات العميل ضيف العميل تاريخ العملية ضيف اعرف أكثر ملاحظات ملغاة مؤكدة مستردة حالة العملية تأكيد الطلب طباعة استرداد عكس العملية إلغاء إجراءات دفع بواسطة بطاقة تفاصيل الدفع بيانات الدفع عملية العملية حالة العملية ملغاة تم البدء مؤكدة مستردة جزئيًا بانتظار التأكيد جاري الاسترداد مستردة محفظة مستردة جزئياً محفظة مستردة رقم العملية ⟪مطلوب توثيق المتجر لتفعيل طريقة الدفع هذه.⟫ محافظ رقمية أدخل القيمة الإجمالية للطلب الرسوم المستقطعة من عمليات الدفع عبر شبكة {{method}}. رسوم مدى رسوم stc pay رسوم فيزا أو ماستركارد لا تُطبَّق رسوم إضافية عند الدفع باستخدام طرق الدفع التالية: اختر طريقة الدفع مدى stc pay فيزا أو ماستركارد تشمل خدمات حفظ بطاقة وعنوان العميل، الشراء السريع عبر Apple Pay، الحماية من الاحتيال، ومزايا أخرى من مدفوعات سلة. رسوم تجربة الشراء ({{amount}} ر.س) ضريبة القيمة المضافة المطبَّقة على رسوم وسيلة الدفع و…

### Q5-SA-K1653

**Cited at:** section 1, line 13

**The same record as Q1-SA-K1653,** whose card is in `Q1-salla-2.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: لن تتمكن من تفعيل مدفوعات سلة حاليًا لوجود ربط فعَّال مع تاب.
- scope: 

### Q5-SA-048

**Cited at:** section 1, line 16; section 2, line 69; section 3, line 109

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-048
- bears_on: 1;2
- identifier: ❓هل يمكنني رفع حد معاملات الدفع الإلكتروني؟
- statement: لا يمكن رفع الحد يدوياً، حيث يتم تحديده وفقاً للسياسات المحلية لكل دولة.
- scope: ميزة حدود معاملات الدفع الإلكتروني مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.
- cite_ids: Q5-SA-C081
- from: held

**Citation Q5-SA-C081:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 987 (article bqrpidrk4v27bhquze2a9blo, حدود معاملات الدفع الإلكتروني), paragraph 22 | 2026-08-31 | kind: stated | quote check: found
- quote: لا يمكن رفع الحد يدوياً، حيث يتم تحديده وفقاً للسياسات المحلية لكل دولة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …قسم (حدود معاملات الدفع الإلكتروني). ❓ هل تختلف حدود معاملات الدفع الإلكتروني بين متجر وآخر؟ نعم ، قد تختلف الحدود بين المتاجر بناءً على عدة عوامل مثل حجم المتجر، القطاع الذي ينتمي إليه، والسياسات التي تعتمدها سلة لحماية عمليات الدفع. كما يتم تحديث هذه الحدود بشكل دوري بناءً على متغيرات السوق وسياسات الجهات المعنية. لذا يُنصح بمراجعة صفحة حدود معاملات الدفع الإلكتروني بانتظام للاطلاع على آخر التحديثات. ❓هل يمكنني رفع حد معاملات الدفع الإلكتروني؟ ⟪لا يمكن رفع الحد يدوياً، حيث يتم تحديده وفقاً للسياسات المحلية لكل دولة.⟫ 🎯 لا تنتظر المفاجآت! راجع حدود معاملات الدفع الإلكتروني لتدير عملياتك بثقة وشفافية. ps7h1x68hdol062zqr45tm83 https://help.salla.sa/article/%D8%AD%D8%B3%D8%A7%D8%A8-%D8%A7%D9%84%D8%B9%D9%85%D9%8A%D9%84-%D8%A7%D9%84%D9%85%D9%88%D8%AD%D8%AF-%D8%B9%D9%84%D9%89-%D9%85%D8%AA%D8%A7%D8%AC%D8%B1-%D8%B3%D9%84%D8%A9/ps7h1x68hdol062zqr45tm83 أصبح بإمكان العميل تعديل جميع بياناته من صفحة واحدة بسهولة وسرعة، مما يختصر عليه الوقت ويُسهّل عليه إتمام عملية الشرا…

### Q5-SA-057

**Cited at:** section 1, line 17; section 2, line 65; section 2, line 66

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-057
- bears_on: 2
- identifier: gateway_settings.status_rejected_desc
- statement: فضلًا تواصل مع خدمة عملاء {{name}} لمعرفة أسباب الرفض.
- cite_ids: Q5-SA-C090
- from: held

**Citation Q5-SA-C090:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | gateway_settings.status_rejected_desc | 2026-10-08 | kind: observed | quote check: found
- quote: فضلًا تواصل مع خدمة عملاء {{name}} لمعرفة أسباب الرفض.
- in context: …ل","radio_request":"إرسال طلب فتح حساب أعمال","save":"حفظ","save_success":"حُفظت بيانات ربط {{name}} بنجاح.","settings_section":"الإعدادات","status_applied_desc":"ستصلك رسالة من فريق {{name}} عبر البريد الإلكتروني لتزويدك ببيانات الربط، بعد استلامها، عد لإكمال إعدادات الربط هنا.","status_applied_title":"أُرسل طلبك إلى {{name}} وجارٍ مراجعته","status_failed_retry":"إعادة المحاولة","status_failed_title":"تعذَّر إرسال الطلب","status_rejected_desc":"⟪فضلًا تواصل مع خدمة عملاء {{name}} لمعرفة أسباب الرفض.⟫","status_rejected_retry":"إعادة المحاولة","status_rejected_title":"عذرًا، تم رفض طلبك لفتح حساب للأعمال في {{name}}","toggle_error":"تعذَّر تحديث حالة بوابة الدفع.","toggle_success":"تم تحديث حالة {{name}} بنجاح.","tutorial_alert_link":"تواصل مع {{name}}","tutorial_alert_text":"ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة. لمعرفة المزيد،","verification_description":"وثِّق متجرك لتفعيل طرق الدفع وإدارة مدفوعاتك بأمان.","verification_requir…

### Q5-SA-066

**Cited at:** section 1, line 17; section 3, line 105

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-066
- bears_on: 1;2
- identifier: ماذا يحدث بعد التفعيل؟
- statement: بعد تفعيل تابي، يمكن أن تظهر كطريقة دفع متاحة للعملاء المؤهلين في صفحة إتمام الطلب. وتحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة.
- scope: الإمارات (article: تفعيل تابي على متجرك في سلة الإمارات | سلة)
- cite_ids: Q5-SA-C099
- from: held

**Citation Q5-SA-C099:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 866 (article wmmkc305vzb52ka2al4zbfrh, تفعيل تابي على متجرك في سلة الإمارات | سلة), paragraph 28 | 2026-09-16 | kind: stated | quote check: found
- quote: بعد تفعيل تابي، يمكن أن تظهر كطريقة دفع متاحة للعملاء المؤهلين في صفحة إتمام الطلب. وتحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … على سلة: من القائمة الرئيسية في لوحة تحكم سلة، افتح «الكل». من قسم «الإعدادات والأدوات»، اختر «طرق الدفع». انتقل إلى قسم «اشترِ الآن وادفع لاحقًا»، ثم اختر «تابي». أدخل Merchant Public Key وMerchant Private Key المرتبطين بحسابك لدى تابي. راجع إعدادات تابي المتاحة لمتجرك. وافق على شروط استخدام سلة، ثم اضغط «حفظ». مهم : إذا كان متجرك خارج السعودية، تواصل مع تابي مباشرة لاستكمال إعداد حساب التاجر وتفعيله قبل ربط الحساب بسلة. ماذا يحدث بعد التفعيل؟ ⟪بعد تفعيل تابي، يمكن أن تظهر كطريقة دفع متاحة للعملاء المؤهلين في صفحة إتمام الطلب. وتحدد تابي أهلية العميل أو الطلب لاستخدام الخدمة.⟫ كيف تعمل تابي؟ الشراء: يختار العميل تابي عند إتمام الطلب ويقدّم المعلومات التي تطلبها تابي. الدفع على دفعات: يختار العميل أحد خيارات الدفع المتاحة له من تابي. تنفيذ الطلب: تعالج الطلب وتشحنه كالمعتاد. وتتولى تابي تحصيل المدفوعات من العميل وفق شروطها، ويستلم متجرك مستحقاته وفق اتفاقية التاجر مع تابي. الأسئلة الشائعة ما فوائد إضافة تابي إلى متجري؟ تمنح تابي العملاء المؤهلين خيارات دفع أكثر مرونة، مما قد يساعد على زيادة القوة الشرائية، ورفع متوسط ق…

### Q5-SA-P0079

**Cited at:** section 1, line 23

**The same record as Q2-SA-P0079,** whose card is in `Q2-salla.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: توفّر منصة سلة عبر شركائها نظام الدفع والسداد في منصة سلّة فيمكن أن يتم عبر الانترنت كلياً من خلال خيارات الدفع المتوفرة على منصة سلّة أو من خلال أي طريقة دفع توفرها منصة سلّة من حين لآخر.
- scope: 

### Q5-SA-K1638

**Cited at:** section 1, line 24

**Record** (`studies/proposals/records/Q5/salla/copied.tsv`):
- concern_id: SA-C-120
- placement: where
- structure: https://help.salla.sa/article/-إدارة-طرق-الدفع-وتفعيل-المدفوعات-الإلكترونية/dtdojcntv3f4lwqzj4h0jvij
- identifier: أولاً: طريقة الوصول لصفحة طرق الدفع
- statement: بوابات الدفع الأخرى (ميسر - هايبر باي)
- cite_ids: SA-S-0069

**Citation SA-S-0069:** `https://help.salla.sa/article/-إدارة-طرق-الدفع-وتفعيل-المدفوعات-الإلكترونية/dtdojcntv3f4lwqzj4h0jvij` | أولاً: طريقة الوصول لصفحة طرق الدفع (line 696 of the rendered text) | 2026-08-22 | kind: stated | quote check: found
- quote: بوابات الدفع الأخرى (ميسر - هايبر باي)
- title: تفعيل طرق الدفع الإلكتروني في متجرك | مركز المساعدة - سلة
- the page opens: تفعيل طرق الدفع الإلكتروني في متجرك مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل…
- in context: …يقة الوصول لصفحة الدفع. - تخصيص المدفوعات الإلكترونية. - المحافظ الرقمية. - وسائل الدفع الآجلة. - الحسابات البنكية. أولاً: طريقة الوصول لصفحة طرق الدفع 1. من القائمة لوحة التحكم الجانبية، اضغط على (إعدادات المتجر). 2. من صفحة إعدادات المتجر، اضغط على (طرق الدفع). ستظهر صفحة الدفع الإلكتروني بالشكل التالي: وتتكون صفحة الدفع من الأقسام التالية: المدفوعات الإلكترونية، المدفوعات الأمنة والأكثر سهولة في التفعيل. المحافظ الرقمية مثل: paypal، وstc pay. ⟪بوابات الدفع الأخرى (ميسر - هايبر باي)⟫ وسائل الدفع الآجل مثل: تابي، وتمارا الحسابات البنكية. ثانياً: تخصيص المدفوعات الإلكترونية المدفوعات الإلكترونية: خدمة تقدمها سلة لمعالجة المدفوعات في متجرك بشكل مباشر، وإتمام العمليات المالية مع البنوك ووسائل الدفع المعتمدة في متجرك بشكل آلي. خطوات تفعيل المدفوعات الإلكترونية: من صفحة طرق الدفع، من المدفوعات الإلكترونية، اضغط على (تفعيل). بعد قراءة (سياسة البيع)، اضغط على (أوافق على سياسة البيع). أصبحت المدفوعات الإلكترونية جاهزة. الإعدادات الأس…

### Q5-SA-015

**Cited at:** section 1, line 25; section 2, line 56

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-015
- bears_on: 3
- identifier: 🚀 صفحة طرق الدفع
- statement: - طرق دفع أخرى - التحويل البنكي يمكنك إضافة أكثر من حساب بنكي إلى متجرك.
- cite_ids: Q5-SA-C026;Q5-SA-C027;Q5-SA-C028
- from: held

**Citation Q5-SA-C026:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 874 (article dcrwxldslve7spa8eqdgii8g, تفعيل طرق الدفع في المتجر), paragraph 31 | 2026-08-31 | kind: stated | quote check: found
- quote: - طرق دفع أخرى
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ن التفاصيل حول تفعيل المدفوعات الإلكترونية - وسائل الدفع الآجل (اشترِ الآن وادفع لاحقًا) مثل: تابي، تمارا، ميس باي، مدفوع، إمكان. لمزيد من التفاصيل حول: - تفعيل وسيلة الدفع الآجل تابي - تفعيل وسيلة الدفع الآجل تمارا - تفعيل وسيلة الدفع الآجل | مدفوع - تفعيل وسيلة الدفع الآجل Mispay - تفعيل وسلة الدفع الآجل | إمكان -المحافظ الرقمية مثل: paypal، حيث توفر سلة العديد من الخيارات في المحافظ الرقمية. لمزيد من التفاصيل حول تفعيل الربط مع باي بال paypal ⟪- طرق دفع أخرى⟫ - التحويل البنكي يمكنك إضافة أكثر من حساب بنكي إلى متجرك. لمزيد من التفاصيل حول إعداد الحساب البنكي ونظام الحوالات السريع إعدادات صفحة الدفع يمكنك التحكم بإعدادات الدفع من خلال تبويب ( صفحة إتمام الطلب ) في صفحة مركز الإعدادات الموحد. لمزيد من التفاصيل حول مركز الإعدادات الموحد. لمزيد من التفاصيل حول تفاصيل صفحة الدفع للعميل - حاسبة الرسوم يمكنك حساب الرسوم المترتبة على الطلبات من خلال إدخال قيمة الطلب في الحقل المخصص وتحديد طريقة الدفع، فتظهر ق…

**Citation Q5-SA-C027:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 874 (article dcrwxldslve7spa8eqdgii8g, تفعيل طرق الدفع في المتجر), paragraph 32 | 2026-08-31 | kind: stated | quote check: found
- quote: - التحويل البنكي
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …تفعيل المدفوعات الإلكترونية - وسائل الدفع الآجل (اشترِ الآن وادفع لاحقًا) مثل: تابي، تمارا، ميس باي، مدفوع، إمكان. لمزيد من التفاصيل حول: - تفعيل وسيلة الدفع الآجل تابي - تفعيل وسيلة الدفع الآجل تمارا - تفعيل وسيلة الدفع الآجل | مدفوع - تفعيل وسيلة الدفع الآجل Mispay - تفعيل وسلة الدفع الآجل | إمكان -المحافظ الرقمية مثل: paypal، حيث توفر سلة العديد من الخيارات في المحافظ الرقمية. لمزيد من التفاصيل حول تفعيل الربط مع باي بال paypal - طرق دفع أخرى ⟪- التحويل البنكي⟫ يمكنك إضافة أكثر من حساب بنكي إلى متجرك. لمزيد من التفاصيل حول إعداد الحساب البنكي ونظام الحوالات السريع إعدادات صفحة الدفع يمكنك التحكم بإعدادات الدفع من خلال تبويب ( صفحة إتمام الطلب ) في صفحة مركز الإعدادات الموحد. لمزيد من التفاصيل حول مركز الإعدادات الموحد. لمزيد من التفاصيل حول تفاصيل صفحة الدفع للعميل - حاسبة الرسوم يمكنك حساب الرسوم المترتبة على الطلبات من خلال إدخال قيمة الطلب في الحقل المخصص وتحديد طريقة الدفع، فتظهر قيمة الرسوم المترت…

**Citation Q5-SA-C028:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 874 (article dcrwxldslve7spa8eqdgii8g, تفعيل طرق الدفع في المتجر), paragraph 33 | 2026-08-31 | kind: stated | quote check: found
- quote: يمكنك إضافة أكثر من حساب بنكي إلى متجرك.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …لإلكترونية - وسائل الدفع الآجل (اشترِ الآن وادفع لاحقًا) مثل: تابي، تمارا، ميس باي، مدفوع، إمكان. لمزيد من التفاصيل حول: - تفعيل وسيلة الدفع الآجل تابي - تفعيل وسيلة الدفع الآجل تمارا - تفعيل وسيلة الدفع الآجل | مدفوع - تفعيل وسيلة الدفع الآجل Mispay - تفعيل وسلة الدفع الآجل | إمكان -المحافظ الرقمية مثل: paypal، حيث توفر سلة العديد من الخيارات في المحافظ الرقمية. لمزيد من التفاصيل حول تفعيل الربط مع باي بال paypal - طرق دفع أخرى - التحويل البنكي ⟪يمكنك إضافة أكثر من حساب بنكي إلى متجرك.⟫ لمزيد من التفاصيل حول إعداد الحساب البنكي ونظام الحوالات السريع إعدادات صفحة الدفع يمكنك التحكم بإعدادات الدفع من خلال تبويب ( صفحة إتمام الطلب ) في صفحة مركز الإعدادات الموحد. لمزيد من التفاصيل حول مركز الإعدادات الموحد. لمزيد من التفاصيل حول تفاصيل صفحة الدفع للعميل - حاسبة الرسوم يمكنك حساب الرسوم المترتبة على الطلبات من خلال إدخال قيمة الطلب في الحقل المخصص وتحديد طريقة الدفع، فتظهر قيمة الرسوم المترتبة على الطلب بالشكل: - حدود الدفع الإلكتر…

### Q5-SA-064

**Cited at:** section 1, line 26; section 3, line 101

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-064
- bears_on: 3
- identifier: ## Enabling Recurring Payments
- statement: Once enabled, the App can add subscription products to the cart and start processing recurring payments through the Recurring Payments API.
- cite_ids: Q5-SA-C097
- from: held

**Citation Q5-SA-C097:** `https://docs.salla.dev/recurring-payments/overview.md` | ## Enabling Recurring Payments | 2026-10-05 | kind: stated | quote check: found
- quote: Once enabled, the App can add subscription products to the cart and start processing recurring payments through the Recurring Payments API.
- title: Overview
- the page opens: The Recurring Payments feature enables merchants and third-party apps to offer subscription billing to customers. This feature provides comprehensive subscription lifecycle management through APIs, allowing you to create, charge, and manage recurring payments seamlessly. It supports full lifecycle operations, including subscription creation, invoicing, payment processing, renewal, and cancellation, using a consistent RESTful architecture. This API is designed for developers integrating recurring…
- headings: Overview > Enabling Recurring Payments > How to Enable Recurring Payments
- in context: … }' ``` </Tab> <Tab title="Response"> For this, the **reponse** will be: ``` { "status": 201, "success": true, "data": { "message": "The record has been updated successfully", "code": 201 } } ``` </Tab> </Tabs> <CardGroup cols={2}> <Card> :::info[Further Details] Refer to the following resources for full implementation details: 🔗 [Update Setting Slug](https://docs.salla.dev/6965780e0): Update individual settings. ::: </Card> <Card> :::note[Note] ⟪Once enabled, the App can add subscription products to the cart and start processing recurring payments through the Recurring Payments API.⟫ ::: </Card> </CardGroup> --- ## Process Flow The following diagrams illustrate the **end-to-end flow** of the Recurring Payments process, beginning from the checkout page where the merchant's customer submits payment. They show how the system validates the recurring configuration, processes the payment through the gateway, and emits webhook events to reflect successful or failed charge attempts within the subscription lifecycle. --- ### Subscrip…

### Q5-SA-001

**Cited at:** section 1, line 31; section 2, line 94

**Record** (`studies/proposals/records/Q5/salla/statements.tsv`):
- stmt_id: Q5-SA-001
- bears_on: 1;2;4
- identifier: المادة الثامنة – خدمات الدفع والسداد للمتاجر في منصة سلّة
- statement: لإدارة منصة سلّة الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع التي قامت بإتاحتها على منصة سلّة.
- cite_ids: Q5-SA-C001
- from: held

**Citation Q5-SA-C001:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/com-policies/terms/text.txt` | line 91 (المادة الثامنة – خدمات الدفع والسداد للمتاجر في منصة سلّة) | 2026-10-06 | kind: official page | quote check: found
- quote: لإدارة منصة سلّة الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع التي قامت بإتاحتها على منصة سلّة.
- in context: …، ولما في هذا التنظيم من مصالح قانونية واقتصادية وتجارية للتجار، وفي حالة مخالفة التاجر لأحكام هذا البند فإنه يُعَد مسئولاً عن أي أضرار قد تنشأ نتيجة هذه المخالفة. منصة سلّة لها الحق في منع استكمال إجراءات أي عملية دفع مخالفة لقواعد وأحكام اتفاقية الاستخدام أو إلغاء أي طلب شراء أو بيع نتيجة خطأ فني أو تقني في المنصة أدى إلى اختلاف الأسعار المعروضة على المنصة عن قيمة المنتج السوقية بما فيه خسارة لمنصة سلّة ولا تتحمل منصة سلّة مسئولية تلك المبالغ. ⟪لإدارة منصة سلّة الحق في إلغاء أو تعديل أو تغيير أي من وسائل الدفع التي قامت بإتاحتها على منصة سلّة.⟫ المادة التاسعة - معلوماتك الشخصية ومعلومات تفاصيل العمليات: لا مانع لديك بأن تمنح منصة سلّة حقاً غير محدود، وعالمي، ودائم وغير قابل للإلغاء، ومعفي من المصاريف، ومرخص، باستخدام معلومات أو مواد شخصية أو غير ذلك مما وفرتها أو زودت بها المنصة أو أعلنتها على المنصة من خلال انضمامك إليها أو تأسيسك لمتجرك، وذلك عبر النماذج المخصصة للتواصل والتسجيل، أو عبر أي رسائل إلكترونية أو أي من قنوات الاتصال المتاحة بالمنصة. وذلك بهدف تحقيق أي من المصالح التي تراه…

### Q5-SA-K1654

**Cited at:** section 1, line 35; section 2, line 58; section 2, line 59; section 2, line 60; section 2, line 91

**Record** (`studies/proposals/records/Q5/salla/copied.tsv`):
- concern_id: SA-C-120
- placement: decides
- structure: https://help.salla.sa/article/-الربط-مع-knet-tap/eqc4nnrdzbtzq3alko0asl3q
- identifier: شروط الربط مع Knet tap
- statement: يُشترط للربط مع K net tap تفعيل خدمة الدفع Tap أولاً، وفي حال تمّ إلغاء خدمة الدفع Tap سيتم إلغاء الربط مع K net tap تلقائياً.
- cite_ids: SA-S-0130

**Citation SA-S-0130:** `https://help.salla.sa/article/-الربط-مع-knet-tap/eqc4nnrdzbtzq3alko0asl3q` | شروط الربط مع Knet tap (line 654 of the rendered text) | 2026-08-18 | kind: stated | quote check: found
- quote: يُشترط للربط مع K net tap تفعيل خدمة الدفع Tap أولاً، وفي حال تمّ إلغاء خدمة الدفع Tap سيتم إلغاء الربط مع K net tap تلقائياً.
- title: تفعيل وسيلة الدفع كي نت Knet | مركز المساعدة - سلة
- the page opens: تفعيل وسيلة الدفع كي نت Knet مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حلول ت…
- in context: … SAFWAT ELFORSAN للخدمات اللوجستية عرض كل المقالات (43) ← مركز المساعدة مقالات قديمة - إدارة المدفوعات ومحفظة المتجر تفعيل طرق الدفع - الربط مع Knet tap هذه المقالة قديمة. يرجى زيارة المقالة الجديدة. المقالة الجديدة - الربط مع Knet tap تاريخ اخر تحديث: الثلاثاء 18 أغسطس 2026. ما هي Knet tap؟ إتمام عمليّة دفع إلكتروني باستخدام كي نت يمنحك الحماية عبر استخدام تقنية الOTP لتقديم حماية وأمان أكبر لمستخدمي البطاقات الإئتمانية. شروط الربط مع Knet tap: ⟪يُشترط للربط مع K net tap تفعيل خدمة الدفع Tap أولاً، وفي حال تمّ إلغاء خدمة الدفع Tap سيتم إلغاء الربط مع K net tap تلقائياً.⟫ خطوات الربط مع Knet tap: 1. من القائمة الجانبية للوحة التحكم، اضغط (إعدادات المتجر). 2. من صفحة إعدادات المتجر، اضغط (طرق الدفع). ثم اضغط (وسائل الدفع المفعلة). 3. من صفحة وسائل الدفع، من وسائل الدفع المتاحة، عيّن (كي-نت) ثم اضغط (حفظ). الأسئلة الشائعة ما هو رمز الOTP؟ OTP (رمز مرور لمرّة واحدة): وهي تقنية أمان تقوم بتوفير رمز مرور يمكن استخدامه لمرّة واحدة خلال فترة زمنية معيّنة، يعمل الOTP عن طريق إنتاج رمز مرور عشوائي مختلف عند كل محاولة دفع،…
