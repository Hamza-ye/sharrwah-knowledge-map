# Held pass, Shopify, batch SH-70: notes

80 entries of `pricing-page-data` (effort high), evidence at observed-sh@e38dc17e3, in `structures/shopify/pricing-page-data/20261031T003815Z-shopify-com-pricing-by-country/items.jsonl`. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-70`).
- **1 to 24:** the rest of www.shopify.com/ae-ar's POS page (items.jsonl line 3):
  - `posLiteVsProPlans`, PosLite and PosPro with their features (1 to 13);
  - 'كيفية البدء' and its three blocks (14 to 17);
  - the two promo cards (18, 19);
  - the five FAQs (20 to 24).
- **25 to 42:** www.shopify.com/ae's international pricing page (line 4): its terms entry (25, the same words as eg's), then the hero, the fee table and its two FAQs, each the same on the 18 English sites but for the Shopify Payments row (29, ae alone).
- **43 to 80:** www.shopify.com/ae's plans page (line 5): its terms entry, the hero, the four plan cards with their features, the always-included block, the POS Pro card with its three features, and the Agentic card. SH-71 begins with the Agentic card's features.

**Placed:** 80 entries in 147 lines: 76 entries on capabilities, 3 `new` (the new thing SH-68 named), 1 `out` (the heading 'كيفية البدء'). 42 entries take more than one line. Supports: 120 `core`, 25 `shows`, 1 `own-service`; no `extension-point` or `outside`; no filler. 47 lines carry qualities.

**Sources read:**
- the brief and what it names: the evidence map; the rulings, the last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run"; observed-sh's `README.md`, `docs/READING.md` (fetch runs, structures, indexes), `docs/GAPS.md` (nothing on these pages), `structures/README.md`;
- `structures/REGISTER.tsv` row 141; `index/ledger-summary.tsv`'s shopify-com-sitemaps rows; `selection.tsv`'s row; `show --meta`;
- SH-68's and SH-69's notes and placements first, with their coordinator's checks, and kept to their R0 to R11 and rules 1 to 7;
- items.jsonl line 3 (the ae-ar POS page) for the pruned parts of my entries' sections, and the www.shopify.com/ae POS page (`howToGetStartedContent`, `promoCardsContent`, `faqContent`) to clarify only. Every line's terms and quotes are its own entry's;
- the model: `earlier`; `cells` for every capability placed on and the leads; `caps --terms` for migration, getting started, experts, transfers, pickup, discounts, returns and exchanges, reports, inventory reports, lifetime value.

## Rules followed

**SH-68's and SH-69's rules, as kept:**
- R0: a line on every read site of its language takes no site; a line on some takes those sites, after its plans. Entries labelled with the three Arabic sites or the 18 English ones take none. The others take their labels: 5, 20 to 23 (ae-ar), 25 (ae, eg), 29 (ae), 43 to 47, 50 to 53, 55, 57, 58, 60, 61, 65, 66, 68 to 70, 75, 76 and 80.
- R1: the two terms entries (25, 43), three `core` lines each.
- R2: the plan cards and their features, the always-included block, the POS Pro and Agentic cards (43 to 80), each on the capability SH-68 placed its Arabic twin on (its lines 34 to 93).
- R4: the POS page's lists, blocks and promo cards (1 to 19).
- R5: the international fee table (26 to 40), with the coordinator's move of managed international pricing to CM-MKS-006 (32).
- R6: the FAQs (20 to 24, 41, 42).
- R7: the qualities.
- SH-69's rule 5: a list ending in 'والمزيد' or naming things 'مثل' (like) gives examples, which take no line (20, 21).

**Entries 1 to 13 take SH-69's lines for 71 to 83.** `posLiteVsProPlans` holds the same two lists, in the same words, as SH-69's `posLiteVsProContent.plans`. Each line repeats its twin's capability, support, scope, terms and quality, and its reading names the twin.

**Rules for kinds R0 to R11 and rules 1 to 7 don't cover, for the coordinator to align with SH-71 to SH-79:**
1. **An FAQ whose answer lists the things of two offers** takes a line per thing, each with its offer's scope (22). The things included 'مع كل باقة Shopify مدفوعة' take the four plans; those 'يضيف اشتراك Pro' takes POS Pro. Where both offers name a thing of one capability, the capability takes a line for each: CM-POS-001, CM-CUS-001 and CM-RET-003. This applies the ruling after SH-69 and the one after SH-34.
2. **'Every plan', 'every paid plan', 'all plans' on the POS page** ('كل باقة Shopify مدفوعة' in 22, 'جميع الباقات' in 23) are read as the four plans, Basic;Grow;Advanced;Plus. That is how R4 has 'متضمن في كل باقة'. The POS page's summaries also list Starter and Retail (SH-69), and whether 'every paid plan' takes them in isn't stated.
3. **A thing stated 'depending on the plan' with no plan named** takes the site alone (23's CM-CHN-001, 'اعتمادًا على الباقة التي تختارها'). This is the ruling after SH-69: its condition is its own, but it isn't named.
4. **A provider statement inside an FAQ is `own-service`,** beside the FAQ's `shows`. In 21, 'حامل iPad المرن من Shopify' names Shopify as the stand's provider, so CM-POS-002 is `own-service`, as its cell holds Shopify's sale of the equipment (SH-S-7269). 'قارئ بطاقات Shopify' and 'أجهزة Shopify' are brands in names, which name no maker. The English twin reads 'Shopify's flexible iPad stand'. `shows` is the other reading (below).
5. **A block's subhead that names its things 'from X to Y'** ('بدءًا من … وصولاً إلى', 'ابتداءً من … وصولاً إلى') states what the block offers, with no 'والمزيد', so each thing takes its line (SH-69's rule 5). 16's support takes CM-ONB-003 and its POS migration apps CM-MIG-005, beside R4's CM-ONB-004. 18's two ends are both POS hardware (CM-POS-002), so they take one line.
6. **A block's narrower thing beside R4's line.** 17's 'قم بإضفاء طابع شخصي على نظام POS الخاص بك باستخدام التطبيقات' is apps personalizing the POS, so it takes CM-POS-004 (app extensions in the POS app) `shows` beside R4's CM-APP-001 (rule 2, a broad lead doesn't end the search). Its 'خبراء Shopify' takes CM-PTN-005 `shows`, the experts merchants hire (the ruling after SA-25).
7. **A promo card's figure is a quality** (19, 'عبر 1,000 متجر'), as R7 has 'a number a card claims'.
8. **A section heading with no subhead, over blocks of several capabilities** (14, 'كيفية البدء': the account and its free start, the store's setup, apps), names only a grouping: `out`, as R3 and R10 have Core features and Customization.
9. **The POS Pro card's scope.** SH-68 gave the plans page's POS Pro card (posProCard) its site alone (SH-E-a090e3ae); SH-69 gave the POS page's PosPro plan 'POS Pro' and its site (SH-E-abc35c09). I kept each kind to its earlier batch: 76 takes its sites, 5 takes 'POS Pro;www.shopify.com/ae-ar'. The coordinator may align them.

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 3 lines: 52, 57 and 65 (SH-E-36085b8c, SH-E-cf7c4e76, SH-E-8d1255c6), the Basic, Grow and Advanced cards' credits on www.shopify.com/ae and ng.
- **English words:** 'Earn up to $4,500 in credits', 'Earn up to $6,500 in credits' and 'Earn up to $8,000 in credits', with the popover's 'Get 0.5% back on sales' and 'Add a domain, get US$20'. The key is `gmv_rewards_signup_redesign`. The Arabic words, its place of its own (the comparison table's row Earn 1% back on all sales), the proposed domain A, area PLN and parent CM-PLN-004 (or CM-PLN-001), and the terms searched are in SH-68's notes.
- **The leads' cells, read:**
  - CM-SFR-008 (by 'domain'): domains; the domain credit is a way to earn the credit;
  - CM-CHK-002 (by 'add', 'item'): the buyer's cart;
  - CM-PTN-008 (by 'earn', 'sale'; it holds nothing on Shopify): a referral programme's commission on plans a member brings, not credits on the merchant's own sales;
  - CM-PLN-001 and CM-API-001 (by Grow, Advanced): the plans and the API.

  None holds the platform's credits to the merchant.

## Entries I couldn't tell, and what would settle each

- **14, 'كيفية البدء', `out`:** CM-ONB-004 `shows` is the other reading, if the heading names the store's onboarding as one thing. Its cell's own reading cites no 'setting up' statement that doesn't show the admin's steps (below).
- **16 on CM-ONB-004 `shows`** (a CHANGES line, below).
- **17 on CM-POS-004 beside CM-APP-001:** rule 6 above. CM-APP-001 alone, as R4 says, is the other reading.
- **19's figure as a quality** ('stores: 1,000 متجر'): the card may name one business's 1,000 stores, as a case study's demo. Its link, /ae-ar/pos/demo#watch-demo, isn't in this structure.
- **20's 'رسوم المعاملات' on CM-PLN-003:** 'a percentage deducted automatically from each sale through Shopify', which 'depends on the plan', matches CM-PLN-003's definition, a fee on sales by plan. The other reading is the in-person card rates (CM-PAY-021), since CM-PLN-003's cell holds no transaction fees on POS orders (SH-S-0276), and the FAQ is about POS's cost. Both lines are `shows`. A help page on POS's fees would settle it.
- **21 on CM-POS-002 `own-service`:** rule 4 above. `shows` is the other reading, if 'من Shopify' and 'Shopify's' are read as the stand's brand, as the cell's reading has the Shopify Hardware Store's name (SH-S-7270). The cell is `own-service` either way.
- **22 and 23's 'every plan' as the four plans:** rule 2 above. The POS page's own words for Starter's and Retail's point of sale would settle it (SH-69 placed them).
- **24's 'Shopify Payments' on CM-PAY-021:** the answer recommends it with POS, and links Shopify Payments for POS's supported countries. CM-PAY-002 (the payment service itself) is the other reading. Both are `shows`.
- **66, Plus's price:** written from its `priceLabel` template, '{{startingAtText}} {{price}}{{cadence}}' with 'from': 'from $2,300/mo'. The bytes hold the parts, not the rendered words.

## A structure whose items and sources disagree

- **The Basic annual price** (43, 45): the plans page's terms give 'basicAnnualPrice: <span>$24.00 USD</span>' with a 25% annual discount, while www.shopify.com/ae's Basic card gives $29 a month paid yearly. This is the same as SH-68 noted for ae-ar. Each line quotes its own entry.
- **The always-included block's fourth card** (75) is keyed `pos` and is a `hoverVideo`, but on these 12 sites it holds support ('24/7 support'). The content governs: CM-ONB-003, as R2 has it.
- **The items and the entries agree:** the entries are the items' decoded loader data. I didn't print the WARC records.

## What the sources state that no entry holds (for the second stage)

- **The ae-ar POS page (items.jsonl line 3), pruned by the selection's rule (`button`, `cta`) or left unwrapped:**
  - the promo cards' buttons, 'تعرّف على الأجهزة' (/ae-ar/pos/hardware) and 'شاهد العرض التوضيحي' (/ae-ar/pos/demo#watch-demo): leads for CM-POS-002 (the hardware store) and the POS demo;
  - the get-started call to action 'ابدأ الآن', to admin.shopify.com/signup with `signup_types[]=pos`, `paid_trial_experience` and the treatment `e_06d1ad5d27d16046cc6d829de669769b__treatment`: a sign-up from the POS page, a lead for CM-ACC-001;
  - the FAQ heading 'الأسئلة الشائعة' (`faqContent.heading`), CM-ONB-003 `shows` elsewhere (SH-68's R6).
- **The FAQs' links** (in the entries; their pages aren't in this structure):
  - 21's /ae-ar/pos/hardware ('تصفح أجهزة Shopify') and help.shopify.com/manual/sell-in-person/hardware#model-number-quick-reference: the hardware's sale and its compatibility, for CM-POS-002;
  - 24's help.shopify.com/manual/sell-in-person/getting-started/setup-payment-method/shopify-payments-pos#supported: the countries of Shopify Payments for POS, for CM-PAY-021 and CM-POS-002.
- **Kept from SH-69's leads:** POS Pro's staff performance and the endless aisle still have no capability. This batch's POS lists name neither.
- **www.shopify.com/ae's plans page (line 5):** I didn't read its pruned parts. SH-68 lists those of the ae-ar twin.

## The checker's lines, read again

- **`CHANGES CM-ONB-004@shopify holds nothing: becomes held`, by line 29 (16, SH-E-b871f05f, 'قم بإعداد متجرك'):** kept, as SH-68's R4 decides this block: "'set up your store' is CM-ONB-004". The line is `shows`, so the cell becomes held with no placement (`not-stated`).
  - Against it: the cell's reading cites none of the Shopify hits on setting up, since 'None shows steps or a checklist the admin gives a new store', and this block shows none either. It names help 'في كل خطوة', support and POS migration apps.
  - If the coordinator keeps that reading, the line goes and the block keeps its CM-ONB-003 and CM-MIG-005 lines.
- **`CHANGES CM-SHP-020@shopify gains core`, by lines 77 and 79 (35, 36):** kept. These are the English twins of SH-68's HS code classification and import restrictions management (SH-E-7faf9fda, SH-E-f37b6426), which the coordinator's check after SH-68 kept as `core`.
- **`NOTE own-service on CM-POS-002`** (21): rule 4 above.
- **`NOTE` on a product named with the platform's brand** (lines 64, 67, 68, 83, 84 and 91, header as line 1): Shopify Managed Markets (26, 30, 38, 42), Shopify Payments (29) and Shopify Protect (38). Each is `core` by its cell's place, not by its name, as SH-68's check has them:
  - Managed Markets: its routes managed and :id/managed;
  - Shopify Payments: its route and plan rows;
  - Protect: its route shopify-protect.
- **`NOTE` on footnote marks** (lines 75 and 76: 34, 'Discounted international shipping labels*'): the reading quotes its footnote, '*Shipping rates apply separately.', from its row (30).
- **`NOTE` on a new thing whose entry has leads** (lines 107, 113, 122): read, above.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 3 lines.

## Problems with the brief or the script

- **`earlier` printed no line for 1 to 13,** though SH-69's lines 157 to 180 hold the same lists, and SH-69's terms hold the label 'البيع الشخصي العادي' (its line 157). The message said `earlier` prints them. I read SH-69's placements for its entries 71 to 83 directly (`held/batches/SH-69.txt`, lines 71 to 83).
- **A quote can't hold a straight apostrophe** inside single quotes without ending the quote. The English entries' 'buyer's', 'You've', 'World's' and 'You're' are therefore quoted around those words or not quoted (29, 39, 41, 44), and 75's term is 'best checkout'.
- **No B-extent conflict:** I found no rule of the brief that reads differently from B-extent.md, beyond the two the brief states (qualities wider than B-extent's list; the rulings).

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes beyond earlier batches'.** CM-SHP-020's `core` repeats SH-68's.
  - CM-ONB-004's `shows` line ('قم بإعداد متجرك', set up your store) stands under SH-68's R4. The cell is `core` from SH-36's Launch Check app, so its reading keeps the setup steps apart.
- **Rules 1 to 9 stand for SH-71 to SH-79.** Rule 9's two kinds of POS Pro scope are one rule (the ruling after SH-70): the card, the offer itself, takes its site, and what comes with POS Pro takes 'POS Pro'.
- **New thing:** the subscription credits again, on three of www.shopify.com/ae's and ng's cards.
- **`held_entries.py earlier`** now finds a label held as a whole term, so SH-69's line 157 is printed for this batch's first entry.
- **Cost:** 9.7 million tokens over 54 requests, about 121,000 an entry. The context stayed under 300,000 tokens.
