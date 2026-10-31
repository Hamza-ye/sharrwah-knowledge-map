# E-backfill-zid: notes

The back-fill after `E-zid`, which added one capability to domain E: CM-CNT-009, URL redirects (Zid: إعادة توجيه الروابط). This part writes its cells for Shopify, Salla and WooCommerce. It adds no capability and lands no concern.

`candidates --domain E --platform P --areas CNT` found nothing on any of the three: its terms are Zid's, in Arabic only. Each cell was then searched for the thing itself, an old address sent on to a new one, in English and, for Salla, in Arabic (singular and plural, with and without ال). The terms searched are in each cell.

## Shopify: held, on one statement, a reading

E-anchor's note (CM-CNT-006, and CM-CNT-005's capability note) says Shopify's URL redirects have no statement of their own and are named only in notes. Checked against the statements and the inventory:
- **No statement's identifier or text names redirects.** `search` for redirect, redirects, redirection, URL redirect, urlRedirect, url_redirect, redirects:list, redirect_entry, 301, forward, moved permanently and old url finds only other things: payment, billing, finance and agentic routes (SH-S-5026, SH-S-5044, SH-S-5064, SH-S-5167), payment and verification session redirects (SH-I-0140, SH-I-0145), and SH-I-2152, storefront redirection of customers by where they are. `outscope` finds no unplaced inventory entry for them.
- **SH-C-031/decides/SH-S-5123** is the route menus:list. Its note, not its text, says the same eligibility (entitlement storefront.enabled, permission LINKS) holds on redirects:list, redirects:new and redirect_entry:update. That is confirmed, as context only, in observed-sh@e49840729 `structures/shopify/admin-router/items.jsonl` lines 415 to 417 (section Content, title "URL redirects") and 816 to 819 (section OnlineStore). Not cited: the routes are only in the note.
- **SH-C-031/boundary/SH-S-6245** is the line "Requires `write_online_store_navigation` access scope. Also: Requires an active user." Its citation in `citations.tsv` locates it on the page of the mutation urlRedirectBulkDeleteAll (observed-sh@e49840729, `structures/shopify/dev-access-lines/shopify.dev_md/items.jsonl`, line 722). This part reads the citation's locator as the statement's source, a fact at a commit, not a note's inference. So the statement is a requirement of a mutation of Shopify's own API for its own feature, which the dry run's convention reads as `core`. **This departs from E-anchor's reading**, which counted the source page among the notes. If the reviewer reads it E-anchor's way, the cell becomes `none-held` with the terms above, and the reading already lists them.

So E-anchor's note holds for the statements' text: no statement of its own. It doesn't hold for SH-S-6245's source, which is the redirects mutation.

**Gap:** no statement is keyed on Shopify's redirects routes (redirects:list, LINKS, section Content) or on the redirects page of the API. One would place the admin feature as `core` without resting on a locator. SH-C-031/responsible is `stated only in general terms` and SH-C-031/reason is `searched, not found`, so the cell claims no responsibility and no reason.

**CM-CNT-006 is kept apart,** as its note says: Custom URLs is Salla's, and no Shopify statement is cited there. No statement is cited in both capabilities.

## Salla: none-held

No statement shows a link sent on to another. `services-redirect` (SA-C-205/decides/SA-S-3436; `scope.tsv` gives SA-C-205 domain F, and the checker's none-held match doesn't list it) is a feature flag of the merchant services marketplace, and its name is all it states. A flag's name isn't evidence of the capability. CM-CNT-006, Custom URLs, has an admin link, an API folder, a plan line, a permission and a flag, but no Salla statement defines a custom URL. So whether Salla's custom URLs redirect isn't stated, and the cell doesn't cite them. **Gap:** a Salla statement defining custom URLs would settle whether they are redirects, the same gap E-anchor named.

## WooCommerce: none-held

The hits are payment gateways that redirect the buyer to the processor, and Store API routes and admin menu entries keyed by slug. None sends a store's old address to a new one.

## The checker's flags

- **cells.tsv line 2, Shopify, core rests only on a boundary statement.** Yes: the cell's `core` rests on the scope the mutation urlRedirectBulkDeleteAll requires. The dry run's convention reads a mutation's requirement for the platform's own feature as `core`. That Shopify itself has a URL redirects page in its admin is shown only by SH-S-5123's note and by the evidence read as context, as above.
- **cells.tsv line 3, Salla, none-held with 2 matches:** SA-S-3262 is the flag order-comment, matched by its position 301; SA-S-5085 is التوجه, going to the complaints page. Neither is a redirect. services-redirect is answered above.
- **cells.tsv line 4, WooCommerce, none-held with 17 matches:** payment redirects (WC-S-0624, WC-S-0607), Store API routes by slug (WC-S-0177, WC-S-0180 to WC-S-0182 and their inventory entries), and the admin menu slugs WC-S-5420 and WC-S-5439. None is a redirect of the store's links.

## Problems

- The candidates use only the terms of the platforms with cells. CM-CNT-009 had only Zid's Arabic terms, so they found nothing on the English platforms. The cells rest on the searches above.

## The coordinator's ruling (30 October)

- **A statement's citation says what it is about.** SH-S-6245 reads only "Requires `write_online_store_navigation` access scope. Also: Requires an active user." Its citation places it on the documentation page of Shopify's mutation `urlRedirectBulkDeleteAll` (observed-sh@e49840729, `structures/shopify/dev-access-lines/shopify.dev_md/items.jsonl`, line 722). The citation's source and locator are part of the fact, traced to its source at a commit, so the statement is a requirement of that mutation: Shopify's own API for its own feature, `core` by the dry run's C1. This is not a note: convention 5's "a note never counts" stands. It is a method ruling, listed for the founder's veto with the extent's report, and the final review checks the other cells that rest on a citation's locator in the same way.
