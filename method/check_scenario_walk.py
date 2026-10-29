"""Check a subject's scenario walk (SUBJECT_DIR/scenario-walk.tsv) against its brief (`briefs/F-scenario-walk.md`).

Usage: python3 -I method/check_scenario_walk.py SUBJECT_DIR

It checks:
- the columns, in the brief's order;
- that each `decision_id` is a founder decision or an engineering constraint of SUBJECT_DIR/register.tsv, and that each
  of those is walked through the brief's three scenarios: a second market, the company based in another country, and
  the first market dropped (told apart by their words: "second market", "based in" or "company", "dropped");
- that `root_decision` is one of the frame's (RD1, RD2, ...);
- that `cost` is a setting, one module or a redesign, and `flag` is premature, one market or empty;
- that a row which closes an option gives its reason, one of the brief's three (a confirmed fact, the founder's
  choice, an engineering cost greater than the option's value), or is flagged premature;
- that `market` is named or `hypothetical`;
- that each cited id is the subject's: a statement, variant, variation point or register row.
Prints each problem, and exits 1 if there is any.
"""
import csv, glob, os, re, sys

csv.field_size_limit(10**9)
COLUMNS = ["root_decision", "decision_id", "scenario", "market", "what_changes", "cost", "keeps_open", "closes", "reason",
           "flag", "evidence", "note"]
COSTS = ("a setting", "one module", "a redesign")
FLAGS = ("premature", "one market", "")
SCENARIOS = (("a second market", re.compile(r"second market|another market|market whose", re.I)),
             ("the company based elsewhere", re.compile(r"based in|company|headquarter", re.I)),
             ("the first market dropped", re.compile(r"dropped|drop", re.I)))
REASONS = re.compile(r"confirmed fact|founder'?s? (?:own )?(?:choice|decision)|engineering cost", re.I)
NOTHING = re.compile(r"^(?:nothing|none|—|-|n/a)\b", re.I)


def rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def first_column(path):
    return {r[0] for r in rows(path) if r}


def main(subj):
    table = rows(os.path.join(subj, "scenario-walk.tsv"))
    problems = []
    if table[0] != COLUMNS:
        problems.append(f"columns are {table[0]}, not {COLUMNS}")
    for n, r in enumerate(table[1:], start=2):
        if len(r) != len(table[0]):
            problems.append(f"line {n}: {len(r)} fields, not {len(table[0])}")
    data = [dict(zip(table[0], r)) for r in table[1:] if any(x.strip() for x in r)]
    reg = rows(os.path.join(subj, "register.tsv"))
    register = [dict(zip(reg[0], r)) for r in reg[1:]]
    walked = {r["id"] for r in register if r.get("kind") in ("founder decision", "engineering constraint")}
    roots = {os.path.basename(p) for p in glob.glob(os.path.join(subj, "c", "RD*"))}
    ids = {r["id"] for r in register}
    for p in glob.glob(os.path.join(subj, "*", "statements.tsv")):
        ids |= first_column(p)
    for f in ("variants.tsv", "variation-points.tsv"):
        ids |= first_column(os.path.join(subj, f))
    seen = {}
    for n, r in enumerate(data, start=2):
        where = f"line {n} ({r.get('decision_id', '')})"
        d = r.get("decision_id", "")
        if d not in walked:
            problems.append(f"{where}: not a founder decision or engineering constraint of the register")
        if r.get("root_decision") not in roots:
            problems.append(f"{where}: root decision '{r.get('root_decision')}' is not one of {sorted(roots)}")
        kinds = [name for name, words in SCENARIOS if words.search(r.get("scenario", ""))]
        if not kinds:
            problems.append(f"{where}: scenario '{r.get('scenario', '')[:60]}' is none of the brief's three")
        seen.setdefault(d, set()).update(kinds[:1])
        if r.get("cost") not in COSTS:
            problems.append(f"{where}: cost is '{r.get('cost')}'")
        if r.get("flag", "") not in FLAGS:
            problems.append(f"{where}: flag is '{r.get('flag')}'")
        closes = r.get("closes", "").strip()
        if closes and not NOTHING.match(closes) and r.get("flag") != "premature" and not REASONS.search(r.get("reason", "")):
            problems.append(f"{where}: closes an option with none of the three reasons, and isn't flagged premature")
        market = r.get("market", "").strip()
        if not market:
            problems.append(f"{where}: no market, named or hypothetical")
        for i in re.findall(r"\bS\d\d-(?:[A-Z]{2}-\d+|V-\d+|VP-\d+|[RDEFM]\d+)\b", " ".join((r.get("evidence", ""), r.get("reason", "")))):
            if i not in ids:
                problems.append(f"{where}: {i} not found")
    for d in sorted(walked):
        missing = [name for name, _ in SCENARIOS if name not in seen.get(d, set())]
        if missing:
            problems.append(f"{d}: not walked through {', '.join(missing)}")
    for p in problems:
        print(p)
    redesigns = [r for r in data if r.get("cost") == "a redesign"]
    flagged = [r for r in data if r.get("flag")]
    print(f"{len(data)} rows, {len(walked)} decisions and constraints; {len(redesigns)} a redesign, {len(flagged)} flagged; "
          f"{len(problems)} problem(s)")
    for r in redesigns + flagged:
        print(f"- {r['decision_id']}, {r['scenario'][:50]}: {r['cost']}{', ' + r['flag'] if r.get('flag') else ''}")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
