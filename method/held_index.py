# What observed-sa, observed-sh, other-product-class (its platform folders) and this repository's capture runs hold,
# by address, and in what readable form. An archive held in parts is read at the part its fetch.cdx names.
# PLAN.md Stage 0: before a gap goes to anyone, its route is checked against what is held.
#
# Readable forms, best first:
#   structure  a structure in observed-sa or observed-sh whose meta.json names the address (text or rows in git)
#   capture    a page in this repository's evidence/product-class/runs, with its text file
#   step       a step of a browser run in observed-sa or observed-sh whose page ended at the address, with its page
#              text in git (steps/NNN.text.txt or NNN.aria.yaml, or observed-sh's text of the saved HTML in
#              derived/step-text-from-html/<run>/NNN.html.txt; read it with git show)
#   answer     what a browser run's page received, saved in git: observed-sa's responses (raw/runs/<run>/responses/
#              NNNN.json, named in the run's responses.jsonl by host and path) and observed-sh's answers (named in
#              its answers.jsonl by host and endpoint)
#   warc       a record in a fetch archive that is in git (read it with method/warc_text.py)
#   cdx-only   an index line whose archive is not in git: held, but not readable from the repository
import csv, glob, json, os, re, subprocess, unicodedata, urllib.parse
from collections import defaultdict

csv.field_size_limit(10**9)
RANK = {"structure": 0, "capture": 1, "step": 2, "answer": 3, "warc": 4, "cdx-only": 5}
URL_RE = re.compile(r"https?://[^\s,;)\]>\"'|]+")
BARE_RE = re.compile(r"(?<![\w@/.-])((?:[a-z0-9-]+\.)+(?:com|sa|dev|net|org|io|ae|me|co|app|store|partners)"
                     r"(?:/[^\s,;)\]>\"'|]*)?)", re.I)

SOURCE_PATH = re.compile(r"structures/|derived/|raw/runs/|@[0-9a-f]{6,}:|"
                         r"[\w-]+/[\w./-]+\.(php|js|jsx|ts|tsx|json|md|txt|html|xml|ya?ml)\b")
CORPORA = {  # held text corpora a "searched, not found" must have covered: platform -> (marker, where)
    "salla": ("help-articles", "observed-sa structures/salla/help-articles/{ar,en}/texts.jsonl"),
}

def names_a_source(text):
    return bool(urls_in(text) or SOURCE_PATH.search(text or ""))

def norm_url(u):
    u = u.strip().rstrip(".,;:)")
    if not re.match(r"^[a-z][a-z0-9+.-]*://", u, re.I):
        u = "https://" + u
    p = urllib.parse.urlsplit(u)
    host = (p.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = unicodedata.normalize("NFC", urllib.parse.unquote(p.path))
    path = re.sub(r"/+$", "", path) or "/"
    return host + path + ("?" + p.query if p.query else "")

def url_keys(u):
    k = norm_url(u)
    keys = [k]
    base = k.split("?")[0]
    if base != k:
        keys.append(base)
    for suffix in (".md", ".txt", ".html"):
        if base.endswith(suffix):
            keys.append(base[: -len(suffix)])
    return keys

def urls_in(text):
    """Addresses named in free text: full URLs, and bare host/path tokens such as docs.salla.dev/x."""
    text = text or ""
    found = [m.rstrip(".,;:") for m in URL_RE.findall(text)]
    rest = URL_RE.sub(" ", text)
    found += [m.rstrip(".,;:") for m in BARE_RE.findall(rest)]
    out = []
    for u in found:
        if u not in out:
            out.append(u)
    return out

def git(root, *args):
    p = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""

class Held:
    def __init__(self, roots, capture_runs):
        self.by_key = defaultdict(list)
        self.commits = {}
        for repo in ("observed-sa", "observed-sh"):
            root = roots.get(repo)
            if root and os.path.isdir(os.path.join(root, ".git")):
                self._repo(repo, root)
        # other-product-class holds one folder per platform, each laid out as an observed repository is
        root = roots.get("other-product-class")
        if root and os.path.isdir(os.path.join(root, ".git")):
            for sub in ("zid/", "bigcommerce/", "woocommerce/"):
                if os.path.isdir(os.path.join(root, sub)):
                    self._repo("other-product-class", root, sub)
        skm = roots.get("sharrwah-knowledge-map")
        for run in capture_runs:
            self._capture(run, skm)

    def _add(self, url, h):
        h["url"] = url
        for k in url_keys(url):
            self.by_key[k].append(h)

    def _repo(self, repo, root, sub=""):
        """A repository, or one platform folder of it (`sub`, such as "zid/"), whose paths are given from the root."""
        commit = git(root, "rev-parse", "HEAD").strip()
        self.commits[repo] = commit
        # an archive over 100 MB is held in parts, fetch-00000.warc.gz and on; fetch.cdx names each record's part
        tracked = set(git(root, "ls-files", f"{sub}raw/runs/*/fetch.warc.gz", f"{sub}raw/runs/*/fetch-*.warc.gz").split())
        for cdx in sorted(glob.glob(os.path.join(root, sub, "raw/runs/*/fetch.cdx"))):
            run = os.path.basename(os.path.dirname(cdx))
            with open(cdx, encoding="utf-8", errors="replace") as f:
                for line in f:
                    t = line.rstrip("\n").split(" ")
                    if len(t) < 9 or line.startswith(" CDX"):
                        continue
                    part = os.path.basename(t[9]) if len(t) > 9 and re.fullmatch(r"fetch(-\d+)?\.warc\.gz", os.path.basename(t[9])) else "fetch.warc.gz"
                    warc = f"{sub}raw/runs/{run}/{part}"
                    in_git = warc in tracked
                    status = t[4]
                    self._add(t[0], {"repo": repo, "commit": commit, "kind": "warc" if in_git else "cdx-only",
                                     "status": status, "redirect": t[6] if t[6] != "-" else "",
                                     "location": f"{warc}@{t[8]}", "readable": in_git and status.startswith("2")})
        for meta in sorted(glob.glob(os.path.join(root, sub, "structures/**/meta.json"), recursive=True)):
            try:
                m = json.load(open(meta, encoding="utf-8"))
            except Exception:
                continue
            src = m.get("source") if isinstance(m, dict) else None
            if not isinstance(src, dict):
                continue
            uri = src.get("uri") or src.get("url")
            if isinstance(uri, str) and uri.startswith("http"):
                status = str(src.get("status", "200"))
                self._add(uri, {"repo": repo, "commit": commit, "kind": "structure", "status": status, "redirect": "",
                                "location": os.path.relpath(os.path.dirname(meta), root),
                                "readable": status.startswith("2")})
        # The pages browser runs' steps ended at, each with its page text in git (the steps' witnesses).
        steps = set(git(root, "ls-files", f"{sub}raw/runs/*/steps/*.text.txt", f"{sub}raw/runs/*/steps/*.aria.yaml",
                        f"{sub}derived/step-text-from-html/*/*.html.txt").split())
        for acts in sorted(glob.glob(os.path.join(root, sub, "raw/runs/*/actions.jsonl"))):
            run = os.path.basename(os.path.dirname(acts))
            with open(acts, encoding="utf-8", errors="replace") as f:
                for line in f:
                    try:
                        a = json.loads(line)
                        n = int(a.get("step"))
                    except Exception:
                        continue
                    url = a.get("url") or ""
                    files = [f"{sub}raw/runs/{run}/steps/{n:03d}.{k}" for k in ("text.txt", "aria.yaml")] + \
                            [f"{sub}derived/step-text-from-html/{run}/{n:03d}.html.txt"]
                    files = [x for x in files if x in steps]
                    if not url.startswith("http") or not files:
                        continue
                    status = str(a.get("http_status") or "200")
                    h = {"repo": repo, "commit": commit, "kind": "step", "status": status, "redirect": "",
                         "location": files[0], "readable": a.get("outcome") in (None, "ok") and status.startswith("2")}
                    self._add(url, h)
                    # Shopify's help links its admin without a store (admin.shopify.com/settings/payments), and the
                    # admin opens that address in the signed-in store: a store's page is held for it too
                    m = re.match(r"^(https://admin\.shopify\.com)/store/[^/?#]+(/.*)?$", url)
                    if m:
                        self._add(m.group(1) + (m.group(2) or "/"), dict(h))
        # What runs' pages received, saved in git: each saved body by the address it was received from.
        saved = set(git(root, "ls-files", f"{sub}raw/runs/*/responses/*", f"{sub}raw/runs/*/answers/*").split())
        for f_name, kind in (("responses.jsonl", "responses"), ("answers.jsonl", "answers")):
            for lst in sorted(glob.glob(os.path.join(root, sub, "raw/runs/*", f_name))):
                run = os.path.basename(os.path.dirname(lst))
                with open(lst, encoding="utf-8", errors="replace") as f:
                    for line in f:
                        try:
                            o = json.loads(line)
                        except Exception:
                            continue
                        loc = f"{sub}raw/runs/{run}/{o.get('file', '')}"
                        host = o.get("host") or ""
                        path = o.get("path") if kind == "responses" else o.get("endpoint")
                        if loc not in saved or not host or not path:
                            continue
                        status = str(o.get("status") or "200")
                        self._add(f"https://{host}{path}", {"repo": repo, "commit": commit, "kind": "answer",
                                                             "status": status, "redirect": "", "location": loc,
                                                             "readable": status.startswith("2")})
        # Corpora held as rows, one address per row: Salla's help-centre articles (observed-sa item 11).
        for items in sorted(glob.glob(os.path.join(root, "structures/salla/help-articles/*/items.jsonl"))):
            lang_dir = os.path.relpath(os.path.dirname(items), root)
            with open(items, encoding="utf-8") as f:
                for line in f:
                    try:
                        r = json.loads(line)
                    except Exception:
                        continue
                    if r.get("url"):
                        self._add(r["url"], {"repo": repo, "commit": commit, "kind": "structure", "status": "200",
                                             "redirect": "", "readable": True,
                                             "location": f"{lang_dir}/texts.jsonl (position {r.get('position')})"})

    def _capture(self, run, skm):
        mf = os.path.join(run, "manifest.tsv")
        if not os.path.exists(mf):
            return
        rel = os.path.relpath(run, skm) if skm else run
        with open(mf, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                status = r.get("http_browser") or r.get("http_raw") or ""
                ok = r.get("result") == "captured" and bool(r.get("text_file") or r.get("primary_file"))
                if ok and r.get("text_file"):     # a capture whose text came out empty is held but not readable
                    tp = os.path.join(run, r.get("dir", ""), r["text_file"])
                    ok = os.path.isfile(tp) and bool(open(tp, encoding="utf-8", errors="replace").read(4096).strip())
                h = {"repo": "sharrwah-knowledge-map", "commit": "", "kind": "capture", "status": status, "redirect": "",
                     "location": f"{rel}/{r.get('dir', '')}/{r.get('text_file') or r.get('primary_file')}",
                     "readable": ok and status.startswith("2")}
                holdings = [h]
                # A page the browser was refused (a bot challenge) may still be held whole by the raw fetch: its body
                # is readable where the raw fetch succeeded and the body holds more than a challenge page
                raw_status = r.get("http_raw") or ""
                if not h["readable"] and raw_status.startswith("2"):
                    for raw in sorted(glob.glob(os.path.join(run, r.get("dir", ""), "raw*.html"))):
                        if os.path.getsize(raw) > 20000:
                            holdings.append({"repo": "sharrwah-knowledge-map", "commit": "", "kind": "capture",
                                             "status": raw_status, "redirect": "", "readable": True,
                                             "location": f"{rel}/{r.get('dir', '')}/{os.path.basename(raw)} "
                                                         f"(the raw fetch; read it with method/quote_check.py --text)"})
                            break
                for u in {r.get("url", ""), r.get("final_url", "")}:
                    if u:
                        for x in holdings:
                            self._add(u, dict(x))

    def lookup(self, url, _hops=0):
        """Every holding of an address, best first. A held redirect is followed once."""
        seen, out = set(), []
        for k in url_keys(url):
            for h in self.by_key.get(k, []):
                key = (h["repo"], h["location"])
                if key not in seen:
                    seen.add(key)
                    out.append(h)
        if _hops == 0:
            for h in list(out):
                if h["status"].startswith("3") and h["redirect"]:
                    target = urllib.parse.urljoin(h["url"], h["redirect"])
                    out += [dict(x, via=h["url"]) for x in self.lookup(target, 1)]
        return sorted(out, key=lambda h: (not h["readable"], RANK[h["kind"]]))

    def best(self, url):
        hs = self.lookup(url)
        return hs[0] if hs else None

def describe(h):
    where = f"{h['repo']}@{h['commit'][:8]}:" if h["commit"] else f"{h['repo']}:"
    return f"{where}{h['location']} ({h['kind']}, {h['status']})"

if __name__ == "__main__":
    # Usage: python3 -I method/held_index.py URL [URL ...]
    # Prints where each address is held, best readable form first. A "warc" location is read with
    # python3 -I method/warc_text.py <repository root> <location> --text
    import sys
    here = os.path.dirname(os.path.abspath(__file__))
    skm = os.path.dirname(here)
    held = Held({"observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa"),
                 "observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
                 "other-product-class": os.environ.get("OTHER_PRODUCT_CLASS", "/home/user/other-product-class"),
                 "sharrwah-knowledge-map": skm},
                sorted(glob.glob(os.path.join(skm, "evidence/product-class/runs/*"))))
    for u in sys.argv[1:]:
        hs = held.lookup(u)
        print(u)
        for h in hs or [None]:
            print("   not held" if h is None else f"   {'readable' if h['readable'] else 'not readable'}: {describe(h)}")
