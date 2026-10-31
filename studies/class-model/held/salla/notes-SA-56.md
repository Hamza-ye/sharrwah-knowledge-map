# Held pass, Salla, batch SA-56: notes

55 entries (effort high), evidence at observed-sa@b0bd0b16, all of `settings-center` as rebuilt after SA-50 (one entry per node, every store's answer in it, with `if:`). This is the structure's last batch. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-56`). Eight sub-pages and one section:
- 1 to 10, the Customer wallet section's Gift cards (`/wallet/gift-card`); 11 to 21, its Wallet & Cashback Notifications (`/wallet/notifications`);
- 22 to 32, the section Markets (`/markets`);
- 33 to 39, the Orders section's Order confirmation page (`/orders/processing/order-confirmation-page`);
- 40 to 49, the Domain section's Connect external domain (40, 41), Register custom domain (42 to 44), Renew domain (45 to 47) and Transfer domain (48, 49);
- 50 to 55, the real store's Product display in store (`/products/products.product_quantity`), the twins of SA-54's 50 to 54 with the extra item `hide_out_of_stock_products` (53).

**Which stores' answers hold each body** (sha256 of `<label>/<section>.json` compared):
- the two wallet pages, the same bytes on all five labels (gift-card `7d0d525f…`, notifications `ebcda1b3…`);
- Markets, `17d36b6c…` on `demo@en`, `merchant@en` and `real-merchant@en`; the other two labels hold no answer;
- Order confirmation page, `2204241f…` on four labels; `demo@en` holds none;
- the four domains sub-pages, `real-merchant@en` only;
- Product display in store, the real store's `c5725714…` (the other four stores' `ebb14cff…` is SA-54's).

The entries' labels match these files.

**Placed:** 53 entries on capabilities, none `new`, 2 `out`, in 77 lines: 63 `core`, 12 `shows`, 2 `out`. No `own-service`, `extension-point` or `outside`, no filler.
- Lines by capability: CM-NTF-001 11, CM-MKS-001 11, CM-SFR-008 10, CM-LOY-002 9, CM-LOY-001 9, CM-ORD-010 7, CM-SFR-015 6, CM-LOY-003 5, CM-B2B-003 2, and one each on CM-MKS-004, CM-CHN-006, CM-MKS-007, CM-CHK-001 and CM-TAX-001.
- `shows`: every line of Gift cards, which is behind `wallet-gift-card`, released on no held store (10 lines, 1 to 9). Also the real store's extra item behind `hide-out-of-stock-products`, released on no held store (53), and the domain form's tag 'Required for markets' on CM-MKS-001 (41).
- Scope on 52 lines: `customer-wallet` (24), `multi-countries-advanced` (17), `wallet-gift-card` (10), `hide-out-of-stock-products` (1). The order confirmation page and the domains sub-pages name no gate on the store.
- Three qualities:
  - the countries a market may have under tax by market country (32);
  - the domain transfer's duration and its two 60-day conditions (49);
  - the remaining-quantity threshold, taken from SA-54 (55).
- **The checker prints no `CHANGES` line: no cell changes.**

**Sources read:**
- **The brief and what it names:** the evidence map; observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`; the register's row for `settings-center`; `index/ledger-summary.tsv`; the selection rows.
- **The model's rules:** B-extent's "Cells and evidence" and its conventions; the rulings to their last section.
- **The earlier batches:** SA-48's to SA-54's notes, with their rules S1 to S12, R1 to R9, T1 to T8, U1 to U8, V1 to V8, W1 to W8 and X1 to X4, and the coordinator's checks. Also SA-54's lines for Product display in store, and the earlier lines `held_entries.py earlier` named: SA-33's plan gates of the same addresses; SA-48's, SA-49's, SA-50's and SA-53's items and sub-pages.
- **The bodies.** I printed each of the nine bodies once as a tree of its nodes, with the `if`s above them, and read code only where an entry left a column open:
  - 3, 10, 13, 35 and 51: which lists one entry stands for;
  - 2 and 5 to 9: the gift card page's conditions;
  - 14: where the channels come from;
  - 15 and 18: the lists' titles;
  - 16 and 20: their `if` on the channels;
  - 22: `feature` and `featureMeta`;
  - 24: the two lists;
  - 40 to 49: `permissionMeta` and the queries;
  - 53: its `features` and `hidden`.
  A grep for store gates found none in the order confirmation page or the domains bodies.
- **To clarify only, each cited where a line rests on it:**
  - `dashboard-features/*@en/items.jsonl` for `wallet-gift-card` (demo line 538), `customer-wallet` (187), `multi-countries-advanced` (568) and `hide-out-of-stock-products` (real store's line 524), with the other stores' lines;
  - `dashboard-translations/{en,ar}/settings.json`, for the quotes and the keys no body uses (below);
  - the Pro store's Gift cards and Wallet notifications pages (`20261009T033607Z-sweep-settings-demo-en/steps/074.text.txt`, `075.text.txt`), and that run's answer to the channels request (`responses/4567.json`, at its step 75);
  - the Basic and Pro stores' Markets pages (`20261009T041819Z-sweep-markets-merchant-en/steps/001.text.txt`; `20261008T180430Z-journey-localization-demo/steps/015.text.txt`);
  - the real store's Product display page (`20261012T010906Z-sweep-real-merchant-full-en/steps/338.text.txt`);
  - for the markets items' second lines, the model's cells and `merged/interfaces.tsv`, which name the statements CM-B2B-003 and CM-MKS-007 cite (S02-SA-082, S02-SA-078, SA-S-0117).
- **Entries whose capability, support or scope the entry's text left open,** so that I read the body or a run page: 1 to 10 (scope), 13, 14, 22, 24, 41, 43, 53 and 55.

## The rules: S1 to S12 and R1 to X4, kept, and what I added where they don't reach

I kept the earlier rules as the coordinator's checks and rulings left them:
- S1 for each sub-page: the item that opens it, and the concern map's keys SA-S-1767, SA-S-1768, SA-S-1769, SA-S-1735 and SA-S-1730;
- S7, R5 and U2 for the forms and lists, with U2's several capabilities where a page is itself several things (Wallet & Cashback Notifications, as SA-50 placed its item on CM-LOY-001, CM-LOY-003 and CM-NTF-001);
- T1 and W7 for the sections' `features` and `feature.flagKey`;
- S4 for the released and unreleased flags;
- S2's second exception for the titled lists (15, 18, 47);
- V7 for the Save lists whose label is an unresolved array (35, 51); U2 for the one whose label is a string (10, `out`);
- S5 for what a setting is set by (the order statuses and payment methods of 36 to 39, the channels of 14);
- X4 and SA-54's lines for the real store's Product display.

SA-55 ran beside this batch, and its notes and the coordinator's check were committed while I worked. The check says 'Y1 to Y8 stand for SA-56', so I read them against my entries:
- **Y2** ('A sub-page's own section node governs its gate') is the rule I had reached for Gift cards (Z1 below). So Z1 is Y2's case, with a gate of the page's own in place of none.
- **Y1** (an option's description or disabled state under a store feature) has no case here. The bodies hold no `useFeature` or other store gate on an option. The wallet channels' disabled state comes from the page's own request (Z3).
- **Y4** (a cell that cites the entry's own statement): `class_slice.py search` on my sub-pages' keys and labels found only the statements the lines cite (SA-S-1767, SA-S-0157). It also found three inventory entries that no cell cites: SA-I-0735, SA-I-0768 and SA-I-2623.
- **Y5:** 55's threshold is already a quality, and 19's day, week and month aren't amounts.
- **Y3, Y6, Y7 and Y8** have no case here.

For the coordinator to align, I added these, named Z, since SA-55 used Y:
- **Z1. A sub-page whose own answer names a gate other than its parent section's.** Gift cards names `features: [wallet-gift-card]`. The item that opens it sits in the wallet section, behind `customer-wallet`.
  - I took the sub-page's own gate as the scope of its nodes (1 to 9), as SA-55's Y2 does for `/wallet/max-credit-usage`, which names none. The parent's gate is a gate over another answer's nodes, so it goes in `reading`.
  - The loyalty and gifting sub-pages name their own features too (SA-53's `loyalty-system`, `loyalty-system;multi-countries`).
  - If the coordinator reads a section's gate as over its sub-pages, the scope is `customer-wallet and wallet-gift-card` (the ruling after SA-53).
  - SA-50's `customer-wallet;wallet-gift-card` on the item (SA-E-98767fb7) is the item's own case, inside the wallet section. Under the ruling after SA-53 it would be written `customer-wallet and wallet-gift-card`: as it stands, it reads as alternatives.
  - No support changes: `wallet-gift-card` isn't released anywhere.
- **Z2. A notices page that is the wallet's own settings** (11 to 21). The section and the form take the page's three capabilities: CM-LOY-001, CM-LOY-003 and CM-NTF-001, as SA-50's item has them (the ruling after SA-19).
  - Each list and template takes the capability of the notice it is: the cashback credit's message is CM-LOY-003 (15 to 17), and the wallet balance's expiry alert and status channels are CM-LOY-001 (14, 18 to 21).
  - Each also takes CM-NTF-001, since it is a template or setting of the store's automatic messages to customers. That is CM-NTF-001's own description: 'with their settings and templates'. SA-48 placed the order status notifications' channels there.
  - This differs from U1 as the coordinator corrected it, where a staff notice's subject took no line. There the notice was CM-NTF-002's own thing and the subject was named in passing. Here the page is the wallet's own settings route (SA-S-1768), so the notice's subject is the page's capability.
  - The message variables (`{cashback_amount}` and the others) are a list named in passing (the ruling after SA-41). So 21's cashback amount takes no CM-LOY-003 line.
- **Z3. A channel select whose options come from the page's own request, not from the body** (14). The body draws a checkbox for each channel in the answer of `settings/fields/wallet.cashback_notifications`. The Pro store's answer lists `email`, `mobile` (disabled: 'Publish a mobile app with App Maker first.') and `sms` (disabled: 'You must connect one of the SMS apps first', linking to apps.salla.sa) (`raw/runs/20261009T033607Z-sweep-settings-demo-en/responses/4567.json`).
  - I read the answer only to clarify the setting's input. The App Store requirement is stated only there, so it isn't placed (M-12): unlike V4 and SA-54's 77, where the body's own option states it.
  - If the coordinator reads the answer as the entry's, 14 takes an `extension-point` line on CM-NTF-004, with no filler. CM-NTF-004 is `extension-point` already.
- **Z4. A feature card in a section's `featureMeta`** (22, Markets). The card's words are the section's own, on its line: 'Multi-market', 'Start creating new markets and selling in multiple countries.', the button 'Activate' (defined `disabled: true`) and 'Contact your account manager to enable this feature.'.
  - The flag `multi-countries-advanced` is released (plans special) and enabled on no held store. So the section and every node inside it are `core`, scope `multi-countries-advanced` (S4, W7), as SA-53 placed Market selection's markets version. Every held store's page shows only the card.
  - The account manager is named as the way to the feature, so it goes in `reading`, not on a line on CM-ONB-003.
  - If the coordinator reads the disabled button under 'Contact your account manager' as an offer stated unavailable where it is listed (the ruling after WC-5), 22 and 24 to 32 become `shows`. I didn't: the words say how the feature is enabled, not that it can't be. A lead, in the repository's own words, not Salla's: observed-sa's `docs/GAPS.md` says the public demo, badged Special, offered 'Create your first market' (run `20261028T155312Z-journey-markets-public-demo-en`).
- **Z5. A link item to a sub-page that no answer holds** (27 to 30: `default_scope`, `auto_show_products_in_scope`, `show_scopes_in_app`, `product_prices`).
  - The item goes on the section's capability by its own words (S7).
  - It also goes on each capability whose cell already cites the sub-page's own keys, or names its thing (rule 2; the ruling after SA-19):
    - 28 takes CM-B2B-003 (S02-SA-082 cites `markets#auto_show_products_in_scope.description`);
    - 29 takes CM-CHN-006 (its released flag `store-app-scopes`; T6);
    - 30 takes CM-B2B-003 (S02-SA-078, `markets/product_prices#option.fixed.description`) and CM-MKS-007 (SA-S-0117, `#option.auto.description`, and its note names the page).
  - 27, the dashboard's default market, takes CM-MKS-001 alone. No capability holds the admin's own view (the ruling after SH-37 on the admin's frame).
- **Z6. A page's own search box** (43, the domain register page's header): the domain availability search, the page's own function, on CM-SFR-008 `core`. S8's `out` is for a header that searches the settings. If the coordinator reads every `s:header` with a search box as S8's, 43 is `out`, and no cell changes.
- **Z7. A tag in a form that states another capability's requirement** (41's 'Required for markets' / 'مطلوب للأسواق المتعددة' on the nameserver option). It is `shows` on the capability the tag names, CM-MKS-001: a condition stated, not a setting of markets. It bears on a market's subdomain, which CM-MKS-004's cell holds (S02-SA-052), so CM-MKS-004 would do as well. Either cell is `core` already.
- **Z8. A staff permission's card text on a sub-page.** The four domains sub-pages show `permissionMeta`'s 'Manage store domain' and 'Set up and manage your store’s domain and DNS settings.', the card a staff member without `domain_management` sees.
  - I read it as a gate on the user, in `reading` (S3).
  - SA-49 read the same words on the Domain section as the section's own, and gave the section a CM-SFR-009 line (SA-E-2f51bb9b). The sub-pages' own descriptions narrow them to linking, registering, renewing and transferring, so they take no CM-SFR-009 line.
  - 41's DNS records are changed at the domain provider, not managed from Salla.
  - If the coordinator follows SA-49, 40, 42, 45 and 48 each take a CM-SFR-009 `core` line. CM-SFR-009 is `core` already.
- **Z9. Qualities from what a page states as a requirement or a duration:**
  - the transfer's 'usually 7 to 10 days' and its two 60-day conditions (49);
  - tax by market country's 'one country only' per market (32), on the CM-TAX-001 line, since it is the condition of that setting, not of markets in general.

  A check that a value is above zero isn't a limit the platform sets, so it takes no quality (8).
- **Z10. An item whose `features` the rendering leaves out** (53). The real store's body gives `hide_out_of_stock_products` the `features` `{flagKey: hide-out-of-stock-products, released: true}`, which the entry doesn't render. The body governs, so the feature is its scope (S4).
  - The store's features list has the flag `released: false`, with no plans, on all four held stores. The list is the store's answer and governs, as SA-54's notes said, so the line is `shows`.
  - Its label and description keys resolve nowhere in the held translations. So its term is its id, as S9 allows.

## `new` things

None. Each entry's thing is already a capability's: the sub-pages by the concern map's settings keys and the items earlier batches placed, and the settings by the capability of what they set. Searched with `caps --terms`, besides the leads:
- subdomain, دومين فرعي, النطاق الفرعي, redirect;
- default market, السوق الرئيسي, السوق الافتراضي, dashboard market, admin market, market switcher, default scope, store scopes;
- restrict purchases, تقييد, حصر, country restriction, restrict sales, restrict checkout, block checkout, delivery address, عنوان التوصيل, sell to, ship to;
- tax by country, الضريبة حسب الدولة, market tax, tax per country, tax region, tax zone, market country, دولة السوق;
- account manager, مدير حساب; auto-assign; store app, تطبيق المتجر, App Maker;
- deferred payment, مهلة للدفع, payment period, pay later.

The searches found CM-MKS-004, CM-CHN-006 and CM-TAX-001, which I placed, and CM-PAY-015, which I set aside. CM-PAY-015 (buy now, pay later) matched 'deferred payment'. Salla's word for the bank transfer's payment period is the same ('مهلة الدفع', SA-48's SA-E-8190f0b7 on CM-PAY-030), so 37 names that in its reading, not CM-PAY-015.

## The `CHANGES` lines

None.

## Entries I couldn't tell, and what would settle each

- **1 to 9, the scope:** `wallet-gift-card` alone, as Y2 has it, or `customer-wallet and wallet-gift-card` (Z1). The coordinator's reading of a section's gate over a sub-page that names a gate of its own settles it. No support changes.
- **13, the list holding only the channels:**
  - I made it a container on its setting's two capabilities (U2).
  - SA-49's R4 had a list whose one item is on two capabilities `out` (its 83).
  - The coordinator's choice between R4 and U2 for a sub-page settles it. No cell changes.
- **14, the SMS app requirement:** in the notes only (Z3), or an `extension-point` line on CM-NTF-004. Whether a page's own request's answer counts as the entry's settles it.
- **22 and 24 to 32, `core` or `shows`** (Z4). The ruling after WC-5, read against 'Contact your account manager to enable this feature.', settles it. A store with the feature on would show the settings themselves.
- **25, Domain redirection:** CM-MKS-004 `core` (a market's subdomain falling back to the main domain), not CM-CNT-009, URL redirects, whose Salla cell holds nothing.
  - CM-CNT-009's note is a merchant's own redirects between the store's links (Zid's feature, for a store moving platforms).
  - This toggle is the markets' domains' fallback.
  - If the coordinator reads 'redirected' as CM-CNT-009's thing, 25 takes a CM-CNT-009 `core` line, and that cell would become held: a `CHANGES` line.
- **30, three lines:** CM-MKS-007 rests on the sub-page's own option (SA-S-0117), which the item opens but doesn't name. If the coordinator keeps the ruling after SA-19 to pages a held answer draws, 30 keeps CM-MKS-001 and CM-B2B-003. CM-B2B-003's cell cites the page's other option (S02-SA-078). No cell changes.
- **31, Restrict purchases by market:** CM-CHK-001 for the blocked checkout, not CM-MKS-004. The restriction is by the delivery address, not by where the visitor is. No cell changes either way.
- **32's quality:** on the CM-TAX-001 line (Z9), or the CM-MKS-001 line.
- **37, 'deferred payment':** read as the bank transfer's payment period, in `reading` only, as a condition the message is shown under (S5). A help article on the order confirmation page would settle which payment it means.
- **41, 'Required for markets':** CM-MKS-001 `shows` (Z7), or CM-MKS-004 `shows`, or no line if the coordinator reads the tag as named in passing.
- **43, the register page's search:** `core` (Z6) or `out` (S8).
- **40, 42, 45 and 48, CM-SFR-009:** no line (Z8), or a `core` line each, as SA-49 placed the Domain section.
- **53, `shows`:** the store's features list against the item's own `released: true` (Z10). A store whose list releases `hide-out-of-stock-products` would settle it.

## A structure whose items and sources disagree

- **14's id renders as a translation,** 'id: Sales channels (قنوات البيع) [channels]'. The body's id is `channels`, which the build resolves as the settings translations' key `channels`. It is cosmetic, as SA-54's 77 was. It makes `show` lead to CM-CHN-001, which is no lead.
- **53's `features`** (`flagKey: hide-out-of-stock-products, released: true`) and its `hidden` condition aren't rendered. Its label and description render as keys, since no held translation holds them. The body governs (Z10).
- **22's `feature.defaultValue`, `featureMeta` (the button's `disabled: true`, the help article's address) and `permissionMeta`** aren't rendered. The entry gives the card's texts under `shows`, which reads as if they were the section's settings.
- **40, 42, 45 and 48** render `permissionMeta`'s title and description among the page's texts. They are the permission's card (Z8).
- **The gift card page's queries:** its form reads the wallet's own settings (`$walletSettings`, `settings/wallet`) beside its own, and saves a `product_id` with the card (`initialValues`). No entry holds either. It is a lead on how Salla keeps a gift card: as a product.

## For the second stage: what the sources state that no entry holds

Keys of `structures/salla/dashboard-translations/{en,ar}/settings.json` that no settings body uses:
- **`wallet/gift-card#image.size_limit`:** 'Supported formats: JPG, JPEG, PNG. Maximum size: 2 MB.' / 'الصيغ المدعومة: JPEG، JPG ،PNG حتى 2 ميجابايت'. Also `#image.description`, 'Add an image for the gift card.', and `#amounts.currency`, 'SAR' / 'ر.س'. These are the strings of the components GiftCardImageUploader and GiftCardValues: a quality for CM-LOY-002, behind an unreleased feature.
- **`wallet/notifications#channels.whatsapp`** ('WhatsApp'), `#channels.sms_install` ('Install the SMS app to enable this channel.') and `#channels.whatsapp_install` ('Install the WhatsApp app to enable this channel.'). These are a lead for CM-NTF-004's `extension-point`, as is the Pro store's answer (Z3).
- **`wallet/notifications#cashback.description`** ('The message sent to the customer when cashback credit is added to their wallet.') and `#expiry.description` ('The message sent to the customer before their wallet balance expires.'). Also `#cashback.message_desc`, `#expiry.message_desc`, the two `#…variables_hint` and `#variables.*`: an older set of message variables (`{cashback_credit}`, `{wallet_credit}`, `{wallet_expire}`).
- **The four markets sub-pages no answer holds:**
  - `markets/default_scope#field.*`: 'Default market', with the option 'All';
  - `markets/auto_show_products_in_scope#field.*`: 'Default markets for new products';
  - `markets/show_scopes_in_app#field.*`;
  - `markets/product_prices#type.*` and `#option.*`: 'Pricing method'; 'Automatic pricing by exchange rate', 'Custom price per market', 'Set product prices manually for each market from the product page.'.

  Their answers would hold the pages' own settings. A lead for CM-B2B-003 and CM-MKS-007, read by the subjects already.
- **`domains#register.price-info`:** 'Register this domain for {{currency}} {{price}} per year'. Also `#register.price-free` ('Free'), `#transfer.price-error` ('Unable to load transfer pricing. Please try again.') and `#transfer.modal-title` ('Transfer domain to Salla'). The register, renew and transfer pages each read a price by a request (`settings/domain/price/…`) whose answer the structure doesn't hold. A price per year is a quality for CM-SFR-008. SA-49 listed `domains#*` for the second stage too.

Run pages and answers:
- `raw/runs/20261009T033607Z-sweep-settings-demo-en/responses/4567.json`: the wallet notices' `channels_config`, as in Z3, and the store's own default titles and messages.
- `20261009T033607Z-sweep-settings-demo-en/steps/075.text.txt`, lines 154 to 195: the Pro store's default cashback and expiry messages, among them an expiry title with `{days_left}`, a variable the form's description doesn't list. This is store data.
- `domains~link.json`'s help article `https://help.salla.sa/article/139992612` ('Learn more'), on the nameserver and CNAME methods, and `markets.json`'s `featureMeta.articleUrl`, the help centre's Markets subcategory. They are a lead for whether a market needs the nameserver connection (Z7).

## Leads set aside as no leads

- **By a permission's name:** CM-ORD-001 and CM-PAY-020 (`order_management`, 33); CM-MKS-006 (`domain_management`, 40, 42, 45, 48).
- **By a common word:**
  - CM-PAY-024 (by cards), CM-PAY-032 (by link), CM-CHK-008 (by buy), CM-API-013, CM-PAY-014, CM-PAY-021, CM-ORD-004 (by cancel), CM-API-003 (by write), CM-AIA-003 (by description), CM-ACC-001 (by your store);
  - CM-API-009 (by notifications), CM-NTF-002, CM-MKT-020 (by wallet, balance), CM-ORD-015, CM-CUS-001, CM-SHP-017, CM-RET-002 (by amount, credit);
  - CM-LOY-004 (by markets), CM-EVO-001 (by enable, feature), CM-INV-010, CM-B2B-001, CM-MKT-016, CM-ACC-008, CM-OPS-001, CM-APP-002, CM-API-004, CM-SHP-014, CM-B2B-002;
  - CM-CNT-003 (by page), CM-CHK-009, CM-PAY-029 and CM-PAY-008 (by order, payment);
  - CM-CHN-003 (by connect, external), CM-APP-008, CM-SHP-015 (by خاص, ربط), CM-SFR-013 (by search), CM-PLN-002 (by تجديد), CM-API-008, CM-INV-006 (by transfer), CM-PAY-003, CM-ORD-003 (49, by can);
  - CM-CAT-001 (by المنتجات), CM-TRU-005, CM-INV-004.
- **Named only as an input or a condition:** CM-ORD-003 (the statuses of 36 to 39); CM-PAY-016 and CM-PAY-030 (the bank transfer and cash on delivery of 37, 38); CM-CHK-001 (36, 'after checkout': the confirmation page is CM-ORD-010's, as SA-48 placed its item); CM-NTF-001 (34 to 39, by 'order confirmation'); CM-SFR-015 (30, by how, product).
- **Kept apart by a note:** CM-LOY-006, gifting, for the gift card's 'send to others' (CM-LOY-002's note keeps gift cards apart from gifting); CM-SFR-009 (Z8); CM-CNT-009 (25, above).
- **Kept to SA-54's reading:** CM-INV-001 for 54 and 55 (X4).
- **No lead:** CM-CHN-001 (the build fault on 14).

## The checker's lines, read again

- **No `CHANGES` line and no `NEW` line.**
- **The 'holds other entries: a container' notes:** each is a section or a form I placed as a container on its page's capability (1, 2, 11, 12, 22, 33, 34, 40, 42, 45, 46, 48, 50).
- **One quote note, fixed.** The checker read the typographic apostrophe in 'isn’t' inside 25's quote as the quote's end. I now quote only the words after it. The same mark inside 'store’s' passed.

## Problems with the brief or the script

- **This batch's placements file is already in a commit, which I didn't make.** Commit `eb95fae6`, 'Held pass SA-55 at high…' (06:01:55), adds `notes-SA-55.md` and `placements-SA-56.tsv`, my file as it stood after my last rebuild. It matches the working tree. SA-55's own placements were committed earlier, with the running agents' placements (`b86ce2a4`). So this reads as the same practice, my file taken as written so far. `notes-SA-56.md` is uncommitted.
- **The checker's quote pattern splits a quote at the typographic apostrophe of 'isn’t',** but not of 'store’s' (above).
- **The rendering leaves out:**
  - an item's `features` where the item has no `href` (53);
  - a section's `featureMeta` and `permissionMeta`, and `feature.defaultValue` (22, 40, 42, 45, 48).

  These are the same kind of gap V1 and U4 found for `getFeatureState`.
- **No other problem.** Most entries carried their sections' `features` and `flag:`, and the bodies were needed for the lists and the few columns above.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes and no new things.** `settings-center` is now placed whole, from SA-48 to SA-56.
- **Z1 to Z10 stand.**
  - **Z1:** the gift cards' sub-page takes its own gate, `wallet-gift-card`, alone (Y2). SA-50's item in the Wallet section, which sits under both gates, now reads `customer-wallet and wallet-gift-card`.
  - **Z4:** Markets stays `core` under `multi-countries-advanced`. The disabled Activate button says to contact the account manager, which is an offer on request, not one stated unavailable.
  - **25:** domain redirection stays on CM-MKS-004.
- **The nested gates in SA-50 to SA-53 are rewritten with ` and `,** 23 lines, by the ruling after SA-56.
- **SA-54's product display lines** are taken for the real store's twins (50 to 55). The extra `hide_out_of_stock_products` is `shows`, since the features list, which governs, has it unreleased.
- **Cost:** 26.5 million tokens over 111 requests, about 482,000 an entry: a short batch of complex pages.
