# Checks the output of PLAN.md Stage 1, Yemen's axes and cases, against studies/yemen-cases/brief.md:
# files and columns, ids, that every state is cited, that every case gives every axis one of that axis's states,
# that today's case matches each axis's "today", that every unknown is listed with what was read, that only
# Yemen evidence is cited at a pinned commit, and that every quote is found verbatim in the file it cites.
#
# Usage: python3 -I method/check_yemen_cases.py STUDY_DIR OUT
import csv, os, re, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources

study, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = Sources({"sharrwah-knowledge-map": SKM})
HEADERS = {
    "conditions.tsv": ["condition_id", "condition", "state", "place", "held_at", "date_basis", "cite_ids", "note"],
    "axes.tsv": ["axis_id", "axis", "what_varies", "condition_ids", "states", "today", "today_cite_ids", "note"],
    "constants.tsv": ["constant_id", "condition", "condition_ids", "cite_ids", "note"],
    "cases.tsv": ["case_id", "name", "axis_states", "basis", "cite_ids", "note"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "fetched_from", "url"],
    "unknowns.tsv": ["about", "what_would_show_it", "who_can", "route", "read", "why_not_held"],
}
IDS = {"conditions.tsv": ("condition_id", r"^YQ-\d{3}$"), "axes.tsv": ("axis_id", r"^YA-\d{2}$"), "constants.tsv": ("constant_id", r"^YK-\d{2}$"),
       "cases.tsv": ("case_id", r"^YC-\d{2}$"), "citations.tsv": ("cite_id", r"^YE-\d{3}$")}
BASES = {"today", "in force", "occurred", "provided for"}
FETCHED = {"inside Yemen", "outside Yemen", "attestation"}
WHO = {"agent", "founder", "reader"}
SOURCE = re.compile(r"^sharrwah-knowledge-map@[0-9a-f]{7,40}:evidence/yemen/(runs|blocked-evidence-founder|derived|attestations)/")
MAX_AXES = 20
issues = []

def err(f, i, x, level="error"):
    issues.append((level, f, i, x))

def read(name):
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
    if head != HEADERS[name]:
        err(name, "", f"header is {head}, expected {HEADERS[name]}")
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

data = {n: read(n) for n in HEADERS}
conds, axes, consts, cases, cits, unk = (data[n] for n in HEADERS)
if not os.path.exists(os.path.join(study, "notes.md")):
    err("notes.md", "", "file missing")
for name, (key, pat) in IDS.items():
    for k, n in Counter(r[key] for r in data[name]).items():
        if n > 1:
            err(name, k, f"id used {n} times")
    for r in data[name]:
        if not re.match(pat, r[key]):
            err(name, r[key], f"id doesn't match {pat}")
cit_ids = {c["cite_id"] for c in cits}
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

if len(axes) > MAX_AXES:
    err("axes.tsv", "", f"{len(axes)} axes: the brief stops for review past {MAX_AXES}", "review")
    if cases:
        err("cases.tsv", "", f"cases were built past the {MAX_AXES}-axis stop for review")
cond_ids = {c["condition_id"] for c in conds}
for c in conds:
    if not c["condition"] or not c["state"]:
        err("conditions.tsv", c["condition_id"], "condition or state is empty")
    if not c["held_at"] or not c["date_basis"]:
        err("conditions.tsv", c["condition_id"], "held_at or date_basis is empty")
    cites("conditions.tsv", c["condition_id"], c["cite_ids"])
placed = Counter(x for r in axes + consts for x in ids(r["condition_ids"]))
for x, n in placed.items():
    if x not in cond_ids:
        err("axes.tsv", x, "a condition_id that conditions.tsv doesn't hold")
    elif n > 1:
        err("axes.tsv", x, f"condition on {n} axes or constants; each sits on exactly one")
for x in cond_ids - set(placed):
    err("conditions.tsv", x, "on no axis and no constant")
unknown_about = {u["about"] for u in unk}
labels, today = {}, {}

def part_ok(aid, x):
    x = x.strip()
    return x in labels.get(aid, []) or x == "unknown" or x == "disputed" or x.startswith("disputed @ ")
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
    t = today[aid] = a["today"]
    if not all(part_ok(aid, x) for x in t.split(" + ")):
        err("axes.tsv", aid, f"today '{t[:50]}' is not its state labels joined by ' + ', with 'disputed' or 'unknown' parts")
    if "unknown" in [x.strip() for x in t.split(" + ")] and aid not in unknown_about:
        err("axes.tsv", aid, "today has an unknown part, but unknowns.tsv has no row about it")
    if t != "unknown":
        cites("axes.tsv", f"{aid} today", a["today_cite_ids"])
    if not ids(a["condition_ids"]):
        err("axes.tsv", aid, "condition_ids is empty")
for k in consts:
    cites("constants.tsv", k["constant_id"], k["cite_ids"])
    if not ids(k["condition_ids"]):
        err("constants.tsv", k["constant_id"], "condition_ids is empty")
case_ids = {c["case_id"] for c in cases}
if "YC-00" not in case_ids:
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
quotes = []
for c in cits:
    cid, src = c["cite_id"], c["source"]
    if not SOURCE.match(src):
        err("citations.tsv", cid, f"source '{src[:90]}' is not Yemen evidence at a pinned commit")
    if not c["quote"]:
        err("citations.tsv", cid, "quote is empty")
    if "..." in c["quote"] or "…" in c["quote"]:
        err("citations.tsv", cid, "quote contains an ellipsis")
    if len(c["quote"]) > 300:
        err("citations.tsv", cid, f"quote is {len(c['quote'])} characters; the brief allows 300")
    if c["fetched_from"] not in FETCHED:
        err("citations.tsv", cid, f"fetched_from '{c['fetched_from']}' is not one of {sorted(FETCHED)}")
    for col in ("locator", "source_date", "date_basis"):
        if not c[col]:
            err("citations.tsv", cid, f"{col} is empty")
    if cid not in used:
        err("citations.tsv", cid, "not used by any state, today, constant or case", "warning")
    res, why, share = SRC.check_quote(c["quote"], src) if c["quote"] and src else ("unresolved", "no quote or source", "")
    if not res.startswith("found"):
        err("citations.tsv", cid, f"quote {res}{'; ' + why if why else ''}{'; best 6-word share ' + share if share else ''}")
    quotes.append((cid, res, why, share, src, c["quote"][:200]))
with open(os.path.join(OUT, "yemen-cases-issues.tsv"), "w", encoding="utf-8") as f:
    f.write("level\tfile\tid\tissue\n")
    for row in issues:
        f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in row) + "\n")
with open(os.path.join(OUT, "yemen-cases-quotes.tsv"), "w", encoding="utf-8") as f:
    f.write("cite_id\tresult\twhy\tshare_of_6-word_runs_found\tsource\tquote_start\n")
    for q in quotes:
        f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in q) + "\n")
print(f"conditions {len(conds)}, axes {len(axes)}, constants {len(consts)}, cases {len(cases)}, citations {len(cits)}, unknowns {len(unk)} | "
      f"issues: {dict(Counter(i[0] for i in issues))} | quotes: {dict(Counter(q[1].split(' (')[0] for q in quotes))}")
