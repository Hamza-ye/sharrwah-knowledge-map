# H-005: Salla's multiple markets, switched on and set up

**Repository:** observed-sa. **Instrument:** a store whose plan includes multiple markets (الأسواق المتعددة). First look at the real merchant store (dandye-dandy-ksa, Pro: `docs/PLAN.md`, item 5), then the demo store (store-sherawya, Pro).

**What to capture:**
1. Settings > Markets, and Products > الأسواق المتعددة: whether "Activate" is enabled on the store's plan.
2. If it is: activate, then create a market for a country other than the store's own, and record each settings section as it shows it: currency, domain, prices, shipping options and design, and how a buyer's market is chosen. Stop before anything that charges.
3. If it isn't: record what the page says is needed.

**Extended on 27 October 2026** by gap-closing (phase A2), with five gaps on what a market takes. With a second market set up (step 2), record whether each of these offers a choice of market, as the customers' login methods do (`customers/login_methods#market`; `studies/subjects/S-02/salla/statements.tsv`, S02-SA-085), or holds one value for the whole store:

4. The informational page of type return policy (الصفحات التعريفية, سياسة الاستبدال والاسترجاع) and the order cancellation setting (Settings > Orders, `orders#order-cancellation`) (gap S02-SA-G06).
5. The settings of the installed Google Analytics and Google Tag Manager apps (التطبيقات المثبتة > إعدادات التطبيق), and a market's own settings: whether either takes a data stream, a container or an ad pixel per market (S02-SA-G08).
6. Any other installed app's settings: whether they take a value per market (the second half of S02-SA-G09).
7. The notifications settings (`/?settings=/notifications`): whether a notification or its channel takes a value per market (S02-SA-G10).
8. The storefront of the second market: the storefront settings answer (`GET api.salla.dev/store/v1/store/settings`), with its `store_country` and `country`, beside the same answer on the store's own market (S02-SA-G11). Held: one store country per store, and the same two values on one market's storefront (S02-SA-292, S02-SA-430).

**Stop before** anything that charges, publishes a change to a live store's buyers, or can't be undone. On the real merchant store, read only, and activate nothing without its owner's leave.

**Already held:**
- Settings > Markets on the Basic merchant store, Activate shown (run `20261009T041819Z-sweep-markets-merchant-en`);
- multi-location switched on at the demo store, where Settings > Markets kept Activate disabled (run `20261008T165800Z-journey-localization-demo`; `docs/GAPS.md`, the row on Multi Market);
- the help articles on multiple markets, which say the feature is on Salla's Special plan.

**Why:** S-02, root decisions 2 and 3: what a market a store sells into is, and which settings take a value per market, as the dashboard shows them, beside what the help articles state. Steps 4 to 8 answer gaps S02-SA-G06, S02-SA-G08, S02-SA-G09, S02-SA-G10 and S02-SA-G11 (`studies/subjects/S-02/salla/gaps.tsv`).

**Needs:** if no held store's plan opens it, a store on Salla's Special plan. That is a spending decision for the founder: what it costs, and that without it S-02 rests on Salla's help articles and the disabled page alone.

**Done when** a run holds the markets settings switched on and one market set up, with steps 4 to 8 on it, or shows what each held store's plan allows.
