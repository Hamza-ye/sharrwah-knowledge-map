# S-02: evidence only you can get

**What this file is:** the founder's page for the evidence S-02 still lacks that no run in this session, in observed-sh or in observed-sa can capture (`PLAN.md`, section 6, Evidence). Written on 27 October 2026, after gap-closing.

**Nothing here blocks the work.** Phase B's second pass and phase C go on. A question still open for a platform is marked as not stated for that platform. An answer that comes later is added, and the rows it touches are checked again.

**Where the evidence stands.** Gap-closing read the pages its agents could find on S-02's open questions, and added 1,165 statements. 49 questions remain that nothing read answers. Each is a *gap*, kept in the platform's `gaps.tsv` with the work that would close it:
- **15 can be captured by your local agent:** 5 on Shopify and 10 on Salla. They are in the capture requests ([`handoffs/`](../handoffs/README.md)).
- **34 need you:** 21 on Zid, 7 on BigCommerce, 5 on WooCommerce and 1 on Salla. Your local agent's repositories hold only Shopify and Salla, so these need a store on the platform, or a question to it.

*Changed on 28 October 2026,* after your local agent's runs for H-006 to H-008 (observed-sh `19a5f6435`). They settled Shopify's five capturable gaps: two are answered, and three are narrowed into questions no run can answer. One needs a valid SSN or ITIN; the others need the platform's own word. Those three are now in section 5, "To Shopify". Salla's ten capturable gaps wait on H-001 to H-005.

*Changed on the evening of 28 October 2026,* after your local agent's captures of Salla (H-001 to H-005, observed-sa `b0bd0b16`) and Zid (`other-product-class`, `zid/`):
- **Sections 1 and 2 need no answer now.** H-001 to H-008 have run, as far as Salla's review and gate allowed, and Zid has been looked at.
- **Sections 3 and 4 need none either.** Your local agent is capturing BigCommerce and WooCommerce.
- **What remains is section 5,** the questions only a platform can answer. Each gap's verdict, whether closing it could change an S-02 decision, is in [`gap-assessment.tsv`](../studies/subjects/S-02/gap-assessment.tsv).

## 1. Hand the capture requests to your local agent

H-001 to H-007 are as before. What changed today:
- **[H-008](../handoffs/H-008-observed-sh-markets-per-plan-checkout-address.md) is new,** for observed-sh. On its own dev stores, one per plan: how many markets of each kind a plan allows, which business types Markets is offered to, and the checkout's address form for six buyer countries.
- **[H-002](../handoffs/H-002-observed-sa-onboarding-countries.md) and [H-005](../handoffs/H-005-observed-sa-multi-market.md) take five more Salla questions,** on screens of the same journeys.

H-005 may still need a store on Salla's Special plan, a spending decision that comes with it.

**Answer:** handed over, or not now.

*Done on 28 October 2026:* H-006 to H-008 ran at observed-sh `19a5f6435`, and H-001 to H-003 at observed-sa `b0bd0b16`. H-004 stopped at Salla's review, and H-005 at Salla's gate ([`handoffs/README.md`](../handoffs/README.md)).

## 2. Zid: a store to look at (up to 17 of its 21 gaps)

Most of Zid's gaps ask one thing: which settings can differ by market. Zid's pages describe each setting for the whole store, and its page on markets doesn't say. A look at a Zid store with two markets settles them. It also shows where the store's country is held, and which countries sign-up offers.
- **(a) A development store.** Zid's developer documentation has app developers test on development stores they create: "Set up your app on development stores after creating them, to test its functionality" (docs.zid.sa, held). It doesn't say what one costs, or whether it includes markets.
- **(b) One month of Zid's Growth plan,** 299 riyals. Zid's help article on markets gives one market on Rise, two on Growth and five on Professional. Its Saudi pricing page gives Rise at 99 riyals a month and Growth at 299.
- **(c) Neither.** Zid's per-market questions stay open.

**My recommendation:** (a) first, then (b) only if the development store has no markets. You, or your local agent with your account, would sign up, save each settings page as it shows, and stop before any payment or document.

*Changed on 27 October 2026, after your report from Yemen:* Zid's sign-up code doesn't reach you, and no purchase or verification completes. So (a) and (b) can't be done from Yemen. **My recommendation is now (c),** with Zid's questions in section 5 sent by email. Zid's per-market questions stay open, and phase C marks them as not stated for Zid.

**Answer:** a, then b if needed / a only / b / c.

*Done on 28 October 2026:* your local agent looked at Zid's public demo store and at a development store, and pushed what it saw to `other-product-class`. Neither store shows Zid's markets screens: Zid keeps them behind a setting only Zid turns on. Of Zid's 23 gaps:
- **10 are answered.** Seven of those answers rest on the dashboard's complete list of routes, which holds no page under a market for those settings. An agent that didn't record them is auditing them.
- **10 are narrowed.** Only one could still change an S-02 decision: who checks a store's country after it changes (S02-ZD-G30).
- **3 can't change a decision,** and are closed.

## 3. BigCommerce: a free trial store (5 of its 7 gaps)

BigCommerce's pricing page says "Start with a free trial", and its Help Center describes the trial's sign-up form. On a trial store, your local agent would save:
- what sign-up asks for;
- the store's country and localization settings after creation;
- the checkout's address form for buyers in different countries;
- the returns settings;
- BigCommerce Payments' sign-up, up to its first request for a document.

**My recommendation:** yes. It costs nothing.

*Changed on 27 October 2026:* **wait for phase C.** None of these five gaps is expected to change an S-02 decision, and whether BigCommerce's sign-up works from Yemen isn't known. The trial is worth a run only if phase C finds a decision that turns on one of them.

**Answer:** yes or no.

*28 October 2026:* your local agent is capturing BigCommerce into `other-product-class`. When it is pushed, the gaps that could change a decision are read first.

## 4. WooCommerce: a test store (2 of its 5 gaps, and part of the other 3)

WooCommerce is free software, so a test store needs only a WordPress host. Your local agent would record two things:
- what changing the store's country does once the store has orders and tax rates;
- whether a market can have a domain of its own.

Connecting WooPayments on the same store would show what its sign-up asks for by country. WooPayments offers a test account that "requires no personal information" and runs only in test mode, so this needs none of your details. The documents a real account is asked for show only on a real sign-up, stopped at the first request.

**My recommendation:** yes, after the questions in section 5, which may answer most of it first.

*Changed on 27 October 2026:* **not yet.** WooCommerce's own code, which we hold at a fixed version, can settle part of this first, at no cost to you: which settings it has at all. A test store is worth it only for what the code can't show, and only if phase C needs it.

**Answer:** yes or no.

*28 October 2026:* your local agent is capturing WooCommerce into `other-product-class`, as for BigCommerce.

## 5. Questions to the platforms (what no store shows)

Some questions only the platform can answer, such as:
- which company contracts with a merchant in each country;
- which tax its fees carry;
- which countries it won't serve;
- where it keeps data.

They are written out below, per platform, ready to send. The replies are the platforms' own words. Forward them, and they are held as evidence, dated.

**My recommendation:** send all four. *(28 October 2026:)* five, with Shopify's.

*Changed on the evening of 28 October 2026:* Zid's list is shorter, and each question names the subject that needs it. Only Zid's first question, Shopify's first, and the WooCommerce and BigCommerce questions on checks bear on S-02. The rest serve later subjects. Sending them all at once costs you one message per platform. Nothing waits on any of them.

**Answer:** send, don't send, or send some (say which).

### To Zid

*Rewritten on 28 October 2026,* after your local agent's captures. The questions they answered are gone.
1. For a store whose Business address country is outside Saudi Arabia, such as Kuwait, the UAE, Oman, Bahrain, Qatar, Egypt or Syria, does Zid check that country and address after they are saved, and with which documents? On a development store, Kuwait saved once the form's district and street were filled in, and the store's address then read `is_address_confirmed` true, with no step after the save. (S02-ZD-G30; S-02, and S-07 on verification)
2. In each of those countries, which Zid company contracts with the merchant, and under which terms? The subscription checkout links zid.sa's terms for each of them; zid.eg's terms name Zid Egypt. (S02-ZD-G31; S-03)
3. Which tax do Zid's transaction fees, Zid Pay's fees and app fees carry for a store in each of those countries? The subscription checkout's VAT already varies by the store's country. (S02-ZD-G32; S-05)
4. From which countries can a merchant not open a Zid store at its public sign-up? A store's Business address offers 162 countries. (S02-ZD-G33; S-07)

### To WooCommerce

1. WooCommerce's terms name the company a merchant contracts with by whether the merchant resides in the "Designated Countries". Which of the merchant's records decides that: the account's address, the billing address, or the store's country? Once a WooPayments account exists, where is its country held? (S02-WC-G01)
2. When a merchant's answer to WooPayments' "Where is your business located?" differs from the store's country, is either checked, and by whom? (S02-WC-G06)
3. Which documents or checks does WooPayments' business verification ask for, and do they differ by the merchant's country? (S02-WC-G07)
4. If no test store is looked at (section 4): once a store has orders, tax rates or WooPayments, can its country still be changed, and what does a change carry to other settings? Can a market be served on a domain of its own? (S02-WC-G03, G08)

### To BigCommerce

1. Which taxes does BigCommerce add to its own fees, and what decides them: the billing address, the VAT details, or the store's country? (S02-BC-G10)
2. Can a store sell in one storefront or channel through a business other than the merchant's own, or through a merchant of record? (S02-BC-G14)
3. Which documents or checks does BigCommerce Payments ask for, and do they differ by the store's country? (S02-BC-G06)
4. If no trial store is looked at (section 3): is the store's country checked by anyone? Do a new store's units and date formats follow its country? Do the checkout's address fields, and which are required, follow the buyer's country or the storefront? Can return settings differ by storefront? (S02-BC-G09, G11, G12, G13)

### To Shopify

*Added on 28 October 2026,* from what the runs for H-006 to H-008 couldn't reach:
1. When a store that uses no financial services, such as Shopify Payments, switches its business entity to one in another country, does Shopify check the new country, or the new store address, after the change saves? If it does, who checks, and against what? On a development store, the switch saved with no step asking for verification. (S02-SH-G14)
2. For which business types are Managed Markets, and a business entity per market, offered? On a store in the United States, Managed Markets' eligibility named only the missing Shopify Payments. Shopify Payments' set-up asks for a valid SSN or ITIN, which no capture holds. (S02-SH-G15)
3. How many markets of each kind (country or region, B2B, retail, channel), and how many submarkets, can a store hold on each plan? On a Basic development store, a second B2B market, a second retail market and a submarket three levels deep each saved, with no limit shown. (S02-SH-G16)

### To Salla

1. In which country or countries are a store's data and its customers' personal data stored and processed, and from where may they be accessed? Salla's privacy policy names its data protection contact: dataprotection@salla.sa. (S02-SA-G05, narrowed on 28 October into S02-SA-G17; S-08)
