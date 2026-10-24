# Candidate statements for the Q1 Salla and WooCommerce re-passes (questions/Q1-concern-map.md, "Changed on 11 October 2026").
# Every candidate reuses a first-run citation whose quote is already checked, so every statement is a verbatim excerpt.
#
#   list-entry   each inventory entry's own citation, under the placement its list answers (rule 2 of the change):
#                lists of locations -> where; lists of APIs, events, scopes and extension targets -> boundary;
#                lists that themselves state availability or control (plan lines, feature flags, permissions,
#                suggestions per country) -> decides. Lists of names only (agreement titles, countries) give none.
#   first-run    the first run's shown placements -> their cited quotes, placement renamed, value dropped
#
# Usage: python3 -I q1_list_joins.py Q1_PLATFORM_DIR salla|woocommerce OUT_DIR
import csv, json, os, re, sys, collections

q1, platform, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
csv.field_size_limit(10**9)

def rd(name):
    with open(os.path.join(q1, name), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

COMMON = {"api-resources": "boundary", "access-scopes": "boundary", "webhook-topics": "boundary",
          "admin-navigation": "where", "settings": "where", "plan-features": "decides"}
RULES = {
    "salla": {**COMMON,
              "other:dashboard-features": "decides", "other:staff-permissions": "decides",
              "other:partner-access-permissions": "decides", "other:dashboard-apps": "where", "other:order-statuses": "where"},
    "woocommerce": {**COMMON, "extension-points": "boundary",
                    "other:marketplace-categories": "where", "other:payment-extension-suggestions": "decides",
                    "other:features": "decides", "other:emails": "where", "other:onboarding-tasks": "where",
                    "other:privacy-exporters-erasers": "boundary", "other:order-statuses": "where",
                    "other:shipping-partner-suggestions": "decides", "other:core-payment-gateways": "where",
                    "other:core-shipping-methods": "where"},
}[platform]

def placement_for(entry_list, source):
    if platform == "salla" and entry_list == "extension-points":
        m = re.search(r"structures/salla/([^/]+)/", source)
        s = m.group(1) if m else ""
        return "boundary" if s in ("docs-event-lists", "twilight-components") else "where"
    if platform == "woocommerce" and entry_list == "access-scopes":
        return "decides" if "class-wc-install" in source else "boundary"   # roles and capabilities vs REST API key access
    if platform == "woocommerce" and entry_list == "extension-points" and "includes/gateways" in source:
        return "where"
    return RULES.get(entry_list)

def scope_of(quote):
    """Plans and countries a Salla dashboard feature names, as written in its own item."""
    try:
        v = json.loads(quote.strip().rstrip(",")).get("value", {})
    except Exception:
        return ""
    bits = []
    if isinstance(v, dict):
        if v.get("plans"): bits.append("plans: " + ", ".join(map(str, v["plans"])))
        if v.get("countries"): bits.append("countries: " + ", ".join(map(str, v["countries"])))
    return "; ".join(bits)

inv, con, cit, pl = rd("inventory.tsv"), rd("concerns.tsv"), rd("citations.tsv"), rd("placements.tsv")
cite = {r["cite_id"]: r for r in cit}
inv_cites = {r["cite_id"] for r in inv}
inv_list_of_cite = {r["cite_id"]: r["list"] for r in inv}
STATING_LISTS = {k for k, v in RULES.items() if v == "decides"}

rows, seen = [], set()
def add(c, placement, cr, identifier, scope, join, note):
    key = (c, placement, cr["cite_id"])
    if key in seen:
        return
    seen.add(key)
    rows.append({"concern_id": c, "placement": placement, "structure": cr["source"], "identifier": identifier,
                 "statement": cr["quote"], "scope": scope, "cite_ids": cr["cite_id"], "note": note, "join": join})

for r in inv:
    cr = cite.get(r["cite_id"])
    if not cr:
        continue
    p = placement_for(r["list"], cr["source"])
    if not p:
        continue
    scope = scope_of(cr["quote"]) if r["list"] == "other:dashboard-features" else ""
    for c in ids(r["concern_ids"]):
        add(c, p, cr, r["entry"], scope, "list-entry", f"list {r['list']}")

RENAME = {"software": "where", "decides": "decides", "legal": "responsible", "boundary": "boundary", "reason": "reason"}
for r in pl:
    if r["status"] != "shown":
        continue
    p = RENAME.get(r["placement"])
    for x in ids(r["cite_ids"]):
        cr = cite.get(x)
        if not cr:
            continue
        if x in inv_cites and p in ("decides", "responsible") and inv_list_of_cite.get(x) not in STATING_LISTS:
            continue  # a list entry only shows that the entry exists
        add(r["concern_id"], p, cr, cr["locator"] or cr["source"], "", "first-run",
            "from the first run's citations; check that it answers this placement")

cols = ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note", "join"]
with open(os.path.join(out, "candidates.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(cols) + "\n")
    for s in rows:
        f.write("\t".join(str(s[k]).replace("\t", " ").replace("\n", " ") for k in cols) + "\n")
concern_ids = {r["concern_id"] for r in con}
cov = collections.Counter((s["concern_id"], s["placement"]) for s in rows)
covered = collections.Counter(p for (c, p) in cov)
print(f"{platform}: candidates {len(rows)} by join {dict(collections.Counter(s['join'] for s in rows))}")
print("concerns with at least one candidate, per placement:",
      {p: f"{covered[p]}/{len(concern_ids)}" for p in ("where", "decides", "responsible", "boundary", "reason")})
