# D-backfill-woocommerce: notes

D-woocommerce added one capability to domain D, CM-MKT-022 (abandoned cart and order recovery). This back-fill writes
its two missing cells, Shopify's and Salla's. It adds no capabilities and lands no concerns.

## How the cells were found

`candidates --domain D --areas MKT` found nothing for either platform: the only term in the model's cells is
WooCommerce's "Recovering orders". So I read the two concerns D-woocommerce named, SH-C-050 and SA-C-048, under every
placement with their gaps, and searched further:
- Shopify: abandoned; recover; cart reminder; checkout reminder.
- Salla, in English: abandoned; forget cart; recover; reminder. In Arabic, singular and plural, with and without ال:
  متروك; المتروك; سلة متروكة; السلة المتروكة; سلات متروكة; السلات المتروكة; تذكير; التذكير; تذكيرية; التذكيرية;
  رسالة تذكيرية; الرسالة التذكيرية; رسائل تذكيرية; الرسائل التذكيرية; استعادة; الاستعادة; استرجاع السلة;
  استرجاع السلات.

Both cells are `statements`.

## The concerns read under `also`, and what is left to C

SH-C-050 and SA-C-048 are domain C in scope.tsv, both with D under `also`, so they may support a placement here
(convention 8). I cite only what is about recovering the sale: reminders, messages and apps addressed to the buyer who
left. Domain C may build its own capability for abandoned checkouts as records, and these statements are left to it:
- **Shopify (SH-C-050):** the admin path `checkouts` (SH-S-5001), the navigation Abandoned checkouts (SH-S-1538), the
  section's eligibility, MANAGE_ABANDONED_CHECKOUTS with the entitlement abandonedCartRecovery (SH-S-5002), and the
  webhook topic checkouts/update (SH-S-1164). Also the inventory entries for the checkouts webhooks, the staff
  permissions, and the admin extension targets on abandoned checkouts (SH-I-1503, SH-I-1523, SH-I-1524, SH-I-1561,
  SH-I-1562). SH-S-5002 names the recovery entitlement, but it states the gate of the records section, so I leave it to
  C and cite the entitlement's own values (SH-S-5276, SH-S-5277).
- **Salla (SA-C-048):** the plan line السلات المتروكة (SA-S-2003), which has no description; the dashboard app at
  `/marketing/(carts)` (SA-S-3591, the same route as SA-S-1814); the Abandoned Carts API folder (SA-S-1035); the
  scope `carts` (SA-S-1548); the webhook topics abandoned.cart, abandoned.cart.update, abandoned.cart.purchased and
  abandoned.cart.status.changed (SA-S-1625, SA-S-1628 to SA-S-1630); the permissions forget_cart_browse and
  forget_cart_management (SA-S-2352, SA-S-2353, SA-S-2569, SA-S-2570); and the feature flags abandoned-cart-rule,
  abandoned-cart-complete-order, abandoned-cart-cursor-pagination and abandoned-cart-merchant-notifications
  (SA-S-3248 to SA-S-3250, SA-S-3458). The flags' names don't say whether a rule or a completed order is about
  recovering the sale: a reading could put abandoned-cart-rule and abandoned-cart-complete-order here, and I left them
  to C rather than decide it from a name.
- **SA-S-1814** (the link Abandoned carts at `/marketing/carts`) is the one statement I cite that C will likely cite
  for the records too. I cite it as `core` because Salla puts the page under its marketing routes; that the reminders
  of SA-S-2099 are sent from it is a reading. If C cites it as `core`, the merge will flag it, and the coordinator
  decides which domain keeps it.

## Other statements cited from domain D's own concerns

- **SH-I-2021 and SH-I-2029,** the notification templates Abandoned checkout and POS abandoned checkout, are inventory
  entries Q1 placed in SH-C-150 (Notifications, domain D). No statement covers them, so they are cited by id. That
  they are the messages to the buyer who left is a reading from their names.
- **SA-S-1668,** the Communication Webhooks type customer.cart.abandoned, is a statement of SA-C-200 (domain D). It
  is cited as `extension-point` the way D-anchor cited customer.repurchase.reminder (SA-S-1672) in CM-LOY-007. The
  statement held is cut after its entity type (`cart`), so its description and meta aren't in the concern map: a gap.
- **SH-I-1827 and SA-S-1191,** the App Store categories Abandoned cart apps and Abandoned Cart, are `extension-point`
  on the reading, from their names, that their apps recover the sale. Neither is defined. SH-I-1827 is cited by its
  inventory id because no statement covers it.
- **Not cited:** SA-S-1304, the App Functions event Abandoned Cart ("Triggered when a cart is abandoned"), is SA-C-196,
  domain F without D under `also`, and it is an event on the cart, not a recovery.

## Slot filler not written

SA-S-5017, from Salla's abandoned-carts FAQ, says discount messages can't be sent at any time "تماشياً مع الشروط
والأحكام الخاصة بتقديم الخدمة التي أقرتها هيئة الاتصالات وتقنية المعلومات السعودية". It names a regulator as setting
the terms of the messages: a slot filler for CM-MKT-022 on Salla, with no scope stated on the statement. A back-fill
writes only cells, evidence and notes, so it isn't in a `slot-fillers.tsv`; the coordinator may add it.

## Gaps

- SH-C-050/reason: searched, not found. SH-C-050/responsible: stated only in general terms.
- SA-C-048/responsible: page not read.
- SA-S-1668 is cut after its entity type (above).
- No statement held defines Shopify's "abandoned cart recovery features" beyond the plan line, or names what the
  Abandoned checkout template sends.

## U-001

D-woocommerce's two rulings on U-001 are `joined:CM-MKT-022`, for WC-C-105 against SH-C-050 and against SA-C-048.
They hold now: CM-MKT-022's Shopify cell cites SH-C-050/decides/SH-S-7224 (with SH-S-7041, SH-S-5276 and SH-S-5277),
and its Salla cell cites SA-C-048/decides/SA-S-2099 (with SA-S-1814, SA-S-1191 and SA-S-5017), while WooCommerce's
cell cites WC-C-105/where/WC-S-0719. The Shopify–Salla pair of U-001 (SH-C-050 against SA-C-048) is domain C's to
rule on, since both concerns land there; both are now cited together in CM-MKT-022 if C wants that ruling to follow
these cells.

## Checker

The checker printed no problem and no flag.

## The coordinator's addition (30 October)

- **The slot filler** this part named in its notes is written to `slot-fillers.tsv`: the Saudi communications regulator, هيئة الاتصالات وتقنية المعلومات السعودية, which sets the terms on which Salla's discount messages to abandoned carts may be sent (SA-S-5017), by convention 9, as D-anchor wrote الهيئة العامة للنقل for CM-CUS-008.
