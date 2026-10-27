"""Print what phase C compares for one or more variation points of a root decision: each platform's rows, with the
answer each gives, its kind, scope, release markers and the (h) statements that condition it; then each platform's
set of answers, and the answers two or more platforms share.

Usage: python3 -I method/point_view.py SUBJECT_DIR RD VP_ID [VP_ID ...]
       python3 -I method/point_view.py SUBJECT_DIR --stmts ID[,ID...]

--stmts prints statements whole by id, from any bullet, (h) among them, with their platform, bullet, identifier,
statement, scope, marker and conditions, but no note.

Reads SUBJECT_DIR/b/<RD>/variation-points.tsv and variants.tsv, SUBJECT_DIR/slices/<RD>/statements.tsv for each
statement's kind, and each platform's statements.tsv for scope, marker and conditions. A statement under (h) names in
`conditions` the statements it conditions; this prints them beside the rows whose statements they condition.

The platforms come in the brief's three groups: Salla and Zid, Shopify and BigCommerce, then WooCommerce.

`answer` is the tool's reading of a row's basis_evidence, for the agent to check against it, never to cite:
- under `what "X" takes its value per`, the phrases of the brief's rule 4 the evidence names: `a market the store
  sells into`, `the buyer's country`, `the store's own country`, `the whole store`;
- elsewhere, `every store` or `no market` where the evidence names them, or else the evidence's words before its
  first colon, where they are short.
"""
import csv, os, re, signal, sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # a pipe into head ends quietly
csv.field_size_limit(10**9)
GROUPS = (("salla", "zid"), ("shopify", "bigcommerce"), ("woocommerce",))
PER = ("a market the store sells into", "the buyer's country", "the store's own country", "the whole store")


def table(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def answer(question, ev, form):
    if form in ("gap", "absent", "not covered"):
        return form
    low = ev.lower()
    if question.startswith("what ") and "takes its value per" in question:
        found = [p for p in PER if p in low]
        return "; ".join(found) if found else "?"
    for w in ("every store", "no market"):
        if w in low:
            return w
    head = ev.split(":")[0].strip()
    return head if 0 < len(head) <= 90 else "?"


def main(subj, rd, vps):
    points = {p["vp_id"]: p for p in table(os.path.join(subj, "b", rd, "variation-points.tsv"))}
    variants = table(os.path.join(subj, "b", rd, "variants.tsv"))
    kind = {r["stmt_id"]: r["kind"] for r in table(os.path.join(subj, "slices", rd, "statements.tsv"))}
    st, cond = {}, {}
    for g in GROUPS:
        for p in g:
            for r in table(os.path.join(subj, p, "statements.tsv")):
                st[r["stmt_id"]] = r
                if "h" in [b.strip() for b in r["bullet"].split(";")]:
                    for s in ids(r["conditions"]):
                        cond.setdefault(s, []).append(r["stmt_id"])
    for vp in vps:
        p = points.get(vp)
        if not p:
            print(f"{vp}: not a point of b/{rd}/variation-points.tsv")
            continue
        q = p["question"]
        print(f"{vp} ({p['bullet']}) {q}")
        print(f"  kind of X: {p['x_words'].split(' | ')[0]}")
        sets = []
        for g in GROUPS:
            for plat in g:
                rows = [v for v in variants if v["vp_id"] == vp and v["platform"] == plat]
                got = []
                print(f"  {plat}:" + ("" if rows else " no row"))
                for v in rows:
                    form = v["variant"] if v["variant"] in ("gap", "absent", "not covered") else "answer"
                    a = answer(q, v["basis_evidence"], form)
                    got.extend(a.split("; "))
                    sids = ids(v["stmt_ids"])
                    marks = sorted({f"{s}: {st[s]['marker']}" for s in sids if s in st and st[s]["marker"].strip()})
                    scopes = sorted({st[s]["scope"].strip() for s in sids if s in st and st[s]["scope"].strip()})
                    hs = []
                    for s in sids:
                        for h in cond.get(s, []):
                            if h not in hs:
                                hs.append(h)
                    print(f"    {v['variant_id']} {form} | answer: {a} | kind {v['kind'] or '-'} | {len(sids)} statements"
                          + (f" | gaps {v['gap_ids']}" if v["gap_ids"] else "")
                          + (f" | absences {v['absence_ids']}" if v["absence_ids"] else ""))
                    if form == "answer":
                        print(f"      variant: {v['variant'][:140]}")
                        print(f"      evidence: {v['basis_evidence'][:320]}")
                        print(f"      statements: {';'.join(sids)}")
                    if scopes:
                        print(f"      scopes: {' | '.join(x[:90] for x in scopes[:6])}" + (f" (+{len(scopes) - 6})" if len(scopes) > 6 else ""))
                    if marks:
                        print(f"      markers: {'; '.join(marks[:6])}")
                    for h in hs[:5]:
                        r = st[h]
                        print(f"      condition {h}: {r['statement'][:130]}" + (f" [scope: {r['scope'][:60]}]" if r["scope"].strip() else ""))
                    if len(hs) > 5:
                        print(f"      conditions also: {';'.join(hs[5:])}")
                sets.append(f"{plat} {{{', '.join(sorted(set(got))) or '-'}}}")
        print("  answer sets: " + " | ".join(sets))
        share = {}
        for line in sets:
            plat, rest = line.split(" ", 1)
            for a in rest.strip("{}").split(", "):
                if a and a not in ("-", "?", "gap", "absent", "not covered"):
                    share.setdefault(a, []).append(plat)
        both = [f"{a}: {', '.join(ps)}" for a, ps in share.items() if len(ps) > 1]
        print("  shared: " + (" | ".join(both) if both else "none"))
        print()


def stmts(subj, wanted):
    found = set()
    for g in GROUPS:
        for p in g:
            for r in table(os.path.join(subj, p, "statements.tsv")):
                if r["stmt_id"] in wanted:
                    found.add(r["stmt_id"])
                    print("\t".join([p, r["stmt_id"], r["bullet"], r["identifier"], r["statement"], r["scope"], r["marker"], r["conditions"]]))
    for w in wanted:
        if w not in found:
            print(f"{w}: no such statement", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[2] == "--stmts":
        stmts(sys.argv[1].rstrip("/"), ids(sys.argv[3]))
    elif len(sys.argv) < 4:
        sys.exit(__doc__)
    else:
        main(sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3:])
