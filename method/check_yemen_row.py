"""Check a subject's Yemen row (SUBJECT_DIR/yemen-row.tsv) against its brief (`briefs/E-yemen-row.md`).

Usage: python3 -I method/check_yemen_row.py SUBJECT_DIR

It checks:
- the columns, in the brief's order;
- that each `decision_id` is a founder decision of SUBJECT_DIR/register.tsv, and that every founder decision has rows;
- that `exists` is yes, no or unknown; that a yes or a no cites Stage 1's ids, with each fact's date in `as_of`, unless
  the option needs nothing particular in any market or the row takes another row's facts ("As (a)"); and that an
  unknown says what would show it;
- that each cited Stage 1 id (YA, YK, YC, YE, YQ) is in its file in `studies/yemen-cases/`;
- that no product gap names Yemen, or a place, party or currency that only Yemen has (`PLAN.md`, section 6, step 5).
It warns where a lettered option of a decision's `alternatives`, (a), (b) and on, has no row that starts with it.
It then lists each cited id that Stage 1's `corrections.md` corrects or cautions, with what the record should say,
for the coordinator to read against the row. Prints each problem, and exits 1 if there is any.
"""
import csv, os, re, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YEMEN = os.path.join(SKM, "studies", "yemen-cases")
COLUMNS = ["decision_id", "option", "needs", "exists", "evidence", "as_of", "what_would_show_it", "product_gap", "note"]
FILES = {"YA": "axes.tsv", "YK": "constants.tsv", "YC": "cases.tsv", "YE": "citations.tsv", "YQ": "conditions.tsv"}
# Names that only Yemen has; a product gap is written without them
YEMEN_ONLY = re.compile(r"\bYemen\w*|\bSana'?a\b|\bAden\b|\bHouthi\w*|\bCBY\b|\bKuraimi\b|\bYER\b|اليمن|يمني|صنعاء|عدن|الحوثي",
                        re.I)
# A currency name Yemen shares with others: a warning, not a problem
SHARED = re.compile(r"\brials?\b|ريال", re.I)


def rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def first_column(path):
    return {r[0] for r in rows(path) if r}


def corrections():
    """Stage 1's corrections and cautions, by the id each row of corrections.md's table names first."""
    found = {}
    for line in open(os.path.join(YEMEN, "corrections.md"), encoding="utf-8"):
        m = re.match(r"\| \[(Y[A-Z]-\d+)\]\([^)]*\) \| (correction|caution) \| (.*?) \|", line)
        if m:
            found[m.group(1)] = (m.group(2), m.group(3))
    return found


def main(subj):
    table = rows(os.path.join(subj, "yemen-row.tsv"))
    problems, warnings = [], []
    if table[0] != COLUMNS:
        problems.append(f"columns are {table[0]}, not {COLUMNS}")
    data = [dict(zip(table[0], r)) for r in table[1:] if any(x.strip() for x in r)]
    for n, r in enumerate(table[1:], start=2):
        if len(r) != len(table[0]):
            problems.append(f"line {n}: {len(r)} fields, not {len(table[0])}")
    register = [dict(zip(rows(os.path.join(subj, "register.tsv"))[0], r)) for r in rows(os.path.join(subj, "register.tsv"))[1:]]
    decisions = {r["id"]: r for r in register if r.get("kind") == "founder decision"}
    ids = {k: first_column(os.path.join(YEMEN, f)) for k, f in FILES.items()}
    fixes = corrections()
    cited_fixes = {}
    for n, r in enumerate(data, start=2):
        where = f"line {n} ({r.get('decision_id', '')})"
        if r.get("decision_id") not in decisions:
            problems.append(f"{where}: not a founder decision of the register")
        exists = r.get("exists", "").strip()
        if exists not in ("yes", "no", "unknown"):
            problems.append(f"{where}: exists is '{exists}'")
        cited = re.findall(r"\bY[AKCEQ]-[A-Z]?\d+\b", r.get("evidence", ""))
        # An option that needs nothing particular in any market cites nothing; a row may take another row's facts ("As (a)")
        bare = "nothing particular" in r.get("needs", "").lower() or r.get("evidence", "").startswith("As ")
        if exists in ("yes", "no") and not cited and not bare:
            problems.append(f"{where}: exists is {exists} with no Stage 1 id")
        if cited and not r.get("as_of", "").strip():
            problems.append(f"{where}: cites {', '.join(cited)} with no date in as_of")
        if exists == "unknown" and not r.get("what_would_show_it", "").strip():
            problems.append(f"{where}: unknown, with nothing saying what would show it")
        for i in cited:
            if i not in ids[i[:2]]:
                problems.append(f"{where}: {i} not in {FILES[i[:2]]}")
            if i in fixes:
                cited_fixes.setdefault(i, []).append(n)
        gap = r.get("product_gap", "")
        for m in YEMEN_ONLY.finditer(gap):
            problems.append(f"{where}: the product gap names '{m.group(0)}'")
        for m in SHARED.finditer(gap):
            warnings.append(f"{where}: the product gap names '{m.group(0)}', a currency Yemen shares with others")
    for d, r in decisions.items():
        mine = [x for x in data if x.get("decision_id") == d]
        if not mine:
            problems.append(f"{d}: no row")
            continue
        for letter in sorted(set(re.findall(r"(?:^|[.;]\s)\(([a-z])\)\s", r.get("alternatives", "")))):
            if not any(x.get("option", "").lstrip().startswith(f"({letter})") for x in mine):
                warnings.append(f"{d}: option ({letter}) has no row that starts with it")
    for p in problems:
        print(p)
    for w in warnings:
        print(f"warning: {w}")
    if cited_fixes:
        print("\nCited ids that Stage 1's corrections.md corrects or cautions; read each row against it:")
        for i, lines in sorted(cited_fixes.items()):
            kind, text = fixes[i]
            print(f"- {i} ({kind}), lines {', '.join(map(str, lines))}: {text}")
    print(f"\n{len(data)} rows, {len(decisions)} founder decisions; {len(problems)} problem(s), {len(warnings)} warning(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
