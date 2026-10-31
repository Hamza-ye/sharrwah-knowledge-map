# Brief: the qualities pass, what the five platforms state about their own qualities (Stage 4A)

**What this is.** `PLAN.md`, Stage 4A, the qualities pass (31 October): "It reads what the class states on how well, how safely, or within what bounds it does what it does. It reads from the evidence's side, through each repository's guides first, for each platform. A quality is one of four things:
- a commitment, such as uptime or a support response;
- a bound, such as a rate limit, a size or a scale;
- an attestation, such as a certification or an audit;
- how data is kept: where, by which subprocessors, isolated how, encrypted, and kept how long.

Its kinds are the characteristics of ISO/IEC 25010:2023, with three named: isolation between stores, where data lives, and identity. Each quality is quoted at its commit, on the capability it bears on."

**Why it runs.** The model's qualities were never read as such. Its parts recorded them beside the capabilities, by `B-extent.md`'s line: "**a quality:** a limit, a certification, an uptime or a data location a platform states, on the capability it bears on". The held pass widened it: "or a value of the kind the model's `qualities.tsv` records (a maximum, a rate, a fee, a price, a duration)" (`briefs/H-held.md`, rule 5). So most of the model's rows are the plans' prices and allowances, and few say how stores are kept apart, where data lives or who may sign in (`architecture/plan-review.md`, APR-7). This pass reads the platforms' own statements for the four things, kind by kind, so that architecture's first decisions start from evidence.

You draft one row per finding. The coordinator checks every row and lands it in the model. Its design is in `briefs/QL-qualities-design.md`, which you don't need to read.

**Your part.** Your message names it (such as `QL-SA`), with its platform, its kinds, the commits fixed for the run, and your effort. The parts are listed in `studies/class-model/qualities/parts.tsv`.
- `python3 -I method/ql_qualities.py asks --part <part>` prints your asks (below): for each, its kind and question, the model's quality rows of your platform that the coordinator's labelling already marks as that kind, the capabilities the kind lands on by default with your platform's cells (held or not, their readings), and the places the coordinator's table of sources names for it.
- `python3 -I method/ql_qualities.py asks --part <part> --left` lists the asks your file has no row for yet.

**Effort:** your message names it. The founder, 30 October: "No agent runs at `medium` or `low` for reading evidence, reviewing, or making an engineering judgement: `high`, `xhigh` or `max`."

## Read only this brief and, in this order

1. **The evidence map,** `studies/class-model/evidence-map.md`: where to start, and the faults the tools have shown on your platform ("Found in the held pass").
2. **Your platform's guides, read whole once, at the start:**
   - Shopify (`/home/user/observed-sh`) and Salla (`/home/user/observed-sa`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `docs/OPERATING.md` and `structures/README.md`;
   - Zid, BigCommerce and WooCommerce (`/home/user/other-product-class`): `README.md`, `docs/OPERATING.md`, and your platform folder's `README.md` and `GAPS.md`;
   - this repository's own evidence, `evidence/product-class/README.md`, and for Shopify `evidence/shopify-engineering/README.md`.

   Then grep, never read whole: `structures/REGISTER.tsv`, `index/runs.tsv`, `index/run-notes.tsv`, `index/ledger-summary.tsv` and `index/ledger/*.tsv` where your repository has them, and each capture run's `manifest.tsv` under `evidence/product-class/runs/`. The founder's rule of 30 October: "what the evidence repositories hold is read through their own reading guides and indexes, not by search alone ... Search (method/held_index.py, method/corpus_search.py) follows the guides."
3. **Your asks,** by `asks --part <part>`.
4. **The model's rules:**
   - `studies/class-model/briefs/B-extent.md`, "Cells and evidence", with "Qualities and slot fillers";
   - `briefs/H-held.md`, rule 5, `scope`: "the plan, country, market, store or account the entry or its sources state it for, in their words, or empty".

   The rules marked (ruling, proposed) below are the coordinator's, each listed for the founder's veto. Where any other rule of this brief reads differently from `PLAN.md`, B-extent.md or H-held.md, those govern: say so in your notes.
5. **The tools,** by their headers and `--help`, not their code: `method/corpus_search.py` (`--brief`; `--runs-only` for Shopify's and Salla's runs, in seconds), `method/held_index.py <address>`, `method/warc_text.py`, `method/quote_check.py` (`--text SOURCE [LOCATOR]` prints a source's text as the checker reads it), and the model's `method/class_slice.py` (`caps --terms`, `search`, `key`) and `method/held_entries.py cells --platform <p> <cap_id> ...`.

## What a quality is, and what it isn't

**A quality** is what the platform itself states about how well, how safely, or within what bounds it does what it does: one of the plan's four forms, quoted above. Its `form` is one of:
- `commitment`: what the platform undertakes or reports about its service: uptime, a support response, notice before a change, the time to notify a breach;
- `bound`: a limit the system enforces, or a scale it states it reaches: a rate limit, a size, a timeout, a retention window, a count of things a store may hold, a peak it handled;
- `attestation`: a certification, an audit, an assessment or a test by a party other than the merchant, and its scope and date;
- `data-keeping`: where data is hosted and processed, by which subprocessors, how stores are kept apart, how data is encrypted, and how long it is kept.

**Its `basis`** says how the platform states it:
- `promised`: in terms, a service level or a policy;
- `enforced`: a limit in its docs, code or answers;
- `reported`: a figure of its own past, such as a status page's uptime or a peak it handled;
- `attested`: by a named third party.

A reported figure is filed under the form of what it measures: a past uptime is a `commitment`, `reported`; a peak handled is a `bound`, `reported` (ruling, proposed: `QL-R3`).

**Not a quality: the plans' terms.** `PLAN.md`, Stage 4A: "Prices, fees and plan allowances are the plans' terms, not qualities. The model's rows of them are relabelled by script and kept." You write no row for a price, a fee, a rate charged, a trial, a discount or a plan allowance. The line between an allowance and a bound is drawn by what the value measures, not by where it is stated (ruling, proposed: `QL-R1`):
- **a term** measures money, or a quantity of something the merchant buys or is granted with a plan: staff accounts, locations, storefronts, expansion stores, credits, catalogues;
- **a bound** measures the system's behaviour: requests in a time, a size, a time, a retention window, a maximum of records the platform enforces as a system limit. It stays a bound when it differs by plan: its plans are its `scope`. Shopify's plan table row "API rate limits: Standard, Standard, Up to 2x on select APIs, Up to 10x on select APIs" is a bound, scoped by plan.

**Not a quality either:**
- a mark of inclusion: "A mark of inclusion (a check, "Available", "Included", "Yes") is never a quality" (`H-held.md`, rule 5);
- a store's own value of a setting (H-held.md, rule 5: "A store's own value of a setting or a flag ... is never a quality");
- a feature's description without a measure, a limit or a commitment ("secure checkout" alone). Write it as `unclear` only where it may be the thing and its words don't settle it.

## The kinds: the checklist

Sixteen kinds, each with its asks. Each ask is a question your platform's statements may answer; your file holds rows for every ask your part names. The ISO/IEC 25010:2023 characteristic is a reading: this repository doesn't hold the standard, and its names here are from memory of the 2023 edition (functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety). The decisions are `architecture/plan.md`, section 3's first decisions: **D1** how stores are kept apart, and where their data lives; **D2** identity and permissions; **D3** money records and currency; **D4** markets and the seller's country; **D5** events and extension points; **D6** configuration. **S** means the kind drives none of the six, but feeds the quality scenarios of section 5.

| Kind | Plain name | ISO/IEC 25010:2023 (a reading) | Drives | Lands by default on |
| --- | --- | --- | --- | --- |
| `ISO` | Isolation between stores | security (confidentiality, integrity); reliability (fault tolerance); performance efficiency (capacity) | D1 | `platform` |
| `LOC` | Where data lives | security (confidentiality, accountability); no product characteristic names it: ISO/IEC 25012's compliance is nearer | D1, D4 | CM-TRU-014 |
| `SUB` | Subprocessors | security (confidentiality, accountability) | D1, D5 | CM-TRU-015 |
| `RET` | Retention and deletion | security (confidentiality); reliability (recoverability) for backups | D1, D3 | CM-TRU-016 |
| `ENC` | Protection of data in transit and at rest | security (confidentiality, integrity) | D1, D2 | `platform`; CM-TRU-018 for card data |
| `IDN` | Identity, sign-in and access | security (authenticity, accountability, non-repudiation, resistance) | D2 | CM-TRU-001, CM-TRU-002, CM-API-002, CM-CUS-010, CM-CUS-011, CM-STF-005 |
| `AUD` | Records of who did what | security (accountability, non-repudiation) | D2 | CM-TRU-003 |
| `ATT` | Attestations: certifications, audits, tests | evidence of security, and of what else it audits; not a characteristic itself | D1, D2, D3 | CM-TRU-018 for card data, CM-TRU-022 for security research; otherwise `platform` |
| `AVL` | Availability and continuity | reliability (availability, fault tolerance, recoverability) | D1, D5 | CM-OPS-001, CM-OPS-002 |
| `CAP` | Scale and speed | performance efficiency (time behaviour, capacity, resource utilization); flexibility (scalability) | D1, through the scale bands | CM-OPS-001, CM-OPS-003, CM-OPS-006 |
| `IFB` | Bounds on the interfaces | performance efficiency (capacity); compatibility (interoperability) | D5 | CM-API-005, CM-API-007, CM-API-008, CM-APP-005 |
| `STB` | Bounds on a store's own records | performance efficiency (capacity) | D1, D6 | the capability of the records bounded |
| `CHG` | Commitments on change | maintainability (modifiability); compatibility (interoperability) | D5 | CM-API-006 |
| `PRV` | Privacy commitments | security (confidentiality, accountability) | D1, D2 | CM-TRU-013, CM-TRU-007, CM-TRU-017 |
| `SUP` | Support commitments | none: a service's quality, not the product's (ISO/IEC 25019:2023 holds quality in use; a reading) | S | CM-ONB-003 |
| `ACS` | Accessibility | interaction capability (inclusivity) | S | `platform`, or the surface's capability |

**The asks,** and the words a platform may use for them. Search the words in every language your platform holds, with your platform's own terms where a guide or a held page gives them. B-extent: "A broken plural is another word, so search each Arabic term in its singular and its plural, with and without ال."
- **`ISO`:** `ISO-1` how one store's data is kept from another's; `ISO-2` how one store's load or failure is kept from another's; `ISO-3` whether a store can be hosted apart, on its own resources.
  - en: isolated, isolation, multi-tenant, tenant, pod, shard, partition, each store, separate database, dedicated, noisy neighbour, sandbox.
  - ar: عزل، معزول، معزولة، مستأجر، متعدد المستأجرين، بيئة مستقلة، خوادم مخصصة، قاعدة بيانات منفصلة.
- **`LOC`:** `LOC-1` where store data is hosted and processed (countries, regions, providers); `LOC-2` whether data leaves the merchant's or the buyer's country, and on what basis; `LOC-3` whether the location can be chosen, or differs by market or plan.
  - en: data center, hosted in, hosting, region, stored in, data residency, transfer, cross-border, outside the country, cloud, Google Cloud, AWS, Azure.
  - ar: مركز البيانات، مراكز البيانات، استضافة، مستضافة، تخزين البيانات، داخل المملكة، خارج المملكة، نقل البيانات عبر الحدود، الحوسبة السحابية، موقع البيانات.
- **`SUB`:** `SUB-1` the subprocessors: who, for what, where; `SUB-2` how a change in them is notified.
  - en: subprocessor, sub-processor, processor list, service providers, third parties we use, notification of new subprocessors.
  - ar: المعالج الفرعي، المعالجون الفرعيون، معالج البيانات، مقدمو الخدمات، مزودو الخدمة، الأطراف الثالثة.
- **`RET`:** `RET-1` how long store data is kept after the store closes, and when it is deleted; `RET-2` how long personal data, logs and backups are kept; `RET-3` how long records the platform says the law requires (orders, invoices, payments) are kept.
  - en: retain, retention, delete, deletion, after termination, after closure, within N days, backups.
  - ar: الاحتفاظ، مدة الاحتفاظ، حذف، إتلاف، بعد إغلاق المتجر، بعد إنهاء الاشتراك، نسخ احتياطية.
- **`ENC`:** `ENC-1` encryption in transit; `ENC-2` encryption at rest, and how card data is held (tokenized, never stored); `ENC-3` who holds the keys, where stated.
  - en: encrypted, encryption, TLS, SSL, HTTPS, AES, at rest, in transit, tokenized, tokenization.
  - ar: تشفير، مشفرة، مشفّر، شهادة SSL، اتصال آمن، الترميز، بيانات البطاقة.
- **`IDN`:** `IDN-1` the staff's sign-in: two-step, passkeys, single sign-on, password rules; `IDN-2` sessions: idle sign-out, devices, concurrent sign-ins; `IDN-3` apps' and partners' access: tokens, their lifetimes, scopes granted; `IDN-4` buyers' sign-in security; `IDN-5` the checks on the people behind a store: levels, attempts, documents.
  - en: two-step, two-factor, 2FA, passkey, SSO, SAML, password, session, sign out after, token expires, valid for, OAuth, verification, identity verification.
  - ar: التحقق بخطوتين، المصادقة الثنائية، رمز التحقق، كلمة المرور، تسجيل الخروج، الجلسة، مستوى الأمان، تسجيل الدخول الموحد، صلاحية الرمز، توثيق الهوية، نفاذ.
- **`AUD`:** `AUD-1` which admin actions are recorded, and for how long; `AUD-2` how the merchant reaches the record (export, API).
  - en: audit log, activity log, history, events, recorded, last N days.
  - ar: سجل النشاطات، سجل العمليات، سجل التغييرات، سجل الدخول، سجل الأحداث.
- **`ATT`:** `ATT-1` card data: PCI DSS, its level, scope and date; `ATT-2` information security: ISO/IEC 27001, SOC 2 or SOC 3, a national framework (such as the Saudi National Cybersecurity Authority's controls); `ATT-3` privacy: ISO/IEC 27701, a data privacy framework, binding corporate rules, a national registration; `ATT-4` security tests: penetration tests, scans, a bug bounty.
  - en: certified, certification, compliant, attestation, audit, report, SOC, ISO, PCI DSS, Level 1, assessment, penetration test, bug bounty.
  - ar: شهادة، معتمد، متوافق، الامتثال، تدقيق، الهيئة الوطنية للأمن السيبراني، ضوابط الأمن السيبراني، البنك المركزي السعودي، اختبار الاختراق.
- **`AVL`:** `AVL-1` the availability promised, with any credit; `AVL-2` the availability reported (a status page, a past uptime); `AVL-3` backups and recovery; `AVL-4` maintenance and how incidents are told.
  - en: uptime, availability, service level, SLA, 99.9%, status, incident, outage, downtime, backup, disaster recovery, maintenance.
  - ar: وقت التشغيل، نسبة التوفر، اتفاقية مستوى الخدمة، حالة الخدمة، انقطاع، عطل، نسخ احتياطي، استعادة، صيانة.
- **`CAP`:** `CAP-1` the scale stated (orders, transactions, requests at a peak); `CAP-2` the speed stated (page load, response time, a content network).
  - en: per minute, per second, peak, Black Friday, BFCM, transactions a day, milliseconds, fast, CDN, points of presence, unlimited bandwidth.
  - ar: معاملة في يوم، الذروة، سرعة، زمن الاستجابة، شبكة توصيل المحتوى، زوار غير محدودين.
- **`IFB`:** `IFB-1` request rate limits, by API and plan; `IFB-2` event delivery: timeouts, retries, when a subscription is switched off; `IFB-3` sizes and counts: a payload, a file, a page, a bulk operation, a query's cost; `IFB-4` limits on code the platform runs for apps (execution time, memory, size).
  - en: rate limit, requests per, throttled, 429, timeout, retry, retries, maximum size, MB, bulk, query cost, points, execution time.
  - ar: حد الطلبات، عدد الطلبات، معدل الطلبات، المهلة، إعادة المحاولة، حجم الملف، الحد الأقصى.
- **`STB`:** `STB-1` the most records of a kind a store may hold, stated as a system limit (products, variants, options, collections, customers, locations); `STB-2` the sizes of a store's files and media.
  - en: limit, maximum, up to, per product, per store, platform limits.
  - ar: الحد الأقصى، عدد المنتجات، عدد الخيارات، حجم الصورة، حتى.
- **`CHG`:** `CHG-1` how long an API version is supported, and how often one is released; `CHG-2` the notice given before a breaking change or a removal.
  - en: version, supported for, release schedule, deprecated, deprecation, breaking change, sunset, notice.
  - ar: إصدار، الإصدارات، إيقاف الدعم، إشعار مسبق، تغيير جذري، سجل التغييرات.
- **`PRV`:** `PRV-1` the time to notify a breach; `PRV-2` who answers a data subject's request, and within what time; `PRV-3` requests from governments and others, and any report of them.
  - en: breach, notify, without undue delay, within 72 hours, data subject, access request, government, law enforcement, transparency report.
  - ar: خرق البيانات، تسرب، إشعار، صاحب البيانات، طلب الوصول، الجهات الحكومية، الجهات القضائية، نظام حماية البيانات الشخصية.
- **`SUP`:** `SUP-1` support's channels, hours, languages and response times, by plan.
  - en: 24/7, support, response time, within, priority support, dedicated, languages.
  - ar: الدعم الفني، على مدار الساعة، وقت الاستجابة، خدمة العملاء، مدير حساب.
- **`ACS`:** `ACS-1` the accessibility claimed for the admin, checkout, storefront themes or apps: a WCAG level, a conformance report.
  - en: accessibility, accessible, WCAG, VPAT, conformance, screen reader.
  - ar: إمكانية الوصول، سهولة الوصول، ذوي الإعاقة، قارئ الشاشة.

## Where your platform states its qualities

Read the places your guides name first, then search. What follows is where the coordinator's survey found each kind of source, at the commits the part list names. It is a lead: what it says a file holds, you read in the file.
- **Shopify** (observed-sh):
  - trust and compliance: `structures/shopify/compliance-reports/` (the SOC 3 reports, the PCI DSS attestation of compliance, the ASV scans, page by page), and the shopify.com pages on security, PCI and the transparency reports, held in the `shopify-com-pages` fetch run;
  - legal terms: `structures/shopify/legal-documents/` (the terms, the data processing addendum, the processor list, the privacy policies, the cookie policy, the binding corporate rules, the government access policy), with `structures/shopify/shopify-legal-index/` and the subprocessor notification page;
  - status: `status-page`, a fetch archive only (run `20260930T080834Z-shopifystatus-api`), read with `warc_text.py`;
  - limits: shopify.dev's pages in its fetch runs, `/docs/api/usage/limits` among them; the API reference's own groups (`structures/shopify/admin-graphql-reference-nav/`); `dev-changelog` for changes to them;
  - the Help Center (`structures/shopify/help-center/`, English and Arabic) for sign-in, staff, sessions and data;
  - scale and speed: the pricing pages and Editions, whose entries the model already holds (`asks` prints them);
  - accessibility: the shopify.com accessibility pages and conformance reports, in the same fetch run;
  - engineering writing: `structures/shopify/engineering-blog/` (436 posts, with their dates and tags), `structures/shopify/embedded-videos/` (subtitles), and this repository's `evidence/shopify-engineering/` (E001 to E040). Search its titles and tags first; read a post only where its words bear on an ask.
- **Salla** (observed-sa):
  - legal terms: `structures/salla/com-policies/` (the usage agreement, the privacy policy, payments, shipping and the others) and `structures/salla/partners-legal/`, with this repository's captures of `partners.salla.com/legal/*`;
  - status: this repository's captures of `status.salla.sa` and `status.salla.com`;
  - limits and security for developers: docs.salla.dev (`structures/salla/docs-index/`, `docs-operations`, and this repository's captures of its `security.md` and `rate-limiting.md`);
  - help: `structures/salla/help-articles/{ar,en}/texts.jsonl`, every article;
  - the dashboard: `settings-center` and the dashboard's translations for sign-in and security settings; the partners portal's settings;
  - scale and speed: salla.com's pages (`com-llms` and the `com-pages` fetch run).
- **Zid** (other-product-class, and this repository):
  - legal terms: this repository's captures of `zid.sa/{en,ar}/legal/*` (terms, privacy policy, Zid Pay's terms for Saudi Arabia and Kuwait, shipping and logistics), the `zid-assurance` page, and other-product-class's run `20261028T190806Z-terms-pricing-sa-eg`;
  - help and docs: this repository's captures of help.zid.sa and docs.zid.sa, with their sitemaps and `llms.txt`. `zid/GAPS.md`: "Zid's other surfaces: help.zid.sa, docs.zid.sa, zid.sa ... not captured here; sharrwah-knowledge-map holds some of their pages";
  - the dashboard: `zid/structures/dashboard-locales/` (security levels, sessions), `store-plan-policies` (limits), `store-permissions`.
- **BigCommerce** (other-product-class, and this repository):
  - trust and compliance: the founder's saves of its company's Trust Center, `evidence/product-class/blocked-evidence-founder/bigcommerce/` (the page, and its documents: the ISO certificates, the statement of applicability, the data transfer papers, the PCI guide and others). `security.bigcommerce.com` answered 403 to this repository's capture;
  - legal terms: other-product-class's runs `20261029T024622Z-legal-pricing-docs` and `20261029T025119Z-fees-and-billing`, and `structures/contracting-entities`;
  - limits: this repository's captures of docs.bigcommerce.com (its rate limits, infrastructure hosting and PCI pages) and support.bigcommerce.com (its Platform Limits, PCI Compliance and Security and Privacy Settings articles);
  - scale and speed: bigcommerce.com's pages in this repository's captures.
- **WooCommerce** (other-product-class, the release, and this repository): the store is the merchant's own, so many kinds are its host's (`holder`, below).
  - the release at `/home/user/woocommerce-release/11.2.1/woocommerce/` for bounds the code sets (sessions, rate limiting of its Store API, logs' retention);
  - this repository's captures of woocommerce.com's docs (PCI DSS compliance, privacy, WooPayments' policies), developer.woocommerce.com (privacy, rate limiting, order storage) and Automattic's privacy and data processing pages;
  - other-product-class's `options` structure and the plugins' code (run `20261029T023950Z-plugin-code`).

`corpus_search.py` reads all of these for your platform, this repository's captures and the founder's saves among them, PDFs through their text (its header). The evidence map's table of the tools says what each misses.

## For each ask

1. **Read the ask** as `asks` prints it: its kind, its question, the model's rows already labelled as its kind, the default capabilities' cells, and the leads.
2. **Find where your platform would state it,** from the guides and the list above. Record in `read` the guides' rows, structures, runs and addresses that bear on it.
3. **Read the primary document first:** the terms, the data processing terms, a service level, a certificate or report, the developer docs' page on limits, the help article. Then the marketing and engineering pages.
4. **Name what is already held.** Where the model already holds the passage (`asks` prints its rows; a concern-map statement by `class_slice.py search`; a held entry by grepping `studies/class-model/held/<platform>/entries.tsv` and `entries-s2.tsv`), its id is your `source`, with `locator` and `quote` empty. Write a quote only for what neither holds.
5. **Write the passage that states the value most plainly, in the platform's own primary document, then stop.** Add a passage only for a value, a scope (a plan, a market, an API), a date or a holder your rows don't show yet (ruling, proposed: `QL-R4`).
6. **Write the row,** by its outcome.

## The outcomes

- **`found`:** a held passage states the quality. Quote it in the platform's own words; `value` is the words of the quote that give the measure, the place, the party or the commitment.
- **`not-found`:** what is held was read and searched, and no passage states it. `PLAN.md`, section 6: "A 'searched, not found' lists what it read, at a commit." And Stage 0's rule for the checkers: "An index or a sitemap doesn't count, and a held corpus left unsearched rules that kind out."
- **`not-held`:** as `not-found`, and the place where your platform would state it isn't held: a ledger's `not attempted` or `not opened`, a sitemap entry not captured, a `GAPS.md` row, or a held page's link to a page not held. That such a page would state it is an assumption: say so. `capture` and `could_change` follow.
- **`absent`:** "Absence counts only from a complete list the platform publishes, such as an enumerated schema or a full plan table. Otherwise it is a gap" (`PLAN.md`, section 6, the test form, step 2). A complete list the platform publishes leaves it out, such as a compliance page that lists its reports, or the platform states it doesn't do it. Cite the list as for `found`, and say in `reading` what makes it complete in the platform's words, as a reading.
- **`unreadable`:** the place is held only in a form the tools can't read, such as an archive not in git or a capture that answered 403. `capture` names the file and where it is held.
- **`unclear`:** a passage may state the quality, but its words don't settle it. Cite it as for `found`, and say in `capture` what would settle it.

**An ask's rows** are one or more `found` rows, or exactly one row of another outcome.

**`could_change`,** on `not-held`, `unreadable` and `unclear`: one or more of `D1` to `D6`, `;`-separated, where the quality could change that first decision of `architecture/plan.md`, section 3 (the kind's row in the checklist names which it drives), `S` where it would only change a quality scenario, or `no`. Say why in `reading`. The coordinator writes a capture request only for `D1` to `D6` (ruling, proposed: `QL-R6`). `PLAN.md`, Stage 4A: "What isn't held becomes a capture request only where it could change an architecture decision."

**`capture`,** for `not-held`: `<repository>; <instrument, from index/instruments.json, or none>; <the run: a fetch of the named addresses, a journey unit by its ledger id, or the GAPS.md row, quoted>; stop at <...>; needs: <what only the founder can give, or nothing>`. Write `none: <why>` only where no run can capture it at all, such as a document the platform gives only on request or under contract: the coordinator then names what to ask the platform, through the founder (`PLAN.md`, section 6: "Where documents can't settle a question, it goes to the platforms, partners, regulators or a lawyer, through the founder").

## Which capability, or the platform as a whole

`PLAN.md`: "Each quality is quoted at its commit, on the capability it bears on." A `found` row's `cap_id` is the narrowest capability whose definition names the thing the quality measures, read from the capability's own definition and note (`class_slice.py caps --terms`, `held_entries.py cells`). The checklist's last column gives the default. Where the quality's words cover the whole platform or all of a store's data, `cap_id` is `platform` (ruling, proposed: `QL-R2`). For example, a retention rule for one record (a log) goes on its capability; a data processing addendum's deletion of all store data goes on CM-TRU-016; an ISO/IEC 27001 certificate of the company goes on `platform`.

A quality never makes a capability. Where a quality bears on a thing no capability holds, write `platform`, and name the thing in your notes.

**`holder`,** on `found` rows: who the statement says holds the quality:
- `platform`: the platform's company;
- `own-service`: a separate service of the platform's company or group, by B-extent's definition;
- `third-party`: a named third party, such as a payment company's certification or a cloud's region;
- `merchant`: the statement leaves it to the merchant or the merchant's host. B-extent: "A statement that makes the merchant or buyer responsible is `shows`, never `outside`"; here, it is a `found` row with `holder` `merchant` (ruling, proposed: `QL-R7`). WooCommerce's hosting is the usual case.

**This pass places nothing.** It records qualities, not where a platform puts a capability. Where a passage would change what a cell is placed as (a support value the cell lacks), name it in your notes with its source, for the final review (ruling, proposed: `QL-R8`).

## The row

`studies/class-model/qualities/<platform>/<part>.tsv`: tab-separated, with a header row, no quoting, no double quote (`"`), and no tab or newline inside a field. Lists are `;`-separated. Its columns:
- `subject`: the ask's code, such as `LOC-1`. A quality you meet that no ask names takes the kind's code alone, such as `IFB`.
- `outcome`: `found`, `not-found`, `not-held`, `absent`, `unreadable` or `unclear`.
- `kind`: the kind's code. `form`: `commitment`, `bound`, `attestation` or `data-keeping`. `basis`: `promised`, `enforced`, `reported` or `attested`. All three on `found` rows; `kind` on every row.
- `cap_id`: on `found` rows, a cap_id of `merged/capabilities.tsv` or `platform`; otherwise empty.
- `holder`: on `found` rows.
- `quality`: on `found` rows, what is measured, in a few words, in the platform's term where it gives one: no colon, no mark of inclusion.
- `value`: on `found` rows, the quote's own words that state the measure, verbatim, as a part of `quote` (or of the held id's text).
- `source`, `locator`, `quote`: on `found`, `absent` and `unclear` (below). For an id already held, `source` is the id, and `locator` and `quote` are empty.
- `identifier`: the document's or page's title, the API's name, or the item's id.
- `date`: the source's own date where it states one (a revision date, a report's period, a post's date), in its words; otherwise empty.
- `scope`: by H-held.md's rule 5, `scope`: "the plan, country, market, store or account the entry or its sources state it for, in their words, or empty". An API or a surface the quality is stated for goes here too.
- `source_type`: the seed's code for the source (`studies/class-model/seed/km-source-types.tsv`): `DECL` for the platform's docs, terms, help and pages; `SHIP` for its code; `OBS` for what a run observed; `LIT` for its engineering writing. A certificate or an auditor's report the platform publishes is `DECL`, with its issuer in `reading`.
- `read`: on every row but `found`: the guides' rows and the documents you read, `;`-separated. On a `found` row, what led you to it.
- `searched`: on every row but `found`: each search as `<tool> <language>: <terms>`, `;`-separated. A search that printed nothing is recorded as `nothing`.
- `capture`, `could_change`: as above.
- `reading`: a reading, marked as one: why the passage states the quality, and why its `form`, `basis`, `cap_id` and `holder`; or what you read and why it doesn't state it. A quote in single quotes is copied exactly from the passage or a file the reading names.

**Engineering writing and marketing pages** are the platform's own account. Record them with their `date` and `source_type`, and where a primary document of the same platform states another value for the same thing, write both, and say in `reading` which is the commitment (ruling, proposed: `QL-R5`). Never settle which holds now from what you know.

## Sources and locators

- **A held file:** `<repository>@<commit>:<path>`, at the commit your message names, with `line N` as `locator`: the line where the quote begins. A structure's `items.jsonl` is cited at its line.
- **A record of a fetch archive:** `<repository>@<commit>:<the archive's file, as fetch.cdx or corpus_search.py names it>`, with the record's offset as `locator`.
- **A page this repository captured, or a founder's save:** `sharrwah-knowledge-map@<commit>:<path>`, the path as `corpus_search.py` prints it, with `line N` of the text `quote_check.py --text` prints for it (for a PDF, its text).
- **WooCommerce's release:** `woocommerce-11.2.1:<path>`, the path inside `/home/user/woocommerce-release/11.2.1/woocommerce/`, with `line N`.
- **The repository is your platform's:** observed-sh for Shopify, observed-sa for Salla, `other-product-class@<commit>:<platform>/...` for Zid, BigCommerce and WooCommerce, the release for WooCommerce, and this repository's captures of your platform's hosts and its saves.
- **The quote** is verbatim, as held: the shortest whole part that states the quality, such as a sentence, a table row with its heading, or a list item with the heading it sits under. `corpus_search.py`, its header: "Snippets are folded for matching (case, diacritics, letter forms): never quote one; quote the document." Test each quote with `quote_check.py SOURCE LOCATOR TEXT` before you write it.

## Rules

- Every claim is one of three (`PLAN.md`, section 6):
  - a fact traced to its source at a commit;
  - a reading, marked as one;
  - an assumption, marked as one.
- The founder's words are never evidence of what a platform does.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence.
- observed-sh, observed-sa and other-product-class are read-only: never write, commit or push to them.
- Run Python with `python3 -I`.
- Don't change the model's files, the held pass's files, Q3's or the subjects'. Write only your part's two files, and make no commits.
- Nothing gets settled that the evidence didn't settle. Never state a quality from what you know of the platform. Where you can't tell, write `unclear`, with what would settle it.

## How to work, keeping your context small

Your context should stay under about 200,000 tokens.
- **Read once, at the start:** the evidence map, the guides and your asks.
- **Work kind by kind.** Decide a kind's asks and write its rows in one write before the next kind.
- **Search a kind at once:** one `corpus_search.py --brief` per language with all the kind's words in one call, its output written to a file in your folder. Read the file's first 80 lines and its last line, and grep the rest. For Shopify and Salla, run `--runs-only` first.
- **Read a long document in parts,** with `quote_check.py --text`, `grep -n` or `sed -n`, never whole. A legal document is read by its headings first.
- **Make your lookups together.** Each turn re-reads your whole context.
- **Keep your working files in a folder of your own,** named for your part, inside the scratchpad directory your system prompt names (such as `<scratchpad>/QL-SA/`), never in its root.
- **When your context passes about 200,000 tokens,** finish the kind, write it, and stop. Report the asks left (`asks --part <part> --left`): a fresh agent continues from your file.

## Output, in `studies/class-model/qualities/<platform>/`

- **`<part>.tsv`:** the rows.
- **`<part>.md`,** your notes:
  - its first line, the commits you read: `observed-sh@<c>`, `observed-sa@<c>`, `other-product-class@<c>`, `sharrwah-knowledge-map@<c>` and `woocommerce-11.2.1`, as your message names them;
  - the guides you read whole, and what you grepped;
  - for each kind, what your platform states, in two or three lines;
  - each capture lead whose `could_change` is `D1` to `D6`;
  - each quality on `platform` whose thing no capability holds;
  - what a passage states that would change a cell's placement (`QL-R8`);
  - problems with this brief or the scripts.

Check your part with `python3 -I method/ql_qualities.py check --part <part>` until it prints no problem. It tests every quote against its source at its locator, and every `value` inside its quote. Then read again each line it prints as `NOTE`.

## Report

Back to the coordinator:
- your rows' count by outcome, and the `found` rows by kind and by `cap_id` (`platform` among them);
- for D1 and D2's kinds (`ISO`, `LOC`, `SUB`, `RET`, `ENC`, `IDN`, `AUD`, `ATT`), what your platform states, in one line each;
- the capture leads whose `could_change` is `D1` to `D6`;
- any problem;
- the checker's final line.

## After the parts: the coordinator

The coordinator checks each part and runs `method/ql_qualities.py land --platform <p>`:
- each `found` row's quoted passage becomes a held entry (`held/<platform>/entries-s2.tsv`), so the model cites it as it cites the second stage's;
- a row on a capability becomes a quality placement in the batch `QL-<XX>`, which `held_entries.py check` checks and `held_amend.py apply` writes into the part that holds the cell;
- a row on `platform` becomes a row of `qualities/platform.tsv`;
- every landed row takes its label, kind and form in `qualities/labels.tsv`, and the other outcomes go to `qualities/outcomes.tsv`.

Then the parts are checked and merged again, the Knowledge Map's page shows the qualities by kind, and the capture leads the coordinator takes go to `handoffs/`.
