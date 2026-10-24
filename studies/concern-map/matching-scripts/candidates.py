"""Generate cross-platform candidate pairs for the Q1 matching pass.

Three generators, each recorded per pair:
  1. term   - normalized phrase overlap over concern name parts, platform_terms and
              inventory entries (exact after normalization; a second, looser key strips
              platform brand words and trailing 'apps', flagged as 'brandless').
  2. ident  - identifier families: webhook/event topics, access scopes and API resource
              names reduced to a resource noun (e.g. orders/create, order.created,
              read_orders, wc/v3 > orders -> 'order').
  3. tfidf  - cosine similarity of content-word bags (name + terms + entries); top hits.

Usage: python3 -I candidates.py <outdir>
Writes <outdir>/candidates.tsv and <outdir>/phrase-index.tsv.
"""
import collections
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import load  # noqa: E402

BRAND = {"shopify", "salla", "woocommerce", "woo", "wc", "سلة"}
STOP = set("""a an and the of for to in on at by with from or as is are be your you our we it its this that
these those into per via not no all any each other others more most new our their them they he she
do does use using used can may within out up over off about than then so such only also via
apps app - & + / | > < : ; , . ( ) * ? ! ' " 0 1 2 3 4 5 6 7 8 9""".split())


def norm_phrase(s):
    s = s.lower()
    s = s.replace("®", "").replace("™", "").replace("’", "'")
    s = re.sub(r"[¹²³*]+", "", s)
    s = re.sub(r"\s+", " ", s).strip(" .:;,-")
    return s


def sing(w):
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("ses") and not w.endswith("sses"):
        return w[:-2]
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss") and not w.endswith("us"):
        return w[:-1]
    return w


def phrase_key(s):
    s = norm_phrase(s)
    words = re.findall(r"[\w؀-ۿ]+", s)
    words = [sing(w) for w in words]
    return " ".join(words)


def brandless_key(s):
    k = phrase_key(s)
    words = [w for w in k.split() if w not in BRAND]
    if words and words[-1] == "app":
        words = words[:-1]
    return " ".join(words)


def name_parts(name):
    parts = [name]
    m = re.match(r"^(.*?)\s*\((.*)\)\s*$", name)
    if m:
        parts.append(m.group(1))
        for p in re.split(r"[;/,]", m.group(2)):
            parts.append(p)
    return [p.strip() for p in parts if p.strip()]


def entry_parts(entry):
    parts = [entry]
    if " > " in entry:
        parts.append(entry.split(" > ")[-1])
    m = re.match(r"^(.*?)\s*\((.*)\)\s*$", entry)
    if m:
        parts.append(m.group(1))
    return parts


# ---------- identifier families ----------
RES_ALIASES = {
    "variant": "product_variant", "variation": "product_variant", "product-variation": "product_variant",
    "product_variation": "product_variant", "productvariation": "product_variant",
    "storetax": "tax", "taxe": "tax",
    "specialoffer": "special_offer", "shipping_zone": "shipping_zone", "shippingzone": "shipping_zone",
    "shipping-zone": "shipping_zone",
}


def res_norm(r):
    r = r.lower().strip().replace("-", "_")
    r = sing(r)
    return RES_ALIASES.get(r, r)


def identifiers(platform, c):
    out = set()
    texts = []
    for r in c["inv"]:
        texts.append((r["list"], r["entry"]))
    for s in c["stmts"]:
        if s["placement"] == "boundary":
            texts.append(("stmt", s["identifier"]))
    for lst, t in texts:
        t = t.strip()
        # Shopify webhook topic: resource/action
        m = re.fullmatch(r"([a-z_]+)/([a-z_]+)", t)
        if m and platform == "shopify":
            out.add(("topic", res_norm(m.group(1))))
            continue
        # Salla / Woo webhook topic: resource.action(.more)
        m = re.fullmatch(r"([a-z_]+)\.([a-z_.A-Z]+)", t)
        if m and platform in ("salla", "woocommerce") and lst in ("webhook-topics", "stmt"):
            first = m.group(1)
            if first in ("store",):  # store.branch.created -> branch
                first = t.split(".")[1]
            out.add(("topic", res_norm(first)))
            continue
        # Shopify scopes read_x / write_x / customer_read_x / unauthenticated_read_x
        m = re.fullmatch(r"(?:customer_|unauthenticated_)?(?:read|write)_([a-z_]+)", t)
        if m and lst in ("access-scopes", "stmt"):
            out.add(("scope", res_norm(m.group(1))))
            continue
        # Salla scopes are bare nouns in the access-scopes list
        if platform == "salla" and lst == "access-scopes" and re.fullmatch(r"[a-z\-]+", t):
            out.add(("scope", res_norm(t)))
            continue
        # Woo REST resources wc/v3 > orders
        m = re.fullmatch(r"wc/v\d > ([a-z\-]+)", t)
        if m:
            out.add(("api", res_norm(m.group(1))))
            continue
        if lst == "api-resources" and re.fullmatch(r"[A-Za-z ]+", t):
            out.add(("api", res_norm(t.replace(" ", "_"))))
    return out


def tokens(c):
    bag = collections.Counter()
    texts = name_parts(c["name"]) + c["terms"] + [r["entry"] for r in c["inv"]]
    for t in texts:
        for w in re.findall(r"[a-zA-Z]+", t.lower()):
            w = sing(w)
            if len(w) < 3 or w in STOP or w in BRAND:
                continue
            bag[w] += 1
    return bag


def main(outdir):
    data = load.load_all()
    concerns = {}
    for p in load.PLATFORMS:
        for cid, c in data[p][0].items():
            concerns[cid] = c
    # phrase index
    phr = collections.defaultdict(lambda: collections.defaultdict(list))  # key -> cid -> [(src, raw)]
    bphr = collections.defaultdict(lambda: collections.defaultdict(list))
    for cid, c in concerns.items():
        srcs = [("concern", x) for x in name_parts(c["name"])]
        srcs += [("platform_terms", t) for t in c["terms"]]
        for r in c["inv"]:
            for x in entry_parts(r["entry"]):
                srcs.append((f"inventory {r['inv_id']}", x))
        for src, raw in srcs:
            k = phrase_key(raw)
            if not k or len(k) < 3:
                continue
            phr[k][cid].append((src, raw))
            bk = brandless_key(raw)
            if bk and len(bk) >= 3 and bk != k:
                bphr[bk][cid].append((src, raw))
    # document frequency of phrase across concerns
    pairs = collections.defaultdict(lambda: {"term": [], "brandless": [], "ident": [], "tfidf": 0.0})

    def plat(cid):
        return cid[:2]

    for k, d in phr.items():
        cids = list(d)
        if len(set(plat(x) for x in cids)) < 2:
            continue
        df = len(cids)
        for i, a in enumerate(cids):
            for b in cids[i + 1:]:
                if plat(a) == plat(b):
                    continue
                key = tuple(sorted((a, b)))
                pairs[key]["term"].append((k, df))
    for k, d in bphr.items():
        cids = list(d)
        if len(set(plat(x) for x in cids)) < 2:
            continue
        df = len(cids)
        for i, a in enumerate(cids):
            for b in cids[i + 1:]:
                if plat(a) == plat(b):
                    continue
                key = tuple(sorted((a, b)))
                pairs[key]["brandless"].append((k, df))
    # identifiers
    ids = {cid: identifiers(c["platform"], c) for cid, c in concerns.items()}
    idx = collections.defaultdict(set)
    for cid, s in ids.items():
        for kind, res in s:
            idx[res].add(cid)
    for res, cids in idx.items():
        cids = sorted(cids)
        if len(cids) > 25:
            continue
        for i, a in enumerate(cids):
            for b in cids[i + 1:]:
                if plat(a) == plat(b):
                    continue
                key = tuple(sorted((a, b)))
                pairs[key]["ident"].append((res, len(cids)))
    # tfidf
    bags = {cid: tokens(c) for cid, c in concerns.items()}
    dfc = collections.Counter()
    for b in bags.values():
        for w in b:
            dfc[w] += 1
    N = len(bags)
    vec = {}
    for cid, b in bags.items():
        v = {w: (1 + math.log(n)) * math.log(N / dfc[w]) for w, n in b.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vec[cid] = {w: x / norm for w, x in v.items()}
    cl = list(concerns)
    for i, a in enumerate(cl):
        best = collections.defaultdict(list)
        for b in cl:
            if plat(a) == plat(b):
                continue
            va, vb = vec[a], vec[b]
            s = sum(x * vb.get(w, 0.0) for w, x in va.items())
            best[plat(b)].append((s, b))
        for pf, lst in best.items():
            lst.sort(reverse=True)
            for s, b in lst[:4]:
                if s < 0.12:
                    continue
                key = tuple(sorted((a, b)))
                pairs[key]["tfidf"] = max(pairs[key]["tfidf"], round(s, 3))
    # write
    with open(os.path.join(outdir, "candidates.tsv"), "w", encoding="utf-8") as f:
        f.write("a\tb\ta_name\tb_name\tterm_shared\tbrandless_shared\tident_shared\ttfidf\tscore\n")
        rows = []
        for (a, b), d in pairs.items():
            tscore = sum(1.0 / df for _, df in d["term"])
            bscore = sum(0.5 / df for _, df in d["brandless"])
            iscore = sum(1.0 / df for _, df in d["ident"])
            score = round(tscore + bscore + iscore + d["tfidf"], 3)
            rows.append((score, a, b, d))
        rows.sort(key=lambda x: (-x[0], x[1], x[2]))
        for score, a, b, d in rows:
            t = "; ".join(sorted(set(f"{k}[{df}]" for k, df in d["term"])))
            bl = "; ".join(sorted(set(f"{k}[{df}]" for k, df in d["brandless"])))
            idt = "; ".join(sorted(set(f"{k}[{df}]" for k, df in d["ident"])))
            f.write(f"{a}\t{b}\t{concerns[a]['name']}\t{concerns[b]['name']}\t{t}\t{bl}\t{idt}\t{d['tfidf']}\t{score}\n")
    with open(os.path.join(outdir, "phrase-index.tsv"), "w", encoding="utf-8") as f:
        f.write("key\tconcern_id\tsource\traw\n")
        for k, d in sorted(phr.items()):
            if len(set(plat(x) for x in d)) < 2:
                continue
            for cid, lst in d.items():
                for src, raw in lst:
                    f.write(f"{k}\t{cid}\t{src}\t{raw}\n")
    print("pairs:", len(pairs))


if __name__ == "__main__":
    main(sys.argv[1])
