# Statements and gaps from the help-centre articles and the Zid Voice page read after the first pass.
# Each block first removes the gaps these pages now answer, then adds what the pages state.
import stlib
from stlib import S, OBS, SNF, H, struct, PL, CHUNK, ST, PLAN_SCOPE, PLAN_NOTE

def drop(c, p, kinds=("page not read",)):
    n = len(stlib.GAPS)
    stlib.GAPS[:] = [g for g in stlib.GAPS if not (g["c"] == c and g["p"] == p and g["kind"] in kinds)]
    assert len(stlib.GAPS) < n, ("nothing to drop", c, p, kinds)

def HT(key, title): return struct(H(key), title)
NO_REASON = "The articles in the route were read in this run; they describe the feature and how to use it, but state no reason for where it sits, who sets it or who is responsible for it."
VOICE = "https://zid.sa/en/solutions/zid-voice/"
VOICE_ST = "product page Zid Voice (zid.sa/en/solutions/zid-voice)"

# ---------- ZD-C-054 Credit notes ----------
c = "ZD-C-054"; k = "credit-debit-notifications"; t = HT(k, "إشعارات الدائن والمدين ( لوحة التحكم الجديدة )")
drop(c, "reason"); drop(c, "decides", ("observation needed",))
S(c, "decides", H(k), "عرض ملخص الطلب", t, "اشعارات الدائن والمدين",
  "عند القيام بأي تعديل على الطلب يتم إصدار وإرسال إشعارات فواتير سواء إلغاء الطلب أو تعديل الطلب وتسمى اشعارات الدائن والمدين.")
S(c, "decides", H(k), "ملاحظة", t, "إعدادات الضريبة المضافة", "لن يتم إرسالها إلى عملاء المتجر المفعل لإعدادات الضريبة المضافة.")
SNF(c, "decides", "Which plans include credit and debit notes",
    "help.zid.sa/credit-debit-notifications/; zid.sa/en/pricing/ (compare-plans data, which has no credit-note line)")
S(c, "reason", H(k), "إشعار المدين", t, "هيئة الزكاة والضريبة والجمارك",
  "الفاتورة الأصلية تبقى كما هي من دون أي تغيير و حسب اشتراطات ولوائح هيئة الزكاة والضريبة والجمارك",
  note="The stated basis for leaving the original invoice unchanged when an order is modified or cancelled.")

# ---------- ZD-C-080 Orders ----------
c = "ZD-C-080"; k = "change-order-status"; t = HT(k, "حالات الطلب وتغييرها (لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "decides", H(k), "جاري التوصيل", t, "جاري التوصيل",
  "تم استلام الطلب من قبل شركة الشحن وسيتم توصيله للعميل، وشركة الشحن هي من تقوم بتغيير حالة الطلب إلى جاري التوصيل.")
S(c, "boundary", H(k), "جاهز", t, "جاهز", "وتصل أيضاً رسالة لشركات الشحن المربوطة بنظام زد بأن الطلب جاهز للاستلام من موقع المخزن.")
SNF(c, "reason", "A stated reason for where order statuses are set and by whom",
    "help.zid.sa/change-order-status/; help.zid.sa/credit-debit-notifications/; docs.zid.sa Orders pages", why=NO_REASON)

# ---------- ZD-C-081 Reverse orders and returns ----------
c = "ZD-C-081"; k1, k2 = "return-order", "partial-return"
t1 = HT(k1, "استرجاع الطلبات (لوحة التحكم الجديدة )"); t2 = HT(k2, "استرجاع جزئي للطلبات ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "where", H(k1), "استرجاع يدوي", t1, "استرجاع يدوي", "المقصود به تصدير بوليصة الرجيع من شركة الشحن التي تتعامل معها وليس من نظام زد.")
S(c, "decides", H(k2), "إصدار بوليصة الإرجاع تلقائيًا", t2, "بوليصة الإرجاع", "سيتم خصم تكلفة البوليصة من محفظة زد، ويمكن استرجاع حتى 7 صناديق من إجمالي الطلب.")
S(c, "boundary", H(k2), "ملاحظة", t2, "طرق الاسترداد", "طرق الاسترداد تعتمد على طريقة الدفع الأساسية للطلب.")
S(c, "boundary", H(k1), "ملاحظة", t1, "سمسا; أرامكس", "الشركات الحالية اللتي تدعم الاسترجاع سمسا ( تسليم الفرع ) أرامكس ( تسليم الفرع )",
  note="The carriers named as supporting return labels.")
SNF(c, "reason", "A stated reason for where returns are placed and who issues the return label",
    "help.zid.sa/return-order/; help.zid.sa/partial-return/", why=NO_REASON)

# ---------- ZD-C-082 Abandoned carts ----------
c = "ZD-C-082"; k1, k2 = "abandonment-cart", "zid-reminder"
t1 = HT(k1, "السلات المتروكة ( لوحة التحكم الجديدة )"); t2 = HT(k2, "تنبيهات زد ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "decides", H(k1), "تفاصيل السلات المتروكة", t1, "الباقات المجانية", "هذي الميزة عير متوفرة في الباقات المجانية", scope="الباقات المجانية")
S(c, "decides", H(k1), "تحليلات السلات المتروكة", t1, "الباقة الاحترافية; باقة الأعمال الكبيرة",
  "بعض المؤشرات متوفرة للباقة الاحترافية و باقة الأعمال الكبيرة فقط .", scope="الباقة الاحترافية; باقة الأعمال الكبيرة")
S(c, "decides", H(k2), "تفعيل تنبيهات زد", t2, "تنبيهات زد", "خاصية تنبيهات زد مفعلة تلقائيًا لمساعدتك في استهداف السلات المتروكة.")
S(c, "boundary", H(k2), "تخصيص الرسالة", t2, "رقم زد", "رسائل واتساب الخاصة بتنبيهات زد تُرسل بقالب ثابت من رقم زد.")
SNF(c, "reason", "A stated reason for where abandoned carts and their reminders sit",
    "help.zid.sa/abandonment-cart/; help.zid.sa/zid-reminder/", why=NO_REASON)

# ---------- ZD-C-083 Products ----------
c = "ZD-C-083"
drop(c, "reason")
SNF(c, "reason", "A stated reason for this concern's placement",
    "help.zid.sa/product-without-options/ (category المنتجات); docs.zid.sa Products pages", why=NO_REASON)

# ---------- ZD-C-084 Product categories ----------
c = "ZD-C-084"; k = "create-category"; t = HT(k, "إضافة تصنيف ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "decides", H(k), "تحسين محركات البحث", t, "تحسين محركات البحث", "هذه الميزة غير متاحة في الباقة المجانية", scope="الباقة المجانية",
  note="Said of the search-engine fields of a category.")
SNF(c, "reason", "A stated reason for this concern's placement", "help.zid.sa/create-category/; help.zid.sa/organize-category/", why=NO_REASON)

# ---------- ZD-C-085 Inventory and stock ----------
c = "ZD-C-085"; k1, k2 = "shipping-adress", "withdrawal-priority"
t1 = HT(k1, "عناوين المخزون ( لوحة التحكم الجديدة )"); t2 = HT(k2, "أولوية السحب من المخزون ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "decides", H(k1), "ملاحظة", t1, "عدد المخازن",
  "الباقة الاحترافية متاح بها إضافة و تفعيل 5 مخازن وفي حال تم تفعيل زد كاشير يتاح لك زيادة مخزن واحد لكل جهاز.", scope="الباقة الاحترافية")
S(c, "decides", H(k1), "ملاحظة", t1, "عدد المخازن", "باقة الأعمال الكبيرة عدد المخازن لا محدود.", scope="باقة الأعمال الكبيرة")
S(c, "decides", H(k2), "ملاحظة", t2, "أولوية السحب من المخزون", "هذي الميزة غير متوفرة في الباقات المجانية", scope="الباقات المجانية")
S(c, "boundary", H(k1), "إنشاء عناوين المخزون", t1, "جاهز", "يمكنك أيضاً إضافة أكثر من موقع للمخزن و شركة الشحن ستتجه للمخزن المحدد عند تحويل الطلب لـ ” جاهز ”")
SNF(c, "reason", "A stated reason for this concern's placement", "help.zid.sa/shipping-adress/; help.zid.sa/withdrawal-priority/", why=NO_REASON)

# ---------- ZD-C-086 Product reviews and questions ----------
c = "ZD-C-086"; k1 = "customer-reviews"; k2 = "customer-questions"
t1 = HT(k1, "تقييمات العملاء ( لوحة التحكم الجديدة )"); t2 = HT(k2, "أسئلة العملاء ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "where", H(k2), "intro", t2, "الاسئلة", "لوحة التحكم > العملاء > الاسئلة")
S(c, "decides", H(k1), "تفعيل التقييمات في المتجر", t1, "مكتمل",
  "بعد تفعيل الخاصية و تحويل طلب العميل إلى مكتمل سيتمكن من إضافة تقييمه بشكل مباشر في صفحة المنتج")
S(c, "reason", H(k1), "ملاحظة", t1, "بعد كل طلب منفصل",
  "يمكن للعميل النهائي تقييم المنتج بعد كل طلب منفصل حتي يستطيع تقيم تجربته للمنتج بكل مصداقية في كل مرة",
  note="The stated reason for allowing a review after each separate order.")

# ---------- ZD-C-087 Product availability notifications ----------
c = "ZD-C-087"; k = "stock-notifications"; t = HT(k, "إشعارات توفر المخزون (تذكيرات الشراء)")
drop(c, "reason")
S(c, "where", H(k), "الوصول لها", t, "إشعارات المخزون", "عن طريق لوحة تحكم زد، انتقل إلى: العملاء ← إشعارات المخزون")
S(c, "boundary", H(k), "intro", t, "البريد الإلكتروني أو واتساب",
  "إشعارات المخزون هي ميزة تتيح لعملائك التسجيل لتلقي إشعار تلقائي فور توفر منتج نفدت كميته، سواء عبر البريد الإلكتروني أو واتساب")
SNF(c, "reason", "A stated reason for this concern's placement", "help.zid.sa/stock-notifications/", why=NO_REASON)

# ---------- ZD-C-088 Coupons and discounts ----------
c = "ZD-C-088"; k = "discounts"; t = HT(k, "خصومات البنك (لوحة التحكم الجديدة)")
drop(c, "reason")
S(c, "decides", H(k), "intro", t, "خصومات البنك",
  "خصومات البنك ميزة تمكنك من إنشاء خصومات مخصصة مرتبطة ببنوك أو علامات بطاقات محددة، بناءً على العروض والاتفاقيات التي يتم التفاوض عليها مباشرة مع البنوك.")
SNF(c, "reason", "A stated reason for this concern's placement", "help.zid.sa/create-discount/; help.zid.sa/discounts/", why=NO_REASON)

# ---------- ZD-C-089 Bundle offers ----------
c = "ZD-C-089"; k1, k2 = "add-dynamic-product", "bundle_offer"
t1 = HT(k1, "إنشاء حزمة مرنة ( لوحة التحكم الجديدة )"); t2 = HT(k2, "الحزم التسويقية")
drop(c, "reason")
S(c, "decides", H(k1), "ملاحظة", t1, "باقة النمو", "الخاصية متاحه لباقة النمو", scope="باقة النمو", note="Said of the flexible bundle (حزمة مرنة).")
S(c, "decides", H(k2), "معلومة", t2, "عدد القطع", "الحزم التسويقية في زد تعتمد على كمية المنتجات (عدد القطع) وليس على قيمة السلة.")
S(c, "reason", H(k2), "intro", t2, "ليست خصومات عادية",
  "الحزم التسويقية ليست خصومات عادية، هي استراتيجية لرفع متوسط قيمة الطلب (AOV) دون تآكل هامش الربح، لأن العميل يشتري أكثر ليحصل على الميزة.",
  note="The stated reason why bundle offers sit apart from ordinary discounts.")

# ---------- ZD-C-090 Loyalty program ----------
c = "ZD-C-090"; k = "loyalty-program"; t = HT(k, "برنامج الولاء ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "decides", H(k), "ملاحظة", t, "الباقة الاحترافية", "نقاط الولاء متاحة للباقة الاحترافية فقط", scope="الباقة الاحترافية")
S(c, "decides", H(k), "ملاحظة", t, "الإضافات", "يمكنك شراء نقاط الولاء من خلال  الإضافات")
SNF(c, "reason", "A stated reason for this concern's placement", "help.zid.sa/loyalty-program/", why=NO_REASON)

# ---------- ZD-C-091 Customers ----------
c = "ZD-C-091"; k = "customer-list"; t = HT(k, "قائمة العملاء (لوحة التحكم الجديدة )")
drop(c, "reason")
drop(c, "responsible", ("stated only in general terms",))  # the privacy policy places responsibility for customers' data (statement in st_rest)
S(c, "where", H(k), "intro", t, "العملاء", "يمكنك البحث عن عملائك و الإطلاع على معلوماتهم بشكل مباشر من خلال: لوحة التحكم > العملاء.")
SNF(c, "reason", "A stated reason for this concern's placement", "help.zid.sa/customer-list/; help.zid.sa/create-customer/", why=NO_REASON)

# ---------- ZD-C-092 Customer self-service portal ----------
c = "ZD-C-092"; k = "c-zid-sa"; t = HT(k, "بوابة خدمة العملاء الذاتيه (لوحة التحكم الجديدة)")
drop(c, "reason")
S(c, "where", H(k), "خطوات طلب الدعم", t, "العملاء> دعم العملاء",
  "أيضا ستصلك رسالة على رقمك المسجل بالمتجر وستجد التذكره في لوحة التحكم من خلال : العملاء> دعم العملاء")
S(c, "boundary", H(k), "للحالات الخاصة", t, "RMS; HubSpot",
  "طلبات مزيد وضمان زد يتم توجيهها تلقائيًا إلى تذاكر RMS أو HubSpot بحسب الحالة، مع إرسال إشعارات واتس آب من الحساب المناسب لكل خدمة.")
S(c, "reason", H(k), "intro", t, "تجربة موحّدة",
  "بوابة خدمة العملاء الذاتية هي منصة جديدة تمكّن عملاء المتاجر من إدارة طلباتهم والحصول على الدعم بعد الشراء بسهولة، من خلال تجربة موحّدة تتيح لهم استعراض الطلبات ورفع طلبات الخدمة أو الدعم من مكان واحد بشكل أبسط وأوضح.",
  note="The stated reason for one portal where store customers follow orders and raise requests.")

# ---------- ZD-C-093 Blogs ----------
c = "ZD-C-093"; k1, k2 = "channels-online-store-blog", "blog-app"
t1 = HT(k1, "المدونة ( لوحة التحكم الجديدة)"); t2 = HT(k2, "تطبيق المدونة | Blog ( لوحة التحكم الجديدة )")
drop(c, "reason"); drop(c, "decides", ("observation needed",))
S(c, "where", H(k1), "intro", t1, "المتجر الإلكتروني > المدونة", "لوحة التحكم >المتجر الإلكتروني > المدونة")
S(c, "where", H(k2), "خطوات تفعيل تطبيق بلوق", t2, "Blog", "سيتم توجيهك لمنصة Blog قم بتسجيل حساب جديد او تسجيل الدخول في حال وجود حساب مسبق",
  note="Said of the blog app installed from the App Market.")
S(c, "decides", H(k1), "ملاحظة", t1, "باقة النمو; الباقة الاحترافية", "خاصية المدونة متاحة فقط لتجار باقة النمو والباقة الاحترافية",
  scope="باقة النمو; الباقة الاحترافية")
S(c, "boundary", H(k2), "ملاحظة", t2, "تك ستيشن", "التطبيق يدعم الثيمات المطورة من قبل شركة تك ستيشن والثيمات المطورة من قبل زد فقط")
S(c, "reason", H(k1), "intro", t1, "مباشرة داخل المتجر",
  "تمكّن خاصية المدونة من نشر المقالات والمحتوى مباشرة داخل المتجر، بما يساهم في جذب زيارات مجانية عبر محركات البحث، وبناء ثقة العملاء وتعزيز العلامة التجارية، وزيادة الزيارات المتكررة من خلال محتوى متجدد، دون الاعتماد على الإعلانات المدفوعة أو وسائل التواصل الاجتماعي",
  note="The stated reason for publishing content inside the store.")

# ---------- ZD-C-098 Sender name ----------
c = "ZD-C-098"; k = "abandonment-cart"; t = HT(k, "السلات المتروكة ( لوحة التحكم الجديدة )")
S(c, "decides", H(k), "اسم المرسل", t, "ZeSTORE",
  "وفي حال لم تقم بتفعيل اسم مرسل مخصص لمتجرك، فسيتم استخدام الاسم الافتراضي “ZeSTORE” الخاص بمنصة زد.")
S(c, "reason", H(k), "ملاحظة", t, "هيئة الاتصالات",
  "بناء على اشتراطات هيئة الاتصالات تجنب ارسال اي محتوى ترويجي لمناسبات او ارسال اكواد خصم كونه يعد مخالف ويعرضك لإيقافها، لإرسال رسائل دعائية لابد من تخصيص اسم المرسل وارسال رسائل دعائية عبر الرسائل النصية من الاسم المنتهي بـ AD",
  note="The stated basis for requiring a custom sender name for promotional SMS.")

# ---------- ZD-C-105 Reports and analytics ----------
c = "ZD-C-105"; k1, k2 = "dashboard-analytics", "customizable-reports"
t1 = HT(k1, "التحليلات ( لوحة التحكم الجديدة )"); t2 = HT(k2, "التحليلات التقارير ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "decides", H(k1), "ملاحظة", t1, "باقة زد لايت; باقة النمو; الباقة الاحترافية; باقة الأعمال الكبيرة",
  "بعض عناصر الإحصائيات غير متاحة في باقة زد لايت و باقة النمو ، و متوفرة في الباقة الاحترافية وباقة الأعمال الكبيرة.",
  scope="الباقة الاحترافية; باقة الأعمال الكبيرة")
S(c, "decides", H(k2), "ملاحظة", t2, "التقارير", "التقارير خاصة فقط لباقة الأعمال الكبيره ، النخبة ، الإحترافية",
  scope="باقة الأعمال الكبيره; النخبة; الإحترافية")
S(c, "decides", CHUNK, "compare-plans group Reports & Analytics", ST[CHUNK], "Reports - Sales Channels", PL("Reports - Sales Channels"),
  scope=PLAN_SCOPE, note=PLAN_NOTE + " Recorded beside the help article, which states that reports are only for باقة الأعمال الكبيره، النخبة، الإحترافية.")
S(c, "reason", H(k2), "intro", t2, "دون الحاجة إلى أدوات خارجية",
  "تتيح لك هذي الخاصيه إنشاء وتخصيص وإدارة التقارير مباشرة من داخل منصة زد، دون الحاجة إلى أدوات خارجية أو معرفة تقنية متقدمة",
  note="The stated reason for building reports into the dashboard.")

# ---------- ZD-C-106 Marketing tools ----------
c = "ZD-C-106"
drop(c, "reason")
SNF(c, "reason", "A stated reason for the marketing tools placement",
    "zid.sa/en/solutions/marketing-tools/; help.zid.sa/create-discount/; help.zid.sa/discounts/; help.zid.sa/bundle_offer/; help.zid.sa/loyalty-program/",
    why=NO_REASON)

# ---------- ZD-C-107 WhatsApp ----------
c = "ZD-C-107"
for p in ("responsible", "boundary", "reason"): drop(c, p)
S(c, "responsible", H("whatsapp"), "قبل أن تبدأ", HT("whatsapp", "تفعيل الحساب في واتساب زد"), "حساب Meta للأعمال",
  "هذه الخطوة تتطلب أن يكون لديك حساب Meta للأعمال جاهزًا مع بيانات نشاطك التجارية مكتملة.",
  note="The account linked is the merchant's own Meta business account.")
S(c, "responsible", H("meta-restriction"), "الأسئلة الشائعة", HT("meta-restriction", "التقييد والحظر على حافظة الأعمال"), "سياسات ميتا",
  "لا، مشاكل التقييد أو الحظر تخضع بالكامل لسياسات ميتا، والقرار النهائي من جهتهم فقط.")
S(c, "decides", H("meta-restriction"), "intro", HT("meta-restriction", "التقييد والحظر على حافظة الأعمال"), "ميتا",
  "مشاكل التقييد أو الحظر على حافظة الأعمال أو رقم الواتساب لاتستطيع زد التحكم فيها أو الإطلاع على أسبابها، والقرار النهائي في رفعها أو الإبقاء عليها يعود لميتا.",
  note="What the help centre states happens when the partner restricts the account.")
S(c, "boundary", H("whatsapp-app-vs-api"), "واتساب زد: المنصة جاهزة داخل متجرك",
  HT("whatsapp-app-vs-api", "الفرق بين تطبيق واتساب أعمال والواتساب المؤسسي API"), "منصة واتساب للأعمال (API)",
  "واتساب زد مبني على منصة واتساب للأعمال (API) ومربوط بمتجرك مباشرة، فلا تحتاج مطورًا ولا مزود خدمة آخر.")
S(c, "decides", H("whatsapp-templates"), "أنواع القوالب وتكلفتها", HT("whatsapp-templates", "أنواع قوالب الواتساب وتكلفتها"), "رصيد النقاط",
  "تُصنّف ميتا الرسائل إلى أربعة أنواع، وتختلف تكلفة كل رسالة تبعًا لنوعها ومفتاح دولة رقم العميل المستلم. وتُحتسب التكلفة عن كل رسالة مُسلَّمة وتُخصم من رصيد النقاط في متجرك.")
S(c, "decides", H("whatsapp-templates"), "تكاليف الرسائل ليست ثابتة", HT("whatsapp-templates", "أنواع قوالب الواتساب وتكلفتها"), "شركة ميتا",
  "تقوم شركة ميتا بتحديث أسعارها دوريًا (كل ربع سنة تقريبًا) والذي تعتمد عليها النقاط المحسوبة.")
S(c, "reason", H("whatsapp-templates"), "طريقة الإنشاء", HT("whatsapp-templates", "أنواع قوالب الواتساب وتكلفتها"), "مراجعة ميتا",
  "تتولّى زد صياغة القوالب بعناية مع ضبط المتغيرات (Variables) والتحقق من الصياغة وإظهار رسالة خطأ عند الصياغة الخاطئة قبل إرسال القالب لمراجعة ميتا، بهدف رفع فرص قبولها وتقليل حالات الرفض.",
  note="The stated reason for Zid drafting the message templates before Meta reviews them.")

# ---------- ZD-C-110 Sales channels (marketplaces) ----------
c = "ZD-C-110"; kf, ka, kj = "marketplaces-faq", "about-marketplaces", "jahez"
tf = HT(kf, "الأسئلة الشائعة لقنوات البيع"); ta = HT(ka, "عن قنوات البيع ( لوحة التحكم الجديدة)"); tj = HT(kj, "ربط جاهز (لوحة التحكم الجديدة )")
drop(c, "responsible")
S(c, "responsible", H(kf), "الإعداد والتسجيل, السؤال 2", tf, "أمازون البائعين",
  "نعم، تحتاج إلى حساب نشط على أمازون البائعين للاستفادة من خدمة ربط زد بأمازون.",
  note="The merchant sells on Amazon through its own seller account.")
S(c, "responsible", H(kf), "السؤال 8", tf, "GDPR; CCPA; PCI-DSS",
  "تم تصميم التكامل للامتثال إلى أعلى معايير الامتثال التنظيمي، بما في ذلك GDPR، CCPA، وPCI-DSS.",
  note="A compliance statement for the marketplace integration; it names no party.")
S(c, "decides", H(ka), "نسبة زد من أمازون حسب الباقة", ta, "نسبة زد من أمازون",
  "نسبة زد من أمازون حسب الباقة : النمو: 5% الانطلاقة : 8% الاحترافية:0.95%", scope="النمو; الانطلاقة; الاحترافية")
S(c, "decides", H(kf), "السؤال 9", tf, "المحفظة",
  "يتم فرض الرسوم باستخدام المحفظة. نسمح بحد أقصى 500 ريال سعودي كرصيد. بعد ذلك، سيتوقف التطبيق عن العمل حتى تقوم بإعادة شحن محفظتك.")
S(c, "decides", H(kf), "الإعداد والتسجيل, السؤال 4", tf, "باقة زد لايت", "لا، تطبيق ربط قنوات البيع غير متاح على باقة زد لايت.", scope="باقة زد لايت")
S(c, "decides", H(kf), "الإعداد والتسجيل, السؤال 7", tf, "أمازون", "حاليًا، لدينا أمازون في السعودية والإمارات.", scope="السعودية; الإمارات")
S(c, "decides", H(kj), "ماهي شروط الانضمام لـ جاهز؟", tj, "شروط الانضمام لـ جاهز",
  "1- سجل تجاري او وثيقة عمل حر. 2-تفعيل مزيد. 3-المنتجات سريعة التحضير او الجاهزة التي لا يتعدى تحضيرها 10 دقائق. 4-موقع المتجر او المخزون في احد مدن المملكة.",
  scope="احد مدن المملكة")
S(c, "boundary", H(kf), "السؤال 2", tf, "واجهات برمجة التطبيقات (APIs)",
  "يستخدم التكامل واجهات برمجة التطبيقات (APIs) لمزامنة البيانات بين نظام زد ونظام قناة البيع.")
S(c, "boundary", H(kj), "الأسئلة الشائعة (جاهز)", tj, "مندوب جاهز",
  "الشحن سيتم إنشاؤه بشكل تلقائي بأسم مندوب جاهز ولا يظهر في متجرك، فقط لعملاء جاهز في التطبيق.")

# ---------- ZD-C-112 Zid Voice ----------
c = "ZD-C-112"; k = "zid-voice"; t = HT(k, "زد فويس")
for p in ("decides", "responsible", "boundary", "reason"): drop(c, p)
S(c, "where", H(k), "طريقة الاستخدام", t, "زد فويس", "من القائمة الرئيسية ← الطلبات ← زد فويس.")
S(c, "decides", H(k), "مزايا الخدمة", t, "100 مكالمة مجانية", "100 مكالمة مجانية.")
S(c, "decides", VOICE, "hero", VOICE_ST, "Limited pilot", "Available now for abandoned cart recovery · Limited pilot")
SNF(c, "decides", "Which plans or add-ons include Zid Voice beyond the free calls, and the price of further calls",
    "help.zid.sa/zid-voice/; zid.sa/en/solutions/zid-voice/; zid.sa/en/pricing/")
S(c, "responsible", H(k), "مزايا الخدمة", t, "بالنيابة عنك", "ذكاء اصطناعي يتواصل بالنيابة عنك.",
  note="States on whose behalf the calls are made; the company behind the voice agent is not named.")
SNF(c, "responsible", "Which company provides the voice agent, and the terms that govern the calls",
    "help.zid.sa/zid-voice/; zid.sa/en/solutions/zid-voice/; zid.sa/ar/legal/terms-conditions/")
S(c, "boundary", H(k), "لإنشاء حملة", t, "السلات المتروكة", "حدد طريقة اختيار العملاء من السلات المتروكة او رفع ملف عندك")
S(c, "reason", VOICE, "A call, not another message.", VOICE_ST, "A call, not another message.",
  "Instead of messages that get missed, Zid Voice reaches customers with a smart, personal call and responds to hesitation in real time.",
  note="The stated reason for reaching customers by a call rather than a message.")

# ---------- ZD-C-113 Online store and store design ----------
c = "ZD-C-113"; k1, k2 = "store-design", "themes"
t1 = HT(k1, "تصميم المتجر"); t2 = HT(k2, "الثيمات ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "where", H(k1), "تصميم المتجر", t1, "تصميم المتجر",
  "يمكنك تخصيص تصميم متجرك و إضافة شعار المتجر و أيقونة المتجر من خلال: لوحة التحكم  > تصميم المتجر")
S(c, "decides", H(k1), "القائمة الرئيسية", t1, "القائمة الرئيسية", "القائمة الرئيسية : متاحة في الباقة الاحترافية وباقة الأعمال الكبيرة.",
  scope="الباقة الاحترافية; باقة الأعمال الكبيرة")
S(c, "decides", H(k2), "الثيمات المخصصة", t2, "تخصيص الثيمات", "خاصية تخصيص الثيمات متاحة للباقة الإحترافية وباقة الاعمال الكبيرة فقط",
  scope="الباقة الإحترافية; باقة الاعمال الكبيرة")
S(c, "decides", H(k1), "عبارة حفظ الحقوق", t1, "صنع بواسطة زد",
  "إفتراضياً يظهر أسفل المتجر نص حقوق (صنع بواسطة زد)، يمكنك تعديل النص بحيث يكون بأي نص تفضله")
SNF(c, "reason", "A stated reason for the store design placement",
    "help.zid.sa/store-design/; help.zid.sa/themes/; zid.sa/en/solutions/e-store/", why=NO_REASON)

# ---------- ZD-C-114 Merchant support ----------
c = "ZD-C-114"; k = "create-ticket"; t = HT(k, "تذاكر الدعم ( لوحة التحكم الجديدة )")
drop(c, "reason")
S(c, "where", H(k), "intro", t, "تذكرة", "يمكنك رفع طلب أو تقديم اعتراض عبر لوحة تحكم متجرك من خلال: لوحة التحكم > الضغط على أيقونة تذكرة")
SNF(c, "reason", "A stated reason for the support placement", "help.zid.sa/create-ticket/", why=NO_REASON)

# ---------- ZD-C-115 Zid Growth ----------
c = "ZD-C-115"; k = "zid-growth"; t = HT(k, "عن زد نمو ( لوحة التحكم الجديدة )")
drop(c, "responsible"); drop(c, "reason")
S(c, "where", H(k), "intro", t, "النمو", "يمكنك الوصول الى خدمات النمو من خلال : لوحة التحكم > النمو")
S(c, "decides", H(k), "مدير العلاقات لمتجرك", t, "مدير العلاقة", "مدير العلاقة متاح للباقة الإحترافية", scope="الباقة الإحترافية")
S(c, "responsible", H(k), "خدمات النمو", t, "شركاء يقدمون الخدمة",
  "شركاء يقدمون الخدمة. رقم الجوال للتواصل. قم بقراءة الشروط والأحكام ثم قم بالضغط على إضافة الى السلة وسيتم نقلك لصفحة الاشتراك لمتابعة الدفع",
  note="Each Growth service shows the partners who provide it and terms to read before purchase.")
OBS(c, "responsible", "The terms shown for each Zid Growth service and the partner named as its provider",
    "Zid merchant dashboard: النمو > خدمات النمو (a service's details before purchase)")
SNF(c, "reason", "A stated reason for the Zid Growth placement", "help.zid.sa/zid-growth/", why=NO_REASON)

# ---------- ZD-C-116 Store mobile app ----------
c = "ZD-C-116"; k1, k2 = "create-app", "subscription-to-mobile-app"
t1 = HT(k1, "عن تطبيق الجوال ( لوحة التحكم الجديدة )"); t2 = HT(k2, "الاشتراك بخدمة تطبيق الجوال ( لوحة التحكم الجديدة )")
for p in ("responsible", "boundary", "reason"): drop(c, p)
S(c, "where", H(k1), "أبزر المميزات", t1, "عناقيد التطبيقات", "بإمكانك إنشاء تطبيق لمتجرك بواسطة عناقيد التطبيقات.")
S(c, "where", H(k2), "الدخول للتطبيق", t2, "سوق التطبيقات في زد", "يمكن الوصول للتطبيق من سوق التطبيقات في زد أو مباشرة عبر الرابط من هنا")
S(c, "decides", H(k2), "مدة الاشتراك في التطبيق", t2, "مدة الاشتراك", "مدة الاشتراك في التطبيق سنة واحدة، وعند انتهاء فترة التجديد ينتهي الاشتراك.")
S(c, "responsible", H(k2), "ملاحظة", t2, "حساب مطورين (شركات)",
  "يلتزم التاجر بإنشاء حساب مطورين (شركات) في متاجر التطبيقات ابل / قوقل وتزويد فريق عناقيد التطبيقات بالبيانات الخاصة بالحساب، ليتمكن فريق عناقيد من رفع تطبيق التاجر على متجر التطبيقات.")
S(c, "responsible", H(k2), "ملاحظة", t2, "عناقيد التطبيقات",
  "في حال عدم توفر حساب مطورين ستقوم عناقيد التطبيقات برفع التطبيق على أحد الحسابات الشخصية الفرعية التابعة لعناقيد التطبيقات مجانًا في منصة ابل فقط.")
S(c, "boundary", H(k1), "أبزر المميزات", t1, "لوحة التحكم", "إدارة واحدة من لوحة التحكم لمحتويات المتجر من منتجات وتصنيفات والصفحات واستقبال الطلبات.")
S(c, "reason", H(k1), "لماذا يهمك تطبيق الجوال لمتجرك", t1, "لماذا يهمك تطبيق الجوال لمتجرك",
  "تعزيز العلامة التجارية الخاصة بمشروعك وذلك بتواجدك على متجر ابل iOS وقوقل بلاي Android.",
  note="Given under the heading لماذا يهمك تطبيق الجوال لمتجرك.")
