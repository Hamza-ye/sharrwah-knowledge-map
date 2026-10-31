# Held pass, Salla, batch SA-18: notes

85 entries (effort high), evidence at observed-sa@b0bd0b163: `dashboard-main-navigation`, its entries 43 to 127 (`merchant@ar/items.jsonl` lines 43 to 127, positions 42 to 126), from the Marketing group's first link إعلانات سلة to the Logs group's last link سجل الترجمة. SA-17 placed lines 1 to 42; SA-19 holds lines 128 to 133 (Home and the five top-bar buttons) and hasn't run.

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-18`); entry n is line n+42 of both `merchant@ar/items.jsonl` and `merchant@en/items.jsonl`.

**Placed:** 82 entries on capabilities, 0 `new`, 3 `out` (47, 71, 77), in 90 lines. Five entries take two lines: 2, 3, 7, 56 and 60. Supports: 89 `core`, 1 `shows` (53, Salla Chat). No `own-service`, `extension-point` or `outside`. No scope, no filler. One quality: `price: كاشير مجاني` (25, Salla Point's tag, as SA-20 read the same tag).

**Sources read:** the brief and what it names: the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register's row for the structure (and `dashboard-nav`'s); `show --meta` and the selection row; the rulings, their last section included; SA-17's notes and placements first, then SA-20's to SA-23's placements of the same items and addresses (`dashboard-nav`, `dashboard-nav-segments`, `dashboard-menu-store-channels`, `dashboard-menu-reports`, `dashboard-quick-actions`, `dashboard-settings-menu`) and the earlier lines on each address (SA-7 to SA-14, SA-30, SA-32), joined through `held/salla/entries.tsv`. Sources: `dashboard-main-navigation/merchant@ar/` and `merchant@en/` `items.jsonl` and `meta.json`, and `merchant@ar/source.html` for each group's heading element and each tag; run `20261008T113513Z-dashboard-menus` `steps/002.text.txt` (line 114, 'Basic'). To clarify only: `20261008T141131Z-sweep-merchant-en/steps/065.text.txt` (the Basic store's /channel/chat) and `20261008T122729Z-sweep-merchant-menus-ar/steps/065.text.txt` (/shipping, which SA-13 quoted). The model: the cells of every capability a line names, and of CM-OPS-005, CM-SHP-002, CM-SHP-009, CM-DVT-001 and CM-PAY-005 for the alternatives.

## The rules my lines follow

SA-17's nine rules, kept where the things are the same:
1. **The entries are the Arabic items;** each reading gives the English label at the same line of `merchant@en/items.jsonl`.
2. **A link takes the capability of the earlier line on the same item or address:** SA-20's `dashboard-nav` item of the same title and address for Marketing, Online Store, Sales Channels and Reports (each reading names the entry). The nav's data has no Customers, Staff, Help Desk, Shipping, Payment, Tools or Logs sections, so for those I kept to SA-21's and SA-22's segment of the same address (`dashboard-nav-segments`), which each reading names. Every one agrees with the routes' lines (SA-7 to SA-14) and the gates' (SA-30, SA-32) on the same address.
3. **`supports`: `core`,** but for Salla Chat (53): SA-8, SA-21, SA-23 and SA-32 placed the address `shows`, since its page says 'Salla Chat is no longer available for new subscriptions.' The same Basic store's page says so too (`20261008T141131Z-sweep-merchant-en/steps/065.text.txt`), so I kept `shows`. SA-17's rule 3 (core unless the gate isn't released) didn't meet this case.
4. **No scope:** the rendered entries carry no gate.
5. **Containers over several sections are `out`:** the h2 الإعدادات والأدوات (47, Tools & Settings), over the five groups the navigation API's menu `tools` answers with (SA-22's SA-E-8ca38054, out), by the rulings after SA-22 and SA-28.
6. **A group heading** (h3) goes on the capability its title names: المتجر الإلكتروني CM-SFR-001 (as SA-21 placed Store & Channels, which the mega menu names Online Store), قنوات البيع CM-CHN-001 (as SA-20 placed the same heading of the Store & Channels menu), العملاء CM-CUS-001, الموظفين CM-STF-001, التقارير CM-ANL-001 (as SA-21 placed the nav's section Reports), مركز الدعم CM-SUP-005 (see "couldn't tell"), الشحن CM-SHP-001 (as SA-32 placed the Shipping groups at /more and /tools), الدفع CM-PAY-001. Two headings name only a grouping over several capabilities' pages and are `out` (the ruling after SA-28; SA-22's notes name both so): الأدوات المساعدة (71, Tools: apps, the App Store, Merchant Services, webhooks) and السجلات (77, Logs: eight capabilities' logs). قنوات البيع (24) and الموظفين (37) are h3 headings set inside the previous group's list (`list: 4` and `5`), as `source.html` holds them; each is a group of its own.
7. **A quick action** (a `text` item whose `parent` is a link: the tooltip of the link's Quick actions button in `source.html`) takes its link's capability where it adds the link's own thing: إضافة صفحة جديدة (21), رابط جديد (23), انشاء صفحة هبوط (28), عميل جديد (32), مجموعة جديدة (35), إضافة موظف (39), دور وظيفي جديد (41), شكوى جديدة (52), طلب جديد under مواد التغليف (59, a packaging request, not an order: the homonym of SA-17's طلب جديد under إدارة الطلبات), إضافة قيد جديد (67), إضافة Webhook جديد (76). None is another thing, so none takes another capability.
8. **A link whose page is two things takes two lines, as the earlier lines gave it:** أدوات التتبع (2, CM-MKT-009 and CM-CHN-004, the English 'Pixels & feeds'), السلات المتروكة (3, CM-CHK-007 and CM-MKT-022), الحملات التسويقية (7, CM-MKT-005 and CM-MKT-007), أرشيف البوليصات (60, CM-SHP-002 by the Arabic, CM-SHP-009 by the English 'Shipment log', as SA-22). One more by the ruling after SA-4 (a thing only one language names takes its own line): شركات الشحن (56), whose Arabic names the shipping companies (CM-SHP-015's term) where the English label is 'Shipping & delivery' (CM-SHP-001's link); its page says 'فعّل شركات الشحن المناسبة' (`20261008T122729Z-sweep-merchant-menus-ar/steps/065.text.txt`). SA-20's third line for Pixels & feeds (CM-MKT-010, by the gate `salla-ads`) isn't taken: the rendered entry holds no gate, and a line resting only on a gate goes in reading (the ruling after SA-22).
9. **Tags** are marks, not qualities, except a price: الأكثر زيارة on تصميم المتجر (17) and كل ما تحتاج / 'Essentials' on خدمات التاجر (74) are in `reading`; كاشير مجاني on سلة بوينت (25) is the quality `price: كاشير مجاني`, as SA-20 read it. The terms drop the tag where the text runs into it (تصميم المتجر, خدمات التاجر).

**Leads set aside:** CM-PTN-005 on /marketing/influencers and CM-MKT-015 on /manage/experts (the address alone); CM-PAY-032 on رابط, عميل and دفع; CM-CHK-008 on شراء and طلب; CM-CUS-001 on العملاء inside نظام ولاء العملاء; CM-CUS-006 on عميل; CM-AIA-003 on SEO; CM-MKT-007 on نصية; CM-PAY-009 on شكوى; CM-PAY-020 on العمليات; CM-INV-002 on سجل for the deleted products; CM-MIG-001 on التصدير for the export log (CM-MIG-004); CM-PAY-016 on طرق الدفع; CM-PAY-005 on /payments/wallet (the wallet is CM-PLN-006, the cell's own link; the payouts tabs are SA-14's lines).

## New things

None.

## Entries I couldn't tell, and what would settle each

- **48, مركز الدعم (Help Desk):** CM-SUP-005, by its English title, the cell's help desk, and its Arabic support centre, one part of the admin. Its five links are four capabilities' pages (CM-SUP-001, CM-SUP-005, CM-SHP-022, CM-SUP-004, CM-SUP-008), so `out` by the ruling after SA-28 is the alternative, if the coordinator reads Help Desk as only a grouping. Domain D's support area has no parent capability that holds all five. Searched: help desk; مركز الدعم; support centre; customer support; خدمة العملاء; الدعم الفني (CM-SUP-005 and CM-ONB-003, the platform's support for merchants, which this isn't).
- **82, سجل المنتجات المحذوفة (Deleted products, /products/trash):** CM-CAT-001, as SA-21 placed the segment. No capability holds deleted products; CM-ORD-012 is deleted orders, though its released flag restore-data and permission restore_data_management cover deleted data in general (its cell's reading). If the coordinator widens CM-ORD-012 to deleted records, this line moves there. Searched: deleted products; المنتجات المحذوفة; محذوف; restore; استعادة.
- **56, شركات الشحن:** two lines (CM-SHP-001, CM-SHP-015). If the ruling after SA-4 takes only the more exact words, the Arabic شركات الشحن (CM-SHP-015) would be the one line; the earlier lines on /shipping are all CM-SHP-001, by the English label and the route.
- **71 and 77 (Tools, Logs), `out`:** M-13's line on a capability is the alternative only if one is found that the titles name; for Logs, CM-OPS-005 (Store logs) is a homonym, as its note and its empty Salla cell say, and CM-TRU-003's note names Salla's Logs section (/logs) only as holding the export log beside the activity history.

## Differences between the rendered menu and the nav's data (for SA-19 and the coordinator)

- The rendered Marketing group lacks the nav's Blog (/marketing/blog, gated by `store-blog`, released false); the rendered Sales Channels lacks Souq Eljomla (/channel/vendors). Both are among SA-20's four items whose gate isn't released.
- Salla Ads: rendered at /marketing/ads/dashboard, the nav's data at /marketing/ads/v2/dashboard. The Customer wallet and Reorder Reminder: the nav's data writes `marketing/customer_wallet` and `marketing/reorder-reminders` with no leading slash; the rendered links have one.
- The Shipping group's first link is شركات الشحن in Arabic and 'Shipping & delivery' in English at the same position; the mobile menu (/more) names the group itself الشحن والتوصيل, the mega menu الشحن.
- The tags Most Viewed (الأكثر زيارة) and Essentials (كل ما تحتاج) are rendered; the nav's data gives Store design's tag `visible_days` 0 (SA-20's reading).

## Items against sources

None: each entry's text matches `merchant@ar/items.jsonl` at its line, and the English file holds the same addresses in the same order. In `source.html` the group headings are h3 elements (with an icon each), الإعدادات والأدوات an h2, the tags `s-tag` elements inside the link, and each quick action a `p.text-xs` inside the `s-tooltip` of the link's button.

## For the second stage: what the sources state that no entry holds

- `20261008T141131Z-sweep-merchant-en/steps/065.text.txt` (the Basic store's /channel/chat), lines 13 to 17: 'Everything you need to serve your customers', 'Provide unparalleled support with quick access to your customer's profile and order history, making your service faster and more accurate.', 'Stay connected with your customers through various communication channels, including WhatsApp and your store's website, without the need for external tools.' For CM-SUP-004, which cites the Arabic of the last (SA-S-5138).
- `20261008T122729Z-sweep-merchant-menus-ar/steps/065.text.txt` line 20 (/shipping): 'فعّل شركات الشحن المناسبة، واضبط أسعار التوصيل بالطريقة التي تناسب متجرك، وتابع تكاليف البوليصات من مكان واحد': the carriers (CM-SHP-015), the delivery prices (CM-SHP-001) and the labels' costs (CM-SHP-002) on one page.

## The checker's lines, read again

- **No `CHANGES` line.** Every line falls on a cell that is already `core`, or adds `shows` where the cell holds `core` (CM-SUP-004).
- **`NOTE` containers, 11 lines:** the links whose quick actions are entries with that link as `parent` (الصفحات التعريفية, روابط مخصصة, صفحات الهبوط, إدارة العملاء, إدارة المجموعات, إدارة الموظفين, الأدوار الوظيفية, بوابة الجودة, مواد التغليف, قيود الدفع, أدوات المطور). Each link is placed on its own capability and each action has its own line (rule 7). The group headings aren't flagged, since their `parent` is الكل; they are containers too (rule 6).
- **No `NEW` line.**

## Problems with the brief or the script

- **`show` prints a quick action's `parent` as its link's text,** as SA-17 found; in this batch no two parent links share a title, but طلب جديد (59) shares its own text with SA-17's quick action under إدارة الطلبات: its parent, position 99 (مواد التغليف), settles it.
- **The checker flags the links with quick actions as containers but not the group headings,** whose `parent` is الكل's position: the headings are the containers that rule 3 governs here.

The checker's last line, for SA-18: `85 of 85 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes.** The batch's lines agree with the routes' (SA-7 to SA-14), the gates' (SA-30, SA-32) and the nav segments' (SA-21, SA-22) lines on the same addresses.
- **The agent's open points stand as placed:**
  - 48 مركز الدعم stays on CM-SUP-005. A container goes on the capability its title names (M-13), and this title names the help desk.
  - 82, the deleted products' log, stays on CM-CAT-001, as SA-21 placed it.
  - 56 شركات الشحن keeps both lines, by the ruling after SA-4.
- **Salla Chat is `shows`,** as SA-8, SA-21, SA-23 and SA-32 placed it. Its cell is read again at Salla's amendment.
- **The checker's container notes are left as they are.** The checker flags the links with quick actions as containers, but not the group headings. The agent read the headings under rule 3, and SA-19 holds only six more lines of this structure, so the checker isn't changed for it.
- **Cost:** 9.6 million tokens over 52 requests, about 113,000 an entry.
