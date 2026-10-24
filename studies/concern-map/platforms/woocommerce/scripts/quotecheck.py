# Show how a quote sits in a raw HTML file: which parts fall in separate text nodes.
# Usage: python3 -I quotecheck.py FILE.html "quote"
import html, re, sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import cite
t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
t = re.sub(r"<(script|style)\b.*?</\1>", " ", t, flags=re.S | re.I)
marked = cite.fold(html.unescape(re.sub(r"<[^>]+>", " ‖ ", t)))
q = cite.fold(sys.argv[2])
plain = re.sub(r"\s*‖\s*", " ", marked)
plain = cite.fold(plain)
print("in tag-stripped text:", q in plain)
if q in plain:
    # rebuild the marked span
    words = q.split(" ")
    i = marked.find(words[0])
    while i >= 0:
        seg = marked[i:i + len(q) * 2]
        if cite.fold(re.sub(r"\s*‖\s*", " ", seg)).startswith(q):
            print(seg[:len(q) + 60])
            break
        i = marked.find(words[0], i + 1)
