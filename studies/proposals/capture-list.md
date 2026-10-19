# What only you can capture, or ask (optional)

Written by `method/capture_list.py` from the recording runs' rows that only you can close: pages inside a seller's account, pages that can't be read from here, and questions only the platform can answer. Each says where to go, what to capture or ask, and what it would show. Capturing is optional, and the work doesn't wait for it. Anything you capture can still feed the proposals.

**How to save a page:** SingleFile from a normal browser, into `evidence/product-class/blocked-evidence-founder/<platform>/`, as before. Captured accounts are synthetic, so nothing needs masking.

## Shopify (11)

**To capture:**

- **each captured store's admin, Settings > General (admin.shopify.com/settings/general, not held): the store address and billing country section**
  - It would show: The country of each captured store's address or billing address, held beside its RequestDetails feature values (Q1, `Q1-SH-N04`)
- **Capture, on a store with Shopify Payments, the page reached from Settings > Payments > Shopify Payments in the Shopify admin (admin.shopify.com/settings/payments) while a verification request or the Activate Shopify Payments flow is open: each step's fields and any deadline shown.**
  - It would show: What the Shopify Payments verification request in the admin asks a given store for, and the deadlines it displays: the pages read say a deadline is displayed in the Shopify admin (Q3-SH-069) and that the request is reached from Settings > Payments > Shopify Payments, but show no such request. (Q3, `Q3-SH-N03`)
- **help.shopify.com pages on refunding orders paid by manual payment methods; or a refund of a test order paid with a manual payment method on a held store**
  - It would show: What happens when a seller refunds an order paid with a manual payment method: whether Shopify moves any money, and how the refund is recorded on the order (Q4, `Q4-SH-N02`)
- **https://admin.shopify.com/settings/payments: the Payment providers section, Manual payment methods drop-down, with its list of suggested methods**
  - It would show: The list of suggested manual payment methods that Settings > Payments offers in the Payment providers section (Q4, `Q4-SH-N03`)
- **the payment gateways page of shopify.com (its held copy and the live page read here show only the unfiltered list): type a country in its 'Type in your country' filter and capture the list it then shows**
  - It would show: The payment providers that https://www.shopify.com/payment-gateways lists for a given country or region once a country is typed in its filter (Type in your country) (Q6, `Q6-SH-N01`)
- **admin.shopify.com/store/2jiwxs-gr/settings/payments: the whole Payments page, then the list that Choose a provider opens in the Payment providers section**
  - It would show: What the Payments settings page shows to a store whose Shopify Payments provider answers "eligible":false (store 2jiwxs-gr.myshopify.com, signed up with country=YE): its Payment providers section and the list behind Choose a provider (Q6, `Q6-SH-N02`)
- **the sign-up flow on accounts.shopify.com (its held copy was read): choose, in I'm located in:, each place the held list leaves out, if it can be entered, and capture any message shown**
  - It would show: Words, on the sign-up page or in Shopify's help, that present the options of the combobox I'm located in: as the full set of places a seller can register from, or that name the places it leaves out (Q6, `Q6-SH-N03`)
- **admin.shopify.com/payments/payouts in a store with Shopify Payments active and a reserve or a balance: the Payout balance and Reserved funds amounts, with the currency each is shown in**
  - It would show: The currency in which Shopify Payments holds Reserved funds, and the currency of funds held in a Payment Processor Account before a payout is made (Q7, `Q7-SH-N01`)
- **admin.shopify.com/settings/general, Store defaults section, menu > Change store currency: the full drop-down list of currencies, in one store whose location is set to a country without Shopify Payments and one with it**
  - It would show: The full list of currencies offered as store currency in the Change store currency drop-down (Q7, `Q7-SH-N03`)
- **a store invited by Shopify to a Beta Service: the beta terms shown in the Shopify admin before the store first uses it**
  - It would show: The additional terms and conditions that apply to a Beta Service, which the Terms of Service say Shopify will provide before its use, and which Beta Services are offered (Q8, `Q8-SH-N01`)
- **Shopify's enterprise sales team, through the contact form on Shopify's enterprise page: the enterprise agreement or order form that sets these services**
  - It would show: The contract terms on which the Shopify for enterprise services marked *Dependent on contract terms depend (Q8, `Q8-SH-N02`)

## Salla (13)

**To capture:**

- **Merchant dashboard https://s.salla.sa/localization/settings (الأسواق المتعددة > الإعدادات > تسعير المنتجات), as the owner of a Special-plan store with Markets active: capture the Product pricing setting with Automatic pricing by exchange rate selected, and any text on the rate used**
  - It would show: Where the exchange rate used by Automatic pricing by exchange rate (تسعير تلقائي حسب سعر الصرف) comes from, and who sets or can change it. (Q1, `Q1-SA-N02`)
- **Merchant dashboard, Orders (الطلبات): open an order placed by bank transfer in status بانتظار المراجعة and save the order page, showing the attached receipt and the actions offered on it (https://s.salla.sa/orders, not held)**
  - It would show: The steps by which a merchant reviews a bank transfer receipt (إيصال) attached by a customer and confirms the payment, moving the order out of بانتظار المراجعة, and whether Salla takes part in that review (Q4, `Q4-SA-N02`)
- **Merchant dashboard: (الكل) › الإعدادات والأدوات › طرق الدفع › المحافظ الرقمية › PayPal: capture the connection drawer's text when PayPal is activated**
  - It would show: Where payments made by customers through PayPal go: into the PayPal account whose email the merchant enters, or through Salla (Q5, `Q5-SA-N02`)
- **no address in Salla's material read; the providers' own merchant agreements**
  - It would show: The terms of the merchant's own agreements with the providers Salla's articles name: عقد التاجر مع تمارا, اتفاقية التاجر مع تابي and عقد التاجر مع جيديا. Salla's material read names them and gives no address for them (Q5, `Q5-SA-N03`)
- **Merchant dashboard: the page مقارنة بوابات الدفع at /payments/gateways/comparison (the path as payments.json's breadcrumb key names it), and the page طرق الدفع at /payments/gateways**
  - It would show: A list, presented as complete, of the payment gateways (بوابات الدفع الأخرى) a merchant can connect besides مدفوعات سلة. The pages read give examples only (مثل; ميسر - هايبر باي) (Q5, `Q5-SA-N04`)
- **Store sign-up at https://s.salla.sa/auth/register (not held): the country step (دولة المتجر), choosing a country outside the list, and the screen that follows**
  - It would show: What Salla states a seller based in a country other than Saudi Arabia, the UAE and Kuwait can do, beyond the sign-up message countryOther.description and the help centre's answer on a foreign merchant registering with a Saudi commercial registration (Q6, `Q6-SA-N03`)

**To ask:**

- **Question to Salla merchant support, asked from the merchant dashboard: does Salla screen merchants, owners or payments against sanctions lists, which lists, and which countries are refused**
  - It would show: A statement that Salla restricts or withholds its platform, Salla Payments or stores for a country, person or customer because of sanctions or a sanctions list, with the list it applies and its reason; the held KYC schema names a check CheckSallaBlacklisted ('ID suspended due to compliance or terms violations') without naming what it checks against (Q2, `Q2-SA-N01`)
- **Merchant dashboard, store verification page (توثيق المتجر, https://s.salla.sa/payments/kyc; not held) of a store not yet verified: capture any notice or banner that states the period before payments are suspended; or ask Salla merchant support (dashboard help) how long the period is.**
  - It would show: The length of the period (المهلة) after which payment and settlement operations (عمليات الدفع والسداد) of a store that is not verified are suspended, and when that period starts. (Q3, `Q3-SA-N01`)
- **Question to Salla merchant support (dashboard help): which products or activities need a licence before they can be sold on Salla, and whether and when Salla checks it.**
  - It would show: A list of the products or activities for which Salla requires a licence before they are sold, or a statement of whether, when and how Salla checks such a licence. (Q3, `Q3-SA-N02`)
- **Question to Salla merchant support (dashboard help): when and how a store's products are checked against سياسة البيع, and what the merchant can do while a violation (المخالفات, /manage/violation) is open.**
  - It would show: When and how Salla checks that a store and its products comply with the selling policy (سياسة البيع) or the usage agreement's المادة العشرون after the policy is accepted. (Q3, `Q3-SA-N03`)
- **A question to Salla merchant support from the merchant dashboard's help: does Salla charge any fee on an order paid by bank transfer, or paid on delivery to the merchant's own carrier or courier?**
  - It would show: A statement of whether Salla charges any fee of its own on an order paid by bank transfer (التحويل البنكي), or paid on delivery to the merchant's own carrier or courier (Q4, `Q4-SA-N01`)
- **A question to Salla merchant support from the merchant dashboard's help: is there any limit on the amount of an order paid by bank transfer?**
  - It would show: Any limit on the amount of an order paid by bank transfer (التحويل البنكي), other than the payment restrictions (قيود الدفع) a merchant sets (Q4, `Q4-SA-N03`)
- **a question to Salla's merchant support on what notice precedes the withdrawal of a payment method**
  - It would show: A notice to the merchant, or a period, before Salla cancels, changes or replaces a payment method it made available under المادة الثامنة of اتفاقية الاستخدام, and what then happens to orders paid and amounts held through that method (Q5, `Q5-SA-N01`)

## WooCommerce (1)

**To capture:**

- **A store with WooPayments: Payments > Settings > Advanced settings, the Enable Multi-Currency box, and the WooCommerce > Settings multi-currency tab with its Enabled currencies list**
  - It would show: The recorded state of the Enable Multi-Currency setting on a running store (Q7, `Q7-WC-N13`)

## Zid (16)

**To capture:**

- **store dashboard: الاعدادات > الأسواق > إدارة السوق (capture the market settings form); no dashboard address is held**
  - It would show: Payment methods turned on or off for one market only (Q1, `Q1-ZD-N05`)
- **store dashboard: الاعدادات > الأسواق > إدارة السوق (capture the market settings form); no dashboard address is held**
  - It would show: Store languages set for one market only (beyond the market's name in Arabic and English) (Q1, `Q1-ZD-N07`)
- **store dashboard: الاعدادات > الأسواق > إدارة السوق (capture the market settings form); no dashboard address is held**
  - It would show: A domain or subdomain set for one market (Q1, `Q1-ZD-N08`)
- **store dashboard: الاعدادات > الأسواق > إدارة السوق (capture the market settings form); no dashboard address is held**
  - It would show: Closing the store for one market only (Q1, `Q1-ZD-N12`)
- **Zid dashboard, المدفوعات > تفعيل الدفع الالكتروني: capture the page shown after pressing تفعيل, and the payments page while the review is pending**
  - It would show: What a Saudi seller can and cannot do with زد باي between submitting activation and the review's acceptance: whether payments are taken and held, or not taken, while the review is pending (Q3, `Q3-ZD-N02`)
- **Zid dashboard, home page after sign-up: capture the panels معلومات متجرك, موثوقية المتجر and تجهيز المتجر, and any notice shown before the store is reachable by buyers**
  - It would show: A check or condition Zid applies before a store is opened to buyers (إطلاق المتجر), or any setting for opening or closing the store to buyers beyond the steps the onboarding pages list (Q3, `Q3-ZD-N03`)
- **Zid's registration flow, past its first page (captured on 19 October 2026): after entering an email, the steps معلوماتك and تفاصيل المتجر; capture the question من وين تبيع ؟ (تحديد موقعك أو موقع المخزون) with its full country list, and what the flow shows when a country outside the list is entered**
  - It would show: The countries a person can choose as the store's location (الدولة) in the registration flow, and what the flow shows when a location outside them is entered (Q6, `Q6-ZD-N01`)
- **dashboard of a store whose country is a Gulf country other than Saudi Arabia: الاعدادات > المتجر > بيانات المتجر > تفاصيل النشاط التجاري; capture the entity types offered and the documents each asks for**
  - It would show: The business-details requirements (تفاصيل النشاط التجاري: entity types and documents) for a store whose country is not Saudi Arabia; the held store-data article gives only the section السعودية (Q6, `Q6-ZD-N03`)
- **Seller dashboard: لوحة التحكم > الاعدادات > اللغات والعملات, the screen and any confirmation shown when choosing a different currency with اختيار كعملة أساسية in a store that already has orders; then one existing order before and after. Address not known; held_index: web.zid.sa and dashboard.zid.sa not held**
  - It would show: What happens to orders already recorded, and to their amounts, when the seller changes the store's العملة الأساسية (Q7, `Q7-ZD-N03`)
- **Seller dashboard: لوحة التحكم > الاعدادات > اللغات والعملات, the currency list with its تفعيل and اختيار كعملة أساسية controls, in one store on each plan available. Address not known; held_index: web.zid.sa and dashboard.zid.sa not held**
  - It would show: The list of currencies a seller can choose as العملة الأساسية or activate in لوحة التحكم > الاعدادات > اللغات والعملات, and whether the choice is limited by the store's country or plan (Q7, `Q7-ZD-N05`)

**To ask:**

- **ask Zid how long the review of زد باي activation takes**
  - It would show: How long Zid's team takes to review the information submitted when a Saudi seller activates زد باي (تفعيل الدفع الالكتروني), before the seller is notified by email (Q3, `Q3-ZD-N01`)
- **ask Zid for the list of activities that need a licence**
  - It would show: The full list of business activities or products for which Zid requires a licence (تراخيص) before activating payments; the page gives one example (بيع الكتب, وزارة الإعلام) and says it is decided after reviewing the data (Q3, `Q3-ZD-N04`)
- **ask Zid for the provider terms that apply to a Zid Pay merchant**
  - It would show: The terms and conditions of مقدم الخدمة to which the زد باي terms make the payment networks (خيارات الدفع (شبكات الدفع)) subject; the terms give no name or address for them. Q3-ZD-G0015 covers the providers' names and licences (Q3, `Q3-ZD-N06`)
- **Ask Zid; or read the held pages again after a new capture**
  - It would show: The currency in which the balance in Zid Pay (رصيد حسابك في زد باي; رصيد قيد المعالجة; لم يتم الإيداع) is held before deposit (Q7, `Q7-ZD-N01`)
- **Ask Zid; or read the held pages again after a new capture**
  - It would show: The currency in which Zid Pay deposits (الإيداعات) are paid into the seller's bank account, named as a currency rather than as the amounts of the minimum and fee (Q7, `Q7-ZD-N02`)
- **Ask Zid, or the gateways' own merchant documentation as Zid names it**
  - It would show: The currency in which buyers pay, and the seller is paid, through بوابات الدفع الأُخرى (باي موب Paymob, اموال باي amwal pay, بوابة الدفع تاب Tap) (Q7, `Q7-ZD-N04`)

## BigCommerce (5)

**To capture:**

- **Capture the Help Center chapters "Enabling Multi-Storefront" and "Configuring Storefronts" of the Guide to Multi-Storefront (the held capture of its first chapter holds only chapter 1), and the Channel Manager menu articles "Create Storefronts" and "Creating an International Storefront"; held_index: not held; support.bigcommerce.com renders no text from here**
  - It would show: What BigCommerce says adding a storefront involves in the control panel: the steps, requirements and limits of the Help Center chapters named "Enabling Multi-Storefront", "Configuring Storefronts", "Create Storefronts" and "Creating an International Storefront" (Q1, `Q1-BC-N01`)
- **Capture https://support.bigcommerce.com/s/article/Multi-Storefront-Payment-Methods?language=en_US; held_index: not held; it renders no text from here**
  - It would show: Which payment methods and payment provider settings can be set per storefront, and how, as the Help Center article "Multi-Storefront Payment Methods" gives it (Q1, `Q1-BC-N02`)
- **Capture the Help Center article on shipping zones (https://support.bigcommerce.com/s/article/Shipping-Zones, held_index: not held) and, in a store, Settings > Setup > Shipping with more than one storefront**
  - It would show: Whether shipping zones are set for the whole store or per storefront, and the control panel page where a shipping zone is added (Settings > Setup > Shipping) (Q1, `Q1-BC-N03`)
- **In a BigCommerce store's control panel, Settings › Payments, Embedded tab, Online Payment Methods, BigCommerce Payments › Set up: capture each step of the onboarding flow and the Actions section's tasks, including Know Your Customer (KYC) status**
  - It would show: The information and documents a seller provides for the BigCommerce Payments Know Your Customer (KYC) check, and which people (owners, representatives) must be identified (Q3, `Q3-BC-N01`)
- **BigCommerce control panel (manage.bigcommerce.com and login.bigcommerce.com not held): the left navigation menu that Using the App Marketplace names, with every top-level entry expanded**
  - It would show: The top-level entries of the control panel's left navigation menu, which show how the control panel groups what a store can use (Q8, `Q8-BC-N03`)
