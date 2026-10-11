# The combined Q1 map: matched concerns side by side, each platform in its own words.
# For every match and placement it shows what each platform states (identifier, statement, scope, citation) or the
# kind of gap. Nothing is translated into categories; differences are left for the reader.
#
# Usage: python3 -I q1_side_by_side.py STUDY_DIR
#   reads  STUDY_DIR/matches.tsv and STUDY_DIR/platforms/<platform>/{concerns,statements,gaps}.tsv
#   writes STUDY_DIR/map/side-by-side.md, STUDY_DIR/map/stated-or-gap.tsv and STUDY_DIR/map/single-platform.tsv
import csv, collections, os, re, sys

study = sys.argv[1]
PLATS = ["shopify", "salla", "woocommerce"]
NAMES = {"shopify": "Shopify", "salla": "Salla", "woocommerce": "WooCommerce"}
PLACEMENTS = [("where", "Where it lives"), ("decides", "Who decides"), ("responsible", "Who is legally responsible"),
              ("boundary", "How it meets the rest"), ("reason", "Stated reason")]
MAX_SHOWN = 6

def rd(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

def short(text, n=160):
    t = " ".join(text.split())
    return (t[:n] + " [cut]") if len(t) > n else t

def cell(text):
    return text.replace("|", "\\|")

con, st, gp = {}, {}, {}
for p in PLATS:
    base = os.path.join(study, "platforms", p)
    con[p] = {r["concern_id"]: r for r in rd(os.path.join(base, "concerns.tsv"))}
    st[p] = collections.defaultdict(list)
    for r in rd(os.path.join(base, "statements.tsv")):
        st[p][(r["concern_id"], r["placement"])].append(r)
    gp[p] = collections.defaultdict(list)
    for r in rd(os.path.join(base, "gaps.tsv")):
        gp[p][(r["concern_id"], r["placement"])].append(r)

matches = rd(os.path.join(study, "matches.tsv"))
os.makedirs(os.path.join(study, "map"), exist_ok=True)
md = ["# Q1 map, side by side", "",
      "Each match pairs concerns whose platforms' own terms clearly match (`matches.tsv`). Under each placement, each "
      "platform is quoted in its own words: the identifier it uses, an excerpt of its statement (cut at 160 characters "
      "where marked), the scope it holds for, and the citation. A gap shows its kind. Differences are left for the reader.", ""]
grid = [["match_id", "placement"] + [f"{p}_stated" for p in PLATS] + [f"{p}_gap_kind" for p in PLATS]]
matched = {p: set() for p in PLATS}
for m in matches:
    mid = m["match_id"]
    group = {p: ids(m.get(p, "")) for p in PLATS}
    for p in PLATS:
        matched[p] |= set(group[p])
    title = "; ".join(f"{NAMES[p]}: " + ", ".join(f"{c} {con[p].get(c, {}).get('concern', '?')}" for c in group[p])
                      for p in PLATS if group[p])
    md += [f"## {mid}", "", title, ""]
    if m.get("basis"):
        md += [f"Basis: {m['basis']}", ""]
    for pl, label in PLACEMENTS:
        md += [f"### {label}", ""]
        row = [mid, pl]
        kinds = []
        for p in PLATS:
            if not group[p]:
                row.append(""); kinds.append(""); continue
            s = [x for c in group[p] for x in st[p].get((c, pl), [])]
            g = [x for c in group[p] for x in gp[p].get((c, pl), [])]
            row.append(str(len(s)))
            kinds.append("; ".join(sorted({x["gap_kind"] for x in g})) if g and not s else "")
            md.append(f"- **{NAMES[p]}**" + ("" if s else f": gap ({kinds[-1] or 'no row'})"))
            for x in s[:MAX_SHOWN]:
                scope = f" [scope: {x['scope']}]" if x["scope"] else ""
                md.append(f"  - `{cell(x['identifier'][:80])}`: {cell(short(x['statement']))}{cell(scope)} ({x['cite_ids'].split(';')[0]})")
            if len(s) > MAX_SHOWN:
                md.append(f"  - and {len(s) - MAX_SHOWN} more statements in `platforms/{p}/statements.tsv`")
        md.append("")
        grid.append(row + kinds)

with open(os.path.join(study, "map", "side-by-side.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")
with open(os.path.join(study, "map", "stated-or-gap.tsv"), "w", encoding="utf-8") as f:
    for r in grid:
        f.write("\t".join(r) + "\n")
with open(os.path.join(study, "map", "single-platform.tsv"), "w", encoding="utf-8") as f:
    f.write("platform\tconcern_id\tconcern\n")
    for p in PLATS:
        for c, r in con[p].items():
            if c not in matched[p]:
                f.write(f"{p}\t{c}\t{r['concern']}\n")
print(f"matches {len(matches)}; unmatched: " + ", ".join(f"{p} {len(con[p]) - len(matched[p] & set(con[p]))}" for p in PLATS))
