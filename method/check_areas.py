"""Check the areas files of step R1.

Usage:
  python3 -I method/check_areas.py PLATFORM [AREAS_DIR]   one platform's areas file
  python3 -I method/check_areas.py merged [AREAS_DIR]     the coordinator's merged list and depth choice

AREAS_DIR defaults to studies/proposals/areas. Files are read tab-separated, with no quoting.

For one platform, it reads areas-<platform>.tsv and areas-<platform>-notes.md, and checks:
- the columns;
- each area_id is unique and of the form <CODE>-A-<nn>;
- each area has at least one name, and each name is one of the platform's own names, whole, under
  the label its brackets give (method/areas_extract.py, own_names);
- grouping is "platform's own" or "agent's own", and an "agent's own" grouping gives its reason in note;
- each area has a plain line;
- concern_ids holds only this platform's concern ids, and each concern is under exactly one area, or
  listed under the notes' "## Under none" heading as "- <id>: <reason>".
It warns when the number of areas is outside 15 to 30.

For the merged list, it reads areas.tsv and depth.tsv, and checks:
- the columns, and each area_id unique, of the form A-<nn>;
- each platform area is in exactly one merged area, and each id named is a platform area;
- a heading taken from a platform names that platform and label, and is one of its own names;
  a heading of the coordinator's own gives its reason in note;
- each area has a plain line, what a "won't do" mark removes, and what is kept anyway;
- an area no question draws on says why the work leaves it out;
- depth.tsv has one row for each question and platform, a depth of "in depth", "check" or "none",
  a reason, and what the reason cites; and each question has at least one platform in depth,
  unless all its rows are "none".
It warns when the merged list has fewer than 10 or more than 60 areas.

Exit status 1 if there is any problem. Warnings don't fail.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from areas_extract import CM, PLATFORMS, own_names

CODE = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
COLS = ["area_id", "platform_names", "plain_line", "grouping", "concern_ids", "note"]
MERGED_COLS = ["area_id", "heading", "heading_source", "plain_line", "platform_area_ids", "questions",
               "wont_do_removes", "kept_anyway", "left_out", "note"]
DEPTH_COLS = ["question", "platform", "depth", "why", "cites"]
QUESTIONS = [f"Q{i}" for i in range(1, 9)]


def read(path, cols, problems):
    with open(path, encoding="utf-8") as f:
        rd = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        if rd.fieldnames != cols:
            problems.append(f"{os.path.basename(path)}: columns are {rd.fieldnames}, not {cols}")
        return list(rd)


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def name_parts(cell):
    """'Payments [settings]; Shopify Payments [term]' -> [('Payments', 'settings'), ...]."""
    out = []
    for part in split(cell):
        m = re.match(r"^(.*?)\s*\[([^\]]+)\]$", part)
        out.append((m.group(1).strip(), m.group(2).strip()) if m else (part, None))
    return out


def under_none(notes):
    """Ids listed under the notes' '## Under none' heading, each with a reason."""
    ids, bad = {}, []
    m = re.search(r"^## Under none\s*$(.*?)(?=^## |\Z)", notes, flags=re.M | re.S)
    if not m:
        return ids, bad
    for ln in m.group(1).splitlines():
        if not ln.strip().startswith("-"):
            continue
        mm = re.match(r"^\s*-\s*([A-Z]{2}-C-\d+)\s*:\s*(.*)$", ln)
        if mm and mm.group(2).strip():
            ids[mm.group(1)] = mm.group(2).strip()
        else:
            bad.append(ln.strip())
    return ids, bad


def check_platform(platform, d):
    problems, warnings = [], []
    code = CODE[platform]
    names = own_names(platform)
    with open(os.path.join(CM, platform, "concerns.tsv"), encoding="utf-8") as f:
        con = {r["concern_id"] for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}
    notes_path = os.path.join(d, f"areas-{platform}-notes.md")
    notes = open(notes_path, encoding="utf-8").read() if os.path.exists(notes_path) else ""
    rows = read(os.path.join(d, f"areas-{platform}.tsv"), COLS, problems)
    ids, placed = set(), {}
    for r in rows:
        a = r.get("area_id") or ""
        if not re.fullmatch(rf"{code}-A-\d{{2}}", a):
            problems.append(f"{a or '(no id)'}: area_id isn't of the form {code}-A-<nn>")
        if a in ids:
            problems.append(f"{a}: area_id used twice")
        ids.add(a)
        parts = name_parts(r.get("platform_names"))
        if not parts:
            problems.append(f"{a}: no name")
        for name, label in parts:
            if label is None:
                problems.append(f"{a}: name without its list in brackets: {name}")
            elif label not in names:
                problems.append(f"{a}: unknown label [{label}] for: {name}")
            elif name not in names[label]:
                problems.append(f"{a}: not one of the platform's own names under [{label}]: {name}")
        if r.get("grouping") not in ("platform's own", "agent's own"):
            problems.append(f"{a}: grouping is '{r.get('grouping')}'")
        if r.get("grouping") == "agent's own" and not (r.get("note") or "").strip():
            problems.append(f"{a}: an agent's own grouping gives no reason in note")
        if not (r.get("plain_line") or "").strip():
            problems.append(f"{a}: no plain line")
        for i in split(r.get("concern_ids")):
            if i not in con:
                problems.append(f"{a}: {i} in concern_ids isn't a concern of {platform}")
            placed.setdefault(i, []).append(a)
    for i, areas in placed.items():
        if len(areas) > 1:
            problems.append(f"{i} is under more than one area: {', '.join(areas)}")
    none, bad = under_none(notes)
    for ln in bad:
        problems.append(f"notes, Under none: not '- <concern id>: <reason>': {ln}")
    for i in sorted(none):
        if i in placed:
            problems.append(f"{i} is under an area and also under none")
        if i not in con:
            problems.append(f"notes, Under none: {i} isn't a concern of {platform}")
    for i in sorted(con - set(placed) - set(none)):
        problems.append(f"{i} is under no area, and not under none with a reason")
    if not 15 <= len(rows) <= 30:
        warnings.append(f"{len(rows)} areas, outside the brief's aim of 15 to 30")
    return f"{platform}: {len(rows)} areas, {len(placed)} concerns placed, {len(none)} under none", problems, warnings


def check_merged(d):
    problems, warnings = [], []
    platform_areas, platform_names = {}, {}
    for p in PLATFORMS:
        path = os.path.join(d, f"areas-{p}.tsv")
        if not os.path.exists(path):
            problems.append(f"areas-{p}.tsv is missing")
            continue
        for r in read(path, COLS, problems):
            platform_areas[r["area_id"]] = p
        platform_names[p] = own_names(p)
    rows = read(os.path.join(d, "areas.tsv"), MERGED_COLS, problems)
    ids, member = set(), {}
    for r in rows:
        a = r.get("area_id") or ""
        if not re.fullmatch(r"A-\d{2}", a):
            problems.append(f"{a or '(no id)'}: area_id isn't of the form A-<nn>")
        if a in ids:
            problems.append(f"{a}: area_id used twice")
        ids.add(a)
        for pa in split(r.get("platform_area_ids")):
            if pa not in platform_areas:
                problems.append(f"{a}: {pa} isn't a platform area")
            member.setdefault(pa, []).append(a)
        src = (r.get("heading_source") or "").strip()
        m = re.match(r"^(\w+)\s*\[([^\]]+)\]$", src)
        if src == "coordinator's own":
            if not (r.get("note") or "").strip():
                problems.append(f"{a}: a heading of the coordinator's own gives no reason in note")
        elif m and m.group(1) in platform_names:
            p, label = m.group(1), m.group(2)
            if (r.get("heading") or "").strip() not in platform_names[p].get(label, set()):
                problems.append(f"{a}: heading isn't one of {p}'s own names under [{label}]")
        else:
            problems.append(f"{a}: heading_source is '{src}', not '<platform> [label]' or \"coordinator's own\"")
        for col in ("plain_line", "wont_do_removes", "kept_anyway"):
            if not (r.get(col) or "").strip():
                problems.append(f"{a}: no {col}")
        qs = split(r.get("questions"))
        for q in qs:
            if q not in QUESTIONS:
                problems.append(f"{a}: unknown question {q}")
        if not qs and not (r.get("left_out") or "").strip():
            problems.append(f"{a}: no question draws on it, and left_out doesn't say why")
    for pa in sorted(platform_areas):
        n = len(member.get(pa, []))
        if n != 1:
            problems.append(f"{pa} is in {n} merged areas, not one")
    if not 10 <= len(rows) <= 60:
        warnings.append(f"{len(rows)} merged areas: 'tens, not hundreds' expects about 10 to 60")
    depth_path = os.path.join(d, "depth.tsv")
    if not os.path.exists(depth_path):
        problems.append("depth.tsv is missing")
    else:
        drows = read(depth_path, DEPTH_COLS, problems)
        seen = {}
        for r in drows:
            key = (r.get("question"), r.get("platform"))
            if key[0] not in QUESTIONS or key[1] not in PLATFORMS:
                problems.append(f"depth.tsv: unknown question or platform {key}")
            if key in seen:
                problems.append(f"depth.tsv: {key} given twice")
            seen[key] = r.get("depth")
            if r.get("depth") not in ("in depth", "check", "none"):
                problems.append(f"depth.tsv: {key} depth is '{r.get('depth')}'")
            if not (r.get("why") or "").strip() or not (r.get("cites") or "").strip():
                problems.append(f"depth.tsv: {key} needs both why and cites")
        for q in QUESTIONS:
            ds = [seen.get((q, p)) for p in PLATFORMS]
            if None in ds:
                problems.append(f"depth.tsv: {q} lacks a row for some platform")
            elif "in depth" not in ds and set(ds) != {"none"}:
                problems.append(f"depth.tsv: {q} has no platform in depth")
    return f"merged: {len(rows)} areas over {len(platform_areas)} platform areas", problems, warnings


def main(which, d):
    head, problems, warnings = check_merged(d) if which == "merged" else check_platform(which, d)
    print(f"{head}; {len(problems)} problems, {len(warnings)} warnings")
    for p in problems:
        print("  problem: " + p)
    for w in warnings:
        print("  warning: " + w)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else os.path.join(SKM, "studies", "proposals", "areas")))
