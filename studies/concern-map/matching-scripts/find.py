"""Find where a quote appears verbatim for a concern: concern name, platform_terms,
inventory entries, statement identifiers or statement text.
Usage: python3 -I find.py CID "text" ["text" ...]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import load  # noqa: E402
data = load.load_all()
allc = {}
for p in load.PLATFORMS:
    allc.update(data[p][0])
cid = sys.argv[1]
c = allc[cid]
for q in sys.argv[2:]:
    hits = []
    if q in c["name"]:
        hits.append("concern")
    if any(q in t for t in c["terms"]):
        hits.append("platform_terms")
    for r in c["inv"]:
        if q in r["entry"]:
            hits.append(f"inventory {r['inv_id']} [{r['entry'][:60]}]")
    for s in c["stmts"]:
        if q in s["statement"]:
            hits.append(f"statement {s['cite_ids']} id={s['identifier'][:50]!r} [{s['placement']}]")
        elif q in s["identifier"]:
            hits.append(f"statement-identifier {s['cite_ids']} id={s['identifier'][:50]!r}")
    print(f"{cid} {q!r}: " + (" || ".join(hits[:6]) if hits else "NOT FOUND"))
