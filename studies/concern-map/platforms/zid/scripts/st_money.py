# Statements and gaps: holding money, payments and Zid's own money services (ZD-C-001 to ZD-C-028).
from stlib import *

# ---------- ZD-C-001 Zid Pay activation ----------
c = "ZD-C-001"
S(c, "where", H("activate-online-payments"), "طريقة تفعيل الدفع الإلكتروني", struct(H("activate-online-payments"), "تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"),
  "المدفوعات > تفعيل الدفع الالكتروني", "ابدأ بتفعيل الدفع الإلكتروني عبر التوجه إلى القائمة الجانبية واختيار المدفوعات و بعد ذلك ، قم بالضغط على ايقونة تفعيل الدفع الالكتروني")
S(c, "decides", H("payment-requirements"), "opening paragraph", struct(H("payment-requirements"), "متطلبات تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"),
  "متطلبات تفعيل الدفع الالكتروني", "لإتاحة خيار الدفع الإلكتروني في المتجر يتطلب تزويد بوابة الدفع بمتطلبات التفعيل حسب الكيان التجاري (فرد – شركة – مؤسسة) ليتم اعتماد الحساب لدى بوابة الدفع.",
  scope="متطلبات تفعيل الدفع الالكتروني للسعودية")
S(c, "decides", AR_ZPSA, "الشروط العامة", ST[AR_ZPSA], "الشروط العامة",
  "يمكن فقط للشركات، والمؤسسات، والأشخاص، والمنظمات المسموح لهم إجراء عمليات دفع واستلام أموال داخل بلادهم من الجهات الرسمية، الاشتراك لاستخدام زد باي.",
  scope="Zid Pay, Saudi Arabia")
S(c, "decides", H("faq-22"), "answer", struct(H("faq-22"), "FAQ: هل بإمكاني كتاجر تفعيل زد باي في متجري في حال كنت من خارج السعودية ؟"),
  "FAQ: تفعيل زد باي من خارج السعودية", "في الوقت الحالي خيار زد باي متاح لتجار المملكة العربية السعودية و دولة الكويت.", scope="المملكة العربية السعودية; دولة الكويت")
S(c, "decides", PRICING, "plan card Rise", ST[PRICING], "Rise (package_code rise): All features of Starter package, plus:",
  "Zid Payments gateway to accept Mada, Visa, and Mastercard", scope="plan Rise; the Starter card lists Basic payment methods (bank transfer, cash on delivery)",
  note="The line sits in the Rise card's group 'All features of Starter package, plus:'.")
S(c, "decides", H("activate-online-payments"), "ملاحظة", struct(H("activate-online-payments"), "تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"),
  "ملاحظة: منتج منشور", "لابد من اضافة منتج واحد منشور ومطابق للنشاط في المتجر قبل رفع طلب التفعيل")
S(c, "responsible", AR_ZPSA, "الشروط العامة", ST[AR_ZPSA], "الشروط العامة",
  "يجب أن يكون التاجر قد تحصّل على متجره وفق شروط وأحكام الدفع الإلكتروني المعتمدة في زد عند الاشتراك ومتوافقة مع جميع المتطلبات النظامية والقانونية، التاجر وحده مسؤولا عن الالتزام بكافة هذه المتطلبات.",
  scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "opening", ST[AR_ZPSA], "شروط وأحكام زد باي", "تمثل الشروط والأحكام المذكورة أدناه العقد المبرم بين مستخدمي زد باي وشركة زد.", scope="Zid Pay, Saudi Arabia")
S(c, "boundary", D("merchant-activation"), "Overview", struct(D("merchant-activation"), "Merchant Activation"), "Link Merchant webhook (merchant_linked)",
  "After the onboarding of the merchant happens at the provider side (a new merchant account / record is created), the provider must share the Public/Secret Keys of the merchant with Zid Payments through this webhook",
  note="Provider side of activation in the Zid Payments Open APIs.")
S(c, "boundary", D("merchant-activation"), "Overview", struct(D("merchant-activation"), "Merchant Activation"), "storeId",
  'Upon redirection to the provider\'s login page, Zid Payments will append the "storeId" query string parameter to the URL, which is the unique identifier for the merchant at Zid.')
S(c, "reason", H("activate-online-payments"), "ملاحظة", struct(H("activate-online-payments"), "تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"),
  "العدد المتوقع لعمليات الدفع", "مشاركة عدد العمليات المتوقعة لغرض ضمان حقك المالي ولا يوجد تأثير على رسوم الخدمة.",
  note="A reason stated for one activation step (expected transaction volume), not for placing activation with the gateway.")
ASK(c, "reason", "Zid's stated reason for having payment gateways approve Zid Pay accounts", "help.zid.sa/payment-requirements/; zid.sa/ar/legal/zidpay-terms-conditions-sa/")

# ---------- ZD-C-002 Zid Pay transactions and refunds ----------
c = "ZD-C-002"
S(c, "where", H("transactions"), "intro", struct(H("transactions"), "العمليات والاسترداد ( لوحة التحكم الجديدة )"), "المدفوعات > العمليات",
  "يمكنك الوصول الى العمليات من خلال : المدفوعات > العمليات")
S(c, "where", H("refund-requests"), "intro", struct(H("refund-requests"), "استرداد المبلغ للعميل ( لوحة التحكم الجديدة )"), "لوحة التحكم > المدفوعات > العمليات",
  "يمكنك استرداد المبلغ الى العميل من خلال : لوحة التحكم > المدفوعات > العمليات")
S(c, "decides", H("refund-requests"), "ملاحظة", struct(H("refund-requests"), "استرداد المبلغ للعميل ( لوحة التحكم الجديدة )"), "ملاحظة: 30 يوم",
  "لا يمكن استرداد المبلغ للعميل بعد مرور 30 يوم من تاريخ الشراء")
S(c, "decides", H("zidpay_staff_and_currencies"), "صلاحيات فريق العمل", struct(H("zidpay_staff_and_currencies"), "صلاحيات فريق العمل و خاصية العملات"),
  "صلاحية استرداد المبالغ", "من خلال هذه الخاصية بامكانك تحديد صلاحية استرداد المبالغ بشكل ( كلي | جزئي) للعميل النهائي.", scope="staff permission (الاعدادات > فريق عمل)")
S(c, "decides", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "رد الأموال",
  "المستخدم متاح له استخدام خيار “رد الأموال” لاسترداد مبلغ عملية الدفع بالكامل أو جزء منه وعليه يجب أن يتوفر رصيد كافي في حسابه لدى زد باي لاستخدام خيار “رد الأموال”.",
  scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "حدود المسؤولية", ST[AR_ZPSA], "حدود المسؤولية",
  "التاجر هو المسؤول الوحيد عن طبيعة عمليات الدفع التي تتم على حسابه سواء خاطئة أو مشبوهة، وزد باي لن تتحمل أي مسؤولية عن أي عملية دفع لابد من ردها إلى مصدرها.",
  scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "الشروط العامة", ST[AR_ZPSA], "تفويض زد", "إن استخدام التاجر للخدمة في تنفيذ عملياته  تعني تفويض زد بإجراء تلك العملية", scope="Zid Pay, Saudi Arabia")
S(c, "boundary", LLMS, "API Docs: Refund", ST[LLMS], "Refund > Request Refund (POST /{ProviderUrl}/refund)", APIW("Refund"),
  note="The refund call goes from Zid Payments to the provider's API (Zid Payments Open APIs).")
S(c, "boundary", D("overview-1341008m0"), "Request Model", struct(D("overview-1341008m0"), "Webhooks Overview (Zid Payments)"), "refund_status_changed",
  "Types:<br>“merchant_linked”,<br>“payment_paid”,<br>“refund_status_changed”", note="Provider-to-Zid Payments webhook types.")
SNF(c, "reason", "A stated reason for running refunds through the Zid Pay balance", "help.zid.sa/refund-requests/; help.zid.sa/transactions/; zid.sa/ar/legal/zidpay-terms-conditions-sa/")

# ---------- ZD-C-003 Zid Pay deposits ----------
c = "ZD-C-003"
S(c, "where", H("deposits_zidpay"), "كشف الحساب والإيداعات", struct(H("deposits_zidpay"), "خصائص زد باي | كشف الحساب و الإيداعات"), "كشف الحساب",
  "يمكنك الوصول إلى الصفحة عن طريق الضغط على أيقونة كشف الحساب في الصفحة الرئيسية.")
S(c, "where", H("deposits_zidpay"), "ملاحظة", struct(H("deposits_zidpay"), "خصائص زد باي | كشف الحساب و الإيداعات"), "قيد المعالجة",
  "يتم يومياً في تمام الساعة 12 AM انتقال الرصيد الحالي و جميع العمليات إلى رصيد قيد المعالجة لتتم مراجعة المعلومات وتهيئتها لعملية الإيداع  في الحساب البنكي في أقرب يوم تحصيل.")
S(c, "decides", AR_ZPSA, "تحصيل المبالغ", ST[AR_ZPSA], "تحصيل المبالغ", "تُحصّل المبالغ ثلاث مرات أسبوعيًا.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "تحصيل المبالغ", ST[AR_ZPSA], "تحصيل المبالغ: الحد الأدنى", "تُحصّل المبالغ عند اجتياز المبالغ المحصلة للحد الأدنى وهو: ١٠٠ ريال.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "تحصيل المبالغ", ST[AR_ZPSA], "رسوم الإيداع",
  "يتم فرض رسوم رمزية بقيمة ٣ ريال مع إجمالي كل عملية إيداع، باستثناء التجار من عملاء بنك الرياض يعفون من رسوم الإيداع.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "أيام التسوية",
  "تسوية عمليات الدفع والإيداعات تتم في يوم الأحد، والثلاثاء، والخميس من كل أسبوع.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPKW, "تحصيل المبالغ", ST[AR_ZPKW], "تحصيل المبالغ", "تُحصّل المبالغ بشكل يومي.", scope="Zid Pay, Kuwait")
S(c, "decides", AR_ZPKW, "تحصيل المبالغ", ST[AR_ZPKW], "تحصيل المبالغ: الحد الأدنى", "تحوّل المبالغ عند اجتياز المبالغ المحصلة ١ دينار كويتي.", scope="Zid Pay, Kuwait")
S(c, "decides", H("activate-online-payments"), "إيداع المبالغ", struct(H("activate-online-payments"), "تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"), "إيداع المبالغ",
  "يتم إيداع المبالغ المحصلة إلى حسابك البنكي بعد اعتماد المعلومات بشكل يومي من الأحد إلى الخميس.",
  note="Sources differ on the Saudi deposit days: this article's general line says daily Sunday to Thursday; its Saudi section, the Zid Pay terms and the deposits article say Sunday, Tuesday, Thursday. Recorded as found.")
S(c, "decides", PAYMENTS, "How We Power Your Payments, 07", ST[PAYMENTS], "Hassle-Free Fund Collection",
  "We'll deposit your funds every 2-3 days, complete with a detailed report.")
S(c, "responsible", AR_ZPSA, "تحصيل المبالغ", ST[AR_ZPSA], "مراجعة الإيداع",
  "ستقوم زد باي بمراجعة البيانات وتحديث التاجر بالقبول أو الرفض، مع إعطاءه مهلة للتصحيح قبل إتمام عملية الإيداع.", scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "رصيد التاجر",
  "يجوز لزد باي ومزود الخدمة بخصم رسوم العمليات بشكل مباشر من المبالغ المحصلة وإضافة المبلغ المستحق لرصيد التاجر.", scope="Zid Pay, Saudi Arabia")
S(c, "responsible", H("faq-10"), "answer", struct(H("faq-10"), "FAQ: في حال تم تعطيل زد باي هل يتم تحويل رصيد المبالغ؟"), "تعطيل زد باي",
  "نعم يتم تحويل المبلغ المتوفر في رصيد التاجر  إلى الحساب البنكي.")
ASK(c, "responsible", "Which licensed entity or bank holds collected Zid Pay funds between collection and deposit, and under which licence", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; zid.sa/ar/legal/terms-conditions/ (زد باي); help.zid.sa/deposits_zidpay/")
SNF(c, "boundary", "An API endpoint, scope or webhook for Zid Pay deposits in the Merchant APIs", "docs.zid.sa/llms.txt (all API groups read); docs.zid.sa/payment-paid-event-17956148e0.md",
    why="All API reference groups were read; the Merchant APIs name no deposit endpoint, scope or webhook.")
SNF(c, "reason", "A stated reason for the deposit schedule or the minimum amount", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; help.zid.sa/deposits_zidpay/; help.zid.sa/activate-online-payments/")

# ---------- ZD-C-004 Bank accounts ----------
c = "ZD-C-004"
S(c, "where", H("bank-accounts"), "intro", struct(H("bank-accounts"), "الحسابات البنكية ( لوحة التحكم الجديدة )"), "إدارة طرق الدفع > الحسابات البنكية",
  "يمكنك الوصول الى الحسابات البنكية من خلال : إدارة طرق الدفع > الحسابات البنكية")
S(c, "decides", H("activate-online-payments"), "الخطوة الثانية", struct(H("activate-online-payments"), "تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"), "اختيار الحساب البنكي",
  "قم باختيار الحساب البنكي لاستقبال إيداعات المبالغ المحصلة .")
S(c, "decides", H("activate-online-payments"), "ملاحظة", struct(H("activate-online-payments"), "تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"), "مطابقة الهوية",
  "لابد من مطابقة الهوية للحساب البنكي ليتم التحقق بنجاح")
S(c, "decides", H("faq-2"), "answer", struct(H("faq-2"), "FAQ: ماهي البنوك التي تدعمها زد باي لتحصيل المبالغ ؟"), "البنوك المدعومة", "زد باي تدعم جميع البنوك في السعودية.")
S(c, "decides", H("bank-accounts"), "اختيار البنك", struct(H("bank-accounts"), "الحسابات البنكية ( لوحة التحكم الجديدة )"), "اختيار البنك",
  "اختر البنك من القائمة التي تحتوي على البنوك السعودية، بالإضافة إلى مجموعة من بنوك دول الخليج.")
S(c, "responsible", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "البيانات البنكية",
  "تسوية الإيداعات تتم على البيانات البنكية المتوفرة من المستخدم عند تسجيل الحساب لدى زد باي.", scope="Zid Pay, Saudi Arabia")
SNF(c, "boundary", "An API endpoint, scope or webhook for store bank accounts", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names store bank accounts.")
SNF(c, "reason", "A stated reason for the bank account rules (identity match, Saudi and Gulf banks)", "help.zid.sa/bank-accounts/; help.zid.sa/activate-online-payments/")

# ---------- ZD-C-005 Payment networks ----------
c = "ZD-C-005"
S(c, "where", H("about_zidpay"), "الشبكات المدعومة", struct(H("about_zidpay"), "عن زد باي"), "إدارة زد باي",
  "يمكنك إتاحة الشبكات في زد باي عن طريق تفعيل الشبكة المرغوبة من خلال إدارة زد باي")
S(c, "decides", H("faq-33"), "answer", struct(H("faq-33"), "FAQ: هل يجب أفعل جميع الشبكات ( فيزا – ماستركارد – مدى –الخ) ؟"), "كي نت",
  "لا. في زد باي متاح لك حرية تفعيل الشبكات بحسب ما تراه مناسب لك, سواء كنت فرد أم مؤسسة بإمكانك التحكم بتفعيل جميع الشبكات باستثناء شبكة كي نت فهي متاحة للمؤسسات والشركات فقط.")
S(c, "decides", PRICING, "plan card Rise", ST[PRICING], "Rise: All features of Starter package, plus:", "Enable Apple Pay for faster checkout", scope="plan Rise")
S(c, "decides", H("faq-27"), "answer", struct(H("faq-27"), "FAQ: هل يمكن تفعيل آبل باي لبطاقات مدى فقط دون بطاقات فيزا و ماستركارد ؟"), "آبل باي ( مدى )",
  "نعم ، متاح لك حرية الاختيار للتحكم في تفعيل آبل باي ( مدى ) فقط أو آبل باي ( فيزا أو ماستركارد) ) فقط أو كلاهما.")
S(c, "decides", PAYMENTS, "FAQ For our Kuwait Crew", ST[PAYMENTS], "Who's on the payment network lineup?",
  'Who\'s on the payment network lineup?","answer":"K-Net, Apple Pay, Visa, American Express.', scope="Kuwait",
  note="FAQ question and answer as held in the page's embedded data (the answer opens on click).")
S(c, "responsible", AR_ZPSA, "حدود المسؤولية", ST[AR_ZPSA], "شبكات الدفع", "يقر التاجر ويوافق على أن خيارات الدفع (شبكات الدفع) خاضعة لشروط وأحكام مقدم الخدمة.", scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "الشروط العامة", ST[AR_ZPSA], "Apple Pay Merchant Terms",
  "يقر ويفهم التاجر الذي يستخدم طريقة الدفع “Apple Pay” أنه خاضع لشروط وأحكام شركة أبل", scope="Zid Pay, Saudi Arabia")
S(c, "boundary", D("get-payment-options-43307434e0"), "description", struct(D("get-payment-options-43307434e0"), "Get Payment Options"),
  EP("get-payment-options-43307434e0") + " (third_payment_read)",
  "Returns the store’s enabled payment options, including card networks and built-in payment methods available through ZidPay.")
S(c, "boundary", D("embedded-payment-1030692m0"), "Config params", struct(D("embedded-payment-1030692m0"), "Embedded Payment"), "supportedNetworks",
  "| supportedNetworks | string | Networks to be displayed<br>Example:<br>\"visa,mada,amex\" |", note="Provider-side form configuration in the Zid Payments Open APIs.")
S(c, "reason", H("zidpay-paymentpage"), "intro", struct(H("zidpay-paymentpage"), "خطوة الدفع في زد باي"), "خطوة الدفع",
  "ومن باب تسريع مرحلة الدفع الإلكتروني في خطوة الشراء ، عند تفعيل زد باي في المتجر يمكن للعميل النهائي إتمام عملية الشراء بشكل كامل من خلال المتجر دون الحاجة لنقله إلى صفحة دفع أخرى لتعبئة معلومات البطاقة البنكية.",
  note="A reason stated for taking card details on the store page rather than on another payment page.")

# ---------- ZD-C-006 Zid Pay fees ----------
c = "ZD-C-006"
S(c, "where", H("activate-online-payments"), "طريقة تفعيل الدفع الإلكتروني", struct(H("activate-online-payments"), "تفعيل الدفع الالكتروني ( لوحة التحكم الجديدة )"), "اعرف المزيد",
  "من خلال ايقونة اعرف المزيد يمكنك استعراض مميزات المدفوعات الالكترونية والاطلاع على الرسوم حسب الباقات")
S(c, "decides", AR_ZPSA, "رسوم العمليات", ST[AR_ZPSA], "رسوم العمليات",
  "رسوم زد باي تعتمد على حسب باقتك المختارة في متجر زد، فإن كانت باقتك الأساسية تُفرض عليك رسوم زد باي للباقة الأساسية وإن كانت باقة النمو تُفرض عليك رسوم زد باي لباقة النمو.",
  scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "رسوم العمليات", ST[AR_ZPSA], "سقف مدى", "تحديد سقف أعلى بقيمة ٢٠٠ ريال لنسبة شبكة الدفع مدى (غير شامل لضريبة القيمة المضافه).", scope="Zid Pay, Saudi Arabia")
S(c, "decides", PAYMENTS, "Grab Your Perfect Plan", ST[PAYMENTS], "Transaction Fees (Rise, Growth, Professional)",
  "Transaction Fees: 1% + 1 SAR 2.3% + 1 SAR Based on the card used 3.3% + 1 SAR All fees exclude VAT",
  note="Table cells read in page order; the page does not state in text which cell belongs to which plan column.")
S(c, "decides", H("faq-14"), "مثال", struct(H("faq-14"), "FAQ: كيف يتم تحديد رسوم العمليات؟"), "مثال: مدى، باقة النمو",
  "عملية بقيمة 100 ريال تمت عن طريق شبكة الدفع مدى وباقة التاجر النمو", scope="mada, plan النمو",
  note="The FAQ continues: الرسوم: 1% + 1 ريال = 2 ريال.")
S(c, "decides", AR_ZPSA, "الشروط العامة", ST[AR_ZPSA], "عمولة", "يحق لزد تغيير عمولة عمليات شراء التاجر في أي وقت.", scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "رسوم رمزية", "يجوز لزد باي ومزودو الخدمة باقتطاع رسوم رمزية على إجمالي العملية.", scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "الشروط العامة", ST[AR_ZPSA], "ضريبة القيمة المضافة على حامل البطاقة",
  "يتعهد التاجر بعدم تحميل حامل البطاقة أي جزء من الرسوم أو الضرائب التي قد يكون التاجر مسؤولاً عن دفعها بموجب هذه الأحكام والشروط أو أي نظام ساري في المملكة العربية السعودية بما في ذلك نظام ضريبة القيمة المضافة، سواء بزيادة الأسعار أو غير ذلك، أو دفع أي تكلفة تمويل مطلوبة تتعلق بالبطاقات المستخدمة عبر الخدمة.",
  quote="يتعهد التاجر بعدم تحميل حامل البطاقة أي جزء من الرسوم أو الضرائب التي قد يكون التاجر مسؤولاً عن دفعها بموجب هذه الأحكام والشروط أو أي نظام ساري في المملكة العربية السعودية بما في ذلك نظام ضريبة القيمة المضافة",
  scope="Zid Pay, Saudi Arabia")
SNF(c, "boundary", "An API field or endpoint that exposes Zid Pay fees to apps", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names Zid Pay fees.")
SNF(c, "reason", "A stated reason for tying the fee to the Zid plan", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; zid.sa/en/solutions/payments/; help.zid.sa FAQ كيف يتم تحديد رسوم العمليات؟")

# ---------- ZD-C-007 Chargebacks, fraud and held funds ----------
c = "ZD-C-007"
S(c, "where", PAYMENTS, "Fraud Shield", ST[PAYMENTS], "Fraud Shield",
  "Our advanced fraud protection system watches over your transactions, spotting any suspicious activity before it becomes a problem.")
S(c, "decides", PRICING, "plan card Growth", ST[PRICING], "Growth: All features of Rise package, plus:", "Fraud protection to prevent losses", scope="plan Growth")
S(c, "decides", AR_ZPSA, "حدود المسؤولية", ST[AR_ZPSA], "توصية مزودي الخدمة",
  "يحق لزد باي بناءً على توصية مزودي الخدمة القيام بـ -على سبيل المثال لا الحصر- تعليق الخدمة مؤقتًا، احتجاز بعض أو كل الأموال، تمديد فترة احتجاز الأموال، أو تعليق الخدمة في حال وجود تكرار في طلبات الرسوم التعويضية (Chargeback) على حسابك بشكل غير مبرر.",
  quote="يحق لزد باي بناءً على توصية مزودي الخدمة القيام بـ -على سبيل المثال لا الحصر- تعليق الخدمة مؤقتًا، احتجاز بعض أو كل الأموال، تمديد فترة احتجاز الأموال",
  scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "مبلغ احتياطي",
  "قد تقوم زد باي بحجز مبلغ احتياطي يحسب من حجم معاملات العملاء ذوى المخاطر العالية. يتم تسوية هذا المبلغ الاحتياطي عند إغلاق الحسابات في حالة عدم استخدامها.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "احتجاز المدفوعات",
  "يجوز لزد باي احتجاز المدفوعات لفترة غير محددة إذا توصلت إلى أو وجدت أن عمليات الدفع قد تكون مشبوهة أو غير قانونية.", scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "الشروط العامة", ST[AR_ZPSA], "charge back",
  "يتحمل التاجر مسؤولية تسديد المبالغ التي تخص عمليات رد المبالغ المدفوعة  “charge back ” أو المبالغ التي تخص دعاوى الاحتيال “Fraud” و تم خصمها من زد باي في حالة خسارة النزاع لصالح صاحب البطاقة البنكية",
  scope="Zid Pay, Saudi Arabia")
S(c, "responsible", EN_ZPSA, "Liability", ST[EN_ZPSA], "Liability", "Zid Pay assumes no responsibility for disputes or chargebacks, which are the merchant's liability.", scope="Zid Pay, Saudi Arabia")
SNF(c, "boundary", "An API endpoint, scope or webhook for chargebacks, disputes or fund holds", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names chargebacks, disputes or holds.")
SNF(c, "reason", "A stated reason for holding funds or keeping a reserve", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; zid.sa/en/solutions/payments/")

# ---------- ZD-C-008 Payment links ----------
c = "ZD-C-008"
S(c, "where", H("payment-links"), "intro", struct(H("payment-links"), "روابط الدفع ( لوحة التحكم الجديدة )"), "الخدمات > المدفوعات > روابط الدفع",
  "يمكنك الوصول الى روابط الدفع وإدارتها من خلال : الخدمات > المدفوعات > روابط الدفع")
S(c, "decides", H("payment-links"), "خطوات انشاء طلب يدوي", struct(H("payment-links"), "روابط الدفع ( لوحة التحكم الجديدة )"), "الطلبات > الطلبات اليدوية > إنشاء طلب جديد",
  "في صفحة روابط الدفع ستظهر لك  جميع الروابط لاستعراضها وتصديرها ولإنشاء رابط دفع  يتم من خلال : الطلبات > الطلبات اليدوية > إنشاء طلب جديد")
GEN(c)
S(c, "boundary", D("get-payment-options-43307434e0"), "Note", struct(D("get-payment-options-43307434e0"), "Get Payment Options"), "payment_link",
  "The value field can include card network identifiers or built-in values such as bank, direct, prepaid, and payment_link.")
SNF(c, "reason", "A stated reason for payment links' placement", "help.zid.sa/payment-links/; help.zid.sa/tap-gateway/")

# ---------- ZD-C-009 Payment service providers behind Zid Pay ----------
c = "ZD-C-009"
S(c, "where", AR_ZPSA, "التعريفات", ST[AR_ZPSA], "زد باي (definition)",
  "زد باي: هي خدمة تمكين التاجر من تنفيذ عمليات البيع والتجارة الإلكترونية من خلال مقدمي خدمات الدفع على منصة تابعة لزد", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "الأنشطة المحظورة", ST[AR_ZPSA], "المنتجات الرقمية", "المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة",
  scope="Zid Pay, Saudi Arabia")
S(c, "decides", H("nafath_verification"), "ملاحظة", struct(H("nafath_verification"), "اجتياز التحقق من نفاذ"), "طلب التحقق", "يكون طلب التحقق باسم مزود الخدمة.")
S(c, "responsible", AR_TERMS, "زد باي", ST[AR_TERMS], "زد باي: حدود المسؤولية",
  "يوافق التاجر ويدرك أن زد لن تكون مسؤولة عن أي أضرار مباشرة أو غير مباشرة أو عرضية أو خاصة أو تبعية أو فادحة بما في ذلك على سبيل الذكر لا الحصر الأضرار الناجمة عن خسارة الربح أو السمعة أو الاستخدام أو البيانات أو الخسائر غير الملموسة الأخرى الناتجة من استخدام الخدمة أو عدم القدرة على استخدامها أو عدم تقديم شركات مقدمي خدمات الدفع للخدمة  بطريقة فعّالة.",
  quote="الناتجة من استخدام الخدمة أو عدم القدرة على استخدامها أو عدم تقديم شركات مقدمي خدمات الدفع للخدمة  بطريقة فعّالة.",
  note="What happens when a provider fails, as the Terms state it.")
S(c, "responsible", AR_ZPSA, "حق تقديم الخدمة بالتعاقد من الباطن", ST[AR_ZPSA], "التعاقد من الباطن", "يحق لزد باي تقديم الخدمة عن طريق التعاقد من الباطن دون أي إشعارات أو إفصاحات.", scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "ظروف القوة القهرية", ST[AR_ZPSA], "فشل في النظام المصرفي",
  "لن تتحمل زد باي أي مسؤولية عن أي خسارة أو تأخير بسبب الحريق، أو الكوارث الطبيعية أو فشل في النظام المصرفي، أو انقطاع الكهرباء، أو مشاكل في الاتصالات السلكية واللاسلكية، أو الحروب، أو الإضرابات، أو اندلاع أعمال شغب، أو هجمات إرهابية، أو فشل في أداء التجار أو أي حوادث أو أحداث زد باي ليس لها القدرة على التحكم فيها.",
  quote="لن تتحمل زد باي أي مسؤولية عن أي خسارة أو تأخير بسبب الحريق، أو الكوارث الطبيعية أو فشل في النظام المصرفي",
  scope="Zid Pay, Saudi Arabia")
SNF(c, "responsible", "The names and licences of the payment service providers behind Zid Pay", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; zid.sa/ar/legal/zidpay-terms-conditions-kw/; help.zid.sa/about_zidpay/; help.zid.sa/nafath_verification/; zid.sa/en/solutions/payments/",
    why="The pages in the route were read; they speak of مقدمي خدمات الدفع and مزود الخدمة without naming them.")
S(c, "boundary", D("overview-1340225m0"), "intro", struct(D("overview-1340225m0"), "Overview (Zid Payments Open APIs)"), "Open APIs integration model",
  "The Open APIs integration model sets an API contract for our partners to implement.")
SNF(c, "reason", "A stated reason for running Zid Pay through payment service providers", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; zid.sa/ar/legal/terms-conditions/ (زد باي); docs.zid.sa/overview-1340225m0.md")

# ---------- ZD-C-010 Zid Payments Open APIs ----------
c = "ZD-C-010"
S(c, "where", D("overview-1340225m0"), "base URLs", struct(D("overview-1340225m0"), "Overview (Zid Payments Open APIs)"), "zidpay.org",
  "These are the base URLs for Zid Payments' system based on the environment: - Testing environment: https://testing.zidpay.org/ - Production environment: https://zidpay.org/")
S(c, "where", D("overview-1340225m0"), "intro", struct(D("overview-1340225m0"), "Overview (Zid Payments Open APIs)"), "Zid Payments",
  "This document provides a clear explanation for partners / payment service providers (PSPs) who want to integrate with Zid Payments through the Open APIs model.")
S(c, "decides", D("overview-1340608m0"), "intro", struct(D("overview-1340608m0"), "Payment Overview"), "Direct payment; Embedded payment",
  "There are two types of payment checkout on Zid and the provider will choose based on their preference;")
S(c, "decides", D("merchant-activation"), "Overview", struct(D("merchant-activation"), "Merchant Activation"), "thirdPartyProviderId",
  "thirdPartyProviderId is the unique ID of the payment service provider (Zid Payments assigns and provides this ID to the partner upfront before starting the integration)")
ASK(c, "responsible", "The agreement between Zid and a payment service provider that implements the Open APIs (parties, liability, licences)", "docs.zid.sa/overview-1340225m0.md (no agreement linked)")
S(c, "boundary", D("overview-1340608m0"), "Direct payment", struct(D("overview-1340608m0"), "Payment Overview"), "Direct payment",
  "Zid will draw the payment form, then collect and submit the card info using an API, exposed by the provider, through a call made directly from the client side.")
S(c, "boundary", D("overview-1341008m0"), "Path", struct(D("overview-1341008m0"), "Webhooks Overview (Zid Payments)"), "/api/webhook/v1/thirdpartywebhook",
  "This section describes the Webhook endpoint used to send events to Zid Payments.")
S(c, "boundary", D("applepay-3801359f0"), "Overview", struct(D("applepay-3801359f0"), "ApplePay"), "domain association file",
  "During the initial steps of the integration process, a file for each country where the payment provider operates must be provided.")
S(c, "boundary", D("applepay-checkout-1032876m0"), "On Payment Authorized", struct(D("applepay-checkout-1032876m0"), "ApplePay Checkout"), "execute payment",
  "Then, a request will be sent to Zid Payments backend with the encrypted payment payload / token. From there, an execute payment API request will be sent to the payment provider passing the token.")
SNF(c, "reason", "A stated reason for the Open APIs model or for the two checkout types", "docs.zid.sa/overview-1340225m0.md; docs.zid.sa/overview-1340608m0.md; docs.zid.sa/merchant-activation.md")

# ---------- ZD-C-011 Other payment gateways ----------
c = "ZD-C-011"
S(c, "where", H("payment-gateways"), "intro", struct(H("payment-gateways"), "بوابات الدفع الأُخرى( لوحة التحكم الجديدة)"), "المدفوعات > بوابات الدفع الأُخرى",
  "يمكنك الوصول الى بوابات الدفع الأُخرى من خلال : المدفوعات > بوابات الدفع الأُخرى")
S(c, "decides", H("payment-gateways"), "باي موب Paymob", struct(H("payment-gateways"), "بوابات الدفع الأُخرى( لوحة التحكم الجديدة)"), "Paymob",
  "بوابة الدفع باي موب (Paymob) متاحة للتجار في الإمارات، السعودية، وعمان.", scope="الإمارات، السعودية، عمان")
S(c, "decides", H("payment-gateways"), "اموال باي", struct(H("payment-gateways"), "بوابات الدفع الأُخرى( لوحة التحكم الجديدة)"), "amwal pay",
  "بوابة الدفع اموال باي amwal pay متاحة للتجار في عمان", scope="عمان")
S(c, "decides", H("payment-gateways"), "بوابة الدفع تاب Tap", struct(H("payment-gateways"), "بوابات الدفع الأُخرى( لوحة التحكم الجديدة)"), "Tap",
  "بوابة الدفع تاب متاحة لتجار السعودية والكويت والبحرين والامارات ، قطر وعمان", scope="السعودية، الكويت، البحرين، الإمارات، قطر، عمان")
S(c, "decides", AR_ZPSA, "طريقة الاستفادة من خدمات زد باي", ST[AR_ZPSA], "تفعيل الخدمة", "عند تفعيلك لخدمة زد باي ستتعطل بوابة الدفع الأخرى من المتجر.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", H("faq-11"), "answer", struct(H("faq-11"), "FAQ: هل بإمكاني تفعيل زد باي مع أي بوابة دفع أخرى ؟"), "تمارا و تابي",
  "لا يمكن تفعيل أي بوابة دفع أخرى مع زد باي باستثناء تمارا و تابي.")
S(c, "decides", H("gcc-merchants"), "طريقة الدفع", struct(H("gcc-merchants"), "إنشاء متجر في زد لمستخدمي دول الخليج"), "الاعدادات > طرق الدفع",
  "يمكنك تفعيل بوابة الدفع تاب من خلال الاعدادات > طرق الدفع", scope="مستخدمي دول الخليج")
S(c, "responsible", H("tap-gateway"), "intro", struct(H("tap-gateway"), "بوابة الدفع تاب | Tap"), "تاب",
  "تاب بوابة دفع الكترونية مصرحة من البنك المركزي تسمح لك باستقبال المدفوعات عن طريق الوسائل المختلفة مثل مدى، ڤيزا ، ماستر كارد وغيرها كما انها تقدم خدماتها لجميع التجار في السعودية و دول الخليج ومصر.",
  note="A licence statement about a partner gateway, as Zid states it.")
S(c, "responsible", AR_TERMS, "مسؤولية زد أمام المستهلك والتاجر", ST[AR_TERMS], "مسؤولية زد أمام المستهلك والتاجر",
  "زد غير مسؤولة بأي شكل من الأشكال عن أي أداء غير مرضِ أو متأخر من قبل المتاجر أو شركات الشحن أو بوابات الدفع الإلكتروني أو البنوك",
  note="What happens when a gateway, carrier or bank performs badly, as the Terms state it.")
S(c, "boundary", H("tap-gateway"), "تفعيل تاب", struct(H("tap-gateway"), "بوابة الدفع تاب | Tap"), "رقم الهوية المسجل في تاب",
  "ادخل رقم الهوية المسجل في تاب للتحقق عن طريق نفاذ واكمل المعلومات المطلوبة")
S(c, "boundary", H("gcc-merchants"), "طريقة الدفع", struct(H("gcc-merchants"), "إنشاء متجر في زد لمستخدمي دول الخليج"), "مفاتيح الربط", "قم بإدخال مفاتيح الربط")
SNF(c, "reason", "A stated reason for offering other gateways per country", "help.zid.sa/payment-gateways/; help.zid.sa/tap-gateway/; help.zid.sa/gcc-merchants/")

# ---------- ZD-C-012 Store payment methods ----------
c = "ZD-C-012"
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Store Settings", APIW("Merchant APIs > Store Settings", "List Payment Methods"))
S(c, "decides", CHUNK, "compare-plans group Payments", ST[CHUNK], "Various Payment Methods", PL("Various Payment Methods"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Advanced Payment Methods", PL("Advanced Payment Methods"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", H("faq-26"), "answer", struct(H("faq-26"), "FAQ: ماهي طرق الدفع التي استطيع توفيرها في متجري؟"), "طرق الدفع",
  "الدفع عند الاستلام مع شركات التوصيل. التحويل البنكي. مدى. فيزا / ماستر كارد. آبل باي (Apple Pay). أمريكان إكسبريس. سامسونج باي. سداد.")
GEN(c)
S(c, "boundary", D("get-payment-options-43307434e0"), "Scopes", struct(D("get-payment-options-43307434e0"), "Get Payment Options"), EP("get-payment-options-43307434e0"), SCOPEQ("get-payment-options-43307434e0"))
S(c, "boundary", D("list-of-payment-method"), "Scopes", struct(D("list-of-payment-method"), "List Payment Methods"), EP("list-of-payment-method"), SCOPEQ("list-of-payment-method"))
S(c, "boundary", D("list-of-payment-method"), "Note", struct(D("list-of-payment-method"), "List Payment Methods"), "POS payment methods",
  "**Note:** This API does not return the active payment methods configured in POS.")
SNF(c, "reason", "A stated reason for the payment-method placement", "help.zid.sa FAQ ماهي طرق الدفع التي استطيع توفيرها في متجري؟; docs.zid.sa/list-of-payment-method.md")

# ---------- ZD-C-013 Instalment services ----------
c = "ZD-C-013"
S(c, "where", H("bnpl-2"), "intro", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "لوحة التحكم > المدفوعات > الدفع لاحقاً",
  "يمكنك الوصول الى خيارات الدفع بالتقسيط من خلال : لوحة التحكم > المدفوعات > الدفع لاحقاً")
S(c, "decides", H("bnpl-2"), "خدمة مدفوع", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "مدفوع", "لتفعيل خدمة مدفوع  بالمتجر يتطلب أن يكون لديك حساب لديهم")
S(c, "decides", H("bnpl-2"), "خدمة إمكان", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "إمكان مع زد باي",
  "لتفعيل خدمة إمكان ادفع لاحقا بالمتجر  في حال تفعيل زد باي في المتجر اتبع التالي:")
S(c, "decides", H("bnpl-2"), "خدمة أم آي إس باي", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "MIS pay",
  "تقدم لك أم آي إس باي خدمة الدفع بالأقساط وتقسيم قيمة مدفوعات العملاء على 3 دفعات شهرية بدون رسوم تأخير و بحد أدنى للطلب 200 ريال و حد أعلى 2000 ريال.")
S(c, "responsible", H("bnpl-2"), "خدمة تابي", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "تابي",
  "تقدم لك تابي حلولاً لتسهيل عمليات التسوق و الدفع من غير فوائد وتقسيم قيمة مدفوعاتهم على 4 دفعات شهرية وتقوم تابي بالدفع للمتاجر مباشرة عن طريق عمليات الشراء المدفوعة",
  note="States who pays the merchant for Tabby purchases.")
S(c, "responsible", H("bnpl-2"), "خدمة تمارا", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "تمارا",
  "إدخال اكواد الـ ( Merchant Key /API and Notification Token ) الخاصة بتمارا ستصلك من تمارا على البريد الإلكتروني بعد توقيع العقد")
S(c, "boundary", H("bnpl-2"), "خدمة أم آي إس باي", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "App ID and App Secret",
  "بعد الانتهاء من عملية التسجيل، ستظهر لك مفاتيح التفعيل (App ID and App Secret) ومن ثم بإمكانك ربط أم آي إس باي على متجركم في زد.")
S(c, "boundary", H("bnpl-2"), "خدمة تابي", struct(H("bnpl-2"), "خدمات التقسيط (لوحة التحكم الجديدة )"), "رمز وثيقة العمل الحر",
  "في حال لا يوجد لديك حساب في تابي وترغب في تفعيله ، قم بإدخال رمز وثيقة العمل الحر وسنقوم بطلب إنشاء الحساب لك تلقائيا من لوحة التحكم")
SNF(c, "reason", "A stated reason for placing instalments with outside providers", "help.zid.sa/bnpl-2/; zid.sa/en/solutions/payments/")

# ---------- ZD-C-014 Cash on delivery option ----------
c = "ZD-C-014"
S(c, "where", H("cod"), "intro", struct(H("cod"), "الغاء او تفعيل الدفع عند الاستلام ( لوحة التحكم الجديدة )"), "لوحة التحكم > اللوجستيات",
  "يمكنك تفعيل أو إلغاء الدفع عند الاستلام من خلال : لوحة التحكم > اللوجستيات")
S(c, "decides", H("cod"), "خطوات", struct(H("cod"), "الغاء او تفعيل الدفع عند الاستلام ( لوحة التحكم الجديدة )"), "شركة الشحن",
  "قم بالضغط على شركة الشحن التي ترغب بتفعيل او الغاء الدفع عند الاستلام فيها")
S(c, "decides", CHUNK, "compare-plans group Payments", ST[CHUNK], "Block Cash on Delivery", PL("Block Cash on Delivery"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Payments", ST[CHUNK], "Cash on Delivery", PL("Cash on Delivery"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "responsible", AR_TERMS, "خدمة الدفع عند التوصيل", ST[AR_TERMS], "خدمة الدفع عند التوصيل",
  "تقر بتحملك مسؤولية خدمات الدفع عند التوصيل بشكل كامل بصفتك مالك الحساب – وفي حالة رغبتك – بإلغاء هذه الخدمة فعليك أن تقوم بذلك بنفسك، نظراً لكونها خدمة مقدمة من طرف ثالث.")
S(c, "boundary", D("webhooks"), "Supported Conditions", struct(D("webhooks"), "Webhooks Overview"), "payment_method condition",
  "`payment_method` | String | Filters the event based on the payment method used. | `Cash On Delivery`, `Credit Card`, `Bank Transfer`")
S(c, "reason", AR_TERMS, "خدمة الدفع عند التوصيل", ST[AR_TERMS], "نظراً لكونها خدمة مقدمة من طرف ثالث",
  "فعليك أن تقوم بذلك بنفسك، نظراً لكونها خدمة مقدمة من طرف ثالث.", note="The stated reason why the merchant cancels the service himself.")

# ---------- ZD-C-015 COD collection through Zid shipping ----------
c = "ZD-C-015"
S(c, "where", AR_TERMS, "خدمة الدفع عند الاستلام (COD)", ST[AR_TERMS], "محفظة التاجر",
  "تقوم زد بتحصيل المبالغ من العملاء النهائيين وتحويل إجمالي المستحقات إلى محفظة التاجر مرتين كل شهر ميلادي، ويتم خصم رسوم وتكاليف زد المتعلقة بهذه الخدمة مباشرة فور الإيداع.",
  scope="الشحن المباشر (زد شب)")
S(c, "decides", CHUNK, "compare-plans group Shipping", ST[CHUNK], "Cash on Delivery Collection", PL("Cash on Delivery Collection"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", AR_TERMS, "خدمة الدفع عند الاستلام (COD)", ST[AR_TERMS], "رسوم الدفع عند الاستلام",
  "تستحق زد على خدمة الدفع عند الاستلام رسوم إضافية منفصلة يتم خصمها من إجمالي المبالغ المحصّلة قبل تحويلها إلى محفظة التاجر.")
S(c, "decides", "https://zid.sa/en/legal/domestic-shipping-terms/", "Domestic Shipping", "Domestic Shipping terms (zid.sa/en/legal/domestic-shipping-terms)", "COD Limit",
  "COD Limit: Up to $1000 (3750 SAR).")
S(c, "decides", H("faq-9"), "answer", struct(H("faq-9"), "FAQ: كيف يتم تحصيل أموال شحنات مبالغ الدفع عند الاستلام؟"), "زد شب",
  "في حين فعلت خدمة الدفع عن الاستلام ، سيتم تحصيل مبالغ الدفع عند الاستلام من قبل زد شب وخلال أسبوعين عمل سيتم تحويل المبالغ.",
  note="Sources differ on timing: this FAQ (last updated July 20, 2023) says within two working weeks; the Terms (August 2026) say twice each calendar month. Recorded as found.")
S(c, "responsible", AR_TERMS, "خدمة الدفع عند الاستلام (COD)", ST[AR_TERMS], "خدمة الدفع عند الاستلام (COD)",
  "هي خدمة تتيح للعميل النهائي الدفع عند استلام الشحنة بدلاً من الدفع المسبق، حيث تقوم زد بتحصيل المبلغ نيابة عن التاجر من العميل عند التسليم ثم تقوم بتحويلها إلى التاجر وفق الأحكام أدناه.")
S(c, "responsible", AR_TERMS, "خدمة الدفع عند الاستلام (COD)", ST[AR_TERMS], "لا يستحق أي مبالغ مباشرة",
  "التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء. وفي حال تحويل أي مبالغ من شركات الشحن إلى التاجر بشكل مباشر، يلتزم التاجر برد هذه المبالغ إلى شركة الشحن المعنية فوراً وإخطار زد بذلك.")
ASK(c, "responsible", "Which licensed entity or account holds COD amounts that Zid collects before they reach the merchant's wallet", "zid.sa/ar/legal/terms-conditions/ (زد شب, خدمة الدفع عند الاستلام (COD))")
SNF(c, "boundary", "An API endpoint, scope or webhook for COD collections or wallet transfers", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names COD collections.")
SNF(c, "reason", "A stated reason for Zid collecting COD amounts itself", "zid.sa/ar/legal/terms-conditions/ (زد شب); zid.sa/en/solutions/shipping/")

# ---------- ZD-C-016 Bank transfer option ----------
c = "ZD-C-016"
S(c, "where", H("bank-accounts"), "intro", struct(H("bank-accounts"), "الحسابات البنكية ( لوحة التحكم الجديدة )"), "صفحة الدفع",
  "من خلال هذه الخاصية يمكنك عرض بيانات حسابك البنكي في صفحة الدفع لتمكين العملاء من الدفع عن طريق التحويل البنكي، مع إمكانية التحكم الكامل في عرض أو إخفاء التفاصيل.")
S(c, "decides", EN_TERMS, "Bank Transfer Service", ST[EN_TERMS], "Bank Transfer Service",
  "When you subscribe to the Service and upon your request, we will activate the Bank Transfer service using your provided information.",
  note="The Arabic Terms (which prevail) repeat the cash-on-delivery sentence under خدمة التحويل البنكي; the English text is quoted here as found.")
S(c, "decides", CHUNK, "compare-plans group Payments", ST[CHUNK], "Bank Transfer Payment", PL("Bank Transfer Payment"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "responsible", AR_TERMS, "خدمة التحويل البنكي", ST[AR_TERMS], "خدمة التحويل البنكي",
  "تقر بتحملك المسؤولية الكاملة في إدارة خدمات التحويل البنكي بصفتك مالك الحساب ويجب عليك الحفاظ على معلومات الحساب البنكي الصحيحة لمتجرك.")
S(c, "responsible", AR_TERMS, "خدمة التحويل البنكي", ST[AR_TERMS], "شروط وأحكام البنك",
  "يقر التاجر بأنه موافقًا على شروط وأحكام البنك بمجرد استخدام خدمة التحويل البنكي في متجره.")
S(c, "boundary", D("webhooks"), "Supported Conditions", struct(D("webhooks"), "Webhooks Overview"), "`Bank Transfer`",
  "`payment_method` | String | Filters the event based on the payment method used. | `Cash On Delivery`, `Credit Card`, `Bank Transfer`")
SNF(c, "reason", "A stated reason for the bank transfer placement", "zid.sa/ar/legal/terms-conditions/ (خدمة التحويل البنكي); help.zid.sa/bank-accounts/")

# ---------- ZD-C-017 Zid Wallet ----------
c = "ZD-C-017"
S(c, "where", AR_TERMS, "محفظة زد", ST[AR_TERMS], "ما هي محفظة التاجر في زد؟",
  "هي محفظة تمكن التاجر من حفظ وإدارة المبالغ الخاصة به والخاصة بمتجره الإلكتروني في منصة زد، من خلال إضافة رصيد مالي والاستفادة منه في شراء المنتجات، أو الخدمات المعروضة في منصة زد، أو بتحويل الأموال إلى خارج المحفظة، وذلك وفقاً لهذه الشروط والأحكام (“المحفظة”) أو (“محفظة التاجر”).",
  quote="هي محفظة تمكن التاجر من حفظ وإدارة المبالغ الخاصة به والخاصة بمتجره الإلكتروني في منصة زد")
S(c, "where", H("zid-wallet"), "إضافة رصيد للمحفظة", struct(H("zid-wallet"), "محفظة زد ( لوحة التحكم الجديدة )"), "لوحة التحكم > المالية > المحفظة",
  "يمكنك إضافة رصيد من خلال الضغط على أيقونة إضافة رصيد للمحفظة من اعلى الصفحة او من خلال لوحة التحكم > المالية > المحفظة")
S(c, "where", H("zid-wallet"), "ملاحظة", struct(H("zid-wallet"), "محفظة زد ( لوحة التحكم الجديدة )"), "محفظة لكل متجر", "سيتم إنشاء محفظة لكل متجر.")
S(c, "decides", AR_TERMS, "محفظة زد", ST[AR_TERMS], "حد السحب",
  "يحق للتاجر إنشاء عملية سحب من المحفظة إلى حسابه البنكي بشرط ألا يتجاوز المبلغ عشرين ألف (20,000) ريال للعملية الواحدة.")
S(c, "decides", AR_TERMS, "محفظة زد", ST[AR_TERMS], "حد الشحن بالبطاقة",
  "في حال رغبة التاجر في شحن رصيده في محفظة زد من خلال (البطاقات الائتمانية / أبل باي)، يكون الحد الأقصى للتحويل هو خمسة آلاف (5,000) ريال.")
S(c, "decides", H("zid-wallet"), "ملاحظة", struct(H("zid-wallet"), "محفظة زد ( لوحة التحكم الجديدة )"), "توثيق الحساب",
  "يمكنك إضافة رصيد للمحفظة و يمكنك الشراء عن طريق المحفظة لكن لا يتاح لك سحب المبالغ حتى يتم إكمال عملية توثيق الحساب .")
S(c, "decides", AR_TERMS, "بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية", ST[AR_TERMS], "عملة المحفظة",
  "استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية، ويُستثنى من ذلك التجار في دول مجلس التعاون الخليجي (مملكة البحرين، دولة الكويت، سلطنة عُمان، دولة الإمارات العربية المتحدة، ودولة قطر)، حيث يُتاح لهم تفعيل، شحن، واستخدام رصيد المحفظة بالعملة المحلية لبلدهم.",
  quote="استخدام المحفظة متاح لجميع التجار خارج المملكة ومحددة بالريال السعودي كعملة أساسية، ويُستثنى من ذلك التجار في دول مجلس التعاون الخليجي",
  scope="merchants outside Saudi Arabia")
S(c, "decides", AR_TERMS, "بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية", ST[AR_TERMS], "عملات لا يمكن سحبها",
  "يقر التاجر بأنه لا يمكن سحب المبالغ المالية المتاحة في المحفظة للعملات التالية: (الريال العماني، الدرهم الإماراتي، الدينار الكويتي، والدينار البحريني).", scope="merchants outside Saudi Arabia")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Zid Wallet", PL("Zid Wallet", 0), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "responsible", AR_TERMS, "خصم الخدمات والمستحقات من المحفظة", ST[AR_TERMS], "الخصم الآلي",
  "يحق لزد الخصم الآلي والمباشر من أي مبالغ تُودع أو تُدخل في محفظة التاجر وذلك فور إيداعها لتسوية وسداد أي مستحقات، أو فروقات مالية، أو مبالغ مطالب بها لصالح زد كلما كان ذلك ضرورياً.")
S(c, "responsible", AR_TERMS, "محفظة زد", ST[AR_TERMS], "رقم الآيبان الخاص بالمحفظة",
  "يقر التاجر ويوافق بأنه لا يحق له استخدام رقم الآيبان الخاص بمحفظته لدى منصة زد في -على سبيل المثال لا الحصر- استقبال الحوالات الخارجية، أو خارج خدمات منصة زد، أو استخدامه لغير الأغراض المخصصة له.")
ASK(c, "responsible", "Which bank or licensed entity holds the funds behind the wallet's IBAN, and under which licence the wallet operates", "zid.sa/ar/legal/terms-conditions/ (محفظة زد); help.zid.sa/zid-wallet/")
S(c, "boundary", AR_TERMS, "توثيق الحساب لتفعيل المحفظة", ST[AR_TERMS], "معلومات مستندات اعرف عميلك",
  "إذا كان التاجر مفعلاً لخدمة (زد باي) فإنه يتم الاعتماد على معلومات مستندات اعرف عميلك التي تم توثيق حساب (زد باي) بناءً عليها كمعلومات معتمدة لدى المحفظة والتي ستظهر مباشرة في لوحة تحكم المحفظة.")
SNF(c, "reason", "A stated reason for the wallet's currency and withdrawal rules", "zid.sa/ar/legal/terms-conditions/ (محفظة زد); help.zid.sa/zid-wallet/")

# ---------- ZD-C-018 Wallet deduction ----------
c = "ZD-C-018"
S(c, "where", H("wallet-split"), "intro", struct(H("wallet-split"), "الاستقطاع للمحفظة ( لوحة التحكم الجديدة )"), "إدارة المحفظة",
  "يمكنك الوصول الى خاصية الاستقطاع للمحفظة من خلال اعلى الصفحة الرئيسية")
S(c, "decides", H("wallet-split"), "ملاحظة", struct(H("wallet-split"), "الاستقطاع للمحفظة ( لوحة التحكم الجديدة )"), "التجار السعوديين والكويتيين",
  "خاصية الاستقطاع للمحفظة متوفرة فقط للتجار السعوديين والكويتيين المفعلين لمدفوعات زد ( زد باي )", scope="Saudi and Kuwaiti merchants with Zid Pay")
S(c, "decides", H("wallet-split"), "طريقة الاستقطاع", struct(H("wallet-split"), "الاستقطاع للمحفظة ( لوحة التحكم الجديدة )"), "مبلغ ثابت; نسبة مئوية",
  "مبلغ ثابت : سيتم خصم مبلغ ثابت محدد من المدفوعات")
S(c, "responsible", AR_TERMS, "آلية استيفاء المبالغ في حالة عدم توافر رصيد بالمحفظة", ST[AR_TERMS], "رصيد التاجر في زد باي", "سحب المبالغ المستحقة من رصيد التاجر في زد باي.")
S(c, "boundary", AR_TERMS, "آلية إضافة وتحويل الأموال من وإلى المحفظة", ST[AR_TERMS], "الاستقطاع المباشر من زد باي", "الاستقطاع المباشر من زد باي.")
S(c, "reason", H("wallet-split"), "intro", struct(H("wallet-split"), "الاستقطاع للمحفظة ( لوحة التحكم الجديدة )"), "الاستقطاع للمحفظة",
  "يساعد ذلك في ضمان توفر رصيد دائم لتغطية المصاريف الأساسية مثل شراء بوليصات الشحن، دون الحاجة لانتظار تحويل الأرباح بالكامل إلى الحساب البنكي.")

# ---------- ZD-C-019 Customer wallet and cashback ----------
c = "ZD-C-019"
S(c, "where", H("customer-wallet"), "خطوات تفعيل محفظة العميل", struct(H("customer-wallet"), "محفظة العميل والكاش باك"), "التسويق ← برامج الولاء ← محفظة العميل",
  "من لوحة التحكم: التسويق ← برامج الولاء ← محفظة العميل")
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Marketing > Customer Wallets > Manager Customer Wallet", APIW("Merchant APIs > Marketing > Customer Wallets > Manager Customer Wallet"))
S(c, "decides", H("customer-wallet"), "ملاحظة", struct(H("customer-wallet"), "محفظة العميل والكاش باك"), "الباقة الاحترافية",
  "خاصية محفظة العميل والكاش باك متاحة في الباقة الاحترافية ، في حال كانت الباقة اقل يمكنك شرائها من خلال الاضافات > خاصية محفظة العميل", scope="الباقة الاحترافية; add-on for lower plans")
S(c, "decides", CHUNK, "compare-plans group Other", ST[CHUNK], "Zid Wallet (Other group)", PL("Zid Wallet", 1), scope=PLAN_SCOPE,
  note=PLAN_NOTE + " This line's description speaks of payment options for customers via the Zid digital wallet; it is a different line from the Basic Features 'Zid Wallet'.")
S(c, "responsible", H("customer-wallet"), "المؤشرات التشغيلية", struct(H("customer-wallet"), "محفظة العميل والكاش باك"), "إجمالي الأرصدة",
  "إجمالي الأرصدة: مجموع الأرصدة المتاحة حالياً في محافظ كل عملاء متجرك (التزام مستقبلي عليك)")
S(c, "boundary", D("credit-customer-wallet-42917653e0"), "Scopes", struct(D("credit-customer-wallet-42917653e0"), "Credit Customer Wallet"),
  EP("credit-customer-wallet-42917653e0"), SCOPEQ("credit-customer-wallet-42917653e0"))
SNF(c, "reason", "A stated reason for the customer wallet's placement", "help.zid.sa/customer-wallet/; docs.zid.sa Customer Wallets group")

# ---------- ZD-C-020 Zid subscriptions and fees ----------
c = "ZD-C-020"
S(c, "where", H("subscription"), "intro", struct(H("subscription"), "إدارة الاشتراك ( لوحة التحكم الجديدة )"), "إدارة الأشتراك",
  "يمكنك الوصول الى إدارة الاشتراك من خلال : الضغط على شعار المتجر اعلى الصفحة > إدارة الأشتراك")
S(c, "decides", PRICING, "Compare Plans", ST[PRICING], "Starter; Rise; Growth; Pro", "StarterFree forever Rise99 SAR/month Growth299 SAR/month ProLet's talk")
S(c, "decides", AR_TERMS, "الاشتراكات", ST[AR_TERMS], "عملة الرسوم", "جميع الرسوم تكون بالريال السعودي أو بعملة التاجر المحلية ويجب أن تكون جميع المدفوعات بالعملة المحلية.")
S(c, "decides", AR_TERMS, "الاشتراكات", ST[AR_TERMS], "تغيير الأسعار",
  "يجوز لنا تغيير خطط الاشتراك وأسعار الرسوم والخدمات التي نقدمها من وقت لآخر؛ ومع ذلك، سنقوم بإشعارك بأي تغييرات في الأسعار أو تغييرات في خطط الاشتراك أو الخدمات قبل تطبيقها بـ(7) سبعة أيام على الأقل.")
S(c, "responsible", AR_TERMS, "الاشتراكات", ST[AR_TERMS], "ضريبة القيمة المضافة", "أنت مسؤول عن سداد ودفع كافة الرسوم الضريبية، بما في ذلك ضريبة القيمة المضافة.")
S(c, "responsible", AR_TERMS, "الاشتراكات", ST[AR_TERMS], "لغة الفاتورة",
  "الأصل أن تُقدم الفاتورة باللغة العربية ويمكن كذلك تقديمها باللغة العربية والإنجليزية معًا، وعلى أن تتضمن الفاتورة تاريخ إصدارها، ومعلوماتنا وبياناتنا الرسمية، ونوع الخدمة ووصفها وسعرها وكميتها.")
S(c, "boundary", PRICING, "plan card Rise (CTA)", ST[PRICING], "package_code=rise", "https://dashboard.zid.sa/en/register?package_code=rise")
SNF(c, "reason", "A stated reason for the plan structure", "zid.sa/en/pricing/; zid.sa/ar/legal/terms-conditions/ (الاشتراكات); help.zid.sa/subscription/")

# ---------- ZD-C-021 Purchases from Zid and payment processing ----------
c = "ZD-C-021"
S(c, "where", AR_TERMS, "المدفوعات والمشتريات", ST[AR_TERMS], "المدفوعات والمشتريات",
  "أنت تدرك أن استخدام الخدمات قد يؤدي إلى عمليات الشراء التي تقوم بها للخدمات أو السلع التي تتلقاها (“عملية الشراء”).")
S(c, "decides", AR_TERMS, "المدفوعات والمشتريات", ST[AR_TERMS], "تبديل موردي معالجة الدفع",
  "نحتفظ بالحق في تبديل موردي معالجة الدفع أو استخدام البائعين البديلين أو الاحتياطيين وفقًا لتقديرنا.", note="States Zid may switch to alternative or backup processors.")
S(c, "responsible", AR_TERMS, "المدفوعات والمشتريات", ST[AR_TERMS], "معالج دفع تابع لجهة خارجية",
  "نحن نوفر خدمات معالجة الدفع بواسطة معالج دفع تابع لجهة خارجية، في حين إكمال عملية شراء من خلال الخدمة فإنك توافق على الالتزام ببنود وشروط معالجي الدفع الخارجيين، والتي قد يتم تعديلها من وقت لآخر.")
SNF(c, "responsible", "The name of the third-party payment processor for purchases from Zid", "zid.sa/ar/legal/terms-conditions/; zid.sa/en/legal/terms-conditions/; help.zid.sa/subscription/")
S(c, "boundary", AR_TERMS, "المدفوعات والمشتريات", ST[AR_TERMS], "أطراف ثالثة",
  "من خلال تقديم هذه المعلومات، أو أي معلومات أخرى ذات صلة نراها ضرورية لعملية الشراء، فإنك تمنحنا الحق في تقديم المعلومات إلى أطراف ثالثة لأغراض تسهيل إتمام عمليات الشراء.")
SNF(c, "reason", "A stated reason for using an outside processor", "zid.sa/ar/legal/terms-conditions/ (المدفوعات والمشتريات)")

# ---------- ZD-C-022 App Market subscriptions and partner payouts ----------
c = "ZD-C-022"
S(c, "where", PAYOUTS, "Tracking payouts in the Partner Dashboard", ST[PAYOUTS], "Payments → Payouts", "Everything about payouts lives under Payments → Payouts in the Partner Dashboard.")
S(c, "where", D("app-management-3013257f0"), "Docs", struct(D("app-management-3013257f0"), "App Management"), "App Management > Events",
  "Subscription app events notify applications about important subscription activities, such as installation, authorization, renewals, and expiration.")
S(c, "decides", D("zid-app-activation-oauth-policy-2422816m0"), "callout", struct(D("zid-app-activation-oauth-policy-2422816m0"), "Zid App Activation & OAuth Policy"), "app-plan payment",
  "Any required app-plan payment is completed through Zid before activation becomes available.")
S(c, "decides", D("zid-app-activation-oauth-policy-2422816m0"), "6. External account and onboarding requirements", struct(D("zid-app-activation-oauth-policy-2422816m0"), "Zid App Activation & OAuth Policy"),
  "applicable Zid plans", "For standard apps, keep app charges within the applicable Zid plans; account linking must not introduce another partner-side payment.")
S(c, "decides", PAYOUTS, "When you earn and how your share is calculated", ST[PAYOUTS], "Partner rate",
  "Your partner rate is set in the agreement you sign with Zid before publishing, and it may change subject to Zid's approval.")
S(c, "responsible", PAYOUTS, "When you earn and how your share is calculated", ST[PAYOUTS], "monthly payouts",
  "The merchant pays Zid, the transaction joins the next payout cycle, and Zid settles your payout once the invoicing step is complete.")
S(c, "responsible", AR_TERMS, "سوق تطبيقات زد", ST[AR_TERMS], "تحصيل زد لرسوم تفعيل الخدمة",
  "يقر التاجر ويفهم أنه في حال تحصيل زد لرسوم تفعيل الخدمة من التاجر ، سيكون هذا التحصيل وفق ما يتفق عليه مع الشريك من خلال الاتفاقيات والوثائق بينهما، ولا تكون زد مسؤولة عن أية مطالبات، أو الاسترجاعات ناقصة، أو تغيير رسوم الخدمة حيث أن زد مجرد أداة تقنية يستخدمها التاجر والشريك.",
  quote="يقر التاجر ويفهم أنه في حال تحصيل زد لرسوم تفعيل الخدمة من التاجر ، سيكون هذا التحصيل وفق ما يتفق عليه مع الشريك من خلال الاتفاقيات والوثائق بينهما")
S(c, "responsible", PAYOUTS, "The invoice: what it must include", ST[PAYOUTS], "Withholding tax",
  "Non-Saudi bank account: in USD, deducting withholding tax (WHT): 15% for apps and 5% for themes.")
S(c, "boundary", D("apis-6456258f0"), "Docs", struct(D("apis-6456258f0"), "App Management APIs"), "Subscription Details",
  "This endpoint enables app partners to fetch details about a merchant's app subscription, including plan, status, and billing information.")
S(c, "boundary", D("apis-6456258f0"), "Docs", struct(D("apis-6456258f0"), "App Management APIs"), "Update Usage-Based Charges",
  "This endpoint allows app partners to update the outstanding balance for their app's usage-based plan, ensuring flexible billing adjustments to align with merchants' pay-as-you-go consumption.")
S(c, "boundary", D("events-878234m0"), "App Subscription Events", struct(D("events-878234m0"), "App Management Events"), "app.market.subscription.active",
  "`app.market.subscription.active` | Send notification on successful activation of subscription.")
SNF(c, "reason", "A stated reason for Zid collecting app payments and paying partners", "docs.zid.sa/zid-app-activation-oauth-policy-2422816m0.md; zid.sa/en/partners/developers/blog/partner-payouts/; help-partner.zid.sa payout articles")

# ---------- ZD-C-023 Zid Financing ----------
c = "ZD-C-023"
S(c, "where", AR_TERMS, "تمويل زد: التعريفات", ST[AR_TERMS], "تمويل زد (definition)",
  "تمويل زد: هي خدمة إلكترونية تقدمها زد، تتيح للتجار الاستفادة من عروض التمويل لجهة التمويل، وتتيح لجهة التمويل استلام دفعات السداد عن طريق الاستقطاع من عمليات بيع التاجر المنفذة على منصة زد لحلول الدفع (“زد باي”) خلال مدة اشتراكه في هذه الخدمة.",
  quote="تمويل زد: هي خدمة إلكترونية تقدمها زد، تتيح للتجار الاستفادة من عروض التمويل لجهة التمويل، وتتيح لجهة التمويل استلام دفعات السداد عن طريق الاستقطاع من عمليات بيع التاجر المنفذة على منصة زد لحلول الدفع (“زد باي”)")
S(c, "decides", H("about-zid-financing"), "متطلبات التقديم", struct(H("about-zid-financing"), "عن تمويل زد ( لوحة التحكم الجديدة )"), "الدولة", "الدولة : متاح لتجار المملكة العربية السعودية فقط.", scope="المملكة العربية السعودية")
S(c, "decides", H("about-zid-financing"), "متطلبات التقديم", struct(H("about-zid-financing"), "عن تمويل زد ( لوحة التحكم الجديدة )"), "بوابة الدفع", "بوابة الدفع: تفعيل واعتماد زد باي.")
S(c, "decides", H("about-zid-financing"), "ملاحظه", struct(H("about-zid-financing"), "عن تمويل زد ( لوحة التحكم الجديدة )"), "الباقات", "تمويل زد متاح لجميع الباقات ماعدا لايت")
S(c, "decides", AR_TERMS, "تمويل زد: حدود المسؤولية", ST[AR_TERMS], "تقدير جهة التمويل",
  "بناء على الفقرة (1) ، فإن قبول أو رفض تقديم خدمة التمويل، وكذلك تحديد عرض السعر للتمويل، خاضع لتقدير جهة التمويل باستقلال عن زد")
S(c, "decides", AR_TERMS, "تمويل زد: أحكام وشروط عامة إضافية", ST[AR_TERMS], "إلغاء زد باي",
  "بعد اشتراك التاجر في الخدمة، فإنه لن يتمكن من إلغاء اشتراكه في زد باي، أو التحويل إلى قناة دفع أخرى إلى حين استكمال كامل التزاماته بالسداد.")
S(c, "responsible", AR_TERMS, "تمويل زد: حدود المسؤولية", ST[AR_TERMS], "جهة التمويل",
  "يفهم التاجر ويوافق على أن جهة التمويل هي المقدم لخدمة التمويل وأن علاقته بجهة التمويل مستقلة عن علاقته بزد، وأن زد مجرد مقدم للحلول الالكترونية للتمويل بحسب التعريف الوارد في هذه الشروط والأحكام.")
S(c, "responsible", AR_TERMS, "تمويل زد: حدود المسؤولية", ST[AR_TERMS], "تعذر الاستقطاع",
  "في حال لم تتمكن زد باي من استقطاع التزامات السداد أو حدّها الشهري الأدنى بحسب اتفاق التاجر وجهة التمويل، لأيّ سبب، اختياري أو قهري، عائد إليها أو إلى التاجر،  فإن التاجر يفهم أن ذلك لا يعفيه من التزامه بالسداد في مقابل جهة التمويل، وأنه عليه استكمال التزاماته عن طريق التحويل البنكي، أو أي طريقة أخرى يتفق التاجر وجهة التمويل عليها.",
  quote="في حال لم تتمكن زد باي من استقطاع التزامات السداد أو حدّها الشهري الأدنى بحسب اتفاق التاجر وجهة التمويل، لأيّ سبب، اختياري أو قهري، عائد إليها أو إلى التاجر")
SNF(c, "responsible", "The name and licence of the financing entity (جهة التمويل)", "zid.sa/ar/legal/terms-conditions/ (تمويل زد); help.zid.sa/about-zid-financing/; help.zid.sa/zidfinance-requirements/; help.zid.sa/defaulting/; zid.sa/en/solutions/financing/",
    why="The pages in the route were read; they speak of جهة التمويل and شريك التمويل without naming it.")
S(c, "boundary", AR_TERMS, "تمويل زد: أحكام وشروط عامة إضافية", ST[AR_TERMS], "مشاركة المعلومات", "لأغراض تقديم الخدمة، ستشارك زد كافة المعلومات المتعلقة بمبيعات التاجر مع جهة التمويل.")
S(c, "boundary", H("defaulting"), "التعثر عن السداد", struct(H("defaulting"), "التعثر عن السداد"), "الحد الأدنى للسداد",
  "الحد الأدنى للسداد بناء على عقد التمويل الذي تم توقيعه مع شريك التمويل: هو الحد الأدنى لسداد مبلغ التمويل خلال الشهر")
SNF(c, "reason", "A stated reason for collecting repayments through Zid Pay", "zid.sa/ar/legal/terms-conditions/ (تمويل زد); help.zid.sa/about-zid-financing/")

# ---------- ZD-C-024 Mazeed collections and dues ----------
c = "ZD-C-024"
S(c, "where", H("mazeed-settlement-2"), "intro", struct(H("mazeed-settlement-2"), "المستحقات المالية لمزيد ( لوحة التحكم الجديدة )"), "لوحة التحكم > منصات البيع > مزيد",
  "للوصول الى المستحقات المالية الخاصة بمزيد من خلال : لوحة التحكم > منصات البيع > مزيد")
S(c, "where", H("faq-28"), "answer", struct(H("faq-28"), "FAQ: هل بوابة الدفع في مزيد مماثلة لبوابة الدفع في متجري؟"), "بوابة الدفع في مزيد", "لا، بوابة الدفع في مزيد مختلفة وخاصة في التطبيق فقط.")
S(c, "decides", AR_TERMS, "مزيد: الأحكام المالية", ST[AR_TERMS], "تحويل المبالغ المستحقة",
  "تحول شركة زد المبالغ المستحقة في يوم  (30) من كل شهر ميلادي إلى حساب التاجر البنكي بشرط أن يكون قد مر على العمليات الشرائية 7 أيام كحد أدنى من تاريخ الشراء، والا تقل المبالغ المحولة عن 500 ريال كحد أدنى.")
S(c, "decides", AR_TERMS, "مزيد: الأحكام المالية", ST[AR_TERMS], "النسبة المقتطعة", "تحدد شركة زد النسبة المقتطعة من التاجر على كل عملية شرائية بناءً على تصنيف قطاع المتجر في منصة مزيد.")
S(c, "decides", H("mazeed-settlement-2"), "مثال لعملية التحصيل", struct(H("mazeed-settlement-2"), "المستحقات المالية لمزيد ( لوحة التحكم الجديدة )"), "كل يوم ثلاثاء",
  "التحصيلات مع مزيد تتم بشكل إسبوعي كل يوم ثلاثاء بدون حد ادنى أو قيود على الطلب",
  note="Sources differ: this article says weekly on Tuesdays with no minimum; the Mazeed collections article and the Terms say monthly with a 500 SAR minimum. Recorded as found.")
S(c, "decides", H("mazeed-financial-collection"), "مثال لعملية التحصيل", struct(H("mazeed-financial-collection"), "تحصيلات مزيد ( لوحة التحكم الجديدة )"), "بشكل شهري",
  "التحصيلات مع مزيد تتم بشكل شهري بشرط أن تكون المبيعات 500 ريال فأكثر")
S(c, "responsible", AR_TERMS, "مزيد: مسؤوليات وحقوق زد", ST[AR_TERMS], "احتجاز الأموال",
  "يحق لشركة زد احتجاز بعض أو كل الأموال إذا كانت العمليات مشتبه بها في -على سبيل المثال لا الحصر- عمليات الاحتيال، والاختلاس، وطلب مستندات وأدلة داعمة للتحقق من شرعية العمليات",
  note="The clause continues with returning amounts to their sources, closing the account and informing the authorities.")
S(c, "responsible", AR_TERMS, "مزيد: إلغاء ربط الحساب", ST[AR_TERMS], "احتجاز الأموال عند الإلغاء",
  "في حال رغبة التاجر في إلغاء حسابه في مزيد فيحق لشركة زد احتجاز الأموال ليتم تسوية العمليات المعلقة")
S(c, "boundary", AR_TERMS, "مزيد: الأحكام المالية", ST[AR_TERMS], "فاتورة بالمبالغ المستحقة", "يحصر التاجر العمليات الشرائية ويُصدر فاتورة بالمبالغ المستحقة في يوم (15) و يوم (30) من كل شهر ميلادي.")
S(c, "boundary", H("mazeed-settlement-2"), "أحدث العمليات المالية", struct(H("mazeed-settlement-2"), "المستحقات المالية لمزيد ( لوحة التحكم الجديدة )"), "فواتير ضريبية B2B",
  "المرفقات : الفواتير، وهي فواتير ضريبية B2B.")
S(c, "reason", AR_TERMS, "مزيد: الاسترداد", ST[AR_TERMS], "عدم تحديث المخزون",
  "وتهدف هذه السياسة إلى تحقيق التوازن بين حقوق الأطراف المعنية وتجنب الإضرار بمصالح البائع أو العميل، مع تعزيز الالتزام بتحديث المخزون لضمان تقديم تجربة تجارية موثوقة وفعالة.",
  note="Stated reason for sharing refund costs between the merchant and Mazeed.")

# ---------- ZD-C-025 Zid Agent ----------
c = "ZD-C-025"
S(c, "where", AR_TERMS, "خدمة وكيل زد (Zid Agent)", ST[AR_TERMS], "المحفظة الرقمية الخاصة بوكيل زد",
  "تتيح الخدمة للتاجر شحن رصيد المحفظة الرقمية الخاصة بوكيل زد للاستفادة من المزايا المختلفة")
S(c, "decides", AR_TERMS, "خدمة وكيل زد (Zid Agent)", ST[AR_TERMS], "متجر نشط", "للاستفادة من خدمات \"وكيل زد (Zid Agent)\" يجب أن يمتلك التاجر متجرًا نشطًا ومفعلاً على منصة زد.")
S(c, "decides", AR_TERMS, "أحكام استرجاع رصيد وكيل زد (Zid Agent)", ST[AR_TERMS], "النافذة الزمنية للاسترجاع",
  "النافذة الزمنية للاسترجاع: تكون المدة المسموحة لطلب استرجاع مبلغ الشحن هي ساعتان (٢) فقط تبدأ من وقت إتمام عملية الشحن.")
S(c, "responsible", AR_TERMS, "خدمة وكيل زد (Zid Agent)", ST[AR_TERMS], "شركاء ومزودو التقنية", "تملك منصة زد الحق في توفير الخدمة من خلالها مباشرة أو عبر شركائها ومزودي التقنية الخارجيين.")
S(c, "boundary", EN_PRIV, "AI Data Processing", ST[EN_PRIV], "Google Cloud Vertex AI",
  "Zid Agent uses Google Cloud Vertex AI as a data processor to power AI-assisted features including product research, store optimization, campaign management, and conversational assistance.")
SNF(c, "reason", "A stated reason for the Zid Agent wallet and its refund window", "zid.sa/ar/legal/terms-conditions/ (خدمة وكيل زد)")

# ---------- ZD-C-026 Value added services ----------
c = "ZD-C-026"
S(c, "where", AR_TERMS, "خدمة المميزات الإضافية VAS: خطوات الاسترجاع", ST[AR_TERMS], "طلب استرداد باقة جديدة/حالية",
  "يرفع التاجر طلب الاسترجاع من خلال الذهاب إلى لوحة التحكم > فتح تذكرة جديدة > اختيار فئة التذكرة “طلبات على المتجر” > اختيار الفئة الفرعية “طلب استرداد باقة جديدة/حالية” > وصف الطلب وإرفاق نسخة من شهادة الآيبان.",
  note="Where VAS refunds are requested; the Terms name no dashboard section for VAS itself.")
S(c, "decides", AR_TERMS, "خدمة المميزات الإضافية VAS", ST[AR_TERMS], "متجر مفعل", "للاستفادة من خدمة المميزات الإضافية يجب أن يكون لديك متجرًا مفعلاً على منصة زد.")
S(c, "decides", AR_TERMS, "خدمة المميزات الإضافية VAS", ST[AR_TERMS], "الأسعار", "تملك منصة زد الحق في مراجعة وتحديث أسعار خدمة المميزات الإضافية في أي وقت ولأي سبب من الأسباب بعد إشعار التاجر بذلك.")
S(c, "responsible", AR_TERMS, "خدمة المميزات الإضافية VAS", ST[AR_TERMS], "شركاء", "تملك منصة زد الحق في توفير الخدمة من خلالها أو من خلال شركائها.")
SNF(c, "boundary", "An API endpoint, scope or webhook for value added services", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names value added services.")
SNF(c, "reason", "A stated reason for the VAS placement", "zid.sa/ar/legal/terms-conditions/ (خدمة المميزات الإضافية VAS)")

# ---------- ZD-C-028 Order payment status ----------
c = "ZD-C-028"
S(c, "where", D("webhooks"), "Order Events", struct(D("webhooks"), "Webhooks Overview"), "order.payment_status.update",
  "order.payment_status.update | Triggered when an order's payment status changes to `paid` or `unpaid`.")
S(c, "decides", CHUNK, "compare-plans group Payments", ST[CHUNK], "Payment Status", PL("Payment Status"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Payments", ST[CHUNK], "Bulk Payment Status Update", PL("Bulk Payment Status Update"), scope=PLAN_SCOPE, note=PLAN_NOTE)
GEN(c)
S(c, "boundary", D("webhooks"), "Order Events", struct(D("webhooks"), "Webhooks Overview"), "order.payment_status.update",
  "Note that `unpaid` includes `pending`, `refunded`, and `voided` statuses.")
SNF(c, "reason", "A stated reason for the payment-status placement", "docs.zid.sa/webhooks.md; zid.sa pricing compare-plans data")
