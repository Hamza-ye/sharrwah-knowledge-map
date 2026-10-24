# Joins Stage 1's step 2b files (studies/yemen-cases/brief.md) for the build:
#   1. adds to places.tsv each place a step 2b agent added in pass2/places-<k>.tsv and places.tsv doesn't list;
#   2. joins pass2/states-<k>.tsv into states.tsv, taking each row's place to the place places.tsv groups it with,
#      through every link where groupings chain.
# It is idempotent. Run it once after step 2b, so that step 2c can group variants among the added places, and
# again after step 2c, so that the rows follow those groupings. It refuses a states file whose header differs,
# a row given twice, or groupings that form a cycle.
#
# Usage: python3 -I method/join_pass2.py STUDY_DIR
import csv, glob, os, sys

PLACES = ["place", "grouped", "kind", "why", "basis", "note"]
STATES = ["condition_id", "group_id", "label", "place", "holds", "now", "note"]

def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    return (rows[0] if rows else []), [r for r in rows[1:] if any(c.strip() for c in r)]

def write(path, head, rows):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(head) + "\n")
        for r in rows:
            f.write("\t".join(r) + "\n")

def main(study):
    problems = []
    head, places = read(os.path.join(study, "places.tsv"))
    if head != PLACES:
        sys.exit(f"places.tsv: header {head}, expected {PLACES}")
    listed = {r[0] for r in places}
    added = 0
    for path in sorted(glob.glob(os.path.join(study, "pass2", "places-*.tsv"))):
        h, rows = read(path)
        if h != PLACES:
            problems.append(f"{path}: header {h}")
            continue
        for r in rows:
            if r[0] not in listed:
                places.append(r)
                listed.add(r[0])
                added += 1
    grouped = {r[0]: r[1] for r in places if r[0] != "across Yemen"}   # a state's across Yemen is never regrouped
    states, seen = [], set()
    for path in sorted(glob.glob(os.path.join(study, "pass2", "states-*.tsv"))):
        h, rows = read(path)
        if h != STATES:
            problems.append(f"{path}: header {h}")
            continue
        for r in rows:
            if r[0] in seen:
                problems.append(f"{path}: {r[0]} is given twice")
            seen.add(r[0])
            place, passed = r[3], set()
            while grouped.get(place, place) != place:   # follow groupings to the place grouped with itself
                if place in passed:
                    problems.append(f"places.tsv: the groupings from {r[3]} form a cycle")
                    break
                passed.add(place)
                place = grouped[place]
            states.append(r[:3] + [place] + r[4:])
    if problems:
        sys.exit("not joined:\n  " + "\n  ".join(problems[:50]))
    write(os.path.join(study, "places.tsv"), PLACES, places)
    write(os.path.join(study, "states.tsv"), STATES, states)
    print(f"places.tsv: {added} places added from step 2b; states.tsv: {len(states)} rows")

if __name__ == "__main__":
    main(sys.argv[1].rstrip("/"))
