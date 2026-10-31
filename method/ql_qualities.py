"""The qualities pass (PLAN.md, Stage 4A, "The qualities pass"; the brief studies/class-model/briefs/QL-qualities.md, its
design briefs/QL-qualities-design.md with the coordinator's decisions of 31 October): what the five platforms state on
how well, how safely, or within what bounds they do what they do, read kind by kind (16 kinds, 44 asks), one row per
finding; the coordinator lands the `found` rows as held entries and quality rows, and labels the model's existing
quality rows as qualities, the plans' terms, or other. It imports the second stage's source, commit and quote tests and
its entry ids (method/s2_held.py), so a passage either stage quotes is one entry of held/<platform>/entries-s2.tsv.

Usage: python3 -I method/ql_qualities.py COMMAND [options]

For the agents (a part, such as QL-SA, as studies/class-model/qualities/parts.tsv lists it):
  asks   --part P [--left]
         the part's asks, kind by kind: each kind's plain name, its ISO/IEC 25010:2023 characteristic (a reading), the
         first decisions it drives and the capabilities it lands on by default; the model's quality rows of the
         platform that qualities/labels.tsv labels as the kind; the default capabilities' cells on the platform (held,
         placed as, reading) and the second stage's rows on them where landed; the places qualities/sources.tsv names
         for the platform and kind; then each ask with its question. --left lists the asks the part's file has no row
         for yet
  check  --part P
         tests qualities/<platform>/<part>.tsv and <part>.md: the form (the header, the field counts, no double
         quote); that every ask of the part has its rows, one or more `found` or exactly one other (a kind's code
         alone, or an ask of another part's kind as QL-SH-3 writes them, takes found rows only); the values of
         outcome, kind, form, basis, holder, source_type (the seed's codes) and could_change; the subject's prefix
         against kind; cap_id a capability of merged/capabilities.tsv with a cell for the platform, or `platform`;
         quality with no colon and not a mark of inclusion; a price, a fee or a rate charged never a quality (QL-R1);
         value inside its quote, as quote_check folds it, or inside the held id's text, and holding no `;`; each
         source by s2_held.py's tests (its form, the platform's repository, the part's commits, `line N` with the
         quote beginning within three lines of N, an archive's offset, the quote found), or an id held on the
         platform; the columns each outcome takes; capture's form on not-held, and its place; the reading's quotes;
         the notes' first line. NOTE lines, to read again: a row the term rules would call a plan allowance (a term?
         QL-R1); a found row on `platform` whose kind lands on a capability by default; an absent row; a short quote;
         a could_change the kind doesn't drive. Exits 1 on a problem

For the coordinator:
  parts  [--write]
         the seven parts of the design's section 8, with the commits fixed for the run (each repository's HEAD);
         --write writes qualities/parts.tsv (part, platform, kinds, asks, commits, model, state), refusing to rewrite
         it once a part is checked or landed
  mark   --part P --state checked|open
         sets a part's state: `checked` only where `check` finds no problem
  land   --platform P [--batch B] [--dry-run]
         lands the platform's parts at `checked` (or `landed`) into the batch QL-<XX> (or a correction batch
         QL-<XX>-R<n>), each part checked again first. It refuses a part with a problem, a platform whose second-stage
         batch S2-<XX> isn't in held/batches.tsv yet (the coordinator's decision 1), and a batch already applied to the
         model. For each found row: its passage as an entry of held/<platform>/entries-s2.tsv (s2_held.py's id, so a
         passage the second stage quoted is the same entry), or the held id it names; on a capability, a line of
         held/<platform>/placements-<B>.tsv (placement `quality`, supports `shows`, quality `<quality>: <value>`), or,
         where it names a concern-map statement, a row of held/<platform>/s2-keys.tsv with batch <B>; on `platform`, a
         row of qualities/platform.tsv; and its label in qualities/labels.tsv (decided_by `<part> line <n>`). A row
         whose quality row (cap_id, platform, quality, value, key) is already in a part's qualities.tsv isn't placed
         again: it takes its label only. Also writes held/batches/<B>.txt, a row of held/batches.tsv,
         held/<platform>/notes-<B>.md (its first line the parts' commits), qualities/outcomes.tsv (the other
         outcomes), qualities/captures.tsv (every capture lead) and qualities/coverage.tsv (each platform and ask:
         found with its count, or its outcome, with the commits), and sets the parts landed. Then:
         held_entries.py check --platform P --batch B; held_amend.py plan / apply --platform P --batch B;
         check_class_part.py on each part it names; class_merge.py --complete; labels check
  labels propose [--write]
         labels each of the model's quality rows (the parts' qualities.tsv and qualities/platform.tsv) by the design's
         rules, in order: Q1 a measure of the system with no money word (quality, with its kind), T1 money (term), T2
         a plan allowance from a plan structure or naming a plan (term), T3 a plan structure's other line (term),
         otherwise unsure, for the review. A label decided by review or by a part is kept. Prints the counts per rule,
         label, kind and platform; --write writes qualities/labels.tsv
  labels review [--from I] [--to J]
         the unsure rows, numbered, each with its capability, key and its entry's structure, for QL-L, who writes
         qualities/labels-review.tsv (row_id, label, kind, form, reading)
  labels apply-review
         takes qualities/labels-review.tsv into labels.tsv, decided_by `review`
  labels check
         every model row has a settled label, every label names a row, and the merged files' rows (merged/qualities.tsv
         and merged/terms.tsv) are exactly the parts' rows and platform.tsv's; the counts by label, rule, kind and
         platform. Exits 1 on a problem
  labels clear --rule R
         removes the labels rule R decided (Q1, T1, T2, T3 or unsure)

A row's columns (qualities/<platform>/<part>.tsv, tab-separated, a header, no quoting, no double quote): subject,
outcome, kind, form, basis, cap_id, holder, quality, value, source, locator, quote, identifier, date, scope,
source_type, read, searched, capture, could_change, reading. The model's folder is studies/class-model, or
CLASS_MODEL_DIR (for tests); the evidence repositories' roots are q3_misses.py's ROOTS. Run with python3 -I from the
repository's root.
"""
import argparse, collections, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, PREFIX, rows, citable, key as skey
import quote_check
import held_entries as he
import s2_held as s2
from s2_held import (semi, clip, rel, read_tsv, write_tsv, parse_commits, notes_commits, same, sources,
                     source_problems, id_text, plat_of, passage_key, passage_id, not_held_place, reading_problems,
                     commits_now, caps_table, merged_cells, keep_others, FILE_SOURCE, ENTRY_ID, EVIDENCE, RELEASE,
                     OWN, ARABIC)
from class_merge import (row_ids, model_parts, quality_rows, QDIR, LABELS, PLATFORM_QUAL, PLATFORM_HEAD,
                         LABELS_HEAD, LABEL_VALUES, QUAL_FIELDS)

HELD = os.path.join(MODEL, "held")
MERGED = os.path.join(MODEL, "merged")
PARTS_TSV = os.path.join(QDIR, "parts.tsv")
SOURCES_TSV = os.path.join(QDIR, "sources.tsv")
REVIEW_TSV = os.path.join(QDIR, "labels-review.tsv")
OUTCOMES_TSV = os.path.join(QDIR, "outcomes.tsv")
CAPTURES_TSV = os.path.join(QDIR, "captures.tsv")
COVERAGE_TSV = os.path.join(QDIR, "coverage.tsv")
PARTS_HEAD = ["part", "platform", "kinds", "asks", "commits", "model", "state"]
HEAD = ["subject", "outcome", "kind", "form", "basis", "cap_id", "holder", "quality", "value", "source", "locator",
        "quote", "identifier", "date", "scope", "source_type", "read", "searched", "capture", "could_change", "reading"]
OUT_HEAD = ["platform", "batch", "subject", "kind", "outcome", "part", "line", "commits", "read", "searched", "capture",
            "could_change", "reading"]
CAPTURES_HEAD = ["platform", "batch", "part", "line", "subject", "kind", "outcome", "could_change", "capture", "read",
                 "searched", "reading"]
COVER_HEAD = ["platform", "ask", "kind", "result", "found", "part", "lines", "commits"]
REVIEW_HEAD = ["row_id", "label", "kind", "form", "reading"]
KEYS_HEAD = s2.KEYS_HEAD
OUTCOMES = s2.OUTCOMES
CITING = s2.CITING
FORMS = ("commitment", "bound", "attestation", "data-keeping")
BASES = ("promised", "enforced", "reported", "attested")
HOLDERS = ("platform", "own-service", "third-party", "merchant")
DECISIONS = ("D1", "D2", "D3", "D4", "D5", "D6")
CAPTURE_REPOS = {p: tuple(r for r in OWN[p] if r != RELEASE) for p in PLATFORMS}
LIST_FIELDS = ("scope", "read", "searched", "could_change")
PLATFORM = "platform"
CLIP = 400                      # read and searched, clipped in outcomes.tsv

# The checklist (the brief, "The kinds: the checklist"): code -> plain name, ISO/IEC 25010:2023 (a reading), the first
# decisions it drives, the capabilities it lands on by default (or `platform`), and the default as the brief words it.
KINDS = collections.OrderedDict([
    ("ISO", ("Isolation between stores", "security (confidentiality, integrity); reliability (fault tolerance); performance efficiency (capacity)", ("D1",), ["platform"], "platform")),
    ("LOC", ("Where data lives", "security (confidentiality, accountability); no product characteristic names it: ISO/IEC 25012's compliance is nearer", ("D1", "D4"), ["CM-TRU-014"], "CM-TRU-014")),
    ("SUB", ("Subprocessors", "security (confidentiality, accountability)", ("D1", "D5"), ["CM-TRU-015"], "CM-TRU-015")),
    ("RET", ("Retention and deletion", "security (confidentiality); reliability (recoverability) for backups", ("D1", "D3"), ["CM-TRU-016"], "CM-TRU-016")),
    ("ENC", ("Protection of data in transit and at rest", "security (confidentiality, integrity)", ("D1", "D2"), ["platform", "CM-TRU-018"], "platform; CM-TRU-018 for card data")),
    ("IDN", ("Identity, sign-in and access", "security (authenticity, accountability, non-repudiation, resistance)", ("D2",), ["CM-TRU-001", "CM-TRU-002", "CM-API-002", "CM-CUS-010", "CM-CUS-011", "CM-STF-005"], "CM-TRU-001, CM-TRU-002, CM-API-002, CM-CUS-010, CM-CUS-011, CM-STF-005")),
    ("AUD", ("Records of who did what", "security (accountability, non-repudiation)", ("D2",), ["CM-TRU-003"], "CM-TRU-003")),
    ("ATT", ("Attestations: certifications, audits, tests", "evidence of security, and of what else it audits; not a characteristic itself", ("D1", "D2", "D3"), ["CM-TRU-018", "CM-TRU-022", "platform"], "CM-TRU-018 for card data, CM-TRU-022 for security research; otherwise platform")),
    ("AVL", ("Availability and continuity", "reliability (availability, fault tolerance, recoverability)", ("D1", "D5"), ["CM-OPS-001", "CM-OPS-002"], "CM-OPS-001, CM-OPS-002")),
    ("CAP", ("Scale and speed", "performance efficiency (time behaviour, capacity, resource utilization); flexibility (scalability)", ("D1",), ["CM-OPS-001", "CM-OPS-003", "CM-OPS-006"], "CM-OPS-001, CM-OPS-003, CM-OPS-006")),
    ("IFB", ("Bounds on the interfaces", "performance efficiency (capacity); compatibility (interoperability)", ("D5",), ["CM-API-005", "CM-API-007", "CM-API-008", "CM-APP-005"], "CM-API-005, CM-API-007, CM-API-008, CM-APP-005")),
    ("STB", ("Bounds on a store's own records", "performance efficiency (capacity)", ("D1", "D6"), [], "the capability of the records bounded")),
    ("CHG", ("Commitments on change", "maintainability (modifiability); compatibility (interoperability)", ("D5",), ["CM-API-006"], "CM-API-006")),
    ("PRV", ("Privacy commitments", "security (confidentiality, accountability)", ("D1", "D2"), ["CM-TRU-013", "CM-TRU-007", "CM-TRU-017"], "CM-TRU-013, CM-TRU-007, CM-TRU-017")),
    ("SUP", ("Support commitments", "none: a service's quality, not the product's (ISO/IEC 25019:2023 holds quality in use; a reading)", ("S",), ["CM-ONB-003"], "CM-ONB-003")),
    ("ACS", ("Accessibility", "interaction capability (inclusivity)", ("S",), ["platform"], "platform, or the surface's capability")),
])
ASKS = collections.OrderedDict([
    ("ISO-1", "how one store's data is kept from another's"),
    ("ISO-2", "how one store's load or failure is kept from another's"),
    ("ISO-3", "whether a store can be hosted apart, on its own resources"),
    ("LOC-1", "where store data is hosted and processed (countries, regions, providers)"),
    ("LOC-2", "whether data leaves the merchant's or the buyer's country, and on what basis"),
    ("LOC-3", "whether the location can be chosen, or differs by market or plan"),
    ("SUB-1", "the subprocessors: who, for what, where"),
    ("SUB-2", "how a change in them is notified"),
    ("RET-1", "how long store data is kept after the store closes, and when it is deleted"),
    ("RET-2", "how long personal data, logs and backups are kept"),
    ("RET-3", "how long records the platform says the law requires (orders, invoices, payments) are kept"),
    ("ENC-1", "encryption in transit"),
    ("ENC-2", "encryption at rest, and how card data is held (tokenized, never stored)"),
    ("ENC-3", "who holds the keys, where stated"),
    ("IDN-1", "the staff's sign-in: two-step, passkeys, single sign-on, password rules"),
    ("IDN-2", "sessions: idle sign-out, devices, concurrent sign-ins"),
    ("IDN-3", "apps' and partners' access: tokens, their lifetimes, scopes granted"),
    ("IDN-4", "buyers' sign-in security"),
    ("IDN-5", "the checks on the people behind a store: levels, attempts, documents"),
    ("AUD-1", "which admin actions are recorded, and for how long"),
    ("AUD-2", "how the merchant reaches the record (export, API)"),
    ("ATT-1", "card data: PCI DSS, its level, scope and date"),
    ("ATT-2", "information security: ISO/IEC 27001, SOC 2 or SOC 3, a national framework (such as the Saudi National Cybersecurity Authority's controls)"),
    ("ATT-3", "privacy: ISO/IEC 27701, a data privacy framework, binding corporate rules, a national registration"),
    ("ATT-4", "security tests: penetration tests, scans, a bug bounty"),
    ("AVL-1", "the availability promised, with any credit"),
    ("AVL-2", "the availability reported (a status page, a past uptime)"),
    ("AVL-3", "backups and recovery"),
    ("AVL-4", "maintenance and how incidents are told"),
    ("CAP-1", "the scale stated (orders, transactions, requests at a peak)"),
    ("CAP-2", "the speed stated (page load, response time, a content network)"),
    ("IFB-1", "request rate limits, by API and plan"),
    ("IFB-2", "event delivery: timeouts, retries, when a subscription is switched off"),
    ("IFB-3", "sizes and counts: a payload, a file, a page, a bulk operation, a query's cost"),
    ("IFB-4", "limits on code the platform runs for apps (execution time, memory, size)"),
    ("STB-1", "the most records of a kind a store may hold, stated as a system limit (products, variants, options, collections, customers, locations)"),
    ("STB-2", "the sizes of a store's files and media"),
    ("CHG-1", "how long an API version is supported, and how often one is released"),
    ("CHG-2", "the notice given before a breaking change or a removal"),
    ("PRV-1", "the time to notify a breach"),
    ("PRV-2", "who answers a data subject's request, and within what time"),
    ("PRV-3", "requests from governments and others, and any report of them"),
    ("SUP-1", "support's channels, hours, languages and response times, by plan"),
    ("ACS-1", "the accessibility claimed for the admin, checkout, storefront themes or apps: a WCAG level, a conformance report"),
])
assert len(ASKS) == 44 and all(a.split("-")[0] in KINDS for a in ASKS)
ALL = list(KINDS)
# the parts (design, section 8): part, platform, its kinds, the kinds whose asks are its own. QL-SH-3 writes only found
# rows for AVL and LOC, whose asks are QL-SH-1's and QL-SH-2's
PART_DEFS = [("QL-SA", "salla", ALL, ALL), ("QL-ZD", "zid", ALL, ALL), ("QL-BC", "bigcommerce", ALL, ALL),
             ("QL-WC", "woocommerce", ALL, ALL),
             ("QL-SH-1", "shopify", ["LOC", "SUB", "RET", "ENC", "ATT", "PRV", "SUP", "ACS"], ["LOC", "SUB", "RET", "ENC", "ATT", "PRV", "SUP", "ACS"]),
             ("QL-SH-2", "shopify", ["IDN", "AUD", "AVL", "IFB", "STB", "CHG"], ["IDN", "AUD", "AVL", "IFB", "STB", "CHG"]),
             ("QL-SH-3", "shopify", ["ISO", "CAP", "AVL", "LOC"], ["ISO", "CAP"])]

# ---------------------------------------------------------------- the term rules (design, section 7.2)

PLAN_STRUCTURES = {"pricing-page-data", "plan-page-public", "plan-page-admin", "plan-comparison-public",
                   "plan-comparison-admin", "plan-feature-set", "billing-plans", "dev-store-plans", "merchant-plans",
                   "plans-offered", "store-plan-policies", "plan-comparison"}
SYSTEM = [   # Q1: the label names a measure of the system; the first kind whose words it holds
    ("SUB", r"sub-?processor"),
    ("RET", r"retention|\bretain|\bdelet|kept for|\bpurge"),
    ("ENC", r"encrypt|\btls\b|\bssl\b|\bhttps\b|tokeni[sz]"),
    ("ATT", r"\bpci\b|\bsoc ?[123]?\b|\biso ?\d|certif|\baudit(?!\w* log)|attest|penetration|bug bounty"),
    ("LOC", r"hosting|\bhosted\b|\bregions?\b|residen|data cent|data location|stored in"),
    ("AUD", r"audit log|activity log|\blogs?\b"),
    ("AVL", r"uptime|platform availability|service level|\bsla\b|backup|disaster recovery|data recovery|outage|incident|downtime|status page"),
    ("IDN", r"session|(?<!ai )\btokens?\b|password|two-step|two-factor|\b2fa\b|sign-?in|log-?in attempts|inactivity|\block\b|verification attempts|nafath|passkey"),
    ("IFB", r"rate limit|\brequests?\b|per second|per minute|throttl|timeout|retr(?:y|ies)|webhook|payload|query cost|\bbulk\b|\bapis?\b|execution time|\bmemory\b"),
    ("CAP", r"bandwidth|response time|latency|page load|\bpeak\b|\bcdn\b|transactions? (?:a|per|in)|orders? (?:a|per) (?:minute|second|day)"),
    ("SUP", r"\bsupport\b|response within"),
    ("CHG", r"\bapi versions?\b|deprecat|breaking change|\bsunset"),
    ("STB", r"file size|image size|\bmb\b|\bgb\b|maximum (?:number of )?(?:products|variants|options|collections|customers|images)|variants per|options per"),
    ("ACS", r"accessib|\bwcag\b|\bvpat\b"),
    ("PRV", r"\bbreach|data subject|government request|law enforcement"),
]
SYSTEM = [(k, re.compile(x)) for k, x in SYSTEM]
MONEY = re.compile(r"price|pricing|\bfees?\b|card rates?|\brates?\b(?! ?limit)|\btrials?\b|discount|cash ?back|promotion|"
                   r"\boffers?\b|repayment|interest|commission|surcharge|billing|\brewards?\b|payout|financ|\bannual|"
                   r"monthly|biennial|triennial|add-? ?ons?\b|bundle|\bcosts?\b|earnings|\bpaid\b|back on sales|سعر|أسعار|اسعار|رسوم|"
                   r"عمولة|عموله|خصم|تجربة|تجربه")
CURRENCY = re.compile(r"[$€£₹﷼]|\b(?:usd|eur|gbp|sar|aed|kwd|egp|cad|aud|inr|sr)\b|ريال|ر\.س|جنيه|دينار|درهم", re.I)
ALLOWANCE = re.compile(r"\b(?:staff|accounts?|logins?|locations?|expansion stores?|storefronts?|catalog(?:ue)?s?|"
                       r"products?|users?|employees?|features?|credits?|seats?|members?|plans that include it|markets?|"
                       r"languages?|currencies|branches)\b|موظف|حساب|فرع|فروع|منتج")
PLAN_WORDS = re.compile(r"\bplans?\b|\b(?:basic|grow|advanced|plus|enterprise|starter|pro|special|standard|premium|"
                        r"growth|team|pioneer)\b|باقة|باقه|الباقة|خطة", re.I)


def words(s):
    """A label as words: camelCase and snake_case split, case folded."""
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s or "")
    return " ".join(re.sub(r"[_.]+", " ", s).split()).casefold()


def system_kind(label):
    w = words(label)
    return next((k for k, x in SYSTEM if x.search(w)), "")


def rule_of(quality, value, structure=""):
    """(rule, label, kind) by the design's rules, in order; (unsure, unsure, '') where none settles it."""
    w = words(quality)
    kind = system_kind(quality)
    money = MONEY.search(w)
    if kind and not money:
        return "Q1", "quality", kind
    if money or (not kind and CURRENCY.search(value or "") and re.search(r"\d", value or "")):
        return "T1", "term", ""
    if ALLOWANCE.search(w) and (structure in PLAN_STRUCTURES or PLAN_WORDS.search(w + " " + (value or ""))):
        return "T2", "term", ""
    if structure in PLAN_STRUCTURES:
        return "T3", "term", ""
    return "unsure", "unsure", ""


_struct = {}


def structures(p):
    """Each key's structure, for the rules: a held entry's, an inventory entry's list; a statement has none."""
    if p not in _struct:
        m = {e["entry_id"]: e.get("structure", "") for e in he.entries(p)}
        for x in citable(p):
            k = skey(x)
            if k not in m and x.get("placement") == "inventory":
                m[k] = x.get("structure", "")
        _struct[p] = m
    return _struct[p]


# ---------------------------------------------------------------- the parts

def compute_parts():
    commits = commits_now()
    model = commits.split("sharrwah-knowledge-map@")[1].split(";")[0]
    out = []
    for part, p, kinds, own in PART_DEFS:
        asks = [a for a in ASKS if a.split("-")[0] in own]
        out.append({"part": part, "platform": p, "kinds": ";".join(kinds), "asks": ";".join(asks),
                    "commits": commits, "model": model, "state": "open"})
    return out


def part_row(part):
    rs = rows(PARTS_TSV)
    if not os.path.exists(PARTS_TSV):
        print(f"({rel(PARTS_TSV)} isn't written yet: {part} as `parts` computes it now)", file=sys.stderr)
        rs = compute_parts()
    for r in rs:
        if r["part"] == part:
            return r
    sys.exit(f"no part {part} in {rel(PARTS_TSV)}: its parts are {', '.join(r['part'] for r in rs)}")


def rows_file(pr):
    return os.path.join(QDIR, pr["platform"], f"{pr['part']}.tsv")


def part_file_rows(pr):
    path = rows_file(pr)
    return read_tsv(path, HEAD, []) if os.path.exists(path) else []


def cmd_parts(a):
    ps = compute_parts()
    for r in ps:
        own = sorted({x.split("-")[0] for x in semi(r["asks"])}, key=ALL.index)
        extra = [k for k in semi(r["kinds"]) if k not in own]
        print(f"{r['part']}\t{r['platform']}\t{len(semi(r['asks']))} asks of {', '.join(own)}"
              f"{'; found rows only for ' + ', '.join(extra) if extra else ''}\t{r['commits']}")
    print(f"{len(ps)} parts, {sum(len(semi(r['asks'])) for r in ps)} asks")
    if a.write:
        old = rows(PARTS_TSV)
        if any(r["state"] != "open" for r in old):
            sys.exit(f"{rel(PARTS_TSV)}: a part is checked or landed already: not rewritten")
        write_tsv(PARTS_TSV, PARTS_HEAD, ps)
        print(f"wrote {rel(PARTS_TSV)}")


def set_state(part, state):
    rs = rows(PARTS_TSV)
    for r in rs:
        if r["part"] == part:
            r["state"] = state
    write_tsv(PARTS_TSV, PARTS_HEAD, rs)


def cmd_mark(a):
    if not os.path.exists(PARTS_TSV):
        sys.exit(f"no {rel(PARTS_TSV)}: write the part list first (parts --write)")
    pr = part_row(a.part)
    if a.state == "checked":
        _, problems, _ = check_part(pr)
        if problems:
            sys.exit(f"{a.part}: {len(problems)} problems: run check --part {a.part}; not marked checked")
    set_state(a.part, a.state)
    print(f"{a.part}: {a.state}")


# ---------------------------------------------------------------- asks

def labelled_rows(p):
    """The model's quality rows of a platform with their labels: [(row, label row)], or None without labels.tsv."""
    if not os.path.exists(LABELS):
        return None
    lab = {r["row_id"]: r for r in rows(LABELS)}
    return [(r, lab[r["row_id"]]) for r in quality_rows(model_parts()) if r["platform"] == p and r["row_id"] in lab]


def s2_rows(p, caps_):
    """The second stage's landed rows on these capabilities: placement lines, s2-keys rows, outcome rows."""
    out = collections.defaultdict(list)
    for path in sorted(glob.glob(os.path.join(HELD, p, "placements-S2-*.tsv"))):
        for i, r in enumerate(rows(path), 2):
            if r.get("cap_id") in caps_:
                out[r["cap_id"]].append(f"{os.path.basename(path)} line {i}: {r['entry_id']} {r['supports']}"
                                        f"{' quality ' + r['quality'] if r.get('quality') else ''}: {clip(r['reading'], 160)}")
    for i, r in enumerate(rows(os.path.join(HELD, p, "s2-keys.tsv")), 2):
        if r.get("cap_id") in caps_ and r.get("batch", "").startswith("S2-"):
            out[r["cap_id"]].append(f"s2-keys.tsv line {i} ({r['batch']}): {r['key']} {r['supports']}: {clip(r['why'], 160)}")
    for i, r in enumerate(rows(os.path.join(HELD, p, "s2-outcomes.tsv")), 2):
        if r.get("subject") in caps_ and not r.get("superseded"):
            out[r["subject"]].append(f"s2-outcomes.tsv line {i} ({r['batch']}): {r['outcome']}: {clip(r['reading'], 160)}")
    return out


def cmd_asks(a):
    pr = part_row(a.part)
    p = pr["platform"]
    asks = semi(pr["asks"])
    kinds = semi(pr["kinds"])
    if a.left:
        done = {r["subject"].strip() for _, r in part_file_rows(pr)}
        left = [x for x in asks if x not in done]
        print(f"{len(left)} of {len(asks)} asks of {a.part} have no row in {rel(rows_file(pr))}")
        for x in left:
            print(f"   {x}: {ASKS[x]}")
        return
    caps = caps_table()
    cells = merged_cells()
    lab = labelled_rows(p)
    defaults = {c for k in kinds for c in KINDS[k][3] if c != PLATFORM}
    s2r = s2_rows(p, defaults)
    src = [r for r in rows(SOURCES_TSV) if r.get("platform") == p]
    print(f"{a.part} ({p}): {len(asks)} asks of the kinds {', '.join(k for k in kinds if any(x.startswith(k + '-') for x in asks))}"
          + (f"; for {', '.join(k for k in kinds if not any(x.startswith(k + '-') for x in asks))}, found rows only (their asks are another part's)"
             if any(not any(x.startswith(k + '-') for x in asks) for k in kinds) else ""))
    print(f"   commits fixed for the run: {pr['commits']}")
    if lab is None:
        print(f"   ({rel(LABELS)} isn't written yet: the model's rows of each kind print once the coordinator's labels propose --write has run)")
    if not os.path.exists(SOURCES_TSV):
        print(f"   ({rel(SOURCES_TSV)} isn't written yet: the places to read first are in the brief's \"Where your platform states its qualities\")")
    print()
    for k in kinds:
        name, iso, drives, dcaps, dtext = KINDS[k]
        own = [x for x in asks if x.startswith(k + "-")]
        print(f"== {k}: {name}. ISO/IEC 25010:2023 (a reading): {iso}. Drives: {', '.join(drives)}. Lands by default on: {dtext}")
        if not own:
            print(f"   found rows only, subject {k} or the ask's code: its asks are another part's")
        if lab is not None:
            mine = [(r, L) for r, L in lab if L["label"] == "quality" and L["kind"] == k]
            print(f"   the model's rows of {p} labelled {k}: {len(mine)}" + ("" if mine else " (none)"))
            for r, L in mine:
                print(f"      {r['cap_id']} {r['quality']}: {clip(r['value'], 140)} [{r['key']}; {r['row_id']}; {L['decided_by']}]")
        for c in [c for c in dcaps if c != PLATFORM]:
            cell = cells.get((c, p))
            print(f"   {c} {clip(caps.get(c, {}).get('capability', '?'), 110)}")
            if not cell:
                print(f"      {p}: no cell")
                continue
            print(f"      {p}: {cell['held']}, placed {cell.get('placed_as') or '-'}; reading: {clip(cell.get('reading', ''), 300)}")
            for x in s2r.get(c, []):
                print(f"      the second stage: {x}")
        if PLATFORM in dcaps:
            print(f"   platform: a quality whose words cover the whole platform or all of a store's data (QL-R2)")
        for r in src:
            if r.get("kind") == k:
                print(f"   read first: {r.get('place', '')}{' (' + r['note'] + ')' if r.get('note') else ''}")
        for x in own:
            print(f"   {x}: {ASKS[x]}")
        print()


# ---------------------------------------------------------------- the check

_codes = []


def source_codes():
    if not _codes:
        _codes.append({r["code"] for r in rows(os.path.join(MODEL, "seed", "km-source-types.tsv"))})
    return _codes[0]


def folds(s):
    return [v for _, v in quote_check.variants(s or "")]


def value_in(value, text):
    """Is value inside text, at one of quote_check's folding levels (as held, markup removed, case and diacritics)?"""
    return any(v and v in t for v, t in zip(folds(value), folds(text)))


def check_part(pr):
    """Tests a part's rows and notes: (rows, problems, notes)."""
    p, part = pr["platform"], pr["part"]
    problems, notes = [], []
    path = rows_file(pr)
    name = f"{part}.tsv"
    rs = read_tsv(path, HEAD, problems, name)
    asks = semi(pr["asks"])
    kinds = semi(pr["kinds"])
    commits = parse_commits(pr["commits"])
    caps = caps_table()
    cells = merged_cells()
    codes = source_codes()
    S = sources()
    cit = {skey(x): x for x in citable(p)}
    held = {e["entry_id"]: e for e in he.entries(p)}
    st = structures(p)
    by_subj = collections.defaultdict(list)
    seen = collections.defaultdict(list)
    for i, r in rs:
        w = f"{name} line {i}"
        r = {h: (v if h in ("quote", "reading") else v.strip()) for h, v in r.items()}
        for fld in LIST_FIELDS:
            if r[fld] and any(not x.strip() for x in r[fld].split(";")):
                problems.append(f"{w}: {fld} has an empty `;` piece")
        subj, oc, kind = r["subject"], r["outcome"], r["kind"]
        if not kind:
            problems.append(f"{w}: kind is the kind's code, on every row")
        elif kind not in KINDS:
            problems.append(f"{w}: kind is one of {', '.join(KINDS)}")
        elif kind not in kinds:
            problems.append(f"{w}: {kind} is not a kind of {part} ({', '.join(kinds)})")
        if subj in ASKS:
            if subj.split("-")[0] != kind:
                problems.append(f"{w}: subject {subj} is an ask of {subj.split('-')[0]}, and kind says {kind or 'nothing'}")
            only_found = subj not in asks
        elif subj in KINDS:
            if subj != kind:
                problems.append(f"{w}: subject {subj} is the kind's code, and kind says {kind or 'nothing'}")
            only_found = True
        else:
            problems.append(f"{w}: subject is an ask's code of {part} (asks --part {part}), or a kind's code alone for a quality no ask names")
            continue
        if oc not in OUTCOMES:
            problems.append(f"{w}: outcome is one of {', '.join(OUTCOMES)}")
            continue
        by_subj[subj].append((i, oc))
        if only_found and oc != "found":
            problems.append(f"{w}: {subj}: {'a kind' + chr(39) + 's code alone' if subj in KINDS else 'an ask of another part'} takes found rows only")
        cap = r["cap_id"]
        # found: what is measured, how, where
        if oc == "found":
            for fld, vals in (("form", FORMS), ("basis", BASES), ("holder", HOLDERS)):
                if r[fld] not in vals:
                    problems.append(f"{w}: {fld} is one of {', '.join(vals)}, on a found row")
            if not cap:
                problems.append(f"{w}: a found row's cap_id is a capability of the model, or platform")
            elif cap != PLATFORM and cap not in caps:
                problems.append(f"{w}: {cap} is not a capability of the model (merged/capabilities.tsv): name the narrowest one whose definition names the thing measured, or platform; a quality never makes a capability")
            elif cap != PLATFORM and (cap, p) not in cells:
                problems.append(f"{w}: {cap} has no cell for {p} in merged/cells.tsv")
            elif cap == PLATFORM and kind in KINDS and any(c != PLATFORM for c in KINDS[kind][3]):
                notes.append(f"{w}: {subj}: on the platform, not {' or '.join(c for c in KINDS[kind][3] if c != PLATFORM)}? ({kind} lands by default on {KINDS[kind][4]}; QL-R2: platform only where the quality's words cover the whole platform or all of a store's data)")
            q, v = r["quality"], r["value"]
            if not q:
                problems.append(f"{w}: quality says what is measured, in a few words, on a found row")
            elif ":" in q:
                problems.append(f"{w}: quality holds no colon: the model writes it as `<quality>: <value>`")
            else:
                pieces = [he.fold(re.sub(r"\s*\([^)]*\)", "", x)).strip(" .") for x in q.split(",")]
                if any(pieces) and all(x in he.MARKS for x in pieces if x):
                    problems.append(f"{w}: quality {q!r} is a mark of inclusion: never a quality (H-held.md, rule 5)")
            if not v:
                problems.append(f"{w}: value is the quote's own words that state the measure, verbatim, on a found row")
            elif ";" in v:
                problems.append(f"{w}: value holds no `;` (the model's quality field is `;`-separated): quote a shorter part of the passage")
            elif he.fold(v) in he.MARKS:
                problems.append(f"{w}: value {v!r} is a mark of inclusion: never a quality")
            if q:
                rule, label, _ = rule_of(q, v, st.get(r["source"], ""))
                if rule == "T1":
                    problems.append(f"{w}: {q!r} is a price, a fee, a rate charged, a trial or a discount: one of the plans' terms, never a quality (PLAN.md, Stage 4A; QL-R1). Write no row for it")
                elif rule in ("T2", "T3"):
                    notes.append(f"{w}: {subj}: {q!r}: a term? QL-R1: a quantity the merchant gets with a plan is a term; a limit the system enforces is a bound, its plans its scope")
            if not r["source_type"]:
                problems.append(f"{w}: source_type is the seed's code for the source ({', '.join(sorted(codes))})")
        else:
            for fld in ("form", "basis", "cap_id", "holder", "quality", "value"):
                if r[fld]:
                    problems.append(f"{w}: {fld} is for a found row only")
        if r["source_type"] and r["source_type"] not in codes:
            problems.append(f"{w}: source_type {r['source_type']!r} is not a code of seed/km-source-types.tsv ({', '.join(sorted(codes))})")
        # the source
        text = None
        if oc in CITING:
            src, loc, quote = r["source"], r["locator"], r["quote"]
            if not r["identifier"]:
                problems.append(f"{w}: {oc} names its identifier: the document's or page's title, the API's name, or the item's id")
            if not src:
                problems.append(f"{w}: {oc} cites its source, locator and quote, or an id already held")
            elif FILE_SOURCE.match(src) or re.search(r"@\d+(?:#piece-\d+)?$", src):
                if not loc or not quote.strip():
                    problems.append(f"{w}: a held file is cited with its locator and its quote")
                else:
                    problems += [f"{w}: {x}" for x in source_problems(p, src, loc, quote, commits, S)]
                    text = quote
                    if len(quote.strip()) < 30:
                        notes.append(f"{w}: the quote is under 30 characters: the shortest whole part that states the quality?")
            else:
                text = id_text(p, src, held, cit)
                if text is None:
                    problems.append(f"{w}: source {src!r} is neither `<repository>@<commit>:<path>`, `woocommerce-11.2.1:<path>`, nor an id held on {p} (a held entry, a concern-map statement's key, a placed inventory id)")
                elif plat_of(src) not in (p, None):
                    problems.append(f"{w}: {src} is {plat_of(src)}'s, not {p}'s")
                if loc or quote.strip():
                    problems.append(f"{w}: for an id already held, locator and quote are empty")
            if oc == "found" and r["value"] and text is not None and not value_in(r["value"], text):
                problems.append(f"{w}: value {clip(r['value'], 60)!r} is not inside {'the quote' if FILE_SOURCE.match(src) else 'the text of ' + src}: it is the quote's own words, verbatim")
            if oc == "found" and src:
                seen[(cap, he.fold(r["quality"]), he.fold(r["value"]), passage_key(src, loc, quote))].append(i)
        else:
            for fld in ("source", "locator", "quote"):
                if r[fld].strip():
                    problems.append(f"{w}: {fld} is for found, absent and unclear rows only")
        # what was read and searched
        if oc != "found":
            for fld in ("read", "searched"):
                if r[fld] in ("", "-"):
                    problems.append(f"{w}: {fld} lists what was {'read' if fld == 'read' else 'searched'}, `;`-separated")
            for x in semi(r["searched"]):
                if ":" not in x:
                    problems.append(f"{w}: each search is `<tool> <language>: <terms>` (or `held_index: <address>`): {clip(x, 60)!r}")
            if oc in ("not-found", "not-held", "absent") and p in ("salla", "zid") and not any(
                    "corpus_search" in x and ARABIC.search(x) for x in semi(r["searched"])):
                notes.append(f"{w}: {subj}: no corpus_search in Arabic: the held pages' Arabic was not searched")
        # capture and could_change
        cap_s, cc = r["capture"], r["could_change"]
        if oc == "not-held":
            pcs = [x.strip() for x in cap_s.split(";")]
            if cap_s == "none" or (cap_s.startswith("none") and not re.match(r"^none: \S", cap_s)):
                problems.append(f"{w}: capture is `none: <why>` only where no run can capture it at all, never none alone")
            elif not cap_s.startswith("none: ") and not (len(pcs) == 5 and all(pcs[:3]) and pcs[3].startswith("stop at ")
                                                          and pcs[4].startswith("needs:")):
                problems.append(f"{w}: capture is `<repository>; <instrument, or none>; <the run>; stop at <...>; needs: <...>` "
                                f"(the repository {' or '.join(CAPTURE_REPOS[p])}), or `none: <why>`")
            elif not cap_s.startswith("none: ") and pcs[0] not in CAPTURE_REPOS[p]:
                problems.append(f"{w}: capture's repository is {p}'s, {' or '.join(CAPTURE_REPOS[p])}, not {pcs[0]}")
            x = not_held_place(p, r)
            if x:
                problems.append(f"{w}: {x}")
            if not re.search(r"\bassum", r["reading"], re.I):
                notes.append(f"{w}: {subj}: not-held: that the place would state it is an assumption: does reading say so?")
        elif oc in ("unreadable", "unclear"):
            if not cap_s or cap_s == "none":
                problems.append(f"{w}: capture says {'the file and where it is held' if oc == 'unreadable' else 'what would settle it'}")
        elif cap_s:
            problems.append(f"{w}: capture is for not-held, unreadable and unclear rows only")
        if oc in ("not-held", "unreadable", "unclear"):
            vs = semi(cc)
            if not vs or not (vs in (["S"], ["no"]) or all(x in DECISIONS for x in vs)) or len(set(vs)) != len(vs):
                problems.append(f"{w}: could_change is one or more of {', '.join(DECISIONS)}, `;`-separated, or S, or no")
            elif kind in KINDS and all(x in DECISIONS for x in vs) and not set(vs) <= set(KINDS[kind][2]):
                notes.append(f"{w}: {subj}: could_change {cc}, where {kind} drives {', '.join(KINDS[kind][2])}: say why in reading")
        elif cc:
            problems.append(f"{w}: could_change is for not-held, unreadable and unclear rows only")
        if oc == "absent":
            notes.append(f"{w}: {subj}: absent: does reading say, in the platform's own words, what makes the list complete?")
        if not r["reading"].strip():
            problems.append(f"{w}: reading says why, as a reading")
        else:
            problems += [f"{w}: {x}" for x in reading_problems(p, r, text, S)]
    # coverage: one or more found, or exactly one other
    for x in asks:
        if x not in by_subj:
            problems.append(f"{x} has no row")
    for sj, xs in by_subj.items():
        ocs = [o for _, o in xs]
        if not (all(o == "found" for o in ocs) or len(ocs) == 1):
            problems.append(f"{sj}: its rows are one or more found, or exactly one of another outcome (lines {', '.join(str(i) for i, _ in xs)})")
    for k, ls in seen.items():
        if len(ls) > 1:
            problems.append(f"lines {', '.join(map(str, ls))}: the same quality, value and passage on {k[0]} twice: write it once")
    # the notes
    md = path[:-4] + ".md"
    if not os.path.exists(md):
        problems.append(f"no notes {part}.md")
    else:
        first = open(md, encoding="utf-8").readline()
        named = notes_commits(first)
        for repo, cs in commits.items():
            if repo == RELEASE:
                if RELEASE not in first:
                    problems.append(f"{part}.md: its first line names {RELEASE}")
            elif not any(same(c, x) for c in cs for x in named.get(repo, ())):
                problems.append(f"{part}.md: its first line names the commits fixed for the run: {repo}@{', '.join(sorted(cs))}")
    return rs, problems, notes


def cmd_check(a):
    pr = part_row(a.part)
    rs, problems, notes = check_part(pr)
    for n in notes:
        print("NOTE", n)
    for x in problems:
        print("PROBLEM", x)
    n = collections.Counter(r["outcome"].strip() for _, r in rs)
    f = collections.Counter(r["kind"].strip() for _, r in rs if r["outcome"].strip() == "found")
    print(f"{a.part}: {len(rs)} rows ({', '.join(f'{k} {v}' for k, v in sorted(n.items())) or 'none'}; found by kind: "
          f"{', '.join(f'{k or chr(45)} {v}' for k, v in sorted(f.items())) or 'none'}) for {len(semi(pr['asks']))} asks; "
          f"{len(notes)} notes, {len(problems)} problems")
    sys.exit(1 if problems else 0)


# ---------------------------------------------------------------- land

def model_quality_tuples():
    """The quality rows in the parts' qualities.tsv now: {(cap_id, platform, quality, value, key)}."""
    out = set()
    for _, _, d in model_parts():
        for r in rows(os.path.join(MODEL, "parts", d, "qualities.tsv")):
            out.add(tuple(r.get(f, "") for f in QUAL_FIELDS))
    return out


def batch_tuples(p, b):
    """The quality rows a QL batch's lines would write: from its placements and its s2-keys rows."""
    out = set()
    for r in rows(os.path.join(HELD, p, f"placements-{b}.tsv")):
        if r.get("placement") == "quality":
            for q in semi(r["quality"]):
                what, _, val = q.partition(":")
                for e in semi(r["entry_id"]):
                    out.add((r["cap_id"].strip(), p, what.strip(), val.strip() or what.strip(), e))
    for r in rows(os.path.join(HELD, p, "s2-keys.tsv")):
        if r.get("batch") == b:
            for q in semi(r["quality"]):
                what, _, val = q.partition(":")
                out.add((r["cap_id"].strip(), p, what.strip(), val.strip() or what.strip(), r["key"].strip()))
    return out


def applied(p, b, in_model):
    """Is batch b in the model: an evidence row held_amend.py wrote for it, or one of its quality rows?"""
    for path in glob.glob(os.path.join(MODEL, "parts", "*", "evidence.tsv")):
        for r in rows(path):
            if r.get("platform") == p and r.get("why", "").startswith(f"(the qualities pass, {b})"):
                return True
    return bool(batch_tuples(p, b) & in_model)


def cmd_land(a):
    p, X = a.platform, PREFIX[a.platform]
    main_b = f"QL-{X}"
    B = a.batch or main_b
    if not re.fullmatch(rf"{re.escape(main_b)}(?:-R\d+)?", B):
        sys.exit(f"the batch is {main_b}, or a correction batch {main_b}-R<n>")
    batches_tsv = os.path.join(HELD, "batches.tsv")
    listed = [r["batch"] for r in rows(batches_tsv)]
    if f"S2-{X}" not in listed and not any(b.startswith(f"S2-{X}-") for b in listed):
        sys.exit(f"S2-{X} isn't in held/batches.tsv: {p}'s qualities land after its second-stage batch (the coordinator's "
                 f"decision 1, briefs/QL-qualities-design.md, section 12)")
    prs = [r for r in rows(PARTS_TSV) if r["platform"] == p]
    if not prs:
        sys.exit(f"no part of {p} in {rel(PARTS_TSV)}")
    use = [r for r in prs if r["state"] in ("checked", "landed")]
    for r in prs:
        if r not in use:
            print(f"{r['part']}: {r['state']}: waits, and lands in turn once checked")
    if not use:
        sys.exit(f"no part of {p} is checked")
    earlier = [b for b in listed if b != B and (b == main_b or b.startswith(main_b + "-R"))]
    if B == main_b and earlier:
        sys.exit(f"{', '.join(earlier)} exist: land the next correction batch, --batch {main_b}-R{len(earlier) + 1}")
    if B != main_b and main_b not in listed:
        sys.exit(f"{main_b} is not landed yet: land it first")
    in_model = model_quality_tuples()
    if B in listed and applied(p, B, in_model):
        sys.exit(f"{B} was applied: its rows are in the model. Land what came after in a correction batch, "
                 f"--batch {main_b}-R{len([b for b in listed if b.startswith(main_b + '-R')]) + 1}")
    allrows = []
    for pr in use:
        rs, problems, _ = check_part(pr)
        if problems:
            sys.exit(f"{pr['part']}: {len(problems)} problems: run check --part {pr['part']}; nothing landed")
        allrows += [(pr, i, {h: (v if h in ("quote", "reading") else v.strip()) for h, v in r.items()}) for i, r in rs]
    base = {e["entry_id"] for e in he.entries(p, second=False)}
    s2_path = os.path.join(HELD, p, "entries-s2.tsv")
    old_s2 = rows(s2_path)
    old_by = {e["entry_id"]: e for e in old_s2}
    held = {e["entry_id"] for e in he.entries(p)}
    taken = {}
    for e in old_s2:
        if FILE_SOURCE.match(e["source"].strip()):
            taken[e["entry_id"]] = passage_key(e["source"].strip(), e["locator"], e["text"])
    ql_parts = {r["part"] for r in prs}
    # an entry another batch's placements scope keeps that scope: a QL line on it carries none (class_slice.py takes
    # an entry's scope from the first placements file that gives one)
    scoped = {}
    for path in sorted(glob.glob(os.path.join(HELD, p, "placements-*.tsv"))):
        b = re.search(r"placements-(.+)\.tsv$", path).group(1)
        if b in listed and not b.startswith("QL-"):
            for r in rows(path):
                for e in semi(r["entry_id"]):
                    if r.get("scope") and e not in scoped:
                        scoped[e] = b
    # what earlier QL batches of the platform hold, which a correction batch leaves out
    e_tuples = set()
    for b in earlier:
        e_tuples |= batch_tuples(p, b)
    caps = caps_table()
    cells = merged_cells()
    tuples_now = []                                     # every found row's quality row, for the ids
    entries, lines, keys, plat, labels_new = collections.OrderedDict(), collections.OrderedDict(), [], collections.OrderedDict(), []
    outcomes, captures, cover, not_landed, became, kept_scope = [], [], collections.OrderedDict(), [], set(), []
    lengthened = []
    for pr, i, r in allrows:
        part, ref = pr["part"], f"qualities/{p}/{pr['part']}.tsv line {i}"
        subj, oc, src, kind = r["subject"], r["outcome"], r["source"], r["kind"]
        ck = (subj, part)
        c = cover.setdefault(ck, {"platform": p, "ask": subj, "kind": kind, "result": oc, "found": 0, "part": part,
                                  "lines": [], "commits": s2.platform_commits(p, pr)})
        c["lines"].append(str(i))
        if oc == "found":
            c["found"] += 1
        if r["capture"]:
            captures.append({"platform": p, "batch": B, "part": part, "line": str(i), "subject": subj, "kind": kind,
                             "outcome": oc, "could_change": r["could_change"], "capture": r["capture"], "read": r["read"],
                             "searched": r["searched"], "reading": r["reading"]})
        eid = None
        if oc in CITING and FILE_SOURCE.match(src):
            eid, n = passage_id(p, src, r["locator"], r["quote"], base, taken)
            if n > 8:
                lengthened.append(f"{ref}: {eid} ({n} digits)")
            if eid not in entries:
                if eid in old_by:
                    e = dict(old_by[eid])
                    if part not in e["labels"].split(","):
                        e["labels"] = ",".join(x for x in e["labels"].split(",") + [part] if x)
                    entries[eid] = e
                else:
                    entries[eid] = {"entry_id": eid, "structure": "second-stage", "labels": part, "source": src,
                                    "locator": r["locator"], "section": r["identifier"], "text": r["quote"]}
            elif part not in entries[eid]["labels"].split(","):
                entries[eid]["labels"] += "," + part
        elif oc in CITING:
            eid = src
        if oc != "found":
            outcomes.append({"platform": p, "batch": B, "subject": subj, "kind": kind, "outcome": oc, "part": part,
                             "line": str(i), "commits": s2.platform_commits(p, pr), "read": clip(r["read"], CLIP),
                             "searched": clip(r["searched"], CLIP), "capture": r["capture"],
                             "could_change": r["could_change"], "reading": " ".join(r["reading"].split())})
            continue
        cap, q, v = r["cap_id"], r["quality"].strip(), r["value"].strip()
        t = (cap, p, q, v, eid)
        tuples_now.append(t)
        reading = " ".join(r["reading"].split())
        labels_new.append({"t": t, "label": "quality", "kind": kind, "form": r["form"], "basis": r["basis"],
                           "holder": r["holder"], "date": r["date"], "source_type": r["source_type"],
                           "decided_by": f"{part} line {i}", "reading": reading})
        if cap == PLATFORM:
            k = (q, v, eid)
            if k not in plat:
                plat[k] = {"cap_id": PLATFORM, "platform": p, "quality": q, "value": v, "key": eid, "kind": kind,
                           "form": r["form"], "basis": r["basis"], "holder": r["holder"], "scope": r["scope"],
                           "date": r["date"], "source_type": r["source_type"], "part": part, "line": str(i)}
            continue
        if t in in_model:
            not_landed.append(f"{ref}: {cap} {q}: {clip(v, 60)} ({eid}) is in the model's qualities already: it takes its label only")
            continue
        if t in e_tuples:
            continue
        if cells[(cap, p)]["held"] != "statements":
            became.add(cap)
        qual = f"{q}: {v}"
        if eid in held or eid in entries:
            scope = r["scope"]
            if scope and eid in scoped:
                kept_scope.append(f"{ref}: {eid} keeps the scope {scoped[eid]} gave it; this row's scope ({scope}) is in its reading")
                scope = ""
            k = (eid, cap, qual)
            if k in lines:
                lines[k]["refs"].append(ref)
                continue
            lines[k] = {"entry_id": eid, "placement": "quality", "cap_id": cap, "supports": "shows", "scope": scope,
                        "terms": "", "filler": "", "quality": qual,
                        "reading": reading + (f" (scope as the row states it: {r['scope']})" if r["scope"] and not scope else ""),
                        "refs": [ref]}
        else:
            if any(x["cap_id"] == cap and x["key"] == eid and x["quality"] == qual for x in keys):
                continue
            keys.append({"batch": B, "cap_id": cap, "platform": p, "supports": "shows", "key": eid,
                         "why": f"(the qualities pass, {B}, {part} line {i}) {reading}", "terms": "", "filler": "",
                         "quality": qual})
    # an entry another batch's placements name, or the model's evidence cites, is never dropped
    protected = set()
    for path in glob.glob(os.path.join(MODEL, "parts", "*", "evidence.tsv")):
        protected |= {r["key"] for r in rows(path) if r.get("platform") == p}
    for path in glob.glob(os.path.join(HELD, p, "placements-*.tsv")):
        if os.path.basename(path) != f"placements-{B}.tsv":
            for r in rows(path):
                protected |= set(semi(r["entry_id"]))
    protected |= {r["key"] for r in rows(PLATFORM_QUAL) if r.get("platform") == p} - {x[2] for x in plat}
    ql_only = lambda e: all(x in ql_parts for x in semi(e["labels"].replace(",", ";")))
    dropped = [e["entry_id"] for e in old_s2 if ql_only(e) and e["entry_id"] not in entries]
    if set(dropped) & protected:
        sys.exit(f"{p}: the landing would drop {len(set(dropped) & protected)} entries of entries-s2.tsv that a placements "
                 f"file or the model names, such as {sorted(set(dropped) & protected)[:3]}: refused")
    # the labels: every found row's, by the ids the merge gives (the parts' rows, platform.tsv's rows as landed now)
    others_plat = [r for r in rows(PLATFORM_QUAL) if r.get("platform") != p]
    model_rows = [r for r in quality_rows(model_parts()) if r["part"] != "QL"]
    all_t = [tuple(r[f] for f in QUAL_FIELDS) for r in model_rows] + [tuple(r.get(f, "") for f in QUAL_FIELDS) for r in others_plat] + tuples_now
    ids_ = row_ids(all_t)
    old_lab = rows(LABELS)
    in_now = {ids_[t] for t in all_t}
    mine = {}
    for L in labels_new:
        cap, pp, q, v, k = L["t"]
        mine[ids_[L["t"]]] = {"row_id": ids_[L["t"]], "cap_id": cap, "platform": pp, "quality": q, "key": k,
                              **{h: L[h] for h in ("label", "kind", "form", "basis", "holder", "date", "source_type",
                                                   "decided_by", "reading")}}
    relabel, lab_out = [], []
    model_ids = {ids_[tuple(r[f] for f in QUAL_FIELDS)] for r in model_rows}
    for L in old_lab:
        rid = L["row_id"]
        if rid in mine:
            if L["decided_by"] == "review" and L["label"] != "quality":
                relabel.append(f"{rid} ({L['cap_id']} {L['quality']}): review said {L['label']}, {mine[rid]['decided_by']} says quality")
            continue
        ours = L.get("platform") == p and any(L.get("decided_by", "").startswith(x + " line ") for x in ql_parts)
        if ours and rid not in model_ids:
            continue                     # a QL label of a row no current row gives, and not in the model: dropped
        lab_out.append({h: L.get(h, "") for h in LABELS_HEAD})
    lab_out += list(mine.values())
    batch_ids = list(dict.fromkeys(v["entry_id"] for v in lines.values()))
    # the counts
    n = collections.Counter(r["outcome"] for _, _, r in allrows)
    fk = collections.Counter(r["kind"] for _, _, r in allrows if r["outcome"] == "found")
    commits = list(dict.fromkeys(x for pr in use for x in semi(pr["commits"])))
    print(f"{p}, {B}: {len(allrows)} rows from {', '.join(pr['part'] for pr in use)} ({', '.join(f'{k} {v}' for k, v in sorted(n.items()))})")
    print(f"   found by kind: {', '.join(f'{k} {v}' for k, v in sorted(fk.items())) or 'none'}")
    print(f"   {len([e for e in entries if e not in old_by])} new entries in entries-s2.tsv ({len([e for e in entries if e in old_by])} "
          f"already there), {len(batch_ids)} in the batch, {len(lines)} quality lines, {len(keys)} rows to s2-keys.tsv, "
          f"{len(plat)} platform-wide rows, {len(mine)} labels, {len(outcomes)} outcomes, {len(captures)} capture leads, "
          f"{len(not_landed)} rows not placed")
    print(f"   cells that would become held: {', '.join(sorted(became)) or 'none'}")
    for x in lengthened:
        print(f"   COLLISION {x}")
    for x in kept_scope:
        print(f"   SCOPE {x}")
    for x in relabel:
        print(f"   RELABEL {x}")
    for x in not_landed:
        print(f"   NOT PLACED {x}")
    if a.dry_run:
        return
    keep = [e for e in old_s2 if e["entry_id"] not in entries and not ql_only(e)]
    write_tsv(s2_path, he.E_HEAD, keep + [e for e in entries.values() if e["entry_id"] not in {k["entry_id"] for k in keep}])
    os.makedirs(os.path.join(HELD, "batches"), exist_ok=True)
    with open(os.path.join(HELD, "batches", f"{B}.txt"), "w", encoding="utf-8") as f:
        f.write("".join(x + "\n" for x in batch_ids))
    raw = open(batches_tsv, encoding="utf-8").read().rstrip("\n").split("\n") if os.path.exists(batches_tsv) else ["batch\tplatform\tentries\tstructures"]
    row = f"{B}\t{p}\t{len(batch_ids)}\tsecond-stage"
    raw = [row if l.split("\t")[0] == B else l for l in raw]
    if row not in raw:
        raw.append(row)
    open(batches_tsv, "w", encoding="utf-8").write("\n".join(raw) + "\n")
    pl = [dict(v, reading=f"{v['reading']} (the qualities pass: {'; '.join(v['refs'])})") for v in lines.values()]
    write_tsv(os.path.join(HELD, p, f"placements-{B}.tsv"), he.P_HEAD, pl)
    kp = os.path.join(HELD, p, "s2-keys.tsv")
    write_tsv(kp, KEYS_HEAD, keep_others(kp, KEYS_HEAD, "batch", B) + keys)
    write_tsv(PLATFORM_QUAL, PLATFORM_HEAD, others_plat + list(plat.values()))
    write_tsv(LABELS, LABELS_HEAD, lab_out)
    write_tsv(OUTCOMES_TSV, OUT_HEAD, keep_others(OUTCOMES_TSV, OUT_HEAD, "batch", B) + outcomes)
    first = {(r["part"], r["subject"], r["capture"]): r["batch"] for r in rows(CAPTURES_TSV) if r.get("platform") == p}
    for c in captures:
        c["batch"] = first.get((c["part"], c["subject"], c["capture"]), B)
    write_tsv(CAPTURES_TSV, CAPTURES_HEAD, keep_others(CAPTURES_TSV, CAPTURES_HEAD, "platform", p) + captures)
    cov = [dict(c, lines=";".join(c["lines"]), found=str(c["found"]), result="found" if c["found"] else c["result"]) for c in cover.values()]
    write_tsv(COVERAGE_TSV, COVER_HEAD, keep_others(COVERAGE_TSV, COVER_HEAD, "platform", p) + cov)
    md = [" ".join(x.replace(";", " ") for x in commits), "",
          f"# Notes: the qualities pass, {p}, batch {B} (written by method/ql_qualities.py land)", "",
          f"Parts landed: {', '.join(pr['part'] for pr in use)}. Still open: {', '.join(r['part'] for r in prs if r not in use) or 'none'}.", "",
          "## Counts by outcome", ""]
    md += [f"- {k}: {v}" for k, v in sorted(n.items())]
    md += ["", "## Found rows by kind", ""] + ([f"- {k}: {v}" for k, v in sorted(fk.items())] or ["- none"])
    md += ["", f"{len(batch_ids)} entries in the batch, {len(lines)} quality lines, {len(keys)} rows to s2-keys.tsv, "
           f"{len(plat)} rows of qualities/platform.tsv.", "",
           "## Rows not placed, and why", ""] + ([f"- {x}" for x in not_landed] or ["- none"])
    md += ["", "## Scopes kept from another batch", ""] + ([f"- {x}" for x in kept_scope] or ["- none"])
    md += ["", "## Rows sent to s2-keys.tsv", ""] + ([f"- {k['why'].split(')')[0][1:]}: {k['key']} on {k['cap_id']}" for k in keys] or ["- none"])
    open(os.path.join(HELD, p, f"notes-{B}.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    for pr in use:
        if pr["state"] != "landed":
            set_state(pr["part"], "landed")
    print(f"wrote held/{p}/entries-s2.tsv, held/batches/{B}.txt, held/batches.tsv, held/{p}/placements-{B}.tsv, "
          f"notes-{B}.md, s2-keys.tsv, qualities/platform.tsv, labels.tsv, outcomes.tsv, captures.tsv, coverage.tsv; then: "
          f"held_entries.py check --platform {p} --batch {B}; held_amend.py plan --platform {p} --batch {B}")


# ---------------------------------------------------------------- labels

KEEP_DECIDED = re.compile(r"^(?:review$|QL-)")


def propose():
    """[(row, label row)] for every model row: the rules' labels, a review's or a part's kept."""
    old = {r["row_id"]: r for r in rows(LABELS)}
    out = []
    for r in quality_rows(model_parts()):
        L = old.get(r["row_id"])
        if L and KEEP_DECIDED.match(L.get("decided_by", "")):
            out.append((r, {h: L.get(h, "") for h in LABELS_HEAD}))
            continue
        rule, label, kind = rule_of(r["quality"], r["value"], structures(r["platform"]).get(r["key"], ""))
        out.append((r, {"row_id": r["row_id"], "cap_id": r["cap_id"], "platform": r["platform"], "quality": r["quality"],
                        "key": r["key"], "label": label, "kind": kind, "form": "", "basis": "", "holder": "", "date": "",
                        "source_type": "", "decided_by": f"rule:{rule}", "reading": ""}))
    return out


def counts(ls):
    by_rule = collections.Counter(L["decided_by"] if L["decided_by"].startswith("rule:") or L["decided_by"] == "review"
                                  else "QL part" for _, L in ls)
    by_label = collections.Counter(L["label"] for _, L in ls)
    by_kind = collections.Counter(L["kind"] for _, L in ls if L["label"] == "quality")
    unsure = collections.Counter(r["platform"] for r, L in ls if L["label"] == "unsure")
    rule_label = collections.Counter((L["decided_by"], L["label"]) for _, L in ls)
    by_plat = collections.Counter((r["platform"], L["label"]) for r, L in ls)
    out = [f"{len(ls)} rows: " + ", ".join(f"{k} {v}" for k, v in sorted(by_label.items())),
           "   by rule: " + ", ".join(f"{k} {v}" for k, v in sorted(by_rule.items())),
           "   by rule and label: " + ", ".join(f"{k}={l} {v}" for (k, l), v in sorted(rule_label.items()) if not k.startswith("QL-")),
           "   quality by kind: " + (", ".join(f"{k or '-'} {v}" for k, v in sorted(by_kind.items())) or "none"),
           "   unsure by platform: " + (", ".join(f"{k} {v}" for k, v in sorted(unsure.items())) or "none"),
           "   by platform: " + "; ".join(f"{p} " + ", ".join(f"{l} {by_plat[(p, l)]}" for l in ("quality", "term", "other", "unsure") if by_plat[(p, l)])
                                         for p in PLATFORMS if any(by_plat[(p, l)] for l in ("quality", "term", "other", "unsure")))]
    return out


def cmd_labels(a):
    if a.action == "propose":
        ls = propose()
        for x in counts(ls):
            print(x)
        if a.write:
            write_tsv(LABELS, LABELS_HEAD, [L for _, L in ls])
            print(f"wrote {rel(LABELS)}")
        else:
            print(f"(nothing written: --write writes {rel(LABELS)})")
        return
    if a.action == "clear":
        if not a.rule:
            sys.exit("labels clear --rule R (Q1, T1, T2, T3 or unsure)")
        old = rows(LABELS)
        keep = [r for r in old if r.get("decided_by") != f"rule:{a.rule}"]
        write_tsv(LABELS, LABELS_HEAD, keep)
        print(f"removed {len(old) - len(keep)} labels of rule:{a.rule} from {rel(LABELS)}")
        return
    if not os.path.exists(LABELS):
        sys.exit(f"no {rel(LABELS)}: labels propose --write first")
    lab = {r["row_id"]: r for r in rows(LABELS)}
    qr = quality_rows(model_parts())
    if a.action == "review":
        un = [r for r in qr if lab.get(r["row_id"], {}).get("label") == "unsure"]
        lo, hi = max(1, a.from_ or 1), min(len(un), a.to or len(un))
        caps = caps_table()
        print(f"{len(un)} unsure rows; {lo} to {hi}. Write qualities/labels-review.tsv: {' '.join(REVIEW_HEAD)} "
              f"(label {', '.join(LABEL_VALUES)}; kind and form for a quality)")
        for n in range(lo, hi + 1):
            r = un[n - 1]
            print(f"[{n}/{len(un)}] {r['row_id']} {r['cap_id']} ({clip(caps.get(r['cap_id'], {}).get('capability', 'platform'), 80)}) "
                  f"{r['platform']}: {r['quality']}: {clip(r['value'], 200)} [{r['key']}; {structures(r['platform']).get(r['key'], '') or 'a statement'}; {r['part']}]")
        return
    if a.action == "apply-review":
        problems = []
        rv = read_tsv(REVIEW_TSV, REVIEW_HEAD, problems)
        for i, r in rv:
            r = {h: v.strip() for h, v in r.items()}
            w = f"labels-review.tsv line {i}"
            if r["row_id"] not in lab:
                problems.append(f"{w}: {r['row_id']} names no label of labels.tsv")
                continue
            if r["label"] not in LABEL_VALUES:
                problems.append(f"{w}: label is one of {', '.join(LABEL_VALUES)}")
            if r["label"] == "quality" and (r["kind"] not in KINDS or r["form"] not in FORMS):
                problems.append(f"{w}: a quality takes a kind ({', '.join(KINDS)}) and a form ({', '.join(FORMS)})")
            if r["label"] != "quality" and (r["kind"] or r["form"]):
                problems.append(f"{w}: kind and form are for a quality only")
            if not r["reading"]:
                problems.append(f"{w}: reading says why, as a reading")
        if problems:
            for x in problems:
                print("PROBLEM", x)
            sys.exit(1)
        for _, r in rv:
            L = lab[r["row_id"].strip()]
            if KEEP_DECIDED.match(L["decided_by"]) and L["decided_by"] != "review":
                print(f"KEPT {L['row_id']}: decided by {L['decided_by']}, not by the review")
                continue
            L.update(label=r["label"].strip(), kind=r["kind"].strip(), form=r["form"].strip(), decided_by="review",
                     reading=" ".join(r["reading"].split()))
        write_tsv(LABELS, LABELS_HEAD, list(lab.values()))
        print(f"{len(rv)} review labels taken into {rel(LABELS)}")
        return
    # check
    problems = []
    ids_ = {r["row_id"] for r in qr}
    for r in qr:
        L = lab.get(r["row_id"])
        if not L:
            problems.append(f"{r['row_id']} ({r['cap_id']}@{r['platform']} {r['quality']}, {r['part']}) has no label")
        elif L["label"] not in LABEL_VALUES:
            problems.append(f"{r['row_id']} ({r['cap_id']}@{r['platform']} {r['quality']}) is {L['label']}: settle it (labels review)")
        elif L["label"] == "quality" and L["kind"] not in KINDS:
            problems.append(f"{r['row_id']}: a quality without its kind")
    for rid, L in lab.items():
        if rid not in ids_:
            problems.append(f"the label {rid} ({L['cap_id']}@{L['platform']} {L['quality']}, {L['decided_by']}) names no row: its row was corrected or removed")
    mq, mt = rows(os.path.join(MERGED, "qualities.tsv")), rows(os.path.join(MERGED, "terms.tsv"))
    if not os.path.exists(os.path.join(MERGED, "terms.tsv")) or "row_id" not in (mq[0] if mq else {}):
        problems.append("merged/qualities.tsv and merged/terms.tsv aren't the labelled merge: run class_merge.py")
    else:
        merged_t = collections.Counter(tuple(r[f] for f in QUAL_FIELDS) + (r["part"],) for r in mq + mt)
        want = collections.Counter(tuple(r[f] for f in QUAL_FIELDS) + (r["part"],) for r in qr)
        if merged_t != want:
            problems.append(f"merged/qualities.tsv and merged/terms.tsv hold {sum(merged_t.values())} rows, the parts and "
                            f"platform.tsv {sum(want.values())}; {sum((want - merged_t).values())} rows missing, "
                            f"{sum((merged_t - want).values())} extra: run class_merge.py")
        wrong = [r["row_id"] for r in mt if lab.get(r["row_id"], {}).get("label") != "term"] + \
                [r["row_id"] for r in mq if lab.get(r["row_id"], {}).get("label") == "term"]
        if wrong:
            problems.append(f"{len(wrong)} merged rows sit in the other file than their label says, such as {wrong[0]}: run class_merge.py")
    for x in counts([(r, lab[r["row_id"]]) for r in qr if r["row_id"] in lab]):
        print(x)
    for x in problems[:200]:
        print("PROBLEM", x)
    if len(problems) > 200:
        print(f"... and {len(problems) - 200} more")
    print(f"{len(qr)} rows, {len(lab)} labels; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("asks", help="the part's asks, kind by kind")
    s.add_argument("--part", required=True); s.add_argument("--left", action="store_true"); s.set_defaults(f=cmd_asks)
    s = sub.add_parser("check", help="tests a part's rows and notes")
    s.add_argument("--part", required=True); s.set_defaults(f=cmd_check)
    s = sub.add_parser("parts", help="the parts; --write writes qualities/parts.tsv")
    s.add_argument("--write", action="store_true"); s.set_defaults(f=cmd_parts)
    s = sub.add_parser("mark", help="sets a part's state")
    s.add_argument("--part", required=True); s.add_argument("--state", choices=["checked", "open"], required=True)
    s.set_defaults(f=cmd_mark)
    s = sub.add_parser("land", help="lands a platform's checked parts into its batch QL-<XX>")
    s.add_argument("--platform", choices=PLATFORMS, required=True); s.add_argument("--batch")
    s.add_argument("--dry-run", action="store_true"); s.set_defaults(f=cmd_land)
    s = sub.add_parser("labels", help="the labels of the model's quality rows")
    s.add_argument("action", choices=["propose", "review", "apply-review", "check", "clear"])
    s.add_argument("--write", action="store_true"); s.add_argument("--rule")
    s.add_argument("--from", dest="from_", type=int); s.add_argument("--to", type=int)
    s.set_defaults(f=cmd_labels)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
