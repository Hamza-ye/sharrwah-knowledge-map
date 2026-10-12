# Writes studies/concern-map/gaps-to-close.md from each platform's gaps.tsv: which gaps someone can close, and how.
# Usage: python3 -I q1_gaps_report.py STUDY_DIR
import csv, collections, os, sys

study = sys.argv[1]
NAMES = {"shopify": "Shopify", "salla": "Salla", "woocommerce": "WooCommerce", "zid": "Zid", "bigcommerce": "BigCommerce"}
PLACEMENT = {"where": "where it lives", "decides": "who decides", "responsible": "who is legally responsible",
             "boundary": "how it meets the rest", "reason": "stated reason"}
KIND_ORDER = ["observation needed", "page not read", "stated only in general terms", "searched, not found"]

def rd(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def cell(text):
    return " ".join(text.split()).replace("|", "\\|")

out = ["# Gaps to close (Q1)", "",
       "Each platform's re-pass records a gap wherever the platform's own sources, as held, state nothing for a concern "
       "and placement. This page lists the gaps someone can close and how. It is generated from each platform's "
       "`gaps.tsv` by `method/q1_gaps_report.py`.", "",
       "Gap kinds:", "",
       "- **observation needed**: a journey, a store on a plan, a page saved from a browser, or a question to the platform would show it.",
       "- **page not read**: a named page would likely state it, and an agent can read it.",
       "- **stated only in general terms**: the platform's terms speak only of its services in general. The clause is cited in the gap. Applying it to one concern would be inference, so it is not a statement.",
       "- **searched, not found**: the likely pages and structures were read, and none states it. Stated reasons are the most common case, because platforms rarely say why.", ""]
for plat in ("shopify", "salla", "woocommerce", "zid", "bigcommerce"):
    gp = os.path.join(study, "platforms", plat, "gaps.tsv")
    if not os.path.exists(gp):
        continue
    gaps = rd(gp)
    con = {r["concern_id"]: r for r in rd(os.path.join(study, "platforms", plat, "concerns.tsv"))}
    by_kind = collections.Counter(r["gap_kind"] for r in gaps)
    by_who = collections.Counter(r["who_can"] for r in gaps)
    out += [f"## {NAMES[plat]}", "",
            f"{len(gaps)} gaps: " + ", ".join(f"{by_kind[k]} {k}" for k in KIND_ORDER if by_kind[k]) + ". "
            f"Who can close them: {by_who['agent']} an agent, {by_who['either']} either, {by_who['founder']} the founder.", ""]
    closable = [r for r in gaps if r["gap_kind"] in ("observation needed", "page not read")]
    if not closable:
        out += ["No gap is closable by a known page or observation.", ""]
        continue
    groups = collections.OrderedDict()
    for r in sorted(closable, key=lambda r: (r["who_can"] != "founder", r["means"], r["concern_id"])):
        groups.setdefault((r["who_can"], r["means"]), []).append(r)
    for (who, means), rows in groups.items():
        out += [f"### {means[0].upper() + means[1:]} ({who}, {len(rows)})", "",
                "| Concern | Placement | What would show it | Route |", "| --- | --- | --- | --- |"]
        for r in rows:
            name = con.get(r["concern_id"], {}).get("concern", "")
            out.append(f"| {r['concern_id']} {cell(name)} | {PLACEMENT.get(r['placement'], r['placement'])} | "
                       f"{cell(r['what_would_show_it'])} | {cell(r['route'])} |")
        out.append("")
open(os.path.join(study, "gaps-to-close.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("written", os.path.join(study, "gaps-to-close.md"))
