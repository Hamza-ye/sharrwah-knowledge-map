# Boundary statements from the held API schemas, for concerns whose boundary cell was empty:
# a type of the GraphQL Admin API (2026-10) or the Partner API (2025-10) that names the concern, with the schema's own description.
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
A = Adder("schema")

def T(c, path, name, scope, note="", field_of=None, field=None):
    lines = git_show(path).splitlines()
    for n, l in enumerate(lines, start=1):
        d = json.loads(l)
        if field_of is None and d["name"] == name:
            q = '"name": "%s", "kind": "%s", "description": %s' % (d["name"], d["kind"], json.dumps(d["description"], ensure_ascii=False))
            assert q in l, name
            cid = osh_cite(path, f"line {n} (type {name})", q, sid="shopify/" + path.split("/")[2])
            A.add(c, "boundary", "structures/shopify/" + path.split("/")[2], name, q, scope, cid, note or "a type of the API, with the schema's own description")
            return
        if field_of is not None and d["name"] == field_of:
            for f in d.get("fields") or []:
                if f["name"] == field:
                    q = json.dumps(f, ensure_ascii=False)
                    assert q in l, field
                    cid = osh_cite(path, f"line {n} (type {field_of}, field {field})", q, sid="shopify/" + path.split("/")[2])
                    A.add(c, "boundary", "structures/shopify/" + path.split("/")[2], f"{field_of}.{field}", q, scope, cid,
                          note or f"a field of the API's {field_of} type")
                    return
    raise SystemExit(f"not found: {name} {field_of} {field}")

AS = "structures/shopify/admin-graphql-schema/2026-10/items.jsonl"
PS = "structures/shopify/partner-graphql-schema/2025-10/items.jsonl"
adm, par = "GraphQL Admin API 2026-10", "Partner API 2025-10"
T("SH-C-015", AS, "ShopPlan", adm)
T("SH-C-015", AS, None, adm, field_of="Shop", field="plan")
T("SH-C-038", AS, "CombinedListing", adm)
T("SH-C-105", AS, "Duty", adm)
T("SH-C-107", AS, None, adm, "the Shop type's currencyCode field; the Help Center calls the currency 'used within your Shopify admin for pricing products' the store currency", field_of="Shop", field="currencyCode")
T("SH-C-111", AS, "MarketWebPresence", adm)
T("SH-C-126", AS, "FulfillmentTrackingInfo", adm)
T("SH-C-062", AS, "PaymentSettings", adm)
T("SH-C-142", AS, "PointOfSaleDevice", adm)
T("SH-C-042", AS, "IdentityProviderSubject", adm)
T("SH-C-168", PS, "Organization", par)
T("SH-C-169", PS, "Transaction", par)

def E(c, path, typ, value, scope, note):
    lines = git_show(path).splitlines()
    for n, l in enumerate(lines, start=1):
        d = json.loads(l)
        if d["name"] == typ:
            for e in d.get("enumValues") or []:
                if e["name"] == value:
                    q = json.dumps(e, ensure_ascii=False)
                    assert q in l
                    cid = osh_cite(path, f"line {n} (enum {typ}, value {value})", q, sid="shopify/" + path.split("/")[2])
                    A.add(c, "boundary", "structures/shopify/" + path.split("/")[2], f"{typ}.{value}", q, scope, cid,
                          note + f"; the enum's own description: '{d.get('description')}'")
                    return
    raise SystemExit(f"not found {typ}.{value}")
T("SH-C-036", AS, None, adm, "a field of the API's Domain type", field_of="Domain", field="sslEnabled")
E("SH-C-011", AS, "AccountType", "COLLABORATOR", adm, "a value of the API's AccountType enum")
E("SH-C-141", AS, "ShopifyPaymentsTransactionType", "SHOPIFY_COLLECTIVE_DEBIT", adm, "a value of the API's ShopifyPaymentsTransactionType enum")
E("SH-C-141", AS, "ShopifyPaymentsTransactionType", "SHOPIFY_COLLECTIVE_CREDIT", adm, "a value of the API's ShopifyPaymentsTransactionType enum")
E("SH-C-117", AS, "ShippingLabelPurchaseUserErrorCode", "MISSING_INSURANCE_COVERAGE_AMOUNT", adm, "an error code of the API's shipping label purchase")

# access lines that name the concern (structures/shopify/dev-access-lines)
AL = "structures/shopify/dev-access-lines/shopify.dev_md/items.jsonl"
al = {n: json.loads(l) for n, l in enumerate(git_show(AL).splitlines(), start=1)}
def L(c, n, ident, note):
    d = al[n]
    q = d["line"].strip()
    cid = osh_cite(AL, f"line {n} ({d['page']})", q, sid="shopify/dev-access-lines")
    A.add(c, "boundary", "structures/shopify/dev-access-lines", ident, q, "", cid, note + f"; access line on {d['page']}")
L("SH-C-160", 1551, "shopifyqlQuery (read_reports; Level 2 access to Customer data)", "the access line names protected customer data")
L("SH-C-160", 1978, "read_customer_email", "the access line names protected customer data")
for c in ["SH-C-094", "SH-C-095", "SH-C-096", "SH-C-097"]:
    L(c, 1357, "read_capital", "the scope and the Capital permission are not country-specific")
A.save()
