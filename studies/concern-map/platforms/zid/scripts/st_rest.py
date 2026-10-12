# Statements and gaps: shipping and partners, the app platform, commerce, settings and product lines (ZD-C-060 to ZD-C-116).
from stlib import *
ROLES = D("-user-roles-and-permissions-604944m0")
ROLES_ST = "docs.zid.sa: User Roles and Permissions (List of Available Permissions)"
OVERVIEW = D("zid-apps-overview"); POLICY = D("zid-app-activation-oauth-policy-2422816m0"); AUTH = D("authorization")
HOME = "https://help.zid.sa/"
NAV = "https://zid.sa/en/solutions/payments/"
def PERMQ(slug):
    t = open(F + "/docs/-user-roles-and-permissions-604944m0.md", encoding="utf-8").read()
    m = re.search(r"^\| `" + re.escape(slug) + r"`\s*\| ([^|]+?)\s*\| ([^|]+?)\s*\|$", t, re.M)
    return f"`{slug}` | {m.group(1)} | {m.group(2)}"
def PERM(c, slug, note=""):
    S(c, "decides", ROLES, "List of Available Permissions", ROLES_ST, slug, PERMQ(slug), scope="staff permission", note=note)

# ---------- ZD-C-060 Zid Logistics and direct shipping ----------
c = "ZD-C-060"
S(c, "where", AR_TERMS, "زد شب: ما هي خدمة الشحن المباشر؟", ST[AR_TERMS], "الشحن المباشر",
  "هي أداة تُتيح للتاجر شحن وتوصيل الطلبات إلى العملاء النهائيين عبر إتاحة وصول التاجر لشركات شحن متعددة بخيارات توصيل متنوعة، وتُفعّل فورياً من لوحة تحكم التاجر، على أن تُدار جميع رسومها والتسويات المالية المتعلقة بها تلقائياً من محفظة التاجر وفقاً لهذه الشروط والأحكام.")
S(c, "where", H("logistics-shipping-methods"), "intro", struct(H("logistics-shipping-methods"), "اللوجستيات ( لوحة التحكم الجديدة )"), "لوحة التحكم > اللوجستيات > طرق الشحن",
  "للوصول الى طرق الشحن من خلال : لوحة التحكم > اللوجستيات > طرق الشحن")
S(c, "decides", CHUNK, "compare-plans group Shipping", ST[CHUNK], "Zid Logistics: One Contract for 35 Carriers", PL("Zid Logistics: One Contract for 35 Carriers"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", AR_TERMS, "أحكام الدفع في الشحن المباشر", ST[AR_TERMS], "باقة التاجر",
  "تختلف أسعار بوالص الشحن والأوزان المحددة والرسوم المتعلقة بها باختلاف نوع باقة التاجر لدى منصة زد.")
S(c, "decides", PRICING, "plan card Rise", ST[PRICING], "Rise: All features of Starter package, plus:", "Shipping rates starting from 11 SAR", scope="plan Rise")
S(c, "decides", PRICING, "plan card Professional", ST[PRICING], "Professional: Standout Features", "Shipping rates starting from 8.5 SAR", scope="plan Professional")
PERM(c, "manage.zidship.settings")
S(c, "responsible", AR_TERMS, "التعويض في خدمة الشحن المباشر", ST[AR_TERMS], "وسيطاً تقنياً",
  "تُعد زد وسيطاً تقنياً ومسهّلاً لخدمات الشحن، ولا تُعد شركة نقل مباشرة؛ وتخضع كافة أحكام التعويض لسياسات وشروط شركات الشحن المزودة للخدمة.")
S(c, "responsible", AR_TERMS, "آلية طلب التعويض للشحنات المفقودة", ST[AR_TERMS], "قرار قبول التعويض",
  "في حالة تعذر العثور على الشحنة، تنتقل زد إلى مرحلة المطالبة بالتعويض من شركة الشحن. غير أن قرار قبول التعويض أو رفضه، وتحديد قيمته، يخضع لسياسات شركة الشحن المعتمدة، وليس لزد سيطرة على هذا القرار.",
  note="What happens when a carrier loses a shipment, as the Terms state it.")
S(c, "responsible", AR_TERMS, "أنواع الشحن المتاحة في الشحن المباشر", ST[AR_TERMS], "شروط شركة الشحن",
  "تخضع كل خدمة شحن للشروط والأحكام الخاصة بشركة الشحن المزودة لها، والمعلنة ضمن إعدادات وسيلة الشحن في لوحة تحكم المتجر.")
S(c, "responsible", "https://zid.sa/en/legal/global-shipping-terms/", "Global Shipping", "Global Shipping terms (zid.sa/en/legal/global-shipping-terms)", "Customs duties",
  "Customs duties will be charged to the merchant if the end customer refuses to pay them, and the fees will be deducted from the Zid wallet.", scope="Global Shipping")
S(c, "boundary", AR_TERMS, "حساب الوزن والأوزان الإضافية", ST[AR_TERMS], "قياسات شركة الشحن",
  "تتولى شركة الشحن المعتمدة قياس وتدقيق الوزن الفعلي والحجمي للشحنة في أي مرحلة من مراحل الاستلام أو الشحن أو التوصيل، وتُحدَّث بيانات الشحنة بناءً على قياسات شركة الشحن؛ وبناءً عليه تقوم زد بتحديث تكلفة الشحنة تلقائياً وخصم الفروق المالية المستحقة من محفظة التاجر.")
S(c, "boundary", "https://help-partner.zid.sa/en/articles/10325692-critical-update-new-shipping-pricing-structure", "New Pricing Structure",
  struct("https://help-partner.zid.sa/en/articles/10325692-critical-update-new-shipping-pricing-structure", "Critical Update: New Shipping Pricing Structure"), "integrated with ZidShip",
  "Fulfillment & Shipping Apps integrated with ZidShip: 0.30 SAR per transaction")
S(c, "reason", CHUNK, "compare-plans group Shipping", ST[CHUNK], "Zid Logistics: One Contract for 35 Carriers",
  "Save time and effort with one contract covering 35 carriers instead of dealing with each separately.", note="The stated reason for one contract across carriers.")
ASK(c, "responsible", "The names of the carriers behind the 35-carrier contract and which party contracts with each carrier", "zid.sa/en/solutions/shipping/; zid.sa/ar/legal/terms-conditions/ (زد شب)")

# ---------- ZD-C-061 Shipping apps and third-party logistics companies ----------
c = "ZD-C-061"
S(c, "where", CATS, "categories.apps_by_category", ST[CATS], "category id 5", '"id":5,"parent_id":null,"name":"الشحن والتخزين"')
S(c, "where", OVERVIEW, "Shipping apps", struct(OVERVIEW, "Overview (app types)"), "Shipping apps",
  "Shipping apps are specifically designed to integrate logistics and shipping services into the merchant's store.")
S(c, "decides", OVERVIEW, "Prerequisites for Developing Private Apps", struct(OVERVIEW, "Overview (app types)"), "logistic type",
  "The app should not be of the \"logistic\" type, as all shipping and fulfillment apps must be public.")
S(c, "decides", AR_TERMS, "شركات الخدمات اللوجستية الطرف الثالث على متجر زد للتطبيقات (ZAM)", ST[AR_TERMS], "السعودية أو أي من دول الخليج",
  "بإمكان التاجر إذا كان موجودا في المملكة  العربية السعودية أو أي من دول الخليج  تفعيل الشحن من خلال شركات الخدمات اللوجستية المرخصة من داخل الموقع / التطبيق لتسليم البضائع التي تم شراؤها من متجر زد الخاص به.",
  scope="المملكة العربية السعودية; دول الخليج")
S(c, "decides", AR_TERMS, "خيارات الدفع في الشحن المباشر", ST[AR_TERMS], "الربط المخصص مع شركة الشحن",
  "الربط المخصص مع شركة الشحن: في حالة قيام التاجر بربط حسابه مباشرة مع شركة شحن محددة (عبر عقد خاص بين التاجر والشركة)، يتم خصم رسوم خدمة قدرها 1 ريال (غير شاملة لضريبة القيمة المضافة) لكل بوليصة شحن يتم إصدارها عبر هذا الربط المخصص.")
S(c, "responsible", AR_TERMS, "شركات الخدمات اللوجستية الطرف الثالث على متجر زد للتطبيقات (ZAM)", ST[AR_TERMS], "ليست طرفًا",
  "قد يوقع التاجر وشركات الخدمات اللوجستية الثالثة اتفاقيات ووثائق قانونية تنظم العلاقة بينهما، ويقر التاجر ويفهم أن زد ليست طرفًا في هذه الالتزامات، ولا ما ينشأ عنها.")
S(c, "responsible", AR_TERMS, "شركات الخدمات اللوجستية الطرف الثالث على متجر زد للتطبيقات (ZAM)", ST[AR_TERMS], "عدم تقديم الخدمة بطريقة فعّالة",
  "يوافق التاجر ويدرك أن زد لن تكون مسؤولة عن أي أضرار مباشرة أو غير مباشرة أو عرضية أو خاصة أو تبعية أو فادحة بما في ذلك على سبيل الذكر لا الحصر الأضرار الناجمة عن خسارة الربح أو السمعة أو الاستخدام أو البيانات أو الخسائر غير الملموسة الأخرى الناتجة من استخدام الخدمة أو عدم القدرة على استخدامها أو عدم تقديم شركات الخدمات اللوجستية الطرف الثالث الخدمة بطريقة فعّالة.",
  quote="الناتجة من استخدام الخدمة أو عدم القدرة على استخدامها أو عدم تقديم شركات الخدمات اللوجستية الطرف الثالث الخدمة بطريقة فعّالة.",
  note="What happens when a third-party logistics company fails, as the Terms state it.")
S(c, "boundary", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Orders [Add Order Comment]", APIW("Merchant APIs > Orders", "Add Order Comment"))
S(c, "boundary", PAYOUTS, "When you earn and how your share is calculated", ST[PAYOUTS], "Shipping apps cycle",
  "Shipping apps follow a different cycle: the record is created on the 1st of the month, and Zid uploads an invoice for activation and order fees that the partner pays.")
S(c, "boundary", "https://help-partner.zid.sa/en/articles/10325692-critical-update-new-shipping-pricing-structure", "New Pricing Structure",
  struct("https://help-partner.zid.sa/en/articles/10325692-critical-update-new-shipping-pricing-structure", "Critical Update: New Shipping Pricing Structure"), "Shipping Apps", "Shipping Apps: 0.70 SAR per transaction")
SNF(c, "reason", "A stated reason why shipping and fulfillment apps must be public", "docs.zid.sa/zid-apps-overview.md; help-partner.zid.sa shipping app articles; zid.sa/ar/legal/terms-conditions/")

# ---------- ZD-C-062 Store shipping methods ----------
c = "ZD-C-062"
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Shipping", APIW("Merchant APIs > Shipping"))
S(c, "where", H("shipping-settings"), "intro", struct(H("shipping-settings"), "اعدادات الشحن ( لوحة التحكم الجديدة )"), "إعدادات الشحن",
  "إعدادات الشحن تمنحك القدرة على إدارة تجربة الشحن بالكامل في متجرك، بما في ذلك تحديد قيود الشحن لكل منتج أو منطقة، ترتيب شركات التوصيل حسب الأولوية، وضبط شروط الشحن المجاني بما يتوافق مع سياساتك وعروضك، لضمان تجربة سلسة ومريحة لعملائك.")
OBS(c, "decides", "Which plans or staff permissions turn custom shipping methods on", "dashboard: لوحة التحكم > اللوجستيات > طرق الشحن")
GEN(c)
S(c, "boundary", D("list-store-delivery-options"), "Scopes", struct(D("list-store-delivery-options"), "List Store Shipping Methods"), EP("list-store-delivery-options"), SCOPEQ("list-store-delivery-options"))
S(c, "boundary", D("webhooks"), "Supported Conditions", struct(D("webhooks"), "Webhooks Overview"), "delivery_option_id",
  "`delivery_option_id` | Integer | The delivery option ID in Zid. | Any valid delivery option ID")
SNF(c, "reason", "A stated reason for the shipping-method placement", "help.zid.sa/shipping-settings/; help.zid.sa/logistics-shipping-methods/; docs.zid.sa Shipping group")

# ---------- ZD-C-063 Shipping and payment restrictions ----------
c = "ZD-C-063"
S(c, "where", H("payment-constraints"), "intro", struct(H("payment-constraints"), "قيود الشحن و الدفع (لوحة التحكم الجديدة )"), "الاعدادات > عام > قيود الشحن والدفع",
  "الطريقة الاولى : الاعدادات > عام > قيود الشحن والدفع")
S(c, "decides", H("payment-constraints"), "ملاحظة", struct(H("payment-constraints"), "قيود الشحن و الدفع (لوحة التحكم الجديدة )"), "الباقات",
  "خاصية قيود الشحن و  الدفع متاحة في باقة النمو والباقة الاحترافية وباقة الأعمال الكبيرة.", scope="باقة النمو; الباقة الاحترافية; باقة الأعمال الكبيرة")
S(c, "decides", H("payment-constraints"), "ملاحظة", struct(H("payment-constraints"), "قيود الشحن و الدفع (لوحة التحكم الجديدة )"), "3 خيارات دفع", "متاح لك إضافة 3 خيارات دفع ضمن خيارات الدفع.")
GEN(c)
SNF(c, "boundary", "An API endpoint, scope or webhook for shipping and payment restrictions", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names restrictions.")
S(c, "reason", H("payment-constraints"), "شروط القيد", struct(H("payment-constraints"), "قيود الشحن و الدفع (لوحة التحكم الجديدة )"), "عدد طلبات العميل الملغاة",
  "عدد طلبات العميل الملغاة: يمكنك تحديد عدد طلبات العميل وتحديد طريقة الدفع والاستفادة من القيد لحمايتك من طلبات الدفع عند الاستلام الوهمية أو من العملاء الغير جادين.")

# ---------- ZD-C-070 Zid App Market ----------
c = "ZD-C-070"
S(c, "where", AR_TERMS, "سوق تطبيقات زد: التعريفات", ST[AR_TERMS], "سوق تطبيقات زد (definition)",
  "سوق تطبيقات زد: هي منصة مملوكة لزد توفر حلول الربط التقني بين التاجر والشريك، وذلك لتمكين التاجر من ربط متجره بأحد تطبيقات المعروضة في خدمة سوق تطبيقات زد، وذلك لمساعدته في إدارة عمليات متجره بسهولة.")
S(c, "where", CATS, "categories.apps_by_category", ST[CATS], "category id 19", '"id":19,"parent_id":null,"name":"المالية والمدفوعات"',
  note="One of the seven top App Market categories; the full list is in the inventory.")
S(c, "decides", OVERVIEW, "Subscription Apps", struct(OVERVIEW, "Overview (app types)"), "Public apps",
  "Public apps:** Apps designed for wider use and are listed in Zid App Market. All merchants on the platform can view, install, and benefit from these apps.")
S(c, "decides", OVERVIEW, "App Development Cycle", struct(OVERVIEW, "Overview (app types)"), "Submit for Review",
  "After developing the app, our team will take some time to review your submission and test the app functionality before publishing it to the public.")
S(c, "decides", POLICY, "12. Review and enforcement", struct(POLICY, "Zid App Activation & OAuth Policy"), "Review and enforcement",
  "Apps that do not comply may be returned for correction, rejected during review, suspended until corrected or removed when the flow creates material security, privacy, usability or merchant-trust risk.")
PERM(c, "manage.app.market.details")
S(c, "responsible", AR_TERMS, "سوق تطبيقات زد: آلية التنفيذ وحدود المسؤولية", ST[AR_TERMS], "الشريك هو المقدم للخدمة",
  "يفهم التاجر ويوافق على أن الشريك هو المقدم للخدمة وأن علاقته بالشريك مستقلة عن علاقته بزد، وأن زد مجرد مقدم لحلول الربط التقني للاستفادة من سوق تطبيقات زد حسب التعريف الوارد أعلاه فى بند التعريفات.")
S(c, "responsible", AR_TERMS, "سوق تطبيقات زد: آلية التنفيذ وحدود المسؤولية", ST[AR_TERMS], "المشاكل التقنية",
  "لا تتحمل زد أي مسؤولية عن المشاكل التقنية التي تقع في التطبيقات أو الخدمات التي تم تطويرها أو تقديمها من قبل شركاء سوق التطبيقات.",
  note="What happens when an app partner's service fails, as the Terms state it.")
S(c, "responsible", H("faq-31"), "answer", struct(H("faq-31"), "FAQ: هل التطبيقات موثوقة؟"), "لا تضمن زد",
  "تبذل زد أقصى جهودها لاختبار وتدقيق التطبيقات للتأكد من كفاءة الجودة المقدمة قبل إطلاق أي تطبيق ولا تضمن زد أي طرف ثالث مستقل مقدم للخدمة")
S(c, "boundary", AR_TERMS, "سوق تطبيقات زد: آلية التنفيذ وحدود المسؤولية", ST[AR_TERMS], "صلاحيات النطاقات",
  "يفهم التاجر ويوافق على تحمله مسؤولية مشاركة بيانات المتجر مع الشريك بعد تثبيت تطبيق الخدمة وإعطاءه صلاحيات النطاقات المطلوبة بحسب طبيعة الخدمة المقدمة.")
S(c, "boundary", D("events-878234m0"), "App Subscription Events", struct(D("events-878234m0"), "App Management Events"), "app.market.application.install",
  "`app.market.application.install` | Send notification on the installation of the application.")
SNF(c, "reason", "A stated reason for placing apps with independent partners", "zid.sa/ar/legal/terms-conditions/ (سوق تطبيقات زد); docs.zid.sa/zid-apps-overview.md; help.zid.sa FAQ ماهو سوق تطبيقات زد؟")

# ---------- ZD-C-071 OAuth and scopes ----------
c = "ZD-C-071"
S(c, "where", AUTH, "Base URIs", struct(AUTH, "Authorization"), "https://oauth.zid.sa", "**Base OAuth Server URL**: This URL is for handling app authentication.")
S(c, "decides", AUTH, "2- Redirect", struct(AUTH, "Authorization"), "scopes approval",
  "The merchant will see the scopes that your application is requesting and approve (or decline)")
S(c, "decides", AUTH, "2- Redirect", struct(AUTH, "Authorization"), "Partner Dashboard scopes",
  "Zid AppMarket supports many scopes to be requested from the merchant; you can select the needed scopes for your application via your application page in the Partner Dashboard")
S(c, "decides", D("create-first-app"), "Select App Scopes", struct(D("create-first-app"), "Create your First App"), "Select App Scopes",
  "Be sure to provide clear justifications for each scope to help the review team approve your selections.")
S(c, "responsible", POLICY, "4. Rejected activation flows, C", struct(POLICY, "Zid App Activation & OAuth Policy"), "Manual credentials",
  "Never ask merchants to paste Zid access or refresh tokens, manager tokens, API keys, client secrets or Zid passwords into your app.")
S(c, "responsible", POLICY, "8. OAuth and security requirements", struct(POLICY, "Zid App Activation & OAuth Policy"), "Request only the scopes needed",
  "Request only the scopes needed for the app's documented functionality.")
S(c, "boundary", AUTH, "Important Requirements", struct(AUTH, "Authorization"), "Authorization; X-Manager-Token",
  "All API requests into our system require the call to be authorized, usally by sending `Authorization` & `X-Manager-Token` headers")
S(c, "boundary", D("events-878234m0"), "App Subscription Events", struct(D("events-878234m0"), "App Management Events"), "app.market.application.authorized",
  "`app.market.application.authorized` | Triggered when a merchant authorizes an app prior to installation.")
S(c, "reason", AUTH, "Benefits of Using OAuth 2.0 with Zid", struct(AUTH, "Authorization"), "Scoped Permissions",
  "**Scoped Permissions**: Define specific access levels through scopes, allowing merchants to control what data your app can access.")
S(c, "reason", POLICY, "11. Approved Partner-managed setup", struct(POLICY, "Zid App Activation & OAuth Policy"), "Partner-managed setup",
  "This path is for apps whose service may require meaningful preparation before a Zid store can be connected—for example, creating or selecting an operational tenant, provisioning a carrier account, completing contractual checks or configuring an existing business platform.")

# ---------- ZD-C-072 Webhooks ----------
c = "ZD-C-072"
S(c, "where", D("webhook-health-tracking-2197281m0"), "intro", struct(D("webhook-health-tracking-2197281m0"), "Webhook Health Tracking"), "circuit breaker",
  "Zid automatically monitors the health of your webhook endpoints using a circuit breaker pattern.")
S(c, "where", LLMS, "API Docs", ST[LLMS], "Webhooks > APIs", APIW("Webhooks > APIs"))
S(c, "decides", D("webhook-health-tracking-2197281m0"), "Health States", struct(D("webhook-health-tracking-2197281m0"), "Webhook Health Tracking"), "broken",
  "| broken | The endpoint has failed 30 or more times in the past hour | Event delivery is suspended until you recover the webhook |")
S(c, "decides", D("webhooks"), "Event Conditions", struct(D("webhooks"), "Webhooks Overview"), "conditions",
  "**Note:** Conditions are currently supported only for the `order.create` and `order.status.update` events.")
S(c, "responsible", D("webhook-health-tracking-2197281m0"), "What Happens When a Webhook Is Broken", struct(D("webhook-health-tracking-2197281m0"), "Webhook Health Tracking"), "No new events are dispatched",
  "**No new events are dispatched** to that endpoint. Pending undelivered events for the webhook are also discarded to prevent backlogs.",
  note="What happens when a partner's endpoint keeps failing.")
S(c, "boundary", D("create-a-webhook"), "Scopes", struct(D("create-a-webhook"), "Create Webhook"), EP("create-a-webhook"), SCOPEQ("create-a-webhook"))
S(c, "reason", D("webhook-health-tracking-2197281m0"), "intro", struct(D("webhook-health-tracking-2197281m0"), "Webhook Health Tracking"), "health states",
  "When an endpoint starts failing consistently, its status transitions through health states that reduce noise and   protect your systems from unnecessary traffic — and notify you before things get worse.")

# ---------- ZD-C-073 Embedded apps ----------
c = "ZD-C-073"
S(c, "where", D("embedded-apps-2168216m0"), "intro", struct(D("embedded-apps-2168216m0"), "Embedded Apps"), "iframe",
  "These applications are integrated directly into the dashboard through an iframe, allowing merchants to access and interact with your app without leaving the Zid Merchant Dashboard.")
S(c, "decides", POLICY, "7. Embedded applications", struct(POLICY, "Zid App Activation & OAuth Policy"), "Embedded applications",
  "Embedded apps should open inside the Zid Merchant Dashboard without an unnecessary separate partner login.")
S(c, "responsible", POLICY, "7. Embedded applications", struct(POLICY, "Zid App Activation & OAuth Policy"), "embedded authentication mechanism",
  "Use the embedded authentication mechanism supported by Zid for your integration.")
S(c, "boundary", D("embedded-apps-2168216m0"), "Step 1", struct(D("embedded-apps-2168216m0"), "Embedded Apps"), "embedded_apps_tokens_write",
  "Ensure you include the `embedded_apps_tokens_write` scope in your initial OAuth request.")
S(c, "reason", D("embedded-apps-2168216m0"), "flow", struct(D("embedded-apps-2168216m0"), "Embedded Apps"), "bypass standard logins", "The embedded apps feature is designed to bypass standard logins.")

# ---------- ZD-C-074 Private apps and direct API access ----------
c = "ZD-C-074"
S(c, "where", H("unpublished-app"), "خطوات الربط", struct(H("unpublished-app"), "تفعيل تطبيق غير متوفر او منشور في سوق التطبيقات ( لوحة التحكم الجديدة )"), "سوق التطبيقات> تطبيقاتي",
  "تفعيل التطبيق في المتجر من خلال  صفحه سوق التطبيقات> تطبيقاتي")
S(c, "decides", OVERVIEW, "Prerequisites for Developing Private Apps", struct(OVERVIEW, "Overview (app types)"), "Professional or Enterprise plan; API Access",
  "The store must have a Professional or Enterprise plan subscription, or the merchant must have activated [API Access](https://web.zid.sa/subscriptions) from the dashboard to be able to install the private app.")
S(c, "decides", H("unpublished-app"), "باقة المتجر", struct(H("unpublished-app"), "تفعيل تطبيق غير متوفر او منشور في سوق التطبيقات ( لوحة التحكم الجديدة )"), "خدمة الربط المباشرة (APIs)",
  "او في حال كانت باقة المتجر اقل من الاحترافية يمكنك شراء خاصيه الربط الخاص API من خلال : المالية > الفوترة > الإضافات > تصفح الإضافات > خدمة الربط المباشرة (APIs)")
S(c, "decides", PRICING, "plan card Professional", ST[PRICING], "Professional: Standout Features", "Connect your store with external systems (via API)", scope="plan Professional")
PERM(c, "manage.store.zid.keys")
S(c, "responsible", H("api-integration"), "دور منصة زد ودور المطور التقني", struct(H("api-integration"), "خطوات الربط مع انظمة خارجية API"), "التاجر (Merchant)",
  "• التعاقد مع المطور التقني أو مزود النظام الخارجي.")
S(c, "responsible", H("api-integration"), "دور منصة زد ودور المطور التقني", struct(H("api-integration"), "خطوات الربط مع انظمة خارجية API"), "منصة زد (Zid)",
  "• توفير الواجهات البرمجية (APIs) وأدوات الربط.")
S(c, "boundary", OVERVIEW, "Subscription Apps", struct(OVERVIEW, "Overview (app types)"), "Private apps",
  "Private apps:** Apps intended for specific stores only. They are not listed in the Zid App Market and can only be installed by stores explicitly granted access.")
SNF(c, "reason", "A stated reason for limiting private apps to Professional plans or the API add-on", "docs.zid.sa/zid-apps-overview.md; help.zid.sa/unpublished-app/; help.zid.sa/api-integration/")

# ---------- ZD-C-075 Storefront APIs ----------
c = "ZD-C-075"
S(c, "where", LLMS, "API Docs", ST[LLMS], "API's > Checkout", APIW("API's > Checkout"))
S(c, "where", LLMS, "API Docs", ST[LLMS], "API's > Authentication", APIW("API's > Authentication"))
SNF(c, "decides", "What turns the storefront APIs on for a store (plan, setting or permission)", "docs.zid.sa API's groups (all endpoint pages read)", why="All storefront API pages were read; none states an entitlement.")
GEN(c)
S(c, "boundary", ROLES, "User Roles", ROLES_ST, "Role: Customer",
  "When interacting with the API, set the **`Role`** header in the request to **`Customer`** to perform operations as a customer.")
SNF(c, "reason", "A stated reason for the storefront API placement", "docs.zid.sa API's groups; docs.zid.sa/-user-roles-and-permissions-604944m0.md")

# ---------- ZD-C-076 Theme Market and themes ----------
c = "ZD-C-076"
S(c, "where", AR_TERMS, "سوق ثيمات زد: التعريفات", ST[AR_TERMS], "سوق الثيمات (definition)",
  "سوق الثيمات: هو منصة مملوكة لزد تحتوي على العديد من الثيمات المجانية، أو المدفوعة، لتمكن التاجر من تصميم متجره.")
S(c, "decides", PRICING, "plan card Rise", ST[PRICING], "Rise: All features of Starter package, plus:", "Access to themes store (Over 50 professional themes)", scope="plan Rise")
S(c, "decides", AR_TERMS, "سوق ثيمات زد", ST[AR_TERMS], "إعادة المتجر الى احد الثيمات المجانية",
  "في حال انتهى اشتراك التاجر في خدمة الثيمات المخصصة، يتم إعادة المتجر الى احد الثيمات المجانية التي تقدمها زد.")
S(c, "responsible", AR_TERMS, "سوق ثيمات زد", ST[AR_TERMS], "شريك سوق الثيمات",
  "في حال شراء او تفعيل أحد ثيمات شركاء سوق الثيمات يقر التاجر ويوافق على أن الشريك هو المقدم للخدمة وأن علاقته بالشريك مستقلة عن علاقته بزد.")
S(c, "responsible", AR_TERMS, "سوق ثيمات زد", ST[AR_TERMS], "حقوق الملكية الفكرية", "تمتلك زد حقوق الملكية الفكرية للثيمات التابعة لها.")
S(c, "boundary", PAYOUTS, "When you earn and how your share is calculated", ST[PAYOUTS], "Partner Share",
  "Partner Share = (Paid Amount by Merchant Excluding VAT) × Partner Rate", note="Theme partners are paid on this formula, as stated for apps, themes and landing pages.")
SNF(c, "reason", "A stated reason for the theme market placement", "zid.sa/ar/legal/terms-conditions/ (سوق ثيمات زد); zid.sa/en/solutions/themes/")

# ---------- ZD-C-077 Store account and profile ----------
c = "ZD-C-077"
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Account > Store", APIW("Merchant APIs > Account > Store"))
S(c, "where", H("account-settings"), "intro", struct(H("account-settings"), "اعدادات الحساب ( لوحة التحكم الجديدة )"), "لوحة التحكم > الإعدادات > إعدادات الحساب",
  "يمكنك التعديل على إعدادات الحساب ك البريد الالكتروني والرقم السري من خلال : لوحة التحكم > الإعدادات > إعدادات الحساب")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Account Details", PL("Account Details"), scope=PLAN_SCOPE, note=PLAN_NOTE)
PERM(c, "manage.store.account.settings")
S(c, "responsible", AR_TERMS, "الحسابات", ST[AR_TERMS], "حماية الحساب", "أنت مسؤول عن حماية حسابك، لذا عليك استخدام كلمة مرور قوية وحصر استخدامها على هذا الحساب فقط.")
S(c, "boundary", D("me-33664055e0"), "Scopes", struct(D("me-33664055e0"), "Me"), EP("me-33664055e0"), SCOPEQ("me-33664055e0"))
S(c, "boundary", D("store-33664558e0"), "Scopes", struct(D("store-33664558e0"), "Store"), EP("store-33664558e0"), SCOPEQ("store-33664558e0"))
SNF(c, "reason", "A stated reason for the account placement", "help.zid.sa/account-settings/; docs.zid.sa Account groups")

# ---------- commerce concerns: API group, plan line, scope and webhook ----------
def commerce(c, crumb, plan_lines, scope_slug, webhook=None, perm=None, reason_route=""):
    S(c, "where", LLMS, "API Docs", ST[LLMS], crumb, APIW(crumb))
    for (line, nth) in plan_lines:
        S(c, "decides", CHUNK, "compare-plans", ST[CHUNK], line, PL(line, nth), scope=PLAN_SCOPE, note=PLAN_NOTE)
    if perm: PERM(c, perm)
    GEN(c)
    if scope_slug:
        S(c, "boundary", D(scope_slug), "Scopes", struct(D(scope_slug)), EP(scope_slug), SCOPEQ(scope_slug))
    if webhook:
        wh = open(F + "/docs/webhooks.md", encoding="utf-8").read()
        m = re.search(r"^\| (" + re.escape(webhook) + r") \| ([^|]+?) \|", wh, re.M)
        S(c, "boundary", D("webhooks"), "Merchant Events", struct(D("webhooks"), "Webhooks Overview"), webhook, f"{m.group(1)} | {m.group(2).strip()}")
    PNR(c, "reason", "A stated reason for this concern's placement", reason_route)

commerce("ZD-C-080", "Merchant APIs > Orders", [("Order Tags", 0), ("Draft Orders", 0)], "list-of-orders", None, "edit.store.orders",
         "help.zid.sa category الطلبات (20 articles; e.g. حالات الطلب وتغييرها (لوحة التحكم الجديدة ))")
S("ZD-C-080", "where", D("list-of-orders"), "description", struct(D("list-of-orders"), "List Orders"), EP("list-of-orders"),
  "Orders can be created either by the customers from the storefronts or by the merchants from their dashboard.")
S("ZD-C-080", "decides", LLMS, "API Docs", ST[LLMS], "Change Order Status", APIW("Merchant APIs > Orders", "Change Order Status"))
S("ZD-C-080", "boundary", D("webhooks"), "Order Events", struct(D("webhooks"), "Webhooks Overview"), "order.create",
  "order.create [(Supports `conditions`)](#event-conditions) | Triggered when a new order is created.")
S("ZD-C-080", "boundary", D("create-order-20612055e0"), "Scopes", struct(D("create-order-20612055e0"), "Create Order"), EP("create-order-20612055e0"), SCOPEQ("create-order-20612055e0"))

commerce("ZD-C-081", "Merchant APIs > Reverse Orders", [("Full & Partial Returns", 0), ("Returned Orders", 0)], "create-reverse-orders", None, None,
         "help.zid.sa articles استرجاع الطلبات (لوحة التحكم الجديدة ); استرجاع جزئي للطلبات ( لوحة التحكم الجديدة )")
S("ZD-C-081", "boundary", LLMS, "API Docs", ST[LLMS], "Upload bank transfer receipt", APIW("Merchant APIs > Reverse Orders", "Upload bank transfer receipt"))
commerce("ZD-C-082", "Merchant APIs > Abandoned Carts", [("Abandoned Cart Details", 0)], "list-abandoned-carts", "abandoned_cart.created", "manage.store.abandonedcarts",
         "help.zid.sa articles السلات المتروكة ( لوحة التحكم الجديدة ); تنبيهات زد ( لوحة التحكم الجديدة )")
commerce("ZD-C-083", "Merchant APIs > Products > Managing Products", [("Add Products", 0), ("Product Management - Bulk Add Products", 0)], "create-a-new-product", "product.create", "list.store.products",
         "help.zid.sa category المنتجات (33 articles)")
commerce("ZD-C-084", "Merchant APIs > Products > Product Categories", [("Product Categories", 0)], "set-categories-nesting-42347136e0", "category.create", "list.store.categories",
         "help.zid.sa articles إضافة تصنيف ( لوحة التحكم الجديدة ); ترتيب التصنيفات ( لوحة التحكم الجديدة )")
commerce("ZD-C-085", "Merchant APIs > Inventories", [("Inventory Management", 0), ("Inventory Withdrawal Priority", 0)], "add-a-new-location", None, "manage.store.inventory.addresses",
         "help.zid.sa articles عناوين المخزون ( لوحة التحكم الجديدة ); أولوية السحب من المخزون ( لوحة التحكم الجديدة )")
S("ZD-C-085", "decides", PRICING, "plan card Growth", ST[PRICING], "Growth: All features of Rise package, plus:", "Inventory management across 2 branches or warehouses", scope="plan Growth")
S("ZD-C-085", "responsible", H("faq-24"), "answer", struct(H("faq-24"), "FAQ: هل تقومون بتخزين منتجاتي؟"), "خدمات التعهيد",
  "زد لا يقوم بتخزين منتجات التجار .. ولكن وفرنا خدمات التعهيد اللي يقدمون خدمات تخزين وتجهيز وغيره")
commerce("ZD-C-086", "Merchant APIs > Products > Product Questions & Answers", [("Review Management", 0), ("Q&A and Review Messages", 0)], "get-questions", None, None,
         "help.zid.sa articles أسئلة العملاء ( لوحة التحكم الجديدة ); تقييمات العملاء ( لوحة التحكم الجديدة )")
commerce("ZD-C-087", "Merchant APIs > Products > Product Availability Notifications", [("Product Availability Notification", 0)], "availability-notification-stats", None, None,
         "help.zid.sa article إشعارات توفر المخزون (تذكيرات الشراء)")
commerce("ZD-C-088", "Merchant APIs > Marketing > Coupons", [("Add Discount Coupons", 0), ("Card Discount", 0)], "list-coupons-13955120e0", None, "manage.store.coupons",
         "help.zid.sa articles انشاء خصم – كود او تلقائي (لوحة التحكم الجديدة); خصومات البنك (لوحة التحكم الجديدة)")
commerce("ZD-C-089", "Merchant APIs > Marketing > Bundle Offers", [("Add Dynamic Bundle", 0)], "retrieve-all-bundle-offers", None, "manage.store.bundleoffers",
         "help.zid.sa articles إنشاء حزمة مرنة ( لوحة التحكم الجديدة ); الحزم التسويقية")
commerce("ZD-C-090", "Merchant APIs > Marketing > Loyalty Program", [("Loyalty Programs", 0)], "loyalty-status", None, None,
         "help.zid.sa article برنامج الولاء ( لوحة التحكم الجديدة )")
S("ZD-C-090", "decides", PRICING, "plan card Professional", ST[PRICING], "Professional: Standout Features", "Complete loyalty program to increase customer retention", scope="plan Professional")
commerce("ZD-C-091", "Merchant APIs > Customers", [("Customer Information", 0), ("Block Customers", 0)], "list-of-customers", "customer.create", "list.store.customers",
         "help.zid.sa category العملاء (13 articles)")
S("ZD-C-091", "responsible", EN_PRIV, "As the Merchants", ST[EN_PRIV], "as directed by you",
  "To support your business, we collect and use personal information about your customers. Generally, we do this as directed by you.")

# ---------- ZD-C-092 Customer self-service portal ----------
c = "ZD-C-092"
S(c, "where", "https://c.zid.sa/ar-sa", "page", "Zid stores' customer self-service portal (c.zid.sa)", "بوابة خدمة العملاء الذاتية", "بوابة خدمة العملاء الذاتية")
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Customers > Customer Portal Tickets", APIW("Merchant APIs > Customers > Customer Portal Tickets"))
OBS(c, "decides", "Which plans or settings turn the self-service portal on for a store", "help.zid.sa article بوابة خدمة العملاء الذاتيه (لوحة التحكم الجديدة); dashboard")
GEN(c)
S(c, "boundary", AR_TERMS, "آلية التعامل مع الشكاوى والبلاغات", ST[AR_TERMS], "الرابط المخصص",
  "في حال ورود شكوى بحق إحدى المتاجر أو مزودي الخدمات، يُرجى التقدم بالشكوى عبر الرابط المخصص لذلك في موقع زد، أو التواصل مع فريق الدعم لاتخاذ ما يلزم.")
PNR(c, "reason", "A stated reason for the self-service portal placement", "help.zid.sa article بوابة خدمة العملاء الذاتيه (لوحة التحكم الجديدة)")

# ---------- ZD-C-093 Blogs ----------
c = "ZD-C-093"
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Blogs > Posts", APIW("Merchant APIs > Blogs > Posts"))
OBS(c, "decides", "Which plans or permissions turn the blog on", "help.zid.sa article المدونة ( لوحة التحكم الجديدة)")
GEN(c)
S(c, "boundary", D("list-38273360e0"), "path", struct(D("list-38273360e0"), "Blogs > Posts > List"), EP("list-38273360e0"), "/v2/blogs/posts/:",
  note="The blog endpoints show no scopes accordion.")
PNR(c, "reason", "A stated reason for the blog placement", "help.zid.sa articles المدونة ( لوحة التحكم الجديدة); تطبيق المدونة | Blog ( لوحة التحكم الجديدة )")

# ---------- ZD-C-094 Team members and permissions ----------
c = "ZD-C-094"
S(c, "where", H("team-member"), "intro", struct(H("team-member"), "فريق العمل (لوحة التحكم الجديدة )"), "فريق العمل",
  "يمكنك الوصول الى خاصية الفريق من خلال : لوحة التحكم > الضغط على أيقونة الاعدادات .")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Add Team Members", PL("Add Team Members"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", ROLES, "Important Notes", ROLES_ST, "permissions tied to role", "Please note that all permissions are tied to the user's role in the system.")
GEN(c)
S(c, "boundary", ROLES, "User Roles", ROLES_ST, "Role: Manager",
  "When interacting with the API, set the **`Role`** header in the request to **`Manager`** to perform operations as a store owner or other staff members.")
S(c, "reason", ROLES, "Important Notes", ROLES_ST, "security and consistency", "This design ensures the security and consistency of your store's operations.")

# ---------- ZD-C-095 Security settings ----------
SEC = "https://help.zid.sa/%d8%a7%d8%b9%d8%af%d8%a7%d8%af%d8%a7%d8%aa-%d8%a7%d9%84%d8%a7%d9%85%d8%a7%d9%86-%d9%84%d9%88%d8%ad%d8%a9-%d8%a7%d9%84%d8%aa%d8%ad%d9%83%d9%85-%d8%a7%d9%84%d8%ac%d8%af%d9%8a%d8%af%d8%a9/"
c = "ZD-C-095"
S(c, "where", SEC, "intro", struct(SEC, "اعدادات الامان (لوحة التحكم الجديدة )"), "تفعيل التحقق بخطوتين", "لتفعيل الخاصية، انتقل إلى خانة تفعيل التحقق بخطوتين واضغط على أيقونة حفظ.")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Security Settings", PL("Security Settings"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", SEC, "إدارة الجلسات", struct(SEC, "اعدادات الامان (لوحة التحكم الجديدة )"), "عالي",
  "عالي : تسجيل خروج اي عضو من دون نشاط بعد نص ساعة مع امكانية تسجيل الدخول من متصفح واحد فقط")
GEN(c)
S(c, "boundary", SEC, "إدارة الجلسات", struct(SEC, "اعدادات الامان (لوحة التحكم الجديدة )"), "Zapier; API",
  "و قد يؤثر هذا الإجراء على ربط Zapier وأي ربط آخر عبر API.")
S(c, "reason", SEC, "intro", struct(SEC, "اعدادات الامان (لوحة التحكم الجديدة )"), "التحقق بخطوتين (2FA)",
  "مما يعزز مستوى الأمان ويحمي الحساب من محاولات الاختراق.")

# ---------- ZD-C-096 Domains ----------
c = "ZD-C-096"
S(c, "where", H("domain"), "intro", struct(H("domain"), "قائمة النطاقات (لوحة التحكم الجديدة )"), "قائمة النطاقات",
  "يمكنك الوصول إلى قائمة النطاقات من خلال : لوحة التحكم > الضغط على أيقونة الإعدادات")
S(c, "decides", H("domain"), "نطاق مجاني", struct(H("domain"), "قائمة النطاقات (لوحة التحكم الجديدة )"), "النمو والباقة الاحترافية",
  "إذا كنت على باقة تدعم طلب نطاق مجاني مثل النمو والباقة الاحترافية بإمكانك التوجه لأسفل الصفحة والبحث عن نطاق متاح من خلال محرك البحث:", scope="النمو; الباقة الاحترافية")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Custom Domain Linking", PL("Custom Domain Linking"), scope=PLAN_SCOPE, note=PLAN_NOTE)
PERM(c, "manage.store.custom.domain")
S(c, "responsible", AR_TERMS, "أسماء النطاقات (رابط المتجر)", ST[AR_TERMS], "خدمات الطرف الثالث",
  "يقر التاجر بتحمل مسؤولية شراء النطاق (الرابط) وتنشيطه وتعطيله بناءً على رغبته.")
S(c, "boundary", AR_TERMS, "أسماء النطاقات (رابط المتجر)", ST[AR_TERMS], "zid.store",
  "تتيح زد للتاجر خاصية النطاقات الفرعية تحت عنوان “zid.store” للمتجر الخاص به والتي بإمكانه استخدامها ومشاركتها مع المستهلكين.")
SNF(c, "reason", "A stated reason for the domain placement", "help.zid.sa/domain/; help.zid.sa/buy-new-domain/; zid.sa/ar/legal/terms-conditions/ (أسماء النطاقات)")

# ---------- ZD-C-097 Notifications and order status messages ----------
c = "ZD-C-097"
S(c, "where", H("order-status-messages"), "intro", struct(H("order-status-messages"), "رسائل حالات الطلب ( لوحة التحكم الجديدة )"), "الاعدادات > التواصل > رسائل الطلبات",
  "لتفعيل رسائل حالات الطلب من خلال : الاعدادات > التواصل > رسائل الطلبات")
S(c, "decides", CHUNK, "compare-plans group Other", ST[CHUNK], "Team Notifications", PL("Team Notifications"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", H("order-status-messages"), "الرصيد", struct(H("order-status-messages"), "رسائل حالات الطلب ( لوحة التحكم الجديدة )"), "رصيد حالات الطلب",
  "في حال عدم توفر رصيد سيتم إرسال الرسائل عن طريق البريد الالكتروني للعميل ، ولشراء رصيد حالات الطلب من خلال إدارة الاشتراك>الإضافات")
PERM(c, "manage.store.staff.notifications")
GEN(c)
S(c, "boundary", D("onesignal-store-settings-39420053e0"), "Scopes", struct(D("onesignal-store-settings-39420053e0"), "OneSignal Store Settings"), EP("onesignal-store-settings-39420053e0"), SCOPEQ("onesignal-store-settings-39420053e0"))
SNF(c, "reason", "A stated reason for the notifications placement", "help.zid.sa/order-status-messages/; help.zid.sa/team-notification/; help.zid.sa/zid-reminder/")

# ---------- ZD-C-098 Sender name ----------
c = "ZD-C-098"
S(c, "where", H("senderid"), "طريقة تفعيل خدمة اسم المرسل", struct(H("senderid"), "تفعيل اسم المرسل ( لوحة التحكم الجديدة )"), "صفحة الاشتراكات",
  "بعد شراء الخدمة من صفحة الاشتراكات، سيتم التواصل معكم عبر البريد الإلكتروني المسجّل لدينا في زد، حيث سيُرسل لكم نموذج مخصص لتعبئته.")
S(c, "decides", CHUNK, "compare-plans group Other", ST[CHUNK], "Sender Name", PL("Sender Name"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", H("senderid"), "طريقة تفعيل خدمة اسم المرسل", struct(H("senderid"), "تفعيل اسم المرسل ( لوحة التحكم الجديدة )"), "هيئة الاتصالات وتقنية المعلومات",
  "وبعد استلام النموذج، سيتولى الفريق المختص من طرفهم برفع الطلب نيابةً عنكم، وذلك بعد التأكد من استيفاء جميع متطلبات هيئة الاتصالات وتقنية المعلومات.")
S(c, "responsible", H("senderid"), "ملاحظة", struct(H("senderid"), "تفعيل اسم المرسل ( لوحة التحكم الجديدة )"), "الغرفة التجارية",
  "للشركات و المؤسسات الخاصة بعد تعبئة خطاب التفويض يجب تصديقه من الغرفة التجارية حسب شروط هيئة الاتصالات")
S(c, "boundary", H("senderid"), "5. تفويض", struct(H("senderid"), "تفعيل اسم المرسل ( لوحة التحكم الجديدة )"), "ينيفونك",
  "الغرض هو تفويض  (زد) للتواصل مع (ينيفونك )في كل ما يخص اسم المرسل أو باقات الرسائل الخاصة بك", note="Names the messaging partner.")
SNF(c, "reason", "A stated reason for routing sender names through the messaging partner", "help.zid.sa/senderid/; help.zid.sa sender name renewal article")

# ---------- ZD-C-099 Checkout page settings ----------
c = "ZD-C-099"
S(c, "where", H("checkout-page-options"), "intro", struct(H("checkout-page-options"), "إعدادات صفحة إتمام عملية الشراء ( لوحة التحكم الجديدة )"), "لوحة التحكم > الاعدادات",
  "يمكنك الوصول إلى خيارات صفحة إتمام الشراء من خلال : لوحة التحكم > الاعدادات")
OBS(c, "decides", "Which plans or permissions turn checkout options on", "dashboard: لوحة التحكم > الاعدادات (صفحة إتمام الشراء)")
GEN(c)
S(c, "boundary", LLMS, "API Docs", ST[LLMS], "API's > Checkout", APIW("API's > Checkout"))
SNF(c, "reason", "A stated reason for the checkout settings placement", "help.zid.sa/checkout-page-options/")

# ---------- simple settings concerns ----------
def setting(c, url, title, ident, where_text, decides=None, boundary=None, reason=None, reason_ident=""):
    S(c, "where", url, "intro", struct(url, title), ident, where_text)
    if decides: S(c, "decides", *decides)
    else: OBS(c, "decides", "Which plans or staff permissions turn it on", url.replace("https://", ""))
    GEN(c)
    if boundary: S(c, "boundary", *boundary)
    else: SNF(c, "boundary", "An API endpoint, scope or webhook for it", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names it.")
    if reason: S(c, "reason", url, "intro", struct(url, title), reason_ident, reason)
    else: SNF(c, "reason", "A stated reason for its placement", url.replace("https://", ""))

setting("ZD-C-100", H("orders-properties"), "خصائص الطلبات والمنتجات | الطلبات ( لوحة التحكم الجديدة )", "خصائص الطلبات والمنتجات",
        "للوصول الى خصائص الطلبات والمنتجات من خلال : لوحة التحكم > الضغط على أيقونة الاعدادات",
        decides=(CHUNK, "compare-plans group Other", ST[CHUNK], "Custom Fields", PL("Custom Fields"), PLAN_SCOPE, PLAN_NOTE),
        boundary=(LLMS, "API Docs", ST[LLMS], "List Product Settings", APIW("Merchant APIs > Products > Managing Products", "List Product Settings")))
S("ZD-C-100", "decides", H("product-properties"), "حجز المنتج", struct(H("product-properties"), "خصائص الطلبات والمنتجات | المنتجات ( لوحة التحكم الجديدة )"), "حجز المنتج 30 دقيقة",
  "عند إضافة المنتج للسلة من قبل العميل وتأكيد عملية الشراء من خلال الدفع الإلكتروني و الانتقال إلى صفحة إدخال معلومات البطاقة سوف يتم حجز المنتج بشكل تلقائي لمدة 30 دقيقة")
setting("ZD-C-101", H("gift-feature"), "خاصية الإهداء ( لوحة التحكم الجديدة )", "خاصية الإهداء",
        "بإمكانك تفعيل خاصية الإهداء من خلال: لوحة التحكم > الضغط على أيقونة الأعدادات .")
setting("ZD-C-102", H("settings-url-redirects"), "خاصية إعادة توجيه الروابط ( لوحة التحكم الجديدة)", "لوحة التحكم > الإعدادات > إعادة توجيه الروابط",
        "يمكنك الوصول للخاصية من خلال: لوحة التحكم > الإعدادات > إعادة توجيه الروابط",
        reason="عند انتقالك إلى زد من منصة أخرى، قد تحتاج لإضافة عدد كبير من عمليات إعادة التوجيه دفعة واحدة.", reason_ident="الانتقال من منصة أخرى")
setting("ZD-C-103", H("google-maps-2"), "تفعيل Google maps ( لوحة التحكم الجديدة )", "تفعيل Google maps",
        "بإمكانك تفعيل خرائط جوجل في متجرك الإلكتروني بشكل مباشر من خلال : لوحة التحكم > الضغط على أيقونة الإعدادات .")
setting("ZD-C-104", H("working-hours"), "اوقات العمل الرسمية (لوحة التحكم الجديدة )", "الاعدادات > المتجر > أوقات العمل الرسمية",
        "يمكنك التحكم بأوقات العمل و إغلاق المتجر بشكل كلي مؤقتاً من خلال: الاعدادات > المتجر > أوقات العمل الرسمية")

# ---------- product lines and help-centre products ----------
c = "ZD-C-105"
S(c, "where", HOME, "category grid", "help.zid.sa home, دليل استخدام منصة التاجر", "التحليلات", "بيانات تحليلية توضّح أداء المتجر وتدعم اتخاذ القرار")
S(c, "decides", CHUNK, "compare-plans group Reports & Analytics", ST[CHUNK], "Reports - Total Profit", PL("Reports - Total Profit"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Reports & Analytics", ST[CHUNK], "Visit Count", PL("Visit Count"), scope=PLAN_SCOPE, note=PLAN_NOTE)
PERM(c, "view.store.dashboard")
GEN(c)
SNF(c, "boundary", "An analytics API group, scope or webhook", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; only Get Orders Highlights returns summary figures, and no analytics group exists.")
PNR(c, "reason", "A stated reason for the analytics placement", "help.zid.sa category التحليلات (13 articles)")

c = "ZD-C-106"
S(c, "where", NAV, "header menu Solutions", "zid.sa header menu Solutions", "Marketing Tools", "Marketing ToolsTurn Your Store into a Customer Magnet")
S(c, "decides", CHUNK, "compare-plans group Marketing & Growth Tools", ST[CHUNK], "Add Marketing Affiliates", PL("Add Marketing Affiliates"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Marketing & Growth Tools", ST[CHUNK], "Create New Campaign", PL("Create New Campaign"), scope=PLAN_SCOPE, note=PLAN_NOTE)
PERM(c, "manage.store.marketing")
GEN(c)
SNF(c, "boundary", "An API group, scope or webhook for campaigns, affiliates or SMS", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; coupons, bundles and loyalty have groups, campaigns and affiliates do not.")
PNR(c, "reason", "A stated reason for the marketing tools placement", "help.zid.sa category التسويق (32 articles); zid.sa/en/solutions/marketing-tools/")

c = "ZD-C-107"
S(c, "where", HOME, "category grid", "help.zid.sa home, دليل استخدام منصة التاجر", "واتساب زد", "تجربة واتساب متكاملة داخل متجرك، والقناة الأمثل للتواصل مع عملائك.")
S(c, "decides", PRICING, "plan card Rise", ST[PRICING], "Rise: All features of Starter package, plus:", "Free WhatsApp (Basic Plan)", scope="plan Rise")
S(c, "decides", PRICING, "plan card Professional", ST[PRICING], "Professional: Standout Features", "Completely free WhatsApp", scope="plan Professional")
PNR(c, "responsible", "Which party holds the WhatsApp Business account and its terms (Zid or the merchant)", "help.zid.sa articles التقييد والحظر على حافظة الأعمال; الفرق بين تطبيق واتساب أعمال والواتساب المؤسسي API")
PNR(c, "boundary", "The WhatsApp interface Zid uses (API or app) and its provider", "help.zid.sa articles تحويل رقم واتساب زد إلى WhatsApp API; الفرق بين تطبيق واتساب أعمال والواتساب المؤسسي API")
PNR(c, "reason", "A stated reason for the WhatsApp placement", "help.zid.sa category واتساب زد (32 articles)")

c = "ZD-C-108"
S(c, "where", AR_TERMS, "زد كاشير: التعريفات", ST[AR_TERMS], "زد كاشير (definition)",
  "زد كاشير: هي خدمة تقدمها زد تمكن التاجر من ربط بيانات المعارض التجارية الخاصة بالتاجر ببيانات متجره الإلكتروني في منصة واحدة")
S(c, "where", H("connect-payment-device"), "steps", struct(H("connect-payment-device"), "خطوات ربط جهاز الدفع بتطبيق زد كاشير ( لوحة التحكم الجديدة )"), "تطبيق زد كاشير > الاعدادات > ربط جهاز الدفع",
  "تطبيق زد كاشير > الاعدادات > ربط جهاز الدفع")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Mobile & Tablet POS App", PL("Mobile & Tablet POS App"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", PRICING, "plan card Professional", ST[PRICING], "Professional: Standout Features", "Completely free Zid POS - two cashiers", scope="plan Professional")
PERM(c, "pos.payment.methods")
S(c, "responsible", AR_TERMS, "زد كاشير: آلية التنفيذ وحدود المسؤولية", ST[AR_TERMS], "تركيب أجهزة نقاط البيع", "يقر ويوافق التاجر على أن زد لا تتحمل مسؤولية تركيب أجهزة نقاط البيع.")
S(c, "responsible", AR_TERMS, "زد كاشير: عروض", ST[AR_TERMS], "ضمان الأجهزة", "يتحمل الوكيل مسؤولية ضمان الأجهزة.")
S(c, "boundary", AR_TERMS, "زد كاشير: التعريفات", ST[AR_TERMS], "أجهزة نقاط البيع",
  "أجهزة نقاط البيع: هي أجهزة تمكن التاجر من الإشراف، والمتابعة على جميع عمليات متجره في منصة واحدة متنقلة بما في ذلك المبيعات، والمخزون، وتسوية فورية للمعاملات المالية وقبول جميع طرق الدفع.")
S(c, "boundary", H("faq-17"), "answer", struct(H("faq-17"), "FAQ: هل الفواتير متطابقة مع متطلبات هيئة الزكاة والضريبة؟"), "فوترة إلكترونية",
  "نعم ، كفوترة إلكترونية مع العلم أن زد حاصلة على جوائز واعتماد من الهيئة")
ASK(c, "responsible", "Which acquirer or payment provider settles card payments taken on Zid POS payment devices", "help.zid.sa/connect-payment-device/; zid.sa/ar/legal/terms-conditions/ (زد كاشير)")
SNF(c, "reason", "A stated reason for the POS placement", "zid.sa/ar/legal/terms-conditions/ (زد كاشير); help.zid.sa/about_zidpos/")

c = "ZD-C-109"
S(c, "where", AR_TERMS, "مزيد", ST[AR_TERMS], "مزيد (definition)",
  "مزيد هي  منصة/تطبيق للتجارة الإلكترونية تتيح للمستخدمين من تجار زد عرض وبيع المنتجات، كما تتيح للعملاء تسوق مجموعة متنوعة من هذه المنتجات المعروضة.")
S(c, "where", H("activate-mazeed"), "steps", struct(H("activate-mazeed"), "تفعيل مزيد ( لوحة التحكم الجديدة )"), "منصات البيع",
  "لوحة التحكم > منصات البيع > تفعيل منصة البيع > ربط منصات البيع .")
S(c, "decides", AR_TERMS, "مزيد: شروط تفعيل الخدمة للتجار", ST[AR_TERMS], "مشترك بأحد الباقات", "يجب أن يكون لديك متجر على منصة زد، ومشترك بأحد الباقات.")
S(c, "decides", AR_TERMS, "مزيد: شروط تفعيل الخدمة للتجار", ST[AR_TERMS], "أنظمة المملكة العربية السعودية",
  "يجب أن يكون نشاط التاجر صحيح، ولا يخدم أي من النشاطات المحظورة حسب أنظمة المملكة العربية السعودية.")
S(c, "decides", H("faq-8"), "answer", struct(H("faq-8"), "FAQ: هل مزيد متاح لتجار الخليج؟"), "تجار الخليج", "نعم متاح لجميع متاجر زد.")
S(c, "responsible", AR_TERMS, "مزيد: مسؤوليات وإقرارات التاجر", ST[AR_TERMS], "الممثل القانوني للبائع",
  "يقر التاجر بكامل أهليته المعتبرة شرعا وقانونا بموجب هذه الشروط والأحكام بتفويض زد متمثلة في منصة \"مزيد\" على اعتبار أنها الممثل القانوني للبائع أمام الأطراف التجارية الأخرى التي قد تتعامل مع البائع، بما في ذلك على سبيل المثال لا الحصر منصات التجارة الإلكترونية الأخرى أو شركات الشحن أو المزودين مثل منصة PIK.",
  quote="يقر التاجر بكامل أهليته المعتبرة شرعا وقانونا بموجب هذه الشروط والأحكام بتفويض زد متمثلة في منصة \"مزيد\" على اعتبار أنها الممثل القانوني للبائع أمام الأطراف التجارية الأخرى")
S(c, "responsible", AR_TERMS, "مزيد: مسؤوليات وإقرارات التاجر", ST[AR_TERMS], "شحن وتوصيل الطلب", "يتحمل التاجر مسؤولية شحن، و توصيل الطلب إلى العميل النهائي")
S(c, "boundary", AR_TERMS, "مزيد: مسؤوليات وإقرارات التاجر", ST[AR_TERMS], "إضافة المنتجات بشكل تلقائي",
  "يقر التاجر ويوافق على إضافة منتجات متجره إلى منصة \"مزيد\" بشكل تلقائي، بحيث تظهر منتجاته المتوفرة في متجره على منصة \"مزيد\" دون الحاجة إلى أي إجراء إضافي من قبله")
S(c, "boundary", AR_TERMS, "مزيد: مسؤوليات وحقوق زد", ST[AR_TERMS], "بيانات عملاء التاجر",
  "يحق لشركة زد الاطلاع على بيانات عملاء التاجر على سبيل المثال (العمليات الشرائية )، وذلك بغرض التقييم وتحسين تجربة العميل الشرائية في مزيد.")
S(c, "reason", AR_TERMS, "مزيد: مسؤوليات وحقوق زد", ST[AR_TERMS], "بغرض التقييم", "وذلك بغرض التقييم وتحسين تجربة العميل الشرائية في مزيد.",
  note="The stated reason for Zid's access to the merchant's customer data on Mazeed.")

c = "ZD-C-110"
S(c, "where", NAV, "header menu Solutions", "zid.sa header menu Solutions", "Marketplaces", "MarketplacesSold on Amazon and Trendyol and Jahez")
S(c, "decides", H("faq-29"), "answer", struct(H("faq-29"), "FAQ: كيف طريقة التحصيل؟ وكم النسبة مع جاهز ؟"), "جاهز", "عن طريق مزيد لا يوجد تغيير.", scope="جاهز",
  note="Collection for Jahez orders is stated as going through Mazeed.")
GEN(c)
S(c, "boundary", D("list-of-orders"), "Data Masking for Marketplace Orders", struct(D("list-of-orders"), "List Orders"), "is_marketplace_order",
  "When `is_marketplace_order` is true, the order is from an external provider, and certain customer information, such as `customer.name`, `customer.email`, and `customer.phone`, will be masked for privacy.")
S(c, "reason", D("list-of-orders"), "Data Masking for Marketplace Orders", struct(D("list-of-orders"), "List Orders"), "masked for privacy",
  "When `is_marketplace_order` is true, the order is from an external provider, and certain customer information, such as `customer.name`, `customer.email`, and `customer.phone`, will be masked for privacy.",
  note="The reason stated for masking customer data on marketplace orders.")
PNR(c, "responsible", "Which party contracts with Amazon, Trendyol and Jahez for the merchant, and who collects payment", "help.zid.sa articles عن قنوات البيع ( لوحة التحكم الجديدة); ربط جاهز (لوحة التحكم الجديدة ); zid.sa/en/marketplace/")

c = "ZD-C-111"
ASSUR = "https://zid.sa/en/zid-assurance/"
S(c, "where", H("faq-zid-warranty"), "FAQ", struct(H("faq-zid-warranty"), "الأسئلة الشائعة لضمان زد"), "صفحة إتمام الشراء > ضمان زد",
  "كيف يمكن الغاء برنامج ضمان زد كتاجر؟من خلال لوحة التحكم > الإعدادات > صفحة إتمام الشراء > ضمان زد")
S(c, "decides", ASSUR, "Zid Assurance: Optional Protection for Your Orders", "product page Zid Assurance (zid.sa/en/zid-assurance)", "100% optional",
  "A 100% optional service that we don't impose on anyone")
S(c, "responsible", ASSUR, "Customer Service at No Cost", "product page Zid Assurance (zid.sa/en/zid-assurance)", "entirely on Zid",
  "The service is entirely on Zid and we cover all costs of sending order status updates to customers and handle any complaints or inquiries")
S(c, "boundary", ASSUR, "hero", "product page Zid Assurance (zid.sa/en/zid-assurance)", "WhatsApp updates; badge",
  "A free program from Zid that sends your customers real-time order updates via WhatsApp, and adds the \"Zid Assurance\" badge to your store")
S(c, "reason", ASSUR, "Why did we launch \"Zid Assurance\"", "product page Zid Assurance (zid.sa/en/zid-assurance)", "Ministry of Commerce",
  "After collaborating with the Ministry of Commerce in processing complaints with merchants and helping them resolve them, we noticed that many cases could have been resolved before reaching any escalation.")

c = "ZD-C-112"
S(c, "where", NAV, "header menu Solutions", "zid.sa header menu Solutions", "Zid Voice", "Zid VoiceRecover abandoned carts with a voice agent")
PNR(c, "decides", "Which plans or add-ons turn Zid Voice on", "help.zid.sa article زد فويس")
PNR(c, "responsible", "Who provides the voice agent and under which terms", "help.zid.sa article زد فويس")
PNR(c, "boundary", "How Zid Voice reaches abandoned carts (API, channel, provider)", "help.zid.sa article زد فويس")
PNR(c, "reason", "A stated reason for the Zid Voice placement", "help.zid.sa article زد فويس")

c = "ZD-C-113"
S(c, "where", NAV, "header menu Solutions", "zid.sa header menu Solutions", "E-store", "E-storeTurn Your Idea into a Thriving E-Store")
S(c, "decides", CHUNK, "compare-plans group Store Design", ST[CHUNK], "Store - SDK Template Design (Up to 2)", PL("Store - SDK Template Design (Up to 2)"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "CSS interface customization", PL("CSS interface customization"), scope=PLAN_SCOPE, note=PLAN_NOTE)
PERM(c, "manage.store.front.customization")
GEN(c)
S(c, "boundary", LLMS, "API Docs", ST[LLMS], "API's > Storefront", APIW("API's > Storefront"))
PNR(c, "reason", "A stated reason for the store design placement", "help.zid.sa category تصميم المتجر (8 articles); zid.sa/en/solutions/e-store/")

c = "ZD-C-114"
S(c, "where", CHUNK, "compare-plans group Other", ST[CHUNK], "Ticketing & Chat System", PL("Ticketing & Chat System"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Live Chat Support", PL("Live Chat Support"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", PRICING, "plan card Professional", ST[PRICING], "Professional: Standout Features", "24/7 priority support", scope="plan Professional")
GEN(c)
SNF(c, "boundary", "An API or channel through which support is reached by apps", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names merchant support.")
PNR(c, "reason", "A stated reason for the support placement", "help.zid.sa article تذاكر الدعم ( لوحة التحكم الجديدة )")

c = "ZD-C-115"
S(c, "where", HOME, "منتجات وخدمات زد", "help.zid.sa home, منتجات وخدمات زد", "زد نمو", "تعاون مع حلول زد لتطوير وتحسين نشاطك التجاري، وابرز الأسئلة الشائعة حول حلول زد.")
PERM(c, "manage.store.ecosystem.packaging")
PNR(c, "responsible", "Who provides Zid Growth services (Zid or partners) and under which terms", "help.zid.sa article عن زد نمو ( لوحة التحكم الجديدة )")
SNF(c, "boundary", "An API group, scope or webhook for Zid Growth services", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names Zid Growth.")
PNR(c, "reason", "A stated reason for the Zid Growth placement", "help.zid.sa article عن زد نمو ( لوحة التحكم الجديدة )")

c = "ZD-C-116"
S(c, "where", HOME, "منتجات وخدمات زد", "help.zid.sa home, منتجات وخدمات زد", "تطبيق الجوال", "تعرّف على متطلبات تطبيق الجوال للمتاجر، وخصائص التطبيق والأسئلة الشائعة حوله")
PERM(c, "manage.store.ecosystem.mobileapps")
PNR(c, "responsible", "Who publishes the store's mobile app and under whose developer account", "help.zid.sa articles عن تطبيق الجوال ( لوحة التحكم الجديدة ); الاشتراك بخدمة تطبيق الجوال ( لوحة التحكم الجديدة )")
PNR(c, "boundary", "How the store mobile app connects to the store (API, scripts)", "help.zid.sa article عن تطبيق الجوال ( لوحة التحكم الجديدة ); docs.zid.sa Mobile Apps pages")
PNR(c, "reason", "A stated reason for the mobile app placement", "help.zid.sa article عن تطبيق الجوال ( لوحة التحكم الجديدة )")
