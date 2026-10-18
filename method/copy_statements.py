"""Copy the recorded statements that bear on a question, for steps R2 and R3, in two phases.

Usage:
  python3 -I method/copy_statements.py candidates QUESTION PLATFORM [OUT_DIR]
  python3 -I method/copy_statements.py copy QUESTION PLATFORM [OUT_DIR]
  python3 -I method/copy_statements.py --counts

A question draws on the merged areas whose `questions` column names it (studies/proposals/areas/areas.tsv). For a
platform, those merged areas hold some of its platform areas (areas-<platform>.tsv), and those hold concerns.

`candidates` writes OUT_DIR/selection.tsv: one row per concern of those areas, with its terms, the concern map's
description, how many statements and gaps it holds, and its area, and with action `candidate`. For Q5 it adds a row
`S-01` with action `copy`: the pilot's statements, reused for the money paragraph of Q5.

The recording run then sets each row's action:
- `copy`: the concern bears on the question;
- `set aside`: it doesn't, and `reason` says why;
- `add`: a concern of the same platform outside those areas that bears on the question, with its reason.

`copy` reads selection.tsv, refuses while a row is still `candidate` or a `set aside` or `add` row has no reason,
and writes, unchanged:
- copied.tsv: copy_id, source_file, source_line, then every column of the concern map's statement row, for each
  statement under a `copy` or `add` concern;
- copied-gaps.tsv: source_file, source_line, then every column of the concern map's gaps under those concerns;
- copied-pilot.tsv (Q5 only): copy_id, source_file, source_line, then every column of the pilot's statement row;
- copied-citations.tsv: source_file, then every column of each citation the copies cite.

`--counts` prints, for every question and platform, the candidate concerns and the statements and gaps they hold.

OUT_DIR defaults to studies/proposals/records/<QUESTION>/<platform>/. Files are tab-separated, with a header row and
no quoting.
"""
import csv, os, sys

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


def read(path):
    """(header, [(line number, row dict)]) for a tab-separated file with no quoting."""
    with open(path, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        return rd.fieldnames, [(i, r) for i, r in enumerate(rd, start=2)]


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def rel(path):
    return os.path.relpath(path, SKM)


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
    if question == PILOT_QUESTION:
        n = len(read(os.path.join(PILOT, platform, "statements.tsv"))[1])
        rows.append(["S-01", "", "the pilot's statements on who holds the merchant's funds", str(n), "", "", "copy",
                     "reused for the money paragraph of Q5"])
    write(os.path.join(out, "selection.tsv"), SEL, rows)
    return len(rows)


def copy(question, platform, out):
    code = CODE[platform]
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
    st_path = os.path.join(CM, platform, "statements.tsv")
    st_head, st = read(st_path)
    copied, cites = [], []
    for line, r in st:
        if r["concern_id"] in keep:
            copied.append([f"{question}-{code}-K{len(copied) + 1:04d}", rel(st_path), str(line)] + [r[c] or "" for c in st_head])
            cites.extend(c for c in split(r["cite_ids"]) if c not in cites)
    write(os.path.join(out, "copied.tsv"), ["copy_id", "source_file", "source_line"] + st_head, copied)
    gp_path = os.path.join(CM, platform, "gaps.tsv")
    gp_head, gp = read(gp_path)
    gaps = [[rel(gp_path), str(line)] + [r[c] or "" for c in gp_head] for line, r in gp if r["concern_id"] in keep]
    write(os.path.join(out, "copied-gaps.tsv"), ["source_file", "source_line"] + gp_head, gaps)
    sources = [(os.path.join(CM, platform, "citations.tsv"), cites)]
    pilot = []
    if any(r["concern_id"] == "S-01" and r["action"] == "copy" for _, r in sel):
        pst_path = os.path.join(PILOT, platform, "statements.tsv")
        pst_head, pst = read(pst_path)
        pcites = []
        for line, r in pst:
            pilot.append([f"{question}-{code}-P{len(pilot) + 1:04d}", rel(pst_path), str(line)] + [r[c] or "" for c in pst_head])
            pcites.extend(c for c in split(r["cite_ids"]) if c not in pcites)
        write(os.path.join(out, "copied-pilot.tsv"), ["copy_id", "source_file", "source_line"] + pst_head, pilot)
        sources.append((os.path.join(PILOT, platform, "citations.tsv"), pcites))
    out_cites, cit_head = [], None
    for path, wanted in sources:
        head, rows = read(path)
        cit_head = cit_head or head
        by = {r["cite_id"]: r for _, r in rows}
        out_cites.extend([rel(path)] + [by[c][h] or "" for h in cit_head] for c in wanted if c in by)
    write(os.path.join(out, "copied-citations.tsv"), ["source_file"] + (cit_head or []), out_cites)
    return len(keep), len(copied), len(gaps), len(pilot)


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
    if len(args) < 3 or args[0] not in ("candidates", "copy") or args[1] not in QUESTIONS or args[2] not in PLATFORMS:
        sys.exit("usage: copy_statements.py candidates|copy QUESTION PLATFORM [OUT_DIR], or --counts")
    phase, q, p = args[:3]
    out = args[3] if len(args) > 3 else os.path.join(SKM, "studies", "proposals", "records", q, p)
    if phase == "candidates":
        print(f"{q} {p}: {candidates(q, p, out)} rows written to {rel(out)}/selection.tsv")
    else:
        print(f"{q} {p}: %d concerns, %d statements, %d gaps and %d pilot statements copied to {rel(out)}" % copy(q, p, out))
