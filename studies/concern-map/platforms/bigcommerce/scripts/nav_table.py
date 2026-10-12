# Table of API reference navigation pages: nav title (from llms.txt), url, page H1, first prose line.
# Usage: python3 -I nav_table.py LLMS_TXT APIREF_DIR OUT_TSV
import re, sys, os
llms, d, out = sys.argv[1:4]
lines = open(llms, encoding="utf-8").read().splitlines()[535:645]
o = open(out, "w", encoding="utf-8")
o.write("line\tnav_title\turl\th1\tfirst_line\n")
for i, l in enumerate(lines, start=536):
    m = re.match(r"^- \[([^\]]*)\]\((https://docs\.bigcommerce\.com/developer/api-reference/[^)]*\.md)\)", l)
    if not m: continue
    title, url = m.groups()
    n = url.replace("https://docs.bigcommerce.com/developer/api-reference/", "")[:-3].replace("/", "_")
    p = os.path.join(d, n + ".md")
    h1 = first = ""
    if os.path.exists(p):
        body = open(p, encoding="utf-8").read().splitlines()
        seen_h1 = False
        for b in body:
            if b.startswith("# ") and not seen_h1:
                h1, seen_h1 = b[2:].strip(), True; continue
            if seen_h1 and b.strip() and not b.startswith(("#", "```", "|", "![", "[![")):
                first = b.strip(); break
    o.write("\t".join([str(i), title, url, h1, first[:400].replace("\t", " ")]) + "\n")
