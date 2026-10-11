# Writes final/notes.md: the first run's notes as they stand, then the re-pass section with counts taken from final/.
# Usage: python3 -I write_notes.py CAPTURE_RUN_DIR
import sys, os, csv, collections, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

run_dir = sys.argv[1]
F = f"{SP}/final"
st, gp = rd(f"{F}/statements.tsv"), rd(f"{F}/gaps.tsv")
inv, con, cit, nr, log = rd(f"{F}/inventory.tsv"), rd(f"{F}/concerns.tsv"), rd(f"{F}/citations.tsv"), rd(f"{F}/not-reached.tsv"), rd(f"{F}/review-log.tsv")
newst = rd(f"{SP}/work/new_statements.tsv")
fetchlog = rd(f"{SP}/fetched/log.tsv")
man = rd(f"{run_dir}/manifest.tsv")
have = set((r["concern_id"], r["placement"]) for r in st)
ncon = len(con)
cells = {p: sum(1 for c, q in have if q == p) for p in PLACEMENTS}
gpl = collections.Counter(r["placement"] for r in gp)
gk = collections.Counter(r["gap_kind"] for r in gp)
gw = collections.Counter(r["who_can"] for r in gp)
gm = collections.Counter(r["means"] for r in gp)
gkw = collections.Counter((r["gap_kind"], r["who_can"]) for r in gp)
hosts = collections.Counter(urllib.parse.urlparse(r["url"]).netloc for r in fetchlog)
moves = sum(1 for r in log if r["action"].startswith("move"))
drops = sum(1 for r in log if r["action"] == "drop")
newcit = [r for r in cit if r["cite_id"] >= "SA-S-5001"]
nst_src = collections.Counter("held in observed-sa" if not r["structure"].startswith("http") else urllib.parse.urlparse(r["structure"]).netloc for r in newst)
nst_pl = collections.Counter(r["placement"] for r in newst)
salla_routes = sorted(set(r["route"] for r in gp if r["route"].startswith("https://salla.com/")))
nr_urls = {r["url"] for r in rd(f"{SP}/final/not-reached.tsv")}
assert all(u in nr_urls for u in salla_routes), [u for u in salla_routes if u not in nr_urls]
first_man = {r["url"] for r in rd("/home/user/sharrwah-knowledge-map/evidence/product-class/runs/20261010T235130Z-q1-salla-sources/manifest.tsv")}
newweb_first = sorted({r["source"] for r in newcit if r["source"].startswith("http")} & first_man)

def tbl(rows, head):
    out = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    out += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
    return "\n".join(out)

first = open(f"{FIRST}/notes.md", encoding="utf-8").read().rstrip("\n")
S = []
S.append("\n\n## Re-pass, 11 October 2026\n")
S.append("This section records the re-pass of the placement step under \"Changed on 11 October 2026: the placement step\" in "
         "`questions/Q1-concern-map.md`, with `studies/concern-map/measurements-2026-10-11.md` as its background. The sections above are the "
         "first run's notes, kept as they were; where they describe placements with our fixed values, `placements.tsv` is now a record only. "
         "Its values were not reused. The split pass named under \"Where this run stopped\" was withdrawn and was not done.\n")
S.append("### Files\n")
S.append(tbl([
    ("`inventory.tsv`", f"{len(inv):,}", "the first run's 2,620 entries, unchanged, and 7 new entries (SA-I-2621 to SA-I-2627) for the new concerns"),
    ("`concerns.tsv`", f"{ncon}", "the first run's 148, unchanged, and SA-C-301 to SA-C-304"),
    ("`citations.tsv`", f"{len(cit):,}", f"the first run's 2,828, unchanged, and {len(newcit)} new (SA-S-5001 to {max(r['cite_id'] for r in newcit)})"),
    ("`statements.tsv`", f"{len(st):,}", f"{len(st) - len(newst):,} from the reviewed candidates and {len(newst)} new"),
    ("`gaps.tsv`", f"{len(gp)}", "one row for every concern × placement with no statement"),
    ("`review-log.tsv`", f"{len(log)}", f"every candidate moved ({moves}) or dropped ({drops})"),
    ("`not-reached.tsv`", f"{len(nr)}", "the first run's 85 rows and the salla.com pages and one partners page the gaps route to"),
    ("`placements.tsv`", "740", "the first run's file, copied unchanged as a record; the checker reads it"),
], ["File", "Rows", "What"]))
S.append(f"\nConcern × placement cells: {ncon} × 5 = {ncon * 5}. Cells with at least one statement: {len(have)}. Cells with a gap: {len(gp)}. "
         "Every cell has one or the other, never both.\n")
S.append(tbl([(p, cells[p], gpl[p]) for p in PLACEMENTS] + [("total", len(have), len(gp))], ["Placement", "Cells with a statement", "Cells with a gap"]))
S.append("\n### Sources used\n")
S.append("- **Held lists and records, observed-sa@145f137.** The first run's citations to the held lists stand. New citations add the dashboard's own "
         "text (`structures/salla/dashboard-translations/ar/*.json`: payments, apps, shipping, orders, customers, domain, settings, manage, chat, "
         "merchant-services, themes-marketplace-monorepo, devstore, app-maker, reminders, marketing, ads-meta, channel); the Partners portal's help-centre "
         "answers (`portal-help-center-article/partner@en`); the Partners portal menu (`portal-menu-definitions/layout-mf@prod`); the communication-app "
         "event list and Twilight components already cited by the first run; the held sitemaps of salla.com and partners.salla.com; help.salla.sa's "
         "`llms.txt`; and one request line of a recorded Partners portal sweep (`raw/runs/20261008T145200Z-sweep-partner-portal-routes-en/responses.jsonl`).")
S.append(f"- **Pages read live on 2026-10-11.** {sum(hosts.values())} requests, logged in `fetched/log.tsv`: "
         + ", ".join(f"{n} {h}" for h, n in hosts.most_common()) + ". help.salla.sa articles were rendered with `page_text.mjs` and read in Arabic; "
         "docs.salla.dev pages were read as `.md`; partners.salla.com pages were rendered. Requests were sequential, at least 1.5 seconds apart per host, start to start (the log records times to the second). "
         "The two raw.githubusercontent.com requests looked for the Salla CLI licence and returned 404; nothing from them is cited. One docs URL "
         "(`ecommerce-events/overview.md`) returned 404; the section's real path is `ecommerc-events/`, which was read.")
S.append("- **First-run captures.** Statements from pages the first run captured are checked against `evidence/product-class/runs/20261010T235130Z-q1-salla-sources/`.")
S.append(f"- **New captures.** The {len(man)} web pages newly cited were captured into `fetched/capture/{os.path.basename(run_dir)}/` with "
         "`method/capture/run.sh`, `CAPTURE_LANG='en,ar;q=0.8'`, two workers and 1.5 seconds between requests per host. New statements from these pages are checked against these captures; new statements from the " + str(len(newweb_first)) + " newly cited pages the first run had already captured are checked against the first run's capture.")
S.append("- **salla.com and salla.sa.** Not requested in the re-pass; they refused this session in the first run. Every cell only those pages could show is a gap for the founder: save a page from a browser, with the exact URL as the route (" + str(len(salla_routes)) + " URLs, all in `not-reached.tsv`).")
S.append("\n### How the candidates were reviewed\n")
S.append(f"- **Candidates.** 2,617 candidates from `candidates.tsv`: 2,163 from list entries and 454 from the first run's citations. {len(st) - len(newst):,} were kept as statements, "
         f"{moves} of them under another placement; {drops} were dropped. Every move and drop is in `review-log.tsv` with its reason. No statement's text was edited; "
         "identifiers were tidied to the platform's own key or heading.")
S.append("- **List entries.** A list entry answers `where` or `boundary` only when its list is one of Salla's location or boundary structures: navigation, settings pages, the "
         "dashboard's bundle registry, API groups, scopes, webhook topics, extension points. It answers `decides` only when the item states availability or control: "
         "a plan line, a feature flag (with its plans and countries, or the answering store's values when it has none), a staff permission or a partner access "
         "permission. Order statuses were moved to `boundary`, as records the Merchant API returns. Comparison-table rows of the plans page were dropped, because the held "
         "text has the row titles but not which plans have them. App Store categories were dropped as statements about the App Store itself.")
S.append("- **First-run candidates.** Each was decided one by one (`scripts/review.py` holds the decisions). Navigation and settings entries cited under `boundary` were moved "
         "to `where`. Quotes that state a condition, limit or value were moved to `decides`; terms clauses and named contracts to `responsible`; API operations to "
         "`boundary`. A quote already kept under one placement for a concern was not kept again under another.")
S.append("\n### What the new statements add\n")
S.append(f"{len(newst)} new statements, by placement: " + ", ".join(f"{nst_pl[p]} {p}" for p in PLACEMENTS) + ". By source: "
         + ", ".join(f"{n} {k}" for k, n in nst_src.most_common()) + ".")
S.append("- **Who is responsible.** Salla's own words now place responsibility for, among others: transferring a domain (the merchant confirms the transfer is under their "
         "full responsibility, and Salla's is limited to carrying it out); the national address setting; carrying out an order the protection system stopped; held "
         "amounts for partner apps (سياسة إدارة المبالغ المحجوزة) and for carriers' apps (Salla holds label amounts from the wallet and settles with the carrier after "
         "its commission); Salla shipping labels (no contract with the carrier, the carriers' cancellation and refund policies, the postpaid terms); Salla Point card "
         "payments (Geidea's annual fees under the merchant's contract with Geidea, and the transfer through the provider); Mahally's terms; App Maker apps on the "
         "merchant's own developer accounts and the App Maker publishing policy's disclaimer by شركة تطبيق سلة; Salla Ads on Meta (Sweply is not responsible for "
         "results); the merchant services, ads services and agencies programmes (independent relationships Salla is not party to); and the partner's licences.")
S.append("- **Stated reasons.** A reason is recorded only where the text gives one explicitly (لأن، لضمان، بهدف، حرصًا، نظرًا، تماشيًا، حتى يتسنى، لأسباب, or an answer to a "
         "\"why\" question). Benefit statements (\"يساعدك على…\") were not taken as reasons.")
S.append("- **How a concern meets the rest.** Communication-app events and Twilight components already in the first run's lists now answer `boundary` for gifting, back-in-stock "
         "alerts, reorder reminders, marketing campaigns and quick purchase, because the item itself names the concern.")
S.append("\n### New concerns\n")
for r in con[148:]:
    S.append(f"- **{r['concern_id']}** {r['concern']}. {r['split_note']}")
S.append("- **Judged covered, so no new concern.** Inference: Mushammir (مشمّر) sits with the AI tools (SA-C-012); App Store ads with the App Store (SA-C-194); the events "
         "manager with marketing campaigns (SA-C-075); the Special plan's wholesale store (متجر الجملة) with customers and login (SA-C-060, SA-C-062), and it is "
         "distinct from the wholesale market (سوق الجملة, SA-C-098); the National Day 95 packages (partners.salla.com/legal/nd-packages) with the store plan (SA-C-004). "
         "These are readings, not Salla's own grouping.")
S.append("\n### Gaps\n")
S.append(tbl([(k, gk[k]) for k in ("page not read", "observation needed", "searched, not found", "stated only in general terms")], ["Kind", "Gaps"]))
S.append("")
S.append(tbl([(k, gw[k]) for k in ("agent", "founder", "either")], ["Who can close it", "Gaps"]))
S.append("")
S.append(tbl([(k, n) for k, n in gm.most_common()], ["Means", "Gaps"]))
S.append("\n- **No gap is left as `page not read`.** Each page named as likely to state a cell was read: the main help article for most concerns (73 fetched for this "
         "purpose), the docs pages for the developer concerns, and the partners.salla.com legal pages. Where none of them states the cell, the gap says so and names the next route.")
S.append("- **Observation needed (founder).** Mostly salla.com pages: the usage agreement (`https://salla.com/terms`) for who answers for each merchant feature; "
         "the privacy policy for where data lives; the selling policy, the nd96 policy and the affiliate terms; and Salla's product pages (payments, shipping, "
         "crossborder, Mahally, Salla Point, Salla Chat, Ads, the wholesale market, Salla Capital and others) for stated reasons. The rest are journeys: store verification, "
         "to see the payment services contract (عقد خدمات الدفع) and its parties; a settlement statement of a store with Salla Payments; sign-up choosing another "
         "country; and the Partners portal's Report Builder, app publication and Domains sections.")
S.append("- **Searched, not found.** Reasons and boundaries that the pages read do not state. The route is a question to Salla's merchant support or partner team, written in the gap.")
S.append("- **Stated only in general terms.** Who answers for developer-facing concerns (OAuth, scopes, webhooks, app events, App Functions, embedded pages, snippets, app "
         "settings, communication apps, rate limits, versioning, tooling, report builder, accounting apps, recurring-payment apps, storefront SDK, storefront API and "
         "e-commerce events). The App Store terms, the joining policy and the themes terms speak of apps, partners and themes in general; each gap quotes the clause and "
         "says why applying it would be inference.")
S.append("- **The one gap either can close.** SA-C-304 `decides`: the global selling page's FAQ answers are collapsed, and neither the rendered text nor the HTML holds them.")
S.append("\n### What could not be shown, and why\n")
S.append("- **Salla's legal entities per market (SA-C-230).** The partner-facing terms name the owning company, and differently (see below). No source read names the entity that "
         "contracts with merchants in Saudi Arabia, the UAE or Kuwait. Where, who decides and how it meets the rest wait on the usage agreement (`https://salla.com/terms`, "
         "`https://salla.com/ar-ae/terms`).")
S.append("- **Who processes and acquires Salla Payments, under which licence (SA-C-114).** Help articles say only that settlement and fees follow the payment services contract "
         "signed during store verification. Its parties are not stated anywhere read. The gaps route to `https://salla.com/payments` and to the verification journey.")
S.append("- **Who holds the funds.** Shown for partner apps' held amounts, carriers' label amounts and postpaid labels, all in Salla's own dashboard text. Not shown for the "
         "e-payments balance itself, the settlement currency (SA-C-164) or cash on delivery collected through Salla labels (SA-C-115).")
S.append("- **Sanctions and screening (SA-C-232).** Restricted products are shown for App Maker apps and fraud measures for orders. No source read mentions sanctions lists or "
         "screening; no reason is stated.")
S.append("- **Where data lives (SA-C-233).** No source read says where personal data is stored or processed. All five cells wait on the privacy policy (`https://salla.com/privacy`).")
S.append("- **Partner failure (SA-C-235).** No source read says what happens when a payment gateway or carrier is down; the gaps are questions to Salla.")
S.append("- **Responsibility for most merchant features.** 103 `responsible` cells remain gaps. For merchant features the usage agreement is the page that would say; "
         "for payments features, the payment services contract; for developer features, the partner terms speak only in general terms.")
S.append("\n### Where Salla's own sources disagree (new in the re-pass; recorded, not resolved)\n")
S.append("- **Minimum theme price.** The theme publishing docs say \"Price your theme at a minimum of *SAR250*\"; the Partners portal's help answer says the minimum is 150 ر.س. Both are recorded under SA-C-208.")
S.append("- **Owning company and registration number.** The store migration terms name شركة منصة سلة للاتصالات وتقنية المعلومات with registration 4031200589, the number the "
         "App Store terms give for شركة تطبيق سلة لتقنية المعلومات. The National Day 95 terms name شركة منصة سلة للاتصالات وتقنية المعلومات (شخص واحد). Both are added to SA-C-230 beside the first run's.")
S.append("- **Presence in Saudi Arabia.** Theme developers anywhere may sell themes (held Partners portal help answer 759769406); service providers must be in Saudi Arabia (partners help-centre page). "
         "These are different programmes; recorded as stated.")
S.append("\n### Problems with method, and facts about the sites\n")
S.append("- **Dashboard text as Salla's words.** The dashboard's translation files are Salla's own UI text, held as structures. Statements from them carry the key as identifier, "
         "and a note says where the text shows when the key makes it clear. They are dated by the files' capture (2026-10-08) because the text carries no date.")
S.append("- **Text with markup.** Docs statements are quoted as the page reads, without Markdown markers or link targets; the checker's markup-removed comparison matches them to the `.md` captures.")
S.append("- **Help pages with two versions.** The App Maker publishing policy exists as two articles (sxfhz2u8o03sfkimbkmcs71x, 2026-08-22, and l6e8bqm8vm89arp4krr40cdm, 2026-08-29) with the same clauses; the later one is cited.")
S.append("- **The nd96 policy (SA-C-180).** Inference: by its path it may be the terms of a National Day 96 campaign, like `partners.salla.com/legal/nd-packages` for National Day 95. Its content was not reached, so nothing is recorded from this guess.")
S.append("- **Sweply.** The dashboard's Meta ads screens name Sweply (processing fees, an ads wallet, no responsibility for results). Who Sweply is is not stated in anything read.")
S.append("- **(سلة بي).** The shipping translation of the postpaid-labels terms says amounts are taken \"من مبيعاتك القادمة عبر (سلة بي)\"; the orders translation of the same clause says \"مستحقاتك القادمة عبر سلة\". Recorded as text; nothing is concluded about a product or entity named سلة بي.")
S.append("- **Check.** `method/check_concern_map.py` was run on `check/run/salla` (a link to `final/`) with the first-run capture and the new capture run; the result is in `check/out/`.")
open(f"{F}/notes.md", "w", encoding="utf-8").write(first + "\n".join(S) + "\n")
print("notes written", len(first), "+", sum(len(s) for s in S))
