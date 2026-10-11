# Candidate statements for the Q1 Shopify re-pass (questions/Q1-concern-map.md, "Changed on 11 October 2026").
# Joins only on identifiers Shopify states; every statement is a verbatim excerpt of the source it cites.
#
#   router-where      concern -> its admin-router sections (first run's inventory) -> top-level routes: "path"
#   router-eligibility  ... -> each route's stated "eligibility" object, as written
#   store-values      ... -> the entitlement and feature keys those objects name -> each store's value
#                       (structures/shopify/shop-request-details), with the store's plan at that set
#   access-lines      concern -> its access scopes (first run's inventory) -> shopify.dev lines naming the scope
#   help-links        concern -> help pages its first-run citations quote -> admin links those pages state
#   first-run         concern -> the first run's shown placements -> their cited quotes, placement renamed, value dropped
#
# Usage: python3 -I q1_shopify_joins.py Q1_SHOPIFY_DIR OBSERVED_SH COMMIT CAPTURE_RUN OUT_DIR
import csv, json, os, re, subprocess, sys, collections

q1, osh, commit, capture, out = sys.argv[1:6]
os.makedirs(out, exist_ok=True)
csv.field_size_limit(10**9)

def rd(name):
    with open(os.path.join(q1, name), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def show(path):
    p = subprocess.run(["git", "-C", osh, "show", f"{commit}:{path}"], capture_output=True)
    if p.returncode:
        raise SystemExit(f"git show {commit}:{path} failed")
    return p.stdout.decode("utf-8")

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

inv, con, cit, pl = rd("inventory.tsv"), rd("concerns.tsv"), rd("citations.tsv"), rd("placements.tsv")
cite = {r["cite_id"]: r for r in cit}
inv_cites = {r["cite_id"] for r in inv}
concern_ids = {r["concern_id"] for r in con}

register = {r["structure_id"]: r for r in csv.DictReader(show("structures/REGISTER.tsv").splitlines(), delimiter="\t", quoting=csv.QUOTE_NONE)}
def seen(sid):
    return register.get(sid, {}).get("date seen", "") or "undated"

new_cites, statements = [], []
next_id = [5001]
cite_key = {}

def add_cite(path, locator, quote, sid):
    key = (path, quote)
    if key in cite_key:
        return cite_key[key]
    cid = f"SH-S-{next_id[0]:04d}"; next_id[0] += 1
    new_cites.append({"cite_id": cid, "source": f"observed-sh@{commit[:9]}:{path}", "locator": locator, "quote": quote,
                      "source_date": seen(sid), "date_basis": "observed-sh structures/REGISTER.tsv, date seen",
                      "accessed": "2026-10-11", "access_path": "local"})
    cite_key[key] = cid
    return cid

def add(concern, placement, structure, identifier, statement, scope, cids, join, note=""):
    statements.append({"concern_id": concern, "placement": placement, "structure": structure, "identifier": identifier,
                       "statement": statement, "scope": scope, "cite_ids": ";".join(cids), "note": note, "join": join})

def balanced(text, start):
    """The JSON object or array that starts at text[start], as written."""
    depth, i, in_str, esc = 0, start, False, False
    while i < len(text):
        ch = text[i]
        if in_str:
            if esc: esc = False
            elif ch == "\\": esc = True
            elif ch == '"': in_str = False
        elif ch == '"': in_str = True
        elif ch in "{[": depth += 1
        elif ch in "}]":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
        i += 1
    return None

# ---- router ----
RPATH = "structures/shopify/admin-router/items.jsonl"
router = [(n, line, json.loads(line)) for n, line in enumerate(show(RPATH).splitlines(), start=1) if line.strip()]
by_section = collections.defaultdict(list)
for n, line, it in router:
    by_section[it.get("section")].append((n, line, it))

concern_sections = collections.defaultdict(set)
for r in inv:
    if "structures/shopify/admin-router/" in cite.get(r["cite_id"], {}).get("source", ""):
        for c in ids(r["concern_ids"]):
            concern_sections[c].add(r["entry"])

def eligibility_keys(el):
    keys = set()
    if isinstance(el, dict):
        for k, v in el.items():
            if k in ("entitlements", "features") and isinstance(v, list):
                keys |= {(k, x) for x in v if isinstance(x, str)}
            elif isinstance(v, (dict, list)):
                keys |= eligibility_keys(v)
    elif isinstance(el, list):
        for x in el:
            keys |= eligibility_keys(x)
    return keys

concern_keys = collections.defaultdict(set)
for c, secs in concern_sections.items():
    seen_el = {}
    for s in sorted(secs):
        for n, line, it in by_section.get(s, []):
            if "parent" not in it and it.get("path") is not None:
                stmt = f'"path":{json.dumps(it["path"], ensure_ascii=False)}'
                if stmt in line:
                    add(c, "where", "structures/shopify/admin-router", it["id"], stmt, "",
                        [add_cite(RPATH, f"line {n} ({it['id']})", stmt, "shopify/admin-router")], "router-where",
                        f"section {s}")
            if it.get("eligibility"):
                i = line.find('"eligibility":')
                obj = balanced(line, line.find("{", i)) if i >= 0 else None
                if not obj:
                    continue
                stmt = '"eligibility":' + obj
                if stmt not in line:
                    continue
                if stmt in seen_el:
                    seen_el[stmt][1].append(it["id"])
                    continue
                cid = add_cite(RPATH, f"line {n} ({it['id']})", stmt, "shopify/admin-router")
                seen_el[stmt] = (cid, [it["id"]], s)
                concern_keys[c] |= eligibility_keys(it["eligibility"])
    for stmt, (cid, routes, s) in seen_el.items():
        note = f"section {s}" + (f"; the same eligibility on {len(routes) - 1} more route(s): {' '.join(routes[1:6])}" if len(routes) > 1 else "")
        add(c, "decides", "structures/shopify/admin-router", routes[0], stmt, "", [cid], "router-eligibility", note)

# ---- store values ----
SRD = "structures/shopify/shop-request-details"
stores = sorted(x.split("/")[-1] for x in subprocess.run(["git", "-C", osh, "ls-tree", "--name-only", f"{commit}:{SRD}"],
                                                       capture_output=True, text=True).stdout.split() if "." not in x)
store_lines, store_plan = {}, {}
for s in stores:
    lines = [(n, l, json.loads(l)) for n, l in enumerate(show(f"{SRD}/{s}/items.jsonl").splitlines(), start=1) if l.strip()]
    store_lines[s] = lines
    plan = collections.defaultdict(dict)
    for n, l, d in lines:
        if d["section"] == "plan":
            plan[d["set"]][d["key"]] = d["value"]
    store_plan[s] = plan

def plan_label(s, st):
    p = store_plan[s].get(st, {})
    bits = [str(p.get("displayName") or p.get("name") or "plan not stated")]
    if p.get("partnerDevelopment"): bits.append("development store")
    return f"{s} ({', '.join(bits)})"

for c, keys in concern_keys.items():
    for kind, key in sorted(keys):
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
                    g["cites"].append(add_cite(f"{SRD}/{s}/items.jsonl", f"line {n} (set {d['set']})", l, "shopify/shop-request-details"))
        for val, g in groups.items():
            s, n, l = g["first"]
            add(c, "decides", SRD, f"{kind}.{key}", l, "; ".join(g["scope"]), g["cites"], "store-values",
                "value per store as the admin's RequestDetails answer states it; the route's eligibility names this key")

# ---- access lines ----
DAL = "structures/shopify/dev-access-lines"
dal = []
for sub in ("shopify.dev_md", "shopify.dev_md-sitemap-delta"):
    for n, l in enumerate(show(f"{DAL}/{sub}/items.jsonl").splitlines(), start=1):
        if l.strip():
            dal.append((sub, n, json.loads(l)))
concern_scopes = collections.defaultdict(set)
for r in inv:
    if r["list"] == "access-scopes":
        for c in ids(r["concern_ids"]):
            concern_scopes[c].add(r["entry"].strip())
for c, scopes in concern_scopes.items():
    for sc in sorted(scopes):
        hits = [(sub, n, d) for sub, n, d in dal if f"`{sc}`" in d["line"]]
        distinct = collections.OrderedDict()
        for sub, n, d in hits:
            distinct.setdefault(d["line"].strip(), (sub, n, d))
        for text, (sub, n, d) in list(distinct.items())[:5]:
            placement = "decides" if re.search(r"must have .{0,80}permission", text, re.I) else "boundary"
            cid = add_cite(f"{DAL}/{sub}/items.jsonl", f"line {n} ({d['page']} > {' > '.join(d.get('headings') or [])})", text, "shopify/dev-access-lines")
            more = len(hits) - 1
            add(c, placement, DAL, sc, text, "", [cid], "access-lines",
                f"{d['page']}" + (f"; {more} more line(s) on shopify.dev name this scope" if more > 0 else ""))

# ---- help links ----
HAL = show("derived/help-admin-links.tsv").splitlines()
hal = [r for r in csv.DictReader([l for l in HAL if not l.startswith("#")], delimiter="\t", quoting=csv.QUOTE_NONE)]
links_by_page = collections.defaultdict(list)
for r in hal:
    links_by_page[r["help_page"]].append(r)
manifest = {}
with open(os.path.join(capture, "manifest.tsv"), encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        manifest[r["url"]] = r
concern_pages = collections.defaultdict(set)
for r in pl:
    for x in ids(r["cite_ids"]):
        src = cite.get(x, {}).get("source", "")
        if src.startswith("https://help.shopify.com/"):
            concern_pages[r["concern_id"]].add(src.split("#")[0])
for c, pages in concern_pages.items():
    done = set()
    for page in sorted(pages):
        m = manifest.get(page)
        if not m:
            continue
        raw = open(os.path.join(capture, m["dir"], m["primary_file"]), encoding="utf-8", errors="replace").read()
        for r in links_by_page.get(page, []):
            md = f"[{r['link_text']}]({r['address']})"
            if md not in raw or (page, r["admin_path"]) in done:
                continue
            done.add((page, r["admin_path"]))
            cid = f"WEB:{page}|{md}"
            add(c, "where", page, r["admin_path"] or r["address"], md, "", [cid], "help-links",
                f"admin route(s) {r['route_ids'] or 'not matched'}; heading {r['heading'] or '(none)'}")

# ---- first run ----
RENAME = {"software": "where", "decides": "decides", "legal": "responsible", "boundary": "boundary", "reason": "reason"}
inv_list_of_cite = {r["cite_id"]: r["list"] for r in inv}
for r in pl:
    if r["status"] != "shown":
        continue
    placement = RENAME.get(r["placement"])
    for x in ids(r["cite_ids"]):
        cr = cite.get(x)
        if not cr:
            continue
        if x in inv_cites and placement in ("decides", "responsible") and inv_list_of_cite.get(x) != "plan-features":
            continue  # a list entry only shows that the entry exists
        add(r["concern_id"], placement, cr["source"], cr["locator"], cr["quote"], "", [x], "first-run",
            "from the first run's citations; check that it answers this placement")

# ---- web citations for help links ----
for s in statements:
    if s["cite_ids"].startswith("WEB:"):
        page, md = s["cite_ids"][4:].split("|", 1)
        key = (page, md)
        if key not in cite_key:
            cid = f"SH-S-{next_id[0]:04d}"; next_id[0] += 1
            new_cites.append({"cite_id": cid, "source": page, "locator": s["identifier"], "quote": md,
                              "source_date": "undated", "date_basis": "live page, read on capture date",
                              "accessed": "2026-10-11", "access_path": "md"})
            cite_key[key] = cid
        s["cite_ids"] = cite_key[key]

cols = ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note", "join"]
with open(os.path.join(out, "candidates.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(cols) + "\n")
    for s in statements:
        f.write("\t".join(str(s[k]).replace("\t", " ").replace("\n", " ") for k in cols) + "\n")
ccols = ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"]
with open(os.path.join(out, "citations-new.tsv"), "w", encoding="utf-8") as f:
    f.write("\t".join(ccols) + "\n")
    for r in new_cites:
        f.write("\t".join(str(r[k]).replace("\t", " ").replace("\n", " ") for k in ccols) + "\n")

cov = collections.Counter((s["concern_id"], s["placement"]) for s in statements)
per = collections.Counter(s["join"] for s in statements)
covered = collections.Counter(p for (c, p) in cov)
print(f"candidates {len(statements)} by join {dict(per)}; new citations {len(new_cites)}")
print("concerns with at least one candidate, per placement:", {p: f"{covered[p]}/{len(concern_ids)}" for p in ("where", "decides", "responsible", "boundary", "reason")})
