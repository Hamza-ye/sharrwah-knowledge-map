# Load the spec parts and print a summary (and any anchor or quote errors).
# Usage: python3 -I run_spec.py [part ...]
import os, sys, importlib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newcite
parts = sys.argv[1:] or ["spec_a"]
for p in parts:
    importlib.import_module(p)
st, gp = newcite.STATEMENTS, newcite.GAPS
print("statements", len(st), dict(collections.Counter(s["placement"] for s in st)))
print("gaps", len(gp))
for s in st[-int(os.environ.get("SHOW", "0")) or len(st):][:int(os.environ.get("SHOW", "0"))]:
    print(s["concern_id"], s["placement"], s["identifier"][:40], "|", s["cite"]["locator"], "|", s["cite"]["quote"][:200])
