"""Join the files that agents working one root decision each wrote, into the subject's own files.

Usage: python3 -I method/merge_slices.py SUBJECT_DIR PHASE

PHASE is `b` (variation-points.tsv, variants.tsv and notes-b.md) or `c` (analysis.tsv and notes-c.md). The agents
write in SUBJECT_DIR/<PHASE>/<root decision>/; this writes SUBJECT_DIR/<file>, in the order of the root decisions'
names. Each TSV's header must be the same in every folder, and an id may appear in one folder only. Notes are joined
under a heading per root decision. The subject's files are written again each time, from the folders: the folders are
where the agents work, and method/check_subject.py checks the joined files.
"""
import os, sys

FILES = {"b": ["variation-points.tsv", "variants.tsv", "notes-b.md"], "c": ["analysis.tsv", "notes-c.md"]}


def main(subj, phase):
    base = os.path.join(subj, phase)
    rds = sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))) if os.path.isdir(base) else []
    if not rds:
        sys.exit(f"no folders in {base}")
    for name in FILES[phase]:
        parts = [(rd, os.path.join(base, rd, name)) for rd in rds if os.path.exists(os.path.join(base, rd, name))]
        if not parts:
            continue
        out = os.path.join(subj, name)
        if name.endswith(".md"):
            with open(out, "w", encoding="utf-8") as f:
                for rd, p in parts:
                    f.write(f"# {rd}\n\n" + open(p, encoding="utf-8").read().strip() + "\n\n")
            print(f"{name}: {len(parts)} parts")
            continue
        head, body, seen = None, [], {}
        for rd, p in parts:
            lines = [l for l in open(p, encoding="utf-8").read().split("\n") if l.strip()]
            if not lines:
                continue
            if head is None:
                head = lines[0]
            elif lines[0] != head:
                sys.exit(f"{p}: its header differs from the first folder's")
            for l in lines[1:]:
                key = l.split("\t")[0]                 # vp_id or variant_id: one folder's own
                if key in seen:
                    sys.exit(f"{p}: {key} is also in {seen[key]}'s file")
                seen[key] = rd
                body.append(l)
        with open(out, "w", encoding="utf-8") as f:
            f.write(head + "\n" + "".join(l + "\n" for l in body))
        print(f"{name}: {len(body)} rows from {len(parts)} folders")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] not in FILES:
        sys.exit(__doc__)
    main(sys.argv[1].rstrip("/"), sys.argv[2])
