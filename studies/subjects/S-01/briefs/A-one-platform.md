# Brief: S-01, what one platform states (pilot, step 1, phase A)

This is `PLAN.md` Stage 2, the pilot. You are one agent with one task, for one platform. The message that started you names the platform; this brief calls it "your platform". Read only this brief and the inputs it names. You don't see the other platforms' work.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

**The two ends** are named in your platform's own words. Record:
- what your platform calls the buyer's payment, and where it says that happens;
- what it calls the merchant's payout, and where it says that happens.

If it names no payout, or several, record what it names.

**What bears on the subject:** any statement by your platform, or by an agreement its terms incorporate, that says one of these about the merchant's money between the two ends:
- **(a)** who or what holds or controls it;
- **(b)** under whose account, licence or terms it is held;
- **(c)** when, or on what conditions, it is released to the merchant or held back;
- **(d)** that your platform has no part in it.

**Your task:** collect everything your platform states that bears on the subject, in its own words, and record what it doesn't state. Don't compare it with any other platform, and don't judge it.

## Inputs

**Your platform's Q1 index,** in `studies/concern-map/platforms/<platform>/`. Open only these four files there:
- `concerns.tsv`;
- `statements.tsv`;
- `gaps.tsv`;
- `citations.tsv`.

Its statements were already checked verbatim against their sources, and its gaps name pages or collections that may close them.

**Your platform's own material, as held or live.** For every platform this includes any agreement its terms incorporate (`PLAN.md` section 6 allows them).

| Platform | Held | Live (declarations only) |
| --- | --- | --- |
| shopify | observed-sh at `e4984072995bf730a98292a1903de1a49390229a`: `structures/shopify/` and committed text under `raw/runs/` | help.shopify.com, shopify.dev, shopify.com/legal |
| salla | observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3`: `structures/salla/`, including `help-articles/{ar,en}/texts.jsonl`, `com-policies/` and `partners-legal/` | docs.salla.dev |
| woocommerce | WooCommerce 11.2.1 release files, cited as `woocommerce-11.2.1:<path>` | woocommerce.com docs and legal pages |
| zid | none | docs.zid.sa, zid.sa and Zid's help pages |
| bigcommerce | none | docs.bigcommerce.com, bigcommerce.com and its legal pages, support.bigcommerce.com where it can be read |

**Tools:**
- To find whether a page is held, run `python3 -I method/held_index.py <url>`.
- To read a record held in a fetch archive, run `python3 -I method/warc_text.py <repository root> <location> --text`.

**Reading a live page.** Read it as the Q1 runs did: a `.md` endpoint, the raw file, or the rendered page through `method/capture/page_text.mjs`. A summary returned by a fetching tool is not the page. Don't get around logins, paywalls or bot challenges.

**Don't open:**
- anything else under `studies/`, except your own output folder;
- `PLAN.md`, `STATE.md`, `NEXT.md` and `questions/`;
- `register/`, `model/`, `yemen-setup-options/`, `shopify-payments-study/` and `evidence/yemen/`.

## Rules

1. **A statement** is your platform's own words or data, copied verbatim. It carries the platform's identifiers where it has them, such as a key, scope, route, plan name or section heading. Never use a category name of ours.
2. **Placement.** Give each statement the one question it answers:
   - `where`: where the platform puts it in its own organization;
   - `decides`: what turns it on or off, limits it, or sets its value;
   - `responsible`: who answers for it, as terms, policies or legal-entity records state;
   - `boundary`: the API resource, webhook topic, access scope, extension target or event where it meets the rest;
   - `reason`: a reason the platform states.

   Typical sources for each, from Q1:
   - `where`: admin sections and routes, API groups, app or extension targets, separate hosts or products, code paths;
   - `decides`: eligibility conditions, entitlements and features, plan lines, settings, staff permissions;
   - `responsible`: terms, policies, legal-entity records;
   - `boundary`: APIs, webhooks, scopes, extension targets, events.

   For a help page, the question the statement answers decides its placement.
3. **Scope.** A statement holds where the platform says it holds: a store, plan, country or role. Record that scope as stated, and leave it empty when the statement is general.
4. **Release marker.** When the source attaches a word that marks a stage of release to what the statement describes, copy that word into `marker`, verbatim. `PLAN.md` section 6's examples are beta and sunset.
5. **Copying from the index.**
   - Give a statement copied from your Q1 index a new `cite_id`, keeping its index source, locator and quote unchanged.
   - Set `from` to `index:<concern_id>:<index cite_id>`.
   - Read its source again only if the excerpt is too short to show what bears on the subject.
6. **Terms.** Record each word your platform uses for the money, for who holds it, and for the two ends:
   - quote the platform's own definition where it gives one;
   - where the platform gives its own translation of the term, such as an Arabic and an English page for the same thing, quote that too.
7. **Absences.** Absence counts only from a complete list your platform publishes, whose own words present it as the full set. Record such an absence in `absences.tsv`, citing:
   - the list;
   - the words that make it complete.

   Anything else your platform doesn't state is a gap.
8. **Gaps.** Make one gap for each of (a) to (d) that your platform doesn't state, and one for each end it doesn't name.
   - `read`: list what you read looking for it. Write held paths with their commit, and live URLs with the date you read them.
   - `gap_kind`, as Q1 defines them:
     - `page not read`: a named page or file that would likely state it hasn't been read yet;
     - `observation needed`: a journey, a store on a plan, a page saved from a browser, or a question to the platform would show it;
     - `searched, not found`: the likely pages and structures were read, as `read` lists, and none states it. An index or a sitemap doesn't count as reading the pages it lists. A held collection of the platform's pages that you didn't search rules this kind out.
     - `stated only in general terms`: the terms speak only of the platform's services in general.
   - `who_can`: `agent`, `founder` or `either`.
   - Before you give a gap `founder` or `either`, run `method/held_index.py` on each address in its route. If the page is held and readable, read it instead.
9. **No inference, anywhere.** Notes record what was read, what couldn't be read, and problems. They never record inference.
10. **Stop and report** past 150 statements.

## Quotes and citations

- **Quotes are verbatim,** at most 300 characters, with no ellipses, and within one paragraph of the source. Arabic stays as written. The checker collapses whitespace, removes HTML tags and decodes entities, on both sides.
- **A local source** is `<repository>@<commit>:<path>`.
  - Copied citations keep their index commit. New ones use the full commits in the table, or `woocommerce-11.2.1:<path>`.
  - A record in a fetch archive is cited by its archive path, with the offset as the locator.
- **A live source** is the exact URL you fetched: the `.md` endpoint if that is what you read. The coordinator captures every cited URL after your run, and the checker looks for each quote in that capture.
- **`locator`** is the heading, anchor or line.
- **`source_date`** is the date the source shows: published, updated or effective. For an undated live page, it is the date you read it. `date_basis` says which.
- **`accessed`** is the date you read it.

## Output, in `studies/subjects/S-01/<platform>/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. `XX` is your platform's code: SH, SA, WC, ZD or BC.

| File | Columns |
| --- | --- |
| `statements.tsv` | `stmt_id` (S01-XX-001…) · `bullet` (`a`–`d`, or `end` for a statement naming an end) · `placement` · `identifier` · `statement` · `scope` · `marker` · `cite_ids` · `from` (`index:<concern_id>:<index cite_id>`, or `new`) · `note` |
| `terms.tsv` | `term` · `translation` (verbatim, or empty) · `definition` (verbatim, or empty) · `cite_ids` |
| `absences.tsv` | `absence_id` (S01-XX-N01…) · `what_is_absent` · `list_cite_ids` · `complete_cite_ids` · `note` |
| `gaps.tsv` | `gap_id` (S01-XX-G01…) · `bullet` (`a`–`d` or `end`) · `what_is_missing` · `read` · `gap_kind` · `who_can` · `route` |
| `citations.tsv` | `cite_id` (S01-XX-C001…) · `source` · `locator` · `quote` · `source_date` · `date_basis` · `accessed` · `access_path` (`md`, `raw`, `rendered` or `local`) |
| `notes.md` | What you read; what you couldn't read; problems with the method. |

Write the files as you go: if you are interrupted, the next run continues from them.
