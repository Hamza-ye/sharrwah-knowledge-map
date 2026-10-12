# All scope identifiers named in the docs: accordion "Scopes" blocks in endpoint pages, plus `scope=` and `..._write`/`..._read` tokens in narrative pages.
import sys, os, re, json
api_dir, urls_tsv, docs_dir = sys.argv[1], sys.argv[2], sys.argv[3]
first = {}
order = []
def add(scope, slug, raw):
    if scope not in first:
        first[scope] = (slug, raw); order.append(scope)
for line in open(urls_tsv, encoding="utf-8"):
    url, slug = line.rstrip("\n").split("\t")
    p = os.path.join(api_dir, slug + ".md")
    if not os.path.exists(p): continue
    t = open(p, encoding="utf-8").read()
    for acc in re.finditer(r'<Accordion title="[^"]*[Ss]cope[^"]*"[^>]*>(.*?)</Accordion>', t, re.S):
        body = acc.group(1)
        raw = re.sub(r"\s+", " ", body).strip()
        for s in re.findall(r"`\s*([a-z_.]+)\s*`", body):
            add(s, slug, raw)
for f in sorted(os.listdir(docs_dir)):
    if not f.endswith(".md"): continue
    t = open(os.path.join(docs_dir, f), encoding="utf-8").read()
    for m in re.finditer(r"scope=([a-z_.,]+)|`([a-z]+(?:_[a-z]+)*_(?:read|write))`", t):
        s = m.group(1) or m.group(2)
        for x in s.split(","):
            add(x, "docs/" + f, t[max(0, m.start()-120):m.end()+60].replace("\n", " "))
for s in order:
    slug, raw = first[s]
    print(f"{s}\t{slug}\t{raw[:220]}")
