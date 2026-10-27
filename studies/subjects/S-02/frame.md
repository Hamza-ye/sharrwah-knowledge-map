# S-02, what a market is: the frame

**What this file is:** the coordinator's frame for S-02, written before any of its agents run (`PLAN.md`, Stage 4, and section 6, steps 0 and 1). It sets out:
- the subject;
- its root decisions, named from the platforms' own top-level statements;
- the concerns it starts from;
- where it meets other subjects;
- how it runs, and its budget.

The coordinator's readings are marked as readings. Every quote below is a line of the concern map, which was checked word for word against its source (`studies/concern-map/README.md`), or a held file at a commit.

## The subject

- **The question:** "What fills 'a market' in Sharrwah: which settings bind per market (among them address formats), and who sets each?" ([`subjects.tsv`](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/subjects/subjects.tsv?plain=1#L3))
- **Why it is expensive to change:** "data model: every per-market binding (S-01's holding arrangement among them) hangs on it" ([the same row](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/subjects/subjects.tsv?plain=1#L3)).
- **The founder's mark at G2:** evidence, as for all ten subjects (`founder-decisions.tsv`).
- **Step 0, what kind of subject it is:** product. It asks what Sharrwah's data model holds. *Reading:* which countries Sharrwah serves, and when, is the founder's business question, and the company's own country is S-03's. Neither is decided here. This subject decides where such answers are held, and what hangs on them.
- **A decision already rests on it.** The founder decided on 26 October that "Who holds sellers' money is a market's setting, with C everywhere at launch (E1)" ([`founder-decisions.tsv`](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/founder-decisions.tsv?plain=1#L19), the S-01 follow-on on building ahead). That setting needs a market to be held on.

## Two senses of market in the platforms' words

The platforms use the word, or the thing, in two senses.

**1. The country a store belongs to.** A store has one country, and it binds the store:
- **Shopify, its terms:** "You must maintain an accurate location in the administrative console of your Shopify Store. If you change jurisdictions you must promptly update your location in the administrative console." ([concern map, SH-C-006](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/shopify/statements.tsv?plain=1#L1271))
- **Salla, on creating a store:** "دولة المتجر حدد من أي دولة تسجل متجرك، لأن ذلك يحدد الوثائق الحكومية لتهيئة متجرك وفق أنظمتها." (in English: store country, specify which country you register your store from, because that sets the government documents for setting up your store under its rules; [SA-C-006](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/salla/statements.tsv?plain=1#L83))
- **Zid, on changing it:** "في حال قيام التاجر بنقل أو تغيير دولته في إعدادات المتجر إلى دولة أخرى، يشترط تصفير رصيد المحفظة أولاً" (in English: if the merchant moves or changes their country in the store's settings to another country, the wallet balance must first be brought to zero; [ZD-C-033](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/zid/statements.tsv?plain=1#L230))
- **WooCommerce:** "From your store’s general settings page, you can enter your business address, define the regions you will sell and ship orders to, enable tax calculations and coupons, and select the currency your shop will use for sales." ([WC-C-030](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/woocommerce/statements.tsv?plain=1#L535))

The country is drawn from the countries a platform serves:
- **Shopify:** "Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account." ([SH-C-006](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/shopify/statements.tsv?plain=1#L1270))
- **Salla:** "Primary markets are Saudi Arabia first, followed by the GCC." ([SA-C-167](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/salla/statements.tsv?plain=1#L1987))
- **Zid:** "حاليًا زد يخدم التجار المتواجدين في السعودية ودول الخليج فقط من جميع الجنسيات" (in English: Zid currently serves merchants located in Saudi Arabia and the Gulf states only, of all nationalities; [ZD-C-032](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/zid/statements.tsv?plain=1#L226))

**2. The markets a store sells into.** A store defines groups of buyers, and sets each one up:
- **Shopify:** "You can use Markets to manage how different customers experience your store based on their location, customer group, retail location, or sales channel." ([SH-C-106](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/shopify/statements.tsv?plain=1#L1930))
- **Salla:** "ميزة الأسواق المتعددة تمكنك من إنشاء نسخ مخصصة من متجرك الإلكتروني لكل دولة تستهدفها أو منطقة أو مدينة" (in English: the multiple markets feature lets you create customised copies of your online store for each country you target, or region or city; [SA-C-165](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/salla/statements.tsv?plain=1#L1976))
- **Zid:** "خاصية الأسواق تتيح لك عدد من الأسواق حسب باقتك" (in English: the markets feature gives you a number of markets by your plan; [ZD-C-034](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/zid/statements.tsv?plain=1#L235))
- **WooCommerce:** "This option lets you limit which countries you are willing to sell to." ([WC-C-030](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/woocommerce/statements.tsv?plain=1#L534))
- **BigCommerce:** "A channel is anywhere a merchant sells their products." ([BC-C-038](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/bigcommerce/statements.tsv?plain=1#L209)) And "“Multi-Storefront” or “MSF” means the ability to manage multiple unique Storefronts within one Store." ([BC-C-039](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/bigcommerce/statements.tsv?plain=1#L216))

**The two senses meet.** Shopify's home country is the second sense's default: "Your backup region is automatically set to your store's home country when you create your store." ([SH-C-113](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/shopify/statements.tsv?plain=1#L1974))

**And a market of the second sense can carry who processes payments.** In Shopify's schema, a business entity is "A legal entity through which a merchant operates.", and "objects can be assigned to a business entity to determine payment processing" ([observed-sh, the Admin API's `BusinessEntity`](https://github.com/Hamza-ye/observed-sh/blob/febbf6c98a1f2a464bb92bd97856b8ba070f3185/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L217); the objects are `Market`).

*Reading:* Sharrwah's own records use the first sense. "C, with the three defaults, in every market at launch" ([Decision 1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/founder-decisions.tsv?plain=1#L16)) speaks of the countries Sharrwah serves sellers in. The platforms show that a setting such as who processes payments can also bind to the second sense. Which of the two carries each setting is what this subject decides.

## The root decisions

Each is a question of the form "who or what fills X" ([`PLAN.md`, section 6, step 1](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/PLAN.md?plain=1#L241)). Phase B splits each into the facets that can change it, and anything else stays as a note.

| | Root decision | What it asks |
| --- | --- | --- |
| **RD1** | **The store's own country** | What fills a store's country; who sets it, checks it, and can change it, and on what conditions; what binds to it; and how the countries a platform serves are held |
| **RD2** | **The markets a store sells into** | Whether a store holds one market or several; what defines one (a country, a region, a city, a group of customers, a location, a channel); who creates them, and within what limits, such as a plan |
| **RD3** | **What binds per market, and who sets it** | Which settings take a value per market, and in which sense of market; which hold for the whole store; which are set by the platform and which by the seller. Among them: currency, languages, domains, prices and product availability, taxes, payment methods and who processes payments, shipping, and address formats |

*Reading:* RD3 decides where each setting is held, not its value. The value of each setting belongs to the subject that covers it (below).

## The concerns it starts from

From the concern map, the index subjects draw from, and from the pilot, as Stage 4's "From what is recorded" asks ([`PLAN.md`](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/PLAN.md?plain=1#L171)). `method/seed_subject.py` copies their statements into each platform's `recorded.tsv`; `concerns.tsv` in this folder lists them, with the root decisions each bears on.

| Platform | Concerns | How it is read |
| --- | --- | --- |
| Shopify | SH-C-106 Markets; SH-C-113 backup region; SH-C-006 merchant location at sign-up; SH-C-110 Managed Markets; SH-C-111 international domains and geolocation; SH-C-037 catalogs; SH-C-032 languages; SH-C-033 domains; SH-C-002 contracting party by billing address | In full: the held Help Center's Markets and international sections, the Admin API's market and business-entity types, and the admin's markets pages |
| Salla | SA-C-165 Markets; SA-C-167 countries served, which also holds SA-C-006's statement on the store's country; SA-C-166 countries, cities and districts; SA-C-065 customer addresses; SA-C-007 domains; SA-C-008 languages; SA-C-230 legal entities per country | In full: the held help articles on markets and on stores outside Saudi Arabia, the dashboard's features and navigation, and the API's store scopes |
| Zid | ZD-C-032 countries served; ZD-C-033 store country, operating countries and cities; ZD-C-034 markets; ZD-C-050 languages and currencies; ZD-C-030 contracting entity | From what is recorded; further only where a cause or a gap needs it |
| WooCommerce | WC-C-030 selling and shipping locations; WC-C-004, only its lines saying the list is per country; WC-C-010 WooPayments by country; WC-C-099 countries and continents; WC-C-053 more than one currency; WC-C-108 international extensions; WC-C-046 geolocation; WC-C-023 contracting entity | From what is recorded; the release's address formats (`includes/class-wc-countries.php`) are read, since the subject's question names them |
| BigCommerce | BC-C-038 channels; BC-C-039 Multi-Storefront; BC-C-047 store profile and settings; BC-C-048 locales; BC-C-074 currencies; BC-C-075 geography; BC-C-079 contracting entity | From what is recorded; further only where a cause or a gap needs it |

The draft row cited SA-C-165, SA-C-167, ZD-C-033, SH-C-110, WC-C-010, WC-C-004 and SA-C-065. All are kept. What the frame adds is the core markets concerns the row missed (`STATE.md`), and the concerns that show what binds to a store's country.

**Why Shopify and Salla are read in full:** their held evidence is the deepest, and the plan reads them first and in full (`PLAN.md`, Stage 4). The other three come from what the concern map recorded, as the founder asked on 24 October.

## Where it meets other subjects

*Reading,* the coordinator's split, for phase C and the register to test:
- **S-01:** who holds sellers' money is a market's setting (E1). S-02 says which market carries it.
- **S-03, the contracting company:** Shopify keys its contracting party on "the billing address of your Store" ([SH-C-002](https://github.com/Hamza-ye/sharrwah-knowledge-map/blob/dadf943395603154a03a8ac341048807a7f9caa8/studies/concern-map/platforms/shopify/statements.tsv?plain=1#L1243)). S-02 records what such bindings key on; S-03 decides what fills them.
- **S-04, S-05, S-09 and S-10:** payment methods, tax, currency and delivery each take values per market. S-02 decides where each is held; each of those subjects decides its value.
- **S-07:** which countries are served, and the screening behind it. S-02 decides how the served countries are held, not which they are.

## How it runs

The pilot's five steps, under Stage 4's changes (`PLAN.md`, Stage 4, and section 6):

| Step | What | Who | Writes |
| --- | --- | --- | --- |
| 1A | What each platform states, under the bullets of `bullets.tsv` | one agent per platform, blind to the others | `<platform>/statements.tsv`, `terms.tsv`, `absences.tsv`, `gaps.tsv`, `citations.tsv`, `notes.md` |
| | Capture and kinds | the coordinator | captures, then `kinds.tsv` by the checker |
| 1B | Variation points per root decision, and variants | in parts, each a fresh agent, one after another for the same root decision (`b/parts.tsv`) | `b/<root decision>/`, joined by `method/merge_slices.py` into `variation-points.tsv`, `variants.tsv` and `notes-b.md` |
| 1A2, 1A3 | Closing the gaps a root decision needs, and auditing claims of absence it rests on | one agent per platform, where needed | `<platform>/a2.tsv`, `absence-audit.tsv` |
| 1C | Cause, coexistence and what follows, per root decision | per root decision, in parts where it is large | `c/<root decision>/`, joined into `analysis.tsv` and `notes-c.md` |
| 2 | The Yemen row per root decision (section 6, step 6) | the coordinator; each fact checked against its quote first | in the register |
| 3 | The scenario walk per root decision (section 6, step 7) | the coordinator | in the register |
| 4 | The register | the coordinator | `register.tsv` |
| 5 | Independent review | one agent that produced none of it | `review.md` |
| 6 | The quote check, and the report for G3 with the cost against the budget | the coordinator | `reports/S-02.md` |

**Running the agents.** The pilot's phase A started five agents at once on 12 October, and four stopped at the usage limit within 35 minutes. Two of them had written nothing, so their 75 million tokens were lost and they were run again from the start. Resuming a paused agent cost 0.2 to 0.7 million each time (the pilot's transcripts; [the method report, section 12](../S-01/method-report.md#12-what-a-subject-costs)). So:
- no more than two agents run at once;
- an agent writes each finding to its files as soon as it is checked;
- an agent that stops is resumed, never started again from nothing; where its context has grown large, a fresh agent continues from its files and notes, so nothing is read twice;
- each agent's cost is measured after its first steps with `method/count_tokens.py`.

## Budget

**700 million agent tokens,** counted by `method/count_tokens.py` (the founder, 27 October: `founder-decisions.tsv`). The first budget, 200 million, was passed by a quarter in phase A, whose two agents read with contexts of up to 780 thousand tokens ([`method-report.md`](method-report.md), section 2). The budget never costs evidence about the references: past a quarter over it, the cost is reported to the founder and the work goes on (`PLAN.md`, section 8).

| Step | Millions |
| --- | --- |
| Spent by 27 October, 03:00 UTC: the briefs' inspections, and phase A for all five platforms (measured) | 534 |
| 1B, in nine parts, and its second pass | 150 to 300 |
| 1A2 and 1A3, where a root decision needs them | 50 to 100 |
| 1C, per root decision | 90 to 150 |
| Inspection of the later briefs | 15 to 30 |
| 5, the review | 40 to 80 |
| **All of S-02, projected** | **about 880 to 1,190** |

Phase A cost 504 million, against the 325 to 375 million this table first set for it ([`method-report.md`](method-report.md), section 4). The rest is projected from phase A's measured cost per request, and is measured again after phase B's first parts. The projection passes the budget plus a quarter, 875 million. When the spending does, the cost comes to the founder with a new projection, and the work goes on (`PLAN.md`, section 8).
