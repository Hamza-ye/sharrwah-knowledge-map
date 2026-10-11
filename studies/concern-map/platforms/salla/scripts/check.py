# Independent check of the six output files. Usage: python3 -I check.py
import csv, os, sys, re
OUT = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1/salla"
OBS = "/home/user/observed-sa"
FETCHED = os.path.join(OUT, "fetched")
csv.field_size_limit(10**9)


def read(name):
    with open(os.path.join(OUT, name), encoding="utf-8") as f:
        lines = f.read().split("\n")
    hdr = lines[0].split("\t")
    rows = []
    for n, l in enumerate(lines[1:], 2):
        if not l:
            continue
        parts = l.split("\t")
        if len(parts) != len(hdr):
            print(f"{name}:{n}: {len(parts)} fields, expected {len(hdr)}")
        rows.append(dict(zip(hdr, parts)))
    return hdr, rows


errs = 0
_, inv = read("inventory.tsv")
_, con = read("concerns.tsv")
_, pl = read("placements.tsv")
_, cit = read("citations.tsv")
url2file = {}
for i, l in enumerate(open(os.path.join(FETCHED, "log.tsv"), encoding="utf-8")):
    if i == 0 or not l.strip():
        continue
    u, f, st, at, sha = l.rstrip("\n").split("\t")
    if f:
        url2file[u] = f
cids = {c["cite_id"] for c in cit}
cache = {}
for c in cit:
    s = c["source"]
    if s.startswith("observed-sa@145f137:"):
        fp = os.path.join(OBS, s.split(":", 1)[1])
    elif s in url2file:
        fp = os.path.join(FETCHED, url2file[s])
    else:
        print("unresolved source", c["cite_id"], s); errs += 1; continue
    if fp not in cache:
        cache[fp] = open(fp, encoding="utf-8").read()
    if c["quote"] not in cache[fp]:
        print("quote not in source", c["cite_id"], s, c["quote"][:60]); errs += 1
    if len(c["quote"]) > 320 or "..." in c["quote"] or "…" in c["quote"]:
        print("quote length/ellipsis", c["cite_id"], len(c["quote"])); errs += 1
    for k in ("source_date", "date_basis", "accessed", "access_path"):
        if not c[k]:
            print("missing", k, c["cite_id"]); errs += 1
conids = {c["concern_id"] for c in con}
for r in inv:
    if r["cite_id"] not in cids:
        print("inventory cite missing", r["inv_id"]); errs += 1
    if not r["concern_ids"] and not r["out_of_scope_reason"]:
        print("inventory row unplaced", r["inv_id"]); errs += 1
    for c in r["concern_ids"].split():
        if c not in conids:
            print("unknown concern", r["inv_id"], c); errs += 1
invids = {r["inv_id"] for r in inv}
for c in con:
    for i in c["inv_ids"].split():
        if i not in invids:
            print("concern inv missing", c["concern_id"], i); errs += 1
seen = {}
for p in pl:
    if p["concern_id"] not in conids:
        print("placement concern unknown", p); errs += 1
    if p["status"] not in ("shown", "not shown"):
        print("bad status", p); errs += 1
    if p["status"] == "shown" and not p["cite_ids"]:
        print("shown without cites", p["concern_id"], p["placement"]); errs += 1
    for c in p["cite_ids"].split():
        if c not in cids:
            print("placement cite missing", p["concern_id"], c); errs += 1
    if p["note"].lower().startswith("inference") and not p["note"].startswith("Inference:"):
        print("inference label", p["concern_id"]); errs += 1
    seen.setdefault(p["concern_id"], set()).add(p["placement"])
for c in conids:
    if seen.get(c) != {"software", "decides", "legal", "boundary", "reason"}:
        print("placements incomplete", c, seen.get(c)); errs += 1

cq = {c["cite_id"]: c["quote"] for c in cit}
for r in inv:
    q = cq.get(r["cite_id"], "")
    if r["entry"] != "(no text)" and r["entry"] not in q and r["entry"].replace('"', chr(92) + '"') not in q:
        print("entry not in its quote", r["inv_id"], r["entry"][:40]); errs += 1
# entries are never empty
for r in inv:
    if not r["entry"].strip():
        print("empty entry", r["inv_id"]); errs += 1
# a concern's inv_ids are exactly the rows that carry its id
carriers = {}
for r in inv:
    for c in r["concern_ids"].split():
        carriers.setdefault(c, set()).add(r["inv_id"])
for c in con:
    have = set(c["inv_ids"].split())
    if have != carriers.get(c["concern_id"], set()):
        print("inv_ids and concern_ids disagree", c["concern_id"], sorted(have ^ carriers.get(c["concern_id"], set()))[:5]); errs += 1
    if not have and not c["split_note"].startswith("Not in the platform's lists:"):
        print("concern without entries lacks the 'Not in the platform's lists:' note", c["concern_id"]); errs += 1
# placement values use the agreed values or other: followed by the source's own words
AGREED = {
    "software": ["core", "separate service or product line", "extension point", "outside the platform"],
    "decides": ["platform at build", "operator per market", "operator per plan", "operator", "merchant", "buyer", "outside rules"],
    "legal": ["platform company", "separate entity of the platform", "partner", "app developer", "merchant", "buyer"],
}
cloc = {c["cite_id"]: c["locator"] for c in cit}


def plain(t):
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return t.replace("**", "").replace("`", "").replace("\xa0", " ")


strict = []
for p in pl:
    if p["status"] != "shown" or p["placement"] not in AGREED:
        continue
    v = p["value"]
    if v.startswith("other:"):
        words = v[len("other:"):].strip()
        hay = " ".join(plain(cq.get(c, "")) + " " + plain(cloc.get(c, "")) for c in p["cite_ids"].split())
        if plain(words) not in hay:
            strict.append(f"{p['concern_id']}/{p['placement']}: other: words not verbatim in its cited quotes or locators")
        continue
    if not any(a in v for a in AGREED[p["placement"]]):
        print("value matches no agreed value", p["concern_id"], p["placement"], v[:60]); errs += 1
    elif not any(v == a or re.match(re.escape(a) + r"[\s(:;,]", v) for a in AGREED[p["placement"]]):
        strict.append(f"{p['concern_id']}/{p['placement']}: does not start with an agreed value: {v[:60]}")
for w in strict:
    print("  note:", w)
_, nr = read("not-reached.tsv") if os.path.exists(os.path.join(OUT, "not-reached.tsv")) else (None, [])
print(f"inventory {len(inv)} concerns {len(con)} placements {len(pl)} citations {len(cit)} not-reached {len(nr)}; errors {errs}")
