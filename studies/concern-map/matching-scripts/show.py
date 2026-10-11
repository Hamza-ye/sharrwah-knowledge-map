"""Print full statements (and inventory) for given concern ids.
Usage: python3 -I show.py [--inv] [--max N] CID [CID ...]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import load  # noqa: E402
args = sys.argv[1:]
inv = "--inv" in args
mx = 600
if "--max" in args:
    i = args.index("--max"); mx = int(args[i + 1]); args = args[:i] + args[i + 2:]
args = [a for a in args if a != "--inv"]
data = load.load_all()
allc = {}
for p in load.PLATFORMS:
    allc.update(data[p][0])
for cid in args:
    c = allc[cid]
    print(f"#### {cid} | {c['name']}\n  TERMS: {c['terms_raw']}")
    if inv:
        for r in c["inv"]:
            print(f"  INV {r['inv_id']} [{r['list']}] {r['entry']} (cite {r['cite_id']})")
    for s in c["stmts"]:
        print(f"  ST [{s['placement']}] id={s['identifier']!r} cite={s['cite_ids']} struct={s['structure'][:80]}\n     \"{s['statement'][:mx]}\"")
    print()
