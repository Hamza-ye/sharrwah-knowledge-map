# Fetch the Marketplace search listing (all pages) for category slugs, via fetch.py (logged, rate-limited),
# and report which listed products are also in "Developed by Woo".
# Usage: python3 -I catlist.py slug [slug ...]
import json, os, subprocess, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "fetched"))
WORK = os.path.normpath(os.path.join(HERE, "..", "work"))
API = "https://woocommerce.com/wp-json/wccom-extensions/1.0/search?category={slug}&per_page=60&page={page}"

def get(slug, page):
    name = f"mkt_search_{slug}_p{page}"
    path = os.path.join(OUT, name + ".json")
    if not os.path.exists(path):
        subprocess.run([sys.executable, "-I", os.path.join(HERE, "fetch.py"), API.format(slug=slug, page=page), name], check=True)
    return json.load(open(path))

def listing(slug):
    first = get(slug, 1)
    prods = list(first["products"])
    for page in range(2, int(first.get("total_pages") or 1) + 1):
        prods += get(slug, page)["products"]
    return first.get("total_products"), prods

woo = {}
for f in ["woocommerce.com_wp_json_wccom_extensions_1.0_search_category_developed_by_woo_per_page_100.json",
          "woocommerce.com_wp_json_wccom_extensions_1.0_search_category_developed_by_woo_per_page_100_page_2.json"]:
    for p in json.load(open(os.path.join(OUT, f)))["products"]:
        woo[p["id"]] = p
res = {}
for slug in sys.argv[1:]:
    total, prods = listing(slug)
    hits = [(p["id"], p["title"], p["vendor_name"], p["link"].split("?")[0]) for p in prods if p["id"] in woo]
    vend = sorted({str(p.get("vendor_name")) for p in prods})
    res[slug] = {"total": total, "n": len(prods), "woo": hits, "vendors_n": len(vend)}
    print(f"{slug}: {total} listed, {len(prods)} read, Developed by Woo: {len(hits)}")
    for h in hits:
        print("    ", h)
path = os.path.join(WORK, "catlist.json")
old = json.load(open(path)) if os.path.exists(path) else {}
old.update(res)
json.dump(old, open(path, "w"), indent=1)
