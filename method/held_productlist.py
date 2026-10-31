"""The held pass, Shopify Editions: SH-52 by SH-51's rule E18: each of Winter '23's Product list entries takes its solution item's first line, the item
found by its collection and its order; terms the heading's own words. Collections whose counts differ are left."""
import csv, re, collections, sys
H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
by = {}
with open(f"{H}/shopify/entries.tsv", newline="") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        if r["structure"] == "editions-page-data": by[r["entry_id"]] = r
SOL = re.compile(r"/winter2023/content/solutions/(\d+)/collections/(\d+)/collectionSections/(\d+)/items/(\d+)$")
PL = re.compile(r"/winter2023/content/productList/solutions/(\d+)/collections/(\d+)/products/(\d+)$")
items, prods = collections.defaultdict(list), collections.defaultdict(list)
for e, r in by.items():
    m = SOL.search(r["locator"]); n = PL.search(r["locator"])
    if m: items[(int(m[1]), int(m[2]))].append(((int(m[3]), int(m[4])), e))
    if n: prods[(int(n[1]), int(n[2]))].append((int(n[3]), e))
for k in items: items[k].sort()
for k in prods: prods[k].sort()
lines = collections.defaultdict(list)
HEAD = None
for b in ("SH-50", "SH-51"):
    L = open(f"{H}/shopify/placements-{b}.tsv", encoding="utf-8").read().split("\n"); HEAD = L[0].split("\t")
    for l in L[1:]:
        if not l: continue
        r = dict(zip(HEAD, l.split("\t")))
        for x in r["entry_id"].split(";"): lines[x.strip()].append(r)
batch = [l.strip() for l in open(f"{H}/batches/SH-52.txt") if l.strip()]
out, left = [], []
for e in batch:
    n = PL.search(by[e]["locator"])
    key = (int(n[1]), int(n[2])); k = int(n[3])
    if len(items[key]) != len(prods[key]) or k >= len(items[key]):
        left.append((e, "counts differ" if len(items[key]) != len(prods[key]) else "past the items")); continue
    item = items[key][k][1]
    if not lines.get(item):
        left.append((e, f"item {item} has no line")); continue
    first = lines[item][0]
    head = re.search(r"; heading: ([^;]+)", by[e]["text"]).group(1).strip()
    coll = by[e]["text"].split(";")[0].split(" > ")[-1].strip()
    ihead = re.search(r"heading: ([^;}]+)", by[item]["text"])
    row = {h: "" for h in HEAD}
    row.update(entry_id=e, placement=first["placement"], cap_id=first["cap_id"], supports=first["supports"], scope=first["scope"],
               terms=head if first["placement"] != "out" else "",
               reading=(f"a reading: Winter ’23’s Product list heading “{head}” in its collection “{coll}”, the solution item {item}"
                        + (f" (“{ihead.group(1).strip()}”)" if ihead else "") +
                        f" by its collection and order (SH-51’s E18), whose first line it takes, {first['cap_id'] or 'out'} {first['supports']}; placed by the coordinator, by script"))
    assert '"' not in "".join(row.values()), row
    out.append("\t".join(row[h] for h in HEAD))
print("placed", len(out), "of", len(batch), "| left:", left[:5])
if "--write" in sys.argv:
    open(f"{H}/shopify/placements-SH-52.tsv", "w", encoding="utf-8").write("\t".join(HEAD) + "\n" + "\n".join(out) + "\n")
