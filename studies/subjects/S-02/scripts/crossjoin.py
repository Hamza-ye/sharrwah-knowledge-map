"""Measure how many names match across platforms after plain normalization (lowercase, singular, no separators)."""
import json
import re
from collections import Counter

SH = "/home/user/observed-sh/structures/shopify"
SA = "/home/user/observed-sa/structures/salla"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def norm(s):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    words = []
    for w in s.split():
        if w.endswith("ies") and len(w) > 4:
            w = w[:-3] + "y"
        elif w.endswith("ses") and len(w) > 4:
            w = w[:-2]
        elif w.endswith("s") and not w.endswith("ss") and len(w) > 3:
            w = w[:-1]
        words.append(w)
    return " ".join(words)


def report(name, a, b):
    na = {norm(x): x for x in a}
    nb = {norm(x): x for x in b}
    both = sorted(set(na) & set(nb))
    print(f"== {name}: shopify {len(na)} names, salla {len(nb)} names, exact after normalization {len(both)}")
    print("   matched:", [f"{na[k]}={nb[k]}" for k in both])
    print("   shopify only (first 40):", sorted(na[k] for k in set(na) - set(nb))[:40])
    print("   salla only (first 40):", sorted(nb[k] for k in set(nb) - set(na))[:40])


# 1. events: resource part
schema = {t["name"]: t for t in load(f"{SH}/admin-graphql-schema/2026-10/items.jsonl")}
topics = [e["name"] for e in schema["WebhookSubscriptionTopic"]["enumValues"]]
verbs = {"CREATE", "UPDATE", "DELETE", "CANCELLED", "CREATED", "UPDATED", "DELETED", "EDITED", "FULFILLED", "PAID",
         "ADD", "REMOVE", "DISABLE", "ENABLE", "ACTIVATE", "DEACTIVATE", "PUBLISH", "DESTROY", "CONNECT", "DISCONNECT",
         "ADDED", "REMOVED", "REQUEST", "APPROVE", "PROCESS", "DECLINE", "CANCEL", "CLOSE", "REOPEN", "SUCCESS", "FAILURE",
         "MERGE", "DUE", "FINISH", "FIRST", "LAST", "UNINSTALLED", "REVOKE", "SKIP", "UNSKIP", "PAUSE", "FAIL", "EXPIRE",
         "SPLIT", "MERGED", "MOVED", "RESCHEDULED", "COMPLETE", "READY", "SUBMITTED", "ACCEPTED", "REJECTED"}
sh_ev = set()
for t in topics:
    parts = t.split("_")
    while len(parts) > 1 and parts[-1] in verbs:
        parts = parts[:-1]
    sh_ev.add(parts[0] if parts[0] in ("ORDERS", "PRODUCTS", "CUSTOMERS", "CARTS", "CHECKOUTS", "COLLECTIONS", "THEMES", "LOCATIONS", "MARKETS", "DISCOUNTS", "DOMAINS", "REFUNDS", "RETURNS", "SHOP", "APP", "COMPANIES", "DISPUTES", "SEGMENTS", "LOCALES", "PROFILES", "METAOBJECTS", "ROLLOUTS") else "_".join(parts))
sa_ev = set()
for p in [f"{SA}/dashboard-webhook-events/demo@en/items.jsonl"]:
    for r in load(p):
        sa_ev.add(r["event"].split(".")[0])
for r in load(f"{SA}/docs-event-lists/webhooks/items.jsonl"):
    m = re.search(r"`([A-Za-z_\.]+)`", r["cells"].get("Name", ""))
    if m:
        sa_ev.add(m.group(1).split(".")[0])
for r in load(f"{SA}/docs-event-lists/partner-apis.app-events/items.jsonl"):
    m = re.search(r"`([A-Za-z_\.]+)`", r["cells"].get("Event Name", ""))
    if m:
        sa_ev.add(m.group(1).split(".")[0])
report("event resources (Shopify WebhookSubscriptionTopic 2026-10 vs Salla dashboard+docs+app events)", sh_ev, sa_ev)

# 2. API groups
gnav = [c["label"] for c in load(f"{SH}/admin-graphql-reference-nav/shopify.dev@latest/items.jsonl")]
ops = load(f"{SA}/docs-operations/md-openapi/items.jsonl")
tags = set()
for o in ops:
    d = o["document"]["paths"][o["path"]][o["method"]]
    t = (d.get("tags") or ["?"])[-1].split("/")[-1]
    tags.add(t)
report("API groups (Shopify GraphQL reference nav categories vs Salla operation tags)", gnav, tags)

# 3. GraphQL object names vs Salla operation tags (resource nouns)
objs = [k for k, v in schema.items() if v["kind"] == "OBJECT" and not re.search(r"(Edge|Connection|Payload|UserError)$", k)]
report("resource types (Shopify GraphQL OBJECT types vs Salla operation tags)", objs, tags)

# 4. nav labels
shnav = [r["text"] for r in load(f"{SH}/admin-main-nav/demo-fake-dev-store@settings-organization-account/items.jsonl") if r.get("href")]
shset = [r["title"] for r in load(f"{SH}/admin-settings-nav/ibx5bt-xy/items.jsonl")]
sanav = [r["text"] for r in load(f"{SA}/dashboard-main-navigation/merchant@en/items.jsonl") if r.get("kind") in ("link", "text")]
saset = [r["text"] for r in load(f"{SA}/dashboard-settings-menu/merchant@en/items.jsonl")]
report("navigation labels (Shopify main+settings nav vs Salla main nav+settings menu, English)", shnav + shset, sanav + saset)

# 5. permission handles
tree = [r["id"] for r in load(f"{SH}/admin-permission-tree/use-store-options-f948ecd551d0/items.jsonl")]
groups = load(f"{SA}/staff-permission-groups/demo@en/items.jsonl")
saperm = [p["name"] for g in groups for p in g["permissions"]]
report("permission handles (Shopify permission tree ids vs Salla permission names)", tree, saperm)
