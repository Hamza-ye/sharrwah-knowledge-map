"""The Knowledge Map's page, rebuilt from the class's model's files (PLAN.md, Stage 4A; the founder, 30 October).

The founder's view of the extent: its areas and capabilities, which platforms establish each and where, each linked to
its cells at a pinned commit, and Q3's check. The script reads only the model's merged files, the seed's areas and
source types, the concern map's statements, inventory and citations, and Q3's check when it has run, so the page
can't drift from them. A cell with nothing held reads as nothing held, never as absent.

    python3 -I method/km_page.py [--commit <sha>] [--out <file>] [--draft]

--commit is the commit the links pin, by default HEAD; the merged files and Q3's check in the working tree must equal
it. --draft marks the page as a draft, for a view before every domain and platform has run.
"""
import argparse, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows, items, key

ROOT = os.path.abspath(os.path.join(MODEL, "..", ".."))
CMAP = os.path.join(ROOT, "studies", "concern-map", "platforms")
REPO = "https://github.com/Hamza-ye/sharrwah-knowledge-map"
NAMES = {"shopify": ("Shopify", "SH"), "salla": ("Salla", "SA"), "woocommerce": ("WooCommerce", "WC"),
         "zid": ("Zid", "ZD"), "bigcommerce": ("BigCommerce", "BC")}
MERGED = os.path.join(MODEL, "merged")
Q3 = os.path.join(MODEL, "q3-check.tsv")
TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "km_page_template.html")


def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True)


def clip(s, n):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[:n] + " …"


def numbered(path):
    """Rows of a TSV with the line each holds in the file, the header being line 1."""
    return [(r, i + 2) for i, r in enumerate(rows(path))]


def source(src, locator, commit):
    """A citation's source as a label and a link: a page by its address, a held file at its commit and line."""
    m = re.match(r"line (\d+)", locator or "")
    line = f"#L{m.group(1)}" if m else ""
    at = f" {locator}" if locator else ""
    if src.startswith(("http://", "https://")):
        return clip(re.sub(r"^https?://", "", src) + at, 140), src
    m = re.match(r"(observed-sh|observed-sa|other-product-class)@([0-9a-f]+):(.+)", src)
    if m:
        return clip(f"{m.group(1)} {m.group(3)}{at}", 140), f"https://github.com/Hamza-ye/{m.group(1)}/blob/{m.group(2)}/{m.group(3)}{line}"
    m = re.match(r"woocommerce-(\d+\.\d+\.\d+):(.+)", src)
    if m:
        return clip(f"WooCommerce {m.group(1)} {m.group(2)}{at}", 140), f"https://plugins.trac.wordpress.org/browser/woocommerce/tags/{m.group(1)}/{m.group(2)}{line}"
    m = re.match(r"sharrwah-knowledge-map:(.+)", src)
    if m:
        return clip(f"{m.group(1)}{at}", 140), f"{REPO}/blob/{commit}/{m.group(1)}"
    return clip(src + at, 140), ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", default="HEAD")
    ap.add_argument("--out", default=os.path.join(MODEL, "knowledge-map.html"))
    ap.add_argument("--draft", action="store_true")
    a = ap.parse_args()
    r = git("rev-parse", a.commit)
    if r.returncode:
        sys.exit(f"no commit {a.commit}")
    commit = r.stdout.strip()
    watched = [os.path.relpath(MERGED, ROOT)] + ([os.path.relpath(Q3, ROOT)] if os.path.exists(Q3) else [])
    if git("diff", "--quiet", commit, "--", *watched).returncode:
        sys.exit(f"the merged files or Q3's check differ from {commit[:9]}: commit them, then pin that commit")
    date = git("show", "-s", "--format=%cs", commit).stdout.strip()

    pi = {p: i for i, p in enumerate(PLATFORMS)}
    areas_seed = rows(os.path.join(MODEL, "seed", "km-areas.tsv"))
    domains = []
    for r in areas_seed:
        d, _, name = r["domain"].partition(" ")
        if [d, name] not in domains:
            domains.append([d, name])
    areas = [[r["area_id"], r["domain"].split(" ")[0], r["area"], r["shopify_own_groupings"], r["salla_own_groupings"]] for r in areas_seed]

    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    landed = {}
    for r in rows(os.path.join(MERGED, "landings.tsv")):
        landed.setdefault(r["cap_id"], []).append([pi[r["platform"]], r["concern_id"], r["fit"]])
    cells, cell_ix = [], {}
    for r, ln in numbered(os.path.join(MERGED, "cells.tsv")):
        cell_ix[(r["cap_id"], r["platform"])] = len(cells)
        cells.append([r["cap_id"], pi[r["platform"]], r["held"], r["placed_as"], r["where"], r["scopes"], r["gaps"],
                      r["reading"], r["terms"], r["searched"], ln, r["part"]])
    caps = []
    for r, ln in numbered(os.path.join(MERGED, "capabilities.tsv")):
        k = kinds.get(r["cap_id"], {})
        caps.append([r["cap_id"], r["area"], r["capability"], r["parent"], r["note"], k.get("kind", ""), int(k.get("count") or 0),
                     k.get("class_scope", ""), [cell_ix.get((r["cap_id"], p), -1) for p in PLATFORMS], landed.get(r["cap_id"], []), ln])

    # evidence, each row with its source
    st = {}
    for p in PLATFORMS:
        for s in items(p):
            st[key(s)] = s
    inv_cite = {}
    for p in PLATFORMS:
        for r in rows(os.path.join(CMAP, p, "inventory.tsv")):
            inv_cite[r["inv_id"]] = r["cite_id"]
    cite_src = {}
    for p in PLATFORMS:
        for r in rows(os.path.join(CMAP, p, "citations.tsv")):
            cite_src[r["cite_id"]] = r
    ev, cites = {}, {}
    for r, ln in numbered(os.path.join(MERGED, "evidence.tsv")):
        k = r["key"]
        s = st.get(k)
        cid = inv_cite.get(k) if k in inv_cite else (re.split(r"[;,\s]+", s.get("cite_ids", "") or "")[0] if s else "")
        if not cid and s and "/" in k:
            cid = k.rsplit("/", 1)[-1]
        if cid and cid not in cites and cid in cite_src:
            c = cite_src[cid]
            label, url = source(c["source"], c["locator"], commit)
            cites[cid] = [label, url, clip(c["quote"], 220), c.get("source_date", "")]
        ev.setdefault(r["cap_id"], []).append([pi[r["platform"]], r["supports"], k, r["why"], cid if cid in cites else "", ln])
    qual, fill = {}, {}
    for r in rows(os.path.join(MERGED, "qualities.tsv")):
        qual.setdefault(r["cap_id"], []).append([pi[r["platform"]], r["quality"], r["value"], r["key"]])
    for r in rows(os.path.join(MERGED, "slot-fillers.tsv")):
        fill.setdefault(r["cap_id"], []).append([pi[r["platform"]], r["filler"], r["key"]])

    # which platforms have run in each domain, so a missing cell reads as not mapped yet
    cap_dom = {r["cap_id"]: r["domain"] for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    run = {}
    for c in cells:
        run.setdefault(cap_dom.get(c[0], "?"), set()).add(c[1])
    q3 = None
    if os.path.exists(Q3):
        q3r = numbered(Q3)
        q3 = {"head": list(q3r[0][0].keys()) if q3r else [], "rows": [[*r.values(), ln] for r, ln in q3r]}
    src_types = [[r["code"], r["source_type"], r["authoritative_for"], r["cannot_tell_you"], r["grading"]]
                 for r in rows(os.path.join(MODEL, "seed", "km-source-types.tsv"))]
    D = {
        "meta": {"commit": commit, "short": commit[:9], "date": date, "repo": REPO, "draft": a.draft,
                 "run": {d: sorted(v) for d, v in run.items()}},
        "platforms": [[p, *NAMES[p]] for p in PLATFORMS],
        "domains": domains, "areas": areas, "caps": caps, "cells": cells, "ev": ev, "cites": cites,
        "qual": qual, "fill": fill, "q3": q3, "sources": src_types,
    }
    data = json.dumps(D, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = open(TEMPLATE, encoding="utf-8").read()
    assert page.count("__DATA__") == 1
    page = page.replace("__DATA__", data)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write(page)
    print(f"{os.path.relpath(a.out, ROOT)}: {len(caps)} capabilities, {len(cells)} cells, {sum(len(v) for v in ev.values())} evidence rows, "
          f"{len(cites)} sources, Q3's check {'with ' + str(len(q3['rows'])) + ' rows' if q3 else 'not yet run'}; "
          f"links pinned to {commit[:9]}; {len(page) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
