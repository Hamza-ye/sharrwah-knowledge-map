# Resolve settings-center sections and items to labels from the dashboard's settings translations.
# Usage: python3 -I settings_resolve.py OBSERVED_SA_ROOT [--items]
import json, sys, os

root = sys.argv[1]
show_items = "--items" in sys.argv
sc = os.path.join(root, "structures/salla/settings-center/merchant@en/items.jsonl")
en = json.load(open(os.path.join(root, "structures/salla/dashboard-translations/en/settings.json"), encoding="utf-8"))
ar = json.load(open(os.path.join(root, "structures/salla/dashboard-translations/ar/settings.json"), encoding="utf-8"))

def t(key, tr):
    if key is None:
        return ""
    if key in tr:
        return tr[key]
    return ""

for n, line in enumerate(open(sc, encoding="utf-8"), 1):
    d = json.loads(line)
    k = d["kind"]
    if k == "s:section":
        sec = d["section"]
        print(f"\nLINE {n}\tSECTION\t{sec}\tpath={d.get('path','')}\ten={t(sec, en)!r}\tar={t(sec, ar)!r}")
    elif show_items and k in ("s:item", "s:field", "s:plan-gate", "s:link", "s:redirect", "s:list-header", "s:header", "s:header-title"):
        lab = d.get("label") or d.get("title") or ""
        desc = d.get("description") or ""
        extra = {kk: vv for kk, vv in d.items() if kk not in ("position", "section", "kind", "parent", "label", "description")}
        print(f"LINE {n}\t  {k}\tid={d.get('id','')}\ten={t(lab, en)!r}\tar={t(lab, ar)!r}\tdesc_en={t(desc, en)[:140]!r}\t{json.dumps(extra, ensure_ascii=False)[:200]}")
