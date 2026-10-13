# What observed-sa, observed-sh and this repository's capture runs hold, by address, and in what readable form.
# PLAN.md Stage 0: before a gap goes to anyone, its route is checked against what is held.
#
# Readable forms, best first:
#   structure  a structure in observed-sa or observed-sh whose meta.json names the address (text or rows in git)
#   capture    a page in this repository's evidence/product-class/runs, with its text file
#   warc       a record in a fetch archive that is in git (read it with method/warc_text.py)
#   cdx-only   an index line whose archive is not in git: held, but not readable from the repository
import csv, glob, json, os, re, subprocess, unicodedata, urllib.parse
from collections import defaultdict

csv.field_size_limit(10**9)
RANK = {"structure": 0, "capture": 1, "warc": 2, "cdx-only": 3}
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
        skm = roots.get("sharrwah-knowledge-map")
        for run in capture_runs:
            self._capture(run, skm)

    def _add(self, url, h):
        h["url"] = url
        for k in url_keys(url):
            self.by_key[k].append(h)

    def _repo(self, repo, root):
        commit = git(root, "rev-parse", "HEAD").strip()
        self.commits[repo] = commit
        tracked = set(git(root, "ls-files", "raw/runs/*/fetch.warc.gz").split())
        for cdx in sorted(glob.glob(os.path.join(root, "raw/runs/*/fetch.cdx"))):
            run = os.path.basename(os.path.dirname(cdx))
            warc = f"raw/runs/{run}/fetch.warc.gz"
            in_git = warc in tracked
            with open(cdx, encoding="utf-8", errors="replace") as f:
                for line in f:
                    t = line.rstrip("\n").split(" ")
                    if len(t) < 9 or line.startswith(" CDX"):
                        continue
                    status = t[4]
                    self._add(t[0], {"repo": repo, "commit": commit, "kind": "warc" if in_git else "cdx-only",
                                     "status": status, "redirect": t[6] if t[6] != "-" else "",
                                     "location": f"{warc}@{t[8]}", "readable": in_git and status.startswith("2")})
        for meta in sorted(glob.glob(os.path.join(root, "structures/**/meta.json"), recursive=True)):
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
                for u in {r.get("url", ""), r.get("final_url", "")}:
                    if u:
                        self._add(u, dict(h))

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
                 "sharrwah-knowledge-map": skm},
                sorted(glob.glob(os.path.join(skm, "evidence/product-class/runs/*"))))
    for u in sys.argv[1:]:
        hs = held.lookup(u)
        print(u)
        for h in hs or [None]:
            print("   not held" if h is None else f"   {'readable' if h['readable'] else 'not readable'}: {describe(h)}")
