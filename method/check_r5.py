"""Check one file of step R5's checks against its card file (studies/proposals/briefs/R5-checks.md).

Usage: python3 -I method/check_r5.py FILE.tsv CARDS.md

Checks that FILE has the columns id, verdict, lines, what, fix and read, in order; that each row's verdict is one of
the brief's; that every card in CARDS has one row, and no row names a card that isn't there (a Yemen run's rows for
section 6 points, `<question>:<line>`, aside); that a row other than `holds` says what in `what`, and names its
lines where it fixes a point; and that each line given is of the form Q4:9. Prints each problem and exits 1 on any.
"""
import csv, re, sys

csv.field_size_limit(10**9)
COLUMNS = ["id", "verdict", "lines", "what", "fix", "read"]
VERDICTS = {"holds", "fix point", "fix record", "found", "later state", "open"}
LINE = re.compile(r"^Q[1-8]:\d+$")


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    tsv, cards = argv
    ids = re.findall(r"(?m)^### (\S+)", open(cards, encoding="utf-8").read())
    problems = []
    with open(tsv, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows or rows[0] != COLUMNS:
        problems.append(f"the header is {rows[0] if rows else 'missing'}: want {COLUMNS}")
        rows = rows[1:] if rows else []
    else:
        rows = rows[1:]
    seen = {}
    for n, r in enumerate(rows, start=2):
        if len(r) != len(COLUMNS):
            problems.append(f"line {n}: {len(r)} fields, want {len(COLUMNS)} (a tab or line break inside a field?)")
            continue
        i, verdict, lines, what, fix, read = r
        if i in seen:
            problems.append(f"line {n}: {i} has a row already, at line {seen[i]}")
        seen[i] = n
        if i not in ids and not re.match(r"^Q[1-8]:\d+$", i):
            problems.append(f"line {n}: {i} is no card of {cards}")
        if verdict not in VERDICTS:
            problems.append(f"line {n}: verdict '{verdict}': want one of {', '.join(sorted(VERDICTS))}")
        if verdict != "holds" and not what.strip():
            problems.append(f"line {n}: {i} is '{verdict}' and says nothing in `what`")
        if verdict == "fix point" and not lines.strip():
            problems.append(f"line {n}: {i} fixes a point and names no line")
        for x in lines.split():
            if not LINE.match(x):
                problems.append(f"line {n}: '{x}' in `lines`: want the form Q4:9")
    for i in ids:
        if i not in seen:
            problems.append(f"{i}: a card with no row")
    for p in problems:
        print(p)
    counts = {}
    for r in rows:
        if len(r) == len(COLUMNS):
            counts[r[1]] = counts.get(r[1], 0) + 1
    print(f"{len(rows)} rows for {len(ids)} cards; " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
          + (f"; {len(problems)} problems" if problems else "; no problems"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
