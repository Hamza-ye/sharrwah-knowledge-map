# Router helpers shared by the add_* scripts: verbatim where and eligibility excerpts of admin-router items.jsonl.
import json
from common import *
RP = "structures/shopify/admin-router/items.jsonl"
_lines = git_show(RP).splitlines()
byid = {}
for _n, _l in enumerate(_lines, start=1):
    _d = json.loads(_l)
    byid[_d["id"]] = (_n, _l, _d)

def balanced(text, start):
    depth, i, in_str, esc = 0, start, False, False
    while i < len(text):
        ch = text[i]
        if in_str:
            if esc: esc = False
            elif ch == "\\": esc = True
            elif ch == '"': in_str = False
        elif ch == '"': in_str = True
        elif ch in "{[": depth += 1
        elif ch in "}]":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
        i += 1
    return None

def where_quote(rid):
    n, l, d = byid[rid]
    i = l.index('"section":')
    j = i + len('"section":') + len(json.dumps(d["section"]))
    if l.startswith(',"path":', j):
        if isinstance(d["path"], (dict, list)):
            j = j + len(',"path":') + len(balanced(l, j + len(',"path":')))
        else:
            j = j + len(',"path":') + len(json.dumps(d["path"], ensure_ascii=False))
    if l.startswith(',"title":', j):
        t = balanced(l, j + len(',"title":'))
        if isinstance(d.get("title"), dict) and set(d["title"]) != {"value"}:
            v = ',"title":{"value":' + json.dumps(d["title"]["value"], ensure_ascii=False)
            assert l.startswith(v, j), rid
            j = j + len(v)
        else:
            j = j + len(',"title":') + len(t)
    q = l[i:j]
    assert q in l
    return n, q

def elig_quote(rid):
    n, l, d = byid[rid]
    i = l.index('"eligibility":')
    obj = balanced(l, i + len('"eligibility":'))
    return n, '"eligibility":' + obj

def make(A):
    def W(c, rid, note=""):
        n, q = where_quote(rid)
        cid = osh_cite(RP, f"line {n} ({rid})", q, sid="shopify/admin-router")
        A.add(c, "where", "structures/shopify/admin-router", rid, q, "", cid,
              "route's section, path and title as the router states them" + ("; " + note if note else ""))
    def D(c, rid, note=""):
        n, q = elig_quote(rid)
        cid = osh_cite(RP, f"line {n} ({rid})", q, sid="shopify/admin-router")
        A.add(c, "decides", "structures/shopify/admin-router", rid, q, "", cid,
              "eligibility the router states for the route" + ("; " + note if note else ""))
    return W, D
