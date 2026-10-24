# Statements from Shopify's web pages: the pages captured in evidence/product-class/runs/20261011T061248Z-q1-shopify-sources,
# and the two Shopify Credit terms pages, read from this run's working copies (fetched/pages; not yet captured).
# Each statement is the sentence of the page that holds the fragment given, normalized as the checker normalizes text.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from weblib import *
A = Adder("web")
VERBOSE = "-v" in sys.argv

TOS = "https://www.shopify.com/legal/terms"
SPT = "https://www.shopify.com/legal/terms-shopify-payments"
API = "https://www.shopify.com/legal/api-terms"
DPA = "https://www.shopify.com/legal/dpa"
CPT = "https://www.shopify.com/legal/shopify-credit-program-terms"
CIB = "https://www.shopify.com/legal/shopify-credit-issuing-bank-terms"
H = "https://help.shopify.com/en/manual/"
DEV = "https://shopify.dev/docs/"

def S(c, placement, url, frag, n=1, ident="", scope="", note="", quote=None):
    q = quote or sentence(url, frag, n)
    cid = wcite(url, q)
    working = url.split("#")[0] not in MANIFEST
    A.add(c, placement, url, ident or url.split("/")[-1], q, scope, cid,
          note + ("; " if note else "") + ("read from this run's working copy (page not in the capture)" if working else ""))
    if VERBOSE:
        print(c, placement, "|", q[:200])

# ---------- where ----------
S("SH-C-159", "where", DEV + "api/usage/access-scopes.md", "Some access scopes need Shopify's approval before you can declare them", 2, "access-scopes")
S("SH-C-160", "where", DEV + "apps/launch/protected-customer-data.md", "Public apps request access to protected customer data and protected customer fields through the Partner Dashboard", 1, "protected-customer-data", "public apps")
S("SH-C-107", "where", H + "payments/shopify-payments/store-currency/understanding-store-and-payout-currencies.md", "Your store currency is the currency used within your Shopify admin", 1, "store currency")
S("SH-C-177", "where", "https://www.shopify.com/legal/p2b/legal-notices", "The P2B complaint form allows Shopify merchants to submit complaints", 1, "P2B Form", "Platform to Business Regulation (EU and UK)")
S("SH-C-179", "where", "https://www.shopify.com/legal/gvtaccesspolicy", "Legal requests for information must be submitted online through our Legal Access Request form", 1, "Legal Access Request form")
S("SH-C-143", "where", TOS, "The POS Services include the Shopify POS software", 1, "9.3 POS Services")
S("SH-C-133", "where", H + "online-sales-channels/shop/shop-campaigns.md", "Your ads can run across the", 1, "Shop Campaigns")
S("SH-C-090", "where", CPT, "Your Transaction History and Card Statements will be available on your Shopify Admin", 1, "Shopify Credit Program Terms")
S("SH-C-090", "where", CPT, "Shopify will communicate the Issuing Bank", 1, "Shopify Credit Program Terms")

S("SH-C-132", "where", H + "promoting-marketing/shopify-audiences.md", "Install Shopify Audiences from the Shopify App Store", 1, "Shopify Audiences")
S("SH-C-161", "where", DEV + "apps/build/compliance/privacy-law-compliance.md", "You can subscribe to the compliance webhook topics by making the following changes", 1, "shopify.app.toml")
S("SH-C-175", "where", H + "compliance/legal/consumer-protection.md", "You can add and display these required, customer-facing warnings on your product pages", 1, "Product disclosures")
S("SH-C-172", "where", "https://www.shopify.com/legal/aup", "If you believe a Shopify user is violating this Acceptable Use Policy, you can submit a report", 1, "Acceptable Use Policy")
S("SH-C-176", "where", TOS, "If you believe content on our platform infringes your intellectual property rights, you can report it here", 1, "11. Intellectual Property Infringement")

# ---------- decides ----------
S("SH-C-176", "decides", TOS, "Posting content that constitutes an infringement of others' legal rights violates our Acceptable Use Policy", 1, "11. Intellectual Property Infringement")
S("SH-C-180", "decides", DPA, "The Parties agree that the Terms together with this DPA constitute Your documented instructions", 1, "Data Processing Addendum")
S("SH-C-142", "decides", TOS, "If you use our POS Services, you must use the same payment processor", 1, "9.3 POS Services")
S("SH-C-033", "decides", TOS, "domain registration will be preset to automatically renew", 1, "2.9 Domain Names")
S("SH-C-067", "decides", SPT, "Where the Payments Services include payment activities that are regulated under the Retail Payment Activities Act", 1, "Regulated Payment Services", "Designated Country Canada")
S("SH-C-090", "decides", CIB, "Following submission of your application, the Issuing Bank will determine your eligibility to participate in the Program", 1, "Issuing Bank Terms")
S("SH-C-090", "decides", CIB, "Issuing Bank reserves the right to decline to provide you a Card Account in its sole discretion", 1, "Issuing Bank Terms")
S("SH-C-090", "decides", CPT, "Based on your application, the Issuing Bank will establish your Credit Limit for the Card Account", 2, "Shopify Credit Program Terms")
S("SH-C-090", "decides", CPT, "The Card Services are only made available to entities or persons in the Territory", 1, "Shopify Credit Program Terms")

S("SH-C-143", "decides", SPT, "you may elect to purchase POS Equipment from Shopify", 1, "POS Equipment")
S("SH-C-143", "where", SPT, "POS hardware may be purchased on the Shopify Hardware Store", 1, "POS Equipment")

# ---------- responsible ----------
S("SH-C-033", "responsible", TOS, "You acknowledge that it is your sole responsibility to deactivate the auto-renewal function", 1, "2.9 Domain Names")
S("SH-C-033", "responsible", TOS, "it will be your sole responsibility to handle all matters related to your domain with the domain provider", 1, "14 Term and Termination")
S("SH-C-142", "responsible", TOS, "we can't guarantee that all transmissions using the POS Equipment are 100% secure", 2, "9.3 POS Services")
S("SH-C-143", "responsible", TOS, "POS Equipment is purchased, and not leased", 3, "9.3 POS Services")
S("SH-C-132", "responsible", TOS, "If you use Shopify Audiences, your use is subject to the Shopify Audiences Terms and Conditions", 1, "9.12 Audiences")
S("SH-C-106", "responsible", H + "international/managed-markets.md", "Unless another party such as Global-e is hired to take on these responsibilities", 2, "merchant of record")
S("SH-C-090", "responsible", CPT, "", 1, "Shopify Credit Program Terms", quote="These Program Terms constitute a legal agreement between you (if your business is a sole proprietorship) or your business (if you are signing up on behalf of a corporation or other legal entity) (the “Merchant”, “you” or “your”) and Shopify Capital Inc., organized under the laws of Virginia")
S("SH-C-090", "responsible", CPT, "acts as a program manager and processor for such Cards", 1, "Shopify Credit Program Terms")
S("SH-C-090", "responsible", CIB, "", 1, "Issuing Bank Terms", quote="These Celtic Bank Issuing Bank Charge Card Terms (these “Issuing Bank Terms”) constitute a legal agreement between Celtic Bank Corporation (“Issuing Bank”, “we”, “us” or “our”)")
S("SH-C-090", "responsible", CIB, "", 1, "Issuing Bank Terms", quote="Issuing Bank has appointed Stripe, Inc. as its program manager for the Program (“Program Manager” or \"Stripe\") and access to the Program has been provided to you by Shopify Capital Inc.")
S("SH-C-090", "responsible", CPT, "While Shopify is not a party to the Issuing Bank Terms", 1, "Shopify Credit Program Terms")
api_tie = {
    "SH-C-163": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-052": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-053": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-083": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-122": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-123": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-124": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-128": ("functions.md", "Stores on any plan can use public apps that are distributed through the Shopify App Store and contain functions."),
    "SH-C-164": ("admin.md", "Your app can extend the Shopify admin"),
    "SH-C-144": ("pos.md", "integrate your app into Shopify Point of Sale"),
    "SH-C-166": ("theme-app-extensions.md", "Create theme extensions for apps that integrate with online stores."),
    "SH-C-167": ("", ""),
    "SH-C-165": ("customer-accounts.md", "Building apps for customer accounts"),
    "SH-C-162": ("webhooks.md", "When your app needs information about specific events that have occurred on a shop, it can subscribe to Shopify webhook topics"),
}
api_q = sentence(API, "Developer must inform Merchants in the Merchant Agreement that", 3)
if "(iii)" in api_q:
    api_q = api_q[:api_q.index("(iii)")].rstrip()
for c, (page, tie) in api_tie.items():
    note = "API License and Terms of Use speak of the Developer's Application"
    if page:
        note += f"; shopify.dev {page} ties the concern to apps: \"{tie}\""
    S(c, "responsible", API, "", 1, "API License and Terms of Use", "Developers' Applications", note, quote=api_q)

# ---------- boundary ----------
S("SH-C-130", "boundary", TOS, "Shopify's Email Services utilize Third Party Providers", 2, "9.7 Shopify Email", "Email Services")
S("SH-C-090", "boundary", CPT, "Shopify will develop, operate, maintain, and host a secure application programming interface", 1, "Shopify Credit Program Terms")
tps = sentence(TOS, "If you install or enable a Third Party Service for use with the Services", 1)
for c in ["SH-C-154", "SH-C-185", "SH-C-187", "SH-C-189", "SH-C-190", "SH-C-191", "SH-C-192", "SH-C-194", "SH-C-196"]:
    S(c, "boundary", TOS, "", 1, "9.9 Third Party Services and Third Party Partners",
      "Third Party Services, including Apps via the Shopify App Store", "the concern is an App Store category; 9.9 defines Third Party Services to include Apps offered via the Shopify App Store", quote=tps)

# ---------- reason ----------
S("SH-C-142", "reason", H + "apps/apps-by-shopify.md", "German merchants can meet TSE Compliance", 1, "TSE Compliance", "Germany")
S("SH-C-148", "reason", H + "privacy-and-security/privacy/customer-privacy-settings.md", "Because privacy laws and regulations vary across different regions", 1, "Customer privacy")
S("SH-C-078", "reason", H + "payments/accelerated-checkouts.md", "Accelerated or express checkouts save customer payment and shipping information so that", 1, "accelerated checkouts", "", "stated purpose")
S("SH-C-111", "reason", H + "international/pricing.md", "so that customers can select their local country or region and your store displays their local currency", 1, "country selector")
S("SH-C-090", "reason", H + "finance/shopify-credit/getting-started.md", "We continuously review your business to ensure our products remain suitable and beneficial", 1, "Shopify Credit")
S("SH-C-183", "reason", DPA, "Shopify may retain Your Customer Personal Data", 3, "Data Processing Addendum")
A.save()
