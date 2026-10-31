"""The held pass, Shopify's dev-dashboard-scopes (the coordinator's re-plan of 31 October): the Dev Dashboard's scope
picker lists each resource as a heading, then under it the API that grants the resource's scopes ('Admin API; parent:
<heading>'). SH-23's R23.10 places such a label on its heading's capability alone, with the heading's support (E157), and
all 38 of SH-23's labels take exactly their heading's lines. The script cuts SH-24 again: SH-24 keeps the headings and
the picker's other entries, for an agent, and the new batch SH-104 the API labels whose heading is a held entry, which the
script places once SH-24 is checked: each label takes its heading's lines, the API its term.

Usage:
  python3 -I method/held_scope_apis.py            prints what it would do
  python3 -I method/held_scope_apis.py --cut      re-cuts SH-24 and writes SH-104
  python3 -I method/held_scope_apis.py --apply    writes SH-104's lines, once SH-24 is placed
"""
import csv, collections, glob, os, re, sys

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    sys.exit(__doc__)

H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
AGENT, SCRIPT = "SH-24", "SH-104"
csv.field_size_limit(10**9)
E = {}
with open(f"{H}/shopify/entries.tsv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        E[r["entry_id"]] = r
HEAD = open(f"{H}/shopify/placements-SH-1.tsv", encoding="utf-8").readline().rstrip("\n").split("\t")
LABEL = re.compile(r"kind: text; text: ([\w ]+ API); parent: (.*)$")

heads = {}                                          # a heading's name -> its entry, in SH-23 and SH-24
for b in ("SH-23", AGENT, SCRIPT):
    p = f"{H}/batches/{b}.txt"
    for e in [x.strip() for x in open(p) if x.strip()] if os.path.exists(p) else []:
        m = re.match(r"kind: text; text: (.*)$", E[e]["text"])
        if m and E[e]["structure"] == "dev-dashboard-scopes" and not LABEL.match(E[e]["text"]):
            heads[m.group(1).strip()] = e

if os.path.exists(f"{H}/batches/{SCRIPT}.txt"):
    agent = [x.strip() for x in open(f"{H}/batches/{AGENT}.txt") if x.strip()]
    script = [x.strip() for x in open(f"{H}/batches/{SCRIPT}.txt") if x.strip()]
else:
    ids = [x.strip() for x in open(f"{H}/batches/{AGENT}.txt") if x.strip()]
    script = [e for e in ids if LABEL.match(E[e]["text"]) and LABEL.match(E[e]["text"]).group(2).strip() in heads]
    agent = [e for e in ids if e not in script]
print(f"{AGENT} {len(agent)} entries for an agent; {SCRIPT} {len(script)} API labels for the script")

if "--cut" in sys.argv:
    assert not os.path.exists(f"{H}/batches/{SCRIPT}.txt"), f"{SCRIPT} exists: the cut is made once"
    open(f"{H}/batches/{AGENT}.txt", "w").write("".join(x + "\n" for x in agent))
    open(f"{H}/batches/{SCRIPT}.txt", "w").write("".join(x + "\n" for x in script))
    rows = open(f"{H}/batches.tsv", encoding="utf-8").read().split("\n")
    for i, l in enumerate(rows):
        f = l.split("\t")
        if f and f[0] == AGENT:
            f[2] = str(len(agent)); rows[i] = "\t".join(f)
            rows.insert(i + 1, "\t".join([SCRIPT, "shopify", str(len(script)), "dev-dashboard-scopes"]))
            break
    open(f"{H}/batches.tsv", "w", encoding="utf-8").write("\n".join(rows))
    print(f"re-cut {AGENT} and wrote {SCRIPT}")

if "--apply" in sys.argv:
    p = f"{H}/shopify/placements-{SCRIPT}.tsv"
    assert not os.path.exists(p), f"{p} exists: the script writes the batch's lines once"
    lines = collections.defaultdict(list)           # entry -> its placed rows, with batch and line
    for q in sorted(glob.glob(f"{H}/shopify/placements-SH-*.tsv")):
        b = os.path.basename(q)[len("placements-"):-len(".tsv")]
        L = open(q, encoding="utf-8").read().split("\n")
        hd = L[0].split("\t")
        for n, l in enumerate(L[1:], 2):
            if l.strip():
                r = dict(zip(hd, l.split("\t")))
                for x in r["entry_id"].split(";"):
                    lines[x.strip()].append((b, n, r))
    out = []
    for e in script:
        api, head = (s.strip() for s in LABEL.match(E[e]["text"]).groups())
        h = heads[head]
        assert lines.get(h), f"{e}: its heading {h} ('{head}') isn't placed yet"
        for b, n, r in lines[h]:
            row = {k: "" for k in HEAD}
            row.update(entry_id=e, placement=r["placement"], cap_id=r["cap_id"], supports=r["supports"],
                       scope=r["scope"], terms=api if r["placement"] != "out" else "")
            row["reading"] = (f"a reading: the API the picker lists under '{head}', {api}: apps reach that resource’s "
                              f"scopes through the {api}, so its heading’s line ({b}:{n}, its entry {h}), the same "
                              f"capability and support (SH-23’s R23.10; E157); placed by method/held_scope_apis.py")
            out.append(row)
    with open(p, "w", encoding="utf-8") as f:
        f.write("\t".join(HEAD) + "\n")
        for r in out:
            assert '"' not in "".join(r.values()), r
            f.write("\t".join(r[k] for k in HEAD) + "\n")
    print(f"wrote {p}: {len(out)} lines")
