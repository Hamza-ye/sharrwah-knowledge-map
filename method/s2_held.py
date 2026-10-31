"""The held pass's second stage (PLAN.md, Stage 4A: "each cell still holding nothing is read against the held pages";
the brief studies/class-model/briefs/S2-held.md, its design briefs/S2-held-design.md with the coordinator's decisions
of 31 October): each cell holding nothing, and each part of Q3's candidate misses, read against what the evidence
repositories hold, one row per finding. The coordinator lands the `found` rows as held entries and placements, which
the model then cites as it cites the held pass's entries.

Usage: python3 -I method/s2_held.py COMMAND [options]

For the agents (a part, such as S2-ZD-1, as studies/class-model/held/s2-parts.tsv lists it):
  cells  --part P [--from I] [--to J] [--left]
         the part's cells holding nothing, I to J (counted from 1): each capability's definition, parent and note, its
         kind and count; the cell's searched terms and reading; the other platforms' terms, Shopify's names in Arabic
         and the held pass's lines on the other platforms; the Q3 rows and the subjects' points that name the cell or
         the capability; the leads that name it. --left lists the cells the part's file has no row for yet
  leads  --part P [--held]
         what the held pass's notes (held/<platform>/notes-*.md, calibrations included) sent to the second stage, each
         with its batch, file and line: those naming one of the part's cells, those naming no capability, and a count
         of those naming only cells already held or another part's, which --held prints one line each, to grep
  misses --part P
         the part's misses: each thing, its parts (each the subject `M-nn: <part>` of its own rows), its Q3 rows with
         their questions and what each row's rest says, and the capabilities whose names or terms share its words
         (leads, not answers)
  check  --part P
         tests held/<platform>/s2/<part>.tsv and <part>.md: the form; that every cell and miss part has its rows, one
         or more `found` or exactly one other; the values; each cap_id; each source (its form, the platform's
         repository, the part's commit, `line N` with the quote's first words within three lines of N, an archive's
         offset) with the quote found in it, or an id already held; the columns each outcome takes; the reading's
         quotes; the notes' first line and names. Prints NOTE lines to read again, then PROBLEM lines; exits 1 on a
         problem

For the coordinator:
  parts  [--write]
         the cells holding nothing per platform, from merged/cells.tsv, cut into parts by domain (a platform of more
         than 60 cells in two: A to C and D to G), with the misses each part takes and the commits fixed for the run;
         --write writes held/s2-parts.tsv (part, platform, domains, cells, misses, commits, model, state), refusing to
         rewrite it once a part is checked or landed
  mark   --part P --state checked|open
         sets a part's state in held/s2-parts.tsv: `checked` only where `check` finds no problem
  misses-join [--miss M-nn]
         each miss's rows on the five platforms, part by part: the outcomes, the proposals and the places, with `held`
         per platform (yes where every part is found, part where some are, no where none is). Writes nothing
  check-misses
         tests held/s2-misses.tsv (miss, capability, as, reading): one decision per miss; `as` one of its thing,
         feature, new, not a capability; the capability a cap_id of the merged model, new:<name>, or empty only with
         not a capability; new only where some platform's found row names a place
  land   --platform P [--batch B] [--dry-run]
         lands the platform's parts at `checked` (or `landed`) into its batch S2-<XX>, the parts' rows in turn; a part
         still open waits, and lands on a later run. Each part is checked again first. It refuses a part with a
         problem, a found miss row whose miss has no decision, and a batch already applied to the model (B names a
         correction batch, S2-<XX>-R<n>, which takes only what no earlier S2 batch of the platform holds). Writes:
           held/<platform>/entries-s2.tsv   each passage quoted by a `found` row (and an `absent` or `unclear` row's,
                                            entries of no batch): <PREFIX>-E-<8 hex of sha1("second-stage", the
                                            repository and path without the commit, the locator, the folded quote)>,
                                            lengthened on a collision; structure `second-stage`
           held/batches/<B>.txt, a row of held/batches.tsv, held/<platform>/placements-<B>.tsv (H-held.md's columns:
                                            the row's capability, or the coordinator's decision for a miss) and
                                            notes-<B>.md (its first line the parts' commits)
           held/<platform>/s2-keys.tsv      a found row naming a concern-map statement, a placed inventory entry or a
                                            subject's statement: an evidence row held_amend.py applies
           held/<platform>/s2-outcomes.tsv  the other outcomes, which held_amend.py writes into the cells' readings
           held/s2-captures.tsv             every row with a capture lead, across the platforms
         and sets the parts it landed to `landed`. A second run writes the same files. Then:
         held_entries.py check --platform P --batch B, and held_amend.py plan / apply --platform P --batch B

A row's columns (held/<platform>/s2/<part>.tsv, tab-separated, a header, no quoting, no double quote): subject, outcome,
cap_id, as, source, locator, quote, identifier, place, supports, scope, terms, filler, quality, read, searched, capture,
could_change, reading. The model's folder is studies/class-model, or CLASS_MODEL_DIR (for tests); the evidence
repositories' roots are q3_misses.py's ROOTS. Run with python3 -I from the repository's root.
"""
import argparse, collections, glob, hashlib, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, PREFIX, rows, citable, key as skey, fold as cfold
import quote_check
from q3_misses import MISSES, PARTS as MISS_PARTS, ROOTS, KINDS, REST_LABEL
import held_entries as he

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HELD = os.path.join(MODEL, "held")
MERGED = os.path.join(MODEL, "merged")
PARTS_TSV = os.path.join(HELD, "s2-parts.tsv")
PARTS_HEAD = ["part", "platform", "domains", "cells", "misses", "commits", "model", "state"]
HEAD = ["subject", "outcome", "cap_id", "as", "source", "locator", "quote", "identifier", "place", "supports", "scope",
        "terms", "filler", "quality", "read", "searched", "capture", "could_change", "reading"]
MISSES_HEAD = ["miss", "capability", "as", "reading"]
KEYS_HEAD = ["batch", "cap_id", "platform", "supports", "key", "why", "terms", "filler", "quality"]
OUT_HEAD = ["batch", "subject", "outcome", "part", "line", "commits", "entry_id", "source", "locator", "quote", "read",
            "searched", "capture", "could_change", "reading"]
CAPTURES_HEAD = ["platform", "part", "line", "subject", "outcome", "could_change", "capture", "reading"]
OUTCOMES = ("found", "not-found", "not-held", "absent", "unreadable", "unclear")
CITING = ("found", "absent", "unclear")          # the outcomes that cite a passage
AS = ("its thing", "feature", "new", "not a capability")
COULD = ("kind", "count", "decision", "no")
SEMI_FIELDS = ("supports", "scope", "terms", "filler", "quality", "read", "searched")
EVIDENCE = ("observed-sh", "observed-sa", "other-product-class", "sharrwah-knowledge-map")
RELEASE = "woocommerce-11.2.1"
OWN = {"shopify": ("observed-sh", "sharrwah-knowledge-map"), "salla": ("observed-sa", "sharrwah-knowledge-map"),
       "zid": ("other-product-class", "sharrwah-knowledge-map"),
       "bigcommerce": ("other-product-class", "sharrwah-knowledge-map"),
       "woocommerce": ("other-product-class", "sharrwah-knowledge-map", RELEASE)}
SPLIT_AT = 60                                    # a platform of more cells is cut in two by domain (design, section 4)
HALVES = (("1", "ABC"), ("2", "DEFG"))
MISS_HALF = {"1": ["M-01", "M-02", "M-05", "M-06", "M-07", "M-10", "M-11", "M-12", "M-13"],
             "2": ["M-03", "M-04", "M-08", "M-09"]}
SECOND = re.compile(r"second[ -]stage", re.I)
CAP = re.compile(r"\bCM-[A-Z]{3}-\d{3}\b")
ENTRY_ID = re.compile(r"^[A-Z]{2}-E-[0-9a-f]{8,40}$")
FILE_SOURCE = re.compile(r"^(?:(observed-sh|observed-sa|other-product-class|sharrwah-knowledge-map)@([0-9a-f]{7,40})|(woocommerce-11\.2\.1)):(\S.*)$")
NAMED = re.compile(r"(?:(?:observed-sh|observed-sa|other-product-class|sharrwah-knowledge-map)@[0-9a-f]{7,40}|woocommerce-11\.2\.1):[^\s;,()'’]+")


def semi(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


def clip(s, n):
    s = " ".join(str(s).split())
    return s if n <= 0 or len(s) <= n else s[: n - 1] + "…"


def rel(path):
    return os.path.relpath(path, MODEL)


def read_tsv(path, head, problems, name=None):
    """A file of the second stage, as (line number, row): its header, field count and double quotes tested."""
    name = name or rel(path)
    if not os.path.exists(path):
        problems.append(f"no file {name}")
        return []
    raw = open(path, encoding="utf-8-sig").read().replace("\r\n", "\n").split("\n")
    if raw[0].split("\t") != head:
        problems.append(f"{name}: the header is: {' '.join(head)}")
        return []
    out = []
    for i, l in enumerate(raw[1:], 2):
        if not l.strip():
            continue
        if '"' in l:
            problems.append(f"{name} line {i}: holds a double quote (\"), which these files can't carry: quote with ' or “ ”")
            continue
        f = l.split("\t")
        if len(f) != len(head):
            problems.append(f"{name} line {i}: {len(head)} tab-separated fields, no quoting (it has {len(f)})")
            continue
        out.append((i, dict(zip(head, f))))
    return out


def write_tsv(path, head, rs):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(head) + "\n")
        for r in rs:
            f.write("\t".join(" ".join(str(r.get(h, "")).split("\t")).replace("\n", " ") for h in head) + "\n")


def parts_rows():
    return rows(PARTS_TSV)


def part_row(part):
    for r in parts_rows():
        if r["part"] == part:
            return r
    sys.exit(f"no part {part} in {rel(PARTS_TSV)}: its parts are {', '.join(r['part'] for r in parts_rows()) or 'none yet (parts --write)'}")


def rows_file(pr):
    return os.path.join(HELD, pr["platform"], "s2", f"{pr['part']}.tsv")


def caps_table():
    return {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}


def merged_cells():
    return {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(MERGED, "cells.tsv"))}


def git(root, *a):
    p = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else ""


def head_commits(n=40):
    """Each evidence repository's HEAD, and this repository's, n hex digits long."""
    return {r: git(ROOTS[r], "rev-parse", *([f"--short={n}"] if n < 40 else []), "HEAD") for r in EVIDENCE}


def parse_commits(s):
    """`repo@commit;...;woocommerce-11.2.1` as {repo: {commit}}; the release has no commit."""
    out = {}
    for x in semi(s):
        repo, _, c = x.partition("@")
        out.setdefault(repo, set()).add(c)
    return out


def notes_commits(line):
    """The commits a line names, as {repo: {commit}} (a notes file's first line)."""
    out = {}
    for m in re.finditer(r"\b(observed-sh|observed-sa|other-product-class|sharrwah-knowledge-map)@([0-9a-f]{7,40})\b", line):
        out.setdefault(m.group(1), set()).add(m.group(2))
    if RELEASE in line:
        out.setdefault(RELEASE, set()).add("")
    return out


def same(a, b):
    return len(a) >= 7 and len(b) >= 7 and (a.startswith(b) or b.startswith(a))


_S = []


def sources():
    """The quote checker over the evidence repositories, this repository's capture runs loaded (inspection-Q3M.md, Q3M-1)."""
    if not _S:
        _S.append(quote_check.Sources(ROOTS, sorted(d for d in glob.glob(os.path.join(ROOT, "evidence", "product-class", "runs", "*")) if os.path.isdir(d))))
    return _S[0]


def belongs(p, repo, path):
    """Is a held file the platform's: its repository, its folder of other-product-class, the release, or this
    repository's captures of the platform's hosts and the founder's saves for it (corpus_search.py's HOSTS)."""
    if repo == "sharrwah-knowledge-map":
        from corpus_search import HOSTS
        m = re.match(r"^evidence/product-class/runs/[^/]+/items/\d+-([^/]+)/", path)
        if m:
            return re.search(HOSTS[p], m.group(1)) is not None
        return path.startswith(f"evidence/product-class/blocked-evidence-founder/{p}/")
    if repo == RELEASE:
        return p == "woocommerce"
    if repo == "other-product-class":
        return p in ("zid", "bigcommerce", "woocommerce") and path.startswith(p + "/")
    return {"observed-sh": "shopify", "observed-sa": "salla"}.get(repo) == p


_lines = {}


def file_lines(S, source):
    if source not in _lines:
        texts, why = S.local_texts(source)
        _lines[source] = texts[0].split("\n") if texts else None
    return _lines[source]


def unescape(s):
    s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)
    return s.replace('\\"', '"').replace("\\/", "/").replace("\\n", " ").replace("\\t", " ")


def loose(s):
    return quote_check.variants(s)[2][1]          # markup removed, case and Arabic diacritics ignored


def near_problem(S, source, n, quote):
    """The quote's first words within three lines of line n (the brief: "the line where the quote begins")."""
    ls = file_lines(S, source)
    if ls is None:
        return None                               # the source's own problem is reported by the quote test
    if not 1 <= n <= len(ls):
        return f"line {n}: the file has {len(ls)} lines"
    win = "\n".join(ls[max(0, n - 4):n + 3])
    first = " ".join(loose(quote).split()[:5])
    hays = (win, unescape(win), quote_check.html_text(win), quote_check.html_text(unescape(win)))
    if any(first in loose(h) for h in hays):
        return None
    return f"line {n}: the quote's first words ('{clip(first, 60)}') are not within three lines of it: the locator is the line where the quote begins"


def source_problems(p, source, locator, quote, commits, S):
    """What is wrong with a held passage's citation: its form, the platform's repository, the commit, the locator, and
    whether the quote is found in it. commits: {repository: {commit}} allowed. Used by held_entries.py check too."""
    source, locator = source.strip(), locator.strip()
    if re.search(r"@\d+(?:#piece-\d+)?$", source):
        return ["the offset goes in `locator`: the source is the archive's file, `<repository>@<commit>:<path>`, as corpus_search.py prints it before its `@<offset>`"]
    m = FILE_SOURCE.match(source)
    if not m:
        return ["source is `<repository>@<commit>:<path>` (a held file, a fetch archive, this repository's capture or a "
                "founder's save), `woocommerce-11.2.1:<path>`, or the id of a held entry or a concern-map statement"]
    repo = m.group(1) or m.group(3)
    commit, path = m.group(2) or "", m.group(4).strip()
    out = []
    if not belongs(p, repo, path):
        out.append(f"{repo}:{path} is not {p}'s: cite {p}'s repository ({', '.join(OWN[p])}), at its own folder, host or saves")
    if repo != RELEASE:
        want = commits.get(repo, set())
        if not any(same(commit, c) for c in want):
            out.append(f"{repo}@{commit} is not a commit allowed here: the run fixed {', '.join(sorted(repo + '@' + c for c in want)) or 'none named'})")
    if path.endswith(".warc.gz"):
        if not re.fullmatch(r"\d+", locator):
            out.append("an archive's locator is its record's offset, digits only")
    else:
        lm = re.fullmatch(r"line (\d+)", locator)
        if not lm:
            out.append("a file's locator is `line N`, the line where the quote begins")
    res, why, share = S.check_quote(quote, source, locator)
    if res == "unresolved":
        out.append(f"the source doesn't resolve: {why}")
    elif not res.startswith("found"):
        out.append(f"the quote is not found in its source{f' ({share} of its six-word runs are)' if share else ''}: copy it exactly, from the document, never a snippet")
    elif not path.endswith(".warc.gz") and re.fullmatch(r"line (\d+)", locator):
        x = near_problem(S, source, int(locator.split()[1]), quote)
        if x:
            out.append(x)
    return out


def id_text(p, src, held, cit):
    """The text of an id already held: a held entry's, or a concern-map statement's (with its identifier)."""
    if src in held:
        return held[src]["text"]
    x = cit.get(src)
    return ((x.get("identifier") or "") + " " + (x.get("statement") or "")) if x else None


def plat_of(token):
    for p, x in PREFIX.items():
        if re.match(rf"^{x}-[A-Z]-", token):
            return p
    m = re.match(r"^S\d\d-([A-Z]{2})-\d+$", token)
    return next((p for p, x in PREFIX.items() if m and x == m.group(1)), None)


# ---------------------------------------------------------------- the leads

def natural(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


BULLET = re.compile(r"^(?:[-*+]|\d+[.)])\s+")
HEADING = re.compile(r"^(#{1,6})\s+(.*)")


def blocks(lines):
    """A note's blocks, as (kind, first, end, level, title): headings, top-level bullets with their nested lines, and
    paragraphs."""
    out, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i]
        if not l.strip():
            i += 1
            continue
        h = HEADING.match(l)
        if h:
            out.append(("h", i, i + 1, len(h.group(1)), h.group(2)))
            i += 1
            continue
        j = i + 1
        if BULLET.match(l):
            while j < n:
                if not lines[j].strip():
                    k = j
                    while k < n and not lines[k].strip():
                        k += 1
                    if k < n and lines[k][:1] in (" ", "\t"):
                        j = k
                        continue
                    break
                if lines[j][:1] in (" ", "\t"):
                    j += 1
                    continue
                if BULLET.match(lines[j]) or HEADING.match(lines[j]):
                    break
                j += 1
            out.append(("b", i, j, 0, ""))
        else:
            while j < n and lines[j].strip() and not BULLET.match(lines[j]) and not HEADING.match(lines[j]):
                j += 1
            out.append(("p", i, j, 0, ""))
        i = j
    return out


_leads = {}


def leads_of(p):
    """The held pass's leads for the second stage on a platform: in a section whose heading names the second stage,
    each top-level bullet with its nested lines and each paragraph, up to the next heading of its level; outside one,
    a bullet or paragraph that names it."""
    if p not in _leads:
        out = []
        paths = glob.glob(os.path.join(HELD, p, "notes-*.md"))
        for path in sorted(paths, key=lambda x: natural(os.path.basename(x))):
            batch = os.path.basename(path)[6:-3]
            if batch.startswith("S2-"):
                continue                          # the landing's own notes
            lines = open(path, encoding="utf-8").read().split("\n")
            sec = None
            for kind, s, e, lev, title in blocks(lines):
                if kind == "h":
                    if sec is not None and lev <= sec:
                        sec = None
                    if sec is None and SECOND.search(title):
                        sec = lev
                    continue
                text = "\n".join(lines[s:e]).rstrip()
                if sec is not None or SECOND.search(text):
                    out.append({"batch": batch, "file": rel(path), "line": s + 1, "text": text,
                                "caps": list(dict.fromkeys(CAP.findall(text)))})
        _leads[p] = out
    return _leads[p]


def grouped(pr):
    """The part's leads in the brief's three groups: naming one of its cells; naming no capability; the rest."""
    mine, caps = set(semi(pr["cells"])), caps_table()
    g = ([], [], [])
    for L in leads_of(pr["platform"]):
        cs = [c for c in L["caps"] if c in caps]
        g[0 if any(c in mine for c in cs) else 1 if not cs else 2].append(L)
    return g


def show_lead(L):
    print(f"-- {L['batch']} {L['file']} line {L['line']}{' [' + ', '.join(L['caps']) + ']' if L['caps'] else ''}")
    print(L["text"])


def cmd_leads(a):
    pr = part_row(a.part)
    g1, g2, g3 = grouped(pr)
    print(f"{a.part} ({pr['platform']}): {len(g1)} leads name one of its cells, {len(g2)} name no capability, "
          f"{len(g3)} name only cells already held or another part's. A lead is only a lead: read what it says a file "
          f"states in the file.")
    print(f"\n== {len(g1)} naming one of {a.part}'s cells")
    for L in g1:
        show_lead(L)
    print(f"\n== {len(g2)} naming no capability: a thing your cells may hold, or a new thing")
    for L in g2:
        show_lead(L)
    if a.held:
        print(f"\n== {len(g3)} naming only cells already held or another part's (batch:line, cap_ids, first 100 characters)")
        for L in g3:
            print(f"{L['batch']}:{L['line']} {','.join(L['caps'])} {clip(L['text'], 100)}")
    else:
        print(f"\n== {len(g3)} naming only cells already held or another part's: they take no row here; "
              f"`leads --part {a.part} --held` prints them one line each, to grep with a chunk's terms")


# ---------------------------------------------------------------- cells and misses

def part_file_rows(pr):
    path = rows_file(pr)
    return read_tsv(path, HEAD, []) if os.path.exists(path) else []


def cmd_cells(a):
    pr = part_row(a.part)
    p = pr["platform"]
    ids = semi(pr["cells"])
    caps = caps_table()
    if a.left:
        done = {r["subject"] for _, r in part_file_rows(pr)}
        left = [(n, c) for n, c in enumerate(ids, 1) if c not in done]
        print(f"{len(left)} of {len(ids)} cells of {a.part} have no row in {rel(rows_file(pr))}")
        for n, c in left:
            print(f"   {n} {c} [{caps.get(c, {}).get('domain', '?')} {caps.get(c, {}).get('area', '?')}] {clip(caps.get(c, {}).get('capability', ''), 120)}")
        return
    lo, hi = max(1, a.from_ or 1), min(len(ids), a.to or len(ids))
    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    cells = merged_cells()
    names = collections.defaultdict(list)
    for r in rows(os.path.join(MODEL, "names-ar.tsv")):
        names[r["cap_id"]].append(r)
    ev = collections.defaultdict(list)
    for r in rows(os.path.join(MERGED, "evidence.tsv")):
        if r["platform"] != p and re.match(r"^[A-Z]{2}-E-", r["key"]):
            ev[r["cap_id"]].append(r)
    q3rows = {f"{r['set']}:{r['row_id']}": r for r in rows(os.path.join(MODEL, "q3", "rows.tsv"))}
    q3 = []
    for path in sorted(glob.glob(os.path.join(MODEL, "q3", "check-*.tsv"))):
        q3 += [(os.path.basename(path), r) for r in rows(path)]
    points = []
    for path in sorted(glob.glob(os.path.join(MODEL, "points", "P-*.tsv")), key=natural):
        points += rows(path)
    g1 = grouped(pr)[0]
    for n in range(lo, hi + 1):
        c = ids[n - 1]
        r = caps.get(c, {})
        print(f"[{n}/{len(ids)}] {c} (domain {r.get('domain', '?')}, area {r.get('area', '?')}): {r.get('capability', '')}")
        par = r.get("parent") or ""
        print(f"   parent: {par + ' ' + clip(caps.get(par, {}).get('capability', ''), 100) if par else 'none'}")
        print(f"   note: {r.get('note') or '-'}")
        k = kinds.get(c, {})
        print(f"   kind: {k.get('kind', '?')}, count {k.get('count', '?')}{', ' + k['class_scope'] if k.get('class_scope') else ''}; "
              + "; ".join(f"{q} {k.get(q, '')}" for q in PLATFORMS))
        cell = cells.get((c, p), {})
        print(f"   {p}: {cell.get('held', 'no cell')}; searched: {cell.get('searched') or '-'}")
        print(f"   {p} reading: {cell.get('reading') or '-'}")
        print("   other platforms' terms: " + " | ".join(f"{q}: {cells.get((c, q), {}).get('terms') or '-'}" for q in PLATFORMS if q != p))
        if names.get(c):
            print("   Shopify's names in Arabic: " + "; ".join(f"{x['name_en']} = {x['name_ar']}{' (also ' + x['others'] + ')' if x.get('others') else ''}" for x in names[c]))
        if ev.get(c):
            by = collections.defaultdict(list)
            for x in ev[c]:
                by[x["platform"]].append(x)
            for q, xs in by.items():
                print(f"   the held pass on {q}, {len(xs)} rows: " + "; ".join(f"{x['supports']} {x['key']}: {clip(x['why'], 150)}" for x in xs[:3]) + (" …" if len(xs) > 3 else ""))
        for f, x in q3:
            toks = semi(x.get("basis", "")) + semi(x.get("cap_ids", ""))
            if c in toks or any(t.startswith(c + "@") for t in toks):
                mark = " (names this cell)" if f"{c}@{p}" in toks else ""
                qq = q3rows.get(f"{x['set']}:{x['row_id']}", {}).get("question", "")
                print(f"   Q3 {x['set']}:{x['row_id']} ({f}, {x['result']}{' / ' + x['rest'] if x.get('rest') else ''}){mark}: {clip(qq, 180)}")
        for x in points:
            if c in semi(x.get("cap_ids", "")):
                print(f"   point {x['vp_id']} ({x.get('subject', '')}, {x.get('status', '')}): {clip(x.get('question', ''), 180)}")
        for L in g1:
            if c in L["caps"]:
                print(f"   lead: {L['batch']} {L['file']} line {L['line']}")
                print("      " + L["text"].replace("\n", "\n      "))
        print()


def cmd_misses(a):
    pr = part_row(a.part)
    p = pr["platform"]
    q3rows = {f"{r['set']}:{r['row_id']}": r for r in rows(os.path.join(MODEL, "q3", "rows.tsv"))}
    rests = {}
    for path in sorted(glob.glob(os.path.join(MODEL, "q3", "check-*.tsv"))):
        for r in rows(path):
            rests[f"{r['set']}:{r['row_id']}"] = (os.path.basename(path), r)
    idx = he.candidate_index(p)
    names, state = idx[2], idx[4]
    for m in semi(pr["misses"]):
        rids, thing = MISSES[m]
        print(f"{m}: {thing}")
        print(f"   its parts, each the subject of its own rows:")
        for x in MISS_PARTS[m]:
            print(f"      {m}: {x}")
        for rid in rids:
            f, r = rests.get(rid, ("?", {}))
            print(f"   {rid} ({f}, {r.get('result', '?')}{' / ' + r['rest'] if r.get('rest') else ''}): {q3rows.get(rid, {}).get('question', '')}")
            print(f"      {REST_LABEL}:")
            print(f"      its rest: {r.get('what_would_settle_it', '')}")
            print(f"      its basis: {r.get('basis', '')}")
        leads = collections.OrderedDict()
        for t in [thing] + MISS_PARTS[m]:
            for c, why in he.candidates({"text": t.replace(":", ",")}, idx):
                leads.setdefault(c, set()).update(why)
        print(f"   capabilities sharing its words (leads, not answers): " + ("; ".join(
            f"{c} {clip(names.get(c, ''), 60)} [{p}: {state.get(c, '?')}] ({', '.join(sorted(w)[:3])})" for c, w in leads.items()) or "none"))
        print()


# ---------------------------------------------------------------- the check

def check_part(pr):
    """Tests a part's rows and notes: (rows, problems, notes)."""
    p, part = pr["platform"], pr["part"]
    problems, notes = [], []
    path = rows_file(pr)
    name = f"{part}.tsv"
    rs = read_tsv(path, HEAD, problems, name)
    cells = semi(pr["cells"])
    msubj = {f"{m}: {x}": m for m in semi(pr["misses"]) for x in MISS_PARTS[m]}
    caps = caps_table()
    cap_names = {he.fold(r["capability"].split(":")[0].split("(")[0]) for r in caps.values()} | {he.fold(c) for c in caps}
    new_tsv = os.path.join(HELD, "new.tsv")
    decided = {(r["platform"], he.fold(r["name"])) for r in rows(new_tsv) if r.get("decision")}
    commits = parse_commits(pr["commits"])
    S = sources()
    cit = {skey(x): x for x in citable(p)}
    held = {e["entry_id"]: e for e in he.entries(p)}
    by_subj = collections.defaultdict(list)
    new_names = collections.defaultdict(list)
    proposals = collections.defaultdict(set)
    placed = collections.defaultdict(list)
    for i, r in rs:
        w = f"{name} line {i}"
        for fld in SEMI_FIELDS:
            if r[fld] and any(not x.strip() for x in r[fld].split(";")):
                problems.append(f"{w}: {fld} has an empty `;` piece")
        subj, oc = r["subject"].strip(), r["outcome"].strip()
        kind = "cell" if subj in cells else "miss" if subj in msubj else "new" if subj == "new" else None
        if not kind:
            problems.append(f"{w}: subject is a cap_id of {part}'s cells, `M-nn: <part>` as `misses --part {part}` prints it, or new")
            continue
        by_subj[subj].append((i, oc))
        if oc not in OUTCOMES:
            problems.append(f"{w}: outcome is one of {', '.join(OUTCOMES)}")
            continue
        cap, as_ = r["cap_id"].strip(), r["as"].strip()
        # cap_id and as
        if kind == "cell":
            if as_:
                problems.append(f"{w}: as is for a miss's rows only")
            if oc == "found" and cap != subj:
                problems.append(f"{w}: a cell's found row names its own cap_id, {subj}")
            if oc != "found" and cap:
                problems.append(f"{w}: cap_id is empty on a cell's {oc} row")
        elif kind == "new":
            if oc != "found":
                problems.append(f"{w}: a new thing is a found row (subject new, outcome found)")
            if as_:
                problems.append(f"{w}: as is for a miss's rows only")
            if not re.match(r"^new:\S", cap):
                problems.append(f"{w}: a new row's cap_id is new:<its name, in the platform's words>")
        else:
            m = msubj[subj]
            if as_ not in AS:
                problems.append(f"{w}: a miss's row carries as: one of {', '.join(AS)}")
            elif as_ in ("its thing", "feature") and cap not in caps:
                problems.append(f"{w}: as {as_} names a cap_id of the merged model in cap_id")
            elif as_ == "new" and not re.match(r"^new:\S", cap):
                problems.append(f"{w}: as new names new:<name> in cap_id")
            elif as_ == "not a capability" and cap:
                problems.append(f"{w}: as not a capability leaves cap_id empty, and reading says why")
            proposals[m].add((cap, as_))
        if cap.startswith("new:"):
            nm = cap[4:].strip()
            if (he.fold(nm) in cap_names or re.match(r"^CM-[A-Z]{3}-\d{3}$", nm)) and (p, he.fold(nm)) not in decided:
                problems.append(f"{w}: new:{nm} is an existing capability's name or id: name that capability")
            new_names[he.fold(nm)].append(nm)
        # the columns each outcome takes
        if oc == "found":
            ss = semi(r["supports"])
            if not ss or any(x not in he.SUPPORTS for x in ss) or len(ss) > 2 or len(set(ss)) != len(ss):
                problems.append(f"{w}: supports is one value of {', '.join(he.SUPPORTS)}, or two different ones, `;`-separated")
            elif ss == ["shows"]:
                notes.append(f"{w}: {subj}: found, and its only support is shows")
        else:
            for fld in ("supports", "scope", "terms", "filler", "quality"):
                if r[fld].strip():
                    problems.append(f"{w}: {fld} is for a found row only")
        wants_place = kind == "new" or (kind == "miss" and oc == "found")
        if wants_place:
            pl = r["place"].strip()
            if pl != "none" and not re.match(rf"^({'|'.join(KINDS)}): \S", pl):
                problems.append(f"{w}: place is none, or `<kind>: <the words or identifier the platform's own list names it by>`, the kind one of {', '.join(KINDS)}")
            if kind == "miss":
                placed[msubj[subj]].append(pl)
        elif r["place"].strip():
            problems.append(f"{w}: place is for a new row and a miss's found rows only")
        text = None
        if oc in CITING:
            src, loc, quote = r["source"].strip(), r["locator"].strip(), r["quote"]
            if not r["identifier"].strip():
                problems.append(f"{w}: {oc} names its identifier: the page's title, the API's name, or the item's own id")
            if not src:
                problems.append(f"{w}: {oc} cites its source, locator and quote, or an id already held")
            elif FILE_SOURCE.match(src) or re.search(r"@\d+(?:#piece-\d+)?$", src):
                if not loc or not quote.strip():
                    problems.append(f"{w}: a held file is cited with its locator and its quote")
                else:
                    problems += [f"{w}: {x}" for x in source_problems(p, src, loc, quote, commits, S)]
                    text = quote
                    if len(quote.strip()) < 30 or he.fold(quote) == he.fold(r["identifier"]):
                        notes.append(f"{w}: the quote is {'its identifier, a title only' if he.fold(quote) == he.fold(r['identifier']) else 'under 30 characters'}: the shortest whole part that states the thing?")
            else:
                text = id_text(p, src, held, cit)
                if text is None:
                    problems.append(f"{w}: source {src!r} is neither `<repository>@<commit>:<path>`, `woocommerce-11.2.1:<path>`, nor an id held on {p} (a held entry, a concern-map statement's key, a placed inventory id)")
                elif plat_of(src) not in (p, None):
                    problems.append(f"{w}: {src} is {plat_of(src)}'s, not {p}'s")
                if loc or quote.strip():
                    problems.append(f"{w}: for an id already held, locator and quote are empty")
        else:
            for fld in ("source", "locator", "quote"):
                if r[fld].strip():
                    problems.append(f"{w}: {fld} is for found, absent and unclear rows only")
        if text is not None:
            ft = (cfold(text), he.fold(text))
            for t in semi(r["terms"]):
                if cfold(t) not in ft[0] or he.fold(t) not in ft[1]:
                    problems.append(f"{w}: term {t!r} is not in the quote: each term is the platform's own word, found in it")
            for fl in semi(r["filler"]):
                named = re.sub(r"^(?:the )?law of ", "", re.sub(r"\s*\([^)]*\)", "", fl), flags=re.I).strip()
                if not any(he.fold(n) in ft[1] for n in (named, fl)):
                    problems.append(f"{w}: filler {fl!r} is not named in the quote: a party known only from elsewhere goes in reading")
                if any(he.fold(g) in he.fold(fl) for g in he.GROUP.get(p, ())):
                    problems.append(f"{w}: filler {fl!r} is a company of the platform's group (CM-ACC-002): never a filler")
        for q in semi(r["quality"]):
            what, _, val = q.partition(":")
            pieces = [he.fold(re.sub(r"\s*\([^)]*\)", "", x)).strip(" .") for x in (val or what).split(",")]
            if pieces and all(x in he.MARKS for x in pieces if x) and any(pieces):
                problems.append(f"{w}: quality {q!r} is a mark of inclusion: never a quality (H-held.md, rule 5)")
        # the other outcomes
        if oc != "found":
            for fld in ("read", "searched"):
                if r[fld].strip() in ("", "-"):
                    problems.append(f"{w}: {fld} lists what was {'read' if fld == 'read' else 'searched'}, `;`-separated")
            for x in semi(r["searched"]):
                if ":" not in x:
                    problems.append(f"{w}: each search is `<tool> <language>: <terms>` (or `held_index: <address>`): {clip(x, 60)!r}")
            if oc == "not-found" and p in ("salla", "zid") and not any(re.search(r"\bar:", x) for x in semi(r["searched"])):
                notes.append(f"{w}: {subj}: not-found on {p} with no Arabic search")
        cap_s, cc = r["capture"].strip(), r["could_change"].strip()
        if oc == "not-held":
            pcs = [x.strip() for x in cap_s.split(";")]
            if cap_s == "none" or (cap_s.startswith("none") and not re.match(r"^none: \S", cap_s)):
                problems.append(f"{w}: capture is `none: <why>` only where no run can capture it at all, never none alone")
            elif not cap_s.startswith("none: ") and not (len(pcs) == 5 and pcs[0] in EVIDENCE[:3] and all(pcs[:3])
                                                          and pcs[3].startswith("stop at ") and pcs[4].startswith("needs:")):
                problems.append(f"{w}: capture is `<repository>; <instrument>; <the run>; stop at <...>; needs: <...>` "
                                f"(the repository one of {', '.join(EVIDENCE[:3])}), or `none: <why>`")
        elif oc in ("unreadable", "unclear"):
            if not cap_s or cap_s == "none":
                problems.append(f"{w}: capture says {'the file and where it is held' if oc == 'unreadable' else 'what would settle it'}")
        elif cap_s:
            problems.append(f"{w}: capture is for not-held, unreadable and unclear rows only")
        if oc in ("not-held", "unreadable", "unclear"):
            if cc not in COULD:
                problems.append(f"{w}: could_change is one of {', '.join(COULD)}")
            elif cc in ("kind", "decision"):
                notes.append(f"{w}: {subj}: could_change {cc}: {clip(cap_s, 120)}")
        elif cc:
            problems.append(f"{w}: could_change is for not-held, unreadable and unclear rows only")
        if oc == "absent":
            notes.append(f"{w}: {subj}: absent: does reading say, in the platform's own words, what makes the list complete?")
        # the reading
        if not r["reading"].strip():
            problems.append(f"{w}: reading says why, as a reading")
        else:
            problems += [f"{w}: {x}" for x in reading_problems(p, r, text, S)]
    # coverage
    for c in cells:
        if c not in by_subj:
            problems.append(f"{c} has no row")
    for sj in msubj:
        if sj not in by_subj:
            problems.append(f"{sj} has no row")
    for sj, xs in by_subj.items():
        if sj == "new":
            continue
        ocs = [o for _, o in xs]
        if not (all(o == "found" for o in ocs) or len(ocs) == 1):
            problems.append(f"{sj}: its rows are one or more found, or exactly one of another outcome (lines {', '.join(str(i) for i, _ in xs)})")
    for m, ps in proposals.items():
        if len(ps) > 1:
            problems.append(f"{m}: its rows propose one capability, one way: {sorted(ps)}")
        if any(a_ == "new" for _, a_ in ps) and not any(x != "none" for x in placed.get(m, [])):
            problems.append(f"{m}: as new: your platform gives it a place of its own, which a found row of the miss names in place")
    for k, ns in new_names.items():
        if len(set(ns)) > 1:
            problems.append(f"one new thing named several ways: {sorted(set(ns))}: name it one way")
    # the notes
    md = path[:-4] + ".md"
    if not os.path.exists(md):
        problems.append(f"no notes {part}.md")
    else:
        txt = open(md, encoding="utf-8").read()
        first = txt.split("\n", 1)[0]
        named = notes_commits(first)
        for repo, cs in commits.items():
            if repo == RELEASE:
                if RELEASE not in first:
                    problems.append(f"{part}.md: its first line names {RELEASE}")
            elif not any(same(c, x) for c in cs for x in named.get(repo, ())):
                problems.append(f"{part}.md: its first line names the commits fixed for the run: {repo}@{', '.join(sorted(cs))}")
        nt = he.fold(txt)
        for k, ns in new_names.items():
            if he.fold(ns[0]) not in nt:
                problems.append(f"{part}.md doesn't name the new thing {ns[0]!r}")
        for m in semi(pr["misses"]):
            if m not in txt:
                problems.append(f"{part}.md doesn't name {m}, with what {p} holds of each part and why you propose what you do")
    return rs, problems, notes


def reading_problems(p, r, text, S):
    """Each quote in single quotes in a reading is found in the row's quote or id, its source, or a file or statement the
    reading names (held_entries.py's QUOTE test)."""
    hay = [he.quote_norm(text or "")]
    srcs = []
    if FILE_SOURCE.match(r["source"].strip()):
        srcs.append((r["source"].strip(), r["locator"].strip()))
    for m in NAMED.finditer(r["reading"]):
        x = m.group(0).rstrip(".:")
        a = re.match(r"^(.+\.warc\.gz)@(\d+)$", x)
        srcs.append((a.group(1), a.group(2)) if a else (x, ""))
    out = []
    qs = he.QUOTE.findall(r["reading"])
    if not qs:
        return out
    for s, loc in srcs:
        texts, why = S.texts(s, loc)
        hay += [he.quote_norm(t) for k, t, o in texts or [] if k == "exact"]
    hay.append(he.cited_text(p, r["reading"]))
    for qt in qs:
        qn = he.quote_norm(qt)
        if "..." in qt or "…" in qt:
            qn = max((he.quote_norm(x) for x in re.split(r"\.\.\.|…", qt)), key=len)
        if qn and not any(qn in h for h in hay):
            out.append(f"the reading's quote '{clip(qt, 70)}' is found neither in the row's quote, its source, nor a file or statement the reading names: copy it exactly")
    return out


def cmd_check(a):
    pr = part_row(a.part)
    rs, problems, notes = check_part(pr)
    for n in notes:
        print("NOTE", n)
    for x in problems:
        print("PROBLEM", x)
    n = collections.Counter(r["outcome"] for _, r in rs)
    print(f"{a.part}: {len(rs)} rows ({', '.join(f'{k} {v}' for k, v in sorted(n.items())) or 'none'}) for "
          f"{len(semi(pr['cells']))} cells and {sum(len(MISS_PARTS[m]) for m in semi(pr['misses']))} parts of "
          f"{len(semi(pr['misses']))} misses; {len(notes)} notes, {len(problems)} problems")
    sys.exit(1 if problems else 0)


# ---------------------------------------------------------------- the coordinator's commands

def commits_now():
    c = head_commits(9)
    return ";".join([f"{r}@{c[r]}" for r in EVIDENCE] + [RELEASE])


def compute_parts():
    caps = caps_table()
    by_p = collections.defaultdict(list)
    for r in rows(os.path.join(MERGED, "cells.tsv")):
        if r["held"] == "none-held":
            by_p[r["platform"]].append(r["cap_id"])
    commits = commits_now()
    model = commits.split("sharrwah-knowledge-map@")[1].split(";")[0]
    out = []
    for p in PLATFORMS:
        cs = sorted(by_p[p], key=lambda c: (caps[c]["domain"], caps[c]["area"], c))
        halves = [(f"S2-{PREFIX[p]}-{h}", d, MISS_HALF[h]) for h, d in HALVES] if len(cs) > SPLIT_AT else [(f"S2-{PREFIX[p]}", "ABCDEFG", list(MISSES))]
        for part, doms, ms in halves:
            out.append({"part": part, "platform": p, "domains": ";".join(doms),
                        "cells": ";".join(c for c in cs if caps[c]["domain"] in doms), "misses": ";".join(ms),
                        "commits": commits, "model": model, "state": "open"})
    return out


def cmd_parts(a):
    caps = caps_table()
    ps = compute_parts()
    for r in ps:
        cs = semi(r["cells"])
        by = collections.Counter(caps[c]["domain"] for c in cs)
        print(f"{r['part']}\t{r['platform']}\t{len(cs)} cells ({', '.join(f'{d} {by[d]}' for d in semi(r['domains']) if by[d])})\t{len(semi(r['misses']))} misses\t{r['commits']}")
    print(f"{len(ps)} parts, {sum(len(semi(r['cells'])) for r in ps)} cells holding nothing")
    if a.write:
        old = parts_rows()
        if any(r["state"] != "open" for r in old):
            sys.exit(f"{rel(PARTS_TSV)}: a part is checked or landed already; its cells stay as they were: not rewritten")
        write_tsv(PARTS_TSV, PARTS_HEAD, ps)
        print(f"wrote {rel(PARTS_TSV)}")


def set_state(part, state):
    rs = parts_rows()
    for r in rs:
        if r["part"] == part:
            r["state"] = state
    write_tsv(PARTS_TSV, PARTS_HEAD, rs)


def cmd_mark(a):
    pr = part_row(a.part)
    if a.state == "checked":
        _, problems, _ = check_part(pr)
        if problems:
            sys.exit(f"{a.part}: {len(problems)} problems: run check --part {a.part}; not marked checked")
    set_state(a.part, a.state)
    print(f"{a.part}: {a.state}")


def all_rows():
    out = collections.defaultdict(list)
    for pr in parts_rows():
        for i, r in part_file_rows(pr):
            out[pr["platform"]].append((pr["part"], i, r))
    return out


def held_of(rs, parts):
    """yes where every part is found, part where some are, no where none is; the parts absent, unreadable or unclear
    named (inspection-Q3M.md, Q3M-3)."""
    if not rs:
        return "not read yet"
    found = {r["subject"] for _, _, r in rs if r["outcome"] == "found"}
    v = "yes" if all(x in found for x in parts) else "part" if found else "no"
    rest = [f"{r['outcome']}: {r['subject'].split(': ', 1)[1]}" for _, _, r in rs if r["outcome"] in ("absent", "unreadable", "unclear")]
    missing = [x for x in parts if not any(r["subject"] == x for _, _, r in rs)]
    return v + (f" ({'; '.join(rest)})" if rest else "") + (f" [{len(missing)} parts with no row yet]" if missing else "")


def cmd_misses_join(a):
    allr = all_rows()
    for m in ([a.miss] if a.miss else list(MISSES)):
        if m not in MISSES:
            sys.exit(f"no miss {m}")
        print(f"{m}: {MISSES[m][1]}")
        subs = [f"{m}: {x}" for x in MISS_PARTS[m]]
        for sj in subs:
            print(f"   {sj}")
            for p in PLATFORMS:
                rs = [(part, i, r) for part, i, r in allr.get(p, []) if r["subject"] == sj]
                if not rs:
                    print(f"      {p}: no row yet")
                    continue
                ocs = ", ".join(f"{r['outcome']} ({part} line {i})" for part, i, r in rs)
                prop = "; ".join(dict.fromkeys(f"{r['cap_id'] or '-'} ({r['as']})" for _, _, r in rs))
                pl = "; ".join(dict.fromkeys(r["place"] for _, _, r in rs if r["place"]))
                print(f"      {p}: {ocs}; proposes {prop}{'; place: ' + pl if pl else ''}")
        print("   held: " + "; ".join(f"{p} {held_of([x for x in allr.get(p, []) if x[2]['subject'] in subs], subs)}" for p in PLATFORMS))
        print()


def decisions(problems=None):
    problems = [] if problems is None else problems
    return read_tsv(os.path.join(HELD, "s2-misses.tsv"), MISSES_HEAD, problems, "s2-misses.tsv")


def cmd_check_misses(a):
    problems = []
    rs = decisions(problems)
    caps = caps_table()
    allr = all_rows()
    placed = collections.defaultdict(bool)
    for p, xs in allr.items():
        for part, i, r in xs:
            m = r["subject"].split(":")[0]
            if m in MISSES and r["outcome"] == "found" and r["place"].strip() not in ("", "none"):
                placed[m] = True
    seen = set()
    for i, r in rs:
        w = f"s2-misses.tsv line {i}"
        m, cap, as_ = r["miss"].strip(), r["capability"].strip(), r["as"].strip()
        if m not in MISSES:
            problems.append(f"{w}: miss is one of M-01 to M-13")
            continue
        if m in seen:
            problems.append(f"{w}: {m} decided again: one row per miss")
        seen.add(m)
        if as_ not in AS:
            problems.append(f"{w}: as is one of {', '.join(AS)}")
        elif as_ in ("its thing", "feature") and cap not in caps:
            problems.append(f"{w}: as {as_} names a cap_id of the merged model")
        elif as_ == "new":
            if not re.match(r"^new:\S", cap):
                problems.append(f"{w}: as new names new:<name>")
            elif not placed[m]:
                problems.append(f"{w}: new, but no platform's found row names a place of its own")
        elif as_ == "not a capability" and cap:
            problems.append(f"{w}: not a capability leaves capability empty")
        if not r["reading"].strip():
            problems.append(f"{w}: reading says why, from the five platforms' rows")
    for m in MISSES:
        if m not in seen:
            problems.append(f"{m} has no decision")
    for x in problems:
        print("PROBLEM", x)
    print(f"{len(seen)} of {len(MISSES)} misses decided; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def passage_id(p, src, loc, quote, base, taken):
    """<PREFIX>-E-<hex>: sha1 of the second stage's mark, the repository and path without the commit, the locator and
    the folded quote; lengthened where another passage holds the id (design, section 3.2)."""
    m = FILE_SOURCE.match(src)
    where = f"{m.group(1) or m.group(3)}:{m.group(4).strip()}"
    passage = (where, loc.strip(), he.fold(quote))
    h = hashlib.sha1(f"second-stage\x00{where}\x00{loc.strip()}\x00{he.fold(quote)}".encode()).hexdigest()
    for n in (8, 10, 12, 40):
        i = f"{PREFIX[p]}-E-{h[:n]}"
        if i not in base and taken.get(i) in (None, passage):
            taken[i] = passage
            return i, n
    sys.exit("an id collision no length resolves")


def platform_commits(p, pr):
    c = parse_commits(pr["commits"])
    return ";".join(f"{r}@{sorted(c.get(r, {''}))[0]}" if r != RELEASE else RELEASE for r in OWN[p])


def evidence_rows(p):
    out = []
    for path in glob.glob(os.path.join(MODEL, "parts", "*", "evidence.tsv")):
        out += [r for r in rows(path) if r.get("platform") == p]
    return out


def keep_others(path, head, col, value):
    """The rows of a shared file that another batch or platform wrote, kept as they are."""
    return [r for _, r in (read_tsv(path, head, []) if os.path.exists(path) else []) if r[col] != value]


def cmd_land(a):
    p, X = a.platform, PREFIX[a.platform]
    main_b = f"S2-{X}"
    B = a.batch or main_b
    if not re.fullmatch(rf"{re.escape(main_b)}(?:-R\d+)?", B):
        sys.exit(f"the batch is {main_b}, or a correction batch {main_b}-R<n>")
    prs = [r for r in parts_rows() if r["platform"] == p]
    if not prs:
        sys.exit(f"no part of {p} in {rel(PARTS_TSV)}")
    use = [r for r in prs if r["state"] in ("checked", "landed")]
    for r in prs:
        if r not in use:
            print(f"{r['part']}: {r['state']}: waits, and lands in turn once checked")
    if not use:
        sys.exit(f"no part of {p} is checked")
    batches_tsv = os.path.join(HELD, "batches.tsv")
    listed = [r["batch"] for r in rows(batches_tsv)]
    earlier = [b for b in listed if b != B and (b == main_b or b.startswith(main_b + "-R"))]
    if B == main_b and earlier:
        sys.exit(f"{', '.join(earlier)} exist: land the next correction batch, --batch {main_b}-R{len(earlier) + 1}")
    if B != main_b and main_b not in listed:
        sys.exit(f"{main_b} is not landed yet: land it first")
    ev = evidence_rows(p)
    if any(re.match(rf"^\(the held pass's second stage, {re.escape(B)}[,)]", r.get("why", "")) for r in ev):
        sys.exit(f"{B} was applied: its lines are in the model's evidence. Land what came after in a correction batch, "
                 f"--batch {main_b}-R{len([b for b in listed if b.startswith(main_b + '-R')]) + 1} (design, section 3.2)")
    in_model = {(r["cap_id"], r["key"]) for r in ev}
    allrows = []
    for pr in use:
        rs, problems, _ = check_part(pr)
        if problems:
            sys.exit(f"{pr['part']}: {len(problems)} problems: run check --part {pr['part']}; nothing landed")
        allrows += [(pr, i, r) for i, r in rs]
    dec_problems = []
    dec = {r["miss"].strip(): r for _, r in decisions(dec_problems)} if os.path.exists(os.path.join(HELD, "s2-misses.tsv")) else {}
    if dec_problems:
        sys.exit(f"held/s2-misses.tsv: {dec_problems[0]}: run check-misses")
    caps = caps_table()
    cells = merged_cells()
    base = {e["entry_id"] for e in he.entries(p, second=False)}
    old_s2 = rows(os.path.join(HELD, p, "entries-s2.tsv"))
    cit = {skey(x): x for x in citable(p)}
    taken, entries, lines, keys, outcomes, captures, not_landed, lengthened = {}, collections.OrderedDict(), collections.OrderedDict(), [], [], [], [], []
    batch_ids, misses_landed, became = [], collections.Counter(), set()
    # what earlier S2 batches of the platform hold, which a correction batch leaves out
    e_lines, e_keys, e_out = set(), set(), set()
    for b in earlier:
        e_lines |= {(r["entry_id"], r["cap_id"], r["scope"], r["filler"]) for r in rows(os.path.join(HELD, p, f"placements-{b}.tsv"))}
    e_keys = {(r["cap_id"], r["key"]) for r in rows(os.path.join(HELD, p, "s2-keys.tsv")) if r["batch"] in earlier}
    e_out = {(r["part"], r["subject"], r["outcome"]) for r in rows(os.path.join(HELD, p, "s2-outcomes.tsv")) if r["batch"] in earlier}
    cell_ids = {c for pr in use for c in semi(pr["cells"])}
    for pr, i, r in allrows:
        part, ref = pr["part"], f"s2/{pr['part']}.tsv line {i}"
        subj, oc, src = r["subject"].strip(), r["outcome"].strip(), r["source"].strip()
        eid = None
        if oc in CITING and FILE_SOURCE.match(src):
            eid, n = passage_id(p, src, r["locator"], r["quote"], base, taken)
            if n > 8:
                lengthened.append(f"{ref}: {eid} ({n} digits)")
            if eid not in entries:
                entries[eid] = {"entry_id": eid, "structure": "second-stage", "labels": part, "source": src,
                                "locator": r["locator"].strip(), "section": r["identifier"].strip(), "text": r["quote"]}
            elif part not in entries[eid]["labels"].split(","):
                entries[eid]["labels"] += "," + part
        elif oc in CITING:
            eid = src                              # an id already held
        if r["capture"].strip():
            captures.append({"platform": p, "part": part, "line": str(i), "subject": subj, "outcome": oc,
                             "could_change": r["could_change"], "capture": r["capture"], "reading": r["reading"]})
        if oc != "found":
            if (part, subj, oc) not in e_out:
                outcomes.append({"batch": B, "subject": subj, "outcome": oc, "part": part, "line": str(i),
                                 "commits": platform_commits(p, pr), "entry_id": eid if eid in entries else "",
                                 "source": src, "locator": r["locator"], "quote": r["quote"], "read": r["read"],
                                 "searched": r["searched"], "capture": r["capture"], "could_change": r["could_change"],
                                 "reading": r["reading"]})
            continue
        if subj in cell_ids:
            cap = subj
        elif subj == "new":
            cap = r["cap_id"].strip()
        else:
            m = subj.split(":")[0]
            d = dec.get(m)
            if not d:
                sys.exit(f"{m}: a found row ({ref}) and no decision in held/s2-misses.tsv: decide it first (check-misses)")
            if d["as"].strip() == "not a capability":
                not_landed.append(f"{ref}: {m} is not a capability (held/s2-misses.tsv): it stays in Q3's record")
                continue
            cap = d["capability"].strip()
            misses_landed[f"{m} -> {cap} ({d['as'].strip()})"] += 1
        if not cap.startswith("new:") and (cap not in caps or (cap, p) not in cells):
            sys.exit(f"{ref}: {cap} has no cell for {p} in the merged model")
        if (cap, eid) in in_model:
            not_landed.append(f"{ref}: {eid} is in the model's evidence on {cap} already")
            continue
        if not cap.startswith("new:") and cells[(cap, p)]["held"] != "statements":
            became.add(cap)
        if eid in entries or ENTRY_ID.match(eid):
            k = (eid, cap, r["scope"].strip(), r["filler"].strip())
            if k in e_lines:
                continue
            if k in lines:
                lines[k]["refs"].append(ref)
                continue
            lines[k] = {"entry_id": eid, "placement": "new" if cap.startswith("new:") else "capability", "cap_id": cap,
                        "supports": r["supports"], "scope": r["scope"], "terms": r["terms"], "filler": r["filler"],
                        "quality": r["quality"], "reading": " ".join(r["reading"].split()), "refs": [ref]}
            if eid not in batch_ids:
                batch_ids.append(eid)
        else:
            if (cap, eid) in e_keys or any(x["cap_id"] == cap and x["key"] == eid for x in keys):
                continue
            keys.append({"batch": B, "cap_id": cap, "platform": p, "supports": r["supports"], "key": eid,
                         "why": f"(the held pass's second stage, {B}, {part} line {i}) {' '.join(r['reading'].split())}",
                         "terms": r["terms"], "filler": r["filler"], "quality": r["quality"]})
    # an entry a placements file of another batch names, or the model's evidence cites, is never dropped
    protected = {r["key"] for r in ev}
    for path in glob.glob(os.path.join(HELD, p, "placements-*.tsv")):
        if os.path.basename(path) != f"placements-{B}.tsv":
            for r in rows(path):
                protected |= set(semi(r["entry_id"]))
    lost = {e["entry_id"] for e in old_s2} - set(entries)
    if lost & protected:
        sys.exit(f"{p}: the landing would drop {len(lost & protected)} entries of entries-s2.tsv that a placements file or the model names, such as {sorted(lost & protected)[:3]}: refused")
    # the counts
    n = collections.Counter(r["outcome"] for _, _, r in allrows)
    commits = list(dict.fromkeys(x for pr in use for x in semi(pr["commits"])))
    print(f"{p}, {B}: {len(allrows)} rows from {', '.join(pr['part'] for pr in use)} ({', '.join(f'{k} {v}' for k, v in sorted(n.items()))})")
    print(f"   {len(entries)} entries in entries-s2.tsv, {len(batch_ids)} in the batch, {len(lines)} placement lines, "
          f"{len(keys)} rows to s2-keys.tsv, {len(outcomes)} outcomes, {len(captures)} capture leads, {len(not_landed)} rows not landed")
    print(f"   cells that would become held: {', '.join(sorted(became)) or 'none'}")
    for x in lengthened:
        print(f"   COLLISION {x}")
    for x, k in misses_landed.items():
        print(f"   MISS {x}: {k} rows")
    for x in not_landed:
        print(f"   NOT LANDED {x}")
    if a.dry_run:
        return
    write_tsv(os.path.join(HELD, p, "entries-s2.tsv"), he.E_HEAD, list(entries.values()))
    os.makedirs(os.path.join(HELD, "batches"), exist_ok=True)
    with open(os.path.join(HELD, "batches", f"{B}.txt"), "w", encoding="utf-8") as f:
        f.write("".join(x + "\n" for x in batch_ids))
    raw = open(batches_tsv, encoding="utf-8").read().rstrip("\n").split("\n") if os.path.exists(batches_tsv) else ["batch\tplatform\tentries\tstructures"]
    row = f"{B}\t{p}\t{len(batch_ids)}\tsecond-stage"
    raw = [row if l.split("\t")[0] == B else l for l in raw]
    if row not in raw:
        raw.append(row)
    open(batches_tsv, "w", encoding="utf-8").write("\n".join(raw) + "\n")
    pl = [dict(v, reading=f"{v['reading']} (the second stage: {'; '.join(v['refs'])})") for v in lines.values()]
    write_tsv(os.path.join(HELD, p, f"placements-{B}.tsv"), he.P_HEAD, pl)
    kp = os.path.join(HELD, p, "s2-keys.tsv")
    write_tsv(kp, KEYS_HEAD, keep_others(kp, KEYS_HEAD, "batch", B) + keys)
    op = os.path.join(HELD, p, "s2-outcomes.tsv")
    write_tsv(op, OUT_HEAD, keep_others(op, OUT_HEAD, "batch", B) + outcomes)
    cp = os.path.join(HELD, "s2-captures.tsv")
    write_tsv(cp, CAPTURES_HEAD, keep_others(cp, CAPTURES_HEAD, "platform", p) + captures)
    news = collections.Counter(v["cap_id"][4:] for v in lines.values() if v["cap_id"].startswith("new:"))
    news.update(k["cap_id"][4:] for k in keys if k["cap_id"].startswith("new:"))
    md = [" ".join(x.replace(";", " ") for x in commits),
          "",
          f"# Notes: the held pass's second stage, {p}, batch {B} (written by method/s2_held.py land)",
          "",
          f"Parts landed: {', '.join(pr['part'] for pr in use)}. Still open: {', '.join(r['part'] for r in prs if r not in use) or 'none'}.",
          "",
          "## Counts by outcome", ""]
    md += [f"- {k}: {v}" for k, v in sorted(n.items())]
    md += ["", f"{len(entries)} entries in entries-s2.tsv ({len([e for e in entries if e not in batch_ids])} of no batch: "
           f"the absent and unclear rows' passages, and the found rows not landed), {len(lines)} placement lines, "
           f"{len(keys)} rows to s2-keys.tsv.", "", "## New things", ""]
    md += [f"- {k}: {v} line{'s' if v > 1 else ''}" for k, v in news.items()] or ["- none"]
    md += ["", "## Misses landed", ""] + ([f"- {x}: {k} rows" for x, k in misses_landed.items()] or ["- none"])
    md += ["", "## Rows not landed, and why", ""] + ([f"- {x}" for x in not_landed] or ["- none"])
    md += ["", "## Rows sent to s2-keys.tsv", ""] + ([f"- {k['why'].split(')')[0][1:]}: {k['key']} on {k['cap_id']}" for k in keys] or ["- none"])
    open(os.path.join(HELD, p, f"notes-{B}.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    for pr in use:
        if pr["state"] != "landed":
            set_state(pr["part"], "landed")
    print(f"wrote held/{p}/entries-s2.tsv, held/batches/{B}.txt, held/batches.tsv, held/{p}/placements-{B}.tsv, "
          f"notes-{B}.md, s2-keys.tsv, s2-outcomes.tsv, held/s2-captures.tsv; then: "
          f"held_entries.py check --platform {p} --batch {B}; held_amend.py plan --platform {p} --batch {B}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("cells", help="the part's cells holding nothing")
    s.add_argument("--part", required=True); s.add_argument("--from", dest="from_", type=int); s.add_argument("--to", type=int)
    s.add_argument("--left", action="store_true"); s.set_defaults(f=cmd_cells)
    s = sub.add_parser("leads", help="the held pass's leads for the second stage")
    s.add_argument("--part", required=True); s.add_argument("--held", action="store_true"); s.set_defaults(f=cmd_leads)
    s = sub.add_parser("misses", help="the part's misses, with their parts and Q3 rows")
    s.add_argument("--part", required=True); s.set_defaults(f=cmd_misses)
    s = sub.add_parser("check", help="tests a part's rows and notes")
    s.add_argument("--part", required=True); s.set_defaults(f=cmd_check)
    s = sub.add_parser("parts", help="the parts; --write writes held/s2-parts.tsv")
    s.add_argument("--write", action="store_true"); s.set_defaults(f=cmd_parts)
    s = sub.add_parser("mark", help="sets a part's state")
    s.add_argument("--part", required=True); s.add_argument("--state", choices=["checked", "open"], required=True)
    s.set_defaults(f=cmd_mark)
    s = sub.add_parser("misses-join", help="each miss's rows on the five platforms")
    s.add_argument("--miss"); s.set_defaults(f=cmd_misses_join)
    s = sub.add_parser("check-misses", help="tests held/s2-misses.tsv")
    s.set_defaults(f=cmd_check_misses)
    s = sub.add_parser("land", help="lands a platform's checked parts into its batch")
    s.add_argument("--platform", choices=PLATFORMS, required=True); s.add_argument("--batch")
    s.add_argument("--dry-run", action="store_true"); s.set_defaults(f=cmd_land)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
