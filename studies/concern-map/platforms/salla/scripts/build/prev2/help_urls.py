# List help.salla.sa article URLs from the held sitemaps, with decoded slugs and lastmod.
# Usage: python3 -I help_urls.py SITEMAP_XML [...]
import sys, re, urllib.parse

for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r"<url>(.*?)</url>", text, re.S):
        block = m.group(1)
        loc = re.search(r"<loc>(.*?)</loc>", block)
        lm = re.search(r"<lastmod>(.*?)</lastmod>", block)
        if not loc:
            continue
        u = loc.group(1).strip()
        print("\t".join([path.rsplit("/", 1)[-1], lm.group(1).strip() if lm else "", urllib.parse.unquote(u), u]))
