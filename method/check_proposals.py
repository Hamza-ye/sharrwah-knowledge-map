"""Check the proposals' files mechanically (PLAN.md section 3, the checker).

Usage:
  python3 -I method/check_proposals.py records QUESTION PLATFORM [--dir DIR] [--check] [CAPTURE_RUN ...]

`records` checks one recording run's folder, studies/proposals/records/<QUESTION>/<platform>/ (step R3):
- selection.tsv: each row's action is copy, set aside or add; a set aside or add row gives its reason; every
  candidate concern a fresh `copy_statements.py candidates` run gives is in it;
- the copies (copied.tsv, copied-gaps.tsv and, for Q5, copied-pilot.tsv, copied-pilot-gaps.tsv and
  copied-pilot-absences.tsv): each row, after its first three columns, is its source line unchanged, byte for byte;
  each copy_id names that line; each file holds every row of the concerns chosen, and no other; each row of
  copied-citations.tsv is its source's row unchanged, and every citation the copies cite is there;
- statements.tsv and citations.tsv: their columns; ids of the form Q-XX-001 and Q-XX-C001, each used once; each
  cite_id known; bears_on numbers among the question's sentences (studies/proposals/questions-for-agents.md);
  `from` held or live; each statement found verbatim in its first cited source, and each quote in its own; every
  citation used;
- not-found.tsv: its kinds; a "not in what was read" that names what was read and shows the corpus search; an
  absent that cites its list and the words that make it complete; who_can; no route to the founder for a page that
  is held and readable;
- account.md: each section is headed by a sentence's number, as `## [2]`; each point (a list item or a paragraph)
  cites at least one id, and each id it cites exists in the folder. With --check (a checking run), each point also
  starts with its label: differs, goes beyond, the same or not in what was read.

A live source is checked against the capture runs named, and in this repository's capture runs. Before the
coordinator captures it, a quote from it is "pending capture", which doesn't fail. Prints each problem, and exits 1
on any error.
"""
import csv, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources
from source_kinds import kind_of
from held_index import Held, describe, names_a_source, norm_url, urls_in
from copy_statements import COPIES, LEAD, candidates_for, copy_id
from agent_questions import sentences

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
LABELS = ("differs", "goes beyond", "the same", "not in what was read")
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


def raw_lines(path):
    """The lines of a file as written: no field stripped, only the line ending removed."""
    with open(path, encoding="utf-8", newline="") as f:
        return [l.rstrip("\n").rstrip("\r") for l in f]


def check_copies(d, q, platform, code):
    _, sel = read(os.path.join(d, "selection.tsv"))
    if not sel:
        err("selection.tsv", "", "missing or empty: run copy_statements.py candidates, then set each action")
        return set()
    keep, listed, pilot = set(), {}, False
    for n, r in sel:
        c = r.get("concern_id")
        if c in listed:
            err("selection.tsv", f"line {n}", f"{c} is listed twice, first at line {listed[c]}")
        listed.setdefault(c, n)
        if r.get("action") not in ("copy", "set aside", "add"):
            err("selection.tsv", f"line {n}", f"action '{r.get('action')}' is not copy, set aside or add")
        if r.get("action") in ("set aside", "add") and not r.get("reason"):
            err("selection.tsv", f"line {n}", f"a '{r['action']}' row needs its reason")
        if r.get("action") in ("copy", "add") and c != "S-01":
            keep.add(c)
        if c == "S-01" and r.get("action") == "copy":
            pilot = True
    for c, _ in candidates_for(q, platform):
        if c not in listed:
            err("selection.tsv", c, "a candidate concern is missing: set it aside with a reason instead of deleting it")
    copy_ids, cited = set(), {}
    for name, (letter, base, fname) in COPIES.items():
        path = os.path.join(d, name)
        from_pilot = name.startswith("copied-pilot")
        if from_pilot and not pilot:
            if os.path.exists(path):
                err(name, "", "the selection doesn't copy S-01: run the copy again")
            continue
        if not os.path.exists(path):
            err(name, "", "missing: run copy_statements.py copy after setting the selection")
            continue
        src_path = os.path.join(base, platform, fname)
        src_rel = os.path.relpath(src_path, SKM)
        src = raw_lines(src_path)
        lines = raw_lines(path)
        head = lines[0].split("\t") if lines else []
        if head != LEAD + src[0].split("\t"):
            err(name, "", f"header isn't {LEAD} and then {src_rel}'s header")
            continue
        got = set()
        for n, raw in enumerate(lines[1:], start=2):
            if not raw.strip():
                continue
            f = raw.split("\t")
            cid = f[0]
            try:
                line = int(f[2])
            except ValueError:
                err(name, cid or f"line {n}", f"source_line '{f[2]}' isn't a line number")
                continue
            if f[1] != src_rel:
                err(name, cid, f"source_file is {f[1]}, not {src_rel}")
            if cid != copy_id(q, platform, letter, line):
                err(name, cid, f"copy_id doesn't name its source line: it is {copy_id(q, platform, letter, line)}")
            if not 2 <= line <= len(src) or "\t".join(f[3:]) != src[line - 1]:
                err(name, cid, f"not unchanged from {src_rel} line {line}")
                continue
            got.add(line)
            copy_ids.add(cid)
            row = dict(zip(head, f))
            if not from_pilot and row["concern_id"] not in keep:
                err(name, cid, f"{row['concern_id']} isn't chosen in selection.tsv")
            for col in ("cite_ids", "list_cite_ids", "complete_cite_ids"):
                for c in ids(row.get(col)):
                    cited.setdefault(os.path.relpath(os.path.join(base, platform, "citations.tsv"), SKM), set()).add(c)
        want = set()
        for n, raw in enumerate(src[1:], start=2):
            if raw.strip() and (from_pilot or raw.split("\t")[0] in keep):
                want.add(n)
        if want - got:
            err(name, "", f"{len(want - got)} rows of the concerns chosen are missing, such as {src_rel} line "
                          f"{min(want - got)}: run the copy again")
    path = os.path.join(d, "copied-citations.tsv")
    if not os.path.exists(path):
        err("copied-citations.tsv", "", "missing: run copy_statements.py copy after setting the selection")
        return copy_ids
    srcs, have = {}, {}
    for n, raw in enumerate(raw_lines(path)[1:], start=2):
        if not raw.strip():
            continue
        f = raw.split("\t")
        if f[0] not in srcs:
            if not os.path.exists(os.path.join(SKM, f[0])):
                err("copied-citations.tsv", f"line {n}", f"source_file {f[0]} doesn't exist")
                continue
            srcs[f[0]] = {l.split("\t")[0]: l for l in raw_lines(os.path.join(SKM, f[0]))[1:] if l.strip()}
        have.setdefault(f[0], set()).add(f[1] if len(f) > 1 else "")
        if srcs[f[0]].get(f[1] if len(f) > 1 else "") != "\t".join(f[1:]):
            err("copied-citations.tsv", f[1] if len(f) > 1 else f"line {n}", "not unchanged from its source's row")
    for sf, cs in cited.items():
        missing = sorted(cs - have.get(sf, set()))
        if missing:
            err("copied-citations.tsv", "", f"{len(missing)} citations the copies cite are missing, such as {missing[0]}")
    return copy_ids


def check_own(d, q, code, src, held):
    pre = f"{q}-{code}"
    nsent = len(sentences(q))
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
        if not r["bears_on"] or not all(x.isdigit() and 1 <= int(x) <= nsent for x in ids(r["bears_on"])):
            err("statements.tsv", sid, f"bears_on gives the question's sentence numbers, 1 to {nsent}")
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
        if not re.fullmatch(rf"{pre}-N\d{{2,3}}", nid):
            err("not-found.tsv", nid, f"nf_id isn't of the form {pre}-N01")
        own.add(nid)
        if r["kind"] not in KINDS:
            err("not-found.tsv", nid, f"kind '{r['kind']}' is not one of {sorted(KINDS)}")
        if r["who_can"] not in WHO:
            err("not-found.tsv", nid, f"who_can '{r['who_can']}' is not one of {sorted(WHO)}")
        if not r["bears_on"] or not all(x.isdigit() and 1 <= int(x) <= nsent for x in ids(r["bears_on"])):
            err("not-found.tsv", nid, f"bears_on gives the question's sentence numbers, 1 to {nsent}")
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
                if norm_url(u).split("?")[0].endswith("/") or "/" not in norm_url(u):
                    continue                    # a bare host names a site, not the page to capture
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


def points(text):
    """(line, text) of each point of an account: each list item, with its continuation lines, and each paragraph.
    Headings and blank lines separate points."""
    out, cur = [], None
    for n, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#") or re.match(r"^\s*\*\*[^*]+\*\*:?\s*$", line):
            cur = None                  # a heading, or a line that is only a bold subheading, is no point
            continue
        if re.match(r"^\s*([-*]|\d+[.)])\s+\S", line) or cur is None:
            cur = [n, line.strip()]
            out.append(cur)
        else:
            cur[1] += " " + line.strip()
    return [tuple(p) for p in out]


def check_account(d, q, code, known, checking=False, nf_ids=()):
    path = os.path.join(d, "account.md")
    if not os.path.exists(path):
        err("account.md", "", "missing")
        return
    text = open(path, encoding="utf-8").read()
    pat = re.compile(rf"\b{q}-{code}-(?:[KPGHA]\d{{4}}|N\d{{2,3}}|\d{{3}})\b")
    any_id = re.compile(rf"\b{q}-[A-Z]{{2}}-(?:[KPGHA]\d{{4}}|N\d{{2,3}}|C\d{{3}}|\d{{3}})\b")   # any platform's
    for c in sorted(set(pat.findall(text)) - known):
        err("account.md", c, "cites an id the folder doesn't hold")
    nsent = len(sentences(q))
    seen, first_section = [], None
    for n, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^##(?!#)", line):     # a section; ### subheadings within it are free
            m = re.match(r"^## \[(\d+)\]\s*$", line)
            if not m or not 1 <= int(m.group(1)) <= nsent:
                err("account.md", f"line {n}", f"a section is headed by one sentence's number, from [1] to [{nsent}], as ## [2]")
            elif checking:
                k = int(m.group(1))
                if seen and k <= seen[-1]:
                    err("account.md", f"line {n}", f"section [{k}] comes after [{seen[-1]}]: one section per sentence, in order")
                seen.append(k)
            first_section = first_section or n
        elif checking and re.match(r"^#+\s*\[\d+\]", line):
            err("account.md", f"line {n}", "a sentence's section is headed as ## [n], at the second level")
    cited_nf = set()
    for n, p in points(text):
        if not pat.search(p):
            err("account.md", f"line {n}", "a point that cites no id of this folder")
        cited_nf.update(x for x in pat.findall(p) if re.search(r"-N\d+$", x))
        if checking:
            m = re.match(r"^([-*]|\d+[.)])?\s*\**(" + "|".join(LABELS) + r")\b", p)
            if not m:
                err("account.md", f"line {n}", f"a point starts with its label: {', '.join(LABELS)}")
            elif m.group(2) == "not in what was read" and not re.search(rf"\b{q}-{code}-(?:[GH]\d{{4}}|N\d{{2,3}})\b", p):
                err("account.md", f"line {n}", "a 'not in what was read' point cites its not-found row or copied gap")
            if first_section is None or n < first_section:
                err("account.md", f"line {n}", "a point before the first section")
    if checking:
        for nid in sorted(set(nf_ids) - cited_nf):
            err("account.md", nid, "a not-found row that no point cites")
    words = len(re.findall(r"\w+", any_id.sub("", text)))     # ids, of any platform, aren't words
    if words > (900 if checking else 1800):
        err("account.md", "", f"{words} words, past the brief's length", "warning")


def records(q, platform, captures, d=None, checking=False):
    code = CODE[platform]
    d = d or os.path.join(SKM, "studies", "proposals", "records", q, platform)
    if not os.path.isdir(d):
        sys.exit(f"no folder {os.path.relpath(d, SKM)}")
    caps = list(captures) + sorted(glob.glob(os.path.join(SKM, "evidence/product-class/runs/*")))
    src = Sources(ROOTS, caps)
    held = Held(ROOTS, caps)
    copies = check_copies(d, q, platform, code)
    own = check_own(d, q, code, src, held)
    check_account(d, q, code, copies | own, checking, {x for x in own if re.search(r"-N\d+$", x)})


def main(argv):
    if len(argv) >= 3 and argv[0] == "records":
        rest, d = argv[3:], None
        if "--dir" in rest:
            i = rest.index("--dir")
            d = rest[i + 1]
            del rest[i:i + 2]
        checking = "--check" in rest
        rest = [x for x in rest if x != "--check"]
        records(argv[1], argv[2], rest, d, checking)
    else:
        sys.exit("usage: check_proposals.py records QUESTION PLATFORM [--dir DIR] [--check] [CAPTURE_RUN ...]")
    levels = {}
    for level, f, i, x in issues:
        levels[level] = levels.get(level, 0) + 1
        print(f"{level}\t{f}\t{i}\t{x}")
    print("; ".join(f"{k}: {v}" for k, v in sorted(levels.items())) or "no issues")
    return 1 if levels.get("error") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
