# Extract method, path, tags and scopes from the fetched Apidog .md endpoint pages.
import sys, os, re, csv
api_dir, urls_tsv, out = sys.argv[1], sys.argv[2], sys.argv[3]
crumbs = {}
for line in open(sys.argv[4], encoding="utf-8"):
    m = re.match(r"^- (.*?)\[([^\]]*)\]\((https://docs\.zid\.sa/([^)]*)\.md)\)", line)
    if m: crumbs[m.group(4)] = (m.group(1).strip(), m.group(2))
rows = []
for line in open(urls_tsv, encoding="utf-8"):
    url, slug = line.rstrip("\n").split("\t")
    p = os.path.join(api_dir, slug + ".md")
    if not os.path.exists(p): continue
    t = open(p, encoding="utf-8").read()
    title = (re.search(r"^# (.+)$", t, re.M) or [None, ""])[1]
    pm = re.search(r"^paths:\n  (/\S+):\n    (get|post|put|patch|delete):", t, re.M)
    path, method = (pm.group(1), pm.group(2).upper()) if pm else ("", "")
    tags = re.findall(r"^      tags:\n((?:        - .+\n)+)", t, re.M)
    tag = ""
    if tags:
        tl = [x.strip()[2:] for x in tags[0].splitlines()]
        tag = " | ".join(tl)
    acc = re.search(r'<Accordion title="[^"]*Scopes[^"]*"[^>]*>(.*?)</Accordion>', t, re.S)
    scopes = []
    if acc:
        scopes = re.findall(r"`([a-z_.]+)`\s*-\s*([^\n`]+)", acc.group(1))
    crumb = crumbs.get(slug, ("", ""))[0]
    rows.append([slug, crumb, title, method, path, tag, "; ".join(f"{a} - {b.strip()}" for a, b in scopes)])
with open(out, "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["slug", "crumb", "title", "method", "path", "tags", "scopes"])
    w.writerows(rows)
print(len(rows))
