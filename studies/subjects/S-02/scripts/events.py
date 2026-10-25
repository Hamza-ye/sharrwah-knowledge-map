"""Events on both platforms: prefixes, overlaps between lists."""
import json
import re
from collections import Counter

SA = "/home/user/observed-sa/structures/salla"
SH = "/home/user/observed-sh/structures/shopify"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


dash = load(f"{SA}/dashboard-webhook-events/demo@en/items.jsonl")
dash2 = load(f"{SA}/dashboard-webhook-events/real-merchant@en/items.jsonl")
dn = [e["event"] for e in dash]
print("SALLA dashboard events", len(dn), "real-merchant same list:", dn == [e["event"] for e in dash2])
print(" prefixes:", Counter(e.split(".")[0] for e in dn))
print(" ", dn)
docs = load(f"{SA}/docs-event-lists/webhooks/items.jsonl")
docn = []
for r in docs:
    m = re.search(r"`([a-z_\.]+)`", r["cells"].get("Name", ""))
    docn.append(m.group(1) if m else r["cells"].get("Name"))
print("SALLA docs webhooks list", len(docn), "tables:", Counter(r["headings"][-1] for r in docs))
print(" dashboard - docs:", sorted(set(dn) - set(docn)))
print(" docs - dashboard:", sorted(set(docn) - set(dn)))

adm = load(f"{SH}/admin-webhook-topics/fake-demo-sharrwah/items.jsonl")
an = [r["item"]["topic"] for r in adm]
schema = {t["name"]: t for t in load(f"{SH}/admin-graphql-schema/2026-10/items.jsonl")}
en = [e["name"] for e in schema["WebhookSubscriptionTopic"]["enumValues"]]
print("SHOPIFY admin topics", len(an), "schema enum (2026-10)", len(en))
print(" admin - enum:", sorted(set(an) - set(en)))


def pref(t):
    # resource part: drop the last verb segment
    return t.rsplit("_", 1)[0]


print(" admin topic resources:", Counter(pref(t) for t in an))
print(" ", an)
