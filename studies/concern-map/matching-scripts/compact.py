"""Compact view: per concern, terms and inventory entries grouped by list (truncated).
Usage: python3 -I compact.py <platform> [maxchars]"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import load  # noqa: E402
p = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 500
concerns = load.load(p)[0]
for cid, c in concerns.items():
    print(f"#### {cid} | {c['name']}\n  TERMS: {c['terms_raw']}")
    g = collections.OrderedDict()
    for r in c["inv"]:
        g.setdefault(r["list"], []).append(r["entry"])
    for k, v in g.items():
        s = " | ".join(v)
        print(f"  [{k}] ({len(v)}) {s[:mx]}")
