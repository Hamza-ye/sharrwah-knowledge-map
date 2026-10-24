# Build inventory.tsv, concerns.tsv and placements.tsv from the inventory JSON and the concern specs.
# Usage: python3 -I build.py
import csv, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import spec
import concerns_a, concerns_b, concerns_c  # noqa: F401  (they register concerns)
from oos import OOS

keys = json.load(open(os.path.join(HERE, "out", "cite_keys.json")))
with open(os.path.join(ROOT, "citations.tsv"), encoding="utf-8") as f:
    cite_ids = {r["cite_id"] for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}


def clean(s):
    return re.sub(r"[\t\r\n]+", " ", str(s)).strip()


def resolve(refs):
    out = []
    for r in refs:
        if isinstance(r, spec.I):
            out += r.ids()
        elif isinstance(r, str) and r.startswith("WC-S-"):
            out.append(r)
        elif isinstance(r, str):
            if r not in keys:
                raise KeyError(f"unknown citation key {r}")
            out.append(keys[r])
        else:
            raise TypeError(r)
    for c in out:
        if c not in cite_ids:
            raise KeyError(f"cite id {c} not in citations.tsv")
    return list(dict.fromkeys(out))


inv = spec.inventory()
inv_concerns = {r["inv_id"]: [] for r in inv}
concern_invs = {}
for c in spec.CONCERNS:
    ids = []
    for rule in c["match"]:
        lst, ent = rule[0], rule[1]
        note_rx = rule[2] if len(rule) > 2 else None
        hit = [r["inv_id"] for r in inv if re.search(lst, r["list"]) and re.search(ent, r["entry"])
               and (note_rx is None or re.search(note_rx, r.get("note", "")))]
        if not hit:
            raise LookupError(f"{c['id']}: match rule matched nothing: {rule}")
        ids += hit
    ids = list(dict.fromkeys(ids))
    concern_invs[c["id"]] = ids
    for i in ids:
        inv_concerns[i].append(c["id"])

# out-of-scope reasons for rows without a concern
missing = []
for r in inv:
    r["oos"] = ""
    if not inv_concerns[r["inv_id"]]:
        for lst, ent, reason in OOS:
            if re.search(lst, r["list"]) and re.search(ent, r["entry"]):
                r["oos"] = reason
                break
        if not r["oos"]:
            missing.append(r)
if missing:
    for r in missing[:40]:
        print("UNPLACED", r["inv_id"], r["list"], r["entry"])
    raise SystemExit(f"{len(missing)} inventory rows have neither a concern nor an out-of-scope reason")

with open(os.path.join(ROOT, "inventory.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"]) + "\n")
    for r in inv:
        f.write("\t".join(clean(x) for x in [r["inv_id"], r["list"], r["entry"], r["cite_id"], " ".join(inv_concerns[r["inv_id"]]), r["oos"]]) + "\n")

with open(os.path.join(ROOT, "concerns.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(["concern_id", "concern", "platform_terms", "inv_ids", "split_note"]) + "\n")
    for c in spec.CONCERNS:
        f.write("\t".join(clean(x) for x in [c["id"], c["concern"], c["terms"], " ".join(concern_invs[c["id"]]), c["split_note"]]) + "\n")

with open(os.path.join(ROOT, "placements.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(["concern_id", "placement", "value", "status", "cite_ids", "note"]) + "\n")
    for c in spec.CONCERNS:
        for name in ["software", "decides", "legal", "boundary", "reason"]:
            p = c["placements"][name]
            ids = resolve(p["refs"]) if p["status"] == "shown" else []
            if p["status"] == "shown" and not ids:
                raise ValueError(f"{c['id']} {name}: shown without citations")
            if p["status"] == "not shown" and p["value"]:
                raise ValueError(f"{c['id']} {name}: not shown with a value")
            if p["note"].lower().startswith("inference") is False and "inference" in p["note"].lower() and not re.search(r"(^|\. )Inference:", p["note"]):
                raise ValueError(f"{c['id']} {name}: inference not labelled at the start of a sentence")
            f.write("\t".join(clean(x) for x in [c["id"], name, p["value"], p["status"], " ".join(ids), p["note"]]) + "\n")

from collections import Counter
print(len(inv), "inventory rows;", sum(1 for r in inv if r["oos"]), "out of scope;", len(spec.CONCERNS), "concerns;", len(spec.CONCERNS) * 5, "placements")
print(Counter((n, c["placements"][n]["status"]) for c in spec.CONCERNS for n in c["placements"]))
