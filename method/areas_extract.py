"""Extract each platform's own organizing lists from what is recorded, for the areas step (R1).

Usage: python3 -I method/areas_extract.py OUT_DIR

Writes OUT_DIR/extract-<platform>.md for the five platforms. Each holds:
- every list the concern map's inventory was built from, with the platform's own names for its entries;
- the concerns recorded for the platform: the platform's own terms for each, the concern map's
  description of it (marked as the concern map's words), and what its statements show by placement
  and by scope (the country, plan or arrangement a statement is scoped to);
- for Shopify, the Help Center's menus, two levels deep, held in observed-sh;
- for Salla, the help centre's categories and subcategories, held in observed-sa.

Held files are read from the observed repositories' git objects at one commit: HEAD when the
script runs, or OBSERVED_SH_COMMIT / OBSERVED_SA_COMMIT. Nothing is read from their working trees,
and nothing in them is run.

own_names(platform) gives the platform's own names by label, for method/check_areas.py. A concern's
terms are separated by ";" or "|", as the platforms' concern files write them.
"""
import csv, json, os, re, subprocess, sys
from collections import Counter

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CM = os.path.join(SKM, "studies", "concern-map", "platforms")
OSH = os.environ.get("OBSERVED_SH", "/home/user/observed-sh")
OSA = os.environ.get("OBSERVED_SA", "/home/user/observed-sa")
PLATFORMS = ["shopify", "salla", "woocommerce", "zid", "bigcommerce"]
SHOPIFY_OUTLINE = "structures/shopify/help-center/help.shopify.com@en-ar/outline.md"
SALLA_TREE = "structures/salla/help-tree/{lang}/items.jsonl"
# Lists of technical identifiers: their entries are shown as one compact line each.
COMPACT = {"webhook-topics", "access-scopes", "extension-points", "other:staff-permissions",
           "other:partner-access-permissions", "api-resources", "other:notification-templates",
           "other:translatable-resources"}
# The labels a name can carry besides an inventory list's own label.
TERM, HELP_CENTER, HELP_CENTRE = "term", "Help Center", "help centre"
MAX_SCOPES = 12


def rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def commit_of(repo, env):
    pinned = os.environ.get(env)
    rev = pinned or "HEAD"
    out = subprocess.run(["git", "--git-dir", os.path.join(repo, ".git"), "rev-parse", rev],
                         capture_output=True, text=True)
    return out.stdout.strip()


def held(repo, commit, rel):
    """A held file's text at a commit, from git's objects; None if it isn't there."""
    out = subprocess.run(["git", "--git-dir", os.path.join(repo, ".git"), "show", f"{commit}:{rel}"],
                         capture_output=True)
    return out.stdout.decode("utf-8") if out.returncode == 0 else None


def clean(name):
    """A help-centre name without a leading emoji or dash, or a trailing article count."""
    name = re.sub(r"^[^\w؀-ۿ]+", "", name.strip())
    return re.sub(r"\s+\d+$", "", name).strip()


def shopify_menu():
    """(level, name, path, tail) for the Help Center outline's menus, two levels deep, and the commit."""
    commit = commit_of(OSH, "OBSERVED_SH_COMMIT")
    text = held(OSH, commit, SHOPIFY_OUTLINE)
    items = []
    if text is None:
        return commit, items
    for ln in text.splitlines():
        if ln.startswith("## "):
            if ln.startswith("## Pages no menu places"):
                items.append(("heading", None, None, "Pages no menu places (the outline's own label)"))
                continue
            m = re.match(r"^## (?:\[([^\]]+)\]\([^)]*\)|([^`]+?))?\s*`([^`]+)`(.*)$", ln)
            if m:
                items.append(("heading", (m.group(1) or m.group(2) or "").strip() or None, m.group(3), m.group(4).strip()))
            continue
        m = re.match(r"^(\s*)- (?:\[([^\]]+)\]\([^)]*\)|([^`]+?))\s*`([^`]+)`(.*)$", ln)
        if not m:
            continue
        level = len(m.group(1)) // 2
        if level > 1:
            continue
        items.append((level, (m.group(2) or m.group(3) or "").strip(), m.group(4), m.group(5).strip()))
    return commit, items


def salla_tree():
    """{lang: [(breadcrumb, [subcategory names with counts])]} and the commit."""
    commit = commit_of(OSA, "OBSERVED_SA_COMMIT")
    tree = {}
    for lang in ("en", "ar"):
        text = held(OSA, commit, SALLA_TREE.format(lang=lang))
        if text is None:
            continue
        tree[lang] = []
        for line in text.splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            tree[lang].append(([b for b in d.get("breadcrumb") or [] if b != "Home" and b != "الرئيسية"],
                               [x.get("text", "") for x in d.get("subcategories") or []]))
    return commit, tree


def own_names(platform):
    """The platform's own names, by the label a name carries in an areas file."""
    names = {}
    for r in rows(os.path.join(CM, platform, "inventory.tsv")):
        if not r["out_of_scope_reason"]:
            names.setdefault(r["list"], set()).add(r["entry"].strip())
    for r in rows(os.path.join(CM, platform, "concerns.tsv")):
        for t in re.split(r"[;|]", r["platform_terms"] or ""):
            if t.strip():
                names.setdefault(TERM, set()).add(t.strip())
    if platform == "shopify":
        for level, name, _, _ in shopify_menu()[1]:
            if name:
                names.setdefault(HELP_CENTER, set()).add(name)
    if platform == "salla":
        for cats in salla_tree()[1].values():
            for crumb, subs in cats:
                for n in crumb + subs:
                    if n.strip():
                        names.setdefault(HELP_CENTRE, set()).update({n.strip(), clean(n)})
    return names


def concern_lines(platform):
    sts = rows(os.path.join(CM, platform, "statements.tsv"))
    by = {}
    for s in sts:
        by.setdefault(s["concern_id"], []).append(s)
    out = []
    for r in rows(os.path.join(CM, platform, "concerns.tsv")):
        ss = by.get(r["concern_id"], [])
        places = Counter(s["placement"] for s in ss)
        scopes = Counter(s["scope"].strip() for s in ss if s["scope"].strip())
        line = (f"- **{r['concern_id']}.** The platform's terms: {r['platform_terms'] or '(none recorded)'}. "
                f"The concern map's description: {r['concern']}.")
        if ss:
            line += f" Statements: {len(ss)} (" + ", ".join(f"{k} {v}" for k, v in sorted(places.items())) + ")."
        if scopes:
            top = scopes.most_common(MAX_SCOPES)
            line += " Scopes: " + "; ".join(f"{k} ({v})" for k, v in top)
            if len(scopes) > MAX_SCOPES:
                line += f"; and {len(scopes) - MAX_SCOPES} more"
            line += "."
        out.append(line)
    return out


def main(out):
    os.makedirs(out, exist_ok=True)
    for p in PLATFORMS:
        inv = rows(os.path.join(CM, p, "inventory.tsv"))
        con = rows(os.path.join(CM, p, "concerns.tsv"))
        lines = [f"# {p}: its own organizing lists, as recorded\n",
                 f"From `studies/concern-map/platforms/{p}/inventory.tsv` ({len(inv)} entries), `concerns.tsv` ({len(con)} concerns) "
                 "and `statements.tsv`.\n",
                 "**Whose words.** Entry names, the platform's terms and the help-centre names are the platform's own words. "
                 "List labels (such as `legal-agreements`) and each concern's description are the concern map's words: "
                 "they say where a list came from and what a concern is about, and are never names of the platform's.\n",
                 "**Labels for names.** A name taken from a list carries that list's label in brackets, as `Payments [settings]`. "
                 f"A concern's term carries `[{TERM}]`; a Shopify Help Center menu name `[{HELP_CENTER}]`; "
                 f"a Salla help-centre name `[{HELP_CENTRE}]`.\n"]
        by = {}
        for r in inv:
            by.setdefault(r["list"], []).append(r)
        lines.append("\n## Lists\n")
        for name, rs in sorted(by.items(), key=lambda kv: -len(kv[1])):
            ins = [r for r in rs if not r["out_of_scope_reason"]]
            outs = [r for r in rs if r["out_of_scope_reason"]]
            lines.append(f"\n### List `{name}` ({len(rs)} entries, {len(outs)} out of the concern map's scope)\n")
            if name in COMPACT:
                lines.append("Entries: " + "; ".join(r["entry"] for r in ins) + "\n")
            else:
                for r in ins:
                    lines.append(f"- {r['entry']} ({r['inv_id']}, {r['cite_id']}; concerns {r['concern_ids'] or 'none'})")
            if outs:
                lines.append("\nOut of the concern map's scope: " + "; ".join(f"{r['entry']} ({r['out_of_scope_reason']})" for r in outs) + "\n")
        lines.append("\n## Concerns recorded for this platform\n")
        lines.append("Each with the platform's own terms, the concern map's description, its statements by placement, "
                     f"and the scopes its statements give (the {MAX_SCOPES} most frequent).\n")
        lines.extend(concern_lines(p))
        if p == "shopify":
            commit, items = shopify_menu()
            lines.append(f"\n## The Help Center's menus (observed-sh@{commit}:{SHOPIFY_OUTLINE})\n")
            lines.append("Two levels deep, in the order and with the names the Help Center gives. The locale home's topic list comes first.\n")
            for level, name, path, tail in items:
                if level == "heading":
                    lines.append(f"\n### {name or ''} `{path}` {tail}".replace("###  ", "### ") if path else f"\n### {tail}")
                else:
                    lines.append(f"{'  ' * level}- {name} `{path}`{(' ' + tail) if tail and level == 0 else ''}")
        if p == "salla":
            commit, tree = salla_tree()
            for lang, cats in tree.items():
                lines.append(f"\n## The help centre's categories, {lang} (observed-sa@{commit}:{SALLA_TREE.format(lang=lang)})\n")
                lines.append("Each category with its breadcrumb and its subcategories, each subcategory with its number of articles.\n")
                for crumb, subs in cats:
                    s = "; ".join(f"{clean(x)} ({x.split()[-1]} articles)" if re.search(r"\s\d+$", x) else clean(x) for x in subs)
                    lines.append(f"- {' › '.join(crumb)}" + (f": {s}" if s else ""))
        with open(os.path.join(out, f"extract-{p}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
