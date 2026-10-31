# SH-85: notes (Shopify, `notification-templates`, 80 entries)

**What the batch is.** The structure's two pages, Settings > Notifications > Customer notifications and > Staff notifications, on fake-demo-sharrwah (run `20261007T102602Z-journey-notifications`, steps 1 and 2; observed-sh at `e38dc17e3`). The batch holds the items the concern map doesn't cite: each template's line ('Sent when …'), the groups' buttons, the page's frame, the Shopify Messaging card, Remarketing with Shop and the staff page's recipients. The templates' names (the listitems' links) and the headings are the concern map's inventory entries (SH-I-1998 to SH-I-2065). Rule 1 reads each line with its listitem's link and its group, so each reading names its template. No batch had placed this structure before.

## Rules set by this batch (R85.n), for the coordinator to check

- **R85.1, the page's frame.** The breadcrumb 'Notifications' (entry 1, on both pages) is `out`: by the ruling after SH-37, the admin's frame and its breadcrumbs are `out`. The page's title, Customer notifications, is CM-NTF-001 `core`, as SH-14 placed its route. So is the link Customize email templates, the route `email-settings` (section Notifications, PREFERENCES), which the cell's reading already cites.
- **R85.2, the groups.** Each group's button (Order processing … Accounts and outreach, all `[expanded]`) is a container of templates. It is CM-NTF-001 `core` alone (R14.7), as SH-14 placed the route's ten anchors (SH-E-6e0f3042). What a group's templates are about gives the group no line (M-6 refined).
  - Several group titles match other places' labels: Gift cards, Store credit, Local delivery, Point of Sale and Payments. Order processing also matches Settings > General's anchor, which SH-17 placed on CM-ORD-001. Each of these is another thing, and the readings say so.
- **R85.3, a template's line.** A template's line ('Sent …') is its template's statement. A customer notification is CM-NTF-001 `core`; a staff one is CM-NTF-002 `core`.
  - The coordinator's message reads it this way: the admin's own notification, at the settings section Notifications.
  - Where a template's own toggle shows in the step's text, the store's value goes in `reading`: '[x]' on, '[ ]' off (steps `001.text.txt` and `002.text.txt`).
  - Entry SH-E-6439d9dd is the line of two templates, the customer's Order confirmation and the staff's New order. It takes both lines.
- **R85.4, the event a template is sent on** (the coordinator's question). The event takes a line on its own capability. A description's named thing takes a line (M-6), and the event is what the line is about: it isn't named in passing (the ruling after SA-41). The support depends on what the message does:
  - **(a) `core`, where the message does that capability's own work.** It is, or carries to the buyer, the capability's thing:
    - an invoice, a gift card sent or a receipt asked for at the POS;
    - a return label or tracking;
    - an invitation to create an account, or a password reset;
    - a request to add or update a saved payment method, or B2B access;
    - a new order-status link, or a POS cart or draft order to complete online;
    - a payment reminder, a merchant's email to a customer, a consent confirmation or a recovery reminder.

    The platform does that work itself through its built-in template (B-extent's `core`). The model already holds messages so: CM-MKT-022's cell cites the template Abandoned checkout as `core`, SH-50 placed the payment reminders on CM-PAY-008, and SH-14 placed the double opt-in on CM-CUS-007.
  - **(b) `shows`, where the message only tells of an event that the capability does.** Examples: an order placed, fulfilled, edited, cancelled or refunded; store credit credited; a pickup's or a local delivery's state; a payment's failure or success; a return or cancellation request answered; an account activated. The line shows that the platform has the capability and gives its terms. It doesn't say who does the work or how, so it supports no placement (B-extent's `shows`).
  - **The notes and readings this keeps.** It keeps the capabilities' notes and readings that leave the templates themselves to the notifications: CM-ORD-008's reading leaves Order invoice and Draft order invoice to them, and CM-RET-004's leaves the cancellation requests to ORD's cells. Every template keeps its CM-NTF-001 or CM-NTF-002 line.
  - **How it differs from R14.7.** R14.7 ('CM-NTF-001's alone') was set on router routes, which carry no event words. SH-14 read a group's subject so: 'a notification of a return being no kind of return'. Here the descriptions name the event in the platform's words, so R85.4 adds the event's line, and R85.2 keeps the groups alone.
  - **CM-SHP-017.** Its note says 'The customer notifications that carry a shipping update are D's CM-NTF-001'. But its own `core` evidence SH-S-7208 is the built-in feature Order tracking, whose 'Get started' opens this page with `surface_detail=order-tracking`.
    - So the three templates that name a tracking number (SH-E-50789e61, SH-E-39c61556, SH-E-16dc5b5b) are also CM-SHP-017's, by rule 2's test that a cell's reading cites the same place. They take (a) `core`: the message shows the buyer the tracking.
    - They keep their CM-NTF-001 lines, as the note has it.
    - What would settle it: the part of the page the surface `order-tracking` opens. If the coordinator reads the note as excluding them, the three lines become `shows`.
- **R85.5, Remarketing with Shop.** Its description (SH-E-d74a80d0) says that Shop users get Shop's 'email and push reminders to buy', and that 'These settings extend those reminders to trigger based on activity on your storefront'. So the four reminders are Shop's.
  - Each takes `own-service` on its own capability: Shop is Shopify's own app (SH-S-0056; the ruling after SH-34).
  - They are settings with toggles (all '[x]'), not templates: no preview link, no editable email. So they take no CM-NTF-001 line.
  - Their trigger takes a (b) line where it names another capability's thing, by R85.4.
- **R85.6, the Shopify Messaging card** (in the group Marketing double opt-in). Its icon, its card and its button 'Open app' are the app's: CM-MKT-007 `own-service`, by its maker statement (SH-E-32e5ccc3) and the rename (SH-E-6be48c3e), the ruling after SH-37.
  - The button holds no address (`data-component-name="app-card-action"`, step `001.html`), so it takes no CM-APP-007 line: M-10 asks for the source to link the page.
  - 'Installed' is the store's state of the app: `out`.
  - CM-MKT-007's reading ('No statement names Shopify Messaging as a separate app's maker … SH-I-2056, is only a name') predates the ruling, which the coordinator aligns at the amendment.
- **R85.7, the staff page's recipients.** The two rows are the store's own recipients, each with 'All orders': `out`, as one store's own people and values. 'More actions' is a UI string: `out`. 'Add recipient' (the button and its paragraph) names the recipients setting: CM-NTF-002 `core`.

**R85.4, template by template** ((a) `core`; (b) `shows`; the template's own line is on CM-NTF-001 unless marked staff, on CM-NTF-002):

| Template | Entry | Event's line |
| --- | --- | --- |
| Order confirmation / New order (staff) | SH-E-6439d9dd | CM-ORD-001 (b) |
| Draft order invoice | SH-E-5109c5e5 | CM-ORD-005 (a): the draft orders' invoices; CM-ORD-008's note holds them apart as a homonym |
| Shipping confirmation | SH-E-dd07f96c | CM-SHP-009 (b) |
| Ready for local pickup; Picked up by customer | SH-E-b479ef2b; SH-E-4ef02383 | CM-SHP-007 (b) |
| Order out for local delivery; locally delivered; missed local delivery | SH-E-869a46c9; SH-E-5944b1f5; SH-E-8ef9d761 | CM-SHP-008 (b) |
| New gift card | SH-E-38528a74 | CM-LOY-002 (a) |
| Gift card receipt | SH-E-01dc6f92 | CM-LOY-002 (b) |
| Store credit issued | SH-E-8f6759fa | CM-LOY-001 (b) |
| Order invoice | SH-E-3a9ecb8d | CM-ORD-015 (b) |
| Order edited | SH-E-dc69f969 | CM-ORD-002 (b) |
| Order canceled | SH-E-afb9707c | CM-ORD-004 (b) |
| Order payment receipt | SH-E-c2e0b61a | CM-PAY-022 (b) |
| Order refund | SH-E-a055d6fc | CM-RET-002 (b) |
| Abandoned checkout | SH-E-b6e8c975 | CM-MKT-022 (a); CM-CHK-007 (b) |
| Order link | SH-E-1c425a87 | CM-CUS-010 (a) |
| Payment error; Pending payment error; Pending payment success | SH-E-3a19c814; SH-E-5bdb7d51; SH-E-e63109bc | CM-PAY-020 (b) |
| Payment reminder | SH-E-e9054453 | CM-PAY-008 (a) |
| POS abandoned checkout | SH-E-34194650 | CM-POS-001 (a); CM-ORD-005 (a); CM-MKT-022 (a) |
| POS email to customer | SH-E-5914956b | CM-POS-001 (a) |
| POS and mobile receipt | SH-E-7311a703 | CM-POS-001 (a) |
| POS exchange receipt | SH-E-92a98cec | CM-POS-001 (a); CM-RET-003 (b) |
| Return receipt | SH-E-0b1f3e09 | CM-POS-001 (a), by its group; CM-RET-003 (b) |
| Shipping update; Out for delivery; Delivered | SH-E-50789e61; SH-E-39c61556; SH-E-16dc5b5b | CM-SHP-017 (a), by SH-S-7208 (R85.4) |
| Return created | SH-E-e0cfec8d | CM-RET-003 (a) |
| Order-level return label created | SH-E-82e13d0e | CM-RET-003 (a), scope US only |
| Return request approved; declined | SH-E-006bba3c; SH-E-55e049c0 | CM-RET-003 (b) |
| Request received | SH-E-83b9e3ef | CM-RET-003 (b); CM-ORD-004 (b) |
| Cancellation request declined | SH-E-8f195456 | CM-ORD-004 (b) |
| Customer account invite; password reset | SH-E-912959df; SH-E-a70b2b18 | CM-CUS-010 (a) |
| Customer account welcome; email address change confirmation | SH-E-99d4a191; SH-E-f3b31d00 | CM-CUS-010 (b) |
| Customer payment method add request | SH-E-74f6fc28 | CM-PAY-022 (a) |
| B2B access email | SH-E-e05f49ff | CM-B2B-002 (a) |
| B2B location update payment method | SH-E-98d36180 | CM-PAY-022 (a); CM-B2B-002 (b) |
| Contact customer | SH-E-93d4fa9d | new:Email customer (a) |
| Customer marketing confirmation | SH-E-b4790913 | CM-CUS-007 (a) |
| New change request (staff) | SH-E-ebf277be | CM-ORD-002 (b) |
| Sales attribution edited (staff) | SH-E-166a1578 | new:Staff sales attribution (b) |
| Order dispute updates (staff) | SH-E-7c4e3b2c | CM-PAY-009 (b) |
| New draft order (staff) | SH-E-072a4f53 | CM-ORD-005 (b) |

**Where this batch differs from earlier lines,** for the coordinator to align:
- **Store credit.** SH-36 (SH-E-62f349d4) and SH-64 (SH-E-a7736370) placed the store credit email `core` on CM-LOY-001. Their entries name the merchant's issuing of store credit, with its option to notify the customer; that issuing form's option is the store credit's own feature. This batch's line names only the event, so it is (b) `shows`. The cell is `core` either way.
- **Double opt-in.** SH-14 put the double opt-in's anchor on CM-CUS-007 alone (SH-E-6e0f3042). This batch keeps CM-CUS-007 for the group's line (SH-E-1f7464fa). It gives the template's line (SH-E-b4790913) CM-NTF-001 too, as R85.3 does for every template.
- **Order processing.** SH-17's line on the label Order processing (SH-E-01cb1d60, CM-ORD-001) is Settings > General's anchor, another thing.

## New things

- **`new:Email customer`** (SH-E-93d4fa9d, the template Contact customer, 'Sent when you contact a customer from the orders or customers page'), `core`.
  - It is the thing SH-12 (`mobile-email-customer:show`) and SH-15 (the modal titled Contact customer at `orders/:orderId/mobile_email_customer`) named. Its places are those routes and this template (`email_templates/contact_buyer/preview`), a template of the admin's section Notifications.
  - Proposed: domain D, area CUS. Parent CM-CUS-001, the customer records it is sent from, with the orders page. English only, as the admin isn't held in Arabic.
  - Searched: `contact customer; email customer; customer email; email the customer`. Nothing holds it.
- **`new:Price drop`** (SH-E-42b06479, Remarketing with Shop), `shows`.
  - It is Shop's reminder 'Sent to shoppers when the selling price decreases below the price they viewed previously', on in this store. It has no place of its own: it is a toggle in a section.
  - Were it a capability, it would be `own-service`, as Shop's.
  - Proposed: domain D, area MKT. Parent: beside CM-MKT-016 (back-in-stock alerts), as an alert on a product's change, or under CM-MKT-022.
  - Searched: `price drop; price alert; price change; browse; remarketing; retargeting; reminder`. CM-MKT-016 holds back in stock only; CM-MKT-017 holds wishlist notifications, which are about saved products, not viewed ones; CM-LOY-007 holds reorder reminders.
  - The checker's leads (CM-PTN-007, CM-CHK-010) are by the words 'selling', 'they' and 'when': no lead.
- **`new:Staff sales attribution`** (SH-E-166a1578, staff template Sales attribution edited), `shows`. It is the thing earlier batches named (SH-32 to SH-45). The line tells of the attributed staff edited. Its leads CM-CUS-007 (by 'subscribers': the order notifications' staff subscribers, not marketing subscribers) and CM-NTF-001/002 were read.

## Entries I couldn't tell, and what would settle each

- **SH-E-1c425a87, Order link → CM-CUS-010 (a).** The order status page is the customer account's by SH-23's line (SH-E-8d9ed79f). Whether the page whose link expires is the customer account's, or the checkout's order status page for guests, would settle it.
- **SH-E-0b1f3e09, Return receipt → CM-POS-001.** It rests on its group, Point of Sale; its own words don't say POS.
- **SH-E-82e13d0e, Order-level return label created.** It goes on CM-RET-003 (return shipments are kept inside it). Whether the label is bought through Shopify Shipping (CM-SHP-002) isn't stated; '(US only)' is its scope.
- **SH-E-34194650, POS abandoned checkout.** CM-MKT-022's cell cites it by its name (SH-I-2029) as a message to the buyer who left. Its line says it is a POS draft order sent 'so a customer can complete a purchase online'. So it takes CM-POS-001 and CM-ORD-005, and CM-MKT-022 as the cell's place (rule 2). The coordinator may read the line as narrowing the name, a statement's description governing its title, and drop the CM-MKT-022 line.
- **SH-E-83b9e3ef, SH-E-8f195456, the cancellation requests → CM-ORD-004 (b).** The words say cancellation, and CM-RET-004's reading leaves Shopify's cancellation requests to the orders' cells.
  - The template's address names `requested_edit_declined`, beside CM-ORD-002's route Decline requested edit.
  - What would settle it: whether that route declines cancellation requests. If it does, CM-ORD-002 takes them as the buyer's requests.
- **SH-E-ebf277be, New change request (staff) → CM-ORD-002 (b),** by its words, 'requests a change on an order'. Its template's address is `merchant_return_requested` (a return request, CM-RET-003). What would settle it: the preview's text (`notification-template-previews`).
- **SH-E-f3b31d00, the email address change confirmation → CM-CUS-010 (b).** It reads the address as the account's sign-in. It could be CM-CUS-001's record, or (a) if the message asks the customer to confirm the change.
- **SH-E-05d29ea1, Browse abandonment → CM-MKT-022 own-service,** a reading: bringing back shoppers who left without ordering, as SH-34 placed Shop's resurfacing of items viewed (SH-E-eedc9ee3). If recovery is only for carts and orders, it is a `new:Browse abandonment` beside `new:Price drop`.
- **SH-E-d74a80d0, Remarketing with Shop's line.** It takes CM-CHN-002 and CM-MKT-022, both `own-service`. CM-MKT-022 is a reading: two of the section's four reminders aren't recovery.
- **SH-E-3a19c814, SH-E-5bdb7d51, SH-E-e63109bc, payments → CM-PAY-020 (b),** the processing of an order's payment, a reading. CM-ORD-015 (pending as an unpaid state) and CM-CHK-001 (checkout) are the other readings.
- **SH-E-a569f376, 'Sent every Monday 9:00 AM GMT+3'.** The schedule is recorded as a quality. That GMT+3 is the store's time zone is a reading.

## The structure against its sources

The source (`source.aria.yaml`, the ARIA tree) holds no toggle. The step's `text.txt` holds a checkbox after many lines:
- the local delivery templates, Out for delivery and Delivered: '[x]';
- Customer marketing confirmation: '[ ]';
- the four Remarketing with Shop reminders: '[x]';
- every staff notification: '[x]'.

So the structure holds the templates and their lines, but not which are turned off and on, nor that some can't be turned off. The readings cite `001.text.txt` and `002.text.txt` for the store's values. The source governs what the entries state; the toggles are the run step's, listed below.

## What the run steps state that no entry holds (for the second stage)

- `raw/runs/20261007T102602Z-journey-notifications/steps/001.text.txt`, lines 63 to 173: the checkboxes listed above. They show which customer notifications the merchant can turn off: local delivery, tracking updates, the double opt-in and Shop's reminders. The others show none.
- `…/steps/002.text.txt`, after each staff notification: '[x]', so each staff notification can be turned off.
- `notification-template-previews`, the same run's steps 8 to 55, not selected. These would settle:
  - whether Order invoice and Draft order invoice carry a link to pay (CM-PAY-032 holds nothing on Shopify; its note, U-018);
  - what New change request is about (returns or edits);
  - what the Customer email address change confirmation asks.
- The second recipient, 'Demo-name demo-last-name's 21121119SC', reads as the owner's phone, an assumption the entry doesn't state. If the staff notifications go to the Shopify app as a recipient (push), that is a lead for CM-NTF-002 and CM-SRF-001, which the mobile app's notification settings would hold.

## Leads that are no leads (the checker's notes)

- **No leads, by a shared word only:**
  - CM-ORD-003, by 'processing' and 'pending payment': it is order statuses the merchant sets, and its note keeps Shopify's order status page apart;
  - CM-LOY-008, by 'customer', 'order', 'when' and 'invite';
  - CM-OPS-004, by 'status';
  - CM-PTN-007 and CM-CHK-010, by 'selling', 'they' and 'when'.
- **Homonyms:**
  - CM-ORD-009 ('order summary', Salla's printed order summary) for Store order summary, which is staff's weekly email (SH-36's line);
  - CM-ACC-004 ('company') for a B2B company;
  - CM-INV-005 ('location') for a B2B location;
  - CM-CUS-007 ('subscribers') for the order notifications' staff subscribers;
  - CM-LOY-007 ('reminders'): its note already keeps Payment reminder apart, and Shop's reminders to buy aren't reorder reminders;
  - CM-PAY-021 ('in-person'): the receipt, not a card payment;
  - CM-CHK-002 ('cart'): the POS cart is the POS app's, as SH-35 placed it;
  - CM-ORD-001 ('All orders'): the recipient's order filter.
- **In passing:** CM-ACC-001 ('store owner'), the recipient of New draft order, named only.

## Problems with the brief or the script

- **The checker's quote pairing.** It paired a quote's closing mark with a later plural possessive ("notifications' subscribers"), and reported the run between them as a quote found nowhere. The reading was reworded.
- **`earlier` printed no twins** for this structure.
- **R14.7 and the coordinator's message.** R14.7 ('a notification template … is CM-NTF-001's alone') and the coordinator's message (decide whether the event takes its own capability) pull apart for the templates' lines. R85.4 is how this batch settles it, keeping R14.7 for groups and routes.

## The coordinator's check

Measured: 16.9 million tokens over 79 requests, about 211,000 an entry. The checker prints no problem.
- **Kept:** R85.1 to R85.7, every `CHANGES` line (Shopify Messaging `own-service` by the ruling after SH-37; Shop's Back in Stock and remarketing reminders `own-service`, the section's own words making them Shop's) and the three new things, whose names earlier batches gave.
- **R85.4, the coordinator's question, settled as the batch has it:** a template keeps its notification line (CM-NTF-001 or CM-NTF-002 `core`), and the event takes a second line on its own capability: `core` where the message does that capability's work (an invoice, a gift card, a recovery, a tracking number), `shows` where it only tells of an event.
- **CM-SHP-017 for the templates that give a tracking number:** `core` stands. The message does the order tracking's work for the buyer, and the cell's own `core` evidence (SH-S-7208) opens the same page; the cell's note, which leaves shipping updates to CM-NTF-001, goes to the amendment with it.
- **Store credit:** SH-36's and SH-64's `core` lines on CM-LOY-001 announce the store credit email as a feature, while this batch's template only tells of credit issued (`shows`). Both stand, by R85.4's two kinds; the cell is `core` either way.
