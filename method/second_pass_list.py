"""Write the work list of phase B's second pass, one per root decision, from what phases A2 and A3 added; or check a
root decision's ledger against its work list.

Usage: python3 -I method/second_pass_list.py SUBJECT_DIR CHECK_OUT
       python3 -I method/second_pass_list.py SUBJECT_DIR --check

CHECK_OUT is the output folder of `method/check_subject.py` run on the whole subject after A2 and A3, whose
unplaced.tsv lists the statements, by root decision, bullet and platform, that are neither in a variant nor noted.
For each root decision it writes SUBJECT_DIR/b/second-pass/<root decision>/worklist.tsv, a row per task, in this order:
- revisit: a variants row that is `gap`, `absent` or `not covered`, under a point of that decision, whose platform has
  an a2.tsv row for the point. `why` gives that row's statements: first the leads, those under the point's own bullet,
  which this task places or notes under that bullet; then the others, which aren't this task's (those under another
  bullet of the decision have their own `place` rows; those outside its slice are left). Then its gaps and absences;
- place: a statement unplaced.tsv lists for that decision, under the `bullet` given, that no revisit takes as a lead:
  phases A2 and A3 added it, or an earlier part left it;
- reread: a statement b/second-pass.md lists under a rule widened since its part ran, with that rule, one row per
  bullet of the decision it carries;
- note: a statement b/second-pass.md lists as not to place, with the reason; the second pass notes it, and places
  nothing for it.
So the second pass prints by id what its list names (`method/subject_slice.py --print RD --ids ...`), and doesn't read
whole slices. Columns: task, id, platform, bullet, vp_id, why.

--check reads each root decision's ledger, b/<root decision>/done.tsv (task, id, bullet, outcome; written by
`method/variants_edit.py done`), and lists the revisit, reread and note tasks of its work list that have no row there.
`place` tasks are checked by the checker's unplaced.tsv instead.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
PLATFORMS = ("shopify", "salla", "zid", "woocommerce", "bigcommerce")
PREFIX = {"SH": "shopify", "SA": "salla", "ZD": "zid", "WC": "woocommerce", "BC": "bigcommerce"}
ORDER = {"revisit": 0, "place": 1, "reread": 2, "note": 3}


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)]


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def expand(text):
    """Statement ids in a cell of b/second-pass.md: single ids and ranges such as S02-SH-441 to S02-SH-446."""
    out = []
    for a, b in re.findall(r"(S\d\d-[A-Z]{2}-\d{3,4})(?:\s+to\s+(S\d\d-[A-Z]{2}-\d{3,4}))?", text):
        if b:
            pre, lo, hi = a.rsplit("-", 1)[0], int(a.rsplit("-", 1)[1]), int(b.rsplit("-", 1)[1])
            out += [f"{pre}-{n:03d}" for n in range(lo, hi + 1)]
        else:
            out.append(a)
    return out


def main(subj, check_out):
    rd_of = {r["bullet"]: [x.strip() for x in r["root_decision"].split(";")] for r in rows(os.path.join(subj, "bullets.tsv"))}
    rd_bullets = {}
    for b, rds in rd_of.items():
        for d in rds:
            rd_bullets.setdefault(d, set()).add(b)
    vp_bullet = {r["vp_id"]: r["bullet"] for r in rows(os.path.join(subj, "variation-points.tsv"))}
    tasks = {}                                     # root decision -> [task rows]
    bullets_of = {r["stmt_id"]: [b.strip() for b in r["bullet"].split(";") if b.strip()]
                  for p in PLATFORMS for r in rows(os.path.join(subj, p, "statements.tsv"))}

    def rds(stmt):                                 # the root decisions of a statement's bullets, (h) aside
        return sorted({d for b in bullets_of.get(stmt, []) if b != "h" for d in rd_of.get(b, [])})

    # b/second-pass.md: its tables of statements to read again, and of statements not to place
    reread, not_place = {}, {}
    sp = os.path.join(subj, "b", "second-pass.md")
    table = None
    for line in (open(sp, encoding="utf-8").read().splitlines() if os.path.exists(sp) else []):
        if line.startswith("**Statements not to place**"):
            table = "not"
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else []
        if len(cells) < 2 or set(cells[0]) <= set("- ") or cells[0] in ("Part", "Statements"):
            continue
        if table == "not":
            for s in expand(cells[0]):
                not_place[s] = cells[1]
        else:
            for s in expand(cells[1]):
                reread[s] = f"{cells[0]}: {cells[2]}"

    # revisit: the rows that were gap, absent or not covered, where gap-closing worked the point
    a2 = {}
    for p in PLATFORMS:
        for r in rows(os.path.join(subj, p, "a2.tsv")):
            a2.setdefault((p, r["vp_id"]), []).append(r)
    taken = set()                                  # (root decision, statement, bullet) a revisit places or notes
    for v in rows(os.path.join(subj, "variants.tsv")):
        if v["variant"] not in ("gap", "absent", "not covered"):
            continue
        work = a2.get((v["platform"], v["vp_id"]))
        if not work:
            continue
        b = vp_bullet.get(v["vp_id"], "")
        st = sorted({s for w in work for s in ids(w["stmt_ids"])} - set(not_place))   # those have their own note task
        gp = sorted({g for w in work for g in ids(w["gap_ids"])})
        ab = sorted({a for w in work for a in ids(w["absence_ids"])})
        for rd in rd_of.get(b, []):
            leads = [s for s in st if b in bullets_of.get(s, [])]
            other = [s for s in st if b not in bullets_of.get(s, []) and rd in rds(s)]
            outside = [s for s in st if b not in bullets_of.get(s, []) and rd not in rds(s)]
            taken |= {(rd, s, b) for s in leads}
            why = (f"was {v['variant']}; leads under ({b}), which this task places or notes: {';'.join(leads) or 'none'}; "
                   f"A2 statements under this decision's other bullets, with their own tasks: {';'.join(other) or 'none'}; "
                   f"A2 statements outside this decision's slice, left: {';'.join(outside) or 'none'}; "
                   f"A2 gaps: {';'.join(gp) or 'none'}; A2 absences: {';'.join(ab) or 'none'}")
            tasks.setdefault(rd, []).append(["revisit", v["variant_id"], v["platform"], b, v["vp_id"], why])

    # place, and note: the statements the checker found neither in a variant nor noted, but a revisit's leads
    for r in rows(os.path.join(check_out, "unplaced.tsv")):
        s, rd, b = r["stmt_id"], r["root_decision"], r["bullet"]
        if s in not_place:
            tasks.setdefault(rd, []).append(["note", s, r["platform"], b, "", not_place[s]])
        elif (rd, s, b) not in taken:
            tasks.setdefault(rd, []).append(["place", s, r["platform"], b, "", ""])
    # not-to-place statements already noted or placed still go on the list, so that their row is checked
    listed = {t[1] for v in tasks.values() for t in v if t[0] == "note"}
    for s, why in not_place.items():
        if s not in listed:
            plat = PREFIX.get(s.split("-")[1], "")
            for rd in rds(s):
                for b in [b for b in bullets_of.get(s, []) if b in rd_bullets.get(rd, set())]:
                    tasks.setdefault(rd, []).append(["note", s, plat, b, "", why + " (already placed or noted: check its row)"])

    # reread: statements noted under a rule widened since their part ran, one row per bullet of the decision
    for s, why in reread.items():
        plat = PREFIX.get(s.split("-")[1], "")
        part = why.split(",")[0]
        rd = part.split("-")[0] if part.startswith("RD") else ""
        for d in ([rd] if rd else rds(s)):
            for b in [b for b in bullets_of.get(s, []) if b in rd_bullets.get(d, set()) and b != "h"]:
                tasks.setdefault(d, []).append(["reread", s, plat, b, "", why])

    for rd, ts in sorted(tasks.items()):
        d = os.path.join(subj, "b", "second-pass", rd)
        os.makedirs(d, exist_ok=True)
        ts.sort(key=lambda t: (ORDER[t[0]], t[2], t[3], t[1]))
        with open(os.path.join(d, "worklist.tsv"), "w", encoding="utf-8") as f:
            f.write("task\tid\tplatform\tbullet\tvp_id\twhy\n")
            for t in ts:
                f.write("\t".join(c.replace("\t", " ") for c in t) + "\n")
        counts = {k: sum(1 for t in ts if t[0] == k) for k in ORDER}
        print(rd, ", ".join(f"{k} {n}" for k, n in counts.items()))


def check(subj):
    """List the revisit, reread and note tasks of each work list that have no row in their ledger."""
    base = os.path.join(subj, "b", "second-pass")
    bad = 0
    for rd in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        wl = rows(os.path.join(base, rd, "worklist.tsv"))
        if not wl:
            continue
        done = {(r["task"], r["id"], r["bullet"]) for r in rows(os.path.join(subj, "b", rd, "done.tsv"))}
        left = [t for t in wl if t["task"] != "place" and (t["task"], t["id"], t["bullet"]) not in done]
        bad += len(left)
        print(f"{rd}: {len(left)} of its revisit, reread and note tasks have no row in b/{rd}/done.tsv")
        for t in left[:40]:
            print(f"  {t['task']} {t['id']} ({t['bullet']}) {t['platform']}")
    return bad


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[2] == "--check":
        sys.exit(1 if check(sys.argv[1].rstrip("/")) else 0)
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1].rstrip("/"), sys.argv[2])
