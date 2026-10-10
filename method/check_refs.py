"""Check that every citation in a sorted-outcomes file resolves.

Usage: python3 method/check_refs.py SORTED_TSV [--repo DIR] [--observed DIR]

A citation resolves when:
- a repository path with a line exists and has that many lines;
- an observed-sh:/observed-sa: path with a line exists under the observed root;
- a crossing or source id (S###, L###, E###) exists in its list;
- a founder id (F-##, O-##) appears in decisions/founder.md;
- "seam rule N" or "frame rule N" names a rule that exists.
"""
import argparse, csv, os, re, sys

p = argparse.ArgumentParser()
p.add_argument("sorted_tsv")
p.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p.add_argument("--observed", default="/home/user")
a = p.parse_args()

def ids_in(path, col="id"):
    with open(path, encoding="utf-8") as fh:
        return {r[col].strip() for r in csv.DictReader(fh, delimiter="\t")}

R = a.repo
crossings = ids_in(f"{R}/studies/payment-seam/notes/shopify-crossings.tsv") | ids_in(f"{R}/studies/payment-seam/notes/salla-crossings.tsv")
sources = ids_in(f"{R}/evidence/shopify-engineering/finding-aids/20261010-shopify-engineering-sources.tsv")
founder = open(f"{R}/decisions/founder.md", encoding="utf-8").read()
seam_rules = len(re.findall(r"^\d+\. \*\*", open(f"{R}/studies/payment-seam/seam.md", encoding="utf-8").read().split("## Rules added after tagging")[1].split("## Tagging")[0], re.M))
frame_rules = len(re.findall(r"^\d+\. \*\*", open(f"{R}/method/frame.md", encoding="utf-8").read().split("## 3. Rules")[1].split("## 4.")[0], re.M))
line_counts = {}

def lines(path):
    if path not in line_counts:
        with open(path, "rb") as fh:
            line_counts[path] = sum(1 for _ in fh)
    return line_counts[path]

def check(ref):
    ref = ref.strip().strip("`")
    if re.fullmatch(r"[SL]\d{3}", ref):
        return ref in crossings
    if re.fullmatch(r"E\d{3}", ref):
        return ref in sources
    if re.fullmatch(r"[FO]-\d{2}", ref):
        return f"| {ref} |" in founder
    m = re.fullmatch(r"seam rule (\d+)", ref)
    if m:
        return 1 <= int(m.group(1)) <= seam_rules
    m = re.fullmatch(r"frame rule (\d+)", ref)
    if m:
        return 1 <= int(m.group(1)) <= frame_rules
    m = re.fullmatch(r"observed-(sh|sa):(.+?):(\d+)(?:-(\d+))?", ref)
    if m:
        path = os.path.join(a.observed, f"observed-{m.group(1)}", m.group(2))
        last = int(m.group(4) or m.group(3))
        return os.path.isfile(path) and last <= lines(path)
    m = re.fullmatch(r"(.+?):(\d+)(?:-(\d+))?", ref)
    if m:
        path = os.path.join(R, m.group(1))
        last = int(m.group(3) or m.group(2))
        return os.path.isfile(path) and last <= lines(path)
    return False

total, bad, empty = 0, [], []
with open(a.sorted_tsv, encoding="utf-8") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        refs = [x for x in (row.get("references") or "").split(";") if x.strip()]
        if not refs:
            empty.append(row.get("outcome_id", "?"))
        for ref in refs:
            total += 1
            if not check(ref):
                bad.append((row.get("outcome_id", "?"), ref.strip()))

print(f"citations: {total}; resolved: {total - len(bad)}; unresolved: {len(bad)}; outcomes without a citation: {len(empty)}")
print(f"(seam rules found: {seam_rules}; frame rules found: {frame_rules})")
for oid, ref in bad[:200]:
    print(f"  {oid}\t{ref}")
for oid in empty[:50]:
    print(f"  {oid}\t(no citation)")
sys.exit(1 if bad or empty else 0)
