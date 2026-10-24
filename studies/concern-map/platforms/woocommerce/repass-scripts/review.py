# Apply the review to every candidate: list-entry rules (by list) and the one-by-one first-run decisions
# (work/dec_fr.tsv). Writes work/kept.tsv (statements kept or moved) and work/review-log.tsv (every move or drop).
# Usage: python3 -I review.py WORKDIR
import csv, os, sys, collections
csv.field_size_limit(10**9)
W = sys.argv[1]
def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
cands = rd(os.path.join(W, "candidates.tsv"))
dec_fr = {int(r["row"]): r for r in rd(os.path.join(W, "work", "dec_fr.tsv"))}

# list-entry rules: what each list is, and so what its entries answer on their own
LOCATION = {"settings", "admin-navigation", "other:marketplace-categories", "other:emails", "other:onboarding-tasks",
            "other:core-payment-gateways", "other:core-shipping-methods"}
BOUNDARY = {"api-resources", "webhook-topics", "extension-points", "other:privacy-exporters-erasers"}
REASONS = {
    "other:order-statuses": "A list of order status values, not a location or boundary structure; the entry shows only that the status exists.",
    "other:features": "A feature's name only; it states no default and no one who switches it. The feature's definition (enabled_by_default, disable_ui) is added as a new decides statement.",
    "other:payment-extension-suggestions": "A suggestion's id constant only; it states no country or condition. The per-country lists in the same file are added as new decides statements.",
    "other:shipping-partner-suggestions": "A partner's name only; it states no condition. Its is_visible country rule is added as a new decides statement.",
    "access-scopes:install": "A bare role or capability token; it states no permission rule. The code that assigns capabilities and the capability each admin page requires are added as new decides statements.",
}
OVERRIDES = {  # row -> (action, to, reason)
    567: ("move", "boundary", "A base class that payment gateways extend: an extension point (its list is extension-points), which answers how it meets the rest, not where it lives."),
    568: ("move", "boundary", "A base class that payment gateways extend: an extension point (its list is extension-points), which answers how it meets the rest, not where it lives."),
    589: ("drop", "", "A heading of the REST API reference ('Introduction'), not an API resource."),
}
kept, log = [], []
def logit(row, r, action, reason):
    log.append({"row": row, "concern_id": r["concern_id"], "placement": r["placement"],
                "statement_start": r["statement"][:80], "cite_ids": r["cite_ids"], "action": action, "reason": reason})

for i, r in enumerate(cands, start=2):
    if r["join"] == "list-entry":
        lst = r["note"].replace("list ", "", 1)
        if lst == "access-scopes":
            lst = "access-scopes:install" if r["placement"] == "decides" else "access-scopes:keys"
        if i in OVERRIDES:
            act, to, why = OVERRIDES[i]
        elif lst in LOCATION and r["placement"] == "where":
            act, to, why = "keep", "", ""
        elif (lst in BOUNDARY or lst == "access-scopes:keys") and r["placement"] == "boundary":
            act, to, why = "keep", "", ""
        elif lst in REASONS:
            act, to, why = "drop", "", REASONS[lst]
        else:
            raise SystemExit(f"no rule for row {i} list {lst} placement {r['placement']}")
        scope, note = "", f"Entry of the list {'access-scopes' if lst.startswith('access-scopes') else lst}."
    else:
        d = dec_fr[i]
        act, to, why, scope, note = d["action"], d["to"], d["reason"], d["scope"], d["note"]
    if act == "drop":
        logit(i, r, "drop", why); continue
    p = r["placement"]
    if act == "move":
        p = to
    elif act != "keep":
        raise SystemExit(f"bad action {act} row {i}")
    kept.append({"row": i, "concern_id": r["concern_id"], "placement": p, "structure": r["structure"],
                 "identifier": r["identifier"], "statement": r["statement"], "scope": scope or r["scope"],
                 "cite_ids": r["cite_ids"], "note": note, "join": r["join"], "act": act, "why": why, "from": r["placement"]})

# duplicates: same concern, placement and first citation -> keep the first, log the rest as dropped
seen, out = {}, []
for k in kept:
    key = (k["concern_id"], k["placement"], k["cite_ids"].split()[0])
    r0 = cands[k["row"] - 2]
    if key in seen:
        prev = seen[key]
        lead = f"Answers {k['placement']}: {k['why']} " if k["act"] == "move" else ""
        logit(k["row"], r0, "drop", f"{lead}Duplicate of row {prev}: the same citation is already kept for this concern under {k['placement']}.")
        continue
    seen[key] = k["row"]
    if k["act"] == "move":
        logit(k["row"], r0, f"move to {k['placement']}", k["why"])
    out.append(k)

cols = ["row", "concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note", "join"]
with open(os.path.join(W, "work", "kept.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(cols) + "\n")
    for k in out:
        f.write("\t".join(str(k[c]).replace("\t", " ").replace("\n", " ") for c in cols) + "\n")
lcols = ["row", "concern_id", "placement", "statement_start", "cite_ids", "action", "reason"]
with open(os.path.join(W, "work", "review-log.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(lcols) + "\n")
    for l in sorted(log, key=lambda x: (x["row"], x["action"])):
        f.write("\t".join(str(l[c]).replace("\t", " ").replace("\n", " ") for c in lcols) + "\n")
acts = collections.Counter(l["action"].split(" to ")[0] for l in log)
print(f"candidates {len(cands)}; kept statements {len(out)}; log rows {len(log)} {dict(acts)}")
print("kept by placement", dict(collections.Counter(k["placement"] for k in out)))
