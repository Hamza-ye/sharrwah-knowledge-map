# Re-pass spec, part A: payments, WooPayments and the per-country payment suggestion lists.
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from newcite import R, RL, Web, Old, S, G

TOS = "https://wordpress.com/tos/"
GW_BACS = "includes/gateways/bacs/class-wc-gateway-bacs.php"
GW_CHEQUE = "includes/gateways/cheque/class-wc-gateway-cheque.php"
GW_COD = "includes/gateways/cod/class-wc-gateway-cod.php"
SUG = "src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php"
PGS_INIT = "src/Admin/Features/PaymentGatewaySuggestions/Init.php"
PGS_POLL = "src/Admin/Features/PaymentGatewaySuggestions/PaymentGatewaySuggestionsDataSourcePoller.php"
ADV = "includes/admin/settings/class-wc-settings-advanced.php"
WP = "https://woocommerce.com/document/woopayments/"

# ---------- WC-C-002 offline payment methods: who decides ----------
S("WC-C-002", "decides", R(GW_BACS, "'enabled'         => array(", "'default' => 'no',"), "woocommerce_bacs_settings: enabled",
  scope="Direct bank transfer (bacs)")
S("WC-C-002", "decides", R(GW_CHEQUE, "'enabled'      => array(", "'default' => 'no',"), "woocommerce_cheque_settings: enabled",
  scope="Check payments (cheque)")
S("WC-C-002", "decides", R(GW_COD, "'enabled'            => array(", "'default'     => 'no',"), "woocommerce_cod_settings: enabled",
  scope="Cash on delivery (cod)")
S("WC-C-002", "boundary", R(GW_BACS, "$process_payment_status = apply_filters( 'woocommerce_bacs_process_payment_order_status'"),
  "woocommerce_bacs_process_payment_order_status", scope="Direct bank transfer (bacs)")
S("WC-C-002", "boundary", R(GW_CHEQUE, "$process_payment_status = apply_filters( 'woocommerce_cheque_process_payment_order_status'"),
  "woocommerce_cheque_process_payment_order_status", scope="Check payments (cheque)")
S("WC-C-002", "boundary", R(GW_COD, "$process_payment_status = apply_filters( 'woocommerce_cod_process_payment_order_status'"),
  "woocommerce_cod_process_payment_order_status", scope="Cash on delivery (cod)")

# ---------- WC-C-003 PayPal Standard ----------
S("WC-C-003", "responsible", Old("WC-S-0475"), "Terms 8.j Third-Party Services",
  note="The same Terms paragraph names PayPal among third-party services used to collect payment (WC-S-0651).")
S("WC-C-003", "boundary", R("src/Gateways/PayPal/Request.php", "private const WPCOM_PROXY_REST_BASE"),
  "WPCOM_PROXY_REST_BASE", note="PayPal Standard's order and payment requests go through this WordPress.com proxy base (src/Gateways/PayPal/Request.php).")
S("WC-C-003", "decides", R("includes/gateways/paypal/class-wc-gateway-paypal.php", "// Set default `_should_load` to 'yes' on existing stores", "$should_load = 'yes' === $this->enabled"),
  "_should_load")

# ---------- WC-C-004 payment provider suggestions per country ----------
S("WC-C-004", "decides", R(ADV, "'title'         => __( 'Show Suggestions', 'woocommerce' ),", "'default'       => 'yes',"),
  "woocommerce_show_marketplace_suggestions", note="Settings > Advanced > WooCommerce.com, Marketplace suggestions.")
S("WC-C-004", "decides", R(PGS_INIT, "if ( 'no' === get_option( 'woocommerce_show_marketplace_suggestions', 'yes' ) ) {", "return apply_filters( 'woocommerce_admin_payment_gateway_suggestion_specs', DefaultPaymentGateways::get_all() );"),
  "woocommerce_show_marketplace_suggestions", note="The onboarding payments task's suggestions (PaymentGatewaySuggestions).")
S("WC-C-004", "boundary", R(PGS_POLL, "WC_Helper::get_woocommerce_com_base_url() . 'wp-json/wccom/payment-gateway-suggestions/2.0/suggestions.json',"),
  "wccom/payment-gateway-suggestions/2.0/suggestions.json", note="The data source the onboarding suggestions are fetched from; a country query parameter is added in the lines that follow.")
S("WC-C-004", "boundary", R(PGS_INIT, "// Fetch specs if they don't yet exist.", "return apply_filters( 'woocommerce_admin_payment_gateway_suggestion_specs', DefaultPaymentGateways::get_all() );", nth=1),
  "woocommerce_admin_payment_gateway_suggestion_specs", note="When the remote specs are missing, the bundled defaults are used; the filter applies either way.")
S("WC-C-004", "decides", R(SUG, "* Get the list of payment extensions details for a specific country.", "* Get the list of payment extensions details for a specific country."),
  "PaymentsExtensionSuggestions::get_country_extensions")
S("WC-C-004", "decides", R(SUG, "* @return array The list of payment extensions (their full details) for the given country.", "*               Empty array if no extensions are available for the country or the country is not supported."),
  "PaymentsExtensionSuggestions::get_country_extensions")
S("WC-C-004", "decides", R(SUG, "// For Square, we add the preferred tags if the merchant self-identified as selling offline via the core profiler."),
  "PaymentsExtensionSuggestions::with_store_state_details", scope="Square")

# the per-country lists: one statement per country (long lists split into consecutive line ranges)
_here = os.path.dirname(os.path.abspath(__file__))
_blocks = json.load(open(os.path.join(_here, "..", "work", "country_map.json")))
for b in _blocks:
    a, z, cc = b["a"], b["b"], b["cc"]
    whole = RL(SUG, a, z)
    if len(whole["quote"]) <= 330:
        S("WC-C-004", "decides", whole, f"$country_extensions['{cc}']", scope=f"store country {cc}")
        continue
    # cover the country key line and every line naming an extension (self::...) with ranges of at most ~300 characters;
    # lines holding only link details (pricing and terms URLs) between those ranges are not quoted
    from newcite import _L
    L = _L(SUG)
    need = [a] + [i for i in range(a, z + 1) if "self::" in L[i - 1]]
    parts, covered = [], set()
    for ln in need:
        if ln in covered:
            continue
        end = ln
        while end + 1 <= z and len(RL(SUG, ln, end + 1)["quote"]) <= 300:
            end += 1
        # trim trailing lines that name no extension
        while end > ln and "self::" not in L[end - 1]:
            end -= 1
        parts.append((ln, end))
        covered.update(range(ln, end + 1))
    for k, (p, q) in enumerate(parts, start=1):
        if len(parts) == 1:
            nt = f"These lines name every extension in the list for {cc} (lines {a}-{z}); the other lines hold link details (pricing and terms URLs)."
        else:
            nt = f"Part {k} of {len(parts)} of the list for {cc} (lines {a}-{z}); lines between the quoted parts hold link details (pricing and terms URLs)."
        S("WC-C-004", "decides", RL(SUG, p, q), f"$country_extensions['{cc}']", scope=f"store country {cc}", note=nt)

# ---------- WC-C-006 WooPayments ----------
S("WC-C-006", "reason", Old("WC-S-0621"), "PaymentsController",
  note="The comment gives the reason WooPayments owns the Payments menu item once onboarded.")

# ---------- WC-C-007 balance and payouts ----------
S("WC-C-007", "responsible", Old("WC-S-0650"), "Terms 8.j Fees and Negative Balances", scope="Ecommerce Services (Terms 8.j), which name WooPayments")
S("WC-C-007", "reason", Web(WP + "payouts/why-payouts-suspended/",
  "In most cases, payouts are usually paused because there's problem with your bank account that prevents us from issuing a payout.",
  '"Payouts are currently paused..."'), '"Payouts are currently paused"', scope="paused payouts")

# ---------- WC-C-010 availability by country ----------
CTRY = WP + "compatibility/countries/"
S("WC-C-010", "decides", Web(CTRY,
  "Australia Austria Belgium Bulgaria Canada Croatia Cyprus Czech Republic Denmark Estonia Finland France Germany Greece Hong Kong Hungary Ireland Italy Japan Latvia Lithuania Luxembourg Malta Netherlands New Zealand Norway Poland Portugal Romania Singapore Slovakia Slovenia Spain Sweden Switzerland United Arab Emirates United Kingdom United States",
  "Supported countries"), "Supported countries", note="The list that follows 'WooPayments is available for individuals and businesses in:' (WC-S-0511).")
S("WC-C-010", "decides", Web(CTRY, "A business must be located in the 50 states, Washington D.C., or Puerto Rico to sign up with WooPayments as a U.S. business.",
  "Outlying territories of the U.S."), "Outlying territories of the U.S.", scope="U.S. businesses")
S("WC-C-010", "decides", Web(CTRY, "Businesses located in a British Overseas Territory, like Bermuda, or a British Crown Dependency, like Jersey, are not currently supported.",
  "Outlying territories of the UK"), "Outlying territories of the UK", scope="UK businesses")
S("WC-C-010", "decides", Web(CTRY, "Businesses based in a constituent country of the Kingdom of the Netherlands, such as Aruba and Curaçao, are not currently supported.",
  "Outlying territories of the Netherlands"), "Outlying territories of the Netherlands")
S("WC-C-010", "reason", Web(CTRY, "In support of creating a global commerce platform, the WooCommerce team is actively working to make WooPayments available to other countries.",
  "Other countries"), "Other countries")

# ---------- WC-C-011 restricted businesses / accounts ----------
POL = WP + "our-policies/"
S("WC-C-011", "boundary", Web(POL, "If your account is restricted, you should receive an email with more information from either the WooCommerce team or Stripe.",
  "Restricted accounts"), "Restricted accounts")
S("WC-C-011", "where", Web(POL, "However, restricted accounts will still be able to access the Transactions and Disputes menus in order to manage new and existing disputes.",
  "Restricted accounts"), "Restricted accounts", scope="restricted accounts")

# ---------- WC-C-012 fees ----------
FEES = WP + "fees/"
S("WC-C-012", "where", Web(FEES, "The original fee and the matching refund will both appear in the order timeline and fee breakdown.", "Amazon Pay fees"),
  "Amazon Pay fees", scope="Amazon Pay non-card payments")
S("WC-C-012", "decides", Web(FEES, "The country your business is located in. The country your customer is located in. The currency in which the customer paid. The specific payment method used to pay.",
  "WooPayments: Fees"), "WooPayments: Fees", note="The list after 'The exact fees we charge differ based on various factors, such as:' (WC-S-0537).")
S("WC-C-012", "decides", Web(FEES, "Transaction fees are not refunded to you when you issue refunds to customers.", "Notes for all countries"), "Notes for all countries")
S("WC-C-012", "reason", Web(FEES, "Because Amazon Pay is a wallet that can be funded by cards, bank accounts, and other methods, the fees will vary depending on how the shopper chooses to pay.",
  "Amazon Pay fees"), "Amazon Pay fees", scope="Amazon Pay")

# ---------- WC-C-013 fraud rules ----------
S("WC-C-013", "reason", Web(WP + "fraud-and-disputes/fraud-protection/",
  "In order to avoid revealing your specific fraud protection rules to customers, WooPayments will show a generic error message when the rules block a transaction.",
  "What customers see"), "What customers see")

# ---------- WC-C-016 Stripe Capital ----------
S("WC-C-016", "reason", Web(WP + "stripe-capital/overview/",
  "Rather, the withholding starts after seven days in order to ensure the loan payout is completed before payments begin.", "Repayment"), "Repayment")

# ---------- WC-C-019 PCI DSS of the merchant's store ----------
PCI = "https://woocommerce.com/document/pci-dss-compliance-and-woocommerce/"
S("WC-C-019", "responsible", Web(PCI, "PCI DSS compliance is ultimately the responsibility of the store owner.", "WooCommerce and PCI compliance"), "WooCommerce and PCI compliance")
S("WC-C-019", "where", Web(PCI, "The core WooCommerce plugin is not PCI certified, as it does not handle cardholder data or process payments directly.",
  "WooCommerce and PCI compliance"), "WooCommerce and PCI compliance")
S("WC-C-019", "where", Web(PCI, "Many PCI requirements apply to your broader environment - including your hosting provider, the plugins you use, and your policies around user access, updates, and security scans.",
  "WooCommerce and PCI compliance"), "WooCommerce and PCI compliance")
S("WC-C-019", "decides", Web(PCI, "PCI compliance is often enforced by your payment processor, who may ask you to complete a self-assessment questionnaire (SAQ) or undergo scans by an approved scanning vendor (ASV).",
  "Reporting compliance"), "Reporting compliance")
S("WC-C-019", "boundary", Web(PCI, "WooCommerce never stores card details, and official WooCommerce payment gateways only retain partial data when using payment tokens (e.g., last 4 digits).",
  "WooCommerce and PCI compliance"), "WooCommerce and PCI compliance")
S("WC-C-019", "reason", Web(PCI, "However, because your site still serves the checkout page, PCI-DSS does still apply - though your compliance scope may be significantly reduced.",
  "Do I need to be PCI-DSS compliant?"), "Do I need to be PCI-DSS compliant?",
  scope="sites using a gateway that processes payments off-site or through hosted fields")

# ---------- WC-C-021 tax documents ----------
TAXES = WP + "taxes/"
S("WC-C-021", "where", Web(TAXES, "For EU and UKmerchants who may require VAT invoices for WooPayments fees, those are provided under the Payments > Documents menu in your dashboard.",
  "VAT invoices for EU and UK merchants"), "Payments > Documents", scope="EU and UK merchants")
S("WC-C-021", "where", Web(TAXES, "For Japan-based merchants who may require JCT invoices for WooPayments fees, those are provided under the Payments > Documents menu in your dashboard.",
  "JCT invoices for Japan merchants"), "Payments > Documents", scope="Japan-based merchants")

# ---------- WC-C-048 dependence on Stripe ----------
STRIPE = WP + "account-management/partnership-with-stripe/"
S("WC-C-048", "boundary", Old("WC-S-0504"), "WooPayments built in partnership with Stripe")
S("WC-C-048", "boundary", Old("WC-S-0506"), "Access to the Stripe dashboard")
S("WC-C-048", "boundary", Web(STRIPE, "Updating certain account information can only be done in the Stripe Express dashboard.", "Updating account information"),
  "Updating account information")
S("WC-C-048", "decides", Web(STRIPE, "Although WooPayments built in partnership with Stripe, it is not possible to connect an existing Stripe account to WooPayments.",
  "Existing Stripe Accounts"), "Existing Stripe Accounts")

# ---------- WC-C-051 payout currency ----------
PAYC = WP + "payouts/payout-currencies/"
S("WC-C-051", "boundary", Web(PAYC, "To avoid these fees, you may be able to have funds in different currencies paid out into separate bank accounts.",
  "Payout currencies"), "Payout currencies")
S("WC-C-051", "decides", Web(PAYC, "When using multiple bank accounts, one must be chosen as the default.", "Payout currencies"), "Payout currencies")
S("WC-C-051", "reason", Web(WP + "payouts/",
  "If your store accepts multiple currencies, you might also be able to accept payouts in multiple currencies as well, in order to avoid currency conversion fees.",
  "Payouts"), "Payouts")

# ---------- WC-C-057 taxes on Woo's own fees ----------
S("WC-C-057", "where", Web(TAXES, "For EU and UKmerchants who may require VAT invoices for WooPayments fees, those are provided under the Payments > Documents menu in your dashboard.",
  "VAT invoices for EU and UK merchants"), "Payments > Documents", scope="EU and UK merchants")
S("WC-C-057", "responsible", Web(TAXES, "You are responsible for self-accounting for any applicable VAT in your country under the reverse charge mechanism.",
  "VAT invoices for EU and UK merchants"), "VAT invoices for EU and UK merchants",
  scope="VAT-registered businesses whose invoice shows VAT reverse charged")

# ---------- WC-C-116 disputes ----------
DISP = WP + "fraud-and-disputes/managing-disputes/"
S("WC-C-116", "where", Web(DISP, "A red bubble next to the Payments > Disputes menu item.", "Dispute notifications"), "Payments > Disputes")
S("WC-C-116", "where", Web(DISP, "An alert on the order page under WooCommerce > Orders.", "Dispute notifications"), "WooCommerce > Orders")
S("WC-C-116", "boundary", Web(DISP, "An email to the address we have on file for your account.", "Dispute notifications"), "Dispute notifications")
S("WC-C-116", "boundary", Web(DISP, "The disputed amount and the dispute fee are immediately withdrawn from your account and returned to the card issuing bank.",
  "How disputes work"), "How disputes work")
S("WC-C-116", "decides", Web(DISP, "The card issuer (i.e. the customer's bank) decides the outcome.", "How disputes work"), "How disputes work")
S("WC-C-116", "decides", Web(DISP, "NOTE: The dispute outcome is determined solely by the cardholder's bank. Neither we nor our payment processor can influence their decision.",
  "How disputes work"), "How disputes work")
S("WC-C-116", "reason", Web(DISP, "Keep in mind that dispute fees are originally imposed by card networks. These fees get passed through to our payments processor and then to your WooPayments account.",
  "Dispute fees"), "Dispute fees")
