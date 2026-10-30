"""Check one part of the class's model against its brief (`studies/class-model/briefs/B-extent.md`), and derive what the
part doesn't write: each cell's places, scopes and gaps, from its statement keys.

Usage: python3 -I method/check_class_part.py studies/class-model/scope.tsv
       python3 -I method/check_class_part.py studies/class-model/parts/<domain>-<part> [--concerns IDS] [--areas AREAS]

--concerns and --areas check one batch of a part that runs in batches: only the batch's concerns must land, only the
capabilities of the batch's areas need their cells, and only the candidates of the batch's concerns need rulings. Every
other test runs on all the part's rows. The last batch, and the coordinator, check the whole part without them.

A part is <domain>-anchor, -woocommerce, -backfill-woocommerce, -zid, -backfill-zid, -bigcommerce, -backfill-bigcommerce
or -amend, in that order. A part is checked against the domain's model so far: the parts of the same domain that come
before it. Prints each problem, prefixed with the part it is in, then flags for the reviewer, which are not failures.
Writes the part's `derived.tsv` (for each cell: the placements its evidence supports, its `where` identifiers, the scopes
of its statements and the gaps on its concerns) and `derived-qualities.tsv` (each quality with its key's scope).
Exits 1 if any problem is found.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import CMAP, MODEL, PLATFORMS, PREFIX, PART_ORDER, rows, key, fold, ids, statements, concerns, items

HEADS = {
    "capabilities.tsv": ["cap_id", "area", "capability", "parent", "note"],
    "landings.tsv": ["platform", "concern_id", "cap_id", "join", "join_evidence", "fit", "reading"],
    "cells.tsv": ["cap_id", "platform", "held", "terms", "searched", "reading"],
    "evidence.tsv": ["cap_id", "platform", "supports", "key", "why"],
    "qualities.tsv": ["cap_id", "platform", "quality", "value", "key"],
    "slot-fillers.tsv": ["cap_id", "platform", "filler", "key"],
    "rulings.tsv": ["candidate_id", "ruling", "basis", "keys"],
}
BACKFILL_FILES = ("cells.tsv", "evidence.tsv")          # a back-fill may leave out the others
SCOPE_HEAD = ["platform", "concern_id", "domain", "also", "reason"]
DOMAINS = "ABCDEFG"
HELD = {"statements", "none-held"}
SUPPORTS = {"core", "own-service", "extension-point", "outside", "shows"}
PLACED = SUPPORTS - {"shows"}
FIT = {"clean", "strained"}
problems, flags = [], []
LABEL = [""]


def problem(m):
    problems.append(f"{LABEL[0]}: {m}" if LABEL[0] else m)


def flag(m):
    flags.append(f"{LABEL[0]}: {m}" if LABEL[0] else m)


def plat(token):
    """The platform of a concern id or statement key, or None."""
    for p, x in PREFIX.items():
        if token.startswith(x + "-C-") or token.startswith(x + "-I-"):
            return p
    return None


def semi(s):
    """A `;`-separated list, as the brief writes it."""
    return [x.strip() for x in s.split(";") if x.strip()]


def table(path, head, sink, optional=False):
    if not os.path.exists(path):
        if not optional:
            sink(f"{os.path.basename(path)}: missing")
        return []
    with open(path, encoding="utf-8", newline="") as f:
        raw = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not raw or raw[0] != head:
        sink(f"{os.path.basename(path)}: header must be {' · '.join(head)}")
        return []
    out = []
    for n, r in enumerate(raw[1:], 2):
        if not any(c.strip() for c in r):
            continue
        if len(r) != len(head):
            sink(f"{os.path.basename(path)} line {n}: {len(r)} fields, header has {len(head)}")
            continue
        out.append(dict(zip(head, r)) | {"_line": n})
    return out


def areas_of(domain):
    return {r["area_id"] for r in rows(os.path.join(MODEL, "seed", "km-areas.tsv")) if r["domain"].startswith(domain + " ")}


def all_concerns():
    return {p: {c["concern_id"]: c for c in concerns(p)} for p in PLATFORMS}


def stmt_index():
    return {p: {key(r): r for r in items(p)} for p in PLATFORMS}


def statement_of(k, stm):
    p = plat(k)
    return stm[p].get(k) if p else None


def check_scope(path):
    LABEL[0] = "scope.tsv"
    sc = table(path, SCOPE_HEAD, problem)
    cons = all_concerns()
    seen = {}
    for r in sc:
        p, c = r["platform"], r["concern_id"]
        w = f"line {r['_line']}"
        if p not in PLATFORMS:
            problem(f"{w}: unknown platform {p}"); continue
        if c not in cons[p]:
            problem(f"{w}: {c} is not a concern of {p}")
        if c in seen:
            problem(f"{w}: {c} already on line {seen[c]}")
        seen[c] = r["_line"]
        if r["domain"] not in DOMAINS or len(r["domain"]) != 1:
            problem(f"{w}: domain must be one of {', '.join(DOMAINS)}, not {r['domain']!r}")
        if "," in r["also"] or any(" " in x for x in semi(r["also"])):
            problem(f"{w}: also is `;`-separated")
        if any(d not in DOMAINS or d == r["domain"] for d in semi(r["also"])):
            problem(f"{w}: also lists other domains of A to G")
        if not r["reason"].strip():
            problem(f"{w}: no reason")
    for p in PLATFORMS:
        for c in cons[p]:
            if c not in seen:
                problem(f"{c} has no row")
    dom = {r["concern_id"]: r["domain"] for r in sc}
    reason = {r["concern_id"]: r["reason"] for r in sc}
    split = 0
    for m in rows(os.path.join(CMAP, "matches.tsv")):
        cs = [c for col in ("shopify", "salla", "woocommerce") for c in ids(m[col]) if c in dom]
        ds = [dom[c] for c in cs]
        if len(set(ds)) > 1:
            split += 1
            top = max(set(ds), key=ds.count)
            tie = ds.count(top) * 2 <= len(ds)
            odd = [c for c in cs if tie or dom[c] != top]
            for c in odd:
                if m["match_id"] not in reason[c]:
                    problem(f"{c} is in domain {dom[c]}, apart from {m['match_id']}'s other concerns, and its reason doesn't name {m['match_id']}")
            flag(f"{m['match_id']} is split: " + "; ".join(f"{c} {dom[c]}" for c in cs) + " (for the coordinator's check)")
    counts = {d: sum(1 for r in sc if r["domain"] == d) for d in DOMAINS}
    print("concerns per domain: " + ", ".join(f"{d} {n}" for d, n in counts.items()) + f"; {split} matches split")


def part_kind(name):
    m = re.fullmatch(r"([A-G])-(" + "|".join(PART_ORDER) + ")", name)
    if not m:
        sys.exit(f"{name}: a part is named <domain>-<{'|'.join(PART_ORDER)}>")
    return m.groups()


def load_part(d, sink):
    kind = part_kind(os.path.basename(os.path.normpath(d)))[1]
    out = {}
    for f, h in HEADS.items():
        out[f] = table(os.path.join(d, f), h, sink, optional=kind.startswith("backfill") and f not in BACKFILL_FILES)
    return out


def family(cap, caps):
    """The capability, its ancestors and its descendants."""
    up, x = set(), cap
    while x in caps and x not in up:
        up.add(x)
        x = caps[x]["parent"].strip()
    down, grew = {cap}, True
    while grew:
        grew = False
        for c, r in caps.items():
            if r["parent"].strip() in down and c not in down:
                down.add(c); grew = True
    return up | down


BATCH = {"concerns": None, "areas": None}


def check_part(d):
    name = os.path.basename(os.path.normpath(d))
    domain, kind = part_kind(name)
    LABEL[0] = name
    base = os.path.dirname(os.path.normpath(d))
    order = PART_ORDER.index(kind)
    before = [os.path.join(base, f"{domain}-{k}") for k in PART_ORDER[:order]]
    before = [b for b in before if os.path.isdir(b)]
    later = [os.path.join(base, f"{domain}-{k}") for k in PART_ORDER[order + 1:]]
    later = [b for b in later if os.path.isdir(b)]
    if kind != "anchor" and not any(b.endswith("-anchor") for b in before):
        problem(f"no {domain}-anchor to map onto")
    if not os.path.exists(os.path.join(d, "notes.md")):
        problem("notes.md: missing")

    # earlier parts are read, never judged here: a fault in one is reported once, against it
    prior = []
    for b in before:
        bad = []
        prior.append(load_part(b, bad.append))
        if bad:
            problem(f"{os.path.basename(b)} doesn't pass its own check ({bad[0]}): re-run python3 -I method/check_class_part.py {b}")
    part = load_part(d, problem)
    after = [load_part(b, lambda m: None) for b in later]
    cons, stm = all_concerns(), stmt_index()
    sc = rows(os.path.join(MODEL, "scope.tsv"))
    if not sc:
        problem("studies/class-model/scope.tsv: missing or empty")
    sdom = {r["concern_id"]: r for r in sc}
    areas = areas_of(domain)

    mapped = [k for k in ("woocommerce", "zid", "bigcommerce") if os.path.isdir(os.path.join(base, f"{domain}-{k}"))
              and PART_ORDER.index(k) < order]
    done_before = ["shopify", "salla"] * (kind != "anchor") + mapped
    if kind == "anchor":
        plats = ["shopify", "salla"]
    elif kind in ("woocommerce", "zid", "bigcommerce"):
        plats = [kind]
    elif kind.startswith("backfill"):
        plats = []
        target = kind.split("-", 1)[1]
        if target not in mapped:
            problem(f"{kind} follows the {domain}-{target} part, which hasn't run")
    else:   # amend: the platforms of the concerns it lands
        plats = sorted({r["platform"] for r in part["landings.tsv"]})

    caps_prior = {r["cap_id"]: r for p in prior for r in p["capabilities.tsv"]}
    caps = dict(caps_prior)
    caps_new = set()
    for r in part["capabilities.tsv"]:
        w = f"capabilities.tsv line {r['_line']}"
        if kind.startswith("backfill"):
            problem(f"{w}: a back-fill adds no capabilities"); continue
        mm = re.fullmatch(r"CM-([A-Z]{3})-(\d{3})", r["cap_id"])
        if not mm:
            problem(f"{w}: cap_id must be CM-<area>-nnn"); continue
        if r["cap_id"] in caps:
            problem(f"{w}: {r['cap_id']} already exists")
        if mm.group(1) != r["area"]:
            problem(f"{w}: area {r['area']} differs from the cap_id's {mm.group(1)}")
        if r["area"] not in areas:
            problem(f"{w}: area {r['area']} is not an area of domain {domain}")
        hi = max([int(c[-3:]) for c in caps_prior if c[3:6] == r["area"]] or [0])
        if int(mm.group(2)) <= hi:
            problem(f"{w}: {r['cap_id']} must be numbered past the model's highest in {r['area']} (CM-{r['area']}-{hi:03d})")
        if not r["capability"].strip():
            problem(f"{w}: no name")
        caps[r["cap_id"]] = r
        caps_new.add(r["cap_id"])
    for r in part["capabilities.tsv"]:
        p = r["parent"].strip()
        if p and p not in caps:
            problem(f"capabilities.tsv line {r['_line']}: parent {p} is not a capability of domain {domain}")
        seen, x = set(), r["cap_id"]
        while x in caps and caps[x]["parent"].strip():
            if x in seen:
                problem(f"capabilities.tsv: a cycle of parents through {r['cap_id']}"); break
            seen.add(x); x = caps[x]["parent"].strip()

    # landings: every concern scope.tsv gives this part, exactly once
    land_prior = {r["concern_id"]: r for p in prior for r in p["landings.tsv"]}
    land_later = {r["concern_id"] for p in after for r in p["landings.tsv"]}
    if kind == "amend":
        want = {r["concern_id"] for r in sc if r["domain"] == domain} - set(land_prior) - land_later
    else:
        want = {r["concern_id"] for r in sc if r["domain"] == domain and r["platform"] in plats} - land_later
    landed = {}
    matches = {m["match_id"]: m for m in rows(os.path.join(CMAP, "matches.tsv"))}
    for r in part["landings.tsv"]:
        w = f"landings.tsv line {r['_line']}"
        c, p = r["concern_id"], r["platform"]
        if kind.startswith("backfill"):
            problem(f"{w}: a back-fill lands no concerns"); continue
        if p not in plats:
            problem(f"{w}: platform {p} is not this part's"); continue
        if c not in cons[p]:
            problem(f"{w}: {c} is not a concern of {p}"); continue
        if c in landed:
            problem(f"{w}: {c} already landed on line {landed[c]['_line']}")
        landed[c] = r
        cap = r["cap_id"]
        if cap.startswith("moved:"):
            to = cap[6:]
            if to not in DOMAINS or to == domain:
                problem(f"{w}: moved: names another domain, A to G")
            elif c not in want and sdom.get(c, {}).get("domain") != to:
                problem(f"{w}: scope.tsv gives {c} to neither domain {domain} nor {to}")
            if not r["reading"].strip():
                problem(f"{w}: a moved concern says why in reading")
            continue
        if c not in want:
            problem(f"{w}: scope.tsv doesn't give {c} to domain {domain}")
        if cap not in caps:
            problem(f"{w}: {cap} is not a capability of domain {domain}"); continue
        j = r["join"]
        jk = semi(r["join_evidence"])
        if "," in r["join_evidence"]:
            problem(f"{w}: join_evidence is `;`-separated")
        if j.startswith("match:"):
            mid = j[6:]
            mrow = matches.get(mid)
            if not mrow:
                problem(f"{w}: {mid} is not a Q1 match")
            else:
                held = ids(mrow["shopify"]) + ids(mrow["salla"]) + ids(mrow["woocommerce"])
                if c not in held:
                    problem(f"{w}: {mid} doesn't hold {c}")
        elif j in ("terms", "identifier", "definition", "role"):
            kp = set()
            for k in jk:
                if not statement_of(k, stm):
                    problem(f"{w}: join_evidence {k!r} is not a statement key"); continue
                kp.add(plat(k))
            if len(kp) < 2:
                problem(f"{w}: a {j} join cites keys of both sides in join_evidence")
            if j == "role" and not r["reading"].strip():
                problem(f"{w}: a join on role is a reading, and says why in reading")
        elif j != "single":
            problem(f"{w}: join must be match:<M-id>, terms, identifier, definition, role or single")
        if r["fit"] not in FIT:
            problem(f"{w}: fit must be clean or strained")
        if r["fit"] == "strained" and not r["reading"].strip():
            problem(f"{w}: a strained fit says what doesn't fit in reading")
    if BATCH["concerns"] is not None:
        want &= BATCH["concerns"]
    for c in sorted(want - set(landed)):
        problem(f"landings.tsv: {c} (domain {domain} in scope.tsv) doesn't land")

    # a landing by match sits with another of the match's concerns: same capability, ancestor or descendant
    where_landed = {c: r["cap_id"] for c, r in list(land_prior.items()) + list(landed.items()) if not r["cap_id"].startswith("moved:")}
    for c, r in landed.items():
        if r["join"].startswith("match:") and r["join"][6:] in matches and r["cap_id"] in caps:
            m = matches[r["join"][6:]]
            others = [x for x in ids(m["shopify"]) + ids(m["salla"]) + ids(m["woocommerce"]) if x != c and x in where_landed]
            fam = family(r["cap_id"], caps)
            if not any(where_landed[x] in fam for x in others):
                problem(f"landings.tsv line {r['_line']}: {c} lands by {m['match_id']} in {r['cap_id']}, where none of the match's other concerns landed (nor in its parent or children)")

    # cells and evidence
    cells_prior = {(r["cap_id"], r["platform"]): r for p in prior for r in p["cells.tsv"]}
    cells = {}
    for r in part["cells.tsv"]:
        w = f"cells.tsv line {r['_line']}"
        k = (r["cap_id"], r["platform"])
        if r["cap_id"] not in caps:
            problem(f"{w}: {r['cap_id']} is not a capability of domain {domain}"); continue
        if r["platform"] not in PLATFORMS:
            problem(f"{w}: unknown platform"); continue
        if kind.startswith("backfill"):
            if r["platform"] not in done_before:
                problem(f"{w}: {r['platform']} isn't mapped in domain {domain} yet, so a back-fill writes no cell for it")
        elif kind != "amend" and r["platform"] not in plats:
            problem(f"{w}: {r['platform']} is not this part's platform")
        if k in cells or k in cells_prior:
            problem(f"{w}: a cell for {k[0]} and {k[1]} already exists")
        if r["held"] not in HELD:
            problem(f"{w}: held must be statements or none-held")
        cells[k] = r
    ev = {}
    for r in part["evidence.tsv"]:
        w = f"evidence.tsv line {r['_line']}"
        k = (r["cap_id"], r["platform"])
        if k not in cells:
            problem(f"{w}: no cell in this part for {k[0]} and {k[1]}"); continue
        if r["supports"] not in SUPPORTS:
            problem(f"{w}: supports must be one of {', '.join(sorted(SUPPORTS))}")
        s = statement_of(r["key"], stm)
        if not s:
            problem(f"{w}: {r['key']!r} is not a statement key"); continue
        if plat(r["key"]) != r["platform"]:
            problem(f"{w}: {r['key']} is a statement of {plat(r['key'])}, not {r['platform']}")
        if not r["why"].strip():
            problem(f"{w}: why is empty")
        ev.setdefault(k, []).append((r, s))
        its = [sdom[c] for c in s.get("concern_ids", [s["concern_id"]]) if c in sdom]
        if its and not any(x["domain"] == domain or domain in semi(x["also"]) for x in its):
            flag(f"{w}: {r['key']} is a statement of {', '.join(x['concern_id'] for x in its)}, which scope.tsv gives domain {', '.join(sorted({x['domain'] for x in its}))} without naming {domain} under also")
        if r["supports"] == "core" and re.search(r"partner can request", s.get("note", ""), re.I):
            problem(f"{w}: core on {r['key']}, a permission a partner can request (its note): shows, by the dry run's S7; cite the staff permission for core")
        if r["supports"] == "own-service":
            flag(f"{w}: own-service on {r['key']}: does the statement name {r['platform']}'s company as the maker or provider? ({r['why']})")
    other_terms = {}
    for (c, p), r in list(cells_prior.items()) + list(cells.items()):
        other_terms.setdefault(c, {})[p] = semi(r["terms"])
    for k, r in cells.items():
        w = f"cells.tsv line {r['_line']}"
        e = ev.get(k, [])
        if r["held"] == "statements" and not e:
            problem(f"{w}: held statements, with no evidence rows")
        if r["held"] == "none-held":
            if e:
                problem(f"{w}: none-held, with evidence rows")
            if not r["searched"].strip():
                problem(f"{w}: none-held records the terms it searched, in each language")
            terms = {fold(t) for t in semi(r["searched"])}
            terms |= {fold(t) for p, ts in other_terms.get(k[0], {}).items() if p != k[1] for t in ts if len(t) > 3}
            hits = [key(s) for s in items(k[1]) if any(t in fold(s["identifier"] + " " + s["statement"]) for t in terms)]
            if hits:
                flag(f"{w}: none-held, and {len(hits)} {k[1]} statements match its searched terms or the other platforms' terms for {k[0]}: {', '.join(hits[:8])}{' …' if len(hits) > 8 else ''}")
        if any(x["supports"] in PLACED for x, _ in e) and not r["reading"].strip():
            problem(f"{w}: a placement is a reading, and reading says why")
        core = [s for x, s in e if x["supports"] == "core"]
        if core and all(re.search(r'"released":\s*false', s["statement"]) for s in core):
            flag(f"{w}: core rests only on feature flags that aren't released: shows, by the dry run's rulings (C6)")
        if core and all(s["placement"] == "boundary" for s in core):
            flag(f"{w}: core rests only on boundary statements (API objects, scopes, topics): do they show {k[1]} itself doing it?")
        hay = [fold(s["identifier"] + " " + s["statement"]) for _, s in e]
        hay += [fold(cons[k[1]].get(s["concern_id"], {}).get("platform_terms", "")) for _, s in e]
        for t in semi(r["terms"]):
            if not any(fold(t) in h for h in hay):
                problem(f"{w}: term {t!r} is not in a cited statement or its concern's platform_terms")

    # every landed concern is cited in its capability's cell
    for c, r in landed.items():
        if r["cap_id"].startswith("moved:"):
            continue
        p = r["platform"]
        if not any(c in s.get("concern_ids", [s["concern_id"]]) for _, s in ev.get((r["cap_id"], p), [])):
            if any(s["concern_id"] == c for s in statements(p)):
                problem(f"landings.tsv line {r['_line']}: no evidence row of {r['cap_id']}'s {p} cell cites a statement of {c}")

    # joins not made, for the reviewer: a statement this part cites that a capability of another tree also cites; a Q1
    # match whose concerns landed in more than one tree; a capability of this part with nothing landed in its tree
    def root(c):
        seen = set()
        while c in caps and caps[c]["parent"].strip() and c not in seen:
            seen.add(c); c = caps[c]["parent"].strip()
        return c
    cited = {}
    for pr in prior + [part]:
        for r in pr["evidence.tsv"]:
            if r["cap_id"] in caps:
                cited.setdefault(r["key"], set()).add(r["cap_id"])
    for k in sorted({r["key"] for r in part["evidence.tsv"]}):
        cs = sorted(cited.get(k, ()))
        if len({root(c) for c in cs}) > 1:
            flag(f"evidence: {k} is cited by {', '.join(cs)}, in more than one tree of capabilities: one capability, or one the other's parent?")
    for mid, m in matches.items():
        held = [x for x in ids(m["shopify"]) + ids(m["salla"]) + ids(m["woocommerce"]) if x in where_landed]
        if len(held) > 1 and any(x in landed for x in held) and len({root(where_landed[x]) for x in held}) > 1:
            flag(f"landings: {mid}'s concerns land in more than one tree: " + "; ".join(f"{x} in {where_landed[x]}" for x in held))
    for c, r in landed.items():
        if r["cap_id"].startswith("moved:") or r["cap_id"] not in caps:
            continue
        elsewhere = sorted({cap for k, caps_ in cited.items() if c in (statement_of(k, stm) or {}).get("concern_ids", [k.split("/")[0]])
                            for cap in caps_ if root(cap) != root(r["cap_id"])})
        if elsewhere and r["fit"] == "clean":
            flag(f"landings.tsv line {r['_line']}: {c} is clean in {r['cap_id']}, and its statements are cited in another tree ({', '.join(elsewhere)}): strained, by the dry run's rulings (S1)")
    landed_roots = {root(c) for c in where_landed.values() if c in caps}
    for c in sorted(set(caps) - set(caps_prior)):
        if root(c) not in landed_roots:
            flag(f"capabilities: {c} has no concern landed in its tree of capabilities")

    # one cell per capability and platform
    caps_new = set(caps) - set(caps_prior)
    if kind == "anchor":
        need = {(c, p) for c in caps for p in plats}
    elif kind in ("woocommerce", "zid", "bigcommerce"):
        need = {(c, p) for c in caps for p in plats}
        gap = sorted({(c, p) for c in caps_prior for p in done_before} - set(cells_prior))
        if gap:
            problem(f"the model so far lacks {len(gap)} cells, such as {gap[0][0]} for {gap[0][1]}: its back-fill must run before this part")
    elif kind.startswith("backfill"):
        need = {(c, p) for c in caps for p in done_before}
    else:
        need = {(c, p) for c in caps for p in set(done_before) | set(plats) | {"shopify", "salla"}}
    if BATCH["areas"] is not None:
        need = {(c, p) for c, p in need if caps[c]["area"] in BATCH["areas"]}
    for c, p in sorted(need - set(cells) - set(cells_prior)):
        problem(f"cells.tsv: no cell for {c} and {p}")

    # side files
    inv = {}
    for p in PLATFORMS:
        for r in rows(os.path.join(CMAP, "platforms", p, "inventory.tsv")):
            inv[r["inv_id"]] = p
    for f in ("qualities.tsv", "slot-fillers.tsv"):
        for r in part[f]:
            w = f"{f} line {r['_line']}"
            if r["cap_id"] not in caps:
                problem(f"{w}: {r['cap_id']} is not a capability of domain {domain}")
            k = r["key"]
            if k in inv:
                if inv[k] != r["platform"]:
                    problem(f"{w}: {k} is an inventory entry of {inv[k]}")
            elif statement_of(k, stm):
                if plat(k) != r["platform"]:
                    problem(f"{w}: {k} is a statement of {plat(k)}, not {r['platform']}")
            else:
                problem(f"{w}: {k!r} is neither a statement key nor an inventory id")

    # rulings: the anchor on Shopify–Salla joins, WooCommerce's part on its own concerns' joins
    uc = {u["candidate_id"]: u for u in rows(os.path.join(CMAP, "unclear-matches.tsv"))}
    taken = {c for c, r in landed.items() if not r["cap_id"].startswith("moved:")}
    need_r = set()
    for cid, u in uc.items():
        sh, sa, wc = ids(u["shopify"]), ids(u["salla"]), ids(u["woocommerce"])
        if kind == "anchor" and sh and sa and set(sh + sa) & taken:
            need_r.add(cid)
        if kind == "woocommerce" and set(wc) & taken:
            need_r.add(cid)
    # a ruling is tested on its own keys: the statements it says stand for the candidate, and the capabilities that cite them
    citing = {}
    for pr in prior + [part]:
        for r in pr["evidence.tsv"]:
            if r["cap_id"] in caps:
                citing.setdefault(r["key"], set()).add(r["cap_id"])

    def ancestors(c):
        out, seen = set(), set()
        while c in caps and caps[c]["parent"].strip() and c not in seen:
            seen.add(c); c = caps[c]["parent"].strip(); out.add(c)
        return out
    got_r = set()
    for r in part["rulings.tsv"]:
        w = f"rulings.tsv line {r['_line']}"
        u = uc.get(r["candidate_id"])
        if not u:
            problem(f"{w}: {r['candidate_id']} is not an unclear candidate"); continue
        got_r.add(r["candidate_id"])
        if not r["basis"].strip():
            problem(f"{w}: basis is empty")
        keys = semi(r["keys"])
        for k in keys:
            if not statement_of(k, stm):
                problem(f"{w}: {k!r} is not a statement key")
        sh, sa, wc = ids(u["shopify"]), ids(u["salla"]), ids(u["woocommerce"])
        mine, theirs = (sh, sa) if kind == "anchor" else (wc, sh + sa)
        def kc(k):
            it = statement_of(k, stm)
            return it.get("concern_ids", [it["concern_id"]]) if it else []
        outside = [k for k in keys if statement_of(k, stm) and not set(kc(k)) & set(mine + theirs)]
        if outside:
            problem(f"{w}: keys {', '.join(outside)} aren't statements of {r['candidate_id']}'s concerns")
        km = [k for k in keys if set(kc(k)) & set(mine)]
        kt = [k for k in keys if set(kc(k)) & set(theirs)]
        for side, ks in (("this part's", km), ("the other", kt)):
            cs = {x for k in ks for x in kc(k) if x in (mine if side == "this part's" else theirs)}
            if len(cs) > 1:
                problem(f"{w}: keys of {len(cs)} concerns on {side} side ({', '.join(sorted(cs))}): one row per pair of concerns")
        cm = set().union(*[citing.get(k, set()) for k in km]) if km else set()
        ct = set().union(*[citing.get(k, set()) for k in kt]) if kt else set()
        ru = r["ruling"]
        if ru.startswith("joined:") or ru.startswith("nested:"):
            cap = ru.split(":", 1)[1]
            if cap not in caps:
                problem(f"{w}: {cap} is not a capability"); continue
            if not km or not kt:
                problem(f"{w}: {ru} names keys of both sides of the candidate in keys")
            elif ru.startswith("joined:") and not (cap in cm and cap in ct):
                if kind in ("woocommerce", "zid", "bigcommerce") and cap in caps_new:
                    flag(f"{w}: joined:{cap}, a capability this part adds: it holds once its back-fill writes the other side's cell, and the merge re-tests it")
                else:
                    problem(f"{w}: joined:{cap}, but {cap}'s cells don't cite keys of both sides")
            elif ru.startswith("nested:") and not ((cap in cm and ancestors(cap) & ct) or (cap in ct and ancestors(cap) & cm)):
                problem(f"{w}: nested:{cap}, but its keys aren't cited in {cap} on one side and in a parent of it on the other")
        elif ru == "apart":
            both = cm & ct
            if both:
                problem(f"{w}: apart, but {', '.join(sorted(both))} cites keys of both sides: joined?")
        else:
            problem(f"{w}: ruling must be joined:<cap_id>, nested:<cap_id> or apart")
    if BATCH["concerns"] is not None:
        # a batch rules on a pair once both its sides have landed: the batch that lands the second side
        def both_landed(cid):
            u = uc[cid]
            if kind == "anchor":
                return any(x in where_landed for x in ids(u["shopify"])) and any(x in where_landed for x in ids(u["salla"]))
            return True
        need_r = {cid for cid in need_r if set(ids(uc[cid]["shopify"]) + ids(uc[cid]["salla"]) + ids(uc[cid]["woocommerce"])) & BATCH["concerns"]
                  and both_landed(cid)}
    for cid in sorted(need_r - got_r):
        problem(f"rulings.tsv: no ruling on {cid}, which holds concerns whose join this part decides")

    # derived: what the part doesn't write
    gaps = {}
    for p in PLATFORMS:
        for g in rows(os.path.join(CMAP, "platforms", p, "gaps.tsv")):
            gaps.setdefault(g["concern_id"], []).append(f"{g['concern_id']}/{g['placement']}:{g['gap_kind']}")

    def clean(v):
        return v.replace("\t", " ").replace("\n", " ")
    with open(os.path.join(d, "derived.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("cap_id\tplatform\theld\tplaced_as\twhere\tscopes\tgaps\town_scopes\n")
        for k in sorted(cells):
            r = cells[k]
            e = ev.get(k, [])
            placed = sorted({x["supports"] for x, _ in e} & PLACED) or (["not-stated"] if r["held"] == "statements" else [])
            where = sorted({" ".join(s["identifier"].split()) for _, s in e if s["placement"] == "where"})
            scopes = sorted({f"{key(s)}={' '.join(s['scope'].split())}" for _, s in e if s["scope"].strip()})
            cs = sorted({s["concern_id"] for _, s in e})
            g = [x for c in cs for x in gaps.get(c, [])]
            own = [s for x, s in e if x["supports"] in ("core", "own-service")]
            own_scopes = "" if not own else ("general" if any(not s["scope"].strip() for s in own)
                                               else " | ".join(sorted({" ".join(s["scope"].split()) for s in own})))
            f.write("\t".join(clean(v) for v in [k[0], k[1], r["held"], ";".join(placed), " | ".join(where), " | ".join(scopes), ";".join(g), own_scopes]) + "\n")
    with open(os.path.join(d, "derived-qualities.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("cap_id\tplatform\tquality\tvalue\tkey\tscope\n")
        for r in part["qualities.tsv"]:
            s = statement_of(r["key"], stm)
            scope = " ".join(s["scope"].split()) if s else ("(an inventory entry)" if r["key"] in inv else "")
            f.write("\t".join(clean(v) for v in [r["cap_id"], r["platform"], r["quality"], r["value"], r["key"], scope]) + "\n")
    print(f"{name}: {len(part['capabilities.tsv'])} capabilities, {len(landed)} landings, {len(cells)} cells, "
          f"{sum(len(v) for v in ev.values())} evidence rows; derived.tsv and derived-qualities.tsv written")


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    t = args[0]
    for opt in ("--concerns", "--areas"):
        if opt in args:
            v = args[args.index(opt) + 1]
            BATCH[opt[2:]] = set(x for x in re.split(r"[,;\s]+", v) if x)
    if t.endswith("scope.tsv"):
        check_scope(t)
    else:
        check_part(t)
    for p in problems:
        print("PROBLEM", p)
    for x in flags:
        print("FLAG", x)
    print(f"{len(problems)} problems, {len(flags)} flags for the reviewer")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
