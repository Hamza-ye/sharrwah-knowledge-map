# Print, for each concern in the coordinator's multi-party list, its rows by list and its placements.
# Usage: python3 -I analyse.py [concern_id ...]
import json, os, sys
OUT = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1/salla"
LIST = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1check/salla-multi-party.tsv"


def tsv(p):
    L = open(p, encoding="utf-8").read().split("\n")
    h = L[0].split("\t")
    return [dict(zip(h, l.split("\t"))) for l in L[1:] if l]


inv = tsv(os.path.join(OUT, "inventory.tsv"))
con = {c["concern_id"]: c for c in tsv(os.path.join(OUT, "concerns.tsv"))}
pl = tsv(os.path.join(OUT, "placements.tsv"))
cit = {c["cite_id"]: c for c in tsv(os.path.join(OUT, "citations.tsv"))}
B = json.load(open(os.path.join(OUT, "scripts", "build", "inventory_build.json"), encoding="utf-8"))
label = {f"SA-I-{i + 1:04d}": r["label"] for i, r in enumerate(B)}
listed = tsv(LIST)
want = sys.argv[1:] or list(dict.fromkeys(r["concern_id"] for r in listed))
for cid in want:
    c = con[cid]
    print(f"=== {cid} {c['concern']}")
    for r in listed:
        if r["concern_id"] == cid:
            print(f"  LISTED {r['placement']}: {r['value'][:200]}")
    rows = [r for r in inv if cid in r["concern_ids"].split()]
    by = {}
    for r in rows:
        by.setdefault(r["list"], []).append(r)
    for lst, rs in by.items():
        for r in rs:
            q = cit.get(r["cite_id"], {}).get("quote", "")
            extra = ""
            if lst == "other:dashboard-features":
                extra = " | " + q[q.find('"value"'):][:110]
            print(f"    {r['inv_id']} [{lst}] {label.get(r['inv_id'], r['entry'])[:90]} -> {r['concern_ids']}{extra}")
    for p in pl:
        if p["concern_id"] == cid:
            print(f"  {p['placement']}: {p['value'][:170]} | {p['status']} | {p['cite_ids']} | {p['note'][:120]}")
