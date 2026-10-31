# Held pass, Salla, batch SA-22: notes

80 entries (effort high), evidence at observed-sa@b0bd0b163: `dashboard-nav-segments`, items.jsonl positions 76 to 155, `reports` to `marketing/integration-tools/x`. SA-23 holds the last segment, `shipping/setting` (position 156), with its other structures.

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-22`).

**Placed:** 76 entries on capabilities, 2 `new`, 2 `out`, in 95 lines.
- Supports: 74 `core`, 19 `shows`. No `own-service`, `extension-point` or `outside`.
- No scope and no quality on any line (SA-21's rule 6). A filler on 14 lines: the ad platform each integration page is for (Snapchat, Google, Meta, TikTok, X), the venue (M-3).
- 15 entries take two lines (below); every other entry one.

## What I read

- The brief and what it names: observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the structure's register row and `meta.json` (`show --meta`); its selection row; the rulings, the last section included.
- **SA-21's placements and notes first,** with the coordinator's check after it. I kept to its rules for the segments ("for SA-22 and SA-23") throughout.
- Each of my 80 answers, `dashboard-nav-segments/prod/<segment>.json`, whole: each item's Arabic label, `feature`, `permission`, `tags`, `isNewFeature`, `isBeta`, which items.jsonl leaves out; and each answer's sha256 against the earlier segments, for the answers shared byte for byte.
- Salla's earlier lines for the same addresses, joined to their entries' text: the routes (SA-7 to SA-12), the nav (SA-20, SA-21) and the gates (SA-32 to SA-34).
- **To clarify only**, each cited in its line's reading: the features list `structures/salla/dashboard-features/demo@en/items.jsonl` (each page item's feature, its release and plans); `derived/map-steps.tsv` and the sweep and journey steps it names for the pages no item names (reports/sales/products, shipping/tickets, the Salla Ads v2 pages, the integration tools); the steps SA-32 and SA-33 cited for a page's own words.
- The model: the cells of every capability a line names; `caps --terms` for tickets and complaints, questions, custom fields, events manager, referral, express delivery, certificates, catalog and UTM (below).

## Rules my lines follow (SA-21's, restated where my batch met a case of its own)

1. **A segment is a container on the capability of the page its own address opens** (rule 3, the coordinator's check after SA-21), with its page item's Arabic label, feature, release, plans, badges and staff permissions in `reading`, "reading, not scope".
2. **Its other items take no line here:** each page address is a segment of its own; each settings drawer is a settings-centre section, named by id (`?settings=/shipping` SA-E-f27adfb7, `/products` SA-E-b93ad281, `/customers` SA-E-85917545, `/feedback` SA-E-edd31286, `/markets` SA-E-82d7f20c); the Messages drawer (manage/experts/orders, 36; marketing/influencers/campaigns-archive, 47) is read as a part of the container's capability, as SA-21 did.
3. **Where an earlier batch placed the address, I kept to its capability.** Where it gave two lines, I kept both only where the page itself is two things, by its own labels or words; a second line that rests only on a gate feature is named in the reading instead. This is how SA-21 kept logs/export on CM-MIG-004 alone and payments on CM-PAY-001 alone. The cases:
   - two lines kept: shipping/logs (7: CM-SHP-009 by 'Shipment log', CM-SHP-002 by 'أرشيف البوليصات'), apps/settings (19), channel/mobile/reports (21), feedback/blogs (26), localization (29: its two page items), products/importer (30), the softpos page (55), utm-builder (71), and the integration tools and ads tools (32, 39, 72, 77 to 80);
   - a gate-only second line left to the reading: reports/performance (2, SA-32's CM-ANL-002), users/roles (17, CM-STF-001), users/targets (18, CM-POS-001), customers/register-form (23, CM-CUS-001), shipping/bullet-delivery (62, CM-SHP-016), and the Pixels & feeds pages' CM-MKT-010 (salla-ads), which their items in this answer don't name.
4. **`shows`** where the page item's feature is held as not released (channel/mobile/reports, customers/register-form, customers/join-requests, feedback/blogs, the localization's Multi Market, products/importer, marketing/blog and its two sub-pages, channel/vendors, shipping/delivery-promises, marketing/referrals, products/metal-pricing), or the page isn't offered (marketing/events-manager: the Pro store's page answered '404', as SA-32); and on the second line of the softpos page (CM-PAY-021) and utm-builder (CM-MKT-008), as SA-32 and SA-8 placed them.
5. **A page no item of its answer names** goes on the capability of what shows the page: a sweep's or journey's step through `derived/map-steps.tsv` (reports/sales/products, shipping/tickets, the Salla Ads v2 pages 31 and 38 to 40), or the line that placed the address (the six Salla Point sub-pages, 52 to 57).
6. **`terms`:** the segment, and the page item's English label where the entry lists it.

## New things

- **`new:Bullet Delivery`**, entry 62 (SA-E-a022d289, shipping/bullet-delivery), `core`. The name SA-32 gave the same address.
  - **What it is:** the page Bullet Delivery (التوصيل السريع) in the shipping section, titled 'Express Delivery' (20261008T133523Z-sweep-demo-store-en/steps/273.text.txt), on the feature shipping-routes (released, plans pro, special). What it delivers, and by whom, isn't stated: the page answered 'Express delivery data is currently unavailable.'
  - **Its place of its own:** a route of the dashboard, /shipping/bullet-delivery, with an item of its own in the shipping sub-navigation.
  - **Proposed:** domain C, area SHP, parent CM-SHP-001 (by the shipping section's grouping); the alternative is CM-SHP-016 (shipping routes), whose feature gates it.
  - **Names:** Bullet Delivery; التوصيل السريع; Express Delivery.
  - **Terms searched:** express; express delivery; fast delivery; same day; سريع; التوصيل; local delivery; delivery option; delivery speed; on-demand. Nearest: CM-SHP-008 (local delivery, the store's own) and CM-SHP-019 (delivery option generators), neither of which names it.
  - **A lead:** the settings centre's field `show-express-delivery-checkout-tag`, 'Show the express delivery tag to the customer …' (SA-E-7638f449, SA-E-fa8ec7c5, SA-E-1fb4e28d), in SA-48 to SA-63's settings-center entries.
  - The checker's leads (CM-SHP-020, CM-SHP-009, CM-SHP-016, CM-RET-003, CM-SHP-003) are the other items' capabilities by path, or a word only.
- **`new:Product certificates`**, entry 66 (SA-E-fa404196, products/certificates), `core`. The name SA-32 gave the same address.
  - **What it is:** the page Product certificates (شهادات المنتج), titled 'Certificate templates' (20261009T000821Z-sweep-merchant-compare-en/steps/001.text.txt), on the feature product-certificates (released, plans plus, pro, special). What a certificate is isn't stated.
  - **Its place of its own:** a route, /products/certificates, with an item of its own in the products sub-navigation.
  - **Proposed:** domain B, area CAT, parent CM-CAT-001 (by the products section's grouping).
  - **Names:** Product certificates; شهادات المنتج; Certificate templates.
  - **Terms searched:** certificate; شهادات; شهادة; product certificate; certificate template; قوالب الشهادات; authenticity. Homonyms: CM-SFR-010 (SSL certificate), CM-LOY-002 (gift cards, a gift certificate), CM-TRU-010 (the seller's licences).
  - The checker's leads (CM-CAT-001, CM-INV-001, CM-INV-005, CM-TRU-003, CM-MIG-006) are the other items' capabilities by path, or a word only.

## Entries I couldn't tell, and what would settle each

- **15 (tools) and 58 (more), `out`.** Each answers with groups that span several sections of the admin: tools with five groups at /tools (Help Desk, Shipping, Payment, Tools, Logs), more with six at /more (Customers and the same five, the mobile menu's). Each group's children are nested.
  - Neither answer names a title, and both pages answered '404' (20261009T000815Z-sweep-nav-unreached-demo-en/steps/018 and 016).
  - The groups are the mega menu's own. The main navigation's entries hold them (such as مركز الدعم, SA-E-24793706; SA-17 to SA-19), and each child is placed by its own segment.
  - So I read them as main and mega were read after SA-21: a container over several sections names no capability.
  - **The alternative is M-13,** since the ruling keeps M-13 for "a container over one part of the admin":
    - `new:<title>` with `core`, for a container with no title and no page;
    - or a line on each group's capability: Customers CM-CUS-001, Help Desk CM-SUP-*, Shipping CM-SHP-001, Payment CM-PAY-001. Tools and Logs name only groupings.

    The coordinator's ruling on whether a container over several sections is "one part" would settle it.
- **65 (marketing/referrals): CM-PTN-008 or CM-MKT-013.** SA-12 read the page's strings: a programme where merchants invite merchants, with 'a monthly commission of 0.4% of their sales'. On that reading it placed the route on CM-PTN-008, with a note that the cell's commission is on plan sales. SA-32 placed the address on CM-MKT-013, saying whom it refers isn't stated. I kept to SA-12, whose reading rests on the page's own words. Either way it is `shows`, since affiliate-referral isn't released.
- **60 and 61 (shipping/operations, shipping/reports): CM-ANL-001,** as SA-32. The pages measure Salla's shipments. A shipping line (CM-SHP-002, the platform's labels) is the alternative, if the coordinator reads 'Track your Salla shipments' as the labels' service.
- **22 (customers/custom-fields): CM-CUS-001,** as SA-32, on the cell's feature customer-metadata. CM-CNT-002 (custom data: metafields) is the alternative, if the coordinator reads a customer's custom fields as custom data.
- **50 (marketing/seo/llms-txt): CM-CNT-007 alone.** The ruling after SA-2 puts a line on CM-AIA-005 only where the words name AI platforms or buyers' discovery through AI. 'LLMs.txt' is the file's name. SA-7 and SA-32 gave the address no AIA line either.
- **45 (marketing/events-manager): CM-MKT-005, `shows`,** as SA-32. What the manager manages isn't stated, and the Pro store's page answered '404'. If its events are the pixels' events (CM-MKT-009, which holds Ecommerce Events), the page would be theirs. A held page would settle it.
- **32, 77 to 80 (the integration tools): filler.** Each page is Salla's own integration with an ad platform's pixel and catalog: 'The X Pixel is automatically installed on your Salla store' (20261008T182638Z-journey-pixels-demo/steps/005.text.txt). So `core`, with the ad platform as the venue the entry names (M-3). Catalog (76) names no platform in its item, so it has no filler.

## A structure whose items and sources disagree

- As SA-21 found, items.jsonl lists only each answer's top-level urls and English labels. The answers hold each item's Arabic label, `feature`, `permission`, `tags` and badges, and, for tools and more, the groups' nested children. The source governs: I read every answer.
- **Several answers name none of their segment's own page:**
  - reports/sales/products, which answers reports' sub-navigation;
  - shipping/tickets, which answers shipping's;
  - marketing/ads/v2/dashboard, campaigns, tools/snapchat and audience, which answer Salla Ads' sub-navigation at the /marketing/ads/* addresses;
  - the six Salla Point sub-pages, which answer only Salla Point.
- **The Salla Ads v2 pages render the older addresses:** v2/tools/snapchat rendered /marketing/ads/tools/snapchat, and v2/audience rendered /marketing/ads/audience-manager (`derived/map-steps.tsv`, `rendered` column).
- **marketing/carts/reminders' items are written without a leading slash,** as in marketing/carts.
- **marketing/events-manager answers differently from marketing/campaign/retargeting** (another sha256), though both list the same two items, Campaigns and Events manager. I didn't trace the difference.

## What a source states that no entry holds (for the second stage)

- **tools.json and more.json nest the groups' children,** with labels that differ from the top-level items:
  - under Shipping: Shipping & delivery as 'شركات الشحن' (carriers, CM-SHP-015's thing), and Shipping settings;
  - under Payment: Store Verification (/payments/kyc), and Wallet & Billing (المحفظة والفواتير) in more;
  - under Tools: Developer tools (/manage/webhooks) and Referral program;
  - under Customers, in more: Staff (url '#'), Staff Members and Roles & Permissions.

  The main navigation (SA-17 to SA-19) may hold these as entries.
- **The settings centre's `show-express-delivery-checkout-tag`** is a lead for Bullet Delivery (above).
- **Pages a sweep holds and no segment entry quotes:**
  - Shipping performance's 'Shipping statistics' and 'COD delivery success rate' (20261008T133523Z-sweep-demo-store-en/steps/262.text.txt);
  - the integration pages' features, such as Meta's 'Conversion API (CAPI)' (20261008T182638Z-journey-pixels-demo/steps/004.text.txt) and Google's 'Google Merchant Center, Ads Tag, and Analytics' (steps/003.text.txt).

  The last two are leads for CM-MKT-009 and CM-CHN-004.

## The checker's lines, read again

- **`CHANGES` CM-MKT-008@salla, line 82 (71, utm-builder): kept.**
  - SA-8 placed the same route there, `shows`, on the page's own words: 'UTM parameters are tracking codes used by tools like Google Analytics to identify website traffic from specific sources.' (20261009T000815Z-sweep-nav-unreached-demo-en/steps/019.text.txt).
  - That orders are credited to marketing isn't stated, so it is `shows`.
  - The cell holds nothing yet because SA-8's line isn't amended into the model. With SA-8's line, mine changes nothing.
- **`NOTE` lines 61 to 64, 66 and 67, `core` on a product named with the platform's brand (Salla Point):** `core` by Salla's own dashboard pages under /channel/sallapoint, as SA-21, SA-32 and SA-33 placed them. No maker is needed for `core`.
- **`NOTE` line 17, the first lead CM-OPS-004 holds nothing:** it is a lead by the word 'tools' only. CM-OPS-004 is WooCommerce's system status tools, not this grouping.
- **`NOTE` lines 72 and 76, a new thing whose entry has leads:** read above. Each lead is another item's capability, or a word only.
- **`NEW`:** Bullet Delivery, 1 line; Product certificates, 1 line.

## Problems with the brief or the script

- **The checker's "first lead holds nothing" note also fires on an `out` line** (17, tools). There, the lead is a word every Salla tools page shares.
- **SA-21's rule 2 ("two lines where they gave two") and its practice differ.** Its practice dropped a gate-only second line (logs/export, payments). I followed the practice (rule 3 above). The coordinator may want one statement of it for SA-23.
