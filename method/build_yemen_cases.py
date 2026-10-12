# Builds Stage 1's axes.tsv, constants.tsv and cases.tsv (studies/yemen-cases/brief.md, "The build") from pass 2's
# judgments, so that the brief's mechanical rules are applied the same way everywhere:
#   - a group whose held or provided-for rows carry two or more labels is an axis; otherwise it is a constant;
#   - today is the latest held state of each place (supersession, precision, disputes and `now` as the brief says);
#   - the further cases are one per non-today state, then one per combination a single source shows holding at
#     one time; a proposed state is listed on its axis but is never today and builds no case.
# Inputs in STUDY_DIR: conditions.tsv and citations.tsv (pass 1, joined), groups.tsv and states.tsv (pass 2).
# Past MAX_AXES axes it writes no cases (cases.tsv keeps only its header) until review-axes.md exists.
#
# Usage: python3 -I method/build_yemen_cases.py STUDY_DIR
import csv, os, re, sys
from collections import OrderedDict, defaultdict

ACROSS, NOT_STATED = "across Yemen", "place not stated"
CAPTURED = (2026, 10, 10)   # the evidence was captured by then: no source attests a later state
MAX_AXES = 20
HEADS = {
    "axes.tsv": ["axis_id", "axis", "what_varies", "condition_ids", "states", "today", "today_cite_ids", "note"],
    "constants.tsv": ["constant_id", "condition", "state", "place", "condition_ids", "cite_ids", "note"],
    "cases.tsv": ["case_id", "name", "axis_states", "basis", "cite_ids", "note"],
}

def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    head = rows[0] if rows else []
    return head, [{h: (r[k].strip() if k < len(r) else "") for k, h in enumerate(head)}
                  for r in rows[1:] if any(c.strip() for c in r)]

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

def when(s):
    """A held_at as (year[, month[, day]]); anything that isn't a date is undated (None)."""
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?(?:[ T]\d{1,2}:\d{2}(?::\d{2})?)?$", (s or "").strip())
    if not m:
        return None
    w = tuple(int(x) for x in m.groups() if x)
    return CAPTURED[:len(w)] if later(w, CAPTURED) else w

def later(a, b):
    """a is strictly later than b, compared at the coarser of their precisions."""
    n = min(len(a), len(b))
    return a[:n] > b[:n]

def full(label, place):
    return label if place == ACROSS else f"{label} @ {place}"

def place_order(places):
    rest = sorted(p for p in places if p not in (ACROSS, NOT_STATED))
    return ([ACROSS] if ACROSS in places else []) + rest + ([NOT_STATED] if NOT_STATED in places else [])

def uniq(xs):
    return list(OrderedDict.fromkeys(xs))

def latest(rs):
    dated = [r for r in rs if r["when"]]
    if not dated:
        return list(rs)                     # an undated state is the latest only where no state is dated
    return [r for r in dated if not any(later(o["when"], r["when"]) for o in dated)]

def settle(rs, place):
    """The part a place takes: (value, rows it rests on, labels that hold now there)."""
    held = [r for r in rs if r["holds"] == "held"]
    if not held:
        return f"unknown @ {place}", [], set()
    top = latest(held)
    # One source, two states: where a source marks one of its states `now`, its other states give way to it.
    nows = [r for r in top if r["now"]]
    top = [r for r in top if r["now"] or not any(n["sources"] & r["sources"] for n in nows)]
    if len({r["label"] for r in top}) == 1:
        own = [r for r in top if r["place"] != ACROSS]
        return (own or top)[0]["full"], top, {r["full"] for r in top}
    return f"disputed @ {place}", top, {r["full"] for r in top}

def joined(parts):
    return " + ".join(uniq(parts.values()))

def build(study):
    _, conds = read_tsv(os.path.join(study, "conditions.tsv"))
    _, cits = read_tsv(os.path.join(study, "citations.tsv"))
    _, groups = read_tsv(os.path.join(study, "groups.tsv"))
    _, states = read_tsv(os.path.join(study, "states.tsv"))
    cond = {c["condition_id"]: c for c in conds}
    source = {c["cite_id"]: c["source"].split(":", 1)[-1] for c in cits}
    by_group = defaultdict(list)
    for s in states:
        c = cond[s["condition_id"]]
        cites = ids(c["cite_ids"])
        by_group[s["group_id"]].append({
            "id": s["condition_id"], "label": s["label"], "place": s["place"], "full": full(s["label"], s["place"]),
            "holds": s["holds"], "now": s["now"] == "yes", "when": when(c["held_at"]),
            "cites": cites, "sources": frozenset(source[x] for x in cites if x in source)})
    axes, consts = [], []
    for g in groups:
        rs = by_group.get(g["group_id"], [])
        if rs:
            shown = {r["label"] for r in rs if r["holds"] != "proposed"}
            (axes if len(shown) > 1 else consts).append((g, rs))

    out = {"axes.tsv": [], "constants.tsv": [], "cases.tsv": []}
    for n, (g, rs) in enumerate(consts, start=1):
        shown = [r for r in rs if r["holds"] != "proposed"]
        state = shown[0]["label"] if shown else f"proposed: {rs[0]['label']}"
        proposed = uniq(f"{r['full']} [{', '.join(r['cites'])}]" for r in rs if r["holds"] == "proposed")
        out["constants.tsv"].append([f"YK-{n:02d}", g["condition"], state,
                                     "; ".join(place_order({r["place"] for r in (shown or rs)})),
                                     ", ".join(r["id"] for r in rs), ", ".join(uniq(x for r in rs for x in r["cites"])),
                                     ("proposed: " + " | ".join(proposed)) if shown and proposed else ""])
    info = OrderedDict()
    for n, (g, rs) in enumerate(axes, start=1):
        aid = f"YA-{n:02d}"
        places = place_order({r["place"] for r in rs})
        across = [r for r in rs if r["place"] == ACROSS]
        parts, rests, live, notes = OrderedDict(), [], set(), []
        for p in places:
            if p == ACROSS:
                if not any(r["holds"] == "held" for r in across):
                    continue                 # the part for places the axis doesn't name exists only when held
                v, top, now = settle(across, p)
            else:
                v, top, now = settle([r for r in rs if r["place"] == p] + across, p)
            parts[p], rests, live = v, rests + top, live | now
            if v.startswith("disputed @ "):
                notes.append(f"{v}: " + " / ".join(uniq(r["full"] for r in top)))
        order = sorted(uniq(r["full"] for r in rs),
                       key=lambda f: (places.index(next(r["place"] for r in rs if r["full"] == f)),
                                      min((r["when"] or (0,)) for r in rs if r["full"] == f)))
        tag = lambda f: " (proposed)" if all(r["holds"] == "proposed" for r in rs if r["full"] == f) else ""
        states_col = " | ".join(f"{f}{tag(f)} [{', '.join(uniq(x for r in rs if r['full'] == f for x in r['cites']))}]"
                                for f in order)
        info[aid] = {"rows": rs, "parts": parts, "order": order, "live": live}
        out["axes.tsv"].append([aid, g["condition"], g["what_varies"], ", ".join(r["id"] for r in rs), states_col,
                                joined(parts), ", ".join(uniq(x for r in rests for x in r["cites"])), "; ".join(notes)])

    reviewed = os.path.exists(os.path.join(study, "review-axes.md"))
    if len(axes) > MAX_AXES and not reviewed:
        return out, f"{len(axes)} axes: past {MAX_AXES}, the brief stops for review. No cases were built."

    today = OrderedDict((aid, joined(i["parts"])) for aid, i in info.items())
    cases, seen = [], {tuple(today.values())}

    def add(changes, cites, note):
        """changes: [(axis, place, full label)]. A case with those states and every other axis at today."""
        parts = {aid: OrderedDict(info[aid]["parts"]) for aid in {a for a, _, _ in changes}}
        for aid, p, f in sorted(changes, key=lambda c: c[1] != ACROSS):
            if p == ACROSS:
                parts[aid] = OrderedDict((k, f) for k in parts[aid]) or OrderedDict([(ACROSS, f)])
            else:
                parts[aid][p] = f
        st = OrderedDict(today)
        for aid, ps in parts.items():
            st[aid] = joined(ps)
        key = tuple(st.values())
        if key in seen:
            return
        seen.add(key)
        changed = [a for a in st if st[a] != today[a]]
        new = [(a, f) for a in changed for f in st[a].split(" + ") if f not in today[a].split(" + ")]
        if all(f in info[a]["live"] for a, f in new):
            basis = "in force"
        elif all(f in info[a]["live"] or any(r["holds"] == "held" for r in info[a]["rows"] if r["full"] == f) for a, f in new):
            basis = "occurred"
        else:
            basis = "provided for"
        cases.append(["; ".join(f"{a}={st[a]}" for a in changed), "; ".join(f"{a}={st[a]}" for a in st),
                      basis, ", ".join(uniq(cites)), note])

    for aid, i in info.items():                               # one per non-today state
        now_parts = set(i["parts"].values())
        for f in i["order"]:
            rs = [r for r in i["rows"] if r["full"] == f and r["holds"] != "proposed"]
            if f in now_parts or not rs:
                continue
            add([(aid, rs[0]["place"], f)], [x for r in rs for x in r["cites"]], "")
    combos = defaultdict(list)                                # one per combination a single source shows holding at once
    for aid, i in info.items():
        for r in i["rows"]:
            if r["holds"] == "held" and r["when"]:
                for s in r["sources"]:
                    combos[(s, r["when"])].append((aid, r))
    for (s, w), rs in sorted(combos.items()):
        changes, cites, slots = [], [], OrderedDict()
        for aid, r in rs:
            slots.setdefault((aid, r["place"]), []).append(r)
        for (aid, p), rr in slots.items():
            labels = uniq(r["full"] for r in rr)
            if len(labels) > 1:
                labels = uniq(r["full"] for r in rr if r["now"])
                if len(labels) != 1:
                    continue
            changes.append((aid, p, labels[0]))
            cites += [x for r in rr if r["full"] == labels[0] for x in r["cites"]]
        if changes:                                           # add() skips today and duplicates
            add(changes, cites, f"shown together by {s}, held at {'-'.join(f'{x:02d}' for x in w)}")

    out["cases.tsv"].append(["YC-00", "today", "; ".join(f"{a}={v}" for a, v in today.items()), "today",
                             ", ".join(uniq(x for i in info.values() for r in i["rows"] for x in r["cites"]
                                            if r["full"] in set(i["parts"].values()))), ""])
    for n, c in enumerate(cases, start=1):
        out["cases.tsv"].append([f"YC-{n:02d}"] + c)
    return out, f"{len(axes)} axes, {len(consts)} constants, {len(cases)} further cases"

def render(rows, head):
    clean = lambda v: re.sub(r"[\t\r\n]+", " ", str(v)).strip()
    return "\t".join(head) + "\n" + "".join("\t".join(clean(v) for v in r) + "\n" for r in rows)

if __name__ == "__main__":
    study = sys.argv[1].rstrip("/")
    out, summary = build(study)
    for name, rows in out.items():
        with open(os.path.join(study, name), "w", encoding="utf-8") as f:
            f.write(render(rows, HEADS[name]))
    print(summary)
