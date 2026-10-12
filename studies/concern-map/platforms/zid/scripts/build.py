# Build the Q1 Zid output files in final/ from the inventory, the concerns and the statement modules.
# Usage: python3 -I build.py   (run from anywhere; paths are fixed below)
import csv, json, os, re, sys
from collections import Counter, defaultdict
Z = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid"
sys.path.insert(0, os.path.join(Z, "scripts"))
import stlib, zverify, concerns
import st_money, st_legal, st_rest, st_more  # noqa: F401  (they fill stlib.STATEMENTS and stlib.GAPS)

F = os.path.join(Z, "fetched"); OUT = os.path.join(Z, "final"); os.makedirs(OUT, exist_ok=True)
ACCESSED = "2026-10-12"
reg = json.load(open(os.path.join(F, "registry.json"), encoding="utf-8"))
inv = json.load(open(os.path.join(F, "inventory.json"), encoding="utf-8"))

def clean(s):
    return re.sub(r"\s+", " ", (s or "").replace("\t", " ").replace("\r", " ").replace("\n", " ")).strip()

def cut(text, n=300):
    """A verbatim piece of at most n characters, cut at a space, kept clear of ellipses."""
    t = clean(text)
    for e in ("...", "…"):
        if e in t:
            i = t.index(e)
            t = t[:i].rstrip() if i >= 40 else t[i + len(e):].lstrip()
    if len(t) <= n: return t
    c = t[:n]; i = c.rfind(" ")
    if i > n // 2: c = c[:i]
    return c.rstrip(" ,;:،")

problems = []
cites = {}          # (url, quote) -> cite row
def cite(url, quote, locator):
    q = cut(quote)
    key = (url, q)
    if key in cites: return cites[key]["cite_id"]
    r = reg.get(url)
    if not r:
        problems.append(f"no registry entry for {url}"); r = dict(files=[], access="", date="", basis="")
    cid = f"ZD-S-{len(cites) + 1:04d}"
    cites[key] = dict(cite_id=cid, source=url, locator=clean(locator), quote=q, source_date=r["date"],
                      date_basis=r["basis"], accessed=ACCESSED, access_path=r["access"], _files=r["files"])
    return cid

# ---- inventory ----
inv_rows = []; con_inv = defaultdict(list)
for e in inv:
    cids, oos = concerns.map_entry(e)
    c = cite(e["url"], e["quote"], e["locator"])
    inv_rows.append([e["inv_id"], e["list"], clean(e["entry"]), c, ", ".join(cids), clean(oos)])
    for x in cids: con_inv[x].append(e["inv_id"])

# ---- concerns ----
con_rows = []
for cid, name, terms, note in concerns.CONCERNS:
    ids = con_inv.get(cid, [])
    if not ids and not note.startswith("Not in the platform's lists:"):
        problems.append(f"{cid} has no inventory entries and its split_note doesn't start with the required words")
    con_rows.append([cid, clean(name), clean(terms), ", ".join(ids), clean(note)])
known = set(concerns.CIDS)

# ---- statements and gaps ----
st_rows = []
for s in stlib.STATEMENTS:
    if s["c"] not in known: problems.append(f"statement for unknown concern {s['c']}")
    c = cite(s["url"], s["quote"] or s["text"], s["loc"])
    st_rows.append([s["c"], s["p"], clean(s["structure"]), clean(s["ident"]), clean(s["text"]), clean(s["scope"]), c, clean(s["note"])])
gp_rows = []
for g in stlib.GAPS:
    if g["c"] not in known: problems.append(f"gap for unknown concern {g['c']}")
    gp_rows.append([g["c"], g["p"], clean(g["what"]), clean(g["means"]), g["who"], clean(g["route"]), clean(g["why"]), g["kind"]])

# ---- verify every citation quote and statement against the working copies ----
by_id = {r["cite_id"]: r for r in cites.values()}
for r in cites.values():
    res = zverify.check(r["quote"], r["_files"]) if r["_files"] else "no files"
    if not res.startswith("found"): problems.append(f"quote not found: {r['cite_id']} {r['source'][:60]} | {r['quote'][:80]}")
    if "..." in r["quote"] or "…" in r["quote"]: problems.append(f"ellipsis in {r['cite_id']}")
for row in st_rows:
    r = by_id[row[6]]
    res = zverify.check(row[4], r["_files"])
    if not res.startswith("found"): problems.append(f"statement not found: {row[0]} {row[1]} | {row[4][:80]}")

# ---- coverage ----
P = ["where", "decides", "responsible", "boundary", "reason"]
cov = defaultdict(lambda: [0, 0])
for row in st_rows: cov[(row[0], row[1])][0] += 1
for row in gp_rows: cov[(row[0], row[1])][1] += 1
for c in concerns.CIDS:
    for p in P:
        if cov[(c, p)] == [0, 0]: problems.append(f"no statement and no gap: {c}/{p}")

# ---- not reached ----
nr_rows = [
 ["https://partner.zid.sa/partnership-details",
  "HTTP 200; the page renders the Partner Dashboard login (redirect to https://partner.zid.sa/login?redirect=%2F); no account was used",
  "ZD-C-070 Zid App Market (responsible); ZD-C-022 App Market subscriptions and partner payouts",
  "The partnership agreement that docs.zid.sa says app partners complete before creating a public app: the contracting Zid entity, the governing law, liability, payout and revenue-share clauses"],
 ["https://help-partner.zid.sa/en/",
  "HTTP 200. The links App Partner terms, Theme Partner terms and Theme commercial policy on zid.sa/en/partners/developers/blog/partner-payouts/ all point to this partner help centre home, which shows no agreement text. Its collections Getting Started, FAQs, App Support and Theme Support list no article with these agreements; the article Create your partner account says partnership details are submitted to receive the agreement",
  "ZD-C-070 Zid App Market and ZD-C-076 Theme Market and themes (responsible); ZD-C-022 App Market subscriptions and partner payouts",
  "The text of the App Partner terms, the Theme Partner terms and the Theme commercial policy, with their dates and the parties named"],
 ["https://web.zid.sa/login",
  "Not attempted: the merchant dashboard needs a store account, and the brief allows no accounts",
  "Every gap of kind 'observation needed' that names a dashboard journey (settings, plan limits, staff roles)",
  "The dashboard sections and settings as they appear on each plan; the limits a plan sets; the permission each staff role needs"],
 ["https://partner.zid.sa/login",
  "Not attempted beyond the page above: the partner dashboard needs a partner account",
  "ZD-C-071 OAuth authorization and app scopes; ZD-C-072 Webhooks; ZD-C-074 Private apps and direct API access",
  "The scope list offered when an app is created, the webhook management screen, and the app review states as the dashboard shows them"],
]

# ---- write ----
def write(name, header, rows):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            vals = [clean(str(v)) for v in r]
            for v in vals:
                if "\t" in v or "\n" in v: problems.append(f"{name}: tab or newline in a field")
            f.write("\t".join(vals) + "\n")
write("inventory.tsv", ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"], inv_rows)
write("concerns.tsv", ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"], con_rows)
cit_rows = [[r[k] for k in ("cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path")]
            for r in sorted(cites.values(), key=lambda r: r["cite_id"])]
write("citations.tsv", ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"], cit_rows)
write("statements.tsv", ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note"], st_rows)
write("gaps.tsv", ["concern_id", "placement", "what_would_show_it", "means", "who_can", "route", "why_not_held", "gap_kind"], gp_rows)
write("not-reached.tsv", ["url", "status", "needed_for", "what_to_look_for"], nr_rows)

# ---- stats ----
stats = dict(inventory=len(inv_rows), concerns=len(con_rows), citations=len(cit_rows), statements=len(st_rows), gaps=len(gp_rows),
             not_reached=len(nr_rows), lists=Counter(r[1] for r in inv_rows), out_of_scope=sum(1 for r in inv_rows if not r[4]))
per = {}
for p in P:
    s = sum(1 for c in concerns.CIDS if cov[(c, p)][0]); g = sum(1 for c in concerns.CIDS if cov[(c, p)][1])
    b = sum(1 for c in concerns.CIDS if cov[(c, p)][0] and cov[(c, p)][1]); go = sum(1 for c in concerns.CIDS if cov[(c, p)][1] and not cov[(c, p)][0])
    per[p] = dict(with_statement=s, with_gap=g, both=b, gap_only=go, statements=sum(1 for r in st_rows if r[1] == p), gaps=sum(1 for r in gp_rows if r[1] == p))
stats["per_placement"] = per
stats["gap_kind"] = Counter(r[7] for r in gp_rows); stats["who_can"] = Counter(r[4] for r in gp_rows)
stats["kind_by_who"] = Counter(f"{r[7]} / {r[4]}" for r in gp_rows)
stats["access_path"] = Counter(r[7] for r in cit_rows)
stats["sources"] = len({r[1] for r in cit_rows})
json.dump(stats, open(os.path.join(Z, "check", "build-stats.json") if os.path.isdir(os.path.join(Z, "check")) else os.path.join(F, "build-stats.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps(stats, ensure_ascii=False, indent=1))
print("problems:", len(problems))
for x in problems[:80]: print(" ", x)
