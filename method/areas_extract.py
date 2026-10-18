"""Extract each platform's own organizing lists from what is recorded, for the areas step.

Usage: python3 -I method/areas_extract.py OUT_DIR

Writes OUT_DIR/extract-<platform>.md for the five platforms. Each holds, in the platform's own
words and with their ids, every list the concern map's inventory was built from, the concerns
recorded for the platform, and, for Shopify, the Help Center's menus as held in observed-sh.
Nothing here is grouped or named by us: lists keep the names the inventory gave them, which name
where each list came from.
"""
import csv, os, re, subprocess, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CM = os.path.join(SKM, "studies", "concern-map", "platforms")
OSH = os.environ.get("OBSERVED_SH", "/home/user/observed-sh")
OSA = os.environ.get("OBSERVED_SA", "/home/user/observed-sa")
PLATFORMS = ["shopify", "salla", "woocommerce", "zid", "bigcommerce"]
# Lists of technical identifiers: shown as one compact line each, not entry by entry.
COMPACT = {"webhook-topics", "access-scopes", "extension-points", "other:staff-permissions",
           "other:partner-access-permissions", "api-resources", "other:notification-templates",
           "other:translatable-resources"}


def rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def head(repo):
    return subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()


def shopify_help(lines):
    """The Help Center outline's menus, two levels deep, from observed-sh's outline.md."""
    rel = "structures/shopify/help-center/help.shopify.com@en-ar/outline.md"
    path = os.path.join(OSH, rel)
    if not os.path.exists(path):
        return
    commit = head(OSH)
    lines.append(f"\n## The Help Center's menus (observed-sh@{commit[:9]}:{rel})\n")
    lines.append("Two levels deep, in the order and names the Help Center gives. The locale home's topic list comes first.\n")
    text = open(path, encoding="utf-8").read().splitlines()
    for ln in text:
        m = re.match(r"^(\s*)- (?:\[([^\]]+)\]\([^)]*\)|([^`]+?))\s*`([^`]+)`(.*)$", ln)
        if ln.startswith("## "):
            lines.append("\n" + ln.replace("## ", "### ", 1))
            continue
        if not m:
            continue
        indent = len(m.group(1)) // 2
        if indent > 1:
            continue
        name = (m.group(2) or m.group(3) or "").strip()
        tail = m.group(5).strip()
        lines.append(f"{'  ' * indent}- {name} `{m.group(4)}`{(' ' + tail) if tail and indent == 0 else ''}")


def salla_help(lines):
    """The help centre's categories and their subcategories, from observed-sa's help-tree."""
    import json
    commit = head(OSA)
    for lang in ("en", "ar"):
        rel = f"structures/salla/help-tree/{lang}/items.jsonl"
        path = os.path.join(OSA, rel)
        if not os.path.exists(path):
            continue
        lines.append(f"\n## The help centre's categories, {lang} (observed-sa@{commit[:9]}:{rel})\n")
        lines.append("Each category with its breadcrumb and its subcategories, as the help centre gives them.\n")
        with open(path, encoding="utf-8") as f:
            for line in f:
                d = json.loads(line)
                crumb = " › ".join(d.get("breadcrumb") or [])
                subs = "; ".join(x.get("text", "") for x in d.get("subcategories") or [])
                lines.append(f"- {crumb}" + (f": {subs}" if subs else ""))


def main(out):
    os.makedirs(out, exist_ok=True)
    for p in PLATFORMS:
        inv = rows(os.path.join(CM, p, "inventory.tsv"))
        con = rows(os.path.join(CM, p, "concerns.tsv"))
        lines = [f"# {p}: its own organizing lists, as recorded\n",
                 f"From `studies/concern-map/platforms/{p}/inventory.tsv` ({len(inv)} entries) and `concerns.tsv` ({len(con)} concerns). "
                 "Each entry keeps its `inv_id` and `cite_id`; the citation gives its source at a commit. "
                 "List names are the inventory's own labels for where each list came from.\n"]
        by = {}
        for r in inv:
            by.setdefault(r["list"], []).append(r)
        lines.append("\n## Lists\n")
        for name, rs in sorted(by.items(), key=lambda kv: -len(kv[1])):
            ins = [r for r in rs if not r["out_of_scope_reason"]]
            outs = [r for r in rs if r["out_of_scope_reason"]]
            lines.append(f"\n### {name} ({len(rs)} entries, {len(outs)} out of the concern map's scope)\n")
            if name in COMPACT:
                lines.append("Entries: " + "; ".join(r["entry"] for r in ins) + "\n")
            else:
                for r in ins:
                    lines.append(f"- {r['entry']} ({r['inv_id']}, {r['cite_id']}; concerns {r['concern_ids'] or 'none'})")
            if outs:
                lines.append("\nOut of the concern map's scope: " + "; ".join(f"{r['entry']} ({r['out_of_scope_reason']})" for r in outs) + "\n")
        lines.append("\n## Concerns recorded for this platform\n")
        for r in con:
            lines.append(f"- {r['concern_id']}: {r['concern']}. Terms: {r['platform_terms']}")
        if p == "shopify":
            shopify_help(lines)
        if p == "salla":
            salla_help(lines)
        with open(os.path.join(out, f"extract-{p}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
