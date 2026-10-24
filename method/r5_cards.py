"""Cards for step R5's checks (PLAN.md section 4, step R5): for each record a proposal cites, what it rests on, with
each quote in its source's context, so that a checking run reads one file and opens a source only where the card
doesn't settle a point.

Usage: python3 -I method/r5_cards.py [QUESTION ...] [--file NAME] [--out DIR]

Reads studies/proposals/drafts/<QUESTION>/<NAME> (draft.md by default; all eight questions when none is named) and
writes, in DIR (studies/proposals/checks/R5/cards by default):
- <QUESTION>-<platform>.md: a card for each statement, copy and pilot copy the file cites on that platform;
- claims-<platform>.md: a card for each not-found row, copied gap and pilot absence cited on that platform, across
  the questions named;
- yemen.md: a card for each of Stage 1's ids cited, across the questions named.

A card gives:
- where the file cites the record: each point's section, line and text;
- the record's fields, as `method/record_ids.py --all` prints them;
- for a fact, each citation: its source, locator, date and kind (`method/source_kinds.py`), its quote, whether the
  script finds the quote in the source (`method/quote_check.py`), and the quote in its context: the source's title,
  the headings above the quote where the source has them, and the text around it, with the quote between ⟪ and ⟫.
  For a step of an observed run, the step's intent, address, title and time from the run's `actions.jsonl`.

The context is the source's text as the quote check normalizes it (whitespace joined, entities decoded), so a
table or a list reads as one line. A card decides nothing: the checking run does.
"""
import json, os, re, subprocess, sys
from collections import OrderedDict, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import record_ids as rid
from check_proposals import points, ROOTS
from quote_check import Sources, variants
from source_kinds import kind_of
from runs_corpus import STEP, HTML_TEXT

SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS = os.path.join(SKM, "studies", "proposals", "drafts")
OUT = os.path.join(SKM, "studies", "proposals", "checks", "R5", "cards")
CAPTURES = os.path.join(SKM, "evidence", "product-class", "runs")
PLATFORMS = {"SH": "shopify", "SA": "salla", "ZD": "zid", "WC": "woocommerce", "BC": "bigcommerce"}
FACT = re.compile(r"-(?:[KP]\d{4}|C\d{3}|\d{3})$")
CLAIM = re.compile(r"-(?:[GHA]\d{4}|N\d{2,3})$")
WIDTH = 450          # characters of context on each side of a quote
MARKUP = re.compile(r"[<>{}\\]|&\w+;")
FIELD_CAP = 1500     # a record's long working fields are cut here; its statement and scope never are


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
    """{id: [(section, line, point)]} for every id the draft cites, in order of first citation."""
    path = os.path.join(DRAFTS, q, name)
    text = open(path, encoding="utf-8").read()
    sec = sections(text)
    out = OrderedDict()
    for n, p in points(text):
        for i in dict.fromkeys(rid.PLATFORM_ID.findall(p) + rid.YEMEN_ID.findall(p)):
            if i.startswith("Q") and not i.startswith(q + "-"):
                continue
            out.setdefault(i, []).append((sec.get(n, 0), n, p))
    return out


class Context:
    """The quote in its source, read once per source."""

    def __init__(self):
        caps = sorted(os.path.join(CAPTURES, d) for d in os.listdir(CAPTURES)) if os.path.isdir(CAPTURES) else []
        self.src = Sources(ROOTS, caps)
        self.raw, self.actions = {}, {}

    def raw_texts(self, source, locator):
        key = (source, locator if source.endswith(".warc.gz") else "")
        if key not in self.raw:
            if re.match(r"^https?://", source):
                self.raw[key] = self.src.web_texts(source)[0] or []
            else:
                self.raw[key] = self.src.local_texts(source, locator)[0] or []
        return self.raw[key]

    def step(self, source):
        """The step's row of its run's actions.jsonl, for a step file of an observed run."""
        m = re.match(r"^(observed-s[ha])(?:@([0-9a-f]{6,40}))?:(.+)$", source)
        if not m:
            return None
        repo, commit, rel = m.group(1), m.group(2) or "HEAD", m.group(3).strip().lstrip("/")
        s = STEP.match(rel) or HTML_TEXT.match(rel)
        if not s:
            return None
        run, n = s.group(1), int(s.group(2))
        key = (repo, commit, run)
        if key not in self.actions:
            p = subprocess.run(["git", "-C", ROOTS[repo], "show", f"{commit}:raw/runs/{run}/actions.jsonl"],
                               capture_output=True)
            rows = {}
            for line in p.stdout.decode("utf-8", "replace").splitlines():
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if isinstance(r, dict) and "step" in r:
                    rows[r["step"]] = r
            self.actions[key] = rows
        return self.actions[key].get(n)

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
        if not re.search(r"(?m)^#{1,6}\s", raw):
            return []
        probe = " ".join(variants(quote)[2][1].split()[:6])
        lines = raw.splitlines()
        at = next((i for i, l in enumerate(lines) if probe and probe in variants(l)[2][1]), None)
        if at is None:
            return []
        path, level = [], 7
        for line in reversed(lines[:at + 1]):
            m = re.match(r"^(#{1,6})\s+(.*)", line)
            if m and len(m.group(1)) < level:
                path.append(m.group(2).strip())
                level = len(m.group(1))
                if level == 1:
                    break
        return path[::-1]

    def around(self, source, locator, quote):
        """(title, headings, excerpt): the quote with the text around it, at the first level of matching that finds
        it, from the cleanest of the source's texts that hold it (the fewest marks of markup around it)."""
        raws = self.raw_texts(source, locator)
        title = next((t for t in (self.title(r) for r in raws) if t), "")
        texts, _ = self.src.texts(source, locator)
        for level, (kind, q) in enumerate(variants(quote)):
            if not q:
                continue
            found = []
            for tkind, t in texts or []:
                k = t.find(q) if tkind == kind else -1
                if k < 0:
                    continue
                a, b = max(0, k - WIDTH), min(len(t), k + len(q) + WIDTH)
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


def fact_card(i, uses, ctx):
    hit = rid.lookup(i)
    if not hit:
        return f"### {i}\n\nNo such record.\n"
    path, row, _, rests = hit
    lines = [f"### {i}", "", where(uses), "", f"**Record** (`{path}`):"] + field_lines(row)
    for c in rests:
        source, locator, quote = c.get("source", ""), c.get("locator", ""), c.get("quote", "")
        kind = kind_of(source, ROOTS)[0] if source else ""
        found = ctx.src.check_quote(quote, source, locator)[0] if source and quote else "no quote"
        lines += ["", f"**Citation {c.get('cite_id')}:** `{source}` | {locator} | {c.get('source_date', '')} | "
                      f"kind: {kind} | quote check: {found}"]
        st = ctx.step(source) if source else None
        if st:
            lines.append(f"- step {st.get('step')}: {st.get('intent')} | {st.get('url')} | \"{st.get('title')}\" | "
                         f"{st.get('t_start')}")
        lines.append(f"- quote: {quote}")
        if source and quote:
            title, heads, excerpt = ctx.around(source, locator, quote)
            if title:
                lines.append(f"- title: {title}")
            if heads:
                lines.append(f"- headings: {' > '.join(heads)}")
            lines.append(f"- in context: {excerpt}" if excerpt else "- in context: (the quote was not found in the source's text)")
    return "\n".join(lines) + "\n"


def claim_card(i, uses):
    hit = rid.lookup(i)
    if not hit:
        return f"### {i}\n\nNo such record.\n"
    path, row, _, rests = hit
    lines = [f"### {i}", "", where(uses), "", f"**Record** (`{path}`):"] + field_lines(row)
    for c in rests:
        lines.append(f"- rests on {c.get('cite_id')}: `{c.get('source')}` | {c.get('locator')} | "
                     f"{c.get('source_date', '')} | {c.get('quote')}")
    return "\n".join(lines) + "\n"


def yemen_card(i, uses):
    lines = [f"### {i}", "", where(uses), "", "**Record:**", "", "```", rid.show(i, None), "```"]
    return "\n".join(lines) + "\n"


def main(argv):
    name, out, qs = "draft.md", OUT, []
    i = 0
    while i < len(argv):
        if argv[i] == "--file":
            name, i = argv[i + 1], i + 2
        elif argv[i] == "--out":
            out, i = argv[i + 1], i + 2
        else:
            qs.append(argv[i])
            i += 1
    qs = qs or [f"Q{n}" for n in range(1, 9)]
    os.makedirs(out, exist_ok=True)
    ctx = Context()
    claims, yemen = defaultdict(OrderedDict), OrderedDict()
    for q in qs:
        by_platform = defaultdict(list)
        for i_, uses in cited(q, name).items():
            if rid.YEMEN_ID.fullmatch(i_):
                yemen.setdefault(i_, []).extend((f"{q}, section {s}", n, p) for s, n, p in uses)
                continue
            code = i_.split("-")[1]
            if CLAIM.search(i_):
                claims[code][i_] = [(f"{q}, section {s}", n, p) for s, n, p in uses]
            elif FACT.search(i_):
                by_platform[code].append((i_, uses))
        for code, items in sorted(by_platform.items()):
            cards = [fact_card(i_, uses, ctx) for i_, uses in items]
            head = (f"# Cards: {q} on {PLATFORMS.get(code, code)}\n\n{len(items)} records cited by "
                    f"`studies/proposals/drafts/{q}/{name}`, made by `method/r5_cards.py`.\n\n")
            with open(os.path.join(out, f"{q}-{PLATFORMS.get(code, code)}.md"), "w", encoding="utf-8") as f:
                f.write(head + point_list(items) + "\n".join(cards))
            print(f"{q}-{PLATFORMS.get(code, code)}.md\t{len(items)} cards", file=sys.stderr)
    for code, items in sorted(claims.items()):
        cards = [claim_card(i_, uses) for i_, uses in items.items()]
        with open(os.path.join(out, f"claims-{PLATFORMS.get(code, code)}.md"), "w", encoding="utf-8") as f:
            f.write(f"# Cards: what the proposals cite as not found or absent, on {PLATFORMS.get(code, code)}\n\n"
                    f"{len(items)} rows, from {', '.join(qs)}.\n\n" + point_list(list(items.items()), "q") + "\n".join(cards))
        print(f"claims-{PLATFORMS.get(code, code)}.md\t{len(items)} cards", file=sys.stderr)
    if yemen:
        cards = [yemen_card(i_, uses) for i_, uses in yemen.items()]
        with open(os.path.join(out, "yemen.md"), "w", encoding="utf-8") as f:
            f.write(f"# Cards: Stage 1's facts the proposals cite\n\n{len(yemen)} ids, from {', '.join(qs)}.\n\n"
                    + point_list(list(yemen.items()), "q") + "\n".join(cards))
        print(f"yemen.md\t{len(yemen)} cards", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
