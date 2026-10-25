"""Search the working files for the framings of the work that is now history (PLAN.md, risk 14).

Usage: python3 -I method/check_surface.py

The work done between G1 and the reset of 25 October 2026 is outside the working files, at the commit HISTORY.md
names. This check searches every working file except evidence/ (raw captures) for the terms that work used, and
fails where one appears outside the places allowed to name it:
- HISTORY.md and reports/, which name history by design, and this script, which names the terms;
- a link pinned to a commit, which is a deliberate way into history (it is removed before the search);
- the platforms' own words, captured before G1 (PLATFORM_DATA below);
- the pairs in ALLOWED below, each with its reason.

Prints each hit outside those places, and each allowance in ALLOWED that no longer matches anything, and exits 1 if
there is either: an unused allowance would let the term back in unnoticed.
"""
import re, subprocess, sys

TERMS = {
    "the re-frame": r"\bre-?fram",
    "the method of 24 October": r"METHOD\.md|\b[Aa]mendments? [1-4]\b|\b[Aa]mendment 4[a-f]\b",
    "the obligation model": r"\bobligation model\b|\bmodel/",
    "the payment seam": r"\bseam\b",
    "the re-frame's folder": r"studies/proposals|\bproposals folder\b",
    "the decision records": r"\bD-00\d\b|\bdecisions/",
    "the glossary": r"\bglossary\b|12-glossary",
    "the areas list": r"\b34 areas\b|\bareas list\b|areas\.tsv",
    "the Yemen setup options": r"yemen-setup-options|\bsetup options\b",
    "the milestone reports": r"\bM[0-8]\b",
    "the re-frame's questions": r"\bQ[4-8]\b|drafts?/Q\d",
    "the risk register": r"risks\.tsv",
    "the Knowledge Map": r"Knowledge Map|km-questions|\bregister/",
    "scripts now in history": r"slice_coverage|decision_status|km_select|record_ids|yemen_digest|copy_statements|inventory_quotes|r5_cards|check_r5",
}
# Terms matched whatever their case; the rest are matched as written ("Knowledge Map", not this repository's name).
CASE_FREE = {"the re-frame", "the payment seam", "the glossary", "the Yemen setup options", "the obligation model"}
NAMES_HISTORY = re.compile(r"^(HISTORY\.md|reports/|method/check_surface\.py$)")
# The platforms' own words, captured and quoted before G1 and unchanged since (Q1's map, and the pilot's records
# per platform): their terms ("glossary", "amendment 1", "M1") are the platforms', not the history's.
PLATFORM_DATA = re.compile(r"^studies/(concern-map/|subjects/S-01/(shopify|salla|zid|woocommerce|bigcommerce)/)")
# (file, term): why it may appear there
ALLOWED = {
    ("PLAN.md", "the re-frame"): "G1's three choices, and the reset's own record (Stage 2's note, section 5, section 11)",
    ("PLAN.md", "the areas list"): "Stage 5's cross-check, which names the list by a pinned link",
    ("PLAN.md", "the Knowledge Map"): "Q3's rows, agreed at G0 and read once at close-out",
    ("founder-decisions.tsv", "the re-frame"): "the reset decision names what it ends",
    ("studies/subjects/S-01/method-report.md", "the re-frame"): "G1's three choices, as the pilot put them",
    ("questions/Q3-placing-rows.md", "the Knowledge Map"): "Q3's rows, agreed at G0",
    ("founder-decisions.tsv", "the Knowledge Map"): "the G0 decision on Q3's rows",
    ("questions/Q1-concern-map.md", "the obligation model"): "Q1's list of paths not to open",
    ("questions/Q1-concern-map.md", "the Yemen setup options"): "Q1's list of paths not to open",
    ("questions/Q1-concern-map.md", "the Knowledge Map"): "Q1's list of paths not to open",
    ("questions/Q2-yemen-stress-test.md", "the obligation model"): "Q2's list of paths not to read",
    ("questions/Q2-yemen-stress-test.md", "the Yemen setup options"): "Q2's list of paths not to read",
    ("questions/Q2-yemen-stress-test.md", "the Knowledge Map"): "Q2's list of paths not to read",
    ("studies/subjects/S-01/briefs/A-one-platform.md", "the obligation model"): "the brief's list of paths its agents must not read",
    ("studies/subjects/S-01/briefs/A-one-platform.md", "the Yemen setup options"): "the brief's list of paths its agents must not read",
    ("studies/subjects/S-01/briefs/A-one-platform.md", "the Knowledge Map"): "the brief's list of paths its agents must not read",
    ("studies/yemen-cases/brief.md", "the obligation model"): "Stage 1's list of paths its agents must not read",
    ("studies/yemen-cases/brief.md", "the Yemen setup options"): "Stage 1's list of paths its agents must not read",
    ("studies/yemen-cases/brief.md", "the Knowledge Map"): "Stage 1's list of paths its agents must not read",
    ("studies/subjects/S-01/briefs/E-rows.md", "the Knowledge Map"): "Q3's brief, run once at close-out, reading the rows at the commit PLAN.md links",
}
PINNED = re.compile(r"https://github\.com/Hamza-ye/[\w.-]+/(?:blob|tree)/[0-9a-f]{40}/[^\s)\]>|]*")


def files():
    out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                         capture_output=True, text=True, check=True).stdout.split("\n")
    return [f for f in out if f and not f.startswith("evidence/") and not f.startswith('"evidence/')]


def main():
    hits, allowed_seen = [], set()
    for f in files():
        if NAMES_HISTORY.match(f) or PLATFORM_DATA.match(f):
            continue
        try:
            text = open(f, encoding="utf-8").read()
        except (UnicodeDecodeError, FileNotFoundError, IsADirectoryError):
            continue
        for n, line in enumerate(text.split("\n"), 1):
            line = PINNED.sub("<pinned link>", line)
            for term, pattern in TERMS.items():
                if re.search(pattern, line, re.I if term in CASE_FREE else 0):
                    if (f, term) in ALLOWED:
                        allowed_seen.add((f, term))
                        continue
                    hits.append((f, n, term, line.strip()[:160]))
    for f, n, term, line in hits:
        print(f"{f}:{n}: {term}: {line}")
    unused = sorted(set(ALLOWED) - allowed_seen)
    print(f"\n{len(hits)} hit(s) outside the allowed places; {len(allowed_seen)} allowed pair(s) seen:")
    for f, term in sorted(allowed_seen):
        print(f"  {f}: {term} ({ALLOWED[(f, term)]})")
    for f, term in unused:
        print(f"unused allowance: {f}: {term}")
    return 1 if hits or unused else 0


if __name__ == "__main__":
    sys.exit(main())
