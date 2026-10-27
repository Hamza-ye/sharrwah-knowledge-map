"""Cut a subject's phase A files into one slice per root decision, for agents that work on one decision each; and print
a part of a slice.

Usage: python3 -I method/subject_slice.py SUBJECT_DIR
       python3 -I method/subject_slice.py SUBJECT_DIR --print RD [--bullet B] [--platform P] [--ids ID[,ID...]]
                                          [--what statements|gaps|absences|terms]

Cutting reads SUBJECT_DIR/bullets.tsv (each bullet's `root_decision`, `;`-separated where it serves several, and its
`role`), each platform's statements.tsv, gaps.tsv, absences.tsv, terms.tsv and citations.tsv, and SUBJECT_DIR/kinds.tsv,
which `method/check_subject.py` writes: run the checker first, so that every statement has its kind. For each root
decision it writes SUBJECT_DIR/slices/<root decision>/:
- statements.tsv: every statement under a bullet of that decision, with its platform, its kind, and its first
  citation's source (statements that share a source and an identifier may be runs of one list); a statement under
  bullets of several decisions goes in each of their slices;
- gaps.tsv and absences.tsv: those under a bullet of that decision, with their platform (and an absence's kind);
- terms.tsv: every platform's terms, with their platform.

Only bullets whose role is `ask` or `no-part` make a slice: `conditions` statements are read later, and `end` bullets
have no decision of their own. A slice keeps only the columns phase B reads: never a `note`, nor citations, routes or
what was read. It stops, naming them, if any statement or absence has no kind in kinds.tsv. The slices are copies:
phase A's files stay the record. Cut them again after anything adds to phase A's files, such as gap-closing.

--print prints the rows of one root decision's slice, filtered by bullet, platform or ids, so an agent reads the part
it needs instead of the whole slice.
"""
import csv, os, signal, sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # a pipe into head ends quietly

csv.field_size_limit(10**9)
PLATFORMS = ("shopify", "salla", "zid", "woocommerce", "bigcommerce")
KEEP = {"statements": ["stmt_id", "bullet", "placement", "identifier", "statement", "scope", "marker"],
        "gaps": ["gap_id", "bullet", "what_is_missing", "gap_kind"],
        "absences": ["absence_id", "bullet", "what_is_absent"],
        "terms": ["term", "translation", "definition"]}


def rows(path):
    if not os.path.exists(path):
        return [], []
    with open(path, encoding="utf-8", newline="") as f:
        r = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not r:
        return [], []
    return r[0], [dict(zip(r[0], x)) for x in r[1:] if any(c.strip() for c in x)]


def write(path, head, body):
    with open(path, "w", encoding="utf-8", newline="") as f:
        for r in [head] + body:
            if any("\t" in c or "\n" in c for c in r):
                sys.exit(f"{path}: a field holds a tab or a newline: {r[:3]}")
            f.write("\t".join(r) + "\n")


def decisions(subj):
    _, bullets = rows(os.path.join(subj, "bullets.tsv"))
    if not bullets:
        sys.exit(f"{subj}/bullets.tsv is missing or empty")
    rds = {}
    for b in bullets:
        if b["role"] not in ("ask", "no-part"):
            continue
        for rd in (x.strip() for x in b["root_decision"].split(";") if x.strip()):
            rds.setdefault(rd, set()).add(b["bullet"])
    return rds


def cut(subj):
    rds = decisions(subj)
    kinds = {r["id"]: r["kind"] for r in rows(os.path.join(subj, "kinds.tsv"))[1]}
    data = {p: {n: rows(os.path.join(subj, p, n + ".tsv"))
                for n in ("statements", "gaps", "absences", "terms", "citations")}
            for p in PLATFORMS if os.path.isdir(os.path.join(subj, p))}
    missing = [r["stmt_id"] for d in data.values() for r in d["statements"][1] if not kinds.get(r["stmt_id"])] + \
              [r["absence_id"] for d in data.values() for r in d["absences"][1] if not kinds.get(r["absence_id"])]
    if missing:
        sys.exit(f"{len(missing)} ids have no kind in kinds.tsv (run method/check_subject.py first): "
                 f"{', '.join(missing[:10])}")
    for rd, mine in sorted(rds.items()):
        out = os.path.join(subj, "slices", rd)
        os.makedirs(out, exist_ok=True)
        st, gp, ab, tm = [], [], [], []
        for p, d in data.items():
            src = {c["cite_id"]: c["source"] for c in d["citations"][1]}
            for r in d["statements"][1]:
                if {x.strip() for x in r["bullet"].split(";")} & mine:
                    first = next((c for c in r["cite_ids"].replace(",", ";").split(";") if c.strip()), "").strip()
                    st.append([p, kinds[r["stmt_id"]], src.get(first, "")] + [r.get(c, "") for c in KEEP["statements"]])
            for r in d["gaps"][1]:
                if r["bullet"].strip() in mine:
                    gp.append([p] + [r.get(c, "") for c in KEEP["gaps"]])
            for r in d["absences"][1]:
                if r["bullet"].strip() in mine:
                    ab.append([p, kinds[r["absence_id"]]] + [r.get(c, "") for c in KEEP["absences"]])
            tm += [[p] + [r.get(c, "") for c in KEEP["terms"]] for r in d["terms"][1]]
        write(os.path.join(out, "statements.tsv"), ["platform", "kind", "source"] + KEEP["statements"], st)
        write(os.path.join(out, "gaps.tsv"), ["platform"] + KEEP["gaps"], gp)
        write(os.path.join(out, "absences.tsv"), ["platform", "kind"] + KEEP["absences"], ab)
        write(os.path.join(out, "terms.tsv"), ["platform"] + KEEP["terms"], tm)
        print(f"{rd}\tbullets {''.join(sorted(mine))}\t{len(st)} statements\t{len(gp)} gaps\t{len(ab)} absences\t"
              f"{len(tm)} terms")


def show(subj, args):
    opts = {"--bullet": "", "--platform": "", "--ids": "", "--what": "statements"}
    rd, it = args[0], iter(args[1:])
    for a in it:
        if a not in opts:
            sys.exit(f"unknown option {a}")
        v = next(it, "").strip()
        if not v or v.startswith("--"):
            sys.exit(f"{a} needs a value")               # an empty value would print the whole slice
        opts[a] = v
    if opts["--what"] not in KEEP:
        sys.exit(f"--what is one of {', '.join(KEEP)}")
    if opts["--platform"] and opts["--platform"] not in PLATFORMS:
        sys.exit(f"--platform is one of {', '.join(PLATFORMS)}")
    head, recs = rows(os.path.join(subj, "slices", rd, opts["--what"] + ".tsv"))
    if not head:
        sys.exit(f"no slice {rd}/{opts['--what']}.tsv: cut the slices first")
    if opts["--bullet"]:
        if "bullet" not in head:
            sys.exit(f"{opts['--what']} have no bullet")
        mine = decisions(subj).get(rd, set())
        if opts["--bullet"] not in mine:
            sys.exit(f"{rd}'s bullets are {', '.join(sorted(mine))}")
    key = KEEP[opts["--what"]][0]                        # the id column: stmt_id, gap_id, absence_id or term
    want = {x.strip() for x in opts["--ids"].split(",") if x.strip()}
    print("\t".join(head))
    for r in recs:
        if opts["--platform"] and r.get("platform") != opts["--platform"]:
            continue
        if opts["--bullet"] and opts["--bullet"] not in {x.strip() for x in r.get("bullet", "").split(";")}:
            continue
        if want and r.get(key) not in want:
            continue
        print("\t".join(r.get(h, "") for h in head))
    # an id asked for that the slice doesn't hold is named, so that it isn't missed in silence: it is under none of
    # this root decision's bullets (or under none the filters let through)
    missing = sorted(want - {r.get(key) for r in recs})
    if missing:
        print(f"not in {rd}'s slice: {', '.join(missing)}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        cut(sys.argv[1].rstrip("/"))
    elif len(sys.argv) >= 4 and sys.argv[2] == "--print":
        show(sys.argv[1].rstrip("/"), sys.argv[3:])
    else:
        sys.exit(__doc__)
