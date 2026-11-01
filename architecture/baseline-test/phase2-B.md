# T-baseline, phase 2, part B: BT-4, BT-7 and BT-14

**What this is.** Part B of phase 2 of the baseline test (`studies/class-model/briefs/T-baseline.md`). It answers three of the 14 questions in phase 1 (`architecture/baseline-test.md`): BT-4, BT-7 and BT-14. The founder said go on 1 November 2026, with phase 1's questions as written. Three other parts answer the other eleven. For each question, in the brief's order:
1. Shopify's evidence;
2. whether that is enough for Sharrwah;
3. the other four platforms, only as far as the question needs them;
4. what no platform shows;
5. phase 1's expectations, checked.

**What I read.**
- The brief.
- Phase 1: its opening sections, its sections on these three questions, and its paragraph on which platforms each question needs.
- `CLAUDE.md`: its rules for an agent working from a brief, and for everyone.
- `founder-decisions.tsv`, at the lines phase 1 names for these questions: 16, 20, 25 and 26. They say what Sharrwah needs, never what a platform does.
- The evidence below, through each repository's own guides first (`README.md`, `docs/READING.md`, `structures/REGISTER.tsv`, `index/`), then `method/corpus_search.py`.
- The Yemen cases only as phase 1 records them. I opened none of their files.
- Nothing else in this repository, apart from the scripts I ran: `method/corpus_search.py`, `method/check_report.py` and `method/quote_check.py`, which the checker uses.

**The evidence, at its commits.**
- Shopify: observed-sh at `04de369da9ac84ae530ae80a55749167ff4139d4`. Its Help Center pages cited here are held from run `20261016T213535Z-help-en-ar-html-md` (16 October 2026).
- Salla: observed-sa at `b0bd0b16355f5a7de0358db4895f3e77c2e1fc96`.
- Zid, BigCommerce and WooCommerce: other-product-class at `0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4`, cited as `other-product-class@<commit>:<path>:<line>`. Its quotes stand on lines of their own here, and I checked them by script against the cited lines.
- This repository's `evidence/` at `9420f437cfe09065a2083e6a2a3a5f9c1127f99f`. It holds:
  - pages of shopify.dev captured on 11 October 2026;
  - pages of help.zid.sa and docs.zid.sa captured on 12 October 2026;
  - the cited files of the WooCommerce 11.2.1 release.

**How claims are marked.** As in phase 1:
- A fact carries its quote in double quotes, and its source at a commit.
- *(reading)* marks my reading. *(assumption)* marks what I take without evidence.
- A quote in Arabic is followed by my English rendering of it, which is a reading.
- *Not held* is never *doesn't do*. Where a platform is held too thinly to tell, I say so and name what I searched.

## In short

| Id | Shopify's shape, for Sharrwah | Other platforms' evidence needed to see it |
| --- | --- | --- |
| BT-4 | **Not enough**, in Yemen and wherever small providers won't build an app. The buyer's steps fit Shopify's payments extensions. Missing: a connection the platform itself runs for each seller's own account with a provider, that seller's credentials held by the platform apart from every other store's, and the provider's calls routed to the right store. Shopify fills its provider place only with apps that approved partners build and run. | Salla and Zid. BigCommerce added a detail. WooCommerce added nothing needed. |
| BT-7 | **Not enough** for sellers who can only send a payment, as I read most Yemeni sellers. Shopify charges a method it holds on file, bills in dollars in all of the founder's markets, and freezes a store 28 days after a failed charge. Missing: a bill that stays open until a payment the seller sends is confirmed, the payments reported against it with their states, and bills in the market's currency. Enough with a provider only where a market has a debit a provider can draw. | Salla and Zid. BigCommerce added nothing. |
| BT-14 | **Not enough under C, though the order shape is there.** Shopify's Product Network shows a checkout across stores: goods grouped by store, each store's own order, each store's own payment. But it rests on one processor, Shopify Payments, for every store. Missing: one checkout that runs each store's payment with that store's own provider, and a record of the basket's payments store by store, through partial failure. | Salla. Zid is held too thinly to tell. BigCommerce and WooCommerce added nothing. |

## BT-4. Local providers' payments, run by the platform for each seller

**The question,** as phase 1 asks it: can the platform itself run a local wallet's or bank's payment at checkout for each seller's own account with it (a phone number, then a one-time code or PIN), keeping each seller's credentials apart, where the provider offers only an API?

### Shopify's evidence

**Only an approved partner's app adds a provider.** From shopify.dev, captured on 11 October 2026:
- "Only approved Partners can build payments extensions on Shopify's Payments Platform." ([payments.md, L14](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt?plain=1#L14))
- "payments apps must be approved by Shopify" ([L87](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt?plain=1#L87))
- "Payments extensions must adhere to all Payments Partner requirements, including revenue share agreements." ([L89](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt?plain=1#L89))
- The scopes a payments app needs "are restricted scopes, and you need to apply for access" ([considerations.md, L26](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/122-shopify.dev/text.txt?plain=1#L26)).
- A merchant can build one for its own store only if it qualifies: "The option to build a custom payment extensions is limited to eligible Shopify Plus Merchants only." ([payments.md, L26](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt?plain=1#L26))

**The app, not Shopify, holds each merchant's settings with the provider.**
- "The merchant is redirected to the payments app page to configure the payments app settings." ([L44](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt?plain=1#L44))
- "The app marks itself as ready by calling the Shopify API." ([L46](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt?plain=1#L46))
- The Payments Apps API's `paymentsAppConfigure` "Configures the partner-managed payments gateway to work on the merchant's" store ([shopify.dev front matter, line 4654](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/docs-front-matter/shopify.dev@md/items.jsonl?plain=1#L4654)).

**The buyer's steps can run in checkout, on the app's page, or later.**
- Alternative payments extensions: "Partners can collect information directly on checkout and complete payment process with or without redirecting buyers to an app-hosted website." ([payments.md, L72](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/121-shopify.dev/text.txt?plain=1#L72))
- The Shopify CLI's template for an onsite payments extension declares fields for checkout, "extensions.checkout_payment_method_fields" ([shopify.extension.toml.liquid, L37](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-extension-template-files/github.com@Shopify-extensions-templates-main/files/extensions-templates-main/payments-app-extension-custom-onsite/shopify.extension.toml.liquid?plain=1#L37)). It also declares the countries the app is offered in: "country codes your app is available for installation by merchants" ([L14](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/cli-extension-template-files/github.com@Shopify-extensions-templates-main/files/extensions-templates-main/payments-app-extension-custom-onsite/shopify.extension.toml.liquid?plain=1#L14)).
- An app can leave a payment pending and settle it later: the Payments Apps API's mutations include "paymentSessionPending" and "paymentSessionRedirect" ([payments-apps schema 2026-10, line 26](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl?plain=1#L26)).

**The older shape, credentials typed into Shopify's admin, is being retired.**
- The Help Center still says, for a credit card provider, "Enter your account credentials for the provider that you selected." ([configuring-providers.md, L32](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md?plain=1#L32)), with "only one credit card payment provider activated at a time" ([L13](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md?plain=1#L13)).
- But "you must re-connect your payment account with your Shopify store by installing their payment app" ([updating-third-party-providers.md, L29](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/updating-third-party-providers.md?plain=1#L29)).
- For a provider without one: "If you're using a payment provider that doesn't offer an updated integration, then you must select a new payment provider." ([L8](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/updating-third-party-providers.md?plain=1#L8))
- ActiveMerchant, the way gateways were once built into Shopify, "is no longer used to integrate payment gateways with Shopify" ([configuring-providers.md, L170](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/configuring-providers.md?plain=1#L170)).

**Without an app, a provider can only be a manual method.**
- "Orders that accept manual payments are marked as unpaid on the Orders page. After you receive payment for a customer's order, you can mark the order as paid on the order details page" ([manual-payments.md, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments.md?plain=1#L10)).
- Shopify runs no provider's API for such a method *(reading)*.

**Shopify's own provider is offered in one of the founder's markets.**
- Its list of countries for Shopify Payments has "Shopify Payments for the United Arab Emirates" ([supported-countries.md, L52](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/supported-countries.md?plain=1#L52)). No other country of the founder's markets is on it, in lines 14 to 54.
- Elsewhere: "If your country isn't listed, or if Shopify Payments doesn't support your business category, then you need to use a third-party payment provider" ([L7](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/supported-countries.md?plain=1#L7)).

### Is it enough for Sharrwah?

**Not enough as it is, in Yemen.** By phase 1's assumption, the same holds wherever small local providers won't build an app for a platform: North Africa, Jordan, Lebanon, and the GCC's smaller providers.

**What fits.** The buyer's steps. A payments extension can ask for fields in checkout, redirect the buyer, and leave a payment pending until it is confirmed. That is the shape of the flow phase 1 records for Cash Pay and Floosak, from community-written clients: a phone number, then a code that the merchant's system sends back ([phase 1, BT-4's origin](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/architecture/baseline-test.md?plain=1#L106)) *(reading)*.

**What is missing:** who runs the connection, and where each seller's credentials live.
- **A connection the platform itself runs, per store and per provider.** In Shopify's shape, an approved partner builds the app, runs it, and onboards each merchant into it. The partner, not the platform, holds each merchant's settings. A provider that offers only an API, as phase 1 records Yemen's, gets no integration until someone builds and runs that app *(reading)*.
- **Each seller's credentials, held by the platform apart from every other store's,** with their rotation and removal. Phase 1 records them from community-written clients: at Cash Pay a username, a service-provider ID, an encrypted password and a certificate; at Floosak a phone, a short code, a wallet ID and a key.
- **The provider's calls into the platform, routed to the right store:** payment confirmations, refunds, and Kuraimi's verify-customer call, which a package page says the merchant hosts (phase 1, YK-138).

If Sharrwah built those apps itself, it would become the partner for every provider, and the connection would be the platform's own all the same. So this is a place in the platform's core, not a value filled into a place Shopify's shape has *(reading)*.

Where a market's provider does build an app, Shopify's shape is enough with that provider. Its Help Center says "Most payment providers have new integrations that you can easily connect to your Shopify account." ([updating-third-party-providers.md, L8](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/third-party-providers/updating-third-party-providers.md?plain=1#L8))

### The other platforms

**Salla (needed): the platform holds each merchant's credentials for the region's gateways itself.**
- Its dashboard's English strings hold a form titled "Gateway credentials", which says "Find the following details in your payment gateway account, then enter them in the corresponding fields." Its fields include "Secret key", "Public key" and "Merchant token" ([payments.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/payments.json?plain=1#L1)).
- The gateways it names include "HyperPay", "Moyasar", "PayTabs", "Tap", "stc pay", "Tabby", "Tamara" and "Emkan" ([payments.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/payments.json?plain=1#L1)).
- Its help on Moyasar: "you need the Secret Key from your Moyasar merchant account", then "Paste it into the Moyasar settings on the payment methods page of your Salla store." ([help, en, line 319](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/en/texts.jsonl?plain=1#L319))

**Salla also lets a merchant open its own account with a provider through Salla.** This has the shape of the case D16's default 1 counts as C: an account a seller requests through the platform but holds under its own agreement with the provider *(reading)*. Whether Salla is party to that agreement isn't in what I read.
- The merchant chooses between "I already have a {{name}} Business account" and "Open a Business account" ([payments.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/payments.json?plain=1#L1)).
- To open one: "By proceeding, you authorize Salla to share the required store information with {{name}} to create your account. Salla is not responsible for any services or actions provided by {{name}}." Then: "You'll receive an email from {{name}} with your gateway credentials." ([payments.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/payments.json?plain=1#L1))
- With a gateway connected: "Your payments will be collected through {{name}} instead of Salla Payments." ([payments.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/payments.json?plain=1#L1))

**For one wallet, Salla's own gateway is replacing the direct connection** *(reading)*. For stc pay: "Merchants who previously connected STC Pay through a direct integration can continue using it without any issues." But once a merchant moves to Salla's own gateway, "Salla fees will be calculated as part of the gateway" and "Once switched, you cannot return back to the direct integration" ([help, en, line 570](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/en/texts.jsonl?plain=1#L570)).

**Not seen in Salla's evidence:** whether Salla's checkout itself asks the buyer for a wallet's phone number and code. I searched Salla's corpus for stc pay, stcpay, stc_pay and its Arabic name, with otp, verification code, mobile number, رمز التحقق and رقم الجوال. I found the method's name, its fees and its logo, not its buyer steps.

**Zid (needed): Zid's own integrations take the merchant's keys, and providers call Zid with the merchant's ID on their side.**
- Zid's dashboard, Emkan's page on the demo store: Zid names itself as the integration's maker, and the merchant fills in its own keys and switches the integration on:
  - "By: Zid" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/raw/runs/20261028T160128Z-dashboard-routes-rest-en/steps/124.text.txt:32)
  - "Client key", "Client secret", "Merchant ID", "Enabled" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/raw/runs/20261028T160128Z-dashboard-routes-rest-en/steps/124.text.txt:49-56)
- A third-party gateway replaces the current one:
  - "The current payment gateway will be disabled to activate the new payment gateway." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:5401)
- Zid's help, published in 2024: "يمكنك تفعيل بوابة الدفع تاب من خلال الاعدادات > طرق الدفع" ([help.zid.sa, L153](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/128-help.zid.sa/text.txt?plain=1#L153)), then "قم بإدخال مفاتيح الربط" ([L155](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/128-help.zid.sa/text.txt?plain=1#L155)). In my rendering: you can turn on the Tap gateway from Settings, Payment methods; enter the connection keys.
- Zid's developer docs describe one entry point for providers' calls: "the Webhook endpoint used to send events to Zid Payments" ([docs.zid.sa, L3](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/054-docs.zid.sa/text.txt?plain=1#L3)).
  - Its events are "merchant_linked", "payment_paid" and "refund_status_changed" ([L12](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/054-docs.zid.sa/text.txt?plain=1#L12)).
  - Each carries the provider's ID, "Which is assigned to each provider on the initial phases of the integration" ([L13](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/054-docs.zid.sa/text.txt?plain=1#L13)), and the merchant's: "Merchant ID on the provider side" ([L14](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261012T045101Z-q1-zid-sources/items/054-docs.zid.sa/text.txt?plain=1#L14)).
  - That is the routing Sharrwah needs: every provider's calls arrive at one place, and the provider's ID with the merchant's ID on its side finds the store *(reading)*.

**BigCommerce (added a detail, not needed to see the gap).** Its own integrations are set up in the control panel with the merchant's credentials, several accounts can serve one store, and a provider outside its own list costs the merchant a fee. The form itself wasn't seen, because the trial store held has online payments switched off; the Help Center states it.
- "Please switch to a paid plan to activate online payments." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:bigcommerce/README.md:11)
- "Enter any required account credentials, such as API keys, and set up any desired provider-specific settings." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/014.text.txt:142)
- "A payment provider can have multiple payment configurations, which allows the same payment provider to be set up multiple times using different merchant accounts, currencies, and settings in a single store." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/014.text.txt:61)
- "Note that custom integrations to processors on the Embedded Payment Provider list, including those connected via third-party apps, will incur Open Payment Provider fees." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/001.text.txt:77)

**WooCommerce (added nothing needed).** The gateway runs inside the merchant's own site, with the merchant's own credentials:
- The gateway class is "Extended by individual payment gateways to handle payments." ([abstract-wc-payment-gateway.php, L24](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/woocommerce-11.2.1/files/includes/abstracts/abstract-wc-payment-gateway.php?plain=1#L24))
- A gateway may show "fields on the checkout" ([L99](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/woocommerce-11.2.1/files/includes/abstracts/abstract-wc-payment-gateway.php?plain=1#L99)), and does its work in "public function process_payment( $order_id )" ([L459](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/woocommerce-11.2.1/files/includes/abstracts/abstract-wc-payment-gateway.php?plain=1#L459)).
- Any plugin adds one: "apply_filters( 'woocommerce_payment_gateways', $load_gateways )" ([class-wc-payment-gateways.php, L92](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/woocommerce-11.2.1/files/includes/class-wc-payment-gateways.php?plain=1#L92)).
- PayPal's gateway keeps "$this->get_option( 'api_username' )" in the store's own settings ([class-wc-gateway-paypal.php, L672](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/woocommerce-11.2.1/files/includes/gateways/paypal/class-wc-gateway-paypal.php?plain=1#L672)).

That is the shape the Yemeni clients assume: a merchant's own system driving the provider's API *(reading)*. With one store to each site, it says nothing about keeping stores apart.

### What no platform shows

- **Whether a provider lets a platform hold and use a merchant's credentials,** or makes the platform sign its own agreement for the integration. Under D16's default 1, an account is B, and comes to the founder, where Sharrwah would be party to the money or to the provider's agreement for it: "one where Sharrwah would be party to the money, or to the provider's agreement for it, is B and comes to the founder" ([D16](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/founder-decisions.tsv?plain=1#L16)). Only each provider's terms decide which case a connection is.
- **Whether a party that runs payments for merchants needs a licence or a registration** in a market. Only the market's law decides it.
- **How Yemen's providers' APIs work, by their own documentation.** Phase 1 had only community-written clients and a package page. No platform's evidence holds the providers' own documentation; it would settle the buyer's steps and the calls a store must answer.

### Phase 1's expectations, checked

**Shopify's shape: confirmed, with one correction.** Phase 1 expected "Payments other than Shopify's own run as payment apps that an approved provider builds and runs." ([phase 1, L110](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/architecture/baseline-test.md?plain=1#L110))
- Confirmed: the app holds the merchant's settings, and the buyer's steps run in checkout or on the app's page.
- Corrected: the builder is an approved Partner, who need not be the provider.
- Made precise: the older gateways, with credentials in Shopify's admin, are still described, but are being moved to apps.

**The other platforms: confirmed for all four, but only two were needed.** Phase 1 expected all four for BT-4 ([phase 1, L307](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/architecture/baseline-test.md?plain=1#L307)).
- Salla and Zid were needed: they show what is missing in Shopify's shape, a connection the platform builds and runs with each merchant's own credentials. Zid also shows how the providers' calls are routed.
- BigCommerce added a detail: several accounts with one provider in one store, and a fee on providers outside its own list.
- WooCommerce confirmed its expected shape, but added nothing needed.

## BT-7. Sharrwah's own fees, from sellers without cards

**The question,** as phase 1 asks it: can Sharrwah bill its own fees to a seller who has no card, paid by wallet, transfer or cash in the market's currency and left unpaid until the payment is confirmed, without taking them from sellers' money or from a balance sellers pay into?

### Shopify's evidence

**Shopify charges its bills to a method it holds on file.**
- "Shopify uses your primary payment method to pay your bills." ([payment-methods-for-bills.md, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills.md?plain=1#L3))
- Cards: "Prepaid and virtual credit cards aren't accepted." ([L7](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills.md?plain=1#L7)) And "Debit cards that aren't co-branded with Mastercard, Visa, or American Express can't be used to pay Shopify bills." ([L13](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills.md?plain=1#L13))
- The page's other methods are Shopify Balance's card, PayPal, Revolut Pay, Apple Pay and Google Pay, ACH debits in the United States, SEPA Direct Debit in some European countries, and UPI in India. UPI runs on a "UPI autopay mandate" ([L270](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills.md?plain=1#L270)).
- Each is a method Shopify charges, or a payment Shopify starts and the merchant approves. None is a payment the seller sends on its own against an open bill *(reading)*.

**Its terms require it, in dollars.** "You must keep a valid payment method on file with us to pay for all" fees, and "Unless otherwise indicated, all Fees and other charges are in ... U.S. dollars, and all payments will be in U.S. currency." ([Terms of Service, legal documents, line 1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/legal-documents/20260930T081039Z-shopify-legal-documents/items.jsonl?plain=1#L1))

**In the founder's markets, the bills are in dollars.** Local currency billing lists Australia, Canada, the European Union, India, Japan, the United Kingdom and some European currencies, then: "For all other countries and regions, Shopify bills are issued in USD." ([local-currency.md, L33](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/paying-your-bills/managing-payments/local-currency.md?plain=1#L33))

**An unpaid bill freezes the store, after retries on the method on file.**
- "Shopify doesn't grant extensions or grace periods for bill payments." ([billing-extensions.md, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-extensions.md?plain=1#L3))
- "If a subscription payment fails, then Shopify retries the charge periodically." Then "If the invoice is still unpaid after 28 days from the first failed attempt, then your store becomes frozen." ([L9](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-extensions.md?plain=1#L9))
- In a frozen store, "customers can't view your store" ([frozen-store.md, L5](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-charges/frozen-store.md?plain=1#L5)).

**Shopify Payments' processing fees are taken from payouts.** They are "deducted from your payouts rather than billed on your Shopify bill" ([types-of-charges.md, L12](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges.md?plain=1#L12)).

**What I searched for and didn't find.** I searched the Help Center's billing pages for a bill the seller pays by its own transfer (wire transfer, bank transfer, pay by invoice). The only bank transfer they name is for one plan in one country: "Automated Clearing House (ACH) Bank transfers for Shopify Plus plans" ([unknown-charge.md, L79](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges/unknown-charge.md?plain=1#L79)). Whether that is a debit or a transfer the merchant sends, the page doesn't say.

### Is it enough for Sharrwah?

**Not enough for sellers who can only send a payment,** which in Yemen I read as most sellers. That is phase 1's reading, from about 400,000 active debit cards at the end of 2019 (YA-120) and Stripe's not serving a business in Yemen (YA-62, as `corrections.md` corrects it).

**What is missing:**
- **A bill that stays open until a payment the seller sends is confirmed.** It needs:
  - the bill;
  - each payment the seller reports against it, by wallet, transfer or cash;
  - each payment's state until Sharrwah confirms or rejects it;
  - the match between a transfer and the bill it pays.
- **Bills in the market's currency.** Shopify's shape bills every one of the founder's markets in dollars.
- **A freeze rule tied to the bill's due date and to the payments pending on it, not to failed charges.** Under Shopify's rule, a seller with no method Shopify can charge is frozen 28 days after the first failed attempt *(reading)*.

**The class's other ways of collecting fees are closed to Sharrwah at launch.** The founder's decisions say Sharrwah's fees are "billed apart, never taken from sellers' money at a provider", and "No balance that sellers pay into" ([D16](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/founder-decisions.tsv?plain=1#L16)), while "a market runs only C" ([D20](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/founder-decisions.tsv?plain=1#L20)). So Shopify's deduction from payouts can't fill the gap either.

**Where it would be enough with a provider.** Where a market has a debit that a provider can draw on the seller's behalf, as UPI's autopay mandate is in India, Shopify's shape is enough with that provider. The evidence I read doesn't say whether Yemen's wallets offer such a mandate, and phase 1 records none.

### The other platforms

**Salla (needed): bills that wait for a transfer.** Its billing pages have:
- "Outstanding invoices", described as "Review all outstanding invoices on your store with amount and due-date details.", each with "Pay invoice" ([billing.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/billing.json?plain=1#L1));
- "Bank transfer requests", described as "View all bank transfer requests from your store, including details and status." ([billing.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/billing.json?plain=1#L1));
- the methods a bill can be paid by: "Bank transfer", "Credit card", "Mada", "Apple Pay" and "Store wallet" ([billing.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/billing.json?plain=1#L1)).

How a transfer is matched to the invoice it pays isn't in the strings I read.

**Salla also uses the two shapes Sharrwah's defaults rule out.**
- A wallet the merchant pays into: "Add funds", after which "Your wallet balance may take up to 48 hours to update." Salla takes subscriptions from it: "Total amount deducted from your store wallet balance, including subscriptions, services, purchases, and refunds transferred to your bank account." ([payments.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/payments.json?plain=1#L1))
- Fees taken before the payout: "The amount that will be transferred to your bank account after fees and taxes are deducted." ([payments.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/payments.json?plain=1#L1))

**Zid (needed): a plan paid by bank transfer, and its status confirmed later.**
- Zid's subscription checkout offers a bank transfer to Zid's own account:
  - "To pay by bank transfer, please transfer the due amount to the Zid account at Al Rajhi Bank" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:2203)
- Its questions for merchants include how to confirm a transfer:
  - "How can i confirm the status of a bank transfer?" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:2265)
  - "You can confirm the status of your bank transfer by logging into your store dashboard and checking the status of the bank transfer." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:2264)
- Zid too has a wallet that the merchant tops up and can spend at the plan's checkout:
  - "Your wallet account information in Zid for recharging via bank transfer" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:1730)
  - "Use wallet balance" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:2233)
- One way Zid collects is out of its own payment service's takings, as I read this name of a wallet transaction *(reading)*:
  - "Collection through ZidPay splitting" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:1773)

**BigCommerce (added nothing).** Its shape is Shopify's: a method on file, charged automatically.
- "The methods available to pay your invoice can vary depending on your store's plan and region." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/008.text.txt:117)
- "Note that this method will now be used to automatically pay charges for future billing cycles." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/008.text.txt:118)

**WooCommerce: not searched for this question.** It is software the merchant runs, and phase 1 didn't expect it to be needed here.

### What no platform shows

- **Whether a seller in each market may pay Sharrwah's company,** wherever the founder places it (the company is the founder's: [D26](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/founder-decisions.tsv?plain=1#L26)), in which currency and by which channel. And whether Sharrwah must hold an account in the market to receive it. Only each market's law and its banks' practice decide it. Phase 1's restrictions in Algeria, Tunisia, Egypt and Lebanon are an assumption, still unchecked.
- **What Sharrwah's bill must be as a document in each market,** whether a tax invoice or not. Only the market's tax law decides it; this is BT-11's ground.

### Phase 1's expectations, checked

**Shopify's shape: confirmed, with additions.** Phase 1 expected "Shopify charges its bills to a card or PayPal on file, or in some countries a bank account, in a set of billing currencies, and freezes a store whose bill goes unpaid" ([phase 1, L165](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/architecture/baseline-test.md?plain=1#L165)).
- Added: the methods are more (Balance's card, wallets, mandates), but all are methods Shopify charges.
- Added: bills are in dollars in every one of the founder's markets.
- Added: the freeze comes 28 days after the first failed attempt.
- Made precise: what Shopify Payments takes from payouts is its processing fees; the subscription is billed.

**The other platforms: confirmed.** Phase 1 expected Salla and Zid. Both were needed, and both show a bill paid by transfer and confirmed later. BigCommerce, not expected, added nothing.

## BT-14. A basket across stores

**The question,** as phase 1 asks it: can one basket, and the order it makes, take goods from several stores, with each store's share paid into that store's own provider account?

### Shopify's evidence

**Shopify has a checkout across stores, but only on its own payments, in one country, in an app closed to new stores.** This is Shopify Product Network.
- "Customers can add recommended products to their cart along with your own." ([customer-experience.md, L41](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/customer-experience.md?plain=1#L41))
- With goods of several stores, the buyer uses "multi-store checkout" ([L71](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/customer-experience.md?plain=1#L71)):
  - "Products are grouped by store." ([L75](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/customer-experience.md?plain=1#L75))
  - "Taxes and shipping are calculated for each store." ([L76](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/customer-experience.md?plain=1#L76))
  - "Payment is processed separately for your store and for other brands' stores." ([L77](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/customer-experience.md?plain=1#L77))
- Each store gets its own order: "each store that has line items in the checkout gets its own order" ([orders.md, L23](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/orders.md?plain=1#L23)).
- Disputes stay with each store: "Payment disputes and chargebacks for seller line items are between the customer and the selling store (and its payment provider), not your store." ([orders.md, L75](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/orders.md?plain=1#L75))
- Its limits:
  - payment by "Shopify Payments or Shop Pay only." ([customer-experience.md, L60](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/customer-experience.md?plain=1#L60));
  - "Your store must have both Shopify Payments and Shop Pay activated" ([requirements.md, L14](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/requirements.md?plain=1#L14));
  - the other stores' products are "visible only to customers in the United States" ([customer-experience.md, L15](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/customer-experience.md?plain=1#L15));
  - "The Shopify Product Network app is no longer available for new installations." ([shopify-product-network.md, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network.md?plain=1#L3))

**Collective: one store sells another store's goods, and Shopify Payments moves the share.**
- "When a customer places an order in your store, you receive full payment for that order. From that payment, you need to pay your supplier for the cost of the product sold, and for the cost of shipping." ([Collective, retailers, payments.md, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shopify-collective/retailers/payments.md?plain=1#L3))
- "the cost price of any Shopify Collective product that you sell is automatically debited from your Shopify Payments balance. The funds then transfer to your supplier's Shopify Payments account automatically when they mark the order as fulfilled." ([L9](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shopify-collective/retailers/payments.md?plain=1#L9))
- "After a customer places an order in your store, you and your supplier receive an order in your Shopify stores." ([managing-collective-orders.md, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shopify-collective/retailers/managing-collective-orders.md?plain=1#L3))
- It needs Shopify Payments, whose "account must have active payouts" ([requirements-and-considerations.md, L17](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shopify-collective/retailers/requirements-and-considerations.md?plain=1#L17)).

**For agents: a cart across merchants, in early access; otherwise each cart goes to its merchant for payment.** From shopify.dev, captured on 11 October 2026. How a universal cart is paid isn't stated in what is held.
- "The Universal Cart API lets AI agents collect items from any merchant, on or off Shopify, into a single, unified cart, all via UCP." ([agents.md, L100](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/108-shopify.dev/text.txt?plain=1#L100)) It sits behind "Join the early access waitlist." ([L106](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/108-shopify.dev/text.txt?plain=1#L106))
- Otherwise agents "Build carts, convert them to checkouts, and hand off to the merchant for payment." ([L118](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/evidence/product-class/runs/20261011T061248Z-q1-shopify-sources/items/108-shopify.dev/text.txt?plain=1#L118))
- A store's own agent tools sit under that store's own address, "capture-plus.myshopify.com/api/ucp/mcp" ([UCP tools, meta.json, L9](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/storefront-ucp-mcp-tools/capture-plus/meta.json?plain=1#L9)).

**The Shop app syncs one store's cart.**
- "Cart sync doesn't combine carts." ([shop, customer-experience.md, L99](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shop/customer-experience.md?plain=1#L99))
- "Shop is available in countries where Shopify Payments is supported" ([shop.md, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/online-sales-channels/shop.md?plain=1#L10)), which in the founder's markets means the United Arab Emirates (BT-4).

**Shopify's terms make each sale the store's own.** "You acknowledge and agree that the Services are not a marketplace, and any contract of sale made through the Services is directly and only between you and the customer." ([Terms of Service, legal documents, line 1](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/legal-documents/20260930T081039Z-shopify-legal-documents/items.jsonl?plain=1#L1))

### Is it enough for Sharrwah?

**Not enough under C, in all markets, though the order shape is there.** D26 keeps room for a marketplace and a buyer app in every market.

**The order shape is there.** Product Network shows it: one checkout, goods grouped by store, each store's own order, each store's own payment.

**What is missing is the money under C,** which D16 sets in every market at launch.
- **One checkout that runs a separate payment with each store's own provider.**
  - Shopify's multi-store checkout works because one processor, Shopify Payments, takes every store's payment.
  - Collective works because Shopify Payments moves the supplier's share out of the retailer's balance.
  - Under D16, each store's provider holds the money "in the seller's own account with that provider" ([D16](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/founder-decisions.tsv?plain=1#L16)). The stores in one basket may use different providers, each with its own buyer steps (BT-4), and some may take cash on delivery or a transfer *(reading)*.
- **A record above the stores' orders** that holds the basket's payments store by store, and says what happens when one store's payment succeeds and another's fails or is still pending *(reading)*. Shopify's evidence shows a marker on the referring store's own order, not such a record: "That order includes a banner indicating that seller products were also purchased from other brands at checkout." ([orders.md, L33](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/promoting-marketing/shopify-product-network/orders.md?plain=1#L33))

**Where Shopify's shape would come nearer.** If the founder switched on B in a market, where Sharrwah would be party to the money, a one-processor checkout like Shopify's might come nearer to enough there *(reading)*. Switching A or B on is the founder's decision (D16's guard).

### The other platforms

**Salla (needed): a basket across stores in the region, with one payment page, for card methods only.** Salla's help on Mahally, its marketplace app, says four things ([help, ar, line 1077](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/ar/texts.jsonl?plain=1#L1077)). Each is followed by my rendering:
- "عندما يضيف العميل منتجات من متاجر متعددة إلى سلة واحدة،يتم توجيهه تلقائيًا إلى صفحة دفع مخصصة للسلة الموحدة." ([line 1077](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/ar/texts.jsonl?plain=1#L1077)) When a customer adds products from several stores to one cart, they are sent to a payment page for the unified cart.
- "طرق الدفع المتاحة حاليًا تدعم صفحة الدفع الموحدة حاليًا ثلاث طرق دفع فقط : فيزا/ماستركارد مدى آبل باي" ([line 1077](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/ar/texts.jsonl?plain=1#L1077)) The unified payment page supports only three methods: Visa or Mastercard, mada, and Apple Pay.
- "ففي حال كان متجرك يدعم الدفع عند الاستلام أو التحويل البنكي فلن تظهر حالياً هذه الوسائل للعميل في صفحة الدفع عند إنهاء الطلب من خلال محلي." ([line 1077](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/ar/texts.jsonl?plain=1#L1077)) Cash on delivery and bank transfer don't show at Mahally's checkout.
- "حيث سيظهر الطلب القادم من محلي في لوحة تحكم متجرك في صفحة الطلبات، مع توضيح أن الطلب من محلي داخل صفحة الطلب." ([line 1077](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/ar/texts.jsonl?plain=1#L1077)) Each store gets its order in its own dashboard, marked as from Mahally.

**What Mahally is.** It calls itself "The premier Saudi Arabian digital marketplace and mobile platform connecting consumers with tens of thousands of local stores." ([Mahally's llms.txt, L3](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/mahally-llms/llms-txt/source.txt?plain=1#L3)) A store that would join it is asked to "Enable online payments" ([mahally.json](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/dashboard-translations/en/mahally.json?plain=1#L1)).

**Not stated in what I read:** who collects the unified payment, and how each store's share reaches the store. *(Reading:)* the three methods are those of Salla's own payment service, which "processes payments in your store directly, settling transactions with banks and your approved payment methods automatically" ([help, en, line 808](https://github.com/Hamza-ye/observed-sa/blob/b0bd0b16355f5a7de0358db4895f3e77c2e1fc96/structures/salla/help-articles/en/texts.jsonl?plain=1#L808)). So the platform's own service likely takes the unified payment, which in Sharrwah's terms would not be C.

**What Salla adds to Shopify.** Shopify and Salla both narrow a checkout across stores to the methods of one processor. Neither shows one over several providers, or over cash on delivery or transfers: the methods Yemen's C relies on *(reading)*.

**Zid: held too thinly to tell.**
- I searched Zid's corpus (its dashboard's strings, its run steps and saved answers, and this repository's Zid pages) for multiple stores, several stores, more than one store, one cart, unified cart, multi-vendor, متاجر متعددة, أكثر من متجر and سلة واحدة. I found nothing on a basket across stores.
- Zid's buyer-facing surfaces (zid.sa, its apps) aren't held (other-product-class, `zid/GAPS.md`).
- Zid's dashboard shows only orders from outside marketplaces synced into the store, the shape Shopify's sales channels have:
  - "Sync every order from {{marketplace}} in your Zid account (even if the product doesn't exist in your catalog)" (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:zid/structures/dashboard-locales/items.jsonl:7984)

**BigCommerce (added nothing).** Its marketplace channels feed orders into the store, as Shopify's do:
- "Orders from marketplace channels come into your control panel the same way storefront orders do." (other-product-class@0d79b794ff33b310ba34ca6c14acc8a2b9f0a3e4:bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/011.text.txt:67)

**WooCommerce (added nothing).** It runs one store to each site. I searched its held evidence for multi-vendor, multivendor, multiple vendors, vendors, multi-seller and marketplace. I found WooCommerce's marketplace of extensions, a script's name and card-category keywords, but nothing on several sellers in one checkout. No multi-vendor extension is held, so WooCommerce is held too thinly to tell what one would do.

### What no platform shows

- **Who the seller of record is for a basket across stores,** and whether one checkout that takes payment for several sellers makes the platform a payment intermediary or a marketplace operator, with the licence and duties that brings. Only each market's law decides it.
- **Whether a market's providers can take one buyer's authorization and pay it into several merchants' accounts,** a split at the provider. Only each provider's offer decides it, and no platform's evidence holds it.
- **Whether Sharrwah's own company runs a marketplace or a buyer app.** That is the founder's decision ([D26](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/founder-decisions.tsv?plain=1#L26)); the platform keeps room for it either way.

### Phase 1's expectations, checked

**Shopify's shape: partly wrong.** Phase 1 expected "A cart and an order belong to one store; the Shop app gathers stores for buyers but checks out store by store." ([phase 1, L292](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/architecture/baseline-test.md?plain=1#L292))
- An order belongs to one store: confirmed.
- A cart belongs to one store: wrong. Product Network's multi-store checkout takes several stores' goods in one cart and one checkout. The Universal Cart, in early access, gathers any merchant's items for agents.
- The Shop app: not shown either way. The held evidence shows it syncing one store's cart, not a basket across stores.
- Collective, which phase 1 didn't expect, is a third shape: one store sells another's goods and Shopify Payments pays the share.

**The other platforms: partly confirmed.** Phase 1 expected Salla and Zid ([phase 1, L307](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/9420f437cfe09065a2083e6a2a3a5f9c1127f99f/architecture/baseline-test.md?plain=1#L307)).
- Salla: confirmed, and needed.
- Zid: not confirmed. It is held too thinly to tell.
