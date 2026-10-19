# Q8, WooCommerce: account

## [1]

- The readme describes WooCommerce as "the open-source ecommerce platform for WordPress" and says "Our core platform is free, flexible, and amplified by a global community", under "License: GPLv3". Q8-WC-K0507, Q8-WC-001, Q8-WC-K0511, Q8-WC-K0513
- The Terms of Service define "Woo services" as "WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet, and other products or services available at WooCommerce.com", and say some Services are offered for a fee, "like certain WordPress.com plans or Woo themes or extensions (collectively, “Paid Services”)". Q8-WC-K0497, Q8-WC-K0736

## [2]

### WooCommerce and its packages

- The release loads "packages developed outside of core" from `/packages`. `$packages` holds `email-editor`. Q8-WC-003, Q8-WC-004
- `$base_packages` holds `woocommerce-admin` and `woocommerce-gutenberg-products-block`, which "cannot be deactivated and will always load with WooCommerce core". `$merged_packages` holds `woocommerce-brands` and `woocommerce-additional-variation-images`, which "can be deactivated via the 'woocommerce_merged_packages' filter". Q8-WC-005, Q8-WC-006, Q8-WC-008, Q8-WC-009

### Features

- Settings > Advanced has a "Features" section. `FeaturesController` defines "the WooCommerce features that can be enabled and disabled by admin users". Q8-WC-K1309, Q8-WC-K1310
- The features it defines carry names such as "Marketplace", "Variation gallery", "Point of Sale", "Customer review request (beta)", "Blueprint (beta)", "Block Email Editor (alpha)" and "WooCommerce MCP". Q8-WC-016, Q8-WC-020, Q8-WC-022, Q8-WC-026, Q8-WC-027, Q8-WC-028, Q8-WC-029
- The admin's build-time feature config lists `experimental-blocks`, `minified-js`, `settings-ui`, `store-alerts`, `rest-api-v4` and `order-detail-redesign`, each on or off. Q8-WC-030, Q8-WC-031

### Extensions, themes and business services

- The Woo Marketplace is organized as "Discover", "Extensions", "Themes" and "Business services". Q8-WC-038, Q8-WC-K0457, Q8-WC-K0458, Q8-WC-K1466
- The extensions listing reads "Grow your business with hundreds of free and paid extensions". Its Category filter lists "All Extensions", "Developed by Woo", "Official payments", "Shipping, delivery and fulfillment", "Conversion", "Customer service", "Merchandising", "Store content and customizations", "Store management" and "Marketing". Q8-WC-042, Q8-WC-043
- Each category has subcategories, such as "Processors & gateways", "Buy now pay later", "Subscriptions", "Bookings and appointments", "Sales channels" and "International and localization". Q8-WC-K0338, Q8-WC-K0340, Q8-WC-K1389, Q8-WC-K1393, Q8-WC-K1453, Q8-WC-K1438
- Business services are divided into "Insurance", "Business Formation", "Compliance", "Finance", "Law" and other subcategories. Q8-WC-K1467, Q8-WC-K1468, Q8-WC-K1470, Q8-WC-K1472, Q8-WC-K1473
- The Marketplace marks some products "Excellence verified": "Extensions that meet our highest bar for security, compatibility, and reliability". It groups others as "Built by WooCommerce": "high-quality solutions crafted by WooCommerce". Q8-WC-039, Q8-WC-040
- A vendor submits one of four product types: "Extension", "Theme", "SaaS" or "Business Service". Q8-WC-069
- A Marketplace purchase gives the buyer "a WooCommerce.com subscription". For one year, Paid Services come with "access to any necessary downloads along with updates and support". Q8-WC-K0735, Q8-WC-K0734

### Extension points in the software

- Payment gateways "are class based and can be added through traditional plugins" through `WC_Payment_Gateway` and the `woocommerce_payment_gateways` filter. Shipping methods are added through the "Shipping Method API" (`WC_Shipping_Method`). Integrations are added through `WC_Integration` and `woocommerce_integrations`. Q8-WC-K0006, Q8-WC-K0013, Q8-WC-K0014, Q8-WC-K0856, Q8-WC-K0857, Q8-WC-K1267, Q8-WC-K1268
- The block checkout is extended through `IntegrationInterface`, `ExtendSchema` and `woocommerce_register_additional_checkout_field`. "Your application can change the way the Store API works by extending certain endpoints." Q8-WC-K1277, Q8-WC-K1279, Q8-WC-K1280, Q8-WC-K1203
- Copied gaps: no statement was found of why Woo-made extensions, the extension framework or block extensibility are placed as they are. Q8-WC-G0068, Q8-WC-G0129, Q8-WC-G0131

## [3]

### What units depend on

- The readme header reads "Requires at least: 7.0", "Tested up to: 7.1" and "Requires PHP: 7.4". Q8-WC-002
- WooPayments requires a WordPress.com account and connection. "Your use of certain Services offered via Woo, like those related to tax calculation, payment, and shipping, may require a Jetpack connection to function." Q8-WC-K0360, Q8-WC-K0372, Q8-WC-K0728
- WooPayments "is powered by Stripe". Signing up "creates a Stripe Express account that is connected to the WooPayments service". Q8-WC-K0008, Q8-WC-K0711
- WooPay depends on WooPayments: "When you use WooPayments, WooPay may be available as a checkout option". Q8-WC-K0446
- "Extensions may have their own requirements (like requiring a connection to their servers in order to provide their services) and terms that apply." Q8-WC-K0830
- Extensions declare their dependence on WooCommerce in plugin headers. "WC requires at least" names the minimum version an extension needs, and "WC tested up to" the latest version it was tested with. Plugins with a "WC tested up to" header are listed as "WooCommerce aware". Q8-WC-032, Q8-WC-033, Q8-WC-035
- The "Woo" header "is used in WooCommerce extensions and is picked up by the helper". It is "A unique identifier for a plugin sold on WooCommerce.com", which Woo adds automatically. Q8-WC-034, Q8-WC-059
- Plugins declare whether they are compatible with a feature through `FeaturesUtil::declare_compatibility`. Q8-WC-K1272
- A false HPOS declaration "hides the warning WooCommerce would otherwise show them". Q8-WC-074

### How extensions and themes are added

- To list a product, a vendor must first be approved for a Marketplace vendor account. Products "must share revenue with Woo". Q8-WC-060, Q8-WC-061
- Under the Marketplace Vendor Agreement, WooCommerce pays the Partner "70% of the Product Net Revenue". Products "must be GPL compatible". Payments Solutions need "a separate agreement". Q8-WC-K0461, Q8-WC-K0826, Q8-WC-K0353
- Products must support "the two latest major releases" of WooCommerce and WordPress. "All new extension submissions must be HPOS-compatible." Tiered monthly SaaS pricing requires the "SaaS Billing API". Q8-WC-062, Q8-WC-067, Q8-WC-063
- Only submissions "compatible with the latest enhancements to the core WooCommerce platform" are accepted. Products that break widely-used Marketplace extensions "may be rejected or removed". Those extensions are WooCommerce Bookings, WooCommerce Subscriptions, Product Add-Ons, Product Bundles, Min/Max Quantities and Shipment Tracking. Q8-WC-066, Q8-WC-064, Q8-WC-065
- Themes: "we are prioritizing block themes". Freemium products need "two separate submissions". Q8-WC-068, Q8-WC-070
- Review has four steps: Business review, Code review, User experience (UX) review, then Launch preparations. Q8-WC-071
- The "Excellence Verified" badge rests on four factors: Secure, Compatible, Maintained and Merchant-approved. Products without it "keep their existing visibility and placement". "New and noteworthy" lists "Fresh additions and rising stars in our marketplace, carefully vetted for your success". Q8-WC-072, Q8-WC-073, Q8-WC-041
- Woo may "suspend or remove a Product from the Marketplace(s) and/or a User’s Website". Q8-WC-K0462
- Connecting a store to WooCommerce.com "enables you to install extensions automatically, receive product updates and support". Q8-WC-K0869

### How core grows: packages merged into core

- When a package is merged into WooCommerce Core, it moves to the merged list, "the feature plugin is disabled", and the standalone plugin "cannot be activated because its functionality is now included in WooCommerce core". Q8-WC-007, Q8-WC-010

### How features are introduced and retired

- `enabled_by_default` makes a feature "opt-out instead of opt-in". `is_experimental` puts it "under the "Experimental" heading". The default is `is_experimental` true. Q8-WC-011, Q8-WC-012, Q8-WC-K1311
- The "Experimental features" section warns: "These features are either experimental or incomplete, enable them at your own risk!" Q8-WC-014, Q8-WC-015
- `deprecated_since` forces a feature to a fixed value. "Marketplace" has `deprecated_since` 10.5.0, "Variation gallery" 11.1.0 and "Point of Sale" 11.0.0, each with `deprecated_value` true. Q8-WC-013, Q8-WC-018, Q8-WC-019, Q8-WC-021, Q8-WC-023
- "POS staff" is "Experimental" and "Hidden while incomplete". "WooCommerce MCP" has `is_experimental` true and `enabled_by_default` false. Q8-WC-024, Q8-WC-025, Q8-WC-029
- HPOS "is officially released under the stable flag and will be enabled by default for new installations". Q8-WC-K0559
- Not found: when, or by what steps, a feature moves between these states. Copied gap: why feature settings are placed as they are. Q8-WC-N02, Q8-WC-G0133

### Release stages

- WooCommerce releases "roughly every five weeks". Q8-WC-045
- Pre-releases are `nightly`, `-dev`, `-beta.1`, `-beta.2` and later betas, `-rc.1`, and `-rc.2` and later RCs, each with its own timing. Q8-WC-049, Q8-WC-050, Q8-WC-051, Q8-WC-052, Q8-WC-053, Q8-WC-054
- Nightlies are "neither announced publicly nor uploaded to WordPress.org". Betas are "Meant to be used by plugin authors and early adopters" and "are available both on GitHub and WordPress.org". RCs are "feature-complete and considered stable enough for final testing". Q8-WC-055, Q8-WC-056, Q8-WC-057, Q8-WC-058
- Beta 1 includes "Regression testing with Woo-maintained extensions". At final release, "We make the stable release version available to everyone". Patch releases are versioned `x.y.z`. Q8-WC-046, Q8-WC-047, Q8-WC-048

### By place

- Payment extension suggestions are kept as "The payment extension list for each country". "The order is important as it will be used to determine the priority of the suggestions." Q8-WC-K0054, Q8-WC-K0055, Q8-WC-K0061
- Admin suggestions can use a rule on "the base location - country". Q8-WC-037
- WooPayments is available to businesses "in one of our supported countries". "We prioritize new countries and currencies based on a number of factors". WooPay "is currently available for U.S. merchants only". Q8-WC-K0400, Q8-WC-K0403, Q8-WC-K0447
- The Marketplace extensions listing has a "Country" filter set to "All Countries". Its values were not in what was read. Q8-WC-044, Q8-WC-N03

### By plan

- Admin rules can test "when the site is on a Woo Express plan", and can target "a specific Woo Express plan". The plans and what each includes were not in what was read. Q8-WC-036, Q8-WC-N01
