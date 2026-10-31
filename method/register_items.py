"""List the founder items of a subject's phase C that its register doesn't answer, or answers twice.

Usage: python3 -I method/register_items.py SUBJECT_DIR

A founder item is a key of SUBJECT_DIR/c/<root decision>/answers.tsv whose `founder_item` isn't empty, named as
`vp_id|key`. Every row of SUBJECT_DIR/register.tsv names the items it answers, or moves to another subject, in its
`answers_items` column, `;`-separated. Each item must be named by exactly one row. Prints the items no row names, the
items two or more rows name, and the names no item has; exits 1 if any list isn't empty.
"""
import csv, glob, os, sys

csv.field_size_limit(10**9)


def rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def main(subj):
    items = set()
    for p in sorted(glob.glob(os.path.join(subj, "c", "*", "answers.tsv"))):
        items |= {f"{r['vp_id']}|{r['key']}" for r in rows(p) if r.get("founder_item", "").strip()}
    named = {}
    for r in rows(os.path.join(subj, "register.tsv")):
        for x in (r.get("answers_items") or "").split(";"):
            x = x.strip()
            if x:
                named.setdefault(x, []).append(r["id"])
    missing = sorted(items - set(named))
    twice = sorted((x, ids) for x, ids in named.items() if len(ids) > 1 and x in items)
    unknown = sorted(x for x in named if x not in items)
    for x in missing:
        print(f"no row answers {x}")
    for x, ids in twice:
        print(f"{x} is answered by {', '.join(ids)}")
    for x in unknown:
        print(f"{x}: no founder item has this name")
    print(f"{len(items)} founder items; {len(missing)} unanswered, {len(twice)} answered twice, {len(unknown)} names unknown")
    return 1 if missing or twice or unknown else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
