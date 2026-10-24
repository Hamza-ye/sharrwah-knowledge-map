# Notes · Q3 · Salla

## What was read

All reading was of held material at observed-sa `4ca2e896a729215f422a137a364e7e9488610ba3`. No live page was read.

Help centre articles, through `method/help_map.py salla page`, in Arabic unless marked:

- From the map's categories ✨ متجر جديد and 🛠️ تكتيكات في توثيق المتجر, for sentences [1]–[4], 10 pages: ig4b4l5hc542j4bcd2tp82bz, zbcnt9hu9kf8lfh2gmf1vccr, evrib312myg7282hjg7nlrje, ndz1k0tts5p7gfnqqxcubspl, zgflevdt56pvfugbbnnkzr06, g0cbvwqncrfmptexs580y6f7, v6ymzcrb4i7euybyuta4cfad and poppbr8akg1iqlr2798u8gfz. From the category 🗂️ تكتيكات في قطاعات التجار: c7kvq9bm0bxjtef4yf5us13q (pharmacies) and q70uv78qn8jm2wuxf8305qy4 (gold; added nothing).
- From the corpus searches: pvoh9k11k2sjti6k1xu667e5 (Mahally), l751qim50vlfzr5z2b8r8vzg (en, Salla Capital FAQ), wmmkc305vzb52ka2al4zbfrh (Tabby, UAE), cezia1wnc93ng3c75e90ll74 (ZATCA, ar; the en version was opened first), itmpqrf58xz73g2yyxfnllbz (UAE verification) and iparbtoxqor7rjnuhg9ppnrh (older copy of the verification FAQ, for Q3-SA-N01).

Held structures and fetch records:

- `structures/salla/com-policies/terms/text.txt`: the usage agreement, Articles 2, 4, 5, 8, 10, 20 and 22.
- `structures/salla/com-policies/policies-selling/text.txt`: the selling policy.
- `structures/salla/kyc-schema/demo@en/source.json`: the GET `/kyc/api/kyc/schema` response from the demo store, captured 2026-10-08. Its `renderer_schema.id` is `merchants_saudi_kyc`.
- `raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz` at offset 12898484: https://salla.com/souq-eljomla. Copied gap Q3-SA-G0103 lists this page as held but not read. It was read here for the joining conditions, not for G0103's subject.
- `raw/runs/20261008T121631Z-com-pages/fetch.warc.gz` at offsets 64784169 (https://salla.com/en-sa/blog/ecommerce-for-pharmacies) and 65748829 (https://salla.com/en-sa/blog/online-store-license-saudi-arabia).

Corpus searches run (each with `--max 10`):

- prohibited products;
- activation and joining requirements;
- the verification period;
- products requiring a licence;
- selling-policy checks;
- store verification with الإمارات / UAE.

The not-found rows give the exact commands.

## What wasn't read

- The KYC schema holds only the Saudi workflow (`merchants_saudi_kyc`). The verification form for other countries is not held. The UAE article was read instead.
- The KYC schema has no state or text that names عقد خدمات الدفع or a contract: no match for `عقد` or `contract` in the decoded translations. Where the contract is presented stays open as copied gap Q3-SA-G0176. This records what the held schema contains. The schema is a demo store's response at its first state (`current_state` `kyc_requirements_preview`).
- Not opened because their titles or snippets didn't bear on the question: the other documents that each search listed, named in not-found.tsv.

## Copies

- No copy was found wrong.
- Q3-SA-K0084 copies only the individual (فرد) row of the entity list. Q3-SA-014 records the whole table from another article.
- Q3-SA-K1450 copies only the Mahally terms condition. Q3-SA-061 records the full list of conditions.
- Help article zgflevdt56pvfugbbnnkzr06 lists the e-payment requirements with the plans "سلة بلس" or "سلة برو". The copy Q3-SA-P0060 names "بلس أو برو أو سبيشال". Nothing was recorded from zgflevdt56pvfugbbnnkzr06 on this point, since the copy already says it.

## Problems with the method

- The checker requires a statement to appear verbatim in its first cited source, after collapsing whitespace. A list whose items are not consecutive lines in the source, or a table recorded with added separators, fails that check. Such statements were split into one statement per passage: Q3-SA-006/007, Q3-SA-019/020 and Q3-SA-063 to 065.
- Pages held only in observed-sa fetch archives are reported as "unresolved; not captured" when cited by URL. They were cited by archive path and offset instead, as the brief's rule for fetch archives gives.
- The KYC schema stores its Arabic strings as `\u` escapes. Quotes from it use the English values, which appear verbatim.
- `held_index.py` reports help.salla.sa as held, as `structures/salla/help-self-descriptions/link-header`. So the checker refuses a founder route that names help.salla.sa's support page. The route in Q3-SA-N02 names only the dashboard help.
- The English ZATCA article (cezia1wnc93ng3c75e90ll74, en) carries an editor's bracket "[Verify: ...]" inside a requirement. The Arabic version was quoted instead.

## Re-check against the observed runs, 19 October 2026

### What was read

- observed-sa `4ca2e896a729215f422a137a364e7e9488610ba3`: `README.md` and `docs/READING.md`, whole.
- Corpus searches (each with `--max 10`), in Arabic and English as alternatives in one call:
  - `"المهلة" "مهلة" "توثيق المتجر" "grace period" "verify your store"` (Q3-SA-N01; sentences [1] and [4]);
  - `"عقد خدمات الدفع" "عقد" "اتفاقية الاستخدام" "payment services contract" "contract" "agreement"`, then the narrower `"عقد خدمات الدفع" "اتفاقية خدمات الدفع" "payment services agreement" "payment services contract"` (Q3-SA-G0009, G0176, G0177, G0179, H0002). The narrower search listed no run document;
  - `"تتطلب ترخيص" "رخصة" "ترخيص" "license" "licence" "permit"` (Q3-SA-N02; sentence [2]);
  - `"المخالفات" "مخالفة" "سياسة البيع" "violation" "violations" "selling policy"` (Q3-SA-N03);
  - `"يشترط" "يجب توثيق" "يلزم توثيق" "store_documents_required" "requires_paid_plan" "blocks_payment_activation"` (sentences [1] and [2]);
  - `"قيد المراجعة" "مرفوض" "تعليق المتجر" "إيقاف متجرك" "under review" "suspended" "rejection"` (sentence [4]). It listed partner-portal, ads, Salla Point and ticket statuses; none was opened.
- Run files opened (all at the commit above, under `raw/runs/`):
  - `20261008T122729Z-sweep-merchant-menus-ar`: `run.json`, `actions.jsonl` (steps 70 to 78), `responses.jsonl` (steps 71 to 77), `steps/076.text.txt` (`/payments/kyc`), `responses/1683.json` (gateways), `responses/1722.json` (wallet summary), `responses/1818.json` (KYC schema; searched only, for عقد, contract, مهلة, grace, period and deadline, with no match);
  - `20261012T010906Z-sweep-real-merchant-full-en`: `run.json`, `actions.jsonl` (steps 17, 42, 55 to 66), `responses.jsonl`, `steps/063.text.txt` (`/payments/kyc`; the page shows "Access restricted", so it holds no verification content), `responses/1488.json` (gateways), `responses/0614.json` (wallet summary), `responses/0029.json` (post-onboarding missions; nothing recorded);
  - `20261008T125139Z-sweep-merchant-routes-ar`: `run.json`, `actions.jsonl` (steps 22 to 25, 37), `responses.jsonl`, `steps/023.text.txt` and `024.text.txt` (`/persona/qna`), `steps/026.text.txt` (plan choice; nothing recorded, the plans are in the copies), `responses/0535.json` (persona-country), `responses/0529.json` (onboarding status), `responses/0576.json` (create-store activities; nothing recorded), `responses/0709.json` (store info);
  - `20261008T131847Z-sweep-merchant-routes-ar`: `run.json`, `actions.jsonl` (step 14), `responses/0344.json` (checkout translations).
- `method/held_index.py` on https://s.salla.sa/manage/violation (not held), https://s.salla.sa/payments/kyc (held in four runs' steps), https://s.salla.sa/entity/verification/verify (not held) and https://s.salla.sa/persona/qna (held).

### New statements

Q3-SA-073 to Q3-SA-088, cited by Q3-SA-C158 to Q3-SA-C197. JSON statements and quotes are copied in the form the checker decodes (`\u` escapes decoded, keys and values kept).
- Run `20261008T125139Z-sweep-merchant-routes-ar` names no store in `run.json` `extra`. Its store is named from the run's own `GET /admin/v2/store/info` answer (`responses/0709.json`, step 37): "Store 1", "plan": "basic", "kyc_country": "SA". That file is cited for Q3-SA-084 to Q3-SA-087.
- The plan in the scope of the merchant store's statements is the word the same store's page shows beside the account name (`steps/076.text.txt`: "بيسك"); for real-merchant, `steps/063.text.txt` ("Pro").
- Lists recorded in full: `quick_methods` (4 items) and `online_payment_gateways` (1 item) of each gateways answer read, and the onboarding `steps` (13 items).

### Open items

- Q3-SA-N01: unchanged. The verification page of an unverified store, which its route asked for, is held (run `20261008T122729Z-sweep-merchant-menus-ar`, step 76) and was read: it shows no period. The route now names only the question to merchant support. `read` and `searched` extended.
- Q3-SA-N02: unchanged; `searched` extended.
- Q3-SA-N03: unchanged; `searched` extended. `/manage/violation` is not held.
- Q3-SA-G0009: unchanged. No run document names the usage agreement beyond a footer link in a Salla e-mail.
- Q3-SA-G0176, Q3-SA-G0177, Q3-SA-G0179: unchanged. No run document holds عقد خدمات الدفع; the verification page held is its first screen (requirements), and the merchant store's KYC schema answer has no match for عقد or contract.
- Q3-SA-H0002: unchanged. The gateways answers label Salla's own gateway (`"slug": "salla"`) "noon" (Q3-SA-075, Q3-SA-080); they don't say who holds the funds.
- No row closed, so no `not-found-closed.tsv` was written.

### Wording changes (step 4)

- Q3-SA-N01's route: the address https://s.salla.sa/payments/kyc and the capture request were removed, since a run holds the page. No other change: `method/check_not_found_wording.py Q3 --platform salla` reports no phrase missing from what the rows read.

### Not read

- The other run documents the searches listed (their headings and snippets are in the searches' output), including the English KYC pages (runs `20261008T141131Z-sweep-merchant-en` step 78, `20261008T133523Z-sweep-demo-store-en` step 76), the demo and public-demo stores' gateways and wallet answers, and `derived/state-gates.tsv`.

### Problems

- The corpus search lists published material and run documents together, with `--max 10` per corpus; the runs' documents are found only by reading past the help-centre results.
- The checker ran with no issues after the route of Q3-SA-N01 was changed: its first version kept the held address and was reported.
