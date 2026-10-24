# Lists the backlog (decisions/subjects.tsv) and the decision records (decisions/D-*.md) by status, and checks
# that the backlog covers each of the 34 areas once (METHOD.md sections 4 and 9).
#
# With --guard it runs METHOD.md section 3a's market guard instead:
# - on each decision record whose outcome is Built: its "Decision outcome" and "Consequences" sections must name
#   no market, and its evidence must not come only from one market's Context ids (Stage 1's Y..- ids);
# - on each other Markdown file given, such as a draft: every line in a design section that names a market. A
#   draft's design sections are 2 to 5 (studies/proposals/briefs/R4-drafting.md); --sections changes them.
# The guard prints what it flags and exits 1 if it flags anything. A flag is for the coordinator to judge: a
# general mechanism with a precedent is allowed (METHOD.md section 3a).
#
# Usage: python3 -I method/decision_status.py
#        python3 -I method/decision_status.py --guard [--sections 2,3,4,5] [FILE.md ...]
import csv, glob, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SKM = os.path.dirname(HERE)
SUBJECTS = os.path.join(SKM, "decisions", "subjects.tsv")
AREAS = os.path.join(SKM, "studies", "proposals", "areas", "areas.tsv")
RECORDS = os.path.join(SKM, "decisions", "D-*.md")
MARKET = re.compile(r"\b(Yemen|Yemeni|Sana'?a|Aden|rials?|YER|Oman|Omani|Saudi|KSA|riyals?|UAE|Emirati|Egypt|Egyptian)\b"
                    r"|اليمن|صنعاء|عدن|ريال|عمان|السعودية")
MARKET_CONTEXT_ID = re.compile(r"^Y[A-Z]-\d+")
STATUSES = ("in progress", "waiting on the founder", "open", "closed")
RECORD_STATUSES = ("proposed", "accepted", "deferred", "under review", "superseded")


def tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def expand(ids):
    """'A-01 to A-34' or 'A-04 A-05' -> the list of area ids."""
    m = re.fullmatch(r"A-(\d+) to A-(\d+)", ids.strip())
    if m:
        return [f"A-{n:02d}" for n in range(int(m.group(1)), int(m.group(2)) + 1)]
    return ids.split()


def fields(text):
    """The fields block at the top of a record, between two '---' lines."""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(":")
        out[k.strip()] = re.sub(r"\s+#.*$", "", v).strip()
    return out


def sections(text, level="## "):
    """{heading: [(line number, line), ...]} for one heading level."""
    out, cur = {}, None
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith(level):
            cur = line[len(level):].strip()
            out[cur] = []
        elif cur is not None:
            out[cur].append((n, line))
    return out


def status():
    subjects = tsv(SUBJECTS)
    print(f"Backlog: {len(subjects)} subjects ({SUBJECTS[len(SKM) + 1:]})")
    for s in subjects:
        print(f"  {s['id']}  {s['status']:<24} {s['milestone']:<12} {s['subject']}")
    count = Counter(s["status"] for s in subjects)
    print("  by status: " + ", ".join(f"{k} {count[k]}" for k in STATUSES if count[k]))
    bad = [s["id"] for s in subjects if s["status"] not in STATUSES]
    if bad:
        print(f"  unknown status: {' '.join(bad)}")

    owner = {}
    for s in subjects:
        if s["id"] == "S-15" or s["id"] == "S-02":      # these cover every area as a whole, not as owners
            continue
        for a in expand(s["areas"]):
            owner.setdefault(a, []).append(s["id"])
    areas = [r["area_id"] for r in tsv(AREAS)]
    missing = [a for a in areas if a not in owner]
    twice = [f"{a} ({' '.join(owner[a])})" for a in areas if len(owner.get(a, [])) > 1]
    print(f"Areas: {len(areas) - len(missing)} of {len(areas)} have a subject"
          + (f"; none for {' '.join(missing)}" if missing else "")
          + (f"; more than one for {', '.join(twice)}" if twice else ""))

    records = sorted(glob.glob(RECORDS))
    print(f"Decision records: {len(records)}")
    rc = Counter()
    for path in records:
        f = fields(open(path, encoding="utf-8").read())
        st = f.get("status", "")
        rc[st.split()[0] if st else "no status"] += 1
        print(f"  {f.get('id', '?'):<6} {st:<16} {f.get('door', ''):<8} {f.get('outcome', ''):<11} "
              f"{f.get('subject', ''):<5} {f.get('title', os.path.basename(path))}")
    if records:
        print("  by status: " + ", ".join(f"{k} {v}" for k, v in sorted(rc.items())))
    return 1 if (missing or twice or bad) else 0


def guard(paths, design):
    flagged = 0
    for path in sorted(glob.glob(RECORDS)):
        text = open(path, encoding="utf-8").read()
        f = fields(text)
        if f.get("outcome", "").lower() != "built":
            continue
        secs = sections(text)
        for name in ("Decision outcome", "Consequences"):
            for n, line in secs.get(name, []):
                if MARKET.search(line):
                    flagged += 1
                    print(f"{path[len(SKM) + 1:]}:{n}: [{name}] names a market: {line.strip()[:160]}")
        ev = [e for e in re.split(r"[,\s]+", f.get("evidence", "")) if e and e != "—"]
        if ev and all(MARKET_CONTEXT_ID.match(e) for e in ev):
            flagged += 1
            print(f"{path[len(SKM) + 1:]}: a Built outcome resting only on one market's Context ids: {' '.join(ev)}")
    for path in paths:
        text = open(path, encoding="utf-8").read()
        cur = None
        for n, line in enumerate(text.splitlines(), 1):
            m = re.match(r"## (\d+)\.", line)
            if line.startswith("## "):
                cur = int(m.group(1)) if m else None
                continue
            if cur in design and MARKET.search(line):
                flagged += 1
                print(f"{path}:{n}: [section {cur}] names a market: {line.strip()[:160]}")
    print(f"Guard: {flagged} flagged")
    return 1 if flagged else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--guard":
        args = args[1:]
        design = {2, 3, 4, 5}
        if args[:1] == ["--sections"]:
            design = {int(x) for x in args[1].split(",")}
            args = args[2:]
        sys.exit(guard(args, design))
    sys.exit(status())
