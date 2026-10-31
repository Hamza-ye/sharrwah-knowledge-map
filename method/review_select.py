"""Select what the final review of the class's model's extent reads, by risk, and check what the reviewers write
(PLAN.md, Stage 4A: "An independent review of the whole extent"; the method report, sections 7, 13 and 18; the brief
`studies/class-model/briefs/R-extent.md` and its design `briefs/R-extent-design.md`; the inspection
`studies/class-model/inspection-Q3R.md`, part 2).

    python3 -I method/review_select.py [select] [--out PATH] [--since 9d204b46] [--seed 20261030] [--batch-size 30]
    python3 -I method/review_select.py check --share N --batch B [--selection PATH] [--review-dir DIR]
    python3 -I method/review_select.py rates [--selection PATH] [--review-dir DIR]

Run `select` once, after the last landing before the final review (the second stage's, the qualities pass's and the
omission review's batches applied, the model merged), and commit the selection: its commit is the one the reviewers'
messages name. It writes studies/class-model/review/selection.tsv (or --out), one row per item. An item is a cell (a
capability on one platform), a capability, or a question that is neither, with every reason it was chosen. Reasons:

From the merge (as on 30 October):
- kind: a cell its capability's kind hinges on (the one cell of a class whose count is 1; every cell of a slot or open);
- count: a cell of a class held with statements but placed neither core nor own-service, which would change the count;
- none-held: a cell with nothing held where the platform's own statements hold two or more of the other platforms'
  terms for it, the leads a false none-held leaves;
- role: a landing joined on role, a reading; terms-homonym: a landing joined on a term Q1 lists as a homonym;
- own-service: a placement as the platform company's own service, on maker evidence;
- scope: a class that holds only under a plan, a beta or an observed store (its class_scope isn't general);
- strained: a capability with landings marked strained, and the merge's `strained?` flags on it, one item per capability;
- flag: the merge's questions (merged/flags.tsv): counted twice with a cell resting on the statement alone, one item
  for the other counted-twice flags, ruled differently, and `one capability?` by risk: every pair sharing
  --one-cap-terms terms or more, every pair with a capability made since --since, every pair flagged at --since, and a
  seeded tenth of the rest;
- coordinator: every row the coordinator wrote or changed in the parts' files or scope.tsv, every line of the parts'
  notes that names the coordinator; and every held line whose reading names the coordinator's check, correction or
  alignment (not a line that only cites a coordinator's ruling, which `ruling` samples, nor one placed by script,
  which `batch` samples), one item per cell;
- lead: every line of a part's notes, or of the held pass's notes and digests, that names the final review or the
  reviewer; a capability whose cells cite only inventory entries;
- q3: every candidate miss and unclear row of Q3's check, every beyond-the-class row the model doesn't answer, and a
  seeded tenth of its covered rows;
- point: every subject's variation point whose drafted landing found a conflict, and a seeded tenth of the rest;
- sample: a seeded sample of each part's other cells, at least two or the fraction given (--sample, raised for a
  platform by --platform-sample), whichever is larger, leaving out the cells the omission review sampled.

From the held pass on:
- changed: a cell whose placement changed since the merge of 30 October (--since) so that it now counts, or no longer
  counts (core or own-service), and every changed cell of a capability whose kind changed;
- new-cap: every cell of a capability made since --since, and every changed cell of a capability widened since (its
  definition changed);
- ruling: for each high-weight ruling from the held pass on in reports/GM-rulings.md, a seeded sample of the held lines
  whose reading names it (one per platform it reaches, then up to --ruling-min, or --ruling-rate of its lines,
  whichever is larger), so that each ruling's application is tested on each platform;
- batch: a seeded sample of every batch of the held pass and its later stages (held/batches.tsv), --batch-lines lines
  each, from the lines no other reason took, leaving out what the omission review sampled;
- s2-lead: the second stage's leads that name only held cells (its coordinator's decision 1), by risk: a lead whose
  words name a maker, a support value a cell it names lacks, or a quality;
- s2-note: a bullet of the second stage's notes (held/<platform>/s2/<part>.md) on a held cell a passage would change
  (S2-R2; its coordinator's decision 7);
- ql-note: a bullet of the qualities pass's notes (qualities/<platform>/<part>.md) on a placement (QL-R8);
- omission: the omission review's findings that don't land (omission/<part>-items.tsv: miss `support` or `out`,
  verdict `unclear`, an `absorbed` capability), each finding row of an OM- part that gives a cell core or
  own-service, and a seeded tenth of its `held` verdicts, which `rates` counts as that review's own miss rate (the
  coordinator's decision 11 on its design).

A reason whose inputs don't exist yet selects nothing, and the summary says so.
"""
import argparse, collections, glob, math, os, random, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, ROOT, rows, fold, items, citable, key, hits

MERGED = os.path.join(MODEL, "merged")
HELD = os.path.join(MODEL, "held")
OMISSION = os.path.join(MODEL, "omission")
QUALITIES = os.path.join(MODEL, "qualities")
REVIEW = os.path.join(MODEL, "review")
OUT = os.path.join(REVIEW, "selection.tsv")
GM = os.environ.get("GM_RULINGS") or os.path.join(ROOT, "reports", "GM-rulings.md")   # the variable is for tests
SHARES = {"A": "1", "B": "1", "C": "2", "D": "3", "E": "4", "F": "4", "G": "4"}
NO_DOMAIN = "5"         # an item with no capability: a held line placed `out` or on a new thing not yet decided
OWN = {"core", "own-service"}
VALUES = ("core", "own-service", "extension-point", "outside", "shows")
HOMONYMS = ["supported countries", "complaint", "log", "rate limit", "mcp", "ucp", "order limit"]
MARK = re.compile(r"\(the coordinator|the coordinator, ")
CAP = re.compile(r"\bCM-[A-Z0-9]{3}-\d{3}\b")
ROW_ID = re.compile(r"\b[A-Z]{2}-(?:C-\d{3}|S-\d{4}|I-\d{4}|E-[0-9a-f]{8})|\bU-\d{3}\b|\bM-\d{3}\b")
HEAD_COV = ["item", "verdict", "severity", "basis", "correction", "what_would_settle_it"]
HEAD_SEL = ["item", "reasons", "cap_id", "platform", "detail", "share", "batch"]
OM_PLATFORM = {"ZD": "zid", "SH": "shopify", "SA": "salla", "BC": "bigcommerce", "WC": "woocommerce"}

# A held line names the coordinator's own correction or alignment (the `coordinator` reason) ...
COORD_LINE = re.compile(r"the coordinator", re.I)
# ... unless it only cites a ruling the coordinator made or confirmed (sampled by `ruling`), or was placed by script
COORD_RULING_ONLY = re.compile(r"the coordinator'?s'? (?:ruling|rulings|decision|message)|which the coordinator confirmed|"
                               r"as the coordinator ruled|the coordinator ruled", re.I)
COORD_SCRIPT = re.compile(r"placed by the coordinator, by script", re.I)

# The rulings whose handle names no line, or names lines of other rulings too: what their lines say instead
# (each a reading of the ruling's own words in reports/GM-rulings.md)
RULING_PATTERN = {
    "Flags, badges and release states":
        r"early access|released\W{0,3}(?:false|true)|is_experimental|disable_ui|feature_flags|hashed beta|admin-betas|"
        r"\bbetas?\W{0,3}(?:enabled|true|false|on|off)|\bD1\b|feature test drive",
    "A maker field counts only where merchants are shown it": r"is_built_by_wc|made_in_woo|Built by WooCommerce",
    "A store's llms.txt is a file for search": r"llms",
    "Only a route's own gates on the store are its scope": r"ancestor's gate|ancestors' gates",
    "Once a new thing is a capability, each line's support is what its entry shows": "new-caps",
}
HANDLE_STOP = re.compile(r";|, (?:extending|with|refined|a limit|the join|and its|the second|the third|the first|in part)")


def seed_domains():
    return {r["area_id"]: r["domain"].split(" ")[0] for r in rows(os.path.join(MODEL, "seed", "km-areas.tsv"))}


def share_of(cap, part=None, areas=None):
    if part:
        return SHARES.get(part.split("-")[0], "4")
    m = re.match(r"CM-([A-Z0-9]{3})-", cap or "")
    if not m:
        return NO_DOMAIN
    return SHARES.get((areas or {}).get(m.group(1), ""), "4")


def rel(path):
    return os.path.relpath(path, MODEL)


def clip(s, n):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[:n] + " …"


def semi(s):
    return [x.strip() for x in re.split(r"[;,]", s or "") if x.strip()]


def at_since(a, name):
    """A merged file as it stood at the merge of 30 October: --since-dir for tests, else the commit --since."""
    if a.since_dir:
        p = os.path.join(a.since_dir, name)
        return rows(p) if os.path.exists(p) else []
    try:
        t = subprocess.run(["git", "-C", ROOT, "show", f"{a.since}:studies/class-model/merged/{name}"],
                           capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        sys.exit(f"git show {a.since}:studies/class-model/merged/{name} failed: {e}")
    import csv, io
    return list(csv.DictReader(io.StringIO(t), delimiter="\t", quoting=csv.QUOTE_NONE))


def held_lines():
    """The held pass's lines and its later stages' (held/<platform>/placements-<batch>.tsv), of the batches
    held/batches.tsv lists (a calibration's batch never reaches the model), each with its batch, file and line."""
    listed = {r["batch"] for r in rows(os.path.join(HELD, "batches.tsv"))}
    out = []
    for p in PLATFORMS:
        for path in sorted(glob.glob(os.path.join(HELD, p, "placements-*.tsv"))):
            b = re.search(r"placements-(.+)\.tsv$", path).group(1)
            if b not in listed:
                continue
            for i, r in enumerate(rows(path), 2):
                out.append(dict(r, _batch=b, _platform=p, _file=rel(path), _line=i))
    return out, listed


def line_ref(L):
    return f"{L['_file']} line {L['_line']} ({L['_batch']} {L['entry_id']}: {L['placement']} {L.get('cap_id', '')} {L.get('supports', '')})".replace("  ", " ")


def gm_rulings(path):
    """The high-weight rulings from the held pass on in reports/GM-rulings.md: each `####` entry whose weight is high,
    and each table row whose weight cell begins 'high', with its title and handle (the parenthesis that ends its
    Decides line, or the table row's first cell)."""
    if not os.path.exists(path):
        return [], [f"no {path}"]
    t = open(path, encoding="utf-8").read()
    i = t.find("\n## From the held pass on")
    if i < 0:
        return [], [f"{path} has no section '## From the held pass on'"]
    held = t[i:]
    out, problems = [], []
    for b in re.split(r"\n(?=#### )", held):
        if not b.startswith("#### "):
            continue
        title = b.split("\n")[0][5:].strip()
        w = re.search(r"\*\*Weight:\*\*\s*(\w+)", b)
        if w and w.group(1).lower() == "high":
            d = re.search(r"\*\*Decides:\*\*(.*)", b)
            h = re.findall(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)\s*$", d.group(1).strip()) if d else []
            out.append({"title": title, "handle": h[-1] if h else "", "block": b})
        for l in b.split("\n"):
            if l.startswith("| ") and not l.startswith("| ---"):
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                if any(re.match(r"high\b", c) for c in cells[1:]):
                    first = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", cells[0])
                    hm = re.findall(r"\(([^()]*)\)", first)
                    out.append({"title": clip(first, 90), "handle": hm[-1] if hm else "", "block": l, "row": True})
    return out, problems


def ruling_pattern(r, new_rows):
    """The regex a line's reading matches where it names the ruling, or 'cap:<id>' / 'new-caps', or None."""
    for k, v in RULING_PATTERN.items():
        if r["title"].startswith(k):
            return v
    m = re.search(r"\((N\d\d)\b", r["title"])
    if m and m.group(1) in new_rows:
        return "cap:" + new_rows[m.group(1)]
    h = HANDLE_STOP.split(r["handle"])[0] if r["handle"] else ""
    pats = [rf"\bM-{n}(?!\d)" for n in re.findall(r"\bM-(\d+)\b", h)]
    for m in re.finditer(r"rulings? after ((?:[A-Z]{2}-\d+(?:,? (?:and )?|\b))+)", h):
        for x in re.findall(r"[A-Z]{2}-\d+", m.group(1)):
            pats.append(rf"rulings? after (?:[A-Z]{{2}}-\d+(?:,| and| or)? ?)*{x}(?!\d)")
    pats += [rf"\b{x}\b" for x in re.findall(r"\bS\d+\b", h)]
    if r.get("row"):
        pats += [rf"\b{re.escape(x)}(?![\d.])" for x in re.findall(r"\b(?:R\d+\.\d+|E\d+|D\d+)\b", h)]
        pats += [rf"\brule {x}(?!\d)" for x in re.findall(r"\brule (\d+)\b", h)]
    return "|".join(pats) or None


DIGEST = {"Editions": "editions", "changelog": "changelog", "router": "admin-router", "Router": "admin-router"}


def ruling_batches(r, structures):
    """A digest's table row applies to its structure's batches only: the batches whose structures name it."""
    if not r.get("row"):
        return None
    w = next((v for k, v in DIGEST.items() if r["title"].startswith(k)), None)
    return {b for b, s in structures.items() if w and w in s} if w else None


def note_bullets(path, heading, line):
    """The top-level bullets of a notes file in a section whose heading matches `heading`, with their nested lines, and
    any bullet elsewhere that matches `line`: each (line number, text)."""
    if not os.path.exists(path):
        return []
    ls = open(path, encoding="utf-8").read().split("\n")
    out, sec, cur = [], None, None
    for i, l in enumerate(ls, 1):
        h = re.match(r"^(#+)\s+(.*)", l)
        if h:
            if cur:
                out.append(cur); cur = None
            lev = len(h.group(1))
            if sec is not None and lev <= sec:
                sec = None
            if sec is None and heading.search(h.group(2)):
                sec = lev
            continue
        top = re.match(r"^[-*] ", l)
        if top or (not l.strip() and cur):
            if cur:
                out.append(cur); cur = None
            if top and (sec is not None or line.search(l)):
                cur = [i, l]
            continue
        if cur and (l.startswith((" ", "\t"))):
            cur[1] += "\n" + l
    if cur:
        out.append(cur)
    return [(i, t) for i, t in out]


def select(a):
    areas = seed_domains()
    caps = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "capabilities.tsv"))}
    kinds = {r["cap_id"]: r for r in rows(os.path.join(MERGED, "kinds.tsv"))}
    cells = {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(MERGED, "cells.tsv"))}
    ev = rows(os.path.join(MERGED, "evidence.tsv"))
    rnd = random.Random(a.seed)
    found, notes = {}, []          # item key -> item; notes for the summary

    def item(k, cap, plat, part=""):
        return found.setdefault(k, {"reasons": [], "details": [], "cap": cap, "plat": plat, "part": part})

    def add(it, reason, detail):
        if reason not in it["reasons"]:
            it["reasons"].append(reason)
        if detail and detail not in it["details"]:
            it["details"].append(detail)

    def add_cell(cap, plat, reason, detail, part=None):
        add(item(("cell", cap, plat), cap, plat, part or (cells.get((cap, plat)) or {}).get("part", "")), reason, detail)

    other_n = [0]

    def add_other(reason, cap, detail, part=None):
        """A question that isn't one cell's: one item per capability, with every reason; else one of its own."""
        cap = cap or ""
        if CAP.fullmatch(cap):
            add(item(("cap", cap), cap, "", part or ""), reason, detail)
        else:
            other_n[0] += 1
            add(item(("other", other_n[0]), cap, "", part or ""), reason, detail)

    def add_line(L, reason, detail):
        cap, p = L.get("cap_id", ""), L["_platform"]
        if L["placement"] == "capability" and (cap, p) in cells:
            add_cell(cap, p, reason, detail)
        elif L["placement"] == "new" and new_cap.get((p, cap[4:].strip())):
            add_cell(new_cap[(p, cap[4:].strip())], p, reason, detail + f" (the new thing, decided {new_cap[(p, cap[4:].strip())]})")
        else:
            other_n[0] += 1
            add(item(("line", L["_file"], L["_line"]), cap if CAP.fullmatch(cap or "") else "", p, ""), reason, detail)

    placed = {k: set((r.get("placed_as") or "").split(";")) - {""} for k, r in cells.items()}

    # ---------------------------------------------------------------- kind, count, own-service, scope
    for c, k in kinds.items():
        kind = k["kind"]
        if kind == "class" and int(k["count"] or 0) == 1:
            for p in PLATFORMS:
                if placed.get((c, p), set()) & OWN:
                    add_cell(c, p, "kind", "the one cell that makes this capability a class; is it another capability's thing, in any domain? (caps)")
        elif kind != "class":
            for p in PLATFORMS:
                if (c, p) in cells:
                    add_cell(c, p, "kind", f"a cell of a {kind}: a missed core would change the kind")
        if kind == "class" and (k.get("class_scope") or "general") != "general":
            add_other("scope", c, f"a class that holds only under: {k.get('class_scope')}")
    for (c, p), r in cells.items():
        if kinds.get(c, {}).get("kind") == "class" and r["held"] == "statements" and not (placed[(c, p)] & OWN):
            add_cell(c, p, "count", "held, but placed neither core nor own-service: does the platform do it itself after all?")
        if "own-service" in placed[(c, p)]:
            add_cell(c, p, "own-service", "placed as the company's own service: does a statement name the company?")

    # ---------------------------------------------------------------- none-held with leads
    terms_of = {}
    for (c, p), r in cells.items():
        for t in (r.get("terms") or "").split(";"):
            t = fold(t.strip())
            if len(t) > 2:
                terms_of.setdefault(c, {}).setdefault(p, set()).add(t)
    hay = {p: [fold(s["identifier"] + " " + s["statement"]) for s in items(p)] for p in PLATFORMS}
    s2_read = {(r.get("subject", ""), p) for p in PLATFORMS for r in rows(os.path.join(HELD, p, "s2-outcomes.tsv"))
               if r.get("outcome") in ("not-found", "absent", "not-held")}
    n_s2_read = 0
    for (c, p), r in cells.items():
        if r["held"] != "none-held":
            continue
        if (c, p) in s2_read and not a.none_held_all:
            n_s2_read += 1; continue        # the second stage read it against the held pages; the omission review samples it
        ts = set().union(*[v for q, v in terms_of.get(c, {}).items() if q != p] or [set()])
        if len(ts) < 2:
            continue
        best = max((sum(1 for t in ts if hits(t, h)) for h in hay[p]), default=0)
        if best >= 2:
            add_cell(c, p, "none-held", f"nothing held, while one of its statements holds {best} of the other platforms' terms: read candidates")
    notes.append(f"none-held: {n_s2_read} cells the second stage read and left holding nothing are left to the omission review's sample"
                 if s2_read else "none-held: no held/<platform>/s2-outcomes.tsv yet: every none-held cell with leads is read")

    # ---------------------------------------------------------------- joins and strained
    landings = rows(os.path.join(MERGED, "landings.tsv"))
    for r in landings:
        if r["join"] == "role":
            add_cell(r["cap_id"], r["platform"], "role", f"{r['concern_id']} joined on role")
        elif r["join"] == "terms":
            text = fold(r["join_evidence"] + " " + r["reading"])
            hit = [h for h in HOMONYMS if hits(h, text)]
            if hit:
                add_cell(r["cap_id"], r["platform"], "terms-homonym", f"{r['concern_id']} joined on a term Q1 lists as a homonym ({', '.join(hit)})")
    strained = {}
    for r in landings:
        if r["fit"] == "strained":
            strained.setdefault(r["cap_id"], []).append(r["concern_id"])
    for c, cs in sorted(strained.items()):
        add_other("strained", c, f"strained landings: {', '.join(cs)}: should a concern be split out, and where?")

    # ---------------------------------------------------------------- the capabilities made or changed since 30 October
    old_k = {r["cap_id"]: r for r in at_since(a, "kinds.tsv")}
    old_c = {r["cap_id"]: r for r in at_since(a, "capabilities.tsv")}
    made = [c for c in kinds if c not in old_k] if old_k else []
    widened = [c for c in caps if c in old_c and " ".join(caps[c]["capability"].split()) != " ".join(old_c[c]["capability"].split())]

    def counts(v):
        return bool(set((v or "").split(":", 1)[-1].split(";")) & OWN)

    n_changed = 0
    for c in kinds:
        if c not in old_k:
            continue
        kch = kinds[c]["kind"].split(":")[0] != old_k[c]["kind"].split(":")[0]
        for p in PLATFORMS:
            nv, ov = kinds[c].get(p, ""), old_k[c].get(p, "")
            if nv == ov:
                continue
            if counts(nv) != counts(ov) or kch:
                n_changed += 1
                why = "now counts" if counts(nv) and not counts(ov) else "no longer counts" if counts(ov) and not counts(nv) else "changed"
                add_cell(c, p, "changed", f"since {a.since}: {ov or '-'} -> {nv or '-'} ({why}; kind {old_k[c]['kind']} -> {kinds[c]['kind']}, count {old_k[c]['count']} -> {kinds[c]['count']})")
            if c in widened:
                add_cell(c, p, "new-cap", f"widened since {a.since} (its definition changed), and this cell changed: {ov or '-'} -> {nv or '-'}")
    for c in made:
        for p in PLATFORMS:
            if (c, p) in cells:
                add_cell(c, p, "new-cap", f"a capability made since {a.since} ({cells[(c, p)].get('part', '')}): is it a thing of its own, and is this cell right?")
    if not old_k:
        notes.append(f"changed, new-cap: no kinds.tsv at {a.since}: nothing selected")

    # ---------------------------------------------------------------- the merge's questions
    old_flags = {r["flag"] for r in at_since(a, "flags.tsv")}
    loose, one_cap_rest = 0, []
    for r in rows(os.path.join(MERGED, "flags.tsv")):
        cs = list(dict.fromkeys(CAP.findall(r["flag"])))
        if r["kind"] == "counted twice" and "rests on it alone" not in r["flag"]:
            loose += 1; continue
        if r["kind"] == "one capability?":
            m = re.search(r"share terms (.*): one capability\?", r["flag"])
            n = len(m.group(1).split(", ")) if m else 0
            if n >= a.one_cap_terms or any(c in made for c in cs) or r["flag"] in old_flags:
                add_other("flag", cs[0] if cs else "", f"{r['kind']}: {r['flag']}")
            else:
                one_cap_rest.append(r)
            continue
        if r["kind"] == "strained?":
            add_other("strained", cs[0] if cs else "", f"the merge's strained?: {r['flag']}")
            continue
        add_other("flag", cs[0] if cs else "", f"{r['kind']}: {r['flag']}")
    for r in rnd.sample(one_cap_rest, math.ceil(len(one_cap_rest) * 0.1)) if one_cap_rest else []:
        cs = list(dict.fromkeys(CAP.findall(r["flag"])))
        add_other("flag", cs[0] if cs else "", f"{r['kind']} (a seeded tenth of those sharing fewer than {a.one_cap_terms} terms): {r['flag']}")
    if loose:
        add_other("flag", "", f"counted twice: {loose} statements that support core or own-service in two domains with no cell resting on them alone (merged/flags.tsv): settle them together by the brief's rule")
    notes.append(f"flag: `one capability?` {len(one_cap_rest)} pairs below {a.one_cap_terms} shared terms, of which a seeded tenth")

    # ---------------------------------------------------------------- leads and the coordinator, in the parts
    inv_only = {}
    for r in ev:
        inv_only.setdefault(r["cap_id"], set()).add("inv" if re.match(r"^[A-Z]{2}-I-\d{4}$", r["key"]) else "stmt")
    for c, s in inv_only.items():
        if s == {"inv"}:
            add_other("lead", c, "every cell cites inventory entries only: a capability, or does it fold into its parent?")
    base = os.path.join(MODEL, "parts")
    for d in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        for f in ("evidence.tsv", "landings.tsv", "cells.tsv", "capabilities.tsv", "rulings.tsv", "qualities.tsv", "slot-fillers.tsv"):
            for r in rows(os.path.join(base, d, f)):
                if re.match(r"^[A-Z]{2}-E-[0-9a-f]{8,40}$", r.get("key", "")):
                    continue            # a held line, amended in: its coordinator's mark is read from its placements file, by risk
                if MARK.search(" ".join(v or "" for v in r.values())):
                    cap, plat = r.get("cap_id", ""), r.get("platform", "")
                    what = r.get("concern_id") or r.get("key") or r.get("candidate_id") or cap
                    if cap and plat and (cap, plat) in cells:
                        add_cell(cap, plat, "coordinator", f"{d}/{f}: {what}", part=d)
                    else:
                        add_other("coordinator", cap, f"{d}/{f}: {what}", part=d)
        nf = os.path.join(base, d, "notes.md")
        if os.path.exists(nf):
            for i, l in enumerate(open(nf, encoding="utf-8").read().split("\n"), 1):
                low = l.lower()
                if "the coordinator" in low and l.lstrip().startswith(("-", "*", "|")):
                    if CAP.search(l) or ROW_ID.search(l):
                        add_other("coordinator", (CAP.findall(l) or [""])[0], f"{d}/notes.md line {i}: {clip(l, 200)}", part=d)
                    else:               # a line naming no row: the part's such lines are read together, as one item
                        add(item(("notes", d), "", "", d), "coordinator", f"{d}/notes.md line {i}: {clip(l, 200)}")
                elif ("final review" in low or "the reviewer" in low) and l.lstrip().startswith(("-", "*")):
                    add_other("lead", (CAP.findall(l) or [""])[0], f"{d}/notes.md line {i}: {clip(l, 200)}", part=d)
    for r in rows(os.path.join(MODEL, "scope.tsv")):
        if MARK.search(r.get("reason", "")):
            add_other("coordinator", "", f"scope.tsv: {r['concern_id']}: domain {r['domain']}, also {r['also'] or '-'}", part=r["domain"])

    # ---------------------------------------------------------------- the held pass: its notes' leads for the final review
    held_mds = sorted(set(glob.glob(os.path.join(HELD, "*.md")) + glob.glob(os.path.join(HELD, "*", "*.md"))
                          + glob.glob(os.path.join(HELD, "rules", "*.md"))))
    for nf in held_mds:
        if re.search(r"/s2/", nf):
            continue
        for i, l in enumerate(open(nf, encoding="utf-8").read().split("\n"), 1):
            low = l.lower()
            if ("final review" in low or "the reviewer" in low) and not l.startswith("#"):
                plat = next((p for p in PLATFORMS if f"/held/{p}/" in nf), "")
                c = (CAP.findall(l) or [""])[0]
                if plat and c and (c, plat) in cells:
                    add_cell(c, plat, "lead", f"{rel(nf)} line {i}: {clip(l, 200)}")
                else:
                    add_other("lead", c, f"{rel(nf)} line {i}: {clip(l, 200)}")

    # ---------------------------------------------------------------- Q3 and the points
    q3 = []
    for path in sorted(glob.glob(os.path.join(MODEL, "q3", "check-*.tsv"))):
        q3 += rows(path)
    covered = [r for r in q3 if r["result"] == "covered"]
    for r in q3:
        who = r["who_answers"]
        if r["result"].startswith("candidate miss") or r["result"] == "unclear" or (r["result"] == "beyond the class" and "model" not in who) \
                or r.get("rest", "").startswith("candidate miss"):
            add_other("q3", (r["cap_ids"].split(";") or [""])[0], f"Q3's {r['set']}:{r['row_id']}: {r['result']}")
    for r in rnd.sample(covered, max(1, round(len(covered) * 0.1))) if covered else []:
        add_other("q3", (r["cap_ids"].split(";") or [""])[0], f"Q3's {r['set']}:{r['row_id']}: covered (a seeded tenth)")
    pts = []
    for path in sorted(glob.glob(os.path.join(MODEL, "points", "P-*.tsv"))):
        pts += [(os.path.basename(path)[:-4], r) for r in rows(path)]
    landed = [x for x in pts if x[1]["status"] == "landed"]
    scope = {r["concern_id"]: r["domain"] for r in rows(os.path.join(MODEL, "scope.tsv"))}

    def point_part(r):
        """A point landed on none goes to the share of its leads' domain: its basis's first concern."""
        if (r["cap_ids"].split(";") or [""])[0].strip() != "none":
            return None
        con = next((x.strip()[8:] for x in r["basis"].split(";") if x.strip().startswith("concern:")), "")
        return f"{scope[con]}-points" if con in scope else None

    for b, r in pts:
        if r["status"] != "landed":
            add_other("point", (r["cap_ids"].split(";") or [""])[0],
                      f"points/{b}.tsv {r['vp_id']}: {clip(r['conflict'], 160)} -> {clip(r.get('outcome', ''), 120) or 'no outcome'}",
                      part=point_part(r))
    for b, r in rnd.sample(landed, max(1, round(len(landed) * 0.1))) if landed else []:
        add_other("point", (r["cap_ids"].split(";") or [""])[0], f"points/{b}.tsv {r['vp_id']}: landed (a seeded tenth)",
                  part=point_part(r))

    # ---------------------------------------------------------------- the held pass's lines
    lines, listed = held_lines()
    new_cap = {}
    for r in rows(os.path.join(HELD, "new.tsv")):
        m = re.match(r"capability:(CM-[A-Z0-9]{3}-\d{3})", r.get("decision", ""))
        if m:
            new_cap[(r["platform"], r["name"].strip())] = m.group(1)
    taken = set()          # (file, line) of lines another reason took

    # coordinator: its corrections and alignments on held lines, one item per cell
    # by risk: every such line on a cell that doesn't count, or whose counting rests only on such lines (an error there
    # changes a count); a seeded share (--coord-rest) of the others, whose cell counts through lines the coordinator
    # didn't touch, and of the `out` lines, which the omission review also samples (its group 6)
    coord = [L for L in lines if COORD_LINE.search(L.get("reading", "")) and not COORD_SCRIPT.search(L["reading"])
             and not (COORD_RULING_ONLY.search(L["reading"]) and len(COORD_LINE.findall(L["reading"])) == len(COORD_RULING_ONLY.findall(L["reading"])))]
    counting = collections.defaultdict(set)
    for r in ev:
        if set(semi(r.get("supports", ""))) & OWN:
            counting[(r["cap_id"], r["platform"])].add(r["key"])
    touched = collections.defaultdict(set)
    for L in coord:
        touched[(L.get("cap_id", ""), L["_platform"])].add(L["entry_id"])
    risky, rest = [], []
    for L in coord:
        k = (L.get("cap_id", ""), L["_platform"])
        if L["placement"] == "capability" and k in cells and (not counting[k] or counting[k] <= touched[k]):
            risky.append(L)
        else:
            rest.append(L)
    for L in risky + (rnd.sample(rest, math.ceil(len(rest) * a.coord_rest)) if rest else []):
        m = re.search(r".{0,60}the coordinator.{0,90}", L["reading"], re.I)
        add_line(L, "coordinator", f"{line_ref(L)}: '{clip(m.group(0), 150)}'" + ("" if L in risky else " (a seeded share of those an error wouldn't move a count by)"))
        taken.add((L["_file"], L["_line"]))
    notes.append(f"coordinator: {len(coord)} held lines name the coordinator's check, correction or alignment: {len(risky)} where an "
                 f"error could move a count, all read; {len(rest)} others, {a.coord_rest:.0%} of them read")

    # ruling: a seeded sample of each high-weight ruling's lines
    new_rows = {}
    if os.path.exists(GM):
        for l in open(GM, encoding="utf-8").read().split("\n"):
            m = re.match(r"^\| (N\d\d) \|.*\bnew, (CM-[A-Z0-9]{3}-\d{3})", l)
            if m:
                new_rows[m.group(1)] = m.group(2)
    structures = {r["batch"]: r.get("structures", "") for r in rows(os.path.join(HELD, "batches.tsv"))}
    rulings, probs = gm_rulings(GM)
    notes += probs
    a.ruling_table = []
    for r in rulings:
        pat = ruling_pattern(r, new_rows)
        if not pat:
            a.ruling_table.append((r["title"], None, 0, 0)); continue
        if pat == "new-caps":
            mine = [L for L in lines if L.get("cap_id") in made or (L["placement"] == "new" and (L["_platform"], L.get("cap_id", "")[4:].strip()) in new_cap)]
        elif pat.startswith("cap:"):
            mine = [L for L in lines if L.get("cap_id") == pat[4:] or new_cap.get((L["_platform"], L.get("cap_id", "")[4:].strip())) == pat[4:]]
        else:
            rx = re.compile(pat, re.I)
            mine = [L for L in lines if rx.search(L.get("reading", ""))]
        only = ruling_batches(r, structures)
        if only is not None:
            mine = [L for L in mine if L["_batch"] in only]
        n = min(len(mine), max(a.ruling_min, math.ceil(len(mine) * a.ruling_rate)))
        pick, by_p = [], collections.defaultdict(list)
        for L in mine:
            by_p[L["_platform"]].append(L)
        for p in sorted(by_p):
            pick.append(rnd.choice(by_p[p]))
        rest = [L for L in mine if L not in pick]
        pick += rnd.sample(rest, max(0, min(len(rest), n - len(pick))))
        for L in pick:
            add_line(L, "ruling", f"applies '{clip(r['title'], 110)}' ({clip(r['handle'], 60) or 'GM-rulings.md'}): {line_ref(L)}")
            taken.add((L["_file"], L["_line"]))
        a.ruling_table.append((r["title"], pat, len(mine), len(pick)))

    # ---------------------------------------------------------------- the second stage, the qualities pass, the omission review
    om_items, om_cells, om_entries = [], set(), set()
    om_parts = {r["part"]: r.get("platform", "") for r in rows(os.path.join(OMISSION, "parts.tsv"))}
    for path in sorted(glob.glob(os.path.join(OMISSION, "*-items.tsv"))):
        part = os.path.basename(path)[:-len("-items.tsv")]
        plat = om_parts.get(part) or OM_PLATFORM.get((re.match(r"OM-([A-Z]{2})", part) or [None, ""])[1], "")
        for i, r in enumerate(rows(path), 2):
            om_items.append((part, plat, i, r))
            om_entries.add(r.get("item", ""))
            om_entries |= {x.split("@")[0] for x in semi(r.get("basis", ""))}
            if CAP.fullmatch(r.get("cap_id", "")):
                om_cells.add((r["cap_id"], plat))
    held_v = []
    for part, plat, i, r in om_items:
        where = f"omission/{part}-items.tsv line {i}, item {r.get('item', '')}"
        c = r.get("cap_id", "")
        absorbed = any(re.search(r"\babsorbed\b", r.get(k, "") or "") for k in r)
        if r.get("verdict") == "held" and not absorbed:
            held_v.append((part, plat, i, r)); continue
        if not ((r.get("verdict") == "miss" and r.get("miss") in ("support", "out")) or r.get("verdict") == "unclear" or absorbed):
            continue
        what = "absorbed" if absorbed and r.get("verdict") != "unclear" and r.get("miss") not in ("support", "out") else (r.get("miss") or r.get("verdict"))
        d = f"{where}: {what}: {clip(r.get('reading', ''), 160)}"
        if absorbed and CAP.fullmatch(c) and what == "absorbed":
            add_other("omission", c, d)
        elif CAP.fullmatch(c) and (c, plat) in cells:
            add_cell(c, plat, "omission", d)
        else:
            add_other("omission", c if CAP.fullmatch(c) else "", d)
    for part, plat, i, r in rnd.sample(held_v, math.ceil(len(held_v) * 0.1)) if held_v else []:
        d = (f"omission/{part}-items.tsv line {i}, item {r.get('item', '')}: held verdict (a seeded tenth, counted as the "
             f"omission review's own miss rate): does the model hold the item's thing here, on {r.get('basis', '') or 'its basis'}?")
        c = r.get("cap_id", "")
        if CAP.fullmatch(c) and (c, plat) in cells:
            add_cell(c, plat, "omission", d)
        else:
            add_other("omission", c if CAP.fullmatch(c) else "", d)
    n_om_find = 0
    for p in PLATFORMS:
        for path in sorted(glob.glob(os.path.join(HELD, p, "s2", "OM-*.tsv"))):
            for i, r in enumerate(rows(path), 2):
                if r.get("outcome") == "found" and set(semi(r.get("supports", ""))) & OWN and CAP.fullmatch(r.get("cap_id", "")):
                    add_cell(r["cap_id"], p, "omission", f"{rel(path)} line {i}: the omission review's finding gives {r['supports']}: does the passage show it?")
                    n_om_find += 1
    if not om_items and not n_om_find:
        notes.append("omission: no omission/*-items.tsv and no held/<platform>/s2/OM-*.tsv yet: nothing selected")

    # s2-lead: the second stage's leads naming only held cells, by risk
    s2_err = None
    try:
        import s2_held
    except Exception as e:          # the second stage's tool, built by another agent: say why the reason is empty
        s2_err = f"{type(e).__name__}: {e}"
    MAKER = re.compile(r"\bmakers?\b|made by|built by|\bdeveloper\b|\bprovider\b|first-party|own[- ]service|its company|"
                       r"\bby Automattic\b|شركة", re.I)         # 'by' or 'from' the platform's own name: on its own platform only
    QUALITY = re.compile(r"rate limit|uptime|\bSLA\b|\bat most\b|\bmaximum\b|\bup to \d|encrypt|retention|retain|certif|\bPCI\b|"
                         r"SOC ?[12]\b|ISO ?\d|GDPR|subprocessor|data (?:residency|location|cent(?:re|er))|stored in|hosted in", re.I)
    SUPPORT = {"core": r"\bcore\b|built in", "own-service": r"own[- ]service", "extension-point": r"extension-point|left to apps",
               "outside": r"\boutside\b"}
    n_lead_all = n_lead = 0
    if s2_err is None:
        for p in PLATFORMS:
            try:
                leads = s2_held.leads_of(p)
            except Exception as e:
                s2_err = f"leads_of({p}): {type(e).__name__}: {e}"; break
            for L in leads:
                cs = [c for c in L["caps"] if c in caps]
                if not cs or not all((c, p) in cells and cells[(c, p)]["held"] != "none-held" and not s2_held.not_placed(cells[(c, p)]) for c in cs):
                    continue
                n_lead_all += 1
                text = L["text"] + "\n" + (L.get("label") or "")
                own_name = re.compile(rf"\b(?:by|from) {s2_held.PLATFORM_NAME[p]}\b|\bmade by\b|\bbuilt by\b", re.I)
                lacks = [v for v, rx in SUPPORT.items() if re.search(rx, text, re.I) and any(v not in placed.get((c, p), set()) for c in cs)]
                why = (["a maker"] if MAKER.search(re.sub(r"\b(?:by|from) (?:Shopify|Salla|Zid|WooCommerce|BigCommerce)\b", "", text)) or own_name.search(text) else []) + ([f"a support value a cell lacks ({', '.join(lacks)})"] if lacks else []) \
                      + (["a quality"] if QUALITY.search(text) else [])
                if not why:
                    continue
                n_lead += 1
                d = (f"{L['file']} line {L['line']} ({L['batch']}{', set aside by its batch' if L.get('aside') else ''}): "
                     f"names {'; '.join(why)}; on {', '.join(cs)}: {clip(L['text'], 160)}")
                if len(cs) == 1:
                    add_cell(cs[0], p, "s2-lead", d)
                else:                   # one item per lead: its passage is read once, for each cell it names
                    add(item(("lead", L["file"], L["line"]), cs[0], p, ""), "s2-lead", d)
    notes.append(f"s2-lead: {n_lead} of {n_lead_all} leads naming only held cells name a maker, a support value a cell lacks, or a quality"
                 if s2_err is None else f"s2-lead: method/s2_held.py doesn't import or run ({s2_err}): nothing selected; run again once it does")

    # s2-note, ql-note: notes on a placement
    for reason, pattern, heading, line in (
            ("s2-note", os.path.join(HELD, "*", "s2", "*.md"), re.compile(r"S2-R2|held cell|final review", re.I), re.compile(r"S2-R2|final review", re.I)),
            ("ql-note", os.path.join(QUALITIES, "*", "*.md"), re.compile(r"QL-R8|placement|final review", re.I), re.compile(r"QL-R8|final review", re.I))):
        n = 0
        for nf in sorted(glob.glob(pattern)):
            plat = next((p for p in PLATFORMS if f"/{p}/" in nf), "")
            for i, t in note_bullets(nf, heading, line):
                cs = [c for c in dict.fromkeys(CAP.findall(t)) if c in caps]
                d = f"{rel(nf)} line {i}: {clip(t, 200)}"
                n += 1
                if cs and plat:
                    for c in cs:
                        add_cell(c, plat, reason, d) if (c, plat) in cells else add_other(reason, c, d)
                else:
                    add_other(reason, cs[0] if cs else "", d)
        if not glob.glob(pattern):
            notes.append(f"{reason}: no {rel(pattern)} yet: nothing selected")

    # ---------------------------------------------------------------- the samples: every batch, every part
    by_batch = collections.defaultdict(list)
    for L in lines:
        if (L["_file"], L["_line"]) not in taken and L["entry_id"] not in om_entries:
            by_batch[L["_batch"]].append(L)
    for b in sorted(by_batch):
        for L in rnd.sample(by_batch[b], min(len(by_batch[b]), a.batch_lines)):
            add_line(L, "batch", f"a seeded sample of batch {b}: {line_ref(L)}")
    empty = sorted(b for b in listed if b not in by_batch and not any(L["_batch"] == b for L in lines))
    if empty:
        notes.append(f"batch: {len(empty)} listed batches have no placements file: {', '.join(empty[:8])}")
    psample = {x.split("=")[0]: float(x.split("=")[1]) for x in a.platform_sample}
    by_part = {}
    for k, r in cells.items():
        if ("cell",) + k not in found and k not in om_cells:
            by_part.setdefault(r.get("part", ""), []).append(k)
    for part, ks in sorted(by_part.items()):
        pick = rnd.sample(sorted(ks), min(len(ks), max(2, math.ceil(len(ks) * a.sample))))
        for p, f in sorted(psample.items()):          # a platform's raised sample, within the part
            kp = sorted(k for k in ks if k[1] == p and k not in pick)
            want = math.ceil(len([k for k in ks if k[1] == p]) * f) - len([k for k in pick if k[1] == p])
            pick += rnd.sample(kp, max(0, min(len(kp), want)))
        for k in pick:
            add_cell(k[0], k[1], "sample", f"a seeded sample of {part}'s other cells" + (f" (raised for {k[1]})" if k[1] in psample else ""))

    # ---------------------------------------------------------------- thinning, where the coordinator chooses it
    thin = {x.split("=")[0]: float(x.split("=")[1]) for x in a.thin}
    if thin:
        for r, f in sorted(thin.items()):
            alone = sorted((k for k, it in found.items() if it["reasons"] == [r]), key=str)
            drop = set(map(str, alone)) - set(map(str, rnd.sample(alone, math.ceil(len(alone) * f)))) if alone else set()
            for k in [k for k in found if str(k) in drop]:
                del found[k]
            notes.append(f"thinned: {r}: {len(alone) - len(drop)} of the {len(alone)} items it alone selects kept, a seeded {f:.0%}")

    # ---------------------------------------------------------------- write
    out = []
    for k, it in found.items():
        part = it["part"] if not CAP.fullmatch(it["cap"] or "") else None
        out.append([",".join(it["reasons"]), it["cap"], it["plat"], " | ".join(it["details"]), share_of(it["cap"], part, areas)])
    out.sort(key=lambda x: (x[4], x[1] or "~", x[2], x[0], x[3]))
    counters, lines_out = {}, []
    for i, x in enumerate(out, 1):
        n = counters.get(x[4], 0); counters[x[4]] = n + 1
        lines_out.append([f"R-{i:04d}"] + [" ".join(str(v).split()) for v in x] + [str(n // a.batch_size + 1)])
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\t".join(HEAD_SEL) + "\n")
        for l in lines_out:
            f.write("\t".join(l) + "\n")
    summary(a, lines_out, cells, notes)


def summary(a, lines_out, cells, notes):
    n_cells = sum(1 for l in lines_out if l[3])
    print(f"{os.path.relpath(a.out)}: {len(lines_out)} items ({n_cells} on one platform, {len(lines_out) - n_cells} on a capability or no capability) from {len(cells)} cells")
    carry, alone = collections.Counter(), collections.Counter()
    for l in lines_out:
        rs = l[1].split(",")
        carry.update(rs)
        if len(rs) == 1:
            alone[rs[0]] += 1
    lo, hi = a.rate_low / 1e6, a.rate_high / 1e6
    print(f"  by reason: items carrying it; items it alone selects; the cost of those alone at {a.rate_low:,} to {a.rate_high:,} tokens an item (an assumption)")
    for r in sorted(carry, key=lambda r: -carry[r]):
        print(f"    {r:14} {carry[r]:5} {alone[r]:5}   {alone[r] * lo:6.1f} to {alone[r] * hi:6.1f} million")
    batches = 0
    for s in sorted({l[5] for l in lines_out}):
        sel = [l for l in lines_out if l[5] == s]
        nb = max(int(l[6]) for l in sel)
        batches += nb
        print(f"  share {s}: {len(sel)} items in {nb} batches")
    print(f"  in all: {len(lines_out)} items in {batches} batches: {len(lines_out) * lo:.0f} to {len(lines_out) * hi:.0f} million tokens "
          f"for the reviewers' agents, an assumption")
    if getattr(a, "ruling_table", None) is not None:
        print("  rulings of high weight from the held pass on (reports/GM-rulings.md): lines naming it, lines sampled")
        for t, pat, n, k in a.ruling_table:
            print(f"    {n:5} {k:3}  {clip(t, 100)}{'' if pat else '  [no handle a held line names: not a placement rule of the held lines, or its lines are found another way]'}")
    for n in notes:
        print(f"  note: {n}")


def coverage_problems(path, sel, keys):
    raw = open(path, encoding="utf-8").read().split("\n")
    problems, seen = [], {}
    if raw[0].split("\t") != HEAD_COV:
        problems.append(f"header must be: {' '.join(HEAD_COV)}")
    for i, l in enumerate(raw[1:], 2):
        if not l.strip():
            continue
        f = l.split("\t")
        if len(f) != len(HEAD_COV) or '"' in l:
            problems.append(f"line {i}: {len(HEAD_COV)} tab-separated fields, no quoting"); continue
        r = dict(zip(HEAD_COV, f))
        if r["item"] in seen:
            problems.append(f"line {i}: {r['item']} again")
        seen[r["item"]] = r
        if r["verdict"] not in ("holds", "wrong", "unclear"):
            problems.append(f"line {i}: verdict is holds, wrong or unclear")
        if r["verdict"] == "wrong":
            if r["severity"] not in ("kind", "placement", "structure", "reading"):
                problems.append(f"line {i}: a wrong item's severity is kind, placement, structure or reading")
            if not re.match(r"^[A-Z]-[a-z-]+/[a-z-]+\.(tsv|md)|^scope\.tsv|^points/P-\d+\.tsv|^held/(?:new\.tsv|[a-z]+/placements-[A-Z0-9-]+\.tsv|[a-z]+/s2/[A-Z0-9-]+\.tsv)"
                            r"|^omission/[A-Z0-9-]+-items\.tsv|^qualities/[a-z]+/[A-Z0-9-]+\.tsv", r["correction"]):
                problems.append(f"line {i}: a correction names <part>/<file> (or held/<platform>/placements-<batch>.tsv, held/new.tsv, "
                                f"held/<platform>/s2/<part>.tsv, omission/<part>-items.tsv, qualities/<platform>/<part>.tsv), the row and the new value")
        elif r["severity"] or r["correction"]:
            problems.append(f"line {i}: severity and correction are for wrong items")
        if r["verdict"] == "unclear" and not r["what_would_settle_it"].strip():
            problems.append(f"line {i}: an unclear item says what would settle it")
        if not r["basis"].strip():
            problems.append(f"line {i}: basis names the keys read")
        for b in [x.strip() for x in r["basis"].split(";") if x.strip()]:
            b0 = b.split("@")[0]
            if re.match(r"^[A-Z]{2}-(C-\d{3}/[a-z]+/[A-Z]{2}-S-\d{4}|I-\d{4}|E-[0-9a-f]{8,40})$", b0) and b0 not in keys:
                problems.append(f"line {i}: {b} is not a statement key, inventory id or held entry id")
    want = {r["item"] for r in sel}
    for r in sel:
        if r["item"] not in seen:
            problems.append(f"{r['item']} has no line")
    for x in seen:
        if x not in want:
            problems.append(f"{x} is not an item of this batch")
    return problems, seen


def all_keys():
    keys = set()
    for p in PLATFORMS:
        keys |= {key(s) for s in citable(p)}
    return keys


def check(a):
    sel = [r for r in rows(a.selection) if r["share"] == a.share and r["batch"] == a.batch]
    if not sel:
        sys.exit(f"no items for share {a.share}, batch {a.batch} in {os.path.relpath(a.selection)}")
    path = os.path.join(a.review_dir, f"coverage-{a.share}-{a.batch}.tsv")
    if not os.path.exists(path):
        sys.exit(f"no {path}")
    problems, seen = coverage_problems(path, sel, all_keys())
    for p in problems:
        print("PROBLEM", p)
    print(f"{len([x for x in seen if x in {r['item'] for r in sel}])} of {len(sel)} items; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def wilson(k, n, z=1.96):
    if not n:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - m) / d), min(1.0, (c + m) / d))


def rates(a):
    """The verdicts so far, by reason, from every coverage file; and the omission review's own miss rate: the share of
    its `held` verdicts in the seeded tenth that the final review finds `wrong` (the coordinator's decision 11)."""
    sel = {r["item"]: r for r in rows(a.selection)}
    by, om = collections.defaultdict(collections.Counter), collections.Counter()
    for path in sorted(glob.glob(os.path.join(a.review_dir, "coverage-*.tsv"))):
        for r in rows(path):
            s = sel.get(r["item"])
            if not s:
                continue
            for reason in s["reasons"].split(","):
                by[reason][r["verdict"]] += 1
            if "held verdict (a seeded tenth" in s["detail"]:
                om[r["verdict"]] += 1
    for reason in sorted(by):
        c = by[reason]
        print(f"{reason:14} {sum(c.values()):5} read: holds {c['holds']}, wrong {c['wrong']}, unclear {c['unclear']}")
    n = sum(om.values())
    lo, hi = wilson(om["wrong"], n)
    print(f"the omission review's held verdicts, a seeded tenth: {n} read, {om['wrong']} wrong, {om['unclear']} unclear: "
          f"its own miss rate {om['wrong'] / n if n else 0:.1%} (95% interval {lo:.1%} to {hi:.1%}, Wilson)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("cmd", nargs="?", default="select", choices=["select", "check", "rates"])
    ap.add_argument("--out", default=OUT, help="where select writes the selection (default studies/class-model/review/selection.tsv)")
    ap.add_argument("--selection", default=OUT, help="the selection check and rates read")
    ap.add_argument("--review-dir", default=REVIEW, help="the folder of the reviewers' coverage files")
    ap.add_argument("--since", default="9d204b46", help="the commit of the merge of 30 October, for changed and new-cap")
    ap.add_argument("--since-dir", help="for tests: a folder holding the merged kinds.tsv, capabilities.tsv and flags.tsv of --since")
    ap.add_argument("--sample", type=float, default=0.05)
    ap.add_argument("--platform-sample", action="append", default=[], metavar="PLATFORM=FRACTION",
                    help="a higher sample of a platform's other cells (the omission review's decision 13)")
    ap.add_argument("--one-cap-terms", type=int, default=5, help="a `one capability?` pair sharing this many terms or more is read whole")
    ap.add_argument("--ruling-min", type=int, default=4)
    ap.add_argument("--ruling-rate", type=float, default=0.02)
    ap.add_argument("--batch-lines", type=int, default=1)
    ap.add_argument("--coord-rest", type=float, default=0.34, help="the share read of the coordinator's held lines an error wouldn't move a count by")
    ap.add_argument("--none-held-all", action="store_true", help="read the none-held cells the second stage read too")
    ap.add_argument("--thin", action="append", default=[], metavar="REASON=FRACTION",
                    help="keep a seeded fraction of the items this reason alone selects (the lean selection; R-extent-design.md)")
    ap.add_argument("--rate-low", type=int, default=120000, help="tokens an item, for the estimate (an assumption)")
    ap.add_argument("--rate-high", type=int, default=250000)
    ap.add_argument("--seed", type=int, default=20261030)
    ap.add_argument("--batch-size", type=int, default=30)
    ap.add_argument("--share"); ap.add_argument("--batch")
    a = ap.parse_args()
    {"select": select, "check": check, "rates": rates}[a.cmd](a)


if __name__ == "__main__":
    main()
