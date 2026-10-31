# Notes: held pass, Salla, batch SA-29 (`partners-portal-navigation`, rest; `performance-reports`; `permission-gates`, first part)

130 entries, effort high, evidence at observed-sa@b0bd0b163. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-29`).

**Placed:** 129 entries on capabilities, 1 `out`, no `new`, in 194 lines. Supports over the lines: 155 `core`, 25 `extension-point`, 13 `shows`. No scope, filler or quality on any line: no entry states a plan, a store condition, a third party, a limit or a price.

| Structure | Entries | Lines | Placement |
| --- | --- | --- | --- |
| `partners-portal-navigation @partner@ar` (1 to 40) | 40 | 48 | 39 capability, 1 out (33, 'روابط مساعدة') |
| `performance-reports @demo@en` (41 to 53) | 13 | 13 | 13 capability, all CM-ANL-003 `core` |
| `permission-gates` (54 to 130) | 77 | 133 | 77 capability |

## What I read

- The brief, `H-held.md`; the evidence map; the coordinator's rulings, `held/review-H-rulings.md`, to its last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run".
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the `structures/REGISTER.tsv` rows of my three structures; `show --meta` and the three `selection.tsv` rows (`where`, `where`, and `decides` with the rule `rows:derived/permission-gates.tsv:.`).
- SA-28's notes and placements (its rules H1 to H8 and the coordinator's check); SA-33's coordinator's check (a row whose lines are another page's).
- The lines of SA-34 to SA-37 for each portal route the menu opens, and of SA-7 to SA-14, SA-20 to SA-22 and SA-32 to SA-33 for each dashboard address the permission rows name.
- **Sources:**
  - `partners-portal-navigation`: both labels' `items.jsonl` (the English label's 45 items stand at the same positions as the Arabic ones and have no entries of their own; I read them for each item's English title, which the readings cite).
  - The portal sweep's pages for the routes no batch has placed: `raw/runs/20261008T124250Z-sweep-partner-portal-en/steps/013`, `014`, `015`, `016` and `020.text.txt`.
  - `performance-reports`: `source.json` (`raw/runs/20261008T211326Z-journey-reports-demo/responses/0036.json`, step 1) and the same step's page, `steps/001.text.txt`, lines 1 to 31.
  - `permission-gates`: `derived/permission-gates.tsv`, lines 2 to 78; `capture/gates.py`, its header and the part that writes the permission rows (which says each dashboard row is the union of the navigation entries' `permission` at one address, from `dashboard-nav/prod/source.json` and `dashboard-nav-segments/prod/*.json`, and each store's 'Access restricted' lines from its first rendered step); the navigation answers for each address's item, its title and feature; `staff-permission-groups/demo@en/items.jsonl`, for the labels of the permissions no cell holds; the two demo-store steps whose lines the table quotes (`20261008T133523Z-sweep-demo-store-en/steps/114.text.txt` and `199.text.txt`).

## The structures' split with other batches

- **`partners-portal-navigation`:** SA-28 holds its first 4 entries (the logo, Dashboard, My Apps, the group Themes), and I hold the other 40. I kept SA-28's H1, H2, H6 and H7, and the coordinator's ruling that 'Others' is `out`. The empty link at position 1 has no entry.
- **`performance-reports`:** no batch had placed it. I placed it whole.
- **`permission-gates`:** no batch had placed it. I hold its first 77 rows, the dashboard rows `/orders` to `/marketing/carts/reminders` (table lines 2 to 78). **SA-30 and SA-31 hold the rest** (the remaining dashboard rows, from line 79, and the portal rows, `surface: portal (…)`), **and haven't run.** The rules my lines follow are below, for them; the coordinator aligns the batches.

## Rules my lines follow

### The portal's side menu (for the coordinator's alignment with SA-28)

- **N1 (H1).** A link to a portal route takes the capability and support that SA-34 to SA-37 gave the same route, citing that line. Its gate (a permission, a feature, `requiresThemeAccess`) is the route's, so it goes in `reading`, never in `scope`.
- **N2.** Where no batch has placed the route yet, I placed the link by the cell that already cites the same Partners portal link (SA-S-1905 to SA-S-1947), and by its page in the sweep. These are the layout-mf and affiliate routes SA-38 holds: /affiliates/marketplace, /affiliates/my-opportunities, /affiliates/orders, /affiliates/active-merchants and /affiliates. SA-38 should keep to these lines, or the coordinator aligns them.
- **N3 (H2, M-13).** A group with href '#' is a container. It goes on the capability its title names, as the cells' readings show, with the support its children's routes took:
  - My Services is on CM-PTN-005;
  - Affiliates and Marketing Tools are on CM-PTN-009, whose note names both menus;
  - Stores is on CM-DVT-003, whose note names the item;
  - Help Center is on CM-PTN-001.

  Three titles name a thing the model keeps as two capabilities. Each takes a line on both, as M-6 counts a thing in each capability it names:
  - Influencer, on CM-PTN-009 and CM-MKT-015, as SA-34 placed both of its routes;
  - My Subscriptions, on CM-APP-003 (apps) and CM-SFR-003 (themes);
  - Payments (الماليات), on CM-PTN-003 and CM-PTN-004, whose cells' readings both cite their links as under Payments.
- **N4.** A child that is a kind of its group's thing takes the group's line too (M-6 refined). Demo Stores and Ready Stores are partner stores, as CM-DVT-003's cell already cites both. Store management isn't: it is access to merchants' stores (CM-DVT-003's note). Bundles isn't a kind of theme.
- **N5 (D1).** A badge 'جديد' ('NEW') is a release badge with no limit stated, so the item is offered. The badge goes in `reading` and doesn't lower the support: the line takes its siblings' support (`extension-point` on CM-PTN-009). SA-28's note for SA-29 said such an item is `core`. I read D1 as saying the item isn't `shows`, not as changing the support its thing takes. The coordinator may align it.
- **N6.** 'روابط مساعدة' (English 'Others') is `out`, by the ruling after SA-28.

### Store performance's reports

- **R1.** Each report is a tab of Store performance (/reports/performance), the cell's own link: CM-ANL-003 `core`. Each is Salla's own (`is_default_report: true`).
- **R2.** A report is a kind of report by its subject (orders, wallet, abandoned carts). Its subject's capability takes no line, as CM-ANL-002's note keeps Salla's report types in analytics.
- **R3.** No scope: the answer states no plan. `visibility` is the store's own setting (the page's 'Manage reports'), so it goes in `reading`. The Conversion rate tab's 'Beta' badge is D1: `core`.

### The permission gates (for SA-30 and SA-31)

- **P1. The address's line.** A row goes on the capability of its address's page, with the support the earlier batches gave that address: SA-20 to SA-22 for the navigation item and segment, SA-7 to SA-14 for the route, SA-32 and SA-33 for the plan gate. Its terms are the path and the permissions that name the page's thing, or the section's general one (order_management, products_management, customer_management, reviews_management).
- **P2. A permission that names another capability's thing takes its own `core` line** there, by the ruling on a list of permissions (after ZD-7). Its capability is the one the model's cells already place it on, from the staff permission groups. Examples are order_refund_payment on CM-RET-002, import_export_management on CM-MIG-001 and customer_block on CM-CUS-005.
  - The section's general permission on a sub-page takes no line of its own: it is in the address's line.
  - One entry has one line per capability, since the checker refuses two lines of one entry on one capability.
- **P3.** Only a permission over the staff's permissions goes on CM-STF-002. None of my rows holds one (users_browse and users_management are on /users rows, which are SA-30's). support_access_requests is CM-STF-005's.
- **P4. An address whose navigation feature isn't released keeps `shows`,** as SA-21's rule 5 and SA-32 placed it: products-importer, store-blog, app-performance-reports, custom-customer-fields, auth-forced. So does Events manager, which answered 404 (SA-22). Its P2 lines stay `core`: each permission is in the staff permission groups and already `core` in its cell.
- **P5. No scope.** The row states no plan or store. The nav entry's feature is the plan gate's, which `plan-gates` and SA-32 and SA-33 place with that feature as their scope.
- **P6. A store's 'Access restricted' lines** go in `reading`, quoted from the step with their line numbers, after reading which element they belong to. My two rows are the demo store's /marketing/blog (step 114) and /channel/mobile/reports (step 199). Both are the page's own lines, under the page's breadcrumb. Neither is a drawer over the home page, so SA-33's case (a row is `out`) doesn't arise. Every settings-drawer row of mine (`/?settings=/…`) has no store lines.
- **P7. The repository's own columns stay its own.** `held` and '(not swept)' are never a term, a scope or a quote. One reading names `held`'s 'no' for product_inventory, as the repository's observation.
- **P8. Rows the entry's rendering cuts.** Four entries end in '…' (54, 101, 102, 103), so their terms hold only the permissions the entry's text shows. Those the table's line holds beyond it (order_browse_status_canceled, order_browse_status_price_quote, report_shipping, report_payments, report_selling_channels) are named in `reading`. Entry 54's lines on CM-ORD-004 and CM-B2B-004 have no terms for that reason.

## Each new thing

None.

## Entries I couldn't tell, and what would settle each

- **19 My Subscriptions and 28 Payments (الماليات): two container lines each.** Each title names one thing (the subscriptions merchants pay for the partner's products; the partner's finances) that the model keeps as two capabilities.
  - If the coordinator reads either as a grouping over several capabilities' pages, the ruling after SA-28 makes it `out`.
  - No cell changes either way.
- **13 Influencer: two container lines,** CM-PTN-009 and CM-MKT-015, matching its two children.
- **17 Create Coupons on CM-APP-003 `core`:** SA-37 placed /coupons there, "unsure". The coupons are on what merchants pay for the partner's apps (SA-37's reading of /coupons/new). The page itself (`steps/019.text.txt`: 'Coupon details', 'Discount', 'Limit per user') doesn't say whose payments they discount.
- **18 Add Affiliate Product on CM-PTN-009 only:** its page offers marketers a commission to promote the partner's own products ('Market your products with affiliate', `steps/020.text.txt`, line 26). It isn't a store's affiliate programme (CM-MKT-014). Whether those products are apps, themes or services isn't stated there.
- **9 Affiliate Marketplace takes CM-MKT-014 `extension-point` too,** as that cell already holds the link. My Opportunities, Affiliate Orders and Active Merchants take CM-PTN-009 alone, as the concern map placed Affiliate Orders. Their pages show stores' affiliate opportunities, so CM-MKT-014 is their alternative.
- **11 and 12, Affiliate Orders and Active Merchants:** both pages answered 'Something went wrong loading this page.' (`steps/015.text.txt` and `016.text.txt`, line 32). Active Merchants is read from its title only. A page that loads would settle it.
- **41 to 53, the reports on CM-ANL-003 alone.** CM-ANL-002 (report types) is the alternative for each. CM-ANL-003 is the place the answer serves them from (Store performance's tabs). The tab each name stands for is a reading of their order: the answer's `index` ties (orders and sales both 1; conversion_rate and abandoned_carts both 6), and the page shows Sales before Orders.
- **product_sorting_edit (64) on CM-CAT-001:** SA-21's reading. No capability holds product sorting.
- **inventory_management (72) on CM-INV-006:** the model places it on inventory transfers, its staff group's thing. Its name alone would read as CM-INV-001.
- **custom_fields_management (64, 66) on CM-CHK-009,** as the cell holds it. On the products rows it may gate products' custom fields: SA-32's new thing Custom Product Fields, if the coordinator makes it.
- **The two 'Access restricted' lines (90, 108)** stand on the Pro demo store's own pages. Whether they rest on that account's permissions or on the unreleased features (store-blog, app-performance-reports) isn't stated. The account's permissions on the demo store would settle it.

## Structures whose items and sources disagree

- **`permission-gates`:** four entries' text ends in '…' before the row's permissions end. Entry 54 (/orders) cuts at 'order_browse_status_ca…'. Entries 101 to 103 (/reports/performance, /reports/smart-analysis, /reports) cut at 'report_shippin…' or near it. The table's lines 2, 49, 50 and 51 hold them whole. The source governs, so my readings name what is cut.
- **`performance-reports`:** the answer's `index` repeats (1, 1; 6, 6), while the page orders the tabs Sales, Orders and Conversion rate, Abandoned carts (`steps/001.text.txt`, lines 18, 19, 24, 26).
- **`partners-portal-navigation`:** the English label's items have no entries. They are the same 45 items in the same positions.

## What the sources state that no entry holds (for the second stage)

- **Store performance's page** (`raw/runs/20261008T211326Z-journey-reports-demo/steps/001.text.txt`):
  - 'Create report' (line 13) and 'Manage reports' (line 31): the merchant's own reports and the tabs' order and visibility, for CM-ANL-002 and CM-ANL-006 (the register says Manage reports writes `PATCH .../report/config/bulk`);
  - the summary's figures from line 35 on ('Gross sales', 'Net sales', 'Total costs', 'Net profit').
- **The affiliate marketplace's categories** (`20261008T124250Z-sweep-partner-portal-en/steps/013.text.txt`, from line 40): Electronics, Home Supplies and others, the stores' sectors a partner chooses from. They are a lead for CM-PTN-009 only. Taken alone, a list of sectors is market data.
- **My Opportunities' columns** (`steps/014.text.txt`): 'Affiliate Link', 'Coupon', 'Product', 'Sub Affiliate'. The affiliate's tools are a lead for CM-PTN-009 and CM-MKT-014.
- **product_inventory** is named by the navigation's Inventory audit (/products/quantities), but `capture/gates.py`'s join finds it in no staff permission group (`derived/permission-gates.tsv`, line 20). It is a lead on what the role editor offers for stocktakes.

## The checker's lines, read again

- **`CHANGES`:** none. Every line falls on a cell that already holds its support. The partners' links, the reports and the permissions are already the cells' evidence, through the concern map's portal navigation (SA-S-1905 to SA-S-1947) and the staff permission groups.
- **`NOTE` containers:**
  - line 4, خدماتي: CM-PTN-005;
  - line 8, التسويق بالعمولة: CM-PTN-009;
  - lines 15 and 16, المؤثر: CM-PTN-009 and CM-MKT-015;
  - line 21, أدوات التسويق جديد: CM-PTN-009;
  - lines 24 and 25, إشتراكاتي: CM-APP-003 and CM-SFR-003;
  - line 29, المتاجر: CM-DVT-003;
  - lines 36 and 37, الماليات: CM-PTN-003 and CM-PTN-004;
  - line 46, مركز المساعدة: CM-PTN-001.

  Each is as above (N3).
- **`NEW`:** none.
- No `own-service`, no third party and no quote found nowhere held.

## Problems with this brief or the script

- None that blocked.
- `entries.tsv` cuts a long entry's text with '…', and `show --width 4000` can't print past it. The checker tests terms against that text, so a permission the table holds beyond the cut can't be a term. I named those in `reading` (P8).
- The checker accepts a capability line with empty terms (entry 54's CM-ORD-004 and CM-B2B-004 lines). Such a line was needed by P8.
- The brief's reading list doesn't name `staff-permission-groups` or the navigation answers, which a `permission-gates` row is built from. I read them only for the permissions' labels and each address's item, as the brief's "cite the step or file it was built from" asks.
