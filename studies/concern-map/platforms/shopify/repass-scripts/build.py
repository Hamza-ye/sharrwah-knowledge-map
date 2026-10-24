# Assembles final/: inventory, concerns, citations, statements, gaps, not-reached, review-log, placements (record), notes.
# Usage: python3 -I scripts/build.py
import sys, os, glob, collections, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
FINAL = os.path.join(BASE, "final")
os.makedirs(FINAL, exist_ok=True)

# ---------- inventory ----------
INV_COLS = ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"]
inv = rd(os.path.join(FIRST, "inventory.tsv")) + rd(os.path.join(WORK, "inventory-new.tsv"))
wr(os.path.join(FINAL, "inventory.tsv"), INV_COLS, inv)

# ---------- concerns (first run's, with the new inventory entries appended, and the new concerns) ----------
CON_COLS = ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"]
con = rd(os.path.join(FIRST, "concerns.tsv"))
newc = rd(os.path.join(WORK, "new-concerns.tsv"))
by_con = collections.defaultdict(list)
for r in rd(os.path.join(WORK, "inventory-new.tsv")):
    for c in ids(r["concern_ids"]):
        by_con[c].append(r["inv_id"])
for r in con:
    extra = [i for i in by_con.get(r["concern_id"], []) if i not in ids(r["inv_ids"])]
    if extra:
        r["inv_ids"] = ";".join(ids(r["inv_ids"]) + extra)
for r in newc:
    r["inv_ids"] = ";".join(dict.fromkeys(ids(r["inv_ids"]) + by_con.get(r["concern_id"], [])))
con_all = con + newc
wr(os.path.join(FINAL, "concerns.tsv"), CON_COLS, con_all)

# ---------- citations ----------
cit = rd(os.path.join(FIRST, "citations.tsv")) + rd(os.path.join(BASE, "citations-new.tsv")) + rd(os.path.join(WORK, "cites-added.tsv"))
seen = collections.Counter(r["cite_id"] for r in cit)
dups = [k for k, v in seen.items() if v > 1]
assert not dups, dups[:5]
wr(os.path.join(FINAL, "citations.tsv"), CCOLS, cit)
cit_by = {r["cite_id"]: r for r in cit}

# ---------- statements ----------
st = rd(os.path.join(WORK, "reviewed-statements.tsv"))
for f in sorted(glob.glob(os.path.join(WORK, "added", "*.tsv"))):
    st += rd(f)
out, keys, problems = [], set(), []
for r in st:
    cs = ids(r["cite_ids"])
    k = (r["concern_id"], r["placement"], cs[0], r["statement"])
    if k in keys:
        continue
    keys.add(k)
    for c in cs:
        assert c in cit_by, (c, r["concern_id"])
    res, why = check_quote(r["statement"], cit_by[cs[0]]["source"])
    if not res.startswith("found"):
        problems.append((r["concern_id"], r["placement"], cs[0], res, why, r["statement"][:100]))
    out.append({k2: r.get(k2, "") for k2 in SCOLS})
wr(os.path.join(FINAL, "statements.tsv"), SCOLS, out)

# ---------- gaps ----------
GAP_COLS = ["concern_id", "placement", "what_would_show_it", "means", "who_can", "route", "why_not_held", "gap_kind"]
gaps = rd(os.path.join(WORK, "gaps.tsv"))
wr(os.path.join(FINAL, "gaps.tsv"), GAP_COLS, gaps)

# ---------- not reached ----------
NR_COLS = ["url", "status", "needed_for", "what_to_look_for"]
nr = rd(os.path.join(FIRST, "not-reached.tsv"))
extra_nr = os.path.join(WORK, "not-reached-new.tsv")
if os.path.exists(extra_nr):
    nr += rd(extra_nr)
wr(os.path.join(FINAL, "not-reached.tsv"), NR_COLS, nr)

# ---------- review log ----------
LOG_COLS = ["concern_id", "placement", "statement", "cite_ids", "action", "reason"]
wr(os.path.join(FINAL, "review-log.tsv"), LOG_COLS, rd(os.path.join(WORK, "review-log.tsv")))

# ---------- placements.tsv: the first run's record, plus "not shown" rows for the new concerns ----------
PL_COLS = ["concern_id", "placement", "value", "status", "cite_ids", "note"]
pl = rd(os.path.join(FIRST, "placements.tsv"))   # the first run's record, unchanged
wr(os.path.join(FINAL, "placements.tsv"), PL_COLS, pl)

# ---------- summary ----------
cover = collections.defaultdict(lambda: [0, 0])
for r in out:
    cover[(r["concern_id"], r["placement"])][0] += 1
for r in gaps:
    cover[(r["concern_id"], r["placement"])][1] += 1
P5 = ["where", "decides", "responsible", "boundary", "reason"]
missing = [(c["concern_id"], p) for c in con_all for p in P5 if not any(cover[(c["concern_id"], p)])]
print("inventory", len(inv), "| concerns", len(con_all), "| citations", len(cit), "| statements", len(out), "| gaps", len(gaps),
      "| not-reached", len(nr), "| review-log", len(rd(os.path.join(WORK, 'review-log.tsv'))), "| placements (record)", len(pl))
for p in P5:
    s = sum(1 for c in con_all if cover[(c["concern_id"], p)][0])
    g = sum(1 for c in con_all if cover[(c["concern_id"], p)][1] and not cover[(c["concern_id"], p)][0])
    print(f"  {p}: cells with a statement {s}, with a gap {g}")
print("cells with neither:", missing[:10], len(missing))
print("gaps by kind:", dict(collections.Counter(r["gap_kind"] for r in gaps)), "| by who:", dict(collections.Counter(r["who_can"] for r in gaps)))
print("statements whose first source doesn't contain them:", len(problems))
for x in problems[:20]:
    print("  ", x)
wc = [r for r in out if check_quote(r["statement"], cit_by[ids(r["cite_ids"])[0]]["source"], allow_working=False)[0] == "unresolved"]
print("statements whose first source is a web page outside the capture:", len(wc), collections.Counter(cit_by[ids(r["cite_ids"])[0]]["source"] for r in wc))
