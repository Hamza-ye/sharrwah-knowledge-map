"""Shopify GraphQL reference nav categories and schema enums of interest."""
import json
from collections import Counter

B = "/home/user/observed-sh/structures/shopify"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


nav = load(f"{B}/admin-graphql-reference-nav/shopify.dev@latest/items.jsonl")


def leaves(node, path=()):
    ch = node.get("children")
    if ch:
        for c in ch:
            yield from leaves(c, path + (node.get("label"),))
    else:
        yield path + (node.get("label"),), node.get("href")


allleaf = {}
for cat in nav:
    kinds = Counter()
    for path, href in leaves(cat):
        kinds[path[1] if len(path) > 1 else "?"] += 1
        allleaf.setdefault(path[-1], set()).add(cat["label"])
    subs = [c.get("label") for c in cat.get("children", [])]
    print(cat["label"], dict(kinds))
print("distinct leaf labels", len(allleaf))
multi = {k: v for k, v in allleaf.items() if len(v) > 1}
print("leaf labels in more than one category", len(multi), list(multi.items())[:15])

schema = {t["name"]: t for t in load(f"{B}/admin-graphql-schema/2026-10/items.jsonl")}
print("schema types", len(schema))
for name in ("WebhookSubscriptionTopic", "AccessScope", "StaffMemberPermission", "AppInstallation", "ShopPlan"):
    t = schema.get(name)
    if not t:
        print("MISSING", name)
        continue
    ev = t.get("enumValues") or []
    print(name, t["kind"], "enumValues", len(ev), "fields", len(t.get("fields") or []))
    if ev:
        print("  ", [e["name"] if isinstance(e, dict) else e for e in ev][:400])
q = schema["QueryRoot"]["fields"]
m = schema["Mutation"]["fields"]
print("QueryRoot fields", len(q), "Mutation fields", len(m))
# how many query/mutation names appear in the reference nav leaves
qn = {f["name"] for f in q}
mn = {f["name"] for f in m}
print("queries in nav", len(qn & set(allleaf)), "mutations in nav", len(mn & set(allleaf)))
print("types in nav", len(set(schema) & set(allleaf)), "of", len(schema))
