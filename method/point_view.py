"""Print what phase C reads on one or more variation points of a root decision, or records by id.

Usage: python3 -I method/point_view.py SUBJECT_DIR RD VP_ID [VP_ID ...] [--full] [--platform P]
       python3 -I method/point_view.py SUBJECT_DIR --records ID[,ID ...]

For each point: its question and kind of X, then each platform's rows, in the brief's three groups (Salla and Zid,
Shopify and BigCommerce, then WooCommerce). For each row:
- its form, excerpt and evidence (basis_evidence);
- the statements it names, grouped by kind (SUBJECT_DIR/kinds.tsv), with their scopes and release markers;
- the statements under (h) that name its statements in `conditions`;
- for a `gap` row, what each of its gaps asks; for an `absent` row, what each absence says is absent.
--platform P prints one platform's rows only, for a large point. A row's evidence is cut at 800 characters, and its excerpt at 300, unless --full is given. A condition's text is printed
once per point, at its first row; later rows name it by id. No `note` column is printed.

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


def main(subj, rd, vps, full=False, only=None):
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
        shown = set()
        for plat in [x for x in PLATFORMS if not only or x == only]:
            rows = [v for v in variants if v["vp_id"] == vp and v["platform"] == plat]
            print(f"  {plat}:" + ("" if rows else " no row"))
            for v in rows:
                form = v["variant"] if v["variant"] in ("gap", "absent", "not covered") else "answer"
                sids = ids(v["stmt_ids"])
                print(f"    {v['variant_id']} {form} | basis {v['basis'] or '-'} | {len(sids)} statements")
                if form == "answer":
                    print(f"      variant: {cut(v['variant'], 10**6 if full else 300)}")
                    print(f"      evidence: {cut(v['basis_evidence'], 10**6 if full else 800)}")
                by_kind = {}
                for x in sids:
                    by_kind.setdefault(R.kind.get(x, "?"), []).append(x)
                if sids:
                    print("      statements by kind: " + " | ".join(f"{k}: {';'.join(v)}" for k, v in by_kind.items()))
                scopes = {}
                for x in sids:
                    sc = R.st.get(x, {}).get("scope", "").strip()
                    if sc:
                        scopes.setdefault(sc, []).append(x)
                for sc, xs in list(scopes.items())[:6]:
                    print(f"      scope {cut(sc, 100)}: {';'.join(xs)}")
                if len(scopes) > 6:
                    print(f"      {len(scopes) - 6} more scopes (print the statements with --records)")
                marks = [f"{x} ({R.st[x]['marker']})" for x in sids if x in R.st and R.st[x]["marker"].strip()]
                if marks:
                    print(f"      release markers: {'; '.join(marks)}")
                for g in ids(v["gap_ids"]):
                    print(f"      gap {g}: {cut(R.gap.get(g, {}).get('what_is_missing', '(not found)'), 400)}")
                for a in ids(v["absence_ids"]):
                    print(f"      absence {a}: {cut(R.ab.get(a, {}).get('what_is_absent', '(not found)'), 400)}")
                hs = []
                for s in sids:
                    for h in R.cond.get(s, []):
                        if h not in hs and h not in sids:
                            hs.append(h)
                again = [h for h in hs if h in shown]
                for h in [h for h in hs if h not in shown][:8]:
                    r = R.st[h]
                    shown.add(h)
                    print(f"      condition {h}: {cut(r['statement'], 200)}" + (f" [scope: {cut(r['scope'], 80)}]" if r["scope"].strip() else ""))
                rest = [h for h in hs if h not in shown]
                if again:
                    print(f"      conditions printed above: {';'.join(again)}")
                if rest:
                    print(f"      conditions also (print with --records): {';'.join(rest)}")
        print()


if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[2] == "--records":
        R = Records(sys.argv[1].rstrip("/"))
        for i in ids(" ".join(sys.argv[3:])):
            R.print_record(i)
    elif len(sys.argv) < 4:
        sys.exit(__doc__)
    else:
        rest, only = sys.argv[3:], None
        if "--platform" in rest:
            k = rest.index("--platform")
            only = rest[k + 1] if k + 1 < len(rest) else sys.exit("--platform names a platform")
            if only not in PLATFORMS:
                sys.exit(f"--platform: {only} is not one of {', '.join(PLATFORMS)}")
            rest = rest[:k] + rest[k + 2:]
        main(sys.argv[1].rstrip("/"), sys.argv[2], [a for a in rest if a != "--full"], full="--full" in rest, only=only)
