"""Copy what is already recorded for a subject into the subject's folder, for its phase A agents.

Usage: python3 -I method/seed_subject.py SUBJECT_DIR

Reads SUBJECT_DIR/concerns.tsv: `platform`, `concern_id`, `lines` (the concern map's statements.tsv line numbers to
take, `;`-separated; empty takes every statement of the concern), `root_decisions` and `note`. And, if it exists,
SUBJECT_DIR/subjects-from.tsv: `subject` (an earlier subject, such as S-01), `bullets` (`;`-separated: its statements
under any of them are taken), `root_decisions` and `note`. For each platform it writes SUBJECT_DIR/<platform>/:
- recorded.tsv: each statement as the concern map or the earlier subject holds it, with where it is held (`held_in`:
  the concern and the line of the concern map's statements.tsv, or the earlier subject's statement id), its release
  `marker` (the concern map records none), and `from`,
  the value a phase A statement copied from it takes: `index:<concern_id>:<index cite_id>`, for its first citation,
  or the earlier subject's statement id;
- recorded-citations.tsv: each citation those statements cite, unchanged.

The concern map's and the earlier subjects' statements and quotes were checked word for word against their sources
(studies/concern-map/README.md; method/check_subject.py). This copies them; it decides nothing about what bears on
the subject.
"""
import csv, os, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(SKM, "studies", "concern-map", "platforms")
PLATFORMS = ("shopify", "salla", "zid", "woocommerce", "bigcommerce")
HEAD = ["rec", "held_in", "root_decisions", "placement", "identifier", "statement", "scope", "marker", "cite_ids", "from",
        "note"]


def rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def records(path):
    head, *body = rows(path)
    return head, [dict(zip(head, r)) for r in body if any(c.strip() for c in r)]


def write(path, head, body):
    with open(path, "w", encoding="utf-8", newline="") as f:
        for r in [head] + body:
            if any("\t" in c or "\n" in c for c in r):
                sys.exit(f"{path}: a field holds a tab or a newline: {r[:3]}")
            f.write("\t".join(r) + "\n")


def from_index(plat, concerns, out, cite):
    """The concern map's statements of the given concerns, with the line each is on."""
    st = rows(os.path.join(INDEX, plat, "statements.tsv"))
    known = {r["concern_id"] for r in records(os.path.join(INDEX, plat, "concerns.tsv"))[1]}
    got = {}
    for n, r in enumerate(st[1:], start=2):              # n: the line in the file, the header being line 1
        rec = dict(zip(st[0], r))
        if rec.get("concern_id") not in concerns:
            continue
        lines, rds = concerns[rec["concern_id"]]
        if lines and n not in lines:
            continue
        got.setdefault(rec["concern_id"], set()).add(n)
        cids = [c for c in rec["cite_ids"].split(";") if c]
        out.append([rds, rec["placement"], rec["identifier"], rec["statement"], rec["scope"], "", rec["cite_ids"],
                    f"index:{rec['concern_id']}:{cids[0]}", rec["note"], f"{rec['concern_id']} line {n}"])
        cite(cids, f"statements.tsv line {n}")
    for cid, (lines, _) in concerns.items():
        if cid not in known:
            sys.exit(f"{plat}: {cid} is not a concern of the concern map")
        if not got.get(cid):
            sys.exit(f"{plat}: {cid} has no statements")
        if lines - got[cid]:
            sys.exit(f"{plat}: {cid}'s lines {sorted(lines - got[cid])} are not its statements")


def from_subject(plat, e, out, cite):
    """An earlier subject's statements under the given bullets."""
    d = os.path.join(SKM, "studies", "subjects", e["subject"], plat)
    if not os.path.isdir(d):
        return
    bullets = {b.strip() for b in e["bullets"].split(";") if b.strip()}
    for rec in records(os.path.join(d, "statements.tsv"))[1]:
        if not bullets & {b.strip() for b in rec["bullet"].split(";")}:
            continue
        cids = [c for c in rec["cite_ids"].split(";") if c]
        note = f"{e['subject']}, bullet {rec['bullet']}" + (f"; {rec['note']}" if rec["note"] else "")
        out.append([e["root_decisions"], rec["placement"], rec["identifier"], rec["statement"], rec["scope"],
                    rec["marker"], rec["cite_ids"], rec["stmt_id"], note, f"{e['subject']} {rec['stmt_id']}"])
        cite(cids, rec["stmt_id"])


def seed(subj, plat, concerns, earlier):
    out, used, seen = [], [], set()
    ihead, icites = records(os.path.join(INDEX, plat, "citations.tsv"))
    pool = {c["cite_id"]: c for c in icites}
    for e in earlier:
        p = os.path.join(SKM, "studies", "subjects", e["subject"], plat, "citations.tsv")
        if os.path.exists(p):
            h, cs = records(p)
            if h != ihead:
                sys.exit(f"{p} has the header {h}, not the concern map's {ihead}")
            pool.update({c["cite_id"]: c for c in cs})

    def cite(cids, where):
        for c in cids:
            if c not in pool:
                sys.exit(f"{plat}: {where} cites {c}, which its citations don't hold")
            if c not in seen:
                seen.add(c)
                used.append([pool[c][h] for h in ihead])

    if concerns:
        from_index(plat, concerns, out, cite)
    for e in earlier:
        from_subject(plat, e, out, cite)
    if not out:
        return
    body = [[f"R{i:03d}", r[9]] + r[:9] for i, r in enumerate(out, start=1)]
    d = os.path.join(subj, plat)
    os.makedirs(d, exist_ok=True)
    write(os.path.join(d, "recorded.tsv"), HEAD, body)
    write(os.path.join(d, "recorded-citations.tsv"), ihead, used)
    print(f"{plat}\t{len(concerns)} concerns\t{len(out)} statements\t{len(used)} citations")


def main(subj):
    want = {}
    for r in records(os.path.join(subj, "concerns.tsv"))[1]:
        if r["platform"] not in PLATFORMS:
            sys.exit(f"concerns.tsv: platform '{r['platform']}' is not one of {PLATFORMS}")
        lines = {int(x) for x in r["lines"].split(";") if x.strip()}
        want.setdefault(r["platform"], {})[r["concern_id"]] = (lines, r["root_decisions"])
    sf = os.path.join(subj, "subjects-from.tsv")
    earlier = records(sf)[1] if os.path.exists(sf) else []
    for plat in PLATFORMS:
        seed(subj, plat, want.get(plat, {}), earlier)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1].rstrip("/"))
