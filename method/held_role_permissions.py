"""The held pass, Shopify's admin-role-permissions (after SH-4): each role permission whose handle is a permission the
permission tree holds, and SH-3 or SH-4 placed, takes that permission's line or lines, with the same capability
and support; the tree's scope and filler are named in `reading`, since the role's answer states no condition; its access level (ALLOW, DENY) is the role's own setting, in `reading`. A handle the tree
holds more than once with lines that differ, or holds not at all, is left to an agent's batch.

Usage:
  python3 -I method/held_role_permissions.py             prints what it would do: matched and left, by batch
  python3 -I method/held_role_permissions.py --apply     re-cuts SH-5 to SH-7 (SH-5 the matched entries, SH-6 and
                                                         SH-7 the rest, in their order) and writes SH-5's lines
"""
import csv, re, collections, sys

H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
BATCHES = ("SH-5", "SH-6", "SH-7")
csv.field_size_limit(10**9)

E = {}
with open(f"{H}/shopify/entries.tsv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        E[r["entry_id"]] = r

tree = collections.defaultdict(list)                      # permission id -> the tree's entries for it
for e, r in E.items():
    if r["structure"] == "admin-permission-tree":
        m = re.search(r"(?:^|; )id: ([A-Z0-9_]+)", r["text"])
        if m:
            tree[m.group(1)].append(e)

HEAD, lines = None, collections.defaultdict(list)          # tree entry -> its placed rows, with batch and line
for b in ("SH-3", "SH-4"):
    L = open(f"{H}/shopify/placements-{b}.tsv", encoding="utf-8").read().split("\n")
    HEAD = L[0].split("\t")
    for n, l in enumerate(L[1:], 2):
        if l.strip():
            r = dict(zip(HEAD, l.split("\t")))
            for x in r["entry_id"].split(";"):
                lines[x.strip()].append((b, n, r))


def title(e):
    """The tree entry's title, or its member's name where the code computes the title (a plan's two titles)."""
    m = re.search(r"(?:^|; )title: ([^;]+)", E[e]["text"]) or re.search(r"(?:^|; )member: ([^;]+)", E[e]["text"])
    return m.group(1).strip() if m else "untitled"


ids = [x.strip() for b in BATCHES for x in open(f"{H}/batches/{b}.txt") if x.strip()]
matched, left, out = [], [], []
for e in ids:
    m = re.search(r"handle: ([A-Z0-9_]+); accessLevel: (\w+)", E[e]["text"])
    if not m:
        left.append(e); continue
    handle, level = m.group(1), m.group(2)
    placed = [t for t in tree.get(handle, []) if lines.get(t)]
    sets = {tuple((r["cap_id"], r["supports"], r["scope"], r["filler"]) for _, _, r in lines[t]) for t in placed}
    if len(sets) != 1:
        left.append(e); continue
    t = placed[0]
    matched.append(e)
    # the tree's rows by capability and support: with no scope, two rows the tree scopes apart (a title the code
    # computes by plan, 'shopifyPlus' and 'not shopifyPlus') are one line, both scopes named in the reading
    groups = collections.OrderedDict()
    for b, n, r in lines[t]:
        groups.setdefault((r["cap_id"], r["supports"]), []).append((b, n, r))
    for (cap, sup), grp in groups.items():
        b, n, r = grp[0]
        scopes = [x["scope"] for _, _, x in grp if x["scope"]]
        r = dict(r, scope=" or ".join(scopes))
        n = ",".join(str(m) for _, m, _ in grp)
        row = {h: "" for h in HEAD}
        # the entry's own words are its handle and level: its terms are the handle, and the tree's titles and
        # fillers stay with the tree's line, which the reading cites
        # and no scope: the role's answer states none, so the tree's condition is named in the reading (SH-6's R6)
        row.update(entry_id=e, placement="capability", cap_id=r["cap_id"], supports=r["supports"], scope="",
                   terms=handle)
        row["reading"] = (f"a reading: the role's permission {handle}, access level {level}, the role's own setting "
                          f"(store ctcbwa-r1); the same permission's line in the permission tree ({b}:{n}, its entry "
                          f"{t}, titled {title(t)}{', filler ' + r['filler'] if r['filler'] else ''}"
                          f"{', its scope there ' + r['scope'] if r['scope'] else ''}), by the rule after "
                          f"SH-4: a role's permission takes its permission's line")
        out.append(row)

print(f"{len(ids)} role permissions: {len(matched)} take their permission's line ({len(out)} lines), {len(left)} are left")
if "--apply" in sys.argv:
    half = (len(left) + 1) // 2      # it reads all three batches, so a second run makes the same cut
    cut = {"SH-5": matched, "SH-6": left[:half], "SH-7": left[half:]}
    for b, es in cut.items():
        open(f"{H}/batches/{b}.txt", "w").write("".join(x + "\n" for x in es))
    rows = open(f"{H}/batches.tsv", encoding="utf-8").read().split("\n")
    for i, l in enumerate(rows):
        f = l.split("\t")
        if f and f[0] in cut:
            f[2] = str(len(cut[f[0]])); rows[i] = "\t".join(f)
    open(f"{H}/batches.tsv", "w", encoding="utf-8").write("\n".join(rows))
    with open(f"{H}/shopify/placements-SH-5.tsv", "w", encoding="utf-8") as f:
        f.write("\t".join(HEAD) + "\n")
        for r in out:
            f.write("\t".join(r[h] for h in HEAD) + "\n")
    print("re-cut: " + ", ".join(f"{b} {len(es)}" for b, es in cut.items()) + "; wrote placements-SH-5.tsv")
