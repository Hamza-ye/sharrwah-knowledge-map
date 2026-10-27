"""Join the files that agents working one root decision each wrote, into the subject's own files.

Usage: python3 -I method/merge_slices.py SUBJECT_DIR PHASE

PHASE is `b` (variation-points.tsv, variants.tsv and notes-b.md) or `c` (analysis.tsv and notes-c.md). The agents
write in SUBJECT_DIR/<PHASE>/<root decision>/; this writes SUBJECT_DIR/<file>, in the order of the root decisions'
names. Each TSV's header must be the same in every folder, and an id may appear in one folder only. Notes are joined
under a heading per root decision. The subject's files are written again each time, from the folders: the folders are
where the agents work, and method/check_subject.py checks the joined files.

If SUBJECT_DIR/<PHASE>/ranges.tsv exists (`root_decision`, `vp_from`, `vp_to`, `variant_from`, `variant_to`, `cap`),
each folder's ids must fall in its root decision's ranges, its variation points must take a question's bullet (role
`ask`) of that root decision in SUBJECT_DIR/bullets.tsv, and it may hold at most `cap` variation points. Any problem is listed, and nothing
is written.
"""
import csv, os, re, sys

FILES = {"b": ["variation-points.tsv", "variants.tsv", "notes-b.md"], "c": ["analysis.tsv", "notes-c.md"]}


def table(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        r = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    return [dict(zip(r[0], x)) for x in r[1:] if any(c.strip() for c in x)] if r else []


def number(i):
    m = re.search(r"(\d+)$", i)
    return int(m.group(1)) if m else -1


def checks(subj, base, rds):
    """Problems with each folder's ids, bullets and count, against ranges.tsv and bullets.tsv."""
    ranges = {r["root_decision"]: r for r in table(os.path.join(base, "ranges.tsv"))}
    if not ranges:
        return []
    bullets = {}
    for b in table(os.path.join(subj, "bullets.tsv")):
        if b.get("role") != "ask":                   # a variation point takes a question's bullet
            continue
        for rd in (x.strip() for x in b["root_decision"].split(";") if x.strip()):
            bullets.setdefault(rd, set()).add(b["bullet"])
    out = []
    for rd in rds:
        r = ranges.get(rd)
        if not r:
            out.append(f"{rd}: no row in ranges.tsv")
            continue
        vps = table(os.path.join(base, rd, "variation-points.tsv"))
        if len(vps) > int(r["cap"]):
            out.append(f"{rd}: {len(vps)} variation points, past its cap of {r['cap']}: stop and report")
        for v in vps:
            if not int(r["vp_from"]) <= number(v["vp_id"]) <= int(r["vp_to"]):
                out.append(f"{rd}: {v['vp_id']} is outside its range {r['vp_from']} to {r['vp_to']}")
            if v.get("bullet") not in bullets.get(rd, set()):
                out.append(f"{rd}: {v['vp_id']} takes bullet '{v.get('bullet')}', not one of "
                           f"{''.join(sorted(bullets.get(rd, set())))}")
        for x in table(os.path.join(base, rd, "variants.tsv")):
            if not int(r["variant_from"]) <= number(x["variant_id"]) <= int(r["variant_to"]):
                out.append(f"{rd}: {x['variant_id']} is outside its range {r['variant_from']} to {r['variant_to']}")
    return out


def main(subj, phase):
    base = os.path.join(subj, phase)
    # b/second-pass/ holds the coordinator's work lists for phase B's second pass, not a root decision's files
    rds = sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and d != "second-pass") \
        if os.path.isdir(base) else []
    if not rds:
        sys.exit(f"no folders in {base}")
    problems = checks(subj, base, rds)
    if problems:
        print("\n".join(problems))
        sys.exit(f"{len(problems)} problems: nothing joined")
    out = {}                                           # every file is joined first, and written only if all join
    for name in FILES[phase]:
        parts = [(rd, os.path.join(base, rd, name)) for rd in rds if os.path.exists(os.path.join(base, rd, name))]
        if not parts:
            continue
        if name.endswith(".md"):
            out[name] = ("".join(f"# {rd}\n\n" + open(p, encoding="utf-8").read().strip() + "\n\n" for rd, p in parts),
                         f"{len(parts)} parts")
            continue
        head, body, seen = None, [], {}
        for rd, p in parts:
            lines = [l for l in open(p, encoding="utf-8").read().split("\n") if l.strip()]
            if not lines:
                continue
            if head is None:
                head = lines[0]
            elif lines[0] != head:
                sys.exit(f"{p}: its header differs from the first folder's: nothing joined")
            for l in lines[1:]:
                key = l.split("\t")[0]                 # vp_id or variant_id: one folder's own
                if key in seen:
                    sys.exit(f"{p}: {key} is also in {seen[key]}'s file: nothing joined")
                seen[key] = rd
                body.append(l)
        out[name] = (head + "\n" + "".join(l + "\n" for l in body), f"{len(body)} rows from {len(parts)} folders")
    for name, (text, said) in out.items():
        with open(os.path.join(subj, name), "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{name}: {said}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] not in FILES:
        sys.exit(__doc__)
    main(sys.argv[1].rstrip("/"), sys.argv[2])
