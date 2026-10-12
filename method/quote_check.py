# Verbatim-quote checking, shared by the checkers: is a quote found, word for word, in its cited source?
# A source is a URL captured in one of the capture runs given, or a local path written as
# <repo>[@<commit>]:<path> for a repository named in roots (observed-sh, observed-sa, woocommerce-11.2.1,
# sharrwah-knowledge-map). Matching tries the text exactly, then with markup removed, then ignoring case and
# Arabic diacritics, after Unicode and whitespace normalization.
import csv, html, io, json, os, re, subprocess, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

csv.field_size_limit(10**9)

BIDI = dict.fromkeys(map(ord, "​‌‍‎‏‪‫‬‭‮⁦⁧⁨⁩﻿ـ"), None)
SUBS = [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"),
        ("−", "-"), (" ", " "), (" ", " "), (" ", " ")]
HARAKAT = re.compile(r"[ً-ْٰ]")

def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s)).translate(BIDI)
    for a, b in SUBS:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()

def md_plain(s):
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)        # links and images -> their text
    s = re.sub(r"<[^>]{1,200}>", " ", s)                     # inline tags
    s = s.replace("**", "").replace("__", "").replace("`", "").replace("\\", "")
    s = re.sub(r"(^|\s)#{1,6}\s", r"\1", s)
    s = s.replace("|", " ")
    return re.sub(r"\s+", " ", s).strip()

def variants(s):
    n = norm(s)
    p = md_plain(n)
    return [("exact", n), ("markup removed", p), ("case and diacritics ignored", HARAKAT.sub("", p).casefold())]

def html_text(raw):
    # Block tags break text; inline tags (links, emphasis) vanish so the sentence they sit in stays whole.
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)</?(p|div|li|ul|ol|br|hr|h[1-6]|tr|td|th|table|thead|tbody|section|article|header|footer|nav|main|aside|blockquote|pre|dd|dt|dl|figure|figcaption)\b[^>]*>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", "", raw)
    return raw

def json_strings(o, out):
    if isinstance(o, dict):
        for v in o.values(): json_strings(v, out)
    elif isinstance(o, list):
        for v in o: json_strings(v, out)
    elif isinstance(o, str):
        out.append(o)
    return out

def json_unescaped(raw):
    out = []
    for line in raw.splitlines():
        try:
            out.append("\n".join(json_strings(json.loads(line), [])))
        except Exception:
            pass
    for line in raw.splitlines():
        try:
            out.append(json.dumps(json.loads(line), ensure_ascii=False))
        except Exception:
            out.append(line)
    try:
        out.append(json.dumps(json.loads(raw), ensure_ascii=False))
    except Exception:
        pass
    return "\n".join(out)

def shingle_share(q, src, k=6):
    w = q.split()
    if len(w) <= k:
        return 1.0 if q in src else 0.0
    sh = [" ".join(w[i:i + k]) for i in range(len(w) - k + 1)]
    return sum(1 for s in sh if s in src) / len(sh)

class Sources:
    def __init__(self, roots, captures=()):
        self.roots, self.cache, self.manifest = roots, {}, {}
        for cap in captures:
            mf = os.path.join(cap, "manifest.tsv")
            if not os.path.exists(mf):
                continue
            with open(mf, encoding="utf-8", newline="") as f:
                for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                    self.manifest.setdefault(r["url"].split("#")[0], (cap, r))

    def local_texts(self, source, locator=""):
        m = re.match(r"^([a-z0-9.-]+)(?:@([0-9a-f]{6,40}))?:(.+)$", source)
        if not m or m.group(1) not in self.roots:
            return None, "not a known local source"
        root, commit, rel = self.roots[m.group(1)], m.group(2), m.group(3).strip().lstrip("/")
        rel = re.sub(r"[#:]L?\d+(-L?\d+)?$", "", rel)  # a trailing line locator is not part of the path
        if rel.endswith(".warc.gz"):
            return self.warc_texts(root, commit, rel, locator)
        if commit:
            p = subprocess.run(["git", "-C", root, "show", f"{commit}:{rel}"], capture_output=True)
            if p.returncode != 0:
                return None, f"git show {commit}:{rel} failed in {root}"
            raw = p.stdout.decode("utf-8", errors="replace")
        else:
            fp = os.path.join(root, rel)
            if not os.path.isfile(fp):
                return None, f"no file {fp}"
            raw = open(fp, encoding="utf-8", errors="replace").read()
        texts = [raw]
        if rel.endswith((".json", ".jsonl")):
            texts.append(json_unescaped(raw))
        if rel.endswith((".html", ".htm", ".mhtml")):
            texts.append(html_text(raw))
        return texts, ""

    def warc_texts(self, root, commit, rel, locator):
        """A record of a fetch archive, at the offset the citation's locator gives."""
        from warc_text import read_record_fp, html_text as warc_html_text
        off = re.search(r"(\d{3,})", locator or "")
        if not off:
            return None, "a fetch archive is cited with its record's offset as the locator"
        if commit:
            p = subprocess.run(["git", "-C", root, "show", f"{commit}:{rel}"], capture_output=True)
            if p.returncode != 0:
                return None, f"git show {commit}:{rel} failed in {root}"
            fp = io.BytesIO(p.stdout)
        else:
            path = os.path.join(root, rel)
            if not os.path.isfile(path):
                return None, f"no file {path}"
            fp = open(path, "rb")
        try:
            warc, status, headers, body = read_record_fp(fp, int(off.group(1)))
        except Exception as e:
            return None, f"no readable record at offset {off.group(1)}: {e}"
        cs = re.search(r"charset=([\w-]+)", headers.get("content-type", ""))
        text = body.decode(cs.group(1) if cs else "utf-8", "replace")
        return [text, html_text(text), warc_html_text(text)], ""

    def web_texts(self, url):
        key = url.split("#")[0]
        if key not in self.manifest:
            return None, "not captured"
        cap, r = self.manifest[key]
        d = os.path.join(cap, r["dir"])
        texts = []
        for name in sorted(os.listdir(d)):  # raw.*, raw-browser.*, rendered.html, text.txt
            fp = os.path.join(d, name)
            if not os.path.isfile(fp) or not name.startswith(("raw", "rendered", "text")):
                continue
            if name.endswith((".pdf", ".bin", ".png", ".jpg", ".jpeg", ".gif", ".webp")):
                continue
            raw = open(fp, encoding="utf-8", errors="replace").read()
            texts.append(raw)
            if name.endswith(".html"):
                texts.append(html_text(raw))
            if name.endswith(".json"):
                texts.append(json_unescaped(raw))
        if not texts:
            return None, f"captured as '{r['result']}' with no readable text"
        return texts, ""

    def texts(self, source, locator=""):
        key = (source, locator if source.endswith(".warc.gz") else "")
        if key in self.cache:
            return self.cache[key]
        res = self.web_texts(source) if re.match(r"^https?://", source) else self.local_texts(source, locator)
        if res[0] is not None:
            res = ([v for t in res[0] for v in variants(t)], res[1])
        self.cache[key] = res
        return res

    def check_quote(self, quote, source, locator=""):
        texts, why = self.texts(source, locator)
        if texts is None:
            return "unresolved", why, ""
        qv = variants(quote)
        for (kind, q), level in zip(qv, range(3)):
            for (tkind, t) in texts:
                if tkind == kind and q and q in t:
                    return ("found" if level == 0 else f"found ({kind})"), "", ""
        best = max((shingle_share(qv[2][1], t) for tk, t in texts if tk == "case and diacritics ignored"), default=0.0)
        return "not found", "", f"{best:.2f}"
