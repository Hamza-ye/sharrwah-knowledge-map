# Build the re-pass output in ../final/ from the first run's files, the reviewed candidates and the spec.
# Usage: python3 -I build.py            write final/ (quotes of web citations must be in a capture)
#        python3 -I build.py --items    also write work/capture-items.json (new web sources, with the cite ids citing them)
# Set ALLOW_WORKING=1 to check new web quotes against working copies before they are captured.
import csv, collections, json, os, re, shutil, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import newcite, qcheck
W = os.path.dirname(HERE)
FIRST = newcite.FIRST
FINAL = os.path.join(W, "final")
os.makedirs(FINAL, exist_ok=True)
csv.field_size_limit(10**9)

def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def wr(name, cols, rows):
    with open(os.path.join(FINAL, name), "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ").strip() for c in cols) + "\n")

for part in ["spec_a", "spec_b", "spec_c", "spec_d", "spec_e", "spec_g"]:
    importlib.import_module(part)

concerns = rd(os.path.join(FIRST, "concerns.tsv"))
order = {r["concern_id"]: i for i, r in enumerate(concerns)}
P = ["where", "decides", "responsible", "boundary", "reason"]
cites_old = rd(os.path.join(FIRST, "citations.tsv"))
old_ids = {r["cite_id"] for r in cites_old}

# ---- new citations: dedupe on (source, locator, quote), ids from WC-S-5001 ----
new_cites, key2id = [], {}
def cid_for(c):
    if c.get("cite_id"):
        assert c["cite_id"] in old_ids, c["cite_id"]
        return c["cite_id"]
    k = (c["source"], c["locator"], c["quote"])
    if k not in key2id:
        key2id[k] = f"WC-S-{5001 + len(new_cites)}"
        new_cites.append({"cite_id": key2id[k], **{x: c[x] for x in ("source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path")}})
    return key2id[k]

# ---- identifiers for kept statements whose identifier was only a line locator ----
IDENT = {
    "WC-S-0603": "bacs (WC_Gateway_BACS method_description)", "WC-S-0605": "cod (WC_Gateway_COD method_description)",
    "WC-S-0606": "cheque (WC_Gateway_Cheque method_description)", "WC-S-0604": "WC_Gateway_BACS::process_payment",
    "WC-S-0607": "paypal (WC_Gateway_Paypal method_description)", "WC-S-0608": "WC_Gateway_Paypal::should_load",
    "WC-S-0616": "DefaultPaymentGateways", "WC-S-0618": "PaymentsExtensionSuggestions::$country_extensions",
    "WC-S-0619": "PaymentsExtensionSuggestions::$country_extensions", "WC-S-0621": "PaymentsController (Payments menu item)",
    "WC-S-0597": "license.txt: 15. Disclaimer of Warranty", "WC-S-0600": "woocommerce_allowed_countries",
    "WC-S-0932": "rate_limit_checkout", "WC-S-0609": "WC_Tracker::$api_url", "WC-S-0610": "WC_Tracks_Client::PIXEL",
    "WC-S-0611": "RemoteLogger::LOG_ENDPOINT", "WC-S-0936": "remote_logging", "WC-S-0622": "analytics",
    "WC-S-0929": "personal_data_retention", "WC-S-0602": "woocommerce_default_customer_address",
    "WC-S-0615": "WC_Integration_MaxMind_Database_Service (database download URL)", "WC-S-0612": "WC_Geolocation IP lookup services: ipify",
    "WC-S-0613": "WC_Geolocation IP lookup services: ipinfo.io", "WC-S-0598": "woocommerce_currency", "WC-S-0601": "woocommerce_calc_taxes",
    "WC-S-0599": "store_address", "WC-S-0439": "WC_Shipping_Method", "WC-S-0950": "woocommerce_review_rating_verification_required",
    "WC-S-0928": "woocommerce_enable_guest_checkout", "WC-S-0931": "X-WC-Webhook-Signature", "WC-S-0941": "wc/store",
    "WC-S-0935": "order_attribution", "WC-S-0937": "point_of_sale", "WC-S-0939": "push_notifications",
    "WC-S-0934": "order_withdrawal", "WC-S-0938": "fulfillments", "WC-S-0940": "cost_of_goods_sold",
}
_readme = open(os.path.join(newcite.WOO, "readme.txt"), encoding="utf-8").read().split("\n")
def readme_heading(line):
    for i in range(line - 1, -1, -1):
        m = re.match(r"^=+\s*(.+?)\s*=+\s*$", _readme[i])
        if m:
            return m.group(1)
    return ""
def better_identifier(r):
    if not re.match(r"^lines? \d", r["identifier"]):
        return r["identifier"]
    cid = r["cite_ids"].split()[0]
    if cid in IDENT:
        return IDENT[cid]
    if r["structure"].endswith(":readme.txt"):
        ln = int(re.match(r"^lines? (\d+)", r["identifier"]).group(1))
        h = readme_heading(ln)
        return f"readme.txt: {h}" if ln > 1 and h and h != "WooCommerce" else "readme.txt: header"
    raise SystemExit(f"no identifier for {r['concern_id']} {r['placement']} {cid} {r['identifier']}")

# ---- statements ----
st_rows = []
for r in rd(os.path.join(W, "work", "kept.tsv")):
    st_rows.append({"concern_id": r["concern_id"], "placement": r["placement"], "structure": r["structure"], "identifier": better_identifier(r),
                    "statement": r["statement"], "scope": r["scope"], "cite_ids": r["cite_ids"], "note": r["note"], "_src": 0, "_row": int(r["row"])})
seen = {(r["concern_id"], r["placement"], r["cite_ids"].split()[0]) for r in st_rows}
for i, s in enumerate(newcite.STATEMENTS):
    cid = cid_for(s["cite"])
    more = [cid_for(m) for m in s["more"]]
    key = (s["concern_id"], s["placement"], cid)
    if key in seen:
        continue
    seen.add(key)
    st_rows.append({"concern_id": s["concern_id"], "placement": s["placement"], "structure": s["cite"]["source"], "identifier": s["identifier"],
                    "statement": s["cite"]["quote"], "scope": s["scope"], "cite_ids": " ".join([cid] + more), "note": s["note"], "_src": 1, "_row": i})
st_rows.sort(key=lambda r: (order[r["concern_id"]], P.index(r["placement"]), r["_src"], r["_row"]))

# ---- gaps ----
gp_rows = sorted(newcite.GAPS, key=lambda g: (order[g["concern_id"]], P.index(g["placement"])))

# ---- checks ----
problems = []
allcites = {r["cite_id"]: r for r in cites_old}
allcites.update({r["cite_id"]: r for r in new_cites})
for r in st_rows:
    first = r["cite_ids"].split()[0]
    src = allcites[first]["source"]
    res = qcheck.check(r["statement"], src)
    if not res.startswith("found"):
        problems.append(f"statement not found ({res}): {r['concern_id']} {r['placement']} {first} {r['statement'][:80]}")
for c in new_cites:
    res = qcheck.check(c["quote"], c["source"])
    if not res.startswith("found"):
        problems.append(f"new citation not found ({res}): {c['cite_id']} {c['source']} {c['quote'][:80]}")
cover = collections.Counter((r["concern_id"], r["placement"]) for r in st_rows)
gcover = collections.Counter((g["concern_id"], g["placement"]) for g in gp_rows)
for c in order:
    for p in P:
        if not cover[(c, p)] and not gcover[(c, p)]:
            problems.append(f"cell with neither statement nor gap: {c} {p}")
        if cover[(c, p)] and gcover[(c, p)]:
            problems.append(f"cell with both statement and gap: {c} {p}")

# ---- write ----
for name in ("inventory.tsv", "concerns.tsv", "placements.tsv"):
    shutil.copyfile(os.path.join(FIRST, name), os.path.join(FINAL, name))
CC = ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"]
wr("citations.tsv", CC, cites_old + new_cites)
wr("statements.tsv", ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note"], st_rows)
wr("gaps.tsv", ["concern_id", "placement", "what_would_show_it", "means", "who_can", "route", "why_not_held", "gap_kind"], gp_rows)
log = rd(os.path.join(W, "work", "review-log.tsv"))
wr("review-log.tsv", ["concern_id", "placement", "statement_start", "cite_ids", "action", "reason", "candidate_row"],
   [{**r, "candidate_row": r["row"]} for r in log])
nr = rd(os.path.join(FIRST, "not-reached.tsv"))
extra_nr = os.path.join(W, "work", "not-reached-new.tsv")
if os.path.exists(extra_nr):
    nr += rd(extra_nr)
wr("not-reached.tsv", ["url", "status", "needed_for", "what_to_look_for"], nr)

if "--items" in sys.argv:
    cited = collections.defaultdict(list)
    for c in new_cites:
        # only web sources that no capture holds yet (the follow-up capture adds to the earlier ones)
        if c["source"].startswith("http") and c["source"].split("#")[0] not in qcheck.MANIFEST:
            cited[c["source"].split("#")[0]].append(c["cite_id"])
    items = [{"n": n, "url": u, "kind": "web", "cited_in": ids} for n, (u, ids) in enumerate(sorted(cited.items()), start=1)]
    json.dump(items, open(os.path.join(W, "work", "capture-items.json"), "w"), indent=0)
    print("capture items:", len(items))

pc = collections.Counter(r["placement"] for r in st_rows)
cells = {p: sum(1 for c in order if cover[(c, p)]) for p in P}
print(f"statements {len(st_rows)} (kept {sum(1 for r in st_rows if r['_src'] == 0)}, new {sum(1 for r in st_rows if r['_src'] == 1)}); by placement {dict(pc)}")
print(f"cells with a statement {cells}; gaps {len(gp_rows)}; new citations {len(new_cites)}; citations {len(cites_old) + len(new_cites)}")
print("problems:", len(problems))
for x in problems[:40]:
    print("  ", x)
