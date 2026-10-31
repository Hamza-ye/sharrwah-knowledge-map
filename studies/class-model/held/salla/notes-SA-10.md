# Held pass, Salla, batch SA-10: notes

82 entries of `dashboard-app-routes` (items.jsonl lines 1384 to 1872: the apps ads-media, ads-meta, ads-snapchat, ads-tiktok, ads-utils, app-maker, app-notification and billing). Evidence at observed-sa@b0bd0b163.

**Placed:** 56 entries on capabilities, in 58 lines; 0 `new`; 26 `out`, in 13 lines. Two entries take two lines (79, `/billing`; 82, `/billing/control`); entries 15 to 28 share one `out` line. 71 lines in all.
- Every line supports `core`. No `shows`, `own-service`, `extension-point` or quality.
- Fillers: the ad platform the app is named for (`meta`, `snapchat`, `tiktok`), as SA-8 and SA-9 wrote them.
- Scope on 30 entries, all store gates read from the bundles:
  - `plan not basic` (7 to 10, 31 to 45, 61 to 65): the Meta, Snapchat and TikTok apps send a basic store to /billing, as the YouTube and Google apps do (SA-8, SA-9). Their breadcrumb labels sit outside that gate and carry no scope;
  - `billing-native` (80, 81): the billing app renders `/billing/subscriptions/*` and `/billing/invoices/*` only where `getFeatureState` gives the feature billing-native, CM-PLN-004's released flag.
- No CHANGES line: every line falls on a cell that already holds `core`.

Entry numbers below are the batch's order (`held_entries.py show --batch SA-10`). Bundles are cited by their record in `raw/runs/20261008T120306Z-dashboard-bundles-chunks1/fetch.warc.gz`: ads-media @13340475, ads-meta @15310651, ads-snapchat @17873096, ads-tiktok @21614063, ads-utils @23917517, app-maker @26246425, app-notification @26252311, billing @28487776 (`held_index.py`).

## How I read the entries

I kept SA-7's eight rules and SA-8's and SA-9's additions.
- **Rule 2, the place the cell cites:** every Salla Ads route here is CM-MKT-010's, whose cell cites ads-media, the Meta app at /marketing/ads/meta, and the Snapchat and TikTok apps; the app maker's routes are CM-CHN-006's (link /channel/mobile, app ui-merchant-app-maker); the app notification module's are CM-MKT-007's (its app, SA-S-3575); the billing app's are CM-PLN-004's (its app at /billing).
- **Every item of an entry's app and path** (the brief's known case, after SA-9's check): I listed each entry's items. Only entry 73 (`ui-merchant-app-notification`, `/`) holds a route among others: line 1864 (keys `element`), a redirect to /marketing/ads/app-notification-ads. It goes on CM-MKT-007 with its target. Its other items (1834, 1842, 1843) are cookie libraries' defaults. Every other `/` entry (1, 5, 29, 52, 66) holds cookie defaults only, and every `m@4@5l@4@11@9@11@9@5xe` entry (2, 6, 30, 53, 67, 74) two VML shapes only.
- **Breadcrumb labels** (rule 4) go where their route goes. Meta's and Snapchat's `/reports` labels title the reports routes they prefix. TikTok's `/reports/creative-list` has no route: the bundle's `ads-tiktok:overview-report.creative-list` puts it in the overview report, so it goes with the app's own thing, unsure.
- **Leads set aside as common words:** CM-CAT-007 (media: the ads' images and videos), CM-ANL-002, CM-ANL-003, CM-ANL-006 (a campaign's own reports), CM-MKT-001 and CM-MKT-003 (app promotion: an app-install objective), CM-PLN-001 for `/basic/*` (Snapchat's basic campaign mode, beside `/advance/*`), CM-PAY-026 (advance), CM-OPS-004 (tools: Snapchat's public profile tool), CM-CNT-007 and CM-SFR-010 (website traffic), CM-MKT-012 and CM-MKT-005 (a campaign's receipt), CM-MKT-008 (a sales objective, with no statement that orders are credited to it), CM-CHN-001 for `/channel/mobile/*` (Sales channels is the group the app maker sits under; publishing here is to the app stores), CM-PTN-004 (invoice: the partners' billing).

## Entries I couldn't tell, and what would settle each

- **15 to 28, Snapchat's lifestyle categories** ('scls:{id:' objects with a name, a path, a parentId and the source SNAPCHAT, in English and Arabic). `out`, as SA-8 placed the v2 ads apps' interest mappers: they are a third party's targeting list bundled as data, not routes. The selection's rule dropped the categories whose names hold a space; the one-word ones are entries. A lead for CM-MKT-011 (audiences), below.
- **39, `/basic/traffic/:id?`.** Its element is `appInstallPage`, the bundle's name for an app-install page, while `/advance/traffic/:id?` renders `WebsiteTrafficPage`. The names are minified, so this may be a reused component or a slip. Placed with the traffic objective on CM-MKT-010 either way.
- **71, `/channel/mobile/reports`.** The store app's reports. On the demo store it showed only 'Access restricted' (a staff gate), and its chunk `Reports-PWZ6eNNr.js` isn't held, so what it reports isn't stated. Placed on CM-CHN-006 only; CM-ANL-002 is the alternative. The chunk, or a run with the permission, would settle it.
- **79, `/billing`.** Two lines: CM-PLN-004 (the billing app's main route) and CM-PLN-001, since the route's own title is 'Store plan' (`billing.json`, `breadcrumb./billing`) and its page holds the current plan and, on a Basic store, the plans to upgrade to. CM-PLN-001's cell cites the settings link Store plan at /plan; whether /plan leads here isn't held.
- **80, `/billing/subscriptions/*`.** 'Add-on subscriptions'. Its page lists the plan's own subscription, and its empty state reads 'Run and grow your store with powerful apps.' (`billing.json`). Placed on CM-PLN-004 only. CM-APP-003 (app charges billed through the platform) is the alternative for a second line; a page listing an app's subscription would settle it.
- **82, `/billing/control`.** 'Account control'. Two lines: CM-PLN-004, and CM-PLN-002 for pausing the plan's subscription (the public demo's paused plan with 'Resume subscription', `20261009T022751Z-sweep-public-demo-en/steps/203.text.txt`; the locale's 'Pause for 30 days, available twice per year.'). The route's chunk (`index-5Nwog4rj.js`) isn't held, so whether it also holds the cancel and delete actions the locale lists under `settings` isn't shown.

## What a source or run step states that no entry holds (for the second stage)

- **CM-CHN-006, qualities and terms of App Maker** (`structures/salla/dashboard-translations/en/app-maker.json`; `20261008T133523Z-sweep-demo-store-en/steps/047.text.txt` and `197.text.txt`):
  - the setup fee: “I don't have developer accounts (setup fee: SAR 990)”; the price on the demo store '5739.12SAR', 'Annual', 'Monthly', and 'Try for free';
  - 'Additional fees apply to changes made after your app is published.', and an update price (`home.update_panel.price_suffix`);
  - 'Your store app will be published within 72 hours once all requirements are completed and the information provided is accurate and complete.', 'Review typically takes up to 4 days', 'Publishing your app may take 2 weeks to 1 month if you do not already have developer accounts.';
  - 'A custom domain is required to subscribe to App Maker.' (a link to the domain cells);
  - the developer accounts' fees paid to Apple (USD 99 a year) and Google (USD 25 once), and 'The Salla team will need access to complete publishing.' (`form.apple_id.tooltip_description`, `form.gmail.tooltip_description`);
  - 'Transfer your app to your App Store account to continue renewing your App Maker subscription.' (`home.account_warning.description`), beside the cell's apps held on Salla's own store accounts (SA-S-5035).
- **CM-PLN-001, CM-PLN-002, CM-PLN-004** (`/billing` and the billing locale, `billing.json`):
  - the merchant store's plan cards: 'Pay annually with installment options', 'Get a free custom domain with an annual plan', 'Salla Plus' 'Starting at' '99', 'Salla Pro' '299', and 'Starter Package for Offline Stores - Pro' at 599 a month (`20261008T141131Z-sweep-merchant-en/steps/205.text.txt`), prices and a bundle offer;
  - the Support Plan: 'If you’re not ready to sell yet, you can continue setting up your store at a lower cost with the Support Plan.' and its special price until the first orders (`support_plans.*`);
  - 'Plan pricing differs between the Salla app and the website' (`mobile_pricing_basic`);
  - cancelling: 'If you cancel, your store will switch to the free Salla Basic plan. No charges will apply, and the free trial can’t be used again on this account.' (`subscription_actions.cancel_subscription_desc_free_trial`); the pause: 'Pausing the subscription will temporarily disable plan features for up to 30 days.' (`settings.control.desc`), a quality for CM-PLN-002.
- **CM-PLN-005:** a subscription's 'Payment Schedule' in instalments (`subscriptions.installment.*`), and the store's bank transfer requests among its invoices ('Bank transfers', `invoices.bank_transfers.*`): means of paying Salla's bills.
- **CM-PLN-007:** the store's 'Tax invoices' from Salla (`breadcrumb./billing/invoices/vat-invoices`; `20261008T133523Z-sweep-demo-store-en/steps/205.text.txt`). The cell holds only a `shows` row for VAT on Salla's fees; these invoices are a lead for it.
- **CM-ONB-002, CM-TRU-016:** 'Delete store', 'The store will be permanently deleted and cannot be restored.' (`settings.link_delete_subscription.*`).
- **The add-ons Salla sells on /billing** ('Add-ons', `20261008T133523Z-sweep-demo-store-en/steps/203.text.txt`): 'Warehouses & branches' (CM-INV-005), 'Staff accounts', 'Add extra staff accounts to help manage your store.' (CM-STF-001), SMS messages (CM-NTF-004), 'Instant translation', 'Add translation characters to translate your store instantly into 40+ languages.' (CM-MKS-008); 'Gift a Salla plan', 'Help your loved ones grow their business with a monthly or annual Salla plan.' (CM-PLN-001); the app subscriptions (CM-APP-003); 'Cancel the service and refund the remaining balance for messages, sender name, and domain.' (`settings.link_cancel_subscription.desc`).
- **CM-MKT-022:** the app-notification campaign on the demo store is an abandoned-cart engagement: 'Engagement Condition', 'Duration of abandoned cart', 'Objective', 'Abandoned Carts' (`20261008T133523Z-sweep-demo-store-en/steps/195.text.txt`, `201.text.txt`).
- **CM-MKT-011:** Snapchat's lifestyle categories bundled for targeting (entries 15 to 28, bundle @17873096), beside SA-8's `IN_MARKET` and `AFFINITY` interests.
- **CM-MKT-010:** the media library's limits, 'Please upload images under 30 MB to ensure a successful upload.', 'Please upload videos under 100 MB to ensure a successful upload.' and its restricted content (`ads-media.json`); the Meta app's 'Add funds to your Sweply Ads wallet.' and 'Monthly Invoice' (`ads-meta.json`), as the cell's Sweply rows.

## A structure whose items and sources disagree

None. One observation: the TikTok bundle is a development build. Its routes are `jsxDEV` calls carrying their source file, such as `/home/runner/_work/ui-merchant-ads-tiktok/ui-merchant-ads-tiktok/src/App.tsx` with its line numbers (bundle @21614063). docs/GAPS.md says Salla serves no source maps for its modules; this one bundle names its own source files and components.

## Problems with the brief or the script

- None new. The checker's container NOTEs (`reports`, `channel/mobile`, `billing`) fire on paths that prefix their app's other routes; each is placed on the capability of its children, as SA-7 placed containers by path.

## The coordinator's check (30 October 2026, after the batch)

- **Every entry's items were listed,** by the brief's new known case. Only entry 73's app and path hold a route among other objects, and its line follows the route. `ads-utils`' `/` holds no route among its four objects, so it stays `out`.
- **The served module is `core` and the unserved one `shows`.** The app-notification module v0.10.1, which the registry serves, is `core` on CM-MKT-007. SA-9's v0.4.0, which it doesn't serve, stays `shows`.
- **The billing routes stand** on CM-PLN-004, with the plan's own lines on CM-PLN-001 and CM-PLN-002. So do the store gates as scope: `plan not basic` and `billing-native`.
- **Cost:** 12.8 million tokens over 67 requests, about 156,000 an entry. No cell changes.
