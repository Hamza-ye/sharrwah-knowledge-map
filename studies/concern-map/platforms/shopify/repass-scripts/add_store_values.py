# Each store's value for every entitlement or feature key that a concern's eligibility statements name,
# where the review did not already carry it (keys named by routes added in this re-pass).
# Statements are lines of structures/shopify/shop-request-details/<store>/items.jsonl at the re-pass commit,
# grouped by value, with the stores and their plans as scope.
import sys, os, json, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
A = Adder("store-values")
rows = rd(os.path.join(WORK, "reviewed-statements.tsv"))
for f in sorted(glob.glob(os.path.join(WORK, "added", "*.tsv"))):
    if not f.endswith("store-values.tsv"):
        rows += rd(f)

def keys_of(stmt):
    out = set()
    try:
        obj = json.loads(stmt[len('"eligibility":'):])
    except Exception:
        return out
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("entitlements", "features") and isinstance(v, list):
                    out.update((k, z) for z in v if isinstance(z, str))
                elif isinstance(v, (dict, list)):
                    walk(v)
        elif isinstance(o, list):
            for z in o:
                walk(z)
    walk(obj)
    return out

named = collections.defaultdict(set)
have = collections.defaultdict(set)
for r in rows:
    if r["statement"].startswith('"eligibility":'):
        named[r["concern_id"]] |= keys_of(r["statement"])
    if r["structure"] == "structures/shopify/shop-request-details":
        try:
            d = json.loads(r["statement"])
            have[r["concern_id"]].add((d["section"], d["key"]))
        except Exception:
            pass

SRD = "structures/shopify/shop-request-details"
stores = sorted(x for x in git_ls(SRD) if "." not in x)
store_lines, store_plan = {}, {}
for s in stores:
    ls = [(n, l, json.loads(l)) for n, l in enumerate(git_show(f"{SRD}/{s}/items.jsonl").splitlines(), start=1) if l.strip()]
    store_lines[s] = ls
    plan = collections.defaultdict(dict)
    for n, l, d in ls:
        if d["section"] == "plan":
            plan[d["set"]][d["key"]] = d["value"]
    store_plan[s] = plan

def plan_label(s, st):
    p = store_plan[s].get(st, {})
    bits = [str(p.get("displayName") or p.get("name") or "plan not stated")]
    if p.get("partnerDevelopment"):
        bits.append("development store")
    return f"{s} ({', '.join(bits)})"

def groups_for(kind, key):
    top = key.split(".")[0]
    groups = collections.OrderedDict()
    for s in stores:
        seen_plan = set()
        for n, l, d in store_lines[s]:
            if d["section"] == kind and d["key"] == top:
                val = json.dumps(d["value"], sort_keys=True)
                lab = plan_label(s, d["set"])
                if (val, lab) in seen_plan:
                    continue
                seen_plan.add((val, lab))
                g = groups.setdefault(val, {"first": (s, n, l), "scope": [], "cites": []})
                g["scope"].append(lab)
                g["cites"].append(osh_cite(f"{SRD}/{s}/items.jsonl", f"line {n} (set {d['set']})", l, sid="shopify/shop-request-details"))
    return groups

cache = {}
for c in sorted(named):
    for kind, key in sorted(named[c]):
        ident = f"{kind}.{key}"
        if (kind, key.split(".")[0]) in have[c]:
            continue
        have[c].add((kind, key.split(".")[0]))
        if (kind, key) not in cache:
            cache[(kind, key)] = groups_for(kind, key)
        for val, g in cache[(kind, key)].items():
            s, n, l = g["first"]
            A.add(c, "decides", SRD, ident, l, "; ".join(g["scope"]), g["cites"],
                  "value per store as the admin's RequestDetails answer states it; the route's eligibility names this key")
        if not cache[(kind, key)]:
            print("no store value held for", c, ident)
A.save()
