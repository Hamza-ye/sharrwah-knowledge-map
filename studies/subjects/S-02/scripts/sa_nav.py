"""Salla dashboard-nav tree with permissions; permission groups; overlap."""
import json
from collections import Counter

B = "/home/user/observed-sa/structures/salla"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


nav = load(f"{B}/dashboard-nav/prod/items.jsonl")
navperms = Counter()
nodes = 0


def walk(n, depth=0):
    global nodes
    nodes += 1
    lab = n.get("label") or {}
    perms = n.get("permission") or []
    navperms.update(perms)
    extra = []
    if n.get("feature"):
        extra.append(f"feature={n.get('feature')}")
    if n.get("tags"):
        extra.append("tags=" + ",".join((t.get("label") or {}).get("en", "") if isinstance(t, dict) else str(t) for t in n["tags"]))
    acts = n.get("actions") or []
    print("  " * depth + f"- [{n.get('id','')}] {lab.get('en', n.get('title'))} | {lab.get('ar','')} | url={n.get('url')} | perms={perms} {' '.join(extra)} | actions={[ (a.get('title') or {}).get('en') for a in acts]}")
    for c in n.get("children") or []:
        walk(c, depth + 1)


for n in nav:
    walk(n)
print("NODES", nodes, "distinct nav permissions", len(navperms))

groups = load(f"{B}/staff-permission-groups/demo@en/items.jsonl")
allp = {}
for g in groups:
    names = [p["name"] for p in g["permissions"]]
    print(f"GROUP {g['id']} {g['name']} ({len(names)}): {names}")
    for p in g["permissions"]:
        allp[p["name"]] = g["name"]
print("permissions in groups", len(allp))
print("nav perms not in groups", sorted(set(navperms) - set(allp)))
print("group perms not used by nav", len(set(allp) - set(navperms)))
