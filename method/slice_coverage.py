# Lists a slice of the concern map (studies/concern-map/, Q1) and whether the decision records use it: for each
# concern Shopify's or Salla's own lists gave in the named areas, is any source its statements cite also cited by
# the decision records (decisions/, the glossary, decisions/checks/) at a commit, or by the pilot's S-01 citations?
# Written for the founder's question of 25 October (reports/M1-method-assessment.md): an omission check, where a
# check of a record's claims can't see what the record never cited.
#
# Areas reach the concern map through R1's platform areas: studies/proposals/areas/areas.tsv names each area's
# platform areas, and areas-<platform>.tsv each platform area's concerns. A source is matched by its Help Center page
# (HC:path), its Salla help article (SA-en:N, SA-ar:N, by the article's id), its structure's id, or else its address.
# Matching a structure's id says only that the records cite the same structure, not the same item of it.
#
# Usage: python3 -I method/slice_coverage.py COMMIT AREA [AREA ...] > out.tsv
#   e.g.  python3 -I method/slice_coverage.py HEAD A-03 A-11 A-12 A-13
import csv, json, os, re, subprocess, sys
from collections import defaultdict

KM = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
ARTICLES = "/home/user/observed-sa/structures/salla/help-articles/"
PLATFORMS = {"shopify": "SH-A-", "salla": "SA-A-"}
SHORT = {"RT": "admin-route-titles-en", "ROUTER": "admin-router", "GQL": "admin-graphql-schema",
         "CLI": "cli-extension-templates", "SMENU": "dashboard-settings-menu", "SNAV": "dashboard-nav",
         "SSTAT": "order-statuses", "SINV": "invoice-settings", "SAPI": "docs-operations",
         "SDS": "docs-dataschemas", "STR": "dashboard-translations"}
csv.field_size_limit(10**9)

def tsv(path):
    return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))

article = {}
for lang in ("en", "ar"):
    for line in open(ARTICLES + lang + "/texts.jsonl", encoding="utf-8"):
        d = json.loads(line)
        article.setdefault(d["id"], []).append(f"SA-{lang}:{d['position']}")

def keys(source):
    """The keys one cited source is matched by."""
    m = re.search(r"help\.shopify\.com/(?:[a-z-]+/)?manual/([^#?\s]+)", source) or re.search(r"/md/en/manual/([^#?\s]+)", source)
    if m:
        return {"HC:" + re.sub(r"\.md$", "", m.group(1)).rstrip("/")}
    m = re.search(r"help\.salla\.sa/(?:en/)?article/[^/]+/([a-z0-9]+)", source)
    if m:
        return set(article.get(m.group(1), []))
    m = re.search(r"structures/(?:shopify|salla)/([^/]+)", source)
    if m:
        return {"STRUCT:" + m.group(1)}
    m = re.search(r"https?://([^\s#?]+)", source)
    return {"URL:" + m.group(1).rstrip("/").removesuffix(".md")} if m else set()

def git(*args):
    return subprocess.run(["git", "-C", KM, *args], capture_output=True, text=True).stdout

def record_keys(commit):
    files = [f for f in git("ls-tree", "-r", "--name-only", commit, "decisions", "architecture/12-glossary.md").split()
             if re.search(r"decisions/D-\d+.*\.md$|decisions/checks/|12-glossary\.md$", f)]
    text = "\n".join(git("show", f"{commit}:{f}") for f in files)
    k = {"HC:" + p for p in re.findall(r"HC:([\w./-]+?)(?:\.md)?(?=[:`\s)|])", text)}
    k |= set(re.findall(r"SA-(?:en|ar):\d+", text))
    k |= {"STRUCT:" + sid for short, sid in SHORT.items() if re.search(rf"`{short}(?:-ar|-en)?:", text)}
    k |= {"STRUCT:" + s for s in re.findall(r"structures/(?:shopify|salla)/([\w-]+)", text)}
    for url in re.findall(r"https?://[^\s`)\]>\"']+", text):
        k |= keys(url.rstrip(".,;:"))
    return k

def pilot_keys():
    k = set()
    for p in PLATFORMS:
        for r in tsv(KM + f"studies/subjects/S-01/{p}/citations.tsv"):
            k |= keys(r["source"])
    return k

def main(commit, areas):
    used, pilot = record_keys(commit), pilot_keys()
    platform_areas = {r["area_id"]: r["platform_area_ids"].split(";") for r in tsv(KM + "studies/proposals/areas/areas.tsv")}
    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["area", "platform_area", "concern", "concern_name", "statements", "sources",
                "sources_cited_by_records", "structures_cited_by_records", "sources_cited_by_pilot"])
    for p, prefix in PLATFORMS.items():
        base = KM + f"studies/concern-map/platforms/{p}/"
        cites = {r["cite_id"]: r["source"] for r in tsv(base + "citations.tsv")}
        names = {r["concern_id"]: r["concern"] for r in tsv(base + "concerns.tsv")}
        stmts = defaultdict(list)
        for r in tsv(base + "statements.tsv"):
            stmts[r["concern_id"]].append(r)
        concerns = {r["area_id"]: r["concern_ids"].split(";") for r in tsv(KM + f"studies/proposals/areas/areas-{p}.tsv")}
        for area in areas:
            for pa in (x for x in platform_areas.get(area, []) if x.startswith(prefix)):
                for c in filter(None, concerns.get(pa, [])):
                    ks = set()
                    for s in stmts[c]:
                        for cid in filter(None, re.split(r"[;,\s]+", s["cite_ids"])):
                            ks |= keys(cites.get(cid, ""))
                    pages = {k for k in ks if not k.startswith("STRUCT:")}
                    w.writerow([area, pa, c, names.get(c, ""), len(stmts[c]), len(ks), len(pages & used),
                                len((ks - pages) & used), len(ks & pilot)])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
