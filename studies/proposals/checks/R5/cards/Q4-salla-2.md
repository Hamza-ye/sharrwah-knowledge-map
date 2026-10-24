# Cards: Q4 on salla

14 records cited by `studies/proposals/drafts/Q4/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 35:** - **By place.** Shopify and Salla limit methods by the seller's country (role, basis 4, both stated): Shopify offers email money transfers only to merchants in Canada (not checked on Zid); Salla's help says its STC pay, الدفع عن التسليم and حوالة بنكية are "مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط" (29 September 2026). Q4-SH-027, Q4-SA-054
- **section 1, line 36:** - Salla's records disagree on cash on delivery in the UAE: that help limits it to Saudi stores, while its UAE article (12 September 2026) says "يمكنك تفعيل الدفع عند الاستلام". The proposal rests on neither for the UAE, only on availability being set per country. Q4-SA-054, Q4-SA-K1530
- **section 1, line 38:** - **By plan.** Salla offers bank transfer and cash on delivery on its basic plan, where "طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط" (stated); Zid's plan comparison (shipped) offers Bank Transfer Payment on all four plans. Q4-SA-P0099, Q4-SA-P0068, Q4-ZD-K0126
- **section 1, line 39:** - **The seller's conditions.** Salla's قيود الدفع and Zid's قيود الشحن و الدفع, rules the seller sets to hide a method, match in part on term (basis 1, both stated). Salla's can hide cash on delivery above a cart value; Zid's, from its growth plan up, act on cart value, products, weight, customer group, the customer's location and the customer's cancelled orders, against "طلبات الدفع عند الاستلام الوهمية". In Salla's dashboard text (recorded session, 12 October 2026), cash on delivery can also be hidden from "العملاء المحظورين في متاجر سلة الأخرى". Q4-SA-055, Q4-ZD-026, Q4-ZD-K0357, Q4-SA-029
- **section 1, line 40:** - **By carrier, courier or shipping method** (role, basis 4, all stated). On Salla "يمكن تفعيل أو تعطيل الدفع عند الاستلام بشكل مستقل لكل مندوب أو تسعيرة"; Zid's cash on delivery is turned on per carrier; WooCommerce's merchant chooses "which shipping methods and rates will offer COD". Q4-SA-P0199, Q4-ZD-K0111, Q4-WC-033
- **section 1, line 45:** - **Salla.** With بوليصات سلة, cash on delivery is collected through the carriers ("يتم تحصيلها من خلال شركات الشحن") and "يتم تحويلها لاحقًا إلى حساب المتجر وفق دورة التحويل المحددة", on "يومي الأحد والأربعاء لجميع شركات الشحن ضمن بوليصات سلة" (stated). In its dashboard text (recorded session, 8 October 2026), "تحوِّل شركة الشحن المبلغ إلى سلة". Q4-SA-P0038, Q4-SA-P0093, Q4-SA-P0042
- **section 1, line 46:** - Who collects and holds those amounts before payout was not in what was read. Salla's usage agreement (6 October 2026) says "ليس هناك أي علاقة لمنصة سلة بطريقة الدفع عند الاستلام", while its help (7 October 2026) describes the dues reaching the store's account: records that may disagree. The proposal rests on the help for the flow, and on neither for who holds the money. Q4-SA-G0117, Q4-SA-P0080, Q4-SA-P0038
- **section 1, line 49:** - Salla and Zid match on role (basis 4): cash on delivery taken through the platform's own shipping service reaches the seller on the platform's cycle, into the store's account on Salla and, after Zid's fee, into the merchant's wallet on Zid. Salla's evidence is its help (stated), Zid's its terms (official page). Q4-SA-P0038, Q4-ZD-K0117, Q4-ZD-K0119
- **section 2, line 59:** - Why: rule 1, as which kinds a place offers is set up in the **Availability rule**, the way Salla limits methods by the seller's country; rule 2, as each kind sits behind one interface (name, instructions, availability, how its payment is recorded), so a kind one place needs is added without changing orders. Q4-SA-054
- **section 2, line 60:** - Alternative not taken: cash on delivery only as a seller-named method, as Shopify's Help Center has sellers in Italy set it up. Cash on delivery is tied to couriers, carriers and shipping methods on Salla, Zid and WooCommerce, which a seller-named method can't carry (rule 2). Q4-SH-045, Q4-SA-P0199, Q4-WC-033
- **section 2, line 62:** - Why: rule 1. The fields that identify an account (on Salla: bank, holder, account number, IBAN) are set per place: Zid's IBAN must start with SA or AE, and Salla's نظام الحوالات السريع identifier is for Saudi stores only. Q4-SA-004, Q4-ZD-006, Q4-SA-005
- **section 2, line 63:** - It is kept apart from any account Sharrwah might pay a seller into, which belongs to an arrangement under the guard; Salla's help, too, names the bank account within payment methods as the one "لاستقبال المدفوعات من عملائك عبر التحويل البنكي". Q4-SA-P0100
- **section 2, line 79:** - **Availability rule**: whether a seller-collected method shows to a buyer is decided at three levels: Sharrwah, per place, sets which kinds stores there may offer; the seller, per store, turns each on and sets conditions (order value, weight, products, customer group, the buyer's area, the buyer's cancelled orders, shipping method or courier); and a courier or carrier decides whether it collects cash at all. Q4-SA-054, Q4-ZD-026, Q4-SA-066
- **section 2, line 80:** - It draws on Salla's and Zid's seller-set restrictions, and on cash on delivery set per courier, carrier or shipping method on Salla, Zid and WooCommerce. Q4-SA-055, Q4-SA-P0199, Q4-ZD-K0111, Q4-WC-033
- **section 2, line 81:** - Why: rule 1 for the place level, which is set up, not built apart; rule 2 for the conditions, which sit behind one rule so that a new condition changes no method. Q4-SA-054
- **section 2, line 82:** - Alternative not taken: BigCommerce's merchant-set Available Countries as the only control of place. Salla's limit by the seller's country is one a seller can't set (rule 1); the buyer's area stays among the seller's conditions. Q4-BC-P0121, Q4-SA-054
- **section 2, line 83:** - Not proposed: hiding cash on delivery from buyers banned in other stores, as Salla can, which shares a buyer's record across sellers; it is a company decision (section 7). Q4-SA-029
- **section 2, line 90:** - **Collection-on-delivery service**: a service in which a courier or carrier working with Sharrwah collects cash at delivery, and the seller receives it after the service's deductions, on the service's schedule. The design would give it a part of its own. Where it holds sellers' money through Sharrwah, or through a payment company in an account opened through Sharrwah, it goes live anywhere only by the founder's decision. Q4-SA-P0038, Q4-ZD-K0122
- **section 2, line 91:** - It draws on Salla's label carriers, whose cash reaches the store's account on a set cycle, Zid's service collecting "نيابة عن التاجر" into محفظة التاجر after a separate fee, and WooPayments' card payment at delivery. Q4-SA-P0093, Q4-ZD-K0122, Q4-ZD-K0119, Q4-WC-036
- **section 3, line 101:** - **Plugs in:** couriers and carriers that collect cash for the seller, each turned on for cash on delivery on its own. Q4-SA-P0199, Q4-ZD-K0111
- **section 3, line 102:** - **Plugs in:** a **Collection-on-delivery service** provider, only by the founder's decision. Q4-SA-P0042, Q4-ZD-K0122
- **section 3, line 103:** - **Set per place:** the kinds offered, and a **Receiving account**'s fields. Q4-SA-054, Q4-ZD-006
- **section 3, line 110:** - **Set by Sharrwah:** the kinds per place, plan entitlements, any charge, and, only by the founder's decision, a collection service. Q4-SA-054, Q4-BC-012
- **section 3, line 112:** - **Set by the courier or carrier:** whether it collects cash, and how it settles with the seller; on Salla "تختلف طرق تسوية مبالغ الدفع عند الإستلام بحسب سياسة شركة الشحن", and cash on delivery must be turned on in the carrier's settings. Q4-SA-P0202, Q4-SA-066
- **section 5, line 132:** - Who holds the cash a **Collection-on-delivery service** collects, between delivery and the seller: Sharrwah, a payment company, or the carrier paying the seller directly. Salla's carriers transfer to Salla and Zid collects on the merchant's behalf, but in what capacity Salla holds the amounts was not in what was read. The design keeps the service in a part of its own, with its own kind of entry, and gives no other part a balance of sellers' money. Settled by the founder's decision under the guard, with the company decisions on carriers and licences (section 7). Q4-SA-P0042, Q4-ZD-K0122, Q4-SA-G0117
- **section 5, line 134:** - The fields of a **Receiving account** in each place. The design keeps them per place. Settled by each place's banking facts (Yemen's in section 6). Q4-ZD-006, Q4-SA-005
- **section 5, line 138:** - Whether a buyer's record in one store may change what another store offers that buyer. The design keeps buyer conditions within one store. Settled by the company decision in section 7. Q4-SA-029
- **section 7, line 158:** - Will Sharrwah offer a collection-on-delivery service, with which carriers or couriers, and who would hold the cash before the seller is paid? Q4-SA-P0042, Q4-ZD-K0122, Q4-SA-G0117
- **section 7, line 161:** - May a buyer's cash-on-delivery history in one store change what other stores offer that buyer? Q4-SA-029
- **section 7, line 162:** - Which couriers and carriers will Sharrwah work with for cash on delivery, and on what terms? Q4-SA-P0093, Q4-ZD-K0111

## The cards

### Q4-SA-054

**Cited at:** section 1, line 35; section 1, line 36; section 2, line 59; section 2, line 79; section 2, line 81; section 2, line 82; section 3, line 103; section 3, line 110

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-054
- bears_on: 4
- identifier: ثانياً- خطوات إضافة قيود الدفع
- statement: 🔔 تنويه هام: طرق الدفع (ٍSTC pay, الدفع عن التسليم, حوالة بنكية) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.
- scope: المملكة العربية السعودية
- cite_ids: Q4-SA-C086
- from: held

**Citation Q4-SA-C086:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع) | 2026-09-29 | kind: stated | quote check: found
- quote: 🔔 تنويه هام: طرق الدفع (ٍSTC pay, الدفع عن التسليم, حوالة بنكية) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … عبر تقييد وسائل الدفع للمنتجات الحساسة مثل الأجهزة الإلكترونية، يتم ضمان جدية العملاء وتقليل الإلغاءات غير الضرورية. ثانياً- خطوات إضافة قيود الدفع 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( قيود الدفع ). 2. من صفحة قيود الدفع، اضغط (إضافة قيد جديد). 3. أدخل اسم القيد بحيث يكون بسيطاً ومعبراً عن شروطه وإجراءاته، علماً أنه لن يظهر للعميل. 4. حدّد طريقة الدفع التي ترغب بتقييدها, ويمكنك تحديد أكثر من طريقة دفع معاً. ⟪🔔 تنويه هام: طرق الدفع (ٍSTC pay, الدفع عن التسليم, حوالة بنكية) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.⟫ 5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية: المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد. كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. دولة العميل / IP Address: …

### Q4-SA-K1530

**Cited at:** section 1, line 36

**Record** (`studies/proposals/records/Q4/salla/copied.tsv`):
- concern_id: SA-C-110
- placement: decides
- structure: https://help.salla.sa/article/تفعيل-طرق-الدفع-في-المتجر-الإمارات/z2mys3spo71u3yovhs7lhii4
- identifier: الأسئلة الشائعة
- statement: يمكنك تفعيل الدفع عند الاستلام. أما طرق الدفع الإلكترونية فتتوفر على الباقات المدفوعة المؤهلة.
- scope: الإمارات (article: تفعيل مدفوعات سلة في الإمارات)
- cite_ids: SA-S-0060

**Citation SA-S-0060:** `https://help.salla.sa/article/تفعيل-طرق-الدفع-في-المتجر-الإمارات/z2mys3spo71u3yovhs7lhii4` | الأسئلة الشائعة (line 849 of the rendered text) | 2026-09-12 | kind: stated | quote check: found
- quote: يمكنك تفعيل الدفع عند الاستلام. أما طرق الدفع الإلكترونية فتتوفر على الباقات المدفوعة المؤهلة.
- title: تفعيل مدفوعات سلة في الإمارات | سلة | مركز المساعدة - سلة
- the page opens: تفعيل مدفوعات سلة في الإمارات سلة مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل ح…
- in context: …كم متجرك. مقالات ذات صلة تفعيل التاجر لمحفظة العميل. إعدادات صفحة إتمام الطلب يمكنك إدارة إعدادات الدفع المرتبطة بصفحة إتمام الطلب من تبويب (صفحة إتمام الطلب) في مركز الإعدادات الموحد. مقالات ذات صلة مركز الإعدادات الموحد في لوحة تحكم سلة تفاصيل صفحة إتمام الطلب للعميل -توثيق متجرك في الإمارات | سلة -تحويلات مدفوعات سلة والتسويات في الإمارات | سلة -تفعيل شركات الشحن بعقدك الخاص في الإمارات | سلة الأسئلة الشائعة ما طرق الدفع المتاحة في باقة بيسك؟ ⟪يمكنك تفعيل الدفع عند الاستلام. أما طرق الدفع الإلكترونية فتتوفر على الباقات المدفوعة المؤهلة.⟫ هل يمكنني تفعيل المدفوعات الإلكترونية قبل توثيق المتجر؟ لا. يجب إكمال توثيق المتجر قبل تفعيل مدفوعات سلة. متى تظهر أدوات التحكم في طرق الدفع بعد الضغط على «تفعيل»؟ بعد التفعيل، تظهر أدوات التحكم لتتمكن من تشغيل طرق الدفع المتاحة أو إيقافها. إذا كان متجرك موثقًا وما زال طلب التفعيل يظهر «قيد المراجعة»، تواصل مع دعم سلة، فقد تكون هناك معلومات إضافية مطلوبة. ما طرق الدفع المتاحة عبر مدفوعات سلة في الإمارات؟ فيزا، ماستركارد، وApple Pay. ما خيارات «ا…

### Q4-SA-P0068

**Cited at:** section 1, line 38

**The same record as Q3-SA-P0068,** whose card is in `Q3-salla-1.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: أما طرق الدفع الإلكترونية فهي متاحة ضمن الباقات المدفوعة فقط.
- scope: 

### Q4-SA-055

**Cited at:** section 1, line 39; section 2, line 80

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-055
- bears_on: 4
- identifier: 5. أضف قيد الدفع أو أكثر من قيد معاً
- statement: المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد.
- scope: قيود الدفع
- cite_ids: Q4-SA-C087
- from: held

**Citation Q4-SA-C087:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 166 (article d9me3k8vqi09hdiun8r2ngfr, إعدادات قيود الدفع) | 2026-09-29 | kind: stated | quote check: found
- quote: المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …الكل)، من قسم الإعدادات والأدوات، اضغط ( قيود الدفع ). 2. من صفحة قيود الدفع، اضغط (إضافة قيد جديد). 3. أدخل اسم القيد بحيث يكون بسيطاً ومعبراً عن شروطه وإجراءاته، علماً أنه لن يظهر للعميل. 4. حدّد طريقة الدفع التي ترغب بتقييدها, ويمكنك تحديد أكثر من طريقة دفع معاً. 🔔 تنويه هام: طرق الدفع (ٍSTC pay, الدفع عن التسليم, حوالة بنكية) مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. 5. أضف قيد الدفع أو أكثر من قيد معاً، حيث تشمل الأنواع التالية: ⟪المبلغ المدفوع: يتيح لك تطبيق القيود بناءً على قيمة السلة، مثل إخفاء الدفع عند الاستلام إذا كانت قيمة الطلب أعلى من مبلغ محدد.⟫ كمية المنتجات: يتيح لك تحديد القيود بناءً على كمية المنتجات في السلة، مثل منع العميل من شراء أكثر من كمية معينة. دولة العميل / مفتاح الجوال: يتحقق من دولة رقم جوال العميل، ويمكن استخدامه للسماح أو منع عمليات الدفع بناءً على الدولة. دولة العميل / IP Address: يتحقق من الدولة المرتبطة بعنوان IP للعميل، ويمكن استخدامه لمراجعة أو رفض العمليات التي لا تتوافق مع الدولة المحددة. دولة البطاقة الائتمانية: يتحقق من دولة إصدار البطاقة المستخدمة في الدفع، مث…

### Q4-SA-029

**Cited at:** section 1, line 39; section 2, line 83; section 5, line 138; section 7, line 161

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-029
- bears_on: 4
- identifier: cod.disable_cod_for_banned_customers_desc (disable_cod_for_banned_customers_label: إخفاء الدفع عند الاستلام عن العملاء غير الجادين)
- statement: سيُخفى خيار الدفع عند الاستلام عن العملاء المحظورين في متاجر سلة الأخرى.
- scope: شروط الدفع عند الاستلام
- cite_ids: Q4-SA-C046;Q4-SA-C045
- from: held

**Citation Q4-SA-C046:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | key "cod.disable_cod_for_banned_customers_desc" | 2026-10-12 | kind: observed | quote check: found
- quote: "disable_cod_for_banned_customers_desc":"سيُخفى خيار الدفع عند الاستلام عن العملاء المحظورين في متاجر سلة الأخرى."
- in context: …","title":"اربط حسابك في {{name}} مع سلة"},"description":"فعِّل طرق الدفع الإلكترونية بسهولة عبر بوابات الدفع المتاحة.","gateways_title":"بوابات الدفع","title":"طرق الدفع للجمعيات الخيرية"},"cod":{"categories_excluded_from_cod_desc":"حدِّد التصنيفات التي لا تقبل منتجاتها الدفع عند الاستلام.","categories_excluded_from_cod_label":"استثناء تصنيفات من الدفع عند الاستلام","disable_cod_for_banned_customers":"تعطيل الدفع عند الاستلام للعملاء المحظورين",⟪"disable_cod_for_banned_customers_desc":"سيُخفى خيار الدفع عند الاستلام عن العملاء المحظورين في متاجر سلة الأخرى."⟫,"disable_cod_for_banned_customers_label":"إخفاء الدفع عند الاستلام عن العملاء غير الجادين","excluded":"استثناء","field_required":"هذا الحقل مطلوب.","included_categories":"التصنيفات المشمولة","included_products":"المنتجات المشمولة","maximum_amount":"الحد الأقصى لقيمة الطلب","maximum_amount_desc":"إذا كانت شركة الشحن ضمن بوليصات سلة، فسيُطبَّق حد أقصى قدره {{amount}} <c></c>.","maximum_weight":"الحد الأقصى لوزن المنتجات في السلة","min_exceeds_max_…

**Citation Q4-SA-C045:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | key "cod.disable_cod_for_banned_customers_label" | 2026-10-12 | kind: observed | quote check: found
- quote: "disable_cod_for_banned_customers_label":"إخفاء الدفع عند الاستلام عن العملاء غير الجادين"
- in context: …حة.","gateways_title":"بوابات الدفع","title":"طرق الدفع للجمعيات الخيرية"},"cod":{"categories_excluded_from_cod_desc":"حدِّد التصنيفات التي لا تقبل منتجاتها الدفع عند الاستلام.","categories_excluded_from_cod_label":"استثناء تصنيفات من الدفع عند الاستلام","disable_cod_for_banned_customers":"تعطيل الدفع عند الاستلام للعملاء المحظورين","disable_cod_for_banned_customers_desc":"سيُخفى خيار الدفع عند الاستلام عن العملاء المحظورين في متاجر سلة الأخرى.",⟪"disable_cod_for_banned_customers_label":"إخفاء الدفع عند الاستلام عن العملاء غير الجادين"⟫,"excluded":"استثناء","field_required":"هذا الحقل مطلوب.","included_categories":"التصنيفات المشمولة","included_products":"المنتجات المشمولة","maximum_amount":"الحد الأقصى لقيمة الطلب","maximum_amount_desc":"إذا كانت شركة الشحن ضمن بوليصات سلة، فسيُطبَّق حد أقصى قدره {{amount}} <c></c>.","maximum_weight":"الحد الأقصى لوزن المنتجات في السلة","min_exceeds_max_error":"يجب أن يكون الحد الأدنى أقل من الحد الأقصى.","minimum_amount":"الحد الأدنى لقيمة ال…

### Q4-SA-P0199

**Cited at:** section 1, line 40; section 2, line 60; section 2, line 80; section 3, line 101

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-198
- bullet: a;end-payment
- placement: decides
- identifier: تفعيل الدفع عند الاستلام (إدارة المناديب والشركات الخاصة)
- statement: مثال: إذا كان المندوب يقدم خدمة تحصيل المبالغ عند التسليم، فعّل هذا الخيار لإتاحة الدفع عند الاستلام للعملاء.
- scope: مناديب المتجر: مندوب محلي أو شركة شحن خارجية غير مرتبطة مباشرة بسلة
- cite_ids: S01-SA-C307;S01-SA-C308;S01-SA-C309
- from: new
- note: Phase A2 (S01-VP-06). The option it gives the example for: 'يمكنك السماح للعملاء باستخدام الدفع عند الاستلام عند اختيار هذا المندوب.' (second citation); the FAQ: 'نعم ، يمكن تفعيل أو تعطيل الدفع عند الاستلام بشكل مستقل لكل مندوب أو تسعيرة بحسب إعداداتك.' (third). Salla's English for مناديب المتجر and مندوب جديد is 'Store delivery agents' and 'New delivery agent' (terms.tsv); the held English version of this article (en line 826) calls them private couriers and has no paragraph on cash on delivery.

**Citation S01-SA-C307:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 77 (article bd1gqp671opnoppoa52oi6w4, إدارة المناديب والشركات الخاصة), paragraph 45 | 2026-08-31 | kind: stated | quote check: found
- quote: مثال: إذا كان المندوب يقدم خدمة تحصيل المبالغ عند التسليم، فعّل هذا الخيار لإتاحة الدفع عند الاستلام للعملاء.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ن المدن المدعومة. المدن المستثناة: استخدم هذا الخيار لاستثناء مدن معينة من التسعيرة المحددة. 💡 مثال: إذا اخترت جميع مدن السعودية ولكنك لا ترغب في الشحن إلى بعض المدن البعيدة، يمكنك إضافتها ضمن المدن المستثناة. مدة الشحن: حدد المدة المتوقعة لوصول الشحنة إلى العميل. 💡 مثال: 1-2 يوم عمل أو 3-5 أيام عمل. تظهر هذه المدة للعميل أثناء اختيار طريقة الشحن. تفعيل الدفع عند الاستلام يمكنك السماح للعملاء باستخدام الدفع عند الاستلام عند اختيار هذا المندوب. 💡 ⟪مثال: إذا كان المندوب يقدم خدمة تحصيل المبالغ عند التسليم، فعّل هذا الخيار لإتاحة الدفع عند الاستلام للعملاء.⟫ إدارة المناديب إخفاء مندوب من خيارات الشحن يُعد هذا الخيار مناسباً عند توقف المندوب مؤقتاً أو عند الرغبة في إيقاف استقبال الطلبات عبره. من صفحة المناديب وشركات الشحن الخاصة، اختر حالة المندوب (تفعيل) أو (تعطيل | إخفاء شركة الشحن من صفحة الشراء). حذف مندوب لحذف مندوب أو شركة شحن، من صفحة المناديب اضغط حذف. أكد عملية الحذف. ملاحظة : لا يمكن التراجع عن عملية الحذف بعد تنفيذها. الأسئلة الشائعة ❓ هل يمكن إضافة أكثر من تسعيرة للمندوب نفسه؟ نعم ، يمكنك…

**Citation S01-SA-C308:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 77 (article bd1gqp671opnoppoa52oi6w4, إدارة المناديب والشركات الخاصة), paragraph 44 | 2026-08-31 | kind: stated | quote check: found
- quote: يمكنك السماح للعملاء باستخدام الدفع عند الاستلام عند اختيار هذا المندوب.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …حددة فقط. 💡 مثال: إذا كان المندوب يغطي الرياض والخرج فقط، يمكنك إضافتهما ضمن المدن المدعومة. المدن المستثناة: استخدم هذا الخيار لاستثناء مدن معينة من التسعيرة المحددة. 💡 مثال: إذا اخترت جميع مدن السعودية ولكنك لا ترغب في الشحن إلى بعض المدن البعيدة، يمكنك إضافتها ضمن المدن المستثناة. مدة الشحن: حدد المدة المتوقعة لوصول الشحنة إلى العميل. 💡 مثال: 1-2 يوم عمل أو 3-5 أيام عمل. تظهر هذه المدة للعميل أثناء اختيار طريقة الشحن. تفعيل الدفع عند الاستلام ⟪يمكنك السماح للعملاء باستخدام الدفع عند الاستلام عند اختيار هذا المندوب.⟫ 💡 مثال: إذا كان المندوب يقدم خدمة تحصيل المبالغ عند التسليم، فعّل هذا الخيار لإتاحة الدفع عند الاستلام للعملاء. إدارة المناديب إخفاء مندوب من خيارات الشحن يُعد هذا الخيار مناسباً عند توقف المندوب مؤقتاً أو عند الرغبة في إيقاف استقبال الطلبات عبره. من صفحة المناديب وشركات الشحن الخاصة، اختر حالة المندوب (تفعيل) أو (تعطيل | إخفاء شركة الشحن من صفحة الشراء). حذف مندوب لحذف مندوب أو شركة شحن، من صفحة المناديب اضغط حذف. أكد عملية الحذف. ملاحظة : لا ي…

**Citation S01-SA-C309:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 77 (article bd1gqp671opnoppoa52oi6w4, إدارة المناديب والشركات الخاصة), paragraph 64 | 2026-08-31 | kind: stated | quote check: found
- quote: نعم ، يمكن تفعيل أو تعطيل الدفع عند الاستلام بشكل مستقل لكل مندوب أو تسعيرة بحسب إعداداتك.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … أكثر من تسعيرة للمندوب الواحد وتخصيص كل تسعيرة لدولة أو مدينة مختلفة. ❓ هل يمكن إخفاء المندوب دون حذفه؟ نعم ، يمكنك تغيير حالة المندوب إلى غير نشط وسيختفي من خيارات الشحن دون فقدان إعداداته. ❓ هل يمكن تخصيص رسوم مختلفة لمدن مختلفة؟ نعم ، من خلال إنشاء تسعيرات متعددة وربط كل تسعيرة بالمدن المناسبة. ❓ هل تظهر مدة الشحن للعميل؟ نعم ، تظهر المدة التي تحددها للمندوب أثناء اختيار العميل لخيار الشحن. ❓ هل يمكن تفعيل الدفع عند الاستلام لمندوب معين فقط؟ ⟪نعم ، يمكن تفعيل أو تعطيل الدفع عند الاستلام بشكل مستقل لكل مندوب أو تسعيرة بحسب إعداداتك.⟫ xltpy21ggchqzpqwha1000uy https://help.salla.sa/article/%D8%A5%D8%AF%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA-%D9%88%D8%AA%D8%AE%D8%B5%D9%8A%D8%B5-%D8%B7%D8%B1%D9%8A%D9%82%D8%A9-%D8%B9%D8%B1%D8%B6%D9%87%D8%A7/xltpy21ggchqzpqwha1000uy يسهّل جدول إدارة المنتجات إدارة كتالوج متجرك من خلال واجهة مرنة تتيح لك تعديل بيانات المنتجات مباشرة، وتخصيص طريقة عرض الجدول بما يتناسب مع احتياجاتك، وتنفيذ الإجراءات المجمعة على عدة منتجات…

### Q4-SA-P0038

**Cited at:** section 1, line 45; section 1, line 46; section 1, line 49; section 2, line 90

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-037
- bullet: a;c;end-payment;end-payout
- placement: boundary
- identifier: 💵 رصيد المدفوعات عند الاستلام
- statement: يُخصص تبويب المدفوعات عند الاستلام لعرض جميع المستحقات الناتجة عن الطلبات التي تم دفعها عبر خدمة الدفع عند الاستلام، والتي يتم تحصيلها من خلال شركات الشحن، ويتم تحويلها لاحقًا إلى حساب المتجر وفق دورة التحويل المحددة.
- cite_ids: S01-SA-C037
- from: new

**Citation S01-SA-C037:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 664 (article g36cl2hlsv256gr55vutx5rv, صفحة المحفظة), paragraph 59 | 2026-10-07 | kind: stated | quote check: found
- quote: يُخصص تبويب المدفوعات عند الاستلام لعرض جميع المستحقات الناتجة عن الطلبات التي تم دفعها عبر خدمة الدفع عند الاستلام، والتي يتم تحصيلها من خلال شركات الشحن، ويتم تحويلها لاحقًا إلى حساب المتجر وفق دورة التحويل المحددة.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ّل لاحقاً إلى حسابك البنكي. - سجل العمليات: يظهر سجل مفصل للطلبات الإلكترونية، ويشمل:(رقم الطلب، المبلغ الأساسي للطلب، قيمة الرسوم، إجمالي الطلب بعد الخصم، الضريبة، طريقة الدفع، تاريخ الطلب، ملاحظات إضافية (إن وجدت)). ⚙️ إدارة رصيد المدفوعات الإلكترونية - استعراض سجل المدفوعات الإلكترونية من تبويب المدفوعات الإلكترونية, اضغط (عرض السجل) ستظهر كافة عمليات المدفوعات الإلكترونية, كما يمكنك تصدير العمليات بالضغط (تصدير) 💵 رصيد المدفوعات عند الاستلام ⟪يُخصص تبويب المدفوعات عند الاستلام لعرض جميع المستحقات الناتجة عن الطلبات التي تم دفعها عبر خدمة الدفع عند الاستلام، والتي يتم تحصيلها من خلال شركات الشحن، ويتم تحويلها لاحقًا إلى حساب المتجر وفق دورة التحويل المحددة.⟫ حيث يشمل البيانات التالية: - إجمالي رصيد مدفوعات عند الاستلام: مجموع مبالغ الطلبات التي تم تحصيلها عند الاستلام. - إجمالي رسوم الدفع عند الاستلام: الرسوم المخصومة مقابل خدمة التحصيل عبر شركة الشحن. - إجمالي رسوم الضريبة : قيمة الضريبة المطبقة على رسوم الدفع عند الاستلام. - إجمالي الرصيد بعد خصم الرسوم: صافي المبلغ المتوقع تحويله بعد خصم الرسوم والضريبة. - سجل العمليات: يشمل: رقم الطلب، المبلغ لكل طلب، شركة الشحن، رقم الشحنة أو التتبع، قيمة الضري…

### Q4-SA-P0093

**Cited at:** section 1, line 45; section 2, line 91; section 7, line 162

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-092
- bullet: c;end-payout
- placement: decides
- identifier: الأسئلة الشائعة
- statement: الأيام المحددة لتحويل رصيد الدفع عند الاستلام من الشركات التي تدعم الدفع عند الاستلام في بوليصات سلة إلى التاجر هي: يومي الأحد والأربعاء لجميع شركات الشحن ضمن بوليصات سلة.
- scope: بوليصات سلة
- cite_ids: S01-SA-C097
- from: index:SA-C-115:SA-S-0122

**Citation S01-SA-C097:** `https://help.salla.sa/article/تفعيل-وإدارة-الدفع-عند-الاستلام-مع-بوليصات-سلة/koda8pykc6pdhylg7zb2iu0g` | الأسئلة الشائعة (line 794 of the rendered text) | 2026-08-31 | kind: stated | quote check: found
- quote: الأيام المحددة لتحويل رصيد الدفع عند الاستلام من الشركات التي تدعم الدفع عند الاستلام في بوليصات سلة إلى التاجر هي: يومي الأحد والأربعاء لجميع شركات الشحن ضمن بوليصات سلة.
- title: تفعيل الدفع عند الاستلام وإدارته | مركز المساعدة - سلة
- the page opens: تفعيل الدفع عند الاستلام وإدارته مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل حل…
- in context: …الداعمة للدفع عند الاستلام من بوليصات سلة هي: 1- أرامكس 2- جي اند تي اكسبريس | J&T 3- أي مكان 4- سمسا 5- ريد بوكس 6- شيبا | shipa ❓ هل تقوم سلة بتحصيل مبالغ الدفع عند الاستلام عند استخدام شركة شحن خارج نطاق بوليصات سلة؟ لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة. تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين. ❓ما هي أيام تحويل رصيد الدفع عند الاستلام الناتج من بوليصات سلة للتاجر؟ ⟪الأيام المحددة لتحويل رصيد الدفع عند الاستلام من الشركات التي تدعم الدفع عند الاستلام في بوليصات سلة إلى التاجر هي: يومي الأحد والأربعاء لجميع شركات الشحن ضمن بوليصات سلة.⟫ تُصدر الفاتورة بمبالغ الطلبات التي استلمها العميل وتكون حالتها (تم التوصيل) أو (تم الشحن)، وتشمل الطلبات المنجزة خلال الأسبوع السابق. يرجى ملاحظة أن وصول المبلغ إلى حسابك البنكي قد يستغرق وقتاً إضافياً حسب سياسة البنك الذي تتعامل معه. ❓ هل ميزة الدفع عند الاستلام متاحة مهما كانت قيمة السلة؟ إذا كانت قيمة السلة أقل من 20 ريال فلن تظهر وسيلة الدفع عند الاستلام في صفحة إتمام الطلب حتى وإن كانت مفعلة. ❓كيف يستخدم العميل ميزة الدفع عند الاستلام؟ أولا…

### Q4-SA-P0042

**Cited at:** section 1, line 45; section 3, line 102; section 5, line 132; section 7, line 158

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-041
- bullet: a
- placement: boundary
- identifier: wallet.payout.flow.cod.step2
- statement: تحوِّل شركة الشحن المبلغ إلى سلة
- cite_ids: S01-SA-C041
- from: new
- note: Next in the same flow: wallet.payout.flow.bank 'تُحوَّل المستحقات إلى حسابك البنكي'.

**Citation S01-SA-C041:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/payments.json` | wallet.payout.flow.cod.step2 | 2026-10-08 | kind: observed | quote check: found
- quote: تحوِّل شركة الشحن المبلغ إلى سلة
- in context: …كتروني عند اكتماله. تصدير المستحقات الحالية إغلاق آخر فاتورة حالة آخر تحويل لمستحقاتك إلى حسابك البنكي. إجمالي ما ستستلمه ستظهر مدفوعاتك ومستحقاتك وحوالاتك البنكية هنا بعد أول طلب مدفوع عند الاستلام. تابع مدفوعاتك عند الاستلام ستظهر مدفوعاتك ومستحقاتك وحوالاتك البنكية هنا بعد أول طلب مدفوع إلكترونيًا. تابع مدفوعاتك الإلكترونية تُحوَّل المستحقات إلى حسابك البنكي تُحوَّل المستحقات إلى حسابك البنكي المنتهي ب {{last4}} يدفع العميل نقدًا عند الاستلام ⟪تحوِّل شركة الشحن المبلغ إلى سلة⟫ يدفع العميل إلكترونيًا يُضاف إلى رصيد المدفوعات المستحقات القادمة إجراءات المبلغ تاريخ العملية الوصف الحالة تفاصيل العملية رقم العملية النوع المحفظة ستتمكَّن من استعراض آخر العمليات عند توفرها. لا توجد عمليات بعد ابحث برقم العملية استعرض رصيد متجرك المستخدم للاشتراكات والخدمات والمشتريات من المنصة. نظرة عامة إجمالي المبالغ المضافة إلى رصيد المتجر منذ إنشائه. إجمالي المبالغ المخصومة من رصيد محفظة المتجر، وتشمل الاشتراكات والخدمات والمشتريات والمب…

### Q4-SA-004

**Cited at:** section 2, line 62

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-004
- bears_on: 1
- identifier: خطوات إضافة حساب بنكي جديد
- statement: 1- اسم البنك. 2- اسم صاحب الحساب. 3- رقم الحساب. 4- رقم الأيبان. 5- خيار إضافة المعرف البديل.
- cite_ids: Q4-SA-C005;Q4-SA-C006;Q4-SA-C007;Q4-SA-C008;Q4-SA-C009
- from: held

**Citation Q4-SA-C005:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 169 (article xwboef9bg8yax7dpsmuq0aq3, إعداد الحساب البنكي ونظام الحوالات السريع) | 2026-08-31 | kind: stated | quote check: found
- quote: 1- اسم البنك.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …أكثر أمانًا، لزيادة كفاءة عملك. 📌 المحاور الرئيسية للمقالة: - خطوات إضافة حساب بنكي جديد - تفعيل نظام الحوالات السريع - الأسئلة الشائعة 🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. خطوات إضافة حساب بنكي جديد: 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( طرق الدفع ). 2. من قسم التحويل البنكي، اضغط (+إضافة حساب بنكي). 3. اكتب البيانات المطلوبة، ثم اضغط (إضافة حساب بنكي). ⟪1- اسم البنك.⟫ 2- اسم صاحب الحساب. 3- رقم الحساب. 4- رقم الأيبان. 5- خيار إضافة المعرف البديل. 🚀 تفعيل نظام الحوالات السريع نظام الحوالات السريع: هو نظام سريع لتحويل المبالغ بين البنوك في فترة قصيرة باستخدام معرّفات مختلفة عن رقم الحساب أو الآيبان. عند تفعيل المعرف البديل المفضل لديك، سواء رقم الجوال أو رقم الهوية أو البريد الالكتروني. الأسئلة الشائعة ❓ كيف يظهر المعرف البديل في متجرك؟ من صفحة إكمال الدفع في متجرك، ستظهر معلومات التحويل السريع بشكل تلقائي. ❓ ه…

**Citation Q4-SA-C006:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 169 (article xwboef9bg8yax7dpsmuq0aq3, إعداد الحساب البنكي ونظام الحوالات السريع) | 2026-08-31 | kind: stated | quote check: found
- quote: 2- اسم صاحب الحساب.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …زيادة كفاءة عملك. 📌 المحاور الرئيسية للمقالة: - خطوات إضافة حساب بنكي جديد - تفعيل نظام الحوالات السريع - الأسئلة الشائعة 🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. خطوات إضافة حساب بنكي جديد: 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( طرق الدفع ). 2. من قسم التحويل البنكي، اضغط (+إضافة حساب بنكي). 3. اكتب البيانات المطلوبة، ثم اضغط (إضافة حساب بنكي). 1- اسم البنك. ⟪2- اسم صاحب الحساب.⟫ 3- رقم الحساب. 4- رقم الأيبان. 5- خيار إضافة المعرف البديل. 🚀 تفعيل نظام الحوالات السريع نظام الحوالات السريع: هو نظام سريع لتحويل المبالغ بين البنوك في فترة قصيرة باستخدام معرّفات مختلفة عن رقم الحساب أو الآيبان. عند تفعيل المعرف البديل المفضل لديك، سواء رقم الجوال أو رقم الهوية أو البريد الالكتروني. الأسئلة الشائعة ❓ كيف يظهر المعرف البديل في متجرك؟ من صفحة إكمال الدفع في متجرك، ستظهر معلومات التحويل السريع بشكل تلقائي. ❓ هل يمكنني تعطيل المعر…

**Citation Q4-SA-C007:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 169 (article xwboef9bg8yax7dpsmuq0aq3, إعداد الحساب البنكي ونظام الحوالات السريع) | 2026-08-31 | kind: stated | quote check: found
- quote: 3- رقم الحساب.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …المحاور الرئيسية للمقالة: - خطوات إضافة حساب بنكي جديد - تفعيل نظام الحوالات السريع - الأسئلة الشائعة 🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. خطوات إضافة حساب بنكي جديد: 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( طرق الدفع ). 2. من قسم التحويل البنكي، اضغط (+إضافة حساب بنكي). 3. اكتب البيانات المطلوبة، ثم اضغط (إضافة حساب بنكي). 1- اسم البنك. 2- اسم صاحب الحساب. ⟪3- رقم الحساب.⟫ 4- رقم الأيبان. 5- خيار إضافة المعرف البديل. 🚀 تفعيل نظام الحوالات السريع نظام الحوالات السريع: هو نظام سريع لتحويل المبالغ بين البنوك في فترة قصيرة باستخدام معرّفات مختلفة عن رقم الحساب أو الآيبان. عند تفعيل المعرف البديل المفضل لديك، سواء رقم الجوال أو رقم الهوية أو البريد الالكتروني. الأسئلة الشائعة ❓ كيف يظهر المعرف البديل في متجرك؟ من صفحة إكمال الدفع في متجرك، ستظهر معلومات التحويل السريع بشكل تلقائي. ❓ هل يمكنني تعطيل المعرف البديل؟ نعم .…

**Citation Q4-SA-C008:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 169 (article xwboef9bg8yax7dpsmuq0aq3, إعداد الحساب البنكي ونظام الحوالات السريع) | 2026-08-31 | kind: stated | quote check: found
- quote: 4- رقم الأيبان.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ة للمقالة: - خطوات إضافة حساب بنكي جديد - تفعيل نظام الحوالات السريع - الأسئلة الشائعة 🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. خطوات إضافة حساب بنكي جديد: 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( طرق الدفع ). 2. من قسم التحويل البنكي، اضغط (+إضافة حساب بنكي). 3. اكتب البيانات المطلوبة، ثم اضغط (إضافة حساب بنكي). 1- اسم البنك. 2- اسم صاحب الحساب. 3- رقم الحساب. ⟪4- رقم الأيبان.⟫ 5- خيار إضافة المعرف البديل. 🚀 تفعيل نظام الحوالات السريع نظام الحوالات السريع: هو نظام سريع لتحويل المبالغ بين البنوك في فترة قصيرة باستخدام معرّفات مختلفة عن رقم الحساب أو الآيبان. عند تفعيل المعرف البديل المفضل لديك، سواء رقم الجوال أو رقم الهوية أو البريد الالكتروني. الأسئلة الشائعة ❓ كيف يظهر المعرف البديل في متجرك؟ من صفحة إكمال الدفع في متجرك، ستظهر معلومات التحويل السريع بشكل تلقائي. ❓ هل يمكنني تعطيل المعرف البديل؟ نعم . اضغط خيار إضافة…

**Citation Q4-SA-C009:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 169 (article xwboef9bg8yax7dpsmuq0aq3, إعداد الحساب البنكي ونظام الحوالات السريع) | 2026-08-31 | kind: stated | quote check: found
- quote: 5- خيار إضافة المعرف البديل.
- title, opening and note boxes: as for this source's citation above
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …ات إضافة حساب بنكي جديد - تفعيل نظام الحوالات السريع - الأسئلة الشائعة 🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط. خطوات إضافة حساب بنكي جديد: 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( طرق الدفع ). 2. من قسم التحويل البنكي، اضغط (+إضافة حساب بنكي). 3. اكتب البيانات المطلوبة، ثم اضغط (إضافة حساب بنكي). 1- اسم البنك. 2- اسم صاحب الحساب. 3- رقم الحساب. 4- رقم الأيبان. ⟪5- خيار إضافة المعرف البديل.⟫ 🚀 تفعيل نظام الحوالات السريع نظام الحوالات السريع: هو نظام سريع لتحويل المبالغ بين البنوك في فترة قصيرة باستخدام معرّفات مختلفة عن رقم الحساب أو الآيبان. عند تفعيل المعرف البديل المفضل لديك، سواء رقم الجوال أو رقم الهوية أو البريد الالكتروني. الأسئلة الشائعة ❓ كيف يظهر المعرف البديل في متجرك؟ من صفحة إكمال الدفع في متجرك، ستظهر معلومات التحويل السريع بشكل تلقائي. ❓ هل يمكنني تعطيل المعرف البديل؟ نعم . اضغط خيار إضافة المعرف لتعطيله. ❓ هل يمكنني …

### Q4-SA-005

**Cited at:** section 2, line 62; section 5, line 134

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-005
- bears_on: 4
- identifier: 🔔 تنويه هام
- statement: 🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.
- scope: المملكة العربية السعودية
- cite_ids: Q4-SA-C010
- from: held

**Citation Q4-SA-C010:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 169 (article xwboef9bg8yax7dpsmuq0aq3, إعداد الحساب البنكي ونظام الحوالات السريع) | 2026-08-31 | kind: stated | quote check: found
- quote: 🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: …D8%B8%D8%A7%D9%85-%D8%A7%D9%84%D8%AD%D9%88%D8%A7%D9%84%D8%A7%D8%AA-%D8%A7%D9%84%D8%B3%D8%B1%D9%8A%D8%B9/xwboef9bg8yax7dpsmuq0aq3 هل تبحث عن طريقة سهلة لإضافة حساب بنكي إلى متجرك أو تفعيل نظام الحوالات السريعة؟ هذا الدليل يقدم لك خطوات بسيطة وسريعة لربط حسابك البنكي مع النظام، مما يتيح لك تحويل الأموال بشكل أسرع وأكثر أمانًا، لزيادة كفاءة عملك. 📌 المحاور الرئيسية للمقالة: - خطوات إضافة حساب بنكي جديد - تفعيل نظام الحوالات السريع - الأسئلة الشائعة ⟪🔔 تنويه هام: ميزة نظام الحوالات السريع مخصصة حالياً للمتاجر في المملكة العربية السعودية فقط.⟫ خطوات إضافة حساب بنكي جديد: 1. من القائمة الرئيسية، من قائمة (الكل)، من قسم الإعدادات والأدوات، اضغط ( طرق الدفع ). 2. من قسم التحويل البنكي، اضغط (+إضافة حساب بنكي). 3. اكتب البيانات المطلوبة، ثم اضغط (إضافة حساب بنكي). 1- اسم البنك. 2- اسم صاحب الحساب. 3- رقم الحساب. 4- رقم الأيبان. 5- خيار إضافة المعرف البديل. 🚀 تفعيل نظام الحوالات السريع نظام الحوالات السريع: هو نظام سريع لتحويل المبالغ بين البنوك في فترة قصيرة باستخدام معرّفات مختلفة عن رقم…

### Q4-SA-P0100

**Cited at:** section 2, line 63

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-099
- bullet: a;end-payment
- placement: where
- identifier: الأسئلة الشائعة
- statement: الحساب البنكي ضمن طرق الدفع: تستخدمه لاستقبال المدفوعات من عملائك عبر التحويل البنكي، ويظهر لهم أثناء إتمام الطلب.
- cite_ids: S01-SA-C110
- from: index:SA-C-117:SA-S-0095

**Citation S01-SA-C110:** `https://help.salla.sa/article/-إعداد-الحساب-البنكي/bhrrwm3oexjhzqjibwnic7dg` | الأسئلة الشائعة (line 771 of the rendered text) | 2026-10-05 | kind: stated | quote check: found
- quote: الحساب البنكي ضمن طرق الدفع: تستخدمه لاستقبال المدفوعات من عملائك عبر التحويل البنكي، ويظهر لهم أثناء إتمام الطلب.
- title: إضافة الحساب البنكي وسحب رصيد متجرك | مركز المساعدة - سلة
- the page opens: إضافة الحساب البنكي وسحب رصيد متجرك مركز المساعدة - سلة Enأنشئ متجرك مجاناَ الرئيسية التعليم مركز المساعدة مكتبة متكاملة لكل ما تحتاجه لبدء تجارتك مع سلة مجتمع سلة تبادل الخبرات والتجارب واستلهم طرقًا مميزة للنجاح مدونة سلة وسع دائرة معارفك بالعديد من الموضوعات المثيرة منصة المطورين انضم إلى مجتمع مطوري سلة أكاديمية سلة دورات احترافية تساعدك على نجاحك التجاري أدوات التجار أدوات متكاملة لدعم نمو متجرك الحلول متجر التطبيقات أدوات عديدة لنجاح متجرك صانع التطبيقات اصنع تطبيقًا خاصًا لمتجرك سلة سبيشل…
- in context: … تقديم طلب الاسترداد. الأسئلة الشائعة ❓ ما هي آلية سحب الرصيد في سلة؟ يتم تحويل الرصيد إلى الحساب البنكي بشكل دوري، وذلك بشرط: ✅ صحة واكتمال بيانات التوثيق. ✅ عدم وجود أي أخطاء في بيانات الحساب البنكي. ✅ عدم وجود شكاوى مفتوحة على المتجر. ❓هل الحساب البنكي لاستلام مستحقاتي من سلة هو نفسه الحساب البنكي الذي يظهر لعملائي؟ لا. لكل حساب استخدام مختلف: الحساب البنكي المرتبط بتوثيق المتجر: تستخدمه سلة لتحويل مستحقاتك إلى حسابك البنكي، ولا يظهر لعملائك. ⟪الحساب البنكي ضمن طرق الدفع: تستخدمه لاستقبال المدفوعات من عملائك عبر التحويل البنكي، ويظهر لهم أثناء إتمام الطلب.⟫ ❓لماذا لم يتم تحويل الرصيد إلى حسابي البنكي؟ تحقق أولًا من: - تطابق اسم صاحب الحساب مع بيانات التوثيق. - صحة بيانات الحساب البنكي. - عدم وجود أخطاء في كتابة الاسم. - عدم وجود شكوى مفتوحة على المتجر. إذا كانت البيانات صحيحة، راجع حالة طلب الاسترداد. ❓هل يمكن استخدام الحساب البنكي في اكثر من متجر في سلة؟ نعم، يمكن استخدام نفس الحساب البنكي والهوية الوطنية لإنشاء أكثر من متجر على سلة. ❓كيف يمكنني حذف حساب بنكي الخاص باستقبال المدفوعات من العملاء؟ م…

### Q4-SA-066

**Cited at:** section 2, line 79; section 3, line 112

**Record** (`studies/proposals/records/Q4/salla/statements.tsv`):
- stmt_id: Q4-SA-066
- bears_on: 4
- identifier: SettingsPage.cash-on-delivery-first-alert-description
- statement: يجب إتاحة خيار الدفع عند الاستلام من إعدادات شركة الشحن.
- cite_ids: Q4-SA-C098
- from: held

**Citation Q4-SA-C098:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/dashboard-translations/ar/shipping.json` | key "SettingsPage.cash-on-delivery-first-alert-description" | 2026-10-12 | kind: observed | quote check: found
- quote: يجب إتاحة خيار الدفع عند الاستلام من إعدادات شركة الشحن.
- in context: …قيد اختر نوع القيد اختر شرطًا واحدًا على الأقل للمتابعة. اختر الفروع والمستودعات اختر مجموعة العملاء اختر المنتجات اختر التصنيفات حالة شركة الشحن نوع قيد الشحن قيمة السلة ظاهرة الطلب من مناطق محددة إذا كان عنوان العميل (الدولة والمدينة) يقع داخل نطاق المناطق المسموحة أو المستثناة. اختر دولة أو مدينة واحدة لاستخدام هذا الشرط. بداية الوقت يبدأ من إعدادات متقدمة الدفع عند الاستلام حدِّد شروط الدفع عند الاستلام واختر المنتجات أو التصنيفات المستثناة. ⟪يجب إتاحة خيار الدفع عند الاستلام من إعدادات شركة الشحن.⟫ حدِّد الشروط التي تُعطِّل ظهور خيار الدفع عند الاستلام في صفحة إتمام الطلب. تصنيفات مستثناة من الدفع عند الاستلام اختر التصنيفات المستثناة شروط الدفع عند الاستلام تأكيد استلام الطلب أرسل رسالة تأكيد للعميل عند استلام الطلب المدفوع عند الاستلام. الشحن المجاني فعِّل الشحن المجاني بالشروط التي تناسب متجرك. إعدادات متقدمة الحد الأقصى لوزن المنتجات في السلة الحد الأقصى للطلب إذا كانت شركة الشحن ضمن بوليصات سلة، فسيُطبَّق حد أقصى قدره يجب أن يكون الحد…

### Q4-SA-P0202

**Cited at:** section 3, line 112

**Record** (`studies/proposals/records/Q4/salla/copied-pilot.tsv`):
- stmt_id: S01-SA-201
- bullet: c
- placement: decides
- identifier: الدفع عند الاستلام (كيف تشحن منتجاتك بأقل الأسعار وبأقصر وقت)
- statement: كما تختلف طرق تسوية مبالغ الدفع عند الإستلام بحسب سياسة شركة الشحن.
- cite_ids: S01-SA-C320;S01-SA-C321
- from: new
- note: Phase A2 (S01-VP-06). Found while searching for waybill and behalf (the English article says Salla waybill rates are 'negotiated on behalf of Salla merchants'). Salla's English (second citation): 'Cash on delivery is one of the payment methods customers ask for most, and how those amounts are settled back to you depends on each shipping company's policy.'

**Citation S01-SA-C320:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/ar/texts.jsonl` | line 1312 (article gycje7y8x0jv84d6arbwyrwf, كيف تشحن منتجاتك بأقل الأسعار وبأقصر وقت), paragraph 31 | 2026-08-22 | kind: stated | quote check: found
- quote: كما تختلف طرق تسوية مبالغ الدفع عند الإستلام بحسب سياسة شركة الشحن.
- headings: اسم البرومبت الوصف الرابط الكامل
- in context: … كانت غير مضافة. لمزيد من التفاصيل حول: طباعة بوليصات الشحن المحفظة والفواتير بوليصات الشحن خطوة بخطوة ولطريقة تغيير خصم رسوم البوليصة إعداد خيارات الطلبات الرسوم الإضافية للشحن الدولي بعد احتساب الرسوم الجمركية والرسوم الإضافية للشحن الدولي بما يخص البوليصات سيتم تسويتها مباشرة من خلال رصيد المحفظة. لمزيد من التفاصيل حول إدارة بوليصات الشحن الدفع عند الاستلام ميزة الدفع عند الإستلام تعتبر من أهم طرق الدفع في أي متجر إلكتروني لأسباب تفضيلية عدة، ⟪كما تختلف طرق تسوية مبالغ الدفع عند الإستلام بحسب سياسة شركة الشحن.⟫ بامكانك تفعيل ميزة الدفع عند الاستلام في متجرك في سلة 1. من صفحة خيارات الشحن والتوصيل، اضغط (الدفع عند الاستلام). 2. أدخل الشروط التي عند تحقيقها يتم تعطيل خيار الدفع عند الاستلام، ثم اضغط (حفظ). 1- أدخل الحد الأعلى لقيمة سلة مشتريات العميل الذي إن تجاوزته سلة المشتريات سيتم تعطيل ميزة الدفع عند الاستلام. 2- أدخل الحد الأعلى لوزن المنتجات الذي إن تجاوزته سلة المشتريات سيتم تعطيل ميزة الدفع عند الاستلام. 3. حدد المنتجات والتصنيفات المستثناة من ا…

**Citation S01-SA-C321:** `observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3:structures/salla/help-articles/en/texts.jsonl` | line 1087 (article gycje7y8x0jv84d6arbwyrwf, How to ship your products faster and for less on Salla), paragraph 33 | 2026-08-29 | kind: stated | quote check: found
- quote: how those amounts are settled back to you depends on each shipping company's policy.
- in context: …ptions . For more details, see the wallet and invoices . For more details, see shipping waybills step by step . 🌍 Extra fees for international shipping Customs duties and the extra fees that apply to international shipping are calculated on the waybill and then settled directly from your wallet balance. For more details, see managing shipping waybills . 💳 Cash on delivery Cash on delivery is one of the payment methods customers ask for most, and ⟪how those amounts are settled back to you depends on each shipping company's policy.⟫ You control when the option is offered from your store settings. 1. From the side menu of your dashboard, click (Store settings). 2. On the store settings page, click (Shipping and delivery options). 3. On the shipping and delivery page, click (Cash on delivery). 4. Enter the conditions that will disable cash on delivery when they are met, then click (Save). 1. Enter the minimum cart value . If the customer's cart falls outside it, cash on deliv…
