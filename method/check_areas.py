"""Check one platform's areas file against its extract (step R1).

Usage: python3 -I method/check_areas.py PLATFORM [AREAS_DIR]

Reports: inventory entries or concerns placed under no area or more than once (unless listed
under none in the notes), names not found verbatim in the extract, and malformed rows.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLS = ["area_id", "platform_names", "plain_line", "grouping", "inv_ids", "concern_ids", "note"]


def main(platform, d):
    cm = os.path.join(SKM, "studies", "concern-map", "platforms", platform)
    with open(os.path.join(cm, "inventory.tsv"), encoding="utf-8") as f:
        inv = {r["inv_id"] for r in csv.DictReader(f, delimiter="\t") if not r["out_of_scope_reason"]}
    with open(os.path.join(cm, "concerns.tsv"), encoding="utf-8") as f:
        con = {r["concern_id"] for r in csv.DictReader(f, delimiter="\t")}
    extract = open(os.path.join(d, f"extract-{platform}.md"), encoding="utf-8").read()
    notes_path = os.path.join(d, f"areas-{platform}-notes.md")
    notes = open(notes_path, encoding="utf-8").read() if os.path.exists(notes_path) else ""
    problems = []
    with open(os.path.join(d, f"areas-{platform}.tsv"), encoding="utf-8") as f:
        rd = csv.DictReader(f, delimiter="\t")
        if rd.fieldnames != COLS:
            problems.append(f"columns are {rd.fieldnames}, not {COLS}")
        rows = list(rd)
    seen = {}
    for r in rows:
        a = r.get("area_id", "")
        if r.get("grouping") not in ("platform's own", "agent's own"):
            problems.append(f"{a}: grouping is '{r.get('grouping')}'")
        if r.get("grouping") == "agent's own" and not r.get("note"):
            problems.append(f"{a}: an agent's own grouping gives no reason in note")
        if not r.get("plain_line"):
            problems.append(f"{a}: no plain line")
        for part in [x.strip() for x in (r.get("platform_names") or "").split(";") if x.strip()]:
            name = re.sub(r"\s*\[[^\]]*\]\s*$", "", part).strip()
            if name and name not in extract:
                problems.append(f"{a}: name not in the extract verbatim: {name}")
        for col in ("inv_ids", "concern_ids"):
            for i in [x.strip() for x in (r.get(col) or "").split(";") if x.strip()]:
                seen.setdefault(i, []).append(a)
    for i, areas in seen.items():
        if len(areas) > 1:
            problems.append(f"{i} is placed under more than one area: {', '.join(areas)}")
        if i not in inv and i not in con:
            problems.append(f"{i} is not an in-scope inventory entry or concern of {platform}")
    for i in sorted((inv | con) - set(seen)):
        if i not in notes:
            problems.append(f"{i} is under no area, and the notes don't list it")
    print(f"{platform}: {len(rows)} areas; {len(problems)} problems")
    for p in problems:
        print("  " + p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else os.path.join(SKM, "studies", "proposals", "areas")))
