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
    "axes.tsv": ["axis_id", "axis", "what_varies", "states", "today", "today_cite_ids", "note"],
    "constants.tsv": ["constant_id", "condition", "cite_ids", "note"],
    "cases.tsv": ["case_id", "name", "axis_states", "basis", "place", "cite_ids", "note"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "fetched_from", "url"],
    "unknowns.tsv": ["about", "what_would_show_it", "who_can", "route", "read", "why_not_held"],
}
IDS = {"axes.tsv": ("axis_id", r"^YA-\d{2}$"), "constants.tsv": ("constant_id", r"^YK-\d{2}$"),
       "cases.tsv": ("case_id", r"^YC-\d{2}[a-z]?$"), "citations.tsv": ("cite_id", r"^YE-\d{3}$")}
BASES = {"today", "in force", "occurred", "provided for"}
FETCHED = {"inside Yemen", "outside Yemen"}
WHO = {"agent", "founder", "reader"}
SOURCE = re.compile(r"^sharrwah-knowledge-map@[0-9a-f]{7,40}:evidence/yemen/(runs|blocked-evidence-founder|derived|attestations)/")
MAX_AXES = 15
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
axes, consts, cases, cits, unk = (data[n] for n in HEADERS)
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
    err("axes.tsv", "", f"{len(axes)} axes: the brief says stop and report past {MAX_AXES}")
unknown_about = {u["about"] for u in unk}
labels, today = {}, {}
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
    if t not in labels[aid] and t not in ("disputed", "unknown"):
        err("axes.tsv", aid, f"today '{t[:50]}' is not one of its states, 'disputed' or 'unknown'")
    if t == "unknown":
        if aid not in unknown_about:
            err("axes.tsv", aid, "today is unknown, but unknowns.tsv has no row about it")
    else:
        cites("axes.tsv", f"{aid} today", a["today_cite_ids"])
for k in consts:
    cites("constants.tsv", k["constant_id"], k["cite_ids"])
case_ids = {c["case_id"] for c in cases}
today_cases = sorted(c for c in case_ids if re.match(r"^YC-00[a-z]?$", c))
if not today_cases:
    err("cases.tsv", "YC-00", "today's case is missing")
elif "YC-00" in today_cases and len(today_cases) > 1:
    err("cases.tsv", "YC-00", "today is either one case, YC-00, or split by place into YC-00a, YC-00b…, not both")
for c in cases:
    cid = c["case_id"]
    is_today = cid in today_cases
    if c["basis"] not in BASES:
        err("cases.tsv", cid, f"basis '{c['basis']}' is not one of {sorted(BASES)}")
    if is_today != (c["basis"] == "today"):
        err("cases.tsv", cid, "basis 'today' belongs to today's case(s) only")
    if (cid != "YC-00" and is_today) != bool(c["place"]):
        err("cases.tsv", cid, "place is given for today's split cases, and only for them")
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
        elif v not in labels[ax] and not (is_today and v == "disputed"):
            err("cases.tsv", cid, f"{ax}='{v[:50]}' is not one of that axis's state labels")
    for ax in given:
        if ax not in labels:
            err("cases.tsv", cid, f"{ax} is not an axis")
    if cid == "YC-00":
        for ax in labels:
            if given.get(ax) not in (today[ax], None):
                err("cases.tsv", cid, f"{ax} differs from that axis's today")
    elif not is_today:
        if "YC-00" in today_cases:
            changed = {ax for ax in labels if given.get(ax) not in (None, today[ax])}
            named = {p.split("=")[0].strip() for p in c["name"].split(";") if "=" in p}
            if not changed:
                err("cases.tsv", cid, "the same as today's case")
            elif named != changed:
                err("cases.tsv", cid, f"name lists {sorted(named)}, but the states that differ from today are {sorted(changed)}")
    cites("cases.tsv", cid, c["cite_ids"])
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
        err("citations.tsv", cid, f"fetched_from '{c['fetched_from']}' is not inside Yemen or outside Yemen")
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
print(f"axes {len(axes)}, constants {len(consts)}, cases {len(cases)}, citations {len(cits)}, unknowns {len(unk)} | "
      f"issues: {dict(Counter(i[0] for i in issues))} | quotes: {dict(Counter(q[1].split(' (')[0] for q in quotes))}")
