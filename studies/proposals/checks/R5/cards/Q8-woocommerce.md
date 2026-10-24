# Cards: Q8 on woocommerce

22 records cited by `studies/proposals/drafts/Q8/draft.md`, made by `method/r5_cards.py`.

## The points cited

- **section 1, line 9:** - WooCommerce grows through extensions: "Grow your business with hundreds of free and paid extensions". Q8-WC-042
- **section 1, line 21:** - WooCommerce's shipped FeaturesController defines "the WooCommerce features that can be enabled and disabled by admin users". Q8-WC-K1310
- **section 1, line 34:** - WooCommerce's payment gateways "are class based and can be added through traditional plugins", loaded through the `woocommerce_payment_gateways` filter in shipped code; plugins add shipping rates through a "Shipping Method API". Q8-WC-K0006; Q8-WC-K0014; Q8-WC-K0856
- **section 1, line 36:** - WooCommerce's Marketplace offers "Discover Extensions Themes Business services"; BigCommerce's App Marketplace, "Apps & Integrations Themes Partner Services". Both use the term Themes (basis 1). Q8-WC-038; Q8-BC-045
- **section 1, line 38:** - Two list their own units beside partners'. Shopify's App Store has pages for built-in features, as B2B, "Included with Shopify Plus"; WooCommerce groups products "crafted by WooCommerce". Same role (basis 4; both stated). Q8-SH-K2696; Q8-WC-040
- **section 1, line 42:** - A WooCommerce extension declares the version it needs ("WC requires at least") and its compatibility with features through `declare_compatibility`. Q8-WC-032; Q8-WC-K1272
- **section 1, line 46:** - All five set a third party's unit apart under that party's terms. Shopify's Third Party Services are "solely between you and" their provider; WooCommerce's "Extensions may have their own requirements"; Salla's third-party services have "أحكامها المستقلة التي تتم بين التاجر وبين الطرف الثالث"; on Zid "الشريك هو المقدم للخدمة"; BigCommerce's Third-Party Products "are governed by their own terms of service". Same role (basis 4; all official pages). Q8-SH-K2169; Q8-WC-K0830; Q8-SA-035; Q8-ZD-K0366; Q8-BC-K0453
- **section 1, line 47:** - WooCommerce grows its core by merging packages into it: once a package is merged, "the feature plugin is disabled" (shipped). Not checked on Zid. Q8-WC-007
- **section 1, line 49:** - Apps are reviewed. Shopify's public apps "undergo Shopify's app review process"; WooCommerce's review runs from "Business review" to "Launch preparations"; on BigCommerce "The Marketplace team reviews all app submissions". Same role (basis 4). Q8-SH-029; Q8-WC-071; Q8-BC-K0316
- **section 1, line 50:** - Payment integrations are held apart. Shopify's payments extension needs review and approval; WooCommerce requires "a separate agreement" for a "Payments Solution"; BigCommerce has "paused all new externally built payment integrations"; Zid Payments assigns a provider's ID "upfront before starting the integration". Same role (basis 4; all stated). Q8-SH-095; Q8-WC-K0353; Q8-BC-058; Q8-ZD-K0079
- **section 1, line 52:** - Salla pays developers after "عادة 15 يومًا" (official page); WooCommerce pays a vendor "70% of the Product Net Revenue" (stated). Q8-SA-K2146; Q8-WC-K0461
- **section 1, line 61:** - WooCommerce's shipped code keeps "The payment extension list for each country", in which "The order is important as it will be used to determine the priority of the suggestions". Q8-WC-K0054; Q8-WC-K0055
- **section 1, line 66:** - In WooCommerce's shipped feature definitions, `is_experimental` puts a feature under "Experimental" and "Defaults to true"; `enabled_by_default` makes it "opt-out instead of opt-in"; `deprecated_since` forces its value. Q8-WC-012; Q8-WC-011; Q8-WC-013
- **section 1, line 67:** - One feature is "Hidden while incomplete so it can't ship merchant-toggleable". When, or by what steps, a feature moves between these states was not in what was read. Q8-WC-025; Q8-WC-N02
- **section 1, line 73:** - WooCommerce's betas are "Meant to be used by plugin authors and early adopters"; Shopify publishes an API release candidate with each stable version. Q8-WC-056; Q8-SH-068
- **section 2, line 80:** - Alternative not taken: separate mechanisms for features and for partners' units, as WooCommerce's features class and its Marketplace; one catalogue lets plan, place and stage gate every kind alike (rule 1). Q8-WC-K1310; Q8-WC-038
- **section 2, line 90:** - The merchant's own switch, as WooCommerce's features "can be enabled and disabled by admin users", is one of the rule's conditions, where it lets the merchant choose (rule 1). Q8-WC-K1310
- **section 2, line 96:** - **Release stage**: each offer is hidden (built, not switchable), preview (by invitation, on request or on test stores, marked as such, under preview terms), released (opt-in, or on by default with opt-out), or retired (held at one value, then removed). The stage is a condition of the rule, and moving an offer is a catalogue change, so code ships behind it (rule 2). Q8-WC-025; Q8-WC-011; Q8-WC-013; Q8-SH-111
- **section 2, line 105:** - Alternative not taken: extensions inside the core through its hooks, as WooCommerce's plugins, which must then declare compatibility with its changes. Through defined points the core and apps change apart (rule 2). Q8-WC-K0014; Q8-WC-K1272
- **section 2, line 107:** - It combines the points Shopify, Salla, BigCommerce and WooCommerce show, with Shopify's review flags. Q8-SA-K2253; Q8-BC-077; Q8-WC-K0856
- **section 2, line 108:** - The **Payment provider interface** opens only to providers Sharrwah has agreed with, after review, as four platforms hold payment integrations apart. Q8-WC-K0353; Q8-BC-058
- **section 2, line 111:** - It takes Salla's version in each call, Shopify's support period and delisting, and Shopify's release candidates and WooCommerce's betas for partners. Q8-SH-068; Q8-WC-056
- **section 2, line 113:** - **Partner**: a party registered under a signed **Partner agreement**, as app maker, theme maker or service provider. Sharrwah reviews each app, theme and partner service before listing it, and may suspend or remove it. Partner terms are decided now (rule 3). Q8-ZD-018; Q8-WC-071; Q8-ZD-K0364
- **section 2, line 118:** - **Place profile**: Sharrwah's set-up for one place: which offers open there, which providers fill each provider interface and in what order they are suggested, the contracting entity, terms that supplement Sharrwah's there, and defaults. A store holds one place, with the basis it was set on. Q8-WC-K0054; Q8-WC-K0055; Q8-BC-030
- **section 3, line 128:** - Plugs in: payment providers, through gateways or apps. Q8-WC-K0006; Q8-ZD-K0079
- **section 3, line 129:** - Plugs in: shipping rates and carriers. Q8-WC-K0856
- **section 3, line 134:** - Set per place: which offers open there, the suggested providers and their order, the contracting entity and place terms. Q8-SH-K0041; Q8-WC-K0054; Q8-BC-030
- **section 3, line 140:** - Set per partner: its share. Q8-WC-K0461
- **section 3, line 143:** - Set by the merchant: plan, add-ons, apps and the scopes it approves, its own switches where the rule allows, and the facts that set its place. Q8-ZD-K0372; Q8-WC-K1310
- **section 5, line 171:** - Who may plug in payment methods: keep the **Payment provider interface** closed to all but agreed providers; settled by a company decision and any licence it needs. Q8-BC-058; Q8-WC-K0353
- **section 6, line 180:** - WooPayments, which "is powered by Stripe", is not available in Yemen, a request to add it open, and nor is Stripe, both as of 2026-10-10. Q8-WC-K0008; YA-62 (Not available, a request to add it open @ WooPayments's service, as of 2026-10-10); YA-62 (Unavailable @ Stripe's service, as of 2026-10-10)
- **section 7, line 191:** - Whether Sharrwah bills partners' app charges as their agent, whether that needs a licence in each area, and the partners' share and payout period. Q8-BC-K0168; Q8-WC-K0461; YK-87 (Transfers, collections, prepaid cards, remittances, payment instruments and e-money @ the internationally recognized government's area, as of 2022-09-13)
- **section 7, line 193:** - Which providers Sharrwah works with behind each additional service, and on what agreement. Q8-WC-K0008; Q8-BC-K0129

## The cards

### Q8-WC-042

**Cited at:** section 1, line 9

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-042
- bears_on: 2
- identifier: Extensions
- statement: Grow your business with hundreds of free and paid extensions
- cite_ids: Q8-WC-C042
- from: held

**Citation Q8-WC-C042:** `https://woocommerce.com/product-category/woocommerce-extensions/` | Extensions | 2026-10-10 | kind: stated | quote check: found
- quote: Grow your business with hundreds of free and paid extensions
- title: WooCommerce extensions - WooCommerce
- in context: WooCommerce extensions - WooCommerce Skip to navigation Skip to content Develop on Woo Hire an expert Get support Sell Extensions Resources Enterprise ecommerce Extensions ⟪Grow your business with hundreds of free and paid extensions⟫ Discover Extensions Themes Business services Search filters 30-day money-back guarantee Support teams across the world Safe and secure online payments Sell WooCommerce WooCommerce pricing Payments No-code customization Marketing Checkout Shipping Mobile app Enterprise ecommerce Marketplace WooCommerce extensions WooCommerce themes New Essentials Collections Developed by Woo Build Woo for developers Developer resources Become a Woo agency Become …

### Q8-WC-K1310

**Cited at:** section 1, line 21; section 2, line 80; section 2, line 90; section 3, line 143

**Record** (`studies/proposals/records/Q8/woocommerce/copied.tsv`):
- concern_id: WC-C-088
- placement: decides
- structure: woocommerce-11.2.1:src/Internal/Features/FeaturesController.php
- identifier: FeaturesController
- statement: * Class to define the WooCommerce features that can be enabled and disabled by admin users, * provides also a mechanism for WooCommerce plugins to declare that they are compatible * (or incompatible) with a given feature.
- cite_ids: WC-S-5433

**Citation WC-S-5433:** `woocommerce-11.2.1:src/Internal/Features/FeaturesController.php` | lines 30-32 | 2026-10-09 | kind: shipped | quote check: found
- quote: * Class to define the WooCommerce features that can be enabled and disabled by admin users, * provides also a mechanism for WooCommerce plugins to declare that they are compatible * (or incompatible) with a given feature.
- in context: …ttic\WooCommerce\Internal\ProductGallery\ProductMediaGallery; use Automattic\WooCommerce\Internal\PushNotifications\PushNotifications; use Automattic\WooCommerce\Internal\StockNotifications\StockNotifications; use Automattic\WooCommerce\Proxies\LegacyProxy; use Automattic\WooCommerce\Utilities\ArrayUtil; use Automattic\WooCommerce\Utilities\PluginUtil; use Automattic\WooCommerce\Enums\FeaturePluginCompatibility; defined( 'ABSPATH' ) || exit; /** ⟪* Class to define the WooCommerce features that can be enabled and disabled by admin users, * provides also a mechanism for WooCommerce plugins to declare that they are compatible * (or incompatible) with a given feature.⟫ * * Note: the 'woocommerce_register_feature_definitions' hook allows registering new features * externally. This hook is deprecated, features should be registered from within get_feature_definitions. * However, in case you use it for testing purposes, keep in mind that the hook is fired from inside 'init'; * therefore, features that need to be queried, enabled, or disabled before 'init' (e.g. during WP CLI initialization) * can't be registered u…

### Q8-WC-K0006

**Cited at:** section 1, line 34; section 3, line 128

**The same record as Q1-WC-K0006,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: Payment gateways in WooCommerce are class based and can be added through traditional plugins.
- scope: 

### Q8-WC-K0014

**Cited at:** section 1, line 34; section 2, line 105

**Record** (`studies/proposals/records/Q8/woocommerce/copied.tsv`):
- concern_id: WC-C-001
- placement: boundary
- structure: woocommerce-11.2.1:includes/class-wc-payment-gateways.php
- identifier: woocommerce_payment_gateways
- statement: $load_gateways = apply_filters( 'woocommerce_payment_gateways', $load_gateways );
- cite_ids: WC-S-0435
- note: Entry of the list extension-points.

**Citation WC-S-0435:** `woocommerce-11.2.1:includes/class-wc-payment-gateways.php` | line 92 | 2026-10-09 | kind: shipped | quote check: found
- quote: $load_gateways = apply_filters( 'woocommerce_payment_gateways', $load_gateways );
- in context: …bidden. * * @since 2.1 */ public function __wakeup() { wc_doing_it_wrong( __FUNCTION__, __( 'Unserializing instances of this class is forbidden.', 'woocommerce' ), '2.1' ); } /** * Initialize payment gateways. */ public function __construct() { $this->init(); } /** * Load gateways and hook in functions. */ public function init() { $load_gateways = array( 'WC_Gateway_BACS', 'WC_Gateway_Cheque', 'WC_Gateway_COD', 'WC_Gateway_Paypal', ); // Filter. ⟪$load_gateways = apply_filters( 'woocommerce_payment_gateways', $load_gateways );⟫ // Preload option caches to minimize future queries for options that do not yet exist or are not set to autoload. wp_prime_option_caches( array( 'woocommerce_bacs_settings', 'woocommerce_bacs_accounts', 'woocommerce_cheque_settings', 'woocommerce_cod_settings', 'woocommerce_paypal_settings', ) ); // Get sort order option. $ordering = (array) get_option( 'woocommerce_gateway_order' ); $order_end = 999; // Load gateways in order. foreach ( $load_g…

### Q8-WC-K0856

**Cited at:** section 1, line 34; section 2, line 107; section 3, line 129

**Record** (`studies/proposals/records/Q8/woocommerce/copied.tsv`):
- concern_id: WC-C-061
- placement: boundary
- structure: https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/shipping/shipping-method-api.md
- identifier: Shipping method API
- statement: WooCommerce has a Shipping Method API which plugins can use to add their own rates.
- cite_ids: WC-S-0628

**Citation WC-S-0628:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/features/shipping/shipping-method-api.md` | Shipping method API | 2026-10-10 | kind: stated | quote check: found
- quote: WooCommerce has a Shipping Method API which plugins can use to add their own rates.
- title: Shipping method API
- the page opens: WooCommerce has a Shipping Method API which plugins can use to add their own rates. This article will take you through the steps to creating a new shipping method based on the core Flat Rate method that interacts with the Shipping API. Create a plugin First off, create a regular WordPress/WooCommerce plugin - see our Building Your First Extension guide to get started. You'll define your shipping method class in this plugin file and maintain it outside of WooCommerce. Checking for WooCommerce and…
- headings: Shipping method API
- in context: --- post_title: Shipping method API sidebar_label: Shipping method API sidebar_position: 1 --- # Shipping method API ⟪WooCommerce has a Shipping Method API which plugins can use to add their own rates.⟫ This article will take you through the steps to creating a new shipping method based on the core Flat Rate method that interacts with the Shipping API. ## Create a plugin First off, create a regular WordPress/WooCommerce plugin - see our [Building Your First Extension guide](/docs/extensions/getting-started-extensions/building-your-first-extension) to get started. You'll define your shipping method class in this plugin file and maintain it outsi…

### Q8-WC-038

**Cited at:** section 1, line 36; section 2, line 80

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-038
- bears_on: 2
- identifier: WooCommerce Marketplace
- statement: Discover Extensions Themes Business services
- cite_ids: Q8-WC-C038
- from: held

**Citation Q8-WC-C038:** `https://woocommerce.com/products/` | WooCommerce Marketplace | 2026-08-13 | kind: stated | quote check: found
- quote: Discover Extensions Themes Business services
- title: WooCommerce Extensions, Themes, Plugins, and More
- in context: WooCommerce Extensions, Themes, Plugins, and More Skip to navigation Skip to content Develop on Woo Hire an expert Get support Sell Extensions Resources Enterprise ecommerce WooCommerce Marketplace ⟪Discover Extensions Themes Business services⟫ Curated picks for your store See more Explore our curated selection of standout extensions to boost sales and streamline your store operations. Mastercard Merchant Cloud Free download Free download ShipStation Excellence verified Meets elevated standards for security, compatibility, maintenance, and customer satisfaction. Learn more Excellence verified Free download Free download Rated 3.8 out of 5 stars 3.8 (21) Klaviyo Free download Free downl…

### Q8-WC-040

**Cited at:** section 1, line 38

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-040
- bears_on: 2
- identifier: Built by WooCommerce
- statement: Trust in high-quality solutions crafted by WooCommerce for a seamless and powerful store experience.
- cite_ids: Q8-WC-C040
- from: held

**Citation Q8-WC-C040:** `https://woocommerce.com/products/` | Built by WooCommerce | 2026-08-13 | kind: stated | quote check: found
- quote: Trust in high-quality solutions crafted by WooCommerce for a seamless and powerful store experience.
- title: WooCommerce Extensions, Themes, Plugins, and More
- in context: …evated standards for security, compatibility, maintenance, and customer satisfaction. Learn more Excellence verified Price $199 annually $199 annually Rated 4.4 out of 5 stars 4.4 (7) Stachethemes Seat Planner Excellence verified Meets elevated standards for security, compatibility, maintenance, and customer satisfaction. Learn more Excellence verified Price $79 annually $79 annually Rated 4.8 out of 5 stars 4.8 (5) Built by WooCommerce See more ⟪Trust in high-quality solutions crafted by WooCommerce for a seamless and powerful store experience.⟫ AutomateWoo Excellence verified Meets elevated standards for security, compatibility, maintenance, and customer satisfaction. Learn more Excellence verified Price $159 annually $159 annually Rated 3.5 out of 5 stars 3.5 (28) Product Bundles Excellence verified Meets elevated standards for security, compatibility, maintenance, and customer satisfaction. Learn more Excellence verified Price $79 annually $79 annually Rated 4.7 out of 5 stars 4.7 (1…

### Q8-WC-032

**Cited at:** section 1, line 42

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-032
- bears_on: 3
- identifier: wc_enable_wc_plugin_headers
- statement: // WC requires at least - allows developers to define which version of WooCommerce the plugin requires to run.
- cite_ids: Q8-WC-C032
- from: held

**Citation Q8-WC-C032:** `woocommerce-11.2.1:includes/wc-core-functions.php` | line 2281 | 2026-10-09 | kind: shipped | quote check: found
- quote: // WC requires at least - allows developers to define which version of WooCommerce the plugin requires to run.
- in context: …m string $default Default value. * @return mixed */ function wc_get_var( &$var, $default = null ) { return isset( $var ) ? $var : $default; } /** * Read in WooCommerce headers when reading plugin headers. * * @since 3.2.0 * @param array $headers Headers. * @return array */ function wc_enable_wc_plugin_headers( $headers ) { if ( ! class_exists( 'WC_Plugin_Updates' ) ) { include_once __DIR__ . '/admin/plugin-updates/class-wc-plugin-updates.php'; } ⟪// WC requires at least - allows developers to define which version of WooCommerce the plugin requires to run.⟫ $headers[] = WC_Plugin_Updates::VERSION_REQUIRED_HEADER; // WC tested up to - allows developers to define which version of WooCommerce they have tested up to. $headers[] = WC_Plugin_Updates::VERSION_TESTED_HEADER; // Woo - This is used in WooCommerce extensions and is picked up by the helper. $headers[] = 'Woo'; return $headers; } add_filter( 'extra_theme_headers', 'wc_enable_wc_plugin_headers' ); add_filter( 'extra_plugin_headers', 'wc_enable_w…

### Q8-WC-K1272

**Cited at:** section 1, line 42; section 2, line 105

**Record** (`studies/proposals/records/Q8/woocommerce/copied.tsv`):
- concern_id: WC-C-086
- placement: boundary
- structure: woocommerce-11.2.1:src/Utilities/FeaturesUtil.php
- identifier: FeaturesUtil::declare_compatibility
- statement: public static function declare_compatibility( string $feature_id, string $plugin_file, bool $positive_compatibility = true ): bool {
- cite_ids: WC-S-0455
- note: Entry of the list extension-points.

**Citation WC-S-0455:** `woocommerce-11.2.1:src/Utilities/FeaturesUtil.php` | line 87 | 2026-10-09 | kind: shipped | quote check: found
- quote: public static function declare_compatibility( string $feature_id, string $plugin_file, bool $positive_compatibility = true ): bool {
- in context: …main plugin file passing __FILE__ or 'my-plugin/my-plugin.php' for the * $plugin_file argument. * * @param string $feature_id Unique feature id. * @param string $plugin_file The full plugin file path. * @param bool $positive_compatibility True if the plugin declares being compatible with the feature, false if it declares being incompatible. * @return bool True on success, false on error (feature doesn't exist or not inside the required hook). */ ⟪public static function declare_compatibility( string $feature_id, string $plugin_file, bool $positive_compatibility = true ): bool {⟫ return wc_get_container()->get( FeaturesController::class )->declare_compatibility( $feature_id, $plugin_file, $positive_compatibility ); } /** * Get the ids of the features that a certain plugin has declared compatibility for. * * This method can't be called before the 'woocommerce_init' hook is fired. * * @param string $plugin_name Plugin name, in the form 'directory/file.php'. * @return array An array having a 'compatible' and an 'incompatibl…

### Q8-WC-K0830

**Cited at:** section 1, line 46

**Record** (`studies/proposals/records/Q8/woocommerce/copied.tsv`):
- concern_id: WC-C-059
- placement: responsible
- structure: https://wordpress.com/tos/
- identifier: 8. Specific Service Terms: c. Woo (Extensions)
- statement: Extensions may have their own requirements (like requiring a connection to their servers in order to provide their services) and terms that apply.
- cite_ids: WC-S-0465

**Citation WC-S-0465:** `https://wordpress.com/tos/` | 8. Specific Service Terms: c. Woo (Extensions) | 2026-10-06 | kind: official page | quote check: found
- quote: Extensions may have their own requirements (like requiring a connection to their servers in order to provide their services) and terms that apply.
- title: WordPress.com
- in context: …m give you the power to sell your products and services in whatever way your business needs. Your use of certain Services offered via Woo, like those related to tax calculation, payment, and shipping, may require a Jetpack connection to function. If you enable those features, the Jetpack-specific terms also apply. Extensions. The software in the extensions available in the Woo Marketplace is licensed under the GNU General Public License ("GPL"). ⟪Extensions may have their own requirements (like requiring a connection to their servers in order to provide their services) and terms that apply.⟫ Compatibility, access, updates, and support. When you purchase Paid Services from WooCommerce.com, you'll receive access to any necessary downloads along with updates and support (as described in our Support Policy) for those Paid Services for a period of one year, starting on the date of your purchase. Once your year is up, you'll need to renew your subscription if you'd like continued access to updates or support, or if you need to download an…

### Q8-WC-007

**Cited at:** section 1, line 47

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-007
- bears_on: 3
- identifier: Packages::$base_packages
- statement: Once a package has been merged into WooCommerce Core it should be moved from the package list and placed in * this list. This will ensure that the feature plugin is disabled as well as provide the class to handle * initialization for the now-merged feature plugin.
- cite_ids: Q8-WC-C007
- from: held

**Citation Q8-WC-C007:** `woocommerce-11.2.1:src/Packages.php` | lines 39-41 | 2026-10-09 | kind: shipped | quote check: found
- quote: Once a package has been merged into WooCommerce Core it should be moved from the package list and placed in * this list. This will ensure that the feature plugin is disabled as well as provide the class to handle * initialization for the now-merged feature plugin.
- in context: …and their main package classes. Once a package has been merged into WooCommerce * directly it should be removed from here and added to the merged packages array. * * @var array Key is the package name/directory, value is the main package class which handles init. */ protected static $packages = array( 'email-editor' => '\\Automattic\\WooCommerce\\Internal\\EmailEditor\\Package', ); /** * Array of package names and their main package classes. * * ⟪Once a package has been merged into WooCommerce Core it should be moved from the package list and placed in * this list. This will ensure that the feature plugin is disabled as well as provide the class to handle * initialization for the now-merged feature plugin.⟫ * * Once a package has been merged into WooCommerce Core it should have its slug added here. This will ensure * that we deactivate the feature plugin automatically to prevent any problems caused by conflicts between * the two versions caused by them both being active. * * The packages included in this array cannot be deactivated and will always load with WooCommerce core. * * @var array Key is the package name/directory, value is the main packag…

### Q8-WC-071

**Cited at:** section 1, line 49; section 2, line 113

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-071
- bears_on: 3
- identifier: Review process
- statement: A review consists of the following steps: 1. **Business review**: to ensure your product is a good fit for the Marketplace, and that there is a business model to share revenue. 2. **Code review**: to ensure the submitted product's code is original, secure, and aligned with overall WordPress and WooCommerce quality standards. 3. **User experience (UX) review**: to ensure the product works as expected and its look and feel aligns with our UX guidelines. 4. **Launch preparations**: once a submission successfully passes these review phases, it will be formally approved and proceed to onboarding for launch.
- cite_ids: Q8-WC-C073;Q8-WC-C074;Q8-WC-C075;Q8-WC-C076;Q8-WC-C077
- from: live

**Citation Q8-WC-C073:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/woo-marketplace/submitting-your-product.mdx` | Review process | 2026-10-19 | kind: stated | quote check: found
- quote: A review consists of the following steps:
- title: Submitting your product to the Woo Marketplace
- the page opens: We look forward to reviewing your extension, theme, or integration for listing in the WooCommerce.com Marketplace. Before getting started, make sure you have applied for a Marketplace vendor account and your application has been approved. Pre-submission checklist Business review This includes an analysis of the product's business model and revenue share structure with Woo, as well as product rationale, competition, and developer/company history. - Mutually beneficial partnership: Products must s…
- headings: Submitting your product to the Woo Marketplace > Review process
- in context: … process. ![Replace zip file](./_media/replace-zip-file.png) :::tip If your product is at a stage other than *Changes required*, you will not be able to replace this file. Please comment within the submission to request a status change from the Marketplace team. ::: ## Review process Once the submitted product passes automated code tests, it moves to our review queue. Once it has been reviewed, the reviewer will share feedback (if any) with you. ⟪A review consists of the following steps:⟫ 1. **Business review**: to ensure your product is a good fit for the Marketplace, and that there is a business model to share revenue. 2. **Code review**: to ensure the submitted product's code is original, secure, and aligned with overall WordPress and WooCommerce quality standards. 3. **User experience (UX) review**: to ensure the product works as expected and its look and feel aligns with our UX guidelines. 4. **Launch preparations**: once a …

**Citation Q8-WC-C074:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/woo-marketplace/submitting-your-product.mdx` | Review process | 2026-10-19 | kind: stated | quote check: found
- quote: 1. **Business review**: to ensure your product is a good fit for the Marketplace, and that there is a business model to share revenue.
- title, opening and note boxes: as for this source's citation above
- headings: Submitting your product to the Woo Marketplace > Review process
- in context: …lace-zip-file.png) :::tip If your product is at a stage other than *Changes required*, you will not be able to replace this file. Please comment within the submission to request a status change from the Marketplace team. ::: ## Review process Once the submitted product passes automated code tests, it moves to our review queue. Once it has been reviewed, the reviewer will share feedback (if any) with you. A review consists of the following steps: ⟪1. **Business review**: to ensure your product is a good fit for the Marketplace, and that there is a business model to share revenue.⟫ 2. **Code review**: to ensure the submitted product's code is original, secure, and aligned with overall WordPress and WooCommerce quality standards. 3. **User experience (UX) review**: to ensure the product works as expected and its look and feel aligns with our UX guidelines. 4. **Launch preparations**: once a submission successfully passes these review phases, it will be formally approved and proceed to onboarding for launch. ## FAQs <details…

**Citation Q8-WC-C075:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/woo-marketplace/submitting-your-product.mdx` | Review process | 2026-10-19 | kind: stated | quote check: found
- quote: 2. **Code review**: to ensure the submitted product's code is original, secure, and aligned with overall WordPress and WooCommerce quality standards.
- title, opening and note boxes: as for this source's citation above
- headings: Submitting your product to the Woo Marketplace > Review process
- in context: …e comment within the submission to request a status change from the Marketplace team. ::: ## Review process Once the submitted product passes automated code tests, it moves to our review queue. Once it has been reviewed, the reviewer will share feedback (if any) with you. A review consists of the following steps: 1. **Business review**: to ensure your product is a good fit for the Marketplace, and that there is a business model to share revenue. ⟪2. **Code review**: to ensure the submitted product's code is original, secure, and aligned with overall WordPress and WooCommerce quality standards.⟫ 3. **User experience (UX) review**: to ensure the product works as expected and its look and feel aligns with our UX guidelines. 4. **Launch preparations**: once a submission successfully passes these review phases, it will be formally approved and proceed to onboarding for launch. ## FAQs <details> <summary>How long will it take for my product to be reviewed?</summary> Once the submission is in business review, you can expect a formal decision …

**Citation Q8-WC-C076:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/woo-marketplace/submitting-your-product.mdx` | Review process | 2026-10-19 | kind: stated | quote check: found
- quote: 3. **User experience (UX) review**: to ensure the product works as expected and its look and feel aligns with our UX guidelines.
- title, opening and note boxes: as for this source's citation above
- headings: Submitting your product to the Woo Marketplace > Review process
- in context: …d code tests, it moves to our review queue. Once it has been reviewed, the reviewer will share feedback (if any) with you. A review consists of the following steps: 1. **Business review**: to ensure your product is a good fit for the Marketplace, and that there is a business model to share revenue. 2. **Code review**: to ensure the submitted product's code is original, secure, and aligned with overall WordPress and WooCommerce quality standards. ⟪3. **User experience (UX) review**: to ensure the product works as expected and its look and feel aligns with our UX guidelines.⟫ 4. **Launch preparations**: once a submission successfully passes these review phases, it will be formally approved and proceed to onboarding for launch. ## FAQs <details> <summary>How long will it take for my product to be reviewed?</summary> Once the submission is in business review, you can expect a formal decision from a reviewer within 30 days. Throughout the review process, we may provide feedback and request changes before rejecting or ap…

**Citation Q8-WC-C077:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/woo-marketplace/submitting-your-product.mdx` | Review process | 2026-10-19 | kind: stated | quote check: found
- quote: 4. **Launch preparations**: once a submission successfully passes these review phases, it will be formally approved and proceed to onboarding for launch.
- title, opening and note boxes: as for this source's citation above
- headings: Submitting your product to the Woo Marketplace > Review process
- in context: …ew consists of the following steps: 1. **Business review**: to ensure your product is a good fit for the Marketplace, and that there is a business model to share revenue. 2. **Code review**: to ensure the submitted product's code is original, secure, and aligned with overall WordPress and WooCommerce quality standards. 3. **User experience (UX) review**: to ensure the product works as expected and its look and feel aligns with our UX guidelines. ⟪4. **Launch preparations**: once a submission successfully passes these review phases, it will be formally approved and proceed to onboarding for launch.⟫ ## FAQs <details> <summary>How long will it take for my product to be reviewed?</summary> Once the submission is in business review, you can expect a formal decision from a reviewer within 30 days. Throughout the review process, we may provide feedback and request changes before rejecting or approving a submission. </details> <details> <summary>Can I resubmit a previously rejected product?</summary> Yes. You are welcome to resubmit products, pro…

### Q8-WC-K0353

**Cited at:** section 1, line 50; section 2, line 108; section 5, line 171

**The same record as Q1-WC-K0353,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: 1.2.10. ensure the Product is not a solution for processing or enabling payment transactions (“Payments Solution”). In order to make a Payments Solution available to Users of the Marketplace(s), Partner must enter into a separate agreement with Automattic and/or WooCommerce, as applicable.
- scope: 

### Q8-WC-K0461

**Cited at:** section 1, line 52; section 3, line 140; section 7, line 191

**Record** (`studies/proposals/records/Q8/woocommerce/copied.tsv`):
- concern_id: WC-C-017
- placement: decides
- structure: https://woocommerce.com/woo-vendor-agreement/
- identifier: 2.2
- statement: 2.2. For Products listed on the Woo Marketplace, WooCommerce will pay Partner 70% of the Product Net Revenue that WooCommerce collects in connection with a User’s purchase of the Product from the Woo Marketplace on a monthly basis within thirty (30) days of the end of each calendar month.
- cite_ids: WC-S-0580

**Citation WC-S-0580:** `https://woocommerce.com/woo-vendor-agreement/` | 2.2 | 2023-06-02 | kind: stated | quote check: found
- quote: 2.2. For Products listed on the Woo Marketplace, WooCommerce will pay Partner 70% of the Product Net Revenue that WooCommerce collects in connection with a User’s purchase of the Product from the Woo Marketplace on a monthly basis within thirty (30) days of the end of each calendar month.
- title: Marketplace Vendor Agreement - WooCommerce
- in context: …om all Partner Products if at any time if Partner does not comply with the terms of this Agreement or does not respond to our attempts to resolve an issue. 2. Fees 2.1. For Products listed on the WP Marketplace, Automattic will pay Partner 70% of the Product Net Revenue that Automattic collects in connection with a User's subscription to the Product from WP Marketplace on a monthly basis within thirty (30) days of the end of each calendar month. ⟪2.2. For Products listed on the Woo Marketplace, WooCommerce will pay Partner 70% of the Product Net Revenue that WooCommerce collects in connection with a User's purchase of the Product from the Woo Marketplace on a monthly basis within thirty (30) days of the end of each calendar month.⟫ 2.3. Partner shall be responsible and liable for all amounts relating to Taxes. We will be responsible for facilitating any User requests or claims related to returns, cancellations, refunds, and/or fraud. We will not be liable and Partner shall have no right to claw back any such amounts relating to the amounts outlined in the preceding sentence. 3. Removal of the Product 3.1. While we do not take on an obligation to monitor the Product, we res…

### Q8-WC-K0054

**Cited at:** section 1, line 61; section 2, line 118; section 3, line 134

**The same record as Q1-WC-K0054,** whose card is in `Q1-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: * The payment extension list for each country.
- scope: 

### Q8-WC-K0055

**Cited at:** section 1, line 61; section 2, line 118

**Record** (`studies/proposals/records/Q8/woocommerce/copied.tsv`):
- concern_id: WC-C-004
- placement: decides
- structure: woocommerce-11.2.1:src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php
- identifier: PaymentsExtensionSuggestions::$country_extensions
- statement: * The order is important as it will be used to determine the priority of the suggestions.
- cite_ids: WC-S-0619

**Citation WC-S-0619:** `woocommerce-11.2.1:src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php` | line 127 | 2026-10-09 | kind: shipped | quote check: found
- quote: * The order is important as it will be used to determine the priority of the suggestions.
- in context: …base details to avoid computing them multiple times during a request. * * @var array|null */ private ?array $extensions_base_details_memo = null; /** * The memoized processed country extensions to avoid rebuilding the list multiple times during a request. * * Keyed by user, country code, and context. Cleared via clear_cache(). * * @var array */ private array $country_extensions_memo = array(); /** * The payment extension list for each country. * ⟪* The order is important as it will be used to determine the priority of the suggestions.⟫ * * Each entry is keyed by the two-letter country code and consists of a list of payment extensions. * Each payment extension can be identified by its ID (the shorthand version) or by an array with the following format: * array( * 'id' => 'woopayments', // This is required. * '_type' => 'provider', // Overrides the '_type' key. * // Special entry that instructs the system to append the given items to a list-type entry. * // If the original entry…

### Q8-WC-012

**Cited at:** section 1, line 66

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-012
- bears_on: 3
- identifier: FeaturesController::add_feature_definition: is_experimental
- statement: $is_experimental              Set to true to display this feature under the "Experimental" heading on * the Features screen. Features set to experimental are also omitted from * the features list in some cases. Defaults to true.
- cite_ids: Q8-WC-C012
- from: held

**Citation Q8-WC-C012:** `woocommerce-11.2.1:src/Internal/Features/FeaturesController.php` | lines 206-208 | 2026-10-09 | kind: shipped | quote check: found
- quote: $is_experimental              Set to true to display this feature under the "Experimental" heading on * the Features screen. Features set to experimental are also omitted from * the features list in some cases. Defaults to true.
- in context: …eature, used as an input label if the feature * setting is a checkbox. * @type bool $disabled True to disable the setting field for this feature on the Features screen, * so it can't be changed. * @type bool $disable_ui Set to true to hide the setting field for this feature on the * Features screen. Defaults to false. * @type bool $enabled_by_default Set to true to have this feature by opt-out instead of opt-in. * Defaults to false. * @type bool ⟪$is_experimental Set to true to display this feature under the "Experimental" heading on * the Features screen. Features set to experimental are also omitted from * the features list in some cases. Defaults to true.⟫ * @type bool $skip_compatibility_checks Set to true if the feature should not produce warnings about incompatible plugins. * Defaults to false. * @type string $learn_more_url The URL to the learn more page for the feature. * @type string $option_key The key name for the option that enables/disables the feature. * @type int $order The order that the feature will appear in the list on the Features screen. * Higher number = higher in the list. Defa…

### Q8-WC-011

**Cited at:** section 1, line 66; section 2, line 96

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-011
- bears_on: 3
- identifier: FeaturesController::add_feature_definition: enabled_by_default
- statement: $enabled_by_default           Set to true to have this feature by opt-out instead of opt-in.
- cite_ids: Q8-WC-C011
- from: held

**Citation Q8-WC-C011:** `woocommerce-11.2.1:src/Internal/Features/FeaturesController.php` | line 204 | 2026-10-09 | kind: shipped | quote check: found
- quote: $enabled_by_default           Set to true to have this feature by opt-out instead of opt-in.
- in context: …creen. See the Settings API * for the schema of these props. * @type string $description A brief description of the feature, used as an input label if the feature * setting is a checkbox. * @type bool $disabled True to disable the setting field for this feature on the Features screen, * so it can't be changed. * @type bool $disable_ui Set to true to hide the setting field for this feature on the * Features screen. Defaults to false. * @type bool ⟪$enabled_by_default Set to true to have this feature by opt-out instead of opt-in.⟫ * Defaults to false. * @type bool $is_experimental Set to true to display this feature under the "Experimental" heading on * the Features screen. Features set to experimental are also omitted from * the features list in some cases. Defaults to true. * @type bool $skip_compatibility_checks Set to true if the feature should not produce warnings about incompatible plugins. * Defaults to false. * @type string $learn_more_url The URL to the learn mor…

### Q8-WC-013

**Cited at:** section 1, line 66; section 2, line 96

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-013
- bears_on: 3
- identifier: FeaturesController::add_feature_definition: deprecated_since
- statement: $deprecated_since             The WooCommerce version since which this feature is deprecated. * When set, feature_is_enabled() will force feature value to the deprecated_value * instead of reading from the database.
- cite_ids: Q8-WC-C013
- from: held

**Citation Q8-WC-C013:** `woocommerce-11.2.1:src/Internal/Features/FeaturesController.php` | lines 217-219 | 2026-10-09 | kind: shipped | quote check: found
- quote: $deprecated_since             The WooCommerce version since which this feature is deprecated. * When set, feature_is_enabled() will force feature value to the deprecated_value * instead of reading from the database.
- in context: …ore page for the feature. * @type string $option_key The key name for the option that enables/disables the feature. * @type int $order The order that the feature will appear in the list on the Features screen. * Higher number = higher in the list. Defaults to 10. * @type array $setting The properties used by the Settings API to render the setting control on * the Features screen. See the Settings API for the schema of these props. * @type string ⟪$deprecated_since The WooCommerce version since which this feature is deprecated. * When set, feature_is_enabled() will force feature value to the deprecated_value * instead of reading from the database.⟫ * @type bool $deprecated_value The value to return for deprecated features when feature_is_enabled() * is called. Defaults to false. * } * * @return void */ public function add_feature_definition( $slug, $name, array $args = array() ) { $defaults = array( 'disable_ui' => false, 'enabled_by_default' => false, 'is_experimental' => true, 'default_plugin_compatibility' => FeaturePluginCompatibility::COMPATIBLE, 'skip_compatibility_checks' => false, …

### Q8-WC-025

**Cited at:** section 1, line 67; section 2, line 96

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-025
- bears_on: 3
- identifier: features: point_of_sale_staff
- statement: // Hidden while incomplete so it can't ship merchant-toggleable; flip to // false when it's ready for an experimental preview.
- marker: Experimental
- cite_ids: Q8-WC-C025
- from: held

**Citation Q8-WC-C025:** `woocommerce-11.2.1:src/Internal/Features/FeaturesController.php` | lines 597-598 | 2026-10-09 | kind: shipped | quote check: found
- quote: // Hidden while incomplete so it can't ship merchant-toggleable; flip to // false when it's ready for an experimental preview.
- in context: …=> false, 'enabled_by_default' => true, 'disable_ui' => true, 'skip_compatibility_checks' => true, 'default_plugin_compatibility' => FeaturePluginCompatibility::COMPATIBLE, 'deprecated_since' => '11.0.0', 'deprecated_value' => true, ), 'point_of_sale_staff' => array( 'name' => __( 'POS staff', 'woocommerce' ), 'description' => __( 'Experimental: POS staff management, roles, and order attribution.', 'woocommerce' ), 'enabled_by_default' => false, ⟪// Hidden while incomplete so it can't ship merchant-toggleable; flip to // false when it's ready for an experimental preview.⟫ 'disable_ui' => true, 'is_experimental' => true, 'skip_compatibility_checks' => true, 'default_plugin_compatibility' => FeaturePluginCompatibility::COMPATIBLE, ), 'fulfillments' => array( 'name' => __( 'Order Fulfillments', 'woocommerce' ), 'description' => __( 'Enable the Order Fulfillments feature to manage order fulfillment and shipping.', 'woocommerce' ), 'enabled_by_default' => false, 'disable_ui' => true, 'is_experimental' => false, 'defau…

### Q8-WC-056

**Cited at:** section 1, line 73; section 2, line 111

**Record** (`studies/proposals/records/Q8/woocommerce/statements.tsv`):
- stmt_id: Q8-WC-056
- bears_on: 3
- identifier: Beta
- statement: Meant to be used by plugin authors and early adopters to test the features and functionality in an upcoming version.
- marker: Beta
- cite_ids: Q8-WC-C056
- from: live

**Citation Q8-WC-C056:** `https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/contribution/releases/prereleases.md` | Beta | 2026-10-19 | kind: stated | quote check: found
- quote: Meant to be used by plugin authors and early adopters to test the features and functionality in an upcoming version.
- title: WooCommerce Pre-releases
- the page opens: WooCommerce pre-releases provide early access to upcoming features and improvements, allowing developers, testers, and the community to prepare for future releases. This document outlines the different types of pre-releases available, their timing, and how they fit into the overall release cycle. Release Name Estimated Timing ------------------- ----------------------------------------------------------------- nightly Every night -dev At feature freeze -beta.1 1 week after feature freeze -beta.2…
- headings: WooCommerce Pre-releases > Release cycle pre-releases > Beta
- in context: …ource of truth for any specific dates is [our release calendar](https://developer.woocommerce.com/release-calendar/). ### `-dev` release This is an auto-generated tag that is created at the same time as the feature freeze happens for the current cycle. For example, when the feature freeze for `10.1.0` happened, `10.1.0-dev` was tagged. This is an internal development tag, available only in the GitHub repository and not on WordPress.org. ### Beta ⟪Meant to be used by plugin authors and early adopters to test the features and functionality in an upcoming version.⟫ The first beta is usually released 1 week after the feature freeze. Betas are versioned incrementally, starting with `-beta.1`, then `-beta.2`, and so on. We aim to release at least 2 betas per cycle, but more are possible if any important bug fixes or functionality require additional testing or receive an important update before the final stable release. All beta versions are available both on GitHub and WordPress.org. For guidance on how to pa…

### Q8-WC-K0008

**Cited at:** section 6, line 180; section 7, line 193

**The same record as Q5-WC-K0008,** whose card is in `Q5-woocommerce.md`: its record and sources are checked there. Check only this proposal's points against it.
- statement: You may decide to use third-party services, like Stripe or PayPal to collect payment or EasyPost to manage shipping. Please note that WooPayments is powered by Stripe.
- scope: 
