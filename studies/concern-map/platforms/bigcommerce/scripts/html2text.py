# Plain text of an HTML file, block tags as newlines (same idea as the checker's html_text). Usage: python3 -I html2text.py FILE
import re, sys, html
raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
raw = re.sub(r"(?is)</?(p|div|li|ul|ol|br|hr|h[1-6]|tr|td|th|table|thead|tbody|section|article|header|footer|nav|main|aside|blockquote|pre|dd|dt|dl|figure|figcaption|button|summary|details)\b[^>]*>", "\n", raw)
raw = re.sub(r"(?s)<[^>]+>", "", raw)
for line in html.unescape(raw).splitlines():
    line = re.sub(r"\s+", " ", line).strip()
    if line: print(line)
