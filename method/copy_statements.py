"""Copy the recorded statements that bear on a question, for steps R2 and R3.

Usage:
  python3 -I method/copy_statements.py QUESTION PLATFORM [OUT_DIR]   write one question's copies for one platform
  python3 -I method/copy_statements.py --counts                      count what each question and platform would copy

A question draws on the merged areas whose `questions` column names it (studies/proposals/areas/areas.tsv). For a
platform, those merged areas hold some of its platform areas (areas-<platform>.tsv), and those hold concerns. The
copies are the concern map's statements under those concerns, and the gaps recorded under them, unchanged, with
the citations they cite. For Q5 they also hold the pilot's statements (studies/subjects/S-01/<platform>/), which the
money paragraph of Q5 reuses.

OUT_DIR defaults to studies/proposals/records/<QUESTION>/<platform>/. It writes:
- copied.tsv: copy_id, source_file, source_line, then every column of the concern map's statement row, unchanged;
- copied-pilot.tsv (Q5 only): copy_id, source_file, source_line, then every column of the pilot's statement row;
- copied-citations.tsv: source_file, then every column of each citation those rows cite, unchanged;
- copied-gaps.tsv: source_file, source_line, then every column of the concern map's gaps under those concerns;
- selection.tsv: id, action, reason. One row per concern copied, and for Q5 one row for the pilot's statements,
  each with action "copied". The run adds what it adds and sets aside what doesn't bear, each with its reason.
Files are tab-separated, with a header row and no quoting.
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


def read(path):
    """(header, [(line number, row dict)]) for a tab-separated file with no quoting."""
    with open(path, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        return rd.fieldnames, [(i, r) for i, r in enumerate(rd, start=2)]


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def concerns_for(question, platform):
    """The concern ids of a platform that a question draws on, through the merged areas, in the platform's order."""
    _, merged = read(os.path.join(AREAS, "areas.tsv"))
    wanted = set()
    for _, r in merged:
        if question in split(r["questions"]):
            wanted.update(split(r["platform_area_ids"]))
    _, mine = read(os.path.join(AREAS, f"areas-{platform}.tsv"))
    out = []
    for _, r in mine:
        if r["area_id"] in wanted:
            out.extend(c for c in split(r["concern_ids"]) if c not in out)
    return out


def rel(path):
    return os.path.relpath(path, SKM)


def write(path, header, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            f.write("\t".join(r) + "\n")


def copy(question, platform, out):
    code = CODE[platform]
    concerns = concerns_for(question, platform)
    keep = set(concerns)
    os.makedirs(out, exist_ok=True)
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
    selection = [[c, "copied", "held under an area the question draws on"] for c in concerns]
    if question == PILOT_QUESTION:
        pst_path = os.path.join(PILOT, platform, "statements.tsv")
        pst_head, pst = read(pst_path)
        pilot, pcites = [], []
        for line, r in pst:
            pilot.append([f"{question}-{code}-P{len(pilot) + 1:04d}", rel(pst_path), str(line)] + [r[c] or "" for c in pst_head])
            pcites.extend(c for c in split(r["cite_ids"]) if c not in pcites)
        write(os.path.join(out, "copied-pilot.tsv"), ["copy_id", "source_file", "source_line"] + pst_head, pilot)
        sources.append((os.path.join(PILOT, platform, "citations.tsv"), pcites))
        selection.append(["S-01", "copied", "the pilot's statements, reused for the money paragraph of Q5"])
    out_cites, cit_head = [], None
    for path, wanted in sources:
        head, rows = read(path)
        cit_head = cit_head or head
        by = {r["cite_id"]: r for _, r in rows}
        out_cites.extend([rel(path)] + [by[c][h] or "" for h in cit_head] for c in wanted if c in by)
    write(os.path.join(out, "copied-citations.tsv"), ["source_file"] + (cit_head or []), out_cites)
    write(os.path.join(out, "selection.tsv"), ["id", "action", "reason"], selection)
    return len(concerns), len(copied), len(gaps)


def counts():
    print("question\tplatform\tconcerns\tstatements\tgaps\tpilot_statements")
    for q in QUESTIONS:
        for p in PLATFORMS:
            cs = set(concerns_for(q, p))
            _, st = read(os.path.join(CM, p, "statements.tsv"))
            _, gp = read(os.path.join(CM, p, "gaps.tsv"))
            n = sum(1 for _, r in st if r["concern_id"] in cs)
            g = sum(1 for _, r in gp if r["concern_id"] in cs)
            pilot = len(read(os.path.join(PILOT, p, "statements.tsv"))[1]) if q == PILOT_QUESTION else 0
            print(f"{q}\t{p}\t{len(cs)}\t{n}\t{g}\t{pilot}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--counts"]:
        counts()
    else:
        q, p = sys.argv[1], sys.argv[2]
        assert q in QUESTIONS and p in PLATFORMS, "usage: copy_statements.py QUESTION PLATFORM [OUT_DIR]"
        out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(SKM, "studies", "proposals", "records", q, p)
        print(f"{q} {p}: %d concerns, %d statements, %d gaps copied to {rel(out)}" % copy(q, p, out))
