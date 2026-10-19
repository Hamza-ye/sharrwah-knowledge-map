"""Look up the ids a proposal cites (steps R4 and R5), with the text each stands for.

Usage: python3 -I method/record_ids.py [--all] ID [ID ...]

An id is one of:
- a record's, in studies/proposals/records/<question>/<platform>/: a statement (Q5-SA-001), a citation
  (Q5-SA-C001), a not-found row (Q5-SA-N01), or a copy (copy_statements.py): K a concern map statement, G its gap,
  P a pilot statement, H a pilot gap, A a pilot absence (Q5-SA-K0059);
- Stage 1's, in studies/yemen-cases/: an axis (YA-01), a constant (YK-01), a condition (YQ-B005) or a citation
  (YE-A001);
- a pilot variation point (S01-VP-01), in studies/subjects/S-01/variation-points.tsv;
- an area of the areas list (A-01), in studies/proposals/areas/areas.tsv: the coordinator's grouping, never
  evidence of what a platform does.

For each id it prints the file it is in and its row, then the citations it rests on, each with its source,
locator, date and quote: the first 12, or every one with --all. `texts(question)` gives, for the drafts' checks, each id's own text and its quotes.
"""
import csv, html, os, re, sys, unicodedata
from functools import lru_cache
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_statements import COPIES, cite_split

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORDS = os.path.join(SKM, "studies", "proposals", "records")
STAGE1 = os.path.join(SKM, "studies", "yemen-cases")
VPS = os.path.join(SKM, "studies", "subjects", "S-01", "variation-points.tsv")
AREAS = os.path.join(SKM, "studies", "proposals", "areas", "areas.tsv")

PLATFORM_ID = re.compile(r"\bQ\d-[A-Z]{2}-(?:[KPGHA]\d{4}|N\d{2,3}|C\d{3}|\d{3})\b")
YEMEN_ID = re.compile(r"\bY[AK]-\d{2,3}\b|\bY[QE]-[A-Z]\d{3,4}\b")
VP_ID = re.compile(r"\bS01-VP-\d{2}\b")
AREA_ID = re.compile(r"(?<![\w-])A-\d{2}\b")
# the fields of each file that hold its own words; a citation's quote is added from its citations
OWN = {
    "statements.tsv": ["identifier", "statement", "scope"],
    "citations.tsv": ["quote"],
    "not-found.tsv": ["what_is_missing"],
    "copied.tsv": ["identifier", "statement", "scope"],
    "copied-gaps.tsv": ["what_would_show_it", "means"],
    "copied-pilot.tsv": ["identifier", "statement", "scope", "conditions"],
    "copied-pilot-gaps.tsv": ["what_is_missing"],
    "copied-pilot-absences.tsv": ["what_is_absent"],
}
CITES = {"statements.tsv": "cite_ids", "copied.tsv": "cite_ids", "copied-pilot.tsv": "cite_ids",
         "copied-pilot-absences.tsv": "list_cite_ids", "not-found.tsv": "list_cite_ids"}


def read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


@lru_cache(maxsize=None)
def platform_rows(question):
    """{id: (file, row, own text, [citation rows])} for every record of the question, on every platform."""
    out = {}
    qdir = os.path.join(RECORDS, question)
    for platform in sorted(os.listdir(qdir)) if os.path.isdir(qdir) else []:
        d = os.path.join(qdir, platform)
        cits = {r["cite_id"]: r for r in read(os.path.join(d, "citations.tsv"))}
        copied_cits = {r["cite_id"]: r for r in read(os.path.join(d, "copied-citations.tsv"))}
        for name, key in [("statements.tsv", "stmt_id"), ("citations.tsv", "cite_id"), ("not-found.tsv", "nf_id")] + \
                         [(n, "copy_id") for n in COPIES]:
            pool = copied_cits if name.startswith("copied") else cits
            for r in read(os.path.join(d, name)):
                rid = r.get(key, "")
                if not rid:
                    continue
                own = " ".join(r.get(f) or "" for f in OWN[name])
                rests = [pool[c] for c in cite_split(r.get(CITES.get(name, ""), "")) if c in pool]
                if name == "not-found.tsv":
                    rests += [pool[c] for c in cite_split(r.get("complete_cite_ids", "")) if c in pool]
                out[rid] = (os.path.relpath(os.path.join(d, name), SKM), r, own, rests)
    return out


@lru_cache(maxsize=None)
def stage1_rows():
    """{id: (file, row, own text, [citation rows])} for Stage 1's axes, constants, conditions and citations."""
    cits = {r["cite_id"]: r for r in read(os.path.join(STAGE1, "citations.tsv"))}
    out = {}
    for name, key, fields, cite_cols in [
            ("axes.tsv", "axis_id", ["axis", "what_varies", "states", "today", "note"], ["today_cite_ids"]),
            ("constants.tsv", "constant_id", ["condition", "state", "place", "note"], ["cite_ids"]),
            ("conditions.tsv", "condition_id", ["condition", "state", "place", "held_at", "note"], ["cite_ids"]),
            ("citations.tsv", "cite_id", ["quote"], [])]:
        for r in read(os.path.join(STAGE1, name)):
            own = " ".join(r.get(f) or "" for f in fields)
            rests = [cits[c] for col in cite_cols for c in cite_split(r.get(col, "")) if c in cits]
            if name == "axes.tsv":      # every state's citations, written after it in `states`
                rests += [cits[c] for c in re.findall(r"\bYE-[A-Z]\d{3,4}\b", r.get("states", "")) if c in cits]
            out[r[key]] = (os.path.relpath(os.path.join(STAGE1, name), SKM), r, own, rests)
    return out


@lru_cache(maxsize=None)
def other_rows():
    out = {}
    for r in read(VPS):
        out[r["vp_id"]] = (os.path.relpath(VPS, SKM), r, " ".join(r.values()), [])
    for r in read(AREAS):
        out[r["area_id"]] = (os.path.relpath(AREAS, SKM), r, " ".join(r.get(f) or "" for f in
                             ["heading", "plain_line", "platform_area_ids"]), [])
    return out


def lookup(i):
    m = re.match(r"^(Q\d)-", i)
    if m:
        return platform_rows(m.group(1)).get(i)
    if YEMEN_ID.fullmatch(i):
        return stage1_rows().get(i)
    return other_rows().get(i)


def norm(s):
    """Text as the checks compare it: entities decoded, tags and markdown emphasis removed, Unicode composed (NFC, so
    that marks on one letter compare in any order), quotes and dashes made plain, whitespace collapsed, Latin letters in
    lower case."""
    s = unicodedata.normalize("NFC", html.unescape(re.sub(r"<[^>]+>", " ", s or "")))
    s = s.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-",
                                   "—": "-", " ": " ", "ـ": ""}))
    s = re.sub(r"[*_]{1,2}", "", s)
    return " ".join(s.split()).lower()


def text_of(i):
    """An id's own words with every quote it rests on, normalized; None for an unknown id."""
    hit = lookup(i)
    if not hit:
        return None
    _, _, own, rests = hit
    return norm(" ".join([own] + [c.get("quote", "") for c in rests]))


def show(i, cap=12):
    hit = lookup(i)
    if not hit:
        return f"{i}: not found"
    path, row, _, rests = hit
    lines = [f"{i}  ({path})"]
    for k, v in row.items():
        if v and k not in ("copy_id", "source_file", "source_line"):
            lines.append(f"  {k}: {v}")
    for c in rests[:cap]:
        lines.append(f"  cites {c.get('cite_id')}: {c.get('source')} | {c.get('locator')} | "
                     f"{c.get('source_date')} | {c.get('quote')}")
    if cap is not None and len(rests) > cap:
        lines.append(f"  ... and {len(rests) - cap} more citations (--all prints every one)")
    return "\n".join(lines)


def main(argv):
    every = "--all" in argv
    argv = [a for a in argv if a != "--all"]
    if not argv:
        sys.exit(__doc__)
    print("\n\n".join(show(i, None if every else 12) for i in argv))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
