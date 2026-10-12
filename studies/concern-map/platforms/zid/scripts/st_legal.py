# Statements and gaps: legal entities, licences, sanctions and screening, data, currency and tax (ZD-C-030 to ZD-C-054).
from stlib import *
EGYPT = H("about-zid-egypt")

# ---------- ZD-C-030 Zid's contracting entity and governing law ----------
c = "ZD-C-030"
S(c, "where", AR_TERMS, "footer", ST[AR_TERMS], "footer: زد متاحة في",
  "Al-Qudrah Al-Taqniyah for Technology and Communication Company", note="The entity name as printed in the zid.sa footer, beside the country list (زد متاحة في).")
S(c, "decides", AR_TERMS, "النظام الحاكم وآلية حسم النزاعات", ST[AR_TERMS], "النظام الحاكم وآلية حسم النزاعات",
  "تخضع هذه الشروط والأحكام لأنظمة وقوانين المملكة العربية السعودية، وفي حال نشوء أي نزاع بين التاجر وزد أو فيما يتعلق بها (بما في ذلك النزاع المتعلق بأي التزامات غير تعاقدية ناشئة عنها أو فيما يتعلق بها) يجب حله وديًا من خلال التسوية الودية.")
S(c, "decides", AR_ZPKW, "الشروط العامة", ST[AR_ZPKW], "القانون الحاكم (الكويت)",
  "يخضع هذا العقد لقوانين المملكة العربية السعودية حيث تقدم زد باي خدماتها، وأي نزاع ينشأ بين التاجر وزد باي يندرج تنفيذه ضمن اختصاص محاكم تلك الدولة، في محاكم مدينة الرياض.",
  scope="Zid Pay, Kuwait", note="The Kuwait Zid Pay contract names Saudi law and the courts of Riyadh.")
S(c, "decides", AR_TERMS, "الأحكام العامة", ST[AR_TERMS], "النسخة المعتمدة",
  "ستكون شروط الاستخدام متاحة باللغتين العربية والإنجليزية. في حال وجود أي تضارب أو تناقض بين شروط الاستخدام الإنجليزية وشروط الاستخدام المتوفرة باللغة العربية، فإن النسخة العربية هي النسخة المعتمدة.")
S(c, "responsible", AR_TERMS, "opening", ST[AR_TERMS], "شركة القدرة التقنية لتقنية المعلومات والاتصالات ذ.م.م",
  "المملوكة لشركة القدرة التقنية لتقنية المعلومات والاتصالات ذ.م.م، سجل تجاري رقم (1010365366) (يُشار إليها فيما بعد باسم “نحن” أو “لنا” أو “زد”، حسب ما يقتضيه السياق) التي تقوم بإدارة الخدمات وتشغيلها.")
S(c, "responsible", AR_TERMS, "footer", ST[AR_TERMS], "رقم ضريبة القيمة المضافة", "رقم ضريبة القيمة المضافة 300827827900003")
S(c, "responsible", EN_PRIV, "INTRODUCTION", ST[EN_PRIV], "Al Qudrah Technical for Information and Communication Technology Company L.L.C",
  "This Privacy Policy provides you with information regarding the collection, processing, and use of your personal data by Al Qudrah Technical for Information and Communication Technology Company L.L.C (“Zid,” “we,” “us,” or “our”)",
  note="The English privacy policy names the entity differently from the Terms and the footer; recorded as found.")
S(c, "responsible", AR_ZPKW, "opening", ST[AR_ZPKW], "العقد المبرم (الكويت)", "تمثل الشروط والأحكام المذكورة أدناه العقد المبرم بين مستخدمي زد باي وشركة زد.", scope="Zid Pay, Kuwait")
S(c, "responsible", PAYOUTS, "The invoice: what it must include", ST[PAYOUTS], "Zid's legal name",
  "Zid's legal name in Arabic and English: شركة القدرة التقنية لتقنية المعلومات والاتصالات / Al-Qudrah Al-Taqniyah for Technology and Communication Company.",
  scope="partner payout invoices")
SNF(c, "responsible", "Whether Zid has separate legal entities for the Gulf countries it serves (Kuwait, UAE, Oman, Bahrain, Qatar), as it states for Egypt",
    "zid.sa/ar/legal/terms-conditions/; zid.sa/ar/legal/zidpay-terms-conditions-kw/; zid.sa/en/kuwait/; zid.sa/en/uae/; zid.sa/en/oman/; help.zid.sa/gcc-merchants/",
    why="The pages in the route were read; only Egypt has a stated separate registration (help.zid.sa/about-zid-egypt/).")
SNF(c, "boundary", "An API field or endpoint naming the contracting entity", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names the contracting entity.")
SNF(c, "reason", "A stated reason for Saudi law governing contracts with merchants outside Saudi Arabia", "zid.sa/ar/legal/terms-conditions/; zid.sa/ar/legal/zidpay-terms-conditions-kw/")

# ---------- ZD-C-031 Zid Egypt ----------
c = "ZD-C-031"
S(c, "where", EGYPT, "About Zid Egypt", struct(EGYPT, "حول زد مصر"), "Zid Egypt",
  "Zid has expanded its operations to Egypt as part of its regional growth strategy, empowering merchants with advanced e-commerce solutions tailored to the local market.")
S(c, "where", "https://zid.sa/en/egypt/", "hero", "country page Egypt (zid.sa/en/egypt)", "Egypt", "Join thousands of merchants in Egypt and launch your online store easily.")
S(c, "responsible", EGYPT, "About Zid Egypt", struct(EGYPT, "حول زد مصر"), "Commercial Registration No.: 201574",
  ":Zid Egypt operates officially under Commercial Registration No.:201574 Tax ID No.: 711-549-443",
  note="The Arabic part of the same article gives the tax number as 711-459-443; recorded as found.")
S(c, "responsible", EGYPT, "حول زد مصر", struct(EGYPT, "حول زد مصر"), "رقم السجل التجاري: 201574", "تعمل زد مصر رسميًا تحت: رقم السجل التجاري: 201574 الرقم الضريبي: 711-459-443")
S(c, "responsible", EGYPT, "About Zid Egypt", struct(EGYPT, "حول زد مصر"), "Address", "Address: 55 Street 18, Sarayat Maadi, Cairo, Egypt")
SNF(c, "responsible", "Which terms and which contracting entity apply to merchants in Egypt (zid.eg serves the same Terms naming the Saudi entity)",
    "help.zid.sa/about-zid-egypt/; zid.sa/en/egypt/; zid.eg/ar/ (footer); zid.eg/ar/legal/terms-conditions/",
    why="The pages in the route were read; zid.eg serves the zid.sa site with the Saudi entity in its footer and Terms; no Egypt-specific terms were found.")
OBS(c, "decides", "Which Zid services (payments, shipping, plans) a store registered in Egypt can turn on", "zid.sa/en/egypt/; dashboard registration for an Egyptian store",
    means="Open a store with Egypt as its country and record which services the dashboard offers")
SNF(c, "boundary", "An API field or endpoint for Zid Egypt", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names Zid Egypt.")
S(c, "reason", EGYPT, "About Zid Egypt", struct(EGYPT, "حول زد مصر"), "compliance", "Ensuring full compliance with Egyptian regulatory and taxation requirements.")

# ---------- ZD-C-032 Countries Zid serves ----------
c = "ZD-C-032"
S(c, "where", ZLLMS, "## Other countries", ST[ZLLMS], "Other countries", "- [Egypt](https://zid.sa/en/egypt/) - [UAE](https://zid.sa/en/uae/) - [Kuwait](https://zid.sa/en/kuwait/) - [Oman](https://zid.sa/en/oman/) - [Syria](https://zid.sa/en/syria/)")
S(c, "decides", H("faq-0"), "answer", struct(H("faq-0"), "FAQ: زد يخدم التجار في السعودية فقط؟ هل يخدم الخليج؟"), "السعودية ودول الخليج",
  "حاليًا زد يخدم التجار المتواجدين في السعودية ودول الخليج فقط من جميع الجنسيات",
  note="This FAQ was last updated August 30, 2023; the country pages and the Zid Egypt article (2026) name Egypt and Syria. Recorded as found.")
S(c, "decides", PAYMENTS, "FAQ For our Saudi Superstars", ST[PAYMENTS], "Is this available across the GCC?",
  'Is this available across the GCC?","answer":"Currently in Saudi Arabia and Kuwait.', scope="Zid Payments", note="FAQ held in the page's embedded data (opens on click).")
GEN(c, what="A clause stating which entity contracts with merchants in each country Zid serves")
SNF(c, "boundary", "An API endpoint listing the countries Zid serves (as opposed to a store's operating countries)", "docs.zid.sa/llms.txt (all API groups read)",
    why="All API reference groups were read; Countries and Cities lists store and shipping countries, not the countries Zid serves.")
SNF(c, "reason", "A stated reason for the list of countries served", "zid.sa/llms.txt; zid.sa country pages; help.zid.sa FAQ زد يخدم التجار في السعودية فقط؟")

# ---------- ZD-C-033 Store country, operating countries and cities ----------
c = "ZD-C-033"
S(c, "where", D("retrieve-store-operating-countries"), "description", struct(D("retrieve-store-operating-countries"), "List Store Operating Countries"),
  EP("retrieve-store-operating-countries"), "Retrieve a list of countries where the store operates. This list includes the country's unique ID, name, ISO codes, and flag image URL.")
S(c, "decides", H("store-language"), "ملاحظة", struct(H("store-language"), "لغة وعملات المتجر ( لوحة التحكم الجديدة )"), "تفعيل عملة دولة", "عند تفعيل عملة دولة يتم تفعيل الشحن إليها.")
S(c, "decides", AR_TERMS, "بعض الشروط والأحكام الخاصة بالمحفظة للتجار خارج المملكة العربية السعودية", ST[AR_TERMS], "تغيير دولة المتجر",
  "في حال قيام التاجر بنقل أو تغيير دولته في إعدادات المتجر إلى دولة أخرى، يشترط تصفير رصيد المحفظة أولاً")
S(c, "decides", H("gcc-merchants"), "مرحلة التسجيل", struct(H("gcc-merchants"), "إنشاء متجر في زد لمستخدمي دول الخليج"), "تحديد موقعك أو موقع المخزون", "تحديد موقعك أو موقع المخزون.", scope="مستخدمي دول الخليج")
GEN(c)
S(c, "boundary", D("retrieve-store-operating-countries"), "Scopes", struct(D("retrieve-store-operating-countries"), "List Store Operating Countries"), EP("retrieve-store-operating-countries"), SCOPEQ("retrieve-store-operating-countries"))
S(c, "boundary", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Countries and Cities", APIW("Merchant APIs > Countries and Cities"))
SNF(c, "reason", "A stated reason for tying shipping countries to activated currencies", "help.zid.sa/store-language/; docs.zid.sa Countries and Cities group")

# ---------- ZD-C-034 Markets ----------
c = "ZD-C-034"
S(c, "where", H("markets"), "intro", struct(H("markets"), "الأسواق ( لوحة التحكم الجديدة )"), "الاعدادات > الأسواق", "يمكنك الوصول الى خاصية الأسواق من خلال : الاعدادات > الأسواق")
S(c, "decides", H("markets"), "ملاحظة", struct(H("markets"), "الأسواق ( لوحة التحكم الجديدة )"), "عدد الأسواق حسب الباقة",
  "خاصية الأسواق تتيح لك عدد من الأسواق حسب باقتك: باقة الانطلاقة سوق واحد افتراضي باقة النمو سوقين افتراضي وجديد الباقة الاحترافية خمس أسواق",
  scope="باقة الانطلاقة; باقة النمو; الباقة الاحترافية")
S(c, "decides", H("markets"), "خطوات إنشاء السوق", struct(H("markets"), "الأسواق ( لوحة التحكم الجديدة )"), "عملة السوق", "عملة السوق: حدّد العملة التي سيتم اعتمادها لعرض أسعار المنتجات داخل هذا السوق.")
GEN(c)
SNF(c, "boundary", "An API endpoint, scope or webhook for markets", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names markets.")
SNF(c, "reason", "A stated reason for the markets placement", "help.zid.sa/markets/")

# ---------- ZD-C-035 Store business data and verification ----------
c = "ZD-C-035"
S(c, "where", H("store-info-ksa"), "intro", struct(H("store-info-ksa"), "بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )"), "الاعدادات > المتجر > بيانات المتجر",
  "يمكنك الوصول الى بيانات المتجر من خلال : لوحة التحكم > الضغط على أيقونة الاعدادات . بعد ذلك المتجر> الضغط على بيانات المتجر .")
S(c, "where", H("saudi-merchants"), "موثوقية المتجر", struct(H("saudi-merchants"), "إنشاء متجر في زد لمستخدمي السعودية"), "توثيق منصة المركز السعودي للأعمال",
  "توثيق منصة المركز السعودي للأعمال (لتجار السعودية)", scope="تجار السعودية")
S(c, "decides", H("store-info-ksa"), "تفاصيل النشاط التجاري", struct(H("store-info-ksa"), "بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )"), "نوع النشاط",
  "اختر تفاصيل النشاط، ثم حدد نوع النشاط (فرد، مؤسسة، شركة، جمعية خيرية) وأكمل البيانات المطلوبة ثم اضغط حفظ.", scope="السعودية")
S(c, "decides", H("store-info-ksa"), "ملاحظة", struct(H("store-info-ksa"), "بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )"), "حسب نوع النشاط والدولة",
  "تختلف المتطلبات والبيانات المطلوبة حسب نوع النشاط التجاري والدولة.")
S(c, "decides", H("faq-5"), "answer", struct(H("faq-5"), "FAQ: هل يشترط وجود سجل تجاري للتسجيل في زد والاستفادة من خدماته؟"), "سجل تجاري",
  "لا، لا يشترط وجود سجل تجاري للمتجر إلا إن كنت ترغب بربط المتجر ببوابات الدفع لتوفير خدمات الدفع مثل مدى، فيزا ، ماستر كارد، آبل بي (Apple Pay)، وحساب سداد")
S(c, "responsible", AR_TERMS, "الحسابات", ST[AR_TERMS], "الأهلية القانونية",
  "في حال قيامك بالتسجيل كمؤسسة أو شركة أو أي شكل نظامي آخر، فإن هذه المؤسسة أو الشركة أو الشكل النظامي الآخر يجب أن تتوافر فيه الأهلية القانونية والنظامية والشرعية اللازمة للقيام بأعمال التجارة عبر منصة زد.")
S(c, "boundary", D("business-33664762e0"), "description", struct(D("business-33664762e0"), "Business"), EP("business-33664762e0") + " (third_store_business_read)",
  "Retrieves the KYC (Know Your Customer) verification details of the current store, including the Commercial Registration (CR) information and associated business details.")
S(c, "reason", H("faq-5"), "answer", struct(H("faq-5"), "FAQ: هل يشترط وجود سجل تجاري للتسجيل في زد والاستفادة من خدماته؟"), "ويفضّل وجوده",
  "ويفضّل وجوده لحفظ هويتك واعتمادها ولزيادة موثوقية العملاء لمتجرك وعلامتك التجارية.")

# ---------- ZD-C-036 E-commerce store regulations ----------
c = "ZD-C-036"
S(c, "where", AR_TERMS, "ضوابط المتجر الإلكتروني", ST[AR_TERMS], "ضوابط المتجر الإلكتروني",
  "ينبغي على كافة المتاجر والتجّار الالتزام بالإفصاح في المتجر الإلكتروني عن البيانات التالية: الاسم والعنوان – السجل التجاري والرقم الضريبي أو وثيقة العمل الحر – ووسائل الاتصال الرسمية.")
S(c, "decides", AR_TERMS, "ضوابط المتجر الإلكتروني", ST[AR_TERMS], "الأنظمة",
  "ينبغي على كافة المتاجر والتُجّار الالتزام بكافة القوانين المعمول بها لتنظيم التجارة عبر الانترنت وكذلك الالتزام بنظام الجرائم المعلوماتية وأنظمة وزارة التجارة والاستثمار ونظام التعاملات الإلكترونية ونظام التجارة الإلكترونية.")
S(c, "decides", AR_TERMS, "ضوابط المتجر الإلكتروني", ST[AR_TERMS], "الترخيص",
  "ينبغي على كافة المتاجر والتجّار الذين يقدمون منتجات أو خدمات معينة تتطلب ترخيصاً من الجهات الرسمية، بالإفصاح عن الترخيص وكافة بياناته.")
S(c, "responsible", AR_TERMS, "ضوابط المتجر الإلكتروني", ST[AR_TERMS], "ليست طرفاً",
  "وعلى أن زد غير مسؤولة قانوناً أو شرعاً عن هذا الإخلال الحاصل من قبل التاجر في مواجهة المستهلك، حيث إنها ليست طرفاً في العلاقة بين المستهلك والتاجر")
S(c, "boundary", H("store-info-ksa"), "ملاحظة", struct(H("store-info-ksa"), "بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )"), "أسفل صفحة المتجر",
  "البريد الإلكتروني و رقم الهاتف و رقم السجل التجاري ستظهر للعملاء في أسفل صفحة المتجر.")
S(c, "reason", AR_TERMS, "ضوابط المتجر الإلكتروني", ST[AR_TERMS], "لدواعي تحسين جودة تجربة التاجر والمستهلك", "ولكنها تقوم بذلك لدواعي تحسين جودة تجربة التاجر والمستهلك مع زد.")

# ---------- ZD-C-037 Zid Pay prohibited activities and sanctions ----------
c = "ZD-C-037"
S(c, "where", AR_ZPSA, "الأنشطة المحظورة", ST[AR_ZPSA], "الأنشطة المحظورة",
  "لا يجوز للتاجر استخدام زد باي في أي نشاط محظور أو التعامل مع هيئات محظورة من زد باي أو المملكة العربية السعودية أو بلد النشاط، تتضمن:", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "الأنشطة المحظورة", ST[AR_ZPSA], "البلدان الخاضعة للعقوبات الدولية",
  "الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، جنوب السودان، كوبا، ارتريا، جمهورية افريقيا الوسطى) وما إلى ذلك.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "الأنشطة المحظورة", ST[AR_ZPSA], "قوائم العقوبات",
  "التاجر أو المستفيد النهائي (الشريك في عملية البيع والشراء) الذين طبقت عليهم عقوبات بناء على قرارات الأمم المتحدة، أو وزارة الخزانة الإنجليزية، أو الاتحاد الأوروبي، أو مكتب مراقبة الأصول الأجنبية، أو من هو مطالب للامتثال إذا كان الاسم مطابق لأي قائمة عقوبات أخرى.",
  scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPKW, "الأنشطة المحظورة", ST[AR_ZPKW], "البلدان الخاضعة للعقوبات الدولية (الكويت)",
  "الأنشطة التي تتعامل بشكل مباشر أو غير مباشر مع البلدان الخاضعة للعقوبات الدولية، تتضمن (إيران، سوريا، روسيا، السودان، كوبا، ارتريا،جزيرة القرم ، جمهورية افريقيا الوسطى، كوريا الشمالية، اليمن، العراق، اوكرانيا) وما إلى ذلك.",
  scope="Zid Pay, Kuwait")
S(c, "decides", AR_ZPSA, "التحويلات والمدفوعات الدولية", ST[AR_ZPSA], "مبالغ كبيرة من دول أجنبية",
  "يتم إيقاف إيداعات المبالغ، ويتم التدقيق والتحقيق لجميع الحسابات التي تستقبل مبالغ كبيرة من دول أجنبية.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", AR_ZPSA, "الأنشطة المحظورة", ST[AR_ZPSA], "تحديث الأنشطة المحظورة", "الأنشطة المحظورة أو المقيدة يمكن تحديثها في أي وقت، مع إشعار التاجر.", scope="Zid Pay, Saudi Arabia")
S(c, "decides", EN_ZPSA, "Prohibited Activities", ST[EN_ZPSA], "Prohibited Activities", "Dealings with internationally sanctioned countries or entities.", scope="Zid Pay, Saudi Arabia (English text)")
S(c, "responsible", AR_ZPSA, "تسوية المدفوعات وعملية الاسترداد", ST[AR_ZPSA], "إبلاغ الجهات المعنية",
  "يجوز لزد باي احتجاز عمليات دفع وطلب مستندات وأدلة داعمة للتحقق من شرعية عمليات الدفع وفي حالة فشل العميل في تقديم الأدلة الكافية لإثبات شرعية المبالغ المحولة فإن زد باي لها الحق في اتخاذ كافة الإجراءات اللازمة في هذه الحالة والتي تتضمن رد المبالغ لمصدرها، إلغاء الحساب وإبلاغ الجهات المعنية دون إعلام المستخدم أو الحصول على أي نوع من الموافقة.",
  quote="فإن زد باي لها الحق في اتخاذ كافة الإجراءات اللازمة في هذه الحالة والتي تتضمن رد المبالغ لمصدرها، إلغاء الحساب وإبلاغ الجهات المعنية دون إعلام المستخدم أو الحصول على أي نوع من الموافقة.",
  scope="Zid Pay, Saudi Arabia")
S(c, "responsible", AR_ZPSA, "الأنشطة المحظورة", ST[AR_ZPSA], "موافقة البنك المركزي",
  "التجار مقدمي الخدمات المالية بدون موافقة البنك المركزي على سبيل المثال (الاستثمارات المالية غير المصرح بها، شركات التداول، تجميع الأموال أو الحوالات وخلافه).", scope="Zid Pay, Saudi Arabia")
ASK(c, "responsible", "Who screens merchants and buyers against the named sanctions lists (Zid Pay or the payment service provider), and with which tool", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; zid.sa/ar/legal/zidpay-terms-conditions-kw/")
SNF(c, "boundary", "An API field or webhook for screening results or prohibited-activity flags", "docs.zid.sa/llms.txt (all API groups read)", why="All API reference groups were read; none names screening.")
SNF(c, "reason", "A stated reason for the two different sanctioned-country lists (Saudi Arabia and Kuwait)", "zid.sa/ar/legal/zidpay-terms-conditions-sa/; zid.sa/ar/legal/zidpay-terms-conditions-kw/; help.zid.sa FAQ ماهي الأنشطة المحظورة في زد باي ؟")

# ---------- ZD-C-038 Nafath identity verification ----------
c = "ZD-C-038"
S(c, "where", H("nafath_verification"), "خطوات اجتياز تحقق نفاذ", struct(H("nafath_verification"), "اجتياز التحقق من نفاذ"), "خطوة التحقق من نفاذ",
  "قم بالضغط على أيقونة تأكيد تفعيل زد باي في أخر خطوة من التفعيل و الموافقة على الشروط والأحكام.")
S(c, "decides", H("nafath_verification"), "intro", struct(H("nafath_verification"), "اجتياز التحقق من نفاذ"), "شرط نفاذ",
  "لتفعيل زد باي و استقبال عمليات الدفع الإلكتروني يشترط لمالك المتجر اجتياز التحقق من نفاذ.")
S(c, "decides", H("nafath_verification"), "ملاحظة", struct(H("nafath_verification"), "اجتياز التحقق من نفاذ"), "عدد المحاولات", "عدد محاولات التحقق المتاحة خلال اليوم الواحد هي 3 محاولات.")
S(c, "responsible", H("nafath_verification"), "ملاحظة", struct(H("nafath_verification"), "اجتياز التحقق من نفاذ"), "باسم مزود الخدمة", "يكون طلب التحقق باسم مزود الخدمة.")
S(c, "boundary", H("nafath_verification"), "خطوات", struct(H("nafath_verification"), "اجتياز التحقق من نفاذ"), "إنشاء الحساب في زد باي",
  "قم بالعودة إلى لوحة تحكم المتجر و يتم تلقائياً تحديث حالة التحقق و إنشاء الحساب في زد باي.")
S(c, "boundary", PAYMENTS, "Get Started in Four Easy Steps", ST[PAYMENTS], "Quick ID Check", "Verify your identity with Nafath using the store owner's ID.")
SNF(c, "reason", "A stated reason for requiring Nafath", "help.zid.sa/nafath_verification/; zid.sa/en/solutions/payments/")

# ---------- ZD-C-039 Store legal pages ----------
c = "ZD-C-039"
S(c, "where", H("legal-pages"), "intro", struct(H("legal-pages"), "الصفحات القانونية ( لوحة التحكم الجديدة )"), "الاعدادات > المتجر > الصفحات القانونية",
  "يمكنك الوصول الى الصفحات القانونية من خلال : الاعدادات > المتجر > الصفحات القانونية")
S(c, "decides", H("legal-pages"), "أنواع الصفحات القانونية", struct(H("legal-pages"), "الصفحات القانونية ( لوحة التحكم الجديدة )"), "أنواع الصفحات",
  "سياسة الخصوصية الشروط والاحكام سياسة الاستبدال والارجاع الشكاوى والاقتراحات التراخيص")
S(c, "decides", AR_TERMS, "ضوابط المتجر الإلكتروني", ST[AR_TERMS], "سياسات المستهلك",
  "ينبغي على كافة المتاجر والتجّار الالتزام بإيضاح الشروط والأحكام للمستهلك، وتوضيح الوسائل اللازمة لتلقي شكاوى المستهلك ومعالجتها، وسياسة الاستبدال والارجاع وكيفية ارجاع المبالغ -إن وجدت- وسياسة الخصوصية وحماية بيانات المستهلك.")
S(c, "responsible", EN_PRIV, "As the Merchants", ST[EN_PRIV], "privacy policy on your store",
  "You must ensure they understand how you (and we, on your behalf) collect and process their data, as you should post a privacy policy on your store detailing the information you collect, how you use it, and with whom you share it.")
S(c, "boundary", LLMS, "API Docs", ST[LLMS], "API's > Storefront [Pages]", APIW("API's > Storefront", "Pages"))
SNF(c, "reason", "A stated reason for the legal pages placement", "help.zid.sa/legal-pages/; zid.sa/ar/legal/terms-conditions/ (ضوابط المتجر الإلكتروني)")

# ---------- ZD-C-040 Privacy and personal data ----------
c = "ZD-C-040"
S(c, "where", EN_PRIV, "CONTACT US", ST[EN_PRIV], "Data Protection Officer", "Attn: Data Protection Officer 3893 Prince Sultan Bin Salman Bin Abdulaziz St, Ar Rahmaniyyah, Riyadh 12341",
  note="The policy's contact address; it does not state where personal data is stored.")
S(c, "decides", EN_PRIV, "THE DATA & INFORMATION COLLECTION", ST[EN_PRIV], "consent", "In all cases, we process your personal information only with your consent.")
S(c, "decides", EN_PRIV, "THE RETENTION OF THE INFORMATION & DATA", ST[EN_PRIV], "retention", "We will retain and use your Personal data for the period necessary to comply with our legal obligations.")
S(c, "responsible", EN_PRIV, "As the Merchants", ST[EN_PRIV], "data processor", "Legally, we act as a “data processor” and “service provider” under the applicable privacy laws.")
S(c, "responsible", EN_PRIV, "Processing Your Personal Data on behalf of Merchants", ST[EN_PRIV], "under the direction of the Merchant",
  "In this role, Zid acts under the direction of the Merchant, and the Merchant’s terms of service and privacy policy apply, not Zid’s.")
S(c, "responsible", EN_PRIV, "Partner processes the Merchant’s information & data and Using", ST[EN_PRIV], "Partner responsibility",
  "It is your responsibility to protect and process the Merchants’ personal information securely and in compliance with applicable laws, and other relevant terms.")
S(c, "boundary", EN_PRIV, "Partner processes the Merchant’s information & data and Using", ST[EN_PRIV], "sharing with partners",
  "When Merchants sign up for your services (e.g., installing an app or service you developed), we share their personal information with you based on the Merchant’s instructions.")
S(c, "boundary", EN_PRIV, "SHARING THE INFORMATION & DATA", ST[EN_PRIV], "service providers",
  "including service providers who access information about you to perform services on our behalf (e.g., fraud prevention and verification services), and including financial institutions, processors, and other entities that are part of the payment or transfer process;")
S(c, "boundary", EN_PRIV, "DISCLOSURE OF INFORMATION", ST[EN_PRIV], "public entity",
  "If the entity requesting the disclosure is a public entity, for security purposes, to implement another system, or to meet judicial requirements per the provisions specified by the regulations.")
S(c, "reason", EN_PRIV, "THE DATA & INFORMATION COLLECTION", ST[EN_PRIV], "legal basis",
  "We process your personal data to fulfill our contract with you or because it is in our legitimate interests to maintain our business relationship, prevent risk and fraud, provide effective services, improve our products and services, and respond to your needs.")

# ---------- ZD-C-041 Cross-border data transfer ----------
c = "ZD-C-041"
SNF(c, "where", "The country or cloud region where Zid stores merchant and customer data",
    "zid.sa/en/legal/privacy-policy/; zid.sa/ar/legal/privacy-policy/; zid.sa/ar/legal/terms-conditions/; docs.zid.sa (all pages read); help.zid.sa FAQ ماهي سياسة الخصوصية والأمان في زد؟",
    why="The pages in the route were read; none states where data is stored. API examples show S3 URLs, which the notes record as inference only.")
ASK(c, "where", "Where Zid stores merchant and customer data, and in which country or region", "zid.sa/en/legal/privacy-policy/ (Data Protection Officer)")
S(c, "decides", EN_PRIV, "THE DATA TRANSFER ACROSS THE BORDERS", ST[EN_PRIV], "transfer to other countries",
  "In accordance with the relevant laws and regulations, we may transfer or disclose your personal data to parties in other countries.")
S(c, "decides", AR_PRIV, "نقل البيانات عبر الحدود", ST[AR_PRIV], "نقل البيانات عبر الحدود",
  "وفقًا للقوانين واللوائح ذات الصلة، قد نقوم بنقل أو الإفصاح عن بياناتك الشخصية إلى أطراف في بلدان أخرى.")
S(c, "responsible", EN_PRIV, "THE DATA TRANSFER ACROSS THE BORDERS", ST[EN_PRIV], "appropriate safeguards",
  "However, such transfer or disclosure will only occur if appropriate safeguards are in place to protect your privacy and ensure that the level of protection guaranteed for your personal data under the law and its regulations is not compromised.")
SNF(c, "boundary", "An API or setting through which a merchant chooses where data is held", "docs.zid.sa/llms.txt (all API groups read); help.zid.sa settings articles",
    why="All API reference groups and settings articles were read; none offers a data-location choice.")
SNF(c, "reason", "A stated reason for cross-border transfers", "zid.sa/en/legal/privacy-policy/; zid.sa/ar/legal/privacy-policy/")

# ---------- ZD-C-042 AI data processing ----------
c = "ZD-C-042"
S(c, "where", EN_PRIV, "AI Data Processing", ST[EN_PRIV], "Google Cloud Vertex AI",
  "Zid Agent uses Google Cloud Vertex AI as a data processor to power AI-assisted features including product research, store optimization, campaign management, and conversational assistance.")
SNF(c, "where", "The region where Google Cloud Vertex AI processes Zid Agent data", "zid.sa/en/legal/privacy-policy/ (AI Data Processing); zid.sa/ar/legal/privacy-policy/",
    why="The section was read; it names the processor but no region.")
S(c, "decides", EN_PRIV, "AI Data Processing", ST[EN_PRIV], "explicit in-app consent", "All AI processing occurs only after the user provides explicit in-app consent.")
S(c, "responsible", EN_PRIV, "AI Data Processing", ST[EN_PRIV], "processor",
  "We retain full control over user data and determine the purposes and means of processing. Google Cloud acts solely as an infrastructure provider and processor under Google Cloud's enterprise data processing terms.")
S(c, "boundary", EN_PRIV, "AI Data Processing", ST[EN_PRIV], "on our behalf", "Google Cloud processes user-submitted messages, images, and store data solely on our behalf.")
S(c, "boundary", EN_PRIV, "AI Data Processing", ST[EN_PRIV], "no model training", "Google Cloud does not use this data to train foundation models or for model improvement.")
SNF(c, "reason", "A stated reason for using Google Cloud Vertex AI", "zid.sa/en/legal/privacy-policy/ (AI Data Processing)")

# ---------- ZD-C-043 Digital products and vouchers ----------
c = "ZD-C-043"
S(c, "where", D("upload-file-to-s3-11396102e0"), "description", struct(D("upload-file-to-s3-11396102e0"), "Upload File to S3"), "Amazon S3",
  "The \"Upload File to S3\" endpoint provides a pre-signed URL for secure, temporary access to upload files directly to Amazon S3 storage.",
  note="Where digital-product files are stored, as the API reference states it; no region is stated.")
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Products > Digital Products", APIW("Merchant APIs > Products > Digital Products"))
S(c, "decides", AR_ZPSA, "الأنشطة المحظورة", ST[AR_ZPSA], "المنتجات الرقمية", "المنتجات الرقمية : يتم قبول بعض المنتجات الرقمية بناء على تقييم نوع المنتجات من قبل مزود الخدمة",
  scope="Zid Pay, Saudi Arabia")
GEN(c)
S(c, "boundary", D("generate-upload-url-11396021e0"), "Scopes", struct(D("generate-upload-url-11396021e0"), "Generate Upload URL"), EP("generate-upload-url-11396021e0"), SCOPEQ("generate-upload-url-11396021e0"))
S(c, "boundary", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Products > Digital Vouchers", APIW("Merchant APIs > Products > Digital Vouchers"))
SNF(c, "where", "The region of the Amazon S3 storage used for digital-product files", "docs.zid.sa/upload-file-to-s3-11396102e0.md; docs.zid.sa/generate-upload-url-11396021e0.md",
    why="The pages were read; they name Amazon S3 but no region.")
SNF(c, "reason", "A stated reason for storing digital-product files in Amazon S3", "docs.zid.sa Digital Products group")

# ---------- ZD-C-044 Export requests ----------
c = "ZD-C-044"
S(c, "where", H("export-request"), "intro", struct(H("export-request"), "طلبات التصدير ( لوحة التحكم الجديدة )"), "طلبات التصدير",
  "يمكنك الوصول الى طلبات التصديرات من خلال : لوحة التجكم > الضغط على أيقونة الاعدادات . بعد ذلك الضغط على خانة طلبات التصدير .")
S(c, "decides", H("export-request"), "اعدادات الأمان", struct(H("export-request"), "طلبات التصدير ( لوحة التحكم الجديدة )"), "حماية الملفات المصدّرة بكلمة مرور",
  "عند طلب أي ملف مُصدّر، ستتمكن من تحميله مباشرة في متصفحك. ولزيادة أمان خصوصيتك، يُنصح بتفعيل خيار حماية الملفات المصدّرة بكلمة مرور.")
GEN(c)
S(c, "boundary", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Products > Product Export", APIW("Merchant APIs > Products > Product Export"))
S(c, "reason", H("export-request"), "اعدادات الأمان", struct(H("export-request"), "طلبات التصدير ( لوحة التحكم الجديدة )"), "لضمان حماية بياناتك",
  "سيتم إرسال كلمة المرور مباشرة إلى بريدك الإلكتروني، وستتمكن من تحميل الملف باستخدامها لضمان حماية بياناتك.")

# ---------- ZD-C-050 Store languages and currencies ----------
c = "ZD-C-050"
S(c, "where", H("store-language"), "العملات", struct(H("store-language"), "لغة وعملات المتجر ( لوحة التحكم الجديدة )"), "لوحة التحكم > الاعدادات > اللغات والعملات",
  "لتفعيل العملة الرئيسية للمتجر أو إضافة عملات أخرى من خلال: لوحة التحكم > الاعدادات > اللغات والعملات")
S(c, "decides", CHUNK, "compare-plans group Other", ST[CHUNK], "Geo-Based Currency Settings", PL("Geo-Based Currency Settings"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", H("store-language"), "ملاحظة", struct(H("store-language"), "لغة وعملات المتجر ( لوحة التحكم الجديدة )"), "الدفع بالعملة الأساسية",
  "في حال تم تفعيل المدفوعات لزد [ مدفوعات زد  متاحة لتجار السعودية و الكويت] كخيار دفع إلكتروني وتم تفعيل عملات أخرى غير العملة الأساسية (الريال السعودي \\ الدينار الكويتي) بالمتجر ، سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر (الريال السعودي\\ الدينار الكويتي) لجميع الشبكات ما عدا “كي نت” سيتم الدفع بالدينار الكويتي.",
  quote="سيتم استعراض أسعار المنتجات بالعملة المختارة مثل الريال العماني من قبل العميل لكن في مرحلة الدفع النهائي سيتم الدفع بالعملة الأساسية للمتجر",
  scope="مدفوعات زد (السعودية، الكويت)")
S(c, "decides", H("zidpay_staff_and_currencies"), "خاصية العملات", struct(H("zidpay_staff_and_currencies"), "صلاحيات فريق العمل و خاصية العملات"), "سعر الصرف لبوابة الدفع",
  "المبلغ المدفوع خاضع لتحويل سعر الصرف لبوابة الدفع المفعلة.")
S(c, "decides", H("store-language"), "ملاحظة", struct(H("store-language"), "لغة وعملات المتجر ( لوحة التحكم الجديدة )"), "سعر الصرف عند تغيير العملة",
  "عند تغيير العملة سيتم تحويل أسعار المنتجات إلى العملة الجديدة بناءً على سعر الصرف في وقت التغيير، ونتيجة لذلك قد يحصل تغيير في مجموع المبيعات.")
GEN(c)
S(c, "boundary", D("view-order-12479054e0"), "DefaultOrderCurrencySerializer", struct(D("view-order-12479054e0"), "View Order"), "order_currency.exchange_rate",
  "Exchange rate applied to the order currency relative to the store currency.")
S(c, "boundary", D("webhook-events-order"), "Currency Handling for Orders", struct(D("webhook-events-order"), "Order (webhook payload)"), "Currency Handling for Orders",
  "When the store currency, order currency, and the currency of the shipping address (for cash on delivery) are different, partners must convert the order total to the appropriate currency.")
S(c, "boundary", D("localization-33664641e0"), "description", struct(D("localization-33664641e0"), "Localization"), EP("localization-33664641e0"),
  "Retrieves the store's supported languages and currencies, indicating the currently active language and the default currency.")
SNF(c, "reason", "A stated reason for charging Zid Pay in the store's base currency", "help.zid.sa/store-language/; help.zid.sa/zidpay_staff_and_currencies/; zid.sa/en/solutions/payments/")

# ---------- ZD-C-051 Tax settings (VAT) ----------
c = "ZD-C-051"
S(c, "where", H("tax-settings"), "تفعيل ضريبة القيمة المضافة", struct(H("tax-settings"), "اعدادات الضريبة ( لوحة التحكم الجديدة )"), "اعدادات الضرائب",
  "يمكنك تفعيل ضريبة القيمة المضافة من خلال : لوحة التحكم > الضغط على ايقونة الإعدادات بعد ذلك اعدادات الضرائب")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Invoice & Tax Settings", PL("Invoice & Tax Settings"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", CHUNK, "compare-plans group Other", ST[CHUNK], "Tax-Applicable Countries", PL("Tax-Applicable Countries"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", PRICING, "plan card Growth", ST[PRICING], "Growth: All features of Rise package, plus:", "Calculate and display VAT", scope="plan Growth")
S(c, "decides", H("tax-settings"), "تخصيص الضريبة حسب الدول المضافة", struct(H("tax-settings"), "اعدادات الضريبة ( لوحة التحكم الجديدة )"), "إضافة دولة",
  "ستظهر لك الصفحة التالية قم بإدخال التفاصيل التالية ( الدولة ، الرقم الضريبي ، نسبة ضريبة القيمة المضافة ، شهادة ضريبة القيمة المضافة )")
S(c, "responsible", H("tax-settings"), "تخصيص الضريبة حسب الدول المضافة", struct(H("tax-settings"), "اعدادات الضريبة ( لوحة التحكم الجديدة )"), "الإقرار",
  "قم بالإقرار على اطلاعك على دليل ضريبة القيمة المضافة في الدول التي تُطبق فيها، وتم الالتزام بالأنظمة المحددة")
S(c, "boundary", D("get-vat-settings"), "description", struct(D("get-vat-settings"), "Retrieve VAT Settings"), EP("get-vat-settings") + " (third_vat_read)",
  "Return a list of the VAT settings configured on this store. For example, to indicate whether the store VAT is applied on shipping fees or not.")
S(c, "reason", H("tax-settings"), "للمتاجر السعودية", struct(H("tax-settings"), "اعدادات الضريبة ( لوحة التحكم الجديدة )"), "اللائحة الضريبية للمتاجر الإلكترونية",
  "للمتاجر السعودية: تنص اللائحة الضريبية للمتاجر الإلكترونية على ضرورة عرض شهادة ضريبة القيمة المضافة في المتجر.", scope="المتاجر السعودية",
  note="The reason stated for showing the VAT certificate in the store.")

# ---------- ZD-C-052 Invoice settings ----------
c = "ZD-C-052"
S(c, "where", H("invoice-settings"), "intro", struct(H("invoice-settings"), "اعدادات الفواتير (لوحة التحكم الجديدة )"), "اعدادات الفاتورة",
  "للوصول الى اعدادات الفاتورة من خلال : لوحة التحكم > الاعدادات بعد ذلك اخيار خانة اعدادات الفاتورة")
S(c, "decides", CHUNK, "compare-plans group Basic Features", ST[CHUNK], "Invoice Printing", PL("Invoice Printing"), scope=PLAN_SCOPE, note=PLAN_NOTE)
S(c, "decides", H("invoice-settings"), "اعدادات الفاتورة", struct(H("invoice-settings"), "اعدادات الفواتير (لوحة التحكم الجديدة )"), "إرسال فواتير الطلبات لعملائك",
  "في حال اختيار لا ، سيصدر نظام زد ملخص للطلب وسيتم إرسال نسخة للبريد الالكتروني للعميل ، وليس فاتورة أو فاتورة ضريبية.")
S(c, "responsible", H("invoice-settings"), "ملاحظة", struct(H("invoice-settings"), "اعدادات الفواتير (لوحة التحكم الجديدة )"), "غرامات وزارة التجارة",
  "في حال إيقاف إصدار الفواتير من نظام زد ولم تصدرها من نظام محاسبي آخر ، سيعرضك لغرامات وزارة التجارة..")
S(c, "boundary", H("invoice-settings"), "ملاحظة", struct(H("invoice-settings"), "اعدادات الفواتير (لوحة التحكم الجديدة )"), "نظام ERP",
  "بإمكانك إيقاف إصدار وإرسال الفواتير لعملائك في حال كنت تستخدم نظام محاسبي متخصص للفواتير بحيث لا يكون هناك تكرار. ( بعض المتاجر يصدر الفواتير من نظام ERP خاص به).")
SNF(c, "reason", "A stated reason for Zid issuing invoices by default", "help.zid.sa/invoice-settings/")

# ---------- ZD-C-053 ZATCA e-invoicing ----------
c = "ZD-C-053"
S(c, "where", H("zatca-integration"), "intro", struct(H("zatca-integration"), "الربط مع منصة فاتورة ZATCA ( لوحة التحكم الجديدة)"), "الربط مع منصة فاتورة (ZATCA )",
  "يمكنك الوصول الى خاصية الربط مع فوترة من خلال : لوحة التحكم >الضغط على ايقونة الاعدادات . بعد ذلك الضغط على الربط مع منصة فاتورة (ZATCA ) .")
S(c, "decides", H("zatca-integration"), "intro", struct(H("zatca-integration"), "الربط مع منصة فاتورة ZATCA ( لوحة التحكم الجديدة)"), "مجانًا",
  "من خلال خطوتين بسيطتين فقط، يمكنك ربط متجرك الإلكتروني بنظام فاتورة مجانًا، لضمان إرسال الفواتير الإلكترونية بشكل متكامل ومتوافق مع أنظمة الهيئة.")
S(c, "decides", H("zatca-integration"), "ملاحظة", struct(H("zatca-integration"), "الربط مع منصة فاتورة ZATCA ( لوحة التحكم الجديدة)"), "الكاشير", "متاح الربط مع الكاشير")
GEN(c)
S(c, "boundary", H("zatca-integration"), "intro", struct(H("zatca-integration"), "الربط مع منصة فاتورة ZATCA ( لوحة التحكم الجديدة)"), "هيئة الزكاة والضريبة والجمارك",
  "خاصية الربط مع منصة فاتورة تُمكّنك من الربط مباشرةً مع هيئة الزكاة والضريبة والجمارك، مما يضمن الامتثال لمتطلبات المرحلة الثانية من الفوترة الإلكترونية المعروفة باسم مرحلة الربط والتكامل.")
S(c, "boundary", H("zatca-integration"), "الخطوة الثانية : رمز التحقق", struct(H("zatca-integration"), "الربط مع منصة فاتورة ZATCA ( لوحة التحكم الجديدة)"), "رمز التحقق",
  "سجل الدخول في منصة فاتورة اضغط على تهيئة وحدة/جهاز جديد قم بإنشاء رمز تفعيل لجهاز واحد")
S(c, "reason", H("zatca-integration"), "intro", struct(H("zatca-integration"), "الربط مع منصة فاتورة ZATCA ( لوحة التحكم الجديدة)"), "الامتثال",
  "مما يضمن الامتثال لمتطلبات المرحلة الثانية من الفوترة الإلكترونية المعروفة باسم مرحلة الربط والتكامل.")

# ---------- ZD-C-054 Credit notes ----------
c = "ZD-C-054"
S(c, "where", LLMS, "API Docs", ST[LLMS], "Merchant APIs > Orders [List Order Credit Notes]", APIW("Merchant APIs > Orders", "List Order Credit Notes"))
OBS(c, "decides", "Whether credit notes are issued automatically or by the merchant, and on which plans", "dashboard: الطلبات; help.zid.sa article إشعارات الدائن والمدين ( لوحة التحكم الجديدة )")
GEN(c)
S(c, "boundary", D("get-order-credit-notes"), "description", struct(D("get-order-credit-notes"), "List Order Credit Notes"), EP("get-order-credit-notes"),
  "Credit notes are issued for orders that have been cancelled or modified, and this endpoint provides detailed information about each credit note, including customer details, product information, and payment details.")
S(c, "boundary", D("get-order-credit-notes"), "Scopes", struct(D("get-order-credit-notes"), "List Order Credit Notes"), EP("get-order-credit-notes"), SCOPEQ("get-order-credit-notes"))
PNR(c, "reason", "A stated reason for issuing credit notes", "help.zid.sa article إشعارات الدائن والمدين ( لوحة التحكم الجديدة ) (listed on help.zid.sa home)")
