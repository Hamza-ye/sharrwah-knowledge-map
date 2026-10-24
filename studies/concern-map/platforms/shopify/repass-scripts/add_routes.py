# Admin router routes for concerns whose location or eligibility the review left empty or reassigned.
# Each statement is a verbatim excerpt of structures/shopify/admin-router/items.jsonl at the re-pass commit:
#   where:   "section":...,"path":...,"title":{...}   (the route's own section, path and title, as written)
#   decides: "eligibility":{...}                      (the route's stated eligibility object, as written)
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
A = Adder("routes")
RP = "structures/shopify/admin-router/items.jsonl"
lines = git_show(RP).splitlines()
byid = {}
for n, l in enumerate(lines, start=1):
    d = json.loads(l)
    byid[d["id"]] = (n, l, d)

def balanced(text, start):
    depth, i, in_str, esc = 0, start, False, False
    while i < len(text):
        ch = text[i]
        if in_str:
            if esc: esc = False
            elif ch == "\\": esc = True
            elif ch == '"': in_str = False
        elif ch == '"': in_str = True
        elif ch in "{[": depth += 1
        elif ch in "}]":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
        i += 1
    return None

def where_quote(rid):
    n, l, d = byid[rid]
    i = l.index('"section":')
    j = i + len('"section":') + len(json.dumps(d["section"]))
    if l.startswith(',"path":', j):
        j = j + len(',"path":') + len(json.dumps(d["path"], ensure_ascii=False))
    if l.startswith(',"title":', j):
        t = balanced(l, j + len(',"title":'))
        if isinstance(d.get("title"), dict) and set(d["title"]) != {"value"}:
            v = ',"title":{"value":' + json.dumps(d["title"]["value"], ensure_ascii=False)
            assert l.startswith(v, j), rid
            j = j + len(v)
        else:
            j = j + len(',"title":') + len(t)
    q = l[i:j]
    assert q in l
    return n, q

def elig_quote(rid):
    n, l, d = byid[rid]
    i = l.index('"eligibility":')
    obj = balanced(l, i + len('"eligibility":'))
    return n, '"eligibility":' + obj

def W(c, rid, note=""):
    n, q = where_quote(rid)
    cid = osh_cite(RP, f"line {n} ({rid})", q, sid="shopify/admin-router")
    A.add(c, "where", "structures/shopify/admin-router", rid, q, "", cid, ("route's section, path and title as the router states them" + ("; " + note if note else "")))

def D(c, rid, note=""):
    n, q = elig_quote(rid)
    cid = osh_cite(RP, f"line {n} ({rid})", q, sid="shopify/admin-router")
    A.add(c, "decides", "structures/shopify/admin-router", rid, q, "", cid, ("eligibility the router states for the route" + ("; " + note if note else "")))

W("SH-C-004", "settings:general:switch-business-entity", "titled Switch business entity, under Settings > General")
D("SH-C-004", "settings:general:switch-business-entity")
W("SH-C-004", "settings:organizations:details:business-entities", "organization settings")
W("SH-C-005", "payments:settings:business-entity", "payments settings per business entity")
D("SH-C-013", "settings:general")
W("SH-C-014", "store-unavailable")
W("SH-C-026", "customer-store-credit-transaction-history:show")
W("SH-C-026", "customer-store-credit-edit-balance:update")
W("SH-C-034", "setting:legal:index")
D("SH-C-034", "setting:legal")
D("SH-C-034", "setting:legal:cancel_return_policy_create")
W("SH-C-040", "customer-segments")
W("SH-C-042", "identityProviders:auth")
W("SH-C-042", "customerAuthenticationSettings:parent")
W("SH-C-043", "customer:mobile:edit-marketing-status")
W("SH-C-055", "draftOrders:new")
W("SH-C-056", "order:edit")
W("SH-C-056", "order:requested-edit:decline")
W("SH-C-057", "order:refund:create")
W("SH-C-058", "order:return:create")
W("SH-C-058", "order:return-request:review")
W("SH-C-061", "packing-slips")
W("SH-C-061", "document-template-editor")
W("SH-C-069", "payouts")
W("SH-C-069", "finance:payout-reconciliation-report")
W("SH-C-071", "shopify-payments:fees")
W("SH-C-071", "payments:settings:shopify-payments:payments-rates")
W("SH-C-072", "dispute-evidences")
W("SH-C-072", "finance:risk:disputes")
W("SH-C-073", "shopify-protect")
W("SH-C-073", "fraud_protect", "section Reviews")
W("SH-C-073", "seller-protection", "section Reviews")
W("SH-C-074", "payments:settings:shop-pay")
D("SH-C-074", "payments:settings:shop-pay")
W("SH-C-075", "payments:settings:shop-pay-installments")
W("SH-C-075", "payments:shop-pay-installments")
W("SH-C-075", "shop-pay-installments-terms")
W("SH-C-076", "payments:settings:third-party-providers:list")
W("SH-C-076", "payments:settings:alternative-providers")
D("SH-C-076", "payments:settings:third-party-providers:list")
W("SH-C-077", "payments:settings:paypal-express-checkout")
D("SH-C-077", "payments:settings:paypal-express-checkout")
W("SH-C-079", "payments:settings:manual-payment-methods")
D("SH-C-079", "payments:settings:manual-payment-methods")
W("SH-C-080", "shopify-payments:local-payment-methods")
W("SH-C-083", "payments:settings:payment-customizations")
W("SH-C-085", "customer-payment-methods:show")
W("SH-C-099", "finance:tax-forms:1099-k")
W("SH-C-099", "finance:tax-forms:1099-misc")
W("SH-C-100", "tax-settings")
W("SH-C-101", "tax-settings:show-eu:add-registration")
W("SH-C-101", "tax-settings:ioss-registration")
W("SH-C-102", "tax-settings:shared:vat-number-validation")
W("SH-C-103", "tax-settings:providers-manage")
W("SH-C-103", "tax-settings:partner")
W("SH-C-105", "tax-settings:duties-and-taxes")
W("SH-C-110", "market:managed")
W("SH-C-110", "market:update:managed")
W("SH-C-114", "delivery-profile:create")
W("SH-C-115", "shipping-carrier-services:update")
W("SH-C-118", "batches:index")
D("SH-C-118", "batches:index")
W("SH-C-121", "local-delivery:list")
W("SH-C-121", "pickup-in-store:list")
W("SH-C-124", "pickup-point:list")
W("SH-C-125", "shipping:list:shop-promise-examples")
W("SH-C-060", "order-routing:update")
W("SH-C-150", "notification-settings")
W("SH-C-162", "notification-settings:webhooks", "webhooks under Settings > Notifications")
W("SH-C-167", "apps:development_list")
W("SH-C-167", "apps:development_enable")
W("SH-C-169", "settings:organizations:partner-payouts")
A.save()
