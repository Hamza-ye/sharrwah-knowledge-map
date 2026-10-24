# Notes: Q6 on Salla

## Selection

- 10 concerns were copied: SA-C-006, SA-C-110, SA-C-112, SA-C-164, SA-C-167, SA-C-170, SA-C-177, SA-C-230, SA-C-231 and SA-C-232. The script wrote 111 statements and 22 gaps.
- The other 60 rows, including S-01, are set aside, with their reasons in `selection.tsv`. No concern was added.

## What was read (all held, observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3)

### The help map

- `help_map.py salla` gave the categories.
- `f9tgx9usfvxntfgbbo7qet7g` (✨ متجر جديد) and `asqsa2licbq3qbaigkvepipo` (🛠️ تكتيكات في توثيق المتجر) gave their article lists.
- Help articles read in Arabic, from `structures/salla/help-articles/ar/texts.jsonl`:
  - `ya5z2fsehfy3ok1wei82jgr0`;
  - `huvvumstnafaadcw6abpol14`;
  - `i8d4lq5xfx3sr05m59uwh64d`;
  - `ig4b4l5hc542j4bcd2tp82bz`;
  - `itmpqrf58xz73g2yyxfnllbz`;
  - `ff6snmt0dx2w0j6ki594ik7l` (its first 45 lines);
  - `zbcnt9hu9kf8lfh2gmf1vccr`;
  - `evrib312myg7282hjg7nlrje` (its first 80 lines);
  - `brz9k255mdsfjeuty7ojte37`.
- Read only where they mention a place outside Saudi Arabia: `era3k5had61w2de5zacmb82w`, `wmmkc305vzb52ka2al4zbfrh` and `vnmcb3lad5fiwd7xnrmbteql`.
- Article dates are `last_update_at` from `help-articles/ar/items.jsonl`.

### Agreements and pages

- `structures/salla/com-policies/terms/text.txt` (the usage agreement): the introduction, the definitions, المادة الثانية to المادة الخامسة, and المادة السابعة عشرة.
- `raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz`, through `warc_text.py`:
  - at offset 3700206, https://salla.com/ar-ae/terms, compared line by line with the former;
  - at offset 14913731, https://salla.com/gcc-ecommerce;
  - at offset 2046921, https://salla.com/ar-ae/plans;
  - at offset 3261292, https://salla.com/ar-ae/salla-vs-shopify (only its FAQ lines).
- `raw/runs/20261005T235211Z-com-en-scheme/fetch.warc.gz` at offset 2987087, https://salla.com/en-sa/plans, as text and raw HTML.
- `structures/salla/com-plans/en-sa/text.txt`: its FAQ lines.

### Dashboard translations

- `structures/salla/dashboard-translations/{ar,en}/persona.json`, read whole.
- `{ar,en}/payments.json`, `ar/setup.json` and `ar/onboarding.json`: searched for country strings only.

### Corpus searches

The commands are given in `not-found.tsv`.

## Live pages

- https://salla.com/en-sa/plans, on 2026-10-19 through `method/capture/page_text.mjs`. It returned HTTP 403 with the title "Just a moment...", a bot challenge. It was not read, no language was served, and nothing from it is cited.
- No other live page was read.

## Couldn't read

The answers to the FAQ on the plans pages ("Can I use Salla outside Saudi Arabia?") are not in the held HTML or text of en-sa/plans or ar-ae/plans. The live page met a bot challenge (Q6-SA-N01).

## Copies

- None was found wrong.
- Q6-SA-K0084 is the first item of the entity list recorded in full as Q6-SA-026. The held text now reads "- فرد : وثيقة العمل الحر تابعه" where the copy has "- فرد: وثيقة العمل الحر  تابعه". The two differ in spacing only.

## Gaps

- Q6-SA-G0161 is closed by Q6-SA-023.
- Q6-SA-G0160 stays open. Its route page (gcc-ecommerce) was read, and Q6-SA-053 and Q6-SA-054 record what it holds.
- Q6-SA-G0213 stays open: no Kuwait version of the agreement was read.

## Problems with the method

- The usage agreement's المادة الرابعة refers to "المادة الأولى – أهلية التاجر القانونية". In the text read, that heading is المادة الثانية. This is recorded in the note to Q6-SA-015.
- The Kuwait store-creation article (i8d4lq5xfx3sr05m59uwh64d) carries the UAE sentence "وضّح حالة متطلباتك النظامية للبيع في الإمارات". It is cited as written (Q6-SA-005).
- The table "المستند المطلوب حسب نوع كيانك" gives "حساب شخصي باسم مالك المتجر" for a فرد (Q6-SA-030). The FAQ says a فرد may use "حساب شخصي أو تجاري" (Q6-SA-040). Both are recorded as written.

## Re-check against the observed runs, 19 October 2026

All reads at observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3.

### What was read

- The guides: `README.md` and `docs/READING.md`, whole.
- `index/rest-endpoints.tsv`, searched for payment, gateway, kyc and onboarding endpoints.
- Corpus searches (`python3 -I method/corpus_search.py salla …`):
  - "دولة المتجر" "متاحة حاليًا في السعودية" "خارج السعودية" "country_not_supported" "store country" "outside Saudi" --max 10 (no run document listed);
  - "دولة المتجر" "متاحة حاليًا في السعودية والإمارات" "Store country" "onboarding" "persona" --max 10;
  - "نسعد باهتمامك بالتسجيل" "We’re currently available in Saudi Arabia" "Other country" "دولة أخرى" "متاحة حاليًا في السعودية والإمارات فقط" --max 10;
  - "هل يمكنني استخدام سلة خارج السعودية" "Can I use Salla outside Saudi Arabia" "خارج السعودية" "outside Saudi Arabia" --max 10;
  - "supported_countries" "available_countries" "countries" "الدول المدعومة" --with "payment" "gateway" "sallapay" "مدفوعات" --max 10;
  - "admin/v2/gateways/payment" "kyc/api/kyc/schema" "عقد خدمات الدفع" --max 10;
  - "auth/register" "إنشاء متجر جديد" "سجل الآن" "Create your store" "Sign up" "الكيان القانوني" "legal entity" --max 10 (it listed translation files and customer-settings pages; none shows a seller's sign-up, none opened);
  - "اتفاقية الاستخدام" "سياسة الاستخدام" "أهلية التاجر" "usage agreement" "terms of use" "شركة منصة سلة" --with "الكويت" "الإمارات" "Kuwait" "UAE" --max 10.
- Run files read:
  - `raw/runs/20261008T133523Z-sweep-demo-store-en/`: `responses/5134.json` (persona-country), `responses/5171.json` (create-store), `responses/2518.json` (gateways/payment), `steps/134.text.txt`, `actions.jsonl` steps 71, 133 and 134, `responses.jsonl` (the lines of those files), `run.json` (`extra`);
  - `raw/runs/20261008T125139Z-sweep-merchant-routes-ar/`: `responses/0535.json`, `steps/024.text.txt`, `actions.jsonl` steps 23 to 25, `run.json` (it names no store);
  - `raw/runs/20261012T010906Z-sweep-real-merchant-full-en/`: `responses/1488.json` (gateways/payment), `responses.jsonl` and `actions.jsonl` for step 42;
  - `raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/1818.json` (kyc schema, 123 KB), searched for عقد, contract, country, دولة, agreement, اتفاقية, شركة, مواطن, السعود, Saudi, citizen, resident, مقيم, freelance;
  - `raw/runs/20261008T131847Z-sweep-merchant-routes-ar/responses/0344.json` and `raw/runs/20261008T133523Z-sweep-demo-store-en/responses/2513.json` (translation files), searched for the matched terms.
- Held pages re-read for the wording check: `structures/salla/com-plans/en-sa/text.txt` (line 247) and the fetch archive records at offsets 2046921 and 3261292 of `raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz`, through `warc_text.py`.
- `method/help_map.py salla`, its category list, for the names in Q6-SA-N04's route.
- `held_index.py` on https://s.salla.sa/persona/qna and https://s.salla.sa/auth/register: both "not held" (the question page is in the runs' step files, which the tool doesn't list).

### Open items

- Q6-SA-N01: unchanged. No run document shows the plans pages' answer. The search was added to `searched`.
- Q6-SA-N02: unchanged. The search and the two translation files opened were added.
- Q6-SA-N03: narrowed, by Q6-SA-059 and Q6-SA-060. The country question's options are now recorded. What follows the option "Other country" / دولة أخرى is still missing. The route now names the question page.
- Q6-SA-N04: narrowed, by Q6-SA-062. One store's payment methods answer carries `available_countries` for each method, empty for all. A per-country list is still missing.
- Q6-SA-G0162: narrowed, by Q6-SA-059 and Q6-SA-060. The country step's options are shown; what each choice connects to is not. The copy is not edited.
- Q6-SA-G0176 and Q6-SA-G0177: unchanged. The kyc schema answer (1818.json), the candidate their route names, holds no عقد or contract string in the terms searched.
- Q6-SA-G0160, Q6-SA-G0213 and Q6-SA-G0214: unchanged. No run document read shows them. The checkout translation file (0344.json) names "شركة منصة سلة للاتصالات وتقنية المعلومات" under `bank_owner_name` and "SALLA PLATFORM CIT COMPANY (SINGLE PERSON COMPANY)" under `bank_owner_name_ae`. These are names of a bank account's owner, not a party clause, so they were not recorded.
- No row closed. `not-found-closed.tsv` is not written.

### New statements

- Q6-SA-059 to Q6-SA-062, with citations Q6-SA-C077 to Q6-SA-C082. Quotes from JSON answers are given as `json.dumps(…, ensure_ascii=False)` prints them, which is the form the checker reads.

### Wording changes (step 4)

- Q6-SA-N01: both questions it gives are in what it reads: "Can I use Salla outside Saudi Arabia?" at line 247 of `com-plans/en-sa/text.txt`, and "هل يمكنني استخدام سلة خارج السعودية؟" in the ar-ae/plans record at offset 2046921 (the record's text, FAQ item 3). "هل أقدر أبيع خارج السعودية باستخدام سلة؟" is in the record at offset 3261292. No change.
- Q6-SA-N04: "(Salla Payments methods, shipping labels, instalment providers, bank transfer)" removed from `what_is_missing`. Nothing it reads shows that wording.
- Q6-SA-N04: in `route`, "تفعيل شركات الشحن بعقدك الخاص في الإمارات, - في الكويت" was replaced by the two subcategory names as the help map gives them, إنشاء متجر خارج السعودية and تفعيل الشحن للمتاجر خارج السعودية. The UAE title was not found as written. The Kuwait title ("تفعيل شركات الشحن بعقدك الخاص في الكويت | سلة") is held, and is not read.
- Q6-SA-N03: `route` rewritten to name the question page and the option "دولة أخرى / Other country", as the runs show them.

### Not read

- The same question page and gateways answer in the other sweep runs (merchant-en, merchant-menus-ar, public-demo-en). The `/persona/scrapper` steps.
- The `user/features` answers and the coupon and shipping pages the countries search listed.
- `raw/runs/20261012T045412Z-journey-real-merchant-details-en` step 012 (salla.com home page).

### Problems

- `run.json` of `20261008T125139Z-sweep-merchant-routes-ar` names no store, and the search lists it as "store -". Q6-SA-060's scope says so.
- `held_index.py` reports s.salla.sa/persona/qna as not held, though the runs' step files hold it.
