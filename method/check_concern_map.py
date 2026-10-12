# Checks a concern-map run (questions/Q1-concern-map.md): the six files per platform, ids and
# references, placement values, and every quote against its source.
#
# Usage: python3 -I check_concern_map.py RUN_DIR OUT_DIR [CAPTURE_RUN_DIR ...]
#   RUN_DIR          holds one folder per platform (shopify/, salla/, woocommerce/) with the six files
#   OUT_DIR          receives <platform>-issues.tsv, <platform>-quotes.tsv, urls-to-capture.json, summary.txt
#   CAPTURE_RUN_DIR  capture runs (method/capture) whose manifest.tsv holds the cited web pages
#
# Local sources resolve through these roots (override with environment variables):
#   observed-sh@<commit>:<path>         git show in $OBSERVED_SH (default /home/user/observed-sh)
#   observed-sa@<commit>:<path>         git show in $OBSERVED_SA (default /home/user/observed-sa)
#   woocommerce-11.2.1:<path>           $WOO_RELEASE (default /home/user/woocommerce-release/11.2.1/woocommerce)
#   sharrwah-knowledge-map:<path>       $SKM (default: this repository)
import csv, html, json, os, re, subprocess, sys, unicodedata
import collections
from collections import Counter, defaultdict

csv.field_size_limit(10**9)
RUN, OUT = sys.argv[1], sys.argv[2]
CAPTURES = sys.argv[3:]
os.makedirs(OUT, exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOTS = {
    "observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
    "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa"),
    "woocommerce-11.2.1": os.environ.get("WOO_RELEASE", "/home/user/woocommerce-release/11.2.1/woocommerce"),
    "sharrwah-knowledge-map": os.environ.get("SKM", os.path.dirname(HERE)),
}
sys.path.insert(0, HERE)
from held_index import CORPORA, Held, describe, names_a_source, urls_in
HELD = Held(ROOTS, CAPTURES)
PLATFORMS = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
HEADERS = {
    "inventory.tsv": ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"],
    "concerns.tsv": ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"],
    "placements.tsv": ["concern_id", "placement", "value", "status", "cite_ids", "note"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
    "not-reached.tsv": ["url", "status", "needed_for", "what_to_look_for"],
}
NEW_HEADERS = {  # the reshaped placement step (questions/Q1-concern-map.md, "Changed on 11 October 2026")
    "statements.tsv": ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note"],
    "gaps.tsv": ["concern_id", "placement", "what_would_show_it", "means", "who_can", "route", "why_not_held", "gap_kind"],
}
GAP_KINDS = {"page not read", "observation needed", "searched, not found", "stated only in general terms"}
NEW_PLACEMENTS = ["where", "decides", "responsible", "boundary", "reason"]
WHO_CAN = {"agent", "founder", "either"}
LISTS = {"api-resources", "access-scopes", "webhook-topics", "settings", "admin-navigation", "plan-features",
         "legal-agreements", "extension-points"}
PLACEMENTS = ["software", "decides", "legal", "boundary", "reason"]
STATUSES = {"shown", "not shown"}
ACCESS = {"md", "raw", "rendered", "local"}
PARTIES = {  # more than one of these in one value suggests the concern has parts placed differently
    "decides": {"platform at build": r"platform at build|at build", "operator": r"\boperator\b", "merchant": r"\bmerchant",
                "buyer": r"\bbuyer|\bcustomer", "outside rules": r"outside rules|\blaw\b|regulat", "app developer": r"app developer|developer"},
    "legal": {"platform company": r"platform company", "separate entity": r"separate entity", "partner": r"\bpartner",
              "app developer": r"app developer", "merchant": r"\bmerchant", "buyer": r"\bbuyer"},
    "software": {"core": r"\bcore\b", "separate service": r"separate service|product line",
                 "extension point": r"extension point|\bapp\b|function|provider slot", "outside": r"outside the platform"},
}
VOCAB = {  # key words of the agreed values; anything else must start with "other:"
    "software": ["core", "separate service", "product line", "extension point", "outside the platform"],
    "decides": ["platform at build", "operator", "merchant", "buyer", "outside rules"],
    "legal": ["platform company", "separate entity", "partner", "app developer", "merchant", "buyer"],
}

def read_tsv(path, name):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        rows = list(r)
    if not rows:
        return None, [], [f"{name}: empty file"]
    head, body, issues = rows[0], rows[1:], []
    expected = HEADERS.get(name) or NEW_HEADERS[name]
    if head[:len(expected)] != expected:
        issues.append(f"{name}: header is {head}, expected {expected}")
    recs = []
    for i, row in enumerate(body, start=2):
        if not any(c.strip() for c in row):
            continue
        if len(row) != len(head):
            issues.append(f"{name}:{i}: {len(row)} fields, header has {len(head)}")
        recs.append({"_line": i, **{h: (row[k].strip() if k < len(row) else "") for k, h in enumerate(head)}})
    return head, recs, issues

def split_ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

# ---------- quotes: the shared verbatim check in method/quote_check.py ----------
from quote_check import Sources
check_quote = Sources(ROOTS, CAPTURES).check_quote

# ---------- per platform ----------
summary = []
urls = defaultdict(set)
for plat, pfx in PLATFORMS.items():
    d = os.path.join(RUN, plat)
    issues = []
    if not os.path.isdir(d):
        summary.append(f"{plat}: no output folder")
        continue
    data = {}
    for name in HEADERS:
        p = os.path.join(d, name)
        if not os.path.exists(p):
            if name == "placements.tsv" and os.path.exists(os.path.join(d, "statements.tsv")):
                data[name] = []   # platforms that started from the reshaped step have no first-run placements
                continue
            issues.append(("error", name, "", "file missing"))
            data[name] = []
            continue
        _, recs, iss = read_tsv(p, name)
        issues += [("error", name, "", x) for x in iss]
        data[name] = recs
    if not os.path.exists(os.path.join(d, "notes.md")):
        issues.append(("error", "notes.md", "", "file missing"))
    inv, con, pla, cit = (data[n] for n in ("inventory.tsv", "concerns.tsv", "placements.tsv", "citations.tsv"))

    def ids(recs, key, kind):
        seen = Counter(r[key] for r in recs)
        for k, n in seen.items():
            if n > 1:
                issues.append(("error", kind, k, f"id used {n} times"))
            if not re.match(rf"^{pfx}-[A-Z]+-\d+$", k):
                issues.append(("warning", kind, k, f"id does not follow {pfx}-<letter>-<number>"))
        return set(seen)

    inv_ids, con_ids, cit_ids = ids(inv, "inv_id", "inventory"), ids(con, "concern_id", "concerns"), ids(cit, "cite_id", "citations")
    used_cites = set()

    for r in inv:
        if not (r["list"] in LISTS or r["list"].startswith("other:")):
            issues.append(("error", "inventory", r["inv_id"], f"list '{r['list']}' is not one of the agreed lists or other:<name>"))
        if not r["entry"]:
            issues.append(("error", "inventory", r["inv_id"], "entry is empty"))
        if r["cite_id"] not in cit_ids:
            issues.append(("error", "inventory", r["inv_id"], f"cite_id '{r['cite_id']}' not in citations"))
        used_cites.add(r["cite_id"])
        cids = split_ids(r["concern_ids"])
        for c in cids:
            if c not in con_ids:
                issues.append(("error", "inventory", r["inv_id"], f"concern '{c}' not in concerns"))
        if not cids and not r["out_of_scope_reason"]:
            issues.append(("error", "inventory", r["inv_id"], "no concern and no out-of-scope reason"))
        if cids and r["out_of_scope_reason"]:
            issues.append(("warning", "inventory", r["inv_id"], "has concerns and an out-of-scope reason"))

    inv_to_con = {r["inv_id"]: set(split_ids(r["concern_ids"])) for r in inv}
    for r in con:
        if not r["concern"]:
            issues.append(("error", "concerns", r["concern_id"], "concern is empty"))
        for i in split_ids(r["inv_ids"]):
            if i not in inv_ids:
                issues.append(("error", "concerns", r["concern_id"], f"inventory entry '{i}' not in inventory"))
            elif r["concern_id"] not in inv_to_con.get(i, set()):
                issues.append(("warning", "concerns", r["concern_id"], f"lists '{i}', but that entry doesn't list this concern"))
        if not split_ids(r["inv_ids"]):
            if r["split_note"].startswith("Not in the platform's lists:"):
                issues.append(("review", "concerns", r["concern_id"], "not in the platform's lists; " + r["split_note"][28:].strip()[:160]))
            else:
                issues.append(("error", "concerns", r["concern_id"], "no inventory entries, and split_note doesn't start with \"Not in the platform's lists:\""))

    per = defaultdict(list)
    for r in pla:
        per[(r["concern_id"], r["placement"])].append(r)
        key = f"{r['concern_id']}/{r['placement']}"
        if r["concern_id"] not in con_ids:
            issues.append(("error", "placements", key, "concern not in concerns"))
        if r["placement"] not in PLACEMENTS:
            issues.append(("error", "placements", key, f"placement '{r['placement']}' is not one of {PLACEMENTS}"))
        if r["status"] not in STATUSES:
            issues.append(("error", "placements", key, f"status '{r['status']}' is not shown or not shown"))
        cs = split_ids(r["cite_ids"])
        for c in cs:
            if c not in cit_ids:
                issues.append(("error", "placements", key, f"cite_id '{c}' not in citations"))
            used_cites.add(c)
        if r["status"] == "shown" and not cs:
            issues.append(("error", "placements", key, "shown without a citation"))
        if r["status"] == "shown" and r["placement"] in VOCAB and not r["value"].startswith("other:"):
            v = r["value"].lower()
            if not any(k in v for k in VOCAB[r["placement"]]):
                issues.append(("warning", "placements", key, f"value '{r['value'][:80]}' matches no agreed value and doesn't start with other:"))
            named = [k for k, rx in PARTIES[r["placement"]].items() if re.search(rx, v)]
            if len(named) > 1:
                issues.append(("review", "placements", key, f"value names {', '.join(named)}: split the concern if its parts sit with different parties"))
    repass = os.path.exists(os.path.join(d, "statements.tsv")) or os.path.exists(os.path.join(d, "gaps.tsv"))
    for c in con_ids:
        for p in PLACEMENTS:
            rows = per.get((c, p), [])
            if repass:
                continue  # placements.tsv is a record of the first run once the re-pass exists
            if not rows:
                issues.append(("error", "placements", f"{c}/{p}", "no row for this placement"))
            elif len([x for x in rows if x["status"] == "shown"]) > 1:
                issues.append(("review", "placements", f"{c}/{p}", f"{len(rows)} rows: sources differ or the concern needs splitting"))

    st_path, gp_path = os.path.join(d, "statements.tsv"), os.path.join(d, "gaps.tsv")
    if os.path.exists(st_path) or os.path.exists(gp_path):
        st = read_tsv(st_path, "statements.tsv")[1] if os.path.exists(st_path) else []
        gp = read_tsv(gp_path, "gaps.tsv")[1] if os.path.exists(gp_path) else []
        cover = collections.defaultdict(lambda: [0, 0])
        cit_src = {x["cite_id"]: x["source"] for x in cit}
        for r in st:
            key = f"{r['concern_id']}/{r['placement']}"
            if r["concern_id"] not in con_ids:
                issues.append(("error", "statements", key, "concern not in concerns"))
            if r["placement"] not in NEW_PLACEMENTS:
                issues.append(("error", "statements", key, f"placement '{r['placement']}' is not one of {NEW_PLACEMENTS}"))
            if not r["statement"] or not r["identifier"]:
                issues.append(("error", "statements", key, "statement or identifier is empty"))
            cs = split_ids(r["cite_ids"])
            if not cs:
                issues.append(("error", "statements", key, "no citation"))
            for c in cs:
                if c not in cit_ids:
                    issues.append(("error", "statements", key, f"cite_id '{c}' not in citations"))
                used_cites.add(c)
            if cs and cs[0] in cit_ids and r["statement"]:
                src = cit_src[cs[0]]
                res, why, share = check_quote(r["statement"], src)
                if not res.startswith("found"):
                    issues.append(("error", "statements", key, f"statement not found verbatim in {cs[0]}'s source ({res}{'; ' + why if why else ''})"))
            cover[(r["concern_id"], r["placement"])][0] += 1
        for r in gp:
            key = f"{r['concern_id']}/{r['placement']}"
            if r["concern_id"] not in con_ids:
                issues.append(("error", "gaps", key, "concern not in concerns"))
            if r["placement"] not in NEW_PLACEMENTS:
                issues.append(("error", "gaps", key, f"placement '{r['placement']}' is not one of {NEW_PLACEMENTS}"))
            if r["who_can"] not in WHO_CAN:
                issues.append(("error", "gaps", key, f"who_can '{r['who_can']}' is not agent, founder or either"))
            if r.get("gap_kind", "") not in GAP_KINDS:
                issues.append(("error", "gaps", key, f"gap_kind '{r.get('gap_kind', '')}' is not one of {sorted(GAP_KINDS)}"))
            for col in ("what_would_show_it", "means", "route", "why_not_held"):
                if not r[col]:
                    issues.append(("error", "gaps", key, f"{col} is empty"))
            # PLAN.md section 6, Evidence (agreed 12 October 2026)
            said = r["route"] + " " + r["why_not_held"]
            if r.get("gap_kind") == "searched, not found":
                if not names_a_source(said):
                    issues.append(("error", "gaps", key, "a 'searched, not found' must name what it read"))
                if plat in CORPORA and CORPORA[plat][0] not in said:
                    issues.append(("error", "gaps", key, f"the held corpus {CORPORA[plat][1]} was not searched"))
            if r["who_can"] in ("founder", "either") and r["means"] != "commit the held archive" and \
                    ("save a page from a browser" in r["means"] or r.get("gap_kind") == "page not read"):
                for u in urls_in(r["route"]):
                    held = [h for h in HELD.lookup(u) if h["readable"]]
                    if held:
                        issues.append(("error", "gaps", key, f"{u} is held at {describe(held[0])}: route it to an agent"))
            cover[(r["concern_id"], r["placement"])][1] += 1
        for c in con_ids:
            for p in NEW_PLACEMENTS:
                n_st, n_gp = cover.get((c, p), [0, 0])
                if not n_st and not n_gp:
                    issues.append(("error", "coverage", f"{c}/{p}", "no statement and no gap"))
        summary.append(f"{plat} re-pass: statements {len(st)}, gaps {len(gp)}; concern x placement cells with a statement: "
                       f"{sum(1 for v in cover.values() if v[0])} of {len(con_ids) * len(NEW_PLACEMENTS)}")
    quotes = []
    for r in cit:
        cid = r["cite_id"]
        if not r["source"]:
            issues.append(("error", "citations", cid, "source is empty"))
        if not r["quote"]:
            issues.append(("error", "citations", cid, "quote is empty"))
        if "..." in r["quote"] or "…" in r["quote"]:
            issues.append(("warning", "citations", cid, "quote contains an ellipsis"))
        if len(r["quote"]) > 400:
            issues.append(("warning", "citations", cid, f"quote is {len(r['quote'])} characters"))
        if r["access_path"] not in ACCESS:
            issues.append(("error", "citations", cid, f"access_path '{r['access_path']}' is not md, raw, rendered or local"))
        if not r["source_date"]:
            issues.append(("error", "citations", cid, "source_date is empty"))
        if not r["accessed"]:
            issues.append(("warning", "citations", cid, "accessed is empty"))
        if cid not in used_cites:
            issues.append(("warning", "citations", cid, "not used by any inventory entry, placement or statement"))
        if re.match(r"^https?://", r["source"]):
            urls[r["source"].split("#")[0]].add(cid)
        result, why, share = check_quote(r["quote"], r["source"]) if r["quote"] and r["source"] else ("unresolved", "no quote or source", "")
        quotes.append((cid, result, why, share, r["source"], r["quote"][:200]))

    with open(os.path.join(OUT, f"{plat}-issues.tsv"), "w", encoding="utf-8") as f:
        f.write("level\tfile\tid\tissue\n")
        for lv, fl, i, x in issues:
            f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in (lv, fl, i, x)) + "\n")
    with open(os.path.join(OUT, f"{plat}-quotes.tsv"), "w", encoding="utf-8") as f:
        f.write("cite_id\tresult\twhy\tshare_of_6-word_runs_found\tsource\tquote_start\n")
        for q in quotes:
            f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in q) + "\n")
    lv = Counter(x[0] for x in issues)
    qr = Counter(q[1].split(" (")[0] for q in quotes)
    summary.append(f"{plat}: inventory {len(inv)}, concerns {len(con)}, placements {len(pla)}, citations {len(cit)}, "
                   f"not reached {len(data['not-reached.tsv'])} | issues: {dict(lv)} | quotes: {dict(qr)}")

items = [{"n": n, "url": u, "kind": "web", "cited_in": sorted(c)} for n, (u, c) in enumerate(sorted(urls.items()), start=1)]
json.dump(items, open(os.path.join(OUT, "urls-to-capture.json"), "w"), ensure_ascii=False, indent=0)
summary.append(f"web sources cited: {len(items)} unique URLs")
open(os.path.join(OUT, "summary.txt"), "w").write("\n".join(summary) + "\n")
print("\n".join(summary))
