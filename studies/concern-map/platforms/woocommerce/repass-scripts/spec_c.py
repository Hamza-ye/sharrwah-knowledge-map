# Re-pass spec, part C: core concerns (settings, capabilities, feature flags, hooks, REST, code paths).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from newcite import R, RL, RS, Web, Old, S, G

FC = "src/Internal/Features/FeaturesController.php"
GEN = "includes/admin/settings/class-wc-settings-general.php"
PROD = "includes/admin/settings/class-wc-settings-products.php"
ADV = "includes/admin/settings/class-wc-settings-advanced.php"
ACC = "includes/admin/settings/class-wc-settings-accounts.php"
SHIP = "includes/admin/settings/class-wc-settings-shipping.php"
PT = "includes/class-wc-post-types.php"
MENUS = "includes/admin/class-wc-admin-menus.php"
DEV = "https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/"

def FEAT(key, start, end, nth=1):
    """A span of one feature's definition in FeaturesController, from the line containing `start` to the line containing `end`."""
    return R(FC, start, end, after=key, nth=nth)

# ---------- WC-C-030 selling and shipping locations ----------
S("WC-C-030", "decides", R(GEN, "'title'    => __( 'Selling location(s)', 'woocommerce' ),", "'type'     => 'select',"), "woocommerce_allowed_countries")
S("WC-C-030", "decides", R(GEN, "'title'    => __( 'Shipping location(s)', 'woocommerce' ),", "'type'     => 'select',"), "woocommerce_ship_to_countries")
S("WC-C-030", "boundary", R("includes/class-wc-countries.php", "return apply_filters( 'woocommerce_countries_allowed_countries', $countries );"), "woocommerce_countries_allowed_countries")
S("WC-C-030", "boundary", R("includes/class-wc-countries.php", "return apply_filters( 'woocommerce_countries_shipping_countries', $countries );"), "woocommerce_countries_shipping_countries")

# ---------- WC-C-031 checkout rate limiting ----------
RLD = DEV + "apis/store-api/rate-limiting.md"
S("WC-C-031", "where", Web(RLD, "is available for Store API endpoints. This is optional and disabled by default.", "Rate Limiting for Store API endpoints"),
  "Rate Limiting for Store API endpoints")
S("WC-C-031", "decides", FEAT("'rate_limit_checkout'", "'is_experimental'", "'enabled_by_default'"), "rate_limit_checkout")
S("WC-C-031", "decides", Web(RLD, "When enabled via the UI, the rate limiting will only be applied to the `POST /checkout` and Place Order flow for Checkout block. The limit will be a maximum of 3 requests per 60 seconds.",
  "Checkout rate limiting"), "Checkout rate limiting")
S("WC-C-031", "decides", Web(RLD, "Currently, this feature is only controlled via the `woocommerce_store_api_rate_limit_options` filter.", "UI Control"),
  "woocommerce_store_api_rate_limit_options", scope="Store API endpoints")
S("WC-C-031", "boundary", R("src/StoreApi/Utilities/RateLimits.php", "'woocommerce_store_api_rate_limit_options',"), "woocommerce_store_api_rate_limit_options")
S("WC-C-031", "reason", Web(RLD, "The main purpose prevent abuse on endpoints from excessive calls and performance degradation on the machine running the store.",
  "Rate Limiting for Store API endpoints"), "Rate Limiting for Store API endpoints")

# ---------- WC-C-032 store data in the WordPress database ----------
DST = DEV + "best-practices/data-management/data-stores.md"
S("WC-C-032", "boundary", Web(DST, "Data store classes act as a bridge between WooCommerce's data CRUD classes (`WC_Product`, `WC_Order`, `WC_Customer`, etc) and the database layer.",
  "Introduction"), "data stores")
S("WC-C-032", "decides", Web(DST, "The data stores shipped with WooCommerce core (powered by WordPress' custom posts system and some custom tables) can be swapped out for a different database structure, type, or even be powered by an external API.",
  "Introduction"), "data stores")

# ---------- WC-C-033 HPOS ----------
HPOSD = "https://woocommerce.com/document/high-performance-order-storage/"
S("WC-C-033", "boundary", Web(HPOSD, "It uses Woo's Create, Read, Update, Delete (CRUD) design to store order data in custom tables optimized for WooCommerce queries, with minimal impact on the store's performance.",
  "High-Performance Order Storage"), "High-Performance Order Storage")
S("WC-C-033", "boundary", Web(DEV + "features/orders/high-performance-order-storage/enable-hpos.md",
  "The action `wc_schedule_pending_batch_process` checks whether there are orders that need to be backfilled.", "How to enable High Performance Order Storage"),
  "wc_schedule_pending_batch_process")
S("WC-C-033", "where", Web(HPOSD, "Order data is synced from the _posts and _postmeta table to four custom order tables: _wc_orders _wc_order_addresses _wc_order_operational_data _wc_orders_meta",
  "Background"), "custom order tables")
S("WC-C-033", "decides", R("src/Internal/DataStores/Orders/CustomOrdersTableController.php", "public const CUSTOM_ORDERS_TABLE_USAGE_ENABLED_OPTION = 'woocommerce_custom_orders_table_enabled';"),
  "woocommerce_custom_orders_table_enabled")

# ---------- WC-C-035 usage tracking ----------
S("WC-C-035", "decides", R(ADV, "'id'            => 'woocommerce_allow_tracking',", "'default'       => 'no',", after="'title'         => __( 'Enable tracking', 'woocommerce' ),"),
  "woocommerce_allow_tracking", note="Settings > Advanced > WooCommerce.com, Usage Tracking.")

# ---------- WC-C-036 remote logging ----------
S("WC-C-036", "decides", FEAT("'remote_logging'", "'enabled_by_default'", "'disable_ui'"), "remote_logging")
S("WC-C-036", "decides", R("src/Internal/Logging/RemoteLogger.php", "if ( ! WC_Site_Tracking::is_tracking_enabled() ) {", "return false;"), "RemoteLogger::is_remote_logging_allowed",
  note="Remote logging is not allowed unless usage tracking is enabled.")

# ---------- WC-C-037 store logs ----------
S("WC-C-037", "decides", R("src/Internal/Admin/Logging/Settings.php", "private const DEFAULTS = array(", ");"), "woocommerce_logs_ settings",
  note="Defaults for the settings under WooCommerce > Status > Logs > Settings (option prefix woocommerce_logs_).")

# ---------- WC-C-038 analytics and reports ----------
S("WC-C-038", "decides", FEAT("'analytics'                            => array(", "'option_key'", "'disable_ui'"), "analytics (woocommerce_analytics_enabled)")
S("WC-C-038", "decides", Old("WC-S-0043"), "wc-reports", note="The Reports page requires the view_woocommerce_reports capability.")
S("WC-C-038", "decides", R("src/Admin/PageController.php", "'capability' => 'view_woocommerce_reports',", after="public function register_page( $options ) {"),
  "PageController::register_page", note="The default capability for pages registered through wc_admin_register_page.")

# ---------- WC-C-045 personal data export, erasure and retention ----------
S("WC-C-045", "decides", R(ACC, "'id'       => 'woocommerce_erasure_request_removes_order_data',", "'default'  => 'no',", after="'title'    => __( 'Account erasure requests', 'woocommerce' ),"),
  "woocommerce_erasure_request_removes_order_data")

# ---------- WC-C-046 geolocation ----------
S("WC-C-046", "decides", R(GEN, "'id'       => 'woocommerce_default_customer_address',", "'type'     => 'select',"), "woocommerce_default_customer_address")
S("WC-C-046", "decides", Web("https://woocommerce.com/document/maxmind-geolocation-integration/",
  "Once geolocation is enabled, you'll need to create a MaxMind account and configure MaxMind via the Integration tab in WooCommerce > Settings.",
  "Enabling geolocation"), "Enabling geolocation")

# ---------- WC-C-047 address autocomplete ----------
S("WC-C-047", "decides", R(GEN, "'id'       => 'woocommerce_address_autocomplete_enabled',", "'default'  => 'no',"), "woocommerce_address_autocomplete_enabled")
S("WC-C-047", "decides", R(GEN, "'id'      => 'woocommerce_address_autocomplete_provider',", "'default' => $address_autocomplete_providers[0]->id ?? '',"),
  "woocommerce_address_autocomplete_provider", note="Shown when more than one provider is available.")

# ---------- WC-C-052 store currency ----------
S("WC-C-052", "decides", R(GEN, "'id'       => 'woocommerce_currency',", "'type'     => 'select',"), "woocommerce_currency")

# ---------- WC-C-054 core tax ----------
S("WC-C-054", "decides", R(GEN, "'id'       => 'woocommerce_calc_taxes',", "'desc_tip' => __( 'Rates will be configurable and taxes will be calculated during checkout.', 'woocommerce' ),"),
  "woocommerce_calc_taxes")

# ---------- WC-C-058 customs ----------
CUST = DEV + "features/products/product-customs-data.md"
S("WC-C-058", "where", Web(CUST, "WooCommerce stores three optional customs fields on products and variations.", "Product customs data"), "Product customs data")
S("WC-C-058", "decides", Web(CUST, "Open a product in the classic product editor. In **Product data → Shipping → Customs**, enter:", "Set customs details in the product editor"),
  "Product data > Shipping > Customs")
S("WC-C-058", "boundary", Web(CUST, "The `/wc/v3/products` and `/wc/v3/products/{product_id}/variations` endpoints expose `customs_commodity_code`, `customs_country_of_origin`, and `customs_description`.",
  "Use the REST API"), "customs_commodity_code, customs_country_of_origin, customs_description")
S("WC-C-058", "reason", Web(CUST, "They help merchants keep a description of goods for cross-border shipping. They do not calculate duties or produce shipping labels.",
  "Product customs data"), "Product customs data")

# ---------- WC-C-064 products ----------
S("WC-C-064", "decides", R(PT, "'capability_type'     => 'product',", "'map_meta_cap'        => true,"), "product (post type)")
S("WC-C-064", "where", R(PT, "'description'         => __( 'This is where you can browse products in this store.', 'woocommerce' ),"), "product (post type)")

# ---------- WC-C-065 reviews ----------
CRR = DEV + "features/email/customer-review-request.md"
S("WC-C-065", "decides", R(PROD, "'id'              => 'woocommerce_enable_reviews',", "'type'            => 'checkbox',"), "woocommerce_enable_reviews")
S("WC-C-065", "decides", Web(CRR, "The feature ships **off by default** behind the `customer_review_request` feature flag (beta). Merchants enable it under **WooCommerce → Settings → Advanced → Features**.",
  "Feature flag"), "customer_review_request")
S("WC-C-065", "where", Web(CRR, "The feature lives in the `Automattic\\WooCommerce\\Internal\\OrderReviews` namespace and registers its WordPress hooks only when the feature flag is on.",
  "Overview"), "Automattic\\WooCommerce\\Internal\\OrderReviews", scope="Customer review request")
S("WC-C-065", "boundary", Web(CRR, "routes `/review-order/{id}/?key={order_key}` to the WC-managed Review Order page and renders it through the `[woocommerce_review_order]` shortcode.",
  "How it works"), "/review-order/{id}/", scope="Customer review request")

# ---------- WC-C-066 downloads ----------
S("WC-C-066", "decides", R(PROD, "'id'       => 'woocommerce_file_download_method',", "'default'  => 'force',", after="'title'    => __( 'File download method', 'woocommerce' ),"), "woocommerce_file_download_method")
S("WC-C-066", "decides", R(PROD, "'id'            => 'woocommerce_downloads_require_login',", "'default'       => 'no',"), "woocommerce_downloads_require_login")
S("WC-C-066", "decides", R(PROD, "'id'            => 'woocommerce_downloads_grant_access_after_payment',", "'default'       => 'yes',"), "woocommerce_downloads_grant_access_after_payment")

# ---------- WC-C-067 product import and export ----------
S("WC-C-067", "decides", R("includes/admin/class-wc-admin-importers.php", "return current_user_can( 'edit_products' ) && current_user_can( 'import' );"), "import_allowed")
S("WC-C-067", "decides", R("includes/admin/class-wc-admin-exporters.php", "return current_user_can( 'edit_products' ) && current_user_can( 'export' );"), "export_allowed")
S("WC-C-067", "boundary", R("includes/import/abstract-wc-product-importer.php", "$object = apply_filters( 'woocommerce_product_import_pre_insert_product_object', $object, $data );"),
  "woocommerce_product_import_pre_insert_product_object")
S("WC-C-067", "boundary", R("includes/export/class-wc-product-csv-exporter.php", "\"woocommerce_product_export_{$this->export_type}_default_columns\","),
  "woocommerce_product_export_{export_type}_default_columns")

# ---------- WC-C-068 inventory ----------
S("WC-C-068", "decides", R(PROD, "'id'      => 'woocommerce_manage_stock',", "'type'    => 'checkbox',"), "woocommerce_manage_stock")
S("WC-C-068", "decides", R(PROD, "'desc'              => __( 'Hold stock (for unpaid orders) for x minutes.", "'type'              => 'number',"), "woocommerce_hold_stock_minutes")
S("WC-C-068", "decides", R(PROD, "'default'           => '60',", after="'id'                => 'woocommerce_hold_stock_minutes',"), "woocommerce_hold_stock_minutes")

# ---------- WC-C-069 back-in-stock notifications ----------
S("WC-C-069", "decides", FEAT("StockNotifications::FEATURE_NAME       => array(", "'option_key'", "'disable_ui'"), "customer_stock_notifications")
S("WC-C-069", "boundary", R("src/Internal/StockNotifications/Frontend/SignupRateLimiter.php", "do_action( 'woocommerce_customer_stock_notifications_signup_rate_limit_exceeded', $rate_limit_id, $user_email );"),
  "woocommerce_customer_stock_notifications_signup_rate_limit_exceeded")
S("WC-C-069", "boundary", R("src/Internal/StockNotifications/Emails/CustomerStockNotificationEmail.php", "$this->title       = __( 'Back in stock notification', 'woocommerce' );"),
  "CustomerStockNotificationEmail", note="An email sent to customers who signed up.")

# ---------- WC-C-070 orders ----------
S("WC-C-070", "decides", R(PT, "'capability_type'     => 'shop_order',", "'map_meta_cap'        => true,"), "shop_order (post type)")
S("WC-C-070", "decides", Old("WC-S-0039"), "woocommerce (admin menu)", note="The WooCommerce menu requires edit_others_shop_orders.")

# ---------- WC-C-071 refunds ----------
S("WC-C-071", "decides", R("includes/class-wc-ajax.php", "public static function refund_line_items() {", "wp_die( -1 );"), "refund_line_items")
S("WC-C-071", "responsible", Web("https://wordpress.com/tos/",
  "must maintain fair and legally compliant return, refund, cancellation, and adjustment policies and clearly explain how customers can request a refund.",
  "8. j. Ecommerce Services: Your responsibilities"), "8. j. Ecommerce Services: Your responsibilities", scope="Ecommerce Services (Terms 8.j)")

# ---------- WC-C-074 coupons ----------
S("WC-C-074", "decides", R(GEN, "'id'              => 'woocommerce_enable_coupons',", "'type'            => 'checkbox',"), "woocommerce_enable_coupons")
S("WC-C-074", "decides", R(PT, "'capability_type'     => 'shop_coupon',", "'map_meta_cap'        => true,"), "shop_coupon (post type)")

# ---------- WC-C-075 core shipping ----------
S("WC-C-075", "decides", R(SHIP, "'id'            => 'woocommerce_enable_shipping_calc',", "'type'          => 'checkbox',"), "woocommerce_enable_shipping_calc")

# ---------- WC-C-076 emails ----------
S("WC-C-076", "decides", R("includes/emails/class-wc-email.php", "'enabled'            => array(", "'default' => 'yes',"), "WC_Email: enabled",
  note="The default for each email that uses the base WC_Email form fields.")
S("WC-C-076", "decides", FEAT("'deferred_transactional_emails'", "'Send transactional emails asynchronously via Action Scheduler instead of during the current request.',", "'enabled_by_default'"),
  "deferred_transactional_emails")

# ---------- WC-C-078 REST API ----------
S("WC-C-078", "decides", FEAT("'rest_api_caching'", "'enabled_by_default'", "'disable_ui'"), "rest_api_caching")

# ---------- WC-C-080 roles and capabilities ----------
INST = "includes/class-wc-install.php"
S("WC-C-080", "decides", R(INST, "* Get capabilities for WooCommerce - these are assigned to admin/shop manager during installation or reset."), "WC_Install::get_core_capabilities")
S("WC-C-080", "decides", R(INST, "$capabilities['core'] = array(", ");", after="public static function get_core_capabilities() {"), "WC_Install::get_core_capabilities")
S("WC-C-080", "decides", R("includes/wc-rest-functions.php", "// Check to allow shop_managers to manage only customers."), "wc_rest_check_user_permissions")
S("WC-C-080", "boundary", R("includes/wc-rest-functions.php", "$shop_manager_editable_roles = apply_filters( 'woocommerce_shop_manager_editable_roles', array( 'customer' ) );"),
  "woocommerce_shop_manager_editable_roles")
S("WC-C-073", "decides", R(INST, "// Customer role.", "'read' => true,"), "customer (role)")

# ---------- WC-C-081 store administration ----------
S("WC-C-081", "decides", Old("WC-S-0039"), "woocommerce (admin menu)")
S("WC-C-081", "decides", R("src/Internal/Admin/Homescreen.php", "'id'         => 'woocommerce-home',", "'capability' => 'read',", nth=2), "woocommerce-home")

# ---------- WC-C-082 site visibility ----------
S("WC-C-082", "decides", R(INST, "public static function add_coming_soon_option() {", "add_option( 'woocommerce_store_pages_only', 'yes' );"), "woocommerce_coming_soon",
  note="The method's docblock: 'Add the coming soon options for new shops.'")
S("WC-C-082", "reason", R(INST, "* Ensure that the options are set for all shops for performance even if core profiler is disabled on the host."), "WC_Install::add_coming_soon_option")
S("WC-C-082", "boundary", Web(DEV + "extensions/extension-onboarding/integrating-coming-soon-mode.md",
  "add_action( 'update_option_woocommerce_coming_soon', 'clear_server_cache', 10, 3 );", "Clear server cache on site visibility settings change"),
  "update_option_woocommerce_coming_soon")
S("WC-C-082", "reason", Web(DEV + "extensions/extension-onboarding/integrating-coming-soon-mode.md",
  "By default, Coming-soon pages are set with `Cache-Control: max-age=60` header. This setting enables CDNs and other caching mechanisms to cache the page for 60 seconds, balancing the need for efficient performance with reasonable update times.",
  "Clear server cache on template changes"), "Cache-Control: max-age=60", scope="coming-soon pages")

# ---------- WC-C-083 status ----------
S("WC-C-083", "decides", Old("WC-S-0045"), "wc-status")

# ---------- WC-C-084 marketing ----------
S("WC-C-084", "decides", R("src/Internal/Admin/Marketing.php", "'id'         => 'woocommerce-marketing',", "'capability' => 'manage_woocommerce',"), "woocommerce-marketing")

# ---------- WC-C-085 order attribution ----------
OAT = "https://woocommerce.com/document/order-attribution-tracking/"
S("WC-C-085", "where", Web(OAT, 'Within the order edit page for each new order, you\'ll find two meta boxes - "Order attribution" and "Customer history."', "Order Edit Page"),
  "Order attribution (meta box)")
S("WC-C-085", "where", Web(OAT, "As no data is stored in WooCommerce unless an order is placed and all cookies of this feature expire with each session, this feature cannot be used to track your visitors across sessions.",
  "Principles of Order Attribution Tracking"), "Principles of Order Attribution Tracking")
S("WC-C-085", "boundary", R("src/Internal/Orders/OrderAttributionController.php", "do_action( 'woocommerce_order_save_attribution_data', $order, $params );"),
  "woocommerce_order_save_attribution_data")
S("WC-C-085", "decides", R("src/Internal/Orders/OrderAttributionController.php", "$allow_tracking = wc_bool_to_string( apply_filters( 'wc_order_attribution_allow_tracking', true ) );"),
  "wc_order_attribution_allow_tracking")

# ---------- WC-C-086 extension framework ----------
S("WC-C-086", "decides", R(MENUS, "$settings_page = add_submenu_page(", "'wc-settings',"), "wc-settings", note="The settings page that extension settings pages are added to requires manage_woocommerce.")

# ---------- WC-C-087 block extensibility ----------
S("WC-C-087", "decides", FEAT("'cart_checkout_blocks'", "'description'", "'disable_ui'"), "cart_checkout_blocks")

# ---------- WC-C-088 feature settings ----------
S("WC-C-088", "where", R(FC, "if ( ! isset( $sections['features'] ) ) {", "$sections['features'] = __( 'Features', 'woocommerce' );"), "features (Settings > Advanced)")
S("WC-C-088", "decides", R(FC, "* Class to define the WooCommerce features that can be enabled and disabled by admin users,", "* (or incompatible) with a given feature."), "FeaturesController")
S("WC-C-088", "decides", R(FC, "'disable_ui'                   => false,", "'is_experimental'              => true,"), "FeaturesController::add_feature_definition",
  note="The values a feature definition gets when it does not set them.")

# ---------- WC-C-089 Point of Sale ----------
POSC = "src/Internal/POS/Capabilities.php"
S("WC-C-089", "decides", R(POSC, "* POS access is defined entirely by `woocommerce_pos_*` capabilities granted per-user", "* capabilities (those in all_pos_capabilities(); see has_pos_access())."),
  "woocommerce_pos_*")
S("WC-C-089", "reason", R(POSC, "* Capabilities are granted per-user via add_cap(), never bundled onto a WP role.", "* them roleless."), "woocommerce_pos_*")

# ---------- WC-C-090 mobile app and push notifications ----------
S("WC-C-090", "decides", FEAT("PushNotifications::FEATURE_NAME        => array(", "'is_experimental'", "'disable_ui'"), "push_notifications")

# ---------- WC-C-091 order withdrawal ----------
OWD = "https://woocommerce.com/document/customer-order-withdrawal/"
S("WC-C-091", "where", Web(OWD, "When a customer visits /my-account/withdraw-order/, they'll be presented with a withdrawal request form:", "How customers submit a request"),
  "/my-account/withdraw-order/")
S("WC-C-091", "where", R("src/Internal/OrderWithdrawal/OrderWithdrawalController.php", "private const ENDPOINT_SLUG   = 'withdraw-order';"), "withdraw-order")
S("WC-C-091", "decides", FEAT("'order_withdrawal'", "'description'", "'disable_ui'"), "order_withdrawal")
S("WC-C-091", "decides", Web(OWD, "WooCommerce uses the order's creation date only to show an age warning to the merchant; it does not determine whether the customer has a legal right to withdraw.",
  "Submission limits and timing"), "Submission limits and timing")
S("WC-C-091", "responsible", Web(OWD, "The customer order withdrawal feature does not guarantee compliance. For advice specific to your business and customers' locations, consult a qualified legal professional.",
  "Customer Order Withdrawal"), "Customer Order Withdrawal")
S("WC-C-091", "boundary", Web(OWD, "Successful requests that match an order also add an order note and an inbox notification, even if the merchant email is disabled.",
  "Review a withdrawal request"), "Review a withdrawal request")

# ---------- WC-C-092 fulfillments ----------
S("WC-C-092", "decides", FEAT("'fulfillments'                         => array(", "'enabled_by_default'", "'disable_ui'"), "fulfillments")

# ---------- WC-C-093 cost of goods sold ----------
COGS = "src/Internal/CostOfGoodsSold/CostOfGoodsSoldController.php"
S("WC-C-093", "decides", R(COGS, "'description'                  => __( 'Allows entering cost of goods sold information for products.', 'woocommerce' ),", "'enabled_by_default'           => false,"),
  "cost_of_goods_sold")
S("WC-C-093", "where", R("includes/admin/meta-boxes/views/html-product-data-general.php", "'id'          => '_cogs_value',", "'label'       => __( 'Cost of goods', 'woocommerce' ) . ' (' . get_woocommerce_currency_symbol() . ')',"),
  "_cogs_value", note="A field of the product data panel (General tab) in the product editor.")
S("WC-C-093", "boundary", R("src/Internal/CostOfGoodsSold/CogsAwareRestControllerTrait.php", "$schema['properties']['cost_of_goods_sold'] = array(", "'description' => __( 'Cost of Goods Sold data.', 'woocommerce' ),"),
  "cost_of_goods_sold (REST product schema)")

# ---------- WC-C-094 Blueprint ----------
BP = "src/Admin/Features/Blueprint/RestApi.php"
S("WC-C-094", "decides", R(BP, "! current_user_can( 'manage_woocommerce' ) ||", "( is_multisite() && ! is_super_admin() )", after="public function check_import_permission() {"),
  "check_import_permission")
S("WC-C-094", "decides", R(BP, "// Only allow imports in coming soon mode.", "return false;"), "can_import_blueprint")
S("WC-C-094", "reason", R(BP, "// Blueprint imports can change network-wide settings, so require super admin on multisite."), "check_import_permission",
  scope="multisite")
S("WC-C-094", "boundary", R(BP, "'/blueprint/export',", after="public function register_routes() {"), "wc-admin/blueprint/export")

# ---------- WC-C-095 WooCommerce MCP ----------
MCP = "src/Internal/MCP/MCPAdapterProvider.php"
S("WC-C-095", "decides", FEAT("'mcp_integration'", "'enabled_by_default'", "'is_experimental'"), "mcp_integration")
S("WC-C-095", "boundary", R(MCP, "const MCP_NAMESPACE = 'woocommerce';"), "MCP_NAMESPACE")
S("WC-C-095", "boundary", R(MCP, "const MCP_ROUTE = 'mcp';"), "MCP_ROUTE")

# ---------- WC-C-097 shopper lists ----------
SLC = "src/Internal/ShopperLists/ShopperListsController.php"
S("WC-C-097", "where", R(SLC, "* Tracks which shopper-list types are turned on and registers the", "* user-facing pieces that depend on each."), "ShopperListsController")
S("WC-C-097", "decides", R(SLC, "private const SUPPORTED_LISTS = array(", "'wishlist'        => 'product_wishlist',"), "SUPPORTED_LISTS")
S("WC-C-097", "decides", FEAT("'product_wishlist'", "'is_experimental'", "'option_key'"), "product_wishlist")
S("WC-C-097", "decides", FEAT("'cart_save_for_later'", "'is_experimental'", "'enabled_by_default'"), "cart_save_for_later")

# ---------- WC-C-099 reference data ----------
S("WC-C-099", "where", R("i18n/countries.php", "* Returns an array of countries and codes."), "i18n/countries.php")
S("WC-C-099", "decides", R("i18n/countries.php", "* Country codes and names should follow the Unicode CLDR recommendation"), "i18n/countries.php")
S("WC-C-099", "boundary", R("includes/class-wc-countries.php", "$this->geo_cache['countries'][ $locale ] = apply_filters( 'woocommerce_countries', include WC()->plugin_path() . '/i18n/countries.php' );"),
  "woocommerce_countries")
