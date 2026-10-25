"""Shopify admin-router: sections, resources, eligibility permissions; overlap with permission ids."""
import json
import sys
from collections import Counter, defaultdict

B = "/home/user/observed-sh/structures/shopify"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


routes = load(f"{B}/admin-router/items.jsonl")
tree = load(f"{B}/admin-permission-tree/use-store-options-f948ecd551d0/items.jsonl")
cats = load(f"{B}/admin-permission-tree/use-store-options-f948ecd551d0/categories.jsonl")
roleperm = load(f"{B}/admin-role-permissions/ctcbwa-r1/items.jsonl")
assign = load(f"{B}/admin-assignable-permissions/ctcbwa-r1/items.jsonl")

sections = Counter(r.get("section") for r in routes)
print("SECTIONS", len(sections))
print(sorted(sections.items(), key=lambda x: (-x[1], str(x[0]))))
resources = Counter(r.get("resource") for r in routes)
print("RESOURCES", len(resources))
print(sorted(resources.items(), key=lambda x: (-x[1], str(x[0])))[:200])

elig_perm = Counter()
elig_ent = Counter()
elig_keys = Counter()
for r in routes:
    e = r.get("eligibility")
    if isinstance(e, dict):
        elig_keys.update(e.keys())
        for p in e.get("permissions", []) or []:
            elig_perm[p if isinstance(p, str) else json.dumps(p)] += 1
        for p in e.get("entitlements", []) or []:
            elig_ent[p if isinstance(p, str) else json.dumps(p)] += 1
print("ELIG KEYS", dict(elig_keys))
print("ELIG PERMISSIONS", len(elig_perm))
print(sorted(elig_perm.items(), key=lambda x: -x[1]))
print("ELIG ENTITLEMENTS", len(elig_ent))

tree_ids = {t["id"] for t in tree}
rp_handles = {r["handle"] for r in roleperm}
as_handles = {a["value"] for a in assign}
ep = set(elig_perm)
print("tree ids", len(tree_ids), "roleperm handles", len(rp_handles), "assignable", len(as_handles), "elig perms", len(ep))
print("elig ∩ tree", len(ep & tree_ids), "elig - tree", sorted(ep - tree_ids))
print("elig ∩ assignable", len(ep & as_handles), "elig - assignable", sorted(ep - as_handles))
print("tree - assignable", sorted(tree_ids - as_handles))
print("assignable - tree", sorted(as_handles - tree_ids))
print("roleperm - assignable", sorted(rp_handles - as_handles))
print("CATEGORIES", [(c["id"], c["title"]) for c in cats])
bycat = defaultdict(list)
for t in tree:
    bycat[t["category"]].append(t["id"])
for c, ids in bycat.items():
    print(" ", c, len(ids), ids[:60])
