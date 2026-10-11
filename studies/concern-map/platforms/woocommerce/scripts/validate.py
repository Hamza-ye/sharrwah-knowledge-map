# Structural checks on the six output files.
# Usage: python3 -I validate.py
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import cite

COLS = {
    "inventory.tsv": ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"],
    "concerns.tsv": ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"],
    "placements.tsv": ["concern_id", "placement", "value", "status", "cite_ids", "note"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
    "not-reached.tsv": ["url", "status", "needed_for", "what_to_look_for"],
}
LISTS = {"api-resources", "access-scopes", "webhook-topics", "settings", "admin-navigation", "plan-features", "legal-agreements", "extension-points"}
problems = []


def load(name):
    path = os.path.join(ROOT, name)
    lines = open(path, encoding="utf-8").read().split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    head = lines[0].split("\t")
    if head != COLS[name]:
        problems.append(f"{name}: header {head}")
    for n, l in enumerate(lines[1:], 2):
        if l.count("\t") != len(COLS[name]) - 1:
            problems.append(f"{name}:{n}: {l.count(chr(9)) + 1} fields")
        if "\r" in l:
            problems.append(f"{name}:{n}: carriage return")
    return [dict(zip(head, l.split("\t"))) for l in lines[1:]]


inv, con, pla, cit, nr = (load(n) for n in ["inventory.tsv", "concerns.tsv", "placements.tsv", "citations.tsv", "not-reached.tsv"])
cids = {r["cite_id"] for r in cit}
conids = {r["concern_id"] for r in con}
invids = {r["inv_id"] for r in inv}
if len(cids) != len(cit): problems.append("duplicate cite ids")
if len(conids) != len(con): problems.append("duplicate concern ids")
if len(invids) != len(inv): problems.append("duplicate inventory ids")
for r in inv:
    if not re.fullmatch(r"WC-I-\d{4}", r["inv_id"]): problems.append(f"bad inv id {r['inv_id']}")
    if r["list"] not in LISTS and not r["list"].startswith("other:"): problems.append(f"bad list {r['list']}")
    if r["cite_id"] not in cids: problems.append(f"{r['inv_id']}: cite {r['cite_id']} missing")
    cs = r["concern_ids"].split()
    if not cs and not r["out_of_scope_reason"]: problems.append(f"{r['inv_id']}: no concern and no reason")
    if cs and r["out_of_scope_reason"]: problems.append(f"{r['inv_id']}: both concern and reason")
    for c in cs:
        if c not in conids: problems.append(f"{r['inv_id']}: unknown concern {c}")
for r in con:
    if not re.fullmatch(r"WC-C-\d{3}", r["concern_id"]): problems.append(f"bad concern id {r['concern_id']}")
    for i in r["inv_ids"].split():
        if i not in invids: problems.append(f"{r['concern_id']}: unknown inv {i}")
seen = {}
for r in pla:
    seen.setdefault(r["concern_id"], []).append(r["placement"])
    if r["concern_id"] not in conids: problems.append(f"placement for unknown concern {r['concern_id']}")
    if r["status"] not in ("shown", "not shown"): problems.append(f"{r['concern_id']} {r['placement']}: status {r['status']}")
    if r["status"] == "shown" and (not r["value"] or not r["cite_ids"]): problems.append(f"{r['concern_id']} {r['placement']}: shown without value or cites")
    if r["status"] == "not shown" and (r["value"] or r["cite_ids"]): problems.append(f"{r['concern_id']} {r['placement']}: not shown with value or cites")
    for c in r["cite_ids"].split():
        if c not in cids: problems.append(f"{r['concern_id']}: cite {c} missing")
    if "inference" in r["note"].lower() and not re.search(r"(^|\. )Inference:", r["note"]):
        problems.append(f"{r['concern_id']} {r['placement']}: unlabelled inference")
for c in conids:
    if sorted(seen.get(c, [])) != sorted(["software", "decides", "legal", "boundary", "reason"]):
        problems.append(f"{c}: placements {seen.get(c)}")
for r in cit:
    if not re.fullmatch(r"WC-S-\d{4}", r["cite_id"]): problems.append(f"bad cite id {r['cite_id']}")
    if r["access_path"] not in ("md", "raw", "rendered", "local"): problems.append(f"{r['cite_id']}: access {r['access_path']}")
    if not re.fullmatch(r"\d{4}-\d\d-\d\d", r["source_date"]): problems.append(f"{r['cite_id']}: date {r['source_date']}")
    if not re.fullmatch(r"\d{4}-\d\d-\d\d", r["accessed"]): problems.append(f"{r['cite_id']}: accessed {r['accessed']}")
    if not (r["source"].startswith(("https://", "http://", "woocommerce-11.2.1:"))): problems.append(f"{r['cite_id']}: source {r['source']}")
    if len(r["quote"]) > 320 or "..." in r["quote"] or "…" in r["quote"]: problems.append(f"{r['cite_id']}: quote form")
used = {r["cite_id"] for r in inv} | {c for r in pla for c in r["cite_ids"].split()}
unused = sorted(cids - used)
for word in ["historical"]:
    for r in pla:
        if word in (r["status"] + r["note"]).lower(): problems.append(f"{r['concern_id']}: '{word}' in placement")
cite.check_all()
print(f"inventory {len(inv)}, concerns {len(con)}, placements {len(pla)}, citations {len(cit)} ({len(unused)} unused), not-reached {len(nr)}")
print("PROBLEMS:", len(problems))
for p in problems[:50]:
    print(" ", p)
