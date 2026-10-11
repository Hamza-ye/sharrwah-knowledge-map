"""Verify the judged decisions against the three platform outputs and write
matches.tsv, unclear.tsv and work/stats.json.

Checks: every id exists on the right platform; no concern in two match rows; every
concern in a match row has at least one basis quote; every quote appears verbatim in
the cited field (concern name, platform_terms, an inventory entry linked to that
concern, or a statement of that concern with that cite id).

Usage: python3 -I build.py <q1m_dir>
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import load  # noqa: E402
import decisions  # noqa: E402

PREF = {"sh": "SH-C-", "sa": "SA-C-", "wc": "WC-C-"}
COLS = {"sh": "shopify", "sa": "salla", "wc": "woocommerce"}


def clean(s):
    return " ".join(str(s).replace("\t", " ").replace("\n", " ").split())


def main(outdir):
    data = load.load_all()
    concerns = {}
    inv_rows = {}
    for p in load.PLATFORMS:
        concerns.update(data[p][0])
        inv_rows.update(data[p][3])
    errors = []

    def check_quote(cid, src, q):
        c = concerns[cid]
        if src == "concern":
            return q in c["name"]
        if src == "platform_terms":
            return q in c["terms_raw"]
        if src.startswith("inventory "):
            iid = src.split(" ", 1)[1]
            r = inv_rows.get(iid)
            if not r:
                return False
            linked = cid in load.split_ids(r["concern_ids"])
            return linked and q in r["entry"]
        if src.startswith("statement "):
            sid = src.split(" ", 1)[1]
            for s in c["stmts"]:
                if sid in [x.strip() for x in s["cite_ids"].split(";")]:
                    if q in s["statement"] or q in s["identifier"]:
                        return True
            return False
        return False

    used = {}
    match_rows = []
    for n, m in enumerate(decisions.MATCHES, 1):
        mid = f"M-{n:03d}"
        ids = []
        for k in ("sh", "sa", "wc"):
            for cid in m[k]:
                if cid not in concerns or not cid.startswith(PREF[k]):
                    errors.append(f"{mid}: bad id {cid} in {k}")
                    continue
                if cid in used:
                    errors.append(f"{mid}: {cid} already in {used[cid]}")
                used[cid] = mid
                ids.append(cid)
        nplat = sum(1 for k in ("sh", "sa", "wc") if m[k])
        if nplat < 2:
            errors.append(f"{mid}: fewer than two platforms")
        quoted = set()
        groups = collections.OrderedDict()
        for cid, src, q in m["basis"]:
            if cid not in ids:
                errors.append(f"{mid}: basis cites {cid} not in row")
                continue
            if not check_quote(cid, src, q):
                errors.append(f"{mid}: quote not found: {cid} {src} {q!r}")
            quoted.add(cid)
            groups.setdefault(cid, []).append(f'{src} "{q}"')
        for cid in ids:
            if cid not in quoted:
                errors.append(f"{mid}: no basis quote for {cid}")
        basis = " | ".join(f"{cid} " + "; ".join(v) for cid, v in groups.items())
        note = f"Basis kind: {m['kind']}."
        if m.get("note"):
            note += " " + m["note"]
        match_rows.append({
            "match_id": mid,
            "shopify": ";".join(m["sh"]),
            "salla": ";".join(m["sa"]),
            "woocommerce": ";".join(m["wc"]),
            "basis": clean(basis),
            "granularity": clean(m["gran"]),
            "note": clean(note),
            "_nplat": nplat,
        })
    # resolve {M:key} references to match ids
    keymap = {m["key"]: f"M-{n:03d}" for n, m in enumerate(decisions.MATCHES, 1) if m.get("key")}
    import re as _re

    def resolve(txt):
        def sub(mo):
            k = mo.group(1)
            if k not in keymap:
                errors.append(f"unknown row key {k}")
                return mo.group(0)
            return keymap[k]
        return _re.sub(r"\{M:([a-z]+)\}", sub, txt)

    for r in match_rows:
        r["granularity"] = resolve(r["granularity"])
        r["note"] = resolve(r["note"])
    unclear_rows = []
    in_unclear = collections.defaultdict(list)
    for n, u in enumerate(decisions.UNCLEAR, 1):
        uid = f"U-{n:03d}"
        nplat = 0
        for k in ("sh", "sa", "wc"):
            if u[k]:
                nplat += 1
            for cid in u[k]:
                if cid not in concerns or not cid.startswith(PREF[k]):
                    errors.append(f"{uid}: bad id {cid}")
                in_unclear[cid].append(uid)
        if nplat < 2:
            errors.append(f"{uid}: fewer than two platforms")
        inrows = collections.OrderedDict()
        for k in ("sh", "sa", "wc"):
            for cid in u[k]:
                if cid in used:
                    inrows.setdefault(used[cid], []).append(cid)
        why = resolve(clean(u["why"]))
        if inrows:
            why += " Already in match rows: " + "; ".join(
                f"{mid} ({', '.join(c)})" for mid, c in sorted(inrows.items())) + "."
        unclear_rows.append({
            "candidate_id": uid,
            "shopify": ";".join(u["sh"]),
            "salla": ";".join(u["sa"]),
            "woocommerce": ";".join(u["wc"]),
            "why_unclear": why,
            "what_would_settle_it": resolve(clean(u["settle"])),
        })
    if errors:
        print("ERRORS:")
        for e in errors:
            print("  " + e)
    # write
    mcols = ["match_id", "shopify", "salla", "woocommerce", "basis", "granularity", "note"]
    with open(os.path.join(outdir, "matches.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(mcols) + "\n")
        for r in match_rows:
            f.write("\t".join(r[c] for c in mcols) + "\n")
    ucols = ["candidate_id", "shopify", "salla", "woocommerce", "why_unclear", "what_would_settle_it"]
    with open(os.path.join(outdir, "unclear.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(ucols) + "\n")
        for r in unclear_rows:
            f.write("\t".join(r[c] for c in ucols) + "\n")
    # stats
    stats = {"matches_total": len(match_rows),
             "matches_three_platforms": sum(1 for r in match_rows if r["_nplat"] == 3),
             "matches_two_platforms": sum(1 for r in match_rows if r["_nplat"] == 2),
             "unclear_total": len(unclear_rows)}
    pairs = collections.Counter()
    for r in match_rows:
        if r["_nplat"] == 2:
            key = "+".join(COLS[k] for k in ("sh", "sa", "wc") if r[COLS[k]])
            pairs[key] += 1
    stats["two_platform_pairs"] = dict(pairs)
    per = {}
    for p, pref in (("shopify", "SH-C-"), ("salla", "SA-C-"), ("woocommerce", "WC-C-")):
        allids = [c for c in concerns if c.startswith(pref)]
        matched = [c for c in allids if c in used]
        unmatched = [c for c in allids if c not in used]
        per[p] = {"concerns": len(allids), "matched": len(matched), "unmatched": len(unmatched),
                  "unmatched_in_unclear": len([c for c in unmatched if c in in_unclear]),
                  "unmatched_nowhere": [c for c in unmatched if c not in in_unclear],
                  "unmatched_in_unclear_ids": [c for c in unmatched if c in in_unclear]}
    stats["per_platform"] = per
    os.makedirs(os.path.join(outdir, "work"), exist_ok=True)
    with open(os.path.join(outdir, "work", "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in stats.items() if k != "per_platform"}, ensure_ascii=False))
    for p, v in per.items():
        print(p, {k: v[k] for k in ("concerns", "matched", "unmatched", "unmatched_in_unclear")})
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
