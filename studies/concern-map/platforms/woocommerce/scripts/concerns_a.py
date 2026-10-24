# Concerns A: money, licences, entities, sanctions, data location, partners, currency and tax.
import re
from spec import C, S, N, I


def E(s):
    return "^" + re.escape(s) + "$"


ST, NAV, API, EXT = "^settings$", "^admin-navigation$", "^api-resources$", "^extension-points$"
WPT, MKT, LEG = "^other:woopayments-doc-topics$", "^other:marketplace-categories$", "^legal-agreements$"
PES, TOSL, PPF = "^other:payment-extension-suggestions$", "^other:tos-woo-services$", "^other:plugin-page-features$"
CORE_LEGAL = ["tos_woo_services", "tos_ecom_def", "tos_ecom_control"]
CORE_LEGAL_NOTE = ("The Terms name WooCommerce among Woo services and make the merchant solely responsible for their ecommerce "
                   "activities; the core plugin itself is GPL software with no warranty (WC-C-025).")

# ---------------- holding money ----------------
C("WC-C-001", "Buyer payments through payment gateways (no balance held in core)", "Payment gateways; Payments",
  "Split from offline methods (WC-C-002), PayPal Standard (WC-C-003), WooPayments balances (WC-C-007) and Marketplace revenue (WC-C-017), which are placed differently.",
  match=[(ST, E("Payments")), (ST, E("Payments > main")), (NAV, E("Payments")), (EXT, r"^WC_Payment_Gateway"), (EXT, r"^woocommerce_payment_gateways"),
         (EXT, r"^AbstractPaymentMethodType"), (API, E("wc/v3 > payment-gateways")), (API, E("wc/v4 > settings-payment-gateways")),
         (API, E("Payment gateways")), (EXT, r"^(Payment method integration|Filtering payment methods)")],
  software=S("outside the platform", ["dev_pg_form", "dev_pg_plugins"], "Gateways are plugins; form-based gateways send the buyer to the processor's own website. No source read describes a balance held by core."),
  decides=S("merchant", [I(ST, E("Payments")), "dev_pg_extend"], "The merchant installs gateway plugins and enables them on the Payments settings tab."),
  legal=S("partner", ["tos_third_party_pay", "tos_third_party_data", "tos_not_involved_ext"], "The payment provider the merchant chooses; its own terms apply. The extension developer may be a different party (WC-C-005)."),
  boundary=S("WC_Payment_Gateway class and the woocommerce_payment_gateways filter; Blocks payment method registration", [I(EXT, E("WC_Payment_Gateway")), I(EXT, r"^woocommerce_payment_gateways"), I(EXT, r"^AbstractPaymentMethodType")]),
  reason=N())

C("WC-C-002", "Offline payment methods (direct bank transfer, check, cash on delivery)", "Direct bank transfer; Check payments; Cash on delivery; offline",
  "Split from gateway payments (WC-C-001): no processor is involved and the money reaches the merchant outside the platform.",
  match=[("^other:core-payment-gateways$", r"^(Direct bank transfer|Check payments|Cash on delivery)$"), (ST, r"^Payments > (offline|cod|bacs|cheque)$"),
         (API, E("wc/v4 > offline-payment-methods"))],
  software=S("core", [I("^other:core-payment-gateways$", "Direct bank transfer"), "code_bacs_desc", "code_cod_desc", "code_cheque_desc", "dev_pg_offline"], "Bundled in core; per the gateway docs no online payment is made."),
  decides=S("merchant", [I(ST, E("Payments > offline")), "code_bacs_account_details"], "The merchant enables the method and, for bank transfer, enters the account details shown to buyers."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("order set to on-hold awaiting payment (\"Awaiting BACS payment.\"); the merchant confirms receipt", ["code_bacs_onhold"]),
  reason=N())

C("WC-C-003", "PayPal Standard (core gateway that redirects to PayPal)", "PayPal Standard",
  "Split from WC-C-001: shipped in core but hidden on new installs, and it hands the buyer to PayPal.",
  match=[("^other:core-payment-gateways$", E("PayPal Standard")), (API, r"^wc/v3 > paypal-(standard|webhooks|buttons)$")],
  software=S("core", [I("^other:core-payment-gateways$", "PayPal Standard"), "code_paypal_should_load"], "Bundled in core, but not loaded on new installs or on sites that have not set it up."),
  decides=S("merchant", ["code_paypal_should_load"], "Loaded only where the merchant enabled it or has PayPal Standard orders; the platform at build hides it otherwise."),
  legal=S("partner", ["code_paypal_desc", "tos_third_party_pay"], "PayPal takes the payment; the Terms name PayPal as a third-party service."),
  boundary=S("redirect to PayPal; REST wc/v3 paypal-standard, paypal-webhooks and paypal-buttons", [I(API, r"^wc/v3 > paypal-"), "code_paypal_desc"]),
  reason=N())

C("WC-C-004", "Payment provider suggestions per store country (Payments settings)", "Payments; Set up payments; payment-gateway-suggestions",
  "Split from the providers themselves (WC-C-005, WC-C-006): this is WooCommerce's own per-country list of what to offer the merchant.",
  match=[(PES, "."), ("^other:onboarding-tasks$", r"^(Set up payments|Set up additional payment options)$"), (API, r"^wc-admin > payment-gateway-suggestions")],
  software=S("core", ["code_pes_country_map", "code_pgs_fallback_doc"], "Count by script over the release's country map: 247 country codes; WooPayments is listed for 38, the same set as the WooPayments countries doc."),
  decides=S("operator, per market or plan", ["code_pes_country_map", "code_pes_order"], "WooCommerce sets which payment extensions are suggested for each store country and their order."),
  legal=N("No source read says who answers for the suggestions; each suggested extension carries its provider's own terms (WC-C-005)."),
  boundary=S("Settings > Payments page; remote suggestion specs with bundled defaults used when remote specs are missing", ["code_pgs_fallback", "code_pgs_fallback_doc"]),
  reason=N())

C("WC-C-005", "Third-party payment extensions (Marketplace Official payments)", "Official payments; Processors & gateways; Wallets & express checkouts; Buy now pay later; Crypto payments; B2B payments",
  "Split from WooPayments (WC-C-006), a Woo-made service, and from in-person payments (WC-C-014).",
  match=[(MKT, r"^Extensions > Official payments"), ("^other:marketplace-categories$", E("Extensions > Store management > Payment management"))],
  software=S("extension point", [I(MKT, E("Extensions > Official payments")), "dev_pg_extend"]),
  decides=S("merchant", ["tos_third_party_pay"]),
  legal=S("partner", ["tos_third_party_data", "tos_3p_not_vetted", "privpay_shared", "mkt_card_stripe", "mkt_card_paypal", "mkt_card_square", "doc_stripe_fees"], "The payment provider's own terms and privacy policy apply. The Marketplace lists Stripe's extension as by Stripe and PayPal Payments as by PayPal, while Square is listed by Woo."),
  boundary=S("Payment Gateway API; a payments solution sold on the Marketplace needs a separate agreement with Automattic or WooCommerce", ["dev_pg_extend", "va_payments_solution", "va_tpv", "doc_square", "wp_vs_stripe"]),
  reason=N())

C("WC-C-006", "WooPayments payment processing (Woo-made extension and service)", "WooPayments",
  "WooPayments is placed as an extension and a separate service, not as WooCommerce core. Split into processing (here), balance and payouts (WC-C-007), reserves (WC-C-008), verification (WC-C-009), country availability (WC-C-010), restricted businesses (WC-C-011), fees (WC-C-012), fraud and disputes (WC-C-013), in-person payments (WC-C-014) and its dependence on Stripe (WC-C-048).",
  match=[(PES, E("woopayments")), ("^other:onboarding-tasks$", r"WooPayments"), (TOSL, E("WooPayments")), (PPF, E("Choose how you want to get paid")),
         (WPT, r"^(Payment Methods|Payment Failures / Declines|Compatibility|Customization and Translation|Testing and Troubleshooting)$")],
  software=S("separate service or product line", ["wp_not_required", "wp_policies_wpcom", "code_payments_menu_woopay", "mkt_card_woopayments", "wp_lpm"], "Delivered as an extension that connects to the WooPayments server; core treats it as one gateway among many but gives it the Payments menu once onboarded."),
  decides=S("merchant", ["wp_not_required"], "The merchant chooses whether to install and enable it."),
  legal=S("separate entity of the platform", ["tos_woo_services", "tos_woo_inc", "tos_woo_ie", "tos_wp_third_parties", "wp_policies_tos"], "A Woo service contracted with WooCommerce, Inc. or WooCommerce Ireland Ltd.; Stripe is the payment partner (WC-C-048)."),
  boundary=S("WooPayments extension on the core gateway API; WordPress.com connection to the WooPayments server; a Stripe Express account per merchant", ["wp_policies_wpcom", "wp_partnership", "wp_connection_required", "wp_no_stripe_dash"]),
  reason=S("other: \"It integrates into your site’s admin dashboard so that you can manage your payments and orders from one place.\"", ["wp_one_place", "wp_by_woo"]))

C("WC-C-007", "WooPayments account balance and payouts", "Payouts; account balance",
  "Split from WC-C-008 (reserves are applied by Stripe) and WC-C-051 (payout currency).",
  match=[(WPT, r"^(Payouts|Managing Money and Refunds)$")],
  software=S("separate service or product line", ["wp_payout_balance", "wp_partnership"], "Payments add to the WooPayments account balance, with a Stripe Express account behind it, and are paid out to the merchant's bank account."),
  decides=S("operator, per market or plan", ["wp_payout_location", "wp_payout_currency_single"], "Payout timing and payout currencies depend on the business location."),
  legal=S("partner", ["wp_partnership", "wp_caa", "wp_payout_stripe_cards"], "Shown in part: Stripe sends payouts under its Connected Account Agreement. No source read names the entity that legally holds the balance or the licence it holds it under (WC-C-020)."),
  boundary=S("Stripe Express account and the merchant's bank account; Payments > Payouts in WP Admin", ["wp_partnership", "wp_payout_balance", "wp_payout_held", "wp_payout_suspended"]),
  reason=N())

C("WC-C-008", "WooPayments reserves (funds withheld for risk)", "reserve",
  "Split from WC-C-007: Stripe, not WooPayments, decides and applies reserves.",
  match=[(WPT, E("Our Policies"))],
  software=S("outside the platform", ["wp_reserves_applies"], "Applied and managed by Stripe."),
  decides=S("other: the payments partner (\"they make the final decision\")", ["wp_reserves_stripe", "wp_policies_reserves"]),
  legal=S("partner", ["wp_reserves_applies", "wp_reserves_contact"]),
  boundary=S("email from Stripe naming the reserve type; funds withheld from the balance", ["wp_reserves_email"]),
  reason=S("other: \"Reserves are meant to protect the payments processor (Stripe, in this case) against losses arising from future refunds and disputes.\"", ["wp_reserves_purpose"]))

C("WC-C-009", "WooPayments know-your-customer verification", "Know Your Customer; KYC",
  "", match=[(WPT, r"^(Account Management|Our Policies)$")],
  software=S("separate service or product line", ["wp_partnership", "wp_kyc_stripe"]),
  decides=S("outside rules", ["wp_policies_kyc", "wp_kyc_why", "wp_delete_retain"], "Account information is also retained for tax and compliance purposes."),
  legal=S("partner", ["wp_partnership", "wp_kyc_stripe"], "Merchant information is verified with Stripe; WooPayments works with Stripe to confirm identity."),
  boundary=S("WooPayments signup, which creates a Stripe Express account; later changes in the Stripe Express dashboard", ["wp_partnership"]),
  reason=S("other: \"Because the payments sector is heavily regulated\"", ["wp_policies_kyc"]))

C("WC-C-010", "WooPayments availability by country", "WooPayments in Your Country; supported countries",
  "Split from WC-C-004 (core's suggestion list) because availability is set by the WooPayments service.",
  match=[(WPT, E("Compatibility"))],
  software=S("separate service or product line", ["wp_countries_list", "wp_countries_intro"]),
  decides=S("operator, per market or plan", ["wp_countries_list", "wp_countries_registered", "wp_countries_other", "readme_wp_countries"], "Sources disagree: the WooPayments doc lists 38 countries; the 11.2.1 readme and plugin page name 10. Both recorded. The country is where the business is registered."),
  legal=S("partner", ["wp_countries_reason"], "Account types per country follow the partner's adherence to local law."),
  boundary=S("country chosen at signup (where the business is registered)", ["wp_countries_registered"]),
  reason=S("other: \"our partner (Stripe) strictly adheres to the laws and regulations of the country each account is based in\"", ["wp_countries_reason", "wp_countries_uae"]))

C("WC-C-011", "Restricted and prohibited businesses on WooPayments", "prohibited or restricted; restricted businesses or activities",
  "Split from the Store guidelines for e-commerce on WordPress.com (WC-C-022).",
  match=[(WPT, E("Our Policies")), (LEG, r"^(Restricted businesses and activities|Woo Guidelines for CBD and Other Hemp-Derived Products)$")],
  software=S("separate service or product line", ["wp_prohibited_enforce"]),
  decides=S("outside rules", ["wp_prohibited_reason", "restricted_stripe_list"], "Card networks, processors and their financial service providers; the linked restricted list is Stripe's."),
  legal=S("merchant", ["tos_wp_restricted", "wp_prohibited_enforce"], "The merchant agrees not to transact restricted activities; WooPayments may restrict or close the account."),
  boundary=S("account review, restriction or shutdown; CBD sellers must use Square or Viva Wallet", ["wp_prohibited_enforce", "wp_prohibited_cbd", "tos_wp_suspend", "wp_policies_restricted"]),
  reason=S("other: \"Due to restrictions put in place by card networks, our payment processors, and their financial service providers\"", ["wp_prohibited_reason"]))

C("WC-C-012", "WooPayments fees", "Fees; Fees and Debits",
  "", match=[(WPT, E("Fees and Debits"))],
  software=S("separate service or product line", ["wp_fees_deducted"]),
  decides=S("operator, per market or plan", ["wp_fees_factors"], "Fees differ by business country, customer country, currency and payment method."),
  legal=S("separate entity of the platform", ["tos_ecom_woopay_fees", "tos_ecom_negative"], "Charged under the Terms by the Automattic entity the merchant contracts with."),
  boundary=S("fees deducted from each payment; negative balances recovered by debiting the bank account", ["wp_fees_deducted", "wp_payout_negative"]),
  reason=N())

C("WC-C-013", "WooPayments fraud protection rules set by the merchant", "fraud protection; Fraud and Disputes",
  "Split from Stripe Radar screening, whose rules the WooPayments team manages (WC-C-115), and from disputes started by cardholders (WC-C-116).",
  match=[(WPT, E("Fraud and Disputes"))],
  software=S("separate service or product line", ["wp_fraud_rules"]),
  decides=S("merchant", ["wp_fraud_rules"], "The merchant sets the protection risk level and rules."),
  legal=S("merchant", ["tos_ecom_identity"], "The Terms make the merchant responsible for verifying customers and their eligibility to transact."),
  boundary=S("rules run when an order is placed; blocked orders are not charged and go to Pending payment", ["wp_fraud_blocked"]),
  reason=N())

C("WC-C-014", "WooPayments in-person payments (card readers, Tap to Pay)", "In-Person Payments",
  "Split from the POS mode of the mobile app (WC-C-089), which can use other methods too.",
  match=[(WPT, E("In-Person Payments"))],
  software=S("separate service or product line", ["wp_ipp_feature"]),
  decides=S("operator, per market or plan", ["wp_ipp_countries", "wp_ipp_currency"]),
  legal=S("partner", ["tos_terminal_stripe", "tos_wp_terminal"], "Terminals are made by third parties; Stripe Terminal terms apply."),
  boundary=S("Woo mobile app with a card reader or Tap to Pay", ["wp_ipp_feature"]),
  reason=N())

C("WC-C-015", "WooPay (saved checkout details across stores)", "WooPay",
  "", match=[(LEG, E("Terms of Service"))],
  software=S("separate service or product line", ["tos_woopay_service"]),
  decides=S("merchant", ["tos_woopay_default"], "Offered by default with WooPayments unless the merchant removes it."),
  legal=S("merchant", ["tos_woopay_party"], "Automattic is not a party to the merchant–customer transaction."),
  boundary=S("checkout option shown with WooPayments", ["tos_woopay_default"]),
  reason=N())

C("WC-C-016", "Merchant financing (Stripe Capital)", "Stripe Capital; Merchant financing",
  "", match=[(WPT, E("Stripe Capital")), (MKT, E("Extensions > Store management > Merchant financing"))],
  software=S("outside the platform", ["wp_capital_partner"]),
  decides=S("other: eligibility reviewed automatically (\"automatically reviewed for eligibility on a daily basis\")", ["wp_capital_eligibility"]),
  legal=S("partner", ["wp_capital_bank"], "Loans issued by Celtic Bank, a Utah-chartered industrial bank, through Stripe."),
  boundary=S("offer by email or dashboard; repayment withheld from transactions", ["wp_capital_repay"]),
  reason=N())

C("WC-C-017", "Woo Marketplace sales and vendor revenue share", "Woo Marketplace; Marketplace Vendor Agreement; Refund Policy",
  "Split from third-party extensions in use (WC-C-059): this is the sale on WooCommerce.com, where WooCommerce, Inc. collects revenue.",
  match=[(LEG, r"^(Marketplace Vendor Agreement|Refund Policy)$"), (MKT, r"^(Extensions|Themes)$")],
  software=S("separate service or product line", ["va_parties", "va_revenue"]),
  decides=S("other: \"WooCommerce will pay Partner 70% of the Product Net Revenue that WooCommerce collects\"", ["va_revenue"]),
  legal=S("separate entity of the platform", ["va_parties", "va_revenue", "va_taxes_refunds", "va_user_data"], "WooCommerce, Inc. contracts with vendors and collects purchase revenue; vendors bear taxes; WooCommerce handles refunds and fraud claims."),
  boundary=S("Marketplace Vendor Agreement; WooCommerce.com checkout and Refund Policy", ["va_parties", "legal_refund_policy", "va_remove", "dev_mkt_connects"], "WooCommerce reserves the right to remove a product from the Marketplace and from a user's website."),
  reason=N())

C("WC-C-018", "Cardholder data security for WooPayments (PCI DSS)", "PCI DSS; Level 1 service provider",
  "Split from the merchant's own PCI scope (WC-C-019).",
  match=[(WPT, E("Our Policies"))],
  software=S("separate service or product line", ["wp_pci_fields"]),
  decides=S("outside rules", ["wp_pci_level1", "tos_wp_pci"]),
  legal=S("separate entity of the platform", ["tos_wp_pci"], "Automattic entities acknowledge responsibility for cardholder data within their possession or control."),
  boundary=S("hosted payment fields from the partner's environment; saved-card tokens stored by the partner", ["wp_pci_fields", "wp_pci_tokens"]),
  reason=S("other: \"Because sensitive payment information is never handled by your site or stored on your server, WooPayments helps reduce your PCI compliance scope significantly.\"", ["wp_pci_scope"]))

C("WC-C-019", "PCI DSS compliance of the merchant's store", "PCI-DSS compliance and WooCommerce",
  "", match=[(LEG, E("Terms of Service")), (WPT, E("Our Policies"))],
  software=S("outside the platform", ["wp_pci_site", "dev_pg_pci"], "The merchant's own site and server."),
  decides=S("outside rules", ["doc_pci_applies", "tos_ecom_pci"]),
  legal=S("merchant", ["tos_ecom_pci", "wp_pci_site"]),
  boundary=S("hosting environment; direct gateways need server security", ["dev_pg_pci"]),
  reason=N())

C("WC-C-020", "Licence under which WooPayments funds are held and moved", "Connected Account Agreement",
  "Kept separate so the gap is visible: no source read names the licensed entity.", match=[(LEG, E("Connected Account Agreement"))],
  software=N(), decides=N(),
  legal=N("No WooCommerce or Automattic source read names the licence, licensed entity or regulator for WooPayments balances. The docs point to Stripe's Connected Account Agreement, accepted at signup, which is Stripe's document and was not read."),
  boundary=S("Stripe Connected Account Agreement accepted at WooPayments signup", ["wp_caa"]),
  reason=N())

C("WC-C-021", "Tax reporting tied to payments (Form 1099-K, tax invoices for fees)", "Taxes and Documents; Form 1099-K; Documents",
  "", match=[(WPT, E("Taxes and Documents"))],
  software=S("separate service or product line", ["wp_tax_1099", "wp_tax_docs"]),
  decides=S("outside rules", ["wp_tax_1099", "wp_tax_irs"]),
  legal=S("other: WooPayments (\"WooPayments is required to issue a Form 1099-K\")", ["wp_tax_1099"], "The issuing entity is not named on the page."),
  boundary=S("Payments > Documents menu; monthly invoices", ["wp_tax_docs"]),
  reason=S("other: \"an information filing required by the Internal Revenue Service (IRS)\"", ["wp_tax_irs"]))

C("WC-C-022", "Prohibited items for e-commerce on WordPress.com sites (Store guidelines)", "Store guidelines",
  "Split from WC-C-011: these guidelines come from the Terms for e-commerce services on WordPress.com sites, not from WooPayments.",
  match=[(LEG, E("Store guidelines"))],
  software=S("separate service or product line", ["legal_store_guidelines", "sg_scope"], "Applies to e-commerce services on WordPress.com sites, such as a WooCommerce store there."),
  decides=S("other: Automattic's Store guidelines (\"you may not sell (or facilitate the sale of) any of the following\")", ["sg_list"]),
  legal=S("merchant", ["tos_ecom_control"]),
  boundary=S("Terms of Service: Ecommerce Services, Prohibited Uses", ["tos_ecom_ofac"]),
  reason=N())

# ---------------- legal entities and terms ----------------
C("WC-C-023", "Contracting entity for Woo services", "Woo services; WooCommerce, Inc.; WooCommerce Ireland Ltd.",
  "", match=[(LEG, E("Terms of Service")), (TOSL, ".")],
  software=S("separate service or product line", ["tos_woo_services"], "Applies to Woo services: WooCommerce, WooPayments, WooCommerce Shipping, WooCommerce Tax, MailPoet and services at WooCommerce.com."),
  decides=S("operator, per market or plan", ["tos_woo_inc", "tos_woo_ie", "tos_designated"], "Set by where the customer resides (Designated Countries or not)."),
  legal=S("separate entity of the platform", ["tos_woo_inc", "tos_woo_ie", "tos_collectively"]),
  boundary=S("Terms of Service, section 1 Who's Who; business use only", ["tos_woo_services", "tos_business_use"]),
  reason=N())

C("WC-C-024", "Data controller for Woo services", "Controllers and Responsible Companies",
  "", match=[(LEG, r"^(Privacy Policy|Privacy Notice for California Users|Do not sell or share my personal information)$")],
  software=S("separate service or product line", ["priv_controllers"]),
  decides=S("operator, per market or plan", ["priv_controllers_world"]),
  legal=S("separate entity of the platform", ["priv_controllers", "priv_woo_inc_also", "priv_woo_ie_joint", "priv_woo_inc_addr"], "WooCommerce, Inc. or WooCommerce Ireland Ltd., with Automattic Inc. as controller or joint controller for some processing."),
  boundary=S("Privacy Policy controllers chart", ["priv_controllers"]),
  reason=N())

C("WC-C-025", "Core software licence and warranty", "GPLv3; open-source",
  "", match=[(LEG, E("GPLv3"))],
  software=S("core", ["readme_license", "readme_open_source", "tos_woo_open_source", "readme_automattic"]),
  decides=S("platform at build", ["readme_license"]),
  legal=S("other: GPL licence with no warranty (\"THERE IS NO WARRANTY FOR THE PROGRAM\")", ["license_no_warranty"]),
  boundary=S("GPLv3 licence", ["readme_license"]),
  reason=S("other: \"The freedom of open-source means you retain full ownership of your store’s content and data forever.\"", ["readme_ownership"]))

C("WC-C-026", "Governing law and courts", "Jurisdiction and Applicable Law",
  "", match=[(LEG, E("Terms of Service"))],
  software=S("separate service or product line", ["tos_scope"]),
  decides=S("platform at build", ["tos_law"]),
  legal=S("platform company", ["tos_law", "tos_venue"], "California law; state and federal courts in San Francisco County."),
  boundary=S("Terms of Service, section 15", ["tos_law"]),
  reason=N())

C("WC-C-027", "Merchant responsibility for the store's sales, receipts, refunds and consumer law", "Ecommerce Services; Your responsibilities",
  "", match=[(LEG, E("Terms of Service"))],
  software=S("outside the platform", ["tos_ecom_control"]),
  decides=S("merchant", ["tos_ecom_control"]),
  legal=S("merchant", ["tos_ecom_control", "tos_ecom_identity", "tos_ecom_disputes"]),
  boundary=S("Terms of Service: Ecommerce Services, Your responsibilities", ["tos_ecom_def"]),
  reason=S("other: \"You have control over your store, and with great power comes great responsibility.\"", ["tos_ecom_power"]))

# ---------------- sanctions and screening ----------------
C("WC-C-028", "US sanctions on access to Automattic and Woo services", "US Economic Sanctions; OFAC",
  "Split from WC-C-029 (the merchant's own transactions).",
  match=[(LEG, E("Terms of Service"))],
  software=S("separate service or product line", ["tos_sanctions_block"]),
  decides=S("outside rules", ["tos_sanctions_reason", "tos_sanctions_list", "tos_ecom_ofac"], "The Terms list Cuba, Crimea, Iran, North Korea, the Donetsk and Luhansk People's Republics and Syria, and the SDN list."),
  legal=S("platform company", ["tos_sanctions_customers", "tos_sanctions_block"], "Automattic restricts or blocks access; users represent they are not in sanctioned places or on restricted lists."),
  boundary=S("Terms of Service section 18 and Ecommerce Services prohibited uses", ["tos_sanctions_list", "tos_sanctions_sdn", "tos_ecom_ofac"]),
  reason=S("other: \"our ability to provide our Services to you is subject to compliance with US sanctions\"", ["tos_sanctions_reason"]))

C("WC-C-029", "Sanctions and export compliance of the merchant's own sales", "export, import, and sanctions laws",
  "", match=[(LEG, E("Terms of Service"))],
  software=N("Inference: no buyer screening was found in core; the Selling location(s) setting (WC-C-030) limits countries but no source describes it as a sanctions control."),
  decides=S("outside rules", ["tos_ecom_sanctions_merchant"]),
  legal=S("merchant", ["tos_ecom_sanctions_merchant"]),
  boundary=S("Terms of Service: Ecommerce Services, Your responsibilities", ["tos_ecom_sanctions_merchant"]),
  reason=N())

C("WC-C-030", "Selling and shipping locations", "Selling location(s); Shipping location(s)",
  "", match=[(ST, E("General"))],
  software=S("core", ["code_selling_locations"]),
  decides=S("merchant", ["code_selling_locations", "doc_general"]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("settings woocommerce_allowed_countries and woocommerce_ship_to_countries", ["code_allowed_countries", "code_ship_to_countries"]),
  reason=N())

C("WC-C-031", "Checkout rate limiting", "Rate limit Checkout",
  "", match=[("^other:features$", E("Rate limit Checkout"))],
  software=S("core", [I("^other:features$", E("Rate limit Checkout"))]),
  decides=S("merchant", ["code_feat_rate_limit"], "A Features setting."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("Checkout place order and Store API /checkout endpoint", ["code_feat_rate_limit"]),
  reason=N())

# ---------------- where data lives ----------------
C("WC-C-032", "Store data in the merchant's own WordPress database", "Own and control your store data – forever",
  "Split from order table layout (WC-C-033) and from data flows to Automattic or partners (WC-C-035 to WC-C-044).",
  match=[(PPF, E("Own and control your store data – forever"))],
  software=S("core", ["wp_pci_site_data", "dev_hpos_trad", "dev_data_options"]),
  decides=S("merchant", ["readme_ownership", "readme_unlike_hosted"]),
  legal=S("merchant", ["readme_data_belongs"], "\"your data belongs to you\"; no source read names the merchant as data controller in those words."),
  boundary=S("WordPress database: posts and postmeta or HPOS order tables, and the wp_options table", ["dev_hpos_trad", "dev_data_options"]),
  reason=S("other: \"The freedom of open-source means you retain full ownership of your store’s content and data forever.\"", ["readme_ownership"]))

C("WC-C-033", "Order storage tables (High-Performance Order Storage)", "High-Performance order storage; HPOS",
  "", match=[("^other:features$", r"^(High-Performance order storage|HPOS Full text search indexes|HPOS Data Caching)$")],
  software=S("core", [I("^other:features$", E("High-Performance order storage")), "dev_hpos_tables"]),
  decides=S("merchant", [I("^other:features$", E("High-Performance order storage")), "dev_hpos_default"], "A Features setting; on by default for new installations since 8.2."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("dedicated order tables reached through the CRUD data stores", ["dev_hpos_tables"]),
  reason=S("other: \"This comes with performance issues.\" (of storing orders as posts)", ["dev_hpos_trad"]))

C("WC-C-034", "Hosting of the store", "WooCommerce Server Recommendations",
  "Not in the platform's lists: comes from the question's architecture concern \"where data lives\" and from the WooCommerce Server Recommendations page (https://woocommerce.com/document/server-requirements/), which asks the merchant to check their hosting environment.", match=[],
  software=S("outside the platform", ["doc_server_req", "readme_unlike_hosted", "priv_vendors_hosting"], "Automattic lists the user's hosting provider among vendors \"if your site is not hosted by Automattic\"."),
  decides=S("merchant", ["doc_server_req"]),
  legal=N("No source read states who is legally responsible for hosting a self-hosted store. Inference: the merchant and their host."),
  boundary=S("server requirements: WordPress, PHP, MySQL or MariaDB, HTTPS", ["doc_server_req"]),
  reason=N())

C("WC-C-035", "Usage tracking sent to WooCommerce", "WooCommerce usage tracking; wc-telemetry",
  "", match=[(API, r"^(wc-telemetry|wc-telemetry > tracker)$"), (LEG, E("WooCommerce usage tracking")), (ST, E("Advanced > WooCommerce.com"))],
  software=S("core", ["code_tracker_url", "ut_sent"], "Core sends the data when tracking is enabled."),
  decides=S("merchant", ["ut_off_default"], "Off by default for the WordPress.org plugin."),
  legal=S("separate entity of the platform", ["priv_usage_tracker", "priv_controllers"], "Collected under the Automattic Privacy Policy by the Automattic company that contracts with the user."),
  boundary=S("HTTPS to https://tracking.woocommerce.com/v1/ and the Tracks pixel https://pixel.wp.com/t.gif", ["code_tracker_url", "code_tracks_pixel"]),
  reason=S("other: \"the collected data will help us improve WooCommerce and develop features to support your business growth\"", ["ut_reason"]))

C("WC-C-036", "Remote logging to WooCommerce", "Remote Logging",
  "", match=[("^other:features$", E("Remote Logging"))],
  software=S("core", [I("^other:features$", E("Remote Logging")), "code_remote_log"]),
  decides=S("merchant", ["code_feat_remote_logging"], "Requires usage tracking to be enabled."),
  legal=N(),
  boundary=S("HTTPS to https://public-api.wordpress.com/rest/v1.1/logstash", ["code_remote_log"]),
  reason=S("other: \"to help improve WooCommerce\"", ["code_feat_remote_logging"]))

C("WC-C-037", "Store logs", "Logs; Logging in WooCommerce",
  "", match=[(NAV, E("Status > Logs")), (EXT, r"^WC_Log_Handler")],
  software=S("core", [I(NAV, E("Status > Logs")), "dev_logging"]),
  decides=N("Inference: the merchant, who reads the logs and configures the log storage method the logging doc refers to."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("WC_Logger with pluggable log handlers", [I(EXT, r"^WC_Log_Handler"), "dev_logging"]),
  reason=N())

C("WC-C-038", "Store analytics and reports kept in the store", "Analytics; Reports; WooCommerce Analytics",
  "Split from the WooCommerce Analytics service (WC-C-039), which syncs data to Automattic.",
  match=[(NAV, r"^Analytics"), (NAV, E("WooCommerce > Reports")), (API, r"^wc-analytics > (reports|leaderboards|imports)"), (API, r"^wc/v3 > reports"),
         (API, E("Reports")), ("^other:features$", E("WooCommerce Analytics")), ("^access-scopes$", E("view_woocommerce_reports")),
         (API, r"^wc-analytics > (Reports/Controller|Orders|Products|ProductVariations|ProductCategories|Coupons|Taxes|Data|DataCountries|ProductAttributes|ProductAttributeTerms|ProductReviews|ProductsLowInStock|SettingOptions)$"),
         (API, r"^wc-analytics > (activity-panel/counts|customers|data/download-ips)"), (API, E("wc-analytics"))],
  software=S("core", ["code_analytics_stays", "doc_analytics"], "The feature description says all data stays within the store."),
  decides=S("merchant", [I("^other:features$", E("WooCommerce Analytics"))], "A Features setting, on by default."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("wc-analytics REST namespace", [I(API, E("wc-analytics"))]),
  reason=N())

C("WC-C-039", "WooCommerce Analytics service (data synced to Automattic)", "WooCommerce Analytics data syncing",
  "", match=[(LEG, E("WooCommerce Analytics data syncing"))],
  software=S("separate service or product line", ["wca_sync"]),
  decides=S("merchant", ["wca_sync"], "The merchant connects the store and authorizes collection."),
  legal=S("separate entity of the platform", ["wca_sync", "priv_controllers", "wca_no_share"]),
  boundary=S("Jetpack Sync", ["wca_jetpack"]),
  reason=N())

C("WC-C-040", "Data shared with payment providers", "Privacy considerations when using official payments extensions",
  "", match=[(LEG, E("Terms of Service")), (LEG, E("Privacy Policy"))],
  software=S("outside the platform", ["privpay_shared", "privpay_not_wccom"]),
  decides=S("merchant", ["privpay_shared"]),
  legal=S("partner", ["privpay_shared", "tos_third_party_data", "priv_third_party"]),
  boundary=S("the payment extension sends billing and payment data to the provider", ["privpay_shared"]),
  reason=N())

C("WC-C-041", "Data shared with shipping providers", "Privacy considerations when using official shipping extensions",
  "", match=[(LEG, E("Terms of Service"))],
  software=S("outside the platform", ["privship_shared"]),
  decides=S("merchant", ["privship_shared"]),
  legal=S("partner", ["privship_shared", "tos_third_party_data"]),
  boundary=S("the shipping extension sends rate, label and tracking data to the carrier", ["privship_shared"]),
  reason=N())

C("WC-C-042", "WooPayments data and saved-card tokens held by the payment partner", "payment token",
  "", match=[(LEG, E("Terms of Service")), (LEG, E("Privacy Policy"))],
  software=S("outside the platform", ["wp_pci_tokens", "wp_pci_fields"]),
  decides=N(),
  legal=S("partner", ["tos_wp_share", "priv_wp_stripe"]),
  boundary=S("the site's connection to WordPress.com; tokens stored by the partner", ["wp_pci_tokens"]),
  reason=N())

C("WC-C-043", "Transfer outside the EEA and UK of data processed by Automattic", "Transferring Information",
  "", match=[(LEG, E("Privacy Policy"))],
  software=S("separate service or product line", ["priv_transfer"]),
  decides=S("platform at build", ["priv_transfer"]),
  legal=S("separate entity of the platform", ["priv_transfer", "priv_scc"]),
  boundary=S("standard contractual arrangements", ["priv_scc"]),
  reason=S("other: \"Because Automattic’s Services are offered worldwide\"", ["priv_transfer_reason"]))

C("WC-C-044", "Automattic as processor of site visitors' data (data processing agreement)", "Data Processing Agreement",
  "", match=[(LEG, E("Request a data processing agreement"))],
  software=S("separate service or product line", ["tos_dpa", "legal_dpa_page"]),
  decides=S("merchant", ["legal_dpa_page"], "Available to WordPress.com site owners on request; not shown for self-hosted stores."),
  legal=S("separate entity of the platform", ["tos_dpa", "priv_visitors"]),
  boundary=S("Data Processing Agreement, an amendment to the Terms", ["legal_dpa_page"]),
  reason=S("other: \"for the GDPR requirements that apply to us as a data processor for your website\"", ["tos_dpa"]))

C("WC-C-045", "Personal data export, erasure and retention", "Accounts & Privacy; Personal data retention",
  "", match=[("^other:privacy-exporters-erasers$", "."), (ST, E("Accounts & Privacy"))],
  software=S("core", [I("^other:privacy-exporters-erasers$", "^add_exporter"), "code_retention"]),
  decides=S("merchant", ["doc_accounts_privacy", "code_retention"]),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("WordPress personal data exporters and erasers", [I("^other:privacy-exporters-erasers$", "^add_eraser")]),
  reason=N())

C("WC-C-046", "Customer geolocation (MaxMind and IP lookup services)", "MaxMind Geolocation; Default customer location",
  "", match=[("^other:core-integrations$", E("MaxMind Geolocation")), (ST, E("Integration"))],
  software=S("core", ["doc_maxmind", "code_default_location"]),
  decides=S("merchant", ["code_default_location", "doc_maxmind_key"], "The merchant picks the default customer location and adds a MaxMind licence key."),
  legal=S("partner", ["doc_maxmind", "doc_maxmind_key"], "MaxMind GeoLite2 data under the merchant's own MaxMind licence key."),
  boundary=S("MaxMind database downloaded to wp-content; external IP lookup services tried in shuffled order", ["code_default_location", "code_maxmind_download", "code_geo_ip_apis", "code_geo_geoip_apis", "code_geo_shuffle"]),
  reason=S("other: \"to display tax rates and shipping methods specific to their location\"", ["doc_maxmind_purpose"]))

C("WC-C-047", "Address autocomplete providers", "Address autocomplete; Preferred address autocomplete provider",
  "", match=[(EXT, r"^WC_Address_Provider")],
  software=S("extension point", [I(EXT, r"^WC_Address_Provider"), "dev_address"]),
  decides=S("merchant", ["code_address_provider"]),
  legal=N(),
  boundary=S("WC_Address_Provider class, registered for shortcode and block checkouts", ["dev_address"]),
  reason=N())

# ---------------- partners and what happens when one fails ----------------
C("WC-C-048", "WooPayments dependence on Stripe and processor substitution", "built in partnership with Stripe",
  "Split from WC-C-006 to record the partner dependency and what the sources say happens when it breaks.",
  match=[(WPT, E("Account Management")), (LEG, E("Connected Account Agreement"))],
  software=S("outside the platform", ["wp_partnership", "tos_third_party_pay"]),
  decides=S("other: Stripe updates its Connected Account Agreement; the Terms let WooPayments move to another processor", ["wp_caa", "tos_wp_alt_processor"]),
  legal=S("partner", ["wp_caa", "wp_existing_stripe", "wp_support_first"]),
  boundary=S("Stripe Connected Account Agreement; WordPress.com connection", ["wp_caa", "wp_connection_required", "wp_optout_ends", "wp_optout_balance", "wp_disconnect", "tos_ecom_force_refunds"],
             "If the merchant opts out of updated Stripe terms, WooPayments use ends at once though the remaining balance is still paid out; if the WordPress.com connection is cut, WooPayments cannot take payments until reconnected; Automattic may force refunds if a payment processor or regulator requires it."),
  reason=N())

C("WC-C-049", "WordPress.com / Jetpack connection for Woo services", "WordPress.com account; Jetpack connection",
  "", match=[(LEG, E("Terms of Service")), (WPT, E("Our Policies"))],
  software=S("separate service or product line", ["tos_woo_jetpack", "wp_connection_required", "doc_wctax_connect"]),
  decides=S("merchant", ["doc_wctax_connect"], "The merchant connects the site."),
  legal=S("separate entity of the platform", ["tos_jetpack_terms"], "Jetpack-specific terms also apply."),
  boundary=S("WordPress.com connection token", ["doc_wctax_connect", "wp_disconnect"]),
  reason=S("other: \"to ensure that requests from your site (e.g., payments, refunds, etc.) are securely and correctly attributed to your store\"", ["wp_wpcom_reason"]))

C("WC-C-050", "Woo-made extensions (Developed by Woo)", "Developed by Woo",
  "Split from third-party extensions (WC-C-059): the seller and supporter is a Woo entity.",
  match=[(MKT, E("Extensions > Developed by Woo"))],
  software=S("extension point", [I(MKT, E("Extensions > Developed by Woo")), "code_pes_made_in_woo"]),
  decides=S("merchant", ["tos_paid_services"]),
  legal=S("separate entity of the platform", ["tos_woo_services", "tos_paid_services"], "Sold as Woo Paid Services under the Terms."),
  boundary=S("WooCommerce.com subscription for downloads, updates and support", ["tos_ext_updates", "doc_wccom_subs"]),
  reason=N())

# ---------------- currency and tax ----------------
C("WC-C-051", "WooPayments payout currency and currency conversion", "Payout currencies; currency conversion fee",
  "", match=[(WPT, r"^(Payouts|Fees and Debits)$")],
  software=S("separate service or product line", ["wp_payout_currency", "wp_fx_fee"]),
  decides=S("operator, per market or plan", ["wp_payout_currency_single"]),
  legal=N(),
  boundary=S("bank accounts per payout currency; conversion to the default currency", ["wp_payout_currency", "wp_fee_currency"]),
  reason=N())

C("WC-C-052", "Store currency (one base currency per store)", "Currency; base currency",
  "Split from presentment in other currencies, which needs an extension (WC-C-053).",
  match=[(ST, E("General")), (API, E("wc/v3 > data-currencies"))],
  software=S("core", ["code_currency_desc", "doc_currency_one"]),
  decides=S("merchant", ["code_currency_desc", "doc_currency_record", "doc_currency_noconvert"], "Changing the base currency does not convert existing amounts."),
  legal=S("merchant", CORE_LEGAL, CORE_LEGAL_NOTE),
  boundary=S("setting woocommerce_currency; REST wc/v3 data/currencies", ["code_currency_id", I(API, E("wc/v3 > data-currencies"))]),
  reason=N())

C("WC-C-053", "Selling in more than one currency (multi-currency)", "multi-currency; International and localization",
  "Split from the store currency (WC-C-052): core allows one base currency; other currencies come from an extension such as WooPayments.",
  match=[(WPT, E("Currencies"))],
  software=S("extension point", ["doc_currency_ext", "wp_cur_presentment"]),
  decides=S("merchant", ["wp_mc_manual", "wp_cur_default"], "The merchant enables currencies and can set manual rates; by default the customer currency is the store currency."),
  legal=N(),
  boundary=S("WooPayments: exchange rates fetched from the WooPayments server unless set manually; optional geolocation to switch currency", ["wp_mc_rates", "wp_mc_manual", "wp_mc_geo"]),
  reason=N())

C("WC-C-054", "Core tax calculation with merchant-entered rates", "Tax; Tax options; Standard rates; Collect sales tax",
  "Split from automated tax services (WC-C-055, WC-C-056).",
  match=[(ST, r"^Tax"), (API, r"^wc/v3 > (taxes|tax-classes)$"), (API, E("wc/v4 > settings-tax")), (API, r"^Tax (rates|classes)$"),
         (NAV, E("Analytics > Taxes")), ("^other:onboarding-tasks$", E("Collect sales tax"))],
  software=S("core", ["code_calc_taxes", I(ST, E("Tax")), "wp_tax_none"], "WooPayments itself has no tax-charging function."),
  decides=S("merchant", [I(ST, E("Tax > Standard rates")), "doc_tax_scope"]),
  legal=S("merchant", ["tos_ecom_taxes", "doc_tax_not_pro"]),
  boundary=S("Tax settings tab; REST wc/v3 taxes and tax-classes; the store address as tax location", [I(API, E("wc/v3 > taxes")), I(API, E("wc/v3 > tax-classes")), "code_store_address"]),
  reason=N())

C("WC-C-055", "WooCommerce Tax (automated tax calculation service)", "WooCommerce Tax; Automated taxes",
  "", match=[(TOSL, E("WooCommerce Tax")), (PPF, E("Simplify sales tax"))],
  software=S("separate service or product line", ["doc_wctax_scope", "doc_wctax_connect"]),
  decides=S("operator, per market or plan", ["doc_wctax_countries"]),
  legal=S("merchant", ["doc_wctax_scope", "tos_tax_calc", "tos_tax_calc2", "doc_wctax_no_nexus", "doc_wctax_not_pro"], "The service does not file or remit tax; the Terms say calculations may be provided by Taxamo and cannot be guaranteed."),
  boundary=S("WordPress.com connection to the WooCommerce Tax service, which uses Automattic's servers and a calculation partner", ["doc_wctax_connect", "doc_wctax_conn_error", "jp_wctax_servers", "jp_taxjar", "tos_tax_calc"],
             "Sources differ on the partner: Jetpack's sync page says tax calculations are provided by TaxJar; the Terms give Taxamo as an example. Both recorded. On a broken connection the doc's remedy is to reconnect; no fallback calculation is described."),
  reason=S("other: \"designed to remove the work of building and updating custom tax rate tables\"", ["doc_wcst_purpose"]))

C("WC-C-056", "Third-party tax extensions (Sales tax and duties)", "Sales tax and duties",
  "", match=[(MKT, E("Extensions > Store management > Sales tax and duties"))],
  software=S("extension point", [I(MKT, E("Extensions > Store management > Sales tax and duties"))]),
  decides=S("merchant", ["readme_tax"]),
  legal=S("app developer", ["tos_3p_not_vetted", "tos_3p_risk"]),
  boundary=N(),
  reason=N())

C("WC-C-057", "Taxes on Woo's own fees", "Taxes; VAT/GST/CT on fees",
  "", match=[(LEG, E("Terms of Service"))],
  software=S("separate service or product line", ["tos_fees_taxes"]),
  decides=S("outside rules", ["tos_fees_taxes", "wp_tax_fees_vat"]),
  legal=S("merchant", ["tos_fees_taxes"]),
  boundary=S("tax invoices for WooPayments fees under Payments > Documents", ["wp_tax_docs"]),
  reason=N())

C("WC-C-058", "Customs duties and import taxes on shipments", "customs charges, import taxes or duties",
  "", match=[(MKT, E("Extensions > Store management > Sales tax and duties")), (LEG, E("Terms of Service"))],
  software=S("outside the platform", ["tos_ship_duties"]),
  decides=S("outside rules", ["tos_ship_customs"]),
  legal=S("merchant", ["tos_ship_customs", "tos_ship_duties"]),
  boundary=N(),
  reason=N())

C("WC-C-115", "Stripe Radar screening on WooPayments accounts", "Stripe Radar",
  "Split from merchant-set fraud rules (WC-C-013): most Radar rules are managed by the WooPayments team, not the merchant.",
  match=[(WPT, E("Fraud and Disputes"))],
  software=S("outside the platform", ["wp_radar"], "Stripe's machine-learning screening."),
  decides=S("other: the WooPayments team (\"managed by our team and cannot be modified by merchants\")", ["wp_radar_managed"]),
  legal=N(),
  boundary=N(),
  reason=S("other: \"protection against risky transactions\"", ["wp_radar"]))

C("WC-C-116", "Disputes (chargebacks) on WooPayments transactions", "Managing Disputes; dispute; chargeback",
  "Split from fraud screening (WC-C-013, WC-C-115): a dispute starts with the cardholder and is answered by the merchant.",
  match=[(WPT, E("Fraud and Disputes"))],
  software=S("separate service or product line", ["wp_disputes_def"]),
  decides=S("buyer", ["wp_disputes_def"], "A dispute occurs when a cardholder contests a payment; the bank can also start one."),
  legal=S("merchant", ["tos_ecom_disputes"]),
  boundary=S("disputes answered through WooPayments; a flat dispute fee", ["wp_disputes_def", "tos_ecom_woopay_fees"]),
  reason=S("other: \"not responding to disputes would be worse, because it can lead to fines and/or being prohibited from charging certain types of cards\"", ["wp_disputes_why"]))

C("WC-C-117", "Store data synced to Automattic for Jetpack-connected Woo services", "Jetpack Sync; What data does Jetpack sync",
  "Split from the merchant's own database (WC-C-032) and from the WooCommerce Analytics service (WC-C-039).",
  match=[(LEG, E("Terms of Service")), (LEG, E("WooCommerce Analytics data syncing")), (LEG, E("wooads-policy"))],
  software=S("separate service or product line", ["jp_sync_servers", "jp_sync_all"]),
  decides=S("merchant", ["jp_sync_servers"], "Sync starts when the merchant connects the site to WordPress.com."),
  legal=S("separate entity of the platform", ["pn_scope", "priv_visitors"], "Automattic processes visitors' data in connection with Jetpack, including WooCommerce Shipping & Tax."),
  boundary=S("Jetpack Sync to WordPress.com servers; order data synced except purchaser address, company, email and phone; a REST API proxy can read live order data", ["jp_orders_sync", "jp_rest_proxy", "jp_stripe_access"]),
  reason=N())
