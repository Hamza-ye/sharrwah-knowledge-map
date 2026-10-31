# Notes: held pass, Salla, batch SA-24 (`design-page-types`, `design-settings`, `docs-event-lists`, first part)

## What I read

- The brief, `H-held.md`; the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; its `structures/REGISTER.tsv` rows for the three structures; `index/ledger-summary.tsv` (`webhook-event` is the ledger these lists bear on).
- The three structures' `meta.json` and selection rows (`design-page-types` read with `drop:default_content`; `docs-event-lists` 'the ones not cited').
- **Sources:**
  - `design-page-types`: `demo@en/source.json`, GET `/admin/v2/design/pages/types` in run `20261008T202107Z-journey-info-pages-demo`, step 2. To clarify it, that run's `actions.jsonl`, `steps/002.text.txt` (the New information page form) and its `index/run-notes.tsv` row.
  - `design-settings`: `demo@en/source.json`, GET `/admin/v2/design/settings?version_id` in run `20261008T203531Z-journey-landing-pages-demo`, step 6, where the theme editor opened on the new landing page (`/themes/editor?landing-1762937504`); that run's `actions.jsonl`, `responses.jsonl`, `steps/005.text.txt`, `steps/006.text.txt` and run note.
  - `docs-event-lists`: each label's `source.md`, and its record in `raw/runs/20261005T234928Z-docs-md/fetch.warc.gz`, which the readings cite: events-brand `@1177694`, -cart `@1173964`, -category `@1151166`, -communication `@1180972`, -customer `@1156880`, -invoice `@1144958`, -order `@1184382`, -review `@1165956`, -shipment `@1170086`, -shipping-company `@1163376`, -shipping-zone `@1148258`, -special-offer `@1154009`, -store-branch `@1160382`; app-functions/welcome `@1090813`; comm-apps/event-payload-reference `@1379312`; conditional-webhooks `@39530`; partner-apis/app-events `@1215456`; recurring-payments/changelog `@1344047`, /webhook-events `@1341772`; webhook-events/communciation-apps `@212637`; webhooks `@29604`.
- SA-2's, SA-9's and SA-32's placements for the canvas, the themes editor and the plan gates of `/channel/pages` and `/themes/landing-pages`; WC-8's webhook topics, for the practice the coordinator let stand; the coordinators' checks at the end of SA-1 to SA-9 and SA-32.
- The cells of every capability my lines name, and `caps --terms` for the things no lead named.

## The batch, and the batches beside it

- SA-24 holds all of `design-page-types` (5) and `design-settings` (12), and the first 113 of `docs-event-lists`' 169 uncited entries: the App Functions event pages (42), the App Functions welcome page (18), the Communication Apps' payload table (1 of 3), Conditional Webhooks (35), App Events (4 of 13), Recurring Payments' changelog (5) and webhook events (5), Communication Webhooks (1 of 18), and the first two rows of the Webhooks page's 'List of Salla Store Events'.
- **SA-25 holds the rest of `docs-event-lists`, and hasn't run:** the Webhooks page's rows 3 to 58 (`order.status.updated` to `review.added`). The rules below are for it to keep to.
- **SA-23 holds `dashboard-webhook-events`, and hasn't run.** Its 63 entries are the events a store's own dashboard offers for a webhook (a label in Arabic, an event name). Its entries meet my lines on the same events:
  - brand.created, .updated, .deleted (my 18 to 20, 64, 109 to 111);
  - abandoned.cart and abandoned.cart.status.changed (21, 23, 67, 112). Its abandoned.cart.update is the App Functions page's abandoned.cart.updated (22) by role, a reading; the names differ;
  - coupon.applied (24, 68);
  - category.created, .updated (25, 26, 65, 107, 108);
  - communication.sms.send, .email.send, .whatsapp.send (27 to 29, 78);
  - customer.created, .updated, .login, .otp.request (30 to 33, 63, 101 to 104);
  - invoice.created (34, 69);
  - review.added (45, 71, 113);
  - shipment.creating, .created, .cancelled, .updated (46 to 49, 62);
  - shipping.company.created, .updated, .deleted (50 to 52). Its labels for shipping.zone.created and .updated are 'انشاء تسعيرة شركة شحن' and 'تعديل تسعيرة شركة شحن', a carrier's pricing, where my 53 and 54 follow CM-SHP-001's cell (shipping zones). SA-23 may want CM-SHP-015 too;
  - specialoffer.created, .updated (55, 56, 70, 105, 106);
  - store.branch.created, .updated, .deleted (57 to 59, 66);
  - storetax.created (66's tax configuration);
  - product.created, .updated, .deleted, .available, .quantity.low (61, 96 to 100);
  - subscription.created, .charge.succeeded, .charge.failed, .cancelled, .updated (118 to 127).

  Its own lines go on CM-API-009 (webhooks set up in the admin), whose cell holds `/manage/webhooks`, beside each event's resource capability. My lines name no CM-API-009, since docs pages aren't the admin.

## Rules my lines follow (for SA-25 and SA-23)

1. **Each event is `core` on the capability of what it is about,** as the platform's own API for its own feature (H-held rule 4; B-extent's convention), and as the model's Salla cells already cite the same events (`event order.created`, `webhook brand.created`). WC-8 placed WooCommerce's topics the same way, and its check let it stand.
2. **Each list adds one line for what the list is:**
   - an App Functions page (`app-fuctions/events-*`, `app-functions/welcome`): CM-APP-005 `core`, as the cell's event folders Merchants Events and Customers Events are `core`. The developer writing the function is the cell's `extension-point` (SA-S-0187), not each event's;
   - Conditional Webhooks: CM-API-010 `core`. I gave these rows no CM-API-008 line: the Webhooks page's own rows carry it for the same topics, and CM-API-010 is its child;
   - the Webhooks page's 'List of Salla Store Events', and Recurring Payments' 'Webhook Events': CM-API-008 `core`, as WC-8;
   - the Recurring Payments changelog: CM-API-006 `core` too, a record of the API's change log, with the release date in `reading`;
   - App Events (Partner APIs): CM-APP-004 `core` only, by CM-API-008's note ('The topics on an app's own lifecycle are CM-APP-004's');
   - Communication Apps' events and Communication Webhooks: CM-NTF-004 `extension-point`, as the cell holds the same tables ('These webhook events are allowed only for Communication applications.').
3. **Recurring Payments' events are `extension-point` on CM-SEL-001,** as the cell's subscription webhooks (SA-S-0195: authorized third-party apps enable the feature).
4. **The buyer's storefront events** (the welcome page's 'Customer E-commerce Events') are `shows` on CM-MKT-009 and on the capability each names, as those cells hold the same family's events (Product Added, Products Searched, Signed In, Promotion Viewed, Product Added to Wishlist) as `shows`.
5. **The resource capabilities used:** brands CM-CAT-005; categories CM-CAT-003; products CM-CAT-001; product.available CM-INV-001 (the cell's term); product.quantity.low CM-INV-004; abandoned carts CM-CHK-007 (not CM-MKT-022's recovery); coupons CM-MKT-002; special offers CM-MKT-003; customers CM-CUS-001; login and OTP CM-CUS-010; orders CM-ORD-001 (with .products.updated, .payment.updated, .total.price.updated and .shipping.address.updated, as the cell); order.status.updated CM-ORD-003; order.cancelled CM-ORD-004; order.refunded CM-RET-002; order.deleted CM-ORD-012; order.coupon.updated CM-ORD-001 and CM-MKT-002; order.shipment.* and shipment.* CM-SHP-009; order.shipment.return.* CM-RET-003; shipping.company.* CM-SHP-015; shipping.zone.* CM-SHP-001; store.branch.* CM-INV-005; storetax and tax CM-TAX-001; invoice.created CM-ORD-008; review.added CM-SUP-001; communication.* CM-NTF-004.
6. **For SA-25's own rows,** leads I found but didn't place (its entries): product.price.updated CM-CAT-013 (its name holds the event); product.category.updated CM-CAT-003 and product.brand.updated CM-CAT-005 (both cells cite them); product.tags.updated CM-CAT-006; product.image.updated CM-CAT-007; store.branch.setDefault and .activated CM-INV-005. Its two struck rows, `~~product.updated~~` and `~~product.available~~` (`webhooks/source.md` lines 277 and 279), are struck by the page itself: I'd read the strike as the platform no longer offering the topic there, `shows`, with the strike in `reading`. Conditional Webhooks (my 99) and the dashboard (SA-23) still list product.available unstruck.
7. **Quotes** are each row's own Description; the page's surrounding words are cited at its record, as above.
8. **No scope** on any docs line: the pages state no plan, store or country. The design lines take none either (below).

## The design lines

- **Page types** (1 to 5) are the Page type options of Store & Channels > Information pages, CM-CNT-003 `core`, and Return Policy and Privacy Policy also CM-CNT-008 `core` (the cell's information pages that carry the store's policies). **Customised** (5) is `shows`: the API lists it, but the form offers only 'General', 'Return Policy', 'Privacy Policy' and 'HTML Code' (`20261008T202107Z-journey-info-pages-demo/steps/002.text.txt`).
- **The design switches** (6 to 8) are store design's, CM-SFR-001 `core`: content protection and Salla's copyright message are the same things as the cell's حماية محتوى المتجر, content-copyright and remove-salla-copyright. They are fetched by the themes editor, but a toggle's own thing isn't the editor (SA-9's CM-SFR-002 routes): I gave them no CM-SFR-002 line. The help centre's article puts content protection under the editor's Design Options ('From the Store Design page, click Customize on the selected theme', `structures/salla/help-articles/en/texts.jsonl`): if the coordinator reads these as the editor's 'Theme settings' route (SA-9's SA-E-6e43adc4), each takes CM-SFR-002 `core` too.
- **The landing page's settings** (10 to 17) are CM-SFR-006 `core`, the cell's landing pages, which SA-9 and SA-2's check keep there for the editor's landing route and the canvas. The product field (13) names the quick purchase element, CM-CHK-008 `core`; the apps' codes switch (17) names the installed apps' snippets, CM-SFR-004 `extension-point`.
- **Scope:** none. The responses are the demo store's (Pro), as `run.json` `extra.store` and the run notes say, but the source names no plan or store, and the label is the capture's. Each reading names the store; the store's values (false, true, صفحة هبوط رقم (1), فستان) are in `reading`.
- **Qualities:** the fields' maximum lengths (100, 50, 1), as `page title maxLength: 100`, by the model's practice of a limit's key and value.

## The new thing

- **`new:Use arabic numbers`** (6, `shows`): the switch 'Use arabic numbers' (`arabic_numbers`), value false on the demo store. No place of its own: one switch of the store's design. Proposed domain E, area SFR, parent CM-SFR-001 (or CM-MKS-008, languages, if the coordinator reads numerals as localization). Its Arabic label isn't held: the response is in English (`demo@en`). Searched: numbers; numeral; أرقام; الارقام; number format; localization; translation; languages. Its entry also takes CM-SFR-001 `core`, as a switch the store design offers.

## Entries I couldn't tell, and what would settle each

- **5, Customised:** `shows`, as above. The themes editor's own pages may be where a customised page is made; a run that opens a page of that type would settle it, and `core` is the alternative.
- **10, 'خيارات المنتج':** a static title in the settings list, placed as a container on CM-SFR-006, the settings it heads being the landing page's. Its words name product options, CM-CAT-002's term, which I read as a homonym. `out` as a layout node is the alternative.
- **27 to 29, the App Functions communication events:** `core` on CM-NTF-004, since the page says only 'Triggered when a sms is sent to a customer'. The Communication Apps' page (78) says the same events reach the app that takes over delivery, which the cell places `extension-point`. If the coordinator reads the two pages as one API, these are `extension-point` too.
- **72, Checkout — started, step completed,** listed under Merchant Events though the cell CM-MKT-009 holds Checkout Started as a buyer's storefront event: `core` on CM-CHK-001 and `shows` on CM-MKT-009.
- **73's 'shared'** on CM-SFR-016, `shows` (below, CHANGES).
- **99, product.available:** CM-INV-001, the cell's term. What makes a product available isn't stated on the Conditional Webhooks page; the Webhooks page strikes the topic ('This event is triggered when a product's stock has been available.'), and the dashboard lists it ('المنتج متاح'). CM-MKT-016 (back-in-stock alerts) is the alternative, by the description's stock.
- **117, app.subscription.started**, 'for an app or an app addon': CM-APP-004 only. The app's subscription itself is CM-APP-003's thing (App Subscriptions); the event names its start, not its charge, so I gave CM-APP-003 no line.
- **128, the Communication Webhooks' order.status.updated:** CM-NTF-004 `extension-point`, as the cell's types, and CM-ORD-003 `shows`, since the message names the order's new status.

## A structure whose items and sources disagree

- **`design-settings`:** the source's label is 'عنوان  الصفحة', with two spaces, where the item and the rendering hold one ('عنوان الصفحة'); the type labels are 'صفحة هبوط منتج ' with a trailing space and ' تهدف…' with a leading one. The terms keep the rendering's single space. The item also leaves out each field's `icon`, `selected` and `labelHTML`.
- **`docs-event-lists`, Conditional Webhooks:** the event names carry a space inside their backticks ('`order.created `'), as the page writes them. The items keep it; the terms drop it.
- **The pages' own slips, as held:** on the App Functions cart page, abandoned.cart.updated and abandoned.cart.status.changed have abandoned.cart's description, 'Triggered when a customer abandons their shopping cart' (`app-fuctions.events-cart/source.md`, lines 7 to 9). The Webhooks page's order.shipment.created and .cancelled read 'an order shipment return' (lines 265 and 266), and its invoice.created (line 354) fires 'when the order status is either `completed` or `restored`', where the App Functions page says 'when an invoice is created for an order'. These are SA-25's.
- **`design-page-types`:** `default_content` is dropped from the items by the selection's rule; the source holds it (below).

## What the sources state that no entry holds (for the second stage)

- **Conditional Webhooks' definition** (`conditional-webhooks/source.md`, lines 11 to 22 and 58 to 64; `…@39530`): Salla Rules filter a webhook's payload by conditions on attributes ('Rules contain basic filtering, which allow writing conditions and then afterwards receive particular payload based on the written condition.'), with operators such as `payment_method = mada OR price < 50`, registered on the merchant's dashboard 'not on the Partners Portal' (line 92). CM-API-010's cell says its definition isn't held; my lines quote it. Each event's attribute tables (lines 304 onward: an order's `branch_id`, `coupon_code`, `payment_method`, …; a product's `sku`, `price`, `quantity`, …) aren't entries.
- **The Webhooks page's delivery terms** (`webhooks/source.md`, lines 236 and 240; `…@29604`): Salla waits 'for around 30 seconds', and with no successful response 'it would trigger the webhook event three times', 'around five minutes' apart. Qualities for CM-API-008.
- **The App Functions pages' Common Use Cases and execution types:**
  - the cart page's 'Send cart recovery emails' and 'Offer discounts to recover carts' (`app-fuctions.events-cart/source.md`, lines 21 to 24), a lead for CM-MKT-022 through apps;
  - the shipment page's 'Calculate custom shipping rates' and 'Generate shipping labels' (`app-fuctions.events-shipment/source.md`), leads for CM-SHP-004 and CM-SHP-002;
  - each page's Event Type (Asynchronous, or Synchronous for shipment.creating), and the welcome page's pricing: 'App Functions are currently in **beta** and **free of charge**' (`app-functions.welcome/source.md`, line 71), with the future pricing by calls, execution time and resource usage (lines 73 to 75), which CM-APP-005's cell holds as a statement but not the pricing basis.
- **The Recurring Payments changelog's endpoints** (`recurring-payments.changelog/source.md`): `PUT /subscriptions/{subscription_id}`, 'Update Subscription Payment Method', and the Create Order fields `products.recurring` and `payment.recurring` (1.1.0, 2025-11-30). For CM-SEL-001 and CM-PAY-022.
- **The information pages' default content** (`design-page-types/demo@en/source.json`): Salla's ready return and exchange policy text ('the consumer has the right to replace the product provided to him from the store within the seven days following the date of receipt of the product') and its usage and privacy policy text, each in Arabic and English. For CM-CNT-008, and for CM-RET-003 as a policy the platform drafts.
- **The landing pages' page** (`20261008T203531Z-journey-landing-pages-demo/steps/005.text.txt`): the template marketplace's industries and paid templates ('Buy now', '287.5'), for CM-SFR-003 and CM-SFR-006.

## The checker's lines, read again

- **`CHANGES` CM-SFR-016 becomes held, by line 144** (73, 'Product Interactions — viewed, clicked, searched, shared, reviewed', `shows`). The welcome page lists 'shared' among the buyer's storefront interactions that trigger App Functions, 'Triggered by storefront interactions, always asynchronous' (`…@1090813`), and the App Functions product page, which is cited elsewhere and isn't an entry, names it 'Product Shared - Customer shares a product' (`app-fuctions.events-product/source.md`, line 13). So the storefront lets a buyer share a product. What shares it (a button, a link) isn't stated, and CM-SFR-016 is share buttons. I kept the line as `shows`, which supports no placement; the coordinator may drop it, the cell staying empty.
- **`NOTE` 'core on a product named with the platform's brand'** (lines 263 to 266, 129 and 130): the brand is the page's heading 'List of Salla Store Events', not a product. `core` by what the rows show, Salla's own webhook topics.
- **`NOTE` line 146** (74, 'Cart & Checkout — … checkout flow'): its first lead CM-AUT-001 matched 'flow'. Workflow automation isn't the entry's thing; the checkout flow is CM-CHK-001's, which the entry's line names.
- **`NEW`:** Use arabic numbers, above.

## Problems with this brief or the script

- None that blocked. The selection's 'the ones not cited' leaves out the App Functions pages whose items the concern map cites (product, account, wishlist, cart-checkout, promotion-coupon), so the batch holds the merchant events' pages and not the buyer's. The welcome page's buyer lines are the batch's only buyer events.

## The coordinator's check (30 October 2026, after the batch)

- **The CHANGES line stands:** CM-SFR-016, social sharing, is held by a `shows` line. The welcome page's storefront events name products 'shared', and App Functions' 'Product Shared - Customer shares a product'. What does the sharing isn't stated, so the cell gains no placement, and the second stage reads it with the cells that hold nothing.
- **The event lines stand.** Each event is `core` on the capability of what it is about, beside the list's own line, as WC-8 placed WooCommerce's webhook topics. SA-25 keeps to the rules in the notes, and SA-23 meets the events the notes list.
- **The page types and design settings stand,** on the cells that hold the same rows, with no scope: the source names no plan, and the readings name the demo store.
- **New thing:** 'Use arabic numbers', a switch of the store's design. It is decided with every platform's new things, beside CM-SFR-001 and CM-MKS-008.
- **Cost:** 18.9 million tokens over 93 requests, about 145,000 an entry, most of it the event lists' two lines an entry. One cell is held, by a `shows` line.
