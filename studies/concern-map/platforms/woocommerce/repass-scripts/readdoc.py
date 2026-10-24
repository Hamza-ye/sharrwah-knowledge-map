# Print the dates and main text of a fetched woocommerce.com page (raw HTML), normalized as the checker does.
# Usage: python3 -I readdoc.py FILE [CHARS] [START_TEXT]
import os, re, sys, textwrap, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qcheck
raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
n = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
dm = re.findall(r'"dateModified":"([^"]+)"', raw)
dp = re.findall(r'"datePublished":"([^"]+)"', raw)
title = re.search(r"<title>(.*?)</title>", raw, re.S)
print("title:", html.unescape(title.group(1)).strip() if title else None, "| published:", dp[:1], "| modified:", dm[:1])
body = raw
m = re.search(r'(?is)<(article|main)\b', raw)
t = qcheck.norm(qcheck.html_text(raw))
start = sys.argv[3] if len(sys.argv) > 3 else None
if start:
    i = t.find(start)
else:
    h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", raw)
    h = qcheck.norm(re.sub(r"<[^>]+>", "", h1.group(1))) if h1 else ""
    i = t.find(h) if h else 0
print("len", len(t), "start", i)
print("\n".join(textwrap.wrap(t[max(i, 0):max(i, 0) + n], 250)))
