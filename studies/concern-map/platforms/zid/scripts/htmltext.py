# Text of a raw HTML file the way check_concern_map.py sees it (html_text + norm per line), for reading.
import sys, re, html, unicodedata
raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
raw = re.sub(r"(?is)</?(p|div|li|ul|ol|br|hr|h[1-6]|tr|td|th|table|thead|tbody|section|article|header|footer|nav|main|aside|blockquote|pre|dd|dt|dl|figure|figcaption)\b[^>]*>", "\n", raw)
raw = re.sub(r"(?s)<[^>]+>", "", raw)
raw = html.unescape(raw)
for line in raw.split("\n"):
    line = re.sub(r"[ \t\r\f\v]+", " ", line).strip()
    if line:
        print(line)
