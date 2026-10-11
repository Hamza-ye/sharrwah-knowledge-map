# Concerns C: commerce features the Marketplace offers as extensions, design, business services and other Woo services.
from spec import C, S, N, I
from concerns_a import E, MKT, LEG, TOSL, PPF, WPT, CORE_LEGAL, CORE_LEGAL_NOTE

EXT_LEGAL_NOTE = ("Third-party extensions answer for themselves under the Terms; where the extension is made by Woo "
                  "(listed as by Woo or Developed by Woo) the seller is a Woo entity (WC-C-050).")


def ext_category(cid, concern, terms, cats, extra_match=(), split_note="", software_refs=(), decides_note=""):
    """A commerce concern the Marketplace offers as extensions in the given categories."""
    match = [(MKT, E(c)) for c in cats] + list(extra_match)
    C(cid, concern, terms, split_note, match=match,
      software=S("extension point", [I(MKT, E(cats[0]))] + list(software_refs)),
      decides=S("merchant", ["tos_3p_enable"], decides_note),
      legal=S("app developer", ["tos_3p_not_vetted", "tos_3p_risk"], EXT_LEGAL_NOTE),
      boundary=S("WordPress plugin hooks and filters and WooCommerce extension APIs", ["readme_hooks"]),
      reason=N())


P = "Extensions > "
ext_category("WC-C-100", "Subscriptions (recurring billing)", "Subscriptions",
             [P + "Merchandising > Subscriptions"], extra_match=[(WPT, E("Subscriptions")), (PPF, E("Sell subscriptions, bookings, or memberships"))],
             software_refs=["readme_vetted_ext"], decides_note="The readme points to extensions for subscriptions, bookings and memberships.")
ext_category("WC-C-101", "Bookings and appointments", "Bookings and appointments",
             [P + "Merchandising > Bookings and appointments"], extra_match=[(PPF, E("Sell subscriptions, bookings, or memberships"))], software_refs=["readme_vetted_ext"])
ext_category("WC-C-102", "Memberships", "Memberships",
             [P + "Merchandising > Memberships"], extra_match=[(PPF, E("Sell subscriptions, bookings, or memberships"))], software_refs=["readme_vetted_ext"])
ext_category("WC-C-103", "B2B selling (wholesale, quotes, B2B payments)", "B2B; B2B payments",
             [P + "Merchandising > B2B"])
ext_category("WC-C-104", "Merchandising extensions (bundles, gifts, product options, pricing, display, variations, extra purchases, order options)",
             "Merchandising; Bundles; Gifts; Product options; Pricing; Product display; Product variations; Additional purchases; Order options",
             [P + "Merchandising", P + "Merchandising > Bundles", P + "Merchandising > Gifts", P + "Merchandising > Product options", P + "Merchandising > Pricing",
              P + "Merchandising > Product display", P + "Merchandising > Product variations", P + "Merchandising > Additional purchases", P + "Merchandising > Order options"])
ext_category("WC-C-105", "Conversion extensions (feedback, promotions, order recovery, loyalty, alerts, upsells)", "Conversion",
             [P + "Conversion", P + "Conversion > Customer feedback", P + "Conversion > Promotions", P + "Conversion > Recovering orders",
              P + "Conversion > Rewards and loyalty", P + "Conversion > Store alerts", P + "Conversion > Upsells and cross-sells"])
ext_category("WC-C-106", "Customer service extensions (accounts, live chat, customer management, post-purchase, support)", "Customer service",
             [P + "Customer service", P + "Customer service > Customer Accounts", P + "Customer service > Live chat", P + "Customer service > Managing customers",
              P + "Customer service > Post-purchase services", P + "Customer service > Support"])
ext_category("WC-C-107", "Store content and customization extensions (checkout features, media, search, page enhancements)", "Store content and customizations",
             [P + "Store content and customizations", P + "Store content and customizations > Cart and checkout features", P + "Store content and customizations > Product images and media",
              P + "Store content and customizations > Search and navigation", P + "Store content and customizations > Store page enhancements"])
ext_category("WC-C-108", "International and localization extensions", "International and localization",
             [P + "Store content and customizations > International and localization"],
             split_note="Split from multi-currency (WC-C-053) and store currency (WC-C-052).")
ext_category("WC-C-109", "Store management extensions (insights, import/export, order management, policy and security, notifications, accounting)", "Store management",
             [P + "Store management", P + "Store management > Business insights", P + "Store management > Import and export", P + "Store management > Order management",
              P + "Store management > Policy and security", P + "Store management > Admin and notifications", P + "Store management > Accounting"])
ext_category("WC-C-110", "Marketing extensions (advertising, automation, CRM, reporting, sales channels, SEO, email, social)", "Marketing",
             [P + "Marketing", P + "Marketing > Advertising and promotions", P + "Marketing > Automation", P + "Marketing > CRM", P + "Marketing > Reporting and analytics",
              P + "Marketing > Sales channels", P + "Marketing > SEO and SEM", P + "Marketing > Email", P + "Marketing > Social"],
             extra_match=[(PPF, E("Rise to the top of search results"))], split_note="Split from the core Marketing hub (WC-C-084).")

C("WC-C-111", "Storefront design (themes and block patterns)", "Themes; Choose your theme; Customize your store",
  "", match=[(MKT, E("Themes")), ("^other:onboarding-tasks$", r"^(Choose your theme|Customize your store)$"), ("^api-resources$", r"^(wc/private > /patterns|wc/private|wc-admin > (themes|onboarding/themes))"),
             (PPF, E("Create beautiful, enticing storefronts"))],
  software=S("extension point", [I(MKT, E("Themes")), I("^api-resources$", E("wc/private > /patterns"))], "Themes are installed separately; core ships block patterns."),
  decides=S("merchant", [I("^other:onboarding-tasks$", E("Choose your theme"))]),
  legal=S("app developer", ["tos_3p_not_vetted"], EXT_LEGAL_NOTE),
  boundary=N(),
  reason=N())

C("WC-C-112", "Business services (formation, legal, compliance, insurance, finance)", "Business services",
  "", match=[(MKT, r"^Business services")],
  software=S("outside the platform", [I(MKT, E("Business services")), I(MKT, E("Business services > Compliance"))], "Listed on the Marketplace as services, not store software."),
  decides=S("merchant", ["tos_3p_enable"]),
  legal=S("partner", ["tos_3p_not_vetted"]),
  boundary=N(),
  reason=N())

C("WC-C-113", "Email marketing (MailPoet, a Woo service)", "MailPoet",
  "", match=[(TOSL, E("MailPoet"))],
  software=S("separate service or product line", ["tos_woo_services", "mkt_mailpoet"]),
  decides=S("merchant", ["tos_paid_services"]),
  legal=S("separate entity of the platform", ["tos_woo_services", "tos_woo_inc", "tos_woo_ie"]),
  boundary=N(),
  reason=N())

C("WC-C-114", "WooAds (ad campaign data service)", "WooAds",
  "", match=[(LEG, E("wooads-policy"))],
  software=S("separate service or product line", ["wooads_access"]),
  decides=S("merchant", ["wooads_access"], "The merchant authorizes access to their ad platform data."),
  legal=S("separate entity of the platform", ["wooads_no_share", "priv_controllers"]),
  boundary=S("ad platform APIs; Jetpack data sync module", ["wooads_access", "wooads_jetpack"]),
  reason=N())

C("WC-C-118", "EU VAT number collection and validation (EU VAT Number, a Woo-made extension)", "EU VAT Number",
  "Not in the platform's lists: comes from the question's architecture concern \"currency and tax\" and from the EU VAT Number documentation page (https://woocommerce.com/document/eu-vat-number/). Split from core tax rates (WC-C-054) and automated tax services (WC-C-055).", match=[],
  software=S("extension point", ["doc_euvat", "doc_euvat_settings"]),
  decides=S("merchant", ["doc_euvat_settings"]),
  legal=S("separate entity of the platform", ["doc_euvat_by_woo", "tos_paid_services"], "Listed as by Woo; sold as a Woo Paid Service."),
  boundary=S("settings under WooCommerce > Settings > Tax; VAT number field at checkout", ["doc_euvat_settings", "doc_euvat"]),
  reason=N())
