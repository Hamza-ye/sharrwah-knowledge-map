# Writes final/notes.md: the first run's notes, unchanged, then the section "Re-pass, 11 October 2026".
import sys, os, glob, collections, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
FINAL = os.path.join(BASE, "final")
first = open(os.path.join(FIRST, "notes.md"), encoding="utf-8").read().rstrip() + "\n"

inv = rd(os.path.join(FINAL, "inventory.tsv"))
con = rd(os.path.join(FINAL, "concerns.tsv"))
cit = rd(os.path.join(FINAL, "citations.tsv"))
st = rd(os.path.join(FINAL, "statements.tsv"))
gp = rd(os.path.join(FINAL, "gaps.tsv"))
nr = rd(os.path.join(FINAL, "not-reached.tsv"))
lg = rd(os.path.join(FINAL, "review-log.tsv"))
newinv = rd(os.path.join(WORK, "inventory-new.tsv"))
added_c = rd(os.path.join(WORK, "cites-added.tsv"))
cand = rd(os.path.join(BASE, "candidates.tsv"))
rev = rd(os.path.join(WORK, "reviewed-statements.tsv"))
P5 = ["where", "decides", "responsible", "boundary", "reason"]
cell_st = collections.defaultdict(int)
for r in st:
    cell_st[(r["concern_id"], r["placement"])] += 1
cit_by = {r["cite_id"]: r for r in cit}
web_out = collections.Counter()
for r in st:
    src = cit_by[ids(r["cite_ids"])[0]]["source"]
    if src.startswith("http") and src.split("#")[0] not in MANIFEST:
        web_out[src] += 1

def cnt(rows, key):
    return collections.Counter(r[key] for r in rows)

L = []
A = L.append
A("\n## Re-pass, 11 October 2026\n")
A("This section records the re-pass of the placement step under \"Changed on 11 October 2026\" in `questions/Q1-concern-map.md`. "
  "The inventory, the concern names and the first run's citations stand. `placements.tsv` is kept as the first run's record; its values were not reused. "
  "The placements are now `statements.tsv` (the platform's own words or data, verbatim) and `gaps.tsv` (one row for every concern and placement with no statement). "
  "Everything above this section is the first run's notes, unchanged.\n")

A("### Sources used\n")
A(f"- **observed-sh at `{COMMIT}`** (cited as `observed-sh@{C9}:<path>`), read with `git show` only. Structures used for new statements: "
  "`admin-router` (where and eligibility excerpts of routes), `admin-permission-tree` (staff permissions), `shop-request-details` (entitlement, feature and resource-limit values per store), "
  "`plan-comparison-public` (whole table rows, with the header order as scope), `plan-page-public` and `plan-page-admin` (footnotes naming providers), "
  "`app-store-built-in-features` (29 pages), `admin-graphql-reference-nav`, `ui-extension-targets`, `dev-access-lines`. "
  "Raw run records used: the PlanFeatureSetQuery, ValidationSchemaByContextQuery, LegalEntityTypesByCountryCode, OrganizationLegalEntities and ServerIntent answers, "
  "the `answers.jsonl` endpoint and variables lines of the sweep runs (admin operation areas and intents), and the sign-up journey of 6 October 2026 (step 4). "
  "`derived/` and `index/` files were used only to find these sources and are never cited.")
A("- **Web pages in the capture** `evidence/product-class/runs/20261011T061248Z-q1-shopify-sources` (152 pages). New quotes from these pages are sentences of the captured text; "
  "dated pages keep the first run's source date, undated pages are dated 2026-10-11 (the capture).")
A("- **The two Shopify Credit terms pages**, read for the first time as the first run's notes asked: the Shopify Credit Program Terms and the Shopify Credit Issuing Bank Terms "
  "(both \"Effective Date: September 1, 2024\"). They were read from working copies made with `method/capture/page_text.mjs` (`fetched/pages/`); "
  "the coordinator's capture `evidence/product-class/runs/20261011T075149Z-q1-shopify-sources-2` holds them.")
more_runs = [x.strip() for x in open(os.path.join(BASE, "fetched", "capture", "EXTRA_RUNS")) if x.strip()]
n_more = sum(len(rd(os.path.join(BASE, x, "manifest.tsv"))) for x in more_runs)
A("- **Pages read for the gap review** (11 October 2026, after the first report): the Help Center page of each concern that no captured page covered (one page each, found through the held "
  "Help Center section lists or, for four concerns, tried at a guessed path), the Shop Campaigns Merchant Terms, the Shopify Collabs Terms, the shopify.dev POS UI and admin UI extension references, the Oxygen runtime page, "
  "the Help Center pages on copyright reports and on Collective supplier payments, and Shopify's compliance reports page. They were read as working copies (`.md` endpoints, or `page_text.mjs`), "
  f"and the {n_more} pages cited from them were captured with `method/capture/run.sh` into " + " and ".join(f"`{x}`" for x in more_runs) + ". "
  "Three guessed Help Center paths returned 404 and are named in the gaps that needed them. The address https://www.shopify.com/legal/shop-cash-merchant-terms serves the Shop Campaigns Merchant Terms. "
  "URLs were found from the held structures, and for the Shop Campaigns and Collabs terms from a web search used only to find the address; nothing is quoted from a search result. Every fetch is logged in `fetched/log.tsv`.")
A("- **Not used:** the first run's `work/` files and placement values; Sharrwah's registers, studies, model page, frame and decision log; the founder's words; the Salla and WooCommerce outputs. "
  "The `argus.shopifycloud.com` answers in the sweep runs hold authorization tokens and were not opened beyond identifying that; none of their content is quoted. "
  "Business-entity answers are quoted without names, addresses or other personal fields.\n")

A("### Counts\n")
A(f"- `inventory.tsv`: {len(inv)} entries ({len(inv) - len(newinv)} from the first run, {len(newinv)} added: " +
  ", ".join(f"{k} {v}" for k, v in cnt(newinv, 'list').most_common()) + ").")
A(f"- `concerns.tsv`: {len(con)} concerns (196 from the first run, 2 added: SH-C-201 Shopify Plus contract terms and renewals; SH-C-202 Shopify Magic for product descriptions and blog posts). "
  "First-run concerns gained the new inventory entries in `inv_ids`; nothing else in them changed.")
A(f"- `citations.tsv`: {len(cit)} (first run SH-S-0001 to SH-S-3192: 3,192; script joins SH-S-5001 to SH-S-6367: 1,367; this re-pass SH-S-7001 to SH-S-{7000 + len(added_c)}: {len(added_c)}). "
  "A new citation reuses an existing id when the source and quote are identical.")
A(f"- `statements.tsv`: {len(st)} statements: " + ", ".join(f"{p} {sum(1 for r in st if r['placement'] == p)}" for p in P5) + ".")
A(f"- `gaps.tsv`: {len(gp)} gaps: " + ", ".join(f"{p} {sum(1 for r in gp if r['placement'] == p)}" for p in P5) + "; by kind: " +
  ", ".join(f"{k} {v}" for k, v in collections.Counter(r['gap_kind'] for r in gp).most_common()) + ".")
A(f"- `review-log.tsv`: {len(lg)} rows: " + ", ".join(f"{k} {v}" for k, v in collections.Counter(r['action'] for r in lg).most_common()) + ".")
A(f"- `not-reached.tsv`: {len(nr)} rows (4 from the first run, {len(nr) - 4} admin-only pages added).")
A(f"- `placements.tsv`: {len(rd(os.path.join(FINAL, 'placements.tsv')))} rows, the first run's record, unchanged. The new concerns have no rows there; their placements are in `statements.tsv` and `gaps.tsv`.\n")
A("Cells (concern x placement) with at least one statement, and with a gap instead:\n")
A("| placement | with a statement | with a gap |")
A("| --- | --- | --- |")
for p in P5:
    s = sum(1 for c in con if cell_st[(c['concern_id'], p)])
    g = sum(1 for r in gp if r["placement"] == p)
    A(f"| {p} | {s} | {g} |")
A("")

A("### How the candidates were reviewed\n")
A(f"- `candidates.tsv` held {len(cand)} candidates. Script joins (router where and eligibility, access lines, Help Center links, store values) were reviewed in groups; "
  "every first-run candidate was reviewed one by one. Each was kept, moved to the placement whose question it answers, or dropped; every move and drop is in `review-log.tsv` with its reason. "
  "No statement text was edited.")
A("- List entries (a settings-navigation title, a Help Center section title, a table-of-contents entry, a legal-index entry, a plan-table row label, a billing-charge filter value, an assignable-permission value) "
  "were dropped from decides, responsible and boundary: an entry only shows that something exists. Entries of location or boundary structures (admin routes, API groups, extension targets, webhook topics, scopes) were kept under where or boundary. "
  "A plan-table row label was replaced by the whole row with its values per plan.")
A("- A router route, access line or Help Center link that belongs to another concern (by its own section, path, title or text) was dropped where it stood and added, with the same citation, under the concern it belongs to.")
A("- Store values were kept only where a route kept under the same concern names the key in its eligibility.")
A("- The first run's step \"one row per party\" was withdrawn and was not done.\n")

A("### New lists and concerns\n")
A("- **Admin operation areas** (`other:admin-operation-areas`): organizations, destinations, capital, banking, contractmanagement, completeness_engine, profile_assessment, server_intents, "
  "each cited from an endpoint line of a sweep run's `answers.jsonl`. The `server_intents` area carries intents with an action and a type (create catalog, create role, open rollout and others); "
  f"{sum(1 for r in st if r['identifier'].startswith('ServerIntent ') and 'server_intents' in r['structure'])} of them are boundary statements of the concerns they name.")
A("- **Permission tree** (`other:staff-permissions`): 16 permission ids not in the first run's permission lists (purchase orders, inventory counts, Flow automations, staff management, external login services, access tokens, collaborators, Balance, Shopify Credit, billing details).")
A("- **Access scopes** named in access lines but not in the first run's scope list: 33.")
A("- **App Store built-in feature pages**: 29. Two of them (Shopify Magic for blog posts, Shopify Magic for product descriptions) are covered by no existing concern; they make SH-C-202.")
A("- **The merchant's own business entities** (`other:merchant-legal-entities`): 4 entity records from the organization answers (all in YE but one in US, on the business-entity journey store).")
A("- **Store keys** (`other:store-entitlements`, `other:store-features`, `other:store-resource-limits`): every top-level key of the RequestDetails answers across the 14 stores held. "
  "A key is tied to a concern only where a route in the admin router names it in its eligibility and that route is under the concern; " + str(len(rd(os.path.join(WORK, "key-ties.tsv")))) + " keys are tied that way. The other keys are listed below with their values per store.")
A("- **SH-C-201** (Shopify Plus contract terms and renewals) is split from SH-C-015 because the admin keeps the Plus contract and its renewals in their own operation area and routes.\n")

A("### Gaps by kind\n")
A("Each gap has a `gap_kind` (questions/Q1-concern-map.md, rule 4):")
kinds = collections.Counter(r["gap_kind"] for r in gp)
A(f"- **searched, not found** ({kinds.get('searched, not found', 0)}): the likely pages and structures were read or searched and none states it. Most are stated reasons; "
  "the rest are boundaries no held API list names, and legal concerns whose pages state rules but no place, condition, party or interface. `why_not_held` names what was read or searched.")
A(f"- **stated only in general terms** ({kinds.get('stated only in general terms', 0)}): responsible cells of features that Shopify's terms cover only as \"the Services\" "
  "(Terms of Service, '13. Shopify Contracting Party and Forum' and '4. Your Responsibilities'), as \"the POS Services\" ('9.3 POS Services') or as the Payments Services "
  "(Shopify Payments Terms of Service, 'Part I, A. The Payment Processor'). Applying such a clause to one concern would be inference, so these stay gaps; `why_not_held` names the clause and the page.")
A(f"- **observation needed** ({kinds.get('observation needed', 0)}): a journey, a store on a plan, or a question to Shopify would show it.")
A(f"- **page not read** ({kinds.get('page not read', 0)}): the pages behind these gaps were read after the first report; what they stated is now in `statements.tsv`, and the rest were reclassified.\n")

A("### Gaps by who can close them\n")
by_who = collections.defaultdict(collections.Counter)
for r in gp:
    by_who[r["who_can"]][(r["means"], r["placement"])] += 1
for who in ["agent", "founder", "either"]:
    rows = [r for r in gp if r["who_can"] == who]
    A(f"- **{who}** ({len(rows)}): " + "; ".join(f"{m} for {p} {n}" for (m, p), n in sorted(by_who[who].items(), key=lambda x: -x[1])) + ".")
    if who == "founder":
        for r in rows:
            A(f"  - {r['concern_id']} {r['placement']}: {r['means']}; {r['route']}")
    if who == "either":
        for r in rows:
            A(f"  - {r['concern_id']} {r['placement']}: {r['means']}; {r['route']}")
A("")
A("The agent rows are pages that were read or searched without finding a statement (mostly stated reasons), and responsible cells that Shopify's terms cover only in general terms. "
  "Plan-specific observation is named in the founder rows: a paid Shopify Plus store would show the Plus contract and renewal routes; the observed stores are trial stores, paid Advanced stores and partner development stores, all registered in YE, "
  "so products offered only in some countries (Shopify Balance, Shopify Credit, Shopify Capital per country) cannot be reached from them.\n")

A("### What could not be shown, and why\n")
A("- **Stated reasons** are rare in Shopify's material: most pages say what a feature does and who may use it, not why it is placed where it is. "
  f"{sum(1 for c in con if cell_st[(c['concern_id'], 'reason')])} concerns have a stated reason.")
A("- **Who is responsible** for most core admin features: the Terms of Service speak of \"the Services\" as a whole; a general clause was not copied onto features it does not name.")
A("- **Terms shown only inside the admin**: the Shopify Plus Terms, the Shopify Balance terms and the Shopify Capital terms per country (`not-reached.tsv`).")
A("- **Plus contract values**: the contractmanagement answers held are empty on every observed store (`currentContractTerms` null, `renewals` []).")
A("- **Absence** is never read as \"does not exist\": a key, route or country missing from observed-sh is a gap.\n")

A("### Method notes\n")
A("- Every statement was checked against its first cited source with the checker's own matching (exact, markup removed, case and diacritics ignored). "
  "Every web page cited is in one of the capture runs passed to the checker: the brief's capture `20261011T061248Z-q1-shopify-sources`, the coordinator's capture of the Credit terms "
  "`20261011T075149Z-q1-shopify-sources-2`, and this re-pass's captures named above.")
used = set(r["cite_id"] for r in inv)
for r in rd(os.path.join(FINAL, "placements.tsv")):
    used.update(ids(r["cite_ids"]))
used_old = set(used)
for r in st:
    used.update(ids(r["cite_ids"]))
unused = [r["cite_id"] for r in cit if r["cite_id"] not in used]
A(f"- Counting the inventory, the first run's placements and the statements, {len(unused)} citations are unused: " + ", ".join(f"{k} {v}" for k, v in collections.Counter(('first run' if int(x[5:]) < 5000 else 'script joins' if int(x[5:]) < 7000 else 're-pass') for x in unused).items()) +
  " (candidates that were dropped, or first-run citations that no placement used). They are kept, as `citations.tsv` holds all citations.")
A("- New web statements are whole sentences of the page as the checker normalizes it (markup removed); where a sentence was long, a contiguous part of it was taken, never with an ellipsis.")
A("- Identifiers: a route id, permission id, key, scope, extension target, intent, API reference key, section heading, or the page's own path where a page has no section heading for the passage.")
A("- Disagreements recorded, not resolved: the product-variants built-in feature page says \"up to 100 variants for each of your products\", while every store's `resourceLimits.maxProductVariants` is 2048; "
  "the public pricing page says Shopify Bill Pay \"is provided by Melio\", the admin plan page says \"is powered by Melio\".\n")

unplaced = open(os.path.join(WORK, "unplaced-keys.md"), encoding="utf-8").read()
L.append(unplaced)
open(os.path.join(FINAL, "notes.md"), "w", encoding="utf-8").write(first + "\n".join(L).rstrip() + "\n")
print("notes.md written:", sum(1 for _ in open(os.path.join(FINAL, "notes.md"), encoding="utf-8")), "lines")
