"""The held pass, Shopify's tinker-tools (the coordinator's re-plan of 31 October): the Tinker app's home screen, its
tool catalog as Android view nodes. Tinker by Shopify is the new thing SH-95 named, `own-service` on its store listing's
developer, Shopify Inc. (SH-E-e95ada94). Its tools are AI tools outside the admin, which go on their place's thing (the
corrections with the Editions digest), so each tool card ('desc: <tool>, <what it does>') and the label that repeats its
name take Tinker's line, the tool's name the term. The screen's own frame (layout nodes, empty labels, its headings
and its input's placeholder) is `out`. The script cuts SH-100 and SH-101 again: SH-101 holds every tinker-tools entry,
placed here, and SH-100 the other structures' entries that were beside them, for an agent.

Usage:
  python3 -I method/held_tinker_tools.py            prints what it would do
  python3 -I method/held_tinker_tools.py --apply    re-cuts SH-100 and SH-101 and writes SH-101's lines
"""
import csv, re, sys

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    sys.exit(__doc__)

H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
csv.field_size_limit(10**9)
E = {}
with open(f"{H}/shopify/entries.tsv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        E[r["entry_id"]] = r
HEAD = open(f"{H}/shopify/placements-SH-1.tsv", encoding="utf-8").readline().rstrip("\n").split("\t")
TINKER = ("Tinker by Shopify, the new thing SH-95 named, own-service on its store listing's developer, Shopify Inc. "
          "(SH-E-e95ada94); an AI tool outside the admin goes on its place's thing (the corrections with the Editions "
          "digest); the new thing's support is decided with it")

ids = [x.strip() for b in ("SH-100", "SH-101") for x in open(f"{H}/batches/{b}.txt") if x.strip()]
tools = [e for e in ids if E[e]["structure"] == "tinker-tools"]
others = [e for e in ids if E[e]["structure"] != "tinker-tools"]
names = {}
for e in tools:
    m = re.search(r"(?:^|; )desc: ([^,;]+), ([^;]+)", E[e]["text"])
    if m:
        names[m.group(1).strip()] = m.group(2).strip()
out = []
for e in tools:
    t = E[e]["text"]
    row = {h: "" for h in HEAD}
    row["entry_id"] = e
    d = re.search(r"(?:^|; )desc: ([^,;]+), ([^;]+)", t)
    lab = re.search(r"(?:^|; )text: ([^;]+)$", t)
    if d:
        row.update(placement="new", cap_id="new:Tinker by Shopify", supports="own-service", terms=d.group(1).strip())
        row["reading"] = (f"a reading: a tool card on the Tinker app's home screen, '{d.group(1).strip()}', "
                          f"'{d.group(2).strip()}': a tool of {TINKER}; placed by method/held_tinker_tools.py")
    elif lab and lab.group(1).strip() in names:
        n = lab.group(1).strip()
        row.update(placement="new", cap_id="new:Tinker by Shopify", supports="own-service", terms=n)
        row["reading"] = (f"a reading: the label '{n}' of its tool card on the Tinker app's home screen "
                          f"('{names[n]}'): a tool of {TINKER}; placed by method/held_tinker_tools.py")
    else:
        row["placement"] = "out"
        row["reading"] = ("a reading: the Tinker app's home screen's own frame (a layout node, an empty label, a "
                          "heading of its catalog or its input's placeholder), which names no tool; placed by "
                          "method/held_tinker_tools.py")
    assert '"' not in "".join(row.values()), row
    out.append(row)

n_tool = sum(1 for r in out if r["placement"] == "new")
print(f"{len(tools)} tinker-tools entries: {n_tool} on Tinker's tools, {len(tools) - n_tool} out; "
      f"{len(others)} other entries stay for an agent (SH-100)")
if "--apply" in sys.argv:
    open(f"{H}/batches/SH-100.txt", "w").write("".join(x + "\n" for x in others))
    open(f"{H}/batches/SH-101.txt", "w").write("".join(x + "\n" for x in tools))
    rows = open(f"{H}/batches.tsv", encoding="utf-8").read().split("\n")
    for i, l in enumerate(rows):
        f = l.split("\t")
        if f and f[0] == "SH-100":
            f[2], f[3] = str(len(others)), ",".join(dict.fromkeys(E[x]["structure"] for x in others)); rows[i] = "\t".join(f)
        elif f and f[0] == "SH-101":
            f[2], f[3] = str(len(tools)), "tinker-tools"; rows[i] = "\t".join(f)
    open(f"{H}/batches.tsv", "w", encoding="utf-8").write("\n".join(rows))
    with open(f"{H}/shopify/placements-SH-101.tsv", "w", encoding="utf-8") as f:
        f.write("\t".join(HEAD) + "\n")
        for r in out:
            f.write("\t".join(r[h] for h in HEAD) + "\n")
    print("re-cut: SH-100 %d, SH-101 %d; wrote placements-SH-101.tsv" % (len(others), len(tools)))
