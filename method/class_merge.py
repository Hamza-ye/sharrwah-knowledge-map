"""Merge the parts of the class's model into one model, check what no single part can, and derive what architecture
reads (`PLAN.md`, Stage 4A, "The parts and the merge"; `studies/class-model/review-dry-run-rulings.md`).

Usage: python3 -I method/class_merge.py [--complete] [--labels-complete] [--exclude PART,...]

Reads every part folder in studies/class-model/parts/ and studies/class-model/scope.tsv. Run
method/check_class_part.py on each part first: the merge reads their derived.tsv.

Checks, across parts and domains:
- each concern lands exactly once (a `moved:` landing passes it on); a concern of a platform and domain no part has run yet
  is counted as not yet run, a problem only with --complete;
- each capability id once; each capability and platform one cell at most;
- each ruling again, on the cells of all its domain's parts (a mapping part can't see its back-fill);
- a statement that supports `core` or `own-service` in capabilities of two domains, which would count twice (a flag);
- capabilities of two domains whose cells share two or more terms, a possible join across domains (a flag).

Writes studies/class-model/merged/:
- capabilities.tsv, landings.tsv, cells.tsv (with each cell's derived places, scopes and gaps), evidence.tsv,
  rulings.tsv, qualities.tsv and slot-fillers.tsv, each row with its part;
- the qualities and the plans' terms apart (the qualities pass, briefs/QL-qualities-design.md, section 6.2), once
  qualities/labels.tsv exists: every quality row of the parts, with its scope from the part's derived-qualities.tsv,
  and the platform-wide rows of qualities/platform.tsv (part QL), each with a stable row_id (QR- and 10 hex digits of
  sha1 of cap_id, platform, quality, value and key, lengthened on a collision), joined to its label: merged/qualities.tsv
  holds the labels quality and other (and a row with no settled label, as unlabelled or unsure), merged/terms.tsv the
  label term. While qualities/labels.tsv doesn't exist, merged/qualities.tsv is written exactly as before, and
  merged/terms.tsv isn't written. An unlabelled or unsure row, and a label naming no row, is a flag, and a problem only
  with --labels-complete, which the coordinator passes once the labels' review (QL-L) is done;
- kinds.tsv, from method/class_kinds.py;
- interfaces.tsv: for each capability, its `boundary` and `decides` statements (data, events and what decides it),
  `exact` where a cell cites the statement, `by landing` where the statement belongs to a concern landed in the
  capability and no cell of the domain cites it (a coarse attribution each area's design refines).
Prints problems, then flags; exits 1 if any problem is found.
"""
import argparse, collections, csv, hashlib, os, re, subprocess, sys

csv.field_size_limit(10**9)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, PART_ORDER, rows, items, key, fold, ids, citable
from check_class_part import HEADS, semi, plat

problems, flags = [], []
QDIR = os.path.join(MODEL, "qualities")
LABELS = os.path.join(QDIR, "labels.tsv")
PLATFORM_QUAL = os.path.join(QDIR, "platform.tsv")
QHEAD = ["cap_id", "platform", "quality", "value", "key", "part", "row_id", "scope", "label", "kind", "form", "basis",
         "holder", "date", "source_type"]
PLATFORM_HEAD = ["cap_id", "platform", "quality", "value", "key", "kind", "form", "basis", "holder", "scope", "date",
                 "source_type", "part", "line"]
LABELS_HEAD = ["row_id", "cap_id", "platform", "quality", "key", "label", "kind", "form", "basis", "holder", "date",
               "source_type", "decided_by", "reading"]
LABEL_VALUES = ("term", "quality", "other")       # unsure: a rule's row left for the review (QL-L)
QUAL_FIELDS = ("cap_id", "platform", "quality", "value", "key")


def row_ids(tuples):
    """{(cap_id, platform, quality, value, key): row_id}: QR- and the first 10 hex digits of the sha1 of the five
    fields joined by NUL, lengthened (12, 16, 40) only among the rows that share a prefix, so a row's id depends on no
    other row but one it collides with (the qualities pass's design, section 6.2)."""
    hs = {t: hashlib.sha1("\x00".join(t).encode("utf-8")).hexdigest() for t in set(tuples)}
    by = collections.defaultdict(list)
    for t, h in hs.items():
        by[h[:10]].append(t)
    out = {}
    for pre, ts in by.items():
        n = 10
        for n in (10, 12, 16, 40):
            if len({hs[t][:n] for t in ts}) == len(ts):
                break
        for t in ts:
            out[t] = "QR-" + hs[t][:n]
    return out


def model_parts(leave=()):
    """The part folders the merge reads, in its order: (domain, order, folder)."""
    base = os.path.join(MODEL, "parts")
    out = []
    for d in sorted(os.listdir(base)):
        dom, _, kind = d.partition("-")
        if kind in PART_ORDER and d not in leave:
            out.append((dom, PART_ORDER.index(kind), d))
    return sorted(out)


def quality_rows(parts, data=None, notes=None):
    """Every quality row of the parts, with its part and its scope from the part's derived-qualities.tsv (written by
    check_class_part.py, row for row), then qualities/platform.tsv's rows (part QL), each with its row_id. notes
    collects what doesn't line up."""
    notes = [] if notes is None else notes
    out = []
    for _, _, d in parts:
        if data is not None:
            qs, dq = data[d]["qualities.tsv"], data[d].get("derived-qualities.tsv", [])
        else:
            qs = rows(os.path.join(MODEL, "parts", d, "qualities.tsv"))
            dq = rows(os.path.join(MODEL, "parts", d, "derived-qualities.tsv"))
        by_t = collections.defaultdict(list)
        for x in dq:
            by_t[tuple(x.get(f, "") for f in QUAL_FIELDS)].append(x.get("scope", ""))
        stale = 0
        for i, r in enumerate(qs):
            t = tuple(r.get(f, "") for f in QUAL_FIELDS)
            if i < len(dq) and tuple(dq[i].get(f, "") for f in QUAL_FIELDS) == t:
                scope = dq[i].get("scope", "")
            elif by_t.get(t):
                scope = by_t[t][0]
            else:
                scope, stale = "", stale + 1
            out.append({**{f: r.get(f, "") for f in QUAL_FIELDS}, "part": d, "scope": scope})
        if stale:
            notes.append(f"{d}: {stale} quality rows have no row in its derived-qualities.tsv, so no scope: run "
                         f"method/check_class_part.py on it")
    for r in rows(PLATFORM_QUAL):
        out.append({**{h: r.get(h, "") for h in PLATFORM_HEAD}, "part": "QL", "_line": r.get("line", "")})
    ids_ = row_ids([tuple(r[f] for f in QUAL_FIELDS) for r in out])
    for r in out:
        r["row_id"] = ids_[tuple(r[f] for f in QUAL_FIELDS)]
    return out


def write(path, head, body):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(head) + "\n")
        for r in body:
            f.write("\t".join(str(r.get(h, "")).replace("\t", " ").replace("\n", " ") for h in head) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--complete", action="store_true")
    ap.add_argument("--exclude", default="", help="parts to leave out, comma-separated, such as one an agent is still writing")
    ap.add_argument("--labels-complete", action="store_true",
                    help="the labels' review (QL-L) is done: an unlabelled or unsure quality row, or a label naming no row, is a problem")
    a = ap.parse_args()
    leave = set(ids(a.exclude))
    base = os.path.join(MODEL, "parts")
    parts = model_parts(leave)
    data = {}
    for dom, _, d in parts:
        data[d] = {f: rows(os.path.join(base, d, f)) for f in list(HEADS) + ["derived.tsv", "derived-qualities.tsv"]}
        if not data[d]["derived.tsv"] and data[d]["cells.tsv"]:
            problems.append(f"{d}: no derived.tsv; run method/check_class_part.py on it first")
    sc = {r["concern_id"]: r for r in rows(os.path.join(MODEL, "scope.tsv"))}
    stm = {p: {key(r): r for r in citable(p)} for p in PLATFORMS}

    def statement(k):
        p = plat(k)
        return stm[p].get(k) if p else None

    def sid(k):
        """The statement a key names: the concern map holds one statement under several concerns, each with its own
        key and the same statement id, so two keys can name one statement. An inventory id names itself."""
        return (plat(k), k.rsplit("/", 1)[-1]) if "/" in k else (plat(k), k)

    # capabilities, landings, cells
    caps, cdom = {}, {}
    for dom, _, d in parts:
        for r in data[d]["capabilities.tsv"]:
            if r["cap_id"] in caps:
                problems.append(f"{d}: {r['cap_id']} also in {caps[r['cap_id']]['part']}")
            caps[r["cap_id"]] = r | {"part": d, "domain": dom}
            cdom[r["cap_id"]] = dom
    landed = {}
    for dom, _, d in parts:
        for r in data[d]["landings.tsv"]:
            c = r["concern_id"]
            if r["cap_id"].startswith("moved:"):
                continue
            if c in landed:
                problems.append(f"{d}: {c} lands again (first in {landed[c]['part']})")
            landed[c] = r | {"part": d, "domain": dom}
    run = set()
    for dom, _, d in parts:
        kind = d.partition("-")[2]
        if kind == "anchor":
            run |= {(dom, "shopify"), (dom, "salla")}
        elif kind in PLATFORMS:
            run.add((dom, kind))
        elif kind == "amend":
            run |= {(dom, r["platform"]) for r in data[d]["landings.tsv"]}
    not_run = 0
    for c, r in sc.items():
        if c in landed:
            if landed[c]["domain"] != r["domain"]:
                problems.append(f"{c} lands in domain {landed[c]['domain']}, and scope.tsv gives {r['domain']}")
            continue
        if (r["domain"], r["platform"]) in run or a.complete:
            problems.append(f"{c} (domain {r['domain']}) lands nowhere")
        else:
            not_run += 1
    cells, derived = {}, {}
    for dom, _, d in parts:
        for r in data[d]["cells.tsv"]:
            k = (r["cap_id"], r["platform"])
            if k in cells:
                problems.append(f"{d}: a second cell for {k[0]} and {k[1]} (first in {cells[k]['part']})")
            cells[k] = r | {"part": d}
        for r in data[d]["derived.tsv"]:
            derived[r["cap_id"], r["platform"]] = r
    ev = []
    for dom, _, d in parts:
        ev += [r | {"part": d, "domain": dom} for r in data[d]["evidence.tsv"]]

    # one statement counted twice: by its statement id, under whichever concern's key each part cites it
    own, own_rows, cell_own = {}, {}, {}
    for r in ev:
        if r["supports"] in ("core", "own-service"):
            own.setdefault(sid(r["key"]), set()).add(cdom.get(r["cap_id"], "?"))
            own_rows.setdefault(sid(r["key"]), []).append(r)
            cell_own.setdefault((r["cap_id"], r["platform"]), set()).add(sid(r["key"]))
    for s_, ds in sorted(own.items()):
        if len(ds) > 1:
            # a cell whose core rests on this statement alone: there the count hinges on it
            uses = sorted({f"{r['cap_id']} ({r['key']}{', its cell rests on it alone' if cell_own[(r['cap_id'], r['platform'])] == {s_} else ''})" for r in own_rows[s_]})
            flags.append("counted twice\t" + f"one statement supports core or own-service in domains {', '.join(sorted(ds))}, so it counts in each: {'; '.join(uses)}")

    # rulings again, on all parts of the domain
    uc = {u["candidate_id"]: u for u in rows(os.path.join(MODEL, "..", "concern-map", "unclear-matches.tsv"))}
    citing = {}
    for r in ev:
        citing.setdefault((r["domain"], r["key"]), set()).add(r["cap_id"])

    def ancestors(c):
        out, seen = set(), set()
        while c in caps and caps[c]["parent"].strip() and c not in seen:
            seen.add(c); c = caps[c]["parent"].strip(); out.add(c)
        return out
    rul = []
    for dom, _, d in parts:
        kind = d.partition("-")[2]
        for r in data[d]["rulings.tsv"]:
            rul.append(r | {"part": d})
            u = uc.get(r["candidate_id"])
            if not u:
                continue
            sh, sa, wc = ids(u["shopify"]), ids(u["salla"]), ids(u["woocommerce"])
            mine, theirs = (sh, sa) if kind == "anchor" else (wc, sh + sa)

            def kc(k):
                it = statement(k)
                return it.get("concern_ids", [it["concern_id"]]) if it else []
            keys = semi(r["keys"])
            cm = set().union(*[citing.get((dom, k), set()) for k in keys if set(kc(k)) & set(mine)] or [set()])
            ct = set().union(*[citing.get((dom, k), set()) for k in keys if set(kc(k)) & set(theirs)] or [set()])
            ru = r["ruling"]
            cap = ru.split(":", 1)[1] if ":" in ru else ""
            if ru.startswith("joined:") and not (cap in cm and cap in ct):
                problems.append(f"{d}: {r['candidate_id']} joined:{cap}, but no cell of {cap} cites keys of both sides, in all of domain {dom}'s parts")
            elif ru.startswith("nested:") and not ((cap in cm and ancestors(cap) & ct) or (cap in ct and ancestors(cap) & cm)):
                problems.append(f"{d}: {r['candidate_id']} nested:{cap} doesn't hold on all of domain {dom}'s parts")
            elif ru == "apart" and cm & ct:
                problems.append(f"{d}: {r['candidate_id']} apart, but {', '.join(sorted(cm & ct))} cites keys of both sides")

    # one pair ruled differently by two parts (two domains each rule from their own cells)
    seen_pairs = {}
    for r in rul:
        u = uc.get(r["candidate_id"])
        if not u:
            continue
        cs = set()
        for k in semi(r["keys"]):
            it = statement(k)
            if it:
                cs |= set(it.get("concern_ids", [it["concern_id"]])) & set(ids(u["shopify"]) + ids(u["salla"]) + ids(u["woocommerce"]))
        if len(cs) == 2:
            pair = (r["candidate_id"], frozenset(cs))
            verdict = "apart" if r["ruling"] == "apart" else "together"
            seen_pairs.setdefault(pair, []).append((r["part"], r["ruling"], verdict))
    for (cid, cs), rs in sorted(seen_pairs.items(), key=lambda x: x[0][0]):
        if len({v for _, _, v in rs}) > 1:
            flags.append("ruled differently\t" + f"{cid} ({' x '.join(sorted(cs))}) is ruled differently: " + "; ".join(f"{p} {ru}" for p, ru, _ in rs) + ": one answer at the review")

    # possible joins across domains
    terms = {}
    for (c, p), r in cells.items():
        for t in semi(r["terms"]):
            if len(t) > 3:
                terms.setdefault(c, set()).add(fold(t))
    cl = sorted(terms)
    for i, x in enumerate(cl):
        for y in cl[i + 1:]:
            if cdom.get(x) != cdom.get(y):
                shared = terms[x] & terms[y]
                if len(shared) >= 2:
                    flags.append("one capability?\t" + f"{x} (domain {cdom.get(x)}) and {y} (domain {cdom.get(y)}) share terms {', '.join(sorted(shared))[:120]}: one capability?")

    # a clean landing whose statement is cited in another tree of its domain under another concern's key (the
    # concern map holds one statement under several concerns): strained by the dry run's S1, unless the statement is
    # general (a term of service, say), which the review decides
    def root(c):
        seen = set()
        while c in caps and caps[c]["parent"].strip() and c not in seen:
            seen.add(c); c = caps[c]["parent"].strip()
        return c
    held_ids = {}
    for p in PLATFORMS:
        for s in stm[p].values():
            if s["placement"] != "inventory":
                held_ids.setdefault(s["concern_id"], set()).add(sid(key(s)))
    by_sid = {}
    for r in ev:
        by_sid.setdefault((r["domain"], sid(r["key"])), []).append(r)
    for c, lr in sorted(landed.items()):
        if lr["fit"] != "clean" or lr["cap_id"] not in caps:
            continue
        far = sorted({f"{r['key']} in {r['cap_id']}" for s_ in held_ids.get(c, ()) for r in by_sid.get((lr["domain"], s_), [])
                      if r["key"].split("/")[0] != c and root(r["cap_id"]) != root(lr["cap_id"])})
        if far:
            flags.append("strained?\t" + f"{c} is clean in {lr['cap_id']}, and a statement it holds is cited in another tree under another concern's key: {'; '.join(far[:4])}{' …' if len(far) > 4 else ''}: strained, unless the statement is general")

    # outputs
    out = os.path.join(MODEL, "merged")
    os.makedirs(out, exist_ok=True)
    write(os.path.join(out, "capabilities.tsv"), ["cap_id", "domain", "area", "capability", "parent", "note", "part"], caps.values())
    write(os.path.join(out, "landings.tsv"), ["platform", "concern_id", "cap_id", "join", "join_evidence", "fit", "reading", "part"], landed.values())
    cell_rows = []
    for k, r in sorted(cells.items()):
        dr = derived.get(k, {})
        cell_rows.append(r | {h: dr.get(h, "") for h in ("placed_as", "where", "scopes", "gaps", "own_scopes")})
    write(os.path.join(out, "cells.tsv"), ["cap_id", "platform", "held", "placed_as", "terms", "where", "scopes", "own_scopes", "gaps", "searched", "reading", "part"], cell_rows)
    write(os.path.join(out, "evidence.tsv"), ["cap_id", "platform", "supports", "key", "why", "part"], ev)
    write(os.path.join(out, "rulings.tsv"), ["candidate_id", "ruling", "basis", "keys", "part"], rul)
    for f in ("qualities.tsv", "slot-fillers.tsv"):
        if f == "qualities.tsv" and os.path.exists(LABELS):
            continue
        allr = [r | {"part": d} for _, _, d in parts for r in data[d][f]]
        write(os.path.join(out, f), HEADS[f] + ["part"], allr)
    qcounts = merge_qualities(parts, data, out, stm, a.labels_complete)
    # interfaces: exact where cited, by landing otherwise
    cited_dom = {(r["domain"], sid(r["key"])) for r in ev}
    iface = []
    for r in ev:
        s = statement(r["key"])
        if s and s["placement"] in ("boundary", "decides"):
            iface.append({"cap_id": r["cap_id"], "grade": "exact", "placement": s["placement"], "key": r["key"], "identifier": " ".join(s["identifier"].split())[:160]})
    for c, lr in landed.items():
        p = lr["platform"]
        for s in items(p):
            if c in s.get("concern_ids", [s["concern_id"]]) and s["placement"] in ("boundary", "decides") and (lr["domain"], sid(key(s))) not in cited_dom:
                iface.append({"cap_id": lr["cap_id"], "grade": "by landing", "placement": s["placement"], "key": key(s), "identifier": " ".join(s["identifier"].split())[:160]})
    seen, iface_u = set(), []
    for r in iface:
        t = (r["cap_id"], r["key"])
        if t not in seen:
            seen.add(t); iface_u.append(r)
    write(os.path.join(out, "interfaces.tsv"), ["cap_id", "grade", "placement", "key", "identifier"], sorted(iface_u, key=lambda r: (r["cap_id"], r["grade"], r["key"])))
    k = subprocess.run([sys.executable, "-I", os.path.join(os.path.dirname(os.path.abspath(__file__)), "class_kinds.py"), "--out", os.path.join(out, "kinds.tsv"), "--exclude", ",".join(sorted(leave))],
                       capture_output=True, text=True, env=os.environ)
    print(k.stderr.strip())
    print(f"{len(caps)} capabilities, {len(landed)} concerns landed, {not_run} in platforms and domains not yet run, {len(cells)} cells, "
          f"{len(ev)} evidence rows, {len(rul)} rulings; {sum(1 for r in iface_u if r['grade'] == 'exact')} interface rows exact, "
          f"{sum(1 for r in iface_u if r['grade'] == 'by landing')} by landing; written to studies/class-model/merged/")
    if qcounts:
        print(qcounts)
    for p_ in problems:
        print("PROBLEM", p_)
    for f_ in flags:
        print("FLAG", f_.split("\t", 1)[1])
    # the flags, for the final review: each kind of question with its text
    with open(os.path.join(out, "flags.tsv"), "w", encoding="utf-8") as fh:
        fh.write("kind\tflag\n")
        for f_ in flags:
            fh.write(f_ + "\n")
    print(f"{len(problems)} problems, {len(flags)} flags")
    sys.exit(1 if problems else 0)


def merge_qualities(parts, data, out, stm, labels_complete):
    """merged/qualities.tsv and merged/terms.tsv, once qualities/labels.tsv exists (the qualities pass's design, section
    6.2); before it, merged/qualities.tsv is today's file, written in main(), and this only says what waits."""
    terms_path = os.path.join(out, "terms.tsv")
    if not os.path.exists(LABELS):
        if os.path.exists(terms_path):
            os.remove(terms_path)          # a terms file without its labels would be stale
            print("removed merged/terms.tsv: qualities/labels.tsv doesn't exist")
        n = len(rows(PLATFORM_QUAL))
        if n:
            flags.append("platform qualities wait\t" + f"qualities/platform.tsv holds {n} rows, merged only once "
                         f"qualities/labels.tsv exists")
        return ""
    def flag_or_problem(kind, text):
        if labels_complete:
            problems.append(text)
        else:
            flags.append(f"{kind}\t{text}")
    notes = []
    qr = quality_rows(parts, data, notes)
    for x in notes:
        flags.append("no scope\t" + x)
    lab = {}
    for i, r in enumerate(rows(LABELS), 2):
        if r["row_id"] in lab:
            problems.append(f"qualities/labels.tsv line {i}: {r['row_id']} labelled again")
        lab[r["row_id"]] = r
        if r["label"] not in LABEL_VALUES + ("unsure",):
            problems.append(f"qualities/labels.tsv line {i}: label is one of {', '.join(LABEL_VALUES)} (or unsure, for review)")
    for r in qr:
        if r["part"] == "QL":
            w = f"qualities/platform.tsv line {r.get('_line') or '?'}"
            if r["cap_id"] != "platform":
                problems.append(f"{w}: cap_id is platform")
            if r["platform"] not in PLATFORMS:
                problems.append(f"{w}: platform {r['platform']!r} is not one of the five")
            elif r["key"] not in stm[r["platform"]]:
                problems.append(f"{w}: {r['key']!r} is neither a statement key, an inventory id nor a held entry of {r['platform']}")
    seen = set()
    for r in qr:
        seen.add(r["row_id"])
        L = lab.get(r["row_id"])
        r["label"] = L["label"] if L else "unlabelled"
        for h in ("kind", "form", "basis", "holder", "date", "source_type"):
            r[h] = (L.get(h) if L else "") or r.get(h, "")
    un = [r for r in qr if r["label"] in ("unlabelled", "unsure")]
    if un:
        by = collections.Counter(r["label"] for r in un)
        flag_or_problem("unlabelled", f"{len(un)} quality rows have no settled label ({', '.join(f'{v} {k}' for k, v in sorted(by.items()))}), such as "
                        f"{un[0]['row_id']} ({un[0]['cap_id']}@{un[0]['platform']} {un[0]['quality']}): run ql_qualities.py labels")
    orphan = sorted(set(lab) - seen)
    if orphan:
        flag_or_problem("label of no row", f"{len(orphan)} labels of qualities/labels.tsv name no row, such as {orphan[0]}: "
                        f"the row was corrected or removed (ql_qualities.py labels check)")
    qs = [r for r in qr if r["label"] != "term"]
    ts = [r for r in qr if r["label"] == "term"]
    write(os.path.join(out, "qualities.tsv"), QHEAD, qs)
    write(terms_path, QHEAD, ts)
    by = collections.Counter(r["label"] for r in qr)
    return (f"qualities: {len(qs)} rows to merged/qualities.tsv, {len(ts)} to merged/terms.tsv "
            f"({', '.join(f'{k} {v}' for k, v in sorted(by.items()))}; {sum(1 for r in qr if r['part'] == 'QL')} of them platform-wide)")


if __name__ == "__main__":
    main()
