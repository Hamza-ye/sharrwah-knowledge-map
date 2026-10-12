# Checks a subject's files (PLAN.md Stages 2 and 4) against its briefs in studies/subjects/<id>/briefs/:
# phase A per platform (statements, terms, gaps, citations), phase B (variation points, variants), phase C
# (analysis), step 2 (Yemen marks) and step 3 (rows), as far as they exist. It checks files and columns, ids and
# the ids each file cites, and that every statement and quote is found verbatim in its cited source. It also lists
# the cited URLs that need capturing.
#
# Usage: python3 -I method/check_subject.py SUBJECT_DIR OUT [CAPTURE_RUN ...]
import csv, json, os, re, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources

subj, OUT = sys.argv[1].rstrip("/"), sys.argv[2]
CAPTURES = sys.argv[3:]
os.makedirs(OUT, exist_ok=True)
SID = os.path.basename(subj).replace("-", "")          # S-01 -> S01
HERE = os.path.dirname(os.path.abspath(__file__))
SKM = os.path.dirname(HERE)
ROOTS = {"observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
         "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa"),
         "woocommerce-11.2.1": os.environ.get("WOO_RELEASE", "/home/user/woocommerce-release/11.2.1/woocommerce"),
         "sharrwah-knowledge-map": SKM}
SRC = Sources(ROOTS, CAPTURES)
PLATFORMS = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
PLACEMENTS = {"where", "decides", "responsible", "boundary", "reason"}
GAP_KINDS = {"page not read", "observation needed", "searched, not found", "stated only in general terms"}
ACCESS = {"md", "raw", "rendered", "local"}
BASES = {"term", "identifiers", "definition", "answers"}
KINDS = {"observed", "shipped", "stated", "official page"}
CAUSES = {"market, named rule", "market, pattern", "vendor choice", "maturity", "business model", "unknown"}
MARKS = {"carried unchanged", "carried with configuration", "carried only with a partner", "no placement", "unknown"}
HEAD = {
    "statements.tsv": ["stmt_id", "placement", "identifier", "statement", "scope", "cite_ids", "from", "note"],
    "terms.tsv": ["term", "definition", "cite_ids"],
    "gaps.tsv": ["gap_id", "what_is_missing", "read", "gap_kind", "who_can", "route"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
    "variation-points.tsv": ["vp_id", "question", "raised_by", "note"],
    "variants.tsv": ["vp_id", "platform", "variant", "stmt_ids", "basis", "kind", "scope", "gap_ids", "note"],
    "analysis.tsv": ["vp_id", "cause", "cause_basis", "cause_reading", "coexistence", "coexistence_basis",
                     "general_variant", "follows", "expensive_because", "founder_item", "note"],
    "yemen-marks.tsv": ["vp_id", "case_id", "mark", "variant_used", "condition_stmt_ids", "case_evidence",
                        "product_gap", "moves", "what_would_show_it", "note"],
    "rows.tsv": ["row_id", "touches", "vp_ids", "who_answers", "when", "time_bombs", "basis", "what_would_settle_it", "note"],
}
issues, quotes, urls = [], [], defaultdict(set)

def err(f, i, x, level="error"):
    issues.append((level, f, i, x))

def read(path, name, check_head=True):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows:
        err(name, "", "empty file")
        return []
    head = rows[0]
    if check_head and head != HEAD[os.path.basename(name)]:
        err(name, "", f"header is {head}, expected {HEAD[os.path.basename(name)]}")
    out = []
    for n, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            continue
        if len(row) != len(head):
            err(name, f"line {n}", f"{len(row)} fields, header has {len(head)}")
        out.append({h: (row[k].strip() if k < len(row) else "") for k, h in enumerate(head)})
    return out

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

def unique(name, recs, key, pat):
    for k, n in Counter(r[key] for r in recs).items():
        if n > 1:
            err(name, k, f"id used {n} times")
    for r in recs:
        if not re.match(pat, r[key]):
            err(name, r[key], f"id doesn't match {pat}")

# ---------- phase A, per platform ----------
stmts, gaps, terms_of = {}, {}, {}
for plat, code in PLATFORMS.items():
    d = os.path.join(subj, plat)
    if not os.path.isdir(d):
        continue
    pre = f"{SID}-{code}"
    st = read(os.path.join(d, "statements.tsv"), f"{plat}/statements.tsv") or []
    tm = read(os.path.join(d, "terms.tsv"), f"{plat}/terms.tsv") or []
    gp = read(os.path.join(d, "gaps.tsv"), f"{plat}/gaps.tsv") or []
    ct = read(os.path.join(d, "citations.tsv"), f"{plat}/citations.tsv") or []
    unique(f"{plat}/statements.tsv", st, "stmt_id", rf"^{pre}-\d{{3}}$")
    unique(f"{plat}/gaps.tsv", gp, "gap_id", rf"^{pre}-G\d{{2}}$")
    unique(f"{plat}/citations.tsv", ct, "cite_id", rf"^{pre}-C\d{{3,4}}$")
    if not os.path.exists(os.path.join(d, "notes.md")):
        err(f"{plat}/notes.md", "", "file missing")
    cit = {c["cite_id"]: c for c in ct}
    index = os.path.join(SKM, "studies/concern-map/platforms", plat, "concerns.tsv")
    concerns = {r["concern_id"] for r in (read(index, "concerns.tsv", False) or [])} if os.path.exists(index) else set()
    used = set()
    for r in st:
        sid = r["stmt_id"]
        stmts[sid] = dict(r, platform=plat)
        if r["placement"] not in PLACEMENTS:
            err(f"{plat}/statements.tsv", sid, f"placement '{r['placement']}' is not one of {sorted(PLACEMENTS)}")
        if not r["statement"]:
            err(f"{plat}/statements.tsv", sid, "statement is empty")
        frm = r["from"]
        if frm != "new" and not (frm.startswith("index:") and frm[6:] in concerns):
            err(f"{plat}/statements.tsv", sid, f"from '{frm}' is neither 'new' nor index:<a concern of the Q1 index>")
        cs = ids(r["cite_ids"])
        if not cs:
            err(f"{plat}/statements.tsv", sid, "no citation")
        for c in cs:
            used.add(c)
            if c not in cit:
                err(f"{plat}/statements.tsv", sid, f"cite_id {c} not in citations")
        if cs and cs[0] in cit and r["statement"]:
            res, why, share = SRC.check_quote(r["statement"], cit[cs[0]]["source"])
            if not res.startswith("found"):
                err(f"{plat}/statements.tsv", sid, f"statement not found verbatim in {cs[0]}'s source ({res}{'; ' + why if why else ''})")
    for t in tm:
        for c in ids(t["cite_ids"]):
            used.add(c)
            if c not in cit:
                err(f"{plat}/terms.tsv", t["term"][:30], f"cite_id {c} not in citations")
        if not ids(t["cite_ids"]):
            err(f"{plat}/terms.tsv", t["term"][:30], "no citation")
    terms_of[plat] = tm
    for g in gp:
        gaps[g["gap_id"]] = dict(g, platform=plat)
        if g["gap_kind"] not in GAP_KINDS:
            err(f"{plat}/gaps.tsv", g["gap_id"], f"gap_kind '{g['gap_kind']}' is not one of {sorted(GAP_KINDS)}")
        if g["who_can"] not in ("agent", "founder"):
            err(f"{plat}/gaps.tsv", g["gap_id"], f"who_can '{g['who_can']}' is not agent or founder")
        if not g["read"]:
            err(f"{plat}/gaps.tsv", g["gap_id"], "read is empty: list each path or URL read")
    for c in ct:
        cid, src = c["cite_id"], c["source"]
        if c["access_path"] not in ACCESS:
            err(f"{plat}/citations.tsv", cid, f"access_path '{c['access_path']}' is not one of {sorted(ACCESS)}")
        if re.match(r"^(observed-sh|observed-sa)(?!@[0-9a-f]{7,40}:)", src):
            err(f"{plat}/citations.tsv", cid, "a local source names its repository at a commit")
        if "..." in c["quote"] or "…" in c["quote"]:
            err(f"{plat}/citations.tsv", cid, "quote contains an ellipsis")
        if len(c["quote"]) > 300:
            err(f"{plat}/citations.tsv", cid, f"quote is {len(c['quote'])} characters; the brief allows 300")
        for col in ("source_date", "date_basis", "accessed"):
            if not c[col]:
                err(f"{plat}/citations.tsv", cid, f"{col} is empty")
        if cid not in used:
            err(f"{plat}/citations.tsv", cid, "not used by any statement or term", "warning")
        if re.match(r"^https?://", src):
            urls[src.split("#")[0]].add(cid)
        res, why, share = SRC.check_quote(c["quote"], src) if c["quote"] and src else ("unresolved", "no quote or source", "")
        if not res.startswith("found"):
            err(f"{plat}/citations.tsv", cid, f"quote {res}{'; ' + why if why else ''}",
                "error" if res == "not found" or not re.match(r"^https?://", src) else "pending capture")
        quotes.append((cid, res, why, share, src, c["quote"][:200]))

# ---------- phase B ----------
vps = read(os.path.join(subj, "variation-points.tsv"), "variation-points.tsv")
var = read(os.path.join(subj, "variants.tsv"), "variants.tsv")
vp_ids = set()
if vps is not None:
    unique("variation-points.tsv", vps, "vp_id", rf"^{SID}-VP-\d{{2}}$")
    vp_ids = {v["vp_id"] for v in vps}
    if len(vps) > 25:
        err("variation-points.tsv", "", f"{len(vps)} variation points: the brief says stop and report past 25")
    for v in vps:
        if not re.match(r"(?i)^(who|what)\b", v["question"]):
            err("variation-points.tsv", v["vp_id"], "the question doesn't take the form 'who or what fills X'", "warning")
        if not ids(v["raised_by"]):
            err("variation-points.tsv", v["vp_id"], "raised_by is empty")
        for s in ids(v["raised_by"]):
            if s not in stmts:
                err("variation-points.tsv", v["vp_id"], f"raised_by {s} is not a statement")
if var is not None:
    seen = set()
    for r in var:
        key = f"{r['vp_id']}/{r['platform']}"
        seen.add((r["vp_id"], r["platform"]))
        if r["vp_id"] not in vp_ids:
            err("variants.tsv", key, "vp_id not in variation-points.tsv")
        if r["platform"] not in PLATFORMS:
            err("variants.tsv", key, "platform is not one of the five")
        if r["variant"] == "gap":
            if not ids(r["gap_ids"]):
                err("variants.tsv", key, "a gap variant names its gap_ids")
            for g in ids(r["gap_ids"]):
                if gaps.get(g, {}).get("platform") != r["platform"]:
                    err("variants.tsv", key, f"gap {g} is not one of {r['platform']}'s gaps")
        elif r["variant"] != "not covered":
            if r["basis"] not in BASES:
                err("variants.tsv", key, f"basis '{r['basis']}' is not one of {sorted(BASES)}")
            for k in [x.strip() for x in r["kind"].split(";") if x.strip()] or [""]:
                if k not in KINDS:
                    err("variants.tsv", key, f"kind '{k}' is not one of {sorted(KINDS)}")
            if not ids(r["stmt_ids"]):
                err("variants.tsv", key, "no stmt_ids")
            for s in ids(r["stmt_ids"]):
                if stmts.get(s, {}).get("platform") != r["platform"]:
                    err("variants.tsv", key, f"{s} is not one of {r['platform']}'s statements")
    for v in vp_ids:
        for p in PLATFORMS:
            if os.path.isdir(os.path.join(subj, p)) and (v, p) not in seen:
                err("variants.tsv", f"{v}/{p}", "no row for this variation point and platform")
    placed = {s for r in var for s in ids(r["stmt_ids"])}
    unplaced = [s for s in stmts if s not in placed]
    if unplaced:
        err("variants.tsv", "", f"{len(unplaced)} phase A statements are under no variation point: {', '.join(unplaced[:12])}", "review")

# ---------- phase C ----------
ana = read(os.path.join(subj, "analysis.tsv"), "analysis.tsv")
founder_items = []
if ana is not None:
    for k, n in Counter(r["vp_id"] for r in ana).items():
        if n > 1:
            err("analysis.tsv", k, f"{n} rows for one variation point")
    for v in vp_ids - {r["vp_id"] for r in ana}:
        err("analysis.tsv", v, "no analysis row")
    for r in ana:
        v = r["vp_id"]
        if r["cause"] not in CAUSES:
            err("analysis.tsv", v, f"cause '{r['cause']}' is not one of {sorted(CAUSES)}")
        if r["cause"] != "unknown" and not r["cause_reading"].startswith("Reading:"):
            err("analysis.tsv", v, "cause_reading doesn't start with 'Reading:'")
        for col in ("cause_basis", "coexistence_basis"):
            for s in ids(r[col]):
                if s not in stmts:
                    err("analysis.tsv", v, f"{col} {s} is not a statement")
        co = r["coexistence"]
        if not (co in ("A", "B", "C", "D") or all(re.match(r"^\s*\w+\s*=\s*[ABCD]\s*$", x) for x in co.split(";") if x.strip())):
            err("analysis.tsv", v, f"coexistence '{co}' is not A–D, or per platform as 'shopify=B; salla=D'")
        if bool(r["founder_item"]) != ("founder" in r["follows"]):
            err("analysis.tsv", v, "a founder_item is given exactly when what follows is a decision for the founder")
        if r["founder_item"]:
            founder_items.append((v, r["founder_item"]))

# ---------- step 2: Yemen marks ----------
marks = read(os.path.join(subj, "yemen-marks.tsv"), "yemen-marks.tsv")
if marks is not None:
    yc = os.path.join(SKM, "studies/yemen-cases")
    cases = {r["case_id"] for r in (read(os.path.join(yc, "cases.tsv"), "yemen-cases/cases.tsv", False) or [])} \
        if os.path.exists(os.path.join(yc, "cases.tsv")) else set()
    ye = set()
    for name, key in (("axes.tsv", "axis_id"), ("constants.tsv", "constant_id"), ("citations.tsv", "cite_id")):
        p = os.path.join(yc, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8", newline="") as f:
                ye |= {r[key] for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}
    for r in marks:
        key = f"{r['vp_id']}/{r['case_id']}"
        if r["vp_id"] not in vp_ids:
            err("yemen-marks.tsv", key, "vp_id not in variation-points.tsv")
        if r["case_id"] not in cases:
            err("yemen-marks.tsv", key, "case_id not in studies/yemen-cases/cases.tsv")
        if r["mark"] not in MARKS:
            err("yemen-marks.tsv", key, f"mark '{r['mark']}' is not one of {sorted(MARKS)}")
        if r["mark"] != "unknown":
            if not ids(r["condition_stmt_ids"]) or not ids(r["case_evidence"]):
                err("yemen-marks.tsv", key, "a mark other than unknown cites both the variant's condition and the case's evidence")
            for s in ids(r["condition_stmt_ids"]):
                if s not in stmts:
                    err("yemen-marks.tsv", key, f"condition {s} is not a statement")
            for y in ids(r["case_evidence"]):
                if y not in ye:
                    err("yemen-marks.tsv", key, f"case evidence {y} is not a Stage 1 id")
        elif not r["what_would_show_it"]:
            err("yemen-marks.tsv", key, "an unknown mark says what would show it")
        if r["mark"] == "no placement" and not r["product_gap"]:
            err("yemen-marks.tsv", key, "no placement is written as a product gap")
        if re.search(r"(?i)yemen|اليمن|يمني", r["product_gap"]):
            err("yemen-marks.tsv", key, "the product gap names Yemen")
    have = {(r["vp_id"], r["case_id"]) for r in marks}
    for v in vp_ids:
        for c in cases:
            if (v, c) not in have:
                err("yemen-marks.tsv", f"{v}/{c}", "no mark for this variation point and case")

# ---------- step 3: rows ----------
rows = read(os.path.join(subj, "rows.tsv"), "rows.tsv")
if rows is not None:
    for r in rows:
        rid = r["row_id"]
        if r["touches"] not in ("yes", "no", "unclear"):
            err("rows.tsv", rid, f"touches '{r['touches']}' is not yes, no or unclear")
        if r["touches"] == "yes":
            if not ids(r["vp_ids"]):
                err("rows.tsv", rid, "a row that touches the subject names its variation points")
            for v in ids(r["vp_ids"]):
                if v not in vp_ids:
                    err("rows.tsv", rid, f"{v} is not a variation point")
            if r["when"] not in ("before build", "before release", "later"):
                err("rows.tsv", rid, f"when '{r['when']}' is not before build, before release or later")
        if r["touches"] == "unclear" and not r["what_would_settle_it"]:
            err("rows.tsv", rid, "an unclear row says what would settle it")
        for t in [x.strip() for x in r["time_bombs"].split(";") if x.strip()]:
            if t not in ("bundles", "wrong party", "wrong time", "market fact"):
                err("rows.tsv", rid, f"time bomb '{t}' is not one of Q3's four types")

# ---------- output ----------
with open(os.path.join(OUT, "subject-issues.tsv"), "w", encoding="utf-8") as f:
    f.write("level\tfile\tid\tissue\n")
    for row in issues:
        f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in row) + "\n")
with open(os.path.join(OUT, "subject-quotes.tsv"), "w", encoding="utf-8") as f:
    f.write("cite_id\tresult\twhy\tshare_of_6-word_runs_found\tsource\tquote_start\n")
    for q in quotes:
        f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in q) + "\n")
items = [{"n": n, "url": u, "kind": "web", "cited_in": sorted(c)} for n, (u, c) in enumerate(sorted(urls.items()), start=1)]
json.dump(items, open(os.path.join(OUT, "urls-to-capture.json"), "w"), ensure_ascii=False, indent=0)
print(f"statements {len(stmts)}, gaps {len(gaps)}, variation points {len(vp_ids)}, founder items {len(founder_items)} | "
      f"issues: {dict(Counter(i[0] for i in issues))} | quotes: {dict(Counter(q[1].split(' (')[0] for q in quotes))} | "
      f"web sources to capture: {len(items)}")
