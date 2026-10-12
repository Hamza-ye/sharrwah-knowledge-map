# Print help.zid.sa links whose anchor text contains any of the given words. Usage: python3 -I findlinks.py WORD... < html files listed in argv after --
import sys, re, html, glob
words, files = [], []
args = sys.argv[1:]; i = args.index("--")
words, files = args[:i], args[i+1:]
seen = set()
for f in files:
    t = open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r'<a\b[^>]*href="(https://help\.zid\.sa/[^"#]*)"[^>]*>(.*?)</a>', t, re.S):
        txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
        if any(w in txt for w in words) and (m.group(1), txt) not in seen:
            seen.add((m.group(1), txt)); print(m.group(1), "|", txt)
