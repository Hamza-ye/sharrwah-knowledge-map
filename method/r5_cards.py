"""Cards for step R5's checks (PLAN.md section 4, step R5; studies/proposals/briefs/R5-checks.md): for each record a
proposal cites, what it rests on, with each quote in its source's context, so that a checking run reads one file and
opens a source only where the card doesn't settle a check.

Usage: python3 -I method/r5_cards.py [QUESTION ...] [--file NAME] [--out DIR] [--quotes TSV] [--uncited TSV]

Reads studies/proposals/drafts/<QUESTION>/<NAME> (draft.md by default; all eight questions when none is named) and
writes, in DIR (studies/proposals/checks/R5/cards by default):
- <QUESTION>-<platform>.md, or -1.md, -2.md and on where the cards pass about 100 KB: a card for each statement, copy
  and pilot copy the file cites on that platform. A copy that an earlier question's file already carries gets a short
  card that names it: its record is checked there, and only this proposal's points here;
- claims-<platform>.md, or in parts of at most 9 cards: a card for each not-found row, copied gap and pilot absence
  cited on that platform, across the questions, a copy's repeats under its first id;
- yemen.md, or yemen-1.md and on in parts of about 150 KB: a card for each of Stage 1's ids cited, across the
  questions;
- doesnt-show.md: a card for each point of a section 6 that says what Yemen's evidence doesn't show, as Q4:146.

A fact's card gives where the proposal cites it; the record's fields; and for each citation its source, locator,
date and kind (`method/source_kinds.py`), its quote, whether the script finds the quote in the source
(`method/quote_check.py`), and the quote in its context: the source's title, the headings above the quote, the text
around it with the quote between ⟪ and ⟫ (narrower where a record has many citations), and, for a page of help or
docs, its opening and its note boxes, once a card. For a
step of an observed run: the step's intent, address, title and time from the run's `actions.jsonl`, and the paths of
the step's files. A claim's card labels each citation as the list or the words that make it complete. A Yemen card
gives the digest's entry, whether each cited part matches it as written, the record with its states one line each,
its conditions without their citations, the cited place's group in `places.tsv`, and in full the citations of the
cited parts and of every state at the same place or at "place not stated".

With --quotes, it also writes TSV: every quote each cited record rests on, checked by script against its source
(the plan's "every quote is checked by script"). With --uncited, every record of the questions no proposal cites,
for the coordinator to record as read.

The context is the source's text as the quote check normalizes it (whitespace joined, entities decoded), so a table
or a list reads as one line. A card decides nothing: the checking run does.
"""
import csv, json, os, re, subprocess, sys
from collections import OrderedDict, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import record_ids as rid
from check_proposals import points, unquoted, DOESNT_SHOW, YEMEN_FACT, ROOTS
from quote_check import Sources, variants, html_text, json_unescaped
from source_kinds import kind_of
from runs_corpus import STEP, HTML_TEXT

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS = os.path.join(SKM, "studies", "proposals", "drafts")
RECORDS = os.path.join(SKM, "studies", "proposals", "records")
DIGEST = os.path.join(SKM, "studies", "proposals", "yemen-digest.md")
PLACES = os.path.join(SKM, "studies", "yemen-cases", "places.tsv")
OUT = os.path.join(SKM, "studies", "proposals", "checks", "R5", "cards")
CAPTURES = os.path.join(SKM, "evidence", "product-class", "runs")
PLATFORMS = {"SH": "shopify", "SA": "salla", "ZD": "zid", "WC": "woocommerce", "BC": "bigcommerce"}
FACT = re.compile(r"-(?:[KP]\d{4}|C\d{3}|\d{3})$")
CLAIM = re.compile(r"-(?:[GHA]\d{4}|N\d{2,3})$")
WIDTH = 450          # characters of context on each side of a quote
LEAD = 500           # characters of a help or docs page's opening
FACT_PART = 100_000  # bytes of fact cards in one file
YEMEN_PART = 150_000
CLAIMS_PART = 9      # claim cards in one file
FIELD_CAP = 1500     # a record's long working fields are cut here; its statement and scope never are
MARKUP = re.compile(r"[<>{}\\]|&\w+;")


def norm_place(s):
    return " ".join((s or "").replace("’", "'").replace("‘", "'").split()).lower().strip(" .")


def sections(text):
    """{line: section number} for each line of a draft."""
    out, sec = {}, 0
    for n, line in enumerate(text.splitlines(), start=1):
        m = re.match(r"^## (\d+)\.", line)
        if m:
            sec = int(m.group(1))
        out[n] = sec
    return out


def cited(q, name):
    """({id: [(section, line, point)]} for every id the draft cites, in order of first citation;
    [(line, point)] for each section 6 point that says what Yemen's evidence doesn't show)."""
    text = open(os.path.join(DRAFTS, q, name), encoding="utf-8").read()
    sec = sections(text)
    out, doesnt = OrderedDict(), []
    for n, p in points(text):
        if sec.get(n) == 6 and DOESNT_SHOW.search(unquoted(p)):
            doesnt.append((n, p))
        for i in dict.fromkeys(rid.PLATFORM_ID.findall(p) + rid.YEMEN_ID.findall(p)):
            if i.startswith("Q") and not i.startswith(q + "-"):
                continue
            out.setdefault(i, []).append((sec.get(n, 0), n, p))
    return out, doesnt


def origin(row):
    """A copy's origin, (file, line), the same for its copies in every question; None for a record of its own."""
    return (row.get("source_file"), row.get("source_line")) if row.get("source_file") else None


class Context:
    """The quote in its source, each source read once."""

    def __init__(self):
        caps = sorted(os.path.join(CAPTURES, d) for d in os.listdir(CAPTURES)) if os.path.isdir(CAPTURES) else []
        self.src = Sources(ROOTS, caps)
        self.raw, self.actions, self.trees = {}, {}, {}

    def raw_texts(self, source, locator):
        key = (source, locator if source.endswith(".warc.gz") else "")
        if key not in self.raw:
            if re.match(r"^https?://", source):
                self.raw[key] = self.src.web_texts(source)[0] or []
            else:
                self.raw[key] = self.src.local_texts(source, locator)[0] or []
        return self.raw[key]

    def captures(self, source):
        """Each capture of a live address: its text file in this repository, with when it was fetched."""
        if not re.match(r"^https?://", source or ""):
            return []
        key = source.split("#")[0]
        if key not in self.src.manifest:
            base = key[:-3] if key.endswith(".md") else key.rstrip("/")
            key = next((k for k in (base, base + ".md", base + "/") if k in self.src.manifest), key)
        out = []
        for cap, r in self.src.manifest.get(key, []):
            d = os.path.join(cap, r.get("dir", ""))
            names = [n for n in (r.get("text_file"), r.get("primary_file")) if n]
            files = []
            for n in dict.fromkeys(names):
                f = os.path.join(d, n)
                size = os.path.getsize(f) if os.path.isfile(f) else 0
                files.append(f"`{os.path.relpath(f, SKM)}` ({size} bytes)")
                if size >= 500:
                    break                   # a text file that holds the page; else its raw file too
            out.append(", ".join(files) + f", fetched {r.get('fetched_at', '')}, {r.get('result', '')}")
        return out

    def git(self, repo, *args):
        return subprocess.run(["git", "-C", ROOTS[repo], *args], capture_output=True).stdout.decode("utf-8", "replace")

    def step(self, source):
        """(the step's row of its run's actions.jsonl, the paths of the step's files at the repository's HEAD), for a
        step file of an observed run; else (None, [])."""
        m = re.match(r"^(observed-s[ha])(?:@([0-9a-f]{6,40}))?:(.+)$", source)
        if not m:
            return None, []
        repo, commit, rel = m.group(1), m.group(2) or "HEAD", m.group(3).strip().lstrip("/")
        s = STEP.match(rel) or HTML_TEXT.match(rel)
        if not s:
            return None, []
        run, num = s.group(1), s.group(2)
        key = (repo, commit, run)
        if key not in self.actions:
            rows = {}
            for line in self.git(repo, "show", f"{commit}:raw/runs/{run}/actions.jsonl").splitlines():
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if isinstance(r, dict) and "step" in r:
                    rows[r["step"]] = r
            self.actions[key] = rows
        if (repo, run) not in self.trees:
            head = self.git(repo, "rev-parse", "--short=9", "HEAD").strip()
            names = self.git(repo, "ls-tree", "--name-only", "HEAD", f"raw/runs/{run}/steps/").splitlines()
            names += self.git(repo, "ls-tree", "--name-only", "HEAD", f"derived/step-text-from-html/{run}/").splitlines()
            self.trees[(repo, run)] = (head, names)
        head, names = self.trees[(repo, run)]
        files = [f"{repo}@{head}:{n}" for n in names if os.path.basename(n).split(".")[0] == num
                 and not n.endswith((".png", ".jpg", ".jpeg", ".webp"))]
        return self.actions[key].get(int(num)), files

    @staticmethod
    def title(raw):
        m = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw)
        if m:
            return " ".join(m.group(1).split())[:200]
        m = re.search(r"(?m)^title:\s*[\"']?(.+?)[\"']?\s*$", raw[:3000])
        if m:
            return m.group(1)[:200]
        m = re.search(r"(?m)^#\s+(.+)$", raw[:20000])
        return m.group(1).strip()[:200] if m else ""

    @staticmethod
    def headings(raw, quote):
        """The markdown headings above the quote's first words, outermost first."""
        if not re.search(r"(?m)^#{1,6}\s", raw) or raw.lstrip().startswith(("{", "[")):
            return []
        probe = " ".join(variants(quote)[2][1].split()[:6])
        lines = raw.splitlines()
        at_ = next((i for i, l in enumerate(lines) if probe and probe in variants(l)[2][1]), None)
        if at_ is None:
            return []
        path, level = [], 7
        for line in reversed(lines[:at_ + 1]):
            m = re.match(r"^(#{1,6})\s+(.*)", line)
            if m and len(m.group(1)) < level:
                path.append(m.group(2).strip())
                level = len(m.group(1))
                if level == 1:
                    break
        return path[::-1]

    @staticmethod
    def opening(source, raws):
        """A help or docs page's opening after its title, and its note boxes, where a page may limit what follows
        (such as to a plan)."""
        if not raws or not re.search(r"\.md$|/manual/|/docs/|help\.|/article/", source):
            return "", []
        raw = raws[0]
        body = re.sub(r"(?s)^---\n.*?\n---\n", "", raw)
        body = re.sub(r"(?m)^#\s+.*$", "", body, count=1)
        lead = variants(html_text(body))[1][1][:LEAD]
        notes = []
        for m in re.finditer(r"(?is)<aside[^>]*>(.*?)</aside>", raw):
            t = variants(html_text(m.group(1)))[1][1]
            if t and t[:300] not in notes:
                notes.append(t[:300])
            if len(notes) == 3:
                break
        return lead, notes

    def around(self, source, locator, quote, width=WIDTH):
        """(title, headings, excerpt): the quote with the text around it, at the first level of matching that finds
        it, from the cleanest of the source's texts that hold it (the fewest marks of markup around it)."""
        raws = self.raw_texts(source, locator)
        title = next((t for t in (self.title(r) for r in raws) if t), "")
        texts, _ = self.src.texts(source, locator)
        ln = re.search(r"\bline (\d+)\b", locator or "")
        if ln and raws and re.search(r"\.(jsonl|tsv)$", source):     # one article or row a line: that line only
            rows = raws[0].splitlines()
            k = int(ln.group(1))
            if 0 < k <= len(rows):
                one = [v for t in (rows[k - 1], json_unescaped(rows[k - 1])) for v in variants(t)]
                if any(q and q in t for (kind, q) in variants(quote) for (tk, t) in one if tk == kind):
                    texts = one                     # the cited line holds it: show it there, nowhere else
        for level, (kind, q) in enumerate(variants(quote)):
            if not q:
                continue
            found = []
            for tkind, t in texts or []:
                k = t.find(q) if tkind == kind else -1
                if k < 0:
                    continue
                a, b = max(0, k - width), min(len(t), k + len(q) + width)
                excerpt = ("…" if a else "") + t[a:k] + "⟪" + t[k:k + len(q)] + "⟫" + t[k + len(q):b] + \
                          ("…" if b < len(t) else "")
                found.append((len(MARKUP.findall(excerpt)), excerpt))
            if found:
                excerpt = min(found)[1]
                heads = next((h for h in (self.headings(r, quote) for r in raws) if h), [])
                return title, heads, excerpt + ("" if level == 0 else f"  (matched {kind})")
        return title, [], ""


def field_lines(row):
    out = []
    for k, v in row.items():
        if not v or k in ("copy_id", "source_file", "source_line"):
            continue
        if k not in ("statement", "scope", "what_is_missing", "what_is_absent") and len(v) > FIELD_CAP:
            v = v[:FIELD_CAP] + f" … ({len(v)} characters; `record_ids.py --all` prints it whole)"
        out.append(f"- {k}: {v}")
    return out


def at(sec, n):
    return f"{sec}, line {n}" if isinstance(sec, str) else f"section {sec}, line {n}"


def where(uses):
    return "**Cited at:** " + "; ".join(at(sec, n) for sec, n, _ in uses)


def point_list(items, label=""):
    """Each point the cards name, once, in order: the cards name points by their line."""
    seen = OrderedDict()
    for _, uses in items:
        for sec, n, p in uses:
            seen.setdefault((str(sec).split(",")[0] if label else "", n), (sec, p))
    out = ["## The points cited", ""]
    for (_, n), (sec, p) in sorted(seen.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        out.append(f"- **{at(sec, n)}:** {p}")
    return "\n".join(out) + "\n\n## The cards\n\n"


def citation_lines(c, ctx, label="", shown=None, width=WIDTH):
    source, locator, quote = c.get("source", ""), c.get("locator", ""), c.get("quote", "")
    kind = kind_of(source, ROOTS, locator)[0] if source else ""
    found = ctx.src.check_quote(quote, source, locator)[0] if source and quote else "no quote"
    lines = ["", f"**Citation {c.get('cite_id')}{label}:** `{source}` | {locator} | {c.get('source_date', '')} | "
                 f"kind: {kind} | quote check: {found}"]
    for cap in ctx.captures(source):
        lines.append(f"- captured: {cap}")
    st, files = ctx.step(source) if source else (None, [])
    if st:
        lines.append(f"- step {st.get('step')}: {st.get('intent')} | {st.get('url')} | \"{st.get('title')}\" | "
                     f"{st.get('t_start')}")
    if files:
        lines.append("- the step's files: " + ", ".join(f"`{f}`" for f in files))
    lines.append(f"- quote: {quote}")
    if source and quote:
        title, heads, excerpt = ctx.around(source, locator, quote, width)
        if shown is None or (source, locator) not in shown:     # a source's title, opening and notes once a card
            lead, notes = ctx.opening(source, ctx.raw_texts(source, locator))
            if title:
                lines.append(f"- title: {title}")
            if lead:
                lines.append(f"- the page opens: {lead}…")
            for t in notes:
                lines.append(f"- a note box: {t}")
            if shown is not None:
                shown.add((source, locator))
        else:
            lines.append("- title, opening and note boxes: as for this source's citation above")
        if heads:
            lines.append(f"- headings: {' > '.join(heads)}")
        lines.append(f"- in context: {excerpt}" if excerpt else "- in context: (the quote was not found in the source's text)")
    return lines


def fact_card(i, uses, ctx, first_seen, part_name, register=False):
    hit = rid.lookup(i)
    if not hit:
        return f"### {i}\n\n{where(uses)}\n\nNo such record.\n"
    path, row, _, rests = hit
    o = origin(row)
    if o and o in first_seen and first_seen[o][0] != i:
        other_id, other_part = first_seen[o]
        lines = [f"### {i}", "", where(uses), "",
                 f"**The same record as {other_id},** whose card is in `{other_part}`: its record and sources are "
                 f"checked there. Check only this proposal's points against it.",
                 f"- statement: {row.get('statement', '')}", f"- scope: {row.get('scope', '')}"]
        return "\n".join(lines) + "\n"
    if o and register:
        first_seen.setdefault(o, (i, part_name))
    lines = [f"### {i}", "", where(uses), "", f"**Record** (`{path}`):"] + field_lines(row)
    shown, width = set(), WIDTH if len(rests) <= 6 else max(150, 2700 // len(rests))
    for c in rests:
        lines += citation_lines(c, ctx, "", shown, width)
    return "\n".join(lines) + "\n"


def claim_card(ids_uses, ctx):
    first = ids_uses[0][0]
    hit = rid.lookup(first)
    uses = [u for _, us in ids_uses for u in us]
    if not hit:
        return f"### {first}\n\n{where(uses)}\n\nNo such record.\n"
    path, row, _, rests = hit
    lines = [f"### {first}", "", where(uses)]
    if len(ids_uses) > 1:
        lines += ["", "**The same record, cited as:** " + ", ".join(i for i, _ in ids_uses[1:])]
    lines += ["", f"**Record** (`{path}`):"] + field_lines(row)
    listed = set(rid.cite_split(row.get("list_cite_ids", "")))
    complete = set(rid.cite_split(row.get("complete_cite_ids", "")))
    shown, width = set(), WIDTH if len(rests) <= 6 else max(150, 2700 // len(rests))
    for c in rests:
        cid = c.get("cite_id")
        label = " (the list)" if cid in listed else " (the words that make the list complete)" if cid in complete else ""
        lines += citation_lines(c, ctx, label, shown, width)
    return "\n".join(lines) + "\n"


def digest_entries():
    """{id: (the digest's lines for it, [(state, place, dates)] of its parts)}, from its axes and constants."""
    out, cur, section = {}, None, ""
    for line in open(DIGEST, encoding="utf-8").read().splitlines():
        if line.startswith("## "):
            section, cur = line[3:].strip(), None
            continue
        if section not in ("Axes", "Constants"):
            continue
        m = re.match(r"^- \*\*(Y[AK]-\d+)\*\*\s*(.*)$", line)
        if m:
            cur = m.group(1)
            parts = []
            if cur.startswith("YK"):
                c = re.match(r"^[^:]*:\s*(.*)$", m.group(2))
                st = re.match(r"^(.*?), at (.*)$", c.group(1) if c else "")
                if st:
                    for pl in re.split(r";\s+", st.group(2)):
                        pm = re.match(r"^(.*?)\s*\(as of ([^)]*)\)\s*$", pl)
                        parts.append((st.group(1), pm.group(1) if pm else pl, pm.group(2) if pm else ""))
            out[cur] = ([line], parts)
            continue
        if cur and line.startswith("  "):
            out[cur][0].append(line)
            t = re.match(r"^  - today: (.*) @ (.*?) \(as of ([^)]*)\)\s*$", line)
            if t:
                out[cur][1].append((t.group(1), t.group(2), t.group(3)))
    return out


def part_matches(i, inner, entries):
    """Whether a cited part, 'state @ place, as of date', is the digest's as written: (True or False, why)."""
    if "@" not in inner:
        return False, "no place after @"
    state, rest = inner.split("@", 1)
    pm = re.match(r"\s*(.*?)(?:,\s*as of\s*(.*))?$", rest.strip())
    place, date = pm.group(1).strip(), (pm.group(2) or "").strip()
    state = state.strip().rstrip(",")
    for s, p, d in entries.get(i, ([], []))[1]:
        if norm_place(s) == norm_place(state) and norm_place(p) == norm_place(place) and \
                norm_place(d).startswith(norm_place(date)):
            return True, ""
    return False, f"the digest has no part '{state} @ {place}, as of {date}' for {i}"


def places_groups():
    group = {}
    with open(PLACES, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
            group[norm_place(r["place"])] = r.get("grouped") or r["place"]
    return group


def yemen_card(i, uses, entries, group, ctx):
    hit = rid.lookup(i)
    lines = [f"### {i}", "", where(uses), "", "**Each part as cited, against the digest** (by script):"]
    cited_parts = []
    for sec, n, p in uses:
        for m in YEMEN_FACT.finditer(p):
            if m.group(1) == i and m.group(2):
                ok, why = part_matches(i, m.group(2), entries)
                cited_parts.append(m.group(2))
                lines.append(f"- {at(sec, n)}: `{i} ({m.group(2)})`: " + ("the digest's part as written" if ok else why))
    lines += ["", "**The digest:**", ""] + [f"> {l.strip()}" for l in entries.get(i, ([f"(no entry for {i})"], []))[0]]
    if not hit:
        return "\n".join(lines + ["", "No such record."]) + "\n"
    path, row, _, rests = hit
    cited_places = {norm_place(re.split(r",\s*as of", x.split("@", 1)[1])[0]) for x in cited_parts if "@" in x}
    cited_groups = {norm_place(group.get(p, p)) for p in cited_places}

    def near(place):
        """A place the check reads: a cited place, one grouped with it, or "place not stated"."""
        pl = norm_place(place)
        return pl in cited_places or norm_place(group.get(pl, pl)) in cited_groups or pl == "place not stated"

    keep, other_states = set(), 0
    lines += ["", f"**Record** (`{path}`):"]
    for k, v in row.items():
        if not v:
            continue
        if k == "states":
            lines.append("- states at the cited places, the places grouped with them, and \"place not stated\", one line "
                         "each (the place after @, the citations in brackets):")
            for st in v.split(" | "):
                sm = re.match(r"^(.*?) @ (.*?) \[([^\]]*)\]\s*$", st.strip())
                if sm and not near(sm.group(2)):
                    other_states += 1
                    continue
                if sm:
                    keep.update(re.findall(r"YE-[A-Z]\d{3,4}", sm.group(3)))
                lines.append(f"  - {st.strip()}")
            if other_states:
                lines.append(f"  - and {other_states} states at other places (in `axes.tsv`)")
        elif k in ("today_cite_ids", "cite_ids", "condition_ids"):
            lines.append(f"- {k}: {v}")
            if k == "cite_ids":
                keep.update(rid.cite_split(v))
        elif len(v) > FIELD_CAP:
            lines.append(f"- {k}: {v[:FIELD_CAP]} … ({len(v)} characters)")
        else:
            lines.append(f"- {k}: {v}")
    for p in sorted(cited_places):
        g = group.get(p, p)
        members = sorted(k for k, v in group.items() if norm_place(v) == norm_place(g) and k != p)
        lines.append(f"- the place '{p}' is grouped in '{g}'" + (f", with: {'; '.join(members[:12])}" if members else ""))
    conds = [c for c in rid.cite_split(row.get("condition_ids", "")) if c]
    by_cite, shown, other_conds = defaultdict(list), [], 0
    for c in conds:
        h = rid.lookup(c)
        if not h:
            continue
        r = h[1]
        for x in rid.cite_split(r.get("cite_ids", "")):
            by_cite[x].append(c)
        if near(r.get("place", "")) or i.startswith("YK"):
            shown.append((c, r))
        else:
            other_conds += 1
    if shown:
        lines += ["", "**Its conditions at those places** (each with its citations' ids; `record_ids.py` prints the "
                      "quotes):"]
        for c, r in shown:
            lines.append(f"- {c}: {r.get('condition', '')} | {r.get('state', '')} | @ {r.get('place', '')} | "
                         f"held_at {r.get('held_at', '')} | cites {r.get('cite_ids', '')}"
                         + (f" | note: {r['note'][:300]}" if r.get("note") else ""))
        if other_conds:
            lines.append(f"- and {other_conds} conditions at other places")
    kept = [c for c in rests if c.get("cite_id") in keep]
    if kept:
        lines += ["", "**The citations of the cited parts, and of every state at the same place or at 'place not "
                      "stated'**, each with the conditions that cite it (the others' are in "
                      "`studies/yemen-cases/citations.tsv`). A citation's path names the run that holds it: the run's "
                      "`README.md` says what kind of source it is:"]
        for c in kept:
            source, locator, quote = c.get("source", ""), c.get("locator", ""), c.get("quote", "")
            found = ctx.src.check_quote(quote, source, locator)[0] if source and quote else "no quote"
            conds_of = ", ".join(by_cite.get(c.get("cite_id"), []))
            lines.append(f"- {c.get('cite_id')}" + (f" (for {conds_of})" if conds_of else "") +
                         f": `{source}` | {locator} | {c.get('source_date', '')} | quote check: {found} | {quote}")
    return "\n".join(lines) + "\n"


def write_parts(out, base, head, items, render, limit, by_count=False):
    """Write the cards in parts: base.md where one part holds them, else base-1.md and on. Each card is sized first,
    then written with its part's final name (render(item, part name, final))."""
    sizes = [1 if by_count else len(render(it, base + ".md", False).encode()) for it in items]
    k = max(1, -(-sum(sizes) // limit))             # as few parts as the limit allows, of about equal size
    target = sum(sizes) / k
    parts, cur, size = [], [], 0
    for it, n in zip(items, sizes):
        if cur and len(parts) < k - 1 and size + n / 2 > target:
            parts.append(cur)
            cur, size = [], 0
        cur.append(it)
        size += n
    if cur:
        parts.append(cur)
    names = [f"{base}.md"] if len(parts) == 1 else [f"{base}-{k}.md" for k in range(1, len(parts) + 1)]
    for name, part in zip(names, parts):
        texts = [render(it, name, True) for it in part]
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(head(name, part) + "\n".join(texts))
        print(f"{name}\t{len(part)} cards", file=sys.stderr)
    return names


def quotes(ctx, cited_by, path):
    """Every quote each cited record rests on, checked against its source: one row per record and citation."""
    done, rows, counts = {}, [], {}
    for i_, qs in cited_by.items():
        hit = rid.lookup(i_)
        if not hit:
            continue
        seen = set()
        for c in hit[3]:
            if c.get("cite_id") in seen:
                continue
            seen.add(c.get("cite_id"))
            source, locator, quote = c.get("source", ""), c.get("locator", ""), c.get("quote", "")
            key = (quote, source, locator)
            if key not in done:
                done[key] = ctx.src.check_quote(quote, source, locator) if source and quote else ("no quote", "", "")
            res, why, share = done[key]
            counts[res.split(" ")[0]] = counts.get(res.split(" ")[0], 0) + 1
            rows.append([" ".join(sorted(qs)), i_, c.get("cite_id", ""), source, locator, res,
                         why or (f"best share of its six-word runs: {share}" if share else "")])
    with open(path, "w", encoding="utf-8") as f:
        f.write("questions\tid\tcite_id\tsource\tlocator\tresult\tnote\n")
        for r in rows:
            f.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    print(f"{os.path.basename(path)}\t{len(rows)} quotes: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())),
          file=sys.stderr)


def uncited(cited_by, path):
    """Every record of the questions that no proposal cites: statements, copies and not-found rows."""
    n = 0
    with open(path, "w", encoding="utf-8") as f:
        f.write("id\tfile\n")
        for q in sorted(os.listdir(RECORDS)):
            if not re.fullmatch(r"Q\d", q):
                continue
            for i_, (p, row, _, _) in sorted(rid.platform_rows(q).items()):
                if re.search(r"-C\d{3}$", i_) or i_ in cited_by:
                    continue
                f.write(f"{i_}\t{p}\n")
                n += 1
    print(f"{os.path.basename(path)}\t{n} records no proposal cites", file=sys.stderr)


def main(argv):
    name, out, qs, quote_tsv, uncited_tsv = "draft.md", OUT, [], None, None
    i = 0
    while i < len(argv):
        if argv[i] in ("--file", "--quotes", "--uncited", "--out"):
            val = argv[i + 1]
            if argv[i] == "--file":
                name = val
            elif argv[i] == "--quotes":
                quote_tsv = val
            elif argv[i] == "--uncited":
                uncited_tsv = val
            else:
                out = val
            i += 2
        else:
            qs.append(argv[i])
            i += 1
    qs = qs or [f"Q{n}" for n in range(1, 9)]
    os.makedirs(out, exist_ok=True)
    ctx = Context()
    claims, yemen, cited_by, first_seen, doesnt = defaultdict(OrderedDict), OrderedDict(), defaultdict(set), {}, []
    for q in qs:
        ids, ds = cited(q, name)
        doesnt += [(q, n, p) for n, p in ds]
        by_platform = defaultdict(list)
        for i_, uses in ids.items():
            cited_by[i_].add(q)
            if rid.YEMEN_ID.fullmatch(i_):
                yemen.setdefault(i_, []).extend((f"{q}, section {s}", n, p) for s, n, p in uses)
                continue
            code = i_.split("-")[1]
            if CLAIM.search(i_):
                hit = rid.lookup(i_)
                key = (origin(hit[1]) if hit else None) or i_
                claims[code].setdefault(key, []).append((i_, [(f"{q}, section {s}", n, p) for s, n, p in uses]))
            elif FACT.search(i_):
                by_platform[code].append((i_, uses))
        for code, items in sorted(by_platform.items()):
            base = f"{q}-{PLATFORMS.get(code, code)}"
            head = lambda nm, its, q=q, code=code: (
                f"# Cards: {q} on {PLATFORMS.get(code, code)}\n\n{len(its)} records cited by "
                f"`studies/proposals/drafts/{q}/{name}`, made by `method/r5_cards.py`.\n\n" + point_list(its))
            write_parts(out, base, head, items,
                        lambda it, part, final: fact_card(it[0], it[1], ctx, first_seen, part, final), FACT_PART)
    for code, groups in sorted(claims.items()):
        items = list(groups.values())
        head = lambda nm, its, code=code: (
            f"# Cards: what the proposals cite as not found or absent, on {PLATFORMS.get(code, code)}\n\n"
            f"{len(its)} records, from {', '.join(qs)}.\n\n" + point_list([(g[0][0], [u for _, us in g for u in us])
                                                                         for g in its], "q"))
        write_parts(out, f"claims-{PLATFORMS.get(code, code)}", head, items,
                    lambda g, part, final: claim_card(g, ctx), CLAIMS_PART, by_count=True)
    if yemen:
        entries, group = digest_entries(), places_groups()
        items = list(yemen.items())
        head = lambda nm, its: (f"# Cards: Stage 1's facts the proposals cite\n\n{len(its)} ids, from "
                                f"{', '.join(qs)}.\n\n" + point_list(its, "q"))
        write_parts(out, "yemen", head, items,
                    lambda it, part, final: yemen_card(it[0], it[1], entries, group, ctx), YEMEN_PART)
    if doesnt:
        entries = digest_entries()

        def ds_card(q, n, p):
            ids = list(dict.fromkeys(rid.YEMEN_ID.findall(p) + [x for x in rid.PLATFORM_ID.findall(p) if x.startswith(q)]))
            out = [f"### {q}:{n}", "", f"**Cited at:** {q}, section 6, line {n}", "", f"**Point:** {p}"]
            for x in ids:
                if x in entries:
                    out += [f"- {x}, as the digest gives it:"] + [f"  > {l.strip()}" for l in entries[x][0]]
                elif rid.lookup(x):
                    out.append(f"- {x}: {rid.lookup(x)[2][:400]}")
            return "\n".join(out) + "\n"
        cards = [ds_card(q, n, p) for q, n, p in doesnt]
        with open(os.path.join(out, "doesnt-show.md"), "w", encoding="utf-8") as f:
            f.write(f"# Cards: what the proposals say Yemen's evidence doesn't show\n\n{len(cards)} points, from "
                    f"{', '.join(qs)}, each named by its question and line.\n\n## The cards\n\n" + "\n".join(cards))
        print(f"doesnt-show.md\t{len(cards)} cards", file=sys.stderr)
    if quote_tsv:
        quotes(ctx, cited_by, quote_tsv)
    if uncited_tsv:
        uncited(cited_by, uncited_tsv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
