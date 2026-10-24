# Writes the BigCommerce run's files to final/: inventory, concerns, citations, statements, gaps, not-reached.
# Usage: python3 -I build.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bcsrc, concerns, inventory, stmts, gaps
from collections import defaultdict

OUT = os.path.join(bcsrc.B, "final")
PL = ["where", "decides", "responsible", "boundary", "reason"]


def clean(s):
    return " ".join(str(s).replace("﻿", "").split())


def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            vals = [clean(r.get(h, "")) for h in header]
            f.write("\t".join(vals) + "\n")


def quote_of(text, limit=300):
    t = clean(text)
    if len(t) <= limit:
        return t
    cut = t[:limit]
    i = cut.rfind(". ")
    if i > 120:
        return cut[:i + 1]
    j = cut.rfind(" ")
    return cut[:j].rstrip(",;:")


# ---------- citations ----------
cites, cite_index = [], {}


def access_path_for(key, text):
    url, files, default, _, _ = bcsrc.resolve(key)
    if default != "rendered":
        return default
    # rendered pages: say "raw" when the text is found only in the raw HTML (hidden on the rendered page)
    first = files[0]
    if first.endswith(".txt"):
        raw = open(first, encoding="utf-8", errors="replace").read()
        tv = bcsrc.variants(raw)
        for (k, q), lvl in zip(bcsrc.variants(text), range(3)):
            if any(tk == k and q in t for tk, t in tv):
                return "rendered"
        return "raw"
    return "rendered"


def cite(key, locator, text):
    url, files, default, date, basis = bcsrc.resolve(key)
    q = quote_of(text)
    k = (url, q)
    if k in cite_index:
        return cite_index[k]
    cid = f"BC-S-{len(cites) + 1:04d}"
    cites.append(dict(cite_id=cid, source=url, locator=locator, quote=q, source_date=date, date_basis=basis,
                      accessed=bcsrc.READ, access_path=access_path_for(key, q)))
    cite_index[k] = cid
    return cid


# ---------- inventory ----------
inv_rows, by_concern = [], defaultdict(list)
for i, (lst, entry, key, loc, quote, cs, oos) in enumerate(inventory.all_lists(), start=1):
    iid = f"BC-I-{i:04d}"
    cid = cite(key, loc, quote)
    inv_rows.append(dict(inv_id=iid, list=lst, entry=entry, cite_id=cid,
                         concern_ids=", ".join(concerns.cid(c) for c in cs), out_of_scope_reason=oos))
    for c in cs:
        by_concern[c].append(iid)

con_rows = [dict(concern_id=concerns.cid(n), concern=name, platform_terms=terms, inv_ids=", ".join(by_concern[n]), split_note=note)
            for n, name, terms, note in concerns.CONCERNS]

# ---------- statements ----------
st_rows, have = [], defaultdict(set)
for s in sorted(stmts.ST, key=lambda x: (x["c"], PL.index(x["pl"]))):
    cid = cite(s["key"], s["loc"], s["text"])
    st_rows.append(dict(concern_id=concerns.cid(s["c"]), placement=s["pl"], structure=s["structure"], identifier=s["ident"],
                        statement=s["text"], scope=s["scope"], cite_ids=cid, note=s["note"]))
    have[s["c"]].add(s["pl"])

# ---------- gaps ----------
gp_rows = []
names = {n: name for n, name, _, _ in concerns.CONCERNS}
for n, name, _, _ in concerns.CONCERNS:
    for pl in PL:
        if pl in have[n]:
            continue
        what, means, who, route, why, kind = gaps.gap(n, name, pl)
        gp_rows.append(dict(concern_id=concerns.cid(n), placement=pl, what_would_show_it=what, means=means, who_can=who,
                            route=route, why_not_held=why, gap_kind=kind))

for n, pl, what, means, who, route, why, kind in gaps.EXTRA:
    gp_rows.append(dict(concern_id=concerns.cid(n), placement=pl, what_would_show_it=what, means=means, who_can=who,
                        route=route, why_not_held=why, gap_kind=kind))
gp_rows.sort(key=lambda r: (r["concern_id"], PL.index(r["placement"])))

# ---------- not reached ----------
SUP = "https://support.bigcommerce.com/s/article/"
nr = [
    dict(url="https://support.bigcommerce.com/llms.txt", status="redirected to the Help Center login page (https://support.bigcommerce.com/s/login/?language=en_US&startURL=%2Fllms.txt)",
         needed_for="the Help Center's own index of articles, listed as the Product index in https://docs.bigcommerce.com/llms.txt",
         what_to_look_for="the control panel settings sections as the Help Center names them, to build the settings list"),
    dict(url="https://support.bigcommerce.com/s/", status="HTTP 200 but renders blank: the Salesforce site's script bundles (/s/sfsites/l/.../resources.js) return HTTP 400 to headless Chromium from this session; the raw HTML is a script shell with no article text",
         needed_for="all Help Center articles (store settings, payments, shipping, tax, plans and policies)",
         what_to_look_for="the Help Center's category and article lists; a saved copy of each article below"),
    dict(url="https://security.bigcommerce.com/", status="HTTP 403: Cloudflare security verification page (\"Performing security verification\")",
         needed_for="BC-C-028, BC-C-082, BC-C-083 (Platform Trust Center: security, compliance and hosting)",
         what_to_look_for="hosting regions and data residency statements, the PCI DSS Attestation of Compliance, subprocessor and certification lists"),
]
needs = defaultdict(list)
for n, hs in gaps.H.items():
    for h in hs:
        needs[h].append(concerns.cid(n))
for h in sorted(needs):
    nr.append(dict(url=SUP + h, status="not rendered (Help Center scripts return HTTP 400 in this session); linked from BigCommerce's developer docs",
                   needed_for=", ".join(needs[h]),
                   what_to_look_for="the control panel section and route, who can turn the feature on or set it (plan, setting, staff permission), and any stated reason"))

os.makedirs(OUT, exist_ok=True)
write("inventory.tsv", ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"], inv_rows)
write("concerns.tsv", ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"], con_rows)
write("citations.tsv", ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"], cites)
write("statements.tsv", ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note"], st_rows)
write("gaps.tsv", ["concern_id", "placement", "what_would_show_it", "means", "who_can", "route", "why_not_held", "gap_kind"], gp_rows)
write("not-reached.tsv", ["url", "status", "needed_for", "what_to_look_for"], nr)
print(f"inventory {len(inv_rows)}, concerns {len(con_rows)}, citations {len(cites)}, statements {len(st_rows)}, gaps {len(gp_rows)}, not reached {len(nr)}")
cells = sum(len(v) for v in have.values())
print(f"cells with a statement {cells} of {len(con_rows) * 5}; gaps {len(gp_rows)}")
