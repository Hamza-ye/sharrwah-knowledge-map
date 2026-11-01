"""The accuracy probe of the class's model (the founder's go, 1 November 2026): how often the model's readings are wrong.

    python3 -I studies/class-model/probe/probe.py sample     # writes sample.tsv, items-<k>.tsv and claims-<k>.tsv
    python3 -I studies/class-model/probe/probe.py rates      # reads verdicts-<k>.tsv and prints the counts

Two samples, drawn by seed so that anyone can draw them again:
- cells: 100 of the cells that hold a placement (not 'none-held', not 'not-stated'), at random. Each is checked on its
  strongest placement, against up to three of its lines that give that placement, drawn at random;
- rulings: for each high-weight ruling of reports/GM-rulings.md (from the held pass on) whose readings name 100 or more
  held lines, five of those lines at random (review_select.py's own matching).
Items go to four checkers at random. A checker's items file gives the capability and the sources only; the claims file
gives what the model says, to be opened only after the checker has written its own reading.
"""
import csv, glob, json, os, random, re, subprocess, sys, tempfile, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "method"))
import review_select as RS
csv.field_size_limit(10**9)
SEED, CHECKERS, ORDER = 20261101, 4, ["core", "own-service", "extension-point", "outside", "shows"]


def tsv(path):
    return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))


def write(path, head, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_NONE, escapechar="\\", lineterminator="\n")
        w.writerow(head)
        for r in rows:
            w.writerow([" ".join(str(x).split()) for x in r])


def page_data():
    """The evidence rows and their sources, as the Knowledge Map's page resolves them (km_page.py)."""
    d = tempfile.mkdtemp()
    subprocess.run([sys.executable, "-I", os.path.join(ROOT, "method", "km_page.py"), "--split", "--out", os.path.join(d, "p.html")],
                   check=True, capture_output=True)
    ev, ci = {}, {}
    for f in sorted(glob.glob(os.path.join(d, "p-ev-*.json"))):
        ev.update(json.load(open(f, encoding="utf-8")))
    for f in sorted(glob.glob(os.path.join(d, "p-cites-*.json"))):
        ci.update(json.load(open(f, encoding="utf-8")))
    return ev, ci


def sample():
    rnd = random.Random(SEED)
    M = os.path.join(ROOT, "studies", "class-model", "merged")
    caps = {r["cap_id"]: r for r in tsv(os.path.join(M, "capabilities.tsv"))}
    plats = RS.PLATFORMS
    ev, ci = page_data()
    src = lambda cid: ci.get(cid) or ["(no source resolved)", "", "", ""]
    items, claims = [], []
    # cells
    cells = [c for c in tsv(os.path.join(M, "cells.tsv")) if c["held"] == "statements" and c["placed_as"] not in ("", "not-stated")]
    for c in sorted(rnd.sample(cells, 100), key=lambda c: (c["cap_id"], c["platform"])):
        pl = [p for p in ORDER if p in c["placed_as"].split(";")]
        top = pl[0] if pl else ""
        i = plats.index(c["platform"])
        lines = [e for e in ev.get(c["cap_id"], []) if e[0] == i and e[1] == top]
        pick = rnd.sample(lines, min(3, len(lines)))
        iid = f"C-{c['cap_id']}-{c['platform']}"
        cap = caps.get(c["cap_id"], {})
        items.append([iid, "cell", c["cap_id"], cap.get("capability", ""), cap.get("note", ""), c["platform"],
                      " || ".join(f"[{n+1}] {src(e[4])[0]} | {src(e[4])[1]} | quote: {src(e[4])[2]} | read {src(e[4])[3]}" for n, e in enumerate(pick)) or "(no line gives this placement)"])
        claims.append([iid, f"cell placed as {c['placed_as']}; strongest: {top}; scopes: {c['scopes']}",
                       " || ".join(f"[{n+1}] supports {e[1]}: {e[3]}" for n, e in enumerate(pick)), c["reading"]])
    # rulings
    new_rows = {}
    for l in open(RS.GM, encoding="utf-8").read().split("\n"):
        m = re.match(r"^\| (N\d\d) \|.*\bnew, (CM-[A-Z0-9]{3}-\d{3})", l)
        if m:
            new_rows[m.group(1)] = m.group(2)
    lines, _ = RS.held_lines()
    structures = {r["batch"]: r.get("structures", "") for r in tsv(os.path.join(RS.HELD, "batches.tsv"))}
    key_cite = {}
    for cap_id, rows in ev.items():
        for e in rows:
            key_cite.setdefault(e[2], e[4])
    rulings, _ = RS.gm_rulings(RS.GM)
    table = []
    for r in rulings:
        pat = RS.ruling_pattern(r, new_rows)
        if not pat or pat == "new-caps":
            mine = [L for L in lines if L["placement"] == "new"] if pat == "new-caps" else []
        elif pat.startswith("cap:"):
            mine = [L for L in lines if L.get("cap_id") == pat[4:]]
        else:
            rx = re.compile(pat, re.I)
            mine = [L for L in lines if rx.search(L.get("reading", ""))]
        only = RS.ruling_batches(r, structures)
        if only is not None:
            mine = [L for L in mine if L["_batch"] in only]
        table.append((r["title"], pat, len(mine)))
        if len(mine) < 100:
            continue
        for k, L in enumerate(rnd.sample(mine, 5)):
            iid = f"R-{len([t for t in table if t[2] >= 100])}-{k+1}"
            cap = caps.get(L.get("cap_id", ""), {})
            s = src(key_cite.get(L["entry_id"], ""))
            items.append([iid, "ruling line", L.get("cap_id", ""), cap.get("capability", ""), cap.get("note", ""), L["_platform"],
                          f"[1] {s[0]} | {s[1]} | quote: {s[2]} | read {s[3]} (held entry {L['entry_id']})"])
            claims.append([iid, f"line placed as {L['placement']} on {L.get('cap_id', '')}, supports {L.get('supports', '')}; scope: {L.get('scope', '')}; terms: {L.get('terms', '')}",
                           f"{L['_file']} line {L['_line']}", L.get("reading", "")])
    order = list(range(len(items)))
    rnd.shuffle(order)
    write(os.path.join(HERE, "rulings.tsv"), ["ruling", "pattern", "held_lines"], table)
    write(os.path.join(HERE, "sample.tsv"), ["item", "kind", "cap_id", "capability", "note", "platform", "sources", "checker"],
          [items[i] + [str(n % CHECKERS + 1)] for n, i in enumerate(order)])
    for k in range(1, CHECKERS + 1):
        mine = [i for n, i in enumerate(order) if n % CHECKERS + 1 == k]
        write(os.path.join(HERE, f"items-{k}.tsv"), ["item", "kind", "cap_id", "capability", "note", "platform", "sources"], [items[i] for i in mine])
        write(os.path.join(HERE, f"claims-{k}.tsv"), ["item", "claim", "lines", "reading"], [claims[i] for i in mine])
    print(f"{sum(1 for i in items if i[1] == 'cell')} cells and {sum(1 for i in items if i[1] != 'cell')} ruling lines, "
          f"from {sum(1 for t in table if t[2] >= 100)} rulings with 100 or more held lines (of {len(table)} high-weight rulings), seed {SEED}")


if __name__ == "__main__":
    {"sample": sample}.get((sys.argv[1:] or ["sample"])[0], sample)()
