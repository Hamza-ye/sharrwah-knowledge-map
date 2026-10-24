# Register one citation per release inventory row (quote = the source line naming the entry).
# Usage: python3 -I cite_release_inventory.py  -> out/inv_release_cited.json
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cite

REL_DATE = "2026-10-09"
REL_BASIS = "released: WooCommerce 11.2.1 on WordPress.org (plugin-info.json last_updated 2026-10-09 3:35pm GMT)"
ACCESSED = "2026-10-10"

rows = json.load(open(os.path.join(HERE, "out", "inv_release.json")))
for r in rows:
    r["cite_id"] = cite.add(
        source="woocommerce-11.2.1:" + r["path"],
        locator=f"line {r['line']}",
        quote=r["quote"],
        source_date=REL_DATE, date_basis=REL_BASIS, accessed=ACCESSED,
        access_path="local", working=None)
json.dump(rows, open(os.path.join(HERE, "out", "inv_release_cited.json"), "w"), ensure_ascii=False, indent=0)
print(len(rows), "rows cited; last id", rows[-1]["cite_id"])
