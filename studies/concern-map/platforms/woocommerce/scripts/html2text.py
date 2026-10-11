# Visible text of a fetched HTML file (scripts, styles and templates dropped), for reading and quote checks.
# Usage: python3 -I html2text.py IN.html [OUT.txt]   (default OUT: IN with .txt)
import sys, re, html
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "template", "svg", "head"}
BLOCK = {"p", "div", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "td", "th", "table", "section",
         "article", "header", "footer", "nav", "br", "dt", "dd", "pre", "blockquote", "main", "aside", "details", "summary"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"\.[a-z]+$", "", src) + ".txt"
p = P()
p.feed(open(src, encoding="utf-8", errors="replace").read())
text = "".join(p.out)
text = re.sub(r"[ \t\r\f\v ]+", " ", text)
text = re.sub(r"\n\s*\n+", "\n\n", text)
open(dst, "w", encoding="utf-8").write(text.strip() + "\n")
print(dst, len(text))
