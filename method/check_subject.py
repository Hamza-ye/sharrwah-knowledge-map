# Checks a subject's files (PLAN.md Stages 2 and 4) against its briefs in studies/subjects/<id>/briefs/:
# phase A per platform (statements, terms, absences, gaps, citations), phase A2 (a2.tsv), phase B (variation
# points, variants), phase C (analysis), step 2 (Yemen marks) and step 3 (rows), as far as they exist.
# It checks files and columns, ids and every id a file cites, that statements and quotes are verbatim in their
# sources, that a variant is an excerpt of its statements, that copied citations are unchanged (from the Q1 index or
# an earlier subject's statement, which a statement's `from` names), and that no
# gap goes to the founder for a page that is held. It writes the subject's kinds.tsv (each statement's kind, by
# rule: method/source_kinds.py) and lists the cited URLs that need capturing.
#
# A subject's bullets, the questions its phase A brief asks of each platform, are in its bullets.tsv: `bullet`,
# `root_decision`, `asks` and `role`. A role is one of:
#   ask         a question each platform states or records as a gap; variation points take one of these;
#   conditions  stated or recorded as a gap too; each statement under it names the `ask` statements it conditions;
#   no-part     that the platform has no part in it, or holds no such thing; it needs no gap;
#   end         an end of the subject's interval, named by a statement or recorded as a gap.
# Without the file, the pilot's bullets hold: a to c ask, d no-part, e conditions, end-payment and end-payout.
# A subject's limits.tsv (`limit`, `value`, `note`) may set `variation points`, the number past which phase B stops
# and reports; it is 25 without it.
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
PILOT_BULLETS = {"a": "ask", "b": "ask", "c": "ask", "d": "no-part", "e": "conditions",
                 "end-payment": "end", "end-payout": "end"}
ROLES = {"ask", "conditions", "no-part", "end"}
PLACEMENTS = {"where", "decides", "responsible", "boundary", "reason"}
# What a value is taken per, under a "takes its value per" question (S-02's phase B brief, rule 4)
PER_PHRASES = ["the store's own country", "a market the store sells into", "the buyer's country", "the whole store"]
GAP_KINDS = {"page not read", "observation needed", "searched, not found", "stated only in general terms"}
WHO = {"agent", "founder", "either", "capture"}   # capture: a run in observed-sh or observed-sa, through a handoff
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
    "bullets.tsv": ["bullet", "root_decision", "asks", "role"],
    "limits.tsv": ["limit", "value", "note"],
    "statements.tsv": ["stmt_id", "bullet", "placement", "identifier", "statement", "scope", "marker", "conditions", "cite_ids", "from", "note"],
    "terms.tsv": ["term", "translation", "definition", "cite_ids"],
    "absences.tsv": ["absence_id", "bullet", "what_is_absent", "list_cite_ids", "complete_cite_ids", "note"],
    "gaps.tsv": ["gap_id", "bullet", "what_is_missing", "read", "gap_kind", "who_can", "route"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
    "a2.tsv": ["vp_id", "stmt_ids", "gap_ids", "absence_ids", "read"],
    "absence-audit.tsv": ["claim_id", "searches", "read", "result", "stmt_ids", "note"],
    "variation-points.tsv": ["vp_id", "bullet", "question", "x_words", "raised_by", "note"],
    "variants.tsv": ["variant_id", "vp_id", "platform", "variant", "stmt_ids", "basis", "basis_evidence", "kind", "scope",
                     "gap_ids", "absence_ids", "note"],
    "analysis.tsv": ["vp_id", "cause", "cause_basis", "scopes_compared", "cause_reading", "coexistence", "coexistence_basis",
                     "general_variant", "follows", "expensive_because", "founder_item", "note"],
    "bears-on.tsv": ["vp_id", "axis_ids", "constant_ids", "basis", "note"],
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

def read_later(plat):
    """What phases A2 and A3 list as read for a platform."""
    return " ".join(r.get("read", "") for n in ("a2.tsv", "absence-audit.tsv")
                    for r in (read(os.path.join(subj, plat, n), f"{plat}/{n}", check_head=False) or []))

def was_read(held, later):
    """A page a gap was routed to, read since by phase A2 or A3: they name its held copy (a capture by its item's
    folder), not only its address, which may have been listed when it couldn't be fetched."""
    return any((os.path.dirname(h["location"]) if h["kind"] == "capture" else h["location"]) in later for h in held)

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

def one_of(bs):
    bs = list(bs)
    return bs[0] if len(bs) == 1 else ", ".join(bs[:-1]) + " or " + bs[-1]

def load_bullets():
    rows = read(os.path.join(subj, "bullets.tsv"), "bullets.tsv")
    if rows is None:
        return dict(PILOT_BULLETS)
    unique("bullets.tsv", rows, "bullet", r"^[a-z][a-z-]*$")
    for r in rows:
        if r["role"] not in ROLES:
            err("bullets.tsv", r["bullet"], f"role '{r['role']}' is not one of {sorted(ROLES)}")
        if not r["asks"]:
            err("bullets.tsv", r["bullet"], "asks is empty")
    if not any(r["role"] == "ask" for r in rows):
        err("bullets.tsv", "", "no bullet has the role 'ask', so no variation point can take one")
    global BULLET_RD
    BULLET_RD = {r["bullet"]: [x.strip() for x in r["root_decision"].split(";") if x.strip()] for r in rows}
    return {r["bullet"]: r["role"] for r in rows}

BULLET_RD = {}                          # bullet -> its root decisions, from bullets.tsv; empty for the pilot
BULLET_ROLE = load_bullets()

def load_limits():
    rows = read(os.path.join(subj, "limits.tsv"), "limits.tsv")
    out = {"variation points": 25}
    for r in rows or []:
        if r["limit"] not in out:
            err("limits.tsv", r["limit"], f"not a limit this checker knows: {sorted(out)}")
        elif not r["value"].isdigit():
            err("limits.tsv", r["limit"], f"value '{r['value']}' is not a whole number")
        else:
            out[r["limit"]] = int(r["value"])
    return out

LIMITS = load_limits()
ORDER = list(BULLET_ROLE)                                 # the subject's own order, for messages
def of_role(*roles):
    return [b for b in ORDER if BULLET_ROLE[b] in roles]
BULLETS = set(ORDER)
ASK, COND, NOPART, ENDS = set(of_role("ask")), set(of_role("conditions")), set(of_role("no-part")), set(of_role("end"))
GAP_BULLETS = ASK | COND | ENDS

_earlier = {}
def earlier_subject(sid, plat):
    """An earlier subject's statements and citations for a platform, by id: what a copied statement came from."""
    if (sid, plat) not in _earlier:
        d = os.path.join(SKM, "studies", "subjects", sid, plat)
        st = read(os.path.join(d, "statements.tsv"), f"{sid}/{plat}/statements.tsv", False) or []
        ct = read(os.path.join(d, "citations.tsv"), f"{sid}/{plat}/citations.tsv", False) or []
        _earlier[(sid, plat)] = ({x["stmt_id"]: x for x in st}, {x["cite_id"]: x for x in ct})
    return _earlier[(sid, plat)]

# ---------- phase A, per platform ----------
stmts, gaps, cit_all, kinds, absences, superseded = {}, {}, {}, {}, {}, {}
for plat, code in PLATFORMS.items():
    d = os.path.join(subj, plat)
    if not os.path.isdir(d):
        continue
    pre = f"{SID}-{code}"
    st = read(os.path.join(d, "statements.tsv"), f"{plat}/statements.tsv") or []
    tm = read(os.path.join(d, "terms.tsv"), f"{plat}/terms.tsv") or []
    ab = read(os.path.join(d, "absences.tsv"), f"{plat}/absences.tsv")
    gp = read(os.path.join(d, "gaps.tsv"), f"{plat}/gaps.tsv") or []
    later = read_later(plat)
    ct = read(os.path.join(d, "citations.tsv"), f"{plat}/citations.tsv") or []
    if ab is None:
        err(f"{plat}/absences.tsv", "", "file missing (a header row alone is fine)")
        ab = []
    unique(f"{plat}/statements.tsv", st, "stmt_id", rf"^{pre}-\d{{3,4}}$")
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
            err(f, sid, f"bullet '{r['bullet']}' is not one or more of {one_of(ORDER)}")
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
        earlier = re.match(r"^S(\d\d)-[A-Z]{2}-\d{3}$", frm)
        if earlier:                              # copied from an earlier subject's statement, by its id
            es, ec = earlier_subject(f"S-{earlier.group(1)}", plat)
            if f"S-{earlier.group(1)}" == os.path.basename(subj) or frm not in es:
                err(f, sid, f"from '{frm}' is not a statement of an earlier subject's {plat} folder")
            elif cs and cs[0] in cit:
                oc = ec.get((ids(es[frm]["cite_ids"]) or [""])[0], {})
                if (oc.get("source"), oc.get("quote")) != (cit[cs[0]]["source"], cit[cs[0]]["quote"]):
                    err(f, sid, f"the copied citation {cs[0]} changed {frm}'s first citation's source or quote")
        elif frm != "new":
            m = re.match(r"^index:([^:]+):([^:]+)$", frm)
            if not m or m.group(1) not in concerns or m.group(2) not in index_cits:
                err(f, sid, f"from '{frm}' is neither 'new', an earlier subject's statement id, nor "
                            "index:<concern_id>:<index cite_id> of the Q1 index")
            elif cs and cs[0] in cit:
                ic, nc = index_cits[m.group(2)], cit[cs[0]]
                if (ic["source"], ic["quote"]) != (nc["source"], nc["quote"]):
                    err(f, sid, f"the copied citation {cs[0]} changed the index citation {m.group(2)}'s source or quote")
        if cs and cs[0] in cit and r["statement"]:
            res, why, share = SRC.check_quote(r["statement"], cit[cs[0]]["source"], cit[cs[0]]["locator"])
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
        lcs = [c for c in ids(a["list_cite_ids"]) if c in cit]
        if lcs:                                  # an absence's kind is its list's, by the same rules
            kinds[a["absence_id"]] = (";".join(sorted({kind_of(cit[c]["source"], ROOTS)[0] for c in lcs})),
                                      kind_of(cit[lcs[0]]["source"], ROOTS)[1])
        if a["bullet"] not in ASK | COND:
            err(f"{plat}/absences.tsv", a["absence_id"], f"bullet '{a['bullet']}' is not {one_of(of_role('ask', 'conditions'))}")
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
        for x in re.findall(r"in place of (S\d\d-[A-Z]{2}-G\d+)", g["what_is_missing"]):
            superseded[x] = gid                    # a gap a later part narrowed: kept as history, settled by its successor
        if g["bullet"] not in GAP_BULLETS:
            err(f, gid, f"bullet '{g['bullet']}' is not one of {one_of(of_role('ask', 'conditions', 'end'))}")
        if g["gap_kind"] not in GAP_KINDS:
            err(f, gid, f"gap_kind '{g['gap_kind']}' is not one of {sorted(GAP_KINDS)}")
        if g["who_can"] not in WHO:
            err(f, gid, f"who_can '{g['who_can']}' is not one of {sorted(WHO)}")
        if g["who_can"] == "capture" and not re.search(r"handoffs/H-\d{3}", g["route"]):
            err(f, gid, "a gap for a capture run names its handoff in route (handoffs/H-NNN)")
        if not g["read"]:
            err(f, gid, "read is empty: list each path or URL read")
        if g["gap_kind"] == "searched, not found" and not names_a_source(g["read"]):
            err(f, gid, "a 'searched, not found' names what it read")
        if g["who_can"] in ("founder", "either", "capture"):
            for u in urls_in(g["route"]):
                held = [h for h in HELD.lookup(u) if h["readable"]]
                if held and not was_read(held, later):   # once A2 or A3 reads it, a2.tsv says what remains
                    err(f, gid, f"{u} is held at {describe(held[0])}: read it instead of routing it to the founder")
    for c in ct:
        cid, src, f = c["cite_id"], c["source"], f"{plat}/citations.tsv"
        if c["access_path"] not in ACCESS:
            err(f, cid, f"access_path '{c['access_path']}' is not one of {sorted(ACCESS)}")
        if re.match(r"^(observed-sh|observed-sa)(?!@[0-9a-f]{7,40}:)", src):
            err(f, cid, "a local source names its repository at a commit")
        if len(c["quote"]) > 300:
            err(f, cid, f"quote is {len(c['quote'])} characters; the brief allows 300", "warning")
        for col in ("locator", "source_date", "date_basis", "accessed"):
            if not c[col]:
                err(f, cid, f"{col} is empty")
        if cid not in used:
            err(f, cid, "not used by any statement, term or absence", "warning")
        if re.match(r"^https?://", src):
            urls[src.split("#")[0]].add(cid)
        res, why, share = SRC.check_quote(c["quote"], src, c["locator"]) if c["quote"] and src else ("unresolved", "no quote or source", "")
        if ("..." in c["quote"] or "…" in c["quote"]) and not res.startswith("found"):
            err(f, cid, "quote contains an ellipsis that its source doesn't hold: a quote leaves nothing out")
        if not res.startswith("found"):
            err(f, cid, f"quote {res}{'; ' + why if why else ''}",
                "pending capture" if res == "unresolved" and re.match(r"^https?://", src) else "error")
        elif res.endswith("in the page's source only"):
            err(f, cid, "quote found only in the page's source (its body as served, or its markup's scripts and "
                        "data), not in the page as it renders: quote what the page shows, or shows on a click "
                        "(briefs/A-one-platform.md, \"Reading a live page\")", "review")
        quotes.append((cid, res, why, share, src, c["quote"][:200]))
# ---------- phase A3: every claim of absence is audited by an agent that didn't make it ----------
for plat in PLATFORMS:
    d = os.path.join(subj, plat)
    if not os.path.isdir(d):
        continue
    audit = read(os.path.join(d, "absence-audit.tsv"), f"{plat}/absence-audit.tsv")
    claims = [g for g, r in gaps.items() if r["platform"] == plat and r["gap_kind"] != "page not read"
              and g not in superseded] + \
             [a for a, r in absences.items() if r["platform"] == plat]
    f = f"{plat}/absence-audit.tsv"
    if audit is None:
        if claims:
            err(f, "", f"{len(claims)} claims of absence not yet audited (phase A3)", "review")
        continue
    done = {}
    for r in audit:
        done[r["claim_id"]] = r
        if r["claim_id"] not in gaps and r["claim_id"] not in absences:
            err(f, r["claim_id"], "not a gap or absence of this platform")
        if "corpus_search.py" not in r["searches"]:
            err(f, r["claim_id"], "searches lists the corpus_search.py commands run")
        if not r["read"]:
            err(f, r["claim_id"], "read is empty: list each document read")
        if r["result"] not in ("confirmed", "partly contradicted", "contradicted"):
            err(f, r["claim_id"], f"result '{r['result']}' is not confirmed, partly contradicted or contradicted")
        if r["result"] == "partly contradicted" and not r["note"]:
            err(f, r["claim_id"], "a partly contradicted claim says in note what part still stands")
        if r["result"] in ("contradicted", "partly contradicted"):
            if not ids(r["stmt_ids"]):
                err(f, r["claim_id"], "a contradicted claim names the statements that show it")
            for x in ids(r["stmt_ids"]):
                if stmts.get(x, {}).get("platform") != plat:
                    err(f, r["claim_id"], f"{x} is not one of {plat}'s statements")
    # the gaps phase A2 leaves after its own searches (its a2.tsv's gap_ids) need no second audit; every other
    # claim, phase A's own searched gaps among them, has its row
    after_a2 = {g for r in (read(os.path.join(d, "a2.tsv"), f"{plat}/a2.tsv", check_head=False) or [])
                for g in ids(r.get("gap_ids", ""))
                if "corpus_search.py" in gaps.get(g, {}).get("read", "")}   # A2's own searches are named in the gap
    a2_absences = {a for r in (read(os.path.join(d, "a2.tsv"), f"{plat}/a2.tsv", check_head=False) or [])
                   for a in ids(r.get("absence_ids", ""))}
    for c in claims:
        if c in done or c in after_a2:
            continue
        if c in a2_absences:                       # an absence phase A2 recorded waits for its own audit
            err(f, c, "an absence phase A2 recorded, waiting for its audit (phase A3)", "review")
        else:
            err(f, c, "a claim of absence that the audit doesn't settle")

for sid, r in stmts.items():
    under = "/".join(f"({b})" for b in of_role("conditions"))
    if r["bullets"] & COND:
        cs = [] if r["conditions"] == "none stated" else ids(r["conditions"])
        if not cs and r["conditions"] != "none stated":
            err(f"{r['platform']}/statements.tsv", sid, f"a statement under {under} names the statements it conditions")
        for c in cs:
            if c not in stmts or stmts[c]["platform"] != r["platform"] or not (stmts[c]["bullets"] & ASK):
                err(f"{r['platform']}/statements.tsv", sid,
                    f"conditions {c} is not one of its platform's statements under {one_of(of_role('ask'))}")
    elif r["conditions"]:
        err(f"{r['platform']}/statements.tsv", sid,
            f"conditions is only for statements under {under}" if COND else "this subject has no conditions bullet")
for plat in PLATFORMS:
    if not os.path.isdir(os.path.join(subj, plat)):
        continue
    stated = {b for r in stmts.values() if r["platform"] == plat for b in r["bullets"]}
    gapped = {g["bullet"] for g in gaps.values() if g["platform"] == plat}
    for b in of_role("ask", "conditions"):
        if b not in stated and b not in gapped:
            err(f"{plat}/gaps.tsv", b, f"bullet ({b}) is neither stated nor recorded as a gap")
    for end in of_role("end"):
        if end not in stated and end not in gapped:
            err(f"{plat}/statements.tsv", end, f"{end} is neither named by a statement nor recorded as a gap")
if stmts:
    with open(os.path.join(subj, "kinds.tsv"), "w", encoding="utf-8") as f:
        f.write("id\tkind\trule\n")
        for sid, (k, why) in kinds.items():
            f.write(f"{sid}\t{k}\t{why}\n")

# ---------- phase B ----------
vps = read(os.path.join(subj, "variation-points.tsv"), "variation-points.tsv")
var = read(os.path.join(subj, "variants.tsv"), "variants.tsv")
vp = {}
if vps is not None:
    unique("variation-points.tsv", vps, "vp_id", rf"^{SID}-VP-\d{{2}}$")
    vp = {v["vp_id"]: v for v in vps}
    if len(vps) > LIMITS["variation points"]:
        err("variation-points.tsv", "", f"{len(vps)} variation points: the brief says stop and report past "
                                        f"{LIMITS['variation points']}")
    kinds_seen = {}
    for v in vps:
        i = v["vp_id"]
        if " | " in v["x_words"]:
            # S-02's brief: under (c) and (f), x_words starts with the kind; two points never share a question and
            # a kind
            key = (v["bullet"], re.sub(r'"[^"]*"|“[^”]*”|«[^»]*»', '""', v["question"]).strip(),
                   v["x_words"].split(" | ")[0].strip())
            if key in kinds_seen:
                err("variation-points.tsv", i, f"shares its question and its kind '{key[2]}' with {kinds_seen[key]}")
            kinds_seen.setdefault(key, i)
        if v["bullet"] not in ASK:
            err("variation-points.tsv", i, f"bullet '{v['bullet']}' is not {one_of(of_role('ask'))}")
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
            elif v["bullet"] not in stmts[s]["bullets"] and not any(
                    set(BULLET_RD.get(nb, [])) & set(BULLET_RD.get(v["bullet"], []))
                    for nb in stmts[s]["bullets"] & NOPART):
                # a no-part statement (S-02's (g)) may raise a point of a question bullet of its own root decision
                err("variation-points.tsv", i, f"raised_by {s} is not under bullet {v['bullet']}")
if var is not None:
    unique("variants.tsv", var, "variant_id", rf"^{SID}-V-\d{{3,4}}$")
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
                if g in superseded:
                    err("variants.tsv", i, f"gap {g} was narrowed into {superseded[g]}: the row names the gap that replaced it")
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
            nopart = [x for x in ids(r["stmt_ids"])
                      if stmts.get(x, {}).get("bullets", set()) & NOPART and not stmts[x]["bullets"] & ASK]
            # a row resting only on no-part statements takes `answers` alone; a row that also holds other statements
            # lists every basis that holds (rule 5), `answers` among them, so that one answer stays one row (rule 4)
            if nopart and len(nopart) == len(ids(r["stmt_ids"])) and bs != ["answers"]:
                err("variants.tsv", i, f"a variant resting only on {'/'.join(f'({b})' for b in of_role('no-part'))} "
                                       "statements takes the basis 'answers' alone")
            elif nopart and "answers" not in bs:
                err("variants.tsv", i, f"a variant holding a {'/'.join(f'({b})' for b in of_role('no-part'))} "
                                       "statement has the basis 'answers' among its bases")
            sids = ids(r["stmt_ids"])
            if not sids:
                err("variants.tsv", i, "no stmt_ids")
            elif all(s in stmts for s in sids) and not any(stmts[s]["bullets"] & (ASK | NOPART) for s in sids):
                err("variants.tsv", i, f"a variant rests on a statement under {one_of(of_role('ask', 'no-part'))}; "
                                       f"the others are conditions or ends, not variants")
            for s in sids:
                if stmts.get(s, {}).get("platform") != plat:
                    err("variants.tsv", i, f"{s} is not one of {plat}'s statements")
            if sids and all(s in stmts for s in sids) and not any(contained(r["variant"], stmts[s]["statement"]) for s in sids):
                err("variants.tsv", i, "the variant is not a verbatim excerpt of any of its statements")
            if "takes its value per" in vp.get(r["vp_id"], {}).get("question", ""):
                # S-02's brief: under (f)'s "what X takes its value per", basis_evidence names what the value is
                # taken per, in one of a fixed set of phrases; an answer resting on (g) alone names "the whole store"
                named = [x for x in PER_PHRASES if x in r["basis_evidence"]]
                only_nopart = sids and all(stmts.get(x, {}).get("bullets", set()) & NOPART
                                           and not stmts[x]["bullets"] & ASK for x in sids if x in stmts)
                if not named:
                    err("variants.tsv", i, f"basis_evidence names none of {PER_PHRASES}")
                elif only_nopart and "the whole store" not in named:
                    err("variants.tsv", i, "an answer resting on a statement that a setting holds for the whole "
                                           "store names 'the whole store' in basis_evidence")
            elif any(BULLET_RD.values()) and sids and all(
                    stmts.get(x, {}).get("bullets", set()) & NOPART and not stmts[x]["bullets"] & ASK
                    for x in sids if x in stmts) and "no market" not in r["basis_evidence"] \
                    and not re.match(r"(?i)^who\b", vp.get(r["vp_id"], {}).get("question", "")):
                # a no-part statement that names who sets a whole-store setting answers that setting's "who" point
                # S-02's brief: an answer resting only on a no-part statement either says the platform has no market
                # of the kind asked about ("no market"), or that a setting holds for the whole store, under a "takes
                # its value per" point
                err("variants.tsv", i, "an answer resting only on a no-part statement names 'no market' in "
                                       "basis_evidence, or goes under a 'takes its value per' point as 'the whole store'")
            want = sorted({k for s in sids if s in kinds for k in kinds[s][0].split(";") if k})
            got = sorted({k.strip() for k in r["kind"].split(";") if k.strip()})
            if want and got != want:
                err("variants.tsv", i, f"kind '{r['kind']}' differs from kinds.tsv's {';'.join(want)}")
    for v in vp:
        for p in PLATFORMS:
            if os.path.isdir(os.path.join(subj, p)) and (v, p) not in seen:
                err("variants.tsv", f"{v}/{p}", "no row for this variation point and platform")
    rows_of = {}
    for r in var:
        rows_of.setdefault((r["vp_id"], r["platform"]), []).append(r)
    for (v, p), rs in rows_of.items():
        if len(rs) > 1:
            for r in rs:
                if r["variant"] == "not covered":
                    err("variants.tsv", r["variant_id"], f"'not covered' says {p} has no row of its own here, but "
                                                         f"{len(rs) - 1} other row(s) of {v} are {p}'s: replace it")
    if not any(BULLET_RD.values()):        # the pilot: one question, so one count
        placed = {s for r in var for s in ids(r["stmt_ids"])}
        unplaced = [s for s in stmts if s not in placed and stmts[s]["bullets"] & (ASK | NOPART)]
        if unplaced:
            err("variants.tsv", "", f"{len(unplaced)} statements under bullets {one_of(of_role('ask', 'no-part'))} "
                                    f"are under no variation point: "
                                    f"{', '.join(unplaced[:12])}", "review")
    else:
        # Each root decision places every statement, under each of its question or no-part bullets the statement
        # carries: in a variant of one of its variation points of that bullet (a no-part statement, of any of its
        # variation points), or named in notes-b.md under the decision's own heading ("# RDn") as its id followed by
        # the bullet, such as "S02-SA-011 (b)", with a reason.
        placed = defaultdict(set)                          # (root decision, bullet) -> stmt_ids
        for r in var:
            b = vp.get(r["vp_id"], {}).get("bullet", "")
            for rd in BULLET_RD.get(b, []):
                placed[(rd, b)].update(ids(r["stmt_ids"]))
                for nb in NOPART:
                    if rd in BULLET_RD.get(nb, []):
                        placed[(rd, nb)].update(ids(r["stmt_ids"]))
        rd_now, nb_path = "", os.path.join(subj, "notes-b.md")
        for line in (open(nb_path, encoding="utf-8").read().split("\n") if os.path.exists(nb_path) else []):
            h = re.match(r"^#\s+(RD\d+)\b", line)
            if h:
                rd_now = h.group(1)
            elif rd_now:
                # only a line that starts with its ids and their bullets is a note: "- S02-SA-011 (b): reason"
                m = re.match(rf"^\s*[-*]?\s*((?:{SID}-[A-Z]{{2}}-\d{{3,4}}\s*,\s*)*{SID}-[A-Z]{{2}}-\d{{3,4}})"
                             rf"\s*\(([a-z](?:\s*[,;]\s*[a-z])*)\)", line)
                if m:
                    for sid in re.findall(rf"{SID}-[A-Z]{{2}}-\d{{3,4}}", m.group(1)):
                        for b in re.split(r"\s*[,;]\s*", m.group(2)):
                            placed[(rd_now, b)].add(sid)
        rows_out = []
        for sid, st in stmts.items():
            for b in sorted(st["bullets"] & (ASK | NOPART)):
                for rd in BULLET_RD.get(b, []):
                    if sid not in placed[(rd, b)]:
                        rows_out.append((rd, sid, b, st["platform"]))
        rows_out = sorted(set(rows_out))
        with open(os.path.join(OUT, "unplaced.tsv"), "w", encoding="utf-8") as f:
            f.write("root_decision\tstmt_id\tbullet\tplatform\n" + "".join("\t".join(r) + "\n" for r in rows_out))
        for rd in sorted({r[0] for r in rows_out}):
            mine = [r for r in rows_out if r[0] == rd]
            err("variants.tsv", rd, f"{len(mine)} of {rd}'s statements, by bullet, are neither in one of its "
                                    f"variants nor noted under its heading in notes-b.md (all in unplaced.tsv): "
                                    f"{', '.join(f'{r[1]} ({r[2]})' for r in mine[:8])}", "review")
# b/ranges.tsv gives each root decision its variation points' numbers; a copy checked with some root decisions only
# (phase B's "Before you finish") holds the others' points nowhere, so their a2.tsv rows aren't flagged there
_ranges = read(os.path.join(subj, "b", "ranges.tsv"), "b/ranges.tsv", check_head=False) or []
def rd_of_vp(v):
    m = re.search(r"-VP-(\d+)$", v or "")
    for r in _ranges:
        if m and int(r["vp_from"]) <= int(m.group(1)) <= int(r["vp_to"]):
            return r["root_decision"]
    return None if _ranges else "all"
rds_present = {rd_of_vp(v) for v in (vp or {})} | ({"all"} if not _ranges else set())
for plat in PLATFORMS:
    a2 = read(os.path.join(subj, plat, "a2.tsv"), f"{plat}/a2.tsv")
    later = read_later(plat)
    for r in a2 or []:
        # a row whose vp_id is `none` holds a lead's statements, or a gap under (h), that answer no variation point
        if vp and r["vp_id"] != "none" and r["vp_id"] not in vp \
                and rd_of_vp(r["vp_id"]) in rds_present:   # checked where its root decision's points are present
            err(f"{plat}/a2.tsv", r["vp_id"], "not a variation point")
        for s in ids(r["stmt_ids"]):
            if s not in stmts:
                err(f"{plat}/a2.tsv", r["vp_id"], f"{s} is not a statement")
        for g in ids(r["gap_ids"]):
            if g not in gaps:
                err(f"{plat}/a2.tsv", r["vp_id"], f"{g} is not a gap")
                continue
            route = [(u, [h for h in HELD.lookup(u) if h["readable"]]) for u in urls_in(gaps[g]["route"])]
            if gaps[g]["gap_kind"] == "page not read" and route and all(h and was_read(h, later) for u, h in route):
                err(f"{plat}/a2.tsv", r["vp_id"], f"{g} remains, but every page it waited on has been read: "
                                                  "record what they state, or a new gap listing what was read")
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
        if not parts or not all(re.match(r"^(\w+)\s*=\s*((A|B|C)(\+(A|B|C))*|D|unknown)$", x) and x.split("=")[0].strip() in PLATFORMS
                                for x in parts):
            err("analysis.tsv", v, f"coexistence '{r['coexistence']}' is not letters per platform, as 'shopify=A+B; salla=D'")
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
bears = read(os.path.join(subj, "bears-on.tsv"), "bears-on.tsv")
marks = read(os.path.join(subj, "yemen-marks.tsv"), "yemen-marks.tsv")
if marks is not None or bears is not None:
    yc = os.path.join(SKM, "studies/yemen-cases")
    cases = {r["case_id"]: r for r in (read(os.path.join(yc, "cases.tsv"), "cases.tsv", False) or [])}
    axes_y = {r["axis_id"]: r for r in (read(os.path.join(yc, "axes.tsv"), "axes.tsv", False) or [])}
    consts_y = {r["constant_id"]: r for r in (read(os.path.join(yc, "constants.tsv"), "constants.tsv", False) or [])}
    ye = set(axes_y) | set(consts_y) | {r["cite_id"] for r in (read(os.path.join(yc, "citations.tsv"), "citations.tsv", False) or [])}
    ye.add("Q2")                             # the frame every case shares: the merchant sells in the Yemeni market
    # What each variation point bears on: a case that changes none of its axes carries YC-00's mark.
    bear = {}
    for b in (bears or []):
        v, ax, ks = b["vp_id"], set(ids(b["axis_ids"])), set(ids(b["constant_ids"]))
        if v not in vp:
            err("bears-on.tsv", v, "vp_id not in variation-points.tsv")
        for a in ax - set(axes_y):
            err("bears-on.tsv", v, f"{a} is not an axis in studies/yemen-cases/axes.tsv")
        for k in ks - set(consts_y):
            err("bears-on.tsv", v, f"{k} is not a constant in studies/yemen-cases/constants.tsv")
        if (ax or ks) and not b["basis"]:
            err("bears-on.tsv", v, "basis is empty: quote each condition and the state labels it is checked against")
        own = {y for a in ax & set(axes_y) for y in ids(re.sub(r"[^\[\]]*\[([^\]]*)\]", r"\1 ", axes_y[a]["states"]))}
        own |= {y for a in ax & set(axes_y) for y in ids(axes_y[a]["today_cite_ids"])}
        own |= {y for k in ks & set(consts_y) for y in ids(consts_y[k]["cite_ids"])}
        bear[v] = (ax, ax | ks | own)
    if marks is not None:
        for v in vp:
            if v not in bear:
                err("bears-on.tsv", v, "no row for this variation point: list the axes and constants its variants' conditions bear on")
    for r in (marks or []):
        key = f"{r['vp_id']}/{r['case_id']}"
        if r["vp_id"] not in vp:
            err("yemen-marks.tsv", key, "vp_id not in variation-points.tsv")
        if r["case_id"] not in cases:
            err("yemen-marks.tsv", key, "case_id not in studies/yemen-cases/cases.tsv")
        if r["mark"] not in MARKS:
            err("yemen-marks.tsv", key, f"mark '{r['mark']}' is not one of {sorted(MARKS)}")
        if r["mark"] not in ("unknown", "no placement") and r["variant_id"] not in variant_ids:
            err("yemen-marks.tsv", key, "the mark names the variant it used by variant_id")
        allowed = bear.get(r["vp_id"], (set(), None))[1]
        evidence = ids(r["case_evidence"]) + [y for e in r["per_variant"].split(";") for y in ids(e.partition("/")[2])]
        for y in evidence:
            if y not in ye:
                err("yemen-marks.tsv", key, f"case evidence {y} is not a Stage 1 id")
            elif allowed is not None and y not in allowed and y != "Q2":
                err("yemen-marks.tsv", key, f"case evidence {y} is not among the axes and constants bears-on.tsv lists for {r['vp_id']}, or their citations")
        if r["mark"] != "unknown":
            if not ids(r["condition_stmt_ids"]) or not ids(r["case_evidence"]):
                err("yemen-marks.tsv", key, "a mark other than unknown cites both the variant's condition and the case's evidence")
            vstmts = set()
            for x in (var or []):
                if x["variant_id"] == r["variant_id"]:
                    vstmts = set(ids(x["stmt_ids"]))
            for s_ in ids(r["condition_stmt_ids"]):
                if s_ not in stmts:
                    err("yemen-marks.tsv", key, f"condition {s_} is not a statement")
                elif vstmts and s_ not in vstmts:
                    st = stmts[s_]
                    linked = bool(st["bullets"] & COND) and (
                        set(ids(st["conditions"])) & vstmts or
                        (st["conditions"] == "none stated" and st["identifier"] and
                         any(st["identifier"] in stmts[v_]["statement"] or st["identifier"] in stmts[v_]["identifier"]
                             for v_ in vstmts if v_ in stmts)))
                    if not linked:
                        err("yemen-marks.tsv", key, f"condition {s_} is neither the variant's statement nor an (e) statement linked to it")
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
            answers = {x["variant_id"] for x in (var or []) if x["vp_id"] == r["vp_id"] and x["variant"] not in NON_ANSWERS}
            if answers - listed:
                err("yemen-marks.tsv", key, f"no placement shows no failure for {', '.join(sorted(answers - listed))}")
        if YEMEN_NAMES.search(r["product_gap"]):
            err("yemen-marks.tsv", key, "the product gap names Yemen or a place in it")
    if marks is not None:
        have = {(r["vp_id"], r["case_id"]) for r in marks}
        for v in vp:
            ax = bear.get(v, (set(), None))[0]
            for c, row in cases.items():
                named = {p_.split("=")[0].strip() for p_ in row["name"].split(";") if "=" in p_}
                if (c == "YC-00" or named & ax) and (v, c) not in have:
                    err("yemen-marks.tsv", f"{v}/{c}", "no mark for this variation point and case: it is YC-00, or changes an axis bears-on.tsv lists")

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
