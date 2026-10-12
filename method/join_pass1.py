# Joins Stage 1's pass 1 parts (studies/yemen-cases/pass1/{conditions,citations}-<part>.tsv) into the study's
# conditions.tsv and citations.tsv, unchanged and in part order, and writes pass2/wordings.tsv: one line per
# condition wording, with its parts, rows and places, which step 2a reads to group the rows into conditions.
# It refuses to join if a part is missing, a header differs, an id repeats, or a condition cites a missing citation.
#
# Usage: python3 -I method/join_pass1.py STUDY_DIR
import csv, os, re, sys
from collections import Counter, OrderedDict

PARTS = "ABCDEF"
HEAD = {"conditions": ["condition_id", "condition", "state", "place", "held_at", "date_basis", "cite_ids", "note"],
        "citations": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "fetched_from", "url"]}

def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    return rows[0] if rows else [], [r for r in rows[1:] if any(c.strip() for c in r)]

def main(study):
    problems, joined = [], {}
    for kind, head in HEAD.items():
        out = []
        for p in PARTS:
            path = os.path.join(study, "pass1", f"{kind}-{p}.tsv")
            if not os.path.exists(path):
                problems.append(f"{path} is missing")
                continue
            h, rows = read(path)
            if h != head:
                problems.append(f"{path}: header {h}")
            for n, r in enumerate(rows, start=2):
                if len(r) != len(head):
                    problems.append(f"{path} line {n}: {len(r)} fields")
            out += rows
        for k, n in Counter(r[0] for r in out).items():
            if n > 1:
                problems.append(f"{kind}: {k} used {n} times")
        joined[kind] = out
    cite_ids = {r[0] for r in joined["citations"]}
    for r in joined["conditions"]:
        for x in re.split(r"[,\s;]+", r[6]):
            if x and x not in cite_ids:
                problems.append(f"conditions: {r[0]} cites {x}, which no part holds")
    if problems:
        print("not joined:\n  " + "\n  ".join(problems[:50]))
        sys.exit(1)
    for kind, head in HEAD.items():
        with open(os.path.join(study, f"{kind}.tsv"), "w", encoding="utf-8") as f:
            f.write("\t".join(head) + "\n")
            for r in joined[kind]:
                f.write("\t".join(r) + "\n")
    words = OrderedDict()
    for r in joined["conditions"]:
        w = words.setdefault(r[1], {"parts": OrderedDict(), "ids": [], "places": Counter()})
        w["parts"][r[0][3]] = 1
        w["ids"].append(r[0])
        w["places"][r[3]] += 1
    os.makedirs(os.path.join(study, "pass2"), exist_ok=True)
    with open(os.path.join(study, "pass2", "wordings.tsv"), "w", encoding="utf-8") as f:
        f.write("condition\tparts\trows\tcondition_ids\tplaces\n")
        for w, v in words.items():
            f.write(f"{w}\t{''.join(v['parts'])}\t{len(v['ids'])}\t{', '.join(v['ids'])}\t"
                    f"{'; '.join(f'{p} ({n})' for p, n in v['places'].most_common())}\n")
    print(f"joined {len(joined['conditions'])} conditions and {len(joined['citations'])} citations; "
          f"{len(words)} condition wordings in pass2/wordings.tsv")

if __name__ == "__main__":
    main(sys.argv[1].rstrip("/"))
