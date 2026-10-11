# Q1 map, side by side

Each match pairs concerns whose platforms' own terms clearly match (`matches.tsv`). Under each placement, each platform is quoted in its own words: the identifier it uses, an excerpt of its statement (cut at 160 characters where marked), the scope it holds for, and the citation. A gap shows its kind. Differences are left for the reader.

## M-001

Shopify: SH-C-002 Shopify Contracting Party for the platform services, by the merchant's billing region; Salla: SA-C-230 Salla's legal entities and the contracting entity per country; WooCommerce: WC-C-023 Contracting entity for Woo services, WC-C-026 Governing law and courts

Basis: SH-C-002 platform_terms "Shopify Contracting Party"; statement SH-S-0001 "You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store."; statement SH-S-0010 "governed by and interpreted in accordance with the laws of the Province of Ontario" | SA-C-230 statement SA-S-5001 "شركة منصة سلة للاتصالات وتقنية المعلومات (شخص واحد) ، المملكة العربية السعودية"; platform_terms "Salla Holding Company" | WC-C-023 statement WC-S-0459 "If you reside outside of the Designated Countries: WooCommerce, Inc."; statement WC-S-0461 "collectively as “Automattic,” “us,” or “we” throughout these Terms" | WC-C-026 platform_terms "Jurisdiction and Applicable Law"; statement WC-S-0488 "governed by the laws of the state of California"

### Where it lives

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

### Who decides

- **Shopify**
  - `13. Shopify Contracting Party and Forum`: Contracting Party. You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store. (SH-S-0001)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `1. Who's Who`: We use the term “Designated Countries” to refer to Australia, Canada, Japan, Mexico, New Zealand, Russia, and all countries located in Europe. (WC-S-0457)
  - `15. Jurisdiction and Applicable Law`: Nothing in this Agreement affects your rights as a consumer to rely on mandatory provisions in your country of residence. (WC-S-5328)

### Who is legally responsible

- **Shopify**
  - `13. Shopify Contracting Party and Forum, table row "United States or Canada"`: Shopify Inc., a Canadian corporation [scope: billing address in the United States or Canada] (SH-S-0002)
  - `Shopify's primary contracting entities`: Shopify Inc.: A Canadian-registered entity contracting with merchants in the United States or Canada. [scope: merchants in the United States or Canada] (SH-S-0242)
  - `13. Shopify Contracting Party and Forum, table row "United States or Canada"`: Shopify Technology (USA) Inc., a Nevada corporation [scope: billing address in the United States or Canada] (SH-S-0003)
  - `13. Shopify Contracting Party and Forum, table row "Asia Pacific"`: Shopify Commerce Singapore Pte. Ltd, a corporation formed under the laws of Singapore [scope: billing address in Asia Pacific (including Australia, New Zealand, China, Japan, and Singapore)] (SH-S-0005)
  - `13. Shopify Contracting Party and Forum, table row "All other jurisdictions"`: Shopify International Limited, a private company limited by shares incorporated in Ireland under registration number 560279 [scope: billing address in all other jurisdictions (including EMEA, Europe, the Middle East, Africa, South America, the Caribbean, and Mexico)] (SH-S-0007)
  - `Shopify's primary contracting entities`: Shopify International Limited: An Irish-registered entity contracting with merchants in Europe, the Middle East, and Africa (EMEA) and Latin America (LATAM). [scope: merchants in EMEA and LATAM] (SH-S-0241)
  - and 4 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `سياسة الشروط والاستخدام – متجر تطبيقات سلة > المقدّمة`: ترحب منصة "سلّة" المملوكة لشركة تطبيق سلة لتقنية المعلومات (س.ت: 4031200589) (SA-S-0015)
  - `سياسة الانضمام إلى برنامج شركاء سلة > تمهيد`: ترحّب بكم منصة شركاء سلّة، التابعة لمنصة سلّة والمملوكة لشركة تطبيق سلّة لتقنية المعلومات، والمسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري [cut] (SA-S-0016)
  - `المادة الأولى – المقدّمة والتعريفات`: منصة سلة: تعني شركة تطبيق سلة لتقنية المعلومات، وتشمل جميع قنواتها الإلكترونية (كموقعها الإلكتروني، أو التطبيق). (SA-S-0017)
  - `الشروط والأحكام لاستخدام متجر الثيمات > المقدمة`: ترحب منصة «سلة» (المملوكة لشركة منصة سلة للاتصالات وتقنية المعلومات، سجل تجاري رقم: 7011845513) (SA-S-0018)
  - `اتفاقية استخدام برنامج التسويق بالعمولة > المقدمة`: تُرحّب منصة سلّة المملوكة لشركة منصة سلة للاتصالات وتقنية المعلومات (شركة شخص واحد) ذات السجل التجاري رقم: 4031200589 (SA-S-0019)
  - `footer`: جميع الحقوق محفوظة لشركة سلة القابضة © 2026 (SA-S-0020)
  - and 5 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `1. Who's Who: Woo Services`: Woo services include WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet, and other products or services available at WooCommerce.com. (WC-S-0458)
  - `1. Who's Who: Woo Services`: If you reside outside of the Designated Countries: WooCommerce, Inc. [scope: residents outside the Designated Countries] (WC-S-0459)
  - `1. Who's Who: Woo Services`: If you reside in the Designated Countries: WooCommerce Ireland Ltd. [scope: residents of the Designated Countries] (WC-S-0460)
  - `1. Who's Who`: We refer to Automattic Inc., Aut O’Mattic A8C Ireland Ltd., WooCommerce, Inc., and WooCommerce Ireland Ltd. collectively as “Automattic,” “us,” or “we” througho [cut] (WC-S-0461)
  - `Terms of Service (opening)`: Please note that Woo-related products and services are intended for commercial use and you acknowledge that your use is that of a representative of a business ( [cut] (WC-S-0456)
  - `Terms of Service (opening)`: These Terms govern your access to and use of the software, applications, extensions, and other products and services we provide through or for WordPress.com, Wo [cut] (WC-S-0643)
  - and 2 more statements in `platforms/woocommerce/statements.tsv`

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

## M-002

Shopify: SH-C-001 Shopify account and Store Owner; Salla: SA-C-001 Merchant account and profile (Your profile / الملف الشخصي)

Basis: SH-C-001 platform_terms "Store Owner"; statement SH-S-0019 "the person signing up for the Service by opening an Account will be the contracting party" | SA-C-001 statement SA-S-1622 "Store Owner Changed"; statement SA-S-1622 "تغيير مالك المتجر"; platform_terms "account_setting_management"

### Where it lives

- **Shopify**
  - `Your store`: "text": "Your store" (SH-S-2520)
  - `destinations/ShopsOnlyActiveDestinations`: "endpoint": "/api/operations/{hash}/ShopsOnlyActiveDestinations/destinations" (SH-S-7184)
- **Salla**
  - `Your profile`: {"position": 1, "kind": "link", "text": "Your profile", "href": "/profile"} (SA-S-1677)
  - `Edit profile`: "profile/edit-profile":"Edit profile" (SA-S-1762)
  - `Registered devices`: "profile/recent-access-devices":"Registered devices" (SA-S-1763)
  - `Quick access`: "profile/quick-login":"Quick access" (SA-S-1764)
  - `@salla.sa/ui-merchant-login`: {"id": 1728225593018, "name": "@salla.sa/ui-merchant-login", "Prod": {}, "env": "prod", "path": "/^\\/auth/", "position": 5} (SA-S-3534)
  - `Merchant`: "id": 841814, "name": "Merchant", "key": "apiDetailFolder.841814", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSet [cut] (SA-S-1061)

### Who decides

- **Shopify**
  - `1. Account Terms`: To complete your Account registration, you must provide us with your full legal name, business address, phone number, a valid email address, and any other infor [cut] (SH-S-0017)
- **Salla**
  - `تطبيق إدارة المتجر على أجهزة iOS و Android`: "sub_features": [{"parent_code": "adar-alhsab-oalmtgr", "title": "تطبيق إدارة المتجر على أجهزة iOS و Android", "description": null, "icon": null, "icon_color":  [cut] [scope: plan: سلة بلس] (SA-S-2082)
  - `حفظ الحسابات المفتوحة مؤخراً عند تسجيل الدخول`: "extra_icons": null}, {"parent_code": "adar-alhsab-oalmtgr", "title": "حفظ الحسابات المفتوحة مؤخراً عند تسجيل الدخول", "description": null, "icon": null, "icon_ [cut] [scope: plan: سلة بلس] (SA-S-2086)
  - `account_setting_management`: "label": "webhook management"}, {"id": 839117208, "name": "account_setting_management", "label": "account setting management"}, {"id": 266864793, "name": "busin [cut] (SA-S-2409)
  - `account_setting_management`: "en": "webhook management"}}, {"id": 839117208, "key": "account_setting_management", "name": {"ar": "التحكم بالحساب", "en": "account setting management"}}, {"id [cut] (SA-S-2626)
  - `store-two-factor-authentication`: {"position": 221, "name": "store-two-factor-authentication", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [] [cut] [scope: plans: plus, pro, special] (SA-S-3182)
  - `biometric-verification`: {"position": 404, "name": "biometric-verification", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": [cut] [scope: plans: plus, pro, special] (SA-S-3365)

### Who is legally responsible

- **Shopify**
  - `2.1 Store Owner`: the person signing up for the Service by opening an Account will be the contracting party ("Store Owner") for the purposes of our Terms of Service (SH-S-0019)
  - `2. Account Activation (summary)`: The Store Owner is responsible for the Account, is bound by these Terms of Service and is responsible for the actions of others accessing the Account. (SH-S-0228)
  - `2.1 Store Owner`: Your Shopify Store can only be associated with one Store Owner. A Store Owner may have multiple Shopify Stores. (SH-S-0238)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `preamble`: By signing up for a Shopify Account (as defined in Section 1) or by using any Shopify Services (as defined below), you are agreeing to be bound by the following [cut] (SH-S-0229)
  - `preamble`: including Shopify's Acceptable Use Policy ("AUP") and Privacy Policy, and, if applicable, the Supplementary Terms of Service for E.U. Merchants ("EU Terms"), th [cut] (SH-S-0076)
- **Salla**
  - `Merchant`: "id": 841814, "name": "Merchant", "key": "apiDetailFolder.841814", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSet [cut] (SA-S-1061)
  - `settings`: {"id": 13, "slug": "settings", "icon": "sicon-settings", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_w [cut] (SA-S-1545)
  - `store.owner.changed`: {"id": 36841469, "slug": "store.owner.changed", "url": "https://salla.sa", "order": 2, "is_enabled": true, "name": {"ar": "تغيير مالك المتجر", "en": "Store Owne [cut] (SA-S-1622)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-003

Shopify: SH-C-068 Onboarding, KYC and underwriting for Shopify Payments; Salla: SA-C-006 Store verification of the merchant's legal entity (Store Verification / توثيق المتجر); WooCommerce: WC-C-009 WooPayments know-your-customer verification

Basis: SH-C-068 platform_terms "read_financial_kyc_information"; statement SH-S-0132 "Before you can use the Payment Services, you need to pass our identity and KYC checks." | SA-C-006 statement SA-S-1881 "Store Verification"; statement SA-S-1881 "/payments/kyc"; platform_terms "kyc_new_workflow"; platform_terms "توثيق المتجر" | WC-C-009 platform_terms "Know Your Customer"; platform_terms "KYC"

### Where it lives

- **Shopify**
  - `profile-assessment:root`: "path":"profile-assessment/" (SH-S-5254)
  - `ProfileAssessment`: "section":"ProfileAssessment" (SH-S-1594)
- **Salla**
  - `Store Verification`: {"position": 111, "kind": "link", "text": "Store Verification", "href": "/payments/kyc", "parent": 0, "list": 9} (SA-S-1881)
  - `@salla.sa/ui-merchant-payments`: {"id": 1729596362158, "name": "@salla.sa/ui-merchant-payments", "Prod": {}, "env": "prod", "path": "/^(/payments(?!/taxes)\|/entity/verifications\|/checkout)(/.*\| [cut] (SA-S-3549)
- **WooCommerce**
  - `WooPayments built in partnership with Stripe`: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the  [cut] (WC-S-0504)
  - `How quickly will you confirm my identity?`: We’ll do our best to work with Stripe to confirm your identity as quickly as we can. (WC-S-0522)

### Who decides

- **Shopify**
  - `help.shopify.com/en/manual/payments/shopify-payments/onboarding/acceptable-busin`: Your business is evaluated when you first apply for Shopify Payments, and risk is continuously monitored throughout your use of the platform. (SH-S-0331)
  - `help.shopify.com/en/manual/payments/shopify-payments/onboarding/acceptable-busin`: If a review identifies practices that create elevated risk or undermine customer trust, then your account might be declined, deactivated, or subject to restrict [cut] (SH-S-0332)
  - `Review criteria, Transaction and operational patterns`: Historical patterns across any businesses that you operate. (SH-S-0337)
  - `Account holds after receiving orders`: However, if Shopify's banking partners require more information for your business, then your Shopify Payments account is put on hold until your details can be v [cut] (SH-S-0357)
  - `Part I, B. Verification and Underwriting`: The Payment Processors may hold funds in your Shopify Payments Account while awaiting the information requested above. (SH-S-0106)
  - `Part I, A. Onboarding, KYC and underwriting`: Before you can use the Payment Services, you need to pass our identity and KYC checks. [scope: EU / EEA and United Kingdom (Payment Facilitator Terms)] (SH-S-0132)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `business_certificate_management`: "label": "account setting management"}, {"id": 266864793, "name": "business_certificate_management", "label": "business certificate management"}, {"id": 1505040 [cut] (SA-S-2410)
  - `business_certificate_management`: "en": "account setting management"}}, {"id": 266864793, "key": "business_certificate_management", "name": {"ar": "شهادة توثيق منصة الأعمال", "en": "business cer [cut] (SA-S-2627)
  - `kyc_new_workflow`: {"position": 140, "name": "kyc_new_workflow", "value": {"enabled": true, "released": true, "plans": [], "countries": ["AE", "SA", "KW", "QA", "OM", "BH"], "type [cut] [scope: countries: AE, SA, KW, QA, OM, BH] (SA-S-3101)
  - `wathq-v6`: {"position": 223, "name": "wathq-v6", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3184)
  - `sbc-registration`: {"position": 224, "name": "sbc-registration", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3185)
  - `ثانياً: نظرة عامة عن متجرك`: 🌍دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها. [scope: الإمارات (article: إنشاء متجر جديد خارج السعودية - الإمارات)] (SA-S-0141)
  - and 5 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `“Know your customer”`: Because the payments sector is heavily regulated, we must gather certain information from you before you’ll be able to use WooPayments. (WC-S-0516)
  - `How do I delete my WooPayments account?`: WooPayments accounts contain information that we must retain for tax and compliance purposes. (WC-S-0558)

### Who is legally responsible

- **Shopify**
  - `Part I, A. Privacy`: Each Payment Processor may also process your personal data or Customer Payment Data as an independent controller, for example, to comply with their own regulato [cut] (SH-S-0099)
  - `Part I, A. Privacy of Others`: the applicable Payment Processor may also process personal data as an independent controller for certain processing activities, including but not limited to com [cut] (SH-S-0100)
  - `Why we process your information`: compliance with a legal obligation to use copies of government-issued identification that you provide us to comply with different laws such as "know your custom [cut] (SH-S-0180)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (page not read)

### How it meets the rest

- **Shopify**
  - `read_financial_kyc_information`: The webhook topic for `finance_app_staff_member/delete` events. Triggers when a staff with access to all or some finance app has been removed. Requires the `rea [cut] (SH-S-5990)
  - `read_financial_kyc_information`: The webhook topic for `finance_app_staff_member/grant` events. Triggers when a staff is granted access to all or some finance app. Requires the `read_financial_ [cut] (SH-S-5991)
  - `read_financial_kyc_information`: The webhook topic for `finance_app_staff_member/revoke` events. Triggers when a staff's access to all or some finance app has been revoked. Requires the `read_f [cut] (SH-S-5992)
  - `read_financial_kyc_information`: The webhook topic for `finance_app_staff_member/update` events. Triggers when a staff's information has been updated. Requires the `read_financial_kyc_informati [cut] (SH-S-5993)
  - `read_financial_kyc_information`: The webhook topic for `finance_kyc_information/update` events. Occurs whenever shop's finance KYC information was updated Requires the `read_financial_kyc_infor [cut] (SH-S-5994)
  - `read_financial_kyc_information`: `read_financial_kyc_information` (SH-S-1122)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `1. ادخل بيانات مالك المتجر بدقة`: سترسل رسالة نصية من أبشر إلى رقم مالك المتجر الذي تم تسجيله في الخطوة السابقة. [scope: السعودية (article: توثيق متجرك الجديد في السعودية)] (SA-S-0132)
  - `توثيق متجرك في الإمارات`: يُعد توثيق المتجر من الخطوات الأخيرة لتجهيز متجرك على سلة للعمل في الإمارات، كما يتيح لك الانتقال إلى تفعيل المدفوعات الإلكترونية لعملائك. [scope: الإمارات (article: توثيق متجرك في الإمارات)] (SA-S-0137)
  - `common.verification_required_tooltip`: مطلوب توثيق المتجر لتفعيل طريقة الدفع هذه. (SA-S-0108)
- **WooCommerce**
  - `WooPayments built in partnership with Stripe`: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the  [cut] (WC-S-0504)

### Stated reason

- **Shopify**
  - `Shopify Payments risk standards and card network thresholds`: Although payment networks such as Visa and Mastercard publish chargeback thresholds, your store is evaluated against a higher standard to maintain merchant and  [cut] (SH-S-0333)
  - `Shopify Payments risk standards and card network thresholds`: A small number of merchants who harm customers make every other merchant on the platform look less trustworthy to banks and card networks. (SH-S-0334)
- **Salla**
  - `لماذا يجب توثيق متجرك؟`: - الالتزام بالمتطلبات النظامية والتنظيمية للتجارة الإلكترونية. [scope: السعودية (article: توثيق متجرك الجديد في السعودية)] (SA-S-0131)
  - `answer4`: نعم، تُعتبر شهادة توثيق التجارة الإلكترونية من منصة الأعمال إلزامية، وأي متجر لا يملكها يُعد مخالفًا لأنظمة وزارة التجارة. (SA-S-0118)
- **WooCommerce**
  - `Why do I have to share this information?`: We follow the same regulations as other financial institutions so that we can ensure we operate in an ethical and trustworthy manner. (WC-S-0521)
  - `“Know your customer”`: Because the payments sector is heavily regulated, we must gather certain information from you before you’ll be able to use WooPayments. (WC-S-0516)

## M-004

Shopify: SH-C-009 Users and staff accounts, SH-C-010 Roles and permissions; Salla: SA-C-009 Staff accounts, roles and permissions (Staff members; Roles & permissions); WooCommerce: WC-C-080 Roles and capabilities

Basis: SH-C-009 platform_terms "Staff Accounts" | SH-C-010 platform_terms "Roles"; platform_terms "permissions" | SA-C-009 platform_terms "Staff members"; platform_terms "Roles & permissions"; platform_terms "إدارة الأدوار الوظيفية" | WC-C-080 statement WC-S-0883 "WooCommerce adds two user roles—Customer and Shop Manager—and extends the existing Administrator role with store management capabilities."

### Where it lives

- **Shopify**
  - `user_management`: "title": "Users" (SH-S-1482)
  - `Account`: "section":"Account" (SH-S-1540)
  - `roles`: "title": "Roles" (SH-S-1483)
- **Salla**
  - `Staff members`: {"position": 79, "kind": "link", "text": "Staff members", "href": "/users", "parent": 0, "list": 5} (SA-S-1849)
  - `Roles & permissions`: {"position": 81, "kind": "link", "text": "Roles & permissions", "href": "/users/roles", "parent": 0, "list": 5} (SA-S-1851)
  - `Employees targets`: {"position": 83, "kind": "link", "text": "Employees targets", "href": "/users/targets", "parent": 0, "list": 5} (SA-S-1853)
  - `@salla.sa/ui-merchant-users`: {"id": 1728571084162, "name": "@salla.sa/ui-merchant-users", "Prod": {}, "env": "prod", "path": "/users", "position": 15} (SA-S-3544)
  - `Employees`: "id": 841813, "name": "Employees", "key": "apiDetailFolder.841813", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1066)
- **WooCommerce**
  - `WooCommerce user roles`: WooCommerce adds two user roles—Customer and Shop Manager—and extends the existing Administrator role with store management capabilities. (WC-S-0883)

### Who decides

- **Shopify**
  - `settings-account:invite`: "eligibility":{"permissions":["STAFF_MANAGEMENT_CREATE"]} (SH-S-5003)
  - `settings-account:edit`: "eligibility":{"excluded":{"oneOf":[{"features":["rbacEnabled"]},{"features":["hasOrgSettings"]}]}} (SH-S-5004)
  - `2.2 Staff Accounts`: With Staff Accounts, the Store Owner can set permissions and let other people work in their Account while determining the level of access by Staff Accounts to s [cut] (SH-S-0021)
  - `2.2 Staff Accounts`: Based on your Shopify pricing plan, you can create one or more staff accounts ("Staff Accounts") allowing other people to access the Account. (SH-S-0020)
  - `settings:organizations:accounts`: "eligibility":{"oneOf":[{"features":["hasOrgSettings"]},{"features":["rbacEnabled"]}]} (SH-S-5233)
  - `settings:organizations:accounts:create`: "eligibility":{"organizationPermissions":["INVITE_USERS"]} (SH-S-5240)
  - and 19 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `زيادة عدد المستخدمين *برسوم إضافية`: "sub_features": [{"parent_code": "mothfo-almtgr", "title": "زيادة عدد المستخدمين *برسوم إضافية", "description": null, "icon": null, "icon_color": null, "icon_ba [cut] [scope: plan: سلة بلس] (SA-S-2078)
  - `إدارة الأدوار الوظيفية`: "extra_icons": null}, {"parent_code": "mothfo-almtgr", "title": "إدارة الأدوار الوظيفية", "description": null, "icon": null, "icon_color": null, "icon_backgroun [cut] [scope: plan: سلة بلس] (SA-S-2079)
  - `إضافة حسابات الموظفين وإدارة صلاحياتهم`: "extra_icons": null}]}, {"title": "إضافة حسابات الموظفين وإدارة صلاحياتهم", "description": "أضف طاقم العمل للوحة التحكم لإدارة الطلبات وضمان سير العمل بسلاسة",  [cut] [scope: plan: سلة برو] (SA-S-2143)
  - `users_browse`: "permissions": [{"id": 1714257133, "name": "users_browse", "label": "users browse"}, {"id": 806067182, "name": "users_management", "label": "users management"}, [cut] (SA-S-2426)
  - `users_management`: "label": "users browse"}, {"id": 806067182, "name": "users_management", "label": "users management"}, {"id": 231783151, "name": "roles_browse", "label": "roles  [cut] (SA-S-2427)
  - `roles_browse`: "label": "users management"}, {"id": 231783151, "name": "roles_browse", "label": "roles browse"}, {"id": 1606277608, "name": "roles_management", "label": "roles [cut] (SA-S-2428)
  - and 3 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `WooCommerce user roles`: To assign roles, go to Users > All Users in the WordPress admin, select a user, and choose a role from the Role dropdown. (WC-S-0884)
  - `WC_Install::get_core_capabilities`: * Get capabilities for WooCommerce - these are assigned to admin/shop manager during installation or reset. (WC-S-5415)
  - `WC_Install::get_core_capabilities`: $capabilities['core'] = array( 'manage_woocommerce', 'create_customers', 'view_woocommerce_reports', ); (WC-S-5416)
  - `wc_rest_check_user_permissions`: // Check to allow shop_managers to manage only customers. (WC-S-5417)

### Who is legally responsible

- **Shopify**
  - `2.2 Staff Accounts`: The Store Owner is responsible for: (a) ensuring its employees, agents and subcontractors, including via Staff Accounts, comply with these Terms of Service; and [cut] (SH-S-0231)
  - `2.2 Staff Accounts`: The Store Owner is responsible for: (a) ensuring its employees, agents and subcontractors, including via Staff Accounts, comply with these Terms of Service; and [cut] (SH-S-0231)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_users`: Requires `read_financial_kyc_information` access scope or `read_users` access scope. (SH-S-6142)
  - `read_users`: Requires `read_users` access scope. Also: The app must be a finance embedded app or installed on a Shopify Plus or Advanced store. Contact Shopify Support to en [cut] (SH-S-6143)
  - `read_users`: The User resource is available for [private apps](https://shopify.dev/concepts/apps#private-apps) and [custom apps](https://shopify.dev/concepts/apps#custom-app [cut] (SH-S-6144)
  - `read_users`: \| `read_users`Shopify approval required \| `StaffMember` Shopify PlusThis type is available to finance embedded apps, and to apps installed on a store on the Sho [cut] (SH-S-6145)
  - `read_users`: `read_users` (SH-S-1146)
  - `ServerIntent create user`: "variables": {"action": "create", "type": "user" [scope: store ts15uk-ug] (SH-S-7244)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Employees`: "id": 841813, "name": "Employees", "key": "apiDetailFolder.841813", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1066)
- **WooCommerce**
  - `woocommerce_shop_manager_editable_roles`: $shop_manager_editable_roles = apply_filters( 'woocommerce_shop_manager_editable_roles', array( 'customer' ) ); (WC-S-5418)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-005

Shopify: SH-C-012 Merchant audit log and admin API activity; Salla: SA-C-010 Activity and audit logs (Activity history; Logs)

Basis: SH-C-012 platform_terms "MerchantAuditLog"; platform_terms "read_audit_events" | SA-C-010 platform_terms "audit_logs_management"; platform_terms "advance-audit-log"; platform_terms "سجل العمليات"

### Where it lives

- **Shopify**
  - `merchant-audit-log:list`: "path":"audit" (SH-S-5206)
  - `MerchantAuditLog`: "section":"MerchantAuditLog" (SH-S-1581)
- **Salla**
  - `Activity history`: {"position": 119, "kind": "link", "text": "Activity history", "href": "/logs/audit", "parent": 0, "list": 11} (SA-S-1889)
  - `Export log`: {"position": 120, "kind": "link", "text": "Export log", "href": "/logs/export", "parent": 0, "list": 11} (SA-S-1890)
  - `@salla.sa/ui-merchant-logs`: {"id": 1729420520665, "name": "@salla.sa/ui-merchant-logs", "Prod": {}, "env": "prod", "path": "/logs", "position": 19} (SA-S-3548)

### Who decides

- **Shopify**
  - `merchant-audit-log:list`: "eligibility":{"permissions":["STAFF_AUDIT_LOG_VIEW"],"betas":["32151445"]} (SH-S-5207)
  - `settings:organizations:accounts:security:activity-log`: "eligibility":{"organizationPermissions":["VIEW_ALL_AUDIT_EVENTS"],"features":["rbacEnabled"]} (SH-S-5239)
  - `features.rbacEnabled`: {"set": 0, "section": "features", "key": "rbacEnabled", "value": true} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-advanced (plan not stated); capture-client-store-vny2vy5w (Custom plan, development store); capture-client-store-vny2vy5w (plan not stated); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-grow (plan not stated); capture-plus (Shopify Plus App Development, development store); capture-plus (plan not stated); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); demo-fake-dev-store (plan not stated); fake-demo-sharrwah (trial); fake-demo-sharrwah (plan not stated); fake-demo-sharrwah (Advanced); hjhjhjjjhj (plan not stated); ibx5bt-xy (trial); ibx5bt-xy (plan not stated); ts15uk-ug (trial); ts15uk-ug (plan not stated); zyd38b-ze (trial)] (SH-S-5307)
  - `features.rbacEnabled`: {"set": 0, "section": "features", "key": "rbacEnabled", "value": false} [scope: ctcbwa-r1 (trial); ibx5bt-xy (trial); zyd38b-ze (trial)] (SH-S-5318)
- **Salla**
  - `سجل التصدير`: "sub_features": [{"parent_code": "almzaya-almtkdm", "title": "سجل التصدير", "description": null, "icon": null, "icon_color": null, "icon_background": null, "ext [cut] [scope: plan: سلة برو] (SA-S-2122)
  - `سجل العمليات`: "extra_icons": null}, {"parent_code": "almzaya-almtkdm", "title": "سجل العمليات", "description": null, "icon": null, "icon_color": null, "icon_background": null [cut] [scope: plan: سلة برو] (SA-S-2123)
  - `audit_logs_management`: "label": "payments operations management"}, {"id": 339762668, "name": "audit_logs_management", "label": "audit logs management"}, {"id": 1703909243, "name": "wh [cut] (SA-S-2421)
  - `export_logs_management`: "label": "whatsapp chat browse"}, {"id": 1895195893, "name": "export_logs_management", "label": "export logs management"}, {"id": 1121747958, "name": "custom_fi [cut] (SA-S-2423)
  - `audit_logs_management`: "en": "payments operations management"}}, {"id": 339762668, "key": "audit_logs_management", "name": {"ar": "سجل العمليات", "en": "audit logs management"}}, {"id [cut] (SA-S-2638)
  - `export_logs_management`: "en": "whatsapp chat browse"}}, {"id": 1895195893, "key": "export_logs_management", "name": {"ar": "سجل التصدير", "en": "export logs management"}}, {"id": 11217 [cut] (SA-S-2640)
  - and 2 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `read_audit_events`: The webhook topic for `audit_events/admin_api_activity` events. Triggers for each auditable Admin API request. This topic is limited to one active subscription  [cut] (SH-S-5938)
  - `audit_events/admin_api_activity`: "value": "audit_events/admin_api_activity" (SH-S-1157)
  - `read_audit_events`: "text": "read_audit_events" (SH-S-0947)
- **Salla**: gap (searched, not found)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `سجل العمليات`: هي صفحة تجمع بيانات العمليات اليومية لمتجرك لتتمكن -أنت أو موظفو متجرك- من مراجعة هذه العمليات وتحليلها وحصرها في مكانٍ واحد لتفادي مشاكل التغييرات التي قد تحدث [cut] [scope: تجار باقة سبيشل] (SA-S-5010)

## M-006

Shopify: SH-C-013 Store details and general settings; Salla: SA-C-002 Store information and general settings (General / عام)

Basis: SH-C-013 platform_terms "General" | SA-C-002 platform_terms "General"; concern "General / عام"

### Where it lives

- **Shopify**
  - `general`: "title": "General" (SH-S-1486)
  - `Store properties`: "label": "Store properties" (SH-S-0789)
- **Salla**
  - `General`: {"position": 2, "kind": "link", "text": "General", "href": "/general"} (SA-S-1678)
  - `Store activity`: "general/store-information":"Store activity" (SA-S-1722)
  - `Maintenance mode`: "general/maintenance-mode":"Maintenance mode" (SA-S-1726)
  - `@salla.sa/ui-merchant-utils`: {"id": 1768207266275, "name": "@salla.sa/ui-merchant-utils", "Prod": {}, "env": "prod", "path": "/^(/settings)(/.*)?$/", "position": 57} (SA-S-3586)
  - `Settings`: "id": 1243992, "name": "Settings", "key": "apiDetailFolder.1243992", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingS [cut] (SA-S-1054)

### Who decides

- **Shopify**
  - `settings:general`: "eligibility":{"permissions":["PREFERENCES"]} (SH-S-5131)
- **Salla**
  - `تفعيل وضع صيانة المتجر`: "extra_icons": null}, {"parent_code": "adar-alhsab-oalmtgr", "title": "تفعيل وضع صيانة المتجر", "description": null, "icon": null, "icon_color": null, "icon_bac [cut] [scope: plan: سلة بلس] (SA-S-2084)
  - `ميزة البحث في إعدادات المتجر`: "extra_icons": null}, {"parent_code": "adar-alhsab-oalmtgr", "title": "ميزة البحث في إعدادات المتجر", "description": null, "icon": null, "icon_color": null, "ic [cut] [scope: plan: سلة بلس] (SA-S-2087)
  - `تفريغ الكاش`: "extra_icons": null}, {"parent_code": "almzaya-almtkdm", "title": "تفريغ الكاش", "description": null, "icon": null, "icon_color": null, "icon_background": null, [cut] [scope: plan: سلة بلس] (SA-S-2092)
  - `تخصيص خيارات المتجر`: "title": "تخصيص خيارات المتجر", "description": "تحكم أكبر بخيارات متجرك من خلال:\r\n\r\nتخصيص الطلبات (حد أدنى، أوقات استقبال، تفعيل الكوبونات، إعادة الطلب)\r\n [cut] [scope: plan: سلة بلس] (SA-S-2097)
  - `store_setting_browse`: "permissions": [{"id": 1309137353, "name": "store_setting_browse", "label": "store setting browse"}, {"id": 468515018, "name": "store_setting_edit_basic_info",  [cut] (SA-S-2384)
  - `store_setting_edit_basic_info`: "label": "store setting browse"}, {"id": 468515018, "name": "store_setting_edit_basic_info", "label": "store setting edit basic info"}, {"id": 1976109003, "name [cut] (SA-S-2385)
  - and 10 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `4. Your Responsibilities (summary)`: You acknowledge and agree to provide public-facing contact information, terms of service, a refund policy, and shipping policies (including order fulfilment tim [cut] (SH-S-0014)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `Store properties`: "label": "Store properties" (SH-S-0789)
  - `shop/update`: "value": "shop/update" (SH-S-1357)
- **Salla**
  - `Settings`: "id": 1243992, "name": "Settings", "key": "apiDetailFolder.1243992", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingS [cut] (SA-S-1054)
  - `settings`: {"id": 13, "slug": "settings", "icon": "sicon-settings", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_w [cut] (SA-S-1545)
  - `store-settings`: {"id": 22, "slug": "store-settings", "icon": "sicon-settings", "options": [{"item": "read", "name": "read", "disabled": true}, {"item": "read_write", "name": "r [cut] (SA-S-1565)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-007

Shopify: SH-C-015 Subscription plans; Salla: SA-C-004 Store plan subscription (Store plan / باقة المتجر: Basic, Plus, Pro, Special)

Basis: SH-C-015 platform_terms "Plan"; platform_terms "Basic" | SA-C-004 platform_terms "Store plan"; platform_terms "plans"; concern "باقة المتجر"

### Where it lives

- **Shopify**
  - `inactive-account:subscription:pick_period`: "path":"access_account/subscription/pick_period/:plan/:period" (SH-S-5086)
  - `subscription:pick_period`: "path":"subscription/pick_period/:plan/:period" (SH-S-5090)
  - `plus_inactive_account`: "path":"access_account/plus" (SH-S-5091)
  - `plus`: "path":"plus" (SH-S-5093)
  - `billing_plan`: "title": "Plan" (SH-S-1487)
  - `Plus`: "section":"Plus" (SH-S-1591)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Store plan`: {"position": 3, "kind": "link", "text": "Store plan", "href": "/plan"} (SA-S-1679)

### Who decides

- **Shopify**
  - `inactive-account:reactivate:pick-plan:pos`: "eligibility":{"permissions":["BILLING_SUBSCRIPTIONS","BILLING_PAYMENT_METHODS_VIEW"]} (SH-S-5071)
  - `plan`: "eligibility":{"oneOf":[{"organizationFeatures":["ORGANIZATION_BILLING"],"organizationPermissions":["VIEW_BILLING"],"excluded":{"organizationFlags":["1989d180"] [cut] (SH-S-5082)
  - `settings:plan:shop_plus_self_renewals`: "eligibility":{"organizationFlags":["7351e1b4"],"permissions":["BILLING_SUBSCRIPTIONS"]} (SH-S-5084)
  - `plus_inactive_account`: "eligibility":{"permissions":["MANAGE_PAYMENTS_SETTINGS"]} (SH-S-5092)
  - `plan.name basic`: "plan.name": "basic" [scope: store 2jiwxs-gr (trial), the admin's BillingPlan list] (SH-S-2076)
  - `merchant-checkout:subscribe:plans`: "eligibility":{"oneOf":[{"permissions":["BILLING_INVOICES_VIEW"]},{"permissions":["BILLING_CHARGES"]},{"permissions":["BILLING_PAYMENT_METHODS_VIEW"]}]} (SH-S-5070)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `إدارة الاشتراك في تطبيق سلة على iOS برصيد آيتونز`: "extra_icons": null}, {"parent_code": "adar-alhsab-oalmtgr", "title": "إدارة الاشتراك في تطبيق سلة على iOS برصيد آيتونز", "description": null, "icon": null, "ic [cut] [scope: plan: سلة بلس] (SA-S-2083)
  - `إمكانية تجميد الاشتراك السنوي حتى 30 يومًا`: "extra_icons": null}, {"parent_code": "adar-alhsab-oalmtgr", "title": "إمكانية تجميد الاشتراك السنوي حتى 30 يومًا", "description": null, "icon": null, "icon_col [cut] [scope: plan: سلة بلس] (SA-S-2085)
  - `بدون عمولة منصة على مبيعاتك`: بدون عمولة منصة على مبيعاتك [scope: plan: سلة سبيشل] (SA-S-2198)
  - `enable-special-plan-purchase`: {"position": 434, "name": "enable-special-plan-purchase", "value": {"enabled": true, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3395)
  - `renew-price-by-slug`: {"position": 477, "name": "renew-price-by-slug", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3438)
  - `plan-free-trial`: {"position": 491, "name": "plan-free-trial", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3452)
  - and 1 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `5. Payment of Fees and Taxes`: You will pay the Fees applicable to your subscription to Online Service and/or POS Services ("Subscription Fees") (SH-S-0234)
  - `13. Shopify Contracting Party and Forum`: Contracting Party. You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store. (SH-S-0001)
- **Salla**
  - `"سلة" (التعريفات)`: • "سلة": شركة منصة سلة للاتصالات وتقنية المعلومات (شخص واحد) ، المملكة العربية السعودية. [scope: الشروط والأحكام لحملة اليوم الوطني (95) – باقات/بكجات سلة] (SA-S-5001)

### How it meets the rest

- **Shopify**
  - `ShopPlan`: "name": "ShopPlan", "kind": "OBJECT", "description": "The shop's billing plan and subscription details. Indicates the plan tier (such as Basic, Advanced, or Plu [cut] [scope: GraphQL Admin API 2026-10] (SH-S-7453)
  - `Shop.plan`: {"name": "plan", "type": "ShopPlan!"} [scope: GraphQL Admin API 2026-10] (SH-S-7454)
- **Salla**
  - `💰 طريقة استرجاع المبلغ`: في حال استحقاق الاسترجاع، يتم إعادة المبلغ إلى رصيد المتجر (المحفظة) ليتمكن التاجر من استخدامه داخل المنصة (مثل تجديد الاشتراك أو شراء خدمات أخرى). (SA-S-5002)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `❓ لماذا لا يظهر خيار إلغاء الباقة؟`: يظهر خيار إلغاء الاشتراك فقط في حالات محددة تتيح لك استرداد كامل مبلغ الاشتراك. (SA-S-5003)

## M-008

Shopify: SH-C-016 Shopify bills (charges to the merchant, invoices, payment of bills); Salla: SA-C-005 Store balance and Salla billing (Balance & billing / الرصيد والفواتير; رصيد المتجر)

Basis: SH-C-016 platform_terms "Billing"; platform_terms "Billing history" | SA-C-005 platform_terms "Balance & billing"; platform_terms "إعدادات الفوترة"

### Where it lives

- **Shopify**
  - `billing:invoice-complete-auth:list`: "path":"invoices/:id/complete_payment_authentication" (SH-S-5062)
  - `billing:payment-auth-redirect:approval:list`: "path":"invoices/authenticate_payment" (SH-S-5064)
  - `settings/billing`: [**Billing**](https://admin.shopify.com/settings/billing) (SH-S-6312)
  - `organization_billing`: "title": "Billing" (SH-S-1485)
  - `Billing`: "section":"Billing" (SH-S-1549)
- **Salla**
  - `Balance & billing`: {"position": 6, "kind": "link", "text": "Balance & billing", "href": "/billing"} (SA-S-1682)
  - `Wallet`: {"position": 106, "kind": "link", "text": "Wallet", "href": "/payments/wallet", "parent": 0, "list": 9} (SA-S-1876)
  - `@salla.sa/ui-merchant-billing`: {"id": 1728393005946, "name": "@salla.sa/ui-merchant-billing", "Prod": {}, "env": "prod", "path": "/billing", "position": 9} (SA-S-3538)

### Who decides

- **Shopify**
  - `inactive-account-billing-invoice:list`: "eligibility":{"permissions":["BILLING_PAYMENT_METHODS_VIEW","BILLING_INVOICES_VIEW"]} (SH-S-5072)
  - `inactive-account-billing-invoice:export-credit-note`: "eligibility":{"oneOf":[{"organizationPermissions":["VIEW_BILLING"]},{"organizationPermissions":["MANAGE_BILLING"]}]} (SH-S-5073)
  - `inactive-account-billing-history:list`: "eligibility":{"permissions":["BILLING_INVOICES_VIEW"]} (SH-S-5074)
  - `inactive-account-pay-bills:list`: "eligibility":{"permissions":["BILLING_SUBSCRIPTIONS","BILLING_PAYMENT_METHODS_VIEW","BILLING_INVOICES_VIEW"]} (SH-S-5075)
  - `inactive-account:profile`: "eligibility":{"betas":["7aca6635"],"oneOf":[{"organizationPermissions":["VIEW_BILLING"]},{"organizationPermissions":["MANAGE_BILLING"]}]} (SH-S-5076)
  - `inactive-account:profile:billing:profile:delete-payment-method`: "eligibility":{"organizationPermissions":["MANAGE_BILLING"]} (SH-S-5077)
  - and 10 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `إضافة وسحب رصيد المتجر`: "sub_features": [{"parent_code": "mhfth-almtgr-oalfotr", "title": "إضافة وسحب رصيد المتجر", "description": null, "icon": null, "icon_color": null, "icon_backgro [cut] [scope: plan: سلة بلس] (SA-S-2062)
  - `إعدادات الفوترة`: "extra_icons": null}, {"parent_code": "mhfth-almtgr-oalfotr", "title": "إعدادات الفوترة", "description": null, "icon": null, "icon_color": null, "icon_backgroun [cut] [scope: plan: سلة بلس] (SA-S-2064)
  - `store_setting_purchase_from_salla_store`: "label": "restore data management"}, {"id": 1957673870, "name": "store_setting_purchase_from_salla_store", "label": "store setting purchase from salla store"},  [cut] (SA-S-2391)
  - `wallet_and_invoices_management`: "label": "shipping options management"}, {"id": 273807752, "name": "wallet_and_invoices_management", "label": "wallet and invoices management"}, {"id": 16482366 [cut] (SA-S-2393)
  - `store_setting_purchase_from_salla_store`: "en": "restore data management"}}, {"id": 1957673870, "key": "store_setting_purchase_from_salla_store", "name": {"ar": "الشراء من متجر سلة", "en": "store settin [cut] (SA-S-2608)
  - `wallet_and_invoices_management`: "en": "shipping options management"}}, {"id": 273807752, "key": "wallet_and_invoices_management", "name": {"ar": "المحفظة والفواتير", "en": "wallet and invoices [cut] (SA-S-2610)
  - and 6 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `13. Shopify Contracting Party and Forum`: Contracting Party. You are contracting with the Shopify Contracting Party or Parties below, based on the billing address of your Store. (SH-S-0001)
  - `13. Shopify Contracting Party and Forum, Billing and Collection`: Billing and Collection. Shopify Inc. may act as the billing agent for Shopify Technology (USA) Inc. and/or another Shopify Contracting Party, including to colle [cut] (SH-S-0008)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **Salla**
  - `أولاً: تعريف محفظة متجرك على سلة`: رصيد المتجر: يُستخدم لتجديد باقة المتجر تلقائياً، بالإضافة للشراء من متجر سلة وإصدار البوليصات وغير ذلك. (SA-S-0089)
  - `أولاً: تعريف محفظة متجرك على سلة`: 💡 تنبيه: رصيد المتجر ورصيد المدفوعات الإلكترونية مستقلان عن بعضهما، ولا يمكن تحويل الأموال من رصيد المدفوعات الإلكترونية إلى رصيد المتجر. (SA-S-0091)

### Stated reason

- **Shopify**
  - `help.shopify.com/en/manual/your-account/manage-billing/paying-your-bills/managin`: For accounting reasons, most Shopify bills are charged in US dollars, but merchants in some supported countries can be charged in their local currency. (SH-S-0266)
- **Salla**: gap (searched, not found)

## M-009

Shopify: SH-C-017 Taxes on Shopify's own charges; WooCommerce: WC-C-057 Taxes on Woo's own fees

Basis: SH-C-017 platform_terms "Taxes"; statement SH-S-0036 "To the extent that Shopify charges these Taxes" | WC-C-057 platform_terms "Taxes"; platform_terms "VAT/GST/CT on fees"; statement WC-S-0548 "we will be adding VAT/GST/CT on all fees we charge for WooPayments services"

### Where it lives

- **Shopify**
  - `settings/billing`: [**Billing**](https://admin.shopify.com/settings/billing) (SH-S-6313)
  - `Tax registration`: In the **Tax registration** section, click **Enter Tax ID number**. [scope: Saudi Arabia and the United Arab Emirates (the page's subject)] (SH-S-0279)
- **WooCommerce**
  - `Payments > Documents`: For EU and UKmerchants who may require VAT invoices for WooPayments fees, those are provided under the Payments > Documents menu in your dashboard. [scope: EU and UK merchants] (WC-S-5309)

### Who decides

- **Shopify**
  - `5. Payment of Fees and Taxes`: To the extent that Shopify charges these Taxes, they are calculated using the tax rates that apply based on the billing address you provide to us. (SH-S-0036)
  - `help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-`: This page provides a detailed guide on how Value-Added Tax (VAT) charges are applied at 15% in Saudi Arabia and 5% in the United Arab Emirates (UAE). [scope: Saudi Arabia (15%), United Arab Emirates (5%)] (SH-S-0277)
  - `Understanding VAT obligations for Shopify stores in Saudi Arabia`: If you have a VAT number, then your Shopify bill might be exempt from VAT charges. [scope: Saudi Arabia] (SH-S-0278)
- **WooCommerce**
  - `WooPayments: Taxes`: NOTE: After September 2, 2025 we will be adding VAT/GST/CT on all fees we charge for WooPayments services. [scope: WooPayments] (WC-S-0548)

### Who is legally responsible

- **Shopify**
  - `5. Payment of Fees and Taxes`: You are responsible for all applicable Taxes that arise from or as a result of your subscription to or purchase of Shopify's products and services. (SH-S-0235)
  - `13. Shopify Contracting Party and Forum, Billing and Collection`: Billing and Collection. Shopify Inc. may act as the billing agent for Shopify Technology (USA) Inc. and/or another Shopify Contracting Party, including to colle [cut] (SH-S-0008)
- **WooCommerce**
  - `5. Fees, Payment, and Renewal: a. Automattic Fees (Taxes)`: You’re responsible for paying all applicable Taxes relating to your use of our Services, your payments, or your purchases. (WC-S-0462)
  - `VAT invoices for EU and UK merchants`: You are responsible for self-accounting for any applicable VAT in your country under the reverse charge mechanism. [scope: VAT-registered businesses whose invoice shows VAT reverse charged] (WC-S-5316)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `WooPayments: Tax Documents for VAT/GST/CT`: If your business is based in a country where you may need tax invoices, you can receive a monthly invoice showing our fees and the relevant tax (VAT/GST/CT) on  [cut] (WC-S-0549)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-010

Shopify: SH-C-019 App charges billed through Shopify, SH-C-169 Partner payouts; Salla: SA-C-195 App billing and partner payouts (Billing System Salla partners; Payouts)

Basis: SH-C-019 platform_terms "app_subscriptions/update"; platform_terms "Manage app billing" | SH-C-169 platform_terms "Payouts" | SA-C-195 platform_terms "App Subscriptions"; platform_terms "Billing System Salla partners"; platform_terms "Payouts"

### Where it lives

- **Shopify**
  - `settings/billing`: [**Billing**](https://admin.shopify.com/settings/billing) (SH-S-6315)
  - `settings/apps`: [**Apps**](https://admin.shopify.com/settings/apps) (SH-S-6316)
  - `billing:app-selector:list`: "path":"charges/:appId/pricing_plans" (SH-S-5061)
  - `billing:ot-complete-auth:list`: "path":"charges/:appId/:chargeId/:chargeType/complete_payment_authentication" (SH-S-5063)
  - `billing:charge:approval:list`: "path":"charges/:appId/:chargeId/:chargeType/:chargeTypeUrl" (SH-S-5065)
  - `billing:managed-pricing:charge-approval`: "path":"charges/:appId/plans/:planHandle" (SH-S-5078)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Billing System Salla partners`: "id": "01KFDMDX1KTKJJP5AEX2H8JDZK", "title": "Billing System Salla partners", "target": "blank", "to": "https://salla.dev/tutorial/salla-partners-billing-system [cut] (SA-S-1174)
  - `App Subscriptions`: {"position": 24, "kind": "link", "text": "App Subscriptions", "href": "/subscriptions/apps", "parent": 23, "list": 8} (SA-S-1927)
  - `Payouts`: {"position": 33, "kind": "link", "text": "Payouts", "href": "/payouts", "parent": 32, "list": 10} (SA-S-1936)
  - `Billings`: {"position": 34, "kind": "link", "text": "Billings", "href": "/billing", "parent": 32, "list": 10} (SA-S-1937)
  - `Operation records`: {"position": 35, "kind": "link", "text": "Operation records", "href": "/billing/operations", "parent": 32, "list": 10} (SA-S-1938)
  - `نظام الفوترة الخاص بشركاء سلة`: تم إطلاق نظام فوترة جديد يعمل بشكل آلي على منصة شركاء سلة، حيث يتم إنشاء الفواتير الشهرية للتطبيقات دون الحاجة إلى حسابات يدوية أو تنسيق مباشر مع فرق سلة. (SA-S-0046)

### Who decides

- **Shopify**
  - `Which billing method should you use?`: you configure subscription plans, usage-based pricing, and free trials in the Partner Dashboard instead of writing billing code. (SH-S-0285)
  - `Identify your app charge status`: **Paid charge**: The charge is displayed on a past bill and payment has been collected. To request a refund, [contact the app developer](#request-app-refund). (SH-S-0271)
  - `Part C, App Plan (C.2.2.1)`: An App Developer that has met certain registration requirements, pays 0% of the total revenues on the first USD $1 million for their App Revenues and pays 15% o [cut] (SH-S-0287)
  - `Shopify App Pricing, Important note`: All apps published on the Shopify App Store are required to use a Shopify provided billing solution and adhere to the terms and conditions of the [Shopify Partn [cut] (SH-S-0284)
  - `billing:charge:approval:list`: "eligibility":{"permissions":["BILLING_APPLICATION_CHARGES"]} (SH-S-5066)
  - `billing:charge:approval:add-payment-method`: "eligibility":{"clients":["web"]} (SH-S-5067)
  - and 6 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `المادة (5) – العمولات والدفع`: تحتفظ منصة سلة بحقها في اقتطاع نسبة من قيمة الاشتراك مقابل خدمات الاستضافة والتكامل. (SA-S-0026)
  - `المادة (5) – العمولات والدفع`: تُصرف مستحقات المطورين بعد مرور فترة ضمان الجودة والاسترداد (عادة 15 يومًا). (SA-S-0027)
  - `المادة الخامسة-طبيعة التزام منصة سلة`: تقوم سلة بإعداد تقارير دورية للشريك توضح العمولات أو الأرباح أو المبالغ المستحقة، وتقوم بتحويلها في المواعيد المحددة حسب السياسات المالية إذا لم يوجد ما يمنع ذل [cut] (SA-S-0034)

### Who is legally responsible

- **Shopify**
  - `Part C, 4. Use of the Shopify Billing Resource`: It is the Developer’s responsibility to: (i) obtain Merchant consent to create and issue such charges and (ii) bill the Merchant in compliance with the Merchant [cut] (SH-S-0286)
  - `How Shopify App Pricing helps`: **Revenue sharing**: Shopify collects the charge and automatically pays out your share (SH-S-0282)
  - `How Shopify App Pricing helps`: **Chargeback handling**: Shopify handles all chargeback-related processes. (SH-S-0283)
  - `How Shopify App Pricing helps`: **Revenue sharing**: Shopify collects the charge and automatically pays out your share (SH-S-0282)
- **Salla**
  - `سياسة الشروط والاستخدام – متجر تطبيقات سلة > المقدّمة`: ترحب منصة "سلّة" المملوكة لشركة تطبيق سلة لتقنية المعلومات (س.ت: 4031200589) (SA-S-0015)
  - `المادة (5) – العمولات والدفع`: في حال كان التطبيق مدفوعًا، فإن عملية الدفع تتم عبر منصة سلة وتخضع للعمولات والنسب المعتمدة. (SA-S-0025)

### How it meets the rest

- **Shopify**
  - `How Shopify App Pricing helps`: **Simplified payment process**: Charges are directly added to the merchant's Shopify invoice. (SH-S-0281)
  - `help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-`: These charges are for the recurring use of an app, such as a monthly subscription payment. This cost is included in your regular Shopify subscription bill. (SH-S-0269)
  - `Billing`: "label": "Billing" (SH-S-0769)
  - `app_subscriptions/update`: "value": "app_subscriptions/update" (SH-S-1156)
  - `Transaction`: "name": "Transaction", "kind": "INTERFACE", "description": "A Shopify Partner transaction." [scope: Partner API 2025-10] (SH-S-7464)
- **Salla**
  - `Subscriptions`: "id": 843603, "name": "Subscriptions", "key": "apiDetailFolder.843603", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplaying [cut] (SA-S-1077)
  - `المادة (5) – العمولات والدفع`: في حال كان التطبيق مدفوعًا، فإن عملية الدفع تتم عبر منصة سلة وتخضع للعمولات والنسب المعتمدة. (SA-S-0025)
  - `نظام الفوترة الخاص بشركاء سلة`: يمكنك فتح أي فاتورة للاطلاع على تفاصيلها، البحث عن فاتورة محددة، ودفع الفواتير مباشرة مع إرفاق إثبات التحويل البنكي. (SA-S-0045)

### Stated reason

- **Shopify**
  - `About billing for your app`: Shopify App Pricing creates a predictable, trustworthy, and standardized experience for app users and makes pricing easier to set up and maintain. (SH-S-0280)
- **Salla**
  - `المادة (5) – العمولات والدفع`: تحتفظ منصة سلة بحقها في اقتطاع نسبة من قيمة الاشتراك مقابل خدمات الاستضافة والتكامل. (SA-S-0026)

## M-011

Shopify: SH-C-020 Products and variants; Salla: SA-C-020 Products (Products / المنتجات), SA-C-021 Product options, option values, variants and option templates, SA-C-022 Categories (Categories / الأقسام), SA-C-023 Brands (Brands / الماركات التجارية); WooCommerce: WC-C-064 Products and catalogue structure (types, variations, attributes, categories, tags, brands)

Basis: SH-C-020 platform_terms "Products"; platform_terms "products/create"; inventory SH-I-2502 "Product variants" | SA-C-020 platform_terms "Products"; platform_terms "product.created"; concern "Products / المنتجات" | SA-C-021 platform_terms "Product Variants" | SA-C-022 platform_terms "Categories"; concern "Categories / الأقسام" | SA-C-023 platform_terms "Brands"; concern "Brands / الماركات التجارية" | WC-C-064 platform_terms "Products"; platform_terms "Categories"; platform_terms "Brands"; inventory WC-I-0265 "product.created"

### Where it lives

- **Shopify**
  - `admin-scan:product:open`: "path":"product-scan/:productId" (SH-S-5006)
  - `admin-scan:generate`: "path":"admin-scan" (SH-S-5008)
  - `product:bulk-edit`: "path":"bulk/product" (SH-S-5009)
  - `product:bulk-import`: "path":"bulk/import" (SH-S-5011)
  - `products`: "path":"products" (SH-S-5015)
  - `product:try-media-gen`: "path":"try-media-gen" (SH-S-5025)
  - and 3 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `ProductsNew`: {"position": 14, "kind": "link", "text": "ProductsNew", "href": "/products"} (SA-S-1690)
  - `Show “You may also like” section on product page`: "products/products.recommendations":"Show “You may also like” section on product page" (SA-S-1749)
  - `Automatic pricing`: "products/products.auto_pricing":"Automatic pricing" (SA-S-1751)
  - `Show number of purchases`: "products/products.purchase_count":"Show number of purchases" (SA-S-1753)
  - `Product filter settings`: "products/filters":"Product filter settings" (SA-S-1756)
  - `Product sorting options`: "products/products.product_sorting":"Product sorting options" (SA-S-1759)
  - and 13 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Products`: $this->label = __( 'Products', 'woocommerce' ); (WC-S-0002)
  - `Products > General`: '' => __( 'General', 'woocommerce' ), (WC-S-0012)
  - `Products`: 'menu_name' => _x( 'Products', 'Admin menu name', 'woocommerce' ), (WC-S-0049)
  - `Products > All Products`: 'all_items' => __( 'All Products', 'woocommerce' ), (WC-S-0050)
  - `Products > Add New`: 'add_new' => __( 'Add New', 'woocommerce' ), (WC-S-0051)
  - `Products > Categories`: 'menu_name' => _x( 'Categories', 'Admin menu name', 'woocommerce' ), (WC-S-0052)
  - and 5 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `admin-scan:product:open`: "eligibility":{"betas":["0770b054"]} (SH-S-5007)
  - `product:bulk-edit`: "eligibility":{"clients":["web"],"entitlements":["products"]} (SH-S-5010)
  - `product:bulk-import`: "eligibility":{"clients":["web"],"entitlements":["products"],"betas":["78e33675"]} (SH-S-5012)
  - `products`: "eligibility":{"permissions":["PRODUCTS"],"entitlements":["products"]} (SH-S-5016)
  - `products:imports`: "eligibility":{"permissions":["MANAGE_PRODUCTS"],"betas":["78e33675"]} (SH-S-5017)
  - `products:create`: "eligibility":{"permissions":["MANAGE_PRODUCTS"]} (SH-S-5018)
  - and 5 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `عدد لا محدود من المنتجات`: "sub_features": [{"parent_code": "mzaya-asasy", "title": "عدد لا محدود من المنتجات", "description": null, "icon": null, "icon_color": null, "icon_background": n [cut] [scope: plan: سلة بلس] (SA-S-1949)
  - `إضافة كل أنواع المنتجات`: "extra_icons": null}, {"parent_code": "mzaya-asasy", "title": "إضافة كل أنواع المنتجات", "description": null, "icon": null, "icon_color": null, "icon_background [cut] [scope: plan: سلة بلس] (SA-S-1952)
  - `عرض مرات الشراء`: "extra_icons": null}, {"parent_code": "adar-almntgat", "title": "عرض مرات الشراء", "description": null, "icon": null, "icon_color": null, "icon_background": nul [cut] [scope: plan: سلة بلس] (SA-S-1977)
  - `عرض المنتجات التي نفدت في نهاية الصفحة`: "extra_icons": null}, {"parent_code": "adar-almntgat", "title": "عرض المنتجات التي نفدت في نهاية الصفحة", "description": null, "icon": null, "icon_color": null, [cut] [scope: plan: سلة بلس] (SA-S-1978)
  - `عرض منتجات قد تعجبك في صفحة المنتج`: "extra_icons": null}, {"parent_code": "adar-almntgat", "title": "عرض منتجات قد تعجبك في صفحة المنتج", "description": null, "icon": null, "icon_color": null, "ic [cut] [scope: plan: سلة بلس] (SA-S-1979)
  - `إضافة كل أنواع المنتجات`: "extra_icons": null}, {"parent_code": "adar-almntgat", "title": "إضافة كل أنواع المنتجات", "description": null, "icon": null, "icon_color": null, "icon_backgrou [cut] [scope: plan: سلة بلس] (SA-S-1981)
  - and 61 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `product (post type)`: 'capability_type' => 'product', 'map_meta_cap' => true, (WC-S-5387)

### Who is legally responsible

- **Shopify**
  - `4. Your Responsibilities`: You are responsible for the creation and operation of your Shopify Store, your Materials, the goods and services that you may sell through the Services, and all [cut] (SH-S-0236)
  - `8.1 Your Materials`: We do not take ownership of the Materials that you provide to Shopify; however, we do require a license to your Materials. (SH-S-0042)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_products`: The webhook topic for `products/create` events. Occurs whenever a product is created. Requires the `read_products` scope. (SH-S-6098)
  - `read_products`: The webhook topic for `products/delete` events. Occurs whenever a product is deleted. Requires the `read_products` scope. (SH-S-6099)
  - `unauthenticated_read_product_listings`: Requires `unauthenticated_read_product_listings` access scope. (SH-S-6155)
  - `unauthenticated_read_product_listings`: * To read disclosures from a custom storefront, a Storefront API access token with the `unauthenticated_read_product_listings` and `unauthenticated_read_metaobj [cut] (SH-S-6154)
  - `unauthenticated_read_product_listings`: Make sure you have the correct [access scopes](https://shopify.dev/docs/api/usage/access-scopes#unauthenticated-access-scopes). The Storefront API requires the  [cut] (SH-S-6156)
  - `unauthenticated_read_product_listings`: * Your Headless channel or custom app has the `unauthenticated_read_product_listings`, `unauthenticated_read_customers` and `unauthenticated_write_checkouts` [a [cut] (SH-S-6152)
  - and 7 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Products`: "id": 841792, "name": "Products", "key": "apiDetailFolder.841792", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSet [cut] (SA-S-1022)
  - `Product Tags`: "id": 841793, "name": "Product Tags", "key": "apiDetailFolder.841793", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayin [cut] (SA-S-1024)
  - `Product Images`: "id": 841795, "name": "Product Images", "key": "apiDetailFolder.841795", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1026)
  - `products`: {"id": 7, "slug": "products", "icon": "sicon-t-shirt", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_wri [cut] (SA-S-1552)
  - `product.created`: {"id": 439420598, "slug": "product.created", "url": "https://docs.salla.dev/doc-433805#product-webhook-events-model", "order": 0, "is_enabled": true, "name": {" [cut] (SA-S-1591)
  - `product.updated`: {"id": 1225523539, "slug": "product.updated", "url": "https://docs.salla.dev/doc-433805#product-webhook-events-model", "order": 0, "is_enabled": true, "name": { [cut] (SA-S-1592)
  - and 22 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `wc/v3 > product-attribute-terms`: 'product-attribute-terms' => 'WC_REST_Product_Attribute_Terms_Controller', (WC-S-0093)
  - `wc/v3 > product-attributes`: 'product-attributes' => 'WC_REST_Product_Attributes_Controller', (WC-S-0094)
  - `wc/v3 > product-categories`: 'product-categories' => 'WC_REST_Product_Categories_Controller', (WC-S-0095)
  - `wc/v3 > product-custom-fields`: 'product-custom-fields' => 'WC_REST_Product_Custom_Fields_Controller', (WC-S-0096)
  - `wc/v3 > product-tags`: 'product-tags' => 'WC_REST_Product_Tags_Controller', (WC-S-0099)
  - `wc/v3 > products`: 'products' => 'WC_REST_Products_Controller', (WC-S-0100)
  - and 33 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-012

Shopify: SH-C-022 Inventory; Salla: SA-C-025 Inventory quantities, audit and stock logs (Product Quantity; Inventory management); WooCommerce: WC-C-068 Inventory and stock levels

Basis: SH-C-022 platform_terms "Inventory"; platform_terms "Inventory management" | SA-C-025 platform_terms "Inventory"; platform_terms "Inventory management"; inventory SA-I-0976 "إدارة المخزون" | WC-C-068 platform_terms "Inventory"; platform_terms "Stock"

### Where it lives

- **Shopify**
  - `product_variant:bulk-edit`: "path":"bulk/product_variant" (SH-S-5177)
  - `inventoryMovement`: "path":"inventory_movements" (SH-S-5178)
  - `products:inventory`: "path":"products/inventory" (SH-S-5192)
  - `Inventory`: "text": "Inventory" (SH-S-1511)
  - `Inventory`: "label": "Inventory" (SH-S-0777)
- **Salla**
  - `Inventory`: {"position": 12, "kind": "link", "text": "Inventory", "href": "/inventory"} (SA-S-1688)
  - `Auto restock based on order status`: "orders/auto-restock":"Auto restock based on order status" (SA-S-1742)
  - `Product display in store`: "products/products.product_quantity":"Product display in store" (SA-S-1750)
  - `Exclude products from inventory sync`: "products/sync_ignore_sku":"Exclude products from inventory sync" (SA-S-1758)
  - `Inventory management`: {"position": 27, "kind": "link", "text": "Inventory management", "href": "/products/quantities/bulk", "parent": 0, "list": 2} (SA-S-1797)
  - `Inventory audit`: {"position": 33, "kind": "link", "text": "Inventory audit", "href": "/products/quantities", "parent": 0, "list": 2} (SA-S-1803)
  - and 3 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Products > Inventory`: 'inventory' => __( 'Inventory', 'woocommerce' ), (WC-S-0013)
  - `Analytics > Stock`: 'title' => __( 'Stock', 'woocommerce' ), (WC-S-0074)

### Who decides

- **Shopify**
  - `product_variant:bulk-edit`: "eligibility":{"clients":["web"],"entitlements":["products"]} (SH-S-5010)
  - `inventoryMovement`: "eligibility":{"permissions":["PRODUCTS"],"entitlements":["products","inventory.enabled"]} (SH-S-5022)
  - `products:inventory:history`: "eligibility":{"betas":["10c5f657"]} (SH-S-5193)
  - `products:inventory:counts`: "eligibility":{"betas":["4d3efaac"],"permissions":["PRODUCTS"],"entitlements":["inventory.counts"]} (SH-S-5194)
  - `products:inventory:counts:list`: "eligibility":{"betas":["4d3efaac"],"entitlements":["inventory.counts"],"permissions":["PRODUCTS"]} (SH-S-5195)
  - `products:inventory:counts:create`: "eligibility":{"betas":["4d3efaac"],"permissions":["PRODUCTS","MANAGE_INVENTORY"],"entitlements":["inventory.counts"]} (SH-S-5196)
  - and 12 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `تعديل الكميات`: "extra_icons": null}, {"parent_code": "adar-almntgat", "title": "تعديل الكميات", "description": null, "icon": null, "icon_color": null, "icon_background": null, [cut] [scope: plan: سلة بلس] (SA-S-1975)
  - `إدارة المخزون`: "extra_icons": null}, {"parent_code": "adar-almntgat", "title": "إدارة المخزون", "description": null, "icon": null, "icon_color": null, "icon_background": null, [cut] [scope: plan: سلة بلس] (SA-S-1976)
  - `جرد المنتجات والمخزون`: "sub_features": []}, {"title": "جرد المنتجات والمخزون", "description": "تتبّع حالة المخزون وعدد المنتجات المباعة والمتبقية والتي قاربت على الانتهاء عبر واجهة سه [cut] [scope: plan: سلة بلس] (SA-S-2096)
  - `product_browse_quantity_logs`: "label": "product search"}, {"id": 1314842132, "name": "product_browse_quantity_logs", "label": "product browse quantity logs"}, {"id": 1641439138, "name": "pro [cut] (SA-S-2252)
  - `products_stock_management`: "label": "categories management"}, {"id": 1600568493, "name": "products_stock_management", "label": "products stock management"}, {"id": 692313006, "name": "imp [cut] (SA-S-2256)
  - `inventory_browse`: "label": "inventory transfer show"}, {"id": 1821209542, "name": "inventory_browse", "label": "inventory browse"}, {"id": 1047237319, "name": "inventory_manageme [cut] (SA-S-2307)
  - and 14 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `woocommerce_manage_stock`: 'id' => 'woocommerce_manage_stock', 'default' => 'yes', 'type' => 'checkbox', (WC-S-5400)
  - `woocommerce_hold_stock_minutes`: 'desc' => __( 'Hold stock (for unpaid orders) for x minutes. When this limit is reached, the pending order will be cancelled. Leave blank to disable.', 'woocomm [cut] (WC-S-5401)
  - `woocommerce_hold_stock_minutes`: 'default' => '60', (WC-S-5402)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_inventory`: The webhook topic for `inventory_levels/connect` events. Occurs whenever an inventory level is connected. Requires the `read_inventory` scope. (SH-S-6002)
  - `read_inventory`: The webhook topic for `inventory_levels/disconnect` events. Occurs whenever an inventory level is disconnected. Requires the `read_inventory` scope. (SH-S-6003)
  - `read_inventory`: The webhook topic for `inventory_levels/update` events. Occurs whenever an inventory level is updated. Requires the `read_inventory` scope. (SH-S-6004)
  - `read_inventory`: Requires `read_inventory` access scope or `read_products` access scope. (SH-S-6005)
  - `read_inventory`: Requires `read_inventory` access scope. (SH-S-6006)
  - `write_inventory`: "text": "write_inventory" (SH-S-0997)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Product Quantity`: "id": 841796, "name": "Product Quantity", "key": "apiDetailFolder.841796", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDispl [cut] (SA-S-1030)
  - `product.available`: {"id": 318898285, "slug": "product.available", "url": "https://docs.salla.dev/doc-433805#product-webhook-events-model", "order": 0, "is_enabled": true, "name":  [cut] (SA-S-1594)
  - `product.quantity.low`: {"id": 1176306442, "slug": "product.quantity.low", "url": "https://docs.salla.dev/doc-433805#product-webhook-events-model", "order": 0, "is_enabled": true, "nam [cut] (SA-S-1595)
- **WooCommerce**
  - `wc-analytics > ProductsLowInStock`: 'Automattic\WooCommerce\Admin\API\ProductsLowInStock', (WC-S-0219)
  - `wc-analytics > reports/stock (Reports/Stock/Controller)`: 'Automattic\WooCommerce\Admin\API\Reports\Stock\Controller', (WC-S-0240)
  - `wc-analytics > reports/stock/stats (Reports/Stock/Stats/Controller)`: 'Automattic\WooCommerce\Admin\API\Reports\Stock\Stats\Controller', (WC-S-0241)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `سبب الإنقاص`: 📌 ملاحظة: عند تقليل الكمية، يجب إدخال سبب الإنقاص بشكل إلزامي، لضمان تتبع دقيق لحركة المخزون. (SA-S-5011)
- **WooCommerce**: gap (searched, not found)

## M-013

Shopify: SH-C-025 Gift cards; Salla: SA-C-063 Customer wallet, cashback and gift cards (Customer wallet / محفظة العميل)

Basis: SH-C-025 platform_terms "Gift cards" | SA-C-063 platform_terms "Gift cards"; inventory SA-I-2497 "wallet-gift-card"

### Where it lives

- **Shopify**
  - `gift-card:root`: "path":"gift_cards" (SH-S-5170)
  - `Gift cards`: "text": "Gift cards" (SH-S-1514)
  - `giftcard:create`: "path":"gift_cards/products/new" (SH-S-5013)
- **Salla**
  - `Customer wallet`: {"position": 19, "kind": "link", "text": "Customer wallet", "href": "/wallet"} (SA-S-1695)
  - `Cashback eligibility`: "coupons/cashback-eligibility":"Cashback eligibility" (SA-S-1713)
  - `Maximum Credit Usage Limit`: "wallet/max-credit-usage":"Maximum Credit Usage Limit" (SA-S-1766)
  - `Gift cards`: "wallet/gift-card":"Gift cards" (SA-S-1767)
  - `Wallet & Cashback Notifications`: "wallet/notifications":"Wallet & Cashback Notifications" (SA-S-1768)
  - `Customer wallet`: {"position": 50, "kind": "link", "text": "Customer wallet", "href": "/marketing/customer_wallet", "parent": 0, "list": 3} (SA-S-1820)
  - and 4 more statements in `platforms/salla/statements.tsv`

### Who decides

- **Shopify**
  - `gift-card:root`: "eligibility":{"permissions":["GIFT_CARDS"],"entitlements":["products","giftCards.enabled"]} (SH-S-5171)
  - `gift-card:create`: "eligibility":{"permissions":["CREATE_AND_EDIT_GIFT_CARDS"]} (SH-S-5172)
  - `giftcard:create`: "eligibility":{"permissions":["MANAGE_PRODUCTS"],"entitlements":["products"]} (SH-S-5014)
  - `entitlements.giftCards.enabled`: {"set": 0, "section": "entitlements", "key": "giftCards", "value": {"enabled": true, "__typename": "GiftCardsType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5747)
  - `entitlements.products`: {"set": 0, "section": "entitlements", "key": "products", "value": true} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5349)
  - `Sell gift cards`: {"kind": "row", "section": 1, "position": 55, "cells": [{"tag": "th", "text": "Sell gift cards", "scope": "row"}, {"tag": "td", "text": "Included"}, {"tag": "td [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7043)
- **Salla**
  - `محفظة العميل  *برسوم إضافية`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "محفظة العميل *برسوم إضافية", "description": null, "icon": null, "icon_color": null, "icon_backg [cut] [scope: plan: سلة بلس] (SA-S-2006)
  - `عروض الكاش باك`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "عروض الكاش باك", "description": null, "icon": null, "icon_color": null, "icon_background": null [cut] [scope: plan: سلة بلس] (SA-S-2007)
  - `browse_cashback_offers`: "label": "sweply management"}, {"id": 837963260, "name": "browse_cashback_offers", "label": "browse cashback offers"}, {"id": 64974077, "name": "manage_cashback [cut] (SA-S-2365)
  - `manage_cashback_offers`: "label": "browse cashback offers"}, {"id": 64974077, "name": "manage_cashback_offers", "label": "manage cashback offers"}, {"id": 1571130366, "name": "delete_ca [cut] (SA-S-2366)
  - `delete_cashback_offers`: "label": "manage cashback offers"}, {"id": 1571130366, "name": "delete_cashback_offers", "label": "delete cashback offers"}, {"id": 326407111, "name": "coupon_d [cut] (SA-S-2367)
  - `browse_cashback_offers`: "en": "sweply management"}}, {"id": 837963260, "key": "browse_cashback_offers", "name": {"ar": "الاطلاع على عروض الكاش باك", "en": "browse cashback offers"}}, { [cut] (SA-S-2582)
  - and 8 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `www.shopify.com/legal/terms-gift-cards`: Please note that you are legally responsible for all gift card or store credit issuance and management; Shopify merely provides software to assist with such act [cut] (SH-S-0676)
  - `3. Compliance with Laws`: You are responsible for the handling of any amounts loaded on the Gift Card or offered as Store Credit in compliance with Applicable Laws, including, if require [cut] (SH-S-0677)
  - `4. Gift Card & Store Credit Terms and Issuance`: You will be responsible for supervising and managing all daily funds flow associated with Gift Cards and Store Credit (SH-S-0678)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `read_gift_card_transactions`: Requires `read_gift_card_transactions` access scope. (SH-S-5999)
  - `read_gift_cards`: Requires `read_gift_cards` access scope. (SH-S-6000)
  - `read_gift_cards`: You need to contact Shopify Support to request the `write_gift_cards` and `read_gift_cards` [access scopes](https://shopify.dev/docs/admin-api/access-scopes). (SH-S-6001)
  - `write_gift_card_transactions`: Requires `write_gift_card_transactions` access scope. (SH-S-6210)
  - `write_gift_cards`: Requires `write_gift_cards` access scope. (SH-S-6211)
  - `read_gift_cards`: "text": "read_gift_cards" (SH-S-0995)
- **Salla**
  - `Customer Wallet`: "id": 5737562, "name": "Customer Wallet", "key": "apiDetailFolder.5737562", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisp [cut] (SA-S-1034)
  - `customer-wallets`: {"id": 27, "slug": "customer-wallets", "icon": "sicon-wallet", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": " [cut] (SA-S-1568)
  - `wallet.action`: {"id": 398406680, "slug": "wallet.action", "url": "https://docs.salla.dev/2243750m0", "order": 0, "is_enabled": true, "name": {"ar": "عملية على محفظة العميل", " [cut] (SA-S-1647)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `استعادة قيمة الكاش باك`: عند إلغاء الطلب بعد منح العميل رصيد الكاش باك المستحق عليه، يقوم النظام تلقائياً باستعادة (سحب) قيمة الكاش باك المضافة إلى محفظة العميل والمرتبطة بهذا الطلب، وذ [cut] (SA-S-5019)

## M-014

Shopify: SH-C-029 Online Store themes; Salla: SA-C-090 Themes and store design (Store design; Theme Marketplace; Twilight Engine); WooCommerce: WC-C-111 Storefront design (themes and block patterns)

Basis: SH-C-029 platform_terms "Themes and templates"; platform_terms "read_themes" | SA-C-090 inventory SA-I-0829 "Theme Marketplace"; inventory SA-I-2379 "theme-customization"; inventory SA-I-1031 "اختيار ثيم المتجر" | WC-C-111 platform_terms "Themes"; platform_terms "Choose your theme"

### Where it lives

- **Shopify**
  - `Liquid`: "label": "Liquid" (SH-S-0826)
- **Salla**
  - `Twilight Engine`: {"position": 5, "pointer": "/firstLevelNavbarItems/1/children/0", "depth": 1, "parent": "01HNA8Q9YTZGTHZYF36EYDJEWD", "type": "folder", "id": "01HNFTD5Y5ESFQS3P [cut] (SA-S-1161)
  - `Store designMost Viewed`: {"position": 58, "kind": "link", "text": "Store designMost Viewed", "href": "/themes", "parent": 0, "list": 4} (SA-S-1828)
  - `Theme Marketplace`: {"position": 59, "kind": "link", "text": "Theme Marketplace", "href": "/themes/marketplace", "parent": 0, "list": 4} (SA-S-1829)
  - `@salla.sa/ui-merchant-themes`: {"id": 1729154468415, "name": "@salla.sa/ui-merchant-themes", "Prod": {}, "env": "prod", "path": "/^/(themes$\|themes/marketplace\|themes/landing-pages\|themes/ord [cut] (SA-S-3546)
  - `@salla.sa/themes-editor`: {"id": 1762349896196, "name": "@salla.sa/themes-editor", "Prod": {}, "env": "prod", "path": "/themes/editor", "position": 49} (SA-S-3578)
- **WooCommerce**
  - `Choose your theme`: return __( 'Choose your theme', 'woocommerce' ); (WC-S-0418)
  - `Customize your store`: return __( 'Customize your store', 'woocommerce' ); (WC-S-0419)
  - `Themes`: Themes (WC-S-0695)

### Who decides

- **Shopify**
  - `online-store:parent`: "eligibility":{"entitlements":["storefront.enabled"]} (SH-S-5031)
  - `editor`: "eligibility":{"betas":["4e79d5b1","2847a1c7"],"permissions":["THEMES"]} (SH-S-5211)
  - `write_themes`: Requires `write_files` access scope, `write_themes` access scope or `write_images` access scope. Also: Users must have create files permissions. (SH-S-6199)
  - `write_themes`: Requires `write_files` access scope or `write_themes` access scope. Also: Users must have edit files permissions. (SH-S-6201)
  - `entitlements.storefront.enabled`: {"set": 0, "section": "entitlements", "key": "storefront", "value": {"enabled": true, "__typename": "StorefrontType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5364)
  - `Themes and templates`: {"kind": "row", "section": 1, "position": 6, "cells": [{"tag": "th", "text": "Themes and templates", "scope": "row"}, {"tag": "td", "text": "Included"}, {"tag": [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7003)
- **Salla**
  - `اختيار ثيم المتجر`: "sub_features": [{"parent_code": "tsmym-almtgr", "title": "اختيار ثيم المتجر", "description": null, "icon": null, "icon_color": null, "icon_background": null, " [cut] [scope: plan: سلة بلس] (SA-S-2031)
  - `تخصيص ثيم المتجر`: "extra_icons": null}, {"parent_code": "tsmym-almtgr", "title": "تخصيص ثيم المتجر", "description": null, "icon": null, "icon_color": null, "icon_background": nul [cut] [scope: plan: سلة بلس] (SA-S-2032)
  - `إنشاء نسخ متعددة من الثيم`: "extra_icons": null}, {"parent_code": "tsmym-almtgr", "title": "إنشاء نسخ متعددة من الثيم", "description": null, "icon": null, "icon_color": null, "icon_backgro [cut] [scope: plan: سلة بلس] (SA-S-2033)
  - `جدولة نشر النسخ`: "extra_icons": null}, {"parent_code": "tsmym-almtgr", "title": "جدولة نشر النسخ", "description": null, "icon": null, "icon_color": null, "icon_background": null [cut] [scope: plan: سلة بلس] (SA-S-2034)
  - `حماية محتوى المتجر`: "extra_icons": null}, {"parent_code": "tsmym-almtgr", "title": "حماية محتوى المتجر", "description": null, "icon": null, "icon_color": null, "icon_background": n [cut] [scope: plan: سلة بلس] (SA-S-2035)
  - `تصميم واجهة المتجر`: "sub_features": []}, {"title": "تصميم واجهة المتجر", "description": "ميّز متجرك الإلكتروني عبر اختيار أحد قوالب التصميم المتنوعة التي تمنح جمالية ومرونة وسهولة  [cut] [scope: plan: سلة بلس] (SA-S-2101)
  - and 20 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**: gap (searched, not found)

### Who is legally responsible

- **Shopify**
  - `9.6 Theme Store`: The intellectual property rights of the Theme remain the property of the designer. (SH-S-0052)
  - `9.6 Theme Store`: Technical support for a Theme is the responsibility of the designer, and Shopify accepts no responsibility to provide such support. (SH-S-0053)
- **Salla**
  - `المادة (12): حدود مسؤولية منصة سلة`: تعمل منصة «سلة» كمنصة تقنية وسيطة لتوفير خدمات استضافة ونشر وإدارة الثيمات، ولا تُعد طرفًا مباشرًا في العلاقة التعاقدية أو التنفيذية بين التاجر والمطور (SA-S-0039)
  - `content`: تعمل منصة سلة كمنصة وسيطة لاستضافة ونشر الثيمات، ولا تتحمل مسؤولية مباشرة عن جودة أو أداء أو توافق الثيمات. (SA-S-0119)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_script_tags`: Requires `read_script_tags` access scope. Also: Requires access to script tags. (SH-S-6112)
  - `read_themes`: The webhook topic for `themes/create` events. Occurs whenever a theme is created. Does not occur when theme files are created. Requires the `read_themes` scope. (SH-S-6135)
  - `read_themes`: The webhook topic for `themes/delete` events. Occurs whenever a theme is deleted. Does not occur when theme files are deleted. Requires the `read_themes` scope. (SH-S-6136)
  - `read_themes`: The webhook topic for `themes/publish` events. Occurs whenever a theme with the main or mobile (deprecated) role is published. Requires the `read_themes` scope. (SH-S-6137)
  - `read_themes`: The webhook topic for `themes/update` events. Occurs whenever a theme is updated. Does not occur when theme files are updated. Requires the `read_themes` scope. (SH-S-6138)
  - `write_script_tags`: Requires `write_script_tags` access scope. Also: Requires access to script tags. (SH-S-6291)
  - and 5 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Layouts`: "id": 846214, "name": "Layouts", "key": "apiDetailFolder.846214", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingSettin [cut] (SA-S-1120)
  - `Hooks`: "id": 8372592, "name": "Hooks", "key": "apiDetailFolder.8372592", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSett [cut] (SA-S-1121)
  - `Pages`: "id": 849309, "name": "Pages", "key": "apiDetailFolder.849309", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingSettings [cut] (SA-S-1122)
  - `Product Pages`: "id": 849311, "name": "Product Pages", "key": "apiDetailFolder.849311", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayi [cut] (SA-S-1123)
  - `Customer Pages`: "id": 849314, "name": "Customer Pages", "key": "apiDetailFolder.849314", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1124)
  - `Blog Pages`: "id": 849315, "name": "Blog Pages", "key": "apiDetailFolder.849315", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingS [cut] (SA-S-1125)
  - and 6 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `wc/private`: $this->register_routes( 'private', 'wc/private' ); (WC-S-0082)
  - `wc/private > /patterns`: const IDENTIFIER = 'patterns'; (WC-S-0178)
  - `wc-admin > themes (Themes)`: 'Automattic\WooCommerce\Admin\API\Themes', (WC-S-0194)
  - `wc-admin > onboarding/themes (OnboardingThemes)`: 'Automattic\WooCommerce\Admin\API\OnboardingThemes', (WC-S-0200)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `متجر الثيمات`: وفرت سلة متجر للثيمات من خلاله تستطيع تثبيت الثيمات على متجرك، بإضافة لإمكانية معاينة كيف سيبدو متجرك بالثيم قبل شراؤه لضمان تجربة استخدام لا مثيل لها لعملائك. (SA-S-5031)
- **WooCommerce**: gap (searched, not found)

## M-015

Shopify: SH-C-030 Pages and blog posts, SH-C-031 Menus and URL redirects; Salla: SA-C-081 Store blog (Blog / المدونة), SA-C-093 Information pages, menus and custom URLs

Basis: SH-C-030 platform_terms "Blog posts"; platform_terms "Pages" | SH-C-031 platform_terms "Menus" | SA-C-081 platform_terms "Blog"; platform_terms "مدونة المتجر" | SA-C-093 platform_terms "pages_management"; platform_terms "store-menu"; platform_terms "Information pages"; platform_terms "الصفحات التعريفية"

### Where it lives

- **Shopify**
  - `content:parent`: "path":"content" (SH-S-5119)
  - `Blog posts`: "text": "Blog posts" (SH-S-1527)
  - `Blog`: "label": "Blog" (SH-S-0917)
  - `content:parent`: "path":"content" (SH-S-5119)
  - `Menus`: "text": "Menus" (SH-S-1526)
- **Salla**
  - `Blog`: {"position": 22, "kind": "link", "text": "Blog", "href": "/blog"} (SA-S-1698)
  - `Show blog in navigation`: "blog/blogs.show_in_menu":"Show blog in navigation" (SA-S-1703)
  - `Likes and comments`: "blog/blogs.allow_likes":"Likes and comments" (SA-S-1704)
  - `Blog homepage SEO`: "blog/blogs.homepage_title":"Blog homepage SEO" (SA-S-1705)
  - `@salla.sa/ui-merchant-blog`: {"id": 1733145423329, "name": "@salla.sa/ui-merchant-blog", "Prod": {}, "env": "prod", "path": "/marketing/blog", "position": 26} (SA-S-3555)
  - `Information pages`: {"position": 61, "kind": "link", "text": "Information pages", "href": "/channel/pages", "parent": 0, "list": 4} (SA-S-1831)
  - and 4 more statements in `platforms/salla/statements.tsv`

### Who decides

- **Shopify**
  - `content:parent`: "eligibility":{"entitlements":["metaobjects.enabled"]} (SH-S-5120)
  - `comments`: "eligibility":{"entitlements":["storefront.enabled"],"permissions":["PAGES"]} (SH-S-5124)
  - `entitlements.metaobjects.enabled`: {"set": 0, "section": "entitlements", "key": "metaobjects", "value": {"enabled": true, "__typename": "MetaobjectsType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5625)
  - `entitlements.storefront.enabled`: {"set": 0, "section": "entitlements", "key": "storefront", "value": {"enabled": true, "__typename": "StorefrontType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5364)
  - `content:parent`: "eligibility":{"entitlements":["metaobjects.enabled"]} (SH-S-5120)
  - `menus:list`: "eligibility":{"entitlements":["storefront.enabled"],"permissions":["LINKS"]} (SH-S-5123)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `مدونة المتجر`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "مدونة المتجر", "description": null, "icon": null, "icon_color": null, "icon_background": null,  [cut] [scope: plan: سلة بلس] (SA-S-2011)
  - `blog_browse`: {"id": 1830458757, "name": "المدونة", "label": "المدونة", "permissions": [{"id": 308885434, "name": "blog_browse", "label": "blog browse"}, {"id": 1815500475, " [cut] (SA-S-2345)
  - `blog_management`: {"id": 1830458757, "name": "المدونة", "label": "المدونة", "permissions": [{"id": 308885434, "name": "blog_browse", "label": "blog browse"}, {"id": 1815500475, " [cut] (SA-S-2346)
  - `blog_browse`: "permissions": [{"id": 308885434, "key": "blog_browse", "name": {"ar": "الاطلاع على المدونة", "en": "blog browse"}}, {"id": 1815500475, "key": "blog_management" [cut] (SA-S-2562)
  - `blog_management`: "en": "blog browse"}}, {"id": 1815500475, "key": "blog_management", "name": {"ar": "إدارة المدونة", "en": "blog management"}}], "position": 8} (SA-S-2563)
  - `store-blog`: {"position": 428, "name": "store-blog", "value": {"enabled": false, "released": false, "type": "app", "app_id": "870050397", "plans": ["special", "pro", "plus"] [cut] [scope: plans: special, pro, plus] (SA-S-3389)
  - and 13 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `read_content`: Requires `read_content` access scope or `read_online_store_pages` access scope. (SH-S-5955)
  - `read_content`: Requires `read_privacy_settings` access scope, `read_content` access scope or `read_online_store_pages` access scope. (SH-S-5956)
  - `read_online_store_pages`: **Requires one of the `read_content` or `read_online_store_pages` access scopes.:** (SH-S-6061)
  - `read_online_store_pages`: All triggers require one of the `read_content` or `read_online_store_pages` access scopes. Those triggers that require additional scopes are documented where re [cut] (SH-S-6062)
  - `unauthenticated_read_content`: Requires `unauthenticated_read_content` access scope. (SH-S-6148)
  - `write_content`: Requires Any of `write_content`, `write_online_store_pages` access scopes. (SH-S-6178)
  - and 9 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Custom URLs`: "id": 2108762, "name": "Custom URLs", "key": "apiDetailFolder.2108762", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayi [cut] (SA-S-1069)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `❓ ما الهدف من تحديد صفحة تعريفية كصفحة سياسة الاستبدال والاسترجاع؟`: حتى يظهر رمز الباركود في الفاتورة، ويتمكن العميل من استعراض صفحة سياسة الاستبدال والاسترجاع بمجرد مسحه للباركود، وكل ذلك حتى يستوفي متجرك واحد من أهم شروط الفات [cut] (SA-S-5034)

## M-016

Shopify: SH-C-032 Languages and translations; Salla: SA-C-008 Store languages and translation (Languages / اللغات)

Basis: SH-C-032 platform_terms "Languages"; platform_terms "read_translations" | SA-C-008 platform_terms "Languages"; concern "Languages / اللغات"; platform_terms "Translation log"

### Where it lives

- **Shopify**
  - `languages`: "title": "Languages" (SH-S-1501)
  - `Localizations`: "label": "Localizations" (SH-S-0778)
- **Salla**
  - `Languages`: "general/languages":"Languages" (SA-S-1723)
  - `Translation log`: {"position": 126, "kind": "link", "text": "Translation log", "href": "/manage/languages/logs", "parent": 0, "list": 11} (SA-S-1896)
  - `@salla.sa/ui-merchant-languages`: {"id": 1733319174887, "name": "@salla.sa/ui-merchant-languages", "Prod": {}, "env": "prod", "path": "/^/manage/languages/", "position": 27} (SA-S-3556)
  - `@salla.sa/ui-merchant-localization`: {"id": 1742300460615, "name": "@salla.sa/ui-merchant-localization", "Prod": {}, "env": "prod", "path": "/localization", "position": 38} (SA-S-3567)
  - `Languages`: "id": 841811, "name": "Languages", "key": "apiDetailFolder.841811", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1065)

### Who decides

- **Shopify**
  - `languages`: "eligibility":{"permissions":["PREFERENCES"],"entitlements":["accountManagement.manageStoreLanguage"]} (SH-S-5268)
  - `entitlements.accountManagement.manageStoreLanguage`: {"set": 0, "section": "entitlements", "key": "accountManagement", "value": {"manageStoreLanguage": true, "__typename": "AccountManagementType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5857)
  - `Translate your storefront`: {"kind": "row", "section": 1, "position": 74, "cells": [{"tag": "th", "text": "Translate your storefront", "scope": "row"}, {"tag": "td", "text": "Included"}, { [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7057)
- **Salla**
  - `إتاحة 40 لغة في المتجر`: "extra_icons": null}, {"parent_code": "adar-tgrb-alaamyl", "title": "إتاحة 40 لغة في المتجر", "description": null, "icon": null, "icon_color": null, "icon_backg [cut] [scope: plan: سلة بلس] (SA-S-2074)
  - `الترجمة الفورية *برسوم إضافية`: "extra_icons": null}, {"parent_code": "adar-tgrb-alaamyl", "title": "الترجمة الفورية *برسوم إضافية", "description": null, "icon": null, "icon_color": null, "ico [cut] [scope: plan: سلة بلس] (SA-S-2075)
  - `ميزة ترجمة الرسائل`: "extra_icons": null}, {"parent_code": "almzaya-almtkdm", "title": "ميزة ترجمة الرسائل", "description": null, "icon": null, "icon_color": null, "icon_background" [cut] [scope: plan: سلة بلس] (SA-S-2093)
  - `languages_management`: "label": "size guides management"}, {"id": 165693067, "name": "languages_management", "label": "languages management"}, {"id": 1540187540, "name": "landing_page [cut] (SA-S-2396)
  - `languages_management`: "en": "size guides management"}}, {"id": 165693067, "key": "languages_management", "name": {"ar": "إعدادات اللغات", "en": "languages management"}}, {"id": 15401 [cut] (SA-S-2613)
  - `languages`: {"position": 12, "name": "languages", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature", "de [cut] [scope: plans: plus, pro, special] (SA-S-2973)
  - and 1 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `read_locales`: The webhook topic for `locales/create` events. Occurs whenever a shop locale is created Requires the `read_locales` scope. (SH-S-6020)
  - `read_locales`: The webhook topic for `locales/destroy` events. Occurs whenever a shop locale is destroyed Requires the `read_locales` scope. (SH-S-6021)
  - `read_locales`: The webhook topic for `locales/update` events. Occurs whenever a shop locale is updated, such as published or unpublished Requires the `read_locales` scope. (SH-S-6022)
  - `read_locales`: Requires `read_locales` access scope or `read_markets_home` access scope. (SH-S-6023)
  - `read_translations`: Requires `read_translations` access scope. (SH-S-6140)
  - `read_translations`: * Your app has the `read_translations` [access scope](https://shopify.dev/docs/api/usage/access-scopes#read_translations), and the read scope for each resource  [cut] (SH-S-6141)
  - and 6 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Multi-Language Support`: {"position": 9, "pointer": "/9", "depth": 0, "parent": null, "type": "doc", "id": 421122, "name": "Multi-Language Support", "key": "doc.421122", "parentId": 841 [cut] (SA-S-1010)
  - `Languages`: "id": 841811, "name": "Languages", "key": "apiDetailFolder.841811", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1065)
  - `metadata`: {"id": 14, "slug": "metadata", "icon": "sicon-badge", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_writ [cut] (SA-S-1562)

### Stated reason

- **Shopify**
  - `languages`: You can add languages to your online store so that international customers can read your product details, policies, and checkout in their own language. (SH-S-7493)
- **Salla**
  - `❓ عند إضافة لغة إلى متجري لماذا تظهر معطلة؟`: حتى يتسنى للتاجر اختيار نوع الترجمة (فورية، يدوية) وتحضير متجره باللغة المضافة قبل إتاحتها وإظهارها للعملاء. (SA-S-5009)

## M-017

Shopify: SH-C-033 Domains; Salla: SA-C-007 Store domain and DNS records (Domain / نطاق المتجر; DNS Records), SA-C-301 Domains in the Partners portal (Domains Management, Transfer Domain, Domain Assignment)

Basis: SH-C-033 platform_terms "Domains"; inventory SH-I-1002 "Transfer domain to another Shopify store" | SA-C-007 platform_terms "Domain"; platform_terms "حجز دومين خاص" | SA-C-301 platform_terms "Domains"; platform_terms "Transfer Domain"

### Where it lives

- **Shopify**
  - `domains:inactive`: "path":"access_account/domains" (SH-S-5152)
  - `domains`: "title": "Domains" (SH-S-1497)
- **Salla**
  - `Domain`: {"position": 8, "kind": "link", "text": "Domain", "href": "/domains"} (SA-S-1684)
  - `Domain`: {"position": 60, "kind": "link", "text": "Domain", "href": "/manage/domain", "parent": 0, "list": 4} (SA-S-1830)
  - `@salla.sa/ui-merchant-domain`: {"id": 1728414981405, "name": "@salla.sa/ui-merchant-domain", "Prod": {}, "env": "prod", "path": "/manage/domain", "position": 14} (SA-S-3543)
  - `DNS Records`: "id": 841810, "name": "DNS Records", "key": "apiDetailFolder.841810", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplaying [cut] (SA-S-1064)
  - `Domains Management`: "title":"Domains Management","route":"domains" (SA-S-5116)

### Who decides

- **Shopify**
  - `domains:inactive`: "eligibility":{"permissions":["DOMAINS"]} (SH-S-5153)
  - `domains:inactive:transfer:prepare_for_transfer`: "eligibility":{"entitlements":["sellsOnShopifyPlatforms"]} (SH-S-5154)
  - `domains:root`: "eligibility":{"permissions":["DOMAINS"],"oneOf":[{"entitlements":["sellsOnShopifyPlatforms"]},{"excluded":{"entitlements":["sellsOnShopifyPlatforms"]}}]} (SH-S-5155)
  - `domains:buy`: "eligibility":{"entitlements":["sellsOnShopifyPlatforms","customDomains"]} (SH-S-5156)
  - `2.9 Domain Names`: Upon purchasing a domain name through Shopify, domain registration will be preset to automatically renew each year so long as your Shopify Account remains activ [cut] (SH-S-0029)
  - `entitlements.customDomains`: {"set": 0, "section": "entitlements", "key": "customDomains", "value": true} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5700)
  - and 3 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `دومين سلة الافتراضي`: "sub_features": [{"parent_code": "domyn-almtgr", "title": "دومين سلة الافتراضي", "description": null, "icon": null, "icon_color": null, "icon_background": null, [cut] [scope: plan: سلة بلس] (SA-S-2037)
  - `شهادة SSL مجانية`: "extra_icons": null}, {"parent_code": "domyn-almtgr", "title": "شهادة SSL مجانية", "description": null, "icon": null, "icon_color": null, "icon_background": nul [cut] [scope: plan: سلة بلس] (SA-S-2038)
  - `حجز دومين خاص`: "extra_icons": null}, {"parent_code": "domyn-almtgr", "title": "حجز دومين خاص", "description": null, "icon": null, "icon_color": null, "icon_background": null,  [cut] [scope: plan: سلة بلس] (SA-S-2039)
  - `نقل أو ربط دومين من طرف ثالث`: "extra_icons": null}, {"parent_code": "domyn-almtgr", "title": "نقل أو ربط دومين من طرف ثالث", "description": null, "icon": null, "icon_color": null, "icon_back [cut] [scope: plan: سلة بلس] (SA-S-2040)
  - `إدارة إعدادات DNS`: "extra_icons": null}, {"parent_code": "domyn-almtgr", "title": "إدارة إعدادات DNS", "description": null, "icon": null, "icon_color": null, "icon_background": nu [cut] [scope: plan: سلة بلس] (SA-S-2041)
  - `حجز اسم دومين (رابط) مُخصص لموقع متجرك`: "sub_features": []}, {"title": "حجز اسم دومين (رابط) مُخصص لموقع متجرك", "description": "سهّل على عملائك الوصول لمتجرك عبر حجز نطاق (دومين) خاص بك مثل:\r\nwww.m [cut] [scope: plan: سلة بلس] (SA-S-2104)
  - and 4 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `2.9 Domain Names`: You acknowledge that it is your sole responsibility to deactivate the auto-renewal function should you choose to do so. (SH-S-7271)
  - `14 Term and Termination`: Following termination, it will be your sole responsibility to handle all matters related to your domain with the domain provider. (SH-S-7272)
- **Salla**
  - `move_domain.accept_responsibility`: أقر أن طلب نقل الدومين بناءً على رغبتي وتحت مسؤوليتي الكاملة، وتنحصر مسؤولية منصة سلة في إتمام عملية النقل فقط. (SA-S-5004)

### How it meets the rest

- **Shopify**
  - `domains/create`: "value": "domains/create" (SH-S-1216)
- **Salla**
  - `DNS Records`: "id": 841810, "name": "DNS Records", "key": "apiDetailFolder.841810", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplaying [cut] (SA-S-1064)
  - `dns-records`: {"id": 17, "slug": "dns-records", "icon": "sicon-world", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_w [cut] (SA-S-1556)
  - `/partner-reports/v1/domains/stats`: "method":"GET","host":"api.salla.dev","path":"/partner-reports/v1/domains/stats" (SA-S-5118)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-018

Shopify: SH-C-039 Customers, SH-C-041 Customer accounts; Salla: SA-C-060 Customers (Customers / العملاء); WooCommerce: WC-C-073 Customer accounts

Basis: SH-C-039 platform_terms "Customers"; platform_terms "customers/create" | SH-C-041 platform_terms "Customer accounts" | SA-C-060 platform_terms "Customers"; platform_terms "customer.created"; concern "Customers / العملاء" | WC-C-073 platform_terms "Customers"; platform_terms "Accounts & Privacy"; inventory WC-I-0258 "customer.created"

### Where it lives

- **Shopify**
  - `customer:bulk-edit`: "path":"bulk/customer" (SH-S-5139)
  - `customer`: "path":"customers" (SH-S-5140)
  - `Customers`: "text": "Customers" (SH-S-1515)
  - `Customers`: "label": "Customers" (SH-S-0775)
  - `customer_accounts`: "title": "Customer accounts" (SH-S-1490)
  - `Customer Account API`: "label": "Customer Account API" (SH-S-0836)
- **Salla**
  - `Customers`: {"position": 17, "kind": "link", "text": "Customers", "href": "/customers"} (SA-S-1693)
  - `All customers`: {"position": 72, "kind": "link", "text": "All customers", "href": "/customers", "parent": 0, "list": 5} (SA-S-1842)
  - `Customer settings`: {"position": 74, "kind": "link", "text": "Customer settings", "href": "/customers/settings", "parent": 0, "list": 5} (SA-S-1844)
  - `@salla.sa/ui-merchant-customers`: {"id": 1728830696176, "name": "@salla.sa/ui-merchant-customers", "Prod": {}, "env": "prod", "path": "/customers", "position": 16} (SA-S-3545)
  - `Customers`: "id": 841780, "name": "Customers", "key": "apiDetailFolder.841780", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1032)
- **WooCommerce**
  - `Accounts & Privacy`: $this->label = __( 'Accounts &amp; Privacy', 'woocommerce' ); (WC-S-0006)
  - `WooCommerce > Customers`: 'title' => __( 'Customers', 'woocommerce' ), (WC-S-0042)
  - `Reset password (WC_Email_Customer_Reset_Password)`: $this->title = __( 'Reset password', 'woocommerce' ); (WC-S-0305)
  - `New account (WC_Email_Customer_New_Account)`: $this->title = __( 'New account', 'woocommerce' ); (WC-S-0306)
  - `WooCommerce user roles`: WooCommerce adds two user roles—Customer and Shop Manager—and extends the existing Administrator role with store management capabilities. (WC-S-0883)

### Who decides

- **Shopify**
  - `customer:bulk-edit`: "eligibility":{"clients":["web"]} (SH-S-5067)
  - `customer`: "eligibility":{"permissions":["CUSTOMERS"]} (SH-S-5141)
  - `customer:create`: "eligibility":{"permissions":["CREATE_AND_EDIT_CUSTOMERS"]} (SH-S-5142)
  - `customer-payment-methods:show`: "eligibility":{"clients":["native"]} (SH-S-5145)
  - `customer:merge`: "eligibility":{"permissions":["MERGE_CUSTOMERS"]} (SH-S-5146)
  - `read_customer_merge`: Requires The user must have `read_customer_merge` permissions. (SH-S-5962)
  - and 7 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `فرز العملاء`: "sub_features": [{"parent_code": "alaamlaaa", "title": "فرز العملاء", "description": null, "icon": null, "icon_color": null, "icon_background": null, "extra_ico [cut] [scope: plan: سلة بلس] (SA-S-2055)
  - `حظر العميل`: "extra_icons": null}, {"parent_code": "alaamlaaa", "title": "حظر العميل", "description": null, "icon": null, "icon_color": null, "icon_background": null, "extra [cut] [scope: plan: سلة بلس] (SA-S-2056)
  - `إضافة عميل جديد`: "extra_icons": null}, {"parent_code": "alaamlaaa", "title": "إضافة عميل جديد", "description": null, "icon": null, "icon_color": null, "icon_background": null, " [cut] [scope: plan: سلة بلس] (SA-S-2057)
  - `تعديل معلومات العميل`: "extra_icons": null}, {"parent_code": "alaamlaaa", "title": "تعديل معلومات العميل", "description": null, "icon": null, "icon_color": null, "icon_background": nu [cut] [scope: plan: سلة بلس] (SA-S-2058)
  - `كشف العملاء غير الجادين`: "extra_icons": null}, {"parent_code": "alaamlaaa", "title": "كشف العملاء غير الجادين", "description": null, "icon": null, "icon_color": null, "icon_background": [cut] [scope: plan: سلة بلس] (SA-S-2060)
  - `إدارة مجموعة عملاء كدفعة واحدة`: "extra_icons": null}, {"parent_code": "alaamlaaa", "title": "إدارة مجموعة عملاء كدفعة واحدة", "description": null, "icon": null, "icon_color": null, "icon_backg [cut] [scope: plan: سلة برو] (SA-S-2118)
  - and 20 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Accounts and Privacy Settings`: Use these settings to enable or disable guest checkout, control customer account creation, decide how your store retains or removes personal data, and set your  [cut] (WC-S-0881)
  - `woocommerce_enable_guest_checkout`: 'desc' => __( 'Enable guest checkout (recommended)', 'woocommerce' ), (WC-S-0928)
  - `customer (role)`: // Customer role. add_role( 'customer', 'Customer', array( 'read' => true, (WC-S-5419)

### Who is legally responsible

- **Shopify**
  - `I. PURPOSE`: You shall act as a Data Controller and Shopify shall act as a Data Processor with respect to the processing of Your Customer Personal Data, in connection with Y [cut] (SH-S-0186)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `customer_read_customers`: Requires `customer_read_customers` access scope. (SH-S-5914)
  - `customer_read_customers`: Requires `customer_read_customers` access scope or `customer_read_companies` access scope. (SH-S-5913)
  - `customer_read_customers`: To read or write metafield data on the `CUSTOMER` resource using the Customer Account API, you'll need to include the `customer_read_customers` and `customer_wr [cut] (SH-S-5915)
  - `customer_read_customers`: Metafield writes require `customer_read_customers` and `customer_write_customers` [access scopes](https://shopify.dev/docs/apps/build/cli-for-apps/app-configura [cut] (SH-S-5916)
  - `customer_write_customers`: Requires `customer_write_customers` access scope or `customer_write_companies` access scope. (SH-S-5926)
  - `customer_write_customers`: Requires `customer_write_customers` access scope. (SH-S-5927)
  - and 37 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Customers`: "id": 841780, "name": "Customers", "key": "apiDetailFolder.841780", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1032)
  - `customers`: {"id": 1, "slug": "customers", "icon": "sicon-users", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_writ [cut] (SA-S-1546)
  - `customer.created`: {"id": 1964508071, "slug": "customer.created", "url": "https://docs.salla.dev/doc-433808#customer-webhook-events-model", "order": 0, "is_enabled": true, "name": [cut] (SA-S-1607)
  - `customer.updated`: {"id": 672334404, "slug": "customer.updated", "url": "https://docs.salla.dev/doc-433808#customer-webhook-events-model", "order": 0, "is_enabled": true, "name":  [cut] (SA-S-1608)
- **WooCommerce**
  - `wc/v3 > customers`: 'customers' => 'WC_REST_Customers_Controller', (WC-S-0088)
  - `wc/v4 > customers`: 'customers' => CustomersController::class, (WC-S-0133)
  - `wc/v4 > settings-account`: 'settings-account' => AccountSettingsController::class, (WC-S-0146)
  - `wc/store/v1 > /cart/update-customer`: const IDENTIFIER = 'cart-update-customer'; (WC-S-0161)
  - `wc-analytics > customers (Customers)`: 'Automattic\WooCommerce\Admin\API\Customers', (WC-S-0223)
  - `wc-analytics > reports/customers (Reports/Customers/Controller)`: 'Automattic\WooCommerce\Admin\API\Reports\Customers\Controller', (WC-S-0244)
  - and 5 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-019

Shopify: SH-C-040 Customer segments; Salla: SA-C-061 Customer groups

Basis: SH-C-040 inventory SH-I-0426 "customer_groups/create" | SA-C-061 platform_terms "Customer Groups"; platform_terms "تصنيف العملاء إلى مجموعات"

### Where it lives

- **Shopify**
  - `Segments`: "text": "Segments" (SH-S-1516)
  - `customer_segment_template`: "identifier": "customer_segment_template" (SH-S-2203)
  - `customer-segments`: "section":"Customers","path":"segments" (SH-S-7090)
- **Salla**
  - `Customer groups`: {"position": 75, "kind": "link", "text": "Customer groups", "href": "/customers/groups", "parent": 0, "list": 5} (SA-S-1845)
  - `Customer Groups`: "id": 841781, "name": "Customer Groups", "key": "apiDetailFolder.841781", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDispla [cut] (SA-S-1033)

### Who decides

- **Shopify**
  - `customer-segments`: "eligibility":{"entitlements":["customerSegmentation"]} (SH-S-5143)
  - `entitlements.customerSegmentation`: {"set": 0, "section": "entitlements", "key": "customerSegmentation", "value": true} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5670)
  - `Create customer segments`: {"kind": "row", "section": 1, "position": 47, "cells": [{"tag": "th", "text": "Create customer segments", "scope": "row"}, {"tag": "td", "text": "Included"}, {" [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7036)
- **Salla**
  - `تصنيف العملاء إلى مجموعات`: "sub_features": [{"parent_code": "alaamlaaa", "title": "تصنيف العملاء إلى مجموعات", "description": null, "icon": null, "icon_color": null, "icon_background": nu [cut] [scope: plan: سلة برو] (SA-S-2117)
  - `تصنيف تلقائي لمجموعات العملاء`: "sub_features": []}, {"title": "تصنيف تلقائي لمجموعات العملاء", "description": "صنّف عملائك بناءً على خصائص معينة كعدد الطلبات أو تقييمهم لمتجرك لإعادة استهدافه [cut] [scope: plan: سلة برو] (SA-S-2150)
  - `customer-group`: {"position": 200, "name": "customer-group", "value": {"enabled": false, "released": true, "plans": ["pro", "special"], "countries": [], "type": "feature"}} [scope: plans: pro, special] (SA-S-3161)
  - `customer-groups-draft-status`: {"position": 215, "name": "customer-groups-draft-status", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3176)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `customer.joined_segment`: "value": "customer.joined_segment" (SH-S-1185)
  - `customer_segment_template`: "identifier": "customer_segment_template" (SH-S-2203)
  - `write_customers`: Requires `write_customers` access scope. Also: The user must not have restricted access. (SH-S-6184)
- **Salla**
  - `Customer Groups`: "id": 841781, "name": "Customer Groups", "key": "apiDetailFolder.841781", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDispla [cut] (SA-S-1033)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-020

Shopify: SH-C-044 B2B companies, locations and contacts; WooCommerce: WC-C-103 B2B selling (wholesale, quotes, B2B payments)

Basis: SH-C-044 platform_terms "B2B"; platform_terms "Companies" | WC-C-103 platform_terms "B2B"; platform_terms "B2B payments"

### Where it lives

- **Shopify**
  - `companies:root`: "path":"companies" (SH-S-5113)
  - `Companies`: "text": "Companies" (SH-S-1517)
  - `B2B`: "label": "B2B" (SH-S-0768)
- **WooCommerce**
  - `Extensions > Merchandising > B2B`: B2B (WC-S-0730)

### Who decides

- **Shopify**
  - `companies:root`: "eligibility":{"features":["b2bEnabled"],"permissions":["VIEW_COMPANIES"],"entitlements":["b2b.enabled"]} (SH-S-5114)
  - `company:create`: "eligibility":{"permissions":["CREATE_AND_EDIT_COMPANIES"]} (SH-S-5115)
  - `companyLocation:details`: "eligibility":{"oneOf":[{"entitlements":["markets.b2b.enabled"]},{"features":["b2bEnabled"]}]} (SH-S-5116)
  - `companyLocation:create`: "eligibility":{"oneOf":[{"entitlements":["markets.b2b.enabled"],"permissions":["CREATE_AND_EDIT_COMPANIES"]},{"features":["b2bEnabled"],"permissions":["CREATE_A [cut] (SH-S-5117)
  - `companyLocation:storeCreditTransactionHistory`: "eligibility":{"permissions":["VIEW_COMPANY_STORE_CREDIT_ACCOUNT_TRANSACTIONS"]} (SH-S-5118)
  - `help.shopify.com/en/manual/b2b/getting-started.md`: Before you start using Shopify B2B, you need to decide whether to create a blended store for both B2B and D2C customers and orders, or a dedicated B2B-only stor [cut] (SH-S-0740)
  - and 11 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `Remove the gateway entirely`: If you only need to stop accepting purchase orders, disable the gateway in its settings instead. [scope: WooCommerce Purchase Order Gateway] (WC-S-5471 WC-S-5472)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `customer_read_companies`: Requires `customer_read_customers` access scope or `customer_read_companies` access scope. (SH-S-5913)
  - `customer_write_companies`: Requires `customer_write_customers` access scope or `customer_write_companies` access scope. (SH-S-5926)
  - `read_companies`: Requires `read_customers` access scope or `read_companies` access scope. (SH-S-5948)
  - `read_companies`: Requires `read_customers` access scope or `read_companies` access scope. Also: The shop must have access to B2B. Some operations may require additional plan cap [cut] (SH-S-5949)
  - `read_companies`: **Requires `read_companies` access scope.:** (SH-S-5950)
  - `read_companies`: All triggers require the `read_companies` access scope. Those triggers that require additional scopes are documented where relevant. Deprecated triggers are lis [cut] (SH-S-5951)
  - and 4 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `_po_number`: The purchase order number is stored on the order in the _po_number meta key. [scope: WooCommerce Purchase Order Gateway (version 1.5.12)] (WC-S-5473 WC-S-5472)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-021

Shopify: SH-C-046 Cart, SH-C-047 Shopify Checkout; Salla: SA-C-100 Checkout page and cart (Checkout; Guest checkout; Checkout APIs); WooCommerce: WC-C-072 Cart and checkout

Basis: SH-C-046 platform_terms "Cart"; platform_terms "carts/create" | SH-C-047 platform_terms "Checkout"; platform_terms "checkouts/create" | SA-C-100 platform_terms "Cart"; platform_terms "Checkout"; platform_terms "Guest checkout" | WC-C-072 platform_terms "Cart"; platform_terms "Checkout"

### Where it lives

- **Shopify**
  - `Cart`: "label": "Cart" (SH-S-0771)
  - `checkout`: "title": "Checkout" (SH-S-1489)
- **Salla**
  - `Checkout APIs`: {"position": 10, "pointer": "/firstLevelNavbarItems/1/children/5", "depth": 1, "parent": "01HNA8Q9YTZGTHZYF36EYDJEWD", "type": "folder", "id": "01KR60QF1KY60TRC [cut] (SA-S-1166)
  - `Checkout`: {"position": 9, "kind": "link", "text": "Checkout", "href": "/checkout"} (SA-S-1685)
  - `Guest checkout`: "checkout/guest-checkout":"Guest checkout" (SA-S-1706)
  - `@salla.sa/ui-merchant-payments`: {"id": 1729596362158, "name": "@salla.sa/ui-merchant-payments", "Prod": {}, "env": "prod", "path": "/^(/payments(?!/taxes)\|/entity/verifications\|/checkout)(/.*\| [cut] (SA-S-3549)
- **WooCommerce**
  - `Advanced > Page setup`: '' => __( 'Page setup', 'woocommerce' ), (WC-S-0022)

### Who decides

- **Shopify**
  - `Add-to-cart limit`: A recommended limit for your store displays in the Add-to-cart limit setting with a suggested maximum quantity limit based on your sales history: (SH-S-7483)
  - `Add-to-cart limit`: If you've made less than 250 sales, then the default recommended limit for your store is set to 50. [scope: stores with fewer than 250 sales] (SH-S-7484)
  - `checkout-settings`: "eligibility":{"permissions":["MANAGE_CHECKOUT_SETTINGS"],"entitlements":["webCheckout"]} (SH-S-5106)
  - `4. Your Responsibilities`: You agree to use Shopify Checkout for any sales associated with your online store. (SH-S-0015)
  - `1. Account Terms`: You agree not to work around, bypass, or circumvent any of the technical limitations of the Services, including to process orders outside Shopify's Checkout (SH-S-0016)
  - `2. Using the Shopify API`: not, except with Shopify’s express written authorization, (i) use an alternative to Shopify Checkout for checkout or payment processing for Shopify Merchants (SH-S-0216)
  - and 4 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `store-checkout`: {"position": 151, "name": "store-checkout", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3112)
  - `guest-checkout`: {"position": 152, "name": "guest-checkout", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3113)
  - `embedded-login-checkout`: {"position": 153, "name": "embedded-login-checkout", "value": {"enabled": true, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3114)
  - `ucp-embedded-checkout`: {"position": 163, "name": "ucp-embedded-checkout", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3124)
- **WooCommerce**
  - `woocommerce_enable_guest_checkout`: 'desc' => __( 'Enable guest checkout (recommended)', 'woocommerce' ), (WC-S-0928)

### Who is legally responsible

- **Shopify**
  - `4. Your Responsibilities`: You acknowledge and agree that the Services are not a marketplace, and any contract of sale made through the Services is directly and only between you and the c [cut] (SH-S-0011)
  - `4. Your Responsibilities`: For the avoidance of doubt, Shopify is not the seller or merchant of record and has no responsibility for your Store, your Materials, the goods or services you  [cut] (SH-S-0013)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `unauthenticated_write_checkouts`: * Your Headless channel or custom app has the `unauthenticated_read_product_listings`, `unauthenticated_read_customers` and `unauthenticated_write_checkouts` [a [cut] (SH-S-6152)
  - `dev.ucp.shopping.cart`: "dev.ucp.shopping.cart" [scope: store capture-plus (its UCP profile)] (SH-S-2533)
  - `unauthenticated_write_checkouts`: "text": "unauthenticated_write_checkouts" (SH-S-1101)
  - `carts/update`: "value": "carts/update" (SH-S-1160)
  - `read_orders`: The webhook topic for `carts/create` events. Occurs when a cart is created in the online store. Other types of carts aren't supported. For example, the webhook  [cut] (SH-S-6066)
  - `read_orders`: The webhook topic for `carts/update` events. Occurs when a cart is updated in the online store. Other types of carts aren't supported. For example, the webhook  [cut] (SH-S-6067)
  - and 5 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Cart`: "id": 8189800, "name": "Cart", "key": "apiDetailFolder.8189800", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingSetting [cut] (SA-S-1080)
  - `Cart Items`: "id": 8189801, "name": "Cart Items", "key": "apiDetailFolder.8189801", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingS [cut] (SA-S-1081)
  - `carts`: {"id": 3, "slug": "carts", "icon": "sicon-shopping", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_write [cut] (SA-S-1548)
- **WooCommerce**
  - `wc/store/v1 > /cart`: const IDENTIFIER = 'cart'; (WC-S-0149)
  - `wc/store/v1 > /cart/add-item`: const IDENTIFIER = 'cart-add-item'; (WC-S-0150)
  - `wc/store/v1 > /cart/items`: const IDENTIFIER = 'cart-items'; (WC-S-0155)
  - `wc/store/v1 > /cart/items/(?P<key>[\w-]{32})`: const IDENTIFIER = 'cart-items-by-key'; (WC-S-0156)
  - `wc/store/v1 > /cart/remove-item`: const IDENTIFIER = 'cart-remove-item'; (WC-S-0158)
  - `wc/store/v1 > /cart/update-item`: const IDENTIFIER = 'cart-update-item'; (WC-S-0160)
  - and 2 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**
  - `add-to-cart limit`: To protect your inventory information, you can set a limit on how many of each product a customer can add to their cart in one order. (SH-S-7489)
- **Salla**
  - `Checkout APIs`: This API collection is designed for developers building integrations that need to control cart and checkout-entry flows outside of the standard storefront (SA-S-5139)
- **WooCommerce**: gap (searched, not found)

## M-022

Shopify: SH-C-049 Checkout UI extensions; WooCommerce: WC-C-087 Block extensibility (cart, checkout and product blocks) and Store API extensions

Basis: SH-C-049 inventory SH-I-2421 "Shopify Checkout Extensibility"; platform_terms "Checkout UI" | WC-C-087 platform_terms "Cart and Checkout extensibility"; platform_terms "Additional checkout fields"

### Where it lives

- **Shopify**
  - `Apps in checkout, introduction`: To augment Shopify checkout with new functionality, build an app with extensions. (SH-S-0679)
  - `checkout_ui`: "identifier": "checkout_ui" (SH-S-2181)
  - `Checkout`: "label": "Checkout" (SH-S-0821)
- **WooCommerce**
  - `Front-end extensibility`: To extend the front-end of the blocks, extensions must use JavaScript. (WC-S-5466)

### Who decides

- **Shopify**
  - `9.13 Shopify Checkout Extensibility`: Shopify allows you to use extensions to customize your checkout ("Shopify Checkout Extensibility"). (SH-S-0069)
  - `9.13 Shopify Checkout Extensibility (summary)`: If you use Checkout Extensions, you're responsible for your own compliance, which could include getting all necessary consents from your customers and website v [cut] (SH-S-0070)
- **WooCommerce**
  - `cart_checkout_blocks`: 'description' => __( 'Optimize for faster checkout', 'woocommerce' ), 'is_experimental' => false, 'disable_ui' => true, (WC-S-5431)

### Who is legally responsible

- **Shopify**
  - `9.13 Shopify Checkout Extensibility (summary)`: If you use Checkout Extensions, you're responsible for your own compliance, which could include getting all necessary consents from your customers and website v [cut] (SH-S-0070)
  - `6. Merchant Agreement, Privacy and Data Security, Merchant Agreement and Privacy`: Developer must inform Merchants in the Merchant Agreement that: (i) Developer is solely responsible for the Application; (ii) Shopify is not liable for any faul [cut] (SH-S-0217)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `purchase.checkout.block.render`: "interface": "RenderExtensionTargets", "target": "purchase.checkout.block.render" [scope: checkout UI extensions 2026.7.1] (SH-S-7228)
  - `purchase.thank-you.block.render`: "interface": "RenderExtensionTargets", "target": "purchase.thank-you.block.render" [scope: checkout UI extensions 2026.7.1] (SH-S-7229)
- **WooCommerce**
  - `wc/store/v1 > /cart/extensions`: const IDENTIFIER = 'cart-extensions'; (WC-S-0154)
  - `IntegrationInterface`: interface IntegrationInterface { (WC-S-0451)
  - `AbstractPaymentMethodType`: abstract class AbstractPaymentMethodType implements PaymentMethodTypeInterface { (WC-S-0452)
  - `ExtendSchema`: final class ExtendSchema { (WC-S-0453)
  - `woocommerce_register_additional_checkout_field`: function woocommerce_register_additional_checkout_field( $options ) { // phpcs:ignore WordPress.NamingConventions.ValidFunctionName.FunctionDoubleUnderscore,PHP [cut] (WC-S-0454)
  - `Extending the Store API`: [Extending the Store API](https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/apis/store-api/extending-store-api/README.md) (WC-S-0773)
  - and 27 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**
  - `Customization options`: All customization options are easy to install and upgrade-safe (SH-S-0680)
- **WooCommerce**: gap (searched, not found)

## M-023

Shopify: SH-C-054 Orders, SH-C-056 Order editing and edit requests; Salla: SA-C-040 Orders (Orders / الطلبات), SA-C-041 Order statuses (Order Status; custom statuses), SA-C-046 Order cancellation; WooCommerce: WC-C-070 Orders and order statuses

Basis: SH-C-054 platform_terms "Orders"; platform_terms "orders/create"; inventory SH-I-0646 "Order cancellation" | SH-C-056 platform_terms "Edit orders"; platform_terms "orders/edited" | SA-C-040 platform_terms "Orders"; platform_terms "order.created"; concern "Orders / الطلبات"; inventory SA-I-0747 "Order editing" | SA-C-041 platform_terms "Order statuses"; platform_terms "تخصيص حالات الطلب" | SA-C-046 platform_terms "Order cancellation"; platform_terms "order.cancelled" | WC-C-070 platform_terms "Orders"; platform_terms "Order statuses"; inventory WC-I-0261 "order.created"

### Where it lives

- **Shopify**
  - `product-network-orders`: "path":"product-network-orders" (SH-S-5215)
  - `order:pay_by_creditcard_on_mobile`: "path":"orders/pay_by_creditcard_on_mobile/:id" (SH-S-5216)
  - `orders`: "path":"orders" (SH-S-5218)
  - `Orders`: "text": "Orders" (SH-S-1507)
  - `Order`: "label": "Order" (SH-S-0929)
  - `order:edit`: "section":"Orders","path":":orderId/edit","title":{"value":"Edit order"} (SH-S-7095)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Orders`: {"position": 15, "kind": "link", "text": "Orders", "href": "/orders"} (SA-S-1691)
  - `Customer notes`: "orders/customer-notes":"Customer notes" (SA-S-1744)
  - `Reorder`: "orders/reorder":"Reorder" (SA-S-1746)
  - `Order editing`: "orders/edit-policy":"Order editing" (SA-S-1747)
  - `All orders`: {"position": 2, "kind": "link", "text": "All orders", "href": "/orders", "parent": 0, "list": 1} (SA-S-1772)
  - `Order settings`: {"position": 4, "kind": "link", "text": "Order settings", "href": "/?settings=%2Forders", "parent": 0, "list": 1} (SA-S-1774)
  - and 9 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `WooCommerce > Orders`: 'menu_name' => _x( 'Orders', 'Admin menu name', 'woocommerce' ), (WC-S-0041)

### Who decides

- **Shopify**
  - `product-network-orders`: "eligibility":{"permissions":["ORDERS"]} (SH-S-5209)
  - `order:write-off:create`: "eligibility":{"betas":["bfbcab91"]} (SH-S-5220)
  - `order:edit:shipping-address`: "eligibility":{"oneOf":[{"permissions":["MANAGE_ORDERS_INFORMATION"]},{"permissions":["FULFILL_AND_SHIP_ORDERS"]}]} (SH-S-5221)
  - `write_marketplace_orders`: Requires `write_orders` access scope or `write_marketplace_orders` access scope. Also: The user must have capture\_payments\_for\_orders permission. (SH-S-6228)
  - `write_order_edits`: Requires `write_order_edits` access scope. Also: The user must have apply\_discounts\_to\_orders permission. (SH-S-6247)
  - `order:requested-edit:decline`: "eligibility":{"permissions":["EDIT_ORDERS"]} (SH-S-5219)
- **Salla**
  - `عدد لا محدود من الطلبات`: "extra_icons": null}, {"parent_code": "mzaya-asasy", "title": "عدد لا محدود من الطلبات", "description": null, "icon": null, "icon_color": null, "icon_background [cut] [scope: plan: سلة بلس] (SA-S-1950)
  - `طباعة ملخص الطلب`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "طباعة ملخص الطلب", "description": null, "icon": null, "icon_color": null, "icon_background": nul [cut] [scope: plan: سلة بلس] (SA-S-1988)
  - `إنشاء طلب يدوي`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "إنشاء طلب يدوي", "description": null, "icon": null, "icon_color": null, "icon_background": null, [cut] [scope: plan: سلة بلس] (SA-S-1989)
  - `تعديل الطلب`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "تعديل الطلب", "description": null, "icon": null, "icon_color": null, "icon_background": null, "e [cut] [scope: plan: سلة بلس] (SA-S-1990)
  - `تتبع الطلب عبر محفظة أبل (Apple Wallet)`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "تتبع الطلب عبر محفظة أبل (Apple Wallet)", "description": null, "icon": null, "icon_color": null, [cut] [scope: plan: سلة بلس] (SA-S-1995)
  - `إدارة مجموعة طلبات كدفعة واحدة`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "إدارة مجموعة طلبات كدفعة واحدة", "description": null, "icon": null, "icon_color": null, "icon_ba [cut] [scope: plan: سلة بلس] (SA-S-1996)
  - and 72 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `shop_order (post type)`: 'capability_type' => 'shop_order', 'map_meta_cap' => true, (WC-S-5406)
  - `woocommerce (admin menu)`: add_menu_page( __( 'WooCommerce', 'woocommerce' ), __( 'WooCommerce', 'woocommerce' ), 'edit_others_shop_orders', 'woocommerce', null, $woocommerce_icon, '55.5' [cut] (WC-S-0039)

### Who is legally responsible

- **Shopify**
  - `4. Your Responsibilities`: You acknowledge and agree that the Services are not a marketplace, and any contract of sale made through the Services is directly and only between you and the c [cut] (SH-S-0011)
  - `4. Your Responsibilities`: This includes, but is not limited to, authorizing the charge to the customer in respect of the customer's purchase, determining and collecting taxes, refunds, r [cut] (SH-S-0012)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `customer_read_orders`: Requires `customer_read_orders` access scope or `customer_read_draft_orders` access scope. (SH-S-5917)
  - `customer_read_orders`: Requires `customer_read_orders` access scope. (SH-S-5921)
  - `customer_read_orders`: In your app’s `shopify.app.toml` file, include the required [access scopes](https://shopify.dev/docs/apps/build/cli-for-apps/app-configuration#access_scopes). T [cut] (SH-S-5922)
  - `customer_read_orders`: In your app’s `shopify.app.toml` file, include the `customer_read_orders` and `customer_read_customers` access scopes to display a customer’s information using  [cut] (SH-S-5923)
  - `read_all_orders`: \| `read_all_orders`Shopify approval required \| All relevant [orders](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) rather than the default wi [cut] (SH-S-5929)
  - `read_all_orders`: * You need to [request](https://shopify.dev/docs/api/usage/access-scopes#orders-permissions) the `read_all_orders` access scope. You will need this for your ext [cut] (SH-S-5930)
  - and 24 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Orders`: "id": 841785, "name": "Orders", "key": "apiDetailFolder.841785", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSetti [cut] (SA-S-1016)
  - `Order Histories`: "id": 841790, "name": "Order Histories", "key": "apiDetailFolder.841790", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDispla [cut] (SA-S-1018)
  - `Order Items`: "id": 886364, "name": "Order Items", "key": "apiDetailFolder.886364", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplaying [cut] (SA-S-1041)
  - `orders`: {"id": 2, "slug": "orders", "icon": "sicon-box", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_write", " [cut] (SA-S-1547)
  - `order.coupon.updated`: {"id": 257821489, "slug": "order.coupon.updated", "url": "https://docs.salla.dev/doc-433804#orders-webhook-events-model", "order": 0, "is_enabled": true, "name" [cut] (SA-S-1573)
  - `order.shipping.address.updated`: {"id": 1731593753, "slug": "order.shipping.address.updated", "url": "https://docs.salla.dev/doc-433804#orders-webhook-events-model", "order": 0, "is_enabled": t [cut] (SA-S-1574)
  - and 23 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `wc/v3 > network-orders`: 'network-orders' => 'WC_REST_Network_Orders_Controller', (WC-S-0089)
  - `wc/v3 > order-notes`: 'order-notes' => 'WC_REST_Order_Notes_Controller', (WC-S-0090)
  - `wc/v3 > orders`: 'orders' => 'WC_REST_Orders_Controller', (WC-S-0092)
  - `wc/v4 > order-notes`: 'order-notes' => OrderNotesController::class, (WC-S-0134)
  - `wc/v4 > orders`: 'orders' => OrdersController::class, (WC-S-0137)
  - `wc/store/v1 > /order/(?P<id>[\d]+)`: const IDENTIFIER = 'order'; (WC-S-0164)
  - and 8 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-024

Shopify: SH-C-057 Refunds, SH-C-058 Returns and exchanges; Salla: SA-C-045 Order returns and refunds (refund statuses; return shipments); WooCommerce: WC-C-071 Refunds

Basis: SH-C-057 platform_terms "refunds/create"; platform_terms "Refund" | SH-C-058 platform_terms "returns/request"; platform_terms "Return" | SA-C-045 platform_terms "order.refunded"; platform_terms "order.shipment.return.created"; platform_terms "إدارة طلبات الاسترجاع الجزئي والكلي" | WC-C-071 platform_terms "Refunds"; inventory WC-I-0102 "wc/v3 > refunds"

### Where it lives

- **Shopify**
  - `Refund`: "label": "Refund" (SH-S-0932)
  - `order:refund:create`: "section":"Orders","path":":orderId/refund","title":{"value":"Refund"} (SH-S-7097)
  - `Returns and exchanges apps`: "h1": "Returns and exchanges apps" (SH-S-2623)
  - `order:return:create`: "section":"Orders","path":":orderId/return","title":{"value":"Return and exchange"} (SH-S-7098)
  - `order:return-request:review`: "section":"Orders","path":":orderId/returns/:returnId/review","title":{"value":"Review return request"} (SH-S-7099)
- **Salla**
  - `Manage refund statuses`: "orders/control-refund":"Manage refund statuses" (SA-S-1743)
- **WooCommerce**
  - `Refunded order (WC_Email_Customer_Refunded_Order)`: $this->title = __( 'Refunded order', 'woocommerce' ); (WC-S-0302)
  - `Partially refunded order (WC_Email_Customer_Partially_Refunded_Order)`: $this->title = __( 'Partially refunded order', 'woocommerce' ); (WC-S-0316)

### Who decides

- **Shopify**
  - `order:refund:create`: "eligibility":{"oneOf":[{"permissions":["REFUND_ORDERS"]},{"permissions":["REFUND_TO_STORE_CREDIT"]},{"permissions":["QUICK_SALE"]}]} (SH-S-5222)
  - `write_marketplace_returns`: Requires `write_returns` access scope or `write_marketplace_returns` access scope. Also: The user must have `refund_orders` permission. (SH-S-6231)
  - `write_returns`: Requires `write_returns` access scope. Also: The user must have `return_orders` permission. (SH-S-6288)
  - `order:return:create`: "eligibility":{"permissions":["RETURN_ORDERS"]} (SH-S-5223)
- **Salla**
  - `إدارة طلبات الاسترجاع الجزئي والكلي`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "إدارة طلبات الاسترجاع الجزئي والكلي", "description": null, "icon": null, "icon_color": null, "ic [cut] [scope: plan: سلة بلس] (SA-S-1998)
  - `order_refund_payment`: "label": "order show assigned only"}, {"id": 472545641, "name": "order_refund_payment", "label": "order refund payment"}, {"id": 1891583914, "name": "order_brow [cut] (SA-S-2270)
  - `order_refund_payment`: "en": "order show assigned only"}}, {"id": 472545641, "key": "order_refund_payment", "name": {"ar": "إمكانية إرجاع الطلبات", "en": "order refund payment"}}, {"i [cut] (SA-S-2487)
  - `control-refund-status`: {"position": 326, "name": "control-refund-status", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type":  [cut] [scope: plans: plus, pro, special] (SA-S-3287)
  - `orders-bulk-remove-products-refund`: {"position": 332, "name": "orders-bulk-remove-products-refund", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3293)
- **WooCommerce**
  - `refund_line_items`: public static function refund_line_items() { ob_start(); check_ajax_referer( 'order-item', 'security' ); if ( ! current_user_can( 'edit_shop_orders' ) ) { wp_di [cut] (WC-S-5407)

### Who is legally responsible

- **Shopify**
  - `4. Your Responsibilities`: This includes, but is not limited to, authorizing the charge to the customer in respect of the customer's purchase, determining and collecting taxes, refunds, r [cut] (SH-S-0012)
  - `4. Your Responsibilities`: This includes, but is not limited to, authorizing the charge to the customer in respect of the customer's purchase, determining and collecting taxes, refunds, r [cut] (SH-S-0012)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `8. j. Ecommerce Services: Your responsibilities`: are responsible for all questions, complaints, disputes (including chargebacks), refunds, reversals, or fines that arise from your use of Ecommerce Services. [scope: Ecommerce Services (Terms 8.j)] (WC-S-0469)
  - `8. j. Ecommerce Services: Your responsibilities`: must maintain fair and legally compliant return, refund, cancellation, and adjustment policies and clearly explain how customers can request a refund. [scope: Ecommerce Services (Terms 8.j)] (WC-S-5408)

### How it meets the rest

- **Shopify**
  - `refunds/create`: "value": "refunds/create" (SH-S-1325)
  - `read_marketplace_returns`: Requires `read_returns` access scope or `read_marketplace_returns` access scope. (SH-S-6037)
  - `read_marketplace_returns`: Requires `read_orders` access scope. Also: Requires the `read_returns` access scope or `read_marketplace_returns` access scope. (SH-S-6038)
  - `read_marketplace_returns`: **Requires one of the `read_returns` or `read_marketplace_returns` access scopes.:** (SH-S-6039)
  - `read_marketplace_returns`: All triggers require one of the `read_returns` or `read_marketplace_returns` access scopes. Those triggers that require additional scopes are documented where r [cut] (SH-S-6040)
  - `read_returns`: Requires `read_order_edits` access scope or `read_returns` access scope. (SH-S-6063)
  - and 9 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `order.shipment.return.cancelled`: {"id": 809174908, "slug": "order.shipment.return.cancelled", "url": "https://docs.salla.dev/doc-433804#order-shipment-cancelled-webhook-event-model", "order": 0 [cut] (SA-S-1575)
  - `order.shipment.return.created`: {"id": 488637663, "slug": "order.shipment.return.created", "url": "https://docs.salla.dev/doc-433804#order-shipments-webhook-events-model", "order": 0, "is_enab [cut] (SA-S-1576)
  - `order.shipment.return.creating`: {"id": 1847919650, "slug": "order.shipment.return.creating", "url": "https://docs.salla.dev/doc-433804#order-shipments-webhook-events-model", "order": 0, "is_en [cut] (SA-S-1577)
  - `order.refunded`: {"id": 745999872, "slug": "order.refunded", "url": "https://docs.salla.dev/doc-433804#orders-webhook-events-model", "order": 0, "is_enabled": true, "name": {"ar [cut] (SA-S-1587)
  - `# Transactions`: This endpoint allows you to `refund`, `void`, or `reverse` a transaction by passing the `transaction_id` as a path parameter. (SA-S-0180)
  - `أولاً: تعريف محفظة متجرك على سلة`: رصيد المدفوعات الإلكترونية: الرصيد الحالي لمبيعات متجرك، ويمكن الاستفادة منه في عمليات الإرجاع للعميل إضافةً إلى خيار استعراض تفاصيل الرصيد المعروض. (SA-S-0090)
- **WooCommerce**
  - `wc/v3 > order-refunds`: 'order-refunds' => 'WC_REST_Order_Refunds_Controller', (WC-S-0091)
  - `wc/v3 > refunds`: 'refunds' => 'WC_REST_Refunds_Controller', (WC-S-0102)
  - `wc/v4 > refunds`: 'refunds' => RefundsController::class, (WC-S-0138)
  - `Order refunds`: The order refunds API allows you to create, view, and delete individual refunds, based on an existing order. (WC-S-0669)
  - `Refunds`: The refunds API is a simple, read-only endpoint that allows you to retrieve a list of refunds outside the context of an existing order. (WC-S-0680)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-025

Shopify: SH-C-062 Payment providers settings (which payment methods a store accepts), SH-C-076 Third-party payment providers through payments apps; Salla: SA-C-120 External payment gateways connected by the merchant (Moyasar, HyperPay, Tap, PayTabs and others); WooCommerce: WC-C-001 Buyer payments through payment gateways (no balance held in core), WC-C-005 Third-party payment extensions (Marketplace Official payments)

Basis: SH-C-062 platform_terms "Payments"; platform_terms "Payment providers"; statement SH-S-0584 "select payment gateways and providers that are compatible and available in your region" | SH-C-076 inventory SH-I-0368 "read_payment_gateways"; inventory SH-I-2199 "Third-party payment providers" | SA-C-120 statement SA-S-0069 "بوابات الدفع الأخرى (ميسر - هايبر باي)"; statement SA-S-0099 "ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة" | WC-C-001 platform_terms "Payment gateways"; platform_terms "Payments" | WC-C-005 inventory WC-I-0501 "Processors & gateways"

### Where it lives

- **Shopify**
  - `settings/payments`: [**Payment providers**](https://admin.shopify.com/settings/payments) (SH-S-6320)
  - `payments`: "title": "Payments" (SH-S-1488)
  - `help.shopify.com/en/manual/payments/third-party-providers.md`: You can activate or change a payment provider from the **Payments** page of your Shopify admin. (SH-S-0374)
  - `Build options`: There are five types of payments extensions: (SH-S-0445)
  - `Payments Apps API`: "label": "Payments Apps API" (SH-S-0813)
  - `payments:settings:third-party-providers:list`: "section":"Payments","title":{"value":"Third-party payment providers"} (SH-S-7114)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `أولاً: طريقة الوصول لصفحة طرق الدفع`: بوابات الدفع الأخرى (ميسر - هايبر باي) (SA-S-0069)
  - `gateway_settings.tutorial_alert_text`: ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة. لمعرفة المزيد، (SA-S-0099)
- **WooCommerce**
  - `Payments`: $this->label = esc_html_x( 'Payments', 'Settings tab label', 'woocommerce' ); (WC-S-0005)
  - `Payments > main`: const MAIN_SECTION_NAME = 'main'; (WC-S-0029)
  - `Payments`: $menu_title = esc_html__( 'Payments', 'woocommerce' ); (WC-S-0059)
  - `Types of payment gateway: Form based`: This is where the user must click a button on a form that then redirects them to the payment processor on the gateway's own website. [scope: gateway type: Form based] (WC-S-0624)
  - `WooCommerce Payment Gateway API`: Payment gateways in WooCommerce are class based and can be added through traditional plugins. (WC-S-0623)
  - `Creating a basic payment gateway`: Payment gateways should be created as additional plugins that hook into WooCommerce. (WC-S-0627)
  - and 12 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `payments:settings:index`: "eligibility":{"oneOf":[{"permissions":["MANAGE_PAYMENTS_SETTINGS"]},{"permissions":["GIFT_CARDS"]},{"permissions":["SHOPIFY_PAYMENTS_TRANSFERS"]}]} (SH-S-5246)
  - `help.shopify.com/en/manual/payments.md`: When a customer checks out, they can choose to pay for their order using any of the methods that you've activated in the (SH-S-0319)
  - `help.shopify.com/en/manual/payments/third-party-providers.md`: You can activate or change a payment provider from the **Payments** page of your Shopify admin. (SH-S-0374)
  - `help.shopify.com/en/manual/payments/third-party-providers/payment-gateway-availa`: When setting up payments on your Shopify store, select payment gateways and providers that are compatible and available in your region. (SH-S-0584)
  - `Stripe availability in Shopify Payments regions`: then standalone Stripe isn't available as an alternative. [scope: Shopify Payments regions] (SH-S-0384)
  - `help.shopify.com/en/manual/payments/getting-paid.md`: These providers might charge extra fees and enforce rules about what products you can sell using their service. (SH-S-0309)
  - and 7 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `bayan-pay`: {"position": 146, "name": "bayan-pay", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3107)
  - `pay-tabs`: {"position": 150, "name": "pay-tabs", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3111)
  - `tap`: {"position": 168, "name": "tap", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3129)
  - `hyperpay`: {"position": 169, "name": "hyperpay", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3130)
  - `moyasar`: {"position": 170, "name": "moyasar", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3131)
  - `knet`: {"position": 171, "name": "knet", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3132)
  - and 9 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `8. j. Ecommerce Services: Third-Party Services`: You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by  [cut] (WC-S-0651)
  - `8. j. Ecommerce Services: Third-Party Services`: You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by  [cut] (WC-S-0651)
  - `Stripe WooCommerce Extension`: NOTE: The fees for each transaction are determined exclusively by Stripe themselves. [scope: Stripe extension] (WC-S-0901)

### Who is legally responsible

- **Shopify**
  - `help.shopify.com/en/manual/payments/getting-paid.md`: All Shopify-supported payment methods rely on third-party providers to process your transactions. (SH-S-0308)
  - `Considerations table, Payments Partner requirements`: Payments extensions must adhere to all Payments Partner requirements, including revenue share agreements. (SH-S-0443)
  - `C.4. Additional Terms Applicable to Payments Developers, Revenue Share`: As part of the Payments Application approval process, all Payments Developers must enter a Revenue Share agreement. (SH-S-0292)
  - `C.4. Additional Terms Applicable to Payments Developers, Wind Down Period`: If Payments Developer wishes to no longer support the Payments Application, the Parties agree to the following arrangement for a period not to exceed six (6) mo [cut] (SH-S-0293)
- **Salla**
  - `gateway_settings.tutorial_alert_text`: ستُحصَّل مدفوعاتك عبر {{name}} بدلًا من مدفوعات سلة. لمعرفة المزيد، (SA-S-0099)
- **WooCommerce**
  - `8. j. Ecommerce Services: Third-Party Services`: If you use WooPayments or any third-party services, some of your — and your customers’ — data may be submitted directly to or passed to the respective third par [cut] (WC-S-0475)
  - `8. j. Ecommerce Services: Third-Party Services`: While we may license you relevant extensions, we’re not involved in any third-party services tied to those extensions. (WC-S-0652)
  - `8. j. Ecommerce Services: Third-Party Services`: If you use WooPayments or any third-party services, some of your — and your customers’ — data may be submitted directly to or passed to the respective third par [cut] (WC-S-0475)
  - `11. Third-Party Services`: Third-Party Services aren’t vetted, endorsed, or controlled by Automattic. (WC-S-0487)
  - `1.2.10`: 1.2.10. ensure the Product is not a solution for processing or enabling payment transactions (“Payments Solution”). In order to make a Payments Solution availab [cut] (WC-S-0578)
  - `1.2.9`: Partner must enter into a separate agreement with Automattic and/or WooCommerce for any revenue collection related to Total Payments Volume. (WC-S-0579)

### How it meets the rest

- **Shopify**
  - `PaymentSettings`: "name": "PaymentSettings", "kind": "OBJECT", "description": "Settings related to payments." [scope: GraphQL Admin API 2026-10] (SH-S-7460)
  - `read_payment_gateways`: Requires `read_payment_gateways` access scope. (SH-S-6077)
  - `read_payment_sessions`: Requires `read_payment_sessions` access scope. (SH-S-6080)
  - `write_payment_gateways`: Requires `write_payment_gateways` access scope. (SH-S-6261)
  - `write_payment_gateways`: The `write_payment_gateways` and `write_payment_sessions` [access scopes](https://shopify.dev/docs/api/usage/access-scopes#authenticated-access-scopes) are auto [cut] (SH-S-6262)
  - `write_payment_gateways`: The `write_payment_gateways` and `write_payment_sessions` [access scopes](https://shopify.dev/docs/api/usage/access-scopes#authenticated-access-scopes) are auto [cut] (SH-S-6263)
  - and 7 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `gateway_settings.credentials_desc`: يمكنك الحصول على البيانات التالية من حسابك في بوابة الدفع، ثم نسخها وإضافتها في الحقول المخصصة. انتقل إلى (SA-S-0205)
- **WooCommerce**
  - `wc/v3 > payment-gateways`: 'payment-gateways' => 'WC_REST_Payment_Gateways_Controller', (WC-S-0123)
  - `wc/v4 > settings-payment-gateways`: 'settings-payment-gateways' => PaymentGatewaysController::class, (WC-S-0144)
  - `WC_Payment_Gateway`: abstract class WC_Payment_Gateway extends WC_Settings_API { (WC-S-0434)
  - `woocommerce_payment_gateways`: $load_gateways = apply_filters( 'woocommerce_payment_gateways', $load_gateways ); (WC-S-0435)
  - `WC_Payment_Gateway_CC`: class WC_Payment_Gateway_CC extends WC_Payment_Gateway { (WC-S-0436)
  - `WC_Payment_Gateway_ECheck`: class WC_Payment_Gateway_ECheck extends WC_Payment_Gateway { (WC-S-0437)
  - and 7 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**
  - `Stripe availability in Shopify Payments regions`: This is because Stripe is Shopify Payments' banking partner, and all payment reporting and management takes place in your Shopify admin. (SH-S-0383)
  - `Considerations table, Approval process`: To make sure merchants can present a positive buyer experience, payments apps must be approved by Shopify. (SH-S-0442)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

## M-026

Shopify: SH-C-063 Shopify Payments; Salla: SA-C-110 Salla Payments: online payments processed through Salla (مدفوعات سلة; المدفوعات الإلكترونية); WooCommerce: WC-C-006 WooPayments payment processing (Woo-made extension and service), WC-C-010 WooPayments availability by country

Basis: SH-C-063 statement SH-S-0382 "Shopify Payments is the only payment gateway designed and operated by Shopify."; inventory SH-I-2207 "Supported countries for Shopify Payments" | SA-C-110 statement SA-S-0049 "خدمة تقدمها سلة لمعالجة المدفوعات في متجرك بشكل مباشر"; platform_terms "مدفوعات سلة" | WC-C-006 statement WC-S-0557 "WooPayments is the only payment gateway designed by Woo for Woo." | WC-C-010 platform_terms "supported countries"

### Where it lives

- **Shopify**
  - `payments`: "path":"payments" (SH-S-5251)
  - `shopify-payments`: "path":"shopify-payments" (SH-S-5252)
  - `payments`: [**Payments**](https://admin.shopify.com/payments) (SH-S-6321)
  - `Part I, A. The Shopify Payments Service, Our Role`: The Shopify Payments service ("Shopify Payments" or the "Payments Services") is Shopify's integrated payments solution that arranges for the financial services  [cut] (SH-S-0078)
  - `help.shopify.com/en/manual/payments/shopify-payments/onboarding/eligibility.md`: Shopify Payments is an integrated payment gateway offered by Shopify. Only eligible merchants can use Shopify Payments. (SH-S-0325)
  - `Stripe availability in Shopify Payments regions`: Shopify Payments is the only payment gateway designed and operated by Shopify. (SH-S-0382)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Payments`: {"position": 7, "kind": "link", "text": "Payments", "href": "/payments"} (SA-S-1683)
  - `Payment methods`: {"position": 105, "kind": "link", "text": "Payment methods", "href": "/payments", "parent": 0, "list": 9} (SA-S-1875)
  - `@salla.sa/ui-merchant-payments`: {"id": 1729596362158, "name": "@salla.sa/ui-merchant-payments", "Prod": {}, "env": "prod", "path": "/^(/payments(?!/taxes)\|/entity/verifications\|/checkout)(/.*\| [cut] (SA-S-3549)
  - `المدفوعات الإلكترونية`: خدمة تقدمها سلة لمعالجة المدفوعات في متجرك بشكل مباشر، وإتمام العمليات المالية مع البنوك ووسائل الدفع المعتمدة في متجرك بشكل آلي. (SA-S-0049)
- **WooCommerce**
  - `Get paid with WooPayments`: return sprintf( __( 'Get paid with %s', 'woocommerce' ), 'WooPayments' ); (WC-S-0433)
  - `Is WooPayments required to take payments with WooCommerce?`: WooPayments is not required for your WooCommerce site to take payments. WooPayments is only one of many payment gateways available for WooCommerce. (WC-S-0556)
  - `WordPress.com account`: WooPayments requires a WordPress.com account to connect your site to the WooPayments server. (WC-S-0517)
  - `PaymentsController (Payments menu item)`: // When the WooPayments account is onboarded, WooPayments will own the Payments menu item since it is the native Woo payments solution. (WC-S-0621)
  - `Payment solutions`: WooPayments by Woo The only payment solution fully integrated with WooCommerce. (WC-S-0909)
  - `Is WooPayments required to take payments with WooCommerce?`: WooPayments is the only payment gateway designed by Woo for Woo. (WC-S-0557)

### Who decides

- **Shopify**
  - `payments:settings:shopify-payments-accounts`: "eligibility":{"permissions":["MANAGE_PAYMENTS_SETTINGS"]} (SH-S-5092)
  - `payments:settings:setup`: "eligibility":{"permissions":["SHOPIFY_PAYMENTS"]} (SH-S-5080)
  - `payments:settings:shopify-payments`: "eligibility":{"oneOf":[{"permissions":["SHOPIFY_PAYMENTS"]},{"permissions":["MANAGE_PAYMENTS_SETTINGS"]}]} (SH-S-5248)
  - `payments:settings:worldfirst-setup`: "eligibility":{"permissions":["SHOPIFY_PAYMENTS"],"betas":["822a3c21"]} (SH-S-5250)
  - `read_shopify_payments`: Requires `read_shopify_payments` access scope or `read_financial_kyc_information` access scope. Also: The app must have the Shopify Payments or Financial KYC In [cut] (SH-S-6120)
  - `help.shopify.com/en/manual/payments/shopify-payments/supported-countries.md`: You can use Shopify Payments to accept payments at checkout if your business is located in one of the supported countries listed on this page. (SH-S-0323)
  - and 10 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `تفعيل الدفع الإلكتروني`: "extra_icons": null}, {"parent_code": "mzaya-asasy", "title": "تفعيل الدفع الإلكتروني", "description": null, "icon": null, "icon_color": null, "icon_background" [cut] [scope: plan: سلة بلس] (SA-S-1953)
  - `الدفع عبر مدى`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "الدفع عبر مدى", "description": null, "icon": null, "icon_color": null, "icon_background": null, "extra [cut] [scope: plan: سلة بلس] (SA-S-1959)
  - `الدفع عبر البطاقة الائتمانية (فيزا وماستر كارد)`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "الدفع عبر البطاقة الائتمانية (فيزا وماستر كارد)", "description": null, "icon": null, "icon_color": nul [cut] [scope: plan: سلة بلس] (SA-S-1960)
  - `Apple Pay الدفع عبر`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "Apple Pay الدفع عبر", "description": null, "icon": null, "icon_color": null, "icon_background": null,  [cut] [scope: plan: سلة بلس] (SA-S-1962)
  - `stc pay الدفع عبر`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "stc pay الدفع عبر", "description": null, "icon": null, "icon_color": null, "icon_background": null, "e [cut] [scope: plan: سلة بلس] (SA-S-1963)
  - `Google Pay الدفع عبر`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "Google Pay الدفع عبر", "description": null, "icon": null, "icon_color": null, "icon_background": null, [cut] [scope: plan: سلة بلس] (SA-S-1964)
  - and 28 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Local payment methods`: By default, WooPayments accepts payments via credit and debit cards. (WC-S-0871)
  - `Is WooPayments required to take payments with WooCommerce?`: WooPayments is not required for your WooCommerce site to take payments. WooPayments is only one of many payment gateways available for WooCommerce. (WC-S-0556)
  - `WooPayments in Your Country`: If you are an individual or business based in one of our supported countries, you can sign up as a merchant with WooPayments. (WC-S-0510)
  - `Supported countries`: WooPayments is available for individuals and businesses in: (WC-S-0511)
  - `Supported countries`: NOTE: If you’re using WooPayments for a business, the relevant country is the one where your business is registered — not the one in which you personally live. (WC-S-0512)
  - `Other countries`: We prioritize new countries and currencies based on a number of factors, including the number of requests by WooCommerce store owners in that country. (WC-S-0515)
  - and 6 more statements in `platforms/woocommerce/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `Part I, A. Designated Country / Shopify Entity table, row Canada`: Shopify Inc., a Canadian corporation [scope: Designated Country Canada] (SH-S-0146)
  - `Part I, A. The Shopify Payments Service`: None of the Shopify entities listed above are licensed as a bank, payment institution, or money services business, but are instead, respectively, a supplier of  [cut] (SH-S-0080)
  - `Part I, A. Designated Country / Shopify Entity table, row United States`: Shopify Payments (USA) Inc., organized under the laws of Delaware [scope: Designated Country United States] (SH-S-0147)
  - `Part I, A. Designated Country / Shopify Entity table, row Austria ... United Kin`: Shopify International Limited, organized under the laws of Ireland [scope: Designated Countries Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Mexico, Netherlands, Norway, Poland, Portugal, Romania, Slovenia, Spain, Sweden, Switzerland, United Arab Emirates, United Kingdom] (SH-S-0148)
  - `Part I, A. Designated Country / Shopify Entity table, row Australia ... Singapor`: Shopify Commerce Singapore Pte. Ltd., organized under the laws of Singapore [scope: Designated Countries Australia, Hong Kong, Japan, New Zealand, Singapore] (SH-S-0149)
- **Salla**
  - `عقد خدمات الدفع`: -تتم تسوية المدفوعات وتحويلها وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق متجرك. [scope: الإمارات (article: تحويلات مدفوعات سلة والتسويات في الإمارات)] (SA-S-0081)
- **WooCommerce**
  - `1. Who's Who: Woo Services`: If you reside outside of the Designated Countries: WooCommerce, Inc. [scope: residents outside the Designated Countries] (WC-S-0459)
  - `1. Who's Who: Woo Services`: If you reside in the Designated Countries: WooCommerce Ireland Ltd. [scope: residents of the Designated Countries] (WC-S-0460)
  - `8. j. More on WooPayments Specifically`: As part of WooPayments, we may use certain third parties to fulfill our obligations to you, including integrating with payment processing third parties. (WC-S-0476)
  - `Terms of Service`: By clicking the “Finish setup” button in WooPayments, you agree to the Terms of Service. (WC-S-0520)

### How it meets the rest

- **Shopify**
  - `read_shopify_payments`: Requires `read_shopify_payments` access scope. (SH-S-6118)
  - `read_shopify_payments`: Requires the `read_shopify_payments` or the `read_shopify_payments_accounts` access scope. (SH-S-6119)
  - `read_shopify_payments`: Requires `read_shopify_payments` access scope, `read_shopify_payments_accounts` access scope or `read_shopify_payments_payouts` access scope. Also: The user mus [cut] (SH-S-6121)
  - `www.shopify.com/legal/processor-list`: By accepting the Shopify Payments Terms of Service, you accept and agree to be bound by the Payment Processor Terms identified for your Designated Country. (SH-S-0144)
  - `Shopify Payments`: "label": "Shopify Payments" (SH-S-0788)
  - `read_shopify_payments_accounts`: "text": "read_shopify_payments_accounts" (SH-S-1068)
- **Salla**
  - `Payments`: "id": 841791, "name": "Payments", "key": "apiDetailFolder.841791", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSet [cut] (SA-S-1059)
  - `payments`: {"id": 9, "slug": "payments", "icon": "sicon-wallet", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_writ [cut] (SA-S-1554)
  - `order.payment.updated`: {"id": 1480788116, "slug": "order.payment.updated", "url": "https://docs.salla.dev/doc-433804#orders-webhook-events-model", "order": 0, "is_enabled": true, "nam [cut] (SA-S-1583)
- **WooCommerce**
  - `WordPress.com account`: WooPayments requires a WordPress.com account to connect your site to the WooPayments server. (WC-S-0517)
  - `WooPayments built in partnership with Stripe`: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the  [cut] (WC-S-0504)
  - `Connecting to WordPress.com with WooPayments`: WooPayments requires a connection to WordPress.com in order to function properly. (WC-S-0555)
  - `Access to the Stripe dashboard`: WooPayments accounts do not have access to the Stripe Dashboard provided to standard Stripe accounts. (WC-S-0506)

### Stated reason

- **Shopify**
  - `Part I, A. The Shopify Payments Service, Our Role`: The Shopify Payments service ("Shopify Payments" or the "Payments Services") is Shopify's integrated payments solution that arranges for the financial services  [cut] (SH-S-0078)
  - `help.shopify.com/en/manual/payments/shopify-payments.md`: It eliminates the hassle of setting up a third-party payment provider or merchant account and having to enter the credentials into Shopify. (SH-S-0320)
- **Salla**
  - `الربط مع stc pay ضمن مدفوعات سلة`: لكي تتمكن من الربط مع stc pay بكل سهولة دون تعقيد، يمكنك الربط مباشرًة ضمن مدفوعات سلة كون الربط المباشر يضمن تقليل أي مشاكل أو تأخيرات في معاملات الربط، فيسهل  [cut] (SA-S-0128)
- **WooCommerce**
  - `Is WooPayments required to take payments with WooCommerce?`: It integrates into your site’s admin dashboard so that you can manage your payments and orders from one place. (WC-S-0854)
  - `PaymentsController`: // When the WooPayments account is onboarded, WooPayments will own the Payments menu item since it is the native Woo payments solution. (WC-S-0621)
  - `Restrictions on account types`: Some countries do not have access to all account types because our partner (Stripe) strictly adheres to the laws and regulations of the country each account is  [cut] (WC-S-0513)
  - `Restrictions on account types`: Engaging in any commercial activities typically requires a trade license or permit in the UAE. Therefore, only the Business account type is available for the UA [cut] [scope: UAE] (WC-S-0514)
  - `Other countries`: In support of creating a global commerce platform, the WooCommerce team is actively working to make WooPayments available to other countries. (WC-S-5294)

## M-027

Shopify: SH-C-069 Payouts; Salla: SA-C-111 E-payments balance and payouts to the merchant's bank (رصيد المدفوعات الإلكترونية; دورة تحويل المدفوعات الإلكترونية), SA-C-112 Bank account for receiving dues, tied to store verification; WooCommerce: WC-C-007 WooPayments account balance and payouts

Basis: SH-C-069 platform_terms "Payouts"; inventory SH-I-2224 "Bank account requirements for Shopify Payments" | WC-C-007 platform_terms "Payouts"; platform_terms "account balance"; statement WC-S-0529 "This balance is regularly transferred to your bank account or debit card." | SA-C-111 platform_terms "رصيد المدفوعات الإلكترونية"; platform_terms "دورة تحويل المدفوعات الإلكترونية"; statement SA-S-0076 "ثم تُحوّل المستحقات المؤهلة إلى حسابك البنكي" | SA-C-112 statement SA-S-0094 "تستخدمه سلة لتحويل مستحقاتك إلى حسابك البنكي"

### Where it lives

- **Shopify**
  - `settings/payments`: [**Payments**](https://admin.shopify.com/settings/payments) (SH-S-6324)
  - `Shopify Payments`: "label": "Shopify Payments" (SH-S-0788)
  - `payouts`: "section":"Payments","path":"payouts" (SH-S-7102)
  - `finance:payout-reconciliation-report`: "section":"Finances","path":"documents/activity-report","title":{"value":"Shopify Payments activity report"} (SH-S-7103)
- **Salla**
  - `Wallet`: {"position": 106, "kind": "link", "text": "Wallet", "href": "/payments/wallet", "parent": 0, "list": 9} (SA-S-1876)
  - `الأسئلة الشائعة`: الحساب البنكي المرتبط بتوثيق المتجر: تستخدمه سلة لتحويل مستحقاتك إلى حسابك البنكي، ولا يظهر لعملائك. (SA-S-0094)
- **WooCommerce**
  - `What’s the difference between a payout and a deposit in WooPayments?`: After you receive an order via WooPayments, the payment amount (minus our fees) will be added to your account balance. This balance is regularly transferred to  [cut] (WC-S-0529)
  - `WooPayments built in partnership with Stripe`: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the  [cut] (WC-S-0504)

### Who decides

- **Shopify**
  - `finance:payout-reconciliation-report`: "eligibility":{"permissions":["VIEW_PAYOUTS"]} (SH-S-5165)
  - `Payout schedule`: You can choose daily, weekly, or monthly payouts based on your business needs. Some countries, such as Japan, have requirements that limit available payout opti [cut] (SH-S-0342)
  - `Payouts with Shopify Balance`: This means that using your main Balance account lets you receive money from your Shopify sales up to 7 days earlier than a bank. (SH-S-0347)
  - `help.shopify.com/en/manual/payments/shopify-payments/payouts/payout-timing.md`: Payout settlement times vary by country and risk level. (SH-S-0340)
  - `help.shopify.com/en/manual/payments/shopify-payments/payouts.md`: In certain countries, there's a minimum payout amount for Shopify Payments. (SH-S-0339)
  - `Requirements for Multi-Currency Payouts, Plan requirements`: If your store is on the Basic, Grow, or Shopify plan, then you aren't eligible for Multi-Currency Payouts. [scope: stores on the Basic, Grow, or Shopify plan] (SH-S-0365)
  - and 3 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `سجل المدفوعات الإلكترونية`: "extra_icons": null}, {"parent_code": "mhfth-almtgr-oalfotr", "title": "سجل المدفوعات الإلكترونية", "description": null, "icon": null, "icon_color": null, "icon [cut] [scope: plan: سلة بلس] (SA-S-2063)
  - `سجل المدفوعات الإلكترونية`: "extra_icons": null}, {"parent_code": "mhfth-almtgr-oalfotr", "title": "سجل المدفوعات الإلكترونية", "description": null, "icon": null, "icon_color": null, "icon [cut] [scope: plan: سلة بلس] (SA-S-2065)
  - `ابق متصلًا بالعالم مع خيارات الشحن المتنوعة في سلة، ودعم جميع وسائل الدفع الإلكت`: ابق متصلًا بالعالم مع خيارات الشحن المتنوعة في سلة، ودعم جميع وسائل الدفع الإلكتروني، وإيداع المبيعات كل 24 ساعة، لتجارة أيسر ونمو أسرع. [scope: plan: سلة سبيشل] (SA-S-2193)
  - `list_epayments`: "label": "bank accounts management"}, {"id": 1591178023, "name": "list_epayments", "label": "list epayments"}], "position": 12} (SA-S-2436)
  - `list_epayments`: "en": "bank accounts management"}}, {"id": 1591178023, "key": "list_epayments", "name": {"ar": "المدفوعات الإلكترونية", "en": "list epayments"}}], "position": 1 [cut] (SA-S-2646)
  - `دورة تحويل المدفوعات الإلكترونية`: ⚠️ تنويه هام: يجب أن يصل إجمالي المبلغ المستحق للتحويل إلى 100 ريال سعودي على الأقل حتى يتم تحويله إلى حسابك البنكي. (SA-S-0077)
  - and 15 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Payout timing`: It explains how often your balance will be paid out depending on your business location, as well as other important details to keep in mind when it comes to get [cut] (WC-S-0531)
  - `Eligibility`: If your country only has a single currency listed, that means you can only accept payouts in that currency, and those payouts can only be sent to banks in your  [cut] (WC-S-0536)
  - `Debit cards outside the U.S.`: Although Stripe, our payments partner, might allow you to add a debit card even if your account country isn’t the U.S., what they will not do is send payouts to [cut] [scope: account country other than the U.S.] (WC-S-0532)
  - `Debit cards outside the U.S.`: your WooPayments account balance will simply and silently be held until you add a bank account and make it the default payout method. [scope: debit cards outside the U.S.] (WC-S-0530)
  - `“Payouts are temporarily suspended”`: Stripe, our payments partner, has found other issues with your account. (WC-S-0533)

### Who is legally responsible

- **Shopify**
  - `Part I, D. Effects of Termination`: Any funds in the Financial Services Provider's custody will be paid out to you subject to the Payment Processor Terms. (SH-S-0118)
- **Salla**
  - `عقد خدمات الدفع`: -تتم تسوية المدفوعات وتحويلها وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق متجرك. [scope: الإمارات (article: تحويلات مدفوعات سلة والتسويات في الإمارات)] (SA-S-0081)
  - `كيف تعمل التحويلات؟`: تتم تسوية المدفوعات وتحويلها وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق متجرك. [scope: الكويت (article: تحويلات مدفوعات سلة والتسويات في الكويت)] (SA-S-0088)
- **WooCommerce**
  - `Terms 8.j Fees and Negative Balances`: If you have a negative account balance (for example because of fraud, chargebacks, or other operational issues) or we’re obligated to pay or collect any fees re [cut] [scope: Ecommerce Services (Terms 8.j), which name WooPayments] (WC-S-0650)

### How it meets the rest

- **Shopify**
  - `read_shopify_payments_bank_accounts`: Requires `read_shopify_payments_bank_accounts` access scope. (SH-S-6122)
  - `read_shopify_payments_payouts`: Requires `read_shopify_payments` access scope, `read_shopify_payments_accounts` access scope or `read_shopify_payments_payouts` access scope. Also: The user mus [cut] (SH-S-6121)
  - `read_shopify_payments_payouts`: "text": "read_shopify_payments_payouts" (SH-S-1069)
- **Salla**
  - `الأسئلة الشائعة > المدفوعات الإلكترونية > كيفية عملها`: 1- عند قيام العميل بالدفع، تذهب الأموال أولاً إلى رصيد المدفوعات الإلكترونية. (SA-S-0050)
  - `تعرّف على دورة تحويل المدفوعات الإلكترونية`: عند دفع العميل قيمة الطلب باستخدام إحدى وسائل الدفع الإلكتروني، تُضاف قيمة العملية إلى رصيد المدفوعات الإلكترونية، ثم تُحوّل المستحقات المؤهلة إلى حسابك البنكي  [cut] (SA-S-0076)
  - `الأسئلة الشائعة`: لا. رصيد المتجر مخصص لاشتراكات سلة وخدماتها ومشترياتها، بينما يحتفظ رصيد المدفوعات الإلكترونية بمستحقات مبيعات المتجر قبل تحويلها. [scope: الإمارات] (SA-S-0083)
  - `كيف تتابع مستحقاتك؟`: ملاحظة: رصيد المدفوعات الإلكترونية يختلف عن رصيد المتجر؛ فرصيد المدفوعات الإلكترونية يمثل مستحقات مبيعاتك قبل تحويلها إلى حسابك البنكي، بينما يُستخدم رصيد المتج [cut] (SA-S-0079)
  - `الأسئلة الشائعة`: الحساب البنكي المرتبط بتوثيق المتجر: تستخدمه سلة لتحويل مستحقاتك إلى حسابك البنكي، ولا يظهر لعملائك. (SA-S-0094)
  - `الحساب البنكي المستخدم لاستلام التحويلات`: تُرسل التحويلات إلى الحساب البنكي الذي قدّمته أثناء توثيق المتجر. تأكد من تطابق بيانات الحساب مع مستنداتك البنكية. [scope: الإمارات] (SA-S-0085)
- **WooCommerce**
  - `WooPayments built in partnership with Stripe`: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the  [cut] (WC-S-0504)
  - `What’s the difference between a payout and a deposit in WooPayments?`: After you receive an order via WooPayments, the payment amount (minus our fees) will be added to your account balance. This balance is regularly transferred to  [cut] (WC-S-0529)

### Stated reason

- **Shopify**
  - `Troubleshooting payout delays, Payout destination change`: This pause is intended to protect your account from unauthorized access while Shopify verifies the new account. (SH-S-0578)
  - `help.shopify.com/en/manual/payments/shopify-payments/payouts/payout-timing.md`: After funds are paid out, they might take an additional 1-3 days to display in your bank account. This depends on your bank's processing time and is out of Shop [cut] (SH-S-0341)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `"Payouts are currently paused"`: In most cases, payouts are usually paused because there's problem with your bank account that prevents us from issuing a payout. [scope: paused payouts] (WC-S-5289)

## M-028

Shopify: SH-C-070 Reserves and payout holds; WooCommerce: WC-C-008 WooPayments reserves (funds withheld for risk)

Basis: SH-C-070 platform_terms "Reserves" | WC-C-008 platform_terms "reserve"; statement WC-S-0526 "WooPayments: Reserves"

### Where it lives

- **Shopify**
  - `payments/payouts`: [**Payouts**](https://admin.shopify.com/payments/payouts) (SH-S-6325)
- **WooCommerce**
  - `WooPayments: Reserves (NOTE)`: Because Stripe, not WooPayments, applies and manages reserves, they are the best ones to contact about it. (WC-S-0855)

### Who decides

- **Shopify**
  - `Part I, C. Reserves`: We, in our discretion, will set the terms of any Reserve Account and notify you of such terms, which may require that a certain amount (including the full amoun [cut] (SH-S-0112)
  - `Extending, appealing, and removing reserves`: Each reserve has an expiry date, and a risk assessment decides whether to lift, maintain, reduce, or increase the reserve. (SH-S-0351)
  - `Understanding reserves in Shopify Payments`: A reserve is a temporary hold on a portion, in some cases a full amount, of transactions processed through Shopify Payments for a specified period. (SH-S-0348)
  - `Reasons for account holds, Creditor or legal action`: The payment processors that support Shopify Payments (such as Stripe, PayPal, or Adyen, depending on your region) might receive legal notices from third-party c [cut] [scope: the payment processors that support Shopify Payments (such as Stripe, PayPal, or Adyen, depending on region)] (SH-S-0354)
  - `Reasons for account holds, Creditor or legal action`: When this happens, the processor is legally required to place a hold on your payout account for the amount specified in the notice. (SH-S-0355)
  - `Reasons for account holds, Creditor or legal action`: Shopify can't remove this type of hold. Only the payment processor can remove it after receiving a release directly from your creditor. (SH-S-0356)
- **WooCommerce**
  - `WooPayments: Reserves`: Because WooPayments is built in partnership with Stripe, they make the final decision on whether or not to temporarily withhold some or all of your balance base [cut] (WC-S-0526)
  - `Reserves`: Because WooPayments is built in partnership with Stripe, they make the final determination on whether or not to temporarily withhold some (or all) of your payou [cut] (WC-S-0519)

### Who is legally responsible

- **Shopify**
  - `Part I, C. Reserves`: (i) you are not entitled to any interest or other compensation associated with the funds held in the Reserve Account; (ii) you have no right to direct that acco [cut] (SH-S-0113)
- **WooCommerce**: gap (page not read)

### How it meets the rest

- **Shopify**
  - `Understanding reserves in Shopify Payments`: The terms of reserves are communicated to you using email. (SH-S-0349)
- **WooCommerce**
  - `WooPayments: Reserves (NOTE)`: Our visibility into reserves is very limited. We cannot see why one was applied, nor appeal it on your behalf. (WC-S-0528)
  - `What types of reserves are there?`: The email Stripe sends you will tell you which one applies to your account. (WC-S-0856)

### Stated reason

- **Shopify**
  - `Reasons for using reserves in Shopify Payments`: Shopify Payments requires reserves to ensure that funds are available to handle disputes and refunds that might occur (SH-S-0350)
- **WooCommerce**
  - `WooPayments: Reserves`: Reserves are meant to protect the payments processor (Stripe, in this case) against losses arising from future refunds and disputes. (WC-S-0527)

## M-029

Shopify: SH-C-071 Shopify Payments processing rates; Salla: SA-C-113 Online payment fees (رسوم المدفوعات الإلكترونية; fees calculator); WooCommerce: WC-C-012 WooPayments fees

Basis: SH-C-071 inventory SH-I-2219 "Shopify Payments fees"; platform_terms "IC++ fees" | SA-C-113 platform_terms "حاسبة رسوم المدفوعات الإلكترونية"; statement SA-S-0082 "تُحتسب رسوم المدفوعات الإلكترونية وفق عقد خدمات الدفع" | WC-C-012 platform_terms "Fees"; statement WC-S-0537 "WooPayments: Fees"

### Where it lives

- **Shopify**
  - `shopify-payments/terms`: [Terms of Service](https://admin.shopify.com/shopify-payments/terms) (SH-S-6319)
  - `shopify-payments:fees`: "section":"Payments","path":"fees","title":{"value":"Shopify Payments Fees"} (SH-S-7104)
  - `payments:settings:shopify-payments:payments-rates`: "section":"Payments","path":"payments-rates","title":{"value":"Payment rates"} (SH-S-7105)
- **Salla**
  - `wallet.epayment.summary.tooltips.bank_fees`: تشمل رسوم المدفوعات الإلكترونية ورسوم تجربة الشراء. يمكنك الاطَّلاع على التفاصيل من حاسبة الرسوم. (SA-S-5142)
- **WooCommerce**
  - `Amazon Pay fees`: The original fee and the matching refund will both appear in the order timeline and fee breakdown. [scope: Amazon Pay non-card payments] (WC-S-5297)

### Who decides

- **Shopify**
  - `Pricing and fees`: Transactions processed through Shopify Payments, such as Shop Pay and local payment methods, are charged at standard Shopify Payments rates plus a 1.25% premium [cut] [scope: stores that use a third-party payment provider alongside Shopify Payments] (SH-S-0378)
  - `Online standard card rates`: {"kind": "row", "section": 1, "position": 29, "cells": [{"tag": "th", "text": "Online standard card rates", "scope": "row"}, {"tag": "td", "text": "2.9% + 30¢"} [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7021)
  - `Online premium card rates`: {"kind": "row", "section": 1, "position": 30, "cells": [{"tag": "th", "text": "Online premium card rates", "scope": "row"}, {"tag": "td", "text": "3.5% + 30¢"}, [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7022)
  - `Online international rates`: {"kind": "row", "section": 1, "position": 31, "cells": [{"tag": "th", "text": "Online international rates", "scope": "row"}, {"tag": "td", "text": "+ 1%"}, {"ta [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7023)
- **Salla**
  - `حاسبة رسوم المدفوعات الإلكترونية`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "حاسبة رسوم المدفوعات الإلكترونية", "description": null, "icon": null, "icon_color": null, "icon_backgr [cut] [scope: plan: سلة بلس] (SA-S-1969)
  - `رسوم مرنة لبوابة الدفع`: رسوم مرنة لبوابة الدفع [scope: plan: سلة سبيشل] (SA-S-2191)
  - `الرسوم`: تُحتسب رسوم المدفوعات الإلكترونية وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق متجرك. [scope: الإمارات] (SA-S-0082)
  - `رسوم مرنة لبوابة الدفع`: صُمِّمت سلة سبيشل بشكل أساسي للشركات التي تستقبل زخمًا عاليًا من الطلبات لتلبّي أعلى تطلعات الأعمال عبر حلول دفع مرنة. [scope: سلة سبيشل] (SA-S-0204)
  - `wallet.epayment.summary.tooltips.tax`: قيمة ضريبة القيمة المضافة (15%) المطبَّقة على إجمالي الرسوم. (SA-S-0105)
- **WooCommerce**
  - `WooPayments: Fees`: The exact fees we charge differ based on various factors, such as: (WC-S-0537)
  - `WooPayments: Fees`: The country your business is located in. The country your customer is located in. The currency in which the customer paid. The specific payment method used to p [cut] (WC-S-5298)
  - `Notes for all countries`: Transaction fees are not refunded to you when you issue refunds to customers. (WC-S-5299)

### Who is legally responsible

- **Shopify**
  - `Part I, C. Shopify Payments Fees`: Processing Fees shall be collected from you by the applicable Payment Processor on our behalf in accordance with the Payment Processor Terms. (SH-S-0110)
- **Salla**
  - `الرسوم`: تُحتسب رسوم المدفوعات الإلكترونية وفق عقد خدمات الدفع الذي تم توقيعه أثناء توثيق متجرك. [scope: الإمارات] (SA-S-0082)
- **WooCommerce**
  - `8. j. Ecommerce Services: Fees and Negative Balances`: As another example, if you use WooPayments, there are transaction fees and dispute fees. (WC-S-0649)
  - `8. j. Ecommerce Services: Fees and Negative Balances`: If you have a negative account balance (for example because of fraud, chargebacks, or other operational issues) or we’re obligated to pay or collect any fees re [cut] (WC-S-0650)

### How it meets the rest

- **Shopify**
  - `help.shopify.com/en/manual/international/pricing/fees.md`: You can find the fee values in your [Terms of Service](https://admin.shopify.com/shopify-payments/terms). (SH-S-0558)
- **Salla**
  - `fees_calculator.shopping_experience_fee.description`: تشمل خدمات حفظ بطاقة وعنوان العميل، الشراء السريع عبر Apple Pay، الحماية من الاحتيال، ومزايا أخرى من مدفوعات سلة. (SA-S-0104)
- **WooCommerce**
  - `WooPayments: Fees`: Instead, our fees are deducted directly from each payment made via WooPayments. (WC-S-0538)
  - `Paused to recover a negative balance`: To try to recover the negative balance, WooPayments may debit your bank account. (WC-S-0534)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `Amazon Pay fees`: Because Amazon Pay is a wallet that can be funded by cards, bank accounts, and other methods, the fees will vary depending on how the shopper chooses to pay. [scope: Amazon Pay] (WC-S-5300)

## M-030

Shopify: SH-C-072 Chargebacks and disputes; WooCommerce: WC-C-116 Disputes (chargebacks) on WooPayments transactions

Basis: SH-C-072 platform_terms "Disputes"; platform_terms "disputes/create"; inventory SH-I-2204 "Chargebacks and inquiries" | WC-C-116 platform_terms "Managing Disputes"; platform_terms "chargeback"

### Where it lives

- **Shopify**
  - `finance:risk:disputes:details`: "path":"finance/risk/disputes/:id" (SH-S-5244)
  - `dispute-evidences`: "section":"Payments","path":"dispute_evidences" (SH-S-7106)
  - `finance:risk:disputes`: "section":"Finances","path":"risk/disputes","title":{"value":"Disputes"} (SH-S-7107)
- **WooCommerce**
  - `Payments > Disputes`: A red bubble next to the Payments > Disputes menu item. (WC-S-5317)
  - `WooCommerce > Orders`: An alert on the order page under WooCommerce > Orders. (WC-S-5318)

### Who decides

- **Shopify**
  - `write_shopify_payments_dispute_evidences`: Requires `write_shopify_payments_dispute_evidences` access scope. Also: The user must have `manage_orders_information` permission or the `manage_disputes` permi [cut] (SH-S-6296)
  - `help.shopify.com/en/manual/payments/chargebacks.md`: If the cardholder's bank makes a _chargeback_, then the bank takes the disputed amount from you right away. (SH-S-0395)
  - `help.shopify.com/en/manual/payments/chargebacks.md`: Often, the company that issued the cardholder's credit card reviews any evidence, and then resolves the chargeback in either your favor or the cardholder's favo [cut] (SH-S-0396)
  - `help.shopify.com/en/manual/payments/chargebacks.md`: Some disputes are resolved automatically. If your store is enrolled in a network dispute resolution program, then disputes are (SH-S-0397)
  - `Part I, C. Contesting Chargebacks and Disputes`: We may enroll you in automated dispute resolution programs, including those offered by Payment Networks, if we determine, in our sole discretion, that there is  [cut] (SH-S-0114)
  - `Part I, C. Contesting Chargebacks and Disputes`: You or Shopify may elect to contest chargebacks or other disputes assessed to your account. (SH-S-0115)
  - and 4 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `Managing Disputes with WooPayments`: A dispute (also called a “chargeback”) occurs when a cardholder contests a payment made with their card. (WC-S-0866)
  - `How disputes work`: The card issuer (i.e. the customer's bank) decides the outcome. (WC-S-5321)
  - `How disputes work`: NOTE: The dispute outcome is determined solely by the cardholder's bank. Neither we nor our payment processor can influence their decision. (WC-S-5322)

### Who is legally responsible

- **Shopify**
  - `Part I, A. Payment Methods`: and (v) all refunded, reversed or charged back transactions regardless of the reason for, or timing of the refund, reversal, chargeback or other dispute. (SH-S-0092)
  - `Part I, A. Customer Service`: Shopify does not offer any dispute rights to your customers and will not facilitate the resolution of disputes, including without limitation by accepting, inves [cut] (SH-S-0094)
- **WooCommerce**
  - `8. j. Ecommerce Services: Your responsibilities`: are responsible for all questions, complaints, disputes (including chargebacks), refunds, reversals, or fines that arise from your use of Ecommerce Services. (WC-S-0469)
  - `8. j. Ecommerce Services: Fees and Negative Balances`: As another example, if you use WooPayments, there are transaction fees and dispute fees. (WC-S-0649)

### How it meets the rest

- **Shopify**
  - `read_shopify_payments_dispute_evidences`: Requires `read_shopify_payments_dispute_evidences` access scope. (SH-S-6123)
  - `read_shopify_payments_disputes`: The webhook topic for `disputes/create` events. Occurs whenever a dispute is created. Requires the `read_shopify_payments_disputes` scope. (SH-S-6124)
  - `read_shopify_payments_disputes`: The webhook topic for `disputes/update` events. Occurs whenever a dispute is updated. Requires the `read_shopify_payments_disputes` scope. (SH-S-6125)
  - `read_shopify_payments_disputes`: \| `DISPUTES_CREATE` \| A webhook is sent every time a dispute is created. This requires the `read_shopify_payments_disputes` scope on your custom app. \| (SH-S-6126)
  - `read_shopify_payments_disputes`: \| `DISPUTES_UPDATE` \| A webhook is sent every time a dispute is updated. This requires the `read_shopify_payments_disputes` scope on your custom app. \| (SH-S-6127)
  - `help.shopify.com/en/manual/payments/chargebacks.md`: If you're using Shopify Payments and you're issued a chargeback, then the amount is deducted from your next available payout. (SH-S-0398)
  - and 3 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `Dispute notifications`: An email to the address we have on file for your account. (WC-S-5319)
  - `How disputes work`: The disputed amount and the dispute fee are immediately withdrawn from your account and returned to the card issuing bank. (WC-S-5320)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `Managing Disputes with WooPayments`: But not responding to disputes would be worse, because it can lead to fines and/or being prohibited from charging certain types of cards. (WC-S-0867)
  - `Dispute fees`: Keep in mind that dispute fees are originally imposed by card networks. These fees get passed through to our payments processor and then to your WooPayments acc [cut] (WC-S-5323)

## M-031

Shopify: SH-C-075 Shop Pay Installments; Salla: SA-C-118 Buy now, pay later and instalments (Tabby, Tamara, MISpay, Madfu, Emkan, Deema)

Basis: SH-C-075 platform_terms "Shop Pay Installments" | SA-C-118 platform_terms "tabby_installment"; platform_terms "الدفع بالتقسيط عبر تابي وتمارا"

### Where it lives

- **Shopify**
  - `payments:settings:shop-pay-installments`: "section":"Payments","path":"shop-pay-installments" (SH-S-7112)
  - `shop-pay-installments-terms`: "section":"Payments","path":"shop-pay-installments/terms","title":{"value":"Shop Pay Installments Terms of Service"} (SH-S-7113)
- **Salla**
  - `رابعاً: وسائل الدفع الآجلة`: سهّل على عملائك الشراء المباشر والدفع لاحقاً بالتقسيط، بخيارات أكثر أماناً من الدفع عند الاستلام، وذلك باستخدام وسائل الدفع الآجل التي توفرها سلة، وهي: (SA-S-0070)

### Who decides

- **Shopify**
  - `availability note`: Shop Pay Installments is available to eligible stores in the United States, Canada, and the United Kingdom. [scope: eligible stores in the United States, Canada, and the United Kingdom] (SH-S-0414)
  - `help.shopify.com/en/manual/payments/shop-pay-installments.md`: have both Shopify Payments and Shop Pay activated, and have a business entity in one of the following countries: (SH-S-0415)
- **Salla**
  - `الدفع بالتقسيط عبر تابي وتمارا`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "الدفع بالتقسيط عبر تابي وتمارا", "description": null, "icon": null, "icon_color": null, "icon_backgrou [cut] [scope: plan: سلة بلس] (SA-S-1965)
  - `تفعيل الدفع الإلكتروني عبر مدى وأبل باي وتابي وغيرها`: "sub_features": []}, {"title": "تفعيل الدفع الإلكتروني عبر مدى وأبل باي وتابي وغيرها", "description": "فعّل خيارات الدفع الإلكتروني المفضلة لعملائك، مثل: Apple  [cut] [scope: plan: سلة بلس] (SA-S-2106)
  - `tamara`: {"position": 164, "name": "tamara", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3125)
  - `klarna`: {"position": 165, "name": "klarna", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3126)
  - `deema`: {"position": 166, "name": "deema", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3127)
  - `tabby`: {"position": 167, "name": "tabby", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3128)
  - and 6 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `Shop Pay Installments`: You don't have to collect payments from your customers. (SH-S-0318)
  - `Part II, A. Australia / B. Canada / C. United Kingdom / D. United States, Shop P`: By using Shop Pay Installments, you accept and agree to be bound by the Shop Pay Installments Terms and the Merchant Agreement (Shop Pay Installments) with Affi [cut] [scope: Designated Countries with Shop Pay Installments regional terms (Australia, Canada, United Kingdom, United States)] (SH-S-0126)
  - `apps.shopify.com/built-in-features/shop-pay-installments`: Rates from 0-36% APR. For example, a $800 purchase might cost $72.21/mo over 12 months at 15% APR. Payment options through Shop Pay Installments are subject to  [cut] (SH-S-7219)
- **Salla**
  - `apply_policy_desc`: بناءً على طلبك، فإنك توافق وتمنح شركة سلة الحق في مشاركة بيانات متجرك المطلوبة لإتمام تسجيل حسابك مع شركة {{name}}، مع عدم تحميل شركة سلة أي مسؤولية في هذا الشأ [cut] (SA-S-0109)

### How it meets the rest

- **Shopify**
  - `unauthenticated_read_shop_pay_installments_pricing`: Requires `unauthenticated_read_shop_pay_installments_pricing` access scope. (SH-S-6163)
  - `Shop Pay Installments`: Payouts for these orders are included with your Shopify Payments payouts. (SH-S-0317)
  - `Part II, A. Australia / B. Canada / C. United Kingdom / D. United States, Shop P`: By using Shop Pay Installments, you accept and agree to be bound by the Shop Pay Installments Terms and the Merchant Agreement (Shop Pay Installments) with Affi [cut] [scope: Designated Countries with Shop Pay Installments regional terms (Australia, Canada, United Kingdom, United States)] (SH-S-0126)
  - `unauthenticated_read_shop_pay_installments_pricing`: "text": "unauthenticated_read_shop_pay_installments_pricing" (SH-S-1112)
  - `unauthenticated_read_checkouts`: Requires `unauthenticated_read_checkouts` access scope. (SH-S-6147)
- **Salla**
  - `خدمات مساندة`: في حال احتجت إلى مساعدة في تفعيل طرق الدفع أو ربط بوابات الدفع بالمتجر، بالإضافة لخدمات اخرى مثل فتح حساب في تابي أو تمارا للمتجر، لا تتردد في التواصل مع فريق خ [cut] (SA-S-0075)

### Stated reason

- **Shopify**
  - `help.shopify.com/en/manual/payments/shop-pay-installments.md`: Shop Pay Installments lets customers pay for certain orders in installments payments, which offers your customers more flexible payment options and can improve  [cut] (SH-S-0580)
- **Salla**: gap (observation needed)

## M-032

Shopify: SH-C-077 PayPal Express Checkout; Salla: SA-C-119 Digital wallets and other payment methods connected by the merchant (PayPal; STC Pay direct; Mokafaa Al Rajhi); WooCommerce: WC-C-003 PayPal Standard (core gateway that redirects to PayPal)

Basis: SH-C-077 platform_terms "PayPal Express Checkout" | SA-C-119 platform_terms "PayPal الدفع عبر"; platform_terms "paypal" | WC-C-003 platform_terms "PayPal Standard"

### Where it lives

- **Shopify**
  - `2.3 PayPal Express Checkout and Shopify Payments Accounts`: For the avoidance of doubt, PayPal Express Checkout is a Third Party Service, as defined in Section 9.9 of these Terms of Service. (SH-S-0023)
  - `payments:settings:paypal-express-checkout`: "section":"Payments","title":{"value":"PayPal Express Checkout"} (SH-S-7116)
- **Salla**
  - `المحافظ الرقمية`: يتوفر PayPal كخيار للمحفظة الرقمية. اختر PayPal من صفحة «طرق الدفع» وأدخل بيانات الحساب المطلوبة لإتمام الربط. [scope: الإمارات] (SA-S-0199)
  - `الأسئلة الشائعة`: وفي حالة أراد التاجر تفعيل stc pay عبر بوابة سلة، عندها سيتم احتساب رسوم سلة ثم إيقاف الربط المباشر والانتقال إلى الربط عبر بوابة سلة، ولا يمكنه التراجع والعودة [cut] (SA-S-0129)
- **WooCommerce**
  - `PayPal Standard`: $this->method_title = __( 'PayPal Standard', 'woocommerce' ); (WC-S-0283)
  - `paypal (WC_Gateway_Paypal method_description)`: $this->method_description = __( 'PayPal Standard redirects customers to PayPal to enter their payment information.', 'woocommerce' ); (WC-S-0607)

### Who decides

- **Shopify**
  - `help.shopify.com/en/manual/payments/paypal.md`: When you create your Shopify store, you automatically receive a PayPal Express Checkout account. (SH-S-0416)
  - `help.shopify.com/en/manual/payments/paypal.md`: Shopify asks for your email to set up this account, which is then shared with PayPal. (SH-S-0417)
  - `2.3 PayPal Express Checkout and Shopify Payments Accounts`: Upon completion of sign up for the Service, Shopify will create a PayPal Express Checkout account on your behalf, using your Primary Email Address. Depending on [cut] (SH-S-0022)
  - `payment providers table, row PayPal Wallet, column How you get paid`: Through Shopify Payments for only France and the United States [scope: PayPal Wallet: France and the United States] (SH-S-0312)
  - `help.shopify.com/en/manual/payments/paypal.md`: For security, only the store owner can edit your store's PayPal Express information. (SH-S-0418)
  - `PayPal Wallet rates`: {"kind": "row", "section": 1, "position": 32, "cells": [{"tag": "th", "text": "PayPal Wallet rates", "scope": "row"}, {"tag": "td", "text": "Starting at 3.49% + [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7024)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `PayPal الدفع عبر`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "PayPal الدفع عبر", "description": null, "icon": null, "icon_color": null, "icon_background": null, "ex [cut] [scope: plan: سلة بلس] (SA-S-1961)
  - `stc pay الدفع عبر`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "stc pay الدفع عبر", "description": null, "icon": null, "icon_color": null, "icon_background": null, "e [cut] [scope: plan: سلة بلس] (SA-S-1963)
  - `مكافأة الراجحي`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "مكافأة الراجحي", "description": null, "icon": null, "icon_color": null, "icon_background": null, "extr [cut] [scope: plan: سلة بلس] (SA-S-1966)
  - `mokafaa-alrajhi`: {"position": 179, "name": "mokafaa-alrajhi", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special", "pro"], "countries": [], "type":  [cut] [scope: plans: plus, pro, special, pro] (SA-S-3140)
  - `paypal`: {"position": 184, "name": "paypal", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3145)
  - `المحافظ الرقمية`: يتوفر PayPal كخيار للمحفظة الرقمية. اختر PayPal من صفحة «طرق الدفع» وأدخل بيانات الحساب المطلوبة لإتمام الربط. [scope: الإمارات] (SA-S-0199)
  - and 2 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `WC_Gateway_Paypal::should_load`: * By default PayPal Standard isn't loaded on new installs or on existing sites which haven't set up the gateway. (WC-S-0608)
  - `8. j. Ecommerce Services: Third-Party Services`: You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by  [cut] (WC-S-0651)
  - `_should_load`: // Set default `_should_load` to 'yes' on existing stores with PayPal Standard enabled or with existing PayPal Standard orders. $should_load = 'yes' === $this-> [cut] (WC-S-5008)

### Who is legally responsible

- **Shopify**
  - `2.3 PayPal Express Checkout and Shopify Payments Accounts`: For the avoidance of doubt, PayPal Express Checkout is a Third Party Service, as defined in Section 9.9 of these Terms of Service. (SH-S-0023)
  - `2. Account Activation (summary)`: We automatically create certain accounts for you to accept payments. You are responsible for activating and deactivating these accounts and complying with their [cut] (SH-S-0024)
- **Salla**
  - `gateway_settings.apply_policy_desc`: بناءً على طلبك، فإنك توافق وتمنح شركة سلة الحق في مشاركة بيانات متجرك المطلوبة لإتمام تسجيل حسابك مع شركة {{name}}، مع عدم تحميل شركة سلة أي مسؤولية في هذا الشأ [cut] (SA-S-5048)
- **WooCommerce**
  - `Terms 8.j Third-Party Services`: If you use WooPayments or any third-party services, some of your — and your customers’ — data may be submitted directly to or passed to the respective third par [cut] (WC-S-0475)

### How it meets the rest

- **Shopify**
  - `How you get paid`: have their own methods of transferring funds from your customer to you. (SH-S-0311)
  - `2. Account Activation (summary)`: We automatically create certain accounts for you to accept payments. You are responsible for activating and deactivating these accounts and complying with their [cut] (SH-S-0024)
- **Salla**
  - `المحافظ الرقمية`: يتوفر PayPal كخيار للمحفظة الرقمية. اختر PayPal من صفحة «طرق الدفع» وأدخل بيانات الحساب المطلوبة لإتمام الربط. [scope: الإمارات] (SA-S-0199)
- **WooCommerce**
  - `wc/v3 > paypal-standard`: 'paypal-standard' => 'WC_REST_Paypal_Standard_Controller', (WC-S-0128)
  - `wc/v3 > paypal-webhooks`: 'paypal-webhooks' => 'WC_REST_Paypal_Webhooks_Controller', (WC-S-0129)
  - `wc/v3 > paypal-buttons`: 'paypal-buttons' => 'WC_REST_Paypal_Buttons_Controller', (WC-S-0130)
  - `paypal (WC_Gateway_Paypal method_description)`: $this->method_description = __( 'PayPal Standard redirects customers to PayPal to enter their payment information.', 'woocommerce' ); (WC-S-0607)
  - `WPCOM_PROXY_REST_BASE`: private const WPCOM_PROXY_REST_BASE = 'transact/paypal_standard/proxy'; (WC-S-5007)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

## M-033

Shopify: SH-C-079 Manual payment methods; Salla: SA-C-115 Cash on delivery through Salla shipping labels (COD remitted through Salla), SA-C-116 Cash on delivery through the merchant's own carrier or courier, SA-C-117 Bank transfer as a payment method (bank accounts shown to customers); WooCommerce: WC-C-002 Offline payment methods (direct bank transfer, check, cash on delivery)

Basis: SH-C-079 platform_terms "Manual payment methods"; statement SH-S-0322 "manual payment methods such as cash, cash on delivery (COD), and bank transfers" | SA-C-115 inventory SA-I-0765 "Cash on delivery"; inventory SA-I-0958 "الدفع عند الاستلام" | SA-C-116 inventory SA-I-0765 "Cash on delivery" | SA-C-117 platform_terms "التحويل البنكي" | WC-C-002 platform_terms "Direct bank transfer"; platform_terms "Cash on delivery"; platform_terms "offline"

### Where it lives

- **Shopify**
  - `Use a suggested manual payment method`: You can choose from a list of suggested manual payment methods on the **Payment providers** settings page in your Shopify admin. (SH-S-0387)
  - `payments:settings:manual-payment-methods`: "section":"Payments","path":"manual-payment-methods","title":{"value":"Manual payment methods"} (SH-S-7117)
- **Salla**
  - `Cash on delivery`: "shipping/shipping.cod":"Cash on delivery" (SA-S-1765)
  - `Cash on delivery`: "shipping/shipping.cod":"Cash on delivery" (SA-S-1765)
  - `الدفع عند الاستلام ومحفظة العميل > عبر شركة شحن`: 3. من قسم (تسعيرة الشحن)، فعّل خيار (الدفع عند الاستلام) وحدد عمولة الدفع المتفق عليها في عقدك مع شركة الشحن. [scope: الإمارات] (SA-S-0061)
  - `الأسئلة الشائعة`: الحساب البنكي ضمن طرق الدفع: تستخدمه لاستقبال المدفوعات من عملائك عبر التحويل البنكي، ويظهر لهم أثناء إتمام الطلب. (SA-S-0095)
- **WooCommerce**
  - `Payments > offline`: const OFFLINE_SECTION_NAME = 'offline'; (WC-S-0030)
  - `Payments > cod`: const COD_SECTION_NAME = 'cod'; // Cash on delivery. (WC-S-0031)
  - `Payments > bacs`: const BACS_SECTION_NAME = 'bacs'; // Direct bank transfer. (WC-S-0032)
  - `Payments > cheque`: const CHEQUE_SECTION_NAME = 'cheque'; // Cheque payments. (WC-S-0033)
  - `Direct bank transfer`: $this->method_title = __( 'Direct bank transfer', 'woocommerce' ); (WC-S-0280)
  - `Check payments`: $this->method_title = _x( 'Check payments', 'Check payment method', 'woocommerce' ); (WC-S-0281)
  - and 5 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `help.shopify.com/en/manual/payments/manual-payments.md`: When your customers use a manual payment method, you can arrange to receive their payment in a way that works best for them. (SH-S-0385)
  - `Create a custom manual payment method`: If your business has unique needs for collecting payment or if you want to offer your customers alternative ways to pay, such as booking a service and paying in [cut] (SH-S-0583)
  - `Multi-currency support`: To accept manual payments in multiple currencies, you need to use [Shopify Payments](/manual/payments/shopify-payments/) and activate the [international sales t [cut] (SH-S-0388)
  - `transaction fees paragraph`: and you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers. (SH-S-0322)
  - `order:mobile:record-payment`: "eligibility":{"clients":["native"],"permissions":["ORDERS"]} (SH-S-5144)
  - `payments:settings:manual-payment-methods`: "eligibility":{"permissions":["MANAGE_PAYMENTS_SETTINGS"]} (SH-S-5092)
- **Salla**
  - `الدفع عند الاستلام`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "الدفع عند الاستلام", "description": null, "icon": null, "icon_color": null, "icon_background": null, " [cut] [scope: plan: سلة بلس] (SA-S-1958)
  - `تعيين شروط الدفع عند الاستلام`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "تعيين شروط الدفع عند الاستلام", "description": null, "icon": null, "icon_color": null, "icon_ [cut] [scope: plan: سلة بلس] (SA-S-2027)
  - `cod-branded-route`: {"position": 77, "name": "cod-branded-route", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3038)
  - `cod`: {"position": 187, "name": "cod", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3148)
  - `cash-on-delivery-settings`: {"position": 303, "name": "cash-on-delivery-settings", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type [cut] [scope: plans: plus, pro, special] (SA-S-3264)
  - `2- الحد الأقصى للطلب`: 📝 ملاحظة: في حال كانت شركة الشحن المختارة ضمن بوليصات سلة فسيُطبق الحد الأعلى وهو 1000 ريال سعودي. (SA-S-0123)
  - and 15 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `woocommerce_bacs_settings: enabled`: 'enabled' => array( 'title' => __( 'Enable/Disable', 'woocommerce' ), 'type' => 'checkbox', 'label' => __( 'Enable bank transfer', 'woocommerce' ), 'default' => [cut] [scope: Direct bank transfer (bacs)] (WC-S-5001)
  - `woocommerce_cheque_settings: enabled`: 'enabled' => array( 'title' => __( 'Enable/Disable', 'woocommerce' ), 'type' => 'checkbox', 'label' => __( 'Enable check payments', 'woocommerce' ), 'default' = [cut] [scope: Check payments (cheque)] (WC-S-5002)
  - `woocommerce_cod_settings: enabled`: 'enabled' => array( 'title' => __( 'Enable/Disable', 'woocommerce' ), 'label' => __( 'Enable cash on delivery', 'woocommerce' ), 'type' => 'checkbox', 'descript [cut] [scope: Cash on delivery (cod)] (WC-S-5003)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**
  - `الأسئلة الشائعة`: لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة. (SA-S-0120)
  - `الأسئلة الشائعة`: تتم تسوية مبالغ الدفع عند الاستلام مباشرة بين التاجر وشركة الشحن وفقاً للاتفاق المبرم بين الطرفين. (SA-S-0121)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `help.shopify.com/en/manual/payments/manual-payments.md`: Orders that accept manual payments are marked as unpaid on the **Orders** page. (SH-S-0386)
- **Salla**
  - `wallet.cod.summary.tooltips.cod_fees`: تشمل رسوم الدفع عند الاستلام من قِبل شركة الشحن ورسوم تجربة الشراء. (SA-S-0106)
  - `المحفظة وتتبع التحويلات`: تتبع الدفع عند الاستلام في الإمارات: هذه الميزة غير متاحة حاليًا في المحفظة لمتاجر الإمارات. تابع المبالغ من خلال شركة الشحن التي فعّلتها بعقد خارجي أو من خلال  [cut] [scope: الإمارات] (SA-S-0084)
  - `Payments`: "id": 841791, "name": "Payments", "key": "apiDetailFolder.841791", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSet [cut] (SA-S-1059)
  - `الأسئلة الشائعة`: الحساب البنكي ضمن طرق الدفع: تستخدمه لاستقبال المدفوعات من عملائك عبر التحويل البنكي، ويظهر لهم أثناء إتمام الطلب. (SA-S-0095)
- **WooCommerce**
  - `wc/v4 > offline-payment-methods`: 'offline-payment-methods' => OfflinePaymentMethodsController::class, (WC-S-0139)
  - `WC_Gateway_BACS::process_payment`: $order->update_status( $process_payment_status, __( 'Awaiting BACS payment.', 'woocommerce' ) ); (WC-S-0604)
  - `woocommerce_bacs_process_payment_order_status`: $process_payment_status = apply_filters( 'woocommerce_bacs_process_payment_order_status', OrderStatus::ON_HOLD, $order ); [scope: Direct bank transfer (bacs)] (WC-S-5004)
  - `woocommerce_cheque_process_payment_order_status`: $process_payment_status = apply_filters( 'woocommerce_cheque_process_payment_order_status', OrderStatus::ON_HOLD, $order ); [scope: Check payments (cheque)] (WC-S-5005)
  - `woocommerce_cod_process_payment_order_status`: $process_payment_status = apply_filters( 'woocommerce_cod_process_payment_order_status', $order->has_downloadable_item() ? OrderStatus::ON_HOLD : OrderStatus::P [cut] [scope: Cash on delivery (cod)] (WC-S-5006)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `⚙️تخصيص إعدادات الدفع عند الاستلام`: تتيح لك هذه الإعدادات التحكم في ظهور خيار الدفع عند الاستلام لضمان جدوى الطلبات وتقليل الإلغاءات ورفع جودة تجربة التسليم. يمكنك استخدام كل إعداد بمرونة حسب نوع  [cut] (SA-S-0124)
- **WooCommerce**: gap (searched, not found)

## M-034

Shopify: SH-C-084 Payment authorization, capture and order transactions; Salla: SA-C-123 Payment transactions: refund, void and reverse (Transactions)

Basis: SH-C-084 platform_terms "order_transactions/create"; inventory SH-I-0645 "Transaction creation" | SA-C-123 platform_terms "Transactions"; platform_terms "transactions"

### Where it lives

- **Shopify**
  - `orders`: [**Orders**](https://admin.shopify.com/orders) (SH-S-6322)
- **Salla**
  - `Transactions`: {"position": 110, "kind": "link", "text": "Transactions", "href": "/payments/transactions", "parent": 0, "list": 9} (SA-S-1880)
  - `Transactions`: "id": 1826632, "name": "Transactions", "key": "apiDetailFolder.1826632", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1058)

### Who decides

- **Shopify**
  - `help.shopify.com/en/manual/payments/payment-authorization.md`: By default, credit card payments and some additional methods of payment are captured automatically, but if it suits your business better, then you can change yo [cut] (SH-S-0390)
  - `What is a credit card authorization period?`: provides an authorization period of 7 days. (SH-S-0391)
  - `Extended authorization periods, plan requirement`: Extended authorization periods are available only to stores on the Shopify Plus plan that use Shopify Payments. [scope: stores on the Shopify Plus plan that use Shopify Payments] (SH-S-0393)
  - `What is a credit card authorization period?`: The length of the authorization period depends on your credit card payment provider. (SH-S-0392)
- **Salla**
  - `order_refund_payment`: "label": "order show assigned only"}, {"id": 472545641, "name": "order_refund_payment", "label": "order refund payment"}, {"id": 1891583914, "name": "order_brow [cut] (SA-S-2270)
  - `payments_operations_management`: "label": "shipment history management"}, {"id": 981155555, "name": "payments_operations_management", "label": "payments operations management"}, {"id": 33976266 [cut] (SA-S-2420)
  - `order_refund_payment`: "en": "order show assigned only"}}, {"id": 472545641, "key": "order_refund_payment", "name": {"ar": "إمكانية إرجاع الطلبات", "en": "order refund payment"}}, {"i [cut] (SA-S-2487)
  - `payments_operations_management`: "en": "shipment history management"}}, {"id": 981155555, "key": "payments_operations_management", "name": {"ar": "عمليات الدفع الإلكتروني", "en": "payments oper [cut] (SA-S-2637)
  - `payments-operations`: {"position": 337, "name": "payments-operations", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "fe [cut] [scope: plans: plus, pro, special] (SA-S-3298)
  - `line 211 (PUT /transactions/{transaction_id}, Update Transaction)`: The store must have enough balance to process the refund amounts (SA-S-0181)

### Who is legally responsible

- **Shopify**
  - `How a credit card payment gets processed, Capture`: Capturing a payment sends the transaction details to the acquirer, which is a bank or financial institution that processes credit card transactions on behalf of [cut] (SH-S-0315)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `order_transactions/create`: "value": "order_transactions/create" (SH-S-1292)
  - `orders/paid`: "value": "orders/paid" (SH-S-1299)
- **Salla**
  - `Transactions`: "id": 1826632, "name": "Transactions", "key": "apiDetailFolder.1826632", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1058)
  - `transactions`: {"id": 20, "slug": "transactions", "icon": "sicon-receipt-money", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name" [cut] (SA-S-1563)
  - `# Transactions`: This endpoint allows you to `refund`, `void`, or `reverse` a transaction by passing the `transaction_id` as a path parameter. (SA-S-0180)

### Stated reason

- **Shopify**
  - `introduction, reasons for manual capture`: Complying with a local regulation that prescribes online merchants must offer at least one payment method that allows your customer to pay for the order upon de [cut] (SH-S-0394)
- **Salla**: gap (observation needed)

## M-035

Shopify: SH-C-085 Saved customer payment methods and payment mandates; WooCommerce: WC-C-098 Saved payment methods (payment tokens), WC-C-042 WooPayments data and saved-card tokens held by the payment partner

Basis: SH-C-085 platform_terms "read_customer_payment_methods"; statement SH-S-0592 "Store payment methods that can be used to pay for future orders without requiring the customer to manually go through checkout." | WC-C-098 statement WC-S-0943 "an API for storing and managing payment tokens for gateways"; statement WC-S-0943 "choose from saved payment tokens on checkout" | WC-C-042 platform_terms "payment token"; statement WC-S-0554 "These tokens are stored by our payment partner"

### Where it lives

- **Shopify**
  - `customer-payment-methods:show`: "section":"Customers","path":":id/payment_methods","title":{"value":"Payment methods"} (SH-S-7120)
- **WooCommerce**
  - `WooCommerce Payment Token API`: WooCommerce 2.6 introduced an API for storing and managing payment tokens for gateways. Users can also manage these tokens from their account settings and choos [cut] (WC-S-0943)
  - `What about saved cards and subscriptions?`: These tokens are stored by our payment partner and requested through your site’s connection to WordPress.com. (WC-S-0554)
  - `What makes WooPayments PCI Compliant?`: These fields are served securely from our payment partner’s PCI DSS–validated environment. (WC-S-0552)

### Who decides

- **Shopify**
  - `write_payment_mandate`: Requires `write_payment_mandate` access scope. Also: The user must have `pay_orders_by_vaulted_card` permission. The API client must be installed on a Shopify P [cut] (SH-S-6265)
  - `write_payment_mandate`: Requires `write_payment_mandate` access scope. Also: The user must have `pay_orders_by_vaulted_card` permission. (SH-S-6266)
  - `order:mobile:pay-order-by-vaulted`: "eligibility":{"permissions":["PAY_ORDERS_BY_VAULTED_CARD"]} (SH-S-5225)
- **WooCommerce**
  - `WooCommerce Payment Token API`: WooCommerce 2.6 introduced an API for storing and managing payment tokens for gateways. Users can also manage these tokens from their account settings and choos [cut] (WC-S-0943)
  - `Enable payments via saved cards`: Enable payments via saved cards, if checked, allows customers to save their card info to their account on your site, which allows them to check out much faster  [cut] (WC-S-5468)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **WooCommerce**
  - `8. j. More on WooPayments Specifically`: You authorize us to share data relating to WooPayments with the applicable payment processing third party for their use in accordance with their privacy policy. (WC-S-0480)
  - `Information We Collect: Financial Account Info`: If you use WooPayments, we’ll receive information relating to your Stripe account, such as your email address and phone number. (WC-S-0501)

### How it meets the rest

- **Shopify**
  - `read_customer_payment_methods`: The webhook topic for `customer_payment_methods/create` events. Occurs whenever a customer payment method is created. Requires the `read_customer_payment_method [cut] (SH-S-5964)
  - `read_customer_payment_methods`: The webhook topic for `customer_payment_methods/revoke` events. Occurs whenever a customer payment method is revoked. Requires the `read_customer_payment_method [cut] (SH-S-5965)
  - `read_customer_payment_methods`: The webhook topic for `customer_payment_methods/update` events. Occurs whenever a customer payment method is updated. Requires the `read_customer_payment_method [cut] (SH-S-5966)
  - `read_customer_payment_methods`: Requires `read_customers` access scope. Also: Requires `read_customer_payment_methods` scope. (SH-S-5967)
  - `read_customer_payment_methods`: Requires `read_payment_mandate` access scope or `read_customer_payment_methods` access scope. (SH-S-5968)
  - `read_payment_mandate`: Requires `read_payment_mandate` access scope. (SH-S-6078)
  - and 6 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `add_exporter: WooCommerce Customer Payment Tokens`: $this->add_exporter( 'woocommerce-customer-tokens', __( 'WooCommerce Customer Payment Tokens', 'woocommerce' ), array( 'WC_Privacy_Exporters', 'customer_tokens_ [cut] (WC-S-0360)
  - `add_eraser: WooCommerce Customer Payment Tokens`: $this->add_eraser( 'woocommerce-customer-tokens', __( 'WooCommerce Customer Payment Tokens', 'woocommerce' ), array( 'WC_Privacy_Erasers', 'customer_tokens_eras [cut] (WC-S-0364)
  - `WC_Payment_Token`: abstract class WC_Payment_Token extends WC_Legacy_Payment_Token { (WC-S-0438)
  - `WooCommerce Payment Token API`: WooCommerce 2.6 introduced an API for storing and managing payment tokens for gateways. Users can also manage these tokens from their account settings and choos [cut] (WC-S-0943)
  - `What about saved cards and subscriptions?`: These tokens are stored by our payment partner and requested through your site’s connection to WordPress.com. (WC-S-0554)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-036

Shopify: SH-C-086 In-person card payments; WooCommerce: WC-C-014 WooPayments in-person payments (card readers, Tap to Pay)

Basis: SH-C-086 platform_terms "In-person card rates"; platform_terms "Tap to Pay transaction fees" | WC-C-014 platform_terms "In-Person Payments"; statement WC-S-0868 "Tap to Pay"

### Where it lives

- **Shopify**
  - `apps/point-of-sale-channel`: [**Point of Sale**](https://admin.shopify.com/apps/point-of-sale-channel) (SH-S-6329)
  - `help.shopify.com/en/manual/sell-in-person/getting-started/setup-payment-method/s`: After you set up Shopify Payments in your Shopify admin, your customers can make payment card payments in your store with Shopify POS and a (SH-S-0436)
  - `card_present_payments`: "identifier": "card_present_payments" (SH-S-2248)
- **WooCommerce**
  - `WooPayments: In-Person Payments`: With WooPayments’ In-Person Payments feature, your customers can pay via tap, swipe, chip card, or mobile wallet payments, all using our mobile app and a simple [cut] (WC-S-0868)

### Who decides

- **Shopify**
  - `Supported countries and regions`: Only countries where Shopify Payments supports both online and in-person processing are available. (SH-S-0435)
  - `9.3 POS Services`: If your POS Services are enabled with Shopify Payments, you cannot concurrently use any other payment processing service. The payment gateway used for your POS  [cut] (SH-S-0047)
  - `help.shopify.com/en/manual/sell-in-person/shopify-pos/selling-offline/offline-pa`: Offline payments is an optional feature that extends [offline checkout](/manual/sell-in-person/shopify-pos/selling-offline/offline-checkout) to let you accept c [cut] (SH-S-0585)
  - `Considerations for using offline payments`: Canadian businesses can't accept Interac card payments when offline. [scope: Canadian businesses] (SH-S-0588)
  - `In-person card rates`: {"kind": "row", "section": 1, "position": 35, "cells": [{"tag": "th", "text": "In-person card rates", "scope": "row"}, {"tag": "td", "text": "2.6% + 10¢"}, {"ta [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7027)
  - `In-person manual rates`: {"kind": "row", "section": 1, "position": 37, "cells": [{"tag": "th", "text": "In-person manual rates", "scope": "row"}, {"tag": "td", "text": "3.5% + 10¢"}, {" [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7029)
- **WooCommerce**
  - `WooPayments: In-Person Payments`: In-Person Payments is available to qualified merchants based in Australia, Canada, Finland, Ireland, Luxembourg, the Netherlands, New Zealand, Singapore, the Un [cut] (WC-S-0869)
  - `Currencies`: Card readers and Tap to Pay on iPhone/Android can only collect payments in the default currency for each country. (WC-S-0870)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **WooCommerce**
  - `8. j. More on WooPayments Specifically (in-person payments)`: (b) the Stripe Terminal Services Terms and Stripe Terminal Purchase Terms as applicable (WC-S-0850)
  - `8. j. More on WooPayments Specifically (in-person payments)`: These POS terminals are manufactured by third parties and are provided “as-is” and “with all faults.” (WC-S-0481)

### How it meets the rest

- **Shopify**
  - `Considerations for using offline payments`: Offline transactions aren't routed to the payment processor. You might not know that a transaction has failed until you reconnect to the internet. (SH-S-0586)
  - `Considerations for using offline payments`: If a payment is declined after you reconnect, then you can use the email or phone number that you collected for the order to contact the customer and collect th [cut] (SH-S-0587)
- **WooCommerce**
  - `WooPayments: In-Person Payments`: With WooPayments’ In-Person Payments feature, your customers can pay via tap, swipe, chip card, or mobile wallet payments, all using our mobile app and a simple [cut] (WC-S-0868)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-037

Shopify: SH-C-064 Payment processing and settlement for Shopify Payments; WooCommerce: WC-C-048 WooPayments dependence on Stripe and processor substitution

Basis: SH-C-064 platform_terms "Payment Processor"; statement SH-S-0085 "We reserve the right to change the Payment Processors"; statement SH-S-0116 "offer you a substitute payment processor that is integrated with the Shopify Payments Account" | WC-C-048 statement WC-S-0477 "alternative third-party payment processor that is or will be integrated into WooPayments"

### Where it lives

- **Shopify**
  - `Part I, A. The Payment Processor`: The processing and settlement of Transactions ("Payment Processing") is carried out by one or more Payment Processors and any of its Financial Services Provider [cut] (SH-S-0082)
  - `Part I, A. The Payment Processor`: The Payment Processor's role in relation to the Payments Services is to accept and process payment transactions, and/or to settle funds (which for purposes of t [cut] (SH-S-0086)
  - `How a credit card payment gets processed`: Credit card processing is done for you by your payment provider. (SH-S-0316)
  - `10 Tips for Building Resilient Payment Systems, idempotency`: Our centralized payment service can track attempts, which consists of at least one or more (retried) identical API requests, by sending an idempotency key that’ [cut] (SH-S-0452)
- **WooCommerce**
  - `WooPayments built in partnership with Stripe`: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the  [cut] (WC-S-0504)

### Who decides

- **Shopify**
  - `Part I, A. The Payment Processor`: You authorize Shopify to determine which Payment Processor Account(s) we will facilitate opening on your behalf, and where you have multiple Payment Processor A [cut] (SH-S-0084)
  - `Part I, A. The Payment Processor`: We reserve the right to change the Payment Processors, subject to the terms of our agreement with each Payment Processor. (SH-S-0085)
  - `help.shopify.com/en/manual/payments/payment-authorization.md`: If you use Shopify Payments, then it automatically routes each payment to the processor most likely to authorize it. (SH-S-0389)
  - `www.shopify.com/legal/processor-list`: The following tables identify, for each Designated Country, (a) the Payment Processor(s), and (b) the agreements and documents that comprise the Payment Process [cut] (SH-S-0143)
  - `Part I, D. Termination`: If a Payment Processor terminates its Payment Processor Terms or indicates its intention to do so, or if you elect to cease processing with such Payment Process [cut] (SH-S-0116)
  - `Part I, D. Termination`: or, (iii) upon request of the Payment Network, a Payment Processor, or a provider of Payment Methods including a Card issuer. (SH-S-0117)
- **WooCommerce**
  - `8. j. More on WooPayments Specifically`: If we use another third party to fulfill these services, you authorize us to share your payment method information with an alternative third-party payment proce [cut] (WC-S-0477)
  - `Can I use my existing Stripe account with WooPayments?`: No, it is not possible to use an existing Stripe account with WooPayments. (WC-S-0873)
  - `Stripe agreement updates`: In short, opting out will effectively end your usage of WooPayments immediately. (WC-S-0508)
  - `Stripe agreement updates`: Although your remaining account balance will still be paid out as per your usual schedule, you will not be able to: (WC-S-0509)
  - `8. j. Ecommerce Services: Prohibited Uses`: We may terminate your access to our Services or force refunds (where possible) to your subscribers and customers without notice to you if we determine (in our s [cut] (WC-S-0472)
  - `Existing Stripe Accounts`: Although WooPayments built in partnership with Stripe, it is not possible to connect an existing Stripe account to WooPayments. (WC-S-5312)

### Who is legally responsible

- **Shopify**
  - `B. North America, row United States`: Stripe, Inc. [scope: Designated Country United States] (SH-S-0152)
  - `B. North America, row Canada`: Stripe Payments Canada, Ltd. [scope: Designated Country Canada] (SH-S-0154)
  - `B. North America, row Mexico`: Stripe Payments Mexico, S. de RL de CV. [scope: Designated Country Mexico] (SH-S-0155)
  - `C. EMEA, row Austria`: Stripe Payments Europe, Limited. [scope: Designated Country Austria (the row cited)] (SH-S-0158)
  - `C. EMEA, row United Arab Emirates`: Stripe Payments Europe, Limited, organized under the laws of Ireland [scope: Designated Country United Arab Emirates] (SH-S-0159)
  - `D. Asia-Pacific, row Japan`: Stripe Japan, Ltd. [scope: Designated Country Japan] (SH-S-0161)
  - and 11 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `8. j. Ecommerce Services: Third-Party Services`: You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by  [cut] (WC-S-0651)
  - `Stripe agreement updates`: Occasionally, Stripe may update their Connected Account Agreement, which contains the terms you agreed to during the WooPayments signup process. (WC-S-0507)

### How it meets the rest

- **Shopify**
  - `10 Tips for Building Resilient Payment Systems, idempotency`: makes sure we send only a single request to our financial partners (SH-S-0453)
  - `www.shopify.com/legal/processor-list`: By accepting the Shopify Payments Terms of Service, you accept and agree to be bound by the Payment Processor Terms identified for your Designated Country. (SH-S-0144)
  - `Part I, B. Registration`: You understand that by registering for a Shopify Payments Account, you are also registering for one or more Payment Processor Account(s) under the Payment Proce [cut] (SH-S-0105)
  - `Part I, A. The Shopify Payments Service, Our Role`: You hereby appoint us as your agent to deliver information and instructions on your behalf to one or more payment processors that provide such financial service [cut] (SH-S-0079)
  - `10 Tips for Building Resilient Payment Systems, 2. Install Circuit Breakers`: For Shopify Payments credit card transactions, we add the merchant's country code to the endpoint host and port to create a more fine-grained Semian identifier, [cut] (SH-S-0451)
- **WooCommerce**
  - `WooPayments built in partnership with Stripe`: When you sign up for WooPayments, you verify your personal and business information with Stripe. This creates a Stripe Express account that is connected to the  [cut] (WC-S-0504)
  - `Access to the Stripe dashboard`: WooPayments accounts do not have access to the Stripe Dashboard provided to standard Stripe accounts. (WC-S-0506)
  - `Updating account information`: Updating certain account information can only be done in the Stripe Express dashboard. (WC-S-5311)

### Stated reason

- **Shopify**
  - `help.shopify.com/en/manual/payments/payment-authorization.md`: This can improve authorization rates without any extra setup from you. (SH-S-0577)
- **WooCommerce**: gap (searched, not found)

## M-038

Shopify: SH-C-091 Shopify Capital in the United States, SH-C-092 Shopify Capital in the United Kingdom, SH-C-093 Shopify Capital in Canada, SH-C-094 Shopify Capital in Australia, SH-C-095 Shopify Capital in France, SH-C-096 Shopify Capital in Germany, SH-C-097 Shopify Capital merchant cash advances in Ireland, the Netherlands and Spain; Salla: SA-C-128 Financing for merchants (Salla Capital; financial support); WooCommerce: WC-C-016 Merchant financing (Stripe Capital)

Basis: SH-C-091 platform_terms "Capital - US loan"; statement SH-S-0482 "Loan repayments are made from a daily percentage rate of your daily sales." | SH-C-092 platform_terms "Capital - UK Merchant Cash Advance (MCA)" | SH-C-093 platform_terms "Capital - Canada Merchant Cash Advance (MCA)" | SH-C-094 platform_terms "Capital - Australia" | SH-C-095 platform_terms "Shopify Capital loans" | SH-C-096 platform_terms "Shopify Capital loans" | SH-C-097 platform_terms "Shopify Capital merchant cash advances" | SA-C-128 statement SA-S-0111 "capital.active.payment_details.footnote"; statement SA-S-0111 "يُحسب مبلغ التحصيل بنسبة %25 من صافي المبيعات لكل دفعة"; platform_terms "financial-support" | WC-C-016 platform_terms "Stripe Capital"; platform_terms "Merchant financing"; statement WC-S-0861 "automatically repay the financing over time through a percentage of your transactions"

### Where it lives

- **Shopify**
  - `capital:access-account`: "path":"access_account/capital" (SH-S-5096)
  - `finance`: [**Finance**](https://admin.shopify.com/finance) (SH-S-6333)
  - `finance`: [**Finance**](https://admin.shopify.com/finance) (SH-S-6334)
  - `finance`: [**Finance**](https://admin.shopify.com/finance) (SH-S-6336)
  - `finance/capital`: [Capital transaction history](https://admin.shopify.com/finance/capital) (SH-S-6338)
  - `Capital`: "section":"Capital" (SH-S-1551)
  - and 27 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `capital.active.payment_details.footnote`: يُحسب مبلغ التحصيل بنسبة %25 من صافي المبيعات لكل دفعة، ويُحوّل المتبقي إلى حسابك البنكي. يُدار الاستثمار من خلال صندوق سلة بالشراكة مع تنامي. (SA-S-0111)
- **WooCommerce**
  - `Extensions > Store management > Merchant financing`: Merchant financing (WC-S-0748)
  - `WooPayments: Stripe Capital Overview`: WooCommerce has partnered with Stripe to offer eligible businesses access to fast, flexible financing through the Stripe Capital program. (WC-S-0559)

### Who decides

- **Shopify**
  - `capital:root`: "eligibility":{"entitlements":["shopifyFinance.capital"]} (SH-S-5097)
  - `help.shopify.com/en/manual/finance/shopify-capital/eligibility.md`: Eligibility is automatically evaluated based on a variety of factors including sales, disputes, customer interactions, the time you've been a Shopify platform u [cut] (SH-S-0474)
  - `Application process for Shopify Capital`: an underwriting review is conducted by Shopify Capital to determine if your store is eligible for funding. (SH-S-0480)
  - `help.shopify.com/en/manual/finance/shopify-capital/eligibility.md`: You need to be a store owner to apply for funding through Shopify Capital. (SH-S-0475)
  - `help.shopify.com/en/manual/finance/shopify-capital.md`: Eligible businesses based in Australia, Canada, France, Germany, Ireland, the Netherlands, Spain, the United Kingdom, and the United States can apply for Shopif [cut] [scope: businesses based in Australia, Canada, France, Germany, Ireland, the Netherlands, Spain, the United Kingdom, and the United States] (SH-S-0472)
  - `Countries where Shopify Capital is available`: To be eligible for Capital in a country, your principal place of business must be within the country, and your bank account must be located in the country. (SH-S-0479)
  - and 42 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `financial-support`: {"position": 526, "name": "financial-support", "value": {"enabled": false, "released": true, "plans": ["pro", "special"], "countries": [], "type": "feature"}} [scope: plans: pro, special] (SA-S-3487)
  - `capital.status.whats_next.steps.auto_verify.description`: يتحقق مدير الصندوق من بيانات منشأتك وحسابك البنكي. (SA-S-0113)
- **WooCommerce**
  - `Eligibility`: WooCommerce businesses are automatically reviewed for eligibility on a daily basis, and you will be contacted via email if your business qualifies for an offer. (WC-S-0561)

### Who is legally responsible

- **Shopify**
  - `note at end of page`: All funding through Shopify Capital in the United States is issued by WebBank. [scope: United States] (SH-S-0483)
  - `www.shopify.com/pricing (footnote)`: All funding through Shopify Capital in the U.S. is issued by WebBank. [scope: U.S.] (SH-S-7198)
  - `admin plan page (settings/plan) (footnote)`: All funding through Shopify Capital in the United States is issued by WebBank. [scope: United States; store ibx5bt-xy] (SH-S-7199)
  - `apps.shopify.com/built-in-features/shopify-capital`: * Funding through Shopify Capital is available in select countries either as a loan or merchant cash advance. All loans through Shopify Capital are issued by We [cut] (SH-S-7218)
  - `help.shopify.com/en/manual/finance/shopify-capital/united-kingdom.md`: Shopify provides merchant cash advances in the United Kingdom through our partner YouLend under the receivables purchase agreement. [scope: United Kingdom] (SH-S-0484)
  - `note at end of page`: All merchant cash advances through Shopify Capital in the United Kingdom are issued by YouLend. [scope: United Kingdom] (SH-S-0485)
  - and 7 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `capital.faq.items.shariah.answer`: نعم، الهيكل الاستثماري متوافق مع الشريعة، وبإدارة مدير الصندوق تنامي. (SA-S-0112)
  - `capital.active.payment_details.footnote`: يُحسب مبلغ التحصيل بنسبة %25 من صافي المبيعات لكل دفعة، ويُحوّل المتبقي إلى حسابك البنكي. يُدار الاستثمار من خلال صندوق سلة بالشراكة مع تنامي. (SA-S-0111)
  - `اتفاقية الوكالة بالاستثمار`: وافق مدير الصندوق على طلبك. راجع اتفاقية الوكالة بالاستثمار ووافق عليها لبدء إجراءات التحويل. (SA-S-0114)
- **WooCommerce**
  - `Eligibility (footnote)`: Loans issued by Celtic Bank, a Utah-Chartered Industrial Bank Member FDIC. (WC-S-0560)

### How it meets the rest

- **Shopify**
  - `help.shopify.com/en/manual/finance/shopify-capital/united-states.md`: Loan repayments are made from a daily percentage rate of your daily sales. [scope: United States] (SH-S-0482)
  - `help.shopify.com/en/manual/finance/shopify-capital/united-kingdom.md`: Shopify provides merchant cash advances in the United Kingdom through our partner YouLend under the receivables purchase agreement. [scope: United Kingdom] (SH-S-0484)
  - `bank account changes`: If you want to change your bank account for Shopify Payments payouts and your repayments after accepting a loan, then you need to complete a new pre-authorized  [cut] [scope: Canada] (SH-S-0488)
  - `read_capital`: Requires `read_capital` access scope, `read_financial_kyc_information` access scope or `read_shopify_payments_legal_entities` access scope. Also: The app must h [cut] (SH-S-7310)
  - `read_capital`: Requires `read_capital` access scope, `read_financial_kyc_information` access scope or `read_shopify_payments_legal_entities` access scope. Also: The app must h [cut] (SH-S-7310)
  - `read_capital`: Requires `read_capital` access scope, `read_financial_kyc_information` access scope or `read_shopify_payments_legal_entities` access scope. Also: The app must h [cut] (SH-S-7310)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `capital.active.payment_details.footnote`: يُحسب مبلغ التحصيل بنسبة %25 من صافي المبيعات لكل دفعة، ويُحوّل المتبقي إلى حسابك البنكي. يُدار الاستثمار من خلال صندوق سلة بالشراكة مع تنامي. (SA-S-0111)
- **WooCommerce**
  - `Repayment`: You’ll automatically repay the financing over time through a percentage of your transactions according to your repayment rate. (WC-S-0861)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `Repayment`: Rather, the withholding starts after seven days in order to ensure the loan payout is completed before payments begin. (WC-S-5302)

## M-039

Shopify: SH-C-099 Tax forms and tax documents issued to the merchant; WooCommerce: WC-C-021 Tax reporting tied to payments (Form 1099-K, tax invoices for fees)

Basis: SH-C-099 platform_terms "VIEW_TAX_DOCUMENTS"; platform_terms "1099-MISC forms" | WC-C-021 platform_terms "Taxes and Documents"; platform_terms "Form 1099-K"

### Where it lives

- **Shopify**
  - `finance`: [Finance](https://admin.shopify.com/finance) (SH-S-6347)
  - `Criteria for receiving a Form 1099-K`: This form is generated by Shopify Payments and is provided to you and to the IRS annually. (SH-S-0505)
  - `finance:tax-forms:1099-k`: "section":"Banking","path":"finance/tax-forms/1099-k","title":{"value":"1099-K tax forms"} (SH-S-7121)
  - `finance:tax-forms:1099-misc`: "section":"Banking","path":"finance/tax-forms/1099-misc","title":{"value":"1099-MISC tax forms"} (SH-S-7122)
- **WooCommerce**
  - `Payments > Documents`: For EU and UKmerchants who may require VAT invoices for WooPayments fees, those are provided under the Payments > Documents menu in your dashboard. [scope: EU and UK merchants] (WC-S-5309)
  - `Payments > Documents`: For Japan-based merchants who may require JCT invoices for WooPayments fees, those are provided under the Payments > Documents menu in your dashboard. [scope: Japan-based merchants] (WC-S-5310)

### Who decides

- **Shopify**
  - `help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-`: In the United States, tax laws require Payment Settlement Entities (PSEs) such as Shopify Payments to file a Form 1099-K with the Internal Revenue Service (IRS) [cut] [scope: United States] (SH-S-0502)
  - `help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-`: Depending on your jurisdiction, Shopify might also be required to report your sales to the local tax authorities. (SH-S-0504)
  - `Part I, A. Taxes`: Shopify retains the right, but not the obligation, at its sole discretion, to complete and file tax or related reports with tax authorities regarding Transactio [cut] (SH-S-0096)
  - `balance:inactive:tax-forms:1099-misc`: "eligibility":{"permissions":["VIEW_TAX_DOCUMENTS"]} (SH-S-5045)
  - `finance:tax-forms:1099-misc`: "eligibility":{"features":["hasInitiatedOnboardingToBanking"],"permissions":["VIEW_TAX_DOCUMENTS"]} (SH-S-5054)
  - `features.hasInitiatedOnboardingToBanking`: {"set": 0, "section": "features", "key": "hasInitiatedOnboardingToBanking", "value": false} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-advanced (plan not stated); capture-client-store-vny2vy5w (Custom plan, development store); capture-client-store-vny2vy5w (plan not stated); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-grow (plan not stated); capture-plus (Shopify Plus App Development, development store); capture-plus (plan not stated); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); demo-fake-dev-store (plan not stated); fake-demo-sharrwah (trial); fake-demo-sharrwah (plan not stated); fake-demo-sharrwah (Advanced); hjhjhjjjhj (plan not stated); ibx5bt-xy (trial); ibx5bt-xy (plan not stated); ts15uk-ug (trial); ts15uk-ug (plan not stated); zyd38b-ze (trial)] (SH-S-5463)
- **WooCommerce**
  - `Form 1099-K for U.S. merchants`: WooPayments is required to issue a Form 1099-K to U.S. persons if their total payments exceeds a specific minimum threshold. [scope: U.S. persons] (WC-S-0547)
  - `Form 1099-K for U.S. merchants`: In the U.S., a Form 1099-K is an information filing required by the Internal Revenue Service (IRS). [scope: U.S.] (WC-S-0860)

### Who is legally responsible

- **Shopify**
  - `help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-`: In the United States, tax laws require Payment Settlement Entities (PSEs) such as Shopify Payments to file a Form 1099-K with the Internal Revenue Service (IRS) [cut] [scope: United States] (SH-S-0502)
  - `help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-`: If your business accepts online or in-person payments, then you're responsible for reporting this income on your tax returns. (SH-S-0503)
- **WooCommerce**
  - `Form 1099-K for U.S. merchants`: WooPayments is required to issue a Form 1099-K to U.S. persons if their total payments exceeds a specific minimum threshold. [scope: U.S. persons] (WC-S-0547)

### How it meets the rest

- **Shopify**
  - `Criteria for receiving a Form 1099-K`: This form is generated by Shopify Payments and is provided to you and to the IRS annually. (SH-S-0505)
- **WooCommerce**
  - `WooPayments: Tax Documents for VAT/GST/CT`: If your business is based in a country where you may need tax invoices, you can receive a monthly invoice showing our fees and the relevant tax (VAT/GST/CT) on  [cut] (WC-S-0549)

### Stated reason

- **Shopify**
  - `help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-`: In the United States, tax laws require Payment Settlement Entities (PSEs) such as Shopify Payments to file a Form 1099-K with the Internal Revenue Service (IRS) [cut] [scope: United States] (SH-S-0502)
- **WooCommerce**
  - `Form 1099-K for U.S. merchants`: In the U.S., a Form 1099-K is an information filing required by the Internal Revenue Service (IRS). [scope: U.S.] (WC-S-0860)

## M-040

Shopify: SH-C-100 Sales tax and VAT calculation at checkout; Salla: SA-C-160 Taxes per market (Tax settings; Taxes / الضرائب); WooCommerce: WC-C-054 Core tax calculation with merchant-entered rates, WC-C-055 WooCommerce Tax (automated tax calculation service)

Basis: SH-C-100 platform_terms "Taxes and duties"; platform_terms "Automated sales tax calculations"; platform_terms "read_taxes" | SA-C-160 platform_terms "Taxes"; platform_terms "Tax settings"; platform_terms "taxes"; concern "Taxes / الضرائب" | WC-C-054 platform_terms "Tax"; platform_terms "Tax options"; inventory WC-I-0117 "wc/v3 > taxes" | WC-C-055 platform_terms "WooCommerce Tax"; platform_terms "Automated taxes"

### Where it lives

- **Shopify**
  - `taxes`: "title": "Taxes and duties" (SH-S-1492)
  - `Componentizing Shopify’s Tax Engine, subtitle`: How Shopify built for the long term by moving our tax engine to a componentized architecture within Shopify’s codebase with zero downtime. (SH-S-0539)
  - `tax-settings`: "section":"Taxes","path":"taxes" (SH-S-7123)
- **Salla**
  - `Taxes`: {"position": 10, "kind": "link", "text": "Taxes", "href": "/taxes-and-duties"} (SA-S-1686)
  - `Product tax pricing`: "products/products.product_tax_pricing":"Product tax pricing" (SA-S-1752)
  - `Tax settings`: {"position": 109, "kind": "link", "text": "Tax settings", "href": "/payments/taxes", "parent": 0, "list": 9} (SA-S-1879)
  - `@salla.sa/ui-merchant-shipping`: {"id": 1728402729452, "name": "@salla.sa/ui-merchant-shipping", "Prod": {}, "env": "prod", "path": "/^(/shipping\|/payments/taxes)(/.*)?$/", "position": 13} (SA-S-3542)
  - `Taxes`: "id": 841784, "name": "Taxes", "key": "apiDetailFolder.841784", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSettin [cut] (SA-S-1062)
- **WooCommerce**
  - `Tax`: $this->label = __( 'Tax', 'woocommerce' ); (WC-S-0003)
  - `Tax > Tax options`: '' => __( 'Tax options', 'woocommerce' ), (WC-S-0015)
  - `Tax > Standard rates`: 'standard' => __( 'Standard rates', 'woocommerce' ), (WC-S-0016)
  - `Tax > Reduced rate rates`: WC_Tax::create_tax_class( __( 'Reduced rate', 'woocommerce' ) ); (WC-S-0034)
  - `Tax > Zero rate rates`: WC_Tax::create_tax_class( __( 'Zero rate', 'woocommerce' ) ); (WC-S-0035)
  - `Analytics > Taxes`: 'title' => __( 'Taxes', 'woocommerce' ), (WC-S-0072)
  - and 4 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `tax-settings`: "eligibility":{"permissions":["MANAGE_TAXES_SETTINGS"],"entitlements":["shopifyTax.enabled"]} (SH-S-5271)
  - `tax-settings:fee-configurations:create`: "eligibility":{"betas":["43910bdc"],"permissions":["PRODUCTS"]} (SH-S-5273)
  - `tax-settings:shared:switch-tax-product`: "eligibility":{"betas":["4d063e20"],"permissions":["MANAGE_TAXES_SETTINGS"],"entitlements":["shopifyTax.enabled"]} (SH-S-5275)
  - `Tax service availability by region`: The tax services or settings that you can use for your Shopify store depend on the location of your business. (SH-S-0508)
  - `Tax service availability by region, row The United States`: In the United States, you can use <a href="/manual/taxes/shopify-tax">Shopify Tax</a>. [scope: United States] (SH-S-0509)
  - `help.shopify.com/en/manual/taxes/shopify-tax/considerations.md`: Calculations using Shopify Tax are available only for certain transactions, where the order's destination is a location in the United States, European Union, Un [cut] (SH-S-0514)
  - and 8 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `تفعيل فوري لضريبة القيمة المضافة`: "extra_icons": null}]}, {"title": "تفعيل فوري لضريبة القيمة المضافة", "description": "فعّل إظهار الرقم الضريبي وعرض واحتساب الضريبة على المنتجات والشحن", "icon" [cut] [scope: plan: سلة برو] (SA-S-2125)
  - `ضريبة القيمة المضافة`: "sub_features": [{"parent_code": "aldfaa", "title": "ضريبة القيمة المضافة", "description": null, "icon": null, "icon_color": null, "icon_background": null, "ext [cut] [scope: plan: سلة برو] (SA-S-2138)
  - `عرض واحتساب ضريبة القيمة المضافة`: "extra_icons": null}, {"parent_code": "mzaya-asasy", "title": "عرض واحتساب ضريبة القيمة المضافة", "description": null, "icon": null, "icon_color": null, "icon_b [cut] [scope: plan: سلة برو] (SA-S-2142)
  - `tax_management`: "label": "gift system management"}, {"id": 374975390, "name": "tax_management", "label": "tax management"}, {"id": 1613154975, "name": "webhook_management", "la [cut] (SA-S-2407)
  - `tax_management`: "en": "gift system management"}}, {"id": 374975390, "key": "tax_management", "name": {"ar": "إعدادات الضريبة", "en": "tax management"}}, {"id": 1613154975, "key [cut] (SA-S-2624)
  - `tax-profiles`: {"position": 74, "name": "tax-profiles", "value": {"enabled": false, "released": true, "plans": ["pro", "special"], "countries": [], "type": "feature"}} [scope: plans: pro, special] (SA-S-3035)
  - and 7 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `woocommerce_calc_taxes`: 'desc' => __( 'Enable tax rates and calculations', 'woocommerce' ), (WC-S-0601)
  - `Setting up taxes in WooCommerce`: This documentation covers how to set up tax rates in WooCommerce, as well as how the platform handles taxes/VAT/GST based on these settings — not when or what t [cut] (WC-S-0878)
  - `store_address`: 'desc' => __( 'This is where your business is located. Tax rates and shipping rates will use this address.', 'woocommerce' ), (WC-S-0599)
  - `woocommerce_calc_taxes`: 'id' => 'woocommerce_calc_taxes', 'default' => 'no', 'type' => 'checkbox', 'desc_tip' => __( 'Rates will be configurable and taxes will be calculated during che [cut] (WC-S-5382)
  - `Coverage and tax locations: Supported store countries`: Automated tax calculations are available to stores based in the United States, Canada, Australia, the United Kingdom, and these European Union countries: (WC-S-0635)

### Who is legally responsible

- **Shopify**
  - `5. Payment of Fees and Taxes`: You are solely responsible for determining, collecting, withholding, reporting, and remitting applicable taxes, duties, fees, surcharges and additional charges  [cut] (SH-S-0037)
  - `7. Limitation of Liability and Indemnification`: Shopify is not responsible for any of your tax obligations or liabilities related to the use of Shopify's Services. (SH-S-0041)
  - `2. Merchant Obligations`: You are solely responsible for all aspects of tax compliance and obligations related to your Store, including without limitation, the determination, collection, [cut] (SH-S-0596)
  - `2. Merchant Obligations`: You are solely responsible for the classification of products you sell and determining the appropriate Sales Tax treatment of such products. (SH-S-0597)
  - `www.shopify.com/legal/shopify-tax-terms`: “Shopify” means Shopify Inc. and its Affiliates (SH-S-0594)
  - `2. Merchant Obligations`: Shopify makes no guarantees to you in relation to the availability or uptime of Shopify Tax (SH-S-0598)
- **Salla**
  - `شروط التسجيل في هيئة الزكاة والضريبة والجمارك`: إذا كان دخلك أكبر أو يساوي 375 ألف ريال في السنة فأنت ملزم بالتسجيل، أما إذا كان أقل من ذلك فالتسجيل اختياري. [scope: هيئة الزكاة والضريبة والجمارك] (SA-S-5073)
- **WooCommerce**
  - `8. j. Ecommerce Services: Your responsibilities`: are responsible for payment of all applicable Taxes relating to your ecommerce activities and your use of Ecommerce Services. You must collect, report, and/or p [cut] [scope: Ecommerce Services (Terms 8.j)] (WC-S-0467)
  - `Setting up taxes in WooCommerce`: We are not tax professionals; our advice only applies to how to use our software. (WC-S-0879)
  - `WooCommerce Tax Guide`: WooCommerce Tax calculates sales tax at checkout using your store address and the customer’s address. It does not file returns, remit tax, or determine where yo [cut] (WC-S-0633)
  - `8. j. Ecommerce Services: Tax Calculations`: While some Ecommerce Services allow you to include sales taxes in transactions — for example, tax calculations may be provided by Taxamo — you shouldn’t rely so [cut] (WC-S-0473)
  - `8. j. Ecommerce Services: Tax Calculations`: we can’t guarantee that tax calculations you receive through or in connection with our Services are complete and accurate. (WC-S-0474)
  - `Understand the primary tax location`: It calculates automated rates for that location; it does not discover or maintain every state where your business may have a tax obligation. (WC-S-0636)
  - and 1 more statements in `platforms/woocommerce/statements.tsv`

### How it meets the rest

- **Shopify**
  - `read_taxes`: The webhook topic for `tax_services/create` events. Occurs whenever a tax service is created. Requires the `read_taxes` scope. (SH-S-6130)
  - `read_taxes`: The webhook topic for `tax_services/update` events. Occurs whenver a tax service is updated. Requires the `read_taxes` scope. (SH-S-6131)
  - `read_taxes`: Requires `read_taxes` access scope. Also: The user must have access to manage taxes. (SH-S-6132)
  - `read_taxes`: Requires `read_customers` access scope or `read_taxes` access scope. (SH-S-6133)
  - `read_taxes`: \| `read_taxes`Shopify approval required \| `TaxAppConfiguration` and `TaxSettings` objects.Reading `TaxAppConfiguration` also requires the user to have permissio [cut] (SH-S-6134)
  - `write_taxes`: Requires `write_taxes` access scope. Also: The caller must be a tax calculations app. (SH-S-6298)
  - and 6 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Taxes`: "id": 841784, "name": "Taxes", "key": "apiDetailFolder.841784", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSettin [cut] (SA-S-1062)
  - `taxes`: {"id": 10, "slug": "taxes", "icon": "sicon-newspaper-alt", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read [cut] (SA-S-1555)
  - `storetax.created`: {"id": 1674713693, "slug": "storetax.created", "url": "https://docs.salla.dev/doc-433811#store-tax-webhook-events-model", "order": 0, "is_enabled": true, "name" [cut] (SA-S-1621)
  - `line 220 (POST /taxes, Create Tax)`: You **must** add tax rate and specify which country that tax will be applied to (SA-S-0182)
- **WooCommerce**
  - `wc/v3 > tax-classes`: 'tax-classes' => 'WC_REST_Tax_Classes_Controller', (WC-S-0116)
  - `wc/v3 > taxes`: 'taxes' => 'WC_REST_Taxes_Controller', (WC-S-0117)
  - `wc/v4 > settings-tax`: 'settings-tax' => TaxSettingsController::class, (WC-S-0145)
  - `Tax rates`: The taxes API allows you to create, view, update, and delete individual tax rates, or a batch of tax rates. (WC-S-0681)
  - `Tax classes`: The tax classes API allows you to create, view, and delete individual tax classes. (WC-S-0682)
  - `Set up WooCommerce Tax: Before you start`: The connection is required to authenticate the site with the WooCommerce Tax service. (WC-S-0634)
  - and 2 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**
  - `help.shopify.com/en/manual/taxes/shopify-tax.md`: Shopify Tax offers the highest level of sales tax compliance with the least amount of upkeep for merchants that sell to customers in the United States, European [cut] (SH-S-0513)
- **Salla**: gap (searched, not found)
- **WooCommerce**
  - `Important notes`: WooCommerce Tax is designed to remove the work of building and updating custom tax rate tables by automating tax calculations for supported countries. (WC-S-0639)

## M-041

Shopify: SH-C-102 VAT validation, exemptions and invoicing; WooCommerce: WC-C-118 EU VAT number collection and validation (EU VAT Number, a Woo-made extension)

Basis: SH-C-102 platform_terms "VAT validation, exemptions, and invoicing" | WC-C-118 platform_terms "EU VAT Number"; statement WC-S-5464 "Manage VAT number"

### Where it lives

- **Shopify**
  - `help.shopify.com/en/manual/taxes/shopify-tax/vat-validate.md`: VAT validation lets your business customers enter a VAT number at checkout to claim the reverse charge exemption on eligible cross-border orders. (SH-S-0535)
  - `tax-settings:shared:vat-number-validation`: "section":"Taxes","path":"vat-number-validation" (SH-S-7126)
- **WooCommerce**
  - `Settings`: EU VAT Number settings in WooCommerce > Settings > Tax. (WC-S-0964)
  - `product card`: EU VAT Number by Woo (WC-S-0963)

### Who decides

- **Shopify**
  - `Activate VAT validation in checkout`: VAT validation in checkout is available only for stores that use Shopify Tax to calculate tax in the European Union or the United Kingdom. [scope: stores that use Shopify Tax to calculate tax in the European Union or the United Kingdom] (SH-S-0536)
  - `help.shopify.com/en/manual/taxes/shopify-tax/vat-validate.md`: VAT validation lets your business customers enter a VAT number at checkout to claim the reverse charge exemption on eligible cross-border orders. (SH-S-0535)
  - `VAT validation, exemptions, and invoicing`: {"kind": "row", "section": 1, "position": 89, "cells": [{"tag": "th", "text": "VAT validation, exemptions, and invoicing", "scope": "row"}, {"tag": "td", "text" [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7068)
- **WooCommerce**
  - `Remove VAT for Businesses in Your Base Country`: Remove VAT for Businesses in Your Base Country: If activated, businesses with a valid number in your base country will be VAT exempt. [scope: EU VAT Number] (WC-S-5462)
  - `Enable B2B Transactions`: Enable B2B Transactions: This will force users to check out with a VAT number; useful for sites that transact purely from B2B. [scope: EU VAT Number] (WC-S-5463)

### Who is legally responsible

- **Shopify**
  - `help.shopify.com/en/manual/taxes/shopify-tax/vat-validate.md`: When the exemption applies, VAT is removed from the order and the customer is responsible for reporting and paying VAT on their own tax return. [scope: orders where the reverse charge exemption applies] (SH-S-0633)
- **WooCommerce**
  - `5. Fees, Payment, and Renewal: a. Automattic Fees`: Some of our Services are offered for a fee, like certain WordPress.com plans or Woo themes or extensions (collectively, “Paid Services”). (WC-S-0644)

### How it meets the rest

- **Shopify**
  - `Activate VAT validation in checkout`: field [in your checkout](/manual/checkout-settings/checkout-form-options#customer-information) for customers to enter their VAT number and apply the reverse cha [cut] [scope: eligible EU or UK cross-border orders] (SH-S-0670)
- **WooCommerce**
  - `Manage VAT number`: EU VAT Number also works with the Cart and Checkout blocks, where customers can enter and validate their VAT number directly during checkout. [scope: EU VAT Number] (WC-S-5464)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `EU VAT digital goods handling`: VAT on digital goods must be calculated based on customer location, and store owners need to collect evidence of this via IP address and Billing Address. [scope: B2C sales of digital goods] (WC-S-5465)

## M-042

Shopify: SH-C-105 Duties and import taxes; Salla: SA-C-162 Customs duties on cross-border orders; WooCommerce: WC-C-058 Customs duties and import taxes on shipments

Basis: SH-C-105 platform_terms "Duties and import tax transaction fees"; platform_terms "Shipping duties and import taxes" | SA-C-162 statement SA-S-5075 "الرسوم الجمركية"; statement SA-S-5074 "المعلومات الجمركية" | WC-C-058 platform_terms "customs charges, import taxes or duties"

### Where it lives

- **Shopify**
  - `markets`: [**Markets**](https://admin.shopify.com/markets) (SH-S-6323)
  - `help.shopify.com/en/manual/international/duties-and-import-taxes.md`: You can collect an estimate of those amounts at checkout instead, which helps your customers avoid unexpected charges on delivery. (SH-S-0538)
  - `tax-settings:duties-and-taxes`: "section":"Taxes","path":"duties" (SH-S-7129)
- **Salla**
  - `Taxes`: {"position": 10, "kind": "link", "text": "Taxes", "href": "/taxes-and-duties"} (SA-S-1686)
- **WooCommerce**
  - `Extensions > Store management > Sales tax and duties`: Sales tax and duties (WC-S-0751)
  - `Product customs data`: WooCommerce stores three optional customs fields on products and variations. (WC-S-5383)

### Who decides

- **Shopify**
  - `Understanding what your customer is charged`: Customs authorities set the amount from the product's classification, its origin, and the destination's rules. (SH-S-0537)
  - `help.shopify.com/en/manual/international/duties-and-import-taxes.md`: You can collect an estimate of those amounts at checkout instead, which helps your customers avoid unexpected charges on delivery. (SH-S-0538)
  - `Estimate and collect duties and taxes`: {"kind": "row", "container": 9, "position": 5, "label": "Estimate and collect duties and taxes", "cells": ["enabled", "enabled", "enabled", "enabled"]} [scope: store ibx5bt-xy (trial), Compare plans table in Settings > Plan] (SH-S-7079)
- **Salla**
  - `إظهار حقل المعلومات الجمركية`: 2. فعّل خيار (إظهار حقل المعلومات الجمركية). [scope: الشحن الدولي إلى قطر وعُمان] (SA-S-5074)
- **WooCommerce**
  - `Product data > Shipping > Customs`: Open a product in the classic product editor. In **Product data → Shipping → Customs**, enter: (WC-S-5384)

### Who is legally responsible

- **Shopify**
  - `5. Payment of Fees and Taxes`: You are solely responsible for determining, collecting, withholding, reporting, and remitting applicable taxes, duties, fees, surcharges and additional charges  [cut] (SH-S-0037)
  - `B. Your Responsibilities`: Shopify is not responsible or liable for any local customs charges, import taxes, duties, or other similar charges associated with your shipments. (SH-S-0618)
  - `help.shopify.com/en/manual/international/managed-markets.md`: When using Managed Markets, you don't need tax registration in the countries you sell to. Global-e provides the tax registration, allowing you to comply when se [cut] [scope: stores using Managed Markets] (SH-S-0564)
  - `Managed Markets benefits`: When the amount charged by customs is different, Managed Markets covers the difference, and you don't have to pay any additional fees. [scope: stores using Managed Markets] (SH-S-0571)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `8. j. More on Shipping Services Specifically`: You’re solely responsible for compliance with all applicable rules and regulations, including domestic and international shipping and customs regulations and an [cut] [scope: shipping Services (Terms 8.j)] (WC-S-0484)
  - `8. j. More on Shipping Services Specifically (DHL)`: In addition, you’re solely responsible for customs charges, import taxes or duties, and any other charges related to your shipments. [scope: follows "When using DHL's services:" (Terms 8.j)] (WC-S-0485)

### How it meets the rest

- **Shopify**
  - `Duty`: "name": "Duty", "kind": "OBJECT", "description": "The duty details for a line item." [scope: GraphQL Admin API 2026-10] (SH-S-7456)
- **Salla**
  - `الرسوم الإضافية للشحن الدولي`: بعد احتساب الرسوم الجمركية والرسوم الإضافية للشحن الدولي بما يخص البوليصات سيتم تسويتها مباشرة من خلال رصيد المحفظة. [scope: بوليصات سلة] (SA-S-5075)
- **WooCommerce**
  - `customs_commodity_code, customs_country_of_origin, customs_description`: The `/wc/v3/products` and `/wc/v3/products/{product_id}/variations` endpoints expose `customs_commodity_code`, `customs_country_of_origin`, and `customs_descrip [cut] (WC-S-5385)

### Stated reason

- **Shopify**
  - `help.shopify.com/en/manual/international/duties-and-import-taxes.md`: You can collect an estimate of those amounts at checkout instead, which helps your customers avoid unexpected charges on delivery. (SH-S-0538)
- **Salla**
  - `💡 نصائح مهمة للتجار`: يسهّل التخليص الجمركي ويحسّن تجربة العميل في الشحن الدولي. (SA-S-0146)
- **WooCommerce**
  - `Product customs data`: They help merchants keep a description of goods for cross-border shipping. They do not calculate duties or produce shipping labels. (WC-S-5386)

## M-043

Shopify: SH-C-106 Markets; Salla: SA-C-165 Markets: per-country versions of a store (Markets / الأسواق المتعددة; Store Scopes)

Basis: SH-C-106 platform_terms "Markets"; platform_terms "markets/create" | SA-C-165 platform_terms "Markets"; platform_terms "Market selection"; concern "Markets / الأسواق المتعددة"

### Where it lives

- **Shopify**
  - `market`: "path":"markets" (SH-S-5202)
  - `markets`: [**Markets**](https://admin.shopify.com/markets) (SH-S-6353)
  - `Markets`: "text": "Markets" (SH-S-1528)
  - `Shopify Markets`: "label": "Shopify Markets" (SH-S-0787)
- **Salla**
  - `Market selection`: "markets/browse_product_method":"Market selection" (SA-S-1730)
  - `Markets`: "markets":"Markets" (SA-S-1769)
  - `Store Scopes`: "id": 3291929, "name": "Store Scopes", "key": "apiDetailFolder.3291929", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1055)

### Who decides

- **Shopify**
  - `market`: "eligibility":{"clients":[],"permissions":[],"plans":[],"excluded":{"betas":[],"clients":[],"features":[],"plans":[]},"oneOf":[{"permissions":["OVERVIEWS","REPO [cut] (SH-S-5203)
  - `option-definition:create`: "eligibility":{"features":["marketDrivenShipping"],"oneOf":[{"permissions":["OVERVIEWS","REPORTS","PRODUCTS","DOMAINS","PREFERENCES"]},{"permissions":["VIEW_MAR [cut] (SH-S-5205)
  - `help.shopify.com/en/manual/markets.md`: You can use Markets to manage how different customers experience your store based on their location, customer group, retail location, or sales channel. (SH-S-0540)
  - `Customizing market experiences`: Customizations control settings, such as currency, product availability, theme content, domains, languages, and taxes. (SH-S-0541)
  - `features.marketDrivenShipping`: {"set": 0, "section": "features", "key": "marketDrivenShipping", "value": true} [scope: 2jiwxs-gr (trial); capture-client-store-vny2vy5w (Custom plan, development store); capture-plus-dev (Shopify Plus App Development, development store)] (SH-S-5777)
  - `features.marketDrivenShipping`: {"set": 0, "section": "features", "key": "marketDrivenShipping", "value": false} [scope: capture-advanced (Advanced App Development, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5778)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `multi-market-origin-country-filter`: {"position": 50, "name": "multi-market-origin-country-filter", "value": {"enabled": true, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3011)
  - `multi-countries-activate`: {"position": 378, "name": "multi-countries-activate", "value": {"enabled": false, "released": true, "plans": ["pro"], "countries": [], "type": "feature"}} [scope: plans: pro] (SA-S-3339)
  - `multi-countries-basic`: {"position": 379, "name": "multi-countries-basic", "value": {"enabled": false, "released": false, "plans": ["pro", "special"], "countries": [], "type": "feature [cut] [scope: plans: pro, special] (SA-S-3340)
  - `customize-login-for-multi-markets`: {"position": 381, "name": "customize-login-for-multi-markets", "value": {"enabled": false, "released": true, "plans": ["pro", "special"], "countries": [], "type [cut] [scope: plans: pro, special] (SA-S-3342)
  - `multi-countries`: {"position": 539, "name": "multi-countries", "value": {"enabled": false, "released": true, "plans": ["special", "pro"], "countries": [], "type": "feature", "cou [cut] [scope: plans: special, pro] (SA-S-3500)
  - `multi-countries-link`: {"position": 563, "name": "multi-countries-link", "value": {"enabled": false, "released": false, "plans": ["special"], "type": "feature"}} [scope: plans: special] (SA-S-3524)
  - and 4 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `merchant of record`: Unless another party such as Global-e is hired to take on these responsibilities, most merchants act as their own merchant of record. When you act as your own m [cut] (SH-S-7275)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `customer_read_markets`: Requires `customer_read_markets` access scope. (SH-S-5919)
  - `read_markets`: The webhook topic for `markets_backup_region/update` events. Occurs when a backup region is updated. Requires the `read_markets` scope. (SH-S-6041)
  - `read_markets`: The webhook topic for `markets/create` events. Occurs when a new market is created. Requires the `read_markets` scope. (SH-S-6042)
  - `read_markets`: The webhook topic for `markets/delete` events. Occurs when a market is deleted. Requires the `read_markets` scope. (SH-S-6043)
  - `read_markets`: The webhook topic for `markets/update` events. Occurs when a market is updated. Requires the `read_markets` scope. (SH-S-6044)
  - `read_markets`: Requires Any of `orders` or `shipping` access scopes, `read_markets` access scope or `manage_delivery_settings` user permission. (SH-S-6045)
  - and 6 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Store Scopes`: "id": 3291929, "name": "Store Scopes", "key": "apiDetailFolder.3291929", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1055)
  - `line 191 (GET /scopes, List Store Scopes)`: This endpoint allows you to list store scopes for multi-country functionality. (SA-S-0184)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-044

Shopify: SH-C-107 Store currency, SH-C-108 Prices in local currencies, SH-C-109 Currency conversion and exchange rates; Salla: SA-C-163 Store currencies shown to customers (Currencies / العملات); WooCommerce: WC-C-051 WooPayments payout currency and currency conversion, WC-C-052 Store currency (one base currency per store), WC-C-053 Selling in more than one currency (multi-currency)

Basis: SH-C-107 platform_terms "store currency" | SH-C-108 platform_terms "Show prices in local currencies*"; inventory SH-I-2172 "Testing your multiple currency setup" | SH-C-109 platform_terms "Currency conversions and exchange rates" | SA-C-163 platform_terms "Currencies"; platform_terms "currency-exchange"; concern "Currencies / العملات" | WC-C-052 platform_terms "base currency"; statement WC-S-0876 "Setting a store’s base currency" | WC-C-053 platform_terms "multi-currency" | WC-C-051 platform_terms "currency conversion fee"

### Where it lives

- **Shopify**
  - `store currency`: Your store currency is the currency used within your Shopify admin for pricing products and running reports. (SH-S-0361)
  - `markets`: [**Markets**](https://admin.shopify.com/markets) (SH-S-6354)
  - `markets`: [**Markets**](https://admin.shopify.com/markets) (SH-S-6356)
- **Salla**
  - `Currencies`: "general/currencies":"Currencies" (SA-S-1724)
  - `@salla.sa/ui-merchant-manage`: {"id": 1727862649468, "name": "@salla.sa/ui-merchant-manage", "Prod": {}, "env": "prod", "path": "/^/manage/(custom-urls\|webhooks\|migrate\|complaints\|violation\|c [cut] (SA-S-3533)
  - `Currencies`: "id": 841812, "name": "Currencies", "key": "apiDetailFolder.841812", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingS [cut] (SA-S-1060)
- **WooCommerce**
  - `General`: $this->label = __( 'General', 'woocommerce' ); (WC-S-0001)
  - `Shop currency`: If you’d like to display products in different currencies (or allow customers to pay in a currency that differs from your shop’s base currency), you will need t [cut] (WC-S-0875)
  - `Currencies in a transaction`: Using WooPayments’ built-in multi-currency functions, the customer currency can be changed. [scope: WooPayments] (WC-S-0541)

### Who decides

- **Shopify**
  - `help.shopify.com/en/manual/payments/shopify-payments/onboarding/account-setup.md`: before making your first sale. It’s the currency that will be used throughout your Shopify admin, for pricing your products and viewing your reports. (SH-S-0671)
  - `Store currency`: Your store currency is the currency used within your Shopify admin for pricing products and running reports. (SH-S-0361)
  - `help.shopify.com/en/manual/payments/shopify-payments/onboarding/account-setup.md`: If you need to change your store currency after making your first sale, then contact Shopify Support. (SH-S-0370)
  - `Shopify Payments and other payment providers`: Only stores with [Shopify Payments](/manual/payments/shopify-payments) or [Adyen](/manual/payments/third-party-providers/adyen-gateway) as the primary gateway c [cut] (SH-S-0545)
  - `Shopify Payments and other payment providers`: At checkout, the price will be converted to your store's default currency, and your customer will be charged in that currency. (SH-S-0546)
  - `help.shopify.com/en/manual/international/pricing.md (note)`: Only stores using Shopify Payments with access to <a href="/en/manual/checkout-settings/customize-checkout-configurations/one-page-checkout">one-page checkout</ [cut] [scope: stores using Shopify Payments with access to one-page checkout] (SH-S-0543)
  - and 13 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `إتاحة الدفع عبر +33 عملة`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "إتاحة الدفع عبر +33 عملة", "description": null, "icon": null, "icon_color": null, "icon_background": n [cut] [scope: plan: سلة بلس] (SA-S-1970)
  - `currency_setting_edit`: "label": "store setting edit social media account"}, {"id": 16435258, "name": "currency_setting_edit", "label": "currency setting edit"}, {"id": 1318388567, "na [cut] (SA-S-2388)
  - `currency_setting_edit`: "en": "store setting edit social media account"}}, {"id": 16435258, "key": "currency_setting_edit", "name": {"ar": "إعدادات العملات", "en": "currency setting ed [cut] (SA-S-2605)
  - `reflect-market-currency`: {"position": 362, "name": "reflect-market-currency", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3323)
  - `currency`: {"position": 397, "name": "currency", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3358)
  - `currency-exchange`: {"position": 478, "name": "currency-exchange", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3439)
  - and 5 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Payout currencies`: If you take a payment in a currency that doesn’t match the currency of one of your bank accounts, it will be converted into your default currency and paid out i [cut] (WC-S-0535)
  - `What currency conversion fees are charged with WooPayments?`: When the currency of a customer payment differs from the currency of any bank account you have on file, WooPayments charges a currency conversion fee as part of [cut] (WC-S-0540)
  - `Eligibility`: If your country only has a single currency listed, that means you can only accept payouts in that currency, and those payouts can only be sent to banks in your  [cut] (WC-S-0536)
  - `What currency is used to determine fees`: If the currency in which the customer paid does not match the currency of any bank account on file, the order total is converted to the default currency and the [cut] (WC-S-0539)
  - `Payout currencies`: When using multiple bank accounts, one must be chosen as the default. (WC-S-5314)
  - `Shop currency`: WooCommerce only allows for one base currency per store. (WC-S-0874)
  - and 6 more statements in `platforms/woocommerce/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `Conversion rate and fee`: The fee that Shopify charges (in your payout currency) to convert currencies when you capture a payment. (SH-S-0554)
  - `Currency conversion risks`: Whenever there is a time delay in processing payments or refunds, there is a possibility that you might lose or gain money because of currency conversions. (SH-S-0550)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (page not read; stated only in general terms)

### How it meets the rest

- **Shopify**
  - `Shop.currencyCode`: {"name": "currencyCode", "type": "CurrencyCode!"} [scope: GraphQL Admin API 2026-10] (SH-S-7457)
  - `Set a currency for a market in Markets`: The currency that you select for a market is the currency that's displayed to customers on your online store, and that transactions are performed in. (SH-S-0547)
  - `help.shopify.com/en/manual/international/pricing/fees.md`: You can find the fee values in your [Terms of Service](https://admin.shopify.com/shopify-payments/terms). (SH-S-0558)
- **Salla**
  - `Currencies`: "id": 841812, "name": "Currencies", "key": "apiDetailFolder.841812", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingS [cut] (SA-S-1060)
  - `Currency`: "id": 849360, "name": "Currency", "key": "apiDetailFolder.849360", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingSetti [cut] (SA-S-1148)
  - `metadata`: {"id": 14, "slug": "metadata", "icon": "sicon-badge", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_writ [cut] (SA-S-1562)
- **WooCommerce**
  - `Payout currencies`: To avoid these fees, you may be able to have funds in different currencies paid out into separate bank accounts. (WC-S-5313)
  - `wc/v3 > data-currencies`: 'data-currencies' => 'WC_REST_Data_Currencies_Controller', (WC-S-0127)
  - `Exchange rate`: By default, exchange rates are regularly retrieved from the WooPayments server. [scope: WooPayments] (WC-S-0543)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**
  - `Payouts`: If your store accepts multiple currencies, you might also be able to accept payouts in multiple currencies as well, in order to avoid currency conversion fees. (WC-S-5315)

## M-045

Shopify: SH-C-114 Shipping profiles, zones and rates; Salla: SA-C-142 Shipping zones, rates and shipping restrictions; WooCommerce: WC-C-075 Shipping zones, methods and classes (core)

Basis: SH-C-114 platform_terms "Shipping and delivery"; platform_terms "profiles/create" | SA-C-142 platform_terms "Shipping & delivery"; platform_terms "Shipping Zones"; inventory SA-I-2028 "shipping-profiles"; platform_terms "تخصيص تسعيرة الشحن" | WC-C-075 platform_terms "Shipping zones"; platform_terms "Shipping settings"

### Where it lives

- **Shopify**
  - `shipping`: "title": "Shipping and delivery" (SH-S-1491)
  - `Shipping and fulfillment`: "label": "Shipping and fulfillment" (SH-S-0786)
  - `delivery-profile:create`: "section":"Shipping","path":"profiles/create","title":{"value":"Create shipping profile"} (SH-S-7132)
- **Salla**
  - `Shipping & delivery`: {"position": 16, "kind": "link", "text": "Shipping & delivery", "href": "/shipping"} (SA-S-1692)
  - `Shipping settings`: {"position": 98, "kind": "link", "text": "Shipping settings", "href": "/?settings=%2Fshipping", "parent": 0, "list": 8} (SA-S-1868)
  - `@salla.sa/ui-merchant-shipping`: {"id": 1728402729452, "name": "@salla.sa/ui-merchant-shipping", "Prod": {}, "env": "prod", "path": "/^(/shipping\|/payments/taxes)(/.*)?$/", "position": 13} (SA-S-3542)
  - `Shipping Zones`: "id": 841809, "name": "Shipping Zones", "key": "apiDetailFolder.841809", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1046)
- **WooCommerce**
  - `Shipping`: $this->label = __( 'Shipping', 'woocommerce' ); (WC-S-0004)
  - `Shipping > Shipping zones`: '' => __( 'Shipping zones', 'woocommerce' ), (WC-S-0017)
  - `Shipping > Shipping settings`: 'options' => __( 'Shipping settings', 'woocommerce' ), (WC-S-0018)
  - `Shipping > Classes`: 'classes' => __( 'Classes', 'woocommerce' ), (WC-S-0019)
  - `Flat rate (flat_rate)`: $this->method_title = __( 'Flat rate', 'woocommerce' ); (WC-S-0284)
  - `Free shipping (free_shipping)`: $this->method_title = __( 'Free shipping', 'woocommerce' ); (WC-S-0285)
  - and 10 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `shipping:eligibility`: "eligibility":{"permissions":["MANAGE_DELIVERY_SETTINGS"],"entitlements":["shipping.settingsAccess"]} (SH-S-5260)
  - `shipping-calculator`: "eligibility":{"oneOf":[{"permissions":["MANAGE_DELIVERY_SETTINGS"]},{"permissions":["ORDERS"]}]} (SH-S-5262)
  - `entitlements.shipping.settingsAccess`: {"set": 0, "section": "entitlements", "key": "shipping", "value": {"settingsAccess": true, "labels": true, "__typename": "ShippingType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5842)
- **Salla**
  - `إتاحة الشحن المجاني`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "إتاحة الشحن المجاني", "description": null, "icon": null, "icon_color": null, "icon_background [cut] [scope: plan: سلة بلس] (SA-S-2021)
  - `تخصيص تسعيرة الشحن`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "تخصيص تسعيرة الشحن", "description": null, "icon": null, "icon_color": null, "icon_background" [cut] [scope: plan: سلة بلس] (SA-S-2023)
  - `قيود الشحن والتوصيل`: "sub_features": [{"parent_code": "alshhn-oaltosyl", "title": "قيود الشحن والتوصيل", "description": null, "icon": null, "icon_color": null, "icon_background": nu [cut] [scope: plan: سلة برو] (SA-S-2112)
  - `قيود الشحن والتوصيل`: "sub_features": []}, {"title": "قيود الشحن والتوصيل", "description": "قيود الشحن والتوصيل", "icon": null, "code": "kyod-alshhn-oaltosyl", "icon_color": null, "i [cut] [scope: plan: سلة برو] (SA-S-2146)
  - `shipping_options_management`: "label": "store setting purchase from salla store"}, {"id": 1182063247, "name": "shipping_options_management", "label": "shipping options management"}, {"id": 2 [cut] (SA-S-2392)
  - `shipping_rules_management`: "label": "quick donation management"}, {"id": 1365099159, "name": "shipping_rules_management", "label": "shipping rules management"}, {"id": 591061392, "name":  [cut] (SA-S-2400)
  - and 13 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `store_address`: 'desc' => __( 'This is where your business is located. Tax rates and shipping rates will use this address.', 'woocommerce' ), (WC-S-0599)
  - `woocommerce_enable_shipping_calc`: 'id' => 'woocommerce_enable_shipping_calc', 'default' => 'yes', 'type' => 'checkbox', (WC-S-5411)

### Who is legally responsible

- **Shopify**
  - `4. Your Responsibilities`: This includes, but is not limited to, authorizing the charge to the customer in respect of the customer's purchase, determining and collecting taxes, refunds, r [cut] (SH-S-0012)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_shipping`: The webhook topic for `shipping_addresses/create` events. Occurs whenever a shipping address is created. Requires the `read_shipping` scope. (SH-S-6114)
  - `read_shipping`: The webhook topic for `shipping_addresses/update` events. Occurs whenever a shipping address is updated. Requires the `read_shipping` scope. (SH-S-6115)
  - `read_shipping`: Requires `read_shipping` access scope or `read_orders` access scope. (SH-S-6117)
  - `write_shipping`: To manage delivery profiles on your selling plans, your app needs the `read_shipping` and `write_shipping` [access scopes](https://shopify.dev/docs/api/usage/ac [cut] (SH-S-6295)
  - `write_shipping`: "text": "write_shipping" (SH-S-1067)
  - `dev.ucp.shopping.fulfillment`: "dev.ucp.shopping.fulfillment" [scope: store capture-plus (its UCP profile)] (SH-S-2531)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Shipping Zones`: "id": 841809, "name": "Shipping Zones", "key": "apiDetailFolder.841809", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplay [cut] (SA-S-1046)
  - `shippings`: {"id": 16, "slug": "shippings", "icon": "sicon-shipping-fast", "options": [{"item": "read", "name": "read", "disabled": true}, {"item": "read_write", "name": "r [cut] (SA-S-1559)
  - `shipping.zone.created`: {"id": 526855568, "slug": "shipping.zone.created", "url": "https://docs.salla.dev/doc-433806#shipping-zone-webhook-events-model", "order": 0, "is_enabled": true [cut] (SA-S-1631)
  - `shipping.zone.updated`: {"id": 845294605, "slug": "shipping.zone.updated", "url": "https://docs.salla.dev/doc-433806#shipping-zone-webhook-events-model", "order": 0, "is_enabled": true [cut] (SA-S-1632)
- **WooCommerce**
  - `wc/v3 > product-shipping-classes`: 'product-shipping-classes' => 'WC_REST_Product_Shipping_Classes_Controller', (WC-S-0098)
  - `wc/v3 > shipping-zones`: 'shipping-zones' => 'WC_REST_Shipping_Zones_Controller', (WC-S-0113)
  - `wc/v3 > shipping-zone-locations`: 'shipping-zone-locations' => 'WC_REST_Shipping_Zone_Locations_Controller', (WC-S-0114)
  - `wc/v3 > shipping-zone-methods`: 'shipping-zone-methods' => 'WC_REST_Shipping_Zone_Methods_Controller', (WC-S-0115)
  - `wc/v3 > shipping-methods`: 'shipping-methods' => 'WC_REST_Shipping_Methods_Controller', (WC-S-0122)
  - `wc/v4 > shipping-zones`: 'shipping-zones' => ShippingZonesController::class, (WC-S-0135)
  - and 10 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

## M-046

Shopify: SH-C-121 Local pickup and local delivery; Salla: SA-C-148 Branch pickup and branch delivery zones

Basis: SH-C-121 platform_terms "Local pick up"; platform_terms "Local delivery" | SA-C-148 platform_terms "إتاحة الاستلام من الفرع"; platform_terms "Branch Delivery Zones"

### Where it lives

- **Shopify**
  - `local-delivery:list`: "section":"Shipping","path":"local_deliveries","title":{"value":"Local delivery"} (SH-S-7136)
  - `pickup-in-store:list`: "section":"Shipping","path":"pickup_in_store","title":{"value":"Pickup in store"} (SH-S-7137)
- **Salla**
  - `Branch Delivery Zones`: "id": 5101844, "name": "Branch Delivery Zones", "key": "apiDetailFolder.5101844", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderConten [cut] (SA-S-1071)

### Who decides

- **Shopify**
  - `shipping:eligibility`: "eligibility":{"permissions":["MANAGE_DELIVERY_SETTINGS"],"entitlements":["shipping.settingsAccess"]} (SH-S-5260)
  - `entitlements.shipping.settingsAccess`: {"set": 0, "section": "entitlements", "key": "shipping", "value": {"settingsAccess": true, "labels": true, "__typename": "ShippingType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5842)
- **Salla**
  - `إتاحة الاستلام من الفرع`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "إتاحة الاستلام من الفرع", "description": null, "icon": null, "icon_color": null, "icon_backgr [cut] [scope: plan: سلة بلس] (SA-S-2029)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `unauthenticated_read_product_pickup_locations`: Requires `unauthenticated_read_product_pickup_locations` access scope. (SH-S-6158)
  - `unauthenticated_read_product_pickup_locations`: * Your Headless channel or custom app has the `unauthenticated_read_product_pickup_locations` [access scopes](https://shopify.dev/docs/api/usage/access-scopes#u [cut] (SH-S-6159)
  - `fulfillment_orders/line_items_prepared_for_pickup`: "value": "fulfillment_orders/line_items_prepared_for_pickup" (SH-S-1241)
  - `fulfillment_orders/line_items_prepared_for_local_delivery`: "value": "fulfillment_orders/line_items_prepared_for_local_delivery" (SH-S-1240)
- **Salla**
  - `Branch Delivery Zones`: "id": 5101844, "name": "Branch Delivery Zones", "key": "apiDetailFolder.5101844", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderConten [cut] (SA-S-1071)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)

## M-047

Shopify: SH-C-116 Shopify Shipping (shipping labels); Salla: SA-C-140 Salla shipping labels with integrated carriers (بوليصات سلة); WooCommerce: WC-C-060 WooCommerce Shipping (labels and carrier rates)

Basis: SH-C-116 platform_terms "Shipping labels"; platform_terms "Buy and print shipping labels" | SA-C-140 platform_terms "Shipping label cost deduction"; platform_terms "بوليصات سلة" | WC-C-060 platform_terms "WooCommerce Shipping"; statement WC-S-0655 "Our shipping Services allow you to check shipping rates or buy shipping labels"

### Where it lives

- **Shopify**
  - `shippingLabel:parent`: "path":"shipping_labels" (SH-S-5263)
  - `help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels.md`: You can buy, print, and manage discounted shipping labels from Shopify supported carriers directly in your Shopify admin. (SH-S-0717)
  - `Shipping labels`: "text": "Shipping labels" (SH-S-1537)
  - `9.4 Shopify Shipping`: You can purchase shipping labels from within your Shopify administrative console ("Shopify Shipping") for delivery of goods purchased from you. Your use of Shop [cut] (SH-S-0050)
- **Salla**
  - `Shipping & delivery`: {"position": 16, "kind": "link", "text": "Shipping & delivery", "href": "/shipping"} (SA-S-1692)
  - `Shipping label cost deduction`: "orders/shipping-label-deduction":"Shipping label cost deduction" (SA-S-1741)
  - `Shipping & delivery`: {"position": 97, "kind": "link", "text": "Shipping & delivery", "href": "/shipping", "parent": 0, "list": 8} (SA-S-1867)
  - `@salla.sa/ui-merchant-shipping`: {"id": 1728402729452, "name": "@salla.sa/ui-merchant-shipping", "Prod": {}, "env": "prod", "path": "/^(/shipping\|/payments/taxes)(/.*)?$/", "position": 13} (SA-S-3542)
- **WooCommerce**
  - `WooCommerce Shipping`: With WooCommerce Shipping, you can create ready-to-print labels for UPS®, USPS, DHL Express, and FedEx directly in WooCommerce and use discounted commercial rat [cut] (WC-S-0904)

### Who decides

- **Shopify**
  - `shippingLabel:parent`: "eligibility":{"entitlements":["shipping.labels"]} (SH-S-5264)
  - `shippingLabel:index`: "eligibility":{"permissions":["FULFILL_AND_SHIP_ORDERS"]} (SH-S-5265)
  - `Getting started with shipping labels`: Eligibility varies by carrier and country. (SH-S-0718)
  - `Getting started with shipping labels`: Discounts for shipping labels vary based on your Shopify plan. (SH-S-0719)
  - `A. Shopify Shipping`: Depending on your location, Shopify Shipping provides you with access to purchase third-party shipping services (SH-S-0609)
  - `entitlements.shipping.labels`: {"set": 0, "section": "entitlements", "key": "shipping", "value": {"settingsAccess": true, "labels": true, "__typename": "ShippingType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5842)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `بوليصات شحن سلة المُخفضة`: "extra_icons": null}, {"parent_code": "mzaya-asasy", "title": "بوليصات شحن سلة المُخفضة", "description": null, "icon": null, "icon_color": null, "icon_backgroun [cut] [scope: plan: سلة بلس] (SA-S-1951)
  - `بوليصات شحن سلة المُخفضة`: "sub_features": [{"parent_code": "alshhn-oaltosyl", "title": "بوليصات شحن سلة المُخفضة", "description": null, "icon": null, "icon_color": null, "icon_background [cut] [scope: plan: سلة بلس] (SA-S-2018)
  - `الشحن العادي عبر سمسا، البريد السعودي، DHL Express، أي مكان، J&T Express`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "الشحن العادي عبر سمسا، البريد السعودي، DHL Express، أي مكان، J&T Express", "description": nul [cut] [scope: plan: سلة بلس] (SA-S-2019)
  - `الشحن الاقتصادي عبر مندوبي، ريدبوكس، سمسا (استلام وتسليم من الفرع)`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "الشحن الاقتصادي عبر مندوبي، ريدبوكس، سمسا (استلام وتسليم من الفرع)", "description": null, "ic [cut] [scope: plan: سلة بلس] (SA-S-2020)
  - `مستويات تسعير البوليصات`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "مستويات تسعير البوليصات", "description": null, "icon": null, "icon_color": null, "icon_backgr [cut] [scope: plan: سلة بلس] (SA-S-2022)
  - `حاسبة تكلفة الشحن`: "extra_icons": null}, {"parent_code": "alshhn-oaltosyl", "title": "حاسبة تكلفة الشحن", "description": null, "icon": null, "icon_color": null, "icon_background": [cut] [scope: plan: سلة بلس] (SA-S-2024)
  - and 3 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `WooCommerce Shipping`: It does not provide live shipping rates at checkout. (WC-S-0906)
  - `WooCommerce Shipping`: WooCommerce Shipping is currently available to stores based in the United States, including U.S. territories, that use U.S. dollars. (WC-S-0905)
  - `readme.txt: ALL THE TOOLS YOU NEED TO SELL`: (U.S.-only) (WC-S-0592)

### Who is legally responsible

- **Shopify**
  - `www.shopify.com/legal/terms-shipping-global`: “Shopify” means the applicable Shopify Contracting Party depending on the billing address of your Store (SH-S-0608)
  - `A. Shopify Shipping`: Popout, Inc., d.b.a Shippo (“Shippo”) is a Third-Party Integrator that allows for the purchase of Third-Party Shipping Services from certain Third-Party Shippin [cut] (SH-S-0610)
  - `A. Shopify Shipping`: Auctane, Inc. (“Auctane”) is a Third-Party Integrator (SH-S-0611)
  - `A. Shopify Shipping`: Easyship Fulfillment Services Ltd. (“Easyship”) is a Third-Party Integrator (SH-S-0612)
  - `B. Your Responsibilities`: Shopify serves only as an intermediary between you and the applicable Third-Party Integrator or Third-Party Shipping Provider, allowing you to purchase postage  [cut] (SH-S-0613)
  - `B. Your Responsibilities`: Shopify is not responsible in any event for picking up, transporting, delivering, or otherwise handling your shipments, or providing customer service to your cu [cut] (SH-S-0614)
- **Salla**
  - `إصدار بوليصات بأقل تكلفة`: تقدم سلة لتجارها خيار إصدار مجموعة من البوليصات بدفع مباشر من خلال منصة سلة بدون الحاجة للتعاقد مع شركة الشحن أو بوابات الدفع بشكل فردي ومنفصل، وبذلك أصبحت البو [cut] (SA-S-5059)
  - `actions_bar.create_shipping_policy.summary.postpaid.terms_cancellation_text`: تخضع البوليصات المُصدرة لسياسات الإلغاء والاسترجاع الخاصة بشركات الشحن المعتمدة. [scope: الدفع الآجل لبوليصات سلة] (SA-S-5060)
  - `actions_bar.create_shipping_policy.summary.postpaid.terms_payment_dates_text`: يلتزم التاجر بسداد المبالغ المستحقة في موعدها لتجنُّب إيقاف خدمة الدفع الآجل أو بعض مزايا المتجر. [scope: الدفع الآجل لبوليصات سلة] (SA-S-5061)
- **WooCommerce**
  - `8. j. More on Shipping Services Specifically`: We’re only an intermediary between you and these third parties; we aren’t involved in any way with your product or its shipment. (WC-S-0483)

### How it meets the rest

- **Shopify**
  - `9.4 Shopify Shipping`: You can purchase shipping labels from within your Shopify administrative console ("Shopify Shipping") for delivery of goods purchased from you. Your use of Shop [cut] (SH-S-0050)
  - `D. Fees`: The Shipping Fees will be added to your next Shopify invoice, which will appear on the account page in your Shopify Admin. (SH-S-0619)
- **Salla**
  - `أولاً: تعريف محفظة متجرك على سلة`: رصيد المتجر: يُستخدم لتجديد باقة المتجر تلقائياً، بالإضافة للشراء من متجر سلة وإصدار البوليصات وغير ذلك. (SA-S-0089)
- **WooCommerce**
  - `8. j. More on Shipping Services Specifically`: Our shipping Services allow you to check shipping rates or buy shipping labels from certain mailing services, like DHL, FedEx, UPS, USPS, and Canada Post. (WC-S-0655)
  - `WooCommerce: Shipping Rates and Labels`: are passed to our partners, EasyPost, and the respective mailing service, such as USPS or Canada Post. This is done via Automattic’s servers. (WC-S-0958)
  - `WooCommerce Shipping`: WooCommerce Shipping requires Jetpack to connect with other services and provide live shipping rates, discounted labels, and other features. (WC-S-0567)
  - `WooCommerce Shipping`: With WooCommerce Shipping, you can create ready-to-print labels for UPS®, USPS, DHL Express, and FedEx directly in WooCommerce and use discounted commercial rat [cut] (WC-S-0904)
  - `WooCommerce: Shipping Rates and Labels`: Regarding data handling, we validate (but do not store) the data you send to us and then pass that data on to our partners. (WC-S-0959)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `بوليصات الشحن`: لذلك قدمت سلة حلولها بخدمة بوليصات الشحن بأسعار شحن ثابتة وأقل تكلفة على جيب التاجر، بالإضافة إلى تقديم شركات شحن متعددة وموسعة. (SA-S-5062)
- **WooCommerce**: gap (searched, not found)

## M-048

Shopify: SH-C-118 Fulfillment orders and fulfillments; WooCommerce: WC-C-092 Order fulfillments and shipping providers

Basis: SH-C-118 platform_terms "fulfillments/create"; platform_terms "Fulfill and ship" | WC-C-092 platform_terms "Order Fulfillments"; inventory WC-I-0131 "wc/v4 > fulfillments"

### Where it lives

- **Shopify**
  - `FulfillmentOrder`: "label": "FulfillmentOrder" (SH-S-0921)
  - `batches:index`: "section":"Batches","path":"batches" (SH-S-7134)
- **WooCommerce**
  - `Shipping > Shipping providers`: $sections['fulfillment-providers'] = __( 'Shipping providers', 'woocommerce' ); (WC-S-0020)
  - `Fulfillment created (WC_Email_Customer_Fulfillment_Created)`: $this->title = __( 'Fulfillment created', 'woocommerce' ); (WC-S-0310)
  - `Fulfillment updated (WC_Email_Customer_Fulfillment_Updated)`: $this->title = __( 'Fulfillment updated', 'woocommerce' ); (WC-S-0311)
  - `Fulfillment deleted (WC_Email_Customer_Fulfillment_Deleted)`: $this->title = __( 'Fulfillment deleted', 'woocommerce' ); (WC-S-0312)

### Who decides

- **Shopify**
  - `write_assigned_fulfillment_orders`: Requires `write_assigned_fulfillment_orders` access scope, `write_merchant_managed_fulfillment_orders` access scope or `write_third_party_fulfillment_orders` ac [cut] (SH-S-6168)
  - `write_assigned_fulfillment_orders`: Requires `write_assigned_fulfillment_orders` access scope. Also: The user must have fulfill\_and\_ship\_orders permission. (SH-S-6169)
  - `write_assigned_fulfillment_orders`: Requires `write_assigned_fulfillment_orders` access scope. Also: The user must have `fulfill_and_ship_orders` permission. (SH-S-6170)
  - `write_merchant_managed_fulfillment_orders`: Requires `write_merchant_managed_fulfillment_orders` access scope or `write_third_party_fulfillment_orders` access scope. Also: The user must have fulfill\_and\ [cut] (SH-S-6234)
  - `write_merchant_managed_fulfillment_orders`: Requires `write_merchant_managed_fulfillment_orders` access scope. Also: The user must have fulfill\_and\_ship\_orders permission. (SH-S-6235)
  - `write_third_party_fulfillment_orders`: Requires `write_merchant_managed_fulfillment_orders` access scope, `write_third_party_fulfillment_orders` access scope or `write_marketplace_fulfillment_orders` [cut] (SH-S-6302)
  - and 5 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `fulfillments`: 'Enable the Order Fulfillments feature to manage order fulfillment and shipping.', (WC-S-0938)
  - `fulfillments`: 'enabled_by_default' => false, 'disable_ui' => true, (WC-S-5444)

### Who is legally responsible

- **Shopify**
  - `4. Your Responsibilities`: This includes, but is not limited to, authorizing the charge to the customer in respect of the customer's purchase, determining and collecting taxes, refunds, r [cut] (SH-S-0012)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_assigned_fulfillment_orders`: The API client must be granted the `read_assigned_fulfillment_orders` access scope to access the assigned fulfillment orders. (SH-S-5933)
  - `read_assigned_fulfillment_orders`: * The `read_assigned_fulfillment_orders` and `write_assigned_fulfillment_orders` access scopes are intended for fulfillment services. These scopes grant access  [cut] (SH-S-5934)
  - `read_assigned_fulfillment_orders`: The app must have the `read_assigned_fulfillment_orders` [access scope](https://shopify.dev/docs/api/usage/access-scopes) to be able to retrieve the fulfillment [cut] (SH-S-5935)
  - `read_assigned_fulfillment_orders`: Requires `read_orders` access scope, `read_assigned_fulfillment_orders` access scope, `read_merchant_managed_fulfillment_orders` access scope, `read_third_party [cut] (SH-S-5936)
  - `read_assigned_fulfillment_orders`: Requires `read_assigned_fulfillment_orders` access scope, `read_merchant_managed_fulfillment_orders` access scope, `read_third_party_fulfillment_orders` access  [cut] (SH-S-5937)
  - `read_marketplace_fulfillment_orders`: Requires `read_orders` access scope, `read_marketplace_orders` access scope, `read_assigned_fulfillment_orders` access scope, `read_merchant_managed_fulfillment [cut] (SH-S-6030)
  - and 9 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `wc/v4 > fulfillments`: 'fulfillments' => FulfillmentsController::class, (WC-S-0131)
  - `Order Fulfillment`: This system includes both a user-friendly interface and a robust API for integration with your favorite shipping tools and providers. (WC-S-0897)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-049

Shopify: SH-C-125 Delivery promises; Salla: SA-C-147 Delivery promises

Basis: SH-C-125 platform_terms "read_delivery_promises" | SA-C-147 platform_terms "Shipping Delivery Promises"; platform_terms "delivery-promises"

### Where it lives

- **Shopify**
  - `shipping:list:shop-promise-examples`: "section":"Shipping","path":"shop-promise-examples" (SH-S-7139)
- **Salla**
  - `Shipping Delivery Promises`: "id": 7639454, "name": "Shipping Delivery Promises", "key": "apiDetailFolder.7639454", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderC [cut] (SA-S-1052)

### Who decides

- **Shopify**
  - `shipping:list:shop-promise-examples`: "eligibility":{"betas":["9ed93472"]} (SH-S-5033)
- **Salla**
  - `delivery-promises`: {"position": 86, "name": "delivery-promises", "value": {"enabled": false, "released": false, "plans": ["pro", "special"], "countries": [], "type": "feature"}} [scope: plans: pro, special] (SA-S-3047)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `read_delivery_promises`: Requires `read_delivery_promises` access scope. (SH-S-5975)
  - `write_delivery_promises`: Requires `write_delivery_promises` access scope. (SH-S-6187)
  - `write_delivery_promises`: `write_delivery_promises` (SH-S-1121)
  - `delivery_promise_settings/update`: "value": "delivery_promise_settings/update" (SH-S-1208)
  - `read_shipping`: The webhook topic for `delivery_promise_settings/update` events. Occurs when a promise setting is updated. Requires the `read_shipping` scope. (SH-S-6113)
  - `read_shipping`: Requires `read_shipping` access scope or `read_shop_promise_program` access scope. (SH-S-6116)
- **Salla**
  - `Shipping Delivery Promises`: "id": 7639454, "name": "Shipping Delivery Promises", "key": "apiDetailFolder.7639454", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderC [cut] (SA-S-1052)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)

## M-050

Salla: SA-C-070 Coupons (Coupons / الكوبونات); WooCommerce: WC-C-074 Coupons and discounts

Basis: SA-C-070 platform_terms "Coupons"; platform_terms "coupon.applied"; concern "Coupons / الكوبونات" | WC-C-074 platform_terms "Coupons"; inventory WC-I-0254 "coupon.created"

### Where it lives

- **Salla**
  - `Marketing`: {"position": 18, "kind": "link", "text": "Marketing", "href": "/coupons"} (SA-S-1694)
  - `Multiple coupons`: "coupons/multiple-coupons":"Multiple coupons" (SA-S-1707)
  - `Coupons`: {"position": 45, "kind": "link", "text": "Coupons", "href": "/marketing/coupons", "parent": 0, "list": 3} (SA-S-1815)
  - `@salla.sa/ui-merchant-coupons`: {"id": 1766475628818, "name": "@salla.sa/ui-merchant-coupons", "Prod": {}, "env": "prod", "path": "/marketing/coupons", "position": 54} (SA-S-3583)
  - `Coupons`: "id": 841818, "name": "Coupons", "key": "apiDetailFolder.841818", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSett [cut] (SA-S-1038)
- **WooCommerce**
  - `WooCommerce > Coupons`: __( 'Coupons', 'woocommerce' ), (WC-S-0048)
  - `Marketing > Coupons`: 'menu_name' => _x( 'Coupons', 'Admin menu name', 'woocommerce' ), (WC-S-0062)
  - `Analytics > Coupons`: 'title' => __( 'Coupons', 'woocommerce' ), (WC-S-0071)

### Who decides

- **Salla**
  - `كوبونات التخفيض`: "sub_features": [{"parent_code": "adoat-altsoyk", "title": "كوبونات التخفيض", "description": null, "icon": null, "icon_color": null, "icon_background": null, "e [cut] [scope: plan: سلة بلس] (SA-S-2001)
  - `إنشاء مجموعة كوبونات`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "إنشاء مجموعة كوبونات", "description": null, "icon": null, "icon_color": null, "icon_background" [cut] [scope: plan: سلة بلس] (SA-S-2008)
  - `كوبونات محلي`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "كوبونات محلي", "description": null, "icon": null, "icon_color": null, "icon_background": null,  [cut] [scope: plan: سلة بلس] (SA-S-2009)
  - `إطلاق عروض وخصومات`: "sub_features": []}, {"title": "إطلاق عروض وخصومات", "description": "اجذب المزيد من العملاء عبر تقديم خصومات وعروض خاصة تُطبق تلقائيًا عند الطلب، مع التحكم بنوع [cut] [scope: plan: سلة بلس] (SA-S-2103)
  - `كوبونات تسويقية`: "sub_features": [{"parent_code": "adoat-altsoyk", "title": "كوبونات تسويقية", "description": null, "icon": null, "icon_color": null, "icon_background": null, "e [cut] [scope: plan: سلة برو] (SA-S-2108)
  - `coupon_browse`: "permissions": [{"id": 1209997307, "name": "coupon_browse", "label": "coupon browse"}, {"id": 1041462660, "name": "coupon_management", "label": "coupon manageme [cut] (SA-S-2348)
  - and 15 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `woocommerce_enable_coupons`: 'id' => 'woocommerce_enable_coupons', 'default' => 'yes', 'type' => 'checkbox', (WC-S-5409)
  - `shop_coupon (post type)`: 'capability_type' => 'shop_coupon', 'map_meta_cap' => true, (WC-S-5410)

### Who is legally responsible

- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Salla**
  - `Coupons`: "id": 841818, "name": "Coupons", "key": "apiDetailFolder.841818", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSett [cut] (SA-S-1038)
  - `marketing`: {"id": 15, "slug": "marketing", "icon": "sicon-megaphone", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read [cut] (SA-S-1560)
  - `order.coupon.updated`: {"id": 257821489, "slug": "order.coupon.updated", "url": "https://docs.salla.dev/doc-433804#orders-webhook-events-model", "order": 0, "is_enabled": true, "name" [cut] (SA-S-1573)
  - `coupon.applied`: {"id": 380443386, "slug": "coupon.applied", "url": "https://docs.salla.dev/doc-433812#coupon-applied-webhook-event-model", "order": 0, "is_enabled": true, "name [cut] (SA-S-1623)
- **WooCommerce**
  - `wc/v3 > coupons`: 'coupons' => 'WC_REST_Coupons_Controller', (WC-S-0086)
  - `wc/store/v1 > /cart/apply-coupon`: const IDENTIFIER = 'cart-apply-coupon'; (WC-S-0151)
  - `wc/store/v1 > /cart/coupons`: const IDENTIFIER = 'cart-coupons'; (WC-S-0152)
  - `wc/store/v1 > /cart/coupons/(?P<code>[\w-]+)`: const IDENTIFIER = 'cart-coupons-by-code'; (WC-S-0153)
  - `wc/store/v1 > /cart/remove-coupon`: const IDENTIFIER = 'cart-remove-coupon'; (WC-S-0157)
  - `wc-analytics > Coupons`: 'Automattic\WooCommerce\Admin\API\Coupons', (WC-S-0208)
  - and 7 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-051

Shopify: SH-C-129 Marketing campaigns, automations and marketing activities; Salla: SA-C-075 Marketing campaigns and marketing calendar (Campaigns; SMS and push campaigns); WooCommerce: WC-C-084 Marketing hub (channels, campaigns, recommendations), WC-C-110 Marketing extensions (advertising, automation, CRM, reporting, sales channels, SEO, email, social)

Basis: SH-C-129 platform_terms "Marketing"; platform_terms "Campaigns"; inventory SH-I-1826 "Marketing apps" | SA-C-075 platform_terms "Marketing"; platform_terms "Campaigns"; platform_terms "حملات تسويقية عبر الرسائل النصية وإشعارات التطبيق" | WC-C-084 platform_terms "Marketing"; inventory WC-I-0190 "marketing/campaigns" | WC-C-110 platform_terms "Marketing"

### Where it lives

- **Shopify**
  - `growth`: "path":"growth" (SH-S-5173)
  - `marketing`: "path":"marketing" (SH-S-5176)
  - `Growth`: "text": "Growth" (SH-S-1518)
  - `Campaigns`: "text": "Campaigns" (SH-S-1521)
  - `Marketing apps`: "h1": "Marketing apps" (SH-S-2590)
- **Salla**
  - `Marketing`: {"id": 1617628556, "name": "Marketing", "type": "app", "position": 9} (SA-S-1196)
  - `Marketing`: {"id": 1, "slug": "marketing", "icon": "rocket", "color": "red", "type": "app", "featured": true, "order": 3, "hidden": false, "name": {"ar": "التسويق", "en": " [cut] (SA-S-1223)
  - `Campaigns`: {"position": 48, "kind": "link", "text": "Campaigns", "href": "/marketing/campaign/retargeting", "parent": 0, "list": 3} (SA-S-1818)
  - `Marketing calendar`: {"position": 49, "kind": "link", "text": "Marketing calendar", "href": "/marketing/calendar", "parent": 0, "list": 3} (SA-S-1819)
  - `@salla.sa/ui-merchant-marketing-campaign`: {"id": 1728336477774, "name": "@salla.sa/ui-merchant-marketing-campaign", "Prod": {}, "env": "prod", "path": "/^/marketing/(campaign\|campaigns\|retargeting\|seo\|b [cut] (SA-S-3535)
- **WooCommerce**
  - `Marketing`: 'title' => 'Marketing', (WC-S-0060)
  - `Marketing > Overview`: 'title' => __( 'Overview', 'woocommerce' ), (WC-S-0061)
  - `Grow your business`: return __( 'Grow your business', 'woocommerce' ); (WC-S-0424)
  - `Extensions > Marketing`: Marketing (WC-S-0705)
  - `Extensions > Marketing > Advertising and promotions`: Advertising and promotions (WC-S-0755)
  - `Extensions > Marketing > Automation`: Automation (WC-S-0756)
  - and 6 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `growth`: "eligibility":{"permissions":["MARKETING_SECTION"],"entitlements":["storefront.enabled"]} (SH-S-5174)
  - `growth:channels`: "eligibility":{"permissions":["REPORTS"]} (SH-S-5032)
  - `growth:integrated-campaigns`: "eligibility":{"permissions":["VIEW_MARKETING_INTEGRATED_CAMPAIGNS","REPORTS"]} (SH-S-5175)
  - `entitlements.storefront.enabled`: {"set": 0, "section": "entitlements", "key": "storefront", "value": {"enabled": true, "__typename": "StorefrontType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5364)
  - `Create marketing automations`: {"kind": "row", "section": 1, "position": 52, "cells": [{"tag": "th", "text": "Create marketing automations", "scope": "row"}, {"tag": "td", "text": "Included"} [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7040)
- **Salla**
  - `حملات تسويقية عبر الرسائل النصية وإشعارات التطبيق`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "حملات تسويقية عبر الرسائل النصية وإشعارات التطبيق", "description": null, "icon": null, "icon_co [cut] [scope: plan: سلة بلس] (SA-S-2010)
  - `الجدول الزمني للتسويق`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "الجدول الزمني للتسويق", "description": null, "icon": null, "icon_color": null, "icon_background [cut] [scope: plan: سلة بلس] (SA-S-2013)
  - `تسويق واسع عبر واتساب وتويتر وانستجرام وجوجل`: "sub_features": []}, {"title": "تسويق واسع عبر واتساب وتويتر وانستجرام وجوجل", "description": "ضاعف مبيعات متجرك عبر إنشاء رابط أو كود تسويقي خاص للمسوّق بالعمو [cut] [scope: plan: سلة برو] (SA-S-2151)
  - `campaign_browse`: "label": "coupon management"}, {"id": 1061081537, "name": "campaign_browse", "label": "campaign browse"}, {"id": 200905861, "name": "campaign_management", "labe [cut] (SA-S-2350)
  - `campaign_management`: "label": "campaign browse"}, {"id": 200905861, "name": "campaign_management", "label": "campaign management"}, {"id": 576560079, "name": "forget_cart_browse", " [cut] (SA-S-2351)
  - `campaign_browse`: "en": "coupon management"}}, {"id": 1061081537, "key": "campaign_browse", "name": {"ar": "الاطلاع على الحملات التسويقية", "en": "campaign browse"}}, {"id": 2009 [cut] (SA-S-2567)
  - and 7 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `woocommerce-marketing`: 'id' => 'woocommerce-marketing', 'title' => 'Marketing', 'capability' => 'manage_woocommerce', (WC-S-5425)
  - `General product information`: Since these are required fields for any product to be approved in Google Merchant Center, Google for WooCommerce will not sync WooCommerce products that do not  [cut] [scope: Google for WooCommerce] (WC-S-5492 WC-S-5493)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_marketing_events`: Requires `read_marketing_events` access scope. (SH-S-6029)
  - `write_marketing_events`: Requires `write_marketing_events` access scope. (SH-S-6226)
  - `write_marketing_events`: "text": "write_marketing_events" (SH-S-1016)
  - `read_marketing_integrated_campaigns`: "text": "read_marketing_integrated_campaigns" (SH-S-1014)
- **Salla**
  - `marketing.campaign.broadcast`: Triggered when a marketing campaign is broadcast to customers. (SA-S-1673)
- **WooCommerce**
  - `wc-admin > marketing (Marketing)`: 'Automattic\WooCommerce\Admin\API\Marketing', (WC-S-0186)
  - `wc-admin > marketing/overview (MarketingOverview)`: 'Automattic\WooCommerce\Admin\API\MarketingOverview', (WC-S-0187)
  - `wc-admin > marketing/recommendations (MarketingRecommendations)`: 'Automattic\WooCommerce\Admin\API\MarketingRecommendations', (WC-S-0188)
  - `wc-admin > marketing/channels (MarketingChannels)`: 'Automattic\WooCommerce\Admin\API\MarketingChannels', (WC-S-0189)
  - `wc-admin > marketing/campaigns (MarketingCampaigns)`: 'Automattic\WooCommerce\Admin\API\MarketingCampaigns', (WC-S-0190)
  - `wc-admin > marketing/campaign-types (MarketingCampaignTypes)`: 'Automattic\WooCommerce\Admin\API\MarketingCampaignTypes', (WC-S-0191)
  - and 1 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

## M-052

Shopify: SH-C-130 Shopify Messaging (email and SMS); WooCommerce: WC-C-113 Email marketing (MailPoet, a Woo service)

Basis: SH-C-130 platform_terms "Create email campaigns"; inventory SH-I-2415 "9.7 Shopify Email"; inventory SH-I-1828 "Email marketing apps" | WC-C-113 platform_terms "MailPoet"; statement WC-S-0944 "MailPoet – Newsletters, Email Marketing, and Automation"; statement WC-S-0458 "Woo services include WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet"

### Where it lives

- **Shopify**
  - `email:create`: "path":"email/create" (SH-S-5157)
- **WooCommerce**
  - `Marketing`: MailPoet – Newsletters, Email Marketing, and Automation (WC-S-0944)
  - `What data does our sending service collect?`: If you have created an account with MailPoet to send emails or to purchase a plan, we collect the following data on our servers in the United States of America: [scope: MailPoet accounts created to send emails or to purchase a plan] (WC-S-5498)

### Who decides

- **Shopify**
  - `9.7 Shopify Email`: Shopify employs certain controls to scan the content of emails you deliver using the Email Services prior to delivery ("Content Scanning"). (SH-S-0055)
  - `Create email campaigns`: {"kind": "row", "section": 1, "position": 48, "cells": [{"tag": "th", "text": "Create email campaigns", "scope": "row"}, {"tag": "td", "text": "Included"}, {"ta [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7037)
  - `Pay-per-send SMS campaigns`: {"kind": "row", "section": 1, "position": 49, "cells": [{"tag": "th", "text": "Pay-per-send SMS campaigns", "scope": "row"}, {"tag": "td", "text": "Included"},  [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7038)
- **WooCommerce**
  - `MailPoet Plans and Limits Explained`: When you install the MailPoet plugin, you can use it for free up to 500 subscribers without creating an account with us or subscribing to any plans. (WC-S-5499)
  - `MailPoet > Settings > WooCommerce`: All customers will be automatically added to the WooCommerce Customers list by default, but their status as subscribers will depend on your settings in the Mail [cut] (WC-S-5500)

### Who is legally responsible

- **Shopify**
  - `9.7 Shopify Email`: Shopify's Email Services utilize Third Party Providers, including SendGrid (a Twilio Company). (SH-S-0054)
  - `9.5 SMS Messaging`: The SMS Services use third party providers, and your use is subject to Twilio's Acceptable Use Policy, which may be amended from time to time. (SH-S-0051)
- **WooCommerce**
  - `1. Who's Who: Woo Services`: Woo services include WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet, and other products or services available at WooCommerce.com. (WC-S-0458)
  - `1. Who's Who: Woo Services`: If you reside outside of the Designated Countries: WooCommerce, Inc. [scope: residents outside the Designated Countries] (WC-S-0459)
  - `1. Who's Who: Woo Services`: If you reside in the Designated Countries: WooCommerce Ireland Ltd. [scope: residents of the Designated Countries] (WC-S-0460)

### How it meets the rest

- **Shopify**
  - `9.7 Shopify Email`: Shopify's Email Services utilize Third Party Providers, including SendGrid (a Twilio Company). Your use of the Email Services is subject to Twilio's Acceptable  [cut] [scope: Email Services] (SH-S-7282)
- **WooCommerce**
  - `WooCommerce Customers list`: The WooCommerce Customers list is a list automatically created by MailPoet with all of your WooCommerce customers. (WC-S-5501)
  - `mailpoet_subscription_before_subscribe`: mailpoet_subscription_before_subscribe Action, which fires before a subscription is stored in the database. (WC-S-5502)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `Why You Shouldn't Send with Your Host`: We highly encourage our users to send with MailPoet's Sending Service or a third party email service provider instead of sending with their own website because: [cut] (WC-S-5503)

## M-053

Shopify: SH-C-131 Sales attribution; WooCommerce: WC-C-085 Order attribution

Basis: SH-C-131 platform_terms "Order Attribution Config" | WC-C-085 platform_terms "Order Attribution"

### Where it lives

- **Shopify**
  - `Attribution`: "text": "Attribution" (SH-S-1519)
  - `order_attribution_config`: "identifier": "order_attribution_config" (SH-S-2255)
- **WooCommerce**
  - `Order attribution (meta box)`: Within the order edit page for each new order, you'll find two meta boxes - "Order attribution" and "Customer history." (WC-S-5426)
  - `Principles of Order Attribution Tracking`: As no data is stored in WooCommerce unless an order is placed and all cookies of this feature expire with each session, this feature cannot be used to track you [cut] (WC-S-5427)

### Who decides

- **Shopify**
  - `order:mobile:conversion-summary`: "eligibility":{"permissions":["MARKETING_SECTION"]} (SH-S-5226)
- **WooCommerce**
  - `order_attribution`: 'Enable this feature to track and credit channels and campaigns that contribute to orders on your site', (WC-S-0935)
  - `wc_order_attribution_allow_tracking`: $allow_tracking = wc_bool_to_string( apply_filters( 'wc_order_attribution_allow_tracking', true ) ); (WC-S-5429)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `order_attribution_config`: "identifier": "order_attribution_config" (SH-S-2255)
- **WooCommerce**
  - `woocommerce_order_save_attribution_data`: do_action( 'woocommerce_order_save_attribution_data', $order, $params ); (WC-S-5428)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `Order Attribution Tracking`: It allows you to attribute orders to traffic sources, providing an understanding of the effectiveness of various marketing efforts. (WC-S-0890)

## M-054

Shopify: SH-C-135 Sales channels and publishing; Salla: SA-C-097 Sales channels settings (Sales channels / قنوات البيع)

Basis: SH-C-135 platform_terms "Sales channels"; inventory SH-I-0552 "product_publications/create" | SA-C-097 platform_terms "Sales channels"; platform_terms "product.publish"; concern "Sales channels / قنوات البيع"

### Where it lives

- **Shopify**
  - `Sales channels`: "text": "Sales channels" (SH-S-1534)
  - `sales_channels`: "title": "Sales channels" (SH-S-1496)
  - `What is a sales channel?`: A sales channel app connects a merchant's online store to surfaces outside Shopify. (SH-S-0699)
  - `What is a sales channel?`: Examples include traffic-driving channels like Google and Meta, and marketplaces like Amazon that have their own checkout. (SH-S-0700)
  - `channel_config`: "identifier": "channel_config" (SH-S-2254)
- **Salla**
  - `Sales channels`: {"position": 11, "kind": "link", "text": "Sales channels", "href": "/channels"} (SA-S-1687)
  - `@salla.sa/ui-merchant-channel`: {"id": 1730366475303, "name": "@salla.sa/ui-merchant-channel", "Prod": {}, "env": "prod", "path": "/^/channel/(?!vendors\|chat\|mahally\|sallapoint\|whatsapp\|mobile [cut] (SA-S-3551)

### Who decides

- **Shopify**
  - `write_publications`: Requires `write_publications` access scope. Also: The user must have a permission to publish a collection. (SH-S-6281)
  - `write_publications`: Requires `write_publications` access scope. Also: The user must have a permission to unpublish a collection. (SH-S-6282)
  - `write_publications`: Requires `write_publications` access scope. Also: The user must have a permission to publish a product. (SH-S-6283)
  - `write_publications`: Requires `write_publications` access scope. Also: The user must have a permission to unpublish a product. (SH-S-6284)
  - `write_publications`: Requires `write_publications` access scope. Also: The user must have a permission to create and edit catalogs. (SH-S-6285)
  - `When to create a sales channel?`: Only create a sales channel if you own and operate, or are contracted to represent, a distinct surface where merchants can promote or sell products outside Shop [cut] (SH-S-0701)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `الربط بمنصات التسوّق العالمية`: الربط بمنصات التسوّق العالمية [scope: plan: سلة سبيشل] (SA-S-2195)
  - `instagram-api`: {"position": 1, "name": "instagram-api", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-2962)
  - `brand-sales-channels`: {"position": 552, "name": "brand-sales-channels", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": " [cut] [scope: plans: plus, pro, special] (SA-S-3513)

### Who is legally responsible

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: Such Third Party Services are made available only as a convenience, and your purchase, access or use of any such Third Party Services is solely between you and  [cut] (SH-S-0058)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `read_publications`: The webhook topic for `channels/delete` events. Occurs whenever a channel is deleted. Requires the `read_publications` scope. (SH-S-6100)
  - `read_publications`: The webhook topic for `collection_publications/create` events. Occurs whenever a collection publication listing is created. Requires the `read_publications` sco [cut] (SH-S-6101)
  - `read_publications`: The webhook topic for `collection_publications/delete` events. Occurs whenever a collection publication listing is deleted. Requires the `read_publications` sco [cut] (SH-S-6102)
  - `read_publications`: The webhook topic for `collection_publications/update` events. Occurs whenever a collection publication listing is updated. Requires the `read_publications` sco [cut] (SH-S-6103)
  - `read_publications`: The webhook topic for `product_publications/create` events. Occurs whenever a product publication for an active product is created, or whenever an existing prod [cut] (SH-S-6104)
  - `read_resource_feedbacks`: Requires `read_resource_feedbacks` access scope. Also: App must be configured to use the Storefront API or as a Sales Channel. (SH-S-6105)
  - and 3 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `product.channels.changed`: {"id": 822945434, "slug": "product.channels.changed", "url": "https://docs.salla.dev/doc-433805#product-channels-changed-webhook-events-model", "order": 6, "is_ [cut] (SA-S-1596)
  - `product.unpublish`: {"id": 1388460461, "slug": "product.unpublish", "url": "https://docs.salla.dev/433805m0", "order": 15, "is_enabled": true, "name": {"ar": "تم إلغاء نشر المنتج ف [cut] (SA-S-1598)
  - `product.publish`: {"id": 1070020912, "slug": "product.publish", "url": "https://docs.salla.dev/433805m0", "order": 20, "is_enabled": true, "name": {"ar": "تم نشر المنتج في قناة ب [cut] (SA-S-1606)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `❓ لماذا تظهر بعض قنوات البيع معطّلة في عمود القنوات؟`: تظهر القناة معطّلة تلقائيًا إذا لم تكن متاحة لمتجرك، مثل عدم امتلاكك تطبيقًا مرتبطًا بمتجرك. (SA-S-5046)

## M-055

Shopify: SH-C-138 Product feeds and listings for channels, SH-C-146 Customer events and pixels; Salla: SA-C-074 Pixels, tracking and product feeds (Pixels & feeds), SA-C-092 Storefront e-commerce events (Ecommerce Events)

Basis: SH-C-146 platform_terms "Customer events"; platform_terms "Web pixel"; inventory SH-I-1732 "checkout_started"; inventory SH-I-1727 "cart_viewed" | SH-C-138 platform_terms "product_feeds/create" | SA-C-074 platform_terms "Pixels & feeds"; platform_terms "tiktok-pixel"; platform_terms "google-merchant-feed" | SA-C-092 platform_terms "Ecommerce Events"; platform_terms "Checkout Started"; platform_terms "Cart Viewed"

### Where it lives

- **Shopify**
  - `listings:root`: "path":"listings" (SH-S-5197)
  - `mappings:root`: "path":"mappings" (SH-S-5199)
  - `Listings`: "section":"Listings" (SH-S-1577)
  - `customer_events`: "title": "Customer events" (SH-S-1498)
  - `How web pixels work`: Pixels are JavaScript code snippets that run on the online store and collect behavioral data, referred to as (SH-S-0706)
  - `Benefits`: by loading pixels in a secure sandbox environment with APIs for subscribing to customer events. (SH-S-0708)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `ads Track`: {"id": 343420743, "name": "ads Track", "type": "app", "position": 2} (SA-S-1189)
  - `Pixels & feeds`: {"position": 43, "kind": "link", "text": "Pixels & feeds", "href": "/marketing/integration-tools/snapchat", "parent": 0, "list": 3} (SA-S-1813)
  - `@salla.sa/ui-merchant-marketing`: {"id": 1728378587281, "name": "@salla.sa/ui-merchant-marketing", "Prod": {}, "env": "prod", "path": "/^/marketing/(integration-tools\|affiliate\|advertisements\|gi [cut] (SA-S-3536)
  - `Ecommerce Events`: {"position": 8, "pointer": "/firstLevelNavbarItems/1/children/3", "depth": 1, "parent": "01HNA8Q9YTZGTHZYF36EYDJEWD", "type": "folder", "id": "01KB2PV60WXK636WX [cut] (SA-S-1164)

### Who decides

- **Shopify**
  - `listings:channel-mapping`: "eligibility":{"betas":["b529fc07","715156a4"]} (SH-S-5198)
  - `customer-events-settings:pixel`: "eligibility":{"permissions":["CUSTOM_PIXELS_VIEW"],"entitlements":["storefront.enabled"]} (SH-S-5138)
  - `customer-events-settings:pixel:details`: "eligibility":{"oneOf":[{"permissions":["APPLICATIONS"]},{"permissions":["LIMITED_APPLICATIONS"]}]} (SH-S-5028)
  - `write_pixels`: Requires `write_pixels` access scope. Also: The app must have the write\_server\_pixels access scope, and user access permission. (SH-S-6272)
  - `9.11 Shopify Pixel Manager`: Shopify allows you to add pixels to your Shopify Store to enable you or a third party to track customer events (the "Shopify Pixel Manager"). (SH-S-0066)
  - `Requesting consent`: In regions where customers must consent to tracking, app extension callbacks are executed only after consent is given. [scope: regions where customers must consent to tracking] (SH-S-0707)
  - and 1 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `الربط مع الخدمات الإعلانية`: "sub_features": []}, {"title": "الربط مع الخدمات الإعلانية", "description": "قم بإدارة حملاتك التسويقية باحترافية عبر ربط متجرك بخدمات إعلانية مثل Google Ads, S [cut] [scope: plan: سلة برو] (SA-S-2149)
  - `google-tag`: {"position": 20, "name": "google-tag", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-2981)
  - `utm-campaign`: {"position": 182, "name": "utm-campaign", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature" [cut] [scope: plans: plus, pro, special] (SA-S-3143)
  - `google-merchant-feed`: {"position": 240, "name": "google-merchant-feed", "value": {"enabled": false, "released": true, "type": "app", "app_id": null, "plans": ["plus", "pro", "special [cut] [scope: plans: plus, pro, special] (SA-S-3201)
  - `google-site-verification`: {"position": 241, "name": "google-site-verification", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type" [cut] [scope: plans: plus, pro, special] (SA-S-3202)
  - `facebook-catalog-feed`: {"position": 242, "name": "facebook-catalog-feed", "value": {"enabled": false, "released": true, "type": "app", "app_id": null, "plans": ["plus", "pro", "specia [cut] [scope: plans: plus, pro, special] (SA-S-3203)
  - and 8 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `9.11 Shopify Pixel Manager (summary)`: If you use the Shopify Pixel Manager, you are responsible for obtaining all necessary consents from store visitors and customers whose events you track. (SH-S-0067)
- **Salla**: gap (observation needed; stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_product_listings`: The webhook topic for `collection_listings/add` events. Occurs whenever a collection listing is added. Requires the `read_product_listings` scope. (SH-S-6090)
  - `read_product_listings`: The webhook topic for `collection_listings/remove` events. Occurs whenever a collection listing is removed. Requires the `read_product_listings` scope. (SH-S-6091)
  - `read_product_listings`: The webhook topic for `collection_listings/update` events. Occurs whenever a collection listing is updated. Requires the `read_product_listings` scope. (SH-S-6092)
  - `read_product_listings`: The webhook topic for `product_feeds/create` events. Triggers when product feed is created Requires the `read_product_listings` scope. (SH-S-6093)
  - `read_product_listings`: The webhook topic for `product_feeds/full_sync` events. Triggers when a full sync for a product feed is performed Requires the `read_product_listings` scope. (SH-S-6094)
  - `write_product_feeds`: "text": "write_product_feeds" (SH-S-1047)
  - and 11 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `meta.meta_type_1_desc`: اجمع بيانات التتبع من المتصفح والخادم معًا لتحصل على قياس أكثر دقة لأداء الإعلانات. (SA-S-5136)
  - `Device Mode Events`: "id": 5449698, "name": "Device Mode Events", "key": "apiDetailFolder.5449698", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDis [cut] (SA-S-1082)
  - `Cloud Mode Events`: "id": 8419683, "name": "Cloud Mode Events", "key": "apiDetailFolder.8419683", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisp [cut] (SA-S-1083)
  - `Product Added`: {"position": 0, "line": 7, "headings": ["Cart & Checkout Events", "Available Events"], "indent": 0, "item": "`Product Added` - Customer adds a product to cart"} (SA-S-1339)
  - `Product Removed`: {"position": 1, "line": 8, "headings": ["Cart & Checkout Events", "Available Events"], "indent": 0, "item": "`Product Removed` - Customer removes a product from [cut] (SA-S-1340)
  - `Cart Viewed`: {"position": 2, "line": 9, "headings": ["Cart & Checkout Events", "Available Events"], "indent": 0, "item": "`Cart Viewed` - Customer views their shopping cart" [cut] (SA-S-1341)
  - and 61 more statements in `platforms/salla/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `Cloud Mode (App Functions)`: This server-to-server approach removes the need for client-side scripts and ensures events are delivered reliably and securely. (SA-S-5148)

## M-056

Shopify: SH-C-139 Headless and custom storefronts; Salla: SA-C-101 Storefront API used by store pages; WooCommerce: WC-C-079 Store API (public storefront API)

Basis: SH-C-139 platform_terms "Storefront API" | SA-C-101 statement SA-S-5140 "Twilight comes with a JavaScript SDK for the Salla storefront APIs."; statement SA-S-0211 "Store APIs - Operational" | WC-C-079 platform_terms "Store API"; statement WC-S-0914 "The Store API provides public Rest API endpoints for the development of customer-facing cart, checkout, and product functionality."

### Where it lives

- **Shopify**
  - `headless:parent_route`: "path":"headless" (SH-S-5134)
  - `hydrogen:parent_route`: "path":"hydrogen" (SH-S-5135)
  - `What you get`: Deploy your Hydrogen app to Oxygen, Shopify's global edge hosting platform. (SH-S-0710)
  - `Storefront API`: "label": "Storefront API" (SH-S-0825)
  - `Hydrogen framework`: "label": "Hydrogen framework" (SH-S-0831)
- **Salla**
  - `status page component list`: Store APIs - Operational (SA-S-0211)
- **WooCommerce**
  - `WooCommerce Store API`: The Store API provides public Rest API endpoints for the development of customer-facing cart, checkout, and product functionality. (WC-S-0914)
  - `wc/store`: private static $api_namespace = 'wc/store'; (WC-S-0941)

### Who decides

- **Shopify**
  - `Build headless storefronts`: {"kind": "row", "section": 1, "position": 72, "cells": [{"tag": "th", "text": "Build headless storefronts", "scope": "row"}, {"tag": "td", "text": "1"}, {"tag": [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7056)
- **Salla**: gap (searched, not found)
- **WooCommerce**
  - `WooCommerce Store API`: In contrast to the WooCommerce REST API, the Store API is unauthenticated and does not provide access to sensitive store data or other customer information. (WC-S-0915)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (stated only in general terms)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `unauthenticated_read_checkouts`: Requires `unauthenticated_read_checkouts` access scope. (SH-S-6147)
  - `unauthenticated_read_content`: Requires `unauthenticated_read_content` access scope. (SH-S-6148)
  - `unauthenticated_read_customers`: Requires `unauthenticated_read_customers` access scope. (SH-S-6150)
  - `unauthenticated_read_customers`: * Your app has the `unauthenticated_read_customers`, `unauthenticated_write_customers`, `read_products`, `write_products`, `read_draft_orders`, and `write_draft [cut] (SH-S-6151)
  - `unauthenticated_read_customers`: * Your Headless channel or custom app has the `unauthenticated_read_product_listings`, `unauthenticated_read_customers` and `unauthenticated_write_checkouts` [a [cut] (SH-S-6152)
  - `unauthenticated_read_metaobjects`: Requires `unauthenticated_read_metaobjects` access scope. (SH-S-6153)
  - and 13 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Twilight JS SDK`: Twilight comes with a JavaScript SDK for the Salla storefront APIs. (SA-S-5140)
- **WooCommerce**
  - `wc/store/v1`: $this->register_routes( 'v1', self::$api_namespace . '/v1' ); (WC-S-0081)
  - `wc/store/v1 > /batch`: const IDENTIFIER = 'batch'; (WC-S-0148)
  - `wc/store/v1 > /cart`: const IDENTIFIER = 'cart'; (WC-S-0149)
  - `wc/store/v1 > /cart/add-item`: const IDENTIFIER = 'cart-add-item'; (WC-S-0150)
  - `wc/store/v1 > /cart/apply-coupon`: const IDENTIFIER = 'cart-apply-coupon'; (WC-S-0151)
  - `wc/store/v1 > /cart/coupons`: const IDENTIFIER = 'cart-coupons'; (WC-S-0152)
  - and 38 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**
  - `Build headless commerce`: Get all the power of Shopify under the hood, with complete control over the frontend. (SH-S-0709)
- **Salla**
  - `Twilight JS SDK`: This is to provide the developers with helper methods, or REST API endpoints, that allow communication between the frontend and backend. (SA-S-5141)
- **WooCommerce**: gap (searched, not found)

## M-057

Shopify: SH-C-142 Point of Sale; Salla: SA-C-095 Salla Point point of sale (سلة بوينت); WooCommerce: WC-C-089 Point of Sale in the mobile app

Basis: SH-C-142 platform_terms "Point of Sale"; platform_terms "Shopify Point of Sale (POS)" | SA-C-095 statement SA-S-0006 "Salla Point (سلة بوينت) is Salla's point-of-sale product"; platform_terms "بيع عبر نقاط البيع مع سلة بوينت" | WC-C-089 platform_terms "Point of Sale"; platform_terms "POS"

### Where it lives

- **Shopify**
  - `quick-sale`: "path":"quick-sale" (SH-S-5255)
  - `Shopify Point of Sale (POS)`: Shopify Point of Sale (POS) [scope: Google Play (publisher Shopify Inc.)] (SH-S-2757)
  - `Retail`: "label": "Retail" (SH-S-0785)
- **Salla**
  - `Salla PointFree Cashier`: {"position": 66, "kind": "link", "text": "Salla PointFree Cashier", "href": "/channel/sallapoint", "parent": 0, "list": 4} (SA-S-1836)
  - `@salla.sa/ui-merchant-pos`: {"id": 1728396395423, "name": "@salla.sa/ui-merchant-pos", "Prod": {}, "env": "prod", "path": "/channel/sallapoint", "position": 11} (SA-S-3540)
  - `## 2. What Salla is and is not`: Salla Point (سلة بوينت) is Salla's point-of-sale product for connecting in-person selling with online-store inventory and reporting. (SA-S-0006)
- **WooCommerce**
  - `Point of Sale`: $this->label = __( 'Point of Sale', 'woocommerce' ); (WC-S-0010)
  - `POS completed order (WC_Email_Customer_POS_Completed_Order)`: $this->title = __( 'POS completed order', 'woocommerce' ); (WC-S-0308)
  - `POS refunded order (WC_Email_Customer_POS_Refunded_Order)`: $this->title = __( 'POS refunded order', 'woocommerce' ); (WC-S-0309)
  - `Extensions > Official payments > In-person payments`: In-person payments (WC-S-0711)
  - `Extensions > Store management > Point of sale`: Point of sale (WC-S-0753)
  - `point_of_sale`: 'Enable Point of Sale functionality in the WooCommerce mobile apps.', (WC-S-0937)
  - and 1 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `quick-sale`: "eligibility":{"clients":["web"],"permissions":["QUICK_SALE"]} (SH-S-5227)
  - `9.3 POS Services`: The Fees for POS Services will be determined based on the number of locations at which you are using the POS Services. (SH-S-0049)
  - `Casual, in-person sales at pop-ups and events`: {"kind": "row", "section": 1, "position": 21, "cells": [{"tag": "th", "text": "Casual, in-person sales at pop-ups and events", "scope": "row"}, {"tag": "td", "t [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7017)
  - `POS Pro: Advanced tools for brick‑and‑mortar retailers`: {"kind": "row", "section": 1, "position": 22, "cells": [{"tag": "th", "text": "POS Pro: Advanced tools for brick‑and‑mortar retailers", "scope": "row"}, {"tag": [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7018)
  - `9.3 POS Services`: If you use our POS Services, you must use the same payment processor that you use for the Online Services. (SH-S-7262)
- **Salla**
  - `بيع عبر نقاط البيع مع سلة بوينت`: "title": "بيع عبر نقاط البيع مع سلة بوينت", "description": "أدِر مبيعاتك في الفروع والمعارض الموسمية عبر سلة بوينت، مجانًا ومباشرة من جوالك أو جهازك اللوحي بدون [cut] [scope: plan: سلة بلس] (SA-S-2094)
  - `salla_point_activate`: "permissions": [{"id": 939196354, "name": "salla_point_activate", "label": "salla point activate"}, {"id": 29826755, "name": "salla_point_add_employees", "label [cut] (SA-S-2441)
  - `salla_point_add_employees`: "label": "salla point activate"}, {"id": 29826755, "name": "salla_point_add_employees", "label": "salla point add employees"}, {"id": 1403796940, "name": "salla [cut] (SA-S-2442)
  - `salla_point_manage_accounts`: "label": "salla point add employees"}, {"id": 1403796940, "name": "salla_point_manage_accounts", "label": "salla point manage accounts"}, {"id": 763976909, "nam [cut] (SA-S-2443)
  - `salla_point_manage_payments`: "label": "salla point manage accounts"}, {"id": 763976909, "name": "salla_point_manage_payments", "label": "salla point manage payments"}, {"id": 2136374222, "n [cut] (SA-S-2444)
  - `salla_point_return_policy`: "label": "salla point manage payments"}, {"id": 2136374222, "name": "salla_point_return_policy", "label": "salla point return policy"}, {"id": 1228708559, "name [cut] (SA-S-2445)
  - and 25 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Requirements`: Your store address must be in one of the supported countries. (WC-S-0893)
  - `Requirements`: You must be using that country’s native currency as the store currency. (WC-S-0894)
  - `woocommerce_pos_*`: * POS access is defined entirely by `woocommerce_pos_*` capabilities granted per-user — the * same primitive WordPress uses for every other authorization decisi [cut] (WC-S-5435)

### Who is legally responsible

- **Shopify**
  - `9.3 POS Services`: While we take data security very seriously, we can't guarantee that all transmissions using the POS Equipment are 100% secure. All transactions transmitted usin [cut] (SH-S-7273)
- **Salla**
  - `softpos من جيديا`: - رخص العمل الحر تخضع لرسوم سنوية من جيديا يتم تحديدها حسب عقد التاجر مع جيديا. [scope: الدفع بالبطاقة في كاشير سلة بوينت (SoftPOS)] (SA-S-5038)
  - `❓ماذا يحدث في حال فشل الدفع؟`: في حال فشل الدفع فلا يتم إكمال الطلب, وفي حال نجاح الدفع يتم تحويل العملية تلقائيًا إلى تحويل بنكي من خلال مزود الخدمة مثل جيديا [scope: الدفع بالبطاقة في كاشير سلة بوينت (SoftPOS)] (SA-S-5039)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `PointOfSaleDevice`: "name": "PointOfSaleDevice", "kind": "OBJECT", "description": "Represents a mobile device that Shopify Point of Sale has been installed on." [scope: GraphQL Admin API 2026-10] (SH-S-7461)
- **Salla**
  - `الربط بحساب جيديا`: للبدء في تفعيل الدفع بالبطاقة عبر كاشير سلة بوينت كاشير مجاني، عليك الربط بحساب جيديا. (SA-S-5040)
- **WooCommerce**
  - `Woo Mobile App: Point of Sale Mode`: All sales sync with your existing WooCommerce site. (WC-S-0895)

### Stated reason

- **Shopify**
  - `TSE Compliance`: German merchants can meet TSE Compliance by recording and exporting point of sale (POS) transactions to comply with KassenSichV regulation. [scope: Germany] (SH-S-7285)
- **Salla**
  - `❓لماذا يتم ربط الرقم الخاص بجهاز الدفع(Terminal ID) بموظف محدد؟`: لأسباب أمنية وتنظيمية، ولضمان تتبع العمليات المالية بدقة. (SA-S-5041)
  - `❓لماذا لا يمكن استخدام نفس الجهاز على أكثر من جوال؟`: لأن رقم جهاز الدفع مخصص لجهاز واحد فقط وفق متطلبات أنظمة الدفع وNearPay. (SA-S-5042)
- **WooCommerce**
  - `woocommerce_pos_*`: * Capabilities are granted per-user via add_cap(), never bundled onto a WP role. * POS access can therefore be added to any existing user (shop_manager, * admin [cut] (WC-S-5436)

## M-058

Shopify: SH-C-145 Analytics and reports; Salla: SA-C-220 Store reports and analytics (Reports; Store performance); WooCommerce: WC-C-038 Store analytics and reports kept in the store

Basis: SH-C-145 platform_terms "Analytics"; platform_terms "Reports" | SA-C-220 platform_terms "Analytics"; platform_terms "Reports"; platform_terms "تحليلات المبيعات" | WC-C-038 platform_terms "Analytics"; platform_terms "Reports"

### Where it lives

- **Shopify**
  - `analytics`: "path":"analytics" (SH-S-5030)
  - `Analytics`: "text": "Analytics" (SH-S-1531)
  - `ShopifyQL for analytics`: "label": "ShopifyQL for analytics" (SH-S-0810)
- **Salla**
  - `Analytics`: {"id": 70191848, "name": "Analytics", "type": "app", "position": 10} (SA-S-1197)
  - `Analytics`: {"id": 13, "slug": "analytics", "icon": "graph-bar", "color": "light-blue", "type": "app", "featured": true, "order": 4, "hidden": false, "name": {"ar": "التحلي [cut] (SA-S-1224)
  - `Statuses included in reports`: "orders/order-statuses-in-reports":"Statuses included in reports" (SA-S-1740)
  - `Store performance`: {"position": 85, "kind": "link", "text": "Store performance", "href": "/reports/performance", "parent": 0, "list": 6} (SA-S-1855)
  - `Smart analytics`: {"position": 86, "kind": "link", "text": "Smart analytics", "href": "/reports/smart-analysis", "parent": 0, "list": 6} (SA-S-1856)
  - `Reports`: {"position": 87, "kind": "link", "text": "Reports", "href": "/reports", "parent": 0, "list": 6} (SA-S-1857)
  - and 2 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `WooCommerce > Reports`: add_submenu_page( 'woocommerce', __( 'Reports', 'woocommerce' ), __( 'Reports', 'woocommerce' ), 'view_woocommerce_reports', 'wc-reports', array( $this, 'report [cut] (WC-S-0043)
  - `Analytics`: 'title' => __( 'Analytics', 'woocommerce' ), (WC-S-0064)
  - `Analytics > Overview`: 'title' => __( 'Overview', 'woocommerce' ), (WC-S-0065)
  - `Analytics > Products`: 'title' => __( 'Products', 'woocommerce' ), (WC-S-0066)
  - `Analytics > Revenue`: 'title' => __( 'Revenue', 'woocommerce' ), (WC-S-0067)
  - `Analytics > Orders`: 'title' => __( 'Orders', 'woocommerce' ), (WC-S-0068)
  - and 8 more statements in `platforms/woocommerce/statements.tsv`

### Who decides

- **Shopify**
  - `analytics:overview:eligibility`: "eligibility":{"permissions":["OVERVIEWS"]} (SH-S-5023)
  - `analytics:live`: "eligibility":{"entitlements":["storefront.enabled"]} (SH-S-5031)
  - `analytics:reports:eligibility`: "eligibility":{"permissions":["REPORTS"]} (SH-S-5032)
  - `analytics:reports:promise_summary`: "eligibility":{"betas":["9ed93472"]} (SH-S-5033)
  - `entitlements.storefront.enabled`: {"set": 0, "section": "entitlements", "key": "storefront", "value": {"enabled": true, "__typename": "StorefrontType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5364)
  - `200+ real-time reports, plus custom analytics`: {"kind": "row", "section": 1, "position": 17, "cells": [{"tag": "th", "text": "200+ real-time reports, plus custom analytics", "scope": "row"}, {"tag": "td", "t [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7014)
- **Salla**
  - `ملخص أداء المتجر`: "sub_features": [{"parent_code": "altkaryr", "title": "ملخص أداء المتجر", "description": null, "icon": null, "icon_color": null, "icon_background": null, "extra [cut] [scope: plan: سلة بلس] (SA-S-2043)
  - `تحليلات الأرباح`: "extra_icons": null}, {"parent_code": "altkaryr", "title": "تحليلات الأرباح", "description": null, "icon": null, "icon_color": null, "icon_background": null, "e [cut] [scope: plan: سلة بلس] (SA-S-2044)
  - `تقرير تكاليف وأرباح الشحن`: "extra_icons": null}, {"parent_code": "altkaryr", "title": "تقرير تكاليف وأرباح الشحن", "description": null, "icon": null, "icon_color": null, "icon_background" [cut] [scope: plan: سلة بلس] (SA-S-2045)
  - `تحليلات المبيعات`: "extra_icons": null}, {"parent_code": "altkaryr", "title": "تحليلات المبيعات", "description": null, "icon": null, "icon_color": null, "icon_background": null, " [cut] [scope: plan: سلة بلس] (SA-S-2046)
  - `تحليلات العملاء`: "extra_icons": null}, {"parent_code": "altkaryr", "title": "تحليلات العملاء", "description": null, "icon": null, "icon_color": null, "icon_background": null, "e [cut] [scope: plan: سلة بلس] (SA-S-2047)
  - `تحليلات الزيارات`: "extra_icons": null}, {"parent_code": "altkaryr", "title": "تحليلات الزيارات", "description": null, "icon": null, "icon_color": null, "icon_background": null, " [cut] [scope: plan: سلة بلس] (SA-S-2048)
  - and 72 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `analytics (woocommerce_analytics_enabled)`: 'option_key' => Analytics::TOGGLE_OPTION_NAME, 'is_experimental' => false, 'enabled_by_default' => true, 'disable_ui' => false, (WC-S-5374)
  - `wc-reports`: add_submenu_page( 'woocommerce', __( 'Reports', 'woocommerce' ), __( 'Reports', 'woocommerce' ), 'view_woocommerce_reports', 'wc-reports', array( $this, 'report [cut] (WC-S-0043)
  - `PageController::register_page`: 'capability' => 'view_woocommerce_reports', (WC-S-5375)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_analytics_annotations`: Requires Requires `read_analytics_annotations` or `write_analytics_annotations` access scope. (SH-S-5902)
  - `read_reports`: Requires `read_reports` access scope. (SH-S-5903)
  - `read_reports`: Requires `read_reports` access scope. Also: Level 2 access to Customer data including name, address, phone, and email fields. Please refer to protected customer [cut] (SH-S-5904)
  - `read_reports`: 2. Request the `read_reports` access scope so that your app can read analytics and reporting data. (SH-S-5905)
  - `read_reports`: Running `shopifyqlQuery` requires the [`read_reports`](https://shopify.dev/docs/api/usage/access-scopes#authenticated-access-scopes) access scope, [Level 2 acce [cut] (SH-S-5906)
  - `read_reports`: [`shopifyqlQuery`](https://shopify.dev/docs/api/admin-graphql/latest/queries/shopifyqlQuery) requires the [`read_reports`](https://shopify.dev/docs/api/usage/ac [cut] (SH-S-5907)
  - and 5 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Report Creator`: The Report Creator is a powerful new feature in the Salla Partners Portal that enables developers to build custom analytical reports to be displayed on the Sall [cut] (SA-S-5146)
- **WooCommerce**
  - `wc-analytics`: $rest_api_util->lazy_load_namespace( 'wc-analytics', array( $this, 'rest_api_init_wc_analytics' ) ); (WC-S-0084)
  - `wc/v3 > reports-sales`: 'reports-sales' => 'WC_REST_Report_Sales_Controller', (WC-S-0103)
  - `wc/v3 > reports-top-sellers`: 'reports-top-sellers' => 'WC_REST_Report_Top_Sellers_Controller', (WC-S-0104)
  - `wc/v3 > reports-orders-totals`: 'reports-orders-totals' => 'WC_REST_Report_Orders_Totals_Controller', (WC-S-0105)
  - `wc/v3 > reports-products-totals`: 'reports-products-totals' => 'WC_REST_Report_Products_Totals_Controller', (WC-S-0106)
  - `wc/v3 > reports-customers-totals`: 'reports-customers-totals' => 'WC_REST_Report_Customers_Totals_Controller', (WC-S-0107)
  - and 44 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-059

Shopify: SH-C-148 Customer privacy settings, cookie banner and consent, SH-C-149 Customer data requests and erasure; Salla: SA-C-066 Customers' personal data: privacy policy, consent, data export and deletion; WooCommerce: WC-C-045 Personal data export, erasure and retention

Basis: SH-C-148 platform_terms "Cookie banner"; platform_terms "Customer privacy" | SH-C-149 platform_terms "Request data"; platform_terms "Erase personal data" | SA-C-066 platform_terms "website-cookies"; platform_terms "customer-data-export"; platform_terms "customer-account-deletion" | WC-C-045 inventory WC-I-0357 "add_exporter: WooCommerce Customer Data"; inventory WC-I-0361 "add_eraser: WooCommerce Customer Data"; platform_terms "Accounts & Privacy"

### Where it lives

- **Shopify**
  - `privacy`: "title": "Customer privacy" (SH-S-1502)
  - `help.shopify.com/en/manual/privacy-and-security/privacy/customer-privacy-setting`: Because privacy laws and regulations vary across different regions, the **Customer privacy** settings lets you customize your privacy settings for each country  [cut] (SH-S-0662)
  - `Customer Privacy API`: "label": "Customer Privacy API" (SH-S-0835)
  - `customers`: [**Customers**](https://admin.shopify.com/customers) (SH-S-6362)
- **Salla**
  - `كيف يمكنني إدراج صفحة الخصوصية في متجري؟`: يمكن إدراج صفحة الخصوصية في متجرك كصفحة تعريفية. (SA-S-5022)
- **WooCommerce**
  - `Accounts & Privacy`: $this->label = __( 'Accounts &amp; Privacy', 'woocommerce' ); (WC-S-0006)
  - `personal_data_retention`: 'title' => __( 'Personal data retention', 'woocommerce' ), (WC-S-0929)

### Who decides

- **Shopify**
  - `customer-privacy`: "eligibility":{"permissions":["PREFERENCES"]} (SH-S-5131)
  - `customer-privacy-policy-modal`: "eligibility":{"permissions":["MANAGE_POLICIES"]} (SH-S-5253)
  - `customer-privacy:consent-banner`: "eligibility":{"entitlements":["storefront.enabled"]} (SH-S-5031)
  - `help.shopify.com/en/manual/privacy-and-security/privacy/customer-privacy-setting`: Because privacy laws and regulations vary across different regions, the **Customer privacy** settings lets you customize your privacy settings for each country  [cut] (SH-S-0662)
  - `entitlements.storefront.enabled`: {"set": 0, "section": "entitlements", "key": "storefront", "value": {"enabled": true, "__typename": "StorefrontType"}} [scope: 2jiwxs-gr (trial); capture-advanced (Advanced App Development, development store); capture-client-store-vny2vy5w (Custom plan, development store); capture-gb-plus (Shopify Plus App Development, development store); capture-grow (Grow App Development, development store); capture-plus (Shopify Plus App Development, development store); capture-plus-dev (Shopify Plus App Development, development store); ctcbwa-r1 (trial); ctcbwa-r1 (Advanced); demo-fake-dev-store (Basic App Development, development store); fake-demo-sharrwah (trial); fake-demo-sharrwah (Advanced); ibx5bt-xy (trial); ts15uk-ug (trial); zyd38b-ze (trial)] (SH-S-5364)
  - `apps.shopify.com/built-in-features/automated-privacy`: Your Shopify plan includes automated privacy features that are enabled by default and automatically update as both your store and privacy regulations change. (SH-S-7210)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `customer-account-deletion`: {"position": 213, "name": "customer-account-deletion", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3174)
  - `customer-data-export`: {"position": 214, "name": "customer-data-export", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3175)
  - `website-cookies`: {"position": 411, "name": "website-cookies", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "featu [cut] [scope: plans: plus, pro, special] (SA-S-3372)
  - `توافق سياسة الخصوصية لمتجرك مع نظام حماية البيانات الشخصي`: يجب أن تتوافق سياسة الخصوصية لمتجرك مع نظام حماية البيانات الشخصية الذي أُقر بتاريخ 14/9/2024. (SA-S-0169)
  - `الأسئلة الشائعة`: يطبق هذا النظام على أي عملية معالجة لبيانات شخصية تتعلق بالأفراد المواطنين أو المقيمين في المملكة بأي وسيلة كانت من أي جهة خارج المملكة. [scope: الأفراد المواطنين أو المقيمين في المملكة] (SA-S-0170)
- **WooCommerce**
  - `Accounts and Privacy Settings`: Use these settings to enable or disable guest checkout, control customer account creation, decide how your store retains or removes personal data, and set your  [cut] (WC-S-0881)
  - `woocommerce_erasure_request_removes_order_data`: 'id' => 'woocommerce_erasure_request_removes_order_data', 'type' => 'checkbox', 'default' => 'no', (WC-S-5376)

### Who is legally responsible

- **Shopify**
  - `Configuration options`: Using Shopify alone doesn't guarantee that a merchant complies with the General Data Protection Regulation (GDPR). (SH-S-0646)
  - `9.11 Shopify Pixel Manager (summary)`: If you use the Shopify Pixel Manager, you are responsible for obtaining all necessary consents from store visitors and customers whose events you track. (SH-S-0067)
  - `Processing erasure requests`: When you submit a request to erase a customer's personal data from their profile, Shopify processes the request for you. (SH-S-0666)
  - `help.shopify.com/en/manual/privacy-and-security/privacy/processing-customer-data`: As a Shopify merchant, you're responsible for complying with the privacy and data protection laws and regulations that apply to your business. (SH-S-0663)
  - `Erasing a customer's personal data`: It's your responsibility to contact any other companies that you've shared the customer's personal data with. (SH-S-0665)
  - `Erasing a customer's personal data`: In response to a request to erase, Shopify erases personal data, such as your customer's name and address. (SH-S-0664)
- **Salla**
  - `توافق سياسة الخصوصية لمتجرك مع نظام حماية البيانات الشخصي`: التزامات جهة التحكم:(التاجر المطلع على بيانات عملائه) (SA-S-0168)
  - `المادة (3) – شروط النشر في المتجر (للمطورين)`: تلتزم التطبيقات المنشورة بعدم جمع بيانات حساسة دون تصريح صريح من المستخدم. [scope: التطبيقات المنشورة في متجر تطبيقات سلة] (SA-S-0030)
- **WooCommerce**
  - `When a DPA is useful`: For this type of information, the site owner (usually a business) is acting as a "Data Controller" [scope: a store on WordPress.com that collects and stores other people's names and addresses] (WC-S-5467)

### How it meets the rest

- **Shopify**
  - `read_privacy_settings`: Requires `read_privacy_settings` access scope. (SH-S-6089)
  - `read_privacy_settings`: Requires `read_privacy_settings` access scope, `read_content` access scope or `read_online_store_pages` access scope. (SH-S-5956)
  - `write_privacy_settings`: Requires `write_privacy_settings` access scope. (SH-S-6275)
  - `read_privacy_settings`: "text": "read_privacy_settings" (SH-S-1044)
  - `Customer Privacy API`: "label": "Customer Privacy API" (SH-S-0835)
  - `2. Using the Shopify API`: integrate with Shopify's Consent Tracking API (also referred to as the "Customer Privacy API") (SH-S-0224)
  - and 4 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `عرض سياسة الخصوصية أثناء تسجيل العميل`: عند قيام العميل بإنشاء حساب جديد في متجرك، تظهر له نافذة تسجيل تتضمن تنبيه واضح يفيد بأن إتمام عملية التسجيل يُعد موافقة على سياسة الخصوصية الخاصة بالمتجر، مع إ [cut] (SA-S-5023)
- **WooCommerce**
  - `add_exporter: WooCommerce Customer Data`: $this->add_exporter( 'woocommerce-customer-data', __( 'WooCommerce Customer Data', 'woocommerce' ), array( 'WC_Privacy_Exporters', 'customer_data_exporter' ) ); (WC-S-0357)
  - `add_exporter: WooCommerce Customer Orders`: $this->add_exporter( 'woocommerce-customer-orders', __( 'WooCommerce Customer Orders', 'woocommerce' ), array( 'WC_Privacy_Exporters', 'order_data_exporter' ) ) [cut] (WC-S-0358)
  - `add_exporter: WooCommerce Customer Downloads`: $this->add_exporter( 'woocommerce-customer-downloads', __( 'WooCommerce Customer Downloads', 'woocommerce' ), array( 'WC_Privacy_Exporters', 'download_data_expo [cut] (WC-S-0359)
  - `add_exporter: WooCommerce Customer Payment Tokens`: $this->add_exporter( 'woocommerce-customer-tokens', __( 'WooCommerce Customer Payment Tokens', 'woocommerce' ), array( 'WC_Privacy_Exporters', 'customer_tokens_ [cut] (WC-S-0360)
  - `add_eraser: WooCommerce Customer Data`: $this->add_eraser( 'woocommerce-customer-data', __( 'WooCommerce Customer Data', 'woocommerce' ), array( 'WC_Privacy_Erasers', 'customer_data_eraser' ) ); (WC-S-0361)
  - `add_eraser: WooCommerce Customer Orders`: $this->add_eraser( 'woocommerce-customer-orders', __( 'WooCommerce Customer Orders', 'woocommerce' ), array( 'WC_Privacy_Erasers', 'order_data_eraser' ) ); (WC-S-0362)
  - and 2 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**
  - `Customer privacy`: Because privacy laws and regulations vary across different regions, the Customer privacy settings lets you customize your privacy settings for each country and  [cut] (SH-S-7286)
- **Salla**
  - `عرض سياسة الخصوصية أثناء تسجيل العميل`: يساعد على توضيح كيفية استخدام بيانات العميل بشكل شفاف قبل إتمام التسجيل، كما يضمن اطلاع العميل على سياسة الخصوصية وإقراره بها عند إنشاء الحساب. (SA-S-5024)
- **WooCommerce**: gap (searched, not found)

## M-060

Shopify: SH-C-180 Data protection roles for the merchant's customer data; Salla: SA-C-171 Salla's privacy policy (سياسة الخصوصية); WooCommerce: WC-C-024 Data controller for Woo services, WC-C-044 Automattic as processor of site visitors' data (data processing agreement)

Basis: SH-C-180 platform_terms "Data Processing Addendum"; platform_terms "Data Controller"; inventory SH-I-1376 "View privacy policy" | SA-C-171 platform_terms "سياسة الخصوصية"; platform_terms "https://salla.com/en-sa/privacy" | WC-C-024 platform_terms "Controllers and Responsible Companies"; inventory WC-I-0631 "Privacy Policy" | WC-C-044 platform_terms "Data Processing Agreement"; statement WC-S-5329 "Data processing addendum"

### Where it lives

- **Shopify**: gap (searched, not found)
- **Salla**
  - `https://salla.com/privacy`: <url><loc>https://salla.com/privacy</loc></url> (SA-S-2209)
- **WooCommerce**
  - `Data processing addendum`: Scroll down to the "Data processing addendum" section. Click the "Request a DPA" button. [scope: WordPress.com account (my.wordpress.com/me/account, Preferences > Privacy)] (WC-S-5329)

### Who decides

- **Shopify**
  - `Data Processing Addendum`: a) The Parties agree that the Terms together with this DPA constitute Your documented instructions regarding Shopify's processing of Your Customer Personal Data [cut] (SH-S-7261)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `Controllers and Responsible Companies`: Different Automattic companies are the controller (or co-controller) of personal information, which means that they are the company responsible for processing t [cut] (WC-S-0495)
  - `When a DPA is useful`: This "Data Processing Agreement" is a business to business agreement and is not relevant or needed for the typical free site owner or hobbyists. (WC-S-5330)

### Who is legally responsible

- **Shopify**
  - `I. PURPOSE`: You shall act as a Data Controller and Shopify shall act as a Data Processor with respect to the processing of Your Customer Personal Data, in connection with Y [cut] (SH-S-0186)
  - `I. PURPOSE`: by and between You (or "Merchant"), and the Shopify Contracting Entity as set forth in the Terms ("Shopify") (SH-S-0187)
  - `I. PURPOSE`: If you receive Enhanced Services from Shopify (as defined in Section 9.2 of the Terms of Service) Shopify shall process Your Customer Personal Data as a Data Co [cut] (SH-S-0192)
  - `Shopify's Consumer Services`: When a customer uses Shopify Consumer Services, such as Shop or Shop Pay, then Shopify is directly engaged by the customer and Shopify acts as the data controll [cut] (SH-S-0244)
  - `9.2 Enhanced Services`: To provide the Enhanced Services, Shopify can use Personal Data from your customers' interactions and transactions with Your Store, with other Merchants, and wi [cut] (SH-S-0046)
- **Salla**
  - `المادة (8) – السرية والخصوصية`: يلتزم الجميع بسياسة الخصوصية المعلنة في منصة سلة، وبنظام حماية البيانات الشخصية بالمملكة. [scope: متجر تطبيقات سلة] (SA-S-0029)
- **WooCommerce**
  - `Controllers and Responsible Companies`: Different Automattic companies are the controller (or co-controller) of personal information, which means that they are the company responsible for processing t [cut] (WC-S-0495)
  - `Controllers and Responsible Companies`: Generally, the “controller” is the Automattic company that entered into the contract with you under the Terms of Service for the product or service you use. (WC-S-0494)
  - `Controllers and Responsible Companies: Woo Services`: Automattic Inc. is also the controller for some of the processing activities related to Services provided by WooCommerce, Inc. (WC-S-0498)
  - `Controllers and Responsible Companies: Woo Services`: Automattic Inc. and WooCommerce, Inc. are also the joint controllers for some of the processing activities related to Services provided by WooCommerce Ireland L [cut] (WC-S-0497)
  - `Request a data processing agreement`: The Data Processing Agreement is an amendment to our Terms of Service and is available to all WordPress.com site owners. [scope: WordPress.com site owners] (WC-S-0847)
  - `19. Data Processing Agreement`: If you need a data processing agreement (DPA) with us for the GDPR requirements that apply to us as a data processor for your website, please follow these instr [cut] (WC-S-0658)
  - and 1 more statements in `platforms/woocommerce/statements.tsv`

### How it meets the rest

- **Shopify**
  - `12. Privacy and Data Protection`: Shopify's collection, use, disclosure and processing of Your Customer Personal Data (as defined in the Data Processing Addendum) is subject to these Terms, our  [cut] (SH-S-0072)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `Request a DPA`: This will automatically send a DPA to your account's email address which you can sign and return to privacypolicyupdates@automattic.com for processing. (WC-S-5331)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `19. Data Processing Agreement`: If you need a data processing agreement (DPA) with us for the GDPR requirements that apply to us as a data processor for your website, please follow these instr [cut] (WC-S-0658)

## M-061

Shopify: SH-C-181 Where data is stored and processed; WooCommerce: WC-C-043 Transfer outside the EEA and UK of data processed by Automattic

Basis: SH-C-181 inventory SH-I-2285 "International transfers of personal data" | WC-C-043 platform_terms "Transferring Information"

### Where it lives

- **Shopify**
  - `Data hosting locations`: Shopify dynamically rebalances storage between multiple Google Cloud Platform regions to ensure that we can offer a reliable and scalable infrastructure that ca [cut] (SH-S-0636)
  - `Data hosting locations`: New merchants in Europe automatically avail of this new infrastructure and now have their store data, order data and customer personal data stored at rest in Eu [cut] [scope: new merchants in Europe] (SH-S-0638)
  - `Third-party subprocessors table, row Google Cloud Canada Corporation, column Ser`: Cloud hosting and data processing [scope: subprocessor Google Cloud Canada Corporation (the row cited)] (SH-S-0196)
  - `Third-party subprocessors table, column Data that may be processed (rows Amazon `: <td>All platform data</td> [scope: subprocessor rows cited (Amazon Web Services, Google Cloud)] (SH-S-0198)
  - `A Pods Architecture To Allow Shopify To Scale`: A pod consists of a set of shops that live on a fully isolated set of datastores. (SH-S-0672)
  - `A Pods Architecture To Allow Shopify To Scale, disaster recovery`: We assigned each pod a pair of data centers, and at any point in time one of the two will be the active data center while the second acts as a recovery site. (SH-S-0673)
- **WooCommerce**
  - `Transferring Information`: the information about you that we process when you use the Services in the EU or the UK may be used, stored, and/or accessed by individuals operating outside th [cut] [scope: information processed when the Services are used in the EU or the UK] (WC-S-0659)

### Who decides

- **Shopify**
  - `Data hosting locations`: We need to be able to move data geographically in order to operate our services, and we have mechanisms in place to do so in accordance with applicable laws and [cut] (SH-S-0637)
  - `Data hosting locations`: Even where merchant customer personal data is stored in Europe, we will rely on international data transfers for processing that personal data. (SH-S-0639)
  - `Data hosting locations`: New merchants in Europe automatically avail of this new infrastructure and now have their store data, order data and customer personal data stored at rest in Eu [cut] [scope: new merchants in Europe] (SH-S-0638)
- **WooCommerce**: gap (searched, not found)

### Who is legally responsible

- **Shopify**
  - `Where we send your information, Transfers outside of the EEA, the UK and Switzer`: If you are located in the EEA, the UK, or Switzerland, your Personal Data is received by our Irish affiliate, Shopify International Ltd. [scope: people located in the EEA, the UK, or Switzerland] (SH-S-0227)
  - `help.shopify.com/en/manual/your-account/privacy/subprocessors.md`: All personal data from customers in the European Economic Area (EEA), the United Kingdom (U.K.), and Switzerland is initially processed by Shopify International [cut] [scope: personal data from customers in the EEA, the UK and Switzerland] (SH-S-0194)
  - `Onward transfers of personal data from the EEA and the UK`: International Limited also acts as Shopify’s main establishment for General Data Protection Regulation (GDPR) purposes. (SH-S-0641)
  - `How Shopify meets the GDPR requirements for international data transfers`: Shopify relies on the European Commission’s adequacy decision for Canada when Shopify International Limited transfers personal data to its Canadian-registered c [cut] (SH-S-0640)
  - `Where we send your information`: We are a Canadian company, but we work with and process data about individuals across the world. To operate our business, we may send your Personal Data outside [cut] (SH-S-0175)
  - `Where we send your information, Transfers outside of the EEA, the UK and Switzer`: Your information is then sent to other Shopify locations and to service providers who may be located in other regions, including Canada (where we are headquarte [cut] (SH-S-0226)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `Transferring Information`: These measures include entering into European Commission or UK government approved standard contractual arrangements with entities based in countries outside th [cut] (WC-S-0499)

### How it meets the rest

- **Shopify**
  - `A. Global Data Transfers`: You acknowledge that Your Customer Personal Data may be transferred and processed in any country in which Shopify, its affiliated companies or third party servi [cut] (SH-S-0188)
  - `Appendix C, 8. International Transfers`: Subject to compliance with European Data Protection Laws, Shopify International Ltd. may transfer Your Customer Personal Data processed under this Appendix outs [cut] (SH-S-0191)
  - `How Shopify meets the GDPR requirements for international data transfers`: Shopify also employs comprehensive data transfer and processing agreements (DPAs) incorporating the latest version of the Standard Contractual Clauses (SCCs) ap [cut] (SH-S-0643)
  - `www.shopify.com/legal/binding-corporate-rules`: The links below reflect our most recent BCRs, which took effect on July 8, 2026. (SH-S-0648)
  - `Where we send your information, Transfers outside of the EEA, the UK and Switzer`: If you are in the EEA or Switzerland, when we send your Personal Data to any other Shopify entity outside the EEA or Switzerland, it is transferred in accordanc [cut] [scope: people in the EEA or Switzerland] (SH-S-0176)
- **WooCommerce**: gap (searched, not found)

### Stated reason

- **Shopify**
  - `Data hosting locations`: Shopify dynamically rebalances storage between multiple Google Cloud Platform regions to ensure that we can offer a reliable and scalable infrastructure that ca [cut] (SH-S-0636)
  - `A Pods Architecture To Allow Shopify To Scale`: Simply sharding the databases wasn't enough, we needed to fully isolate each shard so a failure couldn't spiral out into a platform outage. (SH-S-0674)
- **WooCommerce**
  - `Transferring Information`: Because Automattic’s Services are offered worldwide, the information about you that we process when you use the Services in the EU or the UK may be used, stored (WC-S-0942)

## M-062

Shopify: SH-C-184 Payment card data security; WooCommerce: WC-C-018 Cardholder data security for WooPayments (PCI DSS), WC-C-019 PCI DSS compliance of the merchant's store

Basis: SH-C-184 platform_terms "PCI DSS" | WC-C-018 platform_terms "PCI DSS" | WC-C-019 platform_terms "PCI-DSS compliance and WooCommerce"

### Where it lives

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `What makes WooPayments PCI Compliant?`: These fields are served securely from our payment partner’s PCI DSS–validated environment. (WC-S-0552)
  - `WooCommerce and PCI compliance`: The core WooCommerce plugin is not PCI certified, as it does not handle cardholder data or process payments directly. (WC-S-5304)
  - `WooCommerce and PCI compliance`: Many PCI requirements apply to your broader environment - including your hosting provider, the plugins you use, and your policies around user access, updates, a [cut] (WC-S-5305)

### Who decides

- **Shopify**
  - `www.shopify.com/pricing (FAQ answer)`: Yes. Shopify is certified Level 1 PCI DSS compliant, and stores powered by Shopify are PCI compliant by default, which helps keep payment information secure. (SH-S-7202)
- **WooCommerce**
  - `Types of payment gateway`: Direct gateways, however, require server security to be implemented [scope: direct gateways] (WC-S-0626)
  - `Do I need to be PCI-DSS compliant?`: If you store, process, or transmit cardholder data as defined in the PCI SSC glossary, then PCI-DSS applies to you. (WC-S-0882)
  - `Reporting compliance`: PCI compliance is often enforced by your payment processor, who may ask you to complete a self-assessment questionnaire (SAQ) or undergo scans by an approved sc [cut] (WC-S-5306)

### Who is legally responsible

- **Shopify**
  - `12. Privacy and Data Protection`: Where the Services involve Shopify storing, processing or transmitting "Account Data" (as defined under PCI DSS) on your behalf, Shopify acknowledges that it is [cut] (SH-S-0073)
  - `Part I, A. Data Security`: Where the Payments Services involve Shopify storing, processing or transmitting "Account Data", as defined under Payment Card Industry Data Security Standards ( [cut] (SH-S-0097)
  - `Part I, A. POS Equipment`: This P2PE Service is provided, managed, and processed exclusively by Stripe and is designed to encrypt cardholder data at the point of interaction. (SH-S-0089)
  - `PCI Attestation of Compliance (AoC)`: This is Shopify's service provider PCI DSS AOC which is the best evidence of the PCI DSS compliance of Shopify's services. (SH-S-7481)
- **WooCommerce**
  - `Is WooPayments PCI Compliant?`: Yes, WooPayments is PCI DSS compliant as a Level 1 service provider. (WC-S-0550)
  - `8. j. More on WooPayments Specifically`: We acknowledge responsibility for the security of cardholder data we store, process, or transmit on behalf of WooPayments users, where that data is within our p [cut] (WC-S-0479)
  - `8. j. Ecommerce Services: Your responsibilities`: must comply with Payment Card Industry Data Security Standard (PCI DSS) if applicable to you. (WC-S-0471)
  - `Is WooPayments PCI Compliant?`: While WooPayments handles payment processing in a PCI DSS–validated environment, your site still plays a role in presenting the checkout experience and must mee [cut] [scope: stores using WooPayments] (WC-S-0551)
  - `WooCommerce and PCI compliance`: PCI DSS compliance is ultimately the responsibility of the store owner. (WC-S-5303)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `What makes WooPayments PCI Compliant?`: These fields are served securely from our payment partner’s PCI DSS–validated environment. (WC-S-0552)
  - `What about saved cards and subscriptions?`: These tokens are stored by our payment partner and requested through your site’s connection to WordPress.com. (WC-S-0554)
  - `WooCommerce and PCI compliance`: WooCommerce never stores card details, and official WooCommerce payment gateways only retain partial data when using payment tokens (e.g., last 4 digits). (WC-S-5307)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `What makes WooPayments PCI Compliant?`: Because sensitive payment information is never handled by your site or stored on your server, WooPayments helps reduce your PCI compliance scope significantly. (WC-S-0859)
  - `Do I need to be PCI-DSS compliant?`: However, because your site still serves the checkout page, PCI-DSS does still apply - though your compliance scope may be significantly reduced. [scope: sites using a gateway that processes payments off-site or through hosted fields] (WC-S-5308)

## M-063

Shopify: SH-C-150 Notifications; Salla: SA-C-011 Store notification settings (Notifications / الإشعارات)

Basis: SH-C-150 platform_terms "Notifications" | SA-C-011 platform_terms "Notifications"; concern "Notifications / الإشعارات"

### Where it lives

- **Shopify**
  - `email-templates:parent`: "path":"email_templates/:templateId/parent" (SH-S-5210)
  - `notifications`: "title": "Notifications" (SH-S-1499)
  - `notification-settings`: "section":"Notifications","path":"notifications" (SH-S-7141)
- **Salla**
  - `Notifications`: {"position": 25, "kind": "link", "text": "Notifications", "href": "/notifications"} (SA-S-1701)
  - `SMS log`: {"position": 125, "kind": "link", "text": "SMS log", "href": "/logs/messages", "parent": 0, "list": 11} (SA-S-1895)
  - `@salla.sa/ui-merchant-notifications`: {"id": 1758718057224, "name": "@salla.sa/ui-merchant-notifications", "Prod": {}, "env": "prod", "path": "/^/notifications", "position": 47} (SA-S-3576)

### Who decides

- **Shopify**
  - `email-settings`: "eligibility":{"permissions":["PREFERENCES"]} (SH-S-5131)
  - `notification-settings:staff`: "eligibility":{"permissions":["ORDERS"]} (SH-S-5209)
- **Salla**
  - `أرشيف الرسائل النصية`: "extra_icons": null}, {"parent_code": "almzaya-almtkdm", "title": "أرشيف الرسائل النصية", "description": null, "icon": null, "icon_color": null, "icon_backgroun [cut] [scope: plan: سلة بلس] (SA-S-2091)
  - `sms_archive_browse`: "label": "app builder management"}, {"id": 1464104165, "name": "sms_archive_browse", "label": "sms archive browse"}, {"id": 555914214, "name": "sms_archive_mess [cut] (SA-S-2414)
  - `sms_archive_message_view`: "label": "sms archive browse"}, {"id": 555914214, "name": "sms_archive_message_view", "label": "sms archive message view"}, {"id": 1930408679, "name": "store_no [cut] (SA-S-2415)
  - `store_notification_settings_management`: "label": "sms archive message view"}, {"id": 1930408679, "name": "store_notification_settings_management", "label": "store notification settings management"}, { [cut] (SA-S-2416)
  - `sms_archive_browse`: "en": "app builder management"}}, {"id": 1464104165, "key": "sms_archive_browse", "name": {"ar": "استعراض إرشيف الرسائل", "en": "sms archive browse"}}, {"id": 5 [cut] (SA-S-2631)
  - `sms_archive_message_view`: "en": "sms archive browse"}}, {"id": 555914214, "key": "sms_archive_message_view", "name": {"ar": "مشاهدة محتوى الرسائل", "en": "sms archive message view"}}, {" [cut] (SA-S-2632)
  - and 7 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-064

Shopify: SH-C-153 Shopify Inbox (customer chat); Salla: SA-C-099 Salla Chat

Basis: SH-C-153 platform_terms "Shopify Inbox"; platform_terms "Chat with customers" | SA-C-099 platform_terms "Salla Chat"; platform_terms "salla_chat"

### Where it lives

- **Shopify**
  - `Shopify Inbox`: Shopify Inbox [scope: Google Play (publisher Shopify Inc.)] (SH-S-2758)
- **Salla**
  - `Salla Chat`: {"position": 94, "kind": "link", "text": "Salla Chat", "href": "/channel/chat", "parent": 0, "list": 7} (SA-S-1864)
  - `@salla.sa/ui-merchant-chat`: {"id": 1732806043317, "name": "@salla.sa/ui-merchant-chat", "Prod": {}, "env": "prod", "path": "/^/channel/(chat\|whatsapp\|chat-agents)/", "position": 25} (SA-S-3554)
  - `chat-mf`: {"id": 1744718908436, "name": "chat-mf", "Prod": {}, "env": "prod", "path": "/chat-mf", "position": 41} (SA-S-3570)

### Who decides

- **Shopify**
  - `Chat with customers`: {"kind": "row", "section": 1, "position": 51, "cells": [{"tag": "th", "text": "Chat with customers", "scope": "row"}, {"tag": "td", "text": "Included"}, {"tag": [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7039)
- **Salla**
  - `salla_chat`: {"position": 441, "name": "salla_chat", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3402)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **Salla**
  - `ctaDescTwo`: ابقى على اتصال مع عملائك لإدارة استفساراتهم عبر قنوات تواصل متعددة تشمل واتساب وموقع المتجر، دون الحاجة لأدوات خارجية. (SA-S-5138)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)

## M-065

Shopify: SH-C-154 Product reviews; Salla: SA-C-030 Reviews and questions (Reviews; Feedbacks; Questions & Reviews); WooCommerce: WC-C-065 Product reviews and review requests

Basis: SH-C-154 platform_terms "Reviews"; platform_terms "Product review apps" | SA-C-030 platform_terms "Reviews"; platform_terms "review.added"; platform_terms "الأسئلة والتقييمات" | WC-C-065 platform_terms "Reviews"; platform_terms "Product reviews"

### Where it lives

- **Shopify**
  - `Product review apps`: "h1": "Product review apps" (SH-S-2601)
- **Salla**
  - `Reviews`: {"position": 23, "kind": "link", "text": "Reviews", "href": "/feedback"} (SA-S-1699)
  - `Review requests`: "feedback/rating_message":"Review requests" (SA-S-1718)
  - `Thank you message`: "feedback/thanks_message":"Thank you message" (SA-S-1719)
  - `Add media to reviews`: "feedback/image_attachment":"Add media to reviews" (SA-S-1720)
  - `Edit or delete review`: "feedback/update_rating":"Edit or delete review" (SA-S-1721)
  - `Reviews & questions`: {"position": 90, "kind": "link", "text": "Reviews & questions", "href": "/feedback", "parent": 0, "list": 7} (SA-S-1860)
  - and 2 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Products > Reviews`: __( 'Reviews', 'woocommerce' ), (WC-S-0056)
  - `Review request (WC_Email_Customer_Review_Request)`: $this->title = __( 'Review request', 'woocommerce' ); (WC-S-0313)
  - `Automattic\WooCommerce\Internal\OrderReviews`: The feature lives in the `Automattic\WooCommerce\Internal\OrderReviews` namespace and registers its WordPress hooks only when the feature flag is on. [scope: Customer review request] (WC-S-5391)

### Who decides

- **Shopify**: gap (searched, not found)
- **Salla**
  - `الأسئلة والتقييمات`: "sub_features": [{"parent_code": "adar-tgrb-alaamyl", "title": "الأسئلة والتقييمات", "description": null, "icon": null, "icon_color": null, "icon_background": n [cut] [scope: plan: سلة بلس] (SA-S-2071)
  - `إتاحة إضافة صور في تقييم المنتج`: "extra_icons": null}, {"parent_code": "adar-tgrb-alaamyl", "title": "إتاحة إضافة صور في تقييم المنتج", "description": null, "icon": null, "icon_color": null, "i [cut] [scope: plan: سلة بلس] (SA-S-2072)
  - `إرسال رابط التقييم للعميل`: "sub_features": [{"parent_code": "adar-altlbat", "title": "إرسال رابط التقييم للعميل", "description": null, "icon": null, "icon_color": null, "icon_background": [cut] [scope: plan: سلة برو] (SA-S-2127)
  - `reviews_management`: "label": "ask browse review shipping companies"}, {"id": 1742602672, "name": "reviews_management", "label": "reviews management"}, {"id": 834347185, "name": "qu [cut] (SA-S-2311)
  - `questions_management`: "label": "reviews management"}, {"id": 834347185, "name": "questions_management", "label": "questions management"}, {"id": 58740658, "name": "reviews_and_questi [cut] (SA-S-2312)
  - `reviews_and_questions_browse`: "label": "questions management"}, {"id": 58740658, "name": "reviews_and_questions_browse", "label": "reviews and questions browse"}], "position": 5} (SA-S-2313)
  - and 14 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `woocommerce_review_rating_verification_required`: 'desc' => __( 'Reviews can only be left by "verified owners"', 'woocommerce' ), (WC-S-0950)
  - `woocommerce_enable_reviews`: 'id' => 'woocommerce_enable_reviews', 'default' => 'yes', 'type' => 'checkbox', (WC-S-5389)
  - `customer_review_request`: The feature ships **off by default** behind the `customer_review_request` feature flag (beta). Merchants enable it under **WooCommerce → Settings → Advanced → F [cut] (WC-S-5390)

### Who is legally responsible

- **Shopify**
  - `Shop product reviews`: Shop isn't responsible for the content, accuracy, or reliability of the reviews that you receive. [scope: product reviews in the Shop app] (SH-S-7476)
- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: If you install or enable a Third Party Service for use with the Services, you grant us permission to share on your behalf, or allow the applicable Third Party P [cut] [scope: Third Party Services, including Apps via the Shopify App Store] (SH-S-7284)
- **Salla**
  - `Reviews`: "id": 3672516, "name": "Reviews", "key": "apiDetailFolder.3672516", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1039)
  - `Feedbacks`: "id": 841819, "name": "Feedbacks", "key": "apiDetailFolder.841819", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1040)
  - `reviews`: {"id": 19, "slug": "reviews", "icon": "sicon-chat-conversation-alt", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "na [cut] (SA-S-1561)
  - `review.added`: {"id": 1168643479, "slug": "review.added", "url": "https://docs.salla.dev/433815m0#review-added-webhook-event-model", "order": 0, "is_enabled": true, "name": {" [cut] (SA-S-1624)
- **WooCommerce**
  - `wc/v3 > product-reviews`: 'product-reviews' => 'WC_REST_Product_Reviews_Controller', (WC-S-0097)
  - `wc/store/v1 > /products/reviews`: const IDENTIFIER = 'product-reviews'; (WC-S-0173)
  - `Product reviews`: The product reviews API allows you to create, view, update, and delete individual, or a batch, of product reviews. (WC-S-0678)
  - `/review-order/{id}/`: routes `/review-order/{id}/?key={order_key}` to the WC-managed Review Order page and renders it through the `[woocommerce_review_order]` shortcode. [scope: Customer review request] (WC-S-5392)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-066

Shopify: SH-C-155 Merchant support and learning; Salla: SA-C-014 Salla's merchant support and help desk (Self-service system; support plan); WooCommerce: WC-C-062 Support for Woo and Marketplace products

Basis: SH-C-155 platform_terms "24/7 support" | SA-C-014 platform_terms "support-plan"; statement SA-S-5007 "Salla Help Center"; platform_terms "فريقنا معك في كل خطوة" | WC-C-062 platform_terms "WooCommerce Support Policy"

### Where it lives

- **Shopify**
  - `Shopify Community`: "text": "Shopify Community" [scope: accounts.shopify.com destination list] (SH-S-2523)
- **Salla**
  - `مسؤول الحساب`: 1. من قائمة لوحة التحكم الجانبية، في اسفل شعار التاجر اضغط (مسؤول الحساب). [scope: باقة سبيشل] (SA-S-5006)
  - `help.salla.sa`: # مركز المساعدة - سلة (Salla Help Center) (SA-S-5007)
- **WooCommerce**
  - `Public forums`: If you have questions regarding the free, core WooCommerce plugin, please post a question and/or search for answers in the official support forum on WordPress.o [cut] [scope: the free, core WooCommerce plugin] (WC-S-5344)

### Who decides

- **Shopify**
  - `24/7 support`: {"kind": "row", "section": 1, "position": 18, "cells": [{"tag": "th", "text": "24/7 support", "scope": "row"}, {"tag": "td", "text": "Live chat"}, {"tag": "td", [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7015)
  - `Free Shopify Academy courses`: {"kind": "row", "section": 1, "position": 19, "cells": [{"tag": "th", "text": "Free Shopify Academy courses", "scope": "row"}, {"tag": "td", "text": "Included"} [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7016)
- **Salla**
  - `فريقنا معك في كل خطوة`: فريقنا معك في كل خطوة [scope: plan: سلة سبيشل] (SA-S-2194)
  - `مدير حساب مخصص`: مدير حساب مخصص [scope: plan: سلة سبيشل] (SA-S-2196)
  - `intercom-complains`: {"position": 442, "name": "intercom-complains", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3403)
  - `intercom-campaign-complains`: {"position": 443, "name": "intercom-campaign-complains", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3404)
  - `support-plan`: {"position": 490, "name": "support-plan", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3451)
- **WooCommerce**
  - `8. c. Woo: Compatibility, access, updates, and support`: When you purchase Paid Services from WooCommerce.com, you’ll receive access to any necessary downloads along with updates and support (as described in our Suppo [cut] (WC-S-0646)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **Salla**: gap (observation needed)
- **WooCommerce**
  - `WooCommerce Support Policy`: We support products sold on WooCommerce.com (the “Products”), which may be developed by WooCommerce or a third-party developer. (WC-S-0833)
  - `1.1.11`: 1.1.11. For Products listed on the Woo Marketplace, Partner shall provide Product support to Users in accordance with the Woo Support Guidelines, and Partner mu [cut] (WC-S-0582)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **Salla**
  - `support_access.no_request.description`: ستظهر هنا طلبات الوصول المؤقت من فريق الدعم عند طلبك للمساعدة. لا تُمنح صلاحية الوصول إلا بعد موافقتك. (SA-S-5132)
- **WooCommerce**
  - `1.1.11`: 1.1.11. For Products listed on the Woo Marketplace, Partner shall provide Product support to Users in accordance with the Woo Support Guidelines, and Partner mu [cut] (WC-S-0582)
  - `Marketplace developer responsibilities`: If you log a support request for a product made by a Marketplace developer, you will get a reply directly from them. [scope: products made by Marketplace developers] (WC-S-5345)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-067

Shopify: SH-C-156 Apps and third-party services, SH-C-157 Shopify App Store (listing, registration and review); Salla: SA-C-194 App Store and app categories (متجر التطبيقات), SA-C-175 App Store publishing policy for partners; WooCommerce: WC-C-059 Third-party extensions and services (general)

Basis: SH-C-156 platform_terms "Apps"; platform_terms "Third Party Services"; inventory SH-I-2102 "Installing and setting up apps" | SH-C-157 platform_terms "Shopify App Store" | SA-C-194 inventory SA-I-0884 "App Store"; inventory SA-I-0702 "Installed apps"; concern "متجر التطبيقات" | SA-C-175 platform_terms "سياسة الشروط والاستخدام – متجر تطبيقات سلة"; statement SA-S-0023 "يحتفظ فريق سلة بحق مراجعة وقبول أو رفض أي تطبيق يتم تقديمه من قبل المطورين" | WC-C-059 platform_terms "Third-Party Services"; platform_terms "extensions"

### Where it lives

- **Shopify**
  - `apps:embedded_parent`: "path":"apps" (SH-S-5034)
  - `app:grant`: "path":"app/grant" (SH-S-5035)
  - `apps:permissions_error`: "path":"errors/app_permissions" (SH-S-5036)
  - `apps:request_grant`: "path":"oauth/request_grant" (SH-S-5039)
  - `apps`: "title": "Apps" (SH-S-1495)
  - `Apps`: "text": "Apps" (SH-S-1535)
  - and 2 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `Installed apps`: {"position": 26, "kind": "link", "text": "Installed apps", "href": "/apps"} (SA-S-1702)
  - `My apps`: {"position": 113, "kind": "link", "text": "My apps", "href": "/apps/installed", "parent": 0, "list": 10} (SA-S-1883)
  - `App Store`: {"position": 114, "kind": "link", "text": "App Store", "href": "/apps", "parent": 0, "list": 10} (SA-S-1884)
  - `My Apps`: {"position": 3, "kind": "link", "text": "My Apps", "href": "/apps", "list": 2} (SA-S-1906)
  - `@salla.sa/ui-merchant-apps`: {"id": 1728399567489, "name": "@salla.sa/ui-merchant-apps", "Prod": {}, "env": "prod", "path": "/apps", "position": 12} (SA-S-3541)
  - `## 2. What Salla is and is not`: Salla also offers connected products such as Salla Point, Salla Ads, Mahally, an app maker, an app marketplace, and enterprise-oriented services. (SA-S-0002)
  - and 1 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Extensions`: Extensions (WC-S-0694)

### Who decides

- **Shopify**
  - `apps:list`: "eligibility":{"oneOf":[{"permissions":["APPLICATIONS"]},{"permissions":["LIMITED_APPLICATIONS"]}]} (SH-S-5028)
  - `apps:extension_details`: "eligibility":{"betas":["700dab93"],"oneOf":[{"permissions":["APPLICATIONS"]},{"permissions":["LIMITED_APPLICATIONS"]}]} (SH-S-5037)
  - `shopify.dev/docs/api/usage/access-scopes.md`: Merchants approve the scopes when they install it. (SH-S-0755)
  - `9.9 Third Party Services and Third Party Partners`: Shopify does not guarantee the availability of Third Party Services and you acknowledge that Shopify may disable access to any Third Party Services at any time  [cut] (SH-S-0060)
  - `Integrate with 1000s of apps`: {"kind": "row", "section": 1, "position": 68, "cells": [{"tag": "th", "text": "Integrate with 1000s of apps", "scope": "row"}, {"tag": "td", "text": "Included"} [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7052)
  - `Shopify App Pricing, Important note`: All apps published on the Shopify App Store are required to use a Shopify provided billing solution and adhere to the terms and conditions of the [Shopify Partn [cut] (SH-S-0284)
  - and 5 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `marketplace_apps_management`: "label": "store design management"}, {"id": 731002523, "name": "marketplace_apps_management", "label": "marketplace apps management"}, {"id": 92231140, "name":  [cut] (SA-S-2412)
  - `marketplace_apps_management`: "en": "store design management"}}, {"id": 731002523, "key": "marketplace_apps_management", "name": {"ar": "التطبيقات المثبتة", "en": "marketplace apps managemen [cut] (SA-S-2629)
  - `intercom-service`: {"position": 98, "name": "intercom-service", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "featu [cut] [scope: plans: plus, pro, special] (SA-S-3059)
  - `zapier-service`: {"position": 239, "name": "zapier-service", "value": {"enabled": false, "released": true, "plans": ["pro", "special"], "countries": [], "type": "feature"}} [scope: plans: pro, special] (SA-S-3200)
  - `poptin`: {"position": 246, "name": "poptin", "value": {"enabled": false, "released": false, "type": "app", "app_id": null, "plans": ["plus", "pro", "special"], "countrie [cut] [scope: plans: plus, pro, special] (SA-S-3207)
  - `convert-flow`: {"position": 247, "name": "convert-flow", "value": {"enabled": false, "released": false, "type": "app", "app_id": "2055995646", "plans": ["plus", "pro", "specia [cut] [scope: plans: plus, pro, special] (SA-S-3208)
  - and 28 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `1.1.3`: 1.1.3. The Product must be GPL compatible and shall be licensed under the GPL. (WC-S-0577)
  - `11. Third-Party Services`: While using the Services, you may enable, use, or purchase services, products, software, embeds, or applications (like themes, extensions, plugins, blocks, or p [cut] (WC-S-0852)
  - `readme.txt: Grow your business, add features, and monitor your store on the go`: Our developers [vet each new extension] (WC-S-0596)

### Who is legally responsible

- **Shopify**
  - `help.shopify.com/en/manual/apps/apps-by-shopify.md`: Apps that are made by Shopify are usually free and are supported by Shopify. (SH-S-0738)
  - `help.shopify.com/en/manual/apps/apps-by-shopify.md`: Apps that are developed by a third-party developer might have [app charges](/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-cha [cut] (SH-S-0739)
  - `9.9 Third Party Services and Third Party Partners`: Such Third Party Services are made available only as a convenience, and your purchase, access or use of any such Third Party Services is solely between you and  [cut] (SH-S-0058)
  - `9.9 Third Party Services and Third Party Partners`: You acknowledge that Shopify has no control over Third Party Services or Third Party Providers and will not be responsible or liable to you or anyone else for s [cut] (SH-S-0059)
  - `6. Merchant Agreement, Privacy and Data Security, Merchant Agreement and Privacy`: Developer must inform Merchants in the Merchant Agreement that: (i) Developer is solely responsible for the Application; (ii) Shopify is not liable for any faul [cut] (SH-S-0217)
  - `preamble`: The Agreement is between you, as Partner (as defined below in Section A.1.), Shopify Inc. (“Shopify Inc.”) and Shopify Commerce Singapore Pte. Ltd. (“Shopify As [cut] (SH-S-0288)
- **Salla**
  - `المادة (2) – الشروط العامة لاستخدام المتجر`: يتحمل كل من المطور والتاجر مسؤولية استخدامهم للتطبيقات، ولا تتحمل سلة أي مسؤولية عن النتائج الناتجة عن ذلك. (SA-S-0024)
  - `المادة الخامسة-طبيعة التزام منصة سلة`: تقع كامل المسؤولية على الشريك تجاه التجار أو الجهات التنظيمية فيما يخص صحة المحتوى أو مشروعيته أو توافقه مع الأنظمة. (SA-S-0033)
  - `المادة الخامسة-طبيعة التزام منصة سلة`: توفر سلة البنية التحتية التقنية فقط لاستضافة تطبيقات أو خدمات الشركاء، دون أن يُعد ذلك بمثابة "توصية أو تزكية" رسمية لأي منتج أو خدمة. (SA-S-0037)
  - `المادة (11) – حل النزاعات`: في حال نشوء أي نزاع، يتم السعي إلى حله وديًا، وفي حال التعذر يتم رفع النزاع أمام الجهات القضائية المختصة في مدينة جدة، المملكة العربية السعودية. (SA-S-0021)
  - `سياسة الشروط والاستخدام – متجر تطبيقات سلة > المقدّمة`: ترحب منصة "سلّة" المملوكة لشركة تطبيق سلة لتقنية المعلومات (س.ت: 4031200589) (SA-S-0015)
  - `المادة (11) – حل النزاعات`: في حال نشوء أي نزاع، يتم السعي إلى حله وديًا، وفي حال التعذر يتم رفع النزاع أمام الجهات القضائية المختصة في مدينة جدة، المملكة العربية السعودية. (SA-S-0021)
- **WooCommerce**
  - `8. Specific Service Terms: c. Woo (Extensions)`: The software in the extensions available in the Woo Marketplace is licensed under the GNU General Public License (“GPL“). (WC-S-0645)
  - `8. Specific Service Terms: c. Woo (Extensions)`: Extensions may have their own requirements (like requiring a connection to their servers in order to provide their services) and terms that apply. (WC-S-0465)
  - `11. Third-Party Services`: Third-Party Services aren’t vetted, endorsed, or controlled by Automattic. (WC-S-0487)
  - `11. Third-Party Services`: Unless we have indicated that Automattic is providing support for it, any use of a Third-Party Service is at your own risk, and we won’t be responsible or liabl [cut] (WC-S-0656)
  - `Overview of Marketplace developers`: These developers create, maintain, and support their own products. [scope: third-party Marketplace developers] (WC-S-5342)
  - `GDPR compliance guidelines for WooCommerce extensions`: Developers must ensure that WooCommerce extensions are compliant with these regulations. [scope: EU residents' personal data (GDPR)] (WC-S-5343)

### How it meets the rest

- **Shopify**
  - `preamble`: By accessing or using the Shopify API, you agree to this Shopify API License and Terms of Use (“Terms”) with Shopify Inc. and its affiliates (“we”, “our”, “us”  [cut] (SH-S-0214)
  - `app/uninstalled`: "value": "app/uninstalled" (SH-S-1153)
  - `preamble`: The Agreement is between you, as Partner (as defined below in Section A.1.), Shopify Inc. (“Shopify Inc.”) and Shopify Commerce Singapore Pte. Ltd. (“Shopify As [cut] (SH-S-0288)
  - `2. Using the Shopify API`: Developer must obtain an API Client by registering for a Partner Account and agreeing to and complying with the terms and conditions of the Partner Program Agre [cut] (SH-S-0215)
- **Salla**
  - `App Details Builder`: "id": 4811949, "name": "App Details Builder", "key": "apiDetailFolder.4811949", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDi [cut] (SA-S-1075)
  - `المادة (5) – العمولات والدفع`: في حال كان التطبيق مدفوعًا، فإن عملية الدفع تتم عبر منصة سلة وتخضع للعمولات والنسب المعتمدة. (SA-S-0025)
- **WooCommerce**
  - `8. Specific Service Terms: c. Woo (Extensions)`: Extensions may have their own requirements (like requiring a connection to their servers in order to provide their services) and terms that apply. (WC-S-0465)

### Stated reason

- **Shopify**
  - `About billing for your app`: Shopify App Pricing creates a predictable, trustworthy, and standardized experience for app users and makes pricing easier to set up and maintain. (SH-S-0280)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-068

Shopify: SH-C-158 Access scopes granted to apps; Salla: SA-C-191 App access scopes (App Scope)

Basis: SH-C-158 platform_terms "Access scopes" | SA-C-191 concern "App Scope"; statement SA-S-5090 "Set up the App Scope"

### Where it lives

- **Shopify**
  - `Access scopes`: "label": "Access scopes" (SH-S-0795)
- **Salla**
  - `App Scopes Setup`: Set up the App Scope and check the boxes that matches your app scope, such as Product, Order and Webhooks, then click Update Scope. (SA-S-5090)

### Who decides

- **Shopify**
  - `read_checkout_and_accounts_configurations`: Requires `read_checkout_and_accounts_configurations` access scope or `read_checkout_settings` access scope. Also: User must have `manage_checkout_settings` perm [cut] (SH-S-5942)
  - `read_customer_merge`: Requires The user must have `read_customer_merge` permissions. (SH-S-5962)
  - `read_inventory_purchase_orders`: Requires `read_inventory_purchase_orders` access scope. Also: The user must have permission to view purchase orders. (SH-S-6007)
  - `read_shopify_payments`: Requires `read_shopify_payments` access scope or `read_financial_kyc_information` access scope. Also: The app must have the Shopify Payments or Financial KYC In [cut] (SH-S-6120)
  - `write_assigned_fulfillment_orders`: Requires `write_assigned_fulfillment_orders` access scope, `write_merchant_managed_fulfillment_orders` access scope or `write_third_party_fulfillment_orders` ac [cut] (SH-S-6168)
  - `write_assigned_fulfillment_orders`: Requires `write_assigned_fulfillment_orders` access scope. Also: The user must have fulfill\_and\_ship\_orders permission. (SH-S-6169)
  - and 45 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `## OAuth`: Merchants are asked to authorize you, as the service provider, to access only specific portions of their account. (SA-S-0185)

### Who is legally responsible

- **Shopify**
  - `6. Merchant Agreement, Privacy and Data Security`: except as necessary to provide the Application services to the Merchant to whom the Merchant Data relates and as described in the applicable Merchant Agreement  [cut] (SH-S-0220)
- **Salla**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `customer_read_companies`: Requires `customer_read_companies` access scope, `customer_read_customers` access scope, `customer_read_locations` access scope or `customer_read_orders` access [cut] (SH-S-5912)
  - `customer_read_companies`: Requires `customer_read_customers` access scope or `customer_read_companies` access scope. (SH-S-5913)
  - `customer_read_customers`: Requires `customer_read_customers` access scope. (SH-S-5914)
  - `customer_read_customers`: To read or write metafield data on the `CUSTOMER` resource using the Customer Account API, you'll need to include the `customer_read_customers` and `customer_wr [cut] (SH-S-5915)
  - `customer_read_customers`: Metafield writes require `customer_read_customers` and `customer_write_customers` [access scopes](https://shopify.dev/docs/apps/build/cli-for-apps/app-configura [cut] (SH-S-5916)
  - `customer_read_draft_orders`: Requires `customer_read_orders` access scope or `customer_read_draft_orders` access scope. (SH-S-5917)
  - and 352 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `settings`: {"id": 13, "slug": "settings", "icon": "sicon-settings", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_w [cut] (SA-S-1545)
  - `customers`: {"id": 1, "slug": "customers", "icon": "sicon-users", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_writ [cut] (SA-S-1546)
  - `orders`: {"id": 2, "slug": "orders", "icon": "sicon-box", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_write", " [cut] (SA-S-1547)
  - `carts`: {"id": 3, "slug": "carts", "icon": "sicon-shopping", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_write [cut] (SA-S-1548)
  - `branches`: {"id": 4, "slug": "branches", "icon": "sicon-store", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_write [cut] (SA-S-1549)
  - `categories`: {"id": 5, "slug": "categories", "icon": "sicon-inbox-multi", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "re [cut] (SA-S-1550)
  - and 18 more statements in `platforms/salla/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `OAuth 2.0 authorization flow`: By requiring the merchant to grant permission for the App to access their data within specific scope, this process helps to ensure that the store's data is safe [cut] (SA-S-5091)

## M-069

Shopify: SH-C-162 Webhooks (event subscriptions); Salla: SA-C-192 Webhooks: registration, security and conditional webhooks; WooCommerce: WC-C-077 Webhooks

Basis: SH-C-162 platform_terms "Webhooks"; platform_terms "webhook topics" | SA-C-192 platform_terms "Webhooks"; platform_terms "إرسال الإخطارات لخدمات أخرى عبر Webhooks" | WC-C-077 platform_terms "Webhooks"; platform_terms "webhook topics"

### Where it lives

- **Shopify**
  - `Webhooks`: "label": "Webhooks" (SH-S-0791)
  - `notification-settings:webhooks`: "section":"Notifications","path":"webhooks/*","title":{"value":"Webhooks"} (SH-S-7142)
- **Salla**
  - `Developer tools`: {"position": 116, "kind": "link", "text": "Developer tools", "href": "/manage/webhooks", "parent": 0, "list": 10} (SA-S-1886)
  - `Webhooks Log`: {"position": 38, "kind": "link", "text": "Webhooks Log", "href": "/logs", "list": 2} (SA-S-1941)
  - `@salla.sa/ui-merchant-manage`: {"id": 1727862649468, "name": "@salla.sa/ui-merchant-manage", "Prod": {}, "env": "prod", "path": "/^/manage/(custom-urls\|webhooks\|migrate\|complaints\|violation\|c [cut] (SA-S-3533)
  - `Webhooks`: "id": 841782, "name": "Webhooks", "key": "apiDetailFolder.841782", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSet [cut] (SA-S-1068)
- **WooCommerce**
  - `Advanced > Webhooks`: $sections['webhooks'] = __( 'Webhooks', 'woocommerce' ); (WC-S-0025)

### Who decides

- **Shopify**
  - `notification-settings`: "eligibility":{"permissions":["PREFERENCES"]} (SH-S-5131)
- **Salla**
  - `إرسال الإخطارات لخدمات أخرى عبر Webhooks`: "extra_icons": null}, {"parent_code": "almzaya-almtkdm", "title": "إرسال الإخطارات لخدمات أخرى عبر Webhooks", "description": null, "icon": null, "icon_color": n [cut] [scope: plan: سلة برو] (SA-S-2124)
  - `webhook_management`: "label": "tax management"}, {"id": 1613154975, "name": "webhook_management", "label": "webhook management"}, {"id": 839117208, "name": "account_setting_manageme [cut] (SA-S-2408)
  - `webhook_management`: "en": "tax management"}}, {"id": 1613154975, "key": "webhook_management", "name": {"ar": "Webhook", "en": "webhook management"}}, {"id": 839117208, "key": "acco [cut] (SA-S-2625)
  - `webhooks`: {"position": 117, "name": "webhooks", "value": {"enabled": false, "released": true, "plans": ["pro", "special"], "countries": [], "type": "feature"}} [scope: plans: pro, special] (SA-S-3078)
  - `webhook-channel`: {"position": 429, "name": "webhook-channel", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3390)
- **WooCommerce**
  - `Webhooks`: Webhooks let your WooCommerce store send automatic event notifications to a URL of your choice. (WC-S-0885)

### Who is legally responsible

- **Shopify**
  - `API License and Terms of Use`: Developer must inform Merchants in the Merchant Agreement that: (i) Developer is solely responsible for the Application; (ii) Shopify is not liable for any faul [cut] [scope: Developers' Applications] (SH-S-7281)
- **Salla**: gap (stated only in general terms)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `About webhooks`: When your app needs information about specific events that have occurred on a shop, it can subscribe to Shopify webhook topics as a mechanism for receiving near [cut] (SH-S-0685)
  - `How it works`: Verify HMAC signatures and ignore duplicate deliveries using `X-Shopify-Webhook-Id`. (SH-S-0686)
  - `app/uninstalled`: "value": "app/uninstalled" (SH-S-1153)
- **Salla**
  - `Webhooks`: {"position": 7, "pointer": "/7", "depth": 0, "parent": null, "type": "doc", "id": 421119, "name": "Webhooks", "key": "doc.421119", "parentId": 841847, "tags": [ [cut] (SA-S-1008)
  - `Conditional Webhooks`: {"position": 8, "pointer": "/8", "depth": 0, "parent": null, "type": "doc", "id": 421120, "name": "Conditional Webhooks", "key": "doc.421120", "parentId": 84184 [cut] (SA-S-1009)
  - `Webhooks`: "id": 841782, "name": "Webhooks", "key": "apiDetailFolder.841782", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSet [cut] (SA-S-1068)
  - `Webhooks`: "id": 907544, "name": "Webhooks", "key": "apiDetailFolder.907544", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingSetti [cut] (SA-S-1072)
  - `webhooks`: {"id": 8, "slug": "webhooks", "icon": "sicon-arrow-merge", "options": [{"item": "read", "name": "read", "disabled": true}, {"item": "read_write", "name": "read_ [cut] (SA-S-1553)
- **WooCommerce**
  - `wc/v3 > webhooks`: 'webhooks' => 'WC_REST_Webhooks_Controller', (WC-S-0119)
  - `coupon.created`: 'coupon.created' => __( 'Coupon created', 'woocommerce' ), (WC-S-0254)
  - `coupon.updated`: 'coupon.updated' => __( 'Coupon updated', 'woocommerce' ), (WC-S-0255)
  - `coupon.deleted`: 'coupon.deleted' => __( 'Coupon deleted', 'woocommerce' ), (WC-S-0256)
  - `coupon.restored`: 'coupon.restored' => __( 'Coupon restored', 'woocommerce' ), (WC-S-0257)
  - `customer.created`: 'customer.created' => __( 'Customer created', 'woocommerce' ), (WC-S-0258)
  - and 16 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `Security Implementation`: When an event occurs, Salla will send these headers and the relevant details to the specified App along with the token or signature verifies that the request is [cut] (SA-S-5092)
- **WooCommerce**
  - `What are webhooks`: Webhooks are useful for integrating your store with third-party services or other external APIs that support them. (WC-S-0886)

## M-070

Shopify: SH-C-163 Shopify Functions; Salla: SA-C-196 App Functions

Basis: SH-C-163 platform_terms "Shopify Functions"; statement SH-S-0681 "Shopify Functions allow developers to customize the backend logic of Shopify."; statement SH-S-0682 "public apps that are distributed through the Shopify App Store and contain functions" | SA-C-196 platform_terms "App Functions"; statement SA-S-0190 "App Functions are fully managed by Salla"

### Where it lives

- **Shopify**
  - `About Shopify Functions`: Shopify Functions allow developers to customize the backend logic of Shopify. (SH-S-0681)
  - `How Shopify Functions work`: is written in any language that can compile a WebAssembly module (SH-S-0684)
  - `Shopify Functions`: "label": "Shopify Functions" (SH-S-0809)
- **Salla**
  - `App Functions`: {"position": 12, "pointer": "/firstLevelNavbarItems/2", "depth": 0, "parent": null, "type": "folder", "id": "01KR613SBSXNK026G8MEC0DPJB", "title": "App Function [cut] (SA-S-1168)
  - `@salla.sa/app-functions-types`: {"id": 1784033431962, "name": "@salla.sa/app-functions-types", "Prod": {}, "env": "prod", "path": "/{app-name}", "position": 73} (SA-S-3602)
  - `AWB - Getting Started`: There is no need for servers, deployments, infrastructure monitoring, or scaling. App Functions are fully managed by Salla, which reduces operational cost and c [cut] (SA-S-0190)

### Who decides

- **Shopify**
  - `Functions availability`: Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions. (SH-S-0682)
  - `Lifecycle of a Shopify Function`: Shopify Functions are never invoked directly by URL or otherwise. Shopify invokes them as-needed within the customer journey. (SH-S-0683)
  - `Personalize store with custom functions`: {"kind": "row", "section": 1, "position": 99, "cells": [{"tag": "th", "text": "Personalize store with custom functions", "scope": "row"}, {"tag": "td", "text":  [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7076)
- **Salla**
  - `app-functions`: {"position": 118, "name": "app-functions", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3079)
  - `Event types`: **Synchronous Actions** — Execute immediately, **block the user**, must respond in milliseconds (e.g., `shipment.creating`) (SA-S-0189)
  - `Pricing`: App Functions are currently in **beta** and **free of charge**. (SA-S-0188)

### Who is legally responsible

- **Shopify**
  - `API License and Terms of Use`: Developer must inform Merchants in the Merchant Agreement that: (i) Developer is solely responsible for the Application; (ii) Shopify is not liable for any faul [cut] [scope: Developers' Applications] (SH-S-7281)
- **Salla**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `Shopify Functions`: "label": "Shopify Functions" (SH-S-0809)
- **Salla**
  - `Merchants Events`: "id": 5460616, "name": "Merchants Events", "key": "apiDetailFolder.5460616", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDispl [cut] (SA-S-1078)
  - `Customers Events`: "id": 5460615, "name": "Customers Events", "key": "apiDetailFolder.5460615", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDispl [cut] (SA-S-1079)
  - `Order Created`: {"position": 0, "line": 32, "headings": ["Supported Events", "Merchant Actions & Events", "📦 Orders"], "table": 0, "cells": {"Event Name": "**Order Created**",  [cut] (SA-S-1263)
  - `Order Completed`: {"position": 1, "line": 33, "headings": ["Supported Events", "Merchant Actions & Events", "📦 Orders"], "table": 0, "cells": {"Event Name": "**Order Completed**" [cut] (SA-S-1264)
  - `Order Updated`: {"position": 2, "line": 34, "headings": ["Supported Events", "Merchant Actions & Events", "📦 Orders"], "table": 0, "cells": {"Event Name": "**Order Updated**",  [cut] (SA-S-1265)
  - `Order Status Updated`: {"position": 3, "line": 35, "headings": ["Supported Events", "Merchant Actions & Events", "📦 Orders"], "table": 0, "cells": {"Event Name": "**Order Status Updat [cut] (SA-S-1266)
  - and 73 more statements in `platforms/salla/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `App Functions > Welcome`: Write serverless functions that execute automatically when specific events occur in a store - no infrastructure to manage, automatic scaling (SA-S-0187)

## M-071

Shopify: SH-C-168 Shopify Partner Program and Partner Dashboard; Salla: SA-C-204 Partner account, ID verification and employees (Salla Partners portal), SA-C-176 Contract a partner signs to publish an app, SA-C-193 App lifecycle events (App Events)

Basis: SH-C-168 platform_terms "Partner Terms of Service"; platform_terms "Partner Dashboard"; inventory SH-I-0075 "App Events API" | SA-C-204 platform_terms "Developer Portal"; platform_terms "Partners Resources" | SA-C-176 platform_terms "سياسة الانضمام إلى برنامج شركاء سلة" | SA-C-193 statement SA-S-5093 "App Events"

### Where it lives

- **Shopify**
  - `Partner API`: "label": "Partner API" (SH-S-0838)
  - `Shopify Partners`: "text": "Shopify Partners" [scope: accounts.shopify.com destination list] (SH-S-2521)
- **Salla**
  - `Developer Portal`: {"position": 27, "pointer": "/navRightLinkItems/3", "depth": 0, "parent": null, "type": "button", "key": "button-3-https://salla.partners/", "name": "Developer  [cut] (SA-S-1183)
  - `Dashboard`: {"position": 2, "kind": "link", "text": "Dashboard", "href": "/dashboard", "list": 2} (SA-S-1905)
  - `Employees`: {"position": 31, "kind": "link", "text": "Employees", "href": "/employees", "list": 2} (SA-S-1934)
  - `Settings`: {"position": 36, "kind": "link", "text": "Settings", "href": "/settings", "list": 2} (SA-S-1939)
  - `Chats`: {"position": 39, "kind": "link", "text": "Chats", "href": "/conversations", "list": 2} (SA-S-1942)
  - `Message Center`: {"position": 40, "kind": "link", "text": "Message Center", "href": "/message-center", "list": 2} (SA-S-1943)
  - and 5 more statements in `platforms/salla/statements.tsv`

### Who decides

- **Shopify**
  - `2. Using the Shopify API`: Developer must obtain an API Client by registering for a Partner Account and agreeing to and complying with the terms and conditions of the Partner Program Agre [cut] (SH-S-0215)
- **Salla**
  - `المادة الثالثة – شروط قبول و تسجيل الشركاء`: ١. هوية واضحة: يجب تقديم بيانات شخصية/قانونية واضحة مع إثبات الهوية للمؤسسات أو الأفراد. (SA-S-0036)
  - `المادة الثانية – أهلية الشريك القانونية`: إذا كان الشريك كيانًا نظاميًا (شركة أو مؤسسة)، فيجب أن يكون مرخصًا ومصرحًا له بممارسة النشاط التجاري ذي العلاقة. (SA-S-0035)
  - `المادة السابعة – التعديلات على السياسة`: • تحتفظ منصة سلة بحق تعديل شروط هذه الاتفاقية في أي وقت. (SA-S-5084)
  - `Test App Events`: To test the app events in demo stores, save the app as a draft after setting the app price(s). [scope: demo stores] (SA-S-5094)

### Who is legally responsible

- **Shopify**
  - `preamble`: The Agreement is between you, as Partner (as defined below in Section A.1.), Shopify Inc. (“Shopify Inc.”) and Shopify Commerce Singapore Pte. Ltd. (“Shopify As [cut] (SH-S-0288)
  - `Part A, Section 2.2`: (ii) Partner is not resident or located in or organized under the laws of an Unsupported Region. (SH-S-0297)
- **Salla**
  - `التزامات الشركاء العامة`: • يلتزم الشريك بالحفاظ على سرية بيانات حسابه وعدم مشاركتها مع أي طرف ثالث والامتثال لسياسات الخصوصية وحماية البيانات واتفاقية الاستخدام و سياسات الدفع و جميع ال [cut] (SA-S-5097)
  - `سياسة الانضمام إلى برنامج شركاء سلة > تمهيد`: ترحّب بكم منصة شركاء سلّة، التابعة لمنصة سلّة والمملوكة لشركة تطبيق سلّة لتقنية المعلومات، والمسجلة لدى وزارة التجارة في المملكة العربية السعودية بالسجل التجاري [cut] (SA-S-0016)

### How it meets the rest

- **Shopify**
  - `Organization`: "name": "Organization", "kind": "OBJECT", "description": "A Partner organization." [scope: Partner API 2025-10] (SH-S-7463)
- **Salla**
  - `المادة السادسة – الاتصالات الرسمية`: • يتوفر دعم فني وتجاري مخصص لجميع الشركاء تعتبر المراسلات عبر البريد الإلكتروني أو منصة الشركاء وسائل تواصل رسمية وملزمة. (SA-S-5098)
  - `SaaS contract _ individual _.docx`: "contract":{"app_id":1080110626,"name":"SaaS contract _ individual _.docx (SA-S-0213)
  - `data.is_signable_publication`: "is_signable_publication":true (SA-S-0214)
  - `app.uninstalled`: {"id": 1535775013, "slug": "app.uninstalled", "url": "https://docs.salla.dev/doc-421413/?nav=01HNA8M216X4HFNGWM9TWSTCKQ#app-uninstall", "order": 3, "is_enabled" [cut] (SA-S-1569)
  - `app.trial.started`: {"id": 243601858, "slug": "app.trial.started", "url": "https://docs.salla.dev/doc-421413/?nav=01HNA8M216X4HFNGWM9TWSTCKQ#app-trial-start", "order": 4, "is_enabl [cut] (SA-S-1570)
  - `app.trial.expired`: {"id": 710552341, "slug": "app.trial.expired", "url": "https://docs.salla.dev/doc-421413/?nav=01HNA8M216X4HFNGWM9TWSTCKQ#app-trial-expire", "order": 5, "is_enab [cut] (SA-S-1571)
  - and 10 more statements in `platforms/salla/statements.tsv`

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `المادة الخامسة-طبيعة التزام منصة سلة`: • تقوم سلة بمراجعة طلبات الانضمام والتحقق من أهلية الشركاء قبل قبولهم، كما تتابع أداء الشركاء بعد انضمامهم لضمان الالتزام بالمعايير الفنية والأخلاقية المنصوص عل [cut] (SA-S-5099)

## M-072

Shopify: SH-C-170 Partner and expert services hired by merchants; Salla: SA-C-205 Merchant services marketplace (Merchant Services; Experts)

Basis: SH-C-170 platform_terms "Expert services fees"; statement SH-S-7146 "book-shopify-expert-intro-call" | SA-C-205 platform_terms "expert-marketplace"; platform_terms "Services"; statement SA-S-1885 "/manage/experts"

### Where it lives

- **Shopify**
  - `subscribe:book-shopify-expert-intro-call`: "section":"Billing","path":"book-shopify-expert-intro-call","title":{"value":"Schedule intro call"} (SH-S-7146)
  - `subscribe:bring-your-own-partner`: "section":"Billing","path":"bring-your-own-partner","title":{"value":"Bring your own partner"} (SH-S-7147)
- **Salla**
  - `Merchant ServicesEssentials`: {"position": 115, "kind": "link", "text": "Merchant ServicesEssentials", "href": "/manage/experts", "parent": 0, "list": 10} (SA-S-1885)
  - `Services`: {"position": 8, "kind": "link", "text": "Services", "href": "/service", "parent": 7, "list": 4} (SA-S-1911)
  - `Orders Center`: {"position": 9, "kind": "link", "text": "Orders Center", "href": "/services/orders", "parent": 7, "list": 4} (SA-S-1912)
  - `Service Provider Portfolio`: {"position": 10, "kind": "link", "text": "Service Provider Portfolio", "href": "/services-provider-portfolio", "parent": 7, "list": 4} (SA-S-1913)
  - `@salla.sa/ui-merchant-services`: {"id": 1728381120545, "name": "@salla.sa/ui-merchant-services", "Prod": {}, "env": "prod", "path": "/^/(marketing/influencers\|manage/experts)/", "position": 8} (SA-S-3537)

### Who decides

- **Shopify**: gap (observation needed)
- **Salla**
  - `expert-marketplace`: {"position": 230, "name": "expert-marketplace", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3191)
  - `expert-influencer-home`: {"position": 233, "name": "expert-influencer-home", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3194)
  - `recommended-services`: {"position": 234, "name": "recommended-services", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3195)
  - `external-services`: {"position": 237, "name": "external-services", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3198)
  - `services-redesign`: {"position": 459, "name": "services-redesign", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3420)
  - `partners-chat`: {"position": 461, "name": "partners-chat", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3422)
  - and 6 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `Partner Directory, Relationship`: The services provided by a Partner via the Partner Directory are the responsibility of the Partner and not of Shopify. (SH-S-0760)
  - `Partner Directory, Relationship`: It is the Partner’s responsibility to ensure that there is a Merchant Agreement in place between the Partner and Merchant (SH-S-0761)
- **Salla**
  - `المادة الأولى – المقدّمة والتعريفات`: مزود الخدمة: الشريك الذي يقدم خدماته لتجار سلة من خلال منصة الشركاء، ويُعد طرفًا مستقلاً. (SA-S-0198)
  - `المادة الخامسة-طبيعة التزام منصة سلة`: تعمل منصة الشركاء كوسيط رقمي يربط بين الشريك (مطور/مزود خدمة/مسوق) وبين تجار سلة، دون أن تكون طرفًا مباشرًا في العلاقة التعاقدية بين الطرفين، ما لم ينص على خلاف [cut] (SA-S-0032)

### How it meets the rest

- **Shopify**
  - `Partner Directory, Relationship`: It is the Partner’s responsibility to ensure that there is a Merchant Agreement in place between the Partner and Merchant (SH-S-0761)
- **Salla**
  - `سياسة تقديم الخدمات في منصة الشركاء`: • يجب أن تكون كافة المحادثات التي تتم بين الشريك والتاجر طالب الخدمة عن طريق وسائل التواصل المتوفرة داخل منصة الشركاء فقط وأن أي نشر معلومات الاتصال الشخصية (ال [cut] (SA-S-5100)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `service.infoBanner.listSubTitle1`: كافة مزوِّدي الخدمات موثّقون، ويكون التعامل بإشراف سلة لضمان التزام الطرفين. (SA-S-5101)

## M-073

Shopify: SH-C-171 API platform conventions (versioning, limits, bulk operations, IDs); Salla: SA-C-201 API rate limits, SA-C-202 API versioning and changelog; WooCommerce: WC-C-078 REST API, API keys and settings API

Basis: SH-C-171 platform_terms "Versioning"; platform_terms "API rate limits"; inventory SH-I-0030 "API authentication"; inventory SH-I-0050 "REST Admin API (legacy)" | SA-C-201 platform_terms "Rate Limiting" | SA-C-202 platform_terms "Versioning" | WC-C-078 platform_terms "WooCommerce REST API"; inventory WC-I-0457 "Authentication"

### Where it lives

- **Shopify**
  - `Versioning`: "label": "Versioning" (SH-S-0793)
  - `Bulk operations`: "label": "Bulk operations" (SH-S-0770)
- **Salla**
  - `Change Log`: {"position": 11, "pointer": "/firstLevelNavbarItems/1/children/6", "depth": 1, "parent": "01HNA8Q9YTZGTHZYF36EYDJEWD", "type": "link", "id": "01HPF3F3YKNEJ5FBDS [cut] (SA-S-1167)
- **WooCommerce**
  - `Advanced`: $this->label = __( 'Advanced', 'woocommerce' ); (WC-S-0011)
  - `Advanced > REST API keys`: 'keys' => __( 'REST API keys', 'woocommerce' ), (WC-S-0023)
  - `Advanced > REST API caching`: $sections['rest_api_caching'] = __( 'REST API caching', 'woocommerce' ); (WC-S-0024)
  - `Advanced > Legacy API`: $sections['legacy_api'] = __( 'Legacy API', 'woocommerce' ); (WC-S-0026)

### Who decides

- **Shopify**
  - `About Shopify API versioning`: Shopify releases new API versions on a predictable quarterly schedule, giving you time to adopt changes before older versions are retired. (SH-S-0690)
  - `Versioned and unversioned APIs`: Unversioned APIs and surfaces may change at any time. (SH-S-0691)
  - `Rate limits`: Shopify may temporarily reduce API rate limits to protect platform stability. (SH-S-0688)
  - `The leaky bucket algorithm`: Each app has access to a bucket. Its size is set by the API and by your plan. (SH-S-0689)
  - `API rate limits`: {"kind": "row", "section": 1, "position": 71, "cells": [{"tag": "th", "text": "API rate limits", "scope": "row"}, {"tag": "td", "text": "Standard"}, {"tag": "td [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7055)
  - `Up to 500% higher API call limits`: {"kind": "row", "section": 1, "position": 97, "cells": [{"tag": "th", "text": "Up to 500% higher API call limits", "scope": "row"}, {"tag": "td", "text": "Not i [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7075)
- **Salla**
  - `## 📊 **Rate Limit Plans**`: Rate limits vary based on the store subscribed plan. Use the table below for details: (SA-S-0171)
  - `## ⚠️ **Important Notes**`: Exceeding rate limits or exhibiting unusual behavior may result in **temporary access restrictions**. (SA-S-0173)
  - `### When to Add a New Version?`: APIs should only be versioned up when a breaking change occurs. (SA-S-0207)
- **WooCommerce**
  - `WooCommerce REST API`: Most integrations require you to generate API keys in WooCommerce and enter them in the external service to establish the connection. (WC-S-0888)
  - `rest_api_caching`: 'enabled_by_default' => false, 'is_experimental' => true, 'disable_ui' => false, (WC-S-5414)

### Who is legally responsible

- **Shopify**
  - `What we value, Respect our merchants`: You’ll still own your app, but Shopify owns the platform. As owners of the platform, we put reasonable limits on the use of the merchant data it allows you to a [cut] (SH-S-0221)
- **Salla**: gap (stated only in general terms)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `bulk_operations/finish`: "value": "bulk_operations/finish" (SH-S-1158)
- **Salla**
  - `Rate Limiting`: {"position": 0, "pointer": "/0", "depth": 0, "parent": null, "type": "doc", "id": 421125, "name": "Rate Limiting", "key": "doc.421125", "parentId": 841847, "tag [cut] (SA-S-1001)
  - `Versioning`: {"position": 1, "pointer": "/1", "depth": 0, "parent": null, "type": "doc", "id": 421126, "name": "Versioning", "key": "doc.421126", "parentId": 841847, "tags": [cut] (SA-S-1002)
  - `Change Log`: {"position": 13, "pointer": "/13", "depth": 0, "parent": null, "type": "doc", "id": 421127, "name": "Change Log", "key": "doc.421127", "parentId": 841847, "tags [cut] (SA-S-1014)
  - `# Versioning`: To effectively manage the impact of these changes, we have implemented URI versioning. (SA-S-0208)
- **WooCommerce**
  - `wc/v1`: 'wc/v1' => wc_rest_should_load_namespace( 'wc/v1' ) ? $this->get_v1_controllers() : array(), (WC-S-0076)
  - `wc/v2`: 'wc/v2' => wc_rest_should_load_namespace( 'wc/v2' ) ? $this->get_v2_controllers() : array(), (WC-S-0077)
  - `wc/v3`: 'wc/v3' => wc_rest_should_load_namespace( 'wc/v3' ) ? $this->get_v3_controllers() : array(), (WC-S-0078)
  - `wc/v4`: $namespaces['wc/v4'] = $this->get_v4_controllers(); (WC-S-0080)
  - `wc/v3 > settings`: 'settings' => 'WC_REST_Settings_Controller', (WC-S-0111)
  - `wc/v3 > settings-options`: 'settings-options' => 'WC_REST_Setting_Options_Controller', (WC-S-0112)
  - and 12 more statements in `platforms/woocommerce/statements.tsv`

### Stated reason

- **Shopify**
  - `Rate limits`: Rate limits keep the platform stable and fair for everyone. (SH-S-0687)
- **Salla**
  - `# Rate Limiting`: To ensure Salla remains stable and fair for everyone, all APIs are rate-limited. (SA-S-0172)
  - `# Versioning`: To effectively manage the impact of these changes, we have implemented URI versioning. (SA-S-0208)
- **WooCommerce**: gap (searched, not found)

## M-074

Shopify: SH-C-186 Subscriptions and selling plans; Salla: SA-C-125 Recurring payments and subscriptions sold by stores (Recurring Payments API; Subscriptions); WooCommerce: WC-C-100 Subscriptions (recurring billing)

Basis: SH-C-186 platform_terms "Subscription apps"; platform_terms "subscription_contracts/create" | SA-C-125 platform_terms "subscriptions"; platform_terms "subscription.created"; platform_terms "Recurring Payments API" | WC-C-100 platform_terms "Subscriptions"

### Where it lives

- **Shopify**
  - `About subscriptions`: Subscription apps enable developers and merchants to build subscription experiences directly into Shopify's ecosystem. (SH-S-0763)
  - `Subscription apps`: "h1": "Subscription apps" (SH-S-2657)
- **Salla**
  - `Recurring Payments API`: {"position": 17, "pointer": "/firstLevelNavbarItems/3/children/3", "depth": 1, "parent": "01HN8M90ZXYSEZY11QTKPSM7KK", "type": "folder", "id": "01K8GCHYV0AB54K8 [cut] (SA-S-1173)
- **WooCommerce**
  - `Extensions > Merchandising > Subscriptions`: Subscriptions (WC-S-0739)
  - `WooCommerce > Settings > Subscriptions`: Subscriptions General Settings: Explains all the settings you'll find in WooCommerce > Settings > Subscriptions. [scope: WooCommerce Subscriptions] (WC-S-5350)

### Who decides

- **Shopify**
  - `write_own_subscription_contracts`: Requires `write_products` access scope as well as any of `write_own_subscription_contracts`, `write_purchase_options` access scopes. Also: The user must have `m [cut] (SH-S-6254)
  - `write_own_subscription_contracts`: Requires `write_own_subscription_contracts` access scope. Also: The user must have manage\_orders\_information permission. (SH-S-6255)
  - `Subscriptions on Shopify POS, POS limitations`: Subscriptions on POS require Shopify Payments. POS stores that don't use Shopify Payments can't sell subscriptions. (SH-S-0593)
  - `product:purchase_options:update`: "eligibility":{"permissions":["PRODUCTS"]} (SH-S-5019)
  - `customer-subscriptions:show`: "eligibility":{"clients":["native"],"permissions":["ORDERS"]} (SH-S-5144)
- **Salla**
  - `recurring-payment`: {"position": 340, "name": "recurring-payment", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3301)
  - `recurring-apple-pay`: {"position": 341, "name": "recurring-apple-pay", "value": {"enabled": true, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3302)
  - `## Enabling Recurring Payments`: By default, Recurring Payments are **disabled** for all stores. Only merchants or authorized third-party apps can enable this feature. (SA-S-0195)
- **WooCommerce**
  - `Introduction to WooCommerce Subscriptions`: WooCommerce Subscriptions is a premium extension that allows you to sell products and services with recurring payments. [scope: WooCommerce Subscriptions] (WC-S-5351)

### Who is legally responsible

- **Shopify**
  - `How do subscriptions work?, Subscription contracts`: A subscription contract is the agreement between a customer and a merchant over a specific term for recurring purchases over a set or undefined period of time. (SH-S-0762)
- **Salla**: gap (stated only in general terms)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `read_own_subscription_contracts`: The webhook topic for `subscription_billing_attempts/challenged` events. Occurs when the financial instutition challenges the subscripttion billing attempt char [cut] (SH-S-6071)
  - `read_own_subscription_contracts`: The webhook topic for `subscription_billing_attempts/failure` events. Occurs whenever a subscription billing attempt fails. Requires the `read_own_subscription_ [cut] (SH-S-6072)
  - `read_own_subscription_contracts`: The webhook topic for `subscription_billing_attempts/success` events. Occurs whenever a subscription billing attempt succeeds. Requires the `read_own_subscripti [cut] (SH-S-6073)
  - `read_own_subscription_contracts`: The webhook topic for `subscription_billing_cycle_edits/create` events. Occurs whenever a subscription contract billing cycle is edited. Requires the `read_own_ [cut] (SH-S-6074)
  - `read_own_subscription_contracts`: The webhook topic for `subscription_billing_cycle_edits/delete` events. Occurs whenever a subscription contract billing cycle edit is deleted. Requires the `rea [cut] (SH-S-6075)
  - `unauthenticated_read_selling_plans`: Requires `unauthenticated_read_selling_plans` access scope. (SH-S-6161)
  - and 8 more statements in `platforms/shopify/statements.tsv`
- **Salla**
  - `APIs`: "id": 7100503, "name": "APIs", "key": "apiDetailFolder.7100503", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingSetting [cut] (SA-S-1100)
  - `subscriptions`: {"id": 26, "slug": "subscriptions", "icon": "sicon-chat-conversation-alt", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write [cut] (SA-S-1567)
  - `subscription.updated`: {"id": 1621374331, "slug": "subscription.updated", "url": "https://docs.salla.dev/1650531m0", "order": 11, "is_enabled": true, "name": {"ar": "تم تحديث الاشتراك [cut] (SA-S-1641)
  - `subscription.created`: {"id": 886585575, "slug": "subscription.created", "url": "https://docs.salla.dev/1650531m0", "order": 21, "is_enabled": true, "name": {"ar": "تم انشاء اشتراك",  [cut] (SA-S-1642)
  - `subscription.charge.succeeded`: {"id": 1809005444, "slug": "subscription.charge.succeeded", "url": "https://docs.salla.dev/1650531m0", "order": 21, "is_enabled": true, "name": {"ar": "تم دفع ا [cut] (SA-S-1643)
  - `subscription.charge.failed`: {"id": 514734625, "slug": "subscription.charge.failed", "url": "https://docs.salla.dev/1650531m0", "order": 21, "is_enabled": true, "name": {"ar": "فشلت عملية ا [cut] (SA-S-1644)
  - and 1 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `woocommerce_scheduled_subscription_payment`: Description: Fired once when a subscription renewal payment should be processed. [scope: WooCommerce Subscriptions] (WC-S-5469)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-075

Shopify: SH-C-187 Loyalty, rewards, wishlists and donations; Salla: SA-C-064 Loyalty program (Loyalty program / برنامج الولاء; Loyalty Points)

Basis: SH-C-187 platform_terms "Loyalty and reward apps"; platform_terms "Customer loyalty apps" | SA-C-064 platform_terms "Loyalty program"; platform_terms "Loyalty Points"; concern "Loyalty program / برنامج الولاء"

### Where it lives

- **Shopify**
  - `Customer loyalty apps`: "h1": "Customer loyalty apps" (SH-S-2581)
  - `Donation apps`: "h1": "Donation apps" (SH-S-2583)
- **Salla**
  - `Loyalty programNew`: {"position": 20, "kind": "link", "text": "Loyalty programNew", "href": "/loyalty-program"} (SA-S-1696)
  - `Program details`: "loyalty-program/general":"Program details" (SA-S-1731)
  - `Points settings`: "loyalty-program/points-settings":"Points settings" (SA-S-1732)
  - `Rewards banner`: "loyalty-program/prize-promotion":"Rewards banner" (SA-S-1733)
  - `Markets`: "loyalty-program/markets-activation":"Markets" (SA-S-1734)
  - `Loyalty program`: {"position": 53, "kind": "link", "text": "Loyalty program", "href": "/marketing/loyalty", "parent": 0, "list": 3} (SA-S-1823)
  - and 2 more statements in `platforms/salla/statements.tsv`

### Who decides

- **Shopify**
  - `shopify.dev/docs/api/usage/access-scopes.md`: Merchants approve the scopes when they install it. (SH-S-0755)
- **Salla**
  - `نظام ولاء العملاء *برسوم إضافية`: "extra_icons": null}, {"parent_code": "adoat-altsoyk", "title": "نظام ولاء العملاء *برسوم إضافية", "description": null, "icon": null, "icon_color": null, "icon_ [cut] [scope: plan: سلة بلس] (SA-S-2016)
  - `loyalty_system_management`: "label": "affiliate management"}, {"id": 448961677, "name": "loyalty_system_management", "label": "loyalty system management"}, {"id": 172494834, "name": "swepl [cut] (SA-S-2362)
  - `loyalty_system_management`: "en": "affiliate management"}}, {"id": 448961677, "key": "loyalty_system_management", "name": {"ar": "إدارة نظام الولاء", "en": "loyalty system management"}}, { [cut] (SA-S-2579)
  - `loyalty-system`: {"position": 274, "name": "loyalty-system", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature [cut] [scope: plans: plus, pro, special] (SA-S-3235)
  - `loyalty-system-v2`: {"position": 275, "name": "loyalty-system-v2", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feat [cut] [scope: plans: plus, pro, special] (SA-S-3236)
  - `loyalty-free-product-pos`: {"position": 276, "name": "loyalty-free-product-pos", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type [cut] [scope: plans: plus, pro, special] (SA-S-3237)

### Who is legally responsible

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: Such Third Party Services are made available only as a convenience, and your purchase, access or use of any such Third Party Services is solely between you and  [cut] (SH-S-0058)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: If you install or enable a Third Party Service for use with the Services, you grant us permission to share on your behalf, or allow the applicable Third Party P [cut] [scope: Third Party Services, including Apps via the Shopify App Store] (SH-S-7284)
- **Salla**
  - `Loyalty Points`: "id": 2604936, "name": "Loyalty Points", "key": "apiDetailFolder.2604936", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDispl [cut] (SA-S-1070)
  - `Loyalty`: "id": 849356, "name": "Loyalty", "key": "apiDetailFolder.849356", "shareSettings": {"directoryTreeDisplayStyle": "MODULE_TITLE", "folderContentsDisplayingSettin [cut] (SA-S-1141)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-076

Shopify: SH-C-190 Digital goods, events and token-gating; Salla: SA-C-024 Digital products and digital cards (Digitals Product; Digital card history)

Basis: SH-C-190 inventory SH-I-1886 "Digital product apps"; platform_terms "Digital goods and service apps" | SA-C-024 platform_terms "Digitals Product"; platform_terms "digital-product-settings"; platform_terms "إرسال محتوى المنتجات الرقمية"

### Where it lives

- **Shopify**
  - `blockchain`: "path":"nft-application" (SH-S-5094)
  - `Digital goods and service apps`: "h1": "Digital goods and service apps" (SH-S-2648)
  - `Blockchain`: "section":"Blockchain" (SH-S-1550)
- **Salla**
  - `Digital card history`: {"position": 124, "kind": "link", "text": "Digital card history", "href": "/products/card-logs", "parent": 0, "list": 11} (SA-S-1894)
  - `Digitals Product`: "id": 841794, "name": "Digitals Product", "key": "apiDetailFolder.841794", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDispl [cut] (SA-S-1029)

### Who decides

- **Shopify**
  - `blockchain`: "eligibility":{"permissions":["APPLICATIONS"]} (SH-S-5095)
  - `shopify.dev/docs/api/usage/access-scopes.md`: Merchants approve the scopes when they install it. (SH-S-0755)
- **Salla**
  - `إرسال محتوى المنتجات الرقمية`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "إرسال محتوى المنتجات الرقمية", "description": null, "icon": null, "icon_color": null, "icon_back [cut] [scope: plan: سلة بلس] (SA-S-1999)
  - `browse_digital_codes_logs`: "label": "brands management"}, {"id": 797092607, "name": "browse_digital_codes_logs", "label": "browse digital codes logs"}, {"id": 1651844564, "name": "pre_ord [cut] (SA-S-2261)
  - `browse_digital_codes_logs`: "en": "brands management"}}, {"id": 797092607, "key": "browse_digital_codes_logs", "name": {"ar": "الاطلاع على سجل الاكواد الرقمية", "en": "browse digital codes [cut] (SA-S-2478)
  - `digital-code`: {"position": 535, "name": "digital-code", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"} [cut] [scope: plans: plus, pro, special] (SA-S-3496)
  - `digital-file`: {"position": 537, "name": "digital-file", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"} [cut] [scope: plans: plus, pro, special] (SA-S-3498)
  - `digital-product-settings`: {"position": 538, "name": "digital-product-settings", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type" [cut] [scope: plans: plus, pro, special] (SA-S-3499)

### Who is legally responsible

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: Such Third Party Services are made available only as a convenience, and your purchase, access or use of any such Third Party Services is solely between you and  [cut] (SH-S-0058)
- **Salla**: gap (observation needed)

### How it meets the rest

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: If you install or enable a Third Party Service for use with the Services, you grant us permission to share on your behalf, or allow the applicable Third Party P [cut] [scope: Third Party Services, including Apps via the Shopify App Store] (SH-S-7284)
- **Salla**
  - `Digitals Product`: "id": 841794, "name": "Digitals Product", "key": "apiDetailFolder.841794", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDispl [cut] (SA-S-1029)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (observation needed)

## M-077

Shopify: SH-C-191 Accounting and ERP; Salla: SA-C-210 Accounting, finance and ERP integrations (Accounting & Finance; ERP system apps)

Basis: SH-C-191 platform_terms "Accounting apps"; platform_terms "ERP apps" | SA-C-210 platform_terms "Accounting & Finance"; platform_terms "ERP system"; platform_terms "الربط مع الخدمات المحاسبية"

### Where it lives

- **Shopify**
  - `Accounting apps`: "h1": "Accounting apps" (SH-S-2706)
  - `ERP apps`: "h1": "ERP apps" (SH-S-2613)
- **Salla**
  - `Accounting & Finance`: {"id": 1984760154, "name": "Accounting & Finance", "type": "app", "position": 7} (SA-S-1194)
  - `ERP system`: {"id": 1289165728, "name": "ERP system", "type": "app", "position": 8} (SA-S-1195)
  - `Accounting & Finance`: {"id": 7, "slug": "accounting", "icon": "dollar-coin-stack", "color": "pink", "type": "app", "featured": true, "order": 2, "hidden": false, "name": {"ar": "المح [cut] (SA-S-1222)

### Who decides

- **Shopify**
  - `shopify.dev/docs/api/usage/access-scopes.md`: Merchants approve the scopes when they install it. (SH-S-0755)
- **Salla**
  - `الربط مع الخدمات المحاسبية`: "sub_features": []}, {"title": "الربط مع الخدمات المحاسبية", "description": "أدر شؤونك المالية مثل القوائم والضرائب عبر خدمات مالية متوافقة مع هيئة الزكاة والضر [cut] [scope: plan: سلة برو] (SA-S-2148)
  - `ربط المتجر بخدمات محاسبية ومالية متكاملة`: "sub_features": []}, {"title": "ربط المتجر بخدمات محاسبية ومالية متكاملة", "description": "عزّز ظهور صفحات منتجاتك عند البحث عنها في محركات البحث مثل Google", " [cut] [scope: plan: سلة برو] (SA-S-2152)
  - `ربط تكاملي ذكي`: ربط تكاملي ذكي [scope: plan: سلة سبيشل] (SA-S-2188)
  - `daftra-service`: {"position": 14, "name": "daftra-service", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature" [cut] [scope: plans: plus, pro, special] (SA-S-2975)
  - `qoyod-service`: {"position": 33, "name": "qoyod-service", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"} [cut] [scope: plans: plus, pro, special] (SA-S-2994)
  - `zoho-books-service`: {"position": 132, "name": "zoho-books-service", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "fea [cut] [scope: plans: plus, pro, special] (SA-S-3093)
  - and 1 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: Such Third Party Services are made available only as a convenience, and your purchase, access or use of any such Third Party Services is solely between you and  [cut] (SH-S-0058)
- **Salla**: gap (stated only in general terms)

### How it meets the rest

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: If you install or enable a Third Party Service for use with the Services, you grant us permission to share on your behalf, or allow the applicable Third Party P [cut] [scope: Third Party Services, including Apps via the Shopify App Store] (SH-S-7284)
- **Salla**
  - `مزامنة المخزون مع الخدمات الخارجية`: عُدلت كمية المنتج عبر مزامنة المخزون مع شركات الشحن أو الأنظمة المحاسبية. (SA-S-5145)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**: gap (searched, not found)

## M-078

Shopify: SH-C-195 Mobile app builders; Salla: SA-C-094 Store mobile app (App Maker / صانع التطبيقات)

Basis: SH-C-195 platform_terms "Mobile app builder apps" | SA-C-094 platform_terms "Mobile app"; platform_terms "App Maker"; platform_terms "صانع التطبيقات"; statement SA-S-0008 "Salla App Maker lets eligible merchants create a branded mobile commerce app connected to their Salla store."

### Where it lives

- **Shopify**
  - `Mobile app builder apps`: "h1": "Mobile app builder apps" (SH-S-2701)
- **Salla**
  - `App Maker`: {"id": 488637663, "name": "App Maker", "type": "app", "position": 17} (SA-S-1204)
  - `Mobile app`: {"position": 67, "kind": "link", "text": "Mobile app", "href": "/channel/mobile", "parent": 0, "list": 4} (SA-S-1837)
  - `@salla.sa/ui-merchant-app-maker`: {"id": 1738627452779, "name": "@salla.sa/ui-merchant-app-maker", "Prod": {}, "env": "prod", "path": "/^/channel/mobile(?!/editor(/\|$))/", "position": 31} (SA-S-3560)
  - `@salla.sa/app-maker-editor`: {"id": 1762349899657, "name": "@salla.sa/app-maker-editor", "Prod": {}, "env": "prod", "path": "/channel/mobile/editor", "position": 50} (SA-S-3579)
  - `### Store mobile app`: Salla App Maker lets eligible merchants create a branded mobile commerce app connected to their Salla store. (SA-S-0008)
  - `## 2. What Salla is and is not`: Salla also offers connected products such as Salla Point, Salla Ads, Mahally, an app maker, an app marketplace, and enterprise-oriented services. (SA-S-0002)

### Who decides

- **Shopify**
  - `shopify.dev/docs/api/usage/access-scopes.md`: Merchants approve the scopes when they install it. (SH-S-0755)
- **Salla**
  - `صانع التطبيقات *برسوم إضافية`: "extra_icons": null}, {"parent_code": "knoat-albyaa", "title": "صانع التطبيقات *برسوم إضافية", "description": null, "icon": null, "icon_color": null, "icon_back [cut] [scope: plan: سلة بلس] (SA-S-2068)
  - `تطبيق خاص بمتجرك`: تطبيق خاص بمتجرك [scope: plan: سلة سبيشل] (SA-S-2192)
  - `app_builder_management`: "label": "marketplace apps management"}, {"id": 92231140, "name": "app_builder_management", "label": "app builder management"}, {"id": 1464104165, "name": "sms_ [cut] (SA-S-2413)
  - `app_builder_management`: "en": "marketplace apps management"}}, {"id": 92231140, "key": "app_builder_management", "name": {"ar": "صانع التطبيقات", "en": "app builder management"}}, {"id [cut] (SA-S-2630)
  - `app-maker-ai-components`: {"position": 199, "name": "app-maker-ai-components", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type" [cut] [scope: plans: plus, pro, special] (SA-S-3160)
  - `store-app-request`: {"position": 366, "name": "store-app-request", "value": {"enabled": false, "released": false, "plans": ["plus", "pro", "special"], "countries": [], "type": "fea [cut] [scope: plans: plus, pro, special] (SA-S-3327)
  - and 8 more statements in `platforms/salla/statements.tsv`

### Who is legally responsible

- **Shopify**
  - `9.9 Third Party Services and Third Party Partners`: Such Third Party Services are made available only as a convenience, and your purchase, access or use of any such Third Party Services is solely between you and  [cut] (SH-S-0058)
- **Salla**
  - `❓ هل يتأثر تجديد اشتراكي بصانع التطبيقات بوجود تطبيقي على حساب سلة ؟`: إذا كان تطبيقك لا يزال على حسابات سلة على متاجر التطبيقات، يجب نقل التطبيق الى حساباتك الخاصة على أبل ستور وقوقل بلاي لتتمكن من تجديد الاشتراك. (SA-S-5035)

### How it meets the rest

- **Shopify**
  - `read_mobile_platform_applications`: Requires `read_mobile_platform_applications` access scope. Please contact Shopify Support to enable this scope for your app. (SH-S-6058)
  - `read_mobile_platform_applications`: \| `read_mobile_platform_applications``write_mobile_platform_applications`Shopify approval required \| `AndroidApplication` and `AppleApplication` objects, which  [cut] (SH-S-6059)
  - `write_mobile_platform_applications`: Requires `write_mobile_platform_applications` access scope. Please contact Shopify Support to enable this scope for your app. (SH-S-6243)
  - `write_mobile_platform_applications`: `write_mobile_platform_applications` (SH-S-1129)
- **Salla**
  - `لدي حسابات مطور مسبقاً على آبل وجوجل`: وهو اشتراك مخصص لمن لديه حسابات مطور جاهزة مسبقاً من نوع شركة, سيتم بهذه الحالة استخدام الحسابات نفسها بتدشين تطبيق المتجر على متاجر التطبيقات App store و Googl [cut] (SA-S-5037)

### Stated reason

- **Shopify**: gap (searched, not found)
- **Salla**
  - `❓ هل يتأثر تجديد اشتراكي بصانع التطبيقات بوجود تطبيقي على حساب سلة ؟`: هذا النقل ضروري لتنفيذ أي صيانة أو تحديثات للتطبيقات وفقًا لسياسات حقوق الملكية لشركات أبل وقوقل. (SA-S-5036)

## M-079

Salla: SA-C-012 Salla AI Connector (MCP) and AI tools for merchants; WooCommerce: WC-C-095 WooCommerce MCP (AI assistant access to the store)

Basis: SA-C-012 platform_terms "salla-mcp"; platform_terms "Salla AI Connector" | WC-C-095 platform_terms "WooCommerce MCP"; platform_terms "Model Context Protocol"

### Where it lives

- **Salla**
  - `Salla AI Connector`: "general/salla-mcp":"Salla AI Connector" (SA-S-1725)
  - `@salla.sa/ui-merchant-ai-agent`: {"id": 1759925612291, "name": "@salla.sa/ui-merchant-ai-agent", "Prod": {}, "env": "prod", "path": "/ai-agent", "position": 48} (SA-S-3577)
- **WooCommerce**
  - `Introduction`: WooCommerce includes native support for the Model Context Protocol (MCP), enabling AI assistants and tools to interact directly with WooCommerce stores through  [cut] (WC-S-0918)

### Who decides

- **Salla**
  - `توليد تحسينات SEO عبر الذكاء الاصطناعي *برسوم إضافية`: "sub_features": [{"parent_code": "adar-almntgat", "title": "توليد تحسينات SEO عبر الذكاء الاصطناعي *برسوم إضافية", "description": null, "icon": null, "icon_colo [cut] [scope: plan: سلة برو] (SA-S-2133)
  - `suggested-by-moshamer`: {"position": 197, "name": "suggested-by-moshamer", "value": {"enabled": false, "released": true, "plans": ["plus", "pro"], "countries": [], "type": "feature"}} [scope: plans: plus, pro] (SA-S-3158)
  - `merchant-multi-agent-assistant`: {"position": 226, "name": "merchant-multi-agent-assistant", "value": {"enabled": true, "released": false, "plans": ["basic", "plus", "pro", "special"], "countri [cut] [scope: plans: basic, plus, pro, special] (SA-S-3187)
  - `salla-mcp`: {"position": 227, "name": "salla-mcp", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3188)
  - `salla_gpt`: {"position": 439, "name": "salla_gpt", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3400)
  - `ai-product`: {"position": 440, "name": "ai-product", "value": {"enabled": false, "released": false, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3401)
  - and 2 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `mcp_integration`: 'enabled_by_default' => false, 'disable_ui' => false, 'is_experimental' => true, (WC-S-5452)

### Who is legally responsible

- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Salla**
  - `general/salla-mcp/chatgpt#step3.description`: يتيح لك هذا الإعداد إضافة خادم MCP مخصَّص من سلة لمتابعة خطوات الربط. (SA-S-5005)
- **WooCommerce**
  - `Introduction`: WooCommerce includes native support for the Model Context Protocol (MCP), enabling AI assistants and tools to interact directly with WooCommerce stores through  [cut] (WC-S-0918)
  - `MCP_NAMESPACE`: const MCP_NAMESPACE = 'woocommerce'; (WC-S-5453)
  - `MCP_ROUTE`: const MCP_ROUTE = 'mcp'; (WC-S-5454)

### Stated reason

- **Salla**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

## M-080

Salla: SA-C-032 Back-in-stock alerts and wishlists; WooCommerce: WC-C-069 Back-in-stock notifications

Basis: SA-C-032 platform_terms "Back in stock alerts"; statement SA-S-5013 "اعلمني عند التوفر" | WC-C-069 platform_terms "Back in Stock Notifications"

### Where it lives

- **Salla**
  - `Back in stock alerts`: "products/notify_availability":"Back in stock alerts" (SA-S-1754)
  - `Wishlist Notifications`: "products/wishlist-notifications":"Wishlist Notifications" (SA-S-1761)
- **WooCommerce**
  - `WooCommerce > Notifications`: __( 'Stock Notifications', 'woocommerce' ), (WC-S-0047)

### Who decides

- **Salla**
  - `product_availability_notify_management`: "label": "payments rules management"}, {"id": 2097610897, "name": "product_availability_notify_management", "label": "product availability notify management"},  [cut] (SA-S-2402)
  - `product_availability_notify_management`: "en": "payments rules management"}}, {"id": 2097610897, "key": "product_availability_notify_management", "name": {"ar": "أعلمني عند التوفر", "en": "product avai [cut] (SA-S-2619)
  - `wishlist-notifications`: {"position": 212, "name": "wishlist-notifications", "value": {"enabled": true, "released": true, "plans": [], "countries": [], "type": "feature"}} [scope: the answering store (merchant@en)] (SA-S-3173)
  - `product-availability-notify`: {"position": 505, "name": "product-availability-notify", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "ty [cut] [scope: plans: plus, pro, special] (SA-S-3466)
  - `product-sku-availability-notify`: {"position": 506, "name": "product-sku-availability-notify", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], [cut] [scope: plans: plus, pro, special] (SA-S-3467)
- **WooCommerce**
  - `customer_stock_notifications`: 'option_key' => StockNotifications::ENABLE_OPTION_NAME, 'enabled_by_default' => false, 'is_experimental' => true, 'disable_ui' => false, (WC-S-5403)

### Who is legally responsible

- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Salla**
  - `product.availability.alert`: Triggered when a product is back in stock and the customer is notified. (SA-S-1666)
  - `salla-product-availability`: product id that can visitor subscribe to its availability notification (SA-S-1498)
- **WooCommerce**
  - `woocommerce_customer_stock_notifications_signup_rate_limit_exceeded`: do_action( 'woocommerce_customer_stock_notifications_signup_rate_limit_exceeded', $rate_limit_id, $user_email ); (WC-S-5404)
  - `CustomerStockNotificationEmail`: $this->title = __( 'Back in stock notification', 'woocommerce' ); (WC-S-5405)

### Stated reason

- **Salla**
  - `اعلمني عند التوفر`: - تساعدك كتاجر على معرفة المنتجات التي تستحق إعادة توفيرها فعلاً. (SA-S-5013)
- **WooCommerce**: gap (searched, not found)

## M-081

Salla: SA-C-031 Bookings and reservations (Order Reservations; Bookings); WooCommerce: WC-C-101 Bookings and appointments

Basis: SA-C-031 platform_terms "Bookings"; platform_terms "إدارة الحجوزات" | WC-C-101 platform_terms "Bookings and appointments"

### Where it lives

- **Salla**
  - `Bookings`: {"position": 9, "kind": "link", "text": "Bookings", "href": "/orders/reservations", "parent": 0, "list": 1} (SA-S-1779)
  - `Order Reservations`: "id": 889863, "name": "Order Reservations", "key": "apiDetailFolder.889863", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDis [cut] (SA-S-1023)
- **WooCommerce**
  - `Extensions > Merchandising > Bookings and appointments`: Bookings and appointments (WC-S-0731)

### Who decides

- **Salla**
  - `إدارة الحجوزات`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "إدارة الحجوزات", "description": null, "icon": null, "icon_color": null, "icon_background": null, [cut] [scope: plan: سلة بلس] (SA-S-1994)
  - `order_reservation_management`: "label": "order edit status all"}, {"id": 1261758713, "name": "order_reservation_management", "label": "order reservation management"}, {"id": 1154197976, "name [cut] (SA-S-2291)
  - `order_reservation_management`: "en": "order edit status all"}}, {"id": 1261758713, "key": "order_reservation_management", "name": {"ar": "إدارة الحجوزات", "en": "order reservation management" [cut] (SA-S-2508)
  - `product-booking`: {"position": 513, "name": "product-booking", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "featur [cut] [scope: plans: plus, pro, special] (SA-S-3474)
- **WooCommerce**
  - `Availability settings`: Availability settings - You can define availability rules based on specific dates, time slots, or custom ranges. [scope: WooCommerce Bookings] (WC-S-5352)

### Who is legally responsible

- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Salla**
  - `Order Reservations`: "id": 889863, "name": "Order Reservations", "key": "apiDetailFolder.889863", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDis [cut] (SA-S-1023)
- **WooCommerce**
  - `Requirements: Cron`: Working WP Cron (For clearing in-cart bookings from abandoned carts.) [scope: WooCommerce Bookings] (WC-S-5353)
  - `WooCommerce Bookings REST API v1`: WooCommerce Bookings is fully integrated with the WordPress REST API. [scope: WooCommerce Bookings] (WC-S-5470)

### Stated reason

- **Salla**
  - `❓ هل يمكنني الجمع بين منتج عادي و منتج حجز؟`: لا ، لأن منتج الحجز منفصل. (SA-S-5012)
- **WooCommerce**: gap (searched, not found)

## M-082

Salla: SA-C-166 Countries, cities and districts reference data; WooCommerce: WC-C-099 Reference data (countries, continents)

Basis: SA-C-166 platform_terms "Countries"; platform_terms "countries" | WC-C-099 platform_terms "data/countries"

### Where it lives

- **Salla**
  - `Countries`: "id": 841804, "name": "Countries", "key": "apiDetailFolder.841804", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1048)
- **WooCommerce**
  - `i18n/countries.php`: * Returns an array of countries and codes. (WC-S-5459)

### Who decides

- **Salla**: gap (searched, not found)
- **WooCommerce**
  - `i18n/countries.php`: * Country codes and names should follow the Unicode CLDR recommendation (https://cldr.unicode.org/translation/displaynames/countryregion-territory-names). (WC-S-5460)

### Who is legally responsible

- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Salla**
  - `Countries`: "id": 841804, "name": "Countries", "key": "apiDetailFolder.841804", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSe [cut] (SA-S-1048)
  - `Districts`: "id": 4930993, "name": "Districts", "key": "apiDetailFolder.4930993", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplaying [cut] (SA-S-1049)
  - `Cities`: "id": 841805, "name": "Cities", "key": "apiDetailFolder.841805", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSetti [cut] (SA-S-1050)
  - `countries`: {"id": 12, "slug": "countries", "icon": "sicon-earth", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_wri [cut] (SA-S-1558)
  - `metadata`: {"id": 14, "slug": "metadata", "icon": "sicon-badge", "options": [{"item": "read", "name": "read", "disabled": false}, {"item": "read_write", "name": "read_writ [cut] (SA-S-1562)
- **WooCommerce**
  - `wc/v3 > data`: 'data' => 'WC_REST_Data_Controller', (WC-S-0124)
  - `wc/v3 > data-continents`: 'data-continents' => 'WC_REST_Data_Continents_Controller', (WC-S-0125)
  - `wc/v3 > data-countries`: 'data-countries' => 'WC_REST_Data_Countries_Controller', (WC-S-0126)
  - `wc-analytics > DataCountries`: 'Automattic\WooCommerce\Admin\API\DataCountries', (WC-S-0210)
  - `Data`: The data API allows you to view all types of data available. (WC-S-0693)
  - `woocommerce_countries`: $this->geo_cache['countries'][ $locale ] = apply_filters( 'woocommerce_countries', include WC()->plugin_path() . '/i18n/countries.php' ); (WC-S-5461)

### Stated reason

- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-083

Salla: SA-C-027 Import and export of products, orders and customers (Advanced import; Exports); WooCommerce: WC-C-067 Product import and export (CSV)

Basis: SA-C-027 platform_terms "Import & export"; inventory SA-I-2225 "import-products"; inventory SA-I-2226 "export-products"; platform_terms "تصدير الطلبات" | WC-C-067 platform_terms "Product Import"; platform_terms "Product Export"

### Where it lives

- **Salla**
  - `Export templates`: {"position": 17, "kind": "link", "text": "Export templates", "href": "/orders/exports", "parent": 0, "list": 1} (SA-S-1787)
  - `Advanced import`: {"position": 34, "kind": "link", "text": "Advanced import", "href": "/importer", "parent": 0, "list": 2} (SA-S-1804)
  - `Import & export`: {"position": 35, "kind": "link", "text": "Import & export", "href": "/products/imports", "parent": 0, "list": 2} (SA-S-1805)
  - `Export templates`: {"position": 37, "kind": "link", "text": "Export templates", "href": "/products/exports", "parent": 0, "list": 2} (SA-S-1807)
  - `Import customers`: {"position": 77, "kind": "link", "text": "Import customers", "href": "/customers/imports", "parent": 0, "list": 5} (SA-S-1847)
  - `Export log`: {"position": 120, "kind": "link", "text": "Export log", "href": "/logs/export", "parent": 0, "list": 11} (SA-S-1890)
  - and 2 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `Products > Product Import`: 'name' => __( 'Product Import', 'woocommerce' ), (WC-S-0057)
  - `Products > Product Export`: 'name' => __( 'Product Export', 'woocommerce' ), (WC-S-0058)
  - `Import your products`: return __( 'Import your products', 'woocommerce' ); (WC-S-0426)

### Who decides

- **Salla**
  - `تصدير الطلبات`: "extra_icons": null}, {"parent_code": "adar-altlbat", "title": "تصدير الطلبات", "description": null, "icon": null, "icon_color": null, "icon_background": null,  [cut] [scope: plan: سلة بلس] (SA-S-1997)
  - `استيراد العملاء`: "extra_icons": null}, {"parent_code": "alaamlaaa", "title": "استيراد العملاء", "description": null, "icon": null, "icon_color": null, "icon_background": null, " [cut] [scope: plan: سلة بلس] (SA-S-2059)
  - `نقل البيانات بسلاسة`: نقل البيانات بسلاسة [scope: plan: سلة سبيشل] (SA-S-2189)
  - `import_export_management`: "label": "products stock management"}, {"id": 692313006, "name": "import_export_management", "label": "import export management"}, {"id": 2066283183, "name": "p [cut] (SA-S-2257)
  - `custom_importer_management`: "label": "pre order campaigns management"}, {"id": 1577858085, "name": "custom_importer_management", "label": "custom importer management"}, {"id": 736711462, " [cut] (SA-S-2263)
  - `custom_importer_view`: "label": "custom importer management"}, {"id": 736711462, "name": "custom_importer_view", "label": "custom importer view"}], "position": 1} (SA-S-2264)
  - and 18 more statements in `platforms/salla/statements.tsv`
- **WooCommerce**
  - `import_allowed`: return current_user_can( 'edit_products' ) && current_user_can( 'import' ); (WC-S-5396)
  - `export_allowed`: return current_user_can( 'edit_products' ) && current_user_can( 'export' ); (WC-S-5397)

### Who is legally responsible

- **Salla**: gap (observation needed)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Salla**
  - `Exports`: "id": 892455, "name": "Exports", "key": "apiDetailFolder.892455", "shareSettings": {"directoryTreeDisplayStyle": "GENERAL_FOLDER", "folderContentsDisplayingSett [cut] (SA-S-1057)
  - `exports`: {"id": 23, "slug": "exports", "icon": "sicon-download", "options": [{"item": "read", "name": "read", "disabled": true}, {"item": "read_write", "name": "read_wri [cut] (SA-S-1566)
- **WooCommerce**
  - `woocommerce_product_import_pre_insert_product_object`: $object = apply_filters( 'woocommerce_product_import_pre_insert_product_object', $object, $data ); (WC-S-5398)
  - `woocommerce_product_export_{export_type}_default_columns`: "woocommerce_product_export_{$this->export_type}_default_columns", (WC-S-5399)

### Stated reason

- **Salla**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

## M-084

Shopify: SH-C-174 Sanctions and unsupported countries and regions; WooCommerce: WC-C-028 US sanctions on access to Automattic and Woo services, WC-C-029 Sanctions and export compliance of the merchant's own sales

Basis: SH-C-174 platform_terms "Sanctions"; platform_terms "Sanctioned Person"; statement SH-S-0307 "Orders shipping to unsupported countries and regions are prohibited." | WC-C-028 platform_terms "US Economic Sanctions"; platform_terms "OFAC" | WC-C-029 platform_terms "export, import, and sanctions laws"

### Where it lives

- **Shopify**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

### Who decides

- **Shopify**
  - `Part I, D. (after limitation of liability)`: You may not use the Payments Services if you are a resident of a sanctioned country or region embargoed by the United States, Canada, or the European Union, or  [cut] (SH-S-0122)
  - `Part I, A. Onboarding, KYC and underwriting`: Neither you nor your legal representatives, authorized representatives, ultimate beneficial owners, or controlling owners may be subject to trade sanctions impo [cut] [scope: EU / EEA and United Kingdom (Payment Facilitator Terms)] (SH-S-0131)
  - `help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.`: Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors. (SH-S-0298)
  - `list of unsupported countries and regions`: * Cuba (SH-S-0299)
  - `list of unsupported countries and regions`: * Iran (SH-S-0300)
  - `list of unsupported countries and regions`: * North Korea (SH-S-0301)
  - and 8 more statements in `platforms/shopify/statements.tsv`
- **WooCommerce**
  - `18. US Economic Sanctions`: We reserve the right to restrict or block your access, or access by any of your customers or potential customers (if applicable), to the Services and/or to term [cut] (WC-S-0493)
  - `18. US Economic Sanctions`: You agree that our ability to provide our Services to you is subject to compliance with US sanctions that restrict or prohibit who or from where our Services ca [cut] (WC-S-0490)
  - `18. US Economic Sanctions`: (i) are not located or residing in any country or territory subject to comprehensive US sanctions (currently Cuba, Crimea, Iran, North Korea, Donetsk People’s R [cut] (WC-S-0491)
  - `8. j. Ecommerce Services: Prohibited Uses`: Ecommerce Services cannot be used in, from, by, or for the benefit of a country, organization, entity, or person embargoed or blocked by any government, includi [cut] (WC-S-0648)
  - `18. US Economic Sanctions`: (ii) are not listed on any United States list of prohibited or restricted parties, such as OFAC’s Specially Designated Nationals and Persons List (WC-S-0657)
  - `8. j. Ecommerce Services: Prohibited Uses`: Ecommerce Services cannot be used in, from, by, or for the benefit of a country, organization, entity, or person embargoed or blocked by any government, includi [cut] [scope: Ecommerce Services (Terms 8.j)] (WC-S-0648)

### Who is legally responsible

- **Shopify**
  - `Part A, Section 2.2`: (ii) Partner is not resident or located in or organized under the laws of an Unsupported Region. (SH-S-0297)
  - `Part C, App Developers, export control`: App Developer represents and warrants that the U.S. export control classification number of each of their Apps is “EAR99” (SH-S-0296)
  - `Part I, A. Privacy of Others`: the applicable Payment Processor may also process personal data as an independent controller for certain processing activities, including but not limited to com [cut] (SH-S-0100)
  - `Part I, A. Privacy`: Each Payment Processor may also process your personal data or Customer Payment Data as an independent controller, for example, to comply with their own regulato [cut] (SH-S-0099)
- **WooCommerce**
  - `18. US Economic Sanctions`: (iii) shall not use or allow access by any of your customers or potential customers (if applicable) to the Services in any manner that may cause Automattic to v [cut] (WC-S-0492)
  - `8. j. Ecommerce Services: Your responsibilities`: are solely responsible for ensuring that your transactions with customers comply with applicable export, import, and sanctions laws and regulations, including o [cut] (WC-S-0470)

### How it meets the rest

- **Shopify**: gap (observation needed)
- **WooCommerce**: gap (searched, not found)

### Stated reason

- **Shopify**
  - `help.shopify.com/en/manual/your-account/legal/unsupported-countries-and-regions.`: Shopify is unable to support business involving certain regions due to local regulatory requirements, commercial partnerships, and/or other pertinent factors. (SH-S-0298)
  - `Part A, definitions, "Unsupported Region"`: “Unsupported Region” means a region where Shopify is unable to operate due to local legal and regulatory requirements, commercial partnerships, and/or other per [cut] (SH-S-0289)
- **WooCommerce**
  - `18. US Economic Sanctions`: You agree that our ability to provide our Services to you is subject to compliance with US sanctions that restrict or prohibit who or from where our Services ca [cut] (WC-S-0490)

## M-085

Shopify: SH-C-173 Prohibited and restricted businesses for Shopify Payments; WooCommerce: WC-C-011 Restricted and prohibited businesses on WooPayments

Basis: SH-C-173 platform_terms "Prohibited and Restricted Businesses" | WC-C-011 platform_terms "prohibited or restricted"; platform_terms "restricted businesses or activities"

### Where it lives

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `Restricted accounts`: However, restricted accounts will still be able to access the Transactions and Disputes menus in order to manage new and existing disputes. [scope: restricted accounts] (WC-S-5296)
  - `prohibited and restricted businesses`: The full list of prohibited and restricted businesses can be found here. (WC-S-5324)

### Who decides

- **Shopify**
  - `Prohibited businesses and products`: The list of prohibited products and services isn't exhaustive and it varies depending on your region. (SH-S-0328)
  - `Part I, B. Prohibited and Restricted Businesses`: Prohibited Business and Restricted Business categories may be imposed by law or through the Payment Network Rules, by Shopify or the requirements of a Payment P [cut] (SH-S-0108)
  - `Prohibited businesses and products, high-level categories`: Financial products and services: Products or services related to money transfers, virtual currencies and cryptocurrencies, check cashing, or credit repair servi [cut] (SH-S-0329)
  - `Prohibited businesses and products`: There are certain business models that, while legal, Shopify Payments can't support. (SH-S-0327)
  - `Part I, B. Prohibited and Restricted Businesses`: The types of business categories and business practices that are considered Prohibited Businesses or Restricted Businesses are provided by each Payment Processo [cut] [scope: the merchant's Designated Country] (SH-S-0109)
- **WooCommerce**
  - `What businesses and products are prohibited or restricted on WooPayments?`: If we become aware of prohibited activity, we may restrict or shut down the account. (WC-S-0524)
  - `What businesses and products are prohibited or restricted on WooPayments?`: Due to restrictions put in place by card networks, our payment processors, and their financial service providers, some business types and product types are not  [cut] (WC-S-0523)
  - `Alcohol and CBD`: Merchants selling CBD must use Square or Viva Wallet. [scope: merchants selling CBD] (WC-S-0525)
  - `8. j. More on WooPayments Specifically`: We may refuse, condition, or suspend any transaction or account (including your use of WooPayments) if we believe you have violated the Agreement or that your a [cut] (WC-S-0478)
  - `Restricted accounts`: Our payments partner, Stripe, has found other issues with your account. (WC-S-0518)
  - `Restricted accounts`: However, restricted accounts will still be able to access the Transactions and Disputes menus in order to manage new and existing disputes. [scope: restricted accounts] (WC-S-5296)

### Who is legally responsible

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `8. j. More on WooPayments Specifically`: In particular, you cannot use WooPayments to enable any person (including you) to benefit from restricted businesses or activities. (WC-S-0653)
  - `prohibited and restricted businesses`: By signing up to use WooPayments, you agree not to accept payments in connection with these restricted activities, practices, or products. (WC-S-5325)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `Restricted accounts`: If your account is restricted, you should receive an email with more information from either the WooCommerce team or Stripe. (WC-S-5295)

### Stated reason

- **Shopify**
  - `principle "Payment Terms (and terms from other add-on products) can also apply."`: When you use one of these products, you are interacting with an entire supply chain of businesses: for example, Shopify Payments involves an ecosystem of proces [cut] (SH-S-0169)
  - `principle "Payment Terms (and terms from other add-on products) can also apply."`: Shopify offers a range of products and services that leverage partnerships with other organizations. (SH-S-0170)
- **WooCommerce**
  - `What businesses and products are prohibited or restricted on WooPayments?`: Due to restrictions put in place by card networks, our payment processors, and their financial service providers, some business types and product types are not  [cut] (WC-S-0523)

## M-086

Shopify: SH-C-175 Merchant compliance with product, consumer and fiscal rules; WooCommerce: WC-C-027 Merchant responsibility for the store's sales, receipts, refunds and consumer law

Basis: SH-C-175 statement SH-S-0236 "You are responsible for the creation and operation of your Shopify Store"; statement SH-S-0236 "all aspects of the transactions between you and your customer(s)" | WC-C-027 platform_terms "Your responsibilities"; statement WC-S-0466 "solely responsible for all of your ecommerce activities"

### Where it lives

- **Shopify**
  - `Product disclosures`: You can add and display these required, customer-facing warnings on your product pages using the Disclosures product metafield and metaobject entries. (SH-S-7257)
- **WooCommerce**: gap (searched, not found)

### Who decides

- **Shopify**
  - `help.shopify.com/en/manual/compliance/legal.md`: You also need to consider the implications of selling in different jurisdictions, including researching the relevant import and export laws and regulations, and [cut] (SH-S-0667)
- **WooCommerce**
  - `8. j. Ecommerce Services: Your responsibilities`: You have control over your store, and with great power comes great responsibility. (WC-S-0848)

### Who is legally responsible

- **Shopify**
  - `product recalls`: You're responsible for adhering to legal requirements about recalls in any jurisdiction where you conduct business. (SH-S-0669)
  - `4. Your Responsibilities`: You acknowledge and agree that the Services are not a marketplace, and any contract of sale made through the Services is directly and only between you and the c [cut] (SH-S-0011)
  - `4. Your Responsibilities`: You are responsible for the creation and operation of your Shopify Store, your Materials, the goods and services that you may sell through the Services, and all [cut] (SH-S-0236)
  - `4. Your Responsibilities`: For the avoidance of doubt, Shopify is not the seller or merchant of record and has no responsibility for your Store, your Materials, the goods or services you  [cut] (SH-S-0013)
  - `help.shopify.com/en/manual/compliance/legal.md`: Shopify can set you up for success, but there are also steps that you need to take, especially if you plan to sell regulated products. (SH-S-0668)
  - `4. Your Responsibilities`: This includes, but is not limited to, authorizing the charge to the customer in respect of the customer's purchase, determining and collecting taxes, refunds, r [cut] (SH-S-0012)
- **WooCommerce**
  - `8. j. Ecommerce Services: Your responsibilities`: We’re not involved in your relationships or transactions with any customer or potential customer, and you’re solely responsible for all of your ecommerce activi [cut] (WC-S-0466)
  - `8. j. Ecommerce Services: Your responsibilities`: are responsible for acquiring appropriate consent to process customer transactions, giving customers confirmation or receipts for each charge, verifying custome [cut] (WC-S-0468)
  - `8. j. Ecommerce Services: Your responsibilities`: are responsible for all questions, complaints, disputes (including chargebacks), refunds, reversals, or fines that arise from your use of Ecommerce Services. (WC-S-0469)
  - `8. Specific Service Terms: j. Ecommerce Services`: We offer Services via Woo, WordPress.com, and Jetpack that enable you to sell items (goods, content, services, etc.), receive payments on your website, or other [cut] (WC-S-0647)

### How it meets the rest

- **Shopify**: gap (searched, not found)
- **WooCommerce**: gap (searched, not found)

### Stated reason

- **Shopify**: gap (searched, not found)
- **WooCommerce**
  - `8. j. Ecommerce Services: Your responsibilities`: You have control over your store, and with great power comes great responsibility. (WC-S-0848)

## M-087

Shopify: SH-C-111 International domains and geolocation; WooCommerce: WC-C-046 Customer geolocation (MaxMind and IP lookup services)

Basis: SH-C-111 platform_terms "Geolocation apps"; inventory SH-I-2153 "Using the Geolocation app" | WC-C-046 platform_terms "MaxMind Geolocation"

### Where it lives

- **Shopify**
  - `Geolocation apps`: "h1": "Geolocation apps" (SH-S-2681)
- **WooCommerce**
  - `Integration`: $this->label = __( 'Integration', 'woocommerce' ); (WC-S-0008)
  - `MaxMind geolocation integration`: To determine this, WooCommerce integrates with MaxMind GeoLite2 geolocation data. (WC-S-0640)
  - `woocommerce_default_customer_address`: 'desc_tip' => __( 'This option determines a customers default location. The MaxMind GeoLite Database will be periodically downloaded to your wp-content director [cut] (WC-S-0602)

### Who decides

- **Shopify**
  - `Assign local domains`: {"kind": "row", "section": 1, "position": 78, "cells": [{"tag": "th", "text": "Assign local domains", "scope": "row"}, {"tag": "td", "text": "Included"}, {"tag" [cut] [scope: plans, one cell each, in the order of the table header: BasicStart for free, GrowStart for free, AdvancedStart for free, PlusTry for $399] (SH-S-7061)
- **WooCommerce**
  - `woocommerce_default_customer_address`: 'desc_tip' => __( 'This option determines a customers default location. The MaxMind GeoLite Database will be periodically downloaded to your wp-content director [cut] (WC-S-0602)
  - `woocommerce_default_customer_address`: 'id' => 'woocommerce_default_customer_address', 'desc_tip' => __( 'This option determines a customers default location. The MaxMind GeoLite Database will be per [cut] (WC-S-5377)
  - `Enabling geolocation`: Once geolocation is enabled, you'll need to create a MaxMind account and configure MaxMind via the Integration tab in WooCommerce > Settings. (WC-S-5378)

### Who is legally responsible

- **Shopify**: gap (stated only in general terms)
- **WooCommerce**: gap (searched, not found)

### How it meets the rest

- **Shopify**
  - `MarketWebPresence`: "name": "MarketWebPresence", "kind": "OBJECT", "description": "The market’s web presence, which defines its SEO strategy. This can be a different domain" [scope: GraphQL Admin API 2026-10] (SH-S-7458)
- **WooCommerce**
  - `WC_Integration_MaxMind_Database_Service (database download URL)`: 'https://download.maxmind.com/app/geoip_download' (WC-S-0615)
  - `WC_Geolocation IP lookup services: ipify`: 'ipify' => 'https://api64.ipify.org', (WC-S-0612)
  - `WC_Geolocation IP lookup services: ipinfo.io`: 'ipinfo.io' => 'https://ipinfo.io/%s/json', (WC-S-0613)

### Stated reason

- **Shopify**
  - `country selector`: If you sell in local currencies, then you need to have a country selector so that customers can select their local country or region and your store displays the [cut] (SH-S-7288)
- **WooCommerce**
  - `MaxMind geolocation integration`: The free, core WooCommerce plugin enables store owners to automatically geolocate customers to display tax rates and shipping methods specific to their location [cut] (WC-S-0641)

## M-088

Salla: SA-C-122 Fraud protection (نظام الحماية من الاحتيال); WooCommerce: WC-C-013 WooPayments fraud protection rules set by the merchant

Basis: SA-C-122 platform_terms "نظام الحماية من الاحتيال" | WC-C-013 platform_terms "fraud protection"

### Where it lives

- **Salla**
  - `fees_calculator.shopping_experience_fee.description`: تشمل خدمات حفظ بطاقة وعنوان العميل، الشراء السريع عبر Apple Pay، الحماية من الاحتيال، ومزايا أخرى من مدفوعات سلة. (SA-S-0104)
- **WooCommerce**
  - `WooPayments: Fraud Protection`: WooPayments offers configurable fraud protection rules for merchants. (WC-S-0862)

### Who decides

- **Salla**
  - `نظام الحماية من الاحتيال`: "extra_icons": null}, {"parent_code": "aldfaa", "title": "نظام الحماية من الاحتيال", "description": null, "icon": null, "icon_color": null, "icon_background": n [cut] [scope: plan: سلة بلس] (SA-S-1971)
  - `قيود الدفع والحماية من الاحتيال`: "sub_features": []}, {"title": "قيود الدفع والحماية من الاحتيال", "description": "قيود الدفع والحماية من الاحتيال", "icon": null, "code": "kyod-aldfaa-oalhmay-m [cut] [scope: plan: سلة برو] (SA-S-2145)
  - `sift`: {"position": 93, "name": "sift", "value": {"enabled": false, "released": true, "plans": ["plus", "pro", "special"], "countries": [], "type": "feature"}} [scope: plans: plus, pro, special] (SA-S-3054)
- **WooCommerce**
  - `WooPayments: Fraud Protection`: WooPayments offers configurable fraud protection rules for merchants. (WC-S-0862)

### Who is legally responsible

- **Salla**
  - `suspicious_order.confirm_execution.message`: استمرارك بتنفيذ هذا الطلب يحمِّلك المسؤولية في حال وردتنا شكوى من مالك البطاقة، وقد يُخصم مبلغ العملية من حسابك إذا ثبتت صحة الشكوى. (SA-S-5051)
- **WooCommerce**: gap (stated only in general terms)

### How it meets the rest

- **Salla**
  - `وسم (عميل غير جاد)`: يعتمد ظهور وسم (عميل غير جاد) بجانب اسم العميل على نظام سلة لمكافحة الاحتيال بالذكاء الاصطناعي, من خلال تحليل بيانات العملاء على متاجر سلة (SA-S-5052)
- **WooCommerce**
  - `How fraud protection works`: Blocked: The customer’s payment method is not charged, and the order is set to the Pending Payment status. (WC-S-0863)

### Stated reason

- **Salla**
  - `وسم (عميل غير جاد)`: وذلك حرصًا لأن تكون سلة بيئة تسوُّق آمنة وموثوقة لكل من التجار والعملاء. (SA-S-5053)
- **WooCommerce**
  - `What customers see`: In order to avoid revealing your specific fraud protection rules to customers, WooPayments will show a generic error message when the rules block a transaction. (WC-S-5301)

