# Brief: S-01, what one platform states (pilot, step 1, phase A)

This is `PLAN.md` Stage 2, the pilot. You are one agent with one task, for one platform. The message that started you names the platform; it is "your platform" below. Read only this brief and the inputs it names. You don't see the other platforms' work.

## The subject

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

- **The interval.** It starts when a buyer pays for an order. It ends when the money reaches an account the merchant holds outside the platform.
- **What bears on the subject.** Any statement by your platform about one of these:
  - who or what receives, holds or controls the money during the interval;
  - who answers for that money;
  - the rules that govern it;
  - when the interval ends.

  It also includes any statement that your platform has no part in the interval.

**Your task.** Collect everything your platform states that bears on the subject, in its own words, and record what it doesn't state. Don't compare it with any other platform, and don't judge it.

## Inputs

**Start with your platform's Q1 index,** in `studies/concern-map/platforms/<platform>/`:
- `concerns.tsv`, `statements.tsv`, `gaps.tsv` and `citations.tsv`;
- its statements were already checked verbatim against their sources;
- its gaps name pages or corpora that may close them.

**Then read your platform's own material, as held or live:**

| Platform | Held | Live (declarations only) |
| --- | --- | --- |
| shopify | observed-sh at `e4984072995bf730a98292a1903de1a49390229a`: `structures/shopify/` and committed text under `raw/runs/` | help.shopify.com, shopify.dev, shopify.com/legal |
| salla | observed-sa at `4ca2e896a729215f422a137a364e7e9488610ba3`: `structures/salla/`, including `help-articles/{ar,en}/texts.jsonl`, `com-policies/` and `partners-legal/` | docs.salla.dev |
| woocommerce | WooCommerce 11.2.1 release files, cited as `woocommerce-11.2.1:<path>` | woocommerce.com docs and legal pages, and any agreement its terms incorporate |
| zid | none | docs.zid.sa, zid.sa and Zid's help pages |
| bigcommerce | none | docs.bigcommerce.com, bigcommerce.com and its legal pages, support.bigcommerce.com where it can be read |

**Tools for held pages:**
- To find whether a page is held, run `python3 -I method/held_index.py <url>`.
- To read a record held in a fetch archive, run `python3 -I method/warc_text.py <repository root> <location> --text`.

**Reading live pages.** Read them as the Q1 runs did: a `.md` endpoint, the raw file, or the rendered page through `method/capture/page_text.mjs`. A summary returned by a fetching tool is not the page. Don't get around logins, paywalls or bot challenges.

**Don't open:**
- other platforms' folders, and `studies/concern-map/` outside your platform's folder;
- `studies/subjects/` outside your own output folder;
- `PLAN.md`, `STATE.md`, `NEXT.md`, `questions/`;
- `register/`, `model/`, `yemen-setup-options/`, `shopify-payments-study/`, `evidence/yemen/`.

## Rules

1. **A statement** is your platform's own words or data, copied verbatim. It carries the platform's identifiers where it has them, such as a key, scope, route, plan name or section heading. Never use a category name of ours.
2. **Placement.** Each statement answers one of five questions, decided by the kind of source:
   - `where`: where the platform puts it in its own organization (an admin section or route, an API group, an app or extension target, a separate host or product, a code path);
   - `decides`: what turns it on or off, limits it, or sets its value (eligibility conditions, entitlements and features, plan lines, settings, staff permissions);
   - `responsible`: what the terms, policies and legal-entity records state;
   - `boundary`: API resources, webhook topics, access scopes, extension targets, events;
   - `reason`: a reason the platform states.
3. **Scope.** A statement holds where the platform says it holds: a store, plan, country or role. Record that scope as stated. Leave it empty when the statement is general.
4. **Copying from the index.** A statement already in your platform's Q1 index is copied with its quote and citation unchanged, and `from` names its concern. Read its source again only if the excerpt is too short to show what bears on the subject.
5. **Terms.** Record each word your platform uses for the money, for who holds it, and for the steps of the interval. Quote the platform's own definition where it gives one.
6. **Gaps.** For each part of the interval your platform's sources don't state:
   - record what you read looking for it, each path or URL;
   - give its kind:
     - `page not read`: a page you know of and couldn't read now;
     - `observation needed`: only a store, a journey or a question to the platform would show it;
     - `searched, not found`: you read the likely sources, as listed, and none states it;
     - `stated only in general terms`: the terms speak only of the platform's services in general.
7. **No inference.** No inference goes into a statement. A note may hold inference, starting with "Inference:", and it never counts.
8. **Stop and report** past 150 statements.

## Quotes and citations

- **Quotes are verbatim,** at most 300 characters, with no ellipses, and within one paragraph of the source. Arabic stays as written.
- **The checker's matching.** It collapses whitespace, removes HTML tags and decodes entities, on both sides.
- **A local source** is written `<repository>@<full commit>:<path>`, using the commits in the table, or `woocommerce-11.2.1:<path>`. A record in a fetch archive is cited by its archive path and offset as the locator.
- **A live source** is its exact URL. The coordinator captures every cited URL after your run, and the checker looks for each quote in that capture. Quote from the text you actually fetched.

## Output, in `studies/subjects/S-01/<platform>/`

All files are tab-separated, with a header row and no quoting. Tabs and newlines never appear inside a field. `XX` is your platform's code: SH, SA, WC, ZD or BC.

| File | Columns |
| --- | --- |
| `statements.tsv` | `stmt_id` (S01-XX-001…) · `placement` · `identifier` · `statement` · `scope` · `cite_ids` · `from` (`index:<concern_id>`, or `new`) · `note` |
| `terms.tsv` | `term` · `definition` (verbatim, or empty) · `cite_ids` |
| `gaps.tsv` | `gap_id` (S01-XX-G01…) · `what_is_missing` · `read` (each path or URL read, `; `-separated) · `gap_kind` · `who_can` (`agent` or `founder`) · `route` |
| `citations.tsv` | `cite_id` (S01-XX-C001…) · `source` · `locator` · `quote` · `source_date` · `date_basis` · `accessed` · `access_path` (`md`, `raw`, `rendered` or `local`) |
| `notes.md` | What you read; what you couldn't read; problems with the method. |

Write the files as you go: if you are interrupted, the next run continues from them.
