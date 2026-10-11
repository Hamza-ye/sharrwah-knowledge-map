# Citations for the core and extension concerns (second set).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from webcite import web as W, rel as R

TOS = "https://wordpress.com/tos/"
TOSD, TOSB = "2026-10-06", "last updated: Terms of Service 'Last Updated: October 6, 2026'"
DOC = "https://woocommerce.com/document/"
GH = "https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/"
MP = "https://woocommerce.com/products/"

# ---------- Terms: extra clauses ----------
W("tos_ecom_power", TOS, "You have control over your store, and with great power comes great responsibility.", "8. j. Ecommerce Services: Your responsibilities", TOSD, TOSB)
W("tos_woopay_default", TOS, "When you use WooPayments, WooPay may be available as a checkout option on your checkout page unless you remove it from your checkout options through your administrative controls.", "8. j. More on WooPay Specifically", TOSD, TOSB)
W("tos_terminal_stripe", TOS, "(b) the Stripe Terminal Services Terms and Stripe Terminal Purchase Terms as applicable", "8. j. More on WooPayments Specifically (in-person payments)", TOSD, TOSB)
W("tos_jetpack_terms", TOS, "If you enable those features, the Jetpack-specific terms also apply.", "8. Specific Service Terms: c. Woo", TOSD, TOSB)
W("tos_3p_enable", TOS, "While using the Services, you may enable, use, or purchase services, products, software, embeds, or applications (like themes, extensions, plugins, blocks, or point-of-sale terminals) provided or manufactured by a third party or yourself (“Third-Party Services”).", "11. Third-Party Services", TOSD, TOSB)
W("tos_ai_output", TOS, "You’re responsible for your Input, the use of any Output, and for complying with any applicable laws, so you must review all Output before using or publishing it.", "8. k. Artificial Intelligence", TOSD, TOSB)

# ---------- WooPayments docs: extra ----------
W("wp_one_place", DOC + "woopayments/compatibility/is-woopayments-required-to-take-payments/", "It integrates into your site’s admin dashboard so that you can manage your payments and orders from one place.", "Is WooPayments required to take payments with WooCommerce?")
W("wp_reserves_applies", DOC + "woopayments/our-policies/reserves/", "Because Stripe, not WooPayments, applies and manages reserves, they are the best ones to contact about it.", "WooPayments: Reserves (NOTE)")
W("wp_reserves_email", DOC + "woopayments/our-policies/reserves/", "The email Stripe sends you will tell you which one applies to your account.", "What types of reserves are there?")
W("wp_wpcom_reason", DOC + "woopayments/our-policies/", "The WordPress.com account is used to ensure that requests from your site (e.g., payments, refunds, etc.) are securely and correctly attributed to your store.", "WordPress.com account")
W("wp_disconnect", DOC + "woopayments/our-policies/connection/", "WooPayments will be unable to take payments until", "Changing the WordPress.com account you’re connected to (NOTE)")
W("wp_pci_scope", DOC + "woopayments/our-policies/pci-compliance/", "Because sensitive payment information is never handled by your site or stored on your server, WooPayments helps reduce your PCI compliance scope significantly.", "What makes WooPayments PCI Compliant?")
W("wp_tax_irs", DOC + "woopayments/taxes/", "In the U.S., a Form 1099-K is an information filing required by the Internal Revenue Service (IRS).", "Form 1099-K for U.S. merchants")
W("wp_capital_repay", DOC + "woopayments/stripe-capital/overview/", "You’ll automatically repay the financing over time through a percentage of your transactions according to your repayment rate.", "Repayment")
W("wp_fraud_rules", DOC + "woopayments/fraud-and-disputes/fraud-protection/", "WooPayments offers configurable fraud protection rules for merchants.", "WooPayments: Fraud Protection")
W("wp_fraud_blocked", DOC + "woopayments/fraud-and-disputes/fraud-protection/", "Blocked: The customer’s payment method is not charged, and the order is set to the Pending Payment status.", "How fraud protection works")
W("wp_radar", DOC + "woopayments/fraud-and-disputes/does-woopayments-use-stripe-radar/", "Yes, WooPayments utilizes Stripe Radar. This provides merchants with protection against risky transactions via Stripe’s machine learning technology.", "Does WooPayments use Stripe Radar?")
W("wp_radar_managed", DOC + "woopayments/fraud-and-disputes/does-woopayments-use-stripe-radar/", "Most of the Radar rules for WooPayments accounts are managed by our team and cannot be modified by merchants.", "Does WooPayments use Stripe Radar?")
W("wp_disputes_def", DOC + "woopayments/fraud-and-disputes/managing-disputes/", "A dispute (also called a “chargeback”) occurs when a cardholder contests a payment made with their card.", "Managing Disputes with WooPayments")
W("wp_disputes_why", DOC + "woopayments/fraud-and-disputes/managing-disputes/", "But not responding to disputes would be worse, because it can lead to fines and/or being prohibited from charging certain types of cards.", "Managing Disputes with WooPayments")
W("wp_ipp_feature", DOC + "woopayments/in-person-payments/", "With WooPayments’ In-Person Payments feature, your customers can pay via tap, swipe, chip card, or mobile wallet payments, all using our mobile app and a simple card reader or a device that supports Tap to Pay on iPhone or Android.", "WooPayments: In-Person Payments")
W("wp_ipp_countries", DOC + "woopayments/in-person-payments/", "In-Person Payments is available to qualified merchants based in Australia, Canada, Finland, Ireland, Luxembourg, the Netherlands, New Zealand, Singapore, the United Kingdom, and the United States", "WooPayments: In-Person Payments")
W("wp_ipp_currency", DOC + "woopayments/in-person-payments/", "Card readers and Tap to Pay on iPhone/Android can only collect payments in the default currency for each country.", "Currencies")
W("wp_lpm", DOC + "woopayments/payment-methods/local-payment-methods/", "By default, WooPayments accepts payments via credit and debit cards.", "Local payment methods")
W("wp_vs_stripe", DOC + "woopayments/compatibility/woopayments-vs-stripe-plugin-comparison/", "The regular Stripe plugin is not so closely integrated with the WordPress dashboard.", "Bank account payouts inside the WordPress dashboard")
W("wp_existing_stripe", DOC + "woopayments/account-management/existing-stripe-account/", "No, it is not possible to use an existing Stripe account with WooPayments.", "Can I use my existing Stripe account with WooPayments?")

# ---------- core docs ----------
W("doc_currency_one", DOC + "shop-currency/", "WooCommerce only allows for one base currency per store.", "Shop currency")
W("doc_currency_ext", DOC + "shop-currency/", "If you’d like to display products in different currencies (or allow customers to pay in a currency that differs from your shop’s base currency), you will need to add a multi-currency extension/plugin.", "Shop currency")
W("doc_currency_record", DOC + "shop-currency/", "Each WooCommerce store can set one base currency. WooCommerce uses it to display product prices and record new orders.", "Setting a store’s base currency")
W("doc_currency_noconvert", DOC + "shop-currency/", "Changing your base currency changes which currency your store displays and charges in. It does not convert any amounts for you.", "Changing the base currency")
W("doc_tax_scope", DOC + "setting-up-taxes-in-woocommerce/", "This documentation covers how to set up tax rates in WooCommerce, as well as how the platform handles taxes/VAT/GST based on these settings — not when or what to charge.", "Setting up taxes in WooCommerce")
W("doc_tax_not_pro", DOC + "setting-up-taxes-in-woocommerce/", "We are not tax professionals; our advice only applies to how to use our software.", "Setting up taxes in WooCommerce")
W("doc_general", DOC + "configuring-woocommerce-settings/general/", "From your store’s general settings page, you can enter your business address, define the regions you will sell and ship orders to, enable tax calculations and coupons, and select the currency your shop will use for sales.", "General settings")
W("doc_accounts_privacy", DOC + "configuring-woocommerce-settings/accounts-and-privacy/", "Use these settings to enable or disable guest checkout, control customer account creation, decide how your store retains or removes personal data, and set your privacy policy notices.", "Accounts and Privacy Settings")
W("doc_pci_applies", DOC + "pci-dss-compliance-and-woocommerce/", "If you store, process, or transmit cardholder data as defined in the PCI SSC glossary, then PCI-DSS applies to you.", "Do I need to be PCI-DSS compliant?")
W("doc_roles", DOC + "roles-capabilities/", "WooCommerce adds two user roles—Customer and Shop Manager—and extends the existing Administrator role with store management capabilities.", "WooCommerce user roles")
W("doc_roles_assign", DOC + "roles-capabilities/", "To assign roles, go to Users > All Users in the WordPress admin, select a user, and choose a role from the Role dropdown.", "WooCommerce user roles")
W("doc_webhooks", DOC + "webhooks/", "Webhooks let your WooCommerce store send automatic event notifications to a URL of your choice.", "Webhooks")
W("doc_webhooks_why", DOC + "webhooks/", "Webhooks are useful for integrating your store with third-party services or other external APIs that support them.", "What are webhooks")
W("doc_rest", DOC + "woocommerce-rest-api/", "The WooCommerce REST API connects your store to external systems and services.", "WooCommerce REST API")
W("doc_rest_keys", DOC + "woocommerce-rest-api/", "Most integrations require you to generate API keys in WooCommerce and enter them in the external service to establish the connection.", "WooCommerce REST API")
W("doc_analytics", DOC + "woocommerce-analytics/", "The Analytics and Sales Reports include detailed report views, advanced filtering and segmenting tools, CSV downloads, and a customizable dashboard for monitoring key store metrics.", "Analytics and Sales Reports")
W("doc_attribution", DOC + "order-attribution-tracking/", "It allows you to attribute orders to traffic sources, providing an understanding of the effectiveness of various marketing efforts.", "Order Attribution Tracking")
W("doc_coming_soon", DOC + "configuring-woocommerce-settings/coming-soon-mode/", "Coming soon mode controls who can visit your site while you prepare it for launch.", "WooCommerce Coming soon mode")
W("doc_pos", DOC + "woo-mobile-app-point-of-sale-mode/", "POS mode turns a supported tablet or phone into a digital cash register", "Woo Mobile App: Point of Sale Mode")
W("doc_pos_country", DOC + "woo-mobile-app-point-of-sale-mode/", "Your store address must be in one of the supported countries.", "Requirements")
W("doc_pos_currency", DOC + "woo-mobile-app-point-of-sale-mode/", "You must be using that country’s native currency as the store currency.", "Requirements")
W("doc_pos_sync", DOC + "woo-mobile-app-point-of-sale-mode/", "All sales sync with your existing WooCommerce site.", "Woo Mobile App: Point of Sale Mode")
W("doc_fulfillment", DOC + "order-fulfillment/", "The WooCommerce Fulfillments system provides a comprehensive solution for managing the order fulfillment processes.", "Order Fulfillment")
W("doc_fulfillment_api", DOC + "order-fulfillment/", "This system includes both a user-friendly interface and a robust API for integration with your favorite shipping tools and providers.", "Order Fulfillment")
W("doc_order_status", DOC + "managing-orders/order-statuses/", "Every order in WooCommerce has a status that indicates its current state.", "Order Statuses")
W("doc_connect", DOC + "managing-woocommerce-com-subscriptions/connect-your-site-to-woocommerce-com/", "Connecting your WooCommerce store to your WooCommerce.com account enables you to install extensions automatically, receive product updates and support, and manage your subscriptions directly from your site’s WP Admin dashboard.", "Connect your site to WooCommerce.com")
W("doc_wccom_subs", DOC + "managing-woocommerce-com-subscriptions/what-are-woocommerce-com-subscriptions/", "When you purchase an extension or theme from the WooCommerce.com Marketplace, you receive a WooCommerce.com subscription.", "What are WooCommerce.com subscriptions?")
W("doc_stripe_fees", DOC + "stripe/", "NOTE: The fees for each transaction are determined exclusively by Stripe themselves.", "Stripe WooCommerce Extension")
W("doc_square", DOC + "woocommerce-square/", "The WooCommerce Square Extension bridges the gap between your WooCommerce store and Square.", "What You Can Do with WooCommerce Square")
W("doc_euvat", DOC + "eu-vat-number/", "Collect and validate EU VAT numbers at checkout.", "EU VAT Number")
W("doc_wcs_labels", DOC + "woocommerce-shipping/", "With WooCommerce Shipping, you can create ready-to-print labels for UPS®, USPS, DHL Express, and FedEx directly in WooCommerce and use discounted commercial rates.", "WooCommerce Shipping")
W("doc_wcs_us", DOC + "woocommerce-shipping/", "WooCommerce Shipping is currently available to stores based in the United States, including U.S. territories, that use U.S. dollars.", "WooCommerce Shipping")
W("doc_wcs_norates", DOC + "woocommerce-shipping/", "It does not provide live shipping rates at checkout.", "WooCommerce Shipping")
W("doc_install_items", DOC + "installing-uninstalling-woocommerce/", "New menu items, custom post types, and taxonomies for orders, products, and more", "Installing and Uninstalling WooCommerce")
W("doc_maxmind_key", DOC + "maxmind-geolocation-integration/", "Generating a MaxMind license key.", "MaxMind geolocation integration")

# ---------- Marketplace product cards (who makes the payment extensions) ----------
W("mkt_card_woopayments", MP, "WooPayments by Woo The only payment solution fully integrated with WooCommerce.", "Payment solutions", method="rendered")
W("mkt_card_stripe", MP, "Stripe by Stripe Maximize revenue with the new checkout from Stripe.", "Payment solutions", method="rendered")
W("mkt_card_paypal", MP, "PayPal Payments by PayPal The official, all-in-one checkout solution", "Payment solutions", method="rendered")
W("mkt_card_square", MP, "Square by Woo Woo's preferred POS partner, Square,", "Payment solutions", method="rendered")
W("mkt_country_filter", "https://woocommerce.com/product-category/woocommerce-extensions/", "Country All Countries", "Search filters", method="rendered")

# ---------- developer docs ----------
W("dev_store_api", GH + "apis/store-api/README.md", "The Store API provides public Rest API endpoints for the development of customer-facing cart, checkout, and product functionality.", "WooCommerce Store API")
W("dev_store_api_unauth", GH + "apis/store-api/README.md", "In contrast to the WooCommerce REST API, the Store API is unauthenticated and does not provide access to sensitive store data or other customer information.", "WooCommerce Store API")
W("dev_extend_store_api", GH + "apis/store-api/extending-store-api/README.md", "Your application can change the way the Store API works by extending certain endpoints.", "Extending the Store API")
W("dev_blocks_ext", GH + "block-development/extensible-blocks/cart-and-checkout-blocks/README.md", "This document is a high-level overview of the moving parts required to extend the Cart and Checkout blocks.", "Getting started with Cart and Checkout extensibility")
W("dev_mcp", GH + "features/mcp/README.md", "WooCommerce includes native support for the Model Context Protocol (MCP), enabling AI assistants and tools to interact directly with WooCommerce stores through a standardized protocol.", "Introduction")
W("dev_address", GH + "features/address-autocomplete.md", "The WooCommerce Address Autocomplete system allows third-party services to provide address suggestions as customers type in their billing and shipping addresses during checkout.", "Overview")
W("dev_logging", GH + "best-practices/data-management/logging.md", "You can view the entries created by the logger by going to **WooCommerce > Status > Logs**.", "Viewing logs")
W("dev_rest_auth", GH + "apis/rest-api/authentication.mdx", "Pre-generated keys can be used to authenticate use of the REST API endpoints.", "REST API keys")
W("dev_integration", GH + "extensions/settings-and-config/implementing-settings.md", "One of the easiest ways to create a settings page is by taking advantage of the [`WC_Integration` class]", "Creating custom settings for WooCommerce integrations")
W("dev_mkt_connects", GH + "woo-marketplace/getting-started.md", "The WooCommerce.com Marketplace connects trusted developers and merchants worldwide to create powerful and flexible online stores.", "Getting started")

# ---------- release code: settings ids and feature descriptions ----------
GEN = "includes/admin/settings/class-wc-settings-general.php"
FC = "src/Internal/Features/FeaturesController.php"
R("code_allowed_countries", GEN, "'id'       => 'woocommerce_allowed_countries',")
R("code_ship_to_countries", GEN, "'id'       => 'woocommerce_ship_to_countries',")
R("code_currency_id", GEN, "'id'       => 'woocommerce_currency',")
R("code_address_provider", GEN, "'name'    => __( 'Preferred address autocomplete provider', 'woocommerce' ),")
R("code_guest_checkout", "includes/admin/settings/class-wc-settings-accounts.php", "'desc'          => __( 'Enable guest checkout (recommended)', 'woocommerce' ),")
R("code_retention", "includes/admin/settings/class-wc-settings-accounts.php", "'title' => __( 'Personal data retention', 'woocommerce' ),")
R("code_bacs_account_details", "includes/gateways/bacs/class-wc-gateway-bacs.php", "<?php esc_html_e( 'Account details:', 'woocommerce' ); ?>")
R("code_webhook_signature", "includes/class-wc-webhook.php", "$http_args['headers']['X-WC-Webhook-Signature']   = $this->generate_signature( $http_args['body'] );")
R("code_feat_rate_limit", FC, "__( 'Enables rate limiting for Checkout place order and Store API /checkout endpoint. To further control this, refer to <a href=\"%s\" target=\"_blank\">rate limiting documentation</a>.', 'woocommerce' ),")
R("code_feat_marketplace", FC, "'New, faster way to find extensions and themes for your WooCommerce store',")
R("code_feat_withdrawal", FC, "'description'                  => __( 'Enable the public order withdrawal feature for customer requests.', 'woocommerce' ),")
R("code_feat_attribution", FC, "'Enable this feature to track and credit channels and campaigns that contribute to orders on your site',")
R("code_feat_remote_logging", FC, "__( 'Allow WooCommerce to send error logs and non-sensitive diagnostic data to help improve WooCommerce. This feature requires %1$susage tracking%2$s to be enabled.', 'woocommerce' ),")
R("code_feat_pos", FC, "'Enable Point of Sale functionality in the WooCommerce mobile apps.',")
R("code_feat_fulfillments", FC, "'Enable the Order Fulfillments feature to manage order fulfillment and shipping.',")
R("code_feat_push", FC, "'Enable push notifications for the WooCommerce mobile apps to receive order notifications and store updates.',")
R("code_feat_cogs", "src/Internal/CostOfGoodsSold/CostOfGoodsSoldController.php", "'description'                  => __( 'Allows entering cost of goods sold information for products.', 'woocommerce' ),")
R("code_store_api_ns", "src/StoreApi/RoutesController.php", "private static $api_namespace = 'wc/store';")
print("core citations registered")
