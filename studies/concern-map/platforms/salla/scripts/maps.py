# Mapping tables: inventory entry -> concern keys, or an out-of-scope reason (a string starting "OOS:").
import re

HEADING = "OOS: a group heading in the list; the entries under it are inventoried one by one"
DUP_TOPIC = "OOS: an event-model page whose topics are inventoried under webhook-topics"

MERCHANT_API = {
    "Orders": ["orders"], "Order Status": ["order_statuses"], "Order Histories": ["orders"],
    "Order Options": ["order_options"], "Order Assignment": ["order_assignment"], "Order Invoice": ["order_invoices"],
    "Products": ["products"], "Order Reservations": ["bookings"], "Product Tags": ["products"],
    "Product Options": ["product_options_variants"], "Product Images": ["products"],
    "Product Option Values": ["product_options_variants"], "Settlements": ["instant_settlements"],
    "Digitals Product": ["digital_products"], "Product Quantity": ["inventory"],
    "Product Variants": ["product_options_variants"], "Customers": ["customers"], "Customer Groups": ["customer_groups"],
    "Customer Wallet": ["customer_wallet"], "Abandoned Carts": ["abandoned_carts"], "Special Offers": ["special_offers"],
    "Affiliates": ["store_affiliates"], "Coupons": ["coupons"], "Reviews": ["reviews_questions"],
    "Feedbacks": ["reviews_questions"], "Order Items": ["orders"], "Branches": ["branches_warehouses"],
    "Branches Allocations": ["branches_warehouses"], "Shipments": ["shipments"],
    "Shipping Companies": ["own_carriers", "carrier_integrations"], "Shipping Zones": ["shipping_zones_rates"],
    "Shipping Routes": ["shipping_routes"], "Countries": ["geo_reference_data"], "Districts": ["geo_reference_data"],
    "Cities": ["geo_reference_data"], "Product Option Templates": ["product_options_variants"],
    "Shipping Delivery Promises": ["delivery_promises"], "Categories": ["categories"], "Settings": ["store_general"],
    "Store Scopes": ["markets"], "Brands": ["brands"], "Exports": ["import_export"], "Transactions": ["transactions"],
    "Payments": ["salla_payments", "bank_transfer"], "Currencies": ["store_currencies"], "Merchant": ["merchant_account"],
    "Taxes": ["tax_settings"], "SEO": ["seo"], "DNS Records": ["domain_dns"], "Languages": ["languages_translation"],
    "Employees": ["staff_roles"], "Advertisements": ["advertisements"], "Webhooks": ["webhooks"],
    "Custom URLs": ["pages_custom_urls"], "Loyalty Points": ["loyalty"], "Branch Delivery Zones": ["branch_pickup"],
}

MERCHANT_API_DOCS = {
    "Rate Limiting": ["api_rate_limits"], "Versioning": ["api_versioning"],
    "Responses": "OOS: describes response codes and error formats common to every API group",
    "Pagination": "OOS: describes paging mechanics common to every API group",
    "Support": ["platform_security_status", "developer_tooling"], "Security Considerations": ["platform_security_status"],
    "Welcome 👋": "OOS: an introduction page to the developer documentation",
    "Webhooks": ["webhooks"], "Conditional Webhooks": ["webhooks"], "Multi-Language Support": ["languages_translation"],
    "Get Started": "OOS: a tutorial page", "Create Your First App": "OOS: a tutorial page",
    "Authorization": ["oauth"], "Change Log": ["api_versioning"], "APIs": HEADING,
}

OTHER_API_FOLDERS = {
    # nav label -> folder name -> concerns
    "app-api": {"Root": "OOS: an unnamed root folder of the App API navigation", "App Snippets": ["app_snippets"],
                "App Details Builder": ["app_store"], "Settings": ["app_settings"], "Subscriptions": ["app_billing_partner_payouts"]},
    "app-functions": {"*": ["app_functions"]},
    "checkout-apis": {"*": ["checkout"]},
    "ecommerce-events": {"*": ["storefront_events"]},
    "embedded-sdk": {"Report Builder": ["report_builder"], "Report Types": ["report_builder"], "APIs": ["report_builder"],
                     "*": ["embedded_sdk"]},
    "partners-agent-kit": {"*": ["developer_tooling"]},
    "recurring-payments-api": {"*": ["recurring_payments"]},
    "salla-apps-playbook": {"*": ["developer_tooling"]},
    "salla-awb": {"*": ["shipping_apps"]},
    "salla-cli@20261009T033553Z": {"*": ["developer_tooling"]},
    "shipments-fulfillment-apis@20261009T001017Z": {"Shipments": ["shipping_apps", "shipments"],
                                                   "Shipping Companies": ["shipping_apps"], "Shipping Routes": ["shipping_apps", "shipping_routes"],
                                                   "*": ["shipping_apps"]},
    "twilight-engine@20261009T033553Z": {"*": ["themes"]},
    "twilight-sdk": {"Currency": ["storefront_sdk_components", "store_currencies"], "Loyalty": ["storefront_sdk_components", "loyalty"],
                     "*": ["storefront_sdk_components"]},
    "web-components": {"*": ["storefront_sdk_components"]},
}

DOCS_NAVBAR = {
    "Merchant API": ["oauth", "webhooks"], "Embedded SDK": ["embedded_sdk"], "Salla OAuth 2.0": ["oauth"],
    "Twilight Engine": ["themes"], "Twilight SDK": ["storefront_sdk_components"], "Web Components": ["storefront_sdk_components"],
    "Ecommerce Events": ["storefront_events"], "Component Bundle": ["storefront_sdk_components"], "Checkout APIs": ["checkout"],
    "Change Log": ["api_versioning"], "App Functions": ["app_functions"], "App API": ["app_store", "app_settings"],
    "Shipments & Fulfillment APIs": ["shipping_apps"], "Salla AWB": ["shipping_apps"],
    "Recurring Payments API": ["recurring_payments"], "Billing System Salla partners": ["app_billing_partner_payouts"],
    "Communication Apps": ["communication_apps"], "Partners Agent Kit": ["developer_tooling"],
    "Salla Apps Playbook": ["developer_tooling"], "Salla CLI": ["developer_tooling"],
    "Salla - Opensource": "OOS: a link to Salla's public code repositories",
    "Salla - Developers Community": "OOS: a link to the developer chat community",
    "Blog": "OOS: a link to the developer blog", "Developer Portal": ["partner_account"],
    "Merchant ": HEADING, "Storefront": HEADING, "Partner APIs": HEADING, "Dev Tools": HEADING,
}

APP_TYPES = {"app": ["app_store"], "shipping": ["shipping_apps"], "communication": ["communication_apps"]}

APP_CATEGORIES = {
    "Cross/up sell": ["app_store", "special_offers"], "ads Track": ["app_store", "pixels_feeds"],
    "Shipping and Delivery": ["app_store", "shipping_apps"], "Abandoned Cart": ["app_store", "abandoned_carts"],
    "Fulfillment": ["app_store", "shipping_apps"], "Drop shipping": ["app_store", "instant_settlements"],
    "Accounting & Finance": ["app_store", "accounting_erp"], "ERP system": ["app_store", "accounting_erp"],
    "Marketing": ["app_store", "marketing_campaigns"], "Analytics": ["app_store", "reports"],
    "AI-Driven Solutions": ["app_store"], "Email": ["app_store", "communication_apps"],
    "Geolocation": ["app_store", "customer_addresses"], "Site Optimization": ["app_store", "seo"],
    "SMS": ["app_store", "communication_apps"], "Chat": ["app_store"], "App Maker": ["app_store", "mobile_app"],
    "Others": ["app_store"], "All": "OOS: the 'All' filter of the category picker, not a category",
}
PORTAL_APP_CATEGORIES = {
    "shipping": ["app_store", "shipping_apps"], "accounting": ["app_store", "accounting_erp"],
    "marketing": ["app_store", "marketing_campaigns"], "analytics": ["app_store", "reports"],
    "email": ["app_store", "communication_apps"], "geolocation": ["app_store", "customer_addresses"],
    "optimize": ["app_store", "seo"], "sms": ["app_store", "communication_apps"], "chat": ["app_store"], "others": ["app_store"],
}

SCOPES = {
    "settings": ["store_general", "merchant_account"], "customers": ["customers"], "orders": ["orders"],
    "carts": ["abandoned_carts", "checkout"], "branches": ["branches_warehouses"], "categories": ["categories"],
    "brands": ["brands"], "products": ["products"], "webhooks": ["webhooks"], "payments": ["salla_payments"],
    "taxes": ["tax_settings"], "dns-records": ["domain_dns"], "specialoffers": ["special_offers"],
    "countries": ["geo_reference_data"], "shippings": ["shipments", "shipping_zones_rates"],
    "marketing": ["coupons", "store_affiliates"], "reviews": ["reviews_questions"],
    "metadata": ["store_currencies", "languages_translation", "seo", "geo_reference_data"],
    "transactions": ["transactions"], "settlements": ["instant_settlements"], "store-settings": ["store_general"],
    "exports": ["import_export"], "subscriptions": ["recurring_payments"], "customer-wallets": ["customer_wallet"],
}


for _k in list(SCOPES):
    SCOPES[_k] = SCOPES[_k] + ["app_scopes"]


def topic_concerns(t):
    t = t.strip().strip("`").strip()
    exact = {
        "order.status.updated": ["order_statuses"], "order.cancelled": ["order_cancellation"],
        "order.refunded": ["returns_refunds"], "order.coupon.updated": ["coupons", "orders"],
        "order.payment.updated": ["orders", "salla_payments"], "order.shipping.address.updated": ["orders", "customer_addresses"],
        "product.quantity.low": ["inventory"], "product.available": ["inventory"],
        "product.option.updated": ["product_options_variants"], "product.variant.updated": ["product_options_variants"],
        "product.channels.changed": ["sales_channels"], "product.publish": ["sales_channels"], "product.unpublish": ["sales_channels"],
        "customer.login": ["customer_login"], "customer.otp.request": ["customer_login"],
        "storetax.created": ["tax_settings"], "store.owner.changed": ["merchant_account"],
        "coupon.applied": ["coupons"], "review.added": ["reviews_questions"], "invoice.created": ["order_invoices"],
        "wallet.action": ["customer_wallet"], "shipping.company.created": ["own_carriers"],
        "shipping.company.updated": ["own_carriers"], "shipping.company.deleted": ["own_carriers"],
        "auth.otp.verification": ["communication_apps", "customer_login"],
    }
    if t in exact:
        return exact[t]
    pre = [
        ("order.shipment.return", ["returns_refunds", "shipments"]), ("order.shipment", ["shipments"]),
        ("order.", ["orders"]), ("product.", ["products"]), ("customer.", ["customers"]),
        ("category.", ["categories"]), ("brand.", ["brands"]), ("store.branch", ["branches_warehouses"]),
        ("abandoned.cart", ["abandoned_carts"]), ("specialoffer.", ["special_offers"]),
        ("shipping.zone", ["shipping_zones_rates"]), ("shipment.", ["shipments"]),
        ("subscription.", ["recurring_payments"]), ("app.", ["app_events"]), ("communication.", ["communication_apps"]),
    ]
    for p, c in pre:
        if t.startswith(p):
            return c
    return None


# Communication webhook types (sent to communication apps)
def comm_type_concerns(t):
    return ["communication_apps"]


SETTINGS_MENU = {
    "/profile": ["merchant_account"], "/general": ["store_general"], "/plan": ["store_plan"], "/stores": ["multi_stores"],
    "/billing": ["store_balance_billing"], "/payments": ["salla_payments"], "/domains": ["domain_dns"],
    "/checkout": ["checkout"], "/taxes-and-duties": ["tax_settings", "customs_duties"], "/channels": ["sales_channels"],
    "/inventory": ["inventory"], "/products": ["products"], "/orders": ["orders"],
    "/shipping": ["shipping_zones_rates", "salla_shipping_labels"], "/customers": ["customers"],
    "/coupons": ["coupons", "store_affiliates"], "/wallet": ["customer_wallet"], "/loyalty-program": ["loyalty"],
    "/gift-system": ["gifting"], "/blog": ["blog"], "/feedback": ["reviews_questions"],
    "/notifications": ["merchant_notifications"], "/apps": ["app_store"],
}

SETTINGS_SUB = {
    "blog/": ["blog"], "checkout/guest-checkout": ["checkout"], "coupons/multiple-coupons": ["coupons"],
    "coupons/marketer-assets": ["store_affiliates"], "coupons/welcome-email": ["store_affiliates"],
    "coupons/status-settings": ["store_affiliates"], "coupons/commission-period": ["store_affiliates"],
    "coupons/discount-priorities": ["special_offers"], "coupons/cashback-eligibility": ["customer_wallet"],
    "customers/login_methods": ["customer_login"], "customers/recaptcha": ["customer_login"],
    "customers/whatsapp_otp": ["customer_login", "communication_apps"], "customers/address": ["customer_addresses"],
    "feedback/": ["reviews_questions"], "general/store-information": ["store_general"],
    "general/languages": ["languages_translation"], "general/currencies": ["store_currencies"],
    "general/salla-mcp": ["ai_connector"], "general/maintenance-mode": ["store_general"], "gift-system/": ["gifting"],
    "markets/browse_product_method": ["markets", "branches_warehouses"], "markets": ["markets"], "loyalty-program/": ["loyalty"],
    "orders/processing/": ["order_processing_rules"], "orders/auto_complete": ["order_processing_rules"],
    "orders/order-statuses-in-reports": ["reports", "order_statuses"], "orders/shipping-label-deduction": ["salla_shipping_labels"],
    "orders/auto-restock": ["inventory"], "orders/control-refund": ["returns_refunds"], "orders/customer-notes": ["orders"],
    "orders/cancellation": ["order_cancellation"], "orders/reorder": ["orders"], "orders/edit-policy": ["orders"],
    "payments/payment-restrictions": ["payment_restrictions"], "products/products.recommendations": ["products"],
    "products/products.product_quantity": ["inventory"], "products/products.auto_pricing": ["products"],
    "products/products.product_tax_pricing": ["tax_settings"], "products/products.purchase_count": ["products"],
    "products/notify_availability": ["availability_wishlist"], "products/products.branch_sorting": ["branches_warehouses"],
    "products/filters": ["products"], "products/brand_options": ["brands"], "products/sync_ignore_sku": ["inventory"],
    "products/products.product_sorting": ["products"], "products/quick_donation": ["products"],
    "products/wishlist-notifications": ["availability_wishlist"], "profile/": ["merchant_account"],
    "shipping/shipping.cod": ["cod_salla_labels", "cod_own_carrier"], "wallet/": ["customer_wallet"],
}


def settings_sub_concerns(section):
    if section in SETTINGS_SUB:
        return SETTINGS_SUB[section]
    for k, v in SETTINGS_SUB.items():
        if k.endswith("/") and section.startswith(k):
            return v
    return None


MAIN_NAV_HREF = {
    "/orders": ["orders"], "/?settings=%2Forders": ["orders"], "/orders/statuses": ["order_statuses"],
    "/orders/auto-assignee": ["order_assignment"], "/orders/invoice-settings": ["order_invoices"],
    "/orders/reservations": ["bookings"], "/orders/custom-fields": ["order_options"], "/orders/options": ["order_options"],
    "/orders/exports": ["import_export"], "/orders/auto-tags": ["orders"], "/products": ["products"],
    "/?settings=%2Fproducts": ["products"], "/products/options": ["product_options_variants", "categories"],
    "/products/editor": ["products"], "/products/quantities/bulk": ["inventory"],
    "/products/inventory-transfer": ["branches_warehouses"], "/products/campaigns": ["preorder_campaigns"],
    "/products/restrictions": ["product_restrictions"], "/products/quantities": ["inventory"], "/importer": ["import_export"],
    "/products/imports": ["import_export"], "/products/exports": ["import_export"], "/products/branches": ["branches_warehouses"],
    "/products/branches/stock-management": ["branches_warehouses"], "/marketing/ads/dashboard": ["salla_ads"],
    "/marketing/integration-tools/snapchat": ["pixels_feeds"], "/marketing/carts": ["abandoned_carts"],
    "/marketing/coupons": ["coupons"], "/marketing/influencers": ["influencers"], "/marketing/offers": ["special_offers"],
    "/marketing/campaign/retargeting": ["marketing_campaigns"], "/marketing/calendar": ["marketing_campaigns"],
    "/marketing/customer_wallet": ["customer_wallet"], "/marketing/affiliate": ["store_affiliates"],
    "/marketing/seo/homepage": ["seo"], "/marketing/loyalty": ["loyalty"], "/marketing/quick_checkout": ["quick_checkout"],
    "/marketing/gift": ["gifting"], "/marketing/reorder-reminders": ["reorder_reminders"], "/themes": ["themes"],
    "/themes/marketplace": ["themes"], "/manage/domain": ["domain_dns"], "/channel/pages": ["pages_custom_urls"],
    "/manage/custom-urls": ["pages_custom_urls"], "/channel/sallapoint": ["salla_point"], "/channel/mobile": ["mobile_app"],
    "/themes/landing-pages": ["landing_pages"], "/channel/mahally": ["mahally"], "/customers": ["customers"],
    "/customers/settings": ["customers"], "/customers/groups": ["customer_groups"], "/customers/imports": ["import_export"],
    "/users": ["staff_roles"], "/users/roles": ["staff_roles"], "/users/targets": ["staff_roles"],
    "/reports/performance": ["reports"], "/reports/smart-analysis": ["reports"], "/reports": ["reports"],
    "/feedback": ["reviews_questions"], "/tickets": ["store_complaints"], "/shipping/tickets": ["quality_gateway"],
    "/channel/chat": ["salla_chat"], "/manage/complaints": ["store_complaints"],
    "/shipping": ["salla_shipping_labels", "own_carriers"], "/?settings=%2Fshipping": ["shipping_zones_rates"],
    "/shipping/packing": ["packaging"], "/shipping/logs": ["shipments"], "/shipping/setting/routes": ["shipping_routes"],
    "/shipping/international": ["international_shipping"], "/payments": ["salla_payments"],
    "/payments/wallet": ["epayments_balance_payouts", "store_balance_billing", "cod_salla_labels"],
    "/payments/rules": ["payment_restrictions"], "/payments/taxes": ["tax_settings"],
    "/payments/transactions": ["transactions"], "/payments/kyc": ["store_verification", "payout_bank_account"], "/apps/installed": ["app_store"],
    "/apps": ["app_store"], "/manage/experts": ["merchant_services_marketplace"], "/manage/webhooks": ["webhooks"],
    "/logs/audit": ["activity_logs"], "/logs/export": ["activity_logs", "import_export"],
    "/products/quantities/audit": ["inventory"], "/orders/trash": ["orders"], "/products/trash": ["products"],
    "/products/card-logs": ["digital_products"], "/logs/messages": ["merchant_notifications"],
    "/manage/languages/logs": ["languages_translation"],
    "/": "OOS: the dashboard home page, which summarises other concerns",
}
MAIN_NAV_BUTTON = {
    "Bulk status update": ["order_statuses"],
}

PARTNER_NAV = {
    "/": "OOS: the portal logo link", "#": "OOS: a menu opener without its own page",
    "/dashboard": ["partner_account"], "/apps": ["app_store"], "/themes": ["theme_partners"],
    "/themes/bundles": ["theme_partners", "storefront_sdk_components"], "/service": ["merchant_services_marketplace"],
    "/services/orders": ["merchant_services_marketplace"], "/services-provider-portfolio": ["merchant_services_marketplace"],
    "/affiliates/profile": ["partner_affiliate"], "/affiliates/marketplace": ["partner_affiliate"],
    "/affiliates/my-opportunities": ["partner_affiliate"], "/affiliates/orders": ["partner_affiliate"],
    "/affiliates/active-merchants": ["partner_affiliate"], "/influencer/profile": ["partner_affiliate"],
    "/influencers/campaigns": ["partner_affiliate", "influencers"], "/coupons": ["partner_affiliate"],
    "/affiliates": ["partner_affiliate"], "/subscriptions/apps": ["app_billing_partner_payouts"],
    "/subscriptions/themes": ["theme_partners"], "/subscriptions/theme-trials": ["theme_partners"],
    "/demo-stores": ["dev_stores"], "/store": ["dev_stores"], "/store-management": ["partner_store_access"],
    "/employees": ["partner_account"], "/payouts": ["app_billing_partner_payouts"], "/billing": ["app_billing_partner_payouts"],
    "/billing/operations": ["app_billing_partner_payouts"], "/settings": ["partner_account"], "/logs": ["webhooks"],
    "/conversations": ["partner_account"], "/message-center": ["partner_account"], "/help/resources": ["partner_account"],
    "/help/faq": ["partner_account"], "/help/support": ["partner_account"],
}

PLAN_TITLES = {
    "مزايا أساسية": HEADING, "عدد لا محدود من المنتجات": ["products"], "عدد لا محدود من الطلبات": ["orders"],
    "بوليصات شحن سلة المُخفضة": ["salla_shipping_labels"], "إضافة كل أنواع المنتجات": ["products"],
    "تفعيل الدفع الإلكتروني": ["salla_payments"], "إعلانات سلة": ["salla_ads"], "الدفع": HEADING,
    "التحويل البنكي": ["bank_transfer"], "نظام المدفوعات الفورية عبر سريع": ["bank_transfer"],
    "الدفع عند الاستلام": ["cod_salla_labels", "cod_own_carrier"], "الدفع عبر مدى": ["salla_payments"],
    "الدفع عبر البطاقة الائتمانية (فيزا وماستر كارد)": ["salla_payments"], "PayPal الدفع عبر": ["wallets_other_methods"],
    "Apple Pay الدفع عبر": ["salla_payments"], "stc pay الدفع عبر": ["salla_payments", "wallets_other_methods"],
    "Google Pay الدفع عبر": ["salla_payments"], "الدفع بالتقسيط عبر تابي وتمارا": ["bnpl"],
    "مكافأة الراجحي": ["wallets_other_methods"], "زر الشراء السريع": ["quick_checkout"],
    "إرسال رابط الدفع للعميل": ["payment_links"], "حاسبة رسوم المدفوعات الإلكترونية": ["payment_fees"],
    "إتاحة الدفع عبر +33 عملة": ["store_currencies"], "نظام الحماية من الاحتيال": ["fraud_protection"],
    "إدارة المنتجات": HEADING, "إضافة خيارات متعددة للمنتج الواحد": ["product_options_variants"],
    "تصنيفات المنتجات": ["categories"], "تعديل الكميات": ["inventory"], "إدارة المخزون": ["inventory"],
    "عرض مرات الشراء": ["products"], "عرض المنتجات التي نفدت في نهاية الصفحة": ["products"],
    "عرض منتجات قد تعجبك في صفحة المنتج": ["products"], "إظهار العروض الخاصة أسفل المنتج": ["special_offers"],
    "وسوم المنتجات": ["products"], "ترتيب المنتجات": ["products"], "إدارة الطلبات": HEADING,
    "استقبال الطلبات": ["order_processing_rules"], "تحديث حالة الطلب": ["order_statuses"],
    "طباعة فاتورة الطلب بالعربي والانجليزي": ["order_invoices"], "طباعة ملخص الطلب": ["orders"],
    "إنشاء طلب يدوي": ["orders"], "تعديل الطلب": ["orders"], "تعيين أوقات استقبال الطلبات": ["order_processing_rules"],
    "تعيين الحد اليومي للطلبات": ["order_processing_rules"], "تخصيص حالات الطلب": ["order_statuses"],
    "إدارة الحجوزات": ["bookings"], "تتبع الطلب عبر محفظة أبل (Apple Wallet)": ["orders"],
    "إدارة مجموعة طلبات كدفعة واحدة": ["orders"], "تصدير الطلبات": ["import_export"],
    "إدارة طلبات الاسترجاع الجزئي والكلي": ["returns_refunds"], "إرسال محتوى المنتجات الرقمية": ["digital_products"],
    "أدوات التسويق": HEADING, "كوبونات التخفيض": ["coupons"], "التسويق مع المؤثرين": ["influencers"],
    "السلات المتروكة": ["abandoned_carts"], "العروض الخاصة": ["special_offers"], "عروض السلة": ["special_offers"],
    "محفظة العميل  *برسوم إضافية": ["customer_wallet"], "عروض الكاش باك": ["customer_wallet"],
    "إنشاء مجموعة كوبونات": ["coupons"], "كوبونات محلي": ["coupons", "mahally"],
    "حملات تسويقية عبر الرسائل النصية وإشعارات التطبيق": ["marketing_campaigns"], "مدونة المتجر": ["blog"],
    "الطلب المباشر *برسوم إضافية": ["quick_checkout"], "الجدول الزمني للتسويق": ["marketing_campaigns"],
    "شريط إعلاني أعلى المتجر": ["advertisements"], "التسويق بالعمولة": ["store_affiliates"],
    "نظام ولاء العملاء *برسوم إضافية": ["loyalty"], "الشحن والتوصيل": HEADING,
    "الشحن العادي عبر سمسا، البريد السعودي، DHL Express، أي مكان، J&T Express": ["salla_shipping_labels", "carrier_integrations"],
    "الشحن الاقتصادي عبر مندوبي، ريدبوكس، سمسا (استلام وتسليم من الفرع)": ["salla_shipping_labels", "carrier_integrations"],
    "إتاحة الشحن المجاني": ["shipping_zones_rates"], "مستويات تسعير البوليصات": ["salla_shipping_labels"],
    "تخصيص تسعيرة الشحن": ["shipping_zones_rates"], "حاسبة تكلفة الشحن": ["salla_shipping_labels"],
    "بوابة الجودة": ["quality_gateway"], "ربط خاص بـ 190+ شركة شحن": ["own_carriers", "carrier_integrations"],
    "تعيين شروط الدفع عند الاستلام": ["cod_salla_labels", "cod_own_carrier"],
    "زيادة عدد الفروع *برسوم إضافية": ["branches_warehouses"], "إتاحة الاستلام من الفرع": ["branch_pickup"],
    "تصميم المتجر": HEADING, "اختيار ثيم المتجر": ["themes"], "تخصيص ثيم المتجر": ["themes"],
    "إنشاء نسخ متعددة من الثيم": ["themes"], "جدولة نشر النسخ": ["themes"], "حماية محتوى المتجر": ["themes"],
    "دومين المتجر": HEADING, "دومين سلة الافتراضي": ["domain_dns"], "شهادة SSL مجانية": ["domain_dns"],
    "حجز دومين خاص": ["domain_dns"], "نقل أو ربط دومين من طرف ثالث": ["domain_dns"], "إدارة إعدادات DNS": ["domain_dns"],
    "التقارير": HEADING, "ملخص أداء المتجر": ["reports"], "تحليلات الأرباح": ["reports"],
    "تقرير تكاليف وأرباح الشحن": ["reports"], "تحليلات المبيعات": ["reports"], "تحليلات العملاء": ["reports"],
    "تحليلات الزيارات": ["reports"], "أداء المتجر": ["reports"], "تقارير المبيعات": ["reports"],
    "تقارير المنتجات": ["reports"], "تقارير نظام الولاء": ["reports"],
    "تخصيص حالات الطلبات المشمولة في التقارير": ["reports"], "العملاء": HEADING, "فرز العملاء": ["customers"],
    "حظر العميل": ["customers"], "إضافة عميل جديد": ["customers"], "تعديل معلومات العميل": ["customers"],
    "استيراد العملاء": ["import_export"], "كشف العملاء غير الجادين": ["customers"], "محفظة المتجر والفوترة": HEADING,
    "إضافة وسحب رصيد المتجر": ["store_balance_billing"], "سجل المدفوعات الإلكترونية": ["epayments_balance_payouts"],
    "إعدادات الفوترة": ["store_balance_billing"], "قنوات البيع": HEADING, "منصة محلي": ["mahally"],
    "صانع التطبيقات *برسوم إضافية": ["mobile_app"], "سوق الجملة": ["wholesale_market"], "إدارة تجربة العميل": HEADING,
    "الأسئلة والتقييمات": ["reviews_questions"], "إتاحة إضافة صور في تقييم المنتج": ["reviews_questions"],
    "نظام التذاكر": ["store_complaints"], "إتاحة 40 لغة في المتجر": ["languages_translation"],
    "الترجمة الفورية *برسوم إضافية": ["languages_translation"], "الصفحات التعريفية": ["pages_custom_urls"],
    "موظفو المتجر": HEADING, "زيادة عدد المستخدمين *برسوم إضافية": ["staff_roles"],
    "إدارة الأدوار الوظيفية": ["staff_roles"], "إسناد الطلبات تلقائيًا للموظفين": ["order_assignment"],
    "إدارة الحساب والمتجر": HEADING, "تطبيق إدارة المتجر على أجهزة iOS و Android": ["merchant_account"],
    "إدارة الاشتراك في تطبيق سلة على iOS برصيد آيتونز": ["store_plan"], "تفعيل وضع صيانة المتجر": ["store_general"],
    "إمكانية تجميد الاشتراك السنوي حتى 30 يومًا": ["store_plan"],
    "حفظ الحسابات المفتوحة مؤخراً عند تسجيل الدخول": ["merchant_account"], "ميزة البحث في إعدادات المتجر": ["store_general"],
    "إدارة قائمة المتاجر المرتبطة": ["multi_stores"], "المزايا المتقدمة": HEADING,
    "إنشاء روابط مخصصة": ["pages_custom_urls"], "أرشيف الرسائل النصية": ["merchant_notifications"],
    "تفريغ الكاش": ["store_general"], "ميزة ترجمة الرسائل": ["languages_translation"],
    "بيع عبر نقاط البيع مع سلة بوينت": ["salla_point"], "جرد المنتجات والمخزون": ["inventory"],
    "تخصيص خيارات المتجر": ["store_general"], "ربط الخدمات الإضافية": ["app_store"],
    "استهداف السلات المتروكة": ["abandoned_carts"], "إضافة صفحات تعريفية للمتجر": ["pages_custom_urls"],
    "تصميم واجهة المتجر": ["themes"], "إحصائيات وتقارير أداء المتجر": ["reports"],
    "إطلاق عروض وخصومات": ["special_offers", "coupons"], "حجز اسم دومين (رابط) مُخصص لموقع متجرك": ["domain_dns"],
    "شحن محلي وعالمي مع أكثر من 100 شركة شحن": ["carrier_integrations"],
    "تفعيل الدفع الإلكتروني عبر مدى وأبل باي وتابي وغيرها": ["salla_payments", "bnpl"],
    "كوبونات تسويقية": ["coupons"], "صفحات هبوط المنتج": ["landing_pages"], "عروض البنك": ["bank_offers"],
    "قيود الشحن والتوصيل": ["shipping_zones_rates"], "تخصيص الثيم عبر CSS و JS": ["themes"],
    "بناء ثيم خاص عبر Salla Twilight": ["themes"], "تصنيف العملاء إلى مجموعات": ["customer_groups"],
    "إدارة مجموعة عملاء كدفعة واحدة": ["customers"], "الربط بهيئة الزكاة والضريبة والجمارك": ["zatca_einvoicing"],
    "سجل التصدير": ["activity_logs"], "سجل العمليات": ["activity_logs"],
    "إرسال الإخطارات لخدمات أخرى عبر Webhooks": ["webhooks"], "تفعيل فوري لضريبة القيمة المضافة": ["tax_settings"],
    "إرسال رابط التقييم للعميل": ["reviews_questions"], "تكرار الطلب": ["orders"], "إضافة تعليق على الطلب": ["orders"],
    "إضافة خيارات الطلب": ["order_options"], "إضافة حقول مخصصة للطلبات": ["order_options"],
    "توليد تحسينات SEO عبر الذكاء الاصطناعي *برسوم إضافية": ["seo", "ai_connector"],
    "إضافة حقول مخصصة للمنتج": ["products"], "إدارة خيارات التصفية الظاهرة للعميل": ["products"],
    "قيود المنتج": ["product_restrictions"], "ضريبة القيمة المضافة": ["tax_settings"], "تعيين قيود الدفع": ["payment_restrictions"],
    "تحسين ظهور المتجر على محركات البحث (SEO)": ["seo"], "عرض واحتساب ضريبة القيمة المضافة": ["tax_settings"],
    "إضافة حسابات الموظفين وإدارة صلاحياتهم": ["staff_roles"],
    "قيود الدفع والحماية من الاحتيال": ["payment_restrictions", "fraud_protection"],
    "الربط مع الخدمات الإضافية": ["app_store"], "الربط مع الخدمات المحاسبية": ["accounting_erp"],
    "الربط مع الخدمات الإعلانية": ["pixels_feeds"], "تصنيف تلقائي لمجموعات العملاء": ["customer_groups"],
    "تسويق واسع عبر واتساب وتويتر وانستجرام وجوجل": ["marketing_campaigns"],
    "ربط المتجر بخدمات محاسبية ومالية متكاملة": ["accounting_erp"],
    "تخصيص كل عناصر تصميم المتجر عبر CSS أو JS": ["themes"],
}

# Flags: concern -> list of flag names. Anything not listed is out of scope with FLAG_OOS.
FLAG_OOS = "OOS: a feature-flag name that does not identify a concern on its own (rollout, UI or internal toggle)"
FLAGS = {
    "carrier_integrations": "ajeek aymakan barq beez careem diggipacks eijack esnad-express fastcoo isnaad labaih mahmool mkhdoom mlcgo oto redbox road saee safe-arrival saudi-post shipox dhl-shipping-company salasa quick-shipping-company bullet-delivery bullet-delivery-page jnt flow-express fastlo-awb fedex bullet-delivery-v2 mahly-express tookan track ups xturbo zajil dhl-api show-thermal-dhl-policy",
    "activity_logs": "advance-audit-log export-logs",
    "languages_translation": "languages custom-message-translation",
    "accounting_erp": "daftra-service qoyod-service zoho-books-service accounting-service",
    "pixels_feeds": "google-tag google-merchant-feed google-site-verification facebook-catalog-feed tiktok-pixel snapchat-catalog-feed facebook-conversion snapchat-conversion tiktok-conversion twitter-pixel-v2 snapchat-extension utm-campaign",
    "marketing_campaigns": "klaviyo mailchimp-marketing external-campaign marketing-calendar one-signal one-signal-push-notification",
    "shipping_zones_rates": "shipping-rules shipping-pricing-promotions shipping-profiles shipping-rate-management shipping-private-city-restrict restrict-shipping-by-country restrict-shipping-companies-by-country enable-shipping-by-country shipping-delivery-zones free-shipping-channel-payment-rules advance-free-shipping",
    "shipments": "special-shipping-details shipping-customer-additional-info shipping-policy-archive shipping-management shipping-carrier-pickup order-print-multi-policy addressee-shipping sync-order-shipment-status thankyou-page-multi-shipments shipping-indicator",
    "markets": "multi-market-origin-country-filter multi-countries multi-countries-activate multi-countries-basic multi-countries-link multi-countries-advanced customize-login-for-multi-markets",
    "salla_shipping_labels": "shipping-tier-pricing-system shipping-postpaid-balance salla-policies-free-shipping-gift",
    "quality_gateway": "shipping-ticket-system shipping-feedback shipping-rating",
    "packaging": "shipments-packaging-system",
    "own_carriers": "multi-shipping-service-account direct-activate-shipping-company",
    "international_shipping": "international-product",
    "shipping_routes": "shipping-routes",
    "customer_addresses": "saudi-national-address national-address google-maps-service here-service location-i-q-service nominatim-service",
    "tax_settings": "tax-profiles tax-profiles-disable-usa-country tax product-price-tax-included avalara-tax",
    "cod_salla_labels": "cod-branded-route cod cash-on-delivery-settings",
    "cod_own_carrier": "cod cash-on-delivery-settings",
    "shipping_apps": "allow-external-shipment-reconnect storage-station shipping-fulfillment-centers",
    "delivery_promises": "delivery-promises",
    "fraud_protection": "sift",
    "seo": "seo-urls seo-meta-tag bulk-seo ai-seo-generator",
    "merchant_notifications": "sms-archive sms-sender sms-balance sender-name sender-name-ad mail-service",
    "communication_apps": "sms-gateways infobip-service mobily-service msegat-service unifonic-service nexmo-service twilio-service message-bird-service jawal-b-service turkey-sms-service malath-sms-service shamel-sms-service our-sms hisms-service bevatel-service taqnyat-service rbit-service mshastra-service connect-saudi-service whatsapp whatsapp-chat whatsapp-api whatsapp-communication",
    "webhooks": "webhooks webhook-channel",
    "app_functions": "app-functions",
    "staff_roles": "store-team user-advance-management",
    "multi_stores": "multi-stores store-management",
    "customer_login": "whatsapp-otp auth-recaptcha sso-login cross-store-login re-captcha-v3",
    "inventory": "inventory::print_export status-return-to-stock product-quantity-notify product-quantity-log hide-out-of-stock-products inventory-order inventory-management",
    "order_invoices": "order-warehouse-invoice order-print-multi-invoice control-generate-invoice",
    "special_offers": "promotion-title-and-subtitle special-offer special-offer-export discount-offer-table conditional-offer tiered-offer external-purchases-tiered-offer tiered-offer-hide-until-threshold prebuilt-cart-offer cart-offer-applied-tier enable-offers-for-mobile-app customer-group-offer",
    "store_verification": "kyc_new_workflow wathq-v6 sbc-registration",
    "import_export": "products-importer custom-import import-customers export-customers impex import-products export-products update-products export-all-order-products export-product-orders import-order-status product-export-templates order-export-templates export-templates products-competitor-import-banner",
    "advertisements": "advertisements",
    "external_gateways": "bayan-pay pay-tabs tap hyperpay moyasar knet qpay benefit omannet iyzico my-fatoorah paylink geidea",
    "salla_payments": "stc-pay apple-pay google-pay checkout-save-cards knet mada credit_card salla-pay-basic-trial restriction-online-payment-activation apple-pay.merchants",
    "checkout": "store-checkout guest-checkout embedded-login-checkout ucp-embedded-checkout",
    "quick_checkout": "quick-purchase quick-checkout",
    "landing_pages": "landing-pages landing-page-templates show-product-in-landing-page",
    "products": "quick-donation customer-recommendations bundle-zero-price-guard restriction-product-type product-sorting ai-driven-personalized-product ai-bundles size-guides promote-product-video product-tags product-certificates three-dimension-image virtooal product-template products-filters product-donation-options upload-gif-image product-sale-start product-advance-management product-default-weight product-show-sku product-preview advance-bundle-product metal-pricing product-score product-ai-enhance media-center maximum-uploaded-images bundle-section-products-limit",
    "bnpl": "tamara klarna deema tabby spotii emkan mispay madfu",
    "wallets_other_methods": "mokafaa-alrajhi paypal",
    "customer_wallet": "mahally-customer-wallet customer-wallet cashback-accessibility order-summary-cashback wallet-payment-offer-combination wallet-gift-card",
    "mahally": "mahally-customer-wallet mahly",
    "bank_transfer": "bank",
    "themes": "theme-preview component-advanced-visibility remove-salla-copyright content-copyright canvas-mode theme-custom-css theme-customization theme-advanced-activation theme-versions-management theme-trial-versions theme-version-screenshot theme-purchases ready-store-theme-purchase products-layout-views",
    "ai_connector": "suggested-by-moshamer merchant-multi-agent-assistant salla-mcp salla_gpt ai-product ai-description-generator ai-seo-generator",
    "mobile_app": "app-maker-ai-components store-app-request store-ios-app store-android-app app-maker store-app-webview mobile-laverne-theme store-app-scopes update-app-request-for-testing app-editor-enhancements",
    "customer_groups": "customer-group customer-groups-draft-status",
    "customers": "customer-tag custom-customer-fields customer-advance-management customer-metadata customers-bulk-actions customers-unisearch",
    "payment_restrictions": "customer-payment-white-list payments-rules",
    "reviews_questions": "customer-send-rating store-rating order-send-rating feedback-bulk-actions reviews-page pin-feedback review-factors feedback-video-attachments allow-reviews-from-product-page feedback feedback-reporting",
    "reports": "customer-wishlists-reports order-report-statuses reports app-performance-reports reports-download-async report-visit",
    "availability_wishlist": "wishlist-notifications product-availability-notify product-sku-availability-notify",
    "customer_data_rights": "customer-account-deletion customer-data-export website-cookies",
    "merchant_account": "store-two-factor-authentication biometric-verification",
    "domain_dns": "domain",
    "merchant_services_marketplace": "expert-marketplace expert-influencer-home recommended-services external-services services-redesign advanced-services-search services-home-algolia services-algolia-autocomplete services-apple-pay services-redirect partners-chat partners-chat-notifications",
    "influencers": "influencer-marketplace influencer-marketplace-soon advanced-influencers-search celebrity-marketing influencer-campaign-templates influencer-resource-page influencers-packages influencers-apple-pay",
    "store_affiliates": "affiliate-paid-ad coupon-affiliate affiliate affiliates-cta private_affiliate_link merchant-special-link affiliate-public-statistics affiliate-show-contacts affiliate-multi-scopes export_special_opportunity affiliates-attribution-settings affiliate-fixed-commission affiliate-marketer-budget affiliates-settings temp-affiliate-new-design temp-affiliate-create-opportunity temp-affiliate-image-preview",
    "app_store": "zapier-service intercom-service poptin convert-flow mouse-flow popup-smart justino heap-io heyflow-service microsoft-clarity apps-flayer webengage apps-bundles apps-card-v2 merchant-app-store-login salla-portal-marketplace install-new-hydra-method install-app-method-v2 new-apps app-actions-history apps-algolia-autocomplete apps-algolia-search apps-apple-pay apps-store-builder apps-country-filter apps-onboarding apps-plans-redesign app-details-support-revamp move-to-new-app-marketplace header-notify-app-subscription",
    "embedded_sdk": "apps-iframe-sections",
    "zatca_einvoicing": "zatca",
    "gifting": "buy-as-gift",
    "loyalty": "loyalty-system loyalty-system-v2 loyalty-free-product-pos",
    "coupons": "coupon-group coupon-export coupon-payment-method coupon-countries coupon-customer coupon-multi-market bundle-aware-coupon multi_coupon",
    "abandoned_carts": "abandoned-cart-rule abandoned-cart-complete-order abandoned-cart-cursor-pagination abandoned-cart-merchant-notifications",
    "reorder_reminders": "reorder-reminders",
    "salla_ads": "salla-ads",
    "orders": "order-comment order-setting order-estimate order-auto-tagging custom-orders-list order-advance-management order-reorder order-summary duplicated-order-check partial-payments customer-editing show-external-orders batch-order-items-save price-quote restore-data",
    "order_processing_rules": "receiving-orders-times receiving-orders-limit order-count-time",
    "order_statuses": "order-custom-statuses",
    "order_assignment": "order-assignment",
    "returns_refunds": "control-refund-status orders-bulk-remove-products-refund",
    "order_cancellation": "order-cancellation-reasons advanced-order-cancellation-statuses",
    "transactions": "payments-operations",
    "charity_gateways": "e-payment-charity",
    "recurring_payments": "recurring-payment recurring-apple-pay",
    "bank_offers": "bank-offer bank-offer-scope",
    "store_currencies": "reflect-market-currency currency currency-exchange",
    "branches_warehouses": "store-branch multi-warehouses manage-products-by-branches direct-default-branch-quantity unlimited-quantity-by-branch multi-warehouse-link",
    "pages_custom_urls": "store-menu custom-urls store-pages internal-pages",
    "store_general": "store-status made-in-ksa",
    "partner_store_access": "support-access",
    "blog": "store-blog",
    "salla_chat": "salla_chat",
    "salla_support": "intercom-complains intercom-campaign-complains support-plan",
    "salla_point": "app_pos salla-point-app",
    "partner_affiliate": "partner-affiliate partner-unlimited-affiliate partner-merchant-affiliate affiliate-referral",
    "store_plan": "enable-special-plan-purchase renew-price-by-slug plan-free-trial plans",
    "store_balance_billing": "billing-native payg-usage-billing",
    "brands": "brands",
    "product_options_variants": "product-option-color-and-image default-product-option-value",
    "bookings": "product-booking",
    "categories": "category-image google-taxonomy salla-taxonomy",
    "order_options": "order-options custom-fields",
    "salla_capital": "financial-support",
    "digital_products": "digital-code digital-file digital-product-settings",
    "product_restrictions": "sales-restrictions",
    "preorder_campaigns": "pre-order-campaigns",
    "sales_channels": "instagram-api brand-sales-channels",
}


def flag_index():
    idx = {}
    for c, names in FLAGS.items():
        for n in names.split():
            idx.setdefault(n, []).append(c)
    return idx


PERM_EXACT = {
    "complaint_management": ["store_complaints"], "product_browse_quantity_logs": ["inventory"],
    "products_stock_management": ["inventory"], "categories_management": ["categories"],
    "import_export_management": ["import_export"], "browse_digital_codes_logs": ["digital_products"],
    "pre_order_campaigns_management": ["preorder_campaigns"], "order_refund_payment": ["returns_refunds", "transactions"],
    "order_assign": ["order_assignment"], "order_assigned_notification": ["order_assignment"],
    "order_statuses_show": ["order_statuses"], "order_statuses_edit": ["order_statuses"],
    "order_edit_status_all": ["order_statuses"], "order_reservation_management": ["bookings"],
    "inventory_browse": ["inventory"], "inventory_management": ["inventory"],
    "ask_browse_review_shipping_companies": ["quality_gateway"], "loyalty_system_management": ["loyalty"],
    "browse_cashback_offers": ["customer_wallet"], "manage_cashback_offers": ["customer_wallet"],
    "delete_cashback_offers": ["customer_wallet"], "manage_influencers": ["influencers"], "browse_influencers": ["influencers"],
    "currency_setting_edit": ["store_currencies"], "domain_management": ["domain_dns"], "restore_data_management": ["orders", "products"],
    "store_setting_purchase_from_salla_store": ["store_balance_billing"], "shipping_options_management": ["shipping_zones_rates"],
    "wallet_and_invoices_management": ["store_balance_billing"], "register_fields_management": ["customer_login"],
    "size_guides_management": ["products"], "languages_management": ["languages_translation"],
    "landing_pages_management": ["landing_pages"], "quick_checkout_management": ["quick_checkout"],
    "quick_donation_management": ["products"], "shipping_rules_management": ["shipping_zones_rates"],
    "payments_rules_management": ["payment_restrictions"], "product_availability_notify_management": ["availability_wishlist"],
    "stock_settings_management": ["inventory"], "support_access_requests": ["partner_store_access"],
    "branches_management": ["branches_warehouses"], "gift_system_management": ["gifting"], "tax_management": ["tax_settings"],
    "webhook_management": ["webhooks"], "account_setting_management": ["merchant_account"],
    "business_certificate_management": ["store_verification"], "store_design_management": ["themes"],
    "marketplace_apps_management": ["app_store"], "app_builder_management": ["mobile_app"],
    "store_notification_settings_management": ["merchant_notifications"], "custom_urls_management": ["pages_custom_urls"],
    "made_in_ksa_management": ["store_general"], "shipment_history_management": ["shipments"],
    "payments_operations_management": ["transactions"], "audit_logs_management": ["activity_logs"],
    "whatsapp_chat_browse": ["communication_apps"], "export_logs_management": ["activity_logs"],
    "custom_fields_management": ["order_options"], "order_auto_assign_browse": ["order_assignment"],
    "order_auto_assign_management": ["order_assignment"], "payment_method_browse": ["salla_payments"],
    "payment_methods_activation": ["salla_payments"], "bank_accounts_management": ["bank_transfer"],
    "list_epayments": ["epayments_balance_payouts"], "quick_payment_direct": ["payment_links", "salla_point"],
    "sweply_browse": "OOS: names a service (sweply) whose purpose the list does not state",
    "sweply_management": "OOS: names a service (sweply) whose purpose the list does not state",
}
PERM_PREFIX = [
    ("dashboard_", ["reports"]), ("product", ["products"]), ("brands_", ["brands"]), ("custom_importer_", ["import_export"]),
    ("order_", ["orders"]), ("customer_", ["customers"]), ("inventory_transfer_", ["branches_warehouses"]),
    ("reviews_", ["reviews_questions"]), ("questions_", ["reviews_questions"]), ("report", ["reports"]),
    ("pages_", ["pages_custom_urls"]), ("blog_", ["blog"]), ("coupon_", ["coupons"]), ("campaign_", ["marketing_campaigns"]),
    ("forget_cart_", ["abandoned_carts"]), ("special_offers_", ["special_offers"]), ("advertisements_", ["advertisements"]),
    ("seo_enhancement_", ["seo"]), ("affiliate_", ["store_affiliates"]), ("reorder_reminders_", ["reorder_reminders"]),
    ("salla_ads_", ["salla_ads"]), ("store_setting_", ["store_general"]), ("sms_archive_", ["merchant_notifications"]),
    ("users_", ["staff_roles"]), ("roles_", ["staff_roles"]), ("mahally_", ["mahally"]), ("salla_point_", ["salla_point"]),
    ("vendors_", ["wholesale_market"]),
]


def perm_concerns(key):
    if key in PERM_EXACT:
        return PERM_EXACT[key]
    for p, c in PERM_PREFIX:
        if key.startswith(p):
            return c
    return None


DASHBOARD_APPS = {
    "ui-merchant-orders": ["orders"], "ui-merchant-products": ["products"],
    "ui-merchant-widgets": "OOS: the dashboard home widgets bundle, which shows other concerns",
    "ui-merchant-reports": ["reports"], "ui-merchant-manage": ["pages_custom_urls", "webhooks", "store_complaints", "sanctions_screening", "store_currencies", "partner_store_access", "multi_stores"],
    "ui-merchant-login": ["merchant_account"], "ui-merchant-marketing-campaign": ["marketing_campaigns", "seo"],
    "ui-merchant-marketing": ["pixels_feeds", "store_affiliates", "advertisements", "gifting", "quick_checkout", "reorder_reminders"],
    "ui-merchant-services": ["influencers", "merchant_services_marketplace"], "ui-merchant-billing": ["store_balance_billing"],
    "ui-merchant-mahally": ["mahally"], "ui-merchant-pos": ["salla_point"], "ui-merchant-apps": ["app_store"],
    "ui-merchant-shipping": ["salla_shipping_labels", "own_carriers", "shipping_zones_rates", "tax_settings"],
    "ui-merchant-domain": ["domain_dns"], "ui-merchant-users": ["staff_roles"], "ui-merchant-customers": ["customers"],
    "ui-merchant-themes": ["themes", "landing_pages"], "ui-merchant-devstore": ["dev_stores"], "ui-merchant-logs": ["activity_logs"],
    "ui-merchant-payments": ["salla_payments", "store_verification", "checkout"],
    "ui-merchant-partner-marketing": ["partner_affiliate", "store_affiliates", "influencers"],
    "ui-merchant-channel": ["sales_channels", "pages_custom_urls"], "ui-merchant-feedback": ["reviews_questions"],
    "ui-merchant-vendors": ["wholesale_market"], "ui-merchant-chat": ["salla_chat"], "ui-merchant-blog": ["blog"],
    "ui-merchant-languages": ["languages_translation"], "ui-merchant-onboarding": "OOS: the store onboarding flow, which leads into other concerns",
    "ui-merchant-persona": "OOS: a merchant profiling questionnaire bundle; the list does not state its purpose",
    "ui-merchant-ticketing-system": ["store_complaints"], "ui-merchant-app-maker": ["mobile_app"],
    "ui-merchant-setup": "OOS: a setup flow bundle that leads into other concerns", "ui-merchant-localization": ["languages_translation"],
    "ui-merchant-reports_mfe": ["reports"], "chat-mf": ["salla_chat"], "ui-merchant-gamification": "OOS: a gamification bundle; the list does not state its purpose",
    "ui-merchant-app-notification": ["salla_ads"], "ui-merchant-notifications": ["merchant_notifications"],
    "ui-merchant-ai-agent": ["ai_connector"], "themes-editor": ["themes"], "app-maker-editor": ["mobile_app"],
    "ui-merchant-engage": ["salla_ads"], "ui-merchant-{app-name}": ["embedded_sdk"], "ui-merchant-whatsapp": ["salla_ads"],
    "ui-merchant-coupons": ["coupons"], "ui-merchant-template": ["salla_ads"], "ui-merchant-embedded": ["embedded_sdk"],
    "ui-merchant-utils": ["store_general"], "ui-merchant-importer": ["import_export"],
    "ui-merchant-offers": ["special_offers", "bank_offers", "customer_wallet"], "ui-merchant-wallet": ["customer_wallet"],
    "ui-merchant-abandoned_carts": ["abandoned_carts"], "ui-merchant-rms": "OOS: a bundle named rms; the list does not state its purpose",
    "app-functions-types": ["app_functions"], "ui-merchant-loyalty": ["loyalty"], "ui-merchant-gift": ["gifting"],
    "ui-merchant-flows": "OOS: a workflow bundle; the list does not state its purpose", "ui-merchant-inventory": ["branches_warehouses", "inventory"],
    "ui-merchant-organization": "OOS: an organization bundle; the list does not state its purpose",
}


def dashboard_app_concerns(name):
    n = name.replace("@salla.sa/", "")
    if n in DASHBOARD_APPS:
        return DASHBOARD_APPS[n]
    if n.startswith("ui-merchant-ads") or n == "ui-merchant-marketing-credits":
        return ["salla_ads"]
    return None


STORE_PAYMENT_METHODS = {
    "mada": ["salla_payments"], "credit_card": ["salla_payments"], "apple_pay": ["salla_payments"],
    "stc_pay": ["salla_payments", "wallets_other_methods"], "google_pay": ["salla_payments"],
    "tabby_installment": ["bnpl"], "tamara_installment": ["bnpl"], "mispay_installment": ["bnpl"],
    "emkan_installment": ["bnpl"], "madfu_installment": ["bnpl"], "cod": ["cod_salla_labels", "cod_own_carrier"],
    "customer_wallet": ["customer_wallet"], "paypal": ["wallets_other_methods"], "bank": ["bank_transfer"],
    "mokafaa_alrajhi_loyalty": ["wallets_other_methods"],
}

STOREFRONT_API = {
    "advertisements": ["storefront_api", "advertisements"], "branches": ["storefront_api", "branches_warehouses"],
    "brands": ["storefront_api", "brands"], "categories": ["storefront_api", "categories"],
    "currencies": ["storefront_api", "store_currencies"], "menus-footer": ["storefront_api", "pages_custom_urls"],
    "menus-header": ["storefront_api", "pages_custom_urls"], "offers": ["storefront_api", "special_offers"],
    "product-cashback-offer": ["storefront_api", "customer_wallet"], "products-latest": ["storefront_api", "products"],
    "products-related": ["storefront_api", "products"],
}

ORDER_STATUSES = ["order_statuses"]


PLAN_KEYS_AR = {
    "عدد لا محدود من المنتجات": ["products"], "عدد لا محدود من الطلبات": ["orders"],
    "بوليصات شحن سلة المُخفضة": ["salla_shipping_labels"], "إضافة كل أنواع المنتجات": ["products"],
    "تفعيل الدفع الإلكتروني": ["salla_payments"], "إعلانات سلة": ["salla_ads"], "محلي": ["mahally"],
    "تحسين ظهور المتجر على محركات البحث (SEO)": ["seo"],
    "دعم ضريبة القيمة المضافة مع ربط بهيئة الزكاة": ["tax_settings", "zatca_einvoicing"],
}
PLAN_SECTION_OOS = "OOS: a section heading of the plan comparison table; its lines are not in the held page text"

SPECIAL_LINES = {
    "ربط تكاملي ذكي": ["app_store", "accounting_erp"],
    "نقل البيانات بسلاسة": ["import_export"],
    "إدارة مخزون متقدمة": ["branches_warehouses"],
    "رسوم مرنة لبوابة الدفع": ["payment_fees"],
    "تطبيق خاص بمتجرك": ["mobile_app"],
    "ابق متصلًا بالعالم مع خيارات الشحن المتنوعة في سلة، ودعم جميع وسائل الدفع الإلكتروني، وإيداع المبيعات كل 24 ساعة، لتجارة أيسر ونمو أسرع.": ["epayments_balance_payouts"],
    "فريقنا معك في كل خطوة": ["salla_support"],
    "الربط بمنصات التسوّق العالمية": ["sales_channels"],
    "مدير حساب مخصص": ["salla_support"],
    "استقرار المنصة وجاهزيتها للذروة": ["platform_security_status"],
    "بدون عمولة منصة على مبيعاتك": ["store_plan"],
    "تخصيص كامل للمتجر بدون كود": ["themes"],
    "البيع للشركات وبالجملة B2B": "OOS: a marketing line for selling to businesses; the page names no feature or setting behind it",
}

FOOTER_LEGAL = {
    "اتفاقية الاستخدام": ["terms_of_use"], "اتفاقية استخدام التسويق بالعمولة": ["affiliate_program_terms"],
    "سياسة الخصوصية": ["salla_privacy_policy"], "منصة الشكاوي": ["complaints_platform"],
}
FOOTER_MARKETS = {"مدعوم في:": "OOS: the heading of the footer's list of countries; the countries are inventoried one by one",
                  "السعودية": ["salla_markets_served"], "الامارات": ["salla_markets_served"]}


def legal_path_concerns(p):
    t = {"/terms": ["terms_of_use"], "/privacy": ["salla_privacy_policy"], "/policies/terms": ["terms_of_use"],
         "/policies/privacy": ["salla_privacy_policy"], "/policies/selling-policies": ["selling_policy"],
         "/policies/nd96": ["policy_nd96"], "/policies/publising-app-maker": ["app_maker_policy"],
         "/policies/اتفاقية-استخدام-التسويق-بالعمولة": ["affiliate_program_terms"],
         "/اتفاقية-استخدام-التسويق-بالعمولة": ["affiliate_program_terms"]}
    return t.get(p)
