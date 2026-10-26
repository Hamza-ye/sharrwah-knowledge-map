"""Check each quote in a report against the line its pinned citation names.

Usage: python3 -I method/check_report.py reports/S-01-review.md

A pinned citation is a link to this repository, observed-sh or observed-sa at a full commit, such as
https://github.com/Hamza-ye/observed-sh/blob/<commit>/<path>?plain=1#L11 (or #L36-L56). Each quote written
in double quotes since the previous pinned link, in the same line or table cell, must be found in the cited
lines, or anywhere in the file when no line is named. Where pinned links follow one another with no quote
between, as an id and then its held copy, the quote may be in any of them. A quote may skip words with
"..."; each part is looked up. Matching is quote_check.py's: exact, then with markup removed, then ignoring
case and Arabic diacritics.
Prints each quote not found, and the quotes with no pinned citation after them, for a reader to judge (the
founder's own words, a section's name). Exits 1 if any quote is not found.
"""
import os, re, subprocess, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import html_text, variants

SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOTS = {"sharrwah-knowledge-map": SKM,
         "observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
         "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa")}
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
PIN = re.compile(r"https://github\.com/Hamza-ye/([\w-]+)/blob/([0-9a-f]{40})/([^?#)\s]+)(?:\?plain=1)?(?:#L(\d+)(?:-L(\d+))?)?$")
QUOTE = re.compile(r'"([^"]{3,})"')
shown = {}


def show(repo, sha, path):
    if (repo, sha, path) not in shown:
        r = subprocess.run(["git", "-C", ROOTS[repo], "show", f"{sha}:{path}"], capture_output=True)
        shown[repo, sha, path] = None if r.returncode else r.stdout.decode("utf-8", "replace")
    return shown[repo, sha, path]


def held(q, sources):
    for src in sources:
        for (_, qv), (_, sv) in zip(variants(q), variants(src)):
            if qv and qv in sv:
                return True
    return False


def main(report):
    checked, missing, unpinned = 0, [], []

    def settle(quotes, group):
        nonlocal checked
        for q in quotes:
            checked += 1
            parts = [p for p in re.split(r"\s*(?:\.\.\.|…)\s*", q) if p.strip()]
            if not any(sources and all(held(p, sources) for p in parts) for _, sources in group):
                missing.append(f"{'; '.join(w for w, _ in group)}: not found: {q[:80]}")

    for line in open(report, encoding="utf-8").read().split("\n"):
        for cell in (line.split(" | ") if line.startswith("|") else [line]):
            start, quotes, group = 0, [], []
            for m in LINK.finditer(cell):
                pin = PIN.match(m.group(2))
                if not pin or pin.group(1) not in ROOTS:
                    continue
                found = QUOTE.findall(LINK.sub(lambda x: x.group(1), cell[start:m.start()]))
                start = m.end()
                if found:
                    settle(quotes, group)
                    quotes, group = found, []
                if not quotes:
                    continue
                repo, sha, path, a, b = pin.groups()
                path = urllib.parse.unquote(path)
                where = f"{repo}@{sha[:7]}:{path}" + (f" L{a}" + (f"-L{b}" if b else "") if a else "")
                body = show(repo, sha, path)
                if body is None:
                    group.append((f"{where} (no such file)", None))
                    continue
                src = "\n".join(body.split("\n")[int(a) - 1:int(b or a)]) if a else body
                group.append((where, [src, html_text(src)] if path.endswith((".html", ".htm")) else [src]))
            settle(quotes, group)
            rest = LINK.sub(lambda x: x.group(1), cell[start:])
            unpinned += [q[:80] for q in QUOTE.findall(rest)]
    for p in missing:
        print(p)
    print(f"{checked} quotes checked against their pinned lines, {len(missing)} not found")
    if unpinned:
        print(f"{len(unpinned)} quoted words with no pinned citation after them, for a reader to judge:")
        for q in unpinned:
            print("  -", q)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
