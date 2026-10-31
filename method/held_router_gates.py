"""The held pass, Shopify's admin router: each route's ancestors' gates on the store, from the router's own items, named
in the reading of every line of a batch that doesn't yet name them (the ruling after SH-8). Only a route's own gates are
its scope; a route nested under a gated route is reached through it, so its lines name that gate, as a menu group's
feature is named (SA-42's M6).

Usage: python3 -I method/held_router_gates.py <batch> [--apply]   (without --apply, prints what it would add)"""
import json, re, sys, csv
import os
HERE = os.path.dirname(os.path.abspath(__file__))
ROUTER = "/home/user/observed-sh/structures/shopify/admin-router/items.jsonl"
HELD = os.path.join(HERE, "..", "studies", "class-model", "held")
STORE = ("entitlements", "betas", "features", "organizationFlags", "organizationFeatures", "plans", "regions")
def cond(e):
    parts = []
    for k in STORE:
        if isinstance(e.get(k), list) and e[k]:
            parts.append(f"{k} {', '.join(map(str, e[k]))}")
    for x in e.get("excluded") or []:
        if isinstance(x, dict):
            c = cond(x)
            if c: parts.append(f"not ({c})")
    return " and ".join(parts)
def gate(e):
    if not isinstance(e, dict): return ""
    own = cond(e)
    alts = [cond(x) for x in e.get("oneOf") or [] if isinstance(x, dict)]
    alts = [a for a in alts if a]
    return "; ".join(x for x in ([own] if own else []) + (["oneOf: " + " | ".join(alts)] if alts else []))
rows = [json.loads(l) for l in open(ROUTER, encoding="utf-8")]
by = {r["id"]: r for r in rows if isinstance(r, dict) and r.get("id")}
def ancestors(rid):
    out, seen = [], set()
    p = by.get(rid, {}).get("parent")
    while p and p in by and p not in seen:
        seen.add(p); g = gate(by[p].get("eligibility"))
        if g: out.append((p, g))
        p = by[p].get("parent")
    return out
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    sys.exit(__doc__)
batch = sys.argv[1]; apply = "--apply" in sys.argv


def named(a, reading):
    """Whether the reading names the ancestor's id whole: never inside a longer id, as
    organization-settings:organizations is inside organization-settings:organizations:partner-billing (SH-15)."""
    return re.search(r"(?<![\w:.-])" + re.escape(a) + r"(?![\w:-])", reading) is not None
ents = {}
with open(f"{HELD}/shopify/entries.tsv", newline="") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE): ents[r["entry_id"]] = r
p = f"{HELD}/shopify/placements-{batch}.tsv"
L = open(p, encoding="utf-8").read().split("\n"); H = L[0].split("\t"); n = 0; routes = set()
for i, l in enumerate(L[1:], 1):
    f = dict(zip(H, l.split("\t")))
    if not f.get("entry_id"): continue
    e = ents.get(f["entry_id"].split(";")[0])
    if not e or e["structure"] != "admin-router": continue
    m = re.search(r"(?:^|; )id: ([^;]+)", e["text"])
    if not m: continue
    anc = [(a, g) for a, g in ancestors(m.group(1).strip()) if not named(a, f["reading"])]
    if not anc: continue
    routes.add(m.group(1)); n += 1
    add = "; reached under " + ", under ".join(f"{a} (its gate on the store: {g})" for a, g in anc) + \
          ", an ancestor's gate named here, as a menu group's feature is (the ruling after SH-8)"
    if apply:
        f["reading"] += add
        assert '"' not in f["reading"]
        L[i] = "\t".join(f[h] for h in H)
    elif n <= 3:
        print(f["entry_id"], m.group(1), "|", add[:300])
print(f"{n} lines of {len(routes)} routes {'updated' if apply else 'would be updated'}")
if apply: open(p, "w", encoding="utf-8").write("\n".join(L))
