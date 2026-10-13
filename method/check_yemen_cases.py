# Checks the output of PLAN.md Stage 1, Yemen's axes and cases, against studies/yemen-cases/brief.md:
# files and columns, ids, that every state is cited, that every case gives every axis one of that axis's states,
# that today's case matches each axis's "today", that every unknown is listed with what was read, that only
# Yemen evidence is cited at a pinned commit, and that every quote is found verbatim in the file it cites.
# Pass 2's judgments (groups.tsv, places.tsv, states.tsv) are checked for completeness, and axes.tsv,
# constants.tsv and cases.tsv must be exactly what method/build_yemen_cases.py gives from them.
#
# Usage: python3 -I method/check_yemen_cases.py STUDY_DIR OUT [--pass1 PART | --groups | --states FILE]
#   --pass1 PART   one part of pass 1: pass1/conditions-<PART>.tsv and pass1/citations-<PART>.tsv
#   --groups       step 2a: groups.tsv and places.tsv
#   --states FILE [FIRST LAST]  step 2b: one agent's states file (e.g. pass2/states-1.tsv), for the groups it
#                  covers, or for every group from FIRST to LAST (e.g. YG-001 YG-080)
import csv, glob, os, re, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources, variants
import build_yemen_cases as B

study, OUT = sys.argv[1].rstrip("/"), sys.argv[2]
os.makedirs(OUT, exist_ok=True)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = Sources({"sharrwah-knowledge-map": SKM})
HEADERS = {
    "conditions.tsv": ["condition_id", "condition", "state", "place", "held_at", "date_basis", "cite_ids", "note"],
    "groups.tsv": ["group_id", "condition", "what_varies", "condition_ids", "note"],
    "places.tsv": ["place", "grouped", "kind", "why", "basis", "note"],
    "states.tsv": ["condition_id", "group_id", "label", "place", "holds", "now", "note"],
    "axes.tsv": B.HEADS["axes.tsv"],
    "constants.tsv": B.HEADS["constants.tsv"],
    "cases.tsv": B.HEADS["cases.tsv"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "fetched_from", "url"],
    "unknowns.tsv": ["about", "what_would_show_it", "who_can", "route", "read", "why_not_held"],
}
IDS = {"conditions.tsv": ("condition_id", r"^YQ-[A-F]\d{3,}$"), "groups.tsv": ("group_id", r"^YG-\d{3,}$"),
       "axes.tsv": ("axis_id", r"^YA-\d{2,}$"), "constants.tsv": ("constant_id", r"^YK-\d{2,}$"),
       "cases.tsv": ("case_id", r"^YC-\d{2,}$"), "citations.tsv": ("cite_id", r"^YE-[A-F]\d{3,}$")}
BASES = {"today", "in force", "occurred", "provided for"}
FETCHED = {"inside Yemen", "outside Yemen", "attestation"}
WHO = {"agent", "founder", "reader"}
HOLDS = {"held", "provided for", "ended", "proposed"}
KINDS = {"area", "authority", "service"}
WHYS = {"variant", "source", "rule"}
SOURCE = re.compile(r"^sharrwah-knowledge-map@[0-9a-f]{7,40}:evidence/yemen/(runs|blocked-evidence-founder|derived|attestations)/")
LABEL_BAD = re.compile(r"[;|\[\]]| \+ | @ ")
MAX_AXES = B.MAX_AXES
issues = []

def err(f, i, x, level="error"):
    issues.append((level, f, i, x))

def read(name, key=None):
    key = key or os.path.basename(name)
    p = os.path.join(study, name)
    if not os.path.exists(p):
        err(name, "", "file missing")
        return []
    with open(p, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows:
        err(name, "", "empty file")
        return []
    head = rows[0]
    if head != HEADERS[key]:
        err(name, "", f"header is {head}, expected {HEADERS[key]}")
    out = []
    for n, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            continue
        if len(row) != len(head):
            err(name, f"line {n}", f"{len(row)} fields, header has {len(head)}")
        out.append({h: (row[k].strip() if k < len(row) else "") for k, h in enumerate(head)})
    return out

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

def write_issues(name):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write("level\tfile\tid\tissue\n")
        for row in issues:
            f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in row) + "\n")

def check_quotes(cits, fname, used):
    quotes = []
    for c in cits:
        cid, src = c["cite_id"], c["source"]
        if not SOURCE.match(src):
            err(fname, cid, f"source '{src[:90]}' is not Yemen evidence at a pinned commit")
        if not c["quote"]:
            err(fname, cid, "quote is empty")
        if "..." in c["quote"] or "…" in c["quote"]:
            err(fname, cid, "quote contains an ellipsis")
        if len(c["quote"]) > 300:
            err(fname, cid, f"quote is {len(c['quote'])} characters; the brief allows 300")
        if c["fetched_from"] not in FETCHED:
            err(fname, cid, f"fetched_from '{c['fetched_from']}' is not one of {sorted(FETCHED)}")
        if used is not None and cid not in used:
            err(fname, cid, "not used", "warning")
        res, why, share = SRC.check_quote(c["quote"], src, c["locator"]) if c["quote"] and src else ("unresolved", "no quote or source", "")
        if not res.startswith("found"):
            err(fname, cid, f"quote {res}{'; ' + why if why else ''}{'; best 6-word share ' + share if share else ''}")
        quotes.append((cid, res, why, share, src, c["quote"][:200]))
    return quotes

if "--pass1" in sys.argv:
    # Pass 1 of one part: its conditions and citations, with the part's ids, and every quote verbatim.
    part = sys.argv[sys.argv.index("--pass1") + 1]
    conds = read(f"pass1/conditions-{part}.tsv", "conditions.tsv") or []
    cits = read(f"pass1/citations-{part}.tsv", "citations.tsv") or []
    cid_set = {c["cite_id"] for c in cits}
    for name, recs, key, pat in (("conditions", conds, "condition_id", rf"^YQ-{part}\d{{3,}}$"),
                                 ("citations", cits, "cite_id", rf"^YE-{part}\d{{3,}}$")):
        for k, n in Counter(r[key] for r in recs).items():
            if n > 1:
                err(name, k, f"id used {n} times")
        for r in recs:
            if not re.match(pat, r[key]):
                err(name, r[key], f"id doesn't match {pat}")
    used = set()
    for c in conds:
        for col in ("condition", "state", "held_at", "date_basis"):
            if not c[col]:
                err("conditions", c["condition_id"], f"{col} is empty")
        if not ids(c["cite_ids"]):
            err("conditions", c["condition_id"], "no citation")
        for x in ids(c["cite_ids"]):
            used.add(x)
            if x not in cid_set:
                err("conditions", c["condition_id"], f"cite_id {x} not in citations")
    quotes = check_quotes(cits, "citations", used)
    write_issues(f"pass1-{part}-issues.tsv")
    print(f"part {part}: conditions {len(conds)}, citations {len(cits)} | issues: {dict(Counter(i[0] for i in issues))} | "
          f"quotes: {dict(Counter(q[1].split(' (')[0] for q in quotes))}")
    sys.exit(0)

# Pass 2. Its judgments first: groups and places (step 2a), then states (step 2b).
conds = read("conditions.tsv")
cits = read("citations.tsv")
cond = {c["condition_id"]: c for c in conds}
cit_ids = {c["cite_id"] for c in cits}
cit_source = {c["cite_id"]: c["source"].split(":", 1)[-1] for c in cits}

def check_groups():
    groups, places = read("groups.tsv"), read("places.tsv")
    for extra in sorted(glob.glob(os.path.join(study, "pass2", "places-*.tsv"))):
        added = read(os.path.relpath(extra, study), "places.tsv")
        for p in added:                      # step 2b may add an authority's area or a party's service, alone
            if p["grouped"] != p["place"] or p["kind"] not in ("authority", "service"):
                err(os.path.relpath(extra, study), p["place"], "step 2b adds only an authority's area or a party's service, grouped with itself")
        listed = {p["place"] for p in places}
        places += [p for p in added if p["place"] not in listed]   # once joined, places.tsv holds them
    for k, n in Counter(g["group_id"] for g in groups).items():
        if n > 1:
            err("groups.tsv", k, f"id used {n} times")
    member = {}
    for g in groups:
        if not re.match(IDS["groups.tsv"][1], g["group_id"]):
            err("groups.tsv", g["group_id"], "id doesn't match YG-001…")
        if not g["condition"]:
            err("groups.tsv", g["group_id"], "condition is empty")
        if not ids(g["condition_ids"]):
            err("groups.tsv", g["group_id"], "condition_ids is empty")
        for x in ids(g["condition_ids"]):
            if x not in cond:
                err("groups.tsv", g["group_id"], f"{x} is not a pass 1 row")
            elif x in member:
                err("groups.tsv", g["group_id"], f"{x} is also in {member[x]}; each row is in exactly one group")
            member[x] = g["group_id"]
    for x in cond:
        if x not in member:
            err("groups.tsv", x, "a pass 1 row in no group")
    names = Counter(p["place"] for p in places)
    grouped = {p["place"]: p["grouped"] for p in places}
    kind = {p["place"]: p["kind"] for p in places}
    for k, n in names.items():
        if n > 1:
            err("places.tsv", k, f"listed {n} times")
    for p in places:
        if not p["grouped"]:
            err("places.tsv", p["place"], "grouped is empty")
        if p["grouped"] == B.ACROSS or (p["place"] == B.ACROSS and p["grouped"] != B.NOT_STATED):
            err("places.tsv", p["place"], f"'{B.ACROSS}' is set per state in states.tsv; places.tsv may only take it as '{B.NOT_STATED}'")
        if p["kind"] not in KINDS:
            err("places.tsv", p["place"], f"kind '{p['kind']}' is not one of {sorted(KINDS)}")
        if p["grouped"] not in (p["place"], B.NOT_STATED) and kind.get(p["grouped"]) not in (None, p["kind"]):
            err("places.tsv", p["place"], f"a {p['kind']} grouped with a {kind.get(p['grouped'])}: a grouping joins places of one kind")
        if p["grouped"] == p["place"]:
            if p["why"]:
                err("places.tsv", p["place"], "why is for a place grouped with another; leave it empty")
            continue
        if p["grouped"] == B.NOT_STATED:
            if p["why"] != "rule":
                err("places.tsv", p["place"], "a name taken as 'place not stated' has why 'rule' (Yemen or the Republic, no authority)")
        elif grouped.get(p["grouped"]) != p["grouped"]:
            err("places.tsv", p["place"], f"grouped with '{p['grouped'][:50]}', which isn't listed as a place grouped with itself")
        if p["why"] not in WHYS:
            err("places.tsv", p["place"], f"why '{p['why']}' is not one of {sorted(WHYS)}")
        if p["why"] == "source":
            if not ids(p["basis"]):
                err("places.tsv", p["place"], "grouped on a source, but basis cites none")
            if len({cit_source[x] for x in ids(p["basis"]) if x in cit_source}) > 1:
                err("places.tsv", p["place"], "basis cites more than one source; a grouping rests on one source using both names")
        for x in ids(p["basis"]):
            if x not in cit_ids:
                err("places.tsv", p["place"], f"basis {x} is not a citation")
    for c in conds:
        if c["place"] not in grouped and c["place"] not in (B.ACROSS, B.NOT_STATED):
            err("places.tsv", c["place"][:60], f"a place pass 1 gives ({c['condition_id']}) that places.tsv doesn't list")
    global place_kind, place_of
    place_kind = dict(kind)
    place_of = {c["condition_id"]: (B.NOT_STATED if c["place"] == B.NOT_STATED else
                                    None if c["place"] == B.ACROSS else grouped.get(c["place"])) for c in conds}
    return groups, member, {v for v in grouped.values()} | {B.NOT_STATED}

place_kind, place_of = {}, {}
cits_by_id = {c["cite_id"]: c for c in cits}

def tie(a, b):
    """Two held_at values tie: both undated, or neither later at the coarser precision."""
    wa, wb = B.when(a), B.when(b)
    if not wa or not wb:
        return not wa and not wb
    return not B.later(wa, wb) and not B.later(wb, wa)

def check_states(states, fname, member, place_set, whole=True, span=None):
    seen = Counter(s["condition_id"] for s in states)
    for k, n in seen.items():
        if n > 1:
            err(fname, k, f"row given {n} times")
    for s in states:
        cid = s["condition_id"]
        if cid not in cond:
            err(fname, cid, "not a pass 1 row")
            continue
        if member.get(cid) != s["group_id"]:
            err(fname, cid, f"group_id {s['group_id']}, but groups.tsv puts it in {member.get(cid)}")
        if not s["label"]:
            err(fname, cid, "label is empty")
        elif LABEL_BAD.search(s["label"]):
            err(fname, cid, "label contains ';', '|', '[', ']', ' + ' or ' @ ', which the axes and cases files use as separators")
        if s["place"] == B.ACROSS:
            said = re.findall(r'"([^"]+)"|\u201c([^\u201d]+)\u201d|\u00ab([^\u00bb]+)\u00bb', s["note"])
            quotes = [variants(cits_by_id[x]["quote"])[2][1] for x in ids(cond[cid]["cite_ids"]) if x in cits_by_id]
            if not any(variants(w)[2][1] in q for m in said for w in m if w for q in quotes):
                err(fname, cid, f"'{B.ACROSS}' quotes in note, in double quotes, the words of its citations that say the state holds in all of Yemen")
        elif s["place"] not in place_set:
            err(fname, cid, f"place '{s['place'][:50]}' is neither a grouped place in places.tsv nor '{B.ACROSS}'")
        elif place_of.get(cid) is None and s["place"] != B.NOT_STATED:
            err(fname, cid, f"pass 1 placed this row '{B.ACROSS}': it is '{B.ACROSS}' or '{B.NOT_STATED}'")
        elif place_of.get(cid) is not None and s["place"] != place_of.get(cid) and place_kind.get(s["place"]) not in ("authority", "service"):
            err(fname, cid, f"place '{s['place'][:50]}' is neither the row's place as places.tsv groups it "
                            f"('{(place_of.get(cid) or '')[:40]}') nor an authority's area or a party's service")
        if s["holds"] not in HOLDS:
            err(fname, cid, f"holds '{s['holds']}' is not one of {sorted(HOLDS)}")
        if s["now"] not in ("", "yes"):
            err(fname, cid, "now is 'yes' or empty")
    covered = {s["group_id"] for s in states}
    for x, g in member.items():
        if (whole or g in covered or (span and span[0] <= g <= span[1])) and x not in seen:
            err(fname, x, f"a row of {g} with no state")
    by_group = {}
    for s in states:
        by_group.setdefault(s["group_id"], set()).add(s["label"])
    for g, labels in by_group.items():
        folded = Counter(l.casefold() for l in labels)
        for l in labels:
            if folded[l.casefold()] > 1:
                err(fname, g, f"labels '{l[:40]}' and another differ only in case: one state takes one label, word for word")
    # `now` marks the current one of two states a source gives for one place at one date: it needs its pair.
    src_of = {c["cite_id"]: c["source"].split(":", 1)[-1] for c in cits}
    srcs = {s["condition_id"]: {src_of.get(x) for x in ids(cond[s["condition_id"]]["cite_ids"])} - {None}
            for s in states if s["condition_id"] in cond}
    for s in states:
        if s["now"] == "yes" and s["condition_id"] in cond:
            c = cond[s["condition_id"]]
            pair = [o for o in states if o is not s and o["group_id"] == s["group_id"] and o["place"] == s["place"]
                    and o["label"] != s["label"] and o["condition_id"] in cond
                    and tie(cond[o["condition_id"]]["held_at"], c["held_at"]) and srcs[o["condition_id"]] & srcs[s["condition_id"]]]
            if not pair:
                err(fname, s["condition_id"], "now is 'yes', but the same source gives no other state for this place and held_at")

if "--groups" in sys.argv:
    groups, member, place_set = check_groups()
    write_issues("pass2-groups-issues.tsv")
    print(f"groups {len(groups)} over {len(member)} rows, grouped places {len(place_set)} | "
          f"issues: {dict(Counter(i[0] for i in issues))}")
    sys.exit(0)

if "--states" in sys.argv:
    i = sys.argv.index("--states")
    fname = sys.argv[i + 1]
    span = tuple(sys.argv[i + 2:i + 4]) if len(sys.argv) >= i + 4 else None
    groups, member, place_set = check_groups()
    issues.clear()                                   # step 2a's own issues are reported by --groups
    states = read(fname, "states.tsv")
    check_states(states, fname, member, place_set, whole=False, span=span)
    write_issues(f"pass2-{os.path.basename(fname)}-issues.tsv")
    print(f"{fname}: states {len(states)} over {len({s['group_id'] for s in states})} groups | "
          f"issues: {dict(Counter(i[0] for i in issues))}")
    sys.exit(0)

groups, member, place_set = check_groups()
states = read("states.tsv")
check_states(states, "states.tsv", member, place_set)
data = {n: read(n) for n in ("axes.tsv", "constants.tsv", "cases.tsv", "unknowns.tsv")}
axes, consts, cases, unk = (data[n] for n in ("axes.tsv", "constants.tsv", "cases.tsv", "unknowns.tsv"))
if not os.path.exists(os.path.join(study, "notes.md")):
    err("notes.md", "", "file missing")
if not [i for i in issues if i[0] == "error"]:
    built, summary = B.build(study)
    for name, rows in built.items():
        with open(os.path.join(study, name), encoding="utf-8") as f:
            if f.read() != B.render(rows, B.HEADS[name]):
                err(name, "", "differs from what method/build_yemen_cases.py gives: run it, and don't edit the file by hand")
for name in ("conditions.tsv", "axes.tsv", "constants.tsv", "cases.tsv", "citations.tsv"):
    key, pat = IDS[name]
    rows = {"conditions.tsv": conds, "citations.tsv": cits}.get(name) or data[name]
    for k, n in Counter(r[key] for r in rows).items():
        if n > 1:
            err(name, k, f"id used {n} times")
    for r in rows:
        if not re.match(pat, r[key]):
            err(name, r[key], f"id doesn't match {pat}")
used = set()

def cites(f, i, s, need=True):
    cs = ids(s)
    if need and not cs:
        err(f, i, "no citation")
    for c in cs:
        used.add(c)
        if c not in cit_ids:
            err(f, i, f"cite_id {c} not in citations")
    return cs

reviewed = os.path.exists(os.path.join(study, "review-axes.md"))
stopped = len(axes) > MAX_AXES and not reviewed
if len(axes) > MAX_AXES:
    err("axes.tsv", "", f"{len(axes)} axes: the brief stops for review past {MAX_AXES}"
        + ("; reviewed in review-axes.md" if reviewed else ""), "review")
    if stopped and cases:
        err("cases.tsv", "", f"cases were built past the {MAX_AXES}-axis stop for review")
for c in conds:
    if not c["condition"] or not c["state"]:
        err("conditions.tsv", c["condition_id"], "condition or state is empty")
    if not c["held_at"] or not c["date_basis"]:
        err("conditions.tsv", c["condition_id"], "held_at or date_basis is empty")
    cites("conditions.tsv", c["condition_id"], c["cite_ids"])
placed = Counter(x for r in axes + consts for x in ids(r["condition_ids"]))
for x, n in placed.items():
    if x not in cond:
        err("axes.tsv", x, "a condition_id that conditions.tsv doesn't hold")
    elif n > 1:
        err("axes.tsv", x, f"condition on {n} axes or constants; each sits on exactly one")
for x in set(cond) - set(placed):
    err("conditions.tsv", x, "on no axis and no constant")
unknown_about = {u["about"] for u in unk}
labels, today = {}, {}

def part_ok(aid, x):
    x = x.strip()
    return x in labels.get(aid, []) or x in ("unknown", "disputed") or x.startswith(("disputed @ ", "unknown @ "))
for a in axes:
    aid = a["axis_id"]
    parts = [p.strip() for p in a["states"].split(" | ") if p.strip()]
    labels[aid] = []
    for p in parts:
        m = re.match(r"^(.*\S)\s*\[([^\]]*)\]$", p)
        if not m:
            err("axes.tsv", aid, f"state '{p[:50]}' has no [cite_ids]")
            continue
        labels[aid].append(m.group(1))
        cites("axes.tsv", f"{aid} state '{m.group(1)[:40]}'", m.group(2))
    if len(labels[aid]) < 2:
        err("axes.tsv", aid, "an axis needs at least two states; a one-state condition goes in constants.tsv")
    for k, n in Counter(labels[aid]).items():
        if n > 1:
            err("axes.tsv", aid, f"state '{k[:40]}' listed {n} times")
    if not a["what_varies"]:
        err("axes.tsv", aid, "what_varies is empty: groups.tsv says what differs between the states")
    t = today[aid] = a["today"]
    if not all(part_ok(aid, x) for x in t.split(" + ")):
        err("axes.tsv", aid, f"today '{t[:50]}' is not its state labels joined by ' + ', with 'disputed' or 'unknown' parts")
    if any(x.strip().startswith("unknown") for x in t.split(" + ")) and aid not in unknown_about:
        err("axes.tsv", aid, "today has an unknown part, but unknowns.tsv has no row about it")
    if any(not x.strip().startswith("unknown") for x in t.split(" + ")):
        cites("axes.tsv", f"{aid} today", a["today_cite_ids"])
    if not ids(a["condition_ids"]):
        err("axes.tsv", aid, "condition_ids is empty")
for k in consts:
    cites("constants.tsv", k["constant_id"], k["cite_ids"])
    if not ids(k["condition_ids"]):
        err("constants.tsv", k["constant_id"], "condition_ids is empty")
    if not k["state"]:
        err("constants.tsv", k["constant_id"], "state is empty")
case_ids = {c["case_id"] for c in cases}
if not stopped and "YC-00" not in case_ids:
    err("cases.tsv", "YC-00", "today's case is missing")
for c in cases:
    cid = c["case_id"]
    if c["basis"] not in BASES:
        err("cases.tsv", cid, f"basis '{c['basis']}' is not one of {sorted(BASES)}")
    if (cid == "YC-00") != (c["basis"] == "today"):
        err("cases.tsv", cid, "basis 'today' belongs to YC-00 only")
    given = {}
    for part in [p.strip() for p in c["axis_states"].split(";") if p.strip()]:
        ax, _, val = part.partition("=")
        ax, val = ax.strip(), val.strip()
        if ax in given:
            err("cases.tsv", cid, f"{ax} given twice")
        given[ax] = val
    for ax in labels:
        v = given.get(ax)
        if v is None:
            err("cases.tsv", cid, f"{ax} has no state")
        elif v == "unknown":
            if cid not in unknown_about and ax not in unknown_about:
                err("cases.tsv", cid, f"{ax} is unknown, but unknowns.tsv has no row about it")
        elif not all(part_ok(ax, x) for x in v.split(" + ")):
            err("cases.tsv", cid, f"{ax}='{v[:50]}' is not that axis's state labels")
    for ax in given:
        if ax not in labels:
            err("cases.tsv", cid, f"{ax} is not an axis")
    if cid == "YC-00":
        for ax in labels:
            if given.get(ax) not in (today[ax], None):
                err("cases.tsv", cid, f"{ax} differs from that axis's today")
    else:
        changed = {ax for ax in labels if given.get(ax) not in (None, today[ax])}
        named = {p.split("=")[0].strip() for p in c["name"].split(";") if "=" in p}
        if not changed:
            err("cases.tsv", cid, "the same as today's case")
        elif named != changed:
            err("cases.tsv", cid, f"name lists {sorted(named)}, but the states that differ from today are {sorted(changed)}")
    cites("cases.tsv", cid, c["cite_ids"])
dupes = Counter(c["axis_states"] for c in cases)
for st, n in dupes.items():
    if n > 1:
        err("cases.tsv", "", f"{n} cases have the same states: {st[:80]}")
for u in unk:
    if u["about"] not in labels and u["about"] not in case_ids:
        err("unknowns.tsv", u["about"], "not an axis_id or case_id")
    if u["who_can"] not in WHO:
        err("unknowns.tsv", u["about"], f"who_can '{u['who_can']}' is not one of {sorted(WHO)}")
    if not u["read"]:
        err("unknowns.tsv", u["about"], "read is empty: list each path read looking for it")
for c in cits:
    for col in ("locator", "source_date", "date_basis"):
        if not c[col]:
            err("citations.tsv", c["cite_id"], f"{col} is empty")
quotes = check_quotes(cits, "citations.tsv", used)
write_issues("yemen-cases-issues.tsv")
with open(os.path.join(OUT, "yemen-cases-quotes.tsv"), "w", encoding="utf-8") as f:
    f.write("cite_id\tresult\twhy\tshare_of_6-word_runs_found\tsource\tquote_start\n")
    for q in quotes:
        f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in q) + "\n")
print(f"conditions {len(conds)}, groups {len(groups)}, axes {len(axes)}, constants {len(consts)}, cases {len(cases)}, "
      f"citations {len(cits)}, unknowns {len(unk)} | issues: {dict(Counter(i[0] for i in issues))} | "
      f"quotes: {dict(Counter(q[1].split(' (')[0] for q in quotes))}")
