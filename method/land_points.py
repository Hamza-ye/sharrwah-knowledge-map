#!/usr/bin/env python3
"""The subjects' variation points on the class's model (PLAN.md, Stage 4A, "The subjects' points"; the brief
studies/class-model/briefs/P-points.md).

  batches
        the batches the landing runs in, each with its points. Every point of each subject is in one batch.
  show --points ID[,ID...] [--top N] [--width N] [--variants N]
        what landing a point reads, in one view: its question and terms; the register rows that name it, with
        their answer or recommendation and status; the subject's own analysis of it (S-02's answers per key,
        S-01's analysis); its variants per platform, with how many of each platform's statements trace to the
        concern map; then its leads, ranked, each with the statements behind each route, the basis it rests on,
        and its cells' placements and readings, clipped (read a cell whole with `cell`)
  leads [--subjects S-01,S-02] [--points ID[,ID...]] [--top N]
        the ranked leads alone
  cell CAP_ID PLATFORM
        one cell whole: what it holds, its placements, terms and reading, each evidence row (supports, key, why),
        and the capability's slot fillers
  check [--batch NAME] [--final]
        a batch's file, studies/class-model/points/<batch>.tsv, against the subjects and the model; without
        --batch, every batch's file. A draft's outcomes are empty. --final, for the coordinator's pass, requires an
        outcome for each conflict, and each outcome of a form its conflict's rows allow. Then, for each landed
        point and each platform whose statements the subject holds, where none of the point's capabilities holds
        a cell with statements on that platform: a lead to read, not a conflict.

A lead is never an answer. Its routes, and what a statement weighs in the ranking (each statement counted once for
each capability and route):
  cited    a cell cites the concern map's statement the subject's statement comes from, by its concern and its
           citation (3)
  concern  that statement's concern lands in the capability (2)
  page     the subject read its statement on a page that the concern map's statements of a concern also cite, at
           another locator, and the concern lands in the capability (1 over the page's number of concerns). A page
           with more than three concerns, or a collection file (.json, .jsonl, .js), gives no page lead: it is a
           corpus, not a page. Shopify's help pages held in observed-sh read as their help.shopify.com address,
           and Salla's help articles held in observed-sa as the article the concern map cites
  terms    the capability's name, note or cells' terms hold one of the point's own terms (1 a term)

points/<batch>.tsv (tab-separated, a header row, no quoting; the brief defines each field):
  subject · vp_id · question · cap_ids · reach · route · basis · reading · register · conflict · status · outcome

Run with python3 -I from the repository's root.
"""
import argparse, collections, os, re, signal, subprocess, sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import CMAP, MODEL, PLATFORMS, PREFIX, PART_ORDER, rows, fold, hits, first_cite

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJ = os.path.join(ROOT, "studies", "subjects")
OUT = os.path.join(MODEL, "points")
# The subjects whose points land now: S-01 and S-02 have ended. Each later subject's points land as it ends
# (PLAN.md, Stage 4A), with its batches added here.
SUBJECTS = ("S-01", "S-02")
# Each batch small enough that a drafter's context stays well under 200,000 tokens, with each "what X takes its
# value per" beside its "who sets X".
BATCHES = {
    "P-1": ("S-01", list(range(1, 11))),
    "P-2": ("S-01", list(range(11, 24))),
    "P-3": ("S-02", list(range(1, 13))),
    "P-4": ("S-02", list(range(13, 20)) + list(range(26, 30))),
    "P-5": ("S-02", list(range(41, 55))),
    "P-6": ("S-02", list(range(55, 69))),
    "P-7": ("S-02", list(range(69, 77)) + [78, 79, 84]),
    "P-8": ("S-02", [77, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92]),
}
HEAD = ["subject", "vp_id", "question", "cap_ids", "reach", "route", "basis", "reading", "register", "conflict",
        "status", "outcome"]
ROUTES = ("cited", "concern", "page", "terms")
WEIGHT = {"cited": 3, "concern": 2, "page": 1, "terms": 1}
CONFLICTS = ("count", "placement", "structure", "premise")
STATUS = ("landed", "conflict")
# The decisions that cut across every area, as the architecture plan's section 3 names them.
CROSS = ("how stores are kept apart", "identity and permissions", "money records and currency",
         "markets and the seller's country", "events and extension points", "configuration")
REACH = re.compile(r"^(capability|cross-cutting: (" + "|".join(re.escape(c) for c in CROSS) + r"))$")
CONFLICT = re.compile(r"^(count|placement|structure|premise) \(rows: ([^)]+)\): (\S.*)$")
CONFLICT_SPLIT = re.compile(r"\s*\|\s*(?=[\w-]+ \(rows:)")      # a | inside a conflict's text stays in it
OUTCOMES = ("model amended", "re-ruled", "to the founder with plans", "to the founder", "carried to", "re-applied",
            "dismissed", "kept open")
OUTCOME = re.compile(r"^(model amended: \S+/\S+ \S.*|re-ruled: (\S+), listed for veto|carried to (S-\d\d): \S.*|"
                     r"re-applied: (\S+)|to the founder: \S.*|to the founder with plans: \S.*|dismissed: \S.*|"
                     r"kept open: \S.*) \(the coordinator\)$")
OUTCOME_SPLIT = re.compile(r"\s*\|\s*(?=(?:" + "|".join(re.escape(o) for o in OUTCOMES) + r")\b)")
VP = re.compile(r"S\d\d-VP-\d+")
KEY = re.compile(r"^[A-Z]{2}-(C-\d{3}/[a-z]+/[A-Z]{2}-[SI]-\d{4}|I-\d{4})$")
DATA = ("capabilities.tsv", "landings.tsv", "cells.tsv", "evidence.tsv")


def split(s):
    return [x for x in re.split(r"[;,]\s*|\s+", s or "") if x]


def semi(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


def git(*args):
    try:
        return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception:
        return ""


def git_time(paths):
    out = git("log", "-1", "--format=%ct", "--", *paths)
    return int(out) if out else 0


# --- the model: merged where merged, a domain's parts in their order where it isn't ---------------------------

_model = None


def model():
    global _model
    if _model:
        return _model
    merged = os.path.join(MODEL, "merged")
    caps = {r["cap_id"]: r for r in rows(os.path.join(merged, "capabilities.tsv"))}
    land = {(r["platform"], r["concern_id"]): r["cap_id"] for r in rows(os.path.join(merged, "landings.tsv"))}
    cells = {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(merged, "cells.tsv"))}
    evrows = rows(os.path.join(merged, "evidence.tsv"))
    fillers = rows(os.path.join(merged, "slot-fillers.tsv"))
    done = {r["domain"] for r in caps.values()}
    base = os.path.join(MODEL, "parts")
    parts = [d for d in (os.listdir(base) if os.path.isdir(base) else []) if "-" in d]
    order = {p: i for i, p in enumerate(PART_ORDER)}
    parts.sort(key=lambda d: (d.split("-")[0], order.get(d.split("-", 1)[1], 99)))
    mt = git_time([os.path.relpath(os.path.join(merged, f), ROOT) for f in DATA])
    for d in parts:
        dom = d.split("-")[0]
        if dom in done:
            data = [os.path.relpath(os.path.join(base, d, f), ROOT) for f in DATA]
            if (mt and git_time(data) > mt) or git("status", "--porcelain", "--", *data):
                print(f"warning: {d}'s model files changed after the last merge: stop, and tell the coordinator to "
                      f"merge again before landing on domain {dom}", file=sys.stderr)
            continue
        for r in rows(os.path.join(base, d, "capabilities.tsv")):
            caps.setdefault(r["cap_id"], dict(r, domain=dom))
        for r in rows(os.path.join(base, d, "landings.tsv")):
            land[(r["platform"], r["concern_id"])] = r["cap_id"]
        placed = {(r["cap_id"], r["platform"]): r["placed_as"] for r in rows(os.path.join(base, d, "derived.tsv"))}
        for r in rows(os.path.join(base, d, "cells.tsv")):
            cells[(r["cap_id"], r["platform"])] = dict(r, placed_as=placed.get((r["cap_id"], r["platform"]), ""))
        evrows += rows(os.path.join(base, d, "evidence.tsv"))
        fillers += rows(os.path.join(base, d, "slot-fillers.tsv"))
    ev_by_key = collections.defaultdict(set)          # a statement's key -> the capabilities whose cells cite it
    ev_by_cell = collections.defaultdict(list)        # (cap, platform) -> evidence rows
    for r in evrows:
        ev_by_key[r["key"]].add(r["cap_id"])
        ev_by_cell[(r["cap_id"], r["platform"])].append(r)
    by_cap = collections.defaultdict(list)
    for r in fillers:
        by_cap[r.get("cap_id", "")].append(r)
    kinds = {r["cap_id"]: r for r in rows(os.path.join(merged, "kinds.tsv"))}
    _model = dict(caps=caps, land=land, cells=cells, ev_by_key=ev_by_key, ev_by_cell=ev_by_cell, kinds=kinds,
                  merged=done, fillers=by_cap)
    return _model


# --- the concern map's statements, by citation and by page ------------------------------------------------------

def norm_source(source, locator=""):
    """A source as a page: Shopify's help held in observed-sh as its address, Salla's help held in observed-sa as the
    article the concern map cites (its id), other held files without their commit, addresses without scheme or www."""
    s = source.strip()
    m = re.search(r"structures/shopify/help-center/help\.shopify\.com@[^/]+/md/(.+)$", s)
    if m:
        return "help.shopify.com/" + re.sub(r"\.md$", "", m.group(1)).casefold()
    a = re.search(r"\barticle ([0-9a-z]{16,})", locator or "")
    if re.search(r"help-articles/[a-z]+/texts\.jsonl$", s) and a:
        return "salla-help:" + a.group(1)
    m = re.match(r"https?://help\.salla\.sa/article/[^/]+/([0-9a-z]{16,})", s)
    if m:
        return "salla-help:" + m.group(1)
    m = re.match(r"(observed-s[ha]|other-product-class)@[0-9a-f]+:(.*)", s)
    if m:
        return f"{m.group(1)}:{m.group(2)}"
    s = re.sub(r"^https?://", "", s).split("#")[0].rstrip("/")
    s = re.sub(r"^www\.", "", s)
    if s.startswith("help.shopify.com/"):
        s = re.sub(r"\.md$", "", s)
    return s.casefold()


def norm_loc(s):
    return " ".join(fold(s).split())


def collection(src):
    return re.search(r"\.(json|jsonl|js)$", src) is not None


_cmap = {}


def cmap(platform):
    """cite id -> [(concern, key)]; (page, locator) -> cite ids; page -> concerns; every concern's id; every key."""
    if platform in _cmap:
        return _cmap[platform]
    d = os.path.join(CMAP, "platforms", platform)
    by_cite = collections.defaultdict(list)
    keys = set()
    for r in rows(os.path.join(d, "statements.tsv")):
        k = f"{r['concern_id']}/{r['placement']}/{first_cite(r['cite_ids'])}"
        keys.add(k)
        for c in split(r["cite_ids"]):
            by_cite[c].append((r["concern_id"], k))
    for r in rows(os.path.join(d, "inventory.tsv")):
        cs = split(r.get("concern_ids", ""))
        if cs and not r.get("out_of_scope_reason", "").strip():
            keys.add(r["inv_id"])
            for c in cs:
                by_cite[r["inv_id"]].append((c, r["inv_id"]))
    by_loc, by_page = collections.defaultdict(set), collections.defaultdict(set)
    for r in rows(os.path.join(d, "citations.tsv")):
        if r["cite_id"] not in by_cite:
            continue
        src = norm_source(r["source"], r["locator"])
        by_loc[(src, norm_loc(r["locator"]))].add(r["cite_id"])
        by_page[src].update(c for c, _ in by_cite[r["cite_id"]])
    concerns = {r["concern_id"] for r in rows(os.path.join(d, "concerns.tsv"))}
    _cmap[platform] = (by_cite, by_loc, by_page, concerns, keys)
    return _cmap[platform]


def all_concerns():
    return set().union(*(cmap(p)[3] for p in PLATFORMS))


def all_keys():
    return set().union(*(cmap(p)[4] for p in PLATFORMS))


# --- the subjects ----------------------------------------------------------------------------------------------

_subj = {}


def subject(s):
    """(points, variants by point, register rows by point, statements and citations by platform)."""
    if s in _subj:
        return _subj[s]
    vps = rows(os.path.join(SUBJ, s, "variation-points.tsv"))
    var = collections.defaultdict(list)
    for r in rows(os.path.join(SUBJ, s, "variants.tsv")):
        var[r["vp_id"]].append(r)
    reg = collections.defaultdict(list)
    for r in rows(os.path.join(SUBJ, s, "register.tsv")):
        for v in VP.findall(r.get("vp_id", "")):
            if r["id"] not in reg[v]:
                reg[v].append(r["id"])
    st = {}
    for p in PLATFORMS:
        d = os.path.join(SUBJ, s, p)
        stmts = {r["stmt_id"]: (r.get("from", "").strip(), split(r.get("cite_ids", "")))
                 for r in rows(os.path.join(d, "statements.tsv"))}
        cites = {}
        for f in ("citations.tsv", "recorded-citations.tsv"):
            for r in rows(os.path.join(d, f)):
                cites[r["cite_id"]] = (norm_source(r["source"], r["locator"]), norm_loc(r["locator"]))
        st[p] = (stmts, cites)
    _subj[s] = (vps, var, reg, st)
    return _subj[s]


def register_rows(s):
    return {r["id"]: r for r in rows(os.path.join(SUBJ, s, "register.tsv"))}


def owner(r):
    """Whose a register row is: founder, engineering, moved (with its subject, if named), rule, or other."""
    kind, status = r.get("kind", ""), r.get("status", "")
    if kind == "moved":
        m = re.search(r"moved to (S-\d\d)", status)
        return ("moved", m.group(1) if m else None)
    if kind == "follows by rule":
        return ("rule", None)
    if "engineering" in status:
        return ("engineering", None)
    if re.search(r"by the founder|founder's, in force|Decision 1's answer", status):
        return ("founder", None)
    return ("other", None)


def subject_of(vp):
    m = re.match(r"S(\d\d)-VP-\d+$", vp)
    return f"S-{m.group(1)}" if m else None


def trace(s, platform, sid, depth=0):
    """A subject's statement -> [("statement", concern, key)] for the concern map's statements it is, or
    [("page", concern, page, n)] for the concerns of a page it was read on."""
    _, _, _, st = subject(s)
    stmts, cites = st[platform]
    if sid not in stmts:
        return []
    frm, cids = stmts[sid]
    by_cite, by_loc, by_page, _, _ = cmap(platform)
    m = re.match(r"index:([A-Z]{2}-C-\d+):(\S+)", frm)
    if m:
        con, cite = m.groups()
        keys = sorted({k for c, k in by_cite.get(cite, []) if c == con})
        return [("statement", con, k) for k in keys] or [("statement", con, None)]
    m = re.match(r"S(\d\d)-[A-Z]{2}-\d+$", frm)
    if m and depth < 3:   # a statement copied from an earlier subject
        return trace(f"S-{m.group(1)}", platform, frm, depth + 1)
    out = []
    for c in cids:
        if c not in cites:
            continue
        src, loc = cites[c]
        hit = by_loc.get((src, loc))
        if hit:
            for cc in sorted(hit):
                out += [("statement", con, k) for con, k in by_cite[cc]]
        elif src in by_page and not collection(src) and len(by_page[src]) <= 3:
            n = len(by_page[src])
            out += [("page", con, src, n) for con in sorted(by_page[src])]
    return out


def point_terms(vp_row):
    """The point's own terms: its head term and each platform's, without quotes or annotations."""
    out = []
    for part in (vp_row.get("x_words") or "").split("|"):
        part = part.strip()
        m = re.match(r"(shopify|salla|zid|woocommerce|bigcommerce):\s*(.*)$", part, re.S)
        body = m.group(2) if m else part
        for w in re.split(r";|\s/\s", body):
            w = re.sub(r"\([^)]*\)", "", w)
            w = w.strip().strip('"“”\'').strip()
            if 3 <= len(w) <= 60:
                out.append(w)
    seen, terms = set(), []
    for t in out:
        if fold(t) not in seen:
            seen.add(fold(t))
            terms.append(t)
    return terms


def point_leads(s, vp):
    """capability -> route -> platform -> the subject's statements on that route (each once); a page statement's
    weight; capability -> basis items; pages per capability; statements and traced statements per platform; the
    point's terms."""
    m = model()
    vps, var, _, _ = subject(s)
    hit = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(set)))
    pw = collections.defaultdict(dict)                 # (cap, platform) -> statement -> page weight
    basis = collections.defaultdict(set)
    pages = collections.defaultdict(set)
    n, traced = collections.Counter(), collections.Counter()
    seen = set()
    for v in var.get(vp, []):
        p = v["platform"]
        for sid in split(v["stmt_ids"]):
            if (p, sid) in seen:
                continue
            seen.add((p, sid))
            n[p] += 1
            hs = trace(s, p, sid)
            if hs:
                traced[p] += 1
            for h in hs:
                if h[0] == "statement":
                    _, con, k = h
                    for c in (m["ev_by_key"].get(k, ()) if k else ()):
                        hit[c]["cited"][p].add(sid)
                        basis[c].add(k)
                    cap = m["land"].get((p, con))
                    if cap:
                        hit[cap]["concern"][p].add(sid)
                        basis[cap].add(f"concern:{con}")
                else:
                    _, con, src, cnt = h
                    cap = m["land"].get((p, con))
                    if cap:
                        hit[cap]["page"][p].add(sid)
                        pw[(cap, p)][sid] = max(pw[(cap, p)].get(sid, 0), 1 / cnt)
                        basis[cap].add(f"concern:{con}")
                        pages[cap].add((src, cnt))
    row = next(r for r in vps if r["vp_id"] == vp)
    terms = point_terms(row)
    cellterms = collections.defaultdict(list)
    for (cid, _p), r in m["cells"].items():
        cellterms[cid].append(r.get("terms", ""))
    termhits = collections.defaultdict(set)
    for cid, r in m["caps"].items():
        h = fold(" ".join([r.get("capability", ""), r.get("note", "")] + cellterms.get(cid, [])))
        for t in terms:
            if hits(fold(t), h):
                termhits[cid].add(t)
                basis[cid].add(f"term:{t}")
    score = {}
    for c in set(hit) | set(termhits):
        sc = 0.0
        for rt, byp in hit[c].items():
            for p, ss in byp.items():
                sc += sum(pw[(c, p)].values()) if rt == "page" else WEIGHT[rt] * len(ss)
        score[c] = sc + WEIGHT["terms"] * len(termhits[c])
    return dict(hit=hit, termhits=termhits, score=score, basis=basis, pages=pages, n=n, traced=traced, terms=terms)


def placements(cid):
    m = model()
    return " ".join(f"{PREFIX[p]}:{(m['cells'].get((cid, p)) or {}).get('placed_as') or '-'}" for p in PLATFORMS)


def cap_line(cid):
    m = model()
    r = m["caps"].get(cid, {})
    k = m["kinds"].get(cid, {})
    dom = r.get("domain") or "?"
    kind = f"{k.get('kind', '')} {k.get('count', '')}".strip() or ("(not merged)" if dom not in m["merged"] else "")
    return f"{cid} [{dom} {r.get('area', '')}] {r.get('capability', '')[:90]} | {kind} | {placements(cid)}"


def route_line(L, c):
    out = []
    for rt in ROUTES[:3]:
        byp = L["hit"][c].get(rt) if c in L["hit"] else None
        if byp:
            out.append(f"{rt} " + ",".join(f"{PREFIX[p]}{len(byp[p])}" for p in PLATFORMS if byp.get(p)))
    if L["termhits"].get(c):
        out.append(f"terms {len(L['termhits'][c])}")
    return f"score {L['score'][c]:.3g}: " + "; ".join(out) + " (statements, each once; terms, each once)"


def clip(s, n):
    s = " ".join((s or "").split())
    return s if n <= 0 or len(s) <= n else s[:n] + " …"


def ranked(L, top):
    return sorted(L["score"], key=lambda c: (-L["score"][c], c))[:top]


def cmd_leads(a):
    subs = a.subjects.split(",") if a.subjects else list(SUBJECTS)
    want = set(split(a.points)) if a.points else None
    for s in subs:
        vps, _, reg, _ = subject(s)
        for r in vps:
            vp = r["vp_id"]
            if want and vp not in want:
                continue
            L = point_leads(s, vp)
            print(f"## {vp}\t{r['question']}\n   register: {', '.join(reg.get(vp, [])) or '(none)'}"
                  f"\n   statements traced: " + ", ".join(f"{PREFIX[p]} {L['traced'][p]}/{L['n'][p]}"
                                                       for p in PLATFORMS if L["n"][p]))
            for c in ranked(L, a.top):
                print(f"   {cap_line(c)}\n      ({route_line(L, c)})")
            print()


def cmd_show(a):
    m = model()
    for vp in split(a.points):
        s = subject_of(vp)
        if s not in SUBJECTS:
            sys.exit(f"{vp}: not a point of {', '.join(SUBJECTS)}")
        vps, var, reg, _ = subject(s)
        r = next((x for x in vps if x["vp_id"] == vp), None)
        if not r:
            sys.exit(f"{vp}: no such point")
        L = point_leads(s, vp)
        print(f"## {vp}\t{r['question']}\n   terms: {clip('; '.join(L['terms']), a.width)}")
        regs = register_rows(s)
        for rid in reg.get(vp, []):
            x = regs[rid]
            ans = x.get("recommendation") or x.get("answer") or ""
            print(f"   register {rid} [{x['kind']}; {clip(x.get('status', ''), 90)}]: {clip(x['question'], 120)}"
                  f"\n      -> {clip(ans, a.width)}")
        if s == "S-02":
            for x in rows(os.path.join(SUBJ, s, "answers.tsv")):
                if x["vp_id"] == vp:
                    print(f"   answer '{clip(x['key'], 60)}': gives {x['gives'] or '-'}; lacks {x['lacks'] or '-'}; "
                          f"open {x['open'] or '-'}; not stated {x['not_stated'] or '-'}; {x['cause']}"
                          + (f"\n      {clip(x['cause_reading'], a.width)}" if x["cause_reading"] else ""))
        else:
            for x in rows(os.path.join(SUBJ, s, "analysis.tsv")):
                if x["vp_id"] == vp:
                    print(f"   analysis: {x['cause']}; compared: {clip(x['scopes_compared'], 200)}"
                          f"\n      {clip(x['cause_reading'], a.width * 2)}")
        byp = collections.defaultdict(list)
        for v in var.get(vp, []):
            byp[v["platform"]].append(v)
        for p in PLATFORMS:
            vs = byp.get(p, [])
            if not vs:
                continue
            print(f"   {p}: {len(vs)} variants, {L['traced'][p]} of {L['n'][p]} statements traced to the concern map")
            for v in vs[:a.variants]:
                k = len(split(v["stmt_ids"]))
                extra = "".join([f"; absences {v['absence_ids']}" if v["absence_ids"] else "",
                                 f"; gaps {v['gap_ids']}" if v["gap_ids"] else ""])
                print(f"      {v['variant_id']} {clip(v['variant'], 110)} [{v['kind'] or '-'}; {k} statements{extra}]")
            if len(vs) > a.variants:
                print(f"      (+{len(vs) - a.variants} more: studies/subjects/{s}/variants.tsv)")
        print("   leads:")
        for c in ranked(L, a.top):
            b = sorted(L["basis"][c], key=lambda x: (x.startswith("term:"), x.startswith("concern:"), x))
            print(f"   {cap_line(c)}\n      ({route_line(L, c)})\n      basis: {'; '.join(b[:8])}"
                  + (f" (+{len(b) - 8} more)" if len(b) > 8 else ""))
            for src, cnt in sorted(L["pages"][c])[:3]:
                print(f"      page: {clip(src, 110)} ({cnt} concerns)")
            for p in PLATFORMS:
                cell = m["cells"].get((c, p))
                if cell and cell.get("held") != "none-held":
                    print(f"      {PREFIX[p]} {cell.get('placed_as') or '-'}: {clip(cell.get('reading', ''), a.width)}")
        none = [p for p in PLATFORMS if L["n"][p] and not L["traced"][p]]
        if none:
            print(f"   nothing traced on {', '.join(none)}: search for it (class_slice.py caps, search) before you land")
        print()


def cmd_cell(a):
    m = model()
    cid, p = a.cap_id, a.platform
    if cid not in m["caps"]:
        sys.exit(f"{cid}: no capability of the model")
    print(cap_line(cid))
    print(f"   note: {m['caps'][cid].get('note', '')}")
    cell = m["cells"].get((cid, p))
    if not cell:
        print(f"   {p}: no cell")
    else:
        print(f"   {p}: held {cell.get('held')}; placed {cell.get('placed_as') or '-'}\n   terms: {cell.get('terms', '')}")
        if cell.get("searched"):
            print(f"   searched: {cell['searched']}")
        print(f"   reading: {cell.get('reading', '')}")
        for e in m["ev_by_cell"].get((cid, p), []):
            print(f"   {e['supports']}\t{e['key']}\t{e['why']}")
    for f in m["fillers"].get(cid, []):
        print(f"   slot filler on {f.get('platform', '')}: {' · '.join(v for k, v in f.items() if k not in ('cap_id', 'platform', 'part') and v)}")


# --- batches and the check ---------------------------------------------------------------------------------------

def batch_points(name):
    s, nums = BATCHES[name]
    vps, _, _, _ = subject(s)
    have = {int(r["vp_id"].rsplit("-", 1)[1]): r["vp_id"] for r in vps}
    return s, [have[i] for i in nums if i in have]


def batch_problems():
    """Every point of each subject in exactly one batch, and every number a batch names a point."""
    probs = []
    for s in SUBJECTS:
        vps, _, _, _ = subject(s)
        nums = {int(r["vp_id"].rsplit("-", 1)[1]) for r in vps}
        placed = collections.Counter(i for bs, ns in BATCHES.values() if bs == s for i in ns)
        for i in sorted(nums):
            if placed[i] != 1:
                probs.append(f"{s}: point {i} is in {placed[i]} batches, not one")
        for i in sorted(set(placed) - nums):
            probs.append(f"{s}: a batch names point {i}, which the subject doesn't hold")
    return probs


def cmd_batches(a):
    for b in BATCHES:
        s, pts = batch_points(b)
        print(f"{b}\t{s}\t{len(pts)} points\t{','.join(pts)}")
    for p in batch_problems():
        print("PROBLEM", p)


def read_batch(path, probs, b):
    """The rows of one batch's file, its problems reported; a wrong header stops the batch."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        raw = f.read().split("\n")
    head = raw[0].rstrip("\r").split("\t")
    if head != HEAD:
        probs.append(f"{b}: header is {head}, not {HEAD}: fix it first")
        return []
    out = []
    for i, l in enumerate(raw[1:], 2):
        l = l.rstrip("\r")
        if not l.strip():
            continue
        f = l.split("\t")
        if len(f) != len(HEAD):
            probs.append(f"{b} line {i}: {len(f)} fields, not {len(HEAD)}: skipped")
            continue
        out.append(dict(zip(HEAD, f)))
    return out


def outcome_problems(w, o, rids, regs):
    """An outcome against the register rows its conflict names (the brief, "After the batches")."""
    mm = OUTCOME.match(o)
    if not mm:
        return [f"{w}: outcome '{o[:50]}' is not one of the coordinator's forms, marked (the coordinator)"]
    own = {r: owner(regs[r]) for r in rids if r in regs}
    if o.startswith("re-ruled:"):
        r = mm.group(2)
        if r not in own or own[r][0] != "engineering":
            return [f"{w}: re-ruled names {r}, which isn't an engineering row its conflict names"]
    elif o.startswith("to the founder with plans:"):
        if "S02-M9" not in rids:
            return [f"{w}: to the founder with plans is for a conflict on S02-M9"]
    elif o.startswith("to the founder:"):
        if not any(v[0] == "founder" for v in own.values()):
            return [f"{w}: to the founder needs a founder's row among its conflict's rows"]
    elif o.startswith("carried to"):
        sub = mm.group(3)
        if not any(v[0] == "moved" and v[1] in (None, sub) for v in own.values()):
            return [f"{w}: carried to {sub} needs a row moved there among its conflict's rows"]
    elif o.startswith("re-applied:"):
        r = mm.group(4)
        if r not in own or own[r][0] != "rule":
            return [f"{w}: re-applied names {r}, which isn't a follows-by-rule row its conflict names"]
    return []


def cmd_check(a):
    m = model()
    probs = batch_problems()
    names = [a.batch] if a.batch else list(BATCHES)
    if a.batch and a.batch not in BATCHES:
        sys.exit(f"no batch {a.batch}: {', '.join(BATCHES)}")
    have = []
    for b in names:
        path = os.path.join(OUT, f"{b}.tsv")
        if not os.path.exists(path):
            probs.append(f"{b}: no {os.path.relpath(path, ROOT)}")
            continue
        have += [(b, r) for r in read_batch(path, probs, b)]
    seen = collections.Counter((r["subject"], r["vp_id"]) for _, r in have)
    for b in names:
        s, pts = batch_points(b)
        for vp in pts:
            if seen[(s, vp)] != 1:
                probs.append(f"{b} {vp}: landed {seen[(s, vp)]} times, not once")
    known, keys = all_concerns(), all_keys()
    for b, r in have:
        s, vp = r["subject"], r["vp_id"]
        w = f"{b} {vp}"
        bs, pts = batch_points(b)
        if s != bs or vp not in pts:
            probs.append(f"{w}: not a point of batch {b}")
            continue
        vps, var, reg, _ = subject(s)
        regs = register_rows(s)
        row = next(x for x in vps if x["vp_id"] == vp)
        if r["question"] != row["question"]:
            probs.append(f"{w}: question differs from the subject's")
        cs = semi(r["cap_ids"])
        if not cs:
            probs.append(f"{w}: cap_ids empty (write none for a point no capability holds)")
        if "none" in cs and cs != ["none"]:
            probs.append(f"{w}: none stands alone in cap_ids")
        if len(set(cs)) != len(cs):
            probs.append(f"{w}: a capability is named twice")
        for c in cs:
            if c != "none" and c not in m["caps"]:
                probs.append(f"{w}: {c} is no capability of the model")
        caps = [c for c in cs if c != "none" and c in m["caps"]]
        if not REACH.match(r["reach"]):
            probs.append(f"{w}: reach is capability, or cross-cutting: <one of {'; '.join(CROSS)}>")
        routes = semi(r["route"])
        for rt in routes:
            if rt not in ROUTES:
                probs.append(f"{w}: route {rt} not one of {ROUTES}")
        if caps and not routes:
            probs.append(f"{w}: route empty")
        bas = semi(r["basis"])
        if not bas:
            probs.append(f"{w}: basis empty (for none, the leads you set aside)")
        terms = {fold(t) for t in point_terms(row)}
        ckeys = {e["key"] for (c2, _p), es in m["ev_by_cell"].items() if c2 in caps for e in es}
        kinds = collections.Counter()
        for x in bas:
            if x.startswith("concern:"):
                con = x[8:]
                pl = next((p for p, pre in PREFIX.items() if con.startswith(pre + "-")), None)
                ok = con in known and (not caps or m["land"].get((pl, con)) in caps)
                kinds["concern"] += ok
                if not ok:
                    probs.append(f"{w}: basis {x}: not a concern landed in {', '.join(caps) or 'the model'}")
                elif caps and not {"concern", "page"} & set(routes):
                    probs.append(f"{w}: basis {x} has no route concern or page")
            elif x.startswith("term:"):
                ok = fold(x[5:]) in terms
                kinds["term"] += ok
                if not ok:
                    probs.append(f"{w}: basis {x}: not among the point's terms")
                elif caps and "terms" not in routes:
                    probs.append(f"{w}: basis {x} has no route terms")
            else:
                ok = (x in ckeys) if caps else (bool(KEY.match(x)) and x in keys)
                kinds["key"] += ok
                if not ok:
                    probs.append(f"{w}: basis {x}: not a key a cell of {', '.join(caps) or 'the concern map'} holds")
                elif caps and "cited" not in routes:
                    probs.append(f"{w}: basis {x} has no route cited")
        for rt, need in (("cited", "key"), ("concern", "concern"), ("page", "concern"), ("terms", "term")):
            if rt in routes and not kinds[need]:
                probs.append(f"{w}: route {rt} has no basis item of its form ({need})")
        if not r["reading"].strip():
            probs.append(f"{w}: reading empty")
        rlist = reg.get(vp, [])
        if r["register"] != "; ".join(rlist):
            probs.append(f"{w}: register should be '{'; '.join(rlist)}'")
        con = r["conflict"].strip()
        parts = [x.strip() for x in CONFLICT_SPLIT.split(con)] if con and con != "none" else []
        if not con:
            probs.append(f"{w}: conflict empty (none, or <type> (rows: ...): <what>)")
        rows_of = []
        for x in parts:
            mm = CONFLICT.match(x)
            if not mm:
                probs.append(f"{w}: conflict '{x[:50]}' is not <type> (rows: <ids> or model): <what>, "
                             f"type one of {CONFLICTS}")
                rows_of.append([])
                continue
            rids = [y.strip() for y in mm.group(2).split(",") if y.strip()]
            rows_of.append(rids)
            for rid in rids:
                if rid != "model" and rid not in rlist:
                    probs.append(f"{w}: conflict names {rid}, which isn't one of the point's register rows")
        st = r["status"]
        if st not in STATUS:
            probs.append(f"{w}: status {st!r} not one of {STATUS}")
        elif (con == "none") != (st == "landed"):
            probs.append(f"{w}: status landed goes with conflict none, and conflict with a conflict")
        if cs == ["none"] and not any(x.startswith("structure") for x in parts):
            probs.append(f"{w}: a point no capability holds has a structure conflict")
        out = r["outcome"].strip()
        outs = [x.strip() for x in OUTCOME_SPLIT.split(out)] if out else []
        if outs and not a.final:
            probs.append(f"{w}: a draft's outcome is empty: the coordinator writes it, and checks with --final")
        if a.final:
            if parts and len(outs) != len(parts):
                probs.append(f"{w}: {len(outs)} outcomes for {len(parts)} conflicts (--final)")
            for o, rids in zip(outs, rows_of):
                probs += outcome_problems(w, o, rids, regs)
        for p in PLATFORMS:
            held = any(split(v["stmt_ids"]) for v in var.get(vp, []) if v["platform"] == p)
            if held and caps and not any((m["cells"].get((c, p)) or {}).get("held") == "statements" for c in caps):
                print(f"lead: {w}: the subject holds {p}'s statements; no cell of {', '.join(caps)} holds any on {p}")
    for p in probs:
        print("PROBLEM", p)
    print(f"# {len(have)} points in {', '.join(names)}, {len(probs)} problems")
    sys.exit(1 if probs else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("batches")
    s = sub.add_parser("show"); s.add_argument("--points", required=True); s.add_argument("--top", type=int, default=5)
    s.add_argument("--width", type=int, default=160); s.add_argument("--variants", type=int, default=20)
    s = sub.add_parser("leads"); s.add_argument("--subjects"); s.add_argument("--points"); s.add_argument("--top", type=int, default=6)
    s = sub.add_parser("cell"); s.add_argument("cap_id"); s.add_argument("platform", choices=PLATFORMS)
    s = sub.add_parser("check"); s.add_argument("--batch"); s.add_argument("--final", action="store_true")
    a = ap.parse_args()
    {"batches": cmd_batches, "show": cmd_show, "leads": cmd_leads, "cell": cmd_cell, "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    main()
