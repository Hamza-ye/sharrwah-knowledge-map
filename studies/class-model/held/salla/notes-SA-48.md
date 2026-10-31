# Held pass, Salla, batch SA-48: notes

105 entries (effort high), evidence at observed-sa@b0bd0b16. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-48`).
- 1 to 37: `salla-academy` (`home@ar`), the rest of the academy's home page, from its line 55 (the learning paths) to line 199 (the last course card). **`salla-academy` ends here.**
- 38 to 47: `salla-complaints` (`home`), all ten lines of complaint.salla.sa. **It ends here.**
- 48 to 105: `settings-center`, its first 58 entries: the sections Orders (48 to 74) and Products (75 to 105), the entries labelled `demo@en,merchant@ar` (the item rows) or all five labels (the section, its fetcher and its lists). **No batch had placed `settings-center`. SA-49 to SA-63 hold the rest of it (about 1,240 entries) and haven't run.** The rules my lines follow are below (S1 to S12), written for them; the coordinator aligns the batches.

**Placed:** 93 entries on capabilities, none `new`, 12 `out`, in 127 lines.
- Academy (37 entries, 51 lines): 32 lines on CM-ONB-003 `core`; second lines `core` on CM-ACC-001 (3) and CM-SEL-002 (1); `shows` on CM-CAT-010 (2), CM-SEL-002, CM-SFR-001, CM-PTN-009, CM-MKT-022, CM-SFR-006, CM-MKT-014, CM-CNT-007, CM-SHP-021 and CM-SUP-005 (one each); 5 entries `out` in 4 lines.
- Complaints (10 entries, 10 lines): CM-TRU-020 `core` 5 and `shows` 1, CM-TRU-009 `core` 1, CM-TRU-010 `shows` 1; 2 `out`.
- Settings centre (58 entries, 66 lines): 56 lines `core` and 5 `shows` (CM-RET-002, CM-ORD-002 and CM-CAT-013, behind features that aren't released; CM-MIG-001 and CM-LOY-005, a named thing with no placement); 5 entries `out` in 5 lines. Scope only on the nine lines gated by a feature: `order-count-time`, `control-refund-status`, `customer-editing`, `product-show-sku`, `product-advance-management`, `metal-pricing`, `product-default-weight`, `quick-donation` (two lines).
- No `own-service`, `extension-point` or `outside`, no filler, no quality. **The checker prints no `CHANGES` line: no cell changes.**

**Sources read:** the brief and what it names; the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's rows for the three structures, `index/ledger-summary.tsv` and `index/ledger/settings-field.tsv`; the selection rows; the rulings to their last section; B-extent's "Cells and evidence" and conventions. SA-47's notes and placements (its rules A1 to A8 and the coordinator's check); SA-23's notes, placements and check (the settings panel's links); SA-20's rules (the nav's features as scope); SA-16's and SA-17's lines and checks for the features that gate my settings; SA-21's, SA-29's and SA-33's lines for the same addresses (below).
- **The sources:** the academy's `text.txt` and its archive record `raw/runs/20261012T061544Z-thin-surfaces/fetch.warc.gz@52566`, whose HTML gives each link's address and each course's category; complaint.salla.sa's `text.txt` and `fetch.warc.gz@46216`; the settings centre's bodies `structures/salla/settings-center/<label>/orders.json` and `products.json` (the same bytes for all five labels: sha256 `42d7e486…` and `f81c4600…` in each `meta.json`), read whole, with the labels and descriptions in `dashboard-translations/{en,ar}/settings.json`.
- **To clarify only, each cited where a line rests on it:** the Pro store's settings pages (`20261008T133523Z-sweep-demo-store-en/steps/003.text.txt` and `013.text.txt`), the Basic store's (`20261008T141131Z-sweep-merchant-en/steps/005.text.txt` and `015.text.txt`) and the real store's Products page (`20261012T010906Z-sweep-real-merchant-full-en/steps/340.text.txt`), which show which items each store's panel displayed; `dashboard-features/{demo,merchant}@en/items.jsonl` for each gate's `released`, `enabled` and plans; `dashboard-translations/en/orders.json` (the prep list is printed) and `feature-content.json` (product-show-sku); the sub-pages' bodies `orders~prep-list-layout.json`, `orders~orders.weight_threshold.json`, `products~products.product_quantity.json`, `orders~shipping-label-deduction.json`, to read the items that link to them; the concern map's settings keys (SA-S-1703 to SA-S-1769, `class_slice.py search`) and the cells that cite them (`merged/evidence.tsv`).

## The academy: SA-47's rules A1 to A8, kept

Every course is CM-ONB-003 `core` (A1, A2), its address, category and trainer in `reading`. What I added to apply them to the home page's last part:
- **A9. A learning path** (2, 7, 10: مسار المحترفين, مسار المبتدئين, مسار النمو, at /ar/training-path/7, 5 and 6) is a page of the academy: CM-ONB-003 `core`, under the heading المسارات التعليمية that SA-47 placed. Its card's course count ('0 الدورات', '15 الدورات'), its rating ('★', '0.3', 0.3 out of 5 by the HTML) and its button 'عرض التفاصيل' are `out` (A8): values on a card.
- **A10. A home-page section heading over categories** (14 تجهيز متجرك لاستقبال العملاء, over categories 5 and 12; 30 ما بعد عملية البيع, over 6 and 10) is a container on CM-ONB-003 (A1, A3), with no topic line. The headings اختيار المنتجات and التسويق (home lines 71, 139) are the same text as SA-47's category entries, so they had no entry here. **Each 'مشاهدة الكل (n)'** (11, 15, 22, 31) links to the courses page filtered by its categories (`courses?categories=11`, `5%2C12`, `2`, `6%2C10`): CM-ONB-003 `core`, as SA-47's 'مشاهدة الكل (36)'.
- **A2 applied to the 26 courses:**
  - **a title naming Salla's own feature, `core`:** 12 (CM-SEL-002 and CM-ACC-001: a digital products store on Salla), 16 (CM-ACC-001: a store in Salla), 17 (CM-ACC-001: its address's slug names في-سلة; the new dashboard it names takes no line, since no capability is the admin itself, the ruling after SA-21);
  - **a title naming a capability's topic, `shows`:** 9 (dropshipping, CM-CAT-010), 19 (store design, CM-SFR-001), 23 (affiliate marketing for marketers, CM-PTN-009), 25 (abandoned carts, CM-MKT-022, the recovery), 26 (landing pages, CM-SFR-006), 28 (affiliate marketing, CM-MKT-014), 29 (SEO, CM-CNT-007), 32 (product packaging, CM-SHP-021), 34 (customer service, CM-SUP-005), 35 (print on demand, CM-CAT-010), 37 (digital cards, CM-SEL-002);
  - **a third party's tool or a general topic, nothing more:** 8, 13, 18, 20, 21, 24 (Google Analytics), 27, 33, 36.
  - The trainers named in titles (فارس الشريف, محمد باعباد, حميد المطيري, ريم علوي, أسامة الحربي, محمد جواد, محمد البدر, نبيل الجابري, بندر المسند, راكان الجهني, العنود السالم, شكري مخاشن, عبدالله الهلالي, سميره) are in `reading`, never `filler`: no held statement says whether they are of Salla's company or third parties (a gap, as SA-47 said).
- Course 9, 'دورة إنشاء متجر دروب شبينيق', stands only in the learning path's list (`ul path-card-courses`), with no link of its own, so its address and category aren't held.

## The complaints page (38 to 47)

- **C1.** The page is Salla's complaints system, CM-TRU-020: its title (38), heading (40), the paragraph addressed to the shopper, in which Salla reviews the problem and guides them 'بالتنسيق مع المتجر' (44), and its two actions, open a complaint (45, routed to /payment) and follow one up (46, /followup): `core`, as the cell reads Salla's own page ("not a separate product, so core, not own-service").
- **C2.** The two paragraphs that set the boundary go where their words point:
  - 42, the stores' full legal independence and full responsibility for orders, product quality, shipping and customer service, makes the merchant responsible as the seller: CM-TRU-010 `shows`, never `outside`;
  - 43, Salla's compliance team (فريق الامتثال) following the stores' compliance and intervening on violating practices: the platform's own enforcement, CM-TRU-009 `core`.
- **C3.** 41, Salla as 'الشريك التقني لآلاف المتاجر' and its aim of a safe, reliable shopping experience, is the ground the page gives for the system: CM-TRU-020 `shows`. The slogan (39) and the language switch (47) are `out`, as SA-2's and SA-5's.

## The settings centre: what an entry is, and the rules (for SA-49 to SA-63)

**What the structure is.** The settings panel (`?settings=/<path>` over the dashboard) is drawn by Salla's server from a schema, one answer per page: `api.salla.dev/admin/v2/settings-center/settings/<section>`. Each label folder holds the answers as `<section>.json` (a sub-page's `/` written `~`), and `items.jsonl` lists the schema's nodes in document order. An entry is one node, its text resolved from the translations. The kinds:
- **`s:section`:** a page of its own, with its `path`, its title (the `section` the entry names) and its staff `permissions`. The panel's top-level sections (23 on merchant@ar, with Markets 24: orders, products, shipping, profile, general, …) and their sub-pages, each opened by an `s:item`'s `href`.
- **`s:item`:** a link to a sub-page, with a label and description; or, inside a sub-page, one of its settings (`enabled`, `statuses`, …).
- **`s:field`:** a setting saved on the page itself, with its `action` (`PUT settings/fields/<key>`), its inputs and, sometimes, its gate.
- **`s:list`:** a card grouping settings, with no title of its own. **`s:list-header`:** a list's heading, with or without a `title`.
- **`s:form`:** a sub-page's form, with its `id` and `action`, the key its settings are saved under.
- **`s:plan-gate`:** a part of a page shown only on the plans its `plans` names.
- **`s:fetcher`, `s:base-url`, `s:base-origin`:** the request for the page's stored values, and the base of an action's address.
- **`s:header`, `s:header-back`, `s:header-title`, `s:link`, `s:redirect`:** a page's header (a search box), its back link and title, a link to another settings page (`to`), and a redirect to one.

**Before placing, read the node in its body, not only the entry.** The rendering leaves out each `s:item`'s `href` and `features`, every `s:field`'s inputs and options, an `s:plan-gate`'s `plans`, and a label given as a `span` (105's 'Wishlist Notifications', with its badge). The body is the bytes: where it and the entry differ, the body governs, and the reading says so. A `parent` that is a number is the `position` of a node in the same label's `items.jsonl`.

**One setting is up to three entries.** The five labels answer the same bodies (compare the sha256 in each `meta.json`), but each label's positions differ, so an item's `parent` number differs: Orders' Minimum order value is SA-E-c49bc0b3 (`demo@en,merchant@ar`, mine), SA-E-49527563 (`merchant@en,public-demo@en`, entry 794 of the structure) and SA-E-0faddf3c (`real-merchant@en`, entry 1075). Every one of my item entries (all but the two sections, their fetchers and their untitled lists, which carry all five labels) has two twins: **structure entries 794 to 844, `merchant@en,public-demo@en`, in SA-57, and 1075 to 1098 (Orders) and 1113 to 1139 (Products), `real-merchant@en`, in SA-60 and SA-61.** They come in the same order as mine (SA-E-c49bc0b3, SA-E-49527563, SA-E-0faddf3c; …; SA-E-3cf7740b, SA-E-752fcc99, SA-E-56ed006d), found by comparing the texts with the parent's number left out. **Give each the lines SA-48 gave the same node, its reading naming SA-48's entry.** The same holds for every later section: compare a node's text without its parent number, and where a body's sha256 differs between labels, read both.

**S1. A section is a container** (M-13) on the capability its title names, as the earlier batches placed the same address:
- the top-level sections, as SA-23 placed the panel's links (and SA-20, SA-29 the same addresses): profile CM-ACC-001; general CM-ACC-006; plan CM-PLN-001; stores CM-ACC-003; billing CM-PLN-004 and CM-PLN-006; payments CM-PAY-001; domains CM-SFR-008; checkout CM-CHK-001; taxes-and-duties CM-TAX-001 and CM-TAX-008; channels CM-CHN-001; inventory CM-INV-001; products CM-CAT-001; orders CM-ORD-001; shipping CM-SHP-001; customers CM-CUS-001; coupons, titled Marketing, CM-MKT-005 by SA-23's link (SA-29 placed its permission gate on CM-MKT-002; the section holds coupons, affiliates and offers under its list headers, so its title's capability governs); wallet CM-LOY-001; loyalty-program CM-LOY-004; gift-system CM-LOY-006; blog CM-CNT-004; feedback CM-SUP-001; notifications CM-NTF-001; apps CM-APP-001; markets CM-MKS-001 (SA-S-1769);
- **a sub-page takes the capability of the item that links to it** (the item's `href` is the page's `path`): SA-48's items for orders/… and products/…, and, for the other sections, the concern map's settings keys, which are the sub-pages' own titles: blog/* CM-CNT-004; checkout/guest-checkout CM-CHK-001; coupons/multiple-coupons CM-MKT-002; coupons/marketer-assets, welcome-email, status-settings, commission-period CM-MKT-014; coupons/discount-priorities CM-MKT-001; coupons/cashback-eligibility CM-LOY-003; customers/login_methods CM-CUS-010; customers/recaptcha CM-CUS-012; customers/whatsapp_otp CM-CUS-013; customers/address CM-CUS-008; feedback/rating_message CM-SUP-002; feedback/thanks_message, image_attachment, update_rating CM-SUP-001; general/store-information CM-ACC-006; general/languages CM-MKS-008; general/currencies CM-MKS-006; general/salla-mcp CM-AIA-004; general/maintenance-mode CM-ACC-007; gift-system/* CM-LOY-006; markets/browse_product_method CM-MKS-001; loyalty-program/* CM-LOY-004; payments/payment-restrictions CM-PAY-019; profile/* CM-ACC-001; shipping/shipping.cod CM-PAY-016 and CM-PAY-029; wallet/max-credit-usage, wallet/notifications CM-LOY-001; wallet/gift-card CM-LOY-002 (SA-S-1703 to SA-S-1768, read in `merged/evidence.tsv`). The plan and permission gates of the same addresses are SA-29 to SA-34's lines: `grep -h 'settings=/<path>' studies/class-model/held/salla/placements-SA-*.tsv`.
- The section's own words and its sub-page's settings decide where a page is new to the model; the address's prefix doesn't (M-6 refined).

**S2. `out`:** `s:fetcher`, `s:base-url` and `s:base-origin` (the software's own working); an untitled `s:list` or `s:list-header` (a layout node over several capabilities' settings: the rulings after SA-22 and SA-28). One entry stands for every node of the same text, so 50 is all eight of Orders' lists, over several capabilities. **Two exceptions:**
- a list whose entry is its own (its text differs from its siblings', as a gate's flag makes it) and whose settings are one capability's is a container on that capability, with the gate as its scope (103: the list holding only Quick donation, behind `quick-donation`);
- a titled `s:list-header` is a container on the capability its title names (M-13), or `out` where the title names only a grouping of several capabilities.

**S3. Staff `permissions`** on a section or item are a gate on the user: in `reading`, never `scope`, and no CM-STF-002 line (the brief, rule 5).

**S4. A gate on the store is the scope:** a node's `feature.flagKey`, its `features`, the list it sits in, or an `s:plan-gate`'s `plans`, in Salla's identifiers (the feature's key, as SA-20 put the nav's features; the plans as the body names them). Then:
- read the feature in `dashboard-features/<label>/items.jsonl`: released on a held store, `core`, with its plans and each store's `enabled` in `reading`; not released on any held store, `shows` (H-held rule 4, flags; SA-20's rule 2);
- the node's own `defaultValue` (enabled, released) is the schema's fallback, not a store's value: `reading`;
- the stores' pages show what the gate does (the steps each `meta.json` names): Minimum order value, SKU, digital protection and default weight show on the Pro stores only; Manage refund statuses, Order editing, Automatic pricing and Quick donation show on none;
- a gate's feature gives no line of its own (the ruling after SA-22). Where an earlier batch placed it elsewhere, the reading names that line: product-advance-management gates digital protection, and SA-17 placed it as bulk product editing.

**S5. A setting goes on the capability of what it sets.** What it sets it by (the order statuses, payment methods, product types, branches or channels the merchant selects in it) is `reading`: auto-restock's statuses, the branch priority's branches, the refund statuses. Where it sets another capability's thing itself, it takes that line too: auto-complete sets the order's status (CM-ORD-003); the label cost deduction draws on the store wallet (CM-PLN-006); a note or a tracking link added to the notifications is a note on the order (CM-ORD-013) or the shipment's tracking (CM-SHP-017).

**S6. A storefront display option** (show or hide something on the product page, a product list or the cart) is CM-SFR-015's `core`, storefront display, as its plan lines (sold-out products last, the purchase count) are. Three refinements:
- where what it shows is a capability's own thing, it goes on that capability alone: special offers (CM-MKT-003), recommendations (CM-MKT-023), product images (CM-CAT-007), brands (CM-CAT-005), free shipping (CM-SHP-001), filters (CM-SFR-013);
- a place it names outside the storefront takes that place's capability too: the invoice (CM-ORD-008);
- a field of the product record shown in the admin (SKU in product and order details, the HS code in the product's advanced details) isn't a storefront display: it goes on the field's capability, CM-CAT-001 for the SKU, as SA-17 placed its feature product-show-sku, and CM-SHP-020 for the customs code, the cell whose terms hold HS code.

**S7. Inside a sub-page** (the sub-pages' entries, from the structure's entry 271 on, SA-51 onward):
- its `s:form` carries the key its settings are saved under: `core` on the page's capability, the action in `reading`, unless the key names another capability's thing (`marketing_settings.*` on the Products page saves CM-MKT-003's offers);
- each `s:item` setting takes the page's capability, and a second line where its words name another capability's thing it sets (S5), such as a daily limit on cash-on-delivery orders (CM-PAY-029);
- an option or input value (a channel, a unit, a sort order) is the setting's input, in `reading`. An option that names a third party's service through Salla's App Store ('First, link your store to a WhatsApp provider from the App Store.') shows third parties doing it through the platform: `extension-point` on that thing's capability, the provider unnamed, so no filler;
- a store's value of a setting (its minimum amount, the channel chosen, a default weight of 0.1 or 501 kg) is that store's data, `reading` only.

**S8. The other kinds:**
- `s:link` (`to` another settings page) goes on the capability of the page it opens, `core`, as a menu link;
- `s:redirect` names another place, not its own thing: `out`, its target in `reading` (H-held rule 2);
- `s:header-back` is a UI string: `out`;
- `s:header-title` is the page's title, on the page's capability; a title given under a condition (`from=inventory`) is a statement of its own with the condition in `reading`, since a search parameter is no store's condition (M-14);
- `s:header` holding only a search box names nothing: `out`.

**S9. Terms and quotes.** Terms come from the entry's text (the English and Arabic labels, or the id where the label isn't rendered, as in 105). A quote from a locale cites `structures/salla/dashboard-translations/<lang>/settings.json` by its key. Many labels hold an ASCII apostrophe or double quotes (“Set orders as 'Completed' upon placement”, 'they're', 'تعيين حالة "تم التنفيذ"'): quote around them, since a row can't hold `"` and a quote ends at `'`.

**S10. Search before placing.** Each item's own place first: `class_slice.py search --platform salla --terms "<sub-page key>; <label>"` finds the concern map's settings key (SA-S-17xx), and `merged/evidence.tsv` the cell that cites it. That key's cell is the entry's capability (S1). Then the leads, then `caps --terms` for the things the description names.

**S11. A sub-page an item gates differently from its plan gate.** Where an item is hidden behind an unreleased feature (`shows`, S4) and SA-33 placed the same sub-page's plan gate `core` (orders/edit-policy, products/products.auto_pricing), each line stands on its own entry. The coordinator may align them (below).

**S12. No `new` from the settings centre without the search:** every Orders and Products setting here had a capability. A section or sub-page that no cell's reading holds is `new:<its title>` with `core`, its parent named in the notes (rule 3).

## `new` things

None. Searched with `caps --terms`, besides the leads: dropshipping / دروب شب / بدون مخزون; digital product / منتجات رقمية / digital card / البطاقات الرقمية; print on demand / الطباعة حسب الطلب; SEO / السيو / محركات البحث; customer service / خدمة العملاء / ما بعد البيع; packaging / تغليف; لوحة التحكم / dashboard; product description / وصف المنتج; store design / تصميم المتجر; social media / السوشل; compliance team / فريق الامتثال / acceptable use / violation / مخالف / suspend; minimum order / الحد الأدنى للطلب / order limit; prep list / picking / تجهيز الطلب; imported orders / الطلبات المستوردة / external orders / order import; free shipping / الشحن المجاني / progress bar; SKU / رمز التخزين; starting from / يبدأ من; weight / الوزن; deferred payment / مهلة الدفع; tracking link / رابط التتبع; sort / sorting / ترتيب المنتجات.

## Entries I couldn't tell, and what would settle each

- **72, 'Disable deferred payment for bank transfers' / 'تعطيل مهلة الدفع عند التحويل البنكي', on CM-PAY-030 only.** CM-PAY-008 (payment terms: an order paid after it is placed, on terms and a schedule the merchant sets) holds nothing on Salla. Salla's bank-transfer order gives the buyer a period to pay, and the order confirmation page has a message for it, 'Shown when the customer chooses deferred payment.' (`settings.json`, orders/processing/order-confirmation-page#payment_waiting.description). I didn't read it as payment terms: the merchant sets no terms or schedule, only turns the period off, and CM-PAY-008's note already sets three such Salla homonyms aside. A line there would make the cell held (`CHANGES`). The confirmation page's own entries (its Pending payment, SA-E-b68d4d34, in SA-55) and what the period is, in a help article, would settle it.
- **102, Product sorting options, on CM-SFR-015** (how the storefront shows products, as its plan line puts sold-out products last). CM-SFR-013 (search and filtering) is the alternative, since the buyer sorts the list beside its filters. No cell changes either way.
- **57, Order weight limit warning, on CM-SHP-002.** The warning is given when a label is issued ('عند إصدار البوليصة'); whether that is only Salla's own labels, or also the merchant's own carrier contracts (CM-SHP-015), isn't stated.
- **61, Prep list layout, on CM-ORD-009.** The list is printed per order (`dashboard-translations/en/orders.json`, print_prepare_list_desc); CM-SHP-009, order fulfilment, is the alternative if the coordinator reads a prep list as the fulfilment step rather than a printed document.
- **74, Show imported orders:** CM-ORD-001 `core` and CM-MIG-001 `shows`. Where the orders come from ('من مصادر خارجية') and who imports them isn't stated: a channel's orders would be CM-CHN-001's.
- **95, Default product weight for shipping, on CM-CAT-001,** with SA-17's line for its feature. The weight is sent to the carrier ('عند إرسال الطلب لشركة الشحن'); a shipping capability (CM-SHP-015, CM-SHP-020) would take a second line if the coordinator reads it as shipping data. No cell changes.
- **66 and 90, behind unreleased features, `shows`,** where SA-33 placed the same sub-pages' plan gates `core` (SA-E-ac07181a, SA-E-7e66f749). The Pro store's sub-page opened with no plan line, while the panel hides the item that links to it. Both lines rest on their own entries (S11); the coordinator may make SA-33's two lines `shows`, as SA-33 itself did for control-refund (SA-E-60d74b55). No cell changes: CM-ORD-002 and CM-CAT-013 are `core` from other statements.
- **Academy 34 (customer service, CM-SUP-005) and 32 (packaging, CM-SHP-021):** read as A2's capability topics. If the coordinator reads them as general business topics, the two `shows` lines go; neither changes a cell. Likewise 18 (writing product descriptions): I read it as content writing, a general topic, not CM-CAT-001's description field or CM-AIA-003's AI writing.
- **Academy 23, affiliate marketing for marketers, on CM-PTN-009** (the marketers who earn commissions) rather than CM-MKT-014 (the store's programme), which 28 takes. No cell changes.
- **Complaints 45, 'تقديم شكوى جديدة', routed to /payment.** Why a new complaint starts at a page named payment isn't held (complaint.salla.sa/payment is not held). CM-PAY-009 (chargebacks) matched only the word.

## A structure whose items and sources disagree

- **`settings-center`'s items leave out what places an entry:** each `s:item`'s `href` and `features` (control-refund-status, customer-editing and metal-pricing gate three of my items, none rendered), every `s:field`'s inputs and options, and a label given as a `span` (105, whose entry holds only its id). The bodies govern; my readings cite them.
- **One node, several entries; several nodes, one entry.** The same setting is split by its parent's number into up to three entries, and every untitled list or fetcher of a section is one entry.
- **The translations hold strings no held body uses:** Orders' list headings 'Order processing', 'Order and inventory management', 'Customer order options', 'Inventory sync', 'Inventory tracking', 'Stock alerts', 'Order fulfillment' (`settings.json`, orders#receiving-and-treating-orders.label and the keys beside it); no body of any label names those keys. Products' 'Send item details for product bundles' (products#send-sub-products-items) is unused too, but the Shipping section draws the same setting under its own key, shipping#send-sub-products-items (`shipping.json`), SA-49's entry.
- **`salla-academy`:** as SA-47 said, `text.txt` holds no link's address; each course's address and category are in the archived HTML.

## For the second stage: what the sources state that no entry holds

- **CM-ORD-009:** the orders page's print actions 'Print prep list', 'Print prep list (EN)' and 'Print consolidated prep list' (`dashboard-translations/en/orders.json`, print_prepare_list and the keys beside it); the cell holds only the plan line طباعة ملخص الطلب.
- **CM-PAY-008 (question above):** the order confirmation page's 'Pending payment' message, 'Shown when the customer chooses deferred payment.' (`settings.json`, orders/processing/order-confirmation-page#payment_waiting.description).
- **CM-SHP-002 / CM-PLN-006:** the label cost deduction's options 'From store balance only' and 'From store balance and online payments', and 'Salla Shipping Labels gives you carrier rates with no contracts or minimums to help lower costs.' (`settings.json`, orders/shipping-label-deduction#…), for the sub-page's own entries.
- **CM-TRU-020:** the complaint form and the follow-up (complaint.salla.sa/payment, /followup) and the English page (`?lang=en`) aren't held; the form would show what a buyer states and whether a payment is asked for.
- **CM-ONB-003:** the learning paths' pages (/ar/training-path/5, 6, 7) and the courses' pages aren't held (register: 'a course's own page is not held'); who the trainers are isn't held.

## Leads set aside as no leads

- **Academy:** CM-PAY-005 and CM-TRU-010 (8, by الكترونية, تجارة), CM-PTN-005 (10, by النمو), CM-APP-002 (12, 16, by سلة, متجر), CM-CUS-001 (14, 20, 34, by العملاء), CM-MKT-005 (23, 28, by التسويق), CM-PTN-008 (23, 28, by name), CM-CHK-002 and CM-CHK-007 (25: the recovery is CM-MKT-022's, by CM-CHK-007's note), CM-PLN-007 and CM-TAX-001 (32, by قيمة مضافة, added value), CM-ORD-008 and CM-ORD-009 (35, by طباعة, طلب: print on demand).
- **Complaints:** CM-TRU-010 and CM-PAY-002 (38, 39, by name), CM-PTN-006 (41 to 43, by سلة, متاجر), CM-SHP-002 (42, by شحن), CM-CUS-001 and CM-PAY-029 (43), CM-PAY-009 (45, 46, by شكوى).
- **Settings:** CM-ACC-006 (75, by store_setting_browse, the section's permission); CM-RET-002 and CM-PAY-020 (48, by order_management); CM-LOY-008, CM-ORD-015, CM-PAY-022, CM-API-011, CM-SHP-003, CM-INV-007, CM-APP-012, CM-SFR-016, CM-B2B-007, CM-API-007, CM-TAX-002 and CM-INV-010, each holding nothing on Salla, matched by common words only (customer, order, after, payment methods, label, purchase, display, button, storefront, data, tax); CM-CNT-003 (52, 81, 88, by page); CM-ACC-001 (55, 59, 74, 99, 100, by your store); CM-API-005 (57, by limit); CM-SFR-007 (71, by bar); CM-INV-006 (72, by transfer); CM-PTN-004 (94, by invoice); CM-API-001 and CM-PLN-001 (96, by advanced); CM-PAY-019 (97, by the permission); CM-ACC-008 and CM-MKS-009 (99, by available in, data); CM-CHK-008 (104, by quick); CM-MKS-006 (80, 86, by price); CM-AIA-003 (96, by field, product).

## The checker's lines, read again

- **No `CHANGES`:** every line falls on a cell that already holds its support.
- **`NOTE` line 63 (/orders) and line 96 (/products): containers.** Each section is placed on the capability its title names, as SA-23, SA-20 and SA-29 placed the same addresses; its settings are placed by their own entries (S1).
- **`NOTE` line 106: first lead CM-CNT-001 (Files) holds nothing.** CM-CNT-001 is a store-wide file library (Shopify's Files); entry 85 protects the PDF files of digital products, CM-SEL-002's. Its reading names CM-CNT-001 and why it isn't the entry's.
- No `NEW`.

## Problems with the brief or the script

- **The settings centre's rendering** leaves out `href`, `features`, inputs, `plans` and `span` labels (above), so every settings batch must open the bodies; the entry could carry them.
- **The checker's quotes:** a quote ending in an Arabic combining mark ('مجاناً') isn't closed, so a later ’ followed by a space in my prose made a false quote (the NOTE I had on line 36, fixed by rewording). Readings should avoid a plural possessive after such a quote.
- **Quoting the settings' labels:** many hold an ASCII apostrophe or double quotes (S9), so a reading can quote only around them.

The checker's last line for SA-48, after this file was written: `105 of 105 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes and no new things.** The academy keeps A1 to A10, the complaints page sits on CM-TRU-020, and the settings keep the earlier batches' addresses.
- **`settings-center` is rebuilt so its entries carry what governs them** (`selection.tsv`: `nodes:section`). Each item is joined to its node in its section's answer, and gains what the extracted list left out:
  - a sub-page's `href` and `features`;
  - a field's controls and their options, in both languages;
  - a plan gate's `plans`;
  - the other words a setting shows (tooltips, badges, alerts, a label given as a span), under `shows`.
- **A parent with no name of its own is named by its kind under its nearest named ancestor** ('s:list under /orders'). The same setting in each store's answer is now one entry: these were the agent's twins.
  - The structure holds 715 entries, not 1,298.
  - This batch's 58 settings entries are re-keyed to the new ones, which now carry all five stores. The checker passes on them.
  - The other 657 are cut again into SA-49 to SA-56, and SA-57 holds the shipping carriers and the theme lists.
- **The rules S1 to S12 stand.**
  - Their entry numbers and batch names refer to the first build.
  - Read a section's body only where an entry leaves a column open.
  - S11 settles 66 and 90: the list's item is behind a feature no held store has released, and the Pro store's sub-page opened with no plan line (SA-33). Each line stands on its own entry, and the cell takes `core`.
- **The other points stand as placed:**
  - the bank transfer payment period on CM-PAY-030 alone;
  - product sorting on CM-SFR-015;
  - the prep list on CM-ORD-009;
  - the academy's `shows` lines.
- **The checker's quote pattern** now reads an Arabic vowel mark as part of its word, so a quote no longer opens after 'مجاناً'.
- **Cost:** 47.8 million tokens over 151 requests, about 455,000 an entry, the most of any batch. Its settings entries left out what governs their placement, so each was read from its section's body, and the batch also wrote the rules for the structure's other batches. With the rebuilt entries and the twins merged, those batches should cost much less. SA-49's cost will show how much.
