# New statements for the Salla re-pass (11 October 2026), one call per statement.
# W: a web page (working copy in fetched/, or a first-run capture), by line number; part = an exact excerpt of that line.
# T: a held dashboard translation value (observed-sa structures/salla/dashboard-translations/<lang>/<ns>.json).
# J: a held JSONL or text file in observed-sa, by line number; field = a JSON path to a string; part = an exact excerpt.
# E: an existing first-run citation; st must be an exact excerpt of its source.
# loc: the heading the line sits under (help articles), used in the locator.
NEW = []
def W(c, p, url, line, part=None, loc="", ident=None, scope="", note=""):
    NEW.append(dict(kind="W", c=c, p=p, url=url, line=line, part=part, loc=loc, ident=ident, scope=scope, note=note))
def T(c, p, ns, key, part=None, scope="", note="", lang="ar"):
    NEW.append(dict(kind="T", c=c, p=p, ns=ns, key=key, part=part, lang=lang, scope=scope, note=note, ident=key))
def J(c, p, path, line, field=None, part=None, ident=None, loc=None, scope="", note=""):
    NEW.append(dict(kind="J", c=c, p=p, path=path, line=line, field=field, part=part, ident=ident, loc=loc, scope=scope, note=note))
def E(c, p, cite, st, ident, scope="", note=""):
    NEW.append(dict(kind="E", c=c, p=p, cite=cite, st=st, ident=ident, scope=scope, note=note))

H = "https://help.salla.sa/article/"
APPPOL = H + "سياسة-نشر-التطبيق-في-متجر-التطبيقات-1/l6e8bqm8vm89arp4krr40cdm"
APPMAKER = H + "خطوات-الاشتراك-بخدمة-صانع-التطبيقات-من-سلة/dl3kk70gmzq9n9xj1yi8ydls"
POINTCARD = H + "تفعيل-الدفع-بالبطاقة-في-سلة-بوينت/hy4mv5r6yqoyjifiy7659nzk"
MAHALLYFAQ = H + "الأسئلة-الشائعة-حول-منصة-محلي-1/i6552boeb92lhuug905exq0i"
QUALITY = H + "بوابة-الجودة-لشكاوى-الشحن/lzsretdcadjc3r70lsxygiu9"
PACKING = H + "طلب-مواد-التغليف-من-شركات-شحن-بوليصات-سلة/eyeqtkxf1stsm77vzgjil56h"
INTLREADY = H + "جاهزية-الشحن-الدولي/vidfaxjgo1wz8xjimrwfgswi"
INTLID = H + "تفاصيل-العنوان-والهوية-في-صفحة-الدفع-لطلبات-الشحن-الدولي/xv4salemauzwaoov97ccuvwf"
PLANMGMT = H + "إدارة-باقة-المتجر-الاشتراكات-الفواتير-والترقية/gbc2ct0nerndys7sk4l2rvc1"
PAYRESTR = H + "إعدادات-قيود-الدفع/d9me3k8vqi09hdiun8r2ngfr"
COMPLAINTS = H + "-إدارة-شكاوى-العملاء/q1ffpxzoyyg7ub0zn7owtnkn"
REFERRAL = H + "برنامج-الإحالة-التسويق-بالعمولة-لباقات-سلة/ho98sug89tipkyg6cc9jmqrx"
FRAUDTIPS = H + "نصائح-لحماية-متجرك-من-الاحتيال/xiu0yycxeuii6wrdn0hfyowh"
PRIVCONSENT = H + "موافقة-العميل-على-سياسة-خصوصية-المتجر/loqvq0l5sn8jthz02aw49gl7"
PRIVPDPL = H + "توافق-سياسة-الخصوصية-لمتجرك-مع-نظام-حماية-البيانات-الشخصي/g4ycbbfqagvghtjz6ap1t0lb"
AWB = H + "كيف-تستفيد-من-بوليصات-الشحن-في-سلة/y2pqllcsineilgx6h7ofivut"
SPECIALMGR = H + "التواصل-مع-مسؤول-مدير-حساب-باقة-سبيشال/vddgoqvlxygdhaq2gx5bwl3q"
MOYASAR = H + "ربط-الجمعيات-الخيرية-مع-بوابة-الدفع-ميسر/zm2rkn8lfc8gjd6drybo2tvh"
P = "https://partners.salla.com/legal/"
SLA = P + "اتفاقية-الوكالات-لتقديم-خدمات-لتجار-سلة"
MIGR = P + "شروط-وأحكام-خدمة-انتقال-المتاجر-من-منصات-أخرى-إلى-منصة-سلة"
NDPKG = P + "nd-packages"
SERVPROV = P + "service-provider"
INFLU = P + "influencer"
JOIN = P + "privacy"
GLOBAL = "https://partners.salla.com/global-selling-program"
D = "https://docs.salla.dev/"
PHC = "structures/salla/portal-help-center-article/partner@en/items.jsonl"

# ---------------- account, plan, billing, domain ----------------
W("SA-C-004", "responsible", NDPKG, 22, loc="أولًا : التعريفات", ident="\"سلة\" (التعريفات)",
  scope="الشروط والأحكام لحملة اليوم الوطني (95) – باقات/بكجات سلة",
  note="The definition names the company behind the campaign's plan packages.")
W("SA-C-004", "boundary", PLANMGMT, 772, loc="الأسئلة الشائعة: طريقة استرجاع المبلغ", ident="💰 طريقة استرجاع المبلغ",
  note="Refunds of the plan go to the store balance (wallet).")
W("SA-C-004", "reason", H + "باقات-المتجر-اختر-الباقة-المثالية-لتجارتك/glmfvz0wf6rvd9wiczinecb1", 942,
  loc="الأسئلة الشائعة", ident="❓ لماذا لا يظهر خيار إلغاء الباقة؟",
  note="Answer to 'لماذا لا يظهر خيار إلغاء الباقة؟'.")
T("SA-C-007", "responsible", "domain", "move_domain.accept_responsibility",
  note="Text the merchant confirms when asking to transfer a domain.")
T("SA-C-012", "boundary", "settings", "general/salla-mcp/chatgpt#step3.description",
  note="Step of the Salla AI Connector set-up for ChatGPT.")
W("SA-C-014", "where", SPECIALMGR, 654, loc="كيفية الوصول إلى بيانات مسؤول الحساب", ident="مسؤول الحساب",
  scope="باقة سبيشل", note="The account manager of the Special plan, reached from the dashboard's side menu.")
J("SA-C-014", "where", "help.salla.sa/llms.txt", 1, ident="help.salla.sa", loc="line 1",
  note="Salla's help centre, a separate host.")
W("SA-C-013", "responsible", SERVPROV, 29, loc="سياسة تقديم الخدمات في منصة الشركاء", ident="سياسة تقديم الخدمات في منصة الشركاء",
  scope="الشركاء مقدمو الخدمات في منصة الشركاء")

# ---------------- catalogue, orders, customers ----------------
W("SA-C-008", "reason", H + "الأسئلة-الشائعة-حول-اللغات/f5uqqoq0jzr0skh2qxz797ms", 689, loc="الأسئلة الشائعة",
  ident="❓ عند إضافة لغة إلى متجري لماذا تظهر معطلة؟", note="Answer to 'عند إضافة لغة إلى متجري لماذا تظهر معطلة؟'.")
W("SA-C-010", "reason", H + "إدارة-سجل-العمليات-لتجار-باقة-سبيشل/z61qef5grewvqpqvgmrek20z", 647, loc="ما هي صفحة سجل العمليات؟",
  ident="سجل العمليات", scope="تجار باقة سبيشل")
W("SA-C-025", "reason", H + "إدارة-وجرد-المخزون/xzpw5e46wflnxg611caz0aem", 756, loc="ملاحظة", ident="سبب الإنقاص",
  note="The reason given for making a reason mandatory when a quantity is reduced.")
W("SA-C-031", "reason", H + "إضافة-منتج-الحجوزات/gea2uoqanu6oku9a9seoqbfk", 938, loc="الأسئلة الشائعة",
  ident="❓ هل يمكنني الجمع بين منتج عادي و منتج حجز؟", note="Answer to 'هل يمكنني الجمع بين منتج عادي و منتج حجز؟'.")
W("SA-C-032", "reason", H + "اعلمني-عند-التوفر/irngv7s52c5mrdn6xaq1sjtw", 772, loc="❓لماذا تحتاج هذه الميزة؟",
  ident="اعلمني عند التوفر", note="One of the answers to 'لماذا تحتاج هذه الميزة؟'.")
E("SA-C-032", "boundary", "SA-S-1666", "Triggered when a product is back in stock and the customer is notified.",
  "product.availability.alert", note="Communication-app event (Communication Webhooks).")
E("SA-C-032", "boundary", "SA-S-1498", "product id that can visitor subscribe to its availability notification",
  "salla-product-availability", note="Twilight web component; description of its productId property.")
W("SA-C-033", "reason", H + "تحسين-ظهور-متجرك-على-محركات-البحث-seo/oi134aj2ud6ts12ysumrm5za", 719, loc="التعبئة التلقائية لخانات SEO",
  ident="التعبئة التلقائية لخانات SEO")
W("SA-C-044", "reason", H + "إعداد-إصدار-فواتير-الطلبات/iz5t4pco8lhfu41usey0u53z", 647, loc="الهدف من إعداد إصدار فواتير الطلبات:",
  ident="الهدف من إعداد إصدار فواتير الطلبات")
W("SA-C-047", "reason", H + "إعداد-الإقرار-قبل-ارسال-الطلب-استراتيجية-فعالة-لتقليص-المرتجعات/d30d94hdxftazdc9bzsyaq3t", 802,
  loc="الأسئلة الشائعة", ident="الإقرار قبل الشراء",
  note="Answer to 'كيف يمكن أن يساعد الإقرار قبل الشراء في تقليل الطلبات غير الجادة؟'.")
W("SA-C-048", "reason", H + "أسئلة-شائعة-حول-السلات-المتروكة/t54wwgpe01v4li9czmapvf68", 1118, loc="الأسئلة الشائعة",
  ident="❓ لماذا لا يمكنني إرسال رسائل الخصم في أي وقت؟", note="Answer to 'لماذا لا يمكنني إرسال رسائل الخصم في أي وقت؟'.")
W("SA-C-062", "reason", H + "تسجيل-الدخول-السريع-للمتجر-باستخدام-ال-passkey/u7o5nn9xqsl4y2urj30n034d", 750, loc="الأسئلة الشائعة",
  ident="Passkey")
W("SA-C-063", "reason", H + "إدارة-التاجر-لمحفظة-العميل-وعروض-الكاش-باك/i31g2awy4qa2ifu6bp352zoy", 883, loc="الأسئلة الشائعة",
  ident="استعادة قيمة الكاش باك", note="The reason given for taking cashback back when an order is cancelled.")
T("SA-C-065", "responsible", "customers", "settings.address.form.is_saudi_national_address_required_warning",
  scope="is_saudi_national_address_required", note="Warning shown when the merchant turns the setting off.")
T("SA-C-065", "reason", "customers", "settings.address.form.is_saudi_national_address_required_description",
  scope="العملاء في السعودية")
W("SA-C-066", "where", PRIVPDPL, 684, loc="الأسئلة الشائعة", ident="كيف يمكنني إدراج صفحة الخصوصية في متجري؟",
  note="Answer to 'كيف يمكنني إدراج صفحة الخصوصية في متجري؟'.")
W("SA-C-066", "boundary", PRIVCONSENT, 665, loc="🚀عرض سياسة الخصوصية أثناء تسجيل العميل", ident="عرض سياسة الخصوصية أثناء تسجيل العميل")
W("SA-C-066", "reason", PRIVCONSENT, 667, loc="🚀عرض سياسة الخصوصية أثناء تسجيل العميل", ident="عرض سياسة الخصوصية أثناء تسجيل العميل")

# ---------------- marketing ----------------
E("SA-C-075", "boundary", "SA-S-1673", "Triggered when a marketing campaign is broadcast to customers.",
  "marketing.campaign.broadcast", note="Communication-app event (Communication Webhooks).")
W("SA-C-076", "responsible", INFLU, 22, loc="سياسة تقديم الإعلانات في منصة الشركاء", ident="سياسة تقديم الإعلانات في منصة الشركاء",
  scope="الشركاء الذين يقدمون الإعلانات في منصة الشركاء")
E("SA-C-077", "boundary", "SA-S-1663", "Triggered when a customer places a gift order.", "order.gift.placed",
  note="Communication-app event (Communication Webhooks).")
E("SA-C-077", "boundary", "SA-S-1448", "The product id for which the gifting system is required.", "salla-gifting",
  note="Twilight web component; description of its productId property.")
E("SA-C-078", "boundary", "SA-S-1672", "Triggered when a repurchase reminder is sent to the customer for a previously purchased product.",
  "customer.repurchase.reminder", note="Communication-app event (Communication Webhooks).")
W("SA-C-078", "reason", H + "إدارة-التذكير-بإعادة-الشراء/rw8w5jopmx1d4mfa03a2t5gf", 858, loc="الأسئلة الشائعة",
  ident="❓ هل منتج الحجوزات مشمول في ميزة تذكير إعادة الشراء؟",
  note="Answer to 'هل منتج الحجوزات مشمول في ميزة تذكير إعادة الشراء؟'.")
E("SA-C-079", "boundary", "SA-S-1507", '"tag": "salla-quick-buy"', "salla-quick-buy",
  note="Twilight web component; its properties include applePayOnly ('Show Apple Pay only').")
W("SA-C-079", "reason", H + "تفعيل-الشراء-السريع/jpuire3zxn5ayv0mg6zum636", 737, loc="الأسئلة الشائعة", ident="الشراء السريع والإقرار",
  note="Why the order acknowledgement does not show in quick purchase.")
W("SA-C-080", "boundary", H + "عروض-وخصومات-البنك/r50cyw73aywqx15wbsrb6bkk", 671,
  part="هو نوع خصم جديد يُطبق عندما يدفع العميل قيمة الطلب من خلال بطاقة بنك محدد", loc="ما هي عروض البنك؟", ident="عروض وخصومات البنك")
W("SA-C-080", "reason", H + "عروض-وخصومات-البنك/r50cyw73aywqx15wbsrb6bkk", 671,
  part="بهدف تشجيع العملاء للدفع عبر بنك تُفضله", loc="ما هي عروض البنك؟", ident="عروض وخصومات البنك")
W("SA-C-082", "boundary", H + "صفحات-الهبوط-بوابتك-لتحويل-النقرات-إلى-مبيعات/gn0ej4ydhbabd1m9qwnv9pvv", 882, loc="الأسئلة الشائعة",
  ident="البكسل في صفحات الهبوط", note="Answer to whether the pixel tracks events on landing pages.")

# ---------------- design, channels ----------------
W("SA-C-090", "reason", H + "-متجر-الثيمات/r82be2jrf9wgyxahtnz9ug0d", 669, loc="متجر الثيمات", ident="متجر الثيمات")
W("SA-C-091", "decides", D + "component-bundle/publish-requirements.md", 58, loc="## Technical Review > Security",
  ident="Bundle Publish Requirements: Security", scope="component bundles published in Salla Themes Marketplace")
W("SA-C-091", "reason", D + "component-bundle/publish-requirements.md", 3, loc="# Bundle Publish Requirements",
  ident="Bundle Publish Requirements")
W("SA-C-093", "reason", H + "إدارة-الصفحات-التعريفية/kdcldn0jro4n50amy4zwusga", 816, loc="الأسئلة الشائعة",
  ident="❓ ما الهدف من تحديد صفحة تعريفية كصفحة سياسة الاستبدال والاسترجاع؟",
  note="Answer to 'ما الهدف من تحديد صفحة تعريفية كصفحة سياسة الاستبدال والاسترجاع؟'.")
W("SA-C-094", "responsible", APPMAKER, 810, part="إذا كان تطبيقك لا يزال على حسابات سلة على متاجر التطبيقات، يجب نقل التطبيق الى حساباتك الخاصة على أبل ستور وقوقل بلاي لتتمكن من تجديد الاشتراك.",
  loc="الأسئلة الشائعة", ident="❓ هل يتأثر تجديد اشتراكي بصانع التطبيقات بوجود تطبيقي على حساب سلة ؟")
W("SA-C-094", "reason", APPMAKER, 810, part="هذا النقل ضروري لتنفيذ أي صيانة أو تحديثات للتطبيقات وفقًا لسياسات حقوق الملكية لشركات أبل وقوقل.",
  loc="الأسئلة الشائعة", ident="❓ هل يتأثر تجديد اشتراكي بصانع التطبيقات بوجود تطبيقي على حساب سلة ؟")
W("SA-C-094", "boundary", APPMAKER, 685, loc="نوع الاشتراك الأول: لدي حسابات مطور مسبقاً على آبل وجوجل", ident="لدي حسابات مطور مسبقاً على آبل وجوجل")
W("SA-C-095", "responsible", POINTCARD, 699, loc="🔔 ملاحظة: سعر نقاط البيع softpos من جيديا", ident="softpos من جيديا",
  scope="الدفع بالبطاقة في كاشير سلة بوينت (SoftPOS)")
W("SA-C-095", "responsible", POINTCARD, 820, loc="الأسئلة الشائعة", ident="❓ماذا يحدث في حال فشل الدفع؟",
  scope="الدفع بالبطاقة في كاشير سلة بوينت (SoftPOS)", note="Answer to 'ماذا يحدث في حال فشل الدفع؟'.")
W("SA-C-095", "boundary", POINTCARD, 679, loc="أولاً- الربط بحساب جيديا", ident="الربط بحساب جيديا")
W("SA-C-095", "reason", POINTCARD, 796, loc="الأسئلة الشائعة", ident="❓لماذا يتم ربط الرقم الخاص بجهاز الدفع(Terminal ID) بموظف محدد؟",
  note="Answer to 'لماذا يتم ربط الرقم الخاص بجهاز الدفع(Terminal ID) بموظف محدد؟'.")
W("SA-C-095", "reason", POINTCARD, 808, loc="الأسئلة الشائعة", ident="❓لماذا لا يمكن استخدام نفس الجهاز على أكثر من جوال؟",
  note="Answer to 'لماذا لا يمكن استخدام نفس الجهاز على أكثر من جوال؟'.")
W("SA-C-096", "responsible", MAHALLYFAQ, 657, loc="❓ما هي شروط عرض منتجاتي على لمحلي؟", ident="شروط الخصوصية والاستخدام لمنصة محلي",
  note="Names the terms the merchant accepts to list on Mahally; the terms' parties are not stated.")
W("SA-C-096", "boundary", MAHALLYFAQ, 759, loc="❓هل تختلف طريقة استقبال الطلبات من محلي عنها في متجري؟", ident="استقبال الطلبات من محلي")
W("SA-C-096", "reason", MAHALLYFAQ, 662, loc="❓ لماذا لا تظهر بعض منتجاتي في منصة محلي؟", ident="❓ لماذا لا تظهر بعض منتجاتي في منصة محلي؟")
W("SA-C-097", "reason", H + "إدارة-المنتجات/oc3r8o7ofidik6zykxwznrxu", 734, loc="الأسئلة الشائعة",
  ident="❓ لماذا تظهر بعض قنوات البيع معطّلة في عمود القنوات؟", note="Answer to 'لماذا تظهر بعض قنوات البيع معطّلة في عمود القنوات؟'.")
T("SA-C-098", "boundary", "reminders", "edu.shipping_rule.message", note="Dashboard reminder text about the wholesale market.")

# ---------------- payments ----------------
T("SA-C-119", "responsible", "payments", "gateway_settings.apply_policy_desc",
  note="Text the merchant agrees to when applying, through the dashboard, for an account with a payment company ({{name}}); the same gateway_settings namespace names باي بال and مكافأة الراجحي among its gateways.")
W("SA-C-121", "boundary", PAYRESTR, 779, loc="الأسئلة الشائعة", ident="❓ أين يمكنني مراجعة العمليات المرفوضة أو التي هي قيد المراجعة؟")
W("SA-C-121", "reason", PAYRESTR, 663, loc="قيود الدفع في المتاجر الإلكترونية", ident="قيود الدفع في المتاجر الإلكترونية")
T("SA-C-122", "responsible", "orders", "suspicious_order.confirm_execution.message",
  note="Shown when the merchant chooses to carry out an order the protection system stopped.")
W("SA-C-122", "boundary", H + "-الأسئلة-الشائعة-حول-خيارات-التحكم-بالطلبات/ix4gbqo2r370slys3y5qqexs", 813,
  part="يعتمد ظهور وسم (عميل غير جاد) بجانب اسم العميل على نظام سلة لمكافحة الاحتيال بالذكاء الاصطناعي, من خلال تحليل بيانات العملاء على متاجر سلة",
  loc="الأسئلة الشائعة", ident="وسم (عميل غير جاد)")
W("SA-C-122", "reason", H + "-الأسئلة-الشائعة-حول-خيارات-التحكم-بالطلبات/ix4gbqo2r370slys3y5qqexs", 813,
  part="وذلك حرصًا لأن تكون سلة بيئة تسوُّق آمنة وموثوقة لكل من التجار والعملاء.", loc="الأسئلة الشائعة", ident="وسم (عميل غير جاد)")
T("SA-C-124", "responsible", "apps", "apps.agreement.hms.description",
  part="فإنك بتحميلك للتطبيق وموافقتك على هذه السياسة، تمنح منصة سلة تفويضًا صريحًا بتحويل المبالغ المتعلقة بتعاملاتك داخل تطبيق الشريك، كما تُخلي سلة مسؤوليتها عن أي منتجات أو مسترجعات أو شحن أو توصيل أو أي عمليات أو تعاملات بينك وبين الشريك.",
  note="Text of 'سياسة إدارة المبالغ المحجوزة' shown when installing an app; the settlements scope is named 'إدارة المبالغ المحجوزة' (statement under boundary).")
T("SA-C-124", "reason", "apps", "apps.agreement.hms.description",
  part="حرصًا على تسهيل المعاملات المالية بين التاجر وشركاء متجر التطبيقات",
  note="Opening of 'سياسة إدارة المبالغ المحجوزة'.")
W("SA-C-127", "boundary", MOYASAR, 653, loc="ربط الجمعيات الخيرية مع بوابة الدفع ميسر", ident="المفتاح السري (Secret Key)")
W("SA-C-127", "reason", H + "تفعيل-أبل-باي-apple-pay-مع-بوابات-الدفع-الخارجية-للجمعيات-الخيرية/cibzvzd4edofyfsygrxmp3p1", 649,
  loc="تفعيل أبل باي Apple Pay مع بوابات الدفع الخارجية للجمعيات الخيرية", ident="Apple Pay للجمعيات الخيرية",
  note="The problem the article gives for this set-up.")

# ---------------- shipping ----------------
W("SA-C-139", "responsible", AWB, 745, loc="3. الربط مع مقدمي خدمات الشحن والتوصيل", ident="الربط مع مقدمي خدمات الشحن والتوصيل",
  note="Names the carriers as providers contracted with Salla.")
W("SA-C-140", "responsible", AWB, 678, loc="أولاً: إصدار بوليصات بأقل تكلفة", ident="إصدار بوليصات بأقل تكلفة")
T("SA-C-140", "responsible", "orders", "actions_bar.create_shipping_policy.summary.postpaid.terms_cancellation_text",
  scope="الدفع الآجل لبوليصات سلة", note="One of 'الشروط والأحكام للدفع الآجل لبوليصات سلة' shown in the dashboard.")
T("SA-C-140", "responsible", "orders", "actions_bar.create_shipping_policy.summary.postpaid.terms_payment_dates_text",
  scope="الدفع الآجل لبوليصات سلة", note="One of 'الشروط والأحكام للدفع الآجل لبوليصات سلة' shown in the dashboard.")
W("SA-C-140", "reason", AWB, 645, loc="كيف تستفيد من بوليصات الشحن في سلة؟", ident="بوليصات الشحن")
W("SA-C-141", "responsible", H + "تفعيل-شركات-الشحن-بعقدك-الخاص-في-الإمارات-سلة/ujm8x82uf5ugvw967vzrhovl", 776, loc="الأسئلة الشائعة",
  ident="ربط عقد أرامكس الخاص بك", scope="الإمارات")
W("SA-C-141", "responsible", H + "تفعيل-شركات-الشحن-بعقدك-الخاص-لمتجرك-في-الكويت/i1l6ohixzgu4kco8s5csm4yp", 760, loc="الأسئلة الشائعة",
  ident="ربط عقد امباور الخاص بك", scope="الكويت")
T("SA-C-145", "responsible", "apps", "apps.managed_settlement.description", note="Shown when installing a carrier's app ({{carrier}}).")
T("SA-C-145", "responsible", "apps", "apps.managed_settlement.how_it_works.step_3", note="Step 3 of 'كيف تعمل الآلية؟'.")
W("SA-C-146", "boundary", INTLREADY, 767, loc="ثانياً- الوزن الفعلي", ident="الوزن الفعلي")
W("SA-C-149", "boundary", PACKING, 753, loc="- تصعيد الطلب إلى سلة", ident="تصعيد الطلب إلى سلة")
W("SA-C-149", "reason", PACKING, 651, loc="طلب مواد التغليف من شركات شحن بوليصات سلة", ident="طلب مواد التغليف",
  note="The problem the article gives for the service.")
W("SA-C-150", "responsible", QUALITY, 681, loc="- ماهي بوابة الجودة؟", ident="بوابة الجودة",
  note="States who follows complaints up; it says nothing on liability for loss or damage.")
W("SA-C-150", "boundary", QUALITY, 786, loc="2- تصعيد الشكوى", ident="تصعيد الشكوى إلى سلة")
W("SA-C-150", "reason", QUALITY, 658, loc="بوابة الجودة لشكاوى الشحن", ident="بوابة الجودة")

# ---------------- tax, customs, markets ----------------
W("SA-C-160", "responsible", H + "التسجيل-في-هيئة-الزكاة-والضريبة-والجمارك/co7zhuxbz7ym8ez5yd9jel3b", 666,
  loc="✅شروط التسجيل في هيئة الزكاة والضريبة والجمارك", ident="شروط التسجيل في هيئة الزكاة والضريبة والجمارك",
  scope="هيئة الزكاة والضريبة والجمارك")
W("SA-C-162", "decides", INTLID, 731, loc="التحقق من الهوية في قطر: 👣خطوات تفعيل الحقل", ident="إظهار حقل المعلومات الجمركية",
  scope="الشحن الدولي إلى قطر وعُمان", note="A step under 'خطوات تفعيل الحقل'; step 1 is (الكل) > (إعدادات الشحن).")
W("SA-C-162", "boundary", AWB, 772, loc="الرسوم الإضافية للشحن الدولي", ident="الرسوم الإضافية للشحن الدولي",
  scope="بوليصات سلة")

# ---------------- policies and agreements ----------------
E("SA-C-170", "where", "SA-S-2208", "<url><loc>https://salla.com/terms</loc></url>", "https://salla.com/terms",
  note="Entry of the held salla.com sitemap (ar-SA).")
E("SA-C-171", "where", "SA-S-2209", "<url><loc>https://salla.com/privacy</loc></url>", "https://salla.com/privacy",
  note="Entry of the held salla.com sitemap (ar-SA).")
E("SA-C-172", "where", "SA-S-2212", "<url><loc>https://salla.com/policies/selling-policies</loc></url>",
  "https://salla.com/policies/selling-policies", note="Entry of the held salla.com sitemap (ar-SA).")
E("SA-C-173", "where", "SA-S-2210",
  "<url><loc>https://salla.com/%D8%A7%D8%AA%D9%81%D8%A7%D9%82%D9%8A%D8%A9-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A7%D9%84%D8%AA%D8%B3%D9%88%D9%8A%D9%82-%D8%A8%D8%A7%D9%84%D8%B9%D9%85%D9%88%D9%84%D8%A9</loc></url>",
  "https://salla.com/اتفاقية-استخدام-التسويق-بالعمولة", note="Entry of the held salla.com sitemap (ar-SA).")
W("SA-C-173", "decides", REFERRAL, 689, loc="متى تبدأ العمولة؟", ident="برنامج الإحالة لباقات سلة")
W("SA-C-173", "boundary", REFERRAL, 697, loc="متى تُحوّل أرباح الإحالة؟", ident="برنامج الإحالة لباقات سلة")
E("SA-C-174", "where", "SA-S-2211", "<url><loc>https://salla.com/policies/publising-app-maker</loc></url>",
  "https://salla.com/policies/publising-app-maker", note="Entry of the held salla.com sitemap (ar-SA).")
W("SA-C-174", "decides", APPPOL, 688, loc="سياسة الغاء خدمة التطبيق و تجديد الاشتراك", ident="سياسة الغاء خدمة التطبيق و تجديد الاشتراك")
W("SA-C-174", "responsible", APPPOL, 729, loc="إخلاء مسؤولية:", ident="إخلاء مسؤولية",
  note="The help article carries the publishing policy for apps made with App Maker (Google & Apple).")
T("SA-C-174", "boundary", "app-maker", "form.accept_privacy_policy.label", note="Checkbox in the App Maker subscription form.")
W("SA-C-174", "reason", APPPOL, 699, loc="سياسة تطبيقات الجمعيات الخيرية", ident="سياسة تطبيقات الجمعيات الخيرية",
  scope="تطبيقات الجمعيات الخيرية")
J("SA-C-175", "where", "partners.salla.com/sitemap.xml", 88, ident="https://partners.salla.com/en/legal-en/apps-policy",
  note="Entry of the held partners.salla.com sitemap; the Arabic page read is https://partners.salla.com/legal/apps-policy.")
J("SA-C-176", "where", "partners.salla.com/sitemap.xml", 85, ident="https://partners.salla.com/en/legal-en/privacy",
  note="Entry of the held partners.salla.com sitemap; the page is 'سياسة الانضمام إلى برنامج شركاء سلة'.")
W("SA-C-176", "decides", JOIN, 130, loc="المادة السابعة – التعديلات على السياسة", ident="المادة السابعة – التعديلات على السياسة")
W("SA-C-178", "where", COMPLAINTS, 716, loc="كيف يمكن للعميل رفع شكوى على المتجر:", ident="صفحة نظام الشكاوى")
W("SA-C-178", "decides", COMPLAINTS, 710, loc="خطوات الوصول إلى شكوى العميل", ident="إقفال الشكوى")
W("SA-C-178", "responsible", COMPLAINTS, 840, loc="الأسئلة الشائعة", ident="❓ماهو دور سلة في الشكاوى على المتاجر",
  note="Answer to 'ماهو دور سلة في الشكاوى على المتاجر'.")
W("SA-C-178", "boundary", COMPLAINTS, 818, loc="الأسئلة الشائعة", ident="❓ماهي إشعارات حالات الشكاوى الحالية؟",
  note="First of the complaint statuses listed.")
W("SA-C-179", "boundary", COMPLAINTS, 654, loc="خطوات الوصول إلى شكوى العميل", ident="شكاوي العملاء")
E("SA-C-180", "where", "SA-S-2213", "<url><loc>https://salla.com/policies/nd96</loc></url>", "https://salla.com/policies/nd96",
  note="Entry of the held salla.com sitemap (ar-SA).")

# ---------------- apps and developers ----------------
W("SA-C-191", "where", D + "authorization.md", 176,
  part="Set up the App Scope and check the boxes that matches your app scope, such as Product, Order and Webhooks, then click Update Scope.",
  loc="## Easy Mode (Recommended) > App Scopes Setup", ident="App Scopes Setup", note="A step of setting up an app in the Partners Portal.")
W("SA-C-191", "reason", D + "authorization.md", 66,
  part="By requiring the merchant to grant permission for the App to access their data within specific scope, this process helps to ensure that the store's data is safe and private.",
  loc="## Authorization", ident="OAuth 2.0 authorization flow")
W("SA-C-192", "reason", D + "webhooks.md", 21,
  part="When an event occurs, Salla will send these headers and the relevant details to the specified App along with the token or signature verifies that the request is from Salla.",
  loc="## Security Implementation", ident="Security Implementation")
W("SA-C-193", "where", D + "partner-apis/app-events.md", 3, loc="# App Events", ident="App Events")
W("SA-C-193", "decides", D + "partner-apis/app-events.md", 24,
  part="To test the app events in demo stores, save the app as a draft after setting the app price(s).",
  loc=":::tip[Test App Events]", ident="Test App Events", scope="demo stores")
W("SA-C-203", "decides", D + "salla-cli/welcome.md", 13, part="Create a partner account on Salla Partners Portal.",
  loc="### Prerequisites", ident="Salla CLI prerequisites")
W("SA-C-203", "reason", D + "salla-cli/welcome.md", 6,
  part="Salla CLI tool is developed by Salla team to help in creating Salla Apps and Themes by using only 1-command!",
  loc=":::note[Tip]", ident="Salla CLI")
W("SA-C-204", "responsible", JOIN, 68, loc="المادة الرابعة – التزامات الشركاء > أولاً التزامات الشركاء العامة", ident="التزامات الشركاء العامة")
W("SA-C-204", "boundary", JOIN, 125, loc="المادة السادسة – الاتصالات الرسمية", ident="المادة السادسة – الاتصالات الرسمية")
W("SA-C-204", "reason", JOIN, 111, loc="المادة الخامسة-طبيعة التزام منصة سلة", ident="المادة الخامسة-طبيعة التزام منصة سلة")
W("SA-C-205", "boundary", SERVPROV, 42, loc="سياسة تقديم الخدمات في منصة الشركاء", ident="سياسة تقديم الخدمات في منصة الشركاء")
T("SA-C-205", "reason", "merchant-services", "service.infoBanner.listSubTitle1", note="Banner text on the Merchant Services page.")
W("SA-C-206", "boundary", INFLU, 24, loc="سياسة تقديم الإعلانات في منصة الشركاء", ident="سياسة تقديم الإعلانات في منصة الشركاء",
  scope="الشركاء الذين يقدمون الإعلانات في منصة الشركاء")
W("SA-C-206", "reason", INFLU, 38,
  part="تحرص منصة سلة على بيئة منافسة عادلة بين الشركاء، ويُتوقع من الشركاء تقديم خدماتهم عبر المنصة بأسعار مماثلة أو أقل من تلك المعروضة في قنواتهم الأخرى",
  loc="سياسة تقديم الإعلانات في منصة الشركاء", ident="سياسة تقديم الإعلانات في منصة الشركاء",
  scope="الشركاء الذين يقدمون الإعلانات في منصة الشركاء", note="The reason given for expecting partners' prices on the platform to match their other channels.")
W("SA-C-208", "boundary", D + "twilight-engine/publish-theme.md", 23, loc="### Theme Publication", ident="Theme Publication")
T("SA-C-208", "reason", "themes-marketplace-monorepo", "faqs.answer5", note="FAQ answer in the Theme Marketplace.")
W("SA-C-208", "reason", D + "twilight-engine/publish-theme.md", 91,
  part="to align with our platform's pricing policy and ensure fair compensation for your effort.",
  loc="#### 3 Theme Price", ident="Theme Price",
  note="Reason for the minimum theme price, which this page gives as SAR250; the held partner FAQ gives 150 ر.س (statement under decides). Recorded, not resolved.")
J("SA-C-208", "decides", PHC, 7, field="1751913203", ident="من الذي يحدد سعر الثيم؟", loc="line 7 (article 1751913203)",
  note="Partner help-centre answer; the theme publishing docs give SAR250 (statement under reason). Recorded, not resolved.")
J("SA-C-209", "decides", PHC, 1, field="1984760154", ident="كم عدد المتاجر التجريبية التي يمكنني إنشائها ؟", loc="line 1 (article 1984760154)")
T("SA-C-209", "responsible", "devstore", "devstore.privacy-and-terms.privacy.items[4]",
  note="One of the items of the privacy and terms shown in the dev store pages of the dashboard.")
J("SA-C-209", "boundary", PHC, 5, field="1131548349",
  part="يمكنك إختبار تطبيقك قبل إطلاقه عبر متاجر تجريبية توفرها البوابة لكل مطور بشكل مجاني.",
  ident="كيف يمكنني إختبار تطبيقي قبل إطلاقه على متاجر سلة؟", loc="line 5 (article 1131548349)")
J("SA-C-209", "reason", PHC, 13, field="711291874", ident="هل فيه مراجعة أو موافقة من فريق سلة قبل نشر المتجر؟",
  loc="line 13 (article 711291874)", scope="المتاجر الجاهزة")

# ---------------- legal, licences, sanctions, security ----------------
W("SA-C-231", "responsible", SLA, 41, loc="ثانياً: التراخيص والنطاق التقني > 2.1 التأهيل والامتثال النظامي", ident="2.1 التأهيل والامتثال النظامي",
  part="يُقر الشريك ويتعهد بأنه يمتلك الكفاءة الفنية والتأهيل المهني اللازم لتقديم الخدمات، وأنه حاصل على كافة التراخيص، التصاريح، والسجلات التجارية السارية واللازمة لممارسة نشاطه داخل المملكة العربية السعودية وفق الأنظمة واللوائح المتعلقة بنشاطه.",
  scope="الشركاء والوكالات في برنامج تسريع نمو المتاجر")
J("SA-C-231", "where", PHC, 10, field="434594320", ident="ماهي رخصة التسويق (موثوق)؟", loc="line 10 (article 434594320)",
  part="هي رخصة يمكنك الحصول عليها من موقع الهيئة العامة لتنظيم الإعلام، والتي تسمح للأفراد بالتسويق على منصات التواصل الإجتماعي",
  scope="المؤثرون في شركاء سلة (رخصة موثوق)")
W("SA-C-232", "responsible", APPPOL, 718, loc="حتى يحصل تطبيقك على الموافقة بالنشر في متجر التطبيقات يجب الإلتزام بالقواعد التالية :",
  ident="سياسة نشر التطبيق في متجر التطبيقات", scope="تطبيقات المتاجر على متاجر Google وApple (صانع التطبيقات)")
W("SA-C-234", "reason", FRAUDTIPS, 760, loc="ثامناً. نظام التحقق بخطوتين", ident="نظام التحقق بخطوتين")

# ---------------- new concerns ----------------
J("SA-C-301", "where", "structures/salla/portal-menu-definitions/layout-mf@prod/items.jsonl", 91,
  part='"title":"Domains Management","route":"domains"', ident="Domains Management", loc="line 91")
J("SA-C-301", "decides", "structures/salla/portal-menu-definitions/layout-mf@prod/items.jsonl", 90,
  part='"feature":{"expr":"io.DOMAIN_PURCHASE","value":"domain-purchase"},"permissions":[{"expr":"Wi.MANAGE_DOMAINS","value":"manage-domains"}]',
  ident="Domains", loc="line 90", note="The Domains group of the Partners portal menu: feature flag and permission.")
J("SA-C-301", "boundary", "raw/runs/20261008T145200Z-sweep-partner-portal-routes-en/responses.jsonl", None,
  part='"method":"GET","host":"api.salla.dev","path":"/partner-reports/v1/domains/stats"', ident="/partner-reports/v1/domains/stats",
  note="A request the Partners portal made during a recorded sweep (2026-10-08).")
J("SA-C-302", "where", "partners.salla.com/sitemap.xml", 83, ident="partners.salla.com/en/legal-en/ (store migration terms)",
  note="Entry of the held partners.salla.com sitemap; the Arabic page read is " + MIGR)
W("SA-C-302", "decides", MIGR, 33, loc="المادة (2): شروط الاستفادة من الخدمة", ident="المادة (2): شروط الاستفادة من الخدمة")
W("SA-C-302", "responsible", MIGR, 20, part="ترحب منصة \"سلة\"، المملوكة لشركة منصة سلة للاتصالات وتقنية المعلومات (س.ت: 4031200589)",
  loc="المقدمة:", ident="المقدمة")
W("SA-C-302", "boundary", MIGR, 47, loc="المادة (4): المزايا المتاحة ضمن الخدمة", ident="المادة (4): المزايا المتاحة ضمن الخدمة")
W("SA-C-302", "reason", MIGR, 20, part="وتوفر خدمة تهدف إلى تسهيل عملية النقل من منصات التجارة الإلكترونية الأخرى",
  loc="المقدمة:", ident="المقدمة")
J("SA-C-303", "where", "partners.salla.com/sitemap.xml", 81, ident="partners.salla.com/en/legal-en/ (agencies SLA)",
  note="Entry of the held partners.salla.com sitemap; the Arabic page read is " + SLA)
W("SA-C-303", "decides", SLA, 50, loc="ثالثاً: آلية الإسناد واشتراط الموافقة المسبقة للتاجر > 3.1", ident="3.1 الموافقة المسبقة للتاجر شرط للإسناد")
W("SA-C-303", "responsible", SLA, 28, loc="أولاً: الطبيعة القانونية للبرنامج وإخلاء المسؤولية > 1.1 صفة المنصة", ident="1.1 صفة المنصة")
W("SA-C-303", "boundary", SLA, 67, loc="رابعاً: معايير مستوى الخدمة والتواصل (SLA) > 4.2", ident="4.2 الشفافية وإعادة التحديث")
J("SA-C-304", "where", "partners.salla.com/sitemap.xml", 22, ident="https://partners.salla.com/global-selling-program",
  note="Entry of the held partners.salla.com sitemap.")
W("SA-C-304", "responsible", GLOBAL, 68, loc="مجالات الشراكة التي نبحث عنها > المدفوعات و البيع بالنيابة (MoR)",
  ident="المدفوعات و البيع بالنيابة (MoR)", note="One of the partnership areas the programme seeks; it names no partner.")
W("SA-C-304", "boundary", GLOBAL, 24, loc="قدّم خدماتك لتجار يتوسعون عالميًا", ident="قدّم خدماتك لتجار يتوسعون عالميًا")

# the same clauses, recorded again under Salla's legal entities (sources name the company differently; recorded, not resolved)
W("SA-C-230", "responsible", MIGR, 20, part="ترحب منصة \"سلة\"، المملوكة لشركة منصة سلة للاتصالات وتقنية المعلومات (س.ت: 4031200589)",
  loc="المقدمة:", ident="المقدمة", scope="شروط وأحكام خدمة انتقال المتاجر من منصات أخرى إلى منصة سلة",
  note="The App Store terms give the same registration number for 'شركة تطبيق سلة لتقنية المعلومات' (SA-S-0015). Recorded, not resolved.")
W("SA-C-230", "responsible", NDPKG, 22, loc="أولًا : التعريفات", ident="\"سلة\" (التعريفات)",
  scope="الشروط والأحكام لحملة اليوم الوطني (95) – باقات/بكجات سلة")

# ---------------- second pass: targeted searches of held text and a few docs pages ----------------
J("SA-C-013", "boundary", PHC, 8, field="1576165181", ident="الخدمة الموفرة من قبلي تتطلب صلاحيات وصول للمتجر، كيف يمكنني تقديم طلب للوصول؟",
  loc="line 8 (article 1576165181)", scope="مزودو الخدمات في بوابة الشركاء")
T("SA-C-014", "boundary", "manage", "support_access.no_request.description", note="Empty state of the page /manage/support-access (وصول الدعم الفني).")
T("SA-C-073", "responsible", "ads-meta", "launch.sweply-is-not-responsible-for-any-results-including-visits-or-sales",
  scope="إعلانات سلة على Meta (ads-meta)", note="The dashboard's ads screens name Sweply; who Sweply is is not stated in the held text.")
W("SA-C-073", "boundary", H + "طرق-الدفع-لإعلانات-سلة/acd9iqfypgjm1acbof6f3ouc", 669, loc="الدفع المسبق > آلية خصم المبالغ", ident="آلية خصم المبالغ")
T("SA-C-073", "boundary", "ads-meta", "launch.add-funds-to-your-sweply-ads-wallet", scope="إعلانات سلة على Meta (ads-meta)")
T("SA-C-074", "boundary", "marketing", "meta.meta_type_1_desc", note="Description of one of the Meta tracking options in the marketing settings.")
J("SA-C-076", "boundary", PHC, 9, field="675177809", ident="ما هي حالات طلبات الحملات؟", loc="line 9 (article 675177809)",
  scope="المؤثرون في شركاء سلة")
T("SA-C-099", "boundary", "chat", "ctaDescTwo", note="Salla Chat promotional text in the dashboard.")
W("SA-C-100", "reason", D + "checkout-apis/overview.md", 14,
  part="This API collection is designed for developers building integrations that need to control cart and checkout-entry flows outside of the standard storefront",
  loc="# Overview", ident="Checkout APIs")
W("SA-C-101", "boundary", D + "twilight-sdk/overview.md", 5, part="Twilight comes with a JavaScript SDK for the Salla storefront APIs.",
  loc="# Overview", ident="Twilight JS SDK")
W("SA-C-101", "reason", D + "twilight-sdk/overview.md", 5,
  part="This is to provide the developers with helper methods, or REST API endpoints, that allow communication between the frontend and backend.",
  loc="# Overview", ident="Twilight JS SDK", note="The purpose given for the SDK over the storefront APIs.")
T("SA-C-113", "where", "payments", "wallet.epayment.summary.tooltips.bank_fees", note="Tooltip in the e-payments summary of the wallet.")
T("SA-C-126", "where", "orders", "payment.pending_desc", note="Shown on an order whose payment is pending.")
T("SA-C-126", "boundary", "chat", "notifications.order.payment_linkDesc", note="Salla Chat notification setting for payment links.")
W("SA-C-210", "boundary", H + "إدارة-وجرد-المخزون/xzpw5e46wflnxg611caz0aem", 874,
  part="عُدلت كمية المنتج عبر مزامنة المخزون مع شركات الشحن أو الأنظمة المحاسبية.", loc="توضيح إضافي للأسباب التي تظهر في جدول سجل المخزون",
  ident="مزامنة المخزون مع الخدمات الخارجية")
W("SA-C-220", "boundary", D + "report-builder/overview.md", 3, loc="# Overview", ident="Report Creator")
T("SA-C-231", "boundary", "channel", "basic_settings.main_store_data.description",
  note="Store data the merchant updates from the theme editor, the Business Platform certificate (شهادة توثيق منصة الأعمال) among them.")
W("SA-C-092", "reason", D + "ecommerc-events/overview.md", 41,
  part="This server-to-server approach removes the need for client-side scripts and ensures events are delivered reliably and securely.",
  loc="### Cloud Mode (App Functions)", ident="Cloud Mode (App Functions)", note="The reason given for Cloud Mode.")
W("SA-C-092", "decides", D + "ecommerc-events/getting-started.md", 19,
  part="Before integrating, determine which mode best fits your application's architecture.",
  loc="# Choose an Integration Mode", ident="Choose an Integration Mode", note="The app developer chooses Device Mode or Cloud Mode.")
W("SA-C-003", "boundary", H + "إدارة-قائمة-المتاجر-المرتبطة/t9z4bp7g0vo1rcdvq4h4k9b3", 698, loc="ربط المتاجر المتطابقة برقم الهاتف لأول مرة",
  ident="قائمة المتاجر المرتبطة")
W("SA-C-003", "reason", H + "إدارة-قائمة-المتاجر-المرتبطة/t9z4bp7g0vo1rcdvq4h4k9b3", 650, loc="إدارة قائمة المتاجر المرتبطة",
  ident="قائمة المتاجر المرتبطة", note="The problem the article gives for the list of linked stores.")
W("SA-C-146", "responsible", H + "رسوم-بوابة-الشحن-الدولي-عبر-بوليصات-سلة-وآلية-احتسابها/cdyymbn20s5oh556ybaphh7q", 714,
  loc="الأسئلة الشائعة", ident="❓ هل يتحمل التاجر أي تكلفة؟", scope="رسوم بوابة الشحن الدولي (بوليصات سلة)",
  note="Answer to 'هل يتحمل التاجر أي تكلفة؟'; it states who bears the international shipping gateway fee.")
