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
