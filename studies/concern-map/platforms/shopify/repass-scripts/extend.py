# Extends the inventory with the observed-sh lists the first run did not take (questions/Q1-concern-map.md, re-pass step 4),
# adds the concerns no existing concern covers (SH-C-201 on), and writes the unplaced store keys for notes.md (step 5).
# Writes work/inventory-new.tsv, work/new-concerns.tsv, work/unplaced-keys.md, work/key-ties.tsv.
import sys, os, json, re, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

first_inv = rd(os.path.join(FIRST, "inventory.tsv"))
next_inv = max(int(r["inv_id"][5:]) for r in first_inv) + 1
rows = []

def inv(lst, entry, cid, concerns, oos=""):
    global next_inv
    iid = f"SH-I-{next_inv:04d}"
    next_inv += 1
    rows.append({"inv_id": iid, "list": lst, "entry": entry, "cite_id": cid, "concern_ids": ";".join(concerns), "out_of_scope_reason": oos})
    return iid

# all statements so far (for key ties)
stmts = rd(os.path.join(WORK, "reviewed-statements.tsv"))
for f in sorted(glob.glob(os.path.join(WORK, "added", "*.tsv"))):
    stmts += rd(f)

# ---------- 1. admin operation areas ----------
AREAS = [("organizations", "20260930T002940Z-sweep-trial", "OrganizationLegalEntities", "ctcbwa-r1", ["SH-C-003", "SH-C-004", "SH-C-009", "SH-C-010"]),
         ("destinations", "20260930T002940Z-sweep-trial", "ShopsOnlyActiveDestinations", None, ["SH-C-001", "SH-C-003"]),
         ("capital", "20260930T002940Z-sweep-trial", "CapitalAccountOverviewQuery", "ctcbwa-r1", ["SH-C-090", "SH-C-091", "SH-C-092", "SH-C-093", "SH-C-094", "SH-C-095", "SH-C-096", "SH-C-097"]),
         ("banking", "20260930T002940Z-sweep-trial", "CardsIndexQuery", "ctcbwa-r1", ["SH-C-088", "SH-C-089", "SH-C-090"]),
         ("contractmanagement", "20260930T002940Z-sweep-trial", "PlusContractDetails", "ctcbwa-r1", ["SH-C-201"]),
         ("completeness_engine", "20260930T003329Z-pilot-import", "ValidationSchemaByContextQuery", "ibx5bt-xy", ["SH-C-004"]),
         ("profile_assessment", "20260930T002940Z-sweep-trial", "RemediationQuery", "ctcbwa-r1", ["SH-C-008", "SH-C-068"]),
         ("server_intents", "20261006T225457Z-sweep-trial-my-store-8", "ServerIntent", "ts15uk-ug",
          ["SH-C-009", "SH-C-010", "SH-C-020", "SH-C-021", "SH-C-023", "SH-C-024", "SH-C-028", "SH-C-030", "SH-C-037", "SH-C-039", "SH-C-044", "SH-C-055", "SH-C-106", "SH-C-112", "SH-C-114", "SH-C-127"])]
area_inv = {}
for area, run, op, store, cons in AREAS:
    path = f"raw/runs/{run}/answers.jsonl"
    for n, l in enumerate(git_show(path).splitlines(), start=1):
        d = json.loads(l)
        if d["operation"] == op and d["area"] == area and (store is None or d["store"] == store):
            q = f'"endpoint": "{d["endpoint"]}"'
            cid = osh_cite(path, f"line {n} ({op})", q)
            area_inv[area] = inv("other:admin-operation-areas", area, cid, cons)
            break
    else:
        raise SystemExit(f"no {area}")

# ---------- 2. permission tree: ids the first run's permission lists did not hold ----------
PT = "structures/shopify/admin-permission-tree/use-store-options-f948ecd551d0/items.jsonl"
first_entries = set(r["entry"] for r in first_inv)
perm_map = {"VIEW_INVENTORY_PURCHASE_ORDERS": ["SH-C-010", "SH-C-023"], "CREATE_AND_EDIT_INVENTORY_PURCHASE_ORDERS": ["SH-C-010", "SH-C-023"],
            "VIEW_INVENTORY_COUNTS": ["SH-C-010", "SH-C-022"], "MANAGE_INVENTORY_COUNTS": ["SH-C-010", "SH-C-022"], "PERFORM_INVENTORY_COUNTS": ["SH-C-010", "SH-C-022"],
            "MANAGE_AUTOMATIONS": ["SH-C-010", "SH-C-151"], "MANAGE_AUTOMATION_SETTINGS": ["SH-C-010", "SH-C-151"],
            "MANAGE_STAFF_PERMISSIONS": ["SH-C-009", "SH-C-010"], "ADD_REMOVE_STAFF": ["SH-C-009", "SH-C-010"],
            "AUTHENTICATION_MANAGEMENT": ["SH-C-007", "SH-C-010"], "STAFF_API_PERMISSION_MANAGEMENT": ["SH-C-010"],
            "MANAGE_COLLABORATORS": ["SH-C-010", "SH-C-011"], "VIEW_BALANCE_BANK_ACCOUNTS": ["SH-C-010", "SH-C-088"],
            "VIEW_ALL_SHOPIFY_CREDIT_TRANSACTIONS": ["SH-C-010", "SH-C-090"], "VIEW_BILLING_DETAILS": ["SH-C-010", "SH-C-016"],
            "BILLING_PAY_INVOICES": ["SH-C-010", "SH-C-016"]}
seen_ids = set()
for n, l in enumerate(git_show(PT).splitlines(), start=1):
    d = json.loads(l)
    if d["id"] in first_entries or d["id"] in seen_ids:
        continue
    seen_ids.add(d["id"])
    cid = osh_cite(PT, f"line {n} (id {d['id']})", l, sid="shopify/admin-permission-tree")
    assert d["id"] in perm_map, d["id"]
    inv("other:staff-permissions", d["id"], cid, perm_map[d["id"]])

# ---------- 3. access scopes named in access lines, not in the first run's access-scopes list ----------
AL = ["structures/shopify/dev-access-lines/shopify.dev_md/items.jsonl", "structures/shopify/dev-access-lines/shopify.dev_md-sitemap-delta/items.jsonl"]
first_scopes = set(r["entry"] for r in first_inv if r["list"] == "access-scopes")
scope_map = {"customer_merge": ["SH-C-039"], "customer_payment_methods": ["SH-C-085"], "customer_read_payment_instrument_authenticated": ["SH-C-041"],
             "customer_read_pre_authenticated": ["SH-C-041"], "customer_read_unauthenticated": ["SH-C-041"], "customer_write_pre_authenticated": ["SH-C-041"],
             "read_billing": ["SH-C-071"], "read_buyer_membership_orders": ["SH-C-054"],
             "read_capital": ["SH-C-091", "SH-C-092", "SH-C-093", "SH-C-094", "SH-C-095", "SH-C-096", "SH-C-097"],
             "read_customer_address": ["SH-C-146", "SH-C-160"], "read_customer_email": ["SH-C-146", "SH-C-160"], "read_customer_name": ["SH-C-146", "SH-C-160"],
             "read_customer_personal_data": ["SH-C-146", "SH-C-160"], "read_customer_phone": ["SH-C-146", "SH-C-160"],
             "read_images": ["SH-C-027"], "write_images": ["SH-C-027"], "read_mobile_payments": ["SH-C-078"], "write_mobile_payments": ["SH-C-078"],
             "read_payment_session_modals": ["SH-C-076"], "write_payment_session_modals": ["SH-C-076"], "read_point_of_sale_devices": ["SH-C-142"],
             "read_quick_sale": ["SH-C-142"], "write_quick_sale": ["SH-C-142"], "read_shop_promise_program": ["SH-C-125"],
             "read_shopify_payments_legal_entities": ["SH-C-005", "SH-C-063"], "read_shopify_payments_tooling": ["SH-C-069"], "write_shopify_payments_tooling": ["SH-C-069"],
             "write_cart_wallet_payments": ["SH-C-078"], "write_customer_payment_methods": ["SH-C-085"], "write_inventory_purchase_orders": ["SH-C-023"],
             "write_marketplace_fulfillment_orders": ["SH-C-118", "SH-C-137"], "write_pos_staff_member_event_attribution_overrides": ["SH-C-131", "SH-C-142"],
             "write_webhooks": ["SH-C-162"]}
done_scopes = set()
for path in AL:
    for n, l in enumerate(git_show(path).splitlines(), start=1):
        d = json.loads(l)
        for sname in d["named"]:
            if sname in done_scopes or sname in first_scopes or not re.match(r"^(read|write|unauthenticated|customer)_[a-z_]+$", sname):
                continue
            line = d["line"]
            q = line
            if len(q) > 300:
                i = q.index(sname)
                a = max(0, q.rfind(". ", 0, i) + 2 if q.rfind(". ", 0, i) >= 0 else 0)
                b = q.find(". ", i)
                q = q[a:(b + 1 if b >= 0 else len(q))]
                if len(q) > 300:
                    q = q[max(0, i - 120):i + len(sname) + 120]
            cid = osh_cite(path, f"line {n} ({d['page']})", q, sid="shopify/dev-access-lines")
            assert sname in scope_map, sname
            inv("access-scopes", sname, cid, scope_map[sname])
            done_scopes.add(sname)

# ---------- 4. App Store built-in feature pages ----------
BF = "structures/shopify/app-store-built-in-features"
bf_map = {"abandoned-checkout-recovery": ["SH-C-050"], "automated-privacy": ["SH-C-148"], "b2b": ["SH-C-044"], "customer-accounts": ["SH-C-041"],
          "customer-segmentation": ["SH-C-040"], "domains": ["SH-C-033"], "draft-orders": ["SH-C-055"], "gift-cards": ["SH-C-025"], "inventory": ["SH-C-022"],
          "magic-blog-posts": ["SH-C-202"], "magic-product-descriptions": ["SH-C-202"], "managed-markets": ["SH-C-110"], "markets": ["SH-C-106"],
          "metafields-and-metaobjects": ["SH-C-028"], "order-tracking": ["SH-C-126"], "payments": ["SH-C-062"], "product-variants": ["SH-C-020"],
          "shop-pay-installments": ["SH-C-075"], "shop-pay": ["SH-C-074"], "shopify-balance": ["SH-C-088"], "shopify-capital": ["SH-C-091"],
          "shopify-payments": ["SH-C-063"], "shopify-shipping": ["SH-C-116"], "shopify-tax-eu": ["SH-C-100"], "shopify-tax-uk": ["SH-C-100"],
          "shopify-tax-us": ["SH-C-100"], "shopify-theme-store": ["SH-C-029"], "sidekick": ["SH-C-152"], "store-credit": ["SH-C-026"]}
bf_inv = collections.defaultdict(list)
for d in sorted(git_ls(BF)):
    page = d.replace("apps.shopify.com_built-in-features_", "")
    path = f"{BF}/{d}/items.jsonl"
    first = json.loads(git_show(path).splitlines()[0])
    assert first["tag"] == "h3"
    cid = osh_cite(path, "line 1 (h3)", first["text"], sid="shopify/app-store-built-in-features")
    iid = inv("other:app-store-built-in-features", first["text"], cid, bf_map[page])
    for c in bf_map[page]:
        bf_inv[c].append(iid)

# ---------- 5. the merchant's own business entities (organization legal entities, as the admin returns them) ----------
LE = [("raw/runs/20260930T002940Z-sweep-trial/answers/admin.shopify.com/OrganizationLegalEntities/1033e95626c25c43367e339160a0a99a12a0facad9be572e3630832689d14d2a.json",
       '"nickname":"My Store - entity"', "My Store - entity", ["SH-C-004"]),
      ("raw/runs/20260930T045741Z-sweep-trial2/answers/admin.shopify.com/ActiveOrganizationLegalEntities/7683af4f884565954008330f7ebe5ab4803eddf04d6061d5c2763e1582e4204b.json",
       '{"node":{"id":"Z2lkOi8vb3JnYW5pemF0aW9uL0xlZ2FsRW50aXR5LzE5NjQyMjY3MA","countryCode":"YE","archived":false', "Z2lkOi8vb3JnYW5pemF0aW9uL0xlZ2FsRW50aXR5LzE5NjQyMjY3MA", ["SH-C-004", "SH-C-005"]),
      ("raw/runs/20260930T045741Z-sweep-trial2/answers/admin.shopify.com/ActiveOrganizationLegalEntities/7683af4f884565954008330f7ebe5ab4803eddf04d6061d5c2763e1582e4204b.json",
       '{"node":{"id":"Z2lkOi8vb3JnYW5pemF0aW9uL0xlZ2FsRW50aXR5LzE5NjQyMzc4OQ","countryCode":"YE","archived":false', "Z2lkOi8vb3JnYW5pemF0aW9uL0xlZ2FsRW50aXR5LzE5NjQyMzc4OQ", ["SH-C-004", "SH-C-005"]),
      ("raw/runs/20261004T223401Z-journey-business-entity/answers/admin.shopify.com/PersonLegalEntities/1d34bad6d9e7af1bfc72998be05ecca6f6d9faa4480d44ec67fa61218280a00e.json",
       '"legalEntity":{"id":"Z2lkOi8vb3JnYW5pemF0aW9uL0xlZ2FsRW50aXR5LzE5NzUyNTQ1Mg"', "Z2lkOi8vb3JnYW5pemF0aW9uL0xlZ2FsRW50aXR5LzE5NzUyNTQ1Mg", ["SH-C-004"])]
for path, q, entry, cons in LE:
    cid = osh_cite(path, "legal entity", q)
    inv("other:merchant-legal-entities", entry, cid, cons)

# ---------- 6. store keys (entitlements, features, resource limits) and their ties ----------
SRD = "structures/shopify/shop-request-details"
stores = sorted(x for x in git_ls(SRD) if "." not in x)
store_plan, key_lines, key_vals = {}, collections.OrderedDict(), collections.defaultdict(lambda: collections.OrderedDict())
for s in stores:
    plan = collections.defaultdict(dict)
    ls = git_show(f"{SRD}/{s}/items.jsonl").splitlines()
    for n, l in enumerate(ls, start=1):
        d = json.loads(l)
        if d["section"] == "plan":
            plan[d["set"]][d["key"]] = d["value"]
    store_plan[s] = plan
    for n, l in enumerate(ls, start=1):
        d = json.loads(l)
        if d["section"] in ("entitlements", "features", "resourceLimits") and d["key"] not in (None, "__typename"):
            k = (d["section"], d["key"])
            key_lines.setdefault(k, (s, n, l))
            p = plan.get(d["set"], {})
            lab = f"{s} (set {d['set']}: {p.get('displayName') or p.get('name') or 'plan not stated'}{', development store' if p.get('partnerDevelopment') else ''})"
            key_vals[k].setdefault(json.dumps(d["value"], sort_keys=True), []).append(lab)

# routes naming each key, from the router's eligibility objects
RP = "structures/shopify/admin-router/items.jsonl"
route_keys = collections.defaultdict(set)
def walk(o, rid):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("entitlements", "features") and isinstance(v, list):
                for z in v:
                    if isinstance(z, str):
                        route_keys[(k, z.split(".")[0])].add(rid)
            elif isinstance(v, (dict, list)):
                walk(v, rid)
    elif isinstance(o, list):
        for z in o:
            walk(z, rid)
for l in git_show(RP).splitlines():
    d = json.loads(l)
    walk(d.get("eligibility"), d["id"])
    for m in d.get("eligibilityMatch") or []:
        walk(m.get("eligibility"), d["id"])
route_concerns = collections.defaultdict(set)
for r in stmts:
    if r["structure"] == "structures/shopify/admin-router":
        route_concerns[r["identifier"]].add(r["concern_id"])

ties, unplaced = [], []
for (sec, key), (s, n, l) in key_lines.items():
    q = '"section": "%s", "key": "%s"' % (sec, key)
    assert q in l
    cid = osh_cite(f"{SRD}/{s}/items.jsonl", f"line {n} (store {s})", q, sid="shopify/shop-request-details")
    lst = {"entitlements": "other:store-entitlements", "features": "other:store-features", "resourceLimits": "other:store-resource-limits"}[sec]
    routes = sorted(route_keys.get((sec, key), ()))
    cons = sorted(set(c for r in routes for c in route_concerns.get(r, ())))
    if cons:
        inv(lst, key, cid, cons)
        ties.append({"section": sec, "key": key, "routes": " ".join(routes), "concerns": ";".join(cons)})
    else:
        why = ("Unplaced: no Shopify source held ties this key to a concern (" +
               ("routes naming it: " + ", ".join(routes) + ", which no concern's statements cover" if routes else "no route's eligibility in the admin router names it") +
               "); values per store in notes.md, Unplaced keys")
        inv(lst, key, cid, [], why)
        unplaced.append((sec, key, routes))
wr(os.path.join(WORK, "key-ties.tsv"), ["section", "key", "routes", "concerns"], ties)

with open(os.path.join(WORK, "unplaced-keys.md"), "w", encoding="utf-8") as f:
    f.write("### Unplaced keys\n\n")
    f.write("Keys of the admin's RequestDetails answer (`structures/shopify/shop-request-details/<store>/items.jsonl` at `e49840729`) that no Shopify source "
            "held ties to a concern: no route in the admin router names them in its eligibility. They are in the inventory with an out-of-scope reason "
            "that points here. Values are as each store's answer states them; `set` is the answer set within the store's file.\n\n")
    for sec, key, routes in unplaced:
        f.write(f"- `{sec}.{key}`" + (f" (routes naming it, outside any concern's statements: {', '.join(routes)})" if routes else "") + "\n")
        for val, labs in key_vals[(sec, key)].items():
            f.write(f"  - `{val}`: {'; '.join(labs)}\n")
    f.write("\n")

# ---------- new concerns ----------
new = [{"concern_id": "SH-C-201", "concern": "Shopify Plus contract terms and renewals",
        "platform_terms": "Shopify Plus Terms; Switch to 3-year term; Renew on a 3-year term; PlusContractDetails; PlusContractTerms; RenewalsQuery; contractmanagement",
        "inv_ids": area_inv["contractmanagement"],
        "split_note": "New in the re-pass (11 October 2026). Split from SH-C-015 (Subscription plans): the admin keeps the Plus contract and its renewals in their own operation area (contractmanagement) and routes (settings:plan:shop_plus_self_renewals, settings:plan:plus:terms)."},
       {"concern_id": "SH-C-202", "concern": "Shopify Magic for product descriptions and blog posts",
        "platform_terms": "Shopify Magic for product descriptions; Shopify Magic for blog posts; AI generation",
        "inv_ids": ";".join(bf_inv["SH-C-202"]),
        "split_note": "New in the re-pass (11 October 2026). The App Store's built-in feature pages list Shopify Magic for product descriptions and for blog posts as their own features, apart from Sidekick (SH-C-152)."}]
wr(os.path.join(WORK, "new-concerns.tsv"), ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"], new)
wr(os.path.join(WORK, "inventory-new.tsv"), ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"], rows)
save_cites()
c = collections.Counter(r["list"] for r in rows)
print("new inventory entries:", len(rows), dict(c), "; unplaced keys:", len(unplaced), "; tied keys:", len(ties))
