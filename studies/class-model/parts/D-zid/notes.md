# D-zid: notes

Domain D, Customers and growth: Zid mapped onto the model of D-anchor, D-woocommerce and D-backfill-woocommerce. The part
runs in two batches.

## Batch 1: areas CUS, B2B, MKT and LOY

Concerns: ZD-C-091, ZD-C-103, ZD-C-087, ZD-C-088, ZD-C-089, ZD-C-106, ZD-C-019, ZD-C-090 and ZD-C-101. Cells: Zid's,
for every capability of the four areas (46). No capability added.

### How the concerns landed

- **Joined existing capabilities (8):** ZD-C-091 Customers in CM-CUS-001 (terms); ZD-C-103 Google Maps in CM-CUS-009
  (role, strained); ZD-C-087 Product availability notifications in CM-MKT-016 (definition); ZD-C-088 Coupons and
  discounts in CM-MKT-001 (terms); ZD-C-106 Marketing tools in CM-MKT-005 (terms, strained); ZD-C-019 Customer wallet and
  cashback in CM-LOY-001 (terms); ZD-C-090 Loyalty program in CM-LOY-004 (terms); ZD-C-101 Gifting in CM-LOY-006 (terms,
  strained).
- **New capabilities:** none.
- **Moved (1):** ZD-C-089 Bundle offers, `moved:B`. Zid's own words make it a product bundle: 'Bundle multiple products
  into one package' (ZD-S-0928), resting on the number of pieces (ZD-S-1032), 'ليست خصومات عادية' (ZD-S-1033). B-zid
  already cites all seven of its statements in CM-SEL-006 Product bundles, as core, beside Shopify's, Salla's and
  WooCommerce's bundles; D's model has no bundle capability. Landing it in D would make the same statements support core
  in two domains. scope.tsv read it as MKT from its API group Marketing > Bundle Offers and its path /discounts/ (ZD-S-0026,
  ZD-S-0106). **For the coordinator:** an amendment of B (`B-amend`) can land it in CM-SEL-006; until then `uncited`
  lists its statements under D, though B cites them.

### Grains chosen

- **Coarse concerns land in the parent:** ZD-C-088 (coupons, discounts, card discount) in CM-MKT-001; ZD-C-019 (wallet
  and cashback) in CM-LOY-001; ZD-C-106 (all of Marketing & Growth Tools) in CM-MKT-005; ZD-C-091 (the whole Customers
  section) in CM-CUS-001. Their finer statements are cited in the children.
- **Customer tags** (ZD-I-0031) are cited in CM-CUS-001, not CM-CUS-002: the anchor cites Shopify's customer.tags_added
  in CM-CUS-001, and Zid gives no definition that makes tags a segment.
- **Add Business Customers** (ZD-I-0348) is cited at the root CM-B2B-001, not in CM-B2B-002 Companies: the line names
  business buyers and nothing of a company's locations, contacts or prices. CM-B2B-002 and CM-B2B-003 are `none-held`.
- **WhatsApp Login** (ZD-I-0194) is cited in CM-CUS-013, a reading on role: Salla's WhatsApp verification is a code over
  WhatsApp; Zid's line names sign-in through WhatsApp without saying it is a code. Whether WhatsApp is an identity
  provider there (CM-CUS-011) isn't stated.
- **Automatic discounts** rest on one staff permission (ZD-I-0489) in CM-MKT-003; no place, API or plan line of their own.
- **App Market categories** (ZD-C-070, domain F) are cited as `extension-point` in the capability each names, as B-zid
  and F-zid did: إدارة العملاء (CRM) in CM-CUS-001, برامج الولاء والمكافآت in CM-LOY-004, العروض والترقيات in CM-MKT-001,
  التسويق والنمو in CM-MKT-005, أتمتة التسويق والحملات in CM-MKT-006, البريد الإلكتروني والرسائل النصية and التسويق عبر
  واتساب in CM-MKT-007, تتبع الحملات والإسناد in CM-MKT-008, التسويق بالعمولة والمؤثرين in CM-MKT-013 (it names both
  affiliates and influencers, so the parent), البيع المتقاطع والإضافي in CM-MKT-021, استرداد السلال المتروكة in CM-MKT-022.
  F-zid cites ZD-I-0455 in CM-APP-002 as well.

### Joins on role

- **CM-CUS-009 / ZD-C-103:** Zid's تفعيل Google maps, a setting the merchant turns on (ZD-S-0969, ZD-I-0131), with
  Salla's google-maps-service (SA-S-3119): both map services of the store. Neither says the map serves buyers'
  addresses. Context read beyond the statements, never cited: Zid's dashboard locale asks for Google maps to be turned on
  before an on-demand shipping level (`logistics.json`, serviceLevels.activationCondtions.onDemand), so the map may serve
  delivery more than addresses; the reviewer may weigh it.
- **CM-CUS-013:** WhatsApp Login (above).

### Strained fits

- **ZD-C-091 in CM-CUS-001:** its plan lines are cited in other trees: ZD-I-0348 (CM-B2B-001), ZD-I-0339 (CM-LOY-005),
  ZD-I-0351 (CM-LOY-004), ZD-I-0194 (CM-CUS-013, tree CM-CUS-010); and customer.create (ZD-S-0066) in CM-CUS-010. G-zid
  cites its ZD-I-0345 (Export Customer Data) in CM-MIG-001, domain G.
- **ZD-C-103 in CM-CUS-009:** what the map serves isn't stated (above).
- **ZD-C-106 in CM-MKT-005:** its affiliate statements (ZD-S-0974, ZD-I-0514, ZD-I-0292, ZD-I-0294, ZD-I-0295,
  ZD-I-0296) are in CM-MKT-014, tree CM-MKT-013. Its Store SEO Customization line (ZD-I-0300) is left to domain E.
- **ZD-C-101 in CM-LOY-006:** Zid never defines gifting; the join rests on the word الإهداء (Salla's نظام الإهداء
  الرقمي, SA-S-2623). Context, not cited: Zid's dashboard lists خاصية الإهداء among the marketing landing's tools
  (`marketing.json`, landing.tools.gifting).

### Grouping, for `parent`

- Zid's dashboard puts the customer wallet under loyalty programs: 'التسويق ← برامج الولاء ← محفظة العميل' (ZD-S-0666).
  The model keeps CM-LOY-001 and CM-LOY-004 as separate trees, by the anchor; Salla lists both as separate links under
  Marketing (SA-S-1820, SA-S-1823). Not changed.
- Zid puts availability notifications under العملاء in the dashboard (ZD-S-1028), its API under Products (ZD-S-0017),
  and the plan line under Product & Inventory Management (ZD-I-0248). The capability stays in MKT.
- Zid's Card Discount plan line sits under Payments (ZD-I-0225); bank discounts are cited in CM-MKT-018, the discounts
  tree, by the shared definition (Salla SA-S-5028).

### Homonyms kept apart

- **جملة:** Zid's بالجملة is 'in bulk' (Bulk Export Orders / تصدير الطلبات بالجملة, ZD-I-0263; Bulk Payment Status Update,
  ZD-S-0724); Salla's سوق الجملة is a wholesale market (CM-B2B-001). The hits weren't cited in B2B.
- **Cashback:** Zid's customer cashback (ZD-I-0028, ZD-S-0667, CM-LOY-003) and the plan cards' '50% cashback (on annual
  plan only)' (ZD-I-0374, ZD-I-0383, ZD-I-0396, domain A), Zid's discount to the merchant on its own plan. Apart.
- **Zid Wallet / محفظة زد:** the merchant's wallet for Zid's fees (ZD-C-017, ZD-S-0656, domain C), and the compare
  table's customers' payment option (ZD-S-0668, Q1 placed it in ZD-C-019). ZD-S-0668 is cited in CM-LOY-001 as `shows`
  only, since whether it is the customer wallet isn't stated. Zid Agent's wallet (ZD-S-0713) is a third thing.
- **قسائم:** Zid's قسائم التخفيض are discount coupons (ZD-S-0520, CM-MKT-002), not gift vouchers; Digital Vouchers
  (ZD-S-0008) are products' codes (B-zid, CM-SEL-002). CM-LOY-002 Gift cards is `none-held`.

### Concerns read under `also`

- **ZD-C-025 Zid Agent (F):** ZD-S-0717, 'AI-assisted features including … campaign management', cited as `shows` in
  CM-MKT-005. Its Vertex AI is a data processor of the agent, not a slot filler of campaigns.
- **ZD-C-082 Abandoned carts (C):** ZD-S-1018 and ZD-S-1019 (Zid Alerts) cited as core in CM-MKT-022. Its API and
  permission (ZD-S-0006, ZD-S-0474) and its plan lines on cart value, count and details (ZD-I-0289 to ZD-I-0291) are
  the carts themselves, not recovery: not cited.
- **ZD-C-112 Zid Voice (C):** ZD-S-0452 (core, a reading) and ZD-S-1069 (shows) in CM-MKT-022. No statement names Zid's
  company as Zid Voice's maker: a gap; the cell places it as one of Zid's own product lines.
- **ZD-C-040 Privacy (A):** read; its consent statements are consent to Zid's own processing (CM-CUS-007's reading).
- **ZD-C-098 Sender name (D, batch 2's NTF):** ZD-S-1046 cited as `shows` in CM-MKT-007, with هيئة الاتصالات as slot
  filler: promotional SMS go from a sender name ending in AD.

### Qualities and gaps

- **Number of Discount Codes / عدد أكواد الخصم** (ZD-I-0293, CM-MKT-002): a limit whose number the concern map doesn't
  hold. The structure that would hold it is Zid's compare-plans table (`plan-features`), whose entries Q1 placed without
  their per-plan values.
- **Plan lines without plans:** the `plan-features` entries cited here (ZD-I-0194, ZD-I-0339, ZD-I-0340, ZD-I-0343,
  ZD-I-0348, ZD-I-0350, ZD-I-0297, ZD-I-0301, ZD-I-0302, ZD-I-0304, ZD-I-0309, ZD-I-0311, ZD-I-0312, ZD-I-0351 and the
  affiliate lines) carry no plan in the concern map, as G-zid noted.
- **Not defined by Zid:** gifting (CM-LOY-006), the wishlist (CM-LOY-005), automatic discounts (CM-MKT-003), cashback
  (CM-LOY-003), Customer Location (ZD-I-0344) and Customer Targeting (ZD-I-0346). The last two aren't cited (see
  CM-CUS-008 and CM-MKT-011).
- Zid's statements of its own campaigns, affiliates and SMS have no API group (Q1's gap ZD-C-106/boundary).

### Rulings

None. Zid's concerns are in no Q1 match or unclear candidate (`concerns` prints none, and the brief says Zid has none), so
`rulings.tsv` holds its header only.

### Proposed renames (for the coordinator)

- CM-CUS-009: add Zid's تفعيل Google maps.
- CM-LOY-001: add Zid's محفظة العميل (Customer Wallets).
- CM-LOY-004: add Zid's Loyalty Program / برامج الولاء.
- CM-LOY-006: add Zid's خاصية الإهداء.
- CM-MKT-016: add Zid's Product Availability Notifications / إشعارات المخزون.
- CM-MKT-018: add Zid's خصومات البنك / Card Discount (خصم على البطاقة).
- CM-MKT-022: add Zid's تنبيهات زد and Zid Voice.

### What the checker flagged (batch 1)

- **ZD-C-070's App Market categories** (eleven entries): cited as `extension-point` on purpose, each the only statement
  of apps doing that capability on Zid; ZD-C-070 is domain F and doesn't name D. They support no `core`.
- **ZD-C-091/boundary/ZD-S-0066 in CM-CUS-001 and CM-CUS-010:** customer.create is both the record's webhook and the
  only statement that names a buyer's 'customer account'. The anchor keeps CM-CUS-010 outside CM-CUS-001's tree; the
  reviewer may keep one citation.
- **`none-held` with matches:** each cell's reading names its hits and why none is the capability: CM-CUS-003, -006
  (besides those named there, ZD-S-1052 and ZD-S-1053 are Meta's blocking of a WhatsApp number, and ZD-S-0631 and
  ZD-I-0224 block cash on delivery, domain C), -007, -008, -011, -012, -014; CM-B2B-002 (the matches are the B2B terms of
  the other platforms, read in CM-B2B-001); CM-LOY-002; CM-MKT-004 (the matches are coupons, card discounts and the
  discount report lines, all cited elsewhere or left to ANL), -009, -010, -011, -012, -015, -017, -019, -020.

### What batch 2 (areas SUP, ANL and NTF) needs

- **Its concerns:** ZD-C-086 Product reviews and questions, ZD-C-092 Customer self-service portal, ZD-C-097
  Notifications, ZD-C-098 Sender name, ZD-C-105 Reports and analytics, ZD-C-107 WhatsApp, ZD-C-111 Zid Assurance. Under
  `also`: ZD-C-025, ZD-C-040, ZD-C-082, ZD-C-112.
- **Already cited by batch 1 from batch 2's concerns:** ZD-C-098/reason/ZD-S-1046 in CM-MKT-007 (with the filler هيئة
  الاتصالات). By S1, ZD-C-098 lands `strained` unless it lands in CM-MKT-007's tree.
- **Left for ANL, from batch 1's concerns:** the report lines ZD-I-0280, ZD-I-0281, ZD-I-0282, ZD-I-0307 (ZD-C-088);
  ZD-I-0029 Wallet Analytics (ZD-C-019); ZD-I-0335, ZD-I-0337, ZD-I-0338, ZD-I-0341, ZD-I-0347, and perhaps ZD-I-0344
  Customer Location (ZD-C-091); and ZD-I-0322 Traffic Sources (ZD-C-105). If batch 2 cites ZD-C-088's or ZD-C-019's
  report lines in ANL, the clean fits of ZD-C-088 (CM-MKT-001) and ZD-C-019 (CM-LOY-001) no longer hold by S1: the
  coordinator marks them `strained` (ZD-C-091 is already strained).
- **Left for NTF:** Zid Alerts' settings entry التواصل › تنبيهات زد (ZD-I-0144, ZD-C-097), which bears on CM-MKT-022 too
  (ZD-S-1018 says Zid Alerts target abandoned carts); Bulk Customer Alerts (ZD-I-0304) is cited in CM-MKT-007; Zid
  Assurance's WhatsApp updates (ZD-S-0999).
- **App Market categories for its areas:** المراجعات والتقييمات (ZD-I-0453, SUP), خدمة العملاء والمحادثات (ZD-I-0435,
  SUP), التحليلات والتقارير (ZD-I-0432, ANL); الذكاء الاصطناعي والتحليلات (ZD-I-0430) is cited by F-zid in CM-AIA-001.
- **Product availability notifications** go by email or WhatsApp (ZD-S-1029, cited in CM-MKT-016).

## Batch 2: areas SUP, ANL and NTF

Concerns: ZD-C-086, ZD-C-092, ZD-C-111, ZD-C-105, ZD-C-097, ZD-C-098 and ZD-C-107. Cells: Zid's, for every capability
of the three areas (18). No capability added. Also one evidence row on batch 1's cell CM-MKT-022 (ZD-I-0144, below).

### How the concerns landed

- **Joined existing capabilities (7), none new:** ZD-C-086 Product reviews and questions in CM-SUP-001 (terms, clean);
  ZD-C-092 Customer self-service portal in CM-SUP-005 (terms, strained); ZD-C-111 Zid Assurance in CM-SUP-008 (role,
  strained); ZD-C-105 Reports and analytics in CM-ANL-001 (terms, clean); ZD-C-097 Notifications in CM-NTF-001 (terms,
  strained); ZD-C-098 Sender name in CM-NTF-004 (terms, strained); ZD-C-107 WhatsApp in CM-NTF-004 (terms, clean).

### Grains chosen

- **ZD-C-105** is Zid's whole Reports & Analytics section, so the parent CM-ANL-001. The plan lines named "Reports - …"
  (Total Profit, Sales Channels, Sales Value Over Time, Total Sales), the Product Cost Report, Export Data, the help
  article's التقارير (ZD-S-1048) and the custom reports (ZD-S-1050) are in CM-ANL-002. The unprefixed measures (Visit
  Count, Total Sales, Sales Value Over Time, Top-Selling Cities, Traffic Sources, Customer Journey Stages) and the measures
  in other plan groups are in the parent: no statement says where Zid shows them, so whether they are reports or the
  dashboard's isn't stated. A reading: the table lists "Total Sales" beside "Reports - Total Sales", which suggests two
  places, but no statement says so.
- **ZD-C-097** holds customers' order status messages and team notifications, so the parent CM-NTF-001; team
  notifications in CM-NTF-002; the sender, balance, OneSignal and WhatsApp statements in CM-NTF-004.
- **Batch 1's report lines** (ZD-I-0280, 0281, 0282, 0307 of ZD-C-088; ZD-I-0335, 0337, 0338, 0341, 0347 of ZD-C-091)
  are cited as core in CM-ANL-001, as measures; ZD-I-0029 Wallet Analytics (ZD-C-019) in CM-ANL-006, Zid's own API for
  its own feature. **Customer Location** (ZD-I-0344) is left uncited: not defined, it may be a field or a measure.
- **Zid Alerts' settings entry** التواصل › تنبيهات زد (ZD-I-0144) is added to batch 1's cell CM-MKT-022 as core: the
  only stated purpose of Zid Alerts is abandoned carts (ZD-S-1018). It is ZD-C-097's, so ZD-C-097 is strained.
  CM-MKT-022's reading (batch 1's) doesn't name it; the coordinator may add it.
- **The App Market category** خدمة العملاء والمحادثات (ZD-I-0435) names both customer service and chats, and CM-SUP-004
  and CM-SUP-005 are separate trees, so it is cited in both (the checker flags it).

### Joins on role

- **CM-SUP-008 / ZD-C-111:** Zid Assurance, where Zid 'handle[s] any complaints or inquiries' (ZD-S-0998), with Salla's
  Complaints, the store's record of its customers' complaints (SA-S-1865, SA-S-5089). On Zid the platform's company
  handles them (own-service); on Salla the merchant (core). **For the reviewer:** Zid Assurance is a program of three
  parts, complaint handling, WhatsApp order updates (ZD-S-0999, cited in CM-NTF-001) and a badge on the store (not
  cited). It can be split into a capability of its own, a buyer assurance program the platform runs, if another
  platform shows one; Salla's complaints platform (SA-C-178, domain A) is the nearest, and the anchor didn't cite it.
- **CM-ANL-003:** Zid's view.store.dashboard with Shopify's DASHBOARD and Salla's home summaries; no statement says
  what Zid's store dashboard shows.

### Strained fits

- **ZD-C-092 in CM-SUP-005:** its complaint statements (ZD-S-0935, ZD-I-0413) are in CM-SUP-008.
- **ZD-C-111 in CM-SUP-008:** its WhatsApp order updates (ZD-S-0999) are in CM-NTF-001 (above).
- **ZD-C-097 in CM-NTF-001:** ZD-I-0144 in CM-MKT-022 (above).
- **ZD-C-098 in CM-NTF-004:** batch 1's ZD-S-1046 in CM-MKT-007.

### Homonyms kept apart

- **Support, tickets and chat:** Zid's Ticketing & Chat System, Live Chat Support and 24/7 priority support (ZD-C-114,
  domain A: ZD-S-1003, ZD-S-1004, ZD-S-0378, ZD-I-0199, ZD-I-0359) are Zid's support to merchants, not the store's
  support to its buyers (CM-SUP-004, CM-SUP-005). Not cited.
- **FAQ:** Zid's FAQs to merchants (ZD-S-0530, ZD-S-1005, ZD-S-1006, ZD-I-0128) aren't a store's FAQ (CM-SUP-006).
- **سجل:** the commercial register (سجل تجاري) and 'registered' (مسجل) aren't a log (CM-NTF-003).
- **مباشر:** 'direct', not live (CM-ANL-004).
- **Badge:** the Zid Assurance badge (ZD-S-0999) and the API group Product Badge (ZD-I-0011, B-zid's CM-CAT-014).

### Concerns read under `also`

- **ZD-C-082 (C):** Zid Alerts (ZD-S-1018, ZD-S-1019), cited by batch 1 in CM-MKT-022; read for ZD-I-0144.
- **ZD-C-112 (C):** Zid Voice's 'smart, personal call' (ZD-S-1072) is a hit of CM-ANL-005, not smart analytics.
- **ZD-C-025 (F) and ZD-C-040 (A):** nothing for SUP, ANL or NTF.

### Slot fillers and qualities

- **CM-NTF-004:** هيئة الاتصالات وتقنية المعلومات (ZD-S-0958, ZD-S-0959) sets the sender name's terms; Unifonic / ينيفونك
  (ZD-S-0960), with whom Zid deals on the sender name and message packages (`outside`); Meta (ZD-S-1051 to ZD-S-1053,
  ZD-S-1055 to ZD-S-1057) sets WhatsApp's terms, prices and bans; the WhatsApp Business Platform (ZD-S-1054), on which
  واتساب زد is built. Not fillers: OneSignal, a scope's name only (ZD-S-0118, third_one_signal_write); the chamber of
  commerce (ZD-S-0959), which certifies the merchant's letter but neither does the capability nor sets its terms; RMS
  (ZD-S-1038), not identified as a third party. 'الفريق المختص من طرفهم' (ZD-S-0958): whose team it is isn't stated.
- **CM-SUP-005:** HubSpot, to whose tickets Zid Assurance's requests go (ZD-S-1038). **CM-SUP-008:** the Ministry of
  Commerce, with which Zid processes complaints (ZD-S-1000). Neither statement has a scope, so no market is stated.
- **Qualities:** Team Notifications' counts per plan (ZD-S-0954: starter "1", launch "1", growth "3", pro included);
  Order Status Notifications (Limited) (ZD-I-0287), whose limit the concern map doesn't hold: the structure that would
  hold it is Zid's compare-plans table (`plan-features`), placed without per-plan values, as batch 1 noted.

### Gaps and problems with the evidence

- **Plans named differently:** Zid's compare-plans table (starter, launch, growth, pro) says Reports - Sales Channels is
  on launch, growth and pro (ZD-S-1049); the help article says reports are only for الأعمال الكبيره, النخبة and
  الإحترافية (ZD-S-1048), and statistics elements aren't on زد لايت and النمو (ZD-S-1047). The map between the two sets
  of names isn't stated; each statement keeps its scope.
- **No analytics API:** Q1's gap ZD-C-105/boundary (searched, not found). CM-ANL-006 rests on Wallet Analytics only.
- **Not stated:** what Zid's store dashboard shows; what Order Streaks is (ZD-I-0190); the messages and templates Zid's
  notification settings control; whether واتساب زد carries conversations; the self-service portal's plans (Q1 gap
  ZD-C-092/decides, observation needed); a maker statement for Zid Assurance other than 'from Zid' and 'entirely on Zid'.
- **Zid Assurance's badge** (ZD-S-0999) is left out of CM-SUP-003: no statement says it is for trust.

### Rulings

None: Zid's concerns are in no Q1 match or unclear candidate.

### Proposed renames (for the coordinator)

- CM-SUP-001: add Zid's Product Reviews, Product Questions & Answers / الاسئلة.
- CM-SUP-005: add Zid's بوابة خدمة العملاء الذاتية (Customer Portal Tickets).
- CM-SUP-008: add Zid's ضمان زد (Zid Assurance); the name "Customer complaints about the store" fits both.
- CM-ANL-001: add Zid's Reports & Analytics / التقارير والتحليلات.
- CM-NTF-001: add Zid's رسائل حالات الطلب (order status messages).
- CM-NTF-002: add Zid's Team Notifications / إشعارات الفريق.
- CM-NTF-004: add Zid's اسم المرسل (Sender Name) and واتساب زد.

### What the checker flagged (whole part, after batch 2): 0 problems, 46 flags

- **Batch 1's rows, for the coordinator:** landings line 5, ZD-C-088 clean in CM-MKT-001, and line 8, ZD-C-019 clean in
  CM-LOY-001, now have statements cited in CM-ANL-001 and CM-ANL-006: by S1 both become `strained`, as batch 1 foresaw.
  The flag on ZD-C-091/boundary/ZD-S-0066 is batch 1's, answered above.
- **ZD-C-070's App Market categories:** batch 2 adds ZD-I-0453 (CM-SUP-001), ZD-I-0435 (CM-SUP-004 and CM-SUP-005) and
  ZD-I-0432 (CM-ANL-001), each `extension-point`, the only statement of apps doing that capability on Zid; no `core`.
- **ZD-I-0435 in two trees:** on purpose, above.
- **own-service:** ZD-S-0998 names Zid ('The service is entirely on Zid and we … handle any complaints'); ZD-S-0999
  names Zid ('A free program from Zid'); ZD-S-0935 names Zid's site (موقع زد) and Zid's support team as where a complaint
  against a store goes, a reading that Zid's company handles it. The reviewer may hold ZD-S-0935 as `shows`.
- **`none-held` with matches:** each of batch 2's (CM-SUP-002, -003, -006; CM-ANL-004, -005; CM-NTF-003) names its hits
  in its reading and why none is the capability.

## The coordinator's corrections after batch 2 (30 October)

- **ZD-C-088 and ZD-C-019 are `strained`.** Batch 2 cites their report statements in CM-ANL-001 and CM-ANL-006, other trees (S1).
- **CM-MKT-022's Zid cell** names the row batch 2 added, Zid Alerts' settings entry (ZD-I-0144).
- **D-zid added no capability,** so domain D needs no Zid back-fill. BigCommerce maps next.

