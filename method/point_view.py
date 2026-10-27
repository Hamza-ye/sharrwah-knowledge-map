"""Print what phase C reads on one or more variation points of a root decision, or records by id.

Usage: python3 -I method/point_view.py SUBJECT_DIR RD VP_ID [VP_ID ...]
       python3 -I method/point_view.py SUBJECT_DIR --records ID[,ID ...]

For each point: its question and kind of X, then each platform's rows, in the brief's three groups (Salla and Zid,
Shopify and BigCommerce, then WooCommerce). For each row:
- its form, excerpt and evidence (basis_evidence);
- each statement it names, with its kind (SUBJECT_DIR/kinds.tsv), scope and release marker;
- the statements under (h) that name its statements in `conditions`;
- for a `gap` row, what each of its gaps asks; for an `absent` row, what each absence says is absent.
No `note` column is printed.

--records prints statements, gaps and absences whole by id, from any bullet, (h) among them, each with its platform,
kind and the columns a reader needs, but no note. Ids may be separated by commas or spaces.
"""
import csv, os, re, signal, sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # a pipe into head ends quietly
csv.field_size_limit(10**9)
GROUPS = (("salla", "zid"), ("shopify", "bigcommerce"), ("woocommerce",))
PLATFORMS = [p for g in GROUPS for p in g]


def table(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def cut(s, n):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[:n] + f" […{len(s) - n} more]"


class Records:
    def __init__(self, subj):
        self.kind = {r["id"]: r["kind"] for r in table(os.path.join(subj, "kinds.tsv"))}
        self.st, self.gap, self.ab, self.cond = {}, {}, {}, {}
        for p in PLATFORMS:
            for r in table(os.path.join(subj, p, "statements.tsv")):
                self.st[r["stmt_id"]] = dict(r, platform=p)
                if "h" in [b.strip() for b in r["bullet"].split(";")]:
                    for s in ids(r["conditions"]):
                        self.cond.setdefault(s, []).append(r["stmt_id"])
            for r in table(os.path.join(subj, p, "gaps.tsv")):
                self.gap[r["gap_id"]] = dict(r, platform=p)
            for r in table(os.path.join(subj, p, "absences.tsv")):
                self.ab[r["absence_id"]] = dict(r, platform=p)

    def print_record(self, i):
        if i in self.st:
            r = self.st[i]
            print(f"{i} ({r['platform']}, statement, kind {self.kind.get(i, '?')}, bullet {r['bullet']}, placement {r['placement']})")
            print(f"  identifier: {r['identifier']}")
            print(f"  statement: {r['statement']}")
            for c in ("scope", "marker", "conditions"):
                if r[c].strip():
                    print(f"  {c}: {r[c]}")
        elif i in self.gap:
            r = self.gap[i]
            print(f"{i} ({r['platform']}, gap, bullet {r['bullet']}, {r['gap_kind']}, who can: {r['who_can']})")
            print(f"  what is missing: {r['what_is_missing']}")
            print(f"  read: {r['read']}")
            print(f"  route: {r['route']}")
        elif i in self.ab:
            r = self.ab[i]
            print(f"{i} ({r['platform']}, absence, kind {self.kind.get(i, '?')}, bullet {r['bullet']})")
            print(f"  what is absent: {r['what_is_absent']}")
            print(f"  the list: {r['list_cite_ids']}; shown complete by: {r['complete_cite_ids']}")
        else:
            print(f"{i}: no statement, gap or absence of the subject has this id", file=sys.stderr)


def main(subj, rd, vps):
    points = {p["vp_id"]: p for p in table(os.path.join(subj, "b", rd, "variation-points.tsv"))}
    variants = table(os.path.join(subj, "b", rd, "variants.tsv"))
    R = Records(subj)
    for vp in vps:
        p = points.get(vp)
        if not p:
            print(f"{vp}: not a point of b/{rd}/variation-points.tsv")
            continue
        print(f"{vp} ({p['bullet']}) {p['question']}")
        print(f"  kind of X: {p['x_words'].split(' | ')[0]}")
        for plat in PLATFORMS:
            rows = [v for v in variants if v["vp_id"] == vp and v["platform"] == plat]
            print(f"  {plat}:" + ("" if rows else " no row"))
            for v in rows:
                form = v["variant"] if v["variant"] in ("gap", "absent", "not covered") else "answer"
                sids = ids(v["stmt_ids"])
                print(f"    {v['variant_id']} {form} | basis {v['basis'] or '-'} | {len(sids)} statements")
                if form == "answer":
                    print(f"      variant: {cut(v['variant'], 300)}")
                    print(f"      evidence: {cut(v['basis_evidence'], 800)}")
                for s in sids:
                    r = R.st.get(s, {})
                    extra = "".join(f" | {c}: {cut(r.get(c, ''), 90)}" for c in ("scope", "marker") if r.get(c, "").strip())
                    print(f"      {s}: kind {R.kind.get(s, '?')}{extra}")
                for g in ids(v["gap_ids"]):
                    print(f"      gap {g}: {cut(R.gap.get(g, {}).get('what_is_missing', '(not found)'), 400)}")
                for a in ids(v["absence_ids"]):
                    print(f"      absence {a}: {cut(R.ab.get(a, {}).get('what_is_absent', '(not found)'), 400)}")
                hs = []
                for s in sids:
                    for h in R.cond.get(s, []):
                        if h not in hs and h not in sids:
                            hs.append(h)
                for h in hs[:8]:
                    r = R.st[h]
                    print(f"      condition {h}: {cut(r['statement'], 200)}" + (f" [scope: {cut(r['scope'], 80)}]" if r["scope"].strip() else ""))
                if len(hs) > 8:
                    print(f"      conditions also: {';'.join(hs[8:])}")
        print()


if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[2] == "--records":
        R = Records(sys.argv[1].rstrip("/"))
        for i in ids(" ".join(sys.argv[3:])):
            R.print_record(i)
    elif len(sys.argv) < 4:
        sys.exit(__doc__)
    else:
        main(sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3:])
