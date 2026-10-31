"""The held pass, Shopify's mobile app (the coordinator's re-plan of 31 October): `mobile-app-navigation` and
`mobile-app-settings-index` are the Shopify mobile app's screens as Android view nodes, dumped screen by screen, so the
same node (the tab bar, a section's row) recurs on each screen that shows it. A node is the same where its entry's text
is the same apart from its parent's index. The script cuts SH-80 to SH-84 again: SH-80, SH-82 and SH-83 hold each node's
first occurrence, for agents, and SH-81 and SH-84 the repeats and the bare layout nodes (no text, description or id),
which the script places once the agents' batches are checked: a repeat takes its first occurrence's lines, a bare layout
node `out`, as the POS batches and the Tinker script placed theirs. A layout node with an id is left to the agents,
since its id can name a screen or a section (the POS batches' containers).

Usage:
  python3 -I method/held_mobile_repeats.py            prints what it would do
  python3 -I method/held_mobile_repeats.py --cut      re-cuts the five batches
  python3 -I method/held_mobile_repeats.py --apply    writes SH-81's and SH-84's lines, once SH-80, SH-82 and SH-83 are placed
  python3 -I method/held_mobile_repeats.py --apply SH-81    writes SH-81's alone, whose repeats' first occurrences are all SH-80's
"""
import csv, collections, glob, os, re, sys

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    sys.exit(__doc__)

H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
BATCHES = ("SH-80", "SH-81", "SH-82", "SH-83", "SH-84")
AGENT_NAV, AGENT_SET, SCRIPT_NAV, SCRIPT_SET = ("SH-80",), ("SH-82", "SH-83"), "SH-81", "SH-84"
csv.field_size_limit(10**9)
E = {}
with open(f"{H}/shopify/entries.tsv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        E[r["entry_id"]] = r
HEAD = open(f"{H}/shopify/placements-SH-1.tsv", encoding="utf-8").readline().rstrip("\n").split("\t")


def key(t):
    return re.sub(r"(?:^|; )parent: \d+", "", t).strip("; ")


def bare(t):
    return not re.search(r"(?:^|; )(?:text|desc|id): \S", t)


order = [x.strip() for b in BATCHES for x in open(f"{H}/batches/{b}.txt") if x.strip()]
assert {E[e]["structure"] for e in order} == {"mobile-app-navigation", "mobile-app-settings-index"}
first, agent, script = {}, [], []
for e in order:
    t = E[e]["text"]
    if bare(t) or key(t) in first:
        script.append(e)
    else:
        first[key(t)] = e
        agent.append(e)
nav = lambda es: [e for e in es if E[e]["structure"] == "mobile-app-navigation"]
sett = lambda es: [e for e in es if E[e]["structure"] == "mobile-app-settings-index"]
half = (len(sett(agent)) + 1) // 2
cut = {"SH-80": nav(agent), "SH-82": sett(agent)[:half], "SH-83": sett(agent)[half:],
       "SH-81": nav(script), "SH-84": sett(script)}
print(f"{len(order)} entries: {len(agent)} first occurrences for agents, {len(script)} for the script "
      f"({sum(1 for e in script if bare(E[e]['text']))} bare layout nodes, the rest repeats)")
print("  " + ", ".join(f"{b} {len(cut[b])}" for b in BATCHES))

if "--cut" in sys.argv:
    for b in BATCHES:
        open(f"{H}/batches/{b}.txt", "w").write("".join(x + "\n" for x in cut[b]))
    rows = open(f"{H}/batches.tsv", encoding="utf-8").read().split("\n")
    for i, l in enumerate(rows):
        f = l.split("\t")
        if f and f[0] in cut:
            f[2], f[3] = str(len(cut[f[0]])), ",".join(dict.fromkeys(E[x]["structure"] for x in cut[f[0]]))
            rows[i] = "\t".join(f)
    open(f"{H}/batches.tsv", "w", encoding="utf-8").write("\n".join(rows))
    print("re-cut the five batches")

if "--apply" in sys.argv:
    lines = collections.defaultdict(list)          # entry -> its placed rows, with batch and line
    for p in sorted(glob.glob(f"{H}/shopify/placements-SH-*.tsv")):
        b = os.path.basename(p)[len("placements-"):-len(".tsv")]
        if b in (SCRIPT_NAV, SCRIPT_SET):
            continue
        L = open(p, encoding="utf-8").read().split("\n")
        hd = L[0].split("\t")
        for n, l in enumerate(L[1:], 2):
            if l.strip():
                r = dict(zip(hd, l.split("\t")))
                for x in r["entry_id"].split(";"):
                    lines[x.strip()].append((b, n, r))
    for b in [a for a in sys.argv[1:] if a in (SCRIPT_NAV, SCRIPT_SET)] or (SCRIPT_NAV, SCRIPT_SET):
        p = f"{H}/shopify/placements-{b}.tsv"
        assert not os.path.exists(p), f"{p} exists: the script writes the batch's lines once"
        out = []
        for e in [x.strip() for x in open(f"{H}/batches/{b}.txt") if x.strip()]:
            t = E[e]["text"]
            if bare(t):
                row = {h: "" for h in HEAD}
                row.update(entry_id=e, placement="out")
                row["reading"] = ("a reading: a layout node of the Shopify mobile app’s screen with no text, description "
                                  "or id, which names nothing (the POS batches’ and the Tinker script’s frame); placed by "
                                  "method/held_mobile_repeats.py")
                out.append(row)
                continue
            f0 = first[key(t)]
            placed = lines.get(f0)
            assert placed, f"{e}: its first occurrence {f0} isn't placed yet"
            for fb, fn, r in placed:
                row = {h: r.get(h, "") for h in HEAD}
                row["entry_id"] = e
                row["reading"] = (f"a reading: the same node of the Shopify mobile app as {f0} ({fb}:{fn}), on another "
                                  f"screen or at another place of the same screen, its parent’s index apart: that entry’s "
                                  f"line; placed by method/held_mobile_repeats.py")
                out.append(row)
        with open(p, "w", encoding="utf-8") as f:
            f.write("\t".join(HEAD) + "\n")
            for r in out:
                assert '"' not in "".join(r.values()), r
                f.write("\t".join(r[h] for h in HEAD) + "\n")
        print(f"wrote {p}: {len(out)} lines")
