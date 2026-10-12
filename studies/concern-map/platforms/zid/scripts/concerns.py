# Concerns for the Zid run (Q1), in Zid's own terms, and the rules that place each inventory entry in them.
# A concern groups entries whose parts sit in one place; where Zid names parts that sit in different places, they are split.

CONCERNS = [
 # id, concern, platform_terms (Zid's own words naming it, verbatim, Arabic and English as Zid gives them), split_note
 ("ZD-C-001", "Zid Pay activation / تفعيل زد باي", "تفعيل زد باي; تفعيل الدفع الالكتروني; Activate Zid Payments; متطلبات تفعيل الدفع الالكتروني",
  "Split from the other Zid Pay pieces: activation is where eligibility, documents and approval by the payment gateway are stated."),
 ("ZD-C-002", "Zid Pay transactions and refunds / العمليات والاسترداد", "العمليات; العمليات والاسترداد ( لوحة التحكم الجديدة ); استرداد المبلغ للعميل; Refund Flexibility",
  "Zid's help centre names العمليات as its own Zid Pay section; refunds of Zid Pay transactions are made there."),
 ("ZD-C-003", "Zid Pay deposits and account statement / الإيداعات وكشف الحساب", "الإيداعات; كشف الحساب والإيداعات; Funds Collection; تحصيل المبالغ; Crystal-Clear Deposits",
  "Split from transactions: the settlement of collected funds to the merchant's bank account has its own schedule, fees and holds."),
 ("ZD-C-004", "Bank accounts / الحسابات البنكية", "الحسابات البنكية; الحسابات البنكية ( لوحة التحكم الجديدة )",
  "Zid's help centre names it as its own section under زد باي; the same store bank accounts serve bank-transfer display and Zid Pay deposits."),
 ("ZD-C-005", "Zid Pay payment networks / شبكات الدفع", "شبكات الدفع; Supported Payment Networks; Zid Payments gateway to accept Mada, Visa, and Mastercard; Enable Apple Pay for faster checkout",
  "Networks (mada, Visa, Mastercard, American Express, Apple Pay, KNET) are switched per store inside Zid Pay."),
 ("ZD-C-006", "Zid Pay transaction fees / رسوم زد باي", "رسوم زد باي; رسوم العمليات; Transaction Fees; Fair and Clear Pricing",
  "Split from transactions: the fee is set by the store's Zid plan and the payment network."),
 ("ZD-C-007", "Zid Pay chargebacks, fraud and held funds / charge back والاحتيال واحتجاز الأموال", "charge back; Fraud; Fraud Shield; Fraud protection to prevent losses; احتجاز الأموال; مبلغ احتياطي",
  "Split from deposits: the terms place chargeback and fraud liability and fund holds separately from the deposit schedule."),
 ("ZD-C-008", "Payment links / روابط الدفع", "روابط الدفع; Quick Payment Links; payment_link", "Zid's help centre names it as its own Zid Pay section."),
 ("ZD-C-009", "Payment service providers behind Zid Pay / مقدمي خدمات الدفع", "مقدمي خدمات الدفع; مزود الخدمة; payment service providers; التعاقد من الباطن",
  "Split from Zid Pay itself: Zid's terms describe Zid Pay as a service run through payment service providers, and place the providers' failure separately."),
 ("ZD-C-010", "Zid Payments Open APIs for payment service providers", "Zid Payments; Open APIs integration model; Merchant Activation; Direct payment; Embedded payment; Link Merchant Event; Payment Paid Event; Refund Event",
  "The API contract that providers implement for Zid Payments; it sits in its own section of the developer docs, apart from the Merchant APIs."),
 ("ZD-C-011", "Other payment gateways / بوابات الدفع الأُخرى", "بوابات الدفع الأُخرى; باي موب Paymob; اموال باي amwal pay; بوابة الدفع تاب Tap",
  "Not in the platform's lists: none of the lists taken here names it; the help centre gives it its own article, بوابات الدفع الأُخرى( لوحة التحكم الجديدة) (help.zid.sa/payment-gateways/). Split from Zid Pay: gateways the merchant activates with the gateway itself, per country."),
 ("ZD-C-012", "Store payment methods / طرق الدفع", "طرق الدفع; List Payment Methods; Get Payment Options; Various Payment Methods; Advanced Payment Methods",
  "The set of payment methods a store offers, as the Store Settings API and plan lines name it."),
 ("ZD-C-013", "Instalment services (buy now, pay later) / خدمات التقسيط", "خدمات التقسيط; الدفع لاحقاً; Flexible Payments; Tamara; Tabby; MISPay; Emkan; Madfu",
  "Split from Zid Pay: each instalment provider is activated with the merchant's own account at the provider."),
 ("ZD-C-014", "Cash on delivery option / الدفع عند الاستلام", "الدفع عند الاستلام; خدمة الدفع عند التوصيل; Cash on Delivery; Block Cash on Delivery",
  "Split from COD collection: the payment option is a store setting per carrier; the Terms place the service with a third party."),
 ("ZD-C-015", "COD collection through Zid shipping / تحصيل الدفع عند الاستلام", "خدمة الدفع عند الاستلام (COD); تحصيل الدفع عند الاستلام; Cash on Delivery Collection",
  "Split from the COD option: under direct shipping Zid collects the amounts from end customers and transfers them to the merchant's wallet."),
 ("ZD-C-016", "Bank transfer option / خدمة التحويل البنكي", "خدمة التحويل البنكي; الدفع بالتحويل البنكي; Bank Transfer Payment", ""),
 ("ZD-C-017", "Zid Wallet (merchant wallet) / محفظة زد", "محفظة زد; محفظة التاجر; Zid Wallet; Zid Electronic Wallet", ""),
 ("ZD-C-018", "Wallet deduction from Zid Pay / الاستقطاع للمحفظة", "الاستقطاع للمحفظة", "Split from Zid Wallet: available only to merchants with Zid Pay, in Saudi Arabia and Kuwait."),
 ("ZD-C-019", "Customer wallet and cashback / محفظة العميل والكاش باك", "محفظة العميل والكاش باك; Customer Wallets; Cashback Rules; Zid Wallet (customer payment option on the compare table)",
  "Separate from the merchant's Zid Wallet: this wallet holds store credit for the store's customers."),
 ("ZD-C-020", "Zid subscription plans and fees / الاشتراكات", "الاشتراكات; Subscriptions; Subscription Fees; إدارة الاشتراك; Starter; Rise; Growth; Pro; Lite plan",
  "The merchant's subscription to Zid and its billing, refunds and renewal."),
 ("ZD-C-021", "Purchases from Zid and their payment processing / المدفوعات والمشتريات", "المدفوعات والمشتريات; Payments and Purchases; third-party payment processor",
  "Split from subscriptions: the Terms give purchases from Zid their own section, naming the payment processor."),
 ("ZD-C-022", "App Market subscriptions and partner payouts", "App Subscription Events; Subscription Details; Update Usage-Based Charges; Partner Payouts; Payouts",
  "Split from the App Market as a whole: merchants pay Zid for app plans and Zid pays partners, on its own cycle."),
 ("ZD-C-023", "Zid Financing / تمويل زد", "تمويل زد; Zid Financing; Financing; جهة التمويل", ""),
 ("ZD-C-024", "Mazeed collections and dues / المستحقات المالية لمزيد", "المستحقات المالية لمزيد; تحصيلات مزيد; الأحكام المالية",
  "Split from the Mazeed marketplace: Zid collects Mazeed order payments and pays merchants on its own schedule."),
 ("ZD-C-025", "Zid Agent / وكيل زد", "وكيل زد (Zid Agent); Zid Agent", ""),
 ("ZD-C-026", "Value added services / خدمة المميزات الإضافية VAS", "خدمة المميزات الإضافية VAS; Value Added Services (VAS)", ""),
 ("ZD-C-028", "Order payment status / حالة الدفع", "order.payment_status.update; Payment Status; Bulk Payment Status Update",
  "Split from orders: the order's paid or unpaid state is its own webhook event and plan line."),
 ("ZD-C-030", "Zid's contracting entity and governing law", "شركة القدرة التقنية لتقنية المعلومات والاتصالات; Al-Qudrah Al-Taqniyah for Technology and Communication Company; Commercial Registration Number 1010365366; Governing Law and Dispute Resolution", ""),
 ("ZD-C-031", "Zid Egypt / زد مصر", "About Zid Egypt; حول زد مصر; Zid Egypt", "Split from the contracting entity: Zid states a separate commercial registration for Egypt."),
 ("ZD-C-032", "Countries Zid serves", "ZID is available in; زد متاحة في; Egypt; UAE; Kuwait; Oman; Syria", ""),
 ("ZD-C-033", "Store country, operating countries and cities", "Countries and Cities; List Store Operating Countries; countries_cities.read", ""),
 ("ZD-C-034", "Markets / الأسواق", "الأسواق; خاصية الأسواق", ""),
 ("ZD-C-035", "Store business data and verification / بيانات المتجر", "بيانات المتجر; تفاصيل النشاط التجاري; Business; KYC (Know Your Customer); third_store_business_read",
  "Split from Zid Pay activation: the store's business documents are held in store settings and read by the Business API."),
 ("ZD-C-036", "E-commerce store regulations / ضوابط المتجر الإلكتروني", "ضوابط المتجر الإلكتروني; E-Commerce Store Regulations", ""),
 ("ZD-C-037", "Zid Pay prohibited activities and sanctions / الأنشطة المحظورة", "الأنشطة المحظورة; Prohibited Activities", ""),
 ("ZD-C-038", "Nafath identity verification / التحقق من نفاذ", "اجتياز التحقق من نفاذ; Verify your identity with Nafath", ""),
 ("ZD-C-039", "Store legal pages / الصفحات القانونية", "الصفحات القانونية", "The merchant's own policies shown in the store."),
 ("ZD-C-040", "Privacy and personal data / سياسة الخصوصية", "سياسة الخصوصية; Privacy Policy", ""),
 ("ZD-C-041", "Cross-border data transfer / نقل البيانات عبر الحدود", "نقل البيانات عبر الحدود; THE DATA TRANSFER ACROSS THE BORDERS", "Split from privacy: the policy gives it its own section."),
 ("ZD-C-042", "AI data processing / معالجة البيانات بالذكاء الاصطناعي", "معالجة البيانات بالذكاء الاصطناعي; AI Data Processing", "Split from privacy: the policy gives it its own section and names its processor."),
 ("ZD-C-043", "Digital products and vouchers / المنتجات الرقمية", "Digital Products; Digital Vouchers; المنتجات الرقمية; Downloadables", ""),
 ("ZD-C-044", "Export requests / طلبات التصدير", "طلبات التصدير", ""),
 ("ZD-C-050", "Store languages and currencies / لغة وعملات المتجر", "لغة وعملات المتجر; اللغات والعملات; خاصية العملات; Geo-Based Currency Settings; Localization", ""),
 ("ZD-C-051", "Tax settings (VAT) / اعدادات الضريبة", "اعدادات الضريبة; ضريبة القيمة المضافة; Invoice & Tax Settings; Tax-Applicable Countries; Retrieve VAT Settings; Calculate and display VAT", ""),
 ("ZD-C-052", "Invoice settings / اعدادات الفواتير", "اعدادات الفواتير; Invoice Printing", ""),
 ("ZD-C-053", "ZATCA e-invoicing integration / الربط مع منصة فاتورة", "الربط مع منصة فاتورة ZATCA", ""),
 ("ZD-C-054", "Credit notes / إشعارات الدائن", "List Order Credit Notes; Calculate Reverse Totals; Credit notes", ""),
 ("ZD-C-060", "Zid Logistics and direct shipping / زد لوجستيات وزد شب", "زد لوجستيات; زد لوجيستك; زد شب; الشحن المباشر; ZidShip; Zid Logistics: One Contract for 35 Carriers", ""),
 ("ZD-C-061", "Shipping apps and third-party logistics companies", "شركات الخدمات اللوجستية الطرف الثالث; Shipping apps; Shipping and fulfillment company; الشحن والتخزين",
  "Split from Zid Logistics: carriers that merchants connect as App Market apps or by their own contract."),
 ("ZD-C-062", "Store shipping methods / طرق الشحن", "List Store Shipping Methods; delivery-options; طرق الشحن; shipping.read", ""),
 ("ZD-C-063", "Shipping and payment restrictions / قيود الشحن و الدفع", "قيود الشحن و الدفع; قيود الدفع", ""),
 ("ZD-C-070", "Zid App Market / سوق تطبيقات زد", "سوق تطبيقات زد; Zid App Market; App Market categories", "App Market categories share one placement (partner apps installed through the App Market), so they are grouped; shipping apps are split out (ZD-C-061)."),
 ("ZD-C-071", "OAuth authorization and app scopes", "Authorization; OAuth 2.0; Scopes; Zid App Activation & OAuth Policy", ""),
 ("ZD-C-072", "Webhooks", "Webhooks; Webhook Health Tracking; Create Webhook", ""),
 ("ZD-C-073", "Embedded apps", "Embedded Apps; embedded_apps_tokens_write", ""),
 ("ZD-C-074", "Private apps and direct API access", "Private apps; API Access; خدمة الربط المباشرة (APIs); Connect your store with external systems (via API)", ""),
 ("ZD-C-075", "Storefront APIs", "API's; Authentication; Checkout; Storefront", "The customer-facing API groups, apart from the Merchant APIs."),
 ("ZD-C-076", "Theme Market and themes / سوق ثيمات زد", "سوق ثيمات زد; سوق الثيمات; Themes; Theme Market", ""),
 ("ZD-C-077", "Store account and profile", "Account; Me; Store; Retrieve Store Manager Profile; اعدادات الحساب; Account Details", ""),
 ("ZD-C-080", "Orders / الطلبات", "Orders; Order Tags; Custom Order Status; Draft Orders", ""),
 ("ZD-C-081", "Reverse orders and returns", "Reverse Orders; Full & Partial Returns; Returned Orders", ""),
 ("ZD-C-082", "Abandoned carts / السلات المتروكة", "Abandoned Carts; abandoned_cart.created", ""),
 ("ZD-C-083", "Products / المنتجات", "Products; Managing Products; Product Variants; Product Images", ""),
 ("ZD-C-084", "Product categories / التصنيفات", "Product Categories; category.create", ""),
 ("ZD-C-085", "Inventory and stock / المخزون", "Inventories; Product Stock; Inventory Management", ""),
 ("ZD-C-086", "Product reviews and questions", "Product Reviews; Product Questions & Answers; Review Management", ""),
 ("ZD-C-087", "Product availability notifications", "Product Availability Notifications; Product Availability Notification", ""),
 ("ZD-C-088", "Coupons and discounts", "Coupons; Add Discount Coupons; Discounts; Card Discount", ""),
 ("ZD-C-089", "Bundle offers", "Bundle Offers; Add Dynamic Bundle", ""),
 ("ZD-C-090", "Loyalty program", "Loyalty Program; Loyalty Programs", ""),
 ("ZD-C-091", "Customers / العملاء", "Customers; Customer Tags; Customer Information", ""),
 ("ZD-C-092", "Customer self-service portal / بوابة خدمة العملاء الذاتية", "Customer Portal Tickets; بوابة خدمة عملاء متاجر زد الذاتية; Zid Stores' Customer Complaints", ""),
 ("ZD-C-093", "Blogs", "Blogs", ""),
 ("ZD-C-094", "Team members and permissions / فريق العمل", "فريق العمل; مجموعات الفريق; Add Team Members; User Roles and Permissions", ""),
 ("ZD-C-095", "Security settings / اعدادات الامان", "اعدادات الامان; Security Settings", ""),
 ("ZD-C-096", "Domains / النطاقات", "شراء نطاق جديد; قائمة النطاقات; Custom Domain Linking; zid.store", ""),
 ("ZD-C-097", "Notifications and order status messages", "تنبيهات زد; إشعارات الفريق; رسائل حالات الطلب; Team Notifications; OneSignal Store Settings", ""),
 ("ZD-C-098", "Sender name / اسم المرسل", "تفعيل اسم المرسل; تجديد اسم المرسل; Sender Name", ""),
 ("ZD-C-099", "Checkout page settings / إعدادات صفحة إتمام عملية الشراء", "إعدادات صفحة إتمام عملية الشراء", ""),
 ("ZD-C-100", "Order and product properties / خصائص الطلبات والمنتجات", "خصائص الطلبات والمنتجات; Custom Fields", ""),
 ("ZD-C-101", "Gifting / خاصية الإهداء", "خاصية الإهداء", ""),
 ("ZD-C-102", "URL redirects / خاصية إعادة توجيه الروابط", "خاصية إعادة توجيه الروابط", ""),
 ("ZD-C-103", "Google Maps / تفعيل Google maps", "تفعيل Google maps", ""),
 ("ZD-C-104", "Working hours / اوقات العمل الرسمية", "اوقات العمل الرسمية", ""),
 ("ZD-C-105", "Reports and analytics / التقارير والتحليلات", "Reports & Analytics; التقارير والتحليلات", ""),
 ("ZD-C-106", "Marketing tools / أدوات التسويق", "Marketing Tools; Marketing & Growth Tools; أدوات التسويق والنمو", ""),
 ("ZD-C-107", "WhatsApp / واتساب زد", "Whatsapp; واتساب زد; Free WhatsApp (Basic Plan)", ""),
 ("ZD-C-108", "Zid POS / زد كاشير", "POS (Point of Sales); زد كاشير; Zid POS (Cashier)", ""),
 ("ZD-C-109", "Mazeed marketplace / مزيد", "Mazeed Marketplace; مزيد", ""),
 ("ZD-C-110", "Sales channels (marketplaces) / منصات البيع", "Marketplaces; Sold on Amazon and Trendyol and Jahez; منصات البيع", ""),
 ("ZD-C-111", "Zid Assurance / ضمان زد", "ZID Assurance; ضمان زد", ""),
 ("ZD-C-112", "Zid Voice", "Zid Voice; زد فويس", ""),
 ("ZD-C-113", "Online store and store design / المتجر الإلكتروني وتصميم المتجر", "E-store; Store Design; تصميم المتجر", ""),
 ("ZD-C-114", "Merchant support", "Live Chat Support; Ticketing & Chat System; 24/7 priority support", ""),
 ("ZD-C-115", "Zid Growth / زد نمو", "زد نمو", ""),
 ("ZD-C-116", "Store mobile app / تطبيق الجوال", "تطبيق الجوال", ""),
]
CIDS = [c[0] for c in CONCERNS]

# ---- mapping from inventory keys to concerns ----
API = {
 "Merchant APIs > Account > Me": ["ZD-C-077"], "Merchant APIs > Account > Store": ["ZD-C-077", "ZD-C-035", "ZD-C-050"],
 "Merchant APIs > Orders > Order Tags": ["ZD-C-080"], "Merchant APIs > Orders": ["ZD-C-080", "ZD-C-054"],
 "Merchant APIs > Reverse Orders": ["ZD-C-081", "ZD-C-054"], "Merchant APIs > Abandoned Carts": ["ZD-C-082"],
 "Merchant APIs > Products > Managing Products": ["ZD-C-083"], "Merchant APIs > Products > Digital Vouchers": ["ZD-C-043"],
 "Merchant APIs > Products > Product Categories": ["ZD-C-084"], "Merchant APIs > Products > Product Brands": ["ZD-C-083"],
 "Merchant APIs > Products > Product Badge": ["ZD-C-083"], "Merchant APIs > Products > Product Attributes": ["ZD-C-083"],
 "Merchant APIs > Products > Product Attribute Presets": ["ZD-C-083"], "Merchant APIs > Products > Product Variants": ["ZD-C-083"],
 "Merchant APIs > Products > Product Sorting": ["ZD-C-083"], "Merchant APIs > Products > Product Images": ["ZD-C-083"],
 "Merchant APIs > Products > Product Availability Notifications": ["ZD-C-087"], "Merchant APIs > Products > Product Export": ["ZD-C-083"],
 "Merchant APIs > Products > Product Stock": ["ZD-C-085"], "Merchant APIs > Products > Product Questions & Answers": ["ZD-C-086"],
 "Merchant APIs > Products > Product Reviews": ["ZD-C-086"], "Merchant APIs > Products > Digital Products": ["ZD-C-043"],
 "Merchant APIs > Inventories": ["ZD-C-085"], "Merchant APIs > Shipping": ["ZD-C-062"],
 "Merchant APIs > Marketing > Coupons": ["ZD-C-088"], "Merchant APIs > Marketing > Bundle Offers": ["ZD-C-089"],
 "Merchant APIs > Marketing > Loyalty Program": ["ZD-C-090"],
 "Merchant APIs > Marketing > Customer Wallets > Cashback Rules": ["ZD-C-019"], "Merchant APIs > Marketing > Customer Wallets > Wallet Analytics": ["ZD-C-019"],
 "Merchant APIs > Marketing > Customer Wallets > Manager Customer Wallet": ["ZD-C-019"],
 "Merchant APIs > Customers > Customer Tags": ["ZD-C-091"], "Merchant APIs > Customers > Customer Portal Tickets": ["ZD-C-092"],
 "Merchant APIs > Customers": ["ZD-C-091"], "Merchant APIs > Store Settings": ["ZD-C-077", "ZD-C-051", "ZD-C-012", "ZD-C-033", "ZD-C-097"],
 "Merchant APIs > Countries and Cities": ["ZD-C-033"],
 "Merchant APIs > Blogs > Settings": ["ZD-C-093"], "Merchant APIs > Blogs > Categories": ["ZD-C-093"], "Merchant APIs > Blogs > Posts > Media": ["ZD-C-093"],
 "Merchant APIs > Blogs > Posts": ["ZD-C-093"], "Merchant APIs > Blogs > Tags": ["ZD-C-093"], "Merchant APIs > Blogs > Storefront > Posts": ["ZD-C-093"],
 "Merchant APIs > Blogs > Storefront > Categories": ["ZD-C-093"], "Merchant APIs > Blogs > Storefront > Tags": ["ZD-C-093"],
 "Webhooks > APIs": ["ZD-C-072"], "App Management > APIs": ["ZD-C-022"],
 "API's > Authentication": ["ZD-C-075"], "API's > Products": ["ZD-C-075"], "API's > Categories": ["ZD-C-075"], "API's > Checkout": ["ZD-C-075"],
 "API's > Account": ["ZD-C-075"], "API's > Storefront": ["ZD-C-075"], "API's > Countries": ["ZD-C-075"],
 "Payment": ["ZD-C-010"], "ApplePay": ["ZD-C-010"], "Refund": ["ZD-C-010"], "Webhooks": ["ZD-C-010"],
}
SCOPE = {
 "third_account_identity_read": ["ZD-C-077"], "third_store_details_read": ["ZD-C-077", "ZD-C-050"], "third_store_business_read": ["ZD-C-035"],
 "third_store_details_write": ["ZD-C-077"], "third_order_read": ["ZD-C-080"], "third_order_write": ["ZD-C-080"], "third_create_order": ["ZD-C-080"],
 "orders.read_write": ["ZD-C-080", "ZD-C-081"], "orders.read": ["ZD-C-080", "ZD-C-054"], "abandoned_carts.read": ["ZD-C-082"],
 "third_abandoned_carts_read": ["ZD-C-082"], "products.read_write": ["ZD-C-083", "ZD-C-043", "ZD-C-086", "ZD-C-087"], "products.read": ["ZD-C-083", "ZD-C-043"],
 "third_categories_write": ["ZD-C-084"], "inventories.read_write": ["ZD-C-085"], "inventories.read": ["ZD-C-085"], "shipping.read": ["ZD-C-062"],
 "coupons.read": ["ZD-C-088"], "third_coupons_write": ["ZD-C-088"], "coupons.read_write": ["ZD-C-088"], "third_bundle_offers_read": ["ZD-C-089"],
 "third_bundle_offers_write": ["ZD-C-089"], "loyalty_program.read": ["ZD-C-090"], "loyalty_program.read_write": ["ZD-C-090"], "third_loyalty_read": ["ZD-C-090"],
 "third_customer_wallet_read": ["ZD-C-019"], "third_customer_wallet_write": ["ZD-C-019"], "third_customers_read": ["ZD-C-091"], "third_customers_write": ["ZD-C-091"],
 "account.read": ["ZD-C-077", "ZD-C-012"], "third_vat_read": ["ZD-C-051"], "countries_cities.read": ["ZD-C-033"], "third_one_signal_write": ["ZD-C-097"],
 "third_payment_read": ["ZD-C-012", "ZD-C-005"], "third_webhook_read": ["ZD-C-072"], "third_webhook_write": ["ZD-C-072"], "webhooks.read_write": ["ZD-C-072"],
 "embedded_apps_tokens_write": ["ZD-C-073"],
}
WH = {
 "order.create": ["ZD-C-080"], "order.status.update": ["ZD-C-080"], "order.payment_status.update": ["ZD-C-028"],
 "product.create": ["ZD-C-083"], "product.update": ["ZD-C-083"], "product.publish": ["ZD-C-083"], "product.delete": ["ZD-C-083"],
 "abandoned_cart.created": ["ZD-C-082"], "abandoned_cart.completed": ["ZD-C-082"],
 "customer.create": ["ZD-C-091"], "customer.update": ["ZD-C-091"], "customer.merchant.update": ["ZD-C-091"], "customer.login": ["ZD-C-091"],
 "category.create": ["ZD-C-084"], "category.update": ["ZD-C-084"], "category.delete": ["ZD-C-084"],
 "merchant_linked": ["ZD-C-010"], "payment_paid": ["ZD-C-010"], "refund_status_changed": ["ZD-C-010"],
}
SETTINGS = {
 "خاصية إعادة توجيه الروابط ( لوحة التحكم الجديدة)": ["ZD-C-102"], "الأسواق ( لوحة التحكم الجديدة )": ["ZD-C-034"],
 "الأسئلة الشائعة لضمان زد": ["ZD-C-111"], "الربط مع منصة فاتورة ZATCA ( لوحة التحكم الجديدة)": ["ZD-C-053"],
 "إشعارات الفريق ( لوحة التحكم الجديدة )": ["ZD-C-097"], "تفعيل Google maps ( لوحة التحكم الجديدة )": ["ZD-C-103"],
 "طلبات التصدير ( لوحة التحكم الجديدة )": ["ZD-C-044"], "خاصية الإهداء ( لوحة التحكم الجديدة )": ["ZD-C-101"],
 "قيود الشحن و الدفع (لوحة التحكم الجديدة )": ["ZD-C-063"], "إعدادات صفحة إتمام عملية الشراء ( لوحة التحكم الجديدة )": ["ZD-C-099"],
 "اعدادات الضريبة ( لوحة التحكم الجديدة )": ["ZD-C-051"], "خصائص الطلبات والمنتجات | المنتجات ( لوحة التحكم الجديدة )": ["ZD-C-100"],
 "خصائص الطلبات والمنتجات | الطلبات ( لوحة التحكم الجديدة )": ["ZD-C-100"], "اعدادات الفواتير (لوحة التحكم الجديدة )": ["ZD-C-052"],
 "لغة وعملات المتجر ( لوحة التحكم الجديدة )": ["ZD-C-050"], "اعدادات الامان (لوحة التحكم الجديدة )": ["ZD-C-095"],
 "اعدادات الحساب ( لوحة التحكم الجديدة )": ["ZD-C-077"], "تجديد اسم المرسل ( لوحة التحكم الجديدة )": ["ZD-C-098"],
 "تنبيهات زد ( لوحة التحكم الجديدة )": ["ZD-C-097"], "رسائل حالات الطلب ( لوحة التحكم الجديدة )": ["ZD-C-097"],
 "تفعيل اسم المرسل ( لوحة التحكم الجديدة )": ["ZD-C-098"], "الصفحات القانونية ( لوحة التحكم الجديدة )": ["ZD-C-039"],
 "بيانات المتجر لتجار السعودية ( لوحة التحكم الجديدة )": ["ZD-C-035"], "شراء نطاق جديد ( لوحة التحكم الجديدة)": ["ZD-C-096"],
 "قائمة النطاقات (لوحة التحكم الجديدة )": ["ZD-C-096"], "مجموعات الفريق ( لوحة التحكم الجديدة )": ["ZD-C-094"],
 "فريق العمل (لوحة التحكم الجديدة )": ["ZD-C-094"], "اوقات العمل الرسمية (لوحة التحكم الجديدة )": ["ZD-C-104"],
}
HELPPROD = {
 "مزيد": ["ZD-C-109", "ZD-C-024"], "مزيد›عن مزيد": ["ZD-C-109"], "مزيد›خصائص و مميزات مزيد": ["ZD-C-109"],
 "زد لوجيستك": ["ZD-C-060"], "زد لوجيستك›باقات البوليصات": ["ZD-C-060"], "زد لوجيستك›طرق الشحن": ["ZD-C-062", "ZD-C-060"],
 "زد لوجيستك›تتبع الشحنات": ["ZD-C-060"], "زد لوجيستك›اللوجستيات": ["ZD-C-060"],
 "زد باي": ["ZD-C-001", "ZD-C-002", "ZD-C-003", "ZD-C-004", "ZD-C-005", "ZD-C-008"], "زد باي›العمليات": ["ZD-C-002"],
 "زد باي›روابط الدفع": ["ZD-C-008"], "زد باي›الإيداعات": ["ZD-C-003"], "زد باي›الحسابات البنكية": ["ZD-C-004"],
 "زد باي›المدفوعات": ["ZD-C-005", "ZD-C-013"], "زد باي›تفعيل زد باي": ["ZD-C-001", "ZD-C-038"],
 "سوق التطبيقات": ["ZD-C-070"], "سوق التطبيقات›طرق الربط": ["ZD-C-070", "ZD-C-074"], "سوق التطبيقات›التطبيقات": ["ZD-C-070"],
 "سوق التطبيقات›تطبيق الجوال": ["ZD-C-116"], "زد نمو": ["ZD-C-115"], "زد كاشير": ["ZD-C-108"], "زد كاشير›عن زد كاشير": ["ZD-C-108"],
 "زد كاشير›خصائص و مميزات زد كاشير": ["ZD-C-108"], "تمويل زد": ["ZD-C-023"], "تمويل زد›تمويل زد": ["ZD-C-023"],
 "تمويل زد›إدارة التمويل": ["ZD-C-023"], "تمويل زد›متطلبات التمويل": ["ZD-C-023"], "سوق الثيمات": ["ZD-C-076"],
 "سوق الثيمات›الثيمات": ["ZD-C-076"], "سوق الثيمات›تحسين محركات البحث": ["ZD-C-106"], "سوق الثيمات›الصفحات": ["ZD-C-113"],
 "تطبيق الجوال": ["ZD-C-116"],
}
LEGAL = {
 "legal:terms-conditions": ["ZD-C-030", "ZD-C-020", "ZD-C-021", "ZD-C-036", "ZD-C-014", "ZD-C-016", "ZD-C-096"],
 "legal:privacy-policy": ["ZD-C-040", "ZD-C-041", "ZD-C-042"],
 "legal:zidpay-terms-conditions-sa": ["ZD-C-001", "ZD-C-002", "ZD-C-003", "ZD-C-006", "ZD-C-007", "ZD-C-009", "ZD-C-037"],
 "legal:zidpay-terms-conditions-kw": ["ZD-C-001", "ZD-C-002", "ZD-C-003", "ZD-C-006", "ZD-C-007", "ZD-C-009", "ZD-C-037"],
 "legal:domestic-shipping-terms": ["ZD-C-060"], "legal:global-shipping-terms": ["ZD-C-060"], "legal:logistics-t-and-cs": ["ZD-C-060"],
 "legal:complaints": ["ZD-C-092"],
 "legalsec:خدمة وكيل زد (Zid Agent)": ["ZD-C-025"], "legalsec:شركات الخدمات اللوجستية الطرف الثالث على متجر زد للتطبيقات (ZAM)": ["ZD-C-061"],
 "legalsec:زد شب": ["ZD-C-060", "ZD-C-015"], "legalsec:سوق تطبيقات زد": ["ZD-C-070", "ZD-C-022"], "legalsec:سوق ثيمات زد": ["ZD-C-076"],
 "legalsec:زد كاشير": ["ZD-C-108"], "legalsec:محفظة زد": ["ZD-C-017", "ZD-C-018"], "legalsec:خدمة المميزات الإضافية VAS": ["ZD-C-026"],
 "legalsec:مزيد": ["ZD-C-109", "ZD-C-024"], "legalsec:زد باي": ["ZD-C-001", "ZD-C-002", "ZD-C-003", "ZD-C-006", "ZD-C-007", "ZD-C-009", "ZD-C-037"],
 "legalsec:تمويل زد": ["ZD-C-023"], "legal:oauth-policy": ["ZD-C-071"],
 "legal:App Partner terms": ["ZD-C-070", "ZD-C-022"], "legal:Theme Partner terms": ["ZD-C-076"], "legal:Theme commercial policy": ["ZD-C-076"],
}
PRODLINES = {
 "E-store": ["ZD-C-113"], "POS (Point of Sales)": ["ZD-C-108"],
 "Payments": ["ZD-C-001", "ZD-C-002", "ZD-C-003", "ZD-C-005", "ZD-C-006", "ZD-C-007", "ZD-C-008"],
 "Shipping": ["ZD-C-060"], "Inventory Management": ["ZD-C-085"], "Zid Voice": ["ZD-C-112"], "Apps": ["ZD-C-070"], "Themes": ["ZD-C-076"],
 "Mazeed Marketplace": ["ZD-C-109"], "Financing": ["ZD-C-023"], "Marketing Tools": ["ZD-C-106"], "Marketplaces": ["ZD-C-110"],
 "ZID Assurance": ["ZD-C-111"], "Whatsapp": ["ZD-C-107"],
}
APPCAT_SHIP = {"5"}   # الشحن والتخزين

# plan feature lines: by group, with named exceptions
PLAN_GROUP = {"Basic Features": None, "Shipping": ["ZD-C-060"], "Payments": None, "Product & Inventory Management": ["ZD-C-083"],
              "Order Management": ["ZD-C-080"], "Marketing & Growth Tools": ["ZD-C-106"], "Reports & Analytics": ["ZD-C-105"],
              "Store Design": ["ZD-C-113"], "Customer Management": ["ZD-C-091"], "Other": None}
PLAN_LINE = {
 "Security Settings": ["ZD-C-095"], "Invoice Printing": ["ZD-C-052"], "Shipping Label Printing": ["ZD-C-060"],
 "Order Performance Indicator (Order Streaks)": ["ZD-C-105"], "Mobile & Tablet POS App": ["ZD-C-108"], "Account Details": ["ZD-C-077"],
 "WhatsApp Login": ["ZD-C-091"], "Customer Information": ["ZD-C-091"], "Add Team Members": ["ZD-C-094"], "Custom Domain Linking": ["ZD-C-096"],
 "Advanced Payment Methods": ["ZD-C-012", "ZD-C-013", "ZD-C-014"], "Live Chat Support": ["ZD-C-114"], "Invoice & Tax Settings": ["ZD-C-051", "ZD-C-052"],
 "CSS interface customization": ["ZD-C-113"], "Cash on Delivery Collection": ["ZD-C-015"],
 "Cash on Delivery": ["ZD-C-014"], "Bank Transfer Payment": ["ZD-C-016"], "Batch Print Shipping Papers": ["ZD-C-060"], "Payment Status": ["ZD-C-028"],
 "Bulk Payment Status Update": ["ZD-C-028"], "Various Payment Methods": ["ZD-C-012", "ZD-C-005", "ZD-C-013"], "Block Cash on Delivery": ["ZD-C-014"], "Card Discount": ["ZD-C-088"],
 "Product Categories": ["ZD-C-084"], "Best-Selling Products": ["ZD-C-105"], "Top-Selling Products": ["ZD-C-105"], "Product Management - Product Sales": ["ZD-C-105"],
 "Average Products per Order": ["ZD-C-105"], "Inventory Management": ["ZD-C-085"], "Inventory Withdrawal Priority": ["ZD-C-085"], "Export Full Quantities": ["ZD-C-085"],
 "Add Dynamic Bundle": ["ZD-C-089"], "Sales by Inventory Location": ["ZD-C-085"], "Inventory Management Logs": ["ZD-C-085"],
 "Product Management - Update Product Quantities": ["ZD-C-085"], "Product Availability Notification": ["ZD-C-087"], "Inventory Count": ["ZD-C-085"],
 "Product Cost Report": ["ZD-C-105"], "Transfer Inventory Between Branches": ["ZD-C-085"], "Request Inventory via POS": ["ZD-C-085", "ZD-C-108"],
 "Display Products by Customer City": ["ZD-C-085"],
 "Schedule Order Pickups - Zid Ship": ["ZD-C-060"], "Total Value of Carts Converted to Orders": ["ZD-C-082"], "Recovery Rate from Carts Converted to Orders": ["ZD-C-082"],
 "Total Order Sales Using Discount Codes": ["ZD-C-088"], "Orders per Auto Discount": ["ZD-C-088"], "Orders Using Discount Codes": ["ZD-C-088"],
 "Canceled Orders Value": ["ZD-C-105"], "Returned Orders": ["ZD-C-081"], "Order Status Notifications (Limited)": ["ZD-C-097"],
 "Order Click Rate": ["ZD-C-105"], "Order Management - Order Click Rate": ["ZD-C-105"],
 "Add Discount Coupons": ["ZD-C-088"], "Abandoned Cart Value": ["ZD-C-082"], "Abandoned Cart Count": ["ZD-C-082"], "Abandoned Cart Details": ["ZD-C-082"],
 "Abandoned Cart Stage": ["ZD-C-082"], "Abandoned Cart Sales Over Time": ["ZD-C-082"], "Total Abandoned Cart Value": ["ZD-C-082"],
 "Number of Discount Codes": ["ZD-C-088"], "Discounts": ["ZD-C-088"], "Multiple Coupons with Advanced Analytics": ["ZD-C-088"], "Coupons - Coupon Results": ["ZD-C-088"],
 "Average Cart Value": ["ZD-C-105"], "Loyalty - Points Expiry Period": ["ZD-C-090"], "Loyalty - Earned Points": ["ZD-C-090"],
 "Loyalty - Points Redemption Methods": ["ZD-C-090"], "Loyalty Programs": ["ZD-C-090"], "Loyalty - Redeemed Points": ["ZD-C-090"],
 "Review Management": ["ZD-C-086"], "Q&A and Review Messages": ["ZD-C-086"], "Points-Earning Customers": ["ZD-C-090"], "Customer Display Screen": ["ZD-C-108"],
 "Full & Partial Returns": ["ZD-C-081"], "Geo-Based Currency Settings": ["ZD-C-050"], "Team Notifications": ["ZD-C-097"],
 "Ticketing & Chat System": ["ZD-C-114"], "Message Settings": ["ZD-C-097"], "Sender Name": ["ZD-C-098"], "Message Language": ["ZD-C-097"],
 "Custom Fields": ["ZD-C-100"], "Tax-Applicable Countries": ["ZD-C-051"],
}
PLAN_OOS = {  # generic dashboard tools: the line ties them to no single concern
 "Universal Search Center": "A dashboard-wide search tool across products, orders and customers; the line ties it to no single concern.",
 "Bulk Actions": "A dashboard-wide bulk tool across products and customers; the line ties it to no single concern.",
 "Bulk Printing": "A dashboard-wide printing tool; the line names no data type, so it ties to no single concern.",
 "Data Filtering": "A dashboard-wide filter tool across products and customers; the line ties it to no single concern.",
 "Delete All": "A dashboard-wide bulk delete tool; the line ties it to no single concern.",
 "Disable All": "A dashboard-wide bulk disable tool for products or ads; the line ties it to no single concern.",
}
CARD = {
 "Add your products to mazeed marketplace in front of 5 million customers": ["ZD-C-109"], "Unlimited number of products, orders, and customers": ["ZD-C-020"],
 "Add discount coupons": ["ZD-C-088"], "Basic payment methods (bank transfer, cash on delivery)": ["ZD-C-014", "ZD-C-016"],
 "Integration with shipping companies via Zid logistics": ["ZD-C-060"], "50% cashback (for annual package only)": ["ZD-C-020"],
 "50% cashback (on annual plan only)": ["ZD-C-020"], "Store management authority for one extra person": ["ZD-C-094"],
 "Zid Payments gateway to accept Mada, Visa, and Mastercard": ["ZD-C-005"], "Enable Apple Pay for faster checkout": ["ZD-C-005"],
 "Access to themes store (Over 50 professional themes)": ["ZD-C-076"], "Link a custom domain to boost customer trust": ["ZD-C-096"],
 "Shipping rates starting from 11 SAR": ["ZD-C-060"], "Free WhatsApp (Basic Plan)": ["ZD-C-107"], "Free Zid POS on Basic Plan": ["ZD-C-108"],
 "One year free on Zid Cashier (Basic/Pro Package)": ["ZD-C-108"], "Calculate and display VAT": ["ZD-C-051"],
 "Store management access for 5 additional people": ["ZD-C-094"], "Inventory management across 2 branches or warehouses": ["ZD-C-085"],
 "Segment customers for exclusive offers": ["ZD-C-091"], "Fraud protection to prevent losses": ["ZD-C-007"],
 "Instant financing to grow your business with Zid Financing": ["ZD-C-023"], "CSS interface customization": ["ZD-C-113"],
 "Shipping rates starting from 10.5 SAR": ["ZD-C-060"], "24/7 priority support": ["ZD-C-114"],
 "Dedicated merchant relation manager to support your growth and improve performance": ["ZD-C-114"], "Shipping rates starting from 8.5 SAR": ["ZD-C-060"],
 "Completely free WhatsApp": ["ZD-C-107"], "Completely free Zid POS - two cashiers": ["ZD-C-108"], "Store management access for 20 additional people": ["ZD-C-094"],
 "Profitability and cost reports to optimize profit margins": ["ZD-C-105"], "Inventory management across 5 branches or warehouses": ["ZD-C-085"],
 "Complete loyalty program to increase customer retention": ["ZD-C-090"], "Connect your store with external systems (via API)": ["ZD-C-074"],
 "Inventory counting, transfer, and display by customer city": ["ZD-C-085"],
}

PERM = {
 "manage.store.marketing": ["ZD-C-106"], "manage.app.market.details": ["ZD-C-070", "ZD-C-022"], "manage.zidship.settings": ["ZD-C-060"],
 "manage.store.ecosystem.consultation": ["ZD-C-115"], "manage.store.ecosystem.packaging": ["ZD-C-115"], "manage.store.vat.settings": ["ZD-C-051"],
 "manage.store.discount.rules": ["ZD-C-088"], "pos.cashiers.page": ["ZD-C-108"], "manage.store.abandonedcarts": ["ZD-C-082"],
 "manage.store.bundleoffers": ["ZD-C-089"], "manage.zidpay.setting": ["ZD-C-001", "ZD-C-005"], "view.store.dashboard": ["ZD-C-105"],
 "pos.cashier.usage": ["ZD-C-108"], "manage.zidship.orders": ["ZD-C-060"], "pos.homepage": ["ZD-C-108"], "list.store.customers": ["ZD-C-091"],
 "manage.store.ecosystem.orderfulfillment": ["ZD-C-115"], "manage.app.market.settings": ["ZD-C-070"], "list.zidpay.transactions": ["ZD-C-002"],
 "manage.store.ecosystem.printings": ["ZD-C-115"], "view.app.market.home": ["ZD-C-070"], "view.zidship.reports": ["ZD-C-060"],
 "manage.zid.financing": ["ZD-C-023"], "manage.store.front.customization": ["ZD-C-113"], "list.store.orders": ["ZD-C-080"],
 "manage.store.ecosystem.designs": ["ZD-C-115"], "manage.store.custom.domain": ["ZD-C-096"], "manage.store.inventory.addresses": ["ZD-C-085"],
 "manage.store.ecosystem.payments": ["ZD-C-115"], "manage.store.ecosystem.marketing": ["ZD-C-115"], "list.store.products": ["ZD-C-083"],
 "manage.store.affiliate": ["ZD-C-106"], "list.store.categories": ["ZD-C-084"], "manage.store.ecosystem.mobileapps": ["ZD-C-116"],
 "manage.store.staff.notifications": ["ZD-C-097"], "manage.store.settings": ["ZD-C-077"], "manage.store.ecosystem.storepreparation": ["ZD-C-115"],
 "refund.zidpay.transactions": ["ZD-C-002"], "manage.zidship.payments": ["ZD-C-060"], "pos.payment.methods": ["ZD-C-108"],
 "manage.store.ecosystem.delivery": ["ZD-C-115"], "manage.store.ecosystem.selfstorage": ["ZD-C-115"], "manage.store.subscription": ["ZD-C-020"],
 "list.zidpay.deposits": ["ZD-C-003"], "pos.analytics": ["ZD-C-108"], "create.store.orders": ["ZD-C-080"], "list.store.order.drafts": ["ZD-C-080"],
 "manage.store.ecosystem.photographics": ["ZD-C-115"], "manage.store.account.settings": ["ZD-C-077"], "manage.store.ecosystem.workplaces": ["ZD-C-115"],
 "edit.store.orders": ["ZD-C-080"], "manage.store.zid.keys": ["ZD-C-074"], "manage.store.coupons": ["ZD-C-088"], "view.app.market.browse": ["ZD-C-070"],
 "manage.store.front.pages": ["ZD-C-113"],
}
PERM_OOS = {
 "view.zid.academy": "Access to Zid Academy, Zid's learning content for merchants; not a store or platform concern.",
 "view.store.home": "Access to a dashboard home page; the permission ties to no single concern.",
}

def map_entry(e):
    """Return (concern_ids, out_of_scope_reason)."""
    k = e["key"]; kind, _, rest = k.partition(":")
    if kind == "api": return API[rest], ""
    if kind == "wh":
        if rest.startswith("app.market."):
            if "subscription" in rest or "plan" in rest: return ["ZD-C-022"], ""
            if rest == "app.market.application.authorized": return ["ZD-C-071"], ""
            return ["ZD-C-070"], ""
        return WH[rest], ""
    if kind == "scope": return SCOPE[rest], ""
    if kind == "set": return SETTINGS[rest], ""
    if kind == "hp": return HELPPROD[rest], ""
    if kind == "hps": return HELPPROD[rest], ""
    if kind in ("legal", "legalsec"): return LEGAL[k], ""
    if kind == "appcat":
        return (["ZD-C-061"] if rest in APPCAT_SHIP else ["ZD-C-070"]), ""
    if kind == "pl": return PRODLINES[rest], ""
    if kind == "perm":
        if rest in PERM_OOS: return [], PERM_OOS[rest]
        return PERM[rest], ""
    if kind == "country": return (["ZD-C-032", "ZD-C-031"] if rest == "Egypt" else ["ZD-C-032"]), ""
    if kind == "apptype":
        return ({"Public apps": ["ZD-C-070"], "Private apps": ["ZD-C-074"]}.get(rest, ["ZD-C-061"])), ""
    if kind == "card":
        line = rest.split("›", 1)[1]
        return CARD[line], ""
    if kind == "plan":
        group, line = rest.split("›", 1)
        if line in PLAN_OOS: return [], PLAN_OOS[line]
        if line == "Zid Wallet": return (["ZD-C-017"] if group == "Basic Features" else ["ZD-C-019"]), ""
        if line in PLAN_LINE: return PLAN_LINE[line], ""
        if PLAN_GROUP.get(group): return PLAN_GROUP[group], ""
        raise KeyError(k)
    raise KeyError(k)
