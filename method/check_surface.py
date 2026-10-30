"""Search the working files for the framings of the work that is now history (PLAN.md, risk 14).

Usage: python3 -I method/check_surface.py

The work done between G1 and the reset of 25 October 2026 is outside the working files, at the commit HISTORY.md
names. This check searches every working file except evidence/ (raw captures) for the terms that work used, and
fails where one appears outside the places allowed to name it:
- HISTORY.md and reports/, which name history by design, and this script, which names the terms;
- founder-messages/, the founder's messages saved verbatim, which are bases and may name anything;
- a link pinned to a commit, which is a deliberate way into history (it is removed before the search);
- an evidence run's id, such as 20261019T003516Z-proposals-Q6-zid: the runs that work captured are evidence like any
  other (CLAUDE.md), so naming one names evidence, not a framing (it is removed before the search);
- the platforms' own words, captured before G1 (PLATFORM_DATA below);
- the pairs in ALLOWED below, each with its reason. A path ending in "/" allows the term in every file under it.

Prints each hit outside those places, and each allowance in ALLOWED that no longer matches anything, and exits 1 if
there is either: an unused allowance would let the term back in unnoticed.
"""
import re, subprocess, sys

TERMS = {
    "the re-frame": r"\bre-?fram",
    "the method of 24 October": r"METHOD\.md|\b[Aa]mendments? [1-4]\b|\b[Aa]mendment 4[a-f]\b",
    "the obligation model": r"\bobligation model\b|(?<![\w-])model/",
    "the payment seam": r"\bseam\b",
    "the re-frame's folder": r"studies/proposals|\bproposals folder\b",
    "the decision records": r"\bD-00\d\b|\bdecisions/",
    "the glossary": r"\bglossary\b|12-glossary",
    "the areas list": r"\b34 areas\b|\bareas list\b|(?<![\w-])areas\.tsv",
    "the Yemen setup options": r"yemen-setup-options|\bsetup options\b",
    "the milestone reports": r"(?<![\w-])M[0-8]\b",
    "the re-frame's questions": r"\bQ[4-8]\b|drafts?/Q\d",
    "the risk register": r"risks\.tsv",
    "the Knowledge Map": r"Knowledge Map|km-questions|(?<![\w./-])register/",
    "scripts now in history": r"slice_coverage|decision_status|km_select|record_ids|yemen_digest|copy_statements|inventory_quotes|r5_cards|check_r5",
}
# Terms matched whatever their case; the rest are matched as written ("Knowledge Map", not this repository's name).
CASE_FREE = {"the re-frame", "the payment seam", "the glossary", "the Yemen setup options", "the obligation model"}
NAMES_HISTORY = re.compile(r"^(HISTORY\.md|reports/|founder-messages/|method/check_surface\.py$)")
# The platforms' own words, captured and quoted before G1 and unchanged since (Q1's map: its platform folders, quote
# checks and side-by-side map; and the pilot's records per platform): their terms ("glossary", "amendment 1", "M1") are
# the platforms', not the history's. The rest of Q1's folder, written by the coordinator, is searched.
PLATFORM_DATA = re.compile(r"^studies/(concern-map/(platforms|checks|map)/|subjects/S-01/(shopify|salla|zid|woocommerce|bigcommerce)/)")
# (file, term): why it may appear there
ALLOWED = {
    ("PLAN.md", "the re-frame"): "G1's three choices, and the reset's own record (Stage 2's note, section 5, section 11)",
    ("PLAN.md", "the areas list"): "Stage 5's cross-check, which names the list by a pinned link",
    ("PLAN.md", "the Knowledge Map"): "the class's model's seed and the kinds (Stage 4A, section 6), and Q3's rows, agreed at G0",
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
    ("studies/subjects/S-01/briefs/E-rows.md", "the Knowledge Map"): "Q3's brief, reading the rows at the commit PLAN.md links",
    ("studies/class-model/", "the Knowledge Map"): "the class's model's seed, the Knowledge Map's index (PLAN.md, Stage 4A)",
    ("studies/class-model/inspection-A.md", "the areas list"): "the first brief's proposed merged file, studies/class-model/areas.tsv, not the history's list",
    ("STATE.md", "the Knowledge Map"): "the founder's decisions of 30 October: the architecture plan's sources graded by its source types, and its page rebuilt from the model at GM",
    ("studies/class-model/inspection-B.md", "the obligation model"): "the re-inspection's name for its test model directory, `model/`, in the inspector's scratchpad",
    ("studies/subjects/S-02/notes-register.md", "the re-frame"): "the register's note that decisions.md was recast under the founder's intent of 29 October",
    ("studies/subjects/S-02/notes-register.md", "the milestone reports"): "the register's short names for its moved rows, S02-M1 to S02-M8",
    ("studies/subjects/S-02/shopify/notes.md", "the milestone reports"): "the Shopify part's names for its two searches, M1 and M2",
    ("studies/subjects/S-02/shopify/statements.tsv", "the milestone reports"): "the Shopify part's names for its two searches, M1 and M2, and Shopify's own store list (\"M8 My Store 8\"), quoted",
    ("studies/subjects/S-02/shopify/citations.tsv", "the milestone reports"): "Shopify's own store list (\"M8 My Store 8\"), quoted",
    ("studies/subjects/S-02/slices/RD1/statements.tsv", "the milestone reports"): "Shopify's own store list (\"M8 My Store 8\"), quoted",
    ("studies/subjects/S-02/zid/notes.md", "the re-frame's questions"): "the Zid part's short name for a held run, 20261019T052111Z-proposals-Q8-zid",
}
PINNED = re.compile(r"https://github\.com/Hamza-ye/[\w.-]+/(?:blob|tree)/[0-9a-f]{40}/[^\s)\]>|]*")
RUN_ID = re.compile(r"\b\d{8}T\d{6}Z-[\w.-]+")


def allowance(f, term):
    """The ALLOWED key that lets term appear in file f, or None."""
    for key in ALLOWED:
        path, t = key
        if t == term and (f == path or (path.endswith("/") and f.startswith(path))):
            return key
    return None


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
            line = RUN_ID.sub("<run>", PINNED.sub("<pinned link>", line))
            for term, pattern in TERMS.items():
                if re.search(pattern, line, re.I if term in CASE_FREE else 0):
                    key = allowance(f, term)
                    if key:
                        allowed_seen.add(key)
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
