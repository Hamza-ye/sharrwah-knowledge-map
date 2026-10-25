"""Rough keyword probe: how many entries per structure family mention an area's key terms."""
import json
import re

SH = "/home/user/observed-sh/structures/shopify"
SA = "/home/user/observed-sa/structures/salla"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


routes = load(f"{SH}/admin-router/items.jsonl")
sh_route_txt = [" ".join(str(r.get(k) or "") for k in ("id", "section", "resource", "_p")) + " " + str(r.get("path") or "") for r in routes]
tree = load(f"{SH}/admin-permission-tree/use-store-options-f948ecd551d0/items.jsonl")
sh_perm_txt = [t["id"] + " " + str(t.get("title")) for t in tree]
schema = {t["name"]: t for t in load(f"{SH}/admin-graphql-schema/2026-10/items.jsonl")}
sh_topic_txt = [e["name"] for e in schema["WebhookSubscriptionTopic"]["enumValues"]]
sh_ops_txt = [f["name"] for f in schema["QueryRoot"]["fields"]] + [f["name"] for f in schema["Mutation"]["fields"]]

sa_nav_txt = []


def walk(n):
    lab = n.get("label") or {}
    sa_nav_txt.append(f"{lab.get('en','')} {n.get('url','')} {' '.join(n.get('permission') or [])}")
    for c in n.get("children") or []:
        walk(c)


for n in load(f"{SA}/dashboard-nav/prod/items.jsonl"):
    walk(n)
sa_nav_txt += [f"{r.get('text','')} {r.get('href','')}" for r in load(f"{SA}/dashboard-main-navigation/merchant@en/items.jsonl")]
sa_nav_txt += [f"{r.get('text','')} {r.get('href','')}" for r in load(f"{SA}/dashboard-settings-menu/merchant@en/items.jsonl")]
sa_perm_txt = [p["name"] for g in load(f"{SA}/staff-permission-groups/demo@en/items.jsonl") for p in g["permissions"]]
sa_ops_txt = []
for o in load(f"{SA}/docs-operations/md-openapi/items.jsonl"):
    d = o["document"]["paths"][o["path"]][o["method"]]
    sa_ops_txt.append(f"{o['path']} {d.get('summary','')} {' '.join(d.get('tags') or [])}")
sa_ev_txt = [r["event"] for r in load(f"{SA}/dashboard-webhook-events/demo@en/items.jsonl")]
sa_ev_txt += [json.dumps(r.get("cells") or {}) for r in load(f"{SA}/docs-event-lists/webhooks/items.jsonl")]

probes = {
    "A-03 plan|billing|subscri(be|ption).*plan": r"(?i)\bplan\b|billing|plan[-_ ]",
    "A-13 capital|loan|financ|credit card|banking": r"(?i)capital|loan|financing|shopify[-_ ]?credit|banking",
    "A-16 countr|region|unsupported": r"(?i)countr|unsupported",
    "A-17 prohibit|restricted business|sanction": r"(?i)prohibit|sanction|restricted[-_ ]business",
    "A-18 kyc|verification|business certificate": r"(?i)kyc|verif|business[-_ ]certificate|identity",
    "A-19 terms|legal entity|agreement": r"(?i)\bterms\b|legal[-_ ]?entit|agreement|contract(?!s_)",
    "A-20 privacy|personal data|gdpr|erase": r"(?i)privacy|erase|personal[-_ ]data|gdpr|redact",
    "A-26 partner|expert|merchant services": r"(?i)partner|expert",
    "A-29 mobile app|app builder|app maker": r"(?i)mobile|app[-_ ]builder|app[-_ ]maker",
    "A-34 donat|charit": r"(?i)donat|charit",
}
fams = {
    "SH routes": sh_route_txt, "SH perms": sh_perm_txt, "SH topics": sh_topic_txt, "SH gql ops": sh_ops_txt,
    "SA nav": sa_nav_txt, "SA perms": sa_perm_txt, "SA ops": sa_ops_txt, "SA events": sa_ev_txt,
}
for name, pat in probes.items():
    rx = re.compile(pat)
    counts = {f: sum(1 for t in txts if rx.search(t)) for f, txts in fams.items()}
    ex_sa = [t for t in sa_nav_txt + sa_perm_txt + sa_ops_txt if rx.search(t)][:4]
    print(f"{name}: {counts} | SA e.g. {ex_sa}")
