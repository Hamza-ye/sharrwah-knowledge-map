# Checks a subject's files (PLAN.md Stages 2 and 4) against its briefs in studies/subjects/<id>/briefs/:
# phase A per platform (statements, terms, absences, gaps, citations), phase A2 (a2.tsv), phase B (variation
# points, variants), phase C (analysis), step 2 (Yemen marks) and step 3 (rows), as far as they exist.
# It checks files and columns, ids and every id a file cites, that statements and quotes are verbatim in their
# sources, that a variant is an excerpt of its statements, that copied index citations are unchanged, and that no
# gap goes to the founder for a page that is held. It writes the subject's kinds.tsv (each statement's kind, by
# rule: method/source_kinds.py) and lists the cited URLs that need capturing.
#
# Usage: python3 -I method/check_subject.py SUBJECT_DIR OUT [CAPTURE_RUN ...]
import csv, glob, json, os, re, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources, variants as text_variants
from source_kinds import kind_of
from held_index import Held, describe, names_a_source, urls_in

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
HELD = Held(ROOTS, sorted(glob.glob(os.path.join(SKM, "evidence/product-class/runs/*"))) + CAPTURES)
PLATFORMS = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
BULLETS = {"a", "b", "c", "d", "e", "end-payment", "end-payout"}
GAP_BULLETS = {"a", "b", "c", "e", "end-payment", "end-payout"}
PLACEMENTS = {"where", "decides", "responsible", "boundary", "reason"}
GAP_KINDS = {"page not read", "observation needed", "searched, not found", "stated only in general terms"}
WHO = {"agent", "founder", "either"}
ACCESS = {"md", "raw", "rendered", "local"}
BASES = {"term", "identifiers", "definition", "answers"}
KINDS = {"observed", "shipped", "stated", "official page"}
CAUSES = ["no difference", "market, named rule", "maturity", "business model", "market, pattern", "vendor choice", "unknown"]
LETTERS = {"A", "B", "C", "D", "unknown"}
RULES = {"a commonality, carried as the references carry it", "the platform carries all the variants at once",
         "a variation point behind one interface, bound per market, store or plan",
         "bound per product", "a variation point bound per market",
         "a decision for the founder, on a recommendation", "left to the build",
         "kept open as a variation point until evidence settles it"}
FOUNDER_RULE = "a decision for the founder, on a recommendation"
MARKS = {"carried unchanged", "carried with configuration", "carried only with a partner", "no placement", "unknown"}
WHEN = {"before build", "before release", "later", "unclear"}
ANSWERERS = {"founder decision", "partner", "regulator", "Yemen evidence", "platform evidence"}
YEMEN_NAMES = re.compile(r"(?i)yemen|\baden\b|sana'?a|\byer\b|اليمن|يمني|عدن|صنعاء|ريال يمني")
NON_ANSWERS = {"absent", "gap", "not covered"}
HEAD = {
    "statements.tsv": ["stmt_id", "bullet", "placement", "identifier", "statement", "scope", "marker", "conditions", "cite_ids", "from", "note"],
    "terms.tsv": ["term", "translation", "definition", "cite_ids"],
    "absences.tsv": ["absence_id", "bullet", "what_is_absent", "list_cite_ids", "complete_cite_ids", "note"],
    "gaps.tsv": ["gap_id", "bullet", "what_is_missing", "read", "gap_kind", "who_can", "route"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
    "a2.tsv": ["vp_id", "stmt_ids", "gap_ids", "absence_ids", "read"],
    "variation-points.tsv": ["vp_id", "bullet", "question", "x_words", "raised_by", "note"],
    "variants.tsv": ["variant_id", "vp_id", "platform", "variant", "stmt_ids", "basis", "basis_evidence", "kind", "scope",
                     "gap_ids", "absence_ids", "note"],
    "analysis.tsv": ["vp_id", "cause", "cause_basis", "scopes_compared", "cause_reading", "coexistence", "coexistence_basis",
                     "general_variant", "follows", "expensive_because", "founder_item", "note"],
    "yemen-marks.tsv": ["vp_id", "case_id", "mark", "variant_id", "condition_stmt_ids", "case_evidence", "per_variant",
                        "product_gap", "founder_item", "moves", "what_would_show_it", "note"],
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
        if check_head and len(row) != len(head):
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

def contained(part, whole):
    """Is part a verbatim excerpt of whole, after the same normalization quotes get?"""
    pv, wv = text_variants(part), text_variants(whole)
    return any(p[1] and p[1] in w[1] for p, w in zip(pv, wv))

# ---------- phase A, per platform ----------
stmts, gaps, cit_all, kinds, absences = {}, {}, {}, {}, {}
for plat, code in PLATFORMS.items():
    d = os.path.join(subj, plat)
    if not os.path.isdir(d):
        continue
    pre = f"{SID}-{code}"
    st = read(os.path.join(d, "statements.tsv"), f"{plat}/statements.tsv") or []
    tm = read(os.path.join(d, "terms.tsv"), f"{plat}/terms.tsv") or []
    ab = read(os.path.join(d, "absences.tsv"), f"{plat}/absences.tsv")
    gp = read(os.path.join(d, "gaps.tsv"), f"{plat}/gaps.tsv") or []
    ct = read(os.path.join(d, "citations.tsv"), f"{plat}/citations.tsv") or []
    if ab is None:
        err(f"{plat}/absences.tsv", "", "file missing (a header row alone is fine)")
        ab = []
    unique(f"{plat}/statements.tsv", st, "stmt_id", rf"^{pre}-\d{{3}}$")
    unique(f"{plat}/gaps.tsv", gp, "gap_id", rf"^{pre}-G\d{{2}}$")
    unique(f"{plat}/absences.tsv", ab, "absence_id", rf"^{pre}-N\d{{2}}$")
    unique(f"{plat}/citations.tsv", ct, "cite_id", rf"^{pre}-C\d{{3,4}}$")
    if not os.path.exists(os.path.join(d, "notes.md")):
        err(f"{plat}/notes.md", "", "file missing")
    cit = {c["cite_id"]: c for c in ct}
    cit_all.update(cit)
    qdir = os.path.join(SKM, "studies/concern-map/platforms", plat)
    concerns = {r["concern_id"] for r in (read(os.path.join(qdir, "concerns.tsv"), "concerns.tsv", False) or [])}
    index_cits = {r["cite_id"]: r for r in (read(os.path.join(qdir, "citations.tsv"), "citations.tsv", False) or [])}
    used = set()
    for r in st:
        sid = r["stmt_id"]
        f = f"{plat}/statements.tsv"
        bl = [b.strip() for b in r["bullet"].split(";") if b.strip()]
        r["bullets"] = set(bl)
        if not bl or any(b not in BULLETS for b in bl):
            err(f, sid, f"bullet '{r['bullet']}' is not one or more of a, b, c, d, e, end-payment or end-payout")
        stmts[sid] = dict(r, platform=plat)
        if r["placement"] not in PLACEMENTS:
            err(f, sid, f"placement '{r['placement']}' is not one of {sorted(PLACEMENTS)}")
        if not r["statement"]:
            err(f, sid, "statement is empty")
        cs = ids(r["cite_ids"])
        if not cs:
            err(f, sid, "no citation")
        for c in cs:
            used.add(c)
            if c not in cit:
                err(f, sid, f"cite_id {c} not in citations")
        frm = r["from"]
        if frm != "new":
            m = re.match(r"^index:([^:]+):([^:]+)$", frm)
            if not m or m.group(1) not in concerns or m.group(2) not in index_cits:
                err(f, sid, f"from '{frm}' is neither 'new' nor index:<concern_id>:<index cite_id> of the Q1 index")
            elif cs and cs[0] in cit:
                ic, nc = index_cits[m.group(2)], cit[cs[0]]
                if (ic["source"], ic["quote"]) != (nc["source"], nc["quote"]):
                    err(f, sid, f"the copied citation {cs[0]} changed the index citation {m.group(2)}'s source or quote")
        if cs and cs[0] in cit and r["statement"]:
            res, why, share = SRC.check_quote(r["statement"], cit[cs[0]]["source"])
            if not res.startswith("found"):
                err(f, sid, f"statement not found verbatim in {cs[0]}'s source ({res}{'; ' + why if why else ''})",
                    "pending capture" if res == "unresolved" and re.match(r"^https?://", cit[cs[0]]["source"]) else "error")
        ks = sorted({kind_of(cit[c]["source"], ROOTS)[0] for c in cs if c in cit})
        kinds[sid] = (";".join(ks), "; ".join(kind_of(cit[c]["source"], ROOTS)[1] for c in cs[:1] if c in cit))
        if "unknown" in ks:
            err(f, sid, "a citation's kind is unknown under method/source_kinds.py", "review")
    for t in tm:
        cs = ids(t["cite_ids"])
        if not cs:
            err(f"{plat}/terms.tsv", t["term"][:30], "no citation")
        for c in cs:
            used.add(c)
            if c not in cit:
                err(f"{plat}/terms.tsv", t["term"][:30], f"cite_id {c} not in citations")
    for a in ab:
        absences[a["absence_id"]] = dict(a, platform=plat)
        if a["bullet"] not in ("a", "b", "c", "e"):
            err(f"{plat}/absences.tsv", a["absence_id"], f"bullet '{a['bullet']}' is not a, b, c or e")
        for col in ("list_cite_ids", "complete_cite_ids"):
            if not ids(a[col]):
                err(f"{plat}/absences.tsv", a["absence_id"], f"{col} is empty")
            for c in ids(a[col]):
                used.add(c)
                if c not in cit:
                    err(f"{plat}/absences.tsv", a["absence_id"], f"cite_id {c} not in citations")
    for g in gp:
        gid, f = g["gap_id"], f"{plat}/gaps.tsv"
        gaps[gid] = dict(g, platform=plat)
        if g["bullet"] not in GAP_BULLETS:
            err(f, gid, f"bullet '{g['bullet']}' is not one of a, b, c, e, end-payment or end-payout")
        if g["gap_kind"] not in GAP_KINDS:
            err(f, gid, f"gap_kind '{g['gap_kind']}' is not one of {sorted(GAP_KINDS)}")
        if g["who_can"] not in WHO:
            err(f, gid, f"who_can '{g['who_can']}' is not one of {sorted(WHO)}")
        if not g["read"]:
            err(f, gid, "read is empty: list each path or URL read")
        if g["gap_kind"] == "searched, not found" and not names_a_source(g["read"]):
            err(f, gid, "a 'searched, not found' names what it read")
        if g["who_can"] in ("founder", "either"):
            for u in urls_in(g["route"]):
                held = [h for h in HELD.lookup(u) if h["readable"]]
                if held:
                    err(f, gid, f"{u} is held at {describe(held[0])}: read it instead of routing it to the founder")
    for c in ct:
        cid, src, f = c["cite_id"], c["source"], f"{plat}/citations.tsv"
        if c["access_path"] not in ACCESS:
            err(f, cid, f"access_path '{c['access_path']}' is not one of {sorted(ACCESS)}")
        if re.match(r"^(observed-sh|observed-sa)(?!@[0-9a-f]{7,40}:)", src):
            err(f, cid, "a local source names its repository at a commit")
        if "..." in c["quote"] or "…" in c["quote"]:
            err(f, cid, "quote contains an ellipsis")
        if len(c["quote"]) > 300:
            err(f, cid, f"quote is {len(c['quote'])} characters; the brief allows 300", "warning")
        for col in ("locator", "source_date", "date_basis", "accessed"):
            if not c[col]:
                err(f, cid, f"{col} is empty")
        if cid not in used:
            err(f, cid, "not used by any statement, term or absence", "warning")
        if re.match(r"^https?://", src):
            urls[src.split("#")[0]].add(cid)
        res, why, share = SRC.check_quote(c["quote"], src) if c["quote"] and src else ("unresolved", "no quote or source", "")
        if not res.startswith("found"):
            err(f, cid, f"quote {res}{'; ' + why if why else ''}",
                "pending capture" if res == "unresolved" and re.match(r"^https?://", src) else "error")
        quotes.append((cid, res, why, share, src, c["quote"][:200]))
for sid, r in stmts.items():
    if "e" in r["bullets"]:
        cs = [] if r["conditions"] == "none stated" else ids(r["conditions"])
        if not cs and r["conditions"] != "none stated":
            err(f"{r['platform']}/statements.tsv", sid, "a statement under (e) names the statements it conditions")
        for c in cs:
            if c not in stmts or stmts[c]["platform"] != r["platform"] or not (stmts[c]["bullets"] & {"a", "b", "c"}):
                err(f"{r['platform']}/statements.tsv", sid, f"conditions {c} is not one of its platform's (a) to (c) statements")
    elif r["conditions"]:
        err(f"{r['platform']}/statements.tsv", sid, "conditions is only for statements under (e)")
for plat in PLATFORMS:
    if not os.path.isdir(os.path.join(subj, plat)):
        continue
    stated = {b for r in stmts.values() if r["platform"] == plat for b in r["bullets"]}
    gapped = {g["bullet"] for g in gaps.values() if g["platform"] == plat}
    for b in ("a", "b", "c", "e"):
        if b not in stated and b not in gapped:
            err(f"{plat}/gaps.tsv", b, f"bullet ({b}) is neither stated nor recorded as a gap")
    for end in ("end-payment", "end-payout"):
        if end not in stated and end not in gapped:
            err(f"{plat}/statements.tsv", end, f"{end} is neither named by a statement nor recorded as a gap")
if stmts:
    with open(os.path.join(subj, "kinds.tsv"), "w", encoding="utf-8") as f:
        f.write("stmt_id\tkind\trule\n")
        for sid, (k, why) in kinds.items():
            f.write(f"{sid}\t{k}\t{why}\n")

# ---------- phase B ----------
vps = read(os.path.join(subj, "variation-points.tsv"), "variation-points.tsv")
var = read(os.path.join(subj, "variants.tsv"), "variants.tsv")
vp = {}
if vps is not None:
    unique("variation-points.tsv", vps, "vp_id", rf"^{SID}-VP-\d{{2}}$")
    vp = {v["vp_id"]: v for v in vps}
    if len(vps) > 25:
        err("variation-points.tsv", "", f"{len(vps)} variation points: the brief says stop and report past 25")
    for v in vps:
        i = v["vp_id"]
        if v["bullet"] not in ("a", "b", "c"):
            err("variation-points.tsv", i, f"bullet '{v['bullet']}' is not a, b or c")
        if not re.match(r"(?i)^(who|what)\b", v["question"]):
            err("variation-points.tsv", i, "the question doesn't take the form 'who or what fills X'")
        if not v["x_words"]:
            err("variation-points.tsv", i, "x_words is empty")
        quoted = re.findall(r'"([^"]+)"|“([^”]+)”|«([^»]+)»', v["question"])
        spans = [next(x for x in q if x) for q in quoted]
        if not spans:
            err("variation-points.tsv", i, "the question quotes no X")
        elif not any(contained(x, stmts[s]["statement"]) for x in spans for s in ids(v["raised_by"]) if s in stmts):
            err("variation-points.tsv", i, "the question's quoted X is not from a raised_by statement")
        if not ids(v["raised_by"]):
            err("variation-points.tsv", i, "raised_by is empty")
        for s in ids(v["raised_by"]):
            if s not in stmts:
                err("variation-points.tsv", i, f"raised_by {s} is not a statement")
            elif v["bullet"] not in stmts[s]["bullets"]:
                err("variation-points.tsv", i, f"raised_by {s} is not under bullet {v['bullet']}")
if var is not None:
    unique("variants.tsv", var, "variant_id", rf"^{SID}-V-\d{{3}}$")
    seen = set()
    for r in var:
        i, plat = r["variant_id"], r["platform"]
        seen.add((r["vp_id"], plat))
        if r["vp_id"] not in vp:
            err("variants.tsv", i, "vp_id not in variation-points.tsv")
        if plat not in PLATFORMS:
            err("variants.tsv", i, "platform is not one of the five")
        if r["variant"] == "gap":
            if not ids(r["gap_ids"]):
                err("variants.tsv", i, "a gap variant names its gap_ids")
            for g in ids(r["gap_ids"]):
                if gaps.get(g, {}).get("platform") != plat:
                    err("variants.tsv", i, f"gap {g} is not one of {plat}'s gaps")
                elif r["vp_id"] in vp and gaps[g]["bullet"] != vp[r["vp_id"]]["bullet"]:
                    err("variants.tsv", i, f"gap {g} is under bullet {gaps[g]['bullet']}, not the variation point's")
        elif r["variant"] == "absent":
            if not ids(r["absence_ids"]):
                err("variants.tsv", i, "an absent variant names its absence_ids")
            for a in ids(r["absence_ids"]):
                if absences.get(a, {}).get("platform") != plat:
                    err("variants.tsv", i, f"absence {a} is not one of {plat}'s absences")
                elif r["vp_id"] in vp and absences[a]["bullet"] != vp[r["vp_id"]]["bullet"]:
                    err("variants.tsv", i, f"absence {a} is under bullet {absences[a]['bullet']}, not the variation point's")
                else:
                    lk = sorted({kind_of(cit_all[c]["source"], ROOTS)[0] for c in ids(absences[a]["list_cite_ids"]) if c in cit_all})
                    if lk and sorted(k.strip() for k in r["kind"].split(";") if k.strip()) != lk:
                        err("variants.tsv", i, f"kind '{r['kind']}' is not its list's kind {';'.join(lk)}")
        elif r["variant"] != "not covered":
            bs = [b.strip() for b in r["basis"].split(";") if b.strip()]
            if not bs or any(b not in BASES for b in bs):
                err("variants.tsv", i, f"basis '{r['basis']}' is not one or more of {sorted(BASES)}")
            if not r["basis_evidence"]:
                err("variants.tsv", i, "basis_evidence is empty")
            if any(stmts.get(x, {}).get("bullets", set()) & {"d"} and not stmts[x]["bullets"] & {"a", "b", "c"}
                   for x in ids(r["stmt_ids"])) and bs != ["answers"]:
                err("variants.tsv", i, "a variant resting on a (d) statement takes the basis 'answers'")
            sids = ids(r["stmt_ids"])
            if not sids:
                err("variants.tsv", i, "no stmt_ids")
            for s in sids:
                if stmts.get(s, {}).get("platform") != plat:
                    err("variants.tsv", i, f"{s} is not one of {plat}'s statements")
            if sids and all(s in stmts for s in sids) and not any(contained(r["variant"], stmts[s]["statement"]) for s in sids):
                err("variants.tsv", i, "the variant is not a verbatim excerpt of any of its statements")
            want = sorted({k for s in sids if s in kinds for k in kinds[s][0].split(";") if k})
            got = sorted({k.strip() for k in r["kind"].split(";") if k.strip()})
            if want and got != want:
                err("variants.tsv", i, f"kind '{r['kind']}' differs from kinds.tsv's {';'.join(want)}")
    for v in vp:
        for p in PLATFORMS:
            if os.path.isdir(os.path.join(subj, p)) and (v, p) not in seen:
                err("variants.tsv", f"{v}/{p}", "no row for this variation point and platform")
    placed = {s for r in var for s in ids(r["stmt_ids"])}
    unplaced = [s for s in stmts if s not in placed and stmts[s]["bullets"] & {"a", "b", "c", "d"}]
    if unplaced:
        err("variants.tsv", "", f"{len(unplaced)} statements under bullets a to d are under no variation point: "
                                f"{', '.join(unplaced[:12])}", "review")
for plat in PLATFORMS:
    a2 = read(os.path.join(subj, plat, "a2.tsv"), f"{plat}/a2.tsv")
    for r in a2 or []:
        if r["vp_id"] not in vp:
            err(f"{plat}/a2.tsv", r["vp_id"], "not a variation point")
        for s in ids(r["stmt_ids"]):
            if s not in stmts:
                err(f"{plat}/a2.tsv", r["vp_id"], f"{s} is not a statement")
        for g in ids(r["gap_ids"]):
            if g not in gaps:
                err(f"{plat}/a2.tsv", r["vp_id"], f"{g} is not a gap")
        for a in ids(r["absence_ids"]):
            if a not in absences:
                err(f"{plat}/a2.tsv", r["vp_id"], f"{a} is not an absence")
        if not r["read"]:
            err(f"{plat}/a2.tsv", r["vp_id"], "read is empty")

# ---------- phase C ----------
ana = read(os.path.join(subj, "analysis.tsv"), "analysis.tsv")
variant_ids = {r["variant_id"] for r in (var or [])}
founder_items = []
if ana is not None:
    for k, n in Counter(r["vp_id"] for r in ana).items():
        if n > 1:
            err("analysis.tsv", k, f"{n} rows for one variation point")
    for v in set(vp) - {r["vp_id"] for r in ana}:
        err("analysis.tsv", v, "no analysis row")
    for r in ana:
        v = r["vp_id"]
        if r["cause"] not in CAUSES:
            err("analysis.tsv", v, f"cause '{r['cause']}' is not one of {CAUSES}")
        if r["cause"] not in ("unknown", "no difference") and not r["cause_reading"].startswith("Reading:"):
            err("analysis.tsv", v, "cause_reading doesn't start with 'Reading:'")
        for col in ("cause_basis", "coexistence_basis"):
            for s in ids(r[col]):
                if s not in stmts and s not in variant_ids and s not in absences:
                    err("analysis.tsv", v, f"{col} {s} is not a statement, variant or absence")
        parts = [x.strip() for x in r["coexistence"].split(";") if x.strip()]
        if not parts or not all(re.match(r"^(\w+)\s*=\s*(A|B|C|D|unknown)$", x) and x.split("=")[0].strip() in PLATFORMS
                                for x in parts):
            err("analysis.tsv", v, f"coexistence '{r['coexistence']}' is not one letter per platform, as 'shopify=B; salla=D'")
        present = {p for p in PLATFORMS if os.path.isdir(os.path.join(subj, p))}
        named = {x.split("=")[0].strip() for x in parts if "=" in x}
        if present - named:
            err("analysis.tsv", v, f"coexistence leaves out {', '.join(sorted(present - named))}")
        if r["general_variant"] and r["general_variant"] not in variant_ids:
            err("analysis.tsv", v, f"general_variant {r['general_variant']} is not a variant")
        fol = [x.strip() for x in r["follows"].split(";") if x.strip()]
        if fol != ["none applies"] and (not fol or any(x not in RULES for x in fol)):
            err("analysis.tsv", v, "follows is not 'none applies' or rules in exactly the table's words")
        if bool(r["founder_item"]) != (FOUNDER_RULE in fol):
            err("analysis.tsv", v, "a founder_item is given exactly when a decision for the founder follows")
        if not r["expensive_because"]:
            err("analysis.tsv", v, "expensive_because is empty")
        if r["founder_item"]:
            founder_items.append((v, r["founder_item"]))

# ---------- step 2: Yemen marks ----------
marks = read(os.path.join(subj, "yemen-marks.tsv"), "yemen-marks.tsv")
if marks is not None:
    yc = os.path.join(SKM, "studies/yemen-cases")
    cases = {r["case_id"] for r in (read(os.path.join(yc, "cases.tsv"), "cases.tsv", False) or [])}
    ye = set()
    for name, key in (("axes.tsv", "axis_id"), ("constants.tsv", "constant_id"), ("citations.tsv", "cite_id")):
        ye |= {r[key] for r in (read(os.path.join(yc, name), name, False) or [])}
    for r in marks:
        key = f"{r['vp_id']}/{r['case_id']}"
        if r["vp_id"] not in vp:
            err("yemen-marks.tsv", key, "vp_id not in variation-points.tsv")
        if r["case_id"] not in cases:
            err("yemen-marks.tsv", key, "case_id not in studies/yemen-cases/cases.tsv")
        if r["mark"] not in MARKS:
            err("yemen-marks.tsv", key, f"mark '{r['mark']}' is not one of {sorted(MARKS)}")
        if r["mark"] not in ("unknown", "no placement") and r["variant_id"] not in variant_ids:
            err("yemen-marks.tsv", key, "the mark names the variant it used by variant_id")
        if r["mark"] != "unknown":
            if not ids(r["condition_stmt_ids"]) or not ids(r["case_evidence"]):
                err("yemen-marks.tsv", key, "a mark other than unknown cites both the variant's condition and the case's evidence")
            vstmts = set()
            for x in (var or []):
                if x["variant_id"] == r["variant_id"]:
                    vstmts = set(ids(x["stmt_ids"]))
            for s in ids(r["condition_stmt_ids"]):
                if s not in stmts:
                    err("yemen-marks.tsv", key, f"condition {s} is not a statement")
                elif vstmts and s not in vstmts:
                    st = stmts[s]
                    linked = "e" in st["bullets"] and (
                        set(ids(st["conditions"])) & vstmts or
                        (st["conditions"] == "none stated" and st["identifier"] and
                         any(st["identifier"] in stmts[v]["statement"] or st["identifier"] in stmts[v]["identifier"]
                             for v in vstmts if v in stmts)))
                    if not linked:
                        err("yemen-marks.tsv", key, f"condition {s} is neither the variant's statement nor an (e) statement linked to it")
            for y in ids(r["case_evidence"]):
                if y not in ye:
                    err("yemen-marks.tsv", key, f"case evidence {y} is not a Stage 1 id")
        elif not r["what_would_show_it"]:
            err("yemen-marks.tsv", key, "an unknown mark says what would show it")
        if r["mark"] == "no placement":
            if not r["product_gap"]:
                err("yemen-marks.tsv", key, "no placement is written as a product gap")
            if not r["founder_item"]:
                err("yemen-marks.tsv", key, "no placement raises a design decision for the founder in founder_item")
            listed = set()
            for entry in [x for x in r["per_variant"].split(";") if ":" in x]:
                vid, _, rest = entry.partition(":")
                listed.add(vid.strip())
                cond, _, evid = rest.partition("/")
                if not ids(cond) or not ids(evid):
                    err("yemen-marks.tsv", key, f"per_variant entry for {vid.strip()} gives a condition and case evidence, as 'id: stmt_ids / case ids'")
                for c in ids(cond):
                    if c not in stmts:
                        err("yemen-marks.tsv", key, f"per_variant condition {c} is not a statement")
                for y in ids(evid):
                    if y not in ye:
                        err("yemen-marks.tsv", key, f"per_variant evidence {y} is not a Stage 1 id")
            answers = {x["variant_id"] for x in (var or []) if x["vp_id"] == r["vp_id"] and x["variant"] not in NON_ANSWERS}
            if answers - listed:
                err("yemen-marks.tsv", key, f"no placement shows no failure for {', '.join(sorted(answers - listed))}")
        if YEMEN_NAMES.search(r["product_gap"]):
            err("yemen-marks.tsv", key, "the product gap names Yemen or a place in it")
    have = {(r["vp_id"], r["case_id"]) for r in marks}
    for v in vp:
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
                if v not in vp:
                    err("rows.tsv", rid, f"{v} is not a variation point")
            if r["when"] not in WHEN:
                err("rows.tsv", rid, f"when '{r['when']}' is not one of {sorted(WHEN)}")
            who = [x.strip() for x in r["who_answers"].split(";") if x.strip()]
            if not who or any(x not in ANSWERERS for x in who):
                err("rows.tsv", rid, f"who_answers '{r['who_answers']}' is not one or more of {sorted(ANSWERERS)}")
            if ana is not None:
                fol = {v: [x.strip() for x in a["follows"].split(";")] for v, a in ((a["vp_id"], a) for a in ana)}
                marked = {m["vp_id"] for m in (marks or []) if m["founder_item"]}
                def when_of(v):
                    f = fol.get(v, [])
                    if FOUNDER_RULE in f or v in marked:
                        return 0, "before build"
                    if any(x in f for x in ("kept open as a variation point until evidence settles it",
                                            "a variation point behind one interface, bound per market, store or plan",
                                            "a variation point bound per market")):
                        return 1, "before release"
                    if f and f != ["none applies"]:
                        return 2, "later"
                    return 3, "unclear"
                expect = min((when_of(v) for v in ids(r["vp_ids"]) if v in vp), default=(3, "unclear"))[1]
                if r["when"] != expect:
                    err("rows.tsv", rid, f"when is '{r['when']}', but the mapping from follows gives '{expect}'")
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
print(f"statements {len(stmts)}, gaps {len(gaps)}, variation points {len(vp)}, founder items {len(founder_items)} | "
      f"issues: {dict(Counter(i[0] for i in issues))} | quotes: {dict(Counter(q[1].split(' (')[0] for q in quotes))} | "
      f"web sources to capture: {len(items)}")
