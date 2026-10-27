"""Write, show and check one root decision's phase C rows, `c/<RD>/analysis.tsv`, one row per variation point.

Usage: python3 -I method/analysis_edit.py SUBJECT_DIR RD set VP_ID --cause TAG [--FIELD TEXT ...]
       python3 -I method/analysis_edit.py SUBJECT_DIR RD show VP_ID
       python3 -I method/analysis_edit.py SUBJECT_DIR RD check [VP_ID ...]

`set` writes the point's row, or replaces it whole: give every field the row needs each time. The fields, as flags:
  --cause            one of the brief's tags: no difference; market, named rule; maturity; business model;
                     market, pattern; vendor choice; unknown
  --cause-basis      stmt_ids, `;`-separated
  --scopes           scopes_compared
  --reading          cause_reading, one sentence beginning "Reading:"
  --shared           the answers two or more platforms share, each with its platforms
  --blocked-by       variant_ids of the point's `gap`, `not covered` or `absent` rows that leave a comparison open
  --coexistence      one entry per platform, `;`-separated: `salla=A; zid=A+B; shopify=B; bigcommerce=D;
                     woocommerce=unknown`; letters A to D joined by `+`, or `unknown` or D alone
  --coexistence-basis  stmt_ids or variant_ids
  --general          general_variant: variant_ids, or nothing
  --follows          the rule table's results, each in its exact words, `;`-separated, or `none applies`
  --expensive        expensive_because: why, or `cheap: ` and why
  --founder-item     the founder's question, where a decision for the founder follows
  --depends-on       vp_ids whose founder item, once answered, would settle this one
  --note             anything else
It refuses an unknown tag, a coexistence entry it can't read, a phrase not in the rule table, an id that is no
statement of the subject nor row of the point, and a `blocked_by` row that is an answer. Each command holds a lock on
the folder while it reads and writes, so two parts of one root decision can write at once.

`check` runs the same checks on every row, or on the points named, and lists the points of the root decision's
`b/<RD>/variation-points.tsv` that have no row. It exits 1 if it finds a problem.
"""
import csv, fcntl, os, re, sys

csv.field_size_limit(10**9)
PLATFORMS = ("salla", "zid", "shopify", "bigcommerce", "woocommerce")
HEAD = ["vp_id", "cause", "cause_basis", "scopes_compared", "cause_reading", "shared", "blocked_by", "coexistence",
        "coexistence_basis", "general_variant", "follows", "expensive_because", "founder_item", "depends_on", "note"]
FLAGS = {"--cause": "cause", "--cause-basis": "cause_basis", "--scopes": "scopes_compared", "--reading": "cause_reading",
         "--shared": "shared", "--blocked-by": "blocked_by", "--coexistence": "coexistence",
         "--coexistence-basis": "coexistence_basis", "--general": "general_variant", "--follows": "follows",
         "--expensive": "expensive_because", "--founder-item": "founder_item", "--depends-on": "depends_on",
         "--note": "note"}
CAUSES = ("no difference", "market, named rule", "maturity", "business model", "market, pattern", "vendor choice",
          "unknown")
FOLLOWS = ("a commonality, carried as the references carry it",
           "the platform carries all the variants at once",
           "a variation point behind one interface, bound per market, store or plan",
           "bound per product",
           "a variation point bound per market",
           "a decision for the founder, on a recommendation",
           "left to the build",
           "kept open as a variation point until evidence settles it",
           "none applies")


def table(path):
    if not os.path.exists(path):
        return [], []
    with open(path, encoding="utf-8", newline="") as f:
        r = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    return (r[0], [dict(zip(r[0], x)) for x in r[1:] if any(c.strip() for c in x)]) if r else ([], [])


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


class Subject:
    def __init__(self, subj, rd):
        self.dir = os.path.join(subj, "c", rd)
        os.makedirs(self.dir, exist_ok=True)
        self.path = os.path.join(self.dir, "analysis.tsv")
        _, pts = table(os.path.join(subj, "b", rd, "variation-points.tsv"))
        self.points = [p["vp_id"] for p in pts]
        _, var = table(os.path.join(subj, "b", rd, "variants.tsv"))
        self.rows = {}
        for v in var:
            self.rows.setdefault(v["vp_id"], {})[v["variant_id"]] = v
        self.stmts = set()
        for p in PLATFORMS:
            _, st = table(os.path.join(subj, p, "statements.tsv"))
            self.stmts |= {r["stmt_id"] for r in st}
            _, ab = table(os.path.join(subj, p, "absences.tsv"))
            self.stmts |= {r.get("absence_id", "") for r in ab}

    def problems(self, r):
        out, vp = [], r["vp_id"]
        if vp not in self.points:
            out.append(f"{vp} is not a point of this root decision")
        if r["cause"] not in CAUSES:
            out.append(f"cause {r['cause']!r} is not one of the brief's tags")
        for f in ("cause_basis", "coexistence_basis"):
            for x in ids(r[f]):
                if x not in self.stmts and x not in self.rows.get(vp, {}):
                    out.append(f"{f}: {x} is no statement or absence of the subject, nor a row of {vp}")
        for x in ids(r["general_variant"]):
            if x not in self.rows.get(vp, {}):
                out.append(f"general_variant: {x} is not a row of {vp}")
        for x in ids(r["blocked_by"]):
            row = self.rows.get(vp, {}).get(x)
            if not row:
                out.append(f"blocked_by: {x} is not a row of {vp}")
            elif row["variant"] not in ("gap", "not covered", "absent"):
                out.append(f"blocked_by: {x} is an answer row, not gap, not covered or absent")
        seen = []
        for e in [e.strip() for e in r["coexistence"].split(";") if e.strip()]:
            m = re.fullmatch(r"(\w+)=(unknown|D|[ABC](?:\+[ABCD])*)", e)
            if not m or m.group(1) not in PLATFORMS:
                out.append(f"coexistence entry {e!r}: write platform=letters, letters A to D joined by +, or unknown")
            else:
                seen.append(m.group(1))
                if "D" in m.group(2) and m.group(2) != "D":
                    out.append(f"coexistence entry {e!r}: D stands alone")
        missing = [p for p in PLATFORMS if p not in seen]
        if missing:
            out.append(f"coexistence has no entry for {', '.join(missing)}")
        for f in [x.strip() for x in r["follows"].split(";") if x.strip()]:
            if f not in FOLLOWS:
                out.append(f"follows: {f!r} is not in the rule table's words")
        if not r["follows"].strip():
            out.append("follows is empty: write `none applies` if no rule applies")
        if "a decision for the founder, on a recommendation" in r["follows"] and not r["founder_item"].strip():
            out.append("a decision for the founder follows, but founder_item is empty")
        if r["cause_reading"].strip() and not r["cause_reading"].startswith("Reading:"):
            out.append("cause_reading must begin 'Reading:'")
        for x in ids(r["depends_on"]):
            if not re.fullmatch(r"S\d\d-VP-\d+", x):
                out.append(f"depends_on: {x} is not a vp_id")
        return out


def main(subj, rd, cmd, args):
    S = Subject(subj, rd)
    head, recs = table(S.path)
    if head and head != HEAD:
        sys.exit(f"analysis.tsv's header is {head}, expected {HEAD}")
    if cmd == "set":
        if not args:
            sys.exit(__doc__)
        r = {h: "" for h in HEAD}
        r["vp_id"] = args[0]
        k = 1
        while k < len(args):
            if args[k] not in FLAGS or k + 1 >= len(args):
                sys.exit(f"unknown flag or missing value: {args[k]}")
            r[FLAGS[args[k]]] = clean(args[k + 1])
            k += 2
        bad = S.problems(r)
        if bad:
            sys.exit("not written:\n  " + "\n  ".join(bad))
        recs = [x for x in recs if x["vp_id"] != r["vp_id"]] + [r]
        order = {p: i for i, p in enumerate(S.points)}
        recs.sort(key=lambda x: order.get(x["vp_id"], 10**6))
        tmp = S.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write("\t".join(HEAD) + "\n")
            for x in recs:
                f.write("\t".join(clean(x.get(h, "")) for h in HEAD) + "\n")
        os.replace(tmp, S.path)
        print(f"{r['vp_id']}: written ({r['cause']}; {r['follows']})")
    elif cmd == "show":
        for x in recs:
            if x["vp_id"] in args:
                for h in HEAD:
                    print(f"{h}: {x[h]}")
    elif cmd == "check":
        bad = 0
        for x in recs:
            if args and x["vp_id"] not in args:
                continue
            for p in S.problems(x):
                print(f"{x['vp_id']}: {p}")
                bad += 1
        done = {x["vp_id"] for x in recs}
        left = [p for p in S.points if p not in done and (not args or p in args)]
        print(f"{len(done)} points have a row; {len(left)} have none" + (f": {', '.join(left)}" if left else ""))
        sys.exit(1 if bad else 0)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    subj, rd = sys.argv[1].rstrip("/"), sys.argv[2]
    folder = os.path.join(subj, "c", rd)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, ".edit.lock"), "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        main(subj, rd, sys.argv[3], sys.argv[4:])
