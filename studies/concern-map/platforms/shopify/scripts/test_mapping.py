# Map every inventory row and report gaps. Run: python3 -I test_mapping.py
import csv, os, collections
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(D)
ns = {}; exec(open(os.path.join(D, "concerns_def.py")).read(), ns)
ms = {}; exec(open(os.path.join(D, "mapping_def.py")).read(), ms)
keys = [c["key"] for c in ns["C"]]
assert len(keys) == len(set(keys)), "duplicate concern keys"
rows = list(csv.DictReader(open(os.path.join(OUT, "work/inventory_raw.tsv"), encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
per = collections.Counter(); unm = []; badkey = set(); oos = collections.Counter()
for r in rows:
    ks, reason = ms["map_row"](r["list"], r["entry"], r["group"], r["extra"])
    for k in ks:
        if k not in keys: badkey.add(k)
        per[k] += 1
    if not ks and not reason: unm.append(r)
    if reason: oos[r["list"]] += 1
print("rows", len(rows), "unmapped", len(unm), "out-of-scope", sum(oos.values()), dict(oos))
print("bad keys", badkey)
for r in unm: print("UNMAPPED", r["list"], "|", r["entry"], "|", r["group"], "|", r["extra"])
zero = [k for k in keys if per[k] == 0]
print("concerns with no inventory entry:", zero)
