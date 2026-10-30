# B-bigcommerce: notes

The mapping part of domain B, Catalog and inventory (areas CAT, SEL, INV), for BigCommerce: its 6 concerns that
`scope.tsv` gives the domain (BC-C-001, BC-C-002, BC-C-003, BC-C-004, BC-C-005, BC-C-008), mapped onto the model of
`B-anchor`, `B-woocommerce`, `B-backfill-woocommerce`, `B-zid` and `B-backfill-zid` (33 capabilities: CAT 15, SEL 8,
INV 10). BigCommerce was never matched by Q1, so every landing is my join, by terms, and every join is a reading. Every
row is a reading of the statements its keys cite; a fact is only what a cited statement says. Where the brief left a
choice to me, this file says so ("my judgment").

Result: no new capabilities, so the model stays CAT 15, SEL 8, INV 10. 6 landings, all in capabilities of the model so
far (2 strained), 33 cells (8 held, 25 none-held), 43 evidence rows, 2 qualities, no slot fillers, no rulings
(BigCommerce has no unclear candidates). `python3 -I method/check_class_part.py
studies/class-model/parts/B-bigcommerce`: 0 problems, 16 flags, each answered under "What the checker flagged".

## How I mapped, and why

- **Landing.** Each concern lands in the model's capability whose terms it shares, with BigCommerce's own definition
  where it gives one: Products (CM-CAT-001), Brands (CM-CAT-005), Categories (CM-CAT-003), Inventory (CM-INV-001),
  Locations / Inventory locations (CM-INV-005), Pricing (CM-CAT-013). Each `join_evidence` cites BigCommerce's keys and
  the other platforms' keys that carry the same term.
- **BigCommerce's evidence is mostly its API.** Its concerns hold 30 statements (my 6 concerns) and 25 under `also`.
  Most are API reference pages, scopes, webhook topics and settings resources, which are BigCommerce's own API for its
  own feature, so `core` (C1). Where no statement covers a thing, the cell cites the inventory entry Q1 placed in my
  concern, by its id (C2): the API groups for variants, variant options and modifiers (BC-I-0021 to BC-I-0023), the
  webhooks for options, modifiers, low stock and out of stock (BC-I-0161, BC-I-0162, BC-I-0293, BC-I-0294), and the
  product lines Catalog management and Inventory management (BC-I-0525, BC-I-0527). To find which entries Q1 placed in
  my concerns I read the `inv_ids` of my concerns' rows and the `concern_ids` of the inventory entries holding them,
  with `grep` by concern id; the script's `key` prints an entry without its concern.
- **Grain.** BC-C-001 is coarse, like SH-C-020, WC-C-064 and ZD-C-083: products with their variants, variant options
  and modifiers. It lands in the parent CM-CAT-001, and its variant groups are cited in CM-CAT-002. BC-C-003 holds
  categories and category trees; BigCommerce calls the trees endpoints "the more modern and performant counterparts
  to the categories (deprecated) endpoints" (BC-S-0027), so they are the same object and need no capability of their
  own (my judgment).
- **Modifiers.** BigCommerce names Catalog - Product modifiers beside Product variant options (BC-I-0021, BC-I-0023),
  and no statement says what a modifier is. Citing it in CM-CAT-002 as an option is a reading on the name.
- **What I didn't add (my judgment).** By the convention, a capability needs a place of its own. BigCommerce's things
  that the model has no capability for are:
  - **Bulk pricing rules,** named once in the Catalog API's description (BC-S-0017), with no place of their own in the
    concern map. Cited in CM-CAT-013 as a reading. They may be quantity discounts, which would be domain D's; no
    statement says.
  - **Aggregated stock** (BC-S-0040), a by-request setting of how locations' stock is summed: a setting of CM-INV-005,
    not a place of its own.
  - **The Pricing API** (BC-I-0049) is a place of its own. I landed BC-C-008 in CM-CAT-013 rather than making a
    capability, marked `strained` (below).

## Strained fits

- **BC-C-008, Storefront pricing, in CM-CAT-013 Product pricing.** Joined by the term Pricing. BigCommerce's Pricing
  API gets "product pricing on BigCommerce-hosted storefronts" (BC-S-0053), with no scopes, by CORS (BC-S-0054): it
  reads prices for a storefront. The capability's other cells show setting a product's price (Salla's Automatic
  pricing, Zid's Custom Product Pricing, Update Product Prices) or pricing apps, and no platform defines the
  capability. Whether reading a storefront's prices and setting a product's price are one capability isn't stated. A
  reviewer may split it into a capability of its own, BigCommerce's only (API group BC-I-0049).
- **BC-C-001 in CM-CAT-001,** strained by the dry run's rule S1 only: its statement that files can be added to digital
  products only via the control panel or WebDav (BC-S-0023) is cited in CM-SEL-002, another tree. The concern is the
  catalog as a whole; that one statement is the only place BigCommerce names digital products.

## Joins on role, and homonyms

- **No join on role.** Every landing is by BigCommerce's own terms. The landings in CM-CAT-003 and CM-INV-005 rest on
  the anchor's joins on role (Shopify's Collections; Salla's branches and warehouses); mine join by Categories and by
  Locations / Inventory locations.
- **Homonyms kept apart:**
  - **Subscriptions.** BigCommerce's Storefront Subscriptions API group (BC-I-0009) and webhooks store/subscriber/*
    are newsletter subscribers (BC-S-0212, BC-C-035, domain D), and the account_subscriptions scopes (BC-I-0373,
    BC-I-0374) are domain F's. Neither is CM-SEL-001's selling by subscription. The capability's note could name it.
  - **Tags.** BigCommerce's blog tags (BC-S-0252, domain E) aren't product tags (CM-CAT-006).
  - **Badge.** The Unified Billing badge on apps (BC-S-0183, domain F) isn't a product badge (CM-CAT-014).
  - **Shipments.** Order shipments (BC-S-0103, BC-S-0110, domain C) aren't Shopify's inventory shipments (CM-INV-006).
  - **Pricing.** BigCommerce's Pricing API (prices on a storefront) and its Price Lists (customer-group prices,
    BC-C-007, domain D) are split by Q1 (BC-C-008's split note); only the first is cited in CM-CAT-013.

## The concerns read under `also`

- **BC-C-006** (Pickup, domain C): BC-S-0047, "You can store back-office components, such as location and
  inventories, on partner solutions. These partner solutions then serve as the source of truth for your data", is
  cited as `outside` in CM-INV-001 and CM-INV-005. It names partner solutions, not a party by name, so there is no
  slot filler. Its other statements are pickup's and aren't cited.
- **BC-C-007** (Price lists, domain D): read for CM-CAT-013; not cited, since price lists are D's capability and a
  `core` here would count in two domains.
- **BC-C-011** (Product filtering, domain E): the "in-stock" filter on Pro or Enterprise plans (BC-S-0069) is search's,
  not cited.
- **BC-C-012** (Reviews, domain D) and **BC-C-049** (Metafields, domain E): nothing in domain B's capabilities. The
  brand, category, product and location metafield webhooks are placed in both my concerns and BC-C-049; only
  store/brand/metafield/created (BC-S-0025) is cited, as BC-C-002's own statement.

## Gaps

- **BC-C-002, Brands, decides: page not read** (Q1). CM-CAT-005's cell can't say what turns brands on or limits them.
- **BC-C-008, Storefront pricing, decides: page not read** (Q1). CM-CAT-013's cell can't say who sets what the Pricing
  API returns.
- **Every concern: responsible, stated only in general terms; reason, searched, not found** (except BC-C-004's reason,
  BC-S-0036). No cell claims who is responsible.
- **Undefined names.** No statement says what BigCommerce's catalog settings, storefront product and category
  settings, inventory settings or inventory notifications set (BC-S-0018, BC-S-0019, BC-S-0028, BC-S-0032,
  BC-S-0033), what a modifier or a category tree is beyond its API, or what low stock is (BC-I-0293).
- **Capabilities defined by others only.** For CM-CAT-014 (badges), CM-CAT-015 (barcode printing) and CM-INV-009
  (withdrawal priority), BigCommerce's `none-held` cells add to what the Zid cells' notes say: the capability is named,
  not defined, by the platform that shows it.

## What the checker flagged

`python3 -I method/check_class_part.py studies/class-model/parts/B-bigcommerce`, each flag answered:

- **`none-held`, and statements match the searched terms or the other platforms' terms** (CM-CAT-004, CM-CAT-006,
  CM-CAT-007, CM-CAT-010, CM-CAT-014, CM-CAT-015, CM-INV-002, CM-INV-003, CM-INV-006, CM-INV-008, CM-INV-010,
  CM-SEL-001, CM-SEL-004, CM-SEL-008). I read every match; none shows the capability:
  - CM-CAT-004: Google Shopping (BC-I-0522) is a sales channel, not a taxonomy.
  - CM-CAT-006 and CM-CAT-014: blog tags (BC-S-0252), the Unified Billing badge (BC-S-0183), and words holding the
    letters "tag" (StagingPro, BC-S-0413 to BC-S-0416, BC-I-0540; HTTP 429's "strategically" and "outages", BC-S-0315).
  - CM-CAT-007: the logo and favicon images, social media links and 3D Secure.
  - CM-CAT-010: B2B Edition (BC-C-031, BC-C-065) and price lists for B2B customers (BC-S-0049) are selling to
    businesses, not sourcing products.
  - CM-CAT-015: EAN in Ireland, European, Commerce's definitions (BC-S-0189, BC-S-0227, BC-S-0364, BC-S-0427 to
    BC-S-0433, BC-S-0453, BC-I-0544), print in Script Manager (BC-S-0248).
  - CM-INV-002 and CM-INV-003: the System Logs API "for debugging, auditing, and monitoring store activity"
    (BC-S-0331, BC-C-060, another domain's) doesn't say it logs stock changes; the Account API's users (BC-S-0298),
    StagingPro (BC-S-0416) and the category Accounting & Tax (BC-I-0476) match letters only.
  - CM-INV-006: data transfer, licence and SFTP terms, order shipments (BC-S-0103, BC-S-0110).
  - CM-INV-008: an order status (BC-S-0108), "preserved" (BC-S-0132), and responsibility, contracting and timeout
    statements (BC-S-0167, BC-S-0366, BC-S-0367, BC-S-0394, BC-S-0480, BC-I-0547) that match a word like "held" or
    "hold".
  - CM-INV-010: payment regions, widget regions, Script Manager, shipping zones, tax geolocation: none by the
    customer's city.
  - CM-SEL-001: newsletter subscribers, account subscriptions, fees (the homonym above).
  - CM-SEL-004: "event" in webhooks, BODL events and contract terms: none is a booking.
  - CM-SEL-008: customer segments (BC-S-0207, BC-S-0210, domain D), aggregated stock across "all locations"
    (BC-S-0040) and a licence's "exclusive" (BC-S-0419): none is a membership.
- **CM-SEL-002: `core` rests only on boundary statements.** BC-S-0023 is under boundary, and says "Files can only be
  added to digital products via control panel or WebDav": it names BigCommerce's own control panel as where a merchant
  attaches the files, so it shows BigCommerce itself doing it. Its only other words are that the API can't.
- **BC-S-0047 cited by CM-INV-001 and CM-INV-005, two trees.** The statement names both "location and inventories";
  the model keeps CM-INV-005 out of CM-INV-001's tree by the anchor's grouping, so the statement bears on each. It is
  `outside` in both, so it adds no `core` in two places.
- **BC-C-001 clean but cited in another tree (CM-SEL-002),** on the first run. Answered by marking it `strained`
  (above); the flag is gone.

Final run: 0 problems, 16 flags for the reviewer.

## Problems with the brief or the evidence

- The script's `key` prints an inventory entry without the concern Q1 placed it in, so I read `inventory.tsv` and
  `concerns.tsv` by `grep` on my concern ids, not whole.
- BigCommerce's plan names differ between its pricing page (Core, Growth, Scale, Performance) and the locations list
  (Standard, Plus, Pro, Enterprise), as Q1's note on BC-S-0039 records. The qualities keep each as stated; which plan
  is which isn't stated.
