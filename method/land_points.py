#!/usr/bin/env python3
"""The subjects' variation points on the class's model (PLAN.md, Stage 4A, "The subjects' points").

  leads [--subjects S-01,S-02] [--points ID[,ID...]] [--top N]
        each point: its question, the register rows that name it, and the capabilities its statements point to,
        by three routes, strongest first:
          cited    a cell's evidence cites the concern map's statement the subject's statement comes from
          concern  the concern of that statement lands in the capability
          page     the subject's statement was read on a page (or file) that the concern map's statements of a
                   concern also cite, at another locator; the concern lands in the capability
        then the capabilities whose names, notes or cells' terms hold the point's own terms (x_words). Each
        capability with its domain, area and each platform's placement. A lead list, not an answer.
  show --points ID[,ID...] [--top N] [--width N]
        what landing a point reads, in one view: its question; the register rows that name it, with their answer
        or recommendation and status; the subject's own analysis of it (S-02's answers per key, S-01's analysis);
        its variants per platform; then its leads, each with its cells' placements and readings
  batches
        the batches the landing runs in, each with its points
  check [--batch NAME]
        studies/class-model/points/<batch>.tsv against the subjects and the model: each point of the batch landed
        once, its capabilities in the model, its register rows as the registers give them, its values legal.
        Without --batch, every batch's file, and every point of each subject landed once across them.
        Then, for each landed point and each platform, where the subject holds the platform's statements and the
        landing capability's cell on that platform holds none: a lead to read, not a conflict by itself.

points/<batch>.tsv (tab-separated, a header row, no quoting):
  subject · vp_id · question (as the subject words it) · cap_ids (`;`-separated, the first its main landing) ·
  route (`cited`, `concern`, `page`, `terms`, `;`-separated) · basis (the concern map's keys, `concern:<id>` or
  `term:<term>`, `;`-separated) · reading (why it lands there, a reading) · register (the register rows that name
  the point, as `check` computes them) · conflict (`none`, or `<type>: <what>`, the type one of `count`,
  `placement`, `structure`, `premise`; studies/class-model/briefs/P-points.md) · status (`landed` where the
  conflict is none; `reopened`, the model or an engineering ruling read again on the evidence; `to the founder`,
  where the conflict touches the founder's own decision)

A point that lands on no capability holds `none` in cap_ids, and its conflict says what the model lacks.
Run with python3 -I from the repository's root.
"""
import argparse, collections, os, re, signal, sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import CMAP, MODEL, PLATFORMS, PREFIX, rows, fold, hits, key, first_cite

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJ = os.path.join(ROOT, "studies", "subjects")
SUBJECTS = ("S-01", "S-02")
OUT = os.path.join(MODEL, "points")
BATCHES = {"P-1": ("S-01", 1, 23), "P-2": ("S-02", 1, 29), "P-3": ("S-02", 41, 66), "P-4": ("S-02", 67, 92)}
CONFLICTS = ("count", "placement", "structure", "premise")
HEAD = ["subject", "vp_id", "question", "cap_ids", "route", "basis", "reading", "register", "conflict", "status"]
ROUTES = ("cited", "concern", "page", "terms")
STATUS = ("landed", "reopened", "to the founder")


def split(s):
    return [x for x in re.split(r"[;,]\s*|\s+", s or "") if x]


# --- the model: merged where merged, the parts' own files for a domain not merged yet ---------------------------

_model = None


def model():
    global _model
    if _model:
        return _model
    merged = os.path.join(MODEL, "merged")
    caps = {r["cap_id"]: r for r in rows(os.path.join(merged, "capabilities.tsv"))}
    land = {(r["platform"], r["concern_id"]): r["cap_id"] for r in rows(os.path.join(merged, "landings.tsv"))}
    cells = {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(merged, "cells.tsv"))}
    ev = collections.defaultdict(set)   # concern map statement id -> cap_ids whose cells cite it
    for r in rows(os.path.join(merged, "evidence.tsv")):
        ev[r["key"].rsplit("/", 1)[-1]].add(r["cap_id"])
    done = {r["domain"] for r in caps.values()}
    base = os.path.join(MODEL, "parts")
    for d in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        if d.split("-")[0] in done:
            continue
        for r in rows(os.path.join(base, d, "capabilities.tsv")):
            caps.setdefault(r["cap_id"], dict(r, domain=d.split("-")[0]))
        for r in rows(os.path.join(base, d, "landings.tsv")):
            land[(r["platform"], r["concern_id"])] = r["cap_id"]
        placed = {(r["cap_id"], r["platform"]): r["placed_as"] for r in rows(os.path.join(base, d, "derived.tsv"))}
        for r in rows(os.path.join(base, d, "cells.tsv")):
            cells[(r["cap_id"], r["platform"])] = dict(r, placed_as=placed.get((r["cap_id"], r["platform"]), ""))
        for r in rows(os.path.join(base, d, "evidence.tsv")):
            ev[r["key"].rsplit("/", 1)[-1]].add(r["cap_id"])
    kinds = {r["cap_id"]: r for r in rows(os.path.join(merged, "kinds.tsv"))}
    _model = dict(caps=caps, land=land, cells=cells, ev=ev, kinds=kinds, merged=done)
    return _model


# --- the concern map's statements, by cite id and by page --------------------------------------------------------

def norm_source(s):
    s = s.strip()
    m = re.match(r"(observed-s[ha]|other-product-class)@[0-9a-f]+:(.*)", s)
    if m:
        return f"{m.group(1)}:{m.group(2)}"
    s = re.sub(r"^https?://", "", s).split("#")[0].rstrip("/")
    s = re.sub(r"^www\.", "", s)
    return s.casefold()


def norm_loc(s):
    return " ".join(fold(s).split())


_cmap = {}


def cmap(platform):
    """cite id -> concerns; (source, locator) -> cite ids; source -> concerns."""
    if platform in _cmap:
        return _cmap[platform]
    d = os.path.join(CMAP, "platforms", platform)
    by_cite = collections.defaultdict(set)
    for r in rows(os.path.join(d, "statements.tsv")):
        for c in split(r["cite_ids"]):
            by_cite[c].add(r["concern_id"])
    for r in rows(os.path.join(d, "inventory.tsv")):
        cs = split(r.get("concern_ids", ""))
        if cs and not r.get("out_of_scope_reason", "").strip():
            by_cite[r["inv_id"]].update(cs)
    by_loc, by_page = collections.defaultdict(set), collections.defaultdict(set)
    for r in rows(os.path.join(d, "citations.tsv")):
        if r["cite_id"] not in by_cite:
            continue
        src = norm_source(r["source"])
        by_loc[(src, norm_loc(r["locator"]))].add(r["cite_id"])
        by_page[src].update(by_cite[r["cite_id"]])
    _cmap[platform] = (by_cite, by_loc, by_page)
    return _cmap[platform]


# --- the subjects ----------------------------------------------------------------------------------------------

PLAT_OF = {v: k for k, v in PREFIX.items()}


def subject_statements(subject, platform):
    """stmt_id -> (from, cite_ids); with each cite id's (source, locator)."""
    d = os.path.join(SUBJ, subject, platform)
    st = {}
    for f in ("statements.tsv",):
        for r in rows(os.path.join(d, f)):
            st[r["stmt_id"]] = (r.get("from", "").strip(), split(r.get("cite_ids", "")))
    cites = {}
    for f in ("citations.tsv", "recorded-citations.tsv"):
        for r in rows(os.path.join(d, f)):
            cites[r["cite_id"]] = (norm_source(r["source"]), norm_loc(r["locator"]))
    return st, cites


_subj = {}


def subject(s):
    if s in _subj:
        return _subj[s]
    vps = rows(os.path.join(SUBJ, s, "variation-points.tsv"))
    var = collections.defaultdict(list)
    for r in rows(os.path.join(SUBJ, s, "variants.tsv")):
        var[r["vp_id"]].append(r)
    reg = collections.defaultdict(list)
    for r in rows(os.path.join(SUBJ, s, "register.tsv")):
        for v in re.findall(r"S0\d-VP-\d+", r.get("vp_id", "")):
            if r["id"] not in reg[v]:
                reg[v].append(r["id"])
    st = {p: subject_statements(s, p) for p in PLATFORMS}
    _subj[s] = (vps, var, reg, st)
    return _subj[s]


def trace(s, platform, sid, depth=0):
    """A subject's statement -> [(route, concern-map cite id or None, concern)]."""
    _, _, _, st = subject(s)
    stmts, cites = st[platform]
    if sid not in stmts:
        return []
    frm, cids = stmts[sid]
    by_cite, by_loc, by_page = cmap(platform)
    out = []
    m = re.match(r"index:([A-Z]{2}-C-\d+):(\S+)", frm)
    if m:
        return [("concern", m.group(2), m.group(1))]
    m = re.match(r"(S0\d)-[A-Z]{2}-\d+$", frm)
    if m and depth < 2:   # a statement copied from an earlier subject
        return trace(f"S-{m.group(1)[1:]}", platform, frm, depth + 1)
    for c in cids:
        if c not in cites:
            continue
        src, loc = cites[c]
        hit = by_loc.get((src, loc))
        if hit:
            for cc in hit:
                out += [("concern", cc, con) for con in sorted(by_cite[cc])]
        else:
            out += [("page", None, con) for con in sorted(by_page.get(src, ()))]
    return out


def point_leads(s, vp):
    """capability -> route -> platform -> count; and the statements traced."""
    m = model()
    _, var, _, _ = subject(s)
    leads = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    basis = collections.defaultdict(set)
    n, traced = 0, 0
    for v in var.get(vp, []):
        p = v["platform"]
        for sid in split(v["stmt_ids"]):
            n += 1
            hits_ = trace(s, p, sid)
            if hits_:
                traced += 1
            for route, cite, con in hits_:
                cap = m["land"].get((p, con))
                if route == "concern" and cite and m["ev"].get(cite):
                    for c in m["ev"][cite]:
                        leads[c]["cited"][p] += 1
                        basis[c].add(cite)
                elif cap:
                    leads[cap][route][p] += 1
                    basis[cap].add(f"concern:{con}")
    return leads, basis, n, traced


def term_leads(vp_row):
    """The point's own terms, per platform, against every capability's name, note and cells' terms."""
    m = model()
    terms = []
    for part in (vp_row.get("x_words") or "").split("|"):
        if ":" not in part:
            continue
        p, ws = part.split(":", 1)
        for w in re.split(r";|\s/\s", ws):
            w = w.strip().strip('"').strip()
            if 3 <= len(w) <= 60:
                terms.append(w)
    folded = sorted({fold(t) for t in terms})
    hay = {}
    cellterms = collections.defaultdict(list)
    for (cid, _p), r in m["cells"].items():
        cellterms[cid].append(r.get("terms", ""))
    out = collections.Counter()
    for cid, r in m["caps"].items():
        h = fold(" ".join([r.get("capability", ""), r.get("note", "")] + cellterms.get(cid, [])))
        for t in folded:
            if hits(t, h):
                out[cid] += 1
    return out, folded


def placements(cid):
    m = model()
    out = []
    for p in PLATFORMS:
        c = m["cells"].get((cid, p))
        out.append(f"{PREFIX[p]}:{(c or {}).get('placed_as') or '-'}")
    return " ".join(out)


def cap_line(cid):
    m = model()
    r = m["caps"].get(cid, {})
    k = m["kinds"].get(cid, {})
    dom = r.get("domain") or "?"
    kind = f"{k.get('kind', '')} {k.get('count', '')}".strip() or ("(not merged)" if dom not in m["merged"] else "")
    return f"{cid} [{dom} {r.get('area', '')}] {r.get('capability', '')[:90]} | {kind} | {placements(cid)}"


def cmd_leads(a):
    subs = a.subjects.split(",") if a.subjects else list(SUBJECTS)
    want = set(split(a.points)) if a.points else None
    for s in subs:
        vps, var, reg, _ = subject(s)
        for r in vps:
            vp = r["vp_id"]
            if want and vp not in want:
                continue
            leads, basis, n, traced = point_leads(s, vp)
            print(f"## {vp}\t{r['question']}\n   register: {', '.join(reg.get(vp, [])) or '(none)'}"
                  f"\n   statements: {n}, traced to the concern map: {traced}")
            score = {c: sum((3 if rt == "cited" else 2 if rt == "concern" else 1) * sum(cnt.values())
                            for rt, cnt in d.items()) for c, d in leads.items()}
            for c in sorted(score, key=lambda c: -score[c])[:a.top]:
                d = leads[c]
                routes = "; ".join(f"{rt} " + ",".join(f"{PREFIX[p]}{cnt[p]}" for p in PLATFORMS if cnt[p])
                                   for rt in ROUTES if rt in d for cnt in [d[rt]])
                print(f"   {cap_line(c)}\n      ({routes})")
            tl, terms = term_leads(r)
            top = [c for c, _ in tl.most_common(a.top) if c not in leads]
            if top:
                print(f"   by its terms ({len(terms)}):")
                for c in top:
                    print(f"   {cap_line(c)}\n      (terms {tl[c]})")
            print()


def clip(s, n):
    s = " ".join((s or "").split())
    return s if n <= 0 or len(s) <= n else s[:n] + " …"


def cmd_show(a):
    m = model()
    want = split(a.points)
    for vp in want:
        s = f"S-{vp[1:3]}"
        if s not in SUBJECTS:
            sys.exit(f"{vp}: not a point of {SUBJECTS}")
        vps, var, reg, _ = subject(s)
        r = next((x for x in vps if x["vp_id"] == vp), None)
        if not r:
            sys.exit(f"{vp}: no such point")
        print(f"## {vp}\t{r['question']}\n   terms: {clip(r['x_words'], a.width)}")
        regs = {x["id"]: x for x in rows(os.path.join(SUBJ, s, "register.tsv"))}
        for rid in reg.get(vp, []):
            x = regs[rid]
            ans = x.get("recommendation") or x.get("answer") or ""
            print(f"   register {rid} [{x['kind']}; {clip(x.get('status', ''), 80)}]: {clip(x['question'], 120)}"
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
            print(f"   {p}: {len(vs)} variants")
            for v in vs[:a.variants]:
                n = len(split(v["stmt_ids"]))
                extra = "".join([f"; absences {v['absence_ids']}" if v["absence_ids"] else "",
                                 f"; gaps {v['gap_ids']}" if v["gap_ids"] else ""])
                print(f"      {v['variant_id']} {clip(v['variant'], 110)} [{v['kind'] or '-'}; {n} statements{extra}]")
            if len(vs) > a.variants:
                print(f"      (+{len(vs) - a.variants} more)")
        leads, basis, n, traced = point_leads(s, vp)
        score = {c: sum((3 if rt == "cited" else 2 if rt == "concern" else 1) * sum(cnt.values())
                        for rt, cnt in d.items()) for c, d in leads.items()}
        tl, _ = term_leads(r)
        order = sorted(score, key=lambda c: -score[c])[:a.top]
        order += [c for c, _ in tl.most_common(a.top) if c not in order][:max(0, a.top - len(order) + 2)]
        print(f"   leads ({traced} of {n} statements traced to the concern map):")
        for c in order:
            d = leads.get(c, {})
            routes = "; ".join(f"{rt} " + ",".join(f"{PREFIX[p]}{d[rt][p]}" for p in PLATFORMS if d[rt][p])
                               for rt in ROUTES if rt in d) or f"terms {tl[c]}"
            print(f"   {cap_line(c)}\n      ({routes})")
            for p in PLATFORMS:
                cell = m["cells"].get((c, p))
                if cell and cell.get("held") != "none-held":
                    print(f"      {PREFIX[p]} {cell.get('placed_as') or '-'}: {clip(cell.get('reading', ''), a.width)}")
        print()


def batch_points(name):
    s, lo, hi = BATCHES[name]
    vps, _, _, _ = subject(s)
    return s, [r["vp_id"] for r in vps if lo <= int(r["vp_id"].rsplit("-", 1)[1]) <= hi]


def cmd_batches(a):
    for b in BATCHES:
        s, pts = batch_points(b)
        print(f"{b}\t{s}\t{len(pts)} points\t{','.join(pts)}")


def cmd_check(a):
    m = model()
    probs = []
    names = [a.batch] if a.batch else list(BATCHES)
    if a.batch and a.batch not in BATCHES:
        sys.exit(f"no batch {a.batch}: {', '.join(BATCHES)}")
    have = []
    for b in names:
        path = os.path.join(OUT, f"{b}.tsv")
        if not os.path.exists(path):
            probs.append(f"{b}: no {os.path.relpath(path, ROOT)}")
            continue
        with open(path, encoding="utf-8") as f:
            head = f.readline().rstrip("\n").split("\t")
        if head != HEAD:
            probs.append(f"{b}: header is {head}, not {HEAD}")
        for r in rows(path):
            have.append((b, r))
            if None in r or any(v is None for v in r.values()):
                probs.append(f"{b} {r.get('vp_id')}: wrong number of fields")
    seen = collections.Counter((r["subject"], r["vp_id"]) for _, r in have)
    for b in names:
        s, pts = batch_points(b)
        for vp in pts:
            if seen[(s, vp)] != 1:
                probs.append(f"{b} {vp}: landed {seen[(s, vp)]} times, not once")
    for b, r in have:
        s, vp = r["subject"], r["vp_id"]
        bs, pts = batch_points(b)
        if s != bs or vp not in pts:
            probs.append(f"{b} {vp}: not a point of batch {b}")
            continue
        vps, var, reg, _ = subject(s)
        qs = {x["vp_id"]: x["question"] for x in vps}
        if r["question"] != qs[vp]:
            probs.append(f"{b} {vp}: question differs from the subject's")
        cs = split(r["cap_ids"])
        if not cs:
            probs.append(f"{b} {vp}: cap_ids empty (write none for a point no capability holds)")
        for c in cs:
            if c != "none" and c not in m["caps"]:
                probs.append(f"{b} {vp}: {c} is no capability of the model")
        for rt in split(r["route"]):
            if rt not in ROUTES:
                probs.append(f"{b} {vp}: route {rt} not one of {ROUTES}")
        if cs != ["none"] and not r["basis"].strip():
            probs.append(f"{b} {vp}: basis empty")
        if not r["reading"].strip():
            probs.append(f"{b} {vp}: reading empty")
        if r["register"] != "; ".join(reg.get(vp, [])):
            probs.append(f"{b} {vp}: register should be '{'; '.join(reg.get(vp, []))}'")
        con = r["conflict"].strip()
        if not con:
            probs.append(f"{b} {vp}: conflict empty (none, or <type>: <what>)")
        elif con != "none":
            for part in con.split(" | "):
                t = part.split(":", 1)[0].strip()
                if t not in CONFLICTS or ":" not in part:
                    probs.append(f"{b} {vp}: conflict '{part[:40]}' is not <type>: <what>, type one of {CONFLICTS}")
        if r["status"] not in STATUS:
            probs.append(f"{b} {vp}: status {r['status']!r} not one of {STATUS}")
        elif (con == "none") != (r["status"] == "landed"):
            probs.append(f"{b} {vp}: status landed goes with conflict none, and only with it")
        if cs == ["none"] and not con.startswith("structure"):
            probs.append(f"{b} {vp}: a point no capability holds has a structure conflict")
        if cs and cs[0] != "none":
            for p in PLATFORMS:
                held = any(split(v["stmt_ids"]) for v in var.get(vp, []) if v["platform"] == p)
                cell = m["cells"].get((cs[0], p))
                if held and (not cell or cell.get("held") == "none-held"):
                    print(f"lead: {b} {vp} on {cs[0]}: the subject holds {p}'s statements, the cell holds none")
    for p in probs:
        print(p)
    print(f"# {len(have)} points in {', '.join(names)}, {len(probs)} problems")
    sys.exit(1 if probs else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("leads"); s.add_argument("--subjects"); s.add_argument("--points"); s.add_argument("--top", type=int, default=6)
    s = sub.add_parser("show"); s.add_argument("--points", required=True); s.add_argument("--top", type=int, default=5)
    s.add_argument("--width", type=int, default=220); s.add_argument("--variants", type=int, default=8)
    sub.add_parser("batches")
    s = sub.add_parser("check"); s.add_argument("--batch")
    a = ap.parse_args()
    {"leads": cmd_leads, "show": cmd_show, "batches": cmd_batches, "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    main()
