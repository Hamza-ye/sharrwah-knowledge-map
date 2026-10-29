# BigCommerce: what is not held yet

Each row: what BigCommerce shows or publishes that this folder does not hold, why, and how it can be held.

| Not held | Why | Route |
| --- | --- | --- |
| BigCommerce Payments' onboarding and its KYC: the documents and checks it asks for, for a US and a UK store | a trial store has online payments switched off ("Online payment methods are disabled for this store. Please switch to a paid plan to activate online payments.", run 20261029T012951Z-store-settings-en, step 41); BigCommerce states the requirements: a Core, Growth or Scale plan, a store located in the UK or the US, a UK or US PayPal Business account, and KYC status shown in the account's Actions (run 20261029T025543Z-help-center-2-en) | a paid plan, which waits for the founder; then Settings > Payments > BigCommerce Payments > Set up with the store's default country set to the US, then the UK |
| PayPal's business onboarding for the UK | it answered a Security Challenge (run 20261029T025543Z-help-center-2-en, step 3) | the same page with the founder ticking the challenge |
| A second storefront with its own store profile, localization and payment configuration | "Create more storefronts with paid plan" (run 20261029T023811Z-channels-en, step 2) | a paid plan, which waits for the founder |
| A store made with a default country other than Oman | the sign-up asks no country; from this machine's Yemeni network BigCommerce made the store with Oman; through the VPN (GB) it refused the sign-up (`{"pass":false}`) | a sign-up from another network location that BigCommerce accepts |
| An invoice from BigCommerce, with its tax as issued | an invoice is issued after a payment; the checkout's Taxes line is held for 15 billing addresses (run 20261029T015915Z-plan-upgrade-en) | a paid plan, which waits for the founder |
| Apps that sell as merchant of record (cross-border) in the App Marketplace | the public marketplace's search listed every app rather than its matches (run 20261029T023811Z-channels-en, step 5), and the Help Center has no article on "merchant of record" (run 20261029T024758Z-help-center-en, step 22) | the marketplace's categories and app pages one by one, or its search through the control panel |
| An automatic tax service set up (Avalara, TaxJar, Vertex, ...) and its Provider Targeting | each asks for an account with the provider | a provider's free trial account |
| The structures in [structures/REGISTER.tsv](structures/REGISTER.tsv) marked backlogged, as items | held as page and answer bytes | read each into `items.jsonl` |
