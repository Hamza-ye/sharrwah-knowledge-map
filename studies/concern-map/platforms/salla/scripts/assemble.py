# Assemble the Salla Q1 outputs: inventory.tsv, concerns.tsv, placements.tsv, citations.tsv.
# Verifies every quote against its file. Usage: python3 -I assemble.py
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import OBS, OUT, FETCHED, ACCESSED, local_source, clean
import concerns_def, placements_spec, cites_manual

ERR = []
K2ID = concerns_def.key_to_id()
CNAME = {k: (n, name, note) for n, k, name, note in concerns_def.CONCERNS}

# ---------------- fetched log: file -> (url, fetched_at)
LOG = {}
for i, line in enumerate(open(os.path.join(FETCHED, "log.tsv"), encoding="utf-8")):
    if i == 0 or not line.strip():
        continue
    url, f, status, at, sha = line.rstrip("\n").split("\t")
    if f:
        LOG[f] = (url, at, status, sha)

MONTHS = {"يناير": 1, "فبراير": 2, "مارس": 3, "أبريل": 4, "ابريل": 4, "إبريل": 4, "مايو": 5, "يونيو": 6, "يوليو": 7,
          "أغسطس": 8, "اغسطس": 8, "سبتمبر": 9, "أكتوبر": 10, "اكتوبر": 10, "نوفمبر": 11, "ديسمبر": 12}


def ar_updated(text):
    m = re.search(r"تاريخ (?:اخر|آخر) تحديث:\s*\S+\s+(\d{1,2})\s+(\S+)\s+(\d{4})", text)
    if m and m.group(2) in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(2)]:02d}-{int(m.group(1)):02d}"
    return None




import unicodedata


def _norm(s):
    """Length-preserving normalisation: no-break space to space, combining marks in canonical order."""
    out = list(s.replace("\xa0", " "))
    i = 0
    while i < len(out):
        if unicodedata.combining(out[i]):
            j = i
            while j < len(out) and unicodedata.combining(out[j]):
                j += 1
            out[i:j] = sorted(out[i:j], key=unicodedata.combining)
            i = j
        else:
            i += 1
    return "".join(out)


def resolve_quote(text, q):
    """Return the exact substring of text that the quote stands for, or None."""
    if q in text:
        return q
    nt, nq = _norm(text), _norm(q)
    i = nt.find(nq)
    if i < 0:
        return None
    return text[i:i + len(q)]

# ---------------- manual citations
CITES = []          # list of dicts in output order
MKEY = {}           # manual key -> cite id
n = 0
for key, t in cites_manual.C.items():
    kind, path, locator, quote = t[0], t[1], t[2], t[3]
    date = t[4] if len(t) > 4 else None
    basis = t[5] if len(t) > 5 else None
    if kind == "web":
        fp = os.path.join(FETCHED, path)
        if path not in LOG:
            ERR.append(f"{key}: no log entry for {path}")
            continue
        text = open(fp, encoding="utf-8").read()
        url, at, status, sha = LOG[path]
        rq = resolve_quote(text, quote)
        if rq is None:
            ERR.append(f"{key}: quote not found in {path}: {quote[:80]!r}")
            continue
        quote = rq
        ln = text[: text.index(quote)].count("\n") + 1
        locator = f"{locator} (line {ln} of the {'markdown' if path.endswith('.md') else 'rendered text'})"
        if not date:
            d = ar_updated(text) if path.startswith("help.salla.sa/") else None
            if d:
                date, basis = d, "last-updated date shown on the page (تاريخ اخر تحديث)"
            else:
                date, basis = at[:10], f"undated live page; counts as current on the day read ({at[:10]})"
        access = "md" if path.endswith(".md") else "rendered"
        src = url
        accessed = at[:10]
    else:
        fp = os.path.join(OBS, path)
        text = open(fp, encoding="utf-8").read()
        rq = resolve_quote(text, quote)
        if rq is None:
            ERR.append(f"{key}: quote not found in {path}: {quote[:80]!r}")
            continue
        quote = rq
        src = local_source(path)
        access = "local"
        accessed = ACCESSED
    if len(quote) > 320:
        ERR.append(f"{key}: quote too long ({len(quote)})")
    n += 1
    cid = f"SA-S-{n:04d}"
    MKEY[key] = cid
    CITES.append(dict(cite_id=cid, source=src, locator=clean(locator), quote=clean(quote), source_date=date,
                      date_basis=clean(basis), accessed=accessed, access_path=access))

# ---------------- inventory
B = json.load(open(os.path.join(OUT, "scripts", "build", "inventory_build.json"), encoding="utf-8"))
for lst, entry, mk, cks in placements_spec.EXTRA_INV:
    B.append(dict(list=lst, label=entry, entry=entry, concern_keys=cks, oos="", manual_cite=mk))
INV = []
ROWKEY = {}
for i, r in enumerate(B):
    iid = f"SA-I-{i + 1:04d}"
    if "manual_cite" in r:
        cid = MKEY.get(r["manual_cite"])
        if not cid:
            ERR.append(f"inventory {r['entry']}: manual cite {r['manual_cite']} missing")
            continue
    else:
        cid = f"SA-S-{1001 + len([x for x in INV if not x.get('manual')]):04d}"
        c = r["cite"]
        CITES.append(dict(cite_id=cid, **c))
    for k in r["concern_keys"]:
        if k not in K2ID:
            ERR.append(f"inventory {r['entry']}: unknown concern {k}")
    row = dict(inv_id=iid, list=r["list"], entry=r["entry"], label=r.get("label", r["entry"]), cite_id=cid,
               concern_ids=" ".join(K2ID[k] for k in r["concern_keys"] if k in K2ID),
               oos=r["oos"], keys=r["concern_keys"], quote=(r.get("cite") or {}).get("quote", ""),
               manual=("manual_cite" in r))
    INV.append(row)
    ROWKEY.setdefault((r["list"], r.get("label", r["entry"])), row)

BY = {k: [] for k in K2ID}
for r in INV:
    for k in r["keys"]:
        BY.setdefault(k, []).append(r)


def ref(rf):
    if rf.startswith("m:"):
        c = MKEY.get(rf[2:])
        if not c:
            ERR.append(f"ref {rf}: no manual cite")
        return c
    if rf.startswith("i:"):
        lst, ent = rf[2:].split("|", 1)
        r = ROWKEY.get((lst, ent))
        if not r:
            ERR.append(f"ref {rf}: no inventory row")
            return None
        return r["cite_id"]
    if rf.startswith("i~:"):
        lst, sub = rf[3:].split("|", 1)
        for r in INV:
            if r["list"] == lst and sub in r["label"]:
                return r["cite_id"]
        ERR.append(f"ref {rf}: no inventory row")
    return None


NO_TERMS = placements_spec.NO_TERMS


def rows_of(k, pred):
    return [r for r in BY.get(k, []) if pred(r)]


def default_placements(k):
    rs = BY.get(k, [])
    api = [r for r in rs if r["list"] == "api-resources" and r["label"].startswith("Merchant API > APIs >")]
    oapi = [r for r in rs if r["list"] == "api-resources" and not r["label"].startswith("Merchant API >")]
    dapp = [r for r in rs if r["list"] == "other:dashboard-apps"]
    sett = [r for r in rs if r["list"] == "settings" and not r["oos"]]
    nav = [r for r in rs if r["list"] == "admin-navigation" and not r["oos"] and not r["label"].startswith("Partners portal >")]
    pnav = [r for r in rs if r["list"] == "admin-navigation" and r["label"].startswith("Partners portal >")]
    plan = [r for r in rs if r["list"] == "plan-features" and (r["label"].startswith("سلة بلس:") or r["label"].startswith("سلة برو:"))]
    flags = [r for r in rs if r["list"] == "other:dashboard-features" and '"plans": [' in r["quote"] and '"plans": []' not in r["quote"]]
    scopes = [r for r in rs if r["list"] == "access-scopes"]
    topics = [r for r in rs if r["list"] == "webhook-topics"]
    out = {}
    # software
    if api or dapp or sett or nav:
        cs = [x["cite_id"] for x in (api[:1] + dapp[:1] + (sett[:1] or nav[:1]))]
        where = []
        if api: where.append("a group of Salla's own Merchant API")
        if dapp: where.append("a bundle of the merchant dashboard")
        if sett or nav: where.append("a page of the merchant dashboard")
        out["software"] = ("core", cs, "Shown as " + " and ".join(where) + " (inventory rows cited).")
    elif pnav:
        out["software"] = ("core (Salla Partners portal)", [pnav[0]["cite_id"]], "Shown as a page of Salla's Partners portal.")
    else:
        out["software"] = (None, [], "Not shown.")
    # decides
    parts, cs = [], []
    if sett:
        parts.append("merchant"); cs.append(sett[0]["cite_id"])
    elif nav:
        parts.append("merchant"); cs.append(nav[0]["cite_id"])
    if plan:
        parts.append("operator per plan"); cs.append(plan[0]["cite_id"])
    elif flags:
        parts.append("operator per plan"); cs.append(flags[0]["cite_id"])
    if parts:
        note = []
        if "merchant" in parts: note.append("merchant: managed in the merchant's own settings or dashboard page")
        if "operator per plan" in parts: note.append("operator per plan: listed among a plan's features or limited to plans by a dashboard feature flag")
        out["decides"] = ("; ".join(parts), cs, "; ".join(note) + ".")
    else:
        out["decides"] = (None, [], "Not shown.")
    out["legal"] = (None, [], NO_TERMS)
    # boundary
    bparts, bcs = [], []
    if api:
        bparts.append("API: " + ", ".join(r["entry"].split(" > ")[-1] for r in api)); bcs += [r["cite_id"] for r in api[:2]]
    if oapi:
        bparts.append("API: " + ", ".join(r["label"] for r in oapi[:3])); bcs += [r["cite_id"] for r in oapi[:1]]
    if scopes:
        bparts.append("scope: " + ", ".join(r["entry"] for r in scopes)); bcs += [r["cite_id"] for r in scopes[:1]]
    if topics:
        names = [r["entry"] for r in topics]
        bparts.append("webhooks: " + ", ".join(names[:4]) + (f" (+{len(names) - 4} more)" if len(names) > 4 else "")); bcs += [r["cite_id"] for r in topics[:2]]
    if sett:
        bparts.append("setting: " + sett[0]["entry"]); bcs.append(sett[0]["cite_id"])
    elif nav:
        bparts.append("dashboard page: " + nav[0]["entry"]); bcs.append(nav[0]["cite_id"])
    elif pnav:
        bparts.append("portal page: " + pnav[0]["entry"].replace("Partners portal > ", "")); bcs.append(pnav[0]["cite_id"])
    if bparts:
        out["boundary"] = ("; ".join(bparts), bcs[:8], "")
    else:
        out["boundary"] = (None, [], "Not shown.")
    out["reason"] = (None, [], "No source read states why Salla places it this way.")
    return out


PL = []
for n_, k, name, split in concerns_def.CONCERNS:
    cid = K2ID[k]
    d = default_placements(k)
    ov = placements_spec.SPEC.get(k, {})
    for p in ("software", "decides", "legal", "boundary", "reason"):
        v = ov.get(p, d[p])
        val, refs, note = v
        cites = []
        for rf in refs:
            if isinstance(rf, str) and rf.startswith("SA-S-"):
                cites.append(rf)
            else:
                c = ref(rf)
                if c:
                    cites.append(c)
        cites = list(dict.fromkeys(cites))
        if val is None:
            PL.append(dict(concern_id=cid, placement=p, value="not shown", status="not shown", cite_ids=" ".join(cites), note=note))
        else:
            if not cites:
                ERR.append(f"{k}/{p}: shown without citations")
            PL.append(dict(concern_id=cid, placement=p, value=val, status="shown", cite_ids=" ".join(cites), note=note))

# ---------------- links: entries that state a concern, added after the placements (placements and terms unchanged)
TERMS_BY = {k: list(v) for k, v in BY.items()}
for k, refs in getattr(placements_spec, "LINKS", {}).items():
    if k not in K2ID:
        ERR.append(f"link: unknown concern {k}")
        continue
    for lst, lab in refs:
        r = ROWKEY.get((lst, lab))
        if not r:
            ERR.append(f"link {k}: no inventory row {lst}|{lab}")
            continue
        if k in r["keys"]:
            continue
        r["keys"].append(k)
        r["concern_ids"] = " ".join(K2ID[x] for x in r["keys"] if x in K2ID)
        BY.setdefault(k, []).append(r)
for k in BY:
    BY[k].sort(key=lambda r: r["inv_id"])

# ---------------- concerns
CON = []
for n_, k, name, split in concerns_def.CONCERNS:
    rs = BY.get(k, [])
    terms = []
    for r in TERMS_BY.get(k, []):
        e = r["entry"]
        for pre in ("Merchant API > APIs > ", "Merchant API > ", "docs navbar > ", "Partners portal > ", "App Store category: ", "app type: ", "app listing category: "):
            if e.startswith(pre):
                e = e[len(pre):]
        if re.match(r"^(سلة بلس|سلة برو): ", e):
            e = e.split(": ", 1)[1]
        if e.startswith("salla.com plans ("):
            e = e.split("): ", 1)[1]
        if e not in terms and len(e) < 90:
            terms.append(e)
    terms = (concerns_def.EXTRA_TERMS.get(k, []) + [t for t in terms if t not in concerns_def.EXTRA_TERMS.get(k, [])])[:10]
    sn = split
    if not rs and not sn.startswith("Not in the platform's lists:"):
        ERR.append(f"{k}: no inventory entries and no 'Not in the platform's lists:' note")
    CON.append(dict(concern_id=K2ID[k], concern=name, platform_terms=" | ".join(terms), inv_ids=" ".join(r["inv_id"] for r in rs), split_note=sn.strip()))

# ---------------- checks
used = set()
for p in PL:
    used.update(p["cite_ids"].split())
for r in INV:
    used.add(r["cite_id"])
all_ids = {c["cite_id"] for c in CITES}
missing = used - all_ids
if missing:
    ERR.append(f"cite ids used but not defined: {sorted(missing)[:10]}")
unused_manual = [k for k, v in MKEY.items() if v not in used]
for r in INV:
    if not r["concern_ids"] and not r["oos"]:
        ERR.append(f"inventory row without concern or reason: {r['inv_id']} {r['entry']}")


def w(name, cols, rows):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(clean(str(r.get(c, "") if r.get(c) is not None else "")) for c in cols) + "\n")


w("inventory.tsv", ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"],
  [dict(r, out_of_scope_reason=r["oos"]) for r in INV])
w("concerns.tsv", ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"], CON)
w("placements.tsv", ["concern_id", "placement", "value", "status", "cite_ids", "note"], PL)
w("citations.tsv", ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
  sorted(CITES, key=lambda c: c["cite_id"]))

from collections import Counter
print("inventory", len(INV), "concerns", len(CON), "placements", len(PL), "citations", len(CITES))
print("placement status", Counter((p["placement"], p["status"]) for p in PL))
print("manual cites unused:", unused_manual)
print("errors:", len(ERR))
for e in ERR:
    print("  ERR", e)
