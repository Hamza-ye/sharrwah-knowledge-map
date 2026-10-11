# Re-pass spec, part E (follow-up of 11 October 2026): the docs of Woo-made products in the Marketplace categories
# (WC-C-103 to WC-C-112) and MailPoet's own documentation (WC-C-113).
# A product counts as Woo-made when its Marketplace page lists it in "Developed by Woo"; the second citation of each
# category statement is that product page, which shows the product's categories.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from newcite import Web, S, NEWPAGES

JL = "last updated: JSON-LD dateModified"
SM = "last updated: kb.mailpoet.com sitemap-1.xml lastmod (the page shows no date)"
def d(url, date, basis=JL):
    NEWPAGES[url] = (date, basis, "2026-10-11", "rendered")

DOC = "https://woocommerce.com/document/"
PROD = "https://woocommerce.com/products/"
KB = "https://kb.mailpoet.com/article/"
PO_DEV = DOC + "woocommerce-purchase-order-gateway/purchase-order-gateway-developer-reference/"
BUNDLES_REST = DOC + "bundles-rest-api-reference/"
PR_DEV = DOC + "points-and-rewards-developer-documentation/"
BISN = DOC + "back-in-stock-notifications/"
ADVN = DOC + "advanced-notifications/"
CFE = DOC + "checkout-field-editor/"
XERO = DOC + "xero/"
GFW = DOC + "google-for-woocommerce/get-started/product-feed-information-and-free-listings/"
for u, dt in [(PO_DEV, "2026-10-08"), (BUNDLES_REST, "2026-01-26"), (PR_DEV, "2025-02-27"), (BISN, "2025-02-19"),
              (ADVN, "2023-09-01"), (CFE, "2025-12-17"), (XERO, "2026-08-13"), (GFW, "2026-08-11")]:
    d(u, dt)
P_PO, P_BUNDLES, P_PR, P_BISN, P_ADVN, P_CFE, P_XERO, P_GFW, P_WAP = (PROD + s + "/" for s in (
    "woocommerce-gateway-purchase-order", "product-bundles", "woocommerce-points-and-rewards", "back-in-stock-notifications",
    "advanced-notifications", "woocommerce-checkout-field-editor", "xero", "google-listings-and-ads", "woo-agency-partners"))
for u, dt in [(P_PO, "2026-09-16"), (P_BUNDLES, "2026-10-07"), (P_PR, "2026-09-24"), (P_BISN, "2026-07-22"), (P_ADVN, "2026-10-07"),
              (P_CFE, "2026-10-09"), (P_XERO, "2026-09-30"), (P_GFW, "2026-10-11"), (P_WAP, "2025-01-14")]:
    d(u, dt)
MP_PLANS, MP_OPTIN, MP_CUST, MP_HOOKS, MP_HOST, MP_DATA = (KB + s for s in (
    "349-mailpoet-plans-and-limits-explained", "385-adding-an-opt-in-checkbox-to-the-woocommerce-checkout-page",
    "278-the-woocommerce-customers-list", "274-list-of-filters-and-actions", "154-why-you-shouldnt-send-with-your-host",
    "361-data-collected-and-stored-by-mailpoet"))
for u, dt in [(MP_PLANS, "2026-05-13"), (MP_OPTIN, "2025-11-21"), (MP_CUST, "2025-03-21"), (MP_HOOKS, "2026-05-13"),
              (MP_HOST, "2025-12-03"), (MP_DATA, "2026-10-07")]:
    d(u, dt, SM)

# product pages: the categories each product is listed in (quotes as captured)
CAT = {
    "po": Web(P_PO, "Categories B2B Developed by Woo Merchandising Order options WooCommerce extensions", "Categories"),
    "bundles": Web(P_BUNDLES, "Categories WooCommerce extensions Developed by Woo Conversion Promotions Upsells and cross-sells Merchandising Additional purchases Bundles Pricing Product options Marketing", "Categories"),
    "pr": Web(P_PR, "Categories Conversion Developed by Woo Gifts Marketing Merchandising Promotions Rewards and loyalty WooCommerce extensions", "Categories"),
    "bisn": Web(P_BISN, "Categories Conversion Developed by Woo Inventory and order management Recovering orders Shipping, delivery and fulfillment Store alerts WooCommerce extensions", "Categories"),
    "advn": Web(P_ADVN, "Categories WooCommerce extensions Developed by Woo Conversion Store alerts Customer service", "Categories"),
    "cfe": Web(P_CFE, "Categories WooCommerce extensions Developed by Woo Store content and customizations Cart and checkout features", "Categories"),
    "xero": Web(P_XERO, "Categories Accounting Developed by Woo Store management WooCommerce extensions", "Categories"),
    "gfw": Web(P_GFW, "Categories WooCommerce extensions Developed by Woo Conversion Promotions Marketing Advertising and promotions Sales channels", "Categories"),
    "wap": Web(P_WAP, "Marketplace / Business Services / Developer Services / Woo Agency Partners Woo Agency Partners by Woo", "breadcrumb and heading"),
}
def listed(product, *cats):
    names = [f'"{c}"' for c in cats + ("Developed by Woo",)]
    return f"{product} is listed in the categories {', '.join(names[:-1])} and {names[-1]} (second citation: the Categories list on its Marketplace page)."

# WC-C-103 B2B
S("WC-C-103", "decides", Web(PO_DEV, "If you only need to stop accepting purchase orders, disable the gateway in its settings instead.",
  "Remove the gateway entirely"), "Remove the gateway entirely", scope="WooCommerce Purchase Order Gateway",
  note=listed("WooCommerce Purchase Order Gateway", "B2B"), more=[CAT["po"]])
S("WC-C-103", "boundary", Web(PO_DEV, "The purchase order number is stored on the order in the _po_number meta key.",
  "Order data: The _po_number meta key"), "_po_number", scope="WooCommerce Purchase Order Gateway (version 1.5.12)",
  note=listed("WooCommerce Purchase Order Gateway", "B2B") + " The reference describes version 1.5.12.", more=[CAT["po"]])

# WC-C-104 Merchandising
S("WC-C-104", "boundary", Web(BUNDLES_REST, "Product Bundles extends the /products/ and /orders/ endpoint responses with 2 new properties: bundled_by and bundled_items.",
  "REST API Reference"), "bundled_by; bundled_items", scope="Product Bundles",
  note=listed("Product Bundles", "Merchandising", "Bundles"), more=[CAT["bundles"]])

# WC-C-105 Conversion
S("WC-C-105", "decides", Web(BISN, "If you have configured WooCommerce to hide out-of-stock products and variations in your catalog, customers will not be able to sign up for back-in-stock alerts.",
  "Overview (Important)"), "Out of stock visibility > Hide out of stock items from the catalog", scope="Back In Stock Notifications",
  note=listed("Back In Stock Notifications", "Conversion", "Recovering orders"), more=[CAT["bisn"]])
S("WC-C-105", "boundary", Web(BISN, "When a product is restocked, the plugin creates a queue with all pending notification e-mails and processes them in batches using Action Scheduler - a robust, battle-tested task processing system used by WooCommerce core.",
  "Overview"), "Action Scheduler", scope="Back In Stock Notifications",
  note=listed("Back In Stock Notifications", "Conversion", "Recovering orders"), more=[CAT["bisn"]])
S("WC-C-105", "boundary", Web(PR_DEV, "Use the wc_points_rewards_action_settings filter to add your settings to the Points & Rewards settings page in the Points Earned for Actions section.",
  "Integrating a plugin with Points & Rewards"), "wc_points_rewards_action_settings", scope="WooCommerce Points and Rewards",
  note=listed("WooCommerce Points and Rewards", "Conversion"), more=[CAT["pr"]])

# WC-C-106 Customer service
S("WC-C-106", "decides", Web(ADVN, "Triggers determine which products and orders trigger notifications to be sent.",
  "Notification triggers"), "Notification triggers", scope="Advanced Notifications",
  note=listed("Advanced Notifications", "Customer service"), more=[CAT["advn"]])
S("WC-C-106", "boundary", Web(ADVN, "Purchases - Sent when an order has been purchased, not when the original order is created (uses pending_to_processing, pending_to_completed, failed_to_processing, failed_to_completed).",
  "Enable notifications"), "pending_to_processing; pending_to_completed; failed_to_processing; failed_to_completed", scope="Advanced Notifications",
  note=listed("Advanced Notifications", "Customer service"), more=[CAT["advn"]])

# WC-C-107 Store content and customizations
S("WC-C-107", "decides", Web(CFE, "Fields that change dynamically based on the chosen country of a user (address 1, address 2, city, state, postcode) cannot have custom validation rules, e.g., required fields are determined by locale, not by your settings.",
  "Fields (core fields)"), "Core fields", scope="Checkout Field Editor",
  note=listed("Checkout Field Editor", "Store content and customizations", "Cart and checkout features"), more=[CAT["cfe"]])
S("WC-C-107", "boundary", Web(CFE, "This extension works with the legacy checkout only", "Note"), "legacy checkout", scope="Checkout Field Editor",
  note=listed("Checkout Field Editor", "Store content and customizations", "Cart and checkout features"), more=[CAT["cfe"]])
S("WC-C-107", "boundary", Web(CFE, "Name - Name of field, which is used as the meta key to save info. Must be unique.", "Columns"),
  "Columns: Name", scope="Checkout Field Editor",
  note=listed("Checkout Field Editor", "Store content and customizations", "Cart and checkout features"), more=[CAT["cfe"]])
S("WC-C-107", "reason", Web(CFE, "The block-based checkout will soon include native field customization, so this extension isn't needed there.", "Note"),
  "legacy checkout", scope="Checkout Field Editor",
  note=listed("Checkout Field Editor", "Store content and customizations", "Cart and checkout features") + " The reason given for the extension working with the legacy checkout only.",
  more=[CAT["cfe"]])

# WC-C-109 Store management
S("WC-C-109", "decides", Web(XERO, "This setting controls when WooCommerce creates or updates an invoice in Xero", "Miscellaneous Settings: Send Invoices"),
  "Send Invoices", scope="Xero", note=listed("Xero", "Store management", "Accounting"), more=[CAT["xero"]])
S("WC-C-109", "boundary", Web(XERO, "There are two main steps to connect your WooCommerce store to Xero: Create an OAuth 2.0 app in the Xero developer portal. Connect the app to WooCommerce.",
  "Setup and Configuration"), "Setup and Configuration (OAuth 2.0 app)", scope="Xero", note=listed("Xero", "Store management", "Accounting"), more=[CAT["xero"]])

# WC-C-110 Marketing
S("WC-C-110", "decides", Web(GFW, "Since these are required fields for any product to be approved in Google Merchant Center, Google for WooCommerce will not sync WooCommerce products that do not have these fields.",
  "General product information"), "General product information", scope="Google for WooCommerce",
  note=listed("Google for WooCommerce", "Marketing", "Advertising and promotions"), more=[CAT["gfw"]])
S("WC-C-110", "boundary", Web(GFW, "Google for WooCommerce automatically syncs your WooCommerce product data to Google Merchant Center; you can also add or edit products individually or in bulk.",
  "Product Feed Information"), "Product Feed Information (Google Merchant Center)", scope="Google for WooCommerce",
  note=listed("Google for WooCommerce", "Marketing", "Advertising and promotions"), more=[CAT["gfw"]])

# WC-C-112 Business services (Woo Agency Partners is the one business service listed with Woo as vendor)
S("WC-C-112", "decides", Web(P_WAP, "All agency partners pass our rigorous technical and design review, so you can trust your business is in safe hands.",
  "Why work with a Woo Agency Partner?"), "Why work with a Woo Agency Partner?", scope="Woo Agency Partners",
  note="Woo Agency Partners is listed in Business Services > Developer Services, as a service by Woo (second citation: the page's breadcrumb and heading).", more=[CAT["wap"]])
S("WC-C-112", "boundary", Web(P_WAP, "Once you've found an agency (or a few agencies!) you're interested in working with, click the \"Contact on partner website\" button on their profile to get in touch with them directly.",
  "How it works: Step 2"), "How it works: Step 2: Get in touch", scope="Woo Agency Partners",
  note="Woo Agency Partners is listed in Business Services > Developer Services, as a service by Woo (second citation: the page's breadcrumb and heading).", more=[CAT["wap"]])

# WC-C-113 MailPoet (MailPoet is named among the Woo services in the Terms, WC-S-0458)
S("WC-C-113", "where", Web(MP_DATA, "If you have created an account with MailPoet to send emails or to purchase a plan, we collect the following data on our servers in the United States of America:",
  "What data does our sending service collect?"), "What data does our sending service collect?",
  scope="MailPoet accounts created to send emails or to purchase a plan",
  note="The list that follows names email address, names, IP and billing address.")
S("WC-C-113", "decides", Web(MP_PLANS, "When you install the MailPoet plugin, you can use it for free up to 500 subscribers without creating an account with us or subscribing to any plans.",
  "MailPoet Plans and Limits Explained"), "MailPoet Plans and Limits Explained")
S("WC-C-113", "decides", Web(MP_OPTIN, "All customers will be automatically added to the WooCommerce Customers list by default, but their status as subscribers will depend on your settings in the MailPoet > Settings > WooCommerce tab.",
  "Adding an Opt-in Checkbox to the WooCommerce Checkout Page"), "MailPoet > Settings > WooCommerce")
S("WC-C-113", "boundary", Web(MP_CUST, "The WooCommerce Customers list is a list automatically created by MailPoet with all of your WooCommerce customers.",
  "The WooCommerce Customers list"), "WooCommerce Customers list")
S("WC-C-113", "boundary", Web(MP_HOOKS, "mailpoet_subscription_before_subscribe Action, which fires before a subscription is stored in the database.",
  "List of Filters and Actions"), "mailpoet_subscription_before_subscribe")
S("WC-C-113", "reason", Web(MP_HOST, "We highly encourage our users to send with MailPoet's Sending Service or a third party email service provider instead of sending with their own website because: MailPoet and third party senders specialize in delivering emails.",
  "Why You Shouldn't Send with Your Host"), "Why You Shouldn't Send with Your Host")
