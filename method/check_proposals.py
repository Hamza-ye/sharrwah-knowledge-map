"""Check the proposals' files mechanically (PLAN.md section 3, the checker).

Usage:
  python3 -I method/check_proposals.py records QUESTION PLATFORM [--dir DIR] [--check] [CAPTURE_RUN ...]
  python3 -I method/check_proposals.py drafts QUESTION [--dir DIR] [--file NAME] [--cited]
  python3 -I method/check_proposals.py decisions FILE

`records` checks one recording run's folder, studies/proposals/records/<QUESTION>/<platform>/ (step R3):
- selection.tsv: each row's action is copy, set aside or add; a set aside or add row gives its reason; every
  candidate concern a fresh `copy_statements.py candidates` run gives is in it;
- the copies (copied.tsv, copied-gaps.tsv and, for Q5, copied-pilot.tsv, copied-pilot-gaps.tsv and
  copied-pilot-absences.tsv): each row, after its first three columns, is its source line unchanged, byte for byte;
  each copy_id names that line; each file holds every row of the concerns chosen, and no other; each row of
  copied-citations.tsv is its source's row unchanged, and every citation the copies cite is there;
- statements.tsv and citations.tsv: their columns; ids of the form Q-XX-001 and Q-XX-C001, each used once; each
  cite_id known; bears_on numbers among the question's sentences (studies/proposals/questions-for-agents.md);
  `from` held or live; each statement found verbatim in its first cited source, and each quote in its own; every
  citation used;
- not-found.tsv: its kinds; a "not in what was read" that names what was read and shows the corpus search; an
  absent that cites its list and the words that make it complete; who_can; no route to the founder for a page that
  is held and readable;
- account.md: each section is headed by a sentence's number, as `## [2]`; each point (a list item or a paragraph)
  cites at least one id, and each id it cites exists in the folder. With --check (a checking run), each point also
  starts with its label: differs, goes beyond, the same or not in what was read.

`drafts` checks one draft proposal, studies/proposals/drafts/<QUESTION>/draft.md (step R4,
studies/proposals/briefs/R4-drafting.md), or another file of that folder with --file:
- its sections, `## 1.` to `## 7.`, and `## 8.` for Q5 and Q7, in order; section 1's subsections, one heading for each
  of the question's sentences, in order, as `### [2]` or `### [1] [2]`;
- every point cites a platform's or Stage 1's record, but for a part in section 4 that names its elements in bold, a
  section 6 point that says only what Yemen's evidence doesn't show, and section 8, where a variation point counts;
  each id exists among the question's records, Stage 1's files, the pilot's variation points or the areas
  (method/record_ids.py); no id is another question's; the pilot's entry, variants and own ids, and paths under
  studies/subjects/, register/ and founder-messages/, are never cited;
- each quoted word (double, single, curly or angled marks, or backticks) and each run of Arabic is found in the text
  of a platform's or Stage 1's record the point cites, its quotes included; no id is quoted;
- a point saying a reading didn't show something cites its not-found row or copied gap, outside section 6 and
  "not checked on" points; "absent", outside quotation marks, rests on an absent not-found row or a pilot absence;
- as warnings: a Yemen fact without its date; the brief's citing limits, with Yemen facts counted by axis or
  constant and place; the length, and section 1's share of it. notes.md must exist. --cited prints what is cited,
  by kind, and section 6's "doesn't show" points, for the checks that follow (step R5).

`decisions` checks the company decisions' evidence (studies/proposals/briefs/R4-company-decisions.md): its decisions,
headed `## D1.` and on; every point cites a record of any question or of Stage 1, but for its "Raised by" and "Bears
on" lines; and the drafts' rules on quoted words, Arabic, Yemen facts' dates, readings that didn't show something and
"absent".

A live source is checked against the capture runs named, and in this repository's capture runs. Before the
coordinator captures it, a quote from it is "pending capture", which doesn't fail. Prints each problem, and exits 1
on any error.
"""
import csv, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources
from source_kinds import kind_of
from held_index import Held, describe, names_a_source, norm_url, urls_in
from copy_statements import COPIES, LEAD, candidates_for, copy_id
from agent_questions import sentences
import record_ids as rid

csv.field_size_limit(10**9)
HERE = os.path.dirname(os.path.abspath(__file__))
SKM = os.path.dirname(HERE)
ROOTS = {"observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
         "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa"),
         "woocommerce-11.2.1": os.environ.get("WOO_RELEASE", "/home/user/woocommerce-release/11.2.1/woocommerce"),
         "sharrwah-knowledge-map": SKM}
CODE = {"shopify": "SH", "salla": "SA", "woocommerce": "WC", "zid": "ZD", "bigcommerce": "BC"}
HEAD = {
    "statements.tsv": ["stmt_id", "bears_on", "identifier", "statement", "scope", "marker", "cite_ids", "from", "note"],
    "citations.tsv": ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"],
    "not-found.tsv": ["nf_id", "bears_on", "what_is_missing", "kind", "read", "searched", "list_cite_ids",
                      "complete_cite_ids", "who_can", "route"],
}
ACCESS = {"md", "raw", "rendered", "local"}
LABELS = ("differs", "goes beyond", "the same", "not in what was read")
KINDS = {"not in what was read", "absent"}
WHO = {"agent", "founder", "either"}
issues = []


def err(f, i, x, level="error"):
    issues.append((level, f, i, x))


def read(path, head=None):
    """(header, [(line, dict)]) of a tab-separated file with no quoting, or (None, []) if it isn't there."""
    if not os.path.exists(path):
        return None, []
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not rows:
        return [], []
    h, out = rows[0], []
    name = os.path.basename(path)
    if head and h != head:
        err(name, "", f"header is {h}, expected {head}")
    for n, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            continue
        if len(row) != len(h):
            err(name, f"line {n}", f"{len(row)} fields, header has {len(h)}")
        out.append((n, {k: (row[i].strip() if i < len(row) else "") for i, k in enumerate(h)}))
    return h, out


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def raw_lines(path):
    """The lines of a file as written: no field stripped, only the line ending removed."""
    with open(path, encoding="utf-8", newline="") as f:
        return [l.rstrip("\n").rstrip("\r") for l in f]


def check_copies(d, q, platform, code):
    _, sel = read(os.path.join(d, "selection.tsv"))
    if not sel:
        err("selection.tsv", "", "missing or empty: run copy_statements.py candidates, then set each action")
        return set()
    keep, listed, pilot = set(), {}, False
    for n, r in sel:
        c = r.get("concern_id")
        if c in listed:
            err("selection.tsv", f"line {n}", f"{c} is listed twice, first at line {listed[c]}")
        listed.setdefault(c, n)
        if r.get("action") not in ("copy", "set aside", "add"):
            err("selection.tsv", f"line {n}", f"action '{r.get('action')}' is not copy, set aside or add")
        if r.get("action") in ("set aside", "add") and not r.get("reason"):
            err("selection.tsv", f"line {n}", f"a '{r['action']}' row needs its reason")
        if r.get("action") in ("copy", "add") and c != "S-01":
            keep.add(c)
        if c == "S-01" and r.get("action") == "copy":
            pilot = True
    for c, _ in candidates_for(q, platform):
        if c not in listed:
            err("selection.tsv", c, "a candidate concern is missing: set it aside with a reason instead of deleting it")
    copy_ids, cited = set(), {}
    for name, (letter, base, fname) in COPIES.items():
        path = os.path.join(d, name)
        from_pilot = name.startswith("copied-pilot")
        if from_pilot and not pilot:
            if os.path.exists(path):
                err(name, "", "the selection doesn't copy S-01: run the copy again")
            continue
        if not os.path.exists(path):
            err(name, "", "missing: run copy_statements.py copy after setting the selection")
            continue
        src_path = os.path.join(base, platform, fname)
        src_rel = os.path.relpath(src_path, SKM)
        src = raw_lines(src_path)
        lines = raw_lines(path)
        head = lines[0].split("\t") if lines else []
        if head != LEAD + src[0].split("\t"):
            err(name, "", f"header isn't {LEAD} and then {src_rel}'s header")
            continue
        got = set()
        for n, raw in enumerate(lines[1:], start=2):
            if not raw.strip():
                continue
            f = raw.split("\t")
            cid = f[0]
            try:
                line = int(f[2])
            except ValueError:
                err(name, cid or f"line {n}", f"source_line '{f[2]}' isn't a line number")
                continue
            if f[1] != src_rel:
                err(name, cid, f"source_file is {f[1]}, not {src_rel}")
            if cid != copy_id(q, platform, letter, line):
                err(name, cid, f"copy_id doesn't name its source line: it is {copy_id(q, platform, letter, line)}")
            if not 2 <= line <= len(src) or "\t".join(f[3:]) != src[line - 1]:
                err(name, cid, f"not unchanged from {src_rel} line {line}")
                continue
            got.add(line)
            copy_ids.add(cid)
            row = dict(zip(head, f))
            if not from_pilot and row["concern_id"] not in keep:
                err(name, cid, f"{row['concern_id']} isn't chosen in selection.tsv")
            for col in ("cite_ids", "list_cite_ids", "complete_cite_ids"):
                for c in ids(row.get(col)):
                    cited.setdefault(os.path.relpath(os.path.join(base, platform, "citations.tsv"), SKM), set()).add(c)
        want = set()
        for n, raw in enumerate(src[1:], start=2):
            if raw.strip() and (from_pilot or raw.split("\t")[0] in keep):
                want.add(n)
        if want - got:
            err(name, "", f"{len(want - got)} rows of the concerns chosen are missing, such as {src_rel} line "
                          f"{min(want - got)}: run the copy again")
    path = os.path.join(d, "copied-citations.tsv")
    if not os.path.exists(path):
        err("copied-citations.tsv", "", "missing: run copy_statements.py copy after setting the selection")
        return copy_ids
    srcs, have = {}, {}
    for n, raw in enumerate(raw_lines(path)[1:], start=2):
        if not raw.strip():
            continue
        f = raw.split("\t")
        if f[0] not in srcs:
            if not os.path.exists(os.path.join(SKM, f[0])):
                err("copied-citations.tsv", f"line {n}", f"source_file {f[0]} doesn't exist")
                continue
            srcs[f[0]] = {l.split("\t")[0]: l for l in raw_lines(os.path.join(SKM, f[0]))[1:] if l.strip()}
        have.setdefault(f[0], set()).add(f[1] if len(f) > 1 else "")
        if srcs[f[0]].get(f[1] if len(f) > 1 else "") != "\t".join(f[1:]):
            err("copied-citations.tsv", f[1] if len(f) > 1 else f"line {n}", "not unchanged from its source's row")
    for sf, cs in cited.items():
        missing = sorted(cs - have.get(sf, set()))
        if missing:
            err("copied-citations.tsv", "", f"{len(missing)} citations the copies cite are missing, such as {missing[0]}")
    return copy_ids


def check_closed(d, q, code, own):
    """not-found-closed.tsv (the re-check against the observed runs): the not-found rows a run closed, each with the
    statements that close it. A closed row is no longer the folder's: nothing may cite it."""
    path = os.path.join(d, "not-found-closed.tsv")
    if not os.path.exists(path):
        return
    _, rows = read(path, HEAD["not-found.tsv"] + ["closed_by"])
    for n, r in rows:
        nid = r["nf_id"]
        if not re.fullmatch(rf"{q}-{code}-N\d{{2,3}}", nid):
            err("not-found-closed.tsv", nid, "nf_id isn't one of this folder's not-found ids")
        if nid in own:
            err("not-found-closed.tsv", nid, "closed, and still in not-found.tsv")
        by = ids(r.get("closed_by", ""))
        if not by:
            err("not-found-closed.tsv", nid, "closed_by names the statements that close it")
        for i in by:
            if i not in own:
                err("not-found-closed.tsv", nid, f"closed_by: {i} is not a statement of this folder")


def check_own(d, q, code, src, held):
    pre = f"{q}-{code}"
    nsent = len(sentences(q))
    _, cits = read(os.path.join(d, "citations.tsv"), HEAD["citations.tsv"])
    _, sts = read(os.path.join(d, "statements.tsv"), HEAD["statements.tsv"])
    _, nfs = read(os.path.join(d, "not-found.tsv"), HEAD["not-found.tsv"])
    cit, used, own = {}, set(), set()
    for n, c in cits:
        cid = c["cite_id"]
        if not re.fullmatch(rf"{pre}-C\d{{3}}", cid):
            err("citations.tsv", cid, f"cite_id isn't of the form {pre}-C001")
        if cid in cit:
            err("citations.tsv", cid, "cite_id used twice")
        cit[cid] = c
    for n, r in sts:
        sid = r["stmt_id"]
        if not re.fullmatch(rf"{pre}-\d{{3}}", sid):
            err("statements.tsv", sid, f"stmt_id isn't of the form {pre}-001")
        if sid in own:
            err("statements.tsv", sid, "stmt_id used twice")
        own.add(sid)
        if not r["bears_on"] or not all(x.isdigit() and 1 <= int(x) <= nsent for x in ids(r["bears_on"])):
            err("statements.tsv", sid, f"bears_on gives the question's sentence numbers, 1 to {nsent}")
        if r["from"] not in ("held", "live"):
            err("statements.tsv", sid, f"from '{r['from']}' is neither held nor live")
        cs = ids(r["cite_ids"])
        if not cs:
            err("statements.tsv", sid, "no citation")
        for c in cs:
            used.add(c)
            if c not in cit:
                err("statements.tsv", sid, f"cite_id {c} not in citations")
        if cs and cs[0] in cit and r["statement"]:
            res, why, _ = src.check_quote(r["statement"], cit[cs[0]]["source"], cit[cs[0]]["locator"])
            if not res.startswith("found"):
                live = re.match(r"^https?://", cit[cs[0]]["source"])
                err("statements.tsv", sid, f"statement not found verbatim in {cs[0]}'s source ({res}{'; ' + why if why else ''})",
                    "pending capture" if res == "unresolved" and live else "error")
        for c in cs:
            if c in cit and kind_of(cit[c]["source"], ROOTS)[0] == "unknown":
                err("statements.tsv", sid, f"{c}'s kind is unknown under method/source_kinds.py", "warning")
    for n, r in nfs:
        nid = r["nf_id"]
        if not re.fullmatch(rf"{pre}-N\d{{2,3}}", nid):
            err("not-found.tsv", nid, f"nf_id isn't of the form {pre}-N01")
        own.add(nid)
        if r["kind"] not in KINDS:
            err("not-found.tsv", nid, f"kind '{r['kind']}' is not one of {sorted(KINDS)}")
        if r["who_can"] not in WHO:
            err("not-found.tsv", nid, f"who_can '{r['who_can']}' is not one of {sorted(WHO)}")
        if not r["bears_on"] or not all(x.isdigit() and 1 <= int(x) <= nsent for x in ids(r["bears_on"])):
            err("not-found.tsv", nid, f"bears_on gives the question's sentence numbers, 1 to {nsent}")
        if not r["read"] or not names_a_source(r["read"]):
            err("not-found.tsv", nid, "read names what was read: held paths at a commit, live URLs with a date")
        if r["kind"] == "not in what was read" and "corpus_search.py" not in r["searched"]:
            err("not-found.tsv", nid, "searched shows the corpus_search.py commands run")
        if r["kind"] == "absent":
            for col, what in (("list_cite_ids", "the list"), ("complete_cite_ids", "the words that make the list complete")):
                cs = ids(r[col])
                if not cs:
                    err("not-found.tsv", nid, f"an absence cites {what} in {col}")
                for c in cs:
                    used.add(c)
                    if c not in cit:
                        err("not-found.tsv", nid, f"{col}: {c} not in citations")
        if r["who_can"] in ("founder", "either"):
            for u in urls_in(r["route"]):
                if norm_url(u).split("?")[0].endswith("/") or "/" not in norm_url(u):
                    continue                    # a bare host names a site, not the page to capture
                hits = [h for h in held.lookup(u) if h["readable"]]
                if hits:
                    err("not-found.tsv", nid, f"{u} is held at {describe(hits[0])}: read it instead of routing it to the founder")
    for cid, c in cit.items():
        if c["access_path"] not in ACCESS:
            err("citations.tsv", cid, f"access_path '{c['access_path']}' is not one of {sorted(ACCESS)}")
        if re.match(r"^(observed-sh|observed-sa)(?!@[0-9a-f]{7,40}:)", c["source"]):
            err("citations.tsv", cid, "a local source names its repository at a commit")
        if "..." in c["quote"] or "…" in c["quote"]:
            err("citations.tsv", cid, "a quote has no ellipses")
        if len(c["quote"]) > 300:
            err("citations.tsv", cid, "a quote is at most 300 characters")
        for col in ("locator", "source_date", "date_basis", "accessed"):
            if not c[col]:
                err("citations.tsv", cid, f"{col} is empty")
        if cid not in used:
            err("citations.tsv", cid, "not used by any statement or absence", "warning")
        res, why, _ = src.check_quote(c["quote"], c["source"], c["locator"]) if c["quote"] and c["source"] else ("unresolved", "no quote or source", "")
        if not res.startswith("found"):
            live = re.match(r"^https?://", c["source"])
            err("citations.tsv", cid, f"quote {res}{'; ' + why if why else ''}",
                "pending capture" if res == "unresolved" and live else "error")
    return own


def decisions(path):
    """The company decisions' evidence (studies/proposals/briefs/R4-company-decisions.md): its decisions headed
    `## D1.` and on, in order, and nothing but a title and a line before the first; every point cites a record that
    exists and that a draft cites, but for the "Raised by" and "Bears on" lines and a point naming a draft's line of
    what Yemen's evidence doesn't show (as Q4:150); quoted words and Arabic are found in the records the point cites;
    a Yemen fact gives its state, place and date as the digest does; a reading that didn't show something cites its
    not-found row or gap; "absent" rests on an absent row; and every point of the drafts' sections 7 is raised by a
    decision or named in notes.md."""
    from r5_cards import digest_entries, part_matches, cited as cited_by_draft
    name = os.path.relpath(path, SKM)
    text = open(path, encoding="utf-8").read()
    entries = digest_entries()
    drafts_cite, sec7 = set(), set()
    for q in [f"Q{n}" for n in range(1, 9)]:
        ids, _ = cited_by_draft(q, "draft.md")
        drafts_cite.update(ids)
        for i, uses in ids.items():
            sec7.update(f"{q}:{n}" for sec, n, _ in uses if sec == 7)
    want, first = 1, None
    for n, line in enumerate(text.splitlines(), start=1):
        m = re.match(r"^## D(\d+)\.\s+\S", line)
        if re.match(r"^##(?!#)", line):
            if not m or int(m.group(1)) != want:
                err(name, f"line {n}", f"a decision is headed as ## D{want}. followed by its question")
            want += 1
            first = first or n
    if want == 1:
        err(name, "", "no decision headed ## D1.")
    raised = set()
    for n, p in points(text):
        if first is None or n < first:
            continue                        # the title and the line saying what the file is
        if re.match(r"^[-*]?\s*\*\*Raised by:?\*\*", p):
            for q, ln in re.findall(r"\b(Q[1-8])\s*\((?:line|lines)\s*([\d, and]+)\)", p):
                raised.update(f"{q}:{x}" for x in re.findall(r"\d+", ln))
            raised.update(re.findall(r"\bQ[1-8]:\d+\b", p))
            continue
        if re.match(r"^[-*]?\s*\*\*Bears on:?\*\*", p):
            continue
        pids, yids, vids, aids = draft_ids(p)
        for i in pids + yids:
            if not rid.lookup(i):
                err(name, f"line {n}", f"{i}: no such record")
            elif i not in drafts_cite:
                err(name, f"line {n}", f"{i}: no draft cites it")
        records = [i for i in pids + yids if rid.lookup(i)]
        plain = unquoted(p)
        if not records:
            if re.search(r"\bQ[1-8]:\d+\b", p) and DOESNT_SHOW.search(plain):
                continue                    # a draft's point of what Yemen's evidence doesn't show, by its line
            err(name, f"line {n}", "a point that cites no record")
            continue
        texts = [rid.text_of(i) for i in records]
        for m in QUOTED.finditer(p):
            raw = next(g for g in m.groups() if g is not None)
            words = rid.norm(raw)
            if len(words) < 2:
                continue
            if rid.PLATFORM_ID.fullmatch(raw.strip()) or rid.YEMEN_ID.fullmatch(raw.strip()):
                err(name, f"line {n}", f"an id in quotation marks: {raw}")
            elif not any(words in t for t in texts if t):
                err(name, f"line {n}", f"quoted words not found in the records the point cites: {words[:80]}")
        for m in ARABIC.finditer(p):
            run = rid.norm(m.group(0)).strip("\u060c\u061b\u061f\u066a\u06d4 ")
            if ARABIC_LETTER.search(run) and not any(run in t for t in texts if t):
                err(name, f"line {n}", f"Arabic not found in the records the point cites: {run[:60]}")
        if NOT_SHOWN.search(plain) and not any(re.search(r"-(?:[GH]\d{4}|N\d{2,3})$", i) for i in pids):
            err(name, f"line {n}", "a point saying a reading didn't show something cites its not-found row or copied gap")
        if re.search(r"\babsent\b", plain, re.I) and pids:
            if not any(re.search(r"-A\d{4}$", i) or (re.search(r"-N\d+$", i) and rid.lookup(i) and
                       rid.lookup(i)[1].get("kind") == "absent") for i in pids):
                err(name, f"line {n}", "'absent' without an absent row or a pilot absence")
        for i in yids:
            if not re.match(r"^Y[AK]-", i):
                continue
            m = next((m for m in YEMEN_FACT.finditer(p) if m.group(1) == i and m.group(2)), None)
            if not m:
                err(name, f"line {n}", f"{i}: a Yemen fact without its state, place and date, as (state @ place, as of date)")
                continue
            ok, why = part_matches(i, m.group(2), entries)
            if not ok:
                err(name, f"line {n}", f"{i}: {why}")
    notes_path = os.path.join(os.path.dirname(path), "notes.md")
    notes = open(notes_path, encoding="utf-8").read() if os.path.exists(notes_path) else ""
    if not notes:
        err("notes.md", "", "missing")
    named = set(re.findall(r"\bQ[1-8]:\d+\b", notes))
    for q, ln in re.findall(r"\b(Q[1-8])\s*\((?:line|lines)\s*([\d, and]+)\)", notes):
        named.update(f"{q}:{x}" for x in re.findall(r"\d+", ln))
    for x in sorted(sec7 - raised - named, key=lambda s: (s[:2], int(s.split(":")[1]))):
        err(name, "", f"{x}: a point of a draft's section 7 that no decision raises and notes.md doesn't name")


def points(text):
    """(line, text) of each point of an account: each list item, with its continuation lines, and each paragraph.
    Headings and blank lines separate points."""
    out, cur = [], None
    for n, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#") or re.match(r"^\s*\*\*[^*]+\*\*:?\s*$", line):
            cur = None                  # a heading, or a line that is only a bold subheading, is no point
            continue
        if re.match(r"^\s*([-*]|\d+[.)])\s+\S", line) or cur is None:
            cur = [n, line.strip()]
            out.append(cur)
        else:
            cur[1] += " " + line.strip()
    return [tuple(p) for p in out]


def check_account(d, q, code, known, checking=False, nf_ids=()):
    path = os.path.join(d, "account.md")
    if not os.path.exists(path):
        err("account.md", "", "missing")
        return
    text = open(path, encoding="utf-8").read()
    pat = re.compile(rf"\b{q}-{code}-(?:[KPGHA]\d{{4}}|N\d{{2,3}}|\d{{3}})\b")
    any_id = re.compile(rf"\b{q}-[A-Z]{{2}}-(?:[KPGHA]\d{{4}}|N\d{{2,3}}|C\d{{3}}|\d{{3}})\b")   # any platform's
    for c in sorted(set(pat.findall(text)) - known):
        err("account.md", c, "cites an id the folder doesn't hold")
    nsent = len(sentences(q))
    seen, first_section = [], None
    for n, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^##(?!#)", line):     # a section; ### subheadings within it are free
            m = re.match(r"^## \[(\d+)\]\s*$", line)
            if not m or not 1 <= int(m.group(1)) <= nsent:
                err("account.md", f"line {n}", f"a section is headed by one sentence's number, from [1] to [{nsent}], as ## [2]")
            elif checking:
                k = int(m.group(1))
                if seen and k <= seen[-1]:
                    err("account.md", f"line {n}", f"section [{k}] comes after [{seen[-1]}]: one section per sentence, in order")
                seen.append(k)
            first_section = first_section or n
        elif checking and re.match(r"^#+\s*\[\d+\]", line):
            err("account.md", f"line {n}", "a sentence's section is headed as ## [n], at the second level")
    cited_nf = set()
    for n, p in points(text):
        if not pat.search(p):
            err("account.md", f"line {n}", "a point that cites no id of this folder")
        cited_nf.update(x for x in pat.findall(p) if re.search(r"-N\d+$", x))
        if checking:
            m = re.match(r"^([-*]|\d+[.)])?\s*\**(" + "|".join(LABELS) + r")\b", p)
            if not m:
                err("account.md", f"line {n}", f"a point starts with its label: {', '.join(LABELS)}")
            elif m.group(2) == "not in what was read" and not re.search(rf"\b{q}-{code}-(?:[GH]\d{{4}}|N\d{{2,3}})\b", p):
                err("account.md", f"line {n}", "a 'not in what was read' point cites its not-found row or copied gap")
            if first_section is None or n < first_section:
                err("account.md", f"line {n}", "a point before the first section")
    if checking:
        for nid in sorted(set(nf_ids) - cited_nf):
            err("account.md", nid, "a not-found row that no point cites")
    words = len(re.findall(r"\w+", any_id.sub("", text)))     # ids, of any platform, aren't words
    if words > (1800 if checking else 2300):    # with the re-check against the observed runs (19 October 2026)
        err("account.md", "", f"{words} words, past the brief's length", "warning")


def records(q, platform, captures, d=None, checking=False):
    code = CODE[platform]
    d = d or os.path.join(SKM, "studies", "proposals", "records", q, platform)
    if not os.path.isdir(d):
        sys.exit(f"no folder {os.path.relpath(d, SKM)}")
    caps = list(captures) + sorted(glob.glob(os.path.join(SKM, "evidence/product-class/runs/*")))
    src = Sources(ROOTS, caps)
    held = Held(ROOTS, caps)
    copies = check_copies(d, q, platform, code)
    own = check_own(d, q, code, src, held)
    check_closed(d, q, code, own)
    check_account(d, q, code, copies | own, checking, {x for x in own if re.search(r"-N\d+$", x)})


LIMITS = {"Q5": (60, 10, 12, 3, 7000)}            # facts, not-found and absent, Yemen facts, doesn't show, words
DEFAULT_LIMITS = (40, 7, 8, 2, 5000)
QUOTED = re.compile(r'"([^"\n]+)"|\u201c([^\u201d\n]+)\u201d|\u00ab([^\u00bb\n]+)\u00bb|`([^`\n]+)`'
                    r"|(?<![\w'])'([^'\n]{3,}?)'(?![\w])|\u2018([^\u2019\n]{3,}?)\u2019(?![\w])")
ARABIC = re.compile(r"[\u0600-\u06ff\u0750-\u077f\ufb50-\ufdff\ufe70-\ufeff]+"
                    r"(?:[ \u200c\u200e\u200f]+[\u0600-\u06ff\u0750-\u077f\ufb50-\ufdff\ufe70-\ufeff]+)*")
ARABIC_LETTER = re.compile(r"[\u0621-\u064a\u066e-\u06d3\u06fa-\u06ff\u0750-\u077f\ufb50-\ufdff\ufe70-\ufeff]")
NOT_SHOWN = re.compile(r"not in what was read|didn.t show|did not show|not shown|wasn.t shown|was not shown|"
                       r"wasn.t found|was not found|weren.t found|were not found", re.I)
DOESNT_SHOW = re.compile(r"doesn.t show|does not show", re.I)
FORBIDDEN = re.compile(r"\bS01-(?!VP-)[A-Z0-9]+(?:-[A-Z0-9]+)*\b|(?:studies/subjects/|register/|founder-messages/)\S*")
YEMEN_FACT = re.compile(r"\b(Y[AK]-\d{2,3})\b(?:\s*\(((?:[^()]|\([^()]*\))*)\))?")   # a place may hold its own brackets
DATE = re.compile(r"\b(?:19|20)\d\d(?:-\d\d){0,2}\b")


def draft_ids(text):
    return (rid.PLATFORM_ID.findall(text), rid.YEMEN_ID.findall(text), rid.VP_ID.findall(text),
            rid.AREA_ID.findall(text))


def unquoted(p):
    return QUOTED.sub(" ", p)


def drafts(q, d=None, name="draft.md", cited=False):
    d = d or os.path.join(SKM, "studies", "proposals", "drafts", q)
    path = os.path.join(d, name)
    if not os.path.exists(path):
        sys.exit(f"no file {os.path.relpath(path, SKM)}")
    if not os.path.exists(os.path.join(d, "notes.md")):
        err("notes.md", "", "missing")
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    nsent = len(sentences(q))
    want = list(range(1, 9 if q in ("Q5", "Q7") else 8))
    heads, seen_sent = [], []
    for n, line in enumerate(lines, start=1):
        if re.match(r"^##(?!#)", line):
            m = re.match(r"^## (\d+)\.\s+\S", line)
            if not m:
                err(name, f"line {n}", "a section is headed by its number, as ## 2. Proposed: ...")
                continue
            heads.append((int(m.group(1)), n))
        elif re.match(r"^###(?!#)", line) and heads and heads[-1][0] == 1:
            ks = [int(x) for x in re.findall(r"\[(\d+)\]", line)]
            if not ks or any(not 1 <= k <= nsent for k in ks):
                err(name, f"line {n}", f"a subsection of section 1 is headed by sentence numbers, from [1] to [{nsent}]")
            seen_sent += ks
    if [h for h, _ in heads] != want:
        err(name, "", f"sections {[h for h, _ in heads]}: want {want}, in order, each headed as ## 1. ... at level 2")
    if seen_sent != list(range(1, nsent + 1)):
        err(name, "", f"section 1's subsections give sentences {seen_sent}: want each of 1 to {nsent} once, in order")

    def section(n):
        k = 0
        for h, at in heads:
            if at <= n:
                k = h
        return k

    plat, facts_y, doesnt_show = set(), set(), []
    for n, p in points(text):
        sec = section(n)
        if sec == 0:
            err(name, f"line {n}", "a point before the first section")
            continue
        for m in FORBIDDEN.finditer(p):
            err(name, f"line {n}", f"{m.group(0)}: the pilot's entry, variants, pilot ids and these paths are never cited")
        pids, yids, vids, aids = draft_ids(p)
        for i in pids:
            if not i.startswith(q + "-"):
                err(name, f"line {n}", f"{i}: an id of another question")
            elif not rid.lookup(i):
                err(name, f"line {n}", f"{i}: no such record")
        for i in yids + vids + aids:
            if not rid.lookup(i):
                err(name, f"line {n}", f"{i}: no such id")
        records = [i for i in pids + yids if i.startswith(("Q", "Y")) and rid.lookup(i)
                   and (not i.startswith("Q") or i.startswith(q + "-"))]
        plain = unquoted(p)
        says_not_shown = sec == 6 and DOESNT_SHOW.search(plain)
        if says_not_shown:
            doesnt_show.append(n)
        has_id = bool(pids or yids or (sec == 8 and vids))
        if not has_id:
            if sec == 4:
                if not re.search(r"\*\*[^*]+\*\*", p):
                    err(name, f"line {n}", "a part with no id names, in bold, the elements of sections 2 and 3 it builds on")
            elif says_not_shown:
                if re.search(r"\b(allows?|forbids?)\b", plain, re.I):
                    err(name, f"line {n}", "a point that says what Yemen's evidence allows or forbids cites the fact")
            else:
                err(name, f"line {n}", "a point that cites no record")
        texts = [rid.text_of(i) for i in records]
        for m in QUOTED.finditer(p):
            raw = next(g for g in m.groups() if g is not None)
            words = rid.norm(raw)
            if len(words) < 2:
                continue
            if rid.PLATFORM_ID.fullmatch(raw.strip()) or rid.YEMEN_ID.fullmatch(raw.strip()) \
                    or rid.VP_ID.fullmatch(raw.strip()) or rid.AREA_ID.fullmatch(raw.strip()):
                err(name, f"line {n}", f"an id in quotation marks: {raw}")
                continue
            if not any(words in t for t in texts if t):
                err(name, f"line {n}", f"quoted words not found in the records the point cites: {words[:80]}")
        for m in ARABIC.finditer(p):
            run = rid.norm(m.group(0)).strip("\u060c\u061b\u061f\u066a\u06d4 ")
            if not ARABIC_LETTER.search(run):
                continue
            if not any(run in t for t in texts if t):
                err(name, f"line {n}", f"Arabic not found in the records the point cites: {run[:60]}")
        if NOT_SHOWN.search(plain) and sec != 6 and not re.search(r"not checked on", plain, re.I):
            if not any(re.search(r"-(?:[GH]\d{4}|N\d{2,3})$", i) for i in pids):
                err(name, f"line {n}", "a point saying a reading didn't show something cites its not-found row or copied gap")
        if re.search(r"\babsent\b", plain, re.I) and pids:
            ok = any(re.search(r"-A\d{4}$", i) or (re.search(r"-N\d+$", i) and
                     (rid.lookup(i)[1].get("kind") == "absent")) for i in pids if rid.lookup(i))
            if not ok:
                err(name, f"line {n}", "'absent' without an absent row or a pilot absence")
        for m in YEMEN_FACT.finditer(p):
            if not DATE.search(m.group(2) or p[m.end():m.end() + 80]):
                err(name, f"line {n}", f"{m.group(1)}: a Yemen fact without its date", "warning")
            place = re.split(r"[,;]", (m.group(2) or "").split("@", 1)[1])[0].strip() if "@" in (m.group(2) or "") else ""
            if rid.lookup(m.group(1)):
                facts_y.add((m.group(1), place))
        plat.update(i for i in pids if i.startswith(q + "-") and rid.lookup(i))

    facts = sorted(i for i in plat if re.search(r"-(?:[KP]\d{4}|C\d{3}|\d{3})$", i))
    nf = sorted(i for i in plat if re.search(r"-(?:[GHA]\d{4}|N\d{2,3})$", i))
    yem_ids = sorted({i for i, _ in facts_y} | {i for i in rid.YEMEN_ID.findall(text) if i.startswith(("YQ", "YE"))})
    lim = LIMITS.get(q, DEFAULT_LIMITS)
    for label, got, cap in [("statements, copies and citations", facts, lim[0]),
                            ("not-found rows, copied gaps and pilot absences", nf, lim[1]),
                            ("Yemen facts (an axis or constant at one place)", sorted(facts_y), lim[2]),
                            ("\"Yemen's evidence doesn't show\" points", doesnt_show, lim[3])]:
        if len(got) > cap:                    # a guide, not a limit (the founder, 19 October 2026)
            err(name, "", f"{len(got)} {label} cited, past the guide's about {cap}: say in notes.md for what", "note")
    strip = lambda t: rid.AREA_ID.sub("", rid.VP_ID.sub("", rid.YEMEN_ID.sub("", rid.PLATFORM_ID.sub("", t))))
    words = len(re.findall(r"\w+", strip(text)))
    if words > lim[4] * 1.1:
        err(name, "", f"{words} words, past the brief's about {lim[4]}", "warning")
    one = [at for h, at in heads if h == 1]
    two = [at for h, at in heads if h == 2]
    if one and two and words:
        w1 = len(re.findall(r"\w+", strip("\n".join(lines[one[0]:two[0] - 1]))))
        if w1 > 0.55 * words:
            err(name, "", f"section 1 is {w1} of {words} words, past about half", "warning")
    if cited:
        print(f"facts\t{len(facts)}\t{' '.join(facts)}")
        print(f"not found or absent\t{len(nf)}\t{' '.join(nf)}")
        print(f"Yemen facts\t{len(facts_y)}\t" + "; ".join(f"{i} @ {pl}" if pl else i for i, pl in sorted(facts_y)))
        print(f"Stage 1 ids\t{len(yem_ids)}\t{' '.join(yem_ids)}")
        print(f"doesn't show (section 6 lines)\t{len(doesnt_show)}\t{' '.join(map(str, doesnt_show))}")
        print(f"words\t{words}")


def main(argv):
    if len(argv) >= 2 and argv[0] == "drafts":
        rest, d, name = argv[2:], None, "draft.md"
        for flag in ("--dir", "--file"):
            if flag in rest:
                i = rest.index(flag)
                if flag == "--dir":
                    d = rest[i + 1]
                else:
                    name = rest[i + 1]
                del rest[i:i + 2]
        drafts(argv[1], d, name, "--cited" in rest)
    elif len(argv) == 2 and argv[0] == "decisions":
        decisions(argv[1])
    elif len(argv) >= 3 and argv[0] == "records":
        rest, d = argv[3:], None
        if "--dir" in rest:
            i = rest.index("--dir")
            d = rest[i + 1]
            del rest[i:i + 2]
        checking = "--check" in rest
        rest = [x for x in rest if x != "--check"]
        records(argv[1], argv[2], rest, d, checking)
    else:
        sys.exit("usage: check_proposals.py records QUESTION PLATFORM [--dir DIR] [--check] [CAPTURE_RUN ...]\n"
                 "       check_proposals.py drafts QUESTION [--dir DIR] [--file NAME] [--cited]\n"
                 "       check_proposals.py decisions FILE")
    levels = {}
    for level, f, i, x in issues:
        levels[level] = levels.get(level, 0) + 1
        print(f"{level}\t{f}\t{i}\t{x}")
    print("; ".join(f"{k}: {v}" for k, v in sorted(levels.items())) or "no issues")
    return 1 if levels.get("error") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
