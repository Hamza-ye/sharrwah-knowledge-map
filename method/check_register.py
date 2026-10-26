"""Check every citation in a subject's decision register (studies/subjects/<id>/register.tsv).

Usage: python3 -I method/check_register.py studies/subjects/S-01/register.tsv

It checks that each cited id exists where it says, and that each path cited at a commit is there:
- the subject's statement, variant and variation point ids (S01-SH-019, S01-V-528, S01-VP-01);
- Stage 1's ids (YA-62, YK-203) and the concern map's (SH-C-057);
- observed-sh@<commit>:<path> and observed-sa@<commit>:<path>, with any line a citation names (L11). Where a
  name stands before the line, as "OrderTransaction L2447" or "POST /settlements/instant" after "L64", that
  line must contain it;
- Salla's help articles cited as "record N" (line N + 1 of their texts.jsonl);
- this repository's own paths.
Prints each problem, and exits 1 if there is any.
"""
import csv, os, re, subprocess, sys

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOTS = {"observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
         "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa")}
PLATFORMS = {"SH": "shopify", "SA": "salla", "ZD": "zid", "WC": "woocommerce", "BC": "bigcommerce"}


def first_column(path):
    with open(path, encoding="utf-8") as f:
        return {r[0] for r in csv.reader(f, delimiter="\t") if r}


def show(root, sha, path):
    r = subprocess.run(["git", "-C", root, "show", f"{sha}:{path}"], capture_output=True, text=True)
    return None if r.returncode else r.stdout


def main(reg):
    subj = os.path.dirname(os.path.abspath(reg))
    rows = list(csv.DictReader(open(reg, encoding="utf-8"), delimiter="\t"))
    ids = set()
    for p in PLATFORMS.values():
        f = os.path.join(subj, p, "statements.tsv")
        if os.path.exists(f):
            ids |= first_column(f)
    for f in ("variants.tsv", "analysis.tsv"):
        if os.path.exists(os.path.join(subj, f)):
            ids |= first_column(os.path.join(subj, f))
    for f in ("axes.tsv", "constants.tsv"):
        ids |= first_column(os.path.join(SKM, "studies/yemen-cases", f))
    concerns = set()
    for p in PLATFORMS.values():
        concerns |= first_column(os.path.join(SKM, "studies/concern-map/platforms", p, "concerns.tsv"))
    problems, checked = [], 0
    for r in rows:
        where = r["id"]
        text = " ".join(r[c] for c in ("vp_id", "evidence", "rationale_at"))
        for i in re.findall(r"\bS\d\d-(?:[A-Z]{2}-\d+|V-\d+|VP-\d+)\b|\bY[AK]-\d+\b", text):
            checked += 1
            if i not in ids:
                problems.append(f"{where}: {i} not found")
        for i in re.findall(r"\b(?:SH|SA|ZD|WC|BC)-C-\d+\b", text):
            checked += 1
            if i not in concerns:
                problems.append(f"{where}: concern {i} not found")
        for seg in r["evidence"].split(";"):
            found = list(re.finditer(r"(observed-s[ah])@([0-9a-f]{7,40}):(\S+?)(?=[\s:;,(]|$)", seg))
            for k, m in enumerate(found):
                repo, sha, path = m.groups()
                checked += 1
                body = show(ROOTS[repo], sha, path)
                if body is None:
                    problems.append(f"{where}: {repo}:{path} not at {sha[:8]}")
                    continue
                lines = body.split("\n")
                rest = seg[m.end():found[k + 1].start() if k + 1 < len(found) else len(seg)]
                for lm in re.finditer(r"(?:([A-Za-z][\w/{}]*(?: /[\w/{}]+)?) )?L(\d+)\b(?: ((?:POST|GET|PUT|DELETE) \S+))?", rest):
                    name, n, after = lm.group(1), int(lm.group(2)), lm.group(3)
                    checked += 1
                    if n > len(lines):
                        problems.append(f"{where}: {path} has no line {n}")
                        continue
                    want = after or (name if name and name[0].isupper() else None)
                    if not want:
                        continue
                    line = lines[n - 1]
                    if path.endswith(".jsonl"):
                        # A line of a structure is one item: its own name, or method and path, must be the one cited
                        import json
                        item = json.loads(line)
                        own = item.get("name") or f"{str(item.get('method', '')).upper()} {item.get('path', '')}"
                        if own != want:
                            problems.append(f"{where}: {path} line {n} is {own}, not {want}")
                    elif want not in line:
                        problems.append(f"{where}: {path} line {n} doesn't contain {want}")
                for rm in re.finditer(r"records? (\d+)(?: and (\d+))?", rest):
                    for n in filter(None, rm.groups()):
                        checked += 1
                        if int(n) + 1 > len(lines):
                            problems.append(f"{where}: {path} has no record {n}")
        for path in re.findall(r"\b((?:studies|reports|method|evidence)/[\w./-]+\.\w+|PLAN\.md|founder-decisions\.tsv)", text):
            checked += 1
            if not os.path.exists(os.path.join(SKM, path)):
                problems.append(f"{where}: {path} not in this repository")
    for p in problems:
        print(p)
    print(f"{checked} citations checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
