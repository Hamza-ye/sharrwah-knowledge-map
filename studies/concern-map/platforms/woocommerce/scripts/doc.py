# Print a fetched page's dates and main text (woocommerce.com docs: from the breadcrumb to the footer).
# Usage: python3 -I doc.py FETCHED_BASENAME_WITHOUT_EXT [max_chars]
import re, sys, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fetched")
base = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 12000
h = open(os.path.join(D, base + ".html"), encoding="utf-8", errors="replace").read()
dates = {}
for k, rx in [("published", r'"datePublished":"([^"]+)"'), ("modified", r'"dateModified":"([^"]+)"'),
              ("meta_modified", r'article:modified_time" content="([^"]+)"'), ("meta_published", r'article:published_time" content="([^"]+)"')]:
    m = re.search(rx, h)
    if m: dates[k] = m.group(1)
print("DATES", dates)
t = open(os.path.join(D, base + ".txt"), encoding="utf-8").read()
lines = [l.strip() for l in t.split("\n") if l.strip()]
start = 0
for i, l in enumerate(lines):
    if " / Documentation / " in l or l.startswith(("Guides/", "Documentation / ")) or (" / " in l and l.split(" / ")[0] in ("WooPayments", "WooCommerce", "Documentation", "WooCommerce Shipping", "WooCommerce Tax", "Woo Marketplace")):
        start = i; break
end = len(lines)
for i in range(start, len(lines)):
    if lines[i] in ("30-day money-back guarantee", "Was this guide helpful for you?", "On this page"):
        end = i; break
out = "\n".join(l for l in lines[start:end] if l != "\u2191 Back to top")
print(out[:mx])
if len(out) > mx: print(f"[... {len(out) - mx} more chars]")
