# Checks the verbatim quotes of a terms inventory (decisions/checks/*-terms-inventory.md) against the records they
# cite, by script (METHOD.md section 6). The inventory cites held records in short forms, such as `GQL:2447` for a
# line of Shopify's admin schema or `SA-en:807` for the Salla help article at position 807; its table at the top
# names each form's file.
#
# A quote is matched with method/quote_check.py's normalization, in the record cited on its own line first, then
# in a record cited within three lines, then anywhere in its section. Quoted strings on a line about searching
# ("Searched", "corpus tool", "grepped") are search strings, not quotes. What is left is listed for a person.
#
# Usage: python3 -I method/inventory_quotes.py decisions/checks/M1-terms-inventory.md
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import variants, json_unescaped

SH = "/home/user/observed-sh/structures/shopify/"
SA = "/home/user/observed-sa/structures/salla/"
LINE_FILES = {
    "RT": SH + "admin-route-titles-en/items.jsonl",
    "ROUTER": SH + "admin-router/items.jsonl",
    "GQL": SH + "admin-graphql-schema/2026-10/items.jsonl",
    "CLI": SH + "cli-extension-templates/cdn.shopify.com@templates.json/items.jsonl",
    "SMENU-en": SA + "dashboard-settings-menu/merchant@en/items.jsonl",
    "SMENU-ar": SA + "dashboard-settings-menu/merchant@ar/items.jsonl",
    "SNAV": SA + "dashboard-nav/prod/items.jsonl",
    "SSTAT": SA + "order-statuses/merchant@ar/items.jsonl",
    "SINV": SA + "invoice-settings/public-demo@en/items.jsonl",
    "SAPI": SA + "docs-operations/md-openapi/items.jsonl",
}
HC = SH + "help-center/help.shopify.com@en-ar/md/en/manual/"
ARTICLES = {"SA-en": SA + "help-articles/en/texts.jsonl", "SA-ar": SA + "help-articles/ar/texts.jsonl"}
AREAS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "studies", "proposals", "areas", "areas.tsv")
CITE = re.compile(r"`((?:RT|ROUTER|GQL|CLI|SMENU-en|SMENU-ar|SNAV|SSTAT|SINV|SAPI|SA-en|SA-ar):\d+(?:`[–-]`(?:\w+-?\w*):\d+)?"
                  r"|HC:[^`:]+(?::\d+)?|AREAS)`")
QUOTE = re.compile(r'"([^"]{3,})"')
SEARCH = re.compile(r"\bSearched\b|\bcorpus tool\b|\bgrepped\b")

_files, _articles, _hay = {}, {}, {}

def records(cite):
    kind, _, rest = cite.partition(":")
    if kind == "AREAS":
        return [open(AREAS, encoding="utf-8").read()]
    if kind == "HC":
        fp = HC + rest.partition(":")[0]
        return [open(fp, encoding="utf-8").read()] if os.path.isfile(fp) else []
    if kind in ARTICLES:
        if kind not in _articles:
            _articles[kind] = {d["position"]: json.dumps(d, ensure_ascii=False) + "\n" + d.get("text", "")
                               for d in map(json.loads, open(ARTICLES[kind], encoding="utf-8"))}
        return [_articles[kind].get(int(rest), "")]
    m = re.match(r"(\d+)(?:`[–-]`[\w-]+:(\d+))?", rest)
    a, b = int(m.group(1)), int(m.group(2) or m.group(1))
    if kind not in _files:
        _files[kind] = open(LINE_FILES[kind], encoding="utf-8").read().splitlines()
    return [json_unescaped(_files[kind][n - 1]) for n in range(a, b + 1) if 0 < n <= len(_files[kind])]

def hay(cite):
    if cite not in _hay:
        _hay[cite] = [[v for _, v in variants(t)] for t in records(cite) if t]
    return _hay[cite]

def found(quote, cites):
    parts = [p for p in re.split(r"\s*\(…\)\s*|\s*…\s*", quote.replace("&#39;", "'")) if p.strip()]
    for h in (h for c in cites for h in hay(c)):
        if all(any(v and v in x for v, x in zip([t for _, t in variants(p)], h)) for p in parts):
            return True
    return False

def main(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    cites = [CITE.findall(l) for l in lines]
    section, sec_cites = [], {}
    cur = 0
    for i, l in enumerate(lines):
        if l.startswith("## "):
            cur = i
        section.append(cur)
        sec_cites.setdefault(cur, []).extend(cites[i])
    counts = {"same line": 0, "within three lines": 0, "same section": 0, "search strings": 0}
    left, last = [], None
    for i, l in enumerate(lines):
        if cites[i]:
            last = cites[i]
        if l.startswith("#"):
            last = None
        for q in QUOTE.findall(l):
            if last is None and not sec_cites.get(section[i]):
                continue
            if last and found(q, last):
                counts["same line"] += 1
            elif SEARCH.search(l):
                counts["search strings"] += 1
            elif found(q, [c for j in range(max(0, i - 3), min(len(lines), i + 4)) for c in cites[j]]):
                counts["within three lines"] += 1
            elif found(q, sec_cites[section[i]]):
                counts["same section"] += 1
            else:
                left.append((i + 1, q))
    print(f"{path}: {sum(counts.values()) + len(left)} quoted strings")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print(f"  for a person to check: {len(left)}")
    for n, q in left:
        print(f"    line {n}: \"{q[:100]}\"")

if __name__ == "__main__":
    main(sys.argv[1])
