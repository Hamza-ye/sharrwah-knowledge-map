"""Check the proposals' files mechanically (PLAN.md section 3, the checker).

Usage:
  python3 -I method/check_proposals.py records QUESTION PLATFORM [--dir DIR] [CAPTURE_RUN ...]

`records` checks one recording run's folder, studies/proposals/records/<QUESTION>/<platform>/ (step R3):
- selection.tsv: each row's action is copy, set aside or add, and a set aside or add row gives its reason;
- the copies: each row of copied.tsv, copied-pilot.tsv and copied-gaps.tsv is unchanged from the source line it
  names; copied.tsv holds every statement of the concerns chosen, and no other; each row of copied-citations.tsv is
  unchanged from its source's row;
- statements.tsv and citations.tsv: their columns; ids of the form Q-XX-001 and Q-XX-C001, each used once; each
  cite_id known; bears_on numbers; `from` held or live; each statement found verbatim in its first cited source,
  and each quote in its own; every citation used;
- not-found.tsv: its kinds; a "not in what was read" that names what was read and shows the corpus search; an
  absent that cites its list and the words that make it complete; who_can; no route to the founder for a page that
  is held and readable;
- account.md: each id it cites exists in the folder, and each point cites at least one.

A live source is checked against the capture runs named, and in this repository's capture runs. Before the
coordinator captures it, a quote from it is "pending capture", which doesn't fail. Prints each problem, and exits 1
on any error.
"""
import csv, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources
from source_kinds import kind_of
from held_index import Held, describe, names_a_source, urls_in

csv.field_size_limit(10**9)
HERE = os.path.dirname(os.path.abspath(__file__))
SKM = os.path.dirname(HERE)
ROOTS = {"observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
         "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa"),
         "woocommerce-11.2.1": os.environ.get("WOO_RELEASE", "/home/user/woocommerce-release/11.2.1/woocommerce"),
         "sharrwah-knowledge-map": SKM}
CODE = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
HEAD = {
    "statements.tsv": ["stmt_id", "bears_on", "identifier", "statement", "scope", "marker", "cite_ids", "from", "note"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
    "not-found.tsv": ["nf_id", "bears_on", "what_is_missing", "kind", "read", "searched", "list_cite_ids",
                      "complete_cite_ids", "who_can", "route"],
}
ACCESS = {"md", "raw", "rendered", "local"}
KINDS = {"not in what was read", "absent"}
WHO = {"agent", "founder", "either"}
issues = []


def err(f, i, x, level="error"):
    issues.append((level, f, i, x))


def read(path, head=None):
    """(header, [(line, dict)]) of a tab-separated file with no quoting, or (None, []) if it isn't there."""
    if not os.path.exists(path):
        return None, []
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows:
        return [], []
    h, out = rows[0], []
    name = os.path.basename(path)
    if head and h != head:
        err(name, "", f"header is {h}, expected {head}")
    for n, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            continue
        if len(row) != len(h):
            err(name, f"line {n}", f"{len(row)} fields, header has {len(h)}")
        out.append((n, {k: (row[i].strip() if i < len(row) else "") for i, k in enumerate(h)}))
    return h, out


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def source_line(rel, line):
    with open(os.path.join(SKM, rel), encoding="utf-8", newline="") as f:
        for n, text in enumerate(f, start=1):
            if n == line:
                return text.rstrip("\n").rstrip("\r")
    return None


def check_copies(d, q, platform, code):
    _, sel = read(os.path.join(d, "selection.tsv"))
    if not sel:
        err("selection.tsv", "", "missing or empty: run copy_statements.py candidates, then set each action")
        return set()
    keep = set()
    for n, r in sel:
        if r.get("action") not in ("copy", "set aside", "add"):
            err("selection.tsv", f"line {n}", f"action '{r.get('action')}' is not copy, set aside or add")
        if r.get("action") in ("set aside", "add") and not r.get("reason"):
            err("selection.tsv", f"line {n}", f"a '{r['action']}' row needs its reason")
        if r.get("action") in ("copy", "add") and r.get("concern_id") != "S-01":
            keep.add(r["concern_id"])
    copy_ids = set()
    for name in ("copied.tsv", "copied-pilot.tsv", "copied-gaps.tsv", "copied-citations.tsv"):
        h, rows = read(os.path.join(d, name))
        if h is None:
            if name != "copied-pilot.tsv":
                err(name, "", "missing: run copy_statements.py copy after setting the selection")
            continue
        if name == "copied-citations.tsv":
            by_file = {}
            for n, r in rows:
                by_file.setdefault(r["source_file"], {})
            for f in by_file:
                _, src = read(os.path.join(SKM, f))
                by_file[f] = {x["cite_id"]: x for _, x in src}
            for n, r in rows:
                orig = by_file[r["source_file"]].get(r["cite_id"])
                if orig is None or any((orig.get(k) or "") != (r.get(k) or "") for k in orig):
                    err(name, r["cite_id"], "not unchanged from its source's row")
            continue
        start = 3 if name != "copied-gaps.tsv" else 2
        for n, r in rows:
            line = source_line(r["source_file"], int(r["source_line"]))
            row_text = "\t".join(list(r.values())[start:])
            if line is None or line.strip() != row_text.strip():
                err(name, r.get("copy_id") or f"line {n}", f"not unchanged from {r['source_file']} line {r['source_line']}")
            if name == "copied.tsv" and r["concern_id"] not in keep:
                err(name, r["copy_id"], f"{r['concern_id']} isn't chosen in selection.tsv")
            if "copy_id" in r:
                copy_ids.add(r["copy_id"])
    _, st = read(os.path.join(SKM, "studies", "concern-map", "platforms", platform, "statements.tsv"))
    want = sum(1 for _, r in st if r["concern_id"] in keep)
    _, got = read(os.path.join(d, "copied.tsv"))
    if got and len(got) != want:
        err("copied.tsv", "", f"holds {len(got)} statements; the concerns chosen hold {want}: run the copy again")
    return copy_ids


def check_own(d, q, code, src, held):
    pre = f"{q}-{code}"
    _, cits = read(os.path.join(d, "citations.tsv"), HEAD["citations.tsv"])
    _, sts = read(os.path.join(d, "statements.tsv"), HEAD["statements.tsv"])
    _, nfs = read(os.path.join(d, "not-found.tsv"), HEAD["not-found.tsv"])
    cit, used, own = {}, set(), set()
    for n, c in cits:
        cid = c["cite_id"]
        if not re.fullmatch(rf"{pre}-C\d{{3}}", cid):
            err("citations.tsv", cid, f"cite_id isn't of the form {pre}-C001")
        if cid in cit:
            err("citations.tsv", cid, "cite_id used twice")
        cit[cid] = c
    for n, r in sts:
        sid = r["stmt_id"]
        if not re.fullmatch(rf"{pre}-\d{{3}}", sid):
            err("statements.tsv", sid, f"stmt_id isn't of the form {pre}-001")
        if sid in own:
            err("statements.tsv", sid, "stmt_id used twice")
        own.add(sid)
        if not r["bears_on"] or not all(x.isdigit() for x in ids(r["bears_on"])):
            err("statements.tsv", sid, "bears_on gives the question's sentence numbers")
        if r["from"] not in ("held", "live"):
            err("statements.tsv", sid, f"from '{r['from']}' is neither held nor live")
        cs = ids(r["cite_ids"])
        if not cs:
            err("statements.tsv", sid, "no citation")
        for c in cs:
            used.add(c)
            if c not in cit:
                err("statements.tsv", sid, f"cite_id {c} not in citations")
        if cs and cs[0] in cit and r["statement"]:
            res, why, _ = src.check_quote(r["statement"], cit[cs[0]]["source"], cit[cs[0]]["locator"])
            if not res.startswith("found"):
                live = re.match(r"^https?://", cit[cs[0]]["source"])
                err("statements.tsv", sid, f"statement not found verbatim in {cs[0]}'s source ({res}{'; ' + why if why else ''})",
                    "pending capture" if res == "unresolved" and live else "error")
        for c in cs:
            if c in cit and kind_of(cit[c]["source"], ROOTS)[0] == "unknown":
                err("statements.tsv", sid, f"{c}'s kind is unknown under method/source_kinds.py", "warning")
    for n, r in nfs:
        nid = r["nf_id"]
        if not re.fullmatch(rf"{pre}-N\d{{2}}", nid):
            err("not-found.tsv", nid, f"nf_id isn't of the form {pre}-N01")
        own.add(nid)
        if r["kind"] not in KINDS:
            err("not-found.tsv", nid, f"kind '{r['kind']}' is not one of {sorted(KINDS)}")
        if r["who_can"] not in WHO:
            err("not-found.tsv", nid, f"who_can '{r['who_can']}' is not one of {sorted(WHO)}")
        if not r["bears_on"] or not all(x.isdigit() for x in ids(r["bears_on"])):
            err("not-found.tsv", nid, "bears_on gives the question's sentence numbers")
        if not r["read"] or not names_a_source(r["read"]):
            err("not-found.tsv", nid, "read names what was read: held paths at a commit, live URLs with a date")
        if r["kind"] == "not in what was read" and "corpus_search.py" not in r["searched"]:
            err("not-found.tsv", nid, "searched shows the corpus_search.py commands run")
        if r["kind"] == "absent":
            for col, what in (("list_cite_ids", "the list"), ("complete_cite_ids", "the words that make the list complete")):
                cs = ids(r[col])
                if not cs:
                    err("not-found.tsv", nid, f"an absence cites {what} in {col}")
                for c in cs:
                    used.add(c)
                    if c not in cit:
                        err("not-found.tsv", nid, f"{col}: {c} not in citations")
        if r["who_can"] in ("founder", "either"):
            for u in urls_in(r["route"]):
                hits = [h for h in held.lookup(u) if h["readable"]]
                if hits:
                    err("not-found.tsv", nid, f"{u} is held at {describe(hits[0])}: read it instead of routing it to the founder")
    for cid, c in cit.items():
        if c["access_path"] not in ACCESS:
            err("citations.tsv", cid, f"access_path '{c['access_path']}' is not one of {sorted(ACCESS)}")
        if re.match(r"^(observed-sh|observed-sa)(?!@[0-9a-f]{7,40}:)", c["source"]):
            err("citations.tsv", cid, "a local source names its repository at a commit")
        if "..." in c["quote"] or "…" in c["quote"]:
            err("citations.tsv", cid, "a quote has no ellipses")
        if len(c["quote"]) > 300:
            err("citations.tsv", cid, "a quote is at most 300 characters")
        for col in ("locator", "source_date", "date_basis", "accessed"):
            if not c[col]:
                err("citations.tsv", cid, f"{col} is empty")
        if cid not in used:
            err("citations.tsv", cid, "not used by any statement or absence", "warning")
        res, why, _ = src.check_quote(c["quote"], c["source"], c["locator"]) if c["quote"] and c["source"] else ("unresolved", "no quote or source", "")
        if not res.startswith("found"):
            live = re.match(r"^https?://", c["source"])
            err("citations.tsv", cid, f"quote {res}{'; ' + why if why else ''}",
                "pending capture" if res == "unresolved" and live else "error")
    return own


def check_account(d, q, code, known):
    path = os.path.join(d, "account.md")
    if not os.path.exists(path):
        err("account.md", "", "missing")
        return
    text = open(path, encoding="utf-8").read()
    pat = re.compile(rf"\b{q}-{code}-(?:K\d{{4}}|P\d{{4}}|N\d{{2}}|\d{{3}})\b")
    for c in sorted(set(pat.findall(text)) - known):
        err("account.md", c, "cites an id the folder doesn't hold")
    for n, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^\s*[-*]\s+\S", line) and not pat.search(line):
            err("account.md", f"line {n}", "a point that cites no id", "warning")
    words = len(re.findall(r"\w+", text))
    if words > 1800:
        err("account.md", "", f"{words} words, past the brief's length", "warning")


def records(q, platform, captures, d=None):
    code = CODE[platform]
    d = d or os.path.join(SKM, "studies", "proposals", "records", q, platform)
    if not os.path.isdir(d):
        sys.exit(f"no folder {os.path.relpath(d, SKM)}")
    caps = list(captures) + sorted(glob.glob(os.path.join(SKM, "evidence/product-class/runs/*")))
    src = Sources(ROOTS, caps)
    held = Held(ROOTS, caps)
    copies = check_copies(d, q, platform, code)
    own = check_own(d, q, code, src, held)
    check_account(d, q, code, copies | own)


def main(argv):
    if len(argv) >= 3 and argv[0] == "records":
        rest, d = argv[3:], None
        if "--dir" in rest:
            i = rest.index("--dir")
            d = rest[i + 1]
            del rest[i:i + 2]
        records(argv[1], argv[2], rest, d)
    else:
        sys.exit("usage: check_proposals.py records QUESTION PLATFORM [--dir DIR] [CAPTURE_RUN ...]")
    levels = {}
    for level, f, i, x in issues:
        levels[level] = levels.get(level, 0) + 1
        print(f"{level}\t{f}\t{i}\t{x}")
    print("; ".join(f"{k}: {v}" for k, v in sorted(levels.items())) or "no issues")
    return 1 if levels.get("error") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
