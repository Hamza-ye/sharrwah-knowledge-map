# BigCommerce: notes on the Q1 concern map run

**Run:** 12 October 2026, from the cloud session, at declaration level only: developer docs, API reference, legal and pricing pages, and BigCommerce's product pages. No account was used. Ids are prefixed `BC`. The run started from the reshaped placement step (statements and gaps); there is no `placements.tsv`.

**Files:** inventory {INV} entries, concerns {CON}, citations {CIT}, statements {ST}, gaps {GP}, not reached {NR}.

## Where BigCommerce's material lives

- **Developer docs and API reference.** `developer.bigcommerce.com` redirects to `docs.bigcommerce.com`. Every docs page serves markdown at its URL plus `.md`; the run read those (`access_path` md). `https://docs.bigcommerce.com/llms.txt` is a short index; `https://docs.bigcommerce.com/developer/llms.txt` is the full developer index (about 3,999 lines). `llms-full.txt` redirects to `llms.txt`.
- **Legal pages.** The MSA and its Incorporated Terms are on `www.commerce.com`. The MSA's parties are "Commerce.com US, Inc. and any of Commerce's affiliates"; the commerce.com footer reads "Commerce LLC", and bigcommerce.com pages read "BigCommerce Pty. Ltd.". Each legal page shows a "Date of Last Revision", recorded as the source date (the US, UK and Canada Unified Billing page shows none).
- **Pricing and product pages** are on `www.bigcommerce.com`. They are undated; they are recorded as read on 12 October 2026.
- **Help Center** (`support.bigcommerce.com`): not reached; see below.

## Site directives, recorded as facts

- `https://docs.bigcommerce.com/llms.txt` has a section "Instructions for AI Agents": append `.md` for clean Markdown, append `/llms.txt` to a section URL for its index, and connect to an MCP server at `https://docs.bigcommerce.com/_mcp/server`. The run used the `.md` endpoints because the brief asked it to check for them; it did not connect to the MCP server.
- `https://www.bigcommerce.com/llms.txt` (last-updated 2026-02-02) has "Usage Guidelines" and "Attribution Preferences" (cite the exact page, prefer canonical pages, do not imply commercial relationships not stated, attribute as "According to BigCommerce") and a "Legal Notice" that the file grants no licence to train on or redistribute content. These are recorded as facts about the site.

## Lists used and their sizes

| List | Where BigCommerce shows it | Entries |
| --- | --- | --- |
{LISTS}

**Where the inventory stops:**
- **API reference:** taken at the level of the navigation pages listed in the developer index (lines 536-645): one entry per group page, not per endpoint. The four GraphQL APIs are entries; their schemas (Queries, Mutations, Types: about 2,050 index lines) are not expanded type by type. The archived B2B Edition V2 API and the learning courses are left out. Four closed-beta groups (Checkout Extensions, Page Widgets, Powered By, Product Recommendations) are taken from the index's API Docs section.
- **Webhook topics:** every topic on the four event-reference pages (Webhook Events, Channel Webhooks, Inventory and location events, B2B Edition Webhooks). One topic, `store/priceList/assignment/updated`, appears on two pages and is listed twice.
- **OAuth scopes:** the three tables on the API Accounts page (token creation, store resource, account resource), one entry per parameter.
- **Settings:** the Help Center could not be read, so the control panel's settings sections as the Help Center names them are not in the inventory. The settings list used instead is the Settings V3 API's own table of "Available settings and configuration" (19 resources). Control panel paths named in the developer docs (for example `Settings > Setup > Tax`, `Settings > Setup > Currencies`, `Settings > Advanced > Store logs`, `Settings > API and MCP > MCP`) appear in statements, not as inventory entries.
- **Plan features:** the four comparison tables on the pricing page (Features, Payment Processing, Sales Channels, Service & Support). The tables are collapsed on the rendered page; they were read from the raw HTML. The five Service & Support lines are out of scope (BigCommerce's own support service).
- **Product lines:** the "All Features" list on `https://www.bigcommerce.com/product/` (six groups, 45 lines). The site's top menu groups similar items differently and was not used as a list.
- **App Marketplace:** the 21 categories on `https://www.bigcommerce.com/apps/`, not individual apps.
- **Extra lists from BigCommerce's own pages:** the Embedded Payment Provider List on the pricing page (21 providers), the MSA's Contracting Entity table (7 rows), and the Third-Party Subprocessors page (21 subprocessors).

## Concerns

{CON} concerns, named in BigCommerce's terms. Grouping and splits are given in `split_note`. The main choices:
- the four Catalog product groups form one concern; brands and categories are separate;
- payments are split into payment processing (Payments API), payment methods, stored instruments, BigCommerce Payments, the Embedded and Open Payment Providers, digital wallets, PCI, Unified Billing, fees and billing, and B2B invoices and payments;
- tax configuration and tax providers are separate, and so are shipping and shipping providers;
- the legal concerns follow the MSA's own sections and Incorporated Terms.

## Cells

| Placement | Cells with a statement | Cells with only a gap | Statements |
| --- | --- | --- | --- |
{CELLS}

{EXTRA_GAPS} gap rows sit in cells that also hold a statement. They record a specific point on the architecture concerns that BigCommerce does not state: who holds funds for BigCommerce Payments and for the other providers; a licence for Commerce's role as Unified Billing collection agent; screening by BigCommerce itself against sanctions lists; a per-store data region; and failure behaviour for payment and shipping providers.

**Gaps by kind:** {KINDS}. **By who can close them:** {WHO}.

## What could not be shown

- **Help Center.** `https://support.bigcommerce.com/llms.txt` redirects to the Help Center login page. Article pages answer HTTP 200, but the Salesforce site's script bundles (`/s/sfsites/l/.../resources.js`) answer HTTP 400 to headless Chromium from this session: the same URL answered 200 to curl, and disabling HTTP/2 did not change it. The raw HTML is a script shell without article text. The capture tool would meet the same failure, so no Help Center quote could be verified. The articles that BigCommerce's developer docs link to are listed in `not-reached.tsv` for the founder to save. Most "decides" gaps point there.
- **Platform Trust Center.** `https://security.bigcommerce.com/` answers with a Cloudflare security verification (HTTP 403). It was not worked around.
- **Plan cells shown as icons.** On the pricing page many plan cells are images (alt text `blue-checkmark`) rather than text. Statements quote the line and its tooltip. The notes give the cells as they appear; reading a check mark as "included" is marked as inference.
- **Holding money.** No page read names who holds shoppers' funds for BigCommerce Payments or for the other payment providers, or under which licence. BigCommerce Payments terms are not among the Incorporated Terms listed in the MSA. These points are recorded as gaps.

## Where sources differ

Each case below is recorded with its own citation and not resolved.

- **Plan names.** The pricing page names the plans Core, Growth, Scale and Performance. The developer docs on Locations and Rate limits use Standard, Plus, Pro and Enterprise. Both are recorded as stated.
- **BigCommerce Payments eligibility.** The payments page says "*Must be on BigCommerce Retail Plan to qualify". The BigCommerce Payments page's FAQ says "available only to US-based merchants with self-serve and retail plans".
- **The payments host is named two ways.** The Payment Processing reference calls the server on `payments.bigcommerce.com` both "BigCommerce's PCI-compliant Payments server" and the "BigCommerce Payments Gateway".
- **Inventory locations per plan.** The pricing page gives Up to 4, Up to 5, Up to 8 and Custom (Core to Performance). The Locations doc gives Standard up to 4, Plus up to 5, Pro up to 8, and Enterprise 100, which can be customized by request.

## Method notes

- **Quotes.** Quotes are copied from the fetched text and checked with the checker's own matching rules before capture (`scripts/qcheck.py`). Statements that quote a markdown table row join cells with " | ". The checker's "markup removed" form drops pipes, backticks and links, so these match. Webhook topics that support data filtering carry an asterisk after the topic, as on the page.
- **commerce.com pages.** Plain curl loops between `/terms/` and `/en/terms/` on a locale cookie (HTTP 307). The pages were read and captured through the browser render, which keeps the cookie; the capture keeps the browser's body.
- **Hidden content.** Some bigcommerce.com content is collapsed on the rendered page: the comparison tables, and the FAQ answers on the BigCommerce Payments and product pages. It was quoted from the raw HTML, and those citations say `raw`.
- **Rate.** Fetches were spaced at about one per second per host. Every working-copy fetch is in `fetched/log.tsv`.
- **Inference.** Inference appears only in notes and is marked "Inference:".
- **A slip, undone.** During the webhook parse check, a scratch file was written to `/tmp/x_all`, outside the run folder. It was deleted.
- **Platform terms.** In `concerns.tsv`, BigCommerce's names in `platform_terms` are separated by " | ", because one heading, "Checkout Environment; PCI", contains a semicolon.
