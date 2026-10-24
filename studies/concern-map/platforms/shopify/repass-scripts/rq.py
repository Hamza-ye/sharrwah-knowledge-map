# Query the admin router at the re-pass commit: python3 -I scripts/rq.py REGEX  (matches id, path, title, section)
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
pat = re.compile(sys.argv[1], re.I)
for n, l in enumerate(git_show("structures/shopify/admin-router/items.jsonl").splitlines(), start=1):
    d = json.loads(l)
    t = d.get("title"); t = t.get("value") if isinstance(t, dict) else t
    p = d.get("path"); p = json.dumps(p) if isinstance(p, dict) else p
    hay = " ".join(str(x) for x in (d["id"], p, t, d.get("section")))
    if pat.search(hay):
        print(n, d.get("section"), d["id"], "|", p, "|", t, "| elig:", json.dumps(d.get("eligibility")), "| parent:", d.get("parent"))
