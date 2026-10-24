# Pulls a subject's questions from the Knowledge Map (register/km-questions.tsv) for its framing (METHOD.md
# section 5, step 1). A question belongs to a subject when its area is in the subject's km_areas, or its id is in
# the subject's covers (decisions/subjects.tsv). By default it lists the high-risk questions needed for the spine
# or the model; --all lists every one. Each line shows the question's disposition once one is set.
#
# Questions whose evidence cites Salla keys are marked: those paths moved when observed-sa was reorganized, and
# a row's pointers are repaired only when the row is used (register/README.md).
#
# --unassigned lists the questions that belong to no subject. There should be none.
#
# Usage: python3 -I method/km_select.py S-03 [--all]
#        python3 -I method/km_select.py --unassigned
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKM = os.path.dirname(HERE)
KM = os.path.join(SKM, "register", "km-questions.tsv")
SUBJECTS = os.path.join(SKM, "decisions", "subjects.tsv")


def tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def members(subject, questions):
    areas = set(subject["km_areas"].split())
    ids = set(re.findall(r"KM-[A-Z0-9]+-\d+", subject["covers"]))
    return [q for q in questions if q["area"] in areas or q["id"] in ids]


def show(q):
    salla = [k for k in q["evidence"].split() if k.startswith("sa.")]
    flags = " [Salla paths moved]" if salla else ""
    disp = q.get("disposition") or "no disposition yet"
    ref = q.get("disposition_ref") or ""
    print(f"{q['id']}  {q['risk']} {q['needed_by']:<6} {q['kind']:<6} {disp}{(' ' + ref) if ref else ''}{flags}")
    print(f"    {q['question']}")
    if q["feeds"]:
        print(f"    feeds: {q['feeds']}")
    if q["other_sources"]:
        print(f"    outside sources: {q['other_sources']}")


if __name__ == "__main__":
    questions, subjects = tsv(KM), tsv(SUBJECTS)
    args = sys.argv[1:]
    if args == ["--unassigned"]:
        seen = {q["id"] for s in subjects if s["id"] != "S-15" for q in members(s, questions)}
        left = [q["id"] for q in questions if q["id"] not in seen]
        print(f"{len(questions) - len(left)} of {len(questions)} questions belong to a subject"
              + (f"; none for {' '.join(left)}" if left else ""))
        sys.exit(1 if left else 0)
    if not args or args[0] not in {s["id"] for s in subjects}:
        sys.exit("Usage: python3 -I method/km_select.py S-NN [--all] | --unassigned")
    subject = next(s for s in subjects if s["id"] == args[0])
    rows = members(subject, questions)
    picked = rows if "--all" in args else [q for q in rows if q["risk"] == "H" and q["needed_by"] in ("spine", "model")]
    print(f"{subject['id']} {subject['subject']}: {len(picked)} of its {len(rows)} questions"
          + ("" if "--all" in args else " (high risk, needed for the spine or the model)"))
    for q in picked:
        show(q)
