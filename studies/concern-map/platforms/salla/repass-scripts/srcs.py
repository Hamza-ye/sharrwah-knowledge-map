# Source readers for the Salla re-pass: working copies of web pages, held translation files,
# held JSONL lists and held text files in observed-sa@145f137. Used by build.py.
import os, re, json, subprocess, urllib.parse, html, unicodedata
from common import *
OSA_C = "145f137"

def wc_path(url):
    """Working-copy path written by fetch.py for a URL (rendered text or raw file)."""
    p = urllib.parse.urlparse(url)
    s = urllib.parse.unquote(p.path).strip("/").replace("/", "_") or "index"
    s = re.sub(r"[^\w؀-ۿ.\-]+", "-", s)[-120:]
    base = f"{SP}/fetched/{p.netloc}/{s}"
    return base + ("" if s.endswith(".md") else ".txt")

FIRST_CAP = {}
for r in rd(f"{CAP}/manifest.tsv"):
    FIRST_CAP[r["url"]] = f"{CAP}/{r['dir']}/text.txt"

def web_lines(url):
    f = wc_path(url)
    if not os.path.exists(f):
        f = FIRST_CAP.get(url)
    if not f or not os.path.exists(f):
        raise SystemExit(f"no working copy or first-run capture for {url}")
    return open(f, encoding="utf-8").read().split("\n"), f

_git = {}
def osa(path):
    if path not in _git:
        p = subprocess.run(["git", "-c", "safe.directory=*", "-C", OSA, "show", f"{OSA_C}:{path}"], capture_output=True)
        if p.returncode:
            raise SystemExit(f"git show failed: {path}")
        _git[path] = p.stdout.decode("utf-8")
    return _git[path]

def tr_value(lang, ns, key):
    o = json.loads(osa(f"structures/salla/dashboard-translations/{lang}/{ns}.json"))
    # keys are nested dicts; a key segment may itself hold dots, so walk greedily
    def walk(o, rest):
        if rest == "":
            return o
        if isinstance(o, dict):
            # try the longest key that prefixes rest
            for k in sorted(o.keys(), key=len, reverse=True):
                if rest == k:
                    return o[k]
                if rest.startswith(k + "."):
                    v = walk(o[k], rest[len(k) + 1:])
                    if v is not None:
                        return v
                if rest.startswith(k + "["):
                    m = re.match(re.escape(k) + r"\[(\d+)\](?:\.(.*))?$", rest)
                    if m and isinstance(o[k], list):
                        v = o[k][int(m.group(1))]
                        return v if m.group(2) is None else walk(v, m.group(2))
        return None
    v = walk(o, key)
    if not isinstance(v, str):
        raise SystemExit(f"no string at {lang}/{ns}.json {key}")
    return v

def line_of(text, needle):
    """1-based line number of the first line containing needle (whitespace-normalized)."""
    n = re.sub(r"\s+", " ", needle).strip()
    for i, l in enumerate(text.split("\n"), 1):
        if n in re.sub(r"\s+", " ", l):
            return i
    # JSON-escaped content (non-ASCII escaped) - search the json-dumped form
    esc = json.dumps(n, ensure_ascii=True)[1:-1]
    for i, l in enumerate(text.split("\n"), 1):
        if esc in l:
            return i
    return None

# ---------- normalization as in method/check_concern_map.py (kept in step with it) ----------
BIDI = dict.fromkeys(map(ord, "​‌‍‎‏‪‫‬‭‮⁦⁧⁨⁩﻿ـ"), None)
SUBS = [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("−", "-"), (" ", " "), (" ", " "), (" ", " ")]
HARAKAT = re.compile(r"[ً-ْٰ]")
def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s)).translate(BIDI)
    for a, b in SUBS:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()
def md_plain(s):
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]{1,200}>", " ", s)
    s = s.replace("**", "").replace("__", "").replace("`", "").replace("\\", "")
    s = re.sub(r"(^|\s)#{1,6}\s", r"\1", s)
    s = s.replace("|", " ")
    return re.sub(r"\s+", " ", s).strip()
def variants(s):
    n = norm(s); p = md_plain(n)
    return [n, p, HARAKAT.sub("", p).casefold()]
