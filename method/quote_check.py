# Verbatim-quote checking, shared by the checkers: is a quote found, word for word, in its cited source?
# A source is a URL captured in one of the capture runs given, or a local path written as
# <repo>[@<commit>]:<path> for a repository named in roots (observed-sh, observed-sa, woocommerce-11.2.1,
# sharrwah-knowledge-map). Matching tries the text exactly, then with markup removed, then ignoring case and
# Arabic diacritics, after Unicode and whitespace normalization.
#
# Usage as a command, to test a statement or a quote before writing it:
#   python3 -I method/quote_check.py SOURCE LOCATOR TEXT [CAPTURE_RUN ...]
#   python3 -I method/quote_check.py --batch FILE [CAPTURE_RUN ...]
# SOURCE and LOCATOR as a citation gives them (LOCATOR matters only for a fetch archive: its record's offset).
# Prints "found", "found (<how>)" or "not found", with the share of the text's six-word runs the source holds.
# --batch reads FILE's lines, each SOURCE<tab>LOCATOR<tab>TEXT, and tests them all in one process, reading each
# source once: much faster for several quotes from one large file.
#   python3 -I method/quote_check.py --text SOURCE [LOCATOR] [CAPTURE_RUN ...]
# prints the source's text with its markup removed, as the checker matches quotes against it: a page held only as
# raw HTML reads as text, so it costs a reader far less than the HTML.
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
    s = re.sub(r"\s+([.,;:!?،؛])", r"\1", s)      # a tag removed before punctuation leaves no space, on both sides
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
                    self.manifest.setdefault(r["url"].split("#")[0], []).append((cap, r))   # every capture of it

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
            data = p.stdout
        else:
            fp = os.path.join(root, rel)
            if not os.path.isfile(fp):
                return None, f"no file {fp}"
            data = open(fp, "rb").read()
        if rel.lower().endswith(".pdf"):           # a PDF is read as its text, through pdftotext
            p = subprocess.run(["pdftotext", "-q", "-", "-"], input=data, capture_output=True, timeout=120)
            if p.returncode != 0:
                return None, f"pdftotext could not read {rel}"
            data = p.stdout
        raw = data.decode("utf-8", errors="replace")
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
        texts = [text, html_text(text), warc_html_text(text)]
        if "json" in headers.get("content-type", "").lower():   # its strings decoded, as a held .json file's are
            texts.append(json_unescaped(text))
        return texts, ""

    def web_texts(self, url, with_origin=False):
        """The texts of every capture of the address: a quote is found if any capture holds it, since an earlier
        capture may hold an empty shell where a later one holds the page. With with_origin, each text comes with
        where it came from: "shown" for the page as it rendered (its visible text, text.txt, and the text of the
        page after its scripts ran, rendered.html, hidden parts such as a closed FAQ answer included), "source"
        for the markup as stored (the body as served, raw.* and raw-browser.*, and the rendered markup's scripts
        and data). The source can hold what the page doesn't show: zid.eg's Terms page holds the Saudi Terms in
        its body and its data, and its scripts show the Terms of Zid Egypt."""
        key = url.split("#")[0]
        if key not in self.manifest:            # the same page under its .md endpoint, or with or without a slash
            base = key[:-3] if key.endswith(".md") else key.rstrip("/")
            key = next((k for k in (base, base + ".md", base + "/") if k in self.manifest), key)
        if key not in self.manifest:
            return None, "not captured"
        texts, results = [], []
        for cap, r in self.manifest[key]:
            results.append(r.get("result", ""))
            d = os.path.join(cap, r["dir"])
            if not os.path.isdir(d):
                continue
            for name in sorted(os.listdir(d)):  # raw.*, raw-browser.*, rendered.html, text.txt, expanded.txt
                fp = os.path.join(d, name)
                if not os.path.isfile(fp) or not name.startswith(("raw", "rendered", "text", "expanded")):
                    continue
                if name.endswith((".pdf", ".bin", ".png", ".jpg", ".jpeg", ".gif", ".webp")):
                    continue
                raw = open(fp, encoding="utf-8", errors="replace").read()
                if name.startswith(("text", "expanded")):   # the page as first shown, and the lines a click shows
                    texts.append(("shown", raw))
                    continue
                texts.append(("source", raw))       # the markup as stored, its scripts and data included
                if name.endswith(".html"):          # the text of the page after its scripts ran, hidden parts too
                    texts.append(("shown" if name.startswith("rendered") else "source", html_text(raw)))
                if name.endswith(".json"):
                    texts.append(("source", json_unescaped(raw)))
        if not texts:
            return None, f"captured as '{'; '.join(results)}' with no readable text"
        return (texts if with_origin else [t for _, t in texts]), ""

    def texts(self, source, locator=""):
        off = re.search(r"(\d{3,})", locator or "") if source.endswith(".warc.gz") else None
        key = (source, off.group(1) if off else (locator if source.endswith(".warc.gz") else ""))   # a record, by offset
        if key in self.cache:
            return self.cache[key]
        if re.match(r"^https?://", source):
            res = self.web_texts(source, with_origin=True)
            if res[0] is not None:
                res = ([(k, v, o) for o, t in res[0] for k, v in variants(t)], res[1])
        else:
            res = self.local_texts(source, locator)
            if res[0] is not None:
                res = ([(k, v, "file") for t in res[0] for k, v in variants(t)], res[1])
        self.cache[key] = res
        return res

    def check_quote(self, quote, source, locator=""):
        texts, why = self.texts(source, locator)
        if texts is None:
            return "unresolved", why, ""
        qv = variants(quote)
        # a capture that rendered the page: its visible text runs past 1,500 characters, where a failed render
        # shows an error text or nothing
        rendered = any(o == "shown" and k == "exact" and len(re.sub(r"\s+", "", t)) > 1500 for k, t, o in texts)
        for (kind, q), level in zip(qv, range(3)):
            hits = {o for (tkind, t, o) in texts if tkind == kind and q and q in t}
            if hits:
                res = "found" if level == 0 else f"found ({kind})"
                if hits == {"source"} and rendered:  # in the markup as stored, but not in the page as it renders
                    res += " in the page's source only"
                return res, "", ""
        best = max((shingle_share(qv[2][1], t) for tk, t, o in texts if tk == "case and diacritics ignored"),
                   default=0.0)
        return "not found", "", f"{best:.2f}"


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--text":
        src, loc = sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 and not os.path.isdir(sys.argv[3]) else "")
        caps = [a for a in sys.argv[3:] if os.path.isdir(a)]
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        S = Sources({"observed-sh": "/home/user/observed-sh", "observed-sa": "/home/user/observed-sa",
                     "other-product-class": "/home/user/other-product-class",
                     "woocommerce-11.2.1": "/home/user/woocommerce-release/11.2.1/woocommerce",
                     "sharrwah-knowledge-map": here}, caps)
        texts, why = (S.web_texts(src) if re.match(r"^https?://", src) else S.local_texts(src, loc))
        if texts is None:
            sys.exit(f"not readable: {why}")
        # a capture may hold several files (raw, rendered, text): print the one with the most text, so that a
        # page's "Loading" shell gives way to its rendered text
        cands = [html_text(t) if re.search(r"(?i)<(html|body|div|p|span)\b", t) else t for t in texts]
        txt = max(cands, key=lambda t: len(re.sub(r"\s+", "", t)))
        print(re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", txt)).strip())
        sys.exit(0)
    if len(sys.argv) < 4 and not (len(sys.argv) >= 3 and sys.argv[1] == "--batch"):
        sys.exit("usage: quote_check.py SOURCE LOCATOR TEXT [CAPTURE_RUN ...]; or --batch FILE [CAPTURE_RUN ...]; "
                 "or --text SOURCE [LOCATOR] [CAPTURE_RUN ...]")
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    roots = {"observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
             "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa"),
             "woocommerce-11.2.1": os.environ.get("WOO_RELEASE", "/home/user/woocommerce-release/11.2.1/woocommerce"),
             "sharrwah-knowledge-map": here}
    def show(res, why, share):
        return res + (f"; {why}" if why else "") + (f"; {share} of its six-word runs are in the source" if share else "")
    if sys.argv[1] == "--batch":
        S = Sources(roots, sys.argv[3:])
        for n, line in enumerate(open(sys.argv[2], encoding="utf-8"), start=1):
            if not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) != 3:
                print(f"{n}\tline has {len(parts)} fields, not 3 (SOURCE, LOCATOR, TEXT)")
                continue
            print(f"{n}\t" + show(*S.check_quote(parts[2], parts[0], parts[1])))
    else:
        print(show(*Sources(roots, sys.argv[4:]).check_quote(sys.argv[3], sys.argv[1], sys.argv[2])))
