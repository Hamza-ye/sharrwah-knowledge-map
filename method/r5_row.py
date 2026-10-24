"""Append one row to a file of step R5's checks (studies/proposals/briefs/R5-checks.md), writing its header first
if the file is new. Tabs and line breaks inside a field become spaces.

Usage: python3 -I method/r5_row.py FILE --id ID --verdict VERDICT [--lines "Q4:9 Q4:12"] [--what TEXT] [--fix TEXT]
                                   [--read TEXT]
"""
import os, sys

COLUMNS = ["id", "verdict", "lines", "what", "fix", "read"]


def main(argv):
    if not argv or argv[0].startswith("--"):
        sys.exit(__doc__)
    path, vals, i = argv[0], {}, 1
    while i < len(argv):
        key = argv[i][2:] if argv[i].startswith("--") else ""
        if key not in COLUMNS or i + 1 >= len(argv):
            sys.exit(f"unknown or empty option {argv[i]}\n" + __doc__)
        vals[key] = argv[i + 1]
        i += 2
    if not vals.get("id") or not vals.get("verdict"):
        sys.exit("--id and --verdict are needed\n" + __doc__)
    new = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", encoding="utf-8") as f:
        if new:
            f.write("\t".join(COLUMNS) + "\n")
        f.write("\t".join(" ".join(vals.get(c, "").split()) for c in COLUMNS) + "\n")
    print(f"{vals['id']}: {vals['verdict']}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
