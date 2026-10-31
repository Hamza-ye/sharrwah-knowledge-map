# Notes: held pass, Salla, batch SA-27 (`invoice-settings`, rest; `kyc-schema`; `merchant-subscriptions`; `onboarding-missions`, first part)

## What I read

- The brief, `H-held.md`; the evidence map; the coordinator's rulings, `held/review-H-rulings.md`, to its last section.
- observed-sa (at `b0bd0b16`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the `structures/REGISTER.tsv` rows of my four structures; `docs/PLAN.md`'s line on the public demo (giftshop2024).
- The four structures' `meta.json` (`show --meta`) and their `selection.tsv` rows: `invoice-settings`, `kyc-schema` (rule `nested:states,actions,fields,steps`) and `merchant-subscriptions` are `decides`; `onboarding-missions` (rule `nested:completed,pending,uncompleted,available,missions,tasks;drop:statistics,steps`) is `where`.
- SA-26's notes and placements (its rules I1 to I4, its proposal for SA-27, the coordinator's check); SA-7's and SA-9's checks and their CM-ONB-004 lines (SA-7's SA-E-d56afc4e, the app ui-merchant-gamification, the merchant's setup tasks); SA-9's scope `kyc_country SA`; the Salla lines that placed /billing (CM-PLN-004, SA-E-2d68c56e).
- **Sources:**
  - `invoice-settings @public-demo@en`: `source.json` and `items.jsonl`; `raw/runs/20261009T022751Z-sweep-public-demo-en/responses/0205.json` (step 5); its page `20261009T022751Z-sweep-public-demo-en/steps/009.text.txt`, lines 20 to 95.
  - `kyc-schema @demo@en`: `source.json` read whole by its keys (`raw/runs/20261008T133523Z-sweep-demo-store-en/responses/2703.json`, step 76): `workflow_actions`, `renderer_schema`'s `plugins`, `transitions`, `validations`, `translations`, `settings`, and each state's markup, with the buttons that call each plugin and their `visibleOn`.
  - `merchant-subscriptions @public-demo@en`: `items.jsonl` (15 items) and the answer `raw/runs/20261009T022751Z-sweep-public-demo-en/responses/8004.json` (step 201); the page `steps/201.text.txt`; `structures/salla/shipping-carriers/public-demo@en/items.jsonl` for the carriers.
  - `onboarding-missions @public-demo@en`: `source.json` (`raw/runs/20261009T021126Z-journey-public-demo-entry-en/responses/0044.json`, step 3), each entry's object at its pointer; the home page `20261009T021126Z-journey-public-demo-entry-en/steps/003.text.txt`.
- The cells of every capability my lines name, and `caps --terms` for the things no lead named (below).

## The batch, and the batches beside it

- **`invoice-settings`:** SA-27 holds the last 9 of its 52 entries (1 to 9), the public demo's English fields after order-status. With SA-26 the structure is now placed whole.
- **`kyc-schema`:** placed whole here (10 to 29), the first batch to place it. Its 20 entries are only the actions of the workflow's 8 plugins (`renderer_schema/plugins/*/actions`). The states, their fields and texts, the transitions, the validations and the translations have no entries (below, for the second stage).
- **`merchant-subscriptions`:** placed whole here (30 to 44), the first batch to place it. Its 15 items are page 1 of 5 of the store's 61 subscriptions ('1 to 15 of 61. Page 1 of 5', `steps/201.text.txt`, line 26; the answer's `pagination`, total 61). Pages 2 to 5 aren't held.
- **`onboarding-missions`:** SA-27 holds its first 37 of 61 entries (45 to 81): the store's first 9 completed missions and their 28 tasks. **SA-28 holds the rest and hasn't run:** the missions سهّل قرار الشراء على عميلك (6 tasks), سوّق لمتجرك مجاناً (7), وسّع وصولك بالتسويق المدفوع (4) and اعرف كيف تجهّز أول طلب (3), 24 entries. The coordinator aligns the two; the rules my lines follow, for SA-28, are O1 to O5 below.

## Rules my lines follow

### Invoice settings (SA-26's I1 to I4, kept)

- Each field is CM-ORD-008 `core` (I1), with its label, description and tooltip quoted, and its type, default and value on the public demo in `reading`; no scope, no quality (I4).
- SA-26's proposal for SA-27 is followed: product-weight, show-product-id, show-GTIN and show-MPN take CM-CAT-001 `shows`; auto-send-invoice takes CM-NTF-001 `shows`; show-zero-tax takes CM-TAX-001 `shows`; show-delegate-details takes `new:Shipment receipt by another person` `shows` (I2). invoice-title and watermark-opacity take I1 alone (I3). The terms are the English words.
- The public demo's page draws watermark-opacity as 'Transparency' under 'Upload watermark' (`009.text.txt`, lines 82 to 86, after the watermark's upload), and invoice-title as 'Invoice title' with [فاتورة] and AR (lines 25 to 28).

### Store verification (`kyc-schema`)

- **K1.** Each action of a plugin is a step of Salla's own store verification, the workflow `merchants_saudi_kyc`: CM-PAY-003 `core`, whose cell holds Store Verification at /payments/kyc. Its reading names the plugin, the endpoint its `workflow_actions` entry posts to, the button that calls it, and the state its transition leads to.
- **K2.** `out`: an action that only keeps a value in the workflow's context (`set_context`, `otp_id`), the software's own stored state; and a `set_error` whose message is only the generic fallback 'حدث خطأ ما، يرجى المحاولة مرة أخرى', a message that names nothing. Each `out` reading names the entry that places its step.
- **K3.** A `set_error` or `set_toast` whose message names what the step does is placed by K1: 14 (a wrong code refused), 16 (the code resent), 17 (the resend failed).
- **K4.** The three OTP plugins (`sync_otp`, `verify_otp`, `resend_otp`) also take CM-TRU-002 `core`: the store owner's identity checked by an OTP sent from Absher (the state `store_owner_details_verify`, 'Enter the OTP sent to your mobile registered in Absher'). Absher is named only in the source's states, so it is in `reading`, not `filler`.
- **K5.** The `sync_iban` actions also take CM-PAY-005 `shows`: the bank account the cell holds as the one tied to store verification, to which Salla transfers dues (SA-S-0094).
- **K6.** Scope `merchants_saudi_kyc`, the workflow's own id, the condition the source states the actions for. The store's other workflows aren't held as structures (observed-sa's GAPS names the UAE store's `merchants_uae_kyb_workflow`). Terms are the plugin's id and, where the entry gives one, its key, event or message.

### Subscriptions (`merchant-subscriptions`)

- **S1.** A subscription's record is the store's own data: its ids, dates, invoice, status, price paid, remaining days and actions. It goes in `reading`, never as a line of its own. What the subscription names is placed (the brief's rule on `out`): an app (`type: addon`, `type_value: APPS`) on the capability of what its name names, and a domain (`type: domain`) on CM-SFR-008. No CM-PLN-004 or CM-APP-003 line per entry: the billing of the subscription is the record.
- **S2.** An app whose name names a third party's product takes `extension-point`, the third party as `filler`, as M-3 is refined after WC-3 (a suggestion that names a third party's product). These are Mrsool, SPL and Sent Express, which Salla's shipping companies on the same store list as carriers of type app (`shipping-carriers/public-demo@en/items.jsonl`, lines 10, 12 and 14); TikTok Pixel - Catalog; and Zoho Mail. An app whose name names no maker takes `shows`, as M-3 is refined (naming no maker shows the thing). Salla's hosting of partners' apps (CM-APP-001's SA-S-0037) doesn't name any one app's maker.
- **S3.** Where the name doesn't say what the app does (Salla Engage, Naseej Abayas, Bousla) or no capability holds it (Zoho Mail), the line goes on CM-APP-001, the store's apps.
- **S4.** Scope `giftshop2024`, the public demo's store, as Salla addresses it (salla.sa/giftshop2024, `20261009T022751Z-sweep-public-demo-en/steps/039.text.txt`, line 44). An app's price is its offer's, in `reading`. The domain's price, 50 SAR plus tax 0.15, 57.5 SAR 'Annually', is Salla's for its own domain service: `quality` `price: 57.5 SAR, Annually`. That is a reading.

### Missions and tasks (`onboarding-missions`, for SA-28)

- **O1.** A mission (an entry with `gameId`) is a container of setup tasks: CM-ONB-004 `core`, its group, the missions, being the merchant's setup tasks, as SA-7's SA-E-d56afc4e (M-13). No scope. Its list (`completed`), `celebrated` and the task counts are the store's state, in `reading`.
- **O2.** A task is CM-ONB-004 `core`: a setup task of Salla's dashboard. Its reading quotes its title and description, and gives its mission, `task_type`, `ctaLink`, theme, `estimatedTime`, `isSkippable` and `paid`. Its `status` (complete, skipped) is the store's state.
- **O3.** Scope: the task's `plan` (basic, plus, pro), in the source's identifier. Whether it is a listing condition or the plan a task's feature needs isn't stated: the public demo, badged Basic on that date (`docs/PLAN.md`), holds tasks of every plan.
- **O4.** Each thing a task's or a mission's title or description names takes a line on its capability:
  - `shows` where the task only tells the merchant to use the thing;
  - `core` where its words state what Salla itself does or has: 'تفعيل شركات الشحن في سلة فقط بضغطة زر' (59), 'شركات الشحن تتفعّل تلقائياً في متجرك' (79), 'يفعّل ظهور عدد زوار متجرك في تقارير سلة' (80), 'سلة توفّر لك مواد تغليف مجانية' (81);
  - `extension-point` where it names a third party's product (Hotjar, Google Analytics, Claude and ChatGPT), the third party as filler (M-3 refined);
  - a `ctaLink` to an app's page (/apps/view/<id>) that names no maker gives `shows` (the WhatsApp button, 56 and 74; the blog, 49).
  
  A `ctaLink` names another place, so it doesn't give a line by itself. It is cited where it is the cell's own link (/channel/pages, /payments, /manage/domain, /shipping, /shipping/packing, /settings/general/salla-mcp).
- **O5.** A title that names only a goal (استقبل أول زبون, حقق أول طلب, ابنِ الثقة في متجرك, ابدأ اجذب الزوار لمتجرك, جهّز أول طلب, اعرض منتجاتك بإحترافية), and a task that only gives advice with no feature named (51, 62, 64, 65, 68), take O1 or O2 alone.

## Each new thing

- **`new:Shipment receipt by another person`:** SA-E-212804a4 (9, show-delegate-details, public-demo@en), the English counterpart of SA-26's SA-E-e083d60c. SA-26's notes give its definition, domain and the terms it searched. Its English words are 'delegate', 'When a delegate is assigned to receive the order'. Place of its own: none held.
- **`new:Recently Viewed Products`:** SA-E-10582cc4 (35), the app 'Recently Viewed Products App' on the public demo's subscriptions, `shows`.
  - **What it is:** a reading, from its name only: products a buyer viewed, shown again on the storefront. The entry says nothing else.
  - **Place of its own:** none held; it is an app.
  - **Proposed domain, area and parent:** domain D, beside CM-MKT-023 (product recommendations), or under it if the coordinator reads a recently viewed list as a recommendation. The cell's note keeps MKT-023 to products the platform recommends, so I didn't place it there.
  - **Names:** English 'Recently Viewed Products'; Arabic not held in the entry.
  - **Searched:** recently viewed; شوهدت; recommendations; upsell; cross-sell.
- **`new:تقييم جودة بيانات`:** SA-E-7811b65d (76), the task ارفع جودة صفحة منتجك.
  - **What it is:** 'في صفحة كل منتج في لوحة التحكم فيه ميزة «تقييم جودة بيانات»': each product's page in the dashboard rates the product's data. The higher the rating, the more the product shows in Google's results; the task's target, 'أعلى من 70%', is advice.
  - **Place of its own:** none held: a feature inside the product page. So it is `shows`, as the brief says for a thing with no place of its own. The task states it as Salla's own feature in its dashboard, which would read `core`; the coordinator decides.
  - **Proposed domain, area and parent:** domain B, under CM-CAT-001 (the product's record), or beside SEO (CM-CNT-007).
  - **Names:** Arabic تقييم جودة بيانات (المنتجات); English not held.
  - **Searched:** data quality; جودة; جودة بيانات; quality score; product score; listing quality. Only complaints and carrier ratings matched.

## Entries I couldn't tell, and what would settle each

- **CM-TRU-002 `core` (11, 13, 14, 16, 17):** the CHANGES, below. The alternative is `shows`, as the cell's help articles were read, or `outside`, with Absher doing the check. What Absher's step returns to Salla isn't stated. The coordinator's reading of who verifies (Salla's workflow calling Absher, or Absher) would settle it.
- **14 and 17, error messages placed:** I read a message that names the code's check (a wrong code, a failed resend) as a statement of the step, unlike the generic fallback. If the coordinator holds every `set_error` to be a UI string, both go `out` with the six others.
- **20, sync_bypass:** I read its button, shown where the chosen bank isn't one of the eleven banks the IBAN check shows for, as passing the bank account to review without the automatic check. The validations then ask an IBAN certificate for such a bank. That is a reading of the conditions. A run of the bank account step with another bank would settle it.
- **30, Voice Search on CM-SFR-013**, read from the name. **37, Tajer Report on CM-ANL-002**, read from 'Report'. **39, DropCard on CM-SEL-002.** **41, Numoo on CM-MKT-021**, from 'Increase the value of your shopping cart'. **36, Guest Wishlist on CM-LOY-005.** All are readings of an app's name. Each app's listing in Salla's app store (`marketplace-apps`, `apps-sitemap`), which my sources don't name, would settle what it does and who makes it.
- **34, Zoho Mail:** a mail service, by its name. No capability holds a mailbox for the merchant (searched email; إيميل; البريد الإلكتروني; mail; Zoho: only CM-PAY-028, Zoho's accounting, and the marketing and notification capabilities). On CM-APP-001. A domain's mail (CM-SFR-009, DNS records) is a lead.
- **38, Salla Engage:** Salla's brand in the name names no maker (the brief). Who makes it and what it does are gaps. If a held statement names Salla as its maker, its line is `own-service`.
- **42, the domain's price as a quality:** I read the subscription's price for a .com domain as Salla's offer's price. If it is this store's own record, it moves to `reading`.
- **48, Hotjar on CM-ANL-001:** session recordings and heatmaps of visitors, 'شاهد جلسات حقيقية لزوار متجرك بالخرائط والتسجيلات عبر Hotjar'. No capability holds them (searched recording; تسجيلات; heat; session; جلسات; behavio). CM-ANL-001 is the nearest. The coordinator may want a capability of its own.
- **55, جهز مظهر متجرك on CM-SFR-001 `shows`:** a reading of 'مظهر' (look) as the store's design.
- **70, Salla Point's payments on CM-PAY-021 `shows`:** 'تستقبل المدفوعات مباشرة من الجوال، بدون الحاجة لجهاز منفصل'. Who processes them isn't stated in the entry. The cell's Geidea is from other statements.
- **77, the social media accounts on CM-ACC-006:** the store's accounts, as the cell's permission store_setting_edit_social_media_account; the task's link is the themes editor's footer (CM-SFR-002), which I didn't give a line, since a `ctaLink` names another place.
- **O3, a task's `plan`:** see O3. The feature list (`dashboard-features`) by each task's feature would settle whether the plan gates the task.

## Structures whose items and sources disagree

- **`kyc-schema`:** the rendering of 23 and 24 (`set_state`) leaves out each action's `condition`, which the source holds at the same pointer. The source governs, and my readings give it:
  - 23's condition is `entity_type` single with `account_type` business or 'business account';
  - 24's is the error “Action 'IbanVerification' failed: Your application has been rejected due to repeated incorrect IBAN attempts.”
  
  Also, the actions' `value` is the string "true" in the source; `show` prints it as true.
- **`onboarding-missions`:** `show` collapses double spaces. The mission فعّل الدفع والشحن is 'فعّل الدفع والشحن  💳' in the source. One task's `completed` label has a leading space, ' اطّلع على التفاصيل' (78). My quotes are copied from the source. The rule drops `statistics`, which I cite for the missions' task counts.
- **`merchant-subscriptions`:** the items hold page 1 of 5 only (above).
- **The public demo's plan:** the invoice settings and subscriptions pages both show 'Your سلة سبيشال subscription is paused' (`009.text.txt`, line 20; `201.text.txt`, line 16, under the badge Basic, line 9). The home page of the run before shows بيسك (`20261009T021126Z-journey-public-demo-entry-en/steps/003.text.txt`, line 9). observed-sa's `docs/PLAN.md` says its badge read Basic until 2026-10-09 and Special on 2026-10-28. I gave no plan scope to the invoice lines (I4), and gave the store's name for the subscriptions (S4).

## What the sources state that no entry holds (for the second stage)

- **The store verification's schema** (`structures/salla/kyc-schema/demo@en/source.json`):
  - the requirements preview: 'The store owner's national ID must be valid and fully match their data on the Absher platform.'; a freelance work permit, or a commercial registration, by entity; the bank account must match the owner's ID, the permit or the registration. These are leads for CM-PAY-003, CM-TRU-002 and CM-ACC-004.
  - the entity types Single Establishment, Company, Institution, Charity and Government, with each one's documents (commercial registration, freelance certificate, charity certificate, licence and an official authorization letter): leads for CM-ACC-004, whose Salla cell holds only فرد.
  - the bank list (Saudi and foreign banks, STC Bank and D360 Bank among them), personal and business account types, the IBAN certificate, and 'I declare that all submitted data is accurate and I accept legal responsibility for any incorrect information': leads for CM-PAY-005 and CM-PAY-003.
  - the limits: `settings.max_file_size_mb` 10, and 'File must be valid PNG JPEG JPG or PDF format and maximum 10 MB size': a quality for CM-PAY-003.
  - the rejections after repeated incorrect IBAN, commercial registration or freelance certificate attempts, and the statuses 'KYC request Rejected' and 'Revision Required', with their descriptions: leads for CM-PAY-003.
  - the actions' names, AbsherVerification, IbanVerification, FreelanceVerification, CommercialRegistrationLeanVerification and NasaKyc, in the translations' keys: what Salla checks at each step.
  - the manager's OTP, 'enter the otp sent to the manager mobile registered in absher': a lead for CM-TRU-002 (a manager besides the owner).
- **The subscriptions page** (`20261009T022751Z-sweep-public-demo-en/steps/201.text.txt`): its tabs Store plan, Additional Subscriptions and Invoices (lines 10 to 12), its filters All, Active, Inactive and Expire soon (lines 22 to 25) and its columns (lines 27 to 34): leads for CM-PLN-004 and CM-APP-003. The answer's items' actions (renew, cancel, cancel auto-renew, payment schedule, usage details, `is_installment`) are leads for CM-APP-003's billing of apps.
- **The home page** (`20261009T021126Z-journey-public-demo-entry-en/steps/003.text.txt`):
  - its monthly goal, 'أضف هدف الشهر' (line 44);
  - the abandoned carts widget's 'غير متاح في باقتك' (lines 49 and 50), for CM-MKT-022 on Basic;
  - the series 'سلة خطوة بخطوة' (line 52), for CM-ONB-003;
  - a changelog post on Mushammir's recommended products (line 58): 'العناصر مخصصة للباقات المدفوعة، وهي مُفعّلة تلقائياً لباقتي برو وبلس', a lead for CM-MKT-023 and CM-AIA-001;
  - the partners' apps bulletin (lines 60 and 61), naming apps by category (marketing, WhatsApp, accounting and ERP, shipping), leads for CM-PAY-028, CM-SHP-015, CM-SUP-004 and CM-MKT-021.
- **The missions' `user_state`** (`current: state:inactive`, `celebrated: true`) and the tasks' `config.labels` and `helpCenterArticle`: the store's state and the tasks' button labels. No line.

## The checker's lines, read again

- **`CHANGES` CM-TRU-002 gains `core`** (lines 20, 23, 25, 28, 30; entries 11, 13, 14, 16, 17):
  - Salla's own verification workflow sends the owner's OTP and checks it through its KYC API: /kyc/api/kyc/steps/{step_name}, /verify and /verify/resend.
  - The state reads 'OTP Verification - Store Owner' and 'Enter the OTP sent to your mobile registered in Absher', after the owner's identity number and date of birth.
  - The cell held only `shows`, from help articles on the same Absher step (SA-S-0132), under SA-C-006. I read these as the platform doing the identity check itself, with Absher's OTP (a reading). If the coordinator holds the check to be Absher's, the lines become `shows` or `outside`, and the cell stays as it was.
- **`CHANGES` CM-AIA-004 gains `extension-point`** (line 128; entry 78): the task 'اربط متجرك بـ Claude أو ChatGPT وتحكّم فيه بسهولة 🤖'.
  - Its words: the merchant links the store to Claude and ChatGPT, and adds products or improves their descriptions in a chat.
  - Its ctaLink is the cell's own setting, /settings/general/salla-mcp.
  - Third parties' assistants do the merchant's work through the MCP server Salla provides, with Claude and ChatGPT as fillers. It also states whom the assistant acts for, which the cell had found unstated.
- **`CHANGES` CM-CHN-004 gains `extension-point`** (line 61; entry 44): TikTok Pixel - Catalog, read from its name as TikTok's catalog, a product feed for a channel (S2). It rests on the name alone; the app's listing would settle it. If the coordinator doesn't take a feed from the name, the line goes, and the CM-MKT-009 line stays.
- **`CHANGES` CM-ONB-004 becomes held, with `core`** (the 37 onboarding lines). This is the same thing as SA-7's ui-merchant-gamification, the merchant's setup tasks, which SA-7's check already changes. These lines are its contents.
- **`NOTE` line 16, the new Shipment receipt by another person:** its leads CM-PTN-004, CM-CHK-010 and CM-MKT-018 matched only 'invoice', 'switch', 'when' and 'applied'; their cells hold no delegate. The setting's own line is line 15.
- **`NOTE` line 51, the new Recently Viewed Products:** its leads CM-APP-001, CM-MKS-008, CM-PAY-001, CM-CAT-013 and CM-PAY-014 come from 'apps/installed', 'product_id', 'payments' and 'detail'. Read, none is recently viewed products. CM-MKT-023 was read (above).
- **`NOTE` line 121, the new تقييم جودة بيانات:** its leads CM-PLN-001 (by 'basic'), CM-SHP-022 (by 'تقييم', 'جودة', carriers' ratings) and CM-SFR-015 (by 'منتج') are not it.
- **`NEW`:** the three new things above.

## Problems with this brief or the script

- None that blocked.
- `show` collapses double spaces and prints a string "true" as true. The source must be read for an exact quote (above).
- The brief's rule on `out` names "its subscription records" as one store's data, and the message for this batch says what a subscription names is the platform's offer. Neither says which `supports` an app named in a store's subscriptions takes. I read it by M-3 as refined after WC-3 (S2); the coordinator may rule otherwise.

## The coordinator's check (31 October 2026, after the batch)

- **CM-TRU-002 gains `core`,** and it stands. Salla's workflow `merchants_saudi_kyc` runs the owner's verification as its own steps: `sync_otp`, `verify_otp` and `resend_otp`, through Salla's KYC API. The code comes from Absher, Saudi Arabia's national identity platform ('Enter the OTP sent to your mobile registered in Absher'). Absher stays in `reading`, since the entries' own text doesn't name it, as the checker requires of a filler. The cell held only `shows`, from help articles. Its market dependence is S-02's kind of point: the check is the Saudi workflow's.
- **CM-AIA-004 gains `extension-point`,** and it stands. The onboarding task has the merchant link the store to Claude and ChatGPT and work on products by chat, through the cell's `salla-mcp`. It also says whom the assistant acts for, which the cell had found unstated.
- **CM-CHN-004 gains `extension-point`** by the app 'TikTok Pixel - Catalog', a third party's product named in its app's name (M-3), and it stands.
- **The store's subscriptions are page 1 of 5** (15 of its 61). The other pages aren't held. The apps they name are leads, and no capture is asked for them: they are one store's choices, and the App Store's own lists are read in SA-1.
- **New things, decided with every platform's:** Shipment receipt by another person (with SA-26's and ZD-11's), Recently Viewed Products, and تقييم جودة بيانات, the product page's data quality rating.
- **Cost:** 12.6 million tokens over 69 requests, about 156,000 an entry. Three cells change beyond SA-7's CM-ONB-004: CM-TRU-002, CM-AIA-004 and CM-CHN-004.
