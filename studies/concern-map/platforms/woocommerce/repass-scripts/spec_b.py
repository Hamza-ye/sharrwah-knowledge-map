# Re-pass spec, part B: legal agreements, data and privacy, Woo services and the WordPress.com/Jetpack connection.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from newcite import R, RL, RS, Web, Old, S, G

TOS = "https://wordpress.com/tos/"
PRIV = "https://automattic.com/privacy/"
WP = "https://woocommerce.com/document/woopayments/"

# ---------- WC-C-011 restricted and prohibited businesses ----------
PROH = WP + "our-policies/prohibited-and-restricted-products/"
S("WC-C-011", "where", Web(PROH, "The full list of prohibited and restricted businesses can be found here.",
  "What businesses and products are prohibited or restricted on WooPayments?"), "prohibited and restricted businesses",
  note="In the served page, 'here' links to https://stripe.com/legal/restricted-businesses.")
S("WC-C-011", "responsible", Web(PROH, "By signing up to use WooPayments, you agree not to accept payments in connection with these restricted activities, practices, or products.",
  "What businesses and products are prohibited or restricted on WooPayments?"), "prohibited and restricted businesses")
S("WC-C-011", "decides", Web(WP + "our-policies/", "However, restricted accounts will still be able to access the Transactions and Disputes menus in order to manage new and existing disputes.",
  "Restricted accounts"), "Restricted accounts", scope="restricted accounts")

# ---------- WC-C-022 Store guidelines ----------
S("WC-C-022", "responsible", Web(TOS, "If you're using Ecommerce Services, you must observe all Store Guidelines and, if hosted on WordPress.com, the User Guidelines as well.",
  "8. j. Ecommerce Services: Prohibited Uses"), "Store Guidelines", scope="Ecommerce Services (Terms 8.j)",
  note="'Store Guidelines' links to en.support.wordpress.com/store-guidelines/ in the served page.")

# ---------- WC-C-024 data controller ----------
S("WC-C-024", "decides", Old("WC-S-0495"), "Controllers and Responsible Companies",
  note="States what decides which Automattic company is controller: the service and the individual's location.")

# ---------- WC-C-025 core licence ----------
S("WC-C-025", "decides", RS("license.txt", 192, 195, "All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program."), "GPLv3 section 2. Basic Permissions",
  note="From the licence text shipped with the release (license.txt).")

# ---------- WC-C-026 governing law ----------
S("WC-C-026", "decides", Web(TOS, "Nothing in this Agreement affects your rights as a consumer to rely on mandatory provisions in your country of residence.",
  "15. Jurisdiction and Applicable Law"), "15. Jurisdiction and Applicable Law")

# ---------- WC-C-027 merchant responsibility for sales ----------
S("WC-C-027", "decides", Old("WC-S-0848"), "8. j. Ecommerce Services: Your responsibilities")

# ---------- WC-C-029 sanctions in the merchant's own sales ----------
S("WC-C-029", "decides", Old("WC-S-0648"), "8. j. Ecommerce Services: Prohibited Uses", scope="Ecommerce Services (Terms 8.j)")

# ---------- WC-C-044 data processing agreement ----------
DPA = "https://en.support.wordpress.com/automattic-gdpr/data-processing-agreements/"
S("WC-C-044", "where", Web(DPA, 'Scroll down to the "Data processing addendum" section. Click the "Request a DPA" button.', "Get a data processing agreement"),
  "Data processing addendum", scope="WordPress.com account (my.wordpress.com/me/account, Preferences > Privacy)")
S("WC-C-044", "decides", Web(DPA, 'This "Data Processing Agreement" is a business to business agreement and is not relevant or needed for the typical free site owner or hobbyists.',
  "When a DPA is useful"), "When a DPA is useful")
S("WC-C-044", "boundary", Web(DPA, "This will automatically send a DPA to your account's email address which you can sign and return to privacypolicyupdates@automattic.com for processing.",
  "Get a data processing agreement"), "Request a DPA")

# ---------- WC-C-049 WordPress.com / Jetpack connection ----------
CONN = WP + "our-policies/connection/"
POL = WP + "our-policies/"
S("WC-C-049", "where", Web(CONN, "This connectivity is facilitated through the same process that the Jetpack plugin uses to connect to WordPress.com.",
  "Connecting to WordPress.com with WooPayments"), "Connecting to WordPress.com with WooPayments", scope="WooPayments")
S("WC-C-049", "where", Web(POL, "The Jetpack plugin is not required to use WooPayments. WooPayments does connect your site with WordPress.com as described above, but the Jetpack plugin itself is not necessary to make this connection.",
  "Jetpack"), "Jetpack", scope="WooPayments")
S("WC-C-049", "decides", Web(POL, "You will be asked to connect to a WordPress.com account during the signup process, or you can create a new one if you don't have one already.",
  "WordPress.com account"), "WordPress.com account", scope="WooPayments")
S("WC-C-049", "decides", Web(PRIV, "If you use our Ecommerce Services (including WooCommerce Shipping, WooCommerce Tax, and WooPayments), you'll have to create a WordPress.com account or connect an existing account and, for some Services, provide your site URL.",
  "Information We Collect"), "Ecommerce Services (Privacy Policy)")
S("WC-C-049", "boundary", Web(CONN, "NOTE: After you click the Disconnect button in the steps below, WooPayments will be unable to take payments until reconnected to WordPress.com.",
  "Changing the WordPress.com account you're connected to"), "Changing the WordPress.com account you're connected to", scope="WooPayments")

# ---------- WC-C-117 Jetpack sync ----------
S("WC-C-117", "decides", Old("WC-S-0954"), "What data does Jetpack sync?",
  note="Sync covers the data for all features, whether activated or not.")

# ---------- WC-C-039 WooCommerce Analytics service ----------
S("WC-C-039", "decides", Old("WC-S-0573"), "Information and data we collect from your store")

# ---------- WC-C-015 WooPay ----------
WOOPAY = "https://woocommerce.com/document/woopay-merchant-documentation/"
S("WC-C-015", "where", Web(WOOPAY, "Go to Payments > Settings in your site's admin dashboard. Scroll down to to the Express checkouts section. Check the box to enable WooPay.",
  "Enabling WooPay"), "Payments > Settings > Express checkouts")
S("WC-C-015", "decides", Web(WOOPAY, "WooPay is currently available for U.S. merchants only.", "Requirements"), "Requirements", scope="U.S. merchants")
S("WC-C-015", "decides", Web(WOOPAY, "Please note that WooPay and Link by Stripe are currently incompatible. You cannot have both express checkout methods enabled at the same time.",
  "Enabling WooPay"), "Enabling WooPay")

# ---------- WC-C-017 Marketplace sales and vendors ----------
MDEV = "https://woocommerce.com/document/marketplace-developers-customer-overview/"
S("WC-C-017", "boundary", Web(MDEV, "In general, no personal information about customers is shared with Marketplace Developers, although they can see aggregate data about the sales of their products.",
  "Information shared with Marketplace developers"), "Information shared with Marketplace developers")
S("WC-C-017", "where", Web(MDEV, "The developer/owner of a product is displayed below the product's name.", "How to determine who makes a product"),
  "How to determine who makes a product")

# ---------- WC-C-059 third-party extensions ----------
S("WC-C-059", "responsible", Web(MDEV, "These developers create, maintain, and support their own products.", "Overview of Marketplace developers"),
  "Overview of Marketplace developers", scope="third-party Marketplace developers")
S("WC-C-059", "responsible", Web("https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/extensions/best-practices-extensions/gdpr-compliance.md",
  "Developers must ensure that WooCommerce extensions are compliant with these regulations.", "GDPR compliance guidelines for WooCommerce extensions"),
  "GDPR compliance guidelines for WooCommerce extensions", scope="EU residents' personal data (GDPR)")

# ---------- WC-C-062 support ----------
SUPG = "https://woocommerce.com/document/support-guide/"
S("WC-C-062", "where", Web(SUPG, "If you have questions regarding the free, core WooCommerce plugin, please post a question and/or search for answers in the official support forum on WordPress.org.",
  "Public forums"), "Public forums", scope="the free, core WooCommerce plugin")
S("WC-C-062", "decides", Old("WC-S-0646"), "8. c. Woo: Compatibility, access, updates, and support",
  note="Support for Paid Services from WooCommerce.com lasts one year from purchase.")
S("WC-C-062", "boundary", Web(MDEV, "If you log a support request for a product made by a Marketplace developer, you will get a reply directly from them.",
  "Marketplace developer responsibilities"), "Marketplace developer responsibilities", scope="products made by Marketplace developers")

# ---------- WC-C-063 WooCommerce.com connection ----------
S("WC-C-063", "boundary", Web("https://raw.githubusercontent.com/woocommerce/woocommerce/trunk/docs/wc-cli/wc-cli-commands/wc-com.md",
  "Connect the store to WooCommerce.com with an application password.", "wc com connect"), "wc com connect")

# ---------- WC-C-096 AI features ----------
AIG = "https://automattic.com/ai-guidelines"
S("WC-C-096", "where", Web(AIG, "Currently, some of our AI features may be powered by Anthropic and OpenAI.", "AI at Automattic: Third Parties and Usage Policies"),
  "AI at Automattic: Third Parties and Usage Policies", note="The same section also lists Google's terms for features powered by Google.")
S("WC-C-096", "decides", Web(AIG, "We may power AI features with additional or different providers in the future, and different providers may have different practices regarding their use of input data.",
  "AI at Automattic: Third Parties and Usage Policies"), "AI at Automattic: Third Parties and Usage Policies")
S("WC-C-096", "boundary", Web(AIG, "Your input will be shared with third-party AI providers and might be used to train their models, so you should think carefully before inputting any confidential or sensitive information.",
  "Using AI: Things to Think About"), "Using AI: Things to Think About")

# ---------- WC-C-100 / WC-C-101 Woo-made extensions in Marketplace categories ----------
SUBS = "https://woocommerce.com/document/subscriptions/"
S("WC-C-100", "where", Web(SUBS, "Subscriptions General Settings: Explains all the settings you'll find in WooCommerce > Settings > Subscriptions.", "Getting started"),
  "WooCommerce > Settings > Subscriptions", scope="WooCommerce Subscriptions")
S("WC-C-100", "decides", Web(SUBS, "WooCommerce Subscriptions is a premium extension that allows you to sell products and services with recurring payments.",
  "Introduction to WooCommerce Subscriptions"), "Introduction to WooCommerce Subscriptions", scope="WooCommerce Subscriptions",
  note="Inference: as a premium extension, it runs only where the merchant has bought and installed it.")
BOOK = "https://woocommerce.com/document/introduction-to-woocommerce-bookings/"
S("WC-C-101", "decides", Web(BOOK, "Availability settings - You can define availability rules based on specific dates, time slots, or custom ranges.",
  "Creating Bookable Products"), "Availability settings", scope="WooCommerce Bookings")
S("WC-C-101", "boundary", Web(BOOK, "Working WP Cron (For clearing in-cart bookings from abandoned carts.)", "Requirements"), "Requirements: Cron",
  scope="WooCommerce Bookings")
