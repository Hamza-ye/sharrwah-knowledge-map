# Find candidate reason sentences (because / so that / in order to / to ensure / designed to / meant to) that mention a keyword.
# Usage: python3 -I reason_search.py KEYWORD_REGEX
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qcheck
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
kw = re.compile(sys.argv[1], re.I)
rx = re.compile(r"\b(because|so that|in order to|to ensure|designed to|is meant to|are meant to|the reason|this is why|that's why|to help|to prevent|to protect)\b", re.I)
files = glob.glob(os.path.join(W, "work", "txt", "*.txt"))
for fn in glob.glob(os.path.join(W, "fetched", "*")):
    if fn.endswith((".html", ".md")):
        files.append(fn)
for fn in sorted(files):
    raw = open(fn, encoding="utf-8", errors="replace").read()
    t = qcheck.norm(qcheck.html_text(raw)) if fn.endswith(".html") else qcheck.norm(raw)
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", t):
        if rx.search(s) and kw.search(s) and len(s) < 400:
            print(os.path.basename(fn)[:60], "|", s[:300])
