# Applies the review decisions (work/decisions/*.txt) to candidates.tsv.
# Writes work/reviewed-statements.tsv (kept and moved candidates, plus same-citation statements added under
# the concern a route, line or key belongs to) and work/review-log.tsv (every move and drop).
# Usage: python3 -I scripts/review.py
import sys, os, json, re, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

cand = rd(os.path.join(BASE, "candidates.tsv"))
first_cites = {r["cite_id"]: r for r in rd(os.path.join(FIRST, "citations.tsv"))}
new_cites = {r["cite_id"]: r for r in rd(os.path.join(BASE, "citations-new.tsv"))}
allc = {**first_cites, **new_cites}

def load(pattern, nfields):
    out = {}
    for f in sorted(glob.glob(os.path.join(WORK, "decisions", pattern))):
        for line in open(f, encoding="utf-8"):
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.rstrip("\n").split("|", nfields - 1)
            parts += [""] * (nfields - len(parts))
            idx = int(parts[0])
            assert idx not in out, f"duplicate decision {idx}"
            out[idx] = [p.strip() for p in parts[1:]]
    return out

router = load("router.txt", 4)            # action, to, reason
access = load("access-lines.txt", 4)
helpl = load("help-links.txt", 4)
first = load("first-run-*.txt", 5)        # action, scope, reason, identifier

PL = {"WHER": "where"}
def struct_of(source):
    m = re.match(r"^observed-sh@[0-9a-f]+:(structures/shopify/[^/]+)(?:/([^/]+))?/", source)
    if m:
        return m.group(1) + (f" ({m.group(2)})" if m.group(2) and not m.group(2).endswith(".jsonl") and not m.group(2).endswith(".json") else "")
    m = re.match(r"^sharrwah-knowledge-map:evidence/shopify-engineering/runs/[^/]+/items/([^/]+)/", source)
    if m:
        return "Shopify Engineering blog (" + m.group(1) + ")"
    return source

def ident_of(cid, locator, override):
    ov = (override or "").strip().strip("|").strip()
    if ov:
        return ov
    m = re.search(r"\(id ([^)]+)\)", locator)
    if m:
        return m.group(1)
    m = re.search(r"first route of section ([^:]+):", locator)
    if m:
        return m.group(1)
    q = allc.get(cid, {}).get("quote", "")
    m = re.match(r'^"(?:text|title|label|value|name|identifier|h1)": "(.*)"$', q)
    if m and re.match(r"^line \d+", locator):
        return m.group(1)
    if locator.strip().lower() in ("introduction", "page text", "", "note") and re.match(r"^https?://", allc.get(cid, {}).get("source", "")):
        src = re.sub(r"^https?://", "", allc[cid]["source"].split("#")[0])
        return src + (" (note)" if locator.strip().lower() == "note" else "")
    return locator

statements, log = [], []
seen = set()   # (concern, placement, first cite, statement)

def emit(row, note):
    key = (row["concern_id"], row["placement"], ids(row["cite_ids"])[0], row["statement"])
    if key in seen:
        return False
    seen.add(key)
    statements.append({**{k: row.get(k, "") for k in SCOLS}, "note": note, "origin": row.get("origin", "")})
    return True

def logrow(x, action, reason):
    log.append({"concern_id": x["concern_id"], "placement": x["placement"], "statement": x["statement"][:80],
                "cite_ids": x["cite_ids"], "action": action, "reason": reason})

# ---------- script joins: router and access lines and help links ----------
added_elsewhere = []   # (target concern, candidate) pairs to add after the pass
for i, x in enumerate(cand):
    j = x["join"]
    if j in ("router-where", "router-eligibility", "access-lines", "help-links"):
        dec = {"router-where": router, "router-eligibility": router, "access-lines": access, "help-links": helpl}[j].get(i)
        base = {**x, "origin": j}
        if dec is None or dec[0] == "k":
            note = x["note"]
            if j == "help-links":
                note = "Help Center link to the admin page for this concern; " + x["note"]
            emit(base, note)
            continue
        action, to, why = dec
        if to:
            added_elsewhere.append((to, base, why))
            logrow(x, "dropped", why + f"; added under {to} with the same citation")
        else:
            logrow(x, "dropped", why)

# ---------- first-run candidates ----------
for i, x in enumerate(cand):
    if x["join"] != "first-run":
        continue
    action, scope, reason, idov = first[i]
    cid = ids(x["cite_ids"])[0]
    cr = allc[cid]
    row = {**x, "origin": "first-run", "structure": struct_of(cr["source"]),
           "identifier": ident_of(cid, cr["locator"], idov), "scope": scope}
    if action == "k":
        emit(row, ("first run's citation; " + reason) if reason else "first run's citation")
    elif action.startswith("m:"):
        newp = action[2:]
        assert newp in ("where", "decides", "responsible", "boundary", "reason"), action
        row["placement"] = newp
        emit(row, f"first run's citation, moved from {x['placement']}: {reason}")
        logrow(x, f"moved to {newp}", reason)
    elif action == "d":
        logrow(x, "dropped", reason)
    else:
        raise SystemExit(f"bad action {action} at {i}")

# ---------- statements added under the concern a route or line belongs to ----------
for to, base, why in added_elsewhere:
    row = {**base, "concern_id": to}
    emit(row, f"{base['note']}; added from {base['concern_id']}'s candidates: {why}")

# ---------- store values: keep a key's values where the concern's eligibility statements name the key ----------
def keys_of(stmt):
    try:
        obj = json.loads(stmt[len('"eligibility":'):])
    except Exception:
        return set()
    out = set()
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("entitlements", "features") and isinstance(v, list):
                    out.update((k, z) for z in v if isinstance(z, str))
                elif isinstance(v, (dict, list)):
                    walk(v)
        elif isinstance(o, list):
            for z in o:
                walk(z)
    walk(obj)
    return out

named = collections.defaultdict(set)
for s in statements:
    if s["statement"].startswith('"eligibility":') or s["statement"].startswith("eligibility:"):
        named[s["concern_id"]] |= keys_of(s["statement"]) if s["statement"].startswith('"eligibility":') else set()
sv_by_key = collections.defaultdict(list)
for i, x in enumerate(cand):
    if x["join"] == "store-values":
        kind, key = x["identifier"].split(".", 1)
        sv_by_key[(kind, key)].append((i, x))
        if (kind, key) in named[x["concern_id"]]:
            emit({**x, "origin": "store-values"}, x["note"])
        else:
            targets = sorted(c for c, ks in named.items() if (kind, key) in ks)
            why = "the concern's kept route eligibility no longer names this key (its routes belong to another concern)"
            logrow(x, "dropped", why + (f"; the key's values are kept under {', '.join(targets)}" if targets else ""))
for c, ks in named.items():
    for k in ks:
        for i, x in sv_by_key.get(k, []):
            emit({**x, "concern_id": c, "origin": "store-values"}, x["note"])

wr(os.path.join(WORK, "reviewed-statements.tsv"), SCOLS + ["origin"], statements)
wr(os.path.join(WORK, "review-log.tsv"), ["concern_id", "placement", "statement", "cite_ids", "action", "reason"], log)
cnt = collections.Counter(s["placement"] for s in statements)
print("kept or moved statements:", len(statements), dict(cnt))
print("log rows:", len(log), collections.Counter(r["action"].split(" ")[0] for r in log))
print("by origin:", collections.Counter(s["origin"] for s in statements))
