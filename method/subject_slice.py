"""Cut a subject's phase A files into one slice per root decision, for agents that work on one decision each.

Usage: python3 -I method/subject_slice.py SUBJECT_DIR

Reads SUBJECT_DIR/bullets.tsv (each bullet's `root_decision`, `;`-separated where it serves several, and its
`role`) and each platform's statements.tsv, gaps.tsv, absences.tsv and terms.tsv, with SUBJECT_DIR/kinds.tsv. For each
root decision it writes SUBJECT_DIR/slices/<root decision>/:
- statements.tsv: every statement under a bullet of that decision, with its platform and kind; a statement under
  bullets of several decisions goes in each of their slices;
- gaps.tsv and absences.tsv: those under a bullet of that decision, with their platform;
- terms.tsv: every platform's terms, with their platform (terms aren't tied to a bullet).

Only bullets whose role is `ask` or `no-part` make a slice's statements: `conditions` statements are read later, and
`end` bullets have no decision of their own. A slice keeps only the columns phase B reads: never a `note` (phase B
doesn't read notes), nor citations, routes or what was read. The slices are copies: phase A's files stay the record.
"""
import csv, os, sys

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


def main(subj):
    _, bullets = rows(os.path.join(subj, "bullets.tsv"))
    if not bullets:
        sys.exit(f"{subj}/bullets.tsv is missing or empty")
    rds = {}
    for b in bullets:
        if b["role"] not in ("ask", "no-part"):
            continue
        for rd in (x.strip() for x in b["root_decision"].split(";") if x.strip()):
            rds.setdefault(rd, set()).add(b["bullet"])
    kinds = {r["id"]: r["kind"] for r in rows(os.path.join(subj, "kinds.tsv"))[1]}
    data = {p: {n: rows(os.path.join(subj, p, n + ".tsv")) for n in ("statements", "gaps", "absences", "terms")}
            for p in PLATFORMS if os.path.isdir(os.path.join(subj, p))}
    for rd, mine in sorted(rds.items()):
        out = os.path.join(subj, "slices", rd)
        os.makedirs(out, exist_ok=True)
        st, gp, ab, tm = [], [], [], []
        for p, d in data.items():
            for r in d["statements"][1]:
                if {x.strip() for x in r["bullet"].split(";")} & mine:
                    st.append([p, kinds.get(r["stmt_id"], "")] + [r.get(c, "") for c in KEEP["statements"]])
            for r in d["gaps"][1]:
                if r["bullet"].strip() in mine:
                    gp.append([p] + [r.get(c, "") for c in KEEP["gaps"]])
            for r in d["absences"][1]:
                if r["bullet"].strip() in mine:
                    ab.append([p, kinds.get(r["absence_id"], "")] + [r.get(c, "") for c in KEEP["absences"]])
            tm += [[p] + [r.get(c, "") for c in KEEP["terms"]] for r in d["terms"][1]]
        write(os.path.join(out, "statements.tsv"), ["platform", "kind"] + KEEP["statements"], st)
        write(os.path.join(out, "gaps.tsv"), ["platform"] + KEEP["gaps"], gp)
        write(os.path.join(out, "absences.tsv"), ["platform", "kind"] + KEEP["absences"], ab)
        write(os.path.join(out, "terms.tsv"), ["platform"] + KEEP["terms"], tm)
        print(f"{rd}\tbullets {''.join(sorted(mine))}\t{len(st)} statements\t{len(gp)} gaps\t{len(ab)} absences\t"
              f"{len(tm)} terms")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1].rstrip("/"))
