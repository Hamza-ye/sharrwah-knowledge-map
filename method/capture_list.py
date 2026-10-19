"""Write the founder's capture list from the recording runs' not-found rows (PLAN.md section 4, step R3).

Usage: python3 -I method/capture_list.py [OUT]

Reads every studies/proposals/records/<question>/<platform>/not-found.tsv and keeps the rows whose `who_can` is
`founder` or `either`. Writes OUT, by default studies/proposals/capture-list.md: by platform, the pages to capture
inside a seller's account or on a public page, and the questions to ask the platform, each with what it would show
and the row it closes. Capturing is optional, and the work doesn't wait for it.
"""
import csv, glob, os, re, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SKM, "studies", "proposals", "capture-list.md")
NAMES = {"shopify": "Shopify", "salla": "Salla", "woocommerce": "WooCommerce", "zid": "Zid",
         "bigcommerce": "BigCommerce"}
ASK = re.compile(r"\b(ask|question to|a question)\b|اسأل", re.I)


def rows():
    out = []
    for path in sorted(glob.glob(os.path.join(SKM, "studies", "proposals", "records", "Q*", "*", "not-found.tsv"))):
        q, platform = path.split(os.sep)[-3:-1]
        with open(path, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                if r.get("who_can") in ("founder", "either"):
                    out.append((platform, q, r))
    return out


def cell(s):
    return " ".join((s or "").split())


def main(argv):
    out = argv[0] if argv else OUT
    found = rows()
    lines = ["# What only you can capture, or ask (optional)", "",
             "Written by `method/capture_list.py` from the recording runs' rows that only you can close: pages inside "
             "a seller's account, pages that can't be read from here, and questions only the platform can answer. "
             "Each says where to go, what to capture or ask, and what it would show. Capturing is optional, and the "
             "work doesn't wait for it. Anything you capture can still feed the proposals.", "",
             "**How to save a page:** SingleFile from a normal browser, into "
             "`evidence/product-class/blocked-evidence-founder/<platform>/`, as before. Captured accounts are "
             "synthetic, so nothing needs masking.", ""]
    for platform in NAMES:
        mine = [(q, r) for p, q, r in found if p == platform]
        if not mine:
            continue
        lines += [f"## {NAMES[platform]} ({len(mine)})", ""]
        for title, keep in [("To capture", lambda r: not ASK.search(r["route"])),
                            ("To ask", lambda r: ASK.search(r["route"]))]:
            part = [(q, r) for q, r in mine if keep(r)]
            if not part:
                continue
            lines += [f"**{title}:**", ""]
            for q, r in part:
                lines.append(f"- **{cell(r['route'])}**")
                lines.append(f"  - It would show: {cell(r['what_is_missing'])} ({q}, `{r['nf_id']}`)")
            lines.append("")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"wrote {os.path.relpath(out, SKM)}: {len(found)} rows")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
