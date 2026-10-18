"""Write the areas list for the founder, studies/proposals/areas/areas.md, from areas.tsv, depth.tsv and the
platforms' areas files (step R1). It writes nothing of its own beyond the headings and the fixed account of what
the marks do, so areas.md always says what the files say.

Usage: python3 -I method/render_areas.py
"""
import csv, os, re
csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(SKM, "studies", "proposals", "areas")
P = {"SH": "Shopify", "SA": "Salla", "WC": "WooCommerce", "ZD": "Zid", "BC": "BigCommerce"}
FILE = {"SH": "shopify", "SA": "salla", "WC": "woocommerce", "ZD": "zid", "BC": "bigcommerce"}
Q = {"Q1": "places a store sells in or operates from", "Q2": "what a place's rules and the platform's own choices change",
     "Q3": "what a seller must do before doing particular things", "Q4": "orders paid outside the platform",
     "Q5": "payment methods: who decides, and where the money goes", "Q6": "who can register, and from where",
     "Q7": "currencies", "Q8": "how the platform is organized and grows"}
def rows(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
plat = {}
for code, name in FILE.items():
    for r in rows(os.path.join(D, f"areas-{name}.tsv")):
        plat[r["area_id"]] = r
merged = rows(os.path.join(D, "areas.tsv"))
depth = rows(os.path.join(D, "depth.tsv"))
out = ["# The platforms' broad areas, for your marks", "",
 "**Step R1, 18 October 2026.** This is the areas list your G1 answer asked for, before the detailed work. The files behind it are `areas.tsv`, `depth.tsv` and each platform's `areas-<platform>.tsv`, in this folder.", "",
 "**What it is.** Each platform's own areas, named in its own words by one short run per platform, merged into 29 areas. "
 "Where a merged area's heading is one platform's own name, it says whose. Where no one name covers all the platforms, the heading is mine, and marked as mine.", "",
 "**What your marks do.** With your marks, this list becomes Sharrwah's whole extent for the design of its first build.",
 "- **Won't do:** the area is outside Sharrwah. The first build's design leaves it out, and no proposal provides for it. Its recorded evidence still serves the questions that draw on it.",
 "- **Must do:** the area stays in. Where none of your eight items covers it, I bring you what reading it would need, and its cost, for you to decide.",
 "- **Unmarked:** it stays in.", "",
 "**Your eight items, as the questions the work asks:**"]
for k, v in Q.items():
    out.append(f"- **{k}:** {v}.")
out += ["", "## The areas", ""]
for r in merged:
    mine = r["heading_source"] == "coordinator's own"
    out.append(f"### {r['area_id']}. {r['heading']}" + (" *(my heading)*" if mine else f" *({r['heading_source'].split(' ')[0].capitalize()}'s own name)*"))
    out.append("")
    out.append(f"- **What it covers:** {r['plain_line']}")
    by = {}
    for pa in r["platform_area_ids"].split(";"):
        code = pa[:2]
        lst = by.setdefault(code, [])
        ns = [re.sub(r"\s*\[[^\]]+\]$", "", x.strip()) for x in plat[pa]["platform_names"].split(";") if x.strip()]
        lst.extend(n for n in ns[:3] if n not in lst)
    out.append("- **The platforms' own names:** " + "; ".join(f"{P[c]}: {', '.join(v)}" for c, v in by.items()) + ".")
    qs = [q for q in r["questions"].split(";") if q]
    out.append("- **Questions that draw on it:** " + (", ".join(f"{q} ({Q[q]})" for q in qs) if qs else "none") + ".")
    out.append(f"- **If you mark it \"won't do\":** {r['wont_do_removes']}")
    out.append(f"- **Kept anyway:** {r['kept_anyway']}")
    if r["left_out"]:
        out.append(f"- **Why the work leaves it out:** {r['left_out']}")
    if r["note"]:
        out.append(f"- **Note:** {r['note']}")
    out.append("")
out += ["## Which platforms each question reads in depth", "",
 "For each question, some platforms are read in depth, and the others only checked for anything that differs from the in-depth platforms or goes beyond them. Every platform is read for every question.", ""]
for q in Q:
    rs = [d for d in depth if d["question"] == q]
    ind = [d for d in rs if d["depth"] == "in depth"]
    chk = [d for d in rs if d["depth"] == "check"]
    out.append(f"### {q}: {Q[q]}")
    out.append("")
    out.append("- **In depth:** " + ", ".join(FILE_N for FILE_N in [d['platform'].capitalize().replace('Woocommerce','WooCommerce').replace('Bigcommerce','BigCommerce') for d in ind]) + ".")
    for d in ind:
        out.append(f"  - **{d['platform'].capitalize().replace('Woocommerce','WooCommerce').replace('Bigcommerce','BigCommerce')}:** {d['why']}")
    out.append("- **Checked:** " + ", ".join(d['platform'].capitalize().replace('Woocommerce','WooCommerce').replace('Bigcommerce','BigCommerce') for d in chk) + ".")
    for d in chk:
        out.append(f"  - **{d['platform'].capitalize().replace('Woocommerce','WooCommerce').replace('Bigcommerce','BigCommerce')}:** {d['why']}")
    out.append("")
open(os.path.join(D, "areas.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(out), "lines;", sum(len(x) for x in out), "chars")
