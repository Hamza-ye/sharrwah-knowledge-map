# Searches a platform's held text corpora for words, in every language they hold, and lists each document that
# matches: where it is held (at a commit), its address, its title and a snippet. It is the search a gap of kind
# "searched, not found" must show it ran (studies/subjects/S-01/briefs/A-one-platform.md), and the one an absence
# audit re-runs. Matching ignores case, Arabic diacritics and tatweel, and the spelling variants of alef, ta
# marbuta and alef maqsura.
#
# Usage: python3 -I method/corpus_search.py PLATFORM TERM [TERM ...] [--all] [--max N]
#   PLATFORM is shopify, salla, woocommerce, zid or bigcommerce. A document matches when it holds any TERM
#   (every TERM with --all). At most N documents per corpus are listed (default 40).
import csv, glob, json, os, re, subprocess, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import norm, HARAKAT, html_text

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPOS = {"observed-sa": "/home/user/observed-sa", "observed-sh": "/home/user/observed-sh"}
HOSTS = {  # captured pages in this repository's runs, by the host they came from (a whole host or its subdomain)
    "shopify": r"(^|\.)(shopify\.(com|dev)|stripe\.com)$",
    "salla": r"(^|\.)salla\.(sa|com|dev)$",
    "woocommerce": r"(^|\.)(woocommerce\.com|wordpress\.org|stripe\.com|woo\.com)$",
    "zid": r"(^|\.)zid\.(sa|dev)$",
    "bigcommerce": r"(^|\.)(bigcommerce\.com|commerce\.com|bitpay\.com)$",
}
HELD = {  # text corpora held in the observed repositories: (repository, path glob, format)
    "salla": [("observed-sa", "structures/salla/help-articles/ar/texts.jsonl", "articles"),
              ("observed-sa", "structures/salla/help-articles/en/texts.jsonl", "articles"),
              ("observed-sa", "structures/salla/com-policies/*/text.txt", "text"),
              ("observed-sa", "structures/salla/dashboard-translations/*/*.json", "text")],
    "shopify": [("observed-sh", "structures/shopify/**/items.jsonl", "lines")],
}

def fold(s):
    s = HARAKAT.sub("", norm(s)).casefold()
    for a, b in (("أ", "ا"), ("إ", "ا"), ("آ", "ا"), ("ة", "ه"), ("ى", "ي")):
        s = s.replace(a, b)
    return s

def git_files(repo, pattern):
    root = REPOS[repo]
    commit = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    names = subprocess.run(["git", "-C", root, "ls-tree", "-r", "--name-only", commit], capture_output=True,
                           text=True).stdout.split("\n")
    rx = re.compile("^" + re.escape(pattern).replace(r"\*\*/", "(?:.*/)?").replace(r"\*", "[^/]*") + "$")
    for n in names:
        if rx.match(n):
            yield commit, n, subprocess.run(["git", "-C", root, "show", f"{commit}:{n}"],
                                            capture_output=True).stdout.decode("utf-8", "replace")

def documents(platform):
    """(corpus, locator, url, title, text) for every held document of the platform."""
    titles = {}
    for repo, pattern, kind in HELD.get(platform, []):
        if kind == "articles":       # titles live in the items.jsonl beside each texts.jsonl
            for commit, name, raw in git_files(repo, pattern.replace("texts.jsonl", "items.jsonl")):
                for line in raw.splitlines():
                    try:
                        o = json.loads(line)
                        titles[o["url"]] = (o.get("record") or {}).get("title") or ""
                    except Exception:
                        pass
        for commit, name, raw in git_files(repo, pattern):
            if kind == "articles":
                for line in raw.splitlines():
                    try:
                        o = json.loads(line)
                    except Exception:
                        continue
                    yield (f"{repo}:{name}", f"{repo}@{commit}:{name} position {o.get('position')}",
                           o.get("url", ""), titles.get(o.get("url", ""), ""), o.get("text", ""))
            elif kind == "lines":
                for i, line in enumerate(raw.splitlines(), start=1):
                    yield (f"{repo}:{name}", f"{repo}@{commit}:{name} line {i}", "", "", line)
            else:
                yield (f"{repo}:{name}", f"{repo}@{commit}:{name}", "", "", raw)
    head = subprocess.run(["git", "-C", SKM, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    for mf in sorted(glob.glob(os.path.join(SKM, "evidence/product-class/runs/*/manifest.tsv"))):
        run = os.path.dirname(mf)
        with open(mf, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                host = re.sub(r"^https?://([^/]+).*$", r"\1", r.get("url", "")).lower()
                host = host[4:] if host.startswith("www.") else host
                if not re.search(HOSTS[platform], host) or not r.get("text_file"):
                    continue
                d = os.path.join(run, r["dir"])
                tp = os.path.join(d, r["text_file"])
                if os.path.isfile(tp):
                    # The visible text, and the raw page's text too: some sites keep their content only in the
                    # raw HTML, and render an error or an empty shell (zid.sa, for one).
                    text = open(tp, encoding="utf-8", errors="replace").read()
                    for raw in sorted(glob.glob(os.path.join(d, "raw*.html"))):
                        text += "\n" + html_text(open(raw, encoding="utf-8", errors="replace").read())
                    rel = os.path.relpath(tp, SKM)
                    yield ("capture runs", f"sharrwah-knowledge-map@{head}:{rel} (and the raw page beside it)", r["url"], "", text)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    every = "--all" in sys.argv
    cap = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 40
    if "--max" in sys.argv:
        args.remove(str(cap))
    if not args or args[0] not in HOSTS:
        sys.exit(f"usage: corpus_search.py PLATFORM TERM [TERM ...] [--all] [--max N]; PLATFORM is one of {sorted(HOSTS)}")
    platform, terms = args[0], args[1:]
    want = [fold(t) for t in terms]
    # A term in Latin letters matches whole words; an Arabic term matches inside words, which carry prefixes.
    pats = [re.compile(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])") if re.search(r"[a-z]", w) else None
            for w in want]
    shown, total, seen = {}, {}, set()
    for corpus, loc, url, title, text in documents(platform):
        key = (url or loc)
        if key in seen:
            continue
        body = fold(title + "\n" + url + "\n" + text)
        hits = [w for w, p in zip(want, pats) if (p.search(body) if p else w in body)]
        if not hits or (every and len(hits) < len(want)):
            continue
        seen.add(key)
        total[corpus] = total.get(corpus, 0) + 1
        if shown.get(corpus, 0) >= cap:
            continue
        shown[corpus] = shown.get(corpus, 0) + 1
        p0 = pats[want.index(hits[0])]
        i = p0.search(body).start() if p0 else body.find(hits[0])
        snippet = re.sub(r"\s+", " ", body[max(0, i - 80):i + 160]).strip()
        print(f"{loc}\n    {url}\n    title: {title}\n    matched: {', '.join(terms[want.index(h)] for h in hits)}\n    …{snippet}…")
    print(f"\nsearched {platform} for {terms} ({'every' if every else 'any'} term):",
          "; ".join(f"{c}: {n} documents{' (first ' + str(cap) + ' listed)' if n > cap else ''}" for c, n in total.items())
          or "no document matched")

if __name__ == "__main__":
    main()
