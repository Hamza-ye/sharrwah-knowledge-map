# Inventory rows from the WooCommerce 11.2.1 release code, read as text (never executed).
# Each row: list, entry (the platform's own name), path, line, quote (the source line, verbatim), note.
# Usage: python3 -I inv_release.py  -> out/inv_release.json and a size summary per list
import json, os, re, html, glob, collections

R = "/home/user/woocommerce-release/11.2.1/woocommerce"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
rows = []
_lines = {}


def lines(path):
    if path not in _lines:
        _lines[path] = open(os.path.join(R, path), encoding="utf-8", errors="replace").read().split("\n")
    return _lines[path]


def quote_of(line, entry_hint=None):
    q = line.strip().replace("\t", " ")
    if len(q) <= 300:
        return q
    i = q.find(entry_hint) if entry_hint else 0
    i = max(0, i - 100)
    return q[i:i + 290].strip()


def add(lst, entry, path, lineno, note="", hint=None):
    line = lines(path)[lineno - 1]
    rows.append(dict(list=lst, entry=entry, path=path, line=lineno, quote=quote_of(line, hint), note=note))


def find(path, regex, start=1, end=None, nth=1):
    """1-based line number of the nth line matching regex within [start, end]."""
    L = lines(path)
    end = end or len(L)
    k = 0
    for i in range(start - 1, end):
        if re.search(regex, L[i]):
            k += 1
            if k == nth:
                return i + 1
    raise LookupError(f"{path}: {regex}")


def func_span(path, name):
    """Line span of a PHP function body (brace matching on text)."""
    L = lines(path)
    s = find(path, r"function\s+" + re.escape(name) + r"\s*\(")
    depth, opened = 0, False
    for i in range(s - 1, len(L)):
        depth += L[i].count("{") - L[i].count("}")
        if "{" in L[i]:
            opened = True
        if opened and depth <= 0:
            return s, i + 1
    return s, len(L)


def label(s):
    return html.unescape(s).replace("&hellip;", "…")


TR = r"(?:__|_x|esc_html__|esc_html_x)\(\s*'((?:[^'\\]|\\.)*)'"

# ---------- settings: tabs and their own sections ----------
SET = "includes/admin/class-wc-admin-settings.php"
tab_files = []
for i, l in enumerate(lines(SET), 1):
    m = re.search(r"\$settings\[\] = include_once __DIR__ \. '/settings/(class-wc-settings-[a-z\-]+\.php)'", l)
    if m:
        tab_files.append("includes/admin/settings/" + m.group(1))
tab_label = {}
for f in tab_files:
    n = find(f, r"\$this->label\s*=")
    lab = label(re.search(TR, lines(f)[n - 1]).group(1))
    tab_label[f] = lab
    add("settings", lab, f, n, note="settings tab id: " + re.search(r"'([^']+)'", lines(f)[find(f, r"\$this->id\s*=") - 1]).group(1)
        if "'" in lines(f)[find(f, r"\$this->id\s*=") - 1] else "settings tab")
for f in tab_files:
    try:
        s, e = func_span(f, "get_own_sections")
    except LookupError:
        continue
    for i in range(s, e + 1):
        l = lines(f)[i - 1]
        m = re.search(r"(?:'([a-z_\-]*)'\s*=>|\$sections\['([a-z_\-]+)'\]\s*=)\s*" + TR, l)
        if m and "%s" not in l:
            add("settings", tab_label[f] + " > " + label(m.group(3)), f, i, note="settings section")
# Payments tab sections are React pages named by constants
PG = "includes/admin/settings/class-wc-settings-payment-gateways.php"
for c in ["MAIN_SECTION_NAME", "OFFLINE_SECTION_NAME", "COD_SECTION_NAME", "BACS_SECTION_NAME", "CHEQUE_SECTION_NAME"]:
    n = find(PG, r"const " + c + r"\s*=")
    add("settings", "Payments > " + re.search(r"=\s*'([^']+)'", lines(PG)[n - 1]).group(1), PG, n, note="settings section (React page)")
# default tax classes created on install (each gets a section on the Tax tab)
INS = "includes/class-wc-install.php"
for t in ["Reduced rate", "Zero rate"]:
    add("settings", "Tax > " + t + " rates", INS, find(INS, r"create_tax_class\( __\( '" + t), note="tax class created on install; the Tax tab lists '%s rates' per class")
# Status page tabs
ST = "includes/admin/views/html-admin-page-status.php"
for key in ["status", "tools", "logs"]:
    n = find(ST, r"^\s*'" + key + r"'\s*=>")
    add("admin-navigation", "Status > " + label(re.search(TR, lines(ST)[n - 1]).group(1)), ST, n)

# ---------- admin navigation ----------
NAV = [
    ("WooCommerce", "includes/admin/class-wc-admin-menus.php", r"add_menu_page\( __\( 'WooCommerce'"),
    ("WooCommerce > Home", "src/Internal/Admin/Homescreen.php", r"'title'\s*=> __\( 'Home'"),
    ("WooCommerce > Orders", "includes/class-wc-post-types.php", r"'menu_name'\s*=> _x\( 'Orders', 'Admin menu name'"),
    ("WooCommerce > Customers", "src/Internal/Admin/Analytics.php", r"'title'\s*=> __\( 'Customers'"),
    ("WooCommerce > Reports", "includes/admin/class-wc-admin-menus.php", r"add_submenu_page\( 'woocommerce', __\( 'Reports'"),
    ("WooCommerce > Settings", "includes/admin/class-wc-admin-menus.php", r"__\( 'Settings', 'woocommerce' \),"),
    ("WooCommerce > Status", "includes/admin/class-wc-admin-menus.php", r"__\( 'Status', 'woocommerce' \)"),
    ("WooCommerce > Extensions", "src/Internal/Admin/Marketplace.php", r"'title'\s*=> __\( 'Extensions'"),
    ("WooCommerce > Notifications", "src/Internal/StockNotifications/Admin/MenusController.php", r"__\( 'Stock Notifications'"),
    ("WooCommerce > Coupons", "src/Internal/Admin/Coupons.php", r"__\( 'Coupons', 'woocommerce' \),"),
    ("Products", "includes/class-wc-post-types.php", r"'menu_name'\s*=> _x\( 'Products', 'Admin menu name'"),
    ("Products > All Products", "includes/class-wc-post-types.php", r"'all_items'\s*=> __\( 'All Products'"),
    ("Products > Add New", "includes/class-wc-post-types.php", r"'add_new'\s*=> __\( 'Add New'"),
    ("Products > Categories", "includes/class-wc-post-types.php", r"'menu_name'\s*=> _x\( 'Categories'"),
    ("Products > Tags", "includes/class-wc-post-types.php", r"'menu_name'\s*=> _x\( 'Tags'"),
    ("Products > Brands", "includes/class-wc-brands.php", r"'menu_name'\s*=> __\( 'Brands'"),
    ("Products > Attributes", "includes/admin/class-wc-admin-menus.php", r"add_submenu_page\( 'edit.php\?post_type=product', __\( 'Attributes'"),
    ("Products > Reviews", "src/Internal/Admin/ProductReviews/Reviews.php", r"__\( 'Reviews', 'woocommerce' \),"),
    ("Products > Product Import", "includes/admin/class-wc-admin-importers.php", r"'name'\s*=> __\( 'Product Import'"),
    ("Products > Product Export", "includes/admin/class-wc-admin-exporters.php", r"'name'\s*=> __\( 'Product Export'"),
    ("Payments", "src/Internal/Admin/Settings/PaymentsController.php", r"\$menu_title = esc_html__\( 'Payments'"),
    ("Marketing", "src/Internal/Admin/Marketing.php", r"'title'\s*=> 'Marketing'"),
    ("Marketing > Overview", "src/Internal/Admin/Marketing.php", r"'title'\s*=> __\( 'Overview'"),
    ("Marketing > Coupons", "includes/class-wc-post-types.php", r"'menu_name'\s*=> _x\( 'Coupons', 'Admin menu name'"),
    ("Setup Wizard", "src/Admin/PageController.php", r"'title'\s*=> __\( 'Setup Wizard'"),
]
for entry, f, rx in NAV:
    add("admin-navigation", entry, f, find(f, rx))
AN = "src/Internal/Admin/Analytics.php"
s = find(AN, r"'id'\s*=> 'woocommerce-analytics',")
for i in range(s, s + 90):
    m = re.search(r"'title'\s*=> __\( '([^']+)'", lines(AN)[i - 1])
    if m and m.group(1) != "Customers":
        add("admin-navigation", ("Analytics" if m.group(1) == "Analytics" else "Analytics > " + m.group(1)), AN, i)

# ---------- REST API ----------
SV = "includes/rest-api/Server.php"
for ns in ["wc/v1", "wc/v2", "wc/v3", "wc-telemetry"]:
    add("api-resources", ns, SV, find(SV, r"^\s*'" + re.escape(ns) + r"'\s*=>"))
add("api-resources", "wc/v4", SV, find(SV, r"\$namespaces\['wc/v4'\]"), note="feature flag rest-api-v4")
RC = "src/StoreApi/RoutesController.php"
add("api-resources", "wc/store/v1", RC, find(RC, r"register_routes\( 'v1', self::\$api_namespace \. '/v1' \)"))
add("api-resources", "wc/private", RC, find(RC, r"register_routes\( 'private', 'wc/private' \)"))
AI = "src/Admin/API/Init.php"
add("api-resources", "wc-admin", AI, find(AI, r"wc_rest_should_load_namespace\( 'wc-admin' \)"))
add("api-resources", "wc-analytics", AI, find(AI, r"lazy_load_namespace\( 'wc-analytics'"))
WS = "includes/wccom-site/rest-api/endpoints/abstract-wc-rest-wccom-site-controller.php"
add("api-resources", "wccom-site/v3", WS, find(WS, r"\$namespace = 'wccom-site/v3'"))
for fn, ns in [("get_v3_controllers", "wc/v3"), ("get_v4_controllers", "wc/v4")]:
    s, e = func_span(SV, fn)
    for i in range(s, e + 1):
        m = re.search(r"^\s*'([a-z0-9\-]+)'\s*=>", lines(SV)[i - 1])
        if m:
            add("api-resources", ns + " > " + m.group(1), SV, i, note=("feature flag rest-api-v4" if ns == "wc/v4" else ""))
# Store API routes: class names listed in RoutesController, identifiers and paths in each route class
s, e = func_span(RC, "__construct")
group = ""
for i in range(s, e + 1):
    l = lines(RC)[i - 1]
    g = re.search(r"^\s*'(v1|private|shopper_lists)'\s*=>", l)
    if g:
        group = g.group(1)
    m = re.search(r"Routes\\V1\\(\w+)::IDENTIFIER", l)
    if m:
        cf = f"src/StoreApi/Routes/V1/{m.group(1)}.php"
        n = find(cf, r"const IDENTIFIER\s*=")
        ident = re.search(r"'([^']+)'", lines(cf)[n - 1]).group(1)
        try:
            pth = re.search(r"return '([^']+)'", lines(cf)[find(cf, r"return '/") - 1]).group(1)
        except LookupError:
            pth = ""
        ns = {"v1": "wc/store/v1", "private": "wc/private", "shopper_lists": "wc/store/v1"}[group]
        add("api-resources", f"{ns} > {pth or ident}", cf, n, note=f"Store API route {ident}" + (" (shopper lists feature)" if group == "shopper_lists" else ""))
# wc-admin and wc-analytics controllers: class lists in Init.php, rest_base in each class
for fn, ns in [("rest_api_init_wc_admin", "wc-admin"), ("rest_api_init_wc_analytics", "wc-analytics")]:
    s, e = func_span(AI, fn)
    for i in range(s, e + 1):
        m = re.search(r"'Automattic\\WooCommerce\\Admin\\API\\([\w\\]+)'", lines(AI)[i - 1])
        if not m:
            continue
        cls = m.group(1).replace("\\", "/")
        cf = f"src/Admin/API/{cls}.php"
        base = ""
        if os.path.exists(os.path.join(R, cf)):
            for j, l in enumerate(lines(cf), 1):
                b = re.search(r"\$rest_base\s*=\s*'([^']+)'", l)
                if b:
                    base = b.group(1); break
            nsl = [re.search(r"\$namespace\s*=\s*'([^']+)'", l) for l in lines(cf)]
            nsl = [x.group(1) for x in nsl if x]
            real_ns = nsl[0] if nsl else ns
        else:
            real_ns = ns
        add("api-resources", f"{real_ns} > {base} ({cls})" if base else f"{real_ns} > {cls}", AI, i, note="controller " + cls)
add("api-resources", "wc-admin > launch-your-store", AI, find(AI, r"\$controller\s*=\s*'Automattic\\WooCommerce\\Admin\\API\\LaunchYourStore'"), note="controller LaunchYourStore")
for f in sorted(glob.glob(os.path.join(R, "includes/wccom-site/rest-api/endpoints/class-*.php"))):
    p = os.path.relpath(f, R)
    n = find(p, r"\$rest_base\s*=")
    add("api-resources", "wccom-site/v3 > " + re.search(r"'([^']+)'", lines(p)[n - 1]).group(1), p, n)
TL = "includes/rest-api/Controllers/Telemetry/class-wc-rest-telemetry-controller.php"
add("api-resources", "wc-telemetry > tracker", TL, find(TL, r"\$rest_base = 'tracker'"))

# ---------- webhook topics ----------
WH = "includes/admin/settings/views/html-webhooks-edit.php"
s = find(WH, r"'woocommerce_webhook_topics'")
for i in range(s, s + 25):
    m = re.search(r"^\s*'([a-z\.]+)'\s*=>\s*" + TR, lines(WH)[i - 1])
    if m:
        add("webhook-topics", m.group(1), WH, i, note=label(m.group(2)))

# ---------- roles, capabilities, REST key permissions ----------
add("access-scopes", "customer", INS, find(INS, r"^\s*'customer',$"))
add("access-scopes", "shop_manager", INS, find(INS, r"^\s*'shop_manager',$"))
s, e = func_span(INS, "get_core_capabilities")
for cap in ["manage_woocommerce", "create_customers", "view_woocommerce_reports"]:
    add("access-scopes", cap, INS, find(INS, r"^\s*'" + cap + r"',", s, e))
add("access-scopes", "product, shop_order, shop_coupon", INS, find(INS, r"\$capability_types = array\(", s, e),
    note="each type gets edit_/read_/delete_/publish_ and term capabilities from the template that follows")
KE = "includes/admin/settings/views/html-keys-edit.php"
for k in ["read", "write", "read_write"]:
    n = find(KE, r"^\s*'" + k + r"'\s*=>")
    add("access-scopes", label(re.search(TR, lines(KE)[n - 1]).group(1)), KE, n)

# ---------- core payment gateways, shipping methods, integrations ----------
for cls, f in [("WC_Gateway_BACS", "includes/gateways/bacs/class-wc-gateway-bacs.php"), ("WC_Gateway_Cheque", "includes/gateways/cheque/class-wc-gateway-cheque.php"),
               ("WC_Gateway_COD", "includes/gateways/cod/class-wc-gateway-cod.php"), ("WC_Gateway_Paypal", "includes/gateways/paypal/class-wc-gateway-paypal.php")]:
    n = find(f, r"\$this->method_title\s*=")
    add("other:core-payment-gateways", label(re.search(TR, lines(f)[n - 1]).group(1)), f, n, note=cls)
for f in sorted(glob.glob(os.path.join(R, "includes/shipping/*/class-wc-shipping-*.php"))) + [os.path.join(R, "src/Blocks/Shipping/PickupLocation.php")]:
    p = os.path.relpath(f, R)
    n = find(p, r"\$this->method_title\s*=")
    idl = [re.search(r"\$this->id\s*=\s*'([^']+)'", l) for l in lines(p)]
    idv = next((x.group(1) for x in idl if x), "")
    add("other:core-shipping-methods", label(re.search(TR, lines(p)[n - 1]).group(1)) + (f" ({idv})" if idv else ""), p, n,
        note=("legacy method, loaded only if enabled before 2.6" if "legacy" in p else ""))
MX = "includes/integrations/maxmind-geolocation/class-wc-integration-maxmind-geolocation.php"
add("other:core-integrations", "MaxMind Geolocation", MX, find(MX, r"\$this->method_title\s*="))

# ---------- emails ----------
EM = "includes/class-wc-emails.php"
s, e = func_span(EM, "init")
for i in range(s, e + 1):
    m = re.search(r"'(WC_Email_\w+)'\s*\]?\s*=", lines(EM)[i - 1]) or re.search(r"^\s*'(WC_Email_\w+)'\s*=>", lines(EM)[i - 1])
    if m:
        cls = m.group(1)
        cf = "includes/emails/class-" + cls.lower().replace("_", "-") + ".php"
        n = find(cf, r"\$this->title\s*=")
        add("other:emails", label(re.search(TR, lines(cf)[n - 1]).group(1)) + f" ({cls})", cf, n,
            note="feature-gated" if "feature_is_enabled" in "".join(lines(EM)[max(0, i - 4):i]) else "")

# ---------- order statuses ----------
OF = "includes/wc-order-functions.php"
s, e = func_span(OF, "wc_get_order_statuses")
for i in range(s, e + 1):
    m = re.search(r"OrderInternalStatus::(\w+)\s*=>\s*_x\( '([^']+)'", lines(OF)[i - 1])
    if m:
        add("other:order-statuses", m.group(2), OF, i, note="OrderInternalStatus::" + m.group(1))
DO = "src/Blocks/Domain/Services/DraftOrders.php"
add("other:order-statuses", "Draft (checkout-draft)", DO, find(DO, r"\$statuses\[ self::DB_STATUS \] = _x\( 'Draft'"))

# ---------- features (Settings > Advanced > Features) ----------
FC = "src/Internal/Features/FeaturesController.php"
s, e = func_span(FC, "init_feature_definitions")
for i in range(s, e + 1):
    m = re.search(r"^\s*'name'\s*=>\s*__\( '([^']+)'", lines(FC)[i - 1])
    if m:
        add("other:features", label(m.group(1)), FC, i)
add("other:features", "High-Performance order storage", "src/Internal/DataStores/Orders/CustomOrdersTableController.php",
    find("src/Internal/DataStores/Orders/CustomOrdersTableController.php", r"__\( 'High-Performance order storage'"))
add("other:features", "Cost of Goods Sold", "src/Internal/CostOfGoodsSold/CostOfGoodsSoldController.php",
    find("src/Internal/CostOfGoodsSold/CostOfGoodsSoldController.php", r"__\( 'Cost of Goods Sold'"))

# ---------- privacy exporters and erasers ----------
PV = "includes/class-wc-privacy.php"
for i, l in enumerate(lines(PV), 1):
    m = re.search(r"add_(exporter|eraser)\( '([^']+)', __\( '([^']+)'", l)
    if m:
        add("other:privacy-exporters-erasers", f"add_{m.group(1)}: {m.group(3)}", PV, i)

# ---------- payment extension suggestions (Settings > Payments) ----------
PS = "src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php"
s = find(PS, r"const AIRWALLEX")
e = find(PS, r"const HELIOPAY")
for i in range(s, e + 1):
    m = re.search(r"^\s*const (\w+)\s*=\s*'([^']+)'", lines(PS)[i - 1])
    if m:
        add("other:payment-extension-suggestions", m.group(2), PS, i, note="const " + m.group(1))

# ---------- shipping partner suggestions ----------
DS = "src/Admin/Features/ShippingPartnerSuggestions/DefaultShippingPartners.php"
for i, l in enumerate(lines(DS), 1):
    m = re.search(r"^\s*'name'\s*=>\s*'([^']+)'", l)
    if m:
        add("other:shipping-partner-suggestions", m.group(1), DS, i)

# ---------- onboarding tasks ----------
for f in sorted(glob.glob(os.path.join(R, "src/Admin/Features/OnboardingTasks/Tasks/*.php"))):
    p = os.path.relpath(f, R)
    try:
        s, e = func_span(p, "get_title")
    except LookupError:
        continue
    body = "\n".join(lines(p)[s - 1:e])
    m = re.search(r"(?:__|_x)\(\s*'((?:[^'\\]|\\.)*)'", body, re.S)
    if m:
        k = s + body[:m.start(1)].count("\n")
        extra = re.search(r"\),\s*'(WooPayments)'\s*\)", body)
        add("other:onboarding-tasks", (label(m.group(1)).replace("%s", extra.group(1)) if extra else label(m.group(1))), p, k, note=os.path.basename(p)[:-4])

# ---------- extension points in the release code ----------
EXT = [
    ("WC_Payment_Gateway", "includes/abstracts/abstract-wc-payment-gateway.php", r"^abstract class WC_Payment_Gateway extends WC_Settings_API"),
    ("woocommerce_payment_gateways", "includes/class-wc-payment-gateways.php", r"apply_filters\( 'woocommerce_payment_gateways'"),
    ("WC_Payment_Gateway_CC", "includes/gateways/class-wc-payment-gateway-cc.php", r"^class WC_Payment_Gateway_CC extends WC_Payment_Gateway"),
    ("WC_Payment_Gateway_ECheck", "includes/gateways/class-wc-payment-gateway-echeck.php", r"^class WC_Payment_Gateway_ECheck extends WC_Payment_Gateway"),
    ("WC_Payment_Token", "includes/abstracts/abstract-wc-payment-token.php", r"^abstract class WC_Payment_Token"),
    ("WC_Shipping_Method", "includes/abstracts/abstract-wc-shipping-method.php", r"^abstract class WC_Shipping_Method extends WC_Settings_API"),
    ("woocommerce_shipping_methods", "includes/class-wc-shipping.php", r"apply_filters\( 'woocommerce_shipping_methods'"),
    ("WC_Integration", "includes/abstracts/abstract-wc-integration.php", r"^abstract class WC_Integration extends WC_Settings_API"),
    ("woocommerce_integrations", "includes/class-wc-integrations.php", r"apply_filters\( 'woocommerce_integrations'"),
    ("woocommerce_email_classes", "includes/class-wc-emails.php", r"apply_filters\( 'woocommerce_email_classes'"),
    ("woocommerce_get_settings_pages", SET, r"apply_filters\( 'woocommerce_get_settings_pages'"),
    ("WC_Address_Provider", "includes/abstracts/abstract-wc-address-provider.php", r"^abstract class WC_Address_Provider"),
    ("WC_Log_Handler", "includes/abstracts/abstract-wc-log-handler.php", r"^abstract class WC_Log_Handler"),
    ("woocommerce_webhook_topics", WH, r"'woocommerce_webhook_topics'"),
    ("woocommerce_rest_api_get_rest_namespaces", SV, r"'woocommerce_rest_api_get_rest_namespaces'"),
    ("woocommerce_admin_rest_controllers", AI, r"apply_filters\( 'woocommerce_admin_rest_controllers'"),
    ("wc_admin_register_page", "includes/react-admin/page-controller-functions.php", r"^function wc_admin_register_page\("),
    ("IntegrationInterface", "src/Blocks/Integrations/IntegrationInterface.php", r"^interface IntegrationInterface"),
    ("AbstractPaymentMethodType", "src/Blocks/Payments/Integrations/AbstractPaymentMethodType.php", r"^abstract class AbstractPaymentMethodType"),
    ("ExtendSchema", "src/StoreApi/Schemas/ExtendSchema.php", r"^final class ExtendSchema"),
    ("woocommerce_register_additional_checkout_field", "src/Blocks/Domain/Services/functions.php", r"function woocommerce_register_additional_checkout_field\("),
    ("FeaturesUtil::declare_compatibility", "src/Utilities/FeaturesUtil.php", r"public static function declare_compatibility\("),
]
for entry, f, rx in EXT:
    add("extension-points", entry, f, find(f, rx))

json.dump(rows, open(os.path.join(OUT, "inv_release.json"), "w"), ensure_ascii=False, indent=0)
c = collections.Counter(r["list"] for r in rows)
for k, v in c.items():
    print(v, k)
print(len(rows), "rows")
