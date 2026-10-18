"""Copy the recorded statements that bear on a question, for steps R2 and R3, in two phases.

Usage:
  python3 -I method/copy_statements.py candidates QUESTION PLATFORM [OUT_DIR]
  python3 -I method/copy_statements.py show PLATFORM CONCERN_ID [CONCERN_ID ...]
  python3 -I method/copy_statements.py copy QUESTION PLATFORM [OUT_DIR]
  python3 -I method/copy_statements.py --counts

A question draws on the merged areas whose `questions` column names it (studies/proposals/areas/areas.tsv). For a
platform, those merged areas hold some of its platform areas (areas-<platform>.tsv), and those hold concerns.

`candidates` writes OUT_DIR/selection.tsv: one row per concern of those areas, with its terms, the concern map's
description, how many statements and gaps it holds, and its area, and with action `candidate`. Last comes a row `S-01`:
the pilot's statements, gaps and absences on who holds the merchant's funds. It is `copy` for Q5, whose money
paragraph reuses them, and `candidate` for the other questions, whose runs judge it like any other row.

`show` prints the statements of the concerns named: concern_id, line (in the concern map's statements.tsv),
identifier and statement. A run uses it to judge a concern whose terms don't decide it. For S-01 it prints the pilot's
statements, each cut to 160 characters, and for a concern with no statements, its gaps, marked as such.

The recording run then sets each row's action:
- `copy`: the concern bears on the question;
- `set aside`: it doesn't, and `reason` says why;
- `add`: a concern of the same platform outside those areas that bears on the question, with its reason.

`copy` reads selection.tsv, refuses while a row is still `candidate` or a `set aside` or `add` row has no reason,
and writes, unchanged, each row after three columns: copy_id, source_file, source_line. A copy's id is its source
line, so it names the same row however the selection changes: Q2-SA-K1553 is line 1553 of Salla's statements.tsv.
- copied.tsv (K ids): every statement of the concern map under a `copy` or `add` concern;
- copied-gaps.tsv (G ids): every gap of the concern map under those concerns;
- when S-01 is copied, the pilot's: copied-pilot.tsv (P ids), its statements; copied-pilot-gaps.tsv (H ids), its
  gaps; copied-pilot-absences.tsv (A ids), its absences;
- copied-citations.tsv: source_file, then every column of each citation the copies cite;
- two views, to read instead of the copies: copied-index.tsv (copy_id, concern_id, identifier) and copied-view.tsv
  (copy_id, identifier, statement, scope), for every K and P copy. The pilot's concern_id is S-01.

`--counts` prints, for every question and platform, the candidate concerns and the statements and gaps they hold.

OUT_DIR defaults to studies/proposals/records/<QUESTION>/<platform>/. Files are tab-separated, with a header row and
no quoting.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CM = os.path.join(SKM, "studies", "concern-map", "platforms")
PILOT = os.path.join(SKM, "studies", "subjects", "S-01")
AREAS = os.path.join(SKM, "studies", "proposals", "areas")
PLATFORMS = ["shopify", "salla", "woocommerce", "zid", "bigcommerce"]
CODE = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
QUESTIONS = [f"Q{i}" for i in range(1, 9)]
PILOT_QUESTION = "Q5"
SEL = ["concern_id", "terms", "description", "statements", "gaps", "area_id", "action", "reason"]
LEAD = ["copy_id", "source_file", "source_line"]
# copied file -> (id letter, where its rows come from: concern map or pilot, the source file's name)
COPIES = {
    "copied.tsv": ("K", CM, "statements.tsv"),
    "copied-gaps.tsv": ("G", CM, "gaps.tsv"),
    "copied-pilot.tsv": ("P", PILOT, "statements.tsv"),
    "copied-pilot-gaps.tsv": ("H", PILOT, "gaps.tsv"),
    "copied-pilot-absences.tsv": ("A", PILOT, "absences.tsv"),
}


def read(path):
    """(header, [(line number, row dict)]) for a tab-separated file with no quoting."""
    with open(path, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        return rd.fieldnames, [(i, r) for i, r in enumerate(rd, start=2)]


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def cite_split(v):
    """Cite ids, which some rows separate with spaces or commas rather than ";", as the checker reads them."""
    return [x for x in re.split(r"[,\s;]+", v or "") if x]


def rel(path):
    return os.path.relpath(path, SKM)


def copy_id(question, platform, letter, line):
    return f"{question}-{CODE[platform]}-{letter}{line:04d}"


def write(path, header, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            assert all("\t" not in x and "\n" not in x for x in r), r
            f.write("\t".join(r) + "\n")


def candidates_for(question, platform):
    """[(concern_id, area_id)] for the concerns of the platform areas that the question's merged areas hold."""
    _, merged = read(os.path.join(AREAS, "areas.tsv"))
    wanted = set()
    for _, r in merged:
        if question in split(r["questions"]):
            wanted.update(split(r["platform_area_ids"]))
    _, mine = read(os.path.join(AREAS, f"areas-{platform}.tsv"))
    out = []
    for _, r in mine:
        if r["area_id"] in wanted:
            out.extend((c, r["area_id"]) for c in split(r["concern_ids"]))
    return out


def tallies(platform):
    _, st = read(os.path.join(CM, platform, "statements.tsv"))
    _, gp = read(os.path.join(CM, platform, "gaps.tsv"))
    ns, ng = {}, {}
    for _, r in st:
        ns[r["concern_id"]] = ns.get(r["concern_id"], 0) + 1
    for _, r in gp:
        ng[r["concern_id"]] = ng.get(r["concern_id"], 0) + 1
    return ns, ng


def candidates(question, platform, out):
    os.makedirs(out, exist_ok=True)
    _, con = read(os.path.join(CM, platform, "concerns.tsv"))
    info = {r["concern_id"]: r for _, r in con}
    ns, ng = tallies(platform)
    rows = [[c, info[c]["platform_terms"] or "", info[c]["concern"] or "", str(ns.get(c, 0)), str(ng.get(c, 0)), a,
             "candidate", ""] for c, a in candidates_for(question, platform)]
    n = len(read(os.path.join(PILOT, platform, "statements.tsv"))[1])
    pilot = question == PILOT_QUESTION
    rows.append(["S-01", "", "the pilot's statements, gaps and absences on who holds the merchant's funds", str(n),
                 str(len(read(os.path.join(PILOT, platform, "gaps.tsv"))[1])), "", "copy" if pilot else "candidate",
                 "reused for the money paragraph of Q5" if pilot else ""])
    write(os.path.join(out, "selection.tsv"), SEL, rows)
    return len(rows)


def show(platform, concern_ids):
    """Print the statements of each concern named; for S-01, the pilot's, each cut to 160 characters; for a concern
    with no statements, its gaps, marked as such (their wording is the concern map's, not the platform's)."""
    _, con = read(os.path.join(CM, platform, "concerns.tsv"))
    known = {r["concern_id"] for _, r in con} | {"S-01"}
    unknown = [c for c in concern_ids if c not in known]
    if unknown:
        sys.exit(f"not concerns of {platform}: {', '.join(unknown)}")
    _, st = read(os.path.join(CM, platform, "statements.tsv"))
    _, gp = read(os.path.join(CM, platform, "gaps.tsv"))
    print("concern_id\tline\tidentifier\tstatement")
    for c in concern_ids:
        if c == "S-01":
            _, pst = read(os.path.join(PILOT, platform, "statements.tsv"))
            for line, r in pst:
                print(f"S-01\t{line}\t{r['identifier'] or ''}\t{(r['statement'] or '')[:160]}")
            continue
        mine = [(line, r) for line, r in st if r["concern_id"] == c]
        for line, r in mine:
            print(f"{c}\t{line}\t{r['identifier'] or ''}\t{r['statement'] or ''}")
        if not mine:
            for line, r in gp:
                if r["concern_id"] == c:
                    print(f"{c}\tgaps.tsv line {line}\t(no statements; a gap, in the concern map's words)\t{r['what_would_show_it'] or ''}")


def copy_rows(question, platform, name, keep=None):
    """(header, rows) of a copied file: each source row, unchanged, after its copy id, source file and line. The
    concern map's rows are those of the concerns in keep; the pilot's are all."""
    letter, base, fname = COPIES[name]
    path = os.path.join(base, platform, fname)
    head, rows = read(path)
    out = [[copy_id(question, platform, letter, line), rel(path), str(line)] + [r[c] or "" for c in head]
           for line, r in rows if keep is None or r["concern_id"] in keep]
    return LEAD + head, out


def copy(question, platform, out):
    _, sel = read(os.path.join(out, "selection.tsv"))
    problems = []
    for line, r in sel:
        if r["action"] not in ("copy", "set aside", "add"):
            problems.append(f"selection.tsv line {line}: action is '{r['action']}', not copy, set aside or add")
        if r["action"] in ("set aside", "add") and not (r["reason"] or "").strip():
            problems.append(f"selection.tsv line {line}: a '{r['action']}' row needs its reason")
    _, con = read(os.path.join(CM, platform, "concerns.tsv"))
    known = {r["concern_id"] for _, r in con}
    keep = {r["concern_id"] for _, r in sel if r["action"] in ("copy", "add") and r["concern_id"] != "S-01"}
    problems += [f"selection.tsv: {c} isn't a concern of {platform}" for c in sorted(keep - known)]
    if problems:
        sys.exit("\n".join(problems))
    pilot = any(r["concern_id"] == "S-01" and r["action"] == "copy" for _, r in sel)
    names = ["copied.tsv", "copied-gaps.tsv"] + (["copied-pilot.tsv", "copied-pilot-gaps.tsv",
                                                  "copied-pilot-absences.tsv"] if pilot else [])
    files, index, view, wanted = {}, [], [], {}
    for name in names:
        head, rows = copy_rows(question, platform, name, None if name.startswith("copied-pilot") else keep)
        files[name] = rows
        write(os.path.join(out, name), head, rows)
        src = os.path.join(COPIES[name][1], platform, "citations.tsv")
        for r in rows:
            d = dict(zip(head, r))
            for col in ("cite_ids", "list_cite_ids", "complete_cite_ids"):
                for c in cite_split(d.get(col)):
                    wanted.setdefault(src, [])
                    if c not in wanted[src]:
                        wanted[src].append(c)
            if name in ("copied.tsv", "copied-pilot.tsv"):
                index.append([d["copy_id"], d.get("concern_id") or "S-01", d["identifier"]])
                view.append([d["copy_id"], d["identifier"], d["statement"], d["scope"]])
    for name in [n for n in COPIES if n.startswith("copied-pilot") and n not in names]:
        if os.path.exists(os.path.join(out, name)):
            os.remove(os.path.join(out, name))          # a pilot copy left from an earlier selection
    out_cites, cit_head = [], None
    for path, ids in wanted.items():
        head, rows = read(path)
        cit_head = cit_head or head
        by = {r["cite_id"]: r for _, r in rows}
        out_cites.extend([rel(path)] + [by[c][h] or "" for h in cit_head] for c in ids if c in by)
    write(os.path.join(out, "copied-citations.tsv"), ["source_file"] + (cit_head or []), out_cites)
    write(os.path.join(out, "copied-index.tsv"), ["copy_id", "concern_id", "identifier"], index)
    write(os.path.join(out, "copied-view.tsv"), ["copy_id", "identifier", "statement", "scope"], view)
    return {n: len(r) for n, r in files.items()}, len(keep)


def counts():
    print("question\tplatform\tconcerns\tstatements\tgaps")
    for q in QUESTIONS:
        for p in PLATFORMS:
            ns, ng = tallies(p)
            cs = [c for c, _ in candidates_for(q, p)]
            print(f"{q}\t{p}\t{len(cs)}\t{sum(ns.get(c, 0) for c in cs)}\t{sum(ng.get(c, 0) for c in cs)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--counts"]:
        counts()
        sys.exit(0)
    if len(args) >= 3 and args[0] == "show" and args[1] in PLATFORMS:
        show(args[1], args[2:])
        sys.exit(0)
    if len(args) < 3 or args[0] not in ("candidates", "copy") or args[1] not in QUESTIONS or args[2] not in PLATFORMS:
        sys.exit("usage: copy_statements.py candidates|copy QUESTION PLATFORM [OUT_DIR], "
                 "show PLATFORM CONCERN_ID [CONCERN_ID ...], or --counts")
    phase, q, p = args[:3]
    out = args[3] if len(args) > 3 else os.path.join(SKM, "studies", "proposals", "records", q, p)
    if phase == "candidates":
        print(f"{q} {p}: {candidates(q, p, out)} rows written to {rel(out)}/selection.tsv")
    else:
        n, k = copy(q, p, out)
        print(f"{q} {p}: {k} concerns; " + ", ".join(f"{v} rows to {name}" for name, v in n.items()) + f", in {rel(out)}")
