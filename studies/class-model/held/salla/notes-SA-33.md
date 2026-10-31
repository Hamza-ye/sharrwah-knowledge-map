# Held pass, Salla, batch SA-33: notes

130 entries (effort high), evidence at observed-sa@b0bd0b163: rows 131 to 260 of `plan-gates`, the repository's derived table `derived/plan-gates.tsv` (its lines 132 to 261, addresses `/?settings=/inventory` to `/?settings=/orders/auto_complete`). Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-33`).

**Placed:** 129 entries on capabilities, 1 `new` (73), no `out`, in 135 lines. Entries 22, 53 and 95 take two lines, 62 takes three. Supports: 87 `core`, 48 `shows`; no `own-service`, `extension-point` or `outside`. No filler, no quality: no row states a limit, a price or a fee.

**Sources read:** the brief and what it names; SA-32's notes and placements first; observed-sa's `README.md`, `docs/READING.md` (the derived tables' row), `docs/GAPS.md`, `structures/README.md`; the header and writer of `capture/gates.py` (lines 1 to 30 and 170 to 200: the stores, the sweeps, the columns, the plan-line pattern); the model's cells for every line's capability (`held_entries.py cells`, `land_points.py cell CM-SHP-001 salla`, `merged/evidence.tsv` for the cells' flags); SA-7 and SA-8's placements for `/channel/mobile/*` and `/localization/settings`; and, to clarify each row only, the steps its `steps` column names (cited in each line), plus `structures/salla/dashboard-translations/en/reminders.json` for one banner's name (77).

## What this part of the table is

**Every row here is a page-only row.** None of the 130 has a navigation feature, a features-list plan or an edu row: the columns `nav_features`, `features_list_plans`, `enabled_*` and `edu_allowedPlans` are empty on all of them. So SA-32's rules 3 and 4 (supports from the features list, scope from it or the edu row) never apply directly here, and each line rests on the stores' page lines alone, with the step read to see which page element the line belongs to.

**The `demo` column is read as the Pro store's own page lines** (the corrected known case). Each line's reading quotes it where it isn't empty, or says the Pro store's page states no plan line.

Three kinds of row:
1. **1 to 77: a gate on the address's own page** (or its settings drawer), in the Basic store's words: 'This feature isn’t available on your plan / Upgrade your plan to “Pro” or “Special” to use this feature.', a banner 'Available on Plus, Pro, and Special / Upgrade to Plus', or Salla Point's 'Available on Special, Pro, and Plus plans'.
2. **78 to 94: the reports' Arabic gate**, 'plus,pro,special :لا يمكنك استعراض التقرير؛ يتطلب ذلك أن تكون خطتك واحدة من', on the Basic store only (the others not swept).
3. **95 to 130: one statement, 36 times.** Their only lines are the public demo's, 'Not included in your plan / Upgrade your plan to use this feature.', and every one of them is the home page's **Abandoned carts** widget: the settings drawer each address opens sits over the home page, and the sweep's text holds the home page's widgets ('Abandoned carts' / 'Not included in your plan' / 'Upgrade your plan to use this feature.', e.g. `20261009T022751Z-sweep-public-demo-en/steps/004.text.txt` lines 51 to 53, and the same at every step of these rows). So none of these rows states a gate on its address. I placed each on CM-CHK-007 (the abandoned carts, whose cell holds the plan line السلات المتروكة on Salla Plus), `shows`: the line names no plan. Entry 95 is `/`, the home page itself, so it also takes a line on CM-ANL-003 (the store's overview and home summaries), `core`. I gave the other 35 no line on the settings section their address names: the row says nothing about that section's plan. The same two lines open the public demo's column on entries 1 to 4 and 38 to 62. Each of those readings says so, and I gave them no CM-CHK-007 line: the 36 lines here hold the statement.

   The Basic merchant store's home page shows no Abandoned carts widget at all (`20261008T141131Z-sweep-merchant-en/steps/003.text.txt`). The Pro store's shows it with no gate (`20261008T133523Z-sweep-demo-store-en/steps/001.text.txt`, line 36).

## Rules my lines follow (SA-32's, as they apply to page-only rows)

1. **Where a row goes:** on the capability whose cell cites the address or its settings key, or the one the address's page is, as SA-7, SA-8 and SA-32 placed the same pages. Where the path leaves the thing unclear, the step's title or banner names it (quoted in each line).
2. **`supports`:**
   - **A gate or banner that names the plans that include it:** `core` (a plan line that includes it), the plans its `scope`.
   - **A gate that names no plan:** `shows`, the store's words in `reading`. That is 'This feature isn’t available on your plan' followed by 'Upgrade your store plan to use this feature.' (25, 26, 30 to 32, 38, 39; the table leaves that second line out, see below) or 'Not included in your plan' (95 to 130).
   - **Keeping to SA-32 (its rule 6, on Digital Gift Cards):** where the cell holds the page's own flag as not released, the line is `shows` though the page names plans:
     - store-blog (9, 10), as SA-32's `/marketing/blog` lines;
     - delivery-promises (29), as SA-32's `/shipping/delivery-promises`;
     - wallet-gift-card (61), as SA-32's gift cards app page;
     - control-refund-status (54);
     - shipping-profiles (25, 26), shipping-carrier-pickup (30, 31), shipping-fulfillment-centers (32) and whatsapp-otp (39), which the no-plan rule gives `shows` anyway.
   - **Banners on every store, the Basic ones included, 'Available on your plan'** (11, 12): `core`, scope empty.
3. **`scope`:** the plans the Basic store's page names, in its words and order (`Pro;Special` from '“Pro” or “Special”'; `Special;Pro;Plus` from 'Available on Special, Pro, and Plus plans'; `plus;pro;special` from the Arabic report gate, as SA-32 wrote it). Where a banner and a gate on one page name different plans (18: the Bank Offers banner 'Available on Pro and Special', the gate after it Plus, Pro and Special), the scope is their union, as SA-32's rule 4 for two features. Where no plan is named, the scope is empty.
4. **`terms`:** the address's path (without `/?settings=/`), the entry's only words for the thing; the cells hold such settings keys as terms (`wallet/gift-card`, `coupons/cashback-eligibility`). None for 95 to 130, whose address isn't the thing.
5. **Reports stay on CM-ANL-002** (78 to 94): its note keeps Salla's report types there. I gave no line on each report's subject (brands, coupons, branches, loyalty), as SA-32's rule 10 keeps measures on the analytics capabilities.
6. **Settings that a capability's note keeps:**
   - the gifting settings Selected markets, Product type customization and Messages & cards customization (43 to 45) stay on CM-LOY-006, its note naming them;
   - the loyalty settings Program details, Points settings, Rewards banner and Markets (47 to 50) stay on CM-LOY-004, its note naming them.

   So the markets they name take no CM-MKS-001 line.

## Lines worth the coordinator's eye

- **22, `/orders/bulk`:** the page's banner 'Order Editing' goes on CM-ORD-002, as SA-32 placed the same banner on `/orders`. The page's own gate takes a line on CM-ORD-001, the orders' bulk page. In the step, the gate follows a search panel's 'Customize statuses / No results found' (`20261008T141131Z-sweep-merchant-en/steps/245.text.txt`, lines 57 to 61), the same pattern as on 10 and 77, where the gate follows 'No results found'. I read it as the page's gate, not the statuses' (CM-ORD-003). A Basic store's click on the page's bulk actions would settle it.
- **28 and 70, Shipping restrictions (`/shipping/rule`):** on CM-SHP-001, whose cell holds قيود الشحن والتوصيل (plan line on Salla Pro) and the flag shipping-rules (pro, special). CM-SHP-023 (holding nothing; the lead by 'shipping' and 'plan') keeps to a statement naming a rules engine, so I didn't place them there.
- **53, Statuses included in reports:** both CM-ANL-002 (its settings route) and CM-ORD-003 (its term) cite it, so it takes both lines.
- **54, Manage refund statuses:** `shows` by the cell's unreleased flag control-refund-status, though the Pro store's page states no gate (`20261009T033607Z-sweep-settings-demo-en/steps/045.text.txt`). If the coordinator reads the settings route and its plan gate as `core` (the cell's own core is the route, SA-S-1743), this line turns. The same holds for 61 (Gift cards, `wallet/gift-card`, the cell's core route).
- **62, Wallet & Cashback Notifications:** three lines. CM-LOY-001's cell holds the setting, CM-LOY-003's note names it, and its words name the notifications the store sends (CM-NTF-001).
- **15, Import links:** on CM-CNT-006 alone. CM-MIG-001's import is of products, customers and orders, not links.
- **34, `/users/roles/new`:** CM-STF-002 alone. SA-32's second line on CM-STF-001 for `/users/roles` came from its feature user-advance-management, which this row doesn't name.
- **77, `/customers/new`:** on CM-CUS-001, as SA-32 placed `/customers`. The page also shows a box 'Create customer groups', and the gate follows the search panel's 'No results found', so I don't read the gate as the groups' (CM-CUS-002).
- **5, `/localization/settings`:** on CM-MKS-001, as SA-8 placed the route (`SA-E-9d40d620`), scope `Special;Pro`.

## New things

1. **Custom Product Fields** (الحقول المخصصة), entry 73: the same new thing SA-32 named for `/products/options/custom-fields/*` (its entry 117), named the same way.
   - Here it is the listing page `/products/options/custom-fields`, with the banner 'Custom Product Fields', 'Available on Pro and Special / Upgrade to Pro', on 'Categories & options' > 'Custom fields'.
   - Its description: 'Custom fields let you add options your customers can choose from, such as color, size, dimensions, and more.' (`20261009T000821Z-sweep-merchant-compare-en/steps/029.text.txt`, line 25).
   - Its place of its own is SA-32's: the dashboard address under Categories & options. Proposed as SA-32 proposed it: domain B, area CAT, parent CM-CAT-001.
   - The description's 'options your customers can choose from' sets it near product options and variants. The coordinator may read that against CM-CAT-001's options.
   - Terms searched by SA-32 (custom field; حقول مخصصة; product field; attribute; specification; مواصفات; metadata).
   - The checker's leads, CM-PLN-001 and CM-B2B-003, come from the plan names and 'pricing'; neither is the thing.

## Entries I couldn't tell, and what would settle each

- **95 to 130** (above): placed on the widget the page shows, not the address. Settled if the coordinator prefers to leave the 35 settings-drawer rows `out` as repeats of 95. I didn't make them `out`, since each row quotes a platform plan statement.
- **11 and 12** (`/channel/pages/new`, `/marketing/coupons/bulk`): 'Available on your plan' on all three stores, so I left the scope empty. SA-32 scoped `/channel/pages` by the features list (plus, pro, special), which this row doesn't name. A Basic store creating a page would settle whether it is open there.
- **25, 26, 30 to 32, 38, 39:** gated on every swept store, the Pro one included, with no plan named. Which plan, if any, opens them isn't stated. The Special plan's dashboard, which no store of ours holds, would settle it.
- **91, `/reports/products/order_per_product`:** its page is titled 'Back in stock alerts' (`20261009T000821Z-sweep-merchant-compare-en/steps/073.text.txt`, line 16), against its path's order per product. It is on CM-ANL-002 either way.
- **68, Salla Point's user guide:** `core` on CM-POS-001 as a page of Salla Point's own dashboard, with the same gate as its other pages. A guide could instead be read as a topic (`shows`).

## Items against sources

- **The table leaves out a plan line its sources hold.** On 25, 26, 30 to 32, 38 and 39, every swept page follows 'This feature isn’t available on your plan' with 'Upgrade your store plan to use this feature.' (e.g. `20261008T141131Z-sweep-merchant-en/steps/260.text.txt`, line 22). `capture/gates.py`'s pattern matches 'Upgrade your plan', not 'your store plan', so the `merchant`, `demo` and `public_demo` columns hold the first line only. The readings quote the second from the step.
- **The settings drawer's rows carry the home page's lines** (95 to 130, and the public demo's column on 1 to 4 and 38 to 62): `gates.py` quotes every plan line of the step's text, and a drawer's step holds the page under it.
- **32's page has no title of its own:** its breadcrumb is the untranslated key 'breadcrumb./shipping/fulfillment-centers'. So are 63 to 65, 69, 71 and 76 (`breadcrumb./marketing/affiliates/...`, `breadcrumb./orders/custom-fields/new`).

## For the second stage: what the steps state that no entry holds

- **Cashback's claim** 'With cashback offers, the repeat purchase rate among merchants has increased by more than 55%.' (`20261008T141131Z-sweep-merchant-en/steps/238.text.txt`, line 24), for CM-LOY-003.
- **Salla Point's payments:** 'Enable Tap-to-Pay on your phone or send a payment link to your customer.' and 'Mada, Apple Pay, Google Pay, STC Pay, Tamara, and Tabby are all activated and ready.' (`20261009T000821Z-sweep-merchant-compare-en/steps/012.text.txt`, lines 19 and 20), for CM-POS-001, CM-PAY-021 and CM-PAY-032 (payment links). Tamara and Tabby are named there as payment methods, with no role stated.
- **The blog's categories page** states 'الميزة غير متاحة في الوقت الحالي' (the feature isn't available at present) on the English sweep (`20261008T141131Z-sweep-merchant-en/steps/213.text.txt`, line 16), for CM-CNT-004.
- **The public demo's page names its plan,** 'Basic' (`20261009T022751Z-sweep-public-demo-en/steps/004.text.txt`, line 9). I took the store's plan from `capture/gates.py`.
- **The banners' descriptions** on the bulk and new pages, each naming its feature's purpose: Info Pages 'Pages that build trust in your store'; Coupons 'Irresistible offers'; Promotions, Cart Offers, Bank Offers and Staff Accounts (the steps of 11, 12, 16 to 19 and 37).

## The checker's lines, read again

- **No `CHANGES` line:** no line alone changes a cell.
- **`NOTE line 78`:** the new thing's leads, CM-PLN-001 and CM-B2B-003, are no leads (plan names; 'pricing'), as SA-32 found for the same thing.
- **`NOTE` lines 100 to 119** (entries 95 to 116, with gaps): the first lead CM-EVO-001 (holding nothing) comes by the words 'feature', 'included' and 'merchant', which every row of the table holds. No lead, as SA-32 found.
- **`NEW`:** Custom Product Fields, 1 line.

## Problems with the brief or the script

- **Page-only rows:** the brief's known case lists which columns quote the platform, but this part of the table has nothing in the feature columns, and the stores' lines are the whole entry. Their lines often belong to a page element other than the address's own page (the drawer over the home page). The table's `address` is the step's requested path (`gates.py`), so a row's address and its lines can belong to different pages. The brief could say so for the SA-34 and `permission-gates` batches.
- **Quotes beside possessives:** as SA-32 noted, I kept each quote apart from a possessive's apostrophe.

The checker's last line, for SA-33: `130 of 130 entries placed; 0 problems` (after this file was written).

## The coordinator's check (30 October 2026, after the batch)

- **Rows 96 to 130 are `out`.** Each row's only plan lines are the public demo's home page widget, Abandoned carts: 'Not included in your plan' / 'Upgrade your plan to use this feature.' (`20261009T022751Z-sweep-public-demo-en/steps/006.text.txt`, lines 51 to 53, confirmed). They are seen behind the settings drawer each address opens. That is entry 95's statement, placed on 95, and no row's address states a gate of its own. So each is `out`, its reading naming 95, as the notes offered. 35 identical `shows` lines would have given CM-CHK-007's cell 35 rows for one statement.
- **The brief now says so,** in its known case on derived tables:
  - a row's address is the step's requested path;
  - a settings drawer's lines can be the home page's, so each line's element is read in its step;
  - a row whose only lines are another page's is `out`.

  SA-34 and the `permission-gates` batches read it.
- **The rules for page-only rows stand:** a gate naming the plans that include it is `core` with those plans as scope, and a gate naming no plan is `shows`.
- **Two cells are read again at Salla's amendment:** refund statuses (54) and gift cards (61). Each cell's `core` rests on the same settings route whose flag the features list holds as not released.
- **The table's store columns miss a line.** On entries 25, 26, 30 to 32, 38 and 39 the pages add 'Upgrade your store plan to use this feature.', which `capture/gates.py`'s pattern doesn't match. The readings quote it from the steps, so nothing is lost here.
- **Cost:** 9.0 million tokens over 55 requests, about 69,000 an entry. No cell changes. Its one new thing, Custom Product Fields, is SA-32's.
