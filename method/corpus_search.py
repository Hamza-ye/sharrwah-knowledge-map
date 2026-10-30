# Searches a platform's held text corpora for words, in every language they hold, and lists each document that
# matches: where it is held (at a commit), its address, its title and a snippet. It is the search a gap of kind
# "searched, not found" must show it ran (studies/subjects/S-01/briefs/A-one-platform.md), and the one an absence
# audit re-runs. Matching ignores case, Arabic diacritics and tatweel, and the spelling variants of alef, ta
# marbuta and alef maqsura.
#
# The observed repositories' fetch archives (WARC) are searched too, their code bundles (JavaScript) among them, such as
# Shopify's admin and sign-up bundles: a bundle longer than 400,000 characters is searched in pieces of 200,000, each
# listed with its piece's number (`#piece-N`). Their text is extracted once per commit into a cache outside the
# repositories (~/.cache/sharrwah-corpus), which the first search builds in a few minutes.
# So are Shopify's Help Center pages held in observed-sh (English as Markdown, Arabic as content HTML), WooCommerce's
# release files (its code first, built bundles last, and its language template i18n/languages/woocommerce.pot one
# entry at a time), this repository's capture
# runs, and the founder's saves for the platform (evidence/product-class/blocked-evidence-founder/<platform>/:
# browser saves, and PDFs through pdftotext). An address held more than once shows its fullest copy.
#
# For Shopify and Salla, the observed repositories' runs are searched too (method/runs_corpus.py): what the admin's
# own API answered (observed-sh's answers) or Salla's hosts returned (observed-sa's saved responses), what each step's
# page showed (steps/NNN.aria.yaml and NNN.text.txt, journeys and sweeps alike), the requests the pages sent, the
# indexes and derived tables built from them, and the structures' source files. Each document of a run is listed by
# its own place, never merged with another store's or run's.
#
# Usage: python3 -I method/corpus_search.py PLATFORM TERM [TERM ...] [--all] [--max N] [--brief] [--with TERM [TERM ...]]
#                                           [--runs-only | --only TEXT]
#   PLATFORM is shopify, salla, woocommerce, zid or bigcommerce. A document matches when it holds any TERM
#   (every TERM with --all) and, with --with, also any of the terms after --with: such as a thing's names, with the
#   places or plans it may hold for. At most N documents per corpus are listed (default 40), those where the terms
#   are densest first; every address past the cap follows, one line each. A Zid help page is matched on its
#   article alone, without the help centre's menu, which every page holds; a captured page shows its title.
#   --brief prints, past the cap, how many more documents each corpus holds, not every address.
#   --runs-only searches only the observed repositories' runs (Shopify and Salla), in seconds; --only TEXT searches only
#   the run corpora whose name holds TEXT, such as --only "step text from saved HTML".
#   Snippets are folded for matching (case, diacritics, letter forms): never quote one; quote the document.
import csv, glob, gzip, html, json, os, re, subprocess, sys, unicodedata, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import norm, HARAKAT, html_text
import runs_corpus

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPOS = {"observed-sa": "/home/user/observed-sa", "observed-sh": "/home/user/observed-sh",
         "other-product-class": os.environ.get("OTHER_PRODUCT_CLASS", "/home/user/other-product-class")}
HOSTS = {  # captured pages in this repository's runs, by the host they came from (a whole host or its subdomain)
    "shopify": r"(^|\.)(shopify\.(com|dev)|stripe\.com)$",
    "salla": r"(^|\.)salla\.(sa|com|dev)$",
    "woocommerce": r"(^|\.)(woocommerce\.com|wordpress\.org|wordpress\.com|stripe\.com|woo\.com|automattic\.com)$",
    "zid": r"(^|\.)zid\.(sa|dev|eg)$",
    "bigcommerce": r"(^|\.)(bigcommerce\.com|bigcommerce\.co\.uk|commerce\.com|bitpay\.com)$",
}
ARCHIVES = {"salla": ("observed-sa", ""), "shopify": ("observed-sh", ""),   # whose fetch archives each platform's
            "zid": ("other-product-class", "zid/"),                        # search reads: the repository, and the folder
            "bigcommerce": ("other-product-class", "bigcommerce/"),
            "woocommerce": ("other-product-class", "woocommerce/")}
CACHE = os.path.join(os.path.expanduser("~"), ".cache", "sharrwah-corpus")
TEXTUAL = re.compile(r"(?i)text/html|application/xhtml|text/plain|text/markdown|application/json|text/x-markdown|javascript|ecmascript")
SCRIPT = re.compile(r"(?i)javascript|ecmascript")
PIECE = 200000           # a script longer than this is held in pieces this long, each overlapping the last by 2,000
HELD = {  # text corpora held in the observed repositories: (repository, path glob, format)
    # Zid as the founder's local agent captured it (28 October 2026): its dashboard's own structures (routes, page
    # index, locales, plan policies, permissions), and its runs' step text and saved answers
    "zid": [("other-product-class", "zid/structures/**/items.jsonl", "lines"),
            ("other-product-class", "zid/raw/runs/*/steps/*.text.txt", "text"),
            ("other-product-class", "zid/raw/runs/*/answers/**/*.json", "text")],
    # BigCommerce and WooCommerce as the founder's local agent captured them (29 October 2026): a trial store and a
    # test store of our own, their runs' step text and saved answers, BigCommerce's standard formats by country, and
    # the test store's options table
    "bigcommerce": [("other-product-class", "bigcommerce/structures/**/items.jsonl", "lines"),
                    ("other-product-class", "bigcommerce/raw/runs/*/steps/*.text.txt", "text"),
                    ("other-product-class", "bigcommerce/raw/runs/*/answers/**/*.json", "text")],
    "woocommerce": [("other-product-class", "woocommerce/raw/runs/*/steps/*.text.txt", "text"),
                    ("other-product-class", "woocommerce/raw/runs/*/answers/**/*.json", "text"),
                    ("other-product-class", "woocommerce/raw/runs/*/options.tsv", "lines")],
    "salla": [("observed-sa", "structures/salla/help-articles/ar/texts.jsonl", "articles"),
              ("observed-sa", "structures/salla/help-articles/en/texts.jsonl", "articles"),
              ("observed-sa", "structures/salla/com-policies/*/text.txt", "text"),
              ("observed-sa", "structures/salla/dashboard-translations/*/*.json", "text")],
    "shopify": [("observed-sh", "structures/shopify/**/items.jsonl", "lines"),
                # The Help Center as its own menus hold it: English pages as Markdown, Arabic pages as content HTML.
                ("observed-sh", "structures/shopify/help-center/help.shopify.com@en-ar/md/en/**/*.md", "help-md"),
                ("observed-sh", "structures/shopify/help-center/help.shopify.com@en-ar/content.html/ar/**/*.html", "help-html")],
}
HELP_ROOT = "structures/shopify/help-center/help.shopify.com@en-ar/"
RELEASES = {  # release files held outside the repositories: platform -> (citation prefix, folder)
    "woocommerce": ("woocommerce-11.2.1", os.environ.get("WOO_RELEASE", "/home/user/woocommerce-release/11.2.1/woocommerce")),
}
RELEASE_TEXT = re.compile(r"\.(php|js|jsx|ts|tsx|json|txt|html|md|pot|csv)$")
RELEASE_FIRST = ("includes/", "src/", "templates/")
RELEASE_LAST = ("assets/", "packages/", "vendor/", "lib/")

def pot_entries(text):
    """(first line, text) of each entry of a .pot file: the blocks between blank lines."""
    start, block = 1, []
    for i, line in enumerate(text.split("\n"), start=1):
        if line.strip():
            if not block:
                start = i
            block.append(line)
        elif block:
            yield start, "\n".join(block)
            block = []
    if block:
        yield start, "\n".join(block)

def help_url(name):
    """The Help Center address of a held page: md/en/a/b.md -> https://help.shopify.com/en/a/b."""
    rel = name[len(HELP_ROOT):]
    rel = re.sub(r"^(md|content\.html)/", "", rel)
    rel = re.sub(r"\.(md|html)$", "", rel)
    rel = re.sub(r"/index$", "", rel)
    return "https://help.shopify.com/" + rel

def fold(s):
    s = re.sub(r"\\([\\`*_{}\[\]()#+.!|-])", r"\1", s)    # Markdown's escapes: store\_country is store_country
    s = HARAKAT.sub("", norm(s)).casefold()
    for a, b in (("أ", "ا"), ("إ", "ا"), ("آ", "ا"), ("ة", "ه"), ("ى", "ي")):
        s = s.replace(a, b)
    return s

def git_files(repo, pattern):
    """(commit, name, text) for each file at HEAD whose path matches the pattern, read from git's objects in one
    batch."""
    root = REPOS[repo]
    commit = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    names = subprocess.run(["git", "-C", root, "ls-tree", "-r", "--name-only", commit], capture_output=True,
                           text=True).stdout.split("\n")
    rx = re.compile("^" + re.escape(pattern).replace(r"\*\*/", "(?:.*/)?").replace(r"\*", "[^/]*") + "$")
    wanted = [n for n in names if rx.match(n)]
    if not wanted:
        return
    out = subprocess.run(["git", "-C", root, "cat-file", "--batch"], capture_output=True,
                         input="".join(f"{commit}:{n}\n" for n in wanted).encode("utf-8")).stdout
    pos = 0
    for n in wanted:
        end = out.index(b"\n", pos)
        head = out[pos:end].split()
        pos = end + 1
        if len(head) < 3 or head[1] == b"missing":
            continue
        size = int(head[2])
        yield commit, n, out[pos:pos + size].decode("utf-8", "replace")
        pos += size + 1

def members(path):
    """(offset, bytes) of each gzip member of a fetch archive: one WARC record each."""
    with open(path, "rb") as f:
        offset, buf = 0, b""
        while True:
            if not buf:
                buf = f.read(1 << 20)
                if not buf:
                    return
            d, out, start = zlib.decompressobj(16 + zlib.MAX_WBITS), [], offset
            while True:
                out.append(d.decompress(buf))
                if d.eof:
                    used = len(buf) - len(d.unused_data)
                    offset += used
                    buf = d.unused_data
                    break
                offset += len(buf)
                buf = f.read(1 << 20)
                if not buf:
                    return
            yield start, b"".join(out)

def record_text(raw):
    """(target URI, text) of a 2xx textual response record, or None."""
    head, _, rest = raw.partition(b"\r\n\r\n")
    warc = dict(l.split(": ", 1) for l in head.decode("utf-8", "replace").split("\r\n")[1:] if ": " in l)
    if warc.get("WARC-Type") != "response":
        return None
    http_head, _, body = rest.partition(b"\r\n\r\n")
    hh = http_head.decode("iso-8859-1", "replace").split("\r\n")
    if not re.match(r"^HTTP/\S+ 2\d\d", hh[0] if hh else ""):
        return None
    headers = {l.split(":", 1)[0].strip().lower(): l.split(":", 1)[1].strip() for l in hh[1:] if ":" in l}
    ctype = headers.get("content-type", "")
    if not TEXTUAL.search(ctype):
        return None
    try:
        if "chunked" in headers.get("transfer-encoding", "").lower():
            out, rest2 = b"", body
            while True:
                size_line, _, rest2 = rest2.partition(b"\r\n")
                size = int(size_line.split(b";")[0] or b"0", 16)
                if size == 0:
                    break
                out, rest2 = out + rest2[:size], rest2[size + 2:]
            body = out
        if headers.get("content-encoding", "").lower() == "gzip":
            body = gzip.decompress(body)
        elif headers.get("content-encoding", "").lower() == "br":
            return None
    except Exception:
        return None
    cs = re.search(r"charset=([\w-]+)", ctype)
    text = body.decode(cs.group(1) if cs else "utf-8", "replace")
    if re.search(r"html", ctype, re.I):
        text = html_text(text)
    if SCRIPT.search(ctype):                       # a code bundle is kept whole, to be cut into pieces
        return warc.get("WARC-Target-URI", ""), text
    return warc.get("WARC-Target-URI", ""), text[:400000]

def archive_documents(repo, prefix=""):
    """Documents of a repository's fetch archives (those under PREFIX, if given), from the cache for its current commit,
    built if missing."""
    root = REPOS[repo]
    commit = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    tag = "-" + prefix.strip("/").replace("/", "-") if prefix else ""
    cache = os.path.join(CACHE, f"{repo}{tag}-{commit}-scripts.jsonl.gz")   # "-scripts": code bundles are searched too
    if not os.path.exists(cache):
        os.makedirs(CACHE, exist_ok=True)
        names = [n for n in subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True).stdout.split("\n")
                 if n.endswith(".warc.gz") and n.startswith(prefix)]
        tmp = f"{cache}.{os.getpid()}.part"           # each builder writes its own file; the last finished wins
        with gzip.open(tmp, "wt", encoding="utf-8") as out:
            for n in names:
                p = os.path.join(root, n)
                if not os.path.isfile(p):
                    continue
                print(f"building the archive text cache: {n}", file=sys.stderr)
                try:
                    for off, raw in members(p):
                        got = record_text(raw)
                        if got and got[1].strip():
                            text = got[1]
                            if len(text) <= 400000:
                                out.write(json.dumps({"path": n, "offset": off, "uri": got[0], "text": text}, ensure_ascii=False) + "\n")
                            else:                  # a long code bundle: one document per piece, located as #piece-N
                                for k, at in enumerate(range(0, len(text), PIECE)):
                                    out.write(json.dumps({"path": n, "offset": off, "uri": got[0], "piece": k,
                                                          "text": text[max(0, at - 2000):at + PIECE]}, ensure_ascii=False) + "\n")
                except Exception as e:
                    print(f"  stopped reading {n}: {e}", file=sys.stderr)
        os.replace(tmp, cache)
    with gzip.open(cache, "rt", encoding="utf-8") as f:
        for line in f:
            o = json.loads(line)
            piece = f"#piece-{o['piece']}" if "piece" in o else ""
            yield (f"{repo} fetch archives", f"{repo}@{commit}:{o['path']}@{o['offset']}{piece}", o["uri"], "", o["text"])

def documents(platform):
    """(corpus, locator, url, title, text) for every held document of the platform."""
    titles = {}
    for repo, pattern, kind in HELD.get(platform, []):
        if kind == "articles":       # titles live in the items.jsonl beside each texts.jsonl
            for commit, name, raw in git_files(repo, pattern.replace("texts.jsonl", "items.jsonl")):
                for line in raw.split("\n"):   # not splitlines(): it also breaks on U+2028 inside a JSON string
                    try:
                        o = json.loads(line)
                        titles[o["url"]] = (o.get("record") or {}).get("title") or ""
                    except Exception:
                        pass
        for commit, name, raw in git_files(repo, pattern):
            if kind == "articles":               # cited by its line; the record's own position field counts from 0
                for n, line in enumerate(raw.split("\n"), start=1):   # the file's own line numbers
                    try:
                        o = json.loads(line)
                    except Exception:
                        continue
                    yield (f"{repo}:{name}", f"{repo}@{commit}:{name} line {n} (position {o.get('position')})",
                           o.get("url", ""), titles.get(o.get("url", ""), ""), o.get("text", ""))
            elif kind == "lines":            # a corpus is the whole pattern, so that --max caps it, not each file
                for i, line in enumerate(raw.split("\n"), start=1):   # the file's own line numbers
                    if line.strip():
                        yield (f"{repo}:{pattern}", f"{repo}@{commit}:{name} line {i}", "", "", line)
            elif kind == "help-md":
                title = next((l[2:].strip() for l in raw.splitlines() if l.startswith("# ")), "")
                yield ("observed-sh: Help Center, en", f"{repo}@{commit}:{name}", help_url(name), title, raw)
            elif kind == "help-html":
                yield ("observed-sh: Help Center, ar", f"{repo}@{commit}:{name}", help_url(name), "", html_text(raw))
            else:
                yield (f"{repo}:{pattern}", f"{repo}@{commit}:{name}", "", "", raw)
    if platform in ARCHIVES:
        yield from archive_documents(*ARCHIVES[platform])
    if platform in RELEASES:              # read as files, never run
        prefix, root = RELEASES[platform]
        rels = []
        for d, dirs, files in os.walk(root):
            dirs.sort()
            rels += [os.path.relpath(os.path.join(d, fn), root) for fn in sorted(files) if RELEASE_TEXT.search(fn)]
        # The platform's own code and templates first; built bundles and bundled libraries last, so that a capped
        # listing reaches the code.
        rels.sort(key=lambda r: (0 if r.startswith(RELEASE_FIRST) else 2 if r.startswith(RELEASE_LAST) else 1, r))
        for rel in rels:
            text = open(os.path.join(root, rel), encoding="utf-8", errors="replace").read()
            if rel.endswith(".pot"):          # the language template, one entry at a time, each with its line
                for start, block in pot_entries(text):
                    yield (f"{prefix} release", f"{prefix}:{rel} line {start}", "", "", block)
            else:
                yield (f"{prefix} release", f"{prefix}:{rel}", "", "", text)
    head = subprocess.run(["git", "-C", SKM, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    # The addresses some capture rendered (its visible text past 2,000 bytes, where a failed render shows an error
    # text or nothing): a capture of theirs that rendered nothing is left out, since the one that rendered stands
    # for the page, with what only its source holds beside it.
    rendered = set()
    for mf in glob.glob(os.path.join(SKM, "evidence/product-class/runs/*/manifest.tsv")):
        with open(mf, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                tp = os.path.join(os.path.dirname(mf), r.get("dir", ""), r.get("text_file") or "-")
                if os.path.isfile(tp) and os.path.getsize(tp) > 2000:
                    rendered.add(r.get("url", ""))
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
                    # The page as it rendered: its visible text, and the text of its rendered markup, whose hidden
                    # parts (a closed FAQ answer) the visible text leaves out.
                    text, title = open(tp, encoding="utf-8", errors="replace").read(), ""
                    xp = os.path.join(d, "expanded.txt")      # the lines a click shows, such as FAQ answers
                    if os.path.isfile(xp):
                        text += "\n" + open(xp, encoding="utf-8", errors="replace").read()
                    seen = fold(text)
                    rp = os.path.join(d, "rendered.html")
                    if os.path.isfile(rp):
                        page = open(rp, encoding="utf-8", errors="replace").read()
                        m = re.search(r"<title[^>]*>(.*?)</title>", page, re.S | re.I)
                        title = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else ""
                        extra = [l for l in html_text(page).splitlines() if len(l.strip()) >= 20 and fold(l) not in seen]
                        text += "\n" + "\n".join(extra)
                    # The page as served, before its scripts ran. It can hold what the page doesn't show: zid.eg's
                    # Terms page holds the Saudi Terms, which its scripts replace with the Terms of Zid Egypt.
                    served = ""
                    for raw in sorted(glob.glob(os.path.join(d, "raw*.html"))):
                        page = open(raw, encoding="utf-8", errors="replace").read()
                        m = re.search(r"<title[^>]*>(.*?)</title>", page, re.S | re.I)
                        title = title or (html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else "")
                        served += "\n" + html_text(page)
                    if host == "help.zid.sa":
                        text, served = zid_article(text), zid_article(served)
                    rel = os.path.relpath(tp, SKM)
                    if len(re.sub(r"\s+", "", text)) < 1500:
                        if r["url"] in rendered:
                            continue                 # another capture rendered the page, and stands for it
                        # the render showed an error or almost nothing: the page as served is all there is
                        yield ("capture runs", f"sharrwah-knowledge-map@{head}:{rel} (and the raw page beside it, "
                               "since the page rendered almost nothing)", r["url"], title, text + served)
                        continue
                    yield ("capture runs", f"sharrwah-knowledge-map@{head}:{rel}", r["url"], title, text)
                    seen = fold(text)
                    only = "\n".join(l for l in served.splitlines() if len(l.strip()) >= 20 and fold(l) not in seen)
                    if len(only) >= 200:
                        yield ("capture runs", f"sharrwah-knowledge-map@{head}:{os.path.relpath(d, SKM)}/raw "
                               "(the page as served: text the page as rendered doesn't show)", r["url"], title, only)
    # The founder's saves for the platform: browser saves, and the documents saved beside them.
    for path in sorted(glob.glob(os.path.join(SKM, "evidence/product-class/blocked-evidence-founder", platform, "**", "*"),
                              recursive=True)):
        if path.endswith(".html"):
            text = html_text(open(path, encoding="utf-8", errors="replace").read())
        elif path.endswith(".pdf"):
            text = subprocess.run(["pdftotext", "-q", path, "-"], capture_output=True, text=True, timeout=120).stdout
        else:
            continue
        yield ("founder's saves", f"sharrwah-knowledge-map@{head}:{os.path.relpath(path, SKM)}", "",
               os.path.basename(path), text)

ONLY = {"runs": False, "text": ""}      # --runs-only and --only: which corpora a search reads
BRIEF = {"on": False}                   # --brief: past the cap, a count per corpus, not every address

def parse(argv):
    """(platform, terms, --with terms, --all, --max) from the command line."""
    every, cap, terms, also, into = False, 40, [], [], None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--runs-only":
            ONLY["runs"] = True
        elif a == "--brief":
            BRIEF["on"] = True
        elif a == "--only":
            ONLY["runs"], ONLY["text"] = True, argv[i + 1]
            i += 1
        elif a == "--all":
            every = True
        elif a == "--max":
            cap = int(argv[i + 1])
            i += 1
        elif a == "--with":
            into = also
        elif a.startswith("--"):
            sys.exit(f"unknown option {a}")
        else:
            (into if into is not None else terms).append(a)
        i += 1
    if not terms or terms[0] not in HOSTS or len(terms) < 2:
        sys.exit("usage: corpus_search.py PLATFORM TERM [TERM ...] [--all] [--max N] [--with TERM [TERM ...]]; "
                 f"PLATFORM is one of {sorted(HOSTS)}")
    return terms[0], terms[1:], also, every, cap

ZID_START = "آخر تحديث"
ZID_END = ("التقييمات والمراجعات", "هل تحتاج إلى مساعدة إضافية", "لماذا زد")

def zid_article(text):
    """A Zid help page's article alone: from each "آخر تحديث" (last updated) to the ratings, the help prompt or the
    footer, whichever comes first. Every page also holds the help centre's menu, whose words would match on every
    page; a page without the marker is kept whole."""
    parts, at = [], text.find(ZID_START)
    while at >= 0:
        ends = [e for e in (text.find(m, at) for m in ZID_END) if e > at]
        stop = min(ends) if ends else len(text)
        parts.append(text[at:stop])
        at = text.find(ZID_START, stop)
    return "\n".join(parts) if parts else text

def matcher(terms):
    """The folded terms, and a test of which of them a folded text holds. A term in Latin letters matches whole
    words; an Arabic term matches inside words, which carry prefixes."""
    want = [fold(t) for t in terms]
    pats = [re.compile(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])") if re.search(r"[a-z]", w) else None
            for w in want]
    def hits(body):
        return [(t, w, p) for t, w, p in zip(terms, want, pats) if (p.search(body) if p else w in body)]
    return hits

def main():
    platform, terms, also, every, cap = parse(sys.argv[1:])
    main_hits, also_hits = matcher(terms), matcher(also)
    best, order = {}, []
    runs = set(runs_corpus.corpus_names(runs_corpus.RUN_REPO[platform])) if platform in runs_corpus.RUN_REPO else set()
    if ONLY["runs"] and not runs:
        sys.exit(f"--runs-only and --only search the observed runs, which only shopify and salla have")
    def every_document():
        if not ONLY["runs"]:
            for doc in documents(platform):
                yield doc + (None,)
        for corpus, loc, url, title, body in runs_corpus.search(platform, fold, terms, every, also):
            if ONLY["text"] and ONLY["text"] not in corpus:
                continue
            yield corpus, loc, url, title, body, body          # folded already
    for corpus, loc, url, title, text, body in every_document():
        body = body if body is not None else fold(title + "\n" + url + "\n" + text)
        hits = main_hits(body)
        if not hits or (every and len(hits) < len(terms)):
            continue
        with_hits = also_hits(body) if also else []
        if also and not with_hits:
            continue
        key = loc if corpus in runs else (url or loc)   # a run's document is its own observation
        if "doesn't show)" in loc:
            key = (url or loc) + " (as served)"  # what only a page's source holds is listed apart from the page
        if key not in best:
            order.append(key)
        elif len(text.strip()) <= len(best[key][4].strip()):
            continue                         # an address held more than once shows its fullest copy, not its first
        best[key] = (corpus, loc, url, title, text, body, hits, with_hits)
    # Within each corpus, the documents where the terms are densest come first, so that a capped listing reaches the
    # pages most about the terms, not the longest reference pages.
    def density(k):
        body, hits = best[k][5], best[k][6]
        n = sum(len(p.findall(body)) if p else body.count(w) for _, w, p in hits)
        return n / max(len(body), 2000)
    corpora = []
    for key in order:
        if best[key][0] not in corpora:
            corpora.append(best[key][0])
    order = [k for c in corpora for k in sorted((k for k in order if best[k][0] == c),
                                                key=lambda k: -density(k))]
    shown, total, past = {}, {}, {}
    for key in order:
        corpus, loc, url, title, text, body, hits, with_hits = best[key]
        total[corpus] = total.get(corpus, 0) + 1
        if shown.get(corpus, 0) >= cap:
            past.setdefault(corpus, []).append(f"{loc}: {title[:160]}" if corpus in runs else (url or loc))
            continue
        shown[corpus] = shown.get(corpus, 0) + 1
        _, w, p = hits[0]
        i = p.search(body).start() if p else body.find(w)
        snippet = re.sub(r"\s+", " ", body[max(0, i - 80):i + 160]).strip()
        print(f"{loc}\n    {url}\n    title: {title}\n    matched: {', '.join(t for t, _, _ in hits)}"
              + (f"; with: {', '.join(t for t, _, _ in with_hits)}" if also else "") + f"\n    …{snippet}…")
    for corpus, rest in past.items():               # every address past the cap, one line each (a count, with --brief)
        if BRIEF["on"]:
            print(f"\npast the first {cap} in {corpus}: {len(rest)} more (rerun without --brief, or with a higher --max, to list them)")
        else:
            print(f"\npast the first {cap} in {corpus}:" + "".join(f"\n    {r}" for r in rest))
    print(f"\nsearched {platform} for {terms} ({'every' if every else 'any'} term)"
          + (f", with any of {also}" if also else "") + ":",
          "; ".join(f"{c}: {n} documents{' (first ' + str(cap) + ' listed)' if n > cap else ''}" for c, n in total.items())
          or "no document matched")

if __name__ == "__main__":
    main()
