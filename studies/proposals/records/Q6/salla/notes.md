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
