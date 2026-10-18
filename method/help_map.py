"""Show a platform's own map of its help, one part at a time, for recording runs (step R3).

Usage:
  python3 -I method/help_map.py shopify                     the Help Center's menus, each with its line in outline.md
  python3 -I method/help_map.py shopify LINE [--anchors]    the pages the menu at that line files: level, title, held
                                                            path; with --anchors, each page's anchored sections too
  python3 -I method/help_map.py salla [en|ar]               the help centre's categories: id, breadcrumb, subcategories
  python3 -I method/help_map.py salla CATEGORY_ID          the articles that category files, in both languages:
                                                            article id, sub-section, Arabic title, English title
                                                            ("-" where that language has none)
  python3 -I method/help_map.py shopify page PATH            one held page, by the path the menu listing gives
                                                            (md/en/... or content.html/ar/...), as text
  python3 -I method/help_map.py salla page ARTICLE [ar|en]   one held article, by its id (the end of its address) or its
                                                            address, as text; Arabic unless en is given

Salla's Arabic help centre is the fuller one: 1,658 articles against 1,280, and about a quarter of the Arabic
articles have no English version. A Shopify page's Arabic version is at the English path with md/en/ changed to
content.html/ar/ and .md to .html. Arabic pages print as the quote checker reads them (method/quote_check.py,
html_text), so a quote copied from the output passes the checker.

Reads the held files from git's objects at observed-sh's and observed-sa's HEAD, from outside the repositories.
A page or article is printed after the line to cite it by: its source, and for a Salla article its locator.
"""
import json, os, re, subprocess, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import html_text

OSH = os.environ.get("OBSERVED_SH", "/home/user/observed-sh")
OSA = os.environ.get("OBSERVED_SA", "/home/user/observed-sa")
SH_ROOT = "structures/shopify/help-center/help.shopify.com@en-ar/"


def git(repo, *args):
    return subprocess.run(["git", "--git-dir", os.path.join(repo, ".git")] + list(args), capture_output=True).stdout


def head(repo):
    return git(repo, "rev-parse", "HEAD").decode().strip()


def shopify_page(path):
    commit = head(OSH)
    raw = git(OSH, "show", f"{commit}:{SH_ROOT}{path}").decode("utf-8", "replace")
    if not raw:
        sys.exit(f"not held: {SH_ROOT}{path}")
    print(f"source: observed-sh@{commit}:{SH_ROOT}{path}\n")
    if path.endswith(".html"):                       # as the checker reads it
        raw = html_text(raw)
    print(raw)


def salla_page(article, lang):
    commit = head(OSA)
    path = f"structures/salla/help-articles/{lang}/texts.jsonl"
    want = urllib.parse.unquote(article).rstrip("/").split("/")[-1]
    titles = {}
    for line in git(OSA, "show", f"{commit}:structures/salla/help-articles/{lang}/items.jsonl").decode("utf-8").splitlines():
        if line.strip():
            d = json.loads(line)
            titles[d.get("url", "")] = (d.get("record") or {}).get("title", "")
    for n, line in enumerate(git(OSA, "show", f"{commit}:{path}").decode("utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        d = json.loads(line)
        url = urllib.parse.unquote(d.get("url", "")).rstrip("/")
        if d.get("id") == want or url.split("/")[-1] == want or url == urllib.parse.unquote(article).rstrip("/"):
            title = titles.get(d.get("url", ""), "")
            print(f"source: observed-sa@{commit}:{path}\nlocator: line {n} (article {d.get('id')}, {title})\n"
                  f"address: {d.get('url', '')}\n")
            print(d.get("text", ""))
            return
    sys.exit(f"no article {article} in {path}")


def shopify(args):
    if args[:1] == ["page"] and len(args) > 1:
        return shopify_page(args[1])
    commit = head(OSH)
    lines = git(OSH, "show", f"{commit}:{SH_ROOT}outline.md").decode("utf-8").splitlines()
    print(f"observed-sh@{commit}:{SH_ROOT}outline.md")
    menus = [(i, l) for i, l in enumerate(lines, start=1) if re.match(r"^- \[", l)]
    if not args:
        section = ""
        for i, l in enumerate(lines, start=1):
            if l.startswith("## "):
                section = l[3:]
            m = re.match(r"^- \[([^\]]+)\]\(([^)]*)\)", l)
            if m:
                n = sum(1 for x in lines[i:next((j for j, _ in menus if j > i), len(lines) + 1) - 1] if "](md/" in x)
                print(f"{i}\t{m.group(1)}\t{n} pages\t{section[:40]}")
        return
    start = int(args[0])
    end = next((j for j, _ in menus if j > start), len(lines) + 1)
    anchors = "--anchors" in args
    for l in lines[start - 1:end - 1]:
        m = re.match(r"^(\s*)- \[([^\]]+)\]\(([^)]*)\)", l)
        if m:
            print(f"{len(m.group(1)) // 2}\t{m.group(2)}\t{m.group(3)}")
        elif anchors:
            a = re.match(r"^(\s*)- (#\S+): (.*)$", l)
            if a:
                print(f"{len(a.group(1)) // 2}\t  {a.group(3)}\t{a.group(2)}")


def salla(args):
    lang = next((a for a in args if a in ("en", "ar")), None)
    rest = [a for a in args if a not in ("en", "ar")]
    if rest[:1] == ["page"] and len(rest) > 1:
        return salla_page(rest[1], lang or "ar")
    lang = lang or "en"
    commit = head(OSA)
    if not rest:
        path = f"structures/salla/help-tree/{lang}/items.jsonl"
        print(f"observed-sa@{commit}:{path}")
        for line in git(OSA, "show", f"{commit}:{path}").decode("utf-8").splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            cid = d.get("url", "").rstrip("/").split("/")[-1]
            subs = "; ".join(x.get("text", "") for x in d.get("subcategories") or [])
            print(f"{cid}\t{' › '.join(d.get('breadcrumb') or [])}\t{subs}")
        return
    cat = rest[0]
    titles, subs, order = {}, {}, []
    for lg in ("ar", "en"):
        path = f"structures/salla/help-articles/{lg}/items.jsonl"
        if lg == "ar":
            print(f"observed-sa@{commit}:structures/salla/help-articles/{{ar,en}}/items.jsonl")
        for line in git(OSA, "show", f"{commit}:{path}").decode("utf-8").splitlines():
            if not line.strip():
                continue
            d = json.loads(line)
            r = d.get("record") or {}
            if r.get("section_id") != cat:
                continue
            aid = r.get("id") or d.get("url", "").rstrip("/").split("/")[-1]
            if aid not in titles:
                order.append(aid)
                titles[aid] = {}
            titles[aid][lg] = r.get("title", "")
            sub = r.get("sub_section")
            subs.setdefault(aid, sub.get("name", "") if isinstance(sub, dict) else (sub or ""))
    print("article id\tsub-section\tArabic title\tEnglish title")
    for aid in order:
        print(f"{aid}\t{subs[aid]}\t{titles[aid].get('ar', '-')}\t{titles[aid].get('en', '-')}")

if __name__ == "__main__":
    if not sys.argv[1:] or sys.argv[1] not in ("shopify", "salla"):
        sys.exit(__doc__)
    (shopify if sys.argv[1] == "shopify" else salla)(sys.argv[2:])
