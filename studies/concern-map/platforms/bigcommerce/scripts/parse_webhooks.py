# Extract webhook event scopes from the event-reference markdown pages.
# Usage: python3 -I parse_webhooks.py OUT_TSV PAGE.md...
import re, sys
out = open(sys.argv[1], "w", encoding="utf-8")
out.write("page\tsection\tsubsection\tscope\tdescription\n")
for p in sys.argv[2:]:
    sec = sub = ""
    for line in open(p, encoding="utf-8"):
        if line.startswith("## "):
            sec, sub = line[3:].strip(), ""
        elif line.startswith("### "):
            sub = line[4:].strip()
        m = re.match(r"^\|\s*`?((?:store|b2b)/[^`|\s]*)`?(\\\*)?\s*\|\s*(.*?)\s*\|", line)
        if m:
            scope = m.group(1).replace("\\*", "*").replace("\\_", "_")
            out.write("\t".join([p.split("/")[-1], sec, sub, scope, m.group(3).replace("\t", " ")]) + "\n")
