"""Print what a part of the class's model reads, compactly, so no agent loads the concern map's files whole
(`studies/class-model/briefs/B-extent.md`; PLAN.md, Stage 4).

Usage: python3 -I method/class_slice.py COMMAND [options]

Commands:
  seed      [--domain D]                       the seed's areas, with Shopify's and Salla's own groupings
  concerns  --platform P [--domain D] [--all] [--where]
                                               a platform's concerns: id, name, platform_terms, split_note, and the Q1
                                               matches and unclear candidates that hold each. With --domain, the
                                               concerns scope.tsv gives that domain, then those of other domains that
                                               name it under `also` (read-only). With --all, every concern. --where adds
                                               each concern's `where` identifiers
  statements --platform P --concerns ID[,ID...] [--placement PL] [--width N] [--full]
                                               each statement of those concerns by its key, with its identifier, its
                                               first N characters (200), its scope, and a flag where its note holds
                                               inference
  key       KEY [KEY...]                       statements whole, by key
  search    --platform P --terms "a;b" [--placement PL] [--width N]
                                               every statement of the platform whose identifier or text holds a term,
                                               case and Arabic diacritics ignored, with its concern
  matches   --concerns ID[,ID...]              Q1's matches and unclear candidates that hold any of those concerns
  gaps      --platform P --concerns ID[,ID...] Q1's gaps on those concerns, with their kind
  outscope  --platform P --terms "a;b"         the platform's inventory entries Q1 left out of scope, by term
  model     --domain D [--platform P] [--areas A;B]
                                               the domain's model as written so far, from its parts in
                                               studies/class-model/parts/ (yours included): each capability, its
                                               landed concerns, and each platform's cell (held, terms, the placements
                                               its evidence supports)
  homonyms                                     Q1's list of the same word naming different things
  candidates --domain D --platform P [--all] [--top N] [--width N] [--areas A;B]
                                               for each capability of the domain's model that has no cell for P (or
                                               every one, with --all): P's statements that hold the terms the other
                                               platforms' cells use for it, and their searched terms, ranked by how many
                                               terms each holds, the domain's own concerns first. Leads to read, not
                                               evidence: a cell still cites only what its statements show
  batches   --domain D --platforms P[,P] [--size N]
                                               the domain's concerns for those platforms, cut into batches of about N
                                               concerns (12), by the area its scope reason names, areas kept whole where
                                               they fit: for a part that runs in batches, each by a fresh agent
  uncited   --domain D [--platform P] [--width N]
                                               the statements of the domain's concerns that no evidence row of its parts
                                               cites, by concern

A statement's key is `concern_id/placement/first_cite_id`, unique on every platform's statements.tsv (`/` appears in no
id or placement). Run with python3 -I from the repository's root.
"""
import argparse, glob, csv, os, re, signal, sys, unicodedata

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
csv.field_size_limit(10**9)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CMAP = os.path.join(ROOT, "studies", "concern-map")
MODEL = os.environ.get("CLASS_MODEL_DIR") or os.path.join(ROOT, "studies", "class-model")   # the variable is for tests
PLATFORMS = ("shopify", "salla", "woocommerce", "zid", "bigcommerce")
PREFIX = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
PART_ORDER = ("anchor", "woocommerce", "backfill-woocommerce", "zid", "backfill-zid", "bigcommerce", "backfill-bigcommerce", "amend")
PLACEMENTS = ("where", "decides", "responsible", "boundary", "reason")


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def first_cite(cite_ids):
    return re.split(r"[;\s]+", cite_ids.strip())[0]


def key(r):
    if r.get("inv_id"):
        return r["inv_id"]
    return f"{r['concern_id']}/{r['placement']}/{first_cite(r['cite_ids'])}"


def platform_of(concern_id):
    m = re.match(r"S\d\d-([A-Z]{2})-", concern_id)      # a subject's statement, such as S01-SA-104
    if m:
        concern_id = m.group(1) + "-"
    for p, x in PREFIX.items():
        if concern_id.startswith(x + "-"):
            return p
    sys.exit(f"unknown platform prefix: {concern_id}")


def fold(s):
    """Case, diacritics, hamza seats and tatweel ignored. A broken plural is another word: search singular and plural."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c) and c != "ـ")
    return s.casefold().replace("\u0629", "\u0647").replace("\u0649", "\u064a")   # taa marbuta as haa, alef maqsura as yaa


def hits(term, hay):
    """Is a folded term in a folded text? A short Latin term (four characters or fewer) matches only as a whole word,
    so CLI doesn't match client; any other term, Arabic included, matches as a substring."""
    if len(term) <= 4 and re.fullmatch(r"[a-z0-9]+", term):
        return re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", hay) is not None
    return term in hay


def ids(arg):
    if isinstance(arg, list):
        arg = " ".join(arg)
    return [x for x in re.split(r"[,;\s]+", arg or "") if x]


def clip(s, width):
    s = " ".join(s.split())
    return s if width <= 0 or len(s) <= width else s[:width] + " …"


_cache = {}


def statements(platform):
    if platform not in _cache:
        _cache[platform] = rows(os.path.join(CMAP, "platforms", platform, "statements.tsv"))
    return _cache[platform]


_inv = {}


def inventory_items(platform):
    """The inventory entries Q1 placed in a concern, as citable items: key = the inventory id, placement `inventory`.
    A cell may cite one where no statement covers it (the dry run's rulings, C2)."""
    if platform not in _inv:
        out = []
        for r in rows(os.path.join(CMAP, "platforms", platform, "inventory.tsv")):
            cs = [x for x in re.split(r"[,;\s]+", r.get("concern_ids", "")) if x]
            if not cs or r.get("out_of_scope_reason", "").strip():
                continue
            out.append({"inv_id": r["inv_id"], "concern_id": cs[0], "concern_ids": cs, "placement": "inventory",
                        "structure": r["list"], "identifier": r["entry"], "statement": f"{r['list']}: {r['entry']}",
                        "scope": "", "cite_ids": r["cite_id"], "note": ""})
        _inv[platform] = out
    return _inv[platform]


def items(platform):
    """Statements, then placed inventory entries: everything a part's cell may cite."""
    return statements(platform) + inventory_items(platform)


SUBJ = os.path.join(ROOT, "studies", "subjects")
SUBJECTS_CITED = ("S-01", "S-02")     # the subjects whose points have landed on the model
_subj = {}


def subject_items(platform):
    """The landed subjects' own statements, citable by their id (S01-SA-104), each as the subject recorded it. Only an
    amendment from the subjects' points cites one, where a point's conflict showed the concern map lacks what the
    subject holds (PLAN.md, Stage 4A, "The subjects' points"; briefs/P-points.md)."""
    if platform not in _subj:
        out = []
        for s in SUBJECTS_CITED:
            for r in rows(os.path.join(SUBJ, s, platform, "statements.tsv")):
                out.append({"inv_id": r["stmt_id"], "concern_id": "", "concern_ids": [],
                            "placement": r.get("placement", "") or "subject", "structure": f"{s}'s statements",
                            "identifier": r.get("identifier", ""), "statement": r.get("statement", ""),
                            "scope": r.get("scope", ""), "cite_ids": r.get("cite_ids", ""), "note": r.get("note", ""),
                            "subject": s})
        _subj[platform] = out
    return _subj[platform]


HELD = os.path.join(MODEL, "held")
_held = {}


def held_items(platform):
    """The held pass's entries (briefs/H-held.md): an item of a platform's self-description the concern map never read,
    listed by method/held_entries.py at the repository's commit, citable by its id (ZD-E-00001). Only the coordinator's
    amendments from the held pass cite one."""
    if platform not in _held:
        out = []
        path = os.path.join(HELD, platform, "entries.tsv")
        sel = {}
        if os.path.exists(os.path.join(HELD, "selection.tsv")):
            sel = {r["structure"]: r for r in rows(os.path.join(HELD, "selection.tsv")) if r["platform"] == platform}
        scope = {}      # an entry's scope is what its placement states: a plan, a country, a store
        listed = {r["batch"] for r in rows(os.path.join(HELD, "batches.tsv"))} if os.path.exists(os.path.join(HELD, "batches.tsv")) else set()
        for pp in sorted(glob.glob(os.path.join(HELD, platform, "placements-*.tsv"))):
            if re.search(r"placements-(.+)\.tsv$", pp).group(1) not in listed:
                continue            # a calibration's batch, which never reaches the model
            for r in rows(pp):
                for e in [x.strip() for x in r["entry_id"].split(";") if x.strip()]:
                    if r.get("scope") and e not in scope:
                        scope[e] = r["scope"]
        for r in rows(path) if os.path.exists(path) else []:
            sr = sel.get(r["structure"], {})
            out.append({"inv_id": r["entry_id"], "concern_id": "", "concern_ids": [],
                        "placement": sr.get("placement") or "held", "structure": r["structure"],
                        "identifier": r["structure"], "statement": r["text"], "scope": scope.get(r["entry_id"], ""),
                        "cite_ids": r["entry_id"], "note": "; ".join(x for x in ("the held pass", sr.get("note", "")) if x),
                        "subject": "held"})
        _held[platform] = out
    return _held[platform]


def subject_citations(platform):
    """The citations of what the model cites beyond the concern map: the landed subjects' statements, and the held
    pass's entries, each its own citation (its file and line at the repository's commit)."""
    out = {}
    for s in SUBJECTS_CITED:
        for f in ("citations.tsv", "recorded-citations.tsv"):
            for r in rows(os.path.join(SUBJ, s, platform, f)):
                out[r["cite_id"]] = r
    path = os.path.join(HELD, platform, "entries.tsv")
    for r in rows(path) if os.path.exists(path) else []:
        out[r["entry_id"]] = {"cite_id": r["entry_id"], "source": r["source"], "locator": r["locator"], "quote": r["text"],
                              "source_date": "", "date_basis": "", "accessed": "", "access_path": ""}
    return out


def citable(platform):
    """Everything a cell's evidence may name: the concern map's statements and placed entries; the landed subjects'
    statements, which only the points' amendments cite; and the held pass's entries, which only its amendments cite."""
    return items(platform) + subject_items(platform) + held_items(platform)


def concerns(platform):
    return rows(os.path.join(CMAP, "platforms", platform, "concerns.tsv"))


def scope_rows():
    return rows(os.path.join(MODEL, "scope.tsv"))


def show_statement(r, width, full=False):
    flag = "  [note: inference]" if re.search(r"\binfer", r.get("note", ""), re.I) else ""
    scope = f"  [scope: {r['scope']}]" if r.get("scope", "").strip() else ""
    text = " ".join(r["statement"].split()) if full else clip(r["statement"], width)
    print(f"{key(r)}\t{clip(r['identifier'], 120)}\t{text}{scope}{flag}")
    if full and r.get("note", "").strip():
        print(f"    note: {' '.join(r['note'].split())}")


def cmd_seed(a):
    for r in rows(os.path.join(MODEL, "seed", "km-areas.tsv")):
        if a.domain and not r["domain"].startswith(a.domain + " "):
            continue
        print(f"{r['domain']}\t{r['area_id']}\t{r['area']}\n    Shopify: {r['shopify_own_groupings']}\n    Salla: {r['salla_own_groupings']}")


def cmd_concerns(a):
    cs = concerns(a.platform)
    by_id = {c["concern_id"]: c for c in cs}
    where = {}
    if a.where:
        for r in statements(a.platform):
            if r["placement"] == "where":
                where.setdefault(r["concern_id"], []).append(clip(r["identifier"], 80))

    mt, uc = {}, {}
    for r in rows(os.path.join(CMAP, "matches.tsv")):
        held = ids(r["shopify"]) + ids(r["salla"]) + ids(r["woocommerce"])
        for x in held:
            mt.setdefault(x, []).append(f"{r['match_id']} ({' '.join(held)})")
    for r in rows(os.path.join(CMAP, "unclear-matches.tsv")):
        held = ids(r["shopify"]) + ids(r["salla"]) + ids(r["woocommerce"])
        for x in held:
            uc.setdefault(x, []).append(f"{r['candidate_id']} ({' '.join(held)})")

    def show(c, tag=""):
        extra = f"  split: {clip(c['split_note'], 160)}" if c.get("split_note", "").strip() else ""
        print(f"{c['concern_id']}{tag}\t{c['concern']}\t{clip(c['platform_terms'], 200)}{extra}")
        if c["concern_id"] in mt:
            print(f"    Q1 matches: {'; '.join(mt[c['concern_id']])}")
        if c["concern_id"] in uc:
            print(f"    unclear candidates: {'; '.join(uc[c['concern_id']])}")
        if a.where:
            print(f"    where: {'; '.join(where.get(c['concern_id'], [])) or '(none)'}")

    if a.all or not a.domain:
        for c in cs:
            show(c)
        return
    sc = [r for r in scope_rows() if r["platform"] == a.platform]
    if not sc:
        sys.exit("studies/class-model/scope.tsv holds no rows for this platform yet")
    own = [r["concern_id"] for r in sc if r["domain"] == a.domain]
    also = [r for r in sc if r["domain"] != a.domain and a.domain in ids(r.get("also", ""))]
    print(f"# {len(own)} concerns of domain {a.domain}")
    for cid in own:
        show(by_id[cid])
    print(f"# {len(also)} concerns of other domains that name {a.domain} under `also` (read-only: cite, never land)")
    for r in also:
        show(by_id[r["concern_id"]], f" (domain {r['domain']})")


def cmd_statements(a):
    want = set(ids(a.concerns))
    n = 0
    for r in statements(a.platform):
        if r["concern_id"] in want and (not a.placement or r["placement"] == a.placement):
            show_statement(r, a.width, a.full)
            n += 1
    m = 0
    if not a.placement or a.placement == "inventory":
        for r in inventory_items(a.platform):
            if set(r["concern_ids"]) & want:
                show_statement(r, a.width, a.full)
                m += 1
    print(f"# {n} statements, and {m} inventory entries Q1 placed in these concerns (cite one by its id where no statement covers it)")


def cmd_key(a):
    for k in a.keys:
        p = platform_of(k)
        hit = [r for r in citable(p) if key(r) == k or (re.fullmatch(r"[A-Z]{2}-S-\d{4}", k) and key(r).endswith("/" + k))]
        if not hit:
            print(f"{k}\tNOT FOUND")
        for r in hit:
            show_statement(r, 0, True)


def cmd_search(a):
    if "," in a.terms and ";" not in a.terms:
        print("# note: terms are ;-separated; a comma is part of one term", file=sys.stderr)
    terms = [fold(t) for t in a.terms.split(";") if t.strip()]
    n = 0
    for r in items(a.platform):
        if a.placement and r["placement"] != a.placement:
            continue
        hay = fold(r["identifier"] + " " + r["statement"])
        if any(hits(t, hay) for t in terms):
            show_statement(r, a.width)
            n += 1
    print(f"# {n} statements and placed inventory entries match (an inventory entry's key is its id)")


def cmd_matches(a):
    want = set(ids(a.concerns))
    for r in rows(os.path.join(CMAP, "matches.tsv")):
        cs = set(ids(r["shopify"]) + ids(r["salla"]) + ids(r["woocommerce"]))
        if cs & want:
            print(f"{r['match_id']}\tshopify: {r['shopify']}\tsalla: {r['salla']}\twoocommerce: {r['woocommerce']}"
                  f"\n    basis: {clip(r['basis'], 0)}\n    granularity: {clip(r['granularity'], 0)}\n    note: {clip(r['note'], 0)}")
    for r in rows(os.path.join(CMAP, "unclear-matches.tsv")):
        cs = set(ids(r["shopify"]) + ids(r["salla"]) + ids(r["woocommerce"]))
        if cs & want:
            print(f"{r['candidate_id']}\tshopify: {r['shopify']}\tsalla: {r['salla']}\twoocommerce: {r['woocommerce']}"
                  f"\n    why_unclear: {clip(r['why_unclear'], 0)}\n    what_would_settle_it: {clip(r['what_would_settle_it'], 0)}")
    print("# Q1's matches and unclear candidates cover Shopify, Salla and WooCommerce only; Zid and BigCommerce were never matched")


def cmd_gaps(a):
    want = set(ids(a.concerns))
    for r in rows(os.path.join(CMAP, "platforms", a.platform, "gaps.tsv")):
        if r["concern_id"] in want:
            print(f"{r['concern_id']}/{r['placement']}\t{r['gap_kind']}\t{clip(r['what_would_show_it'], 200)}")


def cmd_outscope(a):
    if "," in a.terms and ";" not in a.terms:
        print("# note: terms are ;-separated; a comma is part of one term", file=sys.stderr)
    terms = [fold(t) for t in a.terms.split(";") if t.strip()]
    for r in rows(os.path.join(CMAP, "map", "out-of-scope.tsv")):
        if r.get("platform") != a.platform:
            continue
        if any(t in fold(" ".join(r.values())) for t in terms):
            print("\t".join(clip(v, 160) for v in r.values()))


def cmd_homonyms(a):
    text = open(os.path.join(CMAP, "matching-notes.md"), encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(text) if "The same word naming different things" in l)
    out = [text[start]]
    for l in text[start + 1:]:
        if re.match(r"^\d+\. \*\*|^#", l):
            break
        out.append(l)
    print("\n".join(out).rstrip())


def cmd_candidates(a):
    caps, cells = {}, {}
    for d in part_dirs(a.domain):
        for r in rows(os.path.join(d, "capabilities.tsv")):
            caps[r["cap_id"]] = r
        for r in rows(os.path.join(d, "cells.tsv")):
            cells.setdefault(r["cap_id"], {})[r["platform"]] = r
    dom = {r["concern_id"]: r for r in scope_rows()}
    st = items(a.platform)
    hay = [(r, fold(r["identifier"] + " " + r["statement"])) for r in st]
    keep = set(ids(a.areas)) if a.areas else None
    for cid in sorted(caps):
        if keep and caps[cid]["area"] not in keep:
            continue
        have = cells.get(cid, {})
        if a.platform in have and not a.all:
            continue
        terms = set()
        for p, r in have.items():
            if p == a.platform:
                continue
            terms |= {t.strip() for t in (r["terms"] + ";" + r["searched"]).split(";") if len(t.strip()) > 2}
        folded = {fold(t): t for t in terms}
        scored = []
        for r, h in hay:
            hit = [t for f, t in folded.items() if hits(f, h)]
            if hit:
                d = dom.get(r["concern_id"], {})
                mine = d.get("domain") == a.domain or a.domain in ids(d.get("also", ""))
                scored.append((-len(hit), 0 if mine else 1, key(r), r, hit, d.get("domain", "?")))
        scored.sort(key=lambda x: (x[0], x[1], x[2]))
        print(f"## {cid}\t{caps[cid]['capability']}\n   terms: {'; '.join(sorted(terms)) or '(none)'}\n   {len(scored)} statements hold a term")
        for neg, _, k, r, hit, d in scored[:a.top]:
            print(f"   {k}\t[{d}] {clip(r['identifier'], 60)}\t{clip(r['statement'], a.width)}\t({'; '.join(hit[:4])})")


def cmd_batches(a):
    plats = [x for x in re.split(r"[,;\s]+", a.platforms) if x]
    areas = [r["area_id"] for r in rows(os.path.join(MODEL, "seed", "km-areas.tsv")) if r["domain"].startswith(a.domain + " ")]
    by = {x: [] for x in areas + ["?"]}
    for r in scope_rows():
        if r["domain"] == a.domain and r["platform"] in plats:
            found = [x for x in re.findall(r"\(([A-Z0-9]{3})\)", r["reason"]) if x in areas]
            by[found[0] if found else "?"].append(r["concern_id"])
    batches, cur, cur_areas = [], [], []
    for ar in areas + ["?"]:
        cs = by[ar]
        if not cs:
            continue
        if cur and len(cur) + len(cs) > a.size:
            batches.append((cur_areas, cur)); cur, cur_areas = [], []
        while len(cs) > a.size:
            batches.append(([ar], cs[:a.size])); cs = cs[a.size:]
        cur += cs; cur_areas.append(ar)
    if cur:
        batches.append((cur_areas, cur))
    for i, (ar, cs) in enumerate(batches, 1):
        print(f"batch {i}\tareas {';'.join(dict.fromkeys(ar))}\t{len(cs)} concerns\t{','.join(cs)}")


def cmd_uncited(a):
    cited = set()
    for d in part_dirs(a.domain):
        cited |= {r["key"] for r in rows(os.path.join(d, "evidence.tsv"))}
    mine = [r for r in scope_rows() if r["domain"] == a.domain and (not a.platform or r["platform"] == a.platform)]
    n = 0
    for sr in mine:
        left = [r for r in statements(sr["platform"]) if r["concern_id"] == sr["concern_id"] and key(r) not in cited]
        if left:
            print(f"# {sr['concern_id']}: {len(left)} uncited")
            for r in left:
                show_statement(r, a.width)
            n += len(left)
    print(f"# {n} statements of domain {a.domain}'s concerns uncited")


def part_dirs(domain):
    base = os.path.join(MODEL, "parts")
    out = []
    for name in PART_ORDER:
        d = os.path.join(base, f"{domain}-{name}")
        if os.path.isdir(d):
            out.append(d)
    return out


def cmd_model(a):
    caps, land, cells, ev = {}, {}, {}, {}
    for d in part_dirs(a.domain):
        for r in rows(os.path.join(d, "capabilities.tsv")):
            caps[r["cap_id"]] = r
        for r in rows(os.path.join(d, "landings.tsv")):
            land.setdefault(r["cap_id"], []).append(f"{r['concern_id']} ({r['join']})")
        for r in rows(os.path.join(d, "cells.tsv")):
            cells[r["cap_id"], r["platform"]] = r
        for r in rows(os.path.join(d, "evidence.tsv")):
            if r["supports"] != "shows":
                ev.setdefault((r["cap_id"], r["platform"]), set()).add(r["supports"])
    if not caps:
        sys.exit(f"no parts of domain {a.domain} yet")
    keep = set(ids(a.areas)) if a.areas else None
    for cid in sorted(caps):
        c = caps[cid]
        if keep and c["area"] not in keep:
            continue
        par = f"  parent {c['parent']}" if c.get("parent", "").strip() else ""
        print(f"{cid}\t{c['area']}\t{c['capability']}{par}\n    landed: {', '.join(land.get(cid, [])) or '(none)'}")
        for p in PLATFORMS:
            if a.platform and p != a.platform:
                continue
            cell = cells.get((cid, p))
            if cell:
                placed = ";".join(sorted(ev.get((cid, p), []))) or ("not-stated" if cell["held"] == "statements" else "")
                print(f"    {p}: {cell['held']}  terms: {clip(cell['terms'], 120)}  placed: {placed}")


def cmd_caps(a):
    if "," in a.terms and ";" not in a.terms:
        print("# note: terms are ;-separated; a comma is part of one term", file=sys.stderr)
    """Capabilities of every domain whose name, note or cells' terms hold one of the terms: before adding a capability,
    check that no other domain holds the same thing."""
    want = [fold(t.strip()) for t in a.terms.split(";") if t.strip()]
    base = os.path.join(MODEL, "parts")
    caps, terms = {}, {}
    for d in sorted(os.listdir(base)):
        for r in rows(os.path.join(base, d, "capabilities.tsv")):
            caps[r["cap_id"]] = (d.split("-")[0], r)
        for r in rows(os.path.join(base, d, "cells.tsv")):
            terms.setdefault(r["cap_id"], []).append(r["terms"])
    for cid in sorted(caps):
        dom, r = caps[cid]
        hay = fold(" ".join([r["capability"], r["note"]] + terms.get(cid, [])))
        hit = [t for t in want if hits(t, hay)]
        if hit:
            print(f"{cid}\t[{dom}] {clip(r['capability'], a.width)}\t({'; '.join(hit)})")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("seed"); s.add_argument("--domain")
    s = sub.add_parser("concerns"); s.add_argument("--platform", required=True, choices=PLATFORMS)
    s.add_argument("--domain"); s.add_argument("--all", action="store_true"); s.add_argument("--where", action="store_true")
    s = sub.add_parser("statements"); s.add_argument("--platform", required=True, choices=PLATFORMS)
    s.add_argument("--concerns", required=True, nargs="+"); s.add_argument("--placement", choices=PLACEMENTS + ("inventory",))
    s.add_argument("--width", type=int, default=200); s.add_argument("--full", action="store_true")
    s = sub.add_parser("key"); s.add_argument("keys", nargs="+")
    s = sub.add_parser("search"); s.add_argument("--platform", required=True, choices=PLATFORMS)
    s.add_argument("--terms", required=True); s.add_argument("--placement", choices=PLACEMENTS)
    s.add_argument("--width", type=int, default=160)
    s = sub.add_parser("matches"); s.add_argument("--concerns", required=True, nargs="+")
    s = sub.add_parser("gaps"); s.add_argument("--platform", required=True, choices=PLATFORMS); s.add_argument("--concerns", required=True, nargs="+")
    s = sub.add_parser("outscope"); s.add_argument("--platform", required=True, choices=PLATFORMS); s.add_argument("--terms", required=True)
    s = sub.add_parser("model"); s.add_argument("--domain", required=True); s.add_argument("--platform", choices=PLATFORMS); s.add_argument("--areas")
    sub.add_parser("homonyms")
    s = sub.add_parser("candidates"); s.add_argument("--domain", required=True); s.add_argument("--platform", required=True, choices=PLATFORMS)
    s.add_argument("--all", action="store_true"); s.add_argument("--top", type=int, default=10); s.add_argument("--width", type=int, default=120); s.add_argument("--areas")
    s = sub.add_parser("batches"); s.add_argument("--domain", required=True); s.add_argument("--platforms", required=True); s.add_argument("--size", type=int, default=12)
    s = sub.add_parser("uncited"); s.add_argument("--domain", required=True); s.add_argument("--platform", choices=PLATFORMS); s.add_argument("--width", type=int, default=120)
    s = sub.add_parser("caps"); s.add_argument("--terms", required=True); s.add_argument("--width", type=int, default=140)
    a = ap.parse_args()
    globals()["cmd_" + a.cmd](a)


if __name__ == "__main__":
    main()
