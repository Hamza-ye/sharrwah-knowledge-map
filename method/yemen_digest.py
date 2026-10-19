"""Write the digest of Stage 1's axes and constants that step R4's drafting runs read (PLAN.md section 4, step R4).

Usage: python3 -I method/yemen_digest.py [OUT]

Reads studies/yemen-cases/ (conditions.tsv, citations.tsv, groups.tsv and states.tsv, as Stage 1's build does, and
axes.tsv, constants.tsv and unknowns.tsv as written) and writes OUT, by default studies/proposals/yemen-digest.md:
- each axis with what varies, and each part of its today: the state, its place, the date it held at, and the
  citations it rests on. Proposed states are listed apart, since a proposed state is never today;
- each constant with its state, the places it holds at, each with its date and citations, and its other rows;
- Stage 1's unknowns.

Today and its parts are recomputed with the build's own functions, and checked against axes.tsv and constants.tsv
as written: the digest is refused if they differ, since Stage 1's files would then not be what its build makes.
"""
import hashlib, os, re, sys
from collections import OrderedDict, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_yemen_cases import (ACROSS, full, ids, joined, pick, place_order, read_tsv, settle, uniq, when)

SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUDY = os.path.join(SKM, "studies", "yemen-cases")
OUT = os.path.join(SKM, "studies", "proposals", "yemen-digest.md")

HOW = """## How to read it

- **An axis** is a condition Stage 1 found in more than one state; **a constant**, one it found in a single state.
- **Today** is each place's latest held state, as Stage 1's build takes it. Each part gives the state, its place after
  "@", and the date it held at ("as of", from the condition's `held_at`). A part reads `unknown` where the latest
  state at that place ended, and `disputed` where sources of the same date disagree.
- **Ids.** `YA-` an axis and `YK-` a constant, in `studies/yemen-cases/axes.tsv` and `constants.tsv`; `YQ-` a
  condition, in `conditions.tsv`; `YE-` a citation with its quote, in `citations.tsv`. This digest gives no `YE-`
  ids. A state's citations are in its axis's `states` column, after the state, and a constant's in its `cite_ids`
  column. Its other rows (ended, proposed, or at places where it no longer holds) are in its `note` column.
- **Stage 1's rules for reading a state:**
  - a condition's states are alternatives: only one holds at a place and time;
  - a state's place is the scope its source gives it;
  - only a state whose source says it holds in all of Yemen ("across Yemen") supersedes states at other places;
  - a proposed state is never today;
  - each part of today is read with its date.
- **The frame:** the merchant sells in the Yemeni market. A condition naming only countries or regions is read
  against that.
- **Not shown** is not shown: where no axis, constant or citation gives a fact, Yemen's evidence doesn't show it.
"""


def cell(s):
    return " ".join((s or "").split())


def parts_of(rs):
    """[(place, value, rows it rests on)] for an axis's today, as the build makes it."""
    across = [r for r in rs if r["place"] == ACROSS]
    out = []
    for p in place_order({r["place"] for r in rs}):
        if p == ACROSS:
            if not any(r["holds"] == "held" for r in across):
                continue
            v, top, _ = settle(across, [], p)
        else:
            v, top, _ = settle([r for r in rs if r["place"] == p], across, p)
        out.append((p, v, top))
    return out


def dated(top):
    ats = uniq(r["at"] for r in top if r["at"])
    return f" (as of {', '.join(ats)})" if ats else " (undated)"


def digest(study=STUDY):
    _, conds = read_tsv(os.path.join(study, "conditions.tsv"))
    _, cits = read_tsv(os.path.join(study, "citations.tsv"))
    _, groups = read_tsv(os.path.join(study, "groups.tsv"))
    _, states = read_tsv(os.path.join(study, "states.tsv"))
    _, axes_rows = read_tsv(os.path.join(study, "axes.tsv"))
    _, const_rows = read_tsv(os.path.join(study, "constants.tsv"))
    _, unknowns = read_tsv(os.path.join(study, "unknowns.tsv"))
    cond = {c["condition_id"]: c for c in conds}
    source = {c["cite_id"]: c["source"].split(":", 1)[-1] for c in cits}
    by_group = defaultdict(list)
    for s in states:
        c = cond[s["condition_id"]]
        cs = ids(c["cite_ids"])
        by_group[s["group_id"]].append({
            "id": s["condition_id"], "label": s["label"], "place": s["place"], "full": full(s["label"], s["place"]),
            "holds": s["holds"], "now": s["now"] == "yes", "when": when(c["held_at"]), "at": c["held_at"],
            "before": bool(re.match(r"^before\b", c["held_at"].strip(), re.I)),
            "cites": cs, "sources": frozenset(source[x] for x in cs if x in source)})
    axes, consts = [], []
    for g in groups:
        rs = by_group.get(g["group_id"], [])
        if rs:
            shown = {r["label"] for r in rs if r["holds"] != "proposed"}
            (axes if len(shown) > 1 else consts).append((g, rs))
    written_axes = {a["axis_id"]: a for a in axes_rows}
    written_consts = {k["constant_id"]: k for k in const_rows}
    problems, lines = [], []

    lines.append("## Axes\n")
    for n, (g, rs) in enumerate(axes, start=1):
        aid = f"YA-{n:02d}"
        ps = parts_of(rs)
        today = joined(OrderedDict((p, v) for p, v, _ in ps))
        w = written_axes.get(aid)
        if not w or w["axis"] != g["condition"] or w["today"] != today:
            problems.append(f"{aid}: today as built differs from axes.tsv")
        lines.append(f"- **{aid}** {cell(g['condition'])}: {cell(g['what_varies'])}.")
        shown_today = set()
        for p, v, top in ps:
            between = ""
            if v.startswith("disputed @ "):
                between = ", between " + " / ".join(cell(f) for f in uniq(r["full"] for r in top))
            shown_today |= {v} | {r["full"] for r in top}
            lines.append(f"  - today: {cell(v)}{between}{dated(top)}")
        proposed = [f for f in uniq(r["full"] for r in rs) if all(r["holds"] == "proposed" for r in rs if r["full"] == f)]
        for f in proposed:
            rr = [r for r in rs if r["full"] == f]
            lines.append(f"  - proposed, never today: {cell(f)}{dated(rr)}")
        others = [f for f in uniq(r["full"] for r in rs) if f not in shown_today and f not in proposed]
        if others:
            lines.append(f"  - other states recorded: {len(others)}, in axes.tsv")
    lines.append("\n## Constants\n")
    for n, (g, rs) in enumerate(consts, start=1):
        kid = f"YK-{n:02d}"
        shown = [r for r in rs if r["holds"] != "proposed"]
        w = written_consts.get(kid)
        if not w or w["condition"] != g["condition"]:
            problems.append(f"{kid}: differs from constants.tsv")
        holding = []
        for p in place_order({r["place"] for r in rs}):
            top = pick([r for r in rs if r["place"] == p])
            held = [r for r in top if r["holds"] == "held"]
            if held:
                holding.append(f"{p}{dated(held)}")
        state = cell(shown[0]["label"]) if shown else "proposed"
        rest = len([x for x in (w["note"] if w else "").split("; ") if x.strip()])
        lines.append(f"- **{kid}** {cell(g['condition'])}: {state}, at {'; '.join(holding) if holding else 'no place where it holds'}"
                     + (f". Other rows: {rest}, in constants.tsv" if rest else ""))
    lines.append("\n## What Stage 1 couldn't find\n")
    for u in unknowns:
        lines.append(f"- **{u['about']}** {cell(u['what_would_show_it'])}")
    return lines, problems


def main(argv):
    out = argv[0] if argv else OUT
    lines, problems = digest()
    if problems:
        sys.exit("refused: " + "; ".join(problems[:10]))
    sha = hashlib.sha256(open(os.path.join(STUDY, "axes.tsv"), "rb").read()).hexdigest()
    head = ("# Yemen's evidence, digested for the drafting runs\n\n"
            f"Written by `method/yemen_digest.py` from Stage 1's files in `studies/yemen-cases/` (axes.tsv sha256 "
            f"`{sha[:16]}`). Don't edit it by hand: re-run the script.\n\n")
    with open(out, "w", encoding="utf-8") as f:
        f.write(head + HOW + "\n" + "\n".join(lines) + "\n")
    print(f"wrote {os.path.relpath(out, SKM)}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
