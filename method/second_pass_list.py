"""Write the work list of phase B's second pass, one per root decision, from what phases A2 and A3 added.

Usage: python3 -I method/second_pass_list.py SUBJECT_DIR CHECK_OUT

CHECK_OUT is the output folder of `method/check_subject.py` run on the whole subject after A2 and A3, whose
unplaced.tsv lists the statements, by root decision, bullet and platform, that are neither in a variant nor noted.
For each root decision it writes SUBJECT_DIR/b/second-pass/<root decision>/worklist.tsv, a row per task:
- place: a statement unplaced.tsv lists for that decision: phases A2 and A3 added it, or an earlier part left it;
- revisit: a variants row that is `gap`, `absent` or `not covered`, under a point of that decision, whose platform has
  an a2.tsv row for the point; `why` gives that row's statements, gaps and absences;
- reread: a statement b/second-pass.md lists under a rule widened since its part ran, with that rule;
- note: a statement b/second-pass.md lists as not to place, with the reason; the second pass notes it, and places
  nothing for it.
So the second pass prints by id what its list names (`method/subject_slice.py --print RD --ids ...`), and doesn't read
whole slices. Columns: task, id, platform, bullet, vp_id, why.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
PLATFORMS = ("shopify", "salla", "zid", "woocommerce", "bigcommerce")
PREFIX = {"SH": "shopify", "SA": "salla", "ZD": "zid", "WC": "woocommerce", "BC": "bigcommerce"}


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)]


def ids(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


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

    # place, and note: the statements the checker found neither in a variant nor noted
    for r in rows(os.path.join(check_out, "unplaced.tsv")):
        s = r["stmt_id"]
        task, why = ("note", not_place[s]) if s in not_place else ("place", "")
        tasks.setdefault(r["root_decision"], []).append([task, s, r["platform"], r["bullet"], "", why])
    # not-to-place statements already noted or placed still go on the list, so that their row is checked
    listed = {t[1] for v in tasks.values() for t in v}
    for s, why in not_place.items():
        if s not in listed:
            plat = PREFIX.get(s.split("-")[1], "")
            for rd in rds(s):
                tasks.setdefault(rd, []).append(["note", s, plat, ";".join(bullets_of.get(s, [])), "",
                                                 why + " (already placed or noted: check its row)"])

    # revisit: the rows that were gap, absent or not covered, where gap-closing worked the point
    a2 = {}
    for p in PLATFORMS:
        for r in rows(os.path.join(subj, p, "a2.tsv")):
            a2.setdefault((p, r["vp_id"]), []).append(r)
    for v in rows(os.path.join(subj, "variants.tsv")):
        if v["variant"] not in ("gap", "absent", "not covered"):
            continue
        work = a2.get((v["platform"], v["vp_id"]))
        if not work:
            continue
        b = vp_bullet.get(v["vp_id"], "")
        st = sorted({s for w in work for s in ids(w["stmt_ids"])})
        gp = sorted({g for w in work for g in ids(w["gap_ids"])})
        ab = sorted({a for w in work for a in ids(w["absence_ids"])})
        why = f"was {v['variant']}; A2 statements: {';'.join(st) or 'none'}; A2 gaps: {';'.join(gp) or 'none'}; " \
              f"A2 absences: {';'.join(ab) or 'none'}"
        for rd in rd_of.get(b, []):
            tasks.setdefault(rd, []).append(["revisit", v["variant_id"], v["platform"], b, v["vp_id"], why])

    # reread: statements noted under a rule widened since their part ran
    for s, why in reread.items():
        plat = PREFIX.get(s.split("-")[1], "")
        part = why.split(",")[0]
        rd = part.split("-")[0] if part.startswith("RD") else ""
        for d in ([rd] if rd else rds(s)):
            tasks.setdefault(d, []).append(["reread", s, plat, ";".join(bullets_of.get(s, [])), "", why])

    for rd, ts in sorted(tasks.items()):
        d = os.path.join(subj, "b", "second-pass", rd)
        os.makedirs(d, exist_ok=True)
        order = {"place": 0, "revisit": 1, "reread": 2, "note": 3}
        ts.sort(key=lambda t: (order[t[0]], t[2], t[3], t[1]))
        with open(os.path.join(d, "worklist.tsv"), "w", encoding="utf-8") as f:
            f.write("task\tid\tplatform\tbullet\tvp_id\twhy\n")
            for t in ts:
                f.write("\t".join(c.replace("\t", " ") for c in t) + "\n")
        counts = {k: sum(1 for t in ts if t[0] == k) for k in order}
        print(rd, ", ".join(f"{k} {n}" for k, n in counts.items()))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1].rstrip("/"), sys.argv[2])
