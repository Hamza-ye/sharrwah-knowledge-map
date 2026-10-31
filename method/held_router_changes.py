"""The held pass, Shopify's admin-router-changes (the coordinator's re-plan of 31 October): each change between two of
the router's versions names a route. Where the route is a held entry the router batches placed, and the change leaves
its eligibility the same, the change takes the route's own lines: the same capability, support and scope, the route's id
its term. A removed route takes them as `shows`, no longer served. Every other change (a route the concern map read, an
eligibility that differs, a route added) is left for an agent, in the same batch.

Usage:
  python3 -I method/held_router_changes.py            prints what it would place and leave
  python3 -I method/held_router_changes.py --apply    writes SH-19's lines for the changes it places
"""
import csv, collections, glob, os, re, sys

H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
BATCH = "SH-19"
csv.field_size_limit(10**9)
E = {}
with open(f"{H}/shopify/entries.tsv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        E[r["entry_id"]] = r
route = {}                                     # route id -> its admin-router entry
for e, r in E.items():
    if r["structure"] == "admin-router":
        m = re.match(r"id: ([^;]+)", r["text"])
        if m:
            route[m.group(1).strip()] = e
HEAD, lines = None, collections.defaultdict(list)   # entry -> its placed rows, with batch and line
for p in sorted(glob.glob(f"{H}/shopify/placements-SH-*.tsv")):
    b = os.path.basename(p)[len("placements-"):-len(".tsv")]
    if b == BATCH:
        continue
    L = open(p, encoding="utf-8").read().split("\n")
    HEAD = L[0].split("\t")
    for n, l in enumerate(L[1:], 2):
        if l.strip():
            r = dict(zip(HEAD, l.split("\t")))
            for x in r["entry_id"].split(";"):
                lines[x.strip()].append((b, n, r))

out, left = [], []
for e in [x.strip() for x in open(f"{H}/batches/{BATCH}.txt") if x.strip()]:
    t = E[e]["text"]
    m = re.match(r"id: ([^;]+); change: (\w+); eligibility before: (.*?); eligibility after: (.*)$", t)
    rid, kind, before, after = m.group(1).strip(), m.group(2), m.group(3).strip(), m.group(4).strip()
    placed = [x for x in lines.get(route.get(rid, ""), []) if x[2]["placement"] == "capability"]
    if kind not in ("changed", "removed") or before != after or not placed:
        left.append(e)
        continue
    seen = set()
    for b, n, r in placed:
        if (r["cap_id"], r["scope"]) in seen:
            continue
        seen.add((r["cap_id"], r["scope"]))
        row = {h: "" for h in HEAD}
        sup = "shows" if kind == "removed" else r["supports"]
        row.update(entry_id=e, placement="capability", cap_id=r["cap_id"], supports=sup, scope=r["scope"], terms=rid)
        row["reading"] = (f"a reading: the router's change of route {rid} between its two versions ('change: {kind}'), "
                          f"its eligibility the same before and after: the route's own line ({b}:{n}, its entry "
                          f"{route[rid]}), {r['cap_id']} {r['supports']}"
                          + (", as shows, since the newer version no longer serves the route" if kind == "removed" else "")
                          + "; placed by method/held_router_changes.py")
        out.append(row)

print(f"{len(out)} lines for {len({r['entry_id'] for r in out})} changes; {len(left)} changes left for an agent")
if "--apply" in sys.argv:
    p = f"{H}/shopify/placements-{BATCH}.tsv"
    assert not os.path.exists(p), f"{p} exists: the script writes the batch's first lines only"
    with open(p, "w", encoding="utf-8") as f:
        f.write("\t".join(HEAD) + "\n")
        for r in out:
            assert '"' not in "".join(r.values())
            f.write("\t".join(r[h] for h in HEAD) + "\n")
    print(f"wrote {p}; left: " + " ".join(left))
