# Q3's candidate misses, checked against what the evidence repositories hold (Stage 4A, "The check for what it
# misses"; the brief studies/class-model/briefs/Q3-misses.md). Q3's batches searched the concern map's statements
# and inventories; this check reads the repositories themselves, through their own reading guides and indexes first
# (the founder, 30 October), and records what it finds as statements, verbatim and cited at a commit, which only the
# coordinator's amendments from Q3's check cite in the model.
#
# Usage:
#   python3 -I method/q3_misses.py misses [--batch A]   the misses, each with its Q3 rows and what each row's rest says
#   python3 -I method/q3_misses.py check --batch A      checks misses-A.tsv and statements/A/: every quote in its source
import argparse, csv, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, PREFIX, rows
import quote_check

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q3 = os.path.join(MODEL, "q3")
MERGED = os.path.join(MODEL, "merged")
# each miss: its Q3 rows and the thing, in the words of the rows' rests
MISSES = {
    "M-01": (["km:CHK-02", "pay:PAY-02"], "tipping: the buyer adding a tip at checkout, and the merchant setting the tip options"),
    "M-02": (["pay:PAY-36"], "a payment test mode in a store: test orders and simulated payment outcomes, kept out of the store's balances and reports"),
    "M-03": (["km:AIA-02"], "agent identity: an AI agent linking to, or acting as, a buyer's account in the store"),
    "M-04": (["km:LNG-02"], "the admin's own language, right-to-left layout, numerals, date formats and mixed-direction text"),
    "M-05": (["km:SHP-04"], "scheduled delivery: the buyer choosing a delivery date or time slot"),
    "M-06": (["km:SHP-05"], "packages and box sizes: the package dimensions a merchant saves for labels and rates"),
    "M-07": (["km:RET-02"], "return rules the merchant sets: the return window, return fees, restocking fees, final sale"),
    "M-08": (["km:PTN-02"], "handing a store a partner built to its client: its ownership, and its billing"),
    "M-09": (["km:EVO-01", "km:EVO-02"], "each platform's dated record of what it added, changed or removed: changelogs, release notes, editions"),
    "M-10": (["pay:PAY-05"], "try before you buy: the buyer receiving goods before being charged, charged later on a trigger"),
    "M-11": (["pay:PAY-30"], "a buyer refusing a cash-on-delivery order at the door: the shipment's return and its charges"),
    "M-12": (["pay:PAY-31"], "strong buyer authentication (3D Secure) shifting a fraud loss, or chargeback liability, away from the seller"),
    "M-13": (["pay:PAY-75"], "a buyer's own claim of payment: a transfer receipt or proof of payment the buyer submits for an order"),
}
BATCHES = {"A": ["M-01", "M-02", "M-03", "M-04", "M-05", "M-06", "M-07"],
           "B": ["M-08", "M-09", "M-10", "M-11", "M-12", "M-13"]}
RANGE = {"A": (100, 199), "B": (200, 299)}     # each batch's statement numbers, so the two never collide
HEAD = ["miss", "platform", "held", "statements", "place", "capability", "guides", "searched", "capture", "reading"]
S_HEAD = ["stmt_id", "miss", "placement", "identifier", "statement", "scope", "cite_ids", "note"]
C_HEAD = ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"]
PLACEMENTS = {"where", "decides", "responsible", "boundary", "reason"}
KINDS = ("admin route", "admin section", "API group", "plan line", "app category")
ROOTS = {"observed-sh": "/home/user/observed-sh", "observed-sa": "/home/user/observed-sa",
         "other-product-class": os.environ.get("OTHER_PRODUCT_CLASS", "/home/user/other-product-class"),
         "woocommerce-11.2.1": "/home/user/woocommerce-release/11.2.1/woocommerce", "sharrwah-knowledge-map": ROOT}


def semi(s):
    return [x.strip() for x in s.split(";") if x.strip()]


def table(path, head, problems):
    if not os.path.exists(path):
        problems.append(f"no file {os.path.relpath(path, ROOT)}")
        return []
    raw = open(path, encoding="utf-8").read().split("\n")
    name = os.path.relpath(path, ROOT)
    if raw[0].split("\t") != head:
        problems.append(f"{name}: header must be: {' '.join(head)}")
        return []
    out = []
    for i, l in enumerate(raw[1:], 2):
        if not l.strip():
            continue
        f = l.split("\t")
        if len(f) != len(head):
            problems.append(f"{name} line {i}: {len(head)} tab-separated fields (it has {len(f)})")
            continue
        out.append((i, dict(zip(head, f))))
    return out


def cmd_misses(a):
    q3rows = {f"{r['set']}:{r['row_id']}": r for r in rows(os.path.join(Q3, "rows.tsv"))}
    rests = {}
    for p in sorted(glob.glob(os.path.join(Q3, "check-*.tsv"))):
        for r in rows(p):
            rests[f"{r['set']}:{r['row_id']}"] = (os.path.basename(p), r)
    for m in (BATCHES[a.batch] if a.batch else MISSES):
        rids, thing = MISSES[m]
        print(f"{m}: {thing}")
        for rid in rids:
            f, r = rests[rid]
            print(f"   {rid} ({f}, {r['result']}{' / ' + r['rest'] if r['rest'] else ''}): {q3rows[rid]['question']}")
            print(f"      its rest: {r['what_would_settle_it']}")
            print(f"      its basis: {r['basis']}")


def cmd_check(a):
    problems = []
    b = a.batch
    caps = {r["cap_id"] for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    lo, hi = RANGE[b]
    stmts, cites = {}, {}
    for p in PLATFORMS:
        x = PREFIX[p]
        for i, r in table(os.path.join(Q3, "statements", b, p, "citations.tsv"), C_HEAD, problems) \
                if os.path.exists(os.path.join(Q3, "statements", b, p)) else []:
            w = f"statements/{b}/{p}/citations.tsv line {i}"
            m = re.match(rf"^Q3-{x}-C(\d+)$", r["cite_id"])
            if not m or not lo <= int(m.group(1)) <= hi:
                problems.append(f"{w}: cite_id is Q3-{x}-C<n>, n from {lo} to {hi}")
            if r["cite_id"] in cites:
                problems.append(f"{w}: {r['cite_id']} again")
            if not re.match(r"^(https?://|(observed-sh|observed-sa|other-product-class)@[0-9a-f]{7,40}:|woocommerce-11\.2\.1:)", r["source"]):
                problems.append(f"{w}: source is a captured page's address, or <repository>@<commit>:<path> (woocommerce-11.2.1:<path> for the release)")
            if not r["quote"].strip():
                problems.append(f"{w}: no quote")
            cites[r["cite_id"]] = (w, r)
        for i, r in table(os.path.join(Q3, "statements", b, p, "statements.tsv"), S_HEAD, problems) \
                if os.path.exists(os.path.join(Q3, "statements", b, p)) else []:
            w = f"statements/{b}/{p}/statements.tsv line {i}"
            m = re.match(rf"^Q3-{x}-(\d+)$", r["stmt_id"])
            if not m or not lo <= int(m.group(1)) <= hi:
                problems.append(f"{w}: stmt_id is Q3-{x}-<n>, n from {lo} to {hi}")
            if r["stmt_id"] in stmts:
                problems.append(f"{w}: {r['stmt_id']} again")
            if r["miss"] not in BATCHES[b]:
                problems.append(f"{w}: miss is one of this batch's: {', '.join(BATCHES[b])}")
            if r["placement"] not in PLACEMENTS:
                problems.append(f"{w}: placement is one of {', '.join(sorted(PLACEMENTS))}")
            if not r["statement"].strip():
                problems.append(f"{w}: no statement")
            cs = semi(r["cite_ids"])
            if not cs or any(c not in cites for c in cs):
                problems.append(f"{w}: cite_ids name this platform's citations, `;`-separated")
            stmts[r["stmt_id"]] = (w, r, p)
    # each quote in its source, and each statement inside one of its quotes
    S = quote_check.Sources(ROOTS, [])
    for cid, (w, r) in sorted(cites.items()):
        res, why, share = S.check_quote(r["quote"], r["source"], r["locator"])
        if not res.startswith("found"):
            problems.append(f"{w}: the quote is not found in {r['source']} ({res}{'; ' + why if why else ''})")
    for sid, (w, r, p) in sorted(stmts.items()):
        st = quote_check.norm(quote_check.md_plain(r["statement"])).casefold()
        qs = [quote_check.norm(quote_check.md_plain(cites[c][1]["quote"])).casefold() for c in semi(r["cite_ids"]) if c in cites]
        if qs and not any(st in q for q in qs):
            problems.append(f"{w}: the statement is not word for word inside its citation's quote")
    used = set()
    seen = set()
    for i, r in table(os.path.join(Q3, f"misses-{b}.tsv"), HEAD, problems):
        w = f"misses-{b}.tsv line {i}"
        k = (r["miss"], r["platform"])
        if r["miss"] not in BATCHES[b] or r["platform"] not in PLATFORMS:
            problems.append(f"{w}: miss is one of {', '.join(BATCHES[b])}, platform one of {', '.join(PLATFORMS)}"); continue
        if k in seen:
            problems.append(f"{w}: {r['miss']} on {r['platform']} again")
        seen.add(k)
        ss = semi(r["statements"])
        if r["held"] not in ("yes", "no"):
            problems.append(f"{w}: held is yes or no")
        if r["held"] == "yes":
            if not ss:
                problems.append(f"{w}: held names the statements that hold it")
            if r["capture"].strip():
                problems.append(f"{w}: capture is for a miss not held")
        if r["held"] == "no":
            if ss:
                problems.append(f"{w}: a miss not held names no statement")
            if not r["capture"].strip():
                problems.append(f"{w}: not held names the run that could capture it, or none and why")
        for s in ss:
            if s not in stmts:
                problems.append(f"{w}: {s} is not a statement of statements/{b}/")
            elif stmts[s][2] != r["platform"] or stmts[s][1]["miss"] != r["miss"]:
                problems.append(f"{w}: {s} is another platform's or miss's statement")
            used.add(s)
        if r["place"] != "none":
            for x in semi(r["place"]):
                m = re.match(r"^(" + "|".join(KINDS) + r"): (Q3-[A-Z]{2}-\d+)$", x)
                if not m:
                    problems.append(f"{w}: place is none, or `<kind>: <statement id>`, `;`-separated, kind one of {', '.join(KINDS)}")
                elif m.group(2) not in ss:
                    problems.append(f"{w}: {m.group(2)} in place is among the row's statements")
        if r["capability"] not in caps and r["capability"] not in ("new", "none"):
            problems.append(f"{w}: capability is a cap_id of the merged model, new, or none")
        if r["held"] == "yes" and r["capability"] == "none":
            problems.append(f"{w}: a held miss names the capability whose thing it is, or new")
        if not r["guides"].strip():
            problems.append(f"{w}: guides names the reading guides and indexes read (the founder, 30 October)")
        if not r["searched"].strip():
            problems.append(f"{w}: searched names the searches run, with their terms")
        if not r["reading"].strip():
            problems.append(f"{w}: reading says, as a reading, what the row holds")
    for m in BATCHES[b]:
        for p in PLATFORMS:
            if (m, p) not in seen:
                problems.append(f"{m} on {p} has no line in misses-{b}.tsv")
    for s in sorted(set(stmts) - used):
        problems.append(f"{s} is named by no line of misses-{b}.tsv")
    for p in problems:
        print("PROBLEM", p)
    print(f"{len(seen)} of {len(BATCHES[b]) * len(PLATFORMS)} lines, {len(stmts)} statements, {len(cites)} citations; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("misses"); s.add_argument("--batch", choices=sorted(BATCHES)); s.set_defaults(f=cmd_misses)
    s = sub.add_parser("check"); s.add_argument("--batch", choices=sorted(BATCHES), required=True); s.set_defaults(f=cmd_check)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
