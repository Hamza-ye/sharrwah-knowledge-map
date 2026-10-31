"""Shopify's names in the class's model, in Shopify's own Arabic (Stage 4A, Shopify's amendment; the founder's note of
31 October; held/shopify/amendment-notes.md, 'Shopify's words in Arabic'). Each capability's definition names Shopify's
own words for it in its parentheses ('Shopify X, Y'). observed-sh's vocabularies pair the admin's, checkout's and
shopify.com's Arabic strings with their English by Shopify's own keys. For each Shopify name, the script finds the
strings whose English is that name exactly (case and spacing folded), the admin's first, then checkout's, then
shopify.com's, and writes the Arabic they carry, the most frequent first, with every key it rests on. A name with no
exact twin is left without Arabic, for a reader; a name with several Arabic renderings lists them all.

Usage:
  python3 -I method/shopify_arabic_names.py            prints the counts
  python3 -I method/shopify_arabic_names.py --write    writes studies/class-model/names-ar.tsv
"""
import collections, csv, glob, json, os, re, subprocess, sys

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    sys.exit(__doc__)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.path.join(ROOT, "studies", "class-model")
SH = "/home/user/observed-sh"
COMMIT = subprocess.run(["git", "-C", SH, "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
SOURCES = [("admin-translations", "structures/shopify/admin-translations/en-ar@2026-10-31/items.jsonl"),
           ("checkout-translations", "structures/shopify/checkout-translations/en-ar@2026-10-31/items.jsonl"),
           ("shopify-com-translations", "structures/shopify/shopify-com-translations/ar-en@2026-10-31/items.jsonl")]
csv.field_size_limit(10**9)


def fold(s):
    return re.sub(r"\s+", " ", s.replace("’", "'")).strip().strip(".:").casefold()


index = {name: collections.defaultdict(list) for name, _ in SOURCES}
for name, path in SOURCES:
    for n, l in enumerate(open(os.path.join(SH, path), encoding="utf-8"), 1):
        d = json.loads(l)
        en, ar = d.get("en"), d.get("ar")
        if isinstance(en, str) and isinstance(ar, str) and en.strip() and ar.strip():
            where = "/".join(x for x in (d.get("bundle"), d.get("namespace"), d.get("key")) if x)
            index[name][fold(en)].append((ar.strip(), f"{name}:{where} (line {n})"))


def caps():
    rows = list(csv.DictReader(open(os.path.join(MODEL, "merged", "capabilities.tsv"), encoding="utf-8"),
                               delimiter="\t", quoting=csv.QUOTE_NONE))
    seen = {r["cap_id"] for r in rows}
    for p in sorted(glob.glob(os.path.join(MODEL, "parts", "*-amend", "capabilities.tsv"))):
        for r in csv.DictReader(open(p, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE):
            if r["cap_id"] not in seen:
                rows.append(r); seen.add(r["cap_id"])
    return rows


def shopify_names(text):
    """The names after 'Shopify' in a definition's parentheses, up to the next platform's ';' or the ')'."""
    out = []
    for seg in re.findall(r"\(([^()]*)\)", text):
        for part in seg.split(";"):
            m = re.match(r"\s*Shopify\b[:\s]+(.*)$", part)
            if m:
                body = m.group(1).strip()
                names = [body] + [x.strip() for x in re.split(r",\s+(?![^()]*\))", body)]
                out += [x for x in dict.fromkeys(names) if x and len(x) <= 80]
    return out


rows, stats = [], collections.Counter()
for c in caps():
    for name in shopify_names(c["capability"]):
        hits = []
        for src, _ in SOURCES:
            hits = index[src].get(fold(name), [])
            if hits:
                break
        if not hits and ", " in name:
            continue                      # a whole list of names takes a row only where it is one string itself
        ars = collections.Counter(a for a, _ in hits)
        keys = collections.defaultdict(list)
        for a, k in hits:
            keys[a].append(k)
        if ars:
            best = ars.most_common()
            stats["named"] += 1
            stats["several" if len(best) > 1 else "one"] += 1
            rows.append({"cap_id": c["cap_id"], "platform": "shopify", "name_en": name, "name_ar": best[0][0],
                         "keys": "; ".join(keys[best[0][0]][:3]) + (f"; and {len(keys[best[0][0]]) - 3} more" if len(keys[best[0][0]]) > 3 else ""),
                         "others": "; ".join(f"{a} ({n})" for a, n in best[1:6]),
                         "reading": f"the Arabic the {len(hits)} string(s) with this exact English carry, observed-sh@{COMMIT}; a reading: the platform's word for the name"})
        else:
            stats["none"] += 1
            rows.append({"cap_id": c["cap_id"], "platform": "shopify", "name_en": name, "name_ar": "", "keys": "",
                         "others": "", "reading": "no string with this exact English in the three vocabularies; read, not guessed"})
print(f"{len(rows)} Shopify names in {len({r['cap_id'] for r in rows})} capabilities: {stats['named']} with Arabic "
      f"({stats['one']} one rendering, {stats['several']} several), {stats['none']} with no exact twin; observed-sh@{COMMIT}")
if "--write" in sys.argv:
    p = os.path.join(MODEL, "names-ar.tsv")
    head = ["cap_id", "platform", "name_en", "name_ar", "keys", "others", "reading"]
    with open(p, "w", encoding="utf-8") as f:
        f.write("\t".join(head) + "\n")
        for r in rows:
            f.write("\t".join(str(r[h]).replace("\t", " ").replace("\n", " ") for h in head) + "\n")
    print(f"wrote {os.path.relpath(p, ROOT)}")
