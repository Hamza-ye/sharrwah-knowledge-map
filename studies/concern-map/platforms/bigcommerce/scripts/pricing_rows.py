# Rows of the pricing comparison tables: first cell text, then each cell's text or image alt. Usage: python3 -I pricing_rows.py RAW_HTML OUT_TSV
import re, sys, html
s = open(sys.argv[1], encoding="utf-8", errors="replace").read()
s = re.sub(r'(?is)<script[^>]*>.*?</script>', ' ', s)
s = re.sub(r'(?is)<span role="tooltip"[^>]*>.*?</span>', ' ', s)
out = open(sys.argv[2], "w", encoding="utf-8")
for tr in re.findall(r'(?is)<tr\b.*?</tr>', s):
    cells = re.findall(r'(?is)<t[dh]\b.*?</t[dh]>', tr)
    vals = []
    for c in cells:
        alts = re.findall(r'alt="([^"]*)"', c)
        t = html.unescape(re.sub(r'(?s)<[^>]+>', ' ', c))
        t = re.sub(r'\s+', ' ', t.replace('ⓘ', '')).strip()
        vals.append(t if t else ('[img:' + ','.join(alts) + ']' if alts else ''))
    out.write("\t".join(vals) + "\n")
