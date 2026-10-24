# Quote matching as in method/check_concern_map.py (norm, md_plain, variants, html_text, json_unescaped),
# applied to local working copies, so quotes can be checked before the capture run.
import html, json, os, re, unicodedata
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
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]{1,200}>", " ", s)
    s = s.replace("**", "").replace("__", "").replace("`", "").replace("\\", "")
    s = re.sub(r"(^|\s)#{1,6}\s", r"\1", s)
    s = s.replace("|", " ")
    return re.sub(r"\s+", " ", s).strip()
def variants(s):
    n = norm(s); p = md_plain(n)
    return [("exact", n), ("markup removed", p), ("case and diacritics ignored", HARAKAT.sub("", p).casefold())]
def html_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)</?(p|div|li|ul|ol|br|hr|h[1-6]|tr|td|th|table|thead|tbody|section|article|header|footer|nav|main|aside|blockquote|pre|dd|dt|dl|figure|figcaption)\b[^>]*>", "\n", raw)
    return re.sub(r"(?s)<[^>]+>", "", raw)
def json_strings(o, out):
    if isinstance(o, dict):
        for v in o.values(): json_strings(v, out)
    elif isinstance(o, list):
        for v in o: json_strings(v, out)
    elif isinstance(o, str): out.append(o)
    return out
def json_unescaped(raw):
    out = []
    for line in raw.splitlines():
        try: out.append("\n".join(json_strings(json.loads(line), [])))
        except Exception: pass
    for line in raw.splitlines():
        try: out.append(json.dumps(json.loads(line), ensure_ascii=False))
        except Exception: out.append(line)
    try: out.append(json.dumps(json.loads(raw), ensure_ascii=False))
    except Exception: pass
    return "\n".join(out)
_cache = {}
def texts_for(files):
    key = tuple(files)
    if key in _cache: return _cache[key]
    texts = []
    for fp in files:
        raw = open(fp, encoding="utf-8", errors="replace").read()
        texts.append(raw)
        if fp.endswith((".html", ".htm")): texts.append(html_text(raw))
        if fp.endswith(".json"): texts.append(json_unescaped(raw))
    vs = [v for t in texts for v in variants(t)]
    _cache[key] = vs
    return vs
def check(quote, files):
    vs = texts_for(files)
    for (kind, q), level in zip(variants(quote), range(3)):
        for (tk, t) in vs:
            if tk == kind and q and q in t:
                return "found" if level == 0 else f"found ({kind})"
    return "not found"
