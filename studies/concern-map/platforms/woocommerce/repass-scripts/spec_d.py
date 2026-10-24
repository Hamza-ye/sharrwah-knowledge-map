# Re-pass spec, part D: further statements from captured and newly read pages.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from newcite import R, RL, RS, Web, Old, S, G

EUVAT = "https://woocommerce.com/document/eu-vat-number/"
S("WC-C-118", "decides", Web(EUVAT, "Remove VAT for Businesses in Your Base Country: If activated, businesses with a valid number in your base country will be VAT exempt.",
  "Setup and configuration"), "Remove VAT for Businesses in Your Base Country", scope="EU VAT Number")
S("WC-C-118", "decides", Web(EUVAT, "Enable B2B Transactions: This will force users to check out with a VAT number; useful for sites that transact purely from B2B.",
  "Setup and configuration"), "Enable B2B Transactions", scope="EU VAT Number")
S("WC-C-118", "boundary", Web(EUVAT, "EU VAT Number also works with the Cart and Checkout blocks, where customers can enter and validate their VAT number directly during checkout.",
  "Manage VAT number"), "Manage VAT number", scope="EU VAT Number")
S("WC-C-118", "reason", Web(EUVAT, "VAT on digital goods must be calculated based on customer location, and store owners need to collect evidence of this via IP address and Billing Address.",
  "EU VAT digital goods handling"), "EU VAT digital goods handling", scope="B2C sales of digital goods")

S("WC-C-087", "where", Web("https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/block-development/extensible-blocks/cart-and-checkout-blocks/README.md",
  "To extend the front-end of the blocks, extensions must use JavaScript.", "Front-end extensibility"), "Front-end extensibility")

S("WC-C-045", "responsible", Web("https://en.support.wordpress.com/automattic-gdpr/data-processing-agreements/",
  'For this type of information, the site owner (usually a business) is acting as a "Data Controller"', "When a DPA is useful"),
  "When a DPA is useful", scope="a store on WordPress.com that collects and stores other people's names and addresses",
  note="The page's example is 'a site owner might have a store on WordPress.com that collects and stores other people's names and addresses'.")

S("WC-C-042", "decides", Web("https://woocommerce.com/document/woopayments/settings-guide/",
  "Enable payments via saved cards, if checked, allows customers to save their card info to their account on your site, which allows them to check out much faster if they make more purchases from you in the future.",
  "Transaction preferences"), "Enable payments via saved cards", note="The WooPayments settings are under Payments > Settings.")

S("WC-C-100", "boundary", Web("https://woocommerce.com/document/subscriptions/develop/action-reference/",
  "Description: Fired once when a subscription renewal payment should be processed.", "Payment and Renewal Actions"),
  "woocommerce_scheduled_subscription_payment", scope="WooCommerce Subscriptions",
  note="The description of the action 'woocommerce_scheduled_subscription_payment'.")
S("WC-C-101", "boundary", Web("https://woocommerce.com/document/bookings-rest-api-reference/",
  "WooCommerce Bookings is fully integrated with the WordPress REST API.", "Introduction"), "WooCommerce Bookings REST API v1", scope="WooCommerce Bookings")
