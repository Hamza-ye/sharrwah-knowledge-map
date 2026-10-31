# SH-103: notes

**Batch:** 42 entries the concern map didn't cite, of two of Shopify's structures:
- `translatable-resources` (33): Translate & Adapt's home in the admin, held from run `20261007T131249Z-journey-shopify-apps-2`, step 11's frame (`steps/011.frame-0.aria.yaml`). The page is at `admin.shopify.com/store/capture-plus/apps/translate-and-adapt/?shopLocale=en&market=canada`, its frame `app-iframe` at `store-localization.shopifyapps.com` (`actions.jsonl`, step 11).
- `ui-extension-targets` (9): the admin and POS targets of `@shopify/ui-extensions`, by the selection's rule `latest:target`.

Evidence cited at observed-sh `e38dc17e3`, as the entries are.

**Count by placement:** 42 entries in 48 lines.
- `capability`: 36 entries, 42 lines. Six entries take two lines each: SH-E-b9fd7154, SH-E-a21f1e24, SH-E-0dbd2476, SH-E-d2531436, SH-E-1e0ccd75 and SH-E-c84a6808.
- `out`: 6 entries.
- `new`: none.

No batch had placed these two structures, so the rules below are this batch's own, for the coordinator to check.

## Rules this batch set

**Translate & Adapt's home (`translatable-resources`)**

- **R103.1:** A kind of content that Translate & Adapt's home lists is the store's translation of that content: CM-MKS-008, `own-service`.
  - Translating it is the app's own feature, and held posts name the app's maker: SH-E-04551fad ('we've added automatic translation updates to Translate & Adapt') and SH-E-ff15a593 (“Shopify’s Translate & Adapt app”). This follows the ruling after SH-55 and SH-21's, SH-36's and SH-41's lines.
  - Each of my entries is the heading inside one of the buttons that Q1 cited. Q1 placed those buttons (SH-I-2066 to SH-I-2084) in SH-C-032, Languages and translations, which is CM-MKS-008's concern. So each heading takes the button's capability.
- **R103.2:** The content itself takes no line of its own, because its own capability holds on Shopify in every case (the message's rule, after SH-28's check). The capabilities are:

  | Content | Capability |
  | --- | --- |
  | Collections | CM-CAT-003 |
  | Blog posts, Blog titles | CM-CNT-004 |
  | Cookie banner | CM-TRU-006 |
  | Filters | CM-SFR-013 |
  | Metaobjects | CM-CNT-002 |
  | Pages | CM-CNT-003 |
  | Policies | CM-CNT-008 |
  | Store metadata | CM-CNT-007 (a reading: the store's metadata for search engines) |
  | Menu | CM-CNT-005 |
  | App embeds | CM-SFR-004 |
  | Default theme content, Section groups, Static sections, Templates | CM-SFR-001 |
  | Theme settings | CM-SFR-002 (SH-14's line) |
  | Notifications | CM-NTF-001 |
  | Shipping and delivery | CM-SHP-001 |

- **R103.3:** The page's five group headings are containers of the app's list, so each goes on CM-MKS-008, `own-service` (rule 3).
  - Each group's children are all CM-MKS-008's lines, so none is a grouping over several capabilities (the ruling after SA-28).
  - Each title's own capability holds on Shopify: Products is CM-CAT-001, Online Store and Theme are CM-SFR-001, Content's only child is CM-CNT-005. Settings names no capability of its own. So none takes another line.
  - The containers and their children:

    | Container | Children |
    | --- | --- |
    | Products (SH-E-cd13d05e) | Collections, Products |
    | Online Store (SH-E-89a03991) | Blog posts, Blog titles, Cookie banner, Filters, Metaobjects, Pages, Policies, Store metadata |
    | Content (SH-E-5a7a4f9e) | Menu |
    | Theme (SH-E-2e8ccd79) | App embeds, Default theme content, Section groups, Static sections, Templates, Theme settings |
    | Settings (SH-E-c6b66e50) | Notifications, Shipping and delivery |

- **R103.4:** The page's title, 'Localized content:' (SH-E-b9fd7154), takes two lines:
  - CM-MKS-008, `own-service`;
  - CM-APP-007, `core`, as the admin's page for the app (M-10; the ruling after SH-55), as SH-50's line on the same address has it.
- **R103.5:** The language card.
  - A language's name (English, SH-E-07264119 and SH-E-b90261e6) is `out`: a language is market data, and which language is shown, or is the default, is the store's own value.
  - The badge Default (SH-E-5637188b) names the store's default language. That is a setting of the store's own languages, which the app shows, so it is `core` (a reading). Its value, English, goes in `reading`.
  - The paragraph (SH-E-feb59e10) is `core;own-service` on CM-MKS-008:
    - `core`: the default language, 'visible to all customers';
    - `own-service`: 'Versions customized for markets', the app's versions adapted per market (SH-31's 'market-specific wording', placed so).
- **R103.6:** The guide card.
  - Its heading and text name only a guide to content localization, so both are `shows` on CM-MKS-008. In 'our quick start guide', 'our' names the guide, not a maker (the ruling after SH-55).
  - The buttons View store, Manage and Quick start guide are `out` as UI strings. The frame's HTML gives the first two no address. The third opens the app's own modal.

**UI extension targets (`ui-extension-targets`)**

- **R103.7:** A target is `extension-point` on its surface's extension capability: admin targets on CM-APP-008, POS targets on CM-POS-004.
  - This follows the message, R49.3, and the cells. CM-APP-008 cites admin_print (SH-I-1432). Q1 placed the selection print actions' render targets (SH-I-1539, SH-I-1540) in SH-C-164. CM-POS-004 cites pos.home.tile.render (SH-I-1667).
  - Where the model cites the same target on another capability, it takes that line too (rule 2). The segment template target (SH-E-a21f1e24) takes CM-CUS-002 beside CM-APP-008: CM-CUS-002 cites its later form `admin.customers.segmentation-templates.data` (SH-I-1496), which Q1 placed in both SH-C-040 and SH-C-164.
  - CM-ORD-009's note sends the print action to CM-APP-008, so entries 34 and 35 take no CM-ORD-009 line.
- **R103.8:** Where a target's words say that apps open the connected cash drawer through the Cash Drawer API, the target takes CM-POS-003 `extension-point`. This is R49.3's 'apps do the work through the platform's APIs', as SH-E-683cb064's line on the POS's register targets and APIs has it.
  - The sentence is new in point-of-sale 2026.10.2. It isn't in 2026.7.4's words for `pos.home.tile.render` or `pos.home.modal.render`.
- **R103.9:** A target whose only doc, or whose doc's last tag, is `@private` isn't offered to apps.
  - Where it names a place, it is `shows` on its surface's capability, as an unreleased flag is (the brief's flags ruling): `pos.cart.validations.resolution.render` and `pos.payment.validations.resolution.render`. Each also takes `shows` on CM-CHK-005, for the validation its interceptor returns.
  - Where it names no place, it is `out`: `Playground` (admin 2025.7.4), with StandardApi and AllComponents, whose doc is '@private' alone.
- **R103.10:** The versions that state a target in its words (the entry's labels) go in `reading`, not `scope`.
  - An API version isn't a plan, a country, a market, a store or an account (rule 5).
  - A target that the latest versions no longer state keeps its line, with that fact in `reading` as a release marker:
    - `admin.order-index.selection-print-action.should-render` and `admin.product-index.selection-print-action.should-render` are in admin 2025.10.16 to 2026.7.1. They aren't in 2026.7.4, 2026.10.0-rc.11 or 2026.10.2. Those versions keep both `.render` targets and the details pages' `print-action.should-render` targets.
    - `admin.customers.segmentation-templates.render` (a RenderExtension) is in 2025.7.4 only. From 2025.10.16 on, the one segmentation target is `.data`, a RunnableExtension.

## CHANGES the checker prints

- **CM-MKS-008 gains `own-service`** (25 lines). The model's cell is `core;extension-point`, and it reads the help section on Translate & Adapt (SH-I-2163) as `shows`, 'its maker isn't stated'.
  - The held pass has since found the app's maker statements: SH-E-04551fad, SH-E-d4e7e31f, SH-E-ff15a593 and SH-E-fbf5a621 (`held_entries.py makers`).
  - Earlier batches already give the cell `own-service`: SH-21:55 and 60, SH-31:44, SH-36:104 and 136, SH-39:205, SH-40:157, SH-41:75, SH-42:170, SH-47:77 and SH-55:82.
  - So the change is the ruling after SH-55's ('Translate & Adapt's 1 line', aligned), not this batch's alone. I kept it.
- **CM-POS-003 gains `extension-point`** (lines 42 and 44, the Cash Drawer API lines).
  - SH-E-683cb064's line already gives the cell `core;extension-point` ('added new register extension targets and APIs'; 'New POS targets let apps plug into open/close procedures').
  - So the change waits only on that batch's amendment. I kept it.

## Entries I couldn't tell, and what would settle each

- **SH-E-9c76fc30, `Playground`:** I placed it `out` as a scaffold for no place. If a held statement says what the Playground target is, it could be `shows` instead: on CM-APP-008, or on CM-DVT-001 if it is a developer tool's playground. Shopify.dev's admin extensions reference would settle it, if it names the target.
- **SH-E-c84a6808, CM-CHK-005 line:** I read a `paymentvalidations` interceptor's validation as app-written validation at the POS's checkout, CM-CHK-005's thing. Its words say only that the target 'Renders the remediation interface when a `paymentvalidations` interceptor returns a validation.'
  - The package's POS `events` module (`./events`, imported at `point-of-sale@2026.10.2/source.d.ts`, line 4: `CartValidationsEventData, PaymentValidationsEventData`) would say what each interceptor validates. Its `.d.ts` is in dev-mcp 1.18.0's package, run `20261031T003934Z-npm-dev-mcp-1.18.0-cli-5.0.0`, and isn't extracted as a structure.
  - If it says the validation doesn't stop the payment, the line would go.
- **SH-E-feb59e10:**
  - Its `core` part rests on reading 'Your default language' as the store's language setting. The app's text doesn't say where that setting is, and the Manage button has no address in the HTML.
  - 'Versions customized for markets' also names Markets (CM-MKS-001, whose reading cites market customizations of theme content and languages, SH-S-0541). I gave it no CM-MKS-001 line, because Markets holds on Shopify and the versions are the app's own content (as SH-31's line on 'market-specific wording' has it).
  - The coordinator may prefer a CM-MKS-001 `shows` line.
- **SH-E-5637188b, Default:** I placed it `core` as the default-language setting's badge. Read as only the store's value, it would be `out`.

## Structures whose items and sources disagree

None found:
- `translatable-resources`' 55 items agree with `source.aria.yaml` and with the frame's `steps/011.frame-0.text.txt`, 34 lines.
- The `ui-extension-targets` items I read (`admin@2026.10.2`, `point-of-sale@2026.7.4` and `@2026.10.2`) agree with their `source.d.ts`, lines 228 to 238.

## What a source or run step states that no entry holds (M-12), for the second stage

- **The app's onboarding modal,** which the Quick start guide button opens (`raw/runs/20261007T131249Z-journey-shopify-apps-2/steps/011.frame-0.html`, line 20, in the modal `get-started-onboarding-modal`).
  - Its heading is 'Get started with Translate &amp; Adapt' (HTML-escaped).
  - Its first slide reads 'Localize everywhere', then 'Localize right from where you create content, across Shopify', then 'Access the editor by finding Localize under More actions for any resources like products or collections, and in your Online Store sections. You can also access the editor by selecting a resource from the app home page.', with '1 of 5'.
  - It holds only the first of five slides. It names the app's editor, reached from More actions > Localize on a resource and from the Online Store sections. That is a lead for CM-MKS-008's places in the admin.
- **The admin frame of the same step** (`steps/011.aria.yaml`, lines 76 to 80 and 95) names the app 'Translate & Adapt' in the navigation, with 'Pin to your navigation', and in the breadcrumbs. These are the admin's navigation and are probably held by its own structures; I didn't check.
- **The page was opened with `shopLocale=en&market=canada`.** No held step shows the list for another language or market, or the editor of any resource. Those would show whether the list differs by market or plan. capture-plus is on Plus, per the page's title, 'capture plus · Translate & Adapt · Shopify Plus'.
- **POS 2026.10.2's `./events` module,** for what the two interceptors validate (above).

## Problems with the brief or the script

- **`held_entries.py earlier` found no twin for any of the 18 resource headings,** though each is the heading inside a button that Q1 cited, one line above it in the same `items.jsonl` (SH-I-2066 to SH-I-2084, the concern map's `citations.tsv`). The twin search seems to cover held-pass entries only, not Q1's inventory entries at an adjacent locator.
  - I found them with `class_slice.py search`.
  - A later batch of an ARIA structure, where a button wraps its heading, would be helped if `earlier` printed the inventory entry of the enclosing node.
- **The checker printed no container note for the five group headings,** though the brief says it notes each container. Their readings say 'a container'.
- **The selection's `latest:target` labels an entry by the versions that state it in its latest words.** The entries don't show whether a target is absent from the latest versions or only worded differently there. I read the other versions' `items.jsonl` for each, which `show` doesn't print. Printing that in `show` would save the lookup.

## The coordinator's check

Measured: 9.5 million tokens over 62 requests, about 226,000 an entry. The checker prints no problem.
- **Kept:** R103.1 to R103.10 and both `CHANGES` lines: CM-MKS-008 `own-service`, Translate & Adapt's maker held and the ruling after SH-55 applied, as ten earlier batches have it; CM-POS-003 `extension-point`, the Cash Drawer API, as SH-E-683cb064's line has it.
- **The entries left open** (Playground `out`, SH-E-c84a6808's CM-CHK-005, the paragraph's markets, the 'Default' badge `core`): kept as placed. `translatable-resources` and `ui-extension-targets` are placed whole.
