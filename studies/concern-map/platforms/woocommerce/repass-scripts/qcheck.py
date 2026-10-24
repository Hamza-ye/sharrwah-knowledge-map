# Quote checking that mirrors method/check_concern_map.py (same normalization, same sources).
# Library use: import qcheck; qcheck.check(quote, source) -> "found..." | "not found" | "unresolved: why"
# CLI:  python3 -I qcheck.py text SOURCE            print the normalized text the checker matches against (html variant)
#       python3 -I qcheck.py grep SOURCE REGEX [N]   show matches with N chars of context in the normalized text
#       python3 -I qcheck.py check SOURCE "QUOTE"
import csv, html, json, os, re, sys, unicodedata
csv.field_size_limit(10**9)
HERE = os.path.dirname(os.path.abspath(__file__))
WOO = "/home/user/woocommerce-release/11.2.1/woocommerce"
SKM = "/home/user/sharrwah-knowledge-map"
CAPTURES = [SKM + "/evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources"]
capdir = os.path.normpath(os.path.join(HERE, "..", "fetched", "capture"))
if os.path.isdir(capdir):
    CAPTURES += [os.path.join(capdir, d) for d in sorted(os.listdir(capdir))]

BIDI = dict.fromkeys(map(ord, "​‌‍‎‏‪‫‬‭‮⁦⁧⁨⁩﻿ـ"), None)
SUBS = [("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"),
        ("−", "-"), (" ", " "), (" ", " "), (" ", " ")]
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
    n = norm(s)
    p = md_plain(n)
    return [("exact", n), ("markup removed", p), ("case and diacritics ignored", HARAKAT.sub("", p).casefold())]

def html_text(raw):
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

MANIFEST = {}
for cap in CAPTURES:
    mf = os.path.join(cap, "manifest.tsv")
    if not os.path.exists(mf):
        continue
    with open(mf, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            MANIFEST.setdefault(r["url"].split("#")[0], (cap, r))

WORKING = {}
_log = os.path.normpath(os.path.join(HERE, "..", "fetched", "log.tsv"))
if os.path.exists(_log):
    with open(_log, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            if r["http_status"] == "200" and r["file"]:
                WORKING[r["url"]] = os.path.join(os.path.dirname(_log), r["file"])

def raw_texts(source):
    """The raw texts the checker would read for a source (before variants)."""
    if re.match(r"^https?://", source):
        key = source.split("#")[0]
        if key not in MANIFEST and key in WORKING and os.environ.get("ALLOW_WORKING") == "1":
            raw = open(WORKING[key], encoding="utf-8", errors="replace").read()
            return ([raw, html_text(raw)] if WORKING[key].endswith(".html") else [raw]), ""
        if key not in MANIFEST:
            return None, "not captured"
        cap, r = MANIFEST[key]
        d = os.path.join(cap, r["dir"])
        texts = []
        for name in sorted(os.listdir(d)):
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
        return (texts or None), ("" if texts else "no readable text")
    m = re.match(r"^([a-z0-9.-]+)(?:@([0-9a-f]{6,40}))?:(.+)$", source)
    if not m or m.group(1) not in ("woocommerce-11.2.1", "sharrwah-knowledge-map"):
        return None, "not a known local source"
    root = WOO if m.group(1) == "woocommerce-11.2.1" else SKM
    rel = re.sub(r"[#:]L?\d+(-L?\d+)?$", "", m.group(3).strip().lstrip("/"))
    fp = os.path.join(root, rel)
    if not os.path.isfile(fp):
        return None, f"no file {fp}"
    raw = open(fp, encoding="utf-8", errors="replace").read()
    texts = [raw]
    if rel.endswith((".json", ".jsonl")):
        texts.append(json_unescaped(raw))
    if rel.endswith((".html", ".htm")):
        texts.append(html_text(raw))
    return texts, ""

CACHE = {}
def source_variants(source):
    if source not in CACHE:
        t, why = raw_texts(source)
        CACHE[source] = ([v for x in t for v in variants(x)], why) if t else (None, why)
    return CACHE[source]

def check(quote, source):
    texts, why = source_variants(source)
    if texts is None:
        return "unresolved: " + why
    qv = variants(quote)
    for (kind, q), level in zip(qv, range(3)):
        for (tkind, t) in texts:
            if tkind == kind and q and q in t:
                return "found" if level == 0 else f"found ({kind})"
    return "not found"

if __name__ == "__main__":
    cmd, src = sys.argv[1], sys.argv[2]
    if cmd == "check":
        print(check(sys.argv[3], src))
    else:
        t, why = raw_texts(src)
        if t is None:
            print("unresolved:", why); sys.exit(1)
        # the longest text that is not raw markup: html_text of raw.html, or the rendered text, or the raw file
        cands = [x for x in t if not x.lstrip().startswith("<")] or t
        best = max((norm(x) for x in cands), key=len)
        if cmd == "text":
            print(best)
        elif cmd == "grep":
            n = int(sys.argv[4]) if len(sys.argv) > 4 else 200
            for m in re.finditer(sys.argv[3], best, flags=re.I):
                print("…", best[max(0, m.start() - n):m.end() + n].replace("\n", " "), "…\n")
