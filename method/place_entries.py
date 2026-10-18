"""Place each in-scope inventory entry under the areas of its concerns, for step R1.

Usage: python3 -I method/place_entries.py PLATFORM [AREAS_DIR]

AREAS_DIR defaults to studies/proposals/areas. Reads areas-<platform>.tsv (the concerns each area
holds) and the concern map's inventory.tsv, and writes areas-<platform>-entries.tsv with the columns
inv_id, list, entry, concern_ids, area_ids, split.
- An entry goes under the area of each of its concerns. The inventories separate an entry's concern
  ids with ";", "," or spaces, by platform.
- `split` is "yes" when its concerns fall in different areas. Such an entry is under each of them.
- An entry whose concerns are all under none is under none (`area_ids` is empty).
Prints how many entries each area holds, and how many are split or under none.
"""
import csv, os, re, sys
from collections import Counter

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CM = os.path.join(SKM, "studies", "concern-map", "platforms")


def rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def main(platform, d):
    area_of = {}
    order = []
    for r in rows(os.path.join(d, f"areas-{platform}.tsv")):
        order.append(r["area_id"])
        for c in (r.get("concern_ids") or "").split(";"):
            if c.strip():
                area_of[c.strip()] = r["area_id"]
    out, held, split, none = [], Counter(), 0, 0
    for r in rows(os.path.join(CM, platform, "inventory.tsv")):
        if r["out_of_scope_reason"]:
            continue
        cs = [c for c in re.split(r"[;,\s]+", r["concern_ids"] or "") if c]
        areas = []
        for c in cs:
            a = area_of.get(c)
            if a and a not in areas:
                areas.append(a)
        is_split = len(areas) > 1
        split += is_split
        none += not areas
        for a in areas:
            held[a] += 1
        out.append([r["inv_id"], r["list"], r["entry"], ";".join(cs), ";".join(areas), "yes" if is_split else ""])
    path = os.path.join(d, f"areas-{platform}-entries.tsv")
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_NONE, escapechar="\\", lineterminator="\n")
        w.writerow(["inv_id", "list", "entry", "concern_ids", "area_ids", "split"])
        w.writerows(out)
    print(f"{platform}: {len(out)} entries placed; {split} split across areas; {none} under none")
    for a in order:
        print(f"  {a}: {held[a]}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else os.path.join(SKM, "studies", "proposals", "areas"))
