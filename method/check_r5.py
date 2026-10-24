"""Check one file of step R5's checks against its card file (studies/proposals/briefs/R5-checks.md).

Usage: python3 -I method/check_r5.py FILE.tsv CARDS.md

The kind of run is the card file's: claims-* an absence run, yemen* a Yemen run, doesnt-show a run on what Yemen's
evidence doesn't show, decisions* a run on the company decisions' points, any other a facts run. Checks:
- the columns id, verdict, lines, what, fix and read, in order, and one line per row;
- every card has one row, and no row names a card that isn't there;
- each verdict is one the run's kind allows;
- a row other than `holds` says what in `what`; a fix row gives its `fix`; every row but `holds` and `open` names its
  lines; `holds` carries no fix;
- each line given is one its card is cited at, written as Q4:9 (or D3:12 for the company decisions);
- an absence row's `read` shows its corpus search; a row on what Yemen's evidence doesn't show, its `rg` search.
Prints each problem, and exits 1 on any.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
COLUMNS = ["id", "verdict", "lines", "what", "fix", "read"]
ALLOWED = {
    "facts": {"holds", "fix point", "fix record", "open"},
    "absences": {"holds", "fix point", "fix record", "found", "open"},
    "yemen": {"holds", "fix point", "fix record", "later state", "open"},
    "doesnt-show": {"holds", "fix point", "found", "open"},
    "decisions": {"holds", "fix point", "open"},
}


def kind_of(cards):
    name = os.path.basename(cards)
    for prefix, kind in (("claims-", "absences"), ("yemen", "yemen"), ("doesnt-show", "doesnt-show"),
                         ("decisions", "decisions")):
        if name.startswith(prefix):
            return kind
    return "facts"


def cards_of(cards):
    """{card id: the lines it is cited at, as Q4:9}."""
    text = open(cards, encoding="utf-8").read()
    m = re.match(r"^(Q[1-8])-", os.path.basename(cards))
    q = m.group(1) if m else ""
    out = {}
    for block in re.split(r"(?m)^### ", text)[1:]:
        cid = block.split(None, 1)[0]
        at = re.search(r"\*\*Cited at:\*\*\s*(.*)", block)
        lines = set()
        for part in (at.group(1).split(";") if at else []):
            pm = re.search(r"(?:(Q[1-8]|D\d+),\s*)?(?:section \d+, )?line (\d+)", part.strip())
            if pm:
                lines.add(f"{pm.group(1) or q}:{pm.group(2)}")
        out[cid] = lines
    return out


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    tsv, cards = argv
    kind, known = kind_of(cards), cards_of(cards)
    allowed = ALLOWED[kind]
    problems = []
    with open(tsv, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows or rows[0] != COLUMNS:
        problems.append(f"the header is {rows[0] if rows else 'missing'}: want {COLUMNS}")
    rows = rows[1:] if rows else []
    seen = {}
    for n, r in enumerate(rows, start=2):
        if len(r) != len(COLUMNS):
            problems.append(f"line {n}: {len(r)} fields, want {len(COLUMNS)} (a tab or line break inside a field?)")
            continue
        i, verdict, lines, what, fix, read = r
        if i in seen:
            problems.append(f"line {n}: {i} has a row already, at line {seen[i]}")
        seen[i] = n
        if i not in known:
            problems.append(f"line {n}: {i} is no card of {os.path.basename(cards)}")
        if verdict not in allowed:
            problems.append(f"line {n}: verdict '{verdict}': a {kind} run gives one of {', '.join(sorted(allowed))}")
        if verdict != "holds" and not what.strip():
            problems.append(f"line {n}: {i} is '{verdict}' and says nothing in `what`")
        if verdict in ("fix point", "fix record") and not fix.strip():
            problems.append(f"line {n}: {i} is '{verdict}' and gives no `fix`")
        if verdict not in ("holds", "open") and not lines.strip():
            problems.append(f"line {n}: {i} is '{verdict}' and names no line")
        if verdict == "holds" and fix.strip():
            problems.append(f"line {n}: {i} holds, yet gives a fix")
        for x in lines.split():
            if not re.match(r"^(Q[1-8]|D\d+):\d+$", x):
                problems.append(f"line {n}: '{x}' in `lines`: want the form Q4:9")
            elif i in known and known[i] and x not in known[i]:
                problems.append(f"line {n}: {i} is not cited at {x} (its card: {', '.join(sorted(known[i]))})")
        if kind == "absences" and "corpus_search.py" not in read:
            problems.append(f"line {n}: {i}: `read` shows no corpus search")
        if kind == "doesnt-show" and not re.search(r"\brg\b", read):
            problems.append(f"line {n}: {i}: `read` shows no rg search")
    for i in known:
        if i not in seen:
            problems.append(f"{i}: a card with no row")
    for p in problems:
        print(p)
    counts = {}
    for r in rows:
        if len(r) == len(COLUMNS):
            counts[r[1]] = counts.get(r[1], 0) + 1
    print(f"{len(rows)} rows for {len(known)} cards ({kind}); " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
          + (f"; {len(problems)} problems" if problems else "; no problems"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
