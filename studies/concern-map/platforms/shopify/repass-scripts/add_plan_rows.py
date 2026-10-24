# Plan table rows with their values per plan, for concerns whose first-run plan citation was a row label only.
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
A = Adder("plan-rows")
PUB = "structures/shopify/plan-comparison-public/www.shopify.com_pricing/items.jsonl"
ADM = "structures/shopify/plan-comparison-admin/ibx5bt-xy/items.jsonl"
pub = git_show(PUB).splitlines()
adm = git_show(ADM).splitlines()
head = json.loads(pub[1])
cols = [c["text"] for c in head["cells"][1:]]
LABELS = {
 "SH-C-003": ["Free expansion stores"], "SH-C-009": ["Additional staff accounts"], "SH-C-010": ["Custom user groups"],
 "SH-C-011": ["Invite third-party collaborators"], "SH-C-015": ["Pay monthly", "Pay yearly"], "SH-C-018": ["Third-party transaction fees"],
 "SH-C-020": ["Sell unlimited products"], "SH-C-022": ["Inventory management"], "SH-C-024": ["Inventory locations"],
 "SH-C-025": ["Sell gift cards"], "SH-C-029": ["Themes and templates"], "SH-C-032": ["Translate your storefront"],
 "SH-C-033": ["Custom domain name"], "SH-C-036": ["Free SSL certificate", "Unlimited web hosting"],
 "SH-C-038": ["Merchandise with Shopify Combined Listings"], "SH-C-039": ["Unlimited contacts"], "SH-C-040": ["Create customer segments"],
 "SH-C-044": ["Shopify B2B"], "SH-C-047": ["High volume checkout", "World's best-converting checkout"], "SH-C-048": ["Checkout customization"],
 "SH-C-050": ["Abandoned checkout recovery"], "SH-C-059": ["Built-in fraud analysis*"], "SH-C-071": ["Online international rates", "Online standard card rates"],
 "SH-C-080": ["Accept local payment methods*"], "SH-C-081": ["USDC rates"], "SH-C-088": ["Manage money with Shopify Balance¹"],
 "SH-C-090": ["Shopify Credit pay-in-full Visa® card³"], "SH-C-101": ["Tax liability tracking"], "SH-C-102": ["VAT validation, exemptions, and invoicing"],
 "SH-C-108": ["Show prices in local currencies*"], "SH-C-111": ["Assign local domains"], "SH-C-115": ["3rd-party calculated shipping rates"],
 "SH-C-117": ["Shipping insurance*"], "SH-C-127": ["Create and share discount codes"], "SH-C-129": ["Create marketing automations"],
 "SH-C-130": ["Create email campaigns", "Pay-per-send SMS campaigns"], "SH-C-132": ["Optimize ads with Shopify Audiences"],
 "SH-C-133": ["Acquire customers risk-free with Shop Campaigns"], "SH-C-135": ["Sell on social and marketplaces"],
 "SH-C-137": ["Import unlimited orders from marketplaces"], "SH-C-139": ["Build headless storefronts"], "SH-C-140": ["Sell in AI chats"],
 "SH-C-141": ["Sell and source products with Shopify Collective"], "SH-C-142": ["POS Pro: Advanced tools for brick‑and‑mortar retailers"],
 "SH-C-145": ["200+ real-time reports, plus custom analytics"], "SH-C-153": ["Chat with customers"], "SH-C-155": ["24/7 support"],
 "SH-C-163": ["Personalize store with custom functions"], "SH-C-167": ["Build custom apps using Shopify APIs"], "SH-C-171": ["Up to 500% higher API call limits"],
}
EXTRA = {
 "SH-C-051": ["Bot protection"], "SH-C-063": ["Shopify Payments"], "SH-C-071": ["Online premium card rates"],
 "SH-C-077": ["PayPal Wallet rates"], "SH-C-080": ["MB WAY rates", "Bizum rates"], "SH-C-086": ["In-person card rates", "In-person manual rates"],
 "SH-C-091": ["Flexible growth funding through Shopify Capital\u00b2"], "SH-C-092": ["Flexible growth funding through Shopify Capital\u00b2"],
 "SH-C-093": ["Flexible growth funding through Shopify Capital\u00b2"], "SH-C-094": ["Flexible growth funding through Shopify Capital\u00b2"],
 "SH-C-095": ["Flexible growth funding through Shopify Capital\u00b2"], "SH-C-096": ["Flexible growth funding through Shopify Capital\u00b2"],
 "SH-C-097": ["Flexible growth funding through Shopify Capital\u00b2"], "SH-C-098": ["Schedule, pay, and manage bills with Shopify Bill Pay"],
 "SH-C-100": ["Automated sales tax calculations"], "SH-C-103": ["Advanced tax platform"], "SH-C-106": ["Localized selling with Shopify Markets"],
 "SH-C-116": ["Shipping discounts", "Buy and print shipping labels"], "SH-C-137": ["50 synced marketplace orders per month", "Over 50 synced marketplace orders"],
 "SH-C-142": ["Casual, in-person sales at pop-ups and events"], "SH-C-152": ["Sidekick, AI assistant for commerce"],
 "SH-C-155": ["Free Shopify Academy courses"], "SH-C-156": ["Integrate with 1000s of apps"], "SH-C-157": ["Plus Certified apps"],
 "SH-C-171": ["API rate limits"],
}
for c, labs in EXTRA.items():
    LABELS.setdefault(c, [])
    LABELS[c] = LABELS[c] + [l for l in labs if l not in LABELS[c]]
found = set()
for n, line in enumerate(pub, start=1):
    d = json.loads(line)
    if d.get("kind") != "row" or not d.get("cells"):
        continue
    lab = d["cells"][0]["text"]
    vals = [c["text"] for c in d["cells"][1:]]
    for c, labs in LABELS.items():
        for want in labs:
            if lab == want:
                if len(line) > 420:
                    print("long row", c, len(line))
                cid = osh_cite(PUB, f"line {n} (row '{lab}')", line, sid="shopify/plan-comparison-public")
                scope = "plans, one cell each, in the order of the table header: " + ", ".join(cols)
                A.add(c, "decides", "structures/shopify/plan-comparison-public", lab, line, scope, cid,
                      "plan table row with its values per plan, replacing the first run's row label")
                found.add((c, want))
for c, labs in LABELS.items():
    for want in labs:
        if (c, want) not in found:
            print("NOT FOUND", c, want)
# the admin plan comparison row for duties
for n, line in enumerate(adm, start=1):
    if '"Estimate and collect duties and taxes"' in line:
        cid = osh_cite(ADM, f"line {n}", line, sid="shopify/plan-comparison-admin")
        A.add("SH-C-105", "decides", "structures/shopify/plan-comparison-admin (ibx5bt-xy)", "Estimate and collect duties and taxes", line,
              "store ibx5bt-xy (trial), Compare plans table in Settings > Plan", cid, "admin plan table row with its cells per plan")
A.save()
