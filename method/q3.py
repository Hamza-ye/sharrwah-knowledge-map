"""Q3's check for what the class's model misses (PLAN.md, Stage 4A and section 6, "Q3's rows"; the brief
`studies/class-model/briefs/Q3-check.md`).

    python3 -I method/q3.py rows                      build studies/class-model/q3/rows.tsv from the rows at e4d5cee
    python3 -I method/q3.py slice --rows ID,ID ...    each row with the capabilities that may answer it (an id is
                                                      km:ID or pay:ID, since both sets have PAY-01; a bare id takes both)
    python3 -I method/q3.py slice --area PAY [--from N --to M]
    python3 -I method/q3.py check [--rows ID,ID ...]  check studies/class-model/q3-check.tsv
    python3 -I method/q3.py unasked                   the capabilities no row asks about (Q3's item 3)

A row is known by its set and id together. The rows are read only for their id, question and needed_by: their founder lane is not current (the founder, 29
October), and their other columns hold citations that are not trusted. `slice` reads the model's merged files.
"""
import argparse, csv, io, math, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows, fold, ids

ROOT = os.path.abspath(os.path.join(MODEL, "..", ".."))
ROWS = os.path.join(MODEL, "q3", "rows.tsv")
OUT = os.path.join(MODEL, "q3-check.tsv")
MERGED = os.path.join(MODEL, "merged")
G1 = "e4d5cee3aaea9a12b3e27c1e641075a01d88052c"   # the rows as PLAN.md links them, section 6, "Q3's rows"
HEAD = ["set", "row_id", "needed_by", "result", "cap_ids", "who_answers", "when", "time_bombs", "basis", "what_would_settle_it"]
RESULTS = {"covered", "partly", "beyond the class", "candidate miss: held", "candidate miss: not held", "unclear"}
WHO = re.compile(r"^(model|founder|engineering|outside|subject:S-\d\d)$")
WHEN = {"before build", "before release", "later", "unclear"}
BOMBS = {"bundles", "wrong party", "wrong time", "market fact"}
STOP = set("what which when where whose does each with from into that this they their them than then there these those "
           "have will would should could other more most also only same such between about under over after before "
           "store stores platform platforms merchant merchants sharrwah shopify salla".split())


def cmd_rows(a):
    km = rows(os.path.join(MODEL, "seed", "km-questions.tsv"))
    pay = list(csv.DictReader(io.StringIO(subprocess.run(["git", "-C", ROOT, "show", f"{G1}:register/pay-questions.tsv"],
                                                         capture_output=True, text=True, check=True).stdout), delimiter="\t"))
    os.makedirs(os.path.dirname(ROWS), exist_ok=True)
    with open(ROWS, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(["set", "row_id", "needed_by", "question"]) + "\n")
        for r in km:
            f.write("\t".join(["km", r["km_id"], r["needed_by"], " ".join(r["question"].split())]) + "\n")
        for r in pay:
            f.write("\t".join(["pay", r["id"], r["needed_by"], " ".join(r["question"].split())]) + "\n")
    print(f"{os.path.relpath(ROWS, ROOT)}: {len(km)} Knowledge Map questions and {len(pay)} payment rows, read for id, question and needed_by only")


def model():
    caps = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    hay = {c: [r["capability"], r["note"]] for c, r in caps.items()}
    for r in rows(os.path.join(MERGED, "cells.tsv")):
        if r["cap_id"] in hay:
            hay[r["cap_id"]] += [r["terms"], r["where"]]
    return caps, kinds, {c: fold(" ".join(v)) for c, v in hay.items()}


def placements(k):
    out = []
    for p in PLATFORMS:
        v = k.get(p, "")
        out.append(f"{p[:2]}:{'nothing held' if v == 'none-held' else (v.split(':', 1)[1] or 'not stated') if ':' in v else 'not mapped'}")
    return " ".join(out)


def cmd_slice(a):
    rs = rows(ROWS)
    if a.rows:
        want = set(ids(a.rows)); rs = [r for r in rs if r["row_id"] in want or f"{r['set']}:{r['row_id']}" in want]
    elif a.area:
        rs = [r for r in rs if r["row_id"].split("-")[0] == a.area and (not a.set or r["set"] == a.set)]
        rs = rs[(a.start or 1) - 1:a.end or None]
    caps, kinds, hay = model()
    words_of = {c: set(re.findall(r"[a-z\u0600-\u06ff]{4,}", h)) for c, h in hay.items()}
    df = {}
    for ws in words_of.values():
        for w in ws:
            df[w] = df.get(w, 0) + 1
    N = len(caps) or 1
    for r in rs:
        area = r["row_id"].split("-")[0]
        words = [w for w in re.findall(r"[a-z؀-ۿ]{4,}", fold(r["question"])) if w not in STOP]
        stems = {w[:-1] if w.endswith("s") and len(w) > 4 else w for w in words}
        weight = {w: math.log(N / df[w]) for w in stems if df.get(w)}
        scored = sorted(((-round(sum(v for w, v in weight.items() if w in hay[c]), 1), c) for c in caps if caps[c]["area"] != area), key=lambda x: x)
        print(f"## {r['set']}:{r['row_id']} [needed by {r['needed_by']}] {r['question']}")
        own = [c for c in sorted(caps) if caps[c]["area"] == area]
        print(f"   in area {area}: {len(own)} capabilities")
        for c in own:
            k = kinds.get(c, {})
            print(f"   {c}\t{caps[c]['capability'][:110]}\t[{k.get('kind', '?')}, {k.get('count', '?')} of 5] {placements(k)}")
        top = [(n, c) for n, c in scored[:a.top] if n < 0]
        if top:
            print(f"   elsewhere, by the question's rarer words:")
            for n, c in top:
                k = kinds.get(c, {})
                print(f"   {c}\t{caps[c]['capability'][:110]}\t[{k.get('kind', '?')}, {k.get('count', '?')} of 5; weight {-n}]")


def cmd_check(a):
    problems = []
    rs = {f"{r['set']}:{r['row_id']}": r for r in rows(ROWS)}
    caps = {r["cap_id"] for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    subjects = {r.get("subject_id") or r.get("id") or "" for r in rows(os.path.join(ROOT, "studies", "subjects", "subjects.tsv"))}
    if not os.path.exists(OUT):
        sys.exit(f"no {os.path.relpath(OUT, ROOT)}")
    with open(OUT, encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
    if head != HEAD:
        problems.append(f"header must be: {' '.join(HEAD)}")
    out = rows(OUT)
    seen = {}
    for i, r in enumerate(out, 2):
        w = f"line {i}"
        rid = f"{r['set']}:{r['row_id']}"
        if rid not in rs:
            problems.append(f"{w}: {rid} is not a row (set and row_id)"); continue
        if rid in seen:
            problems.append(f"{w}: {rid} again (first on line {seen[rid]})")
        seen[rid] = i
        if r["needed_by"] != rs[rid]["needed_by"]:
            problems.append(f"{w}: needed_by is the row's own: {rs[rid]['needed_by']}")
        if r["result"] not in RESULTS:
            problems.append(f"{w}: result must be one of {', '.join(sorted(RESULTS))}")
        cs = ids(r["cap_ids"])
        for c in cs:
            if c not in caps:
                problems.append(f"{w}: {c} is not a capability of the model")
        if r["result"] in ("covered", "partly") and not cs:
            problems.append(f"{w}: {r['result']} names the capabilities that answer it")
        who = [x.strip() for x in r["who_answers"].split(";") if x.strip()]
        if not who or any(not WHO.match(x) for x in who):
            problems.append(f"{w}: who_answers is `;`-separated, each model, founder, engineering, outside or subject:S-NN")
        for x in who:
            if x.startswith("subject:") and subjects and x[8:] not in subjects:
                problems.append(f"{w}: {x[8:]} is not in studies/subjects/subjects.tsv")
        if r["result"] in ("covered", "partly") and "model" not in who:
            problems.append(f"{w}: a row the model covers is answered by the model, among others")
        if r["when"] not in WHEN:
            problems.append(f"{w}: when must be one of {', '.join(sorted(WHEN))}")
        bs = [x.strip() for x in r["time_bombs"].split(";") if x.strip()]
        if any(x not in BOMBS for x in bs):
            problems.append(f"{w}: time_bombs are `;`-separated, from {', '.join(sorted(BOMBS))}")
        if not r["basis"].strip():
            problems.append(f"{w}: basis names the keys, capabilities or ids the answer rests on")
        if r["result"] in ("unclear", "candidate miss: not held", "partly") and not r["what_would_settle_it"].strip():
            problems.append(f"{w}: {r['result']} says what would settle it")
        if r["result"] == "candidate miss: held" and not re.search(r"[A-Z]{2}-[SI]-\d{4}", r["basis"]):
            problems.append(f"{w}: a held candidate miss names the statements that hold it")
    want = set(rs) if not a.rows else {k for k in rs for x in ids(a.rows) if x == k or x == k.split(":", 1)[1]}
    for rid in sorted(want - set(seen)):
        problems.append(f"{rid} has no line")
    for p in problems:
        print("PROBLEM", p)
    print(f"{len(seen)} rows placed of {len(want)}; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def cmd_unasked(a):
    caps = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    asked = set()
    for r in rows(OUT):
        asked |= set(ids(r["cap_ids"]))
    parents = {}
    for c, r in caps.items():
        if r["parent"].strip():
            parents.setdefault(r["parent"].strip(), []).append(c)
    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    n = 0
    for c in sorted(caps):
        if c not in asked:
            n += 1
            print(f"{c}\t{caps[c]['area']}\t{kinds.get(c, {}).get('kind', '')}\t{caps[c]['capability'][:120]}")
    print(f"{n} of {len(caps)} capabilities no row asks about")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("rows")
    s = sub.add_parser("slice"); s.add_argument("--rows"); s.add_argument("--area"); s.add_argument("--set"); s.add_argument("--from", dest="start", type=int)
    s.add_argument("--to", dest="end", type=int); s.add_argument("--top", type=int, default=8)
    s = sub.add_parser("check"); s.add_argument("--rows")
    sub.add_parser("unasked")
    a = ap.parse_args()
    {"rows": cmd_rows, "slice": cmd_slice, "check": cmd_check, "unasked": cmd_unasked}[a.cmd](a)


if __name__ == "__main__":
    main()
