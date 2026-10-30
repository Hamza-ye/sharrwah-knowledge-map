"""Q3's check for what the class's model misses (PLAN.md, Stage 4A and section 6, "Q3's rows"; the brief
`studies/class-model/briefs/Q3-check.md`).

    python3 -I method/q3.py rows                       build studies/class-model/q3/rows.tsv from the rows at e4d5cee
    python3 -I method/q3.py slice --rows set:ID,...    each row with the capabilities that may answer it
    python3 -I method/q3.py slice --area PAY [--set km|pay] [--from N --to M]
    python3 -I method/q3.py where KEY_OR_STATEMENT_ID ...   which cells cite a statement, and where its concern lands
    python3 -I method/q3.py check --batch NAME [--rows set:ID,...]   check studies/class-model/q3/check-NAME.tsv
    python3 -I method/q3.py check                      check every batch file together, for the whole set
    python3 -I method/q3.py unasked                    the capabilities no covered row asks about (Q3's item 3)

A row is known by its set and id together (km:PAY-01 and pay:PAY-01 are different rows). The rows are read only for
their id, question and needed_by: their founder lane is not current (the founder, 29 October), and their other
columns hold citations that are not trusted. Each batch writes its own file, studies/class-model/q3/check-NAME.tsv.
The `when` rules and the time-bomb tests here are the coordinator's own, as the brief marks them.
"""
import argparse, csv, glob, io, math, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows, fold, ids, items, key

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repository, whatever CLASS_MODEL_DIR says
ROWS = os.path.join(MODEL, "q3", "rows.tsv")
BATCH_DIR = os.path.join(MODEL, "q3")
MERGED = os.path.join(MODEL, "merged")
G1 = "e4d5cee3aaea9a12b3e27c1e641075a01d88052c"   # the rows as PLAN.md links them, section 6, "Q3's rows"
HEAD = ["set", "row_id", "needed_by", "result", "rest", "cap_ids", "who_answers", "when", "time_bombs", "basis", "what_would_settle_it"]
RESULTS = {"covered", "partly", "beyond the class", "candidate miss: held", "candidate miss: not held", "unclear"}
RESTS = {"beyond the class", "candidate miss: held", "candidate miss: not held"}
WHO = re.compile(r"^(model|founder|engineering:build|engineering:detail|outside|plan|subject:S-\d\d|subject:none)$")
WHEN = {"before build", "at the area's build", "before release", "later", "unclear"}
BOMBS = {"bundles", "wrong party", "wrong time", "market fact"}
ORDER = ["before build", "at the area's build", "before release", "later"]
NEEDED = {"model": "before build", "spine": "before build", "slice": "at the area's build", "launch": "before release", "later": "later"}
# the `when` each answerer gives by itself (the coordinator's own rules; engineering's depends on the row)
FIXED = {"model": "before build", "founder": "before release", "outside": "before release", "plan": "before build",
         "engineering:build": "before build", "engineering:detail": "at the area's build"}
STOP = set("what which when where whose does each with from into that this they their them than then there these those "
           "have will would should could other more most also only same such between about under over after before "
           "store stores platform platforms merchant merchants sharrwah shopify salla".split())
CELL = re.compile(r"^CM-[A-Z0-9]{3}-\d{3}@(" + "|".join(PLATFORMS) + r")$")
SKEY = re.compile(r"^[A-Z]{2}-C-\d{3}/[a-z]+/[A-Z]{2}-S-\d{4}$")
IKEY = re.compile(r"^[A-Z]{2}-I-\d{4}$")


def semi(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def all_rows():
    return {f"{r['set']}:{r['row_id']}": r for r in rows(ROWS)}


def pick(spec, rs):
    """The rows a --rows list names. A bare id that both sets hold is refused, since it names two rows."""
    out, bad = [], []
    for x in ids(spec):
        if ":" in x:
            (out if x in rs else bad).append(x)
        else:
            both = [k for k in rs if k.split(":", 1)[1] == x]
            if len(both) == 1:
                out += both
            elif both:
                sys.exit(f"{x} is in both sets: write " + " or ".join(both))
            else:
                bad.append(x)
    if bad:
        sys.exit(f"not rows: {', '.join(bad)}")
    return out


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


def line(c, caps, kinds, extra=""):
    k = kinds.get(c, {})
    return f"   {c}\t[{caps[c].get('domain', '?')}] {caps[c]['capability'][:110]}\t[{k.get('kind', '?')}, {k.get('count', '?')} of 5{extra}] {placements(k)}"


def cmd_slice(a):
    rs = all_rows()
    if a.rows:
        chosen = [rs[k] for k in pick(a.rows, rs)]
    elif a.area:
        area = a.area.upper()
        chosen = [r for r in rs.values() if r["row_id"].split("-")[0] == area and (not a.set or r["set"] == a.set)]
        chosen = chosen[(a.start or 1) - 1:(a.end if a.end is not None else None)]
        if not chosen:
            sys.exit(f"no rows in area {area}" + (f" and set {a.set}" if a.set else ""))
    else:
        sys.exit("give --rows or --area")
    caps, kinds, hay = model()
    words_of = {c: set(re.findall(r"[a-z؀-ۿ]{4,}", h)) for c, h in hay.items()}
    df = {}
    for ws in words_of.values():
        for w in ws:
            df[w] = df.get(w, 0) + 1
    N = len(caps) or 1
    seed_dom = {x["area_id"]: x["domain"].split(" ")[0] for x in rows(os.path.join(MODEL, "seed", "km-areas.tsv"))}
    shown = set()
    for r in chosen:
        area = r["row_id"].split("-")[0]
        if area not in shown:
            shown.add(area)
            own = [c for c in sorted(caps) if caps[c]["area"] == area]
            why = "" if own else (" (domain H's areas hold none by design)" if seed_dom.get(area) == "H" else " (none merged: its domain may not be merged yet)")
            print(f"# area {area}: {len(own)} capabilities{why}")
            for c in own:
                print(line(c, caps, kinds))
        words = [w for w in re.findall(r"[a-z؀-ۿ]{4,}", fold(r["question"])) if w not in STOP]
        stems = {w[:-1] if w.endswith("s") and len(w) > 4 else w for w in words}
        weight = {w: math.log(N / df[w]) for w in stems if df.get(w)}
        scored = sorted(((-round(sum(v for w, v in weight.items() if w in hay[c]), 1), c) for c in caps if caps[c]["area"] != area))
        print(f"## {r['set']}:{r['row_id']} [needed by {r['needed_by']}] {r['question']}")
        top = [(n, c) for n, c in scored[:a.top] if n < 0]
        if top:
            print("   elsewhere, by the question's rarer words:")
            for n, c in top:
                print(line(c, caps, kinds, f"; weight {-n}"))


def sid(k):
    return k.rsplit("/", 1)[-1]


def cmd_where(a):
    ev = rows(os.path.join(MERGED, "evidence.tsv"))
    land = {r["concern_id"]: r for r in rows(os.path.join(MERGED, "landings.tsv"))}
    caps = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    by_sid = {}
    for p in PLATFORMS:
        for s in items(p):
            by_sid.setdefault(sid(key(s)), []).append(s)
    for q in a.keys:
        s_id = sid(q)
        held = by_sid.get(s_id, [])
        if not held:
            print(f"{q}: no statement or inventory entry with this id"); continue
        print(f"{s_id}: held under {', '.join(sorted({key(s) for s in held}))}")
        cited = [r for r in ev if sid(r["key"]) == s_id]
        for r in cited:
            print(f"   cited in {r['cap_id']}@{r['platform']} as {r['supports']} ({r['key']}): {caps.get(r['cap_id'], {}).get('capability', '')[:90]}")
        if not cited:
            print("   cited in no cell")
        for c in sorted({x for s in held for x in s.get("concern_ids", [s["concern_id"]])}):
            lr = land.get(c)
            print(f"   its concern {c} lands in {lr['cap_id'] if lr else 'no merged capability (its domain may not be merged)'}")


def when_of(who, rest_when=None):
    """The earliest `when` the answerers give, where each gives one by the rules. engineering, subject:none and a
    subject the rules give `before build` are handled as the brief says."""
    vals = []
    for x in who:
        if x in FIXED:
            vals.append(FIXED[x])
        elif x.startswith("subject:S-"):
            vals.append("before build")
    return min(vals, key=ORDER.index) if vals else None


def cmd_check(a):
    problems = []
    rs = all_rows()
    caps = {r["cap_id"] for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    kinds = {r["cap_id"]: r["kind"] for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    cells = {f"{r['cap_id']}@{r['platform']}" for r in rows(os.path.join(MERGED, "cells.tsv"))}
    cited = {sid(r["key"]) for r in rows(os.path.join(MERGED, "evidence.tsv"))}
    keys = {p: {key(s) for s in items(p)} for p in PLATFORMS}
    allkeys = set().union(*keys.values())
    subj_path = os.path.join(ROOT, "studies", "subjects", "subjects.tsv")
    if not os.path.exists(subj_path):
        sys.exit(f"no {subj_path}: the subject test can't run")
    subjects = {r["subject_id"] for r in rows(subj_path)}
    files = [os.path.join(BATCH_DIR, f"check-{a.batch}.tsv")] if a.batch else sorted(glob.glob(os.path.join(BATCH_DIR, "check-*.tsv")))
    if not files:
        sys.exit("no batch file: studies/class-model/q3/check-<batch>.tsv")
    want = set(pick(a.rows, rs)) if a.rows else (set(rs) if not a.batch else None)
    seen = {}
    for path in files:
        name = os.path.basename(path)
        raw = open(path, encoding="utf-8").read().split("\n")
        if raw[0].split("\t") != HEAD:
            problems.append(f"{name}: header must be: {' '.join(HEAD)}")
        for i, l in enumerate(raw[1:], 2):
            if not l.strip():
                continue
            w = f"{name} line {i}"
            f = l.split("\t")
            if len(f) != len(HEAD) or '"' in l:
                problems.append(f"{w}: {len(HEAD)} tab-separated fields, no quoting (it has {len(f)})"); continue
            r = dict(zip(HEAD, f))
            rid = f"{r['set']}:{r['row_id']}"
            if rid in seen:
                problems.append(f"{w}: {rid} again (first in {seen[rid]})")
            seen.setdefault(rid, w)
            if want is not None and rid not in want:
                continue
            if rid not in rs:
                problems.append(f"{w}: {rid} is not a row (set and row_id)"); continue
            res, rest = r["result"], r["rest"]
            if r["needed_by"] != rs[rid]["needed_by"]:
                problems.append(f"{w}: needed_by is the row's own: {rs[rid]['needed_by']}")
            if res not in RESULTS:
                problems.append(f"{w}: result must be one of {', '.join(sorted(RESULTS))}")
            if res == "partly" and rest not in RESTS:
                problems.append(f"{w}: partly says what the rest is, one of {', '.join(sorted(RESTS))}")
            if res != "partly" and rest:
                problems.append(f"{w}: rest is for partly only")
            cs = semi(r["cap_ids"])
            if "," in r["cap_ids"]:
                problems.append(f"{w}: cap_ids are `;`-separated")
            for c in cs:
                if c not in caps:
                    problems.append(f"{w}: {c} is not a capability of the model")
            who = semi(r["who_answers"])
            if not who or any(not WHO.match(x) for x in who):
                problems.append(f"{w}: who_answers is `;`-separated, each model, founder, engineering:build, engineering:detail, outside, plan, subject:S-NN or subject:none")
            for x in who:
                if x.startswith("subject:S-") and x[8:] not in subjects:
                    problems.append(f"{w}: {x[8:]} is not in studies/subjects/subjects.tsv")
            if res in ("covered", "partly"):
                if not cs:
                    problems.append(f"{w}: {res} names the capabilities that answer it")
                if "model" not in who:
                    problems.append(f"{w}: a row the model covers is answered by the model, among others")
            if res == "beyond the class" and ("model" in who or cs):
                problems.append(f"{w}: beyond the class has no model among its answerers and no cap_ids")
            if res == "candidate miss: not held" and cs:
                problems.append(f"{w}: a miss not held names no capability")
            basis = semi(r["basis"])
            if not basis:
                problems.append(f"{w}: basis names the cells, keys or ids the answer rests on")
            stmt = [b for b in basis if SKEY.match(b) or IKEY.match(b)]
            for b in basis:
                if CELL.match(b) and b not in cells:
                    problems.append(f"{w}: {b} is not a cell of the merged model")
                if (SKEY.match(b) or IKEY.match(b)) and b not in allkeys:
                    problems.append(f"{w}: {b} is not a statement key or inventory id")
            if res in ("covered", "partly") and not any(CELL.match(b) for b in basis):
                problems.append(f"{w}: {res} names its cells in basis, as <cap_id>@<platform>")
            if res == "candidate miss: held" or rest == "candidate miss: held":
                if not stmt:
                    problems.append(f"{w}: a held miss names the statements that hold it, by key")
                for b in stmt:
                    if sid(b) in cited:
                        problems.append(f"{w}: {b} is cited by a cell already (q3.py where): the row is covered or partly, not a miss")
            if r["when"] not in WHEN:
                problems.append(f"{w}: when must be one of {', '.join(sorted(WHEN))}")
            ruled = when_of(who)
            if ruled and r["when"] != "unclear" and r["when"] != ruled:
                problems.append(f"{w}: when is {ruled} by the rules for {', '.join(who)}")
            bs = semi(r["time_bombs"])
            if any(x not in BOMBS for x in bs):
                problems.append(f"{w}: time_bombs are `;`-separated, from {', '.join(sorted(BOMBS))}")
            others = when_of([x for x in who if x != "model"])
            wrong = bool(others and r["when"] != "unclear" and NEEDED.get(r["needed_by"]) != others)
            if wrong and "wrong time" not in bs:
                problems.append(f"{w}: wrong time: needed_by {r['needed_by']} against {others}, the earliest when of its answerers other than the model")
            if "wrong time" in bs and others and not wrong:
                problems.append(f"{w}: wrong time without a disagreement between needed_by and its answerers other than the model")
            ks = {kinds.get(c, "?").split(":")[0] for c in cs}
            whens = {v for v in (FIXED.get(x) or ("before build" if x.startswith("subject:S-") else None) for x in who) if v}
            if (len(ks) > 1 or len(whens) > 1) and "bundles" not in bs:
                problems.append(f"{w}: bundles: its capabilities are of different kinds, or its answerers' times differ")
            if res in ("partly", "unclear", "candidate miss: not held") and not r["what_would_settle_it"].strip():
                problems.append(f"{w}: {res} says what would settle it")
    if want is not None:
        for rid in sorted(want - set(seen)):
            problems.append(f"{rid} has no line")
    for p in problems:
        print("PROBLEM", p)
    n = len(want) if want is not None else len(seen)
    print(f"{len([x for x in seen if want is None or x in want])} of {n} rows placed; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def cmd_unasked(a):
    caps = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    asked = set()
    for path in sorted(glob.glob(os.path.join(BATCH_DIR, "check-*.tsv"))):
        for r in rows(path):
            if r["result"] in ("covered", "partly"):
                asked |= set(semi(r["cap_ids"]))
    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    n = 0
    for c in sorted(caps):
        if c not in asked:
            n += 1
            print(f"{c}\t{caps[c]['area']}\t{kinds.get(c, {}).get('kind', '')}\t{caps[c]['capability'][:120]}")
    print(f"{n} of {len(caps)} capabilities no covered or partly row names (a row that names a parent is not read as asking about its children)")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("rows")
    s = sub.add_parser("slice"); s.add_argument("--rows"); s.add_argument("--area"); s.add_argument("--set"); s.add_argument("--from", dest="start", type=int)
    s.add_argument("--to", dest="end", type=int); s.add_argument("--top", type=int, default=8)
    s = sub.add_parser("where"); s.add_argument("keys", nargs="+")
    s = sub.add_parser("check"); s.add_argument("--batch"); s.add_argument("--rows")
    sub.add_parser("unasked")
    a = ap.parse_args()
    {"rows": cmd_rows, "slice": cmd_slice, "where": cmd_where, "check": cmd_check, "unasked": cmd_unasked}[a.cmd](a)


if __name__ == "__main__":
    main()
