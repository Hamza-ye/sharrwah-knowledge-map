# Gap rules for the Salla re-pass: every concern x placement with no statement gets one gap row.
# Each rule returns the six gap fields; overrides name single cells. Used by build_final.py.
H = "https://help.salla.sa/article/"
SC = "https://salla.com/"
TERMS = SC + "terms"
PRIVACY = SC + "privacy"
APPS_POLICY = "https://partners.salla.com/legal/apps-policy"
THEMES_POLICY = "https://partners.salla.com/legal/themes-policy"
JOIN_POLICY = "https://partners.salla.com/legal/privacy"
SALLA_403 = "salla.com answers 403 with a bot challenge to this session (tested on https://salla.com/terms, 2026-10-10)"
DASH_TEXT_SEARCH = ("the held dashboard text (structures/salla/dashboard-translations, ar and en) was searched for stated "
                    "reasons (لضمان، بهدف، حرصًا، لأن، نظرًا، تماشيًا)")
HELD_API_LISTS = ("the held lists docs-sidebar (merchant-api), docs-operations, docs-event-lists, portal-webhook-events, "
                  "portal-app-scopes and twilight-components name no resource, event, scope or component for it")
PAY_JOURNEY = ("Merchant dashboard https://s.salla.sa/payments/kyc (توثيق المتجر), as the owner of a store going through verification: open and save "
               "the payment services contract (عقد خدمات الدفع) presented there")

# salla.com product pages listed in the held sitemap (salla.com/sitemap_ar-SA.xml), by concern
PRODUCT = {
    "SA-C-012": SC + "moshamer-ai", "SA-C-024": SC + "digital-cards", "SA-C-033": SC + "seo-guide",
    "SA-C-072": SC + "affiliate-marketing", "SA-C-073": SC + "ads", "SA-C-074": SC + "marketing-tools",
    "SA-C-075": SC + "marketing", "SA-C-076": SC + "influencers", "SA-C-077": SC + "marketing-tools",
    "SA-C-082": SC + "marketing-tools", "SA-C-090": SC + "store-design", "SA-C-098": SC + "souq-eljomla",
    "SA-C-099": SC + "salla-chat", "SA-C-111": SC + "payments", "SA-C-112": SC + "payments", "SA-C-113": SC + "payments",
    "SA-C-117": SC + "payments", "SA-C-119": SC + "payments", "SA-C-120": SC + "payments", "SA-C-123": SC + "payments",
    "SA-C-126": SC + "payments", "SA-C-164": SC + "payments", "SA-C-114": SC + "payments", "SA-C-118": SC + "tamara",
    "SA-C-127": SC + "charity-sector", "SA-C-128": SC + "sallacapital1", "SA-C-116": SC + "shipping",
    "SA-C-139": SC + "shipping", "SA-C-141": SC + "shipping", "SA-C-142": SC + "shipping", "SA-C-143": SC + "shipping",
    "SA-C-144": SC + "shipping", "SA-C-147": SC + "shipping", "SA-C-148": SC + "branch_pickup",
    "SA-C-146": SC + "salla-crossborder", "SA-C-162": SC + "salla-crossborder", "SA-C-167": SC + "gcc-ecommerce",
    "SA-C-095": SC + "sallapoint", "SA-C-096": SC + "mahally", "SA-C-094": SC + "app-maker", "SA-C-004": SC + "plans",
}
# concerns whose responsibility would sit in the payment services contract rather than the usage agreement
PAY_CONTRACT = {"SA-C-112", "SA-C-123", "SA-C-164", "SA-C-117"}
# shipping concerns whose responsibility Salla's shipping page would state
SHIP_PAGE = {"SA-C-115": SC + "shipping", "SA-C-146": SC + "salla-crossborder", "SA-C-162": SC + "salla-crossborder"}
# partner and developer concerns: their terms are the partners' legal pages, which speak in general terms
GENERAL = {
    "SA-C-190": (APPS_POLICY, "المادة (2) and المادة (8)",
                 "يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك."),
    "SA-C-191": (APPS_POLICY, "المادة (3) and المادة (8)", "يُلزم المطور بعدم مشاركة أو بيع أي بيانات يتم جمعها عبر التطبيق دون موافقة صريحة."),
    "SA-C-192": (APPS_POLICY, "المادة (3)", "يجب أن يتوافق التطبيق مع متطلبات الأمان والتكامل المحددة من قبل فريق سلة."),
    "SA-C-193": (APPS_POLICY, "المادة (2)",
                 "يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك."),
    "SA-C-196": (JOIN_POLICY, "المادة الخامسة",
                 "توفر سلة البنية التحتية التقنية فقط لاستضافة تطبيقات أو خدمات الشركاء، دون أن يُعد ذلك بمثابة \"توصية أو تزكية\" رسمية لأي منتج أو خدمة."),
    "SA-C-197": (APPS_POLICY, "المادة (3)", "يجب أن يتوافق التطبيق مع متطلبات الأمان والتكامل المحددة من قبل فريق سلة."),
    "SA-C-198": (APPS_POLICY, "المادة (3)", "يجب أن يتوافق التطبيق مع متطلبات الأمان والتكامل المحددة من قبل فريق سلة."),
    "SA-C-199": (APPS_POLICY, "المادة (2)",
                 "يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك."),
    "SA-C-200": (APPS_POLICY, "المادة (8)", "يُلزم المطور بعدم مشاركة أو بيع أي بيانات يتم جمعها عبر التطبيق دون موافقة صريحة."),
    "SA-C-201": (APPS_POLICY, "المادة (3)", "يجب أن يتوافق التطبيق مع متطلبات الأمان والتكامل المحددة من قبل فريق سلة."),
    "SA-C-202": (APPS_POLICY, "المادة (3)", "يلتزم المطور بتحديث تطبيقه بشكل دوري ومعالجة أية مشكلات قد تؤثر على المستخدمين."),
    "SA-C-203": (JOIN_POLICY, "المادة الرابعة، ثانيًا", "التوافق مع بيئة التطوير الخاصة بسلة (Salla APIs، Webhooks، واجهات التحكم)."),
    "SA-C-207": (APPS_POLICY, "المادة (2)",
                 "يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك."),
    "SA-C-210": (APPS_POLICY, "المادة (2)",
                 "يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك."),
    "SA-C-125": (APPS_POLICY, "المادة (2)",
                 "يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك."),
    "SA-C-092": (APPS_POLICY, "المادة (2)",
                 "يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك."),
    "SA-C-091": (THEMES_POLICY, "the platform's role",
                 "تعمل منصة «سلة» كمنصة تقنية وسيطة لتوفير خدمات استضافة ونشر وإدارة الثيمات"),
    "SA-C-101": (THEMES_POLICY, "the platform's role",
                 "تعمل منصة «سلة» كمنصة تقنية وسيطة لتوفير خدمات استضافة ونشر وإدارة الثيمات"),
    "SA-C-200": (APPS_POLICY, "المادة (8)", "يُلزم المطور بعدم مشاركة أو بيع أي بيانات يتم جمعها عبر التطبيق دون موافقة صريحة."),
}
PARTNER_SIDE = {"SA-C-125", "SA-C-175", "SA-C-176", "SA-C-190", "SA-C-191", "SA-C-192", "SA-C-193", "SA-C-194", "SA-C-196",
                "SA-C-197", "SA-C-198", "SA-C-199", "SA-C-200", "SA-C-201", "SA-C-202", "SA-C-203", "SA-C-204", "SA-C-207",
                "SA-C-208", "SA-C-209", "SA-C-301", "SA-C-302", "SA-C-303", "SA-C-304", "SA-C-091", "SA-C-092", "SA-C-101"}

def ask_route(c, name):
    if c in PARTNER_SIDE:
        return f"Question to Salla's partner team (partners@salla.sa, or the Partners portal): why is {name} placed and controlled as recorded here?"
    return (f"Question to Salla merchant support (the dashboard's help, or help.salla.sa 'اسأل, واطلب الدعم'): why is {name} "
            f"placed and controlled as recorded here (its dashboard section, plan lines and settings)?")

# single cells: (what, means, who, route, why, kind); "{read}" in why is replaced by the pages read for the concern
OVR = {
    ("SA-C-114", "where"): ("The page where Salla names who processes and acquires Salla Payments transactions, and under which licence",
        "save a page from a browser", "founder", SC + "payments",
        SALLA_403 + "; the help articles read name only the payment services contract (عقد خدمات الدفع), not its parties: {read}", "observation needed"),
    ("SA-C-114", "decides"): ("The clause that says which licensed entity provides Salla Payments and what limits its licence sets",
        "save a page from a browser", "founder", TERMS, SALLA_403 + "; the help articles read are silent on it: {read}", "observation needed"),
    ("SA-C-114", "boundary"): ("The payment services contract (عقد خدمات الدفع), whose parties would show how the processor and acquirer meet the store and the platform",
        "record a journey", "founder", PAY_JOURNEY,
        "The contract is not public; help articles name it without its parties (SA-S-0081, SA-S-0088); " + SALLA_403 + ".", "observation needed"),
    ("SA-C-114", "reason"): ("A sentence on Salla's payments page giving the reason Salla Payments is run as it is (by Salla or through a licensed company)",
        "save a page from a browser", "founder", SC + "payments", SALLA_403 + "; the help articles read give no reason: {read}", "observation needed"),
    ("SA-C-164", "where"): ("The page that says in which currency Salla Payments receives and settles funds, and where that is set",
        "save a page from a browser", "founder", SC + "payments", SALLA_403 + "; the help articles read state the currency per market only: {read}", "observation needed"),
    ("SA-C-164", "boundary"): ("The settlement statement of a store with Salla Payments, showing the currency in which funds are settled and transferred",
        "record a journey", "founder", "Merchant dashboard https://s.salla.sa/payments/wallet/transfer-cycle-invoices (تحصيل المدفوعات; the path as the dashboard's payments.json names it), as the owner of a store with Salla Payments active in each market (SA, AE, KW)",
        "No held journey shows a settlement; the help articles read state the currency per market only: {read}", "observation needed"),
    ("SA-C-167", "where"): ("The page where Salla lists the countries it serves and how each is offered (separate site version, entity or service)",
        "save a page from a browser", "founder", SC + "gcc-ecommerce", SALLA_403 + "; the held salla.com footer lists 'مدعوم في: السعودية الامارات' only (structures/salla/com-plans).", "observation needed"),
    ("SA-C-167", "responsible"): ("The usage agreement's clause naming the entity that contracts with merchants in each country",
        "save a page from a browser", "founder", SC + "ar-ae/terms", SALLA_403 + "; the held sitemaps list per-country versions of the terms (sitemap_ar-AE.xml, sitemap_en-AE.xml) but not their text.", "observation needed"),
    ("SA-C-167", "boundary"): ("The sign-up or onboarding step where a merchant picks a country, showing what the choice connects to (documents, payments, shipping)",
        "record a journey", "founder", "Store sign-up at https://s.salla.sa/auth/register (the sign-up link in salla.com's navigation, held in observed-sa salla.com/ai-info) and the onboarding that follows, as a new merchant choosing a country other than SA, AE or KW",
        "The held text says only 'اختيارك للدولة يحدِّد المتطلبات القانونية اللازمة لمتجرك.' (dashboard-translations persona.json); no journey choosing another country is held.", "observation needed"),
    ("SA-C-177", "where"): ("The dashboard step where the payment services contract (عقد خدمات الدفع) is presented and signed",
        "record a journey", "founder", PAY_JOURNEY, "No held journey goes through store verification; help articles say only that the contract is signed during verification (SA-S-0081).", "observation needed"),
    ("SA-C-177", "responsible"): ("The contract's party clause: which Salla entity or payment company signs with the merchant",
        "record a journey", "founder", PAY_JOURNEY, "The contract is not public and no held journey shows it.", "observation needed"),
    ("SA-C-177", "boundary"): ("How the signed contract is attached to the store: the acceptance step, its version and where a signed copy is kept",
        "record a journey", "founder", PAY_JOURNEY, "No held journey shows the signing step.", "observation needed"),
    ("SA-C-177", "reason"): ("A stated reason for signing a separate payment services contract during verification",
        "ask the platform", "founder", "Question to Salla merchant support: why is a separate payment services contract (عقد خدمات الدفع) signed during store verification, and with which entity?",
        "The help articles read name the contract but give no reason: {read}", "searched, not found"),
    ("SA-C-201", "where"): ("A statement of where API rate limits are enforced (per app, per store, at a gateway)",
        "ask the platform", "founder", "Question to partners@salla.sa: where are the Merchant API rate limits enforced and counted (per app, per store or per token)?",
        "The rate-limiting page read states limits per plan and the headers returned, not where they are enforced: {read}", "searched, not found"),
    ("SA-C-207", "decides"): ("The Partners portal's conditions for using the Report Builder (feature flag, plan, approval)",
        "record a journey", "founder", "Partners portal > Report Builder, as a partner on the account used for observed-sa (partner@en)",
        "The docs read describe the tool, not who may use it: {read}; the held Partners portal menu (portal-menu-definitions) has no Report Builder entry.", "observation needed"),
    ("SA-C-175", "boundary"): ("The step where a partner accepts the App Store terms when submitting an app for publication",
        "record a journey", "founder", "Partners portal > Apps > an app > publication request, as a partner",
        "The terms read (" + APPS_POLICY + ") do not say how they are accepted; no held journey submits an app for publication.", "observation needed"),
    ("SA-C-304", "decides"): ("The answers to the page's FAQ ('من يمكنه التسجيل كشريك؟', 'هل لازم أكون في السعودية؟', 'هل التسجيل عليه رسوم او التزام؟')",
        "record a journey", "either", "https://partners.salla.com/global-selling-program: open each FAQ item and save the page",
        "The answers are collapsed; neither the rendered text nor the HTML fetched on 2026-10-11 holds them.", "observation needed"),
    ("SA-C-301", "responsible"): ("The terms a partner accepts when buying or transferring a domain in the Partners portal",
        "record a journey", "founder", "Partners portal > Domains > Domains Management / Transfer Domain, as a partner whose account has the domain-purchase feature",
        "The held Partners portal menu names the section (portal-menu-definitions) but no held journey opens it, and no partners.salla.com legal page names domains.", "observation needed"),
    ("SA-C-235", "where"): ("A statement of where Salla handles a payment gateway or carrier being unavailable (status page, fallback setting, support)",
        "ask the platform", "founder", "Question to Salla merchant support: what happens to orders, payments and shipments when a payment gateway or a carrier is unavailable, and where is it handled?",
        "Read and none says it: {read}; the status page (status.salla.sa) lists Salla's own components only.", "searched, not found"),
    ("SA-C-235", "decides"): ("A setting or rule that decides what happens when a partner is unavailable (fallback gateway or carrier)",
        "ask the platform", "founder", "Question to Salla merchant support: can a store set a fallback payment gateway or carrier, and who decides when one is unavailable?",
        "Read and none states it: {read}; the carrier auto-assignment text covers a carrier not serving the customer's area, not a carrier being down (SA-S-0162).", "searched, not found"),
    ("SA-C-235", "reason"): ("A stated reason for how Salla handles an unavailable partner",
        "ask the platform", "founder", "Question to Salla merchant support: why is an unavailable payment gateway or carrier handled as it is?",
        "Read and none gives a reason: {read}", "searched, not found"),
    ("SA-C-166", "decides"): ("A statement of who maintains the countries, cities and districts lists and whether a merchant can change them",
        "ask the platform", "founder", "Question to partners@salla.sa: who maintains the countries, cities and districts returned by the Merchant API, and can a store change them?",
        "The held API lists name the resources (Countries, Cities, Districts) and the scope metadata.read, not who sets their values.", "searched, not found"),
    ("SA-C-101", "decides"): ("A statement of what limits or switches the storefront APIs per store or plan",
        "ask the platform", "founder", "Question to partners@salla.sa: are the storefront APIs (Twilight JS SDK) limited or switched per store or plan?",
        "Read and none states it: {read}", "searched, not found"),
}
for c, url, what in [("SA-C-170", TERMS, "the usage agreement (اتفاقية الاستخدام)"), ("SA-C-171", PRIVACY, "the privacy policy (سياسة الخصوصية)"),
                     ("SA-C-172", SC + "policies/selling-policies", "the selling policy (سياسة البيع)"),
                     ("SA-C-180", SC + "policies/nd96", "the policy published at /policies/nd96"),
                     ("SA-C-233", PRIVACY, "the privacy policy (سياسة الخصوصية)"), ("SA-C-230", TERMS, "the usage agreement (اتفاقية الاستخدام)")]:
    WHAT = {
        "where": f"The clause of {what} that says where it applies and where Salla keeps it",
        "decides": f"The clause of {what} on who may change it, and the conditions it sets",
        "responsible": f"The party clause of {what}: the Salla entity that is bound by it and what each party answers for",
        "boundary": f"How {what} is accepted and linked to the account (the acceptance step and the version accepted)",
        "reason": f"A reason {what} gives for its terms",
    }
    if c == "SA-C-233":
        WHAT.update({"where": "The privacy policy's statement of where personal data is stored and processed (country, hosting provider)",
                     "decides": "The privacy policy's statement of who decides where data is stored and how a person exercises their rights",
                     "responsible": "The privacy policy's statement of the controller and processors of personal data",
                     "boundary": "The privacy policy's statement of transfers of personal data to third parties or abroad",
                     "reason": "A reason the privacy policy gives for where data is stored"})
    if c == "SA-C-230":
        WHAT.update({"where": "The usage agreement's party clause naming the Salla entity for each market (Saudi Arabia, UAE, Kuwait)",
                     "decides": "The clause that says which entity applies to a store, and whether it follows the store's country",
                     "boundary": "The contract that links each entity to the merchant (the agreement for each market)",
                     "reason": "A stated reason for contracting through different entities per country"})
    for p in ("where", "decides", "responsible", "boundary", "reason"):
        OVR[(c, p)] = (WHAT[p], "save a page from a browser", "founder", url, SALLA_403 + "; no other held page carries its text.", "observation needed")
OVR[("SA-C-173", "reason")] = ("A reason the affiliate and referral programme terms give for how the programme is run",
    "save a page from a browser", "founder", SC + "%D8%A7%D8%AA%D9%81%D8%A7%D9%82%D9%8A%D8%A9-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A7%D9%84%D8%AA%D8%B3%D9%88%D9%8A%D9%82-%D8%A8%D8%A7%D9%84%D8%B9%D9%85%D9%88%D9%84%D8%A9",
    SALLA_403 + "; the partners copy read (https://partners.salla.com/legal/privacy-affiliate) and the help article read give no reason: {read}", "observation needed")
OVR[("SA-C-232", "reason")] = ("A reason Salla gives for the activities it restricts or the screening it applies",
    "save a page from a browser", "founder", TERMS, SALLA_403 + "; the policies read list restricted products without a reason: {read}", "observation needed")
OVR[("SA-C-234", "responsible")] = ("The usage agreement's clause on who answers for the security of accounts, stores and data",
    "save a page from a browser", "founder", TERMS, SALLA_403 + "; the help and docs pages read describe measures, not responsibility: {read}", "observation needed")
OVR[("SA-C-115", "responsible")] = ("Salla's statement of who collects and holds cash-on-delivery amounts collected through Salla shipping labels before they are paid out",
    "save a page from a browser", "founder", SC + "shipping",
    SALLA_403 + "; the help articles read give the payout days, not who holds the amounts: {read}", "observation needed")
