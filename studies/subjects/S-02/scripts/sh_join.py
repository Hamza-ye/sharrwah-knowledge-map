"""Resolve Shopify router full paths from the parent chain; join nav hrefs to routes; title coverage."""
import json
import re
import sys
from collections import Counter

B = "/home/user/observed-sh/structures/shopify"


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


routes = load(f"{B}/admin-router/items.jsonl")
byid = {}
dup = 0
for r in routes:
    if r["id"] in byid:
        dup += 1
    byid.setdefault(r["id"], r)
print("routes", len(routes), "distinct ids", len(byid), "dup ids", dup)


def full(r, seen=()):
    p = r.get("path")
    if isinstance(p, dict):
        e = str(p.get("expr"))
        p = "/settings" if "o.settings()" in e else "{" + e + "}"
    par = r.get("parent")
    if par and par in byid and par not in seen:
        base = full(byid[par], seen + (r["id"],))
    else:
        base = ""
    if p is None:
        return base
    if p.startswith("/"):
        return p
    return (base.rstrip("/") + "/" + p) if base else "/" + p


paths = {}
for r in routes:
    fp = full(r)
    r["_full"] = fp
    paths.setdefault(fp, []).append(r)


def perms_of(r):
    out = []
    cur = r
    seen = set()
    while cur is not None and cur["id"] not in seen:
        seen.add(cur["id"])
        e = cur.get("eligibility")
        if isinstance(e, dict) and e.get("permissions"):
            out.append((cur["id"], e["permissions"]))
        cur = byid.get(cur.get("parent"))
    return out


titles = {r["key"]: r["value"] for r in load(f"{B}/admin-route-titles-en/items.jsonl")}
have_title = sum(1 for r in routes if f"{r['id']}:title" in titles or (isinstance(r.get('title'), dict) and r['title'].get('value')))
print("routes with a title (inline value or titles-en key)", have_title)
print("titles-en keys matching a route id", sum(1 for k in titles if k.rsplit(':title', 1)[0] in byid))

# join main nav and settings nav
navfiles = [
    f"{B}/admin-main-nav/demo-fake-dev-store@settings-organization-account/items.jsonl",
    f"{B}/admin-settings-nav/ibx5bt-xy/items.jsonl",
]
for nf in navfiles:
    print("==", nf.split('/shopify/')[1])
    hit = miss = 0
    for it in load(nf):
        href = it.get("href") or it.get("url")
        if not href:
            continue
        m = re.search(r"/store/[^/]+(/.*)?$", href) or re.search(r"/admin(/.*)?$", href)
        if not m:
            continue
        p = (m.group(1) or "/").rstrip("/") or "/"
        cands = paths.get(p, [])
        label = it.get("text") or it.get("title")
        if cands:
            hit += 1
            r = cands[0]
            print(f"   OK  {label!r:32} {p:42} -> {r['id']:40} section={r.get('section')} perms={perms_of(r)}")
        else:
            miss += 1
            print(f"   --  {label!r:32} {p:42} (no route with this full path)")
    print("   hit", hit, "miss", miss)

sec = sys.argv[1] if len(sys.argv) > 1 else None
if sec:
    for r in routes:
        if r.get("section") == sec:
            t = (r.get("title") or {}).get("value") if isinstance(r.get("title"), dict) else titles.get(f"{r['id']}:title")
            print(f"   {r['id']:50} {r['_full']:55} {str(t)[:40]:40} res={r.get('resource')} perms={(r.get('eligibility') or {}).get('permissions') if isinstance(r.get('eligibility'), dict) else None}")
