# Print sentences from the main text of captured pages that match a regex.
# Usage: python3 -I sentences.py REGEX FILE [FILE...]
import re, sys
rx = re.compile(sys.argv[1], re.I)
for fn in sys.argv[2:]:
    t = open(fn).read()
    title = t.split(" Documentation - ")[0].split(" - WooCommerce")[0][:60]
    i = t.find(title, len(title)); j = t.find("Was this guide helpful", i)
    body = t[i:j if j > 0 else len(t)]
    sents = re.split(r"(?<=[.!?])\s+(?=[A-Z])", body)
    hits = [s for s in sents if rx.search(s)]
    if hits:
        print("==", fn[:90])
        for s in hits[:12]:
            print("   -", s[:330])
