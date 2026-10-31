"""After a round of gap-closing or an absence audit that adds to phase A's files: list phase B's tasks for that round
and append them to the real work lists.

Usage: python3 -I method/round_tasks.py SUBJECT_DIR COPY_DIR COPY_CHECK_OUT LABEL [--dry]

COPY_DIR is a copy of SUBJECT_DIR (named as the subject, such as .../S-02), checked by `method/check_subject.py` into
COPY_CHECK_OUT. Its work lists are rebuilt there by `method/second_pass_list.py`, and these tasks are appended to
SUBJECT_DIR's lists, each `why` starting with LABEL (such as "Salla and Zid round (28 October, ...): "):
- each `place` task the real lists don't hold yet;
- each `revisit` of a row that names a gap since narrowed or answered (the checker names such rows);
- each other `revisit` whose leads include a statement still unplaced. second_pass_list.py gives no `place` task for a
  statement a revisit takes as its lead, so dropping that revisit would leave the statement with no task.
A revisit already appended in the same round is not appended again: the round is named by LABEL's text before its
first " (", so the script can be run again, with a fuller label, after a later part of the round, such as an audit,
has added statements.
It prints, per root decision, what it appended, and the unplaced statements still without a task."""
import csv, os, re, sys, importlib.util

csv.field_size_limit(10**9)
args = [a for a in sys.argv[1:] if a != "--dry"]
dry = "--dry" in sys.argv
if len(args) != 4:
    sys.exit(__doc__)
real, copy, out, label = args
label = label if label.endswith(" ") else label + " "
name = label.split(" (")[0].strip()          # the round's name, such as "Salla and Zid round": later runs share it
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("spl", os.path.join(here, "second_pass_list.py"))
spl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(spl)
spl.main(copy, out)


def rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


issues = rows(os.path.join(out, "subject-issues.tsv"))
again = {r["id"] for r in issues if r["file"] == "variants.tsv" and
         ("the row names the gap that replaced it" in r["issue"] or "the row gives the answer instead" in r["issue"])}
unplaced = {(r["root_decision"], r["stmt_id"], r["bullet"]) for r in rows(os.path.join(out, "unplaced.tsv"))}


def leads(why):
    """The statements a revisit places or notes: those its `why` lists before the other bullets' statements."""
    m = re.search(r"which this task places or notes:(.*?)(?:A2 statements|$)", why)
    return re.findall(r"S02-[A-Z]{2}-\d+", m.group(1)) if m else []


print("rows naming a narrowed or answered gap:", sorted(again))
for rd in ("RD1", "RD2", "RD3"):
    cw = rows(os.path.join(copy, "b", "second-pass", rd, "worklist.tsv"))
    rp = os.path.join(real, "b", "second-pass", rd, "worklist.tsv")
    rw = rows(rp)
    have = {(t["task"], t["id"], t["bullet"]) for t in rw}
    have_round = {(t["task"], t["id"], t["bullet"]) for t in rw if t["why"].startswith(name)}
    new = []
    for t in cw:
        k = (t["task"], t["id"], t["bullet"])
        if t["task"] == "place" and k not in have:
            new.append(t)
        elif t["task"] == "revisit" and k not in have_round and (
                t["id"] in again or any((rd, s, t["bullet"]) in unplaced for s in leads(t["why"]))):
            new.append(t)
    covered = {t["id"] for t in new + rw if t["task"] == "place"} | \
              {s for t in new + rw if t["task"] == "revisit" for s in leads(t["why"])}
    left = sorted(s for (d, s, b) in unplaced if d == rd and s not in covered)
    if not dry:
        with open(rp, "a", encoding="utf-8") as f:
            for t in new:
                f.write("\t".join([t["task"], t["id"], t["platform"], t["bullet"], t["vp_id"],
                                   (label + t["why"]).strip()]).replace("\n", " ") + "\n")
    print(rd, "would append:" if dry else "appended:",
          sum(1 for t in new if t["task"] == "revisit"), "revisits,", sum(1 for t in new if t["task"] == "place"),
          "places; by platform:", sorted({t["platform"] for t in new}),
          "; unplaced with no task:", left or "none")
