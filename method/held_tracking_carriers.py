"""The held pass, Shopify's tracking-carriers (the coordinator's re-plan of 31 October, method report section 18):
the return form's tracking carrier field lists 203 carriers, the platform's value list Tracking carriers that the
cell CM-SHP-017 (shipment tracking: 'the carriers it can name') cites as a whole (SH-I-2095). Each option is a kind of
the list's thing (M-6), so it takes the list's line, CM-SHP-017 `core`, its carrier the filler; the last option,
Other, names none. The script cuts SH-101 and SH-102 again: SH-102 holds every carrier, placed here, and SH-101 the
tinker-tools entries that were beside them, for an agent.

Usage:
  python3 -I method/held_tracking_carriers.py            prints what it would do
  python3 -I method/held_tracking_carriers.py --apply    re-cuts SH-101 and SH-102 and writes SH-102's lines
"""
import csv, re, sys

H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
csv.field_size_limit(10**9)
E = {}
with open(f"{H}/shopify/entries.tsv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        E[r["entry_id"]] = r
HEAD = open(f"{H}/shopify/placements-SH-1.tsv", encoding="utf-8").readline().rstrip("\n").split("\t")

ids = [x.strip() for b in ("SH-101", "SH-102") for x in open(f"{H}/batches/{b}.txt") if x.strip()]
carriers = [e for e in ids if E[e]["structure"] == "tracking-carriers"]
others = [e for e in ids if E[e]["structure"] != "tracking-carriers"]
out = []
for e in carriers:
    m = re.search(r"label: ([^;]+); value: ([^;]+)", E[e]["text"])
    label, value = m.group(1).strip(), m.group(2).strip()
    row = {h: "" for h in HEAD}
    row.update(entry_id=e, placement="capability", cap_id="CM-SHP-017", supports="core", terms=label)
    if value == "Other":
        row["reading"] = ("a reading: the last option of the return form's tracking carrier field (capture-plus's return "
                          "form), Other, for a carrier the platform's list doesn't name: an option of the value list "
                          "Tracking carriers, which CM-SHP-017's cell cites as a whole (SH-I-2095), so the list's line (M-6)")
    else:
        row["filler"] = label
        row["reading"] = (f"a reading: an option of the return form's tracking carrier field (capture-plus's return form), "
                          f"{label} ({value}): a carrier the platform's tracking can name, an option of the value list "
                          f"Tracking carriers, which CM-SHP-017's cell cites as a whole (SH-I-2095), so the list's line "
                          f"(M-6), the carrier its filler; placed by method/held_tracking_carriers.py")
    out.append(row)

print(f"{len(carriers)} carriers take CM-SHP-017's line; {len(others)} other entries stay for an agent (SH-101)")
if "--apply" in sys.argv:
    open(f"{H}/batches/SH-101.txt", "w").write("".join(x + "\n" for x in others))
    open(f"{H}/batches/SH-102.txt", "w").write("".join(x + "\n" for x in carriers))
    rows = open(f"{H}/batches.tsv", encoding="utf-8").read().split("\n")
    for i, l in enumerate(rows):
        f = l.split("\t")
        if f and f[0] == "SH-101":
            f[2], f[3] = str(len(others)), ",".join(dict.fromkeys(E[x]["structure"] for x in others)); rows[i] = "\t".join(f)
        elif f and f[0] == "SH-102":
            f[2], f[3] = str(len(carriers)), "tracking-carriers"; rows[i] = "\t".join(f)
    open(f"{H}/batches.tsv", "w", encoding="utf-8").write("\n".join(rows))
    with open(f"{H}/shopify/placements-SH-102.tsv", "w", encoding="utf-8") as f:
        f.write("\t".join(HEAD) + "\n")
        for r in out:
            f.write("\t".join(r[h] for h in HEAD) + "\n")
    print("re-cut: SH-101 %d, SH-102 %d; wrote placements-SH-102.tsv" % (len(others), len(carriers)))
