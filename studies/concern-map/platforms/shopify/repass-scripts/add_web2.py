# Statements from the pages read on 11 October 2026 for the gaps marked "page not read" (coordinator's request):
# the Shop Campaigns Merchant Terms, the Shopify Collabs Terms, Help Center pages for concerns no captured page covered,
# and the shopify.dev POS UI and admin UI extension references. Pages cited here are captured in
# fetched/capture/<UTC>-q1r-shopify-more.
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from weblib import *
A = Adder("web2")
VERBOSE = "-v" in sys.argv
H = "https://help.shopify.com/en/manual/"
SCT = "https://www.shopify.com/legal/shop-campaigns-merchant-terms"
COL = "https://collabs.shopify.com/terms"
POSX = "https://shopify.dev/docs/api/pos-ui-extensions.md"
ADMX = "https://shopify.dev/docs/api/admin-extensions.md"

def S(c, placement, url, frag, n=1, ident="", scope="", note="", quote=None):
    q = quote or sentence(url, frag, n)
    cid = wcite(url, q)
    A.add(c, placement, url, ident or re.sub(r"^https?://", "", url), q, scope, cid, note)
    if VERBOSE:
        print(c, placement, "|", q[:220])

# ---------- responsible ----------
S("SH-C-133", "responsible", SCT, "The Advertiser Merchant is responsible for fulfillment of goods and services", 1, "Shop Campaigns Merchant Terms")
S("SH-C-133", "responsible", SCT, "Advertiser Merchant is responsible for collecting and remitting taxes", 1, "Shop Campaigns Merchant Terms")
S("SH-C-134", "responsible", COL, "Shopify is under no circumstance a party to the Program Agreement", 1, "Shopify Collabs Terms")
S("SH-C-134", "responsible", COL, "Merchant will be solely responsible for paying Creators any commissions", 1, "Shopify Collabs Terms")
S("SH-C-141", "responsible", H + "online-sales-channels/shopify-collective/suppliers/payments.md", "It's your responsibility to then agree with each retailer", 1,
  "Shopify Collective (suppliers)", "suppliers who turn off automatic payments with a retailer")
S("SH-C-154", "responsible", H + "online-sales-channels/shop/product-reviews.md", "Shop isn't responsible for the content, accuracy, or reliability of the reviews", 1,
  "Shop product reviews", "product reviews in the Shop app")
S("SH-C-167", "responsible", H + "apps/app-types/custom-apps.md", "The developer of an unsupported app is responsible for updating their app", 1, "custom apps")

# ---------- boundary ----------
S("SH-C-133", "boundary", SCT, "you agree that your use is subject to these Shop Campaigns Merchant Terms of Service", 1, "Shop Campaigns Merchant Terms")
S("SH-C-134", "boundary", COL, "govern your access to and use of the Shopify Collabs application", 1, "Shopify Collabs Terms")

S("SH-C-176", "boundary", H + "compliance/intellectual-property/copyright-policy.md", "online form", 1, "Reporting copyright infringement")
S("SH-C-184", "responsible", "https://www.shopify.com/legal/compliance/reports", "This is Shopify's service provider PCI DSS AOC", 1, "PCI Attestation of Compliance (AoC)")

# ---------- decides ----------
S("SH-C-133", "decides", SCT, "in the case of Offers, determine Buyers eligible to see or redeem Offers", 2, "Shop Campaigns Merchant Terms")
S("SH-C-046", "decides", H + "checkout-settings/add-to-cart-limit.md", "A recommended limit for your store displays in the", 1, "Add-to-cart limit")
S("SH-C-046", "decides", H + "checkout-settings/add-to-cart-limit.md", "then the default recommended limit for your store is set to 50", 1, "Add-to-cart limit", "stores with fewer than 250 sales")
S("SH-C-144", "decides", POSX, "Your compiled UI extension bundle can't exceed 64 KB", 1, "POS UI extensions")
S("SH-C-144", "decides", POSX, "App authentication is available as of POS version 10.6.0", 1, "POS UI extensions")
S("SH-C-164", "decides", ADMX, "Your compiled UI extension bundle can't exceed 64 KB", 1, "Admin UI extensions")
S("SH-C-202", "decides", H + "ai-powered-tools/shopify-magic.md", "Many of these features are available at no additional cost", 1, "AI features in the Shopify admin")

# ---------- reason ----------
S("SH-C-046", "reason", H + "checkout-settings/add-to-cart-limit.md", "To protect your inventory information, you can set a limit", 1, "add-to-cart limit")
S("SH-C-028", "reason", H + "custom-data/overview.md", "Because standard metafield definitions follow standards that are used across all Shopify stores", 1, "standard metafield definitions")
S("SH-C-011", "reason", H + "your-account/users/security/collaborator-accounts.md", "Two-step authentication helps prevent security breaches", 1, "collaborator accounts", "",
  "the page's preceding sentence says collaborators must activate two-step authentication to use a collaborator account")
S("SH-C-087", "reason", H + "sell-in-person/hardware/cash-drawer.md", "This is a security behavior to prevent cash drawers from opening unexpectedly", 1, "cash drawers")
S("SH-C-032", "reason", H + "international/localization-and-translation.md", "You can add languages to your online store so that international customers", 1, "languages")
S("SH-C-027", "reason", H + "shopify-admin/productivity-tools/file-uploads.md", "Shopify's Imagery service manages your images and videos", 1, "Imagery service")
S("SH-C-144", "reason", POSX, "Shopify enforces this limit at deployment to ensure fast loading times", 1, "POS UI extensions")
S("SH-C-164", "reason", ADMX, "Shopify enforces this limit at deployment to ensure fast loading times", 1, "Admin UI extensions")
A.save()
