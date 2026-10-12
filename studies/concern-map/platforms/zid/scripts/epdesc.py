# Print the description block of Apidog endpoint .md pages (for reading).
import sys, re
for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    m = re.search(r"^      description: (.*?)^      (operationId|tags|parameters|requestBody|responses):", t, re.S | re.M)
    print("=========", p.rsplit("/", 1)[-1])
    print(re.sub(r"\n\s*\n", "\n", m.group(1))[:2500] if m else "(no description block)")
